# SQL in Apperate

Apperate supports ANSI-compliant SQL. There are however some limitations.

## Limitations

- `SELECT *` is not supported for views.
- `WHERE` clauses and `ON` clauses must only operate on indexed properties (columns). See the Unique Index components [here](../managing-your-data/understanding-datasets.md#indexing-with-unique-index).