---
url: https://developers.cloudflare.com/client-side-security/best-practices/deploy-rules-in-production/
title: Deploy content security rules in production \u00b7 Client-side security docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:57.083961+00:00
---

# Deploy content security rules in production · Client-side security docs

> Source: https://developers.cloudflare.com/client-side-security/best-practices/deploy-rules-in-production/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Client-side security](https://developers.cloudflare.com/client-side-security/)
  3. /Best practices
  4. /Deploy rules in production



# Deploy content security rules in production

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/client-side-security/best-practices/deploy-rules-in-production/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUpdate rules safelyPre-enforcement checklistRollback a rule change

Note

Only available to customers with Client-Side Security Advanced.

Follow the practices on this page when deploying or updating [content security rules](https://developers.cloudflare.com/client-side-security/rules/) in a production environment. Applying rule changes without a validation period can block legitimate resources and disrupt your application for end users.

## Update rules safely

When updating content security rules in production, avoid the following:

  * Do not edit an existing rule directly in production without testing first.
  * Do not change a rule action from _Log_ to _Allow_ without a validation period.
  * Do not delete all rules at once.



Instead, follow these practices:

  * Test changes in a staging environment before applying them in production.
  * Use the _Log_ [rule action](https://developers.cloudflare.com/client-side-security/rules/#rule-actions) for at least seven days before switching to _Allow_.
  * Update one rule at a time.
  * Monitor [rule violations](https://developers.cloudflare.com/client-side-security/rules/violations/) for 24 hours after each change.
  * Document a rollback procedure before making changes.



## Pre-enforcement checklist

Complete the following checklist before switching a content security rule from _Log_ to _Allow_ :

  * The rule was tested in _Log_ mode for a minimum of seven days.
  * Reviewed all [rule violations](https://developers.cloudflare.com/client-side-security/rules/violations/) and confirmed there are no unexpected blocks.
  * Added all legitimate third-party resources to the rule allowlist.
  * Tested the application on all major browsers (Chrome, Firefox, Safari, Edge).
  * Configured [alerts](https://developers.cloudflare.com/client-side-security/alerts/) for rule violations.
  * There is a documented rollback procedure that is ready to execute.



Caution

Switching a rule from _Log_ to _Allow_ without completing this checklist may block resources required by your application. This will directly affect your end users.

## Rollback a rule change

If a rule change causes unexpected violations or blocks legitimate resources:

  1. Switch the rule action back to _Log_ to stop blocking resources immediately.
  2. Review the [rule violations](https://developers.cloudflare.com/client-side-security/rules/violations/) to identify which resources were blocked.
  3. Update the rule to include any missing resources.
  4. Repeat the validation process before switching back to _Allow_ (blocks resources not present in the allowlist).



[PreviousHandle an alert](https://developers.cloudflare.com/client-side-security/best-practices/handle-an-alert/)[NextConfiguration settings](https://developers.cloudflare.com/client-side-security/reference/settings/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/client-side-security/best-practices/deploy-rules-in-production.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
