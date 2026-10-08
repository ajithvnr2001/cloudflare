---
url: https://developers.cloudflare.com/1.1.1.1/troubleshooting/
title: Troubleshooting DNS Resolver \u00b7 Cloudflare 1.1.1.1 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:05.132455+00:00
---

# Troubleshooting DNS Resolver · Cloudflare 1.1.1.1 docs

> Source: https://developers.cloudflare.com/1.1.1.1/troubleshooting/

  1. [Home](https://developers.cloudflare.com/)
  2. /[1.1.1.1 (DNS Resolver)](https://developers.cloudflare.com/1.1.1.1/)
  3. /Troubleshooting



# Troubleshooting

Last updated May 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/1.1.1.1/troubleshooting/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewName resolution issues Linux/macOS WindowsConnectivity and routing issues Linux/macOS WindowsDNS-over-TLS (DoT) troubleshooting Linux/macOS WindowsDNS-over-HTTPS (DoH) troubleshooting Linux/macOS WindowsCommon issues First hop failuresAdditional resources

This guide helps you diagnose and resolve common issues with Cloudflare's DNS Resolver. Before proceeding with manual troubleshooting steps, [verify your connection](https://developers.cloudflare.com/1.1.1.1/check/) to automatically gather relevant information.

## Name resolution issues

If a domain name is not resolving correctly, test DNS resolution against 1.1.1.1 and compare the result to another resolver (such as `8.8.8.8`). The CHAOS TXT queries (`id.server`) identify which Cloudflare server handled your request, which is useful when reporting issues.

### Linux/macOS
    
    
    # Test DNS resolution
    dig example.com @1.1.1.1
    dig example.com @1.0.0.1
    dig example.com @8.8.8.8
    
    # Check connected nameserver
    dig +short CHAOS TXT id.server @1.1.1.1
    dig +short CHAOS TXT id.server @1.0.0.1
    
    # Optional: Network information
    dig @ns3.cloudflare.com whoami.cloudflare.com txt +short

### Windows
    
    
    # Test DNS resolution
    nslookup example.com 1.1.1.1
    nslookup example.com 1.0.0.1
    nslookup example.com 8.8.8.8
    
    # Check connected nameserver
    nslookup -class=chaos -type=txt id.server 1.1.1.1
    nslookup -class=chaos -type=txt id.server 1.0.0.1
    
    # Optional: Network information
    nslookup -type=txt whoami.cloudflare.com ns3.cloudflare.com

Caution

The network information command reveals your IP address. Only include this in reports to Cloudflare if you are comfortable sharing this information.

For additional analysis, you can generate a [DNSViz ↗︎](http://dnsviz.net/) report for the domain in question.

## Connectivity and routing issues

If DNS queries time out or you cannot reach 1.1.1.1 at all, the problem may be a network routing issue between your device and Cloudflare. Run traceroutes to both resolver addresses to identify where packets are being dropped.

Before reporting connectivity issues:

  1. Search for existing reports from your country and ISP.
  2. Run traceroutes to both Cloudflare DNS resolvers.



### Linux/macOS
    
    
    # Basic connectivity tests
    traceroute 1.1.1.1
    traceroute 1.0.0.1
    
    # If reachable, check nameserver identity
    dig +short CHAOS TXT id.server @1.1.1.1
    dig +short CHAOS TXT id.server @1.0.0.1
    
    # TCP connection tests
    dig +tcp @1.1.1.1 id.server CH TXT
    dig +tcp @1.0.0.1 id.server CH TXT

### Windows
    
    
    # Basic connectivity tests
    tracert 1.1.1.1
    tracert 1.0.0.1
    
    # If reachable, check nameserver identity
    nslookup -class=chaos -type=txt id.server 1.1.1.1
    nslookup -class=chaos -type=txt id.server 1.0.0.1
    
    # TCP connection tests
    nslookup -vc -class=chaos -type=txt id.server 1.1.1.1
    nslookup -vc -class=chaos -type=txt id.server 1.0.0.1

## DNS-over-TLS (DoT) troubleshooting

DNS over TLS encrypts DNS queries using TLS on port `853`. If your DoT connection is not working, test TLS connectivity and then DNS resolution over TLS.

### Linux/macOS
    
    
    # Test TLS connectivity
    openssl s_client -connect 1.1.1.1:853
    openssl s_client -connect 1.0.0.1:853
    
    # Test DNS resolution over TLS
    kdig +tls @1.1.1.1 id.server CH TXT
    kdig +tls @1.0.0.1 id.server CH TXT

### Windows

Windows does not include a standalone DoT client. You can test TLS connectivity using OpenSSL after installing it manually.

## DNS-over-HTTPS (DoH) troubleshooting

DNS over HTTPS sends DNS queries as HTTPS requests. If your DoH connection is not working, test it by querying the Cloudflare DNS endpoint directly.

### Linux/macOS
    
    
    curl -H 'accept: application/dns-json' 'https://cloudflare-dns.com/dns-query?name=cloudflare.com&type=AAAA'

### Windows
    
    
    (Invoke-WebRequest -Uri 'https://cloudflare-dns.com/dns-query?name=cloudflare.com&type=AAAA').RawContent

## Common issues

### First hop failures

If your traceroute fails at the first hop (the first network device after your computer, usually your router), the issue is likely hardware-related. Your router may have a hardcoded route for `1.1.1.1` that conflicts with using it as a DNS resolver. When reporting this issue, include:

  * Router make and model
  * ISP name
  * Any relevant router configuration details



## Additional resources

  * [1.1.1.1 DNS Resolver homepage ↗︎](https://1.1.1.1)
  * [DNS over TLS documentation](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-tls/)
  * [Diagnostic tool ↗︎](https://one.one.one.one/help/)



[PreviousVerify connection](https://developers.cloudflare.com/1.1.1.1/check/)[NextTerms of use](https://developers.cloudflare.com/1.1.1.1/terms-of-use/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/1.1.1.1/troubleshooting.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
