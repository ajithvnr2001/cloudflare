---
url: https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/verify-ai-crawler/
title: Verify your AI crawler \u00b7 Cloudflare AI Crawl Control docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:26.696190+00:00
---

# Verify your AI crawler · Cloudflare AI Crawl Control docs

> Source: https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/verify-ai-crawler/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)
  3. /…

FeaturesPay Per Crawl

  4. /Use pay per crawl as an AI owner
  5. /Verify your AI crawler



# Verify your AI crawler

Last updated Jul 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/verify-ai-crawler/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewContent access restriction1\. Follow Web Bot Auth protocol2\. Follow verified bot policy3\. Submit verification request
    
    
    graph LR
    A[Set up your<br>Cloudflare Account] --> B[Verify your<br>AI crawler]:::highlight
    B --> C[Discover<br>payable content]
    C --> D[Connect to<br>Stripe]
    D --> E[Crawl pages]
    classDef highlight fill:#F6821F,color:white
    

Once you have connected your Stripe account, set up your AI crawler as a [verified bot](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/).

## Content access restriction

When an AI crawler tries to access content protected by pay per crawl, it receives a HTTP status code 402. This indicates payment is required. The HTTP header of the response includes the cost of the content.

For example, the response header may look like below:
    
    
    HTTP/2 402
    date: Fri, 06 Jun 2025 08:42:38 GMT
    content-type: text/plain; charset=utf-8
    crawler-price: USD 0.01
    server: cloudflare

To access this content, you must verify your AI crawler.

## 1\. Follow Web Bot Auth protocol

Ensure your AI crawler identifies itself with the required headers for Web Bot Auth.

Follow the steps found in [Web Both Auth](https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/).

## 2\. Follow verified bot policy

Ensure your AI crawler follows Cloudflare's [verified bots policy](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/).

## 3\. Submit verification request

Submit a form to add your AI crawler to Cloudflare's list of verified bots.

  1. In the Cloudflare dashboard, go to **Manage Account** > **Settings**.

[ Go to **Configurations** ↗ ](https://dash.cloudflare.com/?to=/:account/configurations)
  2. Go to the **Bot Submission Form** tab.

  3. Fill out the form with the following required information:

     * **Select bot type** : Choose either **Verified Bot** or **Signed Agent**.
     * **Verification Method** : Select **Request Signature**.
     * **User-Agents header values** : Provide the User-Agent string(s) your bot uses.
     * **User-Agents Match Pattern** : Provide substring patterns that match your User-Agent (for example, `GoogleBot | GoogleScraper`).
  4. Select **Submit**.




[PreviousSet up your account](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/set-up-cloudflare-account/)[NextConnect Stripe](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/connect-to-stripe/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/verify-ai-crawler.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
