---
url: https://developers.cloudflare.com/changelog/post/2026-07-07-rdp-file-transfer-beta/
title: File transfer controls for browser-based RDP (beta) \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:35.439425+00:00
---

# File transfer controls for browser-based RDP (beta) · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-07-rdp-file-transfer-beta/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 7, 2026

## File transfer controls for browser-based RDP (beta)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now configure file transfer controls for browser-based RDP with Cloudflare Access, allowing you to restrict whether users can upload or download files between their local machine and the remote Windows server.

![File transfer connection settings in the Access policy configuration.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1356,height=692,format=webp/_astro/file-transfer-policy-control.CiSEa5rr.png)

This feature is useful for organizations that support bring-your-own-device (BYOD) policies or third-party contractors using unmanaged devices. By restricting file transfers, you can prevent sensitive data from being moved out of the remote session to a user's personal device.

#### Configuration options

File transfer controls are configured per policy within your Access application, alongside existing [text clipboard controls](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/#connection-settings). For each policy, you can select one of the following options:

  * **Client to remote RDP session allowed** — Users can upload files from their local machine into the browser-based RDP session.
  * **Remote RDP session to client allowed** — Users can download files from the browser-based RDP session to their local machine.
  * **Both directions allowed** — Users can upload and download files between their local machine and the browser-based RDP session.
  * **Disable copying/pasting** — Users are not allowed to transfer files between their local machine and the browser-based RDP session.



By default, file transfer is denied for new policies. For existing Access applications created before this feature was available, file transfer remains denied.

#### How it works

To upload, drag files into the browser window or select the settings gear icon on the left side of the RDP session. To download, copy a file in the remote session and select the settings gear to download it, download multiple files as a zip, or print PDFs to a local printer.

![The clipboard side panel showing files available for transfer.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=812,height=532,format=webp/_astro/clipboard-side-panel.Us2RfXfs.png)![A remote document ready for download or local printing.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=770,height=442,format=webp/_astro/remote-doc-ready-for-download-or-print-local.Dcm5hrGD.png)

This feature is in beta and available on all Zero Trust plans. For more information, refer to [File transfer for browser-based RDP](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/#transfer-files).
