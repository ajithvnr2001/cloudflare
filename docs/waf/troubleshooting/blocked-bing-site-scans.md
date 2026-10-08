---
url: https://developers.cloudflare.com/waf/troubleshooting/blocked-bing-site-scans/
title: Bing's Site Scan blocked by a managed rule \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:49.265287+00:00
---

# Bing's Site Scan blocked by a managed rule · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/troubleshooting/blocked-bing-site-scans/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /Troubleshooting
  4. /Bing's Site Scan blocked by a managed rule



# Bing's Site Scan blocked by a managed rule

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/troubleshooting/blocked-bing-site-scans/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Microsoft [Bing Webmaster Tools ↗︎](https://www.bing.com/webmaster/tools) provides a Site Scan feature that crawls your website searching for possible SEO improvements.

Site Scan does not use the same IP address range as Bingbot (Bing's website crawler). Additionally, the [Verify Bingbot ↗︎](https://www.bing.com/toolbox/verify-bingbot) tool does not recognize Site Scan's IP addresses as Bingbot. Due to this reason, the WAF managed rule that blocks fake Bingbot requests may trigger for Site Scan requests. This is a known issue of Bing Webmaster Tools.

To allow Site Scan to run on your website, Cloudflare recommends that you temporarily skip the triggered WAF managed rule by creating an [exception](https://developers.cloudflare.com/waf/managed-rules/waf-exceptions/). After the scan finishes successfully, delete the exception to start blocking fake Bingbot requests again.

The rule you should temporarily skip is the following:

| Name | ID  
---|---|---  
**Managed Ruleset** | Cloudflare Managed Ruleset | ...376e9aee  
**Rule** | Anomaly:Header:User-Agent - Fake Bing or MSN Bot | ...c12cf9c8  
  
The exception, shown as a rule with a **Skip** action, must appear in the rules list before the rule executing the Cloudflare Managed Ruleset, or else nothing will be skipped.

To check the rule order, use one of the following methods:

  * When using the old Cloudflare dashboard, the rules listed in **Security** > **WAF** > **Managed rules** run in order.
  * When using the new security dashboard, the rules listed in **Security** > **Security rules** run in order.
  * When using the Cloudflare API, the rules in the `rules` object obtained using the [Get a zone entry point ruleset](https://developers.cloudflare.com/api/resources/rulesets/subresources/phases/methods/get/) operation (for your zone and for the `http_request_firewall_managed` phase) run in order.



For more information on creating exceptions, refer to [Create exceptions](https://developers.cloudflare.com/waf/managed-rules/waf-exceptions/).

[PreviousFirewall rules upgrade](https://developers.cloudflare.com/waf/reference/legacy/firewall-rules-upgrade/)[NextFake bot detection blocking legitimate requests](https://developers.cloudflare.com/waf/troubleshooting/fake-bot-managed-rules/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/troubleshooting/blocked-bing-site-scans.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
