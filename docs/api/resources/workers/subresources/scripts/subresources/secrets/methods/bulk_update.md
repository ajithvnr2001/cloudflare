---
url: https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/secrets/methods/bulk_update/
title: Patch multiple Worker script secrets | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:26:48.770269+00:00
---

# Patch multiple Worker script secrets | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/secrets/methods/bulk_update/

[API Reference](https://developers.cloudflare.com/api)

[Workers](https://developers.cloudflare.com/api/resources/workers)

[Scripts](https://developers.cloudflare.com/api/resources/workers/subresources/scripts)

[Secrets](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/secrets)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Patch multiple Worker script secrets

PATCH/accounts/{account_id}/workers/scripts/{script_name}/secrets-bulk

Create, update, or delete multiple secrets on a Worker script in a single operation using JSON Merge Patch (RFC 7396). This operation creates a single version with all changes included. Prefer this API instead of changing many secrets individually.

Usage:

  * To create or update a secret, set its value to a secret object.
  * To delete a secret, set its value to `null`.
  * Secrets not included in the request are left unchanged.



##### Security

API Token

The preferred authorization scheme for interacting with the Cloudflare API. [Create a token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/).

**Example:**`Authorization: Bearer Sn3lZJTBX6kkg7OdcBUAxOO963GEIyGQqnFTOFYY`

API Email + API Key

The previous authorization scheme for interacting with the Cloudflare API, used in conjunction with a Global API key.

**Example:**`X-Auth-Email: user@example.com`

The previous authorization scheme for interacting with the Cloudflare API. When possible, use API tokens instead of Global API keys.

**Example:**`X-Auth-Key: 144c9defac04969c7bfad8efaa8ea194`

##### Path ParametersExpand Collapse 

account_id: string

Identifier.

maxLength32

script_name: string

Name of the script.

##### Body ParametersJSONExpand Collapse 

secrets: optional map[object { name, text, type }  or object { algorithm, format, name, 4 more } ]

Map of secret names to secret values:

  * Set to a secret object to create or update.
  * Set to `null` to delete.
  * Omit to leave unchanged.



One of the following:

SecretText object { name, text, type } 

name: string

A JavaScript variable name for the binding.

text: string

The secret value to use.

type: "secret_text"

The kind of resource that the binding provides.

SecretKey object { algorithm, format, name, 4 more } 

algorithm: unknown

Algorithm-specific key parameters. [Learn more](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#algorithm).

format: "raw" or "pkcs8" or "spki" or "jwk"

Data format of the key. [Learn more](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#format).

One of the following:

"raw"

"pkcs8"

"spki"

"jwk"

name: string

A JavaScript variable name for the binding.

type: "secret_key"

The kind of resource that the binding provides.

usages: array of "encrypt" or "decrypt" or "sign" or 5 more

Allowed operations with the key. [Learn more](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#keyUsages).

One of the following:

"encrypt"

"decrypt"

"sign"

"verify"

"deriveKey"

"deriveBits"

"wrapKey"

"unwrapKey"

key_base64: optional string

Base64-encoded key data. Required if `format` is “raw”, “pkcs8”, or “spki”.

key_jwk: optional unknown

Key data in [JSON Web Key](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#json_web_key) format. Required if `format` is “jwk”.

version_tags: optional map[unknown]

Optional version tags to apply to the new script version.

##### ReturnsExpand Collapse 

errors: array of object { code, message, documentation_url, source } 

code: number

minimum1000

message: string

documentation_url: optional string

source: optional object { pointer } 

pointer: optional string

messages: array of object { code, message, documentation_url, source } 

code: number

minimum1000

message: string

documentation_url: optional string

source: optional object { pointer } 

pointer: optional string

success: true

Whether the API call was successful.

result: optional map[object { name, text, type }  or object { algorithm, format, name, 4 more } ]

Map of secret names to secret metadata for resulting secrets.

One of the following:

SecretText object { name, text, type } 

name: string

A JavaScript variable name for the binding.

text: string

The secret value to use.

type: "secret_text"

The kind of resource that the binding provides.

SecretKey object { algorithm, format, name, 4 more } 

algorithm: unknown

Algorithm-specific key parameters. [Learn more](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#algorithm).

format: "raw" or "pkcs8" or "spki" or "jwk"

Data format of the key. [Learn more](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#format).

One of the following:

"raw"

"pkcs8"

"spki"

"jwk"

name: string

A JavaScript variable name for the binding.

type: "secret_key"

The kind of resource that the binding provides.

usages: array of "encrypt" or "decrypt" or "sign" or 5 more

Allowed operations with the key. [Learn more](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#keyUsages).

One of the following:

"encrypt"

"decrypt"

"sign"

"verify"

"deriveKey"

"deriveBits"

"wrapKey"

"unwrapKey"

key_base64: optional string

Base64-encoded key data. Required if `format` is “raw”, “pkcs8”, or “spki”.

key_jwk: optional unknown

Key data in [JSON Web Key](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#json_web_key) format. Required if `format` is “jwk”.

### Patch multiple Worker script secrets

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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/workers/scripts/$SCRIPT_NAME/secrets-bulk \
        -X PATCH \
        -H 'Content-Type: application/json' \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
        -d '{}'

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
        {
          "code": 1000,
          "message": "message",
          "documentation_url": "documentation_url",
          "source": {
            "pointer": "pointer"
          }
        }
      ],
      "success": true,
      "result": {
        "foo": {
          "name": "myBinding",
          "type": "secret_text"
        }
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
        {
          "code": 1000,
          "message": "message",
          "documentation_url": "documentation_url",
          "source": {
            "pointer": "pointer"
          }
        }
      ],
      "success": true,
      "result": {
        "foo": {
          "name": "myBinding",
          "type": "secret_text"
        }
      }
    }
