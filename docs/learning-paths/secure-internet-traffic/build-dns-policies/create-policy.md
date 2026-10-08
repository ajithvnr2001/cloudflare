---
url: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-dns-policies/create-policy/
title: Create your first DNS policy \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:55.454126+00:00
---

# Create your first DNS policy · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-dns-policies/create-policy/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Secure Internet Traffic

  4. /[Build DNS security policies](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-dns-policies/)
  5. /Create your first DNS policy



# Create your first DNS policy

Last updated May 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-dns-policies/create-policy/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

DNS policies determine how Gateway should handle a DNS request. When a user sends a DNS request, Gateway matches the request against your filters and either allows the query to resolve, blocks the query, or responds to the query with a different IP.

You can filter DNS traffic based on query or response parameters (such as domain, source IP, or geolocation). You can also filter by user identity if you connect your devices to Gateway with the [Cloudflare One Client or Cloudflare One Agent](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/connect-devices-networks/install-agent/).

To create a new DNS policy:

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Traffic policies** > **Firewall policies**.
  2. In the **DNS** tab, select **Add a policy**.
  3. Name the policy.
  4. Under **Traffic** , build a logical expression that defines the traffic you want to allow or block.
  5. Choose an **Action** to take when traffic matches the logical expression. For example, we recommend adding a policy to block all [security categories](https://developers.cloudflare.com/cloudflare-one/traffic-policies/domain-categories/#security-categories): 

Selector | Operator | Value | Action  
---|---|---|---  
Security Categories | in | _All security risks_ | Block  
  
  6. Select **Create policy**.



For more information, refer to [DNS policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/).

To create a new DNS policy using cURL:

Create a Zero Trust Gateway rulebash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/gateway/rules" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"name": "All-DNS-SecurityCategories-Blocklist",
    		"description": "Block known security risks based on Cloudflare'\''s threat intelligence",
    		"precedence": 0,
    		"enabled": true,
    		"action": "block",
    		"filters": [
    				"dns"
    		],
    		"traffic": "any(dns.security_category[*] in {68 178 80 83 176 175 117 131 134 151 153})",
    		"rule_settings": {
    				"block_page_enabled": true,
    				"block_reason": "This domain was blocked due to being classified as a security risk to your organization"
    		}
    	}'

To create a new DNS policy using **Terraform** :
    
    
    resource "cloudflare_zero_trust_gateway_policy" "security_risks_dns_policy" {
      account_id  = var.cloudflare_account_id
      name        = "All-DNS-SecurityCategories-Blocklist"
      description = "Block known security risks based on Cloudflare's threat intelligence"
      precedence  = 0
      enabled     = true
      action      = "block"
      filters     = ["dns"]
      traffic     = "any(dns.security_category[*] in {68 178 80 83 176 175 117 131 134 151 153})"
      rule_settings {
          block_page_enabled = true
          block_page_reason = "This domain was blocked due to being classified as a security risk to your organization"
        }
    }

[PreviousOverview](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-dns-policies/)[NextCreate an allowlist or blocklist](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-dns-policies/create-list/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/secure-internet-traffic/build-dns-policies/create-policy.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
