---
url: https://developers.cloudflare.com/health-checks/how-to/zone-lockdown/
title: Zone lockdown migration guide \u00b7 Cloudflare Health Checks docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:28.839293+00:00
---

# Zone lockdown migration guide · Cloudflare Health Checks docs

> Source: https://developers.cloudflare.com/health-checks/how-to/zone-lockdown/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Health Checks](https://developers.cloudflare.com/health-checks/)
  3. /How to
  4. /Zone Lockdown



# Zone Lockdown

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/health-checks/how-to/zone-lockdown/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBypass zone lockdown Via the API

Currently, any Cloudflare customer on a paid plan can configure Health Checks against any host or IP. [Zone Lockdown](https://developers.cloudflare.com/waf/tools/zone-lockdown/) specifies a list of one or more IP addresses, CIDR ranges, or networks that are the only IPs allowed to access a domain, subdomain, or URL. It allows multiple destinations in a single rule as well as IPv4 and IPv6 addresses. IP addresses not specified in the Zone Lockdown rule are denied access to the specified resources.

Customers who use zone lockdown and want their health checks to continue passing can use [WAF custom rules](https://developers.cloudflare.com/waf/custom-rules/create-dashboard/) to bypass zone lockdown.

## Bypass zone lockdown

To bypass zone lockdown using a WAF custom rule:

  1. Follow the steps to [create a custom rule in the dashboard](https://developers.cloudflare.com/waf/custom-rules/create-dashboard/).

  2. Create a custom rule matching on **user agent**.

Cloudflare Health Checks have a user agent of the following format: `Mozilla/5.0 (compatible;Cloudflare-Healthchecks/1.0;+https://www.cloudflare.com/; healthcheck-id: XXX)` where `XXX` is replaced with the first 16 characters of the Health Check ID.

To allow a specific Health Check, verify if the user agent contains the first 16 characters of the Health Check ID.

  3. Set the action to _Skip_ and the corresponding feature to **Zone Lockdown** under **More components to skip**.




### Via the API

This example adds a new WAF custom rule to the ruleset with ID `{ruleset_id}` that skips zone lockdown for incoming requests with a user agent containing `1234567890abcdef`:
    
    
    curl "https://api.cloudflare.com/client/v4/{zone_id}/rulesets/{ruleset_id}/rules" \
    --header "Authorization: Bearer <API_TOKEN>" \
    --header "Content-Type: application/json" \
    --data '{
      "action": "skip",
      "action_parameters": {
        "products": [
          "zoneLockdown"
        ]
      },
      "expression": "http.user_agent contains \"1234567890abcdef\"",
      "description": "bypass zone lockdown - specific healthcheck"
    }'

[PreviousHealth Checks regions](https://developers.cloudflare.com/health-checks/concepts/health-checks-regions/)[NextHealth Checks notifications](https://developers.cloudflare.com/health-checks/how-to/health-checks-notifications/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/health-checks/how-to/zone-lockdown.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
