---
url: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-new-url/
title: Redirect visitors to a new page URL \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:00.156118+00:00
---

# Redirect visitors to a new page URL · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-new-url/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Redirects](https://developers.cloudflare.com/rules/url-forwarding/)

  4. /[Examples](https://developers.cloudflare.com/rules/url-forwarding/examples/)
  5. /Redirect visitors to a new page URL



# Redirect visitors to a new page URL

Create a redirect rule to redirect visitors from `/contact-us/` to the page's new path `/contacts/`.

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-new-url/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This example static redirect for zone `example.com` will redirect visitors requesting the `/contact-us/` page to the new page URL `/contacts/`.

**When incoming requests match**

  * **Field:** _URI Path_
  * **Operator:** _equals_
  * **Value:** `/contact-us/`



If you are using the Expression Editor, enter the following expression:  
`http.request.uri.path eq "/contact-us/"`

**Then**

  * **Type:** _Static_
  * **URL:** `/contacts/`
  * **Status code:** _301_
  * **Preserve query string:** Enabled



For example, the redirect rule would perform the following redirects:

Request URL | Target URL | Status code  
---|---|---  
`example.com/contact-us/` | `example.com/contacts/` | `301`  
`example.com/contact-us/?state=TX` | `example.com/contacts/?state=TX` | `301`  
`example.com/team/` | (unchanged) | n/a  
  
[PreviousRedirect requests to a different hostname](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-different-hostname/)[NextRemove locale from URL path](https://developers.cloudflare.com/rules/url-forwarding/examples/remove-locale-url/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/url-forwarding/examples/redirect-new-url.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
