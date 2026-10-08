---
url: https://developers.cloudflare.com/api/resources/pipelines/
title: Pipelines | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:18:49.374510+00:00
---

# Pipelines | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/pipelines/

[API Reference](https://developers.cloudflare.com/api)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Pipelines

##### [[DEPRECATED] List Pipelines](https://developers.cloudflare.com/api/resources/pipelines/methods/list)

Deprecated

GET/accounts/{account_id}/pipelines

##### [[DEPRECATED] Get Pipeline](https://developers.cloudflare.com/api/resources/pipelines/methods/get)

Deprecated

GET/accounts/{account_id}/pipelines/{pipeline_name}

##### [[DEPRECATED] Create Pipeline](https://developers.cloudflare.com/api/resources/pipelines/methods/create)

Deprecated

POST/accounts/{account_id}/pipelines

##### [[DEPRECATED] Update Pipeline](https://developers.cloudflare.com/api/resources/pipelines/methods/update)

Deprecated

PUT/accounts/{account_id}/pipelines/{pipeline_name}

##### [[DEPRECATED] Delete Pipeline](https://developers.cloudflare.com/api/resources/pipelines/methods/delete)

Deprecated

DELETE/accounts/{account_id}/pipelines/{pipeline_name}

##### [List Pipelines](https://developers.cloudflare.com/api/resources/pipelines/methods/list_v1)

GET/accounts/{account_id}/pipelines/v1/pipelines

##### [Get Pipeline Details](https://developers.cloudflare.com/api/resources/pipelines/methods/get_v1)

GET/accounts/{account_id}/pipelines/v1/pipelines/{pipeline_id}

##### [Create Pipeline](https://developers.cloudflare.com/api/resources/pipelines/methods/create_v1)

POST/accounts/{account_id}/pipelines/v1/pipelines

##### [Delete Pipeline](https://developers.cloudflare.com/api/resources/pipelines/methods/delete_v1)

DELETE/accounts/{account_id}/pipelines/v1/pipelines/{pipeline_id}

##### [Validate SQL](https://developers.cloudflare.com/api/resources/pipelines/methods/validate_sql)

POST/accounts/{account_id}/pipelines/v1/validate_sql

##### ModelsExpand Collapse 

FieldType = object { type }  or object { type }  or object { type }  or 8 more

One of the following:

Int32 object { type } 

type: "int32"

Int64 object { type } 

type: "int64"

Float32 object { type } 

type: "float32"

Float64 object { type } 

type: "float64"

Bool object { type } 

type: "bool"

String object { type } 

type: "string"

Binary object { type } 

type: "binary"

Timestamp object { type, unit } 

type: "timestamp"

unit: optional "second" or "millisecond" or "microsecond" or "nanosecond"

One of the following:

"second"

"millisecond"

"microsecond"

"nanosecond"

Json object { type } 

type: "json"

Struct object { fields, type, name } 

fields: array of [SourceField](https://developers.cloudflare.com/api/resources/pipelines#\(resource\)%20pipelines%20%3E%20\(model\)%20source_field%20%3E%20\(schema\))

One of the following:

Int32 object { type, metadata_key, name, 2 more } 

type: "int32"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Int64 object { type, metadata_key, name, 2 more } 

type: "int64"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Float32 object { type, metadata_key, name, 2 more } 

type: "float32"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Float64 object { type, metadata_key, name, 2 more } 

type: "float64"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Bool object { type, metadata_key, name, 2 more } 

type: "bool"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

String object { type, metadata_key, name, 2 more } 

type: "string"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Binary object { type, metadata_key, name, 2 more } 

type: "binary"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Timestamp object { type, metadata_key, name, 3 more } 

type: "timestamp"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

unit: optional "second" or "millisecond" or "microsecond" or "nanosecond"

One of the following:

"second"

"millisecond"

"microsecond"

"nanosecond"

Json object { type, metadata_key, name, 2 more } 

type: "json"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Struct = [StructField](https://developers.cloudflare.com/api/resources/pipelines#\(resource\)%20pipelines%20%3E%20\(model\)%20struct_field%20%3E%20\(schema\)) { fields, name } 

type: "struct"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

List = [ListField](https://developers.cloudflare.com/api/resources/pipelines#\(resource\)%20pipelines%20%3E%20\(model\)%20list_field%20%3E%20\(schema\)) { items } 

type: "list"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

type: "struct"

name: optional string

List object { items, type } 

items: [SourceField](https://developers.cloudflare.com/api/resources/pipelines#\(resource\)%20pipelines%20%3E%20\(model\)%20source_field%20%3E%20\(schema\))

type: "list"

ListField object { items } 

items: [SourceField](https://developers.cloudflare.com/api/resources/pipelines#\(resource\)%20pipelines%20%3E%20\(model\)%20source_field%20%3E%20\(schema\))

SourceField = object { type, metadata_key, name, 2 more }  or object { type, metadata_key, name, 2 more }  or object { type, metadata_key, name, 2 more }  or 8 more

One of the following:

Int32 object { type, metadata_key, name, 2 more } 

type: "int32"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Int64 object { type, metadata_key, name, 2 more } 

type: "int64"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Float32 object { type, metadata_key, name, 2 more } 

type: "float32"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Float64 object { type, metadata_key, name, 2 more } 

type: "float64"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Bool object { type, metadata_key, name, 2 more } 

type: "bool"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

String object { type, metadata_key, name, 2 more } 

type: "string"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Binary object { type, metadata_key, name, 2 more } 

type: "binary"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Timestamp object { type, metadata_key, name, 3 more } 

type: "timestamp"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

unit: optional "second" or "millisecond" or "microsecond" or "nanosecond"

One of the following:

"second"

"millisecond"

"microsecond"

"nanosecond"

Json object { type, metadata_key, name, 2 more } 

type: "json"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Struct = [StructField](https://developers.cloudflare.com/api/resources/pipelines#\(resource\)%20pipelines%20%3E%20\(model\)%20struct_field%20%3E%20\(schema\)) { fields, name } 

type: "struct"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

List = [ListField](https://developers.cloudflare.com/api/resources/pipelines#\(resource\)%20pipelines%20%3E%20\(model\)%20list_field%20%3E%20\(schema\)) { items } 

type: "list"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

StructField object { fields, name } 

fields: array of [SourceField](https://developers.cloudflare.com/api/resources/pipelines#\(resource\)%20pipelines%20%3E%20\(model\)%20source_field%20%3E%20\(schema\))

name: optional string

PipelineListResponse object { result_info, results, success } 

result_info: object { count, page, per_page, total_count } 

count: number

Indicates the number of items on current page.

page: number

Indicates the current page number.

per_page: number

Indicates the number of items per page.

total_count: number

Indicates the total number of items.

results: array of object { id, destination, endpoint, 3 more } 

id: string

Specifies the pipeline identifier.

destination: object { batch, compression, format, 2 more } 

batch: object { max_bytes, max_duration_s, max_rows } 

max_bytes: number

Specifies rough maximum size of files.

maximum100000000

minimum1000

max_duration_s: number

Specifies duration to wait to aggregate batches files.

maximum300

minimum0.25

max_rows: number

Specifies rough maximum number of rows per file.

maximum10000000

minimum100

compression: object { type } 

type: "none" or "gzip" or "deflate"

Specifies the desired compression algorithm and format.

One of the following:

"none"

"gzip"

"deflate"

format: "json"

Specifies the format of data to deliver.

path: object { bucket, filename, filepath, prefix } 

bucket: string

Specifies the R2 Bucket to store files.

filename: optional string

Specifies the name pattern to for individual data files.

filepath: optional string

Specifies the name pattern for directory.

prefix: optional string

Specifies the base directory within the bucket.

type: "r2"

Specifies the type of destination.

endpoint: string

Indicates the endpoint URL to send traffic.

name: string

Defines the name of the pipeline.

maxLength128

minLength1

source: array of object { format, type, authentication, cors }  or object { format, type } 

One of the following:

CloudflarePipelinesWorkersPipelinesHTTPSource object { format, type, authentication, cors } 

[DEPRECATED] HTTP source configuration. Use the new streams API instead.

format: "json"

Specifies the format of source data.

type: string

authentication: optional boolean

Specifies whether authentication is required to send to this pipeline via HTTP.

cors: optional object { origins } 

origins: optional array of string

Specifies allowed origins to allow Cross Origin HTTP Requests.

CloudflarePipelinesWorkersPipelinesBindingSource object { format, type } 

[DEPRECATED] Worker binding source configuration. Use the new streams API instead.

format: "json"

Specifies the format of source data.

type: string

version: number

Indicates the version number of last saved configuration.

success: boolean

Indicates whether the API call was successful.

PipelineGetResponse object { id, destination, endpoint, 3 more } 

[DEPRECATED] Describes the configuration of a pipeline. Use the new streams/sinks/pipelines API instead.

id: string

Specifies the pipeline identifier.

destination: object { batch, compression, format, 2 more } 

batch: object { max_bytes, max_duration_s, max_rows } 

max_bytes: number

Specifies rough maximum size of files.

maximum100000000

minimum1000

max_duration_s: number

Specifies duration to wait to aggregate batches files.

maximum300

minimum0.25

max_rows: number

Specifies rough maximum number of rows per file.

maximum10000000

minimum100

compression: object { type } 

type: "none" or "gzip" or "deflate"

Specifies the desired compression algorithm and format.

One of the following:

"none"

"gzip"

"deflate"

format: "json"

Specifies the format of data to deliver.

path: object { bucket, filename, filepath, prefix } 

bucket: string

Specifies the R2 Bucket to store files.

filename: optional string

Specifies the name pattern to for individual data files.

filepath: optional string

Specifies the name pattern for directory.

prefix: optional string

Specifies the base directory within the bucket.

type: "r2"

Specifies the type of destination.

endpoint: string

Indicates the endpoint URL to send traffic.

name: string

Defines the name of the pipeline.

maxLength128

minLength1

source: array of object { format, type, authentication, cors }  or object { format, type } 

One of the following:

CloudflarePipelinesWorkersPipelinesHTTPSource object { format, type, authentication, cors } 

[DEPRECATED] HTTP source configuration. Use the new streams API instead.

format: "json"

Specifies the format of source data.

type: string

authentication: optional boolean

Specifies whether authentication is required to send to this pipeline via HTTP.

cors: optional object { origins } 

origins: optional array of string

Specifies allowed origins to allow Cross Origin HTTP Requests.

CloudflarePipelinesWorkersPipelinesBindingSource object { format, type } 

[DEPRECATED] Worker binding source configuration. Use the new streams API instead.

format: "json"

Specifies the format of source data.

type: string

version: number

Indicates the version number of last saved configuration.

PipelineCreateResponse object { id, destination, endpoint, 3 more } 

[DEPRECATED] Describes the configuration of a pipeline. Use the new streams/sinks/pipelines API instead.

id: string

Specifies the pipeline identifier.

destination: object { batch, compression, format, 2 more } 

batch: object { max_bytes, max_duration_s, max_rows } 

max_bytes: number

Specifies rough maximum size of files.

maximum100000000

minimum1000

max_duration_s: number

Specifies duration to wait to aggregate batches files.

maximum300

minimum0.25

max_rows: number

Specifies rough maximum number of rows per file.

maximum10000000

minimum100

compression: object { type } 

type: "none" or "gzip" or "deflate"

Specifies the desired compression algorithm and format.

One of the following:

"none"

"gzip"

"deflate"

format: "json"

Specifies the format of data to deliver.

path: object { bucket, filename, filepath, prefix } 

bucket: string

Specifies the R2 Bucket to store files.

filename: optional string

Specifies the name pattern to for individual data files.

filepath: optional string

Specifies the name pattern for directory.

prefix: optional string

Specifies the base directory within the bucket.

type: "r2"

Specifies the type of destination.

endpoint: string

Indicates the endpoint URL to send traffic.

name: string

Defines the name of the pipeline.

maxLength128

minLength1

source: array of object { format, type, authentication, cors }  or object { format, type } 

One of the following:

CloudflarePipelinesWorkersPipelinesHTTPSource object { format, type, authentication, cors } 

[DEPRECATED] HTTP source configuration. Use the new streams API instead.

format: "json"

Specifies the format of source data.

type: string

authentication: optional boolean

Specifies whether authentication is required to send to this pipeline via HTTP.

cors: optional object { origins } 

origins: optional array of string

Specifies allowed origins to allow Cross Origin HTTP Requests.

CloudflarePipelinesWorkersPipelinesBindingSource object { format, type } 

[DEPRECATED] Worker binding source configuration. Use the new streams API instead.

format: "json"

Specifies the format of source data.

type: string

version: number

Indicates the version number of last saved configuration.

PipelineUpdateResponse object { id, destination, endpoint, 3 more } 

[DEPRECATED] Describes the configuration of a pipeline. Use the new streams/sinks/pipelines API instead.

id: string

Specifies the pipeline identifier.

destination: object { batch, compression, format, 2 more } 

batch: object { max_bytes, max_duration_s, max_rows } 

max_bytes: number

Specifies rough maximum size of files.

maximum100000000

minimum1000

max_duration_s: number

Specifies duration to wait to aggregate batches files.

maximum300

minimum0.25

max_rows: number

Specifies rough maximum number of rows per file.

maximum10000000

minimum100

compression: object { type } 

type: "none" or "gzip" or "deflate"

Specifies the desired compression algorithm and format.

One of the following:

"none"

"gzip"

"deflate"

format: "json"

Specifies the format of data to deliver.

path: object { bucket, filename, filepath, prefix } 

bucket: string

Specifies the R2 Bucket to store files.

filename: optional string

Specifies the name pattern to for individual data files.

filepath: optional string

Specifies the name pattern for directory.

prefix: optional string

Specifies the base directory within the bucket.

type: "r2"

Specifies the type of destination.

endpoint: string

Indicates the endpoint URL to send traffic.

name: string

Defines the name of the pipeline.

maxLength128

minLength1

source: array of object { format, type, authentication, cors }  or object { format, type } 

One of the following:

CloudflarePipelinesWorkersPipelinesHTTPSource object { format, type, authentication, cors } 

[DEPRECATED] HTTP source configuration. Use the new streams API instead.

format: "json"

Specifies the format of source data.

type: string

authentication: optional boolean

Specifies whether authentication is required to send to this pipeline via HTTP.

cors: optional object { origins } 

origins: optional array of string

Specifies allowed origins to allow Cross Origin HTTP Requests.

CloudflarePipelinesWorkersPipelinesBindingSource object { format, type } 

[DEPRECATED] Worker binding source configuration. Use the new streams API instead.

format: "json"

Specifies the format of source data.

type: string

version: number

Indicates the version number of last saved configuration.

PipelineListV1Response object { id, created_at, modified_at, 3 more } 

id: string

Indicates a unique identifier for this pipeline.

created_at: string

modified_at: string

name: string

Indicates the name of the Pipeline.

maxLength128

minLength1

sql: string

Specifies SQL for the Pipeline processing flow.

status: string

Indicates the current status of the Pipeline.

PipelineGetV1Response object { id, created_at, modified_at, 5 more } 

id: string

Indicates a unique identifier for this pipeline.

created_at: string

modified_at: string

name: string

Indicates the name of the Pipeline.

maxLength128

minLength1

sql: string

Specifies SQL for the Pipeline processing flow.

status: string

Indicates the current status of the Pipeline.

tables: array of object { id, latest, name, 2 more } 

List of streams and sinks used by this pipeline.

id: string

Unique identifier for the connection (stream or sink).

latest: number

Latest available version of the connection.

name: string

Name of the connection.

maxLength128

minLength1

type: "stream" or "sink"

Type of the connection.

One of the following:

"stream"

"sink"

version: number

Current version of the connection used by this pipeline.

failure_reason: optional string

Indicates the reason for the failure of the Pipeline.

PipelineCreateV1Response object { id, created_at, modified_at, 3 more } 

id: string

Indicates a unique identifier for this pipeline.

created_at: string

modified_at: string

name: string

Indicates the name of the Pipeline.

maxLength128

minLength1

sql: string

Specifies SQL for the Pipeline processing flow.

status: string

Indicates the current status of the Pipeline.

PipelineDeleteV1Response = unknown

PipelineValidateSqlResponse object { tables, graph } 

tables: map[object { id, name, type, version } ]

Indicates tables involved in the processing.

id: string

name: string

type: string

version: number

graph: optional object { edges, nodes } 

Indicates the processing flow to implement the SQL.

edges: array of object { dest_id, edge_type, key_type, 2 more } 

dest_id: number

formatint32

minimum0

edge_type: string

key_type: string

src_id: number

formatint32

minimum0

value_type: string

nodes: array of object { description, node_id, operator, parallelism } 

description: string

node_id: number

formatint32

minimum0

operator: string

parallelism: number

formatint32

minimum0

#### PipelinesSinks

##### [List Sinks](https://developers.cloudflare.com/api/resources/pipelines/subresources/sinks/methods/list)

GET/accounts/{account_id}/pipelines/v1/sinks

##### [Get Sink Details](https://developers.cloudflare.com/api/resources/pipelines/subresources/sinks/methods/get)

GET/accounts/{account_id}/pipelines/v1/sinks/{sink_id}

##### [Create Sink](https://developers.cloudflare.com/api/resources/pipelines/subresources/sinks/methods/create)

POST/accounts/{account_id}/pipelines/v1/sinks

##### [Delete Sink](https://developers.cloudflare.com/api/resources/pipelines/subresources/sinks/methods/delete)

DELETE/accounts/{account_id}/pipelines/v1/sinks/{sink_id}

##### ModelsExpand Collapse 

SinkListResponse object { id, created_at, modified_at, 5 more } 

id: string

Indicates a unique identifier for this sink.

created_at: string

formatdate-time

modified_at: string

formatdate-time

name: string

Defines the name of the Sink.

maxLength128

minLength1

type: "r2" or "r2_data_catalog" or "basin_catalog"

Specifies the type of sink.

One of the following:

"r2"

"r2_data_catalog"

"basin_catalog"

config: optional object { account_id, bucket, file_naming, 4 more }  or object { account_id, bucket, table_name, 2 more } 

Defines the configuration of the R2 Sink.

One of the following:

CloudflarePipelinesR2TablePublic object { account_id, bucket, file_naming, 4 more } 

R2 Sink public configuration.

account_id: string

Cloudflare Account ID for the bucket

bucket: string

R2 Bucket to write to

file_naming: optional object { prefix, strategy, suffix } 

Controls filename prefix/suffix and strategy.

prefix: optional string

The prefix to use in file name. i.e prefix-.parquet

strategy: optional "serial" or "uuid" or "uuid_v7" or "ulid"

Filename generation strategy.

One of the following:

"serial"

"uuid"

"uuid_v7"

"ulid"

suffix: optional string

This will overwrite the default file suffix. i.e .parquet, use with caution

jurisdiction: optional string

Jurisdiction this bucket is hosted in

partitioning: optional object { time_pattern } 

Data-layout partitioning for sinks.

time_pattern: optional string

The pattern of the date string

path: optional string

Subpath within the bucket to write to

rolling_policy: optional object { file_size_bytes, inactivity_seconds, interval_seconds } 

Rolling policy for file sinks (when & why to close a file and open a new one).

file_size_bytes: optional number

Files will be rolled after reaching this number of bytes

formatuint64

minimum0

inactivity_seconds: optional number

Number of seconds of inactivity to wait before rolling over to a new file

formatuint64

minimum1

interval_seconds: optional number

Number of seconds to wait before rolling over to a new file

formatuint64

minimum1

CloudflarePipelinesR2DataCatalogTablePublic object { account_id, bucket, table_name, 2 more } 

R2 Data Catalog Sink public configuration.

account_id: string

Cloudflare Account ID

formaturi

bucket: string

The R2 Bucket that hosts this catalog

table_name: string

Table name

namespace: optional string

Table namespace

rolling_policy: optional object { file_size_bytes, inactivity_seconds, interval_seconds } 

Rolling policy for file sinks (when & why to close a file and open a new one).

file_size_bytes: optional number

Files will be rolled after reaching this number of bytes

formatuint64

minimum0

inactivity_seconds: optional number

Number of seconds of inactivity to wait before rolling over to a new file

formatuint64

minimum1

interval_seconds: optional number

Number of seconds to wait before rolling over to a new file

formatuint64

minimum1

format: optional object { type, compression, decimal_encoding, 2 more }  or object { type, compression, row_group_bytes } 

Defines the output data format of a sink.

One of the following:

Json object { type, compression, decimal_encoding, 2 more } 

type: "json"

compression: optional "uncompressed" or "gzip"

Specifies the compression applied to JSON sink output.

One of the following:

"uncompressed"

"gzip"

decimal_encoding: optional "number" or "string" or "bytes"

One of the following:

"number"

"string"

"bytes"

timestamp_format: optional "rfc3339" or "unix_millis"

One of the following:

"rfc3339"

"unix_millis"

unstructured: optional boolean

Parquet object { type, compression, row_group_bytes } 

type: "parquet"

compression: optional "uncompressed" or "snappy" or "gzip" or 2 more

One of the following:

"uncompressed"

"snappy"

"gzip"

"zstd"

"lz4"

row_group_bytes: optional number

formatint64

minimum0

schema: optional object { fields, inferred } 

Defines the schema of the events in the data stream.

fields: optional array of [SourceField](https://developers.cloudflare.com/api/resources/pipelines#\(resource\)%20pipelines%20%3E%20\(model\)%20source_field%20%3E%20\(schema\))

One of the following:

Int32 object { type, metadata_key, name, 2 more } 

type: "int32"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Int64 object { type, metadata_key, name, 2 more } 

type: "int64"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Float32 object { type, metadata_key, name, 2 more } 

type: "float32"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Float64 object { type, metadata_key, name, 2 more } 

type: "float64"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Bool object { type, metadata_key, name, 2 more } 

type: "bool"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

String object { type, metadata_key, name, 2 more } 

type: "string"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Binary object { type, metadata_key, name, 2 more } 

type: "binary"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Timestamp object { type, metadata_key, name, 3 more } 

type: "timestamp"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

unit: optional "second" or "millisecond" or "microsecond" or "nanosecond"

One of the following:

"second"

"millisecond"

"microsecond"

"nanosecond"

Json object { type, metadata_key, name, 2 more } 

type: "json"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Struct = [StructField](https://developers.cloudflare.com/api/resources/pipelines#\(resource\)%20pipelines%20%3E%20\(model\)%20struct_field%20%3E%20\(schema\)) { fields, name } 

type: "struct"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

List = [ListField](https://developers.cloudflare.com/api/resources/pipelines#\(resource\)%20pipelines%20%3E%20\(model\)%20list_field%20%3E%20\(schema\)) { items } 

type: "list"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

inferred: optional boolean

SinkGetResponse object { id, created_at, modified_at, 5 more } 

id: string

Indicates a unique identifier for this sink.

created_at: string

formatdate-time

modified_at: string

formatdate-time

name: string

Defines the name of the Sink.

maxLength128

minLength1

type: "r2" or "r2_data_catalog" or "basin_catalog"

Specifies the type of sink.

One of the following:

"r2"

"r2_data_catalog"

"basin_catalog"

config: optional object { account_id, bucket, file_naming, 4 more }  or object { account_id, bucket, table_name, 2 more } 

Defines the configuration of the R2 Sink.

One of the following:

CloudflarePipelinesR2TablePublic object { account_id, bucket, file_naming, 4 more } 

R2 Sink public configuration.

account_id: string

Cloudflare Account ID for the bucket

bucket: string

R2 Bucket to write to

file_naming: optional object { prefix, strategy, suffix } 

Controls filename prefix/suffix and strategy.

prefix: optional string

The prefix to use in file name. i.e prefix-.parquet

strategy: optional "serial" or "uuid" or "uuid_v7" or "ulid"

Filename generation strategy.

One of the following:

"serial"

"uuid"

"uuid_v7"

"ulid"

suffix: optional string

This will overwrite the default file suffix. i.e .parquet, use with caution

jurisdiction: optional string

Jurisdiction this bucket is hosted in

partitioning: optional object { time_pattern } 

Data-layout partitioning for sinks.

time_pattern: optional string

The pattern of the date string

path: optional string

Subpath within the bucket to write to

rolling_policy: optional object { file_size_bytes, inactivity_seconds, interval_seconds } 

Rolling policy for file sinks (when & why to close a file and open a new one).

file_size_bytes: optional number

Files will be rolled after reaching this number of bytes

formatuint64

minimum0

inactivity_seconds: optional number

Number of seconds of inactivity to wait before rolling over to a new file

formatuint64

minimum1

interval_seconds: optional number

Number of seconds to wait before rolling over to a new file

formatuint64

minimum1

CloudflarePipelinesR2DataCatalogTablePublic object { account_id, bucket, table_name, 2 more } 

R2 Data Catalog Sink public configuration.

account_id: string

Cloudflare Account ID

formaturi

bucket: string

The R2 Bucket that hosts this catalog

table_name: string

Table name

namespace: optional string

Table namespace

rolling_policy: optional object { file_size_bytes, inactivity_seconds, interval_seconds } 

Rolling policy for file sinks (when & why to close a file and open a new one).

file_size_bytes: optional number

Files will be rolled after reaching this number of bytes

formatuint64

minimum0

inactivity_seconds: optional number

Number of seconds of inactivity to wait before rolling over to a new file

formatuint64

minimum1

interval_seconds: optional number

Number of seconds to wait before rolling over to a new file

formatuint64

minimum1

format: optional object { type, compression, decimal_encoding, 2 more }  or object { type, compression, row_group_bytes } 

Defines the output data format of a sink.

One of the following:

Json object { type, compression, decimal_encoding, 2 more } 

type: "json"

compression: optional "uncompressed" or "gzip"

Specifies the compression applied to JSON sink output.

One of the following:

"uncompressed"

"gzip"

decimal_encoding: optional "number" or "string" or "bytes"

One of the following:

"number"

"string"

"bytes"

timestamp_format: optional "rfc3339" or "unix_millis"

One of the following:

"rfc3339"

"unix_millis"

unstructured: optional boolean

Parquet object { type, compression, row_group_bytes } 

type: "parquet"

compression: optional "uncompressed" or "snappy" or "gzip" or 2 more

One of the following:

"uncompressed"

"snappy"

"gzip"

"zstd"

"lz4"

row_group_bytes: optional number

formatint64

minimum0

schema: optional object { fields, inferred } 

Defines the schema of the events in the data stream.

fields: optional array of [SourceField](https://developers.cloudflare.com/api/resources/pipelines#\(resource\)%20pipelines%20%3E%20\(model\)%20source_field%20%3E%20\(schema\))

One of the following:

Int32 object { type, metadata_key, name, 2 more } 

type: "int32"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Int64 object { type, metadata_key, name, 2 more } 

type: "int64"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Float32 object { type, metadata_key, name, 2 more } 

type: "float32"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Float64 object { type, metadata_key, name, 2 more } 

type: "float64"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Bool object { type, metadata_key, name, 2 more } 

type: "bool"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

String object { type, metadata_key, name, 2 more } 

type: "string"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Binary object { type, metadata_key, name, 2 more } 

type: "binary"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Timestamp object { type, metadata_key, name, 3 more } 

type: "timestamp"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

unit: optional "second" or "millisecond" or "microsecond" or "nanosecond"

One of the following:

"second"

"millisecond"

"microsecond"

"nanosecond"

Json object { type, metadata_key, name, 2 more } 

type: "json"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Struct = [StructField](https://developers.cloudflare.com/api/resources/pipelines#\(resource\)%20pipelines%20%3E%20\(model\)%20struct_field%20%3E%20\(schema\)) { fields, name } 

type: "struct"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

List = [ListField](https://developers.cloudflare.com/api/resources/pipelines#\(resource\)%20pipelines%20%3E%20\(model\)%20list_field%20%3E%20\(schema\)) { items } 

type: "list"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

inferred: optional boolean

SinkCreateResponse object { id, created_at, modified_at, 5 more } 

id: string

Indicates a unique identifier for this sink.

created_at: string

formatdate-time

modified_at: string

formatdate-time

name: string

Defines the name of the Sink.

maxLength128

minLength1

type: "r2" or "r2_data_catalog" or "basin_catalog"

Specifies the type of sink.

One of the following:

"r2"

"r2_data_catalog"

"basin_catalog"

config: optional object { account_id, bucket, credentials, 5 more }  or object { token, account_id, bucket, 3 more } 

R2 Data Catalog Sink

One of the following:

CloudflarePipelinesR2Table object { account_id, bucket, credentials, 5 more } 

account_id: string

Cloudflare Account ID for the bucket

bucket: string

R2 Bucket to write to

credentials: object { access_key_id, secret_access_key } 

access_key_id: string

Cloudflare Account ID for the bucket

formatvar-str

secret_access_key: string

Cloudflare Account ID for the bucket

formatvar-str

file_naming: optional object { prefix, strategy, suffix } 

Controls filename prefix/suffix and strategy.

prefix: optional string

The prefix to use in file name. i.e prefix-.parquet

strategy: optional "serial" or "uuid" or "uuid_v7" or "ulid"

Filename generation strategy.

One of the following:

"serial"

"uuid"

"uuid_v7"

"ulid"

suffix: optional string

This will overwrite the default file suffix. i.e .parquet, use with caution

jurisdiction: optional string

Jurisdiction this bucket is hosted in

partitioning: optional object { time_pattern } 

Data-layout partitioning for sinks.

time_pattern: optional string

The pattern of the date string

path: optional string

Subpath within the bucket to write to

rolling_policy: optional object { file_size_bytes, inactivity_seconds, interval_seconds } 

Rolling policy for file sinks (when & why to close a file and open a new one).

file_size_bytes: optional number

Files will be rolled after reaching this number of bytes

formatuint64

minimum0

inactivity_seconds: optional number

Number of seconds of inactivity to wait before rolling over to a new file

formatuint64

minimum1

interval_seconds: optional number

Number of seconds to wait before rolling over to a new file

formatuint64

minimum1

CloudflarePipelinesR2DataCatalogTable object { token, account_id, bucket, 3 more } 

R2 Data Catalog Sink

token: string

Authentication token

formatvar-str

account_id: string

Cloudflare Account ID

formaturi

bucket: string

The R2 Bucket that hosts this catalog

table_name: string

Table name

namespace: optional string

Table namespace

rolling_policy: optional object { file_size_bytes, inactivity_seconds, interval_seconds } 

Rolling policy for file sinks (when & why to close a file and open a new one).

file_size_bytes: optional number

Files will be rolled after reaching this number of bytes

formatuint64

minimum0

inactivity_seconds: optional number

Number of seconds of inactivity to wait before rolling over to a new file

formatuint64

minimum1

interval_seconds: optional number

Number of seconds to wait before rolling over to a new file

formatuint64

minimum1

format: optional object { type, compression, decimal_encoding, 2 more }  or object { type, compression, row_group_bytes } 

Defines the output data format of a sink.

One of the following:

Json object { type, compression, decimal_encoding, 2 more } 

type: "json"

compression: optional "uncompressed" or "gzip"

Specifies the compression applied to JSON sink output.

One of the following:

"uncompressed"

"gzip"

decimal_encoding: optional "number" or "string" or "bytes"

One of the following:

"number"

"string"

"bytes"

timestamp_format: optional "rfc3339" or "unix_millis"

One of the following:

"rfc3339"

"unix_millis"

unstructured: optional boolean

Parquet object { type, compression, row_group_bytes } 

type: "parquet"

compression: optional "uncompressed" or "snappy" or "gzip" or 2 more

One of the following:

"uncompressed"

"snappy"

"gzip"

"zstd"

"lz4"

row_group_bytes: optional number

formatint64

minimum0

schema: optional object { fields, inferred } 

Defines the schema of the events in the data stream.

fields: optional array of [SourceField](https://developers.cloudflare.com/api/resources/pipelines#\(resource\)%20pipelines%20%3E%20\(model\)%20source_field%20%3E%20\(schema\))

One of the following:

Int32 object { type, metadata_key, name, 2 more } 

type: "int32"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Int64 object { type, metadata_key, name, 2 more } 

type: "int64"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Float32 object { type, metadata_key, name, 2 more } 

type: "float32"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Float64 object { type, metadata_key, name, 2 more } 

type: "float64"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Bool object { type, metadata_key, name, 2 more } 

type: "bool"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

String object { type, metadata_key, name, 2 more } 

type: "string"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Binary object { type, metadata_key, name, 2 more } 

type: "binary"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Timestamp object { type, metadata_key, name, 3 more } 

type: "timestamp"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

unit: optional "second" or "millisecond" or "microsecond" or "nanosecond"

One of the following:

"second"

"millisecond"

"microsecond"

"nanosecond"

Json object { type, metadata_key, name, 2 more } 

type: "json"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Struct = [StructField](https://developers.cloudflare.com/api/resources/pipelines#\(resource\)%20pipelines%20%3E%20\(model\)%20struct_field%20%3E%20\(schema\)) { fields, name } 

type: "struct"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

List = [ListField](https://developers.cloudflare.com/api/resources/pipelines#\(resource\)%20pipelines%20%3E%20\(model\)%20list_field%20%3E%20\(schema\)) { items } 

type: "list"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

inferred: optional boolean

SinkDeleteResponse = unknown

#### PipelinesStreams

##### [List Streams](https://developers.cloudflare.com/api/resources/pipelines/subresources/streams/methods/list)

GET/accounts/{account_id}/pipelines/v1/streams

##### [Get Stream Details](https://developers.cloudflare.com/api/resources/pipelines/subresources/streams/methods/get)

GET/accounts/{account_id}/pipelines/v1/streams/{stream_id}

##### [Create Stream](https://developers.cloudflare.com/api/resources/pipelines/subresources/streams/methods/create)

POST/accounts/{account_id}/pipelines/v1/streams

##### [Update Stream](https://developers.cloudflare.com/api/resources/pipelines/subresources/streams/methods/update)

PATCH/accounts/{account_id}/pipelines/v1/streams/{stream_id}

##### [Delete Stream](https://developers.cloudflare.com/api/resources/pipelines/subresources/streams/methods/delete)

DELETE/accounts/{account_id}/pipelines/v1/streams/{stream_id}

##### ModelsExpand Collapse 

StreamListResponse object { id, created_at, http, 7 more } 

id: string

Indicates a unique identifier for this stream.

created_at: string

formatdate-time

http: object { authentication, enabled, cors } 

authentication: boolean

Indicates that authentication is required for the HTTP endpoint.

enabled: boolean

Indicates that the HTTP endpoint is enabled.

cors: optional object { origins } 

Specifies the CORS options for the HTTP endpoint.

origins: optional array of string

modified_at: string

formatdate-time

name: string

Indicates the name of the Stream.

maxLength128

minLength1

version: number

Indicates the current version of this stream.

worker_binding: object { enabled } 

enabled: boolean

Indicates that the worker binding is enabled.

endpoint: optional string

Indicates the endpoint URL of this stream.

formaturi

format: optional object { type, decimal_encoding, timestamp_format, unstructured }  or object { type, compression, row_group_bytes } 

Defines the data format of the events.

One of the following:

Json object { type, decimal_encoding, timestamp_format, unstructured } 

type: "json"

decimal_encoding: optional "number" or "string" or "bytes"

One of the following:

"number"

"string"

"bytes"

timestamp_format: optional "rfc3339" or "unix_millis"

One of the following:

"rfc3339"

"unix_millis"

unstructured: optional boolean

Parquet object { type, compression, row_group_bytes } 

type: "parquet"

compression: optional "uncompressed" or "snappy" or "gzip" or 2 more

One of the following:

"uncompressed"

"snappy"

"gzip"

"zstd"

"lz4"

row_group_bytes: optional number

formatint64

minimum0

schema: optional object { fields, inferred } 

Defines the schema of the events in the data stream.

fields: optional array of [SourceField](https://developers.cloudflare.com/api/resources/pipelines#\(resource\)%20pipelines%20%3E%20\(model\)%20source_field%20%3E%20\(schema\))

One of the following:

Int32 object { type, metadata_key, name, 2 more } 

type: "int32"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Int64 object { type, metadata_key, name, 2 more } 

type: "int64"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Float32 object { type, metadata_key, name, 2 more } 

type: "float32"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Float64 object { type, metadata_key, name, 2 more } 

type: "float64"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Bool object { type, metadata_key, name, 2 more } 

type: "bool"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

String object { type, metadata_key, name, 2 more } 

type: "string"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Binary object { type, metadata_key, name, 2 more } 

type: "binary"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Timestamp object { type, metadata_key, name, 3 more } 

type: "timestamp"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

unit: optional "second" or "millisecond" or "microsecond" or "nanosecond"

One of the following:

"second"

"millisecond"

"microsecond"

"nanosecond"

Json object { type, metadata_key, name, 2 more } 

type: "json"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Struct = [StructField](https://developers.cloudflare.com/api/resources/pipelines#\(resource\)%20pipelines%20%3E%20\(model\)%20struct_field%20%3E%20\(schema\)) { fields, name } 

type: "struct"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

List = [ListField](https://developers.cloudflare.com/api/resources/pipelines#\(resource\)%20pipelines%20%3E%20\(model\)%20list_field%20%3E%20\(schema\)) { items } 

type: "list"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

inferred: optional boolean

StreamGetResponse object { id, created_at, http, 7 more } 

id: string

Indicates a unique identifier for this stream.

created_at: string

formatdate-time

http: object { authentication, enabled, cors } 

authentication: boolean

Indicates that authentication is required for the HTTP endpoint.

enabled: boolean

Indicates that the HTTP endpoint is enabled.

cors: optional object { origins } 

Specifies the CORS options for the HTTP endpoint.

origins: optional array of string

modified_at: string

formatdate-time

name: string

Indicates the name of the Stream.

maxLength128

minLength1

version: number

Indicates the current version of this stream.

worker_binding: object { enabled } 

enabled: boolean

Indicates that the worker binding is enabled.

endpoint: optional string

Indicates the endpoint URL of this stream.

formaturi

format: optional object { type, decimal_encoding, timestamp_format, unstructured }  or object { type, compression, row_group_bytes } 

Defines the data format of the events.

One of the following:

Json object { type, decimal_encoding, timestamp_format, unstructured } 

type: "json"

decimal_encoding: optional "number" or "string" or "bytes"

One of the following:

"number"

"string"

"bytes"

timestamp_format: optional "rfc3339" or "unix_millis"

One of the following:

"rfc3339"

"unix_millis"

unstructured: optional boolean

Parquet object { type, compression, row_group_bytes } 

type: "parquet"

compression: optional "uncompressed" or "snappy" or "gzip" or 2 more

One of the following:

"uncompressed"

"snappy"

"gzip"

"zstd"

"lz4"

row_group_bytes: optional number

formatint64

minimum0

schema: optional object { fields, inferred } 

Defines the schema of the events in the data stream.

fields: optional array of [SourceField](https://developers.cloudflare.com/api/resources/pipelines#\(resource\)%20pipelines%20%3E%20\(model\)%20source_field%20%3E%20\(schema\))

One of the following:

Int32 object { type, metadata_key, name, 2 more } 

type: "int32"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Int64 object { type, metadata_key, name, 2 more } 

type: "int64"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Float32 object { type, metadata_key, name, 2 more } 

type: "float32"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Float64 object { type, metadata_key, name, 2 more } 

type: "float64"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Bool object { type, metadata_key, name, 2 more } 

type: "bool"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

String object { type, metadata_key, name, 2 more } 

type: "string"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Binary object { type, metadata_key, name, 2 more } 

type: "binary"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Timestamp object { type, metadata_key, name, 3 more } 

type: "timestamp"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

unit: optional "second" or "millisecond" or "microsecond" or "nanosecond"

One of the following:

"second"

"millisecond"

"microsecond"

"nanosecond"

Json object { type, metadata_key, name, 2 more } 

type: "json"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Struct = [StructField](https://developers.cloudflare.com/api/resources/pipelines#\(resource\)%20pipelines%20%3E%20\(model\)%20struct_field%20%3E%20\(schema\)) { fields, name } 

type: "struct"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

List = [ListField](https://developers.cloudflare.com/api/resources/pipelines#\(resource\)%20pipelines%20%3E%20\(model\)%20list_field%20%3E%20\(schema\)) { items } 

type: "list"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

inferred: optional boolean

StreamCreateResponse object { id, created_at, http, 7 more } 

id: string

Indicates a unique identifier for this stream.

created_at: string

formatdate-time

http: object { authentication, enabled, cors } 

authentication: boolean

Indicates that authentication is required for the HTTP endpoint.

enabled: boolean

Indicates that the HTTP endpoint is enabled.

cors: optional object { origins } 

Specifies the CORS options for the HTTP endpoint.

origins: optional array of string

modified_at: string

formatdate-time

name: string

Indicates the name of the Stream.

maxLength128

minLength1

version: number

Indicates the current version of this stream.

worker_binding: object { enabled } 

enabled: boolean

Indicates that the worker binding is enabled.

endpoint: optional string

Indicates the endpoint URL of this stream.

formaturi

format: optional object { type, decimal_encoding, timestamp_format, unstructured }  or object { type, compression, row_group_bytes } 

Defines the data format of the events.

One of the following:

Json object { type, decimal_encoding, timestamp_format, unstructured } 

type: "json"

decimal_encoding: optional "number" or "string" or "bytes"

One of the following:

"number"

"string"

"bytes"

timestamp_format: optional "rfc3339" or "unix_millis"

One of the following:

"rfc3339"

"unix_millis"

unstructured: optional boolean

Parquet object { type, compression, row_group_bytes } 

type: "parquet"

compression: optional "uncompressed" or "snappy" or "gzip" or 2 more

One of the following:

"uncompressed"

"snappy"

"gzip"

"zstd"

"lz4"

row_group_bytes: optional number

formatint64

minimum0

schema: optional object { fields, inferred } 

Defines the schema of the events in the data stream.

fields: optional array of [SourceField](https://developers.cloudflare.com/api/resources/pipelines#\(resource\)%20pipelines%20%3E%20\(model\)%20source_field%20%3E%20\(schema\))

One of the following:

Int32 object { type, metadata_key, name, 2 more } 

type: "int32"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Int64 object { type, metadata_key, name, 2 more } 

type: "int64"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Float32 object { type, metadata_key, name, 2 more } 

type: "float32"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Float64 object { type, metadata_key, name, 2 more } 

type: "float64"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Bool object { type, metadata_key, name, 2 more } 

type: "bool"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

String object { type, metadata_key, name, 2 more } 

type: "string"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Binary object { type, metadata_key, name, 2 more } 

type: "binary"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Timestamp object { type, metadata_key, name, 3 more } 

type: "timestamp"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

unit: optional "second" or "millisecond" or "microsecond" or "nanosecond"

One of the following:

"second"

"millisecond"

"microsecond"

"nanosecond"

Json object { type, metadata_key, name, 2 more } 

type: "json"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Struct = [StructField](https://developers.cloudflare.com/api/resources/pipelines#\(resource\)%20pipelines%20%3E%20\(model\)%20struct_field%20%3E%20\(schema\)) { fields, name } 

type: "struct"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

List = [ListField](https://developers.cloudflare.com/api/resources/pipelines#\(resource\)%20pipelines%20%3E%20\(model\)%20list_field%20%3E%20\(schema\)) { items } 

type: "list"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

inferred: optional boolean

StreamUpdateResponse object { id, created_at, http, 7 more } 

id: string

Indicates a unique identifier for this stream.

created_at: string

formatdate-time

http: object { authentication, enabled, cors } 

authentication: boolean

Indicates that authentication is required for the HTTP endpoint.

enabled: boolean

Indicates that the HTTP endpoint is enabled.

cors: optional object { origins } 

Specifies the CORS options for the HTTP endpoint.

origins: optional array of string

modified_at: string

formatdate-time

name: string

Indicates the name of the Stream.

maxLength128

minLength1

version: number

Indicates the current version of this stream.

worker_binding: object { enabled } 

enabled: boolean

Indicates that the worker binding is enabled.

endpoint: optional string

Indicates the endpoint URL of this stream.

formaturi

format: optional object { type, decimal_encoding, timestamp_format, unstructured }  or object { type, compression, row_group_bytes } 

Defines the data format of the events.

One of the following:

Json object { type, decimal_encoding, timestamp_format, unstructured } 

type: "json"

decimal_encoding: optional "number" or "string" or "bytes"

One of the following:

"number"

"string"

"bytes"

timestamp_format: optional "rfc3339" or "unix_millis"

One of the following:

"rfc3339"

"unix_millis"

unstructured: optional boolean

Parquet object { type, compression, row_group_bytes } 

type: "parquet"

compression: optional "uncompressed" or "snappy" or "gzip" or 2 more

One of the following:

"uncompressed"

"snappy"

"gzip"

"zstd"

"lz4"

row_group_bytes: optional number

formatint64

minimum0

schema: optional object { fields, inferred } 

Defines the schema of the events in the data stream.

fields: optional array of [SourceField](https://developers.cloudflare.com/api/resources/pipelines#\(resource\)%20pipelines%20%3E%20\(model\)%20source_field%20%3E%20\(schema\))

One of the following:

Int32 object { type, metadata_key, name, 2 more } 

type: "int32"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Int64 object { type, metadata_key, name, 2 more } 

type: "int64"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Float32 object { type, metadata_key, name, 2 more } 

type: "float32"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Float64 object { type, metadata_key, name, 2 more } 

type: "float64"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Bool object { type, metadata_key, name, 2 more } 

type: "bool"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

String object { type, metadata_key, name, 2 more } 

type: "string"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Binary object { type, metadata_key, name, 2 more } 

type: "binary"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Timestamp object { type, metadata_key, name, 3 more } 

type: "timestamp"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

unit: optional "second" or "millisecond" or "microsecond" or "nanosecond"

One of the following:

"second"

"millisecond"

"microsecond"

"nanosecond"

Json object { type, metadata_key, name, 2 more } 

type: "json"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

Struct = [StructField](https://developers.cloudflare.com/api/resources/pipelines#\(resource\)%20pipelines%20%3E%20\(model\)%20struct_field%20%3E%20\(schema\)) { fields, name } 

type: "struct"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

List = [ListField](https://developers.cloudflare.com/api/resources/pipelines#\(resource\)%20pipelines%20%3E%20\(model\)%20list_field%20%3E%20\(schema\)) { items } 

type: "list"

metadata_key: optional string

name: optional string

required: optional boolean

sql_name: optional string

inferred: optional boolean

StreamDeleteResponse = unknown

[ Previous

* * *

Values ](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/subresources/values)[ Next

* * *

Sinks ](https://developers.cloudflare.com/api/resources/pipelines/subresources/sinks)
