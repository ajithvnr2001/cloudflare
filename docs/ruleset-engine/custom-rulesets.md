---
url: https://developers.cloudflare.com/ruleset-engine/custom-rulesets/
title: Work with custom rulesets \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:01.842694+00:00
---

# Work with custom rulesets · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/custom-rulesets/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /Work with custom rulesets



# Work with custom rulesets

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ruleset-engine/custom-rulesets/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewChange the behavior of a custom ruleset

Use the following workflow to deploy a custom ruleset:

  1. [Create a custom ruleset](https://developers.cloudflare.com/ruleset-engine/custom-rulesets/create-custom-ruleset/), optionally providing a list of rules to include in the custom ruleset.
  2. (Optional) [Add rules to your custom ruleset](https://developers.cloudflare.com/ruleset-engine/custom-rulesets/add-rules-ruleset/).
  3. [Deploy the custom ruleset](https://developers.cloudflare.com/ruleset-engine/custom-rulesets/deploy-custom-ruleset/) by adding an `execute` rule to a phase entry point ruleset. If you skip this step, the rules of the custom ruleset will not run.



Currently, custom rulesets are only supported by the [Cloudflare WAF](https://developers.cloudflare.com/waf/), both at the account and the zone level.

Note

You cannot execute a custom ruleset from another custom ruleset, only from an [entry point ruleset](https://developers.cloudflare.com/ruleset-engine/about/rulesets/#entry-point-ruleset).

## Change the behavior of a custom ruleset

To modify custom ruleset behavior, Cloudflare recommends [creating a new custom ruleset](https://developers.cloudflare.com/ruleset-engine/custom-rulesets/create-custom-ruleset/) or [editing the custom ruleset](https://developers.cloudflare.com/ruleset-engine/custom-rulesets/add-rules-ruleset/) instead of using overrides.

[PreviousCreate an exception](https://developers.cloudflare.com/ruleset-engine/managed-rulesets/create-exception/)[NextCreate a custom ruleset](https://developers.cloudflare.com/ruleset-engine/custom-rulesets/create-custom-ruleset/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ruleset-engine/custom-rulesets/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
