---
url: https://www.cloudflare.com/learning/network-layer/internet-protocol/
title: What is the Internet Protocol?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:29.390413+00:00
---

# What is the Internet Protocol?

> Source: https://www.cloudflare.com/learning/network-layer/internet-protocol/

[ Learning Center ](https://www.cloudflare.com/learning/) / the network layer

##  What is the Internet Protocol? 

The Internet Protocol (IP) is a set of requirements for addressing and routing data on the Internet. IP can be used with several transport protocols, including TCP and UDP. 

[Learning Center](https://www.cloudflare.com/learning)/the network layer/[What is enterprise networking?](https://www.cloudflare.com/learning/network-layer/enterprise-networking/)[How to migrate from MPLS](https://www.cloudflare.com/learning/network-layer/how-to-migrate-from-mpls/)[How to prepare for network modernization projects](https://www.cloudflare.com/learning/network-layer/how-to-prepare-for-network-modernization-projects/)[What is the Internet Protocol?](https://www.cloudflare.com/learning/network-layer/internet-protocol/)[IPsec VPNs vs. SSL VPNs](https://www.cloudflare.com/learning/network-layer/ipsec-vs-ssl-vpn/)[What is NaaS (network-as-a-service)?](https://www.cloudflare.com/learning/network-layer/network-as-a-service-naas/)[What is network modernization?](https://www.cloudflare.com/learning/network-layer/network-modernization/)[What is network security?](https://www.cloudflare.com/learning/network-layer/network-security/)[SD-WAN vs. MPLS: SD-WAN benefits and drawbacks](https://www.cloudflare.com/learning/network-layer/sd-wan-vs-mpls/)[What is a campus area network (CAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-campus-area-network/)[What is a computer port? | Ports in networking](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/)[What is a metropolitan area network (MAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-metropolitan-area-network/)[What is a network switch? | Switch vs. router](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/)[What is a packet? | Network packet definition](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/)[What is a personal area network (PAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-personal-area-network/)[What is a protocol? | Network protocol definition](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/)[What is a router?](https://www.cloudflare.com/learning/network-layer/what-is-a-router/)[What is a subnet? | How subnetting works](https://www.cloudflare.com/learning/network-layer/what-is-a-subnet/)[What is a WAN? | WAN vs. LAN](https://www.cloudflare.com/learning/network-layer/what-is-a-wan/)[What is an autonomous system? | What are ASNs?](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/)[What is SD-WAN?](https://www.cloudflare.com/learning/network-layer/what-is-an-sd-wan/)[What is branch networking?](https://www.cloudflare.com/learning/network-layer/what-is-branch-networking/)[What is GRE tunneling? | How GRE protocol works](https://www.cloudflare.com/learning/network-layer/what-is-gre-tunneling/)[What is IGMP? | Internet Group Management Protocol](https://www.cloudflare.com/learning/network-layer/what-is-igmp/)[What is IGMP snooping?](https://www.cloudflare.com/learning/network-layer/what-is-igmp-snooping/)[What is IPsec? | How IPsec VPNs work](https://www.cloudflare.com/learning/network-layer/what-is-ipsec/)[What is MPLS (multiprotocol label switching)?](https://www.cloudflare.com/learning/network-layer/what-is-mpls/)[What is MSS (maximum segment size)?](https://www.cloudflare.com/learning/network-layer/what-is-mss/)[What is My Traceroute (MTR)?](https://www.cloudflare.com/learning/network-layer/what-is-mtr/)[What is MTU (maximum transmission unit)?](https://www.cloudflare.com/learning/network-layer/what-is-mtu/)[What is peering?](https://www.cloudflare.com/learning/network-layer/what-is-peering/)[What is software-defined networking (SDN)?](https://www.cloudflare.com/learning/network-layer/what-is-sdn/)[What is the control plane? | Control plane vs. data plane](https://www.cloudflare.com/learning/network-layer/what-is-the-control-plane/)[What is the network layer?](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)[What is tunneling? | Tunneling in networking](https://www.cloudflare.com/learning/network-layer/what-is-tunneling/)[How does the Internet work?](https://www.cloudflare.com/learning/network-layer/how-does-the-internet-work/)[What is routing?](https://www.cloudflare.com/learning/network-layer/what-is-routing/)[What is a LAN?](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define the Internet Protocol (IP) 
  * Explain how IP is used to ensure data arrives in the right place 
  * Explore the differences between TCP/IP and UDP/IP 



Related content  [ What is a protocol? | Network protocol definition ](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/)[ What is a packet? | Network packet definition ](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/)[ What is a router? ](https://www.cloudflare.com/learning/network-layer/what-is-a-router/)[ What is an autonomous system? | What are ASNs? ](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/)[ What is IPsec? | How IPsec VPNs work ](https://www.cloudflare.com/learning/network-layer/what-is-ipsec/)

On this page

  * What is the Internet Protocol?

  * What is a network protocol?

  * What is an IP address? How does IP addressing work?

  * IPv4 vs. IPv6

  * What is an IP packet?

  * How does IP routing work?

  * What is TCP/IP?

  * What is UDP/IP?

  * Do network switches refer to IP addresses?




## What is the Internet Protocol (IP)?

The Internet Protocol (IP) is a protocol, or set of rules, for routing and addressing packets of data so that they can travel across networks and arrive at the correct destination. Data traversing the Internet is divided into smaller pieces, called [packets](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/). IP information is attached to each packet, and this information helps [routers](https://www.cloudflare.com/learning/network-layer/what-is-a-router/) to send packets to the right place. Every device or [domain](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/) that connects to the Internet is assigned an [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/), and as packets are directed to the IP address attached to them, data arrives where it is needed.

Once the packets arrive at their destination, they are handled differently depending on which transport protocol is used in combination with IP. The most common transport protocols are TCP and UDP.

## What is a network protocol?

In networking, a [protocol](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/) is a standardized way of doing certain actions and formatting data so that two or more devices are able to communicate with and understand each other.

To understand why protocols are necessary, consider the process of mailing a letter. On the envelope, addresses are written in the following order: name, street address, city, state, and zip code. If an envelope is dropped into a mailbox with the zip code written first, followed by the street address, followed by the state, and so on, the post office won't deliver it. There is an agreed-upon protocol for writing addresses in order for the postal system to work. In the same way, all IP data packets must present certain information in a certain order, and all IP addresses follow a standardized format.

Resource

Regain control with the Connectivity Cloud

[Learn more →](https://www.cloudflare.com/connectivity-cloud/)Guide

The Zero Trust guide to securing aplication access

[Read the guide →](https://www.cloudflare.com/lp/guide-to-zero-trust-access/)

## What is an IP address? How does IP addressing work?

An IP address is a unique identifier assigned to a device or domain that connects to the Internet. Each IP address is a series of characters, such as '192.168.1.1'. Via [DNS](https://www.cloudflare.com/learning/dns/what-is-dns/) resolvers, which translate human-readable domain names into IP addresses, users are able to access websites without memorizing this complex series of characters. Each IP packet will contain both the IP address of the device or domain sending the packet and the IP address of the intended recipient, much like how both the destination address and the return address are included on a piece of mail.

![IP address gets packets to their destination](https://images.ctfassets.net/slt3lc6tev37/4tzfU9Y5ows0uT3u4GUlWr/9d4eaa83ce372454cc14d5fec83fb5b1/internet_protocol_ip_address_diagram.svg)IP address gets packets to their destination

## IPv4 vs. IPv6

The fourth version of IP (IPv4 for short) was introduced in 1983. However, just as there are only so many possible permutations for automobile license plate numbers and they have to be reformatted periodically, the supply of available IPv4 addresses has become depleted. IPv6 addresses have many more characters and thus more permutations; however, IPv6 is not yet completely adopted, and most domains and devices still have IPv4 addresses. For more on IPv4 and IPv6, see [What is my IP address?](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/)

## What is an IP packet?

IP packets are created by adding an IP header to each packet of data before it is sent on its way. An IP header is just a series of bits (ones and zeros), and it records several pieces of information about the packet, including the sending and receiving IP address. IP headers also report:

  * Header length

  * Packet length

  * [Time to live (TTL)](https://www.cloudflare.com/learning/cdn/glossary/time-to-live-ttl/), or the number of network hops a packet can make before it is discarded

  * Which transport protocol is being used (TCP, UDP, etc.)




In total there are 14 fields for information in IPv4 headers, although one of them is optional.

Sign Up

Globally accelerate your traffic with a single click

[Start for free →](https://www.cloudflare.com/application-services/products/argo-smart-routing/)

## How does IP routing work?

The Internet is made up of interconnected large networks that are each responsible for certain blocks of IP addresses; these large networks are known as [autonomous systems (AS)](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/). A variety of routing protocols, including [BGP](https://www.cloudflare.com/learning/security/glossary/what-is-bgp/), help route packets across ASes based on their destination IP addresses. Routers have routing tables that indicate which ASes the packets should travel through in order to reach the desired destination as quickly as possible. Packets travel from AS to AS until they reach one that claims responsibility for the targeted IP address. That AS then internally routes the packets to the destination.

Protocols attach packet headers at different layers of the OSI model:

![Protocols attach packet headers at different layers of OSI model](https://images.ctfassets.net/slt3lc6tev37/6htPEWbcCRIv5FMhWKYy0m/ef16a86a38a638e8fed01c326f8211f1/protocol_headers.svg)Protocols attach packet headers at different layers of OSI model

Packets can take different routes to the same place if necessary, just as a group of people driving to an agreed-upon destination can take different roads to get there.

## What is TCP/IP?

The Transmission Control Protocol (TCP) is a transport protocol, meaning it dictates the way data is sent and received. A TCP header is included in the data portion of each packet that uses [TCP/IP](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/). Before transmitting data, TCP opens a connection with the recipient. TCP ensures that all packets arrive in order once transmission begins. Via TCP, the recipient will acknowledge receiving each packet that arrives. Missing packets will be sent again if receipt is not acknowledged.

TCP is designed for reliability, not speed. Because TCP has to make sure all packets arrive in order, loading data via TCP/IP can take longer if some packets are missing.

TCP and IP were originally designed to be used together, and these are often referred to as the TCP/IP suite. However, other transport protocols can be used with IP.

## What is UDP/IP?

The User Datagram Protocol, or [UDP](https://www.cloudflare.com/learning/ddos/glossary/user-datagram-protocol-udp/), is another widely used transport protocol. It is faster than TCP, but it is also less reliable. UDP does not make sure all packets are delivered and in order, and it does not establish a connection before beginning or receiving transmissions.

## Do network switches refer to IP addresses?

A network switch is an appliance that forwards data packets within a [local area network (LAN)](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/). Most network switches operate at layer 2, the data link layer, not layer 3, the network layer, and therefore use MAC addresses to forward packets, not IP addresses. To learn more, see [What is a network switch?](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/)
