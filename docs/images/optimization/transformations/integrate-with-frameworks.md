---
url: https://developers.cloudflare.com/images/optimization/transformations/integrate-with-frameworks/
title: Integrate with frameworks \u00b7 Cloudflare Images docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:35.695477+00:00
---

# Integrate with frameworks · Cloudflare Images docs

> Source: https://developers.cloudflare.com/images/optimization/transformations/integrate-with-frameworks/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Images](https://developers.cloudflare.com/images/)
  3. /…

Optimization

  4. /Remote images (transformations)
  5. /Integrate with frameworks



# Integrate with frameworks

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/images/optimization/transformations/integrate-with-frameworks/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewNext.js Global Loader Custom Loaders

## Next.js

Image transformations can be used automatically with the Next.js [`<Image />` component ↗︎](https://nextjs.org/docs/api-reference/next/image).

To use image transformations, define a global image loader or multiple custom loaders for each `<Image />` component.

Next.js will request the image with the correct parameters for width and quality.

Image transformations will be responsible for caching and serving an optimal format to the client.

### Global Loader

To use Images with **all** your app's images, define a global [loaderFile ↗︎](https://nextjs.org/docs/pages/api-reference/components/image#loaderfile) for your app.

Add the following settings to the **next.config.js** file located at the root of your Next.js application.
    
    
    module.exports = {
    	images: {
    		loader: "custom",
    		loaderFile: "./imageLoader.ts",
    	},
    };

Next, create the `imageLoader.ts` file in the specified path (relative to the root of your Next.js application).
    
    
    import type { ImageLoaderProps } from "next/image";
    
    const normalizeSrc = (src: string) => {
    	return src.startsWith("/") ? src.slice(1) : src;
    };
    
    export default function cloudflareLoader({
    	src,
    	width,
    	quality,
    }: ImageLoaderProps) {
    	const params = [`width=${width}`];
    	if (quality) {
    		params.push(`quality=${quality}`);
    	}
    	if (process.env.NODE_ENV === "development") {
    		return `${src}?${params.join("&")}`;
    	}
    	return `/cdn-cgi/image/${params.join(",")}/${normalizeSrc(src)}`;
    }

### Custom Loaders

Alternatively, define a loader for each `<Image />` component.
    
    
    import Image from "next/image";
    
    const normalizeSrc = (src) => {
    	return src.startsWith("/") ? src.slice(1) : src;
    };
    
    const cloudflareLoader = ({ src, width, quality }) => {
    	const params = [`width=${width}`];
    	if (quality) {
    		params.push(`quality=${quality}`);
    	}
    	if (process.env.NODE_ENV === "development") {
    		return `${src}?${params.join("&")}`;
    	}
    	return `/cdn-cgi/image/${params.join(",")}/${normalizeSrc(src)}`;
    };
    
    const MyImage = (props) => {
    	return (
    		<Image
    			loader={cloudflareLoader}
    			src="/me.png"
    			alt="Picture of the author"
    			width={500}
    			height={500}
    			{...props}
    		/>
    	);
    };

Note

For local development, you can enable [Resize images from any origin checkbox](https://developers.cloudflare.com/images/optimization/transformations/sources/) for your zone. Then, replace `/cdn-cgi/image/${paramsString}/${normalizeSrc(src)}` with an absolute URL path:

`https://<YOUR_DOMAIN.COM>/cdn-cgi/image/${paramsString}/${normalizeSrc(src)}`

[PreviousControl origin access](https://developers.cloudflare.com/images/optimization/transformations/control-origin-access/)[NextSet up rewrite rules](https://developers.cloudflare.com/images/optimization/transformations/rewrite-rules/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/images/optimization/transformations/integrate-with-frameworks.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
