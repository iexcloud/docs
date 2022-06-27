# Apperate API Basics

> **Note:** IEX Cloud Apperate is available exclusively to select Early Access Program participants If you would like to participate in the Early Access Program or the upcoming Beta, please email us at `product@iexcloud.io`.

The datasets API has RESTful endpoints for building datasets programmatically. They are documented in the IEX Cloud API docs site's [Datasets API](https://iexcloud.io/docs/datasets-api) section.

![](./apperate-api-basics/datasets-api-in-docs.png)

Here you will learn the basics of using the datasets API, create a dataset using the API, and get data from the dataset using the auto-generated RESTful API.

## Datasets API basics

The datasets API leverages the IEX Cloud Core API infrastructure, including these components:

- [Base URL](https://iexcloud.io/docs/guides/rest-how-to)
- [Versioning](https://iexcloud.io/docs/getting-started/versioning) and [deprecations](https://iexcloud.io/docs/getting%20started/deprecation)
- [API Tokens](https://iexcloud.io/docs/getting-started/api-tokens)
- [Error codes](https://iexcloud.io/docs/getting-started/error-codes)
- And more (see the docs site's [Getting Started](https://iexcloud.io/docs/getting-started) and [Guides](https://iexcloud.io/docs/guides) sections for more information)

Dataset endpoint URLs start with the *[base URL + API version*, as described in the [Versioning](https://iexcloud.io/docs/getting%20started/versioning). For example,

**Base URL (v1):** <https://cloud.iexapis.com/v1>

In the example here, you will use the above base URL. 

### Requirements

The API endpoint requests you will run have these requirements.

- **Workspace name** -- You must qualify your HTTP requests with your workspace name. See [Setting Up Your Workspace](../getting-started/setting-up-your-workspace.md) to learn more.
- **Secret API token** -- You must submit your secret API token as a query parameter with your HTTP requests. See [API Tokens](https://iexcloud.io/docs/getting-started/api-tokens) for more information.

> **Important:** The secret token can perform any action on your data and account. **Never** share your secret token publicly.

### Quick test

Check your workspace and secret API token by using the *GET /datasets/:workspace* request as described in [List datasets](https://iexcloud.io/docs/datasets-api/list-datasets). Run this request on your command line, replacing `WORKSPACE` and `SK_NUMBER` with your workspace and secret API token values.

```bash
curl -X GET https://cloud.iexapis.com/v1/datasets/WORKSPACE?token=SK_NUMBER 
```

The response should be a JSON array of your datasets, or an empty collection if you have no datasets. The start of the reponses looks like this:

```json
[{"columnMapping":{"date":"date","key":"symbol"},"symbologyColumn":{"name":"symbol","type":"E"},"date":1650483685000,"updated":1650483685000,"datasetId":"MSFT_ISIN_0YUMDPOZA","schema":{"properties":{"close":{"type":"number"},"date":{"format":"date","type":"string"},"high":{"type":"number"},"low":{"type":"number"},"open":{"type":"number"},"symbol":{"type":"string"},"volume":{"type":"string"}},"required":["symbol","date"],"type":"object"},"description":"","parentDatasetId":null,"keys":0,"records":1509}]
```

> **Note:** If the response states The API key provided is not valid[, your API token (key) is not valid. Make sure to use the secret API token available to copy from your console's [API tokens](https://iexcloud.io/console/tokens) page.

The first step in delivering data to your apps is creating a dataset.

## Creating a dataset

Here you will create a dataset as specified in a JSON text file.

1. Create a .json file that has the following content. Replace `you@company.com`, `Your Company`, and `Your Dataset`, with your own values.

    > **Important:** The `_system` prefix (case-insensitive) is reserved for Apperate system tables and columns. You are forbidden to prefix dataset IDs and dataset property names with `_system`.

    ```
    { 
        "dataset": { 
            "email": "you@company.com", 
            "schema": { 
                "properties": { 
                    "close": { 
                        "type": "number" 
                    }, 
                    "date": { 
                        "type": "string", 
                        "format": "date" 
                    }, 
                    "high": { 
                        "type": "number" 
                    }, 
                    "low": { 
                        "type": "number" 
                    }, 
                    "open": { 
                        "type": "number" 
                    }, 
                    "symbol": { 
                        "type": "string" 
                    }, 
                    "volume": { 
                        "type": "integer" 
                    } 
                }, 
                "required": [ 
                    "symbol", 
                    "date" 
                ], 
                "type": "object" 
            }, 
            "source": "Your Company", 
            "columnMapping": { 
                "key": "symbol", 
                "date": "date" 
            }, 
            "symbologyColumn": { 
                "name": "symbol", 
                "type": "E" 
            }, 
            "title": "SAMPLE AAPL DATASET YOU", 
            "datasetId": "SAMPLE_AAPL_DATASET_YOU" 
        } 
    }
    ```

1. Create a dataset from the .json file by running a `POST /datasets/:workspace` request as described in [Create a dataset](https://iexcloud.io/docs/datasets-api/create-a-dataset). For example, run this command, replacing the *WORKSPACE, SK_NUMBER,* and *FILE* values with your own.

    ```bash
    curl -H "Content-Type: application/json" 
     -X POST "https://cloud.iexapis.com/v1/datasets/WORKSPACE?token=SK_NUMBER" 
     --data-binary @FILE.json
    ```

    **Sample response:**
    
    ```json
    {"success":true,"message":"Dataset has been created","datasetId":"YOUR_DATASET"}
    ```

1. Verify the dataset by running a `GET /datasets/:workspace` request as described in [List datasets](https://iexcloud.io/docs/datasets-api/list-datasets). For example,

    ```bash
    curl -X GET https://cloud.iexapis.com/v1/datasets/WORKSPACE?token=SK_NUMBER
    ```

Let's add data to the dataset.

## Adding data to your dataset

Here you will specify data in a CSV file and submit the file in your request to create a dataset

> **Note:** You can specify data in text files that use CSV, JSON, and JSONL formats. The product supports CSV files that use the following common data delimiters: comma (,), tab, or pipe (|) characters.

Here are the data file ingestion steps:

1. Specify the data in a CSV. Here's a CSV data file. 
     
    **[Data:** 

    ```
    close,date,high,low,open,symbol,volume
    27.72,2016-11-09,27.83,27.0125,27.47,AAPL,236705444
    27.9475,2016-11-25,27.9675,27.7375,27.7825,AAPL,45903688
    27.8925,2016-11-28,28.1163,27.8475,27.8575,AAPL,108775932
    ```

    > **Tip:** Create the file using the following Example Command for your operating system.

    **Example Command** 

    Linux/MacOS

    ```bash
        echo " close,date,high,low,open,symbol,volume
        27.72,2016-11-09,27.83,27.0125,27.47,AAPL,236705444
        27.9475,2016-11-25,27.9675,27.7375,27.7825,AAPL,45903688
        27.8925,2016-11-28,28.1163,27.8475,27.8575,AAPL,108775932
        " \
        >> aapl
    ```

    Windows

    ```
        (
        echo close,date,high,low,open,symbol,volume
        echo 27.72,2016-11-09,27.83,27.0125,27.47,AAPL,236705444
        echo 27.9475,2016-11-25,27.9675,27.7375,27.7825,AAPL,45903688
        echo 27.8925,2016-11-28,28.1163,27.8475,27.8575,AAPL,108775932
        )>aapl
    ```

1. Ingest the data to your dataset using a `POST /data/:workspace/:id` requestas described in [Ingest data](https://iexcloud.io/docs/datasets-api/ingest-data). For example, use this command, replacing the `WORKSPACE`, `YOUR_DATASET`, and `SK_NUMBER` values with your own: 

    ```bash
    curl -H "Content-Type: application/json" \
        -X POST "https://cloud.iexapis.com/v1/data/WORKSPACE/YOUR_DATASET?token=SK_NUMBER" \
     --data-binary @aapl
    ```

    **Sample response:** 

    ```json
    {"success":true,"message":"Data upload of 579B for YOUR_DATASET completed, jobId: 887b948762ff4b5c889112afb21ea463 has been created","jobId":"887b948762ff4b5c889112afb21ea463","jobUrl":"/v1/jobs/WORKSPACE/ingest/887b948762ff4b5c889112afb21ea463"}
    ```

1. Validate your dataset's record count using a `GET /datasets/:workspace/:id` request as described in [Get a dataset](https://iexcloud.io/docs/datasets-api/get-a-dataset). For example, use this command with your values:  

    ```bash
    curl -X GET https:/cloud.iexapis.com/v1/datasets/WORKSPACE/YOUR_DATASET?token=SK_NUMBER
    ```

    **Sample response:** 

    ```json
    {" columnMapping":{" date":"date","key":"symbol"}," symbologyColumn":{" name":"symbol","type":"E"},"date":1650569968000,"updated":1650569968000,"datasetId":" YOUR_DATASET ","schema":{"properties":{"close":{" type":"number"},"date":{" format":"date","type":"string"},"high":{" type":"number"},"low":{" type":"number"},"open":{" type":"number"},"symbol":{" type":"string"},"volume":{" type":"integer"}},"required":[" symbol","date"]," type":"object"},"description":"","parentDatasetId":null,"keys":0,"records":3}
    ```

    The records value `"records":3` matches the number of records in your data file. Your data is ready for apps to access!

Lastly check out your dataset's auto-generated RESTful API and use it.

## Using your dataset API

A RESTful API endpoint was automatically created for your dataset.

1. Visit your API docs in your browser at the following URL, replacing the dataset name. 

    **URL:** `https://iexcloud.io/docs/datasets/YOUR_DATASET` 

    ![](./apperate-api-basics/custom-dataset-api-docs.png)

1. As a test, get your last record by copying this URL in your browser, replacing `WORKSPACE`, `YOUR_DATASET`, and `SK_NUMBER`. 

    **URL:** `https://cloud.iexapis.com/v1/data/WORKSPACE/YOUR_DATASET?last=1&token=SK_NUMBER`

    **Sample response:** 

    ```json
    [{"close":47.8925,"date":"2017-11-28","high":28.1163,"low":27.8475,"open":27.8575,"symbol":"AAPL","volume":108775932}]
    ```

Congratulations on making your data available using the datasets API!

## What's Next

[Now that you're familiar with using the datasets API to create and use datasets, you can explore more dataset API endpoints or execute [SQL queries](https://iexcloud.io/docs/datasets-api/sql-query) via the API.