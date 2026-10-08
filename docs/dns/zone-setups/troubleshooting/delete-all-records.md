---
url: https://developers.cloudflare.com/dns/zone-setups/troubleshooting/delete-all-records/
title: Delete all DNS records \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:04.009927+00:00
---

# Delete all DNS records · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/zone-setups/troubleshooting/delete-all-records/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /…

[DNS setups](https://developers.cloudflare.com/dns/zone-setups/)

  4. /Troubleshooting
  5. /Delete all DNS records



# Delete all DNS records

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dns/zone-setups/troubleshooting/delete-all-records/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

When you connect your domain to Cloudflare, the [DNS records quick scan](https://developers.cloudflare.com/dns/zone-setups/reference/dns-quick-scan/) may automatically add several records to your zone.

If you realize most of them are not applicable and want to bulk delete DNS records, follow the steps below. This method assumes you are familiar with [API calls fundamentals](https://developers.cloudflare.com/fundamentals/api/).

Bulk deletion available in the dashboard

You can delete records in bulk via the dashboard, which removes the need for custom scripts as the one below. Refer to [Batch record changes](https://developers.cloudflare.com/dns/manage-dns-records/how-to/batch-record-changes/#delete-records-in-bulk) for details.

  1. Make sure you have [an API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) that allows you to edit DNS for your zone.
  2. Get your [zone ID](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/).
  3. Run the following script, replacing `<ZONE_ID>` and `<API_TOKEN>` with the values you got from the previous steps.



Warning

This script uses [jq ↗︎](https://jqlang.github.io/jq/) to format `JSON` outputs for readability. Refer to [Make API calls](https://developers.cloudflare.com/fundamentals/api/how-to/make-api-calls/) for details.
    
    
    zoneid=<ZONE_ID>
    bearer=<API_TOKEN>
    curl --silent "https://api.cloudflare.com/client/v4/zones/$zoneid/dns_records?per_page=50000" \
    --header "Authorization: Bearer $bearer" \
    | jq --raw-output '.result[].id' | while read id
    do
      curl --silent --request DELETE "https://api.cloudflare.com/client/v4/zones/$zoneid/dns_records/$id" \
    --header "Authorization: Bearer $bearer"
    done

[PreviousCannot add domain](https://developers.cloudflare.com/dns/zone-setups/troubleshooting/cannot-add-domain/)[NextDomain deleted from Cloudflare](https://developers.cloudflare.com/dns/zone-setups/troubleshooting/domain-deleted/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/zone-setups/troubleshooting/delete-all-records.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
