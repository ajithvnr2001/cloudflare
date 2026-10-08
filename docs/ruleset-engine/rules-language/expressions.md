---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/
title: Rule expressions \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:02.265931+00:00
---

# Rule expressions · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /[Rules language](https://developers.cloudflare.com/ruleset-engine/rules-language/)
  4. /Expressions



# Expressions

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSimple expressionsCompound expressionsMaximum rule expression lengthMaximum regular expressions per ruleAdditional features

The Rules language supports two kinds of expressions: simple and compound.

## Simple expressions

**Simple expressions** compare a value from an HTTP request to a value defined in the expression. For example, this simple expression matches Microsoft Exchange Autodiscover requests:
    
    
    http.request.uri.path matches "/autodiscover\.(xml|src)$"

Simple expressions have the following syntax:
    
    
    <field> <comparison_operator> <value>

Where:

  * [Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/) specify properties associated with an HTTP request.

  * [Comparison operators](https://developers.cloudflare.com/ruleset-engine/rules-language/operators/#comparison-operators) define how values must relate to actual request data for an expression to return `true`.

  * [Values](https://developers.cloudflare.com/ruleset-engine/rules-language/values/) represent the data associated with fields. The right side can contain a [dynamic value](https://developers.cloudflare.com/ruleset-engine/rules-language/operators/#compare-dynamic-values), such as a field or function result.




## Compound expressions

**Compound expressions** use [logical operators](https://developers.cloudflare.com/ruleset-engine/rules-language/operators/#logical-operators) such as `and` to combine two or more expressions into a single expression.

For example, this expression uses the `and` operator to target requests to `www.example.com` that are not on ports 80 or 443:
    
    
    http.host eq "www.example.com" and not cf.edge.server_port in {80 443}

Compound expressions have the following general syntax:
    
    
    <expression> <logical_operator> <expression>

Compound expressions allow you to generate sophisticated, highly targeted rules.

## Maximum rule expression length

The maximum length of a rule expression is 4,096 characters.

This limit applies whether you use the visual [Expression Builder](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/edit-expressions/#expression-builder) to define your expression, or write the expression manually in the [Expression Editor](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/edit-expressions/#expression-editor).

## Maximum regular expressions per rule

Each rule can contain a maximum of 64 regular expressions in its expression. This limit applies across all rule types that use the [Rules language](https://developers.cloudflare.com/ruleset-engine/rules-language/).

Rules that exceed this limit cannot be created or updated. Existing rules above this limit continue to work but cannot be modified until the expression is simplified.

## Additional features

You can also use the following Rules language features in your expressions:

  * [Grouping symbols](https://developers.cloudflare.com/ruleset-engine/rules-language/operators/#grouping-symbols) allow you to explicitly group expressions that should be evaluated together.

  * [Functions](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/) allow you to manipulate and validate values in expressions.




[PreviousOverview](https://developers.cloudflare.com/ruleset-engine/rules-language/)[NextEdit in the dashboard](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/edit-expressions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ruleset-engine/rules-language/expressions/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
