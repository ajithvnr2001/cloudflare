---
url: https://developers.cloudflare.com/changelog/post/2025-03-06-r2-bucket-locks/
title: Set retention polices for your R2 bucket with bucket locks \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:54.180015+00:00
---

# Set retention polices for your R2 bucket with bucket locks · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-03-06-r2-bucket-locks/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 6, 2025

## Set retention polices for your R2 bucket with bucket locks

[R2](https://developers.cloudflare.com/r2/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now use [bucket locks](https://developers.cloudflare.com/r2/buckets/bucket-locks/) to set retention policies on your [R2 buckets](https://developers.cloudflare.com/r2/buckets/) (or specific prefixes within your buckets) for a specified period — or indefinitely. This can help ensure compliance by protecting important data from accidental or malicious deletion.

Locks give you a few ways to ensure your objects are retained (not deleted or overwritten). You can:

  * Lock objects for a specific duration, for example 90 days.
  * Lock objects until a certain date, for example January 1, 2030.
  * Lock objects indefinitely, until the lock is explicitly removed.



Buckets can have up to 1,000 [bucket lock rules](https://developers.cloudflare.com/r2/buckets/). Each rule specifies which objects it covers (via prefix) and how long those objects must remain retained.

Here are a couple of examples showing how you can configure bucket lock rules using [Wrangler](https://developers.cloudflare.com/workers/wrangler/):

#### Ensure all objects in a bucket are retained for at least 180 days
    
    
    npx wrangler r2 bucket lock add <bucket> --name 180-days-all --retention-days 180

#### Prevent deletion or overwriting of all logs indefinitely (via prefix)
    
    
    npx wrangler r2 bucket lock add <bucket> --name indefinite-logs --prefix logs/ --retention-indefinite

For more information on bucket locks and how to set retention policies for objects in your R2 buckets, refer to our [documentation](https://developers.cloudflare.com/r2/buckets/bucket-locks/).
