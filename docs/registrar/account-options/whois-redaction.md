---
url: https://developers.cloudflare.com/registrar/account-options/whois-redaction/
title: WHOIS redaction \u00b7 Cloudflare Registrar docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:44.190445+00:00
---

# WHOIS redaction · Cloudflare Registrar docs

> Source: https://developers.cloudflare.com/registrar/account-options/whois-redaction/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Registrar](https://developers.cloudflare.com/registrar/)
  3. /[Registration options](https://developers.cloudflare.com/registrar/account-options/)
  4. /WHOIS redaction



# WHOIS redaction

Last updated Apr 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/registrar/account-options/whois-redaction/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhat is WHOIS redaction?What is RDAP?How can third parties reach registrants?

Cloudflare Registrar provides personal data redaction on WHOIS information, if permitted by the registry.

WHOIS is a standard for publishing the contact and nameserver information for all registered domains. Each registrar maintains their own WHOIS service. Anyone can query the registrar’s WHOIS service to reveal the data behind a given domain.

However, broadcasting the registrant contact information via the WHOIS service can cause spam mail to be delivered to your personal addresses. Cloudflare Registrar offers personal data redaction on WHOIS for free, that meets current ICANN guidelines.

Cloudflare’s WHOIS service can be found at <https://rdap.cloudflare.com/>[ ↗︎](https://rdap.cloudflare.com/). Select **WHOIS** as the search type.

## What is WHOIS redaction?

WHOIS redaction removes most contact information categorized as personal data (such as registrant name, email address, postal address) from the published WHOIS record for a domain. These fields will read `Data Redacted`. The nameserver, domain lock information, and date records for a domain are still available publicly. The following fields will continue to show in WHOIS, due to ICANN policy:

  * Registrant state/province
  * Registrant country



Cloudflare still maintains the authoritative, unredacted, record of your WHOIS data. You can modify this information at any time. Refer to [Registrant contact updates](https://developers.cloudflare.com/registrar/account-options/domain-contact-updates) for more information.

## What is RDAP?

RDAP (Registration Data Access Protocol) is a new standard for querying domain contact and nameserver information for all registered domains. This new protocol offers some advantages over WHOIS, including standardized data access, support for internationalization, and secure access controls. RDAP is intended to eventually replace WHOIS. However, Cloudflare currently provides both WHOIS and RDAP search capability.

Cloudflare’s RDAP service can be found at <https://rdap.cloudflare.com/>[ ↗︎](https://rdap.cloudflare.com/). Select **RDAP** as the search type.

## How can third parties reach registrants?

As part of the ICANN guidelines, registrars must have a method for third parties to reach the registrant without revealing their identity. Cloudflare has a form available where third parties can [submit a message for a given domain on Cloudflare Registrar ↗︎](https://www.cloudflare.com/abuse/form). Cloudflare will forward the message to the registrant email on file for that domain.

[PreviousOverview](https://developers.cloudflare.com/registrar/account-options/)[NextDomain ownership certificate](https://developers.cloudflare.com/registrar/account-options/domain-ownership-certificate/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/registrar/account-options/whois-redaction.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
