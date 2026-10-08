---
url: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/mcp_portal_logs/
title: MCP Portal Logs \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:12.805104+00:00
---

# MCP Portal Logs · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/mcp_portal_logs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /…

[Logpush](https://developers.cloudflare.com/logs/logpush/)Logpush job setup[Datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/)

  4. /Account-scoped datasets
  5. /MCP Portal Logs



# MCP Portal Logs

Last updated Sep 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/mcp_portal_logs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewClientCountryClientIPColoCodeDatetimeErrorMethodPortalAUDPortalIDPromptGetNameResourceReadURIServerAUDServerIDServerResponseDurationMsServerURLSessionIDSuccessToolCallNameUserEmailUserID

The descriptions below detail the fields available for `mcp_portal_logs`.

## ClientCountry

Type: `string`

Country code of the client IP address.

## ClientIP

Type: `string`

IP address of the client that initiated the request.

## ColoCode

Type: `string`

Colo code of the data center that processed the request (for example, 'DFW').

## Datetime

Type: `int or string`

The date and time the request was made.

## Error

Type: `string`

The error message if the request failed and there is additional information.

## Method

Type: `string`

The JSON-RPC method of the request (for example, 'tools/call', 'prompts/get', 'resources/read').

## PortalAUD

Type: `string`

Audience tag of the MCP Portal.

## PortalID

Type: `string`

Unique identifier of the MCP Portal.

## PromptGetName

Type: `string`

For prompts/get requests, the name of the prompt being fetched.

## ResourceReadURI

Type: `string`

For resources/read requests, the URI of the resource being fetched.

## ServerAUD

Type: `string`

Audience tag of the upstream MCP Server.

## ServerID

Type: `string`

Unique identifier of the upstream MCP Server.

## ServerResponseDurationMs

Type: `int`

The time in milliseconds it took for the upstream MCP server to respond.

## ServerURL

Type: `string`

URL of the upstream MCP Server.

## SessionID

Type: `string`

Unique identifier of the stateful MCP session associated with the request.

## Success

Type: `bool`

If the request succeeded.

## ToolCallName

Type: `string`

For tools/call requests, the name of the tool being called.

## UserEmail

Type: `string`

Email address of the authenticated user who performed the request.

## UserID

Type: `string`

Unique identifier of the authenticated user who performed the request.

[PreviousMagic Network Monitoring Flow Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/mnm_flow_logs/)[NextNetwork Analytics Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/network_analytics_logs/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/logpush/logpush-job/datasets/account/mcp_portal_logs.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
