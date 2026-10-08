---
url: https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/vyos/
title: VyOS \u00b7 Cloudflare WAN docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:30.409651+00:00
---

# VyOS · Cloudflare WAN docs

> Source: https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/vyos/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)
  3. /…

Configuration

  4. /Third-party integration
  5. /VyOS



# VyOS

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/vyos/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewNotesConfiguration parameters Phase 1 Phase 2Configuration template

This tutorial provides configuration information and a sample template for using a VyOS device with an IPsec configuration.

## Notes

  * `vti <NAME_OF_VTI_INTERFACE>` \- Specifies the virtual tunnel interface of the IPsec tunnel.
  * `esp-group <NAME_OF_ESP_GROUP>` \- Encrypts traffic through the tunnel using a particular ESP policy or profile.
  * `ike-group <NAME_OF_IKE_GROUP>` \- Exchanges keys using a particular IKE policy or profile.
  * The IP addresses of the IPsec tunnel interfaces on both ends of the tunnel should be a pair of private IP addresses (RFC 1918) on the same `/31` or `/30` subnet, specifying a point-to-point link.
  * The IPsec tunnel endpoint on this VyOS router is the `<IP_ADDR_OF_UPLINK_INTF_TO_INTERNET/WAN>`.
  * The IP address of the IPsec tunnel endpoint on the Cloudflare side is one of the anycast IP addresses assigned to your account, available in [Leased IPs ↗︎](https://dash.cloudflare.com/?to=/:account/ip-addresses/address-space).
  * This router is configured to initiate the IPsec tunnel connection.



## Configuration parameters

### Phase 1

  * **Encryption**

    * AES-GCM with 128-bit or 256-bit key length
  * **Integrity**

    * SHA512



### Phase 2

  * **Encryption**

    * AES-GCM with 128-bit or 256-bit key length
  * **Integrity**

    * SHA512
  * **PFS group**

    * DH group 20 (348-bit random ECP group)



## Configuration template
    
    
    set interfaces vti <name of the vti interface> address
    '<PRIVATE_IP_ADDRESS_OF_IPSEC_TUNNEL_INTERFACE>'
    set vpn ipsec esp-group <NAME_OF_ESP_GROUP> compression 'disable'
    set vpn ipsec esp-group <NAME_OF_ESP_GROUP> lifetime '86400'
    set vpn ipsec esp-group <NAME_OF_ESP_GROUP> mode 'tunnel'
    set vpn ipsec esp-group <NAME_OF_ESP_GROUP> pfs 'enable'
    set vpn ipsec esp-group <NAME_OF_ESP_GROUP> proposal 1 encryption 'aes256gcm128'
    set vpn ipsec esp-group <NAME_OF_ESP_GROUP> proposal 1 hash 'sha512'
    set vpn ipsec ike-group <NAME_OF_IKE_GROUP> close-action 'none'
    set vpn ipsec ike-group <NAME_OF_IKE_GROUP> dead-peer-detection action 'restart'
    set vpn ipsec ike-group <NAME_OF_IKE_GROUP> dead-peer-detection interval '30'
    set vpn ipsec ike-group <NAME_OF_IKE_GROUP> dead-peer-detection timeout '120'
    set vpn ipsec ike-group <NAME_OF_IKE_GROUP> ikev2-reauth 'no'
    set vpn ipsec ike-group <NAME_OF_IKE_GROUP> key-exchange 'ikev2'
    set vpn ipsec ike-group <NAME_OF_IKE_GROUP> lifetime '28800'
    set vpn ipsec ike-group <NAME_OF_IKE_GROUP> mobike 'disable'
    set vpn ipsec ike-group <NAME_OF_IKE_GROUP> proposal 1 dh-group '20'
    set vpn ipsec ike-group <NAME_OF_IKE_GROUP> proposal 1 encryption 'aes256gcm128'
    set vpn ipsec ike-group <NAME_OF_IKE_GROUP> proposal 1 hash 'sha512'
    set vpn ipsec ipsec-interfaces interface '<UPLINK_INTF_TO_INTERNET/WAN>'
    set vpn ipsec logging log-level '2'
    set vpn ipsec options disable-route-autoinstall
    set vpn ipsec site-to-site peer <CF_ANYCAST_IP> authentication id '<IPSEC_ID_STRING_IN_RESULT_OF_PSK_KEY-GEN_VIA_CF_API>'
    set vpn ipsec site-to-site peer <CF_ANYCAST_IP> authentication pre-shared-secret '<PSK_KEY_STRING_GENERATED_VIA_CF_API>'
    set vpn ipsec site-to-site peer <CF_ANYCAST_IP> authentication remote-id '<CF_ANYCAST_IP>'
    set vpn ipsec site-to-site peer <CF_ANYCAST_IP> connection-type 'initiate'
    set vpn ipsec site-to-site peer <CF_ANYCAST_IP> ike-group '<NAME_OF_IKE_GROUP>'
    set vpn ipsec site-to-site peer <CF_ANYCAST_IP> ikev2-reauth 'no'
    set vpn ipsec site-to-site peer <CF_ANYCAST_IP> local-address '<IP_ADDR_OF_UPLINK_INTF_TO_INTERNET/WAN>'
    set vpn ipsec site-to-site peer <CF_ANYCAST_IP> vti bind '<NAME_OF_VTI_INTERFACE>'
    set vpn ipsec site-to-site peer <CF_ANYCAST_IP> vti esp-group '<NAME_OF_ESP_GROUP>'

[PreviousVelocloud](https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/velocloud/)[NextYamaha RTX Router](https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/yamaha/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-wan/configuration/third-party/vyos.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
