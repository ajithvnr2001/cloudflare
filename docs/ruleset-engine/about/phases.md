---
url: https://developers.cloudflare.com/ruleset-engine/about/phases/
title: Phases \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:00.873031+00:00
---

# Phases · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/about/phases/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /[About](https://developers.cloudflare.com/ruleset-engine/about/)
  4. /Phases



# Phases

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ruleset-engine/about/phases/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

A phase defines a stage in the life of a request where you can execute [rulesets](https://developers.cloudflare.com/ruleset-engine/about/rulesets/). Phases are defined by Cloudflare and cannot be modified.

Phases exist at two levels:

  * At the [account](https://developers.cloudflare.com/fundamentals/concepts/accounts-and-zones/#accounts) level
  * At the [zone](https://developers.cloudflare.com/fundamentals/concepts/accounts-and-zones/#zones) level



For the same phase, rules defined at the account level are evaluated before the rules defined at the zone level.

Each phase has at most one [entry point ruleset](https://developers.cloudflare.com/ruleset-engine/about/rulesets/#entry-point-ruleset) at the account and zone level.

Note

Currently, phases at the account level are only available in Enterprise plans.

The following diagram outlines the request handling process where requests go through the available phases:

![Diagram showing the request handling process. The user request goes through several request phases until it eventually reaches the origin server \(the request can also be blocked\). The origin returns a response, which goes through several response phases until it reaches the user.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1092,height=792,format=webp/_astro/rulesets-phases.D4jji4ui.png)

Cloudflare products are specific to one or more phases, and they add support for different features. Check the documentation for each Cloudflare product for details on the applicable phases.

Refer to [Phases list](https://developers.cloudflare.com/ruleset-engine/reference/phases-list/) for a list of phases and their corresponding Cloudflare products.

[PreviousOverview](https://developers.cloudflare.com/ruleset-engine/about/)[NextRulesets](https://developers.cloudflare.com/ruleset-engine/about/rulesets/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ruleset-engine/about/phases.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
