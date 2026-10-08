---
url: https://developers.cloudflare.com/cloudflare-one/faq/authentication-faq/
title: Identity FAQ \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:45.805014+00:00
---

# Identity FAQ · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/faq/authentication-faq/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /[Faq](https://developers.cloudflare.com/cloudflare-one/faq/)
  4. /Authentication Faq



# Identity FAQ

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/faq/authentication-faq/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCan Access work with multiple identity providers at the same time?What if the identity provider my team uses is not listed?How do end users log out of an application protected by Access?

[❮ Back to FAQ](https://developers.cloudflare.com/cloudflare-one/faq/)

## Can Access work with multiple identity providers at the same time?

Yes. Your team can simultaneously use multiple providers, reducing friction when working with partners or contractors. Get started by adding your preferred identity providers as login methods in Zero Trust. Then, when securing a new application behind Access, you'll be able to choose which providers you want your users to log in with to reach that application.

## What if the identity provider my team uses is not listed?

You can add your preferred identity providers to Cloudflare Access even if you do not see them listed in Zero Trust, as long as these providers support SAML 2.0 or [OpenID Connect (OIDC)](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-oidc/).

## How do end users log out of an application protected by Access?

Access provides a URL that will end a user's current session.

To force log out of an Access application, go to:

`<your-application-domain>/cdn-cgi/access/logout`

To log out of an App Launcher session, go to:

`<your-team-name>.cloudflareaccess.com/cdn-cgi/access/logout`

For more information, refer to our [session management page](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/session-management/#log-out-as-a-user).

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/faq/authentication-faq.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
