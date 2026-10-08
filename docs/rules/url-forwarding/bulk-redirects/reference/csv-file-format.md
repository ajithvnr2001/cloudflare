---
url: https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/csv-file-format/
title: CSV file format for Bulk Redirects \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:59.475311+00:00
---

# CSV file format for Bulk Redirects · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/csv-file-format/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Redirects](https://developers.cloudflare.com/rules/url-forwarding/)[Bulk Redirects](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/)

  4. /Reference
  5. /CSV file format



# CSV file format for Bulk Redirects

Last updated Jul 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/csv-file-format/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewExample CSV fileImportant remarks

You can use a CSV file to import URL redirects into a Bulk Redirect List [using the Cloudflare dashboard](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/create-dashboard/#1-create-a-bulk-redirect-list). Each line in the CSV file must follow this format:
    
    
    <SOURCE_URL>,<TARGET_URL>[,<STATUS_CODE>,<PRESERVE_QUERY_STRING>,<INCLUDE_SUBDOMAINS>,<SUBPATH_MATCHING>,<PRESERVE_PATH_SUFFIX>]

Only the `<SOURCE_URL>` and `<TARGET_URL>` values are mandatory. The default value of `<STATUS_CODE>` is `301` and the default value for all the boolean parameters is `FALSE`.

To enable one of the URL redirect parameters, use one of the following values: `TRUE` or `true`. To keep an option disabled, use one of `FALSE` or `false`, or enter a comma (delimiter) without entering any value.

## Example CSV file

All the lines in this example are valid lines that you can import in the dashboard:
    
    
    example.com/contacts,https://example.net/contact-us,301,,,,
    example.com/about,https://example.net/about-us,,FALSE,TRUE,,
    example.com/docs,https://example.com/draft-docs,302,,TRUE

## Important remarks

  * The source URL cannot include a query string. For details on which URL components are supported in source URLs, refer to [Supported URL components in Bulk Redirects](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/url-components/).
  * The CSV file must not include a header row with column names.
  * A source/target URL must be enclosed in quotes (`"`) when it includes a comma (`,`). You can always enclose URL values in quotes, but it is not required.
  * You can skip an optional value by immediately entering a comma (the delimiter) without entering any value.
  * You do not need to include trailing commas.



[PreviousAvailable fields and functions](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/fields-functions/)[NextAPI JSON objects](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/json-objects/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/url-forwarding/bulk-redirects/reference/csv-file-format.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
