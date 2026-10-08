---
url: https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/gemini-cli/
title: Gemini CLI \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:30.631806+00:00
---

# Gemini CLI · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/gemini-cli/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /…

Integrations

  4. /[Coding agents](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/)
  5. /Gemini CLI



# Gemini CLI

Last updated Oct 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/gemini-cli/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites

[Gemini CLI ↗︎](https://github.com/google-gemini/gemini-cli) supports a custom Google Gemini API base URL. Point it at an AI Gateway [custom domain](https://developers.cloudflare.com/ai-gateway/configuration/custom-domains/) protected by Cloudflare Access. Use `cloudflared` to generate a short-lived Access token before you start Gemini CLI.

Gemini CLI does not support an API key helper. You must refresh the token when the Access session expires.

## Prerequisites

Before you start, you need:

  * An AI Gateway with a [custom domain](https://developers.cloudflare.com/ai-gateway/configuration/custom-domains/).
  * Cloudflare Access enabled on the custom domain with a policy that allows your identity.
  * Credentials for Google AI Studio. Use [Unified Billing](https://developers.cloudflare.com/ai-gateway/features/unified-billing/) credits or store a Google AI Studio key in AI Gateway with [BYOK (Store Keys)](https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/).
  * [`cloudflared`](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/) installed.
  * [Gemini CLI ↗︎](https://github.com/google-gemini/gemini-cli) installed and updated to the latest version.



  1. Set the Google Gemini base URL to your AI Gateway custom domain. Replace `ai.example.com` with your custom domain.
         
         export GOOGLE_GEMINI_BASE_URL="https://ai.example.com/google-ai-studio"

  2. Authenticate to Access and store the resulting token in `GEMINI_API_KEY`.
         
         export GEMINI_API_KEY="$(cloudflared access login -app https://ai.example.com)"

  3. Start Gemini CLI and send a prompt. Requests now route through AI Gateway.
         
         gemini




Run the authentication command again when the Access token expires. You can also add these commands to a bootstrap script that starts Gemini CLI.

For more information about these environment variables, refer to [Gemini CLI configuration ↗︎](https://github.com/google-gemini/gemini-cli/blob/main/docs/reference/configuration.md#environment-variables-and-env-files).

To confirm traffic reaches AI Gateway, refer to [Verify it works](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/#verify-it-works).

[PreviousXcode](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/xcode/)[NextTutorials](https://developers.cloudflare.com/ai-gateway/tutorials/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/integrations/coding-agents/gemini-cli.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
