# Real-Time, Delayed, and Intraday Stock Prices

Here we'll describe the stock and equity market quotes IEX Cloud provides in real-time, at 15-minute delay, and intraday.

## Real-time and 15-minute delayed stock prices on IEX Cloud

IEX Cloud provides both real-time stock prices and 15-minute delayed stock prices during market trading hours for U.S. stocks and ETFs. You can access this data via the **Quote** and **Intraday Prices** endpoints.

Real-time prices are based on all trades that occur on the [Investors Exchange](https://iextrading.com/) (IEX). 15-minute delayed stock prices reflect activity from all U.S. exchanges, and is provided by the [Securities Information Processor / Consolidate Tape Association](https://www.ctaplan.com/index) (SIP).

While real-time prices for Nasdaq-listed stocks are available to all users, 15-minute delayed price data for Nasdaq-listed securities requires [UTP authorization](./getting-nasdaq-listed-utp-otc-stock-data.md). Learn more [here](https://iexcloud.io/disclaimers/).

Note that real-time prices available via the IEX Cloud API are different from real-time prices available via direct connection from IEX. [Learn more](https://iexcloud.io/disclaimers/).

## Using the Quote and Intraday Prices Endpoints

While there are several endpoints that provide stock price data on IEX Cloud in various formats, many users primarily use the **Quote** and **Intraday Prices** endpoints for current stock price data. Other endpoints that provide price data include Historical Prices, Delayed Quote, OHLC, Previous Day Price, and Price.

### Using the Quote Endpoint

Use the following fields on the **Quote** endpoint to access real-time stock prices:

**latestPrice**: The real-time price of a symbol, sourced from Investors Exchange (IEX) stock price data.

In the case of thinly traded securities – or securities traded less frequently – it’s possible that a symbol may not be traded on IEX within the most recent 15 minutes. In this case, since the IEX real-time price would be older than the 15-minute delayed SIP data, IEX Cloud will provide 15-minute delayed SIP data in this field.

Outside of trading hours, this field will provide the last available closing price. For details on accessing extended hours prices, refer to the bottom of this article.

**latestSource**: The source used to provide the price for the latestPrice field.

**iexRealtimePrice**: The real-time price for a stock, using the last trade on IEX.

**delayedPrice**: The 15-minute delayed price using SIP data. For Nasdaq-listed securities, this field and other delayed fields will be returned as null without [UTP authorization](./getting-nasdaq-listed-utp-otc-stock-data.md) and a paid IEX Cloud plan.

Additional information is provided via this endpoint. See a full list of **Quote** endpoint fields [here](https://iexcloud.io/docs/api/#quote).

### Using Intraday Prices Endpoint

You may also use the following fields on the **Intraday Prices** endpoint for the current trading day’s minute-by-minute price data:

**open**: IEX real-time data. First price during a given minute.

**close**: IEX real-time data. Last price during a given minute.

**high**: IEX real-time data. Highest price during the minute on IEX.

**low**: IEX real-time data. Lowest price during the minute on IEX.

The **average**, **volume**, **numberOfTrades**, and **notional** fields are also all sourced from trades on the Investor's Exchange. For thinly traded securities, it is possible there will be no trades in a given minute on the Investors Exchange, in which case those properties would be `null`.

The properties that begin with "market" are all based off 15-minute delayed market-wide prices from the SIP. During a trading day, these prices will populate with a 15-minute delay. For example, during a trading day at 10:00 a.m., you would see Investors Exchange real-time prices immediately for the 10:00 a.m. minute (assuming there are trades for that security on IEX in that minute). However, the market-wide properties for minutes 9:45 – 10:00 a.m. will be null. At 10:01 a.m., the 9:45 a.m. market-wide prices will be available, at 10:02 a.m., the 9:46 a.m. market-wide prices will be available, etc.

For a complete list of the endpoint fields, please see the [**Intraday Prices** API reference page](https://iexcloud.io/docs/api/#intraday-prices).

## OTC Stocks, ADRs, and Extended Market Hours Data

OTC stock 15-minute delayed prices are available through require a separate license agreement with OTC. Please reach out to support at <support@iexcloud.io> for more information.

``` {note} For legacy plan users, 15-minute delated OTC stock prices require an IEX Cloud legacy Business plan or legacy Scale plan, and a separate license agreement with OTC.
```

``` {note} OTC stock end-of-day historical prices are available with all paid plans.
```

ADRs listed in the U.S. are supported on IEX Cloud and have price data available in the same way as regular stock symbols.

Prices outside of market hours can be retrieved from the extendedPrice field from the **Quote** endpoint. These prices are 15-minute delayed, and cover the hours 4:00 a.m. E.T. – 9:30 a.m. E.T. and 4:00 p.m. E.T – 8:00 p.m. E.T. You can see a full list of data points returned for extended hours data in the [Quote endpoint’s API documentation](https://iexcloud.io/docs/api/#quote).

## Legacy Plan Cost for Stock Price Data

The **Quote** and **Intraday Prices** endpoints are available with free legacy plans, although specific fields – such as 15-minute delayed data – require a paid legacy plan. Without a paid legacy plan, those fields return `null`. For both legacy free and legacy paid users, the use of these endpoints requires credits (previously called messages).

Furthermore, 15-minute delayed price data for Nasdaq-listed securities also requires [UTP authorization](./getting-nasdaq-listed-utp-otc-stock-data.md). 

The **Quote** endpoint uses one credit per update per symbol. Similarly, the **Intraday Prices** endpoint uses one credit per update per symbol per interval – for instance, you might request minute-by-minute data for 30 minutes in one API call, which would use 30 credits.

The **Intraday Prices** endpoint only charges you a maximum of 50 credits per update per symbol if you are querying for multiple-minute time intervals. For instance, if you request 90 minutes of data, while this would be 60 intervals, you are charged only 50 credits.

Note that data provided by the Investors Exchange via the IEX Cloud API, including the real-time IEX prices, is free for use. You can access this using our [**TOPS** endpoint](https://iexcloud.io/docs/api/#tops) without using any credits. You can also apply the `chartIEXOnly` parameter to the **Intraday Prices** endpoint to access IEX-only minute-by-minute data from the current trading day free of charge.
