---
url: https://developers.cloudflare.com/billing/payment-methods/additional-payment-method-auto-retry/
title: Additional payment method auto-retry \u00b7 Cloudflare Billing docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:30.047383+00:00
---

# Additional payment method auto-retry · Cloudflare Billing docs

> Source: https://developers.cloudflare.com/billing/payment-methods/additional-payment-method-auto-retry/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Billing](https://developers.cloudflare.com/billing/)
  3. /Payment methods
  4. /Additional payment method auto-retry



# Additional payment method auto-retry

Last updated May 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/billing/payment-methods/additional-payment-method-auto-retry/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow auto-retry worksEligibilitySupported payment methodsEmail notificationManage your payment methodsFAQ Multiple charges All payment methods fail Multiple additional payment methods Next renewal behavior Terminology

If a subscription renewal payment fails on your primary payment method, Cloudflare automatically retries the payment using your additional payment methods on file. This keeps your services active without requiring you to take action.

## How auto-retry works

  1. **Primary attempt** : Cloudflare attempts your subscription renewal payment using your primary (default) payment method.
  2. **Automatic retry** : If the payment fails, Cloudflare attempts each of your other payment methods in sequence.
  3. **Success notification** : If a retry succeeds, your services remain active and you receive an email confirming which payment method was charged.
  4. **All methods fail** : If all payment methods fail, standard payment retry processes continue. You may receive an email asking you to update your payment information.



Note

Auto-retry applies to subscription renewal payments only. Auto-retry does not apply to one-time purchases or initial subscription payments.

## Eligibility

Auto-retry is available to pay-as-you-go accounts with at least two payment methods on file — one primary and one or more additional methods. The feature is enabled automatically. No action is needed to turn it on.

## Supported payment methods

Auto-retry works with all payment methods supported by Cloudflare, including credit cards, debit cards, and PayPal. Auto-retry supports any combination of primary and additional payment method types.

## Email notification

When an additional payment method is charged, you receive an email with:

  * The invoice amount and number
  * Which primary payment method failed
  * Which additional payment method was charged
  * A link to manage your payment methods



## Manage your payment methods

  1. In the Cloudflare dashboard, go to the **Billing** page.

[ Go to **Billing** ↗ ](https://dash.cloudflare.com/?to=/:account/billing)
  2. Go to the **Subscriptions** page and open the **Payment methods** panel.

  3. Review your primary and additional payment methods.




Add a second payment method to ensure auto-retry can keep your services active if your primary method fails.

## FAQ

### Multiple charges

You are never charged on more than one payment method for the same invoice. An additional payment method is only charged if your primary payment method fails.

### All payment methods fail

If your primary and all additional payment methods fail, the standard payment retry process continues. You may receive an email asking you to update your payment information.

### Multiple additional payment methods

All additional payment methods are tried in sequence if your primary payment method fails. The more payment methods you have on file, the more chances for your payment to succeed automatically.

### Next renewal behavior

Your next renewal always attempts your primary (default) payment method first. Additional payment methods are only used if the primary fails.

### Terminology

The label "Backup payment method" was renamed to "Additional payment method" in the Cloudflare dashboard. The auto-retry behavior described on this page is unchanged.

[PreviousInstant Bank Payments via Link](https://developers.cloudflare.com/billing/payment-methods/instant-bank-payments-link/)[NextStablecoin payments](https://developers.cloudflare.com/billing/payment-methods/stablecoin-payments/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/billing/payment-methods/additional-payment-method-auto-retry.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
