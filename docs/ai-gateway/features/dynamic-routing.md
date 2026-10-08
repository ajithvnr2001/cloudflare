---
url: https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/
title: Dynamic routing \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:29.656208+00:00
---

# Dynamic routing · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /[Features](https://developers.cloudflare.com/ai-gateway/features/)
  4. /Dynamic routing



# Dynamic routing

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewIntroductionCore ConceptsGetting Started

## Introduction

Dynamic routing enables you to create request routing flows through a **visual interface** or a **JSON-based configuration**. Instead of hard-coding a single model, with Dynamic Routing you compose a small flow that evaluates conditions, enforces quotas, and chooses models with fallbacks. You can iterate without touching application code—publish a new route version and you’re done. With dynamic routing, you can easily implement advanced use cases such as:

  * Directing different segments (paid/not-paid user) to different models
  * Restricting each user/project/team with budget/rate limits
  * A/B and gradual rollouts



while making it accessible to both developers and non-technical team members.

![Dynamic Routing Overview](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1814,height=1642,format=webp/_astro/dynamic-routing.BtwkWywo.png)

## Core Concepts

  * **Route** : A named, versioned flow (for example, dynamic/support) that you can use as instead of the model name in your requests.
  * **Nodes**
    * **Start** : Entry point for the route.
    * **Conditional** : If/Else branch based on expressions that reference request body, headers, or metadata (for example, user_plan == "paid").
    * **Percentage** : Routes requests probabilistically across multiple outputs, useful for A/B testing and gradual rollouts.
    * **Model** : Calls a provider/model with the request parameters
    * **Rate Limit** : Enforces number of requests quotas (per your key, per period) and switches to fallback when exceeded.
    * **Budget Limit** : Enforces cost quotas (per your key, per period) and switches to fallback when exceeded.
    * **End** : Terminates the flow and returns the final model response.
  * **Metadata** : Arbitrary key-value context attached to the request (for example, userId, orgId, plan). You can pass this from your app so rules can reference it.
  * **Versions** : Each change produces a new draft. Deploy to make it live with instant rollback.



## Getting Started

Caution

Ensure your gateway has [authentication](https://developers.cloudflare.com/ai-gateway/configuration/authentication/) turned on, and you have your upstream providers keys stored with [BYOK](https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/).

  1. Create a route. 
     * Go to **(Select your gateway)** > **Dynamic Routes** > **Add Route** , and name it (for example, `support`).
     * Open **Editor**.
  2. Define conditionals, limits and other settings. 
     * You can use [Custom Metadata](https://developers.cloudflare.com/ai-gateway/observability/custom-metadata/) in your conditionals.
  3. Configure model nodes. 
     * Example: 
       * Node A: Provider OpenAI, Model `o4-mini-high`
       * Node B: Provider OpenAI, Model `gpt-4.1`
  4. Save a version. 
     * Click **Save** to save the state. You can always roll back to earlier versions from **Versions**.
     * Deploy the version to make it live.
  5. Call the route from your code. 
     * Use the route name in place of the model, for example, `dynamic/support`. See [Using a dynamic route](https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/usage/) for examples.



Note

Dynamic routes accept the OpenAI chat completions request shape only. You can call them through the [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/) at `/ai/v1/chat/completions`, the [AI binding](https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/) in a Worker, or the [OpenAI-compatible endpoint](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/) at `/compat/chat/completions`. Other request formats, such as Anthropic Messages, return a `400` error.

Dynamic routes are scoped to the gateway you created them on. On the REST API, set the `cf-aig-gateway-id` header to that gateway, otherwise the request resolves against your default gateway and returns a `404` error.

[PreviousRate limiting](https://developers.cloudflare.com/ai-gateway/features/rate-limiting/)[NextUsing a dynamic route](https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/usage/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/features/dynamic-routing/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
