---
url: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/connect-devices-networks/mdm/
title: MDM deployment \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:57.377315+00:00
---

# MDM deployment · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/connect-devices-networks/mdm/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Secure Internet Traffic

  4. /[Connect devices and networks to Cloudflare](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/connect-devices-networks/)
  5. /MDM deployment



# MDM deployment

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/connect-devices-networks/mdm/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMDM policy file

Organizations can deploy and manage the Cloudflare One Client (formerly WARP) across their fleet of devices in two complementary ways:

  * **Through a mobility management solution (MDM)** — Push the client installer and its deployment parameters using a tool such as [Intune, JAMF, Kandji, or JumpCloud](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/partners/), or by executing an `.msi` file on desktop machines. This page covers the MDM-driven workflow.
  * **From the Cloudflare dashboard** — Manage client versions for groups of devices directly from the Zero Trust dashboard, without relying on a third-party MDM solution. For more information, refer to [Client version assignments](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/client-version-assignments/).



## MDM policy file

Refer to our [managed deployment instructions](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/) and create a `.plist`, `mdm.xml`, or `.msi` policy file based on your organization's software management tool.

[MDM parameters](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/) that you specify in a local policy file will overrule any [device client settings](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/) configured in the dashboard.

Therefore, we recommend that your policy file only contain the organization name and potentially the onboarding flag, [relying on the dashboard](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/configure-device-agent/device-profiles/) to configure the remaining device settings. 
    
    
    <dict>
      <key>organization</key>
      <string>your-team-name</string>
      <key>onboarding</key>
      <false/>
    </dict>

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), select **Zero Trust**.

  2. On the onboarding screen, choose a team name. The team name is a unique, internal identifier for your Zero Trust organization. Users will enter this team name when they enroll their device manually, and it will be the subdomain for your App Launcher (as relevant). Your business name is the typical entry.

You can find your team name in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/) by going to **Zero Trust** > **Settings**.

  3. Complete your onboarding by selecting a subscription plan and entering your payment details. If you chose the **Zero Trust Free plan** , this step is still needed but you will not be charged.




When you create your organization, Cloudflare automatically adds the [Cloudflare identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/cloudflare/) as your default login method, so your users can sign in with their Cloudflare account credentials right away. You can add a [one-time PIN](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/one-time-pin/) or connect a [third-party identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/) at any time.

[PreviousDownload and install the Cloudflare One Client](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/connect-devices-networks/install-agent/)[NextVerify device connectivity](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/connect-devices-networks/validate-traffic-in-gateway/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/secure-internet-traffic/connect-devices-networks/mdm.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
