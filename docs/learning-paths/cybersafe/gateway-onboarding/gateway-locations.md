---
url: https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-locations/
title: Gateway locations \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:46.624490+00:00
---

# Gateway locations · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-locations/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Cybersafe

  4. /[Onboarding Cloudflare Gateway](https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/)
  5. /Gateway locations



# Gateway locations

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-locations/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAdd a DNS location

DNS locations are a collection of DNS endpoints which can be mapped to physical entities such as offices, homes, or data centers.

The fastest way to start filtering DNS queries from a location is by changing the DNS resolvers at the router.

## Add a DNS location

To add a DNS location to Gateway:

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Networks** > **Resolvers & Proxies** > **DNS locations**.
  2. Select **Add a location**.
  3. Choose a name for your DNS location.
  4. Choose at least one [DNS endpoint](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/dns/locations/#dns-endpoints) to resolve your organization's DNS queries.
  5. (Optional) Toggle the following settings: 
     * **Enable EDNS client subnet** sends a user's IP geolocation to authoritative DNS nameservers. [EDNS Client Subnet (ECS)](https://developers.cloudflare.com/cloudflare-one/glossary/?term=ecs) helps reduce latency by routing the user to the closest origin server. Cloudflare enables EDNS in a privacy preserving way by not sending the user's exact IP address but rather the first `/24` range of the larger range that contains their IP address. This `/24` range will share the same geographic location as the user's exact IP address.
     * **Set as Default DNS Location** sets this location as the default DoH endpoint for DNS queries.
  6. Select **Continue**.
  7. (Optional) Turn on source IP filtering for your configured endpoints, then add any source IPv4/IPv6 addresses to validate. 
     * Endpoint authentication is required for standard IPv4 addresses and optional for dedicated IPv4 addresses.
     * **DoH endpoint filtering & authentication** lets you restrict DNS resolution to only valid identities or user tokens in addition to IPv4/IPv6 addresses.
  8. Select **Continue**.
  9. Review the settings for your DNS location, then choose **Done**.



Captive portal limitation

Deploying Gateway DNS filtering using static IP addresses may prevent users from connecting to public Wi-Fi networks through captive portals. If users are experiencing connectivity issues related to captive portals, they should:

  1. Remove the static IP addresses from the device.
  2. Connect to the Wi-Fi network.
  3. Once the connection has been established, add the static IP addresses back.



To avoid this issue, use the [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/) to connect your devices to Cloudflare One.

[PreviousGateway connection methods](https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-connection-methods/)[NextUpdate local DNS resolver](https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-update-local-resolver/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/cybersafe/gateway-onboarding/gateway-locations.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
