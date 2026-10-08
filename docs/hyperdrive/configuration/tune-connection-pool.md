---
url: https://developers.cloudflare.com/hyperdrive/configuration/tune-connection-pool/
title: Tune connection pooling \u00b7 Cloudflare Hyperdrive docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:29.788499+00:00
---

# Tune connection pooling · Cloudflare Hyperdrive docs

> Source: https://developers.cloudflare.com/hyperdrive/configuration/tune-connection-pool/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)
  3. /Configuration
  4. /Tune connection pooling



# Tune connection pooling

Last updated Jun 9, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/hyperdrive/configuration/tune-connection-pool/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigure connection pool sizeBest practicesRelated resources

Hyperdrive maintains a pool of connections to your database that are shared across Worker invocations. You can configure the maximum number of these connections based on your database capacity and application requirements.

Note

Hyperdrive does not have a limit on the number of concurrent _client_ connections made from your Workers to Hyperdrive.

Hyperdrive does have a limit of _origin_ connections that can be made from Hyperdrive to your database. These are shared across Workers, with each Worker using one of these connections over the course of a database transaction. Refer to [transaction pooling mode](https://developers.cloudflare.com/hyperdrive/concepts/connection-pooling/#pooling-mode) for more information.

## Configure connection pool size

You can configure the connection pool size using the Cloudflare dashboard, the Wrangler CLI, or the Cloudflare API.

To configure connection pool size via the dashboard:

  1. Log in to the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com) and select your account.

  2. Go to **Storage & databases** > **Hyperdrive**.

[ Go to **Hyperdrive** ↗ ](https://dash.cloudflare.com/?to=/:account/workers/hyperdrive)
  3. Select your Hyperdrive configuration.

  4. Select **Settings**.

  5. In the **Origin connection limit** section, adjust the **Maximum connections** value.

  6. Select **Save**.




Use the [`wrangler hyperdrive update`](https://developers.cloudflare.com/hyperdrive/reference/wrangler-commands/#hyperdrive-update) command with the `--origin-connection-limit` flag:
    
    
    npx wrangler hyperdrive update <HYPERDRIVE_ID> --origin-connection-limit=<MAX_CONNECTIONS>

Use the [Hyperdrive REST API](https://developers.cloudflare.com/api/resources/hyperdrive/subresources/configs/methods/update/) to update your configuration:
    
    
    curl --request PATCH \
      --url https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/hyperdrive/configs/<HYPERDRIVE_ID> \
      --header 'Content-Type: application/json' \
      --header 'Authorization: Bearer <API_TOKEN>' \
      --data '{
        "origin_connection_limit": <MAX_CONNECTIONS>
      }'

All Hyperdrive configurations have a minimum of 5 connections. The maximum connection count depends on your [Workers plan](https://developers.cloudflare.com/hyperdrive/platform/limits/).

Note

The Hyperdrive connection pool limit is a "soft limit". This means that it is possible for Hyperdrive to make more connections to your database than this limit in the event of network failure to ensure high availability. We recommend that you set the Hyperdrive connection limit to be lower than the limit of your origin database to account for occasions where Hyperdrive needs to create more connections for resiliency.

Note

You can request adjustments to Hyperdrive's origin connection limits. To request an increase, submit a [Limit Increase Request ↗︎](https://forms.gle/eX6pXvit1wBv77Yw5) and Cloudflare will contact you with next steps. Cloudflare also regularly monitors the Hyperdrive channel in [Cloudflare's Discord community ↗︎](https://discord.cloudflare.com/) and can answer questions regarding limits and requests.

## Best practices

  * **Start conservatively** : Begin with a lower connection count and gradually increase it based on your application's performance.
  * **Monitor database metrics** : Watch your database's connection usage and performance metrics to optimize the connection count.
  * **Consider database limits** : Ensure your configured connection count does not exceed your database's maximum connection limit.
  * **Account for multiple configurations** : If you have multiple Hyperdrive configurations connecting to the same database, consider the total connection count across all configurations.



## Related resources

  * [Connection pooling concepts](https://developers.cloudflare.com/hyperdrive/concepts/connection-pooling/)
  * [Connection lifecycle](https://developers.cloudflare.com/hyperdrive/concepts/connection-lifecycle/)
  * [Metrics and analytics](https://developers.cloudflare.com/hyperdrive/observability/metrics/)
  * [Hyperdrive limits](https://developers.cloudflare.com/hyperdrive/platform/limits/)
  * [Query caching](https://developers.cloudflare.com/hyperdrive/concepts/query-caching/)



[PreviousFirewall and networking configuration](https://developers.cloudflare.com/hyperdrive/configuration/firewall-and-networking-configuration/)[NextRotating database credentials](https://developers.cloudflare.com/hyperdrive/configuration/rotate-credentials/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/hyperdrive/configuration/tune-connection-pool.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
