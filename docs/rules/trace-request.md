---
url: https://developers.cloudflare.com/rules/trace-request/
title: Trace a request with Cloudflare Trace \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:55.834868+00:00
---

# Trace a request with Cloudflare Trace · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/trace-request/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /Trace a request



# Trace a request

Last updated Aug 25, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/trace-request/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhen to use TraceResources

Available on all plans

Cloudflare Trace (Beta) simulates an HTTP/S request through Cloudflare's network to your origin server. Use this tool to understand how your Cloudflare configurations (such as rules, caching, and security settings) would affect a specific request. If the hostname you are testing is not [proxied by Cloudflare](https://developers.cloudflare.com/dns/proxy-status/), Cloudflare Trace will still return all the configurations that Cloudflare would have applied to the request.

You can define specific request properties to simulate different conditions for an HTTP/S request. Rules that are turned off in Cloudflare products will not be evaluated.

Cloudflare Trace is available to users with an Administrator or Super Administrator role.

## When to use Trace

Use Trace when you need to test what would happen with a simulated request:

  * Understanding why a rule did not trigger as expected
  * Testing how your rules handle different request scenarios
  * Seeing the evaluation order of your rules
  * Simulating requests from different geolocations or conditions



Use [Log Explorer](https://developers.cloudflare.com/log-explorer/) when you need to investigate what actually happened with real production traffic:

  * Analyzing historical data and trends
  * Investigating security incidents after they occur
  * Searching for patterns across thousands of requests
  * Monitoring application performance over time
  * Providing forensic evidence to support teams



The key difference is that Trace simulates "what-if" scenarios, while Log Explorer shows actual historical traffic.

## Resources

  * [Use Cloudflare Trace](https://developers.cloudflare.com/rules/trace-request/how-to/)
  * [Cloudflare Trace limitations](https://developers.cloudflare.com/rules/trace-request/limitations/)
  * [Cloudflare Trace changelog](https://developers.cloudflare.com/rules/trace-request/changelog/)



[PreviousExamples](https://developers.cloudflare.com/rules/normalization/examples/)[NextUse Cloudflare Trace](https://developers.cloudflare.com/rules/trace-request/how-to/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/trace-request/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
