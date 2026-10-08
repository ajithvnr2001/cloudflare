---
url: https://developers.cloudflare.com/changelog/post/2025-04-10-d1-read-replication-beta/
title: D1 Read Replication Public Beta \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:09.537769+00:00
---

# D1 Read Replication Public Beta · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-04-10-d1-read-replication-beta/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 10, 2025

## D1 Read Replication Public Beta

[D1](https://developers.cloudflare.com/d1/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-10-d1-read-replication-beta/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

D1 read replication is available in public beta to help lower average latency and increase overall throughput for read-heavy applications like e-commerce websites or content management tools.

Workers can leverage read-only database copies, called read replicas, by using D1 [Sessions API](https://developers.cloudflare.com/d1/best-practices/read-replication). A session encapsulates all the queries from one logical session for your application. For example, a session may correspond to all queries coming from a particular web browser session. With Sessions API, D1 queries in a session are guaranteed to be [sequentially consistent](https://developers.cloudflare.com/d1/best-practices/read-replication/#replica-lag-and-consistency-model) to avoid data consistency pitfalls. D1 [bookmarks](https://developers.cloudflare.com/d1/reference/time-travel/#bookmarks) can be used from a previous session to ensure logical consistency between sessions.
    
    
    // retrieve bookmark from previous session stored in HTTP header
    const bookmark = request.headers.get("x-d1-bookmark") ?? "first-unconstrained";
    
    const session = env.DB.withSession(bookmark);
    const result = await session
    	.prepare(`SELECT * FROM Customers WHERE CompanyName = 'Bs Beverages'`)
    	.run();
    // store bookmark for a future session
    response.headers.set("x-d1-bookmark", session.getBookmark() ?? "");

Read replicas are automatically created by Cloudflare (currently one in each supported [D1 region](https://developers.cloudflare.com/d1/best-practices/read-replication/#read-replica-locations)), are active/inactive based on query traffic, and are transparently routed to by Cloudflare at no additional cost.

To checkout D1 read replication, deploy the following Worker code using Sessions API, which will prompt you to create a D1 database and enable read replication on said database.

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/d1-starter-sessions-api)

To learn more about how read replication was implemented, go to our [blog post ↗︎](https://blog.cloudflare.com/d1-read-replication-beta).
