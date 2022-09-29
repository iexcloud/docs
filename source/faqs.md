# FAQs

Here are some frequently asked questions (FAQs) about IEX Cloud.

## Account, Billing, and Pricing

<details><summary>How do Apperate credits work with Core Data?</summary>

Core Data is available as a separate workspace within Apperate and separated into datasets. You can access any dataset from Apperate or through the legacy API using standard database operation pricing.

How many credits you'll use to pull data can be predicted based on:

- **How many records you query** – at a rate of 0.000001 credits per record (another way to look at it, is 1M records per credit)
- **The size of data transferred out** – Each credit gets you 10GB of data transfer. 

Add those two together, and that's your total credit usage for accessing data. If you're a legacy user, you might be used to "data weights" – for simplicity, we've eliminated those for Apperate users.

```{note} **All Core Data resides in Apperate without any storage cost** – so rather than storing Core Data in your own database (and paying for it), you can query it directly.
```

```{seealso} [Credits and Pricing](./administration/credits-and-pricing.md) explains how you simply pay for what you use.
```
</details>

<details><summary>How can I make changes to my plan?</summary>

You can request upgrading, downgrading, or cancelling your subscription at any time via the console's [Manage Plan](https://iexcloud.io/console/manage-plan) page.
</details>

<details><summary>When do plan upgrades take affect?</summary>

When you upgrade your plan, the new subscription goes into effect immediately.
</details>

<details><summary>How many tokens do I need?</summary>

You may want to use separate tokens to track, control, and throttle usage by different projects, apps, or end users. Here are a couple examples for using multiple tokens:

- you have multiple applications or projects that use IEX Cloud.
- your business has multiple teams that share your IEX Cloud account.

``` {seealso} [Access and Security](./administration/access-and-security.md).
```
</details>

<details><summary>What are allowed domains?</summary>

You may restrict individual tokens to certain domains. Leaving the domain blank will allow requests with the token to come from any domain. If you do specity a domain(s), this value must match the HTTP header referer in your requests.

</details>

<details><summary>When do plan downgrades take affect?</summary>

We don't provide prorated refunds for downgrades or cancellations. When you downgrade or cancel, you will remain on your higher-tier subscription through the end of your current term. You can see your current term's next renewal date in the console's [Billing](https://iexcloud.io/console/billing) section. Once your next renewal date comes around, you will automatically be placed on your downgraded subscription. 
</details>

<details><summary>I have a legacy plan; do I have to change anything?</summary>

If you don't want to use any of the new Apperate features, you can continue using IEX Cloud as you do today. You don't need to make any changes.
</details>

<details><summary>Compared to legacy plans, how is Apperate billing different?</summary>

Apperate is a fully-managed cloud database with integrated data services. Much like other serverless cloud databases, you pay for using the system. We track usage of the system using credits. Here's what usage includes:

- Standard database operations (reads, writes, and updates) – for any data. IEX Cloud Core Data **or** your own data.
- Storage of your own data.

```{note} Apperate credits are displayed in smaller units. A credit is represented as 1/1,000,000th smaller than in the past. For example, 100 credits is now represented as 0.0001.
```

The bonuses with Apperate are:

- You **don’t** pay for the storage of Core Data in Apperate – so you essentially get a database that is preloaded with 5TB of financial data without any work (something you wouldn’t get with any other cloud database).
- You query using standard SQL, build views, run transforms and perform joins within Apperate and access the data with our standard API or our new data management UI. Now you don't have to ETL data from IEX Cloud into another database.

```{seealso} [Credits and Pricing](./administration/credits-and-pricing.md) explains how you simply pay for what you use.
```
</details>

<details><summary>(Legacy) Can I add or remove packages on my legacy plan?</summary>

You can both add and remove packages from a legacy plan as needed. Once you add a package, by default, it will be added to your plan for each subsequent month. If you remove a package from your plan, it expires at the end of the current month. Packages can be removed or added month to month for any paid legacy plan.
</details>


## Data

<details><summary>What usage restrictions and requirements do the various plans have?</summary>

Users on the Start Plan (legacy) are only permitted to use data from IEX Cloud for personal, non-commercial use. Paid plan users can use IEX Cloud data for commercial use, including displaying publicly to users.

No user may provide IEX Cloud data via their own API to users, or provide a mechanism for mass downloads, for example as a CSV. For more information please see our terms of service.

Attribution is required for all users. It is as simple as putting “Data provided by IEX Cloud” somewhere on your site or app and linking that text to <https://iexcloud.io>.
</details>

<details><summary>Why does Apperate report "cannot select by 'columnXYZ' (00ED50F1BF0332)" even though the column is valid?</summary> 

You can only select on indexed properties (columns). A property must be a primary, secondary, or date index (See [Unique Index components](./managing-your-data/understanding-datasets.md#indexing-with-unique-index)) to query on it via SQL `WHERE` clauses, SQL `JOIN` `ON` clauses, or via the data query endpoint key/subkey path parameters.
</details>

<details><summary>How do I get data on the S&P 500, Dow Jones Industrial Average, or other major stock indices?</summary>

Data on major stock indices is not currently available on IEX Cloud

Data on the S&P 500, Dow Jones Industrial Average, and other major stock indices is not currently available on IEX Cloud and is unlikely to be in the near future.

Pricing for this data is typically high and requires a direct contract between each consumer and the index provider regardless of who actually supplies the data. For instance, the major index providers charge over $10,000 a year for delayed data.

An alternative is to display ETFs that match those indices, such as SPY for the S&P 500, DIA for Dow Jones, and IWM for Russell 2000.
</details>

<details><summary>How do I grant API access to only specific domains?</summary>

Please see [Restricting Data Access to Specific Domains](./administration/access-and-security/restricting-data-access-to-specific-domains.md).
</details>

<details><summary>How do I get Nasdaq-listed stock data (UTP/OTC Data) on IEX Cloud?</summary>

Please see [Get Nasdaq-listed UTP/OTC Stock Data](./using-core-data/getting-nasdaq-listed-utp-otc-stock-data.md).
</details>

<details><summary>How do I stream in data?</summary>

Please see [Stream Data Using SSE](using-core-data/streaming-data-using-sse.md).
</details>

<details><summary>(Legacy) How do I enable access to earnings and estimates Data?</summary>

There is global coverage of earnings and estimates data. Due to this third-party provider terms of use, however, the data requires additional entitlements and in certain scenarios must be accessed from the data partner directly. Affected endpoints include:

- [Estimates](https://iexcloud.io/docs/api/#estimates)
- [Earnings](https://iexcloud.io/docs/api/#earnings)
- [Earnings Today](https://iexcloud.io/docs/api/#earnings-today)
- [Price Target](https://iexcloud.io/docs/api/#price-target)
- [Analyst Recommendations](https://iexcloud.io/docs/api/#analyst-recommendations)

**If you are planning on using this data for personal or internal use only** – with no redistribution or redisplay – simply follow the instructions below to access this data.

These endpoints will be included in the Marketplace section for entitlement purposes. All usage will use pay-as-you-go credits (legacy) or Premium Data credits, but the data weights and endpoint URLs will remain unchanged.

**If you would like to redistribute this data**, such as redisplaying data on a public-facing website or application, you will need to negotiate an agreement directly with our data partner. Please reach out to our partnerships team at <partners@iexcloud.io> if you would like us to make that introduction.

**Here’s how the entitlement process works:**

Head to the [Marketplace tab in the IEX Cloud Console](https://iexcloud.io/console/marketplace) and request access to “Earnings, Estimates, Price Targets, and Analyst Recommendations.”

You will be asked to provide basic information about who you are and how you will be using the data. Once approved, you will be able to use these endpoints. Access requests will typically be reviewed in 1-2 business days. Our team will reach out if we need additional information.

The number of credits per API call is not changing. However, API calls for these endpoints will use pay-as-you-go credits (legacy) or Premium Data credits, rather than the core credits included with your plan. This means that usage of these endpoints will be billed each month in addition to your base subscription charges.

Questions? Reach out to <support@iexcloud.io> for assistance.
</details>


## General

<details><summary>Can I redisplay/ redistribute the data I receive from IEX Cloud?</summary>

In general, displaying IEX Cloud data is permitted with attribution. The following are some restrictions on the use of IEX Cloud data:

- Users on the Start or Free plan are only permitted to use data from IEX Cloud for personal, non-commercial use. You can still display data to other individuals/users, but you may not include our data in any commercial application. Paid plan users can use IEX Cloud data for commercial use, including displaying publicly to users.
- No user may provide IEX Cloud data via their own API to users, or provide a mechanism for mass downloads, for example as a CSV. For more information please see our terms of service.
- Attribution is required for all users. If a customer distributes IEX Cloud Data, they must state that the data was provided by IEX Cloud and provide a hyperlink to <https://iexcloud.io>.

For more information, please see the **Acceptable Use Policy** within our [Terms](https://iexcloud.io/terms/#aup).
</details>
