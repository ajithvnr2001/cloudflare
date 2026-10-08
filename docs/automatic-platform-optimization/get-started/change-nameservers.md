---
url: https://developers.cloudflare.com/automatic-platform-optimization/get-started/change-nameservers/
title: Change nameservers \u00b7 Cloudflare Automatic Platform Optimization docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:22.041675+00:00
---

# Change nameservers · Cloudflare Automatic Platform Optimization docs

> Source: https://developers.cloudflare.com/automatic-platform-optimization/get-started/change-nameservers/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Automatic Platform Optimization](https://developers.cloudflare.com/automatic-platform-optimization/)
  3. /[Get started](https://developers.cloudflare.com/automatic-platform-optimization/get-started/)
  4. /Change nameservers



# Change nameservers

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/automatic-platform-optimization/get-started/change-nameservers/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewLookup domain name registrationUpdate your nameserver with your domain registrar

After you [confirm your DNS records](https://developers.cloudflare.com/automatic-platform-optimization/get-started/confirm-dns-records/), change your nameservers.

Updating your domain to use Cloudflare's nameservers is a critical step to ensure Cloudflare can optimize and protect your site. Nameservers are your primary DNS controller and identify the location of your domain on the Internet.

Domain registrars can take up to 24 hours to process the nameserver updates. You will receive an email from Cloudflare once your site is activated.

## Lookup domain name registration

  1. Visit [WHOIS ↗︎](https://lookup.icann.org/) to look up your domain name registration.
  2. In the text field, enter your domain name without `https://www.` and select **Lookup**.
  3. From **Domain Information** , make note of the nameserver information that displays. You will update those nameservers to point to Cloudflare.



We recommend keeping this browser tab or window open and opening a new tab or window for the next section.

## Update your nameserver with your domain registrar

  1. Log in to the administrator account for your domain registrar.
  2. Navigate to DNS Management.
  3. Locate your nameserver information. Your nameservers should match the information from Step 3 of Lookup domain name registration.
  4. Replace the existing nameserver information with the Cloudflare nameservers from Step 4 of Create the custom nameserver with Cloudflare.



Note

You may be prompted to confirm the nameserver change with your domain registrar. Confirm or continue after making the update.

[PreviousConfirm DNS records](https://developers.cloudflare.com/automatic-platform-optimization/get-started/confirm-dns-records/)[NextActivate the Cloudflare WordPress plugin](https://developers.cloudflare.com/automatic-platform-optimization/get-started/activate-cf-wp-plugin/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/automatic-platform-optimization/get-started/change-nameservers.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
