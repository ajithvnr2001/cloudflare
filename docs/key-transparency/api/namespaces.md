---
url: https://developers.cloudflare.com/key-transparency/api/namespaces/
title: Namespaces \u00b7 Cloudflare Key Transparency Auditor docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:39.691103+00:00
---

# Namespaces · Cloudflare Key Transparency Auditor docs

> Source: https://developers.cloudflare.com/key-transparency/api/namespaces/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Key Transparency Auditor](https://developers.cloudflare.com/key-transparency/)
  3. /API
  4. /Namespaces



# Namespaces

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/key-transparency/api/namespaces/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate a namespaceList all namespacesDisable a namespace

The Cloudflare Key Transparency API is organized in namespaces, each one representing a Log monitored by Cloudflare Auditor. If you want to register a namespace, contact us.

## Create a namespace

The following fields are required when making a `POST` request:

  * `name`
  * `public`
  * `root`
  * `signature_version`: 
    * 0x0001 for [Protobuf serialisation ↗︎](https://github.com/cloudflare/plexi/blob/main/plexi_core/src/proto/specs/types.proto) Ed25519 signature from the Auditor
    * 0x0002 for [bincode serialisation ↗︎](https://github.com/bincode-org/bincode/blob/trunk/docs/spec.md) E25519 serialisation by the Auditor



The `log_directory` field is optional. If set, Cloudflare will use it to fetch audit proofs and validate them.

This API is authenticated via [mTLS ↗︎](https://www.cloudflare.com/learning/access-management/what-is-mutual-tls/).
    
    
    curl 'https://plexi.key-transparency.cloudflare.com/namespaces' \
            	--header 'Content-Type: application/json' \
            	--data '{
     	"name": "your.new.log.com",
     	"root": "1/1111111111111111111111111111111111111111111111111111111111111111",
     	"log_directory": "https://your.new.log.com/path/to/proofs",
    	"signature_version": 1
      }'
    {
      "name": "your.new.log.com",
      "log_directory": "https://your.new.log.com/path/to/proofs",
      "root": "1/1111111111111111111111111111111111111111111111111111111111111111",
      "status": "Initialization",
      "reports_uri": "/namespaces/your.new.log.com/reports",
      "audits_uri": "/namespaces/your.new.log.com/audits",
      "signature_version": 1
    }

After publishing the first epoch, `status` will show `Online`. Possible statuses include:

  * `Online`
  * `Initialization`
  * `Disabled`



## List all namespaces

Refer to the example below to get information about all public namespaces.
    
    
    curl 'https://plexi.key-transparency.cloudflare.com/namespaces'
    {
       "namespaces": [
           { "name": "your.new.log.com", "root": "1/abc", "reports_uri": "/namespaces/your.new.log.com/reports", "audits_uri": "/namespaces/your.new.log.com/audits", "log_directory": "https://your.new.log.com/path/to/proofs", "status": "online" },
           { "name": "my.new.log.com", "reports_uri": "/namespaces/meta-bt-2024/reports", "audits_uri": "/namespaces/meta-bt-2024/audits", "status": "initialization" }
       ]
    }

## Disable a namespace

If a log state has been corrupted, lost, or needs to be sharded to be maintainable, the Auditor allows the Log operator to mark a namespace as `Disabled`.

This API is authenticated via [mTLS ↗︎](https://www.cloudflare.com/learning/access-management/what-is-mutual-tls/).
    
    
    curl -X PATCH 'https://plexi.key-transparency.cloudflare.com/namespaces/{namespace}' \
            	-H 'Content-Type: application/json' \
            	-d '{
     	"status": "Disabled"
      }'
    {
      "name": "your.new.log.com",
      "log_directory": "https://your.new.log.com/path/to/proofs",
      "root": "1/1111111111111111111111111111111111111111111111111111111111111111",
      "status": "Disabled",
      "reports_uri": "/namespaces/your.new.log.com/reports",
      "audits_uri": "/namespaces/your.new.log.com/audits",
      "signature_version": 1
    }

[PreviousAuditor](https://developers.cloudflare.com/key-transparency/api/auditor-information/)[NextEpochs](https://developers.cloudflare.com/key-transparency/api/epochs/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/key-transparency/api/namespaces.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
