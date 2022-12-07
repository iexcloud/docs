# Load Data

```{toctree}
:maxdepth: 1

load-data/loading-data-from-aws-s3.md
load-data/loading-data-from-a-url.md
load-data/loading-data-from-a-file.md
load-data/load-more-data-into-a-dataset.md
load-data/scheduling-data-ingestion.md
load-data/accessing-nested-json-data.md
load-data/accessing-s3-via-storage-integration.md
load-data/accessing-s3-via-your-access-key.md
```

## Uploading Your Data

Here you can learn how to load data from the following sources:

- [AWS S3 bucket](./load-data/loading-data-from-aws-s3.md)
- [URL](./load-data/loading-data-from-a-url.md)
- [File](./load-data/loading-data-from-a-file.md)

``` {important} **In fact, you can create a dataset instantaneously by dropping a CSV or JSON file onto the console.** On the spot, Apperate infers the schema and indexes automatically and creates the dataset.
```

![](./load-data/dataset-source-types.png)

## Scheduling Data Ingestion

When you're ready to import data regularly per a schedule, see [Schedule Data Ingestion](./load-data/scheduling-data-ingestion.md). 

![](./load-data/ingestion-schedules.png)

You'll have data flowing like clockwork!

## Supporting Articles

If you're parsing JSON response objects for the data you need or configuring access to AWS S3 buckets, check out these articles:

- [Access Nested JSON Data](./load-data/accessing-nested-json-data.md)
- [Access S3 via AWS Integration](./load-data/accessing-s3-via-storage-integration.md)
- [Access S3 via Your Access Key](./load-data/accessing-s3-via-your-access-key.md)