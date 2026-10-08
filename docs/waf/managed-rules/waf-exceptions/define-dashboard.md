---
url: https://developers.cloudflare.com/waf/managed-rules/waf-exceptions/define-dashboard/
title: Add a WAF exception in the dashboard \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:45.663714+00:00
---

# Add a WAF exception in the dashboard · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/managed-rules/waf-exceptions/define-dashboard/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Managed rules](https://developers.cloudflare.com/waf/managed-rules/)

  4. /[Create exceptions](https://developers.cloudflare.com/waf/managed-rules/waf-exceptions/)
  5. /Add an exception in the dashboard



# Add an exception in the dashboard

Last updated Aug 3, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/managed-rules/waf-exceptions/define-dashboard/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview1\. Go to the zone or account dashboard page2\. Define basic exception parameters3\. Select the rules to skip4\. Create the exception5\. (Optional) Edit the exception

## 1\. Go to the zone or account dashboard page

To add an exception at the zone level:

  1. In the Cloudflare dashboard, go to the **Security rules** page.

[ Go to **Security rules** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/security-rules)
  2. Select **Create** > **Managed rules**.




To add an exception at the account level (Enterprise plans only):

  1. In the Cloudflare dashboard, go to the **WAF** page.

[ Go to **WAF** ↗ ](https://dash.cloudflare.com/?to=/:account/application-security/waf)
  2. Go to the **Managed rulesets** tab.

  3. Select **Deploy** > **Deploy managed exception**.




## 2\. Define basic exception parameters

  1. In **Exception name** , enter a name for the exception.

![The Add exception page in the Cloudflare dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=952,height=690,format=webp/_astro/waf-exception-create.DGVMUWUU.png)
  2. In **When incoming requests match** , specify a filter expression that defines the conditions for applying the exception. When the expression matches, the WAF will evaluate the exception skipping one or more rules of WAF managed rulesets. The filter expression uses the [Rules language](https://developers.cloudflare.com/ruleset-engine/rules-language/).




## 3\. Select the rules to skip

  1. In **Then** , select the [exception type](https://developers.cloudflare.com/waf/managed-rules/waf-exceptions/#types-of-exceptions) that determines which rules to skip:

     * **Skip all remaining rules** : Skips all remaining rules of WAF managed rulesets. If you select this option, proceed to 4\. Create the exception.
     * **Skip specific rules from a Managed Ruleset** : Skips one or more rules of a managed ruleset.
  2. Select **Select ruleset**.

  3. Next to the ruleset containing the rule(s) you wish to skip, select **Select rules**.

  4. **A) To skip one or more rules in the ruleset:**

     1. Search for a rule using the available filters. You can search by description, rule ID, or tag. For example, in the Cloudflare OWASP Core Ruleset you can search for `920460` to find the rule `920460: Abnormal character escapes in request`.
     2. Select the checkbox next to the rule(s) you want to skip.
     3. If required, search for other rules and select them. The dashboard keeps a list of the rules you selected between searches.

**B) To skip all the rules in the ruleset:**

     1. Select all the rules in the current page by selecting the checkbox in the table header, near **Description/Rule ID**. The table header will display `10 rules selected (of <TOTAL> rules)`.

![Rule selection page showing the option to select all the rules in the ruleset](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=616,height=202,format=webp/_astro/waf-exception-select-all-rules.CBp6LP58.png)
     2. Select **Select all <TOTAL> rules** in the table header to select all the rules across all pages.

  5. Select **Next**.




## 4\. Create the exception

  1. (Optional) To disable logging for requests matching the exception, disable **Log matching requests**.

  2. To save and deploy your exception, select **Deploy**. If you are not ready to deploy your exception, select **Save as Draft**.




## 5\. (Optional) Edit the exception

To edit an exception at the zone level:

  1. In the Cloudflare dashboard, go to the **Security rules** page.

[ Go to **Security rules** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/security-rules)
  2. (Optional) Filter by **Managed Rules**.

  3. Find the exception you want to edit and select its name. Exceptions are rules listed with **Action** = **Skip**.

  4. Once you have finished making changes, select **Save**.  
Alternatively, to delete the exception, select **Delete exception**.




To edit an exception at the account level (Enterprise plans only):

  1. In the Cloudflare dashboard, go to the **WAF** page.

[ Go to **WAF** ↗ ](https://dash.cloudflare.com/?to=/:account/application-security/waf)
  2. Go to the **Managed rulesets** tab.

  3. Find the exception you want to edit and select its name. Exceptions are rules listed with **Action** = **Skip**.

  4. Once you have finished making changes, select **Save**.  
Alternatively, to delete the exception, select **Delete exception**.




Note

Exceptions only apply to rules executing a managed ruleset listed after them. For example, if you are skipping a rule belonging to the Cloudflare OWASP Core Ruleset, make sure the exception is listed in the rules list before the _Execute_ rule deploying this managed ruleset.

[PreviousOverview](https://developers.cloudflare.com/waf/managed-rules/waf-exceptions/)[NextAdd an exception via API](https://developers.cloudflare.com/waf/managed-rules/waf-exceptions/define-api/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/managed-rules/waf-exceptions/define-dashboard.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
