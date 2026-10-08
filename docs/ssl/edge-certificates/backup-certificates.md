---
url: https://developers.cloudflare.com/ssl/edge-certificates/backup-certificates/
title: Backup certificates \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:39.303689+00:00
---

# Backup certificates · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/edge-certificates/backup-certificates/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /[Edge certificates](https://developers.cloudflare.com/ssl/edge-certificates/)
  4. /Backup certificates



# Backup certificates

Last updated Sep 8, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/edge-certificates/backup-certificates/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAvailabilityOpt outTroubleshooting Backup certificate deleted after turning Universal SSL back on

If Cloudflare is providing [authoritative DNS](https://developers.cloudflare.com/dns/zone-setups/full-setup/) for your domain, Cloudflare will issue a backup [Universal SSL certificate](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/) for every standard Universal certificate issued.

Backup certificates are wrapped with a different private key and issued from a different Certificate Authority — either Google Trust Services, Let's Encrypt, Sectigo, or SSL.com — than your domain's primary Universal SSL certificate.

These backup certificates are not normally deployed, but they will be deployed automatically by Cloudflare in the event of a certificate revocation or key compromise.

For additional details, refer to the [introductory blog post ↗︎](https://blog.cloudflare.com/introducing-backup-certificates/).

## Availability

| Free | Pro | Business | Enterprise  
---|---|---|---|---  
Availability | Yes | Yes | Yes | Yes  
Can opt out? | No | No | No | Yes  
  
## Opt out

Enterprise customers can request to opt out of backup certificates by opening a support case. Opting out removes the backup-certificate redundancy for your domain.

## Troubleshooting

### Backup certificate deleted after turning Universal SSL back on

After you turn off and quickly turn Universal SSL back on, your domain may end up without a backup certificate.

When Universal SSL is toggled off and on in quick succession, certificate processing jobs are not guaranteed to run in the order they were submitted. This race condition can cause a newly issued backup certificate to be deleted before it becomes active.

To recover your backup certificate:

  1. Turn Universal SSL off again.
  2. Wait several minutes.
  3. Turn Universal SSL back on, then allow time for Cloudflare to issue a new backup certificate.



If you need uninterrupted certificate coverage, consider ordering an [Advanced Certificate Manager](https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/) certificate before toggling Universal SSL.

For more troubleshooting help, refer to [Troubleshooting SSL errors](https://developers.cloudflare.com/ssl/troubleshooting/).

[PreviousStaging environment](https://developers.cloudflare.com/ssl/edge-certificates/staging-environment/)[NextECH Protocol](https://developers.cloudflare.com/ssl/edge-certificates/ech/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/edge-certificates/backup-certificates.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
