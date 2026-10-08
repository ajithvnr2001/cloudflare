---
url: https://developers.cloudflare.com/rules/transform/examples/
title: Transform Rules examples \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:55.476810+00:00
---

# Transform Rules examples · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/transform/examples/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /[Transform Rules](https://developers.cloudflare.com/rules/transform/)
  4. /Examples



# Transform Rules examples

Last updated May 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/transform/examples/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[**Add a wildcard CORS response header** Create a CORS response header transform rule to add an `Access-Control-Allow-Origin` HTTP header to the response with wildcard as static value. (`cookiename=value`).](https://developers.cloudflare.com/rules/transform/examples/add-cors-header/)

[**Add a request header with the current bot score** Create a request header transform rule to add a `X-Bot-Score` HTTP header to the request with the current bot score.](https://developers.cloudflare.com/rules/transform/examples/add-request-header-bot-score/)

[**Add request header with a static value** Create a request header transform rule to add an `X-Source` HTTP header to the request with a static value (`Cloudflare`).](https://developers.cloudflare.com/rules/transform/examples/add-request-header-static-value/)

[**Add a request header for subrequests from other zones** Create a request header transform rule to add an HTTP header when the Workers subrequest comes from a different zone.](https://developers.cloudflare.com/rules/transform/examples/add-request-header-subrequest-other-zone/)

[**Add a response header with a static value** Create a response header transform rule to add a `set-cookie` HTTP header to the response with a static value (`cookiename=value`).](https://developers.cloudflare.com/rules/transform/examples/add-response-header-static-value/)

[**Normalize encoded slashes in URL path** Create a URL rewrite rule (part of Transform Rules) to normalize encoded forward slashes (`%2F`) in the request path to standard slashes (`/`).](https://developers.cloudflare.com/rules/transform/examples/normalize-encoded-slash/)

[**Remove a request header** Create a request header transform rule (part of Transform Rules) to remove the `cf-connecting-ip` HTTP header from the request.](https://developers.cloudflare.com/rules/transform/examples/remove-request-header/)

[**Remove a response header** Create a response header transform rule (part of Transform Rules) to remove the `cf-connecting-ip` HTTP header from the response.](https://developers.cloudflare.com/rules/transform/examples/remove-response-header/)

[**Rewrite blog archive URLs** Create a transform rule to rewrite the URL format `/posts/<YYYY>-<MM>-<DD>-<TITLE>` to the new format `/posts/<YYYY>/<MM>/<DD>/<TITLE>`.](https://developers.cloudflare.com/rules/transform/examples/rewrite-archive-urls-new-format/)

[**Rewrite path of moved section of a website** Create a URL rewrite rule (part of Transform Rules) to rewrite everything under `/blog/<PATH>` to `/marketing/<PATH>`.](https://developers.cloudflare.com/rules/transform/examples/rewrite-moved-section/)

[**Rewrite path of archived blog posts** Create a URL rewrite rule (part of Transform Rules) to rewrite any requests for `/news/2012/...` URI paths to `/archive/news/2012/...`.](https://developers.cloudflare.com/rules/transform/examples/rewrite-path-archived-posts/)

[**Rewrite path for object storage bucket** Create a URL rewrite rule (part of Transform Rules) to rewrite any requests for `/files/...` URI paths to `/...`.](https://developers.cloudflare.com/rules/transform/examples/rewrite-path-object-storage/)

[**Rewrite image paths with several URL segments** Create a URL rewrite rule (part of Transform Rules) to rewrite any requests for `/images/<FOLDER1>/<FOLDER2>/<FILENAME>` to `/img/<FILENAME>`.](https://developers.cloudflare.com/rules/transform/examples/rewrite-several-url-different-url/)

[**Rewrite URL query string** Create a transform rule to rewrite the request path from `/blog` to `/blog?sort-by=date`.](https://developers.cloudflare.com/rules/transform/examples/rewrite-url-string-visitors/)

[**Rewrite page path for visitors in specific countries** Create two URL rewrite rules (part of Transform Rules) to rewrite the path of the welcome page for visitors in specific countries.](https://developers.cloudflare.com/rules/transform/examples/rewrite-welcome-for-countries/)

[**Set a response header with the current bot score** Create a response header transform rule (part of Transform Rules) to set an `X-Bot-Score` HTTP header in the response with the current bot score.](https://developers.cloudflare.com/rules/transform/examples/set-response-header-bot-score/)

[**Set response header with a static value** Create a response header transform rule (part of Transform Rules) to set an `X-Bot-Score` HTTP header in the response to a static value (`Cloudflare`).](https://developers.cloudflare.com/rules/transform/examples/set-response-header-static-value/)

[PreviousTroubleshooting](https://developers.cloudflare.com/rules/transform/troubleshooting/)[NextAdd a request header for subrequests from other zones](https://developers.cloudflare.com/rules/transform/examples/add-request-header-subrequest-other-zone/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/transform/examples/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
