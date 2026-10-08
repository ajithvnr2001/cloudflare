---
url: https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/require-warp/
title: Require WARP \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:50.986691+00:00
---

# Require WARP · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/require-warp/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Reusable components[Posture checks](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/)

  4. /[Cloudflare One Client checks](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/)
  5. /Require WARP



# Require WARP

Last updated Apr 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/require-warp/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Enable the WARP check2\. Add the check to an Access policy

Note

This device posture attribute will check for all versions of WARP, including the consumer version.

Cloudflare One enables you to restrict access to your applications to devices running the Cloudflare One Client. This allows you to flexibly ensure that a user's traffic is secure and encrypted before allowing access to a resource protected behind Cloudflare One.

## Prerequisites

  * Cloudflare One Client is [deployed](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/) on the device. For a list of supported modes and operating systems, refer to [Cloudflare One Client Checks](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/).




## 1\. Enable the WARP check

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Traffic policies** > **Traffic settings**.
  2. Ensure that _Allow Secure Web Gateway to proxy traffic_ * is enabled.
  3. Go to **Reusable components** > **Posture checks**.
  4. In **Cloudflare One Client checks** , select **Add a check**.
  5. Select **WARP** , then select **Save**.



## 2\. Add the check to an Access policy

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Access controls** > **Applications**.

  2. Locate the application for which you want to require WARP. Select **Configure**.

  3. In the **Policies** tab, create a new Access policy or edit an existing policy.

  4. In the policy builder, add an Include or Require rule which uses the _WARP_ selector. Save the policy.

  5. Save the Access application.




Before granting access to the application, the policy will check that the device is running the Cloudflare One Client.

[PreviousRequire Gateway](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/require-gateway/)[NextSentinelOne](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/sentinel-one/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/reusable-components/posture-checks/client-checks/require-warp.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
