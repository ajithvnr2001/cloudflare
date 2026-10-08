---
url: https://developers.cloudflare.com/learning-paths/application-security/account-security/review-audit-logs/
title: Review audit logs - v1 \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:42.576340+00:00
---

# Review audit logs - v1 · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/application-security/account-security/review-audit-logs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Application Security

  4. /[Account security](https://developers.cloudflare.com/learning-paths/application-security/account-security/)
  5. /Review audit logs - v1



# Review audit logs - v1

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/application-security/account-security/review-audit-logs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview Using the dashboard Using the API

Note

Audit Logs version 2 is available in beta. Refer to the [Audit Logs v2 documentation](https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/) for more details.

Audit logs summarize the history of changes made within your Cloudflare account. Audit logs include account level actions like login, as well as zone configuration changes.

Audit Logs are available on all plan types and are captured for both individual users and for multi-user organizations.

Note

Most beta features will not appear in audit logs until they are out of beta.

Audit logs are available in the dashboard as well as the API.

### Using the dashboard

To access audit logs in the Cloudflare dashboard:

In the Cloudflare dashboard, go to the **Audit Logs** page.

[ Go to **Audit logs** ↗ ](https://dash.cloudflare.com/?to=/:account/audit-log)

You can search these audit logs by user email or domain and filter by date range. To download audit logs, click **Download CSV**.

Note

Depending on the volume of data, the export of large amounts of events from Audit Logs might fail with errors. We always recommend using Cloudflare [Logpush](https://developers.cloudflare.com/logs/logpush/) to make sure Audit Logs are always available and stored externally.

### Using the API

To get audit logs from the Cloudflare API, send a [GET request](https://developers.cloudflare.com/api/resources/audit_logs/methods/list/).

We recommending using the API for downloading historical audit log data.

To maintain Audit Logs query performance, the Audit Logs API was modified on 2019-06-30 to return records with a maximum age of 18 months.

[PreviousReview active sessions](https://developers.cloudflare.com/learning-paths/application-security/account-security/review-active-sessions/)[NextAudit Logs - v2 ↗︎](https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/application-security/account-security/review-audit-logs.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
