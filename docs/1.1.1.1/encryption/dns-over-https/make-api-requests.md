---
url: https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/make-api-requests/
title: Make API requests to 1.1.1.1 over DoH \u00b7 Cloudflare 1.1.1.1 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:03.454656+00:00
---

# Make API requests to 1.1.1.1 over DoH · Cloudflare 1.1.1.1 docs

> Source: https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/make-api-requests/

  1. [Home](https://developers.cloudflare.com/)
  2. /[1.1.1.1 (DNS Resolver)](https://developers.cloudflare.com/1.1.1.1/)
  3. /…

[Encryption](https://developers.cloudflare.com/1.1.1.1/encryption/)

  4. /[DNS over HTTPS](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/)
  5. /Make API requests to 1.1.1.1



# Make API requests to 1.1.1.1

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/make-api-requests/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHTTP methodValid MIME typesSend multiple questions in a queryAuthenticationSupported TLS versionsReturn codes

Cloudflare offers a DNS over HTTPS resolver at:
    
    
    https://cloudflare-dns.com/dns-query

## HTTP method

Cloudflare's DNS over HTTPS (DoH) endpoint supports `POST` and `GET` for DNS wireformat, and `GET` for JSON format.

When making requests using `POST`, the DNS query is included as the message body of the HTTP request, and the MIME type (`application/dns-message`) is sent in the `Content-Type` request header. Cloudflare will use the message body of the HTTP request as sent by the client, so the message body should not be encoded.

When making requests using `GET`, the DNS query is encoded into the URL.

## Valid MIME types

If you use JSON format, set `application/dns-json`, and if you use DNS wireformat, use `application/dns-message`.

Refer to [DNS wireformat](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/make-api-requests/dns-wireformat/) and [JSON](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/make-api-requests/dns-json/) for cURL examples.

## Send multiple questions in a query

Each DNS query maps to exactly one HTTP request. To send multiple queries concurrently, use HTTP/2 or HTTP/3, which supports multiplexing multiple requests over a single connection.

HTTP/2 is the minimum recommended version of HTTP for use with DoH. This is not specific to 1.1.1.1, but rather how DoH operates per [RFC 8484 ↗︎](https://datatracker.ietf.org/doc/html/rfc8484#section-5.2).

Example request:
    
    
    curl --http2 --header "accept: application/dns-json" "https://one.one.one.one/dns-query?name=cloudflare.com" --next --http2 --header "accept: application/dns-json" "https://one.one.one.one/dns-query?name=example.com"

## Authentication

No authentication is required to send requests to this API.

## Supported TLS versions

Cloudflare's DNS over HTTPS resolver supports TLS 1.2 and TLS 1.3.

## Return codes

HTTP Status | Meaning  
---|---  
`400` | DNS query not specified or too small.  
`413` | DNS query is larger than maximum allowed DNS message size.  
`415` | Unsupported content type.  
`504` | Resolver timeout while waiting for the query response.  
  
[PreviousAbout DoH](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/)[NextDNS Wireformat](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/make-api-requests/dns-wireformat/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/1.1.1.1/encryption/dns-over-https/make-api-requests/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
