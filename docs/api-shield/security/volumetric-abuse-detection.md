---
url: https://developers.cloudflare.com/api-shield/security/volumetric-abuse-detection/
title: Volumetric Abuse Detection \u00b7 Cloudflare API Shield docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:19.638803+00:00
---

# Volumetric Abuse Detection · Cloudflare API Shield docs

> Source: https://developers.cloudflare.com/api-shield/security/volumetric-abuse-detection/

  1. [Home](https://developers.cloudflare.com/)
  2. /[API Shield](https://developers.cloudflare.com/api-shield/)
  3. /[Security](https://developers.cloudflare.com/api-shield/security/)
  4. /Volumetric Abuse Detection



# Volumetric Abuse Detection

Last updated Sep 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/api-shield/security/volumetric-abuse-detection/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewProcess Requirements Rate limiting recommendation calculation Create rate limitsAPISpecial cases Rate limit by JWT claim Rate limit by user tierLimitationsAvailability

Cloudflare Volumetric Abuse Detection generates adaptive, per-session rate limit recommendations for individual operations as traffic patterns change.

Cloudflare looks for endpoint abuse based on user traffic to individual endpoints.

For example, your API might see different levels of traffic to a `/reset-password` endpoint than a `/login` endpoint. Additionally, your `/login` endpoint might see higher than average traffic after a successful marketing campaign.

These two scenarios speak to the limitations of traditional rate limiting. Not only does traffic vary between endpoints, but it also can vary over time for the same endpoint. Volumetric Abuse Detection solves these problems using unsupervised learning (analyzing traffic patterns without predefined rules) to develop separate baselines for each endpoint and adjust to changes in user behavior over time.

Volumetric Abuse Detection rate limits are generated on a per-session basis rather than per IP address. This reduces false positives when traffic to your API increases, because rate limits track individual sessions rather than shared IP addresses.

Volumetric Abuse Detection rate limits are a way to prevent blatant volumetric abuse while minimizing false positives. If you are trying to prevent abusive bot traffic altogether, refer to Cloudflare's [Bot solutions](https://developers.cloudflare.com/bots/).

## Process

Volumetric Abuse Detection groups requests into 10-minute periods for each session. It uses the distribution of these request volumes to recommend one per-session threshold for each eligible operation.

To access the operations list, go to **Security** > **Web Assets** > **Operations**.

Recommendations will continue to update if your traffic pattern changes.

### Requirements

Volumetric Abuse Detection requires sufficient eligible traffic during the seven-day analysis window to produce a reliable recommendation. If a recommendation is unavailable for an operation, it might not have enough eligible traffic.

A [session identifier](https://developers.cloudflare.com/api-shield/get-started/#to-set-up-session-identifiers), such as an authorization token available as a request header or cookie, must be configured so Cloudflare can perform per-session analysis.

After adding or changing a session identifier, allow at least 24 hours for recommendations to appear. Recommendations may take longer or remain unavailable if Cloudflare cannot collect enough eligible traffic or calculate a threshold.

### Rate limiting recommendation calculation

Select an operation row in the operations list to view its rate limit recommendation. The detail view shows the suggested threshold as the overall recommendation, percentile-based values (p50, p90, p99), and a confidence classification calculated by the dashboard.

Percentile values

Percentile values describe the distribution of request counts across observed per-session, 10-minute buckets. For example, a p90 value of `83` means that approximately 90% of these buckets contained 83 or fewer requests.

Cloudflare calculates each recommendation from requests in the previous seven days. The recommendation may not change if your traffic profile remains consistent.

Cloudflare recommends using the overall rate limit recommendation rather than a single percentile value. The overall recommendation accounts for variation across all your API sessions. Choosing a single percentile value may cause false positives due to a high number of outliers.

In the operations list, you can review the dashboard confidence classification for each recommendation.

Implementing low confidence rate limits can still be helpful to prevent API abuse. If the confidence level is low, start your rate limit rule in `log` mode and observe violations for false positives before switching to `block`.

### Create rate limits

Refer to the [Rules documentation](https://developers.cloudflare.com/waf/rate-limiting-rules/create-zone-dashboard/) for more information on how to create an Advanced Rate Limiting rule.

## API

[Rate limit recommendations are available via the API](https://developers.cloudflare.com/api/resources/api_gateway/subresources/operations/methods/get/) if you would like to dynamically update rate limits over time.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Account API Gateway`
  * `Account API Gateway Read`
  * `Domain API Gateway`
  * `Domain API Gateway Read`

Get a web or API operationbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/api_gateway/operations/$OPERATION_ID" \
    	--request GET \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

## Special cases

### Rate limit by JWT claim

Rate Limiting can use string claims from a valid JSON Web Token (JWT) as rate-limit characteristics. This includes registered claims, such as `sub`, and custom claims.

For nested claims, pass each object key separately to [`lookup_json_string()`](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#lookup_json_string). For example, use `"user", "email"` to access `user.email`.

Only valid JWTs populate JWT claim fields. If a rule also matches requests without the selected claim, those requests use a separate missing-value counter. Refer to [Missing field versus empty value](https://developers.cloudflare.com/waf/rate-limiting-rules/parameters/#missing-field-versus-empty-value).

For per-user limits, select a claim that uniquely identifies the user, such as `sub` when it is unique within your application. Requests with the same characteristic value share a rate-limit counter.

### Rate limit by user tier

To apply different per-user limits by tier, create one rate limiting rule for each tier. Match the tier claim in the rule expression and use a separate user identifier claim as the rate-limit characteristic.

For example, a free-tier rule can use:

Example rule expressiontxt
    
    
    lookup_json_string(http.request.jwt.claims["<JWT_TOKEN_CONFIGURATION_ID>"][0], "tier") eq "free"

Use `sub` as the rate-limit characteristic and set the limit to five requests per minute. Create another rule that matches `"tier" eq "premium"` and applies the appropriate premium-tier limit.

## Limitations

A configured session identifier alone does not guarantee a recommendation. Cloudflare must also have sufficient eligible traffic and successfully calculate a threshold. To enable session-based rate limits, [subscribe to Advanced Rate Limiting](https://developers.cloudflare.com/waf/rate-limiting-rules/#availability).

## Availability

Volumetric Abuse Detection is only available for Enterprise customers. If you are an Enterprise customer interested in this product, contact your account team.

[PreviousDiscovery](https://developers.cloudflare.com/api-shield/security/api-discovery/)[NextSequence Analytics](https://developers.cloudflare.com/api-shield/security/sequence-analytics/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/api-shield/security/volumetric-abuse-detection.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
