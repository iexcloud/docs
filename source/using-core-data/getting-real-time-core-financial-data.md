# Getting Real-Time Core Financial Data

The IEX Cloud API is based on REST, has resource-oriented URLs, returns JSON-encoded responses, and returns standard HTTP [response codes](https://iexcloud.io/docs/api/#error-codes). We support [JSONP](https://en.wikipedia.org/wiki/JSONP) for all endpoints.

The API's base URL comprises the API's domain and latest version.

**Base URL:** `https://cloud.iexapis.com/v1`

As an example of getting real-time core data, you'll call the stock quote endpoint to get the latest quote for a stock.

**Prerequisites:**

- **IEX Cloud Apperate account** - Create one [here](https://iexcloud.io/cloud-login#/register).

## Getting a Stock Quote

Here we'll get the latest quote for Apple.

1. Open the [Legacy API Reference](https://iexcloud.io/docs/api/) in your browser. The IEX Cloud API Reference appears.

    ![](./getting-real-time-core-financial-data/iexcloud-api-reference.png)

1. Navigate to the **Core Data &rarr; Stocks / Equities &rarr; Quote** reference [page](https://iexcloud.io/docs/api/#quote). The Quote reference page appears.

    ![](./getting-real-time-core-financial-data/quote-reference-page.png)

    We'll call the `GET /stock/{symbol}/quote` method to get an entire quote.

1. In a browser, enter a request URL to get a stock quote for Apple, following this URL format:

    ```
    BASE_URL + /stock/{symbol}/quote + TOKEN
    ```

    Here's the URL to enter, replacing `{symbol}` with `aapl` and `TOKEN` with your token value.

    ```
    https://cloud.iexapis.com/v1/stock/aapl/quote?token=TOKEN
    ```

    The endpoint returns the quote in the response as a JSON object like this one:

    ```javascript
    {
        "avgTotalVolume": 66796228,
        "calculationPrice": "tops",
        "change": 1.765,
        "changePercent": 0.01054,
        "close": 167.53,
        "closeSource": "official",
        "closeTime": 1661371200838,
        "companyName": "Apple Inc",
        "currency": "USD",
        "delayedPrice": 169.12,
        "delayedPriceTime": 1661451155481,
        "extendedChange": -0.515,
        "extendedChangePercent": -0.00304,
        "extendedPrice": 168.78,
        "extendedPriceTime": 1661434199996,
        "high": 169.92,
        "highSource": "15 minute delayed price",
        "highTime": 1661451155481,
        "iexAskPrice": 170,
        "iexAskSize": 1005,
        "iexBidPrice": 161.87,
        "iexBidSize": 112,
        "iexClose": 169.295,
        "iexCloseTime": 1661452054786,
        "iexLastUpdated": 1661452054786,
        "iexMarketPercent": 0.018660376776247826,
        "iexOpen": 168.78,
        "iexOpenTime": 1661434200050,
        "iexRealtimePrice": 169.295,
        "iexRealtimeSize": 1,
        "iexVolume": 622237,
        "lastTradeTime": 1661452054786,
        "latestPrice": 169.295,
        "latestSource": "IEX real time price",
        "latestTime": "2:27:34 PM",
        "latestUpdate": 1661452054786,
        "latestVolume": 33345361,
        "low": 168.35,
        "lowSource": "IEX real time price",
        "lowTime": 1661446142401,
        "marketCap": 2720697959840,
        "oddLotDelayedPrice": 169.11,
        "oddLotDelayedPriceTime": 1661451155653,
        "open": 168.68,
        "openTime": 1661434200590,
        "openSource": "official",
        "peRatio": 27.98,
        "previousClose": 167.53,
        "previousVolume": 53841524,
        "primaryExchange": "NASDAQ",
        "symbol": "AAPL",
        "volume": 33345361,
        "week52High": 182.19,
        "week52Low": 128.86,
        "ytdChange": -0.04209681715828372,
        "isUSMarketOpen": true
    }
    ```

    ```{note} The [Quote](https://iexcloud.io/docs/api/#quote) reference page describes the response attributes.
    ```

Congratulations! You know how to get IEX Cloud production-ready financial data for your apps.

## What's Next

Now that you know how to get real-time IEX Cloud data, explore the [Legacy API Reference](https://iexcloud.io/docs/api/) for more data to use in your apps.

If you're interested in historical time series data, check out [Getting Time Series Core Financial Data](getting-time-series-core-financial-data.md).

If you need to store application data, learn how at [Writing and Fetching a Data Record](../getting-started/writing-and-fetching-a-record.md).
