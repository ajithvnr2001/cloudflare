---
url: https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/how-checks-work/
title: How exposed credentials checks work \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:43.343367+00:00
---

# How exposed credentials checks work · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/how-checks-work/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Managed rules](https://developers.cloudflare.com/waf/managed-rules/)

  4. /[Check for exposed credentials](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/)
  5. /How it works



# How exposed credentials checks work

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/how-checks-work/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewExample

Deprecation notice

Exposed credentials check has been deprecated.

Switch from exposed credentials check to [leaked credentials detection](https://developers.cloudflare.com/waf/detections/leaked-credentials/) for improved security. To upgrade your current configuration, refer to the [upgrade guide](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/upgrade-to-leaked-credentials-detection/).

WAF rules can include a check for exposed credentials. When enabled in a given rule, exposed credentials checking happens when there is a match for the rule expression (that is, the rule expression evaluates to `true`).

At this point, the WAF looks up the username/password pair in the request against a database of publicly available stolen credentials. When both the rule expression and the exposed credentials check are true, there is a rule match, and Cloudflare performs the action configured in the rule.

## Example

For example, the following rule matches `POST` requests to the `/login.php` URI when Cloudflare identifies the submitted credentials as previously exposed:

**Rule #1**

Rule expression:  
`http.request.method == "POST" and http.request.uri == "/login.php"`

Exposed credentials check with the following configuration:

  * Username expression: `http.request.body.form["user_id"]`
  * Password expression: `http.request.body.form["password"]`



Action: _Interactive Challenge_

When there is a match for the rule above and Cloudflare detects exposed credentials, the WAF presents the user with a challenge.

[PreviousOverview](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/)[NextConfigure via API](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/configure-api/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/managed-rules/check-for-exposed-credentials/how-checks-work.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
