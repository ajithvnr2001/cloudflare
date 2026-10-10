---
url: https://developers.cloudflare.com/changelog/post/2026-06-03-wrangler-keyring-credential-storage/
title: Store Wrangler's OAuth credentials in your OS keychain \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:37.244836+00:00
---

# Store Wrangler's OAuth credentials in your OS keychain · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-03-wrangler-keyring-credential-storage/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 3, 2026

## Store Wrangler's OAuth credentials in your OS keychain

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Wrangler](https://developers.cloudflare.com/workers/wrangler/) can now store the OAuth credentials returned by `wrangler login` in an [AES-256-GCM ↗︎](https://en.wikipedia.org/wiki/Galois/Counter_Mode)-encrypted file, with the encryption key held in your operating system keychain. The default behavior is unchanged — credentials still live in a plaintext TOML file unless you opt in.

To opt in, run:
    
    
    npx wrangler login --use-keyring

The choice is persisted across Wrangler invocations. Opt back out with `npx wrangler login --no-use-keyring`, or override the preference for a single command with the `CLOUDFLARE_AUTH_USE_KEYRING` environment variable.

`wrangler whoami` now reports where credentials are stored:
    
    
    🔐 Credentials are stored in: Encrypted file (~/.config/.wrangler/config/default.enc) with key in macOS Keychain (service=wrangler, account=default)

Per-platform backends:

  * **macOS** uses the built-in Keychain via `/usr/bin/security`.
  * **Linux** uses [libsecret ↗︎](https://wiki.gnome.org/Projects/Libsecret) via the `secret-tool` CLI from the `libsecret-tools` package.
  * **Windows** uses Credential Manager via [`@napi-rs/keyring` ↗︎](https://www.npmjs.com/package/@napi-rs/keyring), installed on-demand the first time you opt in.



Refer to [Storing OAuth credentials in the OS keychain](https://developers.cloudflare.com/workers/wrangler/commands/general/#storing-oauth-credentials-in-the-os-keychain) for the full details, including the migration behavior on opt-in/opt-out and the `CLOUDFLARE_AUTH_USE_KEYRING` environment variable.
