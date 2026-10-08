---
url: https://developers.cloudflare.com/zaraz/web-api/debug-mode/
title: Debug mode \u00b7 Cloudflare Zaraz docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:18:20.520113+00:00
---

# Debug mode · Cloudflare Zaraz docs

> Source: https://developers.cloudflare.com/zaraz/web-api/debug-mode/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Zaraz](https://developers.cloudflare.com/zaraz/)
  3. /[Web API](https://developers.cloudflare.com/zaraz/web-api/)
  4. /Debug mode



# Debug mode

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/zaraz/web-api/debug-mode/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Zaraz offers a debug mode to troubleshoot the events and triggers systems. To activate debug mode you need to create a special debug cookie (`zarazDebug`) containing your debug key. You can set this cookie manually or via the `zaraz.debug` helper function available in your console.

  1. In the Cloudflare dashboard, go to the **Settings** page.

[ Go to **Settings** ↗ ](https://dash.cloudflare.com/?to=/:account/tag-management/settings)
  2. Copy your **Debug Key**.

  3. Open a web browser and access its Developer Tools. For example, to access Developer Tools in Google Chrome, select **View** > **Developer** > **Developer Tools**.

  4. Select the **Console** pane and enter the following command to create a debug cookie:
         
         zaraz.debug("YOUR_DEBUG_KEY")




Zaraz’s debug mode is now enabled. A pop-up window will show up with the debugger information. To exit debug mode, remove the cookie by typing `zaraz.debug()` in the console pane of the browser.

[PreviousE-commerce](https://developers.cloudflare.com/zaraz/web-api/ecommerce/)[NextHTTP Events API](https://developers.cloudflare.com/zaraz/http-events-api/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/zaraz/web-api/debug-mode.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
