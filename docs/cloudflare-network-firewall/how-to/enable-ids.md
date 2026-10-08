---
url: https://developers.cloudflare.com/cloudflare-network-firewall/how-to/enable-ids/
title: Enable Intrusion Detection System (IDS) \u00b7 Cloudflare Network Firewall docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:07.224654+00:00
---

# Enable Intrusion Detection System (IDS) · Cloudflare Network Firewall docs

> Source: https://developers.cloudflare.com/cloudflare-network-firewall/how-to/enable-ids/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/)
  3. /How to
  4. /Enable IDS



# Enable IDS

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-network-firewall/how-to/enable-ids/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewIDS rulesNext steps

Cloudflare's IDS takes advantage of the threat intelligence powered by our global network and extends the capabilities of the Cloudflare Firewall to monitor and protect your network from malicious actors.

You can enable IDS through the dashboard or via the API.

Note

This feature is available for Cloudflare Advanced Network Firewall users. For access, contact your account team.

  1. In the Cloudflare dashboard, go to the [Firewall Policies ↗︎](https://dash.cloudflare.com/?to=/:account/network-security/magic_firewall) page.

  2. Select **IDS** and turn on **IDS**.




To start using IDS via the API, first create a new ruleset in the `magic-transit-ids-managed` phase with a rule which is enabled.

  1. Follow instructions in the [Rulesets Engine Page](https://developers.cloudflare.com/ruleset-engine/basic-operations/view-rulesets/) to view all rulesets for your account. You must see a ruleset with phase `magic-transit-ids-managed` and kind `managed`. If not, please contact your account team. The managed ruleset ID will be used in the next step.

  2. Create a new root ruleset with a single rule in the `magic_transit_ids_managed` phase by running:



    
    
    curl https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets \
    --header "Authorization: Bearer <API_TOKEN>" \
    --header "Content-Type: application/json" \
    --data '{
      "name": "IDS Execute ruleset",
      "description": "Ruleset to enable IDS",
      "kind": "root",
      "phase": "magic_transit_ids_managed",
      "rules": [
        {
          "enabled": true,
          "expression": "true",
          "action": "execute",
          "description": "enable ids",
          "action_parameters": {
            "id": "${managed_ruleset_id}"
          }
        }
      ]
    }'

With this ruleset added, IDS will start inspecting packets and report any anomalous traffic. Next, you can [configure Logpush](https://developers.cloudflare.com/cloudflare-network-firewall/how-to/use-logpush-with-ids/) to start receiving details about the anomalous traffic.

  3. Use the rule created in the previous step to enable or disable IDS. The Rulesets API documentation describes [how to patch a rule](https://developers.cloudflare.com/ruleset-engine/rulesets-api/update-rule/).   
  
For example, the following patch request to set the `enabled` field to `false` will disable IDS. The ruleset and rule ID from the ruleset created in the previous step are used below.


    
    
    curl --request PATCH \
    https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets/{root_ruleset_id}/rules/{rule_id} \
    --header "Authorization: Bearer <API_TOKEN>" \
    --header "Content-Type: application/json" \
    --data '{
      "enabled": false,
      "expression": "true",
      "action": "execute",
      "action_parameters": {
        "id": "${managed_ruleset_id}"
      }
    }'

Similarly, sending a patch request with the `enabled` field set to `true` will enable IDS.

## IDS rules

IDS rules are run on a subset of packets. IDS also supports the current flows:

  * Cloudflare WAN to Cloudflare WAN.
  * Magic Transit ingress traffic (when egress traffic is handled through direct server return).
  * Magic Transit ingress and egress traffic when Magic Transit has the [Egress option enabled](https://developers.cloudflare.com/reference-architecture/architectures/magic-transit/#magic-transit-with-egress-option-enabled).



## Next steps

You must configure Logpush to log detected risks. Refer to [Configure a Logpush destination](https://developers.cloudflare.com/cloudflare-network-firewall/how-to/use-logpush-with-ids/) for more information. Additionally, all traffic that is analyzed can be accessed via [network analytics](https://developers.cloudflare.com/analytics/network-analytics/). Refer to [GraphQL Analytics](https://developers.cloudflare.com/cloudflare-network-firewall/tutorials/graphql-analytics/) to query the analytics data.

[PreviousAdd custom policies](https://developers.cloudflare.com/cloudflare-network-firewall/how-to/add-policies/)[NextEnable user roles](https://developers.cloudflare.com/cloudflare-network-firewall/how-to/enable-roles/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-network-firewall/how-to/enable-ids.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
