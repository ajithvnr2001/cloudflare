---
url: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/account_abuse_protection_events/
title: Account Abuse Protection Events \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:13.965458+00:00
---

# Account Abuse Protection Events · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/account_abuse_protection_events/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /…

[Logpush](https://developers.cloudflare.com/logs/logpush/)Logpush job setup[Datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/)

  4. /Zone-scoped datasets
  5. /Account Abuse Protection Events



# Account Abuse Protection Events

Last updated Sep 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/account_abuse_protection_events/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAuthenticationIdentityProviderAuthenticationMethodAuthenticationStatusBotScoreClientASNClientCityClientCountryClientIPEmailEphemeralIDEventSourceEventTypeFraudEmailRiskHostJA4RayIDTimestampUserAgentUserID

The descriptions below detail the fields available for `account_abuse_protection_events`.

## AuthenticationIdentityProvider

Type: `string`

The identity provider used for login authentication. Only populated for login events.   
Possible values are _unknown_ | _other_ | _selfHosted_ | _amazon_ | _apple_ | _discord_ | _facebook_ | _github_ | _linkedin_ | _microsoft_.

## AuthenticationMethod

Type: `string`

The authentication method used for login. Only populated for login events.   
Possible values are _unknown_ | _password_ | _sso_ | _magicLink_ | _biometric_ | _passkey_.

## AuthenticationStatus

Type: `string`

The outcome of a login attempt. Only populated for login events.   
Possible values are _unknown_ | _other_ | _success_ | _failureOther_ | _failureUserNotFound_ | _failureIncorrectPassword_ | _failureAccountLocked_ | _pendingMfa_.

## BotScore

Type: `int`

Cloudflare Bot Management score. Values from 1 (likely bot) to 99 (likely human).

## ClientASN

Type: `int`

Client AS number.

## ClientCity

Type: `string`

Approximate city of the client.

## ClientCountry

Type: `string`

2-letter ISO-3166 country code of the client IP address.

## ClientIP

Type: `string`

IP address of the client.

## Email

Type: `string`

The email address associated with the event.

## EphemeralID

Type: `string`

The Turnstile ephemeral device identifier, hex-encoded.

## EventSource

Type: `string`

The source of the Account Abuse Protection event.   
Possible values are _cdn_ | _api_.

## EventType

Type: `string`

The type of user action.   
Possible values are _login_ | _logout_ | _signup_ | _warpEnrollment_ | _profileUpdate_ | _transaction_ | _unknown_ | _passwordReset_ | _addPaymentMethod_.

## FraudEmailRisk

Type: `string`

Risk level of the email address.   
Possible values are _Unknown_ | _Low_ | _Medium_ | _High_.

## Host

Type: `string`

The HTTP hostname requested by the visitor.

## JA4

Type: `string`

The JA4 TLS client fingerprint.

## RayID

Type: `string`

The RayID of the request.

## Timestamp

Type: `int or string`

The date and time the event occurred. To specify the timestamp format, refer to [Output types](https://developers.cloudflare.com/logs/logpush/logpush-job/log-output-options/#output-types).

## UserAgent

Type: `string`

The user-agent string of the visitor.

## UserID

Type: `string`

A zone-unique identifier for the user, hex-encoded. Derived from the external user identifier provided during event submission.

[PreviousOverview](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/)[NextDNS logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/dns_logs/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/logpush/logpush-job/datasets/zone/account_abuse_protection_events.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
