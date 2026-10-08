---
url: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/
title: Validate certificates \u00b7 Cloudflare for Platforms docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:02.967636+00:00
---

# Validate certificates · Cloudflare for Platforms docs

> Source: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/)
  3. /…

[Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/)[Security](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/)[Certificate management](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/)

  4. /Issue and validate certificates
  5. /Validate



# Validate

Last updated May 7, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewDCV situations Non-wildcard certificates Wildcard certificates Minimize downtime Minimize customer effortPotential issues

Before a certificate authority (CA) will issue a certificate for a domain, the requester must prove they have control over that domain. This process is known as domain control validation (DCV).

  


When you [create a custom hostname](https://developers.cloudflare.com/api/resources/custom_hostnames/methods/create/), choose one certificate validation method. The API accepts one `ssl.method` value: `http`, `txt`, or `email`.

## DCV situations

### Non-wildcard certificates

Specific (non-wildcard) custom hostnames can use [HTTP based DCV](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/http/) for certificate renewals, as long as:

  * The hostname is pointing to the SaaS provider.
  * The hostname's traffic is proxying through the Cloudflare network.



If your custom hostnames do not meet these requirements, use another validation method.

### Wildcard certificates

Wildcard custom hostnames require TXT-based validation. As the SaaS provider, you have two options for wildcard custom hostname certificate renewals:

  


  * [DCV Delegation](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/delegated-dcv/) (auto-issuance)
  * [Manual](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/txt/)



### Minimize downtime

If you want to minimize downtime, explore one of the following methods to issue and deploy the certificate before onboarding your customers:

  * [Delegated DCV](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/delegated-dcv/): Place a one-time record at your authoritative DNS that allows Cloudflare to auto-renew all future certificate orders.
  * [TXT validation](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/txt/): Have your customers add a `TXT` record to their authoritative DNS.
  * [Manual HTTP validation](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/http/#http-manual): Add a `TXT` record at your origin.



### Minimize customer effort

If you value simplicity and your customers can handle a few minutes of downtime, you can rely on Cloudflare [automatic HTTP validation](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/http/#http-automatic).

Automatic HTTP validation requires the hostname to point to your SaaS target before the CA can fetch the validation token. During that period, the hostname may route to Cloudflare before the certificate reaches `ssl.status: active`.

## Potential issues

To avoid or solve potential issues, refer to our [troubleshooting guide](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/troubleshooting/).

[PreviousIssue](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/issue-certificates/)[NextDelegated](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/delegated-dcv/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
