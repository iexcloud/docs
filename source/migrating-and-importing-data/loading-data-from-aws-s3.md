# Loading Data from AWS S3

In few steps, you can import data from CSV, JSON, or JSONL data files in your S3 buckets. Accessing a bucket requires specifying the bucket and credentials to access it. You can configure bucket access as you create a dataset or *before* you create a dataset (recommended). Here are the access types:

- **Access Key:** Specify credentials composed of an access key and secret access key. For details, see [Accessing S3 via Your Access Key](./accessing-s3-via-your-access-key.md).
- **AWS storage integration:** Grant Apperate's S3 user read access to your bucket. Learn how at [Accessing S3 via Storage Integration](./accessing-s3-via-storage-integration.md).

Here we'll create a dataset from an S3 bucket file.

If you're accessing the bucket using an Access Key, skip to the *Adding an AWS S3 Source* section add your AWS S3 source before creating your dataset.

**Note:** The ability to create a dataset from an S3 source accessed by an Access key is coming soon. For now, if you're using an Access Key, please create your data source before creating your dataset.

If you're using AWS integration, continue.

## Creating a Dataset with Data from an S3 Bucket

1. Click **Create a Dataset** at the top of the console or from the **Datasets** page. The **Create a Dataset** page appears.

    ![](./loading-data-from-aws-s3/create-dataset-page.png)

1. In the **Use a new data source** section, choose **AWS S3 (storage integration)** in the source selector.

    ![](.//loading-data-from-aws-s3/select-aws-source-type.png)

    The AWS S3 bucket fields appear.

    TODO add image

1. Enter your AWS bucket name. 

1. Select your authorization mechanism.

    - If you have AWS integration configured already, there's no need to select anything. 
    - If you have a credential for the bucket in Apperate already, you can select that credential.
    - Otherwise, you can 1) create an AWS integration or 2) add credentials for accessing your bucket. Then select the option you just created.

    When you've connected with your bucket, your bucket filenames appear in a list.

1. Select the bucket file to load data from. A sample of the file contents appear in the response panel on the bottom left.

    **If your file is a CSV file**, click **Parse Data**. The **Dataset Schema** page appears.

    **If your file is a JSON file or JSONL file**, a sample of the data appears in a panel on the bottom left.

    > **Important:** To load data from JSON, the data must be specified in an array of objects.

    If the resulting data shown in the panel specifies the object array you want, leave the JSONNPath field empty. Otherwise, use the JSONPath field to specify the path to the desired object array in your data. A panel on the bottom right shows the data resulting from your JSONPath.

    
    > **See also** [Working with Nested JSON Data](./working-with-nested-json-data.md) for guidance on specifying JSONPath.

    When you're done specifying the path to your data, click **Parse Data**. Apperate ingests your data into a dataset and the dataset's **Overview** page appears.

TODO



## Adding an AWS S3 Source

Here's how to create an AWS S3 data source:

1. Navigate to Sources > Data Sources. The Data Sources list appears.

1. Click **Add a source**. The **Connect a data source** page appears.

1. Select **AWS S3** from the **Source Types** dropdown. The AWS S3 source fields appear.

1. Specify your S3 bucket file(s).

    **Data Source Name:** Enter a unique name.
    **Description:** Describe your data source. (Optional)
    **AWS bucket name:** Enter your bucket's name.
    **File pattern:** Enter your data file's explicit path within the bucket. 
    **JSONPath:** If your file is a JSON file or JSONL file and the data is nested in it, specify the nested location using JSONPath. 

    > **Important:** To load data from JSON, the data must be specified in an array of objects.

    If the resulting data shown in the Response panel specifies the object array you want, leave the JSONNPath field empty. Otherwise, use the JSONPath field to specify the path to the desired object array in your data. A panel on the bottom right shows the data resulting from your JSONPath.

    > **See also** [Working with Nested JSON Data](./working-with-nested-json-data.md) for guidance on specifying JSONPath.

    Click **Save Data Source** when you're done.

Apperate creates your data source and returns you to the **Data Sources** page. Your data source appears in the list and is ready to provide data.

Click *Create a dataset* and then under **Select an existing data source**, select the data source you just created.

## What's Next

Here are some things to explore doing with your new data and data source.

- Schedule data ingestion on your new data source. Learn how at [Scheduling Data Ingestion](./scheduling-data-ingestion.md).

- Provide custom views to the data by joining your dataset with a Core Dataset or one of your other datasets. See [Creating and Managing Views](../managing-your-data/creating-and-managing-views.md) for details.

- Use the data in your apps via your dataset API endpoints. Query for the exact data you want as demonstrated in [Apperate Query API](../interacting-with-your-data/apperate-query-api.md).