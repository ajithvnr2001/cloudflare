---
url: https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/best-practices/
title: Detection settings best practices \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:36.624990+00:00
---

# Detection settings best practices · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/best-practices/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)Settings

  4. /Detection settings
  5. /Detection settings best practices



# Detection settings best practices

Last updated Sep 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/best-practices/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPolicy selection criteriaBest practices for configuration

This guide describes how to configure detection settings to mitigate impersonation risks while ensuring legitimate delivery.

Once you configure the [impersonation registry](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/impersonation-registry/) to mitigate spoof detections, you can add emails in the impersonation registry as secondary email. Refer to [Edit users](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/impersonation-registry/#edit-users) to learn how to add a secondary email address.

For impersonation events that are caused by systems, Cloudflare recommends that you configure an [allow policy](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/allow-policies/) to mitigate delivery disruptions.

To maintain a higher security posture, allow policies should be defined with the narrowest possible scope. Start with specific expressions or email addresses that will target the actual sender or system. If the system is sending from a variety of addresses, you can create an expression that is wider while keeping the expression specific. In some situations, it is better to have multiple specific entries than a more generic policy that allows a whole domain.

## Policy selection criteria

When you configure an [allow policy](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/allow-policies/), you can choose how Email security handles messages that match your criteria.

Allow policies are suitable for services that may spoof people's names.

Use **Accept sender** with **Sender verification (recommended)** turned on for systematic traffic. For example, a file shared through Google Drive will create a notification using the name of the user that is sharing the document. However, the underlying email address used will be a Google system address.

Use **Trusted Sender** for emails that do not require phishing inspections. This will exempt messages from any phishing analysis, including links analysis.

Example use cases:

  * Temporary rules (to avoid over-detection)
  * Phishing simulations
  * Applications that send one time links for verification



## Best practices for configuration

  * Prioritize static IPs: Use known and owned, static IP addresses for relay servers. Avoid [ephemeral IP addresses ↗︎](https://docs.cloud.google.com/vpc/docs/ip-addresses#ephemeral_and_static_ip_addresses) as their transient nature can lead to policy degradation.
  * Enforce Sender Verification: Always have **Sender Verification (Recommended)** enabled in the Cloudflare dashboard. It validates the originating system's email authentication records (namely [SPF ↗︎](https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-spf-record/), [DKIM ↗︎](https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-dkim-record/), and [DMARC ↗︎](https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-dmarc-record/)) against the domain to ensure authenticity.
  * Handle unsanctioned traffic: Unsanctioned traffic is traffic which has not been approved within an organization. This is also known as [Shadow IT ↗︎](https://www.cloudflare.com/en-gb/learning/access-management/what-is-shadow-it/). If an unsanctioned system generates spam or spoofed content, [configure a text add-on](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/configure-text-add-ons/) to append a tag to the subject line and automatically [move](https://developers.cloudflare.com/cloudflare-one/email-security/settings/auto-moves/) the message to the junk folder.



[PreviousAdditional detections](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/additional-detections/)[NextOverview](https://developers.cloudflare.com/cloudflare-one/email-security/settings/submission-settings/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/email-security/settings/detection-settings/best-practices.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
