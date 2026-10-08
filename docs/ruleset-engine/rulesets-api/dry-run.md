---
url: https://developers.cloudflare.com/ruleset-engine/rulesets-api/dry-run/
title: Validate rule changes before deployment \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:15.111882+00:00
---

# Validate rule changes before deployment · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rulesets-api/dry-run/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /[Rulesets API](https://developers.cloudflare.com/ruleset-engine/rulesets-api/)
  4. /Validate rule changes before deployment



# Validate rule changes before deployment

Last updated Sep 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ruleset-engine/rulesets-api/dry-run/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewDashboard validationAPI validation Example

Cloudflare can validate a rule or ruleset before deployment. Validation checks the complete configuration without persisting or publishing changes.

Validation includes:

  * Expression syntax and the availability of fields, functions, and operators
  * Actions, action parameters, and phase compatibility
  * Permissions, plan entitlements, and rule quotas
  * References to resources used by the rule



## Dashboard validation

The Cloudflare dashboard automatically validates supported rule changes before deployment. If validation fails, the dashboard displays the error without publishing the change.

Dashboard validation is available for custom rules and rate limiting rules under **Security** > **Security rules**.

[ Go to **Security rules** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/security-rules)

It is also available when you create or update rules under **Rules** > **Overview**.

[ Go to **Overview** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/rules/overview)

## API validation

Supported Rulesets API mutation endpoints accept the `dry_run=true` query parameter. You can use this parameter with `POST`, `PUT`, `PATCH`, and `DELETE` operations at the account or zone level.

A dry run performs the same authorization and server-side validation checks as the requested operation. It does not create, update, delete, or publish any configuration.

Only `true` and `false` are valid values for `dry_run`. An omitted value defaults to `false`. Any other value returns a `400` response.

### Example

The following request validates a rule update without applying it:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Response Compression Write`
  * `Config Settings Write`
  * `Dynamic URL Redirects Write`
  * `Cache Settings Write`
  * `Custom Errors Write`
  * `Origin Write`
  * `Managed headers Write`
  * `Zone Transform Rules Write`
  * `Mass URL Redirects Write`
  * `Magic Firewall Write`
  * `L4 DDoS Managed Ruleset Write`
  * `HTTP DDoS Managed Ruleset Write`
  * `Sanitize Write`
  * `Transform Rules Write`
  * `Select Configuration Write`
  * `Bot Management Write`
  * `Zone WAF Write`
  * `Account WAF Write`
  * `Account Rulesets Write`
  * `Logs Write`
  * `Logs Write`

Update a zone ruleset rulebash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/rulesets/$RULESET_ID/rules/$RULE_ID?dry_run=true" \
    	--request PATCH \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"action": "block",
    		"expression": "ip.src.country eq \"GB\"",
    		"description": "Block requests from the United Kingdom",
    		"enabled": true
    	}'

The API returns the same errors and status codes as the corresponding write operation. A successful operation that normally returns `200` returns `result: null`. An operation that normally returns `204 No Content` continues to return `204`.

For supported operations and request schemas, refer to the [Rulesets API reference](https://developers.cloudflare.com/api/resources/rulesets/).

[PreviousDelete a ruleset](https://developers.cloudflare.com/ruleset-engine/rulesets-api/delete/)[NextPhases list](https://developers.cloudflare.com/ruleset-engine/reference/phases-list/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ruleset-engine/rulesets-api/dry-run.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
