# Getting Time Series Core Financial Data

```{important} Apperate includes only historical time series Core Data at this time. We are in the process of migrating real-time legacy data, including stock quotes, into Apperate. In the meantime, please see the [Legacy API Reference](https://iexcloud.io/docs/api/) for the real-time legacy data.
```

Apperate's Core Datasets provide historical time series financial data. Here are steps for getting this financial data.

**Prerequisites:**

- **IEX Cloud Apperate account** - Create one [here](https://iexcloud.io/cloud-login#/register).
- **Apperate workspace** - See [Setting Up Your Workspace](../getting-started/getting-started-with-apperate.md#setting-up-your-workspace). 

## Steps

1. Browse the Core Datasets in the console at [**Data > Datasets > Core**](https://iexcloud.io/console/datasets/core). The Core Datasets list appears.

    ![](./getting-time-series-core-financial-data/core-datasets.png)

1. Click on a dataset you want data from. For example, if you want to get cash flow records, click the CASH_FLOW dataset. The dataset overview appears.

    ![](./getting-time-series-core-financial-data/cash-flow-overview.png)

    > **Note:** From a dataset's **Database** page, you can query its data, export the query results to a CSV, and share your query in a URL. 
    
1. Examine the the **Example Request** URL.

    ```
    https://WORKSPACE.iex.cloud/v1/data/CORE/CASH_FLOW?last=1&token=TOKEN
    ```

    Here's a breakdown of the URL.

    | URL Component | Description |
    | --- | --- |
    | `https://WORKSPACE.iex.cloud/v1` | Base URL consisting of the domain (your workspace is the subdomain) and the API version. |
    | `/data/CORE/CASH_FLOW` | The Data API's [`GET /data/` method](https://iexcloud.io/docs/datasets-api/query-data) followed by path parameter values `CORE` for the dataset namespace and `CASH_FLOW` for the dataset ID. |
    | `?last=1&token=TOKEN` | Method parameters `last=1` to return the last record and `token=TOKEN` to authorize access. Please see the [`GET /data/` method](https://iexcloud.io/docs/datasets-api/query-data) reference for additional parameters. See [Security and Access](../administration/access-and-security.md) to create public access tokens. |

1. Get the latest record by clicking the **Example Request** URL. Apperate opens the request in a new browser tab and the A JSON array appears in the response like this:

    ```javascript
    [
        {
            "capitalExpenditures": -153981933.26019996,
            "cashChange": 52921982765.789,
            "cashFlow": -7635540477.244902,
            "cashFlowFinancing": 804800407.0185003,
            "changesInInventories": 0,
            "changesInReceivables": 0,
            "currency": "USD",
            "depreciation": 300821632.50179994,
            "dividendsPaid": null,
            "exchangeRateEffect": null,
            "filingType": "6-K",
            "fiscalDate": "2022-07-31",
            "fiscalQuarter": 3,
            "fiscalYear": 2022,
            "investingActivityOther": null,
            "investments": null,
            "netBorrowings": -786885758368.2644,
            "netIncome": 1956976221.5984,
            "otherFinancingCashFlows": null,
            "reportDate": "2022-08-23",
            "symbol": "BNS",
            "totalInvestingCashFlows": 5990703186.795099,
            "id": "CASH_FLOW",
            "key": "BNS",
            "subkey": "quarterly",
            "date": 1659225600000,
            "updated": 1661439879000
        }
    ]
    ```

    ```{note} The response will be different for you because records are continuously being added.
    ```

1. Update the URL to get Apple's latest cash flow record by adding the `AAPL` symbol as the `key` path parameter after `CASH_FLOw`. Replace `WORKSPACE` and `TOKEN` with your values.

    ```
    https://WORKSPACE.iex.cloud/v1/data/CORE/CASH_FLOW/AAPL?last=1&token=TOKEN
    ```

    A JSON array appears in the response like this:

    ```javascript
    [
        {
            "capitalExpenditures": -2102000000,
            "cashChange": 48231000000,
            "cashFlow": 22892000000,
            "cashFlowFinancing": -27445000000,
            "changesInInventories": 5433000000,
            "changesInReceivables": 42242000000,
            "currency": "USD",
            "depreciation": 2805000000,
            "dividendsPaid": null,
            "exchangeRateEffect": null,
            "filingType": "10-Q",
            "fiscalDate": "2022-06-25",
            "fiscalQuarter": 3,
            "fiscalYear": 2022,
            "investingActivityOther": null,
            "investments": null,
            "netBorrowings": 55074000000,
            "netIncome": 19442000000,
            "otherFinancingCashFlows": null,
            "reportDate": "2022-07-29",
            "symbol": "AAPL",
            "totalInvestingCashFlows": 4234000000,
            "id": "CASH_FLOW",
            "key": "AAPL",
            "subkey": "quarterly",
            "date": 1656115200000,
            "updated": 1661439802000
        }
    ]
    ```

Congratulations on getting core financial time series data.

## What's Next

If you want to get real-time IEX Cloud financial data, see [Getting Real-Time Core Financial Data](./getting-real-time-core-financial-data.md).

Apperate's API is easy to use. For starters, visit [Using Apperate's APIs](../interacting-with-your-data/apperate-api-basics.md).

To dive into more Core Dataset queries using the Data API, see these articles:

- [Querying Datasets](../interacting-with-your-data/querying-data/querying-datasets.md)
- [SQL Query with the API](../interacting-with-your-data/querying-data/sql-query-with-the-api.md)

If want to combine Core Dataset data with data from other datasets, check out [Creating and Managing Views](../managing-your-data/creating-and-managing-views.md).

If you need to store application data, learn how at [Writing and Fetching a Data Record](../getting-started/writing-and-fetching-a-record.md).