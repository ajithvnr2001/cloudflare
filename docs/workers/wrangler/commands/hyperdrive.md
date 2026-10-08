---
url: https://developers.cloudflare.com/workers/wrangler/commands/hyperdrive/
title: Hyperdrive \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:18:07.649170+00:00
---

# Hyperdrive · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/wrangler/commands/hyperdrive/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Wrangler](https://developers.cloudflare.com/workers/wrangler/)

  4. /[Commands](https://developers.cloudflare.com/workers/wrangler/commands/)
  5. /Hyperdrive



# Hyperdrive

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/wrangler/commands/hyperdrive/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Manage [Hyperdrive](https://developers.cloudflare.com/hyperdrive/) database configurations using Wrangler.

To manage mTLS client certificates and CA chain certificates used by Hyperdrive, refer to [Certificate commands](https://developers.cloudflare.com/workers/wrangler/commands/certificates/).

## `hyperdrive create`

Create a Hyperdrive config

npmyarnpnpm
    
    
    npx wrangler hyperdrive create <NAME>
    
    
    yarn wrangler hyperdrive create <NAME>
    
    
    pnpm wrangler hyperdrive create <NAME>

  * `<NAME>``string` required

The name of the Hyperdrive config

  * `--connection-string``string`

The connection string for the database you want Hyperdrive to connect to - ex: protocol://user:password@host:port/database

  * `--service-id``string`

The Workers VPC Service ID of the origin database

  * `--origin-host``string` alias: --host

The host of the origin database

  * `--origin-port``number` alias: --port

The port number of the origin database

  * `--origin-scheme``string` alias: --schemedefault: postgresql

The scheme used to connect to the origin database

  * `--database``string`

The name of the database within the origin database

  * `--origin-user``string` alias: --user

The username used to connect to the origin database

  * `--origin-password``string` alias: --password

The password used to connect to the origin database

  * `--access-client-id``string`

The Client ID of the Access token to use when connecting to the origin database

  * `--access-client-secret``string`

The Client Secret of the Access token to use when connecting to the origin database

  * `--caching-disabled``boolean`

Disables the caching of SQL responses

  * `--max-age``number`

Specifies max duration for which items should persist in the cache, cannot be set when caching is disabled

  * `--swr``number`

Indicates the number of seconds cache may serve the response after it becomes stale, cannot be set when caching is disabled

  * `--ca-certificate-id``string` alias: --ca-certificate-uuid

Sets custom CA certificate when connecting to origin database. Must be valid UUID of already uploaded CA certificate.

  * `--mtls-certificate-id``string` alias: --mtls-certificate-uuid

Sets custom mTLS client certificates when connecting to origin database. Must be valid UUID of already uploaded public/private key certificates.

  * `--sslmode``string`

Sets sslmode for connecting to database. For PostgreSQL: 'require, verify-ca, verify-full'. For MySQL: 'REQUIRED, VERIFY_CA, VERIFY_IDENTITY'.

  * `--origin-connection-limit``number`

The (soft) maximum number of connections that Hyperdrive may establish to the origin database

  * `--binding``string`

The binding name of this resource in your Worker

  * `--update-config``boolean`

Automatically update your config file with the newly added resource




Global flags

  * `--v``boolean` alias: --version

Show version number

  * `--cwd``string`

Run as if Wrangler was started in the specified directory instead of the current working directory

  * `--config``string` alias: --c

Path to Wrangler configuration file

  * `--env``string` alias: --e

Environment to use for operations, and for selecting .env and .dev.vars files

  * `--env-file``string`

Path to an .env file to load - can be specified multiple times - values from earlier files are overridden by values in later files

  * `--install-skills``boolean` default: false

Install Cloudflare skills for detected AI coding agents before running the command

  * `--profile``string`

Use a specific auth profile




## `hyperdrive delete`

Delete a Hyperdrive config

npmyarnpnpm
    
    
    npx wrangler hyperdrive delete <ID>
    
    
    yarn wrangler hyperdrive delete <ID>
    
    
    pnpm wrangler hyperdrive delete <ID>

  * `<ID>``string` required

The ID of the Hyperdrive config




Global flags

  * `--v``boolean` alias: --version

Show version number

  * `--cwd``string`

Run as if Wrangler was started in the specified directory instead of the current working directory

  * `--config``string` alias: --c

Path to Wrangler configuration file

  * `--env``string` alias: --e

Environment to use for operations, and for selecting .env and .dev.vars files

  * `--env-file``string`

Path to an .env file to load - can be specified multiple times - values from earlier files are overridden by values in later files

  * `--install-skills``boolean` default: false

Install Cloudflare skills for detected AI coding agents before running the command

  * `--profile``string`

Use a specific auth profile




## `hyperdrive get`

Get a Hyperdrive config

npmyarnpnpm
    
    
    npx wrangler hyperdrive get <ID>
    
    
    yarn wrangler hyperdrive get <ID>
    
    
    pnpm wrangler hyperdrive get <ID>

  * `<ID>``string` required

The ID of the Hyperdrive config




Global flags

  * `--v``boolean` alias: --version

Show version number

  * `--cwd``string`

Run as if Wrangler was started in the specified directory instead of the current working directory

  * `--config``string` alias: --c

Path to Wrangler configuration file

  * `--env``string` alias: --e

Environment to use for operations, and for selecting .env and .dev.vars files

  * `--env-file``string`

Path to an .env file to load - can be specified multiple times - values from earlier files are overridden by values in later files

  * `--install-skills``boolean` default: false

Install Cloudflare skills for detected AI coding agents before running the command

  * `--profile``string`

Use a specific auth profile




## `hyperdrive list`

List Hyperdrive configs

npmyarnpnpm
    
    
    npx wrangler hyperdrive list
    
    
    yarn wrangler hyperdrive list
    
    
    pnpm wrangler hyperdrive list

Global flags

  * `--v``boolean` alias: --version

Show version number

  * `--cwd``string`

Run as if Wrangler was started in the specified directory instead of the current working directory

  * `--config``string` alias: --c

Path to Wrangler configuration file

  * `--env``string` alias: --e

Environment to use for operations, and for selecting .env and .dev.vars files

  * `--env-file``string`

Path to an .env file to load - can be specified multiple times - values from earlier files are overridden by values in later files

  * `--install-skills``boolean` default: false

Install Cloudflare skills for detected AI coding agents before running the command

  * `--profile``string`

Use a specific auth profile




## `hyperdrive planetscale signature`

  
Experimental

Generate a signed authorization for creating a Cloudflare-billed PlanetScale database

npmyarnpnpm
    
    
    npx wrangler hyperdrive planetscale signature
    
    
    yarn wrangler hyperdrive planetscale signature
    
    
    pnpm wrangler hyperdrive planetscale signature

Global flags

  * `--v``boolean` alias: --version

Show version number

  * `--cwd``string`

Run as if Wrangler was started in the specified directory instead of the current working directory

  * `--config``string` alias: --c

Path to Wrangler configuration file

  * `--env``string` alias: --e

Environment to use for operations, and for selecting .env and .dev.vars files

  * `--env-file``string`

Path to an .env file to load - can be specified multiple times - values from earlier files are overridden by values in later files

  * `--install-skills``boolean` default: false

Install Cloudflare skills for detected AI coding agents before running the command

  * `--profile``string`

Use a specific auth profile




## `hyperdrive update`

Update a Hyperdrive config

npmyarnpnpm
    
    
    npx wrangler hyperdrive update <ID>
    
    
    yarn wrangler hyperdrive update <ID>
    
    
    pnpm wrangler hyperdrive update <ID>

  * `<ID>``string` required

The ID of the Hyperdrive config

  * `--name``string`

Give your config a new name

  * `--connection-string``string`

The connection string for the database you want Hyperdrive to connect to - ex: protocol://user:password@host:port/database

  * `--service-id``string`

The Workers VPC Service ID of the origin database

  * `--origin-host``string` alias: --host

The host of the origin database

  * `--origin-port``number` alias: --port

The port number of the origin database

  * `--origin-scheme``string` alias: --scheme

The scheme used to connect to the origin database

  * `--database``string`

The name of the database within the origin database

  * `--origin-user``string` alias: --user

The username used to connect to the origin database

  * `--origin-password``string` alias: --password

The password used to connect to the origin database

  * `--access-client-id``string`

The Client ID of the Access token to use when connecting to the origin database

  * `--access-client-secret``string`

The Client Secret of the Access token to use when connecting to the origin database

  * `--caching-disabled``boolean`

Disables the caching of SQL responses

  * `--max-age``number`

Specifies max duration for which items should persist in the cache, cannot be set when caching is disabled

  * `--swr``number`

Indicates the number of seconds cache may serve the response after it becomes stale, cannot be set when caching is disabled

  * `--ca-certificate-id``string` alias: --ca-certificate-uuid

Sets custom CA certificate when connecting to origin database. Must be valid UUID of already uploaded CA certificate.

  * `--mtls-certificate-id``string` alias: --mtls-certificate-uuid

Sets custom mTLS client certificates when connecting to origin database. Must be valid UUID of already uploaded public/private key certificates.

  * `--sslmode``string`

Sets sslmode for connecting to database. For PostgreSQL: 'require, verify-ca, verify-full'. For MySQL: 'REQUIRED, VERIFY_CA, VERIFY_IDENTITY'.

  * `--origin-connection-limit``number`

The (soft) maximum number of connections that Hyperdrive may establish to the origin database




Global flags

  * `--v``boolean` alias: --version

Show version number

  * `--cwd``string`

Run as if Wrangler was started in the specified directory instead of the current working directory

  * `--config``string` alias: --c

Path to Wrangler configuration file

  * `--env``string` alias: --e

Environment to use for operations, and for selecting .env and .dev.vars files

  * `--env-file``string`

Path to an .env file to load - can be specified multiple times - values from earlier files are overridden by values in later files

  * `--install-skills``boolean` default: false

Install Cloudflare skills for detected AI coding agents before running the command

  * `--profile``string`

Use a specific auth profile




[PreviousFlagship](https://developers.cloudflare.com/workers/wrangler/commands/flagship/)[NextKV](https://developers.cloudflare.com/workers/wrangler/commands/kv/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/wrangler/commands/hyperdrive.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
