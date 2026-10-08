---
url: https://search.ai.cloudflare.com/
title: AI Search Snippets - Embed AI Search on your website
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:08.189595+00:00
---

# AI Search Snippets - Embed AI Search on your website

> Source: https://search.ai.cloudflare.com/

#### Search Bar

Inline search input with real-time results dropdown. Perfect for navigation bars and sidebars.

#### Search Modal

Command palette style search with Cmd/Ctrl+K keyboard shortcut. Great for documentation sites.

#### Chat Bubble

Floating chat widget that opens from the corner of any page. Ideal for support and assistance.

#### Chat Page

Full-page conversational interface with message history. Best for dedicated chat experiences.

× 

Search Bar  Search Modal  Chat Bubble  Chat Page 

Reset 

### Props

### CSS Variables

Light  Dark 

###  Live Preview 

###  Generated Code 

HTML  React  Vue 

index.html Copy


App.tsx Copy


App.vue Copy


## Quick Start Guide

Add search and chat to your website in minutes.

HTML  React  Vue 

index.html Copy
    
    
    <!-- Import the library -->
    <script type="module" src="https://<hash>.search.ai.cloudflare.com/assets/v0.0.40/search-snippet.es.js"></script>
    
    <!-- 1. Chat Bubble Widget (Fixed bottom-right) -->
    <chat-bubble-snippet 
        api-url="https://api.example.com">
    </chat-bubble-snippet>
    
    <!-- 2. Search Bar Widget -->
    <search-bar-snippet 
        api-url="https://api.example.com"
        placeholder="Search..."
        max-results="50"
        max-render-results="10"
        show-url="true"
        show-date="true">
    </search-bar-snippet>
    
    <!-- 3. Search Modal (Cmd/Ctrl+K to open) -->
    <search-modal-snippet 
        api-url="https://api.example.com"
        placeholder="Search documentation..."
        shortcut="k"
        show-url="true"
        show-date="true">
    </search-modal-snippet>
    
    <!-- 4. Full Page Chat (use in dedicated page) -->
    <chat-page-snippet 
        api-url="https://api.example.com">
    </chat-page-snippet>
    
    <!-- Customize with CSS Variables -->
    <style>
        chat-bubble-snippet {
            --search-snippet-primary-color: #F6821F;
            --search-snippet-border-radius: 12px;
        }
    </style>

App.tsx Copy
    
    
    import "@cloudflare/ai-search-snippet";
    
    // Usage in your app
    export default function App() {
      return (
        <div>
          <search-bar-snippet 
            apiUrl="https://api.example.com"
            placeholder="Search..."
            maxResults={50}
            maxRenderResults={10}
            show-url="true"
            show-date="true"
          />
    
          {/* Chat Bubble - works directly as Web Component */}
          <chat-bubble-snippet 
            apiUrl="https://api.example.com"
            style={{ '--search-snippet-primary-color': '#F6821F' } as React.CSSProperties}
          />
    
          {/* Search Modal with keyboard shortcut */}
          <search-modal-snippet 
            apiUrl="https://api.example.com"
            placeholder="Search documentation..."
            shortcut="k"
            show-url="true"
            show-date="true"
          />
        </div>
      );
    }
    
    // TypeScript declarations see example here: https://github.com/cloudflare/ai-search-snippet/blob/main/demos/react/index.d.ts

App.vue Copy
    
    
    <script setup lang="ts">
    import "@cloudflare/ai-search-snippet";
    import { ref } from 'vue';
    
    const apiUrl = 'https://api.example.com';
    const searchPlaceholder = ref('Search...');
    const maxResults = ref(50);
    const maxRenderResults = ref(10);
    
    // Handle custom events from components
    function onSearchComplete(event: CustomEvent) {
      console.log('Search results:', event.detail);
    }
    
    function onChatMessage(event: CustomEvent) {
      console.log('Chat message:', event.detail);
    }
    </script>
    
    <template>
      <div>
        <!-- Search Bar with v-bind -->
        <search-bar-snippet
          :api-url="apiUrl"
          :placeholder="searchPlaceholder"
          :max-results="maxResults"
          :max-render-results="maxRenderResults"
          show-url="true"
          show-date="true"
          @search-complete="onSearchComplete"
        />
    
        <!-- Chat Bubble Widget -->
        <chat-bubble-snippet
          :api-url="apiUrl"
          placeholder="Ask me anything..."
          @chat-message="onChatMessage"
        />
    
        <!-- Search Modal (Cmd/Ctrl+K) -->
        <search-modal-snippet
          :api-url="apiUrl"
          placeholder="Search documentation..."
          shortcut="k"
          show-url="true"
          show-date="true"
        />
    
        <!-- Full Page Chat -->
        <chat-page-snippet
          :api-url="apiUrl"
          class="chat-container"
        />
      </div>
    </template>
    
    <style>
    /* Customize with CSS Variables */
    search-bar-snippet,
    chat-bubble-snippet {
      --search-snippet-primary-color: #F6821F;
      --search-snippet-border-radius: 12px;
    }
    
    .chat-container {
      height: 500px;
    }
    </style>
    
    <!-- vite.config.ts - Configure Vue to recognize custom elements -->
    <!--
    import { defineConfig } from 'vite';
    import vue from '@vitejs/plugin-vue';
    
    export default defineConfig({
      plugins: [
        vue({
          template: {
            compilerOptions: {
              isCustomElement: (tag) => tag.includes('-snippet')
            }
          }
        })
      ]
    });
    -->

## Why AI Search?

Everything you need to add intelligent search to your applications.

#### Deploy in minutes

Production-ready components out of the box. Just import and use.

#### Always up-to-date

Continuously indexes your data so responses reflect the latest information.

#### Edge-based inference

Runs at the edge, closer to users for reduced latency.

#### Framework agnostic

Works with React, Vue, Angular, or vanilla JavaScript.

#### Zero dependencies

Self-contained Web Components with everything bundled.

#### Fully customizable

50+ CSS variables for complete theme control.

## Component API Reference

HTML attributes (props) and JavaScript methods available for each component.

#### Common Props (All Components)

Attribute| Type| Default| Description  
---|---|---|---  
`api-url`| string| Required| AI Search API endpoint URL  
`placeholder`| string| "Search..." / "Type a message..."| Input placeholder text  
`theme`| "light" | "dark" | "auto"| "auto"| Color scheme (auto follows system preference)  
`hide-branding`| boolean| false| Hide "Powered by Cloudflare" branding  
`translations`| JSON string / object| -| Override any user-facing string. Omitted keys fall back to English defaults. See Translations section below.  
  
#### <search-bar-snippet> Props

Attribute| Type| Default| Description  
---|---|---|---  
`max-results`| number| 50| Maximum number of results to request from the API  
`max-render-results`| number| 10| Maximum number of results rendered in the UI (drives the "see more" affordance)  
`debounce-ms`| number| 300| Input debounce delay in milliseconds  
`show-url`| boolean| false| Show URL in search results  
`show-date`| boolean| false| Show result dates when a timestamp is available  
`hide-thumbnails`| boolean| false| Hide result thumbnails/images  
`group-by`| string| -| Group results by an item metadata field  
`request-options`| JSON string| -| Extra search request configuration with headers, query params, and body fields  
`see-more`| string| -| URL template for "See more" link. The search query is appended URL-encoded (e.g. "https://example.com/search?q=")  
  
##### Methods

Method| Parameters| Returns| Description  
---|---|---|---  
`search(query)`| query: string| Promise<void>| Programmatically perform a search  
  
#### <search-modal-snippet> Props

Attribute| Type| Default| Description  
---|---|---|---  
`max-results`| number| 50| Maximum number of results to request from the API  
`max-render-results`| number| 10| Maximum number of results rendered in the UI (drives the "see more" affordance)  
`debounce-ms`| number| 300| Input debounce delay in milliseconds  
`show-url`| boolean| false| Show URL in search results  
`show-date`| boolean| false| Show result dates when a timestamp is available  
`hide-thumbnails`| boolean| false| Hide result thumbnails/images  
`group-by`| string| -| Group results by an item metadata field  
`request-options`| JSON string| -| Extra search request configuration with headers, query params, and body fields  
`shortcut`| string| "k"| Keyboard shortcut key (used with Cmd/Ctrl)  
`use-meta-key`| "true" | "false"| "true"| Use Cmd/Ctrl modifier for keyboard shortcut  
`see-more`| string| -| URL template for "See more" link. The search query is appended URL-encoded (e.g. "https://example.com/search?q=")  
  
##### Methods

Method| Parameters| Returns| Description  
---|---|---|---  
`open()`| -| void| Open the search modal  
`close()`| -| void| Close the search modal  
`toggle()`| -| void| Toggle the modal open/closed  
`search(query)`| query: string| Promise<void>| Open modal and perform search  
`getResults()`| -| SearchResult[]| Get current search results  
`isModalOpen()`| -| boolean| Check if modal is currently open  
  
#### Metadata-driven Result Icons

Set item metadata.icon to a lowercase kebab-case slug such as "page" or "section". Search components expose matching CSS Shadow Parts; icons remain collapsed until a ::part() rule gives them a display value.

Metadata value| CSS selector| Description  
---|---|---  
`page`| `::part(result-icon-page)`| Style a page icon  
`section`| `::part(result-icon-section)`| Style a section icon or text glyph  
  
#### <chat-bubble-snippet> Props

Uses the common props (api-url, placeholder, theme, hide-branding) plus the chat-only attributes below.

Attribute| Type| Default| Description  
---|---|---|---  
`chat-query-rewrite`| JSON string| -| Configure AI Search query rewriting on subsequent chat turns. See the Chat Query Rewrite section below.  
  
##### Methods

Method| Parameters| Returns| Description  
---|---|---|---  
`clearChat()`| -| void| Clear all chat messages  
`sendMessage(content)`| content: string| Promise<void>| Programmatically send a message  
`getMessages()`| -| Message[]| Get all chat messages  
  
#### <chat-page-snippet> Props

Uses the common props (api-url, placeholder, theme, hide-branding) plus the chat-only attributes below. Includes session history with localStorage persistence.

Attribute| Type| Default| Description  
---|---|---|---  
`chat-query-rewrite`| JSON string| -| Configure AI Search query rewriting on subsequent chat turns. See the Chat Query Rewrite section below.  
  
##### Methods

Method| Parameters| Returns| Description  
---|---|---|---  
`clearChat()`| -| void| Clear current chat session  
`sendMessage(content)`| content: string| Promise<void>| Programmatically send a message  
`getMessages()`| -| Message[]| Get messages from current session  
`getSessions()`| -| ChatSession[]| Get all chat sessions  
`getCurrentSession()`| -| ChatSession | null| Get the current active session  
  
#### Search Request Options

Use the `request-options` attribute on search components or the `request` option on `AISearchClient.search()` and `searchStream()` to enrich search requests.

Key| Type| Description  
---|---|---  
`headers`| Record<string, string>| Extra headers to send with search requests  
`queryParams`| Record<string, string | number | boolean>| Extra query params appended to the request URL  
`body`| Record<string, unknown>| Extra JSON fields merged into the request body  
  
##### Notes

Behavior| Details  
---|---  
Conflict resolution| Core request fields still win over conflicts: `messages`, `stream`, `max_num_results`, and the default search `ai_search_options.retrieval.metadata_only` value.  
  
#### Chat Query Rewrite

Multi-turn chat sends the full conversation to the API so AI Search can rewrite the latest user message into a self-contained retrieval query. Rewriting is automatic from the second user message onward — the first message has no history to rewrite against. Configure via the `chat-query-rewrite` attribute (or `chatQueryRewrite` JS property) on `<chat-bubble-snippet>` and `<chat-page-snippet>`.

##### Configuration keys

Key| Type| Default| Description  
---|---|---|---  
`enabled`| boolean| true (on subsequent turns)| Set to `false` to disable query rewriting entirely. `true` keeps the default behavior — first turn always sends without rewriting.  
`model`| string| "@cf/meta/llama-3.3-70b-instruct-fp8-fast"| Model used by AI Search to rewrite the conversation into a search query. Accepts any model id supported by the AI Search query_rewrite option.  
`rewritePrompt`| string| Built-in prompt| System prompt sent to the rewriter as `rewrite_prompt`. The default instructs the model to resolve coreferences from prior turns and emit a single standalone query.  
  
##### Wire format

Behavior| Details  
---|---  
Request body| Subsequent chat requests include the full prior `messages` (user + assistant turns) plus the new user message, and `ai_search_options.query_rewrite: { enabled, model, rewrite_prompt }`.  
First turn| Sends just the new user message with no `ai_search_options` block, regardless of `enabled`.  
Disabling| Pass `{"enabled": false}` to skip rewriting on every turn — history is still forwarded, but the request omits `ai_search_options.query_rewrite`.  
  
#### AISearchClient

##### Methods

Method| Parameters| Returns| Description  
---|---|---|---  
`search(query, options?)`| query: string, options?: { maxResults?, signal?, request? }| Promise<SearchResult[]>| Perform a search request with optional request enrichment  
`searchStream(query, options?)`| query: string, options?: { maxResults?, signal?, request? }| AsyncGenerator<SearchResult | SearchError>| Perform a streaming search request with optional request enrichment  
`chat(query, options?)`| query: string, options?: { stream?, signal?, history?, queryRewrite? }| AsyncGenerator<ChatTypes>| Perform a chat completion request. Pass `history` to forward prior turns and `queryRewrite: true` (or an override object) to enable AI Search query rewriting.  
  
#### Custom Events

Event| Components| Detail| Description  
---|---|---|---  
`ready`| All| undefined| Fired when component is initialized  
`open`| search-modal| undefined| Fired when modal opens  
`close`| search-modal| undefined| Fired when modal closes  
`result-select`| search-modal| { result, index }| Fired when a search result is selected  
  
## CSS Variables Reference

Customize every aspect of the components using CSS custom properties. All variables use the `--search-snippet-` prefix. 

#### Colors

Variable| Default| Description  
---|---|---  
`--search-snippet-primary-color`| #2563eb| Primary brand color  
`--search-snippet-primary-hover`| #0f51df| Primary hover state  
`--search-snippet-background`| #ffffff| Main background color  
`--search-snippet-surface`| #f8f9fa| Surface/card background  
`--search-snippet-text-color`| #212529| Primary text color  
`--search-snippet-text-secondary`| #6c757d| Secondary/muted text  
`--search-snippet-result-icon-color`| var(--search-snippet-text-secondary)| Resting metadata-driven result icon color  
`--search-snippet-result-icon-active-color`| var(--search-snippet-primary-color)| Active, hovered, or focused result icon color  
`--search-snippet-text-description`| #495057| Search result description text (higher contrast)  
`--search-snippet-border-color`| #dee2e6| Border color  
`--search-snippet-hover-background`| #f1f3f5| Hover state background  
`--search-snippet-focus-ring`| #0066cc40| Focus ring color (with opacity)  
  
#### State Colors

Variable| Default| Description  
---|---|---  
`--search-snippet-error-color`| #dc3545| Error text color  
`--search-snippet-error-background`| #f8d7da| Error background color  
`--search-snippet-success-color`| #28a745| Success text color  
`--search-snippet-success-background`| #d4edda| Success background color  
`--search-snippet-warning-color`| #ffc107| Warning text color  
`--search-snippet-warning-background`| #fff3cd| Warning background color  
  
#### Message Colors (Chat)

Variable| Default| Description  
---|---|---  
`--search-snippet-user-message-bg`| #0066cc| User message bubble background  
`--search-snippet-user-message-text`| #ffffff| User message text color  
`--search-snippet-assistant-message-bg`| #f1f3f5| Assistant message bubble background  
`--search-snippet-assistant-message-text`| #212529| Assistant message text color  
`--search-snippet-system-message-bg`| #fff3cd| System message background  
`--search-snippet-system-message-text`| #856404| System message text color  
  
#### Typography

Variable| Default| Description  
---|---|---  
`--search-snippet-font-family`| -apple-system, BlinkMacSystemFont, ...| Primary font family stack  
`--search-snippet-font-family-mono`| 'SFMono-Regular', Consolas, ...| Monospace font family stack  
`--search-snippet-font-size-base`| 14px| Base font size  
`--search-snippet-font-size-sm`| 12px| Small font size  
`--search-snippet-font-size-lg`| 16px| Large font size  
`--search-snippet-font-size-xl`| 18px| Extra large font size  
`--search-snippet-line-height`| 1.5| Line height  
`--search-snippet-font-weight-normal`| 400| Normal font weight  
`--search-snippet-font-weight-medium`| 500| Medium font weight  
`--search-snippet-font-weight-bold`| 600| Bold font weight  
  
#### Spacing

Variable| Default| Description  
---|---|---  
`--search-snippet-spacing-xs`| 4px| Extra small spacing  
`--search-snippet-spacing-sm`| 8px| Small spacing  
`--search-snippet-spacing-md`| 12px| Medium spacing  
`--search-snippet-spacing-lg`| 16px| Large spacing  
`--search-snippet-spacing-xl`| 24px| Extra large spacing  
`--search-snippet-spacing-xxl`| 32px| Double extra large spacing  
  
#### Sizing

Variable| Default| Description  
---|---|---  
`--search-snippet-width`| 100%| Component width  
`--search-snippet-max-width`| 100%| Maximum width  
`--search-snippet-min-width`| 320px| Minimum width  
`--search-snippet-max-height`| 600px| Maximum height (results area)  
`--search-snippet-input-height`| 44px| Input field height  
`--search-snippet-button-height`| 36px| Button height  
`--search-snippet-icon-size`| 20px| Icon size  
`--search-snippet-result-icon-size`| 20px| Metadata-driven result icon size  
  
#### Border

Variable| Default| Description  
---|---|---  
`--search-snippet-border-width`| 1px| Border width  
`--search-snippet-border-radius`| 18px| Border radius  
  
#### Shadows

Variable| Default| Description  
---|---|---  
`--search-snippet-shadow-sm`| 0 1px 2px 0 rgba(0,0,0,0.05)| Small shadow  
`--search-snippet-shadow`| 0 2px 8px rgba(0,0,0,0.1)| Default shadow  
`--search-snippet-shadow-md`| 0 4px 12px rgba(0,0,0,0.15)| Medium shadow  
`--search-snippet-shadow-lg`| 0 8px 24px rgba(0,0,0,0.2)| Large shadow  
`--search-snippet-shadow-inner`| inset 0 2px 4px 0 rgba(0,0,0,0.06)| Inner shadow  
`--search-snippet-result-item-shadow`| 0 1px 2px 0 rgba(0,0,0,0.05)| Search result item hover shadow  
  
#### Animation & Transitions

Variable| Default| Description  
---|---|---  
`--search-snippet-transition-fast`| 150ms ease| Fast transition timing  
`--search-snippet-transition`| 200ms ease| Default transition timing  
`--search-snippet-transition-slow`| 300ms ease| Slow transition timing  
`--search-snippet-animation-duration`| 0.2s| Animation duration  
  
#### Z-Index Layers

Variable| Default| Description  
---|---|---  
`--search-snippet-z-dropdown`| 1000| Dropdown z-index  
`--search-snippet-z-modal`| 1050| Modal z-index  
`--search-snippet-z-popover`| 1060| Popover z-index  
`--search-snippet-z-tooltip`| 1070| Tooltip z-index  
  
#### Search Specific

Variable| Default| Description  
---|---|---  
`--search-snippet-icon-margin-left`| 6px| Search icon left margin  
`--search-snippet-button-min-border-radius`| 4px| Minimum button border radius  
  
#### Chat Bubble Specific

Variable| Default| Description  
---|---|---  
`--chat-bubble-button-size`| 60px| Bubble button size  
`--chat-bubble-button-radius`| 50%| Bubble button radius  
`--chat-bubble-button-bottom`| 20px| Button bottom position  
`--chat-bubble-button-right`| 20px| Button right position  
`--chat-bubble-position`| fixed| Bubble position type  
`--chat-bubble-button-shadow`| 0 8px 24px rgba(0,0,0,0.2)| Button shadow  
`--chat-bubble-window-shadow`| 0 8px 24px rgba(0,0,0,0.2)| Chat window shadow  
`--chat-bubble-button-icon-size`| 28px| Button icon size  
`--chat-bubble-button-icon-color`| white| Button icon color  
`--chat-bubble-button-z-index`| 9999| Button z-index  
  
#### Translations

##### Common keys

Key| Default| Notes  
---|---|---  
`placeholder`| "Search..."| Search input placeholder  
`chatPlaceholder`| "Type a message..."| Chat input placeholder  
`searchButtonLabel`| "Search"| Search button text / aria-label  
`sendButtonLabel`| "Send"| Chat send button text  
`emptyStateTitle`| "Start Searching"| Bar-variant empty state title  
`emptyStateDescription`| "Enter a query to search for results"| Bar-variant empty state description  
`noResultsTitle`| "No Results Found"| Bar-variant no-results title  
`noResultsDescription`| `No results found for "{query}"`| Bar-variant no-results description; supports {query}  
`resultsCount`| "Found {n} result"| Bar count, singular; supports {n}  
`resultsCountPlural`| "Found {n} results"| Bar count, plural; supports {n}  
`resultsCountOverflow`| "Showing {n} of {total} results"| Bar/modal truncated count; supports {n}, {total}  
`errorPrefix`| "Error:"| Bold prefix for error messages  
`missingApiUrlError`| "The api-url attribute is required. …"| Shown when api-url is missing  
`poweredBy`| "Powered by"| Branding prefix  
`poweredByLinkLabel`| "Cloudflare AI Search"| Branding link label  
`loadingMessages`| array of 10 English strings| Cycling loading phrases; provide the full array to replace  
  
##### Chat & modal only

Key| Default| Notes  
---|---|---  
`chatTitle`| "Chat"| Chat header title  
`chatEmptyTitle`| "Start a Conversation"| Chat empty state title  
`chatEmptyDescription`| "Send a message to begin chatting"| Chat empty state description  
`historyTitle`| "History"| Chat-page sidebar heading  
`newChatButton`| "New Chat"| Chat-page new-chat button / default session title  
`clearChatButton`| "Clear Chat"| Chat-page clear button  
`yesterday`| "Yesterday"| Session list relative date  
`navigateHint`| "Navigate"| Modal footer hint  
`selectHint`| "Select"| Modal footer hint  
`closeHint`| "Close"| Modal footer hint
