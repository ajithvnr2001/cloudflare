---
url: https://developers.cloudflare.com/api-shield/security/sequence-analytics/
title: Sequence Analytics \u00b7 Cloudflare API Shield docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:19.240356+00:00
---

# Sequence Analytics · Cloudflare API Shield docs

> Source: https://developers.cloudflare.com/api-shield/security/sequence-analytics/

  1. [Home](https://developers.cloudflare.com/)
  2. /[API Shield](https://developers.cloudflare.com/api-shield/)
  3. /[Security](https://developers.cloudflare.com/api-shield/security/)
  4. /Sequence Analytics



# Sequence Analytics

Last updated Sep 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/api-shield/security/sequence-analytics/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewProcess Sequence building Sequence scoring Secure your API Repeated sequencesAvailabilityLimitations

Sequence Analytics tracks the order of API endpoint requests over time, allowing you to discover how users interact with your API. Sequence Analytics groups and highlights important user journeys (sequences) across your API. You can enforce preferred sequences using [Sequence mitigation](https://developers.cloudflare.com/api-shield/security/sequence-mitigation/).

## Process

### Sequence building

A sequence is a time-ordered list of HTTP API requests made by a specific visitor as they browse a website, use a mobile app, or interact with a B2B partner via API.

For example, a portion of a sequence made during a bank funds transfer could look like:

Order | Method | Path | Description  
---|---|---|---  
1 | `GET` | `/api/v1/users/{user_id}/accounts` | `user_id` is the active user.  
2 | `GET` | `/api/v1/accounts/{account_id}/balance` | `account_id` is one of the user’s accounts.  
3 | `GET` | `/api/v1/accounts/{account_id}/balance` | `account_id` is a different account belonging to the user.  
4 | `POST` | `/api/v1/transferFunds` | This contains a request body detailing an account to transfer funds from, an account to transfer funds to, and an amount of money to transfer.  
  
API Shield uses your configured session identifier and operations in the `full` or `candidate` state to build a set of ordered API operations (HTTP host, method, and path) requested per session. API Shield may surface sequences in various lengths depending on how it scores the sequences.

### Sequence scoring

API Shield scores sequences by a metric called precedence score. Sequence Analytics displays sequences by the highest precedence score. High-scoring sequences contain API requests which are likely to occur together in order.

Using the example above, a high score means that the last operation in the sequence `POST /api/v1/transferFunds` is highly likely to be preceded by the other operations in sequence `GET /api/v1/users/{user_id}/accounts` followed by `GET /api/v1/accounts/{account_id}/balance`. The scores are probabilities, which API Shield estimates using data from the last 24 hours.

### Secure your API

To proactively secure your API, you should inspect your highest-scoring sequences. For each high-scoring sequence, you should confirm with your development team if the final operation in the sequence must legitimately always be preceded by the other operations in the sequence.

Using the above example, if `POST /api/v1/transferFunds` must legitimately always be preceded by `GET /api/v1/users/{user_id}/accounts` and `GET /api/v1/accounts/{account_id}/balance`, you should create an **Allow** rule in sequence mitigation on the final operation of the sequence.

You should also consider applying other API Shield protections to these endpoints ([rate limiting suggestions](https://developers.cloudflare.com/api-shield/security/volumetric-abuse-detection/), [Schema validation](https://developers.cloudflare.com/api-shield/security/schema-validation/), [JWT validation](https://developers.cloudflare.com/api-shield/security/jwt-validation/), and [mTLS](https://developers.cloudflare.com/api-shield/security/mtls/)).

For more information, refer to the [blog post ↗︎](https://blog.cloudflare.com/api-sequence-analytics).

### Repeated sequences

To facilitate exploration, Sequence Analytics collapses successive requests to the same operation into one when no other operation occurs between them.

## Availability

Sequence Analytics is available for all API Shield customers. Pro, Business, and Enterprise customers who have not purchased API Shield can get started by [enabling the API Shield trial ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/security/api-shield) in the Cloudflare dashboard or contacting your account manager.

## Limitations

Sequence Analytics currently requires a session identifier and operations that API Shield can match at the edge. Ensure that you have [set up your session identifier(s)](https://developers.cloudflare.com/api-shield/get-started/#session-identifiers) and reviewed your operations in the `full` and `candidate` states in [Web Assets](https://developers.cloudflare.com/security/web-assets/manage-operations/#operation-states).

Sequences are currently limited to nine operations in length.

[PreviousVolumetric Abuse Detection](https://developers.cloudflare.com/api-shield/security/volumetric-abuse-detection/)[NextOverview](https://developers.cloudflare.com/api-shield/security/sequence-mitigation/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/api-shield/security/sequence-analytics.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
