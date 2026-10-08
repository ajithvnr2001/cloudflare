---
url: https://developers.cloudflare.com/images/examples/watermark-from-kv/
title: Watermarks \u00b7 Cloudflare Images docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:33.819054+00:00
---

# Watermarks · Cloudflare Images docs

> Source: https://developers.cloudflare.com/images/examples/watermark-from-kv/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Images](https://developers.cloudflare.com/images/)
  3. /[Examples](https://developers.cloudflare.com/images/examples/)
  4. /Watermark From Kv



# Watermarks

Draw a watermark from KV on an image from R2

Last updated Jul 8, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/images/examples/watermark-from-kv/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Enable [Workers Cache](https://developers.cloudflare.com/workers/cache/) so repeat requests for the same watermarked image are served from cache without re-running the Worker or re-transforming the image:
    
    
    {
    	"cache": {
    		"enabled": true,
    	},
    }
    
    
    [cache]
    enabled = true

Then set `Cache-Control` headers on your response to control the cache lifetime:
    
    
    export default {
    	async fetch(request, env) {
    		const watermarkKey = "my-watermark";
    		const sourceKey = "my-source-image";
    
    		const watermark = await env.NAMESPACE.get(watermarkKey, "stream");
    		const source = await env.BUCKET.get(sourceKey);
    
    		if (!watermark || !source) {
    			return new Response("Not found", { status: 404 });
    		}
    
    		const result = await env.IMAGES.input(source.body)
    			.draw(watermark)
    			.output({ format: "image/jpeg" });
    
    		const response = result.response();
    
    		return new Response(response.body, {
    			headers: {
    				...Object.fromEntries(response.headers),
    				"Cache-Control": "public, max-age=3600, stale-while-revalidate=86400",
    			},
    		});
    	},
    };
    
    
    interface Env {
    	BUCKET: R2Bucket;
    	NAMESPACE: KVNamespace;
    	IMAGES: ImagesBinding;
    }
    export default {
    	async fetch(request, env): Promise<Response> {
    		const watermarkKey = "my-watermark";
    		const sourceKey = "my-source-image";
    
    		const watermark = await env.NAMESPACE.get(watermarkKey, "stream");
    		const source = await env.BUCKET.get(sourceKey);
    
    		if (!watermark || !source) {
    			return new Response("Not found", { status: 404 });
    		}
    
    		const result = await env.IMAGES.input(source.body)
    			.draw(watermark)
    			.output({ format: "image/jpeg" });
    
    		const response = result.response();
    
    		return new Response(response.body, {
    			headers: {
    				...Object.fromEntries(response.headers),
    				"Cache-Control": "public, max-age=3600, stale-while-revalidate=86400",
    			},
    		});
    	},
    } satisfies ExportedHandler<Env>;

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/images/examples/watermark-from-kv.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
