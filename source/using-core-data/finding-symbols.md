# Finding Symbols

It's important to know what symbols are supported when making API calls to IEX Cloud. To see the full list of U.S. symbols that IEX Cloud currently supports for "stocks" API calls, you can make an API call to get the full symbols list from our reference data. 

```
https://cloud.iexapis.com/beta/ref-data/symbols?token=YOUR_TOKEN_HERE
```

This call will return an array of objects, each of which represents a symbol that can be used when making API calls. Here is an example of one of the objects for AAPL:

```javascript
{
    symbol: "AAPL",
    exchange: "NAS",
    name: "Apple Inc.",
    date: "2019-05-05",
    type: "cs",
    iexId: "IEX_4D48333344362D52",
    region: "US",
    currency: "USD",
    isEnabled: true
}
```

```{admonition} Legacy Plan Note
:class: note

The data weight for the reference data call is 100 credits. Credits were previously called *messages*.
```

The symbol field is the symbol that should be used when making API calls for prices, company info, and any other call under the [**Stocks** section](https://iexcloud.io/docs/api/#stocks) of the API reference.

The exchange lists the code for the symbol's primary listing exchange, in this case, "NAS" indicating AAPL is listed on the Nasdaq exchange. You can see the list of US exchanges by making [this reference data call](https://iexcloud.io/docs/api/#u-s-exchanges). You can see international exchanges by making [this reference data call](https://iexcloud.io/docs/api/#international-exchanges). 

```{admonition} Legacy Plan Note
:class: note

Both of the exchange reference data calls have a data weight of 1 credit per call.
```

The type for AAPL is "cs", indicating that it is a common stock. The currently supported issues types are:

- AD - ADR
- RE - REIT
- CE - Closed end fund
- SI - Secondary Issue
- LP - Limited Partnerships
- CS - Common Stock
- ET - ETF
- WT - Warrant
- OEF - Open Ended Fund
- CEF - Closed Ended Fund
- PS - Preferred Stock) 

The region for AAPL is "US" indicating that it is a U.S. based stock. The region property refers to the country code for the symbol using [ISO 3166-1 alpha-2 codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).

You can pull up the symbols only for a given exchange or region by using [this reference data call](https://iexcloud.io/docs/api/#international-symbols).

```{attention} **Reference Data** updates at 8 a.m., 9 a.m., 12 p.m., 1 p.m. UTC time every day. We recommend fetching updated reference data from IEX Cloud into your application regularly to stay up to date.
``` 

## IEX Symbols / Real Time Price For Symbols

To pull just the list of symbols that are traded on IEX, you would use [this reference data call](https://iexcloud.io/docs/api/#iex-symbols). 

## Mutual Fund Symbols

Reference data call to pull only mutual fund symbols can be found [here](https://iexcloud.io/docs/api/#mutual-fund-symbols).

 
## OTC Symbols

Reference data call to pull only OTC symbols can be found [here](https://iexcloud.io/docs/api/#otc-symbols).

## International Symbols

You can see which international exchanges IEX Cloud provides price data for at [Supported Exchanges](../reference/supported-exchanges.md).

To see the most up-to-date list of which international symbols are supported, you can use our reference data endpoints here to pull an array of symbols by region or exchange.

To use non-U.S. symbols, add the corresponding exchange suffix to the symbol when making the API call. For example, the exchange suffix for TSX is '-CV', so the symbol for Armor Minerals (TSX: A) is 'A-CV'.

Here is the quote call for A-CV:

```
https://cloud.iexapis.com/stable/stock/a-cv/quote?token=INSERT_TOKEN_HERE
```

You can find the suffixes for international exchanges by querying our [International Exchanges](https://iexcloud.io/docs/api/#international-exchanges) endpoint.