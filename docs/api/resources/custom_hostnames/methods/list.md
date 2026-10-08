---
url: https://developers.cloudflare.com/api/resources/custom_hostnames/methods/list/
title: List Custom Hostnames | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:18:36.134216+00:00
---

# List Custom Hostnames | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/custom_hostnames/methods/list/

[API Reference](https://developers.cloudflare.com/api)

[Custom Hostnames](https://developers.cloudflare.com/api/resources/custom_hostnames)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# List Custom Hostnames

GET/zones/{zone_id}/custom_hostnames

List, search, sort, and filter all of your custom hostnames.

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

`SSL and Certificates Write``SSL and Certificates Read`

##### Path ParametersExpand Collapse 

zone_id: string

Identifier.

maxLength32

##### Query ParametersExpand Collapse 

id: optional string

Hostname ID to match against. This ID was generated and returned during the initial custom_hostname creation. This parameter cannot be used with the ‘hostname’, ‘hostname.exact’, ‘hostname.contain’, or ‘hostname.startsWith’ parameters.

maxLength36

minLength36

certificate_authority: optional "google" or "lets_encrypt" or "ssl_com"

Filter by the certificate authority that issued the SSL certificate.

One of the following:

"google"

"lets_encrypt"

"ssl_com"

custom_origin_server: optional string

Filter by custom origin server name.

direction: optional "asc" or "desc"

Direction to order hostnames.

One of the following:

"asc"

"desc"

hostname: optional object { contain, exact, startsWith } 

contain: optional string

Filters hostnames by a substring match on the hostname value. This parameter cannot be used with the ‘id’, ‘hostname’, ‘hostname.exact’, or ‘hostname.startsWith’ parameters.

maxLength255

exact: optional string

Fully qualified domain name to match against. This parameter cannot be used with the ‘id’, ‘hostname’, ‘hostname.contain’, or ‘hostname.startsWith’ parameters.

maxLength255

startsWith: optional string

Filters hostnames by a prefix match on the hostname value. This parameter cannot be used with the ‘id’, ‘hostname’, ‘hostname.exact’, or ‘hostname.contain’ parameters.

maxLength255

hostname_status: optional "active" or "pending" or "active_redeploying" or 13 more

Filter by the hostname’s activation status.

One of the following:

"active"

"pending"

"active_redeploying"

"moved"

"pending_deletion"

"deleted"

"pending_blocked"

"pending_migration"

"pending_provisioned"

"test_pending"

"test_active"

"test_active_apex"

"test_blocked"

"test_failed"

"provisioned"

"blocked"

order: optional "ssl" or "ssl_status"

Field to order hostnames by.

One of the following:

"ssl"

"ssl_status"

page: optional number

Page number of paginated results.

minimum1

per_page: optional number

Number of hostnames per page.

maximum1000

minimum5

ssl: optional 0 or 1

Whether to filter hostnames based on if they have SSL enabled.

One of the following:

0

1

ssl_status: optional "initializing" or "pending_validation" or "deleted" or 18 more

Filter by SSL certificate status.

One of the following:

"initializing"

"pending_validation"

"deleted"

"pending_issuance"

"pending_deployment"

"pending_deletion"

"pending_expiration"

"expired"

"active"

"initializing_timed_out"

"validation_timed_out"

"issuance_timed_out"

"deployment_timed_out"

"deletion_timed_out"

"pending_cleanup"

"staging_deployment"

"staging_active"

"deactivating"

"inactive"

"backup_issued"

"holding_deployment"

wildcard: optional boolean

Filter by whether the custom hostname is a wildcard hostname.

##### ReturnsExpand Collapse 

errors: array of object { code, message, documentation_url, source } 

code: number

minimum1000

message: string

documentation_url: optional string

source: optional object { pointer } 

pointer: optional string

messages: array of string

Informational messages returned by the custom hostname API.

success: true

Whether the API call was successful.

result: optional array of object { id, hostname, created_at, 8 more } 

id: string

Custom hostname identifier tag.

maxLength36

minLength36

hostname: string

The custom hostname that will point to your hostname via CNAME.

maxLength255

created_at: optional string

This is the time the hostname was created.

formatdate-time

custom_metadata: optional map[string]

Unique key/value metadata for this hostname. These are per-hostname (customer) settings.

custom_origin_server: optional string

a valid hostname that’s been added to your DNS zone as an A, AAAA, or CNAME record.

custom_origin_sni: optional string

A hostname that will be sent to your custom origin server as SNI for TLS handshake. This can be a valid subdomain of the zone or custom origin server name or the string ‘:request_host_header:’ which will cause the host header in the request to be used as SNI. Not configurable with default/fallback origin server.

ownership_verification: optional object { name, type, value } 

This is a record which can be placed to activate a hostname.

name: optional string

DNS Name for record.

type: optional "txt"

DNS Record type.

value: optional string

Content for the record.

ownership_verification_http: optional object { http_body, http_url } 

This presents the token to be served by the given http url to activate a hostname.

http_body: optional string

Token to be served.

http_url: optional string

The HTTP URL that will be checked during custom hostname verification and where the customer should host the token.

ssl: optional object { id, bundle_method, certificate_authority, 17 more } 

id: optional string

Custom hostname SSL identifier tag.

maxLength36

minLength36

bundle_method: optional [BundleMethod](https://developers.cloudflare.com/api/resources/custom_hostnames#\(resource\)%20custom_hostnames%20%3E%20\(model\)%20bundle_method%20%3E%20\(schema\))

A ubiquitous bundle has the highest probability of being verified everywhere, even by clients using outdated or unusual trust stores. An optimal bundle uses the shortest chain and newest intermediates. And the force bundle verifies the chain, but does not otherwise modify it.

One of the following:

"ubiquitous"

"optimal"

"force"

certificate_authority: optional [CertificateCA](https://developers.cloudflare.com/api/resources/$shared#\(resource\)%20%24shared%20%3E%20\(model\)%20certificate_ca%20%3E%20\(schema\))

The Certificate Authority that will issue the certificate.

One of the following:

"digicert"

"google"

"lets_encrypt"

"ssl_com"

custom_certificate: optional string

If a custom uploaded certificate is used.

custom_csr_id: optional string

The identifier for the Custom CSR that was used.

custom_key: optional string

The key for a custom uploaded certificate.

dcv_delegation_records: optional array of object { cname, cname_target, emails, 5 more } 

DCV Delegation records for domain validation.

cname: optional string

The CNAME record hostname for DCV delegation.

cname_target: optional string

The CNAME record target value for DCV delegation.

emails: optional array of string

The set of email addresses that the certificate authority (CA) will use to complete domain validation.

http_body: optional string

The content that the certificate authority (CA) will expect to find at the http_url during the domain validation.

http_url: optional string

The url that will be checked during domain validation.

status: optional string

Status of the validation record.

txt_name: optional string

The hostname that the certificate authority (CA) will check for a TXT record during domain validation .

txt_value: optional string

The TXT record that the certificate authority (CA) will check during domain validation.

expires_on: optional string

The time the custom certificate expires on.

formatdate-time

hosts: optional array of string

A list of Hostnames on a custom uploaded certificate.

issuer: optional string

The issuer on a custom uploaded certificate.

method: optional [DCVMethod](https://developers.cloudflare.com/api/resources/custom_hostnames#\(resource\)%20custom_hostnames%20%3E%20\(model\)%20dcv_method%20%3E%20\(schema\))

Domain control validation (DCV) method used for this hostname.

One of the following:

"http"

"txt"

"email"

serial_number: optional string

The serial number on a custom uploaded certificate.

settings: optional object { ciphers, early_hints, http2, 2 more } 

ciphers: optional array of string

An allowlist of ciphers for TLS termination. These ciphers must be in the BoringSSL format.

early_hints: optional "on" or "off"

Whether or not Early Hints is enabled.

One of the following:

"on"

"off"

http2: optional "on" or "off"

Whether or not HTTP2 is enabled.

One of the following:

"on"

"off"

min_tls_version: optional "1.0" or "1.1" or "1.2" or "1.3"

The minimum TLS version supported.

One of the following:

"1.0"

"1.1"

"1.2"

"1.3"

tls_1_3: optional "on" or "off"

Whether or not TLS 1.3 is enabled.

One of the following:

"on"

"off"

signature: optional string

The signature on a custom uploaded certificate.

status: optional "initializing" or "pending_validation" or "deleted" or 18 more

Status of the hostname’s SSL certificates.

One of the following:

"initializing"

"pending_validation"

"deleted"

"pending_issuance"

"pending_deployment"

"pending_deletion"

"pending_expiration"

"expired"

"active"

"initializing_timed_out"

"validation_timed_out"

"issuance_timed_out"

"deployment_timed_out"

"deletion_timed_out"

"pending_cleanup"

"staging_deployment"

"staging_active"

"deactivating"

"inactive"

"backup_issued"

"holding_deployment"

type: optional [DomainValidationType](https://developers.cloudflare.com/api/resources/custom_hostnames#\(resource\)%20custom_hostnames%20%3E%20\(model\)%20domain_validation_type%20%3E%20\(schema\))

Level of validation to be used for this hostname. Domain validation (dv) must be used.

uploaded_on: optional string

The time the custom certificate was uploaded.

formatdate-time

validation_errors: optional array of object { message } 

Domain validation errors that have been received by the certificate authority (CA).

message: optional string

A domain validation error.

validation_records: optional array of object { cname, cname_target, emails, 5 more } 

cname: optional string

The CNAME record hostname for DCV delegation.

cname_target: optional string

The CNAME record target value for DCV delegation.

emails: optional array of string

The set of email addresses that the certificate authority (CA) will use to complete domain validation.

http_body: optional string

The content that the certificate authority (CA) will expect to find at the http_url during the domain validation.

http_url: optional string

The url that will be checked during domain validation.

status: optional string

Status of the validation record.

txt_name: optional string

The hostname that the certificate authority (CA) will check for a TXT record during domain validation .

txt_value: optional string

The TXT record that the certificate authority (CA) will check during domain validation.

wildcard: optional boolean

Indicates whether the certificate covers a wildcard.

status: optional "active" or "pending" or "active_redeploying" or 13 more

Status of the hostname’s activation.

One of the following:

"active"

"pending"

"active_redeploying"

"moved"

"pending_deletion"

"deleted"

"pending_blocked"

"pending_migration"

"pending_provisioned"

"test_pending"

"test_active"

"test_active_apex"

"test_blocked"

"test_failed"

"provisioned"

"blocked"

verification_errors: optional array of string

These are errors that were encountered while trying to activate a hostname.

result_info: optional object { count, page, per_page, 2 more } 

count: optional number

Total number of results for the requested service.

page: optional number

Current page within paginated list of results.

per_page: optional number

Number of results per page of results.

total_count: optional number

Total results available without any search parameters.

total_pages: optional number

The number of total pages in the entire result set.

### List Custom Hostnames

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
    
    
    curl https://api.cloudflare.com/client/v4/zones/$ZONE_ID/custom_hostnames \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

200 example
    
    
    {
      "errors": [
        {
          "code": 1000,
          "message": "message",
          "documentation_url": "documentation_url",
          "source": {
            "pointer": "pointer"
          }
        }
      ],
      "messages": [
        "string"
      ],
      "success": true,
      "result": [
        {
          "id": "0d89c70d-ad9f-4843-b99f-6cc0252067e9",
          "hostname": "app.example.com",
          "created_at": "2020-02-06T18:11:23.531995Z",
          "custom_metadata": {
            "foo": "string"
          },
          "custom_origin_server": "origin2.example.com",
          "custom_origin_sni": "sni.example.com",
          "ownership_verification": {
            "name": "_cf-custom-hostname.app.example.com",
            "type": "txt",
            "value": "5cc07c04-ea62-4a5a-95f0-419334a875a4"
          },
          "ownership_verification_http": {
            "http_body": "5cc07c04-ea62-4a5a-95f0-419334a875a4",
            "http_url": "http://custom.test.com/.well-known/cf-custom-hostname-challenge/0d89c70d-ad9f-4843-b99f-6cc0252067e9"
          },
          "ssl": {
            "id": "0d89c70d-ad9f-4843-b99f-6cc0252067e9",
            "bundle_method": "ubiquitous",
            "certificate_authority": "google",
            "custom_certificate": "-----BEGIN CERTIFICATE-----\nMIIFJDCCBAygAwIBAgIQD0ifmj/Yi5NP/2gdUySbfzANBgkqhkiG9w0BAQsFADBN\nMQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMScwJQYDVQQDEx5E...SzSHfXp5lnu/3V08I72q1QNzOCgY1XeL4GKVcj4or6cT6tX6oJH7ePPmfrBfqI/O\nOeH8gMJ+FuwtXYEPa4hBf38M5eU5xWG7\n-----END CERTIFICATE-----\n",
            "custom_csr_id": "7b163417-1d2b-4c84-a38a-2fb7a0cd7752",
            "custom_key": "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAwQHoetcl9+5ikGzV6cMzWtWPJHqXT3wpbEkRU9Yz7lgvddmG\ndtcGbg/1CGZu0jJGkMoppoUo4c3dts3iwqRYmBikUP77wwY2QGmDZw2FvkJCJlKn\nabIRuGvBKwzESIXgKk2016aTP6/dAjEHyo6SeoK8lkIySUvK0fyOVlsiEsCmOpid\ntnKX/a+50GjB79CJH4ER2lLVZnhePFR/zUOyPxZQQ4naHf7yu/b5jhO0f8fwt+py\nFxIXjbEIdZliWRkRMtzrHOJIhrmJ2A1J7iOrirbbwillwjjNVUWPf3IJ3M12S9pE\newooaeO2izNTERcG9HzAacbVRn2Y2SWIyT/18QIDAQABAoIBACbhTYXBZYKmYPCb\nHBR1IBlCQA2nLGf0qRuJNJZg5iEzXows/6tc8YymZkQE7nolapWsQ+upk2y5Xdp/\naxiuprIs9JzkYK8Ox0r+dlwCG1kSW+UAbX0bQ/qUqlsTvU6muVuMP8vZYHxJ3wmb\n+ufRBKztPTQ/rYWaYQcgC0RWI20HTFBMxlTAyNxYNWzX7RKFkGVVyB9RsAtmcc8g\n+j4OdosbfNoJPS0HeIfNpAznDfHKdxDk2Yc1tV6RHBrC1ynyLE9+TaflIAdo2MVv\nKLMLq51GqYKtgJFIlBRPQqKoyXdz3fGvXrTkf/WY9QNq0J1Vk5ERePZ54mN8iZB7\n9lwy/AkCgYEA6FXzosxswaJ2wQLeoYc7ceaweX/SwTvxHgXzRyJIIT0eJWgx13Wo\n/WA3Iziimsjf6qE+SI/8laxPp2A86VMaIt3Z3mJN/CqSVGw8LK2AQst+OwdPyDMu\niacE8lj/IFGC8mwNUAb9CzGU3JpU4PxxGFjS/eMtGeRXCWkK4NE+G08CgYEA1Kp9\nN2JrVlqUz+gAX+LPmE9OEMAS9WQSQsfCHGogIFDGGcNf7+uwBM7GAaSJIP01zcoe\nVAgWdzXCv3FLhsaZoJ6RyLOLay5phbu1iaTr4UNYm5WtYTzMzqh8l1+MFFDl9xDB\nvULuCIIrglM5MeS/qnSg1uMoH2oVPj9TVst/ir8CgYEAxrI7Ws9Zc4Bt70N1As+U\nlySjaEVZCMkqvHJ6TCuVZFfQoE0r0whdLdRLU2PsLFP+q7qaeZQqgBaNSKeVcDYR\n9B+nY/jOmQoPewPVsp/vQTCnE/R81spu0mp0YI6cIheT1Z9zAy322svcc43JaWB7\nmEbeqyLOP4Z4qSOcmghZBSECgYACvR9Xs0DGn+wCsW4vze/2ei77MD4OQvepPIFX\ndFZtlBy5ADcgE9z0cuVB6CiL8DbdK5kwY9pGNr8HUCI03iHkW6Zs+0L0YmihfEVe\nPG19PSzK9CaDdhD9KFZSbLyVFmWfxOt50H7YRTTiPMgjyFpfi5j2q348yVT0tEQS\nfhRqaQKBgAcWPokmJ7EbYQGeMbS7HC8eWO/RyamlnSffdCdSc7ue3zdVJxpAkQ8W\nqu80pEIF6raIQfAf8MXiiZ7auFOSnHQTXUbhCpvDLKi0Mwq3G8Pl07l+2s6dQG6T\nlv6XTQaMyf6n1yjzL+fzDrH3qXMxHMO/b13EePXpDMpY7HQpoLDi\n-----END RSA PRIVATE KEY-----\n",
            "dcv_delegation_records": [
              {
                "cname": "_acme-challenge.example.com",
                "cname_target": "dcv.cloudflare.com",
                "emails": [
                  "administrator@example.com",
                  "webmaster@example.com"
                ],
                "http_body": "ca3-574923932a82475cb8592200f1a2a23d",
                "http_url": "http://app.example.com/.well-known/pki-validation/ca3-da12a1c25e7b48cf80408c6c1763b8a2.txt",
                "status": "pending",
                "txt_name": "_acme-challenge.app.example.com",
                "txt_value": "810b7d5f01154524b961ba0cd578acc2"
              }
            ],
            "expires_on": "2021-02-06T18:11:23.531995Z",
            "hosts": [
              "app.example.com",
              "*.app.example.com"
            ],
            "issuer": "DigiCertInc",
            "method": "http",
            "serial_number": "6743787633689793699141714808227354901",
            "settings": {
              "ciphers": [
                "ECDHE-RSA-AES128-GCM-SHA256",
                "AES128-SHA"
              ],
              "early_hints": "on",
              "http2": "on",
              "min_tls_version": "1.2",
              "tls_1_3": "on"
            },
            "signature": "SHA256WithRSA",
            "status": "pending_validation",
            "type": "dv",
            "uploaded_on": "2020-02-06T18:11:23.531995Z",
            "validation_errors": [
              {
                "message": "SERVFAIL looking up CAA for app.example.com"
              }
            ],
            "validation_records": [
              {
                "cname": "_acme-challenge.example.com",
                "cname_target": "dcv.cloudflare.com",
                "emails": [
                  "administrator@example.com",
                  "webmaster@example.com"
                ],
                "http_body": "ca3-574923932a82475cb8592200f1a2a23d",
                "http_url": "http://app.example.com/.well-known/pki-validation/ca3-da12a1c25e7b48cf80408c6c1763b8a2.txt",
                "status": "pending",
                "txt_name": "_acme-challenge.app.example.com",
                "txt_value": "810b7d5f01154524b961ba0cd578acc2"
              }
            ],
            "wildcard": false
          },
          "status": "pending",
          "verification_errors": [
            "None of the A or AAAA records are owned by this account and the pre-generated ownership verification token was not found."
          ]
        }
      ],
      "result_info": {
        "count": 1,
        "page": 1,
        "per_page": 20,
        "total_count": 2000,
        "total_pages": 100
      }
    }

##### Returns Examples

200 example
    
    
    {
      "errors": [
        {
          "code": 1000,
          "message": "message",
          "documentation_url": "documentation_url",
          "source": {
            "pointer": "pointer"
          }
        }
      ],
      "messages": [
        "string"
      ],
      "success": true,
      "result": [
        {
          "id": "0d89c70d-ad9f-4843-b99f-6cc0252067e9",
          "hostname": "app.example.com",
          "created_at": "2020-02-06T18:11:23.531995Z",
          "custom_metadata": {
            "foo": "string"
          },
          "custom_origin_server": "origin2.example.com",
          "custom_origin_sni": "sni.example.com",
          "ownership_verification": {
            "name": "_cf-custom-hostname.app.example.com",
            "type": "txt",
            "value": "5cc07c04-ea62-4a5a-95f0-419334a875a4"
          },
          "ownership_verification_http": {
            "http_body": "5cc07c04-ea62-4a5a-95f0-419334a875a4",
            "http_url": "http://custom.test.com/.well-known/cf-custom-hostname-challenge/0d89c70d-ad9f-4843-b99f-6cc0252067e9"
          },
          "ssl": {
            "id": "0d89c70d-ad9f-4843-b99f-6cc0252067e9",
            "bundle_method": "ubiquitous",
            "certificate_authority": "google",
            "custom_certificate": "-----BEGIN CERTIFICATE-----\nMIIFJDCCBAygAwIBAgIQD0ifmj/Yi5NP/2gdUySbfzANBgkqhkiG9w0BAQsFADBN\nMQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMScwJQYDVQQDEx5E...SzSHfXp5lnu/3V08I72q1QNzOCgY1XeL4GKVcj4or6cT6tX6oJH7ePPmfrBfqI/O\nOeH8gMJ+FuwtXYEPa4hBf38M5eU5xWG7\n-----END CERTIFICATE-----\n",
            "custom_csr_id": "7b163417-1d2b-4c84-a38a-2fb7a0cd7752",
            "custom_key": "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAwQHoetcl9+5ikGzV6cMzWtWPJHqXT3wpbEkRU9Yz7lgvddmG\ndtcGbg/1CGZu0jJGkMoppoUo4c3dts3iwqRYmBikUP77wwY2QGmDZw2FvkJCJlKn\nabIRuGvBKwzESIXgKk2016aTP6/dAjEHyo6SeoK8lkIySUvK0fyOVlsiEsCmOpid\ntnKX/a+50GjB79CJH4ER2lLVZnhePFR/zUOyPxZQQ4naHf7yu/b5jhO0f8fwt+py\nFxIXjbEIdZliWRkRMtzrHOJIhrmJ2A1J7iOrirbbwillwjjNVUWPf3IJ3M12S9pE\newooaeO2izNTERcG9HzAacbVRn2Y2SWIyT/18QIDAQABAoIBACbhTYXBZYKmYPCb\nHBR1IBlCQA2nLGf0qRuJNJZg5iEzXows/6tc8YymZkQE7nolapWsQ+upk2y5Xdp/\naxiuprIs9JzkYK8Ox0r+dlwCG1kSW+UAbX0bQ/qUqlsTvU6muVuMP8vZYHxJ3wmb\n+ufRBKztPTQ/rYWaYQcgC0RWI20HTFBMxlTAyNxYNWzX7RKFkGVVyB9RsAtmcc8g\n+j4OdosbfNoJPS0HeIfNpAznDfHKdxDk2Yc1tV6RHBrC1ynyLE9+TaflIAdo2MVv\nKLMLq51GqYKtgJFIlBRPQqKoyXdz3fGvXrTkf/WY9QNq0J1Vk5ERePZ54mN8iZB7\n9lwy/AkCgYEA6FXzosxswaJ2wQLeoYc7ceaweX/SwTvxHgXzRyJIIT0eJWgx13Wo\n/WA3Iziimsjf6qE+SI/8laxPp2A86VMaIt3Z3mJN/CqSVGw8LK2AQst+OwdPyDMu\niacE8lj/IFGC8mwNUAb9CzGU3JpU4PxxGFjS/eMtGeRXCWkK4NE+G08CgYEA1Kp9\nN2JrVlqUz+gAX+LPmE9OEMAS9WQSQsfCHGogIFDGGcNf7+uwBM7GAaSJIP01zcoe\nVAgWdzXCv3FLhsaZoJ6RyLOLay5phbu1iaTr4UNYm5WtYTzMzqh8l1+MFFDl9xDB\nvULuCIIrglM5MeS/qnSg1uMoH2oVPj9TVst/ir8CgYEAxrI7Ws9Zc4Bt70N1As+U\nlySjaEVZCMkqvHJ6TCuVZFfQoE0r0whdLdRLU2PsLFP+q7qaeZQqgBaNSKeVcDYR\n9B+nY/jOmQoPewPVsp/vQTCnE/R81spu0mp0YI6cIheT1Z9zAy322svcc43JaWB7\nmEbeqyLOP4Z4qSOcmghZBSECgYACvR9Xs0DGn+wCsW4vze/2ei77MD4OQvepPIFX\ndFZtlBy5ADcgE9z0cuVB6CiL8DbdK5kwY9pGNr8HUCI03iHkW6Zs+0L0YmihfEVe\nPG19PSzK9CaDdhD9KFZSbLyVFmWfxOt50H7YRTTiPMgjyFpfi5j2q348yVT0tEQS\nfhRqaQKBgAcWPokmJ7EbYQGeMbS7HC8eWO/RyamlnSffdCdSc7ue3zdVJxpAkQ8W\nqu80pEIF6raIQfAf8MXiiZ7auFOSnHQTXUbhCpvDLKi0Mwq3G8Pl07l+2s6dQG6T\nlv6XTQaMyf6n1yjzL+fzDrH3qXMxHMO/b13EePXpDMpY7HQpoLDi\n-----END RSA PRIVATE KEY-----\n",
            "dcv_delegation_records": [
              {
                "cname": "_acme-challenge.example.com",
                "cname_target": "dcv.cloudflare.com",
                "emails": [
                  "administrator@example.com",
                  "webmaster@example.com"
                ],
                "http_body": "ca3-574923932a82475cb8592200f1a2a23d",
                "http_url": "http://app.example.com/.well-known/pki-validation/ca3-da12a1c25e7b48cf80408c6c1763b8a2.txt",
                "status": "pending",
                "txt_name": "_acme-challenge.app.example.com",
                "txt_value": "810b7d5f01154524b961ba0cd578acc2"
              }
            ],
            "expires_on": "2021-02-06T18:11:23.531995Z",
            "hosts": [
              "app.example.com",
              "*.app.example.com"
            ],
            "issuer": "DigiCertInc",
            "method": "http",
            "serial_number": "6743787633689793699141714808227354901",
            "settings": {
              "ciphers": [
                "ECDHE-RSA-AES128-GCM-SHA256",
                "AES128-SHA"
              ],
              "early_hints": "on",
              "http2": "on",
              "min_tls_version": "1.2",
              "tls_1_3": "on"
            },
            "signature": "SHA256WithRSA",
            "status": "pending_validation",
            "type": "dv",
            "uploaded_on": "2020-02-06T18:11:23.531995Z",
            "validation_errors": [
              {
                "message": "SERVFAIL looking up CAA for app.example.com"
              }
            ],
            "validation_records": [
              {
                "cname": "_acme-challenge.example.com",
                "cname_target": "dcv.cloudflare.com",
                "emails": [
                  "administrator@example.com",
                  "webmaster@example.com"
                ],
                "http_body": "ca3-574923932a82475cb8592200f1a2a23d",
                "http_url": "http://app.example.com/.well-known/pki-validation/ca3-da12a1c25e7b48cf80408c6c1763b8a2.txt",
                "status": "pending",
                "txt_name": "_acme-challenge.app.example.com",
                "txt_value": "810b7d5f01154524b961ba0cd578acc2"
              }
            ],
            "wildcard": false
          },
          "status": "pending",
          "verification_errors": [
            "None of the A or AAAA records are owned by this account and the pre-generated ownership verification token was not found."
          ]
        }
      ],
      "result_info": {
        "count": 1,
        "page": 1,
        "per_page": 20,
        "total_count": 2000,
        "total_pages": 100
      }
    }
