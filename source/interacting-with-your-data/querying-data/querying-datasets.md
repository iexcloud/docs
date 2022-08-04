# Querying Datasets

Datasets that have a primary index and date index (it's included by default) leverage time series. The time series excels at retrieving records within specific time ranges. The `GET /data/...` endpoint supports these features.

Here you'll get familiar with the query data endpoint and use time series parameters to get dataset records that match a time range.

## Understanding the GET /data/ Endpoint

Apperate API URLs include your workspace [base URL](../apperate-api-basics.md), the API version, an endpoint, and any query parameters (API token is required).

**URL Structure:**

```
BASE_URL/VERSION/ENDPOINT?token=TOKEN
```

Here's the standard query data endpoint format:

```
GET /data/:workspace/:id/:key?/:subkey?
```

It has these parameters:

| Path Parameter | Description |
| -------------- | ----------- |
| `workspace` | (Required) Workspace ID |
| `id` | (Required) Dataset ID |
| `key` | (Required) Primary index |
| `subkey` | (Optional) Secondary index |

The endpoint is easy to understand and use. After `/data/`, you specify your workspace ID and dataset ID path parameters, enter your primary index (key) value, and add any query parameters you want.

For example, this URL returns a dataset record for the key value `AAPL`:

```
https://myworkspace.iex.cloud/v1/data/MYWORKSPACE/SAMPLE_AAPL_DATASET_M3RCT0SSX/AAPL?token=TOKEN
```

> **Note:** The query data endpoint returns one record at most unless you specify a date subkey, `range`, or a higher `limit` value.

Let's explore filtering on a time range next.

## Filtering on a Time Range

All time series endpoint parameters apply to the `GET /data/:workspace/:id/:key?/:subkey?` endpoint. The time series query parameters allow you to get records for the time frame you want. 

For example, this query uses the `from` and `to` time series query parameters, to retrieve records for a specific set of days.

```
https://my.iex.cloud/v1/data/MY/SAMPLE_AAPL_DATASET_M3RCT0SSX?token=TOKEN&from=2019-02-13&to=2019-02-20
```

Result:

```javascript
[{"close":43.0075,"date":"2019-02-20","high":43.33,"low":42.7475,"open":42.7975,"symbol":"AAPL","volume":104457448},{"close":42.7325,"date":"2019-02-19","high":42.86,"low":42.3725,"open":42.4275,"symbol":"AAPL","volume":75891304},{"close":42.605,"date":"2019-02-15","high":42.925,"low":42.4375,"open":42.8125,"symbol":"AAPL","volume":98507256},{"close":42.7,"date":"2019-02-14","high":42.8154,"low":42.345,"open":42.4275,"symbol":"AAPL","volume":87342988},{"close":42.545,"date":"2019-02-13","high":43.12,"low":42.48,"open":42.8475,"symbol":"AAPL","volume":89960932}]
```

There are parameters that facilitate filtering on specific quarters and semesters, and the previous/current/future days, weeks, months, and years. For more details and examples, please see the [time series endpoint reference documentation](https://iexcloud.io/docs/guides/time-series).

## What's Next

If you want to get data from Apperate's other endpoints, please see [Core Data Endpoints](../../using-core-data.md#core-data-endpoints).

---
[Go to Docs Home](https://github.com/iexcloud/docs/blob/main/README.md)