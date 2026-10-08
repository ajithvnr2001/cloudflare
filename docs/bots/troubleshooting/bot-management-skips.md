---
url: https://developers.cloudflare.com/bots/troubleshooting/bot-management-skips/
title: Bot Management skips \u00b7 Cloudflare bot solutions docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:35.074646+00:00
---

# Bot Management skips · Cloudflare bot solutions docs

> Source: https://developers.cloudflare.com/bots/troubleshooting/bot-management-skips/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Bots](https://developers.cloudflare.com/bots/)
  3. /Troubleshooting
  4. /Bot Management skips



# Bot Management skips

Last updated Apr 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/bots/troubleshooting/bot-management-skips/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCommon reasons for Bot Management to not score a request Requests to internal endpoints Purge requests Early hints cache requests

There are instances in which Bot Management does not run and certain fields, such as the [JA3/JA4 field](https://developers.cloudflare.com/bots/additional-configurations/ja3-ja4-fingerprint/), are not populated because it has been determined that running Bot Management would not be necessary.

Refer to [bot scores](https://developers.cloudflare.com/bots/concepts/bot-score/#not-computed) for more information about why a request is not scored.

## Common reasons for Bot Management to not score a request

### Requests to internal endpoints

Requests such as `/cdn-cgi/` are handled individually and will never receive a Bot Management score. Email Obfuscation, Web Analytics, Trace Requests, Challenge Pages, and JavaScript Detections do not receive bot scores. Refer to the table below for some examples of internal endpoints.

Route  
---  
`/cdn-cgi/rum`  
`/cdn-cgi/script_monitor/report`  
`/cdn-cgi/trace`  
`/cdn-cgi/challenge-platform/…`  
`/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js`  
  
### Purge requests

All HTTP purge requests will not receive a bot score.

### Early hints cache requests

Early hints cache requests will not receive a bot score.

[PreviousAccount Abuse Protection](https://developers.cloudflare.com/bots/account-abuse-protection/)[NextSuper Bot Fight Mode for WordPress](https://developers.cloudflare.com/bots/troubleshooting/wordpress-loopback-issue/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/bots/troubleshooting/bot-management-skips.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
