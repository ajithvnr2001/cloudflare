---
url: https://developers.cloudflare.com/billing/get-started/create-billing-profile/
title: Create billing profile \u00b7 Cloudflare Billing docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:29.609433+00:00
---

# Create billing profile · Cloudflare Billing docs

> Source: https://developers.cloudflare.com/billing/get-started/create-billing-profile/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Billing](https://developers.cloudflare.com/billing/)
  3. /Get started
  4. /Create billing profile



# Create billing profile

Last updated May 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/billing/get-started/create-billing-profile/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAdd a primary payment methodAdd an additional payment methodRelated resources

## Add a primary payment method

A primary payment method is required to purchase Cloudflare products and services. Cloudflare does not store or have access to your full card number, PIN, or PayPal password.

Note

Because some countries tax goods and services on personal accounts, you may be asked to indicate whether your Cloudflare account is personal or business to determine tax eligibility.

  1. In the Cloudflare dashboard, go to the **Billing** page.

[ Go to **Billing** ↗ ](https://dash.cloudflare.com/?to=/:account/billing)
  2. Go to the **Subscriptions** page and open the **Payment methods** panel.

  3. Select **Add Payment Method**. If no payment method is on file, the dialog opens automatically.

  4. Choose a payment option and enter the required details:

**Card** (Visa, Mastercard, American Express, Discover, UnionPay):

     1. Enter your card details.
     2. Complete 3D Secure authentication if your card issuer requires it.
     3. If applicable, add your business information for your invoice, including your **Company** and **VAT/GST Number**.

**PayPal** (your linked card or bank is charged if you have insufficient funds in your PayPal account):

     1. Select **PayPal**.
     2. Follow the online instructions until PayPal returns you to the Cloudflare **Payment Method** form to continue setup.
     3. Verify your **PayPal username** now appears next to the PayPal logo.
     4. Add your account contact information as well as **Company** and **VAT/GST Number** , if applicable.

**Wallets** : Apple Pay, Google Pay, Link, and [Instant Bank Payments via Link](https://developers.cloudflare.com/billing/payment-methods/instant-bank-payments-link/) (US-based self-serve accounts) are also available.

  5. Review the payment method and contact information.

  6. To finish, select **Confirm**.

  7. Ensure your new payment method appears in the **Payment methods** panel.




## Add an additional payment method

Optionally, add an additional payment method. Cloudflare automatically retries the charge on the additional method if the primary method fails. Refer to [Additional payment method auto-retry](https://developers.cloudflare.com/billing/payment-methods/additional-payment-method-auto-retry/) for details.

Note

You may receive the error message "Your account is limited to 2 payment methods, and you've reached that limit. Please remove an existing payment method before adding a new one." when trying to add additional methods.

If you are unable to add or edit a payment method, [delete a payment method](https://developers.cloudflare.com/billing/get-started/update-billing-info/#delete-a-payment-method) and try again.

  1. In the Cloudflare dashboard, go to the **Billing** page.

[ Go to **Billing** ↗ ](https://dash.cloudflare.com/?to=/:account/billing)
  2. Go to the **Subscriptions** page and open the **Payment methods** panel.

  3. Select **Add Payment Method**.

  4. Enter card details or select a supported wallet. Complete 3D Secure authentication if your card issuer requires it.

  5. Confirm the billing address and select **Save**.

  6. To make the additional payment method the primary method, select **Make primary payment method**.




## Related resources

  * [Update billing information](https://developers.cloudflare.com/billing/get-started/update-billing-info/) — Change payment methods, billing address, or email
  * [How Cloudflare billing works](https://developers.cloudflare.com/billing/understand/how-billing-works/) — Billing lifecycle and charge types
  * [Billing policy](https://developers.cloudflare.com/billing/understand/billing-policy/) — Refund policy and subscription terms



[PreviousOverview](https://developers.cloudflare.com/billing/)[NextUpdate billing information](https://developers.cloudflare.com/billing/get-started/update-billing-info/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/billing/get-started/create-billing-profile.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
