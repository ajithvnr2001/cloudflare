---
url: https://developers.cloudflare.com/turnstile/turnstile-analytics/token-validation/
title: Token validation \u00b7 Cloudflare Turnstile docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:08.679280+00:00
---

# Token validation · Cloudflare Turnstile docs

> Source: https://developers.cloudflare.com/turnstile/turnstile-analytics/token-validation/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Turnstile](https://developers.cloudflare.com/turnstile/)
  3. /[Turnstile Analytics](https://developers.cloudflare.com/turnstile/turnstile-analytics/)
  4. /Token validation



# Token validation

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/turnstile/turnstile-analytics/token-validation/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMetrics Call Siteverify

After a visitor successfully completes a Turnstile challenge, a token is generated and validated via the Siteverify API. Token validation data shows how many tokens your server validated successfully versus how many failed. A high rate of invalid tokens may indicate bot activity, expired tokens, or implementation issues.

For example, the token validation values in your analytics may look like this:

![Token validation example values](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1019,height=1026,format=webp/_astro/token-validation.DRmcNOiF.png)Token validation example

## Metrics

  * **Siteverify requests** : The total number of requests made to the Siteverify API in the given timeframe.
  * **Valid tokens** : The number of Siteverify requests with `success:true` responses.
  * **Invalid tokens** : The number of Siteverify requests with `success:false` responses.



### Call Siteverify

It is important to [call the Siteverify API](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/). Without calling Siteverify API to validate the tokens, your website or application is not protected. Skipping token validation means you cannot confirm the visitor's legitimacy.

  * Tokens can only be redeemed once. Even valid tokens will return `success:false` if they are reused, preventing token theft and replay attacks.
  * Tokens expire after five minutes. Validation must occur within this window to be effective.
  * Tokens can be invalid. Bots might complete challenges, but Cloudflare can detect bot-like signals and mark the token as invalid.



[PreviousChallenge outcome](https://developers.cloudflare.com/turnstile/turnstile-analytics/challenge-outcomes/)[NextOverview](https://developers.cloudflare.com/turnstile/migration/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/turnstile/turnstile-analytics/token-validation.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
