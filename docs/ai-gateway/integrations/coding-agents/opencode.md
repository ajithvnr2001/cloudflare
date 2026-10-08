---
url: https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/opencode/
title: OpenCode \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:32.144552+00:00
---

# OpenCode · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/opencode/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /…

Integrations

  4. /[Coding agents](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/)
  5. /OpenCode



# OpenCode

Last updated Sep 10, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/opencode/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesConnect with a gateway tokenUse with Cloudflare Access

[OpenCode ↗︎](https://opencode.ai/) is an open source coding agent that supports custom provider configuration. Point its built-in providers at AI Gateway to observe and control model requests from OpenCode.

Note

This custom setup is intended for organizations that need more control and want to distribute configuration to a team. For individual use, OpenCode's standard [Cloudflare AI Gateway provider setup ↗︎](https://opencode.ai/docs/providers/#cloudflare-ai-gateway) is usually sufficient.

## Prerequisites

Before you start, you need:

  * An AI Gateway and its gateway slug.
  * [Sufficient Unified Billing credits](https://developers.cloudflare.com/ai-gateway/features/unified-billing/#load-credits) or a stored [provider key](https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/) with the `default` alias for each provider.
  * [OpenCode installed ↗︎](https://opencode.ai/docs/).



## Connect with a gateway token

To use this method, you also need an [authenticated gateway](https://developers.cloudflare.com/ai-gateway/configuration/authentication/) and its gateway token. The token must have `Run` permissions. You also need your Cloudflare account ID. To find it, refer to [Find your account and zone IDs](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/).

  1. Set your gateway token as the `CF_AIG_TOKEN` environment variable. The following commands set it for the current session. To persist it, add it to your shell profile.

Replace `<CF_AIG_TOKEN>` with your gateway token.
         
         export CF_AIG_TOKEN="<CF_AIG_TOKEN>"
         
         $env:CF_AIG_TOKEN = "<CF_AIG_TOKEN>"

  2. In your project root, create an `opencode.json` file. Replace `<ACCOUNT_ID>` and `<GATEWAY_ID>` with your account ID and gateway slug:

opencode.jsonjson
         
         {
           "$schema": "https://opencode.ai/config.json",
           "share": "disabled",
           "disabled_providers": ["opencode"],
           "enabled_providers": ["anthropic", "openai", "google", "xai"],
           "provider": {
             "anthropic": {
               "name": "Anthropic through Cloudflare AI Gateway",
               "options": {
                 "baseURL": "https://gateway.ai.cloudflare.com/v1/<ACCOUNT_ID>/<GATEWAY_ID>/anthropic/v1",
                 "apiKey": "",
                 "headers": {
                   "cf-aig-authorization": "Bearer {env:CF_AIG_TOKEN}"
                 }
               }
             },
             "openai": {
               "name": "OpenAI through Cloudflare AI Gateway",
               "options": {
                 "baseURL": "https://gateway.ai.cloudflare.com/v1/<ACCOUNT_ID>/<GATEWAY_ID>/openai",
                 "apiKey": "",
                 "headers": {
                   "cf-aig-authorization": "Bearer {env:CF_AIG_TOKEN}"
                 }
               }
             },
             "google": {
               "name": "Google AI Studio through Cloudflare AI Gateway",
               "options": {
                 "baseURL": "https://gateway.ai.cloudflare.com/v1/<ACCOUNT_ID>/<GATEWAY_ID>/google-ai-studio/v1beta",
                 "apiKey": "",
                 "headers": {
                   "cf-aig-authorization": "Bearer {env:CF_AIG_TOKEN}"
                 }
               }
             },
             "xai": {
               "name": "xAI through Cloudflare AI Gateway",
               "options": {
                 "baseURL": "https://gateway.ai.cloudflare.com/v1/<ACCOUNT_ID>/<GATEWAY_ID>/grok/v1",
                 "apiKey": "",
                 "headers": {
                   "cf-aig-authorization": "Bearer {env:CF_AIG_TOKEN}"
                 }
               }
             }
           }
         }

Leave each `apiKey` value empty. AI Gateway supplies provider credentials through Unified Billing or your stored provider keys. To use a stored key without the `default` alias, add the [`cf-aig-byok-alias` header](https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/#key-aliases) to that provider's `headers` object. Remove providers that you do not use. For more configuration options, refer to [OpenCode providers ↗︎](https://opencode.ai/docs/providers/).

  3. Start OpenCode and select a configured provider and model:
         
         opencode




To confirm traffic reaches AI Gateway, refer to [Verify it works](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/#verify-it-works).

## Use with Cloudflare Access

If your gateway is protected by [Cloudflare Access](https://developers.cloudflare.com/ai-gateway/configuration/cloudflare-access/), OpenCode can authenticate with a short-lived Access token instead of a gateway token. You can also host the configuration centrally so users connect with one login command.

This setup requires an AI Gateway [custom domain](https://developers.cloudflare.com/ai-gateway/configuration/custom-domains/), [`cloudflared`](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/) on each user's device, and a public HTTPS location for two configuration files. You can use an [R2 bucket with a custom domain](https://developers.cloudflare.com/r2/buckets/public-buckets/#custom-domains).

The files contain configuration, but no credentials. A Single Redirect sends `/.well-known/opencode` requests from your AI Gateway custom domain to the discovery file.

Caution

OpenCode executes the `auth.command` from the discovery file. Only host these files on infrastructure that you control. Protect the configuration host and its DNS from unauthorized changes.

Users can override remote configuration in their global or project configuration. To enforce organization-wide settings, refer to [OpenCode managed settings ↗︎](https://opencode.ai/docs/config/#managed-settings).

The following example uses `ai.example.com` for the AI Gateway domain and `config.example.com` for the configuration host. Replace both hostnames with your own values.

  1. Outside any OpenCode project, create a copy of the `opencode.json` file from Connect with a gateway token. Replace each provider `baseURL` with the corresponding value:

Provider | Base URL  
---|---  
Anthropic | `https://ai.example.com/anthropic/v1`  
OpenAI | `https://ai.example.com/openai`  
Google | `https://ai.example.com/google-ai-studio/v1beta`  
xAI | `https://ai.example.com/grok/v1`  
  
Replace each provider's `headers` object with the following value:
         
         {
           "cf-access-token": "{env:TOKEN}",
           "X-Requested-With": "XMLHttpRequest"
         }

  2. Upload `opencode.json` to your public HTTPS host. Confirm that its URL returns the expected JSON without authentication.

If you use R2, upload the object to the bucket and [connect a custom domain](https://developers.cloudflare.com/r2/buckets/public-buckets/#custom-domains). The example file should be available at `https://config.example.com/opencode.json`.

Do not keep another copy in a project or global OpenCode configuration. Local configuration takes precedence over remote configuration and would prevent later hosted updates from applying.

  3. Create an `opencode` discovery file. Set `remote_config.url` to the public URL of the `opencode.json` file:

opencodejson
         
         {
           "auth": {
             "command": [
               "cloudflared",
               "access",
               "login",
               "--no-verbose",
               "-app=https://ai.example.com/"
             ],
             "env": "TOKEN"
           },
           "remote_config": {
             "url": "https://config.example.com/opencode.json"
           }
         }

OpenCode runs the authentication command and makes its output available as `{env:TOKEN}`. It then substitutes that value into the remote provider configuration.

  4. Upload `opencode` to your public HTTPS host. Confirm that `https://config.example.com/opencode` returns the discovery JSON without authentication.

  5. In the zone for your AI Gateway custom domain, [create a Single Redirect](https://developers.cloudflare.com/rules/url-forwarding/single-redirects/create-dashboard/) with these settings:

     * **Rule name** : `OpenCode discovery`
     * **Custom filter expression** : `(http.host eq "ai.example.com" and http.request.uri.path eq "/.well-known/opencode")`
     * **Target URL** : `https://config.example.com/opencode`
     * **Status code** : `302`
     * **Preserve query string** : Off
  6. In a browser without an active Access session, open `https://ai.example.com/.well-known/opencode`. Confirm that the request returns the discovery JSON without an Access prompt.

  7. To connect OpenCode, run:
         
         opencode auth login https://ai.example.com

Complete the Access login flow when prompted. OpenCode stores the resulting credential locally and loads the remote configuration. Run the command again when the Access session expires.

  8. Start OpenCode and select a configured provider and model:
         
         opencode




[PreviousOpenAI Codex](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/openai-codex/)[NextPi](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/pi/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/integrations/coding-agents/opencode.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
