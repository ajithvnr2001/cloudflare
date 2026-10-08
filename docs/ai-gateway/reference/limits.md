---
url: https://developers.cloudflare.com/ai-gateway/reference/limits/
title: Limits \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:32.497631+00:00
---

# Limits · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/reference/limits/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /[Platform](https://developers.cloudflare.com/ai-gateway/reference/)
  4. /Limits



# Limits

Last updated Sep 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/reference/limits/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewGateway limitsLog limits New AI Gateway customers Existing AI Gateway customersLogpush limitsDLP limits

The following limits apply to gateway configurations, logs, and related features in Cloudflare's platform.

## Gateway limits

Feature | Limit  
---|---  
[Cacheable request size](https://developers.cloudflare.com/ai-gateway/features/caching/) | 25 MB per request  
[Cache TTL](https://developers.cloudflare.com/ai-gateway/features/caching/#cache-ttl-cf-aig-cache-ttl) | 1 month  
[Custom metadata](https://developers.cloudflare.com/ai-gateway/observability/custom-metadata/) | 5 entries per request  
Gateways free plan | 10 per account  
Gateways paid plan | 20 per account  
Gateway name length | 64 characters  
[Unified Billing](https://developers.cloudflare.com/ai-gateway/features/unified-billing/) request rate | 200 requests per 60 seconds per gateway 1  
  
1 This rate limit applies to requests that use Cloudflare-managed credentials through [Unified Billing](https://developers.cloudflare.com/ai-gateway/features/unified-billing/). When the limit is exceeded, AI Gateway returns a `429` error. This limit does not apply to requests that use your own provider keys through [bring your own keys (BYOK)](https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/).

## Log limits

### New AI Gateway customers

Customers who create their first gateway on or after September 24, 2026 follow [Workers Logs limits](https://developers.cloudflare.com/workers/observability/logs/workers-logs/#limits) and [Workers Logs pricing](https://developers.cloudflare.com/workers/observability/logs/workers-logs/#pricing).

### Existing AI Gateway customers

Customers who created a gateway before September 24, 2026 use [Legacy Logs](https://developers.cloudflare.com/ai-gateway/observability/logging/legacy-logs/). The following limits apply:

Feature | Limit  
---|---  
Log storage rate | 500 logs per second per gateway  
Logs stored, paid plan | 10 million per gateway  
Logs stored, free plan | 100,000 per account  
Stored log size | 10 MB per log  
  
The free plan limit applies across all gateways. For behavior at these limits, refer to [Legacy Logs storage](https://developers.cloudflare.com/ai-gateway/observability/logging/legacy-logs/#manage-storage).

## Logpush limits

These limits apply to all AI Gateway customers:

Feature | Limit  
---|---  
[Logpush jobs](https://developers.cloudflare.com/ai-gateway/observability/logging/logpush/) | 4 per account  
[Logpush log size](https://developers.cloudflare.com/ai-gateway/observability/logging/logpush/) | 1 MB per log  
  
## DLP limits

[DLP](https://developers.cloudflare.com/ai-gateway/features/dlp/) for AI Gateway uses shared [Cloudflare One DLP profiles](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/). The following limits apply to DLP profiles and detection entries at the account level:

Feature | Limit  
---|---  
Custom entries | 25  
Exact Data Match cells per spreadsheet | 100,000  
Custom Wordlist keywords per spreadsheet | 200  
Custom Wordlist keywords per account | 1,000  
Dataset cells per account | 1,000,000  
  
DLP profiles are shared with Cloudflare One and are not coupled to individual gateways. You can apply the same DLP profiles across multiple gateways without additional profile limits. There is no separate limit on the number of DLP policies per gateway.

Need a higher limit?

To request an increase to a limit, complete the [Limit Increase Request Form ↗︎](https://forms.gle/cuXu1QnQCrSNkkaS8). If the limit can be increased, Cloudflare will contact you with next steps.

[PreviousOverview](https://developers.cloudflare.com/ai-gateway/reference/)[NextTroubleshooting](https://developers.cloudflare.com/ai-gateway/reference/troubleshooting/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/reference/limits.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
