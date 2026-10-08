---
url: https://www.cloudflare.com/products/stream/
title: Cloudflare Stream - All-in-one Video Platform
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:03:17.066884+00:00
---

# Cloudflare Stream - All-in-one Video Platform

> Source: https://www.cloudflare.com/products/stream/

Stream 

## All-in-one managed media pipeline for live and on-demand video

### Stream makes storing, encoding, and distributing video effortless — eliminating the need for complex infrastructure, multiple vendors, or opaque pricing models.

[ Start building for free ](https://dash.cloudflare.com/sign-up) [ View docs ](https://developers.cloudflare.com/stream/)

**Unified Media Pipeline**

Upload, encode, package, and stream video from a single API — no stitching together services or vendors.

**Simple, Predictable Pricing**

Avoid convoluted billing models with clear, cost-effective rates that scale with you.

**Built on Cloudflare's Network**

Delivers video globally with lower bandwidth costs, faster access, and higher reliability.

### Fast, global, unified

Stream provides a complete media pipeline from upload to delivery. Upload videos via API or direct upload, automatically encode to multiple formats and bitrates, then deliver through Cloudflare's global network. Built-in player or integrate with your own — all managed through a single, unified API. With RTMP/SRT ingest for live streaming and HLS/DASH output for compatibility, Stream handles both real-time and on-demand content seamlessly.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

`Stream`

####  Perfect for modern video workflows 

You can use Stream to: 

[ View docs  ](https://developers.cloudflare.com/stream/)

E-learning and user-generated content 

Perfect for educational platforms, journalism, worship services, and sports broadcasting with reliable delivery and flexible player options.

AI-generated media workflows 

Integrate with Stream or Media Transformations + R2 for AI-generated video content with automatic optimization and global delivery.

Live streaming events 

Broadcast live events with RTMP/SRT ingest and HLS/DASH output, reaching audiences worldwide with minimal latency.

Multi-platform video distribution 

Transform videos for different platforms with resizing, cropping, and repackaging — adapt content for social media, mobile, and web.

### Cloudflare Stream delivers video at global scale with unified media pipeline

Transform, encode, and deliver video worldwide with a single API. Stream handles upload, encoding, delivery, and playback — letting you focus on creating great content instead of managing complex video infrastructure.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

upload.ts  live.ts 

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33 
    
    
    export default {  async fetch(request, env, ctx): Promise<Response> {    // Upload a video file    const formData = new FormData();    formData.append('file', videoFile);
        const uploadResponse = await fetch(      'https://api.cloudflare.com/client/v4/accounts/{account_id}/stream',      {        method: 'POST',        headers: {          Authorization: 'Bearer ' + env.CLOUDFLARE_API_TOKEN,        },        body: formData,      },    );
        const uploadResult = await uploadResponse.json();    const videoId = uploadResult.result.uid;
        // Get video details    const videoResponse = await fetch(      'https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/' +        videoId,      {        headers: {          Authorization: 'Bearer ' + env.CLOUDFLARE_API_TOKEN,        },      },    );
        const videoData = await videoResponse.json();
        return new Response(      JSON.stringify({        videoId: videoId,        playbackUrl: videoData.result.playback.hls,        thumbnailUrl: videoData.result.thumbnail,      }),    );  },};

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38 
    
    
    export default {  async fetch(request, env) {    // Create a live stream    const streamResponse = await fetch(      'https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/live_inputs',      {        method: 'POST',        headers: {          Authorization: 'Bearer ' + env.CLOUDFLARE_API_TOKEN,          'Content-Type': 'application/json',        },        body: JSON.stringify({          meta: {            name: 'Live Event Stream',          },          recording: {            mode: 'automatic',            requireSignedURLs: false,          },        }),      },    );
        const streamData = await streamResponse.json();    const streamId = streamData.result.uid;
        // Get RTMP ingest URL    const rtmpUrl = streamData.result.rtmps.url;
        // Get HLS playback URL    const playbackUrl =      'https://customer-' +      env.CUSTOMER_CODE +      '.cloudflarestream.com/' +      streamId +      '/manifest/video.m3u8';
        return new Response(      JSON.stringify({        streamId: streamId,        rtmpIngestUrl: rtmpUrl,        hlsPlaybackUrl: playbackUrl,      }),      {        headers: { 'content-type': 'application/json' },      },    );  },} satisfies ExportedHandler;

Upload and encode video 

Upload videos and get playback URLs with automatic encoding and delivery.

Live Streaming with RTMP Ingest 

Set up live streaming with RTMP ingest and automatic HLS/DASH output. This example shows how to create a live stream and get the playback URL for real-time broadcasting.

Hypixel 

#### "

####  Video is incredibly important to us and our community. Cloudflare Stream makes it easy for us to show off our game and distribute videos without having to build our own streaming solution from scratch. " 

Director of IT 

###  Stream Pricing 

Video hosting and live streaming. [View Media pricing details](https://www.cloudflare.com/plans/#developer-platform/media)

Component

Free

Paid

Minutes Stored 

Free

—

Paid

$5.00 / thousand minutes 

Minutes Delivered 

Free

—

Paid

$1.00 / thousand minutes 

###  Powerful primitives, seamlessly integrated 

#####  Built on systems powering 20% of the Internet, Stream runs on the same infrastructure Cloudflare uses to build Cloudflare. Enterprise-grade reliability, security, and performance are standard. 

[ Compute ](https://www.cloudflare.com/products/#compute)

[ Browser Run  Automated browsers  ](https://www.cloudflare.com/products/browser-run/)

[ Containers  Any language, anywhere  ](https://www.cloudflare.com/products/containers/)

[ Durable Objects  Stateful compute  ](https://www.cloudflare.com/products/durable-objects/)

[ Sandboxes  Secure code execution  ](https://www.cloudflare.com/products/sandboxes/)

[ Workers  Global serverless functions  ](https://www.cloudflare.com/products/workers/)

[ Workers for Platforms  Programmable Platform Solutions  ](https://www.cloudflare.com/products/workers-for-platforms/)

[ Workflows  Process orchestration  ](https://www.cloudflare.com/products/workflows/)

[ Storage ](https://www.cloudflare.com/products/#storage)

[ Artifacts  Git-native versioned storage  ](https://www.cloudflare.com/products/artifacts/)

[ D1  Serverless SQL  ](https://www.cloudflare.com/products/d1/)

[ Basin  Ingest, catalog & query data  ](https://www.cloudflare.com/products/data-platform/)

[ Hyperdrive  Global databases  ](https://www.cloudflare.com/products/hyperdrive/)

[ K2  Publish and subscribe to durable, ordered event streams  ](https://www.cloudflare.com/products/k2/)

[ Queues  Message processing  ](https://www.cloudflare.com/products/queues/)

[ R2  Egress-free storage  ](https://www.cloudflare.com/products/r2/)

[ KV  Ultra-fast key-value storage  ](https://www.cloudflare.com/products/kv/)

[ AI ](https://www.cloudflare.com/products/#ai)

[ Agents  Build stateful AI agents  ](https://www.cloudflare.com/products/agents/)

[ AI Gateway  AI observability  ](https://www.cloudflare.com/products/ai-gateway/)

[ AI Search  Instant retrieval  ](https://www.cloudflare.com/products/ai-search/)

[ Vectorize  Vector database  ](https://www.cloudflare.com/products/vectorize/)

[ Workers AI  Edge AI models  ](https://www.cloudflare.com/products/workers-ai/)

[ SASE / Zero Trust ](https://www.cloudflare.com/products/#sase)

[ SASE  Cloudflare SASE platform  ](https://www.cloudflare.com/sase/)

[ Access  Zero trust access to private resources  ](https://www.cloudflare.com/products/access/)

[ CASB  SaaS and cloud posture  ](https://www.cloudflare.com/products/casb/)

[ Data Loss Prevention  Protect sensitive data  ](https://www.cloudflare.com/products/dlp/)

[ Gateway  Web filtering  ](https://www.cloudflare.com/products/gateway/)

[ Browser Isolation  Secure web browsing  ](https://www.cloudflare.com/products/browser-isolation/)

[ WAN  Cloud-delivered networking  ](https://www.cloudflare.com/products/wan/)

[ Email Security  Phishing protection  ](https://www.cloudflare.com/products/email-security/)

[ Security ](https://www.cloudflare.com/products/#security)

[ DDoS Protection  Mitigation Solutions  ](https://www.cloudflare.com/products/ddos/)

[ Rate Limiting  Abuse prevention  ](https://www.cloudflare.com/products/rate-limiting/)

[ SSL  Secure Your Site with SSL  ](https://www.cloudflare.com/products/ssl/)

[ Turnstile  A CAPTCHA Replacement Solution  ](https://www.cloudflare.com/products/turnstile/)

[ WAF  Web Application Firewall  ](https://www.cloudflare.com/products/waf/)

[ Magic Transit  DDoS Protection for Networks  ](https://www.cloudflare.com/products/magic-transit/)

[ Client-Side Security  Prevent browser supply chain attacks  ](https://www.cloudflare.com/products/client-side-security/)

[ Bot Management  Block bad bots  ](https://www.cloudflare.com/products/bot-management/)

[ Network & Content Delivery ](https://www.cloudflare.com/products/#network)

[ CDN  Faster delivery & caching  ](https://www.cloudflare.com/products/cdn/)

[ DNS  Fast DNS  ](https://www.cloudflare.com/products/dns/)

[ Load Balancing  Zero downtime  ](https://www.cloudflare.com/products/load-balancing/)

[ TURN / SFU  Real-time infra  ](https://www.cloudflare.com/products/turn-sfu/)

[ Analytics  Web Performance & Security  ](https://www.cloudflare.com/products/analytics/)

# Build without boundaries

Join thousands of developers who've eliminated infrastructure complexity and deployed globally with Cloudflare. Start building for free — no credit card required. 

[ Start building for free  ](https://dash.cloudflare.com/sign-up)[ View docs  ](https://developers.cloudflare.com/)

No cold starts or region complexity  SASE and Zero Trust without the complexity  Deploy to 330+ cities instantly  Defend against the Internet's biggest DDoS attacks  Predictable pricing without surprises  Identity-aware Zero Trust access that retires your VPN  Battle-tested infrastructure powering millions  CDN, WAF, and DNS faster than the public Internet  No cold starts or region complexity  SASE and Zero Trust without the complexity  Deploy to 330+ cities instantly  Defend against the Internet's biggest DDoS attacks  Predictable pricing without surprises  Identity-aware Zero Trust access that retires your VPN  Battle-tested infrastructure powering millions  CDN, WAF, and DNS faster than the public Internet 
