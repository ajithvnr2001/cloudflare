---
url: https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/add-prefix/
title: Add a prefix to Advanced DDoS Protection \u00b7 Cloudflare DDoS Protection docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:45.488250+00:00
---

# Add a prefix to Advanced DDoS Protection · Cloudflare DDoS Protection docs

> Source: https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/add-prefix/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DDoS Protection](https://developers.cloudflare.com/ddos-protection/)
  3. /…

Advanced DDoS systems

  4. /How to
  5. /Add a prefix



# Add a prefix

Last updated Jun 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/add-prefix/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

To add a [prefix](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/concepts/#prefixes) to Advanced DDoS Protection:

  1. In the Cloudflare dashboard, go to the **L3/4 DDoS protection** page.

[ Go to **DDoS Managed Rules** ↗ ](https://dash.cloudflare.com/?to=/:account/network-security/ddos)
  2. Go to **Advanced Protection**.

  3. Under **General settings** > **Prefixes** , select **Edit**.

  4. Expand the **Add existing prefix** section and select **Add** next to the prefix you wish to add.  
Alternatively, enter a prefix and (optionally) a description in **Prefix** and **Description** , respectively, and select **Add**.




Note

The **Add existing prefix** list will not display leased prefixes, but you can add them manually in the Cloudflare dashboard or [using the API](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/). You cannot add [delegated prefixes](https://developers.cloudflare.com/byoip/concepts/prefix-delegations/) to Advanced TCP Protection.

[PreviousConcepts](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/concepts/)[NextAdd an IP or prefix to the allowlist](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/add-prefix-allowlist/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ddos-protection/advanced-ddos-systems/how-to/add-prefix.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
