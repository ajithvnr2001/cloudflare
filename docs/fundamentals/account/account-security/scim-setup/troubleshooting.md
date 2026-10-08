---
url: https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/troubleshooting/
title: SCIM troubleshooting \u00b7 Cloudflare Fundamentals docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:19.951621+00:00
---

# SCIM troubleshooting · Cloudflare Fundamentals docs

> Source: https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/troubleshooting/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)
  3. /…

AccountsAccount security

  4. /[SCIM provisioning](https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/)
  5. /Troubleshooting



# SCIM troubleshooting

Last updated Jul 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/troubleshooting/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRestore Super Administrator after group misconfigurationUpdate email domains after onboarding

## Restore Super Administrator after group misconfiguration

If you have removed all Super Administrators mistakenly, you can restore the role to account member(s) using the Account API Token you created for SCIM provisioning.

First, fetch a list of account members and find the member ID for the user you want to restore Super Admin to via [list members](https://developers.cloudflare.com/api/resources/accounts/subresources/members/methods/list/).
    
    
    curl -X GET "https://api.cloudflare.com/client/v4/accounts/{account_id}/members" \
      -H "Authorization: Bearer YOUR_SCIM_AOT" \
      -H "Content-Type: application/json"

Then restore the Super Admin role to that member via [update member](https://developers.cloudflare.com/api/resources/accounts/subresources/members/methods/update/)
    
    
    curl -X PUT "https://api.cloudflare.com/client/v4/accounts/{account_id}/members/{member_id}" \
      -H "Authorization: Bearer YOUR_SCIM_AOT" \
      -H "Content-Type: application/json" \
      -d '{
        "roles": [
          {
            "id": "33666b9c79b9a5273fc7344ff42f953d"
          }
        ]
      }'

The value `33666b9c79b9a5273fc7344ff42f953d` is the role ID of Super Administrator.

## Update email domains after onboarding

We currently **do not** support updating email domains for users. This means that any SCIM `PATCH`/`PUT` operations that change email domains will be rejected. We recommend not using the email as the matching attribute if email domains are expected to change, and restarting provisioning manually.

[PreviousOkta](https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/okta/)[NextSecure compromised account](https://developers.cloudflare.com/fundamentals/account/account-security/secure-a-compromised-account/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/fundamentals/account/account-security/scim-setup/troubleshooting.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
