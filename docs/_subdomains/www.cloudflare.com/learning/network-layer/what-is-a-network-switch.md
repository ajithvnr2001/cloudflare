---
url: https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/
title: What is a network switch? | Switch vs. router
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:47.634439+00:00
---

# What is a network switch? | Switch vs. router

> Source: https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/

[ Learning Center ](https://www.cloudflare.com/learning/) / the network layer

##  What is a network switch? | Switch vs. router 

A network switch forwards data packets between devices. Switches send packets directly to devices, rather than sending them to networks like a router does. 

[Learning Center](https://www.cloudflare.com/learning)/the network layer/[What is enterprise networking?](https://www.cloudflare.com/learning/network-layer/enterprise-networking/)[How to migrate from MPLS](https://www.cloudflare.com/learning/network-layer/how-to-migrate-from-mpls/)[How to prepare for network modernization projects](https://www.cloudflare.com/learning/network-layer/how-to-prepare-for-network-modernization-projects/)[What is the Internet Protocol?](https://www.cloudflare.com/learning/network-layer/internet-protocol/)[IPsec VPNs vs. SSL VPNs](https://www.cloudflare.com/learning/network-layer/ipsec-vs-ssl-vpn/)[What is NaaS (network-as-a-service)?](https://www.cloudflare.com/learning/network-layer/network-as-a-service-naas/)[What is network modernization?](https://www.cloudflare.com/learning/network-layer/network-modernization/)[What is network security?](https://www.cloudflare.com/learning/network-layer/network-security/)[SD-WAN vs. MPLS: SD-WAN benefits and drawbacks](https://www.cloudflare.com/learning/network-layer/sd-wan-vs-mpls/)[What is a campus area network (CAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-campus-area-network/)[What is a computer port? | Ports in networking](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/)[What is a metropolitan area network (MAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-metropolitan-area-network/)[What is a network switch? | Switch vs. router](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/)[What is a packet? | Network packet definition](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/)[What is a personal area network (PAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-personal-area-network/)[What is a protocol? | Network protocol definition](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/)[What is a router?](https://www.cloudflare.com/learning/network-layer/what-is-a-router/)[What is a subnet? | How subnetting works](https://www.cloudflare.com/learning/network-layer/what-is-a-subnet/)[What is a WAN? | WAN vs. LAN](https://www.cloudflare.com/learning/network-layer/what-is-a-wan/)[What is an autonomous system? | What are ASNs?](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/)[What is SD-WAN?](https://www.cloudflare.com/learning/network-layer/what-is-an-sd-wan/)[What is branch networking?](https://www.cloudflare.com/learning/network-layer/what-is-branch-networking/)[What is GRE tunneling? | How GRE protocol works](https://www.cloudflare.com/learning/network-layer/what-is-gre-tunneling/)[What is IGMP? | Internet Group Management Protocol](https://www.cloudflare.com/learning/network-layer/what-is-igmp/)[What is IGMP snooping?](https://www.cloudflare.com/learning/network-layer/what-is-igmp-snooping/)[What is IPsec? | How IPsec VPNs work](https://www.cloudflare.com/learning/network-layer/what-is-ipsec/)[What is MPLS (multiprotocol label switching)?](https://www.cloudflare.com/learning/network-layer/what-is-mpls/)[What is MSS (maximum segment size)?](https://www.cloudflare.com/learning/network-layer/what-is-mss/)[What is My Traceroute (MTR)?](https://www.cloudflare.com/learning/network-layer/what-is-mtr/)[What is MTU (maximum transmission unit)?](https://www.cloudflare.com/learning/network-layer/what-is-mtu/)[What is peering?](https://www.cloudflare.com/learning/network-layer/what-is-peering/)[What is software-defined networking (SDN)?](https://www.cloudflare.com/learning/network-layer/what-is-sdn/)[What is the control plane? | Control plane vs. data plane](https://www.cloudflare.com/learning/network-layer/what-is-the-control-plane/)[What is the network layer?](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)[What is tunneling? | Tunneling in networking](https://www.cloudflare.com/learning/network-layer/what-is-tunneling/)[How does the Internet work?](https://www.cloudflare.com/learning/network-layer/how-does-the-internet-work/)[What is routing?](https://www.cloudflare.com/learning/network-layer/what-is-routing/)[What is a LAN?](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define network switch 
  * Learn the difference between a switch vs. a router 
  * Learn about Ethernet switches, unmanaged and managed switches, and more 



Related content  [ What is the network layer? ](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)[ What is routing? ](https://www.cloudflare.com/learning/network-layer/what-is-routing/)[ How does the Internet work? ](https://www.cloudflare.com/learning/network-layer/how-does-the-internet-work/)[ What is an autonomous system? | What are ASNs? ](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/)[ What is MSS (maximum segment size)? ](https://www.cloudflare.com/learning/network-layer/what-is-mss/)

On this page

  * What is a network switch?

  * What is the difference between a switch and a router?

  * What is a layer 2 switch? What is a layer 3 switch?

  * What is an unmanaged switch? What is a managed switch?

  * What is the difference between a MAC address and an IP address?

  * How do network switches know the MAC addresses of the devices in their network?

  * How does Cloudflare protect network switches?




## What is a network switch?

A network switch connects devices within a network (often a [local area network, or LAN](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/)*) and forwards [data packets](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/) to and from those devices. Unlike a [router](https://www.cloudflare.com/learning/network-layer/what-is-a-router/), a switch only sends data to the single device it is intended for (which may be another switch, a router, or a user's computer), not to networks of multiple devices.

![Network traffic goes from Internet to router to network switch to computers](https://images.ctfassets.net/slt3lc6tev37/6ENfwtM3iUH99JpYoEC9FY/04abc1654ceff2645f50713394ebcb73/network-switch.svg)Network traffic goes from Internet to router to network switch to computers

*_A local area network (LAN) is a group of connected devices within close physical proximity. Home WiFi networks are one common example of a LAN._

Whitepaper

How to break free from network hardware

[Get the report →](https://www.cloudflare.com/lp/network-hardware/)Whitepaper

Developing a strategy for your network modernization

[Read the whitepaper →](https://www.cloudflare.com/lp/developing-a-strategy-for-network-modernization/)

## What is the difference between a switch and a router?

Routers select paths for data packets to cross networks and reach their destinations. Routers do this by connecting with different networks and forwarding data from network to network — including LANs, [wide area networks (WANs)](https://www.cloudflare.com/learning/network-layer/what-is-a-wan/), or [autonomous systems](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/), which are the large networks that make up the Internet.

In practice, what this means is that routers are necessary for an Internet connection, while switches are only used for interconnecting devices. Homes and small offices need routers for Internet access, but most do not need a network switch, unless they require a large amount of Ethernet* ports. However, large offices, networks, and data centers with dozens or hundreds of computers usually do require switches.

*_Ethernet is a layer 2[protocol](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/) for sending data between devices. Unlike WiFi, Ethernet requires a physical connection via an Ethernet cable._

## What is a layer 2 switch? What is a layer 3 switch?

Network switches can operate at either [OSI](https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/) layer 2 (the data link layer) or [layer 3](https://www.cloudflare.com/learning/ddos/layer-3-ddos-attacks/) (the [network layer](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)). Layer 2 switches forward data based on the destination MAC address (see below for definition), while layer 3 switches forward data based on the destination [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/). Some switches can do both.

Most switches, however, are layer 2 switches. Layer 2 switches most often connect to the devices in their networks using Ethernet cables. Ethernet cables are physical cables that plug into devices via Ethernet ports.

## What is an unmanaged switch? What is a managed switch?

An unmanaged switch simply creates more Ethernet ports on a LAN, so that more local devices can access the Internet. Unmanaged switches pass data back and forth based on device MAC addresses.

A managed switch fulfills the same function for much larger networks, and offers network administrators much more control over how traffic is prioritized. They also enable administrators to set up Virtual LANs (VLANs) to further subdivide a local network into smaller chunks.

Sign Up

Security & speed with any Cloudflare plan

[Start for free →](https://www.cloudflare.com/plans/)

## What is the difference between a MAC address and an IP address?

Network switches refer to MAC addresses in order to send Internet traffic to the right devices, not IP addresses.

Every device that connects to the Internet has an IP address. An IP address is a series of alphanumeric characters, like 192.0.2.255 or 2001:0db8:85a3:0000:0000:8a2e:0370:7334. IP addresses act like a mailing address, enabling Internet communications directed at that address to reach that device. IP addresses often change: because there is a limited number of IPv4 addresses, user devices are typically assigned new ones when they form a new connection with a network.

IP addresses are used at layer 3, which means computers and devices all over the Internet use IP addresses for sending and receiving data, no matter which network they are connected to. All IP packets include their source and destination IP addresses in their headers, just as a piece of mail has a destination address and a return address.

In contrast, a MAC address is a permanent identifier for each piece of hardware, somewhat like a serial number. Unlike IP addresses, MAC addresses do not change. MAC addresses are used at layer 2, not layer 3 — which means they are not included in IP packet headers. In other words, MAC addresses are not part of Internet traffic. They are only used inside a given network.

## How do network switches know the MAC addresses of the devices in their network?

Layer 2 network switches maintain a table in memory that matches MAC addresses to the switch's Ethernet ports. This table is called a Content Addressable Memory (CAM) table.

Suppose Computer A is connected to an Ethernet cable that plugs into the switch's Port 1, Computer B is connected to Port 2, and Computer C to Port 3. When data arrives for Computer A, the switch consults its CAM table, sees where Computer A is connected, and knows to forward Computer A-bound traffic at Port 1, not Ports 2 or 3.

The switch's CAM table would look something like this:

MAC address Port

Computer A's MAC address 1

Computer B's MAC address 2

Computer C's MAC address 3

The switch's CAM table is stored in memory. If the switch is turned off, the table will disappear and the switch has to relearn the table when it is rebooted.

Now, suppose the switch was just turned on and has not yet created its CAM table. It does not know which ports Computers A, B, and C are connected to. It also does not know their MAC addresses.

MAC address Port

? ?

? ?

? ?

Suppose Computer A sends a message to Computer B. The switch takes the following steps to get the message to Computer B and start filling out its CAM table:

  * It records Computer A's MAC address and the port its message came in on

  * It forwards Computer A's message to all other computers on the network (except Computer A); this is known as "flooding"

  * When Computer B replies, it records Computer B's MAC address and port as well




MAC address Port

Computer A's MAC address 1

Computer B's MAC address 2

? ?

Now, the switch's CAM table knows where Computer A and Computer B are. It also knows their MAC addresses.

## How does Cloudflare protect network switches?

Cloudflare Magic Transit protects [network infrastructure](https://www.cloudflare.com/the-net/network-infrastructure/) devices such as switches and routers from [DDoS](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/) attack traffic that can knock them offline or compromise them. Magic Transit protects on-premise, [cloud](https://www.cloudflare.com/learning/cloud/what-is-the-cloud/), and [hybrid](https://www.cloudflare.com/learning/cloud/what-is-hybrid-cloud/) networks. Learn more about [Magic Transit](https://www.cloudflare.com/magic-transit/) or about [layer 3 attacks](https://www.cloudflare.com/learning/ddos/layer-3-ddos-attacks/).
