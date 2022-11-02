# Stream Data Using SSE

We support Server-sent Events ([SSE Streaming](https://en.wikipedia.org/wiki/Server-sent_events)) for streaming data as an alternative to WebSockets. You will need to decide whether SSE streaming is more efficient for your workflow than REST calls. In many cases, streaming is more efficient since you will only receive the latest available data. If you need to control how often you receive updates, then you may use REST to set a timed interval.

When you connect to an SSE endpoint, you should receive a snapshot of the latest message, then updates as they are available.

cURL Example:

```bash
curl --header 'Accept: text/event-stream' https://cloud-sse.iexapis.com/v1/stocksUS\?symbols\=spy\&token\=YOUR_TOKEN
```

cURL Firehose Example (Available with Business plans and legacy Scale plans):

```bash
curl --header 'Accept: text/event-stream' https://cloud-sse.iexapis.com/v1/stocksUS\?token\=YOUR_TOKEN
```

## Firehose

Scale plan users can firehose stream all symbols (except symbols from DEEP endpoints) by leaving off the `symbols` query parameter.

## Interval Streaming

Some SSE endpoints are offered on set intervals such as one second, five seconds, or one minute. This means we will send data no more than the interval subscribed to. This helps make data delivery and credit usage more predictable.