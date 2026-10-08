---
url: https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/dns-protection/json-objects/
title: Advanced TCP Protection API - JSON objects \u00b7 Cloudflare DDoS Protection docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:44.558751+00:00
---

# Advanced TCP Protection API - JSON objects · Cloudflare DDoS Protection docs

> Source: https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/dns-protection/json-objects/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DDoS Protection](https://developers.cloudflare.com/ddos-protection/)
  3. /…

Advanced DDoS systemsAPI configuration

  4. /[Advanced DNS Protection](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/dns-protection/)
  5. /JSON objects



# JSON objects

Last updated Apr 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/dns-protection/json-objects/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

# JSON object

This page contains an example of the DNS protection rule JSON object used in the API.
    
    
    {
      "id": "31c70c65-9f81-4669-94ed-1e1e041e7b06",
      "scope": "region",
      "name": "WEUR",
      "mode": "monitoring",
      "profile_sensitivity": "medium",
      "rate_sensitivity": "medium",
      "burst_sensitivity": "medium",
      "created_on": "2023-10-01T13:10:38.762503+01:00",
      "modified_on": "2023-10-01T13:10:38.762503+01:00"
    }

The `scope` field value must be one of `global`, `region`, or `datacenter`. You must provide a region code (or data center code) in the `name` field when specifying a `region` (or `datacenter`) scope.

The `mode` value must be one of `enabled`, `disabled`, or `monitoring`.

The `profile_sensitivity` field value must be one of `low` (default), `medium`, `high`, or `very_high`.

The `rate_sensitivity` and `burst_sensitivity` field values must be one of `low`, `medium`, or `high`.

For more information on the rule settings, refer to [Rule settings](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/concepts/#rule-settings).

[PreviousCommon API calls](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/dns-protection/examples/)[NextConfigure via the API](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/tcp-protection/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ddos-protection/advanced-ddos-systems/api/dns-protection/json-objects.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
