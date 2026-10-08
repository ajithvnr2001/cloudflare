---
url: https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/
title: Remote browser isolation \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:44.364608+00:00
---

# Remote browser isolation · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /Remote browser isolation



# Remote browser isolation

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPermissionsPrivacyTroubleshooting

Note

Remote browser isolation is available as an add-on to Zero Trust Pay-as-you-go and Enterprise plans.

Cloudflare Browser Isolation complements the [Secure Web Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) (which inspects and filters HTTP/HTTPS traffic) and [Zero Trust Network Access](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) (which controls access to private applications) by executing active webpage content — executable code such as JavaScript and plugins — in a secure isolated browser. Because active content executes remotely instead of on the user's device, Browser Isolation protects users from zero-day attacks (attacks that exploit vulnerabilities with no available patch) and malware.

Browser Isolation also protects users from phishing attacks by preventing user input on risky websites and controlling data transmission to sensitive web applications. You can further filter isolated traffic with Gateway [HTTP](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/) and [DNS](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/) policies.

Remote browsing is invisible to the user who continues to use their browser normally without changing their preferred browser and habits. Every open tab and window is automatically isolated. When the user closes the isolated browser, their session is automatically deleted.

## Permissions

Browser Isolation is configured through Gateway [HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/) with the _Isolate_ or _Do Not Isolate_ action. Gateway role-based access control (RBAC) covers isolation policy management, and there is no separate Browser Isolation permission surface.

You can use [account-level roles](https://developers.cloudflare.com/fundamentals/manage-members/roles/#account-scoped-roles) such as `Zero Trust HTTP Policies Admin` to grant access to all HTTP policies in the account. You can also use [resource-scoped roles](https://developers.cloudflare.com/cloudflare-one/traffic-policies/granular-permissions/) to delegate management of specific isolation policies to individual team members.

For details on available roles and how to assign granular permissions, refer to [Granular permissions for Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/granular-permissions/).

## Privacy

Cloudflare Browser Isolation is a security product. In order to serve transparent isolated browsing and block web based threats our network decrypts Internet traffic using the [Cloudflare root CA](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/user-side-certificates/). Traffic logs are retained as per the [Zero Trust](https://developers.cloudflare.com/cloudflare-one/insights/logs/) documentation.

## Troubleshooting

For help resolving common issues with Browser Isolation, refer to [Troubleshoot Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/troubleshooting/).

[PreviousTroubleshoot DLP](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/troubleshoot-dlp/)[NextGet started](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/remote-browser-isolation/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
