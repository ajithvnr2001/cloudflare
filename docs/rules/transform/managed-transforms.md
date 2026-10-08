---
url: https://developers.cloudflare.com/rules/transform/managed-transforms/
title: Managed Transforms \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:56.691252+00:00
---

# Managed Transforms · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/transform/managed-transforms/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /[Transform Rules](https://developers.cloudflare.com/rules/transform/)
  4. /Managed Transforms



# Managed Transforms

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/transform/managed-transforms/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewNext steps

Managed Transforms allow you to perform common adjustments to HTTP request and response headers with pre-built, one-step configurations. The available adjustments include:

  * Add bot protection request headers.
  * Remove or add headers related to the visitor's IP address.
  * Add request header when Cloudflare detects [leaked credentials](https://developers.cloudflare.com/waf/detections/leaked-credentials/).
  * Add security-related response headers.
  * Remove `X-Powered-By` response headers.



For a complete list, refer to [Available Managed Transforms](https://developers.cloudflare.com/rules/transform/managed-transforms/reference/).

When you enable a Managed Transform, Cloudflare internally deploys one or more Transform Rules to handle the common configuration you selected. These generated rules will not count against the [maximum number of Transform Rules](https://developers.cloudflare.com/rules/transform/#availability) available in your Cloudflare plan.

Enabled Managed Transforms will apply to all inbound requests for the [zone](https://developers.cloudflare.com/fundamentals/concepts/accounts-and-zones/#zones) (domain or subdomain added to Cloudflare).

Note

The generated internal Transform Rules will not appear in the Transform Rules list in the Cloudflare dashboard.

## Next steps

For dashboard, API, and Terraform instructions, refer to [Configure Managed Transforms](https://developers.cloudflare.com/rules/transform/managed-transforms/configure/).

[PreviousAPI parameter reference](https://developers.cloudflare.com/rules/transform/response-header-modification/reference/parameters/)[NextConfigure Managed Transforms](https://developers.cloudflare.com/rules/transform/managed-transforms/configure/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/transform/managed-transforms/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
