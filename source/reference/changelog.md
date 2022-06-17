# Changelog

Here are the notable changes.

## 2022-05-06

- Support `GROUP BY` in SQL queries.

## 2022-04-29

- Get new/modified dataset data by calling `GET /data/:workspace/:id/:key?/:subkey?` specifying a previous query ID using the `queryId` query parameter. See [Query data](https://iexcloud.io/docs/datasets-api/query-data).

## 2022-04-27

- Support synchronous ingestion using "wait" query parameter. You can ingest data synchronously when calling the `POST /data/:workspace/:id` endpoint by setting the `wait` query parameter to `true`. See [Ingest data](https://iexcloud.io/docs/datasets-api/ingest-data).

## 2022-04-25

- Add API endpoint to GET log messages. You can fetch your logs by executing the `GET /logs/:workspace`. endpoint. See [Get logs](https://iexcloud.io/docs/datasets-api/get-logs).

## 2022-04-20

- Improved logging for dataset jobs and console events. Learn more at [Monitoring Logs](https://iexcloud.zendesk.com/hc/en-us/articles/6756010042643-Monitoring-Logs).

## 2022-04-18

- Opt-in to map a property to our financial identifier metadata graph. See [Getting Started with an Example Dataset](../getting-started/getting-started-with-an-example-dataset.md).

## 2022-04-13

- Support scheduled ingestion. In the Console, see [Scheduling Data Ingestion](../migrating-and-importing-data/scheduling-data-ingestion.md).
