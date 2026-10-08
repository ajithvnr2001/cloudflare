---
url: https://developers.cloudflare.com/learning-paths/mtls/mtls-implementation/
title: Types of mTLS implementation \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:51.224151+00:00
---

# Types of mTLS implementation · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/mtls/mtls-implementation/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /Mtls
  4. /Types of mTLS implementation



# Types of mTLS implementation

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/mtls/mtls-implementation/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewOption 1: mTLS Device AuthenticationOption 2: mTLS User AuthenticationOption 3: mTLS Service Authentication

There are different ways to implement mTLS authentication. The most common ones are:

## Option 1: mTLS Device Authentication

This version of mTLS is for device certificates, primarily focused on the number of IoT devices, not user devices.

Here we recommend using [mTLS with Application Security](https://developers.cloudflare.com/learning-paths/mtls/mtls-app-security/).

## Option 2: mTLS User Authentication

When a user wants to establish a secure connection with a server, they present their certificate to the server, which verifies its authenticity. Once the certificate is authenticated, an encrypted connection is established between the user and the server, and all data transmitted between them is encrypted to protect against interception by third parties.

mTLS user authentication is included with Cloudflare Access and depends on the number of users.

## Option 3: mTLS Service Authentication

The hostnames are used to look up the certificates and verify their authenticity. Once the connection is established, all data transmitted between the hosts is encrypted, ensuring that it cannot be intercepted and read by third parties. Here the main driver is the number of hostnames.

[PreviousmTLS with Cloudflare Access](https://developers.cloudflare.com/learning-paths/mtls/mtls-cloudflare-access/)[NextmTLS with Workers](https://developers.cloudflare.com/learning-paths/mtls/mtls-workers/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/mtls/mtls-implementation/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
