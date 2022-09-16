# Querying Datasets with iex.js

Use the [iexjs library](../../developer-tools/iexjs-library.md) `queryDataset` method to search any Apperate [dataset](../../reference/glossary.md#dataset) (Core or private) you have a [token](../../administration/access-and-security.md) for. 

## Example: Searching a Dataset 

Once you've installed the [iexjs](../../developer-tools/iexjs-library.md) package, call `queryDataset` passing the value of the `key` (primary) property you're searching results for.

For example, if you want Apple cash flow records, pass Apple's symbol `AAPL` as the the `key` value to search for in the `CASH_FLOW` dataset.

```javascript
const {Client} = require("@apperate/iexjs")
const client = new Client({api_token: TOKEN, version: VERSION});
client.platform.queryData({key: "AAPL", workspace: "CORE", id: "CASH_FLOW"}).then((res) => {
    console.log(res);
});
```

The `CASH_FLOW` dataset's `key` property is `symbol`. Like all Core datasets, the `CASH_FLOW` dataset is in the `CORE` workspace.

``` {tip} In the Console's Datasets sidebar, click on a dataset's name to expand a dataset's properties, revealing the properties mapped as *primary*, *secondary* (optional), and *date* indexes. Use the *primary* and *secondary* indexes as **key** and **subkey** parameters when calling the **queryData** method.
``` 

You can fine-tune your search by specifying additional [`GET /data`](https://iexcloud.io/docs/apperate-apis/get-data) query parameters.

For example, you can limit results to a particular time range using the `from` and `to` [`GET /data`](https://iexcloud.io/docs/apperate-apis/get-data) query parameters.

```javascript
client.platform.queryData({key: "AAPL", from: "2019-01-01", to: "2019-07-01", workspace: "CORE", id: "CASH_FLOW"}).then((res) => {
    console.log(res);
});
```

It's that easy to query datasets from your JavaScript apps!

## What's Next?

[iex.js Core Data Methods](../../developer-tools/iexjs-library/iexjs-core-data-methods.md) provides a reference to Core Data available for current plans and legacy plans.

[iex.js Apperate CRUD Methods](../../developer-tools/iexjs-library/iexjs-apperate-crud-methods) lists methods for invoking Apperate CRUD operations on data, datasets, and more.
