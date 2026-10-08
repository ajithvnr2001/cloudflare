---
url: https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/
title: Service tokens \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:24.263396+00:00
---

# Service tokens · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Access controls](https://developers.cloudflare.com/cloudflare-one/access-controls/)

  4. /Service credentials
  5. /Service tokens



# Service tokens

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate a service token Client Secret formatConnect your service to Access RequestStrict service token authenticationRotate service token secretsRenew service tokensManage inactive service tokensTurn a service token on or offRevoke service tokensSet a token expiration alert

You can provide automated systems with service tokens to authenticate against your Cloudflare One policies. Cloudflare Access will generate service tokens that consist of a Client ID and a Client Secret. Automated systems or applications can then use these values to reach an application protected by Access.

This section covers how to create, rotate, renew, disable, and revoke a service token. You can also configure Access to manage inactive service tokens automatically.

## Create a service token

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Access controls** > **Service credentials** > **Service Tokens**.

  2. Select **Create Service Token**.

  3. Name the service token. The name allows you to easily identify events related to the token in the logs and to revoke the token individually.

  4. Choose a **Service Token Duration**. This sets the expiration date for the token.

  5. Select **Generate token**. You will see the generated Client ID and Client Secret for the service token, as well as their respective request headers.

  6. Copy the Client Secret.

Caution

This is the only time Cloudflare Access will display the Client Secret. If you lose the Client Secret, you must generate a new service token.




  1. Make a `POST` request to the [Access Service Tokens](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/service_tokens/methods/create/) endpoint:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:
     * `Access: Service Tokens Write`
Create a service tokenbash
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/access/service_tokens" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"name": "CI/CD token",
    		"duration": "8760h"
    	}'

  2. Copy the `client_id` and `client_secret` values returned in the response.

Responsejson
         
         "result": {
         	"client_id": "88bf3b6d86161464f6509f7219099e57.access",
         	"client_secret": "bdd31cbc4dec990953e39163fbbb194c93313ca9f0a6e420346af9d326b1d2a5",
         	"created_at": "2025-09-25T22:26:26Z",
         	"expires_at": "2026-09-25T22:26:26Z",
         	"id": "3537a672-e4d8-4d89-aab9-26cb622918a1",
         	"name": "CI/CD token",
         	"updated_at": "2025-09-25T22:26:26Z",
         	"duration": "8760h",
         	"client_secret_version": 1
         }

Caution

This is the only time Cloudflare Access will display the Client Secret. If you lose the Client Secret, you must generate a new service token.




  1. Add the following permission to your [`cloudflare_api_token` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/api_token):

     * `Access: Service Tokens Write`
  2. Configure the [`cloudflare_zero_trust_access_service_token` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zero_trust_access_service_token) resource:
         
         resource "cloudflare_zero_trust_access_service_token" "example_service_token" {
         	account_id = var.cloudflare_account_id
         	name       = "Example service token"
         	duration  = "8760h"
         
         	lifecycle {
         		create_before_destroy = true
         	}
         }

  3. Get the Client ID and Client Secret of the service token:

Example: Output to CLI

     1. Output the Client ID and Client Secret to the Terraform state file: 
            
            output "example_service_token_client_id" {
            	value     = cloudflare_zero_trust_access_service_token.example_service_token.client_id
            }
            
            output "example_service_token_client_secret" {
            	value     = cloudflare_zero_trust_access_service_token.example_service_token.client_secret
            	sensitive = true
            }

     2. Apply the configuration: 
            
            terraform apply

     3. Read the Client ID and Client Secret: 
            
            terraform output -raw example_service_token_client_id
            
            terraform output -raw example_service_token_client_secret

Example: Store in HashiCorp Vault
    
    	resource "vault_generic_secret" "example_service_token" {
    		path         = "kv/cloudflare/example_service_token"
    
    		data_json = jsonencode({
    			"CLIENT_ID"     = cloudflare_access_service_token.example_service_token.client_id
    			"CLIENT_SECRET" = cloudflare_access_service_token.example_service_token.client_secret
    		})
    	}




You can now configure your Access applications and [device enrollment permissions](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/device-enrollment/#check-for-service-token) to accept this service token. Make sure to set the policy action to [**Service Auth**](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/#service-auth); otherwise, Access will prompt for an identity provider login.

### Client Secret format

As of August 26, 2026, new service token Client Secrets use the format `cfast_[40 alphanumeric characters][8-character checksum]`. The prefix and checksum make the secrets easier for credential scanning tools to identify.

Existing Client Secrets use a 64-character hexadecimal format. These secrets continue to work and do not require rotation. Both formats use the same Client ID and authentication headers.

## Connect your service to Access

### Request

To authenticate to an Access application using your service token, add the following to the headers of any HTTP request:

`CF-Access-Client-Id: <CLIENT_ID>`

`CF-Access-Client-Secret: <CLIENT_SECRET>`

For example,
    
    
    curl -H "CF-Access-Client-Id: <CLIENT_ID>" -H "CF-Access-Client-Secret: <CLIENT_SECRET>" https://app.example.com

#### Authenticate with a single header

You can configure a self-hosted Access application to accept a service token in a single HTTP header, as an alternative to the `CF-Access-Client-Id` and `CF-Access-Client-Secret` pair of headers. This is useful for authenticating SaaS services that only support sending one custom header in a request (for example, the `Authorization` header).

To authenticate using a single header:

  1. Get your existing Access application configuration:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:
     * `Access: Apps and Policies Write`
     * `Access: Apps and Policies Read`
Get an Access applicationbash
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/access/apps/$APP_ID" \
    	--request GET \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

  2. Make a `PUT` request with the name of the header you want to use for service token authentication. To avoid overwriting your existing configuration, the `PUT` request body should contain all fields returned by the previous `GET` request.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:
     * `Access: Apps and Policies Write`
Update an Access applicationbash
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/access/apps/$APP_ID" \
    	--request PUT \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"domain": "app.example.com",
    		"type": "self_hosted",
    		"read_service_tokens_from_header": "Authorization"
    	}'

  3. Add the header to any HTTP request. For example,
         
         curl -H "Authorization: {\"cf-access-client-id\": \"<CLIENT_ID>\", \"cf-access-client-secret\": \"<CLIENT_SECRET>\"}" https://app.example.com




## Strict service token authentication

Strict service token authentication is a Zero Trust organization setting that applies consistent behavior to requests made with service tokens. When the setting is on, Access handles requests with service token headers as follows:

  * If authentication or authorization fails, Access always returns `401` or `403` instead of redirecting the client to the login page with `302`.
  * Only Service Auth policies can authorize the request. Access ignores Allow policies and any `CF_Authorization` cookie sent with the request.
  * Access does not return a `CF_Authorization` cookie to the client after successful authentication. Subsequent requests should continue to use service token headers.
  * Failed requests for recognized service tokens appear in [Access authentication logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/#non-identity-authentication). Access logs expired or disabled tokens, incorrect Client Secrets, and tokens not authorized for the application. It does not log malformed headers or unknown Client IDs.



Zero Trust organizations created on or after `2026-10-05` have strict service token authentication turned on by default and cannot turn it off. Cloudflare recommends that existing organizations turn it on as well.

Note

Organizations created before `2026-10-05` can turn this setting on or off.

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Access controls** > **Access settings**.

[ Go to **Access settings** ↗ ](https://one.dash.cloudflare.com/?to=/:account/access-controls/settings)
  2. Under **Manage service tokens** , turn on **Strict service token authentication**.

  3. In the confirmation dialog, select **Enable**.




To turn off strict service token authentication, turn off the setting and select **Disable**.

Send a `PATCH` request to the [Update your Zero Trust organization](https://developers.cloudflare.com/api/resources/zero_trust/subresources/organizations/methods/update/) endpoint:
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/%7Baccount_id%7D/access/organizations" \
    	--request PATCH \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"strict_service_token_auth": true
    	}'

To turn off strict service token authentication, set `strict_service_token_auth` to `false`.

## Rotate service token secrets

Rotate a service token secret when you suspect exposure or as part of regular credential rotation. The Client ID remains the same, but Access generates a new Client Secret.

You can set a grace period during which both secrets work. Use this period to update your services before Access revokes the previous secret.

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Access controls** > **Service credentials** > **Service Tokens**.

[ Go to ****↗](https://one.dash.cloudflare.com/?to=/:account/access/service-auth/service-tokens)
  2. Locate the token and select the three dots > **Rotate secret**.

  3. In **Keep the current secret valid for** , choose when Access should revoke the current secret. Available grace periods range from one hour to 30 days. To revoke it when you rotate, select _Revoke immediately_.

  4. Select **Rotate**.

  5. Copy the new Client Secret and update your services before the grace period ends.




Make a `POST` request to the [Rotate a service token](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/service_tokens/methods/rotate/) endpoint. Set `previous_client_secret_expires_at` to an RFC 3339 timestamp when the previous secret should expire:

Rotate a service tokenbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/access/service_tokens/$SERVICE_TOKEN_ID/rotate" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"previous_client_secret_expires_at": "2030-01-01T00:00:00Z"
    	}'

To revoke the previous secret immediately, omit `previous_client_secret_expires_at` from the request.

## Renew service tokens

Service tokens expire according to the token duration you selected when you created the token.

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Access controls** > **Service credentials** > **Service Tokens**.
  2. Locate the token you want to renew.
  3. To extend the token's lifetime by one year, select **Refresh**.
  4. To extend the token's lifetime by more than a year: 
     1. Select **Edit**.
     2. Choose a new **Service Token Duration**.
     3. Select **Save**. The expiration date will be extended by the selected amount of time.



To extend the token's lifetime by one year, make a `POST` request to the [Refresh a service token](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/service_tokens/methods/refresh/) endpoint:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Access: Service Tokens Write`

Refresh a service tokenbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/access/service_tokens/$SERVICE_TOKEN_ID/refresh" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

To extend the token's lifetime by a custom duration, make a `PUT` request to the [Update a service token](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/service_tokens/methods/update/) endpoint with the new `duration`:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Access: Service Tokens Write`

Update a service tokenbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/access/service_tokens/$SERVICE_TOKEN_ID" \
    	--request PUT \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"duration": "17520h"
    	}'

To renew the service token, update the `duration` attribute on the [`cloudflare_zero_trust_access_service_token` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zero_trust_access_service_token) resource and apply the change. Cloudflare resets the expiration relative to the time of the update.
    
    
    resource "cloudflare_zero_trust_access_service_token" "example_service_token" {
    	account_id = var.cloudflare_account_id
    	name       = "Example service token"
    	duration   = "17520h"
    
    	lifecycle {
    		create_before_destroy = true
    	}
    }

## Manage inactive service tokens

You can configure Access to automatically disable or delete service tokens that are no longer in use. The setting applies to all service tokens in your Zero Trust account.

Access considers a service token inactive when all of the following are true:

  * The token has not successfully authenticated with an Access application during the configured inactivity period.
  * The token is older than the configured inactivity period.
  * The token is not directly referenced by an Access policy rule.



You can set the inactivity period to a whole number from 30 to 365 days. Disabled tokens remain in your account and can be turned on again. Deleted tokens cannot be recovered.

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Access controls** > **Access settings**.

[ Go to **Access settings** ↗ ](https://one.dash.cloudflare.com/?to=/:account/access-controls/settings)
  2. Under **Manage service tokens** , turn on **Automatically clean up inactive service tokens**.

  3. Enter an **Inactivity period** from 30 to 365 days.

  4. Choose whether Access should disable or delete inactive tokens.

  5. Select **Save**.




Send a `PATCH` request to update your Zero Trust organization. Set `action` to `disable` or `delete`:
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/%7Baccount_id%7D/access/organizations" \
    	--request PATCH \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"service_token_inactivity": {
    				"enabled": true,
    				"inactivity_threshold_days": 90,
    				"action": "disable"
    		}
    	}'

To stop automatic cleanup, set `enabled` to `false`.

Cleanup runs gradually in the background. An eligible token may not be disabled or deleted immediately.

## Turn a service token on or off

Turn off a service token to temporarily prevent it from authenticating. Access preserves the token so you can turn it on again later.

Turning off a token also stops its previous secret from working during an active rotation grace period.

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Access controls** > **Service credentials** > **Service Tokens**.

[ Go to ****↗](https://one.dash.cloudflare.com/?to=/:account/access/service-auth/service-tokens)
  2. Locate the token and select the three dots.

  3. To stop the token from authenticating, select **Disable token** > **Disable**.

  4. To restore authentication, select **Enable token** > **Enable**.




Make a `PUT` request to the [Update a service token](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/service_tokens/methods/update/) endpoint. Set `enabled` to `false` to turn off the token:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Access: Service Tokens Write`

Update a service tokenbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/access/service_tokens/$SERVICE_TOKEN_ID" \
    	--request PUT \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"name": "<TOKEN_NAME>",
    		"enabled": false
    	}'

To turn the token on again, set `enabled` to `true`.

## Revoke service tokens

If you need to revoke access before the token expires, delete the token. Services that rely on a deleted service token can no longer reach your application.

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Access controls** > **Service credentials** > **Service Tokens**.
  2. **Delete** the token you need to revoke.



Make a `DELETE` request to the [Delete a service token](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/service_tokens/methods/delete/) endpoint:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Access: Service Tokens Write`

Delete a service tokenbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/access/service_tokens/$SERVICE_TOKEN_ID" \
    	--request DELETE \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

To revoke the service token, remove the [`cloudflare_zero_trust_access_service_token` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zero_trust_access_service_token) resource from your configuration and run `terraform apply`, or target the resource for destruction:
    
    
    terraform destroy -target=cloudflare_zero_trust_access_service_token.example_service_token

Note

When editing an Access application, selecting **Revoke existing tokens** revokes existing sessions but does not prevent the user from starting a new session. As long as the Client ID and Client Secret are still valid, they can be exchanged for a new token on the next request. To revoke access, you must delete the service token.

## Set a token expiration alert

An alert can be configured to notify a week before a service token expires to allow an administrator to invoke a token refresh.

Expiring Access Service Token Alert

**Who is it for?**

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) customers who want to receive a notification when their service token is about to expire.

**Other options / filters**

None.

**Included with**

Purchase of Access

**What should you do if you receive one?**

Extend the expiration date of the service token. For more details, refer to [Renew your service token](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/#renew-service-tokens).

To configure a service token expiration alert:

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com), go to the **Notifications** page. [ Go to **Notifications** ↗ ](https://dash.cloudflare.com/?to=/:account/notifications)
  2. Select **Add**.
  3. Select _Expiring Access Service Token_.
  4. Enter a name for your alert and an optional description.
  5. (Optional) Add other recipients for the notification email.
  6. Select **Save**.



Your alert has been set and is now visible on the **Notifications** page.

[PreviousMutual TLS](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/)[NextApp Launcher](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/app-launcher/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/access-controls/service-credentials/service-tokens.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
