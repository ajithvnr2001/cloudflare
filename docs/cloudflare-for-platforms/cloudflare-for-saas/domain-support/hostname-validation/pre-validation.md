---
url: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/pre-validation/
title: Pre-validation methods - Custom Hostname Validation \u00b7 Cloudflare for Platforms docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:59.836207+00:00
---

# Pre-validation methods - Custom Hostname Validation · Cloudflare for Platforms docs

> Source: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/pre-validation/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/)
  3. /…

[Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/)[Custom hostnames](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/)

  4. /[Hostname validation](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/)
  5. /Pre-validation



# Pre-validation

Last updated Jun 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/pre-validation/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUse whenHow to TXT records HTTP tokensZero-downtime migration with HTTP DCV

Pre-validation methods help verify domain ownership before your customer's traffic is proxying through Cloudflare.

Not supported for O2O custom hostnames

Pre-validation (TXT and HTTP token methods) is not supported when the custom hostname belongs to a zone that is already on Cloudflare — also known as an [Orange-to-Orange (O2O)](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/how-it-works/) setup.

In an O2O setup, the customer's authoritative DNS is already on Cloudflare, so there is no separate cutover step from a non-Cloudflare provider to Cloudflare. Activating the custom hostname immediately routes traffic through the SaaS zone, which means pre-validation tokens cannot be used to verify ownership ahead of the cutover. For these custom hostnames, use a [real-time validation method](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/realtime-validation/) instead.

## Use when

Use pre-validation methods when your customers cannot tolerate any downtime, which often occurs with production domains.

The downside is that these methods require an additional setup step for your customers. Especially if you already need them to add something to their domain for [certificate validation](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/), pre-validation might make their onboarding more complicated.

If your customers can tolerate a bit of downtime and you want their setup to be simpler, review our [real-time validation methods](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/realtime-validation/).

## How to

### TXT records

TXT validation is when your customer adds a `TXT` record to their authoritative DNS to verify domain ownership.

Note

If your customer cannot update their authoritative DNS, you could also use HTTP validation.

To set up `TXT` validation:

  1. When you [create a custom hostname](https://developers.cloudflare.com/api/resources/custom_hostnames/methods/create/), save the `ownership_verification` information.
         
         {
         "result": [
             {
             "id": "3537a672-e4d8-4d89-aab9-26cb622918a1",
             "hostname": "app.example.com",
             // ...
             "status": "pending",
             "verification_errors": ["custom hostname does not CNAME to this zone."],
             "ownership_verification": {
                 "type": "txt",
                 "name": "_cf-custom-hostname.app.example.com",
                 "value": "0e2d5a7f-1548-4f27-8c05-b577cb14f4ec"
             },
             "created_at": "2020-03-04T19:04:02.705068Z"
             }
         ]
         }

  2. Have your customer add a `TXT` record with that `name` and `value` at their authoritative DNS provider.

  3. After a few minutes, you will see the hostname status become **Active** in the UI.

  4. Once you activate the custom hostname, your customer can remove the `TXT` record.




### HTTP tokens

HTTP validation is when you or your customer places an HTTP token on their origin server to verify domain ownership.

To set up HTTP validation:

When you [create a custom hostname](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/issue-certificates/) using the API, Cloudflare provides an HTTP `ownership_verification` record in the response.

To get and use the `ownership_verification` record:

  1. Make an API call to [create a Custom Hostname](https://developers.cloudflare.com/api/resources/custom_hostnames/methods/create/).

  2. In the response, copy the `http_url` and `http_body` from the `ownership_verification_http` object:

Example response (truncated)json
         
         {
           "result": [
             {
               "id": "24c8c68e-bec2-49b6-868e-f06373780630",
               "hostname": "app.example.com",
               // ...
               "ownership_verification_http": {
                   "http_url": "http://app.example.com/.well-known/cf-custom-hostname-challenge/24c8c68e-bec2-49b6-868e-f06373780630",
                   "http_body": "48b409f6-c886-406b-8cbc-0fbf59983555"
               },
               "created_at": "2020-03-04T20:06:04.117122Z"
             }
           ]
         }

  3. Have your customer place the `http_url` and `http_body` on their origin web server.

Example response (truncated)txt
         
         location "/.well-known/cf-custom-hostname-challenge/24c8c68e-bec2-49b6-868e-f06373780630" {
             return 200 "48b409f6-c886-406b-8cbc-0fbf59983555\n";
         }

Cloudflare will access this token by sending `GET` requests to the `http_url` using `User-Agent: Cloudflare Custom Hostname Verification`.

Note

If you can serve these tokens on behalf of your customers, you can simplify their overall setup.

  4. After a few minutes, you will see the hostname status become **Active** in the UI.

  5. Once the hostname is active, your customer can remove the token from their origin server.




## Zero-downtime migration with HTTP DCV

When onboarding a customer whose hostname is already live with another provider, you can use pre-validation combined with manual HTTP DCV to achieve zero-downtime migration:

  1. Create the custom hostname with `"ssl": {"method": "http", "type": "dv"}`.
  2. Complete hostname ownership pre-validation using a TXT record so the hostname reaches `status: active`.
  3. Wait for the `ssl.validation_records` to populate with the HTTP DCV token (an `http_url` and `http_body` pair).
  4. Ask your customer to serve the DCV token at the `http_url` path on their current live origin. The certificate authority will validate it against the current DNS target.
  5. Once `ssl.status` reaches `active`, the hostname and certificate are both ready.
  6. Your customer can now update their DNS CNAME to point to your SaaS target with no interruption — the certificate is already issued.



Note

The HTTP DCV token is single-use and must be served before it expires. Refer to [DCV tokens validity](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/validation-backoff-schedule/#dcv-tokens-validity) for expiration periods by certificate authority.

[PreviousOverview](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/)[NextReal-time validation](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/realtime-validation/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/pre-validation.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
