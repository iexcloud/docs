# Using IEX Cloud Core Financial Data

```{toctree}
:maxdepth: 1

using-core-data/getting-real-time-core-financial-data.md
using-core-data/getting-time-series-core-financial-data.md
```

IEX Cloud comes with 5+ terabytes of built-in financial data to power fintech applications. It includes real-time financial data and historical time series financial data. Both data types are described here.

##  Real-Time Financial Data

```{important} IEX Cloud's financial data API reference is currently split between the current [API Reference](https://iexcloud.io/docs/) and the [Legacy API Reference](https://iexcloud.io/docs/api/). Until we finish refactoring legacy real-time endpoints, including stock quotes, into Apperate, please see the [Legacy API Reference](https://iexcloud.io/docs/api/) for the IEX Cloud core real-time data.
```

The [Legacy API Reference](https://iexcloud.io/docs/api/) describes everything you need to get IEX Cloud real-time financial data.

![](./using-core-data/iexcloud-api-reference.png)

Here's an overview:

- [Introduction](https://iexcloud.io/docs/api/#introduction) - Covers API basics including authentication, limits, support, how credits work (for legacy plans) and more.
- [Guides](https://iexcloud.io/docs/api/#guides) - Shows how to call REST endpoints and use endpoint data in Microsoft Excel.
- [Developer Tools and Open Source](https://iexcloud.io/docs/api/#developer-tools-and-open-source) - Describes JavaScript and Python SDK libraries and a sandbox for testing API calls.
- [API Usage](https://iexcloud.io/docs/api/#api-usage) - Demonstrates using query parameters, making batch requests, streaming data, and more.
- [Rules Engine](https://iexcloud.io/docs/api/#rules-engine-beta) - Details configuring event-based notifications.
- [Account](https://iexcloud.io/docs/api/#account) - Provides service management information. 
- [API System Metadata](https://iexcloud.io/docs/api/#api-system-metadata) - Links to a live status dashboard and describes the status API.
- [Changelog](https://iexcloud.io/docs/api/#changelog) - Lists notable IEX Cloud data and software changes.
- [Core Data](https://iexcloud.io/docs/api/#core-data) - Describes REST API endpoints for all kinds of financial data, including these:

    - [Stocks / Equities](https://iexcloud.io/docs/api/#stocks-equities)
    - [News](https://iexcloud.io/docs/api/#news)
    - [Cryptocurrency](https://iexcloud.io/docs/api/#cryptocurrency)
    - [Forex / Currencies](https://iexcloud.io/docs/api/#forex-currencies)
    - [Options](https://iexcloud.io/docs/api/#options)
    - [Futures](https://iexcloud.io/docs/api/#futures)
    - [Treasuries](https://iexcloud.io/docs/api/#treasuries)
    - [Commodities](https://iexcloud.io/docs/api/#commodities)
    - [Economic Data](https://iexcloud.io/docs/api/#economic-data)
    - [Rates](https://iexcloud.io/docs/api/#rates)
    - [Mortgage](https://iexcloud.io/docs/api/#mortgage)
    - [Reference Data](https://iexcloud.io/docs/api/#reference-data)
    - [Investors Exchange Data](https://iexcloud.io/docs/api/#investors-exchange-data)

Each endpoint reference includes the HTTP request structure, data weighting (for legacy plans), data timing and schedule, data sources, examples, path/query parameters, and response attributes.

To start calling these endpoints, see [Getting Real-Time Core Financial Data](./using-core-data/getting-real-time-core-financial-data.md).

## Time Series Financial Data

Apperate's built-in historical time series data is available as [datasets](./reference/glossary.md#dataset) (a.k.a. Core Datasets) that you can query and join with other datasets to create views.
The datasets are available in the console at [**Data > Datasets > Core**](https://iexcloud.io/console/datasets/core).

![](./using-core-data/core-datasets.png)

Each dataset **Overview** page provides an example request URL that you can click to get the dataset's last record.

```{note} A dataset's **Database** page (the tab is next to **Overview**) provides an interface for modifying data records and a SQL editor for querying the dataset or combine it with other datasets to create views.
```

The Overview page's **Open Docs** button opens the dataset's `GET /data` endpoint reference page. 

![](./using-core-data/cash_flow_dataset_api_docs.png)

Now you're familiar with the API references for the [core real-time financial data](https://iexcloud.io/docs/api/) and the [core historical time-series financial data](https://iexcloud.io/docs).

## What's Next

To get real-time IEX Cloud financial data, see [Getting Real-Time Core Financial Data](./using-core-data/getting-real-time-core-financial-data.md).

To get IEX Cloud historical time series IEX Cloud financial data, check out [Getting Time Series Core Financial Data](./using-core-data/getting-time-series-core-financial-data.md).

Interested in storing your application data in Apperate? Learn how at [Writing and Fetching a Data Record](../getting-started/writing-and-fetching-a-record.md).