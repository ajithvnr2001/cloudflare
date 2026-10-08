---
url: https://www.cloudflare.com/learning/network-layer/what-is-mpls/
title: What is MPLS (multiprotocol label switching)?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:06.655870+00:00
---

# What is MPLS (multiprotocol label switching)?

> Source: https://www.cloudflare.com/learning/network-layer/what-is-mpls/

[ Learning Center ](https://www.cloudflare.com/learning/) / the network layer

##  What is MPLS (multiprotocol label switching)? 

Multiprotocol label switching (MPLS) is a method for setting up dedicated paths across networks without relying on the typical routing process. 

[Learning Center](https://www.cloudflare.com/learning)/the network layer/[What is enterprise networking?](https://www.cloudflare.com/learning/network-layer/enterprise-networking/)[How to migrate from MPLS](https://www.cloudflare.com/learning/network-layer/how-to-migrate-from-mpls/)[How to prepare for network modernization projects](https://www.cloudflare.com/learning/network-layer/how-to-prepare-for-network-modernization-projects/)[What is the Internet Protocol?](https://www.cloudflare.com/learning/network-layer/internet-protocol/)[IPsec VPNs vs. SSL VPNs](https://www.cloudflare.com/learning/network-layer/ipsec-vs-ssl-vpn/)[What is NaaS (network-as-a-service)?](https://www.cloudflare.com/learning/network-layer/network-as-a-service-naas/)[What is network modernization?](https://www.cloudflare.com/learning/network-layer/network-modernization/)[What is network security?](https://www.cloudflare.com/learning/network-layer/network-security/)[SD-WAN vs. MPLS: SD-WAN benefits and drawbacks](https://www.cloudflare.com/learning/network-layer/sd-wan-vs-mpls/)[What is a campus area network (CAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-campus-area-network/)[What is a computer port? | Ports in networking](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/)[What is a metropolitan area network (MAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-metropolitan-area-network/)[What is a network switch? | Switch vs. router](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/)[What is a packet? | Network packet definition](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/)[What is a personal area network (PAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-personal-area-network/)[What is a protocol? | Network protocol definition](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/)[What is a router?](https://www.cloudflare.com/learning/network-layer/what-is-a-router/)[What is a subnet? | How subnetting works](https://www.cloudflare.com/learning/network-layer/what-is-a-subnet/)[What is a WAN? | WAN vs. LAN](https://www.cloudflare.com/learning/network-layer/what-is-a-wan/)[What is an autonomous system? | What are ASNs?](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/)[What is SD-WAN?](https://www.cloudflare.com/learning/network-layer/what-is-an-sd-wan/)[What is branch networking?](https://www.cloudflare.com/learning/network-layer/what-is-branch-networking/)[What is GRE tunneling? | How GRE protocol works](https://www.cloudflare.com/learning/network-layer/what-is-gre-tunneling/)[What is IGMP? | Internet Group Management Protocol](https://www.cloudflare.com/learning/network-layer/what-is-igmp/)[What is IGMP snooping?](https://www.cloudflare.com/learning/network-layer/what-is-igmp-snooping/)[What is IPsec? | How IPsec VPNs work](https://www.cloudflare.com/learning/network-layer/what-is-ipsec/)[What is MPLS (multiprotocol label switching)?](https://www.cloudflare.com/learning/network-layer/what-is-mpls/)[What is MSS (maximum segment size)?](https://www.cloudflare.com/learning/network-layer/what-is-mss/)[What is My Traceroute (MTR)?](https://www.cloudflare.com/learning/network-layer/what-is-mtr/)[What is MTU (maximum transmission unit)?](https://www.cloudflare.com/learning/network-layer/what-is-mtu/)[What is peering?](https://www.cloudflare.com/learning/network-layer/what-is-peering/)[What is software-defined networking (SDN)?](https://www.cloudflare.com/learning/network-layer/what-is-sdn/)[What is the control plane? | Control plane vs. data plane](https://www.cloudflare.com/learning/network-layer/what-is-the-control-plane/)[What is the network layer?](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)[What is tunneling? | Tunneling in networking](https://www.cloudflare.com/learning/network-layer/what-is-tunneling/)[How does the Internet work?](https://www.cloudflare.com/learning/network-layer/how-does-the-internet-work/)[What is routing?](https://www.cloudflare.com/learning/network-layer/what-is-routing/)[What is a LAN?](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand how multiprotocol label switching (MPLS) works 
  * Contrast MPLS with the typical Internet routing process 
  * Explore the uses for and drawbacks of MPLS 



Related content  [ What is a protocol? | Network protocol definition ](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/)[ What is the Internet Protocol? ](https://www.cloudflare.com/learning/network-layer/internet-protocol/)[ What is IGMP? | Internet Group Management Protocol ](https://www.cloudflare.com/learning/network-layer/what-is-igmp/)[ What is a network switch? | Switch vs. router ](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/)[ What is routing? ](https://www.cloudflare.com/learning/network-layer/what-is-routing/)

On this page

  * What is multiprotocol label switching?

  * How does routing normally work?

  * How does routing work in MPLS?

  * Is an MPLS network a &#39

  * What are the drawbacks of MPLS?

  * When is MPLS used?




## What is multiprotocol label switching (MPLS)?

Multiprotocol label switching (MPLS) is a technique for setting up long-range network connections, first developed in the 1990s. The public Internet functions by forwarding [packets](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/) from one [router](https://www.cloudflare.com/learning/network-layer/what-is-a-router/) to the next until the packets reach their destination. MLPS, on the other hand, sends packets along predetermined network paths. Ideally, the result is that routers do not have to decide where to forward each packet, and packets take the same path every time. The result is highly reliable network paths that can connect far-flung branch locations within a corporate [wide area network (WAN)](https://www.cloudflare.com/learning/network-layer/what-is-a-wan/).

Consider the process of planning a long drive. Instead of identifying which towns and cities one must drive through in order to reach the destination, it is usually more efficient to identify the roads that go in the correct direction. Similarly, MPLS identifies paths — network "roads" — rather than a series of intermediary destinations.

MPLS is considered to operate at [OSI](https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/) layer "2.5", below the [network layer](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/) (layer 3) and above the data link layer (layer 2).

Start building

Build, deploy, and deliver trusted applications

[Get started →](https://www.cloudflare.com/lp/pg-developer-platform-multi-sku/)

## How does routing normally work?

Anything sent from one computer to another over the Internet is divided up into smaller pieces called packets, instead of getting sent all at once. For example, this webpage was sent to your computer or device in a series of packets that your device reassembled and then displayed. Each packet has an attached header that contains information about where the packet is from and where it is going, including its destination [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/) (like the address on a piece of mail).

For a packet to reach its intended destination, routers have to forward it from one network to the next until it finally arrives at the network that contains its destination IP address. That network will then forward the packet to that address and the associated device.

Before routers can forward a packet to its final IP address, they must first determine where the packet needs to go. Routers do this by referencing and maintaining a routing table, which tells them how to forward each packet. Each router examines the packet's headers, consults its internal routing table, and forwards the packet to the next network. A router in the next network goes through the same process, and the process repeats until the packet arrives at its destination.

This approach to [routing](https://www.cloudflare.com/learning/network-layer/what-is-routing/) works well for most purposes; most of the Internet runs using IP addresses and routing tables. However, some users or organizations want their data to travel over paths they can directly control. This is particularly the case when organizations need to ensure reliable connectivity to their internal network at different branch offices, campuses, retail locations, or other remote locations.

Whitepaper

Developing a strategy for your network modernization

[Read the whitepaper →](https://www.cloudflare.com/lp/developing-a-strategy-for-network-modernization/)

## How does routing work in MPLS?

In typical Internet routing, each individual router makes decisions independently based on its own internal routing table. Even if two packets come from the same place and are going to the same destination, they may take different network paths if a router updates its routing table after the first packet passes through. However, with MPLS, packets take the same path every time.

In a network that uses MPLS, each packet is assigned to a class called a forwarding equivalence class (FEC). The network paths that packets can take are called label-switched paths (LSP). A packet's class (FEC) determines which path (LSP) the packet will be assigned to. Packets with the same FEC follow the same LSP.

Each packet has one or more labels attached, and all labels are contained in an MPLS header, which is added on top of all the other headers attached to a packet. FECs are listed within each packet's labels. Routers do not examine the packet's other headers; they can essentially ignore the IP header. Instead, they examine the packet's label and direct the packet to the right LSP.

Because MPLS-supporting routers only need to see the MPLS labels attached to a given packet, MPLS can work with almost any protocol (hence the name "multiprotocol"). It does not matter how the rest of the packet is formatted, as long as the router can read the MPLS labels at the front of the packet.

## Is an MPLS network a 'private' network?

MPLS can be "private" in the sense that only one organization uses certain MPLS paths. However, MPLS does not [encrypt](https://www.cloudflare.com/learning/ssl/what-is-encryption/) traffic. If packets are intercepted along the paths, they can be read. A [virtual private network (VPN)](https://www.cloudflare.com/learning/access-management/what-is-a-vpn/) does provide encryption and is one method for keeping network connections truly private. But whether a VPN or some other security service is used, MPLS is not secure by default.

## What are the drawbacks of MPLS?

**Cost:** MPLS is more expensive than regular Internet service.

**Long setup time:** Setting up complicated dedicated paths across one or more large networks takes time. LSPs have to be manually configured by the MPLS vendor or by the organization using MPLS. This makes it difficult for organizations to scale up their networks quickly.

**Complexity:** MPLS is usually a managed service offered by Internet service providers (ISPs). Since ISPs have different coverage areas, this makes MPLS a region-specific service, and it has to be negotiated with multiple different providers for WANs that span a country or the globe.

**Lack of encryption:** MPLS is not encrypted; any attacker that intercepts packets on MPLS paths can read them in plaintext. Encryption has to be set up separately.

**Cloud challenges:** Organizations that rely on [cloud services](https://www.cloudflare.com/learning/cloud/what-is-the-cloud/) may not be able to set up direct network connections to their cloud servers, as they do not have access to the specific servers where their data and applications live.

## When is MPLS used?

MPLS has often been used to set up wide area networks (WANs) for [branch networking](https://www.cloudflare.com/learning/network-layer/what-is-branch-networking/), connecting various locations to a central headquarters or data center. Branch networks built with MPLS allow spread-out branch offices, restaurants, or campuses to exchange information and access the applications they need.

However, WANs built on MPLS are costly, complex, and difficult to scale up. And because routes are predetermined, network traffic must often be backhauled to central locations, resulting in network bottlenecks and inefficiencies. Many corporate WANs are undergoing a process of [network modernization](https://www.cloudflare.com/learning/network-layer/network-modernization/) to better support cloud computing, remote work, and the use of [Internet of Things (IoT)](https://www.cloudflare.com/learning/ddos/glossary/internet-of-things-iot/) devices.

To [replace MPLS](https://www.cloudflare.com/learning/network-layer/how-to-migrate-from-mpls/), some organizations adopt managed [software-defined WAN (SD-WAN)](https://www.cloudflare.com/learning/network-layer/what-is-an-sd-wan/) services, which are often more flexible and less expensive. Others are turning to [secure access service edge (SASE)](https://www.cloudflare.com/learning/access-management/what-is-sase/) vendors for even better support for the cloud and hybrid work, with security built in instead of tacked on.

Cloudflare WAN replaces or augments MPLS connections with a cloud-based network that is easy to set up and does not rely on expensive hardware appliances. Learn more about [Cloudflare WAN](https://www.cloudflare.com/magic-wan).
