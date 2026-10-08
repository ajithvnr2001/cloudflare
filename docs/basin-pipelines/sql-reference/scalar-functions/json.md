---
url: https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/json/
title: JSON functions \u00b7 Cloudflare Basin Pipelines Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:26.228500+00:00
---

# JSON functions · Cloudflare Basin Pipelines Docs

> Source: https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/json/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)
  3. /…

SQL reference

  4. /Scalar functions
  5. /JSON functions



# JSON functions

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/json/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSQL functions json_contains json_get json_get_str json_get_int json_get_float json_get_bool json_get_json json_as_text json_lengthJson path functions extract_json extract_json_string

Basin Pipelines provides two set of JSON functions, the first based on PostgreSQL's SQL functions and syntax, and the second based on the [JSONPath ↗︎](https://jsonpath.com/) standard.

## SQL functions

The SQL functions provide basic JSON parsing functions similar to those found in PostgreSQL.

### json_contains

Returns `true` if the JSON string contains the specified key(s).
    
    
    SELECT json_contains('{"a": 1, "b": 2, "c": 3}', 'a') FROM source;
    true

Also available via the `?` operator:
    
    
    SELECT '{"a": 1, "b": 2, "c": 3}' ? 'a' FROM source;
    true

### json_get

Retrieves the value from a JSON string by the specified path (keys). Returns the value as its native type (string, int, etc.).
    
    
    SELECT json_get('{"a": {"b": 2}}', 'a', 'b') FROM source;
    2

Also available via the `->` operator:
    
    
    SELECT '{"a": {"b": 2}}'->'a'->'b' FROM source;
    2

Various permutations of `json_get` functions are available for retrieving values as a specific type, or you can use SQL type annotations:
    
    
    SELECT json_get('{"a": {"b": 2}}', 'a', 'b')::int FROM source;
    2

### json_get_str

Retrieves a string value from a JSON string by the specified path. Returns an empty string if the value does not exist or is not a string.
    
    
    SELECT json_get_str('{"a": {"b": "hello"}}', 'a', 'b') FROM source;
    "hello"

### json_get_int

Retrieves an integer value from a JSON string by the specified path. Returns `0` if the value does not exist or is not an integer.
    
    
    SELECT json_get_int('{"a": {"b": 42}}', 'a', 'b') FROM source;
    42

### json_get_float

Retrieves a float value from a JSON string by the specified path. Returns `0.0` if the value does not exist or is not a float.
    
    
    SELECT json_get_float('{"a": {"b": 3.14}}', 'a', 'b') FROM source;
    3.14

### json_get_bool

Retrieves a boolean value from a JSON string by the specified path. Returns `false` if the value does not exist or is not a boolean.
    
    
    SELECT json_get_bool('{"a": {"b": true}}', 'a', 'b') FROM source;
    true

### json_get_json

Retrieves a nested JSON string from a JSON string by the specified path. The value is returned as raw JSON.
    
    
    SELECT json_get_json('{"a": {"b": {"c": 1}}}', 'a', 'b') FROM source;
    '{"c": 1}'

### json_as_text

Retrieves any value from a JSON string by the specified path and returns it as a string, regardless of the original type.
    
    
    SELECT json_as_text('{"a": {"b": 42}}', 'a', 'b') FROM source;
    "42"

Also available via the `->>` operator:
    
    
    SELECT '{"a": {"b": 42}}'->>'a'->>'b' FROM source;
    "42"

### json_length

Returns the length of a JSON object or array at the specified path. Returns `0` if the path does not exist or is not an object/array.
    
    
    SELECT json_length('{"a": [1, 2, 3]}', 'a') FROM source;
    3

## Json path functions

JSON functions provide basic json parsing functions using [JsonPath ↗︎](https://goessner.net/articles/JsonPath/), an evolving standard for querying JSON objects.

### extract_json

Returns the JSON elements in the first argument that match the JsonPath in the second argument. The returned value is an array of json strings.
    
    
    SELECT extract_json('{"a": 1, "b": 2, "c": 3}', '$.a') FROM source;
    ['1']

### extract_json_string

Returns an unescaped String for the first item matching the JsonPath, if it is a string.
    
    
    SELECT extract_json_string('{"a": "a", "b": 2, "c": 3}', '$.a') FROM source;
    'a'

[PreviousRegex functions](https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/regex/)[NextTime and date functions](https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/time-and-date/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/basin-pipelines/sql-reference/scalar-functions/json.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
