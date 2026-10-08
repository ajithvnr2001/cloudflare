---
url: https://developers.cloudflare.com/cloudflare-challenges/reference/private-access-tokens/
title: Private Access Tokens (PAT) \u00b7 Cloudflare challenges docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:58.865251+00:00
---

# Private Access Tokens (PAT) · Cloudflare challenges docs

> Source: https://developers.cloudflare.com/cloudflare-challenges/reference/private-access-tokens/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Challenges](https://developers.cloudflare.com/cloudflare-challenges/)
  3. /Reference
  4. /Private Access Tokens (PAT)



# Private Access Tokens (PAT)

Last updated Jun 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-challenges/reference/private-access-tokens/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewExpected 401 responses

When a visitor is presented with a Challenge Page, Cloudflare evaluates various signals - including the presence of a Private Access Token (PAT) - to decide which challenges to issue. If a visitor presents a valid token, certain challenges are not issued, which reduces the number of steps required to pass.

A PAT does not automatically solve a challenge or let a visitor bypass the Challenge Page. The visitor still encounters the Challenge Page regardless of whether they have a valid PAT.

While some challenges require interactivity, most challenges served are invisible to the visitor.

## Expected 401 responses

While loading a Challenge Page, the visitor's browser may attempt to retrieve a Private Access Token by issuing a request to a `/cdn-cgi/challenge-platform/.../pat/...` path. When the visitor's device, browser, or network environment cannot provide a token — for example, on unsupported platforms, in some managed or enterprise environments, or when connected through certain VPNs — this request returns an HTTP `401` response.

This `401` is expected and does **not** mean the visitor is blocked. The Private Access Token flow is an optimization used to reduce challenge steps. When a token is unavailable, Cloudflare falls back to a standard challenge and the visitor continues through the Challenge Page as usual.

If you are inspecting network requests in your browser's developer tools and notice a `401` on a `/cdn-cgi/challenge-platform/.../pat/...` request, you can safely disregard it. It is part of normal challenge processing and is not the cause of a block.

[PreviousChallenge solve rate (CSR)](https://developers.cloudflare.com/cloudflare-challenges/reference/challenge-solve-rate/)[NextSupported browsers](https://developers.cloudflare.com/cloudflare-challenges/reference/supported-browsers/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-challenges/reference/private-access-tokens.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
