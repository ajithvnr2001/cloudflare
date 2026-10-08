---
url: https://developers.cloudflare.com/data-localization/how-to/
title: Configuration guides \u00b7 Cloudflare Data Localization Suite docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:41.879084+00:00
---

# Configuration guides · Cloudflare Data Localization Suite docs

> Source: https://developers.cloudflare.com/data-localization/how-to/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Data Localization Suite](https://developers.cloudflare.com/data-localization/)
  3. /Configuration guides



# Configuration guides

Last updated Apr 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/data-localization/how-to/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewVerify Regional Services behavior

Learn how to configure Cloudflare products with the Data Localization Suite, including Regional Services (which controls where traffic is decrypted and processed) and Customer Metadata Boundary (which controls where logs are stored).

  * [Zero Trust](https://developers.cloudflare.com/data-localization/how-to/zero-trust/)
  * [Pages](https://developers.cloudflare.com/data-localization/how-to/pages/)
  * [Cache](https://developers.cloudflare.com/data-localization/how-to/cache/)
  * [Load Balancing](https://developers.cloudflare.com/data-localization/how-to/load-balancing/)
  * [Cloudflare for SaaS](https://developers.cloudflare.com/data-localization/how-to/cloudflare-for-saas/)
  * [R2 Object Storage](https://developers.cloudflare.com/data-localization/how-to/r2/)
  * [Durable Objects](https://developers.cloudflare.com/data-localization/how-to/durable-objects/)
  * [Workers](https://developers.cloudflare.com/data-localization/how-to/workers/)



## Verify Regional Services behavior

In order to verify that Regional Services is working, customers can confirm the behavior by executing one of the following `curl` commands on a regionalized hostname:
    
    
    curl -X GET -I https://<HOSTNAME>/ 2>&1 | grep cf-ray
    
    
    curl -s https://<HOSTNAME>/cdn-cgi/trace | grep "colo="

The first command will return a three-letter IATA code (an airport identifier that corresponds to the nearest Cloudflare data center) in the [Cf-Ray](https://developers.cloudflare.com/fundamentals/reference/http-headers/#cf-ray) header, indicating the Cloudflare data center location of processing and/or TLS termination (traffic decryption). The second command will directly return the three-letter IATA code.

For example, when a hostname is configured to use the region European Union (EU), the three-letter IATA code will always return a data center inside of the EU.

[PreviousRegionalized IP Bindings](https://developers.cloudflare.com/data-localization/regional-services/ip-bindings/)[NextZero Trust](https://developers.cloudflare.com/data-localization/how-to/zero-trust/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/data-localization/how-to/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
