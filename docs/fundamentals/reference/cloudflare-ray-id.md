---
url: https://developers.cloudflare.com/fundamentals/reference/cloudflare-ray-id/
title: Cloudflare Ray ID \u00b7 Cloudflare Fundamentals docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:25.126332+00:00
---

# Cloudflare Ray ID · Cloudflare Fundamentals docs

> Source: https://developers.cloudflare.com/fundamentals/reference/cloudflare-ray-id/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)
  3. /Reference
  4. /Cloudflare Ray ID



# Cloudflare Ray ID

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/fundamentals/reference/cloudflare-ray-id/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewLook up Ray IDs Security events Log Explorer Logs Server logs

A **Cloudflare Ray ID** is an identifier given to every request that goes through Cloudflare.

Ray IDs are particularly useful when evaluating Security Events for patterns or false positives or more generally understanding your application traffic.

Ray IDs are added as a [request header, cf-ray](https://developers.cloudflare.com/fundamentals/reference/http-headers/#cf-ray), to the connection from Cloudflare to the origin web server. As such the Ray IDs can be found using the Developer Tools in your browser or using curl with the `-v` option to show the headers.

Caution

Ray IDs are not guaranteed to be unique for every request. In some situations, different requests may have the same Ray ID.

## Look up Ray IDs

### Security events

All customers can view Ray IDs and associated information — IP address, user agent, ASN, etc. — by looking through [sampled logs](https://developers.cloudflare.com/waf/analytics/security-events/#sampled-logs) in Security Events.

![Example list of events in sampled logs, with the Ray ID highlighted from one of the expanded events to show its details](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1132,height=1367,format=webp/_astro/ray-id.CkgisnhS.png)

Additionally, you can [add filters](https://developers.cloudflare.com/waf/analytics/security-events/#adjust-displayed-data) to look for specific Ray IDs.

![Example of adding a new filter in Security Events for the Block action](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=929,height=281,format=webp/_astro/events-add-filter.DDUuZ0g7.png)

Please note that Security Events may use sampled data to improve performance. If sampled data is applied to your search, you might not see all events, and filters might not return the expected results. To display more events, select a smaller timeframe.

### Log Explorer

[Log Explorer](https://developers.cloudflare.com/log-explorer/) provides access to Cloudflare logs with all the context available within the Cloudflare platform. You can monitor security and performance issues with custom dashboards or investigate and troubleshoot issues with log search. Log explorer allows you to [build queries](https://developers.cloudflare.com/log-explorer/log-search/) for filtering specific Ray IDs.

### Logs

Enterprise customers can enable Ray ID as a field in their [Cloudflare Logs](https://developers.cloudflare.com/logs/).

### Server logs

For more details about sending Ray IDs to your server logs, refer to the [Cf-Ray](https://developers.cloudflare.com/fundamentals/reference/http-headers/#cf-ray) header.

[PreviousCloudflare HTTP headers](https://developers.cloudflare.com/fundamentals/reference/http-headers/)[NextCloudy AI agent](https://developers.cloudflare.com/fundamentals/reference/cloudy-ai-agent/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/fundamentals/reference/cloudflare-ray-id.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
