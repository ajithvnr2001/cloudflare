---
url: https://developers.cloudflare.com/learning-paths/dns-best-practices/concepts/summary-considerations/
title: Key considerations and best practices summary \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:48.118199+00:00
---

# Key considerations and best practices summary · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/dns-best-practices/concepts/summary-considerations/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Dns Best Practices

  4. /[Concepts](https://developers.cloudflare.com/learning-paths/dns-best-practices/concepts/)
  5. /Key considerations and best practices summary



# Key considerations and best practices summary

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/dns-best-practices/concepts/summary-considerations/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

  * Plan meticulously: Do not rush the planning and preparation phases.
  * Communicate clearly: Keep stakeholders informed.
  * Lower TTLs in advance: This is crucial for a faster cutover.
  * Disable DNSSEC before NS change (safest): Remove DS records at the registrar well before changing nameservers, then re-enable DNSSEC via Cloudflare.
  * Verify, verify, verify: Double-check record imports and functionality at each stage.
  * Test thoroughly: From multiple locations and for all critical services.
  * Have a rollback plan: Know how to revert if necessary.
  * Migrate during low traffic: Minimize potential user impact.
  * Address BIND Views/ACLs: Understand how Cloudflare will handle or replace this functionality.
  * Take advantage of Cloudflare features: Once stable, explore and implement Cloudflare's security and performance enhancements.



By following these best practices, you can significantly increase the likelihood of a smooth and successful migration from your on-prem BIND DNS to Cloudflare.

[PreviousPhase 4: Post-migration and DNSSEC Re-activation](https://developers.cloudflare.com/learning-paths/dns-best-practices/concepts/phase-4/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/dns-best-practices/concepts/summary-considerations.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
