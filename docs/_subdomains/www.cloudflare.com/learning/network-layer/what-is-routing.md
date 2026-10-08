---
url: https://www.cloudflare.com/learning/network-layer/what-is-routing/
title: What is routing? | Learning Center
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:12.228636+00:00
---

# What is routing? | Learning Center

> Source: https://www.cloudflare.com/learning/network-layer/what-is-routing/

[ Learning Center ](https://www.cloudflare.com/learning/) / the network layer

##  What is routing? 

Routing is the process of selecting a path for traffic across a network or across multiple interconnected networks. 

[Learning Center](https://www.cloudflare.com/learning)/the network layer/[What is enterprise networking?](https://www.cloudflare.com/learning/network-layer/enterprise-networking/)[How to migrate from MPLS](https://www.cloudflare.com/learning/network-layer/how-to-migrate-from-mpls/)[How to prepare for network modernization projects](https://www.cloudflare.com/learning/network-layer/how-to-prepare-for-network-modernization-projects/)[What is the Internet Protocol?](https://www.cloudflare.com/learning/network-layer/internet-protocol/)[IPsec VPNs vs. SSL VPNs](https://www.cloudflare.com/learning/network-layer/ipsec-vs-ssl-vpn/)[What is NaaS (network-as-a-service)?](https://www.cloudflare.com/learning/network-layer/network-as-a-service-naas/)[What is network modernization?](https://www.cloudflare.com/learning/network-layer/network-modernization/)[What is network security?](https://www.cloudflare.com/learning/network-layer/network-security/)[SD-WAN vs. MPLS: SD-WAN benefits and drawbacks](https://www.cloudflare.com/learning/network-layer/sd-wan-vs-mpls/)[What is a campus area network (CAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-campus-area-network/)[What is a computer port? | Ports in networking](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/)[What is a metropolitan area network (MAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-metropolitan-area-network/)[What is a network switch? | Switch vs. router](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/)[What is a packet? | Network packet definition](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/)[What is a personal area network (PAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-personal-area-network/)[What is a protocol? | Network protocol definition](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/)[What is a router?](https://www.cloudflare.com/learning/network-layer/what-is-a-router/)[What is a subnet? | How subnetting works](https://www.cloudflare.com/learning/network-layer/what-is-a-subnet/)[What is a WAN? | WAN vs. LAN](https://www.cloudflare.com/learning/network-layer/what-is-a-wan/)[What is an autonomous system? | What are ASNs?](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/)[What is SD-WAN?](https://www.cloudflare.com/learning/network-layer/what-is-an-sd-wan/)[What is branch networking?](https://www.cloudflare.com/learning/network-layer/what-is-branch-networking/)[What is GRE tunneling? | How GRE protocol works](https://www.cloudflare.com/learning/network-layer/what-is-gre-tunneling/)[What is IGMP? | Internet Group Management Protocol](https://www.cloudflare.com/learning/network-layer/what-is-igmp/)[What is IGMP snooping?](https://www.cloudflare.com/learning/network-layer/what-is-igmp-snooping/)[What is IPsec? | How IPsec VPNs work](https://www.cloudflare.com/learning/network-layer/what-is-ipsec/)[What is MPLS (multiprotocol label switching)?](https://www.cloudflare.com/learning/network-layer/what-is-mpls/)[What is MSS (maximum segment size)?](https://www.cloudflare.com/learning/network-layer/what-is-mss/)[What is My Traceroute (MTR)?](https://www.cloudflare.com/learning/network-layer/what-is-mtr/)[What is MTU (maximum transmission unit)?](https://www.cloudflare.com/learning/network-layer/what-is-mtu/)[What is peering?](https://www.cloudflare.com/learning/network-layer/what-is-peering/)[What is software-defined networking (SDN)?](https://www.cloudflare.com/learning/network-layer/what-is-sdn/)[What is the control plane? | Control plane vs. data plane](https://www.cloudflare.com/learning/network-layer/what-is-the-control-plane/)[What is the network layer?](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)[What is tunneling? | Tunneling in networking](https://www.cloudflare.com/learning/network-layer/what-is-tunneling/)[How does the Internet work?](https://www.cloudflare.com/learning/network-layer/how-does-the-internet-work/)[What is routing?](https://www.cloudflare.com/learning/network-layer/what-is-routing/)[What is a LAN?](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define network routing 
  * Understand routing tables and protocols 
  * Differentiate between static and dynamic routing 



Related content  [ What is the network layer? ](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)

On this page

  * What is routing?

  * How does routing work?

  * What are the main routing protocols?

  * What is a router?

  * How does Cloudflare help make routing more efficient and secure?




## What is routing?

Network routing is the process of selecting a path across one or more networks. The principles of routing can apply to any type of network, from telephone networks to public transportation. In packet-switching networks, such as the Internet, routing selects the paths for [Internet Protocol (IP)](https://www.cloudflare.com/learning/ddos/glossary/internet-protocol/) packets to travel from their origin to their destination. These Internet routing decisions are made by specialized pieces of network hardware called [routers](https://www.cloudflare.com/learning/network-layer/what-is-a-router/).

Consider the image below. For a data packet to get from Computer A to Computer B, should it pass through networks 1, 3, and 5 or networks 2 and 4? The packet will take a shorter path through networks 2 and 4, but networks 1, 3, and 5 might be faster at forwarding packets than 2 and 4. These are the kinds of choices network routers constantly make.

![ip routing diagram](https://images.ctfassets.net/slt3lc6tev37/5biqo5wm6nM8GSmiNyiAnl/b6b5c9befeda6ba99b4380d84953de18/routing-diagram.svg)

## How does routing work?

Routers refer to internal routing tables to make decisions about how to route packets along network paths. A routing table records the paths that packets should take to reach every destination that the router is responsible for. Think of train timetables, which train passengers consult to decide which train to catch. Routing tables are like that, but for network paths rather than trains.

Routers work in the following way: when a router receives a packet, it reads the headers* of the packet to see its intended destination, like the way a train conductor may check a passenger's tickets to determine which train they should go on. It then determines where to route the packet based on information in its routing tables.

Routers do this millions of times a second with millions of packets. As a packet travels to its destination, it may be routed several times by different routers.

Routing tables can either be static or dynamic. Static routing tables do not change. A network administrator manually sets up static routing tables. This essentially sets in stone the routes data packets take across the network, unless the administrator manually updates the tables.

Dynamic routing tables update automatically. Dynamic routers use various routing protocols (see below) to determine the shortest and fastest paths. They also make this determination based on how long it takes packets to reach their destination — similar to the way Google Maps, Waze, and other GPS services determine the best driving routes based on past driving performance and current driving conditions.

Dynamic routing requires more computing power, which is why smaller networks may rely on static routing. But for medium-sized and large networks, dynamic routing is much more efficient.

_*Packet headers are small bundles of data attached to packets that provide useful information, including where the packet is coming from and where it is headed, like the packing slip stamped on the outside of a mail parcel._

## What are the main routing protocols?

In networking, a protocol is a standardized way of formatting data so that any connected computer can understand the data. A routing protocol is a protocol used for identifying or announcing network paths.

The following protocols help data packets find their way across the Internet:

**IP:** The Internet Protocol (IP) specifies the origin and destination for each data packet. Routers inspect each packet's IP header to identify where to send them.

**BGP:** The [Border Gateway Protocol (BGP)](https://www.cloudflare.com/learning/security/glossary/what-is-bgp/) routing protocol is used to announce which networks control which [IP addresses](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/), and which networks connect to each other. (The large networks that make these BGP announcements are called [autonomous systems](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/).) BGP is a dynamic routing protocol.

The below protocols route packets within an AS:

**OSPF:** The Open Shortest Path First (OSPF) protocol is commonly used by network routers to dynamically identify the fastest and shortest available routes for sending packets to their destination.

**RIP:** The Routing Information Protocol (RIP) uses "hop count" to find the shortest path from one network to another, where "hop count" means number of routers a packet must pass through on the way. (When a packet goes from one network to another, this is known as a "hop.")

Other interior routing protocols include EIGRP (the Enhanced Interior Gateway Routing Protocol, mainly for use with Cisco routers) and IS-IS (Intermediate System to Intermediate System).

## What is a router?

A router is a piece of network hardware responsible for forwarding packets to their destinations. Routers connect to two or more IP networks or subnetworks and pass data packets between them as needed. Routers are used in homes and offices for setting up local network connections. More powerful routers operate all over the Internet, helping data packets reach their destinations.

## How does Cloudflare help make routing more efficient and secure?

[Cloudflare Argo](https://www.cloudflare.com/products/argo-smart-routing/) uses [smart routing](https://www.cloudflare.com/learning/performance/routing-vs-smart-routing/) to identify the fastest routes across the Internet, sending packets around highly congested networks rather than through them. The result is similar to when car traffic is routed around traffic jams: data packets arrive faster, accelerating the online experience for users.

[Cloudflare Magic Transit](https://www.cloudflare.com/magic-transit/) uses BGP to announce IP subnets on Cloudflare customers' behalf. Network traffic to those IP addresses is routed through the Cloudflare global network rather than going directly to those customers' networks. Cloudflare filters out any attack traffic before forwarding the legitimate traffic.
