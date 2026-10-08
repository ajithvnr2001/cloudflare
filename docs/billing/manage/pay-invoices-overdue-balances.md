---
url: https://developers.cloudflare.com/billing/manage/pay-invoices-overdue-balances/
title: Pay an outstanding balance \u00b7 Cloudflare Billing docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:29.965584+00:00
---

# Pay an outstanding balance · Cloudflare Billing docs

> Source: https://developers.cloudflare.com/billing/manage/pay-invoices-overdue-balances/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Billing](https://developers.cloudflare.com/billing/)
  3. /Manage
  4. /Pay an outstanding balance



# Pay an outstanding balance

Last updated May 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/billing/manage/pay-invoices-overdue-balances/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUnderstand why you have an outstanding balancePay an outstanding balanceManually pay invoicesRelated resources

If automatic payment retries fail and you do not pay manually, your account accrues an overdue balance. While the balance is unpaid, you cannot purchase products, upgrade subscriptions, or update your billing profile. Attempts to do so return an error:

**"You cannot add or modify subscriptions or services until the outstanding balance is paid."**

To pay, select **Pay Now** from the **Billing** page in the Cloudflare dashboard. You can pay the entire balance in one transaction or pay individual invoices separately.

## Understand why you have an outstanding balance

When an outstanding balance is due, a new invoice is created in your account for that amount. The new invoice shows the original invoice number that the outstanding balance relates to. You can look up this original invoice to identify which products were not fully paid for.

  1. In the Cloudflare dashboard, go to the **Billing** page.

[ Go to **Billing** ↗ ](https://dash.cloudflare.com/?to=/:account/billing)
  2. Select **Invoices and documents**.

  3. Select the most recent invoice. The amount shown should match your outstanding balance.

  4. In the invoice PDF, find **Invoice that pays the following outstanding balance:** and note the invoice number.

  5. Return to **Invoices and documents** and select the original invoice number.




## Pay an outstanding balance

Note

Allow up to 24 hours for your payment to be recognized and for your account to be in good standing. After that time has passed, you will be able to manage your subscriptions and order more services.

To pay the total outstanding balance:

  1. In the Cloudflare dashboard, go to the **Billing** page.

[ Go to **Billing** ↗ ](https://dash.cloudflare.com/?to=/:account/billing)
  2. Go to the **Pay overdue balances** section.

  3. Select **Pay now** next to the balance you want to pay.




You will be redirected to our payment system to proceed.

## Manually pay invoices

If an automatic subscription renewal payment fails, Cloudflare automatically retries the payment using your default payment method five times over five days. During this period, you can log in to the dashboard and attempt to manually pay the invoices.

  1. In the Cloudflare dashboard, go to the **Billing** page.

[ Go to **Billing** ↗ ](https://dash.cloudflare.com/?to=/:account/billing)
  2. Select **Invoices and documents**.

  3. Select **Pay now** next to the invoice you want to pay.




You will be redirected to our payment system to proceed.

## Related resources

  * [Resolve a payment failure](https://developers.cloudflare.com/billing/troubleshoot/troubleshoot-failed-payments/) — Fix errors when paying
  * [Invoices](https://developers.cloudflare.com/billing/manage/invoices/) — View and download invoices
  * [Error reference](https://developers.cloudflare.com/billing/troubleshoot/error-reference/) — Look up billing error messages



[PreviousUpdate billing information](https://developers.cloudflare.com/billing/get-started/update-billing-info/)[NextChange domain plan](https://developers.cloudflare.com/billing/manage/change-plan/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/billing/manage/pay-invoices-overdue-balances.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
