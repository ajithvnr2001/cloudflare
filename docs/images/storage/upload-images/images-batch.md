---
url: https://developers.cloudflare.com/images/storage/upload-images/images-batch/
title: Upload via batch API \u00b7 Cloudflare Images docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:37.690388+00:00
---

# Upload via batch API · Cloudflare Images docs

> Source: https://developers.cloudflare.com/images/storage/upload-images/images-batch/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Images](https://developers.cloudflare.com/images/)
  3. /…

Storage

  4. /Upload images
  5. /Upload via batch API



# Upload via batch API

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/images/storage/upload-images/images-batch/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The Images batch API lets you make several requests in sequence while bypassing Cloudflare’s global API rate limits.

To use the Images batch API, you will need to obtain a batch token and use the token to make several requests. The requests authorized by this batch token are made to a separate endpoint and do not count toward the global API rate limits. Each token is subject to a rate limit of 200 requests per second. You can use multiple tokens if you require higher throughput to the Cloudflare Images API.

To obtain a token, you can use the new `images/v1/batch_token` endpoint as shown in the example below.
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/{account_id}/images/v1/batch_token" \
    --header "Authorization: Bearer <API_TOKEN>"
    
    # Response:
    {
      "result": {
        "token": "<BATCH_TOKEN>",
        "expiresAt": "2023-08-09T15:33:56.273411222Z"
      },
      "success": true,
      "errors": [],
      "messages": []
    }

After getting your token, use it to make requests for:

  * [Upload an image](https://developers.cloudflare.com/api/resources/images/subresources/v1/methods/create/) \- `POST /images/v1`
  * [Delete an image](https://developers.cloudflare.com/api/resources/images/subresources/v1/methods/delete/) \- `DELETE /images/v1/{identifier}`
  * [Image details](https://developers.cloudflare.com/api/resources/images/subresources/v1/methods/get/) \- `GET /images/v1/{identifier}`
  * [Update image](https://developers.cloudflare.com/api/resources/images/subresources/v1/methods/edit/) \- `PATCH /images/v1/{identifier}`
  * [List images V2](https://developers.cloudflare.com/api/resources/images/subresources/v2/methods/list/) \- `GET /images/v2`
  * [Direct upload V2](https://developers.cloudflare.com/api/resources/images/subresources/v2/subresources/direct_uploads/methods/create/) \- `POST /images/v2/direct_upload`



These options use a different host and a different path with the same method, request, and response bodies.

Request for list images V2 against api.cloudflare.combash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/{account_id}/images/v2" \
    --header "Authorization: Bearer <API_TOKEN>"

Example request using a batch tokenbash
    
    
    curl "https://batch.imagedelivery.net/images/v1" \
    --header "Authorization: Bearer <BATCH_TOKEN>"

[PreviousAccept user-uploaded images](https://developers.cloudflare.com/images/storage/upload-images/direct-creator-upload/)[NextOverview](https://developers.cloudflare.com/images/storage/upload-images/import-from-s3/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/images/storage/upload-images/images-batch.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
