---
url: https://developers.cloudflare.com/ai-gateway/observability/costs/
title: Costs \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:31.594150+00:00
---

# Costs · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/observability/costs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /Observability
  4. /Costs



# Costs

Last updated Sep 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/observability/costs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewTrack costs across AI providersCustom costs

Cost metrics are only available for endpoints where the models return token data and the model name in their responses.

## Track costs across AI providers

AI Gateway makes it easier to monitor and estimate token based costs across all your AI providers. This can help you:

  * Understand and compare usage costs between providers.
  * Monitor trends and estimate spend using consistent metrics.
  * Apply custom pricing logic to match negotiated rates.



Note

The cost metric is an **estimation** based on the number of tokens sent and received in requests. While this metric can help you monitor and predict cost trends, refer to your provider's dashboard for the most **accurate** cost details.

Caution

Providers may introduce new models or change their pricing. If you notice outdated cost data or are using a model not yet supported by our cost tracking, please [submit a request ↗︎](https://forms.gle/8kRa73wRnvq7bxL48)

## Custom costs

AI Gateway allows users to set custom costs when operating under special pricing agreements or negotiated rates. Custom costs can be applied at the request level, and when applied, they will override the default or public model costs. For more information on configuration of custom costs, please visit the [Custom Costs](https://developers.cloudflare.com/ai-gateway/configuration/custom-costs/) configuration page.

[PreviousAnalytics](https://developers.cloudflare.com/ai-gateway/observability/analytics/)[NextUser Insights](https://developers.cloudflare.com/ai-gateway/observability/user-insights/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/observability/costs.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
