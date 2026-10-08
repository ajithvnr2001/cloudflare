---
url: https://developers.cloudflare.com/agents/platform/limits/
title: Limits \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:17.318093+00:00
---

# Limits · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/platform/limits/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /Platform
  4. /Limits



# Limits

Last updated Jun 3, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/agents/platform/limits/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Limits that apply to authoring, deploying, and running Agents are detailed below.

Many limits are inherited from those applied to Workers scripts and/or Durable Objects, and are detailed in the [Workers limits](https://developers.cloudflare.com/workers/platform/limits/) documentation.

Feature | Limit  
---|---  
Max concurrent (running) Agents per account | Tens of millions+ 1  
Max definitions per account | ~250,000+ 2  
Max state stored per unique Agent | 1 GB  
Max compute time per Agent | 30 seconds (refreshed per HTTP request / incoming WebSocket message) 3  
Duration (wall clock) per step 3 | Unlimited (for example, waiting on a database call or an LLM response)  
  
* * *

Need a higher limit?

To request an adjustment to a limit, complete the [Limit Increase Request Form ↗︎](https://forms.gle/eX6pXvit1wBv77Yw5). If the limit can be increased, Cloudflare will contact you with next steps.

## Footnotes

  1. Yes, really. You can have tens of millions of Agents running concurrently, as each Agent is mapped to a [unique Durable Object](https://developers.cloudflare.com/durable-objects/concepts/what-are-durable-objects/) (actor). ↩

  2. You can deploy up to [500 scripts per account](https://developers.cloudflare.com/workers/platform/limits/), but each script (project) can define multiple Agents. Each deployed script can be up to 10 MB on the [Workers Paid Plan](https://developers.cloudflare.com/workers/platform/pricing/#workers) ↩

  3. Compute (CPU) time per Agent is limited to 30 seconds, but this is refreshed when an Agent receives a new HTTP request, runs a [scheduled task](https://developers.cloudflare.com/agents/runtime/execution/schedule-tasks/), or an incoming WebSocket message. ↩ ↩2




[PreviousCode Mode MCP server patterns](https://developers.cloudflare.com/agents/model-context-protocol/codemode/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/platform/limits.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
