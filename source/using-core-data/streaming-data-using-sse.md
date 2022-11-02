# Stream Data Using SSE

We stream data using Server-sent Events ([SSE](https://en.wikipedia.org/wiki/Server-sent_events)) as an alternative to using WebSockets. When you connect to an SSE endpoint, you receive a snapshot of the latest message first and then receive updates as they become available.

SSE Streaming is currently available only using [IEX Cloud's legacy SSE Streaming endpoints](https://iexcloud.io/docs/api/#sse-streaming).

``` {note} You must decide whether SSE streaming is more efficient than REST calls for your workflow. In many cases, streaming is more efficient because you receive only the latest available data. If you need more control over update frequency, you may want to use REST to set a timed interval.
```

## Pricing

For Apperate plans, **each message received over the stream counts as a read**.

**1 million reads = 1 credit**

``` {important} Unlike other cloud databases that charge based on table scans and/or data blocks, a read on Apperate equates to getting a **whole** record/row.
```

## US Stocks

`stocksUS` example:

```bash
curl --header 'Accept: text/event-stream' 'https://cloud-sse.iexapis.com/v1/stocksUS?symbols=spy&token=YOUR_TOKEN'
```

``` {important} 
IEX Cloud provides real time prices, volume, and quotes for **all** [NMS](https://www.finra.org/filing-reporting/oats/oats-reportable-securities-list) US securities; sourced from the Investors Exchange. In order to receive **DELAYED** Nasdaq-listed security data through the `stocksUS` endpoint Nasdaq UTP requires you to complete a [Vendor Agreement](http://www.utpplan.com/DOC/VendorAgreement.pdf). Delayed prices include open, close, extended hours prices, and other derived values. All users will continue to receive real time Investors Exchange data for free. **DELAYED** NYSE listed symbols are only available to paid users due to reporting requirements.
```

## No UTP Endpoints

SSE endpoints ending in the `NoUTP` suffix return no UTP data. 

`NoUTP` example:

```bash
curl --header 'Accept: text/event-stream' 'https://cloud-sse.iexapis.com/v1/stocksUSNoUTP?token=YOUR_TOKEN&symbols=spy'
```

## Firehose

If you want to stream data on a specific set of symbols, set the `symbols` query parameter to those symbols, separated by commas.

`symbols` parameter example:

```bash
curl --header 'Accept: text/event-stream' 'https://cloud-sse.iexapis.com/v1/stocksUS?symbols=spy,msft&token=YOUR_TOKEN'
```

If you have the Scale plan and you want to stream data on all available symbols (except symbols from DEEP endpoints), leave off the `symbols` query parameter. This is called **Firehose**.

Firehose example:

```bash
curl --header 'Accept: text/event-stream' 'https://cloud-sse.iexapis.com/v1/stocksUS?token=YOUR_TOKEN'
```

## Interval Streaming

Some SSE endpoints are offered on set intervals such as one second, five seconds, or one minute. This means we will send data no more than the interval subscribed to. This helps make data delivery and credit usage more predictable.

Interval Streaming examples:

```bash
curl --header 'Accept: text/event-stream' 'https://cloud-sse.iexapis.com/v1/stocksUS5Second?token=YOUR_TOKEN&symbols=spy'
```

```bash
curl --header 'Accept: text/event-stream' 'https://cloud-sse.iexapis.com/v1/stocksUS1Minute?token=YOUR_TOKEN&symbols=spy'
```

## What's Next

Try out the [SSE Streaming endpoints](https://iexcloud.io/docs/api/#sse-streaming) available in the Legacy API.