---
url: https://developers.cloudflare.com/workers/wrangler/commands/vpc/
title: VPC \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:18:10.011112+00:00
---

# VPC · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/wrangler/commands/vpc/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Wrangler](https://developers.cloudflare.com/workers/wrangler/)

  4. /[Commands](https://developers.cloudflare.com/workers/wrangler/commands/)
  5. /VPC



# VPC

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/wrangler/commands/vpc/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Manage [Workers VPC](https://developers.cloudflare.com/workers-vpc/) services using Wrangler. VPC services allow your Workers to connect to private services on your network through Cloudflare Tunnels.

## `vpc service create`

Create a new VPC service

npmyarnpnpm
    
    
    npx wrangler vpc service create <NAME>
    
    
    yarn wrangler vpc service create <NAME>
    
    
    pnpm wrangler vpc service create <NAME>

  * `<NAME>``string` required

The name of the VPC service

  * `--type``string` required

The type of the VPC service

  * `--tcp-port``number`

TCP port number

  * `--app-protocol``string`

Application protocol for the TCP service

  * `--http-port``number`

HTTP port (default: 80)

  * `--https-port``number`

HTTPS port number (default: 443)

  * `--ipv4``string`

IPv4 address for the host [conflicts with --ipv6]

  * `--ipv6``string`

IPv6 address for the host [conflicts with --ipv4]

  * `--hostname``string`

Hostname for the host

  * `--resolver-ips``string`

Comma-separated list of resolver IPs

  * `--tunnel-id``string` required

UUID of the Cloudflare tunnel

  * `--cert-verification-mode``string`

TLS certificate verification mode for the connection to the origin




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




## `vpc service delete`

Delete a VPC service

npmyarnpnpm
    
    
    npx wrangler vpc service delete <SERVICE-ID>
    
    
    yarn wrangler vpc service delete <SERVICE-ID>
    
    
    pnpm wrangler vpc service delete <SERVICE-ID>

  * `<SERVICE-ID>``string` required

The ID of the service to delete




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




## `vpc service get`

Get a VPC service

npmyarnpnpm
    
    
    npx wrangler vpc service get <SERVICE-ID>
    
    
    yarn wrangler vpc service get <SERVICE-ID>
    
    
    pnpm wrangler vpc service get <SERVICE-ID>

  * `<SERVICE-ID>``string` required

The ID of the VPC service




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




## `vpc service list`

List VPC services

npmyarnpnpm
    
    
    npx wrangler vpc service list
    
    
    yarn wrangler vpc service list
    
    
    pnpm wrangler vpc service list

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




## `vpc service update`

Update a VPC service

npmyarnpnpm
    
    
    npx wrangler vpc service update <SERVICE-ID>
    
    
    yarn wrangler vpc service update <SERVICE-ID>
    
    
    pnpm wrangler vpc service update <SERVICE-ID>

  * `<SERVICE-ID>``string` required

The ID of the VPC service to update

  * `--name``string` required

The name of the VPC service

  * `--type``string` required

The type of the VPC service

  * `--tcp-port``number`

TCP port number

  * `--app-protocol``string`

Application protocol for the TCP service

  * `--http-port``number`

HTTP port (default: 80)

  * `--https-port``number`

HTTPS port number (default: 443)

  * `--ipv4``string`

IPv4 address for the host [conflicts with --ipv6]

  * `--ipv6``string`

IPv6 address for the host [conflicts with --ipv4]

  * `--hostname``string`

Hostname for the host

  * `--resolver-ips``string`

Comma-separated list of resolver IPs

  * `--tunnel-id``string` required

UUID of the Cloudflare tunnel

  * `--cert-verification-mode``string`

TLS certificate verification mode for the connection to the origin




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




[PreviousVectorize](https://developers.cloudflare.com/workers/wrangler/commands/vectorize/)[NextWorkers for Platforms](https://developers.cloudflare.com/workers/wrangler/commands/workers-for-platforms/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/wrangler/commands/vpc.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
