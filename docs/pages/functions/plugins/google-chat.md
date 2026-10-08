---
url: https://developers.cloudflare.com/pages/functions/plugins/google-chat/
title: Google Chat \u00b7 Cloudflare Pages docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:33.303130+00:00
---

# Google Chat · Cloudflare Pages docs

> Source: https://developers.cloudflare.com/pages/functions/plugins/google-chat/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Pages](https://developers.cloudflare.com/pages/)
  3. /…

[Functions](https://developers.cloudflare.com/pages/functions/)

  4. /[Pages Plugins](https://developers.cloudflare.com/pages/functions/plugins/)
  5. /Google Chat



# Google Chat

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/pages/functions/plugins/google-chat/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInstallationUsage API

The Google Chat Pages Plugin creates a Google Chat bot which can respond to messages. It also includes an API for interacting with Google Chat (for example, for creating messages) without the need for user input. This API is useful for situations such as alerts.

## Installation

npmyarnpnpmbun
    
    
    npm i @cloudflare/pages-plugin-google-chat
    
    
    yarn add @cloudflare/pages-plugin-google-chat
    
    
    pnpm add @cloudflare/pages-plugin-google-chat
    
    
    bun add @cloudflare/pages-plugin-google-chat

## Usage
    
    
    import googleChatPlugin from "@cloudflare/pages-plugin-google-chat";
    
    export const onRequest: PagesFunction = googleChatPlugin(async (message) => {
    	if (message.text.includes("ping")) {
    		return { text: "pong" };
    	}
    
    	return { text: "Sorry, I could not understand your message." };
    });

The Plugin takes a function, which in turn takes an incoming message, and returns a `Promise` of a response message (or `void` if there should not be any response).

The Plugin only exposes a single route, which is the URL you should set in the Google Cloud Console when creating the bot.

![Google Cloud Console's Connection Settings for the Google Chat API showing 'App URL' selected and 'https://example.com/google-chat' entered into the 'App URL' text input.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1122,height=476,format=webp/_astro/google-chat.PImk30WB.png)

### API

The Google Chat API can be called directly using the `GoogleChatAPI` class:
    
    
    import { GoogleChatAPI } from "@cloudflare/pages-plugin-google-chat/api";
    
    export const onRequest: PagesFunction = () => {
    	// Initialize a GoogleChatAPI with your service account's credentials
    	const googleChat = new GoogleChatAPI({
    		credentials: {
    			client_email: "SERVICE_ACCOUNT_EMAIL_ADDRESS",
    			private_key: "SERVICE_ACCOUNT_PRIVATE_KEY",
    		},
    	});
    
    	// Post a message
    	// https://developers.google.com/chat/api/reference/rest/v1/spaces.messages/create
    	const message = await googleChat.createMessage(
    		{ parent: "spaces/AAAAAAAAAAA" },
    		undefined,
    		{
    			text: "I'm an alert!",
    		},
    	);
    
    	return new Response("Alert sent.");
    };

We recommend storing your service account's credentials in KV rather than in plain text as above.

The following functions are available on a `GoogleChatAPI` instance. Each take up to three arguments: an object of path parameters, an object of query parameters, and an object of the request body; as described in the [Google Chat API's documentation ↗︎](https://developers.google.com/chat/api/reference/rest).

  * [`downloadMedia` ↗︎](https://developers.google.com/chat/api/reference/rest/v1/media/download)
  * [`getSpace` ↗︎](https://developers.google.com/chat/api/reference/rest/v1/spaces/get)
  * [`listSpaces` ↗︎](https://developers.google.com/chat/api/reference/rest/v1/spaces/list)
  * [`getMember` ↗︎](https://developers.google.com/chat/api/reference/rest/v1/spaces.members/get)
  * [`listMembers` ↗︎](https://developers.google.com/chat/api/reference/rest/v1/spaces.members/list)
  * [`createMessage` ↗︎](https://developers.google.com/chat/api/reference/rest/v1/spaces.messages/create)
  * [`deleteMessage` ↗︎](https://developers.google.com/chat/api/reference/rest/v1/spaces.messages/delete)
  * [`getMessage` ↗︎](https://developers.google.com/chat/api/reference/rest/v1/spaces.messages/get)
  * [`updateMessage` ↗︎](https://developers.google.com/chat/api/reference/rest/v1/spaces.messages/update)
  * [`getAttachment` ↗︎](https://developers.google.com/chat/api/reference/rest/v1/spaces.messages.attachments/get)



[PreviousCloudflare Access](https://developers.cloudflare.com/pages/functions/plugins/cloudflare-access/)[NextGraphQL](https://developers.cloudflare.com/pages/functions/plugins/graphql/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/pages/functions/plugins/google-chat.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
