---
url: https://developers.cloudflare.com/changelog/post/2026-03-01-rdp-clipboard-controls/
title: Clipboard controls for browser-based RDP \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:42.968034+00:00
---

# Clipboard controls for browser-based RDP · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-01-rdp-clipboard-controls/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 1, 2026

## Clipboard controls for browser-based RDP

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now configure clipboard controls for browser-based RDP with Cloudflare Access. Clipboard controls allow administrators to restrict whether users can copy or paste text between their local machine and the remote Windows server.

![Enable users to copy and paste content from their local machine to remote RDP sessions in the Cloudflare One dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2000,height=546,format=webp/_astro/rdp-clipboard-controls.B0ZmliDb.png)

This feature is useful for organizations that support bring-your-own-device (BYOD) policies or third-party contractors using unmanaged devices. By restricting clipboard access, you can prevent sensitive data from being transferred out of the remote session to a user's personal device.

#### Configuration options

Clipboard controls are configured per policy within your Access application. For each policy, you can independently allow or deny:

  * **Copy from local client to remote RDP session** — Users can copy/paste text from their local machine into the browser-based RDP session.
  * **Copy from remote RDP session to local client** — Users can copy/paste text from the browser-based RDP session to their local machine.



By default, both directions are denied for new policies. For existing Access applications created before this feature was available, clipboard access remains enabled to preserve backwards compatibility.

When a user attempts a restricted clipboard action, the clipboard content is replaced with an error message informing them that the action is not allowed.

For more information, refer to [Clipboard controls for browser-based RDP](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/#clipboard-controls).
