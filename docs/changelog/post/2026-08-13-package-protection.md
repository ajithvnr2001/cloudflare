---
url: https://developers.cloudflare.com/changelog/post/2026-08-13-package-protection/
title: Detect and control software package downloads with package registry security \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:09.238241+00:00
---

# Detect and control software package downloads with package registry security · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-13-package-protection/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 13, 2026

## Detect and control software package downloads with package registry security

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-13-package-protection/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Gateway can now detect software package downloads and give you policy control over supply chain traffic. When a developer or CI/CD pipeline downloads a package through Gateway, the proxy identifies the registry protocol from the request URL and extracts the package ecosystem, name, version, and namespace. You can then write [HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/) using `pkg.*` selectors to allow or block package downloads.

#### Supported ecosystems

Gateway detects package downloads for the following ecosystems:

Ecosystem | Namespace  
---|---  
npm | Scope (for example, `@babel`)  
PyPI | \--  
RubyGems | \--  
Cargo | \--  
Go | Module path  
Maven | Group ID  
NuGet | \--  
  
#### Selectors

In the dashboard, select **Package Ecosystem** to access the package registry selectors. After selecting a single ecosystem, nested fields for package name, version, and namespace become available. Five `pkg.*` selectors are available for HTTP policies with the Allow and Block actions:

Selector | Description  
---|---  
`pkg.ecosystem` | The package ecosystem detected from the request URL.  
`pkg.name` | The package name extracted from the download URL.  
`pkg.version` | The package version, with support for ecosystem-aware comparison operators.  
`pkg.namespace` | The package namespace, when the ecosystem supports one.  
`pkg.purl` | The [Package URL (PURL) ↗︎](https://github.com/package-url/purl-spec) derived from the detected coordinates. Available in the API only.  
  
Detection is based on the registry protocol rather than the hostname, so it works the same way whether traffic goes to a public registry, a corporate proxy such as Artifactory or Nexus, or a self-hosted mirror.

Package registry security requires [TLS decryption](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/tls-decryption/) to be turned on.

For more information, refer to [Package registry security](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/package-registry-security/).
