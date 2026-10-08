---
url: https://developers.cloudflare.com/dns/zone-setups/full-setup/troubleshooting/
title: Troubleshooting primary setup (full) \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:03.306129+00:00
---

# Troubleshooting primary setup (full) · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/zone-setups/full-setup/troubleshooting/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /…

[DNS setups](https://developers.cloudflare.com/dns/zone-setups/)

  4. /[Primary setup (Full)](https://developers.cloudflare.com/dns/zone-setups/full-setup/)
  5. /Troubleshooting



# Troubleshooting

Last updated Jul 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dns/zone-setups/full-setup/troubleshooting/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewIs a DS record present at your registrar?Do the nameservers at your registrar exactly match the values provided by Cloudflare?Are additional nameservers listed at your registrar?Have you waited longer than 24 hours?

If you see unexpected results when [changing your nameservers](https://developers.cloudflare.com/dns/zone-setups/full-setup/setup/), review the following troubleshooting questions.

Note

If your zone is still in **Pending Nameserver Update** status, refer to [Zone stuck in Pending Nameserver Update](https://developers.cloudflare.com/dns/zone-setups/troubleshooting/pending-nameservers/) for a step-by-step check of the delegation at your registrar.

## Is a DS record present at your registrar?

You need to remove any pre-Cloudflare **DS** records at your registrar to update your authoritative nameservers. This will disable DNSSEC and allow Cloudflare to resolve your domain name.

You can then [re-enable DNSSEC](https://developers.cloudflare.com/dns/zone-setups/full-setup/setup/#4-re-enable-dnssec) in Cloudflare and at your registrar after you have changed your nameservers.

## Do the nameservers at your registrar exactly match the values provided by Cloudflare?

If the nameservers in your registrar do not exactly match those provided by Cloudflare, your domain will not resolve correctly.

## Are additional nameservers listed at your registrar?

If so, you should remove these nameservers.

You should have only Cloudflare nameservers listed at your registrar.

## Have you waited longer than 24 hours?

For some registrars, you will need to wait up to 24 hours for updates to your nameservers.

[PreviousSetup](https://developers.cloudflare.com/dns/zone-setups/full-setup/setup/)[NextAbout](https://developers.cloudflare.com/dns/zone-setups/partial-setup/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/zone-setups/full-setup/troubleshooting.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
