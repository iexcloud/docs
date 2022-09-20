# SQL Query with the API

Apperate is MySQL compliant and supports time series functions, vector functions, and more. You can execute SQL commands programatically via the [`GET /sql-query/:workspace`](https://iexcloud.io/docs/apperate-apis/data/sql-query-dataset-data) endpoint. 

## Executing a SQL Query

Here's an example of executing a SQL query using the API.

1. Construct your SQL command to execute on a dataset. For example,

    ```sql
    SELECT * FROM SAMPLE_AAPL_DATASET_AZWDTSJWS 
    WHERE (date >= "2021-10-01" AND date <= "2021-10-08")
    ORDER BY date ASC
    ```

    ``` {important} WHERE clauses must only operate on indexed properties (columns). See the Unique Index components [here](../../managing-your-data/understanding-datasets.md#indexing-with-unique-index).
    ```

1. Call the `/sql-query` endpoint, using your base URL, workspace name, and API token, and entering your SQL command as the `sqlQuery` query parameter value.

    Example format:

    ```
    BASE_URL/sql-query/WORKSPACE?sqlQuery=SQL_QUERY&token=TOKEN
    ```

    Example URL:

    ```
    https://my.iex.cloud/v1/sql-query/MY?SELECT * FROM SAMPLE_AAPL_DATASET_AZWDTSJWS WHERE (date >= "2021-10-01" AND date <= "2021-10-08") ORDER BY date ASC&token=TOKEN
    ```

    The browser encodes your command. For example,

    ```
    https://my.iex.cloud/v1/sql-query/MY?sqlQuery=SELECT%20*%20FROM%20SAMPLE_AAPL_DATASET_AZWDTSJWS%20\%20WHERE%20(date%20%3E=%20%222021-10-01%22%20AND%20date%20%3C=%20%222021-10-08%22)%20\%20ORDER%20BY%20date%20ASC&token=sk_TOKEN
    ```

    Results:

    ```javascript
    [
        {
            "close": 142.65,
            "date": "2021-10-01",
            "high": 142.92,
            "low": 139.1101,
            "open": 141.9,
            "symbol": "AAPL",
            "volume": 94639581
        },
        {
            "close": 139.14,
            "date": "2021-10-04",
            "high": 142.21,
            "low": 138.27,
            "open": 141.76,
            "symbol": "AAPL",
            "volume": 98322008
        },
        {
            "close": 141.11,
            "date": "2021-10-05",
            "high": 142.24,
            "low": 139.36,
            "open": 139.49,
            "symbol": "AAPL",
            "volume": 80861062
        },
        {
            "close": 142,
            "date": "2021-10-06",
            "high": 142.15,
            "low": 138.37,
            "open": 139.47,
            "symbol": "AAPL",
            "volume": 83221119
        },
        {
            "close": 143.29,
            "date": "2021-10-07",
            "high": 144.215,
            "low": 142.72,
            "open": 143.06,
            "symbol": "AAPL",
            "volume": 61732656
        },
        {
            "close": 142.9,
            "date": "2021-10-08",
            "high": 144.1781,
            "low": 142.56,
            "open": 144.03,
            "symbol": "AAPL",
            "volume": 58773155
        }
    ]
    ```

Now you know how to use the API to execute SQL commands on your Apperate datasets.

## Related Topics

[Querying Datasets](./querying-datasets.md)

[Using Apperate's APIs](../apperate-api-basics.md)

[Interact With Your Data](../../interacting-with-your-data.md)