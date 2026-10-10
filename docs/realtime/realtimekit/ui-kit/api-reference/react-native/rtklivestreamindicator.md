---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtklivestreamindicator/
title: RtkLiveStreamIndicator \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:53.663424+00:00
---

# RtkLiveStreamIndicator · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtklivestreamindicator/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkLiveStreamIndicator



# RtkLiveStreamIndicator

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Displays a "Live" indicator when a livestream is active. Only visible in livestream mode for off-stage viewers.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit meeting instance  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Custom icon pack  
`size` | `'lg' | 'md' | 'sm' | 'xl'` | ❌ | `'sm'` | Size variant  
`t` | `RtkI18n` | ❌ | `useLanguage()` | i18n translation function  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkLiveStreamIndicator } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkLiveStreamIndicator meeting={meeting} />;
    }

### With Properties
    
    
    import { RtkLiveStreamIndicator } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkLiveStreamIndicator meeting={meeting} size="md" />;
    }

[PreviousRtkLeaveMeeting](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkleavemeeting/)[NextRtkLiveStreamPlayer](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtklivestreamplayer/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkLiveStreamIndicator.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
