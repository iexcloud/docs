# Production-Ready IEX Cloud Core Data

IEX Cloud Apperate comes with 5+ terabytes of built-in data to power fintech applications and more. Here are some of the data types:

- Stocks / Equities
- Forex / Currencies
- Options
- Futures
- Commodities
- Economic Data
- Rates
- News
- Symbols / Mappings

```{important} Apperate includes only historical time series Core Data at this time. We are in the process of migrating real-time legacy data, including stock quotes, into Apperate. In the meantime, please see the [Legacy API Reference](https://iexcloud.io/docs/api/) for the real-time legacy data.
```

Let's explore the Core Data.

## Exploring Core Data

All the data is available at REST API endpoints, and much of the data is available as [datasets](../reference/glossary.md#dataset) (requires Apperate plan) that you can also use in [views](../managing-your-data/creating-and-managing-views.md). Apperate lists these datasets (Core Data) at [**Data &rarr; Datasets &rarr; Core**](https://iexcloud.io/console/datasets/core).

![](./production-ready-core-data/core-datasets.png)

Like all Apperate datasets, you can access their records via REST endpoints and via the dataset SQL editor.

![](./production-ready-core-data/query-in-sql-editor.png)

The [Apperate API Reference](https://iexcloud.io/docs/) describes all the Core Data REST endpoints.

![](./production-ready-core-data/core-data-api-endpoints.png)

## What's Next

Now that you've been introduced to Core Data, here are some topics to consider next.

[Using Core Data](../using-core-data.md): These articles demonstrate querying real-time and time series data, and leveraging normalized financial symbols. 

[Migrating and Import Data](../migrating-and-importing-data.md): These articles demonstrate loading data from various data sources, including AWS S3 buckets, URLs, and files.

[Writing and Reading a Record](../getting-started/write-and-read-a-record.md): Shows you how to write individual data records to Apperate and read them back.

[Managing Your Data](../managing-your-data.md): This section provides guides that explain dataset schemas, creating views, and creating datasets via the Datasets API.

[Interacting With Your Data](../interacting-with-your-data.md): These articles introduce Apperate API basics, show how to query datasets, and demonstrate updating data.

```{note} IEX Cloud documentation for the legacy plan subscribers is at <https://iexcloud.io/docs/api/>.
```