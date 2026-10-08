---
url: https://developers.cloudflare.com/turnstile/turnstile-analytics/challenge-outcomes/
title: Challenge outcome \u00b7 Cloudflare Turnstile docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:08.739237+00:00
---

# Challenge outcome · Cloudflare Turnstile docs

> Source: https://developers.cloudflare.com/turnstile/turnstile-analytics/challenge-outcomes/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Turnstile](https://developers.cloudflare.com/turnstile/)
  3. /[Turnstile Analytics](https://developers.cloudflare.com/turnstile/turnstile-analytics/)
  4. /Challenge outcome



# Challenge outcome

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/turnstile/turnstile-analytics/challenge-outcomes/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMetrics Call SiteverifySolve rates Metrics

When a visitor encounters Turnstile, it assesses whether they are human or bot-like based on various signals. These outcomes help you evaluate how effectively Turnstile is protecting your application.

## Metrics

A "solved" Turnstile challenge does not automatically confirm the visitor is human. You must call the Siteverify API to validate the token and proceed only if the response returns `success:true`.

For example, the challenge outcome values in your analytics may look like this:

![Challenge outcome example values](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1020,height=1011,format=webp/_astro/challenge-outcomes.Czqs3OEs.png)Challenge outcome example

  * **Challenges issued** : The total number of challenges presented to visitors within a specific timeframe.
  * **Challenges solved** : The number of challenges successfully completed by visitors in that period.
  * **Challenges unsolved** : Challenges that were abandoned or failed in that period.
  * **Likely human** : The total number of challenges solved or the total number of challenges issued.
  * **Likely bot** : The total number of challenges unsolved or the total number challenges issued.



By analyzing these metrics, you can identify trends such as high failure rates in specific regions, device types, or traffic sources, which may indicate bot activity or misconfigurations.

### Call Siteverify

It is important to [call the Siteverify API](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/). Without calling Siteverify API to validate the tokens, your website or application is not protected. Skipping token validation means you cannot confirm the visitor's legitimacy.

  * Tokens can only be redeemed once. Even valid tokens will return `success:false` if they are reused, preventing token theft and replay attacks.
  * Tokens expire after five minutes. Validation must occur within this window to be effective.
  * Tokens can be invalid. Bots might complete challenges, but Cloudflare can detect bot-like signals and mark the token as invalid.



## Solve rates

Turnstile's solve rate indicates how many visitors pass a challenge. Solve rates can be broken down into the total number of challenges solved and whether they are interactive, non-interactive, or pre-clearance solves.

If you are using [managed mode](https://developers.cloudflare.com/turnstile/concepts/widget/#managed-mode-recommended), you can monitor how many of your visitors were prompted to interact with the checkbox on the widget (interactive solves) and how many were verified without any disruptions to their experience (non-interactive solves).

For example, the solve rate values in your analytics may look like this:

![Solve rate example values](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1020,height=996,format=webp/_astro/solve-rates.YNiFNAbV.png)Solve rate example

### Metrics

  * **Non-interactive solves** : Challenges solved without requiring the visitor to click a checkbox.
  * **Interactive solves** : Challenges solved that required visitor interaction to be solved.
  * [**Pre-clearance solves**](https://developers.cloudflare.com/cloudflare-challenges/concepts/clearance/#pre-clearance-support-in-turnstile): Challenges solved that issued the `cf_clearance` cookie along with the Turnstile token.



A low solve rate might indicate increased bot activity attempting to bypass Turnstile or anomalous traffic patterns that require further investigation.

[PreviousOverview](https://developers.cloudflare.com/turnstile/turnstile-analytics/)[NextToken validation](https://developers.cloudflare.com/turnstile/turnstile-analytics/token-validation/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/turnstile/turnstile-analytics/challenge-outcomes.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
