---
url: https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/challenge-passage/
title: Challenge Passage \u00b7 Cloudflare challenges docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:58.788475+00:00
---

# Challenge Passage · Cloudflare challenges docs

> Source: https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/challenge-passage/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Challenges](https://developers.cloudflare.com/cloudflare-challenges/)
  3. /…

Available Challenges

  4. /[Interstitial Challenge Pages](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/)
  5. /Challenge Passage



# Challenge Passage

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/challenge-passage/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview How it works Customize the Challenge Passage Limitations

When a visitor solves a [Cloudflare Challenge](https://developers.cloudflare.com/cloudflare-challenges/) \- as part of a [WAF custom rule](https://developers.cloudflare.com/waf/custom-rules/) or [IP Access rule](https://developers.cloudflare.com/waf/tools/ip-access-rules/) \- you can set the **Challenge Passage** to prevent them from having to solve future Challenges for a specified period of time.

### How it works

When a visitor successfully solves a challenge, Cloudflare sets a [`cf_clearance` cookie](https://developers.cloudflare.com/fundamentals/reference/policies-compliances/cloudflare-cookies/#additional-cookies-used-by-the-challenge-platform) in their browser. This cookie specifies the duration your website is accessible to that visitor.

When that visitor tries to access other parts of your website, Cloudflare evaluates the cookie before presenting another challenge. If the cookie is still valid, no challenges will be shown.

When Cloudflare evaluates a `cf_clearance` cookie, a few extra minutes are included to account for clock skew. For XmlHTTP requests, an extra hour is added to the validation time to prevent breaking XmlHTTP requests for pages that set short lifetimes.

### Customize the Challenge Passage

By default, the `cf_clearance` cookie has a lifetime of 30 minutes. Cloudflare recommends a setting between 15 and 45 minutes.

To update the Challenge Passage (and the value of the `cf_clearance` cookie):

  1. In the Cloudflare dashboard, go to the **Security Settings** page.

[ Go to **Settings** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/settings)
  2. Go to **Challenge passage**.

  3. Select the edit icon to set a timeout duration.




### Limitations

The Challenge Passage does not apply to rate limiting rules.

[PreviousImplementation](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/create-custom-rule/)[NextDetect a Challenge Page response](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/detect-response/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-challenges/challenge-types/challenge-pages/challenge-passage.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
