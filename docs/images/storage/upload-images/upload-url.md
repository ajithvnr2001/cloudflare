---
url: https://developers.cloudflare.com/images/storage/upload-images/upload-url/
title: Upload via URL \u00b7 Cloudflare Images docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:58.722953+00:00
---

# Upload via URL · Cloudflare Images docs

> Source: https://developers.cloudflare.com/images/storage/upload-images/upload-url/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Images](https://developers.cloudflare.com/images/)
  3. /…

Storage

  4. /Upload images
  5. /Upload via URL



# Upload via URL

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Before you upload an image, check the list of [supported formats and dimensions](https://developers.cloudflare.com/images/get-started/limits) to confirm your image will be accepted.

You can use the Images API to use a URL of an image instead of uploading the data.

Make a `POST` request using the example below as reference. Keep in mind that the `--form 'file=<FILE>'` and `--form 'url=<URL>'` fields are mutually exclusive.

Note

The `metadata` included in the request is never shared with end-users.
    
    
    curl --request POST \
    https://api.cloudflare.com/client/v4/accounts/{account_id}/images/v1 \
    --header "Authorization: Bearer <API_TOKEN>" \
    --form 'url=https://[user:password@]example.com/<PATH_TO_IMAGE>' \
    --form 'metadata={"key":"value"}' \
    --form 'requireSignedURLs=false'

After successfully uploading the image, you will receive a response similar to the example below.
    
    
    {
    	"result": {
    		"id": "2cdc28f0-017a-49c4-9ed7-87056c83901",
    		"filename": "image.jpeg",
    		"metadata": {
    			"key": "value"
    		},
    		"uploaded": "2022-01-31T16:39:28.458Z",
    		"requireSignedURLs": false,
    		"variants": [
    			"https://imagedelivery.net/Vi7wi5KSItxGFsWRG2Us6Q/2cdc28f0-017a-49c4-9ed7-87056c83901/public",
    			"https://imagedelivery.net/Vi7wi5KSItxGFsWRG2Us6Q/2cdc28f0-017a-49c4-9ed7-87056c83901/thumbnail"
    		]
    	},
    	"success": true,
    	"errors": [],
    	"messages": []
    }

If your origin server returns an error while fetching the images, the API response will return a 4xx error.

[PreviousMethods](https://developers.cloudflare.com/images/storage/upload-images/methods/)[NextUpload via custom path](https://developers.cloudflare.com/images/storage/upload-images/upload-custom-path/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/images/storage/upload-images/upload-URL.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
