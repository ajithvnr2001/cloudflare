---
url: https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/okta/
title: Provision with Okta \u00b7 Cloudflare Fundamentals docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:19.737609+00:00
---

# Provision with Okta · Cloudflare Fundamentals docs

> Source: https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/okta/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)
  3. /…

AccountsAccount security

  4. /[SCIM provisioning](https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/)
  5. /Okta



# Provision with Okta

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/okta/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSet up your Okta SCIM applicationIntegrate the Cloudflare APIConfigure user & group sync in Okta

Note

**Important Update:** Cloudflare now supports native User Groups for enhanced access control. This new feature replaces the previous method of directly assigning Cloudflare roles based on IdP group mappings (identified by the pattern `CF-<accountID> - <Role Name>`), which is deprecated as of June 2nd, 2025. SCIM Virtual Groups will reach end-of-life on December 2, 2025. Update your SCIM configurations using the instructions below to utilize User Groups for seamless provisioning.

Once you have [gathered the required data](https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/#gather-the-required-data), the following steps will be required to finish the provisioning with Okta.

## Set up your Okta SCIM application

  1. In the Okta dashboard, go to **Applications** > **Applications**.
  2. Select **Browse App Catalog**.
  3. Locate and select **SCIM 2.0 Test App (OAuth Bearer Token)**.
  4. Select **Add Integration** and name your integration.
  5. Enable the following options: 
     * **Do not display application icon to users**
     * **Do not display application icon in the Okta Mobile App**
  6. Disable **Automatically log in when user lands on login page**.
  7. Select **Next** , then select **Done**.



## Integrate the Cloudflare API

Note

The **Update User Attributes** option is not supported.

  1. In your integration page, go to **Provisioning** > **Configure API Integration**.
  2. Enable **Enable API Integration**.
  3. In SCIM 2.0 Base URL, enter: `https://api.cloudflare.com/client/v4/accounts/<accountID>/scim/v2`, substituting `accountID` for your [Cloudflare Account ID](https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/#get-the-account-id).
  4. In the **OAuth Bearer Token** field, enter your API token value.
  5. Deselect **Import Groups**.



## Configure user & group sync in Okta

  1. In **Provisioning to App** , select **Edit**.
  2. Enable **Create Users** and **Deactivate Users**. Select **Save**.
  3. Select **Done**.
  4. In the Assignments tab, add the users you want to synchronize with Cloudflare dashboard. You can add users in batches by assigning a group. If a user is removed from the application assignment via either direct user assignment or removed from the group that was assigned to the app, this will trigger a deprovisioning event from Okta to Cloudflare.
  5. In the Push Groups tab, add the Okta groups you want to synchronize with Cloudflare dashboard. View these Okta groups in the dashboard under Manage Account > Manage members > Members > User Groups.



To verify the integration, select **View Logs** in the Okta SCIM application, and check the Audit Logs in the Cloudflare dashboard by navigating to **Manage Account** > **Audit Log**.

This will provision all of the users in the group(s) affected to your Cloudflare account with "minimal account access."

[PreviousMicrosoft Entra](https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/entra/)[NextTroubleshooting](https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/troubleshooting/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/fundamentals/account/account-security/scim-setup/okta.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
