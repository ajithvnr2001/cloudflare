---
url: https://developers.cloudflare.com/changelog/post/2026-04-15-independent-mfa/
title: Independent MFA for Access applications \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:47.064078+00:00
---

# Independent MFA for Access applications · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-15-independent-mfa/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 15, 2026

## Independent MFA for Access applications

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-15-independent-mfa/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Access now supports independent multi-factor authentication (MFA), allowing you to enforce MFA requirements without relying on your identity provider (IdP). With per-application and per-policy configuration, you can enforce stricter authentication methods like hardware security keys on sensitive applications without requiring them across your entire organization. This reduces the risk of MFA fatigue for your broader user population while adding additional security where it matters most.

This feature also addresses common gaps in IdP-based MFA, such as inconsistent MFA policies across different identity providers or the need for additional security layers beyond what the IdP provides.

Independent MFA supports the following authenticator types:

  * **Authenticator application** — Time-based one-time passwords (TOTP) using apps like Google Authenticator, Microsoft Authenticator, or Authy.
  * **Security key** — Hardware security keys such as YubiKeys.
  * **Biometrics** — Built-in device authenticators including Apple Touch ID, Apple Face ID, and Windows Hello.



Note

Infrastructure applications do not yet support independent MFA.

#### Configuration levels

You can configure MFA requirements at three levels:

Level | Description  
---|---  
**Organization** | Enforce MFA by default for all applications in your account.  
**Application** | Require or turn off MFA for a specific application.  
**Policy** | Require or turn off MFA for users who match a specific policy.  
  
Settings at lower levels (policy) override settings at higher levels (organization), giving you granular control over MFA enforcement.

#### User enrollment

Users enroll their authenticators through the [App Launcher](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/app-launcher/). To help with onboarding, administrators can share a direct enrollment link: `<your-team-name>.cloudflareaccess.com/AddMfaDevice`.

To get started with Independent MFA, refer to [Independent MFA](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/independent-mfa/).
