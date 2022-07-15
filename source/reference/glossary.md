# Glossary

The new data infrastructure product uses the following terms, ordered alphabetically.

## API

Stands for Application Programming Interface. You can interact with software programmatically via its API.

## CSV

Stands for Comma Separated Value. It is a text format for specifying data using rows and columns. The first row’s values describe each column. Each subsequent row represents an instance of the data, including values (in some cases empty values) for each column.

## Data Source

A source from which data is ingested into IEX Cloud.

## Dataset

A modifiable data collection that is defined by a schema, stored in IEX Cloud, and delivered via permissioned, auto-generated APIs. 

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

## Secondary index

A property that serves as an identifier that's used in addition to the Primary index.

## Unique Index

A dataset's main key composed of  the Primary index, Secondary index (optional), and Date index. 

## Workspace

Your unique domain for building and publishing datasets. The URL format and example below show workspace names and dataset names in bold.

URL Format: `https://workspace.iex.cloud/v1/data/WORKSPACE/DATASET`

Example: `https://my.iex.cloud/v1/data/MY/CARS`

---
[Go to Docs Home](https://github.com/iexcloud/docs/blob/main/README.md)