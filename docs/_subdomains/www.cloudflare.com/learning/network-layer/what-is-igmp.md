---
url: https://www.cloudflare.com/learning/network-layer/what-is-igmp/
title: What is IGMP? | Internet Group Management Protocol
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:03.967508+00:00
---

# What is IGMP? | Internet Group Management Protocol

> Source: https://www.cloudflare.com/learning/network-layer/what-is-igmp/

[ Learning Center ](https://www.cloudflare.com/learning/) / the network layer

##  What is IGMP? | Internet Group Management Protocol 

The Internet Group Management Protocol (IGMP) enables a group of networked devices to share the same IP address and receive the same messages. 

[Learning Center](https://www.cloudflare.com/learning)/the network layer/[What is enterprise networking?](https://www.cloudflare.com/learning/network-layer/enterprise-networking/)[How to migrate from MPLS](https://www.cloudflare.com/learning/network-layer/how-to-migrate-from-mpls/)[How to prepare for network modernization projects](https://www.cloudflare.com/learning/network-layer/how-to-prepare-for-network-modernization-projects/)[What is the Internet Protocol?](https://www.cloudflare.com/learning/network-layer/internet-protocol/)[IPsec VPNs vs. SSL VPNs](https://www.cloudflare.com/learning/network-layer/ipsec-vs-ssl-vpn/)[What is NaaS (network-as-a-service)?](https://www.cloudflare.com/learning/network-layer/network-as-a-service-naas/)[What is network modernization?](https://www.cloudflare.com/learning/network-layer/network-modernization/)[What is network security?](https://www.cloudflare.com/learning/network-layer/network-security/)[SD-WAN vs. MPLS: SD-WAN benefits and drawbacks](https://www.cloudflare.com/learning/network-layer/sd-wan-vs-mpls/)[What is a campus area network (CAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-campus-area-network/)[What is a computer port? | Ports in networking](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/)[What is a metropolitan area network (MAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-metropolitan-area-network/)[What is a network switch? | Switch vs. router](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/)[What is a packet? | Network packet definition](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/)[What is a personal area network (PAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-personal-area-network/)[What is a protocol? | Network protocol definition](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/)[What is a router?](https://www.cloudflare.com/learning/network-layer/what-is-a-router/)[What is a subnet? | How subnetting works](https://www.cloudflare.com/learning/network-layer/what-is-a-subnet/)[What is a WAN? | WAN vs. LAN](https://www.cloudflare.com/learning/network-layer/what-is-a-wan/)[What is an autonomous system? | What are ASNs?](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/)[What is SD-WAN?](https://www.cloudflare.com/learning/network-layer/what-is-an-sd-wan/)[What is branch networking?](https://www.cloudflare.com/learning/network-layer/what-is-branch-networking/)[What is GRE tunneling? | How GRE protocol works](https://www.cloudflare.com/learning/network-layer/what-is-gre-tunneling/)[What is IGMP? | Internet Group Management Protocol](https://www.cloudflare.com/learning/network-layer/what-is-igmp/)[What is IGMP snooping?](https://www.cloudflare.com/learning/network-layer/what-is-igmp-snooping/)[What is IPsec? | How IPsec VPNs work](https://www.cloudflare.com/learning/network-layer/what-is-ipsec/)[What is MPLS (multiprotocol label switching)?](https://www.cloudflare.com/learning/network-layer/what-is-mpls/)[What is MSS (maximum segment size)?](https://www.cloudflare.com/learning/network-layer/what-is-mss/)[What is My Traceroute (MTR)?](https://www.cloudflare.com/learning/network-layer/what-is-mtr/)[What is MTU (maximum transmission unit)?](https://www.cloudflare.com/learning/network-layer/what-is-mtu/)[What is peering?](https://www.cloudflare.com/learning/network-layer/what-is-peering/)[What is software-defined networking (SDN)?](https://www.cloudflare.com/learning/network-layer/what-is-sdn/)[What is the control plane? | Control plane vs. data plane](https://www.cloudflare.com/learning/network-layer/what-is-the-control-plane/)[What is the network layer?](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)[What is tunneling? | Tunneling in networking](https://www.cloudflare.com/learning/network-layer/what-is-tunneling/)[How does the Internet work?](https://www.cloudflare.com/learning/network-layer/how-does-the-internet-work/)[What is routing?](https://www.cloudflare.com/learning/network-layer/what-is-routing/)[What is a LAN?](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define multicasting 
  * Learn how IGMP enables multicasting 
  * Explore how IGMP works 



Related content  [ What is the network layer? ](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)[ What is a protocol? | Network protocol definition ](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/)[ What is the Internet Protocol? ](https://www.cloudflare.com/learning/network-layer/internet-protocol/)[ How does the Internet work? ](https://www.cloudflare.com/learning/network-layer/how-does-the-internet-work/)[ What is a network switch? | Switch vs. router ](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/)

On this page

  * What is the Internet Group Management Protocol?

  * What is multicasting?

  * How does IGMP work?

  * What types of IGMP messages are there?

  * What is IGMP snooping?

  * How is multicasting different in IPv4 and IPv6?

  * How is multicasting different from anycast and unicast?

    * Multicast vs. anycast

    * Multicast vs. unicast




## What is the Internet Group Management Protocol (IGMP)?

The Internet Group Management Protocol (IGMP) is a protocol that allows several devices to share one IP address so they can all receive the same data. IGMP is a network layer [protocol](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/) used to set up multicasting on networks that use the [Internet Protocol](https://www.cloudflare.com/learning/network-layer/internet-protocol/) version 4 (IPv4). Specifically, IGMP allows devices to join a multicasting group.

## What is multicasting?

Multicasting is when a group of devices all receive the same messages or [packets](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/). Multicasting works by sharing an IP address between multiple devices. Any network traffic directed at that [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/) will reach all devices that share the IP address, instead of just one device. This is much like when a group of employees all receive company emails directed at a certain email alias.

## How does IGMP work?

Computers and other devices connected to a network use IGMP when they want to join a multicast group. A router that supports IGMP listens to IGMP transmissions from devices in order to figure out which devices belong to which multicast groups.

IGMP uses IP addresses that are set aside for multicasting. Multicast IP addresses are in the range between 224.0.0.0 and 239.255.255.255. (In contrast, anycast networks can use any regular IP address.) Each multicast group shares one of these IP addresses. When a router receives a series of packets directed at the shared IP address, it will duplicate those packets, sending copies to all members of the multicast group.

IGMP multicast groups can change at any time. A device can send an IGMP "join group" or "leave group" message at any point.

IGMP works directly on top of the Internet Protocol (IP). Each IGMP packet has both an IGMP header and an IP header. Just like [ICMP](https://www.cloudflare.com/learning/ddos/glossary/internet-control-message-protocol-icmp/), IGMP does not use a transport layer protocol such as [TCP](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/) or [UDP](https://www.cloudflare.com/learning/ddos/glossary/user-datagram-protocol-udp/).

## What types of IGMP messages are there?

The IGMP protocol allows for several kinds of IGMP messages:

  * Membership reports: Devices send these to a multicast router in order to become a member of a multicast group.

  * "Leave group" messages: These messages go from a device to a router and allow devices to leave a multicast group.

  * General membership queries: A multicast-capable router sends out these messages to the entire connected network of devices to update multicast group membership for all groups on the network.

  * Group-specific membership queries: Routers send these messages to a specific multicast group, instead of the entire network.




## What is IGMP snooping?

IGMP is a [network layer](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/) protocol, and only networking devices that are aware of the network layer can send and receive messages. A router operates at the network layer, while a [network switch](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/) may only be aware of layer 2, also known as the data link layer. As a result, a switch may be unaware of which network devices are part of multicast groups, and which are not. It may end up forwarding multicast traffic to devices that do not need it, which takes up network bandwidth and device processing power, slowing the entire network down.

IGMP snooping solves for this issue by enabling switches to "snoop" on IGMP messages. Ordinarily, a layer 2 switch would not be aware of IGMP messages, but they can listen in to these via IGMP snooping. This enables them to identify where multicast messages should be forwarded, so that only the correct devices receive multicast traffic.

## How is multicasting different in IPv4 and IPv6?

IPv4 and IPv6 are two different versions of the Internet Protocol (IP). IPv6 is more modern, but IPv4 is still in wide use. In IPv6, Multicast Listener Discovery (MLD) is the protocol for multicasting, not IGMP.

## How is multicasting different from anycast and unicast?

#### Multicast vs. anycast

[Anycast](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/) is another technology that enables network communications to go to multiple places. Similar to multicast, an anycast network allows the same group of servers to share one or more IP addresses. However, instead of all servers receiving all traffic to those IP addresses, the network routes traffic to one of those servers based on a predetermined set of criteria. Anycast networks can also support a wider range of IP addresses than multicast groups. As an example, the [Cloudflare network](https://www.cloudflare.com/network/) uses anycast to route all user traffic to the closest data center.

#### Multicast vs. unicast

"Unicast" describes how most of the Internet works. In unicast networks, every connected device on the network has a unique address. Messages directed at that address (on the Internet, an IP address) only go to that device — rather than to multiple devices, as in multicasting.
