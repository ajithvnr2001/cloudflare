---
url: https://developers.cloudflare.com/speed/observatory/faq/
title: FAQ \u00b7 Cloudflare Speed docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:34.118618+00:00
---

# FAQ · Cloudflare Speed docs

> Source: https://developers.cloudflare.com/speed/observatory/faq/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Speed](https://developers.cloudflare.com/speed/)
  3. /[Observatory (beta)](https://developers.cloudflare.com/speed/observatory/)
  4. /FAQ



# FAQ

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/speed/observatory/faq/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow long does it take for a test to load?Are query parameters or anchors supported in tested URLs?I get a 403 response when rerunning the website analysis?Why might users not see any Real User Monitoring (RUM) data on the map in Observatory?What are the potential reasons for discrepancies between RUM analytics and traffic analytics in Observatory?How do I disable Real User Monitoring (RUM) if it has been enabled from the Observatory test result page?

Below you will find answers to our most commonly asked questions. If you cannot find the answer you are looking for, refer to the [community page ↗︎](https://community.cloudflare.com/c/website-application-performance/88) to explore more resources.

## How long does it take for a test to load?

It can vary from about 25 seconds to over a minute. If you leave your speed tab open, your test is still going to run. You can leave and return and still see your test results.

## Are query parameters or anchors supported in tested URLs?

No. At the moment, any query parameter or anchor appended to the tested URL are dropped.

For example, using the `https://example.com/blog/?utm_medium=social#title` URL, the Observatory will discard the `?utm_medium=social` query parameter as well as the `#title` anchor. The tested URL will actually be `https://example.com/blog/`.

## I get a `403` response when rerunning the website analysis?

Check your WAF custom rules to make sure that you are not blocking traffic from Observatory to request your site.

Note

For **IPv6** Cloudflare Observatory tests originate from **ASN 15169** or **ASN 132892** and are generated with the following user agents:

  * Mozilla/5.0 (Linux; Android 11; Moto G Power (2022)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36
  * Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36



For **IPv4** Cloudflare Observatory tests originate from **ASN 396982** and are generated with the following user agents:

  * Mozilla/5.0 (Linux; Android 11; moto g power (2022)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36 CloudflareObservatory/1.0
  * Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 CloudflareObservatory/1.0



## Why might users not see any Real User Monitoring (RUM) data on the map in Observatory?

There are several reasons why users might not see any Real User Monitoring (RUM) data on the map in Observatory:

  * Time Required for RUM Data Population: Populating the RUM database takes some time. It means that newly enabled RUM might not have immediate data available, and users may need to wait for some time before RUM data starts appearing on the map.

  * Progressive Sampling: RUM data is progressively sampled, which means that not all requests are captured. Some requests may pass through the sampling period, resulting in incomplete or missing data points on the map.

  * Adblockers Impact on RUM Data: RUM data collection relies on third-party JavaScript executing on the real-user browser. However, adblockers or similar browser extensions can block this script, preventing the collection of RUM data, and thereby affecting the completeness of the analytics presented on the map.

  * The RUM feature needs to be enabled and configured in your environment. If it has not been turned on, or if configuration is incomplete, RUM data may not appear.




## What are the potential reasons for discrepancies between RUM analytics and traffic analytics in Observatory?

Differences between Real User Monitoring (RUM) analytics and traffic analytics in Observatory can occur due to the following reasons:

  * Adblockers Impact on RUM Data: Similar to the previous point, RUM data collection can be thwarted by adblockers, leading to missed data. Since traffic analytics typically rely on server-side data collection, they may not be as affected by adblockers as RUM.

  * Progressive Sampling in RUM: RUM data is collected through progressive sampling, which means that not all user requests are captured. This sampling method could result in slight variations in analytics when compared to traditional traffic analytics that record every server request.




## How do I disable Real User Monitoring (RUM) if it has been enabled from the Observatory test result page?

Enabling RUM creates a Web Analytics configuration entry for the hostname at the account level.

If you wish to disable RUM, follow these steps:

  1. In the Cloudflare dashboard, go to the **Web Analytics** page.

[ Go to **Web analytics** ↗ ](https://dash.cloudflare.com/?to=/:account/web-analytics)
  2. Select **Manage Site** for the hostname for which you wish to disable RUM.

  3. Select **Delete**.




[PreviousRUM beacon for Web Analytics](https://developers.cloudflare.com/speed/observatory/rum-beacon/)[NextOrigin Analytics](https://developers.cloudflare.com/speed/origin-analytics/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/speed/observatory/faq.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
