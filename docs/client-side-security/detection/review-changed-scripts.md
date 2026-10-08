---
url: https://developers.cloudflare.com/client-side-security/detection/review-changed-scripts/
title: Review changed scripts \u00b7 Client-side security docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:57.250806+00:00
---

# Review changed scripts · Client-side security docs

> Source: https://developers.cloudflare.com/client-side-security/detection/review-changed-scripts/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Client-side security](https://developers.cloudflare.com/client-side-security/)
  3. /Detection
  4. /Review changed scripts



# Review changed scripts

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/client-side-security/detection/review-changed-scripts/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow changes are detected

Note

Only available to customers with Client-Side Security Advanced.

Cloudflare analyzes the JavaScript dependencies in the pages of your domain over time.

## How changes are detected

Cloudflare parses each script into an abstract syntax tree (AST) and hashes its structure. A script is marked as changed when this structural hash changes.

The comparison does not use the raw file bytes. Changes that preserve the same AST structure, such as formatting changes or changing only numeric literal values, do not trigger a code change alert.

You can configure a notification for [code change alerts](https://developers.cloudflare.com/client-side-security/alerts/alert-types/#code-change-alert) to receive a daily notification about changed scripts in your domain.

When you receive such a notification:

  1. In the Cloudflare dashboard, go to the **Web assets** page.

[ Go to **Web assets** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/web-assets)
  2. Select the **Client-side resources** tab.

  3. Check the details of each changed script and validate if it is an expected change.




[PreviousReview resources considered malicious](https://developers.cloudflare.com/client-side-security/detection/review-malicious-scripts/)[NextOverview](https://developers.cloudflare.com/client-side-security/alerts/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/client-side-security/detection/review-changed-scripts.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
