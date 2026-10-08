---
url: https://developers.cloudflare.com/api/resources/radar/subresources/post_quantum/subresources/tls/methods/support/
title: Check Post-Quantum TLS support | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:26:34.397836+00:00
---

# Check Post-Quantum TLS support | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/radar/subresources/post_quantum/subresources/tls/methods/support/

[API Reference](https://developers.cloudflare.com/api)

[Radar](https://developers.cloudflare.com/api/resources/radar)

[Post Quantum](https://developers.cloudflare.com/api/resources/radar/subresources/post_quantum)

[TLS](https://developers.cloudflare.com/api/resources/radar/subresources/post_quantum/subresources/tls)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Check Post-Quantum TLS support

GET/radar/post_quantum/tls/support

Tests whether a hostname or IP address supports Post-Quantum (PQ) TLS key exchange. Returns information about the negotiated key exchange algorithm, whether it uses PQ cryptography, and any detected TLS implementation bugs (Split ClientHello, HRR failure, etc.).

##### Security

API Token

The preferred authorization scheme for interacting with the Cloudflare API. [Create a token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/).

**Example:**`Authorization: Bearer Sn3lZJTBX6kkg7OdcBUAxOO963GEIyGQqnFTOFYY`

API Email + API Key

The previous authorization scheme for interacting with the Cloudflare API, used in conjunction with a Global API key.

**Example:**`X-Auth-Email: user@example.com`

The previous authorization scheme for interacting with the Cloudflare API. When possible, use API tokens instead of Global API keys.

**Example:**`X-Auth-Key: 144c9defac04969c7bfad8efaa8ea194`

##### Accepted Permissions (at least one required)

`User Details Write``User Details Read`

##### Query ParametersExpand Collapse 

host: string

Hostname or IP address to test for Post-Quantum TLS support, optionally with port (defaults to 443).

minLength1

##### ReturnsExpand Collapse 

result: object { bugs, host, kex, 2 more } 

bugs: object { hrrFailure, splitClientHello, unknownKeyshare } 

hrrFailure: boolean

Server sends a HelloRetryRequest but fails to complete the handshake after the client sends the second ClientHello. Often caused by non-compliant TLS 1.3 implementations on shared hosting providers.

splitClientHello: boolean

Server rejects fragmented ClientHello caused by large PQ keyshare, but accepts classical (non-PQ) handshakes. Typically caused by middleboxes or firewalls that cannot reassemble split TLS ClientHello messages.

unknownKeyshare: boolean

Server cannot handle an unknown key exchange algorithm in the ClientHello keyshare extension. Compliant servers should respond with HelloRetryRequest for a supported algorithm.

host: string

The host that was tested

kex: number

TLS CurveID of the negotiated key exchange

kexName: string

Human-readable name of the key exchange algorithm

pq: boolean

Whether the negotiated key exchange uses Post-Quantum cryptography (specifically X25519MLKEM768)

success: boolean

### Check Post-Quantum TLS support

HTTP

HTTP

HTTP

TypeScript

TypeScript

Python

Python

Go

Go

Terraform

Terraform
    
    
    curl https://api.cloudflare.com/client/v4/radar/post_quantum/tls/support \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

200 example
    
    
    {
      "result": {
        "bugs": {
          "hrrFailure": true,
          "splitClientHello": true,
          "unknownKeyshare": true
        },
        "host": "host",
        "kex": 0,
        "kexName": "kexName",
        "pq": true
      },
      "success": true
    }

##### Returns Examples

200 example
    
    
    {
      "result": {
        "bugs": {
          "hrrFailure": true,
          "splitClientHello": true,
          "unknownKeyshare": true
        },
        "host": "host",
        "kex": 0,
        "kexName": "kexName",
        "pq": true
      },
      "success": true
    }
