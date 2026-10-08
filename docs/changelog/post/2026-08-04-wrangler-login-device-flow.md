---
url: https://developers.cloudflare.com/changelog/post/2026-08-04-wrangler-login-device-flow/
title: Log in to Wrangler without a local callback server \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:06.826213+00:00
---

# Log in to Wrangler without a local callback server · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-04-wrangler-login-device-flow/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 4, 2026

## Log in to Wrangler without a local callback server

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-04-wrangler-login-device-flow/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`wrangler login` now supports the [OAuth 2.0 Device Authorization Grant ↗︎](https://www.rfc-editor.org/rfc/rfc8628). Pass `--device` to authenticate without starting a temporary callback server on `localhost:8976`:
    
    
    npx wrangler login --device

Wrangler prints a verification URL and a short user code, opens the URL in your default browser with the code already filled in, and polls Cloudflare for an access token while you approve the request:
    
    
     ⛅️ wrangler 4.119.0
    ────────────────────
    Attempting to login via OAuth Device Authorization Grant...
    To authorize Wrangler, please visit:
    
      https://dash.cloudflare.com/oauth2/device
    
    and enter the code:
    
      jPqK6Qvs
    
    You have 5 minutes to approve this request.
    
    Opening a link in your default browser: https://dash.cloudflare.com/oauth2/device?user_code=jPqK6Qvs
    Successfully logged in.

The default login flow needs your browser to reach `localhost:8976`, which is not always possible from containers, remote SSH sessions, or GitHub Codespaces. Previously these environments required forwarding ports or fetching the callback URL with `curl` from a second terminal session. Because `--device` has no callback server, those workarounds are no longer necessary.

Since the plain verification URL and user code are both printed to the terminal, you can also approve the request from a phone or another machine. Pass `--browser=false` to stop Wrangler from opening a browser at all.

Available in Wrangler version 4.119.0 or later. For more information, refer to [`wrangler login`](https://developers.cloudflare.com/workers/wrangler/commands/general/#login).
