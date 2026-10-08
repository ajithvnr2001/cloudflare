---
url: https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/encrypted-dns-browsers/
title: Configure DoH on your browser \u00b7 Cloudflare 1.1.1.1 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:03.273498+00:00
---

# Configure DoH on your browser · Cloudflare 1.1.1.1 docs

> Source: https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/encrypted-dns-browsers/

  1. [Home](https://developers.cloudflare.com/)
  2. /[1.1.1.1 (DNS Resolver)](https://developers.cloudflare.com/1.1.1.1/)
  3. /…

[Encryption](https://developers.cloudflare.com/1.1.1.1/encryption/)

  4. /[DNS over HTTPS](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/)
  5. /Configure DoH on your browser



# Configure DoH on your browser

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/encrypted-dns-browsers/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMozilla FirefoxGoogle ChromeMicrosoft EdgeBraveCheck if the browser is configured correctly

Several browsers support DNS over HTTPS (DoH), which encrypts your DNS queries to protect them from monitoring and tampering.

Some browsers might already have this setting enabled.

Note

[1.1.1.1 for Families](https://developers.cloudflare.com/1.1.1.1/setup/#1111-for-families) provides additional filtering to block malware, phishing, or adult content. To use it, follow the steps below but, instead of choosing the default 1.1.1.1 option, refer to [Set up](https://developers.cloudflare.com/1.1.1.1/setup/#dns-over-https-doh) and specify the URL you want to use.

## Mozilla Firefox

  1. Select the menu button > **Settings**.
  2. In the **Privacy & Security** menu, scroll down to the **Enable secure DNS using:** section.
  3. Select **Increased Protection** or **Max Protection**. By default, it will use the **Cloudflare** provider.
  4. If this is not the case, select **Cloudflare** in the **Choose Provider** dropdown.



## Google Chrome

  1. Select the three-dot menu in your browser > **Settings**.
  2. Select **Privacy and security** > **Security**.
  3. Scroll down and enable **Use secure DNS**.
  4. Select the **With** option, and from the drop-down menu choose _Cloudflare (1.1.1.1)_.



## Microsoft Edge

  1. Select the three-dot menu in your browser > **Settings**.
  2. Select **Privacy, Search, and Services** , and scroll down to **Security**.
  3. Enable **Use secure DNS**.
  4. Select **Choose a service provider**.
  5. Select the **Enter custom provider** drop-down menu and choose _Cloudflare (1.1.1.1)_.



## Brave

  1. Select the menu button in your browser > **Settings**.
  2. Select **Privacy and security** > **Security**.
  3. Under **Advanced** , enable **Use secure DNS**.
  4. From the **Select DNS provider** drop-down menu, choose _Cloudflare (1.1.1.1)_.



## Check if the browser is configured correctly

Visit [1.1.1.1 help page ↗︎](https://one.one.one.one/help) and check if `Using DNS over HTTPS (DoH)` shows `Yes`.

[PreviousUsing JSON](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/make-api-requests/dns-json/)[NextConnect to 1.1.1.1 using DoH clients](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/dns-over-https-client/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/1.1.1.1/encryption/dns-over-https/encrypted-dns-browsers.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
