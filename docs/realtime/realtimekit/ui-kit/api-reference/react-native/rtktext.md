---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtktext/
title: RtkText \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:11.505092+00:00
---

# RtkText · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtktext/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React Native
  5. /RtkText



# RtkText

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtktext/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

Themed text component that applies the design system's colors, font family, and font size.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`children` | `ReactNode` | ✅ | - | Text content  
`size` | `'sm' | 'md' | 'lg' | 'xl'` | ❌ | `'md'` | Font size (sm=14, md=16, lg=18, xl=20)  
`fontWeight` | `'normal' | 'bold' | '100' | '200' | '300' | '400' | '500' | '600' | '700' | '800' | '900'` | ❌ | `'normal'` | Font weight  
`style` | `StyleProp<TextStyle>` | ❌ | `\{\}` | Custom text styles  
`onBrand` | `boolean` | ❌ | `false` | Use brand text color instead of default text color  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkText } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return <RtkText>Hello World</RtkText>;
    }

### With Properties
    
    
    import { RtkText } from "@cloudflare/realtimekit-react-native-ui";
    
    function MyComponent() {
    	return (
    		<RtkText size="lg" fontWeight="bold" onBrand={true}>
    			Meeting Title
    		</RtkText>
    	);
    }

[PreviousRtkSpotlightGrid](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkspotlightgrid/)[NextRtkTextField](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtktextfield/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react-native/RtkText.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
