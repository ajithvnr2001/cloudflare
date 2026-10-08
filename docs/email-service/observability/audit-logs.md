---
url: https://developers.cloudflare.com/email-service/observability/audit-logs/
title: Email Service audit logs \u00b7 Cloudflare Email Service docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:14.935327+00:00
---

# Email Service audit logs · Cloudflare Email Service docs

> Source: https://developers.cloudflare.com/email-service/observability/audit-logs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Email Service](https://developers.cloudflare.com/email-service/)
  3. /Observability and logs
  4. /Audit logs



# Audit logs

Last updated Jun 9, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/email-service/observability/audit-logs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEmail Routing actionsEmail Sending actions

Email Service writes configuration changes to [Cloudflare audit logs](https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/). Use audit logs to track who changed what and when.

## Email Routing actions

The following Email Routing actions are recorded:

  * Add, edit, or delete a routing rule.
  * Add or delete a destination address.
  * Change the status of a destination address (for example, from pending to verified).
  * Update the catch-all rule.
  * Enable, disable, or unlock the zone for Email Routing.



## Email Sending actions

The following Email Sending actions are recorded:

  * Onboard or remove a sending domain or subdomain.
  * Add, edit, or delete entries on the suppression list.
  * Enable or disable Email Sending on a domain.



To review audit logs, refer to [Review audit logs](https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/).

[PreviousMetrics and analytics](https://developers.cloudflare.com/email-service/observability/metrics-analytics/)[NextEmail logs](https://developers.cloudflare.com/email-service/observability/logs/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/email-service/observability/audit-logs.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
