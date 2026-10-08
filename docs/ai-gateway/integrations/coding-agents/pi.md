---
url: https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/pi/
title: Pi \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:30.908014+00:00
---

# Pi · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/pi/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /…

Integrations

  4. /[Coding agents](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/)
  5. /Pi



# Pi

Last updated Sep 10, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/pi/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites

[Pi ↗︎](https://pi.dev) is a coding agent you run in your terminal. It has built-in support for AI Gateway, so instead of setting a base URL you select the `cloudflare-ai-gateway` provider and point Pi at your gateway. Pi builds the gateway endpoint from your account ID and gateway slug and routes requests through it.

## Prerequisites

Before you start, you need:

  * An [authenticated gateway](https://developers.cloudflare.com/ai-gateway/configuration/authentication/) and its [gateway token](https://developers.cloudflare.com/ai-gateway/configuration/authentication/#setting-up-authenticated-gateway-using-the-dashboard). The gateway token must have `Run` permissions.
  * Your Cloudflare account ID. To find it, refer to [Find your account and zone IDs](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/).
  * Pi installed and updated to the latest version.



Note

The token you give Pi is your gateway token, not a model provider key. To pay for model usage, enable [Unified Billing](https://developers.cloudflare.com/ai-gateway/features/unified-billing/) or store provider keys in AI Gateway with [BYOK (Store Keys)](https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/). Either way, AI Gateway handles the provider authentication for you.

  1. Set your gateway token, account ID, and gateway slug as environment variables. The following commands set them for the current session. To persist them, add them to your shell profile (for example, `~/.zshrc` or `~/.bashrc`).

Replace `<CLOUDFLARE_API_KEY>` and `<CLOUDFLARE_ACCOUNT_ID>` with your values. You can leave `CLOUDFLARE_GATEWAY_ID` as `default` to route through your account's default gateway, or change it to another gateway slug.
         
         # Run `wrangler auth token` to get an auth token.
         export CLOUDFLARE_API_KEY="<CLOUDFLARE_API_KEY>"
         # Run `wrangler whoami` to get your account ID.
         export CLOUDFLARE_ACCOUNT_ID="<CLOUDFLARE_ACCOUNT_ID>"
         # Use `default` to route through your account's default gateway.
         export CLOUDFLARE_GATEWAY_ID="default"
         
         # Run `wrangler auth token` to get an auth token.
         $env:CLOUDFLARE_API_KEY = "<CLOUDFLARE_API_KEY>"
         # Run `wrangler whoami` to get your account ID.
         $env:CLOUDFLARE_ACCOUNT_ID = "<CLOUDFLARE_ACCOUNT_ID>"
         # Use `default` to route through your account's default gateway.
         $env:CLOUDFLARE_GATEWAY_ID = "default"

Alternatively, leave out `CLOUDFLARE_API_KEY` and run `/login` inside Pi to store the token instead.

  2. Start a session against a model. Requests now route through AI Gateway.
         
         pi --provider cloudflare-ai-gateway --model "claude-sonnet-4-6"




To confirm traffic reaches AI Gateway, refer to [Verify it works](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/#verify-it-works).

[PreviousOpenCode](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/opencode/)[NextVisual Studio Code](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/vs-code/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/integrations/coding-agents/pi.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
