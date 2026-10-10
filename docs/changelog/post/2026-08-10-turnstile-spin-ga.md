---
url: https://developers.cloudflare.com/changelog/post/2026-08-10-turnstile-spin-ga/
title: Turnstile Spin is now generally available \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:33.256671+00:00
---

# Turnstile Spin is now generally available · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-10-turnstile-spin-ga/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 10, 2026

## Turnstile Spin is now generally available

[Turnstile](https://developers.cloudflare.com/turnstile/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Turnstile Spin](https://developers.cloudflare.com/turnstile/spin/) is now generally available with three setup paths for creating a Turnstile widget and wiring canonical server-side siteverify into your existing backend. Start in the dashboard, with Wrangler, or from your AI coding agent. All three paths create the same widget. You can complete the integration by hand or have your agent embed the widget, wire siteverify, and validate it.

#### Server-side verification

Turnstile setup has two parts: embed the widget in your frontend, then call siteverify from your backend. Without the second part, the widget appears on the page but does not protect the request.

  * The skill includes insertion snippets for Next.js (App Router and Pages Router), Astro, SvelteKit, Hugo, and vanilla HTML. For other frameworks, the agent proposes a generic pattern and asks you to confirm it first.
  * The Turnstile dashboard flags existing widgets with no matching siteverify traffic. Select **Fix with Spin** to copy a prompt that guides your agent through wiring siteverify into your backend.
  * Before finishing, the agent runs a real Turnstile token through your protected endpoint, checks that it passes, then replays the token to confirm the endpoint rejects it on the second try. If a check fails, the agent stops and shows you where.



#### Run Spin

You can run Spin three ways:

  * In the **Turnstile dashboard** , select **Set up with Spin** , enter your domains, then select **Set up**. Spin creates the widget and returns the sitekey, secret, and a prompt for your agent.
  * From the `Wrangler CLI`, run [`wrangler turnstile widget create`](https://developers.cloudflare.com/turnstile/spin/#set-up-from-the-wrangler-cli). Wrangler prints the sitekey and secret. You wire the frontend and siteverify by hand.
  * From your **AI coding agent** , paste the [Spin prompt](https://developers.cloudflare.com/turnstile/spin/#set-up-from-an-ai-coding-agent) into Claude Code, Cursor, Codex, OpenCode, or GitHub Copilot Chat. Your agent fetches the skill, creates the widget, then embeds it and wires siteverify.



To get started, refer to the [Turnstile Spin documentation](https://developers.cloudflare.com/turnstile/spin/).
