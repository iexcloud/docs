# Update Data

You can update records using the UI, the Data API, or SQL. Here we'll demonstrate updating a record using the UI and the Data API. 

``` {note} Since index properties are immutable, you can't update any of a record's index property values. You can however delete such a record and add a new record with the index property value you want.
```

## Updating a Record in the UI

Here's how to update a record in the UI. 

1. Go to a SQL editor in either the **Datasets** page or in a dataset's **Database** tab. The SQL editor appears.

    ![](./updating-a-data-record/database-page.png)

1. Enter a [query](./querying-data.md) to return the data record you want to update. Then click **Run**. Apperate executes the statement and returns the matching data record.

    ![](./updating-a-data-record/select-a-car.png)

    ``` {important} WHERE clauses must only operate on indexed properties (columns). See the Unique Index components [here](../managing-your-data/understanding-datasets.md#indexing-with-unique-index).
    ```

1. Double click on the row that represents the record. The row editor appears.

    ![](./updating-a-data-record/edit-row-in-ui.png)

1. Make the field value modifications you want to any editable field. Then save your changes.

You've updated the data record. Editing records using the API is easy too.

## Updating a Record Using the API

The Data API [`POST /data/:workspace/:id`](https://iexcloud.io/docs/apperate-apis/data/ingest-data) endpoint's `overwrite=true` query parameter setting enables you to overwrite an existing record. 

``` {note} If you're just getting started with the API, check out the [API Basics](https://iexcloud.io/docs/api-basics) guide.
```

The `wait` query parameter is another one to consider. By default, the endpoint responds immediately after creating the ingestion job. If you prefer to wait for an ingestion job completion response, set `wait=true`.

``` {note} You can also check ingestion job status in the console's [Logs pages](../administration/monitoring-deployments.md) or via the [Logs API endpoint](https://iexcloud.io/docs/apperate-apis/logs/get-logs). 
```

Let's use the API to overwrite a record.

1. To specify your record update, you'll need to know its current values, including its Unique Index values (i.e., primary, secondary, and date indexes). You can fetch the record using the console's SQL editor or using the Data API's `GET /data/:workspace/:id/:key?/:subkey?` method as demonstrated in [Querying Datasets](./querying-data/querying-datasets.md).

    This JSON object for example, is a CARS dataset record:

    ```
    {"current_date":"2020-03-27","estimated_value":38650,"make":"Ford","mileage":8900,"model":"F-150","owner_count":1,"purchase_date":"2022-01-11","reg_state":23,"vin":"SD089VN7678997566","year":2022}
    ```

1. Use the [`POST /data/:workspace/:id`](https://iexcloud.io/docs/apperate-apis/data/ingest-data) endpoint and `overwrite=true` to write a new record in place of the current record. For example, to change the previous example record's `model` value to `F-250`, you could run a cURL command like this one, replacing `WORKSPACE`, `CARS`, and `SECRET_TOKEN` with your values:

    ```bash
    curl -H "Content-Type: application/json" \
    -X POST "https://cloud.iexapis.com/v1/data/WORKSPACE/CARS?overwrite=true&wait=true&token=SECRET_TOKEN" \
    -d '[{"current_date":"2020-03-27","estimated_value":38650,"make":"Ford","mileage":8900,"model":"F-250","owner_count":1,"purchase_date":"2022-01-11","vin":"SD089VN7678997566","year":2022}]'
    ```

    Since the command specifies `overwrite=true`, the record is overwritten with the new values.

    ![](./updating-a-data-record/cars-record-udpated.png)

    Since the command specifies `wait=true`, the response describes the final ingestion status. The response looks like this:

    ```javascript
    [
        {
            "close": 47.8925,
            "date": "2017-11-28",
            "high": 28.1163,
            "low": 27.8475,
            "open": 27.8575,
            "symbol": "AAPL",
            "volume": 108775932
        }
    ]
    ```

If you specify `wait=false` (the default), a response like the one below returns immediately, signaling data upload completion and ingestion commencement.

```javascript
{
    "success": true,
    "message": "Data upload of 198B for CARS completed, jobId: d5d126b0f8c94a7b8737cb64abed11ae has been created",
    "jobId": "d5d126b0f8c94a7b8737cb64abed11ae",
    "jobUrl": "/v1/jobs/MY/ingest/d5d126b0f8c94a7b8737cb64abed11ae"
}
```

You're updating data like a champ!

## What's Next

[Delete Data](https://iexcloud.io/docs/apperate-apis/data/delete-data): This reference page describes the `DELETE /data/:workspace/:id/:key/:subkey?/:date?` endpoint for deleting data.

[Querying Data](./querying-data.md): Describes the various ways to query (get) data.

[Create and Manage Views](../managing-your-data/creating-and-managing-views.md): Demonstrates joining datasets to create views.