---
url: https://developers.cloudflare.com/zaraz/advanced/load-zaraz-manually/
title: Load Zaraz manually \u00b7 Cloudflare Zaraz docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:18:17.008394+00:00
---

# Load Zaraz manually · Cloudflare Zaraz docs

> Source: https://developers.cloudflare.com/zaraz/advanced/load-zaraz-manually/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Zaraz](https://developers.cloudflare.com/zaraz/)
  3. /[Advanced options](https://developers.cloudflare.com/zaraz/advanced/)
  4. /Load Zaraz manually



# Load Zaraz manually

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/zaraz/advanced/load-zaraz-manually/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

By default, if your domain is proxied by Cloudflare, Zaraz will automatically inject itself to HTML pages in your site. This makes it easier to get up and running quickly. However, you might want to load Zaraz manually, for example to test Zaraz on specific pages first.

After you turn off the [Auto-inject script](https://developers.cloudflare.com/zaraz/reference/settings/#auto-inject-script) option, you will have to manually include the Zaraz script in your HTML, immediately before the `</head>` tag closes. The path to your script would be `/cdn-cgi/zaraz/i.js`. Your script tag should look like this:
    
    
    <script src="/cdn-cgi/zaraz/i.js" referrerpolicy="origin"></script>

With the script, your page HTML should be similar to the following:
    
    
    <html>
      <head>
        ….
        <script src="/cdn-cgi/zaraz/i.js" referrerpolicy="origin"></script>
      </head>
      <body>
        …
      </body>
    </html>

Note that if your site is not proxied by Cloudflare, you should refer to the section about [Using Zaraz on domains not proxied by Cloudflare](https://developers.cloudflare.com/zaraz/advanced/domains-not-proxied/).

[PreviousGoogle Consent Mode](https://developers.cloudflare.com/zaraz/advanced/google-consent-mode/)[NextConfiguration Import & Export](https://developers.cloudflare.com/zaraz/advanced/import-export/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/zaraz/advanced/load-zaraz-manually.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
