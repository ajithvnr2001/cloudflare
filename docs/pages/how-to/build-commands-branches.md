---
url: https://developers.cloudflare.com/pages/how-to/build-commands-branches/
title: Set build commands per branch \u00b7 Cloudflare Pages docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:35.236779+00:00
---

# Set build commands per branch · Cloudflare Pages docs

> Source: https://developers.cloudflare.com/pages/how-to/build-commands-branches/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Pages](https://developers.cloudflare.com/pages/)
  3. /How to
  4. /Set build commands per branch



# Set build commands per branch

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/pages/how-to/build-commands-branches/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSet upPublish your changes

This guide will instruct you how to set build commands on specific branches. You will use the `CF_PAGES_BRANCH` environment variable to run a script on a specified branch as opposed to your Production branch. This guide assumes that you have a Cloudflare account and a Pages project.

## Set up

Create a `.sh` file in your project directory. You can choose your file's name, but we recommend you name the file `build.sh`.

In the following script, you will use the `CF_PAGES_BRANCH` environment variable to check which branch is currently being built. Populate your `.sh` file with the following:
    
    
    # !/bin/bash
    
    if [ "$CF_PAGES_BRANCH" == "production" ]; then
      # Run the "production" script in `package.json` on the "production" branch
      # "production" should be replaced with the name of your Production branch
    
      npm run production
    
    elif [ "$CF_PAGES_BRANCH" == "staging" ]; then
      # Run the "staging" script in `package.json` on the "staging" branch
      # "staging" should be replaced with the name of your specific branch
    
      npm run staging
    
    else
      # Else run the dev script
      npm run dev
    fi

## Publish your changes

To put your changes into effect:

  1. In the Cloudflare dashboard, go to the **Workers & Pages** page.

[ Go to **Workers & Pages** ↗ ](https://dash.cloudflare.com/?to=/:account/workers-and-pages)
  2. Select your Pages project.

  3. Go to **Settings** > **Build & deployments** > **Build configurations** > **Edit configurations**.

  4. Update the **Build command** field value to `bash build.sh` and select **Save**.




To test that your build is successful, deploy your project.

[PreviousRedirecting www to domain apex](https://developers.cloudflare.com/pages/how-to/www-redirect/)[NextUse Direct Upload with continuous integration](https://developers.cloudflare.com/pages/how-to/use-direct-upload-with-continuous-integration/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/pages/how-to/build-commands-branches.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
