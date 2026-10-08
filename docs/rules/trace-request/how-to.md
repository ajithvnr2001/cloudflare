---
url: https://developers.cloudflare.com/rules/trace-request/how-to/
title: How to - Cloudflare Trace \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:55.396681+00:00
---

# How to - Cloudflare Trace · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/trace-request/how-to/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /[Trace a request](https://developers.cloudflare.com/rules/trace-request/)
  4. /Use Cloudflare Trace



# Use Cloudflare Trace

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/trace-request/how-to/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUse Trace in the dashboard 1\. Configure one or more Cloudflare products 2\. Build a trace 3\. Assess results 4\. (Optional) Save the trace configurationUse Trace via APISteps in trace results

## Use Trace in the dashboard

### 1\. Configure one or more Cloudflare products

  1. Log in to the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com), and select your account.
  2. Set configuration settings at the account level, or select a domain and configure settings for one or more Cloudflare products.



### 2\. Build a trace

  1. In the Cloudflare dashboard, go to the **Trace** page.

[ Go to **Trace** ↗ ](https://dash.cloudflare.com/?to=/:account/trace)
  2. Enter a URL to trace. The URL must include a hostname that belongs to your account.

  3. Select an HTTP method. If you select _POST_ , _PUT_ , or _PATCH_ , you should enter a value in **Request Body**.

  4. (Optional) Define any custom request properties to simulate the conditions of a specific HTTP/S request. You can customize the following request properties:

     * **Protocol** (HTTP protocol version)
     * **User Agent and Request Headers**
     * **Cookies**
     * **Geolocation** (request source [country](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.country/), [region](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.region/), and [city](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.city/))
     * [**Bot Score**](https://developers.cloudflare.com/bots/concepts/bot-score/)
     * **Request Body** (for `POST`, `PUT`, and `PATCH` requests)
     * **Skip Challenge** (skips a Cloudflare-issued [challenge](https://developers.cloudflare.com/cloudflare-challenges/), if any, allowing the trace to continue)
  5. Select **Send Trace**.




### 3\. Assess results

The **Trace results** page shows all evaluated and executed configurations from different Cloudflare products, in evaluation order. Any inactive rules are not evaluated.

  1. Analyze the different steps with evaluated and executed configurations for the current trace. Trace results include matches for all active rules and configurations, whether configured at the account level or for a specific domain or subdomain.

To show all configurations, including the ones that did not match the request, select _All configurations_ in the **Results shown** dropdown.

  2. (Optional) Update your Cloudflare configuration (at the account or at the domain/subdomain level) and create a new trace to check the impact of your changes.




### 4\. (Optional) Save the trace configuration

To run a trace later with the same configuration:

  1. Copy the JSON shown in the dashboard with the current trace configuration.
  2. When creating a new trace, paste it in the JSON box to define all the settings of the new trace.



## Use Trace via API

Use the [Request Trace](https://developers.cloudflare.com/api/resources/request_tracers/subresources/traces/methods/create/) operation to perform a trace using the Cloudflare API.

* * *

## Steps in trace results

  * Execution of one or more rules of Cloudflare products built on the [Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/). Refer to the Ruleset Engine's [Phases list](https://developers.cloudflare.com/ruleset-engine/reference/phases-list/) for a list of such products.
  * [Page Rules](https://developers.cloudflare.com/rules/page-rules/): Execution of one or more rules.
  * [Workers](https://developers.cloudflare.com/workers/): Execution of one or more scripts.



[PreviousOverview](https://developers.cloudflare.com/rules/trace-request/)[NextLimitations](https://developers.cloudflare.com/rules/trace-request/limitations/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/trace-request/how-to.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
