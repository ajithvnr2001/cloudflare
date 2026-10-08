---
url: https://www.cloudflare.com/learning/network-layer/what-is-sdn/
title: What is software-defined networking (SDN)?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:11.775978+00:00
---

# What is software-defined networking (SDN)?

> Source: https://www.cloudflare.com/learning/network-layer/what-is-sdn/

[ Learning Center ](https://www.cloudflare.com/learning/) / the network layer

##  What is software-defined networking (SDN)? 

Software-defined networking (SDN) makes it possible to configure and manage a network using software instead of hardware. 

[Learning Center](https://www.cloudflare.com/learning)/the network layer/[What is enterprise networking?](https://www.cloudflare.com/learning/network-layer/enterprise-networking/)[How to migrate from MPLS](https://www.cloudflare.com/learning/network-layer/how-to-migrate-from-mpls/)[How to prepare for network modernization projects](https://www.cloudflare.com/learning/network-layer/how-to-prepare-for-network-modernization-projects/)[What is the Internet Protocol?](https://www.cloudflare.com/learning/network-layer/internet-protocol/)[IPsec VPNs vs. SSL VPNs](https://www.cloudflare.com/learning/network-layer/ipsec-vs-ssl-vpn/)[What is NaaS (network-as-a-service)?](https://www.cloudflare.com/learning/network-layer/network-as-a-service-naas/)[What is network modernization?](https://www.cloudflare.com/learning/network-layer/network-modernization/)[What is network security?](https://www.cloudflare.com/learning/network-layer/network-security/)[SD-WAN vs. MPLS: SD-WAN benefits and drawbacks](https://www.cloudflare.com/learning/network-layer/sd-wan-vs-mpls/)[What is a campus area network (CAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-campus-area-network/)[What is a computer port? | Ports in networking](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/)[What is a metropolitan area network (MAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-metropolitan-area-network/)[What is a network switch? | Switch vs. router](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/)[What is a packet? | Network packet definition](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/)[What is a personal area network (PAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-personal-area-network/)[What is a protocol? | Network protocol definition](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/)[What is a router?](https://www.cloudflare.com/learning/network-layer/what-is-a-router/)[What is a subnet? | How subnetting works](https://www.cloudflare.com/learning/network-layer/what-is-a-subnet/)[What is a WAN? | WAN vs. LAN](https://www.cloudflare.com/learning/network-layer/what-is-a-wan/)[What is an autonomous system? | What are ASNs?](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/)[What is SD-WAN?](https://www.cloudflare.com/learning/network-layer/what-is-an-sd-wan/)[What is branch networking?](https://www.cloudflare.com/learning/network-layer/what-is-branch-networking/)[What is GRE tunneling? | How GRE protocol works](https://www.cloudflare.com/learning/network-layer/what-is-gre-tunneling/)[What is IGMP? | Internet Group Management Protocol](https://www.cloudflare.com/learning/network-layer/what-is-igmp/)[What is IGMP snooping?](https://www.cloudflare.com/learning/network-layer/what-is-igmp-snooping/)[What is IPsec? | How IPsec VPNs work](https://www.cloudflare.com/learning/network-layer/what-is-ipsec/)[What is MPLS (multiprotocol label switching)?](https://www.cloudflare.com/learning/network-layer/what-is-mpls/)[What is MSS (maximum segment size)?](https://www.cloudflare.com/learning/network-layer/what-is-mss/)[What is My Traceroute (MTR)?](https://www.cloudflare.com/learning/network-layer/what-is-mtr/)[What is MTU (maximum transmission unit)?](https://www.cloudflare.com/learning/network-layer/what-is-mtu/)[What is peering?](https://www.cloudflare.com/learning/network-layer/what-is-peering/)[What is software-defined networking (SDN)?](https://www.cloudflare.com/learning/network-layer/what-is-sdn/)[What is the control plane? | Control plane vs. data plane](https://www.cloudflare.com/learning/network-layer/what-is-the-control-plane/)[What is the network layer?](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)[What is tunneling? | Tunneling in networking](https://www.cloudflare.com/learning/network-layer/what-is-tunneling/)[How does the Internet work?](https://www.cloudflare.com/learning/network-layer/how-does-the-internet-work/)[What is routing?](https://www.cloudflare.com/learning/network-layer/what-is-routing/)[What is a LAN?](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/)

######  Learning objectives 

After reading this article you will be able to: 

  * Learn how software-defined networking works 
  * Explore the applications for SDN 
  * Compare SDN with SD-WANs 



Related content  [ What is a WAN? | WAN vs. LAN ](https://www.cloudflare.com/learning/network-layer/what-is-a-wan/)[ What is a LAN? ](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/)[ What is the network layer? ](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)[ What is MSS (maximum segment size)? ](https://www.cloudflare.com/learning/network-layer/what-is-mss/)[ What is MTU (maximum transmission unit)? ](https://www.cloudflare.com/learning/network-layer/what-is-mtu/)

On this page

  * Article Summary:

  * What is software-defined networking?

  * What is the control plane?

  * What is network topology?

  * What are some of the main uses for SDN?

  * What is the difference between SDN and SD-WAN?




## Article Summary:

  * Software-defined networking (SDN) centralizes network management by separating the control plane from the forwarding plane, enabling administrators to programmatically control traffic flow and enhance overall agility.

  * By utilizing SDN, organizations transition from hardware-based configurations to software-based virtualization, which simplifies complex network architectures and improves scalability across diverse cloud environments.

  * Implementing software-defined networking improves security and efficiency, allowing for automated resource allocation and granular visibility into data packets moving across the entire network infrastructure.




## What is software-defined networking (SDN)?

Software-defined networking (SDN) is a category of technologies that make it possible to manage a [network](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/) via software. SDN technology enables IT administrators to configure their networks using a software application. SDN software is interoperable, meaning it should be able to work with any [router](https://www.cloudflare.com/learning/network-layer/what-is-routing/) or [switch](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/), no matter which vendor made it.

## What is the control plane?

Technically speaking, SDN is made possible by separating the control plane from the data plane. "Plane" is a networking term that refers to an abstract conception of where networking processes take place. The control plane refers to networking processes that direct network traffic, while the data plane is the actual data traversing the network. The control plane does this by establishing network routes and communicating which protocols should be used.

Think of the control plane as being like the collective group of stoplights that operate at the intersections of a city. Meanwhile, the data plane is more like the cars that drive on the roads, stop at the intersections, and obey the stoplights.

In networking setups that only use physical hardware, each individual router or switch has to be configured on its own. The control plane is closely intertwined with the data plane and with the underlying network hardware. With SDN, the control plane is separated from the data plane and the actual hardware, making it possible to configure the control plane from a central location.

## What is network topology?

"Network topology" is a term that refers to the way data flows in a network. The control plane establishes and changes network topology. Again, think of the stoplights that function at the intersections of a city. Network topology is like the arrangement of the roads and the various destinations in the city, with network routes being like the roads and computing devices like destinations. Meanwhile, routers and switches are the stoplights operating at the "intersections" of these routes.

Network topology does not refer to the physical positions of routers, switches, and computers in relation to each other. Rather, it has to do solely with the paths data takes within the network. If two computers connect directly to a network switch via Ethernet cables, and Computer A is on the near side of the room next to the switch while Computer B is on the far side of the room, both computers are equidistant from the switch in the network topology.

In SDN, because the control plane is separated from the underlying hardware, it is possible to change the network topology via software instead of hardware. Referring back to the example, if an admin using SDN wanted to change where Computer B was in the network topology, they could use their networking software to redefine the topology so that traffic went from the switch to (for instance) another router before going to Computer B.

## What are some of the main uses for SDN?

Software-defined networks are increasingly used in large data centers. A data center is a collection of servers and networking equipment, typically within a single building, which stores, processes, and exchanges data. Almost all [web servers](https://www.cloudflare.com/learning/cdn/glossary/origin-server/) are located inside data centers, and many companies operate their own data centers for storing corporate data and running internal applications (e.g. corporate email). Because data centers use so much physical networking equipment, SDN makes administrative work within them much easier.

SDN also enables companies to more easily connect their on-premise infrastructure with their cloud infrastructure, as in a [hybrid cloud](https://www.cloudflare.com/learning/cloud/what-is-hybrid-cloud/) deployment. Corporate clouds can connect with software much more easily than with hardware; hardware often introduces compatibility issues, while cloud software and SDN software can integrate regardless of the underlying hardware. In fact, many vendors offer both cloud services and an SDN product, making hybrid cloud integrations even simpler.

## What is the difference between SDN and SD-WAN?

A software-defined [wide area network](https://www.cloudflare.com/learning/network-layer/what-is-a-wan/), or [SD-WAN](https://www.cloudflare.com/learning/network-layer/what-is-an-sd-wan/), is a type of software-based network architecture. SD-WANs are one application of software-defined networking. Essentially, all SD-WANs use SDN, but not all software-defined networks are SD-WANs.

Many companies are turning to SDN or SD-WANs as their technology stacks move to the cloud. A software-based virtualized approach to networking enables them to be more flexible. However, software-defined networks are open to various kinds of attacks, including [DDoS attacks](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/). Cloudflare [Magic Transit](https://www.cloudflare.com/magic-transit/) [protects on-premise, hybrid, and cloud networks](https://www.cloudflare.com/network-security/) from such attacks.

In addition, Cloudflare WAN provides a faster, more secure alternative to the use of SD-WANs. Learn more about [Cloudflare WAN](https://www.cloudflare.com/magic-wan).
