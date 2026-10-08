---
url: https://developers.cloudflare.com/workers-vpc/configuration/tunnel/hardware-requirements/
title: Hardware requirements \u00b7 Cloudflare Workers VPC
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:07.334599+00:00
---

# Hardware requirements · Cloudflare Workers VPC

> Source: https://developers.cloudflare.com/workers-vpc/configuration/tunnel/hardware-requirements/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers VPC](https://developers.cloudflare.com/workers-vpc/)
  3. /…

Configuration

  4. /[Cloudflare Tunnel](https://developers.cloudflare.com/workers-vpc/configuration/tunnel/)
  5. /Hardware requirements



# Hardware requirements

Last updated Apr 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers-vpc/configuration/tunnel/hardware-requirements/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRecommendationsCapacity calculatorScaling considerationsNext steps

## Recommendations

For production use cases, we recommend the following baseline configuration:

  * Run a cloudflared replica on two dedicated host machines per network location. Using two hosts enables server-side redundancy. See [tunnel availability and replicas](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/) for setup instructions.
  * Size each host with minimum 4GB of RAM and 4 CPU cores.



This setup is usually sufficient to handle traffic from small-medium sized applications. The actual amount of resources used by cloudflared will depend on many variables, including the number of requests per second, bandwidth, network path, and hardware. If usage increases beyond your existing tunnel capacity, you can scale your tunnel by increasing the hardware allocated to the cloudflared hosts.

## Capacity calculator

To estimate tunnel capacity requirements for your deployment, refer to the [tunnel capacity calculator in the Zero Trust documentation](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/system-requirements/).

## Scaling considerations

Monitor tunnel performance and scale accordingly:

  * **CPU utilization** : Keep below 70% average usage
  * **Memory usage** : Maintain headroom for traffic spikes
  * **Network bandwidth** : Ensure adequate throughput for peak loads
  * **Connection count** : Scale cloudflared vertically when approaching capacity limits



## Next steps

  * Configure [tunnel deployment](https://developers.cloudflare.com/workers-vpc/configuration/tunnel/)
  * Set up [high availability](https://developers.cloudflare.com/workers-vpc/configuration/tunnel/) with multiple replicas



[PreviousOverview](https://developers.cloudflare.com/workers-vpc/configuration/tunnel/)[NextWrangler commands](https://developers.cloudflare.com/workers-vpc/reference/wrangler-commands/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers-vpc/configuration/tunnel/hardware-requirements.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
