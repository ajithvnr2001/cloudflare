---
url: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/
title: Tunnel log streams \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:17.342720+00:00
---

# Tunnel log streams · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

NetworksConnectors[Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

  4. /[Monitor tunnels](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/)
  5. /Log streams



# Log streams

Last updated Sep 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewView logs on the serverView logs on your local machine Dashboard CLI Performance considerationsNetwork session logs

Tunnel logs record all activity between a `cloudflared` instance and Cloudflare's global network, as well as all activity between `cloudflared` and your origin server. These logs allow you to investigate connectivity or performance issues with a Cloudflare Tunnel. You can configure your server to store persistent logs, or you can stream real-time logs from any client machine.

## View logs on the server

If you have access to the origin server, you can use the [`--loglevel` flag](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/run-parameters/#loglevel) to enable logging when you start the tunnel. By default, `cloudflared` writes logs to standard error (`stderr`) and does not store logs on the server.

Note

Requires `cloudflared` version 2025.6.1 or later.

To format each log line as a JSON object, add `--output json` before `run`:
    
    
    cloudflared tunnel --output json run <UUID>

This format is useful for Kubernetes deployments and log collection systems that consume JSON.

For routine persistent logging, [run the tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/run-parameters/#add-run-parameters-to-tunnel-service#log-directory) with `--log-directory <PATH>`. This flag writes logs to `cloudflared.log` in the specified directory, rotates the file when it reaches 1 MB, and keeps up to five backups. It does not remove logs based on age.
    
    
    cloudflared tunnel --loglevel info --log-directory <PATH> run <UUID>

Use the [`--logfile` flag](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/run-parameters/#logfile) instead for short troubleshooting sessions or when another tool manages rotation. `cloudflared` does not rotate the file specified by `--logfile`. If you set both flags, `--logfile` takes precedence.

## View logs on your local machine

You can view real-time logs for a Cloudflare Tunnel via the dashboard or from any machine that has `cloudflared` installed. With remote log streams, you do not need to SSH into the server that is running the tunnel. To get remote logs, the tunnel must be active and able to receive requests.

### Dashboard

Note

Tunnel log streams require [edit permissions](https://developers.cloudflare.com/fundamentals/manage-members/roles/) for Cloudflare Tunnel. Due to the sensitive nature of these logs, read-only roles (such as `Zero Trust Read Only`) do not have access.

To stream tunnel logs from the dashboard:

  1. In the Cloudflare dashboard, go to **Networking** > **Tunnels** and select your tunnel.

[ Go to **Tunnels** ↗ ](https://dash.cloudflare.com/?to=/:account/tunnels)
  2. Go to the **Live logs** tab.

  3. Select **Live** to start streaming.




#### View logs for a replica

If you are running multiple `cloudflared` instances for the same tunnel (also known as [replicas](https://developers.cloudflare.com/tunnel/configuration/#replicas-and-high-availability)), logs from all connected replicas are streamed automatically and grouped by hostname, making it easy to identify which host machine produced each log entry.

To filter the stream to specific replicas, select the **Filter** icon and expand the **Replicas** section. You can also filter by **Log Level** and **Event Type**.

### CLI

The `cloudflared` daemon can stream logs from any tunnel in your account to the local command line. `cloudflared` must be installed on both your local machine and the origin server.

The `cloudflared` daemon can stream logs from any tunnel in your account to the local command line. `cloudflared` must be installed on both your local machine and the origin server.

  1. On your local machine, authenticate `cloudflared` to your Cloudflare account:
         
         cloudflared tunnel login

  2. Run `cloudflared tail` for a specific tunnel:
         
         cloudflared tail <UUID>

For a more structured view of the JSON message, you can pipe the output to tools like [jq ↗︎](https://stedolan.github.io/jq/):
         
         cloudflared tail --output=json <UUID> | jq .




#### Filter logs

You can filter logs by event type (`--event`), event level (`--level`), or sampling rate (`-sampling`) to reduce the volume of logs streamed from the origin. This helps mitigate the performance impact on the origin, especially when the origin is normally under high load. For example:
    
    
    cloudflared tail --level debug <UUID>

Flag | Description | Allowed values | Default value  
---|---|---|---  
`--event` | Filter by the type of event / request. | `cloudflared`, `http`, `tcp`, `udp` | All events  
`--level` | Return logs at this level and above. Works independently of the [`--loglevel`](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/run-parameters/#loglevel) setting on the server. | `debug`, `info`, `warn`, `error`, `fatal` | `debug`  
`--sampling` | Sample a fraction of the total logs. | Number from `0.0` to `1.0` | `1.0`  
  
#### View logs for a replica

If you are running multiple `cloudflared` instances for the same tunnel (also known as [replicas](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/)), you must specify an individual instance to stream logs from:

  1. In the Cloudflare dashboard, go to **Networking** > **Tunnels** and select your tunnel.

[ Go to **Tunnels** ↗ ](https://dash.cloudflare.com/?to=/:account/tunnels)
  2. Find the **Connector ID** for the `cloudflared` instance you want to view.

  3. Specify the Connector ID in `cloudflared tail`:
         
         cloudflared tail --connector-id <CONNECTOR ID> <UUID>




### Performance considerations

  * The logging session will only be held open for one hour. All logging systems introduce some level of performance overhead, and this limit helps prevent long term impact to your tunnel's end-to-end latencies.
  * When streaming logs for a high throughput tunnel, Cloudflare intentionally prioritizes service stability over log delivery. To reduce the number of dropped logs, try requesting fewer logs. To ensure that you are seeing all logs, [view logs on the server](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/#view-logs-on-the-server) instead of streaming the logs remotely.



## Network session logs

[Zero Trust Network Session Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/) record each private network session that Cloudflare routes to a tunnel. Sessions routed to a Cloudflare Tunnel report `Offramp` as `TUNNEL`. Two fields show exactly where a session was sent:

Field | Description  
---|---  
`DestinationTunnelID` | The tunnel that received the session.  
`DestinationReplicaID` | The `cloudflared` replica that received the session. This value matches the replica's **Connector ID** in the dashboard.  
  
If you run multiple [replicas](https://developers.cloudflare.com/tunnel/configuration/#replicas-and-high-availability), use these fields to confirm which tunnel and which replica received traffic for a specific session. To investigate that replica further, stream its logs with `cloudflared tail --connector-id <DESTINATION_REPLICA_ID> <TUNNEL_ID>`.

Network Session Logs are available through [Logpush](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/).

[PreviousOverview](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/)[NextNotifications](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/notifications/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
