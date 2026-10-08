---
url: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/
title: Device profiles \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:55.648036+00:00
---

# Device profiles · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Team and resources[Devices](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/)[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

  4. /[Configure](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/)
  5. /Device profiles



# Device profiles

Last updated May 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate a new profileEdit profile settingsVerify device profile Via the dashboard Via the CLISelectors User email User group emails User group IDs User group names Operating system Operating system version Managed network SAML attributes Service tokenComparison operatorsLogical operatorsOrder of precedence

A device profile defines [Cloudflare One Client settings](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/) for a specific set of devices in your organization. You can create multiple profiles and apply different settings based on the user's identity, the device's location, and other criteria.

For example, users in one identity provider group (signifying a specific office location) might have different routes that need to be excluded from their WARP tunnel, or some device types (like Linux) might need different DNS settings to accommodate local development services.

## Create a new profile

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Team & Resources** > **Devices** > **Device profiles** > **General profiles**.
  2. Select **Create new profile**. This will make a copy of the **Default** profile.
  3. Enter any name for the profile.
  4. Create rules to define the devices that will use this profile. Learn more about the available Selectors, [Operators](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/#comparison-operators), and [Values](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/#value).
  5. Configure [device client settings](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#device-settings) for these devices.



Note

At this time, **Split Tunnels** and **Local Domain Fallback** can only be modified after you save the profile.

  6. Select **Create profile**.



Your profile will appear in the **Profile settings** list. You can rearrange the profiles in the list according to your desired order of precedence.

Send a `POST` request to the [Devices API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/policies/subresources/custom/methods/create/):

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Zero Trust Write`

Create a device settings profilebash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/devices/policy" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"allow_mode_switch": false,
    		"allow_updates": false,
    		"allowed_to_leave": false,
    		"auto_connect": 600,
    		"captive_portal": 180,
    		"description": "Example device profile recommended in the implementation documentation. For details, refer to https://developers.cloudflare.com/learning-paths/replace-vpn/configure-device-agent/device-profiles/",
    		"disable_auto_fallback": true,
    		"enabled": true,
    		"exclude_office_ips": false,
    		"match": "identity.email in {\"jdoe@example.com\"} or any(identity.groups.name[*] in {\"developers\" \"admin\"}) and os.name == \"windows\"",
    		"name": "Example device profile",
    		"precedence": 101,
    		"service_mode_v2": {
    				"mode": "warp"
    		},
    		"support_url": "https://support.example.com",
    		"switch_locked": true
    	}'

  1. Add the following permission to your [`cloudflare_api_token` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/api_token):

     * `Zero Trust Write`
  2. Create a new profile using the [`cloudflare_zero_trust_device_custom_profile` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zero_trust_device_custom_profile) resource:
         
         resource "cloudflare_zero_trust_device_custom_profile" "example" {
         	account_id            = var.cloudflare_account_id
         	name                  = "Example device profile"
         	description           = "Example device profile recommended in the implementation documentation. For details, refer to https://developers.cloudflare.com/learning-paths/replace-vpn/configure-device-agent/device-profiles/"
         	allow_mode_switch     = false
         	allow_updates         = false
         	allowed_to_leave      = false
         	auto_connect          = 600
         	captive_portal        = 180
         	disable_auto_fallback = true
         	enabled               = true
         	exclude_office_ips    = false
         	precedence            = 101
         	service_mode_v2       = {mode = "warp"}
         	support_url           = "https://support.example.com"
         	switch_locked         = true
         	tunnel_protocol       = "wireguard"
         
         	match = trimspace(replace(<<-EOT
         		identity.email in {"jdoe@example.com"}
         		or any(identity.groups.name[*] in {"developers" "admin"})
         		and os.name == "windows"
         	EOT
         	, "\n", " "))
         }




## Edit profile settings

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Team & Resources** > **Devices** > **Device profiles** > **General profiles**.

  2. Locate the [device profile](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/) you would like to update and select **Configure**.

  3. Use [selectors](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/#selectors) to add or adjust match rules, and modify [device client settings](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#device-settings) for this profile as needed.

Note

Changing any of the settings below will cause the client connection to restart. The user may experience a brief period of connectivity loss while the new settings are being applied.

     * [Service mode](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#service-mode)
     * [Local Domain Fallback](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#local-domain-fallback)
     * [Split Tunnels](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#split-tunnels)

  4. Select **Save profile**.




It may take up to 10 minutes for newly updated settings to propagate to devices.

## Verify device profile

### Via the dashboard

To verify the last active device profile for a specific device:

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Team & Resources** > **Devices**.
  2. Under devices, find your device.
  3. Review the device profile under **Last active device profile**.



To verify the last active device profile for a user's devices:

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Team & Resources** > **Users**.
  2. Under **User name** , find the user you would like to investigate.
  3. Select **Devices** to see all devices used by the user.
  4. Find the device you want to investigate and verify the last active device profile for that device under the **Device profile** column.



Alternatively, you can use [DEX remote captures](https://developers.cloudflare.com/cloudflare-one/insights/dex/diagnostics/client-packet-capture/) to collect client diagnostic logs. The device profile UUID is shown in your [detection report](https://developers.cloudflare.com/cloudflare-one/insights/dex/diagnostics/client-packet-capture/#diagnostics-analyzer-beta) under `Profile ID`.

### Via the CLI

To check which device profile and profile settings are currently on a device, open a terminal and run:
    
    
    warp-cli settings

The device profile UUID is shown in the `Profile ID` field.

## Selectors

You can configure device profiles to match against the following selectors, or criteria. Identity-based selectors are only available if the user [enrolled the device](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/) by logging in to an identity provider (IdP).

### User email

Apply a device profile based on the user's email.

UI name | API example value  
---|---  
User email | `identity.email == "user-name@company.com"`  
  
### User group emails

Apply a device profile based on an [IdP group](https://developers.cloudflare.com/cloudflare-one/traffic-policies/identity-selectors/#idp-groups-in-gateway) email address of which the user is configured as a member in the IdP.

UI name | API example  
---|---  
User group emails | `identity.groups.email == "contractors@company.com"`  
  
### User group IDs

Apply a device profile based on an [IdP group](https://developers.cloudflare.com/cloudflare-one/traffic-policies/identity-selectors/#idp-groups-in-gateway) ID of which the user is configured as a member in the IdP.

UI name | API example  
---|---  
User group IDs | `identity.groups.id == "12jf495bhjd7893ml09o"`  
  
### User group names

Apply a device profile based on an [IdP group](https://developers.cloudflare.com/cloudflare-one/traffic-policies/identity-selectors/#idp-groups-in-gateway) name of which the user is configured as a member in the IdP.

UI name | API example  
---|---  
User group names | `identity.groups.name == "\"finance\""`  
  
### Operating system

Apply a device profile based on the operating system of the device.

UI name | API example  
---|---  
Operating system | `os.name in {\"windows\" \"mac\"}`  
  
### Operating system version

Apply a device profile based on the [OS version](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/os-version/#determine-the-os-version) of the device.

UI name | API example  
---|---  
Operating system version | `os.version == \"1.2.0\"`  
  
Note

The OS version must be specified as a valid [Semver ↗︎](https://semver.org/). For example, if your device is running OS version `1.2`, you must enter `1.2.0`.

### Managed network

Apply a device profile based on the [managed network](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/managed-networks/) that the device is connected to.

UI name | API example  
---|---  
Managed network | `network == \"Austin office\"`  
  
### SAML attributes

Apply a device profile based on an attribute name and value from a [SAML IdP](https://developers.cloudflare.com/cloudflare-one/traffic-policies/identity-selectors/#generic-saml-idp).

UI name | API example  
---|---  
SAML Attributes | `identity.saml_attributes == "\"group=finance\""`  
  
### Service token

Apply a device profile based on the [service token](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/device-enrollment/#check-for-service-token) used to enroll the device.

UI name | API example  
---|---  
Service Token | `identity.service_token_uuid == \"f174e90a-fafe-4643-bbbc-4a0ed4fc8415\"`  
  
## Comparison operators

Comparison operators determine how device profiles match a selector.

Operator | Meaning  
---|---  
is | equals the defined value  
in | matches at least one of the defined values  
  
## Logical operators

To evaluate multiple conditions in an expression, select a logical operator:

Operator | Meaning  
---|---  
And | match all of the conditions in the expression  
Or | match any of the conditions in the expression  
  
## Order of precedence

The Cloudflare One Client evaluates device profiles dynamically based on a hierarchy. When a device connects, the client checks the profiles from top to bottom as they appear in the dashboard. The client follows the first match principle — once a device matches a profile, the client stops evaluating and no subsequent profiles can override the decision.

The **Default** profile is always at the bottom of the list. It will only be applied if the device does not meet the criteria of any profile listed above it. If you make another custom profile the default, all settings will be copied over into the **Default** profile.

Administrators can create multiple profiles to apply different settings based on specific criteria such as user identity, location, or operating system. Understanding this top-to-bottom evaluation order is crucial for ensuring that the correct policies are applied to devices.

[PreviousEmergency Disconnect](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/emergency-disconnect/)[NextManaged networks](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/managed-networks/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
