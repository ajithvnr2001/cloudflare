---
url: https://developers.cloudflare.com/cloudflare-network-firewall/how-to/filter-views/
title: Filter different views \u00b7 Cloudflare Network Firewall docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:07.512257+00:00
---

# Filter different views · Cloudflare Network Firewall docs

> Source: https://developers.cloudflare.com/cloudflare-network-firewall/how-to/filter-views/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/)
  3. /How to
  4. /Filter different views



# Filter different views

Last updated May 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-network-firewall/how-to/filter-views/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewFilter by enabled or disabled rulesFilter by allowed or blocked trafficFilter by relevant fields to Network Firewall

You can utilize different [Log filters](https://developers.cloudflare.com/logs/logpush/logpush-job/filters/) to only view specific data from Cloudflare Network Firewall (formerly Magic Firewall).

## Filter by enabled or disabled rules

Use the filter examples below to filter your Network Firewall traffic to display events for enabled or disabled rules.

The example below only displays fields relevant to Network Firewall, and the filter only displays events for disabled rules.
    
    
    curl https://api.cloudflare.com/client/v4/accounts/{account_id}/logpush/jobs \
    --header "X-Auth-Email: <EMAIL>" \
    --header "X-Auth-Key: <API_KEY>" \
    --header "Content-Type: application/json" \
    --data '{
      ...
      "output_options": {
          "field_names": ["ColoName", "Datetime", "Direction", "IPDestinationAddress", "IPDestinationSubnet", "IPProtocol","IPSourceAddress", "IPSourceSubnet", "Outcome", "RuleID", "RulesetID", "SampleInterval", "Verdict"],
      },
      "filter": "{\"where\":{\"or\":[{\"and\":[{\"key\":\"MitigationSystem\",\"operator\":\"eq\",\"value\":\"magic-firewall\"},{\"key\":\"RulesetID\",\"operator\":\"!eq\",\"value\":\"\"},{\"key\":\"Outcome\",\"operator\":\"eq\",\"value\":\"pass\"},{\"key\":\"Verdict\",\"operator\":\"eq\",\"value\":\"drop\"}]}]}}"
    }'

The example below only displays fields relevant to Network Firewall, and the filter only displays events for enabled rules.
    
    
    curl https://api.cloudflare.com/client/v4/accounts/{account_id}/logpush/jobs \
    --header "X-Auth-Email: <EMAIL>" \
    --header "X-Auth-Key: <API_KEY>" \
    --header "Content-Type: application/json" \
    --data '{
      ...
      "output_options": {
          "field_names": ["ColoName", "Datetime", "Direction", "IPDestinationAddress", "IPDestinationSubnet", "IPProtocol","IPSourceAddress", "IPSourceSubnet", "Outcome", "RuleID", "RulesetID", "SampleInterval", "Verdict"],
      },
      "filter": "{\"where\":{\"or\":[{\"and\":[{\"key\":\"MitigationSystem\",\"operator\":\"eq\",\"value\":\"magic-firewall\"},{\"key\":\"RulesetID\",\"operator\":\"!eq\",\"value\":\"\"},{\"or\":[{\"key\":\"Outcome\",\"operator\":\"eq\",\"value\":\"drop\"},{\"key\":\"Verdict\",\"operator\":\"eq\",\"value\":\"pass\"}]}]}]}}"
    }'

## Filter by allowed or blocked traffic

Use the filter examples below to filter your Network Firewall traffic to display events for allowed or blocked traffic.

The example below only displays fields relevant to Network Firewall, and the filter only displays events where no explicit action was taken, for example, a packet "fell through" Network Firewall. This example does not have any rules applied.
    
    
    curl https://api.cloudflare.com/client/v4/accounts/{account_id}/logpush/jobs \
    --header "X-Auth-Email: <EMAIL>" \
    --header "X-Auth-Key: <API_KEY>" \
    --header "Content-Type: application/json" \
    --data '{
      ...
      "output_options": {
          "field_names": ["ColoName", "Datetime", "Direction", "IPDestinationAddress", "IPDestinationSubnet", "IPProtocol","IPSourceAddress", "IPSourceSubnet", "Outcome", "RuleID", "RulesetID", "SampleInterval", "Verdict"],
      },
      "filter": "{\"where\":{\"and\":[{\"key\":\"MitigationSystem\",\"operator\":\"eq\",\"value\":\"magic-firewall\"},{\"key\":\"RulesetID\",\"operator\":\"eq\",\"value\":\"\"}]}}"
    }'

The example below only displays fields relevant to Network Firewall, and the filter only displays events where explicit action was taken. The example includes both enabled and disabled Network Firewall rules.
    
    
    curl https://api.cloudflare.com/client/v4/accounts/{account_id}/logpush/jobs \
    --header "X-Auth-Email: <EMAIL>" \
    --header "X-Auth-Key: <API_KEY>" \
    --header "Content-Type: application/json" \
    --data '{
      ...
      "output_options": {
          "field_names": ["ColoName", "Datetime", "Direction", "IPDestinationAddress", "IPDestinationSubnet", "IPProtocol","IPSourceAddress", "IPSourceSubnet", "Outcome", "RuleID", "RulesetID", "SampleInterval", "Verdict"],
      },
      "filter": "{\"where\":{\"and\":[{\"key\":\"MitigationSystem\",\"operator\":\"eq\",\"value\":\"magic-firewall\"},{\"key\":\"RulesetID\",\"operator\":\"!eq\",\"value\":\"\"}]}}"
    }'

## Filter by relevant fields to Network Firewall

Use the examples below to filter out fields that are not relevant to traffic flowing through Network Firewall. The example below only includes Network Firewall events.
    
    
    curl https://api.cloudflare.com/client/v4/accounts/{account_id}/logpush/jobs \
    --header "X-Auth-Email: <EMAIL>" \
    --header "X-Auth-Key: <API_KEY>" \
    --header "Content-Type: application/json" \
    --data '{
      ...
      "output_options": {
          "field_names": ["ColoName", "Datetime", "Direction", "IPDestinationAddress", "IPDestinationSubnet", "IPProtocol","IPSourceAddress", "IPSourceSubnet", "Outcome", "RuleID", "RulesetID", "SampleInterval", "Verdict"],
      },
      "filter": "{\"where\":{\"key\":\"MitigationSystem\",\"operator\":\"eq\",\"value\":\"magic-firewall\"}}"
    }'

[PreviousEnable Managed Rulesets](https://developers.cloudflare.com/cloudflare-network-firewall/how-to/enable-managed-rulesets/)[NextUse Logpush with IDS](https://developers.cloudflare.com/cloudflare-network-firewall/how-to/use-logpush-with-ids/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-network-firewall/how-to/filter-views.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
