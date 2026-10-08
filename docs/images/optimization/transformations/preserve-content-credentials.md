---
url: https://developers.cloudflare.com/images/optimization/transformations/preserve-content-credentials/
title: Preserve Content Credentials \u00b7 Cloudflare Images docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:35.764732+00:00
---

# Preserve Content Credentials · Cloudflare Images docs

> Source: https://developers.cloudflare.com/images/optimization/transformations/preserve-content-credentials/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Images](https://developers.cloudflare.com/images/)
  3. /…

Optimization

  4. /Remote images (transformations)
  5. /Preserve Content Credentials



# Preserve Content Credentials

Last updated May 26, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/images/optimization/transformations/preserve-content-credentials/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEnable

[Content Credentials ↗︎](https://contentcredentials.org/) (or C2PA metadata) are a type of metadata that includes the full provenance chain of a digital asset. This provides information about an image's creation, authorship, and editing flow. This data is cryptographically authenticated and can be verified using an [open-source verification service ↗︎](https://contentcredentials.org/verify).

You can preserve Content Credentials when optimizing images stored in remote sources.

## Enable

You can configure how Content Credentials are handled for each zone where transformations are served.

In the Cloudflare dashboard under **Images** > **Transformations** , navigate to a specific zone and enable the toggle to preserve Content Credentials:

![Enable Preserving Content Credentials in the dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1632,height=350,format=webp/_astro/preserve-content-credentials.BDptgOn0.png)

The behavior of this setting is determined by the [`metadata`](https://developers.cloudflare.com/images/optimization/features/#metadata) parameter for each transformation.

For example, if a transformation specifies `metadata=copyright`, then the EXIF copyright tag and all Content Credentials will be preserved in the resulting image and all other metadata will be discarded.

When Content Credentials are preserved in a transformation, Cloudflare will keep any existing Content Credentials embedded in the source image and automatically append and cryptographically sign additional actions.

When this setting is disabled, any existing Content Credentials will always be discarded.

[PreviousSet up rewrite rules](https://developers.cloudflare.com/images/optimization/transformations/rewrite-rules/)[NextServe uploaded images](https://developers.cloudflare.com/images/optimization/hosted-images/serve-uploaded-images/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/images/optimization/transformations/preserve-content-credentials.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
