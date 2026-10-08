---
url: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/workers_trace_events/
title: Workers Trace Events \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:13.348111+00:00
---

# Workers Trace Events · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/workers_trace_events/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /…

[Logpush](https://developers.cloudflare.com/logs/logpush/)Logpush job setup[Datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/)

  4. /Account-scoped datasets
  5. /Workers Trace Events



# Workers Trace Events

Last updated Sep 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/workers_trace_events/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCPUTimeMsDispatchNamespaceEntrypointEventEventTimestampMsEventTypeExceptionsLogsOutcomeScriptNameScriptTagsScriptVersionWallTimeMs

The descriptions below detail the fields available for `workers_trace_events`.

## CPUTimeMs

Type: `int`

The amount of CPU time used by the Worker script, in milliseconds.

## DispatchNamespace

Type: `string`

The Cloudflare Worker dispatch namespace.

## Entrypoint

Type: `string`

The name of the entrypoint class in which the Worker began execution.

## Event

Type: `object`

Details about the source event.

## EventTimestampMs

Type: `int`

The timestamp of when the event was received, in milliseconds.

## EventType

Type: `string`

The event type that triggered the invocation.   
Possible values are _fetch_ | _scheduled_ | _alarm_ | _queue_ | _email_ | _worker_rpc_ | _hibernatable_web_socket_.

## Exceptions

Type: `array[object]`

List of uncaught exceptions during the invocation.

## Logs

Type: `array[object]`

List of console messages emitted during the invocation.

## Outcome

Type: `string`

The outcome of the Worker script invocation.   
Possible values are _ok_ | _canceled_ | _exception_ | _unknown_.

## ScriptName

Type: `string`

The Cloudflare Worker script name.

## ScriptTags

Type: `array[string]`

A list of user-defined tags used to categorize the Worker.

## ScriptVersion

Type: `object`

The version of the script that was invoked.

## WallTimeMs

Type: `int`

The elapsed time in milliseconds between the start of a Worker invocation, and when the Workers Runtime determines that no more JavaScript needs to run. Specifically, this measures the wall-clock time that the JavaScript context remained open. For example, when returning a response with a large body, the Workers runtime can, in some cases, determine that no more JavaScript needs to run, and closes the JS context before all the bytes have passed through and been sent. Alternatively, if you use the `waitUntil()` API to perform work without blocking the return of a response, this work may continue executing after the response has been returned, and will be included in `WallTimeMs`.

[PreviousWebSocket Analytics](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/websocket_analytics/)[NextZero Trust Network Session Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/logpush/logpush-job/datasets/account/workers_trace_events.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
