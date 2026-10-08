---
url: https://www.cloudflare.com/learning/network-layer/what-is-mss/
title: What is MSS (maximum segment size)?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:06.874441+00:00
---

# What is MSS (maximum segment size)?

> Source: https://www.cloudflare.com/learning/network-layer/what-is-mss/

[ Learning Center ](https://www.cloudflare.com/learning/) / the network layer

##  What is MSS (maximum segment size)? 

MSS, or maximum segment size, is the largest data payload that a device will accept from a network connection. 

[Learning Center](https://www.cloudflare.com/learning)/the network layer/[What is enterprise networking?](https://www.cloudflare.com/learning/network-layer/enterprise-networking/)[How to migrate from MPLS](https://www.cloudflare.com/learning/network-layer/how-to-migrate-from-mpls/)[How to prepare for network modernization projects](https://www.cloudflare.com/learning/network-layer/how-to-prepare-for-network-modernization-projects/)[What is the Internet Protocol?](https://www.cloudflare.com/learning/network-layer/internet-protocol/)[IPsec VPNs vs. SSL VPNs](https://www.cloudflare.com/learning/network-layer/ipsec-vs-ssl-vpn/)[What is NaaS (network-as-a-service)?](https://www.cloudflare.com/learning/network-layer/network-as-a-service-naas/)[What is network modernization?](https://www.cloudflare.com/learning/network-layer/network-modernization/)[What is network security?](https://www.cloudflare.com/learning/network-layer/network-security/)[SD-WAN vs. MPLS: SD-WAN benefits and drawbacks](https://www.cloudflare.com/learning/network-layer/sd-wan-vs-mpls/)[What is a campus area network (CAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-campus-area-network/)[What is a computer port? | Ports in networking](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/)[What is a metropolitan area network (MAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-metropolitan-area-network/)[What is a network switch? | Switch vs. router](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/)[What is a packet? | Network packet definition](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/)[What is a personal area network (PAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-personal-area-network/)[What is a protocol? | Network protocol definition](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/)[What is a router?](https://www.cloudflare.com/learning/network-layer/what-is-a-router/)[What is a subnet? | How subnetting works](https://www.cloudflare.com/learning/network-layer/what-is-a-subnet/)[What is a WAN? | WAN vs. LAN](https://www.cloudflare.com/learning/network-layer/what-is-a-wan/)[What is an autonomous system? | What are ASNs?](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/)[What is SD-WAN?](https://www.cloudflare.com/learning/network-layer/what-is-an-sd-wan/)[What is branch networking?](https://www.cloudflare.com/learning/network-layer/what-is-branch-networking/)[What is GRE tunneling? | How GRE protocol works](https://www.cloudflare.com/learning/network-layer/what-is-gre-tunneling/)[What is IGMP? | Internet Group Management Protocol](https://www.cloudflare.com/learning/network-layer/what-is-igmp/)[What is IGMP snooping?](https://www.cloudflare.com/learning/network-layer/what-is-igmp-snooping/)[What is IPsec? | How IPsec VPNs work](https://www.cloudflare.com/learning/network-layer/what-is-ipsec/)[What is MPLS (multiprotocol label switching)?](https://www.cloudflare.com/learning/network-layer/what-is-mpls/)[What is MSS (maximum segment size)?](https://www.cloudflare.com/learning/network-layer/what-is-mss/)[What is My Traceroute (MTR)?](https://www.cloudflare.com/learning/network-layer/what-is-mtr/)[What is MTU (maximum transmission unit)?](https://www.cloudflare.com/learning/network-layer/what-is-mtu/)[What is peering?](https://www.cloudflare.com/learning/network-layer/what-is-peering/)[What is software-defined networking (SDN)?](https://www.cloudflare.com/learning/network-layer/what-is-sdn/)[What is the control plane? | Control plane vs. data plane](https://www.cloudflare.com/learning/network-layer/what-is-the-control-plane/)[What is the network layer?](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)[What is tunneling? | Tunneling in networking](https://www.cloudflare.com/learning/network-layer/what-is-tunneling/)[How does the Internet work?](https://www.cloudflare.com/learning/network-layer/how-does-the-internet-work/)[What is routing?](https://www.cloudflare.com/learning/network-layer/what-is-routing/)[What is a LAN?](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand what a packet is and what packet headers are 
  * Define 'payload' 
  * Learn how to calculate MSS based on MTU 



Related content  [ What is the network layer? ](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)[ What is a network switch? | Switch vs. router ](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/)[ What is a LAN? ](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/)[ What is the Internet Protocol? ](https://www.cloudflare.com/learning/network-layer/internet-protocol/)[ What is routing? ](https://www.cloudflare.com/learning/network-layer/what-is-routing/)

On this page

  * What is maximum segment size?

  * What is TCP? What is a TCP header?

  * How long are TCP and IP headers?

  * TCP MSS example

  * How does the use of IPsec impact MSS?

  * Is MSS a network layer or transport layer metric?

  * What is MSS clamping?




## What is maximum segment size (MSS)?

MSS (maximum segment size) limits the size of packets, or small chunks of data, that travel across a network, such as the Internet. All data that travels over a network is broken up into packets. Packets have several headers attached to them that contain information about their contents and destination. MSS measures the non-header portion of a packet, which is called the payload.

If a data packet is compared to a transport truck, with the header being the truck itself and the payload being the trailer and cargo, then MSS is like a scale that measures only the trailer. If the trailer weighs too much, then the truck is not allowed to continue to its destination.

More specifically, MSS is the largest [TCP (Transport Control Protocol)](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/) segment size that a network-connected device can receive. MSS defines "segment" as only the length of the payload, not any attached headers. MSS is measured in bytes.

![Data packet headers and payload - TCP segment and MSS](https://images.ctfassets.net/slt3lc6tev37/29tC841gKxTb6c2fUFJro6/9c49654618fe84f3c00700629f30a6e4/MSS_TCP_segment_packet_diagram.png)Data packet headers and payload - TCP segment and MSS

MSS is determined by another metric that has to do with packet size: [MTU](https://www.cloudflare.com/learning/network-layer/what-is-mtu/), or the maximum transmission unit, which does include the TCP and [IP (Internet Protocol)](https://www.cloudflare.com/learning/ddos/glossary/internet-protocol/) headers. To continue the analogy, MTU measures the total weight of the truck and its trailer and cargo, instead of just the trailer and cargo.

Essentially, the MSS is equal to MTU minus the size of a TCP header and an IP header:

_MTU - (TCP header + IP header) = MSS_

One of the key differences between MTU and MSS is that if a packet exceeds a device's MTU, it is broken up into smaller pieces, or "fragmented." In contrast, if a packet exceeds the MSS, it is dropped and not delivered.

## What is TCP? What is a TCP header?

The Transport Control Protocol, or TCP, is a protocol that ensures data packets are delivered and received in order, with no dropped packets. Imagine if parcel delivery services called all package recipients ahead of time to make sure they would be home at a certain time before delivering packages, then sent word back to the sender to confirm they had been delivered. TCP works somewhat like that, with data packets as the "packages" being delivered.

TCP works by opening a connection between the two devices that are communicating via a process called a TCP handshake. The MSS is agreed on during the TCP handshake: both devices communicate the size of the packets they are able to receive (this can be called "MSS clamping"; see below). TCP adds a header to all packets to indicate which open connection each packet is a part of and what order the packets go in.

## How long are TCP and IP headers?

TCP headers are almost always 20 bytes* long. IP headers include information such as the source and destination [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/), and they are also 20 bytes long. Both TCP and IP packets include optional header fields that can make the headers longer, but these are almost never used.

*_In computer science, a byte is a unit of memory size that represents eight binary digits; in other words, a combination of eight ones and zeroes._

## TCP MSS example

Suppose a network [router](https://www.cloudflare.com/learning/network-layer/what-is-a-router/) has an MTU of 1,500, meaning it only accepts packets up to 1,500 bytes long. (Longer packets will be fragmented.) What should the MSS for the router be set to?

_MTU - (TCP header + IP header) = MSS_

_1,500 - (20 + 20) = 1,460_

The router’s MSS should be set to 1,460 bytes. Packets with a payload size larger than 1,460 bytes will be dropped. (A device could send an overly large packet like this by mistake if it is not aware of the MTU and MSS settings of the routers in between it and another device. A process called path MTU discovery helps avoid such incidents.)

## How does the use of IPsec impact MSS?

IPsec (Internet Protocol security) is the [encrypted](https://www.cloudflare.com/learning/ssl/what-is-encryption/) version of IP. Data packets sent using IPsec are scrambled so that only the two connected devices are able to interpret them, keeping their payload contents secure from anyone who might intercept the packets. IPsec is often used to set up [Virtual Private Networks, or VPNs](https://www.cloudflare.com/learning/access-management/what-is-a-vpn/).

IPsec adds a few bytes to the length of a packet. On connections that use this encryption, MSS must take IPsec into account as well:

_MTU - (TCP header + IP header + IPsec) = MSS_

## Is MSS a network layer or transport layer metric?

MSS is a layer 4, or transport layer, metric. It is used with TCP, a transport layer protocol. However, it is closely related to MTU, which applies to [layer 3](https://www.cloudflare.com/learning/ddos/layer-3-ddos-attacks/) (the [network layer](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)).

## What is MSS clamping?

Occasionally, a router along a network path has an MTU value set lower than the typical 1,500 bytes. This can result in packet loss and can be difficult to discover.

To ensure packets still reach their destination in this situation, one option is to reduce the size of incoming packet payloads. This can be achieved by configuring the server to apply an MSS clamp: during the TCP handshake, the server can signal the MSS for packets it is willing to receive, "clamping" the maximum payload size from the other server. For example, if servers A and B are establishing a TCP connection and server B communicates an MSS of 1,436 bytes, server A will send packets with a maximum payload size of 1,436 bytes for the duration of the connection.

Another application of MSS clamping is in the case of [GRE tunneling](https://www.cloudflare.com/learning/network-layer/what-is-gre-tunneling/), where a 24-byte header is added to the original packet in order to send it to a new destination. If the original packet was larger than 1,476 bytes, this could make the new packet exceed the typical 1,500-byte MTU; an MSS clamp can be applied to require incoming packets to be less than 1,500 bytes even after the GRE header is applied.

To learn more about MTU and MSS, see [What is MTU?](https://www.cloudflare.com/learning/network-layer/what-is-mtu/)
