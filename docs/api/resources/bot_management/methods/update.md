---
url: https://developers.cloudflare.com/api/resources/bot_management/methods/update/
title: Update Zone Bot Management Config | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:24:28.565603+00:00
---

# Update Zone Bot Management Config | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/bot_management/methods/update/

[API Reference](https://developers.cloudflare.com/api)

[Bot Management](https://developers.cloudflare.com/api/resources/bot_management)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Update Zone Bot Management Config

PUT/zones/{zone_id}/bot_management

Updates the Bot Management configuration for a zone.

This API is used to update:

  * **Bot Fight Mode**
  * **Super Bot Fight Mode**
  * **Bot Management for Enterprise**



See [Bot Plans](https://developers.cloudflare.com/bots/plans/) for more information on the different plans   
If you recently upgraded or downgraded your plan, refer to the following examples to clean up old configurations. Copy and paste the example body to remove old zone configurations based on your current plan.

#### Clean up configuration for Bot Fight Mode plan
    
    
    {
      "sbfm_likely_automated": "allow",
      "sbfm_definitely_automated": "allow",
      "sbfm_verified_bots": "allow",
      "sbfm_static_resource_protection": false,
      "optimize_wordpress": false,
      "suppress_session_score": false
    }

#### Clean up configuration for SBFM Pro plan
    
    
    {
      "sbfm_likely_automated": "allow",
      "fight_mode": false
    }

#### Clean up configuration for SBFM Biz plan
    
    
    {
      "fight_mode": false
    }

#### Clean up configuration for BM Enterprise Subscription plan

It is strongly recommended that you ensure you have [custom rules](https://developers.cloudflare.com/waf/custom-rules/) in place to protect your zone before disabling the SBFM rules. Without these protections, your zone is vulnerable to attacks.
    
    
    {
      "sbfm_likely_automated": "allow",
      "sbfm_definitely_automated": "allow",
      "sbfm_verified_bots": "allow",
      "sbfm_static_resource_protection": false,
      "optimize_wordpress": false,
      "fight_mode": false
    }

##### Security

API Token

The preferred authorization scheme for interacting with the Cloudflare API. [Create a token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/).

**Example:**`Authorization: Bearer Sn3lZJTBX6kkg7OdcBUAxOO963GEIyGQqnFTOFYY`

API Email + API Key

The previous authorization scheme for interacting with the Cloudflare API, used in conjunction with a Global API key.

**Example:**`X-Auth-Email: user@example.com`

The previous authorization scheme for interacting with the Cloudflare API. When possible, use API tokens instead of Global API keys.

**Example:**`X-Auth-Key: 144c9defac04969c7bfad8efaa8ea194`

##### Accepted Permissions (at least one required)

`Bot Management Write`

##### Path ParametersExpand Collapse 

zone_id: string

Identifier.

maxLength32

##### Body ParametersJSONExpand Collapse 

body: [BotFightModeConfiguration](https://developers.cloudflare.com/api/resources/bot_management#\(resource\)%20bot_management%20%3E%20\(model\)%20bot_fight_mode_configuration%20%3E%20\(schema\)) { ai_bots_migration_opt_out, ai_bots_protection, ai_search, 12 more }  or [SuperBotFightModeDefinitelyConfiguration](https://developers.cloudflare.com/api/resources/bot_management#\(resource\)%20bot_management%20%3E%20\(model\)%20super_bot_fight_mode_definitely_configuration%20%3E%20\(schema\)) { ai_bots_migration_opt_out, ai_bots_protection, ai_search, 15 more }  or [SuperBotFightModeLikelyConfiguration](https://developers.cloudflare.com/api/resources/bot_management#\(resource\)%20bot_management%20%3E%20\(model\)%20super_bot_fight_mode_likely_configuration%20%3E%20\(schema\)) { ai_bots_migration_opt_out, ai_bots_protection, ai_search, 16 more }  or [SubscriptionConfiguration](https://developers.cloudflare.com/api/resources/bot_management#\(resource\)%20bot_management%20%3E%20\(model\)%20subscription_configuration%20%3E%20\(schema\)) { ai_bots_migration_opt_out, ai_bots_protection, ai_search, 14 more } 

One of the following:

BotFightModeConfiguration object { ai_bots_migration_opt_out, ai_bots_protection, ai_search, 12 more } 

ai_bots_migration_opt_out: optional boolean

Temporary migration flag tracking zones opted out of AI bots managed-rule updates.

ai_bots_protection: optional "block" or "disabled" or "only_on_ad_pages"

Enable rule to block AI Scrapers and Crawlers.

One of the following:

"block"

"disabled"

"only_on_ad_pages"

ai_search: optional "disabled" or "block" or "only_on_ad_pages"

Configure robots.txt policy for AI search bots.

One of the following:

"disabled"

"block"

"only_on_ad_pages"

ai_training: optional "disabled" or "disallow" or "block" or "only_on_ad_pages"

Configure robots.txt policy for AI model training bots.

One of the following:

"disabled"

"disallow"

"block"

"only_on_ad_pages"

ai_user: optional "disabled" or "block" or "only_on_ad_pages"

Configure robots.txt policy for AI assistant and agent bots.

One of the following:

"disabled"

"block"

"only_on_ad_pages"

bot_preference_sync_enabled: optional boolean

Enable Bot Preference Sync for this zone. When enabled, Cloudflare can serve robots.txt content derived from the zone’s AI Search, AI User, and AI Training preferences.

cf_robots_variant: optional "off" or "policy_only"

Specifies the Robots Access Control License variant to use.

One of the following:

"off"

"policy_only"

content_bots_protection: optional "block" or "disabled"

Enable rule to block content bots. When enabled, blocks automated traffic with low bot scores, excluding safe verified bot categories. Exceptions should be managed via skip rules.

One of the following:

"block"

"disabled"

crawler_protection: optional "enabled" or "disabled"

Enable rule to punish AI Scrapers and Crawlers via a link maze.

One of the following:

"enabled"

"disabled"

enable_js: optional boolean

Use lightweight, invisible JavaScript detections to improve Bot Management. [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/).

fight_mode: optional boolean

Whether to enable Bot Fight Mode.

is_robots_txt_managed: optional boolean

Enable cloudflare managed robots.txt. If an existing robots.txt is detected, then managed robots.txt will be prepended to the existing robots.txt.

jsd_api_results_enabled: optional boolean

Whether to use JavaScript Detection results submitted through the API for this zone.

stale_zone_configuration: optional object { optimize_wordpress, sbfm_definitely_automated, sbfm_likely_automated, 3 more } 

A read-only field that shows which unauthorized settings are currently active on the zone. These settings typically result from upgrades or downgrades.

optimize_wordpress: optional boolean

Indicates that the zone’s wordpress optimization for SBFM is turned on.

sbfm_definitely_automated: optional string

Indicates that the zone’s definitely automated requests are being blocked or challenged.

sbfm_likely_automated: optional string

Indicates that the zone’s likely automated requests are being blocked or challenged.

sbfm_static_resource_protection: optional string

Indicates that the zone’s static resource protection is turned on.

sbfm_verified_bots: optional string

Indicates that the zone’s verified bot requests are being blocked.

suppress_session_score: optional boolean

Indicates that the zone’s session score tracking is disabled.

using_latest_model: optional boolean

A read-only field that indicates whether the zone currently is running the latest ML model.

SuperBotFightModeDefinitelyConfiguration object { ai_bots_migration_opt_out, ai_bots_protection, ai_search, 15 more } 

ai_bots_migration_opt_out: optional boolean

Temporary migration flag tracking zones opted out of AI bots managed-rule updates.

ai_bots_protection: optional "block" or "disabled" or "only_on_ad_pages"

Enable rule to block AI Scrapers and Crawlers.

One of the following:

"block"

"disabled"

"only_on_ad_pages"

ai_search: optional "disabled" or "block" or "only_on_ad_pages"

Configure robots.txt policy for AI search bots.

One of the following:

"disabled"

"block"

"only_on_ad_pages"

ai_training: optional "disabled" or "disallow" or "block" or "only_on_ad_pages"

Configure robots.txt policy for AI model training bots.

One of the following:

"disabled"

"disallow"

"block"

"only_on_ad_pages"

ai_user: optional "disabled" or "block" or "only_on_ad_pages"

Configure robots.txt policy for AI assistant and agent bots.

One of the following:

"disabled"

"block"

"only_on_ad_pages"

bot_preference_sync_enabled: optional boolean

Enable Bot Preference Sync for this zone. When enabled, Cloudflare can serve robots.txt content derived from the zone’s AI Search, AI User, and AI Training preferences.

cf_robots_variant: optional "off" or "policy_only"

Specifies the Robots Access Control License variant to use.

One of the following:

"off"

"policy_only"

content_bots_protection: optional "block" or "disabled"

Enable rule to block content bots. When enabled, blocks automated traffic with low bot scores, excluding safe verified bot categories. Exceptions should be managed via skip rules.

One of the following:

"block"

"disabled"

crawler_protection: optional "enabled" or "disabled"

Enable rule to punish AI Scrapers and Crawlers via a link maze.

One of the following:

"enabled"

"disabled"

enable_js: optional boolean

Use lightweight, invisible JavaScript detections to improve Bot Management. [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/).

is_robots_txt_managed: optional boolean

Enable cloudflare managed robots.txt. If an existing robots.txt is detected, then managed robots.txt will be prepended to the existing robots.txt.

jsd_api_results_enabled: optional boolean

Whether to use JavaScript Detection results submitted through the API for this zone.

optimize_wordpress: optional boolean

Whether to optimize Super Bot Fight Mode protections for Wordpress.

sbfm_definitely_automated: optional "allow" or "block" or "managed_challenge"

Super Bot Fight Mode (SBFM) action to take on definitely automated requests.

One of the following:

"allow"

"block"

"managed_challenge"

sbfm_static_resource_protection: optional boolean

Super Bot Fight Mode (SBFM) to enable static resource protection. Enable if static resources on your application need bot protection. Note: Static resource protection can also result in legitimate traffic being blocked.

sbfm_verified_bots: optional "allow" or "block"

Super Bot Fight Mode (SBFM) action to take on verified bots requests.

One of the following:

"allow"

"block"

stale_zone_configuration: optional object { fight_mode, sbfm_likely_automated } 

A read-only field that shows which unauthorized settings are currently active on the zone. These settings typically result from upgrades or downgrades.

fight_mode: optional boolean

Indicates that the zone’s Bot Fight Mode is turned on.

sbfm_likely_automated: optional string

Indicates that the zone’s likely automated requests are being blocked or challenged.

using_latest_model: optional boolean

A read-only field that indicates whether the zone currently is running the latest ML model.

SuperBotFightModeLikelyConfiguration object { ai_bots_migration_opt_out, ai_bots_protection, ai_search, 16 more } 

ai_bots_migration_opt_out: optional boolean

Temporary migration flag tracking zones opted out of AI bots managed-rule updates.

ai_bots_protection: optional "block" or "disabled" or "only_on_ad_pages"

Enable rule to block AI Scrapers and Crawlers.

One of the following:

"block"

"disabled"

"only_on_ad_pages"

ai_search: optional "disabled" or "block" or "only_on_ad_pages"

Configure robots.txt policy for AI search bots.

One of the following:

"disabled"

"block"

"only_on_ad_pages"

ai_training: optional "disabled" or "disallow" or "block" or "only_on_ad_pages"

Configure robots.txt policy for AI model training bots.

One of the following:

"disabled"

"disallow"

"block"

"only_on_ad_pages"

ai_user: optional "disabled" or "block" or "only_on_ad_pages"

Configure robots.txt policy for AI assistant and agent bots.

One of the following:

"disabled"

"block"

"only_on_ad_pages"

bot_preference_sync_enabled: optional boolean

Enable Bot Preference Sync for this zone. When enabled, Cloudflare can serve robots.txt content derived from the zone’s AI Search, AI User, and AI Training preferences.

cf_robots_variant: optional "off" or "policy_only"

Specifies the Robots Access Control License variant to use.

One of the following:

"off"

"policy_only"

content_bots_protection: optional "block" or "disabled"

Enable rule to block content bots. When enabled, blocks automated traffic with low bot scores, excluding safe verified bot categories. Exceptions should be managed via skip rules.

One of the following:

"block"

"disabled"

crawler_protection: optional "enabled" or "disabled"

Enable rule to punish AI Scrapers and Crawlers via a link maze.

One of the following:

"enabled"

"disabled"

enable_js: optional boolean

Use lightweight, invisible JavaScript detections to improve Bot Management. [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/).

is_robots_txt_managed: optional boolean

Enable cloudflare managed robots.txt. If an existing robots.txt is detected, then managed robots.txt will be prepended to the existing robots.txt.

jsd_api_results_enabled: optional boolean

Whether to use JavaScript Detection results submitted through the API for this zone.

optimize_wordpress: optional boolean

Whether to optimize Super Bot Fight Mode protections for Wordpress.

sbfm_definitely_automated: optional "allow" or "block" or "managed_challenge"

Super Bot Fight Mode (SBFM) action to take on definitely automated requests.

One of the following:

"allow"

"block"

"managed_challenge"

sbfm_likely_automated: optional "allow" or "block" or "managed_challenge"

Super Bot Fight Mode (SBFM) action to take on likely automated requests.

One of the following:

"allow"

"block"

"managed_challenge"

sbfm_static_resource_protection: optional boolean

Super Bot Fight Mode (SBFM) to enable static resource protection. Enable if static resources on your application need bot protection. Note: Static resource protection can also result in legitimate traffic being blocked.

sbfm_verified_bots: optional "allow" or "block"

Super Bot Fight Mode (SBFM) action to take on verified bots requests.

One of the following:

"allow"

"block"

stale_zone_configuration: optional object { fight_mode } 

A read-only field that shows which unauthorized settings are currently active on the zone. These settings typically result from upgrades or downgrades.

fight_mode: optional boolean

Indicates that the zone’s Bot Fight Mode is turned on.

using_latest_model: optional boolean

A read-only field that indicates whether the zone currently is running the latest ML model.

SubscriptionConfiguration object { ai_bots_migration_opt_out, ai_bots_protection, ai_search, 14 more } 

ai_bots_migration_opt_out: optional boolean

Temporary migration flag tracking zones opted out of AI bots managed-rule updates.

ai_bots_protection: optional "block" or "disabled" or "only_on_ad_pages"

Enable rule to block AI Scrapers and Crawlers.

One of the following:

"block"

"disabled"

"only_on_ad_pages"

ai_search: optional "disabled" or "block" or "only_on_ad_pages"

Configure robots.txt policy for AI search bots.

One of the following:

"disabled"

"block"

"only_on_ad_pages"

ai_training: optional "disabled" or "disallow" or "block" or "only_on_ad_pages"

Configure robots.txt policy for AI model training bots.

One of the following:

"disabled"

"disallow"

"block"

"only_on_ad_pages"

ai_user: optional "disabled" or "block" or "only_on_ad_pages"

Configure robots.txt policy for AI assistant and agent bots.

One of the following:

"disabled"

"block"

"only_on_ad_pages"

auto_update_model: optional boolean

Automatically update to the newest bot detection models created by Cloudflare as they are released. [Learn more.](https://developers.cloudflare.com/bots/reference/machine-learning-models#model-versions-and-release-notes)

bm_cookie_enabled: optional boolean

Indicates that the bot management cookie can be placed on end user devices accessing the site. Defaults to true

bot_preference_sync_enabled: optional boolean

Enable Bot Preference Sync for this zone. When enabled, Cloudflare can serve robots.txt content derived from the zone’s AI Search, AI User, and AI Training preferences.

cf_robots_variant: optional "off" or "policy_only"

Specifies the Robots Access Control License variant to use.

One of the following:

"off"

"policy_only"

content_bots_protection: optional "block" or "disabled"

Enable rule to block content bots. When enabled, blocks automated traffic with low bot scores, excluding safe verified bot categories. Exceptions should be managed via skip rules.

One of the following:

"block"

"disabled"

crawler_protection: optional "enabled" or "disabled"

Enable rule to punish AI Scrapers and Crawlers via a link maze.

One of the following:

"enabled"

"disabled"

enable_js: optional boolean

Use lightweight, invisible JavaScript detections to improve Bot Management. [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/).

is_robots_txt_managed: optional boolean

Enable cloudflare managed robots.txt. If an existing robots.txt is detected, then managed robots.txt will be prepended to the existing robots.txt.

jsd_api_results_enabled: optional boolean

Whether to use JavaScript Detection results submitted through the API for this zone.

stale_zone_configuration: optional object { fight_mode, optimize_wordpress, sbfm_definitely_automated, 3 more } 

A read-only field that shows which unauthorized settings are currently active on the zone. These settings typically result from upgrades or downgrades.

fight_mode: optional boolean

Indicates that the zone’s Bot Fight Mode is turned on.

optimize_wordpress: optional boolean

Indicates that the zone’s wordpress optimization for SBFM is turned on.

sbfm_definitely_automated: optional string

Indicates that the zone’s definitely automated requests are being blocked or challenged.

sbfm_likely_automated: optional string

Indicates that the zone’s likely automated requests are being blocked or challenged.

sbfm_static_resource_protection: optional string

Indicates that the zone’s static resource protection is turned on.

sbfm_verified_bots: optional string

Indicates that the zone’s verified bot requests are being blocked.

suppress_session_score: optional boolean

Whether to disable tracking the highest bot score for a session in the Bot Management cookie.

using_latest_model: optional boolean

A read-only field that indicates whether the zone currently is running the latest ML model.

##### ReturnsExpand Collapse 

errors: array of object { code, message, documentation_url, source } 

code: number

minimum1000

message: string

documentation_url: optional string

source: optional object { pointer } 

pointer: optional string

messages: array of object { code, message, documentation_url, source } 

code: number

minimum1000

message: string

documentation_url: optional string

source: optional object { pointer } 

pointer: optional string

success: true

Whether the API call was successful.

result: optional [BotFightModeConfiguration](https://developers.cloudflare.com/api/resources/bot_management#\(resource\)%20bot_management%20%3E%20\(model\)%20bot_fight_mode_configuration%20%3E%20\(schema\)) { ai_bots_migration_opt_out, ai_bots_protection, ai_search, 12 more }  or [SuperBotFightModeDefinitelyConfiguration](https://developers.cloudflare.com/api/resources/bot_management#\(resource\)%20bot_management%20%3E%20\(model\)%20super_bot_fight_mode_definitely_configuration%20%3E%20\(schema\)) { ai_bots_migration_opt_out, ai_bots_protection, ai_search, 15 more }  or [SuperBotFightModeLikelyConfiguration](https://developers.cloudflare.com/api/resources/bot_management#\(resource\)%20bot_management%20%3E%20\(model\)%20super_bot_fight_mode_likely_configuration%20%3E%20\(schema\)) { ai_bots_migration_opt_out, ai_bots_protection, ai_search, 16 more }  or [SubscriptionConfiguration](https://developers.cloudflare.com/api/resources/bot_management#\(resource\)%20bot_management%20%3E%20\(model\)%20subscription_configuration%20%3E%20\(schema\)) { ai_bots_migration_opt_out, ai_bots_protection, ai_search, 14 more } 

One of the following:

BotFightModeConfiguration object { ai_bots_migration_opt_out, ai_bots_protection, ai_search, 12 more } 

ai_bots_migration_opt_out: optional boolean

Temporary migration flag tracking zones opted out of AI bots managed-rule updates.

ai_bots_protection: optional "block" or "disabled" or "only_on_ad_pages"

Enable rule to block AI Scrapers and Crawlers.

One of the following:

"block"

"disabled"

"only_on_ad_pages"

ai_search: optional "disabled" or "block" or "only_on_ad_pages"

Configure robots.txt policy for AI search bots.

One of the following:

"disabled"

"block"

"only_on_ad_pages"

ai_training: optional "disabled" or "disallow" or "block" or "only_on_ad_pages"

Configure robots.txt policy for AI model training bots.

One of the following:

"disabled"

"disallow"

"block"

"only_on_ad_pages"

ai_user: optional "disabled" or "block" or "only_on_ad_pages"

Configure robots.txt policy for AI assistant and agent bots.

One of the following:

"disabled"

"block"

"only_on_ad_pages"

bot_preference_sync_enabled: optional boolean

Enable Bot Preference Sync for this zone. When enabled, Cloudflare can serve robots.txt content derived from the zone’s AI Search, AI User, and AI Training preferences.

cf_robots_variant: optional "off" or "policy_only"

Specifies the Robots Access Control License variant to use.

One of the following:

"off"

"policy_only"

content_bots_protection: optional "block" or "disabled"

Enable rule to block content bots. When enabled, blocks automated traffic with low bot scores, excluding safe verified bot categories. Exceptions should be managed via skip rules.

One of the following:

"block"

"disabled"

crawler_protection: optional "enabled" or "disabled"

Enable rule to punish AI Scrapers and Crawlers via a link maze.

One of the following:

"enabled"

"disabled"

enable_js: optional boolean

Use lightweight, invisible JavaScript detections to improve Bot Management. [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/).

fight_mode: optional boolean

Whether to enable Bot Fight Mode.

is_robots_txt_managed: optional boolean

Enable cloudflare managed robots.txt. If an existing robots.txt is detected, then managed robots.txt will be prepended to the existing robots.txt.

jsd_api_results_enabled: optional boolean

Whether to use JavaScript Detection results submitted through the API for this zone.

stale_zone_configuration: optional object { optimize_wordpress, sbfm_definitely_automated, sbfm_likely_automated, 3 more } 

A read-only field that shows which unauthorized settings are currently active on the zone. These settings typically result from upgrades or downgrades.

optimize_wordpress: optional boolean

Indicates that the zone’s wordpress optimization for SBFM is turned on.

sbfm_definitely_automated: optional string

Indicates that the zone’s definitely automated requests are being blocked or challenged.

sbfm_likely_automated: optional string

Indicates that the zone’s likely automated requests are being blocked or challenged.

sbfm_static_resource_protection: optional string

Indicates that the zone’s static resource protection is turned on.

sbfm_verified_bots: optional string

Indicates that the zone’s verified bot requests are being blocked.

suppress_session_score: optional boolean

Indicates that the zone’s session score tracking is disabled.

using_latest_model: optional boolean

A read-only field that indicates whether the zone currently is running the latest ML model.

SuperBotFightModeDefinitelyConfiguration object { ai_bots_migration_opt_out, ai_bots_protection, ai_search, 15 more } 

ai_bots_migration_opt_out: optional boolean

Temporary migration flag tracking zones opted out of AI bots managed-rule updates.

ai_bots_protection: optional "block" or "disabled" or "only_on_ad_pages"

Enable rule to block AI Scrapers and Crawlers.

One of the following:

"block"

"disabled"

"only_on_ad_pages"

ai_search: optional "disabled" or "block" or "only_on_ad_pages"

Configure robots.txt policy for AI search bots.

One of the following:

"disabled"

"block"

"only_on_ad_pages"

ai_training: optional "disabled" or "disallow" or "block" or "only_on_ad_pages"

Configure robots.txt policy for AI model training bots.

One of the following:

"disabled"

"disallow"

"block"

"only_on_ad_pages"

ai_user: optional "disabled" or "block" or "only_on_ad_pages"

Configure robots.txt policy for AI assistant and agent bots.

One of the following:

"disabled"

"block"

"only_on_ad_pages"

bot_preference_sync_enabled: optional boolean

Enable Bot Preference Sync for this zone. When enabled, Cloudflare can serve robots.txt content derived from the zone’s AI Search, AI User, and AI Training preferences.

cf_robots_variant: optional "off" or "policy_only"

Specifies the Robots Access Control License variant to use.

One of the following:

"off"

"policy_only"

content_bots_protection: optional "block" or "disabled"

Enable rule to block content bots. When enabled, blocks automated traffic with low bot scores, excluding safe verified bot categories. Exceptions should be managed via skip rules.

One of the following:

"block"

"disabled"

crawler_protection: optional "enabled" or "disabled"

Enable rule to punish AI Scrapers and Crawlers via a link maze.

One of the following:

"enabled"

"disabled"

enable_js: optional boolean

Use lightweight, invisible JavaScript detections to improve Bot Management. [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/).

is_robots_txt_managed: optional boolean

Enable cloudflare managed robots.txt. If an existing robots.txt is detected, then managed robots.txt will be prepended to the existing robots.txt.

jsd_api_results_enabled: optional boolean

Whether to use JavaScript Detection results submitted through the API for this zone.

optimize_wordpress: optional boolean

Whether to optimize Super Bot Fight Mode protections for Wordpress.

sbfm_definitely_automated: optional "allow" or "block" or "managed_challenge"

Super Bot Fight Mode (SBFM) action to take on definitely automated requests.

One of the following:

"allow"

"block"

"managed_challenge"

sbfm_static_resource_protection: optional boolean

Super Bot Fight Mode (SBFM) to enable static resource protection. Enable if static resources on your application need bot protection. Note: Static resource protection can also result in legitimate traffic being blocked.

sbfm_verified_bots: optional "allow" or "block"

Super Bot Fight Mode (SBFM) action to take on verified bots requests.

One of the following:

"allow"

"block"

stale_zone_configuration: optional object { fight_mode, sbfm_likely_automated } 

A read-only field that shows which unauthorized settings are currently active on the zone. These settings typically result from upgrades or downgrades.

fight_mode: optional boolean

Indicates that the zone’s Bot Fight Mode is turned on.

sbfm_likely_automated: optional string

Indicates that the zone’s likely automated requests are being blocked or challenged.

using_latest_model: optional boolean

A read-only field that indicates whether the zone currently is running the latest ML model.

SuperBotFightModeLikelyConfiguration object { ai_bots_migration_opt_out, ai_bots_protection, ai_search, 16 more } 

ai_bots_migration_opt_out: optional boolean

Temporary migration flag tracking zones opted out of AI bots managed-rule updates.

ai_bots_protection: optional "block" or "disabled" or "only_on_ad_pages"

Enable rule to block AI Scrapers and Crawlers.

One of the following:

"block"

"disabled"

"only_on_ad_pages"

ai_search: optional "disabled" or "block" or "only_on_ad_pages"

Configure robots.txt policy for AI search bots.

One of the following:

"disabled"

"block"

"only_on_ad_pages"

ai_training: optional "disabled" or "disallow" or "block" or "only_on_ad_pages"

Configure robots.txt policy for AI model training bots.

One of the following:

"disabled"

"disallow"

"block"

"only_on_ad_pages"

ai_user: optional "disabled" or "block" or "only_on_ad_pages"

Configure robots.txt policy for AI assistant and agent bots.

One of the following:

"disabled"

"block"

"only_on_ad_pages"

bot_preference_sync_enabled: optional boolean

Enable Bot Preference Sync for this zone. When enabled, Cloudflare can serve robots.txt content derived from the zone’s AI Search, AI User, and AI Training preferences.

cf_robots_variant: optional "off" or "policy_only"

Specifies the Robots Access Control License variant to use.

One of the following:

"off"

"policy_only"

content_bots_protection: optional "block" or "disabled"

Enable rule to block content bots. When enabled, blocks automated traffic with low bot scores, excluding safe verified bot categories. Exceptions should be managed via skip rules.

One of the following:

"block"

"disabled"

crawler_protection: optional "enabled" or "disabled"

Enable rule to punish AI Scrapers and Crawlers via a link maze.

One of the following:

"enabled"

"disabled"

enable_js: optional boolean

Use lightweight, invisible JavaScript detections to improve Bot Management. [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/).

is_robots_txt_managed: optional boolean

Enable cloudflare managed robots.txt. If an existing robots.txt is detected, then managed robots.txt will be prepended to the existing robots.txt.

jsd_api_results_enabled: optional boolean

Whether to use JavaScript Detection results submitted through the API for this zone.

optimize_wordpress: optional boolean

Whether to optimize Super Bot Fight Mode protections for Wordpress.

sbfm_definitely_automated: optional "allow" or "block" or "managed_challenge"

Super Bot Fight Mode (SBFM) action to take on definitely automated requests.

One of the following:

"allow"

"block"

"managed_challenge"

sbfm_likely_automated: optional "allow" or "block" or "managed_challenge"

Super Bot Fight Mode (SBFM) action to take on likely automated requests.

One of the following:

"allow"

"block"

"managed_challenge"

sbfm_static_resource_protection: optional boolean

Super Bot Fight Mode (SBFM) to enable static resource protection. Enable if static resources on your application need bot protection. Note: Static resource protection can also result in legitimate traffic being blocked.

sbfm_verified_bots: optional "allow" or "block"

Super Bot Fight Mode (SBFM) action to take on verified bots requests.

One of the following:

"allow"

"block"

stale_zone_configuration: optional object { fight_mode } 

A read-only field that shows which unauthorized settings are currently active on the zone. These settings typically result from upgrades or downgrades.

fight_mode: optional boolean

Indicates that the zone’s Bot Fight Mode is turned on.

using_latest_model: optional boolean

A read-only field that indicates whether the zone currently is running the latest ML model.

SubscriptionConfiguration object { ai_bots_migration_opt_out, ai_bots_protection, ai_search, 14 more } 

ai_bots_migration_opt_out: optional boolean

Temporary migration flag tracking zones opted out of AI bots managed-rule updates.

ai_bots_protection: optional "block" or "disabled" or "only_on_ad_pages"

Enable rule to block AI Scrapers and Crawlers.

One of the following:

"block"

"disabled"

"only_on_ad_pages"

ai_search: optional "disabled" or "block" or "only_on_ad_pages"

Configure robots.txt policy for AI search bots.

One of the following:

"disabled"

"block"

"only_on_ad_pages"

ai_training: optional "disabled" or "disallow" or "block" or "only_on_ad_pages"

Configure robots.txt policy for AI model training bots.

One of the following:

"disabled"

"disallow"

"block"

"only_on_ad_pages"

ai_user: optional "disabled" or "block" or "only_on_ad_pages"

Configure robots.txt policy for AI assistant and agent bots.

One of the following:

"disabled"

"block"

"only_on_ad_pages"

auto_update_model: optional boolean

Automatically update to the newest bot detection models created by Cloudflare as they are released. [Learn more.](https://developers.cloudflare.com/bots/reference/machine-learning-models#model-versions-and-release-notes)

bm_cookie_enabled: optional boolean

Indicates that the bot management cookie can be placed on end user devices accessing the site. Defaults to true

bot_preference_sync_enabled: optional boolean

Enable Bot Preference Sync for this zone. When enabled, Cloudflare can serve robots.txt content derived from the zone’s AI Search, AI User, and AI Training preferences.

cf_robots_variant: optional "off" or "policy_only"

Specifies the Robots Access Control License variant to use.

One of the following:

"off"

"policy_only"

content_bots_protection: optional "block" or "disabled"

Enable rule to block content bots. When enabled, blocks automated traffic with low bot scores, excluding safe verified bot categories. Exceptions should be managed via skip rules.

One of the following:

"block"

"disabled"

crawler_protection: optional "enabled" or "disabled"

Enable rule to punish AI Scrapers and Crawlers via a link maze.

One of the following:

"enabled"

"disabled"

enable_js: optional boolean

Use lightweight, invisible JavaScript detections to improve Bot Management. [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/).

is_robots_txt_managed: optional boolean

Enable cloudflare managed robots.txt. If an existing robots.txt is detected, then managed robots.txt will be prepended to the existing robots.txt.

jsd_api_results_enabled: optional boolean

Whether to use JavaScript Detection results submitted through the API for this zone.

stale_zone_configuration: optional object { fight_mode, optimize_wordpress, sbfm_definitely_automated, 3 more } 

A read-only field that shows which unauthorized settings are currently active on the zone. These settings typically result from upgrades or downgrades.

fight_mode: optional boolean

Indicates that the zone’s Bot Fight Mode is turned on.

optimize_wordpress: optional boolean

Indicates that the zone’s wordpress optimization for SBFM is turned on.

sbfm_definitely_automated: optional string

Indicates that the zone’s definitely automated requests are being blocked or challenged.

sbfm_likely_automated: optional string

Indicates that the zone’s likely automated requests are being blocked or challenged.

sbfm_static_resource_protection: optional string

Indicates that the zone’s static resource protection is turned on.

sbfm_verified_bots: optional string

Indicates that the zone’s verified bot requests are being blocked.

suppress_session_score: optional boolean

Whether to disable tracking the highest bot score for a session in the Bot Management cookie.

using_latest_model: optional boolean

A read-only field that indicates whether the zone currently is running the latest ML model.

### Update Zone Bot Management Config

HTTP

HTTP

HTTP

TypeScript

TypeScript

Python

Python

Go

Go

Terraform

Terraform
    
    
    curl https://api.cloudflare.com/client/v4/zones/$ZONE_ID/bot_management \
        -X PUT \
        -H 'Content-Type: application/json' \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
        -d '{
              "ai_bots_protection": "block",
              "ai_search": "block",
              "ai_training": "disallow",
              "ai_user": "only_on_ad_pages",
              "bot_preference_sync_enabled": true,
              "cf_robots_variant": "policy_only",
              "content_bots_protection": "disabled",
              "crawler_protection": "enabled",
              "enable_js": true,
              "fight_mode": true,
              "jsd_api_results_enabled": true
            }'

200 example
    
    
    {
      "errors": [
        {
          "code": 1000,
          "message": "message",
          "documentation_url": "documentation_url",
          "source": {
            "pointer": "pointer"
          }
        }
      ],
      "messages": [
        {
          "code": 1000,
          "message": "message",
          "documentation_url": "documentation_url",
          "source": {
            "pointer": "pointer"
          }
        }
      ],
      "success": true,
      "result": {
        "ai_bots_migration_opt_out": false,
        "ai_bots_protection": "block",
        "ai_search": "block",
        "ai_training": "disallow",
        "ai_user": "only_on_ad_pages",
        "bot_preference_sync_enabled": true,
        "cf_robots_variant": "policy_only",
        "content_bots_protection": "disabled",
        "crawler_protection": "enabled",
        "enable_js": true,
        "fight_mode": true,
        "is_robots_txt_managed": false,
        "jsd_api_results_enabled": true,
        "stale_zone_configuration": {
          "optimize_wordpress": true,
          "sbfm_definitely_automated": "sbfm_definitely_automated",
          "sbfm_likely_automated": "sbfm_likely_automated",
          "sbfm_static_resource_protection": "sbfm_static_resource_protection",
          "sbfm_verified_bots": "sbfm_verified_bots",
          "suppress_session_score": true
        },
        "using_latest_model": true
      }
    }

##### Returns Examples

200 example
    
    
    {
      "errors": [
        {
          "code": 1000,
          "message": "message",
          "documentation_url": "documentation_url",
          "source": {
            "pointer": "pointer"
          }
        }
      ],
      "messages": [
        {
          "code": 1000,
          "message": "message",
          "documentation_url": "documentation_url",
          "source": {
            "pointer": "pointer"
          }
        }
      ],
      "success": true,
      "result": {
        "ai_bots_migration_opt_out": false,
        "ai_bots_protection": "block",
        "ai_search": "block",
        "ai_training": "disallow",
        "ai_user": "only_on_ad_pages",
        "bot_preference_sync_enabled": true,
        "cf_robots_variant": "policy_only",
        "content_bots_protection": "disabled",
        "crawler_protection": "enabled",
        "enable_js": true,
        "fight_mode": true,
        "is_robots_txt_managed": false,
        "jsd_api_results_enabled": true,
        "stale_zone_configuration": {
          "optimize_wordpress": true,
          "sbfm_definitely_automated": "sbfm_definitely_automated",
          "sbfm_likely_automated": "sbfm_likely_automated",
          "sbfm_static_resource_protection": "sbfm_static_resource_protection",
          "sbfm_verified_bots": "sbfm_verified_bots",
          "suppress_session_score": true
        },
        "using_latest_model": true
      }
    }
