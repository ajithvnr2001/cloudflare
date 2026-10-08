---
url: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/delegated-dcv/
title: Delegated domain control validation (DCV) \u00b7 Cloudflare for Platforms docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:03.082827+00:00
---

# Delegated domain control validation (DCV) · Cloudflare for Platforms docs

> Source: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/delegated-dcv/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/)
  3. /…

[Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/)[Security](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/)[Certificate management](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/)Issue and validate certificates

  4. /[Validate](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/)
  5. /Delegated



# Delegated

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/delegated-dcv/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSetupMoved domains

Delegated DCV allows SaaS providers to delegate the DCV process to Cloudflare.

DCV Delegation requires your customers to place a one-time record at their authoritative DNS that allows Cloudflare to auto-renew all future certificate orders, so that there is no manual intervention from you or your customers at the time of the renewal.

* * *

## Setup

To set up Delegated DCV:

  1. Add a [custom hostname](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/create-custom-hostnames/) for your zone, choosing `TXT` as the **Certificate validation method**.
  2. On the [**Custom Hostnames** ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/custom-hostnames) page, go to **DCV Delegation for Custom Hostnames**.
  3. Copy the hostname value.
  4. For each hostname, the domain owner needs to place a `CNAME` record at their authoritative DNS. In this example, the SaaS zone is `example.com`. 
         
         _acme-challenge.example.com CNAME example.com.<COPIED_HOSTNAME>.




Once this is complete, Cloudflare will place two TXT DCV records - one for `example.com` and one for `*.example.com` \- at the `example.com.<COPIED_HOSTNAME>` hostname. The CNAME record will need to stay in place in order to allow Cloudflare to continue placing the records for the renewals.

If desired, you could also manually fetch the DCV tokens and share them with your customers.

Remove conflicting `_acme-challenge` TXT records

Existing `_acme-challenge` TXT records will prevent delegated DCV from functioning. Before setting up delegated DCV, check for and remove any records in this form from your customer's authoritative DNS:
    
    
    _acme-challenge.example.com TXT <CERTIFICATE_VALIDATION_VALUE>

This includes records that Cloudflare may have placed automatically during a previous certificate order or Universal SSL issuance. If your customer's domain is also present in a direct Cloudflare zone (for example, they proxy `example.com` through their own Cloudflare account), check that zone's DNS records for any `_acme-challenge` entries and remove them.

To check whether the delegation CNAME is in place, run:
    
    
    dig _acme-challenge.example.com CNAME +short

If this returns nothing, the delegation CNAME is not present — add it before proceeding.

If the CNAME is in place but certificate validation is still stuck, a conflicting `_acme-challenge` TXT record may exist inside your customer's direct Cloudflare zone. Because resolvers follow the CNAME chain rather than exposing records at the source name, the only way to confirm this is to inspect the customer's zone directly: go to **DNS** > **Records** in the Cloudflare dashboard for their zone and look for any `_acme-challenge` TXT entries. Refer to [Troubleshooting](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/troubleshooting/#conflicting-_acme-challenge-txt-records) for remediation steps.

## Moved domains

If you [move your SaaS zone to another account](https://developers.cloudflare.com/fundamentals/manage-domains/move-domain/), you will need to update the `CNAME` record with a new hostname value.

[PreviousOverview](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/)[NextTXT](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/txt/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/delegated-dcv.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
