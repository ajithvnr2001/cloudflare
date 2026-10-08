---
url: https://developers.cloudflare.com/basin-sql/reference/wrangler-commands/
title: Wrangler commands \u00b7 Basin SQL docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:27.823264+00:00
---

# Wrangler commands · Basin SQL docs

> Source: https://developers.cloudflare.com/basin-sql/reference/wrangler-commands/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Basin SQL](https://developers.cloudflare.com/basin-sql/)
  3. /Reference
  4. /Wrangler commands



# Wrangler commands

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/basin-sql/reference/wrangler-commands/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Use the `basin sql` command family to query a warehouse:

npmyarnpnpm
    
    
    npx wrangler basin sql query <WAREHOUSE_NAME> "SELECT * FROM <NAMESPACE>.<TABLE> LIMIT 10"
    
    
    yarn wrangler basin sql query <WAREHOUSE_NAME> "SELECT * FROM <NAMESPACE>.<TABLE> LIMIT 10"
    
    
    pnpm wrangler basin sql query <WAREHOUSE_NAME> "SELECT * FROM <NAMESPACE>.<TABLE> LIMIT 10"

[PreviousLimitations and best practices](https://developers.cloudflare.com/basin-sql/reference/limitations-best-practices/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/basin-sql/reference/wrangler-commands.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
