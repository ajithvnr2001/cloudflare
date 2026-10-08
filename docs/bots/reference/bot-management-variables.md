---
url: https://developers.cloudflare.com/bots/reference/bot-management-variables/
title: Bot Management variables \u00b7 Cloudflare bot solutions docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:34.437811+00:00
---

# Bot Management variables · Cloudflare bot solutions docs

> Source: https://developers.cloudflare.com/bots/reference/bot-management-variables/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Bots](https://developers.cloudflare.com/bots/)
  3. /Reference
  4. /Bot Management variables



# Bot Management variables

Last updated Sep 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/bots/reference/bot-management-variables/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRuleset Engine fieldsWorkers variablesO2O and subrequestsCorporate ProxyLog fieldsEphemeral IDs

## Ruleset Engine fields

Bot Management provides access to several [fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/?field-category=Bots) within the expression builder of Ruleset Engine-based products such as [WAF custom rules](https://developers.cloudflare.com/waf/custom-rules/) and [Cache Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/).

  * **Bot Score** (`cf.bot_management.score`): An integer between 1-99 that indicates [Cloudflare's level of certainty](https://developers.cloudflare.com/bots/concepts/bot-score/) that a request comes from a bot.

  * **Verified Bot** (`cf.bot_management.verified_bot`): A boolean value that indicates whether a request originates from a Cloudflare allowed bot.

Cloudflare maintains a large allowlist of good, automated bots (such as Google Search Engine and Pingdom) that perform beneficial tasks. Cloudflare identifies and verifies these bots primarily through reverse DNS validation, ensuring the source IP matches the requesting service.

We also use additional validation methods, including checking ASN blocks and public lists. If these methods are unavailable, Cloudflare utilizes internal data and machine learning to identify and verify legitimate IP addresses from good bots. Most customers choose to [allow this traffic](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.bot_management.verified_bot/).

  * **Serves Static Resource** (`cf.bot_management.static_resource`): An identifier that matches [file extensions](https://developers.cloudflare.com/bots/additional-configurations/static-resources/) for many types of static resources. Use this variable if you send emails that retrieve static images.

  * **ja3Hash** (`cf.bot_management.ja3_hash`) and **ja4** (`cf.bot_management.ja4`): A [**JA3/JA4 fingerprint**](https://developers.cloudflare.com/bots/additional-configurations/ja3-ja4-fingerprint/) helps you profile specific SSL/TLS clients across different destination IPs, Ports, and X509 certificates.

  * **Bot Detection IDs** (`cf.bot_management.detection_ids`): List of IDs that correlate to the Bot Management heuristic detections made on a request (you can have multiple heuristic detections on the same request).

  * **Bot Tags** (`cf.bot_management.tags`): A list of tags associated with bot traffic.

  * **Signed Agent** (`cf.bot_management.signed_agent`): A boolean value that indicates whether the request originated from a known agent that self-identifies with Web Bot Auth. Such agents are now classified as [verified bots and agents](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/) labeled as intermediary.

  * **Verified Bot Categories** (`cf.verified_bot_category`): A string that allows you to segment your verified bot traffic by its [type and purpose](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/#legacy-categories).




## Workers variables

These variables are also available as part of the [request.cf](https://developers.cloudflare.com/workers/runtime-apis/request/#incomingrequestcfproperties) object via Cloudflare Workers:

  * `request.cf.botManagement.score`
  * `request.cf.botManagement.verifiedBot`
  * `request.cf.botManagement.staticResource`
  * `request.cf.botManagement.ja3Hash`
  * `request.cf.botManagement.ja4`
  * `request.cf.botManagement.jsDetection.passed`
  * `request.cf.botManagement.detectionIds`
  * `request.cf.botManagement.signedAgent`
  * `request.cf.verifiedBotCategory`



## O2O and subrequests

For Orange-to-Orange (O2O) traffic and any related subrequests where Bot Management is in effect, Bot Management fields (including bot score, verified bot, and JA3/JA4) represent the eyeball (end-user) connection to your platform.

Eyeball signals are preserved through the O2O chain, so the fields must be present regardless of which O2O request path you reach.

## Corporate Proxy

The Bot Management Corporate Proxy field contains identified cloud-based corporate proxies and secure web gateways that are Enterprise-only, and provide outbound security services to their clients.

You can access the Corporate Proxy field in [WAF custom rules](https://developers.cloudflare.com/waf/custom-rules/), [Rate limiting rules](https://developers.cloudflare.com/waf/rate-limiting-rules/), or [Workers](https://developers.cloudflare.com/workers/) to provide different security rules for traffic from these sources. You can also exempt them from rules using Bot Management scores.

Exampletxt
    
    
    not cf.bot_management.verified_bot
    and not cf.bot_management.static_resource
    and not  cf.bot_management.corporate_proxy
    and cf.bot_management.score lt 30

## Log fields

Once you enable Bot Management, Cloudflare also surfaces bot information in its [HTTP requests log fields](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/http_requests/):

  * BotDetectionIDs
  * BotScore
  * BotScoreSrc
  * BotTags



## Ephemeral IDs

[Ephemeral IDs](https://developers.cloudflare.com/turnstile/additional-configuration/ephemeral-id/) are short-lived device identifiers returned in the [Turnstile Siteverify API](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/) response under `metadata.ephemeral_id`. They are not Ruleset Engine fields and cannot be used in WAF custom rules or Workers directly.

Note

Ephemeral IDs require **Enterprise Bot Management** with the Turnstile Enterprise add-on, or a standalone **Enterprise Turnstile** subscription. The feature must be enabled by your Cloudflare account team and cannot be self-activated.

Refer to [Ephemeral IDs](https://developers.cloudflare.com/turnstile/additional-configuration/ephemeral-id/) for implementation details and the full enablement process.

[PreviousIP validation](https://developers.cloudflare.com/bots/reference/bot-verification/ip-validation/)[NextMachine Learning models](https://developers.cloudflare.com/bots/reference/machine-learning-models/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/bots/reference/bot-management-variables.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
