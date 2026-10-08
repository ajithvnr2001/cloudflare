---
url: https://developers.cloudflare.com/use-cases/apis/internal-services/
title: Connect your internal network services \u00b7 Cloudflare use cases
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:09.532109+00:00
---

# Connect your internal network services · Cloudflare use cases

> Source: https://developers.cloudflare.com/use-cases/apis/internal-services/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Use cases](https://developers.cloudflare.com/use-cases/)
  3. /[APIs and microservices](https://developers.cloudflare.com/use-cases/apis/)
  4. /Connect your internal network services



# Connect your internal network services

Last updated Apr 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/use-cases/apis/internal-services/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSolutions Cloudflare Tunnel Access Service TokensGet started

Internal services and microservices often need to communicate without exposing endpoints to the public Internet. Cloudflare Tunnel creates outbound-only connections with no inbound firewall rules, while Access enforces Zero Trust policies for every request between services.

## Solutions

### Cloudflare Tunnel

Connect infrastructure to Cloudflare without opening inbound firewall ports. [Learn more about Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/).

  * **No public exposure** \- Internal Application Programming Interfaces (APIs) remain private; Tunnel establishes an outbound-only connection with no inbound firewall rules needed



### Access

Zero Trust access control for applications and infrastructure. [Learn more about Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/).

  * **Zero Trust policies** \- Verify identity and enforce per-service policies for every request between services
  * **Centralized policy management** \- Manage access rules for all internal services from a single control plane



### Service Tokens

Non-interactive credentials for machine-to-machine authentication. [Learn more about Service Tokens](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/).

  * **Service-to-service auth** \- Authenticate internal services with non-interactive credentials managed in Cloudflare One



## Get started

  1. [Create a Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/)
  2. [Cloudflare Access get started](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)
  3. [Create service tokens](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/)



[PreviousProtect your APIs](https://developers.cloudflare.com/use-cases/apis/protect-apis/)[NextMonitor your APIs](https://developers.cloudflare.com/use-cases/apis/monitor-apis/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/use-cases/apis/internal-services.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
