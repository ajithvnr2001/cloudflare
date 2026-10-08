---
url: https://developers.cloudflare.com/changelog/post/2026-01-22-deny-by-default-for-zones/
title: Require Access protection for zones \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:34.380677+00:00
---

# Require Access protection for zones · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-01-22-deny-by-default-for-zones/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)January 22, 2026

## Require Access protection for zones

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-22-deny-by-default-for-zones/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now require Cloudflare Access protection for all hostnames in your account. When enabled, traffic to any hostname that does not have a matching Access application is automatically blocked.

This deny-by-default approach prevents accidental exposure of internal resources to the public Internet. If a developer deploys a new application or creates a DNS record without configuring an Access application, the traffic is blocked rather than exposed.

![Require Cloudflare Access protection in the dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2160,height=738,format=webp/_astro/require-cloudflare-access-protection.BAUmTYOs.png)

#### How it works

  * **Blocked by default** : Traffic to all hostnames in the account is blocked unless an Access application exists for that hostname.
  * **Explicit access required** : To allow traffic, create an Access application with an Allow or Bypass policy.
  * **Hostname exemptions** : You can exempt specific hostnames from this requirement.



To turn on this feature, refer to [Require Access protection](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/require-access-protection/).
