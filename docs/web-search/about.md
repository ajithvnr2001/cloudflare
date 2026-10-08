---
url: https://developers.cloudflare.com/web-search/about/
title: About Web Search API \u00b7 Cloudflare Web Search API docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:53.841276+00:00
---

# About Web Search API · Cloudflare Web Search API docs

> Source: https://developers.cloudflare.com/web-search/about/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Web Search API](https://developers.cloudflare.com/web-search/)
  3. /About



# About Web Search API

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/web-search/about/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow it worksAI Gateway integrationCrawler standardsRelated resources

AI models are only as good as the context you give them. Models are trained and then frozen at a point in time, so they only know about information that existed before their knowledge cutoff date. This makes it difficult to work with models on recent events, changing APIs, or fast-moving news.

Without web search, an agent that needs live information usually guesses the URL of a page and fetches it directly. When the guess is wrong, the request returns a `404 Not Found` and the agent has to try again.

Web Search API gives your agents a better option. Like a person starting with a search engine, your agent sends a query and receives a list of relevant, up-to-date results. You can inject those results into the model's context so its response is grounded in live information.

## How it works

When you send a search request, Web Search API:

  1. Routes the request through the AI Gateway you specify.
  2. Forwards the query to the search provider you choose — Ceramic.ai, Exa, or Linkup. If you do not set a provider, Web Search API uses Ceramic.ai as default.
  3. Normalizes the provider's response into a consistent format, with a URL, title, and optional description, image, favicon, and last-modified date for each result.
  4. Records the request in your AI Gateway logs and bills it to your account.



Because every provider returns the same result format, you can switch providers by changing a single parameter.

## AI Gateway integration

Web Search API is built on [AI Gateway](https://developers.cloudflare.com/ai-gateway/), which acts as the control plane for your AI applications. Every search request goes through a gateway, which gives you:

  * **Observability** — Search requests appear in your gateway's [logs](https://developers.cloudflare.com/ai-gateway/observability/logging/) and [analytics](https://developers.cloudflare.com/ai-gateway/observability/analytics/) alongside your model inference requests.
  * **Unified Billing** — Searches draw down from your [AI Gateway credit balance](https://developers.cloudflare.com/ai-gateway/features/unified-billing/). You pay each provider's list API price, with no additional markup. For rates, refer to [Providers](https://developers.cloudflare.com/web-search/providers/).
  * **Bring your own key (BYOK)** — If you already have an account with a search provider, you can [store your provider API key](https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/) on your gateway. The provider bills you directly.
  * **Access control** — Control which providers your gateway can use and who can send requests.



## Crawler standards

Cloudflare believes that crawlers should be honest and transparent, and should respect the rules and preferences that site owners set. Site owners should have meaningful visibility into and control over how their content is used.

Every Web Search API provider has committed to meet the following standards:

  * **Verified bot compliance** — The crawler the provider uses must meet Cloudflare's published requirements for [verified bots](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/). This includes identifying the crawler and respecting `robots.txt`.
  * **Source attribution** — Every search result must include a link to the location of the crawled content.



When you use Web Search API, your agents consume search results from operators that give site owners transparency, control, and visibility over how their content is crawled.

## Related resources

  * [How to use Web Search API](https://developers.cloudflare.com/web-search/how-to-use/)
  * [Providers and pricing](https://developers.cloudflare.com/web-search/providers/)
  * [AI Gateway](https://developers.cloudflare.com/ai-gateway/)



[PreviousOverview](https://developers.cloudflare.com/web-search/)[NextHow to use](https://developers.cloudflare.com/web-search/how-to-use/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/web-search/about.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
