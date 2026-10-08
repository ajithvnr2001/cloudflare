---
url: https://developers.cloudflare.com/changelog/post/2026-07-15-event-subscriptions/
title: Subscribe to Email Sending events with Queues \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:03.493049+00:00
---

# Subscribe to Email Sending events with Queues · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-15-event-subscriptions/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 15, 2026

## Subscribe to Email Sending events with Queues

[Email Service](https://developers.cloudflare.com/email-service/)[Queues](https://developers.cloudflare.com/queues/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-15-event-subscriptions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now subscribe to **[Email Sending](https://developers.cloudflare.com/email-service/api/send-emails/) events** through [Queues event subscriptions](https://developers.cloudflare.com/queues/event-subscriptions/) and receive outbound transactional email lifecycle events on a queue. Each subscription is scoped to one sending domain — either the zone apex, such as `example.com`, or a verified sending subdomain, such as `send.example.com`.

Six event types are published: `message.delivered`, `message.deferred`, `message.bounced`, `message.failed`, `message.rejected`, and `message.complained`. Use them to track deliverability, react to bounces and complaints, and drive suppression or retry logic. Email Routing events are not published on this source.

Each event includes the message details, delivery status, and SMTP response:
    
    
    {
    	"type": "cf.email.sending.message.delivered",
    	"source": {
    		"type": "email.sending",
    		"zoneId": "023e105f4ecef8ad9ca31a8372d0c353",
    		"domain": "example.com"
    	},
    	"payload": {
    		"messageId": "0101018f7d0c4d9a-msg-deadbeef",
    		"recipient": "user@example.net",
    		"terminal": true,
    		"delivery": {
    			"status": "delivered",
    			"smtpStatusCode": "250"
    		}
    	}
    }

Refer to [Event subscriptions](https://developers.cloudflare.com/email-service/platform/event-subscriptions/) to see all event types and example payloads.
