# Get Nasdaq-listed Stock Data (UTP/OTC Data)

Here is an overview of how to get 15-minute delayed market-wide intraday prices for Nasdaq-listed stocks

For Nasdaq-listed stocks only, certain data is only available through IEX Cloud if you are authorized by UTP directly, and also are under a paid plan with IEX Cloud. 

This does **not** mean that *all* data regarding Nasdaq-listed stocks requires special authorization. Authorization is only required for specific fields that use Nasdaq-listed stocks’ 15-minute delayed prices from UTP. IEX Cloud has a large amount of data regarding Nasdaq-listed stocks that are available regardless of whether you have UTP authorization.

If you do require authorization for the data you need, you are required to fill out Nasdaq UTP’s forms and pay applicable fees. You can find details on how to do so below.

## Why do I need to pay for Nasdaq UTP data? 

While Investors Exchange data is free and unlimited, IEX Cloud also provides access to data from many other sources – such as UTP data for Nasdaq-listed stocks. Nasdaq UTP is the only source and owner of this data, and as a result, is able to dictate the price and terms of its use. IEX Cloud, as well as our customers, are therefore required to abide by these terms.

IEX Cloud continues to work every day to make financial data easy to use for every developer and investor. Thank you for continuing to support our mission of setting new standards inaccessibility of financial data.

## What data on IEX Cloud requires UTP authorization?  

Authorization is required for several fields on the **"Quote” endpoint**, **"Intraday Prices” endpoint**, and **"OHLC” endpoint**.

For Nasdaq-listed symbols ONLY, if you do NOT have UTP authorization, you will encounter the following:

**"Quote”:** `open`, `openTime`, `close`, `closeTime`, `delayedPrice`, `delayedPriceTime`,`extendedPrice`, `extendedPriceTime`, `extendedChange`, `extendedChangePercent`, `week52High`, `week52Low`, `high`, `low` will not be returned.

 **"Quote”:** `latestPrice`, `latestUpdate`, `latestTime`, `latestSource`, `change`, `changePercent`, `marketCap`, `ytdChange` do not incorporate Nasdaq UTP data but use Investors Exchange data. 

**“OHLC”:** all fields will not be returned. 

**“Intraday Prices”:** all fields prefixed with **"market”** will not be returned. 

**SSE Streaming:** If you do not have UTP authorization, SSE streaming for US stocks is still available - you will need to modify your syntax, as shown in our [API Reference](https://iexcloud.io/docs/api/#streaming-data).

## What kind of price-related data can I get through IEX Cloud without requiring UTP authorization? 

If you need to pull out price-related data on a Nasdaq-listed stock, you may not necessarily require Nasdaq UTP data specifically.

Since Nasdaq-listed stocks trade across all exchanges, and not just Nasdaq, IEX Cloud also provides data on prices for Nasdaq-listed stocks according to the most recent trade made on Investors Exchange. 

1. **For “Quote” data:** As described above, if you don’t have UTP authorization, IEX Cloud will automatically use the latest trade seen on Investors Exchange to populate the Quote fields `latestPrice`, `latestTime`, `latestUpdate`, `change`, `changePercent`, `marketCap`, and `vtdChange`. 

1. **For “OHLC” data:** IEX Cloud is able to provide historical official open, close, high, and low data through our “Previous Day Price” and "Historical Prices" endpoints. This data is generally available for the current day around 11:30 PM ET (though the exact timing is dependent on our primary data provider). The official open and close for Nasdaq listed securities earlier in the day requires UTP authorization. As another approach for open and close without UTP data, you can also find the first and last trade prices that occurred on Investors Exchange on the Intraday-Prices endpoint for the current day.

1. **For “Intraday-prices” data:** Non-delayed intraday prices that are based on trades on the Investors Exchange are available for the current day regardless of whether you have UTP authorization. Market-wide 15-minute delayed intraday prices require UTP authorization (these are provided via any fields with “market” as a prefix).

## How do I get UTP authorization?

If you wish to access delayed UTP data via IEX Cloud, you must submit the following documents to UTP and pay the applicable fees:

- Submit a [Vendor Agreement](https://www.utpplan.com/DOC/VendorAgreement.pdf).
- Submit a Data Feed Request Form: [Online](http://www.utpplan.com/datafeed_approval) or Hard Copy.

    - For “Data Provider," select “IEX Cloud Services LLC”.
    - For “Account Number or Datafeed Location with Datafeed Provider.” Provide your IEX Cloud Account ID. This can be found by logging into the IEX Cloud Console, clicking the “Support” tab, and providing the value for “Account No.”

- Submit a System Description: [Online](http://www.utpplan.com/system_application) or Hard Copy

If you have questions about these forms, please contact UTP directly at <admin@utpplan.com>.  When you are approved to receive Nasdaq UTP data, Nasdaq UTP will alert IEX Cloud, at which point access to Nasdaq UTP data via IEX Cloud can be enabled. 

## I already have a UTP vendor agreement – how can I get that data through IEX Cloud?

If you already have a UTP authorization agreement and would like to receive delayed UTP data via IEX Cloud:

- Submit a [Vendor Agreement](http://www.utpplan.com/DOC/VendorAgreement.pdf).
- Submit a Data Feed Request Form: [Online](http://www.utpplan.com/datafeed_approval) or Hard Copy.

    - For “Data Provider," select “IEX Cloud Services LLC”.
    - For “Account Number or Datafeed Location with Datafeed Provider.” Provide your IEX Cloud Account ID. This can be found by logging into the IEX Cloud Console, clicking the “Support” tab, and providing the value for “Account No.”

After completing this, please notify IEX Cloud through <support@iexcloud.io>.
