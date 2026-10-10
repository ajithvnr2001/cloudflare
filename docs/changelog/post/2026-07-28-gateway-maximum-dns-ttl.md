---
url: https://developers.cloudflare.com/changelog/post/2026-07-28-gateway-maximum-dns-ttl/
title: Control Cloudflare Gateway DNS caching with a maximum TTL setting \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:34.144713+00:00
---

# Control Cloudflare Gateway DNS caching with a maximum TTL setting · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-28-gateway-maximum-dns-ttl/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 28, 2026

## Control Cloudflare Gateway DNS caching with a maximum TTL setting

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now set a maximum time-to-live (TTL) for DNS responses returned by Gateway. When an upstream DNS record has a TTL that exceeds the configured maximum, Gateway caps it to your specified value. This ensures that DNS policy changes - such as blocking a newly identified malicious domain - take effect faster across all clients.

![The maximum DNS TTL setting in Traffic policies > Traffic settings, showing a numeric input field that accepts values between 60 and 36,000 seconds](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2170,height=294,format=webp/_astro/gateway-max-ttl-traffic-settings.BRF3NUMp.png)

The setting is available at two levels:

  * **Account level** \- In **Traffic Policies** > **Traffic Settings** , under **Proxy and inspection**. This sets the default cap for all DNS locations.
  * **Per-location** \- Each [DNS location](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-proxies/) can inherit the account setting, disable the cap, or override it with a custom value.



Two new fields are also available in DNS logs: `upstream_record_ttls` (the original TTL from the upstream response) and `applied_max_ttl` (the cap Gateway applied). These appear in the DNS logs column picker and in Logpush datasets.

For more information, refer to [Maximum DNS TTL](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/maximum-dns-ttl/).
