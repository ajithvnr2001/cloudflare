---
url: https://developers.cloudflare.com/secrets-store/audit-logs/
title: Audit logs \u00b7 Cloudflare Secrets Store docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:29.256089+00:00
---

# Audit logs · Cloudflare Secrets Store docs

> Source: https://developers.cloudflare.com/secrets-store/audit-logs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Secrets Store](https://developers.cloudflare.com/secrets-store/)
  3. /Audit logs



# Audit logs

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/secrets-store/audit-logs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Audit logs](https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/) provide a comprehensive summary of changes made within your Cloudflare account. This page lists the actions that are logged for Secrets Store.

  * Access
  * Create 
    * Duplicating a secret is presented as a `create` log with a field `duplicated_from_id`.
  * Update 
    * A boolean `"value_modified": true` is presented when the secret value is edited.
  * Delete



For information on how to access and use audit logs, refer to [Fundamentals](https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/).

[PreviousAI Gateway ↗︎](https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/secrets-store/audit-logs.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
