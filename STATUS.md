# Project Status

## Summary

This repository backs the personal website at ``www.alexmichel.org``.

The site is currently a minimal static GitHub Pages site with:

- a bare homepage
- a podcast feed under ``/podcast/feed.xml``
- a published lecture MP3 episode

## Publishing Setup

- Custom domain: ``www.alexmichel.org``
- GitHub Pages source branch: ``gh-pages``
- Site URL: ``https://www.alexmichel.org/``

The repository also has a ``master`` branch, but the live site is published from ``gh-pages``.

## Current Site Contents

- ``index.html``: minimal homepage stating that this is the personal site of Alexander Michel
- ``podcast/feed.xml``: RSS feed for personal audio uploads
- ``podcast/index.html``: simple pointer page for the podcast feed
- ``podcast/episodes/neural-networks-deep-learning-pytorch.mp3``: published lecture audio file
- ``CNAME``: custom domain configuration for GitHub Pages

## Current Podcast Episode

- Title: ``Neural Networks, Deep Learning, and PyTorch``
- Feed URL: ``https://www.alexmichel.org/podcast/feed.xml``
- Audio URL: ``https://www.alexmichel.org/podcast/episodes/neural-networks-deep-learning-pytorch.mp3``

## Recent Work

- Replaced the old placeholder homepage with a minimal static HTML page.
- Added a podcast feed and a feed index page.
- Published the lecture audio as a named MP3 episode instead of the earlier test file.
- Updated the live publishing branch by creating and pushing a real ``gh-pages`` branch, because GitHub Pages was configured to publish from ``gh-pages`` rather than ``master``.

## Notes

- If future edits should affect the live site immediately, they need to be committed and pushed on ``gh-pages`` unless the GitHub Pages source is changed in repository settings.
- The ``master`` branch currently contains similar content, but it is not the live publishing branch.
