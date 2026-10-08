---
url: https://www.cloudflare.com/learning/network-layer/what-is-igmp-snooping/
title: What is IGMP snooping?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:04.186267+00:00
---

# What is IGMP snooping?

> Source: https://www.cloudflare.com/learning/network-layer/what-is-igmp-snooping/

[ Learning Center ](https://www.cloudflare.com/learning/) / the network layer

##  What is IGMP snooping? 

The Internet Group Management Protocol (IGMP) is used to set up multicasting groups. IGMP snooping allows network switches to be aware of these groups and forward network traffic accordingly. 

[Learning Center](https://www.cloudflare.com/learning)/the network layer/[What is enterprise networking?](https://www.cloudflare.com/learning/network-layer/enterprise-networking/)[How to migrate from MPLS](https://www.cloudflare.com/learning/network-layer/how-to-migrate-from-mpls/)[How to prepare for network modernization projects](https://www.cloudflare.com/learning/network-layer/how-to-prepare-for-network-modernization-projects/)[What is the Internet Protocol?](https://www.cloudflare.com/learning/network-layer/internet-protocol/)[IPsec VPNs vs. SSL VPNs](https://www.cloudflare.com/learning/network-layer/ipsec-vs-ssl-vpn/)[What is NaaS (network-as-a-service)?](https://www.cloudflare.com/learning/network-layer/network-as-a-service-naas/)[What is network modernization?](https://www.cloudflare.com/learning/network-layer/network-modernization/)[What is network security?](https://www.cloudflare.com/learning/network-layer/network-security/)[SD-WAN vs. MPLS: SD-WAN benefits and drawbacks](https://www.cloudflare.com/learning/network-layer/sd-wan-vs-mpls/)[What is a campus area network (CAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-campus-area-network/)[What is a computer port? | Ports in networking](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/)[What is a metropolitan area network (MAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-metropolitan-area-network/)[What is a network switch? | Switch vs. router](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/)[What is a packet? | Network packet definition](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/)[What is a personal area network (PAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-personal-area-network/)[What is a protocol? | Network protocol definition](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/)[What is a router?](https://www.cloudflare.com/learning/network-layer/what-is-a-router/)[What is a subnet? | How subnetting works](https://www.cloudflare.com/learning/network-layer/what-is-a-subnet/)[What is a WAN? | WAN vs. LAN](https://www.cloudflare.com/learning/network-layer/what-is-a-wan/)[What is an autonomous system? | What are ASNs?](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/)[What is SD-WAN?](https://www.cloudflare.com/learning/network-layer/what-is-an-sd-wan/)[What is branch networking?](https://www.cloudflare.com/learning/network-layer/what-is-branch-networking/)[What is GRE tunneling? | How GRE protocol works](https://www.cloudflare.com/learning/network-layer/what-is-gre-tunneling/)[What is IGMP? | Internet Group Management Protocol](https://www.cloudflare.com/learning/network-layer/what-is-igmp/)[What is IGMP snooping?](https://www.cloudflare.com/learning/network-layer/what-is-igmp-snooping/)[What is IPsec? | How IPsec VPNs work](https://www.cloudflare.com/learning/network-layer/what-is-ipsec/)[What is MPLS (multiprotocol label switching)?](https://www.cloudflare.com/learning/network-layer/what-is-mpls/)[What is MSS (maximum segment size)?](https://www.cloudflare.com/learning/network-layer/what-is-mss/)[What is My Traceroute (MTR)?](https://www.cloudflare.com/learning/network-layer/what-is-mtr/)[What is MTU (maximum transmission unit)?](https://www.cloudflare.com/learning/network-layer/what-is-mtu/)[What is peering?](https://www.cloudflare.com/learning/network-layer/what-is-peering/)[What is software-defined networking (SDN)?](https://www.cloudflare.com/learning/network-layer/what-is-sdn/)[What is the control plane? | Control plane vs. data plane](https://www.cloudflare.com/learning/network-layer/what-is-the-control-plane/)[What is the network layer?](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)[What is tunneling? | Tunneling in networking](https://www.cloudflare.com/learning/network-layer/what-is-tunneling/)[How does the Internet work?](https://www.cloudflare.com/learning/network-layer/how-does-the-internet-work/)[What is routing?](https://www.cloudflare.com/learning/network-layer/what-is-routing/)[What is a LAN?](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define 'IGMP snooping' 
  * Understand why IGMP snooping is necessary 
  * Learn how IGMP snooping conserves bandwidth 



Related content  [ What is IGMP? | Internet Group Management Protocol ](https://www.cloudflare.com/learning/network-layer/what-is-igmp/)[ What is a protocol? | Network protocol definition ](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/)[ What is the Internet Protocol? ](https://www.cloudflare.com/learning/network-layer/internet-protocol/)[ What is the network layer? ](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)[ What is a LAN? ](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/)

On this page

  * What is IGMP snooping?

  * What is a network switch?

  * What is the network layer? What is the data link layer?

  * What are the benefits of IGMP snooping?

  * Does IGMP snooping work with IPv6 networks?




## What is IGMP snooping?

IGMP snooping is a method that [network switches](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/) use to identify multicast groups, which are groups of computers or devices that all receive the same network traffic. It enables switches to forward [packets](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/) to the correct devices in their network.

The [Internet Group Management Protocol (IGMP)](https://www.cloudflare.com/learning/network-layer/what-is-igmp/) is a [network layer](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/) protocol that allows several devices to share one IP address so they can all receive the same data. Networked devices use IGMP to join and leave multicasting groups, and each multicasting group shares an [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/).

However, most network switches cannot see which devices have joined multicasting groups, since they do not process network layer [protocols](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/). IGMP snooping is a way around this: it allows switches to "snoop" on IGMP messages, even though they technically belong to a different layer of the [OSI model](https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/). IGMP snooping is not a feature of the IGMP protocol, but is rather an adaptation built into some network switches.

## What is a network switch?

A network switch connects devices within a network and forwards data packets to and from those devices (also known as "hosts"). Unlike a router, a switch does not forward packets between networks; it only forwards packets within a network.

## What is the network layer? What is the data link layer?

The processes that make the Internet work are divided into different layers. The OSI model is one standard way to define the different networking layers. The OSI model contains 7 layers. The data link layer and the network layer are layers 2 and 3, respectively.

![undefined](https://www.cloudflare.com/img/learning/ddos/what-is-a-ddos-attack/osi-model-7-layers.svg)undefined

Networking protocols and equipment are partially defined by which layer they belong to. The functions of networking equipment are limited by the layers that the equipment can interact with. A layer 2 switch does not process layer 3 protocols.

IGMP snooping circumvents this limitation. Layer 2 switches observe layer 3 IGMP traffic, and use this visibility to create a table that tracks multicast groups.

## What are the benefits of IGMP snooping?

**Prevents traffic floods:** If a switch is unaware of which devices belong to multicast groups, it will simply forward all multicast traffic it receives. The result is that devices on the network receive far more traffic than they need to. They have to dedicate computing power to processing these unwanted packets, slowing down normal functions or stopping them altogether.

If a network does not enable IGMP snooping, attackers could exploit this fact in a [denial-of-service (DoS) attack](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/). By sending unnecessary multicast traffic that the network switches then forward across the network, an attacker can tie up network bandwidth and processing power. (Learn more about [layer 3 DDoS attacks](https://www.cloudflare.com/learning/ddos/layer-3-ddos-attacks/).)

**Makes networks faster:** The more traffic that travels across a network, the less bandwidth the network has. IGMP snooping conserves bandwidth by cutting down on the amount of traffic that switches forward. This leaves more bandwidth available, making the network faster.

## Does IGMP snooping work with IPv6 networks?

IGMP is the protocol for multicasting for IPv4, the fourth version of the [Internet Protocol](https://www.cloudflare.com/learning/network-layer/internet-protocol/). IPv6 relies on Multicast Listener Discovery (MLD) for multicasting. IPv6 networks use MLD snooping rather than IGMP snooping.
