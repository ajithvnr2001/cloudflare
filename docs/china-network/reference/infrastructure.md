---
url: https://developers.cloudflare.com/china-network/reference/infrastructure/
title: Infrastructure \u00b7 Cloudflare China Network docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:56.886858+00:00
---

# Infrastructure · Cloudflare China Network docs

> Source: https://developers.cloudflare.com/china-network/reference/infrastructure/

  1. [Home](https://developers.cloudflare.com/)
  2. /[China Network](https://developers.cloudflare.com/china-network/)
  3. /Reference
  4. /Infrastructure



# Infrastructure

Last updated Apr 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/china-network/reference/infrastructure/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewChina data centers Network IP addresses

## China data centers

For up-to-date information, refer to the [Cloudflare China Network ↗︎](https://www.cloudflare.com/china-network/) page.

### Network IP addresses

Cloudflare publishes a list of IP addresses for JD Cloud data centers, used by Cloudflare when connecting to the origin networks of customers to retrieve assets. These addresses are not the same IP addresses returned to website visitors as part of DNS resolution.

You can obtain the list of JD Cloud data center IP addresses via Cloudflare API. Use the [Cloudflare/JD Cloud IP Details](https://developers.cloudflare.com/api/resources/ips/methods/list/) operation with the `networks=jdcloud` query string parameter:

Cloudflare/JD Cloud IP Detailsbash
    
    
    curl "https://api.cloudflare.com/client/v4/ips?networks=jdcloud" \
    	--request GET
    
    
    {
    	"result": {
    		"ipv4_cidrs": [
    			// (...)
    		],
    		"ipv6_cidrs": [
    			// (...)
    		],
    		"jdcloud_cidrs": [
    			// (...)
    		],
    		"etag": "<ETAG>"
    	},
    	"success": true,
    	"errors": [],
    	"messages": []
    }

The `jdcloud_cidrs` array lists the IP addresses of JD Cloud data centers.

Cloudflare will add new IP addresses to this list 30 days in advance before connecting from those IP addresses to an origin server. If you are using the China Network on JD Cloud, you should update your firewalls to reflect any IP address changes at least once every 30 days.

[PreviousAvailable products and features](https://developers.cloudflare.com/china-network/reference/available-products/)[NextVideos](https://developers.cloudflare.com/china-network/videos/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/china-network/reference/infrastructure.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
