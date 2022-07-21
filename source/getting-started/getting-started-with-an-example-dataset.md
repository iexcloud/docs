# Getting Started with an Example Dataset

> **Note:** IEX Cloud Apperate is available exclusively to select Early Access Program participants If you would like to participate in the Early Access Program or Beta, please email us at `product@iexcloud.io`.

We're excited to show you how to use datasets to make data accessible to apps in minutes. Here you load sample data into a dataset, define its schema, and read the data immediately from an auto-generated API.

## Example: Delivering Data

Start using datasets, following these steps:

1.  Go to the IEX Cloud Console at <https://iexcloud.io/console>. The
    new product home page appears.

    ![](./getting-started-with-an-example-dataset/welcome-to-your-workspace.png)
    
2.  In the console, click **Create a dataset**. The dataset
    creation page appears with options for choosing a data source. In
    the bottom right, there is a button labeled **Use IEX Cloud's sample file**.

    ![](./getting-started-with-an-example-dataset/use-sample-file.png)

3.  Load the sample data file by clicking **Use IEX Cloud's sample file** in the bottom right. The file uploads and the **Edit schema** interface appears.

    ![](./getting-started-with-an-example-dataset//sample-aapl-dataset-edit-schema.png)

    **Dataset ID** - Name your dataset by giving it a unique ID. On data ingestion, the product makes a best effort to name your dataset, using the data source name (e.g., file name). If a dataset exists with that name, the product suggests a suffix to make the dataset ID unique. 

    > **Important:** The `_system` prefix (case-insensitive) is reserved for Apperate system tables and columns. You are forbidden to prefix your dataset ID or dataset property names with `_system`.

    **Properties (table)** The product makes a best effort to
    derive data property names using the column names the dataset provides and
    to derive data types from the data values. Lastly, the product attempted
    to determine a Unique Index
    composed of a primary index key, secondary index key (optional), and date index key.

    In this case, the product correctly set *symbol* as the primary index key and *date* as the date index key. The property types were detected correctly too. We could set a secondary index key too, but we will decline.

    There are more options and content below the *Properties* table.

    ![edit-schema-bottom-sections.png](./getting-started-with-an-example-dataset/edit-schema-bottom-sections.png)

    **Sample API Call** - Shows a URL for getting data from the dataset using the current Unique Index.

    **Unique Index Example** - Illustrates the current Unique Index, composed of the Primary index, Secondary index (optional), and Date index.

    **Opt in to IEX Cloud's Metadata Graph** - Provides the opportunity to map a property to IEX Cloud's metadata data graph of [financial identifiers](../managing-your-data/creating-and-managing-views/joining-on-core-data.md). This allows you to enrich your dataset by joining it to IEX Cloud core equities data or any other dataset that is also opted in. Furthermore, you can ingest data into and query for data in this dataset using IEX Cloud's supported financial identifiers.

    > **See Also:** You can learn more about dataset schemas by reading [Understanding Datasets](../managing-your-data/understanding-datasets.md).

    IEX Cloud correctly identified the *symbol* property as containing financial identifiers and therefore opted the dataset in to IEX Cloud's metadata graph.
    
    Since this schema defines our dataset the way we want, click **Create Dataset Now**. The product builds and stores your dataset and your dataset overview appears.

    ![](./getting-started-with-an-example-dataset/sample-appl-dataset-overview.png)

    **Milestone alert!** In just **four clicks**, you
    loaded data, defined the data's types and its unique time series compatible
    index, and generated its auto-documented API! Let's get some data, next.

4.  In your dataset overview, get your dataset's last record by clicking the **Example Request** URL. The URL opens in a new browser tab and the dataset data response (in JSON) appears.

    ![](./getting-started-with-an-example-dataset/sample-appl-execute-query.png)

In only a few minutes, you loaded data into the IEX Cloud Apperate and retrieved it using an auto-generated RESTful API! It's just that easy to get data to your app!!

**Bonus step - visit your API docs** by clicking **Open API Docs**
in your dataset's overview page. Your API docs open in a new tab.

![](./getting-started-with-an-example-dataset/sample-appl-dataset-api-docs.png)

Your auto-documented dataset is ready for consumption.

Congratulations on making data available using a dataset!

## What's Next

Now that you are familiar with creating a dataset from the sample data, you can create datasets using your own data from a [file](../migrating-and-importing-data/loading-data-from-a-file.md) (e.g., from a CSV, JSON, or JSONL file) or from a [URL](../migrating-and-importing-data/loading-data-from-a-url.md). You can also add more data to your datasets (click **Ingest data**) in the dataset overview or modify data via the dataset's **Database** page.

Interested in creating datasets programmatically? Check out [Apperate API Basics](../interacting-with-your-data/apperate-api-basics.md).

Want to learn more about creating and managing datasets? Read [Understanding Datasets](../managing-your-data/understanding-datasets.md).

Want to get more teammates involved? [Add them to your team](../administration/managing-users.md).

---
[Go to Docs Home](https://github.com/iexcloud/docs/blob/main/README.md)