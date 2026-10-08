---
url: https://developers.cloudflare.com/images/tutorials/optimize-mobile-viewing/
title: Optimize mobile viewing \u00b7 Cloudflare Images docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:38.072975+00:00
---

# Optimize mobile viewing · Cloudflare Images docs

> Source: https://developers.cloudflare.com/images/tutorials/optimize-mobile-viewing/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Images](https://developers.cloudflare.com/images/)
  3. /Tutorials
  4. /Optimize mobile viewing



# Optimize mobile viewing

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/images/tutorials/optimize-mobile-viewing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewModify your loading attribute Lazy loading Eager loading

You can use lazy loading to optimize the images on your webpages for mobile viewing. This helps address common challenges of mobile viewing, like slow network connections or weak processing capabilities.

Lazy loading has two main advantages:

  * **Faster page load times** — Images are loaded as the user scrolls down the page, instead of all at once when the page is opened.
  * **Lower costs for image delivery** — When using Cloudflare Images, you only pay to load images that the user actually sees. With lazy loading, images that are not scrolled into view do not count toward your billable Images requests.



Lazy loading is natively supported on all major browsers, including Chrome, Safari, Firefox, Opera, and Edge.

Note

If you use older methods, involving custom JavaScript or a JavaScript library, lazy loading may increase the initial load time of the page since the browser needs to download, parse, and execute JavaScript.

## Modify your loading attribute

Without modifying your loading attribute, most browsers will fetch all images on a page, prioritizing the images that are closest to the viewport by default. You can override this by modifying your `loading` attribute.

There are two possible `loading` attributes for your `<img>` tags: `lazy` and `eager`.

### Lazy loading

Lazy loading is recommended for most images. With Lazy loading, resources like images are deferred until they reach a certain distance from the viewport. If an image does not reach the threshold, then it does not get loaded.

Example of modifying the `loading` attribute of your `<img>` tags to be `"lazy"`:
    
    
    <img src="example.com/cdn-cgi/width=300/image.png" loading="lazy" />

### Eager loading

If you have images that are in the viewport, eager loading, instead of lazy loading, is recommended. Eager loading loads the asset at the initial page load, regardless of its location on the page.

Example of modifying the `loading` attribute of your `<img>` tags to be `"eager"`:
    
    
    <img src="example.com/cdn-cgi/width=300/image.png" loading="eager" />

[PreviousSecurity](https://developers.cloudflare.com/images/reference/security/)[NextTransform user-uploaded images before uploading to R2](https://developers.cloudflare.com/images/tutorials/optimize-user-uploaded-image/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/images/tutorials/optimize-mobile-viewing.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
