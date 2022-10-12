# Glossary

The new data infrastructure product uses the following terms, ordered alphabetically.

## API

Stands for Application Programming Interface. You can interact with software programmatically via its API.

## CSV

Stands for Comma Separated Value. It is a text format for specifying data using rows and columns. The first row’s values describe each column. Each subsequent row represents an instance of the data, including values (in some cases empty values) for each column.

## Data Source

A source from which data is ingested into IEX Cloud.

## Dataset

A modifiable data collection (or table) that is defined by a schema, stored in IEX Cloud Apperate, and delivered via permissioned, auto-generated APIs. 

## Date Index

Designates the time series index portion of a dataset's Unique Index. 

## Ingest (Ingest data)

To load data into a dataset. 

## Ingestion Schedule

A timetable, set by the user, to automatically ingest data from a given data source into IEX Cloud.

## Job (Data Job)

A data-processing instance.  There are jobs for ingesting, modifying, and deleting data.

## JSON

Stands for JavaScript Object Notation. It is a text format for specifying objects. 

## Primary index

A property that serves as a record’s main identifier.

<!-- ## Property (Schema Property) - TODO -->

<!-- ## Publishable Key - TODO -->

<!-- ## Schema (Dataset Schema) - TODO -->

## Secondary index

A property that serves as an identifier that's used in addition to the Primary index.

<!-- ## Secret Key - TODO -->

## SmartLink

A mapping of a dataset property to Apperate's financial metadata graph. This mapping associates the property's values with equivalent values that use any of Apperate's 10+ supported [financial identifiers](./financial-identifiers.md).

A dataset's SmartLinks enable you to query on or join other datasets on the associated property using any equivalent financial identifier type values. 

``` {seealso}
See [Normalized Financial Symbols](../using-core-data/using-normalized-financial-data.md) for examples of querying on and joining datasets on SmartLinked properties.
```

<!-- ## Token (API Token) - TODO -->

<!-- ## Transform - TODO -->

## Unique Index

A dataset's main key composed of  the Primary index, Secondary index (optional), and Date index. 

## Workspace

Your unique domain for building and publishing datasets. The URL format and example below show workspace names and dataset names in bold.

URL Format: `https://workspace.iex.cloud/v1/data/WORKSPACE/DATASET`

Example: `https://my.iex.cloud/v1/data/MY/CARS`