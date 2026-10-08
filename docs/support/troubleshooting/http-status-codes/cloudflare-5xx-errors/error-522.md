---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-522/
title: Error 522 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:58.911131+00:00
---

# Error 522 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-522/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[Cloudflare 5xx errors](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/)
  5. /Error 522



# Error 522

Last updated Jul 31, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-522/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewError 522: connection timed out Common causes Resolution Diagnose with Origin Analytics

## Error 522: connection timed out

Error `522` occurs when Cloudflare times out contacting the origin web server.

### Common causes

Two different timeouts cause HTTP error `522` depending on when they occur between Cloudflare and the origin web server:

  * Before a TCP connection is established, Cloudflare does not receive a SYN+ACK within 19 seconds after sending a SYN. The SYN retry backoff intervals are 1, 1, 1, 1, 1, 2, 4, and 8 seconds.
  * After the TCP connection is established, Cloudflare does not receive an acknowledgment (ACK) of its resource request within 90 seconds.



### Resolution

  * Contact your hosting provider and share the [error details](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/#required-error-details-for-hosting-provider) to assist in troubleshooting these common causes:

    * [Cloudflare IP addresses ↗︎](https://www.cloudflare.com/ips/) are rate limited or blocked in .htaccess, iptables, or firewalls. Confirm your hosting provider allows **all Cloudflare IP ranges** (most common cause). You can use a [Cloudflare WAF Custom Rule](https://developers.cloudflare.com/waf/custom-rules/use-cases/block-by-geographical-location/) if you need to restrict traffic from geographical locations.
    * An overloaded or offline origin web server drops incoming requests.
    * [Keepalives ↗︎](http://tldp.org/HOWTO/TCP-Keepalive-HOWTO/overview.html) are disabled at the origin web server.
    * The origin IP address in your Cloudflare **DNS** app does not match the IP address currently provisioned to your origin web server by your hosting provider.
    * Packets were dropped at your origin web server.
  * If you are using [Cloudflare Pages](https://developers.cloudflare.com/pages/), verify that you have a custom domain set up and that your CNAME record is pointed to your [custom Pages domain](https://developers.cloudflare.com/pages/configuration/custom-domains/#add-a-custom-domain).

  * If you are using [Workers with a Custom Domain](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/), performing a `fetch` to its own hostname will cause a `522` error. Consider using a [Route](https://developers.cloudflare.com/workers/configuration/routing/), targeting another hostname, or enabling the [`global_fetch_strictly_public` compatibility flag](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#global-fetch-strictly-public) instead.

  * If you are using [Origin Rules](https://developers.cloudflare.com/rules/origin-rules/), make sure the resulting hostname can be resolved. For example, if your Origin Rule point to a Worker route, a `522` error will be returned if the hostname for this route is an A record pointing to a reserved address such as `100::` or `192.0.2.0`.

  * If none of the above leads to a resolution, request the following information from your hosting provider or site administrator before [contacting Cloudflare support](https://developers.cloudflare.com/support/contacting-cloudflare-support/):

    * An [MTR or traceroute](https://developers.cloudflare.com/support/troubleshooting/general-troubleshooting/gathering-information-for-troubleshooting-sites/#perform-a-traceroute) from your origin web server to a [Cloudflare IP address ↗︎](http://www.cloudflare.com/ips) that most commonly connected to your origin web server before the issue occurred. Identify a connecting Cloudflare IP recorded in the origin web server logs.
    * Details from the hosting provider's investigation, such as pertinent logs or conversations with the hosting provider.



### Diagnose with Origin Analytics

Use [Origin Analytics](https://developers.cloudflare.com/speed/origin-analytics/) to check for TCP connection failures to your origin. If the **Top endpoints** table shows a high TCP failure rate for specific paths, the issue may be path-specific rather than a general origin problem. Origin Analytics can also help confirm whether your origin is reachable from Cloudflare's edge.

[PreviousError 521](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-521/)[NextError 523](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-523/)

Was this helpful?

YesNo
