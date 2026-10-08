---
url: https://developers.cloudflare.com/monetization-gateway/get-started/
title: Get started \u00b7 Cloudflare Monetization Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:21.885055+00:00
---

# Get started · Cloudflare Monetization Gateway docs

> Source: https://developers.cloudflare.com/monetization-gateway/get-started/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Monetization Gateway](https://developers.cloudflare.com/monetization-gateway/)
  3. /Get started



# Get started

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/monetization-gateway/get-started/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewReview prerequisitesConfigure a payment ruleComplete configuration

Create a rule that charges matching requests for a resource.

## Review prerequisites

  * Your account and zone meet the [eligibility requirements](https://developers.cloudflare.com/monetization-gateway/eligibility/).
  * You have a receiving wallet.



## Configure a payment rule

  1. In Monetization Gateway, select the domain you would like to monetize.

  2. Select the receiving wallet for payments.

  3. Enter the URL for the request to be monetized.

  4. Select an audience:

     * Select _Everyone_ to charge all matching traffic.
     * Select _Verified Bots_ to charge bots identified by [BotBase](https://developers.cloudflare.com/bots/botbase/).
  5. Select a pricing scheme:

     * Select _Fixed_ to charge the same amount per request.
     * Select _Variable_ to authorize a maximum amount. You must [report the actual amount](https://developers.cloudflare.com/monetization-gateway/configuration/payment-validation/#report-variable-settlement) to finalize the transaction.
  6. Enter the price to be charged. The minimum amount is $0.001.

  7. For advanced settings, refer to [Monetization rules](https://developers.cloudflare.com/monetization-gateway/configuration/rules/).




## Complete configuration

To complete configuration, Cloudflare strongly recommends that you [verify payment](https://developers.cloudflare.com/monetization-gateway/configuration/payment-validation/#validate-the-context) at your origin.

[PreviousEligibility](https://developers.cloudflare.com/monetization-gateway/eligibility/)[Nextx402 protocol](https://developers.cloudflare.com/monetization-gateway/x402/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/monetization-gateway/get-started/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
