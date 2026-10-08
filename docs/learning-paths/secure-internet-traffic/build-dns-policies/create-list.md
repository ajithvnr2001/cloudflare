---
url: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-dns-policies/create-list/
title: Create an allowlist or blocklist \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:55.369315+00:00
---

# Create an allowlist or blocklist · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-dns-policies/create-list/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Secure Internet Traffic

  4. /[Build DNS security policies](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-dns-policies/)
  5. /Create an allowlist or blocklist



# Create an allowlist or blocklist

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-dns-policies/create-list/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewExample list policy

In the context of DNS filtering, a blocklist is a list of known harmful domains or IP addresses. An allowlist is a list of allowed domains or IP addresses, such as the domains of essential corporate applications.

Gateway supports creating [lists](https://developers.cloudflare.com/cloudflare-one/reusable-components/lists/) of URLs, hostnames, or other entries to use in your policies.

## Example list policy

The following DNS policy will allow access to all approved corporate domains included in a list called **Corporate Domains**.

Selector | Operator | Value | Action  
---|---|---|---  
Domain | in list | _Corporate Domains_ | Allow  
  
Create a Zero Trust Gateway rulebash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/gateway/rules" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"name": "All-DNS-CorporateDomain-AllowList",
    		"description": "Allow access to the corporate domains defined under the Corporate Domains list",
    		"precedence": 1,
    		"enabled": true,
    		"action": "allow",
    		"filters": [
    				"dns"
    		],
    		"traffic": "any(dns.domains[*] in $<CORPORATE_DOMAINS_LIST_UUID>)"
    	}'

To create a new DNS policy using **Terraform** to allow access to all approved corporate domains included in a list called **Corporate Domains**.
    
    
    resource "cloudflare_zero_trust_gateway_policy" "allow_corporate_domain_access" {
      account_id  = var.cloudflare_account_id
      name        = "All-DNS-CorporateDomain-AllowList"
      description = "Allow access to the corporate domains defined under the Corporate Domains list"
      precedence  = 1
      enabled     = false
      action      = "allow"
      filters     = ["dns"]
      traffic     = "any(dns.domains[*] in $<Corporate Domains List UUID>)"
    }

[PreviousCreate your first DNS policy](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-dns-policies/create-policy/)[NextRecommended DNS policies](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-dns-policies/recommended-dns-policies/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/secure-internet-traffic/build-dns-policies/create-list.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
