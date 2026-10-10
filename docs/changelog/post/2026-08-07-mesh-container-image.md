---
url: https://developers.cloudflare.com/changelog/post/2026-08-07-mesh-container-image/
title: Container image for Cloudflare Mesh \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:33.434953+00:00
---

# Container image for Cloudflare Mesh · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-07-mesh-container-image/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 7, 2026

## Container image for Cloudflare Mesh

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/) nodes can now run as Docker containers. The [`cloudflare/mesh` ↗︎](https://hub.docker.com/r/cloudflare/mesh) image is available on Docker Hub for Docker Compose, Kubernetes, and any OCI-compatible runtime — no host-level package installation required.

The image supports `amd64` and `arm64` architectures and includes built-in [source NAT](https://developers.cloudflare.com/mesh/guides/run-mesh-in-containers/#source-nat) so return traffic routes correctly without VPC route table changes.

#### Deployment patterns

  * **Docker Compose** — add a `cloudflare-mesh` service to your `compose.yaml` and connect your entire stack to a private network.
  * **Kubernetes StatefulSet** — deploy a standalone Mesh node with persistent registration state.
  * **Kubernetes sidecar** — add the Mesh image as a sidecar container in a Pod to connect an application to Cloudflare without application changes.
  * **CI/CD** — pull the image in a pipeline step, join the Mesh, run integration tests against private infrastructure, and tear down. The node disappears when the container exits.



For [high availability](https://developers.cloudflare.com/mesh/features/high-availability/), run multiple replicas with the same Mesh node token. Cloudflare operates replicas in active-passive mode with automatic failover.

[ Go to **Mesh** ↗ ](https://dash.cloudflare.com/?to=/:account/mesh)

For setup steps, runtime configuration, and deployment examples, refer to [Run Mesh in Docker / Kubernetes](https://developers.cloudflare.com/mesh/guides/run-mesh-in-containers/).
