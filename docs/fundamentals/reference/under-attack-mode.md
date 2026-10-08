---
url: https://developers.cloudflare.com/fundamentals/reference/under-attack-mode/
title: Under Attack mode \u00b7 Cloudflare Fundamentals docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:27.260912+00:00
---

# Under Attack mode · Cloudflare Fundamentals docs

> Source: https://developers.cloudflare.com/fundamentals/reference/under-attack-mode/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)
  3. /Reference
  4. /Under Attack mode



# Under Attack mode

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/fundamentals/reference/under-attack-mode/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewTurn on Under Attack mode Globally SelectivelyPreview Under Attack modePotential issues

Cloudflare's Under Attack mode performs additional security checks to help mitigate layer 7 DDoS attacks. Validated users access your website and suspicious traffic is blocked. It is designed to be used as one of the last resorts when a zone is under attack (and will temporarily pause access to your site and impact your site analytics).

When enabled, visitors receive an interstitial page.

## Turn on Under Attack mode

Under Attack mode is turned off by default for your zone.

### Globally

To put your entire zone in Under Attack mode:

  1. In the Cloudflare dashboard, select your account and zone from the **Account home** page.

[ Go to **Account home** ↗ ](https://dash.cloudflare.com/?to=/:account/home)
  2. In the zone overview page, turn on **Under Attack Mode** in the **Quick Actions** sidebar.




### Selectively

To enable Under Attack mode for specific pages or sections of your site, use a [configuration rule](https://developers.cloudflare.com/rules/configuration-rules/) to adjust the **Security Level**.

**When incoming requests match**

  * **Field:** _URI Path_
  * **Operator:** _starts with_
  * **Value:** `/admin`



If you are using the Expression Editor, enter the following expression:  
`(starts_with(http.request.uri.path, "/admin"))`

**Then the settings are**

  1. For **I'm Under Attack** , select **Add**.
  2. Switch the toggle to **On**.



To turn it on for specific ASNs (hosts/ISPs that own IP addresses), countries, or IP ranges, use [IP Access Rules](https://developers.cloudflare.com/waf/tools/ip-access-rules/).

* * *

## Preview Under Attack mode

To preview what Under Attack mode looks like for your visitors:

  1. In the Cloudflare dashboard, go to the **Configurations** page.

[ Go to **Configurations** ↗ ](https://dash.cloudflare.com/?to=/:account/configurations)
  2. Go to **Custom Pages**.

  3. For **Managed Challenge / I'm Under Attack Mode™** , select **Custom Pages** > **View default**.




The `Checking your browser before accessing...` challenge determines whether to block or allow a visitor within five seconds. After passing the challenge, the visitor does not observe another challenge until the duration configured in [Challenge Passage](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/challenge-passage/).

* * *

## Potential issues

Since the Under Attack mode requires your browser to support JavaScript to display and pass the interstitial page, it is expected to observe impact on third party analytics tools.

[PreviousTCP connections](https://developers.cloudflare.com/fundamentals/reference/tcp-connections/)[NextAvailable RSS Feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/fundamentals/reference/under-attack-mode.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
