---
url: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/common-api-calls/
title: Common API Calls \u00b7 Cloudflare for Platforms docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:04.225994+00:00
---

# Common API Calls · Cloudflare for Platforms docs

> Source: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/common-api-calls/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/)
  3. /…

[Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/)

  4. /Get started
  5. /Common API Calls



# Common API Calls

Last updated May 7, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/common-api-calls/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCustom hostnames Confirm custom hostname readinessFallback origins

As a SaaS provider, you may want to configure and manage Cloudflare for SaaS [via the API](https://developers.cloudflare.com/api/) rather than the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/). Below are relevant API calls for creating, editing, and deleting custom hostnames, as well as monitoring, updating, and deleting fallback origins. Further details can be found in the [Cloudflare API documentation](https://developers.cloudflare.com/api/).

* * *

## Custom hostnames

Endpoint | Notes  
---|---  
[List custom hostnames](https://developers.cloudflare.com/api/resources/custom_hostnames/methods/list/) | Use the `page` parameter to pull additional pages. Add a `hostname` parameter to search for specific hostnames.  
[Create custom hostname](https://developers.cloudflare.com/api/resources/custom_hostnames/methods/create/) | In the `validation_records` object of the response, use the `txt_name` and `txt_record` listed to validate the custom hostname.  
[Custom hostname details](https://developers.cloudflare.com/api/resources/custom_hostnames/methods/get/) | Use this endpoint to check hostname activation and certificate status.  
[Edit custom hostname](https://developers.cloudflare.com/api/resources/custom_hostnames/methods/edit/) | When sent with an `ssl` object that matches the existing value, indicates that hostname should restart domain control validation (DCV).  
[Delete custom hostname](https://developers.cloudflare.com/api/resources/custom_hostnames/methods/delete/) | Also deletes any associated SSL/TLS certificates.  
  
### Confirm custom hostname readiness

To confirm that a custom hostname is fully configured, check both status fields in the [Custom hostname details endpoint](https://developers.cloudflare.com/api/resources/custom_hostnames/methods/get/) response:

API field | What it means | Ready value  
---|---|---  
`result.status` | Hostname activation status. This field shows whether Cloudflare has validated and activated the custom hostname. | `active`  
`result.ssl.status` | Certificate status. This field shows whether the hostname's SSL/TLS certificate has completed issuance and deployment. | `active`  
  
Treat the custom hostname as ready for production HTTPS when `result.status` is `active`, `result.ssl.status` is `active`, and the customer's DNS points to your CNAME target or apex proxying target.

If `result.status` is `active` but `result.ssl.status` is not `active`, the hostname is active but its certificate has not completed issuance and deployment. A successful TLS handshake alone does not mean the custom hostname certificate has finished provisioning because Cloudflare may present another matching certificate for that hostname. For more information, refer to [Certificate and hostname priority](https://developers.cloudflare.com/ssl/reference/certificate-and-hostname-priority/).

When you use the [Create custom hostname endpoint](https://developers.cloudflare.com/api/resources/custom_hostnames/methods/create/), choose one `ssl.method` value: `http`, `txt`, or `email`. For non-wildcard custom hostnames, Cloudflare always attempts [HTTP certificate validation](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/http/#non-wildcard-custom-hostnames) after the hostname points to your SaaS target, even if you selected **TXT** validation.

## Fallback origins

Our API includes the following endpoints related to the [fallback origin](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/#1-create-fallback-origin) of a custom hostname:

  * [Get fallback origin](https://developers.cloudflare.com/api/resources/custom_hostnames/subresources/fallback_origin/methods/get/)
  * [Update fallback origin](https://developers.cloudflare.com/api/resources/custom_hostnames/subresources/fallback_origin/methods/update/)
  * [Remove fallback origin](https://developers.cloudflare.com/api/resources/custom_hostnames/subresources/fallback_origin/methods/delete/)



[PreviousWorkers as your fallback origin](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/worker-as-origin/)[NextAbout](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-for-platforms/cloudflare-for-saas/start/common-api-calls.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
