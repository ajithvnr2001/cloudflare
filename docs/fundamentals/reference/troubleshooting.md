---
url: https://developers.cloudflare.com/fundamentals/reference/troubleshooting/
title: Troubleshooting \u00b7 Cloudflare Fundamentals docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:27.020436+00:00
---

# Troubleshooting · Cloudflare Fundamentals docs

> Source: https://developers.cloudflare.com/fundamentals/reference/troubleshooting/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)
  3. /Reference
  4. /Troubleshooting



# Troubleshooting

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/fundamentals/reference/troubleshooting/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewError messagesBehaviorCloudflareGeneral resourcesIs Cloudflare attacking me

When you [set up Cloudflare](https://developers.cloudflare.com/fundamentals/account/), you may experience the following issues or error messages.

## Error messages

  * [`ERR_TOO_MANY_REDIRECTS`](https://developers.cloudflare.com/ssl/troubleshooting/too-many-redirects/)
  * [`525` or `526` errors](https://developers.cloudflare.com/ssl/troubleshooting/too-many-redirects/)
  * [Cannot add DNS records with the same name](https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/records-with-same-name/)
  * [`ERR_SSL_VERSION_OR_CIPHER_MISMATCH` or `SSL_ERROR_NO_CYPHER_OVERLAP`](https://developers.cloudflare.com/ssl/troubleshooting/version-cipher-mismatch/)
  * [`DNS_PROBE_FINISHED_NXDOMAIN`](https://developers.cloudflare.com/dns/troubleshooting/dns-probe-finished-nxdomain/)
  * [Record exposing origin server IP address](https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/exposed-ip-address/)
  * [Mixed content errors](https://developers.cloudflare.com/ssl/troubleshooting/mixed-content-errors/)
  * [SSL errors in appear in my browser](https://developers.cloudflare.com/ssl/troubleshooting/general-ssl-errors/)



## Behavior

  * [Why are Cloudflare's IPs in my origin web server logs?](https://developers.cloudflare.com/support/troubleshooting/restoring-visitor-ips/restoring-original-visitor-ips/)
  * Is Cloudflare attacking me?
  * [Cannot add domain to Cloudflare](https://developers.cloudflare.com/dns/zone-setups/troubleshooting/cannot-add-domain/)
  * [My domain’s email stopped working](https://developers.cloudflare.com/dns/troubleshooting/email-issues/)
  * [Why is my site served over HTTP instead of HTTPS?](https://developers.cloudflare.com/ssl/edge-certificates/encrypt-visitor-traffic/)
  * [SSL is not working for my second-level subdomain, such as `dev.www.example.com`](https://developers.cloudflare.com/ssl/troubleshooting/general-ssl-errors/#only-some-of-your-subdomains-return-ssl-errors)
  * [Why was my domain deleted from Cloudflare?](https://developers.cloudflare.com/dns/zone-setups/troubleshooting/domain-deleted/)



## Cloudflare

  * [Gather information to troubleshoot site issues](https://developers.cloudflare.com/support/troubleshooting/general-troubleshooting/gathering-information-for-troubleshooting-sites/)
  * [Contact Cloudflare support](https://developers.cloudflare.com/support/contacting-cloudflare-support/)
  * [Manage email notifications](https://developers.cloudflare.com/fundamentals/user-profiles/customize-account/#notifications)



## General resources

  * [DNS FAQ](https://developers.cloudflare.com/dns/faq/)
  * [SSL/TLS FAQ](https://developers.cloudflare.com/ssl/faq/)



## Is Cloudflare attacking me

Two common scenarios falsely lead to the perception that Cloudflare is attacking your site:

  * Unless you [restore the original visitor IP addresses](https://developers.cloudflare.com/support/troubleshooting/restoring-visitor-ips/restoring-original-visitor-ips/), Cloudflare IP addresses appear in your server logs for all proxied requests.
  * The attacker is spoofing Cloudflare's IPs. Cloudflare only [sends traffic to your origin web server over a few specific ports](https://developers.cloudflare.com/fundamentals/reference/network-ports/) unless you use [Cloudflare Spectrum](https://developers.cloudflare.com/spectrum/).



Ideally, because Cloudflare is a reverse proxy, your hosting provider observes attack traffic connecting from [Cloudflare IP addresses ↗︎](https://www.cloudflare.com/ips/). In contrast, if you notice connections from IP addresses that do not belong to Cloudflare, the attack is direct to your origin web server. Cloudflare cannot stop attacks directly to your origin IP address because the traffic bypasses Cloudflare's network.

Note

If an attacker is directly targeting your origin web server, refer to [Proactive DDoS defense best practices](https://developers.cloudflare.com/ddos-protection/best-practices/proactive-defense/).

[PreviousSDK ecosystem support policy](https://developers.cloudflare.com/fundamentals/reference/sdk-ecosystem-support-policy/)[Next/cdn-cgi/ endpoint](https://developers.cloudflare.com/fundamentals/reference/cdn-cgi-endpoint/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/fundamentals/reference/troubleshooting.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
