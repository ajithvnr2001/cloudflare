---
url: https://developers.cloudflare.com/learning-paths/replace-vpn/build-policies/session-timeouts/
title: Session timeouts \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:52.871689+00:00
---

# Session timeouts · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/replace-vpn/build-policies/session-timeouts/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Replace Vpn

  4. /[Build secure access policies](https://developers.cloudflare.com/learning-paths/replace-vpn/build-policies/)
  5. /Session timeouts



# Session timeouts

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/replace-vpn/build-policies/session-timeouts/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigure Cloudflare One Client session timeoutGlobal timeouts Common mistake

Most legacy VPNs have a global timeout setting that requires end users to log in every X hours or resets VPN profiles at a certain frequency. By doing continuous identity evaluation, a Zero Trust security model eliminates the need for most of the user-interrupting workflows triggered by session timeouts. However, there can still be valid reasons to want users to reauthenticate, either on a recurring basis or to access specific, highly-sensitive or regulated internal services.

To enforce Cloudflare One Client reauthentication, you can configure the Cloudflare One Client session timeouts on a per-application basis in your Gateway network policies. 

When a user goes to a protected application or website, Cloudflare checks their device client session duration against the configured session timeout. If the session has expired, the user will be prompted to re-authenticate with the identity provider (IdP) used to enroll in the Cloudflare One Client.

![Cloudflare One Client prompts user to re-authenticate session.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=404,height=504,format=webp/_astro/warp-reauthenticate-session.BjGtdKWz.png)

_Note: Labels in this image may reflect a previous product name._

A user's device client session duration resets to zero whenever they re-authenticate with the IdP, regardless of what triggered the authentication event.

## Configure Cloudflare One Client session timeout

You can enforce device client session timeouts on any Gateway Network and HTTP policy that has an Allow action. If you do not specify a session timeout, the device client session will be unlimited by default.

Session timeouts have no impact on Gateway DNS policies. DNS policies remain active even when a user needs to re-authenticate.

To configure a session timeout for a Gateway policy:

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Traffic policies** > **Firewall policies**. Choose either **Network** or **HTTP**.
  2. Add a policy and select the _Allow_ action. Alternatively, choose any existing _Allow_ policy.
  3. Under **Step 4 - Configure policy settings** , select **Edit** next to **Enforce Cloudflare One Client session duration**.
  4. Enter a session expiration time in `1h30m0s` format and save.
  5. Save the policy.



  1. Add the following permission to your [`cloudflare_api_token` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/api_token):

     * `Zero Trust Write`
  2. Choose a Network (`l4`) or HTTP (`http`) policy with an Allow action.

  3. In the policy's [`rule_settings` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zero_trust_gateway_policy), use the `check_session` argument to enable and configure a session timeout:
         
         resource "cloudflare_zero_trust_gateway_policy" "network_allow_wiki_IPs" {
         	name        = "Company Wiki Network policy"
         	enabled     = true
         	account_id  = var.cloudflare_account_id
         	description = "Managed by Terraform - Allow employees to access company wiki IPs."
         	precedence  = 103
         	action      = "allow"
         	filters     = ["l4"]
         	traffic     = "net.dst.ip in ${"$"}${cloudflare_zero_trust_list.wiki_IPs.id}"
         	identity    = "identity.email matches \".*@example.com\""
         
         	rule_settings = {
         		check_session = {
         			enforce = true
         			duration = "1h30m0s"
         		}
         	}
         }




Session checks are now enabled for the application protected by this policy. Users can continue to reach applications outside of the policy definition.

## Global timeouts

To set a global reauthentication event, similar to a global timeout on a traditional VPN, we recommend setting all of your Gateway Network Allow policies to the same baseline Cloudflare One Client session duration (typically between 3-7 days). This will ensure that whenever your user tries to access any application on the private network within that window, they will be forced to reauthenticate with your identity provider when they have not logged in for your chosen number of days.

If a specific application requires a more stringent reauthentication timeline, users accessing that application will not have to complete the baseline reauthentication event because they are already in compliance with the baseline policy.

Note

A global timeout does not necessarily fit all customer needs. With the increased interrogation of traffic offered by ZTNA compared to traditional remote access, many customers choose not to use a global reauthentication event and instead only use reauthentication for specific applications.

### Common mistake

When configuring a global Cloudflare One Client session duration, a common mistake is to build a single policy that covers your entire private network range. An example would be an Allow policy that requires reauthentication every 7 days for all users with traffic to a destination IP in `10.0.0.0/8`. This type of global policy may result in a suboptimal user experience because an expired session blocks the user from the entire internal network (including private DNS functionality) instead of specific applications. If a user misses the one-time reauth notification, they may not know that they need to manually go into their Cloudflare One Client settings to reauthenticate.

[PreviousTest your first application](https://developers.cloudflare.com/learning-paths/replace-vpn/build-policies/test-your-first-application/)[NextGateway block page](https://developers.cloudflare.com/learning-paths/replace-vpn/build-policies/block-page/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/replace-vpn/build-policies/session-timeouts.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
