---
url: https://developers.cloudflare.com/network-interconnect/maintenance/
title: Maintenance \u00b7 Cloudflare Network Interconnect docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:24.908880+00:00
---

# Maintenance · Cloudflare Network Interconnect docs

> Source: https://developers.cloudflare.com/network-interconnect/maintenance/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Network Interconnect](https://developers.cloudflare.com/network-interconnect/)
  3. /Maintenance



# Maintenance

Last updated Sep 11, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/network-interconnect/maintenance/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPlanned maintenance Timing and schedulingEmergency and non-routine maintenanceReceive maintenance notifications

## Planned maintenance

Routine CNI-disruptive maintenance is planned work that can interrupt traffic on an affected CNI connection. Cloudflare coordinates this work across resilient Cloudflare Network Interconnect (CNI) deployments, including across CNI locations.

### Timing and scheduling

For Dataplane v2 connectivity in multi-homed PoPs only:

  * **Routine maintenance** : Minimum one week notice.
  * **Emergency maintenance** : Best-effort notice, which may be less than one week.
  * Routine maintenance on redundant devices at the same location will occur on different days.
  * Routine maintenance is not rescheduled to accommodate customer schedule preferences.



CNI deployment | During routine CNI-disruptive maintenance  
---|---  
One CNI connection at one location | The connection can be interrupted.  
Two CNI connections on separate devices at one location | One connection remains in service.  
Four CNI connections across two coordinated locations, with two connections on separate devices at each location | Three connections remain in service.  
  
## Emergency and non-routine maintenance

Non-routine maintenance, such as maintenance that affects an entire PoP, can affect all CNI connections at the affected location. For the four-connection deployment with two connections at each of two locations, a full-PoP non-routine event at one location can interrupt two connections, leaving two in service. Cloudflare avoids performing non-routine maintenance at multiple coordinated locations at the same time.

Cloudflare coordinates emergency maintenance across locations where feasible.

## Receive maintenance notifications

To configure circuit-specific or point-of-presence (PoP) maintenance notifications, refer to [Monitoring and alerts](https://developers.cloudflare.com/network-interconnect/monitoring-and-alerts/).

[PreviousMonitoring and alerts](https://developers.cloudflare.com/network-interconnect/monitoring-and-alerts/)[NextOperational guidance](https://developers.cloudflare.com/network-interconnect/operational-guidance/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/network-interconnect/maintenance.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
