---
url: https://developers.cloudflare.com/images/optimization/hosted-images/preserve-content-credentials/
title: Preserve Content Credentials \u00b7 Cloudflare Images docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:35.157991+00:00
---

# Preserve Content Credentials · Cloudflare Images docs

> Source: https://developers.cloudflare.com/images/optimization/hosted-images/preserve-content-credentials/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Images](https://developers.cloudflare.com/images/)
  3. /…

Optimization

  4. /Hosted images
  5. /Preserve Content Credentials



# Preserve Content Credentials

Last updated Jul 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/images/optimization/hosted-images/preserve-content-credentials/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEnable

[Content Credentials ↗︎](https://contentcredentials.org/) (or C2PA metadata) are a type of metadata that includes the full provenance chain of a digital asset. This provides information about an image's creation, authorship, and editing flow. This data is cryptographically authenticated and can be verified using an [open-source verification service ↗︎](https://contentcredentials.org/verify).

You can preserve Content Credentials on images uploaded to and delivered from Cloudflare Images.

## Enable

Content Credentials preservation is an account-wide setting that applies to every image delivered from `imagedelivery.net` (and any custom domains configured for your Images account).

  1. In the Cloudflare dashboard, go to the **Hosted Images** page.

[ Go to **Hosted images** ↗ ](https://dash.cloudflare.com/?to=/:account/images/hosted)
  2. Select the **Delivery** tab.

  3. Enable **Preserve Content Credentials**.




You can also enable it via the API by making a `PATCH` request to the [images config endpoint](https://developers.cloudflare.com/api/resources/images/subresources/v1/subresources/variants/methods/edit/):
    
    
    curl --request PATCH https://api.cloudflare.com/client/v4/accounts/{account_id}/images/v1/config \
    --header "Authorization: Bearer <API_TOKEN>" \
    --header "Content-Type: application/json" \
    --data '{"preserve_content_credentials": true}'

The behavior of this setting is determined by the [`metadata`](https://developers.cloudflare.com/images/optimization/features/#metadata) parameter applied to each delivered image or variant.

For example, if a variant specifies `metadata=copyright` (the default), then the EXIF copyright tag and all Content Credentials will be preserved in the resulting image and all other metadata will be discarded.

When Content Credentials are preserved during delivery, Cloudflare will keep any existing Content Credentials embedded in the source image and automatically append and cryptographically sign additional actions describing the transformations it applied (such as resizing or format conversion).

[PreviousDelete variants](https://developers.cloudflare.com/images/optimization/hosted-images/delete-variants/)[NextBrowser TTL](https://developers.cloudflare.com/images/optimization/hosted-images/browser-ttl/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/images/optimization/hosted-images/preserve-content-credentials.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
