---
url: https://developers.cloudflare.com/hyperdrive/examples/python-workers/
title: Python Workers \u00b7 Cloudflare Hyperdrive docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:32.774288+00:00
---

# Python Workers · Cloudflare Hyperdrive docs

> Source: https://developers.cloudflare.com/hyperdrive/examples/python-workers/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)
  3. /Examples
  4. /Python Workers



# Python Workers

Last updated Sep 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/hyperdrive/examples/python-workers/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSupported drivers PostgreSQL MySQLConnect to your databaseLimitations and compatibility Socket support Concurrency and async safety SQLAlchemy support

You can use Hyperdrive with [Python Workers](https://developers.cloudflare.com/workers/languages/python/). To use Hyperdrive with Python Workers, set your compatibility date to `2026-09-08` or later.

## Supported drivers

Hyperdrive in Python Workers uses [TCP socket support](https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/#connect) to establish database connections. While you can use any Python driver that works with TCP connections, we strongly recommend using the drivers in the tables below, as they have been tested and verified to work with Hyperdrive.

### PostgreSQL

Driver | Documentation  
---|---  
`asyncpg` (recommended) | [asyncpg documentation ↗︎](https://magicstack.github.io/asyncpg/current/)  
`pg8000` | [pg8000 documentation ↗︎](https://codeberg.org/tlocke/pg8000)  
`psycopg` | [psycopg documentation ↗︎](https://www.psycopg.org/psycopg3/docs/index.html)  
  
### MySQL

Driver | Documentation  
---|---  
`aiomysql` (recommended) | [aiomysql documentation ↗︎](https://aiomysql.readthedocs.io/en/latest/)  
`pymysql` | [pymysql documentation ↗︎](https://pymysql.readthedocs.io/)  
  
## Connect to your database

Before you begin, [create a Python Worker](https://developers.cloudflare.com/workers/languages/python/#the-pywrangler-cli-tool) and [create a Hyperdrive configuration](https://developers.cloudflare.com/hyperdrive/get-started/) for your database.

  1. Add the Hyperdrive binding to your [Wrangler configuration](https://developers.cloudflare.com/workers/wrangler/configuration/). Replace `<HYPERDRIVE_CONFIG_ID>` with your configuration ID.
         
         {
           "$schema": "./node_modules/wrangler/config-schema.json",
           "name": "python-hyperdrive",
           "main": "src/main.py",
           // Set this to today's date
           "compatibility_date": "2026-10-08",
           "compatibility_flags": [
             "python_workers"
           ],
           "hyperdrive": [
             {
               "binding": "HYPERDRIVE",
               "id": "<HYPERDRIVE_CONFIG_ID>"
             }
           ]
         }
         
         name = "python-hyperdrive"
         main = "src/main.py"
         # Set this to today's date
         compatibility_date = "2026-10-08"
         compatibility_flags = ["python_workers"]
         
         [[hyperdrive]]
         binding = "HYPERDRIVE"
         id = "<HYPERDRIVE_CONFIG_ID>"

  2. Install your driver and replace `src/main.py` with the corresponding example.
         
         [project]
         dependencies = [
             "asyncpg",
         ]

src/main.pypython
         
         from contextlib import closing
         
         import asyncpg
         from workers import Response, WorkerEntrypoint
         
         class Default(WorkerEntrypoint):
             async def fetch(self, request):
                 hd = self.env.HYPERDRIVE
                 connection = await asyncpg.connect(
                     host=hd.host,
                     port=int(hd.port),
                     user=hd.user,
                     password=hd.password,
                     database=hd.database,
                     ssl=False,
                 )
                 await connection.execute("SELECT 1")
                 await connection.close()
         
         [project]
         dependencies = [
             "aiomysql",
         ]

src/main.pypython
         
         import aiomysql
         from workers import Response, WorkerEntrypoint
         
         
         class Default(WorkerEntrypoint):
             async def fetch(self, request):
                 hd = self.env.HYPERDRIVE
                 connection = await aiomysql.connect(
                     host=hd.host,
                     port=int(hd.port),
                     user=hd.user,
                     password=hd.password,
                     db=hd.database,
                     ssl=None,
                 )
                 try:
                     cursor = await connection.cursor()
                     await cursor.execute("SELECT 1")
                     result = await cursor.fetchone()
                     return Response.json({"result": result[0]})
                 finally:
                     connection.close()

  3. Deploy your Worker:
         
         uv run pywrangler deploy




## Limitations and compatibility

### Socket support

TCP socket support in Python Workers internally uses the [`connect`](https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/#connect) API. While most standard library socket operations are supported, some low-level operations might not work as expected.

### Concurrency and async safety

Socket operations in Python Workers do not block the event loop. Although Python's native socket operations are synchronous, the underlying TCP socket implementation in Python Workers is asynchronous. This allows multiple requests to be processed concurrently while one request waits for a socket operation to complete.

To ensure synchronous database operations are serialized, use a lock to prevent concurrent access:
    
    
    import asyncio
    
    lock = asyncio.Lock()
    
    async with lock:
        # Your database operation here
        synchronous_db_operation()

### SQLAlchemy support

Currently, only synchronous SQLAlchemy ORMs are supported in Python Workers. Async SQLAlchemy ORMs are not yet supported due to a lack of greenlet support in the Python Workers environment.

[PreviousDrizzle ORM](https://developers.cloudflare.com/hyperdrive/examples/connect-to-mysql/mysql-drivers-and-libraries/drizzle-orm/)[NextTutorials](https://developers.cloudflare.com/hyperdrive/tutorials/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/hyperdrive/examples/python-workers.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
