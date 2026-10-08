---
url: https://developers.cloudflare.com/logs/logpush/parsing-json-log-data/
title: Parse Cloudflare Logs JSON data \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:16.874971+00:00
---

# Parse Cloudflare Logs JSON data · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/logpush/parsing-json-log-data/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /[Logpush](https://developers.cloudflare.com/logs/logpush/)
  4. /Parse Cloudflare Logs JSON data



# Parse Cloudflare Logs JSON data

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/logpush/parsing-json-log-data/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAggregate fieldsFilter fieldsShow cached requestsShow TLS versions

After downloading your Cloudflare Logs data, you can use different tools to parse and analyze your logs.

One of those tools used to parse your JSON log data is `jq`.

Refer to [Download jq ↗︎](https://jqlang.github.io/jq/download/) for more information on obtaining and installing `jq`.

Note

`jq` is a powerful command line for parsing JSON data and performing certain types of analysis. To perform more detailed analysis, consider a full-fledged data analysis system, such as _Kibana_.

## Aggregate fields

To aggregate a field appearing in the log, such as by IP address, URI, or referrer, you can use several `jq` commands. This is useful to identify any patterns in traffic; for example, to identify your most popular pages or to block an attack.

The following examples match on a field name and provide a count of each field instance, sorted in ascending order by count.
    
    
    jq -r .ClientRequestURI logs.json | sort -n | uniq -c | sort -n | tail
    
    
    2 /nginx-logo.png
    2 /poweredby.png
    2 /testagain
    3 /favicon.ico
    3 /testing
    3 /testing123
    6 /test
    7 /testing1234
    10 /cdn-cgi/nexp/dok3v=1613a3a185/cloudflare/rocket.js
    54 /
    
    
    jq -r .ClientRequestUserAgent logs.json | sort -n | uniq -c | sort -n | tail
    
    
    1 python-requests/2.9.1
    2 Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.56 Safari/537.17
    4 Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36
    5 curl/7.47.2-DEV
    36 Mozilla/5.0 (X11; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0
    51 curl/7.46.0-DEV
    
    
    jq -r .ClientRequestReferer logs.json | sort -n | uniq -c | sort -n | tail
    
    
    2 http://example.com/testagain
    3 http://example.com/testing
    5 http://example.com/
    5 http://example.com/testing123
    7 http://example.com/testing1234
    77 null

## Filter fields

Another common use case involves filtering data for a specific field value and then aggregating after that. This helps answer questions like _Which URLs saw the most 502 errors?_ For example:
    
    
    jq 'select(.OriginResponseStatus == 502) | .ClientRequestURI' logs.json | sort -n | uniq -c | sort -n | tail
    
    
    1 "/favicon.ico"
    1 "/testing"
    3 "/testing123"
    6 "/test"
    6 "/testing1234"
    18 "/"

To find out the top IP addresses blocked by the Cloudflare WAF, use the following query:
    
    
    jq -r 'select(.SecurityAction == "block") | .ClientIP' logs.json | sort -n | uniq -c | sort -n
    
    
    1 127.0.0.1

## Show cached requests

To retrieve your cache ratios, try the following query:
    
    
    jq -r '.CacheCacheStatus' logs.json | sort -n | uniq -c | sort -n
    
    
    3 hit
    3 null
    3 stale
    4 expired
    6 miss
    81 unknown

## Show TLS versions

To find out which TLS versions your visitors are using — for example, to decide if you can disable TLS versions that are older than 1.2 — use the following query:
    
    
    jq -r '.ClientSSLProtocol' logs.json | sort -n | uniq -c | sort -n
    
    
    42 none
    58 TLSv1.2

[PreviousManage Logpush with Python](https://developers.cloudflare.com/logs/logpush/examples/example-logpush-python/)[NextLogpush alerts and analytics](https://developers.cloudflare.com/logs/logpush/alerts-and-analytics/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/logpush/parsing-json-log-data.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
