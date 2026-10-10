---
url: https://developers.cloudflare.com/fundamentals/organizations/limitations/
title: Limitations and troubleshooting \u00b7 Cloudflare Fundamentals docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:25.236968+00:00
---

# Limitations and troubleshooting · Cloudflare Fundamentals docs

> Source: https://developers.cloudflare.com/fundamentals/organizations/limitations/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)
  3. /[Organizations](https://developers.cloudflare.com/fundamentals/organizations/)
  4. /Limitations and troubleshooting



# Limitations and troubleshooting

Last updated Oct 9, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAccount and zone limitsAPI authenticationEnterprise OrganizationsMSSP/Distributor OrganizationsTroubleshooting Organization creation errors Member invitation errors Account assignment errors

The following limitations currently apply to Cloudflare Organizations. For common errors and resolutions, refer to Troubleshooting.

## Account and zone limits

Each Organization supports a maximum of **20,000 accounts** and **200,000 zones**. This limit applies to both Enterprise and MSSP/Distributor Organizations. These limits are defaults and can be adjusted for larger enterprises and partners in some cases.

## API authentication

The following credentials support core Organization management operations and Terraform:

Operation | Supported credentials  
---|---  
[List Organizations](https://developers.cloudflare.com/api/resources/organizations/methods/list/) | Global API key, or user API token with User Details Read or User Details Write  
[Create an Organization](https://developers.cloudflare.com/api/resources/organizations/methods/create/) | Global API key, or user API token with User Details Write  
[Read](https://developers.cloudflare.com/api/resources/organizations/methods/get/), [update](https://developers.cloudflare.com/api/resources/organizations/methods/update/), or [delete](https://developers.cloudflare.com/api/resources/organizations/methods/delete/) an Organization | Global API key  
[List accounts directly attached to an Organization](https://developers.cloudflare.com/api/resources/organizations/subresources/organization_accounts/methods/get/); [view](https://developers.cloudflare.com/api/resources/organizations/subresources/organization_profile/methods/get/) or [update](https://developers.cloudflare.com/api/resources/organizations/subresources/organization_profile/methods/update/) its profile; [manage its members](https://developers.cloudflare.com/api/resources/organizations/subresources/members/) | Global API key  
Accept or reject an Organization invitation | Global API key or user API token for the invited user; no additional token permission  
Create and manage an Organization with Terraform ([`cloudflare_organization` resource ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/organization)) | Global API key and the registered email address  
Look up an existing Organization with Terraform ([`cloudflare_organization` data source ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/data-sources/organization)) | Global API key and the registered email address  
List Organizations with Terraform ([`cloudflare_organizations` data source ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/data-sources/organizations)) | Global API key and the registered email address, or user API token with User Details Read or User Details Write  
  
A supported credential must belong to a user with the required access.

User API tokens cannot currently receive the Organization-scoped permissions required by operations that require a Global API key. Prefer user API tokens where the table supports them. When you use a Global API key, also provide the user's registered email address. A Global API key has full access to the user's Cloudflare resources. Refer to [Global API key limitations](https://developers.cloudflare.com/fundamentals/api/get-started/keys/#limitations).

[Organization audit logs](https://developers.cloudflare.com/api/resources/organizations/subresources/logs/subresources/audit/methods/list/) and [billing usage](https://developers.cloudflare.com/api/resources/organizations/subresources/billing/subresources/usage/methods/get/) are separate subresources outside this matrix.

Account moves and other account-scoped operations are also outside this matrix. Refer to each endpoint's **Security** and **Accepted Permissions** sections, including [move account to an Organization](https://developers.cloudflare.com/api/resources/accounts/subresources/account_organizations/methods/create/), [get account profile](https://developers.cloudflare.com/api/resources/accounts/subresources/account_profile/methods/get/), and [update account profile](https://developers.cloudflare.com/api/resources/accounts/subresources/account_profile/methods/update/).

## Enterprise Organizations

Limitation | Description  
---|---  
Organization creation | You must be a Super Administrator of an Enterprise account to create an Organization.  
Adding accounts | You can add accounts of any plan type (eg Enterprise, or Free) to your Organization. You must have Super Administrator access to the account, and it cannot already belong to another Organization.  
Account creation | Organization Super Administrators can create up to five Free accounts within their Organization. API tokens and OAuth access tokens cannot create accounts within an Organization. Refer to [Create new accounts](https://developers.cloudflare.com/fundamentals/organizations/for-enterprise/#create-new-accounts).  
Sub-Organizations | Not available. Enterprise Organizations use a flat, single-tier structure. Use tags to organize accounts by business unit, region, or environment.  
Moving accounts | Accounts cannot be moved between Organizations.  
Roles | Organization Super Administrator is the only role available. Additional roles (read-only, billing, audit log) will be available in a future release.  
Organization deletion | To delete an Organization, use the [API](https://developers.cloudflare.com/api/resources/organizations/methods/delete). Dashboard support is not yet available.  
Account removal | Self-service account removal is not yet available. To remove an account from your Organization, contact [Cloudflare Support](https://developers.cloudflare.com/support/contacting-cloudflare-support/).  
  
## MSSP/Distributor Organizations

Limitation | Description  
---|---  
Organization creation | MSSP/Distributor Organizations are created by Cloudflare. Contact your account team to set up your Organization.  
Adding existing accounts | Assigning existing accounts is not available for MSSP/Distributor Organizations. Use account creation to add new accounts.  
Account creation | MSSP Organizations can self-serve create new customer accounts within their Organization.  
Sub-Organizations | Distributors can create child MSSP Organizations. MSSP/Distributor Organizations support up to 5 levels of nested sub-organizations.  
Moving accounts | Accounts can be moved between MSSP Organizations within the same Distributor Organization.  
Roles | Organization Super Administrator is the only role available. Additional roles (read-only, billing, audit log) will be available in a future release.  
Organization deletion | To delete an Organization, use the [API](https://developers.cloudflare.com/api/resources/organizations/methods/delete). Dashboard support is not yet available.  
Account removal | Self-service account removal is not yet available. To remove an account from your Organization, contact [Cloudflare Support](https://developers.cloudflare.com/support/contacting-cloudflare-support/).  
Organization type conversion | Organization type (Enterprise vs MSSP/Distributor) is set at creation and cannot be changed. To switch types, a new Organization must be created.  
  
## Troubleshooting

You may encounter the following errors when setting up or managing an Organization.

### Organization creation errors

Error | Description  
---|---  
Organization management is only available on the Enterprise plan at this time. | You are not a member of any Enterprise accounts. You must be a Super Administrator of at least one Enterprise account to create an Organization.  
You need a super admin role on an enterprise account to create an Organization. | You are not a Super Administrator of an Enterprise account. Check your role under **Manage Account** > **Members** on your Enterprise account.  
One or more of your enterprise accounts is already part of an Organization. | Your accounts are already assigned to an Organization. Contact your company administrator to be invited to the existing Organization.  
You have reached the maximum number of organizations. | Each user can only create one Organization. If you need to manage a second Organization, contact [Cloudflare Support](https://developers.cloudflare.com/support/contacting-cloudflare-support/).  
An Organization has already been created for accounts associated with your company. Please contact your company administrator. | Every company is limited to one Organization for all business units. Contact your company's Cloudflare administrator to be invited to the existing Organization.  
You are not eligible to create an Organization because we think there's a problem. Please contact Cloudflare support and we will help you create it. | This rare error may indicate an issue with the internal metadata for one or more of your accounts. Contact [Cloudflare Support](https://developers.cloudflare.com/support/contacting-cloudflare-support/) with your account ID and the error message.  
  
### Member invitation errors

Error | Resolution  
---|---  
Invited member cannot accept the invitation. | The invited user must have [two-factor authentication (2FA)](https://developers.cloudflare.com/fundamentals/user-profiles/2fa/) or [single sign-on (SSO)](https://developers.cloudflare.com/fundamentals/manage-members/dashboard-sso/) enabled on their Cloudflare user account before they can accept an Organization invitation. This is a per-user requirement, not an account-level setting. Ask the user to enable 2FA or SSO, then resend the invitation.  
Member does not have access to accounts after accepting. | Organization membership grants implicit access, which may take a few minutes to propagate. If access does not appear after 5 minutes, ask the member to log out and log back in.  
  
### Account assignment errors

Error | Resolution  
---|---  
Account does not appear in the assignment list. | You must be a Super Administrator of the account. Verify your role under **Manage Account** > **Members** on that account.  
Account cannot be assigned. | The account may already belong to another Organization. Each account can only belong to one Organization. Contact [Cloudflare Support](https://developers.cloudflare.com/support/contacting-cloudflare-support/) if you believe this is incorrect.  
  
[PreviousPolicy sharing](https://developers.cloudflare.com/fundamentals/organizations/policy-sharing/)[NextMembers and permissions](https://developers.cloudflare.com/fundamentals/manage-members/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/fundamentals/organizations/limitations.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
