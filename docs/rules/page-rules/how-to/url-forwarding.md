---
url: https://developers.cloudflare.com/rules/page-rules/how-to/url-forwarding/
title: URL forwarding with Page Rules \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:50.674592+00:00
---

# URL forwarding with Page Rules · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/page-rules/how-to/url-forwarding/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Page Rules](https://developers.cloudflare.com/rules/page-rules/)

  4. /How to
  5. /URL forwarding



# URL forwarding with Page Rules

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/page-rules/how-to/url-forwarding/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRedirect with Page RulesForwarding examplesAdvanced forwarding options

Page Rules allow you to forward or redirect traffic to a different URL, though they are just one of the [options provided by Cloudflare](https://developers.cloudflare.com/fundamentals/reference/redirects/).

Note

Consider alternative [Rules](https://developers.cloudflare.com/rules/) options due to their enhanced configurability. Refer to the [migration guide](https://developers.cloudflare.com/rules/reference/page-rules-migration/) for details.

For more flexibility and customization, consider using [Snippets](https://developers.cloudflare.com/rules/snippets/).

* * *

## Redirect with Page Rules

To configure URL forwarding or redirects using Page Rules:

  1. In the Cloudflare dashboard, go to the **Page Rules** page.

[ Go to **Page Rules** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/rules/page-rules)
  2. Select **Create Page Rule**.

  3. Under **If the URL matches** , enter the URL or URL pattern that should match the rule.

  4. In **Pick a Setting** , choose **Forwarding URL** from the drop-down menu.

  5. For **Select status code** , choose _301 - Permanent Redirect_ or _302 - Temporary Redirect_.

  6. Enter the destination URL.

  7. Select **Save and Deploy Page Rule**.




Note

Page Rules require a [proxied DNS record](https://developers.cloudflare.com/dns/proxy-status/) to work. Page Rules will not apply to subdomains that do not exist in DNS or are not being directed to Cloudflare.

* * *

## Forwarding examples

Imagine you want site visitors to reach your website for a variety of URL patterns. For instance, the page rule URL patterns `*www.example.com/products` and `*example.com/products` match:
    
    
    http://example.com/products
    
    http://www.example.com/products
    
    https://www.example.com/products
    
    https://blog.example.com/products
    
    https://www.blog.example.com/products

but do not match:
    
    
    http://www.example.com/blog/products (extra directory)
    or
    http://www.example.comproducts (no trailing slash)

Once you have created the pattern that matches what you want, select the **Forwarding** toggle. This will display a field where you can enter the address you want requests forwarded to.
    
    
    https://example.com/products

If you enter the address above in the forwarding box and select **Add Rule** , within a few seconds any requests that match the pattern you entered will automatically be forwarded with an `HTTP 302` redirect status code to the new URL.

* * *

## Advanced forwarding options

If you use a basic redirect, such as forwarding the apex domain (`example.com`) to `www.example.com`, then you lose anything else in the URL.

For example, you could set up the pattern:
    
    
    example.com

And have it forward to:
    
    
    http://www.example.com

However, if someone entered `example.com/some-particular-page.html`, they would be redirected to:
    
    
    www.example.com

Instead of:
    
    
    www.example.com/some-particular-page.html

The solution is to use variables. Each wildcard corresponds to a variable when can be referenced in the forwarding address. The variables are represented by a `$` (dollar sign) followed by a number. To refer to the first wildcard you would use `$1`, to refer to the second wildcard you would use `$2`, and so on.

To fix the forwarding from the apex to `www` in the above example, you could use the same pattern:
    
    
    example.com/*

You would then set up the following URL for traffic to forward to:
    
    
    http://www.example.com/$1

In this case, if someone went to:
    
    
    example.com/some-particular-page.html

They would be redirected to:
    
    
    http://www.example.com/some-particular-page.html

[PreviousManage](https://developers.cloudflare.com/rules/page-rules/manage/)[NextSettings](https://developers.cloudflare.com/rules/page-rules/reference/settings/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/page-rules/how-to/url-forwarding.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
