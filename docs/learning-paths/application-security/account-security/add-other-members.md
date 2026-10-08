---
url: https://developers.cloudflare.com/learning-paths/application-security/account-security/add-other-members/
title: Add and manage other members \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:42.479563+00:00
---

# Add and manage other members · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/application-security/account-security/add-other-members/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Application Security

  4. /[Account security](https://developers.cloudflare.com/learning-paths/application-security/account-security/)
  5. /Add and manage other members



# Add and manage other members

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/application-security/account-security/add-other-members/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewView account membersAdd account membersEdit member permissionsResend an invitationRemove account members

Learn how to add new account members, edit or revoke their permissions and access, and resend verifications emails.

Note

To manage account members, you must have a role of **Super Administrator** and have a [verified email address](https://developers.cloudflare.com/fundamentals/user-profiles/verify-email-address/).

## View account members

To manage account members, you must have a role of **Super Administrator** and have a [verified email address](https://developers.cloudflare.com/fundamentals/user-profiles/verify-email-address/).

To view members using the dashboard:

In the [Cloudflare dashboard, go to the **Members** page.

[ Go to **Members** ↗ ](https://dash.cloudflare.com/?to=/:account/members)

To view members using the API, send a [`GET` request](https://developers.cloudflare.com/api/resources/accounts/subresources/members/methods/list/).

## Add account members

To manage account members, you must have a role of **Super Administrator** and have a [verified email address](https://developers.cloudflare.com/fundamentals/user-profiles/verify-email-address/).

To add a member to your account:

  1. In the Cloudflare dashboard, go to the **Members** page.

[ Go to **Members** ↗ ](https://dash.cloudflare.com/?to=/:account/members)
  2. Select **Invite**.

  3. Fill out the following information:

     * **Invite members** : Enter one or more email addresses (if multiple, separate addresses with commas).
     * **Scope** : Use a variety of fields to adjust the [scope](https://developers.cloudflare.com/fundamentals/manage-members/roles/) of your roles.
     * **Roles** : Choose one or more [roles](https://developers.cloudflare.com/fundamentals/manage-members/roles/) to assign your members.
  4. Select **Continue to summary**.

  5. Review the information, then select **Invite**.




Note

If a user already has an account with Cloudflare and you have an Enterprise account, you can also select **Skip email confirmation** to add them to your account without sending an email invitation.

To add a member using the API, send a [`POST` request](https://developers.cloudflare.com/api/resources/accounts/subresources/members/methods/create/).

## Edit member permissions

To manage account members, you must have a role of **Super Administrator** and have a [verified email address](https://developers.cloudflare.com/fundamentals/user-profiles/verify-email-address/).

To edit member permissions using the dashboard:

  1. In the Cloudflare dashboard, go to the **Members** page.

[ Go to **Members** ↗ ](https://dash.cloudflare.com/?to=/:account/members)
  2. Select a member record, then select **Edit**.

  3. Update the scope and roles of their permissions.

  4. Select **Continue to summary**.

  5. Review the information, then select **Update**.




To edit member permissions using the API, get a [list of roles](https://developers.cloudflare.com/api/resources/accounts/subresources/roles/methods/list/) available for an account.

Then, send a [`PUT` request](https://developers.cloudflare.com/api/resources/accounts/subresources/members/methods/update/) to edit their permissions.

Requestbash
    
    
    curl --request PUT \
      --url https://api.cloudflare.com/client/v4/accounts/{account_id}/members/{member_id} \
      --header 'Authorization: Bearer <API_TOKEN>' \
      --header 'Content-Type: application/json' \
      --data '{
    	  "roles": [
    	        {
    	            "id": "<ROLE_ID1>"
    	        },
    	        {
    	            "id": "<ROLE_ID2>"
    	        }
    	  	]
    		}'

## Resend an invitation

If you invited a member to your account but they cannot find the invitation or the invitation expires, you can resend the invitation through the Cloudflare dashboard:

  1. Log in to the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/login) and select your account1.
  2. Go to **Manage Account** > **Members**.
  3. Select a member record where their **Status** is **Invite Pending**.
  4. Select **Resend invite**.



## Footnotes

  1. To manage account members, you must have a role of **Super Administrator** and have a [verified email address](https://developers.cloudflare.com/fundamentals/user-profiles/verify-email-address/). ↩




## Remove account members

To manage account members, you must have a role of **Super Administrator** and have a [verified email address](https://developers.cloudflare.com/fundamentals/user-profiles/verify-email-address/).

To revoke a member's access to your account:

  1. In the Cloudflare dashboard, go to the **Members** page.

[ Go to **Members** ↗ ](https://dash.cloudflare.com/?to=/:account/members)
  2. Locate an account member and expand their record.

  3. Click **Revoke**.

  4. Click **Yes, revoke access**.




To revoke a member's access to your account using the API, send a [`DELETE` request](https://developers.cloudflare.com/api/resources/accounts/subresources/members/methods/delete/).

[PreviousSet-up 2FA](https://developers.cloudflare.com/learning-paths/application-security/account-security/set-up-2fa/)[NextReview active sessions](https://developers.cloudflare.com/learning-paths/application-security/account-security/review-active-sessions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/application-security/account-security/add-other-members.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
