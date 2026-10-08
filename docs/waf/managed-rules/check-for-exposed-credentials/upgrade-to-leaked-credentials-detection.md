---
url: https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/upgrade-to-leaked-credentials-detection/
title: Upgrade to leaked credentials detection \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:44.033893+00:00
---

# Upgrade to leaked credentials detection · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/upgrade-to-leaked-credentials-detection/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Managed rules](https://developers.cloudflare.com/waf/managed-rules/)

  4. /[Check for exposed credentials](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/)
  5. /Upgrade to leaked credentials detection



# Upgrade to leaked credentials detection

Last updated Aug 3, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/upgrade-to-leaked-credentials-detection/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview1\. Turn off Exposed Credentials Check2\. Turn on leaked credentials detection3\. Configure the actions to takeMore resources

This guide describes the general steps to upgrade your [Exposed Credentials Check](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/) configuration to the new [leaked credentials detection](https://developers.cloudflare.com/waf/detections/leaked-credentials/).

Cloudflare recommends that customers update their configuration to use the new leaked credentials detection, which offers the following advantages:

  * Uses a comprehensive database of leaked credentials, containing over 15 billion passwords.
  * After enabling the detection, you can review the amount of incoming requests containing leaked credentials in Security Analytics, even before creating any mitigation rules.
  * You can take action on the requests containing leaked credentials using WAF features like rate limiting rules or custom rules.



Note

This upgrade guide applies to customers changing from Exposed Credentials Check at the zone level.

## 1\. Turn off Exposed Credentials Check

If you had deployed the Cloudflare Exposed Credentials Check managed ruleset:

  1. In the Cloudflare dashboard, go to the **Security rules** page.

[ Go to **Security rules** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/security-rules)
  2. (Optional) Filter by **Managed rules**.

  3. Edit the rule that executes the Cloudflare Exposed Credentials Check Ruleset and take note of the current configuration (namely the performed action). Next, delete (or turn off) that rule.




Note

While Exposed Credentials Check and leaked credentials detection can work side by side, enabling both features will increase the latency on incoming requests related to authentication.

## 2\. Turn on leaked credentials detection

On Free plans, the leaked credentials detection is enabled by default, and no action is required. On paid plans, you can turn on the detection in the Cloudflare dashboard, via API, or using Terraform.

  1. In the Cloudflare dashboard, go to the Security **Settings** page.

[ Go to **Settings** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/settings)
  2. (Optional) Filter by **Detection tools**.

  3. Turn on **Leaked credential detection**.




Use a `POST` request similar to the following:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Zone WAF Write`
  * `Account WAF Write`

Update the Leaked Credential Checks status for a zone.bash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/leaked-credential-checks" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"enabled": true
    	}'

Use the `cloudflare_leaked_credential_check` resource to enable leaked credentials detection for a zone. For example:
    
    
    resource "cloudflare_leaked_credential_check" "zone_lcc_example" {
    	zone_id = var.cloudflare_zone_id
    	enabled = true
    }

## 3\. Configure the actions to take

Based on your previous configuration, do one of the following:

  * If you were using the [default action](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/#available-actions) in Exposed Credentials Check: Turn on the [**Add Leaked Credentials Checks Header** managed transform](https://developers.cloudflare.com/rules/transform/managed-transforms/reference/#add-leaked-credentials-checks-header) that adds the `Exposed-Credential-Check` header to incoming requests containing leaked credentials. Even though the header name is the same as in Exposed Credentials Check, the header values in the new implementation will vary between `1` and `4`.
  * If you were using a different action: Create a [custom rule](https://developers.cloudflare.com/waf/custom-rules/) with an action equivalent to the one you were using. The rule should match `User and password leaked is true` (if you are using the expression editor, enter `(cf.waf.credential_check.username_and_password_leaked)`).



* * *

## More resources

  * Check for the results of leaked credentials detection in [Security Analytics](https://developers.cloudflare.com/waf/analytics/security-analytics/).
  * Refer to [Example mitigation rules](https://developers.cloudflare.com/waf/detections/leaked-credentials/examples/) for example mitigation strategies you can use when detecting leaked credentials.



[PreviousMonitor exposed credentials events](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/monitor-events/)[NextCloudflare Managed Ruleset](https://developers.cloudflare.com/waf/managed-rules/reference/cloudflare-managed-ruleset/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/managed-rules/check-for-exposed-credentials/upgrade-to-leaked-credentials-detection.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
