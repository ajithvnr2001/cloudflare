---
url: https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/
title: What is the network layer? | Learning Center
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:15.378423+00:00
---

# What is the network layer? | Learning Center

> Source: https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/

[ Learning Center ](https://www.cloudflare.com/learning/) / the network layer

##  What is the network layer? 

The network layer is responsible for routing packets of data across networks, enabling communication between devices on different networks. 

[Learning Center](https://www.cloudflare.com/learning)/the network layer/[What is enterprise networking?](https://www.cloudflare.com/learning/network-layer/enterprise-networking/)[How to migrate from MPLS](https://www.cloudflare.com/learning/network-layer/how-to-migrate-from-mpls/)[How to prepare for network modernization projects](https://www.cloudflare.com/learning/network-layer/how-to-prepare-for-network-modernization-projects/)[What is the Internet Protocol?](https://www.cloudflare.com/learning/network-layer/internet-protocol/)[IPsec VPNs vs. SSL VPNs](https://www.cloudflare.com/learning/network-layer/ipsec-vs-ssl-vpn/)[What is NaaS (network-as-a-service)?](https://www.cloudflare.com/learning/network-layer/network-as-a-service-naas/)[What is network modernization?](https://www.cloudflare.com/learning/network-layer/network-modernization/)[What is network security?](https://www.cloudflare.com/learning/network-layer/network-security/)[SD-WAN vs. MPLS: SD-WAN benefits and drawbacks](https://www.cloudflare.com/learning/network-layer/sd-wan-vs-mpls/)[What is a campus area network (CAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-campus-area-network/)[What is a computer port? | Ports in networking](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/)[What is a metropolitan area network (MAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-metropolitan-area-network/)[What is a network switch? | Switch vs. router](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/)[What is a packet? | Network packet definition](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/)[What is a personal area network (PAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-personal-area-network/)[What is a protocol? | Network protocol definition](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/)[What is a router?](https://www.cloudflare.com/learning/network-layer/what-is-a-router/)[What is a subnet? | How subnetting works](https://www.cloudflare.com/learning/network-layer/what-is-a-subnet/)[What is a WAN? | WAN vs. LAN](https://www.cloudflare.com/learning/network-layer/what-is-a-wan/)[What is an autonomous system? | What are ASNs?](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/)[What is SD-WAN?](https://www.cloudflare.com/learning/network-layer/what-is-an-sd-wan/)[What is branch networking?](https://www.cloudflare.com/learning/network-layer/what-is-branch-networking/)[What is GRE tunneling? | How GRE protocol works](https://www.cloudflare.com/learning/network-layer/what-is-gre-tunneling/)[What is IGMP? | Internet Group Management Protocol](https://www.cloudflare.com/learning/network-layer/what-is-igmp/)[What is IGMP snooping?](https://www.cloudflare.com/learning/network-layer/what-is-igmp-snooping/)[What is IPsec? | How IPsec VPNs work](https://www.cloudflare.com/learning/network-layer/what-is-ipsec/)[What is MPLS (multiprotocol label switching)?](https://www.cloudflare.com/learning/network-layer/what-is-mpls/)[What is MSS (maximum segment size)?](https://www.cloudflare.com/learning/network-layer/what-is-mss/)[What is My Traceroute (MTR)?](https://www.cloudflare.com/learning/network-layer/what-is-mtr/)[What is MTU (maximum transmission unit)?](https://www.cloudflare.com/learning/network-layer/what-is-mtu/)[What is peering?](https://www.cloudflare.com/learning/network-layer/what-is-peering/)[What is software-defined networking (SDN)?](https://www.cloudflare.com/learning/network-layer/what-is-sdn/)[What is the control plane? | Control plane vs. data plane](https://www.cloudflare.com/learning/network-layer/what-is-the-control-plane/)[What is the network layer?](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)[What is tunneling? | Tunneling in networking](https://www.cloudflare.com/learning/network-layer/what-is-tunneling/)[How does the Internet work?](https://www.cloudflare.com/learning/network-layer/how-does-the-internet-work/)[What is routing?](https://www.cloudflare.com/learning/network-layer/what-is-routing/)[What is a LAN?](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define the network layer in the OSI model 
  * Understand IP addressing and routing 
  * Know the key protocols at this layer 



Related content  [ How does the Internet work? ](https://www.cloudflare.com/learning/network-layer/how-does-the-internet-work/)

On this page

  * What is the network layer?

  * What is a network?

  * What happens at the network layer?

  * What is a packet?

  * What is the OSI model?

  * OSI model vs. TCP/IP model

  * What is the difference between the 'network' layer and the 'Internet' layer?

  * What protocols are used at the network layer?

  * How does Cloudflare protect the network layer?




## What is the network layer?

Network-to-network connections are what make the Internet possible. The "network layer" is the part of the Internet communications process where these connections occur, by sending packets of data back and forth between different networks. In the 7-layer [OSI model](https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/) (see below), the network layer is layer 3. The [Internet Protocol (IP)](https://www.cloudflare.com/learning/ddos/glossary/internet-protocol/) is one of the main protocols used at this layer, along with several other protocols for routing, testing, and [encryption](https://www.cloudflare.com/learning/ssl/what-is-encryption/).

Suppose Bob and Alice are connected to the same local area network (LAN), and Bob wants to send Alice a message. Because Bob is on the same network as Alice, he could send it directly to her computer across the network. However, if Alice is instead on a different LAN several miles away, Bob's message will have to be addressed and sent to Alice's network before it can reach her computer, which is a network layer process.

## What is a network?

A network is a group of two or more connected computing devices. Usually all devices in the network are connected to a central hub — for instance, a router. A network can also include subnetworks, or smaller subdivisions of the network. Subnetworking is how very large networks, such as those provided by ISPs, are able to manage thousands of IP addresses and connected devices.

Think of the Internet as a network of networks: computers are connected to each other within networks, and these networks connect to other networks. This enables these computers to connect with other computers both near and far.

## What happens at the network layer?

Anything that has to do with inter-network connections takes place at the network layer. This includes setting up the routes for data packets to take, checking to see if a server in another network is up and running, and addressing and receiving IP packets from other networks. This last process is perhaps the most important, as the vast majority of Internet traffic is sent over IP.

## What is a packet?

All data sent over the Internet is broken down into smaller chunks called "packets." When Bob sends Alice a message, for instance, his message is broken down into smaller pieces and then reassembled on Alice's computer. A packet has two parts: the header, which contains information about the packet itself, and the body, which is the actual data being sent.

At the network layer, networking software attaches a header to each packet when the packet is sent out over the Internet, and on the other end, networking software can use the header to understand how to handle the packet.

A header contains information about the content, source, and destination of each packet (somewhat like stamping an envelope with a destination and return address). For example, an IP header contains the destination [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/) of each packet, the total size of the packet, an indication of whether or not the packet has been fragmented (broken up into still smaller pieces) in transit, and a count of how many networks the packet has traveled through.

## What is the OSI model?

The Open Systems Interconnection (OSI) Model is a description of how the Internet works. It breaks down the functions involved in sending data over the Internet into seven layers. Each layer has some function that prepares the data to be sent over wires, cables, and radio waves as a series of bits.

The seven layers of the OSI model are:

  1. **Application layer:** Data generated by and usable by software applications. The main protocol used at this layer is [HTTP](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/).
  2. **Presentation layer:** Data is translated into a form the application can accept. Some authorities consider [HTTPS](https://www.cloudflare.com/learning/ssl/what-is-https/) encryption and decryption to take place at this layer.
  3. **Session layer:** Controls connections between computers (this can also be handled at layer 4 by the [TCP protocol](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/)).
  4. **Transport layer:** Provides the means for transmitting data between the two connected parties, as well as controlling the quality of service. The main protocols used here are TCP and [UDP](https://www.cloudflare.com/learning/ddos/glossary/user-datagram-protocol-udp/).
  5. **Network layer:** Handles the routing and sending of data between different networks. The most important protocols at this layer are IP, ICMP, ARP, and BGP.
  6. **Data link layer:** Handles communications between devices on the same network. If layer 3 is like the address on a piece of mail, then layer 2 is like indicating the office number or apartment number at that address. Ethernet is the protocol most used here.
  7. **Physical layer:** Packets are converted into electrical, radio, or optical pulses and transmitted as bits (the smallest possible units of information) over wires, radio waves, or cables.



It is important to keep in mind that the OSI model is an abstract conceptualization of the processes that make the Internet work, and interpreting and applying the model to the real-world Internet is sometimes a subjective exercise.

The OSI model is useful for helping people talk about networking equipment and protocols, determining which protocols are used by which software and hardware, and showing roughly how the Internet works. But it is not a rigid step-by-step definition of how Internet connections always function.

## OSI model vs. TCP/IP model

The TCP/IP model is an alternative model of how the Internet works. It divides the processes involved into four layers instead of seven. Some would argue that the TCP/IP model better reflects the way the Internet functions today, but the OSI model is still widely referenced for understanding the Internet, and both models have their strengths and weaknesses.

In the TCP/IP model, the four layers are:

  1. **Application layer:** This corresponds, approximately, to layer 7 in the OSI model.
  2. **Transport layer:** Corresponds to layer 4 in the OSI model.
  3. **Internet layer:** Corresponds to layer 3 in the OSI model.
  4. **Network access layer:** Combines the processes of layers 1 and 2 in the OSI model.



But where are OSI layers 5 and 6 in the TCP/IP model? Some sources hold that the processes at OSI layers 5 and 6 either are no longer necessary in the modern Internet, or actually belong to [layers 7](https://www.cloudflare.com/learning/ddos/what-is-layer-7/) and 4 (represented by layers 4 and 3 in the TCP/IP model).

For instance, since the TCP protocol opens and maintains sessions at OSI layer 4, one could consider OSI layer 5 (the "session" layer) to be unnecessary — and it is not represented in the TCP/IP model. Additionally, HTTPS encryption and decryption can be considered an application layer (OSI layer 7 or TCP/IP layer 4) process instead of a presentation layer (OSI layer 6) process.

## What is the difference between the 'network' layer and the 'Internet' layer?

In the TCP/IP model, there is no "network" layer. The OSI model network layer roughly corresponds to the TCP/IP model Internet layer. In the OSI model the network layer is layer 3; in the TCP/IP model the Internet layer is layer 2.

In other words, the network layer and the Internet layer are basically the same thing, but they come from different models of how the Internet works.

## What protocols are used at the network layer?

A protocol is an agreed-upon way of formatting data so that two or more devices are able to communicate with and understand each other. A number of different protocols make connections, testing, routing, and encryption possible at the network layer, including:

  * [IP](https://www.cloudflare.com/learning/ddos/glossary/internet-protocol/)
  * IPsec
  * [ICMP](https://www.cloudflare.com/learning/ddos/glossary/internet-control-message-protocol-icmp/)
  * IGMP
  * [BGP](https://www.cloudflare.com/learning/security/glossary/what-is-bgp/)
  * ARP
  * RIP
  * GRE



## How does Cloudflare protect the network layer?

Because they are exposed to the rest of the Internet, network layer infrastructure is vulnerable to external attacks, especially [distributed denial-of-service (DDoS)](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/) attacks. Routers, switches, and other network interfaces can all be overwhelmed or compromised by malicious network traffic, and almost any of the above network protocols can be used in an attack.

[Cloudflare Magic Transit](https://www.cloudflare.com/magic-transit/) protects networking infrastructure using the same technology that keeps more than %{GlobalWebsiteCount} web properties up and running in the face of vulnerability exploits and DDoS attacks. It extends the protection of Cloudflare to on-premise and data center networks, [keeping organizations secure from network layer attacks](https://www.cloudflare.com/network-security/).
