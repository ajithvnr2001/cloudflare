---
url: https://developers.cloudflare.com/changelog/post/2025-02-02-removed-meta-fields/
title: Removed unused meta fields from DNS records \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:55.127702+00:00
---

# Removed unused meta fields from DNS records · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-02-02-removed-meta-fields/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 2, 2025

## Removed unused meta fields from DNS records

[DNS](https://developers.cloudflare.com/dns/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare is removing five fields from the `meta` object of DNS records. These fields have been unused for more than a year and are no longer set on new records. This change may take up to four weeks to fully roll out.

The affected fields are:

  * the `auto_added` boolean
  * the `managed_by_apps` boolean and corresponding `apps_install_id`
  * the `managed_by_argo_tunnel` boolean and corresponding `argo_tunnel_id`



An example record returned from the API would now look like the following:

Updated API Responsejson
    
    
    {
    	"result": {
    		"id": "<ID>",
    		"zone_id": "<ZONE_ID>",
    		"zone_name": "example.com",
    		"name": "www.example.com",
    		"type": "A",
    		"content": "192.0.2.1",
    		"proxiable": true,
    		"proxied": false,
    		"ttl": 1,
    		"locked": false,
    		"meta": {
    			"auto_added": false,
    			"managed_by_apps": false,
    			"managed_by_argo_tunnel": false,
    			"source": "primary"
    		},
    		"comment": null,
    		"tags": [],
    		"created_on": "2025-03-17T20:37:05.368097Z",
    		"modified_on": "2025-03-17T20:37:05.368097Z"
    	},
    	"success": true,
    	"errors": [],
    	"messages": []
    }

For more guidance, refer to [Manage DNS records](https://developers.cloudflare.com/dns/manage-dns-records/).
