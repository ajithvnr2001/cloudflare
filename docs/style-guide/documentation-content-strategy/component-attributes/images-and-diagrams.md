---
url: https://developers.cloudflare.com/style-guide/documentation-content-strategy/component-attributes/images-and-diagrams/
title: Images and diagrams \u00b7 Cloudflare Style Guide
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:20:08.526744+00:00
---

# Images and diagrams · Cloudflare Style Guide

> Source: https://developers.cloudflare.com/style-guide/documentation-content-strategy/component-attributes/images-and-diagrams/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Style Guide](https://developers.cloudflare.com/style-guide/)
  3. /…

[Product content](https://developers.cloudflare.com/style-guide/documentation-content-strategy/)

  4. /[Component attributes](https://developers.cloudflare.com/style-guide/documentation-content-strategy/component-attributes/)
  5. /Images and diagrams



# Images and diagrams

Last updated Aug 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/style-guide/documentation-content-strategy/component-attributes/images-and-diagrams/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewScreenshots When to use Guidelines Usage MaintenanceDiagrams SVG diagrams Mermaid diagramsReference diagram

Images help a reader see a tool, a process, or an architecture. This page covers three: screenshots, diagrams, and reference diagrams. Because images cost more to maintain than text, use them intentionally.

## Screenshots

A screenshot is a picture of a software tool, in this case usually the Cloudflare dashboard. We only recommend screenshots in specific scenarios, as they have a higher maintenance cost than other types of content.

### When to use

Use screenshots sparingly and intentionally. For example, it is appropriate to use a screenshot when the task is simple but often confuses readers or is hard to describe with words alone.

A canonical example is [Find account and zone ID](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/) because:

  * It is a high driver of SEO traffic to our [Community ↗︎](https://community.cloudflare.com).
  * We tried explaining with words alone and that did not solve the confusion.
  * It is a task specifically related to new users, who are less familiar with Cloudflare concepts or navigation patterns.



Note

Use screenshots liberally in [Changelog entries](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/changelog/), because this content type is an accepted point-in-time reference and it is okay for these screenshots to be outdated.

### Guidelines

Screenshots should:

  * Maintain the original aspect-lock ratio.
  * Keep resolution at 72dpi.
  * Keep width at 500-600 pixels.
  * Avoid sharing sensitive information (you may need to edit the underlying HTML in your browser).
  * Avoid including visuals that change frequently, such as sidebar navigation.
  * Have descriptive alt text.



### Usage
    
    
    ![Alt text](~/assets/images/$PRODUCT_NAME/$IMAGE_NAME.png)

Add screenshots to the corresponding `$PRODUCT_NAME` folder under [`/src/assets/images/` ↗︎](https://github.com/cloudflare/cloudflare-docs/tree/production/src/assets/images). You may want to add subfolders for organizational purposes.

### Maintenance

We avoid screenshots without a clear purpose because they are difficult to maintain. This is because:

  * The UI might change and our team might not know.
  * Even if you do know what changed, it is difficult to find which screenshots reference a particular UI flow.
  * If something changes, you need to fully re-take the screenshot to replace it. This could involve adding fake data or hiding sensitive information.



For more details on how we approach this maintenance, refer to [Image maintenance](https://developers.cloudflare.com/style-guide/how-we-docs/image-maintenance/).

## Diagrams

Diagrams are visualizations that depict a process, architecture, or some other form of technology. They explain complex topics in a compelling way and help a reader visualize a specific solution, process, or interaction between products. Diagrams are used in all content types. We recommend either SVG files or Mermaid diagrams.

### SVG diagrams

Use SVG files instead of PNG or JPEG because SVG scales well when a reader zooms in. Use clear and straightforward alt text with your SVG for use by screen readers. We optimize SVG files with a [recurring script ↗︎](https://github.com/cloudflare/cloudflare-docs/blob/production/scripts/optimize-svgs.ts) in our repo.

Format an SVG like this:
    
    
    ![Alt text](/link/to/image.svg "Caption to go under the image")

For example:

![A simple flow diagram shows interactions between important elements of the design.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=441,height=261,format=webp/_astro/simple-flow.DifdHPUG.png)An example flow diagram
    
    
    ![A simple flow diagram shows interactions between important elements of the design.](~/assets/images/firewall/simple-flow.png "An example flow diagram")

### Mermaid diagrams

Use Mermaid diagrams to illustrate product or process flows. If they work for your use case, Mermaid diagrams are preferable to SVG files because they are more easily searchable and changeable. Our Mermaid diagrams are based on [`rehype-mermaid` ↗︎](https://github.com/remcohaszing/rehype-mermaid/) and [`mermaid` ↗︎](https://www.npmjs.com/package/mermaid).

Format a Mermaid diagram like this:
    
    
    ```mermaid
    flowchart LR
    accTitle: Tunnels diagram
    accDescr: The example in this diagram has three tunnel routes. Tunnels 1 and 2 have top priority and Tunnel 3 is secondary.
    
    subgraph Cloudflare
    direction LR
    B[Cloudflare <br/> data center]
    C[Cloudflare <br/> data center]
    D[Cloudflare <br/> data center]
    end
    
    A((User)) --> Cloudflare --- E[Anycast IP]
    E[Anycast IP] --> F[/Tunnel 1 / <br/> priority 1/] --> I{{Customer <br/> data center/ <br/> network 1}}
    E[Anycast IP] --> G[/Tunnel 2 / <br/> priority 1/] --> J{{Customer <br/> data center/ <br/> network 2}}
    E[Anycast IP] --> H[/Tunnel 3 / <br/> priority 2/] --> K{{Customer <br/> data center/ <br/> network 3}}
    ```

For example, this renders as:
    
    
    flowchart LR
    accTitle: Tunnels diagram
    accDescr: The example in this diagram has three tunnel routes. Tunnels 1 and 2 have top priority and Tunnel 3 is secondary.
    
    subgraph Cloudflare
    direction LR
    B[Cloudflare <br/> data center]
    C[Cloudflare <br/> data center]
    D[Cloudflare <br/> data center]
    end
    
    A((User)) --> Cloudflare --- E[Anycast IP]
    E[Anycast IP] --> F[/Tunnel 1 / <br/> priority 1/] --> I{{Customer <br/> data center/ <br/> network 1}}
    E[Anycast IP] --> G[/Tunnel 2 / <br/> priority 1/] --> J{{Customer <br/> data center/ <br/> network 2}}
    E[Anycast IP] --> H[/Tunnel 3 / <br/> priority 2/] --> K{{Customer <br/> data center/ <br/> network 3}}
    

## Reference diagram

A single diagram that portrays all or part of Cloudflare's platform and how Cloudflare would align with a customer's infrastructure or use case.

**Used in** : [Reference architecture](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/reference-architecture/), [Reference architecture diagram](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/reference-architecture/#reference-architecture-diagrams)

Show a complete Cloudflare architecture aligned with a specific infrastructure or use case. Whenever possible, the image should be an SVG.

For example:

![A fully deployed SASE solution with Cloudflare protects every aspect of your business, ensuring all access to applications is secured and all threats from the Internet mitigated.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1226,height=1080,format=svg/_astro/cf1-ref-arch-21.B4dzMu9Q.svg)A fully deployed SASE solution with Cloudflare

 _Note: Labels in this image may reflect a previous product name._

[ PreviousGlossary entry](https://developers.cloudflare.com/style-guide/documentation-content-strategy/component-attributes/glossary-entry/)[NextIntroductions](https://developers.cloudflare.com/style-guide/documentation-content-strategy/component-attributes/introductions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/style-guide/documentation-content-strategy/component-attributes/images-and-diagrams.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
