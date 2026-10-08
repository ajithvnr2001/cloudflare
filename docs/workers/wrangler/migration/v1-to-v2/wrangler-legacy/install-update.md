---
url: https://developers.cloudflare.com/workers/wrangler/migration/v1-to-v2/wrangler-legacy/install-update/
title: Install / Update \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:18:13.208569+00:00
---

# Install / Update · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/wrangler/migration/v1-to-v2/wrangler-legacy/install-update/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Wrangler](https://developers.cloudflare.com/workers/wrangler/)MigrationsMigrate from Wrangler v1 to v2

  4. /[Wrangler v1 (legacy)](https://developers.cloudflare.com/workers/wrangler/migration/v1-to-v2/wrangler-legacy/)
  5. /Install / Update



# Install / Update

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/wrangler/migration/v1-to-v2/wrangler-legacy/install-update/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInstall Install with npm Install with cargo Manual installUpdate Update with npm Update with cargo

Caution

This page is for Wrangler v1, which has been deprecated. [Learn how to update to the latest version of Wrangler](https://developers.cloudflare.com/workers/wrangler/migration/v1-to-v2/).

## Install

### Install with `npm`
    
    
    npm i @cloudflare/wrangler -g

EACCESS error

You may have already installed npm. It is possible that an `EACCES` error may be thrown while installing Wrangler. This is related to how many systems install the npm binary. It is recommended that you reinstall npm using a Node version manager like [nvm ↗︎](https://github.com/nvm-sh/nvm#installing-and-updating) or [Volta ↗︎](https://volta.sh/).

### Install with `cargo`

Assuming you have Rust’s package manager, [Cargo ↗︎](https://github.com/rust-lang/cargo), installed, run:
    
    
    cargo install wrangler

Otherwise, to install Cargo, you must first install rustup. On Linux and macOS systems, `rustup` can be installed as follows:
    
    
    curl https://sh.rustup.rs -sSf | sh

Additional installation methods are available [on the Rust site ↗︎](https://forge.rust-lang.org/other-installation-methods.html).

Windows users will need to install Perl as a dependency for `openssl-sys` — [Strawberry Perl ↗︎](https://www.perl.org/get.html) is recommended.

After Cargo is installed, you may now install Wrangler:
    
    
    cargo install wrangler

Customize OpenSSL

By default, a copy of OpenSSL is included to make things easier during installation, but this can make the binary size larger. If you want to use your system's OpenSSL installation, provide the feature flag `sys-openssl` when running install:
    
    
    cargo install wrangler --features sys-openssl

### Manual install

  1. Download the binary tarball for your platform from the [releases page ↗︎](https://github.com/cloudflare/wrangler-legacy/releases). You do not need the `wranglerjs-*.tar.gz` download – Wrangler will install that for you.

  2. Unpack the tarball and place the Wrangler binary somewhere on your `PATH`, preferably `/usr/local/bin` for Linux/macOS or `Program Files` for Windows.




## Update

To update [Wrangler ↗︎](https://github.com/cloudflare/wrangler-legacy), run one of the following:

### Update with `npm`
    
    
    npm update -g @cloudflare/wrangler

### Update with `cargo`
    
    
    cargo install wrangler --force

[PreviousOverview](https://developers.cloudflare.com/workers/wrangler/migration/v1-to-v2/wrangler-legacy/)[NextAuthentication](https://developers.cloudflare.com/workers/wrangler/migration/v1-to-v2/wrangler-legacy/authentication/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/wrangler/migration/v1-to-v2/wrangler-legacy/install-update.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
