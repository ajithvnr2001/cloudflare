---
url: https://developers.cloudflare.com/api-shield/security/sequence-mitigation/manage-sequence-rules/
title: Manage sequence rules \u00b7 Cloudflare API Shield docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:19.396411+00:00
---

# Manage sequence rules · Cloudflare API Shield docs

> Source: https://developers.cloudflare.com/api-shield/security/sequence-mitigation/manage-sequence-rules/

  1. [Home](https://developers.cloudflare.com/)
  2. /[API Shield](https://developers.cloudflare.com/api-shield/)
  3. /…

[Security](https://developers.cloudflare.com/api-shield/security/)

  4. /[Sequence mitigation](https://developers.cloudflare.com/api-shield/security/sequence-mitigation/)
  5. /Manage sequence rules



# Manage sequence rules

Last updated Sep 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/api-shield/security/sequence-mitigation/manage-sequence-rules/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate a sequence ruleEdit a sequence ruleReprioritize a sequence rule

Cloudflare recommends creating sequence rules using WAF custom rules. Refer to the [sequence custom rules documentation](https://developers.cloudflare.com/api-shield/security/sequence-mitigation/custom-rules/) for more information.

Note

Sequence mitigation is currently in a closed beta and is only available for Enterprise customers. If you would like to be included in the beta, contact your account team.

## Create a sequence rule

The starting and ending endpoints must use the same hostname.

  1. In the Cloudflare dashboard, go to the **Security rules** page.

[ Go to **Security rules** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/security-rules)
  2. Select **Create rule** and choose **API sequence rules**.

  3. Name your rule.

  4. Select a starting endpoint. This is the endpoint that you expect users to hit first in their request flow when using your API.

     * Choose a hostname to display the list of endpoints for that hostname.
     * Choose an endpoint.
     * Select **Set as starting endpoint**.
  5. Select a final endpoint. This is the endpoint you are targeting for protection.

     * Choose the same hostname as the starting endpoint to display its endpoints.
     * Choose an endpoint.
     * Select **Set as ending endpoint**.
  6. Choose an action that corresponds to the security model type:

     * **Allow** : This will create a positive security model by defining approved sequences on your API.
     * **Log** / **Block** : This will test or enforce a negative security model defining known bad sequences on your API.

Note

If you chose **Allow** , select whether to log or block the request to the final endpoint when users do not first request the starting endpoint in the sequence.

  7. Select **Create rule**.




## Edit a sequence rule

You also have the option to edit an existing rule by selecting it on the rule list. You can rename your rule, adjust the starting and ending endpoint order, modify the endpoint, and change the action of the rule.

## Reprioritize a sequence rule

You can change the priority order of your rules by selecting and dragging the rules on the list.

You can also explicitly set a priority order by selecting the three dots on your rule and choosing **Move to…** where you can set the new priority in the resulting modal window.

[PreviousOverview](https://developers.cloudflare.com/api-shield/security/sequence-mitigation/)[NextAPI](https://developers.cloudflare.com/api-shield/security/sequence-mitigation/api/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/api-shield/security/sequence-mitigation/manage-sequence-rules.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
