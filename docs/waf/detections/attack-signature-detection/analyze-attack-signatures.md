---
url: https://developers.cloudflare.com/waf/detections/attack-signature-detection/analyze-attack-signatures/
title: Analyze attack signatures \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:41.539384+00:00
---

# Analyze attack signatures · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/detections/attack-signature-detection/analyze-attack-signatures/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Traffic detections](https://developers.cloudflare.com/waf/detections/)

  4. /[Attack Signature](https://developers.cloudflare.com/waf/detections/attack-signature-detection/)
  5. /Analyze attack signatures



# Analyze attack signatures

Last updated Sep 8, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/detections/attack-signature-detection/analyze-attack-signatures/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewReview signature matchesInterpret confidenceInvestigate possible false positivesCompare results with Managed RulesSampling

Use **Security Analytics** > **Attack Analysis** to investigate attack signature matches before applying mitigation.

Note

Attack Signature Detection is available in Early Access. Contact your Cloudflare account team to request access.

## Review signature matches

  1. In the Cloudflare dashboard, go to **Security** > **Analytics**.

[ Go to **Analytics** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/analytics)
  2. Select **Attack Analysis**.

  3. Choose the time range and application scope to investigate.

  4. Plot request volume over time by signature Ref, category, or WAF Attack Score.

  5. Compare high- and low-confidence matches.

  6. Filter by request outcome to identify mitigated and unmitigated traffic.

  7. Narrow the analysis by hostname, path, method, category, CVE, or signature Ref.

  8. Review representative requests before creating or changing a Security Rule.




Use this analysis to identify common signatures and attack categories. You can also investigate a specific Common Vulnerabilities and Exposures (CVE) identifier or attack technique. Correlate the matches with [WAF Attack Score](https://developers.cloudflare.com/waf/detections/attack-score/) to add another signal.

The request outcome shows whether existing protections mitigated matching traffic. It also helps identify requests served by Cloudflare or your origin. A detection does not apply an action by itself.

## Interpret confidence

Confidence describes the expected false-positive characteristics of a signature. It does not prove that a request is malicious.

Confidence | Meaning | Comparison with Managed Rules | Recommended analysis  
---|---|---|---  
`high` | The signature targets a high true-positive and low false-positive rate. | Includes the same signatures that the default Managed Rules deployment enables. | Confirm affected traffic and current mitigation before applying a broad action.  
`low` | The signature has a greater risk of matching legitimate application traffic. | Includes the Managed Rules signatures that are disabled by default. | Review requests and scope mitigation to the affected application surface.  
  
## Investigate possible false positives

Legitimate rich-text input can match a generic cross-site scripting signature. For example, a content management or support application may accept HTML.

Filter the analysis to that hostname, path, and method. Review representative requests to distinguish expected content from attacks. Then create a scoped rule or exception instead of changing protection for the entire application.

## Compare results with Managed Rules

Each signature Ref matches the corresponding Managed Rule public Rule ID. Use this identifier to find the Managed Rule and compare the detection with your deployment.

Check the request outcome and [Security Events](https://developers.cloudflare.com/waf/analytics/security-events/) before assuming Managed Rules blocked a match. Managed Rules actions and overrides determine their behavior.

## Sampling

Attack Analysis uses [Security Analytics adaptive sampling](https://developers.cloudflare.com/waf/analytics/security-analytics/#sampling). Use [Log Explorer](https://developers.cloudflare.com/log-explorer/) when you need 100% retention rather than sampled data.

After reviewing historical traffic, refer to [Use attack signatures in Security Rules](https://developers.cloudflare.com/waf/detections/attack-signature-detection/use-attack-signatures-in-security-rules/).

[PreviousOverview](https://developers.cloudflare.com/waf/detections/attack-signature-detection/)[NextUse attack signatures in Security Rules](https://developers.cloudflare.com/waf/detections/attack-signature-detection/use-attack-signatures-in-security-rules/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/detections/attack-signature-detection/analyze-attack-signatures.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
