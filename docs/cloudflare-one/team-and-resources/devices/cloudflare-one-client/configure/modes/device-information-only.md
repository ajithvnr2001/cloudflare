---
url: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/device-information-only/
title: Enable Posture only mode \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:55.363169+00:00
---

# Enable Posture only mode · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/device-information-only/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Team and resources[Devices](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/)[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)[Configure](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/)

  4. /[Client modes](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/)
  5. /Enable Posture only mode



# Enable Posture only mode

Last updated May 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/device-information-only/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview1\. Turn on account settings2\. Configure the Cloudflare One Client3\. (Optional) Verify the client certificate4\. Enforce the client certificateLimitations

Feature availability

System | Availability  
---|---  
Windows | ✅  
macOS | ✅  
Linux | ✅  
iOS | ✅  
Android | ✅  
ChromeOS | ✅  
  
Posture only mode allows you to enforce device posture rules when a user connects to your [self-hosted Access application](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/). This mode relies on a client certificate generated from your account to establish trust between the Access application and the device.

## 1\. Turn on account settings

Using the API, enable client certificate provisioning for [your zone](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/):

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `SSL and Certificates Write`

Update device certificate provisioning statusbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/devices/policy/certificates" \
    	--request PATCH \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"enabled": true
    	}'

## 2\. Configure the Cloudflare One Client

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Team & Resources** > **Devices** > **Device profiles** > **General profiles**.

  2. Choose a [device profile](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/) and select **Edit**.

  3. For **Service mode** , select **Posture only mode**.

  4. Select **Save profile**.

  5. [Enroll your device](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/) into your Zero Trust organization.

When enrolled in Posture only mode, the Cloudflare One Client (formerly WARP) will automatically generate a client certificate and install the certificate on the device. This certificate is necessary to confirm the source of outgoing traffic.




## 3\. (Optional) Verify the client certificate

  1. To view the client certificates installed on the device:

     1. Open the **Start** menu and select **Run**.
     2. Enter `certlm.msc`.
     3. Go to **Personal** > **Certificates**.

     1. Open **Keychain Access**.
     2. Go to **System** > **My Certificates**.

Open a terminal window and run the following command:
    
    $ certutil -L -d sql:/etc/pki/nssdb

Go to **Settings** > **General** > **About** > **Certificate Trust Settings**.

The location of the client certificate may vary depending on the Android device.

     * **Samsung** : Go to **Settings** > **Security** > **Other security settings** > **View security certificates**.
     * **Google Pixel** : Go to **Security** > **Advanced settings** > **Encryption & credentials** > **Credential storage**.

Go to **Settings** > **Apps** > **Google Play Store** > **Manage Android Preferences** > **Security** > **Credentials**.

The client certificate name should match the **Device ID** in your Cloudflare One Client **Preferences**.

  2. To verify the client certificate in your Cloudflare account:

     1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), select the zone for which you enabled client certificates.
     2. Go to **SSL/TLS** > **Client Certificates**.

The certificate name is the WARP enrollment **Device ID**. ![Example client certificate in the Cloudflare dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2066,height=486,format=webp/_astro/device-information-only-cert.CBHcWmIc.png)




## 4\. Enforce the client certificate

To block traffic from devices that do not have a valid client certificate:

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **SSL/TLS** > **Client Certificates**.
  2. Under **Hosts** , select **Edit** and enter the hostname of your Access application (for example, `app.mycompany.com`). This enables mTLS authentication for the application.
  3. Select **Create mTLS rule**.
  4. Create a WAF custom rule that checks all requests to your application for a valid client certificate: 

Field | Operator | Value | Logic | Action  
---|---|---|---|---  
Client Certificate | equals | Off | And | Block  
Hostname | equals | `app.mycompany.com` |  |   
  
  5. Select **Deploy**.



Posture only mode is now enabled on the device. To start enforcing device posture, set up a [WARP client check](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/) and add a _Require_ device posture rule to your [Access policy](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/). When the device connects to the Access application for the first time, the browser will ask to use the client certificate installed by the Cloudflare One Client.

![Browser prompts for client
certificate](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1096,height=610,format=webp/_astro/device-information-only-browser.BARL_mBj.png)

## Limitations

Posture only mode is not compatible with the [Windows pre-login](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/windows-prelogin/) feature. The user must be logged into Windows because the Cloudflare One Client needs to install a certificate in the user store.

[PreviousOverview](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/)[NextOverview](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/device-information-only.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
