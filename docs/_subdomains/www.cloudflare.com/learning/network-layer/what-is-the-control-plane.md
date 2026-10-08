---
url: https://www.cloudflare.com/learning/network-layer/what-is-the-control-plane/
title: What is the control plane? | Control plane vs. data plane
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:15.203568+00:00
---

# What is the control plane? | Control plane vs. data plane

> Source: https://www.cloudflare.com/learning/network-layer/what-is-the-control-plane/

[ Learning Center ](https://www.cloudflare.com/learning/) / the network layer

##  What is the control plane? | Control plane vs. data plane 

The control plane is the part of a network that controls how data is forwarded, while the data plane is the actual forwarding process. 

[Learning Center](https://www.cloudflare.com/learning)/the network layer/[What is enterprise networking?](https://www.cloudflare.com/learning/network-layer/enterprise-networking/)[How to migrate from MPLS](https://www.cloudflare.com/learning/network-layer/how-to-migrate-from-mpls/)[How to prepare for network modernization projects](https://www.cloudflare.com/learning/network-layer/how-to-prepare-for-network-modernization-projects/)[What is the Internet Protocol?](https://www.cloudflare.com/learning/network-layer/internet-protocol/)[IPsec VPNs vs. SSL VPNs](https://www.cloudflare.com/learning/network-layer/ipsec-vs-ssl-vpn/)[What is NaaS (network-as-a-service)?](https://www.cloudflare.com/learning/network-layer/network-as-a-service-naas/)[What is network modernization?](https://www.cloudflare.com/learning/network-layer/network-modernization/)[What is network security?](https://www.cloudflare.com/learning/network-layer/network-security/)[SD-WAN vs. MPLS: SD-WAN benefits and drawbacks](https://www.cloudflare.com/learning/network-layer/sd-wan-vs-mpls/)[What is a campus area network (CAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-campus-area-network/)[What is a computer port? | Ports in networking](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/)[What is a metropolitan area network (MAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-metropolitan-area-network/)[What is a network switch? | Switch vs. router](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/)[What is a packet? | Network packet definition](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/)[What is a personal area network (PAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-personal-area-network/)[What is a protocol? | Network protocol definition](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/)[What is a router?](https://www.cloudflare.com/learning/network-layer/what-is-a-router/)[What is a subnet? | How subnetting works](https://www.cloudflare.com/learning/network-layer/what-is-a-subnet/)[What is a WAN? | WAN vs. LAN](https://www.cloudflare.com/learning/network-layer/what-is-a-wan/)[What is an autonomous system? | What are ASNs?](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/)[What is SD-WAN?](https://www.cloudflare.com/learning/network-layer/what-is-an-sd-wan/)[What is branch networking?](https://www.cloudflare.com/learning/network-layer/what-is-branch-networking/)[What is GRE tunneling? | How GRE protocol works](https://www.cloudflare.com/learning/network-layer/what-is-gre-tunneling/)[What is IGMP? | Internet Group Management Protocol](https://www.cloudflare.com/learning/network-layer/what-is-igmp/)[What is IGMP snooping?](https://www.cloudflare.com/learning/network-layer/what-is-igmp-snooping/)[What is IPsec? | How IPsec VPNs work](https://www.cloudflare.com/learning/network-layer/what-is-ipsec/)[What is MPLS (multiprotocol label switching)?](https://www.cloudflare.com/learning/network-layer/what-is-mpls/)[What is MSS (maximum segment size)?](https://www.cloudflare.com/learning/network-layer/what-is-mss/)[What is My Traceroute (MTR)?](https://www.cloudflare.com/learning/network-layer/what-is-mtr/)[What is MTU (maximum transmission unit)?](https://www.cloudflare.com/learning/network-layer/what-is-mtu/)[What is peering?](https://www.cloudflare.com/learning/network-layer/what-is-peering/)[What is software-defined networking (SDN)?](https://www.cloudflare.com/learning/network-layer/what-is-sdn/)[What is the control plane? | Control plane vs. data plane](https://www.cloudflare.com/learning/network-layer/what-is-the-control-plane/)[What is the network layer?](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)[What is tunneling? | Tunneling in networking](https://www.cloudflare.com/learning/network-layer/what-is-tunneling/)[How does the Internet work?](https://www.cloudflare.com/learning/network-layer/how-does-the-internet-work/)[What is routing?](https://www.cloudflare.com/learning/network-layer/what-is-routing/)[What is a LAN?](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define 'control plane' 
  * Contrast the control plane with the data plane 
  * Learn how the control plane relates to software-defined networking (SDN) 



On this page

  * What is a &#39

  * What is the control plane?

  * What is the data plane? What is the forwarding plane?

  * What protocols do routers use to create their routing tables?

  * What is network topology?

  * What is software-defined networking?




## What is a 'plane' in networking?

In networking, a _plane_ is an abstract conception of where certain processes take place. The term is used in the sense of "plane of existence." The two most commonly referenced planes in networking are the control plane and the data plane (also known as the forwarding plane).

## What is the control plane?

The control plane is the part of a network that controls how data [packets](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/) are forwarded — meaning how data is sent from one place to another. The process of creating a [routing](https://www.cloudflare.com/learning/network-layer/what-is-routing/) table, for example, is considered part of the control plane. Routers use various [protocols](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/) to identify network paths, and they store these paths in routing tables.

## What is the data plane? What is the forwarding plane?

In contrast to the control plane, which determines how packets should be forwarded, the data plane actually forwards the packets. The data plane is also called the forwarding plane.

Think of the control plane as being like the stoplights that operate at the intersections of a city. Meanwhile, the data plane (or the forwarding plane) is more like the cars that drive on the roads, stop at the intersections, and obey the stoplights.

## What protocols do routers use to create their routing tables?

  * [Border Gateway Protocol (BGP)](https://www.cloudflare.com/learning/security/glossary/what-is-bgp/)

  * Open Shortest Path First (OSPF)

  * Enhanced Interior Gateway Routing Protocol (EIGRP)

  * Intermediate System to Intermediate System (IS-IS)




## What is network topology?

Network topology refers to the way data flows in a network. The control plane establishes and changes network topology. Again, think of the stoplights that function at the intersections of a city. Network topology is like the way that the roads are arranged, and the computing devices within the network are like the destinations that those roads lead to.

## What is software-defined networking?

[Software-defined networking (SDN)](https://www.cloudflare.com/learning/network-layer/what-is-sdn/) is a method for managing and configuring networks using software. SDN technology enables IT administrators to configure their networks using a software application, instead of changing the configuration of physical equipment. SDN is made possible by separating the control plane from the forwarding/data plane.
