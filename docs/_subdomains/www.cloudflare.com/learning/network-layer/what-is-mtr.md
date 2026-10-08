---
url: https://www.cloudflare.com/learning/network-layer/what-is-mtr/
title: What is My Traceroute (MTR)?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:07.008156+00:00
---

# What is My Traceroute (MTR)?

> Source: https://www.cloudflare.com/learning/network-layer/what-is-mtr/

[ Learning Center ](https://www.cloudflare.com/learning/) / the network layer

##  What is My Traceroute (MTR)? 

My Traceroute, or MTR, combines traceroute and ping to measure a network path's health. 

[Learning Center](https://www.cloudflare.com/learning)/the network layer/[What is enterprise networking?](https://www.cloudflare.com/learning/network-layer/enterprise-networking/)[How to migrate from MPLS](https://www.cloudflare.com/learning/network-layer/how-to-migrate-from-mpls/)[How to prepare for network modernization projects](https://www.cloudflare.com/learning/network-layer/how-to-prepare-for-network-modernization-projects/)[What is the Internet Protocol?](https://www.cloudflare.com/learning/network-layer/internet-protocol/)[IPsec VPNs vs. SSL VPNs](https://www.cloudflare.com/learning/network-layer/ipsec-vs-ssl-vpn/)[What is NaaS (network-as-a-service)?](https://www.cloudflare.com/learning/network-layer/network-as-a-service-naas/)[What is network modernization?](https://www.cloudflare.com/learning/network-layer/network-modernization/)[What is network security?](https://www.cloudflare.com/learning/network-layer/network-security/)[SD-WAN vs. MPLS: SD-WAN benefits and drawbacks](https://www.cloudflare.com/learning/network-layer/sd-wan-vs-mpls/)[What is a campus area network (CAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-campus-area-network/)[What is a computer port? | Ports in networking](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/)[What is a metropolitan area network (MAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-metropolitan-area-network/)[What is a network switch? | Switch vs. router](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/)[What is a packet? | Network packet definition](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/)[What is a personal area network (PAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-personal-area-network/)[What is a protocol? | Network protocol definition](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/)[What is a router?](https://www.cloudflare.com/learning/network-layer/what-is-a-router/)[What is a subnet? | How subnetting works](https://www.cloudflare.com/learning/network-layer/what-is-a-subnet/)[What is a WAN? | WAN vs. LAN](https://www.cloudflare.com/learning/network-layer/what-is-a-wan/)[What is an autonomous system? | What are ASNs?](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/)[What is SD-WAN?](https://www.cloudflare.com/learning/network-layer/what-is-an-sd-wan/)[What is branch networking?](https://www.cloudflare.com/learning/network-layer/what-is-branch-networking/)[What is GRE tunneling? | How GRE protocol works](https://www.cloudflare.com/learning/network-layer/what-is-gre-tunneling/)[What is IGMP? | Internet Group Management Protocol](https://www.cloudflare.com/learning/network-layer/what-is-igmp/)[What is IGMP snooping?](https://www.cloudflare.com/learning/network-layer/what-is-igmp-snooping/)[What is IPsec? | How IPsec VPNs work](https://www.cloudflare.com/learning/network-layer/what-is-ipsec/)[What is MPLS (multiprotocol label switching)?](https://www.cloudflare.com/learning/network-layer/what-is-mpls/)[What is MSS (maximum segment size)?](https://www.cloudflare.com/learning/network-layer/what-is-mss/)[What is My Traceroute (MTR)?](https://www.cloudflare.com/learning/network-layer/what-is-mtr/)[What is MTU (maximum transmission unit)?](https://www.cloudflare.com/learning/network-layer/what-is-mtu/)[What is peering?](https://www.cloudflare.com/learning/network-layer/what-is-peering/)[What is software-defined networking (SDN)?](https://www.cloudflare.com/learning/network-layer/what-is-sdn/)[What is the control plane? | Control plane vs. data plane](https://www.cloudflare.com/learning/network-layer/what-is-the-control-plane/)[What is the network layer?](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)[What is tunneling? | Tunneling in networking](https://www.cloudflare.com/learning/network-layer/what-is-tunneling/)[How does the Internet work?](https://www.cloudflare.com/learning/network-layer/how-does-the-internet-work/)[What is routing?](https://www.cloudflare.com/learning/network-layer/what-is-routing/)[What is a LAN?](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define “traceroute” and “MTR” 
  * Understand how traceroute and MTR work 
  * Read an MTR result to diagnose problems in a network path 



Related content  [ What is the network layer? ](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)[ What is MTU (maximum transmission unit)? ](https://www.cloudflare.com/learning/network-layer/what-is-mtu/)[ What is the Internet Protocol? ](https://www.cloudflare.com/learning/network-layer/internet-protocol/)[ What is MSS (maximum segment size)? ](https://www.cloudflare.com/learning/network-layer/what-is-mss/)[ What is routing? ](https://www.cloudflare.com/learning/network-layer/what-is-routing/)

On this page

  * What is a traceroute?

  * What is a network path?

  * How does traceroute work?

  * What is My Traceroute?

  * How to read MTR

    * MTR #1: All clean

    * MTR #2: Packet loss - or is there?

    * MTR #3: Actual packet loss

  * Further MTR options




## What is a traceroute?

Traceroute is a tool used to diagnose problems in a network path. Traceroute is used to understand the path [IP packets](https://www.cloudflare.com/learning/network-layer/internet-protocol/) are taking from one computer (source IP address) to another (destination [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/)). The command traceroute (on Linux or macOS) or tracert (on Windows) makes it possible to understand:

  * The path your packets are taking (including the IP addresses of each router)

  * The RTT* between the source and each hop, or router the packets pass through, in the network path




**[Round-trip time (RTT)](https://www.cloudflare.com/learning/cdn/glossary/round-trip-time-rtt/) is the amount of time it takes for data to get to and from a certain point on a network.*

Here is an example traceroute to 1.1.1.1. The lines with asterisks (* * *) represent hops from which packets were not returned; this can happen when routers are configured to ignore traceroute packets. The millisecond times in each line are the roundtrip times from the source to that hop for each packet (traceroute sends three packets at a time to verify the results).

Traceroute example

traceroute to 1.1.1.1 (1.1.1.1), 64 hops max, 52 byte packets

1 myrouter (192.168.47.1) 2.755 ms 1.452 ms 1.325 ms

2 * * *

3 69.168.32.65 (69.168.32.65) 18.159 ms 18.658 ms 15.091 ms

4 * * *

5 206.126.237.30 (206.126.237.30) 30.453 ms 50.242 ms 24.342 ms

6 one.one.one.one (1.1.1.1) 29.000 ms 26.784 ms 26.017 ms

## What is a network path?

A network path refers to the sequence of networks a packet passes through in order to reach its destination.

The Internet is a massive collection of networks that connect to one another via [routing](https://www.cloudflare.com/learning/network-layer/what-is-routing/). Most Internet endpoints — for example, a web browser trying to access a website and the server which hosts that website — are not part of the same network. This means that if said web browser sends a request to the website’s servers, the request will probably have to hop between several intermediary networks along the way.

## How does traceroute work?

A traceroute tool sends packets to a destination IP and with a [time-to-live (TTL)](https://www.cloudflare.com/learning/cdn/glossary/time-to-live-ttl/) set to 1, so that the first router the packets reach will send back an error (“time exceeded”). When the error returns, the traceroute tool records the first router’s identity and round-trip time, increments the TTL, and sends new packets, repeating this process until either 1) the last packet reaches the destination IP or 2) two sets of packets are dropped.

By doing this, the tool enables you to understand the path your packets are taking and the roundtrip time to each hop, so you can troubleshoot packet loss and latency.

Traceroute relies on the [ICMP (Internet Control Message Protocol)](https://www.cloudflare.com/learning/ddos/glossary/internet-control-message-protocol-icmp/) protocol. ICMP is a [network layer](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/) protocol used for error testing. It has no associated transport protocol, running directly on the Internet Protocol (IP). When the TTL of a packet sent by the traceroute tool is exceeded, the router sends back an ICMP Type 11 (Time Exceeded Error) packet.

Outgoing packets (sent from the starting router) can use ICMP (default on MacOS and Linux operating systems) or UDP (default on Windows). Choosing a different protocol for outgoing traceroute packets is one way to get more complete results if routers along the network path are configured to filter out packets of a certain protocol.

## What is My Traceroute (MTR)?

My Traceroute (MTR) is a tool that combines traceroute and ping, which is another common method for testing network connectivity and speed. In addition to the hops along the network path, MTR shows constantly updating information about the latency and packet loss along the route to the destination. This helps in troubleshooting network issues by allowing you to see what’s happening along the path in real-time.

MTR works by discovering the network path in a similar manner to traceroute, and then regularly sending packets to continue collecting information to provide an updated view into the network’s health and speed.

Like traceroute, MTR can use ICMP or UDP for outgoing packets but relies on ICMP for return (Type 11: Time Exceeded) packets.

## How to read MTR

Below are three examples of how to read and draw conclusions from MTR output.

#### MTR #1: All clean

Clean MTR

Start: 2020-04-08T13:28:52+0100

HOST: myrouter Loss% Snt Last Avg Best Wrst StDev

1.|-- 10.10.1.1 0.0% 10 0.3 0.4 0.3 0.4 0.0

2.|-- 141.0.147.177.bcube.co.uk 0.0% 10 2.7 2.7 2.5 3.1 0.2

3.|-- 172.16.28.38 0.0% 10 2.8 6.4 2.8 22.2 6.1

4.|-- 172.17.13.76 0.0% 10 1.1 2.8 1.1 14.6 4.2

5.|-- 172.17.13.49 0.0% 10 1.4 4.0 1.3 25.0 7.4

6.|-- 172.17.13.24 0.0% 10 2.5 2.7 2.0 5.1 1.1

7.|-- one.one.one.one 0.0% 10 1.3 1.2 1.2 1.3 0.0

This example follows the network path between the starting router and Cloudflare’s [1.1.1.1](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1/) [DNS](https://www.cloudflare.com/learning/dns/what-is-dns/) server. The MTR output does not indicate any problems — it takes 7 hops to reach 1.1.1.1, and none of them indicate any packet loss.

#### MTR #2: Packet loss - or is there?

Packet loss on path

Start: 2020-04-08T12:48:28+0000

HOST: myrouter Loss% Snt Last Avg Best Wrst StDev

1.|-- 2400:cb00:207:1000::1 0.0% 10 1.1 6.0 0.6 15.7 5.9

2.|-- 2404:d400:4000:27::1 0.0% 10 0.4 0.6 0.2 2.9 0.8

3.|-- 2404:d400:0:8:: 0.0% 10 125.7 125.7 125.7 126.2 0.2

4.|-- 2001:978:2:42::e:1 50.0% 10 129.2 129.6 129.2 130.5 0.6

5.|-- be2846.ccr42.fra03.atlas.cogentco.com 80.0% 10 151.9 139.5 127.1 151.9 17.6

6.|-- be2814.ccr42.ams03.atlas.cogentco.com 80.0% 10 136.2 137.0 136.2 137.8 1.1

7.|-- be2183.ccr22.lpl01.atlas.cogentco.com 50.0% 10 146.3 146.2 145.9 146.3 0.1

8.|-- be3043.ccr22.ymq01.atlas.cogentco.com 30.0% 10 215.3 215.2 215.0 215.4 0.2

9.|-- be3260.ccr32.yyz02.atlas.cogentco.com 90.0% 10 227.8 227.8 227.8 227.8 0.0

10.|-- be2994.ccr22.cle04.atlas.cogentco.com 30.0% 10 234.9 234.9 234.5 235.1 0.2

11.|-- be2718.ccr42.ord01.atlas.cogentco.com 70.0% 10 233.7 233.8 233.7 233.9 0.1

12.|-- be2832.ccr22.mci01.atlas.cogentco.com 50.0% 10 244.8 245.1 244.8 245.5 0.3

13.|-- be3036.ccr22.den01.atlas.cogentco.com 30.0% 10 259.6 259.6 259.3 259.8 0.2

14.|-- be3038.ccr32.slc01.atlas.cogentco.com 90.0% 10 267.2 267.2 267.2 267.2 0.0

15.|-- be3110.ccr22.sfo01.atlas.cogentco.com 10.0% 10 291.0 291.1 291.0 291.4 0.1

16.|-- be3670.ccr41.sjc03.atlas.cogentco.com 30.0% 10 292.6 292.7 292.6 292.8 0.1

17.|-- 2001:550:2:1f::29:2 0.0% 10 312.3 291.5 287.0 312.3 8.6

8.6 0.0% 10 298.7 299.5 298.7 306.1 2.3

19.|-- ??? 100.0 10 0.0 0.0 0.0 0.0 0.0

20.|-- ??? 100.0 9 0.0 0.0 0.0 0.0 0.0

21.|-- 2400:cb00:36:1008::a29e:40e2 0.0% 9 302.9 302.9 302.8 303.2 0.1

This example shows the network path between the starting router and 2400:cb00:36:1008::a29e:40e2, which is an [IPv6](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/) address. The output shows significant packet loss on all the Cogent hops. However, there is no packet loss on the last hop (21). This indicates that the network path is actually not problematic. What's happening is something often referred to as "Control Plane Policing.”

As discussed earlier, MTR works by sending out (as a default) ICMP Echo packets, with an incrementing TTL (Time-To-Live) per packet. When the TTL expires, a router will send back an ICMP Type 11 (Time Exceeded), indicating how many hops there are from point A to point B.

Many network operators (including Cloudflare) set arbitrary limits on the amount of ICMP packets that are allowed to reach the control plane of a router. (The control plane is the router's brain.) A packet that exceeds a router's TTL has to be processed by the control plane. To prevent the control plane from being overwhelmed by too many of these packets, a rate limit (or policer) is put in place, which is why we see all that loss on the intermediary hops, but not the final hop: the control plane rate limits for the routers on the intermediary hops were exceeded, so Type 11 packets were not sent back for the traceroute packets past those limits, but the packets were able to get through to the destination safely.

#### MTR #3: Actual packet loss

Packet loss on return path

Start: 2020-04-08T13:32:30+0000

HOST: myrouter Loss% Snt Last Avg Best Wrst StDev

1.|-- 162.158.216.129 0.0% 10 0.7 6.9 0.7 62.6 19.6

2.|-- 118.69.221.209 0.0% 10 0.2 0.3 0.2 1.3 0.3

3.|-- 118.69.252.172 0.0% 10 0.7 1.0 0.6 2.9 0.7

4.|-- 118.69.132.169 0.0% 10 11.4 11.3 11.2 11.5 0.1

5.|-- 118.69.247.64 0.0% 10 34.2 34.4 33.9 37.2 1.0

6.|-- 13335.sgw.equinix.com 50.0% 10 27.5 27.9 27.1 29.1 0.8

7.|-- 162.158.161.251 30.0% 10 26.8 26.8 26.8 26.8 0.0

This example shows the network path between the starting router and 162.158.161.251. The output shows packet loss on the last 2 hops.

## Further MTR options

MTR has a lot of options. You can find more through the MTR help page: _mtr --help_

Some of the frequently used options are:

  * TCP MTR: Instead of using ICMP packets, use [TCP](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/). You can optionally choose a destination port as well.

  * UDP MTR: Use [UDP](https://www.cloudflare.com/learning/ddos/glossary/user-datagram-protocol-udp/) instead of ICMP. This can be used to circumvent routers that are blocking ICMP packets, or for the purpose of testing a specific port.

  * Show IPs: Shows IP addresses next to the records for each hop. This makes it easier to report issues upstream.

  * AS Lookup: Shows the [AS number](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/) in the MTR.



