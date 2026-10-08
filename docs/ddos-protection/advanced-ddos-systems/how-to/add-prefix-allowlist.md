---
url: https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/add-prefix-allowlist/
title: Add an IP address/prefix to the Advanced DDoS Protection allowlist \u00b7 Cloudflare DDoS Protection docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:45.448112+00:00
---

# Add an IP address/prefix to the Advanced DDoS Protection allowlist · Cloudflare DDoS Protection docs

> Source: https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/add-prefix-allowlist/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DDoS Protection](https://developers.cloudflare.com/ddos-protection/)
  3. /…

Advanced DDoS systems

  4. /How to
  5. /Add an IP or prefix to the allowlist



# Add an IP or prefix to the allowlist

Last updated Jun 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/add-prefix-allowlist/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

To add an IP address or prefix to the Advanced DDoS Protection [allowlist](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/concepts/#allowlist):

  1. In the Cloudflare dashboard, go to the **L3/4 DDoS protection** page.

[ Go to **DDoS Managed Rules** ↗ ](https://dash.cloudflare.com/?to=/:account/network-security/ddos)
  2. Go to **Advanced Protection**.

  3. Under **General settings** > **Allowlist** , select **Edit**.

  4. Enter a prefix and (optionally) a description in **Prefix** and **Description** , respectively.

  5. To exclude the current prefix from the allowlist instead of including it, uncheck the **Enabled** checkbox. 6. Select **Add**.




Allowlists support approximately 200 IP addresses in a single expression for a rule.

Important

Prefixes in the allowlist will be vulnerable to IP spoofing attacks. If an attacker can guess the source IP addresses you have allowlisted, their packets will be allowlisted.

[PreviousAdd a prefix](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/add-prefix/)[NextCreate a rule](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/create-rule/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ddos-protection/advanced-ddos-systems/how-to/add-prefix-allowlist.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
