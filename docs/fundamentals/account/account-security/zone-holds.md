---
url: https://developers.cloudflare.com/fundamentals/account/account-security/zone-holds/
title: Zone holds \u00b7 Cloudflare Fundamentals docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:19.798632+00:00
---

# Zone holds · Cloudflare Fundamentals docs

> Source: https://developers.cloudflare.com/fundamentals/account/account-security/zone-holds/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)
  3. /…

Accounts

  4. /Account security
  5. /Zone holds



# Zone holds

Last updated Aug 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/fundamentals/account/account-security/zone-holds/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAvailabilityEnable zone holdsRelease zone holds

Zone holds prevent other teams in your organization from adding zones that are already active in another account.

For example, you might already have an active Cloudflare zone for `example.com`. If another team does not realize this, they could add and activate `example.com` in another Cloudflare account, which may cause downtimes or security issues until the original zone could be re-activated.

Note

Zone holds are enabled by default for all Enterprise zones.

## Availability

| Free | Pro | Business | Enterprise  
---|---|---|---|---  
Availability | No | No | No | Yes  
  
## Enable zone holds

When you enable a zone hold, no one else can [add your zone](https://developers.cloudflare.com/fundamentals/manage-domains/add-site/) to their Cloudflare account. If they attempt to, they will receive the following message:

_The zone name provided is subject to a hold which disallows the creation of this zone. Please contact the domain owner to have this hold removed._

To enable a zone hold:

  1. Log into the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com).
  2. Select your account and zone.
  3. On the zone homepage, go to **Quick Actions**.
  4. For **Zone Hold** , switch the toggle to **On**.



You also have the option to **Also prevent subdomains** , which prevents anyone in your organization from creating subdomains or custom hostnames related to your zone.

## Release zone holds

You may want to temporarily release a zone hold to allow another team to [register a subdomain](https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/) in a separate Cloudflare account, such as `docs.example.com`.

To release a zone hold:

  1. Log into the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com).
  2. Select your account and zone.
  3. On the zone homepage, go to **Quick Actions**.
  4. For **Zone Hold** , switch the toggle to **Off**.
  5. Choose the length of your release.
  6. Select **Release hold**.



[PreviousSet up SSO ↗︎](https://developers.cloudflare.com/fundamentals/manage-members/dashboard-sso/)[NextFind account and zone IDs](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/fundamentals/account/account-security/zone-holds.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
