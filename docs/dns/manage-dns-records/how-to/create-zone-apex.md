---
url: https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-zone-apex/
title: Create zone apex record \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:58.774529+00:00
---

# Create zone apex record · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-zone-apex/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /…

[DNS records](https://developers.cloudflare.com/dns/manage-dns-records/)

  4. /How to
  5. /Create zone apex record



# Create zone apex record

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-zone-apex/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview ANAME or ALIASZone apex recordDomain redirectsGet free SSL certificates

When you add a domain to Cloudflare, you may also need to create or review the DNS record on your zone apex. Zone apex refers to the domain (`example.com`) or subdomain (`blog.example.com`) that you are [adding to Cloudflare](https://developers.cloudflare.com/dns/concepts/#zone).

Usually, the zone apex record makes your domain accessible by visitors. In this case, the necessary record type ([A, AAAA, or CNAME](https://developers.cloudflare.com/dns/manage-dns-records/reference/dns-record-types/#ip-address-resolution)) and its content will depend on the provider that [hosts](https://developers.cloudflare.com/fundamentals/manage-domains/#host-your-domain) your website or application. If you are using Cloudflare Pages, refer to [Custom domains](https://developers.cloudflare.com/pages/configuration/custom-domains/). If you are using other providers, look for their guidance on how to connect domains managed on external DNS services.

### ANAME or ALIAS

ANAME or ALIAS are DNS records used by specific DNS providers. If your previous provider was using ANAME or ALIAS, you can recreate these records on Cloudflare as CNAME records. Cloudflare's [CNAME flattening](https://developers.cloudflare.com/dns/cname-flattening/)1 allows you to create CNAME records at your [zone apex](https://developers.cloudflare.com/dns/concepts/#zone-apex), removing the need for those other record types.

## Footnotes

  1. A process in which Cloudflare returns an IP address instead of the target hostname that a CNAME record points to. ↩




## Zone apex record

To create a zone apex record, use `@` for the record **Name** , as in the following example.

Type | Name | IPv4 address | Proxy status  
---|---|---|---  
A | `@` | `192.0.2.1` | Proxied  
  
  1. In the Cloudflare dashboard, go to the **DNS Records** page.

[ Go to **Records** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/dns/records)
  2. Select **Add record**.

  3. Select `A`, `AAAA`, or `CNAME` as the record **Type** , according to your needs:

     * To point to an IPv4 address, select `A`, use your zone apex (`@`) for the record **Name** , and insert the IPv4 address in the respective field.
     * To point to an IPv6 address, select `AAAA`, use your zone apex (`@`) for the record **Name** , and insert the IPv6 address in the respective field.
     * To point to a [fully qualified domain name (FQDN) ↗︎](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) (such as `your-site.host.example.com`), select `CNAME`, use your zone apex (`@`) for the record **Name** , and insert the fully qualified domain name in the **Target** field.
  4. Specify the [**Proxy status**](https://developers.cloudflare.com/dns/proxy-status/) and [**TTL**](https://developers.cloudflare.com/dns/manage-dns-records/reference/ttl/) according to your needs.

  5. Select **Save** to confirm.




Use the [Create DNS Record API endpoint](https://developers.cloudflare.com/api/resources/dns/subresources/records/methods/create/).

For field definitions, refer to the [API documentation](https://developers.cloudflare.com/api/resources/dns/subresources/records/methods/create/) (visible once you select the record type under the request body specification).

  * To point to an IPv4 address, select **A Record** , use your zone apex (`@`) for the field `name`, and use the IPv4 address for the field `content`.
  * To point to an IPv6 address, select **AAAA Record** , use your zone apex (`@`) for the field `name`, and use the IPv6 address for the field `content`.
  * To point to a [fully qualified domain name (FQDN) ↗︎](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) (such as `your-site.host.example.com`), select **CNAME Record** , use your zone apex (`@`) for the field `name`, and use the fully qualified domain name for the field `content`.



## Domain redirects

Once you create a domain, you may want to route that traffic to other places.

For more guidance, refer to [Redirect domain to subdomain](https://developers.cloudflare.com/fundamentals/manage-domains/manage-subdomains/#redirect-the-apex-domain-to-a-subdomain) or [Redirect one domain to another](https://developers.cloudflare.com/fundamentals/manage-domains/redirect-domain/).

## Get free SSL certificates

While DNS is what communicates where your website or application can be reached, SSL/TLS is what enables websites and applications to establish connections in a secure way.

If your domain is not correctly covered by an SSL/TLS certificate, your visitors will find a warning on their browser stating that your website or application is not secure.

Cloudflare offers free, unshared, publicly trusted [Universal SSL certificates](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/) to all Cloudflare domains.

[PreviousManage DNS records](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/)[NextCreate subdomain records](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-subdomain/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/manage-dns-records/how-to/create-zone-apex.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
