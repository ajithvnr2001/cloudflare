---
url: https://developers.cloudflare.com/logs/reference/security-fields/
title: Security fields \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:17.385456+00:00
---

# Security fields · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/reference/security-fields/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /[Reference](https://developers.cloudflare.com/logs/reference/)
  4. /Security fields



# Security fields

Last updated Jul 10, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/reference/security-fields/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSecurityActionsSecuritySources

The Security fields contain rules to block requests that contain specific types of content.

## SecurityActions

Value | Action | Description  
---|---|---  
`unknown` | Unknown | Take no other action.  
`allow` | Allow | Bypass all subsequent rules.  
`block` | Drop | Block with an HTTP status code of 403, 429, or any other [4XX](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/) status code.  
`challenge` | Challenge Drop | Issue an interactive challenge.  
`jschallenge` | Challenge Drop | Issue a non-interactive challenge.  
`log` | Log | Take no action other than logging the event.  
`connectionClose` | Close | Close connection.  
`challengeSolved` | Allow | Allow once interactive challenge solved.  
`challengeBypassed` | Allow | Interactive challenge is not issued again because the visitor had previously passed an interactive challenge and a valid `cf_clearance` cookie is present.  
`jschallengeSolved` | Allow | Allow once non-interactive challenge solved.  
`jschallengeBypassed` | Allow | Non-interactive challenge not issued because the visitor had previously passed a non-interactive or interactive challenge.  
`bypass` | Allow | Bypass all subsequent firewall rules.  
`managedChallenge` | Challenge Drop | Issue managed challenge.  
`managedChallengeNonInteractiveSolved` | Allow | Allow once the managed challenge is solved via non-interactive interstitial page.  
`managedChallengeInteractiveSolved` | Allow | Allow once the managed challenged is solved via interactive interstitial page.  
`managedChallengeBypassed` | Allow | Challenge was not presented because visitor had clearance from previous challenge.  
  
## SecuritySources

Value | Description  
---|---  
`unknown` | Used if an event is received from a new source but the logging system has not been updated.  
`asn` | Allow or block based on autonomous system number.  
`country` | Allow or block based on country.  
`ip` | Allow or block based on IP address.  
`ipRange` | Allow or block based on range of IP addresses.  
`securityLevel` | Allow or block based on requester's security level.  
`zoneLockdown` | Restrict all access to a specific zone.  
`waf` | Allow or block based on the WAF product settings. This is the WAF/managed rules system that is being phased out.  
`firewallRules` | Allow or block based on a zone's firewall rules configuration (deprecated).  
`uaBlock` | Allow or block based on the Cloudflare User Agent Blocking product settings.  
`rateLimit` | Allow or block based on a rate limiting rule, whether set by you or by Cloudflare.  
`bic` | Allow or block based on the Browser Integrity Check product settings.  
`hot` | Allow or block based on the Hotlink Protection product settings.  
`l7ddos` | Allow or block based on the L7 DDoS product settings.  
`validation` | Allow or block based on a request that is invalid (cannot be customized.)  
`botFight` | Allow or block based on the Bot Fight Mode (classic) product settings.  
`botManagement` | Allow or block based on the Bot Management product settings.  
`dlp` | Allow or block based on the Data Loss Prevention product settings.  
`firewallManaged` | Allow or block based on WAF Managed Rules' settings.  
`firewallCustom` | Allow or block based on a rule configured in WAF custom rules.  
  
[PreviousPathing status](https://developers.cloudflare.com/logs/reference/pathing-status/)[NextWAF fields](https://developers.cloudflare.com/logs/reference/waf-fields/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/reference/security-fields.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
