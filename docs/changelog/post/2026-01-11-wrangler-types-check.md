---
url: https://developers.cloudflare.com/changelog/post/2026-01-11-wrangler-types-check/
title: Validate your generated types with `wrangler types --check` \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:33.093560+00:00
---

# Validate your generated types with `wrangler types --check` · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-01-11-wrangler-types-check/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)January 12, 2026

## Validate your generated types with `wrangler types --check`

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-11-wrangler-types-check/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Wrangler now supports a `--check` flag for the `wrangler types` command. This flag validates that your generated types are up to date without writing any changes to disk.

This is useful in CI/CD pipelines where you want to ensure that developers have regenerated their types after making changes to their Wrangler configuration. If the types are out of date, the command will exit with a non-zero status code.
    
    
    npx wrangler types --check

If your types are up to date, the command will succeed silently. If they are out of date, you'll see an error message indicating which files need to be regenerated.

For more information, see the [Wrangler types documentation](https://developers.cloudflare.com/workers/wrangler/commands/general/#types).
