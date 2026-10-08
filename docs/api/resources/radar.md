---
url: https://developers.cloudflare.com/api/resources/radar/
title: Radar | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:19:09.125185+00:00
---

# Radar | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/radar/

[API Reference](https://developers.cloudflare.com/api)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Radar

#### RadarAgent Readiness

##### [Get agent readiness summary](https://developers.cloudflare.com/api/resources/radar/subresources/agent_readiness/methods/summary)

GET/radar/agent_readiness/summary/{dimension}

##### ModelsExpand Collapse 

AgentReadinessSummaryResponse object { meta, summary_0 } 

meta: object { date, domainCategories, lastUpdated, 4 more } 

date: string

Date of the returned scan (YYYY-MM-DD). May differ from the requested date if no scan exists for that exact date.

formatdate

domainCategories: array of object { name, value } 

Available domain sub-categories with their scan counts. Use as filter options for the domainCategory parameter.

name: string

Sub-category name.

value: number

Number of successfully scanned domains in this sub-category.

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

successfulDomains: number

Domains successfully scanned (excludes errors).

totalDomains: number

Total domains attempted in the scan.

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: map[string]

#### RadarAI

#### RadarAITo Markdown

##### [Convert uploaded files to Markdown](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/to_markdown/methods/create)

Deprecated

POST/accounts/{account_id}/ai/tomarkdown

##### ModelsExpand Collapse 

ToMarkdownCreateResponse object { data, format, mimeType, 2 more } 

data: string

format: string

mimeType: string

name: string

tokens: string

#### RadarAIInference

##### [Get Workers AI inference distribution by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/inference/methods/summary_v2)

GET/radar/ai/inference/summary/{dimension}

##### [Get time series distribution of Workers AI inference by dimension.](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/inference/methods/timeseries_groups_v2)

GET/radar/ai/inference/timeseries_groups/{dimension}

##### ModelsExpand Collapse 

InferenceSummaryV2Response object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: map[string]

InferenceTimeseriesGroupsV2Response object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

#### RadarAIInferenceSummary

##### [Get Workers AI models summary](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/inference/subresources/summary/methods/model)

Deprecated

GET/radar/ai/inference/summary/model

##### [Get Workers AI tasks summary](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/inference/subresources/summary/methods/task)

Deprecated

GET/radar/ai/inference/summary/task

##### ModelsExpand Collapse 

SummaryModelResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: map[string]

SummaryTaskResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: map[string]

#### RadarAIInferenceTimeseries Groups

#### RadarAIInferenceTimeseries GroupsSummary

##### [Get Workers AI models time series](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/inference/subresources/timeseries_groups/subresources/summary/methods/model)

Deprecated

GET/radar/ai/inference/timeseries_groups/model

##### [Get Workers AI tasks time series](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/inference/subresources/timeseries_groups/subresources/summary/methods/task)

Deprecated

GET/radar/ai/inference/timeseries_groups/task

##### ModelsExpand Collapse 

SummaryModelResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

SummaryTaskResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

#### RadarAIBots

##### [Get AI bots HTTP requests distribution by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/bots/methods/summary_v2)

GET/radar/ai/bots/summary/{dimension}

##### [Get AI bots HTTP requests time series](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/bots/methods/timeseries)

GET/radar/ai/bots/timeseries

##### [Get time series distribution of AI bots HTTP requests by dimension.](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/bots/methods/timeseries_groups)

GET/radar/ai/bots/timeseries_groups/{dimension}

##### ModelsExpand Collapse 

BotSummaryV2Response object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: map[string]

BotTimeseriesResponse object { meta } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

BotTimeseriesGroupsResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

#### RadarAIBotsSummary

##### [Get AI user agents summary](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/bots/subresources/summary/methods/user_agent)

Deprecated

GET/radar/ai/bots/summary/user_agent

##### ModelsExpand Collapse 

SummaryUserAgentResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: map[string]

#### RadarAITimeseries Groups

##### [Get AI user agents time series](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/timeseries_groups/methods/user_agent)

Deprecated

GET/radar/ai/bots/timeseries_groups/user_agent

##### [Get AI bots HTTP requests distribution by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/timeseries_groups/methods/summary)

Deprecated

GET/radar/ai/bots/summary/{dimension}

##### [Get AI bots HTTP requests time series](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/timeseries_groups/methods/timeseries)

Deprecated

GET/radar/ai/bots/timeseries

##### [Get time series distribution of AI bots HTTP requests by dimension.](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/timeseries_groups/methods/timeseries_groups)

Deprecated

GET/radar/ai/bots/timeseries_groups/{dimension}

##### ModelsExpand Collapse 

TimeseriesGroupUserAgentResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

TimeseriesGroupSummaryResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: map[string]

TimeseriesGroupTimeseriesResponse object { meta } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

TimeseriesGroupTimeseriesGroupsResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

#### RadarAIMarkdown For Agents

##### [Get AI markdown for agents reduction ratio summary](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/markdown_for_agents/methods/summary)

GET/radar/ai/markdown_for_agents/summary

##### [Get AI markdown for agents reduction ratio time series](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/markdown_for_agents/methods/timeseries)

GET/radar/ai/markdown_for_agents/timeseries

##### ModelsExpand Collapse 

MarkdownForAgentSummaryResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { value } 

value: string

A numeric string that can include decimals and infinity values.

MarkdownForAgentTimeseriesResponse object { meta } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

#### RadarCT

##### [Get certificate distribution by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/ct/methods/summary)

GET/radar/ct/summary/{dimension}

##### [Get certificates time series](https://developers.cloudflare.com/api/resources/radar/subresources/ct/methods/timeseries)

GET/radar/ct/timeseries

##### [Get time series of certificate distribution by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/ct/methods/timeseries_groups)

GET/radar/ct/timeseries_groups/{dimension}

##### ModelsExpand Collapse 

CTSummaryResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: map[string] or object { rfc6962, static }  or object { gt_121d, gt_16d_lte_31d, gt_31d_lte_91d, 3 more }  or 5 more

One of the following:

map[string]

object { rfc6962, static } 

rfc6962: string

static: string

object { gt_121d, gt_16d_lte_31d, gt_31d_lte_91d, 3 more } 

gt_121d: string

gt_16d_lte_31d: string

gt_31d_lte_91d: string

gt_3d_lte_16d: string

gt_91d_lte_121d: string

lte_3d: string

object { CERTIFICATE, PRECERTIFICATE } 

CERTIFICATE: string

PRECERTIFICATE: string

object { EXPIRED, VALID } 

EXPIRED: string

VALID: string

object { NEGATIVE, POSITIVE } 

NEGATIVE: string

POSITIVE: string

object { DSA, ECDSA, RSA } 

DSA: string

ECDSA: string

RSA: string

object { domain, extended, organization, unknown } 

domain: string

extended: string

organization: string

unknown: string

CTTimeseriesResponse object { meta } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

CTTimeseriesGroupsResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps }  or object { rfc6962, static }  or object { gt_121d, gt_16d_lte_31d, gt_31d_lte_91d, 3 more }  or 5 more

One of the following:

UnnamedSchemaRef7826220e105d84352ba1108d9ed88e55 object { timestamps } 

timestamps: array of string

object { rfc6962, static } 

rfc6962: array of string

static: array of string

object { gt_121d, gt_16d_lte_31d, gt_31d_lte_91d, 3 more } 

gt_121d: array of string

gt_16d_lte_31d: array of string

gt_31d_lte_91d: array of string

gt_3d_lte_16d: array of string

gt_91d_lte_121d: array of string

lte_3d: array of string

object { CERTIFICATE, PRECERTIFICATE } 

CERTIFICATE: array of string

PRECERTIFICATE: array of string

object { EXPIRED, VALID } 

EXPIRED: array of string

VALID: array of string

object { NEGATIVE, POSITIVE } 

NEGATIVE: array of string

POSITIVE: array of string

object { DSA, ECDSA, RSA } 

DSA: array of string

ECDSA: array of string

RSA: array of string

object { domain, extended, organization, unknown } 

domain: array of string

extended: array of string

organization: array of string

unknown: array of string

#### RadarCTAuthorities

##### [Get certificate authority details](https://developers.cloudflare.com/api/resources/radar/subresources/ct/subresources/authorities/methods/get)

GET/radar/ct/authorities/{ca_slug}

##### [List certificate authorities](https://developers.cloudflare.com/api/resources/radar/subresources/ct/subresources/authorities/methods/list)

GET/radar/ct/authorities

##### ModelsExpand Collapse 

AuthorityGetResponse object { certificateAuthority } 

certificateAuthority: object { appleStatus, authorityKeyIdentifier, certificateRecordType, 15 more } 

appleStatus: "INCLUDED" or "NOT_YET_INCLUDED" or "NOT_INCLUDED" or 4 more

The inclusion status of a Certificate Authority (CA) in the trust store.

One of the following:

"INCLUDED"

"NOT_YET_INCLUDED"

"NOT_INCLUDED"

"NOT_BEFORE"

"REMOVED"

"DISABLED"

"BLOCKED"

authorityKeyIdentifier: string

The authorityKeyIdentifier value extracted from the certificate PEM.

certificateRecordType: "ROOT_CERTIFICATE" or "INTERMEDIATE_CERTIFICATE"

Specifies the type of certificate in the trust chain.

One of the following:

"ROOT_CERTIFICATE"

"INTERMEDIATE_CERTIFICATE"

chromeStatus: "INCLUDED" or "NOT_YET_INCLUDED" or "NOT_INCLUDED" or 4 more

The inclusion status of a Certificate Authority (CA) in the trust store.

One of the following:

"INCLUDED"

"NOT_YET_INCLUDED"

"NOT_INCLUDED"

"NOT_BEFORE"

"REMOVED"

"DISABLED"

"BLOCKED"

country: string

The two-letter ISO country code where the CA organization is based.

countryName: string

The full country name corresponding to the country code.

microsoftStatus: "INCLUDED" or "NOT_YET_INCLUDED" or "NOT_INCLUDED" or 4 more

The inclusion status of a Certificate Authority (CA) in the trust store.

One of the following:

"INCLUDED"

"NOT_YET_INCLUDED"

"NOT_INCLUDED"

"NOT_BEFORE"

"REMOVED"

"DISABLED"

"BLOCKED"

mozillaStatus: "INCLUDED" or "NOT_YET_INCLUDED" or "NOT_INCLUDED" or 4 more

The inclusion status of a Certificate Authority (CA) in the trust store.

One of the following:

"INCLUDED"

"NOT_YET_INCLUDED"

"NOT_INCLUDED"

"NOT_BEFORE"

"REMOVED"

"DISABLED"

"BLOCKED"

name: string

The full name of the certificate authority (CA).

owner: string

The organization that owns and operates the CA.

parentName: string

The name of the parent/root certificate authority that issued this intermediate certificate.

parentSha256Fingerprint: string

The SHA-256 fingerprint of the parent certificate.

related: array of object { certificateRecordType, name, revocationStatus, sha256Fingerprint } 

CAs from the same owner.

certificateRecordType: "ROOT_CERTIFICATE" or "INTERMEDIATE_CERTIFICATE"

Specifies the type of certificate in the trust chain.

One of the following:

"ROOT_CERTIFICATE"

"INTERMEDIATE_CERTIFICATE"

name: string

The full name of the certificate authority (CA).

revocationStatus: "NOT_REVOKED" or "REVOKED" or "PARENT_CERT_REVOKED"

The current revocation status of a Certificate Authority (CA) certificate.

One of the following:

"NOT_REVOKED"

"REVOKED"

"PARENT_CERT_REVOKED"

sha256Fingerprint: string

The SHA-256 fingerprint of the intermediate certificate.

revocationStatus: "NOT_REVOKED" or "REVOKED" or "PARENT_CERT_REVOKED"

The current revocation status of a Certificate Authority (CA) certificate.

One of the following:

"NOT_REVOKED"

"REVOKED"

"PARENT_CERT_REVOKED"

sha256Fingerprint: string

The SHA-256 fingerprint of the intermediate certificate.

subjectKeyIdentifier: string

The subjectKeyIdentifier value extracted from the certificate PEM.

validFrom: string

The start date of the certificate’s validity period (ISO format).

formatdate

validTo: string

The end date of the certificate’s validity period (ISO format).

formatdate

AuthorityListResponse object { certificateAuthorities } 

certificateAuthorities: array of object { certificateRecordType, country, countryName, 6 more } 

certificateRecordType: "ROOT_CERTIFICATE" or "INTERMEDIATE_CERTIFICATE"

Specifies the type of certificate in the trust chain.

One of the following:

"ROOT_CERTIFICATE"

"INTERMEDIATE_CERTIFICATE"

country: string

The two-letter ISO country code where the CA organization is based.

countryName: string

The full country name corresponding to the country code.

name: string

The full name of the certificate authority (CA).

owner: string

The organization that owns and operates the CA.

parentName: string

The name of the parent/root certificate authority that issued this intermediate certificate.

parentSha256Fingerprint: string

The SHA-256 fingerprint of the parent certificate.

revocationStatus: "NOT_REVOKED" or "REVOKED" or "PARENT_CERT_REVOKED"

The current revocation status of a Certificate Authority (CA) certificate.

One of the following:

"NOT_REVOKED"

"REVOKED"

"PARENT_CERT_REVOKED"

sha256Fingerprint: string

The SHA-256 fingerprint of the intermediate certificate.

#### RadarCTLogs

##### [Get certificate log details](https://developers.cloudflare.com/api/resources/radar/subresources/ct/subresources/logs/methods/get)

GET/radar/ct/logs/{log_slug}

##### [List certificate logs](https://developers.cloudflare.com/api/resources/radar/subresources/ct/subresources/logs/methods/list)

GET/radar/ct/logs

##### ModelsExpand Collapse 

LogGetResponse object { certificateLog } 

certificateLog: object { api, avgThroughput, description, 12 more } 

api: "RFC6962" or "STATIC"

The API standard that the certificate log follows.

One of the following:

"RFC6962"

"STATIC"

avgThroughput: number

The average throughput of the CT log, measured in certificates per hour (certs/hour).

description: string

A brief description of the certificate log.

endExclusive: string

The end date and time for when the log will stop accepting certificates.

formatdate-time

lastUpdate: string

Timestamp of the most recent update to the CT log.

formatdate-time

operator: string

The organization responsible for operating the certificate log.

performance: object { endpoints, responseTime, uptime } 

Log performance metrics, including averages and per-endpoint details.

endpoints: array of object { endpoint, responseTime, uptime } 

endpoint: "add-chain (new)" or "add-chain (old)" or "add-pre-chain (new)" or 4 more

The certificate log endpoint names used in performance metrics.

One of the following:

"add-chain (new)"

"add-chain (old)"

"add-pre-chain (new)"

"add-pre-chain (old)"

"get-entries"

"get-roots"

"get-sth"

responseTime: number

uptime: number

responseTime: number

uptime: number

related: array of object { description, endExclusive, slug, 2 more } 

Logs from the same operator.

description: string

A brief description of the certificate log.

endExclusive: string

The end date and time for when the log will stop accepting certificates.

formatdate-time

slug: string

A URL-friendly, kebab-case identifier for the certificate log.

startInclusive: string

The start date and time for when the log starts accepting certificates.

formatdate-time

state: "USABLE" or "PENDING" or "QUALIFIED" or 3 more

The current state of the certificate log. More details about log states can be found here: <https://googlechrome.github.io/CertificateTransparency/log_states.html>

One of the following:

"USABLE"

"PENDING"

"QUALIFIED"

"READ_ONLY"

"RETIRED"

"REJECTED"

slug: string

A URL-friendly, kebab-case identifier for the certificate log.

startInclusive: string

The start date and time for when the log starts accepting certificates.

formatdate-time

state: "USABLE" or "PENDING" or "QUALIFIED" or 3 more

The current state of the certificate log. More details about log states can be found here: <https://googlechrome.github.io/CertificateTransparency/log_states.html>

One of the following:

"USABLE"

"PENDING"

"QUALIFIED"

"READ_ONLY"

"RETIRED"

"REJECTED"

stateTimestamp: string

Timestamp of when the log state was last updated.

formatdate-time

submittableCertCount: string

Number of certificates that are eligible for inclusion to this log but have not been included yet. Based on certificates signed by trusted root CAs within the log’s accepted date range.

submittedCertCount: string

Number of certificates already included in this CT log.

url: string

The URL for the certificate log.

LogListResponse object { certificateLogs } 

certificateLogs: array of object { api, description, endExclusive, 6 more } 

api: "RFC6962" or "STATIC"

The API standard that the certificate log follows.

One of the following:

"RFC6962"

"STATIC"

description: string

A brief description of the certificate log.

endExclusive: string

The end date and time for when the log will stop accepting certificates.

formatdate-time

operator: string

The organization responsible for operating the certificate log.

slug: string

A URL-friendly, kebab-case identifier for the certificate log.

startInclusive: string

The start date and time for when the log starts accepting certificates.

formatdate-time

state: "USABLE" or "PENDING" or "QUALIFIED" or 3 more

The current state of the certificate log. More details about log states can be found here: <https://googlechrome.github.io/CertificateTransparency/log_states.html>

One of the following:

"USABLE"

"PENDING"

"QUALIFIED"

"READ_ONLY"

"RETIRED"

"REJECTED"

stateTimestamp: string

Timestamp of when the log state was last updated.

formatdate-time

url: string

The URL for the certificate log.

#### RadarAnnotations

##### [Get latest annotations](https://developers.cloudflare.com/api/resources/radar/subresources/annotations/methods/list)

GET/radar/annotations

##### ModelsExpand Collapse 

AnnotationListResponse object { annotations } 

annotations: array of object { id, asns, asnsDetails, 15 more } 

id: string

asns: array of number

asnsDetails: array of object { asn, location, name } 

asn: string

location: object { code, name } 

code: string

name: string

name: string

dataSource: string

description: string

endDate: string

entities: array of object { entityName, entityType, entityValue } 

entityName: string

entityType: string

entityValue: string

eventType: string

geoIds: array of string

linkedUrl: string

locations: array of string

locationsDetails: array of object { code, name } 

code: string

name: string

origins: array of string

originsDetails: array of object { name, origin } 

name: string

origin: string

outage: object { outageCause, outageType } 

outageCause: string

outageType: string

scope: string

startDate: string

tags: array of string

#### RadarAnnotationsOutages

##### [Get latest Internet outages and anomalies](https://developers.cloudflare.com/api/resources/radar/subresources/annotations/subresources/outages/methods/get)

GET/radar/annotations/outages

##### [Get the number of outages by location](https://developers.cloudflare.com/api/resources/radar/subresources/annotations/subresources/outages/methods/locations)

GET/radar/annotations/outages/locations

##### ModelsExpand Collapse 

OutageGetResponse object { annotations } 

annotations: array of object { id, asns, asnsDetails, 15 more } 

id: string

asns: array of number

asnsDetails: array of object { asn, location, name } 

asn: string

location: object { code, name } 

code: string

name: string

name: string

dataSource: string

description: string

endDate: string

formatdate-time

entities: array of object { entityName, entityType, entityValue } 

entityName: string

entityType: string

entityValue: string

eventType: string

geoIds: array of string

linkedUrl: string

locations: array of string

locationsDetails: array of object { code, name } 

code: string

name: string

origins: array of string

originsDetails: array of object { name, origin } 

name: string

origin: string

outage: object { outageCause, outageType } 

outageCause: string

outageType: string

scope: string

startDate: string

formatdate-time

tags: array of string

OutageLocationsResponse object { annotations } 

annotations: array of object { clientCountryAlpha2, clientCountryName, value } 

clientCountryAlpha2: string

clientCountryName: string

value: string

A numeric string.

#### RadarBGP

##### [Get BGP time series](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/methods/timeseries)

GET/radar/bgp/timeseries

##### ModelsExpand Collapse 

BGPTimeseriesResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, lastUpdated } 

aggInterval: "15m" or "1h" or "1d" or "1w"

One of the following:

"15m"

"1h"

"1d"

"1w"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

formatdate-time

serie_0: object { timestamps, values } 

timestamps: array of string

values: array of string

#### RadarBGPLeaks

#### RadarBGPLeaksEvents

##### [Get BGP route leak events](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/leaks/subresources/events/methods/list)

GET/radar/bgp/leaks/events

##### ModelsExpand Collapse 

EventListResponse object { asn_info, events } 

asn_info: array of object { asn, country_code, org_name } 

asn: number

country_code: string

org_name: string

events: array of object { id, countries, detected_ts, 10 more } 

id: number

countries: array of string

detected_ts: string

finished: boolean

leak_asn: number

leak_count: number

leak_seg: array of number

leak_type: number

max_ts: string

min_ts: string

origin_count: number

peer_count: number

prefix_count: number

#### RadarBGPTop

##### [Get top prefixes by BGP updates](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/top/methods/prefixes)

GET/radar/bgp/top/prefixes

##### ModelsExpand Collapse 

TopPrefixesResponse object { meta, top_0 } 

meta: object { dateRange } 

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

top_0: array of object { prefix, value } 

prefix: string

value: string

A numeric string.

#### RadarBGPTopAses

##### [Get top ASes by BGP updates](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/top/subresources/ases/methods/get)

GET/radar/bgp/top/ases

##### [Get top ASes by prefix count](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/top/subresources/ases/methods/prefixes)

GET/radar/bgp/top/ases/prefixes

##### ModelsExpand Collapse 

AseGetResponse object { meta, top_0 } 

meta: object { dateRange } 

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

top_0: array of object { asn, ASName, value } 

asn: number

ASName: string

value: string

Percentage of updates by this AS out of the total updates by all autonomous systems.

AsePrefixesResponse object { asns, meta } 

asns: array of object { asn, country, name, pfxs_count } 

asn: number

country: string

name: string

pfxs_count: number

meta: object { data_time, query_time, total_peers } 

data_time: string

query_time: string

total_peers: number

#### RadarBGPHijacks

#### RadarBGPHijacksEvents

##### [Get BGP hijack events](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/hijacks/subresources/events/methods/list)

GET/radar/bgp/hijacks/events

##### ModelsExpand Collapse 

EventListResponse object { asn_info, events, total_monitors } 

asn_info: array of object { asn, country_code, org_name } 

asn: number

country_code: string

org_name: string

events: array of object { id, confidence_score, duration, 15 more } 

id: number

confidence_score: number

duration: number

event_type: number

hijack_msgs_count: number

hijacker_asn: number

hijacker_country: string

is_stale: boolean

max_hijack_ts: string

max_msg_ts: string

min_hijack_ts: string

on_going_count: number

peer_asns: array of number

peer_ip_count: number

prefixes: array of string

tags: array of object { name, score } 

name: string

score: number

victim_asns: array of number

victim_countries: array of string

total_monitors: number

#### RadarBGPRoutes

##### [Get Multi-Origin AS (MOAS) prefixes](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/methods/moas)

GET/radar/bgp/routes/moas

##### [Get prefix-to-ASN mapping](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/methods/pfx2as)

GET/radar/bgp/routes/pfx2as

##### [Get BGP routing table stats ](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/methods/stats)

GET/radar/bgp/routes/stats

##### [List ASes from global routing tables](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/methods/ases)

GET/radar/bgp/routes/ases

##### [Get real-time BGP routes for a prefix](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/methods/realtime)

GET/radar/bgp/routes/realtime

##### ModelsExpand Collapse 

RouteMoasResponse object { meta, moas } 

meta: object { data_time, query_time, total_peers } 

data_time: string

query_time: string

total_peers: number

moas: array of object { origins, prefix } 

origins: array of object { origin, peer_count, rpki_validation } 

origin: number

peer_count: number

rpki_validation: string

prefix: string

RoutePfx2asResponse object { meta, prefix_origins } 

meta: object { data_time, query_time, total_peers } 

data_time: string

query_time: string

total_peers: number

prefix_origins: array of object { origin, peer_count, prefix, rpki_validation } 

origin: number

peer_count: number

prefix: string

rpki_validation: string

RouteStatsResponse object { meta, stats } 

meta: object { data_time, query_time, total_peers } 

data_time: string

query_time: string

total_peers: number

stats: object { distinct_origins, distinct_origins_ipv4, distinct_origins_ipv6, 15 more } 

distinct_origins: number

distinct_origins_ipv4: number

distinct_origins_ipv6: number

distinct_prefixes: number

distinct_prefixes_ipv4: number

distinct_prefixes_ipv6: number

routes_invalid: number

routes_invalid_ipv4: number

routes_invalid_ipv6: number

routes_total: number

routes_total_ipv4: number

routes_total_ipv6: number

routes_unknown: number

routes_unknown_ipv4: number

routes_unknown_ipv6: number

routes_valid: number

routes_valid_ipv4: number

routes_valid_ipv6: number

RouteAsesResponse object { asns, meta } 

asns: array of object { asn, coneSize, country, 7 more } 

asn: number

coneSize: number

AS’s customer cone size.

country: string

Alpha-2 code for the AS’s registration country.

ipv4Count: number

Number of IPv4 addresses originated by the AS.

ipv6Count: string

Number of IPv6 addresses originated by the AS.

name: string

Name of the AS.

pfxsCount: number

Number of total IP prefixes originated by the AS.

rpkiInvalid: number

Number of RPKI invalid prefixes originated by the AS.

rpkiUnknown: number

Number of RPKI unknown prefixes originated by the AS.

rpkiValid: number

Number of RPKI valid prefixes originated by the AS.

meta: object { dataTime, queryTime, totalPeers } 

dataTime: string

The timestamp of when the data is generated.

queryTime: string

The timestamp of the query.

totalPeers: number

Total number of route collector peers used to generate this data.

RouteRealtimeResponse object { meta, routes } 

meta: object { asn_info, collectors, data_time, 2 more } 

asn_info: array of object { as_name, asn, country_code, 2 more } 

as_name: string

Name of the autonomous system.

asn: number

AS number.

country_code: string

Alpha-2 code for the AS’s registration country.

org_id: string

Organization ID.

org_name: string

Organization name.

collectors: array of object { collector, latest_realtime_ts, latest_rib_ts, 4 more } 

collector: string

Public route collector ID.

latest_realtime_ts: string

Latest real-time stream timestamp for this collector.

latest_rib_ts: string

Latest RIB dump MRT file timestamp for this collector.

latest_updates_ts: string

Latest BGP updates MRT file timestamp for this collector.

peers_count: number

Total number of collector peers used from this collector.

peers_v4_count: number

Total number of collector peers used from this collector for IPv4 prefixes.

peers_v6_count: number

Total number of collector peers used from this collector for IPv6 prefixes.

data_time: string

The most recent data timestamp for from the real-time sources.

prefix_origins: array of object { origin, prefix, rpki_validation, 3 more } 

origin: number

Origin ASN.

prefix: string

IP prefix of this query.

rpki_validation: string

Prefix-origin RPKI validation: valid, invalid, unknown.

total_peers: number

Total number of peers.

total_visible: number

Total number of peers seeing this prefix.

visibility: number

Ratio of peers seeing this prefix to total number of peers.

query_time: string

The timestamp of this query.

routes: array of object { as_path, collector, communities, 2 more } 

as_path: array of number

AS-level path for this route, from collector to origin.

collector: string

Public collector ID for this route.

communities: array of string

BGP community values.

prefix: string

IP prefix of this query.

timestamp: string

Latest timestamp of change for this route.

#### RadarBGPRoutesUpstreams

##### [Get upstream composition time series for an AS](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/subresources/upstreams/methods/timeseries)

GET/radar/bgp/routes/upstreams/{asn}/timeseries

##### ModelsExpand Collapse 

UpstreamTimeseriesResponse object { meta, serie_0 } 

meta: object { dataTime, effectiveCollector, queryTime, stale } 

dataTime: string

Timestamp of the underlying RIB data.

formatdate-time

effectiveCollector: string

queryTime: string

Timestamp when the query was executed.

formatdate-time

stale: boolean

serie_0: object { timestamps } 

timestamps: array of string

#### RadarBGPRoutesPaths

##### [Get tier-1 path segments for an AS](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/subresources/paths/methods/list)

GET/radar/bgp/routes/paths/{asn}

##### ModelsExpand Collapse 

PathListResponse object { asnInfo, collectors, meta, paths } 

asnInfo: map[object { asn, country, name } ]

asn: number

ASN number.

country: string

Alpha-2 country code.

name: string

AS name.

collectors: array of string

meta: object { dataTime, effectiveCollector, queryTime, stale } 

dataTime: string

Timestamp of the underlying RIB data.

formatdate-time

effectiveCollector: string

queryTime: string

Timestamp when the query was executed.

formatdate-time

stale: boolean

paths: array of object { collectors, pathsCount, peersCount, segment } 

collectors: array of string

pathsCount: number

peersCount: number

segment: array of number

#### RadarBGPIPs

##### [Get announced IP address space time series](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/ips/methods/timeseries)

GET/radar/bgp/ips/timeseries

##### ModelsExpand Collapse 

IPTimeseriesResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 4 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

delay: optional object { asn_data, country_data, healthy, nowTs } 

asn_data: object { delaySecs, delayStr, healthy, latest } 

delaySecs: number

delayStr: string

healthy: boolean

latest: object { entries_count, path, timestamp } 

entries_count: number

path: string

timestamp: number

country_data: object { delaySecs, delayStr, healthy, latest } 

delaySecs: number

delayStr: string

healthy: boolean

latest: object { count, timestamp } 

count: number

timestamp: number

healthy: boolean

nowTs: number

serie_0: object { ipv4, ipv6, timestamps } 

ipv4: array of string

ipv6: array of string

timestamps: array of string

#### RadarBGPIPsTop

##### [Get top ASes by announced IP space](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/ips/subresources/top/methods/ases)

GET/radar/bgp/ips/top/ases

##### ModelsExpand Collapse 

TopAsesResponse object { anchorTs, asns, country, metric } 

anchorTs: string

formatdate-time

asns: array of object { asn, v4_24s, v6_48s } 

asn: number

v4_24s: number

v6_48s: number

country: string

metric: string

#### RadarBGPRPKI

#### RadarBGPRPKIASPA

##### [Get ASPA objects snapshot](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/snapshot)

GET/radar/bgp/rpki/aspa/snapshot

##### [Get ASPA changes over time](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/changes)

GET/radar/bgp/rpki/aspa/changes

##### [Get ASPA count time series](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/timeseries)

GET/radar/bgp/rpki/aspa/timeseries

##### ModelsExpand Collapse 

ASPASnapshotResponse object { asnInfo, aspaObjects, meta } 

asnInfo: object { "13335" } 

"13335": object { asn, country, name } 

asn: number

ASN number.

country: string

Alpha-2 country code.

name: string

AS name.

aspaObjects: array of object { customerAsn, providers } 

customerAsn: number

The customer ASN publishing the ASPA object.

providers: array of number

meta: object { dataTime, queryTime, totalCount } 

dataTime: string

Timestamp of the underlying data.

formatdate-time

queryTime: string

Timestamp when the query was executed.

formatdate-time

totalCount: number

Total number of ASPA objects.

ASPAChangesResponse object { asnInfo, changes, meta } 

asnInfo: object { "13335" } 

"13335": object { asn, country, name } 

asn: number

ASN number.

country: string

Alpha-2 country code.

name: string

AS name.

changes: array of object { customersAdded, customersRemoved, date, 4 more } 

customersAdded: number

Number of new ASPA objects created.

customersRemoved: number

Number of ASPA objects deleted.

date: string

Date of the changes in ISO 8601 format.

formatdate-time

entries: array of object { customerAsn, providers, type } 

customerAsn: number

The customer ASN affected.

providers: array of number

type: "CustomerAdded" or "CustomerRemoved" or "ProvidersAdded" or "ProvidersRemoved"

One of the following:

"CustomerAdded"

"CustomerRemoved"

"ProvidersAdded"

"ProvidersRemoved"

providersAdded: number

Number of providers added to existing objects.

providersRemoved: number

Number of providers removed from existing objects.

totalCount: number

Running total of active ASPA objects after this day.

meta: object { dataTime, queryTime } 

dataTime: string

Timestamp of the underlying data.

formatdate-time

queryTime: string

Timestamp when the query was executed.

formatdate-time

ASPATimeseriesResponse object { meta, serie_0 } 

meta: object { dataTime, queryTime } 

dataTime: string

Timestamp of the underlying data.

formatdate-time

queryTime: string

Timestamp when the query was executed.

formatdate-time

serie_0: object { timestamps, values } 

timestamps: array of string

values: array of string

#### RadarBGPRPKIRoas

##### [Get RPKI ROA deployment time series](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/roas/methods/timeseries)

GET/radar/bgp/rpki/roas/timeseries

##### ModelsExpand Collapse 

RoaTimeseriesResponse object { meta, serie_0 } 

meta: object { dataTime, queryTime } 

dataTime: string

Timestamp of the underlying data.

formatdate-time

queryTime: string

Timestamp when the query was executed.

formatdate-time

serie_0: object { timestamps, values } 

timestamps: array of string

values: array of string

#### RadarBots

##### [List bots](https://developers.cloudflare.com/api/resources/radar/subresources/bots/methods/list)

GET/radar/bots

##### [Get bot details](https://developers.cloudflare.com/api/resources/radar/subresources/bots/methods/get)

GET/radar/bots/{bot_slug}

##### [Get bots HTTP requests distribution by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/bots/methods/summary)

GET/radar/bots/summary/{dimension}

##### [Get bots HTTP requests time series](https://developers.cloudflare.com/api/resources/radar/subresources/bots/methods/timeseries)

GET/radar/bots/timeseries

##### [Get time series distribution of bots HTTP requests by dimension.](https://developers.cloudflare.com/api/resources/radar/subresources/bots/methods/timeseries_groups)

GET/radar/bots/timeseries_groups/{dimension}

##### ModelsExpand Collapse 

BotListResponse object { bots } 

bots: array of object { category, description, kind, 4 more } 

category: string

The category of the bot.

description: string

A summary for the bot (e.g., purpose).

Deprecatedkind: string

The kind of the bot.

name: string

The name of the bot.

operator: string

The organization that owns and operates the bot.

slug: string

A kebab-case identifier derived from the bot name.

userAgentPatterns: array of string

BotGetResponse object { bot } 

bot: object { category, description, kind, 7 more } 

category: string

The category of the bot.

description: string

A summary for the bot (e.g., purpose).

Deprecatedkind: string

The kind of the bot.

name: string

The name of the bot.

operator: string

The organization that owns and operates the bot.

operatorUrl: string

The link to the bot documentation.

slug: string

A kebab-case identifier derived from the bot name.

userAgentPatterns: array of string

userAgents: array of string

signatureAgentUrl: optional string

The URL of the agent’s [Web Bot Auth](https://blog.cloudflare.com/web-bot-auth/) resource. Null for bots not verified via request signature.

BotSummaryResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: map[string]

BotTimeseriesResponse object { meta } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

BotTimeseriesGroupsResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

#### RadarBotsWeb Crawlers

##### [Get crawler HTTP request distribution by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/bots/subresources/web_crawlers/methods/summary)

GET/radar/bots/crawlers/summary/{dimension}

##### [Get time series of crawler HTTP request distribution by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/bots/subresources/web_crawlers/methods/timeseries_groups)

GET/radar/bots/crawlers/timeseries_groups/{dimension}

##### ModelsExpand Collapse 

WebCrawlerSummaryResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: map[string]

WebCrawlerTimeseriesGroupsResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

#### RadarDatasets

##### [List datasets](https://developers.cloudflare.com/api/resources/radar/subresources/datasets/methods/list)

GET/radar/datasets

##### [Get dataset CSV stream](https://developers.cloudflare.com/api/resources/radar/subresources/datasets/methods/get)

GET/radar/datasets/{alias}

##### [Get dataset download URL](https://developers.cloudflare.com/api/resources/radar/subresources/datasets/methods/download)

POST/radar/datasets/download

##### ModelsExpand Collapse 

DatasetListResponse object { datasets } 

datasets: array of object { id, description, meta, 3 more } 

id: number

description: string

meta: unknown

tags: array of string

title: string

type: string

DatasetGetResponse = string

DatasetDownloadResponse object { dataset } 

dataset: object { url } 

url: string

#### RadarDNS

##### [Get DNS summary by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/dns/methods/summary_v2)

GET/radar/dns/summary/{dimension}

##### [Get DNS queries time series](https://developers.cloudflare.com/api/resources/radar/subresources/dns/methods/timeseries)

GET/radar/dns/timeseries

##### [Get DNS time series grouped by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/dns/methods/timeseries_groups_v2)

GET/radar/dns/timeseries_groups/{dimension}

##### ModelsExpand Collapse 

DNSSummaryV2Response object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: map[string]

DNSTimeseriesResponse object { meta } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

DNSTimeseriesGroupsV2Response object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

#### RadarDNSTop

##### [Get top ASes by DNS queries](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/top/methods/ases)

GET/radar/dns/top/ases

##### [Get top locations by DNS queries](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/top/methods/locations)

GET/radar/dns/top/locations

##### ModelsExpand Collapse 

TopAsesResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { clientASN, clientASName, value } 

clientASN: number

clientASName: string

value: string

A numeric string.

TopLocationsResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { clientCountryAlpha2, clientCountryName, value } 

clientCountryAlpha2: string

clientCountryName: string

value: string

A numeric string.

#### RadarDNSSummary

##### [Get DNS queries by cache status summary](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/summary/methods/cache_hit)

Deprecated

GET/radar/dns/summary/cache_hit

##### [Get DNS queries by DNSSEC support summary](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/summary/methods/dnssec)

Deprecated

GET/radar/dns/summary/dnssec

##### [Get DNS queries by DNSSEC awareness summary](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/summary/methods/dnssec_aware)

Deprecated

GET/radar/dns/summary/dnssec_aware

##### [Get DNS queries by DNSSEC end-to-end summary](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/summary/methods/dnssec_e2e)

Deprecated

GET/radar/dns/summary/dnssec_e2e

##### [Get DNS queries by IP version summary](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/summary/methods/ip_version)

Deprecated

GET/radar/dns/summary/ip_version

##### [Get DNS queries by matching answer summary](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/summary/methods/matching_answer)

Deprecated

GET/radar/dns/summary/matching_answer

##### [Get DNS queries by protocol summary](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/summary/methods/protocol)

Deprecated

GET/radar/dns/summary/protocol

##### [Get DNS queries by type summary](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/summary/methods/query_type)

Deprecated

GET/radar/dns/summary/query_type

##### [Get DNS queries by response code summary](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/summary/methods/response_code)

Deprecated

GET/radar/dns/summary/response_code

##### [Get DNS queries by response TTL summary](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/summary/methods/response_ttl)

Deprecated

GET/radar/dns/summary/response_ttl

##### ModelsExpand Collapse 

SummaryCacheHitResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { NEGATIVE, POSITIVE } 

NEGATIVE: string

A numeric string.

POSITIVE: string

A numeric string.

SummaryDNSSECResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { INSECURE, INVALID, OTHER, SECURE } 

INSECURE: string

A numeric string.

INVALID: string

A numeric string.

OTHER: string

A numeric string.

SECURE: string

A numeric string.

SummaryDNSSECAwareResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { NOT_SUPPORTED, SUPPORTED } 

NOT_SUPPORTED: string

A numeric string.

SUPPORTED: string

A numeric string.

SummaryDNSSECE2EResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { NEGATIVE, POSITIVE } 

NEGATIVE: string

A numeric string.

POSITIVE: string

A numeric string.

SummaryIPVersionResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { IPv4, IPv6 } 

IPv4: string

A numeric string.

IPv6: string

A numeric string.

SummaryMatchingAnswerResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { NEGATIVE, POSITIVE } 

NEGATIVE: string

A numeric string.

POSITIVE: string

A numeric string.

SummaryProtocolResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { HTTPS, TCP, TLS, UDP } 

HTTPS: string

A numeric string.

TCP: string

A numeric string.

TLS: string

A numeric string.

UDP: string

A numeric string.

SummaryQueryTypeResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: map[string]

SummaryResponseCodeResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: map[string]

SummaryResponseTTLResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { gt_15m_lte_1h, gt_1d_lte_1w, gt_1h_lte_1d, 4 more } 

gt_15m_lte_1h: string

A numeric string.

gt_1d_lte_1w: string

A numeric string.

gt_1h_lte_1d: string

A numeric string.

gt_1m_lte_5m: string

A numeric string.

gt_1w: string

A numeric string.

gt_5m_lte_15m: string

A numeric string.

lte_1m: string

A numeric string.

#### RadarDNSTimeseries Groups

##### [Get DNS queries by cache status time series](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/timeseries_groups/methods/cache_hit)

Deprecated

GET/radar/dns/timeseries_groups/cache_hit

##### [Get DNS queries by DNSSEC support time series](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/timeseries_groups/methods/dnssec)

Deprecated

GET/radar/dns/timeseries_groups/dnssec

##### [Get DNS queries by DNSSEC awareness time series](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/timeseries_groups/methods/dnssec_aware)

Deprecated

GET/radar/dns/timeseries_groups/dnssec_aware

##### [Get DNS queries by DNSSEC end-to-end time series](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/timeseries_groups/methods/dnssec_e2e)

Deprecated

GET/radar/dns/timeseries_groups/dnssec_e2e

##### [Get DNS queries by IP version time series](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/timeseries_groups/methods/ip_version)

Deprecated

GET/radar/dns/timeseries_groups/ip_version

##### [Get DNS queries by matching answer time series](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/timeseries_groups/methods/matching_answer)

Deprecated

GET/radar/dns/timeseries_groups/matching_answer

##### [Get DNS queries by protocol time series](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/timeseries_groups/methods/protocol)

Deprecated

GET/radar/dns/timeseries_groups/protocol

##### [Get DNS queries by type time series](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/timeseries_groups/methods/query_type)

Deprecated

GET/radar/dns/timeseries_groups/query_type

##### [Get DNS queries by response code time series](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/timeseries_groups/methods/response_code)

Deprecated

GET/radar/dns/timeseries_groups/response_code

##### [Get DNS queries by response TTL time series](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/timeseries_groups/methods/response_ttl)

Deprecated

GET/radar/dns/timeseries_groups/response_ttl

##### ModelsExpand Collapse 

TimeseriesGroupCacheHitResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { NEGATIVE, POSITIVE } 

NEGATIVE: array of string

POSITIVE: array of string

TimeseriesGroupDNSSECResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { INSECURE, INVALID, OTHER, SECURE } 

INSECURE: array of string

INVALID: array of string

OTHER: array of string

SECURE: array of string

TimeseriesGroupDNSSECAwareResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { NOT_SUPPORTED, SUPPORTED } 

NOT_SUPPORTED: array of string

SUPPORTED: array of string

TimeseriesGroupDNSSECE2EResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { NEGATIVE, POSITIVE } 

NEGATIVE: array of string

POSITIVE: array of string

TimeseriesGroupIPVersionResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { IPv4, IPv6 } 

IPv4: array of string

IPv6: array of string

TimeseriesGroupMatchingAnswerResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { NEGATIVE, POSITIVE } 

NEGATIVE: array of string

POSITIVE: array of string

TimeseriesGroupProtocolResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { HTTPS, TCP, TLS, UDP } 

HTTPS: array of string

TCP: array of string

TLS: array of string

UDP: array of string

TimeseriesGroupQueryTypeResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

TimeseriesGroupResponseCodeResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

TimeseriesGroupResponseTTLResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { gt_15m_lte_1h, gt_1d_lte_1w, gt_1h_lte_1d, 4 more } 

gt_15m_lte_1h: array of string

gt_1d_lte_1w: array of string

gt_1h_lte_1d: array of string

gt_1m_lte_5m: array of string

gt_1w: array of string

gt_5m_lte_15m: array of string

lte_1m: array of string

#### RadarNetFlows

##### [Get network traffic time series](https://developers.cloudflare.com/api/resources/radar/subresources/netflows/methods/timeseries)

GET/radar/netflows/timeseries

##### [Get network traffic summary](https://developers.cloudflare.com/api/resources/radar/subresources/netflows/methods/summary)

Deprecated

GET/radar/netflows/summary

##### [Get network traffic distribution by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/netflows/methods/summary_v2)

GET/radar/netflows/summary/{dimension}

##### [Get time series distribution of network traffic by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/netflows/methods/timeseries_groups)

GET/radar/netflows/timeseries_groups/{dimension}

##### ModelsExpand Collapse 

NetFlowsTimeseriesResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps, values } 

timestamps: array of string

values: array of string

NetFlowsSummaryResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { HTTP, OTHER } 

HTTP: string

A numeric string.

OTHER: string

A numeric string.

NetFlowsSummaryV2Response object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: map[string]

NetFlowsTimeseriesGroupsResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

#### RadarNetFlowsTop

##### [Get top ASes by network traffic](https://developers.cloudflare.com/api/resources/radar/subresources/netflows/subresources/top/methods/ases)

GET/radar/netflows/top/ases

##### [Get top locations by network traffic](https://developers.cloudflare.com/api/resources/radar/subresources/netflows/subresources/top/methods/locations)

GET/radar/netflows/top/locations

##### ModelsExpand Collapse 

TopAsesResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { clientASN, clientASName, value } 

clientASN: number

clientASName: string

value: string

A numeric string.

TopLocationsResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { clientCountryAlpha2, clientCountryName, value } 

clientCountryAlpha2: string

clientCountryName: string

value: string

A numeric string.

#### RadarPost Quantum

#### RadarPost QuantumOrigin

##### [Get Origin Post-Quantum Data Summary](https://developers.cloudflare.com/api/resources/radar/subresources/post_quantum/subresources/origin/methods/summary)

GET/radar/post_quantum/origin/summary/{dimension}

##### [Get Origin Post-Quantum Data Over Time](https://developers.cloudflare.com/api/resources/radar/subresources/post_quantum/subresources/origin/methods/timeseries_groups)

GET/radar/post_quantum/origin/timeseries_groups/{dimension}

##### ModelsExpand Collapse 

OriginSummaryResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: map[string]

OriginTimeseriesGroupsResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

#### RadarPost QuantumTLS

##### [Check Post-Quantum TLS support](https://developers.cloudflare.com/api/resources/radar/subresources/post_quantum/subresources/tls/methods/support)

GET/radar/post_quantum/tls/support

##### ModelsExpand Collapse 

TLSSupportResponse object { bugs, host, kex, 2 more } 

bugs: object { hrrFailure, splitClientHello, unknownKeyshare } 

hrrFailure: boolean

Server sends a HelloRetryRequest but fails to complete the handshake after the client sends the second ClientHello. Often caused by non-compliant TLS 1.3 implementations on shared hosting providers.

splitClientHello: boolean

Server rejects fragmented ClientHello caused by large PQ keyshare, but accepts classical (non-PQ) handshakes. Typically caused by middleboxes or firewalls that cannot reassemble split TLS ClientHello messages.

unknownKeyshare: boolean

Server cannot handle an unknown key exchange algorithm in the ClientHello keyshare extension. Compliant servers should respond with HelloRetryRequest for a supported algorithm.

host: string

The host that was tested

kex: number

TLS CurveID of the negotiated key exchange

kexName: string

Human-readable name of the key exchange algorithm

pq: boolean

Whether the negotiated key exchange uses Post-Quantum cryptography (specifically X25519MLKEM768)

#### RadarSearch

##### [Search for locations, ASes, reports, and more](https://developers.cloudflare.com/api/resources/radar/subresources/search/methods/global)

GET/radar/search/global

##### ModelsExpand Collapse 

SearchGlobalResponse object { search } 

search: array of object { code, name, type } 

code: string

name: string

type: string

#### RadarVerified Bots

#### RadarVerified BotsTop

##### [Get top verified bots by HTTP requests](https://developers.cloudflare.com/api/resources/radar/subresources/verified_bots/subresources/top/methods/bots)

Deprecated

GET/radar/verified_bots/top/bots

##### [Get top verified bot categories by HTTP requests](https://developers.cloudflare.com/api/resources/radar/subresources/verified_bots/subresources/top/methods/categories)

Deprecated

GET/radar/verified_bots/top/categories

##### ModelsExpand Collapse 

TopBotsResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { botCategory, botName, botOwner, value } 

botCategory: string

botName: string

botOwner: string

value: string

A numeric string.

TopCategoriesResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { botCategory, value } 

botCategory: string

value: string

A numeric string.

#### RadarAS112

##### [Get AS112 DNS queries time series](https://developers.cloudflare.com/api/resources/radar/subresources/as112/methods/timeseries)

GET/radar/as112/timeseries

##### [Get AS112 summary by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/as112/methods/summary_v2)

GET/radar/as112/summary/{dimension}

##### [Get AS112 time series grouped by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/as112/methods/timeseries_groups_v2)

GET/radar/as112/timeseries_groups/{dimension}

##### ModelsExpand Collapse 

AS112TimeseriesResponse object { meta } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

AS112SummaryV2Response object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: map[string]

AS112TimeseriesGroupsV2Response object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

#### RadarAS112Summary

##### [Get AS112 DNS queries by DNSSEC summary](https://developers.cloudflare.com/api/resources/radar/subresources/as112/subresources/summary/methods/dnssec)

Deprecated

GET/radar/as112/summary/dnssec

##### [Get AS112 DNS queries by EDNS summary](https://developers.cloudflare.com/api/resources/radar/subresources/as112/subresources/summary/methods/edns)

Deprecated

GET/radar/as112/summary/edns

##### [Get AS112 DNS queries by IP version summary](https://developers.cloudflare.com/api/resources/radar/subresources/as112/subresources/summary/methods/ip_version)

Deprecated

GET/radar/as112/summary/ip_version

##### [Get AS112 DNS queries by DNS protocol summary](https://developers.cloudflare.com/api/resources/radar/subresources/as112/subresources/summary/methods/protocol)

Deprecated

GET/radar/as112/summary/protocol

##### [Get AS112 DNS queries by type summary](https://developers.cloudflare.com/api/resources/radar/subresources/as112/subresources/summary/methods/query_type)

Deprecated

GET/radar/as112/summary/query_type

##### [Get AS112 DNS queries by response code summary](https://developers.cloudflare.com/api/resources/radar/subresources/as112/subresources/summary/methods/response_codes)

Deprecated

GET/radar/as112/summary/response_codes

##### ModelsExpand Collapse 

SummaryDNSSECResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { NOT_SUPPORTED, SUPPORTED } 

NOT_SUPPORTED: string

A numeric string.

SUPPORTED: string

A numeric string.

SummaryEdnsResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { NOT_SUPPORTED, SUPPORTED } 

NOT_SUPPORTED: string

A numeric string.

SUPPORTED: string

A numeric string.

SummaryIPVersionResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { IPv4, IPv6 } 

IPv4: string

A numeric string.

IPv6: string

A numeric string.

SummaryProtocolResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { HTTPS, TCP, TLS, UDP } 

HTTPS: string

A numeric string.

TCP: string

A numeric string.

TLS: string

A numeric string.

UDP: string

A numeric string.

SummaryQueryTypeResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: map[string]

SummaryResponseCodesResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: map[string]

#### RadarAS112Timeseries Groups

##### [Get AS112 DNS queries by DNS protocol time series](https://developers.cloudflare.com/api/resources/radar/subresources/as112/subresources/timeseries_groups/methods/protocol)

Deprecated

GET/radar/as112/timeseries_groups/protocol

##### [Get AS112 DNS queries by type time series](https://developers.cloudflare.com/api/resources/radar/subresources/as112/subresources/timeseries_groups/methods/query_type)

Deprecated

GET/radar/as112/timeseries_groups/query_type

##### [Get AS112 DNS queries by response code time series](https://developers.cloudflare.com/api/resources/radar/subresources/as112/subresources/timeseries_groups/methods/response_codes)

Deprecated

GET/radar/as112/timeseries_groups/response_codes

##### [Get AS112 DNS queries by DNSSEC support time series](https://developers.cloudflare.com/api/resources/radar/subresources/as112/subresources/timeseries_groups/methods/dnssec)

Deprecated

GET/radar/as112/timeseries_groups/dnssec

##### [Get AS112 DNS queries by EDNS support summary](https://developers.cloudflare.com/api/resources/radar/subresources/as112/subresources/timeseries_groups/methods/edns)

Deprecated

GET/radar/as112/timeseries_groups/edns

##### [Get AS112 DNS queries by IP version time series](https://developers.cloudflare.com/api/resources/radar/subresources/as112/subresources/timeseries_groups/methods/ip_version)

Deprecated

GET/radar/as112/timeseries_groups/ip_version

##### ModelsExpand Collapse 

TimeseriesGroupProtocolResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { HTTPS, TCP, TLS, UDP } 

HTTPS: array of string

TCP: array of string

TLS: array of string

UDP: array of string

TimeseriesGroupQueryTypeResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

TimeseriesGroupResponseCodesResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

TimeseriesGroupDNSSECResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { NOT_SUPPORTED, SUPPORTED } 

NOT_SUPPORTED: array of string

SUPPORTED: array of string

TimeseriesGroupEdnsResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { NOT_SUPPORTED, SUPPORTED } 

NOT_SUPPORTED: array of string

SUPPORTED: array of string

TimeseriesGroupIPVersionResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { IPv4, IPv6 } 

IPv4: array of string

IPv6: array of string

#### RadarAS112Top

##### [Get top locations by AS112 DNS queries](https://developers.cloudflare.com/api/resources/radar/subresources/as112/subresources/top/methods/locations)

GET/radar/as112/top/locations

##### [Get top locations by AS112 DNS queries with DNSSEC support](https://developers.cloudflare.com/api/resources/radar/subresources/as112/subresources/top/methods/dnssec)

GET/radar/as112/top/locations/dnssec/{dnssec}

##### [Get top locations by AS112 DNS queries with EDNS support](https://developers.cloudflare.com/api/resources/radar/subresources/as112/subresources/top/methods/edns)

GET/radar/as112/top/locations/edns/{edns}

##### [Get top locations by AS112 DNS queries for an IP version](https://developers.cloudflare.com/api/resources/radar/subresources/as112/subresources/top/methods/ip_version)

GET/radar/as112/top/locations/ip_version/{ip_version}

##### ModelsExpand Collapse 

TopLocationsResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { clientCountryAlpha2, clientCountryName, value } 

clientCountryAlpha2: string

clientCountryName: string

value: string

A numeric string.

TopDNSSECResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { clientCountryAlpha2, clientCountryName, value } 

clientCountryAlpha2: string

clientCountryName: string

value: string

A numeric string.

TopEdnsResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { clientCountryAlpha2, clientCountryName, value } 

clientCountryAlpha2: string

clientCountryName: string

value: string

A numeric string.

TopIPVersionResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { clientCountryAlpha2, clientCountryName, value } 

clientCountryAlpha2: string

clientCountryName: string

value: string

A numeric string.

#### RadarEmail

##### ModelsExpand Collapse 

RadarEmailSeries object { FAIL, NONE, PASS } 

FAIL: array of string

NONE: array of string

PASS: array of string

RadarEmailSummary object { FAIL, NONE, PASS } 

FAIL: string

A numeric string.

NONE: string

A numeric string.

PASS: string

A numeric string.

#### RadarEmailRouting

##### [Get email routing summary by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/routing/methods/summary_v2)

GET/radar/email/routing/summary/{dimension}

##### [Get email routing time series grouped by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/routing/methods/timeseries_groups_v2)

GET/radar/email/routing/timeseries_groups/{dimension}

##### ModelsExpand Collapse 

RoutingSummaryV2Response object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: map[string]

RoutingTimeseriesGroupsV2Response object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

#### RadarEmailRoutingSummary

##### [Get email ARC validation summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/routing/subresources/summary/methods/arc)

Deprecated

GET/radar/email/routing/summary/arc

##### [Get email DKIM validation summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/routing/subresources/summary/methods/dkim)

Deprecated

GET/radar/email/routing/summary/dkim

##### [Get email DMARC validation summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/routing/subresources/summary/methods/dmarc)

Deprecated

GET/radar/email/routing/summary/dmarc

##### [Get email encryption status summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/routing/subresources/summary/methods/encrypted)

Deprecated

GET/radar/email/routing/summary/encrypted

##### [Get email IP version summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/routing/subresources/summary/methods/ip_version)

Deprecated

GET/radar/email/routing/summary/ip_version

##### [Get email SPF validation summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/routing/subresources/summary/methods/spf)

Deprecated

GET/radar/email/routing/summary/spf

##### ModelsExpand Collapse 

SummaryARCResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: [RadarEmailSummary](https://developers.cloudflare.com/api/resources/radar#\(resource\)%20radar.email%20%3E%20\(model\)%20radar_email_summary%20%3E%20\(schema\)) { FAIL, NONE, PASS } 

SummaryDKIMResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: [RadarEmailSummary](https://developers.cloudflare.com/api/resources/radar#\(resource\)%20radar.email%20%3E%20\(model\)%20radar_email_summary%20%3E%20\(schema\)) { FAIL, NONE, PASS } 

SummaryDMARCResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: [RadarEmailSummary](https://developers.cloudflare.com/api/resources/radar#\(resource\)%20radar.email%20%3E%20\(model\)%20radar_email_summary%20%3E%20\(schema\)) { FAIL, NONE, PASS } 

SummaryEncryptedResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { ENCRYPTED, NOT_ENCRYPTED } 

ENCRYPTED: string

A numeric string.

NOT_ENCRYPTED: string

A numeric string.

SummaryIPVersionResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { IPv4, IPv6 } 

IPv4: string

A numeric string.

IPv6: string

A numeric string.

SummarySPFResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: [RadarEmailSummary](https://developers.cloudflare.com/api/resources/radar#\(resource\)%20radar.email%20%3E%20\(model\)%20radar_email_summary%20%3E%20\(schema\)) { FAIL, NONE, PASS } 

#### RadarEmailRoutingTimeseries Groups

##### [Get email ARC validation time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/routing/subresources/timeseries_groups/methods/arc)

Deprecated

GET/radar/email/routing/timeseries_groups/arc

##### [Get email DKIM validation time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/routing/subresources/timeseries_groups/methods/dkim)

Deprecated

GET/radar/email/routing/timeseries_groups/dkim

##### [Get email DMARC validation time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/routing/subresources/timeseries_groups/methods/dmarc)

Deprecated

GET/radar/email/routing/timeseries_groups/dmarc

##### [Get email encryption status time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/routing/subresources/timeseries_groups/methods/encrypted)

Deprecated

GET/radar/email/routing/timeseries_groups/encrypted

##### [Get email IP version time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/routing/subresources/timeseries_groups/methods/ip_version)

Deprecated

GET/radar/email/routing/timeseries_groups/ip_version

##### [Get email SPF validation time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/routing/subresources/timeseries_groups/methods/spf)

Deprecated

GET/radar/email/routing/timeseries_groups/spf

##### ModelsExpand Collapse 

TimeseriesGroupARCResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: [RadarEmailSeries](https://developers.cloudflare.com/api/resources/radar#\(resource\)%20radar.email%20%3E%20\(model\)%20radar_email_series%20%3E%20\(schema\)) { FAIL, NONE, PASS } 

TimeseriesGroupDKIMResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: [RadarEmailSeries](https://developers.cloudflare.com/api/resources/radar#\(resource\)%20radar.email%20%3E%20\(model\)%20radar_email_series%20%3E%20\(schema\)) { FAIL, NONE, PASS } 

TimeseriesGroupDMARCResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: [RadarEmailSeries](https://developers.cloudflare.com/api/resources/radar#\(resource\)%20radar.email%20%3E%20\(model\)%20radar_email_series%20%3E%20\(schema\)) { FAIL, NONE, PASS } 

TimeseriesGroupEncryptedResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { ENCRYPTED, NOT_ENCRYPTED } 

ENCRYPTED: array of string

NOT_ENCRYPTED: array of string

TimeseriesGroupIPVersionResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { IPv4, IPv6 } 

IPv4: array of string

IPv6: array of string

TimeseriesGroupSPFResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: [RadarEmailSeries](https://developers.cloudflare.com/api/resources/radar#\(resource\)%20radar.email%20%3E%20\(model\)%20radar_email_series%20%3E%20\(schema\)) { FAIL, NONE, PASS } 

#### RadarEmailSecurity

##### [Get email security summary by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/methods/summary_v2)

GET/radar/email/security/summary/{dimension}

##### [Get email security time series grouped by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/methods/timeseries_groups_v2)

GET/radar/email/security/timeseries_groups/{dimension}

##### ModelsExpand Collapse 

SecuritySummaryV2Response object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: map[string]

SecurityTimeseriesGroupsV2Response object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

#### RadarEmailSecurityTop

#### RadarEmailSecurityTopTLDs

##### [Get top TLDs by email message volume](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/top/subresources/tlds/methods/get)

GET/radar/email/security/top/tlds

##### ModelsExpand Collapse 

TLDGetResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { name, value } 

name: string

value: string

A numeric string.

#### RadarEmailSecurityTopTLDsMalicious

##### [Get top TLDs by email malicious classification](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/top/subresources/tlds/subresources/malicious/methods/get)

GET/radar/email/security/top/tlds/malicious/{malicious}

##### ModelsExpand Collapse 

MaliciousGetResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { name, value } 

name: string

value: string

A numeric string.

#### RadarEmailSecurityTopTLDsSpam

##### [Get top TLDs by email spam classification](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/top/subresources/tlds/subresources/spam/methods/get)

GET/radar/email/security/top/tlds/spam/{spam}

##### ModelsExpand Collapse 

SpamGetResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { name, value } 

name: string

value: string

A numeric string.

#### RadarEmailSecurityTopTLDsSpoof

##### [Get top TLDs by email spoof classification](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/top/subresources/tlds/subresources/spoof/methods/get)

GET/radar/email/security/top/tlds/spoof/{spoof}

##### ModelsExpand Collapse 

SpoofGetResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { name, value } 

name: string

value: string

A numeric string.

#### RadarEmailSecuritySummary

##### [Get email ARC validation summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/summary/methods/arc)

Deprecated

GET/radar/email/security/summary/arc

##### [Get email DKIM validation summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/summary/methods/dkim)

Deprecated

GET/radar/email/security/summary/dkim

##### [Get email DMARC validation summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/summary/methods/dmarc)

Deprecated

GET/radar/email/security/summary/dmarc

##### [Get email malicious classification summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/summary/methods/malicious)

Deprecated

GET/radar/email/security/summary/malicious

##### [Get email spam classification summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/summary/methods/spam)

Deprecated

GET/radar/email/security/summary/spam

##### [Get email SPF validation summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/summary/methods/spf)

Deprecated

GET/radar/email/security/summary/spf

##### [Get email threat category summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/summary/methods/threat_category)

Deprecated

GET/radar/email/security/summary/threat_category

##### [Get email spoof classification summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/summary/methods/spoof)

Deprecated

GET/radar/email/security/summary/spoof

##### [Get email TLS version summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/summary/methods/tls_version)

Deprecated

GET/radar/email/security/summary/tls_version

##### ModelsExpand Collapse 

SummaryARCResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: [RadarEmailSummary](https://developers.cloudflare.com/api/resources/radar#\(resource\)%20radar.email%20%3E%20\(model\)%20radar_email_summary%20%3E%20\(schema\)) { FAIL, NONE, PASS } 

SummaryDKIMResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: [RadarEmailSummary](https://developers.cloudflare.com/api/resources/radar#\(resource\)%20radar.email%20%3E%20\(model\)%20radar_email_summary%20%3E%20\(schema\)) { FAIL, NONE, PASS } 

SummaryDMARCResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: [RadarEmailSummary](https://developers.cloudflare.com/api/resources/radar#\(resource\)%20radar.email%20%3E%20\(model\)%20radar_email_summary%20%3E%20\(schema\)) { FAIL, NONE, PASS } 

SummaryMaliciousResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { MALICIOUS, NOT_MALICIOUS } 

MALICIOUS: string

A numeric string.

NOT_MALICIOUS: string

A numeric string.

SummarySpamResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { NOT_SPAM, SPAM } 

NOT_SPAM: string

A numeric string.

SPAM: string

A numeric string.

SummarySPFResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: [RadarEmailSummary](https://developers.cloudflare.com/api/resources/radar#\(resource\)%20radar.email%20%3E%20\(model\)%20radar_email_summary%20%3E%20\(schema\)) { FAIL, NONE, PASS } 

SummaryThreatCategoryResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { BrandImpersonation, CredentialHarvester, IdentityDeception, Link } 

BrandImpersonation: string

A numeric string.

CredentialHarvester: string

A numeric string.

IdentityDeception: string

A numeric string.

Link: string

A numeric string.

SummarySpoofResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { NOT_SPOOF, SPOOF } 

NOT_SPOOF: string

A numeric string.

SPOOF: string

A numeric string.

SummaryTLSVersionResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { "TLS 1.0", "TLS 1.1", "TLS 1.2", "TLS 1.3" } 

"TLS 1.0": string

A numeric string.

"TLS 1.1": string

A numeric string.

"TLS 1.2": string

A numeric string.

"TLS 1.3": string

A numeric string.

#### RadarEmailSecurityTimeseries Groups

##### [Get email ARC validation time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/timeseries_groups/methods/arc)

Deprecated

GET/radar/email/security/timeseries_groups/arc

##### [Get email DKIM validation time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/timeseries_groups/methods/dkim)

Deprecated

GET/radar/email/security/timeseries_groups/dkim

##### [Get email DMARC validation time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/timeseries_groups/methods/dmarc)

Deprecated

GET/radar/email/security/timeseries_groups/dmarc

##### [Get email malicious classification time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/timeseries_groups/methods/malicious)

Deprecated

GET/radar/email/security/timeseries_groups/malicious

##### [Get email spam classification time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/timeseries_groups/methods/spam)

Deprecated

GET/radar/email/security/timeseries_groups/spam

##### [Get email SPF validation time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/timeseries_groups/methods/spf)

Deprecated

GET/radar/email/security/timeseries_groups/spf

##### [Get email threat category time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/timeseries_groups/methods/threat_category)

Deprecated

GET/radar/email/security/timeseries_groups/threat_category

##### [Get email spoof classification time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/timeseries_groups/methods/spoof)

Deprecated

GET/radar/email/security/timeseries_groups/spoof

##### [Get email TLS version time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/timeseries_groups/methods/tls_version)

Deprecated

GET/radar/email/security/timeseries_groups/tls_version

##### ModelsExpand Collapse 

TimeseriesGroupARCResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: [RadarEmailSeries](https://developers.cloudflare.com/api/resources/radar#\(resource\)%20radar.email%20%3E%20\(model\)%20radar_email_series%20%3E%20\(schema\)) { FAIL, NONE, PASS } 

TimeseriesGroupDKIMResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: [RadarEmailSeries](https://developers.cloudflare.com/api/resources/radar#\(resource\)%20radar.email%20%3E%20\(model\)%20radar_email_series%20%3E%20\(schema\)) { FAIL, NONE, PASS } 

TimeseriesGroupDMARCResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: [RadarEmailSeries](https://developers.cloudflare.com/api/resources/radar#\(resource\)%20radar.email%20%3E%20\(model\)%20radar_email_series%20%3E%20\(schema\)) { FAIL, NONE, PASS } 

TimeseriesGroupMaliciousResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { MALICIOUS, NOT_MALICIOUS } 

MALICIOUS: array of string

NOT_MALICIOUS: array of string

TimeseriesGroupSpamResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { NOT_SPAM, SPAM } 

NOT_SPAM: array of string

SPAM: array of string

TimeseriesGroupSPFResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: [RadarEmailSeries](https://developers.cloudflare.com/api/resources/radar#\(resource\)%20radar.email%20%3E%20\(model\)%20radar_email_series%20%3E%20\(schema\)) { FAIL, NONE, PASS } 

TimeseriesGroupThreatCategoryResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { BrandImpersonation, CredentialHarvester, IdentityDeception, Link } 

BrandImpersonation: array of string

CredentialHarvester: array of string

IdentityDeception: array of string

Link: array of string

TimeseriesGroupSpoofResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { NOT_SPOOF, SPOOF } 

NOT_SPOOF: array of string

SPOOF: array of string

TimeseriesGroupTLSVersionResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { "TLS 1.0", "TLS 1.1", "TLS 1.2", "TLS 1.3" } 

"TLS 1.0": array of string

"TLS 1.1": array of string

"TLS 1.2": array of string

"TLS 1.3": array of string

#### RadarAttacks

#### RadarAttacksLayer3

##### [Get layer 3 attacks summary by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/methods/summary_v2)

GET/radar/attacks/layer3/summary/{dimension}

##### [Get layer 3 attacks by bytes time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/methods/timeseries)

GET/radar/attacks/layer3/timeseries

##### [Get layer 3 attacks time series grouped by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/methods/timeseries_groups_v2)

GET/radar/attacks/layer3/timeseries_groups/{dimension}

##### ModelsExpand Collapse 

Layer3SummaryV2Response object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: map[string]

Layer3TimeseriesResponse object { meta } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

Layer3TimeseriesGroupsV2Response object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

#### RadarAttacksLayer3Summary

##### [Get layer 3 attacks by bitrate summary](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/summary/methods/bitrate)

Deprecated

GET/radar/attacks/layer3/summary/bitrate

##### [Get layer 3 attacks by duration summary](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/summary/methods/duration)

Deprecated

GET/radar/attacks/layer3/summary/duration

##### [Get layer 3 attacks by IP version summary](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/summary/methods/ip_version)

Deprecated

GET/radar/attacks/layer3/summary/ip_version

##### [Get layer 3 attacks by protocol summary](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/summary/methods/protocol)

Deprecated

GET/radar/attacks/layer3/summary/protocol

##### [Get layer 3 attacks by vector summary](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/summary/methods/vector)

Deprecated

GET/radar/attacks/layer3/summary/vector

##### [Get layer 3 attacks by targeted industry summary](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/summary/methods/industry)

Deprecated

GET/radar/attacks/layer3/summary/industry

##### [Get layer 3 attacks by targeted vertical summary](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/summary/methods/vertical)

Deprecated

GET/radar/attacks/layer3/summary/vertical

##### ModelsExpand Collapse 

SummaryBitrateResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { _1_GBPS_TO_10_GBPS, _10_GBPS_TO_100_GBPS, _500_MBPS_TO_1_GBPS, 2 more } 

_1_GBPS_TO_10_GBPS: string

A numeric string.

_10_GBPS_TO_100_GBPS: string

A numeric string.

_500_MBPS_TO_1_GBPS: string

A numeric string.

OVER_100_GBPS: string

A numeric string.

UNDER_500_MBPS: string

A numeric string.

SummaryDurationResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { _1_HOUR_TO_3_HOURS, _10_MINS_TO_20_MINS, _20_MINS_TO_40_MINS, 3 more } 

_1_HOUR_TO_3_HOURS: string

A numeric string.

_10_MINS_TO_20_MINS: string

A numeric string.

_20_MINS_TO_40_MINS: string

A numeric string.

_40_MINS_TO_1_HOUR: string

A numeric string.

OVER_3_HOURS: string

A numeric string.

UNDER_10_MINS: string

A numeric string.

SummaryIPVersionResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { IPv4, IPv6 } 

IPv4: string

A numeric string.

IPv6: string

A numeric string.

SummaryProtocolResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { GRE, ICMP, TCP, UDP } 

GRE: string

A numeric string.

ICMP: string

A numeric string.

TCP: string

A numeric string.

UDP: string

A numeric string.

SummaryVectorResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: map[string]

SummaryIndustryResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: map[string]

SummaryVerticalResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: map[string]

#### RadarAttacksLayer3Timeseries Groups

##### [Get layer 3 attacks by target industries time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/timeseries_groups/methods/industry)

Deprecated

GET/radar/attacks/layer3/timeseries_groups/industry

##### [Get layer 3 attacks by IP version time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/timeseries_groups/methods/ip_version)

Deprecated

GET/radar/attacks/layer3/timeseries_groups/ip_version

##### [Get layer 3 attacks by protocol time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/timeseries_groups/methods/protocol)

Deprecated

GET/radar/attacks/layer3/timeseries_groups/protocol

##### [Get layer 3 attacks by vector time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/timeseries_groups/methods/vector)

Deprecated

GET/radar/attacks/layer3/timeseries_groups/vector

##### [Get layer 3 attacks by vertical time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/timeseries_groups/methods/vertical)

Deprecated

GET/radar/attacks/layer3/timeseries_groups/vertical

##### [Get layer 3 attacks by bitrate time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/timeseries_groups/methods/bitrate)

Deprecated

GET/radar/attacks/layer3/timeseries_groups/bitrate

##### [Get layer 3 attacks by duration time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/timeseries_groups/methods/duration)

Deprecated

GET/radar/attacks/layer3/timeseries_groups/duration

##### ModelsExpand Collapse 

TimeseriesGroupIndustryResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

TimeseriesGroupIPVersionResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { IPv4, IPv6, timestamps } 

IPv4: array of string

IPv6: array of string

timestamps: array of string

TimeseriesGroupProtocolResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { GRE, ICMP, TCP, 2 more } 

GRE: array of string

ICMP: array of string

TCP: array of string

timestamps: array of string

UDP: array of string

TimeseriesGroupVectorResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

TimeseriesGroupVerticalResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

TimeseriesGroupBitrateResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { _1_GBPS_TO_10_GBPS, _10_GBPS_TO_100_GBPS, _500_MBPS_TO_1_GBPS, 3 more } 

_1_GBPS_TO_10_GBPS: array of string

_10_GBPS_TO_100_GBPS: array of string

_500_MBPS_TO_1_GBPS: array of string

OVER_100_GBPS: array of string

timestamps: array of string

UNDER_500_MBPS: array of string

TimeseriesGroupDurationResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { _1_HOUR_TO_3_HOURS, _10_MINS_TO_20_MINS, _20_MINS_TO_40_MINS, 4 more } 

_1_HOUR_TO_3_HOURS: array of string

_10_MINS_TO_20_MINS: array of string

_20_MINS_TO_40_MINS: array of string

_40_MINS_TO_1_HOUR: array of string

OVER_3_HOURS: array of string

timestamps: array of string

UNDER_10_MINS: array of string

#### RadarAttacksLayer3Top

##### [Get top layer 3 attack pairs (origin and target locations)](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/top/methods/attacks)

GET/radar/attacks/layer3/top/attacks

##### [Get top industries targeted by layer 3 attacks](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/top/methods/industry)

Deprecated

GET/radar/attacks/layer3/top/industry

##### [Get top verticals targeted by layer 3 attacks](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/top/methods/vertical)

Deprecated

GET/radar/attacks/layer3/top/vertical

##### ModelsExpand Collapse 

TopAttacksResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { originCountryAlpha2, originCountryName, value } 

originCountryAlpha2: string

originCountryName: string

value: string

TopIndustryResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { name, value } 

name: string

value: string

TopVerticalResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { name, value } 

name: string

value: string

#### RadarAttacksLayer3TopLocations

##### [Get top origin locations of layer 3 attacks](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/top/subresources/locations/methods/origin)

GET/radar/attacks/layer3/top/locations/origin

##### [Get top target locations of layer 3 attacks](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/top/subresources/locations/methods/target)

GET/radar/attacks/layer3/top/locations/target

##### ModelsExpand Collapse 

LocationOriginResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { originCountryAlpha2, originCountryName, rank, value } 

originCountryAlpha2: string

originCountryName: string

rank: number

value: string

LocationTargetResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { rank, targetCountryAlpha2, targetCountryName, value } 

rank: number

targetCountryAlpha2: string

targetCountryName: string

value: string

#### RadarAttacksLayer7

##### [Get layer 7 attacks summary by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/methods/summary_v2)

GET/radar/attacks/layer7/summary/{dimension}

##### [Get layer 7 attacks time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/methods/timeseries)

GET/radar/attacks/layer7/timeseries

##### [Get layer 7 attacks time series grouped by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/methods/timeseries_groups_v2)

GET/radar/attacks/layer7/timeseries_groups/{dimension}

##### ModelsExpand Collapse 

Layer7SummaryV2Response object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: map[string]

Layer7TimeseriesResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps, values } 

timestamps: array of string

values: array of string

Layer7TimeseriesGroupsV2Response object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

#### RadarAttacksLayer7Summary

##### [Get layer 7 attacks by IP version summary](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/summary/methods/ip_version)

Deprecated

GET/radar/attacks/layer7/summary/ip_version

##### [Get layer 7 attacks by HTTP method summary](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/summary/methods/http_method)

Deprecated

GET/radar/attacks/layer7/summary/http_method

##### [Get layer 7 attacks by HTTP version summary](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/summary/methods/http_version)

Deprecated

GET/radar/attacks/layer7/summary/http_version

##### [Get layer 7 attacks by managed rules summary](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/summary/methods/managed_rules)

Deprecated

GET/radar/attacks/layer7/summary/managed_rules

##### [Get layer 7 attacks by mitigation product summary](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/summary/methods/mitigation_product)

Deprecated

GET/radar/attacks/layer7/summary/mitigation_product

##### [Get layer 7 attacks by targeted industry summary](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/summary/methods/industry)

Deprecated

GET/radar/attacks/layer7/summary/industry

##### [Get layer 7 attacks by targeted vertical summary](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/summary/methods/vertical)

Deprecated

GET/radar/attacks/layer7/summary/vertical

##### ModelsExpand Collapse 

SummaryIPVersionResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { IPv4, IPv6 } 

IPv4: string

IPv6: string

SummaryHTTPMethodResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: map[string]

SummaryHTTPVersionResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { "HTTP/1.x", "HTTP/2", "HTTP/3" } 

"HTTP/1.x": string

"HTTP/2": string

"HTTP/3": string

SummaryManagedRulesResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: map[string]

SummaryMitigationProductResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: map[string]

SummaryIndustryResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: map[string]

SummaryVerticalResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: map[string]

#### RadarAttacksLayer7Timeseries Groups

##### [Get layer 7 attacks by target industries time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/timeseries_groups/methods/industry)

Deprecated

GET/radar/attacks/layer7/timeseries_groups/industry

##### [Get layer 7 attacks by IP version time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/timeseries_groups/methods/ip_version)

Deprecated

GET/radar/attacks/layer7/timeseries_groups/ip_version

##### [Get layer 7 attacks by vertical time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/timeseries_groups/methods/vertical)

Deprecated

GET/radar/attacks/layer7/timeseries_groups/vertical

##### [Get layer 7 attacks by HTTP method time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/timeseries_groups/methods/http_method)

Deprecated

GET/radar/attacks/layer7/timeseries_groups/http_method

##### [Get layer 7 attacks by HTTP version time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/timeseries_groups/methods/http_version)

Deprecated

GET/radar/attacks/layer7/timeseries_groups/http_version

##### [Get layer 7 attacks by managed rules time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/timeseries_groups/methods/managed_rules)

Deprecated

GET/radar/attacks/layer7/timeseries_groups/managed_rules

##### [Get layer 7 attacks by mitigation product time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/timeseries_groups/methods/mitigation_product)

Deprecated

GET/radar/attacks/layer7/timeseries_groups/mitigation_product

##### ModelsExpand Collapse 

TimeseriesGroupIndustryResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

TimeseriesGroupIPVersionResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { IPv4, IPv6, timestamps } 

IPv4: array of string

IPv6: array of string

timestamps: array of string

TimeseriesGroupVerticalResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

TimeseriesGroupHTTPMethodResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

TimeseriesGroupHTTPVersionResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { "HTTP/1.x", "HTTP/2", "HTTP/3", timestamps } 

"HTTP/1.x": array of string

"HTTP/2": array of string

"HTTP/3": array of string

timestamps: array of string

TimeseriesGroupManagedRulesResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

TimeseriesGroupMitigationProductResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

#### RadarAttacksLayer7Top

##### [Get top layer 7 attack pairs (origin and target locations)](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/top/methods/attacks)

GET/radar/attacks/layer7/top/attacks

##### [Get top industries targeted by layer 7 attacks](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/top/methods/industry)

Deprecated

GET/radar/attacks/layer7/top/industry

##### [Get top verticals targeted by layer 7 attacks](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/top/methods/vertical)

Deprecated

GET/radar/attacks/layer7/top/vertical

##### ModelsExpand Collapse 

TopAttacksResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { originCountryAlpha2, originCountryName, targetCountryAlpha2, 2 more } 

originCountryAlpha2: string

originCountryName: string

targetCountryAlpha2: string

targetCountryName: string

value: string

TopIndustryResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { name, value } 

name: string

value: string

TopVerticalResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { name, value } 

name: string

value: string

#### RadarAttacksLayer7TopLocations

##### [Get top origin locations of layer 7 attacks](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/top/subresources/locations/methods/origin)

GET/radar/attacks/layer7/top/locations/origin

##### [Get top target locations of layer 7 attacks](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/top/subresources/locations/methods/target)

GET/radar/attacks/layer7/top/locations/target

##### ModelsExpand Collapse 

LocationOriginResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { originCountryAlpha2, originCountryName, rank, value } 

originCountryAlpha2: string

originCountryName: string

rank: number

value: string

LocationTargetResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { rank, targetCountryAlpha2, targetCountryName, value } 

rank: number

targetCountryAlpha2: string

targetCountryName: string

value: string

#### RadarAttacksLayer7TopAses

##### [Get top origin ASes of layer 7 attacks](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/top/subresources/ases/methods/origin)

GET/radar/attacks/layer7/top/ases/origin

##### ModelsExpand Collapse 

AseOriginResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { originAsn, originAsnName, rank, value } 

originAsn: string

originAsnName: string

rank: number

value: string

#### RadarEntities

##### [Get IP address details](https://developers.cloudflare.com/api/resources/radar/subresources/entities/methods/get)

GET/radar/entities/ip

##### ModelsExpand Collapse 

EntityGetResponse object { ip } 

ip: object { asn, asnLocation, asnName, 5 more } 

asn: string

asnLocation: string

asnName: string

asnOrgName: string

ip: string

ipVersion: string

location: string

locationName: string

#### RadarEntitiesASNs

##### [List autonomous systems](https://developers.cloudflare.com/api/resources/radar/subresources/entities/subresources/asns/methods/list)

GET/radar/entities/asns

##### [Get AS details by ASN](https://developers.cloudflare.com/api/resources/radar/subresources/entities/subresources/asns/methods/get)

GET/radar/entities/asns/{asn}

##### [Get AS-level relationships by ASN](https://developers.cloudflare.com/api/resources/radar/subresources/entities/subresources/asns/methods/rel)

GET/radar/entities/asns/{asn}/rel

##### [Get IRR AS-SETs that an AS is a member of](https://developers.cloudflare.com/api/resources/radar/subresources/entities/subresources/asns/methods/as_set)

GET/radar/entities/asns/{asn}/as_set

##### [Get AS details by IP address](https://developers.cloudflare.com/api/resources/radar/subresources/entities/subresources/asns/methods/ip)

GET/radar/entities/asns/ip

##### [Get AS rankings by botnet threat feed activity](https://developers.cloudflare.com/api/resources/radar/subresources/entities/subresources/asns/methods/botnet_threat_feed)

GET/radar/entities/asns/botnet_threat_feed

##### ModelsExpand Collapse 

ASNListResponse object { asns } 

asns: array of object { asn, country, countryName, 5 more } 

asn: number

country: string

countryName: string

estimatedUsers: object { estimatedUsers } 

estimatedUsers: optional number

Total estimated users.

name: string

aka: optional string

orgName: optional string

website: optional string

ASNGetResponse object { asn } 

asn: object { asn, confidenceLevel, country, 8 more } 

asn: number

confidenceLevel: number

country: string

countryName: string

estimatedUsers: object { locations, estimatedUsers } 

locations: array of object { locationAlpha2, locationName, estimatedUsers } 

locationAlpha2: string

locationName: string

estimatedUsers: optional number

Estimated users per location.

estimatedUsers: optional number

Total estimated users.

name: string

orgName: string

related: array of object { asn, name, aka, estimatedUsers } 

asn: number

name: string

aka: optional string

estimatedUsers: optional number

Total estimated users.

source: string

Regional Internet Registry.

website: string

aka: optional string

ASNRelResponse object { meta, rels } 

meta: object { data_time, query_time, total_peers } 

data_time: string

query_time: string

total_peers: number

rels: array of object { asn1, asn1_country, asn1_name, 4 more } 

asn1: number

asn1_country: string

asn1_name: string

asn2: number

asn2_country: string

asn2_name: string

rel: string

ASNAsSetResponse object { as_sets, paths } 

as_sets: array of object { as_members_count, as_set_members_count, as_set_upstreams_count, 6 more } 

as_members_count: number

The number of AS members in the AS-SET

as_set_members_count: number

The number of AS-SET members in the AS-SET

as_set_upstreams_count: number

The number of recursive upstream AS-SETs

asn_cone_size: number

The number of unique ASNs in the AS-SETs recursive downstream

irr_sources: array of string

The IRR sources of the AS-SET

name: string

The name of the AS-SET

hierarchical_asn: optional number

The AS number following hierarchical AS-SET name

inferred_asn: optional number

The inferred AS number of the AS-SET

peeringdb_asn: optional number

The AS number matching PeeringDB record

paths: array of array of string

Paths from the AS-SET that include the given AS to its upstreams recursively

ASNIPResponse object { asn } 

asn: object { asn, country, countryName, 7 more } 

asn: number

country: string

countryName: string

estimatedUsers: object { locations, estimatedUsers } 

locations: array of object { locationAlpha2, locationName, estimatedUsers } 

locationAlpha2: string

locationName: string

estimatedUsers: optional number

Estimated users per location.

estimatedUsers: optional number

Total estimated users.

name: string

orgName: string

related: array of object { asn, name, aka, estimatedUsers } 

asn: number

name: string

aka: optional string

estimatedUsers: optional number

Total estimated users.

source: string

Regional Internet Registry.

website: string

aka: optional string

ASNBotnetThreatFeedResponse object { ases, meta } 

ases: array of object { asn, country, name, 2 more } 

asn: number

country: string

name: string

rank: number

rankChange: optional number

meta: object { date, total, compareDate } 

date: string

total: number

compareDate: optional string

#### RadarEntitiesLocations

##### [List locations](https://developers.cloudflare.com/api/resources/radar/subresources/entities/subresources/locations/methods/list)

GET/radar/entities/locations

##### [Get location details](https://developers.cloudflare.com/api/resources/radar/subresources/entities/subresources/locations/methods/get)

GET/radar/entities/locations/{location}

##### ModelsExpand Collapse 

LocationListResponse object { locations } 

locations: array of object { alpha2, continent, latitude, 4 more } 

alpha2: string

continent: string

latitude: string

A numeric string.

longitude: string

A numeric string.

name: string

region: string

subregion: string

LocationGetResponse object { location } 

location: object { alpha2, confidenceLevel, continent, 5 more } 

alpha2: string

confidenceLevel: number

continent: string

latitude: string

A numeric string.

longitude: string

A numeric string.

name: string

region: string

subregion: string

#### RadarGeolocations

##### [List Geolocations](https://developers.cloudflare.com/api/resources/radar/subresources/geolocations/methods/list)

GET/radar/geolocations

##### [Get Geolocation details](https://developers.cloudflare.com/api/resources/radar/subresources/geolocations/methods/get)

GET/radar/geolocations/{geo_id}

##### ModelsExpand Collapse 

GeolocationListResponse object { geolocations } 

geolocations: array of object { geoId, latitude, longitude, 5 more } 

geoId: string

latitude: string

A numeric string.

longitude: string

A numeric string.

name: string

parent: object { geoId, latitude, longitude, 5 more } 

geoId: string

latitude: string

A numeric string.

longitude: string

A numeric string.

name: string

parent: object { geoId, latitude, longitude, 4 more } 

geoId: string

latitude: string

A numeric string.

longitude: string

A numeric string.

name: string

type: "CONTINENT" or "COUNTRY" or "ADM1"

The type of the geolocation.

One of the following:

"CONTINENT"

"COUNTRY"

"ADM1"

code: optional string

locale: optional string

BCP 47 locale code used for the geolocation name translation

type: "CONTINENT" or "COUNTRY" or "ADM1"

The type of the geolocation.

One of the following:

"CONTINENT"

"COUNTRY"

"ADM1"

code: optional string

locale: optional string

BCP 47 locale code used for the geolocation name translation

type: "CONTINENT" or "COUNTRY" or "ADM1"

The type of the geolocation.

One of the following:

"CONTINENT"

"COUNTRY"

"ADM1"

code: optional string

locale: optional string

BCP 47 locale code used for the geolocation name translation

GeolocationGetResponse object { geolocation } 

geolocation: object { geoId, latitude, longitude, 5 more } 

geoId: string

latitude: string

A numeric string.

longitude: string

A numeric string.

name: string

parent: object { geoId, latitude, longitude, 5 more } 

geoId: string

latitude: string

A numeric string.

longitude: string

A numeric string.

name: string

parent: object { geoId, latitude, longitude, 4 more } 

geoId: string

latitude: string

A numeric string.

longitude: string

A numeric string.

name: string

type: "CONTINENT" or "COUNTRY" or "ADM1"

The type of the geolocation.

One of the following:

"CONTINENT"

"COUNTRY"

"ADM1"

code: optional string

locale: optional string

BCP 47 locale code used for the geolocation name translation

type: "CONTINENT" or "COUNTRY" or "ADM1"

The type of the geolocation.

One of the following:

"CONTINENT"

"COUNTRY"

"ADM1"

code: optional string

locale: optional string

BCP 47 locale code used for the geolocation name translation

type: "CONTINENT" or "COUNTRY" or "ADM1"

The type of the geolocation.

One of the following:

"CONTINENT"

"COUNTRY"

"ADM1"

code: optional string

locale: optional string

BCP 47 locale code used for the geolocation name translation

#### RadarHTTP

##### [Get HTTP requests summary by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/http/methods/summary_v2)

GET/radar/http/summary/{dimension}

##### [Get HTTP requests time series](https://developers.cloudflare.com/api/resources/radar/subresources/http/methods/timeseries)

GET/radar/http/timeseries

##### [Get HTTP requests time series grouped by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/http/methods/timeseries_groups_v2)

GET/radar/http/timeseries_groups/{dimension}

##### ModelsExpand Collapse 

HTTPSummaryV2Response object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: map[string]

HTTPTimeseriesResponse object { meta } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

HTTPTimeseriesGroupsV2Response object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

#### RadarHTTPLocations

##### [Get top locations by HTTP requests](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/locations/methods/get)

GET/radar/http/top/locations

##### ModelsExpand Collapse 

LocationGetResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { clientCountryAlpha2, clientCountryName, value } 

clientCountryAlpha2: string

clientCountryName: string

value: string

A numeric string.

#### RadarHTTPLocationsBot Class

##### [Get top locations by HTTP requests for a bot class](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/locations/subresources/bot_class/methods/get)

GET/radar/http/top/locations/bot_class/{bot_class}

##### ModelsExpand Collapse 

BotClassGetResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { clientCountryAlpha2, clientCountryName, value } 

clientCountryAlpha2: string

clientCountryName: string

value: string

A numeric string.

#### RadarHTTPLocationsDevice Type

##### [Get top locations by HTTP requests for a device type](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/locations/subresources/device_type/methods/get)

GET/radar/http/top/locations/device_type/{device_type}

##### ModelsExpand Collapse 

DeviceTypeGetResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { clientCountryAlpha2, clientCountryName, value } 

clientCountryAlpha2: string

clientCountryName: string

value: string

A numeric string.

#### RadarHTTPLocationsHTTP Protocol

##### [Get top locations by HTTP requests for an HTTP protocol](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/locations/subresources/http_protocol/methods/get)

GET/radar/http/top/locations/http_protocol/{http_protocol}

##### ModelsExpand Collapse 

HTTPProtocolGetResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { clientCountryAlpha2, clientCountryName, value } 

clientCountryAlpha2: string

clientCountryName: string

value: string

A numeric string.

#### RadarHTTPLocationsHTTP Method

##### [Get top locations by HTTP requests for an HTTP version](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/locations/subresources/http_method/methods/get)

GET/radar/http/top/locations/http_version/{http_version}

##### ModelsExpand Collapse 

HTTPMethodGetResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { clientCountryAlpha2, clientCountryName, value } 

clientCountryAlpha2: string

clientCountryName: string

value: string

A numeric string.

#### RadarHTTPLocationsIP Version

##### [Get top locations by HTTP requests for an IP version](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/locations/subresources/ip_version/methods/get)

GET/radar/http/top/locations/ip_version/{ip_version}

##### ModelsExpand Collapse 

IPVersionGetResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { clientCountryAlpha2, clientCountryName, value } 

clientCountryAlpha2: string

clientCountryName: string

value: string

A numeric string.

#### RadarHTTPLocationsOS

##### [Get top locations by HTTP requests for an OS](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/locations/subresources/os/methods/get)

GET/radar/http/top/locations/os/{os}

##### ModelsExpand Collapse 

OSGetResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { clientCountryAlpha2, clientCountryName, value } 

clientCountryAlpha2: string

clientCountryName: string

value: string

A numeric string.

#### RadarHTTPLocationsTLS Version

##### [Get top locations by HTTP requests for a TLS version](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/locations/subresources/tls_version/methods/get)

GET/radar/http/top/locations/tls_version/{tls_version}

##### ModelsExpand Collapse 

TLSVersionGetResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { clientCountryAlpha2, clientCountryName, value } 

clientCountryAlpha2: string

clientCountryName: string

value: string

A numeric string.

#### RadarHTTPLocationsBrowser Family

##### [Get top locations by HTTP requests for a browser family](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/locations/subresources/browser_family/methods/get)

GET/radar/http/top/locations/browser_family/{browser_family}

##### ModelsExpand Collapse 

BrowserFamilyGetResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { clientCountryAlpha2, clientCountryName, value } 

clientCountryAlpha2: string

clientCountryName: string

value: string

A numeric string.

#### RadarHTTPAses

##### [Get top ASes by HTTP requests](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/ases/methods/get)

GET/radar/http/top/ases

##### ModelsExpand Collapse 

AseGetResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { clientASN, clientASName, value } 

clientASN: number

clientASName: string

value: string

A numeric string.

#### RadarHTTPAsesBot Class

##### [Get top ASes by HTTP requests for a bot class](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/ases/subresources/bot_class/methods/get)

GET/radar/http/top/ases/bot_class/{bot_class}

##### ModelsExpand Collapse 

BotClassGetResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { clientASN, clientASName, value } 

clientASN: number

clientASName: string

value: string

A numeric string.

#### RadarHTTPAsesDevice Type

##### [Get top ASes by HTTP requests for a device type](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/ases/subresources/device_type/methods/get)

GET/radar/http/top/ases/device_type/{device_type}

##### ModelsExpand Collapse 

DeviceTypeGetResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { clientASN, clientASName, value } 

clientASN: number

clientASName: string

value: string

A numeric string.

#### RadarHTTPAsesHTTP Protocol

##### [Get top ASes by HTTP requests for an HTTP protocol](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/ases/subresources/http_protocol/methods/get)

GET/radar/http/top/ases/http_protocol/{http_protocol}

##### ModelsExpand Collapse 

HTTPProtocolGetResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { clientASN, clientASName, value } 

clientASN: number

clientASName: string

value: string

A numeric string.

#### RadarHTTPAsesHTTP Method

##### [Get top ASes by HTTP requests for an HTTP version](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/ases/subresources/http_method/methods/get)

GET/radar/http/top/ases/http_version/{http_version}

##### ModelsExpand Collapse 

HTTPMethodGetResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { clientASN, clientASName, value } 

clientASN: number

clientASName: string

value: string

A numeric string.

#### RadarHTTPAsesIP Version

##### [Get top ASes by HTTP requests for an IP version](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/ases/subresources/ip_version/methods/get)

GET/radar/http/top/ases/ip_version/{ip_version}

##### ModelsExpand Collapse 

IPVersionGetResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { clientASN, clientASName, value } 

clientASN: number

clientASName: string

value: string

A numeric string.

#### RadarHTTPAsesOS

##### [Get top ASes by HTTP requests for an OS](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/ases/subresources/os/methods/get)

GET/radar/http/top/ases/os/{os}

##### ModelsExpand Collapse 

OSGetResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { clientASN, clientASName, value } 

clientASN: number

clientASName: string

value: string

A numeric string.

#### RadarHTTPAsesTLS Version

##### [Get top ASes by HTTP requests for a TLS version](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/ases/subresources/tls_version/methods/get)

GET/radar/http/top/ases/tls_version/{tls_version}

##### ModelsExpand Collapse 

TLSVersionGetResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { clientASN, clientASName, value } 

clientASN: number

clientASName: string

value: string

A numeric string.

#### RadarHTTPAsesBrowser Family

##### [Get top ASes by HTTP requests for a browser family](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/ases/subresources/browser_family/methods/get)

GET/radar/http/top/ases/browser_family/{browser_family}

##### ModelsExpand Collapse 

BrowserFamilyGetResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { clientASN, clientASName, value } 

clientASN: number

clientASName: string

value: string

A numeric string.

#### RadarHTTPSummary

##### [Get HTTP requests by bot class summary](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/summary/methods/bot_class)

Deprecated

GET/radar/http/summary/bot_class

##### [Get HTTP requests by device type summary](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/summary/methods/device_type)

Deprecated

GET/radar/http/summary/device_type

##### [Get HTTP requests by HTTP/HTTPS summary](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/summary/methods/http_protocol)

Deprecated

GET/radar/http/summary/http_protocol

##### [Get HTTP requests by HTTP version summary](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/summary/methods/http_version)

Deprecated

GET/radar/http/summary/http_version

##### [Get HTTP requests by IP version summary](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/summary/methods/ip_version)

Deprecated

GET/radar/http/summary/ip_version

##### [Get HTTP requests by OS summary](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/summary/methods/os)

Deprecated

GET/radar/http/summary/os

##### [Get HTTP requests by TLS version summary](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/summary/methods/tls_version)

Deprecated

GET/radar/http/summary/tls_version

##### [Get HTTP requests by post-quantum support summary](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/summary/methods/post_quantum)

Deprecated

GET/radar/http/summary/post_quantum

##### ModelsExpand Collapse 

SummaryBotClassResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { bot, human } 

bot: string

A numeric string.

human: string

A numeric string.

SummaryDeviceTypeResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { desktop, mobile, other } 

desktop: string

A numeric string.

mobile: string

A numeric string.

other: string

A numeric string.

SummaryHTTPProtocolResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { http, https } 

http: string

A numeric string.

https: string

A numeric string.

SummaryHTTPVersionResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { "HTTP/1.x", "HTTP/2", "HTTP/3" } 

"HTTP/1.x": string

A numeric string.

"HTTP/2": string

A numeric string.

"HTTP/3": string

A numeric string.

SummaryIPVersionResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { IPv4, IPv6 } 

IPv4: string

A numeric string.

IPv6: string

A numeric string.

SummaryOSResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { ANDROID, IOS } 

ANDROID: string

A numeric string.

IOS: string

A numeric string.

SummaryTLSVersionResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { "TLS 1.0", "TLS 1.1", "TLS 1.2", 2 more } 

"TLS 1.0": string

A numeric string.

"TLS 1.1": string

A numeric string.

"TLS 1.2": string

A numeric string.

"TLS 1.3": string

A numeric string.

"TLS QUIC": string

A numeric string.

SummaryPostQuantumResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { NOT_SUPPORTED, SUPPORTED } 

NOT_SUPPORTED: string

A numeric string.

SUPPORTED: string

A numeric string.

#### RadarHTTPTimeseries Groups

##### [Get HTTP requests by TLS version time series](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/timeseries_groups/methods/tls_version)

Deprecated

GET/radar/http/timeseries_groups/tls_version

##### [Get HTTP requests by bot class time series](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/timeseries_groups/methods/bot_class)

Deprecated

GET/radar/http/timeseries_groups/bot_class

##### [Get HTTP requests by user agent time series](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/timeseries_groups/methods/browser)

Deprecated

GET/radar/http/timeseries_groups/browser

##### [Get HTTP requests by user agent family time series](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/timeseries_groups/methods/browser_family)

Deprecated

GET/radar/http/timeseries_groups/browser_family

##### [Get HTTP requests by device type time series](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/timeseries_groups/methods/device_type)

Deprecated

GET/radar/http/timeseries_groups/device_type

##### [Get HTTP requests by HTTP/HTTPS time series](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/timeseries_groups/methods/http_protocol)

Deprecated

GET/radar/http/timeseries_groups/http_protocol

##### [Get HTTP requests by HTTP version time series](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/timeseries_groups/methods/http_version)

Deprecated

GET/radar/http/timeseries_groups/http_version

##### [Get HTTP requests by IP version time series](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/timeseries_groups/methods/ip_version)

Deprecated

GET/radar/http/timeseries_groups/ip_version

##### [Get HTTP requests by OS time series](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/timeseries_groups/methods/os)

Deprecated

GET/radar/http/timeseries_groups/os

##### [Get HTTP requests by post-quantum support time series](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/timeseries_groups/methods/post_quantum)

Deprecated

GET/radar/http/timeseries_groups/post_quantum

##### ModelsExpand Collapse 

TimeseriesGroupTLSVersionResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps, "TLS 1.0", "TLS 1.1", 3 more } 

timestamps: array of string

"TLS 1.0": array of string

"TLS 1.1": array of string

"TLS 1.2": array of string

"TLS 1.3": array of string

"TLS QUIC": array of string

TimeseriesGroupBotClassResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { bot, human, timestamps } 

bot: array of string

human: array of string

timestamps: array of string

TimeseriesGroupBrowserResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

TimeseriesGroupBrowserFamilyResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

TimeseriesGroupDeviceTypeResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { desktop, mobile, other, timestamps } 

desktop: array of string

mobile: array of string

other: array of string

timestamps: array of string

TimeseriesGroupHTTPProtocolResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { http, https, timestamps } 

http: array of string

https: array of string

timestamps: array of string

TimeseriesGroupHTTPVersionResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { "HTTP/1.x", "HTTP/2", "HTTP/3", timestamps } 

"HTTP/1.x": array of string

"HTTP/2": array of string

"HTTP/3": array of string

timestamps: array of string

TimeseriesGroupIPVersionResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { IPv4, IPv6, timestamps } 

IPv4: array of string

IPv6: array of string

timestamps: array of string

TimeseriesGroupOSResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

TimeseriesGroupPostQuantumResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { NOT_SUPPORTED, SUPPORTED, timestamps } 

NOT_SUPPORTED: array of string

SUPPORTED: array of string

timestamps: array of string

#### RadarHTTPTop

##### [Get top user agents by HTTP requests](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/top/methods/browser)

Deprecated

GET/radar/http/top/browser

##### [Get top user agent families by HTTP requests](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/top/methods/browser_family)

Deprecated

GET/radar/http/top/browser_family

##### ModelsExpand Collapse 

TopBrowserResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { name, value } 

name: string

value: string

TopBrowserFamilyResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { name, value } 

name: string

value: string

#### RadarOrigins

##### [List Origins](https://developers.cloudflare.com/api/resources/radar/subresources/origins/methods/list)

GET/radar/origins

##### [Get Origin details](https://developers.cloudflare.com/api/resources/radar/subresources/origins/methods/get)

GET/radar/origins/{slug}

##### [Get origin metrics time series](https://developers.cloudflare.com/api/resources/radar/subresources/origins/methods/timeseries)

GET/radar/origins/timeseries

##### [Get origin metrics distribution by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/origins/methods/summary)

GET/radar/origins/summary/{dimension}

##### [Get origin metrics time series grouped by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/origins/methods/timeseries_groups)

GET/radar/origins/timeseries_groups/{dimension}

##### ModelsExpand Collapse 

OriginListResponse object { origins } 

origins: array of object { regions, slug } 

regions: array of object { region } 

region: string

The region code.

slug: string

The origin slug.

OriginGetResponse object { origin } 

origin: object { regions, slug } 

regions: array of object { region } 

region: string

The region code.

slug: string

The origin slug.

OriginTimeseriesResponse object { meta } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

OriginSummaryResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: map[string]

OriginTimeseriesGroupsResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

#### RadarQuality

#### RadarQualityIQI

##### [Get Internet Quality Index (IQI) summary](https://developers.cloudflare.com/api/resources/radar/subresources/quality/subresources/iqi/methods/summary)

GET/radar/quality/iqi/summary

##### [Get Internet Quality Index (IQI) time series](https://developers.cloudflare.com/api/resources/radar/subresources/quality/subresources/iqi/methods/timeseries_groups)

GET/radar/quality/iqi/timeseries_groups

##### ModelsExpand Collapse 

IQISummaryResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { p25, p50, p75 } 

p25: string

A numeric string.

p50: string

A numeric string.

p75: string

A numeric string.

IQITimeseriesGroupsResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

#### RadarQualitySpeed

##### [Get speed tests summary](https://developers.cloudflare.com/api/resources/radar/subresources/quality/subresources/speed/methods/summary)

GET/radar/quality/speed/summary

##### [Get speed tests histogram](https://developers.cloudflare.com/api/resources/radar/subresources/quality/subresources/speed/methods/histogram)

GET/radar/quality/speed/histogram

##### ModelsExpand Collapse 

SpeedSummaryResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { bandwidthDownload, bandwidthUpload, jitterIdle, 4 more } 

bandwidthDownload: string

A numeric string.

bandwidthUpload: string

A numeric string.

jitterIdle: string

A numeric string.

jitterLoaded: string

A numeric string.

latencyIdle: string

A numeric string.

latencyLoaded: string

A numeric string.

packetLoss: string

A numeric string.

SpeedHistogramResponse object { histogram_0, meta } 

histogram_0: object { bandwidthDownload, bandwidthUpload, bucketMin } 

bandwidthDownload: array of string

bandwidthUpload: array of string

bucketMin: array of string

meta: object { bucketSize, confidenceInfo, dateRange, 4 more } 

Metadata for the results.

bucketSize: number

The width for every bucket in the histogram.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

totalTests: array of number

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

#### RadarQualitySpeedTop

##### [Get top ASes by speed test results](https://developers.cloudflare.com/api/resources/radar/subresources/quality/subresources/speed/subresources/top/methods/ases)

GET/radar/quality/speed/top/ases

##### [Get top locations by speed test results](https://developers.cloudflare.com/api/resources/radar/subresources/quality/subresources/speed/subresources/top/methods/locations)

GET/radar/quality/speed/top/locations

##### ModelsExpand Collapse 

TopAsesResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { bandwidthDownload, bandwidthUpload, clientASN, 7 more } 

bandwidthDownload: string

A numeric string.

bandwidthUpload: string

A numeric string.

clientASN: number

clientASName: string

jitterIdle: string

A numeric string.

jitterLoaded: string

A numeric string.

latencyIdle: string

A numeric string.

latencyLoaded: string

A numeric string.

numTests: number

rankPower: number

TopLocationsResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { bandwidthDownload, bandwidthUpload, clientCountryAlpha2, 7 more } 

bandwidthDownload: string

A numeric string.

bandwidthUpload: string

A numeric string.

clientCountryAlpha2: string

clientCountryName: string

jitterIdle: string

A numeric string.

jitterLoaded: string

A numeric string.

latencyIdle: string

A numeric string.

latencyLoaded: string

A numeric string.

numTests: number

rankPower: number

#### RadarRanking

##### [Get domains rank time series](https://developers.cloudflare.com/api/resources/radar/subresources/ranking/methods/timeseries_groups)

GET/radar/ranking/timeseries_groups

##### [Get top or trending domains](https://developers.cloudflare.com/api/resources/radar/subresources/ranking/methods/top)

GET/radar/ranking/top

##### ModelsExpand Collapse 

RankingTimeseriesGroupsResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

RankingTopResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 3 more } 

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

top_0: object { date } 

date: string

formatdate

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { categories, domain, rank, pctRankChange } 

categories: array of object { id, name, superCategoryId } 

id: number

name: string

superCategoryId: number

domain: string

rank: number

pctRankChange: optional number

Only available in TRENDING rankings.

#### RadarRankingDomain

##### [Get domain rank details](https://developers.cloudflare.com/api/resources/radar/subresources/ranking/subresources/domain/methods/get)

GET/radar/ranking/domain/{domain}

##### ModelsExpand Collapse 

DomainGetResponse object { details_0, meta } 

details_0: object { categories, bucket, rank, top_locations } 

categories: array of object { id, name, superCategoryId } 

id: number

name: string

superCategoryId: number

bucket: optional string

Only available in POPULAR ranking for the most recent ranking.

rank: optional number

top_locations: optional array of object { locationCode, locationName, rank } 

locationCode: string

locationName: string

rank: number

meta: object { dateRange } 

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

#### RadarRankingInternet Services

##### [Get Internet services rank time series](https://developers.cloudflare.com/api/resources/radar/subresources/ranking/subresources/internet_services/methods/timeseries_groups)

GET/radar/ranking/internet_services/timeseries_groups

##### [Get top Internet services](https://developers.cloudflare.com/api/resources/radar/subresources/ranking/subresources/internet_services/methods/top)

GET/radar/ranking/internet_services/top

##### [List Internet services categories](https://developers.cloudflare.com/api/resources/radar/subresources/ranking/subresources/internet_services/methods/categories)

GET/radar/ranking/internet_services/categories

##### ModelsExpand Collapse 

InternetServiceTimeseriesGroupsResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

InternetServiceTopResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 3 more } 

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

top_0: object { date, serviceCategory } 

date: string

formatdate

serviceCategory: string

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { rank, service } 

rank: number

service: string

InternetServiceCategoriesResponse object { categories_0 } 

categories_0: array of object { name } 

name: string

#### RadarTraffic Anomalies

##### [Get latest Internet traffic anomalies](https://developers.cloudflare.com/api/resources/radar/subresources/traffic_anomalies/methods/get)

GET/radar/traffic_anomalies

##### ModelsExpand Collapse 

TrafficAnomalyGetResponse object { trafficAnomalies } 

trafficAnomalies: array of object { asnDetails, endDate, locationDetails, 6 more } 

asnDetails: object { asn, location, name } 

asn: string

location: object { code, name } 

code: string

name: string

name: string

endDate: string

formatdate-time

locationDetails: object { code, name } 

code: string

name: string

originDetails: object { name, origin } 

name: string

origin: string

startDate: string

formatdate-time

status: string

type: string

uuid: string

visibleInDataSources: array of string

#### RadarTraffic AnomaliesLocations

##### [Get top locations by total traffic anomalies](https://developers.cloudflare.com/api/resources/radar/subresources/traffic_anomalies/subresources/locations/methods/get)

GET/radar/traffic_anomalies/locations

##### ModelsExpand Collapse 

LocationGetResponse object { trafficAnomalies } 

trafficAnomalies: array of object { clientCountryAlpha2, clientCountryName, value } 

clientCountryAlpha2: string

clientCountryName: string

value: string

A numeric string.

#### RadarTCP Resets Timeouts

##### [Get TCP resets and timeouts summary](https://developers.cloudflare.com/api/resources/radar/subresources/tcp_resets_timeouts/methods/summary)

GET/radar/tcp_resets_timeouts/summary

##### [Get TCP resets and timeouts time series](https://developers.cloudflare.com/api/resources/radar/subresources/tcp_resets_timeouts/methods/timeseries_groups)

GET/radar/tcp_resets_timeouts/timeseries_groups

##### ModelsExpand Collapse 

TCPResetsTimeoutSummaryResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { later_in_flow, no_match, post_ack, 2 more } 

later_in_flow: string

Connection resets within the first 10 packets from the client, but after the server has received multiple data packets.

no_match: string

All other connections.

post_ack: string

Connection resets or timeouts after the server received both a SYN packet and an ACK packet, meaning the connection was successfully established.

post_psh: string

Connection resets or timeouts after the server received a packet with PSH flag set, following connection establishment.

post_syn: string

Connection resets or timeouts after the server received only a single SYN packet.

TCPResetsTimeoutTimeseriesGroupsResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { later_in_flow, no_match, post_ack, 3 more } 

later_in_flow: array of string

no_match: array of string

post_ack: array of string

post_psh: array of string

post_syn: array of string

timestamps: array of string

#### RadarTLDs

##### [List TLDs](https://developers.cloudflare.com/api/resources/radar/subresources/tlds/methods/list)

GET/radar/tlds

##### [Get TLD details](https://developers.cloudflare.com/api/resources/radar/subresources/tlds/methods/get)

GET/radar/tlds/{tld}

##### ModelsExpand Collapse 

TLDListResponse object { tlds } 

tlds: array of object { manager, tld, type } 

manager: string

The organization that manages the TLD.

tld: string

The actual TLD.

type: string

The type of TLD.

TLDGetResponse object { tld } 

tld: object { manager, tld, type } 

manager: string

The organization that manages the TLD.

tld: string

The actual TLD.

type: string

The type of TLD.

#### RadarTLDsPerformance

##### [Get TLD Performance Summary](https://developers.cloudflare.com/api/resources/radar/subresources/tlds/subresources/performance/methods/summary)

GET/radar/tlds/performance/summary/{dimension}

##### [Get TLD Performance Over Time](https://developers.cloudflare.com/api/resources/radar/subresources/tlds/subresources/performance/methods/timeseries_groups)

GET/radar/tlds/performance/timeseries_groups/{dimension}

##### ModelsExpand Collapse 

PerformanceSummaryResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: map[string]

PerformanceTimeseriesGroupsResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

#### RadarRobots TXT

#### RadarRobots TXTTop

##### [Get top domain categories by robots.txt files parsed](https://developers.cloudflare.com/api/resources/radar/subresources/robots_txt/subresources/top/methods/domain_categories)

GET/radar/robots_txt/top/domain_categories

##### ModelsExpand Collapse 

TopDomainCategoriesResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { name, value } 

name: string

value: number

#### RadarRobots TXTTopUser Agents

##### [Get top user agents on robots.txt files](https://developers.cloudflare.com/api/resources/radar/subresources/robots_txt/subresources/top/subresources/user_agents/methods/directive)

GET/radar/robots_txt/top/user_agents/directive

##### ModelsExpand Collapse 

UserAgentDirectiveResponse object { meta, top_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

top_0: array of object { name, value, fully, partially } 

name: string

value: number

fully: optional number

partially: optional number

#### RadarLeaked Credentials

##### [Get HTTP authentication requests distribution by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/leaked_credentials/methods/summary_v2)

GET/radar/leaked_credential_checks/summary/{dimension}

##### [Get time series distribution of HTTP authentication requests by dimension.](https://developers.cloudflare.com/api/resources/radar/subresources/leaked_credentials/methods/timeseries_groups_v2)

GET/radar/leaked_credential_checks/timeseries_groups/{dimension}

##### ModelsExpand Collapse 

LeakedCredentialSummaryV2Response object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: map[string]

LeakedCredentialTimeseriesGroupsV2Response object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { timestamps } 

timestamps: array of string

#### RadarLeaked CredentialsSummary

##### [Get HTTP authentication requests by bot class summary](https://developers.cloudflare.com/api/resources/radar/subresources/leaked_credentials/subresources/summary/methods/bot_class)

Deprecated

GET/radar/leaked_credential_checks/summary/bot_class

##### [Get HTTP authentication requests by compromised credential status summary](https://developers.cloudflare.com/api/resources/radar/subresources/leaked_credentials/subresources/summary/methods/compromised)

Deprecated

GET/radar/leaked_credential_checks/summary/compromised

##### ModelsExpand Collapse 

SummaryBotClassResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { bot, human } 

bot: string

A numeric string.

human: string

A numeric string.

SummaryCompromisedResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: object { CLEAN, COMPROMISED } 

CLEAN: string

A numeric string.

COMPROMISED: string

A numeric string.

#### RadarLeaked CredentialsTimeseries Groups

##### [Get HTTP authentication requests by bot class time series](https://developers.cloudflare.com/api/resources/radar/subresources/leaked_credentials/subresources/timeseries_groups/methods/bot_class)

Deprecated

GET/radar/leaked_credential_checks/timeseries_groups/bot_class

##### [Get HTTP authentication requests by compromised credential status time series](https://developers.cloudflare.com/api/resources/radar/subresources/leaked_credentials/subresources/timeseries_groups/methods/compromised)

Deprecated

GET/radar/leaked_credential_checks/timeseries_groups/compromised

##### ModelsExpand Collapse 

TimeseriesGroupBotClassResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { bot, human, timestamps } 

bot: array of string

human: array of string

timestamps: array of string

TimeseriesGroupCompromisedResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

serie_0: object { CLEAN, COMPROMISED, timestamps } 

CLEAN: array of string

COMPROMISED: array of string

timestamps: array of string

[ Previous

* * *

Rules ](https://developers.cloudflare.com/api/resources/rum/subresources/rules)[ Next

* * *

Agent Readiness ](https://developers.cloudflare.com/api/resources/radar/subresources/agent_readiness)
