---
url: https://developers.cloudflare.com/waf/glossary/
title: Glossary \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:42.916763+00:00
---

# Glossary · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/glossary/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /Glossary



# Glossary

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/glossary/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Review the definitions for terms used across Cloudflare's WAF documentation.

Term| Definition  
---|---  
allowlist| An allowlist is a list of items (usually websites, IP addresses, email addresses, etc.) that are permitted to access a system.  
attack score| A number from 1 (likely malicious) to 99 (likely clean) classifying how likely an incoming request is malicious or not. Allows you to detect new attack techniques before they are publicly known.  
blocklist| A blocklist is a list of items (usually websites, IP addresses, email addresses, etc.) that are prevented from accessing a system.  
content object| A content object is any binary part of a request body (as detected by Cloudflare systems) that does not match any of the following content types: `text/html`, `text/x-shellscript`, `application/json`, `text/csv`, or `text/xml`.  
credential stuffing| Credential stuffing is the automated injection of stolen username and password pairs (known as "credentials") into website login forms, trying to gain access to user accounts.  
firewall| A firewall is a security system that monitors and controls network traffic based on a set of security rules.  
leaked credentials| Leaked credentials refers to sensitive authentication information disclosed in some way (for example, due to misconfigurations, data breaches, or simple human error), allowing other parties to gain access to digital resources. Credentials may include usernames, passwords, API keys, authentication tokens, or private keys.  
LLM| A machine learning model that can comprehend and generate human language text. It works by analyzing massive data sets of language.  
mitigated request| A request to which Cloudflare applied a terminating action such as block or challenge.  
paranoia level| Classifies rules of the OWASP managed ruleset according to their aggressiveness.  
prompt injection| The process of overwriting the system prompt for a large language model (LLM), which instructs the LLM on how to respond to user input.  
rate limiting| Rate limiting is a technique used in computer systems to control the rate at which requests are processed. It can be used as a security measure to prevent attacks, or to limit resource usage in your origin servers.  
rule characteristics| The set of parameters of a rate limiting rule that define how Cloudflare tracks the rate for the rule.  
SIEM| A Security Information and Event Management (SIEM) solution collects, analyzes, and correlates data to help manage security incidents, detect anomalies, and meet compliance requirements.  
threat score| The threat score was a score from `0` (zero risk) to `100` (high risk) classifying the IP reputation of a visitor. Currently, the threat score is always `0` (zero).  
zero-shot classification model| A pretrained machine learning model capable of categorizing data (text or images) into classes it has never seen during training.  
  
[PreviousFAQ](https://developers.cloudflare.com/waf/troubleshooting/faq/)[NextOverview](https://developers.cloudflare.com/waf/change-log/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/glossary.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
