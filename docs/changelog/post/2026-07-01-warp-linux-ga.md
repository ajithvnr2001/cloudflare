---
url: https://developers.cloudflare.com/changelog/post/2026-07-01-warp-linux-ga/
title: Cloudflare One Client for Linux (version 2026.6.836.0) \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:35.598876+00:00
---

# Cloudflare One Client for Linux (version 2026.6.836.0) · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-01-warp-linux-ga/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 1, 2026

## Cloudflare One Client for Linux (version 2026.6.836.0)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

A new GA release for the Linux Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This package is the same release as 2026.6.822.0, with a fix for our RPM package. Previously the repository served a single build to every OS version, so an install could pull a dependency that isn't available on that release. The repository now serves the correct build for each operating system version, so installs automatically pull the dependencies that version requires. Debian and Ubuntu were not affected.

If you installed version 2026.6.822.0 on an RPM-based distribution, we recommend refreshing your repository configuration:
    
    
    sudo curl -fsSL https://pkg.cloudflareclient.com/cloudflare-warp-ascii.repo | sudo tee /etc/yum.repos.d/cloudflare-warp.repo
    sudo dnf clean all
    sudo dnf install cloudflare-warp
    
