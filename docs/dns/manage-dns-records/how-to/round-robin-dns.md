---
url: https://developers.cloudflare.com/dns/manage-dns-records/how-to/round-robin-dns/
title: Round-robin DNS \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:58.998303+00:00
---

# Round-robin DNS · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/manage-dns-records/how-to/round-robin-dns/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /…

[DNS records](https://developers.cloudflare.com/dns/manage-dns-records/)

  4. /How to
  5. /Round-robin DNS



# Round-robin DNS

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dns/manage-dns-records/how-to/round-robin-dns/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewExample scenario All records unproxied All records proxied (recommended) Unproxied and proxied records

To randomly distribute traffic across multiple servers, set up multiple DNS `A` or `AAAA` records for the same hostname.

Use this setup for simple, [round-robin load balancing ↗︎](https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/). If you need more fine-grained control over traffic distribution — including automatic failover, intelligent routing, and more — set up our [add-on load balancing service](https://developers.cloudflare.com/load-balancing/).

## Example scenario

The following example illustrates how you would distribute traffic intended for `www.example.com`. Though the example uses `A` records, you could also use `AAAA` records.

After [creating an account](https://developers.cloudflare.com/fundamentals/account/create-account/) and [updating your nameservers](https://developers.cloudflare.com/dns/zone-setups/full-setup/setup/) for `example.com`, you might [create multiple subdomain DNS records](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/) for `www`:

Type | Name | IPv4 address  
---|---|---  
A | `www` | `192.0.2.1`  
A | `www` | `192.0.2.2`  
A | `www` | `192.0.2.3`  
  
The exact behavior of your DNS routing would depend on the [proxy status](https://developers.cloudflare.com/dns/proxy-status/) of each record.

### All records unproxied

If all associated records were unproxied, any request to Cloudflare's nameservers would return the three `A` records you previously added.

Each client (oftentimes a browser), would decide which IP address to send the request to. If one IP address fails, the client would choose another option. All requests would be sent directly to the origin server (either `192.0.2.1`, `192.0.2.2`, or `192.0.2.3`, using the example above).

### All records proxied (recommended)

If all associated records were proxied, any request to Cloudflare's nameservers would return two `A` records from Cloudflare's list of IP addresses.

Each client (oftentimes a browser) would decide which Cloudflare IP address to send the request to. Cloudflare would then receive that request and — if Cloudflare needed to contact your origin server — we would pick one of the three IP addresses specified in your DNS records (either `192.0.2.1`, `192.0.2.2`, or `192.0.2.3`, using the example above).

Beyond reducing requests to your origin server, this setup allows your application to take advantage of Cloudflare's [Zero downtime failover](https://developers.cloudflare.com/fundamentals/security/protect-your-origin-server/#zero-downtime-failover). When a request to one IP address fails, Cloudflare automatically retries the request to other IP addresses associated with the same hostname. This behavior prevents end users from experiencing downtime.

### Unproxied and proxied records

If you have a mix of proxied and unproxied records associated with the same hostname, requests happen as if you had all proxied records.

This approach is not typically recommended because it can lead to unexpected behavior. For example, if you had two unproxied records and one proxied record, Cloudflare would treat all records as proxied. However, if you deleted the single proxied record, your remaining two unproxied records would immediately be treated as unproxied.

We recommend either using all proxied or all unproxied records to avoid surprises when you make changes to your DNS records.

[PreviousDynamically update DNS records](https://developers.cloudflare.com/dns/manage-dns-records/how-to/managing-dynamic-ip-addresses/)[NextDelegate subdomains](https://developers.cloudflare.com/dns/manage-dns-records/how-to/subdomains-outside-cloudflare/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/manage-dns-records/how-to/round-robin-dns.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
