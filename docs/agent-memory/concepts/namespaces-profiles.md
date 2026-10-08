---
url: https://developers.cloudflare.com/agent-memory/concepts/namespaces-profiles/
title: Namespaces and profiles \u00b7 Cloudflare Agent Memory docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:05.694574+00:00
---

# Namespaces and profiles · Cloudflare Agent Memory docs

> Source: https://developers.cloudflare.com/agent-memory/concepts/namespaces-profiles/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agent Memory](https://developers.cloudflare.com/agent-memory/)
  3. /Concepts
  4. /Namespaces and profiles



# Namespaces and profiles

Last updated Jun 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/agent-memory/concepts/namespaces-profiles/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewNamespacesProfilesSessionsIsolation model

Agent Memory uses a two-level isolation model: **namespaces** define memory domains, and **profiles** provide isolated memory stores for individual users, agents, teams, tenants, or application objects.

## Namespaces

A namespace is a top-level container that scopes a set of memory profiles. Use namespaces to separate applications, environments, tenants, or memory layers such as user, team, and organization memory.

## Profiles

A profile is an isolated memory store for a single entity. Each profile has its own stored memories and retrieval indexes.

## Sessions

A session groups memories that come from the same interaction or conversation. Sessions are optional, but they make it easier to identify, inspect, and manage memories created from a specific conversation.

Sessions are scoped to a profile. Two different profiles can use the same session ID without conflict.

## Isolation model

Conceptually, memories are scoped as `namespace > profile > memory`. No data crosses these boundaries:
    
    
    Namespace: my-assistant-prod
      Profile: alice
        Memories
        Messages
      Profile: bob
        Memories
        Messages

A `recall()` on Alice's profile never returns memories from Bob's profile. Each profile is a self-contained memory system.

[PreviousHow Agent Memory works](https://developers.cloudflare.com/agent-memory/concepts/how-agent-memory-works/)[NextWorkers API](https://developers.cloudflare.com/agent-memory/api/workers-api/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agent-memory/concepts/namespaces-profiles.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
