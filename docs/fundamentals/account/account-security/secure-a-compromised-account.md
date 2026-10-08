---
url: https://developers.cloudflare.com/fundamentals/account/account-security/secure-a-compromised-account/
title: Secure compromised account \u00b7 Cloudflare Fundamentals docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:20.050520+00:00
---

# Secure compromised account · Cloudflare Fundamentals docs

> Source: https://developers.cloudflare.com/fundamentals/account/account-security/secure-a-compromised-account/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)
  3. /…

Accounts

  4. /Account security
  5. /Secure compromised account



# Secure compromised account

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/fundamentals/account/account-security/secure-a-compromised-account/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewStep 1 - Change your passwordStep 2 - Revoke active account sessionsStep 3 - Enable Two-Factor Authentication (2FA)Step 4 - Change API keys and tokens API keys API tokensStep 5 - Review the audit log

If you observe suspicious activity within your Cloudflare account, secure your account with these steps.

## Step 1 - Change your password

For more guidance on changing your password, refer to [Change email address or password](https://developers.cloudflare.com/fundamentals/user-profiles/change-password-or-email/).

## Step 2 - Revoke active account sessions

When there is more than one active session associated with your email account, you can revoke any session that is not the current session.

To revoke a session:

  1. Log in to the Cloudflare dashboard.

[ Go to **Account home** ↗ ](https://dash.cloudflare.com/?to=/:account/home)
  2. Go to **My Profile** > **Sessions**.

  3. On a specific section, click **Revoke**.

  4. You will be prompted to enter your password before revoking the session.




## Step 3 - Enable Two-Factor Authentication (2FA)

To prevent future compromises, make sure that you have [Two-Factor Authentication (2FA)](https://developers.cloudflare.com/fundamentals/user-profiles/2fa/) enabled on your account.

## Step 4 - Change API keys and tokens

### API keys

If your API key might be compromised, change your API key:

  1. Log in to the Cloudflare dashboard.

[ Go to **Account home** ↗ ](https://dash.cloudflare.com/?to=/:account/home)
  2. Go to **My Profile** > **API Tokens**.

  3. In the **API Keys** section, find your key.

  4. Select **Change**.




### API tokens

If your token is lost or compromised, you can either create a new token or roll your token to generate a new secret. Rolling your API token into a new one will invalidate the previous token, but the access and permissions will be the same as the previous API token. The new token uses the [scannable format](https://developers.cloudflare.com/fundamentals/api/get-started/token-formats/), which allows credential scanning tools to detect leaked tokens.

To roll your API token:

  1. Go to **My Profile** > **API Tokens**.

[ Go to **API Tokens** ↗ ](https://dash.cloudflare.com/profile/api-tokens)
  2. Next to the API token you want to roll, select the **three dot icon** > **Roll**.

  3. Select **Confirm** to generate a new API token.




## Step 5 - Review the audit log

To access audit logs in the Cloudflare dashboard:

In the Cloudflare dashboard, go to the **Audit Logs** page.

[ Go to **Audit logs** ↗ ](https://dash.cloudflare.com/?to=/:account/audit-log)

You can search these audit logs by user email or domain and filter by date range. To download audit logs, click **Download CSV**.

Note

Depending on the volume of data, the export of large amounts of events from Audit Logs might fail with errors. We always recommend using Cloudflare [Logpush](https://developers.cloudflare.com/logs/logpush/) to make sure Audit Logs are always available and stored externally.

If you notice any settings were changed, you should undo those changes.

[PreviousTroubleshooting](https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/troubleshooting/)[NextSet up SSO ↗︎](https://developers.cloudflare.com/fundamentals/manage-members/dashboard-sso/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/fundamentals/account/account-security/secure-a-compromised-account.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
