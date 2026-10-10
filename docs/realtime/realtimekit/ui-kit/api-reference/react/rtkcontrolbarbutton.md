---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcontrolbarbutton/
title: RtkControlbarButton \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:46.301992+00:00
---

# RtkControlbarButton · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcontrolbarbutton/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkControlbarButton



# RtkControlbarButton

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A skeleton component used for composing custom controlbar buttons.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`brandIcon` | `boolean` | ✅ | - | Whether icon requires brand color  
`disabled` | `boolean` | ✅ | - | Whether button is disabled  
`icon` | `string` | ✅ | - | Icon  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`isLoading` | `boolean` | ✅ | - | Loading state Ignores current icon and shows a spinner if true  
`label` | `string` | ✅ | - | Label of button  
`showWarning` | `boolean` | ✅ | - | Whether to show warning icon  
`size` | `Size` | ✅ | - | Size  
`variant` | `ControlBarVariant1` | ✅ | - | Variant  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkControlbarButton } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkControlbarButton />;
    }

### With Properties
    
    
    import { RtkControlbarButton } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkControlbarButton
          brandIcon={true}
          disabled={true}
          icon="example"
        />
      );
    }

[PreviousRtkControlbar](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcontrolbar/)[NextRtkCounter](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcounter/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkControlbarButton.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
