---
url: https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/
title: What is a protocol? | Network protocol definition
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:48.124949+00:00
---

# What is a protocol? | Network protocol definition

> Source: https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/

[ Learning Center ](https://www.cloudflare.com/learning/) / the network layer

##  What is a protocol? | Network protocol definition 

In networking, a protocol is a standardized set of rules for formatting and processing data. Protocols enable computers to communicate with one another. 

[Learning Center](https://www.cloudflare.com/learning)/the network layer/[What is enterprise networking?](https://www.cloudflare.com/learning/network-layer/enterprise-networking/)[How to migrate from MPLS](https://www.cloudflare.com/learning/network-layer/how-to-migrate-from-mpls/)[How to prepare for network modernization projects](https://www.cloudflare.com/learning/network-layer/how-to-prepare-for-network-modernization-projects/)[What is the Internet Protocol?](https://www.cloudflare.com/learning/network-layer/internet-protocol/)[IPsec VPNs vs. SSL VPNs](https://www.cloudflare.com/learning/network-layer/ipsec-vs-ssl-vpn/)[What is NaaS (network-as-a-service)?](https://www.cloudflare.com/learning/network-layer/network-as-a-service-naas/)[What is network modernization?](https://www.cloudflare.com/learning/network-layer/network-modernization/)[What is network security?](https://www.cloudflare.com/learning/network-layer/network-security/)[SD-WAN vs. MPLS: SD-WAN benefits and drawbacks](https://www.cloudflare.com/learning/network-layer/sd-wan-vs-mpls/)[What is a campus area network (CAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-campus-area-network/)[What is a computer port? | Ports in networking](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/)[What is a metropolitan area network (MAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-metropolitan-area-network/)[What is a network switch? | Switch vs. router](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/)[What is a packet? | Network packet definition](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/)[What is a personal area network (PAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-personal-area-network/)[What is a protocol? | Network protocol definition](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/)[What is a router?](https://www.cloudflare.com/learning/network-layer/what-is-a-router/)[What is a subnet? | How subnetting works](https://www.cloudflare.com/learning/network-layer/what-is-a-subnet/)[What is a WAN? | WAN vs. LAN](https://www.cloudflare.com/learning/network-layer/what-is-a-wan/)[What is an autonomous system? | What are ASNs?](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/)[What is SD-WAN?](https://www.cloudflare.com/learning/network-layer/what-is-an-sd-wan/)[What is branch networking?](https://www.cloudflare.com/learning/network-layer/what-is-branch-networking/)[What is GRE tunneling? | How GRE protocol works](https://www.cloudflare.com/learning/network-layer/what-is-gre-tunneling/)[What is IGMP? | Internet Group Management Protocol](https://www.cloudflare.com/learning/network-layer/what-is-igmp/)[What is IGMP snooping?](https://www.cloudflare.com/learning/network-layer/what-is-igmp-snooping/)[What is IPsec? | How IPsec VPNs work](https://www.cloudflare.com/learning/network-layer/what-is-ipsec/)[What is MPLS (multiprotocol label switching)?](https://www.cloudflare.com/learning/network-layer/what-is-mpls/)[What is MSS (maximum segment size)?](https://www.cloudflare.com/learning/network-layer/what-is-mss/)[What is My Traceroute (MTR)?](https://www.cloudflare.com/learning/network-layer/what-is-mtr/)[What is MTU (maximum transmission unit)?](https://www.cloudflare.com/learning/network-layer/what-is-mtu/)[What is peering?](https://www.cloudflare.com/learning/network-layer/what-is-peering/)[What is software-defined networking (SDN)?](https://www.cloudflare.com/learning/network-layer/what-is-sdn/)[What is the control plane? | Control plane vs. data plane](https://www.cloudflare.com/learning/network-layer/what-is-the-control-plane/)[What is the network layer?](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)[What is tunneling? | Tunneling in networking](https://www.cloudflare.com/learning/network-layer/what-is-tunneling/)[How does the Internet work?](https://www.cloudflare.com/learning/network-layer/how-does-the-internet-work/)[What is routing?](https://www.cloudflare.com/learning/network-layer/what-is-routing/)[What is a LAN?](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define 'protocol' in a networking context 
  * Relate protocols to OSI model layers 
  * Learn about the most commonly used protocols on the Internet 



Related content  [ What is the Internet Protocol? ](https://www.cloudflare.com/learning/network-layer/internet-protocol/)[ What is a packet? | Network packet definition ](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/)[ What is a computer port? | Ports in networking ](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/)[ What is routing? ](https://www.cloudflare.com/learning/network-layer/what-is-routing/)[ What is IPsec? | How IPsec VPNs work ](https://www.cloudflare.com/learning/network-layer/what-is-ipsec/)

On this page

  * What is a network protocol?

  * What are the layers of the OSI model?

  * Which protocols run on the network layer?

  * What other protocols are used on the Internet?

  * What protocols do routers use?

  * How are protocols used in cyber attacks?




## What is a network protocol?

In networking, a protocol is a set of rules for formatting and processing data. Network protocols are like a common language for computers. The computers within a network may use vastly different software and hardware; however, the use of protocols enables them to communicate with each other regardless.

Standardized protocols are like a common language that computers can use, similar to how two people from different parts of the world may not understand each other's native languages, but they can communicate using a shared third language. If one computer uses the [Internet Protocol (IP)](https://www.cloudflare.com/learning/network-layer/internet-protocol/) and a second computer does as well, they will be able to communicate — just as the United Nations relies on its 6 official languages to communicate amongst representatives from all over the globe. But if one computer uses IP and the other does not know this protocol, they will be unable to communicate.

On the Internet, there are different protocols for different types of processes. Protocols are often discussed in terms of which OSI model layer they belong to.

eBook

Strengthen security with a unified platform

[Get the eBook →](https://www.cloudflare.com/lp/cloudflare-strengthens-security/)Whitepaper

Developing a strategy for your network modernization

[Read the whitepaper →](https://www.cloudflare.com/lp/developing-a-strategy-for-network-modernization/)

## What are the layers of the OSI model?

The [Open Systems Interconnection (OSI) model](https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/) is an abstract representation of how the Internet works. It contains 7 layers, with each layer representing a different category of networking functions.

![The OSI Model](https://cloudflare.com/img/learning/ddos/what-is-a-ddos-attack/osi-model-7-layers.svg)The OSI Model

Protocols make these networking functions possible. For instance, the Internet Protocol (IP) is responsible for [routing](https://www.cloudflare.com/learning/network-layer/what-is-routing/) data by indicating where [data packets](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/)* come from and what their destination is. IP makes network-to-network communications possible. Hence, IP is considered a [network layer](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/) (layer 3) protocol.

As another example, the [Transmission Control Protocol (TCP)](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/) ensures that the transportation of packets of data across networks goes smoothly. Therefore, TCP is considered a transport layer (layer 4) protocol.

*_A packet is a small segment of data; all data sent over a network is divided into packets._

Sign Up

Security & speed with any Cloudflare plan

[Start for free →](https://www.cloudflare.com/plans/)

## Which protocols run on the network layer?

As described above, IP is a network layer protocol responsible for routing. But it is not the only network layer protocol.

[IPsec:](https://www.cloudflare.com/learning/network-layer/what-is-ipsec/) Internet Protocol Security (IPsec) sets up encrypted, authenticated IP connections over a [virtual private network (VPN)](https://www.cloudflare.com/learning/access-management/what-is-a-vpn/). Technically IPsec is not a protocol, but rather a collection of protocols that includes the Encapsulating Security Protocol (ESP), Authentication Header (AH), and Security Associations (SA).

[ICMP:](https://www.cloudflare.com/learning/ddos/glossary/internet-control-message-protocol-icmp/) The Internet Control Message Protocol (ICMP) reports errors and provides status updates. For example, if a router is unable to deliver a packet, it will send an ICMP message back to the packet's source.

**IGMP:** The Internet Group Management Protocol (IGMP) sets up one-to-many network connections. IGMP helps set up multicasting, meaning multiple computers can receive data packets directed at one [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/).

## What other protocols are used on the Internet?

Some of the most important protocols to know are:

**TCP:** As described above, TCP is a transport layer protocol that ensures reliable data delivery. TCP is meant to be used with IP, and the two protocols are often referenced together as TCP/IP.

**HTTP:** The [Hypertext Transfer Protocol (HTTP)](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/) is the foundation of the World Wide Web, the Internet that most users interact with. It is used for transferring data between devices. HTTP belongs to the [application layer (layer 7)](https://www.cloudflare.com/learning/ddos/what-is-layer-7/), because it puts data into a format that applications (e.g. a browser) can use directly, without further interpretation. The lower layers of the OSI model are handled by a computer's operating system, not applications.

**HTTPS:** The problem with HTTP is that it is not [encrypted](https://www.cloudflare.com/learning/ssl/what-is-encryption/) — any attacker who intercepts an HTTP message can read it. [HTTPS](https://www.cloudflare.com/learning/ssl/what-is-https/) (HTTP Secure) corrects this by encrypting HTTP messages.

**TLS/SSL:** [Transport Layer Security (TLS)](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/) is the protocol HTTPS uses for encryption. TLS used to be called [Secure Sockets Layer (SSL)](https://www.cloudflare.com/learning/ssl/what-is-ssl/).

**UDP:** The [User Datagram Protocol (UDP)](https://www.cloudflare.com/learning/ddos/glossary/user-datagram-protocol-udp/) is a faster but less reliable alternative to TCP at the transport layer. It is often used in services like [video streaming](https://www.cloudflare.com/products/cloudflare-stream/) and gaming, where fast data delivery is paramount.

## What protocols do routers use?

Network routers use certain protocols to discover the most efficient network paths to other routers. These protocols are not used for transferring user data. Important network routing protocols include:

**BGP:** The [Border Gateway Protocol (BGP)](https://www.cloudflare.com/learning/security/glossary/what-is-bgp/) is an application layer protocol networks use to broadcast which IP addresses they control. This information allows routers to decide which networks data packets should pass through on the way to their destinations.

**EIGRP:** The Enhanced Interior Gateway Routing Protocol (EIGRP) identifies distances between routers. EIGRP automatically updates each router's record of the best routes (called a routing table) and broadcasts those updates to other routers within the network.

**OSPF:** The Open Shortest Path First (OSPF) protocol calculates the most efficient network routes based on a variety of factors, including distance and bandwidth.

**RIP:** The Routing Information Protocol (RIP) is an older routing protocol that identifies distances between routers. RIP is an application layer protocol.

## How are protocols used in cyber attacks?

Just as with any aspect of computing, attackers can exploit the way networking protocols function to compromise or overwhelm systems. Many of these protocols are used in distributed denial-of-service (DDoS) attacks. For example, in a [SYN flood attack](https://www.cloudflare.com/learning/ddos/syn-flood-ddos-attack/), an attacker takes advantage of the way the TCP protocol works. They send SYN packets to repeatedly initiate a [TCP handshake](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/) with a server, until the server is unable to provide service to legitimate users because its resources are tied up by all the phony TCP connections.

Cloudflare offers a number of solutions for stopping these and other cyber attacks. [Cloudflare Magic Transit](https://www.cloudflare.com/magic-transit/) is able to mitigate attacks at layers 3, 4, and 7 of the OSI model. In the example case of a SYN flood attack, Cloudflare handles the TCP handshake process on the server's behalf so that the server's resources never become overwhelmed by open TCP connections.
