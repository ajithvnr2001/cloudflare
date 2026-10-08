---
url: https://developers.cloudflare.com/waf/detections/leaked-credentials/
title: Leaked credentials detection \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:41.590097+00:00
---

# Leaked credentials detection · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/detections/leaked-credentials/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /[Traffic detections](https://developers.cloudflare.com/waf/detections/)
  4. /Leaked credentials



# Leaked credentials detection

Last updated Sep 8, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/detections/leaked-credentials/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow it works Notify your origin serverAvailabilityDefault scan locationsCustom detection locationsLeaked credentials fields

The leaked credentials [traffic detection](https://developers.cloudflare.com/waf/detections/) scans incoming requests for credentials (usernames and passwords) previously leaked from [data breaches ↗︎](https://www.cloudflare.com/learning/security/what-is-a-data-breach/).

Note

If you are currently using [exposed credentials check](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/) (a previous implementation that is now deprecated), refer to [Upgrade to leaked credentials detection](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/upgrade-to-leaked-credentials-detection/) to upgrade to the new implementation.

## How it works

When you turn on leaked credentials detection, Cloudflare scans incoming HTTP requests for usernames and passwords. The scan checks authentication patterns from common web applications and any custom detection locations you configure.

Detected credentials are compared against a database of known leaked credentials. This database consists of:

  * The [Have I Been Pwned (HIBP) ↗︎](https://haveibeenpwned.com) matched passwords dataset (passwords only)
  * Cloudflare-collected credentials (usernames)
  * Leaked credentials pairs (username and password)



Based on the results, Cloudflare populates leaked credentials fields for scanned requests. You can use these fields in two ways:

  * **Analyze traffic** : Review detection results in the [Security Analytics](https://developers.cloudflare.com/waf/analytics/security-analytics/) dashboard to understand how often leaked credentials appear in your traffic.
  * **Create rules** : Use the fields in [custom rules](https://developers.cloudflare.com/waf/custom-rules/) or [rate limiting rules](https://developers.cloudflare.com/waf/rate-limiting-rules/) to challenge or block requests that contain compromised credentials.



Leaked credentials can appear in your traffic for different reasons. An attacker may be performing a [credential stuffing ↗︎](https://www.cloudflare.com/learning/bots/what-is-credential-stuffing/) attack, or a legitimate user may be reusing a previously leaked password.

### Notify your origin server

Leaked credentials detection provides a [managed transform](https://developers.cloudflare.com/rules/transform/managed-transforms/reference/#add-leaked-credentials-checks-header) that adds an `Exposed-Credential-Check` request header to matching requests. The header value indicates what was leaked — for example, `1` if both username and password were a leaked pair, `2` if the username was leaked, or `4` if only the password was leaked.

You can use this header at your origin server to warn users and prompt them to reset their password.

Note

Cloudflare does not store, log, or retain plaintext end-user passwords when performing leaked credential checks. Passwords are hashed, converted into a cryptographic representation, and then compared against a database of leaked credentials.

## Availability

For details on available features per plan, refer to [Availability](https://developers.cloudflare.com/waf/detections/#availability) in the traffic detections page.

## Default scan locations

Leaked credentials detection includes rules for identifying credentials in HTTP requests for the following well-known web applications:

  * Drupal
  * Joomla
  * Ghost
  * Magento
  * Plone
  * WordPress
  * Microsoft Exchange OWA



Additionally, the scan includes generic rules for other common web authentication patterns.

You can also configure custom detection locations to address the specific authentication mechanism used in your web applications. A custom detection location tells the Cloudflare WAF where to find usernames and passwords in HTTP requests of your web application.

## Custom detection locations

Note

Only available for Enterprise customers.

The default scan covers common web applications, but your application may send credentials in a different format or field name. Custom detection locations allow you to tell Cloudflare exactly where to find usernames and passwords in HTTP requests.

For example, if the JSON body of an HTTP request authenticating a user looks like the following:
    
    
    { "user": "<username>", "secret": "<password>" }

You could configure a custom detection location with the following settings:

  * Custom location for username:  
`lookup_json_string(http.request.body.raw, "user")`
  * Custom location for password:  
`lookup_json_string(http.request.body.raw, "secret")`



When specifying a custom detection location, only the location of the username field is required.

The following table includes example detection locations for different request types:

Request type | Username location / Password location  
---|---  
JSON body | `lookup_json_string(http.request.body.raw, "user")`  
`lookup_json_string(http.request.body.raw, "secret")`  
URL-encoded form | `url_decode(http.request.body.form["user"][0])`  
`url_decode(http.request.body.form["secret"][0])`  
Multipart form | `url_decode(http.request.body.multipart["user"][0])`  
`url_decode(http.request.body.multipart["secret"][0])`  
  
Expressions used to specify custom detection locations can include the following fields and functions:

  * Fields: 
    * [`http.request.body.form`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.form/)
    * [`http.request.body.multipart`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.multipart/)
    * [`http.request.body.raw`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.raw/)
    * [`http.request.headers`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers/)
    * [`http.request.uri.args`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.args/)
    * [`http.request.uri.query`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.query/)
  * Functions: 
    * [`lookup_json_string()`](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#lookup_json_string)
    * [`url_decode()`](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#url_decode)



For instructions on configuring a custom detection location, refer to [Get started](https://developers.cloudflare.com/waf/detections/leaked-credentials/get-started/#4-optional-configure-a-custom-detection-location).

## Leaked credentials fields

The following fields indicate the type of leaked credential match Cloudflare detected. Use these fields in [custom rules](https://developers.cloudflare.com/waf/custom-rules/) or [rate limiting rules](https://developers.cloudflare.com/waf/rate-limiting-rules/) to act on requests containing compromised credentials.

Field | Description  
---|---  
Password Leaked   
[`cf.waf.credential_check.password_leaked`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.credential_check.password_leaked/)   
`Boolean` | Indicates whether the password detected in the request was previously leaked.   
Available on all plans.  
User and Password Leaked   
[`cf.waf.credential_check.username_and_password_leaked`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.credential_check.username_and_password_leaked/)   
`Boolean` | Indicates whether the username-password pair detected in the request were previously leaked.   
Requires a Pro plan or above.  
Username Leaked   
[`cf.waf.credential_check.username_leaked`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.credential_check.username_leaked/)   
`Boolean` | Indicates whether the username detected in the request was previously leaked.   
Requires an Enterprise plan.  
Similar Password Leaked   
[`cf.waf.credential_check.username_password_similar`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.credential_check.username_password_similar/)   
`Boolean` | Indicates whether a similar version of the username and password credentials detected in the request were previously leaked.   
Requires an Enterprise plan.  
Authentication detected   
[`cf.waf.auth_detected`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.auth_detected/)   
`Boolean` | Indicates whether Cloudflare detected authentication credentials in the request.   
Requires an Enterprise plan.  
  
[PreviousFields](https://developers.cloudflare.com/waf/detections/application-profiles/fields/)[NextGet started](https://developers.cloudflare.com/waf/detections/leaked-credentials/get-started/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/detections/leaked-credentials/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
