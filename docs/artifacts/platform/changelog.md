---
url: https://developers.cloudflare.com/artifacts/platform/changelog/
title: Changelog \u00b7 Cloudflare Artifacts docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:21.923202+00:00
---

# Changelog · Cloudflare Artifacts docs

> Source: https://developers.cloudflare.com/artifacts/platform/changelog/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Artifacts](https://developers.cloudflare.com/artifacts/)
  3. /Platform
  4. /Changelog



# Changelog

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/artifacts/platform/changelog/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/artifacts.xml)

## 2026-10-01

  
**Artifacts is now in open beta**  


[Artifacts](https://developers.cloudflare.com/artifacts/), Cloudflare's versioned file system that speaks Git, is now in open beta. Artifacts is built for scale, so you can create a repository per project, user, session, or task.

With Artifacts, you can:

  * **Deploy repositories to Workers** — Connect an Artifacts repository through [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/artifacts-integration/). Pushes to the production branch deploy the updated Worker, while other branches create or update [Worker Previews](https://developers.cloudflare.com/workers/previews/).
  * **Programmatically manage repositories** — Use an [Artifacts binding](https://developers.cloudflare.com/artifacts/api/workers-binding/) from a Worker to create or fork repos, inspect files and commits, read files by path, and issue repo-scoped Git tokens.
  * **React to repository changes** — [Subscribe to events](https://developers.cloudflare.com/artifacts/guides/event-subscriptions/) when a repository is created, imported, forked, deleted, pushed to, cloned, or fetched.
  * **Control where repository data is stored** — Choose to [store and process](https://developers.cloudflare.com/artifacts/guides/data-localization/) your data in the US or EU.
  * **Monitor repository usage** — View total operations, pulls, pushes, errors, and error rates in the Cloudflare dashboard or [via API for analytics](https://developers.cloudflare.com/artifacts/observability/metrics/).



Artifacts is available for customers on the Workers Paid plan. Cloudflare will begin [billing](https://developers.cloudflare.com/artifacts/platform/pricing/) for Artifacts on October 14, 2026.

#### Build the next GitHub on Cloudflare

We are hosting a competition to see who can build the next GitHub on Cloudflare using Workers and Artifacts.

[Apply today ↗︎](https://www.cloudflare.com/git-competition/) — submissions are open until October 14, 2026.

The first-place team will receive $25,000 in Cloudflare credits. The top three teams will be flown to San Francisco to present what they built at Cloudflare Connect.

Get started with the [Artifacts documentation](https://developers.cloudflare.com/artifacts/).

## 2026-08-13

  
**Data localization support for Artifacts**  


Artifacts now supports jurisdictions, allowing you to select the European Union or the United States as the only location where repo data is stored and processed.

Select a jurisdiction when you create a namespace. Every repo in that namespace automatically uses the selected jurisdiction.
    
    
    curl --request POST \
      "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/artifacts/namespaces" \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "namespace": "my-eu-namespace",
        "jurisdiction": "eu"
      }'

Jurisdictions cannot be changed after namespace creation. If you omit the jurisdiction, Artifacts creates an unrestricted namespace.

For supported jurisdictions and usage details, refer to [Data localization](https://developers.cloudflare.com/artifacts/guides/data-localization/).

## 2026-06-17

  
**Manage Artifacts from the Cloudflare dashboard**  


You can now configure [Artifacts](https://developers.cloudflare.com/artifacts/concepts/how-artifacts-works/) namespaces, repos, and tokens directly from the Cloudflare dashboard.

Artifacts is Git-compatible storage that lets you store repos on Cloudflare and interact with them using standard Git workflows.

You can view and create [namespaces](https://developers.cloudflare.com/artifacts/concepts/namespaces/#use-namespaces-as-containers), which are top-level containers for repos:

![Artifacts namespaces dashboard showing namespace search and create namespace controls](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1804,height=598,format=webp/_astro/dashboard-namespaces.0BJelWZh.png)

You can view, create, fork, and search repos within a namespace:

![Artifacts repositories dashboard showing repo source, access, and created columns](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1874,height=592,format=webp/_astro/dashboard-repositories.M9P9JUL_.png)

You can open a repo to view its files and copy its Git remote URL.

![Artifacts repository overview showing files, commits, token management, and quick actions](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2194,height=806,format=webp/_astro/dashboard-repo-overview.CSHxrCW2.png)

You can also provision tokens directly from the dashboard to scope Git access to a single repo, with read tokens for clone, fetch, and pull workflows, or write tokens when a client needs to push changes.

To get started, go to the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/) and select **Storage & databases** > **Artifacts**.

If you are enrolled in the Artifacts beta, you can use the dashboard to set up Artifacts. If you would like to join the beta, complete the [request form ↗︎](https://forms.gle/DwBoPRa3CWQ8ajFp7).

## 2026-05-18

  
**Manage Artifacts namespaces and repos with Wrangler CLI**  


You can now manage [Artifacts](https://developers.cloudflare.com/artifacts/) namespaces, repos, and repo-scoped tokens directly from Wrangler CLI.

Available commands:

  * `wrangler artifacts namespaces list` — List Artifacts namespaces in your account.
  * `wrangler artifacts namespaces get` — Get metadata for a namespace.
  * `wrangler artifacts repos create` — Create a repo in a namespace.
  * `wrangler artifacts repos list` — List repos in a namespace.
  * `wrangler artifacts repos get` — Get metadata for a repo.
  * `wrangler artifacts repos delete` — Delete a repo.
  * `wrangler artifacts repos issue-token` — Issue a repo-scoped token for Git access.



To get started, refer to the [Wrangler Artifacts commands documentation](https://developers.cloudflare.com/workers/wrangler/commands/artifacts/).

## 2026-04-16

  
**Artifacts now in beta: versioned filesystem with Git access**  


[Artifacts](https://developers.cloudflare.com/artifacts/) is now in private beta. Artifacts is Git-compatible storage built for scale: create tens of millions of repos, fork from any remote, and hand off a URL to any Git client. It provides a versioned filesystem for storing and exchanging file trees across Workers, the REST API, and any Git client, running locally or within an agent.

You can [read the announcement blog ↗︎](https://blog.cloudflare.com/artifacts-git-for-agents-beta/) to learn more about what Artifacts does, how it works, and how to create repositories for your agents to use.

Artifacts has three API surfaces:

  * Workers bindings (for creating and managing repositories)
  * REST API (for creating and managing repos from any other compute platform)
  * Git protocol (for interacting with repos)



As an example: you can use the Workers binding to create a repo and read back its remote URL:
    
    
    # Create a thousand, a million or ten million repos: one for every agent, for every upstream branch, or every user.
    const created = await env.PROD_ARTIFACTS.create("agent-007");
    const remote = (await created.repo.info())?.remote;

Or, use the REST API to create a repo inside a namespace from your agent(s) running on any platform:
    
    
    curl --request POST "https://artifacts.cloudflare.net/v1/api/namespaces/some-namespace/repos" --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" --header "Content-Type: application/json" --data '{"name":"agent-007"}'

Any Git client that speaks smart HTTP can use the returned remote URL:
    
    
    # Agents know git.
    # Every repository can act as a git repo, allowing agents to interact with Artifacts the way they know best: using the git CLI.
    git clone https://x:${REPO_TOKEN}@artifacts.cloudflare.net/some-namespace/agent-007.git

To learn more, refer to [Get started](https://developers.cloudflare.com/artifacts/get-started/), [Workers binding](https://developers.cloudflare.com/artifacts/api/workers-binding/), and [Git protocol](https://developers.cloudflare.com/artifacts/api/git-protocol/).

[PreviousLimits](https://developers.cloudflare.com/artifacts/platform/limits/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/artifacts/platform/changelog.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
