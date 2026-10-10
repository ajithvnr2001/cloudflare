---
url: https://developers.cloudflare.com/changelog/post/2026-08-13-artifacts-jurisdictions/
title: Data localization support for Artifacts \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:33.125279+00:00
---

# Data localization support for Artifacts · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-13-artifacts-jurisdictions/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 13, 2026

## Data localization support for Artifacts

[Artifacts](https://developers.cloudflare.com/artifacts/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Artifacts now supports jurisdictions, allowing you to select the European Union or the United States as the only location where repo data is stored and processed.

Select a jurisdiction when you create a namespace. Every repo in that namespace automatically uses the selected jurisdiction.
    
    
    curl --request POST \
      "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/artifacts/namespaces" \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "namespace": "my-eu-namespace",
        "jurisdiction": "eu"
      }'

Jurisdictions cannot be changed after namespace creation. If you omit the jurisdiction, Artifacts creates an unrestricted namespace.

For supported jurisdictions and usage details, refer to [Data localization](https://developers.cloudflare.com/artifacts/guides/data-localization/).
