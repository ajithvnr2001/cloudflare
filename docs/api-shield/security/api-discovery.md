---
url: https://developers.cloudflare.com/api-shield/security/api-discovery/
title: Discovery \u00b7 Cloudflare API Shield docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:18.168809+00:00
---

# Discovery · Cloudflare API Shield docs

> Source: https://developers.cloudflare.com/api-shield/security/api-discovery/

  1. [Home](https://developers.cloudflare.com/)
  2. /[API Shield](https://developers.cloudflare.com/api-shield/)
  3. /[Security](https://developers.cloudflare.com/api-shield/security/)
  4. /Discovery



# Discovery

Last updated Sep 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/api-shield/security/api-discovery/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewProcess Discovered operations Discovering operationsRequirementsAvailability

Most development teams struggle to keep track of their APIs. Cloudflare Discovery helps you map out and understand your API attack surface — the full set of endpoints that could be targeted by attackers.

## Process

Cloudflare produces a map of API endpoints by applying heuristic path normalization to qualifying sampled traffic. The heuristics group requests by path structure and variable-like segment patterns.

For example, you might have thousands of APIs, but a lot of the calls look similar, such as:

  * `api.example.com/profile/238`
  * `api.example.com/profile/392`



Discovery might group both paths as `api.example.com/profile/{var1}`. Generated `{varN}` placeholders identify variable-like segments. They do not assign semantic names.

The resulting endpoint map might look like:
    
    
    /api/login/{var1}
    /api/auth
    /api/account/{var1}
    /api/password_reset
    /api/logout

Cloudflare can also consolidate common normalized operations across compatible subdomains. Operations unique to one hostname can remain on that hostname.
    
    
    us-api.example.com/api/v1/users/{var1}
    de-api.example.com/api/v1/users/{var1}
    fr-api.example.com/api/v1/users/{var1}
    jp-api.example.com/api/v1/users/{var1}

Cloudflare may consolidate these common operations to `{hostVar1}.example.com/api/v1/users/{var1}`.

For more technical details, refer to the [blog post ↗︎](https://blog.cloudflare.com/ml-api-discovery-and-schema-learning/).

### Discovered operations

Discovery results can appear as candidate or shadow operations. Candidate operations are matched at the edge. Shadow operations are not.

When a request matches a published candidate, the match can provide operation context for logs, rules, analytics, and applicable detections. You do not need to save every discovered operation.

You do not need to save every discovered operation. Save an operation to move it to the `full` state. Full operations support persisted API profiles, risk findings, and protections that require a known API endpoint.

To save a discovered operation:

  1. In the Cloudflare dashboard, go to the **Web Assets** page.

[ Go to **Web assets** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/web-assets)
  2. Go to the **Operations** tab.

  3. Open the row actions for a candidate or shadow operation.

  4. Select **Learn profile**.




Cloudflare moves the operation to the `full` state. The row action then displays **Learning profile** , which does not indicate that learning is complete. For more information, refer to [Start profile learning](https://developers.cloudflare.com/security/web-assets/manage-operations/#start-profile-learning).

### Discovering operations

Discovery uses multiple signals, including machine learning and configured session identifiers, to identify API traffic. Configuring a session identifier is optional.

To review Discovery results:

  1. In the Cloudflare dashboard, go to the **Web Assets** page.

[ Go to **Web assets** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/web-assets)
  2. Go to the **Operations** tab.

  3. Select the **Discovered** quick filter, which applies the **Candidate** and **Shadow** state filters. You can also select both states manually.




You can direct any feedback about your Discovery results to your account team.

## Requirements

Discovery requires an active API Shield subscription at both the account and zone level. If your subscription is active at the account level but not assigned to the zone, Discovery will not run for that zone.

Discovery analyzes sampled proxied traffic. Eligible requests use supported HTTP methods, use paths outside `/cdn-cgi`, and contain qualifying Discovery signals.

For an endpoint to appear in Discovery results, qualifying sampled traffic must meet the following conditions:

  * The request must return a `2xx` response code from the Cloudflare edge.
  * The request must not originate directly from a Cloudflare Worker. Traffic sent through the Cloudflare traffic simulator or other Worker-based test harnesses will not be counted toward Discovery thresholds.
  * The endpoint must receive at least 500 requests within a continuous 10-day period.



For more information, refer to [Discovery requirements](https://developers.cloudflare.com/security/web-assets/manage-operations/#discovery-requirements/).

## Availability

Discovery requires the paid API Shield add-on, which is available to Enterprise customers. Contact your account team for more information.

[PreviousOverview](https://developers.cloudflare.com/api-shield/security/)[NextVolumetric Abuse Detection](https://developers.cloudflare.com/api-shield/security/volumetric-abuse-detection/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/api-shield/security/api-discovery.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
