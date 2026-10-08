---
url: https://developers.cloudflare.com/spectrum/get-started/
title: Get started \u00b7 Cloudflare Spectrum docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:32.846905+00:00
---

# Get started · Cloudflare Spectrum docs

> Source: https://developers.cloudflare.com/spectrum/get-started/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Spectrum](https://developers.cloudflare.com/spectrum/)
  3. /Get started



# Get started

Last updated Jun 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/spectrum/get-started/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate a Spectrum application using an IP addressCreate a Spectrum application using a CNAME recordCreate a Spectrum application using a load balancerCreate a Spectrum application using a virtual network origin Before you beginView traffic

Spectrum is available on all paid plans. Pro and Business support selected protocols only, whereas Enterprise supports all TCP and UDP based traffic. Refer to [Configuration options](https://developers.cloudflare.com/spectrum/reference/configuration-options/) for more configuration details.

To create a Spectrum application, you can either use an IP address, a CNAME Record or a load balancer. Independently of the method you use, you can create the application through the dashboard or via [API](https://developers.cloudflare.com/api/resources/spectrum/subresources/apps/methods/list/).

Certain fields in Spectrum request and response bodies require an Enterprise plan. Refer to the [Settings by plan](https://developers.cloudflare.com/spectrum/reference/settings-by-plan/) page for more details.

## Create a Spectrum application using an IP address

To create a Spectrum application using an IP address, Cloudflare normally assigns you an arbitrary IP from Cloudflare’s IP pool to your application. If you want to use your own IP addresses, you can use [BYOIP](https://developers.cloudflare.com/spectrum/about/byoip/) or you can also use a [Static IP](https://developers.cloudflare.com/spectrum/about/static-ip/). In these two last cases, you need to create your Spectrum application through the API, as these features are not available via dash. When using the API, the field `origin_direct` takes as input the IP address.

Add your application via Dashboard

  1. In the Cloudflare dashboard, go to the **Spectrum** page.

[ Go to **Spectrum** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/spectrum)
  2. Select **Create an Application**. If this is your first time using Spectrum, the **Create an Application** modal appears.

  3. Select your **Application Type**.

  4. Under **Domain** , enter the domain that will use Spectrum.

  5. Under **Edge Port** , enter the port Cloudflare should use for your application.

  6. Under **Origin** , enter your application's origin IP and port.

  7. If your application requires the client IP and supports [Proxy Protocol ↗︎](https://www.haproxy.com/blog/haproxy/proxy-protocol/), enable **Proxy Protocols**. Proxy Protocol is a method for a proxy like Cloudflare to send the client IP to the origin application.

  8. Select **Add**.




Add your application via API

Below is a curl example and the associated data being posted to the API.

**API example:**

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Zone Settings Write`

Create Spectrum application using a name for the originbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/spectrum/apps" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"protocol": "tcp/22",
    		"dns": {
    				"type": "CNAME",
    				"name": "ssh.example.com"
    		},
    		"origin_direct": [
    				"tcp://192.0.2.1:22"
    		],
    		"proxy_protocol": "off",
    		"ip_firewall": true,
    		"tls": "full",
    		"edge_ips": {
    				"type": "dynamic",
    				"connectivity": "all"
    		},
    		"traffic_type": "direct",
    		"argo_smart_routing": true
    	}'

**Example data:**
    
    
    {
    	"success": true,
    	"errors": [],
    	"messages": [],
    	"result": {
    		"id": "ea95132c15732412d22c1476fa83f27a",
    		"protocol": "tcp/22",
    		"dns": {
    			"type": "CNAME",
    			"name": "ssh.example.com"
    		},
    		"origin_direct": ["tcp://192.0.2.1:22"],
    		"proxy_protocol": "off",
    		"ip_firewall": true,
    		"tls": "full",
    		"edge_ips": {
    			"type": "dynamic",
    			"connectivity": "all"
    		},
    		"traffic_type": "direct",
    		"argo_smart_routing": true,
    		"created_on": "2014-01-02T02:20:00Z",
    		"modified_on": "2014-01-02T02:20:00Z"
    	}
    }

## Create a Spectrum application using a CNAME record

To create a Spectrum application using a CNAME record, you will need to create a [CNAME record ↗︎](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/) on your Cloudflare hosted zone that points to your origin's hostname. This is required to resolve to your hostname origin. Refer to [Create DNS records](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/#create-dns-records), for more information. When using a CNAME as an origin, note that Cloudflare needs to be authoritative for that zone. When using the API, the `origin_dns` field takes as input the CNAME record.

Add your application via Dashboard

  1. In the Cloudflare dashboard, go to the **Spectrum** page.

[ Go to **Spectrum** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/spectrum)
  2. Select **Create an Application**. If this is your first time using Spectrum, the **Create an Application** modal appears.

  3. Select your **Application Type**.

  4. Under **Domain** , enter the domain that will use Spectrum.

  5. Under **Edge Port** , enter the port Cloudflare should use for your application.

  6. Under **Origin** , enter your `CNAME` record name.

  7. Select **Add**.




Add your application via API

Below is a curl example and the associated data being posted to the API.

**API example:**

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Zone Settings Write`

Create Spectrum application using a name for the originbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/spectrum/apps" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"dns": {
    				"type": "CNAME",
    				"name": "spectrum-cname.example.com"
    		},
    		"ip_firewall": false,
    		"protocol": "tcp/22",
    		"proxy_protocol": "off",
    		"tls": "off",
    		"origin_dns": {
    				"name": "cname-to-origin.example.com",
    				"ttl": 1200
    		},
    		"origin_port": 22
    	}'

**Example data:**
    
    
    {
    	"dns": {
    		"type": "CNAME",
    		"name": "spectrum-cname.example.com"
    	},
    	"ip_firewall": false,
    	"protocol": "tcp/22",
    	"proxy_protocol": "off",
    	"tls": "off",
    	"origin_dns": {
    		"name": "cname-to-origin.example.com",
    		"ttl": 1200
    	},
    	"origin_port": 22
    }

## Create a Spectrum application using a load balancer

To create a Spectrum application using a load balancer, you will need to generate a load balancer from the dashboard or via the API. Refer to the [Load Balancing documentation](https://developers.cloudflare.com/load-balancing/additional-options/spectrum/#1-configure-your-load-balancer) for more details.

Note

To prevent issues with DNS resolution for a Spectrum application, do not use the same Spectrum hostname as a current Load Balancing hostname.

Add your application via Dashboard

  1. In the Cloudflare dashboard, go to the **Spectrum** page.

[ Go to **Spectrum** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/spectrum)
  2. Select **Create an Application**. If this is your first time using Spectrum, the **Create an Application** modal appears.

  3. Select your **[Application Type](https://developers.cloudflare.com/spectrum/reference/configuration-options/#application-type)**.

  4. Under **Domain** , enter the domain that will use Spectrum.

  5. Under **Edge Port** , enter the port Cloudflare should use for your application.

  6. Under **Origin** , select **Load Balancer**.

  7. Select the load balancer you want to use from the dropdown. Disabled load balancers will not show on the **Load Balancer** menu.

  8. Select **Add**.




Add your application via API

Below is a curl example and the associated data being posted to the API.

**API example:**

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Zone Settings Write`

Create Spectrum application using a name for the originbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/spectrum/apps" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"dns": {
    				"type": "CNAME",
    				"name": "spectrum-cname.example.com"
    		},
    		"ip_firewall": false,
    		"protocol": "tcp/22",
    		"proxy_protocol": "off",
    		"tls": "off",
    		"origin_dns": {
    				"name": "cname-to-origin.example.com",
    				"ttl": 1200
    		},
    		"origin_port": 22
    	}'

**Example data:**
    
    
    {
      "dns": {
        "type": "CNAME",
        "name": "spectrum-cname.example.com"
      },
      "ip_firewall": false,
      "protocol": "tcp/22",
      "proxy_protocol": "off",
      "tls": "off",
      "origin_dns": {
        "name": "cname-to-origin.example.com",
        "ttl": 1200
      },
      "origin_port": 22
    }

## Create a Spectrum application using a virtual network origin

To proxy TCP or UDP traffic to an origin on your private network, attach a Cloudflare Tunnel [virtual network](https://developers.cloudflare.com/cloudflare-one/networks/virtual-networks/) to a Spectrum application. Spectrum routes traffic through the connector (Cloudflare Tunnel or Cloudflare WAN connection) associated with that virtual network. This provides an alternative to the previous pattern of putting a load balancer in front of a private origin.

Virtual network origins are only supported for TCP and UDP applications. The origin must be a single private IP routable within the specified virtual network. Port ranges, hostname origins (`origin_dns`), and multiple addresses in `origin_direct` are not supported. [Proxy Protocol](https://developers.cloudflare.com/spectrum/how-to/enable-proxy-protocol/) is not currently supported, so `proxy_protocol` must be set to `off`. For details on validation errors, refer to [Error codes](https://developers.cloudflare.com/spectrum/reference/error-codes/).

For a primer on virtual networks, refer to [Virtual networks](https://developers.cloudflare.com/cloudflare-one/networks/virtual-networks/).

### Before you begin

Set up the virtual network and a route covering your origin IP before creating the Spectrum application:

  * Create a virtual network and a Cloudflare Tunnel that carries it by following [Manage virtual networks](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/).
  * Attach a route covering your origin's private IP to the tunnel by following [Connect an IP/CIDR](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/).



For Cloudflare WAN (formerly Magic WAN) as the connector, refer to [Get started with Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/get-started/) for setting up tunnel endpoints and routes.

Add your application via Dashboard

  1. In the Cloudflare dashboard, go to the **Spectrum** page.

[ Go to **Spectrum** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/spectrum)
  2. Select **Create an Application**.

  3. Under **Application Type** , select **TCP** or **UDP**.

  4. Under **Domain** , enter the domain that will use Spectrum.

  5. Under **Edge Port** , enter the port Cloudflare should use for your application.

  6. Under **Origin** , select **Virtual Network**.

  7. Under **Virtual Network** , select the virtual network that contains your origin.

  8. Under **IP** , enter the private IP address of your origin.

  9. Under **Port** , enter a single port (port ranges are not supported).

  10. Select **Add**.




Add your application via API

Below is a curl example and the associated data being posted to the API.

**API example:**

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Zone Settings Write`

Create Spectrum application using a name for the originbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/spectrum/apps" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"protocol": "tcp/22",
    		"dns": {
    				"type": "CNAME",
    				"name": "ssh.example.com"
    		},
    		"origin_direct": [
    				"tcp://10.0.0.5:22"
    		],
    		"virtual_network_id": "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
    		"proxy_protocol": "off",
    		"ip_firewall": true,
    		"tls": "off",
    		"edge_ips": {
    				"type": "dynamic",
    				"connectivity": "all"
    		},
    		"traffic_type": "direct"
    	}'

Set `origin_direct` to the private IP of your origin and `virtual_network_id` to the ID of the virtual network that the IP is routable within. You can list virtual networks for your account with the [List virtual networks](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/virtual_networks/methods/list/) endpoint.

**Example data:**
    
    
    {
    	"success": true,
    	"errors": [],
    	"messages": [],
    	"result": {
    		"id": "ea95132c15732412d22c1476fa83f27a",
    		"protocol": "tcp/22",
    		"dns": {
    			"type": "CNAME",
    			"name": "ssh.example.com"
    		},
    		"origin_direct": ["tcp://10.0.0.5:22"],
    		"virtual_network_id": "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
    		"proxy_protocol": "off",
    		"ip_firewall": true,
    		"tls": "off",
    		"edge_ips": {
    			"type": "dynamic",
    			"connectivity": "all"
    		},
    		"traffic_type": "direct",
    		"created_on": "2014-01-02T02:20:00Z",
    		"modified_on": "2014-01-02T02:20:00Z"
    	}
    }

## View traffic

You can now proxy traffic through Cloudflare without additional configuration. As you run traffic through Cloudflare, you will see the last minute of traffic from **Spectrum** in the dashboard.

If you have any feedback, please [let us know ↗︎](https://community.cloudflare.com/c/website-application-performance/spectrum/48).

[PreviousStatic IP](https://developers.cloudflare.com/spectrum/about/static-ip/)[NextEnable Proxy protocol](https://developers.cloudflare.com/spectrum/how-to/enable-proxy-protocol/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/spectrum/get-started.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
