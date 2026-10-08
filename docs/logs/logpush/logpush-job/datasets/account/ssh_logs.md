---
url: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/ssh_logs/
title: SSH Logs \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:13.041458+00:00
---

# SSH Logs · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/ssh_logs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /…

[Logpush](https://developers.cloudflare.com/logs/logpush/)Logpush job setup[Datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/)

  4. /Account-scoped datasets
  5. /SSH Logs



# SSH Logs

Last updated Sep 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/ssh_logs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAccountIDClientAddressDatetimeErrorPTYPayloadProgramFinishDatetimeProgramIDProgramStartDatetimeProgramTypeServerAddressSessionFinishDatetimeSessionIDSessionStartDatetimeTargetIDUserEmailUserIDUsername

The descriptions below detail the fields available for `ssh_logs`.

## AccountID

Type: `string`

Cloudflare account ID.

## ClientAddress

Type: `string`

The source address of the SSH command.

## Datetime

Type: `int or string`

The timestamp in UTC of when this message is being sent.

## Error

Type: `string`

An SSH error. Only used if an error has occurred.

## PTY

Type: `string`

This is used by certain programs types to synchronize local and remote SSH terminal state.

## Payload

Type: `string`

The captured request/response data, in asciicast v2 format. This includes the command associated with the 'exec' program type.

## ProgramFinishDatetime

Type: `int or string`

The timestamp in UTC of the SSH program termination. This is empty until the program ends.

## ProgramID

Type: `string`

The SSH program ID. A single SSH session can have multiple programs running.

## ProgramStartDatetime

Type: `int or string`

The timestamp in UTC of the SSH program creation.

## ProgramType

Type: `string`

The SSH program being run. The options are 'shell': opens an interactive terminal, 'exec': execute a single specified command, 'x11': is for an interactive graphical environment, 'direct-tcpip': direct tunneling, 'forwarded-tcpip': reverse tunneling.

## ServerAddress

Type: `string`

The destination address for the SSH session.

## SessionFinishDatetime

Type: `int or string`

The timestamp in UTC of the SSH session termination. This is empty until the session ends.

## SessionID

Type: `string`

SSH session ID.

## SessionStartDatetime

Type: `int or string`

The timestamp in UTC of the SSH session creation.

## TargetID

Type: `string`

The identifier of the target being accessed.

## UserEmail

Type: `string`

User email address.

## UserID

Type: `string`

Cloudflare user ID.

## Username

Type: `string`

The principal user being accessed on SSH server's machine. This will be empty if an error was thrown when establishing the connection.

[PreviousSinkhole HTTP Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/sinkhole_http_logs/)[NextTurnstile Events](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/turnstile_events/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/logpush/logpush-job/datasets/account/ssh_logs.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
