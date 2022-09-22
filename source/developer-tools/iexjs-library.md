# iex.js JavaScript Library

```{toctree}
:maxdepth: 1

iexjs-library/iexjs-core-data-methods.md
iexjs-library/iexjs-apperate-crud-methods.md
```

iex.js (or simply *iexjs*) is a client library for getting IEX Cloud Core Data and getting data from private permissioned datasets. The library also provides methods for performing CRUD operations on Apperate resources, such as dataset data, datasets, data sources, and more. iexjs provides easy-to-use JavaScript wrapper methods that call IEX Cloud endpoints.

## Installation

Use [npm](https://www.npmjs.com) to install iexjs.

```bash
npm install --save iexjs
```

iexjs can run in the browser via native `fetch` and `eventsource`, or from node via [cross-fetch](https://www.npmjs.com/package/cross-fetch) and [eventsource](https://github.com/EventSource/eventsource).

## Examples

The iexjs `Client` object stores your [token](../administration/access-and-security.md) (API key) and IEX Cloud API version (e.g., `v1`) for convenience. From the client's`platform` object, you can execute iexjs methods. Here are some examples.

Get a real-time stock quote:

```javascript
const {Client} = require("@apperate/iexjs")
const client = new Client({api_token: TOKEN, version: VERSION});
client.quote({symbol: "AAPL"}).then((res) => {
    console.log(res);
});
```

``` {seealso} [iex.js Core Data Methods](./iexjs-library/iexjs-core-data-methods.md) has information on all the methods.
```

Get Apple's latest cash flow details:

```javascript
const {Client} = require("@apperate/iexjs")
const client = new Client({api_token: TOKEN, version: VERSION});
client.platform.queryData({key: "AAPL", workspace: "CORE", id: "CASH_FLOW"}).then((res) => {
    console.log(res);
});
```

The `queryData` method retrieves data from the dataset your specify via the `id`. You can use it to retrieve data from the `CORE` workspace or any other workspace you have access to.

``` {tip} The iexjs client automatically picks up tokens from the environment variable *IEX_TOKEN*.
```

``` {seealso} [Querying Datasets with iex.js](../interacting-with-your-data/querying-data/querying-datasets-with-iexjs.md) provides details on searching datasets.
```

## Open Source Project

The iex.js package is an open source project available at <https://www.npmjs.com/package/@apperate/iexjs>.

## What's Next

[Querying Datasets with iex.js](../interacting-with-your-data/querying-data/querying-datasets-with-iexjs.md) demonstrates reading data from private permissioned datasets (e.g., your datasets).

[iex.js Core Data Methods](./iexjs-library/iexjs-core-data-methods.md) provides a reference to Core Data available for current plans and legacy plans.

[iex.js Apperate CRUD Methods](./iexjs-library/iexjs-apperate-crud-methods) lists methods for invoking Apperate CRUD operations on data, datasets, and more.