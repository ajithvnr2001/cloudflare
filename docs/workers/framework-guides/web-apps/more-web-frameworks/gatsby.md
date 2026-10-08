---
url: https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/gatsby/
title: Gatsby \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:27.940390+00:00
---

# Gatsby · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/gatsby/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

Framework guidesWeb applications

  4. /More guides...
  5. /Gatsby



# Gatsby

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/gatsby/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview1\. Set up a new project2\. Develop locally3\. Deploy your Project

In this guide, you will create a new [Gatsby ↗︎](https://www.gatsbyjs.com/) application and deploy to Cloudflare Workers (with the new [Workers Assets](https://developers.cloudflare.com/workers/static-assets/)).

## 1\. Set up a new project

Use the [`create-cloudflare` ↗︎](https://www.npmjs.com/package/create-cloudflare) CLI (C3) to set up a new project. C3 will create a new project directory, initiate Gatsby's official setup tool, and provide the option to deploy instantly.

To use `create-cloudflare` to create a new Gatsby project with Workers Assets, run the following command:

npmyarnpnpm
    
    
    npm create cloudflare@latest -- my-gatsby-app --framework=gatsby
    
    
    yarn create cloudflare my-gatsby-app --framework=gatsby
    
    
    pnpm create cloudflare@latest my-gatsby-app --framework=gatsby

After setting up your project, change your directory by running the following command:
    
    
    cd my-gatsby-app

## 2\. Develop locally

After you have created your project, run the following command in the project directory to start a local server. This will allow you to preview your project locally during development.

npmyarnpnpm
    
    
    npm run dev
    
    
    yarn run dev
    
    
    pnpm run dev

## 3\. Deploy your Project

Your project can be deployed to a `*.workers.dev` subdomain or a [Custom Domain](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/), from your own machine or from any CI/CD system, including [Cloudflare's own](https://developers.cloudflare.com/workers/ci-cd/builds/).

The following command will build and deploy your project. If you're using CI, ensure you update your ["deploy command"](https://developers.cloudflare.com/workers/ci-cd/builds/configuration/#build-settings) configuration appropriately.

npmyarnpnpm
    
    
    npm run deploy
    
    
    yarn run deploy
    
    
    pnpm run deploy

[PreviousDocusaurus](https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/docusaurus/)[NextHono](https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/hono/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/framework-guides/web-apps/more-web-frameworks/gatsby.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
