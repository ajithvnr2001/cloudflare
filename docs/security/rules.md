---
url: https://developers.cloudflare.com/security/rules/
title: Security rules \u00b7 Security dashboard docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:30.406442+00:00
---

# Security rules · Security dashboard docs

> Source: https://developers.cloudflare.com/security/rules/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Security dashboard](https://developers.cloudflare.com/security/)
  3. /Security rules



# Security rules

Last updated Sep 8, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/security/rules/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSecurity rulesDDoS protectionInteraction between different app security features

Security rules perform security-related actions on incoming requests that match specified filters. Rules are evaluated and executed in order, from first to last.

You can create Security Rules from reviewed [Attack Signature Detection](https://developers.cloudflare.com/waf/detections/attack-signature-detection/use-attack-signatures-in-security-rules/) confidence, category, and Ref metadata.

To access security rules in the new security dashboard, go to the **Security rules** page.

[ Go to **Security rules** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/security-rules)

## Security rules

The **Security rules** tab includes a list of different types of rules configured in your domain/zone to protect your applications and resources.

To create a security rule:

  1. In the Cloudflare dashboard, go to the **Security rules** page.

[ Go to **Security rules** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/security-rules)
  2. (Optional) Select **Templates** , and then select a template from the list. You can customize the default configuration of the template before deploying the new rule. Refer to the resources listed in the next step.

  3. Select **Create rule** > select the type of rule you want to create. Refer to the following resources about each rule type:

     * [Custom rules](https://developers.cloudflare.com/waf/custom-rules/create-dashboard/#rule-form)
     * [Rate limiting rules](https://developers.cloudflare.com/waf/rate-limiting-rules/create-zone-dashboard/#rule-form)
     * [API sequence rules](https://developers.cloudflare.com/api-shield/security/sequence-mitigation/#rule-form)
     * [API JWT validation rules](https://developers.cloudflare.com/api-shield/security/jwt-validation/#rule-form) (requires a [token configuration](https://developers.cloudflare.com/security/settings/#all-settings))
     * [Managed rules exceptions](https://developers.cloudflare.com/waf/managed-rules/waf-exceptions/define-dashboard/#2-define-basic-exception-parameters)
     * [Content security rules](https://developers.cloudflare.com/client-side-security/rules/create-dashboard/#rule-form) (previously known as policies)



Notes

To deploy a managed ruleset, go to the Security **Settings** page. For more information, refer to [Deploy a managed ruleset](https://developers.cloudflare.com/waf/managed-rules/deploy-zone-dashboard/#deploy-a-managed-ruleset).

The **Security rules** tab includes functionality available in different products in the previous dashboard navigation structure, such as the [WAF](https://developers.cloudflare.com/waf/), [API Shield](https://developers.cloudflare.com/api-shield/), and [client-side security](https://developers.cloudflare.com/client-side-security/).

The tab may show additional rule types if you have configured at least one of the following:

  * [IP access rules](https://developers.cloudflare.com/waf/tools/ip-access-rules/)
  * [User agent blocking rules](https://developers.cloudflare.com/waf/tools/user-agent-blocking/)
  * [Zone lockdown rules](https://developers.cloudflare.com/waf/tools/zone-lockdown/)



## DDoS protection

The **DDoS protection** tab shows the multiple DDoS mitigation services provided by Cloudflare. You can create rules to override these mitigation tools. DDoS attack protection overrides are only available to Enterprise customers with the Advanced DDoS Protection subscription.

To learn more about DDoS protection overrides, refer to the following resources:

  * [HTTP DDoS attack protection overrides](https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/http-overrides/)
  * [Network-layer DDoS attack protection overrides](https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/network-overrides/)



Note

You define [overrides for the Network-layer DDoS attack protection managed ruleset](https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/network-overrides/configure-dashboard/) at the account level.

## Interaction between different app security features

If you are using several app security features like custom rules, Managed Rules, and Super Bot Fight Mode, it is important to understand how these features interact and the order in which they execute. Refer to [Security features interoperability](https://developers.cloudflare.com/waf/feature-interoperability/) for more information.

[PreviousDefine security protections](https://developers.cloudflare.com/security/web-assets/define-security-protections/)[NextSettings](https://developers.cloudflare.com/security/settings/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/security/rules.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
