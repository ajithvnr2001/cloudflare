---
url: https://developers.cloudflare.com/tunnel/platform/system-requirements/
title: System requirements \u00b7 Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:05.488818+00:00
---

# System requirements · Cloudflare Docs

> Source: https://developers.cloudflare.com/tunnel/platform/system-requirements/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)
  3. /Platform
  4. /System requirements



# System requirements

Last updated Sep 11, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/tunnel/platform/system-requirements/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBaseline recommendationsPort configurationulimits (Linux and macOS)Capacity calculator

`cloudflared` is lightweight enough to run on a Raspberry Pi or a data center server. Tunnel throughput is primarily limited by the number of ports configured in system software, not hardware.

## Baseline recommendations

Run a `cloudflared` [replica](https://developers.cloudflare.com/tunnel/configuration/#replicas-and-high-availability) on two dedicated hosts per location with a minimum of 4 GB RAM and 4 CPU cores. Allocate 50,000 ports per host.

## Port configuration

To increase the number of ports available to `cloudflared` on Linux:

If your machine has a `/etc/sysctl.d/` directory:
    
    
    echo 'net.ipv4.ip_local_port_range = 11000 60999' | sudo tee -a /etc/sysctl.d/99-cloudflared.conf
    sudo sysctl -p /etc/sysctl.d/99-cloudflared.conf

Otherwise:
    
    
    echo 'net.ipv4.ip_local_port_range = 11000 60999' | sudo tee -a /etc/sysctl.conf
    sudo sysctl -p /etc/sysctl.conf

To increase the number of ports available to `cloudflared` on Windows, set the [dynamic port range ↗︎](https://learn.microsoft.com/en-us/troubleshoot/windows-client/networking/tcp-ip-port-exhaustion-troubleshooting) for TCP and UDP:
    
    
    netsh int ipv4 set dynamicport tcp start=11000 num=50000
    netsh int ipv4 set dynamicport udp start=11000 num=50000
    netsh int ipv6 set dynamicport tcp start=11000 num=50000
    netsh int ipv6 set dynamicport udp start=11000 num=50000

## ulimits (Linux and macOS)

On Linux and macOS, `ulimit` settings determine the system resources available to a logged-in user. We recommend configuring the following ulimits on the `cloudflared` server:

ulimit | Description | Value  
---|---|---  
`-n` | Maximum number of open files or file descriptors | ≥ 70,000  
  
To view your current ulimits, open a terminal and run:
    
    
    ulimit -a

To set the open files `ulimit`:
    
    
    ulimit -n 70000

The command above sets the open files limit only for the current terminal session and will not persist after a reboot or new login. To apply this limit permanently, configure it using the persistent method appropriate for your operating system.

## Capacity calculator

To estimate tunnel capacity requirements for your deployment:

  1. Use the [metrics endpoint](https://developers.cloudflare.com/tunnel/observability/#cloudflared-metrics) to measure `cloudflared_tcp_total_sessions` and `cloudflared_udp_total_sessions`.
  2. Compute the average **TCP requests per second** by dividing `cloudflared_tcp_total_sessions` by total time.
  3. Compute the average **Non-DNS UDP requests per second** by dividing `cloudflared_udp_total_sessions` by total time.
  4. Input **TCP requests per second** and **Non-DNS UDP requests per second** into the calculator below. (You can leave **Private DNS requests per second** as `0` unless you are using the tunnel for [private network access](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/system-requirements/).)



### System configuration

Available ports per host  


Number of cloudflared replicas  


DNS UDP session timeout (in seconds)  


Average non-DNS UDP session timeout (seconds)  


### Metrics

TCP requests per second  


Non-DNS UDP requests per second  


Private DNS requests per second  


### Result

Percent capacity per replica  


Percent capacity across all replicas  


Maximum DNS requests per minute across all replicas  


This calculator is for informational purposes only and all results are estimates.

To increase tunnel capacity, add identical hosts running `cloudflared` replicas.

[PreviousObservability](https://developers.cloudflare.com/tunnel/observability/)[NextChangelog](https://developers.cloudflare.com/tunnel/platform/changelog/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/tunnel/platform/system-requirements.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
