---
url: https://developers.cloudflare.com/spectrum/about/static-ip/
title: Static IP \u00b7 Cloudflare Spectrum docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:32.568803+00:00
---

# Static IP · Cloudflare Spectrum docs

> Source: https://developers.cloudflare.com/spectrum/about/static-ip/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Spectrum](https://developers.cloudflare.com/spectrum/)
  3. /About
  4. /Static IP



# Static IP

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/spectrum/about/static-ip/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUse static IPs with SpectrumCheck your static IPs

When you create a Spectrum application, you are assigned an IP. These IPs are normally dynamic, meaning that they will change over time. But, for instance, if you want to set up WAF custom rules for specific IPs, you may want to use static IPs.

A static IP, like a physical street address can tell other computers or servers on the Internet where a specific computer is located or connected. This makes the device easier to find on the network, since the IP will not change.

With static IPs, Cloudflare commits to never changing the IP address of a client's domain resolved at the Cloudflare global network. For example, `www.example.com` will always resolve and accept traffic sent to `198.51.100.10`. No other customer will be hosted on that IP.

Importantly, the static IP is associated with the DNS name, not with each individual Spectrum application. This means that all Spectrum apps using the same hostname will share the same static IP.

## Use static IPs with Spectrum

Availability

Static IP is an Enterprise feature that does not come standard with Spectrum. Contact your account team to request access.

Once you get your static IP from Cloudflare, you can use it via API, just like [BYOIP](https://developers.cloudflare.com/byoip/). For the moment, there is still no UI available for this feature.

When creating a Spectrum application through the API, specify the static IPs that you have been provided. See, for instance, the API example below that creates an application routing traffic through Cloudflare’s HTTP pipeline.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Zone Settings Write`

Create Spectrum application using a name for the originbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/spectrum/apps" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"protocol": "tcp/80",
    		"dns": {
    				"type": "ADDRESS",
    				"name": "www.example.com"
    		},
    		"origin_direct": [
    				"tcp://192.0.2.1:80"
    		],
    		"tls": "off",
    		"traffic_type": "http",
    		"edge_ips": {
    				"type": "static",
    				"ips": [
    						"198.51.100.10",
    						"2001:DB8::1"
    				]
    		}
    	}'

## Check your static IPs

You can find your leased static IPs for Spectrum on the dashboard under [**Address space** > **Leased IPs** ↗︎](https://dash.cloudflare.com/?to=/:account/ip-addresses/address-space).

[PreviousFTP](https://developers.cloudflare.com/spectrum/about/ftp/)[NextGet started](https://developers.cloudflare.com/spectrum/get-started/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/spectrum/about/static-ip.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
