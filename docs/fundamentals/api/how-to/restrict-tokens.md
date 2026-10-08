---
url: https://developers.cloudflare.com/fundamentals/api/how-to/restrict-tokens/
title: Restrict tokens \u00b7 Cloudflare Fundamentals docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:21.055267+00:00
---

# Restrict tokens · Cloudflare Fundamentals docs

> Source: https://developers.cloudflare.com/fundamentals/api/how-to/restrict-tokens/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)
  3. /…

Cloudflare's API

  4. /How to
  5. /Restrict tokens



# Restrict tokens

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/fundamentals/api/how-to/restrict-tokens/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewClient IP address range filteringTime to live (TTL) constraints

API tokens can be restricted at runtime in two ways:

  * Client IP address range filtering
  * Time To Live (TTL) constraints



## Client IP address range filtering

Client IP address restrictions control which IP addresses can make API requests with this token. By default, if no filtering is applied, all IP addresses can use the token. Once an `Is in` rule is applied, the token can only be used from the defined IP addresses. Define ranges with [CIDR notation ↗︎](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation). To allow an IP range with exceptions, define `Is not in` to exempt specific IPs or smaller ranges.

![IP Address filtering options](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1802,height=442,format=webp/_astro/ip-filter.DbEuurVj.png)

Note

Client IP address range filtering is not applied to the [Verify Token ↗︎](https://developers.cloudflare.com/api/resources/user/subresources/tokens/methods/verify/) endpoint.

## Time to live (TTL) constraints

By default, tokens do not expire and are long lived. Defining a TTL sets when a token starts being valid and when a token is no longer valid. This is often referred to as `notBefore` and `notAfter`. Setting these timestamps limits the lifetime of the token to the defined period. Not setting the start date or `notBefore` means the token is active as soon as it is created. Not setting the end date or `notAfter` means the token does not expire.

Note

Dates selected are defined as 00:00 UTC of that day. For finer grained time selection, use the [API](https://developers.cloudflare.com/fundamentals/api/).

![Time to Live selection calendar](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1280,height=836,format=webp/_astro/ttl.6XWjuAt_.png)

[PreviousControl API Access](https://developers.cloudflare.com/fundamentals/api/how-to/control-api-access/)[NextRoll tokens](https://developers.cloudflare.com/fundamentals/api/how-to/roll-token/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/fundamentals/api/how-to/restrict-tokens.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
