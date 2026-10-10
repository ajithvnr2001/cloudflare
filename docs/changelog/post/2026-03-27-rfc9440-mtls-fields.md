---
url: https://developers.cloudflare.com/changelog/post/2026-03-27-rfc9440-mtls-fields/
title: New RFC 9440 mTLS certificate fields in Workers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:41.409279+00:00
---

# New RFC 9440 mTLS certificate fields in Workers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-27-rfc9440-mtls-fields/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 27, 2026

## New RFC 9440 mTLS certificate fields in Workers

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Four new fields are now available on `request.cf.tlsClientAuth` in Workers for requests that include a mutual TLS (mTLS) client certificate. These fields encode the client certificate and its intermediate chain in [RFC 9440 ↗︎](https://www.rfc-editor.org/rfc/rfc9440) format — the same standard format used by the `Client-Cert` and `Client-Cert-Chain` HTTP headers — so your Worker can forward them directly to your origin without any custom parsing or encoding logic.

#### New fields

Field | Type | Description  
---|---|---  
`certRFC9440` | String | The client leaf certificate in RFC 9440 format (`:base64-DER:`). Empty if no client certificate was presented.  
`certRFC9440TooLarge` | Boolean | `true` if the leaf certificate exceeded 10 KB and was omitted from `certRFC9440`.  
`certChainRFC9440` | String | The intermediate certificate chain in RFC 9440 format as a comma-separated list. Empty if no intermediates were sent or if the chain exceeded 16 KB.  
`certChainRFC9440TooLarge` | Boolean | `true` if the intermediate chain exceeded 16 KB and was omitted from `certChainRFC9440`.  
  
#### Example: forwarding client certificate headers to your origin
    
    
    export default {
      async fetch(request) {
        const tls = request.cf.tlsClientAuth;
    
        // Only forward if cert was verified and chain is complete
        if (!tls || !tls.certVerified || tls.certRevoked || tls.certChainRFC9440TooLarge) {
          return new Response("Unauthorized", { status: 401 });
        }
    
        const headers = new Headers(request.headers);
        headers.set("Client-Cert", tls.certRFC9440);
        headers.set("Client-Cert-Chain", tls.certChainRFC9440);
    
        return fetch(new Request(request, { headers }));
      },
    };

For more information, refer to [Client certificate variables](https://developers.cloudflare.com/ssl/client-certificates/client-certificate-variables/#workers-variables) and [Mutual TLS authentication](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/).
