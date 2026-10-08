---
url: https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/troubleshooting/
title: Troubleshooting Universal SSL \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:41.323410+00:00
---

# Troubleshooting Universal SSL · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/troubleshooting/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /…

[Edge certificates](https://developers.cloudflare.com/ssl/edge-certificates/)

  4. /[Universal SSL](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/)
  5. /Troubleshooting



# Troubleshooting

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/troubleshooting/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewResolve a timed out stateDelete certificatesOther issues

## Resolve a timed out state

If a certificate issuance times out, Cloudflare tells you where in the chain of issuance the timeout occurred: Initializing, Validation, Issuance, Deployment, or Deletion.

To resolve timeout issues, try one or more of the following options:

  * Change the **Proxy status** of related DNS records to **DNS only** (gray-clouded) and wait at least a minute. Then, change the **Proxy status** back to **Proxied** (orange-clouded).
  * [Disable Universal SSL](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/disable-universal-ssl/) and wait at least a minute. Then, re-enable Universal SSL.
  * Send a PATCH request to the [validation endpoint](https://developers.cloudflare.com/api/resources/ssl/subresources/verification/methods/edit/) using the same [DCV method](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/) (API only). Make sure that the `--data` field is not empty in your request.
  * Review your domain control validation (DCV). Changing the DCV method will restart certificate issuance.



## Delete certificates

You can [use the API](https://developers.cloudflare.com/api/resources/ssl/subresources/certificate_packs/methods/delete/) to delete certificates that you no longer want listed on the Cloudflare dashboard.

## Other issues

For additional troubleshooting help, refer to [Troubleshooting SSL errors](https://developers.cloudflare.com/ssl/troubleshooting/).

[PreviousLimitations](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/limitations/)[NextOverview](https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/edge-certificates/universal-ssl/troubleshooting.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
