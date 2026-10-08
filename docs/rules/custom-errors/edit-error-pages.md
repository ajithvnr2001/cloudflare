---
url: https://developers.cloudflare.com/rules/custom-errors/edit-error-pages/
title: Edit Error Pages \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:48.496137+00:00
---

# Edit Error Pages · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/custom-errors/edit-error-pages/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /[Custom Errors](https://developers.cloudflare.com/rules/custom-errors/)
  4. /Edit Error Pages



# Edit Error Pages

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/custom-errors/edit-error-pages/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview1\. Design your custom error page2\. Update an error page in the dashboardFetch custom error page again

You can define custom [Error Pages](https://developers.cloudflare.com/rules/custom-errors/#error-pages) for the following errors and challenges:

  * WAF block
  * IP/Country block
  * IP/Country challenge
  * 500 class errors
  * 1000 class errors
  * Managed challenge / I'm Under Attack Mode
  * Rate limiting block



For more information on the different types of Error Pages, refer to [Error page types](https://developers.cloudflare.com/rules/custom-errors/reference/error-page-types/).

To return custom error responses for requests that match specific conditions, use [Custom Error Rules](https://developers.cloudflare.com/rules/custom-errors/#custom-error-rules) instead.

## 1\. Design your custom error page

Before defining a custom error page in your Cloudflare account, you will need to design and code that page. It can be hosted on your own web server or using a Cloudflare product like [Snippets](https://developers.cloudflare.com/rules/snippets/).

When designing your custom error page, you can include page-specific [custom error tokens](https://developers.cloudflare.com/rules/custom-errors/reference/error-tokens/). Each custom error token provides diagnostic information that appears on the error page.

To display a custom page for each error, create a separate page per error. For example, to create a custom error page for both **IP/Country Block** and **WAF block** , you must design and publish two separate pages.

Notes

  * Your custom error page should include a page-specific custom error token if applicable and cannot exceed 1.5 MB (1,500,000 bytes). Also, it must include HTML `<head>` and `</head>` tags.
  * Make sure that the `referrer` meta tag is not present in your custom error page's HTML code since it will disrupt [Cloudflare challenges](https://developers.cloudflare.com/cloudflare-challenges/): `<meta name="referrer" (...) />`



You can use the following template to start building your error page:
    
    
    <html>
    	<head></head>
    	<body>
    		::[REPLACE WITH CUSTOM ERROR TOKEN NAME]::
    	</body>
    </html>

Example error page for 5XX errors

The following HTML code is an example error page for 5XX errors without styling:
    
    
    <!doctype html>
    <html>
    	<head>
    		<meta charset="utf-8" />
    		<title>5XX Level Errors page</title>
    	</head>
    	<body>
    		<h1>5XX Level Errors</h1>
    		<h2>::CLOUDFLARE_ERROR_500S_BOX::</h2>
    	</body>
    </html>

* * *

## 2\. Update an error page in the dashboard

You can define an error page at the zone level or for your entire account. Zone-level error pages have priority over account-level error pages.

To edit a zone-level custom error page:

  1. In the Cloudflare dashboard, go to the **Error Pages** page.

[ Go to **Error Pages** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/error-pages)
  2. Identify your desired custom error page type.

  3. (Optional) To preview the current error page (default or custom), select the link in the **Show** column.

  4. To edit the error page, select the three dots > **Edit** next to the page type you previously identified.

  5. To use Cloudflare's default page, select **Cloudflare default page.** To provide a custom error page, select **Custom page** and enter the URL of the custom error page you created.

  6. Select **Confirm**.




To update an account-level custom error page:

  1. In the Cloudflare dashboard, go to the **Settings** page.

[ Go to **Configurations** ↗ ](https://dash.cloudflare.com/?to=/:account/configurations)
  2. Go to **Error Pages** and identify your desired custom error page type.

  3. (Optional) To preview the current error page (default or custom), select the link in the **Show** column.

  4. To edit the error page, select the three dots > **Edit** next to the page type you previously identified.

  5. To use Cloudflare's default page, select **Cloudflare default page.** To provide a custom error page, select **Custom page** and enter the URL of the custom error page you created.

  6. Select **Confirm**.




## Fetch custom error page again

After successfully setting the content of the custom error page in **Error Pages** , you can remove the page from your origin server.

If in the future, you need to update your custom error page, you must fetch the page again, even if the page URL remains unchanged. In this case, next to the page type you want to update, select the three dots > **Fetch custom page again**.

[PreviousOverview](https://developers.cloudflare.com/rules/custom-errors/)[NextCreate custom error rules](https://developers.cloudflare.com/rules/custom-errors/create-rules/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/custom-errors/edit-error-pages.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
