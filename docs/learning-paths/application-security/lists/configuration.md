---
url: https://developers.cloudflare.com/learning-paths/application-security/lists/configuration/
title: Configurations \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:43.049850+00:00
---

# Configurations · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/application-security/lists/configuration/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Application Security

  4. /[Lists](https://developers.cloudflare.com/learning-paths/application-security/lists/)
  5. /Configurations



# Configurations

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/application-security/lists/configuration/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCustom ListsManaged ListsCreating a rule

Both Custom and Managed Lists are located in the account settings. Refer to [Features by plan type](https://developers.cloudflare.com/learning-paths/application-security/lists/features/) for more information on plan eligibility.

## Custom Lists

Using a Custom List is an alternative to creating individual Firewall rules with long lists of IP addresses or other types of identifiers. They are easier to read and update, especially when they are used across many security rules. Lists are often used in conjunction with in-house or third party security feeds.

## Managed Lists

The following lists are managed by the Cloudflare team and are regularly updated.

Display name | Name in expressions | Description  
---|---|---  
Cloudflare Open Proxies | `cf.open_proxies` | IP addresses of known open HTTP and SOCKS proxy endpoints, which are frequently used to launch attacks and hide attackers identity.  
Cloudflare Anonymizers | `cf.anonymizer` | IP addresses of known anonymizers (Open SOCKS Proxies, VPNs, and TOR nodes).  
Cloudflare VPNs | `cf.vpn` | IP addresses of known VPN servers.  
Cloudflare Malware | `cf.malware` | IP addresses of known sources of malware.  
Cloudflare Botnets, Command and Control Servers | `cf.botnetcc` | IP addresses of known botnet command-and-control servers.  
  
  


## Creating a rule

Refer to [Use lists in expressions](https://developers.cloudflare.com/waf/tools/lists/use-in-expressions/) to learn how to invoke a Managed List.

[PreviousUse cases](https://developers.cloudflare.com/learning-paths/application-security/lists/use-cases/)[NextOverview](https://developers.cloudflare.com/learning-paths/application-security/security-center/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/application-security/lists/configuration.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
