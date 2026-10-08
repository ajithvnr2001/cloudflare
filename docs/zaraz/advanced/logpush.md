---
url: https://developers.cloudflare.com/zaraz/advanced/logpush/
title: Send Zaraz logs to Logpush \u00b7 Cloudflare Zaraz docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:18:17.037479+00:00
---

# Send Zaraz logs to Logpush · Cloudflare Zaraz docs

> Source: https://developers.cloudflare.com/zaraz/advanced/logpush/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Zaraz](https://developers.cloudflare.com/zaraz/)
  3. /[Advanced options](https://developers.cloudflare.com/zaraz/advanced/)
  4. /Logpush



# Send Zaraz logs to Logpush

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/zaraz/advanced/logpush/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSetup 1\. Create a Logpush job 2\. Enable Logpush from Zaraz settingsFields

Send Zaraz logs to an external storage provider like R2 or S3.

This is an Enterprise only feature.

## Setup

Follow these steps to configure Logpush support for Zaraz:

### 1\. Create a Logpush job

  1. In the Cloudflare dashboard, go to the **Logpush** page.

[ Go to **Logpush** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/analytics/logs)
  2. Select **Create a Logpush Job** and follow the steps described in the [Logpush](https://developers.cloudflare.com/logs/logpush/) documentation.  
When selecting a dataset, make sure you select **Zaraz Events**.




### 2\. Enable Logpush from Zaraz settings

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com), go to **Delivery & Performance** > **Web tag management** > **Tag setup** > select your domain > **Settings**.

Alternatively, navigate directly to [Zaraz settings ↗︎](https://dash.cloudflare.com/?to=/:account/tag-management/zaraz/:zone/tools-config/tools)

  2. Enable **Export Zaraz Logs**.




Note

Zaraz must already be configured on your zone to access the Settings page. If Zaraz has not been set up yet, you will be prompted to complete the initial setup first.

## Fields

Logs will have the following fields:

Field | Type | Description  
---|---|---  
RequestHeaders | `JSON` | The headers that were sent with the request.  
URL | `String` | The Zaraz URL to which the request was made.  
IP | `String` | The originating IP.  
Body | `JSON` | The body that was sent along with the request.  
Event Type | `String` | Can be one of the following: `server_request`, `server_response`, `action_triggered`, `ecommerce_triggered`, `client_request`, `component_error`.  
Event Details | `JSON` | Details about the event.  
TimestampStart | `String` | The time at which the event occurred.  
  
[PreviousUsing JSONata](https://developers.cloudflare.com/zaraz/advanced/using-jsonata/)[NextCustom Managed Components](https://developers.cloudflare.com/zaraz/advanced/load-custom-managed-component/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/zaraz/advanced/logpush.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
