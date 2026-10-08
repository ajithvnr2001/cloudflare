---
url: https://developers.cloudflare.com/images/storage/upload-images/upload-file-worker/
title: Upload via a Worker \u00b7 Cloudflare Images docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:37.946746+00:00
---

# Upload via a Worker · Cloudflare Images docs

> Source: https://developers.cloudflare.com/images/storage/upload-images/upload-file-worker/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Images](https://developers.cloudflare.com/images/)
  3. /…

Storage

  4. /Upload images
  5. /Upload via a Worker



# Upload via a Worker

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/images/storage/upload-images/upload-file-worker/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUpload from AI generated images

You can use a Worker to upload your image to Cloudflare Images.

Refer to the example below or refer to the [Workers documentation](https://developers.cloudflare.com/workers/) for more information.
    
    
    const API_URL =
    	"https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/images/v1";
    const TOKEN = "<YOUR_TOKEN_HERE>";
    
    const image = await fetch("https://example.com/image.png");
    const bytes = await image.bytes();
    
    const formData = new FormData();
    formData.append("file", new File([bytes], "image.png"));
    
    const response = await fetch(API_URL, {
    	method: "POST",
    	headers: {
    		Authorization: `Bearer ${TOKEN}`,
    	},
    	body: formData,
    });
    
    
    const API_URL =
    	"https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/images/v1";
    const TOKEN = "<YOUR_TOKEN_HERE>";
    
    const image = await fetch("https://example.com/image.png");
    const bytes = await image.bytes();
    
    const formData = new FormData();
    formData.append("file", new File([bytes], "image.png"));
    
    const response = await fetch(API_URL, {
    	method: "POST",
    	headers: {
    		Authorization: `Bearer ${TOKEN}`,
    	},
    	body: formData,
    });

## Upload from AI generated images

You can use an AI Worker to generate an image and then upload that image to store it in Cloudflare Images. For more information about using Workers AI to generate an image, refer to the [SDXL-Lightning Model](https://developers.cloudflare.com/workers-ai/models/stable-diffusion-xl-lightning).
    
    
    const API_URL =
    	"https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/images/v1";
    const TOKEN = "YOUR_TOKEN_HERE";
    
    const stream = await env.AI.run("@cf/bytedance/stable-diffusion-xl-lightning", {
    	prompt: YOUR_PROMPT_HERE,
    });
    const bytes = await new Response(stream).bytes();
    
    const formData = new FormData();
    formData.append("file", new File([bytes], "image.jpg"));
    
    const response = await fetch(API_URL, {
    	method: "POST",
    	headers: {
    		Authorization: `Bearer ${TOKEN}`,
    	},
    	body: formData,
    });
    
    
    const API_URL =
    	"https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/images/v1";
    const TOKEN = "YOUR_TOKEN_HERE";
    
    const stream = await env.AI.run("@cf/bytedance/stable-diffusion-xl-lightning", {
    	prompt: YOUR_PROMPT_HERE,
    });
    const bytes = await new Response(stream).bytes();
    
    const formData = new FormData();
    formData.append("file", new File([bytes], "image.jpg"));
    
    const response = await fetch(API_URL, {
    	method: "POST",
    	headers: {
    		Authorization: `Bearer ${TOKEN}`,
    	},
    	body: formData,
    });

[PreviousCredentials](https://developers.cloudflare.com/images/storage/upload-images/import-from-s3/credentials/)[NextConfigure webhooks](https://developers.cloudflare.com/images/storage/upload-images/configure-webhooks/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/images/storage/upload-images/upload-file-worker.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
