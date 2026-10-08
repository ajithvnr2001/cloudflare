---
url: https://developers.cloudflare.com/log-explorer/log-search/
title: Log Search \u00b7 Cloudflare Log Explorer docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:08.496102+00:00
---

# Log Search · Cloudflare Log Explorer docs

> Source: https://developers.cloudflare.com/log-explorer/log-search/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Log Explorer](https://developers.cloudflare.com/log-explorer/)
  3. /Log Search



# Log Search

Last updated Oct 7, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/log-explorer/log-search/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhen to use Log ExplorerUse Log Explorer Headers and cookies Save queriesIntegration with Security AnalyticsOptimize your queries Additional query optimization tips

Log Explorer enables you to store and explore your Cloudflare logs directly within the Cloudflare dashboard or API, giving you visibility into your logs without the need to forward them to third-party services. Logs are stored on Cloudflare's global network using the R2 object storage platform and can be queried via the dashboard or SQL API.

Log Search is now part of Observability Logs

Log Explorer datasets are queried from the [Logs](https://developers.cloudflare.com/observability/logs/) page under **Observability** in the Cloudflare dashboard. The **Log Explorer** menu is no longer shown in the dashboard navigation. Your enabled datasets, saved queries, and SQL queries continue to work on the Logs page, and the previous Log Search page remains available at its direct URL.

## When to use Log Explorer

Use Log Explorer when you need to investigate what actually happened with real production traffic:

  * Analyzing historical data and trends
  * Investigating security incidents after they occur
  * Searching for patterns across thousands of requests
  * Monitoring application performance over time
  * Providing forensic evidence to support teams



Use [Cloudflare Trace](https://developers.cloudflare.com/rules/trace-request/), shown as **Rule simulator** in the dashboard, when you need to test what would happen with a simulated request:

  * Understanding why a rule did not trigger as expected
  * Testing how your rules handle different request scenarios
  * Seeing the evaluation order of your rules
  * Simulating requests from different geolocations or conditions



The key difference is that Log Explorer shows actual traffic, while Cloudflare Trace shows simulated "what-if" scenarios. Both are separate from [Cloudflare Traces](https://developers.cloudflare.com/observability/traces/), which records how real requests move through Cloudflare.

## Use Log Explorer

You can filter and view your logs via the Cloudflare dashboard or the API.

  1. In the Cloudflare dashboard, go to **Observability** > **Logs**.

[ Go to **Logs** ↗ ](https://dash.cloudflare.com/?to=/:account/observability/logs)
  2. Open the dataset selector and choose a Log Explorer dataset, such as **HTTP requests**. For zone-scoped datasets, select one domain or all domains.

  3. Select a preset or custom time range.

  4. Add filters by selecting a field, an operator, and a value. To write SQL instead, select **Open SQL editor** , enter a query against the selected dataset, and select **Run query**.




SQL queries are available for Log Explorer datasets only. For the filter query language, functions, and keyboard shortcuts, refer to the built-in reference on the Logs page or the [Logs overview](https://developers.cloudflare.com/observability/logs/).

For example, to find an HTTP request with a specific [Ray ID](https://developers.cloudflare.com/fundamentals/reference/cloudflare-ray-id/), open the SQL editor and enter the following SQL query:
    
    
    SELECT
    	clientRequestScheme,
    	clientRequestHost,
    	clientRequestMethod,
    	edgeResponseStatus,
    	clientRequestUserAgent
    FROM http_requests
    WHERE RayID = '806c30a3cec56817'
    LIMIT 1

As another example, to find Cloudflare Access requests with selected columns from a specific timeframe you could perform the following SQL query:
    
    
    SELECT
    	CreatedAt,
    	AppDomain,
    	AppUUID,
    	Action,
    	Allowed,
    	Country,
    	RayID,
    	Email,
    	IPAddress,
    	UserUID
    FROM access_requests
    WHERE Date >= '2025-02-06' AND Date <= '2025-02-06' AND CreatedAt >= '2025-02-06T12:28:39Z' AND CreatedAt <= '2025-02-06T12:58:39Z'

### Headers and cookies

To query request headers, response headers, and cookies you must first enable logging for these fields using [Custom fields](https://developers.cloudflare.com/logs/logpush/logpush-job/custom-fields/). Configure the list of custom fields using the API or the dashboard; there is no need to modify the Logpush job itself.

The example below shows how to query HTTP requests by date, timestamp, client country, and a custom request header. Be sure to log the specific headers or cookies you plan to query in advance.
    
    
    SELECT clientip, clientrequesthost, clientrequestmethod, edgeendtimestamp, edgestarttimestamp, rayid, clientcountry, requestheaders
    FROM http_requests
    WHERE Date >= '2025-07-17'
      AND Date <= '2025-07-17'
      AND edgeendtimestamp >= '2025-07-17T07:54:19Z'
      AND edgeendtimestamp <= '2025-07-18T07:54:19Z'
      AND clientcountry = 'us'
      AND requestheaders."x-test-header" like '%654AM%';

### Save queries

After building your query, you can save it by selecting **Save search**. Provide a name and description to help identify it later. To view your saved searches, select **Saved searches**. Queries saved in the previous Log Search page appear as saved searches on the Logs page.

## Integration with Security Analytics

You can also access the Log Explorer dashboard directly from the [Security Analytics dashboard](https://developers.cloudflare.com/waf/analytics/security-analytics/#logs). When doing so, the filters you applied in Security Analytics will automatically carry over to your query in Log Explorer.

## Optimize your queries

All the tables supported by Log Explorer contain a special column called `date`, which helps to narrow down the amount of data that is scanned to respond to your query, resulting in faster query response times. The value of `date` must be in the form of `YYYY-MM-DD`. For example, to query logs that occurred on October 12, 2023, add the following to your `WHERE` clause: `date = '2023-10-12'`. The column supports the standard operators of `<`, `>`, and `=`.

  1. Log in to the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/login) and select your account.
  2. Go to **Observability** > **Logs** , select a Log Explorer dataset, and select **Open SQL editor**.
  3. Enter the following SQL query:


    
    
    SELECT
    	clientip,
    	clientrequesthost,
    	clientrequestmethod,
    	clientrequesturi,
    	edgeendtimestamp,
    	edgeresponsestatus,
    	originresponsestatus,
    	edgestarttimestamp,
    	rayid,
    	clientcountry,
    	clientrequestpath,
    	date
    FROM
    	http_requests
    WHERE
    	date = '2023-10-12' LIMIT 500

### Additional query optimization tips

  * Narrow your query time frame. Focus on a smaller time window to reduce the volume of data processed. This helps avoid querying excessive amounts of data and speeds up response times.
  * Omit `ORDER BY` and `LIMIT` clauses. These clauses can slow down queries, especially when dealing with large datasets. For queries that return a large number of records, reduce the time frame instead of limiting to the newest `N` records from a broader time frame.
  * Select only necessary columns. For example, replace `SELECT *` with the list of specific columns you need. You can also use `SELECT RayId` as a first iteration and follow up with a query that filters by the Ray IDs to retrieve additional columns. Additionally, you can use `SELECT COUNT(*)` to probe for time frames with matching records without retrieving the full dataset.



[PreviousOverview](https://developers.cloudflare.com/log-explorer/)[NextSQL queries supported](https://developers.cloudflare.com/log-explorer/sql-queries/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/log-explorer/log-search.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
