---
url: https://developers.cloudflare.com/client-side-security/reference/settings/
title: Configuration settings \u00b7 Client-side security docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:57.929532+00:00
---

# Configuration settings · Client-side security docs

> Source: https://developers.cloudflare.com/client-side-security/reference/settings/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Client-side security](https://developers.cloudflare.com/client-side-security/)
  3. /Reference
  4. /Configuration settings



# Configuration settings

Last updated Aug 3, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/client-side-security/reference/settings/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewReporting endpoint Prerequisites for using the same hostname for CSP reports Configure the reporting endpointConnection target details Configure the connection target details to useTurn off client-side resource monitoring

## Reporting endpoint

When enabled, client-side security's resource monitoring uses a Content Security Policy (CSP)[report-only HTTP header](https://developers.cloudflare.com/client-side-security/reference/csp-header/) to gather information about all the scripts running on your application.

By default, reports are sent to a Cloudflare-owned endpoint:
    
    
    https://csp-reporting.cloudflare.com/cdn-cgi/script_monitor/report?<QUERY_STRING>

Customers with Client-Side Security Advanced can change the reporting endpoint so that the CSP reports are sent to the same hostname:
    
    
    <YOUR-HOSTNAME>/cdn-cgi/script-monitor/report?<QUERY_STRING>

### Prerequisites for using the same hostname for CSP reports

Using the same hostname for CSP reporting may interfere with other Cloudflare products. Before selecting this option, ensure that your Cloudflare configuration complies with the following:

  * No rate limiting rules match the `cdn-cgi/*` URL path
  * No custom rules match the `cdn-cgi/*` URL path



### Configure the reporting endpoint

Note

Only available to customers with Client-Side Security Advanced.

To configure the CSP reporting endpoint:

  1. In the Cloudflare dashboard, go to the Security **Settings** page.

[ Go to **Settings** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/settings)
  2. (Optional) Filter by **Client-side abuse**.

  3. Under **Continuous script monitoring** > **Configurations** , select the edit icon next to **Reporting endpoint**.

  4. Select **Cloudflare-owned endpoint** or **Same hostname**.

  5. Select **Save**.




## Connection target details

When connection targets are reported to Cloudflare, their URIs can sometimes include sensitive data such as session ID.

By default, client-side security only checks the domain against malicious threat intelligence feeds. You can choose to let Cloudflare use the full URI when analyzing the connections made from your domain's pages. Any sensitive data present in the URI will be logged in clear text, and any user with access to the connection monitor dashboard will be able to view it.

### Configure the connection target details to use

  1. In the Cloudflare dashboard, go to the Security **Settings** page.

[ Go to **Settings** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/settings)
  2. (Optional) Filter by **Client-side abuse**.

  3. Under **Continuous script monitoring** > **Configurations** , select the edit icon next to **Data processing**.

  4. Select **Log host only** to analyze only the hostname or **Log full URI** to use the full URI.

  5. Select **Save**.




## Turn off client-side resource monitoring

When you turn off client-side security's resource monitoring, you lose visibility on the scripts running on your zone, the outbound connections made from pages in your domain, and cookies detected in HTTP traffic.

To turn off client-side resource monitoring:

  1. In the Cloudflare dashboard, go to the Security **Settings** page.

[ Go to **Settings** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/settings)
  2. (Optional) Filter by **Client-side abuse**.

  3. Next to **Continuous script monitoring** , set the toggle to **Off**.




Turning off client-side security's resource monitoring does not turn off [content security rules](https://developers.cloudflare.com/client-side-security/rules/) (previously known as policies). To turn off content security rules:

  1. In the Cloudflare dashboard, go to the **Security rules** page.

[ Go to **Security rules** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/security-rules)
  2. (Optional) Filter by **Content security rules**.

  3. For each rule, select the three dots next to it > **Disable**.




[PreviousDeploy rules in production](https://developers.cloudflare.com/client-side-security/best-practices/deploy-rules-in-production/)[NextStatuses](https://developers.cloudflare.com/client-side-security/reference/script-statuses/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/client-side-security/reference/settings.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
