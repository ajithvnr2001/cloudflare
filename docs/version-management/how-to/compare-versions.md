---
url: https://developers.cloudflare.com/version-management/how-to/compare-versions/
title: Compare versions \u00b7 Cloudflare Version Management docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:14.732651+00:00
---

# Compare versions · Cloudflare Version Management docs

> Source: https://developers.cloudflare.com/version-management/how-to/compare-versions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Version Management](https://developers.cloudflare.com/version-management/)
  3. /How to
  4. /Compare versions



# Compare versions

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/version-management/how-to/compare-versions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Quickly view differences between versions to make sure your configurations are correct before [promoting a version](https://developers.cloudflare.com/version-management/how-to/environments/#change-environment-version) to a new environment.

A common use case would be to compare the versions in staging and production to verify the changes before promoting the staging version to production.

To compare versions:

  1. Log in to the Cloudflare dashboard.

[ Go to **Account home** ↗ ](https://dash.cloudflare.com/?to=/:account/home)
  2. Select your account and zone.

  3. Go to **Version Management** > **Comparisons**.

  4. Select two different versions.

  5. Select **Compare**.




After a few seconds, the page will update automatically with a comparison on a per-product basis. The lower numbered version will always be presented on the left and the top will show you which environments the versions are assigned to so that you can ensure you are comparing the right versions.

![View changes side-by-side between versions](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1224,height=788,format=webp/_astro/compare-versions.AiuozF29.png)

Changes will be highlighted for new additions and removals for that service. Based on the comparison, you can then decide if more changes are necessary or if that new version is ready to be rolled out.

[PreviousManage versions](https://developers.cloudflare.com/version-management/how-to/versions/)[NextAvailable configurations](https://developers.cloudflare.com/version-management/reference/available-configurations/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/version-management/how-to/compare-versions.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
