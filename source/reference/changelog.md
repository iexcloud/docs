# Changelog

Here are the notable changes.

## 2022-06-17

- Add a dataset export mechanism.

## 2022-06-16

- Make indexed schema properties required; allow all others to be null.

## 2022-06-15

- Go to the create dataset page immediately upon creating a workspace.
- Add an API to page through S3 bucket listings.
- Make `_system` a reserved name prefix.

## 2022-06-13

- Support using a regex in the [AWS ARN role](../migrating-and-importing-data/accessing-s3-via-storage-integration.md).
- Support deleting an [AWS integration](../migrating-and-importing-data/accessing-s3-via-storage-integration.md).

## 2022-06-09

- Map the symbology property to the primary index property.
- Add APIs to generate schemas from remote data sources.

## 2022-06-08

- Supprt selecting [data files](../migrating-and-importing-data/loading-data-from-a-file.md) that have any name suffix or no name suffix.

## 2022-06-03

- Support downloading a data ingestion's [invalid records](https://iexcloud.zendesk.com/hc/en-us/articles/6756010042643-Monitoring-Logs) as a CSV file.

## 2022-06-02

- Show job ID in the [log stream](https://iexcloud.zendesk.com/hc/en-us/articles/6756010042643-Monitoring-Logs).

## 2022-05-31

- Save console messages to the [log stream](https://iexcloud.zendesk.com/hc/en-us/articles/6756010042643-Monitoring-Logs).
- Add aliases as suggested words in the SQL editor.

## 2022-05-27

- Improve [API docs](https://iexcloud.io/docs/datasets-api) URLs by replacing spaces with hyphens.

## 2022-05-25

- Fix [Core dataset](https://iexcloud.io/docs/core) overviews.

## 2022-05-24

- Validate schemas during dataset generation.
- Fix insert row on the **DATASET > Database** page.

## 2022-05-19

- Support SQL views. See it in action at [Combining Data into Views](https://iexcloud.zendesk.com/hc/en-us/articles/6670289316115-Combining-Data-into-Views).
- Limit dataset query results to 1000.
- Display AWS user ARN for [AWS integration](../migrating-and-importing-data/accessing-s3-via-storage-integration.md).

## 2022-05-17

- Support `DISTINCT` in SQL queries.
- Support changing a dataset's metadata graph (symbology) property.

## 2022-05-16

- Support querying datasets that have hyphens in their names.

## 2022-05-12

- Generate JSON schema for SQL view datasets.

## 2022-05-11

- Support sampling JSON data with JSONPath and displaying in the UI. For details, go to [Accessing Data Nested in JSON](https://iexcloud.zendesk.com/hc/en-us/articles/6187037773971-Accessing-Data-Nested-in-JSON).

## 2022-05-10

- Improved [API docs](https://iexcloud.io/docs/) load time.

## 2022-05-09

- Make table lookup case-insensitive.
- Add SQL support for column aliases. Try it in your dataset **Databse** page's SQL editor.

## 2022-05-06

- Support `GROUP BY` in SQL queries.

## 2022-04-29

- Get new/modified dataset data by calling `GET /data/:workspace/:id/:key?/:subkey?` specifying a previous query ID using the `queryId` query parameter. See [Query data](https://iexcloud.io/docs/datasets-api/query-data).

## 2022-04-27

- Support synchronous ingestion using "wait" query parameter. You can ingest data synchronously when calling the `POST /data/:workspace/:id` endpoint by setting the `wait` query parameter to `true`. See [Ingest data](https://iexcloud.io/docs/datasets-api/ingest-data).

## 2022-04-25

- Add API endpoint to GET log messages. You can fetch your logs by executing the `GET /logs/:workspace`. endpoint. See [Get logs](https://iexcloud.io/docs/datasets-api/get-logs).

## 2022-04-20

- Improve logging for dataset jobs and console events. Learn more at [Monitoring Logs](https://iexcloud.zendesk.com/hc/en-us/articles/6756010042643-Monitoring-Logs).

## 2022-04-18

- Opt-in to map a property to our financial identifier metadata graph. See [Getting Started with an Example Dataset](../getting-started/getting-started-with-an-example-dataset.md).

## 2022-04-13

- Support scheduled ingestion. In the Console, see [Scheduling Data Ingestion](../migrating-and-importing-data/scheduling-data-ingestion.md).
