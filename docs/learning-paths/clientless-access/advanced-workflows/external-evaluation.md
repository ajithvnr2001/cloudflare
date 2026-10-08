---
url: https://developers.cloudflare.com/learning-paths/clientless-access/advanced-workflows/external-evaluation/
title: External Evaluation rules \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:44.232186+00:00
---

# External Evaluation rules · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/clientless-access/advanced-workflows/external-evaluation/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Clientless Access

  4. /[Advanced workflows](https://developers.cloudflare.com/learning-paths/clientless-access/advanced-workflows/)
  5. /External Evaluation rules



# External Evaluation rules

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/clientless-access/advanced-workflows/external-evaluation/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSet up External Evaluation rule

With Cloudflare Access, you can build infinitely customizable policies using External Evaluation rules. External Evaluation rules allow you to call any API during the evaluation of an Access policy and authenticate users based on custom business logic. Example use cases include:

  * Customize policies based on time of day.
  * Check IP addresses against external threat feeds.
  * Call industry-specific user registries.



The External Evaluation rule requires two values: an API endpoint to call and a key to verify that any request response is coming from a trusted source. After the user authenticates with your identity provider, all information about the user, device and location is passed to your external API. The API returns a pass or fail response to Access which will then either allow or deny access to the user.

## Set up External Evaluation rule

For detailed setup instructions, refer to [External Evaluation rules](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/external-evaluation/).

Example code for the API is available in our [open-source repository ↗︎](https://github.com/cloudflare/workers-access-external-auth-example).

[PreviousOverview](https://developers.cloudflare.com/learning-paths/clientless-access/advanced-workflows/)[NextIsolate Access applications](https://developers.cloudflare.com/learning-paths/clientless-access/advanced-workflows/isolate-application/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/clientless-access/advanced-workflows/external-evaluation.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
