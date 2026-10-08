---
url: https://developers.cloudflare.com/learning-paths/replace-vpn/build-policies/create-list/
title: Create a list of IPs or domains \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:52.778460+00:00
---

# Create a list of IPs or domains · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/replace-vpn/build-policies/create-list/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Replace Vpn

  4. /[Build secure access policies](https://developers.cloudflare.com/learning-paths/replace-vpn/build-policies/)
  5. /Create a list of IPs or domains



# Create a list of IPs or domains

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/replace-vpn/build-policies/create-list/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate a list from a CSV fileCreate a list manually

Gateway supports creating [lists](https://developers.cloudflare.com/cloudflare-one/reusable-components/lists/) of IPs, hostnames, or other entries to reference in your policies.

It is likely that you will be onboarding to the Cloudflare platform with some predetermined series of security policies. Maybe you have explicit deny lists based on hostnames, IPs, or another measure that tie to individual users. Maybe some networks can access certain apex records while others cannot.

The best way to migrate to Cloudflare in a way that will simplify ongoing maintenance is to build as many reusable objects as possible. Not only because that makes policy building simpler, but because as those applications, networks, and services organically change and grow, updates to the lists automatically update everywhere that the lists are applied.

## Create a list from a CSV file

To test uploading CSV lists, you can download a [sample CSV file](https://developers.cloudflare.com/cloudflare-one/static/list-test.csv) of IP address ranges or copy the following into a file:

list-test.csvcsv
    
    
    value,description
    192.0.2.0/24,This is an IP address range in CIDR format
    198.51.100.0/24,This is also an IP address range
    203.0.113.0/24,This is the third IP address range

When you format a CSV file for upload:

  * Each line should be a single entry that includes a value and an optional description.
  * A header row must be present for Zero Trust to recognize descriptions.
  * Trailing whitespace characters are not allowed.
  * CRLF (Windows) and LF (Unix) line endings are valid.



To upload the list to the Cloudflare dashboard:

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Reusable components** > **Lists**.
  2. Select **Upload CSV**.
  3. Next, specify a **List name** , enter an optional description, and choose a **List type**.
  4. Drag and drop a file into the **CSV file** window, or select a file.
  5. Select **Create**.



  1. Add the following permission to your [`cloudflare_api_token` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/api_token):

     * `Zero Trust Write`
  2. Decode the contents of the CSV file and store it as a local value:
         
         locals {
         	ip_list = csvdecode(file("${path.module}/list-test.csv"))
         }

  3. Create a list using the [`cloudflare_zero_trust_list` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zero_trust_list) resource:
         
         resource "cloudflare_zero_trust_list" "ips_from_csv" {
         	account_id  = var.cloudflare_account_id
         	name        = "IPs imported from CSV"
         	description = "Managed by Terraform"
         	type        = "IP"
         	items 			= local.ip_list
         }




You can now use this list in the policy builder by choosing the _in list_ operator.

## Create a list manually

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Reusable components** > **Lists**.
  2. Select **Create manual list**.
  3. Next, specify a **List name** , enter an optional description, and choose a **List type**.
  4. Enter your list element manually into the **Add entry** field and select **Add**.
  5. Select **Save**.



Create Zero Trust listbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/gateway/lists" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"description": "Private application IPs",
    		"items": [
    				{
    						"value": "10.226.0.177/32"
    				},
    				{
    						"value": "10.226.1.177/32"
    				}
    		],
    		"name": "Corporate IP list",
    		"type": "IP"
    	}'

  1. Add the following permission to your [`cloudflare_api_token` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/api_token):

     * `Zero Trust Write`
  2. Create a list using the [`cloudflare_zero_trust_list` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zero_trust_list) resource.

Example list of IPs:
         
         resource "cloudflare_zero_trust_list" "wiki_IPs" {
         	account_id  = var.cloudflare_account_id
         	name        = "Company Wiki IP addresses"
         	description = "Managed by Terraform"
         	type        = "IP"
         	items = [
         		{
         			description = "Example IP address range"
         			value = "192.0.2.0/24",
         		},
         		{
         			value = "198.51.100.0/24"
         		}
         	]
         }

Example list of domains:
         
         resource "cloudflare_zero_trust_list" "wiki_domains" {
         	account_id  = var.cloudflare_account_id
         	name        = "Company Wiki Domains"
         	description = "Managed by Terraform"
         	type        = "DOMAIN"
         	items = [
         		{
         			value = "wiki.example.com"
         		},
         		{
         			value = "wiki2.example.com"
         		}]
         }




You can now use this list in the policy builder by choosing the _in list_ operator.

[PreviousPolicy design](https://developers.cloudflare.com/learning-paths/replace-vpn/build-policies/policy-design/)[NextSecure your first application](https://developers.cloudflare.com/learning-paths/replace-vpn/build-policies/create-policy/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/replace-vpn/build-policies/create-list.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
