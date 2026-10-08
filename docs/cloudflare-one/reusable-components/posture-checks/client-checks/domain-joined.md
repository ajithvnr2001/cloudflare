---
url: https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/domain-joined/
title: Domain joined \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:49.394036+00:00
---

# Domain joined · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/domain-joined/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Reusable components[Posture checks](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/)

  4. /[Cloudflare One Client checks](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/)
  5. /Domain joined



# Domain joined

Last updated May 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/domain-joined/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesEnable the Domain Joined checkValidate the domain value

The Domain Joined device posture attribute ensures that a user is a member of a specific Windows Active Directory domain.

## Prerequisites

  * Cloudflare One Client is [deployed](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/) on the device. For a list of supported modes and operating systems, refer to [Cloudflare One Client Checks](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/).




## Enable the Domain Joined check

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Reusable components** > **Posture checks**.
  2. Go to **Cloudflare One Client checks** and select **Add a check**.
  3. Select **Domain Joined**.
  4. Enter a descriptive name for the check.
  5. Select your operating system.
  6. Enter the domain you want to check for, such as `example.com`. 

Note

The **Domain** field is case-sensitive. If your domain is `example.com`, entering `Example.com` will fail the posture check.

  7. Select **Save**.



Next, go to **Insights** > **Logs** > **Posture logs** and verify that the Domain Joined check is returning the expected results.

## Validate the domain value

To check the domain value on your Windows device:

  1. Open a PowerShell window.

  2. Run the following command:
         
         (Get-WmiObject Win32_ComputerSystem).Domain




The command will return the Active Directory domain to which your device belongs.

[PreviousDisk encryption](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/disk-encryption/)[NextFile check](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/file-check/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/reusable-components/posture-checks/client-checks/domain-joined.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
