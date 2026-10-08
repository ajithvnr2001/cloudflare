---
url: https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/angular/
title: Angular \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:27.740625+00:00
---

# Angular · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/angular/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

Framework guidesWeb applications

  4. /More guides...
  5. /Angular



# Angular

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/angular/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview1\. Set up a new project2\. Develop locally3\. Deploy your ProjectStatic assets

In this guide, you will create a new [Angular ↗︎](https://angular.dev/) application and deploy to Cloudflare Workers (with the new [Workers Assets](https://developers.cloudflare.com/workers/static-assets/)).

Automatic configuration

Run `wrangler deploy` in a project without a Wrangler configuration file and Wrangler will automatically detect Angular, generate the necessary configuration, and deploy your project.

npmyarnpnpm
    
    
    npx wrangler deploy
    
    
    yarn wrangler deploy
    
    
    pnpm wrangler deploy

Learn more about [automatic project configuration](https://developers.cloudflare.com/workers/framework-guides/automatic-configuration/).

AngularDetected

Generated configuration

wrangler.jsonc

assets:directory: dist/browser

wrangler.jsonc

observability:enabled: true

WorkersDeployed

Wrangler handles configuration automatically

## 1\. Set up a new project

Use the [`create-cloudflare` ↗︎](https://www.npmjs.com/package/create-cloudflare) CLI (C3) to set up a new project. C3 will create a new project directory, initiate Angular's official setup tool, and provide the option to deploy instantly.

To use `create-cloudflare` to create a new Angular project with Workers Assets, run the following command:

npmyarnpnpm
    
    
    npm create cloudflare@latest -- my-angular-app --framework=angular
    
    
    yarn create cloudflare my-angular-app --framework=angular
    
    
    pnpm create cloudflare@latest my-angular-app --framework=angular

After setting up your project, change your directory by running the following command:
    
    
    cd my-angular-app

## 2\. Develop locally

After you have created your project, run the following command in the project directory to start a local server. This will allow you to preview your project locally during development.

npmyarnpnpm
    
    
    npm run start
    
    
    yarn run start
    
    
    pnpm run start

## 3\. Deploy your Project

Your project can be deployed to a `*.workers.dev` subdomain or a [Custom Domain](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/), from your own machine or from any CI/CD system, including [Cloudflare's own](https://developers.cloudflare.com/workers/ci-cd/builds/).

The following command will build and deploy your project. If you're using CI, ensure you update your ["deploy command"](https://developers.cloudflare.com/workers/ci-cd/builds/configuration/#build-settings) configuration appropriately.

npmyarnpnpm
    
    
    npm run deploy
    
    
    yarn run deploy
    
    
    pnpm run deploy

* * *

## Static assets

By default, Cloudflare first tries to match a request path against a static asset path, which is based on the file structure of the uploaded asset directory. This is either the directory specified by `assets.directory` in your Wrangler config or, in the case of the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/), the output directory of the client build. Failing that, we invoke a Worker if one is present. If there is no Worker, or the Worker then uses the asset binding, Cloudflare will fallback to the behaviour set by [`not_found_handling`](https://developers.cloudflare.com/workers/static-assets/#routing-behavior).

Refer to the [routing documentation](https://developers.cloudflare.com/workers/static-assets/routing/) for more information about how routing works with static assets, and how to customize this behavior.

[PreviousAnalog](https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/analog/)[NextDocusaurus](https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/docusaurus/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/framework-guides/web-apps/more-web-frameworks/angular.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
