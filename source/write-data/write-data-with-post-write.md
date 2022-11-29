# Write Data with POST /write

Apperate's `POST /write` endpoint and `apperate.write()` JS function are fast ways to write one or a few records. By default, they return after storing the data and making it available for querying. Alternatively you can run them asynchronously. When run asynchronously, the call returns immediately to unblock you, Apperate saves the data and makes the data available for query as soon as possible. The async mode facilitates writing to the same dataset simultaneously. Whenever you're ready to write data, Apperate is ready to store it.

The [Write Data](https://iexcloud.io/docs/apperate-apis/data/write-data) reference doc describes the `POST /write` method and its parameters. 

``` {note} *POST /write* doesn't guarantee the ordering of records.
```

``` {note} *POST /write* doesn't write to any logs. If records fail validation, consider loading the records (instead of writing them) and viewing the validation logs--See the load options at [Loading Data](../migrating-and-importing-data.md).
```

Here we'll write data using the `POST /write` endpoint.

``` {seealso}
[Write and Read Data](../getting-started/write-and-read-data.md) demonstrates using the `apperate.write()` JS method.
```

## Write Data

1. Prepare a `POST /write/` method call. For example, use the following cURL command, replacing the `WORKSPACE`, `DATASET_ID`, and `SECRET_TOKEN` values with your own values and replacing the data (the single-quoted array following `-d`) with your own JavaScript object array.

    ```bash
    curl -X POST https://WORKSPACE.iex.cloud/v1/write/WORKSPACE/DATASET_ID?token=SECRET_TOKEN \
        -H 'Content-Type: application/json' \
        -d '[{"headline": "Are Hovercrafts the next big thing?", "content": "Here is what people are saying ...", "ticker": "GM", "source": "IEX Underground", "date": "2022-07-15"}]'
    ```

    ``` {note} On auto-generating a dataset, Apperate infers a dataset schema from your data; you can [update the schema](../managing-your-data/updating-a-dataset-schema.md) later.
    ```

1. Execute the command.

The method returns a response like the one below and writes the data to the dataset.

```javascript
{"success":true,"message":"wrote 1 messages"}
```

To see the data in the dataset go to the [Datasets](https://iexcloud.io/console/datasets/) page, click on your Workspace, and refresh the page. Then click on the target dataset's name. The dataset's **Database** page lists its values.

Congratulations! You wrote your data to a dataset using the `POST /write` endpoint.

## What's Next

[Write and Read Data](../getting-started/write-and-read-data.md) demonstrates using the `apperate.write()` JS method.

[Update a Dataset Schema](../managing-your-data/updating-a-dataset-schema.md) shows how to examine and modify your dataset schema.