---
url: https://developers.cloudflare.com/ruleset-engine/rulesets-api/
title: Rulesets API \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:14.618418+00:00
---

# Rulesets API · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rulesets-api/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /Rulesets API



# Rulesets API

Last updated Sep 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ruleset-engine/rulesets-api/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewGet startedLimits

The Rulesets API provides an interface for managing and configuring the execution of rulesets, supporting different Cloudflare products powered by the Ruleset Engine.

## Get started

To get started, review the [JSON objects](https://developers.cloudflare.com/ruleset-engine/rulesets-api/json-object/) and the available [endpoints](https://developers.cloudflare.com/ruleset-engine/rulesets-api/endpoints/).

You can also [validate a mutation before deployment](https://developers.cloudflare.com/ruleset-engine/rulesets-api/dry-run/) by adding the `dry_run=true` query parameter.

* * *

## Limits

You should avoid making concurrent updates to the same ruleset. There are rate limits in place to prevent the same ruleset from being concurrently updated too many times. The exact limits depend on the size of the ruleset and volume of requests, and can be different for each ruleset.

The rate limits are most frequently hit when concurrently modifying several rules in the same ruleset. To avoid this, you should [update the entire ruleset in a single operation](https://developers.cloudflare.com/ruleset-engine/rulesets-api/update/) instead.

[PreviousFunctions](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/)[NextJSON objects](https://developers.cloudflare.com/ruleset-engine/rulesets-api/json-object/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ruleset-engine/rulesets-api/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
