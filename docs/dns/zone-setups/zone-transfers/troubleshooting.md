---
url: https://developers.cloudflare.com/dns/zone-setups/zone-transfers/troubleshooting/
title: Troubleshooting secondary nameservers \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:05.448770+00:00
---

# Troubleshooting secondary nameservers · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/zone-setups/zone-transfers/troubleshooting/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /…

[DNS setups](https://developers.cloudflare.com/dns/zone-setups/)

  4. /[DNS Zone transfers](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/)
  5. /Troubleshooting



# Troubleshooting

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/troubleshooting/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCauseSolution

When [updating your registrar](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/setup/#4-update-registrar) with the Cloudflare secondary nameservers (`nsXXXX.secondary.cloudflare.com`), you get an error.

Note

The exact error message depends on the system. Some examples would be: `Entity reference not found`,` Authorization error`, `Unable to create foreign nameserver`.

Upon contacting your registrar, their services confirm that the Cloudflare nameservers cannot be added at this time.

* * *

## Cause

This issue may arise when one of the Cloudflare nameservers used for secondary setup is removed from the Verisign side.

* * *

## Solution

The Cloudflare engineering team needs to be engaged [through Support](https://developers.cloudflare.com/support/contacting-cloudflare-support/) to make sure the nameserver gets registered again manually at Verisign.

[PreviousCreate ACL](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/access-control-lists/create-new-list/)[NextAbout](https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/zone-setups/zone-transfers/troubleshooting.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
