---
url: https://developers.cloudflare.com/ai-gateway/observability/logging/legacy-logs/
title: Legacy Logs \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:32.046117+00:00
---

# Legacy Logs · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/observability/logging/legacy-logs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /…

Observability

  4. /[Logging](https://developers.cloudflare.com/ai-gateway/observability/logging/)
  5. /Legacy Logs



# Legacy Logs

Last updated Sep 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/observability/logging/legacy-logs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewView request detailsManage storageDelete logs automaticallyDelete logs manuallyUse the Logs API

Account eligibility

Legacy Logs applies only to AI Gateway customers who created a gateway before September 24, 2026. Customers who create their first gateway on or after that date use [AI Gateway logging](https://developers.cloudflare.com/ai-gateway/observability/logging/).

Legacy Logs provides an AI Gateway dashboard viewer and Logs API. To configure default collection or per-request headers, refer to [Logging](https://developers.cloudflare.com/ai-gateway/observability/logging/).

## View request details

The dashboard viewer shows individual requests for each gateway. It includes the shared request fields described in [Logging](https://developers.cloudflare.com/ai-gateway/observability/logging/).

## Manage storage

Each gateway has a configurable storage limit based on your plan. Workers Free accounts can store 100,000 logs across all gateways. Workers Paid accounts can store 10 million logs per gateway.

Each stored log can be up to 10 MB. Legacy Logs does not store logs exceeding that size.

Legacy Logs persists stored logs until you delete them.

When you reach a storage limit, Legacy Logs can stop saving logs or automatically delete the oldest logs. If saving stops, delete stored logs before Legacy Logs can save more.

For plan details, refer to [AI Gateway pricing](https://developers.cloudflare.com/ai-gateway/reference/pricing/#accounts-created-before-september-24-2026).

## Delete logs automatically

In your gateway settings, turn on **Automatic Log Deletion**. Legacy Logs deletes the oldest logs when your account reaches its storage limit.

## Delete logs manually

In the dashboard, open the gateway **Logs** tab. Apply filters, and then select **Delete logs**.

The dashboard supports these filters:

Filter category | Filter options | Description  
---|---|---  
Status | Error, status | Matches an error type or status  
Cache | Cached, not cached | Matches cache status  
Provider | Specific providers | Matches an AI provider  
AI models | Specific models | Matches an AI model  
Cost | Less than, greater than | Compares cost with a threshold  
Request type | Workers AI Binding, WebSockets | Matches the request type  
Tokens | Total tokens, Tokens In, Tokens Out | Compares token count with a threshold  
Duration | Less than, greater than | Compares duration with a threshold  
Feedback | Equals, does not equal (thumbs up, thumbs down, no feedback) | Matches feedback  
Metadata key | Equals, does not equal | Matches a metadata key  
Metadata value | Equals, does not equal | Matches a metadata value  
Log ID | Equals, does not equal | Matches a log ID  
Event ID | Equals, does not equal | Matches an event ID  
DLP action | `FLAG`, `BLOCK` | Matches the DLP action  
User agent | Equals, does not equal, contains | Matches the requesting client user agent  
  
## Use the Logs API

The Legacy Logs API lets you [list stored logs](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/logs/methods/list/). To delete matching logs programmatically, use the [`DELETE` logs endpoint](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/logs/methods/delete/).

[PreviousOverview](https://developers.cloudflare.com/ai-gateway/observability/logging/)[NextWorkers Logpush](https://developers.cloudflare.com/ai-gateway/observability/logging/logpush/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/observability/logging/legacy-logs.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
