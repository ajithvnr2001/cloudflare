---
url: https://developers.cloudflare.com/workers-ai/get-started/dashboard/
title: Get started - Dashboard \u00b7 Cloudflare Workers AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:59.080332+00:00
---

# Get started - Dashboard · Cloudflare Workers AI docs

> Source: https://developers.cloudflare.com/workers-ai/get-started/dashboard/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers AI](https://developers.cloudflare.com/workers-ai/)
  3. /[Getting started](https://developers.cloudflare.com/workers-ai/get-started/)
  4. /Dashboard



# Dashboard

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers-ai/get-started/dashboard/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesSetupDevelopment Dashboard Wrangler CLI

Follow this guide to create a Workers AI application using the Cloudflare dashboard.

## Prerequisites

Sign up for a [Cloudflare account ↗︎](https://dash.cloudflare.com/sign-up/workers-and-pages) if you have not already.

## Setup

To create a Workers AI application:

  1. In the Cloudflare dashboard, go to the **Workers & Pages** page.

[ Go to **Workers & Pages** ↗ ](https://dash.cloudflare.com/?to=/:account/workers-and-pages)
  2. Select **Create application**.

  3. Under **Select a template** , select **LLM Chat App**.

  4. Select **Deploy**.

  5. Name your Worker, then select **Create and deploy**.

  6. Preview your Worker at its provided [`workers.dev`](https://developers.cloudflare.com/workers/configuration/routing/workers-dev/) subdomain.




## Development

### Dashboard

Editing in the dashboard is helpful for simpler use cases.

Once you have created your Worker script, you can edit and deploy your Worker using the Cloudflare dashboard:

  1. In the Cloudflare dashboard, go to the **Workers & Pages** page.

[ Go to **Workers & Pages** ↗ ](https://dash.cloudflare.com/?to=/:account/workers-and-pages)
  2. Select your application.

  3. Select **Edit Code**.


![Edit code directly within the Cloudflare dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=566,height=386,format=webp/_astro/workers-edit-code.CKxxvQSe.png)

### Wrangler CLI

To develop more advanced applications or [implement tests](https://developers.cloudflare.com/workers/testing/), start working in the Wrangler CLI.

  1. Install [`npm` ↗︎](https://docs.npmjs.com/getting-started).
  2. Install [`Node.js` ↗︎](https://nodejs.org/en/).



Node.js version manager

Use a Node version manager like [Volta ↗︎](https://volta.sh/) or [nvm ↗︎](https://github.com/nvm-sh/nvm) to avoid permission issues and change Node.js versions. [Wrangler](https://developers.cloudflare.com/workers/wrangler/install-and-update/), discussed later in this guide, requires a Node version of `16.17.0` or later.

  3. Run the following command, replacing the value of `[<DIRECTORY>]` which the location you want to put your Worker Script.



npmyarnpnpm
    
    
    npm create cloudflare@latest -- [<DIRECTORY>] --type=pre-existing
    
    
    yarn create cloudflare [<DIRECTORY>] --type=pre-existing
    
    
    pnpm create cloudflare@latest [<DIRECTORY>] --type=pre-existing

After you run this command - and work through the prompts - your local changes will not automatically sync with dashboard. So, once you download your script, continue using the CLI.

[PreviousREST API](https://developers.cloudflare.com/workers-ai/get-started/rest-api/)[NextModels](https://developers.cloudflare.com/workers-ai/models/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers-ai/get-started/dashboard.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
