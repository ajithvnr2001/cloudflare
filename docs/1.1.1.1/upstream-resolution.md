---
url: https://developers.cloudflare.com/1.1.1.1/upstream-resolution/
title: Upstream resolution \u00b7 Cloudflare 1.1.1.1 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:04.922164+00:00
---

# Upstream resolution · Cloudflare 1.1.1.1 docs

> Source: https://developers.cloudflare.com/1.1.1.1/upstream-resolution/

  1. [Home](https://developers.cloudflare.com/)
  2. /[1.1.1.1 (DNS Resolver)](https://developers.cloudflare.com/1.1.1.1/)
  3. /Upstream resolution



# Upstream resolution

Last updated Apr 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/1.1.1.1/upstream-resolution/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewQuery name minimizationRoot zoneNameserver selectionRetry behaviorResponse selection

When 1.1.1.1 does not have an answer in its cache, it contacts authoritative nameservers on your behalf. Authoritative nameservers are the DNS servers that hold the actual records for a domain. This page describes how 1.1.1.1 selects which nameserver to query, what happens when a nameserver is unreachable, and how the final response is determined.

## Query name minimization

When resolving a multi-level domain name like `foo.bar.example.com`, 1.1.1.1 does not reveal the full name to every server in the chain. Instead, it sends only the minimum information each server needs. For example, when asking the `.com` TLD server, 1.1.1.1 only discloses that it needs to find `example.com` — the subdomain parts (`foo.bar`) are not included. This limits the amount of information exposed to intermediary servers and reduces privacy leakage.

## Root zone

1.1.1.1 uses [locally hosted copies of the root zone file ↗︎](https://blog.cloudflare.com/f-root/) instead of querying remote root servers for every lookup. The root zone file contains the addresses of all top-level domain (TLD) servers. By hosting it locally, 1.1.1.1 avoids a network round trip to root servers, which reduces latency, improves privacy, and decreases load on the global DNS root server system.

## Nameserver selection

Most domains have multiple authoritative nameservers for redundancy. When 1.1.1.1 needs to query one, it chooses based on measured performance. The resolver tracks metrics for each nameserver — including round-trip time (how long a query takes to travel to the server and back) and response quality — then picks the nameserver that has historically been fastest and most reliable from the data center handling your request.

If the selected nameserver does not respond in time or returns an error, 1.1.1.1 retries against a different nameserver for the same zone. Refer to Retry behavior for details.

A small percentage of queries are also sent to alternative nameservers so that performance measurements stay current. This allows a previously slow server to be re-evaluated if its performance improves. For more background on the system that powers this selection, refer to the [BigPineapple architecture blog post ↗︎](https://blog.cloudflare.com/big-pineapple-intro/).

## Retry behavior

If a nameserver does not respond in time or returns a temporary error, 1.1.1.1 retries the query against a different authoritative nameserver for the same zone. The unresponsive server is deprioritized so that subsequent queries prefer healthier alternatives. 1.1.1.1 periodically re-checks deprioritized servers to detect recovery.

When multiple clients request the same domain at the same time, 1.1.1.1 deduplicates the upstream queries so that a single in-flight request serves all waiting clients. The exact retry timing and ranking logic are tuned over time and may change.

## Response selection

For a given query, 1.1.1.1 returns only one answer to the client. When authoritative nameservers disagree, which response 1.1.1.1 selects depends on the type of responses received.

The following DNS response codes are relevant:

  * **`NOERROR`** — The query succeeded. The response contains the requested records, or indicates that the name exists but has no records of the requested type (sometimes called `NODATA`).
  * **`NXDOMAIN`** — The domain name does not exist.
  * **`SERVFAIL`** — The nameserver encountered an internal error and could not answer.
  * **`REFUSED`** — The nameserver refused to answer the query.



How 1.1.1.1 handles disagreements between nameservers:

  * **`NOERROR` versus `NXDOMAIN`:** Both are valid authoritative answers. 1.1.1.1 returns whichever response it receives first and does not query remaining nameservers to compare. Authoritative nameservers for the same zone are expected to be consistent. If one returns `NXDOMAIN` and another returns `NOERROR` for the same name, that indicates a misconfiguration on the authoritative side.
  * **Timeout versus a valid response:** A timeout is not an answer. 1.1.1.1 retries against another nameserver and returns the first valid response it receives.
  * **`SERVFAIL` or `REFUSED` versus a valid response:** Temporary failures are treated as upstream errors, not authoritative answers. 1.1.1.1 retries against another nameserver and returns the first valid response. Only if all nameservers return errors does 1.1.1.1 return a failure to the client — typically `SERVFAIL`, or `REFUSED` if that is what the nameservers consistently returned.



[PreviousDNSKEY](https://developers.cloudflare.com/1.1.1.1/encryption/dnskey/)[NextNetwork operators](https://developers.cloudflare.com/1.1.1.1/infrastructure/network-operators/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/1.1.1.1/upstream-resolution.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
