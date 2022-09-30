# Restricting Data Access to Specific Domains

You can give specific domains and IP addresses access to your dataset APIs by specifying those domains in a given publishable API Token.

All IEX Cloud users can restrict calls made to IEX Cloud with a publishable API token to only those calls that have an [HTTP referer header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer) that matches one of the token's **Allowed Domains** values.

``` {note} The HTTP referer header is a result of a misspelling of the word "referrer" that has now become part of the HTTP standard
``` 

Here's how to specify a restriction on a publishable key.

1. Navigate to [API Tokens](https://iexcloud.io/console/tokens) in the Console.

1. Click the Manage button next to the API key (token) you want to set restrictions for. The **Token settings** page appears for that token.

1. In the **Allowed Domains** field, enter the domain and/or IP address values where you want to allow requests from.

1. When you're done entering allowed domain values, click **Done**. The restriction goes into effect in about 30 seconds.

Now requests that use the token must have an [HTTP header referer](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer) value that matches one of the **Allowed Domains** values.

``` {note} On the **Token settings** page, Business plan users and legacy Grow and Scale users can enable [signed requests](https://iexcloud.io/docs/account/signed-request).
```

## Single Domain Restrictions

A domain restriction can be a URL or an actual IP address. The form checks each domain restriction to ensure it is a valid input. If any of the inputted domain restrictions are not valid you will not be able to hit the “Update domain” button to update the restriction.

### Path Restrictions

Any domain restriction automatically appends a wildcard (“*”) to the end of the domain that allows the referer to include anything in the path following the restriction. So, for example, if you put in a restriction of ‘www.example.com’, all these HTTP referers would be considered valid requests:  

`http://www.example.com/`

`http://www.example.com/app`

`http://www.example.com/app/user/1`

`http//www.example.com/app/stock`

If you want to further restrict the path, you can update your restriction to a longer path. So, if you set the domain restriction to `www.example.com/app/stock`, then these would be valid referers: 

`https://www.example/com/app/stock`

`https://www.example/com/app/stock/AAPL`

while these would not be valid referers under the restriction ‘www.example.com/app/stock’: 

`http://www.example.com/`

`http://www.example.com/app`

### Protocol Restrictions (HTTP v. HTTPS)

If you don't specify a protocol then we will automatically allow for referers with both the HTTPS and HTTP protocol. If you wanted to specify only HTTPS you should include it in the restriction like so - `https://www.example.com`. Under this restriction, `https://www.example.com/stock` would be a valid referer, while `http://www.example.com/stock` would NOT be a valid referer.

### Allowing multiple subdomains 

You can append a wildcard `*` character at the beginning of restrictions to allow for multiple subdomains. So, for example, if you have a restriction of `https://*.example.com`, then the following would all be valid referers: 


`https://www.example.com`

`https://dev.example.com`

`https://app.example.com`

## Multiple Domain Restrictions 

To set multiple domain restrictions simply separate each one with a single space. So, for example, if I set a restriction of 
`www.mysite.com *.example.com`, it would allow requests with referers such as: 

`www.mysite.com/app`

`app.example.com/user`

As the example demonstrates, when multiple restrictions are set, any referer that is valid under any of the constraints will be considered valid

## Limitations 

Please note that while restricting the HTTP referer does provide a layer of security, someone could make a request with your token and spoof the referer header.  

Users who want a more robust security feature may want to utilize [signed requests](https://iexcloud.io/docs/account/signed-request).