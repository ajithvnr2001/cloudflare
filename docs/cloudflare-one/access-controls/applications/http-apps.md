---
url: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/
title: Add web applications \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:11.507646+00:00
---

# Add web applications · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Access controls](https://developers.cloudflare.com/cloudflare-one/access-controls/)

  4. /[Applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/)
  5. /Add web applications



# Add web applications

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Access allows you to secure your web applications by acting as an identity-aware proxy. Access sits in front of your application and checks each request against your [Access policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) before allowing it through. You can use signals from your existing identity providers (IdPs), device posture providers, and [other selectors](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/#selectors) to control who can reach the application.

![Cloudflare Access verifies a user's identity before granting access to your application.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3791,height=1399,format=webp/_astro/diagram-saas.BmFlwn8e.jpg)

You can protect the following types of web applications:

  * [**SaaS applications**](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/) consist of applications your team relies on that are not hosted by your organization. Examples include Salesforce and Workday. To secure SaaS applications, you must integrate Cloudflare Access with the SaaS application's SSO configuration.

  * **Self-hosted applications** consist of internal applications that you host in your own environment. These can be the data center versions of tools like the Atlassian suite or applications created by your own team. Setup requirements for a self-hosted application depend on whether the application is publicly accessible on the Internet or restricted to users on a private network.

    * [**Public hostname applications**](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/) are web applications that have public DNS records. Anyone on the Internet can access the application by entering the URL in their browser and authenticating through Cloudflare Access. Securing access to a public website requires a Cloudflare DNS [full setup](https://developers.cloudflare.com/dns/zone-setups/full-setup/) or [partial CNAME setup](https://developers.cloudflare.com/dns/zone-setups/partial-setup/).
    * [**Private network applications**](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/) do not have public DNS records, meaning they are not reachable from the public Internet. To connect using a private IP or private hostname, the user's traffic must route through Cloudflare Gateway. The preferred method is to install the [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/) on the user's device. Alternative options include forwarding traffic from a [network location](https://developers.cloudflare.com/cloudflare-wan/), using [PAC files](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/), or [Clientless Web Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/).
  * [**Model Context Protocol (MCP) servers**](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/) are web applications that enable generative AI tools to read and write data within your business applications. For example, Salesforce provides an [MCP server ↗︎](https://github.com/salesforcecli/mcp) for developers to interact with resources in their Salesforce tenant using GitHub Copilot or other AI code editors.

  * [**Cloudflare Dashboard SSO**](https://developers.cloudflare.com/fundamentals/manage-members/dashboard-sso/) is a special type of SaaS application that manages SSO settings for the Cloudflare dashboard and has limited permissions for administrator edits.




[PreviousChoose an application type](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/choose-application-type/)[NextOverview](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/access-controls/applications/http-apps/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
