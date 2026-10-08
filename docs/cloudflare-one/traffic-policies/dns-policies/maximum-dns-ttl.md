---
url: https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/maximum-dns-ttl/
title: Maximum DNS TTL \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:07.606742+00:00
---

# Maximum DNS TTL · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/maximum-dns-ttl/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Traffic policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

  4. /[DNS policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/)
  5. /Maximum DNS TTL



# Maximum DNS TTL

Last updated Jul 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/maximum-dns-ttl/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow it worksConfigure the account-level maximum TTLConfigure a per-location maximum TTLDNS log fields

Set a maximum time-to-live (TTL) for DNS responses returned by Gateway. When an upstream DNS record has a TTL that exceeds the configured maximum, Gateway caps the TTL to the value you specify. Lower values ensure that DNS policy changes - such as blocking a newly identified malicious domain - take effect faster across all clients, at the cost of increased query volume from reduced caching.

The maximum TTL cap only applies to upstream-derived DNS answers for allowed queries. Gateway-generated responses (blocks, overrides, safe-search answers) are not affected because they already use a short default TTL.

## How it works

Gateway applies a tiered TTL hierarchy. The most specific setting takes precedence:

  1. If the DNS location has a per-location override, that value is used.
  2. If the location inherits its setting, the account-level maximum TTL is used.
  3. If no maximum TTL is configured at any level, upstream TTL values pass through unchanged.



The valid range for any maximum TTL value is **60 to 36,000 seconds** (1 minute to 10 hours).

## Configure the account-level maximum TTL

The account-level setting applies to all DNS locations that do not have a per-location override.

  1. In [Zero Trust ↗︎](https://dash.cloudflare.com/one), go to **Traffic Policies** > **Traffic Settings**.
  2. Under **Proxy and inspection** , find the **Configure time-to-live for DNS resolution** section.
  3. Enter a value in seconds (between 60 and 36,000).
  4. Select **Save**.


    
    
    curl --request PUT \
      https://api.cloudflare.com/client/v4/accounts/{account_id}/gateway/configuration \
      --header "Authorization: Bearer {api_token}" \
      --header "Content-Type: application/json" \
      --data '{
        "settings": {
          "max_ttl_secs": 3600
        }
      }'

To remove the account-level cap (allow upstream TTLs to pass through), omit the `max_ttl_secs` field or set it to `null`.

## Configure a per-location maximum TTL

Each [DNS location](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-proxies/) can override the account-level setting. The per-location setting supports three modes:

Mode | Behavior  
---|---  
**Respect account-level setting** (`inherit`) | Uses whatever value is configured at the account level. This is the default for new locations.  
**Do not set max value** (`disabled`) | Disables the maximum TTL cap for this location, even if one is configured at the account level. Upstream TTL values pass through unchanged.  
**Custom** (`override`) | Sets a location-specific maximum TTL that overrides the account-level value. Requires a `ttl_secs` value between 60 and 36,000.  
  
  1. In [Zero Trust ↗︎](https://dash.cloudflare.com/one), go to **Networks** > **Resolvers & Proxies** > **DNS locations**.
  2. Select a location, or create a new one.
  3. In the **DNS Endpoints** tab, find the **Configure time-to-live for this location** section.
  4. Choose one of: 
     * **Respect account-level setting** \- inherits the account-level TTL cap.
     * **Do not set max value** \- disables the TTL cap for this location.
     * **Custom** \- enter a TTL value in seconds.
  5. Select **Save**.


    
    
    # Inherit account-level setting (default)
    curl --request PUT \
      https://api.cloudflare.com/client/v4/accounts/{account_id}/gateway/locations/{location_id} \
      --header "Authorization: Bearer {api_token}" \
      --header "Content-Type: application/json" \
      --data '{
        "max_ttl": {
          "mode": "inherit"
        }
      }'
    
    
    # Disable max TTL for this location
    curl --request PUT \
      https://api.cloudflare.com/client/v4/accounts/{account_id}/gateway/locations/{location_id} \
      --header "Authorization: Bearer {api_token}" \
      --header "Content-Type: application/json" \
      --data '{
        "max_ttl": {
          "mode": "disabled"
        }
      }'
    
    
    # Override with a custom value
    curl --request PUT \
      https://api.cloudflare.com/client/v4/accounts/{account_id}/gateway/locations/{location_id} \
      --header "Authorization: Bearer {api_token}" \
      --header "Content-Type: application/json" \
      --data '{
        "max_ttl": {
          "mode": "override",
          "ttl_secs": 3600
        }
      }'

## DNS log fields

When a maximum TTL is active, two additional fields appear in Gateway DNS logs:

Field | Description  
---|---  
`upstream_record_ttls` | The original TTL values from the upstream DNS response, before any cap was applied.  
`applied_max_ttl` | The maximum TTL value that Gateway applied to the response. If no cap was applied, this field is absent.  
  
These fields are visible in the DNS logs column picker under the **DNS Response Details** group in the dashboard, and in Logpush datasets.

[PreviousTimed DNS policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/timed-policies/)[NextOverview](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/traffic-policies/dns-policies/maximum-dns-ttl.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
