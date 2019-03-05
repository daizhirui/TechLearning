# Command List

- `.table`: show all tables

# SELECT statement

## Use ORDER BY clause to sort the result set
```sqlite
SELECT
    column_list
FROM
    table
ORDER_BY
    column_1 ASC,
    column_2 DESC;
```

`ASC` by default.
A row with a `NULL` value is higher than rows with regular values in ascending order.

## Use SELECT DISTINCT clause to remove duplicate rows in the result set
```sqlite
SELECT DISTINCT
    column_list
FROM
    table;
```

SQLite considers `NULL` values as duplicates.

## User WHERE caluse to specify the search condition for rows returned by the query
```sqlite
SELECT
    column_list
FROM
    table
WHERE
    search_condition;
```

The form of `search_condition`:

### `left_expression OPERATOR right_expression`

`COMPARISON_OPERATOR` can be `=, <> or !=, <, >, <=, >=`
`LOGICAL_OPERATOR` can be `ALL(all expressions are 1), AND, ANY, BETWEEN, EXISTS, IN, LIKE, NOT, OR`

Example:
```sqlite
WHERE column_1 = 100;
WHERE column_2 IN (1,2,3);
WHERE column_3 LIKE 'An%'
WHERE column_4 BETWEEN 10 AND 20;
```

