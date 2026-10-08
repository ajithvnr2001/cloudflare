---
url: https://www.cloudflare.com/learning/network-layer/what-is-peering/
title: What is peering?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:09.198953+00:00
---

# What is peering?

> Source: https://www.cloudflare.com/learning/network-layer/what-is-peering/

[ Learning Center ](https://www.cloudflare.com/learning/) / the network layer

##  What is peering? 

Peering is a cost-efficient way for two large networks to connect and exchange traffic. Peering can shorten network paths and reduce latency. 

[Learning Center](https://www.cloudflare.com/learning)/the network layer/[What is enterprise networking?](https://www.cloudflare.com/learning/network-layer/enterprise-networking/)[How to migrate from MPLS](https://www.cloudflare.com/learning/network-layer/how-to-migrate-from-mpls/)[How to prepare for network modernization projects](https://www.cloudflare.com/learning/network-layer/how-to-prepare-for-network-modernization-projects/)[What is the Internet Protocol?](https://www.cloudflare.com/learning/network-layer/internet-protocol/)[IPsec VPNs vs. SSL VPNs](https://www.cloudflare.com/learning/network-layer/ipsec-vs-ssl-vpn/)[What is NaaS (network-as-a-service)?](https://www.cloudflare.com/learning/network-layer/network-as-a-service-naas/)[What is network modernization?](https://www.cloudflare.com/learning/network-layer/network-modernization/)[What is network security?](https://www.cloudflare.com/learning/network-layer/network-security/)[SD-WAN vs. MPLS: SD-WAN benefits and drawbacks](https://www.cloudflare.com/learning/network-layer/sd-wan-vs-mpls/)[What is a campus area network (CAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-campus-area-network/)[What is a computer port? | Ports in networking](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/)[What is a metropolitan area network (MAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-metropolitan-area-network/)[What is a network switch? | Switch vs. router](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/)[What is a packet? | Network packet definition](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/)[What is a personal area network (PAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-personal-area-network/)[What is a protocol? | Network protocol definition](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/)[What is a router?](https://www.cloudflare.com/learning/network-layer/what-is-a-router/)[What is a subnet? | How subnetting works](https://www.cloudflare.com/learning/network-layer/what-is-a-subnet/)[What is a WAN? | WAN vs. LAN](https://www.cloudflare.com/learning/network-layer/what-is-a-wan/)[What is an autonomous system? | What are ASNs?](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/)[What is SD-WAN?](https://www.cloudflare.com/learning/network-layer/what-is-an-sd-wan/)[What is branch networking?](https://www.cloudflare.com/learning/network-layer/what-is-branch-networking/)[What is GRE tunneling? | How GRE protocol works](https://www.cloudflare.com/learning/network-layer/what-is-gre-tunneling/)[What is IGMP? | Internet Group Management Protocol](https://www.cloudflare.com/learning/network-layer/what-is-igmp/)[What is IGMP snooping?](https://www.cloudflare.com/learning/network-layer/what-is-igmp-snooping/)[What is IPsec? | How IPsec VPNs work](https://www.cloudflare.com/learning/network-layer/what-is-ipsec/)[What is MPLS (multiprotocol label switching)?](https://www.cloudflare.com/learning/network-layer/what-is-mpls/)[What is MSS (maximum segment size)?](https://www.cloudflare.com/learning/network-layer/what-is-mss/)[What is My Traceroute (MTR)?](https://www.cloudflare.com/learning/network-layer/what-is-mtr/)[What is MTU (maximum transmission unit)?](https://www.cloudflare.com/learning/network-layer/what-is-mtu/)[What is peering?](https://www.cloudflare.com/learning/network-layer/what-is-peering/)[What is software-defined networking (SDN)?](https://www.cloudflare.com/learning/network-layer/what-is-sdn/)[What is the control plane? | Control plane vs. data plane](https://www.cloudflare.com/learning/network-layer/what-is-the-control-plane/)[What is the network layer?](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)[What is tunneling? | Tunneling in networking](https://www.cloudflare.com/learning/network-layer/what-is-tunneling/)[How does the Internet work?](https://www.cloudflare.com/learning/network-layer/how-does-the-internet-work/)[What is routing?](https://www.cloudflare.com/learning/network-layer/what-is-routing/)[What is a LAN?](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define peering 
  * Differentiate between public peering and private peering 
  * Contrast IP transit vs. peering 
  * Understand the advantages of BGP peering with Cloudflare 



Related content  [ What is an autonomous system? | What are ASNs? ](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/)[ What is the Internet Protocol? ](https://www.cloudflare.com/learning/network-layer/internet-protocol/)[ What is a network switch? | Switch vs. router ](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/)[ What is MPLS (multiprotocol label switching)? ](https://www.cloudflare.com/learning/network-layer/what-is-mpls/)[ What is network modernization? ](https://www.cloudflare.com/learning/network-layer/network-modernization/)

On this page

  * What is peering?

  * How does peering work?

    * Public peering: The role of Internet exchange points in peering

    * Private peering: How peering works via PNI

  * What is depeering?

  * How network peering improves cloud performance

  * How to peer with Cloudflare




## What is peering?

Peering is a connection between two networks that allows each network to send traffic to destinations within the other network, or to downstream destinations connected to that network. Peering occurs between very large networks, especially [autonomous systems (ASes)](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/) — mostly Internet service providers (ISPs) or large organizations managing hundreds or thousands of [IP addresses](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/).

Peering results in more efficient [routing](https://www.cloudflare.com/learning/network-layer/what-is-routing/), as networks can send traffic more directly to its destination instead of sending it through additional intermediary backbone networks. Because it is mutually beneficial, peering is free in over 99% of cases. Free peering is called "settlement-free peering" to differentiate it from the (comparatively rarer) paid arrangements. Peering agreements can be as informal as a handshake agreement, or defined by contractual terms.

Imagine two neighbors who decide to remove the fence between their houses and use each other's yards. This is somewhat like peering: they can use the other's space, even though their properties are still their own. Ideally, the result is beneficial for both neighbors.

For network operators, the alternative to peering is called transit or IP transit. This is a paid arrangement with another network that gives the paying network access to the rest of the Internet, allowing the network's traffic to pass through. Imagine if one of the neighbors from the above example moved to a house that bordered a paid arboretum or zoo; this is like the difference between peering and transit.

## How does peering work?

Peering relies on the use of the [Border Gateway Protocol (BGP)](https://www.cloudflare.com/learning/security/glossary/what-is-bgp/). This [protocol](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/) allows networks to communicate with other networks, announcing which blocks of IP addresses (these blocks are called "prefixes") they control.

Peering typically takes place through physical interconnections. The two methods used are public peering at locations called [Internet exchange points (IxPs)](https://www.cloudflare.com/learning/cdn/glossary/internet-exchange-point-ixp/), and private peering through private network interconnections.

#### Public peering: The role of Internet exchange points (IxPs) in peering

IxPs are hosted in colocation facilities, which are [data centers](https://www.cloudflare.com/learning/cdn/glossary/data-center/) where multiple businesses can host networking equipment and servers. Essentially, IxPs are large [local area networks (LAN)](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/) connected via Ethernet cables and [switches](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/). Within this local network, ASes connect via BGP. They announce their IP addresses to each other, along with the IP addresses that are connected downstream (for an ISP, this would be their customers). With this information communicated, the networks can exchange traffic through the cables and switches.

#### Private peering: How peering works via PNI

A private network interconnection (PNI) is a direct connection between networks. Some PNI connections are simply a large fiber optic cable that plugs into a physical port on each network. Some PNI connections are virtual, running through a third-party network. Just as in a public peering connections, the networks use BGP to announce their IP prefixes and downstream connections to each other.

## What is depeering?

Depeering is the process of ending a peering agreement. The two networks may unplug from each other altogether, or one network may simply decide to start charging the other network for transit. The latter is more likely to happen if one network is larger than the other and has an advantage in the market.

## How network peering improves cloud performance

Since peering results in the most direct connection possible between networks, peering with a [public cloud](https://www.cloudflare.com/learning/cloud/what-is-a-public-cloud/) can vastly improve cloud performance.

Traffic to and from the cloud ordinarily goes over the public Internet, which means it may take different routes each time and can get slowed down by network congestion or outages. It may also be expensive if an organization has to send a lot of traffic to the cloud via paid IP transit. Directly peering with a public cloud provider, in contrast, allows traffic to pass immediately to destinations in the cloud, for a more reliable and faster connection.

## How to peer (or interconnect) with Cloudflare

Cloudflare has an [open peering policy](https://www.cloudflare.com/peering-policy/): in fact, there is no need to be a Cloudflare customer to peer with Cloudflare. Today Cloudflare interconnects with over %{NetworkInterconnects} networks globally. The result is that Cloudflare is tightly connected with networks and ISPs all over the globe for extraordinarily fast traffic routing anywhere.

For customers, Cloudflare offers [Cloudflare Network Interconnect](https://www.cloudflare.com/network-services/products/network-interconnect/), the most direct connection possible to the [connectivity cloud](https://www.cloudflare.com/connectivity-cloud/). Connections can be physical or virtual, and can take place at any of a number of IxPs or through several partners. Cloudflare also enables customers to set up BGP peering, which can improve performance and reduce the [bandwidth](https://www.cloudflare.com/learning/cdn/how-cdns-reduce-bandwidth-cost/) used via Internet transit links.

Peering or interconnecting with Cloudflare can help organizations [begin to modernize their networks](https://www.cloudflare.com/learning/network-layer/how-to-prepare-for-network-modernization-projects/), optimizing for cloud usage and hybrid workforces. Learn more about getting started with [network modernization](https://www.cloudflare.com/learning/network-layer/network-modernization/).
