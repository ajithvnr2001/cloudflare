---
url: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/grafana-saas-oidc/
title: Grafana \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:15.800499+00:00
---

# Grafana · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/grafana-saas-oidc/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Access controls](https://developers.cloudflare.com/cloudflare-one/access-controls/)[Applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/)[Add web applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/)

  4. /[SaaS applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/)
  5. /Grafana



# Grafana

Last updated May 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/grafana-saas-oidc/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Add a SaaS application to Cloudflare One2\. Add a SSO provider to Grafana3\. Test the integration

This guide covers how to configure [Grafana ↗︎](https://grafana.com/docs/grafana/latest/setup-grafana/configure-security/configure-authentication/generic-oauth/) as an OIDC application in Cloudflare One.

## Prerequisites

  * An [identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/) configured in Cloudflare One
  * Admin access to a Grafana account



Note

You can also configure OIDC SSO for Grafana using a [configuration file ↗︎](https://grafana.com/docs/grafana/latest/setup-grafana/configure-security/configure-authentication/generic-oauth/#configure-generic-oauth-authentication-client-using-the-grafana-configuration-file) instead of using Grafana's user interface (UI), as documented in this guide.

## 1\. Add a SaaS application to Cloudflare One

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Access controls** > **Applications**.
  2. Select **Create new application**.
  3. Select **SaaS application**.
  4. For **Application** , select _Grafana_.
  5. For the authentication protocol, select **OIDC**.
  6. Select **Add application**.
  7. In **Scopes** , select the attributes that you want Access to send in the ID token.
  8. In **Redirect URLs** , enter `https://<your-grafana-domain>/login/generic_oauth`.
  9. (Optional) Enable [Proof of Key Exchange (PKCE) ↗︎](https://www.oauth.com/oauth2-servers/pkce/) if the protocol is supported by your IdP. PKCE will be performed on all login attempts.
  10. Copy the **Client secret** , **Client ID** , **Token endpoint** , and **Authorization endpoint**.
  11. Configure [Access policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) for the application.
  12. (Optional) In **Experience settings** , configure [App Launcher settings](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/app-launcher/) by turning on **Enable App in App Launcher** and, in **App Launcher URL** , entering `https://<your-grafana-domain>/login`.
  13. Save the application.



## 2\. Add a SSO provider to Grafana

  1. In Grafana, select the **menu** icon > **Administration** > **Authentication** > **Generic OAuth**.
  2. (Optional) For **Display name** , enter a new display name (for example, `Cloudflare Access`). Users will select **Sign in with (display name)** when signing in via SSO.
  3. Fill in the following fields: 
     * **Client Id** : Client ID from application configuration in Cloudflare One
     * **Client secret** : Client secret from application configuration in Cloudflare One
     * **Scopes** : Delete `user:email` and enter the scopes configured in Cloudflare One
     * **Auth URL** : Authorization endpoint from application configuration in Cloudflare One
     * **Token URL** : Token endpoint from application configuration in Cloudflare One
  4. Select **Save**.



## 3\. Test the integration

Log out, then select **Sign in with (display name)**. You will be redirected to the Cloudflare Access login screen and prompted to sign in with your identity provider.

[PreviousGoogle Workspace](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/google-workspace-saas/)[NextGrafana Cloud](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/grafana-cloud-saas-oidc/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/access-controls/applications/http-apps/saas-apps/grafana-saas-oidc.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
