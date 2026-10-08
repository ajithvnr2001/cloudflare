---
url: https://developers.cloudflare.com/ai-search/configuration/data-source/website/custom-metadata/
title: Custom metadata \u00b7 Cloudflare AI Search docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:39.120437+00:00
---

# Custom metadata · Cloudflare AI Search docs

> Source: https://developers.cloudflare.com/ai-search/configuration/data-source/website/custom-metadata/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Search](https://developers.cloudflare.com/ai-search/)
  3. /…

[Configuration](https://developers.cloudflare.com/ai-search/configuration/)[Data source](https://developers.cloudflare.com/ai-search/configuration/data-source/)

  4. /[Website](https://developers.cloudflare.com/ai-search/configuration/data-source/website/)
  5. /Custom metadata



# Custom metadata

Last updated Aug 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-search/configuration/data-source/website/custom-metadata/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAdd metadata to web pagesRecognized fieldsHow metadata extraction worksBoolean value parsing

You can attach custom metadata to web pages using HTML `<meta>` tags. AI Search extracts metadata from the `<head>` section of each crawled page.

Before custom metadata can be extracted, you must [define a schema](https://developers.cloudflare.com/ai-search/configuration/indexing/metadata/#define-a-schema) in your AI Search configuration.

## Add metadata to web pages

Add `<meta>` tags using either the `name` or `property` attribute:
    
    
    <!DOCTYPE html>
    <html>
    	<head>
    		<meta name="title" content="Getting Started Guide" />
    		<meta name="description" content="Learn how to set up the application" />
    		<meta property="og:title" content="Getting Started Guide" />
    		<meta property="og:image" content="https://example.com/og-image.png" />
    		<meta name="category" content="documentation" />
    		<meta name="version" content="2.5" />
    		<meta name="is_public" content="true" />
    	</head>
    	<body>
    		<!-- Page content -->
    	</body>
    </html>

## Recognized fields

For the following fields, AI Search knows which meta tags to extract from. You must still define these in your schema to enable extraction.

Field | Source  
---|---  
`title` | `<meta name="title">` or `<meta property="og:title">`  
`description` | `<meta name="description">` or `<meta property="og:description">`  
`image` | `<meta property="og:image">`  
  
When both a standard meta tag and an Open Graph tag are present, the standard meta tag takes precedence.

## How metadata extraction works

When the crawler fetches a page:

  1. All `<meta>` tags with `name` or `property` attributes are parsed from the `<head>` section.
  2. Tag names are matched against your schema (case-insensitive).
  3. The `content` attribute value is cast to the configured data type.
  4. Extracted metadata is stored alongside the cached HTML.
  5. On subsequent processing, metadata flows into the vector index.



## Boolean value parsing

For `boolean` fields, the following values are accepted (case-insensitive):

True values | False values  
---|---  
`true`, `1`, `yes` | `false`, `0`, `no`  
  
Any other value is treated as invalid and the field is omitted.

[PreviousContent selectors](https://developers.cloudflare.com/ai-search/configuration/data-source/website/content-selectors/)[NextOverview](https://developers.cloudflare.com/ai-search/configuration/models/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-search/configuration/data-source/website/custom-metadata.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
