---
url: https://developers.cloudflare.com/rules/configuration-rules/response-body-inspection/
title: Response body inspection \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:47.921575+00:00
---

# Response body inspection · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/configuration-rules/response-body-inspection/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /[Configuration Rules](https://developers.cloudflare.com/rules/configuration-rules/)
  4. /Response body inspection



# Response body inspection

Last updated Oct 7, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/configuration-rules/response-body-inspection/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewFeatures that inspect response bodiesStreaming considerationsIsolate inspection issues

When no enabled feature needs response content, Cloudflare can send data to the client as it arrives. Some features inspect or change response content at the edge.

Inspection can hold part of a response at the edge. This may increase time to first byte (TTFB) or delay incremental delivery. The amount of data held depends on the feature and response.

## Features that inspect response bodies

Cloudflare features primarily inspect responses with a `Content-Type` of `text/html`. Some features change the body, while others only read it.

The following features can change HTML response bodies when turned on and applicable:

Feature | Body change  
---|---  
[AI Labyrinth](https://developers.cloudflare.com/bots/additional-configurations/ai-labyrinth/) | Adds invisible links for unauthorized AI crawlers  
[Always Online](https://developers.cloudflare.com/cache/how-to/always-online/) | Adds a banner to archived pages  
[Automatic HTTPS Rewrites](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/automatic-https-rewrites/) | Rewrites eligible HTTP links to HTTPS  
[Cloudflare challenge features](https://developers.cloudflare.com/cloudflare-challenges/) | Injects challenge scripts or returns challenge content  
[Cloudflare Fonts](https://developers.cloudflare.com/speed/optimization/content/fonts/) and [Automatic Platform Optimization](https://developers.cloudflare.com/automatic-platform-optimization/) | Rewrites Google Fonts references  
[Email Address Obfuscation](https://developers.cloudflare.com/waf/tools/scrape-shield/email-address-obfuscation/) | Obfuscates email addresses in page content  
[Markdown for Agents](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/) | Converts HTML to Markdown for eligible requests  
[Replace insecure JavaScript libraries](https://developers.cloudflare.com/waf/tools/replace-insecure-js-libraries/) | Rewrites supported insecure library URLs  
[Rocket Loader](https://developers.cloudflare.com/speed/optimization/content/rocket-loader/) | Changes script loading behavior  
[Web Analytics](https://developers.cloudflare.com/web-analytics/) | Injects the Real User Monitoring beacon  
  
When [Response Body Buffering](https://developers.cloudflare.com/rules/configuration-rules/settings/#response-body-buffering) is set to **None** , these features do not change the response body.

Security and AI features may also read HTML without changing it. [Prefetch URLs](https://developers.cloudflare.com/speed/optimization/content/prefetch-urls/) reads URL manifests served as `text/plain`.

This list excludes explicit rules that inspect response content. Review each rule separately when troubleshooting.

## Streaming considerations

Response body inspection most often affects progressive HTML and plain-text streams. It can affect other responses selected by explicit inspection rules. A client may receive data later or in larger groups than the origin sent it.

Set an accurate `Content-Type` at your origin. Do not serve streaming API responses as `text/html` or `text/plain` unless that media type is required.

The `Cache-Control: no-transform` response directive prevents body changes by supported features. It does not prevent read-only inspection. Refer to [Cache-Control directives](https://developers.cloudflare.com/cache/concepts/cache-control/#cache-control-directives) for other effects of this directive.

## Isolate inspection issues

If a response stops streaming after you proxy it through Cloudflare:

  1. Verify that the origin sends data incrementally without Cloudflare.
  2. Check the origin response's `Content-Type` and `Cache-Control` headers.
  3. Review features and rules that apply to the response path.
  4. Create a path-specific [Configuration Rule](https://developers.cloudflare.com/rules/configuration-rules/) that sets **Response Body Buffering** to **None**.
  5. Test the response again through Cloudflare.



The **None** setting streams the body without inspection. It can prevent security, optimization, and analytics features from working on matching responses. Use the narrowest matching expression possible.

For setting values and API configuration, refer to [Response Body Buffering](https://developers.cloudflare.com/rules/configuration-rules/settings/#response-body-buffering).

[PreviousAvailable settings](https://developers.cloudflare.com/rules/configuration-rules/settings/)[NextOverview](https://developers.cloudflare.com/rules/configuration-rules/examples/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/configuration-rules/response-body-inspection.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
