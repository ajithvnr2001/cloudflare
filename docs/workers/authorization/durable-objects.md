---
url: https://developers.cloudflare.com/workers/authorization/durable-objects/
title: Durable Objects roles and permissions \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:09.339662+00:00
---

# Durable Objects roles and permissions · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/authorization/durable-objects/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Roles and permissions](https://developers.cloudflare.com/workers/authorization/)
  4. /Durable Objects



# Durable Objects roles and permissions

Last updated Sep 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/authorization/durable-objects/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewObservability accessData Studio accessRelated resources

Durable Objects do not have separate roles or permissions. Access to a Durable Object is determined by your access to the Worker that implements it.

To give a member, User Group, or API token access to a Durable Object, assign the appropriate Workers role at either the individual Worker scope or the Workers product scope. Refer to [Workers roles and permissions](https://developers.cloudflare.com/workers/authorization/workers/) for available roles and scopes.

## Observability access

`Metadata Read-Only` access to the implementing Worker includes Durable Object metrics, logs, and traces without granting access to data stored in the Durable Object. Granular authorization supports analytics for both SQLite-backed and KV-backed Durable Objects, with one current exception: the **Total KV storage** metric is unavailable for KV-backed Durable Objects.

## Data Studio access

[Durable Objects Data Studio](https://developers.cloudflare.com/durable-objects/observability/data-studio/) can query and modify data stored in SQLite-backed Durable Objects. Accessing Data Studio requires at least `Editor` access to the Worker that implements the Durable Object.

## Related resources

  * [Workers roles and permissions](https://developers.cloudflare.com/workers/authorization/workers/)
  * [Durable Objects metrics and analytics](https://developers.cloudflare.com/durable-objects/observability/metrics-and-analytics/)
  * [Durable Objects Data Studio](https://developers.cloudflare.com/durable-objects/observability/data-studio/)



[PreviousWorkers](https://developers.cloudflare.com/workers/authorization/workers/)[NextOverview](https://developers.cloudflare.com/workers/versions-and-deployments/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/authorization/durable-objects.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
