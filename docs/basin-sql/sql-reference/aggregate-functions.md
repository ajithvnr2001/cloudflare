---
url: https://developers.cloudflare.com/basin-sql/sql-reference/aggregate-functions/
title: Aggregate functions \u00b7 Basin SQL docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:27.943606+00:00
---

# Aggregate functions · Basin SQL docs

> Source: https://developers.cloudflare.com/basin-sql/sql-reference/aggregate-functions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Basin SQL](https://developers.cloudflare.com/basin-sql/)
  3. /[SQL reference](https://developers.cloudflare.com/basin-sql/sql-reference/)
  4. /Aggregate functions



# Aggregate functions

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/basin-sql/sql-reference/aggregate-functions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBasic aggregates COUNT SUM AVG MIN MAX MEDIAN PERCENTILE_CONTApproximate aggregates approx_percentile_cont approx_percentile_cont_with_weight approx_median approx_distinct approx_top_kStatistical aggregates var / var_samp var_pop stddev / stddev_samp stddev_pop covar_samp covar_pop corr regr_slope regr_intercept regr_count regr_r2 regr_avgx regr_avgy regr_sxx regr_syy regr_sxyBitwise aggregates bit_and bit_or bit_xorBoolean aggregates bool_and bool_orPositional aggregates first_value last_valueCollection aggregates array_agg string_agg

Aggregate functions collapse multiple rows into a single result. They are used with `GROUP BY` to compute summaries per group, or without `GROUP BY` to compute a single result across all rows.

Most aggregates accept a `DISTINCT` modifier, for example `COUNT(DISTINCT customer_id)` or `SUM(DISTINCT total_amount)`.

Note

On large datasets, prefer the approximate aggregates (`approx_distinct`, `approx_median`, `approx_percentile_cont`) over their exact counterparts for lower memory and compute.

* * *

## Basic aggregates

### COUNT

Counts rows. `COUNT(*)` counts all rows. `COUNT(column)` counts non-NULL values.
    
    
    SELECT COUNT(*) AS total_rows
    FROM my_namespace.sales_data
    
    SELECT department, COUNT(*) AS dept_count
    FROM my_namespace.sales_data
    GROUP BY department
    ORDER BY dept_count DESC

### SUM

Returns the sum of values in a column.
    
    
    SELECT SUM(total_amount) AS grand_total
    FROM my_namespace.sales_data
    
    SELECT department, SUM(total_amount) AS dept_total
    FROM my_namespace.sales_data
    GROUP BY department
    ORDER BY dept_total DESC

### AVG

Returns the average of values in a column. Alias: `mean`.
    
    
    SELECT AVG(total_amount) AS avg_amount
    FROM my_namespace.sales_data
    
    SELECT department, AVG(total_amount) AS avg_amount
    FROM my_namespace.sales_data
    GROUP BY department
    ORDER BY avg_amount DESC

### MIN

Returns the minimum value. Works on numeric and string columns.
    
    
    SELECT MIN(total_amount) AS min_amount, MIN(customer_id) AS first_customer
    FROM my_namespace.sales_data
    
    SELECT department, MIN(total_amount) AS min_amount
    FROM my_namespace.sales_data
    GROUP BY department

### MAX

Returns the maximum value. Works on numeric and string columns.
    
    
    SELECT MAX(total_amount) AS max_amount, MAX(customer_id) AS last_customer
    FROM my_namespace.sales_data
    
    SELECT department, MAX(total_amount) AS max_amount
    FROM my_namespace.sales_data
    GROUP BY department

### MEDIAN

Returns the exact median value. For large datasets, use `approx_median` instead.
    
    
    SELECT MEDIAN(total_amount) AS median_amount
    FROM my_namespace.sales_data
    
    SELECT department, MEDIAN(total_amount) AS median_amount
    FROM my_namespace.sales_data
    GROUP BY department

### PERCENTILE_CONT

Returns the exact value at a given percentile using `WITHIN GROUP (ORDER BY ...)`. The percentile parameter must be between `0.0` and `1.0` inclusive. For large datasets, use `approx_percentile_cont` instead.
    
    
    SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY total_amount) AS median,
           PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY total_amount) AS p95
    FROM my_namespace.sales_data

Note

`PERCENTILE_DISC` is not supported. Use `PERCENTILE_CONT` or `approx_percentile_cont`.

* * *

## Approximate aggregates

Approximate aggregation functions produce statistically estimated results while using significantly less memory and compute than their exact counterparts. Use them when analyzing large datasets and an approximate result is acceptable.

### approx_percentile_cont

Returns the approximate value at a given percentile using a T-Digest algorithm. The percentile parameter must be between `0.0` and `1.0` inclusive.
    
    
    SELECT approx_percentile_cont(total_amount, 0.5) AS median,
           approx_percentile_cont(total_amount, 0.95) AS p95
    FROM my_namespace.sales_data
    
    SELECT department,
           approx_percentile_cont(total_amount, 0.5) AS median
    FROM my_namespace.sales_data
    GROUP BY department
    ORDER BY median DESC

### approx_percentile_cont_with_weight

Returns the approximate weighted percentile. Rows are weighted by the `weight` column.
    
    
    SELECT approx_percentile_cont_with_weight(unit_price, quantity, 0.5) AS weighted_median
    FROM my_namespace.sales_data
    WHERE unit_price IS NOT NULL AND quantity IS NOT NULL

### approx_median

Returns the approximate median. Equivalent to `approx_percentile_cont(column, 0.5)`.
    
    
    SELECT approx_median(total_amount) AS median_amount
    FROM my_namespace.sales_data
    
    SELECT department, approx_median(total_amount) AS median
    FROM my_namespace.sales_data
    GROUP BY department

### approx_distinct

Returns the approximate count of distinct values using HyperLogLog.
    
    
    SELECT approx_distinct(customer_id) AS unique_customers
    FROM my_namespace.sales_data
    
    SELECT department, approx_distinct(customer_id) AS unique_customers
    FROM my_namespace.sales_data
    GROUP BY department

### approx_top_k

Returns the _k_ most frequent values with their approximate counts.
    
    
    SELECT approx_top_k(department, 5) AS top_departments
    FROM my_namespace.sales_data

* * *

## Statistical aggregates

### var / var_samp

Returns the sample variance.
    
    
    SELECT var(total_amount) AS variance
    FROM my_namespace.sales_data
    
    SELECT department, var(total_amount) AS variance
    FROM my_namespace.sales_data
    GROUP BY department

### var_pop

Returns the population variance.
    
    
    SELECT var_pop(total_amount) AS pop_variance
    FROM my_namespace.sales_data

### stddev / stddev_samp

Returns the sample standard deviation.
    
    
    SELECT stddev(total_amount) AS std_dev
    FROM my_namespace.sales_data
    
    SELECT department, stddev(total_amount) AS std_dev
    FROM my_namespace.sales_data
    GROUP BY department

### stddev_pop

Returns the population standard deviation.
    
    
    SELECT stddev_pop(total_amount) AS pop_std_dev
    FROM my_namespace.sales_data

### covar_samp

Returns the sample covariance. Alias: `covar`.
    
    
    SELECT covar_samp(total_amount, CAST(quantity AS DOUBLE)) AS covariance
    FROM my_namespace.sales_data
    WHERE total_amount IS NOT NULL AND quantity IS NOT NULL

### covar_pop

Returns the population covariance.
    
    
    SELECT covar_pop(total_amount, CAST(quantity AS DOUBLE)) AS pop_covariance
    FROM my_namespace.sales_data
    WHERE total_amount IS NOT NULL AND quantity IS NOT NULL

### corr

Returns the Pearson correlation coefficient between two columns.
    
    
    SELECT corr(total_amount, CAST(quantity AS DOUBLE)) AS correlation
    FROM my_namespace.sales_data
    WHERE total_amount IS NOT NULL AND quantity IS NOT NULL

### regr_slope

Returns the slope of the linear regression line.
    
    
    SELECT regr_slope(total_amount, CAST(quantity AS DOUBLE)) AS slope
    FROM my_namespace.sales_data
    WHERE total_amount IS NOT NULL AND quantity IS NOT NULL

### regr_intercept

Returns the y-intercept of the linear regression line.
    
    
    SELECT regr_intercept(total_amount, CAST(quantity AS DOUBLE)) AS intercept
    FROM my_namespace.sales_data
    WHERE total_amount IS NOT NULL AND quantity IS NOT NULL

### regr_count

Returns the count of non-NULL pairs.
    
    
    SELECT regr_count(total_amount, CAST(quantity AS DOUBLE)) AS pair_count
    FROM my_namespace.sales_data
    WHERE total_amount IS NOT NULL AND quantity IS NOT NULL

### regr_r2

Returns the coefficient of determination (R-squared).
    
    
    SELECT regr_r2(total_amount, CAST(quantity AS DOUBLE)) AS r_squared
    FROM my_namespace.sales_data
    WHERE total_amount IS NOT NULL AND quantity IS NOT NULL

### regr_avgx

Returns the average of the independent variable (x) for non-NULL pairs.
    
    
    SELECT regr_avgx(total_amount, CAST(quantity AS DOUBLE)) AS avg_qty
    FROM my_namespace.sales_data
    WHERE total_amount IS NOT NULL AND quantity IS NOT NULL

### regr_avgy

Returns the average of the dependent variable (y) for non-NULL pairs.
    
    
    SELECT regr_avgy(total_amount, CAST(quantity AS DOUBLE)) AS avg_amount
    FROM my_namespace.sales_data
    WHERE total_amount IS NOT NULL AND quantity IS NOT NULL

### regr_sxx

Returns the sum of squares of the independent variable.
    
    
    SELECT regr_sxx(total_amount, CAST(quantity AS DOUBLE)) AS sxx
    FROM my_namespace.sales_data
    WHERE total_amount IS NOT NULL AND quantity IS NOT NULL

### regr_syy

Returns the sum of squares of the dependent variable.
    
    
    SELECT regr_syy(total_amount, CAST(quantity AS DOUBLE)) AS syy
    FROM my_namespace.sales_data
    WHERE total_amount IS NOT NULL AND quantity IS NOT NULL

### regr_sxy

Returns the sum of products of the paired variables.
    
    
    SELECT regr_sxy(total_amount, CAST(quantity AS DOUBLE)) AS sxy
    FROM my_namespace.sales_data
    WHERE total_amount IS NOT NULL AND quantity IS NOT NULL

* * *

## Bitwise aggregates

### bit_and

Returns the bitwise AND of all values in a group.
    
    
    SELECT department, bit_and(quantity) AS and_result
    FROM my_namespace.sales_data
    WHERE quantity IS NOT NULL
    GROUP BY department

### bit_or

Returns the bitwise OR of all values in a group.
    
    
    SELECT department, bit_or(quantity) AS or_result
    FROM my_namespace.sales_data
    WHERE quantity IS NOT NULL
    GROUP BY department

### bit_xor

Returns the bitwise XOR of all values in a group.
    
    
    SELECT department, bit_xor(quantity) AS xor_result
    FROM my_namespace.sales_data
    WHERE quantity IS NOT NULL
    GROUP BY department

* * *

## Boolean aggregates

### bool_and

Returns true if all values in a group are true.
    
    
    SELECT department, bool_and(is_completed) AS all_completed
    FROM my_namespace.sales_data
    WHERE is_completed IS NOT NULL
    GROUP BY department

### bool_or

Returns true if any value in a group is true.
    
    
    SELECT department, bool_or(is_completed) AS any_completed
    FROM my_namespace.sales_data
    WHERE is_completed IS NOT NULL
    GROUP BY department

* * *

## Positional aggregates

### first_value

Returns the first value in a group according to the specified ordering.
    
    
    SELECT department,
           first_value(customer_id ORDER BY total_amount ASC) AS lowest_spender
    FROM my_namespace.sales_data
    WHERE total_amount IS NOT NULL
    GROUP BY department

### last_value

Returns the last value in a group according to the specified ordering.
    
    
    SELECT department,
           last_value(customer_id ORDER BY total_amount ASC) AS highest_spender
    FROM my_namespace.sales_data
    WHERE total_amount IS NOT NULL
    GROUP BY department

* * *

## Collection aggregates

These aggregates accumulate all input values into a single result. Because they hold every value in memory, use a `WHERE` filter or `GROUP BY` to keep group sizes bounded on large datasets.

### array_agg

Collects values from a group into an array.
    
    
    SELECT department, array_agg(customer_id) AS customers
    FROM my_namespace.sales_data
    GROUP BY department

### string_agg

Concatenates values from a group into a single string, separated by the given delimiter.
    
    
    SELECT department, string_agg(customer_id, ', ') AS customer_list
    FROM my_namespace.sales_data
    GROUP BY department

[PreviousScalar functions](https://developers.cloudflare.com/basin-sql/sql-reference/scalar-functions/)[NextComplex types](https://developers.cloudflare.com/basin-sql/sql-reference/complex-types/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/basin-sql/sql-reference/aggregate-functions.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
