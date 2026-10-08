---
url: https://developers.cloudflare.com/rules/transform/examples/rewrite-path-object-storage/
title: Rewrite path for object storage bucket \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:56.143662+00:00
---

# Rewrite path for object storage bucket · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/transform/examples/rewrite-path-object-storage/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Transform Rules](https://developers.cloudflare.com/rules/transform/)

  4. /[Examples](https://developers.cloudflare.com/rules/transform/examples/)
  5. /Rewrite path for object storage bucket



# Rewrite path for object storage bucket

Create a URL rewrite rule (part of Transform Rules) to remove `/files/` from URI paths before routing request to your object storage bucket.

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/transform/examples/rewrite-path-object-storage/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

To remove `/files/` from URI paths before routing request to your object storage bucket, create a new URL rewrite rule and define a dynamic URL path rewrite using [wildcard pattern parameters](https://developers.cloudflare.com/rules/transform/url-rewrite/create-dashboard/#wildcard-pattern-parameters):

**When incoming requests match**

  * **Wildcard pattern**
    * **Request URL** : `https://<YOUR_HOSTNAME>/files/*`



**Then rewrite the path and/or query**

  * **Target path** : [`/`] `files/*`
  * **Rewrite to** : [`/`] `${1}`



Make sure to replace `<YOUR_HOSTNAME>` with your actual hostname and adjust the example paths according to your setup. Then, use [Cloud Connector](https://developers.cloudflare.com/rules/cloud-connector/) to route traffic to an object storage bucket.

[PreviousRewrite page path for visitors in specific countries](https://developers.cloudflare.com/rules/transform/examples/rewrite-welcome-for-countries/)[NextRewrite path of archived blog posts](https://developers.cloudflare.com/rules/transform/examples/rewrite-path-archived-posts/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/transform/examples/rewrite-path-object-storage.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
