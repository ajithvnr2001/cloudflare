---
url: https://developers.cloudflare.com/ssl/keyless-ssl/upgrading-your-key-server/
title: Upgrade your key server \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:43.079542+00:00
---

# Upgrade your key server · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/keyless-ssl/upgrading-your-key-server/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /[Keyless SSL](https://developers.cloudflare.com/ssl/keyless-ssl/)
  4. /Upgrade your key server



# Upgrade your key server

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/keyless-ssl/upgrading-your-key-server/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Periodically, you may need to update your key server when using Cloudflare's Keyless SSL.

To upgrade your key server:

  1. Back up the contents of `/etc/keyless`.
  2. Update your OS’ package listings, for example, `apt-get update` or `yum update`.
  3. Upgrade the gokeyless server:
  4. Debian/Ubuntu: `apt-get upgrade gokeyless`
  5. RHEL/CentOS: `yum install gokeyless`
  6. Restart the keyless instance:
  7. systemd: `service gokeyless restart`
  8. upstart/sysvinit: `/etc/init.d/gokeyless restart`
  9. Confirm that HTTPS connections are working as expected.



Caution

If you are running a [high availability configuration](https://developers.cloudflare.com/ssl/keyless-ssl/reference/high-availability/), upgrade one server at a time as new TLS connections will fail to terminate at Cloudflare's global network without a functioning key server.

[PreviousSoftHSMv2](https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/softhsmv2/)[NextHigh availability](https://developers.cloudflare.com/ssl/keyless-ssl/reference/high-availability/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/keyless-ssl/upgrading-your-key-server.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
