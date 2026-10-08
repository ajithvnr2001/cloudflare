---
url: https://developers.cloudflare.com/ruleset-engine/about/
title: About Ruleset Engine \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:00.850148+00:00
---

# About Ruleset Engine · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/about/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /About



# About

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ruleset-engine/about/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewGet started

The Cloudflare Ruleset Engine allows you to create and deploy rules and rulesets. The engine syntax, inspired by the Wireshark Display Filter language, is defined by the [Rules language](https://developers.cloudflare.com/ruleset-engine/rules-language/). Cloudflare uses the Ruleset Engine in different products, allowing you to configure several products using the same basic syntax.

There are several elements involved in the configuration and use of the Ruleset Engine. These elements are:

  * [**Phase**](https://developers.cloudflare.com/ruleset-engine/about/phases/): Defines a stage in the life of a request where you can execute rulesets.
  * [**Ruleset**](https://developers.cloudflare.com/ruleset-engine/about/rulesets/): Defines a versioned set of rules. You deploy rulesets to a phase, where they execute.
  * [**Rule**](https://developers.cloudflare.com/ruleset-engine/about/rules/): Defines a filter and an action to perform on incoming requests that match the filter expression. A rule with an `execute` action executes a ruleset.



* * *

## Get started

To view existing rulesets and their properties, refer to [View rulesets](https://developers.cloudflare.com/ruleset-engine/basic-operations/view-rulesets/).

For more information on deploying managed rulesets and defining overrides, refer to [Work with managed rulesets](https://developers.cloudflare.com/ruleset-engine/managed-rulesets/).

For more information on creating and deploying custom rulesets, refer to [Work with custom rulesets](https://developers.cloudflare.com/ruleset-engine/custom-rulesets/).

[PreviousOverview](https://developers.cloudflare.com/ruleset-engine/)[NextPhases](https://developers.cloudflare.com/ruleset-engine/about/phases/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ruleset-engine/about/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
