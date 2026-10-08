---
url: https://developers.cloudflare.com/key-transparency/api/auditor-information/
title: Auditor \u00b7 Cloudflare Key Transparency Auditor docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:39.647333+00:00
---

# Auditor · Cloudflare Key Transparency Auditor docs

> Source: https://developers.cloudflare.com/key-transparency/api/auditor-information/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Key Transparency Auditor](https://developers.cloudflare.com/key-transparency/)
  3. /API
  4. /Auditor



# Auditor

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/key-transparency/api/auditor-information/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewGet Auditor information

The Auditor is designed to sign epoch information, which includes the time at which the request is received by the Auditor, the epoch number, and the epoch digest. The Auditor serializes this information in binary using protobuf or bincode and checks whether the requested inclusion is valid, as in it satisfies [publication constraints](https://developers.cloudflare.com/key-transparency/api/epochs/#constraints).

If the Log is setup to provide [AKD ↗︎](https://github.com/facebook/akd) audit proof, the Auditor verifies them asynchronously.

## Get Auditor information

`keys` contain Auditor public keys which allow for key rotation later.
    
    
    curl 'https://plexi.key-transparency.cloudflare.com/info'
    {
      "keys": [
        {
          "public_key": "d1036a33a8731e82a29dc68210988b32b60b7c1bd22d2341f2e339f4db3a2f4a",
          "not_before": 1712311441501
        }
      ],
      "logs": [
        "508607faff7cb16be841e901eca41a6239461f239e7e610c9ea2576f334bc144"
      ]
    }

[PreviousOverview](https://developers.cloudflare.com/key-transparency/)[NextNamespaces](https://developers.cloudflare.com/key-transparency/api/namespaces/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/key-transparency/api/auditor-information.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
