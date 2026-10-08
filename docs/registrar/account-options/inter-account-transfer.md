---
url: https://developers.cloudflare.com/registrar/account-options/inter-account-transfer/
title: Move a Cloudflare Registrar domain registration between accounts \u00b7 Cloudflare Registrar docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:43.748978+00:00
---

# Move a Cloudflare Registrar domain registration between accounts · Cloudflare Registrar docs

> Source: https://developers.cloudflare.com/registrar/account-options/inter-account-transfer/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Registrar](https://developers.cloudflare.com/registrar/)
  3. /[Registration options](https://developers.cloudflare.com/registrar/account-options/)
  4. /Move a Cloudflare Registrar domain registration between accounts



# Move a Cloudflare Registrar domain registration between accounts

Last updated Apr 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/registrar/account-options/inter-account-transfer/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview1\. Prepare for the move2\. Submit the move request

Cloudflare supports the move (transfer) of domain registrations between Cloudflare accounts when the source and target account both confirm the move. The move will result in the loss of all configurations and settings for the domain in the source account.

Important

This process only applies to domains which are registered with Cloudflare Registrar. For domains with other registrars, refer to [Move a domain between Cloudflare accounts](https://developers.cloudflare.com/fundamentals/manage-domains/move-domain/).

Before proceeding, please be aware of the following:

  * WHOIS contact information will be moved as is.
  * No other configuration will be moved.
  * After successful move, the registration will be transfer-locked for 30 days.
  * The target account will become responsible for domain renewals going forward.



## 1\. Prepare for the move

Before you request the move, you will need to do the following:

  * Obtain the [account ID](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/) of the new account.
  * Add the domain as a website to the new account and select a plan.
  * [Disable DNSSEC](https://developers.cloudflare.com/dns/dnssec/#disable-dnssec) for the domain and ensure it is set up and ready in the new dashboard account you intend to move it to.



The following pre-conditions must be met before the domain can be moved:

  * The domain must have been registered more than 10 days ago.
  * The domain must be added to the new account as a website and a plan must be selected.
  * The domain must not be administratively locked, such as being locked due to a dispute or court order.
  * The domain must not have any of the following registry statuses: `pendingDelete`, `redemptionPeriod`, or `pendingTransfer`.
  * The registrant email address must be verified.
  * A pending Change of Registrant request cannot be present. If there is a pending request, it should be completed before initiating the move request.
  * DNSSEC must be turned off. It can be re-enabled on the new zone once the move completes.
  * If the current zone is locked, the lock must be released.



## 2\. Submit the move request

You can now submit the move request under the **Configuration** tab of the **Manage Domain** page. Begin the submission process by selecting the **Start** button and follow the instructions.

**Important** : Review the pre-conditions described above. If those conditions have not been met, the domain move will not be completed.

Once the move request has been submitted, the gaining account will receive an email notifying them of the request and will provide instructions for how to approve the request.

The gaining account must log into their account and go to **Manage Domains** (under Domain Registration). A message will appear at the top of the page stating that there are domains requiring action to be taken.

Select **View Actions** to display the domains with a pending move along and choose to accept or reject the request. Action must be taken within five days of the request.

If no action is taken within the five days, the request will be automatically canceled.

[PreviousiCloud Custom Email Domains](https://developers.cloudflare.com/registrar/account-options/icloud-domains/)[NextRegistrant contact updates](https://developers.cloudflare.com/registrar/account-options/domain-contact-updates/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/registrar/account-options/inter-account-transfer.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
