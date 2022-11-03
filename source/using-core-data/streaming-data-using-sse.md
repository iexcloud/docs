# Stream Data Using SSE

We stream data using Server-Sent Events ([SSE](https://en.wikipedia.org/wiki/Server-sent_events)). When you connect to an SSE Streaming endpoint, it returns a snapshot of the latest message at first and then returns updates as they become available (or at set intervals).

Here you'll learn about the SSE Streaming endpoints and how credits work with streaming.

SSE Streaming is currently available via [IEX Cloud's legacy SSE Streaming endpoints](https://iexcloud.io/docs/api/#sse-streaming) only.

``` {note} In many cases, SSE Streaming is more efficient than REST calls because the streaming returns only the latest available data. SSE Streaming has 1 second, 5 second, and 1 minute interval-based endpoints. If you need more timing control, you may want to use REST calls at timed intervals.
```

## How Credits Work with Streaming

For Apperate plans, **each message received over the stream counts as a read**.

**1 million reads = 1 credit**

``` {important} Unlike other cloud databases that charge based on table scans and/or data blocks, a read on Apperate equates to getting a **whole** record/row.
```

``` {seealso} [Credits and Pricing](../administration/credits-and-pricing.md)
```

## US Stocks

The `stockUS` endpoint returns real-time prices, volume, and quotes for **all** [National Market System \(NMS\) US securities](https://www.finra.org/filing-reporting/oats/oats-reportable-securities-list) sourced from the Investors Exchange. Real-time quotes for Nasdaq-listed symbols from trades on the Investors Exchange

Users on paid plans can also receive **DELAYED** Nasdaq-listed securities data, including open, close, extended hours prices, and other derived values by getting authorization from UTP Plan, as described in [Get Nasdaq-listed Stock Data \(UTP/OTC Data\)](./getting-nasdaq-listed-utp-otc-stock-data.md#how-do-i-get-utp-authorization).

If you want to stream data on a specific symbol(s), add the `symbols` query parameter and set it to a symbol or a comma-separated list of symbols.

Example:

```bash
curl --header 'Accept: text/event-stream' 'https://cloud-sse.iexapis.com/v1/stocksUS?symbols=spy,msft&token=YOUR_TOKEN'
```

## Firehose

If you have the Scale plan and you want to stream data on all available symbols (except symbols from DEEP endpoints), leave off the `symbols` query parameter. This is called **Firehose**.

Firehose example:

```bash
curl --header 'Accept: text/event-stream' 'https://cloud-sse.iexapis.com/v1/stocksUS?token=YOUR_TOKEN'
```

## Interval Streaming

Some SSE endpoints return data at (or shortly after) the endpoint's set interval: 1 second, 5 seconds, or 1 minute. This helps make data delivery and credit usage more predictable.

1 second interval:

```bash
curl --header 'Accept: text/event-stream' 'https://cloud-sse.iexapis.com/v1/stocksUS1Second?token=YOUR_TOKEN&symbols=spy'
```

5 second interval:

```bash
curl --header 'Accept: text/event-stream' 'https://cloud-sse.iexapis.com/v1/stocksUS5Second?token=YOUR_TOKEN&symbols=spy'
```

1 minute interval:

```bash
curl --header 'Accept: text/event-stream' 'https://cloud-sse.iexapis.com/v1/stocksUS1Minute?token=YOUR_TOKEN&symbols=spy'
```

## NoUTP Endpoints

SSE endpoints ending in the `NoUTP` suffix return real-time prices, volume, and quotes for **all** [National Market System \(NMS\) US securities](https://www.finra.org/filing-reporting/oats/oats-reportable-securities-list) sourced from the Investors Exchange. **DELAYED** Nasdaq-listed securities data is excluded. 

`NoUTP` example:

```bash
curl --header 'Accept: text/event-stream' 'https://cloud-sse.iexapis.com/v1/stocksUSNoUTP?token=YOUR_TOKEN&symbols=spy'
```

## What's Next

Now you're familiar with some of the SSE Streaming endpoints. Try out more SSE Streaming endpoints as described in the [Legacy API](https://iexcloud.io/docs/api/#sse-streaming).