---
url: https://developers.cloudflare.com/images/examples/transcode-from-workers-ai/
title: Transcode images \u00b7 Cloudflare Images docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:33.698049+00:00
---

# Transcode images · Cloudflare Images docs

> Source: https://developers.cloudflare.com/images/examples/transcode-from-workers-ai/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Images](https://developers.cloudflare.com/images/)
  3. /[Examples](https://developers.cloudflare.com/images/examples/)
  4. /Transcode From Workers Ai



# Transcode images

Transcode an image from Workers AI before uploading to R2

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/images/examples/transcode-from-workers-ai/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)
    
    
    const stream = await env.AI.run("@cf/bytedance/stable-diffusion-xl-lightning", {
    	prompt: YOUR_PROMPT_HERE,
    });
    
    // Convert to AVIF
    const image = (
    	await env.IMAGES.input(stream).output({ format: "image/avif" })
    ).response();
    
    const fileName = "image.avif";
    
    // Upload to R2
    await env.R2.put(fileName, image.body);

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/images/examples/transcode-from-workers-ai.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
