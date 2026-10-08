---
url: https://developers.cloudflare.com/changelog/post/2026-06-10-hosted-images-binding/
title: Manage hosted images with the Images binding \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:57.393704+00:00
---

# Manage hosted images with the Images binding · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-10-hosted-images-binding/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 10, 2026

## Manage hosted images with the Images binding

[Cloudflare Images](https://developers.cloudflare.com/images/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-10-hosted-images-binding/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Use the Images binding to upload, list, retrieve, update, and delete images stored in Images directly from your Worker without managing API tokens or making HTTP requests.

The `env.IMAGES.hosted` namespace supports the following storage and management operations:

  * [`.upload(image, options)`](https://developers.cloudflare.com/images/storage/binding/#uploadimage-options) — Upload a new image to your account.
  * [`.list(options)`](https://developers.cloudflare.com/images/storage/binding/#listoptions) — List images with pagination.
  * [`.image(imageId).details()`](https://developers.cloudflare.com/images/storage/binding/#imageimageiddetails) — Get image metadata.
  * [`.image(imageId).bytes()`](https://developers.cloudflare.com/images/storage/binding/#imageimageidbytes) — Stream the original image bytes.
  * [`.image(imageId).update(options)`](https://developers.cloudflare.com/images/storage/binding/#imageimageidupdateoptions) — Update metadata or access controls.
  * [`.image(imageId).delete()`](https://developers.cloudflare.com/images/storage/binding/#imageimageiddelete) — Delete an image.



For example, you can upload an image from a request body and return its metadata:
    
    
    const image = await env.IMAGES.hosted.upload(request.body, {
    	filename: "upload.jpg",
    	metadata: { source: "worker" },
    });
    
    return Response.json(image);

Or retrieve and serve the original bytes of a hosted image:
    
    
    const bytes = await env.IMAGES.hosted.image("IMAGE_ID").bytes();
    return new Response(bytes);

For more information, refer to the [Images binding](https://developers.cloudflare.com/images/storage/binding/).
