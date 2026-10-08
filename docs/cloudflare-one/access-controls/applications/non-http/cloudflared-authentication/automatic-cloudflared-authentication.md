---
url: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/cloudflared-authentication/automatic-cloudflared-authentication/
title: Enable automatic cloudflared authentication \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:20.433482+00:00
---

# Enable automatic cloudflared authentication · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/cloudflared-authentication/automatic-cloudflared-authentication/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Access controls](https://developers.cloudflare.com/cloudflare-one/access-controls/)[Applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/)[Non-HTTP applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/)

  4. /[Client-side cloudflared](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/cloudflared-authentication/)
  5. /Enable automatic cloudflared authentication



# Enable automatic cloudflared authentication

Last updated May 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/cloudflared-authentication/automatic-cloudflared-authentication/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

When users connect to an Access application through `cloudflared`, the browser prompts them to allow access by displaying this page:

![Access request prompt page displayed after logging in with cloudflared.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1362,height=1016,format=webp/_astro/access-screen.BXZJ23p9.png)

Automatic `cloudflared` authentication allows users to skip this login page if they already have an active IdP session.

To enable automatic `cloudflared` authentication:

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Access controls** > **Applications**.
  2. Locate your application and select **Configure**.
  3. Go to **Authentication**.
  4. Turn on **Allow automatic Cloudflared authentication**.
  5. Select **Save**.



This option will still prompt a browser window in the background, but authentication will now happen automatically.

[PreviousOverview](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/cloudflared-authentication/)[NextArbitrary TCP](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/cloudflared-authentication/arbitrary-tcp/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/access-controls/applications/non-http/cloudflared-authentication/automatic-cloudflared-authentication.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
