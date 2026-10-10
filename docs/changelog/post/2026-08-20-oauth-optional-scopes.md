---
url: https://developers.cloudflare.com/changelog/post/2026-08-20-oauth-optional-scopes/
title: Optional OAuth scopes \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:32.528431+00:00
---

# Optional OAuth scopes · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-20-oauth-optional-scopes/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 20, 2026

## Optional OAuth scopes

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We're announcing the GA of Optional OAuth Scopes.

OAuth client developers can now classify configured scopes as required or optional in the Cloudflare dashboard. By default, all configured scopes remain required .

#### What's New

**Optional Scopes:** OAuth clients can now mark configured scopes as optional, allowing applications to request them without requiring users to approve them.

**Scope Selection:** On the consent screen, users must grant required scopes but can decline optional scopes. This helps customers apply least-privilege access to applications, CLIs, and workloads. Optional scopes are selected by default.

**Templates:** The consent screen now includes **Read Only** and **Full Access** templates to make scope selection faster and easier.

**Search:** Users can now search scopes in the consent screen.

Learn how to [select client scopes](https://developers.cloudflare.com/fundamentals/oauth/create-an-oauth-client/#select-scopes) and [edit optional permissions](https://developers.cloudflare.com/fundamentals/oauth/authorizing-an-application/#edit-optional-permissions).
