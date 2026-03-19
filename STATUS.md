# Project Status

## Summary

This repository backs the personal website at ``www.alexmichel.org``.

The site is currently a minimal static GitHub Pages site with:

- a bare homepage
- a podcast feed under ``/podcast/feed.xml`` titled ``Sapientia Ducit``
- podcast artwork under ``/podcast/artwork/cover.png``
- published lecture MP3 episodes

## Publishing Setup

- Custom domain: ``www.alexmichel.org``
- GitHub Pages source branch: ``gh-pages``
- Site URL: ``https://www.alexmichel.org/``

The repository also has a ``master`` branch, but the live site is published from ``gh-pages``.

## Current Site Contents

- ``index.html``: minimal homepage stating that this is the personal site of Alexander Michel
- ``podcast/feed.xml``: RSS feed for ``Sapientia Ducit``
- ``podcast/index.html``: simple landing page for the podcast feed with the current artwork
- ``podcast/artwork/cover.png``: current square podcast artwork image
- ``podcast/artwork/open-book-source.png``: downloaded source raster for the current artwork
- ``podcast/episodes/neural-networks-deep-learning-pytorch.mp3``: published lecture audio file
- ``podcast/episodes/slurm.mp3``: published lecture audio file
- ``CNAME``: custom domain configuration for GitHub Pages

## Current Podcast Episodes

- Feed title: ``Sapientia Ducit``
- Feed description: ``Audio lectures and notes for thinking things through.``
- Title: ``Neural Networks, Deep Learning, and PyTorch``
- Title: ``Cluster Computing with Slurm: Jobs, Resources, Scheduling, and Performance``
- Feed URL: ``https://www.alexmichel.org/podcast/feed.xml``
- Audio URL: ``https://www.alexmichel.org/podcast/episodes/neural-networks-deep-learning-pytorch.mp3``
- Audio URL: ``https://www.alexmichel.org/podcast/episodes/slurm.mp3``

## Notes

- If future edits should affect the live site immediately, they need to be committed and pushed on ``gh-pages`` unless the GitHub Pages source is changed in repository settings.
- The ``master`` branch currently contains similar content, but it is not the live publishing branch.
