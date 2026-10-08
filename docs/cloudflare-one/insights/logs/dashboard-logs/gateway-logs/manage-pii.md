---
url: https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/manage-pii/
title: Manage PII \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:51.818636+00:00
---

# Manage PII · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/manage-pii/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Insights](https://developers.cloudflare.com/cloudflare-one/insights/)[Logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/)[Dashboard logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/)

  4. /[Gateway activity logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/)
  5. /Manage PII



# Manage PII

Last updated Apr 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/manage-pii/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewTypes of PIIExclude PII

Cloudflare Gateway gives you multiple ways to safely handle your employees' personally identifiable information (PII) in activity logs:

  * **Redact PII** (default) — PII is stored in logs but hidden from view. Only the Super Administrator and users with the [Cloudflare Zero Trust PII role](https://developers.cloudflare.com/cloudflare-one/roles-permissions/#cloudflare-zero-trust-pii) can view redacted PII. The underlying data is preserved — redaction only controls who can see it.
  * **Exclude PII** — PII is not stored in logs at all. No user, including the Super Administrator, can retrieve it.



Only the Super Administrator can assign roles and determine who has permission to view PII. To add or remove the Cloudflare Zero Trust PII role for a user in your organization, refer to [Roles](https://developers.cloudflare.com/fundamentals/manage-members/roles/).

## Types of PII

Cloudflare Gateway can log the following types of PII:

  * Source IP
  * User email
  * User ID
  * Device ID
  * URL
  * Referer
  * User agent



## Exclude PII

When you exclude PII, Gateway logs activity without storing any employee PII. This differs from the default redaction behavior — excluded PII is not stored and cannot be retrieved by any role, including the Super Administrator.

Caution

Excluding PII is irreversible for the period it is active. If you turn on this setting and later turn it off, logs captured while the setting was on will permanently lack PII data.

Changes to this setting do not affect PII already stored in previous logs.

To turn on the setting to exclude PII:

  1. In [Cloudflare One ↗︎](https://one.dash.cloudflare.com/), go to **Traffic policies** > **Traffic settings**.
  2. In **Traffic logging** , turn on **Exclude personally identifiable information (PII) from logs**.



[PreviousOverview](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/)[NextSSH command logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/ssh-command-logs/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/manage-pii.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
