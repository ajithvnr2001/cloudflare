---
url: https://developers.cloudflare.com/queues/examples/send-messages-from-dash/
title: Cloudflare Queues - Sending messages from the dashboard \u00b7 Cloudflare Queues docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:41.352393+00:00
---

# Cloudflare Queues - Sending messages from the dashboard · Cloudflare Queues docs

> Source: https://developers.cloudflare.com/queues/examples/send-messages-from-dash/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Queues](https://developers.cloudflare.com/queues/)
  3. /[Examples](https://developers.cloudflare.com/queues/examples/)
  4. /Send messages from the dashboard



# Send messages from the dashboard

Use the dashboard to send messages to a queue.

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/queues/examples/send-messages-from-dash/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Sending messages from the dashboard allows you to debug Queues or queue consumers without a producer Worker.

To send messages from the dashboard:

  1. In the Cloudflare dashboard, go to the **Queues** page.

[ Go to **Queues** ↗ ](https://dash.cloudflare.com/?to=/:account/workers/queues)
  2. Select the queue to send a message to.

  3. Select the **Messages** tab.

  4. Select **Send**.

  5. Choose your message **Content Type** : _Text_ or _JSON_.

  6. Enter your message. Alternatively, drag a file over the textbox to upload a file as a message.

  7. Select **Send**.




Your message will be sent to the queue.

Refer to the [Get Started guide](https://developers.cloudflare.com/queues/get-started/) to learn how to send messages to a queue from a Worker.

[PreviousUse Queues to store data in R2](https://developers.cloudflare.com/queues/examples/send-errors-to-r2/)[NextList and acknowledge messages from the dashboard](https://developers.cloudflare.com/queues/examples/list-messages-from-dash/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/queues/examples/send-messages-from-dash.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
