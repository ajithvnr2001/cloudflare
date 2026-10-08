---
url: https://www.cloudflare.com/learning/network-layer/what-is-tunneling/
title: What is tunneling? | Tunneling in networking
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:16.019729+00:00
---

# What is tunneling? | Tunneling in networking

> Source: https://www.cloudflare.com/learning/network-layer/what-is-tunneling/

[ Learning Center ](https://www.cloudflare.com/learning/) / the network layer

##  What is tunneling? | Tunneling in networking 

Tunneling is a way to move packets from one network to another. Tunneling works via encapsulation: wrapping a packet inside another packet. 

[Learning Center](https://www.cloudflare.com/learning)/the network layer/[What is enterprise networking?](https://www.cloudflare.com/learning/network-layer/enterprise-networking/)[How to migrate from MPLS](https://www.cloudflare.com/learning/network-layer/how-to-migrate-from-mpls/)[How to prepare for network modernization projects](https://www.cloudflare.com/learning/network-layer/how-to-prepare-for-network-modernization-projects/)[What is the Internet Protocol?](https://www.cloudflare.com/learning/network-layer/internet-protocol/)[IPsec VPNs vs. SSL VPNs](https://www.cloudflare.com/learning/network-layer/ipsec-vs-ssl-vpn/)[What is NaaS (network-as-a-service)?](https://www.cloudflare.com/learning/network-layer/network-as-a-service-naas/)[What is network modernization?](https://www.cloudflare.com/learning/network-layer/network-modernization/)[What is network security?](https://www.cloudflare.com/learning/network-layer/network-security/)[SD-WAN vs. MPLS: SD-WAN benefits and drawbacks](https://www.cloudflare.com/learning/network-layer/sd-wan-vs-mpls/)[What is a campus area network (CAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-campus-area-network/)[What is a computer port? | Ports in networking](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/)[What is a metropolitan area network (MAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-metropolitan-area-network/)[What is a network switch? | Switch vs. router](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/)[What is a packet? | Network packet definition](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/)[What is a personal area network (PAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-personal-area-network/)[What is a protocol? | Network protocol definition](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/)[What is a router?](https://www.cloudflare.com/learning/network-layer/what-is-a-router/)[What is a subnet? | How subnetting works](https://www.cloudflare.com/learning/network-layer/what-is-a-subnet/)[What is a WAN? | WAN vs. LAN](https://www.cloudflare.com/learning/network-layer/what-is-a-wan/)[What is an autonomous system? | What are ASNs?](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/)[What is SD-WAN?](https://www.cloudflare.com/learning/network-layer/what-is-an-sd-wan/)[What is branch networking?](https://www.cloudflare.com/learning/network-layer/what-is-branch-networking/)[What is GRE tunneling? | How GRE protocol works](https://www.cloudflare.com/learning/network-layer/what-is-gre-tunneling/)[What is IGMP? | Internet Group Management Protocol](https://www.cloudflare.com/learning/network-layer/what-is-igmp/)[What is IGMP snooping?](https://www.cloudflare.com/learning/network-layer/what-is-igmp-snooping/)[What is IPsec? | How IPsec VPNs work](https://www.cloudflare.com/learning/network-layer/what-is-ipsec/)[What is MPLS (multiprotocol label switching)?](https://www.cloudflare.com/learning/network-layer/what-is-mpls/)[What is MSS (maximum segment size)?](https://www.cloudflare.com/learning/network-layer/what-is-mss/)[What is My Traceroute (MTR)?](https://www.cloudflare.com/learning/network-layer/what-is-mtr/)[What is MTU (maximum transmission unit)?](https://www.cloudflare.com/learning/network-layer/what-is-mtu/)[What is peering?](https://www.cloudflare.com/learning/network-layer/what-is-peering/)[What is software-defined networking (SDN)?](https://www.cloudflare.com/learning/network-layer/what-is-sdn/)[What is the control plane? | Control plane vs. data plane](https://www.cloudflare.com/learning/network-layer/what-is-the-control-plane/)[What is the network layer?](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)[What is tunneling? | Tunneling in networking](https://www.cloudflare.com/learning/network-layer/what-is-tunneling/)[How does the Internet work?](https://www.cloudflare.com/learning/network-layer/how-does-the-internet-work/)[What is routing?](https://www.cloudflare.com/learning/network-layer/what-is-routing/)[What is a LAN?](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define tunneling 
  * Learn how packet encapsulation works 
  * Explore the uses for network tunnels 



Related content  [ What is the network layer? ](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)[ What is a protocol? | Network protocol definition ](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/)[ What is the Internet Protocol? ](https://www.cloudflare.com/learning/network-layer/internet-protocol/)[ What is routing? ](https://www.cloudflare.com/learning/network-layer/what-is-routing/)[ What is a network switch? | Switch vs. router ](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/)

On this page

  * What is tunneling?

  * How does packet encapsulation work?

  * Why is encapsulation useful?

  * What is a VPN tunnel?

  * What is split tunneling?

  * What is GRE tunneling?

  * What is IP-in-IP?

  * What is SSH tunneling?

  * What are some other tunneling protocols?

  * How does Cloudflare use tunneling?




## What is tunneling?

In the physical world, tunneling is a way to cross terrain or boundaries that could not normally be crossed. Similarly, in networking, tunnels are a method for transporting data across a network using [protocols](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/) that are not supported by that network. Tunneling works by encapsulating packets: wrapping packets inside of other [packets](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/). (Packets are small pieces of data that can be re-assembled at their destination into a larger file.)

Tunneling is often used in [virtual private networks (VPNs)](https://www.cloudflare.com/learning/access-management/what-is-a-vpn/). It can also set up efficient and secure connections between networks, enable the usage of unsupported network protocols, and in some cases allow users to bypass [firewalls](https://www.cloudflare.com/learning/security/what-is-a-firewall/).

## How does packet encapsulation work?

Data traveling over a network is divided into packets. A typical packet has two parts: the header, which indicates the packet's destination and which protocol it uses, and the payload, which is the packet's actual contents.

An encapsulated packet is essentially a packet inside another packet. In an encapsulated packet, the header and payload of the first packet goes inside the payload section of the surrounding packet. The original packet itself becomes the payload.

## Why is encapsulation useful?

All packets use networking protocols — standardized ways of formatting data — to get to their destinations. However, not all networks support all protocols. Imagine a company wants to set up a [wide area network (WAN)](https://www.cloudflare.com/learning/network-layer/what-is-a-wan/) connecting Office A and Office B. The company uses the IPv6 protocol, which is the latest version of the [Internet Protocol (IP)](https://www.cloudflare.com/learning/network-layer/internet-protocol/), but there is a network between Office A and Office B that only supports IPv4. By encapsulating their IPv6 packets inside IPv4 packets, the company can continue to use IPv6 while still sending data directly between the offices.

Encapsulation is also useful for encrypted network connections. [Encryption](https://www.cloudflare.com/learning/ssl/what-is-encryption/) is the process of scrambling data in such a way that it can only be unscrambled using a secret [encryption key](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/); the process of undoing encryption is called _decryption_. If a packet is completely encrypted, including the header, then network routers will not be able to forward the packet to its destination since they do not have the key and cannot see its header. By wrapping the encrypted packet inside another unencrypted packet, the packet can travel across networks like normal.

## What is a VPN tunnel?

A VPN is a secure, encrypted connection over a publicly shared network. Tunneling is the process by which VPN packets reach their intended destination, which is typically a private network.

Many VPNs use the [IPsec](https://www.cloudflare.com/learning/network-layer/what-is-ipsec/) protocol suite. IPsec is a group of protocols that run directly on top of IP at the [network layer](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/). Network traffic in an IPsec tunnel is fully encrypted, but it is decrypted once it reaches either the network or the user device. (IPsec also has a mode called "transport mode" that does not create a tunnel.)

Another protocol in common use for VPNs is [Transport Layer Security (TLS)](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/). This protocol operates at either layer 6 or layer 7 of the OSI model depending on how the model is interpreted. TLS is sometimes called SSL (Secure Sockets Layer), although SSL refers to an older protocol that is no longer in use.

## What is split tunneling?

Usually, when a user connects their device to a VPN, all their network traffic goes through the VPN tunnel. Split tunneling allows some traffic to go outside of the VPN tunnel. In essence, split tunneling lets user devices connect to two networks simultaneously: one public and one private.

## What is GRE tunneling?

Generic Routing Encapsulation (GRE) is one of several tunneling protocols. GRE encapsulates data packets that use one routing protocol inside the packets of another protocol. GRE is one way to set up a direct point-to-point connection across a network, for the purpose of simplifying connections between separate networks.

GRE adds two headers to each packet: the GRE header and an IP header. The GRE header indicates the protocol type used by the encapsulated packet. The IP header encapsulates the original packet's IP header and payload. Only the routers at each end of the GRE tunnel will reference the original, non-GRE IP header.

## What is IP-in-IP?

IP-in-IP is a tunneling protocol for encapsulating IP packets inside other IP packets. IP-in-IP does not encrypt packets and is not used for VPNs. Its main use is setting up network routes that would not normally be available.

## What is SSH tunneling?

The Secure Shell (SSH) protocol sets up encrypted connections between client and server, and can also be used to set up a secure tunnel. SSH operates at layer 7 of the OSI model, the application layer. By contrast, IPsec, IP-in-IP, and GRE operate at the network layer.

## What are some other tunneling protocols?

In addition to GRE, IPsec, IP-in-IP, and SSH, other tunneling protocols include:

  * Point-to-Point Tunneling Protocol (PPTP)

  * Secure Socket Tunneling Protocol (SSTP)

  * Layer 2 Tunneling Protocol (L2TP)

  * Virtual Extensible [Local Area Network](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/) (VXLAN)




## How does Cloudflare use tunneling?

[Cloudflare Magic Transit](https://www.cloudflare.com/magic-transit/) protects on-premise, [cloud](https://www.cloudflare.com/learning/cloud/what-is-the-cloud/), and [hybrid](https://www.cloudflare.com/learning/cloud/what-is-hybrid-cloud/) network infrastructure from [DDoS attacks](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/) and other threats. In order for Magic Transit to work, the Cloudflare network has to be securely connected to the customer's internal network. Cloudflare uses GRE tunneling to form these connections. With GRE tunneling, Magic Transit is able to connect directly to Cloudflare customers' networks securely over the public Internet.
