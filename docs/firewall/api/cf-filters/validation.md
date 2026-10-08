---
url: https://developers.cloudflare.com/firewall/api/cf-filters/validation/
title: Expression validation \u00b7 Cloudflare Firewall Rules (deprecated) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:16.034194+00:00
---

# Expression validation · Cloudflare Firewall Rules (deprecated) docs

> Source: https://developers.cloudflare.com/firewall/api/cf-filters/validation/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Firewall Rules (deprecated)](https://developers.cloudflare.com/firewall/)
  3. /…

[Manage rules via the APIs](https://developers.cloudflare.com/firewall/api/)

  4. /[Cloudflare Filters API](https://developers.cloudflare.com/firewall/api/cf-filters/)
  5. /Expression validation



# Expression validation

Last updated Apr 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/firewall/api/cf-filters/validation/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewExamples Validate expression via query string Validate expression via JSON object

The Cloudflare Filters API supports an endpoint for validating expressions.

## Examples

### Validate expression via query string

Requestbash
    
    
    curl "https://api.cloudflare.com/client/v4/filters/validate-expr?expression=ip.src==34" \
    --header "X-Auth-Email: <EMAIL>" \
    --header "X-Auth-Key: <API_KEY>"

Responsejson
    
    
    {
      "result": null,
      "success": false,
      "errors": [
        {
          "message": "Filter parsing error:\n`ip.src==34`\n          ^^ couldn't parse address in network: invalid IP address syntax\n"
        }
      ],
      "messages": null
    }

Note the validation error in the response. In this example, the error is due to an invalid IP address format:
    
    
    Filter parsing error:
    `ip.src==34`
              ^^ couldn't parse address in network: invalid IP address syntax

### Validate expression via JSON object

Requestbash
    
    
    curl "https://api.cloudflare.com/client/v4/filters/validate-expr" \
    --header "X-Auth-Email: <EMAIL>" \
    --header "X-Auth-Key: <API_KEY>" \
    --header "Content-Type: application/json" \
    --data '{
      "expression": "ip.src in {2400:cb00::/32 2405:8100::/2000 2c0f:f248::/32 2a06:98c0::/29}"
    }'

Responsejson
    
    
    {
      "result": null,
      "success": false,
      "errors": [
        {
          "message": "Filter parsing error:\n`ip.src in {2400:cb00::/32 2405:8100::/2000 2c0f:f248::/32 2a06:98c0::/29}`\n                                        ^^^^ number too large to fit in target type while parsing with radix 10\n"
        }
      ],
      "messages": null
    }

Note the validation error in the response. In this example, the value for the subnet mask, `/2000`, is not a valid IPv6 CIDR mask:
    
    
    Filter parsing error:
    `ip.src in {2400:cb00::/32 2405:8100::/2000 2c0f:f248::/32 2a06:98c0::/29}`
                                           ^^^^ number too large to fit in target type while parsing with radix 10

[PreviousDELETE examples](https://developers.cloudflare.com/firewall/api/cf-filters/delete/)[NextCall sequence](https://developers.cloudflare.com/firewall/api/call-sequence/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/firewall/api/cf-filters/validation.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
