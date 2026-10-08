---
url: https://developers.cloudflare.com/ssl/troubleshooting/mixed-content-errors/
title: Mixed content errors \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:56.414781+00:00
---

# Mixed content errors · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/troubleshooting/mixed-content-errors/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /[Troubleshooting](https://developers.cloudflare.com/ssl/troubleshooting/)
  4. /Mixed content errors



# Mixed content errors

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/troubleshooting/mixed-content-errors/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSymptoms of mixed content occurrence Browser indications Console logsResolution General advice WordPress usersRelated resources

Domains added to Cloudflare receive SSL certificates and can serve traffic over HTTPS. However, after starting to use Cloudflare, some customers notice missing content or page rendering issues when they first serve HTTPS traffic.

Typically, the problem is due to a request for HTTP resources from a web page served over HTTPS. For example, you type `https://example.com` in a browser and the page contains an image reference via HTTP in the HTML to `<img src="http://example.com/resource.jpg">`.

Normally, if your website loads all resources securely over HTTPS, visitors observe a lock icon in the address bar of their browser.

This indicates your site has a working SSL certificate and all resources loaded by the site are loaded over HTTPS. The green lock assures visitors that their connection is safe. One of the symptoms of mixed content is that different icons appear instead of the green lock icon.

* * *

## Symptoms of mixed content occurrence

Most modern browsers block HTTP requests on secure HTTPS pages. Blocked content can include images, JavaScript, CSS, or other content that affects how the page looks or behaves.

### Browser indications

Each web browser uses different methods to warn visitors about mixed content on a website, potentially including:

  * A yellow triangle or information symbol beside the URL bar
  * Messages mentioning "secure content"



### **Console logs**

For mixed content warnings, the web browser loads the resources but users do not see the lock icon in the URL. Warning messages appear within the browser’s debug tools:

![Screenshot of mixed content warnings displayed in a browser console.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1514,height=108,format=webp/_astro/hc-import-mixed_content_warning.WfgcvXqC.png)

For mixed content errors, the browser refuses to load the resources over an insecure connection:

![Screenshot of mixed content errors displayed in a browser console.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1500,height=94,format=webp/_astro/hc-import-mixed_content_error.C3G5mm9r.png)

Information on using the browser’s debug tools to locate these issues are found in the documentation for [Chrome ↗︎](https://developers.google.com/web/fundamentals/security/prevent-mixed-content/fixing-mixed-content) and [Firefox ↗︎](https://developer.mozilla.org/en-US/docs/Web/Security/Mixed_content). Alternatively, you can view your page source and find specific references of  _http://_ for paths to other resources.

* * *

## Resolution

### General advice

There are two methods to resolve mixed content errors.

  1. Load all resources via your HTML source without specifying the HTTP or HTTPS protocols. For example, using `/domain.com/path/to.file` instead of `http://domain.com/path/to.file`.
  2. Depending on your Content Management System, check for plugins that automatically rewrite HTTP resources to HTTPS. Cloudflare provides such a service via [Automatic HTTPS Rewrites](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/automatic-https-rewrites).



### WordPress users

Cloudflare recommends WordPress users to install the [Cloudflare WordPress plugin ↗︎](https://wordpress.org/plugins/cloudflare/) and enable the _Automatic HTTPS rewrites_ option within the plugin.

* * *

## Related resources

  * [Debugging mixed content in Chrome ↗︎](https://developers.google.com/web/fundamentals/security/prevent-mixed-content/fixing-mixed-content)
  * [Debugging mixed content in Firefox ↗︎](https://developer.mozilla.org/en-US/docs/Web/Security/Mixed_content)
  * [Community Tip - Fixing mixed content errors ↗︎](https://community.cloudflare.com/t/community-tip-fixing-mixed-content-errors/42476)



[PreviousERR_TOO_MANY_REDIRECTS](https://developers.cloudflare.com/ssl/troubleshooting/too-many-redirects/)[NextFAQ](https://developers.cloudflare.com/ssl/faq/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/troubleshooting/mixed-content-errors.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
