---
url: https://developers.cloudflare.com/changelog/post/2026-04-13-containers-sandbox-ga/
title: Containers and Sandboxes are now generally available \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:40.722195+00:00
---

# Containers and Sandboxes are now generally available · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-13-containers-sandbox-ga/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 13, 2026

## Containers and Sandboxes are now generally available

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare [Containers](https://developers.cloudflare.com/containers/) and [Sandboxes](https://developers.cloudflare.com/sandbox/) are now generally available.

Containers let you run more workloads on the Workers platform, including resource-intensive applications, different languages, and CLI tools that need full Linux environments.

Since the initial launch of Containers, there have been significant improvements to Containers' performance, stability, and feature set. Some highlights include:

  * [Higher limits](https://developers.cloudflare.com/changelog/post/2026-02-25-higher-container-resource-limits/) allow you to run thousands of containers concurrently.
  * [Active-CPU pricing](https://developers.cloudflare.com/changelog/post/2025-11-21-new-cpu-pricing/) means that you only pay for used CPU cycles.
  * [Easy connections to Workers and other bindings](https://developers.cloudflare.com/changelog/post/2026-03-26-outbound-workers/) via hostnames help you extend your Containers with additional functionality.
  * [Docker Hub support](https://developers.cloudflare.com/changelog/post/2026-03-24-docker-hub-images/) makes it easy to use your existing images and registries.
  * [SSH support](https://developers.cloudflare.com/changelog/post/2026-03-12-ssh-support/) helps you access and debug issues in live containers.



The [Sandbox SDK](https://developers.cloudflare.com/sandbox/) provides isolated environments for running untrusted code securely, with a simple TypeScript API for executing commands, managing files, and exposing services. This makes it easier to secure and manage your agents at scale. Some additions since launch include:

  * [Live preview URLs](https://developers.cloudflare.com/changelog/post/2025-08-05-sandbox-sdk-major-update/) so agents can run long-lived services and verify in-flight changes.
  * [Persistent code interpreters](https://developers.cloudflare.com/changelog/post/2025-08-05-sandbox-sdk-major-update/) for Python, JavaScript, and TypeScript, with rich structured outputs.
  * [Interactive PTY terminals](https://developers.cloudflare.com/changelog/post/2026-02-09-pty-terminal-support/) for real browser-based terminal access with multiple isolated shells per sandbox.
  * [Backup and restore APIs](https://developers.cloudflare.com/changelog/post/2026-02-23-sandbox-backup-restore-api/) to snapshot a workspace and quickly restore an agent's coding session without repeating expensive setup steps.
  * [Real-time filesystem watching](https://developers.cloudflare.com/changelog/post/2026-03-03-sandbox-watch-file-events/) so apps and agents can react immediately to file changes inside a sandbox.



For more information, refer to [Containers](https://developers.cloudflare.com/containers/) and [Sandbox SDK](https://developers.cloudflare.com/sandbox/) documentation.
