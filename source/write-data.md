# Write Data

```{toctree}
:maxdepth: 1

write-data/write-data-with-the-apperate-write-js-method.md
write-data/write-data-with-post-write.md
```

Apperate provides simple, fast ways to store varying amounts of data. We group them into two camps:

**Writing data:** Writing small amounts of data (one record or a few) in real-time.

**Loading data:** Importing variable amounts of data from a data source such as a file, URL, S3 bucket. Apperate's console and APIs support scheduling, monitoring, and detailed logging for data imports.

What's more is both ways have options for creating a dataset schema for you automatically, if you don't already one.

The following articles get you started with storing data to Apperate.

## Writing Data

[Write Data with the apperate.write() JS Method](./write-data/write-data-with-the-apperate-write-js-method.md) and [Write Data Records with POST /record](./write-data/write-data-with-post-write.md) demonstrate writing data records in a fast, light-weight manner. Their asynchronous option supports making multiple write calls simultaneously, writing records in parallel. By default these real-time writes are synchronous, returning a response *after* the data is available to query.

## Loading Data

Apperate's data loading features are great for batch-writing data from various sources. Here are the data loading articles:

- [Load Data From a File](./load-data/loading-data-from-a-file.md)
- [Load Data From AWS S3](./load-data/loading-data-from-aws-s3.md)
- [Load Data From a URL](./load-data/loading-data-from-a-url.md)
- [Load Data via the API](./managing-your-data/creating-a-dataset-with-the-api.md#adding-data-to-your-dataset)

Enjoy writing and loading data into Apperate to support your applications!