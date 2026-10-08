---
url: https://developers.cloudflare.com/logs/logpull/enabling-log-retention/
title: Enabling log retention \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:09.999669+00:00
---

# Enabling log retention · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/logpull/enabling-log-retention/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /[Logpull](https://developers.cloudflare.com/logs/logpull/)
  4. /Enabling log retention



# Enabling log retention

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/logpull/enabling-log-retention/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEndpointsExample API requests using cURL Check log retention status Turn on log retention Turn off log retentionAudit

By default, your HTTP request logs are not retained. When using the Logpull API for the first time, you will need to enable retention. You can also turn off retention at any time. Note that after retention is turned off, previously saved logs will be available until the retention period expires (refer to [Data retention period](https://developers.cloudflare.com/logs/logpull/understanding-the-basics/#data-retention-period)).

## Endpoints

There are two endpoints for managing log retention:

  * `GET /logs/control/retention/flag` \- returns the current status of retention
  * `POST /logs/control/retention/flag` \- turns retention on or off



Note

In the Linux examples below we use the optional [jq](https://developers.cloudflare.com/logs/logpush/parsing-json-log-data/) tool to help parse the response data.

To make a `POST` call, you must have zone-scoped `edit` permissions, such as Super Administrator, Administrator, or Log Share. Refer to [Make API calls](https://developers.cloudflare.com/fundamentals/api/how-to/make-api-calls/) for more information.

## Example API requests using cURL

### Check log retention status

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Logs Write`
  * `Logs Read`

Get log retention flagbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/logs/control/retention/flag" \
    	--request GET \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"
    
    
    curl.exe "https://api.cloudflare.com/client/v4/zones/{zone_id}/logs/control/retention/flag" ^
    --header "Authorization: Bearer <API_TOKEN>"
    
    
    $uri = "https://api.cloudflare.com/client/v4/zones/{zone_id}/logs/control/retention/flag"
    $headers = @{"Authorization" = "Bearer <API_TOKEN>"}
    Invoke-RestMethod -Uri $uri -Method Get -Headers $headers

If the zone has log retention [enabled](https://developers.cloudflare.com/logs/logpull/enabling-log-retention/#enabled-response) you get the value `true`, whereas a value of `false` is returned when it is [disabled](https://developers.cloudflare.com/logs/logpull/enabling-log-retention/#disabled-response).

### Turn on log retention

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Logs Write`

Update log retention flagbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/logs/control/retention/flag" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"flag": true
    	}'
    
    
    curl.exe "https://api.cloudflare.com/client/v4/zones/{zone_id}/logs/control/retention/flag" ^
    --request POST ^
    --header "Authorization: Bearer <API_TOKEN>" ^
    --header "Content-Type: application/json" ^
    --data "{""flag"": true}"
    
    
    $uri = "https://api.cloudflare.com/client/v4/zones/{zone_id}/logs/control/retention/flag"
    $headers = @{"Authorization" = "Bearer <API_TOKEN>"}
    $bodyFlag = @{flag = $true} | ConvertTo-Json
    Invoke-RestMethod -Uri $uri -Method Post -Headers $headers -Body $bodyFlag -ContentType "application/json"

#### Enabled response
    
    
    {
    	"flag": true
    }

### Turn off log retention

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Logs Write`

Update log retention flagbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/logs/control/retention/flag" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"flag": false
    	}'
    
    
    curl.exe "https://api.cloudflare.com/client/v4/zones/{zone_id}/logs/control/retention/flag" ^
    --header "Authorization: Bearer <API_TOKEN>" ^
    --header "Content-Type: application/json" ^
    --data "{""flag"": false}"
    
    
    $uri = "https://api.cloudflare.com/client/v4/zones/{zone_id}/logs/control/retention/flag"
    $headers = @{"Authorization" = "Bearer <API_TOKEN>"}
    $bodyFlag = @{flag = $false} | ConvertTo-Json
    Invoke-RestMethod -Uri $uri -Method Post -Headers $headers -Body $bodyFlag -ContentType "application/json"

#### Disabled response
    
    
    {
    	"flag": false
    }

## Audit

Turning log retention on or off is recorded in [Cloudflare Audit Logs](https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/#access-audit-logs).

[PreviousUnderstanding the basics](https://developers.cloudflare.com/logs/logpull/understanding-the-basics/)[NextRequesting logs](https://developers.cloudflare.com/logs/logpull/requesting-logs/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/logpull/enabling-log-retention.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
