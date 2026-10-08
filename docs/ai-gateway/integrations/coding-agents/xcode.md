---
url: https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/xcode/
title: Xcode \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:31.412163+00:00
---

# Xcode · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/xcode/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /…

Integrations

  4. /[Coding agents](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/)
  5. /Xcode



# Xcode

Last updated Oct 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/xcode/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites

[Xcode ↗︎](https://developer.apple.com/xcode/) supports internet-hosted chat providers that use the OpenAI Chat Completions API. Point a chat provider at an AI Gateway [custom domain](https://developers.cloudflare.com/ai-gateway/configuration/custom-domains/) protected by Cloudflare Access. Xcode authenticates with an Access service token stored as its API key.

This integration uses static credentials. Xcode cannot use `cloudflared` to generate short-lived Access tokens.

## Prerequisites

Before you start, you need:

  * An AI Gateway with a [custom domain](https://developers.cloudflare.com/ai-gateway/configuration/custom-domains/).
  * Cloudflare Access enabled on the custom domain.
  * An Access [service token](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/) allowed by a **Service Auth** policy.
  * The Access application configured to [authenticate service tokens with the `Authorization` header](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/#authenticate-with-a-single-header).
  * [Unified Billing](https://developers.cloudflare.com/ai-gateway/features/unified-billing/) credits or a stored [provider key](https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/) for each model.
  * Xcode installed and updated to the latest version.



Note

Service token requests do not include `cf.user_id` because they do not represent an individual Access user. You cannot filter AI Gateway logs by user for these requests.

  1. In Xcode, go to **Xcode** > **Settings** > **Intelligence**.

  2. Under **Chat** , select **Add a Chat Provider** > **Internet Hosted**.

  3. Enter a name for the provider, such as `AI Gateway`.

  4. For **URL** , enter your AI Gateway custom domain followed by `/compat`.

Replace `ai.example.com` with your custom domain.
         
         https://ai.example.com/compat

Xcode appends `/v1/models` to list available models. It sends prompts to `/v1/chat/completions`. AI Gateway accepts both paths under the `compat` endpoint.

Note

The `/compat` endpoint is deprecated for standard single-model calls. Xcode requires an endpoint that supports both `/v1/models` and `/v1/chat/completions`. The AI Gateway REST API does not provide a `/v1/models` endpoint.

  5. For **API Key** , enter the following single-header service token value. Replace `<CLIENT_ID>` and `<CLIENT_SECRET>` with your Access service token values.
         
         {"cf-access-client-id":"<CLIENT_ID>","cf-access-client-secret":"<CLIENT_SECRET>"}

  6. Set **API Key Header** to `Authorization`.

  7. Select **Add**.

  8. Enable a model, then select it in the coding assistant and send a prompt. Requests now route through AI Gateway.




For more information about custom chat providers, refer to [Setting up coding intelligence ↗︎](https://developer.apple.com/documentation/xcode/setting-up-coding-intelligence).

To confirm traffic reaches AI Gateway, refer to [Verify it works](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/#verify-it-works).

[PreviousVisual Studio Code](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/vs-code/)[NextGemini CLI](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/gemini-cli/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/integrations/coding-agents/xcode.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
