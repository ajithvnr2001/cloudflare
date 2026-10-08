---
url: https://developers.cloudflare.com/security-center/get-started/
title: Get started \u00b7 Cloudflare Security Center docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:29.803062+00:00
---

# Get started · Cloudflare Security Center docs

> Source: https://developers.cloudflare.com/security-center/get-started/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Security Center](https://developers.cloudflare.com/security-center/)
  3. /Get started



# Get started

Last updated Jun 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/security-center/get-started/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesTurn Security Insights on or off Start a new scan Scan frequency

Security Center scans your Cloudflare account configuration and identifies potential security risks, misconfigurations, and vulnerabilities across your domains. This guide covers the initial setup.

## Prerequisites

  * A Cloudflare account.
  * At least one [zone](https://developers.cloudflare.com/fundamentals/concepts/accounts-and-zones/#zones) (domain or subdomain) added to your Cloudflare account.



## Turn Security Insights on or off

Security Insights scans are enabled by default. Security Insights will scan your Cloudflare environment and provide you with a list of detected [insights](https://developers.cloudflare.com/security/security-insights/). Refer to [How it works](https://developers.cloudflare.com/security/security-insights/how-it-works/) to learn more about how Security Insights perform a scan.

The initial scan time depends on the number of IT assets in all the domains of your Cloudflare account. When the scan is complete, the status of the page will change from **Scan in Progress** to **Last scan performed on:`<DATE_TIME>`**.

You can decide to stop a scan, and restart a scan later.

To disable scans:

  1. In the Cloudflare dashboard, go to the **Security Insights** page.

[ Go to **Security insights** ↗ ](https://dash.cloudflare.com/?to=/:account/security-center)
  2. Go to **Disable Security Center scans** , select **Disable scans**.




To restart a scan:

  1. In the Cloudflare dashboard, go to the **Security Insights** page.

[ Go to **Security insights** ↗ ](https://dash.cloudflare.com/?to=/:account/security-center)
  2. Select **Scan now**.




### Start a new scan

To manually start a scan:

  1. In the Cloudflare dashboard, go to the **Security insights** page.

[ Go to **Security insights** ↗ ](https://dash.cloudflare.com/?to=/:account/security-center)
  2. Select **Scan now**.




Note

Only accounts with at least one Business or Enterprise zone, or accounts on the Teams Standard or Teams Enterprise plan, can start manual scans. All plans receive automatic scans.

### Scan frequency

Cloudflare performs scans automatically for all accounts and zones by default. On-demand scans are available on all plans:

Plan | Scan Frequency | On-Demand  
---|---|---  
Free | Every 7 days | Yes  
Pro and Business | Every 3 days | Yes  
Enterprise | Daily | Yes  
  
For more details, refer to [How it works](https://developers.cloudflare.com/security/security-insights/how-it-works/#scan-frequency).

[PreviousOverview](https://developers.cloudflare.com/security-center/)[NextOverview](https://developers.cloudflare.com/security-center/intel-apis/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/security-center/get-started.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
