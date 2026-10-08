---
url: https://developers.cloudflare.com/billing/troubleshoot/resolve-zone-cannot-be-upgraded/
title: Resolve the zone cannot be upgraded error \u00b7 Cloudflare Billing docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:31.505157+00:00
---

# Resolve the zone cannot be upgraded error · Cloudflare Billing docs

> Source: https://developers.cloudflare.com/billing/troubleshoot/resolve-zone-cannot-be-upgraded/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Billing](https://developers.cloudflare.com/billing/)
  3. /Troubleshoot
  4. /Resolve the zone cannot be upgraded error



# Resolve the zone cannot be upgraded error

Last updated May 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/billing/troubleshoot/resolve-zone-cannot-be-upgraded/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCausesSolutionVerify the fixRelated resources

When trying to upgrade a domain or purchase a subscription, you may see an error that contains one of the following phrases:

  * "this zone cannot be upgraded"
  * "there is a problem with your billing profile"



## Causes

  * Your account may have an outstanding unpaid balance.
  * Another account previously associated with the domain or zone may have an outstanding unpaid balance.



## Solution

This message appears when the account or domain involved has an outstanding unpaid balance. For a domain, this may also be triggered by a previous account that owned the domain.

  1. Check each Cloudflare account you have access to for an outstanding balance. Refer to [Email address and password](https://developers.cloudflare.com/fundamentals/user-profiles/change-password-or-email/) if you have forgotten these details.
  2. To pay the balance, refer to [Pay an outstanding balance](https://developers.cloudflare.com/billing/manage/pay-invoices-overdue-balances/#pay-an-outstanding-balance).
  3. Wait 24 hours after paying this balance.
  4. Attempt the upgrade again.



As a reference, the full error messages you may see are:

  * "Due to a Billing related issue, the zone cannot be upgraded at this time. Please visit the Billing section to ensure there is no outstanding balance."
  * "Refer to <https://cfl.re/3VUQyyL>[ ↗︎](https://cfl.re/3VUQyyL) for assistance. For security reasons, there is a problem with your billing profile."



## Verify the fix

After you pay the outstanding balance and wait 24 hours, return to the domain or subscription you were trying to purchase and retry the upgrade.

## Related resources

  * [Pay an outstanding balance](https://developers.cloudflare.com/billing/manage/pay-invoices-overdue-balances/) — Resolve unpaid balances
  * [Change domain plan](https://developers.cloudflare.com/billing/manage/change-plan/) — Upgrade or downgrade your plan
  * [Error reference](https://developers.cloudflare.com/billing/troubleshoot/error-reference/) — Look up other billing error messages



[PreviousResolve a payment failure](https://developers.cloudflare.com/billing/troubleshoot/troubleshoot-failed-payments/)[NextResolve "you cannot modify this subscription"](https://developers.cloudflare.com/billing/troubleshoot/resolve-you-cannot-modify-this-subscription/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/billing/troubleshoot/resolve-zone-cannot-be-upgraded.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
