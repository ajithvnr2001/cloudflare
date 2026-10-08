---
url: https://developers.cloudflare.com/changelog/post/2026-10-02-kv-jurisdictions-ga/
title: Workers KV namespace jurisdictions are now generally available \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:18.758950+00:00
---

# Workers KV namespace jurisdictions are now generally available · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-02-kv-jurisdictions-ga/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 2, 2026

## Workers KV namespace jurisdictions are now generally available

[KV](https://developers.cloudflare.com/kv/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-10-02-kv-jurisdictions-ga/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Jurisdictions for [Workers KV](https://developers.cloudflare.com/kv/) namespaces are now generally available. When you create a namespace, you can set a [jurisdiction](https://developers.cloudflare.com/kv/reference/data-location/) to make sure the namespace's data is only durably stored within that region. Jurisdictions can help you comply with data localization regulations such as GDPR or FedRAMP. Supported jurisdictions are `eu`, `us`, and `fedramp`.

A jurisdiction can only be set when a namespace is created, using the Cloudflare dashboard, Wrangler, the `cf` CLI, or the REST API, and cannot be added or changed afterwards.
    
    
    npx wrangler@latest kv namespace create <NAMESPACE_NAME> --jurisdiction=eu
    
    
    cf kv namespaces create --title <NAMESPACE_NAME> --jurisdiction eu
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/storage/kv/namespaces" \
      --request POST \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "title": "<NAMESPACE_NAME>",
        "jurisdiction": "eu"
      }'

Workers can still access a namespace restricted to a jurisdiction from anywhere in the world, and KV data can be cached outside the jurisdiction on Cloudflare's network. The jurisdiction only controls where the namespace's data is durably stored.

To learn more, refer to [Data location](https://developers.cloudflare.com/kv/reference/data-location/).
