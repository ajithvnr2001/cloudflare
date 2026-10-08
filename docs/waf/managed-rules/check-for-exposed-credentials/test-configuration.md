---
url: https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/test-configuration/
title: Test your exposed credentials checks configuration \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:43.618561+00:00
---

# Test your exposed credentials checks configuration · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/test-configuration/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Managed rules](https://developers.cloudflare.com/waf/managed-rules/)

  4. /[Check for exposed credentials](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/)
  5. /Test your configuration



# Test your exposed credentials checks configuration

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/test-configuration/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Deprecation notice

Exposed credentials check has been deprecated.

Switch from exposed credentials check to [leaked credentials detection](https://developers.cloudflare.com/waf/detections/leaked-credentials/) for improved security. To upgrade your current configuration, refer to the [upgrade guide](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/upgrade-to-leaked-credentials-detection/).

After enabling and configuring exposed credentials checks, you may want to test if the checks are working properly.

Cloudflare provides a special set of case-sensitive credentials for this purpose:

  * Login: `CF_EXPOSED_USERNAME` or `CF_EXPOSED_USERNAME@example.com`
  * Password: `CF_EXPOSED_PASSWORD`



The WAF always considers these specific credentials as having been previously exposed. Use them to force an "exposed credentials" event, which allows you to check the behavior of your current configuration.

[PreviousConfigure using Terraform](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/configure-terraform/)[NextMonitor exposed credentials events](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/monitor-events/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/managed-rules/check-for-exposed-credentials/test-configuration.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
