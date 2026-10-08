---
url: https://developers.cloudflare.com/byoip/concepts/dynamic-advertisement/best-practices/
title: Best practices for dynamic advertisement \u00b7 Cloudflare BYOIP docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:39.831002+00:00
---

# Best practices for dynamic advertisement · Cloudflare BYOIP docs

> Source: https://developers.cloudflare.com/byoip/concepts/dynamic-advertisement/best-practices/

  1. [Home](https://developers.cloudflare.com/)
  2. /[BYOIP](https://developers.cloudflare.com/byoip/)
  3. /…

Concepts

  4. /[Dynamic advertisement](https://developers.cloudflare.com/byoip/concepts/dynamic-advertisement/)
  5. /Best practices



# Best practices

Last updated Sep 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/byoip/concepts/dynamic-advertisement/best-practices/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesEnable prefix advertisementDisable or withdraw prefix advertisementConfigure dynamic advertisement Via the Cloudflare dashboard Via the APIObtain prefix IDs

## Prerequisites

To prevent issues and simplify the advertisement process during an attack scenario, complete the following tasks.

  * Assign appropriate user roles. Ensure that users assigned to manage the status of IP prefix advertisement have the **Administrator** or **Super Administrator** role in your Cloudflare account. For more information, refer to [Setting up Multi-user accounts on Cloudflare](https://developers.cloudflare.com/fundamentals/manage-members/).

  * Get a list of the prefix IDs that you want to manage. Maintain a list of Cloudflare prefix IDs to simplify dynamic advertisement management and operations. You can obtain prefix IDs via the Cloudflare dashboard or use the [list prefixes](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/methods/list/) operation in the Cloudflare API. Refer to these prefix IDs when managing prefix advertisement.




## Enable prefix advertisement

You can avoid latency and the possibility of dropped routes by enabling prefix advertisement from Cloudflare before you withdraw the advertisement from your data center.

  1. Refer to configure dynamic advertisement. This operation requires your account ID, prefix IDs, and API key.
  2. Verify the advertisement using a looking glass of your choice, such as [Hurricane Electric Internet Services ↗︎](https://lg.he.net/). Use the Cloudflare ASN (`13335`) to track the advertisement route.
  3. Remove the prefix advertisement that originates from your data center.



Note

If you do not remove the advertisement from your data center, some of your traffic may not route through Cloudflare for protection, depending on which routes your ISP prefers.

If you want to continue advertising from your data center while using [Magic Transit](https://developers.cloudflare.com/magic-transit/), one option is to advertise a less specific route and have Cloudflare advertise more specific routes.

Enablement takes approximately five to seven minutes.

## Disable or withdraw prefix advertisement

  1. Add the prefix advertisement to your data center.
  2. (Optional) Verify the advertisement using a looking glass of your choice, such as [Hurricane Electric Internet Services ↗︎](https://lg.he.net/).
  3. Refer to configure dynamic advertisement. This operation requires your account ID, prefix IDs, and API key.



Disablement takes approximately 15 minutes.

## Configure dynamic advertisement

Rate limit

After you change a prefix's advertisement status, wait at least 15 minutes before changing it again. Requests made during this interval return a `429` response with error code `1004` (`rate_limit_exceeded`).

### Via the Cloudflare dashboard

  1. Log in to your [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/) and select your account.
  2. Go to **IP Addresses** > **BYOIP Prefixes**.
  3. Select **Edit** at the end of the entry.
  4. From **Edit IP Prefixes** , select **Advertised** or **Withdrawn** under **Status**.
  5. Select **Save** to commit your changes.



After saving your changes, it takes between two to seven minutes to enable advertisement and approximately 15 minutes to disable or withdraw advertisement.

### Via the API

To configure prefix advertisement with the Cloudflare API, use the [IP Address Management and Dynamic Advertisement](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/advertisement_status/methods/edit/) API.

Most dynamic advertisement operations require that you supply the Cloudflare ID for any prefix you want to access with the Cloudflare API. The following section outlines how to obtain prefix IDs.

## Obtain prefix IDs

  1. Log in to your [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/) and select your account.
  2. Go to **IP Addresses** > **BYOIP Prefixes**.
  3. Find the CIDR for which you want the prefix ID, and select the arrow next to it.
  4. Under **Prefix ID** , select **Copy** to add the value to your clipboard.



To obtain prefix IDs using the API, refer to the [list prefixes](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/methods/list/) operation in the Cloudflare API.

[PreviousOverview](https://developers.cloudflare.com/byoip/concepts/dynamic-advertisement/)[NextOverview](https://developers.cloudflare.com/byoip/concepts/irr-entries/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/byoip/concepts/dynamic-advertisement/best-practices.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
