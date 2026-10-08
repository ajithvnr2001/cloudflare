---
url: https://developers.cloudflare.com/fundamentals/reference/report-abuse/submit-report/
title: View and submit reports \u00b7 Cloudflare Fundamentals docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:26.888751+00:00
---

# View and submit reports · Cloudflare Fundamentals docs

> Source: https://developers.cloudflare.com/fundamentals/reference/report-abuse/submit-report/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)
  3. /…

Reference

  4. /[Abuse](https://developers.cloudflare.com/fundamentals/reference/report-abuse/)
  5. /View and submit reports



# View and submit reports

Last updated Sep 10, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/fundamentals/reference/report-abuse/submit-report/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSubmit reportsView submitted reportsReceive notifications

## Submit reports

Cloudflare provides security, performance, and reliability services to millions of websites. When you report abuse involving a website that uses Cloudflare, Cloudflare's ability to respond depends on the Cloudflare service involved. Many reports involve websites using Cloudflare's pass-through CDN and security services, while others involve domains registered through Cloudflare Registrar or content hosted on Cloudflare's developer platform.

If you find abusive content on a website that uses Cloudflare, you can submit a report in one of three ways:

  * **Public form** : Use [Submit an abuse report ↗︎](https://abuse.cloudflare.com/) to report abuse to Cloudflare. This form is available to anyone on the Internet.

  * **Cloudflare dashboard** : Entitled Cloudflare customers can submit abuse reports from the **Abuse reports** page. You must have the **Trust & Safety**, **Admin** , or **Super Admin** role.

[ Go to **Abuse reports** ↗ ](https://dash.cloudflare.com/?to=/:account/abuse-reports)
  * **Cloudflare API** : Entitled Cloudflare customers can submit abuse reports using the [Abuse Reports API](https://developers.cloudflare.com/api/resources/abuse_reports/). You must have the **Trust & Safety**, **Admin** , or **Super Admin** role.




## View submitted reports

Entitled Cloudflare customers with the **Trust & Safety**, **Admin** , or **Super Admin** role can view abuse reports against content associated with their account.

  1. In the Cloudflare dashboard, go to the **Abuse reports** page.

[ Go to **Abuse reports** ↗ ](https://dash.cloudflare.com/?to=/:account/abuse-reports)
  2. Optionally, filter reports by date, report status, report type, or domain.




If Cloudflare applied a mitigation to your website because of an abuse report, you may be able to request a review of that mitigation in the dashboard or using the [Abuse Report Mitigations API](https://developers.cloudflare.com/api/resources/abuse_reports/subresources/mitigations/). Cloudflare will review the request and may remove the mitigation.

## Receive notifications

You can enable abuse notifications for your account to configure email, webhook, or PagerDuty alerts about new abuse reports against your websites.

For help setting up alerts, refer to [Configure Cloudflare notifications](https://developers.cloudflare.com/notifications/get-started/).

[PreviousCustomer abuse report obligations](https://developers.cloudflare.com/fundamentals/reference/report-abuse/abuse-report-obligations/)[NextBlocked Content](https://developers.cloudflare.com/fundamentals/reference/report-abuse/blocked-content/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/fundamentals/reference/report-abuse/submit-report.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
