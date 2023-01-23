# Legacy Plan Credits and Pricing

``` {toctree}
:maxdepth: 1

legacy-plan-credits-and-pricing/legacy-plan-credits-and-sse-streaming.md
legacy-plan-credits-and-pricing/cloud-cache-for-legacy-plans.md
```

```{important} Here is information on credits and pricing for IEX Cloud legacy plans. For credits and pricing on current plans, see [Credits and Pricing](../credits-and-pricing.md).
```

<!--
```{note} On February 16, 2021, our the legacy Individual and Business plans replaced our legacy Launch, Grow, and Scale plans.
```
-->

## Legacy Individual Plans and Business Plans

Included with Individual plans ($9 per month with an annual subscription, or $19 per month with a monthly subscription):

- Five million credits (or messages) per month.
- One API token.
- One user login.
- Additional features, such as free access to [Cloud Cache](#cloud-cache). 
- Both commercial and personal use.

Included with Business plans ($199 per month with an annual subscription, or $299 per month with a monthly subscription):

- 150 million credits (or messages) per month.
- Four API tokens.
- Four user logins.
- Full feature access – everything included with Individual plus more. More detail coming soon.
- Both commercial and personal use.

Both plans provide the following:

- **Credits (previously called messages):** Use credits to make more API calls and request more data from IEX Cloud. 

- **Tokens:** [Tokens](../access-and-security.md) connect your project or application to your account. You can track, control, and throttle data usage by token. Examples of when you’ll use multiple tokens include using IEX Cloud to support multiple applications, projects, teams, or user accounts. For instance, if you support three applications, you would likely use a different token for each app. 

- **User logins:** Adding user logins to your plan adds room for more teammates to join your IEX Cloud account and use its data.

If you need to add more credits, API tokens, or user logins to your account, you can upgrade your plan or add packages.

## Credits in Legacy Plans

Credits are the fundamental units used to access data and make API calls on IEX Cloud legacy plans. Each API endpoint has a certain “data weight,” or a given number of credits that are used every time you make an API call with that endpoint. 

For example, the Earnings endpoint has a data weight of 1,000 credits per symbol per period. This means you would use 1,000 credits to see a company’s earnings for one specific quarter. 

Credits make your legacy subscription with IEX Cloud flexible and adjustable to your use case. You may use a higher volume of lower-weighted endpoints, fewer higher-weighted endpoints, or a combination. Note that certain endpoints are only available with paid legacy plans on IEX Cloud. 

The IEX Cloud Console [**Credits &rarr; Credit Use**](https://iexcloud.io/console/usage) tab automatically keeps track of how many credits you have used so far in the month. Check out our [legacy API documentation](https://iexcloud.io/docs/api) to see the data weights for different endpoints on IEX Cloud. 

### Why do different API endpoints use different numbers of credits?  

Data weights are determined by a number of factors, including agreements between IEX Cloud and our third-party data providers, the cost of sourcing the data further upstream, and other computational costs.  

Rather than requiring customers to pay for a preset selection of data in bulk, credits give you the flexibility to choose exactly the data you want to use with your subscription and how often you want to use it. IEX Cloud serves a diverse range of use cases and is designed to make data accessible for everyone.   

### How many credits do I need, and which plan should I choose? 

Each IEX Cloud legacy plan provides a different monthly allocation of credits, tokens for connecting your applications to your account, and user logins. The different plans also come with a designated set of tools and available datasets, which you can see on our pricing page.

You can choose your plan based on your use case:

- **The legacy Individual plan:** This plan is ideal for personal use, projects, students, building basic applications, testing, freelancers, and light use.
- **The legacy Business plan:** This plan allows for more scale and flexibility for growing technology companies and larger enterprises. With more credits, tokens, and user logins, it’s built to help growing businesses scale, bring flexibility to how firms build and make it easier to integrate IEX Cloud into your team’s workflow.

In addition to choosing your base plan, you can also further customize it by adding legacy packages. Packages add credits for more data usage, tokens for connecting more apps to your account, and user logins.

To help choose your plan and how many packages you need, it can be helpful to estimate how many credits you’ll need on a monthly basis. Once you know what data you would like to use on IEX Cloud, you can estimate your monthly credit usage by referencing those endpoints’ data weights in our documentation and multiplying that weighting by how frequently you will request this data.  

Our calculator [here](https://iexcloud.io/pricing/#pricing-slider) can help assist with a rough estimation. Alternatively, use the following formula as a guideline:  

*Data Weight x Number of Symbols x Frequency = Credit Use for that API Endpoint*

For example, let’s say you were looking to see the last three quarters’ earnings for a list of 5,000 companies. The Earnings endpoint uses 1,000 credits per symbol per period. 

Your credit usage for that endpoint would be: 

*(1,000 credits) x (5,000 symbols) x (3 periods) x (1 call per symbol) = 15,000,000 credits* 

### Core legacy credits vs. Pay-as-you-go Credits (For legacy Launch, Grow, and Scale plans only)

On our legacy plans, each IEX Cloud plan provides a different number of monthly core credits, as well as different pay-as-you-go credits.

Core credits represent the base number of credits included with your subscription each month. Core credits can be used towards any of the Core Data endpoints included with your plan. Your core credit usage is reset at the beginning of each calendar month.

Pay-as-you-go credits can be used in addition to your core credits as needed and are priced at a discounted rate. After you’ve used your core credits for a given month, you can use pay-as-you-go credits to continue accessing as much data as you need. With legacy Launch, Grow, and Scale plans, pay-as-you-go credits can also be used to access Premium Data — specialized datasets that can be added onto your subscription.

**It’s recommended that you enable the automatic use of pay-as-you-go credits in the IEX Cloud Console.** This setting helps prevent disruption in your service and allows IEX Cloud to default over to using pay-as-you-go credits after you have used all of your core credits for the month.

If you do not have the automatic use of pay-as-you-go credits enabled, IEX Cloud will pause access to data after you have used all of your core credits and will restore access at the beginning of the next month.

### Best practices for legacy credits

Make the most of your credits by checking out these IEX Cloud features: 

- **Cloud Cache – automatically enabled with Individual and Business plans:** More efficiently use your credits by storing and reusing the data that you’ve already requested from IEX Cloud. Let us handle the work for you with Cloud Cache. Cloud Cache is automatically included with Individual and Business plans. Learn more.
- **Packages (for Individual and Business plans only):** If you need more credits with your Individual and Business plans, you can simply add packages. Learn more about packages.
- **Pay-as-you-go credits (for legacy Launch, Grow, and Scale plans only):** Enable pay-as-you-go credits in the IEX Cloud Console. This ensures that you can continue to access data without interruption if you use all the core credits allocated with your subscription for the month.   

## Legacy Packages

Packages make it easier to customize your IEX Cloud plan according to your use case so that your plan scales with you as you grow. You can add packages as you need them throughout your legacy plan term.

Add packages to your plan to receive more of the following:

- **Credits (previously called messages)** – Included in packages for both legacy Individual and legacy Business plans: Use credits to make more API calls and request more data from IEX Cloud. 
- **Tokens** – Included in packages for Business plans: Tokens connect your project or application to your account. You can track, control, and throttle data usage by the token. Examples of when you’ll use multiple tokens include using IEX Cloud to support multiple applications, projects, teams, or user accounts. For instance, if you support three applications, you would likely use a different token for each app. Learn more about tokens.
- **User logins** – Included in packages for legaycy Business plans: The number of user logins on your plan refers to the number of seats you have for teammates to log into your IEX Cloud account. Adding user logins to your plan adds room for more people to join your IEX Cloud account and use its data.

You can both add and remove packages from your legacy plan as you need. Once you add a package, by default it will be added to your plan for each subsequent month. If you remove a package from your plan, it expires at the end of the current month. Packages can be removed or added month to month for both monthly and annual plans.

Packages cannot be added to free legacy Start plans or to legacy Launch, Grow, and Scale plans. To use packages, you must have the legacy Individual plan or legacy Business plan.

### What is included with each package?

Packages are different depending on your paid plan, and can only be added to legacy Individual plans or legacy Business plans.

**Legacy Individual plan** ($10 per month per package - for both monthly and annual plans) – each package includes every package adds:

- 10 million credits to your account.

**Legacy Business plan** ($30 per month per package - for both monthly and annual plans) – every package adds:

- 30 million credits.
- One token.
- One user login – or additional login for a teammate on your IEX Cloud account.

### How do I add more packages to my legacy plan, and when should I add them?

How many packages you need depends on how many credits, tokens, or seats for users you need. You can always add more packages to your plan as you go, or purchase multiple packages up front.

To add packages, go to [**Account &rarr; Manage Plan**](https://iexcloud.io/console/manage-plan) in the lower-left corner of the Console. You might add more packages if:

- **You need additional credits.** With the new pricing plans, we replaced pay-as-you-go overages with packages. If you approach your plan’s credit (or message) limits, you can either upgrade your plan or purchase additional packages. We will notify you via email when you reach your credit limits with instructions on how to add packages to your plan.
- **You need more tokens added to your account.** Depending on your use case, you may need additional tokens for your account. For instance, if you have multiple teams or applications, you will likely need multiple tokens for each of those teams or apps. 
- **You need to add more user logins to your account.** Maybe you’re expanding your team, or a new team at your business wants to join your IEX Cloud account to start a new project.

To see your current credit and plan usage, log into the IEX Cloud Console and go to [**Credits &rarr; Credit Use**](https://iexcloud.io/console/usage).

Packages are only available with the legacy Individual and Business plans, and cannot be added to legacy Launch, Grow, or Scale plans. If you already have a paid Launch, Grow, or Scale plan.

### How do overages work with the new plans?

IEX Cloud users on legacy Launch, Grow, or Scale plans will be familiar with the concept of pay-as-you-go messages (now pay-as-you-go credits). Instead of paying overages this way at the end of each month using pay-as-you-go credits, to use additional credits with these pricing plans, you’ll purchase packages.

We replaced overages with packages based on user feedback, with the goal of providing a simpler, more transparent way of scaling your plan with your usage.

If you reach your plan’s monthly credit limits, we will notify you via email with instructions on how to add packages to your plan. To prevent disruption, we suggest periodically checking your credit usage in the Console as well as purchasing packages in advance if you anticipate needing to use additional credits. When you reach your monthly credit limit, access to data will be temporarily paused until more credits are added to your plan or the next month begins.

### How are packages billed?

For both monthly and annual plans, packages are billed immediately upon purchase for the current month. They are then billed on the 1st{sup}`**` of each subsequent month. For instance, let’s say you purchase a package with your annual Business plan on the 16th. You’ll pay $30 upon purchase, and then $30 on the 1st of each subsequent month.
If you remove your package in the middle of a month, you’ll have it for the remainder of the month, after which it expires and you’ll no longer be charged for that package.

{sup}`**` IEX Cloud billing utilizes **Universal Time Coordinated (UTC)**. Renewals will occur at 00:00 UTC (08:00 PM EST). 

## Legacy Premium Data

IEX Cloud paid legacy plans include a breadth of data through a single easy-to-use API - ranging from simple stock prices for everyday investing to Premium Data for more specialized use. 

This guide provides more detail on how Premium Data differs from Core Data and how to get started. 

### Core Data vs. Premium Data

**Core Data** is the data included with IEX Cloud subscriptions. This includes any endpoints listed outside of the Premium Data section in our [Legacy API Reference](https://iexcloud.io/docs/api/), such as stock data, FX data, macroeconomic data, and more. The credits allocated with the IEX Cloud subscription can be used towards Core Data only. 

**Premium Data** is specialized data made available through the IEX Cloud API, sourced from various Data Partners directly. Premium Data consumption is on a pay-as-you-go basis using Premium Data credits, with different credit weights for each specific dataset. Premium Data is only included in paid IEX Cloud legacy subscriptions.  

Premium Data is available to customers with a paid legacy plan on IEX Cloud. 

### How do I start using Premium Data?

Follow the steps below to access Premium Data:

<!--
1. **Log into your paid IEX Cloud account.** If you're new to the platform or currently on a free plan, sign up for an Individual or Business plan to access Premium Data.
-->

1. **Add Premium Data credits to your account on the add-ons page.** Premium Data usage is purchased with [prepaid Premium Data credits](#prepaying-for-premium-data-with-premium-data-credits). 
1. **Request access to data on the Premium Data page of the IEX Cloud Console.** For many datasets, you'll be granted access right away. However, a couple requires partner approval and it could be a few business days before your access is activated. You can request access here.

    Once the Data Partner that provides that dataset confirms your request, it will be marked as “Enabled."  
1. **Start accessing data!** Your account will then be able to successfully make API requests to the dataset’s endpoints. You can start and stop using Premium Data at any time.  

**Be sure to check Premium Dataset endpoints’ data weights before use.** The endpoints for Premium Data and their weighting are documented in the [Legacy API Reference](https://iexcloud.io/docs/api/). 

Please note that each Data Partner has its own unique protocol for processing data access requests. You may be asked to complete a couple of extra steps or experience wait times when confirming access for different datasets.  

### Pricing for Premium Data on IEX Cloud

Premium Data is available **as an addition** to the Core Data already accessible through the IEX Cloud paid legacy subscriptions and uses Premium Data credits. For legacy Launch, Grow, and Scale plan users, it also uses pay-as-you-go credits. Credits included with the IEX Cloud subscriptions are used for Core Data and cannot be used towards Premium Data. 

Premium Data makes it easy to access a wider range of financial data and alternative data all in one place. Premium Data may be priced higher than other endpoints used as a part of the IEX Cloud Core Data offering, as it provides curated, specialized data sourced directly from other data creators.   

### How much data usage do I get with each dollar of Premium Data credits?

When you purchase Premium Data credits, you’ll notice that you purchase in dollar amounts. Our Premium Data endpoints, on the other hand, are priced in credits. For instance – you might purchase $50 worth of Premium Data credits, with the plan of using a Premium Data endpoint with a data weight of 100,000 credits per API call.

For our **Business and Individual legacy plans**, you purchase credits for Premium Data use at $1 per 1 million credits. For instance, $20 would provide 20,000,000 credits.

For our legacy plans, the dollar-to-credit conversion depends on your plan. Premium Data is charged at the cost of your pay-as-you-go credit rate:

- Launch: $1 per 1 million credits
- Grow: $1 per 2 million credits
- Scale: $1 per 3 million credits

### What is the monthly credit budget on Premium Data use? (Legacy Launch, Grow, and Scale plans only)

*Credit budgets are the same as message budgets.*

With legacy Launch, Grow, and Scale plans that use pay-as-you-go credits, IEX Cloud allows you to set customizable limits for the number of credits used on Premium Data per month. Credit budgets can be used to help maintain a cap on your credits consumption for the month or prevent accidental runaway use of Premium Data. 

**A default budget of 100,000,000 credits is set when you enable access to your first dataset.** When this limit is reached, access to Premium Data will be paused until the end of the month or until the limit is modified. You can change this limit at any time in the IEX Cloud Console. 

### Other Premium Data FAQs  

#### What Premium Data is currently available? 

You can see a full list of available Premium Data in the IEX Cloud Console under the Premium Data tab.

If there is certain data you would like to access that is not currently offered, please reach out to <support@iexcloud.io> with your request. Your feedback is essential to our future product roadmap.  

#### Can I test Premium Data with IEX Cloud's sandbox (deprecated)?
  
You can test Premium Data using IEX Cloud’s sandbox (deprecated), regardless of whether you have enabled access to that dataset. IEX Cloud’s sandbox provides scrambled test data and does not charge for any credits. 

## Prepaying for Premium Data with Premium Data Credits

Premium Data credits are a payment method on IEX Cloud where you purchase Premium Data usage upfront in bulk. You can choose how much you purchase in advance based on your anticipated usage of Premium Data, and add more Premium Data credits as you go.

For Individual and Business legacy plans, Premium Data credits are the only payment method for Premium Data.

For other legacy plans, you also have the option of using our legacy pay-as-you-go credits to purchase Premium Data. The legacy Launch, Grow, and Scale plans will allow you to use a certain number of pay-as-you-go credits every month for purchasing Premium Data. For usage beyond that amount, you will need to use prepaid Premium Data credits as your payment method. 

### How do I purchase Premium Data credits?

To view the Premium Data credits option, you must be logged in as an account admin. Navigate to the Add Ons tab of the [IEX Cloud Console](https://iexcloud.io/console/add-ons). You can select how much credit you would like to purchase, with a $20 minimum. There is no limit on how many Premium Data credit packages that can be purchased at a time. After you complete your purchase, Premium Data credits will be valid for one year.

Note that Premium Data credits are available for use after purchase beginning the first day of the upcoming month. For instance, if you purchased $200 worth of Premium Data credits on April 15th, 2020, this credit would be applied to your account and available starting May 1st, 2020 – the first day of the upcoming month – and would be available for use until May 1st, 2021.

Premium Data credits are available with IEX Cloud paid legacy plans only.

### How much data usage do I get with each dollar of Premium Data credits?

When you purchase Premium Data credits, you’ll notice that you purchase in dollar amounts. Our Premium Data endpoints, on the other hand, are priced in credits. For instance – you might purchase $50 worth of Premium Data credits, with the plan of using a Premium Data endpoint with a data weight of 100,000 credits per API call.

For our **Business and Individual legacy plans**, you purchase credits for Premium Data use at $1 per 1 million credits. For instance, $20 would provide 20,000,000 credits.

For our legacy plans, the dollar-to-credit conversion depends on your plan. Premium Data is charged at the cost of your pay-as-you-go credit rate:

- Launch: $1 per 1 million credits
- Grow: $1 per 2 million credits
- Scale: $1 per 3 million credits

### When can I apply my Premium Data credits?

Premium Data credits can be applied towards Premium Data only, and cannot be used towards your Core Data subscription or add-ons, except from widgets (deprecated). Premium Data credits can be used for up to 12 months from the time of purchase.

For instance, if you purchase Premium Data credits on March 1st, 2020, they will expire after March 1st, 2021. Note that unused credits cannot be returned as a refund.

### Where can I see how much credit I have remaining?

After you purchase Premium Data credits in the [Add Ons tab](https://iexcloud.io/console/add-ons), you can track how much credit you have remaining in the [Premium Data usage dashboard](https://iexcloud.io/console/usage).

### Premium Data credits vs. pay-as-you-go credits (For legacy Launch, Grow, and Scale plans only)

For our legacy Launch, Grow, and Scale plans, there are two methods for purchasing Premium Data: Premium Data credits and pay-as-you-go credits.

Premium Data credits can be used towards Premium Data only – credits can be purchased in advance in bulk, rather than paying for Premium Data as you use it. You can choose how much you would like to purchase upfront based on your expected usage of Premium Data. After purchasing Premium Data credits, that balance will be applied to your Premium Data usage for the next 12 months.

You can also pay for Premium Data as you need it using pay-as-you-go credits. Pay-as-you-go credit usage is billed at the end of each month. For each subscription tier, there is a limit for how many pay-as-you-go credits you can use in a month. Consuming credits beyond this monthly limit will require that you purchase prepaid premium data credits. Learn more about pay-as-you-go credits here.

### When do I need to use Premium Data credits? (For legacy Launch, Grow, and Scale plans only)

Depending on your plan and the amount of Premium Data usage, Premium Data credits may be the required payment method. For each subscription tier, there is a monthly limit on how many pay-as-you-go credits you can use for Premium Data. To continue using Premium Data after that limit, you will need to purchase Premium Data credits. Those pay-as-you-go limits are outlined below:

- Launch: 50 million pay-as-you-go credits per month (equivalent to $50 at $1/1 million credits)
- Grow: 100 million pay-as-you-go credits per month (equivalent to $50 at $1/2 million credits)
- Scale: 3 billion pay-as-you-go credits per month (equivalent to $1,000 at $1/3 million credits)

If you have not reached any of the limits above, and you use all your Premium Data credits, pay-as-you-go credits will automatically be used for additional Premium Data usage. If you want to prevent IEX Cloud from automatically using pay-as-you-go credits, you can enable a monthly credit budget. You can also purchase additional Premium Data Credits at any time.

## Caching Data in Legacy Plans

### Setting up your own caching

Legacy Individual and legacy Business plan users, as well as legacy Launch, Grow, and Scale subscribers are permitted to cache data on their own servers and can then display data from the cache to their users for commercial use.

Please note that you cannot provide IEX Cloud data via your own API to users or provide a mechanism for mass downloads, including a CSV download. Read more about acceptable usage of the platform in our [Terms of Service](https://iexcloud.io/terms/).

### Cloud Cache

Cloud Cache is IEX Cloud's fully managed data storage infrastructure. It saves you credits by automatically storing the data that you've already queried from IEX Cloud. When you request that data again, you'll only use one credit rather than the full data weight, so that you don't pay for the same data twice.

Note that any data stored by Cloud Cache is "reset" at the start of each calendar month. This is so we can keep our data storage as high-performant as possible. 

Cloud Cache is automatically enabled for all legacy Individual plan and legacy Business plan users – no setup or additional costs required.

``` {seealso} [Cloud Cache for Legacy Plans](./legacy-plan-credits-and-pricing/cloud-cache-for-legacy-plans.md).
```

## One Additional Credit Used Per API Call

Starting July 15, 2021, each API call uses one additional credit on top of the endpoint’s data weight.

For instance, if the data weight for an endpoint is 100 credits per request, each API call would use a total of 101 credits. Or if you’re using free real-time stock prices from IEX, you would use a total of one credit per API call.

If you’re streaming data, you would use one additional credit per connection.

This applies to all production API calls (API calls **not** made in our Sandbox environment).

### Why is one extra credit used per API call?

This one-credit covers our operational costs for delivering data and enables us to keep the costs lower across dozens of endpoints. This also allows us to continue investing in scalable infrastructure.

For most users, this adds minimal cost – a few cents to a few dollars per month in usage. For instance, if you make one million API calls per month, this update would add roughly $1 per month in credit usage.

### What about sandbox API calls?

``` {attention} The Sandbox environment is deprecated
```

Sandbox API calls are free and unlimited and do not use any of your monthly credit allocations.

Sandbox API calls can also be used to help show how many credits would be used if that same API call were performed in the production. You’ll see this one credit reflected in “sandbox data weight” that’s returned in the API request’s response header to help you accurately estimate how many credits you would use.

### Does this apply to Premium Data, Rules Engine, and other add-ons?

Every production API call across the platform will use one additional credit. This includes:

- Core Data and Reference Data.
- Premium Data. (The additional credit used will be a core credit, rather than a Premium Data credit.)
- Add-ons such as Rules Engines, the Excel plug-in, and Stock Price Widgets.
- API calls that use Cloud Cache. (link)

This does NOT include:

- Every SSE streaming or Firehose update. Streaming will use one additional credit per connection made – not per update.
- Sandbox API calls (deprecated).

### How does this work with Cloud Cache?

[Cloud Cache](./legacy-plan-credits-and-pricing/cloud-cache-for-legacy-plans.md) keeps track of the API calls you’ve already made, so if you make the same request twice, you only pay a data weight of one credit rather than the full data weight. 

This one credit is added **on top** of the one-credit data weight provided by Cloud Cache. So if Cloud Cache returned data to you for one credit, you would use two credits total.