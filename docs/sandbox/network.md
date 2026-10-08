---
url: https://developers.cloudflare.com/sandbox/network/
title: Credentials and network access \u00b7 Cloudflare Sandboxes docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:19.809887+00:00
---

# Credentials and network access · Cloudflare Sandboxes docs

> Source: https://developers.cloudflare.com/sandbox/network/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Sandboxes](https://developers.cloudflare.com/sandbox/)
  3. /Credentials and network



# Credentials and network access

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/sandbox/network/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Any process in a sandbox can read a token that the sandbox holds. Keep the token in your Worker instead, and give the sandbox only the access it needs. A Container sends requests to a hostname that you choose, and your Worker intercepts each request and adds the token. A Dynamic Worker calls a method that your Worker passes it, and the method adds the token.

A Container that starts with `enableInternet: false` reaches only the hostnames you intercept. A Dynamic Worker loaded with `globalOutbound: null` cannot make its own requests, and reaches your application only through the methods you pass.

  * [Call an authenticated API from a sandbox](https://developers.cloudflare.com/sandbox/network/call-an-authenticated-api/): Let code in a Container or Dynamic Worker call an authenticated API without giving it the access token.
  * [Clone a private repository](https://developers.cloudflare.com/sandbox/network/clone-a-private-repository/): Clone a private GitHub repository into a Linux sandbox without giving the sandbox the access token.



For every outbound option in each environment, refer to [Handle outbound traffic](https://developers.cloudflare.com/containers/configuration/outbound-traffic/) for Containers and [Egress control](https://developers.cloudflare.com/dynamic-workers/usage/egress-control/) for Dynamic Workers.

[PreviousPreview on separate hostnames](https://developers.cloudflare.com/sandbox/previews/serve-previews-on-their-own-hostnames/)[NextCall an authenticated API](https://developers.cloudflare.com/sandbox/network/call-an-authenticated-api/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/sandbox/network/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
