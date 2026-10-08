---
url: https://developers.cloudflare.com/cloudflare-one/insights/analytics/network-sessions/
title: Network session analytics \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:47.824815+00:00
---

# Network session analytics · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/insights/analytics/network-sessions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Insights](https://developers.cloudflare.com/cloudflare-one/insights/)

  4. /[Dashboards](https://developers.cloudflare.com/cloudflare-one/insights/analytics/)
  5. /Network session analytics



# Network session analytics

Last updated Sep 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/insights/analytics/network-sessions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUse casesProvided analytics Summary metrics Traffic by location Top analytics Troubleshoot session limit errorsRelated resources

The Network session analytics dashboard provides visibility into your Cloudflare One traffic patterns. This dashboard helps you understand how traffic flows through your network, including on-ramps (how traffic enters Cloudflare, such as the [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/), [proxy endpoints (PAC files)](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/), [Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/), [Cloudflare Mesh](https://developers.cloudflare.com/mesh/), [Workers VPC](https://developers.cloudflare.com/workers-vpc/), or Cloudflare Tunnel) and off-ramps (how traffic exits Cloudflare, such as the public Internet, a [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/), or a Mesh node).

The dashboard is based on the [Zero Trust network sessions Logpush dataset](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/). For definitions on any field, refer to the dataset schema documentation.

To review Network session analytics:

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Insights** > **Dashboards**.
  2. Select **Network session analytics**.



Refer to [Insights overview](https://developers.cloudflare.com/cloudflare-one/insights/) to learn how to use Analytics dashboards together with [Analytics Overview](https://developers.cloudflare.com/cloudflare-one/insights/analytics-overview/) and [Digital Experience Monitoring (DEX)](https://developers.cloudflare.com/cloudflare-one/insights/dex/) for complete visibility and troubleshooting.

## Use cases

The Network session analytics dashboard helps you:

  * **Understand traffic patterns** : Visualize how traffic flows through your network infrastructure.
  * **Monitor bandwidth usage** : Track upload, download, and total bytes transferred across your network.
  * **Identify connection issues** : Analyze connection close reasons to troubleshoot network problems.
  * **Track user and device activity** : Monitor unique users and devices accessing your network.



## Provided analytics

### Summary metrics

  * **Session count** : Total number of network sessions. Each session represents an individual TCP, UDP, ICMP, or ICMPv6 flow that passes through Gateway.
  * **Bytes total** : Total bytes transferred (upload + download)
  * **Unique users** : Number of distinct users



### Traffic by location

  * **World map** : Geographic visualization of network traffic by the Cloudflare data center where traffic entered the network (ingress) and where it exited (egress)
  * **Location list** : Top Cloudflare data center locations by ingress and egress session count with accompanying graph
  * **Change** : Shows the total change across ingress and egress for each location



### Top analytics

  * **Top protocols** : Most used network protocols (TCP, UDP, ICMP, ICMPv6)
  * **Top connection close reasons** : Common reasons for session termination: 
    * Client closed
    * Origin closed
    * Client idle timeout
    * Client error
    * Unknown
    * Client TLS error
    * Origin unreachable
    * Too many new sessions for user
    * Origin TLS error
    * Origin unroutable



For the full list of reasons for session termination, refer to [ConnectionCloseReason](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/#connectionclosereason).

### Troubleshoot session limit errors

Session limit close reasons identify the type and scope of a limit. Reasons containing `ACTIVE_SESSIONS` indicate too many concurrent sessions. Reasons containing `NEW_SESSIONS` indicate that sessions are being created too quickly. `FOR_ACCOUNT` reasons aggregate sessions for the account on the Cloudflare server enforcing the limit and can affect multiple users connected to that server. `FOR_USER` reasons apply to one user.

Use [Zero Trust Network Session Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/), not Gateway activity logs, to investigate these errors. Filter by `ConnectionCloseReason`, then correlate `SessionStartTime` and `SessionID` with fields such as `Email`, `UserID`, `DeviceID`, `SourceIP`, `OriginIP`, `OriginPort`, `Protocol`, and `ConnectionReuse`.

Reduce automatic retries and connection churn in the affected application. Reuse connections when the application and protocol support it. If expected sustained traffic continues to produce these errors, contact your account team or [Cloudflare Support](https://developers.cloudflare.com/cloudflare-one/troubleshooting/contact-support/) for review.

## Related resources

  * [Zero Trust network sessions Logpush dataset](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/): View detailed logs for individual network sessions.
  * [Gateway network policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/): Configure policies that apply to network traffic.



[PreviousAI prompt logs ↗︎](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/#log-generative-ai-prompt-content)[NextPassive Detection ↗︎](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/passive-detection/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/insights/analytics/network-sessions.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
