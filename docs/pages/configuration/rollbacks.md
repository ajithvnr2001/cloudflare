---
url: https://developers.cloudflare.com/pages/configuration/rollbacks/
title: Rollbacks \u00b7 Cloudflare Pages docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:29.241106+00:00
---

# Rollbacks · Cloudflare Pages docs

> Source: https://developers.cloudflare.com/pages/configuration/rollbacks/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Pages](https://developers.cloudflare.com/pages/)
  3. /Configuration
  4. /Rollbacks



# Rollbacks

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/pages/configuration/rollbacks/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRelated resources

Rollbacks allow you to instantly revert your project to a previous production deployment.

Any production deployment that has been successfully built is a valid rollback target. When your project has rolled back to a previous deployment, you may still rollback to deployments that are newer than your current version. Note that preview deployments are not valid rollback targets.

In order to perform a rollback, go to **Deployments** in your Pages project. Browse the **All deployments** list and select the three dotted actions menu for the desired target. Select **Rollback to this deployment** for a confirmation window to appear. When confirmed, your project's production deployment will change instantly.

![Deployments for your Pages project that can be used for rollbacks](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2144,height=662,format=webp/_astro/rollbacks.DNHeRPOm.png)

## Related resources

  * [Preview Deployments](https://developers.cloudflare.com/pages/configuration/preview-deployments/)
  * [Branch deployment controls](https://developers.cloudflare.com/pages/configuration/branch-build-controls/)



[PreviousREST API](https://developers.cloudflare.com/pages/configuration/api/)[NextServing Pages](https://developers.cloudflare.com/pages/configuration/serving-pages/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/pages/configuration/rollbacks.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
