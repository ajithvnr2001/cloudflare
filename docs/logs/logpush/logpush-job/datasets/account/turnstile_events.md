---
url: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/turnstile_events/
title: Turnstile Events \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:13.004378+00:00
---

# Turnstile Events · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/turnstile_events/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /…

[Logpush](https://developers.cloudflare.com/logs/logpush/)Logpush job setup[Datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/)

  4. /Account-scoped datasets
  5. /Turnstile Events



# Turnstile Events

Last updated Sep 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/turnstile_events/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewASNActionBrowserMajorBrowserNameClientIPCountryCodeEventTypeHostnameOSMajorOSNameSitekeyTimestampUserAgent

The descriptions below detail the fields available for `turnstile_events`.

## ASN

Type: `int`

The visitor's autonomous system number (ASN).

## Action

Type: `string`

The Turnstile widget action string configured by the customer.

## BrowserMajor

Type: `int`

The major version of the visitor's browser.

## BrowserName

Type: `string`

The name of the visitor's browser (for example, 'Chrome', 'Firefox').

## ClientIP

Type: `string`

IP address of the visitor.

## CountryCode

Type: `string`

The 2-letter ISO-3166 country code of the visitor.

## EventType

Type: `string`

The type of Turnstile event. Possible values are _challenge_issued_ | _challenge_non_interactive_solved_ | _challenge_interactive_solved_ | _challenge_non_interactive_siteverify_solved_ | _challenge_interactive_siteverify_solved_ | _challenge_clearance_siteverify_solved_ | _challenge_siteverify_failed_double_redemption_ | _challenge_siteverify_failed_invalid_token_ | _challenge_siteverify_failed_other_ | _challenge_siteverify_ratelimited_.

## Hostname

Type: `string`

The hostname where the Turnstile widget was loaded.

## OSMajor

Type: `int`

The major version of the visitor's operating system.

## OSName

Type: `string`

The name of the visitor's operating system (for example, 'Windows', 'macOS').

## Sitekey

Type: `string`

The Turnstile sitekey (widget identifier).

## Timestamp

Type: `int or string`

The date and time the event was logged.

## UserAgent

Type: `string`

The visitor's full user agent string.

[PreviousSSH Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/ssh_logs/)[NextWARP Config Changes](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/warp_config_changes/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/logpush/logpush-job/datasets/account/turnstile_events.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
