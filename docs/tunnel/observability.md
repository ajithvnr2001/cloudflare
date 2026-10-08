---
url: https://developers.cloudflare.com/tunnel/observability/
title: Observability \u00b7 Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:05.238599+00:00
---

# Observability · Cloudflare Docs

> Source: https://developers.cloudflare.com/tunnel/observability/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)
  3. /Observability



# Observability

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/tunnel/observability/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewTunnel health NotificationsLogs Server-side logs Remote log streaming Network session logsMetrics Default metrics server address Configure a custom addressDiagnostic logs Generate diagnostics Diagnostic file contents

Cloudflare Tunnel exposes logs, metrics, and diagnostic tools to help you monitor tunnel health and resolve issues.

## Tunnel health

You can check your tunnel connection status in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/) by going to **Networking** > **Tunnels** , or by running `cloudflared tunnel list`.

[ Go to **Tunnels** ↗ ](https://dash.cloudflare.com/?to=/:account/tunnels)

Status | Meaning | Recommended Action  
---|---|---  
**Healthy** | The tunnel is active and serving traffic through four connections to the Cloudflare global network. | No action is required. Your tunnel is running correctly.  
**Inactive** | The tunnel has been created (via the API or dashboard) but the `cloudflared` connector has never been run to establish a connection. | Install and run `cloudflared` on your origin server to connect the tunnel to Cloudflare. You can find the installation command in the Cloudflare dashboard under **Networking** > **Tunnels** — select your tunnel, then on the **Overview** tab select **Add a replica**. For API-based setup, refer to [Install and run the tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel-api/#4-install-and-run-the-tunnel).  
**Down** | The tunnel was previously connected but is currently disconnected because the `cloudflared` process has stopped. | 1\. Ensure the `cloudflared` [service](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/) or process is actively running on your server.   
2\. Check for server-side issues, such as the machine being powered off, an application crash, or recent network changes.  
**Degraded** | The `cloudflared` connector is running and the tunnel is serving traffic, but at least one individual connection has failed. Further degradation in [tunnel availability](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/) could risk the tunnel going down and failing to serve traffic. | 1\. Review your `cloudflared` [logs](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/) for connection failures or error messages.   
2\. Investigate local network and firewall rules to ensure they are not blocking connections to the [Cloudflare Tunnel IPs and ports](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-with-firewall/).   
  
  
Tunnel status scope

The tunnel status only reflects the connection between `cloudflared` and the Cloudflare network. It does not indicate whether `cloudflared` can reach your internal services. A tunnel can appear **Healthy** while users are unable to connect to an application.

### Notifications

Administrators can receive alerts when tunnels change health or deployment status. Notifications can be delivered by email, webhook, or third-party services.

To configure tunnel notifications, refer to [Create a notification](https://developers.cloudflare.com/notifications/get-started/#create-an-alert).

Tunnel Creation or Deletion Event

**Who is it for?**

Customers who want to receive a notification when Cloudflare Tunnels are created or deleted in their account.

**Other options / filters**

None.

**Included with**

All Cloudflare Zero Trust plans.

**What should you do if you receive one?**

No action is needed.

Tunnel Health Alert

**Who is it for?**

Customers who want to be warned about changes in health status for their Cloudflare Tunnels.

**Other options / filters**

None.

**Included with**

All Cloudflare Zero Trust plans.

**What should you do if you receive one?**

Monitor tunnel health over time and consider deploying [`cloudflared` replicas or load balancers](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/).

**Additional information**

Refer to [Tunnel status](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/common-errors/#tunnel-status) to review the list of possible tunnel statuses (`Healthy`, `Inactive`, `Down` and `Degraded`).

## Logs

Tunnel logs record all activity between `cloudflared` and the Cloudflare global network, and all activity between `cloudflared` and your origin server.

### Server-side logs

If you have access to the origin server, you can use the [`--loglevel` flag](https://developers.cloudflare.com/tunnel/reference/run-parameters/#loglevel) to enable logging when you start the tunnel. By default, `cloudflared` writes logs to standard error (`stderr`) and does not store logs on the server.

Note

Requires `cloudflared` version 2025.6.1 or later.

To format each log line as a JSON object, add `--output json` before `run`:
    
    
    cloudflared tunnel --output json run <UUID>

This format is useful for Kubernetes deployments and log collection systems that consume JSON.

For routine persistent logging, [run the tunnel](https://developers.cloudflare.com/tunnel/reference/run-parameters/#add-run-parameters-to-tunnel-service#log-directory) with `--log-directory <PATH>`. This flag writes logs to `cloudflared.log` in the specified directory, rotates the file when it reaches 1 MB, and keeps up to five backups. It does not remove logs based on age.
    
    
    cloudflared tunnel --loglevel info --log-directory <PATH> run <UUID>

Use the [`--logfile` flag](https://developers.cloudflare.com/tunnel/reference/run-parameters/#logfile) instead for short troubleshooting sessions or when another tool manages rotation. `cloudflared` does not rotate the file specified by `--logfile`. If you set both flags, `--logfile` takes precedence.

### Remote log streaming

You can stream real-time logs from a running tunnel without SSH access to the server.

The `cloudflared` daemon can stream logs from any tunnel in your account to the local command line. `cloudflared` must be installed on both your local machine and the origin server.

  1. On your local machine, authenticate `cloudflared` to your Cloudflare account:
         
         cloudflared tunnel login

  2. Run `cloudflared tail` for a specific tunnel:
         
         cloudflared tail <UUID>

For a more structured view of the JSON message, you can pipe the output to tools like [jq ↗︎](https://stedolan.github.io/jq/):
         
         cloudflared tail --output=json <UUID> | jq .



  3. If you are running multiple [replicas](https://developers.cloudflare.com/tunnel/configuration/#replicas-and-high-availability), you can specify which replica to stream logs from: 
         
         cloudflared tail --connector-id <REPLICA ID> <UUID>

To find the replica ID, go to **Networking** > **Tunnels** and select your tunnel. All active replicas appear in the **Connectors** list on the tunnel overview page. The replica ID is the **Connector ID**.



Log filtering options

You can filter logs by event type (`--event`), event level (`--level`), or sampling rate (`-sampling`) to reduce the volume of logs streamed from the origin. This helps mitigate the performance impact on the origin, especially when the origin is normally under high load. For example:
    
    
    cloudflared tail --level debug <UUID>

Flag | Description | Allowed values | Default value  
---|---|---|---  
`--event` | Filter by the type of event / request. | `cloudflared`, `http`, `tcp`, `udp` | All events  
`--level` | Return logs at this level and above. Works independently of the [`--loglevel`](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/run-parameters/#loglevel) setting on the server. | `debug`, `info`, `warn`, `error`, `fatal` | `debug`  
`--sampling` | Sample a fraction of the total logs. | Number from `0.0` to `1.0` | `1.0`  
  
To stream tunnel logs from the dashboard:

  1. In the Cloudflare dashboard, go to **Networking** > **Tunnels** and select your tunnel.

[ Go to **Tunnels** ↗ ](https://dash.cloudflare.com/?to=/:account/tunnels)
  2. Go to the **Live logs** tab.

  3. Select **Live** to start streaming.




#### View logs for a replica

If you are running multiple `cloudflared` instances for the same tunnel (also known as [replicas](https://developers.cloudflare.com/tunnel/configuration/#replicas-and-high-availability)), logs from all connected replicas are streamed automatically and grouped by hostname, making it easy to identify which host machine produced each log entry.

To filter the stream to specific replicas, select the **Filter** icon and expand the **Replicas** section. You can also filter by **Log Level** and **Event Type**.

### Network session logs

[Zero Trust Network Session Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/) record each private network session that Cloudflare routes to a tunnel. Sessions routed to a Cloudflare Tunnel report `Offramp` as `TUNNEL`. Two fields show exactly where a session was sent:

Field | Description  
---|---  
`DestinationTunnelID` | The tunnel that received the session.  
`DestinationReplicaID` | The `cloudflared` replica that received the session. This value matches the replica's **Connector ID** in the dashboard.  
  
If you run multiple [replicas](https://developers.cloudflare.com/tunnel/configuration/#replicas-and-high-availability), use these fields to confirm which tunnel and which replica received traffic for a specific session. To investigate that replica further, stream its logs with `cloudflared tail --connector-id <DESTINATION_REPLICA_ID> <TUNNEL_ID>`.

Network Session Logs are available through [Logpush](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/).

## Metrics

Tunnel metrics show a Cloudflare Tunnel's throughput and resource usage over time. When you run a tunnel, `cloudflared` will spin up a Prometheus metrics endpoint — an HTTP server that exposes metrics in [Prometheus ↗︎](https://prometheus.io/docs/introduction/overview/) format. You can use the Prometheus toolkit on a remote machine to scrape metrics data from the `cloudflared` server.

### Default metrics server address

In non-containerized environments, `cloudflared` starts the metrics server on `127.0.0.1:<PORT>/metrics`, where `<PORT>` is the first available port in the range `20241` to `20245`. If all ports are unavailable, `cloudflared` binds to a random port. In containerized environments (Docker, Kubernetes), the default address is `0.0.0.0:<PORT>/metrics`.

To determine the default port, check your tunnel logs around the time when the tunnel started. For example:
    
    
    2024-12-19T21:17:58Z INF Starting metrics server on 127.0.0.1:20241/metrics

### Configure a custom address

To serve metrics on a custom IP address and port, perform these steps on the `cloudflared` host:

  1. [Run the tunnel](https://developers.cloudflare.com/tunnel/reference/run-parameters/#add-run-parameters-to-tunnel-service) using the `--metrics` flag. For example,
         
         cloudflared tunnel --metrics 127.0.0.1:60123 run my-tunnel

Note

If you plan to fetch metrics from another machine on the local network, replace `127.0.0.1` with the internal IP of the `cloudflared` server (for example, `198.168.x.x`). To serve metrics on all available network interfaces, use `0.0.0.0`.

  2. Verify that the metrics server is running by going to `http://localhost:60123/metrics`. This will only work if you configured a localhost IP (`127.0.0.1` or `0.0.0.0`).




You can now export the metrics to Prometheus and Grafana to visualize and query the data. Refer to the [Grafana tutorial](https://developers.cloudflare.com/tunnel/tutorials/grafana/) for instructions on getting started with these tools.

cloudflared metrics

Name | Description | Type | Labels  
---|---|---|---  
`build_info` | Build and version information. | GAUGE | `goversion`, `revision`, `type`, `version`  
`cloudflared_config_local_config_pushes` | Number of local configuration pushes to Cloudflare. | COUNTER |   
`cloudflared_config_local_config_pushes_errors` | Number of errors that occurred during local configuration pushes. | COUNTER |   
`cloudflared_orchestration_config_version` | Configuration version. | GAUGE |   
`cloudflared_tcp_active_sessions` | Concurrent number of TCP sessions that are being proxied to any origin. | GAUGE |   
`cloudflared_tcp_total_sessions` | Total number of TCP sessions that have been proxied to any origin. | COUNTER |   
`cloudflared_tunnel_active_streams` | Total number of active streams. | GAUGE |   
`cloudflared_tunnel_concurrent_requests_per_tunnel` | Concurrent number of requests proxied through each tunnel. | GAUGE |   
`cloudflared_tunnel_ha_connections` | Number of active HA connections. | GAUGE |   
`cloudflared_tunnel_request_errors` | Number of errors proxying to origin. | COUNTER |   
`cloudflared_tunnel_server_locations` | Where each tunnel is connected to. `1` means current location, `0` means previous locations. | GAUGE | `connection_id`, `edge_location`  
`cloudflared_tunnel_timer_retries` | Unacknowledged heart beats count. | GAUGE |   
`cloudflared_tunnel_total_requests` | Number of requests proxied through all tunnels. | COUNTER |   
`cloudflared_tunnel_tunnel_authenticate_success` | Number of successful tunnel authentication events. | COUNTER |   
`cloudflared_tunnel_tunnel_register_success` | Number of successful tunnel registrations. | COUNTER | `rpcName`  
`cloudflared_udp_active_sessions` | Concurrent number of UDP sessions that are being proxied to any origin. | GAUGE |   
`cloudflared_udp_total_sessions` | Total number of UDP sessions that have been proxied to any origin. | COUNTER |   
`coredns_panics_total` | Number of panics. | COUNTER |   
`quic_client_closed_connections` | Number of connections that have been closed. | COUNTER |   
`quic_client_latest_rtt` | Latest round-trip time (RTT) measured on a connection. | GAUGE | `conn_index`  
`quic_client_lost_packets` | Number of packets that have been lost from a connection. | COUNTER | `conn_index`, `reason`  
`quic_client_min_rtt` | Lowest RTT measured on a connection in ms. | GAUGE | `conn_index`  
`quic_client_packet_too_big_dropped` | Number of packets received from origin that are too big to send to Cloudflare and are dropped as a result. | COUNTER |   
`quic_client_smoothed_rtt` | Smoothed RTT calculated for a connection in ms. | GAUGE | `conn_index`  
`quic_client_total_connections` | Number of connections initiated. For all QUIC metrics, client means the side initiating the connection. | COUNTER |   
  
Prometheus metrics

Name | Description | Type | Labels  
---|---|---|---  
`promhttp_metric_handler_requests_in_flight` | Current number of scrapes being served. | GAUGE |   
`promhttp_metric_handler_requests_total` | Total number of scrapes by HTTP status code. | COUNTER | `code`  
  
Go runtime metrics

Name | Description | Type | Labels  
---|---|---|---  
`go_gc_duration_seconds` | A summary of the pause duration of garbage collection cycles. | SUMMARY |   
`go_goroutines` | Number of goroutines that currently exist. | GAUGE |   
`go_info` | Information about the Go environment. | GAUGE | `version`  
`go_memstats_alloc_bytes` | Number of bytes allocated and still in use. | GAUGE |   
`go_memstats_alloc_bytes_total` | Total number of bytes allocated, even if freed. | COUNTER |   
`go_memstats_buck_hash_sys_bytes` | Number of bytes used by the profiling bucket hash table. | GAUGE |   
`go_memstats_frees_total` | Total number of frees. | COUNTER |   
`go_memstats_gc_sys_bytes` | Number of bytes used for garbage collection system metadata. | GAUGE |   
`go_memstats_heap_alloc_bytes` | Number of heap bytes allocated and still in use. | GAUGE |   
`go_memstats_heap_idle_bytes` | Number of heap bytes waiting to be used. | GAUGE |   
`go_memstats_heap_inuse_bytes` | Number of heap bytes that are in use. | GAUGE |   
`go_memstats_heap_objects` | Number of allocated objects. | GAUGE |   
`go_memstats_heap_released_bytes` | Number of heap bytes released to OS. | GAUGE |   
`go_memstats_heap_sys_bytes` | Number of heap bytes obtained from system. | GAUGE |   
`go_memstats_last_gc_time_seconds` | Number of seconds since 1970 of last garbage collection. | GAUGE |   
`go_memstats_lookups_total` | Total number of pointer lookups. | COUNTER |   
`go_memstats_mallocs_total` | Total number of mallocs. | COUNTER |   
`go_memstats_mcache_inuse_bytes` | Number of bytes in use by mcache structures. | GAUGE |   
`go_memstats_mcache_sys_bytes` | Number of bytes used for mcache structures obtained from system. | GAUGE |   
`go_memstats_mspan_inuse_bytes` | Number of bytes in use by mspan structures. | GAUGE |   
`go_memstats_mspan_sys_bytes` | Number of bytes used for mspan structures obtained from system. | GAUGE |   
`go_memstats_next_gc_bytes` | Number of heap bytes when next garbage collection will take place. | GAUGE |   
`go_memstats_other_sys_bytes` | Number of bytes used for other system allocations. | GAUGE |   
`go_memstats_stack_inuse_bytes` | Number of bytes in use by the stack allocator. | GAUGE |   
  
## Diagnostic logs

Cloudflare Tunnel generates diagnostic reports that collect data from a single `cloudflared` instance running on the local machine. This requires `cloudflared` version 2024.12.2 or later.

### Generate diagnostics

  1. (Linux only) To include network diagnostics in the logs, allow the `cloudflared` user to create RAW and PACKET sockets without root permissions:
         
         sudo setcap cap_net_raw+ep /usr/bin/traceroute && sudo setcap cap_net_raw+ep /usr/bin/traceroute

If you do not set `cap_net_raw`, then traceroute data will be unavailable.

  2. Get diagnostic logs:
         
         cloudflared tunnel diag

If multiple instances of `cloudflared` are running on the same host, specify the metrics server IP and port for the instance you want to diagnose. For example:
         
         cloudflared tunnel diag --metrics 127.0.0.1:20241




This command will output the status of each diagnostic task and place a `cloudflared-diag-YYYY-MM-DDThh-mm-ss.zip` file in your working directory.

Docker diagnostics

`cloudflared` reads diagnostic data from the tunnel metrics server. To get diagnostic logs, the metrics server must be exposed from the Docker container and reachable from the host machine.

  1. Determine the metrics server port for the `cloudflared` instance running in Docker.

  2. Ensure the container is deployed with port forwarding enabled. The diagnostic feature will request information from the Docker instance using local port `20241`, therefore you should forward port `20241` to the container port obtained in Step 1:
         
         docker run -d -p 20241:<metrics_port> docker.io/cloudflare/cloudflared tunnel ...

  3. Verify that you can reach the metrics server address from the Docker host environment:
         
         curl localhost:20241/diag/tunnel

This command should return a JSON:
         
         {
           "tunnelID": "ef96b330-a7f5-4bce-a00e-827ce5be077f",
           "connectorID": "d236670a-9f74-422f-adf1-030f5c5f0523",
           "connections": [
             { "isConnected": true, "protocol": 1, "edgeAddress": "198.41.192.167"},
             {"isConnected": true, "protocol": 1, "edgeAddress": "198.41.200.113", "index": 1},
             {"isConnected": true, "protocol": 1, "edgeAddress": "198.41.192.47", "index": 2},
             {"isConnected": true, "protocol": 1, "edgeAddress": "198.41.200.73", "index": 3}
           ],
           "icmp_sources": ["192.168.1.243", "fe80::c59:bd4a:e815:ed6"]
         }

  4. Run the diagnostic using the Docker container ID:
         
         cloudflared tunnel diag --diag-container-id=<containerID>

Alternatively, you can specify the container's name instead of its ID:
         
         cloudflared tunnel diag --diag-container-id=<containerName>

Running the diagnostic command with the container ID allows `cloudflared` to collect information from the Docker environment such as logs and container details.




This command will output the status of each diagnostic task and place a `cloudflared-diag-YYYY-MM-DDThh-mm-ss.zip` file in your working directory.

Kubernetes diagnostics

The diagnostic feature will request data from the tunnel metrics server using ports `20241` to `20245`. You will need to use port forwarding to allow the local `cloudflared` instance to connect to the metrics server on one of these ports.

  1. Determine the tunnel's metrics server port.

  2. Enable port forwarding:
         
         kubectl port-forward <pod> <diagnostic_port>:<metrics_port>

     * `<pod>`: Name of the pod where the tunnel is running
     * `<diagnostic_port>` is any local port in the range `20241` to `20245`.
     * `<metrics_port>` is the Kubernetes pod port for the `cloudflared` instance you want to diagnose (obtained in Step 1).

For example, if you set the metrics server address to `0.0.0.0:12345`:
    
    kubectl port-forward cloudflared-6d4897585b-r8kfz 20244:12345

Connections made to local port `20244` are forwarded to port `12345` of the pod that is running the tunnel.

  3. Run the diagnostic:
         
         cloudflared tunnel diag --diag-pod-id=<podID>

If the pod has multiple applications/services running and `cloudflared` is not the first in the pod, you must specify either the container ID or name:
         
         cloudflared tunnel diag --diag-pod-id=<podID> --diag-container-id=<containerName>




This command will output the status of each diagnostic task and place a `cloudflared-diag-YYYY-MM-DDThh-mm-ss.zip` file in your working directory.

### Diagnostic file contents

The `cloudflared-diag-YYYY-MM-DDThh-mm-ss.zip` archive contains the files listed below. The data in a file either applies to the `cloudflared` instance being diagnosed (`diagnosee`) or the instance that triggered the diagnosis (`diagnoser`). For example, if your tunnel is running in a Docker container, the diagnosee is the Docker instance and the diagnoser is the host instance.

File name | Description | Instance  
---|---|---  
`cli-configuration.json` | [Tunnel run parameters](https://developers.cloudflare.com/tunnel/reference/run-parameters/) used when starting the tunnel | diagnosee  
`cloudflared_logs.txt` | Tunnel log file1 | diagnosee  
`configuration.json` | Tunnel configuration parameters | diagnosee  
`goroutine.pprof` | goroutine profile made available by `pprof` | diagnosee  
`heap.pprof` | heap profile made available by `pprof` | diagnosee  
`metrics.txt` | Snapshot of Tunnel metrics at the time of diagnosis | diagnosee  
`network.txt` | JSON traceroutes to Cloudflare's global network using IPv4 and IPv6 | diagnoser  
`raw-network.txt` | Raw traceroutes to Cloudflare's global network using IPv4 and IPv6 | diagnoser  
`systeminformation.json` | Operating system information and resource usage | diagnosee  
`task-result.json` | Result of each diagnostic task | diagnoser  
`tunnelstate.json` | Tunnel connections at the time of diagnosis | diagnosee  
  
## Footnotes

  1. If the log file is blank, you may need to set `--loglevel` to `debug` when you start the tunnel. The `--loglevel` parameter is only required if you ran the tunnel from the CLI using a `cloudflared tunnel run` command. It is not necessary if the tunnel runs as a Linux/macOS service or runs in Docker/Kubernetes. ↩




[PreviousTunnel tokens](https://developers.cloudflare.com/tunnel/reference/tunnel-tokens/)[NextSystem requirements](https://developers.cloudflare.com/tunnel/platform/system-requirements/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/tunnel/observability/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
