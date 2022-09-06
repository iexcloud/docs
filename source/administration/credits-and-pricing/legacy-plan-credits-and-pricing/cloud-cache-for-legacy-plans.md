# Cloud Cache for Legacy Plans

If you have a legacy Individual plan or legacy Business plan, and you query the same API for data which has not changed, your cost is reduced to 1 credit per record thanks to Cloud Cache. This complimentary feature keeps track of every API call you make and helps you avoid paying for the same data twice.

If you make the same API call more than once within the same calendar month, and the data hasn't changed, it’s served to you with **a data weight of only one credit** – regardless of what the full data weight is. (Note that Cloud Cache cannot be used with [files](https://iexcloud.io/console/files).) When you signed up for an Individual or a Business plan, Cloud Cache was automatically enabled for no additional charge. That means you can use our API without worrying about whether the data has changed or not, so you can code faster and spend less time focused on complicated data infrastructure.

Cloud Cache is cleared at the start of each calendar month. That means if you re-pull the same data point across different calendar months, that data will be re-pulled from our API as normal using the full data weights. 

## How it Works


Full credit amount is charged only when data is not available in Cloud Cache or the data has changed, and so is fetched from the Cloud API. Each request that is available in Cloud Cache applies a credit weight of 1 for each unit, as opposed to an endpoint's per unit weighting, as shown in the endpoint's API reference page.

Batch queries count as 1 cache slot per symbol + type combination.

## Cloud Cache Examples

### Caching Estimate Data for AAPL

**Initial Call:**

Estimate is requested: `https://cloud.iexapis.com/v1/stock/aapl/estimate?token={YOUR_TOKEN}`
- `10,000` credits are used
- `1` cache slot is used to store the data

**Future Call (in the same calendar month):**

- Estimate is requested
- Data is found in Cloud Cache
- `1` credit is used

### Batch Call

**Initial Batch Call:**

Batch Request for AAPL and BAC last quarterly earnings and financials: `https://cloud.iexapis.com/v1/stock/market/batch?symbols=AAPL,BAC&types=financials,earnings&token={YOUR_TOKEN}`

- `12,000` credits are used
- `4` cache slots are used to store the data

**Future Batch Call (in the same calendar month):**

Last quarterly earnings and financials are requested for AAPL, BAC, and FB: `https://cloud.iexapis.com/v1/stock/market/batch?symbols=AAPL,BAC,FB&types=financials,earnings&token={YOUR_TOKEN}`

- Data is found in Cloud Cache for AAPL, and BAC. Most recent quarterly earnings and financial for FB pulled from Cloud API.
- `2` credits are used for data fetched from Cache.
- `6,000` credits are used for FB data pulled from API.
- `2` more cache slots are used to store FB earnings and financials

## How much data can you store?

Whether you make 100 API requests or 100,000, we’ll keep track of the requests you've already made. There’s no limit. However, Cloud Cache resets at the start of each calendar month. This means that if you make an API call in June that you had already made in May, even if the data has changed, you will use the full credit amount in June.

If you want to go beyond this to save data for a longer period, you can also always build your own caching system.