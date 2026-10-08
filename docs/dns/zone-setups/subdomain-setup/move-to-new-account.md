---
url: https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/move-to-new-account/
title: Migrate subdomain to a new account \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:04.398967+00:00
---

# Migrate subdomain to a new account · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/move-to-new-account/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /…

[DNS setups](https://developers.cloudflare.com/dns/zone-setups/)

  4. /[Subdomain setup](https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/)
  5. /Migrate to new account



# Migrate to new account

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/move-to-new-account/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

When using a [subdomain setup](https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/), you can have your subdomain as a separate zone within the same account as the parent domain or within a different account.

If you have already [created a standalone subdomain zone](https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/setup/) within the same account, you can still move it to a separate account.

  1. [Add the subdomain](https://developers.cloudflare.com/fundamentals/manage-domains/add-site/) to a new Cloudflare account.
  2. In the original subdomain zone, [export](https://developers.cloudflare.com/dns/manage-dns-records/how-to/import-and-export/#export-records) the DNS records.
  3. Review the exported records, delete any unnecessary ones, and [import](https://developers.cloudflare.com/dns/manage-dns-records/how-to/import-and-export/#import-records) them into the new subdomain zone.
  4. Update the `NS` records in the parent zone to refer to the newly assigned nameservers of the child zone.



[PreviousEnable DNSSEC](https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/dnssec/)[NextRollback](https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/rollback/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/zone-setups/subdomain-setup/move-to-new-account.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
