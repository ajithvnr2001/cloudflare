---
url: https://developers.cloudflare.com/changelog/post/2026-06-08-create-waf-rules-from-threat-events/
title: Create WAF rules directly from Threat Events saved views \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:37.026203+00:00
---

# Create WAF rules directly from Threat Events saved views · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-08-create-waf-rules-from-threat-events/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 8, 2026

## Create WAF rules directly from Threat Events saved views

[Security Center](https://developers.cloudflare.com/security-center/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudforce One users can now turn [Threat Events indicators](https://developers.cloudflare.com/security-center/cloudforce-one/#analyze-threat-events) into active defense. With this update, users can instantly generate a WAF rule that matches the dynamic list of IP addresses returned by any of their **Saved Views**.

#### Why this matters

Threat intelligence is most effective when it is immediately actionable. Previously, blocking threat actors required manually extracting indicators from threat events and copying them into your firewall rules. This new integration bridges the gap between threat discovery and threat mitigation:

  * When you identify an active threat pattern - such as an ongoing campaign targeting a specific industry, or using a known indicator type - you can pivot from investigation to mitigation in a single click.
  * Instead of writing complex, static IP rules, this functionality allows you to leverage the specific filtering logic you have already defined and saved within your Threat Events ecosystem.
  * Automating the generation of the WAF rule expression from your threat views eliminates manual copying errors, ensuring that the right malicious infrastructure is blocked instantly.



#### How to use it

You can implement these rules through both the dashboard UI and via the API / Terraform.

Go to **Cloudflare Dashboard** > **Application Security** > **Threat Intelligence** > **Manage Views** , select your desired view, and select **Create WAF Rule**.

This will automatically pre-populate the [WAF rule builder](https://developers.cloudflare.com/firewall/cf-dashboard/create-edit-delete-rules/) with the matching threat event IP indicators.

You can also automate this workflow by utilizing the [**WAF Rule Builder API**](https://developers.cloudflare.com/firewall/api/cf-firewall-rules/) alongside your [Threat Events saved views endpoints](https://developers.cloudflare.com/firewall/api/cf-firewall-rules/).
