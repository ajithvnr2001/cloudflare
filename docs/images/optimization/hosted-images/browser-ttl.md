---
url: https://developers.cloudflare.com/images/optimization/hosted-images/browser-ttl/
title: Browser TTL \u00b7 Cloudflare Images docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:34.925429+00:00
---

# Browser TTL · Cloudflare Images docs

> Source: https://developers.cloudflare.com/images/optimization/hosted-images/browser-ttl/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Images](https://developers.cloudflare.com/images/)
  3. /…

Optimization

  4. /Hosted images
  5. /Browser TTL



# Browser TTL

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/images/optimization/hosted-images/browser-ttl/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview Default TTLCustom setting Browser TTL for an account Browser TTL for a named variant

Browser TTL controls how long an image stays in a browser's cache and specifically configures the `cache-control` response header.

### Default TTL

By default, an image's TTL is set to two days to meet user needs, such as re-uploading an image under the same [Custom ID](https://developers.cloudflare.com/images/storage/upload-images/upload-custom-path/).

## Custom setting

You can use two custom settings to control the Browser TTL, an account or a named variant. To adjust how long a browser should keep an image in the cache, set the TTL in seconds, similar to how the `max-age` header is set. The value should be an interval between one hour to one year.

### Browser TTL for an account

Setting the Browser TTL per account overrides the default TTL.

Examplebash
    
    
    curl --request PATCH 'https://api.cloudflare.com/client/v4/accounts/{account_id}/images/v1/config' \
    --header "Authorization: Bearer <API_TOKEN>" \
    --header "Content-Type: application/json" \
    --data '{
      "browser_ttl": 31536000
    }'

When the Browser TTL is set to one year for all images, the response for the `cache-control` header is essentially `public`, `max-age=31536000`, `stale-while-revalidate=7200`.

### Browser TTL for a named variant

Setting the Browser TTL for a named variant is a more granular option that overrides all of the above when creating or updating an image variant, specifically the `browser_ttl` option in seconds.

Examplebash
    
    
    curl 'https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_TAG>/images/v1/variants' \
    --header "Authorization: Bearer <API_TOKEN>" \
    --header "Content-Type: application/json" \
    --data '{
      "id":"avatar",
      "options": {
        "width":100,
        "browser_ttl": 86400
      }
    }'

When the Browser TTL is set to one day for images requested with this variant, the response for the `cache-control` header is essentially `public`, `max-age=86400`, `stale-while-revalidate=7200`.

Note

[Private images](https://developers.cloudflare.com/images/optimization/hosted-images/serve-private-images/) do not respect default or custom TTL settings. The private images cache time is set according to the expiration time and can be as short as one hour.

[PreviousPreserve Content Credentials](https://developers.cloudflare.com/images/optimization/hosted-images/preserve-content-credentials/)[NextServe images from custom domains](https://developers.cloudflare.com/images/optimization/hosted-images/serve-from-custom-domains/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/images/optimization/hosted-images/browser-ttl.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
