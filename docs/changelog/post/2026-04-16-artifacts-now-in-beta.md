---
url: https://developers.cloudflare.com/changelog/post/2026-04-16-artifacts-now-in-beta/
title: Artifacts now in beta: versioned filesystem with Git access \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:40.227742+00:00
---

# Artifacts now in beta: versioned filesystem with Git access · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-16-artifacts-now-in-beta/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 16, 2026

## Artifacts now in beta: versioned filesystem with Git access

[Artifacts](https://developers.cloudflare.com/artifacts/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

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
