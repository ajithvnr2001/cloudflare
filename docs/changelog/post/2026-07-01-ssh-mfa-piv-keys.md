---
url: https://developers.cloudflare.com/changelog/post/2026-07-01-ssh-mfa-piv-keys/
title: Independent MFA for infrastructure applications \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:35.613624+00:00
---

# Independent MFA for infrastructure applications · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-01-ssh-mfa-piv-keys/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 1, 2026

## Independent MFA for infrastructure applications

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Access for Infrastructure](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/) now supports independent multi-factor authentication (MFA) for SSH connections using YubiKey PIV keys. This adds a hardware-backed second factor to SSH access, ensuring that a compromised device session alone is not sufficient to reach your servers.

With per-application and per-policy configuration, you can enforce PIV key authentication for sensitive usernames (for example, `root`) while applying different requirements for other usernames. You can also set an MFA session duration to control how often users must re-authenticate.

#### Enrollment

Users enroll their YubiKey PIV key through the [App Launcher](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/app-launcher/). For enrollment instructions and SSH client setup, refer to [Enroll a PIV key for infrastructure apps](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/independent-mfa/#enroll-a-piv-key-for-infrastructure-apps).

#### Configuration

For setup instructions, refer to [Enforce MFA for infrastructure applications](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/mfa-requirements/#infrastructure-applications).
