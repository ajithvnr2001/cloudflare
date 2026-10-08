---
url: https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/explanation/
title: How Authenticated Origin Pulls works \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:43.221412+00:00
---

# How Authenticated Origin Pulls works · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/explanation/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /…

Origin server

  4. /[Authenticated Origin Pulls (mTLS)](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/)
  5. /About



# About

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/explanation/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSimple explanationDetailed explanation Types of handshakes Comparison diagrams

## Simple explanation

When visitors request content from your domain, Cloudflare first attempts to serve content from the cache. If this attempt fails, Cloudflare sends a request — or an `origin pull` — back to your origin web server to get the content.

Authenticated Origin Pulls makes sure that all of these `origin pulls` come from Cloudflare. Put another way, Authenticated Origin Pulls ensures that any HTTPS requests outside of Cloudflare will not receive a response from your origin.

This block also applies for requests to [unproxied DNS records](https://developers.cloudflare.com/dns/proxy-status/#dns-only-records) in Cloudflare.

Caution

The Cloudflare-provided certificate used by [global AOP](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/global/) is not exclusive to your account. It only guarantees that a request is coming from the Cloudflare network.

For stricter security, set up [zone-level](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/zone-level/) or [per-hostname](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/per-hostname/) AOP with your own certificate and consider [other security measures for your origin](https://developers.cloudflare.com/fundamentals/security/protect-your-origin-server/).

## Detailed explanation

Cloudflare enforces authenticated origin pulls by adding an extra layer of TLS client certificate authentication when establishing a connection between Cloudflare and the origin web server.

For more details, refer to the [introductory blog post ↗︎](https://blog.cloudflare.com/protecting-the-origin-with-tls-authenticated-origin-pulls/).

* * *

### Types of handshakes

For more details, refer to [What is a TLS handshake? ↗︎](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/).

**Standard TLS handshake**

![Diagram showing the Standard TLS handshake](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=900,height=1058,format=webp/_astro/client-auth-tls-standard.DZBqll1L.png)

**Client authenticated TLS handshake**

![Diagram showing the client authenticated TLS handshake](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=900,height=1256,format=webp/_astro/client-auth-tls-handshake.B9OeA94c.png)

### Comparison diagrams

Without Authenticated Origin Pulls, Cloudflare performs standard TLS handshakes between a client device and Cloudflare and Cloudflare and your origin. This is true even if you have [**Full**](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full/) or [**Full (strict)**](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full-strict/) encryption modes enabled.
    
    
        flowchart TD
          accTitle: Connection diagram without Authenticated Origin Pulls
          A[End user query for <code>example.com</code>] --Standard TLS Handshake--> B[Cloudflare network]
          B --Standard TLS Handshake--> C[Origin server]
          D[External device] --Standard TLS Handshake ----> C
    

  


This lack of authentication means that - even if your origin is [protected behind Cloudflare](https://developers.cloudflare.com/fundamentals/concepts/how-cloudflare-works/) \- attackers with your origin's IP address will still receive a response from your origin for HTTPS requests.

With Authenticated Origin Pulls, Cloudflare performs standard TLS handshakes between a client device and Cloudflare, but a client-authenticated TLS handshake between Cloudflare and your origin.
    
    
        flowchart TD
          accTitle: Connection diagram with Authenticated Origin Pulls
          A[End user query for <code>example.com</code>] --Standard TLS Handshake--> B[Cloudflare network]
          B --Client authenticated TLS Handshake--> C[Origin server]
          D[External device] --Standard TLS Handshake -----x C
    

  


This additional layer of authentication ensures that any HTTPS requests outside of Cloudflare will not receive a response from your origin.

[PreviousOverview](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/)[NextAWS integration](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/aws-alb-integration/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/origin-configuration/authenticated-origin-pull/explanation.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
