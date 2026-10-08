---
url: https://developers.cloudflare.com/changelog/product/pages/
title: Pages Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:48.055822+00:00
---

# Pages Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/pages/

# Changelog

New updates and improvements at Cloudflare.

All products

Product groups

AI

Analytics

Application performance

Application security

Cloudflare One

Consumer services

Core platform

Developer platform

Docs collections

Media

Network security

Privacy

Storage

Products

1.1.1.1 (DNS Resolver)

Access

Agent Lee

Agents

AI Crawl Control

AI Gateway

AI Search

Analytics

API Shield

Artifacts

Audit Logs

Automatic Platform Optimization

Basin

Basin Catalog

Basin Pipelines

Basin SQL

Billing

Bots

Browser Isolation

Browser Run

Cache / CDN

CASB

Cloudflare CLI

Cloudflare for SaaS

Cloudflare Fundamentals

Cloudflare Images

Cloudflare Mesh

Cloudflare Network Firewall

Cloudflare One

Cloudflare One Appliance

Cloudflare One Client

Cloudflare Tunnel

Cloudflare Tunnel for SASE

Cloudflare WAN

Cloudflare Web Analytics

Containers

D1

Data Localization Suite

Data Loss Prevention

Digital Experience Monitoring

DNS

Durable Objects

Email security

Email Service

Flagship

Gateway

Go SDK

Hyperdrive

KV

Load Balancing

Log Explorer

Logpush

Logpush Connectors

Logs

Magic Transit

Monetization Gateway

Multi-Cloud Networking

Network Flow

Network Interconnect

Organizations

Pages

Privacy Proxy

Queues

R2

Radar

Realtime

Registrar

Resource Tagging

Risk Score

Rules

Sandboxes

SDK

Secrets Store

Security Center

Security Overview

Speed

SSL/TLS

Stream

Support

Terraform

Turnstile

Vectorize

WAF

Web Search API

Workers

Workers AI

Workers Analytics Engine

Workers for Platforms

Workers VPC

Workflows

Zaraz

No products found.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

Aug 11, 2026

## [Pages now skips superseded queued builds](https://developers.cloudflare.com/changelog/post/2026-08-11-skip-superseded-builds/)

[Pages](https://developers.cloudflare.com/pages/)

Pages now automatically skips a queued build when a newer build for the same project, branch, and deployment target is also queued.

Jan 23, 2026

## [Increased Pages file limit to 100,000 for paid plans](https://developers.cloudflare.com/changelog/post/2026-01-23-pages-file-limit-increase/)

[Pages](https://developers.cloudflare.com/pages/)

Paid plans can now have up to 100,000 files per Pages site, increased from the previous limit of 20,000 files.

To enable this increased limit, set the environment variable `PAGES_WRANGLER_MAJOR_VERSION=4` in your Pages project settings.

The Free plan remains at 20,000 files per site.

For more details, refer to the [Pages limits documentation](https://developers.cloudflare.com/pages/platform/limits/#files).

May 30, 2025

## [Cloudflare Pages builds now provide Node.js v22 by default](https://developers.cloudflare.com/changelog/post/2025-05-30-pages-build-image-v3/)

[Pages](https://developers.cloudflare.com/pages/)

When you use the built-in build system that is part of [Cloudflare Pages](https://developers.cloudflare.com/pages/), the [Build Image](https://developers.cloudflare.com/pages/configuration/build-image/) now includes Node.js v22. Previously, Node.js v18 was provided by default, and Node.js v18 is now end-of-life (EOL).

If you are creating a new Pages project, the new V3 build image that includes Node.js v22 will be used by default. If you have an existing Pages project, you can update to the latest build image by navigating to Settings > Build & deployments > Build system version in the Cloudflare dashboard for a specific Pages project.

Note that you can always specify a particular version of Node.js or other built-in dependencies by [setting an environment variable](https://developers.cloudflare.com/pages/configuration/build-image/#override-default-versions).

For more, refer to the [developer docs for Cloudflare Pages builds](https://developers.cloudflare.com/pages/configuration/build-image)

Mar 22, 2025

## [New Managed WAF rule for Next.js CVE-2025-29927.](https://developers.cloudflare.com/changelog/post/2025-03-22-next-js-vulnerability-waf/)

[Workers](https://developers.cloudflare.com/workers/)[Pages](https://developers.cloudflare.com/pages/)[WAF](https://developers.cloudflare.com/waf/)

**Update: Mon Mar 24th, 11PM UTC** : Next.js has made further changes to address a smaller vulnerability introduced in the patches made to its middleware handling. Users should upgrade to Next.js versions `15.2.4`, `14.2.26`, `13.5.10` or `12.3.6`. **If you are unable to immediately upgrade or are running an older version of Next.js, you can enable the WAF rule described in this changelog as a mitigation**.

**Update: Mon Mar 24th, 8PM UTC** : Next.js has now [backported the patch for this vulnerability ↗︎](https://github.com/advisories/GHSA-f82v-jwr5-mffw) to cover Next.js v12 and v13. Users on those versions will need to patch to `13.5.9` and `12.3.5` (respectively) to mitigate the vulnerability.

**Update: Sat Mar 22nd, 4PM UTC** : We have changed this WAF rule to opt-in only, as sites that use auth middleware with third-party auth vendors were observing failing requests.

**We strongly recommend updating your version of Next.js (if eligible)** to the patched versions, as your app will otherwise be vulnerable to an authentication bypass attack regardless of auth provider.

#### Enable the Managed Rule (strongly recommended)

This rule is opt-in only for sites on the Pro plan or above in the [WAF managed ruleset](https://developers.cloudflare.com/waf/managed-rules/).

To enable the rule:

  1. Head to Security > WAF > Managed rules in the Cloudflare dashboard for the zone (website) you want to protect.
  2. Click the three dots next to **Cloudflare Managed Ruleset** and choose **Edit**
  3. Scroll down and choose **Browse Rules**
  4. Search for **CVE-2025-29927** (ruleId: `34583778093748cc83ff7b38f472013e`)
  5. Change the **Status** to **Enabled** and the **Action** to **Block**. You can optionally set the rule to Log, to validate potential impact before enabling it. Log will not block requests.
  6. Click **Next**
  7. Scroll down and choose **Save**



This will enable the WAF rule and block requests with the `x-middleware-subrequest` header regardless of Next.js version.

#### Create a WAF rule (manual)

For users on the Free plan, or who want to define a more specific rule, you can create a [Custom WAF rule](https://developers.cloudflare.com/waf/custom-rules/create-dashboard/) to block requests with the `x-middleware-subrequest` header regardless of Next.js version.

To create a custom rule:

  1. Head to Security > WAF > Custom rules in the Cloudflare dashboard for the zone (website) you want to protect.
  2. Give the rule a name - e.g. `next-js-CVE-2025-29927`
  3. Set the matching parameters for the rule match any request where the `x-middleware-subrequest` header `exists` per the rule expression below.


    
    
    (len(http.request.headers["x-middleware-subrequest"]) > 0)

  4. Set the action to 'block'. If you want to observe the impact before blocking requests, set the action to 'log' (and edit the rule later).
  5. **Deploy** the rule.

![Next.js CVE-2025-29927 WAF rule](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2116,height=1148,format=webp/_astro/waf-rule-cve-2025-29927.0i0XiweZ.png)

#### Next.js CVE-2025-29927

We've made a WAF (Web Application Firewall) rule available to all sites on Cloudflare to protect against the [Next.js authentication bypass vulnerability ↗︎](https://github.com/advisories/GHSA-f82v-jwr5-mffw) (`CVE-2025-29927`) published on March 21st, 2025.

**Note** : This rule is not enabled by default as it blocked requests across sites for specific authentication middleware.

  * This managed rule protects sites using Next.js on Workers and Pages, as well as sites using Cloudflare to protect Next.js applications hosted elsewhere.
  * This rule has been made available (but not enabled by default) to all sites as part of our [WAF Managed Ruleset](https://developers.cloudflare.com/waf/managed-rules/reference/cloudflare-managed-ruleset/) and blocks requests that attempt to bypass authentication in Next.js applications.
  * The vulnerability affects almost all Next.js versions, and has been fully patched in Next.js `14.2.26` and `15.2.4`. Earlier, interim releases did not fully patch this vulnerability.
  * **Users on older versions of Next.js (`11.1.4` to `13.5.6`) did not originally have a patch available**, but this the patch for this vulnerability and a subsequent additional patch have been backported to Next.js versions `12.3.6` and `13.5.10` as of Monday, March 24th. Users on Next.js v11 will need to deploy the stated workaround or enable the WAF rule.



The managed WAF rule mitigates this by blocking _external_ user requests with the `x-middleware-subrequest` header regardless of Next.js version, but we recommend users using Next.js 14 and 15 upgrade to the patched versions of Next.js as an additional mitigation.

Mar 22, 2025

## [Smart Placement is smarter about running Workers and Pages Functions in the best locations](https://developers.cloudflare.com/changelog/post/2025-03-22-smart-placement-stablization/)

[Workers](https://developers.cloudflare.com/workers/)[Pages](https://developers.cloudflare.com/pages/)

[Smart Placement](https://developers.cloudflare.com/workers/configuration/placement/) is a unique Cloudflare feature that can make decisions to move your Worker to run in a more optimal location (such as closer to a database). Instead of always running in the default location (the one closest to where the request is received), Smart Placement uses certain “heuristics” (rules and thresholds) to decide if a different location might be faster or more efficient.

Previously, if these heuristics weren't consistently met, your Worker would revert to running in the default location—even after it had been optimally placed. This meant that if your Worker received minimal traffic for a period of time, the system would reset to the default location, rather than remaining in the optimal one.

Now, once Smart Placement has identified and assigned an optimal location, temporarily dropping below the heuristic thresholds will not force a return to default locations. For example in the previous algorithm, a drop in requests for a few days might return to default locations and heuristics would have to be met again. This was problematic for workloads that made requests to a geographically located resource every few days or longer. In this scenario, your Worker would never get placed optimally. This is no longer the case.

Mar 17, 2025

## [Retry Pages & Workers Builds Directly from GitHub](https://developers.cloudflare.com/changelog/post/2025-03-17-rerun-build/)

[Workers](https://developers.cloudflare.com/workers/)[Pages](https://developers.cloudflare.com/pages/)

You can now retry your Cloudflare Pages and Workers builds directly from GitHub. No need to switch to the Cloudflare Dashboard for a simple retry!

Let\u2019s say you push a commit, but your build fails due to a spurious error like a network timeout. Instead of going to the Cloudflare Dashboard to manually retry, you can now rerun the build with just a few clicks inside GitHub, keeping you inside your workflow.

For Pages and Workers projects connected to a GitHub repository:

  1. When a build fails, go to your GitHub repository or pull request
  2. Select the failed Check Run for the build
  3. Select "Details" on the Check Run
  4. Select "Rerun" to trigger a retry build for that commit



Learn more about [Pages Builds](https://developers.cloudflare.com/pages/configuration/git-integration/github-integration/) and [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/github-integration/).
