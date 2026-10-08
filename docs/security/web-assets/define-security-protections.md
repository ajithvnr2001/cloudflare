---
url: https://developers.cloudflare.com/security/web-assets/define-security-protections/
title: Define security protections \u00b7 Security dashboard docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:30.873830+00:00
---

# Define security protections · Security dashboard docs

> Source: https://developers.cloudflare.com/security/web-assets/define-security-protections/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Security dashboard](https://developers.cloudflare.com/security/)
  3. /[Web Assets](https://developers.cloudflare.com/security/web-assets/)
  4. /Define security protections



# Define security protections

Last updated Jun 26, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/security/web-assets/define-security-protections/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewProtection workflowExample: Protect AI-powered operationsValidate detection behaviorMitigate matched traffic

Web Assets provides application context to security detections. This helps detections inspect the right traffic and lets you create rules focusing on targeted protections.

Use this guide to connect a Web Assets operation to a security detection and create a rule that logs, challenges, blocks, or rate limits risky traffic.

## Protection workflow

Most protections that use Web Assets follow the same workflow:

  1. Turn on the security detection that protects the use case, if applicable.

  2. In Web Assets, confirm that the relevant operation exists.

[ Go to **Web assets** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/web-assets)
  3. Apply the required managed label if not already exists.

  4. In Security Analytics, review matched traffic and detection results.

[ Go to **Analytics** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/analytics)
  5. Create a custom rule, or rate limiting rule to act on risky traffic.




## Example: Protect AI-powered operations

[AI Security for Apps](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/) runs targeted scans on requests to AI-powered operations. Use it to detect prompt injection, personally identifiable information (PII) in prompts, unsafe topics, and other Large Language Model (LLM)-specific signals.

To define protection for an LLM-powered operation:

  1. Turn on AI Security for Apps.
  2. Confirm that the operation receiving LLM prompts exists in Web Assets.
  3. Apply the `cf-llm` managed label if not already exists.
  4. In Security Analytics, filter by the `cf-llm` managed label.
  5. Review AI Security for Apps fields on matched traffic.
  6. Create a custom rule or rate limiting rule that acts on the AI detection fields.



For the full setup workflow, refer to [Get started with AI Security for Apps](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/get-started/).

## Validate detection behavior

Use Security Analytics to confirm that the expected requests carry the right operation and label context before you create a blocking rule.

  1. In the Cloudflare dashboard, go to the **Analytics** page.

[ Go to **Analytics** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/analytics)
  2. Filter by the relevant managed label.

  3. Review **Sampled logs**.

  4. Check detection-specific fields, such as LLM prompt fields or leaked credential fields.




You can also export operation and label data with Logpush or query it with the GraphQL Analytics API. For more information, refer to [Use labels in analytics and logs](https://developers.cloudflare.com/security/web-assets/label-operations/#use-labels-in-analytics-and-logs/).

## Mitigate matched traffic

After you validate detection behavior, create rules that act on relevant detection fields.

For example, a rule can match requests addressed to an operation labeled `cf-llm` that also carry personally identifiable information in an LLM prompt.

You can use [custom rules](https://developers.cloudflare.com/waf/custom-rules/create-dashboard/) to log, challenge, block, or skip traffic. You can use [rate limiting rules](https://developers.cloudflare.com/waf/rate-limiting-rules/) to limit high-volume activity.

[PreviousLabel operations](https://developers.cloudflare.com/security/web-assets/label-operations/)[NextSecurity rules](https://developers.cloudflare.com/security/rules/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/security/web-assets/define-security-protections.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
