---
url: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/understand-policies/
title: Understand and streamline policy creation \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:58.041467+00:00
---

# Understand and streamline policy creation · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/understand-policies/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /Secure Internet Traffic
  4. /Understand and streamline policy creation



# Understand and streamline policy creation

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/understand-policies/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewObjectives

Before you begin building security policies, there are a few key details about Gateway to review.

The next few modules will cover the breadth of types of policies and actions that can be accomplished by sending traffic through the Cloudflare Gateway inspection engine. This implementation guide assumes that your goals are to block threat actors from using attack vectors on your user base (such as malware, complex phishing attempts, and credential theft), as well as detection and prevention of threats to your corporate data (data loss prevention). These security threats may take internal and external forms. Separately, we will detail building threat prevention that uses our Remote Browser Isolation technology to maximally reduce the theoretical attack surface for your users.

This guide will provide you with a baseline of recommended policies to build and address common questions about policy building and accomplishing explicit outcomes.

## Objectives

By the end of this module, you will be able to:

  * Understand the order Gateway enforces policies for filtering traffic.
  * Create reusable lists for Gateway policies.
  * Subscribe to indicator feeds for advanced threat intelligence.



[PreviousDetermine when to use PAC files](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/configure-device-agent/pac-files/)[NextOrder of enforcement](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/understand-policies/order-of-enforcement/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/secure-internet-traffic/understand-policies/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
