---
url: https://www.cloudflare.com/learning/network-layer/what-is-ipsec/
title: What is IPsec? | How IPsec VPNs work
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:04.693318+00:00
---

# What is IPsec? | How IPsec VPNs work

> Source: https://www.cloudflare.com/learning/network-layer/what-is-ipsec/

[ Learning Center ](https://www.cloudflare.com/learning/) / the network layer

##  What is IPsec? | How IPsec VPNs work 

IPsec is a group of networking protocols used for setting up secure encrypted connections, such as VPNs, across publicly shared networks. 

[Learning Center](https://www.cloudflare.com/learning)/the network layer/[What is enterprise networking?](https://www.cloudflare.com/learning/network-layer/enterprise-networking/)[How to migrate from MPLS](https://www.cloudflare.com/learning/network-layer/how-to-migrate-from-mpls/)[How to prepare for network modernization projects](https://www.cloudflare.com/learning/network-layer/how-to-prepare-for-network-modernization-projects/)[What is the Internet Protocol?](https://www.cloudflare.com/learning/network-layer/internet-protocol/)[IPsec VPNs vs. SSL VPNs](https://www.cloudflare.com/learning/network-layer/ipsec-vs-ssl-vpn/)[What is NaaS (network-as-a-service)?](https://www.cloudflare.com/learning/network-layer/network-as-a-service-naas/)[What is network modernization?](https://www.cloudflare.com/learning/network-layer/network-modernization/)[What is network security?](https://www.cloudflare.com/learning/network-layer/network-security/)[SD-WAN vs. MPLS: SD-WAN benefits and drawbacks](https://www.cloudflare.com/learning/network-layer/sd-wan-vs-mpls/)[What is a campus area network (CAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-campus-area-network/)[What is a computer port? | Ports in networking](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/)[What is a metropolitan area network (MAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-metropolitan-area-network/)[What is a network switch? | Switch vs. router](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/)[What is a packet? | Network packet definition](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/)[What is a personal area network (PAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-personal-area-network/)[What is a protocol? | Network protocol definition](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/)[What is a router?](https://www.cloudflare.com/learning/network-layer/what-is-a-router/)[What is a subnet? | How subnetting works](https://www.cloudflare.com/learning/network-layer/what-is-a-subnet/)[What is a WAN? | WAN vs. LAN](https://www.cloudflare.com/learning/network-layer/what-is-a-wan/)[What is an autonomous system? | What are ASNs?](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/)[What is SD-WAN?](https://www.cloudflare.com/learning/network-layer/what-is-an-sd-wan/)[What is branch networking?](https://www.cloudflare.com/learning/network-layer/what-is-branch-networking/)[What is GRE tunneling? | How GRE protocol works](https://www.cloudflare.com/learning/network-layer/what-is-gre-tunneling/)[What is IGMP? | Internet Group Management Protocol](https://www.cloudflare.com/learning/network-layer/what-is-igmp/)[What is IGMP snooping?](https://www.cloudflare.com/learning/network-layer/what-is-igmp-snooping/)[What is IPsec? | How IPsec VPNs work](https://www.cloudflare.com/learning/network-layer/what-is-ipsec/)[What is MPLS (multiprotocol label switching)?](https://www.cloudflare.com/learning/network-layer/what-is-mpls/)[What is MSS (maximum segment size)?](https://www.cloudflare.com/learning/network-layer/what-is-mss/)[What is My Traceroute (MTR)?](https://www.cloudflare.com/learning/network-layer/what-is-mtr/)[What is MTU (maximum transmission unit)?](https://www.cloudflare.com/learning/network-layer/what-is-mtu/)[What is peering?](https://www.cloudflare.com/learning/network-layer/what-is-peering/)[What is software-defined networking (SDN)?](https://www.cloudflare.com/learning/network-layer/what-is-sdn/)[What is the control plane? | Control plane vs. data plane](https://www.cloudflare.com/learning/network-layer/what-is-the-control-plane/)[What is the network layer?](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)[What is tunneling? | Tunneling in networking](https://www.cloudflare.com/learning/network-layer/what-is-tunneling/)[How does the Internet work?](https://www.cloudflare.com/learning/network-layer/how-does-the-internet-work/)[What is routing?](https://www.cloudflare.com/learning/network-layer/what-is-routing/)[What is a LAN?](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/)

######  Learning objectives 

After reading this article you will be able to: 

  * Learn about the IPsec protocol suite 
  * Understand how IPsec VPNs work 
  * Compare IPsec tunnel mode and IPsec transport mode 



Related content  [ What is the network layer? ](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)[ What is MSS (maximum segment size)? ](https://www.cloudflare.com/learning/network-layer/what-is-mss/)[ What is MTU (maximum transmission unit)? ](https://www.cloudflare.com/learning/network-layer/what-is-mtu/)[ What is a WAN? | WAN vs. LAN ](https://www.cloudflare.com/learning/network-layer/what-is-a-wan/)[ What is a LAN? ](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/)

On this page

  * What is IPsec?

  * Why is IPsec important?

  * What is a VPN? What is an IPsec VPN?

  * How do users connect to an IPsec VPN?

  * How does IPsec work?

  * What protocols are used in IPsec?

  * What is the difference between IPsec tunnel mode and IPsec transport mode?

  * What port does IPsec use?

  * How does IPsec impact MSS and MTU?

  * Does Cloudflare support IPsec?




## What is IPsec?

IPsec is a group of protocols for securing connections between devices. IPsec helps keep data sent over public networks secure. It is often used to set up [VPNs](https://www.cloudflare.com/learning/access-management/what-is-a-vpn/), and it works by encrypting [IP](https://www.cloudflare.com/learning/network-layer/internet-protocol/) packets, along with authenticating the source where the packets come from.

Within the term "IPsec," "IP" stands for "Internet Protocol" and "sec" for "secure." The Internet Protocol is the main routing protocol used on the Internet; it designates where data will go using [IP addresses](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/). IPsec is secure because it adds encryption* and authentication to this process.

*_Encryption is the process of concealing information by mathematically altering data so that it appears random. In simpler terms, encryption is the use of a "secret code" that only authorized parties can interpret._

Whitepaper

How to break free from network hardware

[Get the report →](https://www.cloudflare.com/lp/network-hardware/)Guide

The Zero Trust guide to securing aplication access

[Read the guide →](https://www.cloudflare.com/lp/guide-to-zero-trust-access/)

## Why is IPsec important?

Security protocols like IPsec are necessary because networking methods are not encrypted by default.

When sending mail through a postal service, a person typically would not write their message on the outside of the envelope. Instead, they enclose their message inside the envelope so that no one who handles the mail between sender and recipient can read their message. However, networking protocol suites like TCP/IP are only concerned with connection and delivery, and messages sent are not concealed. Anyone in the middle can read them. IPsec, and other protocols that encrypt data, essentially put an envelope around data as it traverses networks, keeping it secure.

## What is a VPN? What is an IPsec VPN?

A virtual private network (VPN) is an encrypted connection between two or more computers. VPN connections take place over public networks, but the data exchanged over the VPN is still private because it is encrypted.

VPNs make it possible to securely access and exchange confidential data over shared [network infrastructure](https://www.cloudflare.com/the-net/network-infrastructure/), such as the public Internet. For instance, when employees are [working remotely](https://www.cloudflare.com/learning/access-management/remote-workforce-security/) instead of in the office, they often use VPNs to access corporate files and applications.

Many VPNs use the IPsec protocol suite to establish and run these encrypted connections. However, not all VPNs use IPsec. Another protocol for VPNs is [SSL](https://www.cloudflare.com/learning/ssl/what-is-ssl/)/[TLS](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/), which operates at a different layer in the [OSI model](https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/) than IPsec. (The OSI model is an abstract representation of the processes that make the [Internet](https://www.cloudflare.com/learning/network-layer/how-does-the-internet-work/) work.)

## How do users connect to an IPsec VPN?

Users can access an IPsec VPN by logging into a VPN application, or "client." This typically requires the user to have installed the application on their device.

VPN logins are usually password-based. While data sent over a VPN is encrypted, if user passwords are compromised, attackers can log into the VPN and steal this encrypted data. Using [two-factor authentication](https://www.cloudflare.com/learning/access-management/what-is-two-factor-authentication/) (2FA) can strengthen IPsec VPN security, since stealing a password alone will no longer give an attacker access.

Sign Up

Security & speed with any Cloudflare plan

[Start for free →](https://www.cloudflare.com/plans/)

## How does IPsec work?

IPsec connections include the following steps:

**Key exchange:** [Keys](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/) are necessary for encryption; a key is a string of random characters that can be used to "lock" (encrypt) and "unlock" (decrypt) messages. IPsec sets up keys with a key exchange between the connected devices, so that each device can decrypt the other device's messages.

**Packet headers and trailers:** All data that is sent over a network is broken down into smaller pieces called packets. Packets contain both a payload, or the actual data being sent, and headers, or information about that data so that computers receiving the packets know what to do with them. IPsec adds several headers to data packets containing authentication and encryption information. IPsec also adds trailers, which go after each packet's payload instead of before.

**Authentication:** IPsec provides authentication for each packet, like a stamp of authenticity on a collectible item. This ensures that packets are from a trusted source and not an attacker.

**Encryption:** IPsec encrypts the payloads within each packet and each packet's IP header (unless transport mode is used instead of tunnel mode — see below). This keeps data sent over IPsec secure and private.

**Transmission:** Encrypted IPsec packets travel across one or more networks to their destination using a transport protocol. At this stage, IPsec traffic differs from regular IP traffic in that it most often uses [UDP](https://www.cloudflare.com/learning/ddos/glossary/user-datagram-protocol-udp/) as its transport protocol, rather than [TCP](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/). TCP, the Transmission Control Protocol, sets up dedicated connections between devices and ensures that all packets arrive. UDP, the User Datagram Protocol, does not set up these dedicated connections. IPsec uses UDP because this allows IPsec packets to get through [firewalls](https://www.cloudflare.com/learning/security/what-is-a-firewall/).

**Decryption:** At the other end of the communication, the packets are decrypted, and applications (e.g. a browser) can now use the delivered data.

## What protocols are used in IPsec?

In [networking](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/), a protocol is a specified way of formatting data so that any networked computer can interpret the data. IPsec is not one protocol, but a suite of protocols. The following protocols make up the IPsec suite:

**Authentication Header (AH):** The AH protocol ensures that data packets are from a trusted source and that the data has not been tampered with, like a tamper-proof seal on a consumer product. These headers do not provide any encryption; they do not help conceal the data from attackers.

**Encapsulating Security Protocol (ESP):** ESP encrypts the IP header and the payload for each packet — unless transport mode is used, in which case it only encrypts the payload. ESP adds its own header and a trailer to each data packet.

**Security Association (SA):** SA refers to a number of protocols used for negotiating encryption keys and algorithms. One of the most common SA protocols is Internet Key Exchange (IKE).

Finally, while the **Internet Protocol (IP)** is not part of the IPsec suite, IPsec runs directly on top of IP.

## What is the difference between IPsec tunnel mode and IPsec transport mode?

IPsec tunnel mode is used between two dedicated routers, with each router acting as one end of a virtual "tunnel" through a public network. In IPsec tunnel mode, the original IP header containing the final destination of the packet is encrypted, in addition to the packet payload. To tell intermediary routers where to forward the packets, IPsec adds a new IP header. At each end of the tunnel, the routers decrypt the IP headers to deliver the packets to their destinations.

In transport mode, the payload of each packet is encrypted, but the original IP header is not. Intermediary routers are thus able to view the final destination of each packet — unless a separate tunneling protocol (such as [GRE](https://www.cloudflare.com/learning/network-layer/what-is-gre-tunneling/)) is used.

## What port does IPsec use?

A network [port](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/) is the virtual location where data goes in a computer. Ports are how computers keep track of different processes and connections; if data goes to a certain port, the computer's operating system knows which process it belongs to. IPsec usually uses port 500.

## How does IPsec impact MSS and MTU?

[MSS](https://www.cloudflare.com/learning/network-layer/what-is-mss/) and [MTU](https://www.cloudflare.com/learning/network-layer/what-is-mtu/) are two measurements of packet size. Packets can only reach a certain size (measured in bytes) before computers, routers, and [switches](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/) cannot handle them. MSS measures the size of each packet's payload, while MTU measures the entire packet, including headers. Packets that exceed a network's MTU may be fragmented, meaning broken up into smaller packets and then reassembled. Packets that exceed the MSS are simply dropped.

IPsec protocols add several headers and trailers to packets, all of which take up several bytes. For networks that use IPsec, either the MSS and MTU have to be adjusted accordingly, or packets will be fragmented and slightly delayed. Usually, the MTU for a network is 1,500 bytes. A normal IP header is 20 bytes long, and a TCP header is also 20 bytes long, meaning each packet can contain 1,460 bytes of payload. However, IPsec adds an Authentication Header, an ESP header, and associated trailers. These add 50-60 bytes to a packet, or more.

Learn more about MTU and MSS in ["What is MTU?"](https://www.cloudflare.com/learning/network-layer/what-is-mtu/)

## Does Cloudflare support IPsec?

Cloudflare supports IPsec as an on-ramp for our [Secure Access Service Edge (SASE)](https://www.cloudflare.com/learning/access-management/what-is-sase/) solution, [Cloudflare One](https://www.cloudflare.com/cloudflare-one/).

To secure traffic, IPsec requires an SA to be set up between two points, creating a tunnel for the traffic to travel through. Depending on the implementation model, this can introduce some challenges. For example, in a mesh model, all nodes (or locations) are connected to each other by dedicated tunnels. However, this requires creating and managing several IPsec tunnels, which is difficult to scale.

Cloudflare, however, uses the Anycast IPsec model. (An [Anycast network](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/) is one that routes incoming requests to a variety of nodes.) With Anycast IPsec, users only need to set up one IPsec tunnel to Cloudflare to gain connectivity to the over 250+ locations in our global network.

To make Anycast IPsec possible, Cloudflare duplicates and distributes SAs across the servers in the Cloudflare edge network. This means that the entire Cloudflare network functions as a single IPsec tunnel to your network.

Learn more about [Anycast IPsec and Cloudflare One](https://blog.cloudflare.com/anycast-ipsec/).
