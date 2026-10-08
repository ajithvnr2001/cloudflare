---
url: https://developers.cloudflare.com/cloudflare-one/email-security/submissions/user-submissions/
title: User submissions \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:44.771969+00:00
---

# User submissions · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/email-security/submissions/user-submissions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

  4. /[Submissions](https://developers.cloudflare.com/cloudflare-one/email-security/submissions/)
  5. /User submissions



# User submissions

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/email-security/submissions/user-submissions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewView user submissionsFilter user submissionsView submission detailsEscalate a submission

User submissions are the emails your users submitted for submission. User submissions help enhance our detection model, but can be escalated for human review.

Any email that is reported as [phish](https://developers.cloudflare.com/cloudflare-one/email-security/settings/phish-submissions/#reclassify-an-email) will be displayed under **User submissions**.

Note

[PhishGuard](https://developers.cloudflare.com/cloudflare-one/email-security/phishguard/) customers can have submissions analyzed when submitting at either user or team level. Any non-PhishGuard customer can still have submissions analyzed by submitting at team level.

## View user submissions

To view user submissions:

  1. Log in to [Cloudflare One ↗︎](https://one.dash.cloudflare.com/).
  2. Select **Email security** > **Submissions**.
  3. Select **User submissions**.



## Filter user submissions

Select among the following filters:

  * **Date Range** : Select a date range from the last 7, last 30, and last 90 days.
  * **Original disposition** : Select among the [available values](https://developers.cloudflare.com/cloudflare-one/email-security/reference/dispositions-and-attributes/#available-values).
  * **Submitted as** : Select among the [available values](https://developers.cloudflare.com/cloudflare-one/email-security/reference/dispositions-and-attributes/#available-values).



Once you have selected all the filters, select **Apply filters**.

The dashboard will populate the table with the list of emails your users submitted for submission, including a **Submission ID** , and the **Email subject**.

## View submission details

To gain more details on a specific submission:

  1. Go to the submission you want to have more details for.
  2. Select the three dots > select among **View more** , **View email message** , **View similar details** , and **Escalate**.



## Escalate a submission

To escalate a submission:

  1. Go to the submission you want to escalate.
  2. Select the three dots > select **Escalate**.
  3. The dashboard will display a message to authorize escalation. Select **Escalate**.



[PreviousTeam submissions](https://developers.cloudflare.com/cloudflare-one/email-security/submissions/team-submissions/)[NextInvalid submissions](https://developers.cloudflare.com/cloudflare-one/email-security/submissions/invalid-submissions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/email-security/submissions/user-submissions.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
