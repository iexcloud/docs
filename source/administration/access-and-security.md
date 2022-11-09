# Access and Security

```{toctree}
:maxdepth: 1

access-and-security/restricting-data-access-to-specific-domains.md
```

You connect your application or project to your IEX Cloud account via API tokens (also referred to simplay as tokens). Tokens allow you to track, control, and throttle platform usage. You can grant users access to datasets by giving them public API tokens. 

``` {warning} Your secret token allows you to perform any action on your data and account. **NEVER** share your secret token publicly.
```

## Creating an API Token

Here's how to create and use a public API token.

1. Navigate to **Access & Security &rarr; API Tokens**. The API Tokens page appears, listing your tokens in order, oldest to newest.

1. Click **Create new token**. A dialog window appears and asks if you are sure you want to add a publishable token.
    
    ![add-token-dialog.png](./access-and-security/add-token-dialog.png)

    ``` {note} Publishable tokens have Core dataset read access by default.
    ```
    
1. Click **Add publishable token**. A new publishable token is added to the bottom of the token list.
    
    ![token-added.png](./access-and-security/token-added.png)
    
1. Edit the token by finding it at the bottom of the token list and clicking on its gear icon or on its token ID. The API token form appears.

1. Define the token. 
    
    **Nickname:** Enter a meaningful name.

    **Signed Requests:** Enables requiring a signature per request. For legacy plans, Business plan users and legacy Grow and Scale users can enable [signed requests](https://iexcloud.io/docs/api/#signed-requests).

    **Core Data Access:** Core dataset read access is granted by default. You can alternatively revoke this access.

    **Premium Data Access:** Grants access to Premium Data (requires Premium Data subscription)

    **Dataset permissions:** Grants read/write/delete access to specified datasets.

    **Allowed Domain(s):** Leaving blank allows requests with the token from any domain. Specifying a domain(s) limits requests to be from that domain(s). Read more at [Restrict Data Access to Specific Domains](./access-and-security/restricting-data-access-to-specific-domains.md).

    **Core Credit Usage Limit:** Restricts the number of core credits available to the token.
    
    The token below, for example, can access Core Data and Premium Data, and has read access to three datasets.
    
    ![api-token.png](./access-and-security/api-token.png)

1. When you're done specifying the token, click **Done**. The token's permissions take affect in a couple minutes. Then you can make the specified API calls using the token.

``` {note} A token's permissions take affect a couple minutes after creating the token.
```

Now the token can be used in calling the specified APIs.

## How many tokens do I need?

Depending on your use case, you may want to use multiple tokens rather than just one. You’ll typically want to use multiple tokens when tracking, controlling, and throttling usage for different projects, apps, or end users separately.

Reasons to use multiple tokens:

- You have multiple applications or projects using IEX Cloud
- Multiple teams at your business are sharing your IEX Cloud account

## What's Next?

Ready to call some dataset APIs? See [Get Started with Apperate](../getting-started/getting-started-with-apperate.md).

Want to get your teammates involved? Learn how to add teammates at [Manage Users](./managing-users.md).