---
url: https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/
title: What is a computer port? | Ports in networking
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:45.190827+00:00
---

# What is a computer port? | Ports in networking

> Source: https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/

[ Learning Center ](https://www.cloudflare.com/learning/) / the network layer

##  What is a computer port? | Ports in networking 

Ports are virtual places within an operating system where network connections start and end. They help computers sort the network traffic they receive. 

[Learning Center](https://www.cloudflare.com/learning)/the network layer/[What is enterprise networking?](https://www.cloudflare.com/learning/network-layer/enterprise-networking/)[How to migrate from MPLS](https://www.cloudflare.com/learning/network-layer/how-to-migrate-from-mpls/)[How to prepare for network modernization projects](https://www.cloudflare.com/learning/network-layer/how-to-prepare-for-network-modernization-projects/)[What is the Internet Protocol?](https://www.cloudflare.com/learning/network-layer/internet-protocol/)[IPsec VPNs vs. SSL VPNs](https://www.cloudflare.com/learning/network-layer/ipsec-vs-ssl-vpn/)[What is NaaS (network-as-a-service)?](https://www.cloudflare.com/learning/network-layer/network-as-a-service-naas/)[What is network modernization?](https://www.cloudflare.com/learning/network-layer/network-modernization/)[What is network security?](https://www.cloudflare.com/learning/network-layer/network-security/)[SD-WAN vs. MPLS: SD-WAN benefits and drawbacks](https://www.cloudflare.com/learning/network-layer/sd-wan-vs-mpls/)[What is a campus area network (CAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-campus-area-network/)[What is a computer port? | Ports in networking](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/)[What is a metropolitan area network (MAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-metropolitan-area-network/)[What is a network switch? | Switch vs. router](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/)[What is a packet? | Network packet definition](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/)[What is a personal area network (PAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-personal-area-network/)[What is a protocol? | Network protocol definition](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/)[What is a router?](https://www.cloudflare.com/learning/network-layer/what-is-a-router/)[What is a subnet? | How subnetting works](https://www.cloudflare.com/learning/network-layer/what-is-a-subnet/)[What is a WAN? | WAN vs. LAN](https://www.cloudflare.com/learning/network-layer/what-is-a-wan/)[What is an autonomous system? | What are ASNs?](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/)[What is SD-WAN?](https://www.cloudflare.com/learning/network-layer/what-is-an-sd-wan/)[What is branch networking?](https://www.cloudflare.com/learning/network-layer/what-is-branch-networking/)[What is GRE tunneling? | How GRE protocol works](https://www.cloudflare.com/learning/network-layer/what-is-gre-tunneling/)[What is IGMP? | Internet Group Management Protocol](https://www.cloudflare.com/learning/network-layer/what-is-igmp/)[What is IGMP snooping?](https://www.cloudflare.com/learning/network-layer/what-is-igmp-snooping/)[What is IPsec? | How IPsec VPNs work](https://www.cloudflare.com/learning/network-layer/what-is-ipsec/)[What is MPLS (multiprotocol label switching)?](https://www.cloudflare.com/learning/network-layer/what-is-mpls/)[What is MSS (maximum segment size)?](https://www.cloudflare.com/learning/network-layer/what-is-mss/)[What is My Traceroute (MTR)?](https://www.cloudflare.com/learning/network-layer/what-is-mtr/)[What is MTU (maximum transmission unit)?](https://www.cloudflare.com/learning/network-layer/what-is-mtu/)[What is peering?](https://www.cloudflare.com/learning/network-layer/what-is-peering/)[What is software-defined networking (SDN)?](https://www.cloudflare.com/learning/network-layer/what-is-sdn/)[What is the control plane? | Control plane vs. data plane](https://www.cloudflare.com/learning/network-layer/what-is-the-control-plane/)[What is the network layer?](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)[What is tunneling? | Tunneling in networking](https://www.cloudflare.com/learning/network-layer/what-is-tunneling/)[How does the Internet work?](https://www.cloudflare.com/learning/network-layer/how-does-the-internet-work/)[What is routing?](https://www.cloudflare.com/learning/network-layer/what-is-routing/)[What is a LAN?](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/)

######  Learning objectives 

After reading this article you will be able to: 

  * Learn the purpose of ports in networking 
  * Learn about the most commonly used port numbers 
  * Understand where ports belong in the OSI model 



Related content  [ What is the Internet Protocol? ](https://www.cloudflare.com/learning/network-layer/internet-protocol/)[ What is a network switch? | Switch vs. router ](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/)[ What is a LAN? ](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/)[ How does the Internet work? ](https://www.cloudflare.com/learning/network-layer/how-does-the-internet-work/)[ What is a subnet? | How subnetting works ](https://www.cloudflare.com/learning/network-layer/what-is-a-subnet/)

On this page

  * What is a port?

  * What is a port number?

  * How do ports make network connections more efficient?

  * Are ports part of the network layer?

  * Why do firewalls sometimes block specific ports?

  * What are the different port numbers?




## What is a port?

A port is a virtual point where network connections start and end. Ports are software-based and managed by a computer's operating system. Each port is associated with a specific process or service. Ports allow computers to easily differentiate between different kinds of traffic: emails go to a different port than webpages, for instance, even though both reach a computer over the same Internet connection.

## What is a port number?

Ports are standardized across all network-connected devices, with each port assigned a number. Most ports are reserved for certain [protocols](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/) — for example, all [Hypertext Transfer Protocol (HTTP)](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/) messages go to port 80. While [IP addresses](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/) enable messages to go to and from specific devices, port numbers allow targeting of specific services or applications within those devices.

## How do ports make network connections more efficient?

Vastly different types of data flow to and from a computer over the same network connection. The use of ports helps computers understand what to do with the data they receive.

Suppose Bob transfers an MP3 audio recording to Alice using the File Transfer Protocol (FTP). If Alice's computer passed the MP3 file data to Alice's email application, the email application would not know how to interpret it. But because Bob's file transfer uses the port designated for FTP (port 21), Alice's computer is able to receive and store the file.

Meanwhile, Alice's computer can simultaneously load HTTP webpages using port 80, even though both the webpage files and the MP3 sound file flow to Alice's computer over the same WiFi connection.

Whitepaper

How to break free from network hardware

[Get the report →](https://www.cloudflare.com/lp/network-hardware/)

## Are ports part of the network layer?

The [OSI model](https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/) is a conceptual model of how the Internet works. It divides different Internet services and processes into 7 layers. These layers are:

![osi model 7 layers](https://www.cloudflare.com/img/learning/ddos/what-is-a-ddos-attack/osi-model-7-layers.svg)osi model 7 layers

Ports are a transport layer (layer 4) concept. Only a transport protocol such as the [Transmission Control Protocol (TCP)](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/) or [User Datagram Protocol (UDP)](https://www.cloudflare.com/learning/ddos/glossary/user-datagram-protocol-udp/) can indicate which port a packet should go to. TCP and UDP headers have a section for indicating port numbers. [Network layer](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/) protocols — for instance, the [Internet Protocol (IP)](https://www.cloudflare.com/learning/network-layer/internet-protocol/) — are unaware of what port is in use in a given network connection. In a standard IP header, there is no place to indicate which port the data [packet](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/) should go to. IP headers only indicate the destination IP address, not the port number at that IP address.

Usually, the inability to indicate the port at the network layer has no impact on networking processes, since network layer protocols are almost always used in conjunction with a transport layer protocol. However, this does impact the functionality of testing software, which is software that "pings" IP addresses using [Internet Control Message Protocol (ICMP)](https://www.cloudflare.com/learning/ddos/glossary/internet-control-message-protocol-icmp/) packets. ICMP is a network layer protocol that can ping networked devices — but without the ability to ping specific ports, network administrators cannot test specific services within those devices.

Some ping software, such as [My Traceroute](https://www.cloudflare.com/learning/network-layer/what-is-mtr/), offers the option to send UDP packets. UDP is a transport layer protocol that can specify a particular port, as opposed to ICMP, which cannot specify a port. By adding a UDP header to ICMP packets, network administrators can test specific ports within a networked device.

Sign Up

Security & speed with any Cloudflare plan

[Start for free →](https://www.cloudflare.com/lp/pg-all-plans-multi-sku-lc/)

## Why do firewalls sometimes block specific ports?

A [firewall](https://www.cloudflare.com/learning/security/what-is-a-firewall/) is a [network security system](https://www.cloudflare.com/network-security/) that blocks or allows network traffic based on a set of security rules. Firewalls usually sit between a trusted network and an untrusted network; often the untrusted network is the Internet. For example, office networks often use a firewall to protect their network from online threats.

Some attackers try to send malicious traffic to random ports in the hopes that those ports have been left "open," meaning they are able to receive traffic. This action is somewhat like a car thief walking down the street and trying the doors of parked vehicles, hoping one of them is unlocked. For this reason, firewalls should be configured to block network traffic directed at most of the available ports. There is no legitimate reason for the vast majority of the available ports to receive traffic.

Properly configured firewalls block traffic to all ports by default except for a few predetermined ports known to be in common use. For instance, a corporate firewall could only leave open ports 25 (email), 80 (web traffic), 443 (web traffic), and a few others, allowing internal employees to use these essential services, then block the rest of the 65,000+ ports.

As a more specific example, attackers sometimes attempt to exploit vulnerabilities in the RDP protocol by sending attack traffic to port 3389. To stop these attacks, a firewall may block port 3389 by default. Since this port is only used for remote desktop connections, such a rule has little impact on day-to-day business operations unless employees need to work remotely.

## What are the different port numbers?

There are 65,535 possible port numbers, although not all are in common use. Some of the most commonly used ports, along with their associated networking protocol, are:

  * **Ports 20 and 21:** File Transfer Protocol (FTP). FTP is for transferring files between a client and a server.

  * **Port 22:** Secure Shell (SSH). SSH is one of many [tunneling](https://www.cloudflare.com/learning/network-layer/what-is-tunneling/) protocols that create secure network connections.

  * [Port 25](https://www.cloudflare.com/learning/email-security/smtp-port-25-587/): Historically, [Simple Mail Transfer Protocol (SMTP)](https://www.cloudflare.com/learning/email-security/what-is-smtp/). SMTP is used for [email](https://www.cloudflare.com/learning/email-security/what-is-email/).

  * **Port 53:** [Domain Name System (DNS)](https://www.cloudflare.com/learning/dns/what-is-dns/). DNS is an essential process for the modern Internet; it matches human-readable [domain names](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/) to machine-readable IP addresses, enabling users to load websites and applications without memorizing a long list of IP addresses.

  * **Port 80:** Hypertext Transfer Protocol (HTTP). HTTP is the protocol that makes the World Wide Web possible.

  * **Port 123:** [Network Time Protocol (NTP)](https://blog.cloudflare.com/secure-time/). NTP allows computer clocks to sync with each other, a process that is essential for [encryption](https://www.cloudflare.com/learning/ssl/what-is-encryption/).

  * **Port 179:** [Border Gateway Protocol (BGP)](https://www.cloudflare.com/learning/security/glossary/what-is-bgp/). BGP is essential for establishing efficient routes between the large networks that make up the Internet (these large networks are called [autonomous systems](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/)). Autonomous systems use BGP to broadcast which IP addresses they control.

  * **Port 443:** [HTTP Secure (HTTPS)](https://www.cloudflare.com/learning/ssl/what-is-https/). HTTPS is the secure and encrypted version of HTTP. All HTTPS web traffic goes to port 443. Network services that use HTTPS for encryption, such as [DNS over HTTPS](https://www.cloudflare.com/learning/dns/dns-over-tls/), also connect at this port.

  * **Port 500:** Internet Security Association and Key Management Protocol (ISAKMP), which is part of the process of setting up secure [IPsec](https://www.cloudflare.com/learning/network-layer/what-is-ipsec/) connections.

  * **Port 587:** Modern, secure SMTP that uses encryption.

  * **Port 3389:** [Remote Desktop Protocol](https://www.cloudflare.com/learning/access-management/what-is-the-remote-desktop-protocol/) (RDP). RDP enables users to remotely connect to their desktop computers from another device.




The Internet Assigned Numbers Authority (IANA) maintains the [full list](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml) of port numbers and protocols assigned to them.
