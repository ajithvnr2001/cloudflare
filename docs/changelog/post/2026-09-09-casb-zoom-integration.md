---
url: https://developers.cloudflare.com/changelog/post/2026-09-09-casb-zoom-integration/
title: New CASB integration for Zoom \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:13.050336+00:00
---

# New CASB integration for Zoom · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-09-casb-zoom-integration/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 9, 2026

## New CASB integration for Zoom

[CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-09-casb-zoom-integration/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Cloudflare CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/) now integrates with [Zoom](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/zoom/). The integration connects through Cloudflare's pre-built OAuth application — no manual app setup in Zoom is required. After an initial scan, CASB continuously scans your Zoom account to surface new findings as your environment changes.

Zoom is widely used for meetings, webinars, and collaboration. Misconfigurations in account settings, meeting security controls, and recording access can expose organizations to data leakage, unauthorized access, and compliance risk. Cloudflare CASB ingests Zoom account data via API to surface security findings across these areas.

#### Key capabilities

Starting today, security teams can scan for security findings across the following assets:

  * **Account settings** — Detect weak password policies, unlocked security controls, and two-factor authentication gaps across your Zoom account
  * **User accounts** — Identify users not enforcing SSO, accounts with insecure host keys, unverified or inactive users, and unsafe overrides of account-level security settings
  * **Meetings** — Surface meetings without passwords or waiting rooms, meetings using Personal Meeting IDs (PMIs), and meetings with external domain hosts
  * **Recordings** — Detect publicly accessible cloud recordings, recordings without passcodes, and weak recording password configurations
  * **Content** — Identify sensitive information in meeting and recording content via DLP Profile matching



#### Learn more

This [integration](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/zoom/) is available to all Cloudflare Zero Trust customers today. New customers can sign up and start with their first two integrations for free. Existing customers can enable the integration directly in the Cloudflare One dashboard under **Cloud & SaaS findings** > **Integrations**. The integration begins scanning immediately and surfaces findings in the dashboard within minutes.
