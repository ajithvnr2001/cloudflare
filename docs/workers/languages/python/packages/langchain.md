---
url: https://developers.cloudflare.com/workers/languages/python/packages/langchain/
title: Langchain \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:32.627168+00:00
---

# Langchain · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/languages/python/packages/langchain/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Languages](https://developers.cloudflare.com/workers/languages/)[Python Workers](https://developers.cloudflare.com/workers/languages/python/)

  4. /[Packages](https://developers.cloudflare.com/workers/languages/python/packages/)
  5. /Langchain



# Langchain

Last updated Aug 26, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/languages/python/packages/langchain/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewGet Started Example code

[LangChain ↗︎](https://www.langchain.com/) is the most popular framework for building AI applications powered by large language models (LLMs).

LangChain publishes multiple Python packages. The following are provided by the Workers runtime:

  * [`langchain` ↗︎](https://pypi.org/project/langchain/) (version `0.1.8`)
  * [`langchain-core` ↗︎](https://pypi.org/project/langchain-core/) (version `0.1.25`)
  * [`langchain-openai` ↗︎](https://pypi.org/project/langchain-openai/) (version `0.0.6`)



## Get Started

Clone the `cloudflare/python-workers-examples` repository and run the LangChain example:
    
    
    git clone https://github.com/cloudflare/python-workers-examples
    cd python-workers-examples/langchain
    uv run pywrangler dev

### Example code
    
    
    from workers import WorkerEntrypoint, Response
    from langchain_core.prompts import PromptTemplate
    from langchain_openai import OpenAI
    
    class Default(WorkerEntrypoint):
        async def fetch(self, request):
            prompt = PromptTemplate.from_template("Complete the following sentence: I am a {profession} and ")
            llm = OpenAI(api_key=self.env.API_KEY)
            chain = prompt | llm
    
            res = await chain.ainvoke({"profession": "electrician"})
            return Response(res.split(".")[0].strip())

[PreviousAgents SDK ↗︎](https://developers.cloudflare.com/agents/)[NextConnect to databases](https://developers.cloudflare.com/workers/databases/connecting-to-databases/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/languages/python/packages/langchain.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
