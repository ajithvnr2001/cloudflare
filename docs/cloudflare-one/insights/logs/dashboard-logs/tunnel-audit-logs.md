---
url: https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/tunnel-audit-logs/
title: Tunnel audit logs \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:52.406979+00:00
---

# Tunnel audit logs · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/tunnel-audit-logs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Insights](https://developers.cloudflare.com/cloudflare-one/insights/)[Logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/)

  4. /[Dashboard logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/)
  5. /Tunnel audit logs



# Tunnel audit logs

Last updated May 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/tunnel-audit-logs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) creates outbound-only connections between your infrastructure and Cloudflare. Tunnel audit logs record when these connections start, stop, or register new DNS records.

Audit logs for Tunnel are available in the [account section of the Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?account=audit-log), which you can find by selecting your name or email in the upper right-hand corner of the dashboard. For general audit log features such as filtering and retention, refer to [Audit Logs](https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/). The following actions are logged:

Action | Description  
---|---  
Registered | A tunnel connector (`cloudflared`) started and connected to Cloudflare's global network.  
Unregistered | A tunnel connector disconnected from Cloudflare's global network.  
CNAME add | A tunnel registered a new DNS record (CNAME or AAAA) to route traffic to an application behind the tunnel.  
  
[PreviousPosture logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/posture-logs/)[NextOverview](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/insights/logs/dashboard-logs/tunnel-audit-logs.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
