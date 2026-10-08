---
url: https://developers.cloudflare.com/fundamentals/api/get-started/ca-keys/
title: Get Origin CA keys \u00b7 Cloudflare Fundamentals docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:20.449897+00:00
---

# Get Origin CA keys · Cloudflare Fundamentals docs

> Source: https://developers.cloudflare.com/fundamentals/api/get-started/ca-keys/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)
  3. /…

Cloudflare's API

  4. /Get started
  5. /Get Origin CA keys



# Get Origin CA keys

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/fundamentals/api/get-started/ca-keys/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewLimitationsView/Change your Origin CA keys

Deprecated

Origin CA keys (Service Keys) are deprecated and will be removed on September 30, 2026. Use an [API Token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) with `Zone`-`SSL and Certificates`-`Edit` permissions instead. For more information, refer to [API deprecations](https://developers.cloudflare.com/fundamentals/api/reference/deprecations/).

Origin CA keys are often used as the value of header `X-AUTH-USER-SERVICE-KEY` when interacting with [Origin CA certificates](https://developers.cloudflare.com/ssl/origin-configuration/origin-ca/) API. It is also used by [Keyless SSL](https://developers.cloudflare.com/ssl/keyless-ssl/) key server.

The key value always starts with `v1.0-`.

## Limitations

  * Changing the Origin CA key is not recorded by [Audit Logs](https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/).
  * Each time you view the Origin CA key, it will be presented as a different value. All these different values are **simultaneously valid** until you click the `Change` button, which immediately invalidates all previously generated values.
  * Origin CA keys have access to every account the user has access to.



## View/Change your Origin CA keys

To retrieve your Origin CA keys:

  1. Log in to the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com).

[ Go to **Account home** ↗ ](https://dash.cloudflare.com/?to=/:account/home)
  2. Go to **User Profile** > **API Tokens**.

  3. In the **API Keys** section, select `Origin CA Key`.




[PreviousGet Global API key (legacy)](https://developers.cloudflare.com/fundamentals/api/get-started/keys/)[NextToken formats](https://developers.cloudflare.com/fundamentals/api/get-started/token-formats/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/fundamentals/api/get-started/ca-keys.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
