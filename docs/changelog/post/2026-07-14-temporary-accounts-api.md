---
url: https://developers.cloudflare.com/changelog/post/2026-07-14-temporary-accounts-api/
title: Platforms can now create Temporary Accounts via the Cloudflare API \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:34.930948+00:00
---

# Platforms can now create Temporary Accounts via the Cloudflare API · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-14-temporary-accounts-api/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 14, 2026

## Platforms can now create Temporary Accounts via the Cloudflare API

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Platforms can now create temporary preview accounts through the Cloudflare REST API. This lets your platform deploy a live Worker before the user signs in to Cloudflare.

With the Temporary Accounts API, coding agents, AI app builders, and other platforms can build a similar flow for generated Workers and supported resources.

Your platform can keep users in its onboarding flow while they generate, deploy, and test an application. Users do not need an existing Cloudflare account, and your platform does not need write access to one.

![Diagram showing an AI agent deploying, verifying, and redeploying a Worker in a temporary account, then a user authenticating and claiming the account to keep its resources](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1748,height=368,format=webp/_astro/claim-deployments-flow.Co0tUHG4.png)

The API returns a claim URL that lets the user make the temporary account and its resources permanent.

[Cloudflare Drop ↗︎](https://www.cloudflare.com/drop/) demonstrates this preview-and-claim pattern for static sites. Someone can upload a site, test and share it for one hour, then sign in or create an account only when they want to keep it.

This API expands the flow first introduced with [`wrangler deploy --temporary`](https://developers.cloudflare.com/changelog/post/2026-06-19-temporary-accounts-for-agents/). Your backend now controls the provisioning and deployment experience directly:

  1. Show Cloudflare's Terms of Service and Privacy Policy in your product, and require the user to accept them.
  2. Request and solve a proof-of-work challenge.
  3. Create a temporary preview account.
  4. Deploy with the returned temporary account ID and API token.
  5. Show the deployed Worker URL and claim URL to the user.


    
    
    curl "https://api.cloudflare.com/client/v4/provisioning/previews/challenge" \
      -X POST \
      -H "Content-Type: application/json" \
      --data '{}'
    
    curl "https://api.cloudflare.com/client/v4/provisioning/previews" \
      -X POST \
      -H "Content-Type: application/json" \
      --data '{
        "termsOfService": "https://www.cloudflare.com/terms/",
        "privacyPolicy": "https://www.cloudflare.com/privacypolicy/",
        "acceptTermsOfService": "yes",
        "challengeToken": "<CHALLENGE_TOKEN>",
        "solution": {
          "checkpoints": "<BASE64_CHECKPOINTS>"
        }
      }'

For the complete API flow, proof-of-work requirements, supported products, and limits, refer to [Claim deployments (temporary accounts)](https://developers.cloudflare.com/workers/platform/claim-deployments/#integrate-with-the-rest-api). For the background and design goals behind this flow, refer to [Temporary Cloudflare Accounts for AI agents ↗︎](https://blog.cloudflare.com/temporary-accounts/).
