---
url: https://developers.cloudflare.com/changelog/post/2025-10-01-new-file-type-support/
title: Expanded File Type Controls for Executables and Disk Images \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:25.170428+00:00
---

# Expanded File Type Controls for Executables and Disk Images · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-10-01-new-file-type-support/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 1, 2025

## Expanded File Type Controls for Executables and Disk Images

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-01-new-file-type-support/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now enhance your security posture by blocking additional application installer and disk image file types with Cloudflare Gateway. Preventing the download of unauthorized software packages is a critical step in securing endpoints from malware and unwanted applications.

We have expanded Gateway's file type controls to include:

  * Apple Disk Image (dmg)
  * Microsoft Software Installer (msix, appx)
  * Apple Software Package (pkg)



You can find these new options within the [_Upload File Types_ and _Download File Types_ selectors](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#download-and-upload-file-types) when creating or editing an HTTP policy. The file types are categorized as follows:

  * **System** : _Apple Disk Image (dmg)_
  * **Executable** : _Microsoft Software Installer (msix)_ , _Microsoft Software Installer (appx)_ , _Apple Software Package (pkg)_



To ensure these file types are blocked effectively, please note the following behaviors:

  * DMG: Due to their file structure, DMG files are blocked at the very end of the transfer. A user's download may appear to progress but will fail at the last moment, preventing the browser from saving the file.
  * MSIX: To comprehensively block Microsoft Software Installers, you should also include the file type _Unscannable_. MSIX files larger than 100 MB are identified as Unscannable ZIP files during inspection.



To get started, go to your HTTP policies in Zero Trust. For a full list of file types, refer to [supported file types](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#supported-file-types).
