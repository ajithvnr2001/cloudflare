---
url: https://www.cloudflare.com/learning/network-layer/what-is-mtu/
title: What is MTU (maximum transmission unit)?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:06.849625+00:00
---

# What is MTU (maximum transmission unit)?

> Source: https://www.cloudflare.com/learning/network-layer/what-is-mtu/

[ Learning Center ](https://www.cloudflare.com/learning/) / the network layer

##  What is MTU (maximum transmission unit)? 

Maximum transmission unit (MTU) is a measurement in bytes of the largest data packets that an Internet-connected device can accept. 

[Learning Center](https://www.cloudflare.com/learning)/the network layer/[What is enterprise networking?](https://www.cloudflare.com/learning/network-layer/enterprise-networking/)[How to migrate from MPLS](https://www.cloudflare.com/learning/network-layer/how-to-migrate-from-mpls/)[How to prepare for network modernization projects](https://www.cloudflare.com/learning/network-layer/how-to-prepare-for-network-modernization-projects/)[What is the Internet Protocol?](https://www.cloudflare.com/learning/network-layer/internet-protocol/)[IPsec VPNs vs. SSL VPNs](https://www.cloudflare.com/learning/network-layer/ipsec-vs-ssl-vpn/)[What is NaaS (network-as-a-service)?](https://www.cloudflare.com/learning/network-layer/network-as-a-service-naas/)[What is network modernization?](https://www.cloudflare.com/learning/network-layer/network-modernization/)[What is network security?](https://www.cloudflare.com/learning/network-layer/network-security/)[SD-WAN vs. MPLS: SD-WAN benefits and drawbacks](https://www.cloudflare.com/learning/network-layer/sd-wan-vs-mpls/)[What is a campus area network (CAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-campus-area-network/)[What is a computer port? | Ports in networking](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/)[What is a metropolitan area network (MAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-metropolitan-area-network/)[What is a network switch? | Switch vs. router](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/)[What is a packet? | Network packet definition](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/)[What is a personal area network (PAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-personal-area-network/)[What is a protocol? | Network protocol definition](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/)[What is a router?](https://www.cloudflare.com/learning/network-layer/what-is-a-router/)[What is a subnet? | How subnetting works](https://www.cloudflare.com/learning/network-layer/what-is-a-subnet/)[What is a WAN? | WAN vs. LAN](https://www.cloudflare.com/learning/network-layer/what-is-a-wan/)[What is an autonomous system? | What are ASNs?](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/)[What is SD-WAN?](https://www.cloudflare.com/learning/network-layer/what-is-an-sd-wan/)[What is branch networking?](https://www.cloudflare.com/learning/network-layer/what-is-branch-networking/)[What is GRE tunneling? | How GRE protocol works](https://www.cloudflare.com/learning/network-layer/what-is-gre-tunneling/)[What is IGMP? | Internet Group Management Protocol](https://www.cloudflare.com/learning/network-layer/what-is-igmp/)[What is IGMP snooping?](https://www.cloudflare.com/learning/network-layer/what-is-igmp-snooping/)[What is IPsec? | How IPsec VPNs work](https://www.cloudflare.com/learning/network-layer/what-is-ipsec/)[What is MPLS (multiprotocol label switching)?](https://www.cloudflare.com/learning/network-layer/what-is-mpls/)[What is MSS (maximum segment size)?](https://www.cloudflare.com/learning/network-layer/what-is-mss/)[What is My Traceroute (MTR)?](https://www.cloudflare.com/learning/network-layer/what-is-mtr/)[What is MTU (maximum transmission unit)?](https://www.cloudflare.com/learning/network-layer/what-is-mtu/)[What is peering?](https://www.cloudflare.com/learning/network-layer/what-is-peering/)[What is software-defined networking (SDN)?](https://www.cloudflare.com/learning/network-layer/what-is-sdn/)[What is the control plane? | Control plane vs. data plane](https://www.cloudflare.com/learning/network-layer/what-is-the-control-plane/)[What is the network layer?](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)[What is tunneling? | Tunneling in networking](https://www.cloudflare.com/learning/network-layer/what-is-tunneling/)[How does the Internet work?](https://www.cloudflare.com/learning/network-layer/how-does-the-internet-work/)[What is routing?](https://www.cloudflare.com/learning/network-layer/what-is-routing/)[What is a LAN?](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define 'MTU' 
  * Learn how IP fragmentation works 
  * Learn about path MTU discovery in IPv4 and IPv6 



Related content  [ What is MSS (maximum segment size)? ](https://www.cloudflare.com/learning/network-layer/what-is-mss/)[ What is the network layer? ](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)[ What is an autonomous system? | What are ASNs? ](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/)[ What is a LAN? ](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/)[ What is the Internet Protocol? ](https://www.cloudflare.com/learning/network-layer/internet-protocol/)

On this page

  * What is MTU?

  * What is a packet?

  * When do packets become fragmented?

  * How does fragmentation work?

  * When is fragmentation not possible?

  * What is the &#39

  * What is path MTU discovery?

  * What is MSS?




## What is MTU?

In [networking](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/), maximum transmission unit (MTU) is a measurement representing the largest [data packet](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/) that a network-connected device will accept. Imagine it as being like a height limit for freeway underpasses or tunnels: Cars and trucks that exceed the height limit cannot fit through, just as packets that exceed the MTU of a network cannot pass through that network.

However, unlike cars and trucks, data packets that exceed MTU are broken up into smaller pieces so that they can fit through. This process is called fragmentation. Fragmented packets are reassembled once they reach their destination.

MTU is measured in bytes — a "byte" is equal to 8 bits of information, meaning 8 ones and zeroes. 1,500 bytes is the maximum MTU size.

## What is a packet?

All data sent over the Internet is broken down into smaller chunks that are called packets. For example, when a webpage is sent from a web server to a user's laptop, the webpage’s constituent data travels over the Internet as a series of packets. The packets are then reassembled into the original, whole webpage by the laptop.

Data packets have two main parts: the _header_ and the _payload_. The header contains information about the packet's source and destination addresses, while the payload is the actual contents of the packet. Think of the header as a shipping label attached to a package, and the payload as the package’s contents. (Unlike packages, packets on the Internet have multiple headers attached by different networking protocols.)

MTU almost always is used in reference to [layer 3](https://www.cloudflare.com/learning/ddos/layer-3-ddos-attacks/)* packets, or packets that use the [Internet Protocol (IP)](https://www.cloudflare.com/learning/ddos/glossary/internet-protocol/). MTU measures the packet as a whole, including all headers and the payload. This includes the IP header and the [TCP (Transport Control Protocol)](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/) header, which usually add up to 40 bytes in length.

*_The[OSI model](https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/) divides the functions that make the Internet possible into 7 layers; layer 3 is the [network layer](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/), where [routing](https://www.cloudflare.com/learning/network-layer/what-is-routing/) takes place._

## When do packets become fragmented?

When two computing devices open a connection and begin exchanging packets, those packets are routed across multiple networks. It is necessary to take into account not just the MTU of the two devices at the ends of each communication, but all [routers](https://www.cloudflare.com/learning/network-layer/what-is-a-router/), [switches](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/), and servers in the middle as well. Packets that exceed the MTU on any point in the network path are fragmented.

Suppose Server A and Computer A are connected, but the data packets they send to each other have to pass through Router B and Router C along the way. Server A, Computer A, and Router B all have an MTU of 1,500 bytes. However, Router C has an MTU of 1,400 bytes. If Server A and Computer A are not aware of Router C's MTU and send 1,500-byte packets, all their data packets will be fragmented by Router B in transit.

![Maximum transmission unit - Packet fragmented to fit 1,400 byte MTU](https://images.ctfassets.net/slt3lc6tev37/4scqAPBzaxHsj3SF9ikdFC/baf0be0ff26dc7f942ece5a834196856/mtu_fragmentation_diagram.png)Maximum transmission unit - Packet fragmented to fit 1,400 byte MTU

Fragmentation adds a small degree of [latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/) and inefficiency to network communications, so it should be avoided if possible. (Outdated network equipment may be vulnerable to [denial-of-service](https://www.cloudflare.com/learning/ddos/layer-3-ddos-attacks/) attacks that exploit fragmentation, such as the "[ping of death](https://www.cloudflare.com/learning/ddos/ping-of-death-ddos-attack/)" attack.)

## How does fragmentation work?

All network routers check the size of each IP packet they receive against the MTU of the next router that will receive the packet. If the packet exceeds the MTU of the next router, the first router breaks the payload into two or more packets, each with its own headers.

Each new packet has a header copied from the original packet (so that the packets all have the original source and destination [IP addresses](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/), etc.) with some important changes. The router edits certain fields in the IP header to indicate that the packets are fragmented and require reassembly, how many packets there are, and in what order they are being sent.

Imagine a shipping company is handling a package that exceeds the weight limits of one of their facilities. Instead of refusing to deliver the package, the shipping company divides the package contents into three smaller packages. It also duplicates the shipping label for each package and adds a note indicating that each package is one part of a series that must arrive together — the first package is 1 of 3, the second is 2 of 3, etc. (Such an approach by a shipping company would be a violation of privacy, so it should not occur in the real world.)

## When is fragmentation not possible?

In certain cases, packets cannot be fragmented, and therefore they will not be delivered if they exceed the MTU of any router or device along the network path:

  * Fragmentation is not permitted in [IPv6](https://www.cloudflare.com/learning/dns/dns-records/dns-aaaa-record/). IPv6 is the latest version of the Internet Protocol, although IPv4 is still widely used. Routers that support IPv6 will drop any IPv6 packets that exceed the MTU, because they cannot be fragmented.

  * Fragmentation is also not possible when the "Don't Fragment" flag is activated in a packet's IP header.




## What is the 'Don't Fragment' flag in an IP header?

Think of the IP header as being like a form consumers fill out when shipping a package to someone. The form indicates source address, destination address, how soon the package should be delivered, and other special instructions for the delivery workers.

The "Don't Fragment" flag is a special instruction for routers, an option that can be selected in the "form" of an IP header. When the flag is set, the attached packet cannot be fragmented.

Any router that receives the packet will analyze the header and check for the Don't Fragment flag. If the flag is on and the packet exceeds the MTU, the router then drops the packet instead of fragmenting it.

In addition to dropping the packet, the router sends back an [ICMP](https://www.cloudflare.com/learning/ddos/glossary/internet-control-message-protocol-icmp/) message to the packet's origin. An ICMP message is a very small data packet that sends a status update. In this case, it essentially says, "This router or device could not deliver these packets because they were too big and could not be fragmented."

## What is path MTU discovery?

Path MTU discovery, or PMTUD, is the process of discovering the MTU of all devices, routers, and switches on a network path. If Computer A and Server A from the example above were to use PMTUD, they would identify Router B's MTU requirements and adjust their packet size accordingly to avoid fragmentation.

PMTU works slightly differently depending on whether the connected devices are using IPv4 or IPv6:

**IPv4:** IPv4 allows fragmentation and thus includes the Don't Fragment flag in the IP header. PMTUD in IPv4 works by sending test packets along the network path with the Don't Fragment flag turned on. If any router or device along the path drops the packet, it sends back an ICMP message with its MTU. The source device lowers its MTU and sends another test packet. This process is repeated until the test packets are small enough to traverse the entire network path without being dropped.

**IPv6:** For IPv6, which does not allow fragmentation, PMTUD works in much the same way. The key difference is that IPv6 headers do not have the Don't Fragment option and so the flag is not set. Routers that support IPv6 will not fragment IPv6 packets, so if the test packets exceed the MTU, the routers drop the packets and send back corresponding ICMP messages without checking for a Don't Fragment flag. IPv6 PMTUD sends smaller and smaller test packets until the packets can traverse the entire network path, just like in IPv4.

## What is MSS?

[MSS](https://www.cloudflare.com/learning/network-layer/what-is-mss/) stands for maximum segment size. MSS is used by TCP at layer 4 of the Internet, the transport layer, instead of layer 3. MSS is only concerned with the size of the payload within each packet. It is calculated by subtracting the length of TCP and IP headers from MTU.

While packets that exceed a router's MTU are either fragmented or dropped, packets that exceed the MSS are always dropped.

To learn more about MTU and MSS, see [What is MSS?](https://www.cloudflare.com/learning/network-layer/what-is-mss/)
