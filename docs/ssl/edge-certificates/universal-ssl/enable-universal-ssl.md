---
url: https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/enable-universal-ssl/
title: Enable Universal SSL certificates \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:41.237368+00:00
---

# Enable Universal SSL certificates · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/enable-universal-ssl/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /…

[Edge certificates](https://developers.cloudflare.com/ssl/edge-certificates/)

  4. /[Universal SSL](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/)
  5. /Enable Universal SSL certificates



# Enable Universal SSL certificates

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/enable-universal-ssl/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewFull DNS setup Minimize downtimePartial DNS setupVerify your certificate is activeUniversal SSL renewal

By default, Cloudflare issues — and [renews](https://developers.cloudflare.com/ssl/reference/certificate-validity-periods/#universal-ssl) — free, unshared, publicly trusted SSL certificates to all domains [added to](https://developers.cloudflare.com/fundamentals/manage-domains/add-site/) and [activated on](https://developers.cloudflare.com/dns/zone-setups/reference/domain-status/) Cloudflare.

* * *

The process for activating a Universal SSL certificate depends on your domain's DNS setup.

## Full DNS setup

For domains on a [primary setup (full)](https://developers.cloudflare.com/dns/zone-setups/full-setup/)1, your domain should **automatically** receive its Universal SSL certificate within **15 minutes to 24 hours** of domain activation2.

This certificate will cover your zone apex (`example.com`) and all first-level subdomains (`subdomain.example.com`), and is provisioned even if your records are DNS only. However, the certificate will only be presented if your domain or subdomains are [proxied](https://developers.cloudflare.com/dns/proxy-status/).

## Footnotes

  1. The most common Cloudflare setup that involves changing your authoritative nameservers. ↩

  2. Provisioning time depends on certain security checks and other requirements mandated by Certificate Authorities (CA). ↩




### Minimize downtime

If your website or application is already live and cannot be uncovered while the Universal certificate is provisioned, consider the following:

  * Order an [advanced certificate](https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/) before proxying traffic to Cloudflare.
  * Upload a [custom certificate](https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/) prior to migrating and then delete the certificate after your Universal certificate is active.
  * Keep DNS records [**unproxied**](https://developers.cloudflare.com/dns/proxy-status/) until your certificate is active.



Note

If your domain is using a **partial setup** , you will need to add [Domain Control Validation (DCV) records](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/) to your authoritative DNS.

## Partial DNS setup

For non-authoritative or [partial domains](https://developers.cloudflare.com/dns/zone-setups/partial-setup/), Universal SSL will be:

  * Provisioned once the DNS record is [proxied through Cloudflare](https://developers.cloudflare.com/dns/zone-setups/partial-setup/setup/#3-add-dns-records).
  * Validated: 
    * Immediately if you add [Domain Control Validation (DCV)](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/) records to your authoritative DNS.
    * After a brief period of downtime if you **do not** add DCV records (once your traffic is proxied).



Unless you cover and validate multiple subdomains with an [advanced certificate](https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/), you will need to proxy and validate new subdomains as they are added.

* * *

## Verify your certificate is active

Once you enable Universal SSL, you can review the [activation status](https://developers.cloudflare.com/ssl/reference/certificate-statuses/) on the [**Edge Certificates** ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/edge-certificates) page or via the API with a [GET request](https://developers.cloudflare.com/api/resources/ssl/subresources/certificate_packs/methods/list/).

* * *

## Universal SSL renewal

For Universal certificates, Cloudflare controls the validity periods and certificate authorities (CAs), making sure that renewal always occur.

Partial setup and DCV

If you are on a [CNAME setup (partial)](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/enable-universal-ssl/#partial-dns-setup), make sure [Domain control validation (DCV)](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/) is configured correctly. Refer to [Troubleshooting DCV](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/troubleshooting/) for further help.

Universal certificates have a 90-day validity period. The auto renewal period starts 30 days before expiration.

For details, refer to [Validity periods and renewal](https://developers.cloudflare.com/ssl/reference/certificate-validity-periods/).

[PreviousOverview](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/)[NextDisable Universal SSL certificates](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/disable-universal-ssl/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/edge-certificates/universal-ssl/enable-universal-ssl.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
