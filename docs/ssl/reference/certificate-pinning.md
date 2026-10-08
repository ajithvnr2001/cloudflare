---
url: https://developers.cloudflare.com/ssl/reference/certificate-pinning/
title: Certificate pinning \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:45.466305+00:00
---

# Certificate pinning · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/reference/certificate-pinning/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /Reference
  4. /Certificate pinning



# Certificate pinning

Last updated Apr 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/reference/certificate-pinning/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRecommended alternativeIf you must pin certificates

Cloudflare does not support [HTTP public key pinning (HPKP)](https://developers.cloudflare.com/ssl/reference/certificate-pinning/) for universal, advanced, or custom hostname certificates.

Cloudflare regularly rotates the edge certificates provisioned for your domain. If HPKP was enabled, your domain would go offline each time a certificate rotates because the new certificate would not match the pinned key. Additionally, [industry experts ↗︎](https://scotthelme.co.uk/im-giving-up-on-hpkp/) discourage using HPKP. For a detailed overview, refer to the Cloudflare blog post on [why certificate pinning is outdated ↗︎](https://blog.cloudflare.com/why-certificate-pinning-is-outdated/).

## Recommended alternative

The problem HPKP tries to solve is preventing certificate misissuance. A safer way to detect misissuance without risking downtime is [Certificate Transparency Monitoring](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/certificate-transparency-monitoring/), which alerts you when a certificate is issued for your domain.

## If you must pin certificates

If your use case requires certificate pinning, the only advisable approach is to upload a [custom certificate](https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/) to Cloudflare and pin to that certificate. Because you control the certificate lifecycle — including renewal timing, CA selection, and key material — you can ensure pin continuity. However, pinning still carries outage risk: if a renewal deploys a new key, clients pinned to the old key will fail TLS. If you need pin continuity, you must intentionally reuse the same key material during renewal. Test renewed certificates in the [staging environment](https://developers.cloudflare.com/ssl/edge-certificates/staging-environment/) before production.

Select the [**user-defined** bundle method](https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/bundling-methodologies/#user-defined) so that you control exactly which CA, intermediate, and leaf certificate are served.

[PreviousRotate ACM certificate packs](https://developers.cloudflare.com/ssl/reference/certificate-rotation/)[NextCertificate statuses](https://developers.cloudflare.com/ssl/reference/certificate-statuses/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/reference/certificate-pinning.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
