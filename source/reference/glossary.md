# Glossary

The new data infrastructure product uses the following terms, ordered alphabetically.

## API

Stands for Application Programming Interface. You can interact with software programmatically via its API. IEX Cloud provides API reference documentation and API tutorials. The tutorials are here in the docs site.

IEX Cloud API reference sites:

- [Apperate API Reference](https://iexcloud.io/docs/)
- [IEX Cloud<sup>LEGACY</sup> API Reference](https://iexcloud.io/docs/api/)

## CSV

Stands for Comma Separated Value. It is a text format for specifying data using rows and columns. The first row’s values describe each column. Each subsequent row represents an instance of the data, including values (in some cases empty values) for each column.

``` {seealso} [Load Data from a File](../load-data/loading-data-from-a-file.md) demonstrates importing data from a CSV file.
```

## Data Source

A source from which data is ingested into Apperate.

The following tutorials demonstrate using data sources:

- [Load More Data into a Dataset](../load-data/load-more-data-into-a-dataset.md)
- [Schedule Data Ingestion](../load-data/scheduling-data-ingestion.md)

## Data Timing

The typical frequency of new data being produced for an entity (e.g., stock price, company dividends, etc.). A Core Dataset endpoint doc's **Data Timing** section describes the new data frequency for the respective entity. For examples, see the **Data Timing** section of any dataset endpoint listed in [IEX Cloud Core Datasets](https://iexcloud.io/docs/core) navigation in the API reference.

## Dataset

A modifiable data collection (or table) that is defined by a schema, stored in IEX Cloud Apperate, and delivered via permissioned, auto-generated APIs.

See these articles to understand datasets and learn how to use them:

- [Getting Started with Apperate](../getting-started/getting-started-with-apperate.md)
- [Understanding Datasets](../managing-your-data/understanding-datasets.md)
- [Querying Data](../search-data.md)
- [Managing Your Data](../managing-your-data.md)

## Date Index

Designates the time series index portion of a dataset's Unique Index. 

``` {seealso} [Understanding Datasets](../managing-your-data/understanding-datasets.md#indexing-with-unique-index)
```

## Ingest (Ingest data)

To load data into a dataset. 

``` {seealso} [Load More Data into a Dataset](../load-data/load-more-data-into-a-dataset.md).
```

## Ingestion Schedule

A timetable, set by the user, to automatically ingest data from a given data source into IEX Cloud.

``` {seealso} [Schedule Data Ingestion](../load-data/scheduling-data-ingestion.md)
```

## Job (Data Job)

A data-processing instance.  There are jobs for ingesting, modifying, and deleting data.

``` {seealso} [Monitoring Deployments](../administration/monitoring-deployments.md).
```

## JSON

Stands for JavaScript Object Notation. It is a text format for specifying objects. 

## Primary index

A property that serves as a record’s main identifier.

``` {seealso} [Understanding Datasets](../managing-your-data/understanding-datasets.md#indexing-with-unique-index)
```

<!-- ## Property (Schema Property) - TODO -->

## Publishable Token (Publishable Key)

All [tokens](#token-api-token), including *publishable tokens*, allow you to execute requests and access specific console pages and specific Apperate API reference pages. Publishable tokens can have Core dataset read access and have read, write, and / or delete permissions for any private datasets. Subscribers can create and share *publishable tokens* to grant access to specific datasets; tokens have Core dataset read access by default.

``` {seealso} [Token](#token-api-token) and [Access and Security](../administration/access-and-security.md).
```

<!-- ## Schema (Dataset Schema) - TODO -->

## Secondary index

A property that serves as an identifier that's used in addition to the Primary index.

``` {seealso} [Understanding Datasets](../managing-your-data/understanding-datasets.md#indexing-with-unique-index)
```

## Secret Token (Secret Key)

Apperate plan subscribers have a *secret token* (aka secret key). A secret token (aka secret key) allows you perform any action on your data or account. **NEVER share your secret token publicly**. Subscribers can create and share *publishable tokens* to grant access to specific data endpoints.

``` {seealso} [Token](#token-api-token) and [Access and Security](../administration/access-and-security.md).
```

## SmartLink

A mapping of a dataset property to Apperate's financial metadata graph. This mapping associates the property's values with equivalent values that use any of Apperate's supported [financial identifiers](./financial-identifiers.md).

A dataset's SmartLinks enable you to query on or join other datasets on the associated property using any equivalent financial identifier type values. 

``` {seealso}
See [Normalized Financial Symbols](../using-core-data/using-normalized-financial-data.md) for examples of querying on and joining datasets on SmartLinked properties.
```

## Storage Amount (Plan Storage Amount)

The amount of data a [pricing plan](https://iexcloud.io/pricing/) includes. 

Storage credit usage is based on your plan's Storage Amount and is calculated and reported hourly as the `STORAGE_ON_DISK` endpoint's **Credits Used** (see the **Credit Use by Endpoint** section at [Credits &rarr; Credit Use &rarr; Core Use](https://iexcloud.io/console/usage)).

``` {important} You cannot exceed your plan's Storage Amount. Apperate blocks any attempt to exceed the Storage Amount. You must upgrade your plan (see **Account** &rarr; [**Manage Plan**](https://iexcloud.io/console/manage-plan)) to store more data.
```

## Token (API Token)

An token (aka API token) allows you to execute requests and access specific console pages and Apperate API reference pages. Tokens have read, write, and/or delete permissions for one or more API endpoints.

Apperate plan subscribers have a *secret token* (aka secret key). This secret token allows you perform any action on your data or account. **NEVER share your secret token publicly**. Subscribers can create and share *publishable tokens* to grant access to specific data endpoints.

``` {seealso} [Access and Security](../administration/access-and-security.md)
```

<!-- ## Transform - TODO -->

## Unique Index

A dataset's main key composed of the Primary index, Secondary index (optional), and Date index.

``` {seealso} [Understanding Datasets](../managing-your-data/understanding-datasets.md#indexing-with-unique-index)
```

## Update Schedules

The regular times Apperate publishes new data to a Core Dataset.  A Core Dataset endpoint doc's **Update Schedule** section describes the publishing times. For examples, see the **Update Schedule** section of any endpoint listed in [IEX Cloud Core Datasets](https://iexcloud.io/docs/core) navigation in the API reference.

## View

A virtual [dataset](#dataset) created from a SQL query that joins multiple datasets.

``` {seealso} [Create a View](../managing-your-data/create-a-view.md).
```

## Workspace

Your unique domain for building and publishing datasets. The URL format and example below show workspace names and dataset names in bold.

URL Format: `https://workspace.iex.cloud/v1/data/WORKSPACE/DATASET`

Example: `https://my.iex.cloud/v1/data/MY/CARS`

``` {seealso} [Create a Workspace](../getting-started/getting-started-with-apperate.md#create-a-workspace).
```