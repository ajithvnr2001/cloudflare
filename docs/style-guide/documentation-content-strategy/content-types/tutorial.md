---
url: https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/tutorial/
title: Tutorial \u00b7 Cloudflare Style Guide
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:20:10.099274+00:00
---

# Tutorial · Cloudflare Style Guide

> Source: https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/tutorial/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Style Guide](https://developers.cloudflare.com/style-guide/)
  3. /…

[Product content](https://developers.cloudflare.com/style-guide/documentation-content-strategy/)

  4. /[Content types](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/)
  5. /Tutorial



# Tutorial

Last updated Aug 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/tutorial/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhen to use itTitle & descriptionScaffold this pageComponent guidanceFrontmatterKeeping tutorials currentWriting for AI and agents

A tutorial takes a newcomer from nothing to a working project, one visible result at a time, with the author carrying all of the responsibility. The tone is guiding, straightforward, educational, and authoritative.

## When to use it

Write a tutorial when competence requires assembling several of the product's pieces into one real project, the kind of value that shows only when features work together. It is the most expensive type to build and keep true, so reach for one deliberately. It is not:

  * **A quickstart.** A quickstart proves the product works in minutes, whereas a tutorial builds competence through a meaningful project in about an hour.
  * **A how-to.** A how-to serves a competent reader who carries themselves, whereas a tutorial's reader knows nothing, so when something breaks it is the tutorial's fault.
  * **A concept course.** A tutorial teaches by doing rather than by explaining. Link the concept instead of unfolding it.



For the full comparison, refer to [Content types](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/). For a live example, refer to [Workers tutorials](https://developers.cloudflare.com/workers/tutorials/).

## Title & description

  * **Title** : a short verb phrase in the second-person imperative, named by the outcome, such as "Build an order-notification service". Do not use "Learn ..." or "Tutorial 1".
  * **Description** : state what the reader will build and what they will be able to do afterward, then give an honest time estimate.



## Scaffold this page

Use the Nimbus tutorial recipe to generate this page. Your coding agent pulls the full page skeleton and self-review checklist, then adapts them to your product:

npmyarnpnpm
    
    
    npx @cloudflare/nimbus-docs add content-tutorial
    
    
    yarn @cloudflare/nimbus-docs add content-tutorial
    
    
    pnpm @cloudflare/nimbus-docs add content-tutorial

Adapt the frontmatter the recipe emits to Cloudflare's schema: set [`pcx_content_type`](https://developers.cloudflare.com/style-guide/build-the-page/frontmatter/custom-properties/#pcx_content_type) and `products` instead of the generic fields the recipe emits, such as `type`.

## Component guidance

  * [**Steps**](https://developers.cloudflare.com/style-guide/build-the-page/components/steps/) or numbered `##` parts are the spine, and every part ends with the verbatim "You should see" output that proves it worked. Never skip one.
  * **Error-recovery prose** at the points readers actually stumble is happy-path content, not an exception callout, because in a tutorial an anticipated error is not an exception.
  * [**GitHubCode**](https://developers.cloudflare.com/style-guide/build-the-page/components/github-code/) and [**PackageManagers**](https://developers.cloudflare.com/style-guide/build-the-page/components/package-managers/) keep sample code and install commands pinned and in sync, and [**ListTutorials**](https://developers.cloudflare.com/style-guide/build-the-page/components/list-tutorials/) surfaces the tutorial in listings.
  * **What does not fit:** Tabs and options of any kind (the author already chose the one path, and per-stack means per-page), long conceptual asides (link out instead), and anything that hides steps.



## Frontmatter
    
    
    pcx_content_type: tutorial
    difficulty: Beginner
    products:
      - product-a
      - product-b

Set `difficulty` to Beginner, Intermediate, or Advanced, and stamp `reviewed` with the date you last ran the tutorial end to end. For more details, refer to [`pcx_content_type`](https://developers.cloudflare.com/style-guide/build-the-page/frontmatter/custom-properties/#pcx_content_type).

## Keeping tutorials current

A tutorial is the most expensive type to keep true, because it must work for every reader, every time, on a cold machine, and a broken tutorial convinces a newcomer that the product itself is broken. Fewest and freshest wins, so one tested tutorial beats five stale ones. Pin every version the tutorial depends on, re-run it end to end on a clean environment each release, and stamp `reviewed` with that date.

  * [`ListTutorials`](https://developers.cloudflare.com/style-guide/build-the-page/components/list-tutorials/)



## Writing for AI and agents

  * **Self-contained parts.** Give every part a full-context heading, the full command, and the verbatim result, so a reader or agent landing mid-tutorial knows where they are, and never use a positional reference such as "as configured above."
  * **Literal output.** Keep every expected output in a fenced code block with complete, realistic values, because that "You should see" text is what agents and readers match against.
  * **Pinned versions.** Name and pin every version in the prerequisites, so the tutorial does not silently drift off the latest release.



[Previous3rd-party integration guide](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/3rd-party-integration-guide/)[NextConfiguration](https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/configuration/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/style-guide/documentation-content-strategy/content-types/tutorial.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
