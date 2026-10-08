---
url: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpollform/
title: RtkPollForm \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:27.293668+00:00
---

# RtkPollForm · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpollform/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/)Component Reference

  4. /React
  5. /RtkPollForm



# RtkPollForm

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpollform/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPropertiesUsage Examples Basic Usage With Properties

A component that lets you create a poll.

## Properties

Property | Type | Required | Default | Description  
---|---|---|---|---  
`iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack  
`t` | `RtkI18n` | ❌ | `useLanguage()` | Language  
  
## Usage Examples

### Basic Usage
    
    
    import { RtkPollForm } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return <RtkPollForm />;
    }

### With Properties
    
    
    import { RtkPollForm } from '@cloudflare/realtimekit-react-ui';
    
    function MyComponent() {
      return (
        <RtkPollForm
          iconPack={defaultIconPack}
          t={rtki18n}
        />
      );
    }

[PreviousRtkPoll](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpoll/)[NextRtkPolls](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpolls/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/ui-kit/api-reference/react/RtkPollForm.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
