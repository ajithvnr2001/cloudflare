---
url: https://www.cloudflare.com/learning/network-layer/what-is-a-packet/
title: What is a packet? | Network packet definition
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:47.511852+00:00
---

# What is a packet? | Network packet definition

> Source: https://www.cloudflare.com/learning/network-layer/what-is-a-packet/

[ Learning Center ](https://www.cloudflare.com/learning/) / the network layer

##  What is a packet? | Network packet definition 

Any data sent over the Internet is divided into smaller segments called packets. 

[Learning Center](https://www.cloudflare.com/learning)/the network layer/[What is enterprise networking?](https://www.cloudflare.com/learning/network-layer/enterprise-networking/)[How to migrate from MPLS](https://www.cloudflare.com/learning/network-layer/how-to-migrate-from-mpls/)[How to prepare for network modernization projects](https://www.cloudflare.com/learning/network-layer/how-to-prepare-for-network-modernization-projects/)[What is the Internet Protocol?](https://www.cloudflare.com/learning/network-layer/internet-protocol/)[IPsec VPNs vs. SSL VPNs](https://www.cloudflare.com/learning/network-layer/ipsec-vs-ssl-vpn/)[What is NaaS (network-as-a-service)?](https://www.cloudflare.com/learning/network-layer/network-as-a-service-naas/)[What is network modernization?](https://www.cloudflare.com/learning/network-layer/network-modernization/)[What is network security?](https://www.cloudflare.com/learning/network-layer/network-security/)[SD-WAN vs. MPLS: SD-WAN benefits and drawbacks](https://www.cloudflare.com/learning/network-layer/sd-wan-vs-mpls/)[What is a campus area network (CAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-campus-area-network/)[What is a computer port? | Ports in networking](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/)[What is a metropolitan area network (MAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-metropolitan-area-network/)[What is a network switch? | Switch vs. router](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/)[What is a packet? | Network packet definition](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/)[What is a personal area network (PAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-personal-area-network/)[What is a protocol? | Network protocol definition](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/)[What is a router?](https://www.cloudflare.com/learning/network-layer/what-is-a-router/)[What is a subnet? | How subnetting works](https://www.cloudflare.com/learning/network-layer/what-is-a-subnet/)[What is a WAN? | WAN vs. LAN](https://www.cloudflare.com/learning/network-layer/what-is-a-wan/)[What is an autonomous system? | What are ASNs?](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/)[What is SD-WAN?](https://www.cloudflare.com/learning/network-layer/what-is-an-sd-wan/)[What is branch networking?](https://www.cloudflare.com/learning/network-layer/what-is-branch-networking/)[What is GRE tunneling? | How GRE protocol works](https://www.cloudflare.com/learning/network-layer/what-is-gre-tunneling/)[What is IGMP? | Internet Group Management Protocol](https://www.cloudflare.com/learning/network-layer/what-is-igmp/)[What is IGMP snooping?](https://www.cloudflare.com/learning/network-layer/what-is-igmp-snooping/)[What is IPsec? | How IPsec VPNs work](https://www.cloudflare.com/learning/network-layer/what-is-ipsec/)[What is MPLS (multiprotocol label switching)?](https://www.cloudflare.com/learning/network-layer/what-is-mpls/)[What is MSS (maximum segment size)?](https://www.cloudflare.com/learning/network-layer/what-is-mss/)[What is My Traceroute (MTR)?](https://www.cloudflare.com/learning/network-layer/what-is-mtr/)[What is MTU (maximum transmission unit)?](https://www.cloudflare.com/learning/network-layer/what-is-mtu/)[What is peering?](https://www.cloudflare.com/learning/network-layer/what-is-peering/)[What is software-defined networking (SDN)?](https://www.cloudflare.com/learning/network-layer/what-is-sdn/)[What is the control plane? | Control plane vs. data plane](https://www.cloudflare.com/learning/network-layer/what-is-the-control-plane/)[What is the network layer?](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)[What is tunneling? | Tunneling in networking](https://www.cloudflare.com/learning/network-layer/what-is-tunneling/)[How does the Internet work?](https://www.cloudflare.com/learning/network-layer/how-does-the-internet-work/)[What is routing?](https://www.cloudflare.com/learning/network-layer/what-is-routing/)[What is a LAN?](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/)

######  Learning objectives 

After reading this article you will be able to: 

  * Learn how network packets work 
  * Understand how packet switching works 
  * Define packet headers and trailers 



Related content  [ How does the Internet work? ](https://www.cloudflare.com/learning/network-layer/how-does-the-internet-work/)[ What is the network layer? ](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)[ What is the Internet Protocol? ](https://www.cloudflare.com/learning/network-layer/internet-protocol/)[ What is a LAN? ](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/)[ What is a WAN? | WAN vs. LAN ](https://www.cloudflare.com/learning/network-layer/what-is-a-wan/)

On this page

  * What is a packet?

  * Why use packets?

  * What is a packet header?

  * Where do packet headers come from?

  * What are packet trailers and footers?

  * What is an IP packet?

    * Packets vs. datagrams

  * What is network traffic? What is malicious network traffic?




## What is a packet?

In [networking](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/), a packet is a small segment of a larger message. Data sent over computer networks*, such as the [Internet](https://www.cloudflare.com/learning/network-layer/how-does-the-internet-work/), is divided into packets. These packets are then recombined by the computer or device that receives them.

Suppose Alice is writing a letter to Bob, but Bob's mail slot is only wide enough to accept envelopes the size of a small index card. Instead of writing her letter on normal paper and then trying to stuff it through the mail slot, Alice divides her letter into much shorter sections, each a few words long, and writes these sections out on index cards. She delivers the group of cards to Bob, who puts them in order to read the whole message.

This is similar to how packets work on the Internet. Suppose a user needs to load an image. The image file does not go from a [web server](https://www.cloudflare.com/learning/cdn/glossary/origin-server/) to the user's computer in one piece. Instead, it is broken down into packets of data, sent over the wires, cables, and radio waves of the Internet, and then reassembled by the user's computer into the original photo.

*_A network is a group of two or more connected computers. The Internet is a network of networks — multiple networks around the world that are all interconnected with each other._

## Why use packets?

Theoretically, it could be possible to send files and data over the Internet without chopping them down into small packets of information. One computer could send data to another computer in the form of a long unbroken line of bits (small units of information, communicated as pulses of electricity that computers can interpret).

However, such an approach quickly becomes impractical when more than two computers are involved. While the long line of bits passed over the wires between the two computers, no third computer could use those same wires to send information — it would have to wait its turn.

In contrast to this approach, the Internet is a "packet switching" network. Packet switching refers to the ability of networking equipment to process packets independently from each other. It also means that packets can take different network paths to the same destination, so long as they all arrive at the destination. (In certain protocols, packets do need to arrive at their final destinations in the correct order, even if each packet took a different route to get there.)

Because of packet switching, packets from multiple computers can travel over the same wires in basically any order. This enables multiple connections to take place over the same networking equipment at the same time. As a result, billions of devices can exchange data on the Internet at the same time, instead of just a handful.

## What is a packet header?

A packet header is a "label" of sorts, which provides information about the packet’s contents, origin, and destination.

When Alice sends her series of index cards to Bob, the words on those cards alone will not give Bob enough context to read the letter correctly. Alice needs to indicate the order that the index cards go in so that Bob does not read them out of order. She also should indicate that each one is from her, in case Bob receives messages from other people while she is delivering hers. So Alice adds this information to the top of each index card, above the actual words of her message. On the first card she writes "Letter from Alice, 1 of 20," on the second she writes "Letter from Alice, 2 of 20," and so on.

Alice has created a miniature header for her cards so that Bob does not lose them or mix them up. Similarly, all network packets include a header so that the device that receives them knows where the packets come from, what they are for, and how to process them.

Packets consist of two portions: the header and the payload. The header contains information about the packet, such as its origin and destination [IP addresses](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/) (an IP address is like a computer's mailing address). The payload is the actual data. Referring back to the photo example, the thousands of packets that make up the image each have a payload, and the payload carries a little piece of the image.

## Where do packet headers come from?

In practice, packets actually have more than one header, and each header is used by a different part of the networking process. Packet headers are attached by certain types of networking protocols.

A protocol is a standardized way of formatting data so that any computer can interpret the data. Many different protocols make the Internet work. Some of these protocols add headers to packets with information associated with that protocol. At minimum, most packets that traverse the Internet will include a [Transmission Control Protocol (TCP)](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/) header and an [Internet Protocol (IP)](https://www.cloudflare.com/learning/network-layer/internet-protocol/) header.

## What are packet trailers and footers?

Packet headers go at the front of each packet. Routers, [switches](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/), computers, and anything else that processes or receives a packet will see the header first. A packet can also have trailers and footers attached at the end. Like headers, these contain additional information about the packet.

Only certain network protocols attach trailers or footers to packets; most only attach headers. ESP (part of the [IPsec](https://www.cloudflare.com/learning/network-layer/what-is-ipsec/) suite) is one example of a network layer protocol that attaches trailers to packets.

## What is an IP packet?

IP (Internet Protocol) is a network layer protocol that has to do with routing. It is used to make sure packets arrive at the correct destination.

Packets are sometimes defined by the protocol they are using. A packet with an IP header can be referred to as an "IP packet." An IP header contains important information about where a packet is from (its source IP address), where it is going (destination IP address), how large the packet is, and how long network routers should continue to forward the packet before dropping it. It may also indicate whether or not the packet can be fragmented, and include information about reassembling fragmented packets.

#### Packets vs. datagrams

"Datagram" is a segment of data sent over a packet-switched network. A datagram contains enough information to be routed from its source to its destination. By this definition, an IP packet is one example of a datagram. Essentially, datagram is an alternative term for "packet."

## What is network traffic? What is malicious network traffic?

Network traffic is a term that refers to the packets that pass through a network, in the same way that automobile traffic refers to the cars and trucks that travel on roads.

However, not all packets are good or useful, and not all network traffic is safe. Attackers can generate malicious network traffic — data packets designed to compromise or overwhelm a network. This can take the form of a [distributed denial-of-service (DDoS) attack](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/), a [vulnerability exploitation](https://www.cloudflare.com/learning/security/what-is-web-application-security/), or several other forms of cyber attack.

Cloudflare offers several products that protect against malicious network traffic. [Cloudflare Magic Transit](https://www.cloudflare.com/magic-transit/), for instance, protects company networks from [DDoS attacks at the network layer](https://www.cloudflare.com/learning/ddos/layer-3-ddos-attacks/) by extending the power of the Cloudflare global cloud network to on-premise, [hybrid](https://www.cloudflare.com/learning/cloud/what-is-hybrid-cloud/), and [cloud](https://www.cloudflare.com/learning/cloud/what-is-the-cloud/) infrastructure.
