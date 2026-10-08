---
url: https://developers.cloudflare.com/rules/transform/examples/add-cors-header/
title: Add a wildcard CORS response header \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:55.590570+00:00
---

# Add a wildcard CORS response header · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/transform/examples/add-cors-header/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Transform Rules](https://developers.cloudflare.com/rules/transform/)

  4. /[Examples](https://developers.cloudflare.com/rules/transform/examples/)
  5. /Add a wildcard CORS response header



# Add a wildcard CORS response header

Create a response header transform rule to add an `Access-Control-Allow-Origin` CORS HTTP header to the response with a static wildcard value.

Last updated Dec 10, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/transform/examples/add-cors-header/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The following response header transform rule adds a header named `Access-Control-Allow-Origin` with a static wildcard value (`*`) to the HTTP response:

Text in **Expression Editor** :
    
    
    (http.host eq "<YOUR_HOSTNAME>")

Selected operation under **Modify response header** : _Set static_

**Header name** : `Access-Control-Allow-Origin`

**Value** : `*`

You can also use an expression similar to the following to apply the CORS header to several specific hostnames:
    
    
    (http.host in {"<YOUR_HOSTNAME_1>" "<YOUR_HOSTNAME_2>"})

[PreviousAdd a response header with a static value](https://developers.cloudflare.com/rules/transform/examples/add-response-header-static-value/)[NextAdd request header with a static value](https://developers.cloudflare.com/rules/transform/examples/add-request-header-static-value/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/transform/examples/add-cors-header.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
