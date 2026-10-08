---
url: https://developers.cloudflare.com/web3/ipfs-gateway/reference/updating-for-ipfs/
title: Using IPFS with your website \u00b7 Cloudflare Web3 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:55.998919+00:00
---

# Using IPFS with your website · Cloudflare Web3 docs

> Source: https://developers.cloudflare.com/web3/ipfs-gateway/reference/updating-for-ipfs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Web3](https://developers.cloudflare.com/web3/)
  3. /…

[IPFS Gateway](https://developers.cloudflare.com/web3/ipfs-gateway/)

  4. /[Reference](https://developers.cloudflare.com/web3/ipfs-gateway/reference/)
  5. /Using IPFS with your website



# Using IPFS with your website

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/web3/ipfs-gateway/reference/updating-for-ipfs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAngular, React, VueGatsbyJekyllGeneric

Though it is not required, it is strongly recommended that websites hosted on IPFS use only relative links, unless linking to a different domain. This is because data can be accessed in many different (but ultimately equivalent) ways:

  * From your custom domain: `https://ipfs.tech/index.html`
  * From a gateway: `https://cloudflare-ipfs.com/ipns/ipfs.tech/index.html`
  * By immutable hash: `https://cloudflare-ipfs.com/ipfs/QmNksJqvwHzNtAtYZVqFZFfdCVciY4ojTU2oFZQSFG9U7B/index.html`



Using only relative links within a web application supports all of these at once, and gives the most flexibility to the user. The exact method for switching to relative links, if you do not use them already, depends on the framework you use.

## Angular, React, Vue

These popular JavaScript frameworks are covered in a [blog post ↗︎](https://medium.com/pinata/how-to-easily-host-a-website-on-ipfs-9d842b5d6a01) from [Pinata ↗︎](https://pinata.cloud/). They are fixed with minor config changes.

## Gatsby

Gatsby is a JavaScript framework based on React. There is a [plugin ↗︎](https://www.gatsbyjs.org/packages/gatsby-plugin-ipfs/) for it that ensures links are relative.

## Jekyll

Add a file `_includes/base.html` with the contents:
    
    
    {% assign base = '' %}
    {% assign depth = page.url | split: '/' | size | minus: 1 %}
    {% if    depth <= 1 %}{% assign base = '.' %}
    {% elsif depth == 2 %}{% assign base = '..' %}
    {% elsif depth == 3 %}{% assign base = '../..' %}
    {% elsif depth == 4 %}{% assign base = '../../..' %}{% endif %}

This snippet computes the relative path back to the root of the website from the current page. Update any pages that need to link to the root by adding this at the top:
    
    
    {%- include base.html -%}

This snippet also prefixing any links with `{{base}}`. So for example, we would change `href="/css/main.css"` to be `href="{{base}}/css/main.css"`

## Generic

For other frameworks, or if a framework was not used, there's a script called [make-relative ↗︎](https://github.com/tmcw/make-relative) that will parse the HTML of a website and automatically rewrite links and images to be relative.

[PreviousPeering](https://developers.cloudflare.com/web3/ipfs-gateway/reference/peering-with-content-providers/)[NextAutomated deployments](https://developers.cloudflare.com/web3/ipfs-gateway/reference/automated-deployment/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/web3/ipfs-gateway/reference/updating-for-ipfs.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
