---
url: https://developers.cloudflare.com/turnstile/troubleshooting/client-side-errors/error-codes/
title: Error codes \u00b7 Cloudflare Turnstile docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:08.637153+00:00
---

# Error codes · Cloudflare Turnstile docs

> Source: https://developers.cloudflare.com/turnstile/troubleshooting/client-side-errors/error-codes/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Turnstile](https://developers.cloudflare.com/turnstile/)
  3. /…

Troubleshooting

  4. /[Client-side errors](https://developers.cloudflare.com/turnstile/troubleshooting/client-side-errors/)
  5. /Error codes



# Error codes

Last updated Sep 25, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/turnstile/troubleshooting/client-side-errors/error-codes/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewTroubleshooting

Note

When an error code is marked with `*`, the remaining digits can vary and are for internal use.

Error Code | Description | Retry | Troubleshooting  
---|---|---|---  
`110100` | Invalid sitekey | No | Verify the sitekey in [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/).  
`110110` | Sitekey not found | No | Check sitekey spelling and dashboard configuration.  
`110200` | Domain not authorized | No | Add current domain in Hostname Management.  
`110600` | Challenge timed out | Yes | The visitor's clock may be wrong, or the challenge took too long.  
`110620` | Interaction timed out | Yes | The visitor did not interact with the widget in time. Reset with `turnstile.reset()`.  
`200100` | Clock or cache problem | No | The visitor's clock is wrong or the challenge was cached by an intermediary.  
`200500` | Iframe load error | Yes | The Turnstile iframe could not load. Check if `challenges.cloudflare.com` is blocked.  
`300*` | Generic challenge failure | Yes | Bot behavior detected. Refer to troubleshooting.  
`400020` | Invalid sitekey | No | Verify the sitekey in [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/).  
`400021` | Sitekey domain mismatch | No | Sitekey region does not match domain in the [Turnstile script tag](https://developers.cloudflare.com/turnstile/get-started/client-side-rendering/#implementation).  
`400070` | Sitekey disabled | No | The sitekey is disabled. Check the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/).  
`600*` | Generic challenge failure | Yes | Bot behavior detected. Refer to troubleshooting.  
  
* * *

## Troubleshooting

You can troubleshoot these error codes using the following recommendations:

  1. Verify your browser compatibility. 
     * Turnstile supports all major browsers, except Internet Explorer.
     * Ensure your browser is up to date. For more information, refer to our [Supported browsers](https://developers.cloudflare.com/cloudflare-challenges/reference/supported-browsers/).
     * Run a test on the [compatibility checking tool ↗︎](https://debug.challenges.cloudflare.com/).
  2. Disable your browser extensions. 
     * Some browser extensions, such as ad blockers, may block the scripts Turnstile needs to operate.
     * Temporarily disable all extensions and reload the page.
  3. Enable JavaScript. 
     * Turnstile requires JavaScript to run. Ensure it is enabled in your browser settings. Refer to your browser's documentation for instructions on enabling JavaScript.
  4. Try Incognito or Private mode. 
     * Use your browser's incognito or private mode to rule out issues caused by extensions or cached data.
  5. Test another browser or device. 
     * Switch to a different browser or device to see if the issue is specific to your current setup.
  6. Avoid VPNs or proxies. 
     * Some virtual private networks (VPN) or proxies may interfere with Turnstile. Disable them temporarily to test.
  7. Switch to a different network. 
     * Your current network may have restrictions causing Turnstile challenges to fail. Try switching to another network, such as a mobile hotspot.



Error code `401`

Turnstile may occasionally generate a `401` Unauthorized error in your browser console during a security check. This is not typically a problem with your implementation. This error often occurs when the widget attempts to request a [Private Access Token](https://developers.cloudflare.com/cloudflare-challenges/reference/private-access-tokens/) that your device or browser does not support yet.

You can generally safely ignore the `401` error, as it is an expected part of Turnstile's underlying Challenge Platform workflow. If the widget is successfully resolving and you are receiving a token, no action is required.

[PreviousOverview](https://developers.cloudflare.com/turnstile/troubleshooting/client-side-errors/)[NextChallenge solve issues ↗︎](https://developers.cloudflare.com/cloudflare-challenges/troubleshooting/challenge-solve-issues/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/turnstile/troubleshooting/client-side-errors/error-codes.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
