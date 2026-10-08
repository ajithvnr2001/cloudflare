---
url: https://developers.cloudflare.com/client-side-security/alerts/alert-types/
title: Alert types \u00b7 Client-side security docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:57.037734+00:00
---

# Alert types · Client-side security docs

> Source: https://developers.cloudflare.com/client-side-security/alerts/alert-types/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Client-side security](https://developers.cloudflare.com/client-side-security/)
  3. /[Alerting](https://developers.cloudflare.com/client-side-security/alerts/)
  4. /Alert types



# Alert types

Last updated Apr 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/client-side-security/alerts/alert-types/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewNew resource alertsCode change alertMalicious resource alerts

You can configure alerts for resources detected in your domain. Refer to [Alerts](https://developers.cloudflare.com/client-side-security/alerts/) for more information.

## New resource alerts

Note

Requires a Business plan or higher.

New resource alerts notify you about new resources detected on your domain, resources detected from new host domains, or issues with the URL length of newly detected resources.

Client-side security New Resources Alert

**Who is it for?**

[Client-side security](https://developers.cloudflare.com/client-side-security/) customers who want to receive a notification when new resources appear in their domain.

**Other options / filters**

None.

**Included with**

Business plans or higher.

**What should you do if you receive one?**

Investigate to confirm that it is an expected change.

**Additional information**

Triggered daily. If configured with a zone filter, the alert is triggered immediately.

Client-side security New Domain Alert

**Who is it for?**

[Client-side security](https://developers.cloudflare.com/client-side-security/) customers who want to receive a notification when resources from new host domains appear in their domain.

**Other options / filters**

None.

**Included with**

Business plans or higher.

**What should you do if you receive one?**

Investigate to confirm that it is an expected change.

**Additional information**

Triggered hourly. If configured with a zone filter, the alert is triggered immediately.

Client-side security New Resource Exceeds Max URL Length Alert

**Who is it for?**

[Client-side security](https://developers.cloudflare.com/client-side-security/) customers who want to receive a notification when a resource's URL exceeds the maximum allowed length.

**Other options / filters**

None.

**Included with**

Business plans or higher.

**What should you do if you receive one?**

Manually check the resource.

## Code change alert

Note

Only available to customers with Client-Side Security Advanced.

This alert notifies you about [code changes](https://developers.cloudflare.com/client-side-security/detection/review-changed-scripts/) in previously detected scripts.

Client-side security New Code Change Detection Alert

**Who is it for?**

[Client-side security](https://developers.cloudflare.com/client-side-security/) customers who want to receive a notification when JavaScript dependencies change in the pages of their domain.

**Other options / filters**

None.

**Included with**

Customers with Client-Side Security Advanced.

**What should you do if you receive one?**

Investigate to confirm that it is an expected change.

**Additional information**

Triggered daily. If configured with a zone filter, the alert is triggered immediately.

## Malicious resource alerts

Note

Only available to customers with Client-Side Security Advanced.

Malicious resource alerts notify you about [resources considered malicious](https://developers.cloudflare.com/client-side-security/how-it-works/malicious-script-detection/), based on their [domain](https://developers.cloudflare.com/client-side-security/how-it-works/malicious-script-detection/#malicious-domain-checks), [URL](https://developers.cloudflare.com/client-side-security/how-it-works/malicious-script-detection/#malicious-url-checks), or [script content](https://developers.cloudflare.com/client-side-security/how-it-works/malicious-script-detection/#malicious-script-detection).

Client-side security New Malicious Domain Alert

**Who is it for?**

[Client-side security](https://developers.cloudflare.com/client-side-security/) customers who want to receive a notification when resources from a known malicious domain appear in their domain. For more information, refer to [Malicious script and connection detection](https://developers.cloudflare.com/client-side-security/how-it-works/malicious-script-detection/).

**Other options / filters**

None.

**Included with**

Customers with Client-Side Security Advanced.

**What should you do if you receive one?**

Review the information in the client-side security dashboard about the detected malicious resources, then update the pages where those resources were detected.

For more information, refer to [Review scripts and connections considered malicious](https://developers.cloudflare.com/client-side-security/detection/review-malicious-scripts/).

Client-side security New Malicious URL Alert

**Who is it for?**

[Client-side security](https://developers.cloudflare.com/client-side-security/) customers who want to receive a notification when resources from a known malicious URL appear in their domain. For more information, refer to [Malicious script and connection detection](https://developers.cloudflare.com/client-side-security/how-it-works/malicious-script-detection/).

**Other options / filters**

None.

**Included with**

Customers with Client-Side Security Advanced.

**What should you do if you receive one?**

Review the information in the client-side security dashboard about the detected malicious resources, then update the pages where those resources were detected.

For more information, refer to [Review scripts and connections considered malicious](https://developers.cloudflare.com/client-side-security/detection/review-malicious-scripts/).

Client-side security New Malicious Script Alert

**Who is it for?**

[Client-side security](https://developers.cloudflare.com/client-side-security/) customers who want to receive a notification when Cloudflare classifies JavaScript dependencies in their domain as malicious. For more information, refer to [Malicious script and connection detection](https://developers.cloudflare.com/client-side-security/how-it-works/malicious-script-detection/).

**Other options / filters**

None.

**Included with**

Customers with Client-Side Security Advanced.

**What should you do if you receive one?**

Review the information in the client-side security dashboard about the detected malicious resources, then update the pages where those resources were detected.

For more information, refer to [Review scripts and connections considered malicious](https://developers.cloudflare.com/client-side-security/detection/review-malicious-scripts/).

Malicious resource alerts will only include resources with an _Active_ status. Refer to [Script and connection statuses](https://developers.cloudflare.com/client-side-security/reference/script-statuses/) for more information.

[PreviousConfigure an alert](https://developers.cloudflare.com/client-side-security/alerts/configure/)[NextOverview](https://developers.cloudflare.com/client-side-security/rules/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/client-side-security/alerts/alert-types.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
