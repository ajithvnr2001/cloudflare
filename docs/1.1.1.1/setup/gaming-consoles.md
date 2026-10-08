---
url: https://developers.cloudflare.com/1.1.1.1/setup/gaming-consoles/
title: Set up 1.1.1.1 on gaming consoles \u00b7 Cloudflare 1.1.1.1 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:04.440737+00:00
---

# Set up 1.1.1.1 on gaming consoles · Cloudflare 1.1.1.1 docs

> Source: https://developers.cloudflare.com/1.1.1.1/setup/gaming-consoles/

  1. [Home](https://developers.cloudflare.com/)
  2. /[1.1.1.1 (DNS Resolver)](https://developers.cloudflare.com/1.1.1.1/)
  3. /[Set up](https://developers.cloudflare.com/1.1.1.1/setup/)
  4. /Gaming consoles



# Gaming consoles

Last updated May 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/1.1.1.1/setup/gaming-consoles/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPS4Xbox OneNintendoNintendo Switch

The steps below configure your gaming console to use 1.1.1.1 instead of the default DNS resolver provided by your ISP.

## PS4

  1. Go to **Settings** > **Network** > **Set Up Internet Connection**.
  2. Select **Wi-Fi** or **LAN** depending on your Internet connection.
  3. Select **Custom**.
  4. Set **IP Address Settings** to **Automatic**.
  5. Change **DHCP Host Name** to **Do Not Specify**.
  6. Set **DNS Settings** to **Manual**.
  7. Change **Primary DNS** and **Secondary DNS** to: 
         
         1.1.1.1
         1.0.0.1

  8. If you are able to add more DNS servers, you can add the IPv6 addresses as well: 
         
         2606:4700:4700::1111
         2606:4700:4700::1001

  9. Set **MTU Settings** to **Automatic**.
  10. Set **Proxy Server** to **Do Not Use**.



## Xbox One

  1. Open the Network screen by pressing the Xbox button on your controller.
  2. Go to **Settings** > **Network** > **Network Settings**.
  3. Go to **Advanced Settings** > **DNS Settings**.
  4. Select **Manual**.
  5. Set **Primary DNS** and **Secondary DNS** to: 
         
         1.1.1.1
         1.0.0.1

  6. If you have the option to add more DNS servers, you can add the IPv6 addresses as well: 
         
         2606:4700:4700::1111
         2606:4700:4700::1001

  7. When you are done, you will be shown a confirmation screen. Press **B** to save.



## Nintendo

The following instructions work on New Nintendo 3DS, New Nintendo 3DS XL, New Nintendo 2DS XL, Nintendo 3DS, Nintendo 3DS XL, and Nintendo 2DS.

  1. Go to the home menu and choose **System Settings** (the wrench icon).
  2. Select **Internet Settings** > **Connection Settings**.
  3. Select your Internet connection and then select **Change Settings**.
  4. Select **Change DNS**.
  5. Set **Auto-Obtain DNS** to **No**.
  6. Select **Detailed Setup**.
  7. Set **Primary DNS** and **Secondary DNS** to: 
         
         1.1.1.1
         1.0.0.1

  8. If you are able to add more DNS servers, you can add the IPv6 addresses as well: 
         
         2606:4700:4700::1111
         2606:4700:4700::1001

  9. Select **Save** > **OK**.



## Nintendo Switch

  1. Press the home button and select **System Settings**.
  2. Scroll down and select **Internet** > **Internet Settings**.
  3. Select your Internet connection and then select **Change Settings**.
  4. Select **DNS Settings** > **Manual**.
  5. Set **Primary DNS** and **Secondary DNS** to: 
         
         1.1.1.1
         1.0.0.1

  6. Select **Save** > **OK**.



[PreviousAzure](https://developers.cloudflare.com/1.1.1.1/setup/azure/)[NextGoogle Cloud](https://developers.cloudflare.com/1.1.1.1/setup/google-cloud/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/1.1.1.1/setup/gaming-consoles.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
