---
url: https://developers.cloudflare.com/waf/detections/attack-signature-detection/use-attack-signatures-in-security-rules/
title: Use attack signatures in Security Rules \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:41.488770+00:00
---

# Use attack signatures in Security Rules · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/detections/attack-signature-detection/use-attack-signatures-in-security-rules/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Traffic detections](https://developers.cloudflare.com/waf/detections/)

  4. /[Attack Signature](https://developers.cloudflare.com/waf/detections/attack-signature-detection/)
  5. /Use attack signatures in Security Rules



# Use attack signatures in Security Rules

Last updated Sep 8, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/detections/attack-signature-detection/use-attack-signatures-in-security-rules/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate a mitigation policyMatch a categoryMatch confidenceMatch a signature RefScope rules and exceptionsUnderstand rule orderingCompare with Managed Rules

Attack Signature Detection fields let Security Rules act on matching traffic. The detection fields do not apply actions by themselves.

Note

Attack Signature Detection is available in Early Access. Contact your Cloudflare account team to request access.

## Create a mitigation policy

  1. Review historical matches in **Security Analytics** > **Attack Analysis**.
  2. Choose whether to match a confidence, category, or signature Ref value.
  3. Scope the rule to the intended hostname, path, method, or endpoint.
  4. Select an action appropriate for the reviewed traffic.
  5. Monitor the result and adjust the expression if legitimate traffic is affected.



Start with the narrowest application scope that meets your security objective. Treat low-confidence signatures as candidates for application-specific review instead of broad blocking.

You can use these fields in Security Rules created in the dashboard or through the API. For rule creation steps, refer to [Create a custom rule in the dashboard](https://developers.cloudflare.com/waf/custom-rules/create-dashboard/) or [Create a custom rule via API](https://developers.cloudflare.com/waf/custom-rules/create-api/).

## Match a category

This expression matches the SQL injection category:
    
    
    any(cf.waf.signature.request.categories[*] eq "sqli")

Use the same array expression for another category, including a specific CVE category. Review historical matches before selecting an action.

## Match confidence

This expression matches high-confidence signatures:
    
    
    any(cf.waf.signature.request.confidence[*] eq "high")

Replace `high` with `low` to match low-confidence signatures. You can create separate rules to apply different actions to each confidence level.

## Match a signature Ref

This expression matches a specific signature Ref:
    
    
    any(cf.waf.signature.request.refs[*] eq "d68f8101f6e14e25aefcaea69c530a29")

The Ref is the same value as the corresponding Managed Rule public Rule ID. Use this mapping to reconcile the rule with your Managed Rules configuration.

## Scope rules and exceptions

Combine a signature condition with request properties in the rule builder. Use properties such as hostname, path, and method to limit mitigation to the affected application surface.

For a known false positive, exclude the legitimate endpoint from mitigation. Keep protection for the rest of the application. Validate combined expressions in the rule builder before deployment.

## Understand rule ordering

Attack Signature Detection and Managed Rules have no special interaction. A Custom Rule using a detection field follows normal Custom Rules ordering.

A terminating action stops request processing at that rule. Managed Rules do not evaluate the same request. A non-terminating _Log_ action lets processing continue to Managed Rules.

## Compare with Managed Rules

To compare the two products without changing traffic:

  1. Create a Custom Rule that references the relevant detection fields.
  2. Select the _Log_ action for the Custom Rule.
  3. Keep the corresponding Managed Rules protection in _Block_ mode.
  4. In [Security Events](https://developers.cloudflare.com/waf/analytics/security-events/), compare logged detection matches with Managed Rules blocks.



Verify whether Managed Rules already mitigate the traffic before adding duplicate handling. Recheck your Security Rules after application releases or major traffic changes.

For field types and Logpush mappings, refer to [Attack Signature Detection fields](https://developers.cloudflare.com/waf/detections/attack-signature-detection/fields/).

[PreviousAnalyze attack signatures](https://developers.cloudflare.com/waf/detections/attack-signature-detection/analyze-attack-signatures/)[NextFields](https://developers.cloudflare.com/waf/detections/attack-signature-detection/fields/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/detections/attack-signature-detection/use-attack-signatures-in-security-rules.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
