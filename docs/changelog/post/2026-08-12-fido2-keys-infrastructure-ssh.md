---
url: https://developers.cloudflare.com/changelog/post/2026-08-12-fido2-keys-infrastructure-ssh/
title: Independent MFA supports FIDO2 for infrastructure applications \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:07.972466+00:00
---

# Independent MFA supports FIDO2 for infrastructure applications · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-12-fido2-keys-infrastructure-ssh/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 12, 2026

## Independent MFA supports FIDO2 for infrastructure applications

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-12-fido2-keys-infrastructure-ssh/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Infrastructure](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/) applications support independent multi-factor authentication (MFA) with FIDO2 keys. You can allow `ssh_fido2_key`, `piv_key`, or both in application-level and policy-level MFA settings.

Users enroll FIDO2 keys through the App Launcher and connect with the generated SSH identity. FIDO2 keys for SSH are separate from browser-based WebAuthn security keys and Personal Identity Verification (PIV) keys.

For setup instructions, refer to [Enroll a FIDO2 key for infrastructure apps](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/independent-mfa/#enroll-a-fido2-key-for-infrastructure-apps) and [Configure MFA for infrastructure applications](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/mfa-requirements/#infrastructure-applications).
