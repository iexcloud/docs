# iex.js JavaScript Library

```{toctree}
:maxdepth: 1

iexjs-library/iexjs-core-data-methods.md
iexjs-library/iexjs-apperate-crud-methods.md
```

iex.js (or simply *iexjs*) is a client library for getting data from Apperate and operating on Apperate resources, such as data, datasets, data sources, and more. The easy-to-use JavaScript methods wrap calls to IEX Cloud endpoints, so you can tap into Core Data, permissioned datasets, and Apperate resource CRUD operations.

## Installation

Use [npm](https://www.npmjs.com) to install iexjs.

```bash
npm install --save iexjs
```

``` {note} iexjs can also run in the browser via native *fetch* and *eventsource*, or from node via [cross-fetch](https://www.npmjs.com/package/cross-fetch) and [eventsource](https://github.com/EventSource/eventsource).
```

## Examples

The iexjs `Client` object stores your [API token](../administration/access-and-security.md) (API key) and IEX Cloud API version (e.g., `v1`) for convenience.

``` {tip} The iexjs client automatically picks up tokens from the environment variable *IEX_TOKEN*.
```

Here are some examples.

**Get a real-time stock quote:**

```javascript
const {Client} = require("@apperate/iexjs")
const client = new Client({api_token: "TOKEN", version: "VERSION"});
client.quote({symbol: "AAPL"}).then((res) => {
    console.log(res);
});
```

``` {seealso} [iex.js Core Data Methods](./iexjs-library/iexjs-core-data-methods.md) has information on all the methods.
```

**Get Apple's latest cash flow details:**

```javascript
const {Client} = require("@apperate/iexjs")
const client = new Client({api_token: "TOKEN", version: "VERSION"});
client.apperate.queryData({key: "AAPL", workspace: "CORE", id: "CASH_FLOW"}).then((res) => {
    console.log(res);
});
```

The client's `apperate` object (shown above) has wrapper methods to [Apperate APIs](https://iexcloud.io/docs/apperate-apis/), including the [Data API](https://iexcloud.io/docs/apperate-apis/data/). The `queryData` method retrieves data from a dataset via the dataset `id`. You can retrieve data from a `CORE` dataset or any workspace dataset you have access to.

``` {seealso} [Querying Datasets with iex.js](../interacting-with-your-data/querying-data/querying-datasets-with-iexjs.md) provides details on searching datasets.
```

## Open Source Project

The iex.js package is an open source project available at <https://www.npmjs.com/package/@apperate/iexjs>.

## What's Next

[Querying Datasets with iex.js](../interacting-with-your-data/querying-data/querying-datasets-with-iexjs.md) demonstrates getting data from private permissioned datasets (e.g., your datasets).

[iex.js Core Data Methods](./iexjs-library/iexjs-core-data-methods.md) provides a reference to Core Data available for current plans and legacy plans.

[iex.js Apperate CRUD Methods](./iexjs-library/iexjs-apperate-crud-methods) lists methods for invoking Apperate CRUD operations on data, datasets, and more.