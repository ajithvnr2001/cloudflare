---
url: https://developers.cloudflare.com/api/resources/hyperdrive/subresources/configs/methods/list/
title: List Hyperdrives | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:18:43.292735+00:00
---

# List Hyperdrives | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/hyperdrive/subresources/configs/methods/list/

[API Reference](https://developers.cloudflare.com/api)

[Hyperdrive](https://developers.cloudflare.com/api/resources/hyperdrive)

[Configs](https://developers.cloudflare.com/api/resources/hyperdrive/subresources/configs)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# List Hyperdrives

GET/accounts/{account_id}/hyperdrive/configs

Returns a list of Hyperdrives.

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

`Hyperdrive Write``Hyperdrive Read`

##### Path ParametersExpand Collapse 

account_id: string

Define configurations using a unique string identifier.

maxLength32

##### Query ParametersExpand Collapse 

page: optional number

Page number of paginated results.

minimum1

per_page: optional number

Maximum number of results per page.

maximum100

minimum1

##### ReturnsExpand Collapse 

errors: array of [ResponseInfo](https://developers.cloudflare.com/api/resources/$shared#\(resource\)%20%24shared%20%3E%20\(model\)%20response_info%20%3E%20\(schema\)) { code, message, documentation_url, source } 

code: number

minimum1000

message: string

documentation_url: optional string

source: optional object { pointer } 

pointer: optional string

messages: array of [ResponseInfo](https://developers.cloudflare.com/api/resources/$shared#\(resource\)%20%24shared%20%3E%20\(model\)%20response_info%20%3E%20\(schema\)) { code, message, documentation_url, source } 

code: number

minimum1000

message: string

documentation_url: optional string

source: optional object { pointer } 

pointer: optional string

result: array of object { id, caching, name, 7 more } 

id: string

Define configurations using a unique string identifier.

maxLength32

caching: object { disabled, max_age, stale_while_revalidate } 

disabled: boolean

Defines whether caching is disabled.

max_age: optional number

Defines the maximum duration (in seconds) items persist in the cache.

maximum3600

minimum1

stale_while_revalidate: optional number

Defines the number of seconds the cache may serve a stale response.

minimum0

name: string

The name of the Hyperdrive configuration. Used to identify the configuration in the Cloudflare dashboard and API.

maxLength2048

origin: object { database, host, password, 3 more }  or object { access_client_id, access_client_secret, database, 4 more }  or object { database, password, scheme, 2 more } 

Combines database connection fields with exactly one supported network location.

One of the following:

PublicDatabase object { database, host, password, 3 more } 

database: string

Set the name of your origin database.

maxLength2048

host: string

Defines the publicly reachable hostname or IP of your origin database. Private, loopback, and link-local IP addresses are not allowed.

password: string

Set the password needed to access your origin database. The API never returns this write-only value.

maxLength2048

port: number

Defines the port of your origin database. Defaults to 5432 for PostgreSQL or 3306 for MySQL if not specified.

maximum65535

minimum1

scheme: "postgres" or "postgresql" or "mysql"

Specifies the URL scheme used to connect to your origin database.

One of the following:

"postgres"

"postgresql"

"mysql"

user: string

Set the user of your origin database.

maxLength2048

AccessProtectedDatabaseBehindCloudflareTunnel object { access_client_id, access_client_secret, database, 4 more } 

access_client_id: string

Defines the Client ID of the Access token to use when connecting to the origin database.

access_client_secret: string

Defines the Client Secret of the Access Token to use when connecting to the origin database. The API never returns this write-only value.

database: string

Set the name of your origin database.

maxLength2048

host: string

Defines the host (hostname or IP) of your origin database.

password: string

Set the password needed to access your origin database. The API never returns this write-only value.

maxLength2048

scheme: "postgres" or "postgresql" or "mysql"

Specifies the URL scheme used to connect to your origin database.

One of the following:

"postgres"

"postgresql"

"mysql"

user: string

Set the user of your origin database.

maxLength2048

DatabaseReachableThroughAWorkersVPC object { database, password, scheme, 2 more } 

database: string

Set the name of your origin database.

maxLength2048

password: string

Set the password needed to access your origin database. The API never returns this write-only value.

maxLength2048

scheme: "postgres" or "postgresql" or "mysql"

Specifies the URL scheme used to connect to your origin database.

One of the following:

"postgres"

"postgresql"

"mysql"

service_id: string

The identifier of the Workers VPC Service to connect through. Hyperdrive will egress through the specified VPC Service to reach the origin database.

user: string

Set the user of your origin database.

maxLength2048

created_on: optional string

Defines the creation time of the Hyperdrive configuration.

formatdate-time

integration: optional object { database_branch_name, database_name, organization_name, 3 more } 

Connects to a PlanetScale database using credentials managed by Cloudflare. The Cloudflare account must already be linked to PlanetScale in the Hyperdrive dashboard.

database_branch_name: string

The name of the PlanetScale database branch.

maxLength2048

minLength1

database_name: string

The name of the PlanetScale database.

maxLength2048

minLength1

organization_name: string

The name of the PlanetScale organization.

maxLength2048

minLength1

provider: "planetscale"

The database integration provider used by this operation.

scheme: "postgres" or "postgresql" or "mysql"

Specifies the URL scheme used to connect to your origin database.

One of the following:

"postgres"

"postgresql"

"mysql"

custom_database_name: optional string

The database name to use when connecting. Defaults to `postgres` for PostgreSQL and `mysql` for MySQL.

maxLength2048

modified_on: optional string

Defines the last modified time of the Hyperdrive configuration.

formatdate-time

mtls: optional object { ca_certificate_id, mtls_certificate_id, sslmode } 

mTLS configuration for the origin connection. Cannot be used with VPC Service origins; TLS must be managed on the VPC Service.

ca_certificate_id: optional string

Define CA certificate ID obtained after uploading CA cert.

mtls_certificate_id: optional string

Define mTLS certificate ID obtained after uploading client cert.

sslmode: optional string

PostgreSQL accepts `require`, `verify-ca`, and `verify-full`. MySQL accepts `REQUIRED`, `VERIFY_CA`, and `VERIFY_IDENTITY`. The verify modes require a CA certificate; the require modes cannot be used with a CA certificate.

origin_connection_limit: optional number

The (soft) maximum number of connections the Hyperdrive is allowed to make to the origin database.

Maximum allowed: 20 for free tier accounts, 100 for paid tier accounts. If not specified, defaults to 20 for free tier and 60 for paid tier. Certain Cloudflare-managed origins may be permitted a higher limit. Contact Cloudflare if you need a higher limit.

minimum5

restarted_on: optional string

Defines the last time the Hyperdrive connection pool was explicitly restarted via the restart endpoint. Omitted if the pool has never been explicitly restarted.

formatdate-time

success: true

Return the status of the API call success.

result_info: optional object { count, page, per_page, total_count } 

count: optional number

Defines the total number of results for the requested service.

page: optional number

Defines the current page within paginated list of results.

per_page: optional number

Defines the number of results per page of results.

total_count: optional number

Defines the total results available without any search parameters.

### List Hyperdrives

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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/hyperdrive/configs \
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
        {
          "code": 1000,
          "message": "message",
          "documentation_url": "documentation_url",
          "source": {
            "pointer": "pointer"
          }
        }
      ],
      "result": [
        {
          "id": "023e105f4ecef8ad9ca31a8372d0c353",
          "caching": {
            "disabled": true,
            "max_age": 1,
            "stale_while_revalidate": 0
          },
          "name": "example-hyperdrive",
          "origin": {
            "database": "postgres",
            "host": "database.example.com",
            "port": 5432,
            "scheme": "postgres",
            "user": "postgres"
          },
          "created_on": "2017-01-01T00:00:00Z",
          "integration": {
            "database_branch_name": "x",
            "database_name": "x",
            "organization_name": "x",
            "provider": "planetscale",
            "scheme": "postgres",
            "custom_database_name": "custom_database_name"
          },
          "modified_on": "2017-01-01T00:00:00Z",
          "mtls": {
            "ca_certificate_id": "00000000-0000-0000-0000-0000000000",
            "mtls_certificate_id": "00000000-0000-0000-0000-0000000000",
            "sslmode": "verify-full"
          },
          "origin_connection_limit": 60,
          "restarted_on": "2017-01-01T00:00:00Z"
        }
      ],
      "success": true,
      "result_info": {
        "count": 1,
        "page": 1,
        "per_page": 20,
        "total_count": 2000
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
      "result": [
        {
          "id": "023e105f4ecef8ad9ca31a8372d0c353",
          "caching": {
            "disabled": true,
            "max_age": 1,
            "stale_while_revalidate": 0
          },
          "name": "example-hyperdrive",
          "origin": {
            "database": "postgres",
            "host": "database.example.com",
            "port": 5432,
            "scheme": "postgres",
            "user": "postgres"
          },
          "created_on": "2017-01-01T00:00:00Z",
          "integration": {
            "database_branch_name": "x",
            "database_name": "x",
            "organization_name": "x",
            "provider": "planetscale",
            "scheme": "postgres",
            "custom_database_name": "custom_database_name"
          },
          "modified_on": "2017-01-01T00:00:00Z",
          "mtls": {
            "ca_certificate_id": "00000000-0000-0000-0000-0000000000",
            "mtls_certificate_id": "00000000-0000-0000-0000-0000000000",
            "sslmode": "verify-full"
          },
          "origin_connection_limit": 60,
          "restarted_on": "2017-01-01T00:00:00Z"
        }
      ],
      "success": true,
      "result_info": {
        "count": 1,
        "page": 1,
        "per_page": 20,
        "total_count": 2000
      }
    }
