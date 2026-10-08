---
url: https://developers.cloudflare.com/workers-ai/features/markdown-conversion/usage/rest-api/
title: REST API \u00b7 Cloudflare Workers AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:58.690086+00:00
---

# REST API · Cloudflare Workers AI docs

> Source: https://developers.cloudflare.com/workers-ai/features/markdown-conversion/usage/rest-api/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers AI](https://developers.cloudflare.com/workers-ai/)
  3. /…

Features[Markdown Conversion](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/)

  4. /Usage
  5. /REST API



# REST API

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/usage/rest-api/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisite: Get Workers AI API tokenTransform Parameters ResponseSupported Response

You can also use the Markdown Conversion REST API to convert your documents into Markdown.

## Prerequisite: Get Workers AI API token

To use the Markdown Conversion service via the REST API, you need an API token with permissions for the [Workers AI](https://developers.cloudflare.com/workers-ai/) REST API. Refer to [Get started with the Workers AI REST API](https://developers.cloudflare.com/workers-ai/get-started/rest-api/) for instructions on obtaining an API token with the correct permissions.

## Transform

This endpoint lets you convert any file given to us into markdown.
    
    
    curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/tomarkdown \
      -X POST \
      -H 'Authorization: Bearer {API_TOKEN}' \
      -F "files=@cat.jpeg" \
      -F "files=@somatosensory.pdf" \
      -F 'conversionOptions={ ... }'

Note

You can get your `ACCOUNT_ID` by going to [Workers & Pages on the dashboard](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/#find-account-id-workers-and-pages).

### Parameters

`files` `File[]` required

The files you want to convert.

`conversionOptions` `ConversionOptions` optional

Options that allow you to control how your files are converted. Refer to [Conversion Options](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/conversion-options/) for further details.

### Response
    
    
    {
    	"success": true,
    	"result": [
    		{
    			"id": "...",
    			"name": "good.html",
    			"mimeType": "text/html",
    			"format": "markdown",
    			"tokens": 49,
    			"data": "# Image Embedded with a Data URI\n\nThis _image_ is directly encoded in the HTML:\n\n\n\nAn image description\n\n \n\nIt's a tiny 5x5 pixel PNG, scaled up to 50x50px.\n\n"
    		},
    		{
    			"id": "...",
    			"name": "bad.pdf",
    			"mimeType": "application/pdf",
    			"format": "error",
    			"error": "Some error that prevented this image from being converted"
    		}
    	]
    }

## Supported

This endpoint lets you programmatically retrieve the full set of rich formats that are supported for conversion.
    
    
    curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/tomarkdown/supported \
      -H 'Authorization: Bearer {API_TOKEN}'

Note

You can get your `ACCOUNT_ID` by going to [Workers & Pages on the dashboard](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/#find-account-id-workers-and-pages).

### Response
    
    
    {
      "success": true,
      "result": [
        {
          "extension": ".html",
          "mimeType": "text/html"
        },
        {
          "extension": ".pdf",
          "mimeType": "application/pdf"
        },
        ...
      ]
    }

[PreviousWorkers Binding](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/usage/binding/)[NextSupported Formats](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/supported-formats/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers-ai/features/markdown-conversion/usage/rest-api.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
