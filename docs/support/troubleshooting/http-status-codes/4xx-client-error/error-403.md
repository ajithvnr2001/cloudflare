---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-403/
title: Error 403 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:53.434259+00:00
---

# Error 403 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-403/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[4xx Client Error](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/)
  5. /Error 403



# Error 403

Last updated Sep 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-403/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview403 Forbidden Common use cases Cloudflare-specific information

## 403 Forbidden

The `403 Forbidden` status code indicates that the client's request was understood by the server but cannot be fulfilled due to insufficient permissions to access the requested resource. For more details, refer to [RFC 9110 ↗︎](https://www.rfc-editor.org/rfc/rfc9110#section-15.5.4).

### Common use cases

If you encounter a `403` error without the Cloudflare branding, this means that the error is being returned directly by the origin web server, not Cloudflare. This is typically related to permission rules set on your server. Common reasons for this error are:

  * Permission rules configured on the origin web server (for example, in an Apache `.htaccess` file).
  * Mod_security rules.
  * IP deny rules, such as blocking traffic from certain IP ranges. Make sure that [Cloudflare's IP ranges ↗︎](https://www.cloudflare.com/ips) are not being blocked.



### Cloudflare-specific information

Cloudflare may serve `403` responses in the following scenarios:

  * **WAF rules** : The request violated a default WAF managed rule (enabled for all orange-clouded Cloudflare domains) or a custom WAF managed rule specific to your zone. For more information, refer to [WAF Managed Rules](https://developers.cloudflare.com/waf/managed-rules/).

  * **Security features** : A `403` response with Cloudflare branding in the response body may be triggered by:

    * [WAF Custom or Managed Rules](https://developers.cloudflare.com/waf/) with the challenge or block action.
    * [Security Level](https://developers.cloudflare.com/waf/tools/security-level/) settings, which default to Medium.
    * [DDoS Protection](https://developers.cloudflare.com/ddos-protection/), which is enabled by default on zones onboarded to Cloudflare, IP applications onboarded to Spectrum, and IP Prefixes onboarded to Magic Transit.
    * Most [1xxx Cloudflare error codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/).
    * The [Browser Integrity Check](https://developers.cloudflare.com/waf/tools/browser-integrity-check/).
    * [Validation Checks](https://developers.cloudflare.com/waf/tools/validation-checks/).



Cloudflare may also serve an unstyled `403` error page in specific cases. These errors are not logged because they occur early in Cloudflare's infrastructure, before domain configuration is loaded. An example is:

  * [SNI ↗︎](https://www.cloudflare.com/learning/ssl/what-is-sni/): A `403` error is returned when the client sends a host that does not match the SNI (Server Name Indication).



[PreviousError 401](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-401/)[NextError 404](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-404/)

Was this helpful?

YesNo
