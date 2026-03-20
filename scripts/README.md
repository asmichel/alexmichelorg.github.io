# Scripts

## ``add_podcast_episode.py``

Adds an MP3 to ``podcast/episodes/`` and inserts a matching ``<item>`` at the top of ``podcast/feed.xml``.

Example:

```sh
./scripts/add_podcast_episode.py ../path/to/example.mp3 "Example Title" "A short description."
```

Useful options:

- ``--slug`` to control the output filename
- ``--pub-date`` to override the generated GMT timestamp
- ``--dry-run`` to preview the destination path and metadata
