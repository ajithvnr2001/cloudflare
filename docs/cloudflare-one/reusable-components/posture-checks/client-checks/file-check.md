---
url: https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/file-check/
title: File check \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:49.509730+00:00
---

# File check · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/file-check/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Reusable components[Posture checks](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/)

  4. /[Cloudflare One Client checks](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/)
  5. /File check



# File check

Last updated May 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/file-check/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesConfigure a file check

The File Check device posture attribute checks for the presence of a file on a device. You can create multiple file checks for each operating system you need to run it on, or if you need to check for multiple files.

## Prerequisites

  * Cloudflare One Client is [deployed](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/) on the device. For a list of supported modes and operating systems, refer to [Cloudflare One Client Checks](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/).




## Configure a file check

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Reusable components** > **Posture checks**.

  2. Go to **Cloudflare One Client checks** and select **Add a check**.

  3. Select **File Check**.

  4. You will be prompted for the following information:

     1. **Name** : Enter a unique name for this device posture check.

     2. **Operating system** : Select your operating system.

     3. **File Path** : Enter a file path (for example, `c:\my folder\myfile.exe`).

Environment variables

File paths can include environment variables to account for differences across devices. Environment variables are resolved in the context of the Cloudflare One Client daemon, not the logged-in user. Only variables available to the daemon process at runtime will work.

        * **Windows** : Use `%VAR%` syntax. For example, `%PROGRAMFILES%\myfolder\myfile.exe`.
        * **macOS/Linux** : Use `${VAR}` syntax. For example, `${RUNTIME_DIRECTORY}/myfolder/myfile`.
     4. **Signing certificate thumbprint (recommended)** : Enter the [thumbprint](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/application-check/#determine-the-signing-thumbprint) of the publishing certificate used to sign the file. Adding this information will enable the check to ensure that the file was signed by the expected software developer.

     5. **SHA-256 (optional)** : Enter the [SHA-256 value](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/application-check/#determine-the-sha-256-value) of the file. This is used to ensure the integrity of the file on the device.

  5. Select **Save**.




Next, go to **Insights** > **Logs** > **Posture logs** and verify that the file check is returning the expected results.

[PreviousDomain joined](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/domain-joined/)[NextFirewall](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/firewall/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/reusable-components/posture-checks/client-checks/file-check.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
