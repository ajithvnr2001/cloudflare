---
url: https://developers.cloudflare.com/queues/platform/audit-logs/
title: Audit Logs \u00b7 Cloudflare Queues docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:41.382746+00:00
---

# Audit Logs · Cloudflare Queues docs

> Source: https://developers.cloudflare.com/queues/platform/audit-logs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Queues](https://developers.cloudflare.com/queues/)
  3. /Platform
  4. /Audit Logs



# Audit Logs

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/queues/platform/audit-logs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewViewing audit logsLogged operations

[Audit logs](https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/) provide a comprehensive summary of changes made within your Cloudflare account, including those made to Queues. This functionality is always enabled.

## Viewing audit logs

To view audit logs for your Queue in the Cloudflare dashboard, go to the **Audit logs** page.

[ Go to **Audit logs** ↗ ](https://dash.cloudflare.com/?to=/:account/audit-log)

For more information on how to access and use audit logs, refer to [Review audit logs](https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/).

## Logged operations

The following configuration actions are logged:

Operation| Description| CreateQueue| Creation of a new queue.  
---|---  
DeleteQueue| Deletion of an existing queue.  
UpdateQueue| Updating the configuration of a queue.  
AttachConsumer| Attaching a consumer, including HTTP pull consumers, to the Queue.  
RemoveConsumer| Removing a consumer, including HTTP pull consumers, from the Queue.  
UpdateConsumerSettings| Changing Queues consumer settings.  
  
[PreviousChangelog](https://developers.cloudflare.com/queues/platform/changelog/)[NextHow Queues Works](https://developers.cloudflare.com/queues/reference/how-queues-works/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/queues/platform/audit-logs.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
