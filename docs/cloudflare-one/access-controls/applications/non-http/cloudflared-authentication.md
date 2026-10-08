---
url: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/cloudflared-authentication/
title: Client-side cloudflared \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:19.858753+00:00
---

# Client-side cloudflared · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/cloudflared-authentication/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Access controls](https://developers.cloudflare.com/cloudflare-one/access-controls/)[Applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/)

  4. /[Non-HTTP applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/)
  5. /Client-side cloudflared



# Client-side cloudflared

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/cloudflared-authentication/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

With Cloudflare Zero Trust, users can connect to non-HTTP applications via a public hostname without installing the Cloudflare One Client. This method requires you to onboard a domain to Cloudflare and install `cloudflared` on both the server and the user's device.

Users log in to the application by running a `cloudflared access` command in their terminal. `cloudflared` will launch a browser window and prompt the user to authenticate with your identity provider.

Note

Automated services should only authenticate with `cloudflared` if they cannot use a [service token](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/). Cloudflared authentication relies on WebSockets to establish a connection. WebSockets have a known limitation where persistent connections may close unexpectedly. We recommend either a [Service Auth policy](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/#service-auth) or using [Warp to Tunnel routing](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/) in these instances.

For examples of how to connect to Access applications with client-side `cloudflared`, refer to these tutorials:

  * [Connect through Access using a CLI](https://developers.cloudflare.com/cloudflare-one/tutorials/cli/)
  * [Connect through Access using kubectl](https://developers.cloudflare.com/cloudflare-one/tutorials/kubectl/)
  * [Connect to SSH with client-side cloudflared](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-cloudflared-authentication/)
  * [Connect over RDP with cloudflared](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/#connect-to-rdp-server-with-cloudflared-access)
  * [Connect over SMB with cloudflared](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/smb/)
  * [Connect over arbitrary TCP with cloudflared](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/cloudflared-authentication/arbitrary-tcp/)



[PreviousBrowser-rendered terminal](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/browser-rendering/)[NextEnable automatic cloudflared authentication](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/cloudflared-authentication/automatic-cloudflared-authentication/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/access-controls/applications/non-http/cloudflared-authentication/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
