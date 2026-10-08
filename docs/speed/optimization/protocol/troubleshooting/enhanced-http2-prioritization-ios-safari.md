---
url: https://developers.cloudflare.com/speed/optimization/protocol/troubleshooting/enhanced-http2-prioritization-ios-safari/
title: Enhanced HTTP/2 Prioritization negatively affects iOS/Safari devices \u00b7 Cloudflare Speed docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:35.983065+00:00
---

# Enhanced HTTP/2 Prioritization negatively affects iOS/Safari devices · Cloudflare Speed docs

> Source: https://developers.cloudflare.com/speed/optimization/protocol/troubleshooting/enhanced-http2-prioritization-ios-safari/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Speed](https://developers.cloudflare.com/speed/)
  3. /…

SettingsProtocol optimization

  4. /Troubleshooting
  5. /Enhanced HTTP/2 Prioritization negatively affects iOS/Safari devices



# Enhanced HTTP/2 Prioritization negatively affects iOS/Safari devices

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/speed/optimization/protocol/troubleshooting/enhanced-http2-prioritization-ios-safari/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSolution

Occasionally, [Enhanced HTTP/2 Prioritization](https://developers.cloudflare.com/speed/optimization/protocol/enhanced-http2-prioritization/) can negatively affect the experience of visitors using Safari on macOS or any browser on iOS.

These visitors may notice not being able to load the site properly, such as images not displaying or content taking too long to load.

## Solution

If visitors using using Safari on macOS or any browser on iOS are experiencing issues with your site loading properly, try [disabling Enhanced HTTP/2 Prioritization](https://developers.cloudflare.com/speed/optimization/protocol/enhanced-http2-prioritization/#enable-enhanced-http2-prioritization).

Note

Sometimes, [HTTP/2](https://developers.cloudflare.com/speed/optimization/protocol/http2/) will cause **Enhanced HTTP/2 Prioritization** to be re-enabled automatically.

If you notice this happening, also disable **HTTP/2**.

[Previous0-RTT Connection Resumption](https://developers.cloudflare.com/speed/optimization/protocol/0-rtt-connection-resumption/)[NextTroubleshoot protocol issues](https://developers.cloudflare.com/speed/optimization/protocol/troubleshooting/protocol-troubleshooting/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/speed/optimization/protocol/troubleshooting/enhanced-http2-prioritization-ios-safari.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
