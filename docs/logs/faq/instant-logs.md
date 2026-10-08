---
url: https://developers.cloudflare.com/logs/faq/instant-logs/
title: Instant Logs FAQ \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:09.394597+00:00
---

# Instant Logs FAQ · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/faq/instant-logs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /[Faq](https://developers.cloudflare.com/logs/faq/)
  4. /Instant Logs



# Instant Logs FAQ

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/faq/instant-logs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview I am getting an HTTP 301 when attempting to connect to my WebSocket. What can I do? I am getting an HTTP 429. What can I do? Why am I not receiving data? I am getting an error fetching my data. How can I solve this?

[❮ Back to FAQ](https://developers.cloudflare.com/logs/faq/)

### I am getting an HTTP 301 when attempting to connect to my WebSocket. What can I do?

Make sure you are using the `wss://` protocol when connecting to your WebSocket.

### I am getting an HTTP 429. What can I do?

Connection requests are rate limited. Try your request again after waiting a few minutes.

### Why am I not receiving data?

First, double-check if you have a filter defined. If you do, it may be too strict (or incorrect) which ends up dropping all your data.

If you are confident in your filter, check the sample rate you used when creating the session. For example, a sample of 100 means you will receive one log for every 100 requests to your zone.

Finally, make sure the destination is proxied through Cloudflare (also known as orange clouded). We cannot log your request if it does not go through Cloudflare's global network.

### I am getting an error fetching my data. How can I solve this?

Make sure you have the correct permissions. To use Instant Logs you need Super Administrator, Administrator, Log Share, or Log Share Reader permissions.

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/faq/instant-logs.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
