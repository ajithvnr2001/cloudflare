---
url: https://developers.cloudflare.com/ssl/keyless-ssl/glossary/
title: Glossary \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:41.676170+00:00
---

# Glossary · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/keyless-ssl/glossary/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /[Keyless SSL](https://developers.cloudflare.com/ssl/keyless-ssl/)
  4. /Glossary



# Glossary

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/keyless-ssl/glossary/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCloudflare Keyless SSL key server (“key server”)Cloudflare Keyless SSL client (“keyless client”)

## Cloudflare Keyless SSL key server (“key server”)

The key server is a daemon that you run on your own infrastructure. The key server receives inbound requests from Cloudflare's keyless client on TCP port `2407` (by default) so you must make sure that your firewall and other access control lists permit these requests from [Cloudflare's IP ranges ↗︎](https://www.cloudflare.com/ips/).

Your key servers are contacted by Cloudflare during the TLS handshake process and must be online to terminate new TLS connections. Existing sessions can be resumed using unexpired TLS session tickets without needing to contact the key server.

## Cloudflare Keyless SSL client (“keyless client”)

The keyless client is a process that runs on Cloudflare's infrastructure. The keyless client makes outbound requests to your key server on TCP port `2407` for assistance in establishing new TLS sessions.

[PreviousKeyless delegation](https://developers.cloudflare.com/ssl/keyless-ssl/reference/keyless-delegation/)[NextTroubleshooting](https://developers.cloudflare.com/ssl/keyless-ssl/troubleshooting/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/keyless-ssl/glossary.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
