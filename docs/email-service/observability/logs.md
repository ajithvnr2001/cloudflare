---
url: https://developers.cloudflare.com/email-service/observability/logs/
title: Email logs \u00b7 Cloudflare Email Service docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:14.992929+00:00
---

# Email logs · Cloudflare Email Service docs

> Source: https://developers.cloudflare.com/email-service/observability/logs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Email Service](https://developers.cloudflare.com/email-service/)
  3. /Observability and logs
  4. /Email logs



# Email logs

View and analyze email sending and routing activity logs with detailed authentication and delivery information

Last updated Jul 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/email-service/observability/logs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewActivity log Email sending logs Email routing logsViewing email details Authentication status Delivery information Message previewBest practices for log monitoring Regular review Key metrics to watch Troubleshooting workflow

Email Service provides comprehensive logging for both email sending and routing activities. Access detailed logs through the Cloudflare dashboard to monitor email flow, troubleshoot delivery issues, and analyze authentication status.

## Activity log

The Activity log allows you to sort through all email activities and check actions taken by Email Service. In the dashboard you can filter the Activity log to a time range between 30 minutes and 30 days, or specify a custom range.

The Activity log surfaces the same per-event data that is also available programmatically through the [`emailSendingAdaptive` and `emailRoutingAdaptive` datasets](https://developers.cloudflare.com/email-service/observability/metrics-analytics/) in the GraphQL Analytics API.

For Email Routing, you can expand an individual email in the Activity log to inspect authentication results ([SPF ↗︎](https://datatracker.ietf.org/doc/html/rfc7208), [DKIM ↗︎](https://datatracker.ietf.org/doc/html/rfc6376), and [DMARC ↗︎](https://datatracker.ietf.org/doc/html/rfc7489)).

### Email sending logs

For outbound emails sent through Email Service:

  * **Sent** : Email successfully accepted and queued for delivery.
  * **Delivered** : Email successfully delivered to recipient's mail server.
  * **Delivery failed** : Email bounced (hard or soft bounce). This corresponds to the `deliveryFailed` status in the [GraphQL Analytics API](https://developers.cloudflare.com/email-service/observability/metrics-analytics/).
  * **Rejected** : Email was not sent because the recipient is on your account's [suppression list](https://developers.cloudflare.com/email-service/concepts/suppressions/).
  * **Failed** : Email failed to send due to configuration or authentication issues.



### Email routing logs

For inbound emails processed through Email Routing:

  * **Forwarded** : Email successfully forwarded to destination address.
  * **Handled** : Email processed by a Worker handler.
  * **Dropped** : Email dropped due to filtering rules or configuration.
  * **Rejected** : Email rejected due to SPF, DKIM, or DMARC failures.
  * **Delivery failed** : Email could not be delivered to the destination address.
  * **Error** : Email could not be processed due to an internal error.



## Viewing email details

Select any email in the Activity log to expand its details and view authentication and delivery information.

### Authentication status

Check the status of email authentication protocols:

  * **SPF status** : Shows pass/fail for Sender Policy Framework validation.
  * **DKIM status** : Shows pass/fail for DomainKeys Identified Mail signature verification.
  * **DMARC status** : Shows pass/fail for Domain-based Message Authentication compliance.



### Delivery information

For sent emails, see delivery details:

  * Recipient mail server response.
  * Delivery attempts and timestamps.
  * Bounce reason codes and categories.
  * Final delivery status.



### Message preview

For sent emails, expand the email in the Activity log to open the **Preview** section and inspect the message as it was sent. The preview provides the following tabs:

  * **HTML** : The rendered HTML body.
  * **Text** : The plain text body.
  * **Headers** : The message headers.
  * **Attachments** : Files included with the message.
  * **Raw** : The full raw [RFC 5322 ↗︎](https://datatracker.ietf.org/doc/html/rfc5322) message source.



To make sent messages previewable, turn on [**Email preview**](https://developers.cloudflare.com/email-service/configuration/domains/#email-preview) for the sending domain. Previews cover messages sent while the setting is turned on and are retained for about seven days. New sending domains have **Email preview** turned on automatically.

## Best practices for log monitoring

### Regular review

  * Monitor logs daily during initial setup
  * Check weekly for ongoing operations
  * Review immediately after configuration changes



### Key metrics to watch

  * Authentication failure rates
  * Bounce patterns and trends
  * Delivery success rates



### Troubleshooting workflow

  1. Identify the issue: Use logs to pinpoint failure types
  2. Check authentication: Verify SPF, DKIM, DMARC configuration
  3. Adjust configuration: Make necessary DNS or routing changes
  4. Monitor improvement: Track metrics after changes



* * *

Email logs provide the visibility needed to maintain high deliverability and properly route incoming emails. Use this data to optimize your email configuration and quickly resolve any delivery issues.

[PreviousAudit logs](https://developers.cloudflare.com/email-service/observability/audit-logs/)[NextPostmaster](https://developers.cloudflare.com/email-service/reference/postmaster/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/email-service/observability/logs.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
