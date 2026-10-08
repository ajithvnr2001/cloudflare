---
url: https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/claude-desktop/
title: Claude Desktop \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:31.484968+00:00
---

# Claude Desktop · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/claude-desktop/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /…

Integrations

  4. /[Coding agents](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/)
  5. /Claude Desktop



# Claude Desktop

Last updated Aug 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/claude-desktop/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites

By pointing [Claude Desktop ↗︎](https://claude.ai/download) at AI Gateway instead of Anthropic directly, you get observability, caching, and centralized credentials for your Anthropic requests, without changing how you use Claude Desktop. Claude Desktop can send third-party inference requests to a custom gateway; this configuration sends those requests to AI Gateway's [Anthropic endpoint](https://developers.cloudflare.com/ai-gateway/usage/providers/anthropic/), authenticated with your Cloudflare gateway token. AI Gateway can supply the Anthropic credentials for you through [Unified Billing](https://developers.cloudflare.com/ai-gateway/features/unified-billing/) or a [stored provider key (BYOK)](https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/).

## Prerequisites

Before you start, you need:

  * An [authenticated gateway](https://developers.cloudflare.com/ai-gateway/configuration/authentication/) and its [gateway token](https://developers.cloudflare.com/ai-gateway/configuration/authentication/#setting-up-authenticated-gateway-using-the-dashboard). The gateway token must have `Run` permissions.
  * Your Cloudflare account ID. To find it, refer to [Find your account and zone IDs](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/).
  * Credentials for Anthropic requests. Use either [Unified Billing](https://developers.cloudflare.com/ai-gateway/features/unified-billing/) credits or an Anthropic API key stored in AI Gateway as a [provider key (BYOK)](https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/).
  * Claude Desktop installed and updated to the latest version.



Note

For the simplest setup, set Claude Desktop's gateway API key to your Cloudflare gateway token. If you set the gateway API key to your own Anthropic API key instead, add `cf-aig-authorization: Bearer <CF_AIG_TOKEN>` as a custom inference header so AI Gateway can authenticate the request.

  1. In Claude Desktop, select **Help** > **Troubleshooting** > **Enable Developer Mode**.

  2. Select **Developer** > **Configure Third-Party Inference**.

  3. In **Connection** , set the connection type to _Gateway_.

  4. In **Gateway credentials** , set **Credential kind** to _Static API key_.

  5. Set **Gateway API key** to your Cloudflare gateway token.

Replace `<CF_AIG_TOKEN>` with your gateway token.
         
         <CF_AIG_TOKEN>

  6. Set **Gateway auth scheme** to _Bearer_.

  7. Set the gateway base URL to your gateway's Anthropic endpoint.

Replace `<ACCOUNT_ID>` and `<GATEWAY_ID>` with your values.
         
         https://gateway.ai.cloudflare.com/v1/<ACCOUNT_ID>/<GATEWAY_ID>/anthropic

  8. In **Models** , add the Claude model you want to use.

Field | Value  
---|---  
Model ID | `claude-sonnet-4-5`  
Display name | `Claude Sonnet 4.5`  
Tier alias | `sonnet`  
  
  9. In **Gateway credentials** , select **Test connection**.

  10. Start a Claude Desktop conversation. Requests now route through AI Gateway.




To confirm traffic reaches AI Gateway, refer to [Verify it works](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/#verify-it-works).

[PreviousClaude Code](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/claude-code/)[NextGitHub Copilot CLI](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/github-copilot-cli/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/integrations/coding-agents/claude-desktop.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
