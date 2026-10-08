---
url: https://developers.cloudflare.com/dns/dns-firewall/setup/
title: Set up DNS Firewall \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:56.437176+00:00
---

# Set up DNS Firewall · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/dns-firewall/setup/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /[DNS Firewall](https://developers.cloudflare.com/dns/dns-firewall/)
  4. /Setup



# Setup

Last updated Jul 10, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dns/dns-firewall/setup/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesConfigure DNS Firewall Create a DNS Firewall cluster Update registrar settings Update DNS servers Test DNS resolution Update security policiesAdditional options

## Prerequisites

Prior to setting up DNS Firewall, you need:

  * Account access to DNS Firewall (provided by your Enterprise account team).
  * Access to **DNS Administrator** or **Super Administrator** privileges on your account.
  * Newly updated IP addresses for your nameservers (protects against previously compromised IP addresses).



## Configure DNS Firewall

### Create a DNS Firewall cluster

  1. In the Cloudflare dashboard, go to the **DNS Firewall Clusters** page.

[ Go to **Clusters** ↗ ](https://dash.cloudflare.com/?to=/:account/dns-firewall/clusters)
  2. Select **Add Firewall Cluster**.

  3. Fill out the required fields, including:

     * **IP Addresses** : The upstream IPv4 and/or IPv6 addresses of your authoritative nameservers.
     * **Minimum Cache TTL** : Recommended setting of **30 seconds**.
     * **Maximum Cache TTL** : Recommended setting of **4 hours**. Larger values increase the cache hit ratio, but also increase the time required for DNS changes to propagate.
     * **ANY queries** : Recommended setting is **Off** because these are often used as part of DDoS attacks. Also refer to this [blog post ↗︎](https://blog.cloudflare.com/rfc8482-saying-goodbye-to-any/).
  4. Optionally, configure any of the additional options available on the same form.

  5. Select **Continue**.

  6. On the following screen, save the values for **Your new DNS Firewall IP Addresses**.




Note:

If you forget to save your new IP addresses, find your cluster and click **IP Addresses**.

If you delete your cluster, the assigned set of IPs will be lost. If you recreate the cluster you will get a different set of IPs.

You can also create a DNS Firewall cluster by sending a [POST request](https://developers.cloudflare.com/api/resources/dns_firewall/methods/create/) to the API.

### Update registrar settings

Update the `A/AAAA` glue records for your nameserver hostnames at your registrar with your DNS Firewall cluster IP addresses.

### Update DNS servers

At your DNS servers, update the `A/AAAA` records for your nameserver hostnames in your DNS zone file with your DNS Firewall cluster IP addresses.

### Test DNS resolution

Confirm that your nameservers are functioning correctly by running a `dig` command.

### Update security policies

Configure security policy in your DNS servers and Firewall to allow only [Cloudflare IPs ↗︎](https://cloudflare.com/ips) and TCP/UDP port 53.

## Additional options

Beyond the required fields, you can configure the following settings on your DNS Firewall cluster — in the Cloudflare dashboard when you create or edit a cluster, or via the API:

  * **Rate limit** (queries per second per data center).
  * **Negative cache TTL** for `REFUSED`, `NXDOMAIN`, and `SERVFAIL` responses.
  * **EDNS Client Subnet (ECS) fallback** — forward the resolver's IP subnet when the incoming query does not include ECS data. Refer to the [FAQ](https://developers.cloudflare.com/dns/dns-firewall/faq/#does-dns-firewall-support-edns-client-subnet-ecs) for details.
  * **Attack mitigation** for [random prefix attacks](https://developers.cloudflare.com/dns/dns-firewall/random-prefix-attacks/).



For the full parameter reference, refer to the [Create](https://developers.cloudflare.com/api/resources/dns_firewall/methods/create/) and [Update](https://developers.cloudflare.com/api/resources/dns_firewall/methods/edit/) DNS Firewall Cluster API endpoints.

[PreviousOverview](https://developers.cloudflare.com/dns/dns-firewall/)[NextAnalytics and logs](https://developers.cloudflare.com/dns/dns-firewall/analytics/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/dns-firewall/setup.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
