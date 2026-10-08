---
url: https://developers.cloudflare.com/pages/how-to/deploy-a-wordpress-site/
title: Deploy a static WordPress site \u00b7 Cloudflare Pages docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:35.206235+00:00
---

# Deploy a static WordPress site · Cloudflare Pages docs

> Source: https://developers.cloudflare.com/pages/how-to/deploy-a-wordpress-site/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Pages](https://developers.cloudflare.com/pages/)
  3. /How to
  4. /Deploy a static WordPress site



# Deploy a static WordPress site

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/pages/how-to/deploy-a-wordpress-site/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewOverviewPrerequisitesSetup Export your WordPress site Deploy your WordPress site with PagesLimitationsConclusion

## Overview

In this guide, you will use a WordPress plugin, [Simply Static ↗︎](https://wordpress.org/plugins/simply-static/), to convert your existing WordPress site to a static website deployed with Cloudflare Pages.

## Prerequisites

This guide assumes that you are:

  * The Administrator account on your WordPress site.
  * Able to install WordPress plugins on the site.



## Setup

To start, install the [Simply Static ↗︎](https://wordpress.org/plugins/simply-static/) plugin to export your WordPress site. In your WordPress dashboard, go to **Plugins** > **Add New**.

Search for `Simply Static` and confirm that the resulting plugin that you will be installing matches the plugin below.

![Simply Static plugin](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=762,height=526,format=webp/_astro/simply-static.B1STKlmC.png)

Select **Install** on the plugin. After it has finished installing, select **Activate**.

### Export your WordPress site

After you have installed the plugin, go to your WordPress dashboard > **Simply Static** > **GENERATE STATIC FILES**.

In the **Activity Log** , find the **ZIP archive created** message and select **Click here to download** to download your ZIP file.

### Deploy your WordPress site with Pages

With your ZIP file downloaded, deploy your site to Pages:

  1. In the Cloudflare dashboard, go to the **Workers & Pages** page.

[ Go to **Workers & Pages** ↗ ](https://dash.cloudflare.com/?to=/:account/workers-and-pages)
  2. Select **Create application** > **Pages** > **Use direct upload**.

  3. Name your project, then select **Create project**.

  4. Drag and drop your ZIP file (or unzipped folder of assets) or select it from your computer.

  5. After your files have been uploaded, select **Deploy site**.




Your WordPress site will now be live on Pages.

Every time you make a change to your WordPress site, you will need to download a new ZIP file from the WordPress dashboard and redeploy to Cloudflare Pages. Automatic updates are not available with the free version of Simply Static.

## Limitations

There are some features available in WordPress sites that will not be supported in a static site environment:

  * WordPress Forms.
  * WordPress Comments.
  * Any links to `/wp-admin` or similar internal WordPress routes.



## Conclusion

By following this guide, you have successfully deployed a static version of your WordPress site to Cloudflare Pages.

With a static version of your site being served, you can:

  * Move your WordPress site to a custom domain or subdomain. Refer to [Custom domains](https://developers.cloudflare.com/pages/configuration/custom-domains/) to learn more.
  * Run your WordPress instance locally, or put your WordPress site behind [Cloudflare Access](https://developers.cloudflare.com/pages/configuration/preview-deployments/#customize-preview-deployments-access) to only give access to your contributors. This has a significant effect on the number of attack vectors for your WordPress site and its content.
  * Downgrade your WordPress hosting plan to a cheaper plan. Because the memory and bandwidth requirements for your WordPress instance are now smaller, you can often host it on a cheaper plan, or moving to shared hosting.



Connect with the [Cloudflare Developer community on Discord ↗︎](https://discord.cloudflare.com) to ask questions and discuss the platform with other developers.

[PreviousAdd custom HTTP headers](https://developers.cloudflare.com/pages/how-to/add-custom-http-headers/)[NextEnable Web Analytics](https://developers.cloudflare.com/pages/how-to/web-analytics/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/pages/how-to/deploy-a-wordpress-site.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
