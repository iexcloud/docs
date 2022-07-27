# Using Apperate's APIs

Apperate's APIs are based on [REST](https://en.wikipedia.org/wiki/Representational_state_transfer), have resource-oriented URLs, and return JSON-encoded responses and standard HTTP response codes. 

The [API Reference](https://iexcloud.io/docs/) (<https://iexcloud.io/docs/>) site aggregates the reference documentation, provides a "Getting Started" guide, and explains key concepts. 

Here's a screenshot of the [Getting Started](https://iexcloud.io/docs/getting-started) guide and the API Reference navigation:

![](./apperate-api-basics/api-reference-getting-started.png)

The tutorials here in this site compliment the API Reference by demonstrating how to complete different tasks using the APIs.

Here are some of the task areas and links to applicable API Reference pages and tutorial sections.

## Querying Data

You can query your datasets and Core Datasets using the Data API. The [Datasets](https://iexcloud.io/docs/datasets) pages describe your dataset endpoints and the [Core Data](https://iexcloud.io/docs/core) pages describe the Core Dataset endpoints. [Querying Time Series Data](./querying-data/querying-time-series-data.md) demonstrates querying data from them.

The API Reference's [Reference Data](https://iexcloud.io/docs/reference-data), [IEX Exchange](https://iexcloud.io/docs/iex-exchange), and [Miscellaneous](https://iexcloud.io/docs/miscellaneous) sections describe the endpoints for Core Data that are not time series. 

## Other Data Operations

Data API instructions for the other data CRUD operations accompany this article's CRUD-related sibling articles.

## Operations Other Data-Related Entities

It's our goal to provide API instructions in the articles that demonstrate using entities such as datasets, sources, schedules, credentials, logs, and more. Those efforts are in progress.

## Using the Data API via an OAS Document

The [`/platform/swagger-json` endpoint](https://iexcloud.io/docs/datasets-api/get-openapi-json) returns a JSON file that specifies the [Datasets API](https://iexcloud.io/docs/datasets-api) per the OpenAPI Specification (OAS). You can generate a client SDK for your favorite language using the JSON file. 

## What's Next

A great way to learn the APIs is by following the API Reference's [Getting Started](https://iexcloud.io/docs/getting-started) guide and digesting the short articles that follow it. Then work with the data and data-related entities as demonstrated in the articles mentioned above.

---
[Go to Docs Home](https://github.com/iexcloud/docs/blob/main/README.md)