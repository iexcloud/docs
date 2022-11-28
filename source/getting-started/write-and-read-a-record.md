# Write and Read Data

Apperate makes writing data a snap. You can write data via the console or do it programmatically using Apperate's RESTful [Data API](https://iexcloud.io/docs/apperate-apis/data/), or using the [iex.js JavaScript library](../developer-tools/iexjs-library.md) (iexjs) which wraps the Data API in JavaScript methods.

The `apperate.write()` iexjs method takes an object array (specified using JSON) as input and creates data records from the objects.

For example, you could write a news event using an array like this one:

```javascript
[
    {
        "headline": "Space traveler bids are stacking up",
        "content": "You may know some of these celebrities and billionaires ...",
        "ticker": "AMZN",
        "source": "IEX Underground",
        "date": "2022-07-14"
    }
]
```

``` {note} The object array can include as many objects as you like; though the write method is intended for writing one or a few records in real time. [Load Data](../migrating-and-importing-data.md) describes recommended ways for writing large numbers of records in a single call.
```

``` {seealso} The [Write Data](https://iexcloud.io/docs/apperate-apis/data/write-data) reference page describes the POST /write method and its parameters.
```

Here we'll use the iexjs library to write the data above and to retrieve that data.

## Write Data with apperate.write()

Here's how to write data using the `apperate.write()` [iexjs](https://www.npmjs.com/package/@apperate/iexjs) JavaScript library method.

1. Open an npmjs environment, such as [RunKit](https://npm.runkit.com/%40apperate%2Fiexjs).

    ![](./write-and-read-a-record/runkit.png)

    Optionally, you can install iexjs with [npm](https://www.npmjs.com) and use iexjs locally:
    
    ```bash
    npm install --save iexjs
    ```

1. Copy the following code into your editor and replace the CAPITALIZED parameter values mentioned below. 

    **Code:**

    ```javascript
    const {Client} = require("@apperate/iexjs")
    const client = new Client({api_token: "SECRET_TOKEN", version: "VERSION"});
    client.apperate.write({
        workspace: "WORKSPACE", 
        id: "DATASET", 
        createDatasetOnDemand: true, 
        data: [{"headline": "Space traveler bids are stacking up", "content": "You may know some of these celebrities and billionaires ...", "ticker": "AMZN", "source": "IEX Underground", "date": "2022-07-14"}]})
            .then((res) => {
                console.log(res);
        });
    ```

    The first two lines of code import the iexjs `Client` definition and instantiate it. The `apperate.write` method call writes data from the `data` parameter into the target dataset specified by the `id` and `workspace` parameters. The `createDatasetOnDemand: true` setting instructs Apperate to create the dataset if it doesn't exist already.

    **Replace in the Code**

    | Placeholder | Replace with ... |
    | --- | --- |
    | `SECRET_TOKEN` | Your [secret API token](../reference/glossary.md#secret-token-secret-key) |
    | `VERSION` | Apperate API version (`v1` is the current version) |
    | `WORKSPACE` | Your [workspace](../reference/glossary.md#workspace) name |
    | `DATASET` | Target dataset ID (the ID of an existing dataset to populate or a new dataset to create) |

1. Run the code. Apperate writes the data record to the target dataset and returns a response like this:

    ```javascript
    {success: true, message: "wrote 1 messages"}
    ```

    If the dataset doesn't exist already, Apperate creates a new dataset, giving it the name you specified and inferring its schema from the data you provided.

Here's what the response looks like in RunKit.

![](./write-and-read-a-record/loadData-response.png)

That was fast and easy, right?! If you opted to generate a new dataset, using the `createDatasetOnDemand: true` setting, let's examine the dataset.

## Examine the Generated Dataset

1. In the Console, go to the [Datasets](https://iexcloud.io/console/datasets/) page, click on your Workspace, and refresh the page. The listing includes your dataset.

1. Click on the name of the dataset. The dataset overview appears.

1. Click **Edit Schema**. The schema editor appears. 

    ![](./write-and-read-a-record/my-news-dataset-schema.png)

    Notice the index assignments and types. Apperate selected the `ticker` property as the Primary Index (aka *key*), and also selected Secondary (*subkey*) and Date (*date*) indexes. The indexes combine to uniquely identify the dataset records.

    ``` {note} You can update the schema as you like. See [Modify a Data Schema](../managing-your-data/updating-a-dataset-schema.md) for details.
    ```

Let's search the target dataset for the data you wrote.

## Query the Data

You can query the data just as easily as you wrote it. Let's retrieve a data record using the iexjs library's `apperate.queryData` method. 

1. In your app or RunKit, enter the following code and make sure to replace the CAPITALIZED values.

    **Code:**

    ```javascript
    const {Client} = require("@apperate/iexjs")
    const client = new Client({api_token: "SECRET_TOKEN", version: "VERSION"});
    client.apperate.queryData({
        workspace: "WORKSPACE", 
        id: "DATASET", 
        data: [{"key": "AMZN"}]})
            .then((res) => {
                console.log(res);
    });
    ```

    The `apperate.queryData` method's `data` parameter takes an object array that includes a `key` index, and may also include a `subkey` and/or `date` index. The code above just uses a `key` index. Here are the the respective attributes for mapping them in your object array:
    
    - `key`: Primary index
    - `subkey`: Secondary index
    - `on`:  Query parameter to search on a Date index.

    ``` {note}
    A dataset's [API docs](https://iexcloud.io/docs/) indicate all applicable data indexes (e.g., key, subkey, date). 
    ```

1. Run the code. Apperate returns the matching records in a query response and prints it. 

Here's what the query response looks like in RunKit.

![](./write-and-read-a-record/queryData-response.png)

Congratulations! You wrote data to Apperate and queried that data.

## What's Next

Now that you know how to write and query data, here are some topics to consider next:

[Search Data](../interacting-with-your-data.md): These articles show various ways to query data.

[Managing Your Data](../managing-your-data.md): These guides explain dataset schema fundamentals, creating views, and creating datasets via the  Datasets API.

[Production-Ready IEX Cloud Core Financial Data](./production-ready-core-data.md): Introduces Apperate's 5+ terabytes of built-in financial data available for enriching your fintech applications.

[Load Data](../migrating-and-importing-data.md): These tutorials show you how to load data from a URL, an AWS S3 bucket, and more.