---
url: https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/exclude-prefix/
title: Exclude a prefix \u00b7 Cloudflare DDoS Protection docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:45.640917+00:00
---

# Exclude a prefix · Cloudflare DDoS Protection docs

> Source: https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/exclude-prefix/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DDoS Protection](https://developers.cloudflare.com/ddos-protection/)
  3. /…

Advanced DDoS systems

  4. /How to
  5. /Exclude a prefix



# Exclude a prefix

Last updated Apr 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/exclude-prefix/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

To exclude a prefix or a prefix subset from Advanced DDoS Protection:

  1. In the Cloudflare dashboard, go to the **L3/4 DDoS protection** page.

[ Go to **DDoS Managed Rules** ↗ ](https://dash.cloudflare.com/?to=/:account/network-security/ddos)
  2. Go to **Advanced Protection**.

  3. [Add the prefix](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/add-prefix/) you previously onboarded to Magic Transit to Advanced TCP Protection.

  4. [Add the prefix](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/add-prefix/) (or subset) you wish to exclude as a new, separate prefix in Advanced TCP Protection.

  5. For the prefix you added in the previous step, select **Exclude Subset** in the **Enrolled Prefixes** list.




Note

Prefixes or subsets added as _Excluded_ will not be protected by Advanced TCP Protection.

[PreviousCreate a filter](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/create-filter/)[NextConfigure via the API](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/dns-protection/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ddos-protection/advanced-ddos-systems/how-to/exclude-prefix.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
