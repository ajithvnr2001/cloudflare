---
url: https://www.cloudflare.com/learning/network-layer/how-does-the-internet-work/
title: How does the Internet work? | Learning Center
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:22.999218+00:00
---

# How does the Internet work? | Learning Center

> Source: https://www.cloudflare.com/learning/network-layer/how-does-the-internet-work/

[ Learning Center ](https://www.cloudflare.com/learning/) / the network layer

##  How does the Internet work? 

The Internet is a global network of interconnected computer networks that communicate using standardized protocols. 

[Learning Center](https://www.cloudflare.com/learning)/the network layer/[What is enterprise networking?](https://www.cloudflare.com/learning/network-layer/enterprise-networking/)[How to migrate from MPLS](https://www.cloudflare.com/learning/network-layer/how-to-migrate-from-mpls/)[How to prepare for network modernization projects](https://www.cloudflare.com/learning/network-layer/how-to-prepare-for-network-modernization-projects/)[What is the Internet Protocol?](https://www.cloudflare.com/learning/network-layer/internet-protocol/)[IPsec VPNs vs. SSL VPNs](https://www.cloudflare.com/learning/network-layer/ipsec-vs-ssl-vpn/)[What is NaaS (network-as-a-service)?](https://www.cloudflare.com/learning/network-layer/network-as-a-service-naas/)[What is network modernization?](https://www.cloudflare.com/learning/network-layer/network-modernization/)[What is network security?](https://www.cloudflare.com/learning/network-layer/network-security/)[SD-WAN vs. MPLS: SD-WAN benefits and drawbacks](https://www.cloudflare.com/learning/network-layer/sd-wan-vs-mpls/)[What is a campus area network (CAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-campus-area-network/)[What is a computer port? | Ports in networking](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/)[What is a metropolitan area network (MAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-metropolitan-area-network/)[What is a network switch? | Switch vs. router](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/)[What is a packet? | Network packet definition](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/)[What is a personal area network (PAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-personal-area-network/)[What is a protocol? | Network protocol definition](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/)[What is a router?](https://www.cloudflare.com/learning/network-layer/what-is-a-router/)[What is a subnet? | How subnetting works](https://www.cloudflare.com/learning/network-layer/what-is-a-subnet/)[What is a WAN? | WAN vs. LAN](https://www.cloudflare.com/learning/network-layer/what-is-a-wan/)[What is an autonomous system? | What are ASNs?](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/)[What is SD-WAN?](https://www.cloudflare.com/learning/network-layer/what-is-an-sd-wan/)[What is branch networking?](https://www.cloudflare.com/learning/network-layer/what-is-branch-networking/)[What is GRE tunneling? | How GRE protocol works](https://www.cloudflare.com/learning/network-layer/what-is-gre-tunneling/)[What is IGMP? | Internet Group Management Protocol](https://www.cloudflare.com/learning/network-layer/what-is-igmp/)[What is IGMP snooping?](https://www.cloudflare.com/learning/network-layer/what-is-igmp-snooping/)[What is IPsec? | How IPsec VPNs work](https://www.cloudflare.com/learning/network-layer/what-is-ipsec/)[What is MPLS (multiprotocol label switching)?](https://www.cloudflare.com/learning/network-layer/what-is-mpls/)[What is MSS (maximum segment size)?](https://www.cloudflare.com/learning/network-layer/what-is-mss/)[What is My Traceroute (MTR)?](https://www.cloudflare.com/learning/network-layer/what-is-mtr/)[What is MTU (maximum transmission unit)?](https://www.cloudflare.com/learning/network-layer/what-is-mtu/)[What is peering?](https://www.cloudflare.com/learning/network-layer/what-is-peering/)[What is software-defined networking (SDN)?](https://www.cloudflare.com/learning/network-layer/what-is-sdn/)[What is the control plane? | Control plane vs. data plane](https://www.cloudflare.com/learning/network-layer/what-is-the-control-plane/)[What is the network layer?](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)[What is tunneling? | Tunneling in networking](https://www.cloudflare.com/learning/network-layer/what-is-tunneling/)[How does the Internet work?](https://www.cloudflare.com/learning/network-layer/how-does-the-internet-work/)[What is routing?](https://www.cloudflare.com/learning/network-layer/what-is-routing/)[What is a LAN?](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand the basic architecture of the Internet 
  * Know how data travels across the Internet 
  * Identify key Internet infrastructure components 



Related content  [ What is the network layer? ](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)

On this page

  * What is the Internet?

  * What is distributed networking, and why is this concept important for the Internet?

  * How does the Internet work?

    * Packets

    * Protocols

  * What physical infrastructure makes the Internet work?

  * How do these concepts relate to websites and applications users access over the Internet?

  * What does 'helping build a better Internet' mean?




## What is the Internet?

![how the Internet works](https://images.ctfassets.net/slt3lc6tev37/2a78t2NoIFtHxWhkfJO1ww/4b072af86f41b9955ad62092a53f40be/how-does-internet-work.png)

Before we cover what the Internet is, we must define what a "network" is. A network is a group of connected computers that are able to send data to each other. A computer network is much like a social circle, which is a group of people who all know each other, regularly exchange information, and coordinate activities together.

The Internet is a vast, sprawling collection of networks that connect to each other. In fact, the word "Internet" could be said to come from this concept: _inter_ connected _net_ works.

Since computers connect to each other within networks and these networks also all connect with each other, one computer can talk to another computer in a faraway network thanks to the Internet. This makes it possible to rapidly exchange information between computers across the world.

Computers connect to each other and to the Internet via wires, cables, radio waves, and other types of networking infrastructure. All data sent over the Internet is translated into pulses of light or electricity, also called "bits," and then interpreted by the receiving computer. The wires, cables, and radio waves conduct these bits at the speed of light. The more bits that can pass over these wires and cables at once, the faster the Internet works.

eBook

5 Ways to Maximize Security & Performance

[Get the eBook](https://www.cloudflare.com/lp/five-ways-maximize-performance/)

ebook

Everywhere security for every phase of the attack lifecycle

[Read the ebook](https://www.cloudflare.com/lp/everywhere-security-ebook/)

## What is distributed networking, and why is this concept important for the Internet?

There is no control center for the Internet. Instead, it is a distributed networking system, meaning it is not dependent on any individual machine. Any computer or hardware that can send and receive data in the correct fashion (e.g. using the correct networking protocols) can be part of the Internet.

The Internet's distributed nature makes it resilient. Computers, servers, and other pieces of networking hardware connect and disconnect from the Internet all the time without impacting how the Internet functions — unlike a computer, which may not function at all if it is missing a component. This applies even at a large scale: if a server, an entire data center, or an entire region of data centers goes down, the rest of the Internet can still function (if more slowly).

Sign Up

Security & speed with any Cloudflare plan

[Start for free](https://www.cloudflare.com/plans/)

## How does the Internet work?

There are two main concepts that are fundamental to the way the Internet functions: _packets_ and _protocols_.

#### Packets

In networking, a packet is a small segment of a larger message. Each packet contains both data and information about that data. The information about the packet's contents is known as the "header," and it goes at the front of the packet so that the receiving machine knows what to do with the packet. To understand the purpose of a packet header, think of how some consumer products come with assembly instructions.

When data gets sent over the Internet, it is first broken up into smaller packets, which are then translated into bits. The packets get routed to their destination by various networking devices such as routers and switches. When the packets arrive at their destination, the receiving device reassembles the packets in order and can then use or display the data.

Compare this process to the way the United States' Statue of Liberty was constructed. The Statue of Liberty was first designed and built in France. However, it was too large to fit onto a ship, so it was shipped to the United States in pieces, along with instructions about where each piece belonged. Workers who received the pieces reassembled them into the statue that stands today in New York.

While this took a long time for the Statue of Liberty, sending digital information in smaller pieces is extremely fast over the Internet. For instance, a photo of the Statue of Liberty stored on a web server can travel across the world one packet at a time and load on someone's computer within milliseconds.

Packets are sent across the Internet using a technique called packet switching. Intermediary routers and switches are able to process packets independently from each other, without accounting for their source or destination. This is by design so that no single connection dominates the network. If data was sent between computers all at once with no packet switching, a connection between two computers could occupy multiple cables, routers, and switches for minutes at a time. Essentially, only two people would be able to use the Internet at a time — instead of an almost unlimited number of people, as is the case in reality.

#### Protocols

Connecting two computers, both of which may use different hardware and run different software, is one of the main challenges that the creators of the Internet had to solve. It requires the use of communications techniques that are understandable by all connected computers, just as two people who grew up in different parts of the world may need to speak a common language to understand each other.

This problem is solved with standardized protocols. In networking, a protocol is a standardized way of doing certain actions and formatting data so that two or more devices are able to communicate with and understand each other.

There are protocols for sending packets between devices on the same network (Ethernet), for sending packets from network to network ([IP](https://www.cloudflare.com/learning/ddos/glossary/internet-protocol/)), for ensuring those packets successfully arrive in order ([TCP](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/)), and for formatting data for websites and applications ([HTTP](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/)). In addition to these foundational protocols, there are also protocols for routing, testing, and [encryption](https://www.cloudflare.com/learning/ssl/what-is-encryption/). And there are alternatives to the protocols listed above for different types of content — for instance, streaming video often uses [UDP](https://www.cloudflare.com/learning/ddos/glossary/user-datagram-protocol-udp/) instead of TCP.

Because all Internet-connected computers and other devices can interpret and understand these protocols, the Internet works no matter who or what connects to it.

## What physical infrastructure makes the Internet work?

A lot of different kinds of hardware and infrastructure go into making the Internet work for everyone. Some of the most important types include the following:

  * [Routers](https://www.cloudflare.com/learning/network-layer/what-is-a-router/) forward packets to different computer networks based on their destination. Routers are like the traffic cops of the Internet, making sure that Internet traffic goes to the right networks.
  * [Switches](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/) connect devices that share a single network. They use packet switching to forward packets to the correct devices. They also receive outbound packets from those devices and pass them along to the right destination.
  * Web servers are specialized high-powered computers that store and serve content (webpages, images, videos) to users, in addition to hosting applications and databases. Servers also respond to [DNS](https://www.cloudflare.com/learning/dns/what-is-dns/) queries and perform other important tasks to keep the Internet up and running. Most servers are kept in large data centers, which are located throughout the world.



## How do these concepts relate to websites and applications users access over the Internet?

![website loading](https://images.ctfassets.net/slt3lc6tev37/5higstotKUWSRPvUc9g7Aj/5b3e03849f5ffb25de2572ebef523fd6/loading-website.png)

Consider this article. In order for you to see it, it was sent over the Internet piece by piece in the form of several thousand data packets. These packets traveled over cables and radio waves and through routers and switches from our web server to your computer or device. Your computer or smartphone received those packets and passed them to your device's browser, and your browser interpreted the data within the packets in order to display the text you are reading now.

The specific steps involved in this process are:

  1. **DNS query:** When your browser started to load this webpage, it likely first made a DNS query to find out the Cloudflare website's IP address.
  2. **TCP handshake:** Your browser opened a connection with that IP address.
  3. **TLS handshake:** Your browser also set up encryption between a Cloudflare web server and your device so that attackers cannot read the data packets that travel between those two endpoints.
  4. **HTTP request:** Your browser requested the content that appears on this webpage.
  5. **HTTP response:** Cloudflare's server transmitted the content in the form of HTML, CSS, and JavaScript code, broken up into a series of data packets. Once your device received the packets and verified it had received all of them, your browser interpreted the HTML, CSS, and JavaScript code contained in the packets to render this article about how the Internet works. The whole process took only a second or two.



As you can see, several different processes and protocols are involved in loading a webpage. You can learn more about these technologies in other parts of the Cloudflare Learning Center:

  * [DNS](https://www.cloudflare.com/learning/dns/what-is-dns/)
  * [TCP](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/)
  * [TLS](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)
  * [HTTP](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/)



## What does 'helping build a better Internet' mean?

The creation of the Internet was an incredible achievement that involved the collective efforts of thousands of individuals and organizations. The fact that the Internet functions today at a far bigger scale than its founders anticipated is a testament to their work.

However, the Internet does not always work as well as it should. Networking issues and malicious activity can slow down Internet access or block it altogether. Third parties can spy on user activities, leading to abuse and, in some cases, government repression. Internet protocols and processes were not designed with security and privacy in mind, since the people who first designed and built the Internet were more concerned with getting it to work than making it perfect.

The Cloudflare mission is to help build a better Internet. Cloudflare aims to accomplish this in a number of ways, including:

  * Contributing to the development of newer, faster, and more secure protocols for the Internet
  * Putting privacy first by building it into all products and offering free services to increase user privacy (such as [1.1.1.1](https://one.one.one.one/) and [DNS over HTTPS](https://www.cloudflare.com/learning/dns/dns-over-tls/))
  * Extending Cloudflare services to a global audience through an ever-expanding international [network of data centers](https://www.cloudflare.com/network/)
  * Offering products that increase security, performance, and reliability for web properties and [network infrastructure](https://www.cloudflare.com/the-net/network-infrastructure/) (many of these products are offered for free to anyone with a website or API)
  * Enabling developers to build faster, more efficient [serverless applications](https://www.cloudflare.com/learning/serverless/what-is-serverless/) to better serve users
  * Educating users about how Internet technology works through the Learning Center and the [Cloudflare Blog](https://blog.cloudflare.com/)



To learn more about Cloudflare's ongoing efforts to contribute to a better Internet, visit our [homepage](https://www.cloudflare.com/) or [follow our blog](https://blog.cloudflare.com/).

To learn in more detail about how networking works, see [What is the network layer?](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)
