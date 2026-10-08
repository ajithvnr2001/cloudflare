---
url: https://developers.cloudflare.com/cloudflare-one/email-security/reference/dispositions-and-attributes/
title: Dispositions and attributes \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:35.064564+00:00
---

# Dispositions and attributes · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/email-security/reference/dispositions-and-attributes/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

  4. /Reference
  5. /Dispositions and attributes



# Dispositions and attributes

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/email-security/reference/dispositions-and-attributes/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewDispositions Available values Header structureAttributes Available values Header structure

Email security uses a variety of factors to determine whether a given email message, domain, URL, or packet is part of a phishing campaign. These small pattern assessments are dynamic in nature and — in many cases — no single pattern will determine the final verdict.

Detection vs. disposition

Detection is the process Email security does to identify what threat an email may contain. An email can have multiple detections, but they will only have one and final disposition. The detections an email have will determine the disposition of the email.

## Dispositions

Any traffic that flows through Email security is given a final disposition, which represents our evaluation of that specific message. Each message will receive only one disposition header, so your organization can take clear and specific actions on different message types.

You can use disposition values when [setting up auto-moves](https://developers.cloudflare.com/cloudflare-one/email-security/settings/auto-moves/).

### Available values

The following disposition values follow an order of maliciousness:

  * **Malicious** : Traffic associated with active threat campaigns. Malicious messages invoked multiple phishing verdict triggers and met thresholds for bad behavior. 
    * **Recommendation** : Block.
  * **Spam** : Traffic associated with non-malicious, commercial campaigns. 
    * **Recommendation** : Route to existing Spam quarantine folder.
  * **Bulk** : Traffic often associated with newsletters or marketing campaigns. Refer to [Graymail ↗︎](https://en.wikipedia.org/wiki/Graymail_%28email%29) for more details. 
    * **Recommendation** : Monitor or tag.
  * **Suspicious** : Traffic associated with phishing campaigns (and is under further analysis by our automated systems). 
    * **Recommendation** : Research these messages internally to evaluate legitimacy.
  * **Spoof** : Traffic associated with phishing campaigns that is either non-compliant with your email authentication policies ([SPF ↗︎](https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-spf-record/), [DKIM ↗︎](https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-dkim-record/), [DMARC ↗︎](https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-dmarc-record/)) or has mismatching `Envelope From` and `Header From` values. 
    * **Recommendation** : Block after investigating (can be triggered by third-party mail services).



### Header structure

When Email security adds a disposition header to an email message, that header matches the following format:
    
    
    X-CFEmailSecurity-Disposition: [Value]

Note that emails with a disposition of `SPAM` will be tagged with `UCE` (unsolicited commercial emails) in their headers:
    
    
    X-CFEmailSecurity-Disposition: UCE

## Attributes

Traffic that flows through Email security can also receive one or more Attributes, which indicate that a specific condition has been met.

### Available values

Attribute | Notes  
---|---  
`CUSTOM_BLOCK_LIST` | This message matches a value you have defined in your custom block list.  
`NEW_DOMAIN_SENDER=<REGISTRATION_DATE>` | Alerts to mail from a newly registered domain. Formatted as yyyy-MM-dd HH:mm:ss ZZZ.  
`NEW_DOMAIN_LINK=<REGISTRATION_DATE>` | Alerts to mail with links pointing out to a newly registered domain. Formatted as yyyy-MM-dd HH:mm:ss ZZZ.  
`ENCRYPTED` | Email message is encrypted.  
`EXECUTABLE` | Email message contains an executable file.  
`BEC` | Indicates that an email address was contained in your [impersonation registry](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/impersonation-registry/) list. Associated with `MALICIOUS` or `SPOOF` dispositions.  
  
### Header structure

When Email security adds a disposition header to an email message, that header matches the following format:
    
    
    X-CFEmailSecurity-Attribute: [Value]
    X-CFEmailSecurity-Attribute: [Value2]

[PreviousHow Email security detects phish](https://developers.cloudflare.com/cloudflare-one/email-security/reference/how-es-detects-phish/)[NextRegional processing](https://developers.cloudflare.com/cloudflare-one/email-security/reference/regional-processing/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/email-security/reference/dispositions-and-attributes.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
