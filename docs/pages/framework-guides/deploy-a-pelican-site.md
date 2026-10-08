---
url: https://developers.cloudflare.com/pages/framework-guides/deploy-a-pelican-site/
title: Pelican \u00b7 Cloudflare Pages docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:30.771887+00:00
---

# Pelican · Cloudflare Pages docs

> Source: https://developers.cloudflare.com/pages/framework-guides/deploy-a-pelican-site/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Pages](https://developers.cloudflare.com/pages/)
  3. /Framework guides
  4. /Pelican



# Pelican

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/pages/framework-guides/deploy-a-pelican-site/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate a Pelican projectBefore you continueCreate a GitHub repositoryDeploy with Cloudflare PagesLearn more

[Pelican ↗︎](https://docs.getpelican.com) is a static site generator, written in Python. With Pelican, you can write your content directly with your editor of choice in reStructuredText or Markdown formats.

## Create a Pelican project

To begin, create a Pelican project directory. `cd` into your new directory and run:
    
    
    python3 -m pip install pelican

Then run:
    
    
    pip freeze > requirements.txt

Create a directory in your project named `content`:
    
    
    mkdir content

This is the directory name that you will set in the build command.

## Before you continue

All of the framework guides assume you already have a fundamental understanding of [Git ↗︎](https://git-scm.com/). If you are new to Git, refer to this [summarized Git handbook ↗︎](https://guides.github.com/introduction/git-handbook/) on how to set up Git on your local machine.

If you clone with SSH, you must [generate SSH keys ↗︎](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) on each computer you use to push or pull from GitHub.

Refer to the [GitHub documentation ↗︎](https://guides.github.com/introduction/git-handbook/) and [Git documentation ↗︎](https://git-scm.com/book/en/v2) for more information.

## Create a GitHub repository

Create a new GitHub repository by visiting [repo.new ↗︎](https://repo.new). After creating a new repository, go to your newly created project directory to prepare and push your local application to GitHub by running the following commands in your terminal:
    
    
    git init
    git remote add origin https://github.com/<your-gh-username>/<repository-name>
    git add .
    git commit -m "Initial commit"
    git branch -M main
    git push -u origin main

## Deploy with Cloudflare Pages

To deploy your site to Pages:

  1. In the Cloudflare dashboard, go to the **Workers & Pages** page.

[ Go to **Workers & Pages** ↗ ](https://dash.cloudflare.com/?to=/:account/workers-and-pages)
  2. Select **Create application**.

  3. Select the **Pages** tab.

  4. Select **Import an existing Git repository**.

  5. Select the new GitHub repository that you created and then select **Begin setup**.

  6. In the **Set up builds and deployments** section, provide the following information:


Configuration option| Value| Production branch| `main`  
---|---  
Build command| `pelican content`  
Build directory| `output`  
  
  7. Select **Environment variables (advanced)** and set the `PYTHON_VERSION` variable with the value of `3.7`.



For the complete guide to deploying your first site to Cloudflare Pages, refer to the [Get started guide](https://developers.cloudflare.com/pages/get-started/).

After deploying your site, you will receive a unique subdomain for your project on `*.pages.dev`.

Every time you commit new code to your Pelican site, Cloudflare Pages will automatically rebuild your project and deploy it. You will also get access to [preview deployments](https://developers.cloudflare.com/pages/configuration/preview-deployments/) on new pull requests and be able to preview how changes look to your site before deploying them to production.

## Learn more

By completing this guide, you have successfully deployed your Pelican site to Cloudflare Pages. To get started with other frameworks, [refer to the list of Framework guides](https://developers.cloudflare.com/pages/framework-guides/).

[PreviousNuxt](https://developers.cloudflare.com/pages/framework-guides/deploy-a-nuxt-site/)[NextPreact](https://developers.cloudflare.com/pages/framework-guides/deploy-a-preact-site/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/pages/framework-guides/deploy-a-pelican-site.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
