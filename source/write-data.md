# Write Data

```{toctree}
:maxdepth: 1

write-data/write-data-with-post-write.md
write-data/write-data-with-the-apperate-write-js-method.md
```

Apperate provides simple, fast ways to store varying amounts of data. We group them into two camps:

**Writing data:** Writing small amounts of data (one record or a few) in real-time.

**Loading data:** Importing variable amounts of data from a data source such as a file, URL, S3 bucket. Apperate's console and APIs support scheduling, monitoring, and detailed logging for data imports.

What's more is both ways have options for creating a dataset schema for you automatically, if you don't already one.

The following articles get you started with storing data to Apperate.

## Writing Data

[Write Data with POST /write](./write-data/write-data-with-post-write.md) demonstrates writing data records in a fast, light-weight manner. Its asynchronous option supports making multiple write calls simultaneously, writing records in parallel. By default it behaves synchronously, returning a response after the data is available to query.

## Loading Data

Apperate's data loading features are great for batch-writing data from various sources. Here are the data loading articles:

- [Load Data From a File](./migrating-and-importing-data/loading-data-from-a-file.md)
- [Load Data From AWS S3](./migrating-and-importing-data/loading-data-from-aws-s3.md)
- [Load Data From a URL](./migrating-and-importing-data/loading-data-from-a-url.md)
- [Load Data via the API](./managing-your-data/creating-a-dataset-with-the-api.md#adding-data-to-your-dataset)

Enjoy writing and loading data into Apperate to support your applications!