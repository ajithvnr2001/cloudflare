---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-image-message/
title: rtk-image-message \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:13:24.800418+00:00
---

# rtk-image-message · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-image-message/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /Angular
  5. /rtk-image-message



# rtk-image-message

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-image-message/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

@deprecated `rtk-image-message` is deprecated and will be removed soon. Use `rtk-image-message-view` instead. A component which renders an image message from chat.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`isContinued` | `boolean` | ✅ | - | Whether the message is continued by same user  
`message` | `ImageMessage` | ✅ | - | Text message object  
`now` | `Date` | ✅ | - | Date object of now, to calculate distance between dates  
`showBubble` | `boolean` | ✅ | - | show message in bubble  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    <!-- component.html -->
    <rtk-image-message></rtk-image-message>

### With Properties
    
    
    <!-- component.html -->
    <rtk-image-message
     [isContinued]="true"
     [message]="imagemessage"
     [now]="date">
    </rtk-image-message>

[Previousrtk-idle-screen](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-idle-screen/)[Nextrtk-image-message-view](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-image-message-view/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/angular/rtk-image-message.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
