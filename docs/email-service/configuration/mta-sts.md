---
url: https://developers.cloudflare.com/email-service/configuration/mta-sts/
title: Configure MTA-STS \u00b7 Cloudflare Email Service docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:12.871943+00:00
---

# Configure MTA-STS · Cloudflare Email Service docs

> Source: https://developers.cloudflare.com/email-service/configuration/mta-sts/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Email Service](https://developers.cloudflare.com/email-service/)
  3. /Configuration
  4. /Configure MTA-STS



# Configure MTA-STS

Last updated Jun 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/email-service/configuration/mta-sts/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAdd the _mta-sts DNS recordServe the policy fileNext steps

MTA Strict Transport Security ([MTA-STS ↗︎](https://datatracker.ietf.org/doc/html/rfc8461)) was introduced by email service providers including Microsoft, Google and Yahoo as a solution to protect against downgrade and man-in-the-middle attacks in SMTP sessions, as well as solving the lack of security-first communication standards in email.

Suppose that `example.com` is your domain and uses Email Service. Here is how you can enable MTA-STS for it.

## Add the `_mta-sts` DNS record

  1. In the Cloudflare dashboard, go to the **Records** page.

[ Go to **Records** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/dns/records)
  2. Create a new CNAME record with the name `_mta-sts` that points to Cloudflare's record `_mta-sts.mx.cloudflare.net`. Make sure to disable the proxy mode.

![MTA-STS CNAME record](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1862,height=304,format=webp/_astro/mta-sts-record.DbwO-t_X.png)
  3. Confirm that the record was created:
         
         dig txt _mta-sts.example.com
         
         _mta-sts.example.com. 300 IN  CNAME _mta-sts.mx.cloudflare.net.
         _mta-sts.mx.cloudflare.net. 300 IN  TXT "v=STSv1; id=20230615T153000;"

This tells the other end client that is trying to connect to us that we support MTA-STS.




## Serve the policy file

Next you need an HTTPS endpoint at `mta-sts.example.com` to serve your policy file. This file defines the mail servers in the domain that use MTA-STS. The reason why HTTPS is used here instead of DNS is because not everyone uses DNSSEC yet, so we want to avoid another MITM attack vector.

To do this you need to deploy a Worker that allows email clients to pull Cloudflare's Email Service policy file using the "well-known" URI convention.

  1. Deploy the MTA-STS proxy Worker to your account:

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/mta-sts-proxy)

This Worker proxies `https://mta-sts.mx.cloudflare.net/.well-known/mta-sts.txt` to your own domain.

  2. After deploying it, go to the Worker configuration, then **Settings** > **Domains & Routes** > **+Add**. Type the subdomain `mta-sts.example.com`.

![MTA-STS Worker Custom Domain](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1999,height=1148,format=webp/_astro/mta-sts-domain.UfZmAoBe.png)

You can then confirm that your policy file is working with the following:
         
         curl https://mta-sts.example.com/.well-known/mta-sts.txt
         
         version: STSv1
         mode: enforce
         mx: *.mx.cloudflare.net
         max_age: 86400

This says that you domain `example.com` enforces MTA-STS. Capable email clients will only deliver email to this domain over a secure connection to the specified MX servers. If no secure connection can be established the email will not be delivered.

Test before enforcing

A misconfigured policy in `enforce` mode causes legitimate inbound mail to be rejected. When rolling out MTA-STS on an existing domain, start with `mode: testing` and monitor [TLS-RPT ↗︎](https://datatracker.ietf.org/doc/html/rfc8460) reports for a few weeks before switching to `enforce`.




Email Service also supports MTA-STS upstream, which greatly improves security when forwarding your emails to service providers like Gmail, Microsoft, and others.

## Next steps

  * [Email authentication](https://developers.cloudflare.com/email-service/concepts/email-authentication/) — SPF, DKIM, and DMARC reference.
  * [Postmaster](https://developers.cloudflare.com/email-service/reference/postmaster/) — TLS, ARC, and SMTP details for postmasters.
  * [Domain configuration](https://developers.cloudflare.com/email-service/configuration/domains/) — review your domain's DNS records.



[PreviousSubdomains](https://developers.cloudflare.com/email-service/configuration/subdomains/)[NextConfigure send bindings](https://developers.cloudflare.com/email-service/configuration/send-bindings/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/email-service/configuration/mta-sts.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
