---
url: https://developers.cloudflare.com/changelog/post/2026-04-29-hyperdrive-vpc-private-databases/
title: Hyperdrive support for private databases with Workers VPC \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:50.110626+00:00
---

# Hyperdrive support for private databases with Workers VPC · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-29-hyperdrive-vpc-private-databases/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 29, 2026

## Hyperdrive support for private databases with Workers VPC

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-29-hyperdrive-vpc-private-databases/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now connect Hyperdrive to a private database through a [Workers VPC service](https://developers.cloudflare.com/workers-vpc/). This is the recommended way to connect Hyperdrive to a private database that is not exposed to the public Internet.

When creating a Hyperdrive configuration in the Cloudflare dashboard, choose **Connect to private database** and then **Workers VPC**. From there, you can select an existing VPC service or create a new one inline by picking a Cloudflare Tunnel and entering your origin host and TCP port.

You can also create a Hyperdrive configuration backed by a Workers VPC service from the command line:
    
    
    npx wrangler hyperdrive create my-vpc-database \
      --service-id <YOUR_VPC_SERVICE_ID> \
      --database <DATABASE_NAME> \
      --user <DATABASE_USER> \
      --password <DATABASE_PASSWORD> \
      --scheme postgresql

Workers VPC services are reusable across Hyperdrive configurations and can also be bound directly to Workers, so you can share the same private connection across multiple products.

To get started, refer to [Connect Hyperdrive to a private database using Workers VPC](https://developers.cloudflare.com/hyperdrive/configuration/connect-to-private-database-vpc/).
