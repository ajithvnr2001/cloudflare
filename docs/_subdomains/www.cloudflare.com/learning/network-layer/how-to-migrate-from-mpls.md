---
url: https://www.cloudflare.com/learning/network-layer/how-to-migrate-from-mpls/
title: How to migrate from MPLS
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:26.400010+00:00
---

# How to migrate from MPLS

> Source: https://www.cloudflare.com/learning/network-layer/how-to-migrate-from-mpls/

[ Learning Center ](https://www.cloudflare.com/learning/) / the network layer

##  How to migrate from MPLS 

Organizations are often constrained by their reliance on MPLS. These are the steps for migrating from MPLS to more flexible, scalable, secure, and cost-effective network architecture. 

[Learning Center](https://www.cloudflare.com/learning)/the network layer/[What is enterprise networking?](https://www.cloudflare.com/learning/network-layer/enterprise-networking/)[How to migrate from MPLS](https://www.cloudflare.com/learning/network-layer/how-to-migrate-from-mpls/)[How to prepare for network modernization projects](https://www.cloudflare.com/learning/network-layer/how-to-prepare-for-network-modernization-projects/)[What is the Internet Protocol?](https://www.cloudflare.com/learning/network-layer/internet-protocol/)[IPsec VPNs vs. SSL VPNs](https://www.cloudflare.com/learning/network-layer/ipsec-vs-ssl-vpn/)[What is NaaS (network-as-a-service)?](https://www.cloudflare.com/learning/network-layer/network-as-a-service-naas/)[What is network modernization?](https://www.cloudflare.com/learning/network-layer/network-modernization/)[What is network security?](https://www.cloudflare.com/learning/network-layer/network-security/)[SD-WAN vs. MPLS: SD-WAN benefits and drawbacks](https://www.cloudflare.com/learning/network-layer/sd-wan-vs-mpls/)[What is a campus area network (CAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-campus-area-network/)[What is a computer port? | Ports in networking](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/)[What is a metropolitan area network (MAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-metropolitan-area-network/)[What is a network switch? | Switch vs. router](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/)[What is a packet? | Network packet definition](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/)[What is a personal area network (PAN)?](https://www.cloudflare.com/learning/network-layer/what-is-a-personal-area-network/)[What is a protocol? | Network protocol definition](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/)[What is a router?](https://www.cloudflare.com/learning/network-layer/what-is-a-router/)[What is a subnet? | How subnetting works](https://www.cloudflare.com/learning/network-layer/what-is-a-subnet/)[What is a WAN? | WAN vs. LAN](https://www.cloudflare.com/learning/network-layer/what-is-a-wan/)[What is an autonomous system? | What are ASNs?](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/)[What is SD-WAN?](https://www.cloudflare.com/learning/network-layer/what-is-an-sd-wan/)[What is branch networking?](https://www.cloudflare.com/learning/network-layer/what-is-branch-networking/)[What is GRE tunneling? | How GRE protocol works](https://www.cloudflare.com/learning/network-layer/what-is-gre-tunneling/)[What is IGMP? | Internet Group Management Protocol](https://www.cloudflare.com/learning/network-layer/what-is-igmp/)[What is IGMP snooping?](https://www.cloudflare.com/learning/network-layer/what-is-igmp-snooping/)[What is IPsec? | How IPsec VPNs work](https://www.cloudflare.com/learning/network-layer/what-is-ipsec/)[What is MPLS (multiprotocol label switching)?](https://www.cloudflare.com/learning/network-layer/what-is-mpls/)[What is MSS (maximum segment size)?](https://www.cloudflare.com/learning/network-layer/what-is-mss/)[What is My Traceroute (MTR)?](https://www.cloudflare.com/learning/network-layer/what-is-mtr/)[What is MTU (maximum transmission unit)?](https://www.cloudflare.com/learning/network-layer/what-is-mtu/)[What is peering?](https://www.cloudflare.com/learning/network-layer/what-is-peering/)[What is software-defined networking (SDN)?](https://www.cloudflare.com/learning/network-layer/what-is-sdn/)[What is the control plane? | Control plane vs. data plane](https://www.cloudflare.com/learning/network-layer/what-is-the-control-plane/)[What is the network layer?](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)[What is tunneling? | Tunneling in networking](https://www.cloudflare.com/learning/network-layer/what-is-tunneling/)[How does the Internet work?](https://www.cloudflare.com/learning/network-layer/how-does-the-internet-work/)[What is routing?](https://www.cloudflare.com/learning/network-layer/what-is-routing/)[What is a LAN?](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/)

######  Learning objectives 

After reading this article you will be able to: 

  * Explain why organizations migrate from MPLS to more flexible network architecture 
  * List the main steps for migrating from MPLS to SD-WAN 
  * List the main steps for migrating from MPLS to SASE 



Related content  [ SD-WAN vs. MPLS: SD-WAN benefits and drawbacks ](https://www.cloudflare.com/learning/network-layer/sd-wan-vs-mpls/)[ How to prepare for network modernization projects ](https://www.cloudflare.com/learning/network-layer/how-to-prepare-for-network-modernization-projects/)[ What is network modernization? ](https://www.cloudflare.com/learning/network-layer/network-modernization/)[ What is MPLS (multiprotocol label switching)? ](https://www.cloudflare.com/learning/network-layer/what-is-mpls/)[ What is SD-WAN? ](https://www.cloudflare.com/learning/network-layer/what-is-an-sd-wan/)

On this page

  * Article Summary:

  * How to migrate from MPLS

  * How to migrate from MPLS to SD-WAN

    * 1\. Assess and document the current network setup

    * 2\. Choose an SD-WAN provider

    * 3\. Create a migration plan

    * 4\. Execute the migration

    * 5\. Monitor post-migration performance

  * Why SASE has evolved out of SD-WAN

  * How to migrate from MPLS to SASE

    * 1\. Modernize user-to-app access

    * 2\. Replace private circuits with broadband Internet access for branch connectivity

    * 3\. Secure cloud environments

    * 4\. Decommission hardware appliances and private circuits

  * How to start modernizing MPLS networks with Cloudflare

  * FAQs

    * Why are traditional multiprotocol label switching networks less effective for modern businesses?

    * What are the primary advantages of upgrading to a more modern network architecture?

    * How does a secure access service edge model differ from software-defined wide area networking?

    * What initial steps should an organization take when starting a migration to SD-WAN?

    * What is the recommended process for transitioning branch offices to a SASE-based model?




## Article Summary:

  * Establish a performance baseline by documenting current network topology and bandwidth. Then, select a provider that supports hybrid environments to ensure a smooth MPLS migration transition.

  * Implement SD-WAN or SASE to replace rigid, location-bound circuits. This modernization enhances scalability, lowers operational costs, and provides faster application performance for distributed, cloud-first workforces.

  * Transition branch offices using Anycast GRE or IPsec tunnels over broadband. Gradually shift traffic to cloud-delivered network services and zero trust security before decommissioning legacy private circuits.




## How to migrate from MPLS

[Multiprotocol label switching (MPLS)](https://www.cloudflare.com/learning/network-layer/what-is-mpls/) offers stability and predictable service levels while allowing enterprises to connect their [branch offices](https://www.cloudflare.com/learning/network-layer/what-is-branch-networking/). However, its static nature makes it a poor fit for modern ways of working, for [cloud computing](https://www.cloudflare.com/learning/cloud/what-is-the-cloud/), and especially for integrating [artificial intelligence (AI)](https://www.cloudflare.com/learning/ai/what-is-artificial-intelligence/) into workflows.

To increase network flexibility, scalability, and security, enterprises often modernize their networks by migrating from MPLS to alternative networking models, including [SD-WAN](https://www.cloudflare.com/learning/network-layer/what-is-an-sd-wan/) or [SASE](https://www.cloudflare.com/learning/access-management/what-is-sase/) (the latter of which natively integrates [zero trust security](https://www.cloudflare.com/learning/security/glossary/what-is-zero-trust/) principles). The move to SD-WAN was a common step in the 2010s for many businesses, although organizations today find that SD-WAN on its own has limitations, and are looking to modernize further by moving straight to SASE.

[Network modernization](https://www.cloudflare.com/learning/network-layer/network-modernization/) can be an intensive process that takes weeks or months, but organizations can reap the benefits of it for years to come, including:

  * Simpler connectivity

  * Faster application and network performance

  * Scalable security

  * Increased agility

  * Lower operational costs




## How to migrate from MPLS to SD-WAN

#### 1\. Assess and document the current network setup

Document bandwidth needs, business-critical applications, and network topology. Recording a baseline of network performance is critical, as that provides a comparison point as the SD-WAN migration is first tested.

#### 2\. Choose an SD-WAN provider

Different providers offer different features and levels of support; ensure the selected vendor can support business-critical applications and other must-haves.

Many organizations have critical systems or infrastructure that cannot be moved off of MPLS. Partial migration to SD-WAN can still help optimize much of their network. In such cases, enterprises should ensure they select a vendor who can support hybrid network environments.

#### 3\. Create a migration plan

Define the future state of the migrated network, determine which steps to take to reach that state, then decide what aspects of the network should be migrated first. Set a schedule for migration

#### 4\. Execute the migration

Start switching over parts of the network to the SD-WAN provider in accordance with the plan from step 3; many organizations start with a single branch network, followed by performance testing, before migrating other parts of the network. Maintain legacy systems as a backup before fully cutting over to the new network.

#### 5\. Monitor post-migration performance

Before switching off legacy systems completely, make sure the new configuration is performing better than the baseline documented in step 1.

## Why SASE has evolved out of SD-WAN

Though SD-WAN is often thought of as the next stage for organizations as they [modernize their networks](https://www.cloudflare.com/learning/network-layer/how-to-prepare-for-network-modernization-projects/), on its own it has many performance and security gaps that can continue to hinder organizational growth. In particular, SD-WAN is designed to connect buildings, not people. As a result, relying solely on SD-WAN means connectivity is fundamentally location-bound. This is less than ideal for the way many modern organizations work. A SASE model replaces location-dependent rules with a unified set of policies and experiences that remains identical whether a user is at an office desk or on the move.

Secure access service edge (SASE) is the next logical step in network modernization. SASE, in addition to a flexible, software-defined networking model, has security built in. It is a cloud-based architecture that converges network connectivity and comprehensive zero trust security in a single, unified platform.

## How to migrate from MPLS to SASE

Ebook

The 10 key milestones for the journey to full SASE architecture

[Get the guide →](https://www.cloudflare.com/lp/10-steps-sase-journey/)

#### 1\. Modernize user-to-app access

Switch to a policy that connects users only to the specific apps they are authorized to use, via zero trust network access ([ZTNA](https://www.cloudflare.com/learning/access-management/what-is-ztna/)) controls, instead of the broad access offered through VPNs. For flexibility, SASE relies on a range of connectivity methods, not exclusively private circuits; internal data, applications, networks, and users therefore need to be protected regardless of location or how they are connected. Start by:

  * Enforcing [multi-factor authentication (MFA)](https://www.cloudflare.com/learning/access-management/what-is-multi-factor-authentication/) for critical applications

  * Applying zero trust policies for access to critical applications

  * Applying advanced [phishing](https://www.cloudflare.com/learning/access-management/phishing-attack/) filters to email traffic

  * Closing all inbound ports open to the Internet for application delivery

  * Using global [DNS filtering](https://www.cloudflare.com/learning/access-management/what-is-dns-filtering/) to block risky requests




#### 2\. Replace private circuits with broadband Internet access for branch connectivity

The goal here is to switch from private circuits to cloud-delivered network services, with network traffic and applications protected by ZTNA instead of [VPNs](https://www.cloudflare.com/learning/access-management/what-is-a-vpn/) and on-premises point solutions at branch networks. Steps include:

  * Choose two MPLS-connected locations to start with, and ensure they have Internet connectivity.

  * Measure network performance at these locations to establish a baseline.

  * Select a cloud-based WAN or [network-as-a-service (NaaS)](https://www.cloudflare.com/learning/network-layer/network-as-a-service-naas/) provider.

  * Establish a pair of redundant Anycast [GRE](https://www.cloudflare.com/learning/network-layer/what-is-gre-tunneling/) or [IPsec](https://www.cloudflare.com/learning/network-layer/what-is-ipsec/) tunnels over Internet circuits to the cloud WAN provider's network. (Anycast specifically addresses reliability concerns by routing traffic to the nearest healthy data center rather than a fixed point.)

  * Test performance (throughput, [latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/), packet loss, jitter) of those tunnels.

  * Change [routing](https://www.cloudflare.com/learning/network-layer/what-is-routing/) policies to migrate production traffic from MPLS to Internet tunnels.

  * Repeat at next MPLS-connected location.

  * Decommission MPLS circuits as needed.




#### 3\. Secure cloud environments

At this point, multi-cloud environments should be connected following a similar process to that described above:

  * Choose one cloud environment to start with, and measure app performance to establish a baseline.

  * Establish a connection to the cloud-based WAN or NaaS provider.

  * Test performance via this connection.

  * Change routing policies to migrate cloud production traffic through WAN/NaaS provider.

  * Repeat for all cloud deployments.

  * Then, use a service like [Multi-Cloud Networking](https://developers.cloudflare.com/multi-cloud-networking/) to discover, manage, and secure all data and workloads in the cloud.




#### 4\. Decommission hardware appliances and private circuits

Not all organizations will be able to, or even desire to, reach the point of turning off all on-premises infrastructure and hardware-based networking and security. However, migrating to SASE does give organizations the opportunity to do so, for increased flexibility and scalability with minimal latency.

## How to start modernizing MPLS networks with Cloudflare

The Cloudflare connectivity cloud delivers secure, fast, and reliable service to any point in the world, and easily adapts to new business requirements. Here's how:

  * Cloudflare handles [BGP](https://www.cloudflare.com/learning/security/glossary/what-is-bgp/) traffic by allowing customer edge routers (CPE) to peer directly with the Cloudflare network. This replaces the need for static routes and allows for dynamic failover.

  * Customers establish a BGP session over their existing connectivity, via GRE tunnels, [IPsec](https://www.cloudflare.com/learning/network-layer/what-is-ipsec/) tunnels, or a Cloudflare Network Interconnect (CNI).

  * Customer routers advertise their internal prefixes (e.g. branch office subnets) to Cloudflare.

  * Cloudflare then updates its Virtual Network routing table across all 335+-plus global data centers.




Use Cloudflare for networking and security to strengthen business continuity, improve the user experience, and reduce operating costs. Learn [how to start modernizing networks with Cloudflare](https://www.cloudflare.com/coffee-shop-networking/).

## FAQs

#### Why are traditional multiprotocol label switching (MPLS) networks less effective for modern businesses?

While MPLS provides reliable connectivity for branch offices, its rigid design struggles to keep up with the demands of cloud computing and the integration of artificial intelligence (AI) into daily operations. Modern work environments require more flexibility than these static networks can offer.

#### What are the primary advantages of upgrading to a more modern network architecture?

Transitioning away from legacy systems allows organizations to experience better application performance, simplified connectivity, and improved agility. Additionally, these updates can lower overall operational costs while providing security that scales alongside the business.

#### How does a secure access service edge (SASE) model differ from software-defined wide area networking (SD-WAN)?

SD-WAN was primarily built to link physical buildings, which can restrict users to specific locations. In contrast, SASE is a cloud-native framework that combines networking with zero trust security. This ensures that employees have a consistent and secure experience whether they are working from a branch office, working from home, or traveling.

#### What initial steps should an organization take when starting a migration to SD-WAN?

The process begins by documenting the current network topology, bandwidth requirements, and most important applications to establish a performance baseline. Organizations must then choose a provider that aligns with their specific technical needs, especially if they require a hybrid setup to maintain certain legacy systems.

#### What is the recommended process for transitioning branch offices to a SASE-based model?

Organizations should start by establishing Internet connectivity at a few locations and measuring their performance baseline. After selecting a cloud-based provider, they can create secure Anycast GRE or IPsec tunnels to route traffic. Once these tunnels are tested and production traffic is successfully moved to the new Internet-based paths, the old private circuits can be decommissioned.
