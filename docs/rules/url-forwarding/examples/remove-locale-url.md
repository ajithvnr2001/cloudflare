---
url: https://developers.cloudflare.com/rules/url-forwarding/examples/remove-locale-url/
title: Remove locale from URL path \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:00.296091+00:00
---

# Remove locale from URL path · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/url-forwarding/examples/remove-locale-url/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Redirects](https://developers.cloudflare.com/rules/url-forwarding/)

  4. /[Examples](https://developers.cloudflare.com/rules/url-forwarding/examples/)
  5. /Remove locale from URL path



# Remove locale from URL path

Create a redirect rule to redirect visitors from an old URL format with locale information to a new URL format.

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/url-forwarding/examples/remove-locale-url/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This example single redirect for zone `example.com` will redirect visitors from an old URL format that included the locale (for example, `/en-us/<page_name>`) to the new format `/<page_name>`.

**When incoming requests match**

  * **Field:** _URI Path_
  * **Operator:** _matches regex_
  * **Value:** `^/[A-Za-z]{2}-[A-Za-z]{2}/`



If you are using the Expression Editor, enter the following expression:  
`http.request.uri.path matches "^/[A-Za-z]{2}-[A-Za-z]{2}/"`

**Then**

  * **Type:** _Dynamic_
  * **Expression:** `regex_replace(http.request.uri.path, "^/[A-Za-z]{2}-[A-Za-z]{2}/(.*)", "/${1}")`
  * **Status code:** _301_
  * **Preserve query string:** Enabled



The function [`regex_replace()`](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#regex_replace) allows you to extract parts of the URL using regular expressions' capture groups. Create capture groups by putting part of the regular expression in parentheses. Then, reference a capture group using `${<num>}` in the replacement string, where `<num>` is the number of the capture group.

For example, the redirect rule would perform the following redirects:

Request URL | Target URL | Status code  
---|---|---  
`example.com/en-us/meet-our-team` | `example.com/meet-our-team` | `301`  
`example.com/pt-BR/meet-our-team` | `example.com/meet-our-team` | `301`  
`example.com/en-us/calendar?view=month` | `example.com/calendar?view=month` | `301`  
`example.com/meet-our-team` | (unchanged) | n/a  
`example.com/robots.txt` | (unchanged) | n/a  
  
[PreviousRedirect visitors to a new page URL](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-new-url/)[NextOverview](https://developers.cloudflare.com/rules/origin-rules/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/url-forwarding/examples/remove-locale-url.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
