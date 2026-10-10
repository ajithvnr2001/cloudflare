---
url: https://developers.cloudflare.com/changelog/product/email-security-cf1/
title: Email security Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:08.071718+00:00
---

# Email security Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/email-security-cf1/

# Changelog

New updates and improvements at Cloudflare.

All products

Product groups

AI

Analytics

Application performance

Application security

Cloudflare One

Consumer services

Core platform

Developer platform

Docs collections

Media

Network security

Privacy

Storage

Products

1.1.1.1 (DNS Resolver)

Access

Agent Lee

Agents

AI Crawl Control

AI Gateway

AI Search

Analytics

API Shield

Artifacts

Audit Logs

Automatic Platform Optimization

Basin

Basin Catalog

Basin Pipelines

Basin SQL

Billing

Bots

Browser Isolation

Browser Run

Cache / CDN

CASB

Cloudflare CLI

Cloudflare for SaaS

Cloudflare Fundamentals

Cloudflare Images

Cloudflare Mesh

Cloudflare Network Firewall

Cloudflare One

Cloudflare One Appliance

Cloudflare One Client

Cloudflare Tunnel

Cloudflare Tunnel for SASE

Cloudflare WAN

Cloudflare Web Analytics

Containers

D1

Data Localization Suite

Data Loss Prevention

Digital Experience Monitoring

DNS

Durable Objects

Email security

Email Service

Flagship

Gateway

Go SDK

Hyperdrive

KV

Load Balancing

Log Explorer

Logpush

Logpush Connectors

Logs

Magic Transit

Monetization Gateway

Multi-Cloud Networking

Network Flow

Network Interconnect

Organizations

Pages

Privacy Proxy

Queues

R2

Radar

Realtime

Registrar

Resource Tagging

Risk Score

Rules

Sandboxes

SDK

Secrets Store

Security Center

Security Overview

Speed

SSL/TLS

Stream

Support

Terraform

Turnstile

Vectorize

WAF

Web Search API

Workers

Workers AI

Workers Analytics Engine

Workers for Platforms

Workers VPC

Workflows

Zaraz

No products found.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

Aug 17, 2026

## [Post-quantum key exchange for MX deployments](https://developers.cloudflare.com/changelog/post/2026-08-17-post-quantum-key-exchange-mx/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Cloudflare Email Security now supports post-quantum hybrid key exchange with X25519MLKEM768 on the SMTP connections we make to receive and deliver mail. Deploying Email Security in front of a provider that supports post-quantum hybrid key agreement (like Google Workspace) will create a TLS 1.3 connection using post-quantum key agreement.

Inbound MX connections and outbound delivery connections now negotiate the [X25519MLKEM768](https://developers.cloudflare.com/ssl/post-quantum-cryptography/#hybrid-key-agreement) hybrid key agreement when the peer supports it, protecting SMTP traffic against [harvest-now, decrypt-later ↗︎](https://blog.cloudflare.com/pq-2024/) attacks.

Support is backwards compatible and enabled automatically for all customers. Senders and receivers that do not yet advertise post-quantum key agreement continue to connect with classical key exchange.

This applies to all Email Security packages:

  * **Advantage**
  * **Enterprise**
  * **Enterprise + PhishGuard**



Aug 12, 2026

## [Block emails by content with blocked content rules](https://developers.cloudflare.com/changelog/post/2026-08-12-blocked-content-rules/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Cloudflare Email security now lets administrators write their own content-based blocking rules. A new **Blocked content** area under **Policies & rules** lets you define a plaintext string or a regular expression, choose whether to scan the message subject, body, or both, and automatically block any message that matches.

  * Create rules using either **plaintext** matches or **regular expressions** — useful for blocking targeted phishing campaigns, known-bad phrases, or content patterns unique to your organization.
  * Choose the **search location** for each rule: **subject** , **body** , or **subject and body**.
  * Use the built-in **regular expression checker** to validate your pattern against sample text before saving, so you can confirm the rule matches what you expect and avoid false positives.
  * Matching messages are marked with a malicious [disposition](https://developers.cloudflare.com/cloudflare-one/email-security/reference/dispositions-and-attributes/) and prevented from reaching users' inboxes.



Blocked content rules currently only support the block action.

This feature is available for the following Email security packages:

  * **Enterprise**
  * **Enterprise + PhishGuard**



To get started, refer to [Blocked content](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/blocked-content/).

May 6, 2026

## [Cloudy Summaries in PhishNet O365](https://developers.cloudflare.com/changelog/post/2026-05-06-cloudy-summaries-in-phishnet_o365/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

PhishNet users can now access **Cloudy summaries** directly within the email investigation experience. When reviewing a message in PhishNet, users will see an AI-generated summary that provides additional context and key details about the email.

These summaries help users quickly understand the nature of a message without needing to manually parse through headers, body content, and detection signals. Cloudy surfaces the most relevant information so users can make faster, more informed decisions about suspicious emails.

**These summaries are not trained on customer data.** They are generated using the outputs of our existing detection models and analysis systems.

This feature is available for PhishNet with Office 365. Support for Gmail will be available by the end of the quarter.

Apr 7, 2026

## [User Submission Triage Status Tracking](https://developers.cloudflare.com/changelog/post/2026-04-07-triage-status-tracking/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Cloudflare Email security now supports **Triage Status Tracking for User Submissions**. This enhancement gives SOC teams a streamlined way to track, manage, and prioritize user-submitted emails directly within the Cloudflare One dashboard.

  * The User Submissions table now includes a **Status** column with three states: **Unreviewed** (new submissions awaiting triage), **Reviewed** (submissions assessed by the SOC team), and **Escalated** (submissions escalated to team submissions for further investigation). Analysts can quickly update statuses and filter the table to focus on what needs attention.
  * SOC teams can now organize their triage workflows, avoid duplicate reviews, and make sure critical threats get escalated for deeper investigation—bringing order to the chaos of high-volume submission management.



Triage Status Tracking is **automatically available** for all Email security customers using the user submissions feature. No additional configuration is required; customers just need to make sure user submissions are being sent to their user submission aliases.

This applies to all Email security packages:

  * **Advantage**
  * **Enterprise**
  * **Enterprise + PhishGuard**



Apr 6, 2026

## [DANE Support for MX Deployments](https://developers.cloudflare.com/changelog/post/2026-04-06-dane-support-mx-deployments/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Cloudflare Email Security now supports DANE (DNS-based Authentication of Named Entities) for MX deployments. This enhancement strengthens email transport security by enabling DNSSEC-backed certificate verification for our regional MX records.

  * Regional MX hostnames now publish DANE TLSA records backed by DNSSEC, enabling DANE-capable SMTP senders to cryptographically validate certificate identities before establishing TLS connections—moving beyond opportunistic encryption to verified encrypted delivery.
  * DANE support is automatically available for all customers using regional MX deployments. No additional configuration is required; DANE-capable mail infrastructure will automatically validate MX certificates using the published records.



This applies to all Email Security packages:

  * **Advantage**
  * **Enterprise**
  * **Enterprise + PhishGuard**



Mar 15, 2026

## [Unlimited result paging in Investigations](https://developers.cloudflare.com/changelog/post/2026-03-15-infinite-paging-investigations/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Investigations now support unlimited result paging in both the dashboard and the API, removing the previous 1,000-record cap. Security teams can page through complete result sets when searching across large mail volumes, giving SOC analysts and automated workflows deeper visibility for forensics and threat hunting.

In the dashboard, infinite paging is now supported in the Investigations view. The 1,000-record ceiling has been removed, so you can navigate through the full result set directly in the UI. The [Investigations API](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/methods/list) now returns up to 10,000 records per page (up from 1,000), with no cap on total result volume across pages.

For high-volume use cases, we recommend:

  * **[Logpush](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/email-security-logs/) to a SIEM** for full-fidelity datasets and long-term retention.
  * **SOAR playbooks** against the async bulk action API for large-scale remediation. Bulk actions initiated from the dashboard remain capped at 1,000 messages per action.
  * **The Investigations API** for report exports larger than 1,000 results, which is the dashboard download cap.



This applies to all Email Security packages:

  * **Advantage**
  * **Enterprise**
  * **Enterprise + PhishGuard**



Feb 2, 2026

## [Improved Accessibility and Search for Monitoring](https://developers.cloudflare.com/changelog/post/2026-02-02-improved-accessibility-search-for-monitoring/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

We have updated the Monitoring page to provide a more streamlined and insightful experience for administrators, improving both data visualization and dashboard accessibility.

  * **Enhanced Visual Layout** : Optimized contrast and the introduction of stacked bar charts for clearer data visualization and trend analysis. ![visual-example](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3212,height=2344,format=webp/_astro/monitoring-bar-charts.Bi-4BuXC.png)
  * **Improved Accessibility & Usability**: 
    * **Widget Search** : Added search functionality to multiple widgets, including Policies, Submitters, and Impersonation.
    * **Actionable UI** : All available actions are now accessible via dedicated buttons.
    * **State Indicators** : Improved UI states to clearly communicate loading, empty datasets, and error conditions. ![buttons-example](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3178,height=664,format=webp/_astro/monitoring-buttons.DORPJvP_.png)
  * **Granular Data Breakdowns** : New views for dispositions by month, malicious email details, link actions, and impersonations. ![monthly-example](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3202,height=1486,format=webp/_astro/monitoring-monthly-dispositions.CYuI5d9y.png)



This applies to all Email Security packages:

  * **Advantage**
  * **Enterprise**
  * **Enterprise + PhishGuard**



Jan 12, 2026

## [Enhanced visibility for post-delivery actions](https://developers.cloudflare.com/changelog/post/2026-01-12-enhanced-visibility-post-delivery-actions/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

The Action Log now provides enriched data for post-delivery actions to improve troubleshooting. In addition to success confirmations, failed actions now display the targeted Destination folder and a specific failure reason within the Activity field.

Note

Error messages will vary depending on whether you are using Google Workspace or Microsoft 365.

![failure-log-example](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2348,height=1692,format=webp/_astro/enhanced-visibility-post-delivery-actions.BNiyPtJU.png)

This update allows you to see the full lifecycle of a failed action. For instance, if an administrator tries to move an email that has already been deleted or moved manually, the log will now show the multiple retry attempts and the specific destination error.

This applies to all Email Security packages:

  * **Enterprise**
  * **Enterprise + PhishGuard**



Dec 3, 2025

## [Reclassifications to Submissions](https://developers.cloudflare.com/changelog/post/2025-12-03-submission-terminology-update/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

We have updated the terminology “Reclassify” and “Reclassifications” to “Submit” and “Submissions” respectively. This update more accurately reflects the outcome of providing these items to Cloudflare.

Submissions are leveraged to tune future variants of campaigns. To respect data sanctity, providing a submission does not change the original disposition of the emails submitted.

![nav_example](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=756,height=628,format=webp/_astro/reclassification-submission.B6nL5Hw7.png)

This applies to all Email Security packages:

  * **Advantage**
  * **Enterprise**
  * **Enterprise + PhishGuard**



Nov 18, 2025

## [Adjustment to Final Disposition Column](https://developers.cloudflare.com/changelog/post/2025-11-18-temporary-adjustment-to-final-disposition-column/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

#### Adjustment to Final Disposition column

#### The **Final Disposition** column in **Submissions** > **Team Submissions** tab is changing for non-Phishguard customers.

#### What's Changing

  * Column will be called **Status** instead of **Final Disposition**
  * Column status values will now be: **Submitted** , **Accepted** or **Rejected**.



#### Next Steps

We will listen carefully to your feedback and continue to find comprehensive ways to communicate updates on your submissions. Your submissions will continue to be addressed at an even greater rate than before, fuelling faster and more accurate email security improvement.

Oct 17, 2025

## [On-Demand Security Report](https://developers.cloudflare.com/changelog/post/2025-10-16-on-demand-security-report/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

You can now generate on-demand security reports directly from the Cloudflare dashboard. This new feature provides a comprehensive overview of your email security posture, making it easier than ever to demonstrate the value of Cloudflare’s Email security to executives and other decision makers.

These reports offer several key benefits:

  * **Executive Summary:** Quickly view the performance of Email security with a high-level executive summary.
  * **Actionable Insights:** Dive deep into trend data, breakdowns of threat types, and analysis of top targets to identify and address vulnerabilities.
  * **Configuration Transparency:** Gain a clear view of your policy, submission, and domain configurations to ensure optimal setup.
  * **Account Takeover Risks:** Get a snapshot of your M365 risky users (requires a Microsoft Entra ID P2 license and [M365 SaaS integration ↗︎](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/microsoft-365/)).



To get started, refer to [Download a security report](https://developers.cloudflare.com/cloudflare-one/email-security/monitoring/download-report/#download-a-security-report). ![Report](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1009,height=571,format=webp/_astro/report.CbkPa8Jt.png)

This feature is available across the following Email security packages:

  * **Advantage**
  * **Enterprise**
  * **Enterprise + PhishGuard**



Sep 23, 2025

## [Invalid Submissions Feedback](https://developers.cloudflare.com/changelog/post/2025-09-23-invalid-submissions/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Email security relies on your submissions to continuously improve our detection models. However, we often receive submissions in formats that cannot be ingested, such as incomplete EMLs, screenshots, or text files.

To ensure all customer feedback is actionable, we have launched two new features to manage invalid submissions sent to our team and user [submission aliases](https://developers.cloudflare.com/cloudflare-one/email-security/settings/phish-submissions/submission-addresses/):

  * **Email Notifications:** We now automatically notify users by email when they provide an invalid submission, educating them on the correct format. To disable notifications, go to **[Settings ↗︎](https://one.dash.cloudflare.com/?to=/:account/email-security/settings)** > **Invalid submission emails** and turn the feature off.

![EmailSec-Invalid-Submissions-Toggle](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1096,height=175,format=webp/_astro/EmailSec-Invalid-Submissions-Toggle.DXjbR6aX.png)

  * **Invalid Submission dashboard:** You can quickly identify which users need education to provide valid submissions so Cloudflare can provide continuous protection.

![EmailSec-Invalid-Submissions-Dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1132,height=511,format=webp/_astro/EmailSec-Invalid-Submissions-Dashboard.zuf1on2n.png)

Learn more about this feature on [invalid submissions](https://developers.cloudflare.com/cloudflare-one/email-security/submissions/invalid-submissions/).

This feature is available across these Email security packages:

  * **Advantage**
  * **Enterprise**
  * **Enterprise + PhishGuard**



Sep 11, 2025

## [Regional Email Processing for Germany, India, or Australia](https://developers.cloudflare.com/changelog/post/2025-09-11-regional-email-processing-gia/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

We’re excited to announce that Email security customers can now choose their preferred mail processing location directly from the UI when onboarding a domain. This feature is available for the following onboarding methods: **MX** , **BCC** , and **Journaling**.

#### What’s new

Customers can now select where their email is processed. The following regions are supported:

  * **Germany**
  * **India**
  * **Australia**



Global processing remains the default option, providing flexibility to meet both compliance requirements or operational preferences.

#### How to use it

When onboarding a domain with MX, BCC, or Journaling:

  1. Select the desired processing location (Germany, India, or Australia).
  2. The UI will display updated processing addresses specific to that region.
  3. For MX onboarding, if your domain is managed by Cloudflare, you can automatically update MX records directly from the UI.



#### Availability

This feature is available across these Email security packages:

  * **Advantage**
  * **Enterprise**
  * **Enterprise + PhishGuard**



#### What’s next

We’re expanding the list of processing locations to match our [Data Localization Suite (DLS)](https://developers.cloudflare.com/data-localization/) footprint, giving customers the broadest set of regional options in the market without the complexity of self-hosting.

Sep 1, 2025

## [Updated Email security roles](https://developers.cloudflare.com/changelog/post/2025-09-01-updated-new-roles/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

To provide more granular controls, we refined the [existing roles](https://developers.cloudflare.com/cloudflare-one/roles-permissions/#email-security-roles) for Email security and launched a new Email security role as well.

All Email security roles no longer have read or write access to any of the other Zero Trust products:

  * **Email Configuration Admin**
  * **Email Integration Admin**
  * **Email security Read Only**
  * **Email security Analyst**
  * **Email security Policy Admin**
  * **Email security Reporting**



To configure [Data Loss Prevention (DLP)](https://developers.cloudflare.com/cloudflare-one/email-security/outbound-dlp/) or [Remote Browser Isolation (RBI)](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/#set-up-clientless-web-isolation), you now need to be an admin for the Zero Trust dashboard with the **Cloudflare Zero Trust** role.

Also through customer feedback, we have created a new additive role to allow **Email security Analyst** to create, edit, and delete Email security policies, without needing to provide access via the **Email Configuration Admin** role. This role is called **Email security Policy Admin** , which can read all settings, but has write access to [allow policies](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/allow-policies/), [trusted domains](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/trusted-domains/), and [blocked senders](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/blocked-senders/).

This feature is available across these Email security packages:

  * **Advantage**
  * **Enterprise**
  * **Enterprise + PhishGuard**



Aug 7, 2025

## [Expanded Email Link Isolation](https://developers.cloudflare.com/changelog/post/2025-08-07-expanded-link-isolation/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

When you deploy MX or Inline, not only can you apply email link isolation to suspicious links in all emails (including benign), you can now also apply email link isolation to all links of a specified disposition. This provides more flexibility in controlling user actions within emails.

For example, you may want to deliver suspicious messages but isolate the links found within them so that users who choose to interact with the links will not accidentally expose your organization to threats. This means your end users are more secure than ever before.

![Expanded Email Link Isolation Configuration](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=497,format=webp/_astro/expanded-link-actions.DziIg6E8.jpg)

To isolate all links within a message based on the disposition, select **Settings** > **Link Actions** > **View** and select **Configure**. As with other other links you isolate, an interstitial will be provided to warn users that this site has been isolated and the link will be recrawled live to evaluate if there are any changes in our threat intel. Learn more about this feature on [Configure link actions ↗︎](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/configure-link-actions/).

This feature is available across these Email security packages:

  * **Enterprise**
  * **Enterprise + PhishGuard**



May 15, 2025

## [Open email attachments with Browser Isolation](https://developers.cloudflare.com/changelog/post/2025-05-08-open-attachments-with-browser-isolation/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

You can now safely open email attachments to view and investigate them.

What this means is that messages now have a **Attachments** section. Here, you can view processed attachments and their classifications (for example, _Malicious_ , _Suspicious_ , _Encrypted_). Next to each attachment, a **Browser Isolation** icon allows your team to safely open the file in a **clientless, isolated browser** with no risk to the analyst or your environment.

![Attachment-RBI](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=517,height=155,format=webp/_astro/Attachment-RBI.U9Dp8dJO.png)

To use this feature, you must:

  * Turn on **Allow users to open a remote browser without the device client** in your Zero Trust settings.
  * Have **Browser Isolation (BISO)** seats assigned.



For more details, refer to our [setup guide](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/).

Some attachment types may not render in Browser Isolation. If there is a file type that you would like to be opened with Browser Isolation, reach out to your Cloudflare contact.

This feature is available across these Email security packages:

  * **Advantage**
  * **Enterprise**
  * **Enterprise + PhishGuard**



May 8, 2025

## [Open email links with Browser Isolation](https://developers.cloudflare.com/changelog/post/2025-05-15-open-links-browser-isolation/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

You can now safely open links in emails to view and investigate them.

![Open links with Browser Isolation](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=558,height=204,format=webp/_astro/investigate-links.pYbpGkt5.jpg)

From **Investigation** , go to **View details** , and look for the **Links identified** section. Next to each link, the Cloudflare dashboard will display an **Open in Browser Isolation** icon which allows your team to safely open the link in a clientless, isolated browser with no risk to the analyst or your environment. Refer to [Open links](https://developers.cloudflare.com/cloudflare-one/email-security/investigation/search-email/#open-links) to learn more about this feature.

To use this feature, you must:

  * Turn on **Allow users to open a remote browser without the device client** in your Zero Trust settings.
  * Have **Browser Isolation (RBI)** seats assigned.



For more details, refer to our [setup guide](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/).

This feature is available across these Email security packages:

  * **Advantage**
  * **Enterprise**
  * **Enterprise + PhishGuard**



Apr 1, 2025

## [CASB and Email security](https://developers.cloudflare.com/changelog/post/2025-04-01-casb-email-security/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

With Email security, you get two free CASB integrations.

Use one SaaS integration for Email security to sync with your directory of users, take actions on delivered emails, automatically provide EMLs for reclassification requests for clean emails, discover CASB findings and more.

With the other integration, you can have a separate SaaS integration for CASB findings for another SaaS provider.

Refer to [Add an integration](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/) to learn more about this feature.

![CASB-EmailSecurity](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=727,height=502,format=webp/_astro/CASB-EmailSecurity.B1wd9be2.png)

This feature is available across these Email security packages:

  * **Enterprise**
  * **Enterprise + PhishGuard**



Mar 1, 2025

## [Use Logpush for Email security detections](https://developers.cloudflare.com/changelog/post/2025-03-01-logpush-detections/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

You can now send detection logs to an endpoint of your choice with Cloudflare Logpush.

Filter logs matching specific criteria you have set and select from over 25 fields you want to send. When creating a new Logpush job, remember to select **Email security alerts** as the dataset.

![logpush-detections](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=927,height=688,format=webp/_astro/Logpush-Detections.Dc5tHta3.png)

For more information, refer to [Enable detection logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/email-security-logs/#enable-detection-logs).

This feature is available across these Email security packages:

  * **Enterprise**
  * **Enterprise + PhishGuard**



Feb 27, 2025

## [Check status of Email security or Area 1](https://developers.cloudflare.com/changelog/post/2025-02-07-check-status/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Concerns about performance for Email security or Area 1? You can now check the operational status of both on the [Cloudflare Status page ↗︎](https://www.cloudflarestatus.com/).

For Email security, look under **Cloudflare Sites and Services**.

  * **Dashboard** is the dashboard for Cloudflare, including Email security
  * **Email security (Zero Trust)** is the processing of email
  * **API** are the Cloudflare endpoints, including the ones for Email security



For Area 1, under **Cloudflare Sites and Services** :

  * **Area 1 - Dash** is the dashboard for Cloudflare, including Email security
  * **Email security (Area1)** is the processing of email
  * **Area 1 - API** are the Area 1 endpoints

![Status-page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=792,height=348,format=webp/_astro/Status-Page.DcFJ1286.png)

This feature is available across these Email security packages:

  * **Advantage**
  * **Enterprise**
  * **Enterprise + PhishGuard**



Feb 25, 2025

## [Use DLP Assist for M365](https://developers.cloudflare.com/changelog/post/2025-02-25-dlp-assist-for-m365/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Cloudflare Email security customers who have Microsoft 365 environments can quickly deploy an Email DLP (Data Loss Prevention) solution for free.

Simply deploy our add-in, create a DLP policy in Cloudflare, and configure Outlook to trigger behaviors like displaying a banner, alerting end users before sending, or preventing delivery entirely.

Refer to [Outbound Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/email-security/outbound-dlp/) to learn more about this feature.

In GUI alert:

![DLP-Alert](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1357,height=212,format=webp/_astro/DLP-Alert.5s-fbKn3.png)

Alert before sending:

![DLP-Pop-up](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1362,height=479,format=webp/_astro/DLP-Pop-up.0gkYy7o5.png)

Prevent delivery:

![DLP-Blocked](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1353,height=329,format=webp/_astro/DLP-Blocked.CmQkGrnM.png)

This feature is available across these Email security packages:

  * **Enterprise**
  * **Enterprise + PhishGuard**



Feb 7, 2025

## [Open email links with Security Center](https://developers.cloudflare.com/changelog/post/2025-02-07-open-links-security-center/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

You can now investigate links in emails with Cloudflare Security Center to generate a report containing a myriad of technical details: a phishing scan, SSL certificate data, HTTP request and response data, page performance data, DNS records, what technologies and libraries the page uses, and more.

![Open links in Security Center](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1118,height=402,format=webp/_astro/Open-Links-Security-Center.b-LJU4YB.png)

From **Investigation** , go to **View details** , and look for the **Links identified** section. Select **Open in Security Center** next to each link. **Open in Security Center** allows your team to quickly generate a detailed report about the link with no risk to the analyst or your environment.

For more details, refer to [Open links](https://developers.cloudflare.com/cloudflare-one/email-security/investigation/search-email/#open-links).

This feature is available across these Email security packages:

  * **Advantage**
  * **Enterprise**
  * **Enterprise + PhishGuard**



Dec 19, 2024

## [Escalate user submissions](https://developers.cloudflare.com/changelog/post/2024-12-19-escalate-user-submissions/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

After you triage your users' submissions (that are machine reviewed), you can now escalate them to our team for reclassification (which are instead human reviewed). User submissions from the submission alias, PhishNet, and our API can all be escalated.

![Escalate](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=897,height=434,format=webp/_astro/Escalate.CwXPIyM3.png)

From **Reclassifications** , go to **User submissions**. Select the three dots next to any of the user submissions, then select **Escalate** to create a team request for reclassification. The Cloudflare dashboard will then show you the submissions on the **Team Submissions** tab.

Refer to [User submissions](https://developers.cloudflare.com/cloudflare-one/email-security/submissions/user-submissions/) to learn more about this feature.

This feature is available across these Email security packages:

  * **Advantage**
  * **Enterprise**
  * **Enterprise + PhishGuard**



Dec 19, 2024

## [Increased transparency for phishing email submissions](https://developers.cloudflare.com/changelog/post/2024-12-19-reclassification-tab/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

You now have more transparency about team and user submissions for phishing emails through a **Reclassification** tab in the Zero Trust dashboard.

Reclassifications happen when users or admins [submit a phish](https://developers.cloudflare.com/cloudflare-one/email-security/settings/phish-submissions/) to Email security. Cloudflare reviews and - in some cases - reclassifies these emails based on improvements to our machine learning models.

This new tab increases your visibility into this process, allowing you to view what submissions you have made and what the outcomes of those submissions are.

![Use the Reclassification area to review submitted phishing emails](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1645,height=758,format=webp/_astro/reclassifications-tab.yDgtjG51.png)

Nov 7, 2024

## [Use Logpush for Email security user actions](https://developers.cloudflare.com/changelog/post/2024-11-07-logpush-user-actions/)

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

You can now send user action logs for Email security to an endpoint of your choice with Cloudflare Logpush.

Filter logs matching specific criteria you have set or select from multiple fields you want to send. For all users, we will log the date and time, user ID, IP address, details about the message they accessed, and what actions they took.

When creating a new Logpush job, remember to select **Audit logs** as the dataset and filter by:

  * **Field** : `"ResourceType"`
  * **Operator** : `"starts with"`
  * **Value** : `"email_security"`.

![Logpush-user-actions](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=829,height=454,format=webp/_astro/Logpush-User-Actions.D14fWgmq.png)

For more information, refer to [Enable user action logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/email-security-logs/#enable-user-action-logs).

This feature is available across all Email security packages:

  * **Enterprise**
  * **Enterprise + PhishGuard**



← Prev

1[2](https://developers.cloudflare.com/changelog/product/email-security-cf1/2/)

[Next →](https://developers.cloudflare.com/changelog/product/email-security-cf1/2/)
