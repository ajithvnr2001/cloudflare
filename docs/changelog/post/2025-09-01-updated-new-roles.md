---
url: https://developers.cloudflare.com/changelog/post/2025-09-01-updated-new-roles/
title: Updated Email security roles \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:21.992645+00:00
---

# Updated Email security roles · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-09-01-updated-new-roles/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 1, 2025

## Updated Email security roles

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-01-updated-new-roles/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

To provide more granular controls, we refined the [existing roles](https://developers.cloudflare.com/cloudflare-one/roles-permissions/#email-security-roles) for Email security and launched a new Email security role as well.

All Email security roles no longer have read or write access to any of the other Zero Trust products:

  * **Email Configuration Admin**
  * **Email Integration Admin**
  * **Email security Read Only**
  * **Email security Analyst**
  * **Email security Policy Admin**
  * **Email security Reporting**



To configure [Data Loss Prevention (DLP)](https://developers.cloudflare.com/cloudflare-one/email-security/outbound-dlp/) or [Remote Browser Isolation (RBI)](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/#set-up-clientless-web-isolation), you now need to be an admin for the Zero Trust dashboard with the **Cloudflare Zero Trust** role.

Also through customer feedback, we have created a new additive role to allow **Email security Analyst** to create, edit, and delete Email security policies, without needing to provide access via the **Email Configuration Admin** role. This role is called **Email security Policy Admin** , which can read all settings, but has write access to [allow policies](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/allow-policies/), [trusted domains](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/trusted-domains/), and [blocked senders](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/blocked-senders/).

This feature is available across these Email security packages:

  * **Advantage**
  * **Enterprise**
  * **Enterprise + PhishGuard**


