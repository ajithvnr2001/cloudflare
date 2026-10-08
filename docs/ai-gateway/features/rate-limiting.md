---
url: https://developers.cloudflare.com/ai-gateway/features/rate-limiting/
title: Rate limiting \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:30.220429+00:00
---

# Rate limiting · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/features/rate-limiting/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /[Features](https://developers.cloudflare.com/ai-gateway/features/)
  4. /Rate limiting



# Rate limiting

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/features/rate-limiting/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewParametersHandling rate limitsDefault configuration

Rate limiting controls the traffic that reaches your application, which prevents expensive bills and suspicious activity.

## Parameters

You can define rate limits as the number of requests that get sent in a specific time frame. For example, you can limit your application to 100 requests per 60 seconds.

You can also select if you would like a **fixed** or **sliding** rate limiting technique. With rate limiting, we allow a certain number of requests within a window of time. For example, if it is a fixed rate, the window is based on time, so there would be no more than `x` requests in a ten minute window. If it is a sliding rate, there would be no more than `x` requests in the last ten minutes.

To illustrate this, let us say you had a limit of ten requests per ten minutes, starting at 12:00. So the fixed window is 12:00-12:10, 12:10-12:20, and so on. If you sent ten requests at 12:09 and ten requests at 12:11, all 20 requests would be successful in a fixed window strategy. However, they would fail in a sliding window strategy since there were more than ten requests in the last ten minutes.

## Handling rate limits

When your requests exceed the allowed rate, you will encounter rate limiting. This means the server will respond with a `429 Too Many Requests` status code and your request will not be processed.

## Default configuration

To set the default rate limiting configuration in the dashboard:

  1. Log into the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/) and select your account.
  2. Go to **AI** > **AI Gateway**.
  3. Go to **Settings**.
  4. Enable **Rate-limiting**.
  5. Adjust the rate, time period, and rate limiting method as desired.



To set the default rate limiting configuration using the API:

  1. [Create an API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) with the following permissions:


  * `AI Gateway - Read`
  * `AI Gateway - Edit`


  2. Get your [Account ID](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/).
  3. Using that API token and Account ID, send a [`POST` request](https://developers.cloudflare.com/api/resources/ai_gateway/methods/create/) to create a new Gateway and include a value for the `rate_limiting_interval`, `rate_limiting_limit`, and `rate_limiting_technique`.



This rate limiting behavior will be uniformly applied to all requests for that gateway.

[PreviousSpend limits](https://developers.cloudflare.com/ai-gateway/features/spend-limits/)[NextOverview](https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/features/rate-limiting.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
