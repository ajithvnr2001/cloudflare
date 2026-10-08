---
url: https://developers.cloudflare.com/tunnel/downloads/
title: Downloads \u00b7 Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:02.645485+00:00
---

# Downloads · Cloudflare Docs

> Source: https://developers.cloudflare.com/tunnel/downloads/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)
  3. /Downloads



# Downloads

Last updated Sep 11, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/tunnel/downloads/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewGitHub repositoryLatest release Linux macOS Windows DockerDeprecated releases

Cloudflare Tunnel requires the installation of a lightweight daemon, `cloudflared`, to connect your infrastructure to Cloudflare. If you are [creating a tunnel through the dashboard](https://developers.cloudflare.com/tunnel/get-started/), you can simply copy-paste the installation command shown in the dashboard.

To download and install `cloudflared` manually, use one of the following links.

## GitHub repository

`cloudflared` is an [open source project ↗︎](https://github.com/cloudflare/cloudflared) maintained by Cloudflare.

  * [All releases ↗︎](https://github.com/cloudflare/cloudflared/releases)

  * [Release notes ↗︎](https://github.com/cloudflare/cloudflared/blob/master/RELEASE_NOTES)




## Latest release

### Linux

You can download and install `cloudflared` via the [Cloudflare Package Repository ↗︎](https://pkg.cloudflare.com/).

Alternatively, download the latest release directly:

Type | amd64 / x86-64 | x86 (32-bit) | ARM | ARM64  
---|---|---|---|---  
Binary | [Download ↗︎](https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64) | [Download ↗︎](https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-386) | [Download ↗︎](https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm) | [Download ↗︎](https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64)  
.deb | [Download ↗︎](https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb) | [Download ↗︎](https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-386.deb) | [Download ↗︎](https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm.deb) | [Download ↗︎](https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64.deb)  
.rpm | [Download ↗︎](https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-x86_64.rpm) | [Download ↗︎](https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-386.rpm) | [Download ↗︎](https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm.rpm) | [Download ↗︎](https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-aarch64.rpm)  
  
### macOS

Download and install `cloudflared` via Homebrew:
    
    
    brew install cloudflared

Alternatively, download the [latest Darwin arm64 release ↗︎](https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-darwin-arm64.tgz) or [latest Darwin amd64 release ↗︎](https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-darwin-amd64.tgz) directly.

### Windows

Download the latest release from [GitHub ↗︎](https://github.com/cloudflare/cloudflared/releases/latest):

Type | 32-bit | 64-bit  
---|---|---  
Executable | [Download ↗︎](https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-386.exe) | [Download ↗︎](https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe)  
MSI | [Download ↗︎](https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-386.msi) | [Download ↗︎](https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.msi)  
  
Note

Instances of `cloudflared` do not automatically update on Windows. You will need to perform manual updates.

### Docker

A Docker image of `cloudflared` is [available on DockerHub ↗︎](https://hub.docker.com/r/cloudflare/cloudflared).

## Deprecated releases

Cloudflare supports versions of `cloudflared` that are within one year of the most recent release. Breaking changes unrelated to feature availability may be introduced that will impact versions released more than one year ago. For example, as of January 2023 Cloudflare will support `cloudflared` version 2023.1.1 to cloudflared 2022.1.1.

To update `cloudflared`, refer to [Update cloudflared](https://developers.cloudflare.com/tunnel/guides/update-cloudflared/).

[PreviousIntegrations](https://developers.cloudflare.com/tunnel/integrations/)[NextOverview](https://developers.cloudflare.com/tunnel/troubleshooting/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/tunnel/downloads/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
