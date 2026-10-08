---
url: https://developers.cloudflare.com/learning-paths/application-security/rate-limiting/configurations/
title: Configurations \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:43.351903+00:00
---

# Configurations · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/application-security/rate-limiting/configurations/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Application Security

  4. /[Rate Limiting](https://developers.cloudflare.com/learning-paths/application-security/rate-limiting/)
  5. /Configurations



# Configurations

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/application-security/rate-limiting/configurations/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAdvanced configurationBest practices

Let's step through an example. If your `/create-account` page is being attacked, you will create a rule to limit the amount of requests, per `counting characteristic`, that you feel comfortable permitting through to your origin.

The rule below is being created on the `free` plan, which limits configuration options. The rule will trigger if the URI path matches `/create-account`, from the same IP address, _after_ 5 requests and within a 10 second window, [within each Cloudflare datacenter](https://developers.cloudflare.com/waf/rate-limiting-rules/request-rate/), globally.

* * *

![rate-limiting-create-account-endpoint](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1048,height=842,format=webp/_astro/rl-create-account-endpoint.BFxHF746.png)![rate-limiting-create-account-endpoint-block](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=800,height=246,format=webp/_astro/rl-create-account-endpoint-block.DOOFhKll.png)

* * *

## Advanced configuration

In the previous module, we reviewed the various configurations available per plan. Using the same endpoint as an example, let us walk through another example, but with the additional advanced configurations.

The rule below is being created on the `enterprise` plan, so we are no longer limited to default configurations.

  * The rule will also limit the number of requests to `/create-account`, but will only trigger against `POST` requests. In the basic example, even requests with the `GET` method will increment the counter.
  * Requests that do not have a [client certificate (mTLS)](https://developers.cloudflare.com/ssl/client-certificates/), will increment the counter.
  * Requests will be counted using the [IP with NAT support](https://developers.cloudflare.com/waf/rate-limiting-rules/parameters/#use-cases-of-ip-with-nat-support) characteristic.
  * Within a 1 minute period, for each counted entity, if the number of requests exceeds 10, then the user will be presented with a [Managed Challenge](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/#managed-challenge) for a custom duration of 1 day.

![rate-limiting-advanced-config-1](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=688,height=868,format=webp/_astro/rl-advanced-config.CWcevnzk.png)

* * *

## Best practices

Rules that match identical criteria can be stacked together. For example, instead of creating just a single rule for `/create-account`, you can create multiple rules that match the same path but have different `counting characteristics` or `request limits` to protect against a threat that might behave dynamically.

[PreviousUse cases](https://developers.cloudflare.com/learning-paths/application-security/rate-limiting/use-cases/)[NextOverview](https://developers.cloudflare.com/learning-paths/application-security/lists/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/application-security/rate-limiting/configurations.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
