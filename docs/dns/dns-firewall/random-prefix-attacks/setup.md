---
url: https://developers.cloudflare.com/dns/dns-firewall/random-prefix-attacks/setup/
title: Protect against random prefix attacks \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:56.686493+00:00
---

# Protect against random prefix attacks · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/dns-firewall/random-prefix-attacks/setup/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /…

[DNS Firewall](https://developers.cloudflare.com/dns/dns-firewall/)

  4. /[Random prefix attack mitigation](https://developers.cloudflare.com/dns/dns-firewall/random-prefix-attacks/)
  5. /Setup



# Setup

Last updated Jul 10, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dns/dns-firewall/random-prefix-attacks/setup/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

In order to enable automatic mitigation of [random prefix attacks](https://developers.cloudflare.com/dns/dns-firewall/random-prefix-attacks/about/):

  1. Set up [DNS Firewall](https://developers.cloudflare.com/dns/dns-firewall/setup/).

  2. Enable attack mitigation on your DNS Firewall cluster.

     1. In the Cloudflare dashboard, go to the **DNS Firewall Clusters** page.

[ Go to **Clusters** ↗ ](https://dash.cloudflare.com/?to=/:account/dns-firewall/clusters)
     2. Select the cluster you want to update, then select **Edit**.

     3. Turn on **Attack mitigation** and choose whether Cloudflare should only mitigate attacks when the upstream is unhealthy.

     4. Select **Save**.

Send a [`PATCH` request](https://developers.cloudflare.com/api/resources/dns_firewall/methods/edit/) to update your DNS Firewall cluster:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:
     * `DNS Firewall Write`
Update DNS Firewall Clusterbash
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/dns_firewall/$DNS_FIREWALL_ID" \
    	--request PATCH \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"attack_mitigation": {
    				"enabled": true,
    				"only_when_upstream_unhealthy": true
    		}
    	}'




Once you turn on attack mitigation, Cloudflare returns a `REFUSED` response to queries that are part of a random prefix attack.

Note

If you do not specify otherwise, Cloudflare automatically sets the `only_when_upstream_unhealthy` parameter to true, which means that Cloudflare will only mitigate attacks when we detect that the upstream is unresponsive (possibly as a result of an attack).

[PreviousAbout](https://developers.cloudflare.com/dns/dns-firewall/random-prefix-attacks/about/)[NextAnalytics API properties](https://developers.cloudflare.com/dns/reference/analytics-api-properties/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/dns-firewall/random-prefix-attacks/setup.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
