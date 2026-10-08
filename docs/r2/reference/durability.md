---
url: https://developers.cloudflare.com/r2/reference/durability/
title: Durability \u00b7 Cloudflare R2 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:48.574743+00:00
---

# Durability · Cloudflare R2 docs

> Source: https://developers.cloudflare.com/r2/reference/durability/

  1. [Home](https://developers.cloudflare.com/)
  2. /[R2](https://developers.cloudflare.com/r2/)
  3. /Reference
  4. /Durability



# Durability

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/r2/reference/durability/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow R2 achieves eleven-nines durability Considerations

R2 is designed to provide 99.999999999% (eleven 9s) of annual durability. This means that if you store 10,000,000 objects on R2, you can expect to lose an object once every 10,000 years on average.

## How R2 achieves eleven-nines durability

R2's durability is built on multiple layers of redundancy and data protection:

  * **Replication** : When you upload an object, R2 stores multiple "copies" of that object through either full replication and/or erasure coding. This ensures that the full or partial failure of any individual disk does not result in data loss. Erasure coding distributes parts of the object across multiple disks, ensuring that even if some disks fail, the object can still be reconstructed from a subset of the available parts, preventing hardware failure or physical impacts to data centers (such as fire or floods) from causing data loss.

  * **Hardware redundancy** : Storage clusters are comprised of hardware distributed across several data centers within a geographic region. This physical distribution ensures that localized failures—such as power outages, network disruptions, or hardware malfunctions at a single facility—do not result in data loss.

  * **Synchronous writes** : R2 returns an `HTTP 200 (OK)` for a write via API or otherwise indicates success only when data has been persisted to disk. We do not rely on asynchronous replication to support underlying durability guarantees. This is critical to R2’s consistency guarantees and mitigates the chance of a client receiving a successful API response without the underlying metadata and storage infrastructure having persisted the change.




### Considerations

  * Durability is not a guarantee of data availability. It is a measure of the likelihood of data loss.
  * R2 provides an availability [SLA of 99.9% ↗︎](https://www.cloudflare.com/r2-service-level-agreement/)
  * Durability does not prevent intentional or accidental deletion of data. Use [bucket locks](https://developers.cloudflare.com/r2/buckets/bucket-locks/) and/or bucket-scoped [API tokens](https://developers.cloudflare.com/r2/api/tokens/) to limit access to data.
  * Durability is also distinct from [consistency](https://developers.cloudflare.com/r2/reference/consistency/), which describes how reads and writes are reflected in the system's state (e.g. eventual consistency vs. strong consistency).



[PreviousData security](https://developers.cloudflare.com/r2/reference/data-security/)[NextUnicode interoperability](https://developers.cloudflare.com/r2/reference/unicode-interoperability/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/r2/reference/durability.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
