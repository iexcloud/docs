# Getting Started with IEX Cloud Apperate

A great way to get familiar with Apperate is to create a dataset and write data to it. A [dataset](../reference/glossary.md#dataset) is like any common database table: it is defined by a schema and can hold data records. Datasets have several additional benefits in that although they can store any data model, they are optimized for time series data. Additionally, Apperate automatically generates an API for accessing the dataset (via a permissioned token, of course).

Here we'll create a dataset with example data in seconds and read the data back from the dataset's auto-generated REST endpoint.

**Prerequisites:**

- **IEX Cloud Apperate account** - Create one [here](https://iexcloud.io/cloud-login#/register).
- **Apperate workspace** - See [Creating a Workspace](../getting-started/creating-a-workspace.md). 

## Creating and Using an Example Dataset

Here you will load IEX Cloud's sample data file and then access the loaded data from an auto-generated REST endpoint.

1. If you're not already in the **Create a dataset** page, click **Create a dataset** at the top right of the console. The **Create a dataset** page appears. The image below highlights the sample file link that you will click in the next step.

    ![](./getting-started-with-apperate/try-our-sample-file.png)

    Optionally, enter a more meaninfgul the dataset ID.

1.  In the **Create a dataset** page, keep the source type set to **Local file** and load the sample data file by clicking **Try using our sample file**. Apperate loads the data into a new dataset, generates a REST endpoint for the dataset, and shows the dataset overview in the console.

    ![](./getting-started-with-apperate/sample-dataset-overview.png)

    Notice these fields:

    - **Example request** is a REST endpoint URL for getting the dataset's last row.
    - **Rows** shows the dataset's row count is 1,257.
    - **Detected symbol** is the data property designated as the primary index. Apperate makes a best effort to determine a primary index. 
    
    ``` {note} you can change the primary index and other parts of the dataset schema using the schema editor available by clicking **Edit schema**.
    ```

    The **HTTP request** panel shows the dataset's last row as a JSON object.

    ```json
    [
        {
            "close": 148.64,
            "date": "2021-10-25",
            "high": 149.37,
            "low": 147.6211,
            "open": 148.68,
            "symbol": "AAPL",
            "volume": 50720556
        }
    ]
    ```

1. Get your dataset's last row by clicking the **Example request** URL.

    ![](./getting-started-with-apperate/sample-dataset-example-request.png)

    The URL opens in a new browser tab and the response appears as a JSON object.

    ```json
    [{"close":148.64,"date":"2021-10-25","high":149.37,"low":147.6211,"open":148.68,"symbol":"AAPL","volume":50720556}]
    ```

You just loaded data into IEX Cloud Apperate and retrieved it using an auto-generated REST API! It's just that easy to make data available to your apps!!

## What's Next

After creating a dataset, you can edit its schema to meet your needs. For more information on working with dataset schemas, please see [Understanding Datasets](../managing-your-data/understanding-datasets.md).

Here you loaded data from a file but you can load data from other sources, including URLs and AWS S3 buckets. To learn more about using other sources and scheduling automated data ingestion, check out [Migrating and Importing Data](../migrating-and-importing-data.md).

Otherwise, learn how to write a record to a dataset as you would write from an application, and then fetch that record. [Write and Read a Record](./write-and-read-a-record.md) shows you how.