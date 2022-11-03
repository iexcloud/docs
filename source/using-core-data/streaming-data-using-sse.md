# Stream Data Using SSE

We stream data using Server-Sent Events ([SSE](https://en.wikipedia.org/wiki/Server-sent_events)). We provide endpoints for streaming the following types of data:

- US stocks and securities
- Cryptocurrency
- Forex / currencies
- News
- Social sentiment
- [IEX Tops](https://iexcloud.io/docs/api/#tops)
- [IEX Last](https://iexcloud.io/docs/api/#last)
- [IEX Deep](https://iexcloud.io/docs/api/#deep)

The endpoints are available via the IEX Cloud Legacy API and described in the [Legacy API Reference](https://iexcloud.io/docs/api/#sse-streaming).

There are three types of endpoints for US stocks and securities. Two of them require a paid plan and a UTP agreement. Here's an overview of these endpoints:

| Endpoint | Response Data | Requirements |
| --- | --- | --- |
| `stocksUS` | - IEX real-time data<br>- 15 min delayed Nasdaq listed data (UTP)<br>- 15 min delayed NYSE listed data (CTA) | - Paid plan<br> - UTP agreement |
| `stocksUSNoUTP` | - IEX real-time data<br>- 15 min delayed NYSE listed data (CTA) | None |
| `stocksOTC` | - 15 min delayed OTC data | - Paid plan<br>- UTP agreement with OTC eligibility |

[Get Nasdaq-listed Stock Data \(UTP/OTC Data\)](./getting-nasdaq-listed-utp-otc-stock-data.md#how-do-i-get-utp-authorization) explains the UTP agreement process.

## How Credits Work with Streaming

For Apperate plans, **each message received over the stream counts as a read**.

**1 million reads = 1 credit**

``` {important} Unlike other cloud databases that charge based on table scans and/or data blocks, a read on Apperate equates to getting a **whole** record/row.
```

``` {seealso} [Credits and Pricing](../administration/credits-and-pricing.md)
```

## Firehose Versus Streaming on Symbols

You can stream on specific symbols or stream everything -- like *drinking from a firehose*.

The `symbols` query parameter enables you to stream on a specific symbol or comma-separated list of symbols. The examples below respectively demonstrate calling the `stocksUS` endpoint on specific symbols and all symbols.

**Stream on symbols:**

```bash
curl --header 'Accept: text/event-stream' 'https://cloud-sse.iexapis.com/v1/stocksUS?symbols=spy,msft&token=YOUR_TOKEN'
```

**Firehose:**

```bash
curl --header 'Accept: text/event-stream' 'https://cloud-sse.iexapis.com/v1/stocksUS?token=YOUR_TOKEN'
```

You can use the `symbols` parameter with all the streaming endpoints.

``` {note} Firehose functionality does not apply to IEX DEEP streaming endpoints.
```

## Snapshots

When you connect to an SSE endpoint, you receive a snapshot of the latest message and then receive updates as they are available. You can disable snapshots by using the query parameter setting `nosnapshot=true`.

You can also specify a starting point for a snapshot by using a query parameter setting `snapshotAsOf=EPOCH_TIMESTAMP`, where the value is in [milliseconds since Epoch](https://currentmillis.com/).

## Interval Streaming 

Some data is available to stream at set intervals: 1 second, 5 seconds, or 1 minute. This helps make data delivery and credit usage more predictable. The endpoints below, for example, compliment the `stocksUS` endpoint.

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

## What's Next

Now you're familiar with some of the SSE Streaming endpoints. You can try more SSE Streaming endpoints as described in the [Legacy API Reference](https://iexcloud.io/docs/api/#sse-streaming).