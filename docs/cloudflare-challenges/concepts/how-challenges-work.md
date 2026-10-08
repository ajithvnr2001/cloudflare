---
url: https://developers.cloudflare.com/cloudflare-challenges/concepts/how-challenges-work/
title: How Challenges work \u00b7 Cloudflare challenges docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:58.824312+00:00
---

# How Challenges work · Cloudflare challenges docs

> Source: https://developers.cloudflare.com/cloudflare-challenges/concepts/how-challenges-work/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Challenges](https://developers.cloudflare.com/cloudflare-challenges/)
  3. /Concepts
  4. /Challenges



# How Challenges work

Last updated Jul 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-challenges/concepts/how-challenges-work/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAvailable challengesLimitations

Challenges can be issued in three primary ways depending on which Cloudflare products or features are in use. Each method is designed to balance security with seamless visitor experience.

Product | Challenge type(s)  
---|---  
[WAF](https://developers.cloudflare.com/waf/) ([custom rules](https://developers.cloudflare.com/waf/custom-rules/), [rate limiting rules](https://developers.cloudflare.com/waf/rate-limiting-rules/), [IP access rules](https://developers.cloudflare.com/waf/tools/ip-access-rules/)) | [Interstitial Challenge Page](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/)  
[Bot Management](https://developers.cloudflare.com/bots/get-started/bot-management/) | [JavaScript Detections](https://developers.cloudflare.com/bots/additional-configurations/javascript-detections/)  
[Bot Fight Mode](https://developers.cloudflare.com/bots/get-started/bot-fight-mode/), [Super Bot Fight Mode](https://developers.cloudflare.com/bots/get-started/super-bot-fight-mode/) | [Interstitial Challenge Page](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/)  
[Turnstile](https://developers.cloudflare.com/turnstile/) | Embedded widget  
[HTTP DDoS attack protection](https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/) | Any Challenge  
[Under Attack Mode](https://developers.cloudflare.com/fundamentals/reference/under-attack-mode/) | [Managed Challenge](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/#managed-challenge)  
  
Challenge Pages and Turnstile rely on the same underlying mechanism to issue challenges to your website or application's visitors.

JavaScript Detections is an optional feature within [Bot Management](https://developers.cloudflare.com/bots/get-started/bot-management/). When enabled, Cloudflare injects a JavaScript snippet into HTML responses to gather client-side signals. Unlike Challenge Pages, JavaScript Detections runs on every HTML request without pausing or interrupting the visitor. It populates a pass/fail result (`cf.bot_management.js_detection.passed`) that you can then act on using a [WAF custom rule](https://developers.cloudflare.com/waf/custom-rules/).

For session-level detection that informs when challenges should be applied, refer to [Precursor](https://developers.cloudflare.com/cloudflare-challenges/precursor/).

* * *

## Available challenges

Refer to the following pages for more information on the different challenge types:

  * [Interstitial Challenge Pages](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/)
  * [Turnstile](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/turnstile/)
  * [JavaScript Detections](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/javascript-detections/)
  * [Precursor](https://developers.cloudflare.com/cloudflare-challenges/precursor/)



* * *

## Limitations

Cloudflare Challenges cannot support the following:

  * [Browser extensions](https://developers.cloudflare.com/cloudflare-challenges/reference/supported-browsers/#browser-extensions) that modify the browser's `User-Agent` value or Web APIs such as `Canvas` and `WebGL`.
  * Implementations where a domain serves a challenge page originally requested for another domain.
  * Challenge Pages cannot be embedded in cross-origin iframes.
  * Client software where the solve request of a Managed Challenge comes from a different IP than the original IP a Challenge request was issued to. For example, if you receive the Challenge from one IP and solve it using another IP, the solve is not valid and you may encounter a Challenge loop.



[PreviousOverview](https://developers.cloudflare.com/cloudflare-challenges/)[NextClearance](https://developers.cloudflare.com/cloudflare-challenges/concepts/clearance/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-challenges/concepts/how-challenges-work.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
