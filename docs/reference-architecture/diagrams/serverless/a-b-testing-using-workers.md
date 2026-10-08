---
url: https://developers.cloudflare.com/reference-architecture/diagrams/serverless/a-b-testing-using-workers/
title: A/B-testing using Workers \u00b7 Cloudflare Reference Architecture docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:42.600638+00:00
---

# A/B-testing using Workers · Cloudflare Reference Architecture docs

> Source: https://developers.cloudflare.com/reference-architecture/diagrams/serverless/a-b-testing-using-workers/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Reference Architecture](https://developers.cloudflare.com/reference-architecture/)
  3. /…

Reference Architecture Diagrams

  4. /Serverless
  5. /A/B-testing using Workers



# A/B-testing using Workers

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/reference-architecture/diagrams/serverless/a-b-testing-using-workers/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewIntroductionA/B testing using WorkersRelated resources

## Introduction

A/B testing, also known as split testing, is a fundamental technique in the realm of web development, allowing teams to iteratively refine and optimize their digital experiences. A/B testing involves comparing two versions of a web page or app feature to determine which one performs better in achieving a predefined goal, such as increasing conversions, engagement, or user satisfaction.

The process typically begins with the creation of two variants: the control (A) and the variant (B). These variants are identical except for the specific element being tested, whether it's a headline, button color, layout, or any other component of the user interface or user experience. For example, a team might test two different call-to-action button colors to see which one generates more clicks.

Once the variants are ready, they are exposed to users in a randomized manner. This randomization ensures that any differences in performance between the variants can be attributed to the changes being tested rather than external factors like user demographics or behavior.

As users interact with the different variants, their actions and behaviors are tracked and analyzed to measure the performance of each variant against the predefined goal. Key metrics such as click-through rates, conversion rates, bounce rates, and engagement metrics are monitored to determine which variant is more effective in achieving the desired outcome.

A/B testing is a powerful tool for continuously optimizing and improving digital experiences, enabling teams to make data-driven decisions based on real user feedback rather than subjective opinions or assumptions. By systematically testing and refining different elements of their websites or applications, organizations can enhance user satisfaction, increase conversions, and ultimately achieve their business objectives in a competitive online landscape.

Cloudflare's low-latency, fully serverless compute platform, [Workers](https://developers.cloudflare.com/workers/) offers powerful capabilities to enable A/B testing using a server-side implementation. With the help of [Workers KV](https://developers.cloudflare.com/kv/), this solution can be make highly configurable with ease.

## A/B testing using Workers

![Figure 1: A/B testing using Workers](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1200,height=466,format=svg/_astro/a-b-testing-workers.2TNh_6Un.svg)Figure 1: A/B testing using Workers

This architecture shows a same-URL A/B testing endpoint. The A/B testing logic and configuration is deployed on the server side, so that clients do not have to implement any changes to make use of A/B testing.

  1. **Client** : Sends requests to server. This could be through a desktop or mobile browser, or native or mobile app.
  2. **Configuration** : Process incoming request using Workers. Read current configuration by reading from [KV](https://developers.cloudflare.com/kv/) using the [`get()`](https://developers.cloudflare.com/kv/api/read-key-value-pairs/) method. This allows for flexible updates to the A/B services configuration fully decoupled from code-deployment.
  3. **Origin requests** : Check for already existing cookies in the request headers. If no cookie for group assignment is set, randomly assign a group. If a cookie is set, extract assigned group from the cookie header. Send request to either the control endpoint (A) or variant endpoints (B) depending on the configuration and the assigned group.
  4. **Response** : Return the response from the origin. Additionally, if no cookie was previously set, set a cookie with the respective assigned group for session affinity.



For an example with code snippets on how to use Workers and Workers KV to route requests to different origin web servers, refer to Workers KV's example on [routing across web servers](https://developers.cloudflare.com/kv/examples/routing-with-workers-kv/).

## Related resources

  * [Workers: Get started](https://developers.cloudflare.com/workers/get-started/guide/)
  * [Workers KV: Get started](https://developers.cloudflare.com/kv/get-started/)
  * [Workers KV: Route requests to web servers with Workers and Workers KV](https://developers.cloudflare.com/kv/examples/routing-with-workers-kv/)
  * [Code Example: A/B testing with same-URL direct access](https://developers.cloudflare.com/workers/examples/ab-testing/)



[PreviousSecuring data in use](https://developers.cloudflare.com/reference-architecture/diagrams/security/securing-data-in-use/)[NextFullstack applications](https://developers.cloudflare.com/reference-architecture/diagrams/serverless/fullstack-application/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/reference-architecture/diagrams/serverless/a-b-testing-using-workers.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
