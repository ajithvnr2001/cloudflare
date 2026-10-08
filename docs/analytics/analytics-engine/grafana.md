---
url: https://developers.cloudflare.com/analytics/analytics-engine/grafana/
title: Querying Workers Analytics Engine from Grafana \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:09.444910+00:00
---

# Querying Workers Analytics Engine from Grafana · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/analytics-engine/grafana/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /[Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/)
  4. /Querying from Grafana



# Querying from Grafana

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/analytics-engine/grafana/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewGrafana plugin setupQuerying timeseries data

Workers Analytics Engine is optimized for powering time series analytics that can be visualized using tools like Grafana. Every event written from the runtime is automatically populated with a `timestamp` field.

## Grafana plugin setup

We recommend the use of the [Altinity plugin for Clickhouse ↗︎](https://grafana.com/grafana/plugins/vertamedia-clickhouse-datasource/) for querying Workers Analytics Engine from Grafana.

Configure the plugin as follows:

  * URL: `https://api.cloudflare.com/client/v4/accounts/<account_id>/analytics_engine/sql`. Replace `<account_id>` with your 32 character account ID (available in the Cloudflare dashboard).
  * Leave all auth settings off.
  * Add a custom header with a name of `Authorization` and value set to `Bearer <token>`. Replace `<token>` with suitable API token string (refer to the [SQL API docs](https://developers.cloudflare.com/analytics/analytics-engine/sql-api/#authentication) for more information on this).
  * No other options need to be set.



## Querying timeseries data

For use in a dashboard, you usually want to aggregate some metric per time interval. This can be achieved by rounding and then grouping by the `timestamp` field. The following query rounds and groups in this way, and then computes an average across each time interval whilst taking into account [sampling](https://developers.cloudflare.com/analytics/analytics-engine/sql-api/#sampling).
    
    
    SELECT
        intDiv(toUInt32(timestamp), 60) * 60 AS t,
        blob1 AS label,
        SUM(_sample_interval * double1) / SUM(_sample_interval) AS average_metric
    FROM dataset_name
    WHERE 
        timestamp <= NOW() 
        AND timestamp > NOW() - INTERVAL '1' DAY
    GROUP BY blob1, t
    ORDER BY t

The Altinity plugin provides some useful macros that can simplify writing queries of this type. The macros require setting `Column:DateTime` to `timestamp` in the query builder, then they can be used like this:
    
    
    SELECT
        $timeSeries AS t,
        blob1 AS label,
        SUM(_sample_interval * double1) / SUM(_sample_interval) AS average_metric
    FROM dataset_name
    WHERE $timeFilter
    GROUP BY blob1, t
    ORDER BY t

This query will automatically adjust the rounding time depending on the zoom level and filter to the correct time range that is currently being displayed.

[PreviousType conversion functions](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/type-conversion-functions/)[NextQuerying from a Worker](https://developers.cloudflare.com/analytics/analytics-engine/worker-querying/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/analytics-engine/grafana.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
