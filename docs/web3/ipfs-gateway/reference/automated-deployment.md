---
url: https://developers.cloudflare.com/web3/ipfs-gateway/reference/automated-deployment/
title: Automated deployments \u00b7 Cloudflare Web3 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:55.936887+00:00
---

# Automated deployments · Cloudflare Web3 docs

> Source: https://developers.cloudflare.com/web3/ipfs-gateway/reference/automated-deployment/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Web3](https://developers.cloudflare.com/web3/)
  3. /…

[IPFS Gateway](https://developers.cloudflare.com/web3/ipfs-gateway/)

  4. /[Reference](https://developers.cloudflare.com/web3/ipfs-gateway/reference/)
  5. /Automated deployments



# Automated deployments

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/web3/ipfs-gateway/reference/automated-deployment/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Static sites are easy to deploy automatically. The code of the site is usually kept in a Git repository and deployed by pushing the latest commit to a repository that's connected to a Continuous Integration service like [Travis CI ↗︎](https://travis-ci.org/), or by pushing to a repository directly on the server and activating a post-receive hook. Either way, the production version of the site is built and then copied into the serving path of an Apache or NGINX instance.

IPFS usually fits into these systems: instead of copying the production version of a website into the serving path of an HTTP server, you would upload the same files to an IPFS node and update your DNS records with the new hash. There are several tools that help with different parts of this:

  * [ipfs-deploy ↗︎](https://github.com/agentofuser/ipfs-deploy) helps upload data to a third-party pinning providers and automatically update Cloudflare-managed DNS records.
  * [dnslink-cloudflare ↗︎](https://github.com/ipfs-shipyard/dnslink-cloudflare) is a script to programmatically update DNSLink records. This can be run with the `-Q` flag of `ipfs add` that only outputs the top-level hash.
  * [Fission's IPFS support ↗︎](https://guide.fission.codes/developers/custom-domains/using-cloudflare-ipfs-gateway) lets you use the Fission IPFS app publishing system from the CLI or from GitHub Actions, while using Cloudflare-managed DNS and gateway.



[PreviousUsing IPFS with your website](https://developers.cloudflare.com/web3/ipfs-gateway/reference/updating-for-ipfs/)[NextTroubleshooting](https://developers.cloudflare.com/web3/ipfs-gateway/troubleshooting/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/web3/ipfs-gateway/reference/automated-deployment.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
