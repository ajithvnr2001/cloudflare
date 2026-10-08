---
url: https://developers.cloudflare.com/speed/observatory/
title: Observatory (beta) \u00b7 Cloudflare Speed docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:34.175812+00:00
---

# Observatory (beta) · Cloudflare Speed docs

> Source: https://developers.cloudflare.com/speed/observatory/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Speed](https://developers.cloudflare.com/speed/)
  3. /Observatory (beta)



# Observatory (beta)

Last updated Aug 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/speed/observatory/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSynthetic tests Browser test Network test Network comparison testReal user monitoring (RUM)

Observatory uses synthetic tests and real user data from browsers to assess the performance of your website. These data sources produce metrics that provide different types of insights into your website’s performance. Cloudflare then uses the analysis run by Observatory to recommend optimizations with the tools that best suit your performance issues.

## Synthetic tests

As its name suggests, synthetic testing uses servers to simulate the conditions that a user might encounter when accessing your website. This has the advantage of being consistent, as the conditions are easily replicated each time the test is run. It also allows you to have an analysis of how a code change might affect the overall performance of your website, as well as test any URL you want. However, due to its synthetic nature, it cannot replicate the breadth and diversity of different conditions that real users will experience.

Observatory provides two different types of synthetic tests:

### Browser test

The browser test loads the requested page in a headless browser and runs Google Lighthouse on it. This reports key performance metrics and provides light suggestions for improvement.

### Network test

The network test is focused on giving a detailed breakdown of the network and back-end performance of an endpoint. For more information on metrics collected, refer to [Network monitoring metrics](https://developers.cloudflare.com/speed/observatory/test-results/#network-monitoring-metrics).

### Network comparison test

You can also compare network tests in Observatory by selecting any two completed tests. The results for each test are displayed side by side as histograms, allowing you to easily visualize and compare the full distribution of data points across both tests.

## Real user monitoring (RUM)

Real user monitoring (also known as RUM), on the other hand, captures real metrics from real users accessing your own websites. This provides information that synthetic tests cannot capture, as users might access your website from different parts of the world, with different network conditions, ISPs, devices, browsers, browser extensions and other software competing for resources. Real user data also includes a user interaction metric that synthetic tests do not offer: [Interaction to Next Paint (INP) ↗︎](https://web.dev/inp/).

Free customers have RUM enabled automatically, with traffic from EEA/UK/CH excluded, and can switch it off if they prefer. Customers on other plans may enable RUM as needed.

[Run test](https://developers.cloudflare.com/speed/observatory/run-speed-test/)

[PreviousOverview](https://developers.cloudflare.com/speed/)[NextObservatory dashboard](https://developers.cloudflare.com/speed/observatory/dashboard/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/speed/observatory/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
