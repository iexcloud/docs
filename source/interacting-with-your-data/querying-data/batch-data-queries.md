# Batch Data Queries

Batch data queries are an API feature for querying multiple keys in multiple datasets. Responses include records for the keys from each dataset. This is convenient way to get data you want for multiple entities.

**Format:**

`GET /data/WORKSPACE/DATASET_A,DATASET_B/KEY_1,KEY_2`

The following table explains how to fill in the request.

| Placeholder | Replace with...
| --- | --- |
| `WORKSPACE` | Workspace is `CORE` for [IEX Cloud Core Datasets](https://iexcloud.io/docs/core) or the workspace name for [your datasets](https://iexcloud.io/docs/datasets). A batch data query can work in only one workspace at a time. You can optionally [create a view](../../managing-your-data/creating-and-managing-views.md) from Core data and your workspace data, and batch query that view. |
| `DATASET_A,DATASET_B` | Example: `QUOTE,NEWS`. The list of datasets to query. Note, each **Dataset ID** is specified in the dataset's reference page. For example, see the [CASH_FLOW](https://iexcloud.io/docs/core/CASH_FLOW) reference page. |
| `KEY_1,KEY_2` | Example: `AAPL,MSFT,TSLA`. The list of symbols to query for in the datasets. A dataset's primary index is labeled `key` in the dataset reference page's **Response Attributes** section. |
| `batchSeparator=,` | **(Optional)** The character for separating the request's dataset IDs and keys; comma (<code>,</code>) is the default separator.<br><br>**Supported separators:** `,` (default), `-`, `.`, `_`, `~` |

**Example:**

The following batch data request returns the latest stock price, fundamentals, and news for mobile carriers AT&T, T-Mobile, and Verizon.

`GET /data/CORE/QUOTE,FUNDAMENTALS,NEWS/T,TMUS,VZ`

**Result:**

The following records are paraphrased for illustration purposes.

```javascript
[
    {
        "symbol": "T",
        "close": 19.06,
        // more QUOTE record values
    },
    {
        "symbol": "TMUS",
        "close": 145.51,
        // more QUOTE record values
    },
    {
        "symbol": "VZ",
        "close": 38.31,
        // more QUOTE record values
    },
    {
        "symbol": "T",
        "pricePerEarnings": 205.758117055085,
        // more FUNDAMENTALS record values
    },
    {
        "symbol": "TMUS",
        "pricePerEarnings": 46.4663449079113,
        // more FUNDAMENTALS record values
    },
    {
        "symbol": "VZ",
        "pricePerEarnings": 11.6117199849925,
        // more FUNDAMENTALS record values
    },
    {
        "symbol": "T",
        "headline": "Should Investors Buy the Dip in Warner Bros. Discovery Stock?",
        // more NEWS record values
    },
    {
        "symbol": "TMUS",
        "headline": "T-Mobile US, Inc. (TMUS) New Street Research 5G Conference Call (Transcript)",
        // more NEWS record values
    },
    {
        "symbol": "VZ",
        "headline": "Verizon Communications Inc. (VZ) NSR & BCG Innovation Conference: 5G and Beyond. Cloud. Convergence 2022 (Transcript)",
        // more NEWS record values
    },
]
```

The resulting array includes records for each key (`T`,`TMUS`,`VZ`) found in each dataset (`QUOTE`,`FUNDAMENTALS`,`NEWS`), starting with the first dataset. 

The response is an array of dataset records. Records are returned from each dataset for each matched key, in the order that the request specified the datasets and keys. If a key is not matched in a dataset, no record is returned for that key/dataset combination.

If a query's [API token](../../reference/glossary.md#token-api-token) is unauthorized for a dataset, the endpoint returns a standard authorization error.

``` {important} A batch data query must operate on either Core datasets or your datasets--the two dataset types can't be mixed. Batch queries are not supported across workspaces.
```

``` {note} Record data returned from each dataset counts as a read. See [Credits and Pricing](../../administration/credits-and-pricing.md) for details.
```

``` {note} Each record returned counts towards your plan's maximum records per second. See [Pricing](https://iexcloud.io/pricing/) for record rate details.
```

## Make a Batch Data Request

Here are steps for making a batch data request.

1. Determine the key values ([primary index](../../reference/glossary.md#primary-index) values) to query on.

    Example: `T,TMUS,VZ` for AT&T, T-Mobile, and Verizon.

1. Determine the IDs of the datasets to search.

    Example: `QUOTE,FUNDAMENTALS,NEWS` for those Core datasets.

    You can browse [Your Datasets](https://iexcloud.io/docs/datasets) or the [Core Datasets](https://iexcloud.io/docs/core) in the API reference or in the [console](https://iexcloud.io/console) (requires Apperate plan).

1. Construct your batch data request on the [`/data`](https://iexcloud.io/docs/apperate-apis/data/get-data) endpoint, including the dataset IDs, the key values, a `batchSeparator` parameter (optional), your API token, and any other [`GET /data`](https://iexcloud.io/docs/apperate-apis/data/get-data) query parameters you want.

    Examples:

    `/data/CORE/QUOTE,FUNDAMENTALS,NEWS/T,TMUS,VZ?last=2`

    `/data/MY_WORKSPACE/DATASET_A,DATASET_B/foo,bar,baz?last=2`
    
    `/data/CORE/QUOTE.FUNDAMENTALS/SPY.MSFT?batchSeparator=.`

1. Execute your batch request.

    For example, click on the following URL and append your [API token](../../reference/glossary.md#token-api-token) as query parameter (e.g., `&token=YOUR_TOKEN`).

    [`/data/CORE/QUOTE,FUNDAMENTALS,NEWS/T,TMUS,VZ?last=2`](https://apis.iex.cloud/v1/data/CORE/QUOTE,FUNDAMENTALS,NEWS/T,TMUS,VZ?last=2)

Apperate returns an array of records for each key in each dataset, starting with the first dataset you specified.

## What's Next

[Create Views](../../managing-your-data/creating-and-managing-views.md) demonstrates combining Core data and workspace data into views.

[Querying Datasets](./querying-datasets.md) shows how to search data from any dataset (Core or your) using the Get Data endpoint.

[Querying Datasets with iex.js](./querying-datasets-with-iexjs.md) makes querying even easier by leveraging a simple, open-source client library for JavaScript.