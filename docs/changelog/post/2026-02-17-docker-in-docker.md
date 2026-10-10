---
url: https://developers.cloudflare.com/changelog/post/2026-02-17-docker-in-docker/
title: Docker-in-Docker support added to Containers and Sandboxes \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:43.618025+00:00
---

# Docker-in-Docker support added to Containers and Sandboxes · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-17-docker-in-docker/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 17, 2026

## Docker-in-Docker support added to Containers and Sandboxes

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Sandboxes](https://developers.cloudflare.com/sandbox/) and [Containers](https://developers.cloudflare.com/containers/) now support running Docker for "Docker-in-Docker" setups. This is particularly useful when your end users or [agents](https://developers.cloudflare.com/agents) want to run a full sandboxed development environment.

This allows you to:

  * Develop containerized applications with your Sandbox
  * Run isolated test environments for images
  * Build container images as part of CI/CD workflows
  * Deploy arbitrary images supplied at runtime within a container



For [Sandbox SDK](https://developers.cloudflare.com/sandbox/) users, see the [Docker-in-Docker guide](https://developers.cloudflare.com/sandbox/guides/docker-in-docker/) for instructions on combining Docker with the SandboxSDK. For general Containers usage, see the [Containers FAQ](https://developers.cloudflare.com/containers/faq/#can-i-run-docker-inside-a-container-docker-in-docker).
