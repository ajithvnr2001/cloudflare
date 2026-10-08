---
url: https://developers.cloudflare.com/pages/configuration/early-hints/
title: Early Hints \u00b7 Cloudflare Pages docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:28.788139+00:00
---

# Early Hints · Cloudflare Pages docs

> Source: https://developers.cloudflare.com/pages/configuration/early-hints/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Pages](https://developers.cloudflare.com/pages/)
  3. /Configuration
  4. /Early Hints



# Early Hints

Last updated Sep 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/pages/configuration/early-hints/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigure Early Hints 1\. Configure your _headers file 2\. Automatic Link header generation Disable automatic Link header generation Automatic Link headerEarly Hints probes in logs Filter probes from logs Reduce probe cache misses Disable Early Hints on Pages

[Early Hints](https://developers.cloudflare.com/cache/advanced-configuration/early-hints/) help the browser to load webpages faster. Early Hints is enabled automatically on all `pages.dev` domains and custom domains.

Early Hints automatically caches any [`preload` ↗︎](https://developer.mozilla.org/en-US/docs/Web/HTML/Link_types/preload) and [`preconnect` ↗︎](https://developer.mozilla.org/en-US/docs/Web/HTML/Link_types/preconnect) type [`Link` headers ↗︎](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Link) to send as Early Hints to the browser. The hints are sent to the browser before the full response is prepared, and the browser can figure out how to load the webpage faster for the end user. There are two ways to create these `Link` headers in Pages:

## Configure Early Hints

Early Hints can be created with either of the two methods detailed below.

### 1\. Configure your `_headers` file

Create custom headers using the [`_headers` file](https://developers.cloudflare.com/pages/configuration/headers/). If you include a particular stylesheet on your `/blog/` section of your website, you would create the following rule:
    
    
    /blog/*
      Link: </styles.css>; rel=preload; as=style

Pages will attach this `Link: </styles.css>; rel=preload; as=style` header. Early Hints will then emit this header as an Early Hint once cached.

### 2\. Automatic `Link` header generation

In order to make the authoring experience easier, Pages also automatically generates `Link` headers from any `<link>` HTML elements with the following attributes:

  * `href`
  * `as` (optional)
  * `rel` (one of `preconnect`, `preload`, or `modulepreload`)



`<link>` elements which contain any other additional attributes (for example, `fetchpriority`, `crossorigin` or `data-do-not-generate-a-link-header`) will not be used to generate `Link` headers in order to prevent accidentally losing any custom prioritization logic that would otherwise be dropped as an Early Hint.

This allows you to directly create Early Hints as you are writing your document, without needing to alternate between your HTML and `_headers` file.
    
    
    <html>
    	<head>
    		<link rel="preload" href="/style.css" as="style" />
    		<link rel="stylesheet" href="/style.css" />
    	</head>
    </html>

### Disable automatic `Link` header generation Automatic `Link` header

Remove any automatically generated `Link` headers by adding the following to your `_headers` file:
    
    
    /*
      ! Link

Caution

Automatic `Link` header generation should not have any negative performance impact on your website. If you need to disable this feature, contact us by letting us know about your circumstance in our [Discord server ↗︎](https://discord.com/invite/cloudflaredev).

## Early Hints probes in logs

Cloudflare automatically runs Early Hints probe requests on all Pages domains, including custom domains. These probes appear in your Cloudflare logs with `ClientRequestSource: earlyHintsCache` and a `ClientRequestUserAgent` of `nginx-ssl early hints` or `bastion early hints`.

A `504` response on a probe means no Early Hint has been cached for that URL yet (a cache miss). A `200` means a cached Early Hint was served. These probes are internal Cloudflare subrequests — they do not reach your Pages project or origin server and have no impact on end users.

Note

Early Hints is always enabled for Cloudflare Pages. The zone-level Early Hints setting does not apply to Pages domains or custom domains.

### Filter probes from logs

To exclude Early Hints probes from Log Explorer queries or alert rules, filter on `ClientRequestSource != "earlyHintsCache"`.

### Reduce probe cache misses

Probes return `504` when Cloudflare has no `Link` headers cached for a URL. To convert cache misses to hits and reduce `504` volume in your logs, configure `Link` headers in your Pages project using either the [`_headers` file](https://developers.cloudflare.com/pages/configuration/headers/) or automatic `Link` header generation from HTML elements.

### Disable Early Hints on Pages

Early Hints cannot be disabled for Cloudflare Pages. If you need full control over the Early Hints setting, [migrate your project from Pages to Workers](https://developers.cloudflare.com/workers/static-assets/migration-guides/migrate-from-pages/). Workers respects the zone-level Early Hints setting.

[PreviousDeploy Hooks](https://developers.cloudflare.com/pages/configuration/deploy-hooks/)[NextOverview](https://developers.cloudflare.com/pages/configuration/git-integration/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/pages/configuration/early-hints.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
