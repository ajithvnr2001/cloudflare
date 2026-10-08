---
url: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/device-metrics/
title: Device metrics \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:25.475832+00:00
---

# Device metrics · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/device-metrics/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

NetworksConnectors[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/)Configuration

  4. /[Configure with Connector](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/)
  5. /Device metrics



# Device metrics

Last updated Aug 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/device-metrics/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewQuery metrics with GraphQL Average CPU load explained

Cloudflare customers can inspect metrics for a specific Cloudflare One Appliance (formerly Magic WAN Connector) in the Cloudflare dashboard. These metrics help you troubleshoot potential issues with your Cloudflare One Appliance. For details, refer to [Troubleshooting](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/troubleshooting/).

## Query metrics with GraphQL

Customers can query Cloudflare's GraphQL API to fetch their Cloudflare One Appliance device metrics. The Cloudflare dashboard displays Cloudflare One Appliance device metrics over the past one hour. Via the GraphQL API, customers can query for up to 30 days of historical Cloudflare One Appliance device metrics.

For example:
    
    
    query telemetry(
      $accountTag: string
      $snapshotsFilter: AccountMconnTelemetrySnapshotsAdaptiveGroupsFilter_InputObject!
      $snapshotMountsFilter: AccountMconnTelemetrySnapshotMountsAdaptiveGroupsFilter_InputObject!
      $snapshotThermalsFilter: AccountMconnTelemetrySnapshotThermalsAdaptiveGroupsFilter_InputObject!
      $limit: int64!
    ) {
      viewer {
        accounts(filter: { accountTag: $accountTag }) {
          snapshots: mconnTelemetrySnapshots(
            filter: $snapshotsFilter
            limit: $limit
            orderBy: [datetimeFiveMinutes_DESC]
          ) {
            max {
              cpuCount
              loadAverage1m
              memoryFreeBytes
              memoryTotalBytes
            }
            dimensions {
              connectorId
              datetimeFiveMinutes
            }
          }
          snapshotMounts: mconnTelemetrySnapshotMounts(
            filter: $snapshotMountsFilter
            limit: $limit
            orderBy: [datetimeFiveMinutes_DESC]
          ) {
            max {
              availableBytes
              totalBytes
            }
            dimensions {
              connectorId
              datetimeFiveMinutes
            }
          }
          snapshotThermals: mconnTelemetrySnapshotThermals(
            filter: $snapshotThermalsFilter
            limit: $limit
            orderBy: [datetimeFiveMinutes_DESC, connectorId_DESC]
          ) {
            max {
              currentCelsius
            }
            dimensions {
              connectorId
              datetimeFiveMinutes
            }
          }
        }
      }
    }

### Average CPU load explained

The metric `average CPU load` is unique and distinctly different from `CPU utilization` which is another common CPU metric. The Cloudflare One Appliance uses a [Unix-style CPU load calculation ↗︎](https://en.wikipedia.org/wiki/Load_\(computing\)).

CPU load is a measure of the number of processes that are currently running and that are waiting to be run on the CPU. Cloudflare collects the one minute load average from the device and converts that into a percentage based on the total number of cores in the CPU. If the Cloudflare One Appliance CPU has eight cores, and a one minute load average of two, then the average CPU load is 25%. If the average CPU load is above 100%, then there are processes in the queue that are waiting to be executed on the CPU.

Cloudflare is still evaluating the typical CPU load operating range on the Cloudflare One Appliance. In general, a healthy range for average CPU load on any device is between 30% and 70%. Customers may experience decreased Cloudflare One Appliance performance if the average CPU load is consistently above 100%.

[PreviousAppliance operations](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/maintenance/appliance-operations/)[NextReference](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/reference/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/device-metrics.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
