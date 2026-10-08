---
url: https://developers.cloudflare.com/rules/transform/troubleshooting/
title: Troubleshoot Transform Rules \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:58.384280+00:00
---

# Troubleshoot Transform Rules · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/transform/troubleshooting/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /[Transform Rules](https://developers.cloudflare.com/rules/transform/)
  4. /Troubleshooting



# Troubleshoot Transform Rules

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/transform/troubleshooting/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhy do I not see my request header modifications?

When troubleshooting a rule configuration, review the [Transform Rules evaluation](https://developers.cloudflare.com/rules/transform/#transform-rules-evaluation) section to understand how and when your Transform Rule is evaluated for each request.

For more information on runtime errors related to Transform Rules configuration, refer to [Cloudflare 1xxx errors](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/).

## Why do I not see my request header modifications?

Transform Rules performing request header modifications affect the HTTP headers sent by Cloudflare's network to your origin server. You will not find these headers in your browser request or response data, which can make it difficult to tell if the rule is working as intended.

To check if a request header transform rule is taking effect, you can check the logs on your origin server or use [Cloudflare Trace](https://developers.cloudflare.com/rules/trace-request/) to check that the rule is matching traffic correctly. Since [Cloudflare Logpush](https://developers.cloudflare.com/logs/logpush/) only logs original HTTP request/response headers, Logpush logs will not include any header transformations done via Transform Rules.

To add HTTP headers that website visitors will receive in their browsers, you must [modify the response headers](https://developers.cloudflare.com/rules/transform/response-header-modification/) instead.

[PreviousAvailable Managed Transforms](https://developers.cloudflare.com/rules/transform/managed-transforms/reference/)[NextOverview](https://developers.cloudflare.com/rules/transform/examples/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/transform/troubleshooting.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
