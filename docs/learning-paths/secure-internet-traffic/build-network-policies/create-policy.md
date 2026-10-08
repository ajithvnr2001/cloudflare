---
url: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-network-policies/create-policy/
title: Create your first network policy \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:56.578507+00:00
---

# Create your first network policy · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-network-policies/create-policy/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Secure Internet Traffic

  4. /[Build network security policies](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-network-policies/)
  5. /Create your first network policy



# Create your first network policy

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-network-policies/create-policy/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can control network-level traffic by filtering requests by selectors such as IP addresses and ports. You can also integrate network policies with an [identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/) to apply identity-based filtering.

To create a new network policy:

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Traffic policies** > **Firewall policies**.

  2. In the **Network** tab, select **Add a network policy**.

  3. Name the policy.

  4. Under **Traffic** , build a logical expression that defines the traffic you want to allow or block.

  5. Choose an **Action** to take when traffic matches the logical expression. For example, you can use a list of [device serial numbers](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/corp-device/) to ensure users can only access an application if they connect with the Cloudflare One Client from a company device:

Selector | Operator | Value | Logic | Action  
---|---|---|---|---  
SNI Domain | is | `internalapp.com` | And | Block  
Passed Device Posture Checks | not in | _Device serial numbers_ |  |   
  
  6. Select **Create policy**.




  1. [Create an API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) with the following permissions:

Type | Item | Permission  
---|---|---  
Account | Zero Trust | Edit  
  
  2. (Optional) Configure your API environment variables to include your [account ID](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/) and API token.

  3. Send a `POST` request to the [Create a Zero Trust Gateway rule](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/rules/methods/create/) endpoint. For example, you can use a list of [device serial numbers](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/corp-device/) to ensure users can only access an application if they connect with the Cloudflare One Client from a company device:

Create a Zero Trust Gateway rulebash
         
         curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/gateway/rules" \
         	--request POST \
         	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
         	--json '{
         		"name": "Enforce device posture",
         		"description": "Ensure only devices in Zero Trust organization can connect to application",
         		"precedence": 0,
         		"enabled": true,
         		"action": "block",
         		"filters": [
         				"l4"
         		],
         		"traffic": "any(net.sni.domains[*] == \"internalapp.com\")",
         		"identity": "",
         		"device_posture": "not(any(device_posture.checks.passed[*] in {\"LIST_UUID\"}))"
         	}'



    
    
    {
    	 "success": true,
    	 "errors": [],
    	 "messages": []
    }

The API will respond with a summary of the policy and the result of your request.

For more information, refer to [network policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/).

[PreviousOverview](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-network-policies/)[NextRecommended network policies](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-network-policies/recommended-network-policies/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/secure-internet-traffic/build-network-policies/create-policy.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
