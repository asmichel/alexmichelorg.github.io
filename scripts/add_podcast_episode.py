#!/usr/bin/env python3

import argparse
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
import xml.etree.ElementTree as ET


REPO_ROOT = Path(__file__).resolve().parent.parent
FEED_PATH = REPO_ROOT / "podcast" / "feed.xml"
EPISODES_DIR = REPO_ROOT / "podcast" / "episodes"
SITE_BASE = "https://www.alexmichel.org"
ITUNES_NS = "http://www.itunes.com/dtds/podcast-1.0.dtd"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy an MP3 into the podcast directory and add it to the RSS feed."
    )
    parser.add_argument("source", help="Path to the source MP3 file")
    parser.add_argument("title", help="Episode title")
    parser.add_argument("description", help="One-line episode description")
    parser.add_argument(
        "--slug",
        help="Output filename slug without extension; defaults to a slugified title",
    )
    parser.add_argument(
        "--pub-date",
        help="RFC 2822 date in GMT; defaults to the current UTC time",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the destination path and feed metadata without changing files",
    )
    return parser.parse_args()


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    if not slug:
        raise ValueError("could not derive a filename slug from the provided title")
    return slug


def format_pub_date(raw_value: str | None) -> str:
    if raw_value:
        return raw_value
    return datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")


def indent(elem: ET.Element, level: int = 0) -> None:
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for child in elem:
            indent(child, level + 1)
        if not elem[-1].tail or not elem[-1].tail.strip():
            elem[-1].tail = i
    elif not elem.tail or not elem.tail.strip():
        elem.tail = i


def register_namespaces() -> None:
    ET.register_namespace("itunes", ITUNES_NS)


def find_channel(root: ET.Element) -> ET.Element:
    channel = root.find("channel")
    if channel is None:
        raise ValueError(f"no channel element found in {FEED_PATH}")
    return channel


def build_item(title: str, description: str, url: str, length: int, pub_date: str) -> ET.Element:
    item = ET.Element("item")

    title_el = ET.SubElement(item, "title")
    title_el.text = title

    description_el = ET.SubElement(item, "description")
    description_el.text = description

    enclosure_el = ET.SubElement(item, "enclosure")
    enclosure_el.set("url", url)
    enclosure_el.set("length", str(length))
    enclosure_el.set("type", "audio/mpeg")

    guid_el = ET.SubElement(item, "guid")
    guid_el.text = url

    pub_date_el = ET.SubElement(item, "pubDate")
    pub_date_el.text = pub_date

    return item


def insert_item(channel: ET.Element, item: ET.Element) -> None:
    insert_at = 0
    for idx, child in enumerate(channel):
        if child.tag == "item":
            insert_at = idx
            break
    else:
        insert_at = len(channel)
    channel.insert(insert_at, item)


def main() -> int:
    args = parse_args()

    source = Path(args.source).expanduser().resolve()
    if not source.exists():
        print(f"source file not found: {source}", file=sys.stderr)
        return 1
    if source.suffix.lower() != ".mp3":
        print(f"source file must be an MP3: {source}", file=sys.stderr)
        return 1

    slug = args.slug or slugify(args.title)
    destination = EPISODES_DIR / f"{slug}.mp3"
    url = f"{SITE_BASE}/podcast/episodes/{destination.name}"
    pub_date = format_pub_date(args.pub_date)
    file_size = source.stat().st_size

    if args.dry_run:
        print(f"source: {source}")
        print(f"destination: {destination}")
        print(f"url: {url}")
        print(f"length: {file_size}")
        print(f"pubDate: {pub_date}")
        return 0

    if destination.exists() and destination.resolve() != source:
        print(f"destination already exists: {destination}", file=sys.stderr)
        return 1

    register_namespaces()
    tree = ET.parse(FEED_PATH)
    root = tree.getroot()
    channel = find_channel(root)

    existing_guids = {item.findtext("guid") for item in channel.findall("item")}
    if url in existing_guids:
        print(f"feed already contains an episode with URL: {url}", file=sys.stderr)
        return 1

    EPISODES_DIR.mkdir(parents=True, exist_ok=True)
    if destination.resolve() != source:
        shutil.copy2(source, destination)

    item = build_item(args.title, args.description, url, file_size, pub_date)
    insert_item(channel, item)
    indent(root)
    tree.write(FEED_PATH, encoding="utf-8", xml_declaration=True)

    print(f"added episode: {args.title}")
    print(f"file: {destination}")
    print(f"url: {url}")
    print(f"length: {file_size}")
    print(f"pubDate: {pub_date}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
