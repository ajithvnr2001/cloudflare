---
url: https://developers.cloudflare.com/cloudflare-one/access-controls/policies/isolate-application/
title: Isolate self-hosted application \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:22.677814+00:00
---

# Isolate self-hosted application · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/access-controls/policies/isolate-application/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Access controls](https://developers.cloudflare.com/cloudflare-one/access-controls/)

  4. /[Policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)
  5. /Isolate self-hosted application



# Isolate self-hosted application

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/isolate-application/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesEnable Browser IsolationPolicies for isolated applicationsProduct compatibility

Note

Requires [Cloudflare Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/).

With Access policies, you can require users to open self-hosted applications in a secure [remote browser](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/). Because the remote browser is directly integrated into our Secure Web Gateway platform, [HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/) can be applied to isolated applications without needing to install the Cloudflare One Client. This allows you to distribute internal applications to unmanaged users while retaining control over sensitive data.

## Prerequisites

Your browser must [allow third-party cookies](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/#allow-third-party-cookies-in-the-browser) on the application domain.

## Enable Browser Isolation

  1. In [Cloudflare One ↗︎](https://one.dash.cloudflare.com/), go to **Browser isolation** > **Browser isolation settings**.
  2. Turn on **Allow users to open a remote browser without the device client**.


  3. Go to **Access controls** > **Applications**.
  4. Choose a [self-hosted application](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/) and select **Configure**.
  5. Go to **Policies**.
  6. Choose an [Allow policy](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) and select **Configure**.
  7. Under **Additional settings** , turn on **Isolate application**.
  8. Save the policy.



Browser Isolation is now enabled for users who match this policy. After the user logs into Access, the application will launch in a remote browser. To confirm that the application is isolated, refer to [Check if a web page is isolated](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/#3-check-if-a-web-page-is-isolated).

You can optionally add another Allow policy for users on managed devices who do not require isolation.

## Policies for isolated applications

Traffic to the isolated Access application is filtered by your Gateway [HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/). Useful policies include:

  * [Identity-based policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/identity-selectors/) to allow or block requests based on user identity.
  * [Data Loss Prevention policies](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/) to log or block transmission of sensitive data.
  * [Isolation policies](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/) to disable browser actions such as copy/paste, printing, or file downloads.



For example, if your application is hosted on `internal.site.com`, the following policy blocks users from uploading and downloading credit card numbers within the remote browser:

Selector | Operator | Value | Logic | Action  
---|---|---|---|---  
Domain | in | `internal.site.com` | And | Block  
DLP Profile | in | `Financial Information` |  |   
  
## Product compatibility

For a list of products that are incompatible with the **Isolate application** feature, refer to [Product Compatibility](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/#product-compatibility) .

[PreviousExternal Evaluation rules](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/external-evaluation/)[NextApplication paths](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/app-paths/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/access-controls/policies/isolate-application.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
