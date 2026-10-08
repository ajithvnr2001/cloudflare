---
url: https://developers.cloudflare.com/api/
title: API Reference | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:18:30.049623+00:00
---

# API Reference | Cloudflare API

> Source: https://developers.cloudflare.com/api/

# API Reference

### Libraries

TypeScript

7.3.0
    
    
    npm install cloudflare

[](https://www.github.com/cloudflare/cloudflare-typescript)[Read Docs](https://developers.cloudflare.com/api/typescript)

Python

5.9.0
    
    
    pip install cloudflare

[](https://www.github.com/cloudflare/cloudflare-python)[Read Docs](https://developers.cloudflare.com/api/python)

Go

v7.12.0
    
    
    go get -u github.com/cloudflare/cloudflare-go/v7@v7.12.0

[](https://www.github.com/cloudflare/cloudflare-go)[Read Docs](https://developers.cloudflare.com/api/go)

Terraform

5.27.0
    
    
    terraform {
      required_providers {
        cloudflare = {
          source  = "cloudflare/cloudflare"
          version = "~> 5.0"
        }
      }
    }

[](https://www.github.com/cloudflare/terraform-provider-cloudflare)[Read Docs](https://developers.cloudflare.com/api/terraform)

### API Overview

#### Accounts

##### [List Accounts](https://developers.cloudflare.com/api/resources/accounts/methods/list)

GET/accounts

##### [Account Details](https://developers.cloudflare.com/api/resources/accounts/methods/get)

GET/accounts/{account_id}

##### [Create an Account](https://developers.cloudflare.com/api/resources/accounts/methods/create)

POST/accounts

##### [Update Account](https://developers.cloudflare.com/api/resources/accounts/methods/update)

PUT/accounts/{account_id}

##### [Delete a specific account](https://developers.cloudflare.com/api/resources/accounts/methods/delete)

DELETE/accounts/{account_id}

#### AccountsAccount Organizations

##### [Move account to organization](https://developers.cloudflare.com/api/resources/accounts/subresources/account_organizations/methods/create)

POST/accounts/{account_id}/move

#### AccountsAccount Profile

##### [Get account profile](https://developers.cloudflare.com/api/resources/accounts/subresources/account_profile/methods/get)

GET/accounts/{account_id}/profile

##### [Update account profile](https://developers.cloudflare.com/api/resources/accounts/subresources/account_profile/methods/update)

PUT/accounts/{account_id}/profile

#### AccountsMembers

##### [List Members](https://developers.cloudflare.com/api/resources/accounts/subresources/members/methods/list)

GET/accounts/{account_id}/members

##### [Member Details](https://developers.cloudflare.com/api/resources/accounts/subresources/members/methods/get)

GET/accounts/{account_id}/members/{member_id}

##### [Add Member](https://developers.cloudflare.com/api/resources/accounts/subresources/members/methods/create)

POST/accounts/{account_id}/members

##### [Update Member](https://developers.cloudflare.com/api/resources/accounts/subresources/members/methods/update)

PUT/accounts/{account_id}/members/{member_id}

##### [Remove Member](https://developers.cloudflare.com/api/resources/accounts/subresources/members/methods/delete)

DELETE/accounts/{account_id}/members/{member_id}

#### AccountsRoles

##### [List Roles](https://developers.cloudflare.com/api/resources/accounts/subresources/roles/methods/list)

Deprecated

GET/accounts/{account_id}/roles

##### [Role Details](https://developers.cloudflare.com/api/resources/accounts/subresources/roles/methods/get)

Deprecated

GET/accounts/{account_id}/roles/{role_id}

#### AccountsSubscriptions

##### [List Subscriptions](https://developers.cloudflare.com/api/resources/accounts/subresources/subscriptions/methods/get)

GET/{accounts_or_zones}/{account_or_zone_id}/subscriptions

##### [Get Subscription](https://developers.cloudflare.com/api/resources/accounts/subresources/subscriptions/methods/get_by_identifier)

GET/accounts/{account_id}/subscriptions/{subscription_identifier}

##### [Create Subscription](https://developers.cloudflare.com/api/resources/accounts/subresources/subscriptions/methods/create)

POST/{accounts_or_zones}/{account_or_zone_id}/subscriptions

##### [Update Subscription](https://developers.cloudflare.com/api/resources/accounts/subresources/subscriptions/methods/update)

PUT/accounts/{account_id}/subscriptions/{subscription_identifier}

##### [Delete Subscription](https://developers.cloudflare.com/api/resources/accounts/subresources/subscriptions/methods/delete)

DELETE/accounts/{account_id}/subscriptions/{subscription_identifier}

##### [Cancel Delayed Downgrade](https://developers.cloudflare.com/api/resources/accounts/subresources/subscriptions/methods/cancel_downgrade)

POST/accounts/{account_id}/subscriptions/cancel-downgrade

#### AccountsSubscriptionsCancel Reason

##### [Create Cancel Reason](https://developers.cloudflare.com/api/resources/accounts/subresources/subscriptions/subresources/cancel_reason/methods/create)

POST/accounts/{account_id}/subscriptions/{subscription_identifier}/cancel-reason

##### [Get Cancel Reason](https://developers.cloudflare.com/api/resources/accounts/subresources/subscriptions/subresources/cancel_reason/methods/get)

GET/accounts/{account_id}/subscriptions/{subscription_identifier}/cancel-reason

#### AccountsSubscriptionsActions

##### [Append Subscription Action](https://developers.cloudflare.com/api/resources/accounts/subresources/subscriptions/subresources/actions/methods/append)

POST/accounts/{account_id}/subscriptions/{subscription_identifier}/action/append

#### AccountsSubscriptionsBulk

##### [Create Subscriptions](https://developers.cloudflare.com/api/resources/accounts/subresources/subscriptions/subresources/bulk/methods/create)

POST/accounts/{account_id}/bulk/subscriptions

#### AccountsTokens

##### [List Tokens](https://developers.cloudflare.com/api/resources/accounts/subresources/tokens/methods/list)

GET/accounts/{account_id}/tokens

##### [Token Details](https://developers.cloudflare.com/api/resources/accounts/subresources/tokens/methods/get)

GET/accounts/{account_id}/tokens/{token_id}

##### [Create Token](https://developers.cloudflare.com/api/resources/accounts/subresources/tokens/methods/create)

POST/accounts/{account_id}/tokens

##### [Update Token](https://developers.cloudflare.com/api/resources/accounts/subresources/tokens/methods/update)

PUT/accounts/{account_id}/tokens/{token_id}

##### [Delete Token](https://developers.cloudflare.com/api/resources/accounts/subresources/tokens/methods/delete)

DELETE/accounts/{account_id}/tokens/{token_id}

##### [Verify Token](https://developers.cloudflare.com/api/resources/accounts/subresources/tokens/methods/verify)

GET/accounts/{account_id}/tokens/verify

#### AccountsTokensPermission Groups

##### [List Permission Groups](https://developers.cloudflare.com/api/resources/accounts/subresources/tokens/subresources/permission_groups/methods/list)

GET/accounts/{account_id}/tokens/permission_groups

##### [List Permission Groups](https://developers.cloudflare.com/api/resources/accounts/subresources/tokens/subresources/permission_groups/methods/get)

GET/accounts/{account_id}/tokens/permission_groups

#### AccountsTokensValue

##### [Roll Token](https://developers.cloudflare.com/api/resources/accounts/subresources/tokens/subresources/value/methods/update)

PUT/accounts/{account_id}/tokens/{token_id}/value

#### AccountsLogs

#### AccountsLogsAudit

##### [Get account audit logs (Version 2)](https://developers.cloudflare.com/api/resources/accounts/subresources/logs/subresources/audit/methods/list)

GET/accounts/{account_id}/logs/audit

##### [Get resource change history from an account audit log entry (Version 2)](https://developers.cloudflare.com/api/resources/accounts/subresources/logs/subresources/audit/methods/history)

GET/accounts/{account_id}/logs/audit/{id}/history

##### [List account audit log product categories (Version 2)](https://developers.cloudflare.com/api/resources/accounts/subresources/logs/subresources/audit/methods/product_categories)

GET/accounts/{account_id}/logs/audit/product_categories

#### AccountsEntitlements

##### [Get Account Entitlements](https://developers.cloudflare.com/api/resources/accounts/subresources/entitlements/methods/list)

GET/accounts/{account_id}/entitlements

#### AccountsSpeed Settings

#### AccountsSpeed SettingsTransformations

##### [List Image Resizing configurations for account](https://developers.cloudflare.com/api/resources/accounts/subresources/speed_settings/subresources/transformations/methods/get)

GET/accounts/{account_id}/settings/transformations

#### AccountsPayment Methods

##### [List Payment Methods](https://developers.cloudflare.com/api/resources/accounts/subresources/payment_methods/methods/list)

GET/accounts/{account_id}/payment-methods

##### [Create Payment Method](https://developers.cloudflare.com/api/resources/accounts/subresources/payment_methods/methods/create)

POST/accounts/{account_id}/payment-methods

##### [Get Payment Method](https://developers.cloudflare.com/api/resources/accounts/subresources/payment_methods/methods/get)

GET/accounts/{account_id}/payment-methods/{payment_method_id}

##### [Update Payment Method](https://developers.cloudflare.com/api/resources/accounts/subresources/payment_methods/methods/update)

PUT/accounts/{account_id}/payment-methods/{payment_method_id}

##### [Delete Payment Method](https://developers.cloudflare.com/api/resources/accounts/subresources/payment_methods/methods/delete)

DELETE/accounts/{account_id}/payment-methods/{payment_method_id}

##### [Set Default Payment Method](https://developers.cloudflare.com/api/resources/accounts/subresources/payment_methods/methods/set_as_default)

POST/accounts/{account_id}/payment-methods/{payment_method_id}/set-as-default

#### AccountsPay Invoice

##### [Pay Invoice](https://developers.cloudflare.com/api/resources/accounts/subresources/pay_invoice/methods/create)

POST/accounts/{account_id}/pay-invoice

#### AccountsPay Bad Debt

##### [Pay Bad Debt](https://developers.cloudflare.com/api/resources/accounts/subresources/pay_bad_debt/methods/create)

POST/accounts/{account_id}/pay-bad-debt

#### AccountsReceipts

##### [Get Receipt PDF](https://developers.cloudflare.com/api/resources/accounts/subresources/receipts/methods/pdf)

GET/accounts/{account_id}/receipts/{receipt_id}/pdf

#### AccountsInvoices

##### [Toggle PDF Invoices](https://developers.cloudflare.com/api/resources/accounts/subresources/invoices/methods/edit)

PATCH/accounts/{account_id}/invoices

#### AccountsClient Secret

##### [Create Setup Intent](https://developers.cloudflare.com/api/resources/accounts/subresources/client_secret/methods/create)

POST/accounts/{account_id}/client-secret

#### Organizations

##### [List organizations the user has access to](https://developers.cloudflare.com/api/resources/organizations/methods/list)

GET/organizations

##### [Get organization](https://developers.cloudflare.com/api/resources/organizations/methods/get)

GET/organizations/{organization_id}

##### [Create organization](https://developers.cloudflare.com/api/resources/organizations/methods/create)

POST/organizations

##### [Update organization](https://developers.cloudflare.com/api/resources/organizations/methods/update)

PUT/organizations/{organization_id}

##### [Delete organization](https://developers.cloudflare.com/api/resources/organizations/methods/delete)

DELETE/organizations/{organization_id}

#### OrganizationsOrganization Accounts

##### [List organization accounts](https://developers.cloudflare.com/api/resources/organizations/subresources/organization_accounts/methods/get)

GET/organizations/{organization_id}/accounts

#### OrganizationsOrganization Profile

##### [Get organization profile](https://developers.cloudflare.com/api/resources/organizations/subresources/organization_profile/methods/get)

GET/organizations/{organization_id}/profile

##### [Modify organization profile.](https://developers.cloudflare.com/api/resources/organizations/subresources/organization_profile/methods/update)

PUT/organizations/{organization_id}/profile

#### OrganizationsMembers

##### [List organization members](https://developers.cloudflare.com/api/resources/organizations/subresources/members/methods/list)

GET/organizations/{organization_id}/members

##### [Get organization member](https://developers.cloudflare.com/api/resources/organizations/subresources/members/methods/get)

GET/organizations/{organization_id}/members/{member_id}

##### [Create organization member](https://developers.cloudflare.com/api/resources/organizations/subresources/members/methods/create)

POST/organizations/{organization_id}/members

##### [Delete organization member](https://developers.cloudflare.com/api/resources/organizations/subresources/members/methods/delete)

DELETE/organizations/{organization_id}/members/{member_id}

#### OrganizationsLogs

#### OrganizationsLogsAudit

##### [Get organization audit logs (Version 2)](https://developers.cloudflare.com/api/resources/organizations/subresources/logs/subresources/audit/methods/list)

GET/organizations/{organization_id}/logs/audit

##### [Get resource change history from an organization audit log entry (Version 2)](https://developers.cloudflare.com/api/resources/organizations/subresources/logs/subresources/audit/methods/history)

GET/organizations/{organization_id}/logs/audit/{id}/history

#### OrganizationsBilling

#### OrganizationsBillingUsage

##### [Get Organization Usage (Version 2, Alpha, Restricted)](https://developers.cloudflare.com/api/resources/organizations/subresources/billing/subresources/usage/methods/get)

GET/organizations/{organization_id}/billable/usage

#### Tenants

##### [Get tenant details](https://developers.cloudflare.com/api/resources/tenants/methods/get)

GET/tenants/{tenant_id}

#### TenantsAccount Types

##### [List tenant account types](https://developers.cloudflare.com/api/resources/tenants/subresources/account_types/methods/list)

GET/tenants/{tenant_id}/account_types

#### TenantsAccounts

##### [List tenant accounts](https://developers.cloudflare.com/api/resources/tenants/subresources/accounts/methods/list)

GET/tenants/{tenant_id}/accounts

#### TenantsEntitlements

##### [List tenant entitlements](https://developers.cloudflare.com/api/resources/tenants/subresources/entitlements/methods/get)

GET/tenants/{tenant_id}/entitlements

#### TenantsMemberships

##### [List tenant memberships](https://developers.cloudflare.com/api/resources/tenants/subresources/memberships/methods/list)

GET/tenants/{tenant_id}/memberships

#### Origin CA Certificates

##### [List Certificates](https://developers.cloudflare.com/api/resources/origin_ca_certificates/methods/list)

GET/certificates

##### [Get Certificate](https://developers.cloudflare.com/api/resources/origin_ca_certificates/methods/get)

GET/certificates/{certificate_id}

##### [Create Certificate](https://developers.cloudflare.com/api/resources/origin_ca_certificates/methods/create)

POST/certificates

##### [Revoke Certificate](https://developers.cloudflare.com/api/resources/origin_ca_certificates/methods/delete)

DELETE/certificates/{certificate_id}

#### IPs

##### [Cloudflare/JD Cloud IP Details](https://developers.cloudflare.com/api/resources/ips/methods/list)

GET/ips

#### Memberships

##### [List Memberships](https://developers.cloudflare.com/api/resources/memberships/methods/list)

GET/memberships

##### [Membership Details](https://developers.cloudflare.com/api/resources/memberships/methods/get)

GET/memberships/{membership_id}

##### [Update Membership](https://developers.cloudflare.com/api/resources/memberships/methods/update)

PUT/memberships/{membership_id}

##### [Delete Membership](https://developers.cloudflare.com/api/resources/memberships/methods/delete)

DELETE/memberships/{membership_id}

#### User

##### [User Details](https://developers.cloudflare.com/api/resources/user/methods/get)

GET/user

##### [Edit User](https://developers.cloudflare.com/api/resources/user/methods/edit)

PATCH/user

#### UserAudit Logs

##### [Get user audit logs](https://developers.cloudflare.com/api/resources/user/subresources/audit_logs/methods/list)

GET/user/audit_logs

#### UserBilling

#### UserBillingHistory

##### [Billing History Details](https://developers.cloudflare.com/api/resources/user/subresources/billing/subresources/history/methods/list)

Deprecated

GET/user/billing/history

#### UserBillingProfile

##### [Billing Profile Details](https://developers.cloudflare.com/api/resources/user/subresources/billing/subresources/profile/methods/get)

Deprecated

GET/user/billing/profile

#### UserInvites

##### [List Invitations](https://developers.cloudflare.com/api/resources/user/subresources/invites/methods/list)

GET/user/invites

##### [Invitation Details](https://developers.cloudflare.com/api/resources/user/subresources/invites/methods/get)

GET/user/invites/{invite_id}

##### [Respond to Invitation](https://developers.cloudflare.com/api/resources/user/subresources/invites/methods/edit)

PATCH/user/invites/{invite_id}

#### UserOrganizations

##### [List Organizations](https://developers.cloudflare.com/api/resources/user/subresources/organizations/methods/list)

Deprecated

GET/user/organizations

##### [Organization Details](https://developers.cloudflare.com/api/resources/user/subresources/organizations/methods/get)

Deprecated

GET/user/organizations/{organization_id}

##### [Leave Organization](https://developers.cloudflare.com/api/resources/user/subresources/organizations/methods/delete)

Deprecated

DELETE/user/organizations/{organization_id}

#### UserSpectrum Analytics

#### UserSpectrum AnalyticsZones

#### UserSpectrum AnalyticsZonesReports

##### [Get zones bandwidth report](https://developers.cloudflare.com/api/resources/user/subresources/spectrum_analytics/subresources/zones/subresources/reports/methods/get)

GET/user/spectrum_analytics/zones/report

#### UserSubscriptions

##### [Get User Subscriptions](https://developers.cloudflare.com/api/resources/user/subresources/subscriptions/methods/get)

GET/user/subscriptions

##### [Update User Subscription](https://developers.cloudflare.com/api/resources/user/subresources/subscriptions/methods/update)

PUT/user/subscriptions/{identifier}

##### [Delete User Subscription](https://developers.cloudflare.com/api/resources/user/subresources/subscriptions/methods/delete)

DELETE/user/subscriptions/{identifier}

#### UserTenants

##### [List user tenants](https://developers.cloudflare.com/api/resources/user/subresources/tenants/methods/list)

GET/user/tenants

#### UserTokens

##### [List Tokens](https://developers.cloudflare.com/api/resources/user/subresources/tokens/methods/list)

GET/user/tokens

##### [Token Details](https://developers.cloudflare.com/api/resources/user/subresources/tokens/methods/get)

GET/user/tokens/{token_id}

##### [Create Token](https://developers.cloudflare.com/api/resources/user/subresources/tokens/methods/create)

POST/user/tokens

##### [Update Token](https://developers.cloudflare.com/api/resources/user/subresources/tokens/methods/update)

PUT/user/tokens/{token_id}

##### [Delete Token](https://developers.cloudflare.com/api/resources/user/subresources/tokens/methods/delete)

DELETE/user/tokens/{token_id}

##### [Verify Token](https://developers.cloudflare.com/api/resources/user/subresources/tokens/methods/verify)

GET/user/tokens/verify

#### UserTokensPermission Groups

##### [List Token Permission Groups](https://developers.cloudflare.com/api/resources/user/subresources/tokens/subresources/permission_groups/methods/list)

GET/user/tokens/permission_groups

#### UserTokensValue

##### [Roll Token](https://developers.cloudflare.com/api/resources/user/subresources/tokens/subresources/value/methods/update)

PUT/user/tokens/{token_id}/value

#### Zones

##### [List Zones](https://developers.cloudflare.com/api/resources/zones/methods/list)

GET/zones

##### [Zone Details](https://developers.cloudflare.com/api/resources/zones/methods/get)

GET/zones/{zone_id}

##### [Create Zone](https://developers.cloudflare.com/api/resources/zones/methods/create)

POST/zones

##### [Edit Zone](https://developers.cloudflare.com/api/resources/zones/methods/edit)

PATCH/zones/{zone_id}

##### [Delete Zone](https://developers.cloudflare.com/api/resources/zones/methods/delete)

DELETE/zones/{zone_id}

#### ZonesActivation Check

##### [Rerun the Activation Check](https://developers.cloudflare.com/api/resources/zones/subresources/activation_check/methods/trigger)

PUT/zones/{zone_id}/activation_check

#### ZonesObservability

#### ZonesObservabilityTracing

#### ZonesObservabilityTracingSettings

##### [View zone tracing settings](https://developers.cloudflare.com/api/resources/zones/subresources/observability/subresources/tracing/subresources/settings/methods/get)

GET/zones/{zone_id}/observability/tracing/settings

##### [Update zone tracing settings](https://developers.cloudflare.com/api/resources/zones/subresources/observability/subresources/tracing/subresources/settings/methods/update)

PATCH/zones/{zone_id}/observability/tracing/settings

##### [Reset zone tracing settings](https://developers.cloudflare.com/api/resources/zones/subresources/observability/subresources/tracing/subresources/settings/methods/delete)

DELETE/zones/{zone_id}/observability/tracing/settings

#### ZonesObservabilityTracingRules

##### [View zone trace rules](https://developers.cloudflare.com/api/resources/zones/subresources/observability/subresources/tracing/subresources/rules/methods/get)

GET/zones/{zone_id}/observability/tracing/rules

##### [Replace zone trace rules](https://developers.cloudflare.com/api/resources/zones/subresources/observability/subresources/tracing/subresources/rules/methods/update)

PUT/zones/{zone_id}/observability/tracing/rules

##### [Delete zone trace rules](https://developers.cloudflare.com/api/resources/zones/subresources/observability/subresources/tracing/subresources/rules/methods/delete)

DELETE/zones/{zone_id}/observability/tracing/rules

#### ZonesSettings

##### [Get all zone settings](https://developers.cloudflare.com/api/resources/zones/subresources/settings/methods/list)

Deprecated

GET/zones/{zone_id}/settings

##### [Get zone setting](https://developers.cloudflare.com/api/resources/zones/subresources/settings/methods/get)

GET/zones/{zone_id}/settings/{setting_id}

##### [Edit zone setting](https://developers.cloudflare.com/api/resources/zones/subresources/settings/methods/edit)

PATCH/zones/{zone_id}/settings/{setting_id}

##### [Edit multiple zone settings](https://developers.cloudflare.com/api/resources/zones/subresources/settings/methods/bulk_edit)

Deprecated

PATCH/zones/{zone_id}/settings

#### ZonesTransformations Allowed Origins

##### [Get Image Transformations Allowed Origins setting](https://developers.cloudflare.com/api/resources/zones/subresources/transformations_allowed_origins/methods/get)

GET/zones/{zone_id}/settings/transformations_allowed_origins

##### [Change Image Transformations Allowed Origins setting](https://developers.cloudflare.com/api/resources/zones/subresources/transformations_allowed_origins/methods/edit)

PATCH/zones/{zone_id}/settings/transformations_allowed_origins

#### ZonesTransformations C2pa

##### [Get Image Transformations C2PA setting](https://developers.cloudflare.com/api/resources/zones/subresources/transformations_c2pa/methods/get)

GET/zones/{zone_id}/settings/transformations_c2pa

##### [Change Image Transformations C2PA setting](https://developers.cloudflare.com/api/resources/zones/subresources/transformations_c2pa/methods/edit)

PATCH/zones/{zone_id}/settings/transformations_c2pa

#### ZonesNEL

##### [Get NEL setting](https://developers.cloudflare.com/api/resources/zones/subresources/nel/methods/get)

GET/zones/{zone_id}/settings/nel

##### [Edit NEL setting](https://developers.cloudflare.com/api/resources/zones/subresources/nel/methods/edit)

PATCH/zones/{zone_id}/settings/nel

#### ZonesEnvironments

##### [List zone environments](https://developers.cloudflare.com/api/resources/zones/subresources/environments/methods/list)

GET/zones/{zone_id}/environments

##### [Create zone environments](https://developers.cloudflare.com/api/resources/zones/subresources/environments/methods/create)

POST/zones/{zone_id}/environments

##### [Upsert zone environments](https://developers.cloudflare.com/api/resources/zones/subresources/environments/methods/update)

PUT/zones/{zone_id}/environments

##### [Partially update zone environments](https://developers.cloudflare.com/api/resources/zones/subresources/environments/methods/edit)

PATCH/zones/{zone_id}/environments

##### [Delete zone environment](https://developers.cloudflare.com/api/resources/zones/subresources/environments/methods/delete)

DELETE/zones/{zone_id}/environments/{environment_id}

##### [Roll back zone environment](https://developers.cloudflare.com/api/resources/zones/subresources/environments/methods/rollback)

POST/zones/{zone_id}/environments/{environment_id}/rollback

#### ZonesCustom Nameservers

##### [Get Account Custom Nameserver Related Zone Metadata](https://developers.cloudflare.com/api/resources/zones/subresources/custom_nameservers/methods/get)

Deprecated

GET/zones/{zone_id}/custom_ns

##### [Set Account Custom Nameserver Related Zone Metadata](https://developers.cloudflare.com/api/resources/zones/subresources/custom_nameservers/methods/update)

Deprecated

PUT/zones/{zone_id}/custom_ns

#### ZonesHolds

##### [Get Zone Hold](https://developers.cloudflare.com/api/resources/zones/subresources/holds/methods/get)

GET/zones/{zone_id}/hold

##### [Create Zone Hold](https://developers.cloudflare.com/api/resources/zones/subresources/holds/methods/create)

POST/zones/{zone_id}/hold

##### [Update Zone Hold](https://developers.cloudflare.com/api/resources/zones/subresources/holds/methods/edit)

PATCH/zones/{zone_id}/hold

##### [Remove Zone Hold](https://developers.cloudflare.com/api/resources/zones/subresources/holds/methods/delete)

DELETE/zones/{zone_id}/hold

#### ZonesSubscriptions

##### [Zone Subscription Details](https://developers.cloudflare.com/api/resources/zones/subresources/subscriptions/methods/get)

GET/zones/{zone_id}/subscription

##### [Create Zone Subscription](https://developers.cloudflare.com/api/resources/zones/subresources/subscriptions/methods/create)

POST/zones/{zone_id}/subscription

##### [Update Zone Subscription](https://developers.cloudflare.com/api/resources/zones/subresources/subscriptions/methods/update)

PUT/zones/{zone_id}/subscription

#### ZonesPlans

##### [List Available Plans](https://developers.cloudflare.com/api/resources/zones/subresources/plans/methods/list)

GET/zones/{zone_id}/available_plans

##### [Available Plan Details](https://developers.cloudflare.com/api/resources/zones/subresources/plans/methods/get)

GET/zones/{zone_id}/available_plans/{plan_identifier}

#### ZonesRate Plans

##### [List Available Rate Plans](https://developers.cloudflare.com/api/resources/zones/subresources/rate_plans/methods/get)

GET/zones/{zone_id}/available_rate_plans

#### ZonesEntitlements

##### [Get Zone Entitlements](https://developers.cloudflare.com/api/resources/zones/subresources/entitlements/methods/list)

GET/zones/{zone_id}/entitlements

#### ZonesCT

#### ZonesCTAlerting

##### [Get CT Alerting Subscription](https://developers.cloudflare.com/api/resources/zones/subresources/ct/subresources/alerting/methods/get)

GET/zones/{zone_id}/ct/alerting

##### [Update CT Alerting Subscription](https://developers.cloudflare.com/api/resources/zones/subresources/ct/subresources/alerting/methods/edit)

PATCH/zones/{zone_id}/ct/alerting

#### Load Balancers

##### [List account or zone Load Balancers](https://developers.cloudflare.com/api/resources/load_balancers/methods/list)

GET/{accounts_or_zones}/{account_or_zone_id}/load_balancers

##### [account or zone Load Balancer Details](https://developers.cloudflare.com/api/resources/load_balancers/methods/get)

GET/{accounts_or_zones}/{account_or_zone_id}/load_balancers/{load_balancer_id}

##### [Create account or zone Load Balancer](https://developers.cloudflare.com/api/resources/load_balancers/methods/create)

POST/{accounts_or_zones}/{account_or_zone_id}/load_balancers

##### [Update account or zone Load Balancer](https://developers.cloudflare.com/api/resources/load_balancers/methods/update)

PUT/{accounts_or_zones}/{account_or_zone_id}/load_balancers/{load_balancer_id}

##### [Patch account or zone Load Balancer](https://developers.cloudflare.com/api/resources/load_balancers/methods/edit)

PATCH/{accounts_or_zones}/{account_or_zone_id}/load_balancers/{load_balancer_id}

##### [Delete account or zone Load Balancer](https://developers.cloudflare.com/api/resources/load_balancers/methods/delete)

DELETE/{accounts_or_zones}/{account_or_zone_id}/load_balancers/{load_balancer_id}

#### Load BalancersMonitors

##### [List Monitors](https://developers.cloudflare.com/api/resources/load_balancers/subresources/monitors/methods/list)

GET/accounts/{account_id}/load_balancers/monitors

##### [Monitor Details](https://developers.cloudflare.com/api/resources/load_balancers/subresources/monitors/methods/get)

GET/accounts/{account_id}/load_balancers/monitors/{monitor_id}

##### [Create Monitor](https://developers.cloudflare.com/api/resources/load_balancers/subresources/monitors/methods/create)

POST/accounts/{account_id}/load_balancers/monitors

##### [Update Monitor](https://developers.cloudflare.com/api/resources/load_balancers/subresources/monitors/methods/update)

PUT/accounts/{account_id}/load_balancers/monitors/{monitor_id}

##### [Patch Monitor](https://developers.cloudflare.com/api/resources/load_balancers/subresources/monitors/methods/edit)

PATCH/accounts/{account_id}/load_balancers/monitors/{monitor_id}

##### [Delete Monitor](https://developers.cloudflare.com/api/resources/load_balancers/subresources/monitors/methods/delete)

DELETE/accounts/{account_id}/load_balancers/monitors/{monitor_id}

#### Load BalancersMonitorsPreviews

##### [Preview Monitor](https://developers.cloudflare.com/api/resources/load_balancers/subresources/monitors/subresources/previews/methods/create)

POST/accounts/{account_id}/load_balancers/monitors/{monitor_id}/preview

#### Load BalancersMonitorsReferences

##### [List Monitor References](https://developers.cloudflare.com/api/resources/load_balancers/subresources/monitors/subresources/references/methods/get)

GET/accounts/{account_id}/load_balancers/monitors/{monitor_id}/references

#### Load BalancersMonitor Groups

##### [List Monitor Groups](https://developers.cloudflare.com/api/resources/load_balancers/subresources/monitor_groups/methods/list)

GET/accounts/{account_id}/load_balancers/monitor_groups

##### [Monitor Group Details](https://developers.cloudflare.com/api/resources/load_balancers/subresources/monitor_groups/methods/get)

GET/accounts/{account_id}/load_balancers/monitor_groups/{monitor_group_id}

##### [Create Monitor Group](https://developers.cloudflare.com/api/resources/load_balancers/subresources/monitor_groups/methods/create)

POST/accounts/{account_id}/load_balancers/monitor_groups

##### [Update Monitor Group](https://developers.cloudflare.com/api/resources/load_balancers/subresources/monitor_groups/methods/update)

PUT/accounts/{account_id}/load_balancers/monitor_groups/{monitor_group_id}

##### [Patch Monitor Group](https://developers.cloudflare.com/api/resources/load_balancers/subresources/monitor_groups/methods/edit)

PATCH/accounts/{account_id}/load_balancers/monitor_groups/{monitor_group_id}

##### [Delete Monitor Group](https://developers.cloudflare.com/api/resources/load_balancers/subresources/monitor_groups/methods/delete)

DELETE/accounts/{account_id}/load_balancers/monitor_groups/{monitor_group_id}

#### Load BalancersMonitor GroupsReferences

##### [List Monitor Group References](https://developers.cloudflare.com/api/resources/load_balancers/subresources/monitor_groups/subresources/references/methods/get)

GET/accounts/{account_id}/load_balancers/monitor_groups/{monitor_group_id}/references

#### Load BalancersPools

##### [List Pools](https://developers.cloudflare.com/api/resources/load_balancers/subresources/pools/methods/list)

GET/accounts/{account_id}/load_balancers/pools

##### [Pool Details](https://developers.cloudflare.com/api/resources/load_balancers/subresources/pools/methods/get)

GET/accounts/{account_id}/load_balancers/pools/{pool_id}

##### [Create Pool](https://developers.cloudflare.com/api/resources/load_balancers/subresources/pools/methods/create)

POST/accounts/{account_id}/load_balancers/pools

##### [Update Pool](https://developers.cloudflare.com/api/resources/load_balancers/subresources/pools/methods/update)

PUT/accounts/{account_id}/load_balancers/pools/{pool_id}

##### [Patch Pool](https://developers.cloudflare.com/api/resources/load_balancers/subresources/pools/methods/edit)

PATCH/accounts/{account_id}/load_balancers/pools/{pool_id}

##### [Delete Pool](https://developers.cloudflare.com/api/resources/load_balancers/subresources/pools/methods/delete)

DELETE/accounts/{account_id}/load_balancers/pools/{pool_id}

##### [Patch Pools](https://developers.cloudflare.com/api/resources/load_balancers/subresources/pools/methods/bulk_edit)

PATCH/accounts/{account_id}/load_balancers/pools

#### Load BalancersPoolsHealth

##### [Pool Health Details](https://developers.cloudflare.com/api/resources/load_balancers/subresources/pools/subresources/health/methods/get)

GET/accounts/{account_id}/load_balancers/pools/{pool_id}/health

##### [Preview Pool](https://developers.cloudflare.com/api/resources/load_balancers/subresources/pools/subresources/health/methods/create)

POST/accounts/{account_id}/load_balancers/pools/{pool_id}/preview

#### Load BalancersPoolsReferences

##### [List Pool References](https://developers.cloudflare.com/api/resources/load_balancers/subresources/pools/subresources/references/methods/get)

GET/accounts/{account_id}/load_balancers/pools/{pool_id}/references

#### Load BalancersPreviews

##### [Preview Result](https://developers.cloudflare.com/api/resources/load_balancers/subresources/previews/methods/get)

GET/accounts/{account_id}/load_balancers/preview/{preview_id}

#### Load BalancersRegions

##### [List Regions](https://developers.cloudflare.com/api/resources/load_balancers/subresources/regions/methods/list)

GET/accounts/{account_id}/load_balancers/regions

##### [Get Region](https://developers.cloudflare.com/api/resources/load_balancers/subresources/regions/methods/get)

GET/accounts/{account_id}/load_balancers/regions/{region_id}

#### Load BalancersSearches

##### [Search Resources](https://developers.cloudflare.com/api/resources/load_balancers/subresources/searches/methods/list)

GET/accounts/{account_id}/load_balancers/search

#### Cache

##### [Purge Cached Content](https://developers.cloudflare.com/api/resources/cache/methods/purge)

POST/zones/{zone_id}/purge_cache

##### [Purge Cached Content by Environment](https://developers.cloudflare.com/api/resources/cache/methods/purge_environment)

POST/zones/{zone_id}/environments/{environment_id}/purge_cache

##### [Invalidate Cached Content](https://developers.cloudflare.com/api/resources/cache/methods/invalidate)

POST/zones/{zone_id}/invalidate_cache

##### [Invalidate Cached Content by Environment](https://developers.cloudflare.com/api/resources/cache/methods/invalidate_environment)

POST/zones/{zone_id}/environments/{environment_id}/invalidate_cache

#### CacheCache Reserve

##### [Get Cache Reserve setting](https://developers.cloudflare.com/api/resources/cache/subresources/cache_reserve/methods/get)

GET/zones/{zone_id}/cache/cache_reserve

##### [Change Cache Reserve setting](https://developers.cloudflare.com/api/resources/cache/subresources/cache_reserve/methods/edit)

PATCH/zones/{zone_id}/cache/cache_reserve

##### [Get Cache Reserve Clear](https://developers.cloudflare.com/api/resources/cache/subresources/cache_reserve/methods/status)

GET/zones/{zone_id}/cache/cache_reserve_clear

##### [Start Cache Reserve Clear](https://developers.cloudflare.com/api/resources/cache/subresources/cache_reserve/methods/clear)

POST/zones/{zone_id}/cache/cache_reserve_clear

#### CacheSmart Tiered Cache

##### [Get Smart Tiered Cache setting](https://developers.cloudflare.com/api/resources/cache/subresources/smart_tiered_cache/methods/get)

GET/zones/{zone_id}/cache/tiered_cache_smart_topology_enable

##### [Create Smart Tiered Cache setting](https://developers.cloudflare.com/api/resources/cache/subresources/smart_tiered_cache/methods/create)

POST/zones/{zone_id}/cache/tiered_cache_smart_topology_enable

##### [Patch Smart Tiered Cache setting](https://developers.cloudflare.com/api/resources/cache/subresources/smart_tiered_cache/methods/edit)

PATCH/zones/{zone_id}/cache/tiered_cache_smart_topology_enable

##### [Delete Smart Tiered Cache setting](https://developers.cloudflare.com/api/resources/cache/subresources/smart_tiered_cache/methods/delete)

DELETE/zones/{zone_id}/cache/tiered_cache_smart_topology_enable

#### CacheVariants

##### [Get variants setting](https://developers.cloudflare.com/api/resources/cache/subresources/variants/methods/get)

GET/zones/{zone_id}/cache/variants

##### [Change variants setting](https://developers.cloudflare.com/api/resources/cache/subresources/variants/methods/edit)

PATCH/zones/{zone_id}/cache/variants

##### [Delete variants setting](https://developers.cloudflare.com/api/resources/cache/subresources/variants/methods/delete)

DELETE/zones/{zone_id}/cache/variants

#### CacheRegional Tiered Cache

##### [Get Regional Tiered Cache setting](https://developers.cloudflare.com/api/resources/cache/subresources/regional_tiered_cache/methods/get)

GET/zones/{zone_id}/cache/regional_tiered_cache

##### [Change Regional Tiered Cache setting](https://developers.cloudflare.com/api/resources/cache/subresources/regional_tiered_cache/methods/edit)

PATCH/zones/{zone_id}/cache/regional_tiered_cache

#### CacheOrigin Cloud Regions

##### [List origin cloud region mappings](https://developers.cloudflare.com/api/resources/cache/subresources/origin_cloud_regions/methods/list)

GET/zones/{zone_id}/origin/cloud_regions

##### [Get an origin cloud region mapping](https://developers.cloudflare.com/api/resources/cache/subresources/origin_cloud_regions/methods/get)

GET/zones/{zone_id}/origin/cloud_regions/{origin_ip}

##### [Create or replace an origin cloud region mapping](https://developers.cloudflare.com/api/resources/cache/subresources/origin_cloud_regions/methods/update)

PUT/zones/{zone_id}/origin/cloud_regions/{origin_ip}

##### [Delete an origin cloud region mapping](https://developers.cloudflare.com/api/resources/cache/subresources/origin_cloud_regions/methods/delete)

DELETE/zones/{zone_id}/origin/cloud_regions/{origin_ip}

##### [Batch create or replace origin cloud region mappings](https://developers.cloudflare.com/api/resources/cache/subresources/origin_cloud_regions/methods/bulk_update)

PUT/zones/{zone_id}/origin/cloud_regions/batch

##### [Batch delete origin cloud region mappings](https://developers.cloudflare.com/api/resources/cache/subresources/origin_cloud_regions/methods/bulk_delete)

DELETE/zones/{zone_id}/origin/cloud_regions/batch

##### [List supported cloud vendors and regions](https://developers.cloudflare.com/api/resources/cache/subresources/origin_cloud_regions/methods/supported_regions)

GET/zones/{zone_id}/origin/cloud_regions/supported_regions

##### [List origin cloud region mappings](https://developers.cloudflare.com/api/resources/cache/subresources/origin_cloud_regions/methods/list_v1)

Deprecated

GET/zones/{zone_id}/cache/origin_cloud_regions

##### [Create an origin cloud region mapping](https://developers.cloudflare.com/api/resources/cache/subresources/origin_cloud_regions/methods/create_v1)

Deprecated

POST/zones/{zone_id}/cache/origin_cloud_regions

##### [Create or update an origin cloud region mapping](https://developers.cloudflare.com/api/resources/cache/subresources/origin_cloud_regions/methods/edit_v1)

Deprecated

PATCH/zones/{zone_id}/cache/origin_cloud_regions

##### [Get an origin cloud region mapping](https://developers.cloudflare.com/api/resources/cache/subresources/origin_cloud_regions/methods/get_v1)

Deprecated

GET/zones/{zone_id}/cache/origin_cloud_regions/{origin_ip}

##### [Delete an origin cloud region mapping](https://developers.cloudflare.com/api/resources/cache/subresources/origin_cloud_regions/methods/delete_v1)

Deprecated

DELETE/zones/{zone_id}/cache/origin_cloud_regions/{origin_ip}

##### [Batch create or update origin cloud region mappings](https://developers.cloudflare.com/api/resources/cache/subresources/origin_cloud_regions/methods/bulk_edit_v1)

Deprecated

PATCH/zones/{zone_id}/cache/origin_cloud_regions/batch

##### [Batch delete origin cloud region mappings](https://developers.cloudflare.com/api/resources/cache/subresources/origin_cloud_regions/methods/bulk_delete_v1)

Deprecated

DELETE/zones/{zone_id}/cache/origin_cloud_regions/batch

##### [List supported cloud vendors and regions](https://developers.cloudflare.com/api/resources/cache/subresources/origin_cloud_regions/methods/supported_regions_v1)

Deprecated

GET/zones/{zone_id}/cache/origin_cloud_regions/supported_regions

#### SSL

#### SSLAnalyze

##### [Analyze Certificate](https://developers.cloudflare.com/api/resources/ssl/subresources/analyze/methods/create)

POST/zones/{zone_id}/ssl/analyze

#### SSLCertificate Packs

##### [List Certificate Packs](https://developers.cloudflare.com/api/resources/ssl/subresources/certificate_packs/methods/list)

GET/zones/{zone_id}/ssl/certificate_packs

##### [Get Certificate Pack](https://developers.cloudflare.com/api/resources/ssl/subresources/certificate_packs/methods/get)

GET/zones/{zone_id}/ssl/certificate_packs/{certificate_pack_id}

##### [Order Advanced Certificate Manager Certificate Pack](https://developers.cloudflare.com/api/resources/ssl/subresources/certificate_packs/methods/create)

POST/zones/{zone_id}/ssl/certificate_packs/order

##### [Restart Validation or Update Advanced Certificate Manager Certificate Pack](https://developers.cloudflare.com/api/resources/ssl/subresources/certificate_packs/methods/edit)

PATCH/zones/{zone_id}/ssl/certificate_packs/{certificate_pack_id}

##### [Delete Advanced Certificate Manager Certificate Pack](https://developers.cloudflare.com/api/resources/ssl/subresources/certificate_packs/methods/delete)

DELETE/zones/{zone_id}/ssl/certificate_packs/{certificate_pack_id}

#### SSLCertificate PacksQuota

##### [Get Certificate Pack Quotas](https://developers.cloudflare.com/api/resources/ssl/subresources/certificate_packs/subresources/quota/methods/get)

GET/zones/{zone_id}/ssl/certificate_packs/quota

#### SSLRecommendations

##### [SSL/TLS Recommendation](https://developers.cloudflare.com/api/resources/ssl/subresources/recommendations/methods/get)

Deprecated

GET/zones/{zone_id}/ssl/recommendation

#### SSLAutomatic Upgrader

##### [Get Automatic SSL/TLS enrollment status for the given zone](https://developers.cloudflare.com/api/resources/ssl/subresources/automatic_upgrader/methods/get)

GET/zones/{zone_id}/settings/ssl_automatic_mode

##### [Patch Automatic SSL/TLS Enrollment status for given zone](https://developers.cloudflare.com/api/resources/ssl/subresources/automatic_upgrader/methods/patch)

PATCH/zones/{zone_id}/settings/ssl_automatic_mode

#### SSLAuto Origin TLS Kex

##### [Get Auto-Origin TLS KEX enrollment status for the given zone](https://developers.cloudflare.com/api/resources/ssl/subresources/auto_origin_tls_kex/methods/get)

GET/zones/{zone_id}/settings/auto_origin_tls_kex

##### [Patch Auto-Origin TLS KEX enrollment status for the given zone](https://developers.cloudflare.com/api/resources/ssl/subresources/auto_origin_tls_kex/methods/edit)

PATCH/zones/{zone_id}/settings/auto_origin_tls_kex

#### SSLUniversal

#### SSLUniversalSettings

##### [Universal SSL Settings Details](https://developers.cloudflare.com/api/resources/ssl/subresources/universal/subresources/settings/methods/get)

GET/zones/{zone_id}/ssl/universal/settings

##### [Edit Universal SSL Settings](https://developers.cloudflare.com/api/resources/ssl/subresources/universal/subresources/settings/methods/edit)

PATCH/zones/{zone_id}/ssl/universal/settings

#### SSLVerification

##### [SSL Verification Details](https://developers.cloudflare.com/api/resources/ssl/subresources/verification/methods/get)

GET/zones/{zone_id}/ssl/verification

##### [Edit SSL Certificate Pack Validation Method](https://developers.cloudflare.com/api/resources/ssl/subresources/verification/methods/edit)

PATCH/zones/{zone_id}/ssl/verification/{certificate_pack_id}

#### ACM

#### ACMTotal TLS

##### [Total TLS Settings Details](https://developers.cloudflare.com/api/resources/acm/subresources/total_tls/methods/get)

GET/zones/{zone_id}/acm/total_tls

##### [Enable or Disable Total TLS](https://developers.cloudflare.com/api/resources/acm/subresources/total_tls/methods/update)

POST/zones/{zone_id}/acm/total_tls

##### [Enable or Disable Total TLS](https://developers.cloudflare.com/api/resources/acm/subresources/total_tls/methods/edit)

POST/zones/{zone_id}/acm/total_tls

#### ACMCustom Trust Store

##### [List Custom Origin Trust Store Details](https://developers.cloudflare.com/api/resources/acm/subresources/custom_trust_store/methods/list)

GET/zones/{zone_id}/acm/custom_trust_store

##### [Upload Custom Origin Trust Store](https://developers.cloudflare.com/api/resources/acm/subresources/custom_trust_store/methods/create)

POST/zones/{zone_id}/acm/custom_trust_store

##### [Custom Origin Trust Store Details](https://developers.cloudflare.com/api/resources/acm/subresources/custom_trust_store/methods/get)

GET/zones/{zone_id}/acm/custom_trust_store/{custom_origin_trust_store_id}

##### [Delete Custom Origin Trust Store](https://developers.cloudflare.com/api/resources/acm/subresources/custom_trust_store/methods/delete)

DELETE/zones/{zone_id}/acm/custom_trust_store/{custom_origin_trust_store_id}

#### Analytics Query

##### [Query analytics summary](https://developers.cloudflare.com/api/resources/analytics_query/methods/summary)

POST/accounts/{account_id}/analytics/query/{dataset}/summary

##### [Query analytics timeseries](https://developers.cloudflare.com/api/resources/analytics_query/methods/timeseries)

POST/accounts/{account_id}/analytics/query/{dataset}/timeseries

##### [Query analytics top-N](https://developers.cloudflare.com/api/resources/analytics_query/methods/top_n)

POST/accounts/{account_id}/analytics/query/{dataset}/top-n

#### Analytics QueryData Security

#### Analytics QueryData SecurityContent Findings

##### [Top integrations by content findings](https://developers.cloudflare.com/api/resources/analytics_query/subresources/data_security/subresources/content_findings/methods/top_n)

POST/accounts/{account_id}/analytics/query/data-security/content-findings/top-n

#### Analytics QueryData SecurityFindings

##### [Data security findings summary](https://developers.cloudflare.com/api/resources/analytics_query/subresources/data_security/subresources/findings/methods/summary)

POST/accounts/{account_id}/analytics/query/data-security/findings/summary

##### [Data security findings timeseries](https://developers.cloudflare.com/api/resources/analytics_query/subresources/data_security/subresources/findings/methods/timeseries)

POST/accounts/{account_id}/analytics/query/data-security/findings/timeseries

#### Argo

#### ArgoSmart Routing

##### [Get Argo Smart Routing setting](https://developers.cloudflare.com/api/resources/argo/subresources/smart_routing/methods/get)

GET/zones/{zone_id}/argo/smart_routing

##### [Patch Argo Smart Routing setting](https://developers.cloudflare.com/api/resources/argo/subresources/smart_routing/methods/edit)

PATCH/zones/{zone_id}/argo/smart_routing

#### ArgoTiered Caching

##### [Get Tiered Caching setting](https://developers.cloudflare.com/api/resources/argo/subresources/tiered_caching/methods/get)

GET/zones/{zone_id}/argo/tiered_caching

##### [Patch Tiered Caching setting](https://developers.cloudflare.com/api/resources/argo/subresources/tiered_caching/methods/edit)

PATCH/zones/{zone_id}/argo/tiered_caching

#### Certificate Authorities

#### Certificate AuthoritiesHostname Associations

##### [List Hostname Associations](https://developers.cloudflare.com/api/resources/certificate_authorities/subresources/hostname_associations/methods/get)

GET/zones/{zone_id}/certificate_authorities/hostname_associations

##### [Replace Hostname Associations](https://developers.cloudflare.com/api/resources/certificate_authorities/subresources/hostname_associations/methods/update)

PUT/zones/{zone_id}/certificate_authorities/hostname_associations

#### Client Certificates

##### [List Client Certificates](https://developers.cloudflare.com/api/resources/client_certificates/methods/list)

GET/zones/{zone_id}/client_certificates

##### [Client Certificate Details](https://developers.cloudflare.com/api/resources/client_certificates/methods/get)

GET/zones/{zone_id}/client_certificates/{client_certificate_id}

##### [Create Client Certificate](https://developers.cloudflare.com/api/resources/client_certificates/methods/create)

POST/zones/{zone_id}/client_certificates

##### [Reactivate Client Certificate](https://developers.cloudflare.com/api/resources/client_certificates/methods/edit)

PATCH/zones/{zone_id}/client_certificates/{client_certificate_id}

##### [Revoke Client Certificate](https://developers.cloudflare.com/api/resources/client_certificates/methods/delete)

DELETE/zones/{zone_id}/client_certificates/{client_certificate_id}

#### Custom Certificates

##### [List SSL Configurations](https://developers.cloudflare.com/api/resources/custom_certificates/methods/list)

GET/zones/{zone_id}/custom_certificates

##### [SSL Configuration Details](https://developers.cloudflare.com/api/resources/custom_certificates/methods/get)

GET/zones/{zone_id}/custom_certificates/{custom_certificate_id}

##### [Create SSL Configuration](https://developers.cloudflare.com/api/resources/custom_certificates/methods/create)

POST/zones/{zone_id}/custom_certificates

##### [Edit SSL Configuration](https://developers.cloudflare.com/api/resources/custom_certificates/methods/edit)

PATCH/zones/{zone_id}/custom_certificates/{custom_certificate_id}

##### [Delete SSL Configuration](https://developers.cloudflare.com/api/resources/custom_certificates/methods/delete)

DELETE/zones/{zone_id}/custom_certificates/{custom_certificate_id}

#### Custom CertificatesPrioritize

##### [Re-prioritize SSL Certificates](https://developers.cloudflare.com/api/resources/custom_certificates/subresources/prioritize/methods/update)

PUT/zones/{zone_id}/custom_certificates/prioritize

#### Custom Csrs

##### [List Custom CSRs](https://developers.cloudflare.com/api/resources/custom_csrs/methods/list)

GET/{accounts_or_zones}/{account_or_zone_id}/custom_csrs

##### [Create Custom CSR](https://developers.cloudflare.com/api/resources/custom_csrs/methods/create)

POST/{accounts_or_zones}/{account_or_zone_id}/custom_csrs

##### [Custom CSR Details](https://developers.cloudflare.com/api/resources/custom_csrs/methods/get)

GET/{accounts_or_zones}/{account_or_zone_id}/custom_csrs/{custom_csr_id}

##### [Delete Custom CSR](https://developers.cloudflare.com/api/resources/custom_csrs/methods/delete)

DELETE/{accounts_or_zones}/{account_or_zone_id}/custom_csrs/{custom_csr_id}

#### Custom Hostnames

##### [List Custom Hostnames](https://developers.cloudflare.com/api/resources/custom_hostnames/methods/list)

GET/zones/{zone_id}/custom_hostnames

##### [Custom Hostname Details](https://developers.cloudflare.com/api/resources/custom_hostnames/methods/get)

GET/zones/{zone_id}/custom_hostnames/{custom_hostname_id}

##### [Create Custom Hostname](https://developers.cloudflare.com/api/resources/custom_hostnames/methods/create)

POST/zones/{zone_id}/custom_hostnames

##### [Edit Custom Hostname](https://developers.cloudflare.com/api/resources/custom_hostnames/methods/edit)

PATCH/zones/{zone_id}/custom_hostnames/{custom_hostname_id}

##### [Delete Custom Hostname (and any issued SSL certificates)](https://developers.cloudflare.com/api/resources/custom_hostnames/methods/delete)

DELETE/zones/{zone_id}/custom_hostnames/{custom_hostname_id}

#### Custom HostnamesFallback Origin

##### [Get Fallback Origin for Custom Hostnames](https://developers.cloudflare.com/api/resources/custom_hostnames/subresources/fallback_origin/methods/get)

GET/zones/{zone_id}/custom_hostnames/fallback_origin

##### [Update Fallback Origin for Custom Hostnames](https://developers.cloudflare.com/api/resources/custom_hostnames/subresources/fallback_origin/methods/update)

PUT/zones/{zone_id}/custom_hostnames/fallback_origin

##### [Delete Fallback Origin for Custom Hostnames](https://developers.cloudflare.com/api/resources/custom_hostnames/subresources/fallback_origin/methods/delete)

DELETE/zones/{zone_id}/custom_hostnames/fallback_origin

#### Custom HostnamesCertificate Pack

#### Custom HostnamesCertificate PackCertificates

##### [Replace Custom Certificate and Custom Key In Custom Hostname](https://developers.cloudflare.com/api/resources/custom_hostnames/subresources/certificate_pack/subresources/certificates/methods/update)

PUT/zones/{zone_id}/custom_hostnames/{custom_hostname_id}/certificate_pack/{certificate_pack_id}/certificates/{certificate_id}

##### [Delete Single Certificate And Key For Custom Hostname](https://developers.cloudflare.com/api/resources/custom_hostnames/subresources/certificate_pack/subresources/certificates/methods/delete)

DELETE/zones/{zone_id}/custom_hostnames/{custom_hostname_id}/certificate_pack/{certificate_pack_id}/certificates/{certificate_id}

#### Custom HostnamesQuota

##### [Get Custom Hostname Quota](https://developers.cloudflare.com/api/resources/custom_hostnames/subresources/quota/methods/get)

GET/zones/{zone_id}/custom_hostnames/quota

#### Account Custom Nameservers

##### [List Account Custom Nameservers](https://developers.cloudflare.com/api/resources/custom_nameservers/methods/get)

GET/accounts/{account_id}/custom_ns

##### [Add Account Custom Nameserver](https://developers.cloudflare.com/api/resources/custom_nameservers/methods/create)

POST/accounts/{account_id}/custom_ns

##### [Delete Account Custom Nameserver](https://developers.cloudflare.com/api/resources/custom_nameservers/methods/delete)

DELETE/accounts/{account_id}/custom_ns/{custom_ns_id}

#### Tenant Custom Nameservers

##### [List Tenant Custom Nameservers](https://developers.cloudflare.com/api/resources/tenant_custom_nameservers/methods/get)

GET/tenants/{tenant_tag}/custom_ns

##### [Add Tenant Custom Nameserver](https://developers.cloudflare.com/api/resources/tenant_custom_nameservers/methods/create)

POST/tenants/{tenant_tag}/custom_ns

##### [Delete Tenant Custom Nameserver](https://developers.cloudflare.com/api/resources/tenant_custom_nameservers/methods/delete)

DELETE/tenants/{tenant_tag}/custom_ns/{custom_ns_id}

#### DNS Firewall

##### [List DNS Firewall Clusters](https://developers.cloudflare.com/api/resources/dns_firewall/methods/list)

GET/accounts/{account_id}/dns_firewall

##### [DNS Firewall Cluster Details](https://developers.cloudflare.com/api/resources/dns_firewall/methods/get)

GET/accounts/{account_id}/dns_firewall/{dns_firewall_id}

##### [Create DNS Firewall Cluster](https://developers.cloudflare.com/api/resources/dns_firewall/methods/create)

POST/accounts/{account_id}/dns_firewall

##### [Update DNS Firewall Cluster](https://developers.cloudflare.com/api/resources/dns_firewall/methods/edit)

PATCH/accounts/{account_id}/dns_firewall/{dns_firewall_id}

##### [Delete DNS Firewall Cluster](https://developers.cloudflare.com/api/resources/dns_firewall/methods/delete)

DELETE/accounts/{account_id}/dns_firewall/{dns_firewall_id}

#### DNS FirewallAnalytics

#### DNS FirewallAnalyticsReports

##### [Table](https://developers.cloudflare.com/api/resources/dns_firewall/subresources/analytics/subresources/reports/methods/get)

Deprecated

GET/accounts/{account_id}/dns_firewall/{dns_firewall_id}/dns_analytics/report

#### DNS FirewallAnalyticsReportsBytimes

##### [By Time](https://developers.cloudflare.com/api/resources/dns_firewall/subresources/analytics/subresources/reports/subresources/bytimes/methods/get)

Deprecated

GET/accounts/{account_id}/dns_firewall/{dns_firewall_id}/dns_analytics/report/bytime

#### DNS FirewallReverse DNS

##### [Show DNS Firewall Cluster Reverse DNS](https://developers.cloudflare.com/api/resources/dns_firewall/subresources/reverse_dns/methods/get)

GET/accounts/{account_id}/dns_firewall/{dns_firewall_id}/reverse_dns

##### [Update DNS Firewall Cluster Reverse DNS](https://developers.cloudflare.com/api/resources/dns_firewall/subresources/reverse_dns/methods/edit)

PATCH/accounts/{account_id}/dns_firewall/{dns_firewall_id}/reverse_dns

#### DNS

#### DNSDNSSEC

##### [DNSSEC Details](https://developers.cloudflare.com/api/resources/dns/subresources/dnssec/methods/get)

GET/zones/{zone_id}/dnssec

##### [Edit DNSSEC Status](https://developers.cloudflare.com/api/resources/dns/subresources/dnssec/methods/edit)

PATCH/zones/{zone_id}/dnssec

##### [Delete DNSSEC records](https://developers.cloudflare.com/api/resources/dns/subresources/dnssec/methods/delete)

DELETE/zones/{zone_id}/dnssec

#### DNSDNSSECZsk

##### [List DNSSEC ZSKs](https://developers.cloudflare.com/api/resources/dns/subresources/dnssec/subresources/zsk/methods/list)

GET/zones/{zone_id}/dnssec/zsk

#### DNSRecords

##### [List DNS Records](https://developers.cloudflare.com/api/resources/dns/subresources/records/methods/list)

GET/zones/{zone_id}/dns_records

##### [DNS Record Details](https://developers.cloudflare.com/api/resources/dns/subresources/records/methods/get)

GET/zones/{zone_id}/dns_records/{dns_record_id}

##### [Create DNS Record](https://developers.cloudflare.com/api/resources/dns/subresources/records/methods/create)

POST/zones/{zone_id}/dns_records

##### [Overwrite DNS Record](https://developers.cloudflare.com/api/resources/dns/subresources/records/methods/update)

PUT/zones/{zone_id}/dns_records/{dns_record_id}

##### [Update DNS Record](https://developers.cloudflare.com/api/resources/dns/subresources/records/methods/edit)

PATCH/zones/{zone_id}/dns_records/{dns_record_id}

##### [Delete DNS Record](https://developers.cloudflare.com/api/resources/dns/subresources/records/methods/delete)

DELETE/zones/{zone_id}/dns_records/{dns_record_id}

##### [Export DNS Records](https://developers.cloudflare.com/api/resources/dns/subresources/records/methods/export)

GET/zones/{zone_id}/dns_records/export

##### [Import DNS Records](https://developers.cloudflare.com/api/resources/dns/subresources/records/methods/import)

POST/zones/{zone_id}/dns_records/import

##### [Scan DNS Records](https://developers.cloudflare.com/api/resources/dns/subresources/records/methods/scan)

Deprecated

POST/zones/{zone_id}/dns_records/scan

##### [Trigger DNS Record Scan](https://developers.cloudflare.com/api/resources/dns/subresources/records/methods/scan_trigger)

POST/zones/{zone_id}/dns_records/scan/trigger

##### [Review Scanned DNS Records](https://developers.cloudflare.com/api/resources/dns/subresources/records/methods/scan_review)

POST/zones/{zone_id}/dns_records/scan/review

##### [List Scanned DNS Records](https://developers.cloudflare.com/api/resources/dns/subresources/records/methods/scan_list)

GET/zones/{zone_id}/dns_records/scan/review

##### [Batch DNS Records](https://developers.cloudflare.com/api/resources/dns/subresources/records/methods/batch)

POST/zones/{zone_id}/dns_records/batch

#### DNSUsage

#### DNSUsageZone

##### [Get DNS Record Usage](https://developers.cloudflare.com/api/resources/dns/subresources/usage/subresources/zone/methods/get)

GET/zones/{zone_id}/dns_records/usage

#### DNSUsageAccount

##### [Get DNS Record Usage for Account](https://developers.cloudflare.com/api/resources/dns/subresources/usage/subresources/account/methods/get)

GET/accounts/{account_id}/dns_records/usage

#### DNSSettings

#### DNSSettingsZone

##### [Show DNS Settings](https://developers.cloudflare.com/api/resources/dns/subresources/settings/subresources/zone/methods/get)

GET/zones/{zone_id}/dns_settings

##### [Update DNS Settings](https://developers.cloudflare.com/api/resources/dns/subresources/settings/subresources/zone/methods/edit)

PATCH/zones/{zone_id}/dns_settings

#### DNSSettingsAccount

##### [Show DNS Settings](https://developers.cloudflare.com/api/resources/dns/subresources/settings/subresources/account/methods/get)

GET/accounts/{account_id}/dns_settings

##### [Update DNS Settings](https://developers.cloudflare.com/api/resources/dns/subresources/settings/subresources/account/methods/edit)

PATCH/accounts/{account_id}/dns_settings

#### DNSSettingsAccountNameserver Sets

##### [List Custom Nameserver Sets](https://developers.cloudflare.com/api/resources/dns/subresources/settings/subresources/account/subresources/nameserver_sets/methods/list)

GET/accounts/{account_id}/dns_settings/nameserver_sets

##### [Get Custom Nameserver Set](https://developers.cloudflare.com/api/resources/dns/subresources/settings/subresources/account/subresources/nameserver_sets/methods/get)

GET/accounts/{account_id}/dns_settings/nameserver_sets/{nameserver_set_id}

##### [Create Custom Nameserver Set](https://developers.cloudflare.com/api/resources/dns/subresources/settings/subresources/account/subresources/nameserver_sets/methods/create)

POST/accounts/{account_id}/dns_settings/nameserver_sets

##### [Delete Custom Nameserver Set](https://developers.cloudflare.com/api/resources/dns/subresources/settings/subresources/account/subresources/nameserver_sets/methods/delete)

DELETE/accounts/{account_id}/dns_settings/nameserver_sets/{nameserver_set_id}

#### DNSSettingsAccountViews

##### [List Internal DNS Views](https://developers.cloudflare.com/api/resources/dns/subresources/settings/subresources/account/subresources/views/methods/list)

GET/accounts/{account_id}/dns_settings/views

##### [DNS Internal View Details](https://developers.cloudflare.com/api/resources/dns/subresources/settings/subresources/account/subresources/views/methods/get)

GET/accounts/{account_id}/dns_settings/views/{view_id}

##### [Create Internal DNS View](https://developers.cloudflare.com/api/resources/dns/subresources/settings/subresources/account/subresources/views/methods/create)

POST/accounts/{account_id}/dns_settings/views

##### [Update Internal DNS View](https://developers.cloudflare.com/api/resources/dns/subresources/settings/subresources/account/subresources/views/methods/edit)

PATCH/accounts/{account_id}/dns_settings/views/{view_id}

##### [Delete Internal DNS View](https://developers.cloudflare.com/api/resources/dns/subresources/settings/subresources/account/subresources/views/methods/delete)

DELETE/accounts/{account_id}/dns_settings/views/{view_id}

#### DNSAnalytics

#### DNSAnalyticsReports

##### [Table](https://developers.cloudflare.com/api/resources/dns/subresources/analytics/subresources/reports/methods/get)

Deprecated

GET/zones/{zone_id}/dns_analytics/report

#### DNSAnalyticsReportsBytimes

##### [By Time](https://developers.cloudflare.com/api/resources/dns/subresources/analytics/subresources/reports/subresources/bytimes/methods/get)

Deprecated

GET/zones/{zone_id}/dns_analytics/report/bytime

#### DNSZone Transfers

#### DNSZone TransfersForce AXFR

##### [Force AXFR](https://developers.cloudflare.com/api/resources/dns/subresources/zone_transfers/subresources/force_axfr/methods/create)

POST/zones/{zone_id}/secondary_dns/force_axfr

#### DNSZone TransfersIncoming

##### [Secondary Zone Configuration Details](https://developers.cloudflare.com/api/resources/dns/subresources/zone_transfers/subresources/incoming/methods/get)

GET/zones/{zone_id}/secondary_dns/incoming

##### [Create Secondary Zone Configuration](https://developers.cloudflare.com/api/resources/dns/subresources/zone_transfers/subresources/incoming/methods/create)

POST/zones/{zone_id}/secondary_dns/incoming

##### [Update Secondary Zone Configuration](https://developers.cloudflare.com/api/resources/dns/subresources/zone_transfers/subresources/incoming/methods/update)

PUT/zones/{zone_id}/secondary_dns/incoming

##### [Delete Secondary Zone Configuration](https://developers.cloudflare.com/api/resources/dns/subresources/zone_transfers/subresources/incoming/methods/delete)

DELETE/zones/{zone_id}/secondary_dns/incoming

#### DNSZone TransfersOutgoing

##### [Primary Zone Configuration Details](https://developers.cloudflare.com/api/resources/dns/subresources/zone_transfers/subresources/outgoing/methods/get)

GET/zones/{zone_id}/secondary_dns/outgoing

##### [Create Primary Zone Configuration](https://developers.cloudflare.com/api/resources/dns/subresources/zone_transfers/subresources/outgoing/methods/create)

POST/zones/{zone_id}/secondary_dns/outgoing

##### [Update Primary Zone Configuration](https://developers.cloudflare.com/api/resources/dns/subresources/zone_transfers/subresources/outgoing/methods/update)

PUT/zones/{zone_id}/secondary_dns/outgoing

##### [Delete Primary Zone Configuration](https://developers.cloudflare.com/api/resources/dns/subresources/zone_transfers/subresources/outgoing/methods/delete)

DELETE/zones/{zone_id}/secondary_dns/outgoing

##### [Disable Outgoing Zone Transfers](https://developers.cloudflare.com/api/resources/dns/subresources/zone_transfers/subresources/outgoing/methods/disable)

POST/zones/{zone_id}/secondary_dns/outgoing/disable

##### [Enable Outgoing Zone Transfers](https://developers.cloudflare.com/api/resources/dns/subresources/zone_transfers/subresources/outgoing/methods/enable)

POST/zones/{zone_id}/secondary_dns/outgoing/enable

##### [Force DNS NOTIFY](https://developers.cloudflare.com/api/resources/dns/subresources/zone_transfers/subresources/outgoing/methods/force_notify)

POST/zones/{zone_id}/secondary_dns/outgoing/force_notify

#### DNSZone TransfersOutgoingStatus

##### [Get Outgoing Zone Transfer Status](https://developers.cloudflare.com/api/resources/dns/subresources/zone_transfers/subresources/outgoing/subresources/status/methods/get)

GET/zones/{zone_id}/secondary_dns/outgoing/status

#### DNSZone TransfersACLs

##### [List ACLs](https://developers.cloudflare.com/api/resources/dns/subresources/zone_transfers/subresources/acls/methods/list)

GET/accounts/{account_id}/secondary_dns/acls

##### [ACL Details](https://developers.cloudflare.com/api/resources/dns/subresources/zone_transfers/subresources/acls/methods/get)

GET/accounts/{account_id}/secondary_dns/acls/{acl_id}

##### [Create ACL](https://developers.cloudflare.com/api/resources/dns/subresources/zone_transfers/subresources/acls/methods/create)

POST/accounts/{account_id}/secondary_dns/acls

##### [Update ACL](https://developers.cloudflare.com/api/resources/dns/subresources/zone_transfers/subresources/acls/methods/update)

PUT/accounts/{account_id}/secondary_dns/acls/{acl_id}

##### [Delete ACL](https://developers.cloudflare.com/api/resources/dns/subresources/zone_transfers/subresources/acls/methods/delete)

DELETE/accounts/{account_id}/secondary_dns/acls/{acl_id}

#### DNSZone TransfersPeers

##### [List Peers](https://developers.cloudflare.com/api/resources/dns/subresources/zone_transfers/subresources/peers/methods/list)

GET/accounts/{account_id}/secondary_dns/peers

##### [Peer Details](https://developers.cloudflare.com/api/resources/dns/subresources/zone_transfers/subresources/peers/methods/get)

GET/accounts/{account_id}/secondary_dns/peers/{peer_id}

##### [Create Peer](https://developers.cloudflare.com/api/resources/dns/subresources/zone_transfers/subresources/peers/methods/create)

POST/accounts/{account_id}/secondary_dns/peers

##### [Update Peer](https://developers.cloudflare.com/api/resources/dns/subresources/zone_transfers/subresources/peers/methods/update)

PUT/accounts/{account_id}/secondary_dns/peers/{peer_id}

##### [Delete Peer](https://developers.cloudflare.com/api/resources/dns/subresources/zone_transfers/subresources/peers/methods/delete)

DELETE/accounts/{account_id}/secondary_dns/peers/{peer_id}

#### DNSZone TransfersTSIGs

##### [List TSIGs](https://developers.cloudflare.com/api/resources/dns/subresources/zone_transfers/subresources/tsigs/methods/list)

GET/accounts/{account_id}/secondary_dns/tsigs

##### [TSIG Details](https://developers.cloudflare.com/api/resources/dns/subresources/zone_transfers/subresources/tsigs/methods/get)

GET/accounts/{account_id}/secondary_dns/tsigs/{tsig_id}

##### [Create TSIG](https://developers.cloudflare.com/api/resources/dns/subresources/zone_transfers/subresources/tsigs/methods/create)

POST/accounts/{account_id}/secondary_dns/tsigs

##### [Update TSIG](https://developers.cloudflare.com/api/resources/dns/subresources/zone_transfers/subresources/tsigs/methods/update)

PUT/accounts/{account_id}/secondary_dns/tsigs/{tsig_id}

##### [Delete TSIG](https://developers.cloudflare.com/api/resources/dns/subresources/zone_transfers/subresources/tsigs/methods/delete)

DELETE/accounts/{account_id}/secondary_dns/tsigs/{tsig_id}

#### Email Security

#### Email SecurityInvestigate

##### [Search email messages](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/methods/list)

GET/accounts/{account_id}/email-security/investigate

##### [Get message details](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/methods/get)

GET/accounts/{account_id}/email-security/investigate/{investigate_id}

#### Email SecurityInvestigateDetections

##### [Get message detection details](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/detections/methods/get)

GET/accounts/{account_id}/email-security/investigate/{investigate_id}/detections

#### Email SecurityInvestigatePreview

##### [Get preview for a detection](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/preview/methods/get)

GET/accounts/{account_id}/email-security/investigate/{investigate_id}/preview

##### [Generate preview for a non-detection message](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/preview/methods/create)

POST/accounts/{account_id}/email-security/investigate/preview

#### Email SecurityInvestigateRaw

##### [Get raw email content](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/raw/methods/get)

GET/accounts/{account_id}/email-security/investigate/{investigate_id}/raw

#### Email SecurityInvestigateTrace

##### [Get email trace](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/trace/methods/get)

GET/accounts/{account_id}/email-security/investigate/{investigate_id}/trace

#### Email SecurityInvestigateMove

##### [Move a message](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/move/methods/create)

POST/accounts/{account_id}/email-security/investigate/{investigate_id}/move

##### [Move messages](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/move/methods/bulk)

POST/accounts/{account_id}/email-security/investigate/move

#### Email SecurityInvestigateReclassify

##### [Change email classification](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/reclassify/methods/create)

Deprecated

POST/accounts/{account_id}/email-security/investigate/{investigate_id}/reclassify

#### Email SecurityInvestigateRelease

##### [Release messages from quarantine](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/release/methods/bulk)

POST/accounts/{account_id}/email-security/investigate/release

#### Email SecurityInvestigateBulk

##### [List bulk action jobs](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/bulk/methods/list)

GET/accounts/{account_id}/email-security/investigate/bulk

##### [Create a bulk action job](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/bulk/methods/create)

POST/accounts/{account_id}/email-security/investigate/bulk

##### [Get bulk action job details](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/bulk/methods/get)

GET/accounts/{account_id}/email-security/investigate/bulk/{job_id}

##### [Delete a bulk action job](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/bulk/methods/delete)

DELETE/accounts/{account_id}/email-security/investigate/bulk/{job_id}

#### Email SecurityInvestigateBulkCancel

##### [Cancel a bulk action job](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/bulk/subresources/cancel/methods/create)

POST/accounts/{account_id}/email-security/investigate/bulk/{job_id}/cancel

#### Email SecurityInvestigateBulkMessages

##### [List messages for a bulk action job](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/bulk/subresources/messages/methods/list)

GET/accounts/{account_id}/email-security/investigate/bulk/{job_id}/messages

#### Email SecurityPhishguard

#### Email SecurityPhishguardReports

##### [List PhishGuard reports](https://developers.cloudflare.com/api/resources/email_security/subresources/phishguard/subresources/reports/methods/list)

GET/accounts/{account_id}/email-security/phishguard/reports

#### Email SecuritySettings

#### Email SecuritySettingsAllow Policies

##### [List email allow policies](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/allow_policies/methods/list)

GET/accounts/{account_id}/email-security/settings/allow_policies

##### [Get an email allow policy](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/allow_policies/methods/get)

GET/accounts/{account_id}/email-security/settings/allow_policies/{policy_id}

##### [Create email allow policy](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/allow_policies/methods/create)

POST/accounts/{account_id}/email-security/settings/allow_policies

##### [Update an email allow policy](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/allow_policies/methods/edit)

PATCH/accounts/{account_id}/email-security/settings/allow_policies/{policy_id}

##### [Delete an email allow policy](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/allow_policies/methods/delete)

DELETE/accounts/{account_id}/email-security/settings/allow_policies/{policy_id}

##### [Batch allow policy operations](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/allow_policies/methods/batch)

POST/accounts/{account_id}/email-security/settings/allow_policies/batch

#### Email SecuritySettingsBlock Senders

##### [List blocked email senders](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/block_senders/methods/list)

GET/accounts/{account_id}/email-security/settings/block_senders

##### [Get a blocked email sender](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/block_senders/methods/get)

GET/accounts/{account_id}/email-security/settings/block_senders/{pattern_id}

##### [Create blocked email sender](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/block_senders/methods/create)

POST/accounts/{account_id}/email-security/settings/block_senders

##### [Update a blocked email sender](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/block_senders/methods/edit)

PATCH/accounts/{account_id}/email-security/settings/block_senders/{pattern_id}

##### [Delete a blocked email sender](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/block_senders/methods/delete)

DELETE/accounts/{account_id}/email-security/settings/block_senders/{pattern_id}

##### [Batch blocked sender operations](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/block_senders/methods/batch)

POST/accounts/{account_id}/email-security/settings/block_senders/batch

#### Email SecuritySettingsContent Policies

##### [List content policies](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/content_policies/methods/list)

GET/accounts/{account_id}/email-security/settings/content_policies

##### [Get a content policy](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/content_policies/methods/get)

GET/accounts/{account_id}/email-security/settings/content_policies/{policy_id}

##### [Create a content policy](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/content_policies/methods/create)

POST/accounts/{account_id}/email-security/settings/content_policies

##### [Update a content policy](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/content_policies/methods/edit)

PATCH/accounts/{account_id}/email-security/settings/content_policies/{policy_id}

##### [Delete a content policy](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/content_policies/methods/delete)

DELETE/accounts/{account_id}/email-security/settings/content_policies/{policy_id}

##### [Batch content policy operations](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/content_policies/methods/batch)

POST/accounts/{account_id}/email-security/settings/content_policies/batch

#### Email SecuritySettingsDomains

##### [List protected email domains](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/domains/methods/list)

GET/accounts/{account_id}/email-security/settings/domains

##### [Get an email domain](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/domains/methods/get)

GET/accounts/{account_id}/email-security/settings/domains/{domain_id}

##### [Replace an email domain](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/domains/methods/update)

PUT/accounts/{account_id}/email-security/settings/domains/{domain_id}

##### [Update an email domain](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/domains/methods/edit)

PATCH/accounts/{account_id}/email-security/settings/domains/{domain_id}

##### [Add a new email domain](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/domains/methods/create)

POST/accounts/{account_id}/email-security/settings/domains

##### [Unprotect an email domain](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/domains/methods/delete)

DELETE/accounts/{account_id}/email-security/settings/domains/{domain_id}

##### [Batch domain operations](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/domains/methods/batch)

POST/accounts/{account_id}/email-security/settings/domains/batch

##### [Unprotect multiple email domains](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/domains/methods/bulk_delete)

Deprecated

DELETE/accounts/{account_id}/email-security/settings/domains

#### Email SecuritySettingsImpersonation Registry

##### [List impersonation registry entries](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/impersonation_registry/methods/list)

GET/accounts/{account_id}/email-security/settings/impersonation_registry

##### [Get an impersonation registry entry](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/impersonation_registry/methods/get)

GET/accounts/{account_id}/email-security/settings/impersonation_registry/{impersonation_registry_id}

##### [Create impersonation registry entry](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/impersonation_registry/methods/create)

POST/accounts/{account_id}/email-security/settings/impersonation_registry

##### [Update an impersonation registry entry](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/impersonation_registry/methods/edit)

PATCH/accounts/{account_id}/email-security/settings/impersonation_registry/{impersonation_registry_id}

##### [Delete an impersonation registry entry](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/impersonation_registry/methods/delete)

DELETE/accounts/{account_id}/email-security/settings/impersonation_registry/{impersonation_registry_id}

#### Email SecuritySettingsSending Domain Restrictions

##### [List sending domain restrictions](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/sending_domain_restrictions/methods/list)

GET/accounts/{account_id}/email-security/settings/sending_domain_restrictions

##### [Get a sending domain restriction](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/sending_domain_restrictions/methods/get)

GET/accounts/{account_id}/email-security/settings/sending_domain_restrictions/{sending_domain_restriction_id}

##### [Create a sending domain restriction](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/sending_domain_restrictions/methods/create)

POST/accounts/{account_id}/email-security/settings/sending_domain_restrictions

##### [Update a sending domain restriction](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/sending_domain_restrictions/methods/edit)

PATCH/accounts/{account_id}/email-security/settings/sending_domain_restrictions/{sending_domain_restriction_id}

##### [Delete a sending domain restriction](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/sending_domain_restrictions/methods/delete)

DELETE/accounts/{account_id}/email-security/settings/sending_domain_restrictions/{sending_domain_restriction_id}

#### Email SecuritySettingsTrusted Domains

##### [List trusted email domains](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/trusted_domains/methods/list)

GET/accounts/{account_id}/email-security/settings/trusted_domains

##### [Get a trusted email domain](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/trusted_domains/methods/get)

GET/accounts/{account_id}/email-security/settings/trusted_domains/{trusted_domain_id}

##### [Create trusted email domain](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/trusted_domains/methods/create)

POST/accounts/{account_id}/email-security/settings/trusted_domains

##### [Update a trusted email domain](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/trusted_domains/methods/edit)

PATCH/accounts/{account_id}/email-security/settings/trusted_domains/{trusted_domain_id}

##### [Delete a trusted email domain](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/trusted_domains/methods/delete)

DELETE/accounts/{account_id}/email-security/settings/trusted_domains/{trusted_domain_id}

##### [Batch trusted domain operations](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/trusted_domains/methods/batch)

POST/accounts/{account_id}/email-security/settings/trusted_domains/batch

#### Email SecuritySettingsURL Ignore Patterns

##### [List URL ignore patterns](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/url_ignore_patterns/methods/list)

GET/accounts/{account_id}/email-security/settings/url_ignore_patterns

##### [Get a URL ignore pattern](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/url_ignore_patterns/methods/get)

GET/accounts/{account_id}/email-security/settings/url_ignore_patterns/{pattern_id}

##### [Create a URL ignore pattern](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/url_ignore_patterns/methods/create)

POST/accounts/{account_id}/email-security/settings/url_ignore_patterns

##### [Update a URL ignore pattern](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/url_ignore_patterns/methods/edit)

PATCH/accounts/{account_id}/email-security/settings/url_ignore_patterns/{pattern_id}

##### [Delete a URL ignore pattern](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/url_ignore_patterns/methods/delete)

DELETE/accounts/{account_id}/email-security/settings/url_ignore_patterns/{pattern_id}

#### Email SecuritySubmissions

##### [List reclassify submissions](https://developers.cloudflare.com/api/resources/email_security/subresources/submissions/methods/list)

GET/accounts/{account_id}/email-security/submissions

#### Email Auth

#### Email AuthDMARC Reports

##### [Get DMARC Report Status](https://developers.cloudflare.com/api/resources/email_auth/subresources/dmarc_reports/methods/get)

GET/zones/{zone_id}/email/auth/dmarc-reports

##### [Configure DMARC Reports](https://developers.cloudflare.com/api/resources/email_auth/subresources/dmarc_reports/methods/edit)

PATCH/zones/{zone_id}/email/auth/dmarc-reports

#### Email AuthSPF

#### Email AuthSPFInspect

##### [Inspect SPF Record](https://developers.cloudflare.com/api/resources/email_auth/subresources/spf/subresources/inspect/methods/get)

GET/zones/{zone_id}/email/auth/spf/inspect

#### Email Routing

##### [Get Email Routing settings](https://developers.cloudflare.com/api/resources/email_routing/methods/get)

GET/zones/{zone_id}/email/routing

##### [Update Email Routing settings](https://developers.cloudflare.com/api/resources/email_routing/methods/edit)

PATCH/zones/{zone_id}/email/routing

##### [Apply Email Routing settings](https://developers.cloudflare.com/api/resources/email_routing/methods/update)

PUT/zones/{zone_id}/email/routing

##### [Disable Email Routing](https://developers.cloudflare.com/api/resources/email_routing/methods/disable)

Deprecated

POST/zones/{zone_id}/email/routing/disable

##### [Enable Email Routing](https://developers.cloudflare.com/api/resources/email_routing/methods/enable)

Deprecated

POST/zones/{zone_id}/email/routing/enable

##### [Unlock Email Routing](https://developers.cloudflare.com/api/resources/email_routing/methods/unlock)

Deprecated

POST/zones/{zone_id}/email/routing/unlock

#### Email RoutingDNS

##### [Email Routing - DNS settings](https://developers.cloudflare.com/api/resources/email_routing/subresources/dns/methods/get)

GET/zones/{zone_id}/email/routing/dns

##### [Enable Email Routing](https://developers.cloudflare.com/api/resources/email_routing/subresources/dns/methods/create)

POST/zones/{zone_id}/email/routing/dns

##### [Unlock Email Routing DNS records](https://developers.cloudflare.com/api/resources/email_routing/subresources/dns/methods/edit)

PATCH/zones/{zone_id}/email/routing/dns

##### [Disable Email Routing](https://developers.cloudflare.com/api/resources/email_routing/subresources/dns/methods/delete)

DELETE/zones/{zone_id}/email/routing/dns

#### Email RoutingRules

##### [List account or zone routing rules](https://developers.cloudflare.com/api/resources/email_routing/subresources/rules/methods/list)

GET/{accounts_or_zones}/{account_or_zone_id}/email/routing/rules

##### [Get routing rule](https://developers.cloudflare.com/api/resources/email_routing/subresources/rules/methods/get)

GET/zones/{zone_id}/email/routing/rules/{rule_identifier}

##### [Create routing rule](https://developers.cloudflare.com/api/resources/email_routing/subresources/rules/methods/create)

POST/zones/{zone_id}/email/routing/rules

##### [Update routing rule](https://developers.cloudflare.com/api/resources/email_routing/subresources/rules/methods/update)

PUT/zones/{zone_id}/email/routing/rules/{rule_identifier}

##### [Delete routing rule](https://developers.cloudflare.com/api/resources/email_routing/subresources/rules/methods/delete)

DELETE/zones/{zone_id}/email/routing/rules/{rule_identifier}

#### Email RoutingRulesCatch Alls

##### [Get catch-all rule](https://developers.cloudflare.com/api/resources/email_routing/subresources/rules/subresources/catch_alls/methods/get)

GET/zones/{zone_id}/email/routing/rules/catch_all

##### [Update catch-all rule](https://developers.cloudflare.com/api/resources/email_routing/subresources/rules/subresources/catch_alls/methods/update)

PUT/zones/{zone_id}/email/routing/rules/catch_all

#### Email RoutingAccount Rules

##### [List account or zone routing rules](https://developers.cloudflare.com/api/resources/email_routing/subresources/account_rules/methods/list)

GET/{accounts_or_zones}/{account_or_zone_id}/email/routing/rules

#### Email RoutingAddresses

##### [List destination addresses](https://developers.cloudflare.com/api/resources/email_routing/subresources/addresses/methods/list)

GET/accounts/{account_id}/email/routing/addresses

##### [Get a destination address](https://developers.cloudflare.com/api/resources/email_routing/subresources/addresses/methods/get)

GET/accounts/{account_id}/email/routing/addresses/{destination_address_identifier}

##### [Create a destination address](https://developers.cloudflare.com/api/resources/email_routing/subresources/addresses/methods/create)

POST/accounts/{account_id}/email/routing/addresses

##### [Update destination address](https://developers.cloudflare.com/api/resources/email_routing/subresources/addresses/methods/edit)

PATCH/accounts/{account_id}/email/routing/addresses/{destination_address_identifier}

##### [Delete destination address](https://developers.cloudflare.com/api/resources/email_routing/subresources/addresses/methods/delete)

DELETE/accounts/{account_id}/email/routing/addresses/{destination_address_identifier}

#### Email Sending

##### [Send an email](https://developers.cloudflare.com/api/resources/email_sending/methods/send)

POST/accounts/{account_id}/email/sending/send

##### [Send a raw MIME email](https://developers.cloudflare.com/api/resources/email_sending/methods/send_raw)

POST/accounts/{account_id}/email/sending/send_raw

#### Email SendingSuppressions

##### [List account Email Sending suppressions](https://developers.cloudflare.com/api/resources/email_sending/subresources/suppressions/methods/list)

GET/accounts/{account_id}/email/sending/suppressions

##### [Get account Email Sending suppression](https://developers.cloudflare.com/api/resources/email_sending/subresources/suppressions/methods/get)

GET/accounts/{account_id}/email/sending/suppressions/{suppression_id}

##### [Create account Email Sending suppression](https://developers.cloudflare.com/api/resources/email_sending/subresources/suppressions/methods/create)

POST/accounts/{account_id}/email/sending/suppressions

##### [Update account Email Sending suppression](https://developers.cloudflare.com/api/resources/email_sending/subresources/suppressions/methods/edit)

PATCH/accounts/{account_id}/email/sending/suppressions/{suppression_id}

##### [Delete account Email Sending suppression](https://developers.cloudflare.com/api/resources/email_sending/subresources/suppressions/methods/delete)

DELETE/accounts/{account_id}/email/sending/suppressions/{suppression_id}

##### [Bulk import account Email Sending suppressions](https://developers.cloudflare.com/api/resources/email_sending/subresources/suppressions/methods/import)

POST/accounts/{account_id}/email/sending/suppressions/bulk

#### Email SendingSubdomains

##### [List sending subdomains](https://developers.cloudflare.com/api/resources/email_sending/subresources/subdomains/methods/list)

GET/zones/{zone_id}/email/sending/subdomains

##### [Get a sending subdomain](https://developers.cloudflare.com/api/resources/email_sending/subresources/subdomains/methods/get)

GET/zones/{zone_id}/email/sending/subdomains/{subdomain_id}

##### [Create a sending subdomain](https://developers.cloudflare.com/api/resources/email_sending/subresources/subdomains/methods/create)

POST/zones/{zone_id}/email/sending/subdomains

##### [Update a sending subdomain](https://developers.cloudflare.com/api/resources/email_sending/subresources/subdomains/methods/edit)

PATCH/zones/{zone_id}/email/sending/subdomains/{subdomain_id}

##### [Delete a sending subdomain](https://developers.cloudflare.com/api/resources/email_sending/subresources/subdomains/methods/delete)

DELETE/zones/{zone_id}/email/sending/subdomains/{subdomain_id}

#### Email SendingSubdomainsDNS

##### [Get sending subdomain DNS records](https://developers.cloudflare.com/api/resources/email_sending/subresources/subdomains/subresources/dns/methods/get)

GET/zones/{zone_id}/email/sending/subdomains/{subdomain_id}/dns

#### Filters

##### [List filters](https://developers.cloudflare.com/api/resources/filters/methods/list)

Deprecated

GET/zones/{zone_id}/filters

##### [Get a filter](https://developers.cloudflare.com/api/resources/filters/methods/get)

Deprecated

GET/zones/{zone_id}/filters/{filter_id}

##### [Create filters](https://developers.cloudflare.com/api/resources/filters/methods/create)

Deprecated

POST/zones/{zone_id}/filters

##### [Update a filter](https://developers.cloudflare.com/api/resources/filters/methods/update)

Deprecated

PUT/zones/{zone_id}/filters/{filter_id}

##### [Delete a filter](https://developers.cloudflare.com/api/resources/filters/methods/delete)

Deprecated

DELETE/zones/{zone_id}/filters/{filter_id}

##### [Update filters](https://developers.cloudflare.com/api/resources/filters/methods/bulk_update)

Deprecated

PUT/zones/{zone_id}/filters

##### [Delete filters](https://developers.cloudflare.com/api/resources/filters/methods/bulk_delete)

Deprecated

DELETE/zones/{zone_id}/filters

#### Firewall

#### FirewallLockdowns

##### [List Zone Lockdown rules](https://developers.cloudflare.com/api/resources/firewall/subresources/lockdowns/methods/list)

GET/zones/{zone_id}/firewall/lockdowns

##### [Get a Zone Lockdown rule](https://developers.cloudflare.com/api/resources/firewall/subresources/lockdowns/methods/get)

GET/zones/{zone_id}/firewall/lockdowns/{lock_downs_id}

##### [Create a Zone Lockdown rule](https://developers.cloudflare.com/api/resources/firewall/subresources/lockdowns/methods/create)

POST/zones/{zone_id}/firewall/lockdowns

##### [Update a Zone Lockdown rule](https://developers.cloudflare.com/api/resources/firewall/subresources/lockdowns/methods/update)

PUT/zones/{zone_id}/firewall/lockdowns/{lock_downs_id}

##### [Delete a Zone Lockdown rule](https://developers.cloudflare.com/api/resources/firewall/subresources/lockdowns/methods/delete)

DELETE/zones/{zone_id}/firewall/lockdowns/{lock_downs_id}

#### FirewallRules

##### [List firewall rules](https://developers.cloudflare.com/api/resources/firewall/subresources/rules/methods/list)

Deprecated

GET/zones/{zone_id}/firewall/rules

##### [Get a firewall rule](https://developers.cloudflare.com/api/resources/firewall/subresources/rules/methods/get)

Deprecated

GET/zones/{zone_id}/firewall/rules/{rule_id}

##### [Create firewall rules](https://developers.cloudflare.com/api/resources/firewall/subresources/rules/methods/create)

Deprecated

POST/zones/{zone_id}/firewall/rules

##### [Update a firewall rule](https://developers.cloudflare.com/api/resources/firewall/subresources/rules/methods/update)

Deprecated

PUT/zones/{zone_id}/firewall/rules/{rule_id}

##### [Update priority of a firewall rule](https://developers.cloudflare.com/api/resources/firewall/subresources/rules/methods/edit)

Deprecated

PATCH/zones/{zone_id}/firewall/rules/{rule_id}

##### [Delete a firewall rule](https://developers.cloudflare.com/api/resources/firewall/subresources/rules/methods/delete)

Deprecated

DELETE/zones/{zone_id}/firewall/rules/{rule_id}

##### [Update firewall rules](https://developers.cloudflare.com/api/resources/firewall/subresources/rules/methods/bulk_update)

Deprecated

PUT/zones/{zone_id}/firewall/rules

##### [Update priority of firewall rules](https://developers.cloudflare.com/api/resources/firewall/subresources/rules/methods/bulk_edit)

Deprecated

PATCH/zones/{zone_id}/firewall/rules

##### [Delete firewall rules](https://developers.cloudflare.com/api/resources/firewall/subresources/rules/methods/bulk_delete)

Deprecated

DELETE/zones/{zone_id}/firewall/rules

#### FirewallAccess Rules

##### [List IP Access rules](https://developers.cloudflare.com/api/resources/firewall/subresources/access_rules/methods/list)

GET/{accounts_or_zones}/{account_or_zone_id}/firewall/access_rules/rules

##### [Get an IP Access rule](https://developers.cloudflare.com/api/resources/firewall/subresources/access_rules/methods/get)

GET/{accounts_or_zones}/{account_or_zone_id}/firewall/access_rules/rules/{rule_id}

##### [Create an IP Access rule](https://developers.cloudflare.com/api/resources/firewall/subresources/access_rules/methods/create)

POST/{accounts_or_zones}/{account_or_zone_id}/firewall/access_rules/rules

##### [Update an IP Access rule](https://developers.cloudflare.com/api/resources/firewall/subresources/access_rules/methods/edit)

PATCH/{accounts_or_zones}/{account_or_zone_id}/firewall/access_rules/rules/{rule_id}

##### [Delete an IP Access rule](https://developers.cloudflare.com/api/resources/firewall/subresources/access_rules/methods/delete)

DELETE/{accounts_or_zones}/{account_or_zone_id}/firewall/access_rules/rules/{rule_id}

#### FirewallUA Rules

##### [List User Agent Blocking rules](https://developers.cloudflare.com/api/resources/firewall/subresources/ua_rules/methods/list)

GET/zones/{zone_id}/firewall/ua_rules

##### [Get a User Agent Blocking rule](https://developers.cloudflare.com/api/resources/firewall/subresources/ua_rules/methods/get)

GET/zones/{zone_id}/firewall/ua_rules/{ua_rule_id}

##### [Create a User Agent Blocking rule](https://developers.cloudflare.com/api/resources/firewall/subresources/ua_rules/methods/create)

POST/zones/{zone_id}/firewall/ua_rules

##### [Update a User Agent Blocking rule](https://developers.cloudflare.com/api/resources/firewall/subresources/ua_rules/methods/update)

PUT/zones/{zone_id}/firewall/ua_rules/{ua_rule_id}

##### [Delete a User Agent Blocking rule](https://developers.cloudflare.com/api/resources/firewall/subresources/ua_rules/methods/delete)

DELETE/zones/{zone_id}/firewall/ua_rules/{ua_rule_id}

#### FirewallWAF

#### FirewallWAFOverrides

##### [List WAF overrides](https://developers.cloudflare.com/api/resources/firewall/subresources/waf/subresources/overrides/methods/list)

Deprecated

GET/zones/{zone_id}/firewall/waf/overrides

##### [Get a WAF override](https://developers.cloudflare.com/api/resources/firewall/subresources/waf/subresources/overrides/methods/get)

Deprecated

GET/zones/{zone_id}/firewall/waf/overrides/{overrides_id}

##### [Create a WAF override](https://developers.cloudflare.com/api/resources/firewall/subresources/waf/subresources/overrides/methods/create)

Deprecated

POST/zones/{zone_id}/firewall/waf/overrides

##### [Update WAF override](https://developers.cloudflare.com/api/resources/firewall/subresources/waf/subresources/overrides/methods/update)

Deprecated

PUT/zones/{zone_id}/firewall/waf/overrides/{overrides_id}

##### [Delete a WAF override](https://developers.cloudflare.com/api/resources/firewall/subresources/waf/subresources/overrides/methods/delete)

Deprecated

DELETE/zones/{zone_id}/firewall/waf/overrides/{overrides_id}

#### FirewallWAFPackages

##### [List WAF packages](https://developers.cloudflare.com/api/resources/firewall/subresources/waf/subresources/packages/methods/list)

Deprecated

GET/zones/{zone_id}/firewall/waf/packages

##### [Get a WAF package](https://developers.cloudflare.com/api/resources/firewall/subresources/waf/subresources/packages/methods/get)

Deprecated

GET/zones/{zone_id}/firewall/waf/packages/{package_id}

#### FirewallWAFPackagesGroups

##### [List WAF rule groups](https://developers.cloudflare.com/api/resources/firewall/subresources/waf/subresources/packages/subresources/groups/methods/list)

Deprecated

GET/zones/{zone_id}/firewall/waf/packages/{package_id}/groups

##### [Get a WAF rule group](https://developers.cloudflare.com/api/resources/firewall/subresources/waf/subresources/packages/subresources/groups/methods/get)

Deprecated

GET/zones/{zone_id}/firewall/waf/packages/{package_id}/groups/{group_id}

##### [Update a WAF rule group](https://developers.cloudflare.com/api/resources/firewall/subresources/waf/subresources/packages/subresources/groups/methods/edit)

Deprecated

PATCH/zones/{zone_id}/firewall/waf/packages/{package_id}/groups/{group_id}

#### FirewallWAFPackagesRules

##### [List WAF rules](https://developers.cloudflare.com/api/resources/firewall/subresources/waf/subresources/packages/subresources/rules/methods/list)

Deprecated

GET/zones/{zone_id}/firewall/waf/packages/{package_id}/rules

##### [Get a WAF rule](https://developers.cloudflare.com/api/resources/firewall/subresources/waf/subresources/packages/subresources/rules/methods/get)

Deprecated

GET/zones/{zone_id}/firewall/waf/packages/{package_id}/rules/{rule_id}

##### [Update a WAF rule](https://developers.cloudflare.com/api/resources/firewall/subresources/waf/subresources/packages/subresources/rules/methods/edit)

Deprecated

PATCH/zones/{zone_id}/firewall/waf/packages/{package_id}/rules/{rule_id}

#### Healthchecks

##### [List Health Checks](https://developers.cloudflare.com/api/resources/healthchecks/methods/list)

GET/zones/{zone_id}/healthchecks

##### [Health Check Details](https://developers.cloudflare.com/api/resources/healthchecks/methods/get)

GET/zones/{zone_id}/healthchecks/{healthcheck_id}

##### [Create Health Check](https://developers.cloudflare.com/api/resources/healthchecks/methods/create)

POST/zones/{zone_id}/healthchecks

##### [Update Health Check](https://developers.cloudflare.com/api/resources/healthchecks/methods/update)

PUT/zones/{zone_id}/healthchecks/{healthcheck_id}

##### [Patch Health Check](https://developers.cloudflare.com/api/resources/healthchecks/methods/edit)

PATCH/zones/{zone_id}/healthchecks/{healthcheck_id}

##### [Delete Health Check](https://developers.cloudflare.com/api/resources/healthchecks/methods/delete)

DELETE/zones/{zone_id}/healthchecks/{healthcheck_id}

#### HealthchecksPreviews

##### [Health Check Preview Details](https://developers.cloudflare.com/api/resources/healthchecks/subresources/previews/methods/get)

GET/zones/{zone_id}/healthchecks/preview/{healthcheck_id}

##### [Create Preview Health Check](https://developers.cloudflare.com/api/resources/healthchecks/subresources/previews/methods/create)

POST/zones/{zone_id}/healthchecks/preview

##### [Delete Preview Health Check](https://developers.cloudflare.com/api/resources/healthchecks/subresources/previews/methods/delete)

DELETE/zones/{zone_id}/healthchecks/preview/{healthcheck_id}

#### Keyless Certificates

##### [List Keyless SSL Configurations](https://developers.cloudflare.com/api/resources/keyless_certificates/methods/list)

GET/zones/{zone_id}/keyless_certificates

##### [Get Keyless SSL Configuration](https://developers.cloudflare.com/api/resources/keyless_certificates/methods/get)

GET/zones/{zone_id}/keyless_certificates/{keyless_certificate_id}

##### [Create Keyless SSL Configuration](https://developers.cloudflare.com/api/resources/keyless_certificates/methods/create)

POST/zones/{zone_id}/keyless_certificates

##### [Edit Keyless SSL Configuration](https://developers.cloudflare.com/api/resources/keyless_certificates/methods/edit)

PATCH/zones/{zone_id}/keyless_certificates/{keyless_certificate_id}

##### [Delete Keyless SSL Configuration](https://developers.cloudflare.com/api/resources/keyless_certificates/methods/delete)

DELETE/zones/{zone_id}/keyless_certificates/{keyless_certificate_id}

#### Logpush

#### LogpushDatasets

#### LogpushDatasetsFields

##### [List fields](https://developers.cloudflare.com/api/resources/logpush/subresources/datasets/subresources/fields/methods/get)

GET/{accounts_or_zones}/{account_or_zone_id}/logpush/datasets/{dataset_id}/fields

#### LogpushDatasetsJobs

##### [List Logpush jobs for a dataset](https://developers.cloudflare.com/api/resources/logpush/subresources/datasets/subresources/jobs/methods/get)

GET/{accounts_or_zones}/{account_or_zone_id}/logpush/datasets/{dataset_id}/jobs

#### LogpushEdge

##### [List Instant Logs jobs](https://developers.cloudflare.com/api/resources/logpush/subresources/edge/methods/get)

GET/zones/{zone_id}/logpush/edge/jobs

##### [Create Instant Logs job](https://developers.cloudflare.com/api/resources/logpush/subresources/edge/methods/create)

POST/zones/{zone_id}/logpush/edge/jobs

#### LogpushJobs

##### [List Logpush jobs](https://developers.cloudflare.com/api/resources/logpush/subresources/jobs/methods/list)

GET/{accounts_or_zones}/{account_or_zone_id}/logpush/jobs

##### [Get Logpush job details](https://developers.cloudflare.com/api/resources/logpush/subresources/jobs/methods/get)

GET/{accounts_or_zones}/{account_or_zone_id}/logpush/jobs/{job_id}

##### [Create Logpush job](https://developers.cloudflare.com/api/resources/logpush/subresources/jobs/methods/create)

POST/{accounts_or_zones}/{account_or_zone_id}/logpush/jobs

##### [Update Logpush job](https://developers.cloudflare.com/api/resources/logpush/subresources/jobs/methods/update)

PUT/{accounts_or_zones}/{account_or_zone_id}/logpush/jobs/{job_id}

##### [Delete Logpush job](https://developers.cloudflare.com/api/resources/logpush/subresources/jobs/methods/delete)

DELETE/{accounts_or_zones}/{account_or_zone_id}/logpush/jobs/{job_id}

#### LogpushOwnership

##### [Get ownership challenge](https://developers.cloudflare.com/api/resources/logpush/subresources/ownership/methods/create)

POST/{accounts_or_zones}/{account_or_zone_id}/logpush/ownership

##### [Validate ownership challenge](https://developers.cloudflare.com/api/resources/logpush/subresources/ownership/methods/validate)

POST/{accounts_or_zones}/{account_or_zone_id}/logpush/ownership/validate

#### LogpushTransformers

##### [List transformers](https://developers.cloudflare.com/api/resources/logpush/subresources/transformers/methods/list)

GET/accounts/{account_id}/logpush/transformers

##### [Get transformer](https://developers.cloudflare.com/api/resources/logpush/subresources/transformers/methods/get)

GET/accounts/{account_id}/logpush/transformers/{transformer_id}

##### [Create transformer](https://developers.cloudflare.com/api/resources/logpush/subresources/transformers/methods/create)

POST/accounts/{account_id}/logpush/transformers

##### [Update transformer](https://developers.cloudflare.com/api/resources/logpush/subresources/transformers/methods/update)

PUT/accounts/{account_id}/logpush/transformers/{transformer_id}

##### [Delete transformer](https://developers.cloudflare.com/api/resources/logpush/subresources/transformers/methods/delete)

DELETE/accounts/{account_id}/logpush/transformers/{transformer_id}

##### [Preview transformer](https://developers.cloudflare.com/api/resources/logpush/subresources/transformers/methods/preview)

POST/accounts/{account_id}/logpush/transformers/preview

#### LogpushTransformersContent

##### [Get transformer content](https://developers.cloudflare.com/api/resources/logpush/subresources/transformers/subresources/content/methods/get)

GET/accounts/{account_id}/logpush/transformers/{transformer_id}/content

#### LogpushTransformersVersions

##### [List transformer versions](https://developers.cloudflare.com/api/resources/logpush/subresources/transformers/subresources/versions/methods/list)

GET/accounts/{account_id}/logpush/transformers/{transformer_id}/versions

#### LogpushValidate

##### [Validate destination](https://developers.cloudflare.com/api/resources/logpush/subresources/validate/methods/destination)

POST/{accounts_or_zones}/{account_or_zone_id}/logpush/validate/destination

##### [Check destination exists](https://developers.cloudflare.com/api/resources/logpush/subresources/validate/methods/destination_exists)

POST/{accounts_or_zones}/{account_or_zone_id}/logpush/validate/destination/exists

##### [Validate origin](https://developers.cloudflare.com/api/resources/logpush/subresources/validate/methods/origin)

POST/{accounts_or_zones}/{account_or_zone_id}/logpush/validate/origin

#### Logs

#### LogsLog Explorer

#### LogsLog ExplorerQuery

##### [Run a log query](https://developers.cloudflare.com/api/resources/logs/subresources/log_explorer/subresources/query/methods/sql)

POST/{accounts_or_zones}/{account_or_zone_id}/logs/explorer/query/sql

#### LogsLog ExplorerDatasets

##### [List account or zone datasets](https://developers.cloudflare.com/api/resources/logs/subresources/log_explorer/subresources/datasets/methods/list)

GET/{accounts_or_zones}/{account_or_zone_id}/logs/explorer/datasets

##### [Get an account or zone dataset](https://developers.cloudflare.com/api/resources/logs/subresources/log_explorer/subresources/datasets/methods/get)

GET/{accounts_or_zones}/{account_or_zone_id}/logs/explorer/datasets/{dataset_id}

##### [Create an account or zone dataset](https://developers.cloudflare.com/api/resources/logs/subresources/log_explorer/subresources/datasets/methods/create)

POST/{accounts_or_zones}/{account_or_zone_id}/logs/explorer/datasets

##### [Update an account or zone dataset](https://developers.cloudflare.com/api/resources/logs/subresources/log_explorer/subresources/datasets/methods/update)

PUT/{accounts_or_zones}/{account_or_zone_id}/logs/explorer/datasets/{dataset_id}

##### [Delete an account or zone dataset](https://developers.cloudflare.com/api/resources/logs/subresources/log_explorer/subresources/datasets/methods/delete)

DELETE/{accounts_or_zones}/{account_or_zone_id}/logs/explorer/datasets/{dataset_id}

#### LogsLog ExplorerDatasetsAvailable

##### [List available account or zone datasets](https://developers.cloudflare.com/api/resources/logs/subresources/log_explorer/subresources/datasets/subresources/available/methods/list)

GET/{accounts_or_zones}/{account_or_zone_id}/logs/explorer/datasets/available

#### LogsControl

#### LogsControlRetention

##### [Get log retention flag](https://developers.cloudflare.com/api/resources/logs/subresources/control/subresources/retention/methods/get)

GET/zones/{zone_id}/logs/control/retention/flag

##### [Update log retention flag](https://developers.cloudflare.com/api/resources/logs/subresources/control/subresources/retention/methods/create)

POST/zones/{zone_id}/logs/control/retention/flag

#### LogsControlCmb

#### LogsControlCmbConfig

##### [Get CMB config](https://developers.cloudflare.com/api/resources/logs/subresources/control/subresources/cmb/subresources/config/methods/get)

GET/accounts/{account_id}/logs/control/cmb/config

##### [Update CMB config](https://developers.cloudflare.com/api/resources/logs/subresources/control/subresources/cmb/subresources/config/methods/create)

POST/accounts/{account_id}/logs/control/cmb/config

##### [Delete CMB config](https://developers.cloudflare.com/api/resources/logs/subresources/control/subresources/cmb/subresources/config/methods/delete)

DELETE/accounts/{account_id}/logs/control/cmb/config

#### LogsRayID

##### [Get logs RayIDs](https://developers.cloudflare.com/api/resources/logs/subresources/rayid/methods/get)

GET/zones/{zone_id}/logs/rayids/{ray_id}

#### LogsReceived

##### [Get logs received](https://developers.cloudflare.com/api/resources/logs/subresources/received/methods/get)

GET/zones/{zone_id}/logs/received

#### LogsReceivedFields

##### [List fields](https://developers.cloudflare.com/api/resources/logs/subresources/received/subresources/fields/methods/get)

GET/zones/{zone_id}/logs/received/fields

#### Origin TLS Client Auth

##### [List Certificates](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/methods/list)

Deprecated

GET/zones/{zone_id}/origin_tls_client_auth

##### [Get Certificate Details](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/methods/get)

Deprecated

GET/zones/{zone_id}/origin_tls_client_auth/{certificate_id}

##### [Upload Certificate](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/methods/create)

Deprecated

POST/zones/{zone_id}/origin_tls_client_auth

##### [Delete Certificate](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/methods/delete)

Deprecated

DELETE/zones/{zone_id}/origin_tls_client_auth/{certificate_id}

#### Origin TLS Client AuthZone Certificates

##### [List Certificates](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/zone_certificates/methods/list)

GET/zones/{zone_id}/origin_tls_client_auth

##### [Get Certificate Details](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/zone_certificates/methods/get)

GET/zones/{zone_id}/origin_tls_client_auth/{certificate_id}

##### [Upload Certificate](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/zone_certificates/methods/create)

POST/zones/{zone_id}/origin_tls_client_auth

##### [Delete Certificate](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/zone_certificates/methods/delete)

DELETE/zones/{zone_id}/origin_tls_client_auth/{certificate_id}

#### Origin TLS Client AuthHostnames

##### [Get the Hostname Status for Client Authentication](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/hostnames/methods/get)

GET/zones/{zone_id}/origin_tls_client_auth/hostnames/{hostname}

##### [Enable or Disable a Hostname for Client Authentication](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/hostnames/methods/update)

PUT/zones/{zone_id}/origin_tls_client_auth/hostnames

#### Origin TLS Client AuthHostname Certificates

##### [List Certificates](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/hostname_certificates/methods/list)

GET/zones/{zone_id}/origin_tls_client_auth/hostnames/certificates

##### [Get the Hostname Client Certificate](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/hostname_certificates/methods/get)

GET/zones/{zone_id}/origin_tls_client_auth/hostnames/certificates/{certificate_id}

##### [Upload a Hostname Client Certificate](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/hostname_certificates/methods/create)

POST/zones/{zone_id}/origin_tls_client_auth/hostnames/certificates

##### [Delete Hostname Client Certificate](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/hostname_certificates/methods/delete)

DELETE/zones/{zone_id}/origin_tls_client_auth/hostnames/certificates/{certificate_id}

#### Origin TLS Client AuthSettings

##### [Get Enablement Setting for Zone](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/settings/methods/get)

GET/zones/{zone_id}/origin_tls_client_auth/settings

##### [Set Enablement for Zone](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/settings/methods/update)

PUT/zones/{zone_id}/origin_tls_client_auth/settings

#### Page Rules

##### [List Page Rules](https://developers.cloudflare.com/api/resources/page_rules/methods/list)

GET/zones/{zone_id}/pagerules

##### [Get a Page Rule](https://developers.cloudflare.com/api/resources/page_rules/methods/get)

GET/zones/{zone_id}/pagerules/{pagerule_id}

##### [Create a Page Rule](https://developers.cloudflare.com/api/resources/page_rules/methods/create)

POST/zones/{zone_id}/pagerules

##### [Update a Page Rule](https://developers.cloudflare.com/api/resources/page_rules/methods/update)

PUT/zones/{zone_id}/pagerules/{pagerule_id}

##### [Edit a Page Rule](https://developers.cloudflare.com/api/resources/page_rules/methods/edit)

PATCH/zones/{zone_id}/pagerules/{pagerule_id}

##### [Delete a Page Rule](https://developers.cloudflare.com/api/resources/page_rules/methods/delete)

DELETE/zones/{zone_id}/pagerules/{pagerule_id}

#### Rate Limits

##### [List rate limits](https://developers.cloudflare.com/api/resources/rate_limits/methods/list)

Deprecated

GET/zones/{zone_id}/rate_limits

##### [Get a rate limit](https://developers.cloudflare.com/api/resources/rate_limits/methods/get)

Deprecated

GET/zones/{zone_id}/rate_limits/{rate_limit_id}

##### [Create a rate limit](https://developers.cloudflare.com/api/resources/rate_limits/methods/create)

Deprecated

POST/zones/{zone_id}/rate_limits

##### [Update a rate limit](https://developers.cloudflare.com/api/resources/rate_limits/methods/edit)

Deprecated

PUT/zones/{zone_id}/rate_limits/{rate_limit_id}

##### [Delete a rate limit](https://developers.cloudflare.com/api/resources/rate_limits/methods/delete)

Deprecated

DELETE/zones/{zone_id}/rate_limits/{rate_limit_id}

#### Smart Shield

##### [Get Smart Shield Settings](https://developers.cloudflare.com/api/resources/smart_shield/methods/get)

GET/zones/{zone_id}/smart_shield

##### [Patch Smart Shield Settings](https://developers.cloudflare.com/api/resources/smart_shield/methods/update)

PATCH/zones/{zone_id}/smart_shield

#### Smart ShieldHealth Checks

##### [List Health Checks](https://developers.cloudflare.com/api/resources/smart_shield/subresources/health_checks/methods/list)

GET/zones/{zone_id}/smart_shield/healthchecks

##### [Health Check Details](https://developers.cloudflare.com/api/resources/smart_shield/subresources/health_checks/methods/get)

GET/zones/{zone_id}/smart_shield/healthchecks/{healthcheck_id}

##### [Create Health Check](https://developers.cloudflare.com/api/resources/smart_shield/subresources/health_checks/methods/create)

POST/zones/{zone_id}/smart_shield/healthchecks

##### [Update Health Check](https://developers.cloudflare.com/api/resources/smart_shield/subresources/health_checks/methods/update)

PUT/zones/{zone_id}/smart_shield/healthchecks/{healthcheck_id}

##### [Patch Health Check](https://developers.cloudflare.com/api/resources/smart_shield/subresources/health_checks/methods/edit)

PATCH/zones/{zone_id}/smart_shield/healthchecks/{healthcheck_id}

##### [Delete Health Check](https://developers.cloudflare.com/api/resources/smart_shield/subresources/health_checks/methods/delete)

DELETE/zones/{zone_id}/smart_shield/healthchecks/{healthcheck_id}

#### Smart ShieldCache Reserve Clear

##### [Get Cache Reserve Clear](https://developers.cloudflare.com/api/resources/smart_shield/subresources/cache_reserve_clear/methods/status)

GET/zones/{zone_id}/smart_shield/cache_reserve_clear

##### [Start Cache Reserve Clear](https://developers.cloudflare.com/api/resources/smart_shield/subresources/cache_reserve_clear/methods/clear)

POST/zones/{zone_id}/smart_shield/cache_reserve_clear

#### Waiting Rooms

##### [List waiting rooms for account or zone](https://developers.cloudflare.com/api/resources/waiting_rooms/methods/list)

GET/{accounts_or_zones}/{account_or_zone_id}/waiting_rooms

##### [Waiting room details](https://developers.cloudflare.com/api/resources/waiting_rooms/methods/get)

GET/zones/{zone_id}/waiting_rooms/{waiting_room_id}

##### [Create waiting room](https://developers.cloudflare.com/api/resources/waiting_rooms/methods/create)

POST/zones/{zone_id}/waiting_rooms

##### [Update waiting room](https://developers.cloudflare.com/api/resources/waiting_rooms/methods/update)

PUT/zones/{zone_id}/waiting_rooms/{waiting_room_id}

##### [Patch waiting room](https://developers.cloudflare.com/api/resources/waiting_rooms/methods/edit)

PATCH/zones/{zone_id}/waiting_rooms/{waiting_room_id}

##### [Delete waiting room](https://developers.cloudflare.com/api/resources/waiting_rooms/methods/delete)

DELETE/zones/{zone_id}/waiting_rooms/{waiting_room_id}

#### Waiting RoomsPage

##### [Create a custom waiting room page preview](https://developers.cloudflare.com/api/resources/waiting_rooms/subresources/page/methods/preview)

POST/zones/{zone_id}/waiting_rooms/preview

#### Waiting RoomsEvents

##### [List events](https://developers.cloudflare.com/api/resources/waiting_rooms/subresources/events/methods/list)

GET/zones/{zone_id}/waiting_rooms/{waiting_room_id}/events

##### [Event details](https://developers.cloudflare.com/api/resources/waiting_rooms/subresources/events/methods/get)

GET/zones/{zone_id}/waiting_rooms/{waiting_room_id}/events/{event_id}

##### [Create event](https://developers.cloudflare.com/api/resources/waiting_rooms/subresources/events/methods/create)

POST/zones/{zone_id}/waiting_rooms/{waiting_room_id}/events

##### [Update event](https://developers.cloudflare.com/api/resources/waiting_rooms/subresources/events/methods/update)

PUT/zones/{zone_id}/waiting_rooms/{waiting_room_id}/events/{event_id}

##### [Patch event](https://developers.cloudflare.com/api/resources/waiting_rooms/subresources/events/methods/edit)

PATCH/zones/{zone_id}/waiting_rooms/{waiting_room_id}/events/{event_id}

##### [Delete event](https://developers.cloudflare.com/api/resources/waiting_rooms/subresources/events/methods/delete)

DELETE/zones/{zone_id}/waiting_rooms/{waiting_room_id}/events/{event_id}

#### Waiting RoomsEventsDetails

##### [Preview active event details](https://developers.cloudflare.com/api/resources/waiting_rooms/subresources/events/subresources/details/methods/get)

GET/zones/{zone_id}/waiting_rooms/{waiting_room_id}/events/{event_id}/details

#### Waiting RoomsRules

##### [List Waiting Room Rules](https://developers.cloudflare.com/api/resources/waiting_rooms/subresources/rules/methods/get)

GET/zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules

##### [Create Waiting Room Rule](https://developers.cloudflare.com/api/resources/waiting_rooms/subresources/rules/methods/create)

POST/zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules

##### [Replace Waiting Room Rules](https://developers.cloudflare.com/api/resources/waiting_rooms/subresources/rules/methods/update)

PUT/zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules

##### [Patch Waiting Room Rule](https://developers.cloudflare.com/api/resources/waiting_rooms/subresources/rules/methods/edit)

PATCH/zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules/{rule_id}

##### [Delete Waiting Room Rule](https://developers.cloudflare.com/api/resources/waiting_rooms/subresources/rules/methods/delete)

DELETE/zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules/{rule_id}

#### Waiting RoomsStatuses

##### [Get waiting room status](https://developers.cloudflare.com/api/resources/waiting_rooms/subresources/statuses/methods/get)

GET/zones/{zone_id}/waiting_rooms/{waiting_room_id}/status

#### Waiting RoomsSettings

##### [Get zone-level Waiting Room settings](https://developers.cloudflare.com/api/resources/waiting_rooms/subresources/settings/methods/get)

GET/zones/{zone_id}/waiting_rooms/settings

##### [Update zone-level Waiting Room settings](https://developers.cloudflare.com/api/resources/waiting_rooms/subresources/settings/methods/update)

PUT/zones/{zone_id}/waiting_rooms/settings

##### [Patch zone-level Waiting Room settings](https://developers.cloudflare.com/api/resources/waiting_rooms/subresources/settings/methods/edit)

PATCH/zones/{zone_id}/waiting_rooms/settings

#### Web3

#### Web3Hostnames

##### [List Web3 Hostnames](https://developers.cloudflare.com/api/resources/web3/subresources/hostnames/methods/list)

GET/zones/{zone_id}/web3/hostnames

##### [Web3 Hostname Details](https://developers.cloudflare.com/api/resources/web3/subresources/hostnames/methods/get)

GET/zones/{zone_id}/web3/hostnames/{identifier}

##### [Create Web3 Hostname](https://developers.cloudflare.com/api/resources/web3/subresources/hostnames/methods/create)

POST/zones/{zone_id}/web3/hostnames

##### [Edit Web3 Hostname](https://developers.cloudflare.com/api/resources/web3/subresources/hostnames/methods/edit)

PATCH/zones/{zone_id}/web3/hostnames/{identifier}

##### [Delete Web3 Hostname](https://developers.cloudflare.com/api/resources/web3/subresources/hostnames/methods/delete)

DELETE/zones/{zone_id}/web3/hostnames/{identifier}

#### Web3HostnamesIPFS Universal Paths

#### Web3HostnamesIPFS Universal PathsContent Lists

##### [IPFS Universal Path Gateway Content List Details](https://developers.cloudflare.com/api/resources/web3/subresources/hostnames/subresources/ipfs_universal_paths/subresources/content_lists/methods/get)

GET/zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list

##### [Update IPFS Universal Path Gateway Content List](https://developers.cloudflare.com/api/resources/web3/subresources/hostnames/subresources/ipfs_universal_paths/subresources/content_lists/methods/update)

PUT/zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list

#### Web3HostnamesIPFS Universal PathsContent ListsEntries

##### [List IPFS Universal Path Gateway Content List Entries](https://developers.cloudflare.com/api/resources/web3/subresources/hostnames/subresources/ipfs_universal_paths/subresources/content_lists/subresources/entries/methods/list)

GET/zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries

##### [IPFS Universal Path Gateway Content List Entry Details](https://developers.cloudflare.com/api/resources/web3/subresources/hostnames/subresources/ipfs_universal_paths/subresources/content_lists/subresources/entries/methods/get)

GET/zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries/{content_list_entry_identifier}

##### [Create IPFS Universal Path Gateway Content List Entry](https://developers.cloudflare.com/api/resources/web3/subresources/hostnames/subresources/ipfs_universal_paths/subresources/content_lists/subresources/entries/methods/create)

POST/zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries

##### [Edit IPFS Universal Path Gateway Content List Entry](https://developers.cloudflare.com/api/resources/web3/subresources/hostnames/subresources/ipfs_universal_paths/subresources/content_lists/subresources/entries/methods/update)

PUT/zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries/{content_list_entry_identifier}

##### [Delete IPFS Universal Path Gateway Content List Entry](https://developers.cloudflare.com/api/resources/web3/subresources/hostnames/subresources/ipfs_universal_paths/subresources/content_lists/subresources/entries/methods/delete)

DELETE/zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries/{content_list_entry_identifier}

#### Workers

#### WorkersBeta

#### WorkersBetaWorkers

##### [List Workers](https://developers.cloudflare.com/api/resources/workers/subresources/beta/subresources/workers/methods/list)

GET/accounts/{account_id}/workers/workers

##### [Get Worker](https://developers.cloudflare.com/api/resources/workers/subresources/beta/subresources/workers/methods/get)

GET/accounts/{account_id}/workers/workers/{worker_id}

##### [Create Worker](https://developers.cloudflare.com/api/resources/workers/subresources/beta/subresources/workers/methods/create)

POST/accounts/{account_id}/workers/workers

##### [Update Worker](https://developers.cloudflare.com/api/resources/workers/subresources/beta/subresources/workers/methods/update)

PUT/accounts/{account_id}/workers/workers/{worker_id}

##### [Edit Worker](https://developers.cloudflare.com/api/resources/workers/subresources/beta/subresources/workers/methods/edit)

PATCH/accounts/{account_id}/workers/workers/{worker_id}

##### [Delete Worker](https://developers.cloudflare.com/api/resources/workers/subresources/beta/subresources/workers/methods/delete)

DELETE/accounts/{account_id}/workers/workers/{worker_id}

#### WorkersBetaWorkersVersions

##### [List Worker Versions](https://developers.cloudflare.com/api/resources/workers/subresources/beta/subresources/workers/subresources/versions/methods/list)

GET/accounts/{account_id}/workers/workers/{worker_id}/versions

##### [Get Worker Version](https://developers.cloudflare.com/api/resources/workers/subresources/beta/subresources/workers/subresources/versions/methods/get)

GET/accounts/{account_id}/workers/workers/{worker_id}/versions/{version_id}

##### [Create Worker Version](https://developers.cloudflare.com/api/resources/workers/subresources/beta/subresources/workers/subresources/versions/methods/create)

POST/accounts/{account_id}/workers/workers/{worker_id}/versions

##### [Profile Worker Version](https://developers.cloudflare.com/api/resources/workers/subresources/beta/subresources/workers/subresources/versions/methods/profile)

POST/accounts/{account_id}/workers/workers/{worker_id}/versions/{version_id}/profile

##### [Delete Worker Version](https://developers.cloudflare.com/api/resources/workers/subresources/beta/subresources/workers/subresources/versions/methods/delete)

DELETE/accounts/{account_id}/workers/workers/{worker_id}/versions/{version_id}

#### WorkersRoutes

##### [List Worker Routes](https://developers.cloudflare.com/api/resources/workers/subresources/routes/methods/list)

GET/zones/{zone_id}/workers/routes

##### [Get Worker Route](https://developers.cloudflare.com/api/resources/workers/subresources/routes/methods/get)

GET/zones/{zone_id}/workers/routes/{route_id}

##### [Create Worker Route](https://developers.cloudflare.com/api/resources/workers/subresources/routes/methods/create)

POST/zones/{zone_id}/workers/routes

##### [Replace Worker Route](https://developers.cloudflare.com/api/resources/workers/subresources/routes/methods/update)

PUT/zones/{zone_id}/workers/routes/{route_id}

##### [Delete Worker Route](https://developers.cloudflare.com/api/resources/workers/subresources/routes/methods/delete)

DELETE/zones/{zone_id}/workers/routes/{route_id}

#### WorkersAssets

#### WorkersAssetsUpload

##### [Upload Worker Assets](https://developers.cloudflare.com/api/resources/workers/subresources/assets/subresources/upload/methods/create)

POST/accounts/{account_id}/workers/assets/upload

#### WorkersScripts

##### [List Worker Scripts](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/methods/list)

GET/accounts/{account_id}/workers/scripts

##### [Search Worker Scripts](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/methods/search)

GET/accounts/{account_id}/workers/scripts-search

##### [Download Worker Script](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/methods/get)

GET/accounts/{account_id}/workers/scripts/{script_name}

##### [Upload Worker Module](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/methods/update)

PUT/accounts/{account_id}/workers/scripts/{script_name}

##### [Delete Worker](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/methods/delete)

DELETE/accounts/{account_id}/workers/scripts/{script_name}

#### WorkersScriptsAssets

#### WorkersScriptsAssetsUpload

##### [Create Worker Assets Upload Session](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/assets/subresources/upload/methods/create)

POST/accounts/{account_id}/workers/scripts/{script_name}/assets-upload-session

#### WorkersScriptsSubdomain

##### [Get Worker Script Subdomain](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/subdomain/methods/get)

GET/accounts/{account_id}/workers/scripts/{script_name}/subdomain

##### [Update Worker Script Subdomain](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/subdomain/methods/create)

POST/accounts/{account_id}/workers/scripts/{script_name}/subdomain

##### [Delete Worker Script Subdomain](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/subdomain/methods/delete)

DELETE/accounts/{account_id}/workers/scripts/{script_name}/subdomain

#### WorkersScriptsSchedules

##### [Get Worker Script Schedules (Cron Triggers)](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/schedules/methods/get)

GET/accounts/{account_id}/workers/scripts/{script_name}/schedules

##### [Update Worker Script Schedules (Cron Triggers)](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/schedules/methods/update)

PUT/accounts/{account_id}/workers/scripts/{script_name}/schedules

#### WorkersScriptsTail

##### [List Worker Tails](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/tail/methods/get)

GET/accounts/{account_id}/workers/scripts/{script_name}/tails

##### [Start Worker Tail](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/tail/methods/create)

POST/accounts/{account_id}/workers/scripts/{script_name}/tails

##### [Delete Worker Tail](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/tail/methods/delete)

DELETE/accounts/{account_id}/workers/scripts/{script_name}/tails/{id}

#### WorkersScriptsContent

##### [Get Worker Script Content](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/content/methods/get)

GET/accounts/{account_id}/workers/scripts/{script_name}/content/v2

##### [Replace Worker Script Content](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/content/methods/update)

PUT/accounts/{account_id}/workers/scripts/{script_name}/content

#### WorkersScriptsSettings

##### [Get Worker Script Settings](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/settings/methods/get)

GET/accounts/{account_id}/workers/scripts/{script_name}/script-settings

##### [Patch Worker Script Settings](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/settings/methods/edit)

PATCH/accounts/{account_id}/workers/scripts/{script_name}/script-settings

#### WorkersScriptsDeployments

##### [List Worker Deployments](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/deployments/methods/list)

GET/accounts/{account_id}/workers/scripts/{script_name}/deployments

##### [Create Worker Deployment](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/deployments/methods/create)

POST/accounts/{account_id}/workers/scripts/{script_name}/deployments

##### [Get Worker Deployment](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/deployments/methods/get)

GET/accounts/{account_id}/workers/scripts/{script_name}/deployments/{deployment_id}

##### [Delete Worker Deployment](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/deployments/methods/delete)

DELETE/accounts/{account_id}/workers/scripts/{script_name}/deployments/{deployment_id}

#### WorkersScriptsVersions

##### [List Versions](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/versions/methods/list)

GET/accounts/{account_id}/workers/scripts/{script_name}/versions

##### [Get Worker Script Version](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/versions/methods/get)

GET/accounts/{account_id}/workers/scripts/{script_name}/versions/{version_id}

##### [Upload Version](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/versions/methods/create)

POST/accounts/{account_id}/workers/scripts/{script_name}/versions

#### WorkersScriptsSecrets

##### [List secrets bound to a Worker script](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/secrets/methods/list)

GET/accounts/{account_id}/workers/scripts/{script_name}/secrets

##### [Get a secret binding](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/secrets/methods/get)

GET/accounts/{account_id}/workers/scripts/{script_name}/secrets/{secret_name}

##### [Add a secret to a Worker script](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/secrets/methods/update)

PUT/accounts/{account_id}/workers/scripts/{script_name}/secrets

##### [Delete Worker script secret](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/secrets/methods/delete)

DELETE/accounts/{account_id}/workers/scripts/{script_name}/secrets/{secret_name}

##### [Patch multiple Worker script secrets](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/secrets/methods/bulk_update)

PATCH/accounts/{account_id}/workers/scripts/{script_name}/secrets-bulk

#### WorkersScriptsScript And Version Settings

##### [Get Worker Script and Version Settings](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/script_and_version_settings/methods/get)

GET/accounts/{account_id}/workers/scripts/{script_name}/settings

##### [Patch Worker Script and Version Settings](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/script_and_version_settings/methods/edit)

PATCH/accounts/{account_id}/workers/scripts/{script_name}/settings

#### WorkersAccount Settings

##### [Fetch Workers Account Settings](https://developers.cloudflare.com/api/resources/workers/subresources/account_settings/methods/get)

GET/accounts/{account_id}/workers/account-settings

##### [Configure Workers Account Settings](https://developers.cloudflare.com/api/resources/workers/subresources/account_settings/methods/update)

PUT/accounts/{account_id}/workers/account-settings

#### WorkersDomains

##### [List Worker Domains](https://developers.cloudflare.com/api/resources/workers/subresources/domains/methods/list)

GET/accounts/{account_id}/workers/domains

##### [Get Worker Domain](https://developers.cloudflare.com/api/resources/workers/subresources/domains/methods/get)

GET/accounts/{account_id}/workers/domains/{domain_id}

##### [Attach Worker Domain](https://developers.cloudflare.com/api/resources/workers/subresources/domains/methods/update)

PUT/accounts/{account_id}/workers/domains

##### [Detach Worker Domain](https://developers.cloudflare.com/api/resources/workers/subresources/domains/methods/delete)

DELETE/accounts/{account_id}/workers/domains/{domain_id}

#### WorkersSubdomains

##### [Get a Workers Subdomain](https://developers.cloudflare.com/api/resources/workers/subresources/subdomains/methods/get)

GET/accounts/{account_id}/workers/subdomain

##### [Create a Workers Subdomain](https://developers.cloudflare.com/api/resources/workers/subresources/subdomains/methods/update)

PUT/accounts/{account_id}/workers/subdomain

##### [Delete Workers Subdomain](https://developers.cloudflare.com/api/resources/workers/subresources/subdomains/methods/delete)

DELETE/accounts/{account_id}/workers/subdomain

#### WorkersObservability

#### WorkersObservabilityTelemetry

##### [List keys](https://developers.cloudflare.com/api/resources/workers/subresources/observability/subresources/telemetry/methods/keys)

POST/accounts/{account_id}/workers/observability/telemetry/keys

##### [Run a query](https://developers.cloudflare.com/api/resources/workers/subresources/observability/subresources/telemetry/methods/query)

POST/accounts/{account_id}/workers/observability/telemetry/query

##### [List values](https://developers.cloudflare.com/api/resources/workers/subresources/observability/subresources/telemetry/methods/values)

POST/accounts/{account_id}/workers/observability/telemetry/values

##### [Prepare live tail](https://developers.cloudflare.com/api/resources/workers/subresources/observability/subresources/telemetry/methods/live_tail)

POST/accounts/{account_id}/workers/observability/telemetry/live-tail

##### [Live tail heartbeat](https://developers.cloudflare.com/api/resources/workers/subresources/observability/subresources/telemetry/methods/live_tail_heartbeat)

POST/accounts/{account_id}/workers/observability/telemetry/live-tail/heartbeat

#### WorkersObservabilityDestinations

##### [Get Destinations](https://developers.cloudflare.com/api/resources/workers/subresources/observability/subresources/destinations/methods/list)

GET/accounts/{account_id}/workers/observability/destinations

##### [Create Destination](https://developers.cloudflare.com/api/resources/workers/subresources/observability/subresources/destinations/methods/create)

POST/accounts/{account_id}/workers/observability/destinations

##### [Update Destination](https://developers.cloudflare.com/api/resources/workers/subresources/observability/subresources/destinations/methods/update)

PATCH/accounts/{account_id}/workers/observability/destinations/{slug}

##### [Delete Destination](https://developers.cloudflare.com/api/resources/workers/subresources/observability/subresources/destinations/methods/delete)

DELETE/accounts/{account_id}/workers/observability/destinations/{slug}

#### WorkersObservabilityQueries

##### [Save query](https://developers.cloudflare.com/api/resources/workers/subresources/observability/subresources/queries/methods/create)

POST/accounts/{account_id}/workers/observability/queries

##### [List queries](https://developers.cloudflare.com/api/resources/workers/subresources/observability/subresources/queries/methods/list)

GET/accounts/{account_id}/workers/observability/queries

#### WorkersObservabilityShared Queries

##### [Create a sharable link to a query result](https://developers.cloudflare.com/api/resources/workers/subresources/observability/subresources/shared_queries/methods/create)

POST/accounts/{account_id}/workers/observability/shared/query

##### [View a query that has been shared](https://developers.cloudflare.com/api/resources/workers/subresources/observability/subresources/shared_queries/methods/get)

GET/accounts/{account_id}/workers/observability/shared/query/{id}

#### KV

#### KVNamespaces

##### [List namespaces](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/methods/list)

GET/accounts/{account_id}/storage/kv/namespaces

##### [Get a namespace](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/methods/get)

GET/accounts/{account_id}/storage/kv/namespaces/{namespace_id}

##### [Create a namespace](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/methods/create)

POST/accounts/{account_id}/storage/kv/namespaces

##### [Rename a namespace](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/methods/update)

PUT/accounts/{account_id}/storage/kv/namespaces/{namespace_id}

##### [Delete a namespace](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/methods/delete)

DELETE/accounts/{account_id}/storage/kv/namespaces/{namespace_id}

##### [Write multiple key-value pairs](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/methods/bulk_update)

PUT/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk

##### [Delete multiple key-value pairs](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/methods/bulk_delete)

POST/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk/delete

##### [Get multiple key-value pairs](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/methods/bulk_get)

POST/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk/get

#### KVNamespacesKeys

##### [List keys in a namespace](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/subresources/keys/methods/list)

GET/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/keys

##### [Write multiple key-value pairs](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/subresources/keys/methods/bulk_update)

Deprecated

PUT/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk

##### [Delete multiple key-value pairs](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/subresources/keys/methods/bulk_delete)

Deprecated

POST/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk/delete

##### [Get multiple key-value pairs](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/subresources/keys/methods/bulk_get)

Deprecated

POST/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk/get

#### KVNamespacesMetadata

##### [Get a key's metadata](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/subresources/metadata/methods/get)

GET/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/metadata/{key_name}

#### KVNamespacesValues

##### [Get a key's value](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/subresources/values/methods/get)

GET/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}

##### [Write a key-value pair with optional metadata](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/subresources/values/methods/update)

PUT/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}

##### [Delete a key-value pair](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/subresources/values/methods/delete)

DELETE/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}

#### Durable Objects

#### Durable ObjectsNamespaces

##### [List Durable Object Namespaces](https://developers.cloudflare.com/api/resources/durable_objects/subresources/namespaces/methods/list)

GET/accounts/{account_id}/workers/durable_objects/namespaces

#### Durable ObjectsNamespacesObjects

##### [List Objects in a Durable Object namespace](https://developers.cloudflare.com/api/resources/durable_objects/subresources/namespaces/subresources/objects/methods/list)

GET/accounts/{account_id}/workers/durable_objects/namespaces/{id}/objects

#### Containers

#### ContainersApplications

##### [List Applications associated with your account](https://developers.cloudflare.com/api/resources/containers/subresources/applications/methods/list)

GET/accounts/{account_id}/containers/applications

##### [Create a new application](https://developers.cloudflare.com/api/resources/containers/subresources/applications/methods/create)

POST/accounts/{account_id}/containers/applications

##### [Get a single application by id](https://developers.cloudflare.com/api/resources/containers/subresources/applications/methods/get)

GET/accounts/{account_id}/containers/applications/{application_id}

##### [Modify an application](https://developers.cloudflare.com/api/resources/containers/subresources/applications/methods/edit)

PATCH/accounts/{account_id}/containers/applications/{application_id}

##### [Delete a single application by id](https://developers.cloudflare.com/api/resources/containers/subresources/applications/methods/delete)

DELETE/accounts/{account_id}/containers/applications/{application_id}

#### ContainersApplicationsInstances

##### [List container instances (deprecated)](https://developers.cloudflare.com/api/resources/containers/subresources/applications/subresources/instances/methods/list_v1)

Deprecated

GET/accounts/{account_id}/containers/applications/{application_id}/instances

##### [List container instances](https://developers.cloudflare.com/api/resources/containers/subresources/applications/subresources/instances/methods/list)

GET/accounts/{account_id}/containers/applications/{application_id}/instances-v2

##### [Get a container instance](https://developers.cloudflare.com/api/resources/containers/subresources/applications/subresources/instances/methods/get)

GET/accounts/{account_id}/containers/applications/{application_id}/instances/{instance_id}

#### ContainersApplicationsRollouts

##### [Create a new rollout for an application](https://developers.cloudflare.com/api/resources/containers/subresources/applications/subresources/rollouts/methods/create)

POST/accounts/{account_id}/containers/applications/{application_id}/rollouts

#### ContainersApplicationsVersions

##### [List all application versions](https://developers.cloudflare.com/api/resources/containers/subresources/applications/subresources/versions/methods/list)

GET/accounts/{account_id}/containers/applications/{application_id}/versions

#### ContainersImages

##### [Prepare a container image](https://developers.cloudflare.com/api/resources/containers/subresources/images/methods/prepare)

POST/accounts/{account_id}/containers/image-preparations

#### ContainersRegistries

##### [Get the list of configured registries in the account](https://developers.cloudflare.com/api/resources/containers/subresources/registries/methods/list)

GET/accounts/{account_id}/containers/registries

##### [Configure a private external image registry](https://developers.cloudflare.com/api/resources/containers/subresources/registries/methods/create)

POST/accounts/{account_id}/containers/registries

##### [Delete a registry from the account](https://developers.cloudflare.com/api/resources/containers/subresources/registries/methods/delete)

DELETE/accounts/{account_id}/containers/registries/{domain}

#### ContainersRegistriesCredentials

##### [Generate a JWT to interact with the specified image registry.](https://developers.cloudflare.com/api/resources/containers/subresources/registries/subresources/credentials/methods/generate)

POST/accounts/{account_id}/containers/registries/{domain}/credentials

#### Queues

##### [List Queues](https://developers.cloudflare.com/api/resources/queues/methods/list)

GET/accounts/{account_id}/queues

##### [Get Queue](https://developers.cloudflare.com/api/resources/queues/methods/get)

GET/accounts/{account_id}/queues/{queue_id}

##### [Get Queue Metrics](https://developers.cloudflare.com/api/resources/queues/methods/get_metrics)

GET/accounts/{account_id}/queues/{queue_id}/metrics

##### [Create Queue](https://developers.cloudflare.com/api/resources/queues/methods/create)

POST/accounts/{account_id}/queues

##### [Update Queue](https://developers.cloudflare.com/api/resources/queues/methods/update)

PUT/accounts/{account_id}/queues/{queue_id}

##### [Update Queue](https://developers.cloudflare.com/api/resources/queues/methods/edit)

PATCH/accounts/{account_id}/queues/{queue_id}

##### [Delete Queue](https://developers.cloudflare.com/api/resources/queues/methods/delete)

DELETE/accounts/{account_id}/queues/{queue_id}

#### QueuesMessages

##### [Push Message](https://developers.cloudflare.com/api/resources/queues/subresources/messages/methods/push)

POST/accounts/{account_id}/queues/{queue_id}/messages

##### [Acknowledge + Retry Queue Messages](https://developers.cloudflare.com/api/resources/queues/subresources/messages/methods/ack)

POST/accounts/{account_id}/queues/{queue_id}/messages/ack

##### [Pull Queue Messages](https://developers.cloudflare.com/api/resources/queues/subresources/messages/methods/pull)

POST/accounts/{account_id}/queues/{queue_id}/messages/pull

##### [Push Message Batch](https://developers.cloudflare.com/api/resources/queues/subresources/messages/methods/bulk_push)

POST/accounts/{account_id}/queues/{queue_id}/messages/batch

##### [Peek Queue Messages](https://developers.cloudflare.com/api/resources/queues/subresources/messages/methods/peek)

POST/accounts/{account_id}/queues/{queue_id}/messages/peek

##### [Purge Peeked Queue Messages](https://developers.cloudflare.com/api/resources/queues/subresources/messages/methods/purge)

POST/accounts/{account_id}/queues/{queue_id}/messages/purge

#### QueuesPurge

##### [Get Queue Purge Status](https://developers.cloudflare.com/api/resources/queues/subresources/purge/methods/status)

GET/accounts/{account_id}/queues/{queue_id}/purge

##### [Purge Queue](https://developers.cloudflare.com/api/resources/queues/subresources/purge/methods/start)

POST/accounts/{account_id}/queues/{queue_id}/purge

#### QueuesConsumers

##### [List Queue Consumers](https://developers.cloudflare.com/api/resources/queues/subresources/consumers/methods/list)

GET/accounts/{account_id}/queues/{queue_id}/consumers

##### [Get Queue Consumer](https://developers.cloudflare.com/api/resources/queues/subresources/consumers/methods/get)

GET/accounts/{account_id}/queues/{queue_id}/consumers/{consumer_id}

##### [Create a Queue Consumer](https://developers.cloudflare.com/api/resources/queues/subresources/consumers/methods/create)

POST/accounts/{account_id}/queues/{queue_id}/consumers

##### [Update Queue Consumer](https://developers.cloudflare.com/api/resources/queues/subresources/consumers/methods/update)

PUT/accounts/{account_id}/queues/{queue_id}/consumers/{consumer_id}

##### [Delete Queue Consumer](https://developers.cloudflare.com/api/resources/queues/subresources/consumers/methods/delete)

DELETE/accounts/{account_id}/queues/{queue_id}/consumers/{consumer_id}

#### QueuesSubscriptions

##### [List Event Subscriptions](https://developers.cloudflare.com/api/resources/queues/subresources/subscriptions/methods/list)

GET/accounts/{account_id}/event_subscriptions/subscriptions

##### [Get Event Subscription](https://developers.cloudflare.com/api/resources/queues/subresources/subscriptions/methods/get)

GET/accounts/{account_id}/event_subscriptions/subscriptions/{subscription_id}

##### [Create Event Subscription](https://developers.cloudflare.com/api/resources/queues/subresources/subscriptions/methods/create)

POST/accounts/{account_id}/event_subscriptions/subscriptions

##### [Update Event Subscription](https://developers.cloudflare.com/api/resources/queues/subresources/subscriptions/methods/update)

PATCH/accounts/{account_id}/event_subscriptions/subscriptions/{subscription_id}

##### [Delete Event Subscription](https://developers.cloudflare.com/api/resources/queues/subresources/subscriptions/methods/delete)

DELETE/accounts/{account_id}/event_subscriptions/subscriptions/{subscription_id}

#### API Gateway

#### API GatewayConfigurations

##### [Get session identifier settings](https://developers.cloudflare.com/api/resources/api_gateway/subresources/configurations/methods/get)

GET/zones/{zone_id}/api_gateway/configuration

##### [Update session identifier settings](https://developers.cloudflare.com/api/resources/api_gateway/subresources/configurations/methods/update)

PUT/zones/{zone_id}/api_gateway/configuration

#### API GatewayDiscovery

##### [Export discovered API operations as OpenAPI schemas](https://developers.cloudflare.com/api/resources/api_gateway/subresources/discovery/methods/get)

GET/zones/{zone_id}/api_gateway/discovery

#### API GatewayDiscoveryOperations

##### [List discovered web and API operations](https://developers.cloudflare.com/api/resources/api_gateway/subresources/discovery/subresources/operations/methods/list)

GET/zones/{zone_id}/api_gateway/discovery/operations

##### [Edit a discovered web or API operation](https://developers.cloudflare.com/api/resources/api_gateway/subresources/discovery/subresources/operations/methods/edit)

PATCH/zones/{zone_id}/api_gateway/discovery/operations/{discovery_id}

##### [Edit discovered web and API operations](https://developers.cloudflare.com/api/resources/api_gateway/subresources/discovery/subresources/operations/methods/bulk_edit)

PATCH/zones/{zone_id}/api_gateway/discovery/operations

#### API GatewayLabels

##### [List operation labels](https://developers.cloudflare.com/api/resources/api_gateway/subresources/labels/methods/list)

GET/zones/{zone_id}/api_gateway/labels

#### API GatewayLabelsUser

##### [Create user-defined operation labels](https://developers.cloudflare.com/api/resources/api_gateway/subresources/labels/subresources/user/methods/bulk_create)

POST/zones/{zone_id}/api_gateway/labels/user

##### [Delete user-defined operation labels](https://developers.cloudflare.com/api/resources/api_gateway/subresources/labels/subresources/user/methods/bulk_delete)

DELETE/zones/{zone_id}/api_gateway/labels/user

##### [Get a user-defined operation label](https://developers.cloudflare.com/api/resources/api_gateway/subresources/labels/subresources/user/methods/get)

GET/zones/{zone_id}/api_gateway/labels/user/{name}

##### [Update a user-defined operation label](https://developers.cloudflare.com/api/resources/api_gateway/subresources/labels/subresources/user/methods/update)

PUT/zones/{zone_id}/api_gateway/labels/user/{name}

##### [Edit a user-defined operation label](https://developers.cloudflare.com/api/resources/api_gateway/subresources/labels/subresources/user/methods/edit)

PATCH/zones/{zone_id}/api_gateway/labels/user/{name}

##### [Delete a user-defined operation label](https://developers.cloudflare.com/api/resources/api_gateway/subresources/labels/subresources/user/methods/delete)

DELETE/zones/{zone_id}/api_gateway/labels/user/{name}

#### API GatewayLabelsUserResources

#### API GatewayLabelsUserResourcesOperation

##### [Replace operations attached to a user-defined label](https://developers.cloudflare.com/api/resources/api_gateway/subresources/labels/subresources/user/subresources/resources/subresources/operation/methods/update)

PUT/zones/{zone_id}/api_gateway/labels/user/{name}/resources/operation

#### API GatewayLabelsManaged

##### [Get a managed operation label](https://developers.cloudflare.com/api/resources/api_gateway/subresources/labels/subresources/managed/methods/get)

GET/zones/{zone_id}/api_gateway/labels/managed/{name}

#### API GatewayLabelsManagedResources

#### API GatewayLabelsManagedResourcesOperation

##### [Replace operations attached to a managed label](https://developers.cloudflare.com/api/resources/api_gateway/subresources/labels/subresources/managed/subresources/resources/subresources/operation/methods/update)

PUT/zones/{zone_id}/api_gateway/labels/managed/{name}/resources/operation

#### API GatewayOperations

##### [List web and API operations](https://developers.cloudflare.com/api/resources/api_gateway/subresources/operations/methods/list)

GET/zones/{zone_id}/api_gateway/operations

##### [Get a web or API operation](https://developers.cloudflare.com/api/resources/api_gateway/subresources/operations/methods/get)

GET/zones/{zone_id}/api_gateway/operations/{operation_id}

##### [Create a web or API operation](https://developers.cloudflare.com/api/resources/api_gateway/subresources/operations/methods/create)

POST/zones/{zone_id}/api_gateway/operations/item

##### [Delete a web or API operation](https://developers.cloudflare.com/api/resources/api_gateway/subresources/operations/methods/delete)

DELETE/zones/{zone_id}/api_gateway/operations/{operation_id}

##### [Create web or API operations](https://developers.cloudflare.com/api/resources/api_gateway/subresources/operations/methods/bulk_create)

POST/zones/{zone_id}/api_gateway/operations

##### [Delete web or API operations](https://developers.cloudflare.com/api/resources/api_gateway/subresources/operations/methods/bulk_delete)

DELETE/zones/{zone_id}/api_gateway/operations

#### API GatewayOperationsLabels

##### [Replace labels on a web or API operation](https://developers.cloudflare.com/api/resources/api_gateway/subresources/operations/subresources/labels/methods/update)

PUT/zones/{zone_id}/api_gateway/operations/{operation_id}/labels

##### [Attach labels to a web or API operation](https://developers.cloudflare.com/api/resources/api_gateway/subresources/operations/subresources/labels/methods/create)

POST/zones/{zone_id}/api_gateway/operations/{operation_id}/labels

##### [Remove labels from a web or API operation](https://developers.cloudflare.com/api/resources/api_gateway/subresources/operations/subresources/labels/methods/delete)

DELETE/zones/{zone_id}/api_gateway/operations/{operation_id}/labels

##### [Replace labels on web or API operations](https://developers.cloudflare.com/api/resources/api_gateway/subresources/operations/subresources/labels/methods/bulk_update)

PUT/zones/{zone_id}/api_gateway/operations/labels

##### [Attach labels to web or API operations](https://developers.cloudflare.com/api/resources/api_gateway/subresources/operations/subresources/labels/methods/bulk_create)

POST/zones/{zone_id}/api_gateway/operations/labels

##### [Remove labels from web or API operations](https://developers.cloudflare.com/api/resources/api_gateway/subresources/operations/subresources/labels/methods/bulk_delete)

DELETE/zones/{zone_id}/api_gateway/operations/labels

#### API GatewayOperationsSchema Validation

##### [Retrieve operation-level schema validation settings](https://developers.cloudflare.com/api/resources/api_gateway/subresources/operations/subresources/schema_validation/methods/get)

Deprecated

GET/zones/{zone_id}/api_gateway/operations/{operation_id}/schema_validation

##### [Update operation-level schema validation settings](https://developers.cloudflare.com/api/resources/api_gateway/subresources/operations/subresources/schema_validation/methods/update)

Deprecated

PUT/zones/{zone_id}/api_gateway/operations/{operation_id}/schema_validation

##### [Update multiple operation-level schema validation settings](https://developers.cloudflare.com/api/resources/api_gateway/subresources/operations/subresources/schema_validation/methods/edit)

Deprecated

PATCH/zones/{zone_id}/api_gateway/operations/schema_validation

#### API GatewaySchemas

##### [Export web and API operations as OpenAPI schemas](https://developers.cloudflare.com/api/resources/api_gateway/subresources/schemas/methods/list)

GET/zones/{zone_id}/api_gateway/schemas

#### API GatewaySettings

#### API GatewaySettingsSchema Validation

##### [Retrieve zone level schema validation settings](https://developers.cloudflare.com/api/resources/api_gateway/subresources/settings/subresources/schema_validation/methods/get)

Deprecated

GET/zones/{zone_id}/api_gateway/settings/schema_validation

##### [Update zone level schema validation settings](https://developers.cloudflare.com/api/resources/api_gateway/subresources/settings/subresources/schema_validation/methods/update)

Deprecated

PUT/zones/{zone_id}/api_gateway/settings/schema_validation

##### [Update zone level schema validation settings](https://developers.cloudflare.com/api/resources/api_gateway/subresources/settings/subresources/schema_validation/methods/edit)

Deprecated

PATCH/zones/{zone_id}/api_gateway/settings/schema_validation

#### API GatewayUser Schemas

##### [Retrieve information about all schemas on a zone](https://developers.cloudflare.com/api/resources/api_gateway/subresources/user_schemas/methods/list)

Deprecated

GET/zones/{zone_id}/api_gateway/user_schemas

##### [Retrieve information about a specific schema on a zone](https://developers.cloudflare.com/api/resources/api_gateway/subresources/user_schemas/methods/get)

Deprecated

GET/zones/{zone_id}/api_gateway/user_schemas/{schema_id}

##### [Upload a legacy schema](https://developers.cloudflare.com/api/resources/api_gateway/subresources/user_schemas/methods/create)

Deprecated

POST/zones/{zone_id}/api_gateway/user_schemas

##### [Enable validation for a schema](https://developers.cloudflare.com/api/resources/api_gateway/subresources/user_schemas/methods/edit)

Deprecated

PATCH/zones/{zone_id}/api_gateway/user_schemas/{schema_id}

##### [Delete a schema](https://developers.cloudflare.com/api/resources/api_gateway/subresources/user_schemas/methods/delete)

Deprecated

DELETE/zones/{zone_id}/api_gateway/user_schemas/{schema_id}

#### API GatewayUser SchemasOperations

##### [Retrieve all operations from a schema](https://developers.cloudflare.com/api/resources/api_gateway/subresources/user_schemas/subresources/operations/methods/list)

Deprecated

GET/zones/{zone_id}/api_gateway/user_schemas/{schema_id}/operations

#### API GatewayUser SchemasHosts

##### [Retrieve schema hosts in a zone](https://developers.cloudflare.com/api/resources/api_gateway/subresources/user_schemas/subresources/hosts/methods/list)

Deprecated

GET/zones/{zone_id}/api_gateway/user_schemas/hosts

#### API GatewayExpression Template

#### API GatewayExpression TemplateFallthrough

##### [Generate a fallthrough WAF expression template](https://developers.cloudflare.com/api/resources/api_gateway/subresources/expression_template/subresources/fallthrough/methods/create)

Deprecated

POST/zones/{zone_id}/api_gateway/expression-template/fallthrough

#### Managed Transforms

##### [List Managed Transforms](https://developers.cloudflare.com/api/resources/managed_transforms/methods/list)

GET/zones/{zone_id}/managed_headers

##### [Update Managed Transforms](https://developers.cloudflare.com/api/resources/managed_transforms/methods/edit)

PATCH/zones/{zone_id}/managed_headers

##### [Delete Managed Transforms](https://developers.cloudflare.com/api/resources/managed_transforms/methods/delete)

DELETE/zones/{zone_id}/managed_headers

#### Page Shield

##### [Get client-side security settings](https://developers.cloudflare.com/api/resources/page_shield/methods/get)

GET/zones/{zone_id}/page_shield

##### [Update client-side security settings](https://developers.cloudflare.com/api/resources/page_shield/methods/update)

PUT/zones/{zone_id}/page_shield

#### Page ShieldPolicies

##### [List content security rules](https://developers.cloudflare.com/api/resources/page_shield/subresources/policies/methods/list)

GET/zones/{zone_id}/page_shield/policies

##### [Get a content security rule](https://developers.cloudflare.com/api/resources/page_shield/subresources/policies/methods/get)

GET/zones/{zone_id}/page_shield/policies/{policy_id}

##### [Create a content security rule](https://developers.cloudflare.com/api/resources/page_shield/subresources/policies/methods/create)

POST/zones/{zone_id}/page_shield/policies

##### [Update a content security rule](https://developers.cloudflare.com/api/resources/page_shield/subresources/policies/methods/update)

PUT/zones/{zone_id}/page_shield/policies/{policy_id}

##### [Delete a content security rule](https://developers.cloudflare.com/api/resources/page_shield/subresources/policies/methods/delete)

DELETE/zones/{zone_id}/page_shield/policies/{policy_id}

#### Page ShieldConnections

##### [List detected connections](https://developers.cloudflare.com/api/resources/page_shield/subresources/connections/methods/list)

GET/zones/{zone_id}/page_shield/connections

##### [Get a detected connection](https://developers.cloudflare.com/api/resources/page_shield/subresources/connections/methods/get)

GET/zones/{zone_id}/page_shield/connections/{connection_id}

#### Page ShieldScripts

##### [List detected scripts](https://developers.cloudflare.com/api/resources/page_shield/subresources/scripts/methods/list)

GET/zones/{zone_id}/page_shield/scripts

##### [Get a detected script](https://developers.cloudflare.com/api/resources/page_shield/subresources/scripts/methods/get)

GET/zones/{zone_id}/page_shield/scripts/{script_id}

#### Page ShieldCookies

##### [List detected cookies](https://developers.cloudflare.com/api/resources/page_shield/subresources/cookies/methods/list)

GET/zones/{zone_id}/page_shield/cookies

##### [Get a detected cookie](https://developers.cloudflare.com/api/resources/page_shield/subresources/cookies/methods/get)

GET/zones/{zone_id}/page_shield/cookies/{cookie_id}

#### Rulesets

##### [List account or zone rulesets](https://developers.cloudflare.com/api/resources/rulesets/methods/list)

GET/{accounts_or_zones}/{account_or_zone_id}/rulesets

##### [Get an account or zone ruleset](https://developers.cloudflare.com/api/resources/rulesets/methods/get)

GET/{accounts_or_zones}/{account_or_zone_id}/rulesets/{ruleset_id}

##### [Create an account or zone ruleset](https://developers.cloudflare.com/api/resources/rulesets/methods/create)

POST/{accounts_or_zones}/{account_or_zone_id}/rulesets

##### [Update an account or zone ruleset](https://developers.cloudflare.com/api/resources/rulesets/methods/update)

PUT/{accounts_or_zones}/{account_or_zone_id}/rulesets/{ruleset_id}

##### [Delete an account or zone ruleset](https://developers.cloudflare.com/api/resources/rulesets/methods/delete)

DELETE/{accounts_or_zones}/{account_or_zone_id}/rulesets/{ruleset_id}

#### RulesetsPhases

##### [Get an account or zone entry point ruleset](https://developers.cloudflare.com/api/resources/rulesets/subresources/phases/methods/get)

GET/{accounts_or_zones}/{account_or_zone_id}/rulesets/phases/{ruleset_phase}/entrypoint

##### [Update an account or zone entry point ruleset](https://developers.cloudflare.com/api/resources/rulesets/subresources/phases/methods/update)

PUT/{accounts_or_zones}/{account_or_zone_id}/rulesets/phases/{ruleset_phase}/entrypoint

#### RulesetsPhasesVersions

##### [List an account or zone entry point ruleset's versions](https://developers.cloudflare.com/api/resources/rulesets/subresources/phases/subresources/versions/methods/list)

GET/{accounts_or_zones}/{account_or_zone_id}/rulesets/phases/{ruleset_phase}/entrypoint/versions

##### [Get an account or zone entry point ruleset version](https://developers.cloudflare.com/api/resources/rulesets/subresources/phases/subresources/versions/methods/get)

GET/{accounts_or_zones}/{account_or_zone_id}/rulesets/phases/{ruleset_phase}/entrypoint/versions/{ruleset_version}

#### RulesetsRules

##### [Create an account or zone ruleset rule](https://developers.cloudflare.com/api/resources/rulesets/subresources/rules/methods/create)

POST/{accounts_or_zones}/{account_or_zone_id}/rulesets/{ruleset_id}/rules

##### [Update an account or zone ruleset rule](https://developers.cloudflare.com/api/resources/rulesets/subresources/rules/methods/edit)

PATCH/{accounts_or_zones}/{account_or_zone_id}/rulesets/{ruleset_id}/rules/{rule_id}

##### [Delete an account or zone ruleset rule](https://developers.cloudflare.com/api/resources/rulesets/subresources/rules/methods/delete)

DELETE/{accounts_or_zones}/{account_or_zone_id}/rulesets/{ruleset_id}/rules/{rule_id}

#### RulesetsVersions

##### [List an account or zone ruleset's versions](https://developers.cloudflare.com/api/resources/rulesets/subresources/versions/methods/list)

GET/{accounts_or_zones}/{account_or_zone_id}/rulesets/{ruleset_id}/versions

##### [Get an account or zone ruleset version](https://developers.cloudflare.com/api/resources/rulesets/subresources/versions/methods/get)

GET/{accounts_or_zones}/{account_or_zone_id}/rulesets/{ruleset_id}/versions/{ruleset_version}

##### [Delete an account or zone ruleset version](https://developers.cloudflare.com/api/resources/rulesets/subresources/versions/methods/delete)

DELETE/{accounts_or_zones}/{account_or_zone_id}/rulesets/{ruleset_id}/versions/{ruleset_version}

#### URL Normalization

##### [Get URL Normalization settings](https://developers.cloudflare.com/api/resources/url_normalization/methods/get)

GET/zones/{zone_id}/url_normalization

##### [Update URL Normalization settings](https://developers.cloudflare.com/api/resources/url_normalization/methods/update)

PUT/zones/{zone_id}/url_normalization

##### [Delete URL Normalization settings](https://developers.cloudflare.com/api/resources/url_normalization/methods/delete)

DELETE/zones/{zone_id}/url_normalization

#### Spectrum

#### SpectrumAnalytics

#### SpectrumAnalyticsAggregates

#### SpectrumAnalyticsAggregatesCurrents

##### [Get current aggregated analytics](https://developers.cloudflare.com/api/resources/spectrum/subresources/analytics/subresources/aggregates/subresources/currents/methods/get)

GET/zones/{zone_id}/spectrum/analytics/aggregate/current

#### SpectrumAnalyticsEvents

#### SpectrumAnalyticsEventsBytimes

##### [Get analytics by time](https://developers.cloudflare.com/api/resources/spectrum/subresources/analytics/subresources/events/subresources/bytimes/methods/get)

GET/zones/{zone_id}/spectrum/analytics/events/bytime

#### SpectrumAnalyticsEventsSummaries

##### [Get analytics summary](https://developers.cloudflare.com/api/resources/spectrum/subresources/analytics/subresources/events/subresources/summaries/methods/get)

GET/zones/{zone_id}/spectrum/analytics/events/summary

#### SpectrumApps

##### [List Spectrum applications](https://developers.cloudflare.com/api/resources/spectrum/subresources/apps/methods/list)

GET/zones/{zone_id}/spectrum/apps

##### [Get Spectrum application configuration](https://developers.cloudflare.com/api/resources/spectrum/subresources/apps/methods/get)

GET/zones/{zone_id}/spectrum/apps/{app_id}

##### [Create Spectrum application using a name for the origin](https://developers.cloudflare.com/api/resources/spectrum/subresources/apps/methods/create)

POST/zones/{zone_id}/spectrum/apps

##### [Update Spectrum application configuration using a name for the origin](https://developers.cloudflare.com/api/resources/spectrum/subresources/apps/methods/update)

PUT/zones/{zone_id}/spectrum/apps/{app_id}

##### [Delete Spectrum application](https://developers.cloudflare.com/api/resources/spectrum/subresources/apps/methods/delete)

DELETE/zones/{zone_id}/spectrum/apps/{app_id}

#### SpectrumProtocols

##### [List Spectrum application protocols](https://developers.cloudflare.com/api/resources/spectrum/subresources/protocols/methods/list)

GET/zones/{zone_id}/spectrum/protocols

#### Addressing

#### AddressingRegional Hostnames

##### [List Regional Hostnames](https://developers.cloudflare.com/api/resources/addressing/subresources/regional_hostnames/methods/list)

GET/zones/{zone_id}/addressing/regional_hostnames

##### [Fetch Regional Hostname](https://developers.cloudflare.com/api/resources/addressing/subresources/regional_hostnames/methods/get)

GET/zones/{zone_id}/addressing/regional_hostnames/{hostname}

##### [Create Regional Hostname](https://developers.cloudflare.com/api/resources/addressing/subresources/regional_hostnames/methods/create)

POST/zones/{zone_id}/addressing/regional_hostnames

##### [Update Regional Hostname](https://developers.cloudflare.com/api/resources/addressing/subresources/regional_hostnames/methods/edit)

PATCH/zones/{zone_id}/addressing/regional_hostnames/{hostname}

##### [Delete Regional Hostname](https://developers.cloudflare.com/api/resources/addressing/subresources/regional_hostnames/methods/delete)

DELETE/zones/{zone_id}/addressing/regional_hostnames/{hostname}

#### AddressingRegional HostnamesRegions

##### [List Regions](https://developers.cloudflare.com/api/resources/addressing/subresources/regional_hostnames/subresources/regions/methods/list)

GET/accounts/{account_id}/addressing/regional_hostnames/regions

#### AddressingServices

##### [List Services](https://developers.cloudflare.com/api/resources/addressing/subresources/services/methods/list)

GET/accounts/{account_id}/addressing/services

#### AddressingAddress Maps

##### [List Address Maps](https://developers.cloudflare.com/api/resources/addressing/subresources/address_maps/methods/list)

GET/accounts/{account_id}/addressing/address_maps

##### [Address Map Details](https://developers.cloudflare.com/api/resources/addressing/subresources/address_maps/methods/get)

GET/accounts/{account_id}/addressing/address_maps/{address_map_id}

##### [Create Address Map](https://developers.cloudflare.com/api/resources/addressing/subresources/address_maps/methods/create)

POST/accounts/{account_id}/addressing/address_maps

##### [Update Address Map](https://developers.cloudflare.com/api/resources/addressing/subresources/address_maps/methods/edit)

PATCH/accounts/{account_id}/addressing/address_maps/{address_map_id}

##### [Delete Address Map](https://developers.cloudflare.com/api/resources/addressing/subresources/address_maps/methods/delete)

DELETE/accounts/{account_id}/addressing/address_maps/{address_map_id}

#### AddressingAddress MapsAccounts

##### [Add an account membership to an Address Map](https://developers.cloudflare.com/api/resources/addressing/subresources/address_maps/subresources/accounts/methods/update)

PUT/accounts/{account_id}/addressing/address_maps/{address_map_id}/accounts/{member_account_id}

##### [Remove an account membership from an Address Map](https://developers.cloudflare.com/api/resources/addressing/subresources/address_maps/subresources/accounts/methods/delete)

DELETE/accounts/{account_id}/addressing/address_maps/{address_map_id}/accounts/{member_account_id}

#### AddressingAddress MapsIPs

##### [Add an IP to an Address Map](https://developers.cloudflare.com/api/resources/addressing/subresources/address_maps/subresources/ips/methods/update)

PUT/accounts/{account_id}/addressing/address_maps/{address_map_id}/ips/{ip_address}

##### [Remove an IP from an Address Map](https://developers.cloudflare.com/api/resources/addressing/subresources/address_maps/subresources/ips/methods/delete)

DELETE/accounts/{account_id}/addressing/address_maps/{address_map_id}/ips/{ip_address}

#### AddressingAddress MapsZones

#### AddressingLOA Documents

##### [Download LOA Document](https://developers.cloudflare.com/api/resources/addressing/subresources/loa_documents/methods/get)

GET/accounts/{account_id}/addressing/loa_documents/{loa_document_id}/download

##### [Upload LOA Document](https://developers.cloudflare.com/api/resources/addressing/subresources/loa_documents/methods/create)

POST/accounts/{account_id}/addressing/loa_documents

#### AddressingPrefixes

##### [List Prefixes](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/methods/list)

GET/accounts/{account_id}/addressing/prefixes

##### [Prefix Details](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/methods/get)

GET/accounts/{account_id}/addressing/prefixes/{prefix_id}

##### [Add Prefix](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/methods/create)

POST/accounts/{account_id}/addressing/prefixes

##### [Update Prefix Description](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/methods/edit)

PATCH/accounts/{account_id}/addressing/prefixes/{prefix_id}

##### [Delete Prefix](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/methods/delete)

DELETE/accounts/{account_id}/addressing/prefixes/{prefix_id}

##### [Validate Prefix](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/methods/validate)

POST/accounts/{account_id}/addressing/prefixes/{prefix_id}/validate

#### AddressingPrefixesService Bindings

##### [List Service Bindings](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/service_bindings/methods/list)

GET/accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings

##### [Get Service Binding](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/service_bindings/methods/get)

GET/accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings/{binding_id}

##### [Create Service Binding](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/service_bindings/methods/create)

POST/accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings

##### [Delete Service Binding](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/service_bindings/methods/delete)

DELETE/accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings/{binding_id}

#### AddressingPrefixesBGP Prefixes

##### [List BGP Prefixes](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/bgp_prefixes/methods/list)

GET/accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes

##### [Fetch BGP Prefix](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/bgp_prefixes/methods/get)

GET/accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes/{bgp_prefix_id}

##### [Create BGP Prefix](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/bgp_prefixes/methods/create)

POST/accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes

##### [Update BGP Prefix](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/bgp_prefixes/methods/edit)

PATCH/accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes/{bgp_prefix_id}

##### [Delete BGP Prefix](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/bgp_prefixes/methods/delete)

DELETE/accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes/{bgp_prefix_id}

#### AddressingPrefixesAdvertisement Status

##### [Get Advertisement Status](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/advertisement_status/methods/get)

Deprecated

GET/accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/status

##### [Update Prefix Dynamic Advertisement Status](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/advertisement_status/methods/edit)

Deprecated

PATCH/accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/status

#### AddressingPrefixesDelegations

##### [List Prefix Delegations](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/delegations/methods/list)

GET/accounts/{account_id}/addressing/prefixes/{prefix_id}/delegations

##### [Create Prefix Delegation](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/delegations/methods/create)

POST/accounts/{account_id}/addressing/prefixes/{prefix_id}/delegations

##### [Delete Prefix Delegation](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/delegations/methods/delete)

DELETE/accounts/{account_id}/addressing/prefixes/{prefix_id}/delegations/{delegation_id}

#### Data Localization Suite

#### Data Localization SuiteRegions

##### [List DLS regions for an account](https://developers.cloudflare.com/api/resources/dls/subresources/regions/methods/list)

GET/accounts/{account_id}/dls/regions

##### [Get a DLS region](https://developers.cloudflare.com/api/resources/dls/subresources/regions/methods/get)

GET/accounts/{account_id}/dls/regions/{region_id}

#### Data Localization SuiteRegional Services

#### Data Localization SuiteRegional ServicesPrefix Bindings

##### [List DLS prefix bindings for an account](https://developers.cloudflare.com/api/resources/dls/subresources/regional_services/subresources/prefix_bindings/methods/list)

GET/accounts/{account_id}/dls/regional_services/prefix_bindings

##### [Get a DLS prefix binding](https://developers.cloudflare.com/api/resources/dls/subresources/regional_services/subresources/prefix_bindings/methods/get)

GET/accounts/{account_id}/dls/regional_services/prefix_bindings/{binding_id}

##### [Create a DLS prefix binding](https://developers.cloudflare.com/api/resources/dls/subresources/regional_services/subresources/prefix_bindings/methods/create)

POST/accounts/{account_id}/dls/regional_services/prefix_bindings

##### [Update a DLS prefix binding](https://developers.cloudflare.com/api/resources/dls/subresources/regional_services/subresources/prefix_bindings/methods/edit)

PATCH/accounts/{account_id}/dls/regional_services/prefix_bindings/{binding_id}

##### [Delete a DLS prefix binding](https://developers.cloudflare.com/api/resources/dls/subresources/regional_services/subresources/prefix_bindings/methods/delete)

DELETE/accounts/{account_id}/dls/regional_services/prefix_bindings/{binding_id}

#### Audit Logs

##### [Get account audit logs](https://developers.cloudflare.com/api/resources/audit_logs/methods/list)

GET/accounts/{account_id}/audit_logs

#### Billing

##### [Validate Billing Address](https://developers.cloudflare.com/api/resources/billing/methods/address_validation)

POST/billing/address-validation

#### BillingProfiles

##### [Get Billing Profile](https://developers.cloudflare.com/api/resources/billing/subresources/profiles/methods/get)

GET/accounts/{account_id}/billing/profile

##### [Create Billing Profile](https://developers.cloudflare.com/api/resources/billing/subresources/profiles/methods/create)

POST/accounts/{account_id}/billing/profile

##### [Update Billing Profile](https://developers.cloudflare.com/api/resources/billing/subresources/profiles/methods/update)

PUT/accounts/{account_id}/billing/profile

##### [Delete Billing Profile](https://developers.cloudflare.com/api/resources/billing/subresources/profiles/methods/delete)

DELETE/accounts/{account_id}/billing/profile

##### [Update Billing Email](https://developers.cloudflare.com/api/resources/billing/subresources/profiles/methods/update_billing_email)

PATCH/accounts/{account_id}/billing/profile

#### BillingProfilesPayment Method

##### [Create Payment Intent for Billing Profile](https://developers.cloudflare.com/api/resources/billing/subresources/profiles/subresources/payment_method/methods/create)

POST/accounts/{account_id}/billing/profile/payment-method

#### BillingUsage

##### [Get Account Billable Usage Info (Version 1, Alpha)](https://developers.cloudflare.com/api/resources/billing/subresources/usage/methods/paygo_info)

Deprecated

GET/accounts/{account_id}/billable-usage/info

##### [Get Account Billable Usage (Version 1, Alpha)](https://developers.cloudflare.com/api/resources/billing/subresources/usage/methods/paygo)

Deprecated

GET/accounts/{account_id}/billable-usage

##### [Get Account Usage (Version 2, Alpha, Restricted)](https://developers.cloudflare.com/api/resources/billing/subresources/usage/methods/get)

Deprecated

GET/accounts/{account_id}/billable/usage

##### [Get Account Billable Usage Info (Version 1, Alpha)](https://developers.cloudflare.com/api/resources/billing/subresources/usage/methods/get_account_usage_info_v1)

GET/accounts/{account_id}/billable-usage/info

##### [Get Account Billable Usage (Version 1, Alpha)](https://developers.cloudflare.com/api/resources/billing/subresources/usage/methods/get_account_usage_v1)

GET/accounts/{account_id}/billable-usage

##### [Get Account Usage (Version 2, Alpha, Restricted)](https://developers.cloudflare.com/api/resources/billing/subresources/usage/methods/get_account_usage_v2)

GET/accounts/{account_id}/billable/usage

#### BillingCredits

##### [Get Account Credits](https://developers.cloudflare.com/api/resources/billing/subresources/credits/methods/get)

GET/accounts/{account_id}/billing/credits

#### BillingHistory

##### [Get Account Billing History](https://developers.cloudflare.com/api/resources/billing/subresources/history/methods/list)

GET/accounts/{account_id}/billing/history

#### BillingBad Debt

##### [Get Account Bad Debt](https://developers.cloudflare.com/api/resources/billing/subresources/bad_debt/methods/get)

GET/accounts/{account_id}/billing/bad-debt

#### BillingUnpaid Invoice

##### [Get Unpaid Invoices](https://developers.cloudflare.com/api/resources/billing/subresources/unpaid_invoice/methods/get)

GET/accounts/{account_id}/billing/unpaid-invoice

#### BillingRate Plans

##### [Get Rate Plan by Public Key](https://developers.cloudflare.com/api/resources/billing/subresources/rate_plans/methods/get)

GET/billing/rate_plans/{public_key}

#### Brand Protection

##### [Create new URL submissions](https://developers.cloudflare.com/api/resources/brand_protection/methods/submit)

POST/accounts/{account_id}/brand-protection/submit

##### [Read submitted URLs by ID](https://developers.cloudflare.com/api/resources/brand_protection/methods/url_info)

GET/accounts/{account_id}/brand-protection/url-info

#### Brand ProtectionQueries

##### [Create new saved string queries](https://developers.cloudflare.com/api/resources/brand_protection/subresources/queries/methods/create)

POST/accounts/{account_id}/brand-protection/queries

##### [Delete saved string queries by ID](https://developers.cloudflare.com/api/resources/brand_protection/subresources/queries/methods/delete)

DELETE/accounts/{account_id}/brand-protection/queries

##### [Create new saved string queries in bulk](https://developers.cloudflare.com/api/resources/brand_protection/subresources/queries/methods/bulk)

POST/accounts/{account_id}/brand-protection/queries/bulk

#### Brand ProtectionMatches

##### [Read matches for string queries by ID](https://developers.cloudflare.com/api/resources/brand_protection/subresources/matches/methods/get)

GET/accounts/{account_id}/brand-protection/matches

##### [Download matches for string queries by ID](https://developers.cloudflare.com/api/resources/brand_protection/subresources/matches/methods/download)

GET/accounts/{account_id}/brand-protection/matches/download

#### Brand ProtectionLogos

##### [Create new saved logo queries from image files](https://developers.cloudflare.com/api/resources/brand_protection/subresources/logos/methods/create)

POST/accounts/{account_id}/brand-protection/logos

##### [Delete saved logo queries by ID](https://developers.cloudflare.com/api/resources/brand_protection/subresources/logos/methods/delete)

DELETE/accounts/{account_id}/brand-protection/logos/{logo_id}

#### Brand ProtectionLogo Matches

##### [Read matches for logo queries by ID](https://developers.cloudflare.com/api/resources/brand_protection/subresources/logo_matches/methods/get)

GET/accounts/{account_id}/brand-protection/logo-matches

##### [Download matches for logo queries by ID](https://developers.cloudflare.com/api/resources/brand_protection/subresources/logo_matches/methods/download)

GET/accounts/{account_id}/brand-protection/logo-matches/download

#### Brand ProtectionV2

#### Brand ProtectionV2Queries

##### [Get queries](https://developers.cloudflare.com/api/resources/brand_protection/subresources/v2/subresources/queries/methods/get)

GET/accounts/{account_id}/cloudforce-one/v2/brand-protection/domain/queries

#### Brand ProtectionV2Matches

##### [List saved query matches](https://developers.cloudflare.com/api/resources/brand_protection/subresources/v2/subresources/matches/methods/get)

GET/accounts/{account_id}/cloudforce-one/v2/brand-protection/domain/matches

#### Brand ProtectionV2Logos

##### [Insert logo query](https://developers.cloudflare.com/api/resources/brand_protection/subresources/v2/subresources/logos/methods/create)

POST/accounts/{account_id}/cloudforce-one/v2/brand-protection/logo/queries

##### [Delete logo query](https://developers.cloudflare.com/api/resources/brand_protection/subresources/v2/subresources/logos/methods/delete)

DELETE/accounts/{account_id}/cloudforce-one/v2/brand-protection/logo/queries/{query_id}

##### [Get logo queries](https://developers.cloudflare.com/api/resources/brand_protection/subresources/v2/subresources/logos/methods/get)

GET/accounts/{account_id}/cloudforce-one/v2/brand-protection/logo/queries

#### Brand ProtectionV2Logo Matches

##### [List logo matches](https://developers.cloudflare.com/api/resources/brand_protection/subresources/v2/subresources/logo_matches/methods/get)

GET/accounts/{account_id}/cloudforce-one/v2/brand-protection/logo/matches

#### Diagnostics

#### DiagnosticsTraceroutes

##### [Traceroute](https://developers.cloudflare.com/api/resources/diagnostics/subresources/traceroutes/methods/create)

POST/accounts/{account_id}/diagnostics/traceroute

#### DiagnosticsEndpoint Healthchecks

##### [List Endpoint Health Checks](https://developers.cloudflare.com/api/resources/diagnostics/subresources/endpoint-healthchecks/methods/list)

GET/accounts/{account_id}/diagnostics/endpoint-healthchecks

##### [Endpoint Health Check](https://developers.cloudflare.com/api/resources/diagnostics/subresources/endpoint-healthchecks/methods/create)

POST/accounts/{account_id}/diagnostics/endpoint-healthchecks

##### [Get Endpoint Health Check](https://developers.cloudflare.com/api/resources/diagnostics/subresources/endpoint-healthchecks/methods/get)

GET/accounts/{account_id}/diagnostics/endpoint-healthchecks/{id}

##### [Delete Endpoint Health Check](https://developers.cloudflare.com/api/resources/diagnostics/subresources/endpoint-healthchecks/methods/delete)

DELETE/accounts/{account_id}/diagnostics/endpoint-healthchecks/{id}

##### [Update Endpoint Health Check](https://developers.cloudflare.com/api/resources/diagnostics/subresources/endpoint-healthchecks/methods/update)

PUT/accounts/{account_id}/diagnostics/endpoint-healthchecks/{id}

#### Images

#### ImagesV1

##### [List images](https://developers.cloudflare.com/api/resources/images/subresources/v1/methods/list)

Deprecated

GET/accounts/{account_id}/images/v1

##### [Image details](https://developers.cloudflare.com/api/resources/images/subresources/v1/methods/get)

GET/accounts/{account_id}/images/v1/{image_id}

##### [Upload an image](https://developers.cloudflare.com/api/resources/images/subresources/v1/methods/create)

POST/accounts/{account_id}/images/v1

##### [Update image](https://developers.cloudflare.com/api/resources/images/subresources/v1/methods/edit)

PATCH/accounts/{account_id}/images/v1/{image_id}

##### [Delete image](https://developers.cloudflare.com/api/resources/images/subresources/v1/methods/delete)

DELETE/accounts/{account_id}/images/v1/{image_id}

#### ImagesV1Keys

##### [List Signing Keys](https://developers.cloudflare.com/api/resources/images/subresources/v1/subresources/keys/methods/list)

GET/accounts/{account_id}/images/v1/keys

##### [Create a new Signing Key](https://developers.cloudflare.com/api/resources/images/subresources/v1/subresources/keys/methods/update)

PUT/accounts/{account_id}/images/v1/keys/{signing_key_name}

##### [Delete Signing Key](https://developers.cloudflare.com/api/resources/images/subresources/v1/subresources/keys/methods/delete)

DELETE/accounts/{account_id}/images/v1/keys/{signing_key_name}

#### ImagesV1Stats

##### [Images usage statistics](https://developers.cloudflare.com/api/resources/images/subresources/v1/subresources/stats/methods/get)

GET/accounts/{account_id}/images/v1/stats

#### ImagesV1Variants

##### [List variants](https://developers.cloudflare.com/api/resources/images/subresources/v1/subresources/variants/methods/list)

GET/accounts/{account_id}/images/v1/variants

##### [Variant details](https://developers.cloudflare.com/api/resources/images/subresources/v1/subresources/variants/methods/get)

GET/accounts/{account_id}/images/v1/variants/{variant_id}

##### [Create a variant](https://developers.cloudflare.com/api/resources/images/subresources/v1/subresources/variants/methods/create)

POST/accounts/{account_id}/images/v1/variants

##### [Update a variant](https://developers.cloudflare.com/api/resources/images/subresources/v1/subresources/variants/methods/edit)

PATCH/accounts/{account_id}/images/v1/variants/{variant_id}

##### [Delete a variant](https://developers.cloudflare.com/api/resources/images/subresources/v1/subresources/variants/methods/delete)

DELETE/accounts/{account_id}/images/v1/variants/{variant_id}

#### ImagesV1Blobs

##### [Download image](https://developers.cloudflare.com/api/resources/images/subresources/v1/subresources/blobs/methods/get)

GET/accounts/{account_id}/images/v1/{image_id}/blob

#### ImagesV2

##### [List images V2](https://developers.cloudflare.com/api/resources/images/subresources/v2/methods/list)

GET/accounts/{account_id}/images/v2

#### ImagesV2Direct Uploads

##### [Create authenticated direct upload URL V2](https://developers.cloudflare.com/api/resources/images/subresources/v2/subresources/direct_uploads/methods/create)

POST/accounts/{account_id}/images/v2/direct_upload

#### Intel

#### IntelASN

##### [Get ASN Overview.](https://developers.cloudflare.com/api/resources/intel/subresources/asn/methods/get)

GET/accounts/{account_id}/intel/asn/{asn}

#### IntelASNSubnets

##### [Get ASN Subnets](https://developers.cloudflare.com/api/resources/intel/subresources/asn/subresources/subnets/methods/get)

GET/accounts/{account_id}/intel/asn/{asn}/subnets

#### IntelDNS

##### [Get Passive DNS by IP](https://developers.cloudflare.com/api/resources/intel/subresources/dns/methods/list)

GET/accounts/{account_id}/intel/dns

#### IntelDomains

##### [Get Domain Details](https://developers.cloudflare.com/api/resources/intel/subresources/domains/methods/get)

GET/accounts/{account_id}/intel/domain

#### IntelDomainsBulks

##### [Get Multiple Domain Details](https://developers.cloudflare.com/api/resources/intel/subresources/domains/subresources/bulks/methods/get)

GET/accounts/{account_id}/intel/domain/bulk

#### IntelDomain History

##### [Get Domain History](https://developers.cloudflare.com/api/resources/intel/subresources/domain_history/methods/get)

GET/accounts/{account_id}/intel/domain-history

#### IntelIPs

##### [Get IP Overview](https://developers.cloudflare.com/api/resources/intel/subresources/ips/methods/get)

GET/accounts/{account_id}/intel/ip

#### IntelIP Lists

#### IntelMiscategorizations

##### [Create Miscategorization](https://developers.cloudflare.com/api/resources/intel/subresources/miscategorizations/methods/create)

POST/accounts/{account_id}/intel/miscategorization

#### IntelWhois

##### [Get WHOIS Record](https://developers.cloudflare.com/api/resources/intel/subresources/whois/methods/get)

GET/accounts/{account_id}/intel/whois

#### IntelURLs

##### [Get URL Intelligence](https://developers.cloudflare.com/api/resources/intel/subresources/urls/methods/get)

GET/accounts/{account_id}/intel/url

#### IntelIndicator Feeds

##### [Get indicator feeds owned by this account](https://developers.cloudflare.com/api/resources/intel/subresources/indicator_feeds/methods/list)

GET/accounts/{account_id}/intel/indicator-feeds

##### [Get indicator feed metadata](https://developers.cloudflare.com/api/resources/intel/subresources/indicator_feeds/methods/get)

GET/accounts/{account_id}/intel/indicator-feeds/{feed_id}

##### [Create new indicator feed](https://developers.cloudflare.com/api/resources/intel/subresources/indicator_feeds/methods/create)

POST/accounts/{account_id}/intel/indicator-feeds

##### [Update indicator feed metadata](https://developers.cloudflare.com/api/resources/intel/subresources/indicator_feeds/methods/update)

PUT/accounts/{account_id}/intel/indicator-feeds/{feed_id}

##### [Get indicator feed data](https://developers.cloudflare.com/api/resources/intel/subresources/indicator_feeds/methods/data)

GET/accounts/{account_id}/intel/indicator-feeds/{feed_id}/data

#### IntelIndicator FeedsSnapshots

##### [Update indicator feed data](https://developers.cloudflare.com/api/resources/intel/subresources/indicator_feeds/subresources/snapshots/methods/update)

PUT/accounts/{account_id}/intel/indicator-feeds/{feed_id}/snapshot

#### IntelIndicator FeedsPermissions

##### [List indicator feed permissions](https://developers.cloudflare.com/api/resources/intel/subresources/indicator_feeds/subresources/permissions/methods/list)

GET/accounts/{account_id}/intel/indicator-feeds/permissions/view

##### [Grant permission to indicator feed](https://developers.cloudflare.com/api/resources/intel/subresources/indicator_feeds/subresources/permissions/methods/create)

PUT/accounts/{account_id}/intel/indicator-feeds/permissions/add

##### [Revoke permission to indicator feed](https://developers.cloudflare.com/api/resources/intel/subresources/indicator_feeds/subresources/permissions/methods/delete)

PUT/accounts/{account_id}/intel/indicator-feeds/permissions/remove

#### IntelIndicator FeedsDownloads

#### IntelSinkholes

##### [List sinkholes owned by this account](https://developers.cloudflare.com/api/resources/intel/subresources/sinkholes/methods/list)

GET/accounts/{account_id}/intel/sinkholes

##### [Get a sinkhole](https://developers.cloudflare.com/api/resources/intel/subresources/sinkholes/methods/get)

GET/accounts/{account_id}/intel/sinkholes/{sinkhole_id}

##### [Create a new sinkhole for your account](https://developers.cloudflare.com/api/resources/intel/subresources/sinkholes/methods/create)

POST/accounts/{account_id}/intel/sinkholes

##### [Update a sinkhole](https://developers.cloudflare.com/api/resources/intel/subresources/sinkholes/methods/update)

PUT/accounts/{account_id}/intel/sinkholes/{sinkhole_id}

##### [Delete a sinkhole](https://developers.cloudflare.com/api/resources/intel/subresources/sinkholes/methods/delete)

DELETE/accounts/{account_id}/intel/sinkholes/{sinkhole_id}

#### IntelSinkholesIngresses

##### [Create an ingress rule](https://developers.cloudflare.com/api/resources/intel/subresources/sinkholes/subresources/ingresses/methods/create)

POST/zones/{zone_id}/intel/sinkholes/{sinkhole_id}/ingresses

##### [Get an ingress rule](https://developers.cloudflare.com/api/resources/intel/subresources/sinkholes/subresources/ingresses/methods/get)

GET/zones/{zone_id}/intel/sinkholes/{sinkhole_id}/ingresses/{ingress_id}

##### [Update an ingress rule](https://developers.cloudflare.com/api/resources/intel/subresources/sinkholes/subresources/ingresses/methods/update)

PUT/zones/{zone_id}/intel/sinkholes/{sinkhole_id}/ingresses/{ingress_id}

##### [Delete an ingress rule](https://developers.cloudflare.com/api/resources/intel/subresources/sinkholes/subresources/ingresses/methods/delete)

DELETE/zones/{zone_id}/intel/sinkholes/{sinkhole_id}/ingresses/{ingress_id}

#### IntelAttack Surface Report

#### IntelAttack Surface ReportIssue Types

##### [Retrieves Security Center Issues Types](https://developers.cloudflare.com/api/resources/intel/subresources/attack_surface_report/subresources/issue_types/methods/get)

GET/accounts/{account_id}/intel/attack-surface-report/issue-types

#### IntelAttack Surface ReportIssues

##### [Retrieves Security Center Issues](https://developers.cloudflare.com/api/resources/intel/subresources/attack_surface_report/subresources/issues/methods/list)

Deprecated

GET/accounts/{account_id}/intel/attack-surface-report/issues

##### [Retrieves Security Center Issue Counts by Class](https://developers.cloudflare.com/api/resources/intel/subresources/attack_surface_report/subresources/issues/methods/class)

Deprecated

GET/accounts/{account_id}/intel/attack-surface-report/issues/class

##### [Retrieves Security Center Issue Counts by Severity](https://developers.cloudflare.com/api/resources/intel/subresources/attack_surface_report/subresources/issues/methods/severity)

Deprecated

GET/accounts/{account_id}/intel/attack-surface-report/issues/severity

##### [Retrieves Security Center Issue Counts by Type](https://developers.cloudflare.com/api/resources/intel/subresources/attack_surface_report/subresources/issues/methods/type)

Deprecated

GET/accounts/{account_id}/intel/attack-surface-report/issues/type

#### Magic Transit

#### Magic TransitApps

##### [List Apps](https://developers.cloudflare.com/api/resources/magic_transit/subresources/apps/methods/list)

GET/accounts/{account_id}/magic/apps

##### [Create a new App](https://developers.cloudflare.com/api/resources/magic_transit/subresources/apps/methods/create)

POST/accounts/{account_id}/magic/apps

##### [Update an App](https://developers.cloudflare.com/api/resources/magic_transit/subresources/apps/methods/update)

PUT/accounts/{account_id}/magic/apps/{account_app_id}

##### [Update an App](https://developers.cloudflare.com/api/resources/magic_transit/subresources/apps/methods/edit)

PATCH/accounts/{account_id}/magic/apps/{account_app_id}

##### [Delete Account App](https://developers.cloudflare.com/api/resources/magic_transit/subresources/apps/methods/delete)

DELETE/accounts/{account_id}/magic/apps/{account_app_id}

#### Magic TransitCf Interconnects

##### [List interconnects](https://developers.cloudflare.com/api/resources/magic_transit/subresources/cf_interconnects/methods/list)

GET/accounts/{account_id}/magic/cf_interconnects

##### [List interconnect Details](https://developers.cloudflare.com/api/resources/magic_transit/subresources/cf_interconnects/methods/get)

GET/accounts/{account_id}/magic/cf_interconnects/{cf_interconnect_id}

##### [Update interconnect](https://developers.cloudflare.com/api/resources/magic_transit/subresources/cf_interconnects/methods/update)

PUT/accounts/{account_id}/magic/cf_interconnects/{cf_interconnect_id}

##### [Update multiple interconnects](https://developers.cloudflare.com/api/resources/magic_transit/subresources/cf_interconnects/methods/bulk_update)

PUT/accounts/{account_id}/magic/cf_interconnects

#### Magic TransitGRE Tunnels

##### [List GRE tunnels](https://developers.cloudflare.com/api/resources/magic_transit/subresources/gre_tunnels/methods/list)

GET/accounts/{account_id}/magic/gre_tunnels

##### [List GRE Tunnel Details](https://developers.cloudflare.com/api/resources/magic_transit/subresources/gre_tunnels/methods/get)

GET/accounts/{account_id}/magic/gre_tunnels/{gre_tunnel_id}

##### [Create a GRE tunnel](https://developers.cloudflare.com/api/resources/magic_transit/subresources/gre_tunnels/methods/create)

POST/accounts/{account_id}/magic/gre_tunnels

##### [Update GRE Tunnel](https://developers.cloudflare.com/api/resources/magic_transit/subresources/gre_tunnels/methods/update)

PUT/accounts/{account_id}/magic/gre_tunnels/{gre_tunnel_id}

##### [Delete GRE Tunnel](https://developers.cloudflare.com/api/resources/magic_transit/subresources/gre_tunnels/methods/delete)

DELETE/accounts/{account_id}/magic/gre_tunnels/{gre_tunnel_id}

##### [Update multiple GRE tunnels](https://developers.cloudflare.com/api/resources/magic_transit/subresources/gre_tunnels/methods/bulk_update)

PUT/accounts/{account_id}/magic/gre_tunnels

#### Magic TransitIPSEC Tunnels

##### [List IPsec tunnels](https://developers.cloudflare.com/api/resources/magic_transit/subresources/ipsec_tunnels/methods/list)

GET/accounts/{account_id}/magic/ipsec_tunnels

##### [List IPsec tunnel details](https://developers.cloudflare.com/api/resources/magic_transit/subresources/ipsec_tunnels/methods/get)

GET/accounts/{account_id}/magic/ipsec_tunnels/{ipsec_tunnel_id}

##### [Create an IPsec tunnel](https://developers.cloudflare.com/api/resources/magic_transit/subresources/ipsec_tunnels/methods/create)

POST/accounts/{account_id}/magic/ipsec_tunnels

##### [Update IPsec Tunnel](https://developers.cloudflare.com/api/resources/magic_transit/subresources/ipsec_tunnels/methods/update)

PUT/accounts/{account_id}/magic/ipsec_tunnels/{ipsec_tunnel_id}

##### [Delete IPsec Tunnel](https://developers.cloudflare.com/api/resources/magic_transit/subresources/ipsec_tunnels/methods/delete)

DELETE/accounts/{account_id}/magic/ipsec_tunnels/{ipsec_tunnel_id}

##### [Update multiple IPsec tunnels](https://developers.cloudflare.com/api/resources/magic_transit/subresources/ipsec_tunnels/methods/bulk_update)

PUT/accounts/{account_id}/magic/ipsec_tunnels

##### [Generate Pre-Shared Key (PSK) for IPsec tunnels](https://developers.cloudflare.com/api/resources/magic_transit/subresources/ipsec_tunnels/methods/psk_generate)

POST/accounts/{account_id}/magic/ipsec_tunnels/{ipsec_tunnel_id}/psk_generate

##### [Set Pre-Shared Keys (PSK) for IPsec tunnels](https://developers.cloudflare.com/api/resources/magic_transit/subresources/ipsec_tunnels/methods/psk_set)

POST/accounts/{account_id}/magic/ipsec_tunnels/psk

#### Magic TransitRoutes

##### [List Routes](https://developers.cloudflare.com/api/resources/magic_transit/subresources/routes/methods/list)

GET/accounts/{account_id}/magic/routes

##### [Route Details](https://developers.cloudflare.com/api/resources/magic_transit/subresources/routes/methods/get)

GET/accounts/{account_id}/magic/routes/{route_id}

##### [Create a Route](https://developers.cloudflare.com/api/resources/magic_transit/subresources/routes/methods/create)

POST/accounts/{account_id}/magic/routes

##### [Update Route](https://developers.cloudflare.com/api/resources/magic_transit/subresources/routes/methods/update)

PUT/accounts/{account_id}/magic/routes/{route_id}

##### [Delete Route](https://developers.cloudflare.com/api/resources/magic_transit/subresources/routes/methods/delete)

DELETE/accounts/{account_id}/magic/routes/{route_id}

##### [Update Many Routes](https://developers.cloudflare.com/api/resources/magic_transit/subresources/routes/methods/bulk_update)

PUT/accounts/{account_id}/magic/routes

##### [Delete Many Routes](https://developers.cloudflare.com/api/resources/magic_transit/subresources/routes/methods/empty)

DELETE/accounts/{account_id}/magic/routes

#### Magic TransitBGP Filter Profiles

##### [List BGP Filter Profiles](https://developers.cloudflare.com/api/resources/magic_transit/subresources/bgp_filter_profiles/methods/list)

GET/accounts/{account_id}/magic/bgp/filter_profiles

##### [Get BGP Filter Profile](https://developers.cloudflare.com/api/resources/magic_transit/subresources/bgp_filter_profiles/methods/get)

GET/accounts/{account_id}/magic/bgp/filter_profiles/{profile_id}

##### [Create BGP Filter Profile](https://developers.cloudflare.com/api/resources/magic_transit/subresources/bgp_filter_profiles/methods/create)

POST/accounts/{account_id}/magic/bgp/filter_profiles

##### [Update BGP Filter Profile](https://developers.cloudflare.com/api/resources/magic_transit/subresources/bgp_filter_profiles/methods/update)

PUT/accounts/{account_id}/magic/bgp/filter_profiles/{profile_id}

##### [Delete BGP Filter Profile](https://developers.cloudflare.com/api/resources/magic_transit/subresources/bgp_filter_profiles/methods/delete)

DELETE/accounts/{account_id}/magic/bgp/filter_profiles/{profile_id}

#### Magic TransitSites

##### [List Sites](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/methods/list)

GET/accounts/{account_id}/magic/sites

##### [Site Details](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/methods/get)

GET/accounts/{account_id}/magic/sites/{site_id}

##### [Create a new Site](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/methods/create)

POST/accounts/{account_id}/magic/sites

##### [Update Site](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/methods/update)

PUT/accounts/{account_id}/magic/sites/{site_id}

##### [Patch Site](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/methods/edit)

PATCH/accounts/{account_id}/magic/sites/{site_id}

##### [Delete Site](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/methods/delete)

DELETE/accounts/{account_id}/magic/sites/{site_id}

#### Magic TransitSitesApp Configuration

##### [List App Configs](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/app_configuration/methods/list)

GET/accounts/{account_id}/magic/sites/{site_id}/app_configs

##### [Create a new App Config](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/app_configuration/methods/create)

POST/accounts/{account_id}/magic/sites/{site_id}/app_configs

##### [Update an App Config](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/app_configuration/methods/update)

PUT/accounts/{account_id}/magic/sites/{site_id}/app_configs/{app_config_id}

##### [Update an App Config](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/app_configuration/methods/edit)

PATCH/accounts/{account_id}/magic/sites/{site_id}/app_configs/{app_config_id}

##### [Delete App Config](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/app_configuration/methods/delete)

DELETE/accounts/{account_id}/magic/sites/{site_id}/app_configs/{app_config_id}

#### Magic TransitSitesACLs

##### [List Site ACLs](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/acls/methods/list)

GET/accounts/{account_id}/magic/sites/{site_id}/acls

##### [Site ACL Details](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/acls/methods/get)

GET/accounts/{account_id}/magic/sites/{site_id}/acls/{acl_id}

##### [Create a new Site ACL](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/acls/methods/create)

POST/accounts/{account_id}/magic/sites/{site_id}/acls

##### [Update Site ACL](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/acls/methods/update)

PUT/accounts/{account_id}/magic/sites/{site_id}/acls/{acl_id}

##### [Patch Site ACL](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/acls/methods/edit)

PATCH/accounts/{account_id}/magic/sites/{site_id}/acls/{acl_id}

##### [Delete Site ACL](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/acls/methods/delete)

DELETE/accounts/{account_id}/magic/sites/{site_id}/acls/{acl_id}

#### Magic TransitSitesLANs

##### [List Site LANs](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/lans/methods/list)

GET/accounts/{account_id}/magic/sites/{site_id}/lans

##### [Site LAN Details](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/lans/methods/get)

GET/accounts/{account_id}/magic/sites/{site_id}/lans/{lan_id}

##### [Create a new Site LAN](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/lans/methods/create)

POST/accounts/{account_id}/magic/sites/{site_id}/lans

##### [Update Site LAN](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/lans/methods/update)

PUT/accounts/{account_id}/magic/sites/{site_id}/lans/{lan_id}

##### [Patch Site LAN](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/lans/methods/edit)

PATCH/accounts/{account_id}/magic/sites/{site_id}/lans/{lan_id}

##### [Delete Site LAN](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/lans/methods/delete)

DELETE/accounts/{account_id}/magic/sites/{site_id}/lans/{lan_id}

#### Magic TransitSitesWANs

##### [List Site WANs](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/wans/methods/list)

GET/accounts/{account_id}/magic/sites/{site_id}/wans

##### [Site WAN Details](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/wans/methods/get)

GET/accounts/{account_id}/magic/sites/{site_id}/wans/{wan_id}

##### [Create a new Site WAN](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/wans/methods/create)

POST/accounts/{account_id}/magic/sites/{site_id}/wans

##### [Update Site WAN](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/wans/methods/update)

PUT/accounts/{account_id}/magic/sites/{site_id}/wans/{wan_id}

##### [Patch Site WAN](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/wans/methods/edit)

PATCH/accounts/{account_id}/magic/sites/{site_id}/wans/{wan_id}

##### [Delete Site WAN](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/wans/methods/delete)

DELETE/accounts/{account_id}/magic/sites/{site_id}/wans/{wan_id}

#### Magic TransitConnectors

##### [List Connectors](https://developers.cloudflare.com/api/resources/magic_transit/subresources/connectors/methods/list)

GET/accounts/{account_id}/magic/connectors

##### [Get Connector](https://developers.cloudflare.com/api/resources/magic_transit/subresources/connectors/methods/get)

GET/accounts/{account_id}/magic/connectors/{connector_id}

##### [Create Connector](https://developers.cloudflare.com/api/resources/magic_transit/subresources/connectors/methods/create)

POST/accounts/{account_id}/magic/connectors

##### [Update Connector](https://developers.cloudflare.com/api/resources/magic_transit/subresources/connectors/methods/update)

PUT/accounts/{account_id}/magic/connectors/{connector_id}

##### [Edit Connector](https://developers.cloudflare.com/api/resources/magic_transit/subresources/connectors/methods/edit)

PATCH/accounts/{account_id}/magic/connectors/{connector_id}

##### [Delete Connector](https://developers.cloudflare.com/api/resources/magic_transit/subresources/connectors/methods/delete)

DELETE/accounts/{account_id}/magic/connectors/{connector_id}

#### Magic TransitConnectorsInterrupts

##### [List Interrupts](https://developers.cloudflare.com/api/resources/magic_transit/subresources/connectors/subresources/interrupts/methods/list)

GET/accounts/{account_id}/magic/connectors/{connector_id}/interrupts

##### [Create Interrupt](https://developers.cloudflare.com/api/resources/magic_transit/subresources/connectors/subresources/interrupts/methods/create)

POST/accounts/{account_id}/magic/connectors/{connector_id}/interrupts

#### Magic TransitConnectorsEvents

##### [List Events](https://developers.cloudflare.com/api/resources/magic_transit/subresources/connectors/subresources/events/methods/list)

GET/accounts/{account_id}/magic/connectors/{connector_id}/telemetry/events

##### [Get Event](https://developers.cloudflare.com/api/resources/magic_transit/subresources/connectors/subresources/events/methods/get)

GET/accounts/{account_id}/magic/connectors/{connector_id}/telemetry/events/{event_t}.{event_n}

#### Magic TransitConnectorsEventsLatest

##### [Get latest Events](https://developers.cloudflare.com/api/resources/magic_transit/subresources/connectors/subresources/events/subresources/latest/methods/list)

GET/accounts/{account_id}/magic/connectors/{connector_id}/telemetry/events/latest

#### Magic TransitConnectorsSnapshots

##### [List Snapshots](https://developers.cloudflare.com/api/resources/magic_transit/subresources/connectors/subresources/snapshots/methods/list)

GET/accounts/{account_id}/magic/connectors/{connector_id}/telemetry/snapshots

##### [Get Snapshot](https://developers.cloudflare.com/api/resources/magic_transit/subresources/connectors/subresources/snapshots/methods/get)

GET/accounts/{account_id}/magic/connectors/{connector_id}/telemetry/snapshots/{snapshot_t}

#### Magic TransitConnectorsSnapshotsLatest

##### [Get latest Snapshots](https://developers.cloudflare.com/api/resources/magic_transit/subresources/connectors/subresources/snapshots/subresources/latest/methods/list)

GET/accounts/{account_id}/magic/connectors/{connector_id}/telemetry/snapshots/latest

#### Magic TransitCf1 Sites

##### [List CF1 Sites](https://developers.cloudflare.com/api/resources/magic_transit/subresources/cf1_sites/methods/list)

GET/accounts/{account_id}/magic/cf1_sites

##### [Get CF1 Site](https://developers.cloudflare.com/api/resources/magic_transit/subresources/cf1_sites/methods/get)

GET/accounts/{account_id}/magic/cf1_sites/{cf1_site_id}

##### [Create CF1 Sites](https://developers.cloudflare.com/api/resources/magic_transit/subresources/cf1_sites/methods/create)

POST/accounts/{account_id}/magic/cf1_sites

##### [Update CF1 Site](https://developers.cloudflare.com/api/resources/magic_transit/subresources/cf1_sites/methods/update)

PATCH/accounts/{account_id}/magic/cf1_sites/{cf1_site_id}

##### [Delete CF1 Site](https://developers.cloudflare.com/api/resources/magic_transit/subresources/cf1_sites/methods/delete)

DELETE/accounts/{account_id}/magic/cf1_sites/{cf1_site_id}

#### Magic TransitCf1 SitesRamps

##### [List CF1 Site Ramps](https://developers.cloudflare.com/api/resources/magic_transit/subresources/cf1_sites/subresources/ramps/methods/list)

GET/accounts/{account_id}/magic/cf1_sites/{cf1_site_id}/ramps

##### [Get CF1 Site Ramp](https://developers.cloudflare.com/api/resources/magic_transit/subresources/cf1_sites/subresources/ramps/methods/get)

GET/accounts/{account_id}/magic/cf1_sites/{cf1_site_id}/ramps/{ramp_id}

##### [Create CF1 Site Ramps](https://developers.cloudflare.com/api/resources/magic_transit/subresources/cf1_sites/subresources/ramps/methods/create)

POST/accounts/{account_id}/magic/cf1_sites/{cf1_site_id}/ramps

##### [Delete CF1 Site Ramp](https://developers.cloudflare.com/api/resources/magic_transit/subresources/cf1_sites/subresources/ramps/methods/delete)

DELETE/accounts/{account_id}/magic/cf1_sites/{cf1_site_id}/ramps/{ramp_id}

#### Magic TransitPCAPs

##### [List packet capture requests](https://developers.cloudflare.com/api/resources/magic_transit/subresources/pcaps/methods/list)

GET/accounts/{account_id}/pcaps

##### [Get PCAP request](https://developers.cloudflare.com/api/resources/magic_transit/subresources/pcaps/methods/get)

GET/accounts/{account_id}/pcaps/{pcap_id}

##### [Create PCAP request](https://developers.cloudflare.com/api/resources/magic_transit/subresources/pcaps/methods/create)

POST/accounts/{account_id}/pcaps

##### [Stop full PCAP](https://developers.cloudflare.com/api/resources/magic_transit/subresources/pcaps/methods/stop)

PUT/accounts/{account_id}/pcaps/{pcap_id}/stop

#### Magic TransitPCAPsOwnership

##### [List PCAPs Bucket Ownership](https://developers.cloudflare.com/api/resources/magic_transit/subresources/pcaps/subresources/ownership/methods/get)

GET/accounts/{account_id}/pcaps/ownership

##### [Add buckets for full packet captures](https://developers.cloudflare.com/api/resources/magic_transit/subresources/pcaps/subresources/ownership/methods/create)

POST/accounts/{account_id}/pcaps/ownership

##### [Delete buckets for full packet captures](https://developers.cloudflare.com/api/resources/magic_transit/subresources/pcaps/subresources/ownership/methods/delete)

DELETE/accounts/{account_id}/pcaps/ownership/{ownership_id}

##### [Validate buckets for full packet captures](https://developers.cloudflare.com/api/resources/magic_transit/subresources/pcaps/subresources/ownership/methods/validate)

POST/accounts/{account_id}/pcaps/ownership/validate

#### Magic TransitPCAPsDownload

##### [Download Simple PCAP](https://developers.cloudflare.com/api/resources/magic_transit/subresources/pcaps/subresources/download/methods/get)

GET/accounts/{account_id}/pcaps/{pcap_id}/download

#### DDoS Protection

#### DDoS ProtectionAdvanced TCP Protection

#### DDoS ProtectionAdvanced TCP ProtectionAllowlist

##### [List all allowlist prefixes.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/allowlist/methods/list)

GET/accounts/{account_id}/magic/advanced_tcp_protection/configs/allowlist

##### [Create allowlist prefix.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/allowlist/methods/create)

POST/accounts/{account_id}/magic/advanced_tcp_protection/configs/allowlist

##### [Delete all allowlist prefixes.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/allowlist/methods/bulk_delete)

DELETE/accounts/{account_id}/magic/advanced_tcp_protection/configs/allowlist

#### DDoS ProtectionAdvanced TCP ProtectionAllowlistItems

##### [Get allowlist prefix.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/allowlist/subresources/items/methods/get)

GET/accounts/{account_id}/magic/advanced_tcp_protection/configs/allowlist/{prefix_id}

##### [Update allowlist prefix.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/allowlist/subresources/items/methods/edit)

PATCH/accounts/{account_id}/magic/advanced_tcp_protection/configs/allowlist/{prefix_id}

##### [Delete allowlist prefix.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/allowlist/subresources/items/methods/delete)

DELETE/accounts/{account_id}/magic/advanced_tcp_protection/configs/allowlist/{prefix_id}

#### DDoS ProtectionAdvanced TCP ProtectionPrefixes

##### [List all prefixes.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/prefixes/methods/list)

GET/accounts/{account_id}/magic/advanced_tcp_protection/configs/prefixes

##### [Create prefix.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/prefixes/methods/create)

POST/accounts/{account_id}/magic/advanced_tcp_protection/configs/prefixes

##### [Delete all prefixes.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/prefixes/methods/bulk_delete)

DELETE/accounts/{account_id}/magic/advanced_tcp_protection/configs/prefixes

##### [Create multiple prefixes.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/prefixes/methods/bulk_create)

POST/accounts/{account_id}/magic/advanced_tcp_protection/configs/prefixes/bulk

#### DDoS ProtectionAdvanced TCP ProtectionPrefixesItems

##### [Get prefix.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/prefixes/subresources/items/methods/get)

GET/accounts/{account_id}/magic/advanced_tcp_protection/configs/prefixes/{prefix_id}

##### [Update prefix.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/prefixes/subresources/items/methods/edit)

PATCH/accounts/{account_id}/magic/advanced_tcp_protection/configs/prefixes/{prefix_id}

##### [Delete prefix.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/prefixes/subresources/items/methods/delete)

DELETE/accounts/{account_id}/magic/advanced_tcp_protection/configs/prefixes/{prefix_id}

#### DDoS ProtectionAdvanced TCP ProtectionSYN Protection

#### DDoS ProtectionAdvanced TCP ProtectionSYN ProtectionFilters

##### [List all SYN Protection filters.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/syn_protection/subresources/filters/methods/list)

GET/accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/filters

##### [Create a SYN Protection filter.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/syn_protection/subresources/filters/methods/create)

POST/accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/filters

##### [Delete all SYN Protection filters.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/syn_protection/subresources/filters/methods/bulk_delete)

DELETE/accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/filters

#### DDoS ProtectionAdvanced TCP ProtectionSYN ProtectionFiltersItems

##### [Get SYN Protection filter.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/syn_protection/subresources/filters/subresources/items/methods/get)

GET/accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/filters/{filter_id}

##### [Update SYN Protection filter.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/syn_protection/subresources/filters/subresources/items/methods/edit)

PATCH/accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/filters/{filter_id}

##### [Delete SYN Protection filter.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/syn_protection/subresources/filters/subresources/items/methods/delete)

DELETE/accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/filters/{filter_id}

#### DDoS ProtectionAdvanced TCP ProtectionSYN ProtectionRules

##### [List all SYN Protection rules.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/syn_protection/subresources/rules/methods/list)

GET/accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/rules

##### [Create SYN Protection rule.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/syn_protection/subresources/rules/methods/create)

POST/accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/rules

##### [Delete all SYN Protection rules.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/syn_protection/subresources/rules/methods/bulk_delete)

DELETE/accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/rules

#### DDoS ProtectionAdvanced TCP ProtectionSYN ProtectionRulesItems

##### [Get SYN Protection rule.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/syn_protection/subresources/rules/subresources/items/methods/get)

GET/accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/rules/{rule_id}

##### [Update SYN Protection rule.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/syn_protection/subresources/rules/subresources/items/methods/edit)

PATCH/accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/rules/{rule_id}

##### [Delete SYN Protection rule.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/syn_protection/subresources/rules/subresources/items/methods/delete)

DELETE/accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/rules/{rule_id}

#### DDoS ProtectionAdvanced TCP ProtectionTCP Flow Protection

#### DDoS ProtectionAdvanced TCP ProtectionTCP Flow ProtectionFilters

##### [List all TCP Flow Protection filters.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/tcp_flow_protection/subresources/filters/methods/list)

GET/accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/filters

##### [Create a TCP Flow Protection filter.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/tcp_flow_protection/subresources/filters/methods/create)

POST/accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/filters

##### [Delete all TCP Flow Protection filters.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/tcp_flow_protection/subresources/filters/methods/bulk_delete)

DELETE/accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/filters

#### DDoS ProtectionAdvanced TCP ProtectionTCP Flow ProtectionFiltersItems

##### [Get TCP Flow Protection filter.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/tcp_flow_protection/subresources/filters/subresources/items/methods/get)

GET/accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/filters/{filter_id}

##### [Update TCP Flow Protection filter.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/tcp_flow_protection/subresources/filters/subresources/items/methods/edit)

PATCH/accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/filters/{filter_id}

##### [Delete TCP Flow Protection filter.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/tcp_flow_protection/subresources/filters/subresources/items/methods/delete)

DELETE/accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/filters/{filter_id}

#### DDoS ProtectionAdvanced TCP ProtectionTCP Flow ProtectionRules

##### [List all TCP Flow Protection rules.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/tcp_flow_protection/subresources/rules/methods/list)

GET/accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/rules

##### [Create TCP Flow Protection rule.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/tcp_flow_protection/subresources/rules/methods/create)

POST/accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/rules

##### [Delete all TCP Flow Protection rules.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/tcp_flow_protection/subresources/rules/methods/bulk_delete)

DELETE/accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/rules

#### DDoS ProtectionAdvanced TCP ProtectionTCP Flow ProtectionRulesItems

##### [Get TCP Flow Protection rule.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/tcp_flow_protection/subresources/rules/subresources/items/methods/get)

GET/accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/rules/{rule_id}

##### [Update TCP Flow Protection rule.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/tcp_flow_protection/subresources/rules/subresources/items/methods/edit)

PATCH/accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/rules/{rule_id}

##### [Delete TCP Flow Protection rule.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/tcp_flow_protection/subresources/rules/subresources/items/methods/delete)

DELETE/accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_flow_protection/rules/{rule_id}

#### DDoS ProtectionAdvanced TCP ProtectionStatus

##### [Get protection status.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/status/methods/get)

GET/accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_protection_status

##### [Update protection status.](https://developers.cloudflare.com/api/resources/ddos_protection/subresources/advanced_tcp_protection/subresources/status/methods/edit)

PATCH/accounts/{account_id}/magic/advanced_tcp_protection/configs/tcp_protection_status

#### Magic Network Monitoring

#### Magic Network MonitoringVPC Flows

#### Magic Network MonitoringVPC FlowsTokens

##### [Generate authentication token for VPC flow logs export.](https://developers.cloudflare.com/api/resources/magic_network_monitoring/subresources/vpc_flows/subresources/tokens/methods/create)

POST/accounts/{account_id}/mnm/vpc-flows/token

#### Magic Network MonitoringConfigs

##### [List account configuration](https://developers.cloudflare.com/api/resources/magic_network_monitoring/subresources/configs/methods/get)

GET/accounts/{account_id}/mnm/config

##### [Create account configuration](https://developers.cloudflare.com/api/resources/magic_network_monitoring/subresources/configs/methods/create)

POST/accounts/{account_id}/mnm/config

##### [Update an entire account configuration](https://developers.cloudflare.com/api/resources/magic_network_monitoring/subresources/configs/methods/update)

PUT/accounts/{account_id}/mnm/config

##### [Update account configuration fields](https://developers.cloudflare.com/api/resources/magic_network_monitoring/subresources/configs/methods/edit)

PATCH/accounts/{account_id}/mnm/config

##### [Delete account configuration](https://developers.cloudflare.com/api/resources/magic_network_monitoring/subresources/configs/methods/delete)

DELETE/accounts/{account_id}/mnm/config

#### Magic Network MonitoringConfigsFull

##### [List rules and account configuration](https://developers.cloudflare.com/api/resources/magic_network_monitoring/subresources/configs/subresources/full/methods/get)

GET/accounts/{account_id}/mnm/config/full

#### Magic Network MonitoringRules

##### [List rules](https://developers.cloudflare.com/api/resources/magic_network_monitoring/subresources/rules/methods/list)

GET/accounts/{account_id}/mnm/rules

##### [Get rule](https://developers.cloudflare.com/api/resources/magic_network_monitoring/subresources/rules/methods/get)

GET/accounts/{account_id}/mnm/rules/{rule_id}

##### [Create rules](https://developers.cloudflare.com/api/resources/magic_network_monitoring/subresources/rules/methods/create)

POST/accounts/{account_id}/mnm/rules

##### [Update rules](https://developers.cloudflare.com/api/resources/magic_network_monitoring/subresources/rules/methods/update)

PUT/accounts/{account_id}/mnm/rules

##### [Update rule](https://developers.cloudflare.com/api/resources/magic_network_monitoring/subresources/rules/methods/edit)

PATCH/accounts/{account_id}/mnm/rules/{rule_id}

##### [Delete rule](https://developers.cloudflare.com/api/resources/magic_network_monitoring/subresources/rules/methods/delete)

DELETE/accounts/{account_id}/mnm/rules/{rule_id}

#### Magic Network MonitoringRulesAdvertisements

##### [Update advertisement for rule](https://developers.cloudflare.com/api/resources/magic_network_monitoring/subresources/rules/subresources/advertisements/methods/edit)

PATCH/accounts/{account_id}/mnm/rules/{rule_id}/advertisement

#### Magic Cloud Networking

#### Magic Cloud NetworkingCatalog Syncs

##### [List Catalog Syncs](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/catalog_syncs/methods/list)

GET/accounts/{account_id}/magic/cloud/catalog-syncs

##### [Read Catalog Sync](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/catalog_syncs/methods/get)

GET/accounts/{account_id}/magic/cloud/catalog-syncs/{sync_id}

##### [Create Catalog Sync](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/catalog_syncs/methods/create)

POST/accounts/{account_id}/magic/cloud/catalog-syncs

##### [Update Catalog Sync](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/catalog_syncs/methods/update)

PUT/accounts/{account_id}/magic/cloud/catalog-syncs/{sync_id}

##### [Patch Catalog Sync](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/catalog_syncs/methods/edit)

PATCH/accounts/{account_id}/magic/cloud/catalog-syncs/{sync_id}

##### [Delete Catalog Sync](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/catalog_syncs/methods/delete)

DELETE/accounts/{account_id}/magic/cloud/catalog-syncs/{sync_id}

##### [Run Catalog Sync](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/catalog_syncs/methods/refresh)

POST/accounts/{account_id}/magic/cloud/catalog-syncs/{sync_id}/refresh

#### Magic Cloud NetworkingCatalog SyncsPrebuilt Policies

##### [List Prebuilt Policies](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/catalog_syncs/subresources/prebuilt_policies/methods/list)

GET/accounts/{account_id}/magic/cloud/catalog-syncs/prebuilt-policies

#### Magic Cloud NetworkingOn Ramps

##### [List On-ramps](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/on_ramps/methods/list)

GET/accounts/{account_id}/magic/cloud/onramps

##### [Read On-ramp](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/on_ramps/methods/get)

GET/accounts/{account_id}/magic/cloud/onramps/{onramp_id}

##### [Create On-ramp](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/on_ramps/methods/create)

POST/accounts/{account_id}/magic/cloud/onramps

##### [Update On-ramp](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/on_ramps/methods/update)

PUT/accounts/{account_id}/magic/cloud/onramps/{onramp_id}

##### [Patch On-ramp](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/on_ramps/methods/edit)

PATCH/accounts/{account_id}/magic/cloud/onramps/{onramp_id}

##### [Delete On-ramp](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/on_ramps/methods/delete)

DELETE/accounts/{account_id}/magic/cloud/onramps/{onramp_id}

##### [Apply On-ramp](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/on_ramps/methods/apply)

POST/accounts/{account_id}/magic/cloud/onramps/{onramp_id}/apply

##### [Export as Terraform](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/on_ramps/methods/export)

POST/accounts/{account_id}/magic/cloud/onramps/{onramp_id}/export

##### [Plan On-ramp](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/on_ramps/methods/plan)

POST/accounts/{account_id}/magic/cloud/onramps/{onramp_id}/plan

#### Magic Cloud NetworkingOn RampsAddress Spaces

##### [Read Magic WAN Address Space](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/on_ramps/subresources/address_spaces/methods/list)

GET/accounts/{account_id}/magic/cloud/onramps/magic_wan_address_space

##### [Update Magic WAN Address Space](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/on_ramps/subresources/address_spaces/methods/update)

PUT/accounts/{account_id}/magic/cloud/onramps/magic_wan_address_space

##### [Patch Magic WAN Address Space](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/on_ramps/subresources/address_spaces/methods/edit)

PATCH/accounts/{account_id}/magic/cloud/onramps/magic_wan_address_space

#### Magic Cloud NetworkingCloud Integrations

##### [List Cloud Integrations](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/cloud_integrations/methods/list)

GET/accounts/{account_id}/magic/cloud/providers

##### [Read Cloud Integration](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/cloud_integrations/methods/get)

GET/accounts/{account_id}/magic/cloud/providers/{provider_id}

##### [Create Cloud Integration](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/cloud_integrations/methods/create)

POST/accounts/{account_id}/magic/cloud/providers

##### [Update Cloud Integration](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/cloud_integrations/methods/update)

PUT/accounts/{account_id}/magic/cloud/providers/{provider_id}

##### [Patch Cloud Integration](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/cloud_integrations/methods/edit)

PATCH/accounts/{account_id}/magic/cloud/providers/{provider_id}

##### [Delete Cloud Integration](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/cloud_integrations/methods/delete)

DELETE/accounts/{account_id}/magic/cloud/providers/{provider_id}

##### [Run Discovery for All Integrations](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/cloud_integrations/methods/discover_all)

POST/accounts/{account_id}/magic/cloud/providers/discover

##### [Run Discovery](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/cloud_integrations/methods/discover)

POST/accounts/{account_id}/magic/cloud/providers/{provider_id}/discover

##### [Get Cloud Integration Setup Config](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/cloud_integrations/methods/initial_setup)

GET/accounts/{account_id}/magic/cloud/providers/{provider_id}/initial_setup

#### Magic Cloud NetworkingResources

##### [List Resources](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/resources/methods/list)

GET/accounts/{account_id}/magic/cloud/resources

##### [Read Resource](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/resources/methods/get)

GET/accounts/{account_id}/magic/cloud/resources/{resource_id}

##### [Export Resources](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/resources/methods/export)

GET/accounts/{account_id}/magic/cloud/resources/export

##### [Preview Rego Query](https://developers.cloudflare.com/api/resources/magic_cloud_networking/subresources/resources/methods/policy_preview)

POST/accounts/{account_id}/magic/cloud/resources/policy-preview

#### Monetization

#### MonetizationRules

##### [List payment rules](https://developers.cloudflare.com/api/resources/monetization/subresources/rules/methods/get)

GET/zones/{zone_id}/monetization/rules

##### [Deploy payment ruleset](https://developers.cloudflare.com/api/resources/monetization/subresources/rules/methods/update)

PUT/zones/{zone_id}/monetization/rules

##### [Delete all payment rules](https://developers.cloudflare.com/api/resources/monetization/subresources/rules/methods/delete)

DELETE/zones/{zone_id}/monetization/rules

##### [Get a payment rule](https://developers.cloudflare.com/api/resources/monetization/subresources/rules/methods/get_rule)

GET/zones/{zone_id}/monetization/rules/{rule_id}

##### [Update a payment rule](https://developers.cloudflare.com/api/resources/monetization/subresources/rules/methods/edit_rule)

PATCH/zones/{zone_id}/monetization/rules/{rule_id}

##### [Delete a payment rule](https://developers.cloudflare.com/api/resources/monetization/subresources/rules/methods/delete_rule)

DELETE/zones/{zone_id}/monetization/rules/{rule_id}

#### Network Interconnects

#### Network InterconnectsCNIs

##### [List existing CNI objects](https://developers.cloudflare.com/api/resources/network_interconnects/subresources/cnis/methods/list)

GET/accounts/{account_id}/cni/cnis

##### [Get information about a CNI object](https://developers.cloudflare.com/api/resources/network_interconnects/subresources/cnis/methods/get)

GET/accounts/{account_id}/cni/cnis/{cni}

##### [Create a new CNI object](https://developers.cloudflare.com/api/resources/network_interconnects/subresources/cnis/methods/create)

POST/accounts/{account_id}/cni/cnis

##### [Modify stored information about a CNI object](https://developers.cloudflare.com/api/resources/network_interconnects/subresources/cnis/methods/update)

PUT/accounts/{account_id}/cni/cnis/{cni}

##### [Delete a specified CNI object](https://developers.cloudflare.com/api/resources/network_interconnects/subresources/cnis/methods/delete)

DELETE/accounts/{account_id}/cni/cnis/{cni}

#### Network InterconnectsInterconnects

##### [List existing interconnects](https://developers.cloudflare.com/api/resources/network_interconnects/subresources/interconnects/methods/list)

GET/accounts/{account_id}/cni/interconnects

##### [Get information about an interconnect object](https://developers.cloudflare.com/api/resources/network_interconnects/subresources/interconnects/methods/get)

GET/accounts/{account_id}/cni/interconnects/{icon}

##### [Create a new interconnect](https://developers.cloudflare.com/api/resources/network_interconnects/subresources/interconnects/methods/create)

POST/accounts/{account_id}/cni/interconnects

##### [Delete an interconnect object](https://developers.cloudflare.com/api/resources/network_interconnects/subresources/interconnects/methods/delete)

DELETE/accounts/{account_id}/cni/interconnects/{icon}

##### [Generate the Letter of Authorization (LOA) for a given interconnect](https://developers.cloudflare.com/api/resources/network_interconnects/subresources/interconnects/methods/loa)

GET/accounts/{account_id}/cni/interconnects/{icon}/loa

##### [Get the current status of an interconnect object](https://developers.cloudflare.com/api/resources/network_interconnects/subresources/interconnects/methods/status)

GET/accounts/{account_id}/cni/interconnects/{icon}/status

#### Network InterconnectsSettings

##### [Get the current settings for the active account](https://developers.cloudflare.com/api/resources/network_interconnects/subresources/settings/methods/get)

GET/accounts/{account_id}/cni/settings

##### [Update the current settings for the active account](https://developers.cloudflare.com/api/resources/network_interconnects/subresources/settings/methods/update)

PUT/accounts/{account_id}/cni/settings

#### Network InterconnectsSlots

##### [Retrieve a list of all slots matching the specified parameters](https://developers.cloudflare.com/api/resources/network_interconnects/subresources/slots/methods/list)

GET/accounts/{account_id}/cni/slots

##### [Get information about the specified slot](https://developers.cloudflare.com/api/resources/network_interconnects/subresources/slots/methods/get)

GET/accounts/{account_id}/cni/slots/{slot}

#### MTLS Certificates

##### [List mTLS certificates](https://developers.cloudflare.com/api/resources/mtls_certificates/methods/list)

GET/accounts/{account_id}/mtls_certificates

##### [Get mTLS certificate](https://developers.cloudflare.com/api/resources/mtls_certificates/methods/get)

GET/accounts/{account_id}/mtls_certificates/{mtls_certificate_id}

##### [Upload mTLS certificate](https://developers.cloudflare.com/api/resources/mtls_certificates/methods/create)

POST/accounts/{account_id}/mtls_certificates

##### [Delete mTLS certificate](https://developers.cloudflare.com/api/resources/mtls_certificates/methods/delete)

DELETE/accounts/{account_id}/mtls_certificates/{mtls_certificate_id}

#### MTLS CertificatesAssociations

##### [List mTLS certificate associations](https://developers.cloudflare.com/api/resources/mtls_certificates/subresources/associations/methods/get)

GET/accounts/{account_id}/mtls_certificates/{mtls_certificate_id}/associations

#### Pages

#### PagesProjects

##### [List Cloudflare Pages projects](https://developers.cloudflare.com/api/resources/pages/subresources/projects/methods/list)

GET/accounts/{account_id}/pages/projects

##### [Get a Cloudflare Pages project](https://developers.cloudflare.com/api/resources/pages/subresources/projects/methods/get)

GET/accounts/{account_id}/pages/projects/{project_name}

##### [Get upload token](https://developers.cloudflare.com/api/resources/pages/subresources/projects/methods/get_upload_token)

GET/accounts/{account_id}/pages/projects/{project_name}/upload-token

##### [Create a Cloudflare Pages project](https://developers.cloudflare.com/api/resources/pages/subresources/projects/methods/create)

POST/accounts/{account_id}/pages/projects

##### [Update a Cloudflare Pages project](https://developers.cloudflare.com/api/resources/pages/subresources/projects/methods/edit)

PATCH/accounts/{account_id}/pages/projects/{project_name}

##### [Delete a Cloudflare Pages project](https://developers.cloudflare.com/api/resources/pages/subresources/projects/methods/delete)

DELETE/accounts/{account_id}/pages/projects/{project_name}

##### [Purge the Pages build cache](https://developers.cloudflare.com/api/resources/pages/subresources/projects/methods/purge_build_cache)

POST/accounts/{account_id}/pages/projects/{project_name}/purge_build_cache

#### PagesProjectsDeployments

##### [List Pages deployments](https://developers.cloudflare.com/api/resources/pages/subresources/projects/subresources/deployments/methods/list)

GET/accounts/{account_id}/pages/projects/{project_name}/deployments

##### [Get a Pages deployment](https://developers.cloudflare.com/api/resources/pages/subresources/projects/subresources/deployments/methods/get)

GET/accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}

##### [Create a Pages deployment](https://developers.cloudflare.com/api/resources/pages/subresources/projects/subresources/deployments/methods/create)

POST/accounts/{account_id}/pages/projects/{project_name}/deployments

##### [Delete a Pages deployment](https://developers.cloudflare.com/api/resources/pages/subresources/projects/subresources/deployments/methods/delete)

DELETE/accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}

##### [Retry a Pages deployment](https://developers.cloudflare.com/api/resources/pages/subresources/projects/subresources/deployments/methods/retry)

POST/accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}/retry

##### [Roll back a Pages deployment](https://developers.cloudflare.com/api/resources/pages/subresources/projects/subresources/deployments/methods/rollback)

POST/accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}/rollback

#### PagesProjectsDeploymentsHistory

#### PagesProjectsDeploymentsHistoryLogs

##### [Get Pages deployment logs](https://developers.cloudflare.com/api/resources/pages/subresources/projects/subresources/deployments/subresources/history/subresources/logs/methods/get)

GET/accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}/history/logs

#### PagesProjectsDeploymentsTails

##### [Create deployment tail](https://developers.cloudflare.com/api/resources/pages/subresources/projects/subresources/deployments/subresources/tails/methods/create)

POST/accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}/tails

##### [Delete deployment tail](https://developers.cloudflare.com/api/resources/pages/subresources/projects/subresources/deployments/subresources/tails/methods/delete)

DELETE/accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}/tails/{tail_id}

#### PagesProjectsDomains

##### [List Pages custom domains](https://developers.cloudflare.com/api/resources/pages/subresources/projects/subresources/domains/methods/list)

GET/accounts/{account_id}/pages/projects/{project_name}/domains

##### [Get a Pages custom domain](https://developers.cloudflare.com/api/resources/pages/subresources/projects/subresources/domains/methods/get)

GET/accounts/{account_id}/pages/projects/{project_name}/domains/{domain_name}

##### [Add a Pages custom domain](https://developers.cloudflare.com/api/resources/pages/subresources/projects/subresources/domains/methods/create)

POST/accounts/{account_id}/pages/projects/{project_name}/domains

##### [Retry custom domain validation](https://developers.cloudflare.com/api/resources/pages/subresources/projects/subresources/domains/methods/edit)

PATCH/accounts/{account_id}/pages/projects/{project_name}/domains/{domain_name}

##### [Delete a Pages custom domain](https://developers.cloudflare.com/api/resources/pages/subresources/projects/subresources/domains/methods/delete)

DELETE/accounts/{account_id}/pages/projects/{project_name}/domains/{domain_name}

#### PagesAssets

##### [Upsert asset hashes](https://developers.cloudflare.com/api/resources/pages/subresources/assets/methods/upsert_hashes)

POST/pages/assets/upsert-hashes

##### [Check missing assets](https://developers.cloudflare.com/api/resources/pages/subresources/assets/methods/check_missing)

POST/pages/assets/check-missing

##### [Upload asset](https://developers.cloudflare.com/api/resources/pages/subresources/assets/methods/upload)

POST/pages/assets/upload

#### Registrar

Registrar API for searching, checking, registering, and managing domains through Cloudflare Registrar.

## Prerequisites

Before using this API, ensure:

  1. **Cloudflare account** — the caller must have a valid Cloudflare account.
  2. **Billing profile** — the account must have a billing profile with a valid, current default payment method (credit card or other accepted method). This cannot be set up via API — the account owner must configure billing at `https://dash.cloudflare.com/{account_id}/billing/payment-info` before calling `POST /registrations`.
  3. **API authentication** — use an API token or API key with the appropriate Registrar permissions for the operations you are calling.



## Terminology: domain extension

Throughout this API, “extension” refers to the domain extension part of a fully qualified domain name — the portion after the registrable label. For example, in `example.co.uk`, the extension is `co.uk` (not just `uk`). This covers both top-level domains like `com` and multi-level extensions like `co.uk`. This is distinct from other uses of the word “extension” (e.g., EPP extensions).

## Supported extensions

This API supports programmatic registration for all extensions supported by the dashboard experience, with the following exceptions:

`giving`, `mom`, `inc`, `lol`, `sh`, `link`, `cc`, `new`

Cloudflare Registrar supports 400+ extensions in the dashboard. Extensions listed above can be registered at `https://dash.cloudflare.com/{account_id}/domains/registrations`.

## Typical workflow

  1. **Search** — call `GET /domain-search?q={keyword}` to discover available domains.
  2. **Check** — call `POST /domain-check` with candidate domains to verify real-time availability and pricing.
  3. **Review the response** — if `registrable: false`, inspect `reason` to understand whether the domain is unavailable, the extension is not supported by this API, the extension is not supported by Cloudflare Registrar at all, or the extension’s registry has frozen new registrations.
  4. **Handle premium domains** — if `tier: premium`, premium registration is not currently supported by this API. Surface the premium pricing to the user, but do not proceed to `POST /registrations` for that domain.
  5. **Observe the registration schema** — call `GET /extensions/:extension_name` to discover the required values for registering this extension.
  6. **Register** — call `POST /registrations` with the chosen domain name for supported non-premium registrations.
  7. **Confirm completion** — if the response is `201 Created`, registration completed within the default timeout and no polling is needed.
  8. **Poll when needed** — if the response is `202 Accepted`, poll `links.self` from the workflow response.
  9. **Stop for user action** — if `state: action_required`, stop polling and surface `context.action` to the user. The workflow will not resolve on its own.
  10. **Continue when blocked** — if `state: blocked`, continue polling and inform the user that a third party, such as the extension registry or losing registrar, is delaying progress.
  11. **Review failures before retrying** — if `state: failed`, review `error.code` and `error.message`, then decide whether user action or a new Check call is needed.



**All successful domain registrations are non-refundable.** Once the registration workflow completes with `state: succeeded`, the charge cannot be reversed. Confirm pricing and domain choice with the user before calling `POST /registrations`.

## Default behavior for mutating operations

By default, mutating operations such as create and update hold the connection for a bounded, server-defined amount of time while the operation completes. In most cases, the response contains a completed workflow status and no polling is required.

  * **Completed within the synchronous wait window:** Returns `201` (create) or `200` (update) with a `workflow_status` where `state: succeeded` and `completed: true`.
  * **Still processing after the synchronous wait window:** Returns `202 Accepted` with a `workflow_status` where `completed: false`. Use the `links.self` URL to poll for completion.



## Non-blocking mode

To receive an immediate `202 Accepted` response without waiting, send the `Prefer: respond-async` request header (RFC 7240). The server will acknowledge it with a `Preference-Applied: respond-async` response header.

## Polling

When the response is `202`, poll the workflow status endpoint indicated by `links.self` in the response body until the workflow reaches a terminal state or requires user action.

##### [Search for available domains](https://developers.cloudflare.com/api/resources/registrar/methods/search)

GET/accounts/{account_id}/registrar/domain-search

##### [Check domain availability](https://developers.cloudflare.com/api/resources/registrar/methods/check)

POST/accounts/{account_id}/registrar/domain-check

##### [Check domain transfer eligibility](https://developers.cloudflare.com/api/resources/registrar/methods/transfer_check)

POST/accounts/{account_id}/registrar/domain-transfer-check

#### RegistrarRegistrations

##### [Create Registration](https://developers.cloudflare.com/api/resources/registrar/subresources/registrations/methods/create)

POST/accounts/{account_id}/registrar/registrations

##### [List Registrations](https://developers.cloudflare.com/api/resources/registrar/subresources/registrations/methods/list)

GET/accounts/{account_id}/registrar/registrations

##### [Get Registration](https://developers.cloudflare.com/api/resources/registrar/subresources/registrations/methods/get)

GET/accounts/{account_id}/registrar/registrations/{domain_name}

##### [Update Registration](https://developers.cloudflare.com/api/resources/registrar/subresources/registrations/methods/edit)

PATCH/accounts/{account_id}/registrar/registrations/{domain_name}

#### RegistrarRegistration Status

##### [Get Registration Status](https://developers.cloudflare.com/api/resources/registrar/subresources/registration_status/methods/get)

GET/accounts/{account_id}/registrar/registrations/{domain_name}/registration-status

#### RegistrarUpdate Status

##### [Get Update Status](https://developers.cloudflare.com/api/resources/registrar/subresources/update_status/methods/get)

GET/accounts/{account_id}/registrar/registrations/{domain_name}/update-status

#### RegistrarExtensions

##### [List extensions](https://developers.cloudflare.com/api/resources/registrar/subresources/extensions/methods/list)

GET/accounts/{account_id}/registrar/extensions

##### [Get extension](https://developers.cloudflare.com/api/resources/registrar/subresources/extensions/methods/get)

GET/accounts/{account_id}/registrar/extensions/{extension}

#### RegistrarTransfer In

##### [Initiate Transfer](https://developers.cloudflare.com/api/resources/registrar/subresources/transfer_in/methods/create)

POST/accounts/{account_id}/registrar/registrations/{domain_name}/transfer-in

#### RegistrarTransfer In Status

##### [Get Transfer Status](https://developers.cloudflare.com/api/resources/registrar/subresources/transfer_in_status/methods/get)

GET/accounts/{account_id}/registrar/registrations/{domain_name}/transfer-in-status

#### Registrar Sandbox

Use the Registrar Sandbox API to test domain search, availability checks, registration, and domain management flows without buying real domains.

**This API is a test environment for the production Registrar API.**

## Prerequisites

Before using this API, make sure you have:

  1. **Cloudflare account** — the caller must have a valid Cloudflare account.
  2. **API authentication** — create an API token with Registrar Sandbox permissions.



## How the Sandbox API differs from the production Registrar API

Because the Sandbox API is intended for testing, it behaves differently from the production Registrar API in a few important ways:

  1. **No billing** — you will not be charged real money for purchasing a domain.
  2. **No real domains** — purchased domains are test records and will not be reachable on the Internet.
  3. **No DNS zones** — purchasing a domain does not create a zone resource.
  4. **No Registration Express Mode** — you must provide full contact data.



Sandbox purchases are still persisted. If you purchase a domain in the sandbox, that domain will not be available for others to purchase in the sandbox.

## Terminology: domain extension

Throughout this API, “extension” refers to the domain extension part of a fully qualified domain name — the portion after the registrable label. For example, in `example.co.uk`, the extension is `co.uk` (not just `uk`). This covers both top-level domains like `com` and multi-level extensions like `co.uk`. This is distinct from other uses of the word “extension” (e.g., EPP extensions).

## Supported extensions

The Sandbox API currently supports programmatic registration for these extensions:

`com`, `net`

The production Registrar API supports 40+ extensions.

Cloudflare Registrar supports 400+ extensions in the dashboard. Extensions not listed above can be registered at `https://dash.cloudflare.com/{account_id}/domains/registrations`.

## Typical workflow

  1. **Search** — call `GET /domain-search?q={keyword}` to discover available domains.
  2. **Check** — call `POST /domain-check` with candidate domains to verify real-time availability and pricing.
  3. **Review the response** — if `registrable: false`, inspect `reason` to understand whether the domain is unavailable, the extension is not supported by this API, the extension is not supported by Cloudflare Registrar at all, or the extension’s registry has frozen new registrations.
  4. **Handle premium domains** — if `tier: premium`, premium registration is not currently supported by this API. The Sandbox API currently supports only `com` and `net`, which do not have premium registrations, but clients should still handle this response for consistency with the production Registrar API. Surface the premium pricing to the user, but do not proceed to `POST /registrations` for that domain.
  5. **Observe the registration schema** — call `GET /extensions/:extension_name` to discover the required values for registering this extension.
  6. **Register** — call `POST /registrations` with the chosen domain name for supported non-premium registrations.
  7. **Confirm completion** — if the response is `201 Created`, registration completed within the default timeout and no polling is needed.
  8. **Poll when needed** — if the response is `202 Accepted`, poll `links.self` from the workflow response.
  9. **Stop for user action** — if `state: action_required`, stop polling and surface `context.action` to the user. The workflow will not resolve on its own.
  10. **Continue when blocked** — if `state: blocked`, continue polling and inform the user that a third party, such as the extension registry or losing registrar, is delaying progress.
  11. **Review failures before retrying** — if `state: failed`, review `error.code` and `error.message`, then decide whether user action or a new Check call is needed.



## Default behavior for mutating operations

By default, mutating operations such as create and update hold the connection for a bounded, server-defined amount of time while the operation completes. In most cases, the response contains a completed workflow status and no polling is required.

  * **Completed within the synchronous wait window:** Returns `201` (create) or `200` (update) with a `workflow_status` where `state: succeeded` and `completed: true`.
  * **Still processing after the synchronous wait window:** Returns `202 Accepted` with a `workflow_status` where `completed: false`. Use the `links.self` URL to poll for completion.



## Non-blocking mode

To receive an immediate `202 Accepted` response without waiting, send the `Prefer: respond-async` request header (RFC 7240). The server will acknowledge it with a `Preference-Applied: respond-async` response header.

## Polling

When the response is `202`, poll the workflow status endpoint indicated by `links.self` in the response body until the workflow reaches a terminal state or requires user action.

##### [Search for available domains](https://developers.cloudflare.com/api/resources/registrar_sandbox/methods/search)

GET/accounts/{account_id}/registrar-sandbox/domain-search

##### [Check domain availability](https://developers.cloudflare.com/api/resources/registrar_sandbox/methods/check)

POST/accounts/{account_id}/registrar-sandbox/domain-check

#### Registrar SandboxRegistrations

##### [Create Registration](https://developers.cloudflare.com/api/resources/registrar_sandbox/subresources/registrations/methods/create)

POST/accounts/{account_id}/registrar-sandbox/registrations

##### [List Registrations](https://developers.cloudflare.com/api/resources/registrar_sandbox/subresources/registrations/methods/list)

GET/accounts/{account_id}/registrar-sandbox/registrations

##### [Get Registration](https://developers.cloudflare.com/api/resources/registrar_sandbox/subresources/registrations/methods/get)

GET/accounts/{account_id}/registrar-sandbox/registrations/{domain_name}

##### [Update Registration](https://developers.cloudflare.com/api/resources/registrar_sandbox/subresources/registrations/methods/edit)

PATCH/accounts/{account_id}/registrar-sandbox/registrations/{domain_name}

#### Registrar SandboxRegistration Status

##### [Get Registration Status](https://developers.cloudflare.com/api/resources/registrar_sandbox/subresources/registration_status/methods/get)

GET/accounts/{account_id}/registrar-sandbox/registrations/{domain_name}/registration-status

#### Registrar SandboxUpdate Status

##### [Get Update Status](https://developers.cloudflare.com/api/resources/registrar_sandbox/subresources/update_status/methods/get)

GET/accounts/{account_id}/registrar-sandbox/registrations/{domain_name}/update-status

#### Registrar SandboxExtensions

##### [List extensions](https://developers.cloudflare.com/api/resources/registrar_sandbox/subresources/extensions/methods/list)

GET/accounts/{account_id}/registrar-sandbox/extensions

##### [Get extension](https://developers.cloudflare.com/api/resources/registrar_sandbox/subresources/extensions/methods/get)

GET/accounts/{account_id}/registrar-sandbox/extensions/{extension}

#### Rules Trace

#### Rules TraceTraces

##### [Request Trace](https://developers.cloudflare.com/api/resources/request_tracers/subresources/traces/methods/create)

POST/accounts/{account_id}/request-tracer/trace

#### Rules Lists

#### Rules ListsLists

##### [Get lists](https://developers.cloudflare.com/api/resources/rules/subresources/lists/methods/list)

GET/accounts/{account_id}/rules/lists

##### [Get a list](https://developers.cloudflare.com/api/resources/rules/subresources/lists/methods/get)

GET/accounts/{account_id}/rules/lists/{list_id}

##### [Create a list](https://developers.cloudflare.com/api/resources/rules/subresources/lists/methods/create)

POST/accounts/{account_id}/rules/lists

##### [Update a list](https://developers.cloudflare.com/api/resources/rules/subresources/lists/methods/update)

PUT/accounts/{account_id}/rules/lists/{list_id}

##### [Delete a list](https://developers.cloudflare.com/api/resources/rules/subresources/lists/methods/delete)

DELETE/accounts/{account_id}/rules/lists/{list_id}

#### Rules ListsListsBulk Operations

##### [Get bulk operation status](https://developers.cloudflare.com/api/resources/rules/subresources/lists/subresources/bulk_operations/methods/get)

GET/accounts/{account_id}/rules/lists/bulk_operations/{operation_id}

#### Rules ListsListsItems

##### [Get list items](https://developers.cloudflare.com/api/resources/rules/subresources/lists/subresources/items/methods/list)

GET/accounts/{account_id}/rules/lists/{list_id}/items

##### [Get a list item](https://developers.cloudflare.com/api/resources/rules/subresources/lists/subresources/items/methods/get)

GET/accounts/{account_id}/rules/lists/{list_id}/items/{item_id}

##### [Create list items](https://developers.cloudflare.com/api/resources/rules/subresources/lists/subresources/items/methods/create)

POST/accounts/{account_id}/rules/lists/{list_id}/items

##### [Update all list items](https://developers.cloudflare.com/api/resources/rules/subresources/lists/subresources/items/methods/update)

PUT/accounts/{account_id}/rules/lists/{list_id}/items

##### [Delete list items](https://developers.cloudflare.com/api/resources/rules/subresources/lists/subresources/items/methods/delete)

DELETE/accounts/{account_id}/rules/lists/{list_id}/items

#### Stream

##### [List videos](https://developers.cloudflare.com/api/resources/stream/methods/list)

GET/accounts/{account_id}/stream

##### [Retrieve video details](https://developers.cloudflare.com/api/resources/stream/methods/get)

GET/accounts/{account_id}/stream/{identifier}

##### [Initiate video uploads using TUS](https://developers.cloudflare.com/api/resources/stream/methods/create)

POST/accounts/{account_id}/stream

##### [Edit video details](https://developers.cloudflare.com/api/resources/stream/methods/edit)

POST/accounts/{account_id}/stream/{identifier}

##### [Delete video](https://developers.cloudflare.com/api/resources/stream/methods/delete)

DELETE/accounts/{account_id}/stream/{identifier}

#### StreamAudio Tracks

##### [List additional audio tracks on a video](https://developers.cloudflare.com/api/resources/stream/subresources/audio_tracks/methods/get)

GET/accounts/{account_id}/stream/{identifier}/audio

##### [Edit additional audio tracks on a video](https://developers.cloudflare.com/api/resources/stream/subresources/audio_tracks/methods/edit)

PATCH/accounts/{account_id}/stream/{identifier}/audio/{audio_identifier}

##### [Delete additional audio tracks on a video](https://developers.cloudflare.com/api/resources/stream/subresources/audio_tracks/methods/delete)

DELETE/accounts/{account_id}/stream/{identifier}/audio/{audio_identifier}

##### [Add audio tracks to a video](https://developers.cloudflare.com/api/resources/stream/subresources/audio_tracks/methods/copy)

POST/accounts/{account_id}/stream/{identifier}/audio/copy

#### StreamVideos

##### [Storage use](https://developers.cloudflare.com/api/resources/stream/subresources/videos/methods/storage_usage)

GET/accounts/{account_id}/stream/storage-usage

#### StreamClip

##### [Clip videos given a start and end time](https://developers.cloudflare.com/api/resources/stream/subresources/clip/methods/create)

POST/accounts/{account_id}/stream/clip

#### StreamCopy

##### [Upload videos from a URL](https://developers.cloudflare.com/api/resources/stream/subresources/copy/methods/create)

POST/accounts/{account_id}/stream/copy

#### StreamDirect Upload

##### [Upload videos via direct upload URLs](https://developers.cloudflare.com/api/resources/stream/subresources/direct_upload/methods/create)

POST/accounts/{account_id}/stream/direct_upload

#### StreamKeys

##### [List signing keys](https://developers.cloudflare.com/api/resources/stream/subresources/keys/methods/get)

GET/accounts/{account_id}/stream/keys

##### [Create signing keys](https://developers.cloudflare.com/api/resources/stream/subresources/keys/methods/create)

POST/accounts/{account_id}/stream/keys

##### [Delete signing keys](https://developers.cloudflare.com/api/resources/stream/subresources/keys/methods/delete)

DELETE/accounts/{account_id}/stream/keys/{identifier}

#### StreamLive Inputs

##### [List live inputs](https://developers.cloudflare.com/api/resources/stream/subresources/live_inputs/methods/list)

GET/accounts/{account_id}/stream/live_inputs

##### [Retrieve a live input](https://developers.cloudflare.com/api/resources/stream/subresources/live_inputs/methods/get)

GET/accounts/{account_id}/stream/live_inputs/{live_input_identifier}

##### [Create a live input](https://developers.cloudflare.com/api/resources/stream/subresources/live_inputs/methods/create)

POST/accounts/{account_id}/stream/live_inputs

##### [Update a live input](https://developers.cloudflare.com/api/resources/stream/subresources/live_inputs/methods/update)

PUT/accounts/{account_id}/stream/live_inputs/{live_input_identifier}

##### [Delete a live input](https://developers.cloudflare.com/api/resources/stream/subresources/live_inputs/methods/delete)

DELETE/accounts/{account_id}/stream/live_inputs/{live_input_identifier}

#### StreamLive InputsOutputs

##### [List all outputs associated with a specified live input](https://developers.cloudflare.com/api/resources/stream/subresources/live_inputs/subresources/outputs/methods/list)

GET/accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs

##### [Create a new output, connected to a live input](https://developers.cloudflare.com/api/resources/stream/subresources/live_inputs/subresources/outputs/methods/create)

POST/accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs

##### [Update an output](https://developers.cloudflare.com/api/resources/stream/subresources/live_inputs/subresources/outputs/methods/update)

PUT/accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs/{output_identifier}

##### [Delete an output](https://developers.cloudflare.com/api/resources/stream/subresources/live_inputs/subresources/outputs/methods/delete)

DELETE/accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs/{output_identifier}

#### StreamWatermarks

##### [List watermark profiles](https://developers.cloudflare.com/api/resources/stream/subresources/watermarks/methods/list)

GET/accounts/{account_id}/stream/watermarks

##### [Watermark profile details](https://developers.cloudflare.com/api/resources/stream/subresources/watermarks/methods/get)

GET/accounts/{account_id}/stream/watermarks/{identifier}

##### [Create watermark profiles via basic upload](https://developers.cloudflare.com/api/resources/stream/subresources/watermarks/methods/create)

POST/accounts/{account_id}/stream/watermarks

##### [Delete watermark profiles](https://developers.cloudflare.com/api/resources/stream/subresources/watermarks/methods/delete)

DELETE/accounts/{account_id}/stream/watermarks/{identifier}

#### StreamWebhooks

##### [View webhook](https://developers.cloudflare.com/api/resources/stream/subresources/webhooks/methods/get)

GET/accounts/{account_id}/stream/webhook

##### [Create VOD webhooks](https://developers.cloudflare.com/api/resources/stream/subresources/webhooks/methods/update)

PUT/accounts/{account_id}/stream/webhook

##### [Delete webhooks](https://developers.cloudflare.com/api/resources/stream/subresources/webhooks/methods/delete)

DELETE/accounts/{account_id}/stream/webhook

#### StreamCaptions

##### [List captions or subtitles](https://developers.cloudflare.com/api/resources/stream/subresources/captions/methods/get)

GET/accounts/{account_id}/stream/{identifier}/captions

#### StreamCaptionsLanguage

##### [List captions or subtitles for a provided language](https://developers.cloudflare.com/api/resources/stream/subresources/captions/subresources/language/methods/get)

GET/accounts/{account_id}/stream/{identifier}/captions/{language}

##### [Generate captions or subtitles for a provided language via AI](https://developers.cloudflare.com/api/resources/stream/subresources/captions/subresources/language/methods/create)

POST/accounts/{account_id}/stream/{identifier}/captions/{language}/generate

##### [Upload captions or subtitles](https://developers.cloudflare.com/api/resources/stream/subresources/captions/subresources/language/methods/update)

PUT/accounts/{account_id}/stream/{identifier}/captions/{language}

##### [Delete captions or subtitles](https://developers.cloudflare.com/api/resources/stream/subresources/captions/subresources/language/methods/delete)

DELETE/accounts/{account_id}/stream/{identifier}/captions/{language}

#### StreamCaptionsLanguageVtt

##### [Return WebVTT captions for a provided language](https://developers.cloudflare.com/api/resources/stream/subresources/captions/subresources/language/subresources/vtt/methods/get)

GET/accounts/{account_id}/stream/{identifier}/captions/{language}/vtt

#### StreamDownloads

##### [List downloads](https://developers.cloudflare.com/api/resources/stream/subresources/downloads/methods/get)

GET/accounts/{account_id}/stream/{identifier}/downloads

##### [Create downloads](https://developers.cloudflare.com/api/resources/stream/subresources/downloads/methods/create)

POST/accounts/{account_id}/stream/{identifier}/downloads

##### [Delete downloads](https://developers.cloudflare.com/api/resources/stream/subresources/downloads/methods/delete)

DELETE/accounts/{account_id}/stream/{identifier}/downloads

#### StreamEmbed

##### [Deprecated: Retrieve legacy embed code HTML](https://developers.cloudflare.com/api/resources/stream/subresources/embed/methods/get)

GET/accounts/{account_id}/stream/{identifier}/embed

#### StreamToken

##### [Create signed URL tokens for videos](https://developers.cloudflare.com/api/resources/stream/subresources/token/methods/create)

POST/accounts/{account_id}/stream/{identifier}/token

#### Alerting

#### AlertingAvailable Alerts

##### [Get Alert Types](https://developers.cloudflare.com/api/resources/alerting/subresources/available_alerts/methods/list)

GET/accounts/{account_id}/alerting/v3/available_alerts

#### AlertingDestinations

#### AlertingDestinationsEligible

##### [Get delivery mechanism eligibility](https://developers.cloudflare.com/api/resources/alerting/subresources/destinations/subresources/eligible/methods/get)

GET/accounts/{account_id}/alerting/v3/destinations/eligible

#### AlertingDestinationsPagerduty

##### [List PagerDuty services](https://developers.cloudflare.com/api/resources/alerting/subresources/destinations/subresources/pagerduty/methods/get)

GET/accounts/{account_id}/alerting/v3/destinations/pagerduty

##### [Create PagerDuty integration token](https://developers.cloudflare.com/api/resources/alerting/subresources/destinations/subresources/pagerduty/methods/create)

POST/accounts/{account_id}/alerting/v3/destinations/pagerduty/connect

##### [Delete PagerDuty Services](https://developers.cloudflare.com/api/resources/alerting/subresources/destinations/subresources/pagerduty/methods/delete)

DELETE/accounts/{account_id}/alerting/v3/destinations/pagerduty

##### [Connect PagerDuty](https://developers.cloudflare.com/api/resources/alerting/subresources/destinations/subresources/pagerduty/methods/link)

GET/accounts/{account_id}/alerting/v3/destinations/pagerduty/connect/{token_id}

#### AlertingDestinationsWebhooks

##### [List webhooks](https://developers.cloudflare.com/api/resources/alerting/subresources/destinations/subresources/webhooks/methods/list)

GET/accounts/{account_id}/alerting/v3/destinations/webhooks

##### [Get a webhook](https://developers.cloudflare.com/api/resources/alerting/subresources/destinations/subresources/webhooks/methods/get)

GET/accounts/{account_id}/alerting/v3/destinations/webhooks/{webhook_id}

##### [Create a webhook](https://developers.cloudflare.com/api/resources/alerting/subresources/destinations/subresources/webhooks/methods/create)

POST/accounts/{account_id}/alerting/v3/destinations/webhooks

##### [Update a webhook](https://developers.cloudflare.com/api/resources/alerting/subresources/destinations/subresources/webhooks/methods/update)

PUT/accounts/{account_id}/alerting/v3/destinations/webhooks/{webhook_id}

##### [Delete a webhook](https://developers.cloudflare.com/api/resources/alerting/subresources/destinations/subresources/webhooks/methods/delete)

DELETE/accounts/{account_id}/alerting/v3/destinations/webhooks/{webhook_id}

#### AlertingHistory

##### [List History](https://developers.cloudflare.com/api/resources/alerting/subresources/history/methods/list)

GET/accounts/{account_id}/alerting/v3/history

#### AlertingPolicies

##### [List Notification policies](https://developers.cloudflare.com/api/resources/alerting/subresources/policies/methods/list)

GET/accounts/{account_id}/alerting/v3/policies

##### [Get a Notification policy](https://developers.cloudflare.com/api/resources/alerting/subresources/policies/methods/get)

GET/accounts/{account_id}/alerting/v3/policies/{policy_id}

##### [Create a Notification policy](https://developers.cloudflare.com/api/resources/alerting/subresources/policies/methods/create)

POST/accounts/{account_id}/alerting/v3/policies

##### [Update a Notification policy](https://developers.cloudflare.com/api/resources/alerting/subresources/policies/methods/update)

PUT/accounts/{account_id}/alerting/v3/policies/{policy_id}

##### [Delete a Notification policy](https://developers.cloudflare.com/api/resources/alerting/subresources/policies/methods/delete)

DELETE/accounts/{account_id}/alerting/v3/policies/{policy_id}

#### AlertingSilences

##### [List Silences](https://developers.cloudflare.com/api/resources/alerting/subresources/silences/methods/list)

GET/accounts/{account_id}/alerting/v3/silences

##### [Get Silence](https://developers.cloudflare.com/api/resources/alerting/subresources/silences/methods/get)

GET/accounts/{account_id}/alerting/v3/silences/{silence_id}

##### [Create Silences](https://developers.cloudflare.com/api/resources/alerting/subresources/silences/methods/create)

POST/accounts/{account_id}/alerting/v3/silences

##### [Update Silences](https://developers.cloudflare.com/api/resources/alerting/subresources/silences/methods/update)

PUT/accounts/{account_id}/alerting/v3/silences

##### [Delete Silence](https://developers.cloudflare.com/api/resources/alerting/subresources/silences/methods/delete)

DELETE/accounts/{account_id}/alerting/v3/silences/{silence_id}

#### D1

#### D1Database

##### [List D1 Databases](https://developers.cloudflare.com/api/resources/d1/subresources/database/methods/list)

GET/accounts/{account_id}/d1/database

##### [Get D1 Database](https://developers.cloudflare.com/api/resources/d1/subresources/database/methods/get)

GET/accounts/{account_id}/d1/database/{database_id}

##### [Create D1 Database](https://developers.cloudflare.com/api/resources/d1/subresources/database/methods/create)

POST/accounts/{account_id}/d1/database

##### [Update D1 Database](https://developers.cloudflare.com/api/resources/d1/subresources/database/methods/update)

PUT/accounts/{account_id}/d1/database/{database_id}

##### [Update D1 Database partially](https://developers.cloudflare.com/api/resources/d1/subresources/database/methods/edit)

PATCH/accounts/{account_id}/d1/database/{database_id}

##### [Delete D1 Database](https://developers.cloudflare.com/api/resources/d1/subresources/database/methods/delete)

DELETE/accounts/{account_id}/d1/database/{database_id}

##### [Query D1 Database](https://developers.cloudflare.com/api/resources/d1/subresources/database/methods/query)

POST/accounts/{account_id}/d1/database/{database_id}/query

##### [Raw D1 Database query](https://developers.cloudflare.com/api/resources/d1/subresources/database/methods/raw)

POST/accounts/{account_id}/d1/database/{database_id}/raw

##### [Export D1 Database as SQL](https://developers.cloudflare.com/api/resources/d1/subresources/database/methods/export)

POST/accounts/{account_id}/d1/database/{database_id}/export

##### [Import SQL into your D1 Database](https://developers.cloudflare.com/api/resources/d1/subresources/database/methods/import)

POST/accounts/{account_id}/d1/database/{database_id}/import

#### D1DatabaseTime Travel

##### [Get D1 database bookmark](https://developers.cloudflare.com/api/resources/d1/subresources/database/subresources/time_travel/methods/get_bookmark)

GET/accounts/{account_id}/d1/database/{database_id}/time_travel/bookmark

##### [Restore D1 Database to a bookmark or point in time](https://developers.cloudflare.com/api/resources/d1/subresources/database/subresources/time_travel/methods/restore)

POST/accounts/{account_id}/d1/database/{database_id}/time_travel/restore

#### R2

#### R2Buckets

##### [List Buckets](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/methods/list)

GET/accounts/{account_id}/r2/buckets

##### [Get Bucket](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/methods/get)

GET/accounts/{account_id}/r2/buckets/{bucket_name}

##### [Create Bucket](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/methods/create)

POST/accounts/{account_id}/r2/buckets

##### [Patch Bucket](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/methods/edit)

PATCH/accounts/{account_id}/r2/buckets/{bucket_name}

##### [Delete Bucket](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/methods/delete)

DELETE/accounts/{account_id}/r2/buckets/{bucket_name}

#### R2BucketsLifecycle

##### [Get Object Lifecycle Rules](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/subresources/lifecycle/methods/get)

GET/accounts/{account_id}/r2/buckets/{bucket_name}/lifecycle

##### [Set Object Lifecycle Rules](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/subresources/lifecycle/methods/update)

PUT/accounts/{account_id}/r2/buckets/{bucket_name}/lifecycle

#### R2BucketsCORS

##### [Get Bucket CORS Policy](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/subresources/cors/methods/get)

GET/accounts/{account_id}/r2/buckets/{bucket_name}/cors

##### [Set Bucket CORS Policy](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/subresources/cors/methods/update)

PUT/accounts/{account_id}/r2/buckets/{bucket_name}/cors

##### [Delete Bucket CORS Policy](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/subresources/cors/methods/delete)

DELETE/accounts/{account_id}/r2/buckets/{bucket_name}/cors

#### R2BucketsDomains

#### R2BucketsDomainsCustom

##### [List Custom Domains of Bucket](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/subresources/domains/subresources/custom/methods/list)

GET/accounts/{account_id}/r2/buckets/{bucket_name}/domains/custom

##### [Get Custom Domain Settings](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/subresources/domains/subresources/custom/methods/get)

GET/accounts/{account_id}/r2/buckets/{bucket_name}/domains/custom/{domain}

##### [Attach Custom Domain To Bucket](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/subresources/domains/subresources/custom/methods/create)

POST/accounts/{account_id}/r2/buckets/{bucket_name}/domains/custom

##### [Configure Custom Domain Settings](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/subresources/domains/subresources/custom/methods/update)

PUT/accounts/{account_id}/r2/buckets/{bucket_name}/domains/custom/{domain}

##### [Remove Custom Domain From Bucket](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/subresources/domains/subresources/custom/methods/delete)

DELETE/accounts/{account_id}/r2/buckets/{bucket_name}/domains/custom/{domain}

#### R2BucketsDomainsManaged

##### [Get r2.dev Domain of Bucket](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/subresources/domains/subresources/managed/methods/list)

GET/accounts/{account_id}/r2/buckets/{bucket_name}/domains/managed

##### [Update r2.dev Domain of Bucket](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/subresources/domains/subresources/managed/methods/update)

PUT/accounts/{account_id}/r2/buckets/{bucket_name}/domains/managed

#### R2BucketsEvent Notifications

##### [List Event Notification Rules](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/subresources/event_notifications/methods/list)

GET/accounts/{account_id}/event_notifications/r2/{bucket_name}/configuration

##### [Get Event Notification Rules for a Queue](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/subresources/event_notifications/methods/get)

GET/accounts/{account_id}/event_notifications/r2/{bucket_name}/configuration/queues/{queue_id}

##### [Create Event Notification Rules](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/subresources/event_notifications/methods/update)

PUT/accounts/{account_id}/event_notifications/r2/{bucket_name}/configuration/queues/{queue_id}

##### [Delete Event Notification Rules](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/subresources/event_notifications/methods/delete)

DELETE/accounts/{account_id}/event_notifications/r2/{bucket_name}/configuration/queues/{queue_id}

#### R2BucketsLocks

##### [Get Bucket Lock Rules](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/subresources/locks/methods/get)

GET/accounts/{account_id}/r2/buckets/{bucket_name}/lock

##### [Set Bucket Lock Rules](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/subresources/locks/methods/update)

PUT/accounts/{account_id}/r2/buckets/{bucket_name}/lock

#### R2BucketsMetrics

##### [Get Account-Level Metrics](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/subresources/metrics/methods/list)

GET/accounts/{account_id}/r2/metrics

#### R2BucketsSippy

##### [Get Sippy Configuration](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/subresources/sippy/methods/get)

GET/accounts/{account_id}/r2/buckets/{bucket_name}/sippy

##### [Enable Sippy](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/subresources/sippy/methods/update)

PUT/accounts/{account_id}/r2/buckets/{bucket_name}/sippy

##### [Disable Sippy](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/subresources/sippy/methods/delete)

DELETE/accounts/{account_id}/r2/buckets/{bucket_name}/sippy

#### R2BucketsObjects

##### [List Objects](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/subresources/objects/methods/list)

GET/accounts/{account_id}/r2/buckets/{bucket_name}/objects

##### [Get Object](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/subresources/objects/methods/get)

GET/accounts/{account_id}/r2/buckets/{bucket_name}/objects/{object_key}

##### [Upload Object](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/subresources/objects/methods/upload)

PUT/accounts/{account_id}/r2/buckets/{bucket_name}/objects/{object_key}

##### [Delete Object](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/subresources/objects/methods/delete)

DELETE/accounts/{account_id}/r2/buckets/{bucket_name}/objects/{object_key}

#### R2Temporary Credentials

##### [Create Temporary Access Credentials](https://developers.cloudflare.com/api/resources/r2/subresources/temporary_credentials/methods/create)

POST/accounts/{account_id}/r2/temp-access-credentials

#### R2Super Slurper

#### R2Super SlurperJobs

##### [List jobs](https://developers.cloudflare.com/api/resources/r2/subresources/super_slurper/subresources/jobs/methods/list)

GET/accounts/{account_id}/slurper/jobs

##### [Get job details](https://developers.cloudflare.com/api/resources/r2/subresources/super_slurper/subresources/jobs/methods/get)

GET/accounts/{account_id}/slurper/jobs/{job_id}

##### [Create a job](https://developers.cloudflare.com/api/resources/r2/subresources/super_slurper/subresources/jobs/methods/create)

POST/accounts/{account_id}/slurper/jobs

##### [Abort all jobs](https://developers.cloudflare.com/api/resources/r2/subresources/super_slurper/subresources/jobs/methods/abort_all)

PUT/accounts/{account_id}/slurper/jobs/abortAll

##### [Abort a job](https://developers.cloudflare.com/api/resources/r2/subresources/super_slurper/subresources/jobs/methods/abort)

PUT/accounts/{account_id}/slurper/jobs/{job_id}/abort

##### [Pause a job](https://developers.cloudflare.com/api/resources/r2/subresources/super_slurper/subresources/jobs/methods/pause)

PUT/accounts/{account_id}/slurper/jobs/{job_id}/pause

##### [Get job progress](https://developers.cloudflare.com/api/resources/r2/subresources/super_slurper/subresources/jobs/methods/progress)

GET/accounts/{account_id}/slurper/jobs/{job_id}/progress

##### [Resume a job](https://developers.cloudflare.com/api/resources/r2/subresources/super_slurper/subresources/jobs/methods/resume)

PUT/accounts/{account_id}/slurper/jobs/{job_id}/resume

#### R2Super SlurperJobsLogs

##### [Get job logs](https://developers.cloudflare.com/api/resources/r2/subresources/super_slurper/subresources/jobs/subresources/logs/methods/list)

GET/accounts/{account_id}/slurper/jobs/{job_id}/logs

#### R2Super SlurperConnectivity Precheck

##### [Check source connectivity](https://developers.cloudflare.com/api/resources/r2/subresources/super_slurper/subresources/connectivity_precheck/methods/source)

PUT/accounts/{account_id}/slurper/source/connectivity-precheck

##### [Check target connectivity](https://developers.cloudflare.com/api/resources/r2/subresources/super_slurper/subresources/connectivity_precheck/methods/target)

PUT/accounts/{account_id}/slurper/target/connectivity-precheck

#### R2 Data Catalog

##### [List R2 catalogs](https://developers.cloudflare.com/api/resources/r2_data_catalog/methods/list)

Deprecated

GET/accounts/{account_id}/r2-catalog

##### [Get R2 catalog details](https://developers.cloudflare.com/api/resources/r2_data_catalog/methods/get)

Deprecated

GET/accounts/{account_id}/r2-catalog/{bucket_name}

##### [Enable R2 bucket as a catalog](https://developers.cloudflare.com/api/resources/r2_data_catalog/methods/enable)

Deprecated

POST/accounts/{account_id}/r2-catalog/{bucket_name}/enable

##### [Disable R2 catalog](https://developers.cloudflare.com/api/resources/r2_data_catalog/methods/disable)

Deprecated

POST/accounts/{account_id}/r2-catalog/{bucket_name}/disable

##### [Delete R2 catalog metadata](https://developers.cloudflare.com/api/resources/r2_data_catalog/methods/delete)

Deprecated

POST/accounts/{account_id}/r2-catalog/{bucket_name}/delete

#### R2 Data CatalogMaintenance Configs

##### [Get catalog maintenance configuration](https://developers.cloudflare.com/api/resources/r2_data_catalog/subresources/maintenance_configs/methods/get)

Deprecated

GET/accounts/{account_id}/r2-catalog/{bucket_name}/maintenance-configs

##### [Update catalog maintenance configuration](https://developers.cloudflare.com/api/resources/r2_data_catalog/subresources/maintenance_configs/methods/update)

Deprecated

POST/accounts/{account_id}/r2-catalog/{bucket_name}/maintenance-configs

#### R2 Data CatalogCredentials

##### [Store catalog credentials](https://developers.cloudflare.com/api/resources/r2_data_catalog/subresources/credentials/methods/create)

Deprecated

POST/accounts/{account_id}/r2-catalog/{bucket_name}/credential

#### R2 Data CatalogNamespaces

##### [List namespaces in catalog](https://developers.cloudflare.com/api/resources/r2_data_catalog/subresources/namespaces/methods/list)

Deprecated

GET/accounts/{account_id}/r2-catalog/{bucket_name}/namespaces

#### R2 Data CatalogNamespacesTables

##### [List tables in namespace](https://developers.cloudflare.com/api/resources/r2_data_catalog/subresources/namespaces/subresources/tables/methods/list)

Deprecated

GET/accounts/{account_id}/r2-catalog/{bucket_name}/namespaces/{namespace}/tables

#### R2 Data CatalogNamespacesTablesMaintenance Configs

##### [Get table maintenance configuration](https://developers.cloudflare.com/api/resources/r2_data_catalog/subresources/namespaces/subresources/tables/subresources/maintenance_configs/methods/get)

Deprecated

GET/accounts/{account_id}/r2-catalog/{bucket_name}/namespaces/{namespace}/tables/{table_name}/maintenance-configs

##### [Update table maintenance configuration](https://developers.cloudflare.com/api/resources/r2_data_catalog/subresources/namespaces/subresources/tables/subresources/maintenance_configs/methods/update)

Deprecated

POST/accounts/{account_id}/r2-catalog/{bucket_name}/namespaces/{namespace}/tables/{table_name}/maintenance-configs

#### Basin Catalog

##### [List Basin Catalogs](https://developers.cloudflare.com/api/resources/basin_catalog/methods/list)

GET/accounts/{account_id}/basin-catalog

##### [Get Basin Catalog details](https://developers.cloudflare.com/api/resources/basin_catalog/methods/get)

GET/accounts/{account_id}/basin-catalog/{bucket_name}

##### [Enable R2 bucket as a catalog](https://developers.cloudflare.com/api/resources/basin_catalog/methods/enable)

POST/accounts/{account_id}/basin-catalog/{bucket_name}/enable

##### [Disable Basin Catalog](https://developers.cloudflare.com/api/resources/basin_catalog/methods/disable)

POST/accounts/{account_id}/basin-catalog/{bucket_name}/disable

##### [Delete Basin Catalog metadata](https://developers.cloudflare.com/api/resources/basin_catalog/methods/delete)

POST/accounts/{account_id}/basin-catalog/{bucket_name}/delete

#### Basin CatalogMaintenance Configs

##### [Get catalog maintenance configuration](https://developers.cloudflare.com/api/resources/basin_catalog/subresources/maintenance_configs/methods/get)

GET/accounts/{account_id}/basin-catalog/{bucket_name}/maintenance-configs

##### [Update catalog maintenance configuration](https://developers.cloudflare.com/api/resources/basin_catalog/subresources/maintenance_configs/methods/update)

POST/accounts/{account_id}/basin-catalog/{bucket_name}/maintenance-configs

#### Basin CatalogCredentials

##### [Store catalog credentials](https://developers.cloudflare.com/api/resources/basin_catalog/subresources/credentials/methods/create)

POST/accounts/{account_id}/basin-catalog/{bucket_name}/credential

#### Basin CatalogNamespaces

##### [List namespaces in catalog](https://developers.cloudflare.com/api/resources/basin_catalog/subresources/namespaces/methods/list)

GET/accounts/{account_id}/basin-catalog/{bucket_name}/namespaces

#### Basin CatalogNamespacesTables

##### [List tables in namespace](https://developers.cloudflare.com/api/resources/basin_catalog/subresources/namespaces/subresources/tables/methods/list)

GET/accounts/{account_id}/basin-catalog/{bucket_name}/namespaces/{namespace}/tables

#### Basin CatalogNamespacesTablesMaintenance Configs

##### [Get table maintenance configuration](https://developers.cloudflare.com/api/resources/basin_catalog/subresources/namespaces/subresources/tables/subresources/maintenance_configs/methods/get)

GET/accounts/{account_id}/basin-catalog/{bucket_name}/namespaces/{namespace}/tables/{table_name}/maintenance-configs

##### [Update table maintenance configuration](https://developers.cloudflare.com/api/resources/basin_catalog/subresources/namespaces/subresources/tables/subresources/maintenance_configs/methods/update)

POST/accounts/{account_id}/basin-catalog/{bucket_name}/namespaces/{namespace}/tables/{table_name}/maintenance-configs

#### Workers For Platforms

#### Workers For PlatformsDispatch

#### Workers For PlatformsDispatchNamespaces

##### [List Workers for Platforms Dispatch Namespaces](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/methods/list)

GET/accounts/{account_id}/workers/dispatch/namespaces

##### [Get Workers for Platforms Dispatch Namespace](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/methods/get)

GET/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}

##### [Create Workers for Platforms Dispatch Namespace](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/methods/create)

POST/accounts/{account_id}/workers/dispatch/namespaces

##### [Delete Workers for Platforms Dispatch Namespace](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/methods/delete)

DELETE/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}

#### Workers For PlatformsDispatchNamespacesScripts

##### [Get Workers for Platforms Script details](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/methods/get)

GET/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}

##### [Upload Workers for Platforms Script Module](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/methods/update)

PUT/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}

##### [Delete Workers for Platforms Script](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/methods/delete)

DELETE/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}

#### Workers For PlatformsDispatchNamespacesScriptsAsset Upload

##### [Create Workers for Platforms Assets Upload Session](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/subresources/asset_upload/methods/create)

POST/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/assets-upload-session

#### Workers For PlatformsDispatchNamespacesScriptsContent

##### [Get Workers for Platforms Script Content](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/subresources/content/methods/get)

GET/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/content

##### [Replace Workers for Platforms Script Content](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/subresources/content/methods/update)

PUT/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/content

#### Workers For PlatformsDispatchNamespacesScriptsSettings

##### [Get Workers for Platforms Script Settings](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/subresources/settings/methods/get)

GET/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/settings

##### [Patch Workers for Platforms Script Settings](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/subresources/settings/methods/edit)

PATCH/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/settings

#### Workers For PlatformsDispatchNamespacesScriptsBindings

##### [Get Workers for Platforms Script Bindings](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/subresources/bindings/methods/get)

GET/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/bindings

#### Workers For PlatformsDispatchNamespacesScriptsSecrets

##### [List Workers for Platforms Script Secrets](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/subresources/secrets/methods/list)

GET/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/secrets

##### [Get Workers for Platforms Script Secret](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/subresources/secrets/methods/get)

GET/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/secrets/{secret_name}

##### [Add a secret to a Workers for Platforms script](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/subresources/secrets/methods/update)

PUT/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/secrets

##### [Delete Workers for Platforms script secret](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/subresources/secrets/methods/delete)

DELETE/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/secrets/{secret_name}

##### [Patch multiple Workers for Platforms script secrets](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/subresources/secrets/methods/bulk_update)

PATCH/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/secrets-bulk

#### Workers For PlatformsDispatchNamespacesScriptsTags

##### [List Workers for Platforms Script Tags](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/subresources/tags/methods/list)

GET/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/tags

##### [Replace Workers for Platforms Script Tags](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/subresources/tags/methods/update)

PUT/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/tags

##### [Delete Workers for Platforms Script Tag](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/subresources/tags/methods/delete)

DELETE/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/tags/{tag}

#### Zero Trust

#### Zero TrustDevices

##### [List devices (deprecated)](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/methods/list)

Deprecated

GET/accounts/{account_id}/devices

##### [Get device (deprecated)](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/methods/get)

Deprecated

GET/accounts/{account_id}/devices/{device_id}

#### Zero TrustDevicesDevices

##### [List devices](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/devices/methods/list)

GET/accounts/{account_id}/devices/physical-devices

##### [Get device](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/devices/methods/get)

GET/accounts/{account_id}/devices/physical-devices/{device_id}

##### [Delete device](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/devices/methods/delete)

DELETE/accounts/{account_id}/devices/physical-devices/{device_id}

##### [Revoke device registrations](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/devices/methods/revoke)

Deprecated

POST/accounts/{account_id}/devices/physical-devices/{device_id}/revoke

#### Zero TrustDevicesResilience

#### Zero TrustDevicesResilienceGlobal WARP Override

##### [Get Global Disconnect](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/resilience/subresources/global_warp_override/methods/get)

GET/accounts/{account_id}/devices/resilience/disconnect

##### [Set Global Disconnect](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/resilience/subresources/global_warp_override/methods/create)

POST/accounts/{account_id}/devices/resilience/disconnect

#### Zero TrustDevicesRegistrations

##### [List registrations](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/registrations/methods/list)

GET/accounts/{account_id}/devices/registrations

##### [Get registration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/registrations/methods/get)

GET/accounts/{account_id}/devices/registrations/{registration_id}

##### [Delete registration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/registrations/methods/delete)

DELETE/accounts/{account_id}/devices/registrations/{registration_id}

##### [Delete registrations](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/registrations/methods/bulk_delete)

DELETE/accounts/{account_id}/devices/registrations

##### [Revoke registrations](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/registrations/methods/revoke)

Deprecated

POST/accounts/{account_id}/devices/registrations/revoke

##### [Unrevoke registrations](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/registrations/methods/unrevoke)

Deprecated

POST/accounts/{account_id}/devices/registrations/unrevoke

#### Zero TrustDevicesDEX Tests

##### [List Device DEX tests](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/dex_tests/methods/list)

GET/accounts/{account_id}/dex/devices/dex_tests

##### [Get Device DEX test](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/dex_tests/methods/get)

GET/accounts/{account_id}/dex/devices/dex_tests/{dex_test_id}

##### [Create Device DEX test](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/dex_tests/methods/create)

POST/accounts/{account_id}/dex/devices/dex_tests

##### [Update Device DEX test](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/dex_tests/methods/update)

PUT/accounts/{account_id}/dex/devices/dex_tests/{dex_test_id}

##### [Delete Device DEX test](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/dex_tests/methods/delete)

DELETE/accounts/{account_id}/dex/devices/dex_tests/{dex_test_id}

#### Zero TrustDevicesIP Profiles

##### [List IP profiles](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/ip_profiles/methods/list)

GET/accounts/{account_id}/devices/ip-profiles

##### [Get IP profile](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/ip_profiles/methods/get)

GET/accounts/{account_id}/devices/ip-profiles/{profile_id}

##### [Create IP profile](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/ip_profiles/methods/create)

POST/accounts/{account_id}/devices/ip-profiles

##### [Update IP profile](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/ip_profiles/methods/update)

PATCH/accounts/{account_id}/devices/ip-profiles/{profile_id}

##### [Delete IP profile](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/ip_profiles/methods/delete)

DELETE/accounts/{account_id}/devices/ip-profiles/{profile_id}

#### Zero TrustDevicesDeployment Groups

##### [List deployment groups](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/deployment_groups/methods/list)

GET/accounts/{account_id}/devices/deployment-groups

##### [Get deployment group](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/deployment_groups/methods/get)

GET/accounts/{account_id}/devices/deployment-groups/{group_id}

##### [Create deployment group](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/deployment_groups/methods/create)

POST/accounts/{account_id}/devices/deployment-groups

##### [Update deployment group](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/deployment_groups/methods/edit)

PATCH/accounts/{account_id}/devices/deployment-groups/{group_id}

##### [Delete deployment group](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/deployment_groups/methods/delete)

DELETE/accounts/{account_id}/devices/deployment-groups/{group_id}

#### Zero TrustDevicesNetworks

##### [List your device managed networks](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/networks/methods/list)

GET/accounts/{account_id}/devices/networks

##### [Get device managed network details](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/networks/methods/get)

GET/accounts/{account_id}/devices/networks/{network_id}

##### [Create a device managed network](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/networks/methods/create)

POST/accounts/{account_id}/devices/networks

##### [Update a device managed network](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/networks/methods/update)

PUT/accounts/{account_id}/devices/networks/{network_id}

##### [Delete a device managed network](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/networks/methods/delete)

DELETE/accounts/{account_id}/devices/networks/{network_id}

#### Zero TrustDevicesFleet Status

##### [Get the latest status of a device.](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/fleet_status/methods/get)

GET/accounts/{account_id}/dex/devices/{device_id}/fleet-status/live

#### Zero TrustDevicesPolicies

#### Zero TrustDevicesPoliciesDefault

##### [Get the default device settings profile](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/policies/subresources/default/methods/get)

GET/accounts/{account_id}/devices/policy

##### [Update the default device settings profile](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/policies/subresources/default/methods/edit)

PATCH/accounts/{account_id}/devices/policy

#### Zero TrustDevicesPoliciesDefaultExcludes

##### [Get the Split Tunnel exclude list](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/policies/subresources/default/subresources/excludes/methods/get)

GET/accounts/{account_id}/devices/policy/exclude

##### [Set the Split Tunnel exclude list](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/policies/subresources/default/subresources/excludes/methods/update)

PUT/accounts/{account_id}/devices/policy/exclude

#### Zero TrustDevicesPoliciesDefaultIncludes

##### [Get the Split Tunnel include list](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/policies/subresources/default/subresources/includes/methods/get)

GET/accounts/{account_id}/devices/policy/include

##### [Set the Split Tunnel include list](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/policies/subresources/default/subresources/includes/methods/update)

PUT/accounts/{account_id}/devices/policy/include

#### Zero TrustDevicesPoliciesDefaultFallback Domains

##### [Get your Local Domain Fallback list](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/policies/subresources/default/subresources/fallback_domains/methods/get)

GET/accounts/{account_id}/devices/policy/fallback_domains

##### [Set your Local Domain Fallback list](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/policies/subresources/default/subresources/fallback_domains/methods/update)

PUT/accounts/{account_id}/devices/policy/fallback_domains

#### Zero TrustDevicesPoliciesDefaultCertificates

##### [Get device certificate provisioning status](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/policies/subresources/default/subresources/certificates/methods/get)

GET/zones/{zone_id}/devices/policy/certificates

##### [Update device certificate provisioning status](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/policies/subresources/default/subresources/certificates/methods/edit)

PATCH/zones/{zone_id}/devices/policy/certificates

#### Zero TrustDevicesPoliciesCustom

##### [List device settings profiles](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/policies/subresources/custom/methods/list)

GET/accounts/{account_id}/devices/policies

##### [Get device settings profile by ID](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/policies/subresources/custom/methods/get)

GET/accounts/{account_id}/devices/policy/{policy_id}

##### [Create a device settings profile](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/policies/subresources/custom/methods/create)

POST/accounts/{account_id}/devices/policy

##### [Update a device settings profile](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/policies/subresources/custom/methods/edit)

PATCH/accounts/{account_id}/devices/policy/{policy_id}

##### [Delete a device settings profile](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/policies/subresources/custom/methods/delete)

DELETE/accounts/{account_id}/devices/policy/{policy_id}

#### Zero TrustDevicesPoliciesCustomExcludes

##### [Get the Split Tunnel exclude list for a device settings profile](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/policies/subresources/custom/subresources/excludes/methods/get)

GET/accounts/{account_id}/devices/policy/{policy_id}/exclude

##### [Set the Split Tunnel exclude list for a device settings profile](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/policies/subresources/custom/subresources/excludes/methods/update)

PUT/accounts/{account_id}/devices/policy/{policy_id}/exclude

#### Zero TrustDevicesPoliciesCustomIncludes

##### [Get the Split Tunnel include list for a device settings profile](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/policies/subresources/custom/subresources/includes/methods/get)

GET/accounts/{account_id}/devices/policy/{policy_id}/include

##### [Set the Split Tunnel include list for a device settings profile](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/policies/subresources/custom/subresources/includes/methods/update)

PUT/accounts/{account_id}/devices/policy/{policy_id}/include

#### Zero TrustDevicesPoliciesCustomFallback Domains

##### [Get the Local Domain Fallback list for a device settings profile](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/policies/subresources/custom/subresources/fallback_domains/methods/get)

GET/accounts/{account_id}/devices/policy/{policy_id}/fallback_domains

##### [Set the Local Domain Fallback list for a device settings profile](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/policies/subresources/custom/subresources/fallback_domains/methods/update)

PUT/accounts/{account_id}/devices/policy/{policy_id}/fallback_domains

#### Zero TrustDevicesPosture

##### [List posture rules](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/posture/methods/list)

GET/accounts/{account_id}/devices/posture

##### [Get posture rule](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/posture/methods/get)

GET/accounts/{account_id}/devices/posture/{rule_id}

##### [Create posture rule](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/posture/methods/create)

POST/accounts/{account_id}/devices/posture

##### [Update posture rule](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/posture/methods/update)

PUT/accounts/{account_id}/devices/posture/{rule_id}

##### [Delete posture rule](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/posture/methods/delete)

DELETE/accounts/{account_id}/devices/posture/{rule_id}

#### Zero TrustDevicesPostureIntegrations

##### [List posture integrations](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/posture/subresources/integrations/methods/list)

GET/accounts/{account_id}/devices/posture/integration

##### [Get posture integration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/posture/subresources/integrations/methods/get)

GET/accounts/{account_id}/devices/posture/integration/{integration_id}

##### [Create posture integration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/posture/subresources/integrations/methods/create)

POST/accounts/{account_id}/devices/posture/integration

##### [Update posture integration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/posture/subresources/integrations/methods/edit)

PATCH/accounts/{account_id}/devices/posture/integration/{integration_id}

##### [Delete posture integration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/posture/subresources/integrations/methods/delete)

DELETE/accounts/{account_id}/devices/posture/integration/{integration_id}

#### Zero TrustDevicesRevoke

##### [Revoke devices (deprecated)](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/revoke/methods/create)

Deprecated

POST/accounts/{account_id}/devices/revoke

#### Zero TrustDevicesSettings

##### [Get device settings](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/settings/methods/get)

GET/accounts/{account_id}/devices/settings

##### [Update device settings (deprecated)](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/settings/methods/update)

Deprecated

PUT/accounts/{account_id}/devices/settings

##### [Update device settings](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/settings/methods/edit)

PATCH/accounts/{account_id}/devices/settings

##### [Reset device settings](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/settings/methods/delete)

DELETE/accounts/{account_id}/devices/settings

#### Zero TrustDevicesUnrevoke

##### [Unrevoke devices (deprecated)](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/unrevoke/methods/create)

Deprecated

POST/accounts/{account_id}/devices/unrevoke

#### Zero TrustDevicesOverride Codes

##### [Get override codes (deprecated) ](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/override_codes/methods/list)

Deprecated

GET/accounts/{account_id}/devices/{device_id}/override_codes

##### [Get override codes](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/override_codes/methods/get)

GET/accounts/{account_id}/devices/registrations/{registration_id}/override_codes

#### Zero TrustIdentity Providers

##### [List Access identity providers](https://developers.cloudflare.com/api/resources/zero_trust/subresources/identity_providers/methods/list)

GET/{accounts_or_zones}/{account_or_zone_id}/access/identity_providers

##### [Get an Access identity provider](https://developers.cloudflare.com/api/resources/zero_trust/subresources/identity_providers/methods/get)

GET/{accounts_or_zones}/{account_or_zone_id}/access/identity_providers/{identity_provider_id}

##### [Add an Access identity provider](https://developers.cloudflare.com/api/resources/zero_trust/subresources/identity_providers/methods/create)

POST/{accounts_or_zones}/{account_or_zone_id}/access/identity_providers

##### [Update an Access identity provider](https://developers.cloudflare.com/api/resources/zero_trust/subresources/identity_providers/methods/update)

PUT/{accounts_or_zones}/{account_or_zone_id}/access/identity_providers/{identity_provider_id}

##### [Delete an Access identity provider](https://developers.cloudflare.com/api/resources/zero_trust/subresources/identity_providers/methods/delete)

DELETE/{accounts_or_zones}/{account_or_zone_id}/access/identity_providers/{identity_provider_id}

#### Zero TrustIdentity ProvidersSCIM

#### Zero TrustIdentity ProvidersSCIMGroups

##### [List SCIM Group resources](https://developers.cloudflare.com/api/resources/zero_trust/subresources/identity_providers/subresources/scim/subresources/groups/methods/list)

GET/accounts/{account_id}/access/identity_providers/{identity_provider_id}/scim/groups

#### Zero TrustIdentity ProvidersSCIMUsers

##### [List SCIM User resources](https://developers.cloudflare.com/api/resources/zero_trust/subresources/identity_providers/subresources/scim/subresources/users/methods/list)

GET/accounts/{account_id}/access/identity_providers/{identity_provider_id}/scim/users

#### Zero TrustIdentity ProvidersSAML Certificate

##### [Create SAML encryption certificate for Identity Provider](https://developers.cloudflare.com/api/resources/zero_trust/subresources/identity_providers/subresources/saml_certificate/methods/create)

POST/accounts/{account_id}/access/identity_providers/{identity_provider_id}/saml_certificate

#### Zero TrustOrganizations

##### [Get your Zero Trust organization](https://developers.cloudflare.com/api/resources/zero_trust/subresources/organizations/methods/list)

GET/{accounts_or_zones}/{account_or_zone_id}/access/organizations

##### [Create your Zero Trust organization](https://developers.cloudflare.com/api/resources/zero_trust/subresources/organizations/methods/create)

POST/{accounts_or_zones}/{account_or_zone_id}/access/organizations

##### [Update your Zero Trust organization](https://developers.cloudflare.com/api/resources/zero_trust/subresources/organizations/methods/update)

PUT/{accounts_or_zones}/{account_or_zone_id}/access/organizations

##### [Revoke all Access tokens for a user](https://developers.cloudflare.com/api/resources/zero_trust/subresources/organizations/methods/revoke_users)

POST/{accounts_or_zones}/{account_or_zone_id}/access/organizations/revoke_user

#### Zero TrustOrganizationsDOH

##### [Get your Zero Trust organization DoH settings](https://developers.cloudflare.com/api/resources/zero_trust/subresources/organizations/subresources/doh/methods/get)

GET/accounts/{account_id}/access/organizations/doh

##### [Update your Zero Trust organization DoH settings](https://developers.cloudflare.com/api/resources/zero_trust/subresources/organizations/subresources/doh/methods/update)

PUT/accounts/{account_id}/access/organizations/doh

#### Zero TrustSeats

##### [Update a user seat](https://developers.cloudflare.com/api/resources/zero_trust/subresources/seats/methods/edit)

PATCH/accounts/{account_id}/access/seats

#### Zero TrustAccess

#### Zero TrustAccessAI Controls

#### Zero TrustAccessAI ControlsMcp

#### Zero TrustAccessAI ControlsMcpPortals

##### [List MCP Portals](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/ai_controls/subresources/mcp/subresources/portals/methods/list)

GET/accounts/{account_id}/access/ai-controls/mcp/portals

##### [Create a new MCP Portal](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/ai_controls/subresources/mcp/subresources/portals/methods/create)

POST/accounts/{account_id}/access/ai-controls/mcp/portals

##### [Read details of an MCP Portal](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/ai_controls/subresources/mcp/subresources/portals/methods/read)

GET/accounts/{account_id}/access/ai-controls/mcp/portals/{id}

##### [Update an MCP Portal](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/ai_controls/subresources/mcp/subresources/portals/methods/update)

PUT/accounts/{account_id}/access/ai-controls/mcp/portals/{id}

##### [Delete an MCP Portal](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/ai_controls/subresources/mcp/subresources/portals/methods/delete)

DELETE/accounts/{account_id}/access/ai-controls/mcp/portals/{id}

#### Zero TrustAccessAI ControlsMcpServers

##### [List MCP Servers](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/ai_controls/subresources/mcp/subresources/servers/methods/list)

GET/accounts/{account_id}/access/ai-controls/mcp/servers

##### [Create a new MCP Server](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/ai_controls/subresources/mcp/subresources/servers/methods/create)

POST/accounts/{account_id}/access/ai-controls/mcp/servers

##### [Read the details of an MCP Server](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/ai_controls/subresources/mcp/subresources/servers/methods/read)

GET/accounts/{account_id}/access/ai-controls/mcp/servers/{id}

##### [Update an MCP Server](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/ai_controls/subresources/mcp/subresources/servers/methods/update)

PUT/accounts/{account_id}/access/ai-controls/mcp/servers/{id}

##### [Delete an MCP Server](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/ai_controls/subresources/mcp/subresources/servers/methods/delete)

DELETE/accounts/{account_id}/access/ai-controls/mcp/servers/{id}

##### [Sync MCP Server Capabilities](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/ai_controls/subresources/mcp/subresources/servers/methods/sync)

POST/accounts/{account_id}/access/ai-controls/mcp/servers/{id}/sync

#### Zero TrustAccessGateway CA

##### [List SSH Certificate Authorities (CA)](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/gateway_ca/methods/list)

GET/accounts/{account_id}/access/gateway_ca

##### [Add a new SSH Certificate Authority (CA)](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/gateway_ca/methods/create)

POST/accounts/{account_id}/access/gateway_ca

##### [Delete an SSH Certificate Authority (CA)](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/gateway_ca/methods/delete)

DELETE/accounts/{account_id}/access/gateway_ca/{certificate_id}

#### Zero TrustAccessIdP Federation Grants

##### [List IdP federation grants](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/idp_federation_grants/methods/list)

GET/accounts/{account_id}/access/idp_federation_grants

##### [Create an IdP federation grant](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/idp_federation_grants/methods/create)

POST/accounts/{account_id}/access/idp_federation_grants

##### [Get an IdP federation grant](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/idp_federation_grants/methods/get)

GET/accounts/{account_id}/access/idp_federation_grants/{grant_id}

##### [Delete an IdP federation grant](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/idp_federation_grants/methods/delete)

DELETE/accounts/{account_id}/access/idp_federation_grants/{grant_id}

#### Zero TrustAccessSAML Certificates

##### [List SAML certificate sets](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/saml_certificates/methods/list)

GET/accounts/{account_id}/access/saml_certificates

##### [Get SAML certificate set](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/saml_certificates/methods/get)

GET/accounts/{account_id}/access/saml_certificates/{saml_cert_set_id}

##### [Rotate SAML certificate](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/saml_certificates/methods/rotate)

POST/accounts/{account_id}/access/saml_certificates/{saml_cert_set_id}/rotate

##### [Download current certificate in PEM format](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/saml_certificates/methods/get_pem)

GET/accounts/{account_id}/access/saml_certificates/{saml_cert_set_id}/pem

#### Zero TrustAccessInfrastructure

#### Zero TrustAccessInfrastructureTargets

##### [List all targets](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/infrastructure/subresources/targets/methods/list)

GET/accounts/{account_id}/infrastructure/targets

##### [Get target](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/infrastructure/subresources/targets/methods/get)

GET/accounts/{account_id}/infrastructure/targets/{target_id}

##### [Create new target](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/infrastructure/subresources/targets/methods/create)

POST/accounts/{account_id}/infrastructure/targets

##### [Update target](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/infrastructure/subresources/targets/methods/update)

PUT/accounts/{account_id}/infrastructure/targets/{target_id}

##### [Delete target](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/infrastructure/subresources/targets/methods/delete)

DELETE/accounts/{account_id}/infrastructure/targets/{target_id}

##### [Create new targets](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/infrastructure/subresources/targets/methods/bulk_update)

PUT/accounts/{account_id}/infrastructure/targets/batch

##### [Delete targets (Deprecated)](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/infrastructure/subresources/targets/methods/bulk_delete)

Deprecated

DELETE/accounts/{account_id}/infrastructure/targets/batch

##### [Delete targets](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/infrastructure/subresources/targets/methods/bulk_delete_v2)

POST/accounts/{account_id}/infrastructure/targets/batch_delete

#### Zero TrustAccessApplications

##### [List Access applications](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/applications/methods/list)

GET/{accounts_or_zones}/{account_or_zone_id}/access/apps

##### [Get an Access application](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/applications/methods/get)

GET/{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}

##### [Add an Access application](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/applications/methods/create)

POST/{accounts_or_zones}/{account_or_zone_id}/access/apps

##### [Update an Access application](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/applications/methods/update)

PUT/{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}

##### [Delete an Access application](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/applications/methods/delete)

DELETE/{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}

##### [Revoke application tokens](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/applications/methods/revoke_tokens)

POST/{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}/revoke_tokens

#### Zero TrustAccessApplicationsCAs

##### [List short-lived certificate CAs](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/applications/subresources/cas/methods/list)

GET/{accounts_or_zones}/{account_or_zone_id}/access/apps/ca

##### [Get a short-lived certificate CA](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/applications/subresources/cas/methods/get)

GET/{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}/ca

##### [Create a short-lived certificate CA](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/applications/subresources/cas/methods/create)

POST/{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}/ca

##### [Delete a short-lived certificate CA](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/applications/subresources/cas/methods/delete)

DELETE/{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}/ca

#### Zero TrustAccessApplicationsUser Policy Checks

##### [Test Access policies](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/applications/subresources/user_policy_checks/methods/list)

GET/{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}/user_policy_checks

#### Zero TrustAccessApplicationsPolicies

##### [List Access application policies](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/applications/subresources/policies/methods/list)

GET/{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}/policies

##### [Get an Access application policy](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/applications/subresources/policies/methods/get)

GET/{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}/policies/{policy_id}

##### [Create an Access application policy](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/applications/subresources/policies/methods/create)

POST/{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}/policies

##### [Update an Access application policy](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/applications/subresources/policies/methods/update)

PUT/{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}/policies/{policy_id}

##### [Delete an Access application policy](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/applications/subresources/policies/methods/delete)

DELETE/{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}/policies/{policy_id}

#### Zero TrustAccessApplicationsPolicy Tests

##### [Get the current status of a given Access policy test](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/applications/subresources/policy_tests/methods/get)

GET/accounts/{account_id}/access/policy-tests/{policy_test_id}

##### [Start Access policy test](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/applications/subresources/policy_tests/methods/create)

POST/accounts/{account_id}/access/policy-tests

#### Zero TrustAccessApplicationsPolicy TestsUsers

##### [Get an Access policy test users page](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/applications/subresources/policy_tests/subresources/users/methods/list)

GET/accounts/{account_id}/access/policy-tests/{policy_test_id}/users

#### Zero TrustAccessApplicationsSettings

##### [Update Access application settings](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/applications/subresources/settings/methods/update)

PUT/{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}/settings

##### [Update Access application settings](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/applications/subresources/settings/methods/edit)

PATCH/{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}/settings

#### Zero TrustAccessCertificates

##### [List mTLS certificates](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/certificates/methods/list)

GET/{accounts_or_zones}/{account_or_zone_id}/access/certificates

##### [Get an mTLS certificate](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/certificates/methods/get)

GET/{accounts_or_zones}/{account_or_zone_id}/access/certificates/{certificate_id}

##### [Add an mTLS certificate](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/certificates/methods/create)

POST/{accounts_or_zones}/{account_or_zone_id}/access/certificates

##### [Update an mTLS certificate](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/certificates/methods/update)

PUT/{accounts_or_zones}/{account_or_zone_id}/access/certificates/{certificate_id}

##### [Delete an mTLS certificate](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/certificates/methods/delete)

DELETE/{accounts_or_zones}/{account_or_zone_id}/access/certificates/{certificate_id}

#### Zero TrustAccessCertificatesSettings

##### [List all mTLS hostname settings](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/certificates/subresources/settings/methods/get)

GET/{accounts_or_zones}/{account_or_zone_id}/access/certificates/settings

##### [Update an mTLS certificate's hostname settings](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/certificates/subresources/settings/methods/update)

PUT/{accounts_or_zones}/{account_or_zone_id}/access/certificates/settings

#### Zero TrustAccessGroups

##### [List Access groups](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/groups/methods/list)

GET/{accounts_or_zones}/{account_or_zone_id}/access/groups

##### [Get an Access group](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/groups/methods/get)

GET/{accounts_or_zones}/{account_or_zone_id}/access/groups/{group_id}

##### [Create an Access group](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/groups/methods/create)

POST/{accounts_or_zones}/{account_or_zone_id}/access/groups

##### [Update an Access group](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/groups/methods/update)

PUT/{accounts_or_zones}/{account_or_zone_id}/access/groups/{group_id}

##### [Delete an Access group](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/groups/methods/delete)

DELETE/{accounts_or_zones}/{account_or_zone_id}/access/groups/{group_id}

#### Zero TrustAccessService Tokens

##### [List service tokens](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/service_tokens/methods/list)

GET/{accounts_or_zones}/{account_or_zone_id}/access/service_tokens

##### [Get a service token](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/service_tokens/methods/get)

GET/{accounts_or_zones}/{account_or_zone_id}/access/service_tokens/{service_token_id}

##### [Create a service token](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/service_tokens/methods/create)

POST/{accounts_or_zones}/{account_or_zone_id}/access/service_tokens

##### [Update a service token](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/service_tokens/methods/update)

PUT/{accounts_or_zones}/{account_or_zone_id}/access/service_tokens/{service_token_id}

##### [Delete a service token](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/service_tokens/methods/delete)

DELETE/{accounts_or_zones}/{account_or_zone_id}/access/service_tokens/{service_token_id}

##### [Refresh a service token](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/service_tokens/methods/refresh)

POST/accounts/{account_id}/access/service_tokens/{service_token_id}/refresh

##### [Rotate a service token](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/service_tokens/methods/rotate)

POST/accounts/{account_id}/access/service_tokens/{service_token_id}/rotate

#### Zero TrustAccessBookmarks

##### [List Bookmark applications](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/bookmarks/methods/list)

Deprecated

GET/accounts/{account_id}/access/bookmarks

##### [Get a Bookmark application](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/bookmarks/methods/get)

Deprecated

GET/accounts/{account_id}/access/bookmarks/{bookmark_id}

##### [Create a Bookmark application](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/bookmarks/methods/create)

Deprecated

POST/accounts/{account_id}/access/bookmarks/{bookmark_id}

##### [Update a Bookmark application](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/bookmarks/methods/update)

Deprecated

PUT/accounts/{account_id}/access/bookmarks/{bookmark_id}

##### [Delete a Bookmark application](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/bookmarks/methods/delete)

Deprecated

DELETE/accounts/{account_id}/access/bookmarks/{bookmark_id}

#### Zero TrustAccessKeys

##### [Get the Access key configuration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/keys/methods/get)

GET/accounts/{account_id}/access/keys

##### [Update the Access key configuration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/keys/methods/update)

PUT/accounts/{account_id}/access/keys

##### [Rotate Access keys](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/keys/methods/rotate)

POST/accounts/{account_id}/access/keys/rotate

#### Zero TrustAccessLogs

#### Zero TrustAccessLogsAccess Requests

##### [Get Access authentication logs](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/logs/subresources/access_requests/methods/list)

GET/accounts/{account_id}/access/logs/access_requests

#### Zero TrustAccessLogsSCIM

#### Zero TrustAccessLogsSCIMUpdates

##### [List Access SCIM update logs](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/logs/subresources/scim/subresources/updates/methods/list)

GET/accounts/{account_id}/access/logs/scim/updates

#### Zero TrustAccessUsers

##### [Get users](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/users/methods/list)

GET/accounts/{account_id}/access/users

##### [Get a user](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/users/methods/get)

GET/accounts/{account_id}/access/users/{user_id}

##### [Create a user](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/users/methods/create)

POST/accounts/{account_id}/access/users

##### [Update a user](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/users/methods/update)

PUT/accounts/{account_id}/access/users/{user_id}

##### [Delete a user](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/users/methods/delete)

DELETE/accounts/{account_id}/access/users/{user_id}

#### Zero TrustAccessUsersActive Sessions

##### [Get active sessions](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/users/subresources/active_sessions/methods/list)

GET/accounts/{account_id}/access/users/{user_id}/active_sessions

##### [Get single active session](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/users/subresources/active_sessions/methods/get)

GET/accounts/{account_id}/access/users/{user_id}/active_sessions/{nonce}

#### Zero TrustAccessUsersLast Seen Identity

##### [Get last seen identity](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/users/subresources/last_seen_identity/methods/get)

GET/accounts/{account_id}/access/users/{user_id}/last_seen_identity

#### Zero TrustAccessUsersFailed Logins

##### [Get failed logins](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/users/subresources/failed_logins/methods/list)

GET/accounts/{account_id}/access/users/{user_id}/failed_logins

#### Zero TrustAccessCustom Pages

##### [List custom pages](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/custom_pages/methods/list)

GET/accounts/{account_id}/access/custom_pages

##### [Get a custom page](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/custom_pages/methods/get)

GET/accounts/{account_id}/access/custom_pages/{custom_page_id}

##### [Create a custom page](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/custom_pages/methods/create)

POST/accounts/{account_id}/access/custom_pages

##### [Update a custom page](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/custom_pages/methods/update)

PUT/accounts/{account_id}/access/custom_pages/{custom_page_id}

##### [Delete a custom page](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/custom_pages/methods/delete)

DELETE/accounts/{account_id}/access/custom_pages/{custom_page_id}

#### Zero TrustAccessTags

##### [List tags](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/tags/methods/list)

GET/accounts/{account_id}/access/tags

##### [Get a tag](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/tags/methods/get)

GET/accounts/{account_id}/access/tags/{tag_name}

##### [Create a tag](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/tags/methods/create)

POST/accounts/{account_id}/access/tags

##### [Update a tag](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/tags/methods/update)

PUT/accounts/{account_id}/access/tags/{tag_name}

##### [Delete a tag](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/tags/methods/delete)

DELETE/accounts/{account_id}/access/tags/{tag_name}

#### Zero TrustAccessPolicies

##### [List Access reusable policies](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/policies/methods/list)

GET/accounts/{account_id}/access/policies

##### [Get an Access reusable policy](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/policies/methods/get)

GET/accounts/{account_id}/access/policies/{policy_id}

##### [Create an Access reusable policy](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/policies/methods/create)

POST/accounts/{account_id}/access/policies

##### [Update an Access reusable policy](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/policies/methods/update)

PUT/accounts/{account_id}/access/policies/{policy_id}

##### [Delete an Access reusable policy](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/policies/methods/delete)

DELETE/accounts/{account_id}/access/policies/{policy_id}

#### Zero TrustCasb

#### Zero TrustCasbApplications

##### [List applications](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/applications/methods/list)

GET/accounts/{account_id}/one/applications

##### [Get application details](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/applications/methods/get)

GET/accounts/{account_id}/one/applications/{application_id}

#### Zero TrustCasbApplicationsAuth Methods

##### [Get auth methods](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/applications/subresources/auth_methods/methods/list)

GET/accounts/{account_id}/one/applications/{application_id}/auth-methods

#### Zero TrustCasbIntegrations

##### [List integrations](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/integrations/methods/list)

GET/accounts/{account_id}/one/integrations

##### [Get integration details](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/integrations/methods/get)

GET/accounts/{account_id}/one/integrations/{id}

##### [Create integration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/integrations/methods/create)

POST/accounts/{account_id}/one/integrations

##### [Update integration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/integrations/methods/update)

PATCH/accounts/{account_id}/one/integrations/{id}

##### [Delete integration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/integrations/methods/delete)

DELETE/accounts/{account_id}/one/integrations/{id}

##### [Pause integration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/integrations/methods/pause)

POST/accounts/{account_id}/one/integrations/{id}/pause

##### [Resume integration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/integrations/methods/resume)

POST/accounts/{account_id}/one/integrations/{id}/resume

#### Zero TrustCasbPosture

#### Zero TrustCasbPostureFindings

##### [List posture findings](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/findings/methods/list)

GET/accounts/{account_id}/data-security/posture/findings

##### [Get a posture finding](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/findings/methods/get)

GET/accounts/{account_id}/data-security/posture/findings/{finding_id}

##### [Create new findings export request](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/findings/methods/export)

POST/accounts/{account_id}/data-security/posture/findings/export

##### [Mark a finding as ignored](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/findings/methods/ignore)

POST/accounts/{account_id}/data-security/posture/findings/ignore

##### [Remove ignore marker from a finding](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/findings/methods/unignore)

POST/accounts/{account_id}/data-security/posture/findings/unignore

##### [Update the severity for a finding](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/findings/methods/tune_severity)

POST/accounts/{account_id}/data-security/posture/findings/{finding_id}/tune_finding_severity

##### [Reset severity for a finding back to the default](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/findings/methods/reset_severity)

POST/accounts/{account_id}/data-security/posture/findings/{finding_id}/reset_finding_severity

#### Zero TrustCasbPostureFindingsInstances

##### [List instances of a finding](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/findings/subresources/instances/methods/list)

GET/accounts/{account_id}/data-security/posture/findings/{finding_id}/instances

##### [Get a finding instance using an instance ID](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/findings/subresources/instances/methods/get)

GET/accounts/{account_id}/data-security/posture/findings/{finding_id}/instances/{instance_id}

##### [Create a finding instances export](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/findings/subresources/instances/methods/export)

POST/accounts/{account_id}/data-security/posture/findings/{storage_namespace_id}/instances/export

##### [Archive a finding](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/findings/subresources/instances/methods/archive)

POST/accounts/{account_id}/data-security/posture/findings/{finding_id}/instances/archive

##### [Remove the archive marking from a finding instance](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/findings/subresources/instances/methods/unarchive)

POST/accounts/{account_id}/data-security/posture/findings/{finding_id}/instances/unarchive

#### Zero TrustCasbPostureExports

##### [List all export jobs](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/exports/methods/list)

GET/accounts/{account_id}/data-security/posture/exports

##### [Get a single export job](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/exports/methods/get)

GET/accounts/{account_id}/data-security/posture/exports/{id}

#### Zero TrustCasbPostureFinding Types

##### [List all finding types](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/finding_types/methods/list)

GET/accounts/{account_id}/data-security/posture/finding_types

##### [Get finding by ID](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/finding_types/methods/get)

GET/accounts/{account_id}/data-security/posture/finding_types/{finding_type_id}

#### Zero TrustCasbPostureFinding TypesRemediation Types

##### [List remediation types for a finding type](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/finding_types/subresources/remediation_types/methods/list)

GET/accounts/{account_id}/data-security/posture/finding_types/{finding_type_id}/remediation_types

#### Zero TrustCasbPostureContent

##### [List DLP content findings](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/content/methods/list)

GET/accounts/{account_id}/data-security/posture/content

##### [Create a content export](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/content/methods/export)

POST/accounts/{account_id}/data-security/posture/content/export

#### Zero TrustCasbPostureRemediations

#### Zero TrustCasbPostureRemediationsJobs

##### [List remediation jobs](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/remediations/subresources/jobs/methods/list)

GET/accounts/{account_id}/data-security/posture/remediations/jobs

##### [Creates remediation jobs](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/remediations/subresources/jobs/methods/create)

POST/accounts/{account_id}/data-security/posture/remediations/jobs

##### [Create a remediation jobs export](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/remediations/subresources/jobs/methods/export)

POST/accounts/{account_id}/data-security/posture/remediations/jobs/export

#### Zero TrustCasbPosturePolicies

##### [List policy configurations](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/policies/methods/list)

GET/accounts/{account_id}/data-security/posture/policies

##### [Create a new policy configuration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/policies/methods/create)

POST/accounts/{account_id}/data-security/posture/policies

##### [Get a policy configuration by ID](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/policies/methods/get)

GET/accounts/{account_id}/data-security/posture/policies/{policy_id}

##### [Update a policy configuration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/policies/methods/update)

PUT/accounts/{account_id}/data-security/posture/policies/{policy_id}

##### [Delete a policy configuration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/policies/methods/delete)

DELETE/accounts/{account_id}/data-security/posture/policies/{policy_id}

#### Zero TrustCasbPostureWebhooks

##### [List webhook configurations](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/webhooks/methods/list)

GET/accounts/{account_id}/data-security/posture/webhooks

##### [Create a new webhook configuration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/webhooks/methods/create)

POST/accounts/{account_id}/data-security/posture/webhooks

##### [Get webhook configuration by ID](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/webhooks/methods/get)

GET/accounts/{account_id}/data-security/posture/webhooks/{webhook_id}

##### [Update an existing webhook configuration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/webhooks/methods/update)

PUT/accounts/{account_id}/data-security/posture/webhooks/{webhook_id}

##### [Delete a webhook configuration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/webhooks/methods/delete)

DELETE/accounts/{account_id}/data-security/posture/webhooks/{webhook_id}

##### [Test a webhook configuration before creating it](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/webhooks/methods/evaluate)

POST/accounts/{account_id}/data-security/posture/webhooks/evaluate

##### [Test an existing webhook configuration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/webhooks/methods/evaluate_existing)

POST/accounts/{account_id}/data-security/posture/webhooks/{webhook_id}/evaluate

#### Zero TrustCasbPostureWebhooksJobs

##### [Create webhook jobs](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/webhooks/subresources/jobs/methods/create)

POST/accounts/{account_id}/data-security/posture/webhooks/jobs

#### Zero TrustDEX

#### Zero TrustDEXWARP Change Events

##### [List WARP change events.](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex/subresources/warp_change_events/methods/get)

GET/accounts/{account_id}/dex/warp-change-events

#### Zero TrustDEXCommands

##### [List account commands](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex/subresources/commands/methods/list)

GET/accounts/{account_id}/dex/commands

##### [Create account commands](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex/subresources/commands/methods/create)

POST/accounts/{account_id}/dex/commands

#### Zero TrustDEXCommandsDevices

##### [List devices eligible for remote captures](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex/subresources/commands/subresources/devices/methods/list)

GET/accounts/{account_id}/dex/commands/devices

#### Zero TrustDEXCommandsDownloads

##### [Download command output file](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex/subresources/commands/subresources/downloads/methods/get)

GET/accounts/{account_id}/dex/commands/{command_id}/downloads/{filename}

#### Zero TrustDEXCommandsQuota

##### [Returns account commands usage, quota, and reset time](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex/subresources/commands/subresources/quota/methods/get)

GET/accounts/{account_id}/dex/commands/quota

#### Zero TrustDEXColos

##### [List Cloudflare colos](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex/subresources/colos/methods/list)

GET/accounts/{account_id}/dex/colos

#### Zero TrustDEXFleet Status

##### [Get live aggregate device details by dimension](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex/subresources/fleet_status/methods/live)

GET/accounts/{account_id}/dex/fleet-status/live

##### [Get over time aggregate details for devices by dimension](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex/subresources/fleet_status/methods/over_time)

GET/accounts/{account_id}/dex/fleet-status/over-time

#### Zero TrustDEXFleet StatusDevices

##### [List details of devices using WARP.](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex/subresources/fleet_status/subresources/devices/methods/list)

GET/accounts/{account_id}/dex/fleet-status/devices

#### Zero TrustDEXHTTP Tests

##### [Get details and aggregate metrics for an http test](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex/subresources/http_tests/methods/get)

GET/accounts/{account_id}/dex/http-tests/{test_id}

#### Zero TrustDEXHTTP TestsPercentiles

##### [Get percentiles for an http test](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex/subresources/http_tests/subresources/percentiles/methods/get)

GET/accounts/{account_id}/dex/http-tests/{test_id}/percentiles

#### Zero TrustDEXTests

##### [List DEX test analytics](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex/subresources/tests/methods/list)

GET/accounts/{account_id}/dex/tests/overview

#### Zero TrustDEXTestsUnique Devices

##### [Get count of devices targeted](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex/subresources/tests/subresources/unique_devices/methods/list)

GET/accounts/{account_id}/dex/tests/unique-devices

#### Zero TrustDEXTraceroute Test Results

#### Zero TrustDEXTraceroute Test ResultsNetwork Path

##### [Get details for a specific traceroute test run](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex/subresources/traceroute_test_results/subresources/network_path/methods/get)

GET/accounts/{account_id}/dex/traceroute-test-results/{test_result_id}/network-path

#### Zero TrustDEXTraceroute Tests

##### [Get details and aggregate metrics for a traceroute test](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex/subresources/traceroute_tests/methods/get)

GET/accounts/{account_id}/dex/traceroute-tests/{test_id}

##### [Get percentiles for a traceroute test](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex/subresources/traceroute_tests/methods/percentiles)

GET/accounts/{account_id}/dex/traceroute-tests/{test_id}/percentiles

##### [Get network path breakdown for a traceroute test](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex/subresources/traceroute_tests/methods/network_path)

GET/accounts/{account_id}/dex/traceroute-tests/{test_id}/network-path

#### Zero TrustDEXRules

##### [Get DEX Rule](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex/subresources/rules/methods/get)

GET/accounts/{account_id}/dex/rules/{rule_id}

##### [Delete a DEX Rule](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex/subresources/rules/methods/delete)

DELETE/accounts/{account_id}/dex/rules/{rule_id}

##### [Update a DEX Rule](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex/subresources/rules/methods/update)

PATCH/accounts/{account_id}/dex/rules/{rule_id}

##### [Create a DEX Rule](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex/subresources/rules/methods/create)

POST/accounts/{account_id}/dex/rules

##### [List DEX Rules](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex/subresources/rules/methods/list)

GET/accounts/{account_id}/dex/rules

#### Zero TrustDEXDevices

#### Zero TrustDEXDevicesISPs

##### [List device ISPs](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex/subresources/devices/subresources/isps/methods/list)

GET/accounts/{account_id}/dex/devices/{device_id}/isps

#### Zero TrustTunnels

##### [List All Tunnels](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/methods/list)

GET/accounts/{account_id}/tunnels

#### Zero TrustTunnelsCloudflared

##### [List Cloudflare Tunnels](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/list)

GET/accounts/{account_id}/cfd_tunnel

##### [Get a Cloudflare Tunnel](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/get)

GET/accounts/{account_id}/cfd_tunnel/{tunnel_id}

##### [Create a Cloudflare Tunnel](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/create)

POST/accounts/{account_id}/cfd_tunnel

##### [Update a Cloudflare Tunnel](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/edit)

PATCH/accounts/{account_id}/cfd_tunnel/{tunnel_id}

##### [Delete a Cloudflare Tunnel](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/delete)

DELETE/accounts/{account_id}/cfd_tunnel/{tunnel_id}

#### Zero TrustTunnelsCloudflaredConfigurations

##### [Get Tunnel configuration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/subresources/configurations/methods/get)

GET/accounts/{account_id}/cfd_tunnel/{tunnel_id}/configurations

##### [Update Tunnel configuration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/subresources/configurations/methods/update)

PUT/accounts/{account_id}/cfd_tunnel/{tunnel_id}/configurations

#### Zero TrustTunnelsCloudflaredConnections

##### [List Cloudflare Tunnel connections](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/subresources/connections/methods/get)

GET/accounts/{account_id}/cfd_tunnel/{tunnel_id}/connections

##### [Clean up Cloudflare Tunnel connections](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/subresources/connections/methods/delete)

DELETE/accounts/{account_id}/cfd_tunnel/{tunnel_id}/connections

#### Zero TrustTunnelsCloudflaredToken

##### [Get a Cloudflare Tunnel token](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/subresources/token/methods/get)

GET/accounts/{account_id}/cfd_tunnel/{tunnel_id}/token

#### Zero TrustTunnelsCloudflaredConnectors

##### [Get Cloudflare Tunnel connector](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/subresources/connectors/methods/get)

GET/accounts/{account_id}/cfd_tunnel/{tunnel_id}/connectors/{connector_id}

#### Zero TrustTunnelsCloudflaredManagement

##### [Get a Cloudflare Tunnel management token](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/subresources/management/methods/create)

POST/accounts/{account_id}/cfd_tunnel/{tunnel_id}/management

#### Zero TrustTunnelsWARP Connector

##### [List Mesh nodes](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/list)

GET/accounts/{account_id}/warp_connector

##### [Get a Mesh node](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/get)

GET/accounts/{account_id}/warp_connector/{tunnel_id}

##### [Create a Mesh node](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/create)

POST/accounts/{account_id}/warp_connector

##### [Update a Mesh node](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/edit)

PATCH/accounts/{account_id}/warp_connector/{tunnel_id}

##### [Delete a Mesh node](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/delete)

DELETE/accounts/{account_id}/warp_connector/{tunnel_id}

#### Zero TrustTunnelsWARP ConnectorToken

##### [Get a Mesh node token](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/subresources/token/methods/get)

GET/accounts/{account_id}/warp_connector/{tunnel_id}/token

#### Zero TrustTunnelsWARP ConnectorConnections

##### [List Mesh node connections](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/subresources/connections/methods/get)

GET/accounts/{account_id}/warp_connector/{tunnel_id}/connections

#### Zero TrustTunnelsWARP ConnectorConnectors

##### [Get a Mesh node connector](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/subresources/connectors/methods/get)

GET/accounts/{account_id}/warp_connector/{tunnel_id}/connectors/{connector_id}

#### Zero TrustTunnelsWARP ConnectorFailover

##### [Trigger a manual failover for a Mesh node](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/subresources/failover/methods/update)

PUT/accounts/{account_id}/warp_connector/{tunnel_id}/failover

#### Zero TrustTunnelsWARP ConnectorConfigurations

##### [Get Mesh node HA configuration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/subresources/configurations/methods/get)

GET/accounts/{account_id}/warp_connector/{tunnel_id}/configurations

##### [Update Mesh node HA configuration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/subresources/configurations/methods/update)

PUT/accounts/{account_id}/warp_connector/{tunnel_id}/configurations

#### Zero TrustConnectivity Settings

##### [Get Zero Trust Connectivity Settings](https://developers.cloudflare.com/api/resources/zero_trust/subresources/connectivity_settings/methods/get)

GET/accounts/{account_id}/zerotrust/connectivity_settings

##### [Updates the Zero Trust Connectivity Settings](https://developers.cloudflare.com/api/resources/zero_trust/subresources/connectivity_settings/methods/edit)

PATCH/accounts/{account_id}/zerotrust/connectivity_settings

#### Zero TrustDLP

#### Zero TrustDLPCustom Prompt Topics

##### [List custom prompt topics](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/custom_prompt_topics/methods/list)

GET/accounts/{account_id}/dlp/custom_prompt_topics

##### [Get custom prompt topic](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/custom_prompt_topics/methods/get)

GET/accounts/{account_id}/dlp/custom_prompt_topics/{entry_id}

##### [Create custom prompt topic](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/custom_prompt_topics/methods/create)

POST/accounts/{account_id}/dlp/custom_prompt_topics

##### [Update custom prompt topic](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/custom_prompt_topics/methods/update)

PUT/accounts/{account_id}/dlp/custom_prompt_topics/{entry_id}

##### [Delete custom prompt topic](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/custom_prompt_topics/methods/delete)

DELETE/accounts/{account_id}/dlp/custom_prompt_topics/{entry_id}

#### Zero TrustDLPDatasets

##### [Fetch all datasets](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/datasets/methods/list)

GET/accounts/{account_id}/dlp/datasets

##### [Fetch a specific dataset](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/datasets/methods/get)

GET/accounts/{account_id}/dlp/datasets/{dataset_id}

##### [Create a new dataset](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/datasets/methods/create)

POST/accounts/{account_id}/dlp/datasets

##### [Update details about a dataset](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/datasets/methods/update)

PUT/accounts/{account_id}/dlp/datasets/{dataset_id}

##### [Delete a dataset](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/datasets/methods/delete)

DELETE/accounts/{account_id}/dlp/datasets/{dataset_id}

#### Zero TrustDLPDatasetsUpload

##### [Prepare to upload a new version of a dataset](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/datasets/subresources/upload/methods/create)

POST/accounts/{account_id}/dlp/datasets/{dataset_id}/upload

##### [Upload a new version of a dataset](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/datasets/subresources/upload/methods/edit)

POST/accounts/{account_id}/dlp/datasets/{dataset_id}/upload/{version}

#### Zero TrustDLPDatasetsVersions

##### [Sets the column information for a multi-column upload](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/datasets/subresources/versions/methods/create)

POST/accounts/{account_id}/dlp/datasets/{dataset_id}/versions/{version}

#### Zero TrustDLPDatasetsVersionsEntries

##### [Upload a new version of a multi-column dataset](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/datasets/subresources/versions/subresources/entries/methods/create)

POST/accounts/{account_id}/dlp/datasets/{dataset_id}/versions/{version}/entries/{entry_id}

#### Zero TrustDLPPatterns

##### [Validate a DLP regex pattern](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/patterns/methods/validate)

POST/accounts/{account_id}/dlp/patterns/validate

#### Zero TrustDLPPayload Logs

##### [Get payload log settings](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/payload_logs/methods/get)

Deprecated

GET/accounts/{account_id}/dlp/payload_log

##### [Set payload log settings](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/payload_logs/methods/update)

Deprecated

PUT/accounts/{account_id}/dlp/payload_log

#### Zero TrustDLPSettings

##### [Get DLP account-level settings.](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/settings/methods/get)

GET/accounts/{account_id}/dlp/settings

##### [Update DLP account-level settings (full replacement).](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/settings/methods/update)

PUT/accounts/{account_id}/dlp/settings

##### [Partially update DLP account-level settings.](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/settings/methods/edit)

PATCH/accounts/{account_id}/dlp/settings

##### [Delete (reset) DLP account-level settings to initial values.](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/settings/methods/delete)

DELETE/accounts/{account_id}/dlp/settings

#### Zero TrustDLPEmail

#### Zero TrustDLPEmailAccount Mapping

##### [Get mapping](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/email/subresources/account_mapping/methods/get)

GET/accounts/{account_id}/dlp/email/account_mapping

##### [Create mapping](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/email/subresources/account_mapping/methods/create)

POST/accounts/{account_id}/dlp/email/account_mapping

#### Zero TrustDLPEmailRules

##### [List all email scanner rules](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/email/subresources/rules/methods/list)

GET/accounts/{account_id}/dlp/email/rules

##### [Get an email scanner rule](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/email/subresources/rules/methods/get)

GET/accounts/{account_id}/dlp/email/rules/{rule_id}

##### [Create email scanner rule](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/email/subresources/rules/methods/create)

POST/accounts/{account_id}/dlp/email/rules

##### [Update email scanner rule](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/email/subresources/rules/methods/update)

PUT/accounts/{account_id}/dlp/email/rules/{rule_id}

##### [Delete email scanner rule](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/email/subresources/rules/methods/delete)

DELETE/accounts/{account_id}/dlp/email/rules/{rule_id}

##### [Update email scanner rule priorities](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/email/subresources/rules/methods/bulk_edit)

PATCH/accounts/{account_id}/dlp/email/rules

#### Zero TrustDLPProfiles

##### [List all profiles](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/profiles/methods/list)

GET/accounts/{account_id}/dlp/profiles

##### [Get DLP Profile](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/profiles/methods/get)

GET/accounts/{account_id}/dlp/profiles/{profile_id}

#### Zero TrustDLPProfilesCustom

##### [Get custom profile](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/profiles/subresources/custom/methods/get)

GET/accounts/{account_id}/dlp/profiles/custom/{profile_id}

##### [Create custom profile](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/profiles/subresources/custom/methods/create)

POST/accounts/{account_id}/dlp/profiles/custom

##### [Update custom profile](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/profiles/subresources/custom/methods/update)

PUT/accounts/{account_id}/dlp/profiles/custom/{profile_id}

##### [Delete custom profile](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/profiles/subresources/custom/methods/delete)

DELETE/accounts/{account_id}/dlp/profiles/custom/{profile_id}

#### Zero TrustDLPProfilesPredefined

##### [Get predefined profile config](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/profiles/subresources/predefined/methods/get)

GET/accounts/{account_id}/dlp/profiles/predefined/{profile_id}/config

##### [Update predefined profile config](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/profiles/subresources/predefined/methods/update)

PUT/accounts/{account_id}/dlp/profiles/predefined/{profile_id}/config

##### [Delete predefined profile](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/profiles/subresources/predefined/methods/delete)

DELETE/accounts/{account_id}/dlp/profiles/predefined/{profile_id}

#### Zero TrustDLPLimits

##### [Fetch limits associated with DLP for account](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/limits/methods/list)

GET/accounts/{account_id}/dlp/limits

#### Zero TrustDLPEntries

##### [List all entries](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/entries/methods/list)

GET/accounts/{account_id}/dlp/entries

##### [Get DLP Entry](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/entries/methods/get)

GET/accounts/{account_id}/dlp/entries/{entry_id}

##### [Create custom entry](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/entries/methods/create)

POST/accounts/{account_id}/dlp/entries

##### [Update entry](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/entries/methods/update)

PUT/accounts/{account_id}/dlp/entries/{entry_id}

##### [Delete custom entry](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/entries/methods/delete)

DELETE/accounts/{account_id}/dlp/entries/{entry_id}

#### Zero TrustDLPEntriesCustom

##### [Create custom entry](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/entries/subresources/custom/methods/create)

POST/accounts/{account_id}/dlp/entries

##### [Update custom entry](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/entries/subresources/custom/methods/update)

PUT/accounts/{account_id}/dlp/entries/custom/{entry_id}

##### [Delete custom entry](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/entries/subresources/custom/methods/delete)

DELETE/accounts/{account_id}/dlp/entries/{entry_id}

##### [Get DLP Entry](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/entries/subresources/custom/methods/get)

GET/accounts/{account_id}/dlp/entries/{entry_id}

##### [List all entries](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/entries/subresources/custom/methods/list)

GET/accounts/{account_id}/dlp/entries

#### Zero TrustDLPEntriesPredefined

##### [Create predefined entry](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/entries/subresources/predefined/methods/create)

POST/accounts/{account_id}/dlp/entries/predefined

##### [Update predefined entry](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/entries/subresources/predefined/methods/update)

PUT/accounts/{account_id}/dlp/entries/predefined/{entry_id}

##### [Delete predefined entry](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/entries/subresources/predefined/methods/delete)

DELETE/accounts/{account_id}/dlp/entries/predefined/{entry_id}

##### [Get DLP Entry](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/entries/subresources/predefined/methods/get)

GET/accounts/{account_id}/dlp/entries/{entry_id}

##### [List all entries](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/entries/subresources/predefined/methods/list)

GET/accounts/{account_id}/dlp/entries

#### Zero TrustDLPEntriesIntegration

##### [Create integration entry](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/entries/subresources/integration/methods/create)

POST/accounts/{account_id}/dlp/entries/integration

##### [Update integration entry](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/entries/subresources/integration/methods/update)

PUT/accounts/{account_id}/dlp/entries/integration/{entry_id}

##### [Delete integration entry](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/entries/subresources/integration/methods/delete)

DELETE/accounts/{account_id}/dlp/entries/integration/{entry_id}

##### [Get DLP Entry](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/entries/subresources/integration/methods/get)

GET/accounts/{account_id}/dlp/entries/{entry_id}

##### [List all entries](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/entries/subresources/integration/methods/list)

GET/accounts/{account_id}/dlp/entries

#### Zero TrustDLPSensitivity Groups

##### [Retrieve all sensitivity groups in an account](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/sensitivity_groups/methods/list)

GET/accounts/{account_id}/dlp/sensitivity_groups

##### [Retrieve a specific sensitivity group.](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/sensitivity_groups/methods/get)

GET/accounts/{account_id}/dlp/sensitivity_groups/{sensitivity_group_id}

##### [Creates a new sensitivity group.](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/sensitivity_groups/methods/create)

POST/accounts/{account_id}/dlp/sensitivity_groups

##### [Update the attributes of a single sensitivity group.](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/sensitivity_groups/methods/update)

PUT/accounts/{account_id}/dlp/sensitivity_groups/{sensitivity_group_id}

##### [Delete a single sensitivity group.](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/sensitivity_groups/methods/delete)

DELETE/accounts/{account_id}/dlp/sensitivity_groups/{sensitivity_group_id}

#### Zero TrustDLPSensitivity GroupsLevels

##### [Retrieve all sensitivity levels in a sensitivity group](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/sensitivity_groups/subresources/levels/methods/list)

GET/accounts/{account_id}/dlp/sensitivity_groups/{sensitivity_group_id}/levels

##### [Retrieve a specific sensitivity level.](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/sensitivity_groups/subresources/levels/methods/get)

GET/accounts/{account_id}/dlp/sensitivity_groups/{sensitivity_group_id}/levels/{sensitivity_level_id}

##### [Creates a new sensitivity level.](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/sensitivity_groups/subresources/levels/methods/create)

POST/accounts/{account_id}/dlp/sensitivity_groups/{sensitivity_group_id}/levels

##### [Update the attributes of a single sensitivity level.](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/sensitivity_groups/subresources/levels/methods/update)

PUT/accounts/{account_id}/dlp/sensitivity_groups/{sensitivity_group_id}/levels/{sensitivity_level_id}

##### [Delete a single sensitivity level.](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/sensitivity_groups/subresources/levels/methods/delete)

DELETE/accounts/{account_id}/dlp/sensitivity_groups/{sensitivity_group_id}/levels/{sensitivity_level_id}

#### Zero TrustDLPSensitivity GroupsLevelsOrder

##### [Retrieve the ordered list of level IDs for a sensitivity group.](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/sensitivity_groups/subresources/levels/subresources/order/methods/get)

GET/accounts/{account_id}/dlp/sensitivity_groups/{sensitivity_group_id}/level_order

##### [Set the ordering of levels within a sensitivity group.](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/sensitivity_groups/subresources/levels/subresources/order/methods/update)

PUT/accounts/{account_id}/dlp/sensitivity_groups/{sensitivity_group_id}/level_order

#### Zero TrustDLPData Tag Categories

##### [Retrieve all data tag categories in an account](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/data_tag_categories/methods/list)

GET/accounts/{account_id}/dlp/data_tag_categories

##### [Retrieve a specific data tag category.](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/data_tag_categories/methods/get)

GET/accounts/{account_id}/dlp/data_tag_categories/{category_id}

##### [Creates a new data tag category.](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/data_tag_categories/methods/create)

POST/accounts/{account_id}/dlp/data_tag_categories

##### [Update the attributes of a single data tag category.](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/data_tag_categories/methods/update)

PUT/accounts/{account_id}/dlp/data_tag_categories/{category_id}

##### [Delete a single data tag category.](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/data_tag_categories/methods/delete)

DELETE/accounts/{account_id}/dlp/data_tag_categories/{category_id}

#### Zero TrustDLPData Tag CategoriesData Tags

##### [Retrieve all data tags in a data tag category](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/data_tag_categories/subresources/data_tags/methods/list)

GET/accounts/{account_id}/dlp/data_tag_categories/{category_id}/data_tags

##### [Retrieve a specific data tag.](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/data_tag_categories/subresources/data_tags/methods/get)

GET/accounts/{account_id}/dlp/data_tag_categories/{category_id}/data_tags/{tag_id}

##### [Creates a new data tag.](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/data_tag_categories/subresources/data_tags/methods/create)

POST/accounts/{account_id}/dlp/data_tag_categories/{category_id}/data_tags

##### [Update the attributes of a single data tag.](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/data_tag_categories/subresources/data_tags/methods/update)

PUT/accounts/{account_id}/dlp/data_tag_categories/{category_id}/data_tags/{tag_id}

##### [Delete a single data tag.](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/data_tag_categories/subresources/data_tags/methods/delete)

DELETE/accounts/{account_id}/dlp/data_tag_categories/{category_id}/data_tags/{tag_id}

#### Zero TrustDLPData Classes

##### [Retrieve all data classes in an account](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/data_classes/methods/list)

GET/accounts/{account_id}/dlp/data_classes

##### [Retrieve a specific data class](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/data_classes/methods/get)

GET/accounts/{account_id}/dlp/data_classes/{data_class_id}

##### [Creates a new data class](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/data_classes/methods/create)

POST/accounts/{account_id}/dlp/data_classes

##### [Update the attributes of a single data class](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/data_classes/methods/update)

PUT/accounts/{account_id}/dlp/data_classes/{data_class_id}

##### [Delete a single data class](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/data_classes/methods/delete)

DELETE/accounts/{account_id}/dlp/data_classes/{data_class_id}

#### Zero TrustGateway

##### [Get Zero Trust account information](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/methods/list)

GET/accounts/{account_id}/gateway

##### [Create Zero Trust account](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/methods/create)

POST/accounts/{account_id}/gateway

#### Zero TrustGatewayAudit SSH Settings

##### [Get Zero Trust SSH settings](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/audit_ssh_settings/methods/get)

GET/accounts/{account_id}/gateway/audit_ssh_settings

##### [Update Zero Trust SSH settings](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/audit_ssh_settings/methods/update)

PUT/accounts/{account_id}/gateway/audit_ssh_settings

##### [Rotate Zero Trust SSH account seed](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/audit_ssh_settings/methods/rotate_seed)

POST/accounts/{account_id}/gateway/audit_ssh_settings/rotate_seed

#### Zero TrustGatewayCategories

##### [List categories](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/categories/methods/list)

GET/accounts/{account_id}/gateway/categories

#### Zero TrustGatewayApp Types

##### [List application and application type mappings](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/app_types/methods/list)

GET/accounts/{account_id}/gateway/app_types

#### Zero TrustGatewayConfigurations

##### [Get Zero Trust account configuration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/configurations/methods/get)

GET/accounts/{account_id}/gateway/configuration

##### [Update Zero Trust account configuration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/configurations/methods/update)

PUT/accounts/{account_id}/gateway/configuration

##### [Patch Zero Trust account configuration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/configurations/methods/edit)

PATCH/accounts/{account_id}/gateway/configuration

#### Zero TrustGatewayConfigurationsCustom Certificate

##### [Get Zero Trust certificate configuration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/configurations/subresources/custom_certificate/methods/get)

Deprecated

GET/accounts/{account_id}/gateway/configuration/custom_certificate

#### Zero TrustGatewayLists

##### [List Zero Trust lists](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/lists/methods/list)

GET/accounts/{account_id}/gateway/lists

##### [Get Zero Trust list details](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/lists/methods/get)

GET/accounts/{account_id}/gateway/lists/{list_id}

##### [Create Zero Trust list](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/lists/methods/create)

POST/accounts/{account_id}/gateway/lists

##### [Update Zero Trust list](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/lists/methods/update)

PUT/accounts/{account_id}/gateway/lists/{list_id}

##### [Patch Zero Trust list.](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/lists/methods/edit)

PATCH/accounts/{account_id}/gateway/lists/{list_id}

##### [Delete Zero Trust list](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/lists/methods/delete)

DELETE/accounts/{account_id}/gateway/lists/{list_id}

#### Zero TrustGatewayListsItems

##### [Get Zero Trust list items](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/lists/subresources/items/methods/list)

GET/accounts/{account_id}/gateway/lists/{list_id}/items

#### Zero TrustGatewayLocations

##### [List Zero Trust Gateway locations](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/locations/methods/list)

GET/accounts/{account_id}/gateway/locations

##### [Get Zero Trust Gateway location details](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/locations/methods/get)

GET/accounts/{account_id}/gateway/locations/{location_id}

##### [Create a Zero Trust Gateway location](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/locations/methods/create)

POST/accounts/{account_id}/gateway/locations

##### [Update a Zero Trust Gateway location](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/locations/methods/update)

PUT/accounts/{account_id}/gateway/locations/{location_id}

##### [Delete a Zero Trust Gateway location](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/locations/methods/delete)

DELETE/accounts/{account_id}/gateway/locations/{location_id}

#### Zero TrustGatewayLogging

##### [Get logging settings for the Zero Trust account](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/logging/methods/get)

GET/accounts/{account_id}/gateway/logging

##### [Update Zero Trust account logging settings](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/logging/methods/update)

PUT/accounts/{account_id}/gateway/logging

#### Zero TrustGatewayProxy Endpoints

##### [List proxy endpoints](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/proxy_endpoints/methods/list)

GET/accounts/{account_id}/gateway/proxy_endpoints

##### [Get a proxy endpoint](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/proxy_endpoints/methods/get)

GET/accounts/{account_id}/gateway/proxy_endpoints/{proxy_endpoint_id}

##### [Create a proxy endpoint](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/proxy_endpoints/methods/create)

POST/accounts/{account_id}/gateway/proxy_endpoints

##### [Update a proxy endpoint](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/proxy_endpoints/methods/edit)

PATCH/accounts/{account_id}/gateway/proxy_endpoints/{proxy_endpoint_id}

##### [Delete a proxy endpoint](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/proxy_endpoints/methods/delete)

DELETE/accounts/{account_id}/gateway/proxy_endpoints/{proxy_endpoint_id}

#### Zero TrustGatewayRules

##### [List Zero Trust Gateway rules](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/rules/methods/list)

GET/accounts/{account_id}/gateway/rules

##### [Get Zero Trust Gateway rule details.](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/rules/methods/get)

GET/accounts/{account_id}/gateway/rules/{rule_id}

##### [Create a Zero Trust Gateway rule](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/rules/methods/create)

POST/accounts/{account_id}/gateway/rules

##### [Update a Zero Trust Gateway rule](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/rules/methods/update)

PUT/accounts/{account_id}/gateway/rules/{rule_id}

##### [Delete a Zero Trust Gateway rule](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/rules/methods/delete)

DELETE/accounts/{account_id}/gateway/rules/{rule_id}

##### [List Zero Trust Gateway rules inherited from the parent account](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/rules/methods/list_tenant)

GET/accounts/{account_id}/gateway/rules/tenant

##### [Reset the expiration of a Zero Trust Gateway Rule](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/rules/methods/reset_expiration)

POST/accounts/{account_id}/gateway/rules/{rule_id}/reset_expiration

#### Zero TrustGatewayCertificates

##### [List Zero Trust certificates](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/certificates/methods/list)

GET/accounts/{account_id}/gateway/certificates

##### [Get Zero Trust certificate details](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/certificates/methods/get)

GET/accounts/{account_id}/gateway/certificates/{certificate_id}

##### [Create Zero Trust certificate](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/certificates/methods/create)

POST/accounts/{account_id}/gateway/certificates

##### [Delete Zero Trust certificate](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/certificates/methods/delete)

DELETE/accounts/{account_id}/gateway/certificates/{certificate_id}

##### [Activate a Zero Trust certificate](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/certificates/methods/activate)

POST/accounts/{account_id}/gateway/certificates/{certificate_id}/activate

##### [Deactivate a Zero Trust certificate](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/certificates/methods/deactivate)

POST/accounts/{account_id}/gateway/certificates/{certificate_id}/deactivate

#### Zero TrustGatewayPacfiles

##### [List PAC files](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/pacfiles/methods/list)

GET/accounts/{account_id}/gateway/pacfiles

##### [Get a PAC file](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/pacfiles/methods/get)

GET/accounts/{account_id}/gateway/pacfiles/{pacfile_id}

##### [Create a PAC file](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/pacfiles/methods/create)

POST/accounts/{account_id}/gateway/pacfiles

##### [Update a Zero Trust Gateway PAC file](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/pacfiles/methods/update)

PUT/accounts/{account_id}/gateway/pacfiles/{pacfile_id}

##### [Delete a PAC file](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/pacfiles/methods/delete)

DELETE/accounts/{account_id}/gateway/pacfiles/{pacfile_id}

#### Zero TrustNetworks

#### Zero TrustNetworksRoutes

##### [List tunnel routes](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/methods/list)

GET/accounts/{account_id}/teamnet/routes

##### [Get tunnel route](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/methods/get)

GET/accounts/{account_id}/teamnet/routes/{route_id}

##### [Create a tunnel route](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/methods/create)

POST/accounts/{account_id}/teamnet/routes

##### [Update a tunnel route](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/methods/edit)

PATCH/accounts/{account_id}/teamnet/routes/{route_id}

##### [Delete a tunnel route](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/methods/delete)

DELETE/accounts/{account_id}/teamnet/routes/{route_id}

#### Zero TrustNetworksRoutesIPs

##### [Get tunnel route by IP](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/subresources/ips/methods/get)

GET/accounts/{account_id}/teamnet/routes/ip/{ip}

#### Zero TrustNetworksRoutesNetworks

##### [Create a tunnel route (CIDR Endpoint)](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/subresources/networks/methods/create)

Deprecated

POST/accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}

##### [Update a tunnel route (CIDR Endpoint)](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/subresources/networks/methods/edit)

Deprecated

PATCH/accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}

##### [Delete a tunnel route (CIDR Endpoint)](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/subresources/networks/methods/delete)

Deprecated

DELETE/accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}

#### Zero TrustNetworksVirtual Networks

##### [List virtual networks](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/virtual_networks/methods/list)

GET/accounts/{account_id}/teamnet/virtual_networks

##### [Get a virtual network](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/virtual_networks/methods/get)

GET/accounts/{account_id}/teamnet/virtual_networks/{virtual_network_id}

##### [Create a virtual network](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/virtual_networks/methods/create)

POST/accounts/{account_id}/teamnet/virtual_networks

##### [Update a virtual network](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/virtual_networks/methods/edit)

PATCH/accounts/{account_id}/teamnet/virtual_networks/{virtual_network_id}

##### [Delete a virtual network](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/virtual_networks/methods/delete)

DELETE/accounts/{account_id}/teamnet/virtual_networks/{virtual_network_id}

#### Zero TrustNetworksSubnets

##### [List Subnets](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/subnets/methods/list)

GET/accounts/{account_id}/zerotrust/subnets

#### Zero TrustNetworksSubnetsWARP

##### [Create WARP IP subnet](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/subnets/subresources/warp/methods/create)

POST/accounts/{account_id}/zerotrust/subnets/warp

##### [Get WARP IP subnet](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/subnets/subresources/warp/methods/get)

GET/accounts/{account_id}/zerotrust/subnets/warp/{subnet_id}

##### [Update WARP IP subnet](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/subnets/subresources/warp/methods/edit)

PATCH/accounts/{account_id}/zerotrust/subnets/warp/{subnet_id}

##### [Delete WARP IP subnet](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/subnets/subresources/warp/methods/delete)

DELETE/accounts/{account_id}/zerotrust/subnets/warp/{subnet_id}

#### Zero TrustNetworksSubnetsCloudflare Source

##### [Update Cloudflare Source Subnet](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/subnets/subresources/cloudflare_source/methods/update)

PATCH/accounts/{account_id}/zerotrust/subnets/cloudflare_source/{address_family}

#### Zero TrustNetworksSubnetsInitial Resolved IP

##### [Get Initial Resolved IP Subnet](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/subnets/subresources/initial_resolved_ip/methods/get)

GET/accounts/{account_id}/zerotrust/subnets/initial_resolved_ip/{address_family}

##### [Update Initial Resolved IP Subnet](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/subnets/subresources/initial_resolved_ip/methods/update)

PUT/accounts/{account_id}/zerotrust/subnets/initial_resolved_ip/{address_family}

#### Zero TrustNetworksHostname Routes

##### [List hostname routes](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/hostname_routes/methods/list)

GET/accounts/{account_id}/zerotrust/routes/hostname

##### [Get hostname route](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/hostname_routes/methods/get)

GET/accounts/{account_id}/zerotrust/routes/hostname/{hostname_route_id}

##### [Create hostname route](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/hostname_routes/methods/create)

POST/accounts/{account_id}/zerotrust/routes/hostname

##### [Update hostname route](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/hostname_routes/methods/edit)

PATCH/accounts/{account_id}/zerotrust/routes/hostname/{hostname_route_id}

##### [Delete hostname route](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/hostname_routes/methods/delete)

DELETE/accounts/{account_id}/zerotrust/routes/hostname/{hostname_route_id}

#### Zero TrustRisk Scoring

##### [Get risk event/score information for a specific user](https://developers.cloudflare.com/api/resources/zero_trust/subresources/risk_scoring/methods/get)

GET/accounts/{account_id}/zt_risk_scoring/{user_id}

##### [Clear the risk score for a particular user](https://developers.cloudflare.com/api/resources/zero_trust/subresources/risk_scoring/methods/reset)

POST/accounts/{account_id}/zt_risk_scoring/{user_id}/reset

#### Zero TrustRisk ScoringBehaviours

##### [Get all behaviors and associated configuration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/risk_scoring/subresources/behaviours/methods/get)

GET/accounts/{account_id}/zt_risk_scoring/behaviors

##### [Update configuration for risk behaviors](https://developers.cloudflare.com/api/resources/zero_trust/subresources/risk_scoring/subresources/behaviours/methods/update)

PUT/accounts/{account_id}/zt_risk_scoring/behaviors

#### Zero TrustRisk ScoringSummary

##### [Get risk score info for all users in the account](https://developers.cloudflare.com/api/resources/zero_trust/subresources/risk_scoring/subresources/summary/methods/get)

GET/accounts/{account_id}/zt_risk_scoring/summary

#### Zero TrustRisk ScoringIntegrations

##### [List all risk score integrations for the account.](https://developers.cloudflare.com/api/resources/zero_trust/subresources/risk_scoring/subresources/integrations/methods/list)

GET/accounts/{account_id}/zt_risk_scoring/integrations

##### [Get risk score integration by id.](https://developers.cloudflare.com/api/resources/zero_trust/subresources/risk_scoring/subresources/integrations/methods/get)

GET/accounts/{account_id}/zt_risk_scoring/integrations/{integration_id}

##### [Create new risk score integration.](https://developers.cloudflare.com/api/resources/zero_trust/subresources/risk_scoring/subresources/integrations/methods/create)

POST/accounts/{account_id}/zt_risk_scoring/integrations

##### [Update a risk score integration.](https://developers.cloudflare.com/api/resources/zero_trust/subresources/risk_scoring/subresources/integrations/methods/update)

PUT/accounts/{account_id}/zt_risk_scoring/integrations/{integration_id}

##### [Delete a risk score integration.](https://developers.cloudflare.com/api/resources/zero_trust/subresources/risk_scoring/subresources/integrations/methods/delete)

DELETE/accounts/{account_id}/zt_risk_scoring/integrations/{integration_id}

#### Zero TrustRisk ScoringIntegrationsReferences

##### [Get risk score integration by reference id.](https://developers.cloudflare.com/api/resources/zero_trust/subresources/risk_scoring/subresources/integrations/subresources/references/methods/get)

GET/accounts/{account_id}/zt_risk_scoring/integrations/reference_id/{reference_id}

#### Zero TrustResource Library

#### Zero TrustResource LibraryApplications

##### [List applications](https://developers.cloudflare.com/api/resources/zero_trust/subresources/resource_library/subresources/applications/methods/list)

GET/accounts/{account_id}/resource-library/applications

##### [Get application](https://developers.cloudflare.com/api/resources/zero_trust/subresources/resource_library/subresources/applications/methods/get)

GET/accounts/{account_id}/resource-library/applications/{id}

##### [Create application](https://developers.cloudflare.com/api/resources/zero_trust/subresources/resource_library/subresources/applications/methods/create)

POST/accounts/{account_id}/resource-library/applications

##### [Update application](https://developers.cloudflare.com/api/resources/zero_trust/subresources/resource_library/subresources/applications/methods/update)

PATCH/accounts/{account_id}/resource-library/applications/{id}

##### [Delete application](https://developers.cloudflare.com/api/resources/zero_trust/subresources/resource_library/subresources/applications/methods/delete)

DELETE/accounts/{account_id}/resource-library/applications/{id}

#### Zero TrustResource LibraryCategories

##### [List application categories](https://developers.cloudflare.com/api/resources/zero_trust/subresources/resource_library/subresources/categories/methods/list)

GET/accounts/{account_id}/resource-library/categories

##### [Get application category](https://developers.cloudflare.com/api/resources/zero_trust/subresources/resource_library/subresources/categories/methods/get)

GET/accounts/{account_id}/resource-library/categories/{id}

#### Turnstile

#### TurnstileWidgets

##### [List Turnstile Widgets](https://developers.cloudflare.com/api/resources/turnstile/subresources/widgets/methods/list)

GET/accounts/{account_id}/challenges/widgets

##### [Turnstile Widget Details](https://developers.cloudflare.com/api/resources/turnstile/subresources/widgets/methods/get)

GET/accounts/{account_id}/challenges/widgets/{sitekey}

##### [Create a Turnstile Widget](https://developers.cloudflare.com/api/resources/turnstile/subresources/widgets/methods/create)

POST/accounts/{account_id}/challenges/widgets

##### [Update a Turnstile Widget](https://developers.cloudflare.com/api/resources/turnstile/subresources/widgets/methods/update)

PUT/accounts/{account_id}/challenges/widgets/{sitekey}

##### [Delete a Turnstile Widget](https://developers.cloudflare.com/api/resources/turnstile/subresources/widgets/methods/delete)

DELETE/accounts/{account_id}/challenges/widgets/{sitekey}

##### [Rotate Secret for a Turnstile Widget](https://developers.cloudflare.com/api/resources/turnstile/subresources/widgets/methods/rotate_secret)

POST/accounts/{account_id}/challenges/widgets/{sitekey}/rotate_secret

#### Connectivity

#### ConnectivityDirectory

#### ConnectivityDirectoryServices

##### [List Workers VPC connectivity services](https://developers.cloudflare.com/api/resources/connectivity/subresources/directory/subresources/services/methods/list)

GET/accounts/{account_id}/connectivity/directory/services

##### [Create Workers VPC connectivity service](https://developers.cloudflare.com/api/resources/connectivity/subresources/directory/subresources/services/methods/create)

POST/accounts/{account_id}/connectivity/directory/services

##### [Get Workers VPC connectivity service](https://developers.cloudflare.com/api/resources/connectivity/subresources/directory/subresources/services/methods/get)

GET/accounts/{account_id}/connectivity/directory/services/{service_id}

##### [Update Workers VPC connectivity service](https://developers.cloudflare.com/api/resources/connectivity/subresources/directory/subresources/services/methods/update)

PUT/accounts/{account_id}/connectivity/directory/services/{service_id}

##### [Delete Workers VPC connectivity service](https://developers.cloudflare.com/api/resources/connectivity/subresources/directory/subresources/services/methods/delete)

DELETE/accounts/{account_id}/connectivity/directory/services/{service_id}

#### Hyperdrive

#### HyperdriveConfigs

##### [List Hyperdrives](https://developers.cloudflare.com/api/resources/hyperdrive/subresources/configs/methods/list)

GET/accounts/{account_id}/hyperdrive/configs

##### [Get Hyperdrive](https://developers.cloudflare.com/api/resources/hyperdrive/subresources/configs/methods/get)

GET/accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}

##### [Create Hyperdrive](https://developers.cloudflare.com/api/resources/hyperdrive/subresources/configs/methods/create)

POST/accounts/{account_id}/hyperdrive/configs

##### [Replace Hyperdrive](https://developers.cloudflare.com/api/resources/hyperdrive/subresources/configs/methods/update)

PUT/accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}

##### [Update Hyperdrive](https://developers.cloudflare.com/api/resources/hyperdrive/subresources/configs/methods/edit)

PATCH/accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}

##### [Restart Hyperdrive](https://developers.cloudflare.com/api/resources/hyperdrive/subresources/configs/methods/restart)

POST/accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}/restart

##### [Delete Hyperdrive](https://developers.cloudflare.com/api/resources/hyperdrive/subresources/configs/methods/delete)

DELETE/accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}

#### RUM

#### RUMSite Info

##### [List Web Analytics sites](https://developers.cloudflare.com/api/resources/rum/subresources/site_info/methods/list)

GET/accounts/{account_id}/rum/site_info/list

##### [Get a Web Analytics site](https://developers.cloudflare.com/api/resources/rum/subresources/site_info/methods/get)

GET/accounts/{account_id}/rum/site_info/{site_id}

##### [Create a Web Analytics site](https://developers.cloudflare.com/api/resources/rum/subresources/site_info/methods/create)

POST/accounts/{account_id}/rum/site_info

##### [Update a Web Analytics site](https://developers.cloudflare.com/api/resources/rum/subresources/site_info/methods/update)

PUT/accounts/{account_id}/rum/site_info/{site_id}

##### [Delete a Web Analytics site](https://developers.cloudflare.com/api/resources/rum/subresources/site_info/methods/delete)

DELETE/accounts/{account_id}/rum/site_info/{site_id}

#### RUMRules

##### [List rules in Web Analytics ruleset](https://developers.cloudflare.com/api/resources/rum/subresources/rules/methods/list)

GET/accounts/{account_id}/rum/v2/{ruleset_id}/rules

##### [Create a Web Analytics rule](https://developers.cloudflare.com/api/resources/rum/subresources/rules/methods/create)

POST/accounts/{account_id}/rum/v2/{ruleset_id}/rule

##### [Update a Web Analytics rule](https://developers.cloudflare.com/api/resources/rum/subresources/rules/methods/update)

PUT/accounts/{account_id}/rum/v2/{ruleset_id}/rule/{rule_id}

##### [Delete a Web Analytics rule](https://developers.cloudflare.com/api/resources/rum/subresources/rules/methods/delete)

DELETE/accounts/{account_id}/rum/v2/{ruleset_id}/rule/{rule_id}

##### [Update Web Analytics rules](https://developers.cloudflare.com/api/resources/rum/subresources/rules/methods/bulk_create)

POST/accounts/{account_id}/rum/v2/{ruleset_id}/rules

#### Vectorize

#### VectorizeIndexes

##### [List Vectorize Indexes](https://developers.cloudflare.com/api/resources/vectorize/subresources/indexes/methods/list)

GET/accounts/{account_id}/vectorize/v2/indexes

##### [Get Vectorize Index](https://developers.cloudflare.com/api/resources/vectorize/subresources/indexes/methods/get)

GET/accounts/{account_id}/vectorize/v2/indexes/{index_name}

##### [Create Vectorize Index](https://developers.cloudflare.com/api/resources/vectorize/subresources/indexes/methods/create)

POST/accounts/{account_id}/vectorize/v2/indexes

##### [Delete Vectorize Index](https://developers.cloudflare.com/api/resources/vectorize/subresources/indexes/methods/delete)

DELETE/accounts/{account_id}/vectorize/v2/indexes/{index_name}

##### [Insert Vectors](https://developers.cloudflare.com/api/resources/vectorize/subresources/indexes/methods/insert)

POST/accounts/{account_id}/vectorize/v2/indexes/{index_name}/insert

##### [Query Vectors](https://developers.cloudflare.com/api/resources/vectorize/subresources/indexes/methods/query)

POST/accounts/{account_id}/vectorize/v2/indexes/{index_name}/query

##### [Upsert Vectors](https://developers.cloudflare.com/api/resources/vectorize/subresources/indexes/methods/upsert)

POST/accounts/{account_id}/vectorize/v2/indexes/{index_name}/upsert

##### [Delete Vectors By Identifier](https://developers.cloudflare.com/api/resources/vectorize/subresources/indexes/methods/delete_by_ids)

POST/accounts/{account_id}/vectorize/v2/indexes/{index_name}/delete_by_ids

##### [Get Vectors By Identifier](https://developers.cloudflare.com/api/resources/vectorize/subresources/indexes/methods/get_by_ids)

POST/accounts/{account_id}/vectorize/v2/indexes/{index_name}/get_by_ids

##### [Get Vectorize Index Info](https://developers.cloudflare.com/api/resources/vectorize/subresources/indexes/methods/info)

GET/accounts/{account_id}/vectorize/v2/indexes/{index_name}/info

##### [List Vectors](https://developers.cloudflare.com/api/resources/vectorize/subresources/indexes/methods/list_vectors)

GET/accounts/{account_id}/vectorize/v2/indexes/{index_name}/list

#### VectorizeIndexesMetadata Index

##### [List Metadata Indexes](https://developers.cloudflare.com/api/resources/vectorize/subresources/indexes/subresources/metadata_index/methods/list)

GET/accounts/{account_id}/vectorize/v2/indexes/{index_name}/metadata_index/list

##### [Create Metadata Index](https://developers.cloudflare.com/api/resources/vectorize/subresources/indexes/subresources/metadata_index/methods/create)

POST/accounts/{account_id}/vectorize/v2/indexes/{index_name}/metadata_index/create

##### [Delete Metadata Index](https://developers.cloudflare.com/api/resources/vectorize/subresources/indexes/subresources/metadata_index/methods/delete)

POST/accounts/{account_id}/vectorize/v2/indexes/{index_name}/metadata_index/delete

#### URL Scanner

#### URL ScannerResponses

##### [Get raw response](https://developers.cloudflare.com/api/resources/url_scanner/subresources/responses/methods/get)

GET/accounts/{account_id}/urlscanner/v2/responses/{response_id}

#### URL ScannerScans

##### [Search URL scans](https://developers.cloudflare.com/api/resources/url_scanner/subresources/scans/methods/list)

GET/accounts/{account_id}/urlscanner/v2/search

##### [Get URL scan](https://developers.cloudflare.com/api/resources/url_scanner/subresources/scans/methods/get)

GET/accounts/{account_id}/urlscanner/v2/result/{scan_id}

##### [Create URL Scan](https://developers.cloudflare.com/api/resources/url_scanner/subresources/scans/methods/create)

POST/accounts/{account_id}/urlscanner/v2/scan

##### [Bulk create URL Scans](https://developers.cloudflare.com/api/resources/url_scanner/subresources/scans/methods/bulk_create)

POST/accounts/{account_id}/urlscanner/v2/bulk

##### [Get URL scan's HAR](https://developers.cloudflare.com/api/resources/url_scanner/subresources/scans/methods/har)

GET/accounts/{account_id}/urlscanner/v2/har/{scan_id}

##### [Get screenshot](https://developers.cloudflare.com/api/resources/url_scanner/subresources/scans/methods/screenshot)

GET/accounts/{account_id}/urlscanner/v2/screenshots/{scan_id}.png

##### [Get URL scan's DOM](https://developers.cloudflare.com/api/resources/url_scanner/subresources/scans/methods/dom)

GET/accounts/{account_id}/urlscanner/v2/dom/{scan_id}

#### Vulnerability Scanner

#### Vulnerability ScannerCredential Sets

##### [List credential sets](https://developers.cloudflare.com/api/resources/vulnerability_scanner/subresources/credential_sets/methods/list)

GET/accounts/{account_id}/vuln_scanner/credential_sets

##### [Create credential set](https://developers.cloudflare.com/api/resources/vulnerability_scanner/subresources/credential_sets/methods/create)

POST/accounts/{account_id}/vuln_scanner/credential_sets

##### [Get credential set](https://developers.cloudflare.com/api/resources/vulnerability_scanner/subresources/credential_sets/methods/get)

GET/accounts/{account_id}/vuln_scanner/credential_sets/{credential_set_id}

##### [Update credential set](https://developers.cloudflare.com/api/resources/vulnerability_scanner/subresources/credential_sets/methods/update)

PUT/accounts/{account_id}/vuln_scanner/credential_sets/{credential_set_id}

##### [Edit credential set](https://developers.cloudflare.com/api/resources/vulnerability_scanner/subresources/credential_sets/methods/edit)

PATCH/accounts/{account_id}/vuln_scanner/credential_sets/{credential_set_id}

##### [Delete credential set](https://developers.cloudflare.com/api/resources/vulnerability_scanner/subresources/credential_sets/methods/delete)

DELETE/accounts/{account_id}/vuln_scanner/credential_sets/{credential_set_id}

#### Vulnerability ScannerCredential SetsCredentials

##### [List credentials](https://developers.cloudflare.com/api/resources/vulnerability_scanner/subresources/credential_sets/subresources/credentials/methods/list)

GET/accounts/{account_id}/vuln_scanner/credential_sets/{credential_set_id}/credentials

##### [Create credential](https://developers.cloudflare.com/api/resources/vulnerability_scanner/subresources/credential_sets/subresources/credentials/methods/create)

POST/accounts/{account_id}/vuln_scanner/credential_sets/{credential_set_id}/credentials

##### [Get credential](https://developers.cloudflare.com/api/resources/vulnerability_scanner/subresources/credential_sets/subresources/credentials/methods/get)

GET/accounts/{account_id}/vuln_scanner/credential_sets/{credential_set_id}/credentials/{credential_id}

##### [Update credential](https://developers.cloudflare.com/api/resources/vulnerability_scanner/subresources/credential_sets/subresources/credentials/methods/update)

PUT/accounts/{account_id}/vuln_scanner/credential_sets/{credential_set_id}/credentials/{credential_id}

##### [Edit credential](https://developers.cloudflare.com/api/resources/vulnerability_scanner/subresources/credential_sets/subresources/credentials/methods/edit)

PATCH/accounts/{account_id}/vuln_scanner/credential_sets/{credential_set_id}/credentials/{credential_id}

##### [Delete credential](https://developers.cloudflare.com/api/resources/vulnerability_scanner/subresources/credential_sets/subresources/credentials/methods/delete)

DELETE/accounts/{account_id}/vuln_scanner/credential_sets/{credential_set_id}/credentials/{credential_id}

#### Vulnerability ScannerScans

##### [List scans](https://developers.cloudflare.com/api/resources/vulnerability_scanner/subresources/scans/methods/list)

GET/accounts/{account_id}/vuln_scanner/scans

##### [Create scan](https://developers.cloudflare.com/api/resources/vulnerability_scanner/subresources/scans/methods/create)

POST/accounts/{account_id}/vuln_scanner/scans

##### [Get scan](https://developers.cloudflare.com/api/resources/vulnerability_scanner/subresources/scans/methods/get)

GET/accounts/{account_id}/vuln_scanner/scans/{scan_id}

#### Vulnerability ScannerTarget Environments

##### [List target environments](https://developers.cloudflare.com/api/resources/vulnerability_scanner/subresources/target_environments/methods/list)

GET/accounts/{account_id}/vuln_scanner/target_environments

##### [Create target environment](https://developers.cloudflare.com/api/resources/vulnerability_scanner/subresources/target_environments/methods/create)

POST/accounts/{account_id}/vuln_scanner/target_environments

##### [Get target environment](https://developers.cloudflare.com/api/resources/vulnerability_scanner/subresources/target_environments/methods/get)

GET/accounts/{account_id}/vuln_scanner/target_environments/{target_environment_id}

##### [Update target environment](https://developers.cloudflare.com/api/resources/vulnerability_scanner/subresources/target_environments/methods/update)

PUT/accounts/{account_id}/vuln_scanner/target_environments/{target_environment_id}

##### [Edit target environment](https://developers.cloudflare.com/api/resources/vulnerability_scanner/subresources/target_environments/methods/edit)

PATCH/accounts/{account_id}/vuln_scanner/target_environments/{target_environment_id}

##### [Delete target environment](https://developers.cloudflare.com/api/resources/vulnerability_scanner/subresources/target_environments/methods/delete)

DELETE/accounts/{account_id}/vuln_scanner/target_environments/{target_environment_id}

#### Radar

#### RadarAgent Readiness

##### [Get agent readiness summary](https://developers.cloudflare.com/api/resources/radar/subresources/agent_readiness/methods/summary)

GET/radar/agent_readiness/summary/{dimension}

#### RadarAI

#### RadarAITo Markdown

##### [Convert uploaded files to Markdown](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/to_markdown/methods/create)

Deprecated

POST/accounts/{account_id}/ai/tomarkdown

#### RadarAIInference

##### [Get Workers AI inference distribution by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/inference/methods/summary_v2)

GET/radar/ai/inference/summary/{dimension}

##### [Get time series distribution of Workers AI inference by dimension.](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/inference/methods/timeseries_groups_v2)

GET/radar/ai/inference/timeseries_groups/{dimension}

#### RadarAIInferenceSummary

##### [Get Workers AI models summary](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/inference/subresources/summary/methods/model)

Deprecated

GET/radar/ai/inference/summary/model

##### [Get Workers AI tasks summary](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/inference/subresources/summary/methods/task)

Deprecated

GET/radar/ai/inference/summary/task

#### RadarAIInferenceTimeseries Groups

#### RadarAIInferenceTimeseries GroupsSummary

##### [Get Workers AI models time series](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/inference/subresources/timeseries_groups/subresources/summary/methods/model)

Deprecated

GET/radar/ai/inference/timeseries_groups/model

##### [Get Workers AI tasks time series](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/inference/subresources/timeseries_groups/subresources/summary/methods/task)

Deprecated

GET/radar/ai/inference/timeseries_groups/task

#### RadarAIBots

##### [Get AI bots HTTP requests distribution by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/bots/methods/summary_v2)

GET/radar/ai/bots/summary/{dimension}

##### [Get AI bots HTTP requests time series](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/bots/methods/timeseries)

GET/radar/ai/bots/timeseries

##### [Get time series distribution of AI bots HTTP requests by dimension.](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/bots/methods/timeseries_groups)

GET/radar/ai/bots/timeseries_groups/{dimension}

#### RadarAIBotsSummary

##### [Get AI user agents summary](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/bots/subresources/summary/methods/user_agent)

Deprecated

GET/radar/ai/bots/summary/user_agent

#### RadarAITimeseries Groups

##### [Get AI user agents time series](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/timeseries_groups/methods/user_agent)

Deprecated

GET/radar/ai/bots/timeseries_groups/user_agent

##### [Get AI bots HTTP requests distribution by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/timeseries_groups/methods/summary)

Deprecated

GET/radar/ai/bots/summary/{dimension}

##### [Get AI bots HTTP requests time series](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/timeseries_groups/methods/timeseries)

Deprecated

GET/radar/ai/bots/timeseries

##### [Get time series distribution of AI bots HTTP requests by dimension.](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/timeseries_groups/methods/timeseries_groups)

Deprecated

GET/radar/ai/bots/timeseries_groups/{dimension}

#### RadarAIMarkdown For Agents

##### [Get AI markdown for agents reduction ratio summary](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/markdown_for_agents/methods/summary)

GET/radar/ai/markdown_for_agents/summary

##### [Get AI markdown for agents reduction ratio time series](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/markdown_for_agents/methods/timeseries)

GET/radar/ai/markdown_for_agents/timeseries

#### RadarCT

##### [Get certificate distribution by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/ct/methods/summary)

GET/radar/ct/summary/{dimension}

##### [Get certificates time series](https://developers.cloudflare.com/api/resources/radar/subresources/ct/methods/timeseries)

GET/radar/ct/timeseries

##### [Get time series of certificate distribution by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/ct/methods/timeseries_groups)

GET/radar/ct/timeseries_groups/{dimension}

#### RadarCTAuthorities

##### [Get certificate authority details](https://developers.cloudflare.com/api/resources/radar/subresources/ct/subresources/authorities/methods/get)

GET/radar/ct/authorities/{ca_slug}

##### [List certificate authorities](https://developers.cloudflare.com/api/resources/radar/subresources/ct/subresources/authorities/methods/list)

GET/radar/ct/authorities

#### RadarCTLogs

##### [Get certificate log details](https://developers.cloudflare.com/api/resources/radar/subresources/ct/subresources/logs/methods/get)

GET/radar/ct/logs/{log_slug}

##### [List certificate logs](https://developers.cloudflare.com/api/resources/radar/subresources/ct/subresources/logs/methods/list)

GET/radar/ct/logs

#### RadarAnnotations

##### [Get latest annotations](https://developers.cloudflare.com/api/resources/radar/subresources/annotations/methods/list)

GET/radar/annotations

#### RadarAnnotationsOutages

##### [Get latest Internet outages and anomalies](https://developers.cloudflare.com/api/resources/radar/subresources/annotations/subresources/outages/methods/get)

GET/radar/annotations/outages

##### [Get the number of outages by location](https://developers.cloudflare.com/api/resources/radar/subresources/annotations/subresources/outages/methods/locations)

GET/radar/annotations/outages/locations

#### RadarBGP

##### [Get BGP time series](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/methods/timeseries)

GET/radar/bgp/timeseries

#### RadarBGPLeaks

#### RadarBGPLeaksEvents

##### [Get BGP route leak events](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/leaks/subresources/events/methods/list)

GET/radar/bgp/leaks/events

#### RadarBGPTop

##### [Get top prefixes by BGP updates](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/top/methods/prefixes)

GET/radar/bgp/top/prefixes

#### RadarBGPTopAses

##### [Get top ASes by BGP updates](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/top/subresources/ases/methods/get)

GET/radar/bgp/top/ases

##### [Get top ASes by prefix count](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/top/subresources/ases/methods/prefixes)

GET/radar/bgp/top/ases/prefixes

#### RadarBGPHijacks

#### RadarBGPHijacksEvents

##### [Get BGP hijack events](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/hijacks/subresources/events/methods/list)

GET/radar/bgp/hijacks/events

#### RadarBGPRoutes

##### [Get Multi-Origin AS (MOAS) prefixes](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/methods/moas)

GET/radar/bgp/routes/moas

##### [Get prefix-to-ASN mapping](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/methods/pfx2as)

GET/radar/bgp/routes/pfx2as

##### [Get BGP routing table stats ](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/methods/stats)

GET/radar/bgp/routes/stats

##### [List ASes from global routing tables](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/methods/ases)

GET/radar/bgp/routes/ases

##### [Get real-time BGP routes for a prefix](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/methods/realtime)

GET/radar/bgp/routes/realtime

#### RadarBGPRoutesUpstreams

##### [Get upstream composition time series for an AS](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/subresources/upstreams/methods/timeseries)

GET/radar/bgp/routes/upstreams/{asn}/timeseries

#### RadarBGPRoutesPaths

##### [Get tier-1 path segments for an AS](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/subresources/paths/methods/list)

GET/radar/bgp/routes/paths/{asn}

#### RadarBGPIPs

##### [Get announced IP address space time series](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/ips/methods/timeseries)

GET/radar/bgp/ips/timeseries

#### RadarBGPIPsTop

##### [Get top ASes by announced IP space](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/ips/subresources/top/methods/ases)

GET/radar/bgp/ips/top/ases

#### RadarBGPRPKI

#### RadarBGPRPKIASPA

##### [Get ASPA objects snapshot](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/snapshot)

GET/radar/bgp/rpki/aspa/snapshot

##### [Get ASPA changes over time](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/changes)

GET/radar/bgp/rpki/aspa/changes

##### [Get ASPA count time series](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/timeseries)

GET/radar/bgp/rpki/aspa/timeseries

#### RadarBGPRPKIRoas

##### [Get RPKI ROA deployment time series](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/roas/methods/timeseries)

GET/radar/bgp/rpki/roas/timeseries

#### RadarBots

##### [List bots](https://developers.cloudflare.com/api/resources/radar/subresources/bots/methods/list)

GET/radar/bots

##### [Get bot details](https://developers.cloudflare.com/api/resources/radar/subresources/bots/methods/get)

GET/radar/bots/{bot_slug}

##### [Get bots HTTP requests distribution by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/bots/methods/summary)

GET/radar/bots/summary/{dimension}

##### [Get bots HTTP requests time series](https://developers.cloudflare.com/api/resources/radar/subresources/bots/methods/timeseries)

GET/radar/bots/timeseries

##### [Get time series distribution of bots HTTP requests by dimension.](https://developers.cloudflare.com/api/resources/radar/subresources/bots/methods/timeseries_groups)

GET/radar/bots/timeseries_groups/{dimension}

#### RadarBotsWeb Crawlers

##### [Get crawler HTTP request distribution by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/bots/subresources/web_crawlers/methods/summary)

GET/radar/bots/crawlers/summary/{dimension}

##### [Get time series of crawler HTTP request distribution by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/bots/subresources/web_crawlers/methods/timeseries_groups)

GET/radar/bots/crawlers/timeseries_groups/{dimension}

#### RadarDatasets

##### [List datasets](https://developers.cloudflare.com/api/resources/radar/subresources/datasets/methods/list)

GET/radar/datasets

##### [Get dataset CSV stream](https://developers.cloudflare.com/api/resources/radar/subresources/datasets/methods/get)

GET/radar/datasets/{alias}

##### [Get dataset download URL](https://developers.cloudflare.com/api/resources/radar/subresources/datasets/methods/download)

POST/radar/datasets/download

#### RadarDNS

##### [Get DNS summary by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/dns/methods/summary_v2)

GET/radar/dns/summary/{dimension}

##### [Get DNS queries time series](https://developers.cloudflare.com/api/resources/radar/subresources/dns/methods/timeseries)

GET/radar/dns/timeseries

##### [Get DNS time series grouped by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/dns/methods/timeseries_groups_v2)

GET/radar/dns/timeseries_groups/{dimension}

#### RadarDNSTop

##### [Get top ASes by DNS queries](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/top/methods/ases)

GET/radar/dns/top/ases

##### [Get top locations by DNS queries](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/top/methods/locations)

GET/radar/dns/top/locations

#### RadarDNSSummary

##### [Get DNS queries by cache status summary](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/summary/methods/cache_hit)

Deprecated

GET/radar/dns/summary/cache_hit

##### [Get DNS queries by DNSSEC support summary](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/summary/methods/dnssec)

Deprecated

GET/radar/dns/summary/dnssec

##### [Get DNS queries by DNSSEC awareness summary](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/summary/methods/dnssec_aware)

Deprecated

GET/radar/dns/summary/dnssec_aware

##### [Get DNS queries by DNSSEC end-to-end summary](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/summary/methods/dnssec_e2e)

Deprecated

GET/radar/dns/summary/dnssec_e2e

##### [Get DNS queries by IP version summary](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/summary/methods/ip_version)

Deprecated

GET/radar/dns/summary/ip_version

##### [Get DNS queries by matching answer summary](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/summary/methods/matching_answer)

Deprecated

GET/radar/dns/summary/matching_answer

##### [Get DNS queries by protocol summary](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/summary/methods/protocol)

Deprecated

GET/radar/dns/summary/protocol

##### [Get DNS queries by type summary](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/summary/methods/query_type)

Deprecated

GET/radar/dns/summary/query_type

##### [Get DNS queries by response code summary](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/summary/methods/response_code)

Deprecated

GET/radar/dns/summary/response_code

##### [Get DNS queries by response TTL summary](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/summary/methods/response_ttl)

Deprecated

GET/radar/dns/summary/response_ttl

#### RadarDNSTimeseries Groups

##### [Get DNS queries by cache status time series](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/timeseries_groups/methods/cache_hit)

Deprecated

GET/radar/dns/timeseries_groups/cache_hit

##### [Get DNS queries by DNSSEC support time series](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/timeseries_groups/methods/dnssec)

Deprecated

GET/radar/dns/timeseries_groups/dnssec

##### [Get DNS queries by DNSSEC awareness time series](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/timeseries_groups/methods/dnssec_aware)

Deprecated

GET/radar/dns/timeseries_groups/dnssec_aware

##### [Get DNS queries by DNSSEC end-to-end time series](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/timeseries_groups/methods/dnssec_e2e)

Deprecated

GET/radar/dns/timeseries_groups/dnssec_e2e

##### [Get DNS queries by IP version time series](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/timeseries_groups/methods/ip_version)

Deprecated

GET/radar/dns/timeseries_groups/ip_version

##### [Get DNS queries by matching answer time series](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/timeseries_groups/methods/matching_answer)

Deprecated

GET/radar/dns/timeseries_groups/matching_answer

##### [Get DNS queries by protocol time series](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/timeseries_groups/methods/protocol)

Deprecated

GET/radar/dns/timeseries_groups/protocol

##### [Get DNS queries by type time series](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/timeseries_groups/methods/query_type)

Deprecated

GET/radar/dns/timeseries_groups/query_type

##### [Get DNS queries by response code time series](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/timeseries_groups/methods/response_code)

Deprecated

GET/radar/dns/timeseries_groups/response_code

##### [Get DNS queries by response TTL time series](https://developers.cloudflare.com/api/resources/radar/subresources/dns/subresources/timeseries_groups/methods/response_ttl)

Deprecated

GET/radar/dns/timeseries_groups/response_ttl

#### RadarNetFlows

##### [Get network traffic time series](https://developers.cloudflare.com/api/resources/radar/subresources/netflows/methods/timeseries)

GET/radar/netflows/timeseries

##### [Get network traffic summary](https://developers.cloudflare.com/api/resources/radar/subresources/netflows/methods/summary)

Deprecated

GET/radar/netflows/summary

##### [Get network traffic distribution by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/netflows/methods/summary_v2)

GET/radar/netflows/summary/{dimension}

##### [Get time series distribution of network traffic by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/netflows/methods/timeseries_groups)

GET/radar/netflows/timeseries_groups/{dimension}

#### RadarNetFlowsTop

##### [Get top ASes by network traffic](https://developers.cloudflare.com/api/resources/radar/subresources/netflows/subresources/top/methods/ases)

GET/radar/netflows/top/ases

##### [Get top locations by network traffic](https://developers.cloudflare.com/api/resources/radar/subresources/netflows/subresources/top/methods/locations)

GET/radar/netflows/top/locations

#### RadarPost Quantum

#### RadarPost QuantumOrigin

##### [Get Origin Post-Quantum Data Summary](https://developers.cloudflare.com/api/resources/radar/subresources/post_quantum/subresources/origin/methods/summary)

GET/radar/post_quantum/origin/summary/{dimension}

##### [Get Origin Post-Quantum Data Over Time](https://developers.cloudflare.com/api/resources/radar/subresources/post_quantum/subresources/origin/methods/timeseries_groups)

GET/radar/post_quantum/origin/timeseries_groups/{dimension}

#### RadarPost QuantumTLS

##### [Check Post-Quantum TLS support](https://developers.cloudflare.com/api/resources/radar/subresources/post_quantum/subresources/tls/methods/support)

GET/radar/post_quantum/tls/support

#### RadarSearch

##### [Search for locations, ASes, reports, and more](https://developers.cloudflare.com/api/resources/radar/subresources/search/methods/global)

GET/radar/search/global

#### RadarVerified Bots

#### RadarVerified BotsTop

##### [Get top verified bots by HTTP requests](https://developers.cloudflare.com/api/resources/radar/subresources/verified_bots/subresources/top/methods/bots)

Deprecated

GET/radar/verified_bots/top/bots

##### [Get top verified bot categories by HTTP requests](https://developers.cloudflare.com/api/resources/radar/subresources/verified_bots/subresources/top/methods/categories)

Deprecated

GET/radar/verified_bots/top/categories

#### RadarAS112

##### [Get AS112 DNS queries time series](https://developers.cloudflare.com/api/resources/radar/subresources/as112/methods/timeseries)

GET/radar/as112/timeseries

##### [Get AS112 summary by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/as112/methods/summary_v2)

GET/radar/as112/summary/{dimension}

##### [Get AS112 time series grouped by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/as112/methods/timeseries_groups_v2)

GET/radar/as112/timeseries_groups/{dimension}

#### RadarAS112Summary

##### [Get AS112 DNS queries by DNSSEC summary](https://developers.cloudflare.com/api/resources/radar/subresources/as112/subresources/summary/methods/dnssec)

Deprecated

GET/radar/as112/summary/dnssec

##### [Get AS112 DNS queries by EDNS summary](https://developers.cloudflare.com/api/resources/radar/subresources/as112/subresources/summary/methods/edns)

Deprecated

GET/radar/as112/summary/edns

##### [Get AS112 DNS queries by IP version summary](https://developers.cloudflare.com/api/resources/radar/subresources/as112/subresources/summary/methods/ip_version)

Deprecated

GET/radar/as112/summary/ip_version

##### [Get AS112 DNS queries by DNS protocol summary](https://developers.cloudflare.com/api/resources/radar/subresources/as112/subresources/summary/methods/protocol)

Deprecated

GET/radar/as112/summary/protocol

##### [Get AS112 DNS queries by type summary](https://developers.cloudflare.com/api/resources/radar/subresources/as112/subresources/summary/methods/query_type)

Deprecated

GET/radar/as112/summary/query_type

##### [Get AS112 DNS queries by response code summary](https://developers.cloudflare.com/api/resources/radar/subresources/as112/subresources/summary/methods/response_codes)

Deprecated

GET/radar/as112/summary/response_codes

#### RadarAS112Timeseries Groups

##### [Get AS112 DNS queries by DNS protocol time series](https://developers.cloudflare.com/api/resources/radar/subresources/as112/subresources/timeseries_groups/methods/protocol)

Deprecated

GET/radar/as112/timeseries_groups/protocol

##### [Get AS112 DNS queries by type time series](https://developers.cloudflare.com/api/resources/radar/subresources/as112/subresources/timeseries_groups/methods/query_type)

Deprecated

GET/radar/as112/timeseries_groups/query_type

##### [Get AS112 DNS queries by response code time series](https://developers.cloudflare.com/api/resources/radar/subresources/as112/subresources/timeseries_groups/methods/response_codes)

Deprecated

GET/radar/as112/timeseries_groups/response_codes

##### [Get AS112 DNS queries by DNSSEC support time series](https://developers.cloudflare.com/api/resources/radar/subresources/as112/subresources/timeseries_groups/methods/dnssec)

Deprecated

GET/radar/as112/timeseries_groups/dnssec

##### [Get AS112 DNS queries by EDNS support summary](https://developers.cloudflare.com/api/resources/radar/subresources/as112/subresources/timeseries_groups/methods/edns)

Deprecated

GET/radar/as112/timeseries_groups/edns

##### [Get AS112 DNS queries by IP version time series](https://developers.cloudflare.com/api/resources/radar/subresources/as112/subresources/timeseries_groups/methods/ip_version)

Deprecated

GET/radar/as112/timeseries_groups/ip_version

#### RadarAS112Top

##### [Get top locations by AS112 DNS queries](https://developers.cloudflare.com/api/resources/radar/subresources/as112/subresources/top/methods/locations)

GET/radar/as112/top/locations

##### [Get top locations by AS112 DNS queries with DNSSEC support](https://developers.cloudflare.com/api/resources/radar/subresources/as112/subresources/top/methods/dnssec)

GET/radar/as112/top/locations/dnssec/{dnssec}

##### [Get top locations by AS112 DNS queries with EDNS support](https://developers.cloudflare.com/api/resources/radar/subresources/as112/subresources/top/methods/edns)

GET/radar/as112/top/locations/edns/{edns}

##### [Get top locations by AS112 DNS queries for an IP version](https://developers.cloudflare.com/api/resources/radar/subresources/as112/subresources/top/methods/ip_version)

GET/radar/as112/top/locations/ip_version/{ip_version}

#### RadarEmail

#### RadarEmailRouting

##### [Get email routing summary by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/routing/methods/summary_v2)

GET/radar/email/routing/summary/{dimension}

##### [Get email routing time series grouped by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/routing/methods/timeseries_groups_v2)

GET/radar/email/routing/timeseries_groups/{dimension}

#### RadarEmailRoutingSummary

##### [Get email ARC validation summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/routing/subresources/summary/methods/arc)

Deprecated

GET/radar/email/routing/summary/arc

##### [Get email DKIM validation summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/routing/subresources/summary/methods/dkim)

Deprecated

GET/radar/email/routing/summary/dkim

##### [Get email DMARC validation summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/routing/subresources/summary/methods/dmarc)

Deprecated

GET/radar/email/routing/summary/dmarc

##### [Get email encryption status summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/routing/subresources/summary/methods/encrypted)

Deprecated

GET/radar/email/routing/summary/encrypted

##### [Get email IP version summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/routing/subresources/summary/methods/ip_version)

Deprecated

GET/radar/email/routing/summary/ip_version

##### [Get email SPF validation summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/routing/subresources/summary/methods/spf)

Deprecated

GET/radar/email/routing/summary/spf

#### RadarEmailRoutingTimeseries Groups

##### [Get email ARC validation time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/routing/subresources/timeseries_groups/methods/arc)

Deprecated

GET/radar/email/routing/timeseries_groups/arc

##### [Get email DKIM validation time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/routing/subresources/timeseries_groups/methods/dkim)

Deprecated

GET/radar/email/routing/timeseries_groups/dkim

##### [Get email DMARC validation time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/routing/subresources/timeseries_groups/methods/dmarc)

Deprecated

GET/radar/email/routing/timeseries_groups/dmarc

##### [Get email encryption status time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/routing/subresources/timeseries_groups/methods/encrypted)

Deprecated

GET/radar/email/routing/timeseries_groups/encrypted

##### [Get email IP version time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/routing/subresources/timeseries_groups/methods/ip_version)

Deprecated

GET/radar/email/routing/timeseries_groups/ip_version

##### [Get email SPF validation time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/routing/subresources/timeseries_groups/methods/spf)

Deprecated

GET/radar/email/routing/timeseries_groups/spf

#### RadarEmailSecurity

##### [Get email security summary by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/methods/summary_v2)

GET/radar/email/security/summary/{dimension}

##### [Get email security time series grouped by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/methods/timeseries_groups_v2)

GET/radar/email/security/timeseries_groups/{dimension}

#### RadarEmailSecurityTop

#### RadarEmailSecurityTopTLDs

##### [Get top TLDs by email message volume](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/top/subresources/tlds/methods/get)

GET/radar/email/security/top/tlds

#### RadarEmailSecurityTopTLDsMalicious

##### [Get top TLDs by email malicious classification](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/top/subresources/tlds/subresources/malicious/methods/get)

GET/radar/email/security/top/tlds/malicious/{malicious}

#### RadarEmailSecurityTopTLDsSpam

##### [Get top TLDs by email spam classification](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/top/subresources/tlds/subresources/spam/methods/get)

GET/radar/email/security/top/tlds/spam/{spam}

#### RadarEmailSecurityTopTLDsSpoof

##### [Get top TLDs by email spoof classification](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/top/subresources/tlds/subresources/spoof/methods/get)

GET/radar/email/security/top/tlds/spoof/{spoof}

#### RadarEmailSecuritySummary

##### [Get email ARC validation summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/summary/methods/arc)

Deprecated

GET/radar/email/security/summary/arc

##### [Get email DKIM validation summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/summary/methods/dkim)

Deprecated

GET/radar/email/security/summary/dkim

##### [Get email DMARC validation summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/summary/methods/dmarc)

Deprecated

GET/radar/email/security/summary/dmarc

##### [Get email malicious classification summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/summary/methods/malicious)

Deprecated

GET/radar/email/security/summary/malicious

##### [Get email spam classification summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/summary/methods/spam)

Deprecated

GET/radar/email/security/summary/spam

##### [Get email SPF validation summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/summary/methods/spf)

Deprecated

GET/radar/email/security/summary/spf

##### [Get email threat category summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/summary/methods/threat_category)

Deprecated

GET/radar/email/security/summary/threat_category

##### [Get email spoof classification summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/summary/methods/spoof)

Deprecated

GET/radar/email/security/summary/spoof

##### [Get email TLS version summary](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/summary/methods/tls_version)

Deprecated

GET/radar/email/security/summary/tls_version

#### RadarEmailSecurityTimeseries Groups

##### [Get email ARC validation time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/timeseries_groups/methods/arc)

Deprecated

GET/radar/email/security/timeseries_groups/arc

##### [Get email DKIM validation time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/timeseries_groups/methods/dkim)

Deprecated

GET/radar/email/security/timeseries_groups/dkim

##### [Get email DMARC validation time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/timeseries_groups/methods/dmarc)

Deprecated

GET/radar/email/security/timeseries_groups/dmarc

##### [Get email malicious classification time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/timeseries_groups/methods/malicious)

Deprecated

GET/radar/email/security/timeseries_groups/malicious

##### [Get email spam classification time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/timeseries_groups/methods/spam)

Deprecated

GET/radar/email/security/timeseries_groups/spam

##### [Get email SPF validation time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/timeseries_groups/methods/spf)

Deprecated

GET/radar/email/security/timeseries_groups/spf

##### [Get email threat category time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/timeseries_groups/methods/threat_category)

Deprecated

GET/radar/email/security/timeseries_groups/threat_category

##### [Get email spoof classification time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/timeseries_groups/methods/spoof)

Deprecated

GET/radar/email/security/timeseries_groups/spoof

##### [Get email TLS version time series](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/subresources/timeseries_groups/methods/tls_version)

Deprecated

GET/radar/email/security/timeseries_groups/tls_version

#### RadarAttacks

#### RadarAttacksLayer3

##### [Get layer 3 attacks summary by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/methods/summary_v2)

GET/radar/attacks/layer3/summary/{dimension}

##### [Get layer 3 attacks by bytes time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/methods/timeseries)

GET/radar/attacks/layer3/timeseries

##### [Get layer 3 attacks time series grouped by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/methods/timeseries_groups_v2)

GET/radar/attacks/layer3/timeseries_groups/{dimension}

#### RadarAttacksLayer3Summary

##### [Get layer 3 attacks by bitrate summary](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/summary/methods/bitrate)

Deprecated

GET/radar/attacks/layer3/summary/bitrate

##### [Get layer 3 attacks by duration summary](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/summary/methods/duration)

Deprecated

GET/radar/attacks/layer3/summary/duration

##### [Get layer 3 attacks by IP version summary](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/summary/methods/ip_version)

Deprecated

GET/radar/attacks/layer3/summary/ip_version

##### [Get layer 3 attacks by protocol summary](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/summary/methods/protocol)

Deprecated

GET/radar/attacks/layer3/summary/protocol

##### [Get layer 3 attacks by vector summary](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/summary/methods/vector)

Deprecated

GET/radar/attacks/layer3/summary/vector

##### [Get layer 3 attacks by targeted industry summary](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/summary/methods/industry)

Deprecated

GET/radar/attacks/layer3/summary/industry

##### [Get layer 3 attacks by targeted vertical summary](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/summary/methods/vertical)

Deprecated

GET/radar/attacks/layer3/summary/vertical

#### RadarAttacksLayer3Timeseries Groups

##### [Get layer 3 attacks by target industries time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/timeseries_groups/methods/industry)

Deprecated

GET/radar/attacks/layer3/timeseries_groups/industry

##### [Get layer 3 attacks by IP version time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/timeseries_groups/methods/ip_version)

Deprecated

GET/radar/attacks/layer3/timeseries_groups/ip_version

##### [Get layer 3 attacks by protocol time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/timeseries_groups/methods/protocol)

Deprecated

GET/radar/attacks/layer3/timeseries_groups/protocol

##### [Get layer 3 attacks by vector time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/timeseries_groups/methods/vector)

Deprecated

GET/radar/attacks/layer3/timeseries_groups/vector

##### [Get layer 3 attacks by vertical time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/timeseries_groups/methods/vertical)

Deprecated

GET/radar/attacks/layer3/timeseries_groups/vertical

##### [Get layer 3 attacks by bitrate time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/timeseries_groups/methods/bitrate)

Deprecated

GET/radar/attacks/layer3/timeseries_groups/bitrate

##### [Get layer 3 attacks by duration time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/timeseries_groups/methods/duration)

Deprecated

GET/radar/attacks/layer3/timeseries_groups/duration

#### RadarAttacksLayer3Top

##### [Get top layer 3 attack pairs (origin and target locations)](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/top/methods/attacks)

GET/radar/attacks/layer3/top/attacks

##### [Get top industries targeted by layer 3 attacks](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/top/methods/industry)

Deprecated

GET/radar/attacks/layer3/top/industry

##### [Get top verticals targeted by layer 3 attacks](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/top/methods/vertical)

Deprecated

GET/radar/attacks/layer3/top/vertical

#### RadarAttacksLayer3TopLocations

##### [Get top origin locations of layer 3 attacks](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/top/subresources/locations/methods/origin)

GET/radar/attacks/layer3/top/locations/origin

##### [Get top target locations of layer 3 attacks](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer3/subresources/top/subresources/locations/methods/target)

GET/radar/attacks/layer3/top/locations/target

#### RadarAttacksLayer7

##### [Get layer 7 attacks summary by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/methods/summary_v2)

GET/radar/attacks/layer7/summary/{dimension}

##### [Get layer 7 attacks time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/methods/timeseries)

GET/radar/attacks/layer7/timeseries

##### [Get layer 7 attacks time series grouped by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/methods/timeseries_groups_v2)

GET/radar/attacks/layer7/timeseries_groups/{dimension}

#### RadarAttacksLayer7Summary

##### [Get layer 7 attacks by IP version summary](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/summary/methods/ip_version)

Deprecated

GET/radar/attacks/layer7/summary/ip_version

##### [Get layer 7 attacks by HTTP method summary](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/summary/methods/http_method)

Deprecated

GET/radar/attacks/layer7/summary/http_method

##### [Get layer 7 attacks by HTTP version summary](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/summary/methods/http_version)

Deprecated

GET/radar/attacks/layer7/summary/http_version

##### [Get layer 7 attacks by managed rules summary](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/summary/methods/managed_rules)

Deprecated

GET/radar/attacks/layer7/summary/managed_rules

##### [Get layer 7 attacks by mitigation product summary](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/summary/methods/mitigation_product)

Deprecated

GET/radar/attacks/layer7/summary/mitigation_product

##### [Get layer 7 attacks by targeted industry summary](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/summary/methods/industry)

Deprecated

GET/radar/attacks/layer7/summary/industry

##### [Get layer 7 attacks by targeted vertical summary](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/summary/methods/vertical)

Deprecated

GET/radar/attacks/layer7/summary/vertical

#### RadarAttacksLayer7Timeseries Groups

##### [Get layer 7 attacks by target industries time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/timeseries_groups/methods/industry)

Deprecated

GET/radar/attacks/layer7/timeseries_groups/industry

##### [Get layer 7 attacks by IP version time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/timeseries_groups/methods/ip_version)

Deprecated

GET/radar/attacks/layer7/timeseries_groups/ip_version

##### [Get layer 7 attacks by vertical time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/timeseries_groups/methods/vertical)

Deprecated

GET/radar/attacks/layer7/timeseries_groups/vertical

##### [Get layer 7 attacks by HTTP method time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/timeseries_groups/methods/http_method)

Deprecated

GET/radar/attacks/layer7/timeseries_groups/http_method

##### [Get layer 7 attacks by HTTP version time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/timeseries_groups/methods/http_version)

Deprecated

GET/radar/attacks/layer7/timeseries_groups/http_version

##### [Get layer 7 attacks by managed rules time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/timeseries_groups/methods/managed_rules)

Deprecated

GET/radar/attacks/layer7/timeseries_groups/managed_rules

##### [Get layer 7 attacks by mitigation product time series](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/timeseries_groups/methods/mitigation_product)

Deprecated

GET/radar/attacks/layer7/timeseries_groups/mitigation_product

#### RadarAttacksLayer7Top

##### [Get top layer 7 attack pairs (origin and target locations)](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/top/methods/attacks)

GET/radar/attacks/layer7/top/attacks

##### [Get top industries targeted by layer 7 attacks](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/top/methods/industry)

Deprecated

GET/radar/attacks/layer7/top/industry

##### [Get top verticals targeted by layer 7 attacks](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/top/methods/vertical)

Deprecated

GET/radar/attacks/layer7/top/vertical

#### RadarAttacksLayer7TopLocations

##### [Get top origin locations of layer 7 attacks](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/top/subresources/locations/methods/origin)

GET/radar/attacks/layer7/top/locations/origin

##### [Get top target locations of layer 7 attacks](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/top/subresources/locations/methods/target)

GET/radar/attacks/layer7/top/locations/target

#### RadarAttacksLayer7TopAses

##### [Get top origin ASes of layer 7 attacks](https://developers.cloudflare.com/api/resources/radar/subresources/attacks/subresources/layer7/subresources/top/subresources/ases/methods/origin)

GET/radar/attacks/layer7/top/ases/origin

#### RadarEntities

##### [Get IP address details](https://developers.cloudflare.com/api/resources/radar/subresources/entities/methods/get)

GET/radar/entities/ip

#### RadarEntitiesASNs

##### [List autonomous systems](https://developers.cloudflare.com/api/resources/radar/subresources/entities/subresources/asns/methods/list)

GET/radar/entities/asns

##### [Get AS details by ASN](https://developers.cloudflare.com/api/resources/radar/subresources/entities/subresources/asns/methods/get)

GET/radar/entities/asns/{asn}

##### [Get AS-level relationships by ASN](https://developers.cloudflare.com/api/resources/radar/subresources/entities/subresources/asns/methods/rel)

GET/radar/entities/asns/{asn}/rel

##### [Get IRR AS-SETs that an AS is a member of](https://developers.cloudflare.com/api/resources/radar/subresources/entities/subresources/asns/methods/as_set)

GET/radar/entities/asns/{asn}/as_set

##### [Get AS details by IP address](https://developers.cloudflare.com/api/resources/radar/subresources/entities/subresources/asns/methods/ip)

GET/radar/entities/asns/ip

##### [Get AS rankings by botnet threat feed activity](https://developers.cloudflare.com/api/resources/radar/subresources/entities/subresources/asns/methods/botnet_threat_feed)

GET/radar/entities/asns/botnet_threat_feed

#### RadarEntitiesLocations

##### [List locations](https://developers.cloudflare.com/api/resources/radar/subresources/entities/subresources/locations/methods/list)

GET/radar/entities/locations

##### [Get location details](https://developers.cloudflare.com/api/resources/radar/subresources/entities/subresources/locations/methods/get)

GET/radar/entities/locations/{location}

#### RadarGeolocations

##### [List Geolocations](https://developers.cloudflare.com/api/resources/radar/subresources/geolocations/methods/list)

GET/radar/geolocations

##### [Get Geolocation details](https://developers.cloudflare.com/api/resources/radar/subresources/geolocations/methods/get)

GET/radar/geolocations/{geo_id}

#### RadarHTTP

##### [Get HTTP requests summary by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/http/methods/summary_v2)

GET/radar/http/summary/{dimension}

##### [Get HTTP requests time series](https://developers.cloudflare.com/api/resources/radar/subresources/http/methods/timeseries)

GET/radar/http/timeseries

##### [Get HTTP requests time series grouped by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/http/methods/timeseries_groups_v2)

GET/radar/http/timeseries_groups/{dimension}

#### RadarHTTPLocations

##### [Get top locations by HTTP requests](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/locations/methods/get)

GET/radar/http/top/locations

#### RadarHTTPLocationsBot Class

##### [Get top locations by HTTP requests for a bot class](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/locations/subresources/bot_class/methods/get)

GET/radar/http/top/locations/bot_class/{bot_class}

#### RadarHTTPLocationsDevice Type

##### [Get top locations by HTTP requests for a device type](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/locations/subresources/device_type/methods/get)

GET/radar/http/top/locations/device_type/{device_type}

#### RadarHTTPLocationsHTTP Protocol

##### [Get top locations by HTTP requests for an HTTP protocol](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/locations/subresources/http_protocol/methods/get)

GET/radar/http/top/locations/http_protocol/{http_protocol}

#### RadarHTTPLocationsHTTP Method

##### [Get top locations by HTTP requests for an HTTP version](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/locations/subresources/http_method/methods/get)

GET/radar/http/top/locations/http_version/{http_version}

#### RadarHTTPLocationsIP Version

##### [Get top locations by HTTP requests for an IP version](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/locations/subresources/ip_version/methods/get)

GET/radar/http/top/locations/ip_version/{ip_version}

#### RadarHTTPLocationsOS

##### [Get top locations by HTTP requests for an OS](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/locations/subresources/os/methods/get)

GET/radar/http/top/locations/os/{os}

#### RadarHTTPLocationsTLS Version

##### [Get top locations by HTTP requests for a TLS version](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/locations/subresources/tls_version/methods/get)

GET/radar/http/top/locations/tls_version/{tls_version}

#### RadarHTTPLocationsBrowser Family

##### [Get top locations by HTTP requests for a browser family](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/locations/subresources/browser_family/methods/get)

GET/radar/http/top/locations/browser_family/{browser_family}

#### RadarHTTPAses

##### [Get top ASes by HTTP requests](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/ases/methods/get)

GET/radar/http/top/ases

#### RadarHTTPAsesBot Class

##### [Get top ASes by HTTP requests for a bot class](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/ases/subresources/bot_class/methods/get)

GET/radar/http/top/ases/bot_class/{bot_class}

#### RadarHTTPAsesDevice Type

##### [Get top ASes by HTTP requests for a device type](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/ases/subresources/device_type/methods/get)

GET/radar/http/top/ases/device_type/{device_type}

#### RadarHTTPAsesHTTP Protocol

##### [Get top ASes by HTTP requests for an HTTP protocol](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/ases/subresources/http_protocol/methods/get)

GET/radar/http/top/ases/http_protocol/{http_protocol}

#### RadarHTTPAsesHTTP Method

##### [Get top ASes by HTTP requests for an HTTP version](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/ases/subresources/http_method/methods/get)

GET/radar/http/top/ases/http_version/{http_version}

#### RadarHTTPAsesIP Version

##### [Get top ASes by HTTP requests for an IP version](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/ases/subresources/ip_version/methods/get)

GET/radar/http/top/ases/ip_version/{ip_version}

#### RadarHTTPAsesOS

##### [Get top ASes by HTTP requests for an OS](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/ases/subresources/os/methods/get)

GET/radar/http/top/ases/os/{os}

#### RadarHTTPAsesTLS Version

##### [Get top ASes by HTTP requests for a TLS version](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/ases/subresources/tls_version/methods/get)

GET/radar/http/top/ases/tls_version/{tls_version}

#### RadarHTTPAsesBrowser Family

##### [Get top ASes by HTTP requests for a browser family](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/ases/subresources/browser_family/methods/get)

GET/radar/http/top/ases/browser_family/{browser_family}

#### RadarHTTPSummary

##### [Get HTTP requests by bot class summary](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/summary/methods/bot_class)

Deprecated

GET/radar/http/summary/bot_class

##### [Get HTTP requests by device type summary](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/summary/methods/device_type)

Deprecated

GET/radar/http/summary/device_type

##### [Get HTTP requests by HTTP/HTTPS summary](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/summary/methods/http_protocol)

Deprecated

GET/radar/http/summary/http_protocol

##### [Get HTTP requests by HTTP version summary](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/summary/methods/http_version)

Deprecated

GET/radar/http/summary/http_version

##### [Get HTTP requests by IP version summary](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/summary/methods/ip_version)

Deprecated

GET/radar/http/summary/ip_version

##### [Get HTTP requests by OS summary](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/summary/methods/os)

Deprecated

GET/radar/http/summary/os

##### [Get HTTP requests by TLS version summary](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/summary/methods/tls_version)

Deprecated

GET/radar/http/summary/tls_version

##### [Get HTTP requests by post-quantum support summary](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/summary/methods/post_quantum)

Deprecated

GET/radar/http/summary/post_quantum

#### RadarHTTPTimeseries Groups

##### [Get HTTP requests by TLS version time series](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/timeseries_groups/methods/tls_version)

Deprecated

GET/radar/http/timeseries_groups/tls_version

##### [Get HTTP requests by bot class time series](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/timeseries_groups/methods/bot_class)

Deprecated

GET/radar/http/timeseries_groups/bot_class

##### [Get HTTP requests by user agent time series](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/timeseries_groups/methods/browser)

Deprecated

GET/radar/http/timeseries_groups/browser

##### [Get HTTP requests by user agent family time series](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/timeseries_groups/methods/browser_family)

Deprecated

GET/radar/http/timeseries_groups/browser_family

##### [Get HTTP requests by device type time series](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/timeseries_groups/methods/device_type)

Deprecated

GET/radar/http/timeseries_groups/device_type

##### [Get HTTP requests by HTTP/HTTPS time series](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/timeseries_groups/methods/http_protocol)

Deprecated

GET/radar/http/timeseries_groups/http_protocol

##### [Get HTTP requests by HTTP version time series](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/timeseries_groups/methods/http_version)

Deprecated

GET/radar/http/timeseries_groups/http_version

##### [Get HTTP requests by IP version time series](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/timeseries_groups/methods/ip_version)

Deprecated

GET/radar/http/timeseries_groups/ip_version

##### [Get HTTP requests by OS time series](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/timeseries_groups/methods/os)

Deprecated

GET/radar/http/timeseries_groups/os

##### [Get HTTP requests by post-quantum support time series](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/timeseries_groups/methods/post_quantum)

Deprecated

GET/radar/http/timeseries_groups/post_quantum

#### RadarHTTPTop

##### [Get top user agents by HTTP requests](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/top/methods/browser)

Deprecated

GET/radar/http/top/browser

##### [Get top user agent families by HTTP requests](https://developers.cloudflare.com/api/resources/radar/subresources/http/subresources/top/methods/browser_family)

Deprecated

GET/radar/http/top/browser_family

#### RadarOrigins

##### [List Origins](https://developers.cloudflare.com/api/resources/radar/subresources/origins/methods/list)

GET/radar/origins

##### [Get Origin details](https://developers.cloudflare.com/api/resources/radar/subresources/origins/methods/get)

GET/radar/origins/{slug}

##### [Get origin metrics time series](https://developers.cloudflare.com/api/resources/radar/subresources/origins/methods/timeseries)

GET/radar/origins/timeseries

##### [Get origin metrics distribution by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/origins/methods/summary)

GET/radar/origins/summary/{dimension}

##### [Get origin metrics time series grouped by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/origins/methods/timeseries_groups)

GET/radar/origins/timeseries_groups/{dimension}

#### RadarQuality

#### RadarQualityIQI

##### [Get Internet Quality Index (IQI) summary](https://developers.cloudflare.com/api/resources/radar/subresources/quality/subresources/iqi/methods/summary)

GET/radar/quality/iqi/summary

##### [Get Internet Quality Index (IQI) time series](https://developers.cloudflare.com/api/resources/radar/subresources/quality/subresources/iqi/methods/timeseries_groups)

GET/radar/quality/iqi/timeseries_groups

#### RadarQualitySpeed

##### [Get speed tests summary](https://developers.cloudflare.com/api/resources/radar/subresources/quality/subresources/speed/methods/summary)

GET/radar/quality/speed/summary

##### [Get speed tests histogram](https://developers.cloudflare.com/api/resources/radar/subresources/quality/subresources/speed/methods/histogram)

GET/radar/quality/speed/histogram

#### RadarQualitySpeedTop

##### [Get top ASes by speed test results](https://developers.cloudflare.com/api/resources/radar/subresources/quality/subresources/speed/subresources/top/methods/ases)

GET/radar/quality/speed/top/ases

##### [Get top locations by speed test results](https://developers.cloudflare.com/api/resources/radar/subresources/quality/subresources/speed/subresources/top/methods/locations)

GET/radar/quality/speed/top/locations

#### RadarRanking

##### [Get domains rank time series](https://developers.cloudflare.com/api/resources/radar/subresources/ranking/methods/timeseries_groups)

GET/radar/ranking/timeseries_groups

##### [Get top or trending domains](https://developers.cloudflare.com/api/resources/radar/subresources/ranking/methods/top)

GET/radar/ranking/top

#### RadarRankingDomain

##### [Get domain rank details](https://developers.cloudflare.com/api/resources/radar/subresources/ranking/subresources/domain/methods/get)

GET/radar/ranking/domain/{domain}

#### RadarRankingInternet Services

##### [Get Internet services rank time series](https://developers.cloudflare.com/api/resources/radar/subresources/ranking/subresources/internet_services/methods/timeseries_groups)

GET/radar/ranking/internet_services/timeseries_groups

##### [Get top Internet services](https://developers.cloudflare.com/api/resources/radar/subresources/ranking/subresources/internet_services/methods/top)

GET/radar/ranking/internet_services/top

##### [List Internet services categories](https://developers.cloudflare.com/api/resources/radar/subresources/ranking/subresources/internet_services/methods/categories)

GET/radar/ranking/internet_services/categories

#### RadarTraffic Anomalies

##### [Get latest Internet traffic anomalies](https://developers.cloudflare.com/api/resources/radar/subresources/traffic_anomalies/methods/get)

GET/radar/traffic_anomalies

#### RadarTraffic AnomaliesLocations

##### [Get top locations by total traffic anomalies](https://developers.cloudflare.com/api/resources/radar/subresources/traffic_anomalies/subresources/locations/methods/get)

GET/radar/traffic_anomalies/locations

#### RadarTCP Resets Timeouts

##### [Get TCP resets and timeouts summary](https://developers.cloudflare.com/api/resources/radar/subresources/tcp_resets_timeouts/methods/summary)

GET/radar/tcp_resets_timeouts/summary

##### [Get TCP resets and timeouts time series](https://developers.cloudflare.com/api/resources/radar/subresources/tcp_resets_timeouts/methods/timeseries_groups)

GET/radar/tcp_resets_timeouts/timeseries_groups

#### RadarTLDs

##### [List TLDs](https://developers.cloudflare.com/api/resources/radar/subresources/tlds/methods/list)

GET/radar/tlds

##### [Get TLD details](https://developers.cloudflare.com/api/resources/radar/subresources/tlds/methods/get)

GET/radar/tlds/{tld}

#### RadarTLDsPerformance

##### [Get TLD Performance Summary](https://developers.cloudflare.com/api/resources/radar/subresources/tlds/subresources/performance/methods/summary)

GET/radar/tlds/performance/summary/{dimension}

##### [Get TLD Performance Over Time](https://developers.cloudflare.com/api/resources/radar/subresources/tlds/subresources/performance/methods/timeseries_groups)

GET/radar/tlds/performance/timeseries_groups/{dimension}

#### RadarRobots TXT

#### RadarRobots TXTTop

##### [Get top domain categories by robots.txt files parsed](https://developers.cloudflare.com/api/resources/radar/subresources/robots_txt/subresources/top/methods/domain_categories)

GET/radar/robots_txt/top/domain_categories

#### RadarRobots TXTTopUser Agents

##### [Get top user agents on robots.txt files](https://developers.cloudflare.com/api/resources/radar/subresources/robots_txt/subresources/top/subresources/user_agents/methods/directive)

GET/radar/robots_txt/top/user_agents/directive

#### RadarLeaked Credentials

##### [Get HTTP authentication requests distribution by dimension](https://developers.cloudflare.com/api/resources/radar/subresources/leaked_credentials/methods/summary_v2)

GET/radar/leaked_credential_checks/summary/{dimension}

##### [Get time series distribution of HTTP authentication requests by dimension.](https://developers.cloudflare.com/api/resources/radar/subresources/leaked_credentials/methods/timeseries_groups_v2)

GET/radar/leaked_credential_checks/timeseries_groups/{dimension}

#### RadarLeaked CredentialsSummary

##### [Get HTTP authentication requests by bot class summary](https://developers.cloudflare.com/api/resources/radar/subresources/leaked_credentials/subresources/summary/methods/bot_class)

Deprecated

GET/radar/leaked_credential_checks/summary/bot_class

##### [Get HTTP authentication requests by compromised credential status summary](https://developers.cloudflare.com/api/resources/radar/subresources/leaked_credentials/subresources/summary/methods/compromised)

Deprecated

GET/radar/leaked_credential_checks/summary/compromised

#### RadarLeaked CredentialsTimeseries Groups

##### [Get HTTP authentication requests by bot class time series](https://developers.cloudflare.com/api/resources/radar/subresources/leaked_credentials/subresources/timeseries_groups/methods/bot_class)

Deprecated

GET/radar/leaked_credential_checks/timeseries_groups/bot_class

##### [Get HTTP authentication requests by compromised credential status time series](https://developers.cloudflare.com/api/resources/radar/subresources/leaked_credentials/subresources/timeseries_groups/methods/compromised)

Deprecated

GET/radar/leaked_credential_checks/timeseries_groups/compromised

#### Bot Management

##### [Get Zone Bot Management Config](https://developers.cloudflare.com/api/resources/bot_management/methods/get)

GET/zones/{zone_id}/bot_management

##### [Update Zone Bot Management Config](https://developers.cloudflare.com/api/resources/bot_management/methods/update)

PUT/zones/{zone_id}/bot_management

#### Bot ManagementFeedback

##### [List zone feedback reports](https://developers.cloudflare.com/api/resources/bot_management/subresources/feedback/methods/list)

GET/zones/{zone_id}/bot_management/feedback

##### [Submit a feedback report](https://developers.cloudflare.com/api/resources/bot_management/subresources/feedback/methods/create)

POST/zones/{zone_id}/bot_management/feedback

#### Fraud

##### [Get Fraud Detection Settings](https://developers.cloudflare.com/api/resources/fraud/methods/get)

GET/zones/{zone_id}/fraud_detection/settings

##### [Update Fraud Detection Settings](https://developers.cloudflare.com/api/resources/fraud/methods/update)

PUT/zones/{zone_id}/fraud_detection/settings

#### Precursor

##### [Get Zone Precursor Config](https://developers.cloudflare.com/api/resources/precursor/methods/get)

GET/zones/{zone_id}/precursor

##### [Update Zone Precursor Config](https://developers.cloudflare.com/api/resources/precursor/methods/update)

PUT/zones/{zone_id}/precursor

#### Origin Post Quantum Encryption

##### [Get Origin Post-Quantum Encryption setting](https://developers.cloudflare.com/api/resources/origin_post_quantum_encryption/methods/get)

Deprecated

GET/zones/{zone_id}/cache/origin_post_quantum_encryption

##### [Change Origin Post-Quantum Encryption setting](https://developers.cloudflare.com/api/resources/origin_post_quantum_encryption/methods/update)

Deprecated

PUT/zones/{zone_id}/cache/origin_post_quantum_encryption

#### Origin TLS Compliance Modes

##### [Get Origin TLS Compliance Modes setting](https://developers.cloudflare.com/api/resources/origin_tls_compliance_modes/methods/get)

GET/zones/{zone_id}/settings/origin_tls_compliance_modes

##### [Replace Origin TLS Compliance Modes setting](https://developers.cloudflare.com/api/resources/origin_tls_compliance_modes/methods/update)

PUT/zones/{zone_id}/settings/origin_tls_compliance_modes

##### [Change Origin TLS Compliance Modes setting](https://developers.cloudflare.com/api/resources/origin_tls_compliance_modes/methods/edit)

PATCH/zones/{zone_id}/settings/origin_tls_compliance_modes

##### [Delete Origin TLS Compliance Modes setting](https://developers.cloudflare.com/api/resources/origin_tls_compliance_modes/methods/delete)

DELETE/zones/{zone_id}/settings/origin_tls_compliance_modes

#### Google Tag Gateway

#### Google Tag GatewayConfig

##### [Get Google Tag Gateway configuration](https://developers.cloudflare.com/api/resources/google_tag_gateway/subresources/config/methods/get)

GET/zones/{zone_id}/settings/google-tag-gateway/config

##### [Update Google Tag Gateway configuration](https://developers.cloudflare.com/api/resources/google_tag_gateway/subresources/config/methods/update)

PUT/zones/{zone_id}/settings/google-tag-gateway/config

#### Zaraz

##### [Update Zaraz workflow](https://developers.cloudflare.com/api/resources/zaraz/methods/update)

PUT/zones/{zone_id}/settings/zaraz/workflow

#### ZarazConfig

##### [Get Zaraz configuration](https://developers.cloudflare.com/api/resources/zaraz/subresources/config/methods/get)

GET/zones/{zone_id}/settings/zaraz/config

##### [Update Zaraz configuration](https://developers.cloudflare.com/api/resources/zaraz/subresources/config/methods/update)

PUT/zones/{zone_id}/settings/zaraz/config

#### ZarazDefault

##### [Get default Zaraz configuration](https://developers.cloudflare.com/api/resources/zaraz/subresources/default/methods/get)

GET/zones/{zone_id}/settings/zaraz/default

#### ZarazExport

##### [Export Zaraz configuration](https://developers.cloudflare.com/api/resources/zaraz/subresources/export/methods/get)

GET/zones/{zone_id}/settings/zaraz/export

#### ZarazHistory

##### [List Zaraz historical configuration records](https://developers.cloudflare.com/api/resources/zaraz/subresources/history/methods/list)

GET/zones/{zone_id}/settings/zaraz/history

##### [Restore Zaraz historical configuration by ID](https://developers.cloudflare.com/api/resources/zaraz/subresources/history/methods/update)

PUT/zones/{zone_id}/settings/zaraz/history

#### ZarazHistoryConfigs

##### [Get Zaraz historical configurations by ID(s)](https://developers.cloudflare.com/api/resources/zaraz/subresources/history/subresources/configs/methods/get)

GET/zones/{zone_id}/settings/zaraz/history/configs

#### ZarazPublish

##### [Publish Zaraz preview configuration](https://developers.cloudflare.com/api/resources/zaraz/subresources/publish/methods/create)

POST/zones/{zone_id}/settings/zaraz/publish

#### ZarazWorkflow

##### [Get Zaraz workflow](https://developers.cloudflare.com/api/resources/zaraz/subresources/workflow/methods/get)

GET/zones/{zone_id}/settings/zaraz/workflow

#### Speed

#### SpeedSchedule

##### [Get a page test schedule](https://developers.cloudflare.com/api/resources/speed/subresources/schedule/methods/get)

GET/zones/{zone_id}/speed_api/schedule/{url}

##### [Create scheduled page test](https://developers.cloudflare.com/api/resources/speed/subresources/schedule/methods/create)

POST/zones/{zone_id}/speed_api/schedule/{url}

##### [Delete scheduled page test](https://developers.cloudflare.com/api/resources/speed/subresources/schedule/methods/delete)

DELETE/zones/{zone_id}/speed_api/schedule/{url}

#### SpeedAvailabilities

##### [Get quota and availability](https://developers.cloudflare.com/api/resources/speed/subresources/availabilities/methods/list)

GET/zones/{zone_id}/speed_api/availabilities

#### SpeedPages

##### [List tested webpages](https://developers.cloudflare.com/api/resources/speed/subresources/pages/methods/list)

GET/zones/{zone_id}/speed_api/pages

##### [List core web vital metrics trend](https://developers.cloudflare.com/api/resources/speed/subresources/pages/methods/trend)

GET/zones/{zone_id}/speed_api/pages/{url}/trend

#### SpeedPagesTests

##### [List page test history](https://developers.cloudflare.com/api/resources/speed/subresources/pages/subresources/tests/methods/list)

GET/zones/{zone_id}/speed_api/pages/{url}/tests

##### [Get a page test result](https://developers.cloudflare.com/api/resources/speed/subresources/pages/subresources/tests/methods/get)

GET/zones/{zone_id}/speed_api/pages/{url}/tests/{test_id}

##### [Start page test](https://developers.cloudflare.com/api/resources/speed/subresources/pages/subresources/tests/methods/create)

POST/zones/{zone_id}/speed_api/pages/{url}/tests

##### [Delete all page tests](https://developers.cloudflare.com/api/resources/speed/subresources/pages/subresources/tests/methods/delete)

DELETE/zones/{zone_id}/speed_api/pages/{url}/tests

#### DCV Delegation

##### [Retrieve the DCV Delegation unique identifier.](https://developers.cloudflare.com/api/resources/dcv_delegation/methods/get)

GET/zones/{zone_id}/dcv_delegation/uuid

#### Hostnames

#### HostnamesSettings

#### HostnamesSettingsTLS

##### [List TLS setting for hostnames](https://developers.cloudflare.com/api/resources/hostnames/subresources/settings/subresources/tls/methods/list)

GET/zones/{zone_id}/hostnames/settings/{setting_id}

##### [Get TLS setting for hostname](https://developers.cloudflare.com/api/resources/hostnames/subresources/settings/subresources/tls/methods/get)

GET/zones/{zone_id}/hostnames/settings/{setting_id}/{hostname}

##### [Edit TLS setting for hostname](https://developers.cloudflare.com/api/resources/hostnames/subresources/settings/subresources/tls/methods/update)

PUT/zones/{zone_id}/hostnames/settings/{setting_id}/{hostname}

##### [Delete TLS setting for hostname](https://developers.cloudflare.com/api/resources/hostnames/subresources/settings/subresources/tls/methods/delete)

DELETE/zones/{zone_id}/hostnames/settings/{setting_id}/{hostname}

#### Snippets

##### [List zone snippets](https://developers.cloudflare.com/api/resources/snippets/methods/list)

GET/zones/{zone_id}/snippets

##### [Get a zone snippet](https://developers.cloudflare.com/api/resources/snippets/methods/get)

GET/zones/{zone_id}/snippets/{snippet_name}

##### [Update a zone snippet](https://developers.cloudflare.com/api/resources/snippets/methods/update)

PUT/zones/{zone_id}/snippets/{snippet_name}

##### [Delete a zone snippet](https://developers.cloudflare.com/api/resources/snippets/methods/delete)

DELETE/zones/{zone_id}/snippets/{snippet_name}

#### SnippetsContent

##### [Get a zone snippet content](https://developers.cloudflare.com/api/resources/snippets/subresources/content/methods/get)

GET/zones/{zone_id}/snippets/{snippet_name}/content

#### SnippetsRules

##### [List zone snippet rules](https://developers.cloudflare.com/api/resources/snippets/subresources/rules/methods/get)

GET/zones/{zone_id}/snippets/snippet_rules

##### [List zone snippet rules](https://developers.cloudflare.com/api/resources/snippets/subresources/rules/methods/list)

GET/zones/{zone_id}/snippets/snippet_rules

##### [Update zone snippet rules](https://developers.cloudflare.com/api/resources/snippets/subresources/rules/methods/update)

PUT/zones/{zone_id}/snippets/snippet_rules

##### [Delete zone snippet rules](https://developers.cloudflare.com/api/resources/snippets/subresources/rules/methods/delete)

DELETE/zones/{zone_id}/snippets/snippet_rules

#### Realtime Kit

#### Realtime KitApps

##### [Fetch all apps](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/apps/methods/get)

GET/accounts/{account_id}/realtime/kit/apps

##### [Create App](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/apps/methods/post)

POST/accounts/{account_id}/realtime/kit/apps

#### Realtime KitMeetings

##### [Fetch all meetings for an App](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/get)

GET/accounts/{account_id}/realtime/kit/{app_id}/meetings

##### [Create a meeting](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/create)

POST/accounts/{account_id}/realtime/kit/{app_id}/meetings

##### [Fetch a meeting for an App](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/get_meeting_by_id)

GET/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}

##### [Update a meeting](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/update_meeting_by_id)

PATCH/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}

##### [Replace a meeting](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/replace_meeting_by_id)

PUT/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}

##### [Fetch all participants of a meeting](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/get_meeting_participants)

GET/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants

##### [Add a participant](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/add_participant)

POST/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants

##### [Fetch a participant's detail](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/get_meeting_participant)

GET/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants/{participant_id}

##### [Edit a participant's detail](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/edit_participant)

PATCH/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants/{participant_id}

##### [Delete a participant](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/delete_meeting_participant)

DELETE/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants/{participant_id}

##### [Refresh participant's authentication token](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/refresh_participant_token)

POST/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants/{participant_id}/token

#### Realtime KitPresets

##### [Fetch all presets](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/presets/methods/get)

GET/accounts/{account_id}/realtime/kit/{app_id}/presets

##### [Create a preset](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/presets/methods/create)

POST/accounts/{account_id}/realtime/kit/{app_id}/presets

##### [Fetch details of a preset](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/presets/methods/get_preset_by_id)

GET/accounts/{account_id}/realtime/kit/{app_id}/presets/{preset_id}

##### [Delete a preset](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/presets/methods/delete)

DELETE/accounts/{account_id}/realtime/kit/{app_id}/presets/{preset_id}

##### [Update a preset](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/presets/methods/update)

PATCH/accounts/{account_id}/realtime/kit/{app_id}/presets/{preset_id}

##### [Replace a preset](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/presets/methods/replace_preset_by_id)

PUT/accounts/{account_id}/realtime/kit/{app_id}/presets/{preset_id}

#### Realtime KitSessions

##### [Fetch all sessions of an App](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/get_sessions)

GET/accounts/{account_id}/realtime/kit/{app_id}/sessions

##### [Fetch details of a session](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/get_session_details)

GET/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}

##### [Fetch participants list of a session](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/get_session_participants)

GET/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/participants

##### [Fetch details of a participant](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/get_session_participant_details)

GET/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/participants/{participant_id}

##### [Fetch all chat messages of a session](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/get_session_chat)

GET/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/chat

##### [Fetch the complete transcript for a session](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/get_session_transcripts)

GET/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/transcript

##### [Fetch summary of transcripts for a session](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/get_session_summary)

GET/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/summary

##### [Generate summary of Transcripts for the session](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/generate_summary_of_transcripts)

POST/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/summary

##### [Fetch details of peer](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/get_participant_data_from_peer_id)

GET/accounts/{account_id}/realtime/kit/{app_id}/sessions/peer-report/{peer_id}

#### Realtime KitRecordings

##### [Fetch all recordings for an App](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/get_recordings)

GET/accounts/{account_id}/realtime/kit/{app_id}/recordings

##### [Start recording a meeting](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/start_recordings)

POST/accounts/{account_id}/realtime/kit/{app_id}/recordings

##### [Fetch active recording](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/get_active_recordings)

GET/accounts/{account_id}/realtime/kit/{app_id}/recordings/active-recording/{meeting_id}

##### [Fetch details of a recording](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/get_one_recording)

GET/accounts/{account_id}/realtime/kit/{app_id}/recordings/{recording_id}

##### [Pause/Resume/Stop recording](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/pause_resume_stop_recording)

PUT/accounts/{account_id}/realtime/kit/{app_id}/recordings/{recording_id}

##### [Start recording participant audio tracks](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/start_track_recording)

POST/accounts/{account_id}/realtime/kit/{app_id}/recordings/track

#### Realtime KitWebhooks

##### [Fetch all webhooks details](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/webhooks/methods/get_webhooks)

GET/accounts/{account_id}/realtime/kit/{app_id}/webhooks

##### [Add a webhook](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/webhooks/methods/create_webhook)

POST/accounts/{account_id}/realtime/kit/{app_id}/webhooks

##### [Fetch details of a webhook](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/webhooks/methods/get_webhook_by_id)

GET/accounts/{account_id}/realtime/kit/{app_id}/webhooks/{webhook_id}

##### [Replace a webhook](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/webhooks/methods/replace_webhook)

PUT/accounts/{account_id}/realtime/kit/{app_id}/webhooks/{webhook_id}

##### [Edit a webhook](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/webhooks/methods/edit_webhook)

PATCH/accounts/{account_id}/realtime/kit/{app_id}/webhooks/{webhook_id}

##### [Delete a webhook](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/webhooks/methods/delete_webhook)

DELETE/accounts/{account_id}/realtime/kit/{app_id}/webhooks/{webhook_id}

#### Realtime KitActive Session

##### [Fetch details of an active session](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/active-session/methods/get_active_session)

GET/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-session

##### [Kick participants from an active session](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/active-session/methods/kick_participants)

POST/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-session/kick

##### [Kick all participants](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/active-session/methods/kick_all_participants)

POST/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-session/kick-all

##### [Create a poll](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/active-session/methods/create_poll)

POST/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-session/poll

#### Realtime KitLivestreams

##### [Fetch all livestreams](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/livestreams/methods/get_all_livestreams)

GET/accounts/{account_id}/realtime/kit/{app_id}/livestreams

##### [Stop livestreaming a meeting](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/livestreams/methods/stop_livestreaming_a_meeting)

POST/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-livestream/stop

##### [Start livestreaming a meeting](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/livestreams/methods/start_livestreaming_a_meeting)

POST/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/livestreams

##### [Fetch complete analytics data for your livestreams](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/livestreams/methods/get_livestream_analytics_complete)

GET/accounts/{account_id}/realtime/kit/{app_id}/analytics/livestreams/overall

##### [Fetch day-wise analytics data for your livestreams](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/livestreams/methods/get_livestream_analytics_daywise)

GET/accounts/{account_id}/realtime/kit/{app_id}/analytics/livestreams/daywise

##### [Fetch day-wise session and recording analytics data for an App](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/livestreams/methods/get_org_analytics)

GET/accounts/{account_id}/realtime/kit/{app_id}/analytics/daywise

##### [Fetch active livestreams for a meeting](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/livestreams/methods/get_meeting_active_livestreams)

GET/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-livestream

##### [Fetch livestream session details using livestream session ID](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/livestreams/methods/get_livestream_session_details_for_session_id)

GET/accounts/{account_id}/realtime/kit/{app_id}/livestreams/sessions/{livestream-session-id}

##### [Fetch active livestream session details](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/livestreams/methods/get_active_livestreams_for_livestream_id)

GET/accounts/{account_id}/realtime/kit/{app_id}/livestreams/{livestream_id}/active-livestream-session

##### [Fetch livestream details using livestream ID](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/livestreams/methods/get_livestream_session_for_livestream_id)

GET/accounts/{account_id}/realtime/kit/{app_id}/livestreams/{livestream_id}

#### Realtime KitAnalytics

##### [Fetch day-wise session and recording analytics data for an App](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/analytics/methods/get_org_analytics)

GET/accounts/{account_id}/realtime/kit/{app_id}/analytics/daywise

#### Calls

#### CallsSFU

##### [List apps](https://developers.cloudflare.com/api/resources/calls/subresources/sfu/methods/list)

GET/accounts/{account_id}/calls/apps

##### [Retrieve SFU app details](https://developers.cloudflare.com/api/resources/calls/subresources/sfu/methods/get)

GET/accounts/{account_id}/calls/apps/{app_id}

##### [Create an SFU app](https://developers.cloudflare.com/api/resources/calls/subresources/sfu/methods/create)

POST/accounts/{account_id}/calls/apps

##### [Update SFU app details](https://developers.cloudflare.com/api/resources/calls/subresources/sfu/methods/update)

PUT/accounts/{account_id}/calls/apps/{app_id}

##### [Delete an SFU app](https://developers.cloudflare.com/api/resources/calls/subresources/sfu/methods/delete)

DELETE/accounts/{account_id}/calls/apps/{app_id}

#### CallsTURN

##### [List TURN keys](https://developers.cloudflare.com/api/resources/calls/subresources/turn/methods/list)

GET/accounts/{account_id}/calls/turn_keys

##### [Retrieve TURN key details](https://developers.cloudflare.com/api/resources/calls/subresources/turn/methods/get)

GET/accounts/{account_id}/calls/turn_keys/{key_id}

##### [Create a TURN key](https://developers.cloudflare.com/api/resources/calls/subresources/turn/methods/create)

POST/accounts/{account_id}/calls/turn_keys

##### [Update TURN key details](https://developers.cloudflare.com/api/resources/calls/subresources/turn/methods/update)

PUT/accounts/{account_id}/calls/turn_keys/{key_id}

##### [Delete TURN key](https://developers.cloudflare.com/api/resources/calls/subresources/turn/methods/delete)

DELETE/accounts/{account_id}/calls/turn_keys/{key_id}

#### MoQ

#### MoQRelays

##### [List relays](https://developers.cloudflare.com/api/resources/moq/subresources/relays/methods/list)

GET/accounts/{account_id}/moq/relays

##### [Get a relay](https://developers.cloudflare.com/api/resources/moq/subresources/relays/methods/get)

GET/accounts/{account_id}/moq/relays/{relay_id}

##### [Create a relay](https://developers.cloudflare.com/api/resources/moq/subresources/relays/methods/create)

POST/accounts/{account_id}/moq/relays

##### [Update a relay](https://developers.cloudflare.com/api/resources/moq/subresources/relays/methods/update)

PUT/accounts/{account_id}/moq/relays/{relay_id}

##### [Delete a relay](https://developers.cloudflare.com/api/resources/moq/subresources/relays/methods/delete)

DELETE/accounts/{account_id}/moq/relays/{relay_id}

#### MoQRelaysTokens

##### [Create a token](https://developers.cloudflare.com/api/resources/moq/subresources/relays/subresources/tokens/methods/create)

POST/accounts/{account_id}/moq/relays/{relay_id}/tokens

##### [List tokens](https://developers.cloudflare.com/api/resources/moq/subresources/relays/subresources/tokens/methods/list)

GET/accounts/{account_id}/moq/relays/{relay_id}/tokens

##### [Revoke a token](https://developers.cloudflare.com/api/resources/moq/subresources/relays/subresources/tokens/methods/delete)

DELETE/accounts/{account_id}/moq/relays/{relay_id}/tokens/{jti}

#### Cloudflare Managed Defense

#### Cloudflare Managed DefenseVulnerability Discovery

#### Cloudflare Managed DefenseVulnerability DiscoveryRepositories

##### [List repositories](https://developers.cloudflare.com/api/resources/managed_defense/subresources/vulnerability_discovery/subresources/repositories/methods/list)

GET/accounts/{account_id}/managed-defense/vulnerability-discovery/repos

##### [Create repository](https://developers.cloudflare.com/api/resources/managed_defense/subresources/vulnerability_discovery/subresources/repositories/methods/create)

POST/accounts/{account_id}/managed-defense/vulnerability-discovery/repos

##### [Get repository](https://developers.cloudflare.com/api/resources/managed_defense/subresources/vulnerability_discovery/subresources/repositories/methods/get)

GET/accounts/{account_id}/managed-defense/vulnerability-discovery/repos/{repo_id}

#### Cloudflare Managed DefenseVulnerability DiscoveryScans

##### [List scans](https://developers.cloudflare.com/api/resources/managed_defense/subresources/vulnerability_discovery/subresources/scans/methods/list)

GET/accounts/{account_id}/managed-defense/vulnerability-discovery/scans

##### [Create scan](https://developers.cloudflare.com/api/resources/managed_defense/subresources/vulnerability_discovery/subresources/scans/methods/create)

POST/accounts/{account_id}/managed-defense/vulnerability-discovery/scans

##### [Get scan](https://developers.cloudflare.com/api/resources/managed_defense/subresources/vulnerability_discovery/subresources/scans/methods/get)

GET/accounts/{account_id}/managed-defense/vulnerability-discovery/scans/{scan_id}

##### [Get reviewed vulnerability report](https://developers.cloudflare.com/api/resources/managed_defense/subresources/vulnerability_discovery/subresources/scans/methods/get_report)

GET/accounts/{account_id}/managed-defense/vulnerability-discovery/scans/{scan_id}/report

#### Cloudflare Managed DefenseVulnerability DiscoveryReports

##### [Get reviewed vulnerability report](https://developers.cloudflare.com/api/resources/managed_defense/subresources/vulnerability_discovery/subresources/reports/methods/get)

GET/accounts/{account_id}/managed-defense/vulnerability-discovery/repos/{repo_id}/scans/{scan_id}/report

#### Cloudforce One

#### Cloudforce OneBinary Storage

##### [Retrieves a file from Binary Storage](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/binary_storage/methods/get)

GET/accounts/{account_id}/cloudforce-one/binary/{hash}

##### [Posts a file to Binary Storage](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/binary_storage/methods/create)

POST/accounts/{account_id}/cloudforce-one/binary

#### Cloudforce OneRequests

##### [List Requests](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/methods/list)

POST/accounts/{account_id}/cloudforce-one/requests

##### [Get a Request](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/methods/get)

GET/accounts/{account_id}/cloudforce-one/requests/{request_id}

##### [Create a New Request.](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/methods/create)

POST/accounts/{account_id}/cloudforce-one/requests/new

##### [Update a Request](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/methods/update)

PUT/accounts/{account_id}/cloudforce-one/requests/{request_id}

##### [Delete a Request](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/methods/delete)

DELETE/accounts/{account_id}/cloudforce-one/requests/{request_id}

##### [Get Request Quota](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/methods/quota)

GET/accounts/{account_id}/cloudforce-one/requests/quota

##### [Get Request Types](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/methods/types)

GET/accounts/{account_id}/cloudforce-one/requests/types

##### [Get Request Priority, Status, and TLP constants](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/methods/constants)

GET/accounts/{account_id}/cloudforce-one/requests/constants

#### Cloudforce OneRequestsMessage

##### [List Request Messages](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/subresources/message/methods/get)

POST/accounts/{account_id}/cloudforce-one/requests/{request_id}/message

##### [Create a New Request Message](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/subresources/message/methods/create)

POST/accounts/{account_id}/cloudforce-one/requests/{request_id}/message/new

##### [Update a Request Message](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/subresources/message/methods/update)

PUT/accounts/{account_id}/cloudforce-one/requests/{request_id}/message/{message_id}

##### [Delete a Request Message](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/subresources/message/methods/delete)

DELETE/accounts/{account_id}/cloudforce-one/requests/{request_id}/message/{message_id}

#### Cloudforce OneRequestsPriority

##### [Get a Priority Intelligence Requirement](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/subresources/priority/methods/get)

GET/accounts/{account_id}/cloudforce-one/requests/priority/{priority_id}

##### [Create a New Priority Intelligence Requirement](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/subresources/priority/methods/create)

POST/accounts/{account_id}/cloudforce-one/requests/priority/new

##### [Update a Priority Intelligence Requirement](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/subresources/priority/methods/update)

PUT/accounts/{account_id}/cloudforce-one/requests/priority/{priority_id}

##### [Delete a Priority Intelligence Requirement](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/subresources/priority/methods/delete)

DELETE/accounts/{account_id}/cloudforce-one/requests/priority/{priority_id}

##### [Get Priority Intelligence Requirement Quota](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/subresources/priority/methods/quota)

GET/accounts/{account_id}/cloudforce-one/requests/priority/quota

#### Cloudforce OneRequestsAssets

##### [Get a Request Asset](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/subresources/assets/methods/get)

GET/accounts/{account_id}/cloudforce-one/requests/{request_id}/asset/{asset_id}

##### [List Request Assets](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/subresources/assets/methods/create)

POST/accounts/{account_id}/cloudforce-one/requests/{request_id}/asset

##### [Update a Request Asset](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/subresources/assets/methods/update)

PUT/accounts/{account_id}/cloudforce-one/requests/{request_id}/asset/{asset_id}

##### [Delete a Request Asset](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/requests/subresources/assets/methods/delete)

DELETE/accounts/{account_id}/cloudforce-one/requests/{request_id}/asset/{asset_id}

#### Cloudforce OneScans

#### Cloudforce OneScansResults

##### [Get the Latest Scan Result](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/scans/subresources/results/methods/get)

GET/accounts/{account_id}/cloudforce-one/scans/results/{config_id}

#### Cloudforce OneScansConfig

##### [List Scan Configs](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/scans/subresources/config/methods/list)

GET/accounts/{account_id}/cloudforce-one/scans/config

##### [Create a new Scan Config](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/scans/subresources/config/methods/create)

POST/accounts/{account_id}/cloudforce-one/scans/config

##### [Update an existing Scan Config](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/scans/subresources/config/methods/edit)

PATCH/accounts/{account_id}/cloudforce-one/scans/config/{config_id}

##### [Delete a Scan Config](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/scans/subresources/config/methods/delete)

DELETE/accounts/{account_id}/cloudforce-one/scans/config/{config_id}

#### Cloudforce OneThreat Events

##### [Filter and list events](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/methods/list)

GET/accounts/{account_id}/cloudforce-one/events

##### [Reads an event](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/methods/get)

Deprecated

GET/accounts/{account_id}/cloudforce-one/events/{event_id}

##### [Creates a new event](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/methods/create)

POST/accounts/{account_id}/cloudforce-one/events/create

##### [Updates an event](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/methods/edit)

PATCH/accounts/{account_id}/cloudforce-one/events/{event_id}

##### [Creates bulk events](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/methods/bulk_create)

POST/accounts/{account_id}/cloudforce-one/events/create/bulk

##### [Creates bulk DOS event with relationships and indicators](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/methods/bulk_create_relationships)

Deprecated

POST/accounts/{account_id}/cloudforce-one/events/create/bulk/relationships

#### Cloudforce OneThreat EventsAggregate

##### [Aggregate events by single or multiple columns with optional date filtering](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/aggregate/methods/list)

GET/accounts/{account_id}/cloudforce-one/events/aggregate

#### Cloudforce OneThreat EventsGraphql

##### [GraphQL endpoint for event aggregation](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/graphql/methods/create)

POST/accounts/{account_id}/cloudforce-one/events/graphql

#### Cloudforce OneThreat EventsGraph

##### [Query graph neighborhood from R2 Data Catalog](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/graph/methods/list)

GET/accounts/{account_id}/cloudforce-one/events/graph

#### Cloudforce OneThreat EventsQueries

##### [List all saved event queries](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/queries/methods/list)

GET/accounts/{account_id}/cloudforce-one/events/queries

##### [Create a saved event query](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/queries/methods/create)

POST/accounts/{account_id}/cloudforce-one/events/queries/create

##### [Read a saved event query](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/queries/methods/get)

GET/accounts/{account_id}/cloudforce-one/events/queries/{query_id}

##### [Update a saved event query](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/queries/methods/edit)

PATCH/accounts/{account_id}/cloudforce-one/events/queries/{query_id}

##### [Delete a saved event query](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/queries/methods/delete)

DELETE/accounts/{account_id}/cloudforce-one/events/queries/{query_id}

#### Cloudforce OneThreat EventsRelationships

##### [Filter and list events related to specific event](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/relationships/methods/list)

Deprecated

GET/accounts/{account_id}/cloudforce-one/events/{event_id}/relationships

#### Cloudforce OneThreat EventsIndicators

##### [Lists indicators across multiple datasets](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/indicators/methods/list)

GET/accounts/{account_id}/cloudforce-one/events/indicators

#### Cloudforce OneThreat EventsIndicatorsAggregate

##### [Aggregate indicators by column(s)](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/indicators/subresources/aggregate/methods/list)

GET/accounts/{account_id}/cloudforce-one/events/indicators/aggregate

#### Cloudforce OneThreat EventsIndicatorsTypes

##### [Lists indicator types across multiple datasets](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/indicators/subresources/types/methods/list)

GET/accounts/{account_id}/cloudforce-one/events/indicator-types

#### Cloudforce OneThreat EventsIndicatorsBy Dataset

##### [Lists indicators](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/indicators/subresources/by_dataset/methods/list)

Deprecated

GET/accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}/indicators

##### [Reads an indicator](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/indicators/subresources/by_dataset/methods/get)

GET/accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}/indicators/{indicator_id}

#### Cloudforce OneThreat EventsIndicatorsBy DatasetTags

##### [List mirrored tags for an indicator dataset](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/indicators/subresources/by_dataset/subresources/tags/methods/list)

GET/accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}/indicators/tags

#### Cloudforce OneThreat EventsAttackers

##### [Lists attackers across multiple datasets](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/attackers/methods/list)

GET/accounts/{account_id}/cloudforce-one/events/attackers

#### Cloudforce OneThreat EventsCategories

##### [Lists categories across multiple datasets](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/categories/methods/list)

GET/accounts/{account_id}/cloudforce-one/events/categories

##### [Reads a category](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/categories/methods/get)

Deprecated

GET/accounts/{account_id}/cloudforce-one/events/categories/{category_id}

##### [Creates a new category](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/categories/methods/create)

POST/accounts/{account_id}/cloudforce-one/events/categories/create

##### [Updates a category](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/categories/methods/edit)

Deprecated

PATCH/accounts/{account_id}/cloudforce-one/events/categories/{category_id}

##### [Deletes a category](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/categories/methods/delete)

Deprecated

DELETE/accounts/{account_id}/cloudforce-one/events/categories/{category_id}

#### Cloudforce OneThreat EventsCategoriesCatalog

##### [Lists categories](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/categories/subresources/catalog/methods/list)

GET/accounts/{account_id}/cloudforce-one/events/categories/catalog

#### Cloudforce OneThreat EventsCountries

##### [Retrieves countries information for all countries](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/countries/methods/list)

GET/accounts/{account_id}/cloudforce-one/events/countries

#### Cloudforce OneThreat EventsCrons

#### Cloudforce OneThreat EventsDatasets

##### [Lists all datasets in an account](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/datasets/methods/list)

GET/accounts/{account_id}/cloudforce-one/events/dataset

##### [Reads a dataset](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/datasets/methods/get)

GET/accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}

##### [Creates a dataset](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/datasets/methods/create)

POST/accounts/{account_id}/cloudforce-one/events/dataset/create

##### [Updates an existing dataset](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/datasets/methods/edit)

PATCH/accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}

##### [Delete a dataset](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/datasets/methods/delete)

DELETE/accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}

##### [Reads raw data for an event by UUID](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/datasets/methods/raw)

Deprecated

GET/accounts/{account_id}/cloudforce-one/events/raw/{dataset_id}/{event_id}

#### Cloudforce OneThreat EventsDatasetsHealth

#### Cloudforce OneThreat EventsDatasetsEvents

##### [Reads an event](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/datasets/subresources/events/methods/get)

GET/accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}/events/{event_id}

#### Cloudforce OneThreat EventsRaw

##### [Reads data for a raw event](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/raw/methods/get)

GET/accounts/{account_id}/cloudforce-one/events/{event_id}/raw/{raw_id}

##### [Updates a raw event](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/raw/methods/edit)

PATCH/accounts/{account_id}/cloudforce-one/events/{event_id}/raw/{raw_id}

#### Cloudforce OneThreat EventsRelate

##### [Removes an event reference](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/relate/methods/delete)

DELETE/accounts/{account_id}/cloudforce-one/events/relate/{event_id}

#### Cloudforce OneThreat EventsTags

##### [Lists all tags (SoT)](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/tags/methods/list)

GET/accounts/{account_id}/cloudforce-one/events/tags

##### [Creates a new tag](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/tags/methods/create)

POST/accounts/{account_id}/cloudforce-one/events/tags/create

##### [Updates a tag (SoT)](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/tags/methods/edit)

PATCH/accounts/{account_id}/cloudforce-one/events/tags/{tag_uuid}

##### [Deletes a tag (SoT)](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/tags/methods/delete)

DELETE/accounts/{account_id}/cloudforce-one/events/tags/{tag_uuid}

#### Cloudforce OneThreat EventsTagsCategories

##### [Lists all tag categories (SoT)](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/tags/subresources/categories/methods/list)

GET/accounts/{account_id}/cloudforce-one/events/tags/categories

##### [Creates a new tag category (SoT)](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/tags/subresources/categories/methods/create)

POST/accounts/{account_id}/cloudforce-one/events/tags/categories/create

##### [Updates a tag category (SoT)](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/tags/subresources/categories/methods/edit)

Deprecated

PATCH/accounts/{account_id}/cloudforce-one/events/tags/categories/{category_uuid}

##### [Deletes a tag category (SoT)](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/tags/subresources/categories/methods/delete)

Deprecated

DELETE/accounts/{account_id}/cloudforce-one/events/tags/categories/{category_uuid}

#### Cloudforce OneThreat EventsTagsIndicators

##### [List indicators related to a tag](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/tags/subresources/indicators/methods/list)

GET/accounts/{account_id}/cloudforce-one/events/tags/{tag_uuid}/indicators

#### Cloudforce OneThreat EventsTagsIndicatorsBy Dataset

##### [List indicators related to a tag within a dataset (deprecated)](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/tags/subresources/indicators/subresources/by_dataset/methods/list)

Deprecated

GET/accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}/tags/{tag_uuid}/indicators

#### Cloudforce OneThreat EventsEvent Tags

##### [Adds a tag to an event](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/event_tags/methods/create)

POST/accounts/{account_id}/cloudforce-one/events/event_tag/{event_id}/create

##### [Removes a tag from an event](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/event_tags/methods/delete)

DELETE/accounts/{account_id}/cloudforce-one/events/event_tag/{event_id}

#### Cloudforce OneThreat EventsTarget Industries

##### [Lists target industries across multiple datasets](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/target_industries/methods/list)

GET/accounts/{account_id}/cloudforce-one/events/targetIndustries

#### Cloudforce OneThreat EventsTarget IndustriesBy Dataset

##### [Lists all target industries for a specific dataset](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/target_industries/subresources/by_dataset/methods/list)

GET/accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}/targetIndustries

#### Cloudforce OneThreat EventsTarget IndustriesCatalog

##### [Lists all target industries from industry map catalog](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/target_industries/subresources/catalog/methods/list)

GET/accounts/{account_id}/cloudforce-one/events/targetIndustries/catalog

#### Cloudforce OneThreat EventsInsights

#### Cloudforce OneThreat Signals

Threat Signals API for managing threat intelligence feeds, articles, indicators, and AI skills in Cloudforce One.

## Prerequisites

  1. **API token** — requests must use an API token with Cloudforce One permissions; write operations (creating, editing, or deleting feeds, skills, and tags) require write access.
  2. **Plan limits** — access on the Free plan is limited; feed quotas and managed default skills apply.



#### Cloudforce OneThreat SignalsSearch

##### [Search Threat Signals articles using AI Search](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/search/methods/search)

GET/accounts/{account_id}/cloudforce-one/v2/threat-signals/search

#### Cloudforce OneThreat SignalsCategories

##### [List Threat Signals feed categories](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/categories/methods/list)

GET/accounts/{account_id}/cloudforce-one/v2/threat-signals/categories

#### Cloudforce OneThreat SignalsFeeds

##### [List Threat Signals feeds](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/feeds/methods/list)

GET/accounts/{account_id}/cloudforce-one/v2/threat-signals/feeds

##### [Create Threat Signals feed](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/feeds/methods/create)

POST/accounts/{account_id}/cloudforce-one/v2/threat-signals/feeds

##### [Update Threat Signals feed](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/feeds/methods/edit)

PATCH/accounts/{account_id}/cloudforce-one/v2/threat-signals/feeds/{feed_id}

##### [Delete Threat Signals feed](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/feeds/methods/delete)

DELETE/accounts/{account_id}/cloudforce-one/v2/threat-signals/feeds/{feed_id}

##### [Trigger Threat Signals feed poll](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/feeds/methods/poll)

POST/accounts/{account_id}/cloudforce-one/v2/threat-signals/feeds/poll

#### Cloudforce OneThreat SignalsFeedsRaw

##### [Get Threat Signals feed XML](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/feeds/subresources/raw/methods/get)

GET/accounts/{account_id}/cloudforce-one/v2/threat-signals/feeds/{feed_id}/raw

#### Cloudforce OneThreat SignalsFeedsSkills

##### [Get Threat Signals feed skills](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/feeds/subresources/skills/methods/get)

GET/accounts/{account_id}/cloudforce-one/v2/threat-signals/feeds/{feed_id}/skills

##### [Set Threat Signals feed skills](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/feeds/subresources/skills/methods/update)

PUT/accounts/{account_id}/cloudforce-one/v2/threat-signals/feeds/{feed_id}/skills

#### Cloudforce OneThreat SignalsArticles

##### [List Threat Signals articles](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/articles/methods/list)

GET/accounts/{account_id}/cloudforce-one/v2/threat-signals/articles

##### [Bulk update Threat Signals article read status](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/articles/methods/bulk_edit)

PATCH/accounts/{account_id}/cloudforce-one/v2/threat-signals/articles

##### [Get Threat Signals article](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/articles/methods/get)

GET/accounts/{account_id}/cloudforce-one/v2/threat-signals/articles/{article_id}

##### [Update Threat Signals article read status](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/articles/methods/edit)

PATCH/accounts/{account_id}/cloudforce-one/v2/threat-signals/articles/{article_id}

#### Cloudforce OneThreat SignalsArticlesContent

##### [Get Threat Signals article content](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/articles/subresources/content/methods/get)

GET/accounts/{account_id}/cloudforce-one/v2/threat-signals/articles/{article_id}/content

#### Cloudforce OneThreat SignalsArticlesTags

##### [Add tag to Threat Signals article](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/articles/subresources/tags/methods/create)

POST/accounts/{account_id}/cloudforce-one/v2/threat-signals/articles/{article_id}/tags

##### [Remove tag from Threat Signals article](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/articles/subresources/tags/methods/delete)

DELETE/accounts/{account_id}/cloudforce-one/v2/threat-signals/articles/{article_id}/tags/{tag_id}

##### [Generate Threat Signals article AI tags](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/articles/subresources/tags/methods/generate)

POST/accounts/{account_id}/cloudforce-one/v2/threat-signals/articles/{article_id}/tag

#### Cloudforce OneThreat SignalsArticlesSkill Outputs

##### [Get Threat Signals article skill output](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/articles/subresources/skill_outputs/methods/get)

GET/accounts/{account_id}/cloudforce-one/v2/threat-signals/articles/{article_id}/skills/{skill_id}/output

#### Cloudforce OneThreat SignalsIndicators

##### [List Threat Signals article indicators](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/indicators/methods/list)

GET/accounts/{account_id}/cloudforce-one/v2/threat-signals/indicators

#### Cloudforce OneThreat SignalsSkills

##### [List Threat Signals skills](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/skills/methods/list)

GET/accounts/{account_id}/cloudforce-one/v2/threat-signals/skills

##### [Create Threat Signals skill](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/skills/methods/create)

POST/accounts/{account_id}/cloudforce-one/v2/threat-signals/skills

##### [Get Threat Signals skill](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/skills/methods/get)

GET/accounts/{account_id}/cloudforce-one/v2/threat-signals/skills/{skill_id}

##### [Update Threat Signals skill](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/skills/methods/edit)

PATCH/accounts/{account_id}/cloudforce-one/v2/threat-signals/skills/{skill_id}

##### [Delete Threat Signals skill](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/skills/methods/delete)

DELETE/accounts/{account_id}/cloudforce-one/v2/threat-signals/skills/{skill_id}

#### Cloudforce OneThreat SignalsSkillsTag Categories

##### [Get Threat Signals skill tag categories](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/skills/subresources/tag_categories/methods/get)

GET/accounts/{account_id}/cloudforce-one/v2/threat-signals/skills/{skill_id}/tag-categories

##### [Replace Threat Signals skill tag categories](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/skills/subresources/tag_categories/methods/update)

PUT/accounts/{account_id}/cloudforce-one/v2/threat-signals/skills/{skill_id}/tag-categories

#### AI Gateway

##### [List gateways](https://developers.cloudflare.com/api/resources/ai_gateway/methods/list)

GET/accounts/{account_id}/ai-gateway/gateways

##### [Get a gateway](https://developers.cloudflare.com/api/resources/ai_gateway/methods/get)

GET/accounts/{account_id}/ai-gateway/gateways/{id}

##### [Create a gateway](https://developers.cloudflare.com/api/resources/ai_gateway/methods/create)

POST/accounts/{account_id}/ai-gateway/gateways

##### [Update a gateway](https://developers.cloudflare.com/api/resources/ai_gateway/methods/update)

PUT/accounts/{account_id}/ai-gateway/gateways/{id}

##### [Delete a gateway](https://developers.cloudflare.com/api/resources/ai_gateway/methods/delete)

DELETE/accounts/{account_id}/ai-gateway/gateways/{id}

#### AI GatewayEvaluation Types

##### [List evaluator types (deprecated)](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/evaluation_types/methods/list)

GET/accounts/{account_id}/ai-gateway/evaluation-types

#### AI GatewayCustom Providers

##### [List custom providers](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/custom_providers/methods/list)

GET/accounts/{account_id}/ai-gateway/custom-providers

##### [Get a custom provider](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/custom_providers/methods/get)

GET/accounts/{account_id}/ai-gateway/custom-providers/{id}

##### [Create a custom provider](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/custom_providers/methods/create)

POST/accounts/{account_id}/ai-gateway/custom-providers

##### [Delete a custom provider](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/custom_providers/methods/delete)

DELETE/accounts/{account_id}/ai-gateway/custom-providers/{id}

#### AI GatewayLogs

##### [List Gateway Logs](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/logs/methods/list)

GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs

##### [Get Gateway Log Detail](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/logs/methods/get)

GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs/{id}

##### [Patch Gateway Log](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/logs/methods/edit)

PATCH/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs/{id}

##### [Delete Gateway Logs](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/logs/methods/delete)

DELETE/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs

##### [Get Gateway Log Request](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/logs/methods/request)

GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs/{id}/request

##### [Get Gateway Log Response](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/logs/methods/response)

GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs/{id}/response

#### AI GatewayDatasets

##### [List datasets (deprecated)](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/datasets/methods/list)

GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/datasets

##### [Get a dataset (deprecated)](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/datasets/methods/get)

GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/datasets/{id}

##### [Create a dataset (deprecated)](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/datasets/methods/create)

POST/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/datasets

##### [Update a dataset (deprecated)](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/datasets/methods/update)

PUT/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/datasets/{id}

##### [Delete a dataset (deprecated)](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/datasets/methods/delete)

DELETE/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/datasets/{id}

#### AI GatewayEvaluations

##### [List evaluations (deprecated)](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/evaluations/methods/list)

GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/evaluations

##### [Get an evaluation (deprecated)](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/evaluations/methods/get)

GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/evaluations/{id}

##### [Create an evaluation (deprecated)](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/evaluations/methods/create)

POST/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/evaluations

##### [Delete an evaluation (deprecated)](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/evaluations/methods/delete)

DELETE/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/evaluations/{id}

#### AI GatewayDynamic Routing

##### [List dynamic routes](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/dynamic_routing/methods/list)

GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes

##### [Get a dynamic route](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/dynamic_routing/methods/get)

GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}

##### [Create a dynamic route](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/dynamic_routing/methods/create)

POST/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes

##### [Rename a dynamic route](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/dynamic_routing/methods/update)

PATCH/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}

##### [Delete a dynamic route](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/dynamic_routing/methods/delete)

DELETE/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}

##### [List dynamic route deployments](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/dynamic_routing/methods/list_deployments)

GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}/deployments

##### [Deploy a dynamic route version](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/dynamic_routing/methods/create_deployment)

POST/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}/deployments

##### [List dynamic route versions](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/dynamic_routing/methods/list_versions)

GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}/versions

##### [Create a dynamic route version](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/dynamic_routing/methods/create_version)

POST/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}/versions

##### [Get a dynamic route version](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/dynamic_routing/methods/get_version)

GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}/versions/{version_id}

#### AI GatewayProvider Configs

##### [List provider keys](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/provider_configs/methods/list)

GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/provider_configs

##### [Store a provider key](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/provider_configs/methods/create)

POST/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/provider_configs

#### AI GatewayURLs

##### [Get Gateway URL](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/urls/methods/get)

GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/url/{provider}

#### AI GatewayBilling

##### [Get credit balance](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/billing/methods/credit_balance)

GET/accounts/{account_id}/ai-gateway/billing/credit-balance

##### [Get usage history](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/billing/methods/usage_history)

GET/accounts/{account_id}/ai-gateway/billing/usage-history

##### [Get invoice history](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/billing/methods/invoice_history)

GET/accounts/{account_id}/ai-gateway/billing/invoice-history

##### [Get invoice preview](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/billing/methods/invoice_preview)

GET/accounts/{account_id}/ai-gateway/billing/invoice-preview

#### AI GatewayBillingTopup

##### [Create a top-up](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/billing/subresources/topup/methods/create)

POST/accounts/{account_id}/ai-gateway/billing/topup

##### [Check top-up status](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/billing/subresources/topup/methods/status)

POST/accounts/{account_id}/ai-gateway/billing/topup/status

#### AI GatewayBillingTopupConfig

##### [Get auto top-up configuration](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/billing/subresources/topup/subresources/config/methods/get)

GET/accounts/{account_id}/ai-gateway/billing/topup/config

##### [Set auto top-up configuration](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/billing/subresources/topup/subresources/config/methods/create)

POST/accounts/{account_id}/ai-gateway/billing/topup/config

##### [Delete auto top-up configuration](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/billing/subresources/topup/subresources/config/methods/delete)

DELETE/accounts/{account_id}/ai-gateway/billing/topup/config

#### AI GatewayBillingSpending Limit

##### [Get spending limit (deprecated)](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/billing/subresources/spending_limit/methods/get)

GET/accounts/{account_id}/ai-gateway/billing/spending-limit

##### [Set spending limit (deprecated)](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/billing/subresources/spending_limit/methods/create)

Deprecated

POST/accounts/{account_id}/ai-gateway/billing/spending-limit

##### [Delete spending limit (deprecated)](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/billing/subresources/spending_limit/methods/delete)

DELETE/accounts/{account_id}/ai-gateway/billing/spending-limit

#### Flagship

#### FlagshipApps

##### [List apps](https://developers.cloudflare.com/api/resources/flagship/subresources/apps/methods/list)

GET/accounts/{account_id}/flagship/apps

##### [Get app](https://developers.cloudflare.com/api/resources/flagship/subresources/apps/methods/get)

GET/accounts/{account_id}/flagship/apps/{app_id}

##### [Create app](https://developers.cloudflare.com/api/resources/flagship/subresources/apps/methods/create)

POST/accounts/{account_id}/flagship/apps

##### [Update app](https://developers.cloudflare.com/api/resources/flagship/subresources/apps/methods/update)

PUT/accounts/{account_id}/flagship/apps/{app_id}

##### [Delete app](https://developers.cloudflare.com/api/resources/flagship/subresources/apps/methods/delete)

DELETE/accounts/{account_id}/flagship/apps/{app_id}

#### FlagshipAppsFlags

##### [List flags](https://developers.cloudflare.com/api/resources/flagship/subresources/apps/subresources/flags/methods/list)

GET/accounts/{account_id}/flagship/apps/{app_id}/flags

##### [Get flag](https://developers.cloudflare.com/api/resources/flagship/subresources/apps/subresources/flags/methods/get)

GET/accounts/{account_id}/flagship/apps/{app_id}/flags/{flag_key}

##### [Create flag](https://developers.cloudflare.com/api/resources/flagship/subresources/apps/subresources/flags/methods/create)

POST/accounts/{account_id}/flagship/apps/{app_id}/flags

##### [Update flag](https://developers.cloudflare.com/api/resources/flagship/subresources/apps/subresources/flags/methods/update)

PUT/accounts/{account_id}/flagship/apps/{app_id}/flags/{flag_key}

##### [Delete flag](https://developers.cloudflare.com/api/resources/flagship/subresources/apps/subresources/flags/methods/delete)

DELETE/accounts/{account_id}/flagship/apps/{app_id}/flags/{flag_key}

#### FlagshipAppsFlagsChangelog

##### [List flag changelog entries](https://developers.cloudflare.com/api/resources/flagship/subresources/apps/subresources/flags/subresources/changelog/methods/list)

GET/accounts/{account_id}/flagship/apps/{app_id}/flags/{flag_key}/changelog

#### FlagshipAppsEvaluate

##### [Evaluate flag from query context](https://developers.cloudflare.com/api/resources/flagship/subresources/apps/subresources/evaluate/methods/get)

GET/accounts/{account_id}/flagship/apps/{app_id}/evaluate

#### IAM

#### IAMPermission Groups

##### [List Account Permission Groups](https://developers.cloudflare.com/api/resources/iam/subresources/permission_groups/methods/list)

GET/accounts/{account_id}/iam/permission_groups

##### [Permission Group Details](https://developers.cloudflare.com/api/resources/iam/subresources/permission_groups/methods/get)

GET/accounts/{account_id}/iam/permission_groups/{permission_group_id}

#### IAMResource Groups

##### [List Resource Groups](https://developers.cloudflare.com/api/resources/iam/subresources/resource_groups/methods/list)

GET/accounts/{account_id}/iam/resource_groups

##### [Resource Group Details](https://developers.cloudflare.com/api/resources/iam/subresources/resource_groups/methods/get)

GET/accounts/{account_id}/iam/resource_groups/{resource_group_id}

##### [Create Resource Group](https://developers.cloudflare.com/api/resources/iam/subresources/resource_groups/methods/create)

POST/accounts/{account_id}/iam/resource_groups

##### [Update Resource Group](https://developers.cloudflare.com/api/resources/iam/subresources/resource_groups/methods/update)

PUT/accounts/{account_id}/iam/resource_groups/{resource_group_id}

##### [Remove Resource Group](https://developers.cloudflare.com/api/resources/iam/subresources/resource_groups/methods/delete)

DELETE/accounts/{account_id}/iam/resource_groups/{resource_group_id}

#### IAMUser Groups

##### [List User Groups](https://developers.cloudflare.com/api/resources/iam/subresources/user_groups/methods/list)

GET/accounts/{account_id}/iam/user_groups

##### [User Group Details](https://developers.cloudflare.com/api/resources/iam/subresources/user_groups/methods/get)

GET/accounts/{account_id}/iam/user_groups/{user_group_id}

##### [Create User Group](https://developers.cloudflare.com/api/resources/iam/subresources/user_groups/methods/create)

POST/accounts/{account_id}/iam/user_groups

##### [Update User Group](https://developers.cloudflare.com/api/resources/iam/subresources/user_groups/methods/update)

PUT/accounts/{account_id}/iam/user_groups/{user_group_id}

##### [Remove User Group](https://developers.cloudflare.com/api/resources/iam/subresources/user_groups/methods/delete)

DELETE/accounts/{account_id}/iam/user_groups/{user_group_id}

#### IAMUser GroupsMembers

##### [List User Group Members](https://developers.cloudflare.com/api/resources/iam/subresources/user_groups/subresources/members/methods/list)

GET/accounts/{account_id}/iam/user_groups/{user_group_id}/members

##### [Get User Group Member](https://developers.cloudflare.com/api/resources/iam/subresources/user_groups/subresources/members/methods/get)

GET/accounts/{account_id}/iam/user_groups/{user_group_id}/members/{member_id}

##### [Add User Group Members](https://developers.cloudflare.com/api/resources/iam/subresources/user_groups/subresources/members/methods/create)

POST/accounts/{account_id}/iam/user_groups/{user_group_id}/members

##### [Update User Group Members](https://developers.cloudflare.com/api/resources/iam/subresources/user_groups/subresources/members/methods/update)

PUT/accounts/{account_id}/iam/user_groups/{user_group_id}/members

##### [Remove User Group Member](https://developers.cloudflare.com/api/resources/iam/subresources/user_groups/subresources/members/methods/delete)

DELETE/accounts/{account_id}/iam/user_groups/{user_group_id}/members/{member_id}

#### IAMSSO

##### [Get all SSO connectors](https://developers.cloudflare.com/api/resources/iam/subresources/sso/methods/list)

GET/accounts/{account_id}/sso_connectors

##### [Get single SSO connector](https://developers.cloudflare.com/api/resources/iam/subresources/sso/methods/get)

GET/accounts/{account_id}/sso_connectors/{sso_connector_id}

##### [Initialize new SSO connector](https://developers.cloudflare.com/api/resources/iam/subresources/sso/methods/create)

POST/accounts/{account_id}/sso_connectors

##### [Update SSO connector state](https://developers.cloudflare.com/api/resources/iam/subresources/sso/methods/update)

PATCH/accounts/{account_id}/sso_connectors/{sso_connector_id}

##### [Delete SSO connector](https://developers.cloudflare.com/api/resources/iam/subresources/sso/methods/delete)

DELETE/accounts/{account_id}/sso_connectors/{sso_connector_id}

##### [Begin SSO connector verification](https://developers.cloudflare.com/api/resources/iam/subresources/sso/methods/begin_verification)

POST/accounts/{account_id}/sso_connectors/{sso_connector_id}/begin_verification

#### IAMOAuth Clients

##### [List OAuth Clients](https://developers.cloudflare.com/api/resources/iam/subresources/oauth_clients/methods/list)

GET/accounts/{account_id}/oauth_clients

##### [OAuth Client Details](https://developers.cloudflare.com/api/resources/iam/subresources/oauth_clients/methods/get)

GET/accounts/{account_id}/oauth_clients/{oauth_client_id}

##### [Create OAuth Client](https://developers.cloudflare.com/api/resources/iam/subresources/oauth_clients/methods/create)

POST/accounts/{account_id}/oauth_clients

##### [Update OAuth Client](https://developers.cloudflare.com/api/resources/iam/subresources/oauth_clients/methods/update)

PATCH/accounts/{account_id}/oauth_clients/{oauth_client_id}

##### [Delete OAuth Client](https://developers.cloudflare.com/api/resources/iam/subresources/oauth_clients/methods/delete)

DELETE/accounts/{account_id}/oauth_clients/{oauth_client_id}

##### [Rotate OAuth Client Secret](https://developers.cloudflare.com/api/resources/iam/subresources/oauth_clients/methods/rotate_secret)

POST/accounts/{account_id}/oauth_clients/{oauth_client_id}/rotate_secret

##### [Delete Rotated OAuth Client Secret](https://developers.cloudflare.com/api/resources/iam/subresources/oauth_clients/methods/delete_rotated_secret)

DELETE/accounts/{account_id}/oauth_clients/{oauth_client_id}/rotate_secret

#### IAMOAuth Scopes

##### [List OAuth Scopes](https://developers.cloudflare.com/api/resources/iam/subresources/oauth_scopes/methods/list)

GET/oauth/scopes

#### Cloud Connector

#### Cloud ConnectorRules

##### [Rules](https://developers.cloudflare.com/api/resources/cloud_connector/subresources/rules/methods/list)

GET/zones/{zone_id}/cloud_connector/rules

##### [Put Rules](https://developers.cloudflare.com/api/resources/cloud_connector/subresources/rules/methods/update)

PUT/zones/{zone_id}/cloud_connector/rules

#### Botnet Feed

#### Botnet FeedASN

##### [Get daily report](https://developers.cloudflare.com/api/resources/botnet_feed/subresources/asn/methods/day_report)

GET/accounts/{account_id}/botnet_feed/asn/{asn_id}/day_report

##### [Get full report](https://developers.cloudflare.com/api/resources/botnet_feed/subresources/asn/methods/full_report)

GET/accounts/{account_id}/botnet_feed/asn/{asn_id}/full_report

#### Botnet FeedConfigs

#### Botnet FeedConfigsASN

##### [Get list of ASNs](https://developers.cloudflare.com/api/resources/botnet_feed/subresources/configs/subresources/asn/methods/get)

GET/accounts/{account_id}/botnet_feed/configs/asn

##### [Delete an ASN](https://developers.cloudflare.com/api/resources/botnet_feed/subresources/configs/subresources/asn/methods/delete)

DELETE/accounts/{account_id}/botnet_feed/configs/asn/{asn_id}

#### Security TXT

##### [Retrieves security.txt](https://developers.cloudflare.com/api/resources/security_txt/methods/get)

GET/zones/{zone_id}/security-center/securitytxt

##### [Updates security.txt](https://developers.cloudflare.com/api/resources/security_txt/methods/update)

PUT/zones/{zone_id}/security-center/securitytxt

##### [Deletes security.txt](https://developers.cloudflare.com/api/resources/security_txt/methods/delete)

DELETE/zones/{zone_id}/security-center/securitytxt

#### Workflows

##### [List all Workflows](https://developers.cloudflare.com/api/resources/workflows/methods/list)

GET/accounts/{account_id}/workflows

##### [Get Workflow details](https://developers.cloudflare.com/api/resources/workflows/methods/get)

GET/accounts/{account_id}/workflows/{workflow_name}

##### [Create/modify Workflow](https://developers.cloudflare.com/api/resources/workflows/methods/update)

PUT/accounts/{account_id}/workflows/{workflow_name}

##### [Deletes a Workflow](https://developers.cloudflare.com/api/resources/workflows/methods/delete)

DELETE/accounts/{account_id}/workflows/{workflow_name}

#### WorkflowsInstances

##### [List of workflow instances](https://developers.cloudflare.com/api/resources/workflows/subresources/instances/methods/list)

GET/accounts/{account_id}/workflows/{workflow_name}/instances

##### [Get logs and status from instance](https://developers.cloudflare.com/api/resources/workflows/subresources/instances/methods/get)

GET/accounts/{account_id}/workflows/{workflow_name}/instances/{instance_id}

##### [Create a new workflow instance](https://developers.cloudflare.com/api/resources/workflows/subresources/instances/methods/create)

POST/accounts/{account_id}/workflows/{workflow_name}/instances

##### [Batch create new Workflow instances](https://developers.cloudflare.com/api/resources/workflows/subresources/instances/methods/bulk)

POST/accounts/{account_id}/workflows/{workflow_name}/instances/batch

##### [Get full step output from instance](https://developers.cloudflare.com/api/resources/workflows/subresources/instances/methods/step)

GET/accounts/{account_id}/workflows/{workflow_name}/instances/{instance_id}/step

#### WorkflowsInstancesStatus

##### [Change status of instance](https://developers.cloudflare.com/api/resources/workflows/subresources/instances/subresources/status/methods/edit)

PATCH/accounts/{account_id}/workflows/{workflow_name}/instances/{instance_id}/status

#### WorkflowsInstancesEvents

##### [Send event to instance](https://developers.cloudflare.com/api/resources/workflows/subresources/instances/subresources/events/methods/create)

POST/accounts/{account_id}/workflows/{workflow_name}/instances/{instance_id}/events/{event_type}

#### WorkflowsVersions

##### [List deployed Workflow versions](https://developers.cloudflare.com/api/resources/workflows/subresources/versions/methods/list)

GET/accounts/{account_id}/workflows/{workflow_name}/versions

##### [Get Workflow version details](https://developers.cloudflare.com/api/resources/workflows/subresources/versions/methods/get)

GET/accounts/{account_id}/workflows/{workflow_name}/versions/{version_id}

##### [Get Workflow version graph](https://developers.cloudflare.com/api/resources/workflows/subresources/versions/methods/graph)

GET/accounts/{account_id}/workflows/{workflow_name}/versions/{version_id}/graph

#### Workers Builds

##### [Get latest builds by script IDs](https://developers.cloudflare.com/api/resources/workers_builds/methods/get_latest_builds)

GET/accounts/{account_id}/builds/builds/latest

##### [Get builds by Worker version](https://developers.cloudflare.com/api/resources/workers_builds/methods/get_builds_by_version)

GET/accounts/{account_id}/builds/builds

##### [Get build-minute availability](https://developers.cloudflare.com/api/resources/workers_builds/methods/get_account_limits)

GET/accounts/{account_id}/builds/account/limits

#### Workers BuildsTriggers

##### [List triggers for a Worker](https://developers.cloudflare.com/api/resources/workers_builds/subresources/triggers/methods/list)

GET/accounts/{account_id}/builds/workers/{external_script_id}/triggers

##### [Create a build trigger](https://developers.cloudflare.com/api/resources/workers_builds/subresources/triggers/methods/create)

POST/accounts/{account_id}/builds/triggers

##### [Update a build trigger](https://developers.cloudflare.com/api/resources/workers_builds/subresources/triggers/methods/update)

PATCH/accounts/{account_id}/builds/triggers/{trigger_uuid}

##### [Delete a build trigger](https://developers.cloudflare.com/api/resources/workers_builds/subresources/triggers/methods/delete)

DELETE/accounts/{account_id}/builds/triggers/{trigger_uuid}

##### [Purge a trigger's build cache](https://developers.cloudflare.com/api/resources/workers_builds/subresources/triggers/methods/purge_cache)

POST/accounts/{account_id}/builds/triggers/{trigger_uuid}/purge_build_cache

##### [Start a Workers build](https://developers.cloudflare.com/api/resources/workers_builds/subresources/triggers/methods/create_build)

POST/accounts/{account_id}/builds/triggers/{trigger_uuid}/builds

#### Workers BuildsTriggersEnvironment Variables

##### [List build variables](https://developers.cloudflare.com/api/resources/workers_builds/subresources/triggers/subresources/environment_variables/methods/list)

GET/accounts/{account_id}/builds/triggers/{trigger_uuid}/environment_variables

##### [Set build variables](https://developers.cloudflare.com/api/resources/workers_builds/subresources/triggers/subresources/environment_variables/methods/upsert)

PATCH/accounts/{account_id}/builds/triggers/{trigger_uuid}/environment_variables

##### [Delete a build variable](https://developers.cloudflare.com/api/resources/workers_builds/subresources/triggers/subresources/environment_variables/methods/delete)

DELETE/accounts/{account_id}/builds/triggers/{trigger_uuid}/environment_variables/{environment_variable_key}

#### Workers BuildsDeploy Hooks

##### [List deploy hooks](https://developers.cloudflare.com/api/resources/workers_builds/subresources/deploy_hooks/methods/list)

GET/accounts/{account_id}/builds/workers/{script_name}/deploy_hooks

##### [Create a deploy hook](https://developers.cloudflare.com/api/resources/workers_builds/subresources/deploy_hooks/methods/create)

POST/accounts/{account_id}/builds/workers/{script_name}/deploy_hooks

##### [Get a deploy hook](https://developers.cloudflare.com/api/resources/workers_builds/subresources/deploy_hooks/methods/get)

GET/accounts/{account_id}/builds/workers/{script_name}/deploy_hooks/{deploy_hook_uuid}

##### [Update a deploy hook](https://developers.cloudflare.com/api/resources/workers_builds/subresources/deploy_hooks/methods/update)

PUT/accounts/{account_id}/builds/workers/{script_name}/deploy_hooks/{deploy_hook_uuid}

##### [Delete a deploy hook](https://developers.cloudflare.com/api/resources/workers_builds/subresources/deploy_hooks/methods/delete)

DELETE/accounts/{account_id}/builds/workers/{script_name}/deploy_hooks/{deploy_hook_uuid}

##### [Trigger deploy hook](https://developers.cloudflare.com/api/resources/workers_builds/subresources/deploy_hooks/methods/trigger)

POST/workers/builds/deploy_hooks/{deploy_hook_uuid}

#### Workers BuildsTokens

##### [Create build token](https://developers.cloudflare.com/api/resources/workers_builds/subresources/tokens/methods/create)

POST/accounts/{account_id}/builds/tokens

##### [List build tokens](https://developers.cloudflare.com/api/resources/workers_builds/subresources/tokens/methods/list)

GET/accounts/{account_id}/builds/tokens

##### [Delete a build token](https://developers.cloudflare.com/api/resources/workers_builds/subresources/tokens/methods/delete)

DELETE/accounts/{account_id}/builds/tokens/{build_token_uuid}

#### Workers BuildsRepos

#### Workers BuildsReposConnections

##### [Create or update a repository connection](https://developers.cloudflare.com/api/resources/workers_builds/subresources/repos/subresources/connections/methods/upsert)

PUT/accounts/{account_id}/builds/repos/connections

##### [Delete a repository connection](https://developers.cloudflare.com/api/resources/workers_builds/subresources/repos/subresources/connections/methods/delete)

DELETE/accounts/{account_id}/builds/repos/connections/{repo_connection_uuid}

#### Workers BuildsReposConfig Autofill

##### [Get repository configuration autofill](https://developers.cloudflare.com/api/resources/workers_builds/subresources/repos/subresources/config_autofill/methods/get)

GET/accounts/{account_id}/builds/repos/{provider_type}/{provider_account_id}/{repo_id}/config_autofill

#### Workers BuildsBuilds

##### [List builds for a Worker](https://developers.cloudflare.com/api/resources/workers_builds/subresources/builds/methods/list)

GET/accounts/{account_id}/builds/workers/{external_script_id}/builds

##### [Get a Workers build](https://developers.cloudflare.com/api/resources/workers_builds/subresources/builds/methods/get)

GET/accounts/{account_id}/builds/builds/{build_uuid}

##### [Cancel a Workers build](https://developers.cloudflare.com/api/resources/workers_builds/subresources/builds/methods/cancel)

PUT/accounts/{account_id}/builds/builds/{build_uuid}/cancel

#### Workers BuildsBuildsLogs

##### [Get Workers build logs](https://developers.cloudflare.com/api/resources/workers_builds/subresources/builds/subresources/logs/methods/get)

GET/accounts/{account_id}/builds/builds/{build_uuid}/logs

#### Resource Sharing

##### [List account shares](https://developers.cloudflare.com/api/resources/resource_sharing/methods/list)

GET/accounts/{account_id}/shares

##### [Get account share by ID](https://developers.cloudflare.com/api/resources/resource_sharing/methods/get)

GET/accounts/{account_id}/shares/{share_id}

##### [Trigger a share creation](https://developers.cloudflare.com/api/resources/resource_sharing/methods/create)

POST/accounts/{account_id}/shares

##### [Trigger a share rename](https://developers.cloudflare.com/api/resources/resource_sharing/methods/update)

PUT/accounts/{account_id}/shares/{share_id}

##### [Trigger a share deletion](https://developers.cloudflare.com/api/resources/resource_sharing/methods/delete)

DELETE/accounts/{account_id}/shares/{share_id}

#### Resource SharingRecipients

##### [List share recipients by share ID](https://developers.cloudflare.com/api/resources/resource_sharing/subresources/recipients/methods/list)

GET/accounts/{account_id}/shares/{share_id}/recipients

##### [Get share recipient by ID](https://developers.cloudflare.com/api/resources/resource_sharing/subresources/recipients/methods/get)

GET/accounts/{account_id}/shares/{share_id}/recipients/{recipient_id}

##### [Trigger a recipient addition to a share](https://developers.cloudflare.com/api/resources/resource_sharing/subresources/recipients/methods/create)

POST/accounts/{account_id}/shares/{share_id}/recipients

##### [Trigger a recipient removal from a share](https://developers.cloudflare.com/api/resources/resource_sharing/subresources/recipients/methods/delete)

DELETE/accounts/{account_id}/shares/{share_id}/recipients/{recipient_id}

#### Resource SharingResources

##### [List share resources by share ID](https://developers.cloudflare.com/api/resources/resource_sharing/subresources/resources/methods/list)

GET/accounts/{account_id}/shares/{share_id}/resources

##### [Get share resource by ID](https://developers.cloudflare.com/api/resources/resource_sharing/subresources/resources/methods/get)

GET/accounts/{account_id}/shares/{share_id}/resources/{share_resource_id}

##### [Trigger a resource addition to a share](https://developers.cloudflare.com/api/resources/resource_sharing/subresources/resources/methods/create)

POST/accounts/{account_id}/shares/{share_id}/resources

##### [Trigger a resource metadata update in a share](https://developers.cloudflare.com/api/resources/resource_sharing/subresources/resources/methods/update)

PUT/accounts/{account_id}/shares/{share_id}/resources/{share_resource_id}

##### [Trigger a resource deletion from a share](https://developers.cloudflare.com/api/resources/resource_sharing/subresources/resources/methods/delete)

DELETE/accounts/{account_id}/shares/{share_id}/resources/{share_resource_id}

#### Resource Tagging

##### [List tagged resources](https://developers.cloudflare.com/api/resources/resource_tagging/methods/list)

GET/accounts/{account_id}/tags/resources

#### Resource TaggingAccount Tags

##### [Get tags for an account-level resource](https://developers.cloudflare.com/api/resources/resource_tagging/subresources/account_tags/methods/get)

GET/accounts/{account_id}/tags

##### [Set tags for an account-level resource](https://developers.cloudflare.com/api/resources/resource_tagging/subresources/account_tags/methods/update)

PUT/accounts/{account_id}/tags

##### [Delete tags from an account-level resource](https://developers.cloudflare.com/api/resources/resource_tagging/subresources/account_tags/methods/delete)

DELETE/accounts/{account_id}/tags

#### Resource TaggingZone Tags

##### [Get tags for a zone-level resource](https://developers.cloudflare.com/api/resources/resource_tagging/subresources/zone_tags/methods/get)

GET/zones/{zone_id}/tags

##### [Set tags for a zone-level resource](https://developers.cloudflare.com/api/resources/resource_tagging/subresources/zone_tags/methods/update)

PUT/zones/{zone_id}/tags

##### [Delete tags from a zone-level resource](https://developers.cloudflare.com/api/resources/resource_tagging/subresources/zone_tags/methods/delete)

DELETE/zones/{zone_id}/tags

#### Resource TaggingKeys

##### [List tag keys](https://developers.cloudflare.com/api/resources/resource_tagging/subresources/keys/methods/list)

GET/accounts/{account_id}/tags/keys

#### Resource TaggingValues

##### [List tag values](https://developers.cloudflare.com/api/resources/resource_tagging/subresources/values/methods/list)

GET/accounts/{account_id}/tags/values/{tag_key}

#### Resource TaggingSummary

##### [List tag key summary](https://developers.cloudflare.com/api/resources/resource_tagging/subresources/summary/methods/get)

GET/accounts/{account_id}/tags/summary

#### Leaked Credential Checks

##### [Get the Leaked Credential Checks status for a zone.](https://developers.cloudflare.com/api/resources/leaked_credential_checks/methods/get)

GET/zones/{zone_id}/leaked-credential-checks

##### [Update the Leaked Credential Checks status for a zone.](https://developers.cloudflare.com/api/resources/leaked_credential_checks/methods/create)

POST/zones/{zone_id}/leaked-credential-checks

#### Leaked Credential ChecksDetections

##### [List the custom detection locations of a zone.](https://developers.cloudflare.com/api/resources/leaked_credential_checks/subresources/detections/methods/list)

GET/zones/{zone_id}/leaked-credential-checks/detections

##### [Create a custom detection location for a zone.](https://developers.cloudflare.com/api/resources/leaked_credential_checks/subresources/detections/methods/create)

POST/zones/{zone_id}/leaked-credential-checks/detections

##### [Get a custom detection location of a zone.](https://developers.cloudflare.com/api/resources/leaked_credential_checks/subresources/detections/methods/get)

GET/zones/{zone_id}/leaked-credential-checks/detections/{detection_id}

##### [Update a custom detection location of a zone.](https://developers.cloudflare.com/api/resources/leaked_credential_checks/subresources/detections/methods/update)

PUT/zones/{zone_id}/leaked-credential-checks/detections/{detection_id}

##### [Delete a custom detection location from a zone.](https://developers.cloudflare.com/api/resources/leaked_credential_checks/subresources/detections/methods/delete)

DELETE/zones/{zone_id}/leaked-credential-checks/detections/{detection_id}

#### Content Scanning

##### [Enable Content Scanning for a zone.](https://developers.cloudflare.com/api/resources/content_scanning/methods/enable)

POST/zones/{zone_id}/content-upload-scan/enable

##### [Disable Content Scanning for a zone.](https://developers.cloudflare.com/api/resources/content_scanning/methods/disable)

POST/zones/{zone_id}/content-upload-scan/disable

##### [Update the Content Scanning status for a zone.](https://developers.cloudflare.com/api/resources/content_scanning/methods/create)

PUT/zones/{zone_id}/content-upload-scan/settings

##### [Update the Content Scanning status for a zone.](https://developers.cloudflare.com/api/resources/content_scanning/methods/update)

PUT/zones/{zone_id}/content-upload-scan/settings

##### [Get the Content Scanning status for a zone.](https://developers.cloudflare.com/api/resources/content_scanning/methods/get)

GET/zones/{zone_id}/content-upload-scan/settings

#### Content ScanningPayloads

##### [List the Content Scanning custom expressions of a zone.](https://developers.cloudflare.com/api/resources/content_scanning/subresources/payloads/methods/list)

GET/zones/{zone_id}/content-upload-scan/payloads

##### [Create Content Scanning custom expressions for a zone.](https://developers.cloudflare.com/api/resources/content_scanning/subresources/payloads/methods/create)

POST/zones/{zone_id}/content-upload-scan/payloads

##### [Delete a Content Scanning custom expression from a zone.](https://developers.cloudflare.com/api/resources/content_scanning/subresources/payloads/methods/delete)

DELETE/zones/{zone_id}/content-upload-scan/payloads/{expression_id}

##### [Update a Content Scanning custom expression for a zone.](https://developers.cloudflare.com/api/resources/content_scanning/subresources/payloads/methods/update)

PATCH/zones/{zone_id}/content-upload-scan/payloads/{expression_id}

#### Content ScanningSettings

##### [Get the Content Scanning status for a zone.](https://developers.cloudflare.com/api/resources/content_scanning/subresources/settings/methods/get)

GET/zones/{zone_id}/content-upload-scan/settings

#### AI Security

##### [Get the AI Security for Apps status for a zone.](https://developers.cloudflare.com/api/resources/ai_security/methods/get)

GET/zones/{zone_id}/ai-security/settings

##### [Update the AI Security for Apps status for a zone.](https://developers.cloudflare.com/api/resources/ai_security/methods/update)

PUT/zones/{zone_id}/ai-security/settings

#### AI SecurityCustom Topics

##### [Get the AI Security for Apps custom topics of a zone.](https://developers.cloudflare.com/api/resources/ai_security/subresources/custom_topics/methods/get)

GET/zones/{zone_id}/ai-security/custom-topics

##### [Update the AI Security for Apps custom topics of a zone.](https://developers.cloudflare.com/api/resources/ai_security/subresources/custom_topics/methods/update)

PUT/zones/{zone_id}/ai-security/custom-topics

#### Csam Scanner

##### [Get CSAM Scanner setting](https://developers.cloudflare.com/api/resources/csam_scanner/methods/get)

GET/zones/{zone_id}/settings/csam_scanner_third_party

##### [Update CSAM Scanner setting](https://developers.cloudflare.com/api/resources/csam_scanner/methods/edit)

PATCH/zones/{zone_id}/settings/csam_scanner_third_party

#### Abuse Reports

##### [Submit an abuse report](https://developers.cloudflare.com/api/resources/abuse_reports/methods/create)

POST/accounts/{account_id}/abuse-reports/{report_param}

##### [Get an abuse report against the account](https://developers.cloudflare.com/api/resources/abuse_reports/methods/get)

GET/accounts/{account_id}/abuse-reports/{report_param}

##### [List abuse reports against the account](https://developers.cloudflare.com/api/resources/abuse_reports/methods/list)

GET/accounts/{account_id}/abuse-reports

#### Abuse ReportsSubmitted

##### [List submitted abuse reports](https://developers.cloudflare.com/api/resources/abuse_reports/subresources/submitted/methods/list)

GET/accounts/{account_id}/abuse-reports/submitted

##### [Get a submitted abuse report](https://developers.cloudflare.com/api/resources/abuse_reports/subresources/submitted/methods/get)

GET/accounts/{account_id}/abuse-reports/submitted/{report_id}

#### Abuse ReportsSubmittedEmails

##### [List emails sent to an abuse report submitter](https://developers.cloudflare.com/api/resources/abuse_reports/subresources/submitted/subresources/emails/methods/list)

GET/accounts/{account_id}/abuse-reports/submitted/{report_id}/emails

#### Abuse ReportsMitigations

##### [List abuse report mitigations](https://developers.cloudflare.com/api/resources/abuse_reports/subresources/mitigations/methods/list)

GET/accounts/{account_id}/abuse-reports/{report_id}/mitigations

##### [Request review on mitigations](https://developers.cloudflare.com/api/resources/abuse_reports/subresources/mitigations/methods/review)

POST/accounts/{account_id}/abuse-reports/{report_id}/mitigations/appeal

#### AI

##### [Run a Workers AI model](https://developers.cloudflare.com/api/resources/ai/methods/run)

POST/accounts/{account_id}/ai/run/{model_name}

#### AIFinetunes

##### [List Finetunes](https://developers.cloudflare.com/api/resources/ai/subresources/finetunes/methods/list)

GET/accounts/{account_id}/ai/finetunes

##### [Create a new Finetune](https://developers.cloudflare.com/api/resources/ai/subresources/finetunes/methods/create)

POST/accounts/{account_id}/ai/finetunes

#### AIFinetunesAssets

##### [Upload a Finetune Asset](https://developers.cloudflare.com/api/resources/ai/subresources/finetunes/subresources/assets/methods/create)

POST/accounts/{account_id}/ai/finetunes/{finetune_id}/finetune-assets

#### AIFinetunesPublic

##### [List Public Finetunes](https://developers.cloudflare.com/api/resources/ai/subresources/finetunes/subresources/public/methods/list)

GET/accounts/{account_id}/ai/finetunes/public

#### AIAuthors

##### [Author Search](https://developers.cloudflare.com/api/resources/ai/subresources/authors/methods/list)

GET/accounts/{account_id}/ai/authors/search

#### AITasks

##### [Task Search](https://developers.cloudflare.com/api/resources/ai/subresources/tasks/methods/list)

GET/accounts/{account_id}/ai/tasks/search

#### AIModels

##### [Model Search](https://developers.cloudflare.com/api/resources/ai/subresources/models/methods/list)

GET/accounts/{account_id}/ai/models/search

#### AIModelsSchema

##### [Get an AI model's input and output schemas](https://developers.cloudflare.com/api/resources/ai/subresources/models/subresources/schema/methods/get)

GET/accounts/{account_id}/ai/models/schema

#### AITo Markdown

##### [Convert uploaded files to Markdown](https://developers.cloudflare.com/api/resources/ai/subresources/to_markdown/methods/transform)

POST/accounts/{account_id}/ai/tomarkdown

##### [List supported Markdown conversion formats](https://developers.cloudflare.com/api/resources/ai/subresources/to_markdown/methods/supported)

GET/accounts/{account_id}/ai/tomarkdown/supported

#### AI Audit

#### AI AuditRobots

##### [Get robots.txt rules](https://developers.cloudflare.com/api/resources/ai_audit/subresources/robots/methods/get)

GET/zones/{zone_id}/ai-audit/robots

##### [Bulk get robots.txt rules](https://developers.cloudflare.com/api/resources/ai_audit/subresources/robots/methods/bulk_get)

POST/zones/{zone_id}/ai-audit/robots/bulk

#### AI Search

#### AI SearchNamespaces

##### [List namespaces](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/methods/list)

GET/accounts/{account_id}/ai-search/namespaces

##### [Create a namespace](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/methods/create)

POST/accounts/{account_id}/ai-search/namespaces

##### [Get a namespace](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/methods/read)

GET/accounts/{account_id}/ai-search/namespaces/{name}

##### [Update a namespace](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/methods/update)

PUT/accounts/{account_id}/ai-search/namespaces/{name}

##### [Delete a namespace](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/methods/delete)

DELETE/accounts/{account_id}/ai-search/namespaces/{name}

##### [Multi-Instance Search](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/methods/search)

POST/accounts/{account_id}/ai-search/namespaces/{name}/search

##### [Multi-Instance Chat Completions](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/methods/chat_completions)

POST/accounts/{account_id}/ai-search/namespaces/{name}/chat/completions

#### AI SearchNamespacesInstances

##### [List AI Search instances.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/list)

GET/accounts/{account_id}/ai-search/namespaces/{name}/instances

##### [Create an AI Search instance.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/create)

POST/accounts/{account_id}/ai-search/namespaces/{name}/instances

##### [Get an AI Search instance.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/read)

GET/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}

##### [Update an AI Search instance.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/update)

PUT/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}

##### [Delete an AI Search instance.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/delete)

DELETE/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}

##### [Get instance statistics.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/stats)

GET/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/stats

##### [Search](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/search)

POST/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/search

##### [Chat Completions](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/chat_completions)

POST/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/chat/completions

#### AI SearchNamespacesInstancesJobs

##### [List Jobs](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/jobs/methods/list)

GET/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/jobs

##### [Create new job](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/jobs/methods/create)

POST/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/jobs

##### [Get a Job Details](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/jobs/methods/get)

GET/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/jobs/{job_id}

##### [Cancel an indexing job.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/jobs/methods/update)

PATCH/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/jobs/{job_id}

##### [List Job Logs](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/jobs/methods/logs)

GET/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/jobs/{job_id}/logs

#### AI SearchNamespacesInstancesItems

##### [Items List.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/list)

GET/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items

##### [Upload Item.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/upload)

POST/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items

##### [Create or Update Item.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/create_or_update)

PUT/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items

##### [Get Item.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/get)

GET/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}

##### [Sync Item.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/sync)

PATCH/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}

##### [Delete Item.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/delete)

DELETE/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}

##### [Download Item Content.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/download)

GET/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}/download

##### [Item Logs.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/logs)

GET/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}/logs

##### [List Item Chunks.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/chunks)

GET/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}/chunks

#### AI SearchInstances

##### [List AI Search instances.](https://developers.cloudflare.com/api/resources/ai_search/subresources/instances/methods/list)

Deprecated

GET/accounts/{account_id}/ai-search/instances

##### [Create an AI Search instance.](https://developers.cloudflare.com/api/resources/ai_search/subresources/instances/methods/create)

Deprecated

POST/accounts/{account_id}/ai-search/instances

##### [Get an AI Search instance.](https://developers.cloudflare.com/api/resources/ai_search/subresources/instances/methods/read)

Deprecated

GET/accounts/{account_id}/ai-search/instances/{id}

##### [Update an AI Search instance.](https://developers.cloudflare.com/api/resources/ai_search/subresources/instances/methods/update)

Deprecated

PUT/accounts/{account_id}/ai-search/instances/{id}

##### [Delete an AI Search instance.](https://developers.cloudflare.com/api/resources/ai_search/subresources/instances/methods/delete)

Deprecated

DELETE/accounts/{account_id}/ai-search/instances/{id}

##### [Get instance statistics.](https://developers.cloudflare.com/api/resources/ai_search/subresources/instances/methods/stats)

Deprecated

GET/accounts/{account_id}/ai-search/instances/{id}/stats

##### [Search](https://developers.cloudflare.com/api/resources/ai_search/subresources/instances/methods/search)

Deprecated

POST/accounts/{account_id}/ai-search/instances/{id}/search

##### [Chat Completions](https://developers.cloudflare.com/api/resources/ai_search/subresources/instances/methods/chat_completions)

Deprecated

POST/accounts/{account_id}/ai-search/instances/{id}/chat/completions

#### AI SearchInstancesJobs

##### [List Jobs](https://developers.cloudflare.com/api/resources/ai_search/subresources/instances/subresources/jobs/methods/list)

Deprecated

GET/accounts/{account_id}/ai-search/instances/{id}/jobs

##### [Create new job](https://developers.cloudflare.com/api/resources/ai_search/subresources/instances/subresources/jobs/methods/create)

Deprecated

POST/accounts/{account_id}/ai-search/instances/{id}/jobs

##### [Get a Job Details](https://developers.cloudflare.com/api/resources/ai_search/subresources/instances/subresources/jobs/methods/get)

Deprecated

GET/accounts/{account_id}/ai-search/instances/{id}/jobs/{job_id}

##### [List Job Logs](https://developers.cloudflare.com/api/resources/ai_search/subresources/instances/subresources/jobs/methods/logs)

Deprecated

GET/accounts/{account_id}/ai-search/instances/{id}/jobs/{job_id}/logs

#### AI SearchTokens

##### [List tokens](https://developers.cloudflare.com/api/resources/ai_search/subresources/tokens/methods/list)

GET/accounts/{account_id}/ai-search/tokens

##### [Create a token](https://developers.cloudflare.com/api/resources/ai_search/subresources/tokens/methods/create)

POST/accounts/{account_id}/ai-search/tokens

##### [Get a token](https://developers.cloudflare.com/api/resources/ai_search/subresources/tokens/methods/read)

GET/accounts/{account_id}/ai-search/tokens/{id}

##### [Update a token](https://developers.cloudflare.com/api/resources/ai_search/subresources/tokens/methods/update)

PUT/accounts/{account_id}/ai-search/tokens/{id}

##### [Delete a token](https://developers.cloudflare.com/api/resources/ai_search/subresources/tokens/methods/delete)

DELETE/accounts/{account_id}/ai-search/tokens/{id}

#### AutoRAG

##### [AI Search](https://developers.cloudflare.com/api/resources/autorag/methods/ai_search)

Deprecated

POST/accounts/{account_id}/autorag/rags/{id}/ai-search

##### [Search](https://developers.cloudflare.com/api/resources/autorag/methods/search)

Deprecated

POST/accounts/{account_id}/autorag/rags/{id}/search

##### [Sync](https://developers.cloudflare.com/api/resources/autorag/methods/sync)

Deprecated

PATCH/accounts/{account_id}/autorag/rags/{id}/sync

##### [Files](https://developers.cloudflare.com/api/resources/autorag/methods/files)

Deprecated

GET/accounts/{account_id}/autorag/rags/{id}/files

#### AutoRAGJobs

##### [List Jobs](https://developers.cloudflare.com/api/resources/autorag/subresources/jobs/methods/list)

Deprecated

GET/accounts/{account_id}/autorag/rags/{id}/jobs

##### [Get a Job Details](https://developers.cloudflare.com/api/resources/autorag/subresources/jobs/methods/get)

Deprecated

GET/accounts/{account_id}/autorag/rags/{id}/jobs/{job_id}

##### [List Job Logs](https://developers.cloudflare.com/api/resources/autorag/subresources/jobs/methods/logs)

Deprecated

GET/accounts/{account_id}/autorag/rags/{id}/jobs/{job_id}/logs

#### Security Center

#### Security CenterInsights

##### [Retrieves Security Center Insights](https://developers.cloudflare.com/api/resources/security_center/subresources/insights/methods/list)

GET/{accounts_or_zones}/{account_or_zone_id}/security-center/insights

##### [Archives Security Center Insight](https://developers.cloudflare.com/api/resources/security_center/subresources/insights/methods/dismiss)

PUT/{accounts_or_zones}/{account_or_zone_id}/security-center/insights/{issue_id}/dismiss

#### Security CenterInsightsClass

##### [Retrieves Security Center Insight Counts by Class](https://developers.cloudflare.com/api/resources/security_center/subresources/insights/subresources/class/methods/get)

GET/{accounts_or_zones}/{account_or_zone_id}/security-center/insights/class

#### Security CenterInsightsSeverity

##### [Retrieves Security Center Insight Counts by Severity](https://developers.cloudflare.com/api/resources/security_center/subresources/insights/subresources/severity/methods/get)

GET/{accounts_or_zones}/{account_or_zone_id}/security-center/insights/severity

#### Security CenterInsightsType

##### [Retrieves Security Center Insight Counts by Type](https://developers.cloudflare.com/api/resources/security_center/subresources/insights/subresources/type/methods/get)

GET/{accounts_or_zones}/{account_or_zone_id}/security-center/insights/type

#### Security CenterInsightsAudit Logs

##### [Retrieves account or zone Audit Log](https://developers.cloudflare.com/api/resources/security_center/subresources/insights/subresources/audit_logs/methods/list)

GET/{accounts_or_zones}/{account_or_zone_id}/security-center/insights/audit-log

##### [Retrieves Issue Audit Log](https://developers.cloudflare.com/api/resources/security_center/subresources/insights/subresources/audit_logs/methods/list_by_insight)

GET/{accounts_or_zones}/{account_or_zone_id}/security-center/insights/{issue_id}/audit-log

#### Security CenterInsightsClassification

##### [Updates Security Center Insight Classification](https://developers.cloudflare.com/api/resources/security_center/subresources/insights/subresources/classification/methods/update)

PATCH/{accounts_or_zones}/{account_or_zone_id}/security-center/insights/{issue_id}/classification

#### Security CenterInsightsContext

##### [Retrieves Security Center Insight Context](https://developers.cloudflare.com/api/resources/security_center/subresources/insights/subresources/context/methods/get)

GET/accounts/{account_id}/security-center/insights/{issue_id}/context

#### Browser Rendering

#### Browser RenderingContent

##### [Get HTML content.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/content/methods/create)

POST/accounts/{account_id}/browser-rendering/content

#### Browser RenderingPDF

##### [Get PDF.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/pdf/methods/create)

POST/accounts/{account_id}/browser-rendering/pdf

#### Browser RenderingScrape

##### [Scrape elements.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/scrape/methods/create)

POST/accounts/{account_id}/browser-rendering/scrape

#### Browser RenderingScreenshot

##### [Get screenshot.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/screenshot/methods/create)

POST/accounts/{account_id}/browser-rendering/screenshot

#### Browser RenderingSnapshot

##### [Get HTML content and screenshot.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/snapshot/methods/create)

POST/accounts/{account_id}/browser-rendering/snapshot

#### Browser RenderingJson

##### [Get json.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/json/methods/create)

POST/accounts/{account_id}/browser-rendering/json

#### Browser RenderingLinks

##### [Get Links.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/links/methods/create)

POST/accounts/{account_id}/browser-rendering/links

#### Browser RenderingMarkdown

##### [Get markdown.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/markdown/methods/create)

POST/accounts/{account_id}/browser-rendering/markdown

#### Browser RenderingAccessibility Tree

##### [Get accessibility tree page](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/accessibility_tree/methods/create)

POST/accounts/{account_id}/browser-rendering/accessibilityTree

#### Browser RenderingCrawl

##### [Crawl websites.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/crawl/methods/create)

POST/accounts/{account_id}/browser-rendering/crawl

##### [Get crawl result.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/crawl/methods/get)

GET/accounts/{account_id}/browser-rendering/crawl/{job_id}

##### [Cancel a crawl job.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/crawl/methods/delete)

DELETE/accounts/{account_id}/browser-rendering/crawl/{job_id}

#### Browser RenderingDevtools

#### Browser RenderingDevtoolsSession

##### [List sessions.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/session/methods/list)

GET/accounts/{account_id}/browser-rendering/devtools/session

##### [Get session details.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/session/methods/get)

GET/accounts/{account_id}/browser-rendering/devtools/session/{session_id}

#### Browser RenderingDevtoolsBrowser

##### [Get a browser session ID.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/browser/methods/create)

POST/accounts/{account_id}/browser-rendering/devtools/browser

##### [Close browser session.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/browser/methods/delete)

DELETE/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}

##### [Get browser version metadata.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/browser/methods/version)

GET/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/json/version

##### [Get Chrome DevTools Protocol schema.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/browser/methods/protocol)

GET/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/json/protocol

#### Browser RenderingDevtoolsBrowserLive View

##### [Mint live view URLs for a browser session](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/browser/subresources/live_view/methods/create)

POST/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/live_view

#### Browser RenderingDevtoolsBrowserPage

#### Browser RenderingDevtoolsBrowserTargets

##### [Open a new browser tab.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/browser/subresources/targets/methods/create)

PUT/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/json/new

##### [List targets.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/browser/subresources/targets/methods/list)

GET/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/json/list

##### [Get a target by ID.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/browser/subresources/targets/methods/get)

GET/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/json/list/{target_id}

##### [Activate a browser target.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/browser/subresources/targets/methods/activate)

GET/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/json/activate/{target_id}

##### [Close a browser target.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/browser/subresources/targets/methods/close)

GET/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/json/close/{target_id}

#### Custom Pages

##### [List custom pages](https://developers.cloudflare.com/api/resources/custom_pages/methods/list)

GET/{accounts_or_zones}/{account_or_zone_id}/custom_pages

##### [Get a custom page](https://developers.cloudflare.com/api/resources/custom_pages/methods/get)

GET/{accounts_or_zones}/{account_or_zone_id}/custom_pages/{identifier}

##### [Update a custom page](https://developers.cloudflare.com/api/resources/custom_pages/methods/update)

PUT/{accounts_or_zones}/{account_or_zone_id}/custom_pages/{identifier}

#### Custom PagesAssets

##### [List custom assets](https://developers.cloudflare.com/api/resources/custom_pages/subresources/assets/methods/list)

GET/{accounts_or_zones}/{account_or_zone_id}/custom_pages/assets

##### [Get a custom asset](https://developers.cloudflare.com/api/resources/custom_pages/subresources/assets/methods/get)

GET/{accounts_or_zones}/{account_or_zone_id}/custom_pages/assets/{asset_name}

##### [Create a custom asset](https://developers.cloudflare.com/api/resources/custom_pages/subresources/assets/methods/create)

POST/{accounts_or_zones}/{account_or_zone_id}/custom_pages/assets

##### [Update a custom asset](https://developers.cloudflare.com/api/resources/custom_pages/subresources/assets/methods/update)

PUT/{accounts_or_zones}/{account_or_zone_id}/custom_pages/assets/{asset_name}

##### [Delete a custom asset](https://developers.cloudflare.com/api/resources/custom_pages/subresources/assets/methods/delete)

DELETE/{accounts_or_zones}/{account_or_zone_id}/custom_pages/assets/{asset_name}

#### Secrets Store

#### Secrets StoreStores

##### [List account stores](https://developers.cloudflare.com/api/resources/secrets_store/subresources/stores/methods/list)

GET/accounts/{account_id}/secrets_store/stores

##### [Get a store by ID](https://developers.cloudflare.com/api/resources/secrets_store/subresources/stores/methods/get)

GET/accounts/{account_id}/secrets_store/stores/{store_id}

##### [Create a store](https://developers.cloudflare.com/api/resources/secrets_store/subresources/stores/methods/create)

POST/accounts/{account_id}/secrets_store/stores

##### [Delete a store](https://developers.cloudflare.com/api/resources/secrets_store/subresources/stores/methods/delete)

DELETE/accounts/{account_id}/secrets_store/stores/{store_id}

#### Secrets StoreStoresSecrets

##### [List store secrets](https://developers.cloudflare.com/api/resources/secrets_store/subresources/stores/subresources/secrets/methods/list)

GET/accounts/{account_id}/secrets_store/stores/{store_id}/secrets

##### [Get a secret by ID](https://developers.cloudflare.com/api/resources/secrets_store/subresources/stores/subresources/secrets/methods/get)

GET/accounts/{account_id}/secrets_store/stores/{store_id}/secrets/{secret_id}

##### [Create a secret](https://developers.cloudflare.com/api/resources/secrets_store/subresources/stores/subresources/secrets/methods/create)

POST/accounts/{account_id}/secrets_store/stores/{store_id}/secrets

##### [Patch a secret](https://developers.cloudflare.com/api/resources/secrets_store/subresources/stores/subresources/secrets/methods/edit)

PATCH/accounts/{account_id}/secrets_store/stores/{store_id}/secrets/{secret_id}

##### [Delete a secret](https://developers.cloudflare.com/api/resources/secrets_store/subresources/stores/subresources/secrets/methods/delete)

DELETE/accounts/{account_id}/secrets_store/stores/{store_id}/secrets/{secret_id}

##### [Delete secrets](https://developers.cloudflare.com/api/resources/secrets_store/subresources/stores/subresources/secrets/methods/bulk_delete)

DELETE/accounts/{account_id}/secrets_store/stores/{store_id}/secrets

##### [Duplicate Secret](https://developers.cloudflare.com/api/resources/secrets_store/subresources/stores/subresources/secrets/methods/duplicate)

POST/accounts/{account_id}/secrets_store/stores/{store_id}/secrets/{secret_id}/duplicate

#### Secrets StoreQuota

##### [View secret usage](https://developers.cloudflare.com/api/resources/secrets_store/subresources/quota/methods/get)

GET/accounts/{account_id}/secrets_store/quota

#### Pipelines

##### [[DEPRECATED] List Pipelines](https://developers.cloudflare.com/api/resources/pipelines/methods/list)

Deprecated

GET/accounts/{account_id}/pipelines

##### [[DEPRECATED] Get Pipeline](https://developers.cloudflare.com/api/resources/pipelines/methods/get)

Deprecated

GET/accounts/{account_id}/pipelines/{pipeline_name}

##### [[DEPRECATED] Create Pipeline](https://developers.cloudflare.com/api/resources/pipelines/methods/create)

Deprecated

POST/accounts/{account_id}/pipelines

##### [[DEPRECATED] Update Pipeline](https://developers.cloudflare.com/api/resources/pipelines/methods/update)

Deprecated

PUT/accounts/{account_id}/pipelines/{pipeline_name}

##### [[DEPRECATED] Delete Pipeline](https://developers.cloudflare.com/api/resources/pipelines/methods/delete)

Deprecated

DELETE/accounts/{account_id}/pipelines/{pipeline_name}

##### [List Pipelines](https://developers.cloudflare.com/api/resources/pipelines/methods/list_v1)

GET/accounts/{account_id}/pipelines/v1/pipelines

##### [Get Pipeline Details](https://developers.cloudflare.com/api/resources/pipelines/methods/get_v1)

GET/accounts/{account_id}/pipelines/v1/pipelines/{pipeline_id}

##### [Create Pipeline](https://developers.cloudflare.com/api/resources/pipelines/methods/create_v1)

POST/accounts/{account_id}/pipelines/v1/pipelines

##### [Delete Pipeline](https://developers.cloudflare.com/api/resources/pipelines/methods/delete_v1)

DELETE/accounts/{account_id}/pipelines/v1/pipelines/{pipeline_id}

##### [Validate SQL](https://developers.cloudflare.com/api/resources/pipelines/methods/validate_sql)

POST/accounts/{account_id}/pipelines/v1/validate_sql

#### PipelinesSinks

##### [List Sinks](https://developers.cloudflare.com/api/resources/pipelines/subresources/sinks/methods/list)

GET/accounts/{account_id}/pipelines/v1/sinks

##### [Get Sink Details](https://developers.cloudflare.com/api/resources/pipelines/subresources/sinks/methods/get)

GET/accounts/{account_id}/pipelines/v1/sinks/{sink_id}

##### [Create Sink](https://developers.cloudflare.com/api/resources/pipelines/subresources/sinks/methods/create)

POST/accounts/{account_id}/pipelines/v1/sinks

##### [Delete Sink](https://developers.cloudflare.com/api/resources/pipelines/subresources/sinks/methods/delete)

DELETE/accounts/{account_id}/pipelines/v1/sinks/{sink_id}

#### PipelinesStreams

##### [List Streams](https://developers.cloudflare.com/api/resources/pipelines/subresources/streams/methods/list)

GET/accounts/{account_id}/pipelines/v1/streams

##### [Get Stream Details](https://developers.cloudflare.com/api/resources/pipelines/subresources/streams/methods/get)

GET/accounts/{account_id}/pipelines/v1/streams/{stream_id}

##### [Create Stream](https://developers.cloudflare.com/api/resources/pipelines/subresources/streams/methods/create)

POST/accounts/{account_id}/pipelines/v1/streams

##### [Update Stream](https://developers.cloudflare.com/api/resources/pipelines/subresources/streams/methods/update)

PATCH/accounts/{account_id}/pipelines/v1/streams/{stream_id}

##### [Delete Stream](https://developers.cloudflare.com/api/resources/pipelines/subresources/streams/methods/delete)

DELETE/accounts/{account_id}/pipelines/v1/streams/{stream_id}

#### K2

#### K2Streams

##### [List K2 streams](https://developers.cloudflare.com/api/resources/k2/subresources/streams/methods/list)

GET/accounts/{account_id}/k2/streams

##### [Get K2 stream](https://developers.cloudflare.com/api/resources/k2/subresources/streams/methods/get)

GET/accounts/{account_id}/k2/streams/{stream_id}

##### [Create K2 stream](https://developers.cloudflare.com/api/resources/k2/subresources/streams/methods/create)

POST/accounts/{account_id}/k2/streams

##### [Update K2 stream](https://developers.cloudflare.com/api/resources/k2/subresources/streams/methods/update)

PATCH/accounts/{account_id}/k2/streams/{stream_id}

##### [Delete K2 stream](https://developers.cloudflare.com/api/resources/k2/subresources/streams/methods/delete)

DELETE/accounts/{account_id}/k2/streams/{stream_id}

#### K2StreamsSubscriptions

##### [List K2 stream subscriptions](https://developers.cloudflare.com/api/resources/k2/subresources/streams/subresources/subscriptions/methods/list)

GET/accounts/{account_id}/k2/streams/{stream_id}/subscriptions

#### Schema Validation

#### Schema ValidationSchemas

##### [List all uploaded schemas](https://developers.cloudflare.com/api/resources/schema_validation/subresources/schemas/methods/list)

GET/zones/{zone_id}/schema_validation/schemas

##### [Get details of a schema](https://developers.cloudflare.com/api/resources/schema_validation/subresources/schemas/methods/get)

GET/zones/{zone_id}/schema_validation/schemas/{schema_id}

##### [Upload a schema](https://developers.cloudflare.com/api/resources/schema_validation/subresources/schemas/methods/create)

POST/zones/{zone_id}/schema_validation/schemas

##### [Set schema validation state](https://developers.cloudflare.com/api/resources/schema_validation/subresources/schemas/methods/edit)

PATCH/zones/{zone_id}/schema_validation/schemas/{schema_id}

##### [Delete a schema](https://developers.cloudflare.com/api/resources/schema_validation/subresources/schemas/methods/delete)

DELETE/zones/{zone_id}/schema_validation/schemas/{schema_id}

#### Schema ValidationSettings

##### [Get global schema validation settings](https://developers.cloudflare.com/api/resources/schema_validation/subresources/settings/methods/get)

GET/zones/{zone_id}/schema_validation/settings

##### [Update global schema validation settings](https://developers.cloudflare.com/api/resources/schema_validation/subresources/settings/methods/update)

PUT/zones/{zone_id}/schema_validation/settings

##### [Edit global schema validation settings](https://developers.cloudflare.com/api/resources/schema_validation/subresources/settings/methods/edit)

PATCH/zones/{zone_id}/schema_validation/settings

#### Schema ValidationSettingsOperations

##### [List per-operation schema validation settings](https://developers.cloudflare.com/api/resources/schema_validation/subresources/settings/subresources/operations/methods/list)

GET/zones/{zone_id}/schema_validation/settings/operations

##### [Get per-operation schema validation setting](https://developers.cloudflare.com/api/resources/schema_validation/subresources/settings/subresources/operations/methods/get)

GET/zones/{zone_id}/schema_validation/settings/operations/{operation_id}

##### [Update per-operation schema validation setting](https://developers.cloudflare.com/api/resources/schema_validation/subresources/settings/subresources/operations/methods/update)

PUT/zones/{zone_id}/schema_validation/settings/operations/{operation_id}

##### [Bulk edit per-operation schema validation settings](https://developers.cloudflare.com/api/resources/schema_validation/subresources/settings/subresources/operations/methods/bulk_edit)

PATCH/zones/{zone_id}/schema_validation/settings/operations

##### [Delete per-operation schema validation setting](https://developers.cloudflare.com/api/resources/schema_validation/subresources/settings/subresources/operations/methods/delete)

DELETE/zones/{zone_id}/schema_validation/settings/operations/{operation_id}

#### Token Validation

#### Token ValidationConfiguration

##### [List token validation configurations](https://developers.cloudflare.com/api/resources/token_validation/subresources/configuration/methods/list)

GET/zones/{zone_id}/token_validation/config

##### [Get a token validation configuration](https://developers.cloudflare.com/api/resources/token_validation/subresources/configuration/methods/get)

GET/zones/{zone_id}/token_validation/config/{config_id}

##### [Create a token validation configuration](https://developers.cloudflare.com/api/resources/token_validation/subresources/configuration/methods/create)

POST/zones/{zone_id}/token_validation/config

##### [Edit a token validation configuration](https://developers.cloudflare.com/api/resources/token_validation/subresources/configuration/methods/edit)

PATCH/zones/{zone_id}/token_validation/config/{config_id}

##### [Delete a token validation configuration](https://developers.cloudflare.com/api/resources/token_validation/subresources/configuration/methods/delete)

DELETE/zones/{zone_id}/token_validation/config/{config_id}

#### Token ValidationConfigurationCredentials

##### [Replace token validation credentials](https://developers.cloudflare.com/api/resources/token_validation/subresources/configuration/subresources/credentials/methods/update)

PUT/zones/{zone_id}/token_validation/config/{config_id}/credentials

##### [Edit token validation credentials](https://developers.cloudflare.com/api/resources/token_validation/subresources/configuration/subresources/credentials/methods/edit)

PATCH/zones/{zone_id}/token_validation/config/{config_id}/credentials

#### Token ValidationRules

##### [List token validation rules](https://developers.cloudflare.com/api/resources/token_validation/subresources/rules/methods/list)

GET/zones/{zone_id}/token_validation/rules

##### [Create a token validation rule](https://developers.cloudflare.com/api/resources/token_validation/subresources/rules/methods/create)

POST/zones/{zone_id}/token_validation/rules

##### [Create token validation rules](https://developers.cloudflare.com/api/resources/token_validation/subresources/rules/methods/bulk_create)

POST/zones/{zone_id}/token_validation/rules/bulk

##### [Edit token validation rules](https://developers.cloudflare.com/api/resources/token_validation/subresources/rules/methods/bulk_edit)

PATCH/zones/{zone_id}/token_validation/rules/bulk

##### [Get a token validation rule](https://developers.cloudflare.com/api/resources/token_validation/subresources/rules/methods/get)

GET/zones/{zone_id}/token_validation/rules/{rule_id}

##### [Delete a token validation rule](https://developers.cloudflare.com/api/resources/token_validation/subresources/rules/methods/delete)

DELETE/zones/{zone_id}/token_validation/rules/{rule_id}

##### [Edit a token validation rule](https://developers.cloudflare.com/api/resources/token_validation/subresources/rules/methods/edit)

PATCH/zones/{zone_id}/token_validation/rules/{rule_id}

#### Field Extractors

##### [Get Field Extractor](https://developers.cloudflare.com/api/resources/field_extractors/methods/get)

GET/accounts/{account_id}/field_extractors/{extractor}

##### [Update Field Extractor](https://developers.cloudflare.com/api/resources/field_extractors/methods/update)

PUT/accounts/{account_id}/field_extractors/{extractor}

##### [Delete Field Extractor](https://developers.cloudflare.com/api/resources/field_extractors/methods/delete)

DELETE/accounts/{account_id}/field_extractors/{extractor}
