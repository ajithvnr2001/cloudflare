---
url: https://developers.cloudflare.com/style-guide/how-we-docs/links/
title: Link maintenance \u00b7 Cloudflare Style Guide
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:20:12.408827+00:00
---

# Link maintenance · Cloudflare Style Guide

> Source: https://developers.cloudflare.com/style-guide/how-we-docs/links/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Style Guide](https://developers.cloudflare.com/style-guide/)
  3. /[How we docs](https://developers.cloudflare.com/style-guide/how-we-docs/)
  4. /Link maintenance



# Link maintenance

Last updated Aug 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/style-guide/how-we-docs/links/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewLink typesChecks Internal links External links Anchor links

Though [links](https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/structure/links/) are an important part of documentation, they also have their own maintenance cost.

We have a few strategies we use to make link maintenance easier.

## Link types

Documentation uses three [types of links](https://developers.cloudflare.com/style-guide/style-and-grammar/formatting/structure/links/#types-of-links): external, internal, and anchor. For each type, we think through a few different aspects of the experience.

  * **External** : 
    * _Source of truth_ : Another site.
    * _Why does it break_ : Another site changed its content.
    * _Customer experience of a break_ : `404` page on another site.
  * **Internal** : 
    * _Source of truth_ : Your site.
    * _Why does it break_ : Your site changed its content.
    * _Customer experience of a break_ : `404` page on your site.
  * **Anchor** : 
    * _Source of truth_ : Your site.
    * _Why does it break_ : Your site changed its content.
    * _Customer experience of a break_ : Page load on your site. Content might be further down the page or have been moved to another page.



## Checks

### Internal links

Of these three link types, only **Internal** links:

  * Happen _within_ the context of a change to your site's content.
  * Universally lead to a bad customer experience (a `404` page).
  * Are easily auditable within the current context.



For these reasons, we choose to make a build **fail** based on broken internal links. For our implementation, we rely on [Nimbus ↗︎](https://nimbus-docs.com/)'s `nimbus/internal-link` [lint rule ↗︎](https://nimbus-docs.com/writing/linting/), configured in [`astro.config.ts` ↗︎](https://github.com/cloudflare/cloudflare-docs/blob/production/astro.config.ts).

We also make two intentional decisions about this link auditing:

  * **Absolute links, not relative** : We enforce absolute links (`/style-guide/how-we-docs/metadata/`) and fail on relative links (`../metadata/`) to avoid time-consuming maintenance in the future. This decision also helps with find/replace work and any future platform migrations.
  * **No redirects** : We do not consider redirects when evaluating links. We have the current source of truth, so we should utilize that truth to its fullest (as well as helping us avoid redirect chains and future maintenance).



### External links

Though external links are not good for the customer experience, they also don't change within the context of a change to your site's content. Additionally, external link checking can be time consuming and error prone, which can slow down contributions.

We use an external SEO tool to help flag these broken external links for us, addressing them as needed (instead of making a build fail because of them).

### Anchor links

Anchor links do not have as dramatic as consequences of being wrong as internal links. If you have a broken anchor link, a customer will either need to manually scroll to the header or, in some cases, go to another page.

Because of these characteristics, we run [periodic, background checks ↗︎](https://github.com/cloudflare/cloudflare-docs/blob/production/.github/workflows/anchor-link-audit.yml) to flag broken anchor links, using the `htmltest` library.

[PreviousImage maintenance](https://developers.cloudflare.com/style-guide/how-we-docs/image-maintenance/)[NextMetadata](https://developers.cloudflare.com/style-guide/how-we-docs/metadata/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/style-guide/how-we-docs/links.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
