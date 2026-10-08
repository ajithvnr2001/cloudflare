---
url: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/lts-releases/
title: Download Cloudflare One Client LTS releases \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:02.745059+00:00
---

# Download Cloudflare One Client LTS releases · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/lts-releases/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Team and resources[Devices](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/)[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

  4. /[Downloads](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/)
  5. /LTS releases



# Download Cloudflare One Client LTS releases

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/lts-releases/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWindowsmacOSLinux

Long-Term Support (LTS) releases are stable releases that are guaranteed to continue receiving security bug fixes for at least 12 months or 90 days after the next LTS release, whichever is greater.

For more details on Cloudflare One Client support timelines and end-of-life (EOL) policies, refer to the [Support lifecycle](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/support-lifecycle/) page.

Note

No LTS releases are currently available, as Cloudflare is still rolling out our new LTS release process. When a stable release is declared an LTS release, it will be listed on this page and announced in the [Cloudflare One Client changelog](https://developers.cloudflare.com/cloudflare-one/changelog/cloudflare-one-client/).

## Windows

**OS version** | Windows 10 LTSC, Windows 11, Windows 365 Cloud PC running Windows 11  
---|---  
**Processor** | AMD64 / x86-64 or ARM64 / AArch64  
**.NET Framework version** | 4.7.2 or later  
**vCPU** | 3 minimum, 4 recommended  
**RAM** | 4 GB minimum, 8 GB recommended  
**Disk space** | 250 MiB minimum, 500 MiB recommended  
**Network interface type** | Wi-Fi or LAN  
**MTU** | 1381 bytes recommended 1  
  
## Footnotes

  1. Minimum 1281 bytes with [Path MTU Discovery](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/) ↩




## macOS

**OS version** | Sequoia 15.1+ (15.0.x is not supported), Tahoe 26.0+, Golden Gate 27.0+  
---|---  
**Processor** | Intel or M series  
**CPU cores** | 3 minimum, 4 recommended  
**RAM** | 8 GB minimum  
**Disk space** | 1 GiB minimum  
**Network interface type** | Wi-Fi or LAN  
**MTU** | 1381 bytes recommended 1  
  
All supported Mac models meet the CPU and RAM requirements, so only disk space may be a constraint.

## Footnotes

  1. Minimum 1281 bytes with [Path MTU Discovery](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/) ↩




## Linux

**OS version** | RHEL 9 1, RHEL 10, Debian 12, Debian 13, Fedora 43, Fedora 44, Ubuntu 22.04 LTS, Ubuntu 24.04 LTS, Ubuntu 26.04 LTS  
---|---  
**Processor** | AMD64 / x86-64 or ARM64 / AArch64  
**vCPU** | 3 minimum, 4 recommended  
**RAM without a desktop** | 1 GB minimum, 2 GB recommended (for example, Ubuntu Server)  
**RAM with a desktop** | 4 GB minimum, 8 GB recommended (for example, Ubuntu GNOME)  
**Disk space** | 250 MiB minimum, 500 MiB recommended  
**Network interface type** | Wi-Fi or LAN  
**MTU** | 1381 bytes recommended 2  
  
## Footnotes

  1. On RHEL 9 and later, enable the [Extra Packages for Enterprise Linux (EPEL) ↗︎](https://docs.fedoraproject.org/en-US/epel/) repository (`sudo dnf install epel-release`) before installing `cloudflare-warp`. EPEL provides dependencies required by the client UI. ↩

  2. Minimum 1281 bytes with [Path MTU Discovery](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/) ↩




[PreviousStable releases](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/)[NextBeta releases](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/lts-releases.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
