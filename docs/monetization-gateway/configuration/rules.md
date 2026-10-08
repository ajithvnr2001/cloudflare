---
url: https://developers.cloudflare.com/monetization-gateway/configuration/rules/
title: Monetization rules \u00b7 Cloudflare Monetization Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:21.676788+00:00
---

# Monetization rules · Cloudflare Monetization Gateway docs

> Source: https://developers.cloudflare.com/monetization-gateway/configuration/rules/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Monetization Gateway](https://developers.cloudflare.com/monetization-gateway/)
  3. /Configuration
  4. /Monetization rules



# Monetization rules

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/monetization-gateway/configuration/rules/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewChoose a pricing schemeEnter a priceSelect an audienceChoose HTTP methodsAdd conditions

Monetization rules determine which matching requests require payment. Each rule defines a domain, URL, price, and audience.

## Choose a pricing scheme

Choose a scheme based on when you determine the charge:

Scheme | x402 scheme | Behavior  
---|---|---  
Fixed | `exact` | Charges the same price for each request with fixed inputs. The gateway settles the signed amount.  
Variable | `upto` | Authorizes a maximum price. Your origin discloses and settles the actual amount.  
  
## Enter a price

Prices and settlements use atomic units. One atomic unit equals $0.000001.

Use these conversions when setting prices:

Amount | Atomic units  
---|---  
$0.001 | 1,000  
$0.01 | 10,000  
  
The minimum settlement amount is $0.001, or 1,000 atomic units. The maximum price is $100, or 100,000,000 atomic units.

## Select an audience

Choose which visitors the rule charges:

Audience | Behavior  
---|---  
Everyone | Charges all traffic matching the URL and advanced conditions.  
Verified Bots | Charges matching bots identified through [BotBase](https://developers.cloudflare.com/bots/botbase/).  
  
## Choose HTTP methods

By default, a rule charges `GET` requests. You can select multiple HTTP methods for one rule.

## Add conditions

Advanced conditions refine which requests the rule charges. You can match these request properties:

Property | Match input  
---|---  
Header | HTTP request header  
URI Query String | URL query string  
User Agent | User agent value  
X-Forwarded-For | `X-Forwarded-For` header value  
IP Source Address | Source IP address  
Continent | Request continent  
Country | Request country  
European Union | European Union location status  
Cookie Value | Request cookie value  
Body | Request body (Enterprise only)  
Body size | Request body size (Enterprise only)  
  
[Previousx402 protocol](https://developers.cloudflare.com/monetization-gateway/x402/)[NextPayment validation](https://developers.cloudflare.com/monetization-gateway/configuration/payment-validation/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/monetization-gateway/configuration/rules.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
