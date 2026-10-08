---
url: https://developers.cloudflare.com/changelog/post/2025-05-08-open-attachments-with-browser-isolation/
title: Open email attachments with Browser Isolation \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:11.772665+00:00
---

# Open email attachments with Browser Isolation · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-05-08-open-attachments-with-browser-isolation/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 15, 2025

## Open email attachments with Browser Isolation

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-05-08-open-attachments-with-browser-isolation/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now safely open email attachments to view and investigate them.

What this means is that messages now have a **Attachments** section. Here, you can view processed attachments and their classifications (for example, _Malicious_ , _Suspicious_ , _Encrypted_). Next to each attachment, a **Browser Isolation** icon allows your team to safely open the file in a **clientless, isolated browser** with no risk to the analyst or your environment.

![Attachment-RBI](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=517,height=155,format=webp/_astro/Attachment-RBI.U9Dp8dJO.png)

To use this feature, you must:

  * Turn on **Allow users to open a remote browser without the device client** in your Zero Trust settings.
  * Have **Browser Isolation (BISO)** seats assigned.



For more details, refer to our [setup guide](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/).

Some attachment types may not render in Browser Isolation. If there is a file type that you would like to be opened with Browser Isolation, reach out to your Cloudflare contact.

This feature is available across these Email security packages:

  * **Advantage**
  * **Enterprise**
  * **Enterprise + PhishGuard**


