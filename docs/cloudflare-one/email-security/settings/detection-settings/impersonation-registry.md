---
url: https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/impersonation-registry/
title: Impersonation registry \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:37.371152+00:00
---

# Impersonation registry · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/impersonation-registry/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)Settings

  4. /Detection settings
  5. /Impersonation registry



# Impersonation registry

Last updated Sep 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/impersonation-registry/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview CSV uploadsEdit usersRemove users

The impersonation registry contains combinations of emails of users who are likely to be impersonated. If there is an email that is on the impersonation registry not listed as an alternative email address, that email will be reported as potential [business email compromise (BEC) ↗︎](https://www.cloudflare.com/en-gb/learning/email-security/business-email-compromise-bec/).

Note

The impersonation registry should contain a list of users who are likely to be impersonated. Email security applies enhanced security to variations of registered email addresses for additional [Business Email Compromise (BEC) ↗︎](https://www.cloudflare.com/en-gb/learning/email-security/business-email-compromise-bec/) protection.

For easier tracking, the Email security team recommends syncing and structuring VIPs in groups, and avoid doing manual inputs of users.

To add a user to the impersonation registry:

  1. Log in to [Cloudflare One ↗︎](https://one.dash.cloudflare.com/).
  2. Select **Email security**.
  3. Select **Settings** > **Impersonation registry** > **View**.
  4. Select **Add a user**.
  5. Select **Input method** : Choose between **Manual input** , **Upload manual list** , and **Select from existing directories** : 
     * **Manual input** : Enter the following information: 
       * **User info** : enter a valid **Display name**.
       * **User email** : Enter one of the following: 
         * **Email address** : Enter all known email addresses, separated by a comma.
         * **Regular expressions** : Must be valid Java expressions.
     * **Upload manual list** : You can upload a file no larger than 150 KB containing all variables of potential emails. The file must contain `Display_Name` and `Email`, and the first row must be the header row. Refer to [CSV uploads](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/impersonation-registry/#csv-uploads) for an example file.
     * **Select from existing directories** : 
       * **Select directory** : Select your directory.
       * **Add users or groups** : Choose the users or groups you want to register.
  6. Select **Save**.



### CSV uploads

You can upload a file no larger than 150 KB containing all variables of potential emails. The file must contain `Display_Name` and `Email`, and the first row must be the header row.

An example file would look like this:
    
    
    Display Name, Email
    Star Phish, star@nophish.com
    Phish Ee, phishee@nophish.com

## Edit users

Note

Administrators can edit the names and emails of users who belong to the Email security directory. Administrators from other integrated directories cannot edit the name and the primary emails of users.

To edit users from the Email security directory:

  1. Select the user you want to edit.
  2. Select the three dots > **Edit**.
  3. Enter the **Display name** , **Email** and **Secondary email**.
  4. Select **Save**.



To edit users from other integrations:

  1. Select the user you want to edit.
  2. Select the three dots > **Edit**.
  3. Enter the **Secondary email**.
  4. Select **Save**.



## Remove users

Note

Administrators can remove users who belong to the Email security directory from the **Impersonation registry**. Users who come from an integrated directory cannot be removed from the **Impersonation registry** directly.

To remove a user from an integrated directory:

  1. Select **Directories** on the sidebar.
  2. Select the directory where your user is allocated.
  3. Select the **Users** tab.
  4. Search for the user you want to remove.
  5. Select the three dots > **Remove from registry**.



To remove a user from the impersonation registry:

  1. Select the user you want to remove.
  2. Select the three dots > **Remove from registry**.
  3. Read the pop-up message, then select **Remove user**.



To remove multiple users at once from the impersonation registry:

  1. Select all the users you want to remove.
  2. Select **Action** > **Remove from registry**.
  3. Read the pop-up message, then select **Remove users**.



[PreviousManage Email security directories](https://developers.cloudflare.com/cloudflare-one/email-security/settings/domains-and-directories/directories/manage-es-directories/)[NextAuto-move events](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/auto-moves/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/email-security/settings/detection-settings/impersonation-registry.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
