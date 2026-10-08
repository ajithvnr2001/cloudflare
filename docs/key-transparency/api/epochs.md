---
url: https://developers.cloudflare.com/key-transparency/api/epochs/
title: Epochs \u00b7 Cloudflare Key Transparency Auditor docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:39.403969+00:00
---

# Epochs · Cloudflare Key Transparency Auditor docs

> Source: https://developers.cloudflare.com/key-transparency/api/epochs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Key Transparency Auditor](https://developers.cloudflare.com/key-transparency/)
  3. /API
  4. /Epochs



# Epochs

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/key-transparency/api/epochs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewGet an epochPublish a new epoch Constraints

## Get an epoch
    
    
    curl 'https://plexi.key-transparency.cloudflare.com/namespaces/{namespace}/audits/1'
    {
      "namespace": "your.new.log.com",
      "timestamp": 1717084639921,
      "epoch": 1,
      "digest": "1111111111111111111111111111111111111111111111111111111111111111",
      "signature": "f6a51443bb6703813b330959d9d97471bc06464142165e59733fa102a18b052782a5307d59c31b8b13c1af7dfff6f6e7bf44e880d44e26e96c50a72f72a30c07"
    }

## Publish a new epoch

Refer to the example below to publish a new epoch by requesting its signature.

This API is authenticated via [mTLS ↗︎](https://www.cloudflare.com/learning/access-management/what-is-mutual-tls/), so that only a Log owner can publish new epochs.
    
    
    curl 'https://plexi.key-transparency.cloudflare.com/namespaces/{namespace}/audits' \
          --header 'Content-Type: application/json' \
          --data '{"epoch": 1, "digest": "1111111111111111111111111111111111111111111111111111111111111111"}'
    {
      "namespace": "your.new.log.com",
      "timestamp": 1717084639921,
      "epoch": 1,
      "digest": "1111111111111111111111111111111111111111111111111111111111111111",
      "signature": "f6a51443bb6703813b330959d9d97471bc06464142165e59733fa102a18b052782a5307d59c31b8b13c1af7dfff6f6e7bf44e880d44e26e96c50a72f72a30c07",
      "key_id": 74,
    }

### Constraints

  * If `root` is defined for the namespace, the first epoch must match it (number and digest).
  * Epochs must be increasing. Second epoch is 2, third is 3, etc.
  * Epochs must have a unique digest or it will be rejected.
  * Epochs cannot be republished.
  * Digest must be a 32 byte string hex encoded (length 64).



If a namespace is disabled, you receive the following error:
    
    
    HTTP 400 Bad Request
    Namespace is disabled and read-only.

[PreviousNamespaces](https://developers.cloudflare.com/key-transparency/api/namespaces/)[NextMonitor the Auditor](https://developers.cloudflare.com/key-transparency/monitor-the-auditor/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/key-transparency/api/epochs.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
