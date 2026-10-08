---
url: https://developers.cloudflare.com/style-guide/documentation-content-strategy/component-attributes/glossary-entry/
title: Glossary entry \u00b7 Cloudflare Style Guide
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:20:08.444239+00:00
---

# Glossary entry · Cloudflare Style Guide

> Source: https://developers.cloudflare.com/style-guide/documentation-content-strategy/component-attributes/glossary-entry/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Style Guide](https://developers.cloudflare.com/style-guide/)
  3. /…

[Product content](https://developers.cloudflare.com/style-guide/documentation-content-strategy/)

  4. /[Component attributes](https://developers.cloudflare.com/style-guide/documentation-content-strategy/component-attributes/)
  5. /Glossary entry



# Glossary entry

Last updated Apr 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/style-guide/documentation-content-strategy/component-attributes/glossary-entry/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewDefinitionUsed inStructure Data Usage

## Definition

A single term and corresponding definition in the glossary.

## Used in

Glossary, documentation pages, tooltips.

## Structure

### Data

The data underlying our glossary lives with YAML files in the [`/src/content/glossary/*` ↗︎](https://github.com/cloudflare/cloudflare-docs/tree/production/src/content/glossary) folder.

Each file should be structured similar to the following:

dns.yamlyaml
    
    
    ---
    productName: DNS
    entries:
      - term: active zone
        general_definition: |-
          a DNS zone that is active on Cloudflare requires changing its nameservers to Cloudflare's for management.
        associated_products:
          - Cloudflare One
    
      - term: apex domain
        general_definition: |-
          apex domain is used to refer to a domain that does not contain a subdomain part, such as `example.com` (without `www.`). It is also known as "root domain" or "naked domain".
    
      - term: DNS over HTTPS
        general_definition: |-
          DNS over HTTPS (DoH) is a standard for encrypting DNS traffic, preventing tracking and spoofing of DNS queries.
        associated_products:
          - 1.1.1.1
          - Cloudflare One
    
      - term: DNS over TLS
        general_definition: |-
          DNS over TLS (DoT) is a standard for encrypting DNS traffic using its own port (853) and TLS encryption.
        associated_products:
          - 1.1.1.1
          - Cloudflare One

Relevant values include the following:

  * `productName` string required

    * Core product associated with this file. Should always match the same formatting / styling used in `associated_products`.
  * `entries` object required

    * `term` string required

      * The glossary term itself.
    * `general_definition` string required

      * Definition of the term. Should be general enough to apply to multiple products. Should also start with a lowercase letter unless starting with a proper noun.
    * `associated_products` array optional

      * If the term is associated with other products. Any names used should correspond to the `productName` of that associated file.



### Usage

Because of the structured data associated with our glossaries, we can pull these terms into multiple places.

#### Product-level glossary

A product-level glossary includes all terms associated with a particular product, which will pull in terms directly in that product's glossary file and any terms that include the product in its `associated_products`.

/src/content/docs/dns/glossary.mdxmdx
    
    
    ---
    title: Glossary
    pcx_content_type: glossary
    ---
    
    import { Glossary } from "~/components";
    
    Review the definitions for terms used across Cloudflare's DNS documentation.
    
    <Glossary product="dns" />

#### Glossary definition

Pull glossary definitions directly into your Markdown by using the `<GlossaryDefinition>` component.

> A DNS zone that is active on Cloudflare requires changing its nameservers to Cloudflare's for management.

Is a quoted definition that comes from:
    
    
    <GlossaryDefinition term="active zone" prepend="An active zone is " />

Properties are:

  * `term` string required

    * Should match a term within an existing glossary YAML file.
  * `prepend` string optional

    * Text to add before a definition.



#### Glossary tooltip

Pull component definitions into a focusable tooltip for a specific phrase by using the `<GlossaryTooltip>` component.

Here's a tooltip example.
    
    
    Here's a <GlossaryTooltip term="active zone">tooltip</GlossaryTooltip> example.

Properties are:

  * `term` string required

    * Should match a term within an existing glossary YAML file.
  * `prepend` string optional

    * Text to add before a definition.
  * `link` string optional

    * Wraps the inner text in a markdown link, similar to normal markdown formatting.



Because of space limitations, the tooltip will always default to the short definition of a term, meaning the definition text before the first line break.

[PreviousExamples](https://developers.cloudflare.com/style-guide/documentation-content-strategy/component-attributes/examples/)[NextImages and diagrams](https://developers.cloudflare.com/style-guide/documentation-content-strategy/component-attributes/images-and-diagrams/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/style-guide/documentation-content-strategy/component-attributes/glossary-entry.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
