---
url: https://developers.cloudflare.com/rules/transform/examples/add-request-header-subrequest-other-zone/
title: Add a request header for subrequests from other zones \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:55.785131+00:00
---

# Add a request header for subrequests from other zones · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/transform/examples/add-request-header-subrequest-other-zone/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Transform Rules](https://developers.cloudflare.com/rules/transform/)

  4. /[Examples](https://developers.cloudflare.com/rules/transform/examples/)
  5. /Add a request header for subrequests from other zones



# Add a request header for subrequests from other zones

Create a request header transform rule to add an HTTP header when the Workers subrequest comes from a different zone.

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/transform/examples/add-request-header-subrequest-other-zone/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The following request header transform rule adds an HTTP header to Workers subrequests coming from a different zone:

Text in **Expression Editor** (replace `myappexample.com` with your domain):
    
    
    (cf.worker.upstream_zone != "" and cf.worker.upstream_zone != "myappexample.com")

Selected operation under **Modify request header** : _Set static_

**Header name** : `X-External-Workers-Subrequest`

**Value** : `1`

The [`cf.worker.upstream_zone`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.worker.upstream_zone/) field used in the rule expression is set to empty if the current request is not a Workers subrequest.

[PreviousOverview](https://developers.cloudflare.com/rules/transform/examples/)[NextAdd a request header with the current bot score](https://developers.cloudflare.com/rules/transform/examples/add-request-header-bot-score/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/transform/examples/add-request-header-subrequest-other-zone.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
