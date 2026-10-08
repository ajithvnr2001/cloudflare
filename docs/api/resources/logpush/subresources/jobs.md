---
url: https://developers.cloudflare.com/api/resources/logpush/subresources/jobs/
title: Jobs | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:26:28.050604+00:00
---

# Jobs | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/logpush/subresources/jobs/

[API Reference](https://developers.cloudflare.com/api)

[Logpush](https://developers.cloudflare.com/api/resources/logpush)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Jobs

##### [List Logpush jobs](https://developers.cloudflare.com/api/resources/logpush/subresources/jobs/methods/list)

GET/{accounts_or_zones}/{account_or_zone_id}/logpush/jobs

##### [Get Logpush job details](https://developers.cloudflare.com/api/resources/logpush/subresources/jobs/methods/get)

GET/{accounts_or_zones}/{account_or_zone_id}/logpush/jobs/{job_id}

##### [Create Logpush job](https://developers.cloudflare.com/api/resources/logpush/subresources/jobs/methods/create)

POST/{accounts_or_zones}/{account_or_zone_id}/logpush/jobs

##### [Update Logpush job](https://developers.cloudflare.com/api/resources/logpush/subresources/jobs/methods/update)

PUT/{accounts_or_zones}/{account_or_zone_id}/logpush/jobs/{job_id}

##### [Delete Logpush job](https://developers.cloudflare.com/api/resources/logpush/subresources/jobs/methods/delete)

DELETE/{accounts_or_zones}/{account_or_zone_id}/logpush/jobs/{job_id}

##### ModelsExpand Collapse 

LogpushJob object { id, dataset, destination_conf, 13 more } 

id: optional number

Unique id of the job.

minimum1

dataset: optional "access_requests" or "account_abuse_protection_events" or "audit_logs" or 34 more

Name of the dataset. A list of supported datasets can be found on the [Developer Docs](https://developers.cloudflare.com/logs/reference/log-fields/).

One of the following:

"access_requests"

"account_abuse_protection_events"

"audit_logs"

"audit_logs_v2"

"biso_user_actions"

"casb_findings"

"device_posture_results"

"dex_application_tests"

"dex_device_state_events"

"dlp_forensic_copies"

"dns_firewall_logs"

"dns_logs"

"email_security_alerts"

"email_security_post_delivery_events"

"firewall_events"

"gateway_dns"

"gateway_http"

"gateway_network"

"http_requests"

"ipsec_logs"

"magic_bgp_logs"

"magic_ids_detections"

"mcp_portal_logs"

"mnm_flow_logs"

"nel_reports"

"network_analytics_logs"

"page_shield_events"

"sinkhole_http_logs"

"spectrum_events"

"ssh_logs"

"turnstile_events"

"warp_config_changes"

"warp_toggle_changes"

"websocket_analytics"

"workers_trace_events"

"zaraz_events"

"zero_trust_network_sessions"

destination_conf: optional string

Uniquely identifies a resource (such as an s3 bucket) where data. will be pushed. Additional configuration parameters supported by the destination may be included.

formaturi

maxLength4096

enabled: optional boolean

Flag that indicates if the job is enabled.

error_message: optional string

If not null, the job is currently failing. Failures are usually. repetitive (example: no permissions to write to destination bucket). Only the last failure is recorded. On successful execution of a job the error_message and last_error are set to null.

filter_attack_traffic: optional boolean

When true, excludes DDoS attack traffic from logs. This option is supported for the `http_requests`, `firewall_events`, and `network_analytics_logs` datasets.

Deprecatedfrequency: optional "high" or "low"

This field is deprecated. Please use `max_upload_*` parameters instead. . The frequency at which Cloudflare sends batches of logs to your destination. Setting frequency to high sends your logs in larger quantities of smaller files. Setting frequency to low sends logs in smaller quantities of larger files.

One of the following:

"high"

"low"

kind: optional "" or "edge"

The kind parameter (optional) is used to differentiate between Logpush and Edge Log Delivery jobs (when supported by the dataset).

One of the following:

""

"edge"

last_complete: optional string

Records the last time for which logs have been successfully pushed. If the last successful push was for logs range 2018-07-23T10:00:00Z to 2018-07-23T10:01:00Z then the value of this field will be 2018-07-23T10:01:00Z. If the job has never run or has just been enabled and hasn’t run yet then the field will be empty.

formatdate-time

last_error: optional string

Records the last time the job failed. If not null, the job is currently. failing. If null, the job has either never failed or has run successfully at least once since last failure. See also the error_message field.

formatdate-time

Deprecatedlogpull_options: optional string

This field is deprecated. Use `output_options` instead. Configuration string. It specifies things like requested fields and timestamp formats. If migrating from the logpull api, copy the url (full url or just the query string) of your call here, and logpush will keep on making this call for you, setting start and end times appropriately.

formaturi-reference

maxLength4096

max_upload_bytes: optional 0 or number

The maximum uncompressed file size of a batch of logs. This setting value must be between `5 MB` and `1 GB`, or `0` to disable it. Note that you cannot set a minimum file size; this means that log files may be much smaller than this batch size.

One of the following:

0

The maximum uncompressed file size of a batch of logs. This setting value must be between `5 MB` and `1 GB`, or `0` to disable it. Note that you cannot set a minimum file size; this means that log files may be much smaller than this batch size.

number

max_upload_interval_seconds: optional 0 or number

The maximum interval in seconds for log batches. This setting must be between 30 and 300 seconds (5 minutes), or `0` to disable it. Note that you cannot specify a minimum interval for log batches; this means that log files may be sent in shorter intervals than this.

One of the following:

0

The maximum interval in seconds for log batches. This setting must be between 30 and 300 seconds (5 minutes), or `0` to disable it. Note that you cannot specify a minimum interval for log batches; this means that log files may be sent in shorter intervals than this.

number

max_upload_records: optional 0 or number

The maximum number of log lines per batch. This setting must be between 1000 and 1,000,000 lines, or `0` to disable it. Note that you cannot specify a minimum number of log lines per batch; this means that log files may contain many fewer lines than this.

One of the following:

0

The maximum number of log lines per batch. This setting must be between 1000 and 1,000,000 lines, or `0` to disable it. Note that you cannot specify a minimum number of log lines per batch; this means that log files may contain many fewer lines than this.

number

name: optional string

Optional human readable job name. Not unique. Cloudflare suggests. that you set this to a meaningful string, like the domain name, to make it easier to identify your job.

maxLength512

output_options: optional [OutputOptions](https://developers.cloudflare.com/api/resources/logpush#\(resource\)%20logpush.jobs%20%3E%20\(model\)%20output_options%20%3E%20\(schema\)) { batch_prefix, batch_suffix, CVE-2021-44228, 10 more } 

The structured replacement for `logpull_options`. When including this field, the `logpull_option` field will be ignored.

OutputOptions object { batch_prefix, batch_suffix, "CVE-2021-44228", 10 more } 

The structured replacement for `logpull_options`. When including this field, the `logpull_option` field will be ignored.

batch_prefix: optional string

String to be prepended before each batch.

batch_suffix: optional string

String to be appended after each batch.

"CVE-2021-44228": optional boolean

If set to true, will cause all occurrences of `${` in the generated files to be replaced with `x{`.

field_delimiter: optional string

String to join fields. This field be ignored when `record_template` is set.

field_names: optional array of string

List of field names to be included in the Logpush output. For the moment, there is no option to add all fields at once, so you must specify all the fields names you are interested in.

merge_subrequests: optional boolean

If set to true, subrequests will be merged into the parent request. Only supported for the `http_requests` dataset.

output_type: optional "ndjson" or "csv"

Specifies the output type, such as `ndjson` or `csv`. This sets default values for the rest of the settings, depending on the chosen output type. Some formatting rules, like string quoting, are different between output types.

One of the following:

"ndjson"

"csv"

record_delimiter: optional string

String to be inserted in-between the records as separator.

record_prefix: optional string

String to be prepended before each record.

record_suffix: optional string

String to be appended after each record.

record_template: optional string

String to use as template for each record instead of the default json key value mapping. All fields used in the template must be present in `field_names` as well, otherwise they will end up as null. Format as a Go `text/template` without any standard functions, like conditionals, loops, sub-templates, etc.

sample_rate: optional number

Specifies the sampling rate as a floating number greater than 0 and at most 1. Sampling is applied on top of filtering, and regardless of the current `sample_interval` of the data.

formatfloat

exclusiveMinimum

maximum1

minimum0

timestamp_format: optional "unixnano" or "unix" or "rfc3339" or 2 more

String to specify the format for timestamps, such as `unixnano`, `unix`, `rfc3339`, `rfc3339ms` or `rfc3339ns`.

One of the following:

"unixnano"

"unix"

"rfc3339"

"rfc3339ms"

"rfc3339ns"

JobDeleteResponse object { id } 

id: optional number

Unique id of the job.

minimum1

[ Previous

* * *

Edge ](https://developers.cloudflare.com/api/resources/logpush/subresources/edge)[ Next

* * *

Ownership ](https://developers.cloudflare.com/api/resources/logpush/subresources/ownership)
