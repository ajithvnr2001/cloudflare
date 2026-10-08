---
url: https://developers.cloudflare.com/basin-sql/sql-reference/scalar-functions/
title: Scalar functions \u00b7 Basin SQL docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:28.789444+00:00
---

# Scalar functions · Basin SQL docs

> Source: https://developers.cloudflare.com/basin-sql/sql-reference/scalar-functions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Basin SQL](https://developers.cloudflare.com/basin-sql/)
  3. /[SQL reference](https://developers.cloudflare.com/basin-sql/sql-reference/)
  4. /Scalar functions



# Scalar functions

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/basin-sql/sql-reference/scalar-functions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCore functions arrow_cast arrow_typeof coalesce get_field greatest least named_struct nullif nvl nvl2 overlay structCrypto functions digest md5 sha224 sha256 sha384 sha512Datetime functions current_date current_time date_bin date_part date_trunc from_unixtime make_date make_time now to_char to_date to_local_time to_time to_timestamp to_timestamp_micros to_timestamp_millis to_timestamp_nanos to_timestamp_seconds to_unixtimeEncoding functions decode encodeJSON functions json_as_text json_contains json_get json_get_array json_get_bool json_get_float json_get_int json_get_json json_get_str json_lengthMath functions abs cbrt ceil degrees exp factorial floor gcd Hyperbolic functions isnan iszero lcm ln log log2 log10 nanvl pi power radians random round signum sqrt Trigonometric functions truncRegex functions regexp_count regexp_instr regexp_like regexp_match regexp_replaceString functions ascii bit_length btrim chr concat concat_ws contains ends_with levenshtein lower ltrim octet_length repeat replace rtrim split_part starts_with to_hex upper uuidUnicode functions character_length find_in_set initcap left lpad reverse right rpad strpos substr substr_index translate

Scalar functions transform individual values and can be used in `SELECT`, `WHERE`, `GROUP BY`, `HAVING`, and `ORDER BY` clauses.

* * *

## Core functions

### arrow_cast

Casts an expression to a specific Arrow data type by string name.
    
    
    SELECT arrow_cast(total_amount, 'Float32') AS amount_f32
    FROM my_namespace.sales_data
    WHERE total_amount IS NOT NULL
    LIMIT 1

### arrow_typeof

Returns the Arrow data type name of an expression.
    
    
    SELECT arrow_typeof(total_amount) AS amount_type,
           arrow_typeof(customer_id) AS id_type
    FROM my_namespace.sales_data
    LIMIT 1

### coalesce

Returns the first non-NULL argument.
    
    
    SELECT coalesce(department, region, 'unknown') AS first_val
    FROM my_namespace.sales_data
    LIMIT 5

### get_field

Extracts a field from a struct by name.
    
    
    SELECT get_field(named_struct('customer', customer_id, 'amount', total_amount), 'amount') AS amt
    FROM my_namespace.sales_data
    WHERE total_amount IS NOT NULL
    LIMIT 1

### greatest

Returns the largest value from a list of arguments.
    
    
    SELECT greatest(total_amount, unit_price, quantity) AS max_val
    FROM my_namespace.sales_data
    WHERE total_amount IS NOT NULL
    LIMIT 5

### least

Returns the smallest value from a list of arguments.
    
    
    SELECT least(total_amount, unit_price, quantity) AS min_val
    FROM my_namespace.sales_data
    WHERE total_amount IS NOT NULL
    LIMIT 5

### named_struct

Creates a struct with named fields from key-value pairs.
    
    
    SELECT named_struct('customer', customer_id, 'amount', total_amount) AS info
    FROM my_namespace.sales_data
    WHERE total_amount IS NOT NULL
    LIMIT 1

### nullif

Returns NULL if both arguments are equal, otherwise returns the first argument.
    
    
    SELECT nullif(department, 'Unknown') AS dept
    FROM my_namespace.sales_data
    LIMIT 5

### nvl

Returns the second argument if the first is NULL. Alias: `ifnull`.
    
    
    SELECT nvl(department, 'N/A') AS dept
    FROM my_namespace.sales_data
    LIMIT 5

### nvl2

Returns the second argument if the first is not NULL, otherwise returns the third.
    
    
    SELECT nvl2(department, 'has_dept', 'no_dept') AS dept_status
    FROM my_namespace.sales_data
    LIMIT 5

### overlay

Replaces a substring at a given position.
    
    
    SELECT customer_id,
           overlay(customer_id PLACING 'XX' FROM 1 FOR 2) AS masked
    FROM my_namespace.sales_data
    LIMIT 3

### struct

Creates a struct with positional fields. Alias: `row`.
    
    
    SELECT struct(customer_id, total_amount, region) AS info
    FROM my_namespace.sales_data
    WHERE total_amount IS NOT NULL
    LIMIT 1

* * *

## Crypto functions

### digest

Returns a hash of a string using a specified algorithm. Supported algorithms: `md5`, `sha224`, `sha256`, `sha384`, `sha512`.
    
    
    SELECT customer_id, digest(customer_id, 'sha256') AS hash
    FROM my_namespace.sales_data
    LIMIT 1

### md5

Returns the MD5 hash of a string.
    
    
    SELECT customer_id, md5(customer_id) AS hash
    FROM my_namespace.sales_data
    LIMIT 1

### sha224

Returns the SHA-224 hash of a string.
    
    
    SELECT sha224(customer_id) AS hash
    FROM my_namespace.sales_data
    LIMIT 1

### sha256

Returns the SHA-256 hash of a string.
    
    
    SELECT customer_id, sha256(customer_id) AS hash
    FROM my_namespace.sales_data
    LIMIT 1

### sha384

Returns the SHA-384 hash of a string.
    
    
    SELECT sha384(customer_id) AS hash
    FROM my_namespace.sales_data
    LIMIT 1

### sha512

Returns the SHA-512 hash of a string.
    
    
    SELECT sha512(customer_id) AS hash
    FROM my_namespace.sales_data
    LIMIT 1

* * *

## Datetime functions

### current_date

Returns today's date. Alias: `today`.
    
    
    SELECT current_date() AS today_date
    FROM my_namespace.sales_data
    LIMIT 1

### current_time

Returns the current time. Precision is quantized to 10ms boundaries.
    
    
    SELECT current_time() AS now_time
    FROM my_namespace.sales_data
    LIMIT 1

### date_bin

Bins a timestamp into fixed-size intervals aligned to an origin.
    
    
    SELECT date_bin(INTERVAL '1 hour', timestamp, '2025-01-01T00:00:00Z') AS hour_bin,
           COUNT(*) AS cnt
    FROM my_namespace.sales_data
    GROUP BY date_bin(INTERVAL '1 hour', timestamp, '2025-01-01T00:00:00Z')
    ORDER BY hour_bin
    LIMIT 5

### date_part

Extracts a component from a timestamp. Alias: `datepart`.

Supported fields: `year`, `month`, `day`, `hour`, `minute`, `second`, `millisecond`, `microsecond`, `week`, `dow`, `doy`, `quarter`, `epoch`.
    
    
    SELECT date_part('hour', timestamp) AS hr,
           date_part('minute', timestamp) AS mn
    FROM my_namespace.sales_data
    LIMIT 1

### date_trunc

Truncates a timestamp to a specified unit. Alias: `datetrunc`.

Supported units: `year`, `month`, `week`, `day`, `hour`, `minute`, `second`.
    
    
    SELECT date_trunc('day', timestamp) AS day_trunc, COUNT(*) AS cnt
    FROM my_namespace.sales_data
    GROUP BY date_trunc('day', timestamp)
    ORDER BY day_trunc
    LIMIT 5

### from_unixtime

Converts a Unix epoch (seconds) to a timestamp.
    
    
    SELECT from_unixtime(1770000000) AS ts
    FROM my_namespace.sales_data
    LIMIT 1

### make_date

Constructs a date from year, month, and day components.
    
    
    SELECT make_date(2026, 3, 1) AS d
    FROM my_namespace.sales_data
    LIMIT 1

### make_time

Constructs a time from hour, minute, and second components.
    
    
    SELECT make_time(14, 30, 0) AS t
    FROM my_namespace.sales_data
    LIMIT 1

### now

Returns the current timestamp. Aliases: `current_timestamp`.

Precision is quantized to 10ms boundaries.
    
    
    SELECT now() AS current_ts
    FROM my_namespace.sales_data
    LIMIT 1

### to_char

Formats a timestamp as a string using strftime format. Alias: `date_format`.
    
    
    SELECT to_char(timestamp, '%Y-%m-%d %H:%M') AS formatted
    FROM my_namespace.sales_data
    LIMIT 1

### to_date

Parses a date from a string using a format pattern.
    
    
    SELECT to_date('2026-03-01', '%Y-%m-%d') AS d
    FROM my_namespace.sales_data
    LIMIT 1

### to_local_time

Strips timezone information from a timestamp.
    
    
    SELECT to_local_time(timestamp) AS local_ts
    FROM my_namespace.sales_data
    LIMIT 1

### to_time

Parses a time from a string using a format pattern.
    
    
    SELECT to_time('14:30:00', '%H:%M:%S') AS t
    FROM my_namespace.sales_data
    LIMIT 1

### to_timestamp

Parses a timestamp from a string using a format pattern.
    
    
    SELECT to_timestamp('2026-03-01 12:00:00', '%Y-%m-%d %H:%M:%S') AS ts
    FROM my_namespace.sales_data
    LIMIT 1

### to_timestamp_micros

Converts microseconds since Unix epoch to a timestamp.
    
    
    SELECT to_timestamp_micros(1770000000000000) AS ts
    FROM my_namespace.sales_data
    LIMIT 1

### to_timestamp_millis

Converts milliseconds since Unix epoch to a timestamp.
    
    
    SELECT to_timestamp_millis(1770000000000) AS ts
    FROM my_namespace.sales_data
    LIMIT 1

### to_timestamp_nanos

Converts nanoseconds since Unix epoch to a timestamp. Large values may overflow.
    
    
    SELECT to_timestamp_nanos(1770000000000000000) AS ts
    FROM my_namespace.sales_data
    LIMIT 1

### to_timestamp_seconds

Converts seconds since Unix epoch to a timestamp.
    
    
    SELECT to_timestamp_seconds(1770000000) AS ts
    FROM my_namespace.sales_data
    LIMIT 1

### to_unixtime

Converts a timestamp to a Unix epoch (seconds).
    
    
    SELECT to_unixtime(timestamp) AS epoch
    FROM my_namespace.sales_data
    LIMIT 1

* * *

## Encoding functions

### decode

Decodes a string to binary data. Supported encoding: `base64`.
    
    
    SELECT decode('aGVsbG8=', 'base64') AS raw
    FROM my_namespace.sales_data
    LIMIT 1

### encode

Encodes binary data to a string. Supported encoding: `base64`.
    
    
    SELECT encode(CAST('hello' AS BYTEA), 'base64') AS b64
    FROM my_namespace.sales_data
    LIMIT 1

* * *

## JSON functions

### json_as_text

Returns any JSON value as unquoted text.
    
    
    SELECT json_as_text(doc, 'description') AS description
    FROM my_namespace.sales_data
    LIMIT 5

### json_contains

Returns true if the specified key path exists in the JSON.
    
    
    SELECT customer_id, json_contains(doc, 'email') AS has_email
    FROM my_namespace.sales_data
    LIMIT 5

### json_get

Extracts a value by key path. Returns a union type — use the typed variants (`json_get_str`, `json_get_int`, etc.) for predictable results.
    
    
    SELECT json_get(doc, 'name') AS name
    FROM my_namespace.sales_data
    LIMIT 5

### json_get_array

Returns a JSON array as a list of strings.
    
    
    SELECT json_get_array(doc, 'tags') AS tags
    FROM my_namespace.sales_data
    LIMIT 5

### json_get_bool

Returns a boolean value from a JSON column by key path.
    
    
    SELECT json_get_bool(doc, 'active') AS is_active
    FROM my_namespace.sales_data
    LIMIT 5

### json_get_float

Returns a float value from a JSON column by key path.
    
    
    SELECT json_get_float(doc, 'price') AS price
    FROM my_namespace.sales_data
    LIMIT 5

### json_get_int

Returns an integer value from a JSON column by key path.
    
    
    SELECT json_get_int(doc, 'age') AS age
    FROM my_namespace.sales_data
    LIMIT 5

### json_get_json

Returns nested JSON as a raw JSON string.
    
    
    SELECT json_get_json(doc, 'metadata') AS metadata
    FROM my_namespace.sales_data
    LIMIT 5

### json_get_str

Returns a string value from a JSON column by key path.
    
    
    SELECT json_get_str(doc, 'name') AS name
    FROM my_namespace.sales_data
    LIMIT 5

### json_length

Returns the length of a JSON array or object.
    
    
    SELECT json_length(doc, 'items') AS item_count
    FROM my_namespace.sales_data
    LIMIT 5

* * *

## Math functions

### abs

Returns the absolute value of a number.
    
    
    SELECT abs(total_amount - 500) AS distance_from_500
    FROM my_namespace.sales_data
    WHERE total_amount IS NOT NULL
    LIMIT 5

### cbrt

Returns the cube root of a number.
    
    
    SELECT cbrt(CAST(quantity AS DOUBLE)) AS cbrt_qty
    FROM my_namespace.sales_data
    WHERE quantity IS NOT NULL
    LIMIT 5

### ceil

Returns the smallest integer greater than or equal to a number.
    
    
    SELECT ceil(total_amount) AS rounded_up
    FROM my_namespace.sales_data
    WHERE total_amount IS NOT NULL
    LIMIT 5

### degrees

Converts radians to degrees.
    
    
    SELECT degrees(pi()) AS full_circle
    FROM my_namespace.sales_data
    LIMIT 1

### exp

Returns _e_ raised to the given power.
    
    
    SELECT exp(total_amount / 1000.0) AS exp_val
    FROM my_namespace.sales_data
    WHERE total_amount IS NOT NULL
    LIMIT 5

### factorial

Returns the factorial of a non-negative integer.
    
    
    SELECT factorial(5) AS fact5
    FROM my_namespace.sales_data
    LIMIT 1

### floor

Returns the largest integer less than or equal to a number.
    
    
    SELECT floor(total_amount) AS rounded_down
    FROM my_namespace.sales_data
    WHERE total_amount IS NOT NULL
    LIMIT 5

### gcd

Returns the greatest common divisor of two integers.
    
    
    SELECT gcd(12, 8) AS gcd_val
    FROM my_namespace.sales_data
    LIMIT 1

### Hyperbolic functions

`sinh`, `cosh`, `tanh`, `asinh`, `acosh`, `atanh`
    
    
    SELECT sinh(1.0) AS sh, cosh(1.0) AS ch, tanh(1.0) AS th
    FROM my_namespace.sales_data
    LIMIT 1

### isnan

Returns true if the value is NaN.
    
    
    SELECT isnan(0.0 / 0.0) AS is_nan
    FROM my_namespace.sales_data
    LIMIT 1

### iszero

Returns true if the value is zero.
    
    
    SELECT iszero(0.0) AS is_zero
    FROM my_namespace.sales_data
    LIMIT 1

### lcm

Returns the least common multiple of two integers.
    
    
    SELECT lcm(4, 6) AS lcm_val
    FROM my_namespace.sales_data
    LIMIT 1

### ln

Returns the natural logarithm.
    
    
    SELECT ln(total_amount) AS ln_val
    FROM my_namespace.sales_data
    WHERE total_amount > 0
    LIMIT 5

### log

Returns the logarithm of a value for a given base.
    
    
    SELECT log(10.0, total_amount) AS log10_val
    FROM my_namespace.sales_data
    WHERE total_amount > 0
    LIMIT 5

### log2

Returns the base-2 logarithm.
    
    
    SELECT log2(total_amount) AS log2_val
    FROM my_namespace.sales_data
    WHERE total_amount > 0
    LIMIT 5

### log10

Returns the base-10 logarithm.
    
    
    SELECT log10(total_amount) AS log10_val
    FROM my_namespace.sales_data
    WHERE total_amount > 0
    LIMIT 5

### nanvl

Returns the first argument if it is not NaN, otherwise returns the second.
    
    
    SELECT nanvl(0.0 / 0.0, -1.0) AS safe_val
    FROM my_namespace.sales_data
    LIMIT 1

### pi

Returns the value of pi.
    
    
    SELECT pi() AS pi_val
    FROM my_namespace.sales_data
    LIMIT 1

### power

Raises a number to a power. Alias: `pow`.
    
    
    SELECT power(total_amount, 2.0) AS amount_squared
    FROM my_namespace.sales_data
    WHERE total_amount IS NOT NULL
    LIMIT 5

### radians

Converts degrees to radians.
    
    
    SELECT radians(180.0) AS pi_val
    FROM my_namespace.sales_data
    LIMIT 1

### random

Returns a random float between 0 and 1.
    
    
    SELECT random() AS rnd
    FROM my_namespace.sales_data
    LIMIT 1

### round

Rounds a number to a specified number of decimal places.
    
    
    SELECT round(total_amount, 2) AS rounded
    FROM my_namespace.sales_data
    WHERE total_amount IS NOT NULL
    LIMIT 5

### signum

Returns the sign of a number: -1, 0, or 1.
    
    
    SELECT signum(total_amount - 500) AS sign_val
    FROM my_namespace.sales_data
    WHERE total_amount IS NOT NULL
    LIMIT 5

### sqrt

Returns the square root of a number.
    
    
    SELECT sqrt(CAST(quantity AS DOUBLE)) AS sqrt_qty
    FROM my_namespace.sales_data
    WHERE quantity IS NOT NULL
    LIMIT 5

### Trigonometric functions

`sin`, `cos`, `tan`, `asin`, `acos`, `atan`, `atan2`, `cot`
    
    
    SELECT sin(1.0) AS s, cos(1.0) AS c, tan(1.0) AS t,
           asin(0.5) AS as_val, acos(0.5) AS ac_val, atan(1.0) AS at_val
    FROM my_namespace.sales_data
    LIMIT 1

### trunc

Truncates a number to a specified number of decimal places.
    
    
    SELECT trunc(total_amount, 0) AS truncated
    FROM my_namespace.sales_data
    WHERE total_amount IS NOT NULL
    LIMIT 5

* * *

## Regex functions

### regexp_count

Returns the number of matches of a pattern in a string.
    
    
    SELECT department, regexp_count(department, '[aeiou]') AS vowels
    FROM my_namespace.sales_data
    WHERE department IS NOT NULL
    LIMIT 5

### regexp_instr

Returns the position of the first match of a pattern.
    
    
    SELECT department, regexp_instr(department, '[0-9]') AS digit_pos
    FROM my_namespace.sales_data
    WHERE department IS NOT NULL
    LIMIT 5

### regexp_like

Returns true if a string matches a regular expression pattern.
    
    
    SELECT department, regexp_like(department, '^[A-Z]{2}') AS starts_two_caps
    FROM my_namespace.sales_data
    WHERE department IS NOT NULL
    LIMIT 5

### regexp_match

Returns the first match of a pattern as an array.
    
    
    SELECT department, regexp_match(department, '([A-Z][a-z]+)') AS first_word
    FROM my_namespace.sales_data
    WHERE department IS NOT NULL
    LIMIT 3

### regexp_replace

Replaces matches of a pattern with a replacement string.
    
    
    SELECT department, regexp_replace(department, '[0-9]', '#') AS no_digits
    FROM my_namespace.sales_data
    WHERE department IS NOT NULL
    LIMIT 5

* * *

## String functions

### ascii

Returns the ASCII code of the first character.
    
    
    SELECT customer_id, ascii(customer_id) AS first_code
    FROM my_namespace.sales_data
    LIMIT 3

### bit_length

Returns the length of a string in bits.
    
    
    SELECT customer_id, bit_length(customer_id) AS bits
    FROM my_namespace.sales_data
    LIMIT 3

### btrim

Trims characters from both sides of a string. Alias: `trim`.
    
    
    SELECT btrim('  hello  ') AS trimmed
    FROM my_namespace.sales_data
    LIMIT 1

### chr

Returns the character for a given ASCII code.
    
    
    SELECT chr(65) AS letter
    FROM my_namespace.sales_data
    LIMIT 1

### concat

Concatenates two or more strings.
    
    
    SELECT concat(department, ' - ', region) AS label
    FROM my_namespace.sales_data
    WHERE department IS NOT NULL
    LIMIT 5

### concat_ws

Concatenates strings with a separator.
    
    
    SELECT concat_ws('/', region, department) AS path
    FROM my_namespace.sales_data
    WHERE department IS NOT NULL
    LIMIT 5

### contains

Returns true if a string contains a substring.
    
    
    SELECT customer_id, contains(department, 'Sales') AS is_sales
    FROM my_namespace.sales_data
    WHERE department IS NOT NULL
    LIMIT 5

### ends_with

Returns true if a string ends with a suffix.
    
    
    SELECT customer_id, ends_with(department, 'ing') AS ends_ing
    FROM my_namespace.sales_data
    WHERE department IS NOT NULL
    LIMIT 5

### levenshtein

Returns the Levenshtein edit distance between two strings.
    
    
    SELECT department, levenshtein(department, 'Engineering') AS dist
    FROM my_namespace.sales_data
    WHERE department IS NOT NULL
    LIMIT 5

### lower

Converts a string to lowercase.
    
    
    SELECT lower(department) AS dept_lower
    FROM my_namespace.sales_data
    LIMIT 5

### ltrim

Trims characters from the left side of a string.
    
    
    SELECT ltrim('  hello') AS trimmed
    FROM my_namespace.sales_data
    LIMIT 1

### octet_length

Returns the length of a string in bytes.
    
    
    SELECT customer_id, octet_length(customer_id) AS bytes
    FROM my_namespace.sales_data
    LIMIT 3

### repeat

Repeats a string a given number of times.
    
    
    SELECT repeat(region, 2) AS doubled
    FROM my_namespace.sales_data
    LIMIT 3

### replace

Replaces all occurrences of a substring.
    
    
    SELECT department, replace(department, ' ', '_') AS underscored
    FROM my_namespace.sales_data
    WHERE department IS NOT NULL
    LIMIT 5

### rtrim

Trims characters from the right side of a string.
    
    
    SELECT rtrim('hello  ') AS trimmed
    FROM my_namespace.sales_data
    LIMIT 1

### split_part

Splits a string by a delimiter and returns the specified part (1-indexed).
    
    
    SELECT customer_id, split_part(customer_id, '-', 1) AS first_part
    FROM my_namespace.sales_data
    WHERE customer_id IS NOT NULL
    LIMIT 5

### starts_with

Returns true if a string starts with a prefix.
    
    
    SELECT customer_id, starts_with(department, 'Eng') AS is_eng
    FROM my_namespace.sales_data
    WHERE department IS NOT NULL
    LIMIT 5

### to_hex

Converts an integer to a hexadecimal string.
    
    
    SELECT to_hex(255) AS hex_ff
    FROM my_namespace.sales_data
    LIMIT 1

### upper

Converts a string to uppercase.
    
    
    SELECT upper(region) AS region_upper
    FROM my_namespace.sales_data
    LIMIT 5

### uuid

Generates a random UUID.
    
    
    SELECT uuid() AS new_id
    FROM my_namespace.sales_data
    LIMIT 1

* * *

## Unicode functions

### character_length

Returns the number of characters in a string. Aliases: `length`, `char_length`.
    
    
    SELECT department, character_length(department) AS len
    FROM my_namespace.sales_data
    WHERE department IS NOT NULL
    LIMIT 5

### find_in_set

Returns the position of a string within a comma-separated list.
    
    
    SELECT find_in_set('North', 'South,North,East,West') AS pos
    FROM my_namespace.sales_data
    LIMIT 1

### initcap

Capitalizes the first letter of each word.
    
    
    SELECT initcap('hello world') AS capped
    FROM my_namespace.sales_data
    LIMIT 1

### left

Returns the leftmost _n_ characters of a string.
    
    
    SELECT department, left(department, 5) AS prefix
    FROM my_namespace.sales_data
    WHERE department IS NOT NULL
    LIMIT 5

### lpad

Left-pads a string to a specified length.
    
    
    SELECT region, lpad(region, 15, '.') AS padded
    FROM my_namespace.sales_data
    LIMIT 5

### reverse

Reverses a string.
    
    
    SELECT department, reverse(department) AS rev
    FROM my_namespace.sales_data
    WHERE department IS NOT NULL
    LIMIT 5

### right

Returns the rightmost _n_ characters of a string.
    
    
    SELECT department, right(department, 3) AS suffix
    FROM my_namespace.sales_data
    WHERE department IS NOT NULL
    LIMIT 5

### rpad

Right-pads a string to a specified length.
    
    
    SELECT region, rpad(region, 15, '.') AS padded
    FROM my_namespace.sales_data
    LIMIT 5

### strpos

Returns the position of a substring (1-indexed). Aliases: `instr`, `position`.
    
    
    SELECT department, strpos(department, 'a') AS a_pos
    FROM my_namespace.sales_data
    WHERE department IS NOT NULL
    LIMIT 5

### substr

Returns a substring starting at a position for a given length. Alias: `substring`.
    
    
    SELECT department, substr(department, 1, 8) AS first_eight
    FROM my_namespace.sales_data
    WHERE department IS NOT NULL
    LIMIT 5

### substr_index

Returns the substring before the _n_ -th occurrence of a delimiter. Alias: `substring_index`.
    
    
    SELECT customer_id, substr_index(customer_id, '-', 1) AS first_segment
    FROM my_namespace.sales_data
    WHERE customer_id IS NOT NULL
    LIMIT 5

### translate

Replaces characters in a string based on a mapping.
    
    
    SELECT department, translate(department, 'aeiou', '12345') AS coded
    FROM my_namespace.sales_data
    WHERE department IS NOT NULL
    LIMIT 5

[PreviousOverview](https://developers.cloudflare.com/basin-sql/sql-reference/)[NextAggregate functions](https://developers.cloudflare.com/basin-sql/sql-reference/aggregate-functions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/basin-sql/sql-reference/scalar-functions.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
