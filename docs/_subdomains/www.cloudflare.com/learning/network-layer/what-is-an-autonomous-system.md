---
url: https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/
title: What is an autonomous system? | What are ASNs?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:25:24.540196+00:00
---

# What is an autonomous system? | What are ASNs?

> Source: https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/

[ Learning Center ](https://www.cloudflare.com/learning/) / the network layer

##  What is an autonomous system? | What are ASNs? 

An autonomous system (AS) is a very large network or group of networks with a single routing policy. Each AS is assigned a unique ASN, which is a number that identifies the AS. 

[Learning Center](https://www.cloudflare.com/learning)/the network layer/[What is enterprise networking?](https://www.cloudflare.com/learning/network-layer/enterprise-networking/)[How to migrate from MPLS](https://www.cloudflare.com/learning/network-layer/how-to-migrate-from-mpls/)[How to prepare for network modernization projects](https://www.cloudflare.com/learning/network-layer/how-to-prepare-for-network-modernization-projects/)[What is the Internet Protocol?](https://www.cloudflare.com/learning/network-layer/internet-protocol/)[IPsec VPNs vs. SSL VPNs](https://www.cloudflare.com/learning/network-layer/ipsec-vs-ssl-vpn/)[What is NaaS (network-as-a-service)?](https://www.cloudflare.com/learning/network-layer/network-as-a-service-naas/)[What is network modernization?](https://www.cloudflare.com/learning/network-layer/network-modernization/)[What is network security?](https://www.cloudflare.com/learning/network-layer/network-security/)[SD-WAN vs. MPLS: SD-WAN benefits and drawbacks](https://www.cloudflare.com/learning/network-layer/sd-wan-vs-mpls/)[What is a campus area network (CAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-campus-area-network/)[What is a computer port? | Ports in networking](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/)[What is a metropolitan area network (MAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-metropolitan-area-network/)[What is a network switch? | Switch vs. router](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/)[What is a packet? | Network packet definition](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/)[What is a personal area network (PAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-personal-area-network/)[What is a protocol? | Network protocol definition](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/)[What is a router?](https://www.cloudflare.com/learning/network-layer/what-is-a-router/)[What is a subnet? | How subnetting works](https://www.cloudflare.com/learning/network-layer/what-is-a-subnet/)[What is a WAN? | WAN vs. LAN](https://www.cloudflare.com/learning/network-layer/what-is-a-wan/)[What is an autonomous system? | What are ASNs?](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/)[What is SD-WAN?](https://www.cloudflare.com/learning/network-layer/what-is-an-sd-wan/)[What is branch networking?](https://www.cloudflare.com/learning/network-layer/what-is-branch-networking/)[What is GRE tunneling? | How GRE protocol works](https://www.cloudflare.com/learning/network-layer/what-is-gre-tunneling/)[What is IGMP? | Internet Group Management Protocol](https://www.cloudflare.com/learning/network-layer/what-is-igmp/)[What is IGMP snooping?](https://www.cloudflare.com/learning/network-layer/what-is-igmp-snooping/)[What is IPsec? | How IPsec VPNs work](https://www.cloudflare.com/learning/network-layer/what-is-ipsec/)[What is MPLS (multiprotocol label switching)?](https://www.cloudflare.com/learning/network-layer/what-is-mpls/)[What is MSS (maximum segment size)?](https://www.cloudflare.com/learning/network-layer/what-is-mss/)[What is My Traceroute (MTR)?](https://www.cloudflare.com/learning/network-layer/what-is-mtr/)[What is MTU (maximum transmission unit)?](https://www.cloudflare.com/learning/network-layer/what-is-mtu/)[What is peering?](https://www.cloudflare.com/learning/network-layer/what-is-peering/)[What is software-defined networking (SDN)?](https://www.cloudflare.com/learning/network-layer/what-is-sdn/)[What is the control plane? | Control plane vs. data plane](https://www.cloudflare.com/learning/network-layer/what-is-the-control-plane/)[What is the network layer?](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)[What is tunneling? | Tunneling in networking](https://www.cloudflare.com/learning/network-layer/what-is-tunneling/)[How does the Internet work?](https://www.cloudflare.com/learning/network-layer/how-does-the-internet-work/)[What is routing?](https://www.cloudflare.com/learning/network-layer/what-is-routing/)[What is a LAN?](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define autonomous system (AS) 
  * Learn about AS numbers (ASNs) 
  * Learn about BGP and routing between ASes 



Related content  [ What is the network layer? ](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)[ What is a LAN? ](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/)[ What is the Internet Protocol? ](https://www.cloudflare.com/learning/network-layer/internet-protocol/)[ How does the Internet work? ](https://www.cloudflare.com/learning/network-layer/how-does-the-internet-work/)[ What is routing? ](https://www.cloudflare.com/learning/network-layer/what-is-routing/)

On this page

  * What is an autonomous system?

  * What is an AS routing policy?

  * What is IP address space?

  * What are IP address prefixes?

  * What is an autonomous system number?

  * What is BGP?

  * Why is BGP routing necessary? Isn&#39

  * How do autonomous systems connect with each other?




## What is an autonomous system?

[The Internet](https://www.cloudflare.com/learning/network-layer/how-does-the-internet-work/) is a network of networks*, and autonomous systems are the big networks that make up the Internet. More specifically, an autonomous system (AS) is a large network or group of networks that has a unified [routing](https://www.cloudflare.com/learning/network-layer/what-is-routing/) policy. Every computer or device that connects to the Internet is connected to an AS.

![Autonomous systems around the world with ASNs](https://images.ctfassets.net/slt3lc6tev37/2VQ6NpacA6xXz9B8iAE7re/e06c5e47d5138d05b27c208a59373a30/autonomous-system-diagram.svg)Autonomous systems around the world with ASNs

Imagine an AS as being like a town's post office. Mail goes from post office to post office until it reaches the right town, and that town's post office will then deliver the mail within that town. Similarly, [data packets](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/) cross the Internet by hopping from AS to AS until they reach the AS that contains their destination [Internet Protocol (IP)](https://www.cloudflare.com/learning/ddos/glossary/internet-protocol/) address. [Routers](https://www.cloudflare.com/learning/network-layer/what-is-a-router/) within that AS send the packet to the [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/).

Every AS controls a specific set of IP addresses, just as every town's post office is responsible for delivering mail to all the addresses within that town. The range of IP addresses that a given AS has control over is called their "IP address space."

Most ASes connect to several other ASes. If an AS connects to only one other AS and shares the same routing policy, it may instead be considered a subnetwork of the first AS.

Typically, each AS is operated by a single large organization, such as an Internet service provider (ISP), a large enterprise technology company, a university, or a government agency.

*_A network is a group of two or more connected computers._

Sign up

Free DNS included with any Cloudflare plan

[Start for free →](https://www.cloudflare.com/lp/pg-all-plans-dns/)

## What is an AS routing policy?

An AS routing policy is a list of the IP address space that the AS controls, plus a list of the other ASes to which it connects. This information is necessary for routing packets to the correct networks. ASes announce this information to the Internet using the [Border Gateway Protocol (BGP)](https://www.cloudflare.com/learning/security/glossary/what-is-bgp/).

## What is IP address space?

A specified group or range of IP addresses is called "IP address space." Each AS controls a certain amount of IP address space. (A group of IP addresses can also be called an IP address "block".)

Imagine if all the phone numbers in the world were listed in order, and each telephone company was assigned a range: Phone Co. A controlled numbers 000-0000 through 599-9999, and Phone Co. B controlled numbers 600-0000 through 999-9999. If Alice calls Michelle at 555-2424, her call will be routed to Michelle via Phone Co. A. If she calls Jenny at 867-5309, her call will be routed to Jenny by Phone Co. B.

This is sort of how IP address space works. Suppose Acme Co. operates an AS and controls an IP address range that includes the address 192.0.2.253. If a computer sends a packet to 192.0.2.253, the packet will eventually reach the AS controlled by Acme Co. If that first computer is also sending packets to 198.51.100.255, the packets go to a different AS (although they may pass through Acme Co.'s AS on the way).

Whitepaper

Developing a strategy for your network modernization

[Read the whitepaper →](https://www.cloudflare.com/lp/developing-a-strategy-for-network-modernization/)

## What are IP address prefixes?

When networking engineers communicate which IP addresses are controlled by which ASes, they do so by talking about the IP address "prefixes" owned by each AS. An IP address prefix is a range of IP addresses. Because of the way IP addresses are written, IP address prefixes are expressed in this fashion: 192.0.2.0/24. This represents IP addresses 192.0.2.0 through 192.0.2.255, not 192.0.2.0 through 192.0.2.24.

## What is an autonomous system number (ASN)?

Each AS is assigned an official number, or autonomous system number (ASN), similar to how every business has a business license with an unique, official number. But unlike businesses, external parties often refer to ASes by their number alone.

AS numbers, or ASNs, are unique 16 bit numbers between 1 and 65534 or 32 bit numbers between 131072 and 4294967294. They are presented in this format: AS(number). For instance, Cloudflare's ASN is AS13335. According to some estimates, there are over 90,000 ASNs in use worldwide.

ASNs are only required for external communications with inter-network routers (see "What is BGP?" below). Internal routers and computers within an AS may not need to know that AS's number, since they are only communicating with devices within that AS.

An AS has to meet certain qualifications before the governing bodies that assign ASNs will give it a number. It must have a distinct routing policy, be of a certain size, and have more than one connection to other ASes. There is a limited amount of ASNs available, and if they were given out too freely, the supply would run out and routing would become much more complex.

## What is BGP?

ASes announce their routing policy to other ASes and routers via the Border Gateway Protocol (BGP). BGP is the protocol for routing data packets between ASes. Without this routing information, operating the Internet on a large scale would quickly become impractical: data packets would get lost or take too long to reach their destinations.

Each AS uses BGP to announce which IP addresses they are responsible for and which other ASes they connect to. BGP routers take all this information from ASes around the world and put it into databases called routing tables to determine the fastest paths from AS to AS. When packets arrive, BGP routers refer to their routing tables to determine which AS the packet should go to next.

With so many ASes in the world, BGP routers are constantly updating their routing tables. As networks go offline, new networks come online, and ASes expand or contract their IP address space, all of this information has to be announced via BGP so that BGP routers can adjust their routing tables.

## Why is BGP routing necessary? Isn't IP used for routing?

IP, or the Internet Protocol, is indeed used for routing in that it specifies which destination each packet is going to. BGP is responsible for directing packets on the fastest route to their destination. Without BGP, IP packets would bounce around the Internet randomly from AS to AS, like a driver trying to reach their destination by guessing which roads to take.

## How do autonomous systems connect with each other?

ASes connect with each other and exchange network traffic (data packets) through a process called [peering](https://www.cloudflare.com/learning/network-layer/what-is-peering/). One way ASes peer with each other is by connecting at physical locations called [Internet Exchange Points (IXPs)](https://www.cloudflare.com/learning/cdn/glossary/internet-exchange-point-ixp/). An IXP is a large [local area network (LAN)](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/) with lots of routers, switches, and cable connections.
