# SQL in Apperate

Apperate supports ANSI-compliant SQL. There are however some limitations.

## Limitations

- `SELECT *` is not supported for views.
- SQL `JOIN` with real-time datasets, such as CORE.QUOTE, is not supported.
- `WHERE` clauses and `ON` clauses must only operate on indexed properties (columns). See the Unique Index components [here](./understanding-datasets.md#indexing-with-unique-index).