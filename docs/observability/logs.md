---
url: https://developers.cloudflare.com/observability/logs/
title: Logs \u00b7 Cloudflare Observability docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:26.476888+00:00
---

# Logs · Cloudflare Observability docs

> Source: https://developers.cloudflare.com/observability/logs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Observability](https://developers.cloudflare.com/observability/)
  3. /Logs



# Logs

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/observability/logs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewChoose a datasetNarrow the resultsVisualize results

Use Logs to query structured events from supported Cloudflare products and services. Filter by time range and field values, then chart or inspect matching events.

You can use Logs to:

  * Inspect HTTP requests and security actions
  * Debug errors in [Workers](https://developers.cloudflare.com/workers/) and [Containers](https://developers.cloudflare.com/containers/)
  * Audit [R2](https://developers.cloudflare.com/r2/) bucket access and operations
  * Investigate [AI Gateway](https://developers.cloudflare.com/ai-gateway/) errors, latency, token usage, and costs
  * Query [Zero Trust](https://developers.cloudflare.com/cloudflare-one/) and network events

![Logs showing Worker query controls, outcome and duration visualizations, and a table of structured events.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2536,height=1298,format=webp/_astro/logs-workers-dashboard-overview.D6sJpjzt.png)

## Choose a dataset

Open the dataset selector to search available datasets, including HTTP requests, security events, Workers, Containers, R2, AI Gateway, and Issues. For domain-scoped datasets, select one domain or all domains.

Available fields and retention periods vary by dataset, and some datasets must be turned on in their source product.

![Dataset selector showing HTTP requests, Workers, Containers, R2, and Issues.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1200,height=365,format=webp/_astro/logs-dataset-selector.DicR71jE.png)

## Narrow the results

Use the field browser to search field names or browse categories. To create a filter, select a field, operator, and value.

You can also enter a query directly, either in the filter query language or as SQL against the selected dataset. The built-in reference covers field queries, comparison operators, functions, Boolean logic, examples, and keyboard shortcuts. To inspect one request, filter on its Ray ID.

Select a preset time range, enter a relative range, or select calendar dates. Results show the returned row count and query duration.

![Logs filter builder matching requests where Path equals /.env, with the generated query and filtered chart.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2170,height=1020,format=webp/_astro/logs-filter-builder.D4R0Ozg1.png)

## Visualize results

Create a visualization from a field, describe the chart you want in plain language, or configure one from scratch. Group results by one or more fields, or add, remove, and reorder custom series with separate labels, metrics, and filters. When Logs detects an anomaly in a series, select it to narrow the results to the affected time range and investigate.

Available chart types include:

  * **Single value:** Stat and Percentage
  * **Time series:** Timeseries, Bar Chart, and Stacked Area
  * **Categories:** Categorical Bar, Horizontal Bar, Vertical Bar, Doughnut Chart, and Top List
  * **Geospatial and flow:** Choropleth Country Map, Proportional Symbol Map, and Sankey Diagram
  * **Tabular data:** Table



Use automatic interval selection or select an interval from one minute to one day. Resize the visualization area, duplicate or remove a chart, and add the chart to a [custom dashboard](https://developers.cloudflare.com/analytics/custom-dashboards/).

![Logs visualizations showing Worker invocation outcomes, error outcomes, latency, and an empty chart ready to configure.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2414,height=1402,format=webp/_astro/logs-visualization-builder.DigfiOXH.png)

[PreviousOverview](https://developers.cloudflare.com/observability/)[NextDatasets](https://developers.cloudflare.com/observability/logs/datasets/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/observability/logs/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
