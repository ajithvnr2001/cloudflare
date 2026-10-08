---
url: https://www.cloudflare.com/learning/access-management/software-defined-perimeter/
title: What is a software-defined perimeter? | SDP vs. VPN
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:38.419446+00:00
---

# What is a software-defined perimeter? | SDP vs. VPN

> Source: https://www.cloudflare.com/learning/access-management/software-defined-perimeter/

[ Learning Center ](https://www.cloudflare.com/learning/) / access management

##  What is a software-defined perimeter? | SDP vs. VPN 

A software-defined perimeter (SDP) is a network boundary that is based on software, not hardware. SDPs can be part of a Zero Trust security approach. 

[Learning Center](https://www.cloudflare.com/learning)/access management/[How to implement Zero Trust security](https://www.cloudflare.com/learning/access-management/how-to-implement-zero-trust/)[What is the principle of least privilege?](https://www.cloudflare.com/learning/access-management/principle-of-least-privilege/)[What is security service edge (SSE)?](https://www.cloudflare.com/learning/access-management/security-service-edge-sse/)[What is a software-defined perimeter? | SDP vs. VPN](https://www.cloudflare.com/learning/access-management/software-defined-perimeter/)[What is browser isolation?](https://www.cloudflare.com/learning/access-management/what-is-browser-isolation/)[What is microsegmentation?](https://www.cloudflare.com/learning/access-management/what-is-microsegmentation/)[What is ZTNA?](https://www.cloudflare.com/learning/access-management/what-is-ztna/)[What is a CASB?](https://www.cloudflare.com/learning/access-management/what-is-a-casb/)[SASE vs. SSE](https://www.cloudflare.com/learning/access-management/sase-vs-sse/)[What is data loss prevention?](https://www.cloudflare.com/learning/access-management/what-is-dlp/)

######  Learning objectives 

After reading this article you will be able to: 

  * Learn what a software-defined perimeter (SDP) is 
  * Explore how SDPs work 
  * Contrast SDPs with VPNs 



On this page

  * What is a software-defined perimeter?

  * How does an SDP work?

  * How does a user gain access over an SDP?

  * What is mutual TLS?

  * What is a VPN?

  * SDP vs. VPN: What are the differences?

  * How do SDPs relate to Zero Trust security?

  * FAQs

    * What is a software-defined perimeter?

    * How does an SDP verify users before granting access?

    * How do SDPs support a Zero Trust security model?

    * What is the difference between an SDP and a traditional VPN?

    * What are the main use cases for deploying an SDP?




## What is a software-defined perimeter (SDP)?

A software-defined perimeter (SDP) is a way to hide Internet-connected infrastructure (servers, routers, etc.) so that external parties and attackers cannot see it, whether it is hosted on-premise or in the [cloud](https://www.cloudflare.com/learning/cloud/what-is-the-cloud/). The goal of the SDP approach is to base the network perimeter on software instead of hardware. A company that uses an SDP is essentially draping a cloak of invisibility over their servers and other infrastructure so that no one can see it from the outside; however, authorized users can still access the infrastructure.

![Software-Defined Perimeter](https://images.ctfassets.net/slt3lc6tev37/SfV8bjQLW2dZTGvNl1HnP/8d15e71f55a0df6cb15fc9977e263940/what_is_software-defined_perimeter_sdp.png)Software-Defined Perimeter

A software-defined perimeter forms a virtual boundary around company assets at the network layer, not the [application layer](https://www.cloudflare.com/learning/ddos/what-is-layer-7/). This separates it from other [access-based controls](https://www.cloudflare.com/learning/access-management/what-is-access-control/) that restrict user privileges but allow wide network access. Another key difference is that an SDP authenticates devices as well as user identity. The Cloud Security Alliance [first developed](https://downloads.cloudsecurityalliance.org/initiatives/sdp/Software_Defined_Perimeter.pdf) the SDP concept.

## How does an SDP work?

With an SDP, it should not be technologically possible to connect with a server unless authorized to do so. SDPs allow access to users only after 1) verifying user identity, and 2) assessing the state of the device.

Once the user and device are [authenticated](https://www.cloudflare.com/learning/access-management/what-is-authentication/), the SDP sets up an individual network connection between that device and the server it is trying to access. An authenticated user is not logged in to a larger network, but rather is given their own network connection that no one else can access and that only includes the services that the user has approved access to.

Imagine a web server that is connected to the Internet but does not open connections with anything. It does not accept requests or send responses; it has no open ports and no network access even though it is plugged into the Internet (somewhat like a toaster or a lamp that is plugged into a wall outlet but turned off so that electricity does not flow through it). This is the default state for servers inside a software-defined perimeter.

Another way to think of SDPs is to imagine a front door that is always kept locked. No one can come through the door, or even look inside, until the person on the other side of the door verifies who the visitor is and what they are doing. Once the visitor is allowed inside, the person in the house locks the door again.

## How does a user gain access over an SDP?

**User identity verification:** User identity is typically verified via a third-party identity provider (IdP). SDPs may integrate with an [SSO](https://www.cloudflare.com/learning/access-management/what-is-sso/) solution as well. User authentication can involve a simple username and password combination, but it is more secure to use [multi-factor authentication](https://www.cloudflare.com/learning/access-management/what-is-multi-factor-authentication/) with some sort of hardware [token](https://www.cloudflare.com/learning/access-management/token-based-authentication/).

**Device verification:** This involves checking to make sure the user's device is running up-to-date software, checking for [malware](https://www.cloudflare.com/learning/ddos/glossary/malware/) infections, and performing other security inspections. Theoretically, an SDP could even create a blocklist of disallowed devices and check to make sure the device is not on the blocklist.

**SDP controller approval:** The SDP "controller" is the logical component of the SDP that is responsible for determining which devices and servers should be allowed to connect. Once the user and device are authenticated, the controller passes along approval of the user and device to the SDP gateway. The SDP gateway is where access is actually allowed or denied.

**Secure network connection established:** The SDP gateway opens the virtual "gate" to allow the user through. It establishes a secure network connection with the user device on one side of the gateway, and on the other side it establishes a network connection with the services that the user has access to. No other users or servers share this connection. These secure network connections typically involve the use of mutual [TLS](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/), and may use a [VPN](https://www.cloudflare.com/learning/access-management/what-is-a-vpn/).

**User access:** The user is able to access previously hidden network resources and can continue using their device like normal. The user operates within an [encrypted](https://www.cloudflare.com/learning/ssl/what-is-encryption/) network to which only they and the services they access belong.

## What is mutual TLS?

[TLS, or Transport Layer Security](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/), is an encryption and authentication protocol that verifies that a server is legitimate, meaning it is who it claims to be. In mutual TLS, the verification process takes place on both sides: the client is verified as well as the server. [Learn more about mutual TLS](https://www.cloudflare.com/learning/access-management/what-is-mutual-tls/).

## What is a VPN?

A [VPN, or virtual private network](https://www.cloudflare.com/learning/access-management/what-is-a-vpn/), is an encrypted network that runs over an unencrypted network. It creates encrypted connections between devices and servers so that it is as if they are on their own private network.

Traditionally, VPNs have been used to secure and manage access to company infrastructure. In some cases, an SDP can replace a VPN.

## SDP vs. VPN: What are the differences?

SDPs may incorporate VPNs into their architecture to create secure network connections between user devices and the servers they need to access. However, SDPs are very different from VPNs. In some ways, they are more secure: while VPNs enable all connected users to access the entire network, SDPs do not share network connections. SDPs may also be easier to manage than VPNs, especially if internal users need multiple levels of access.

Managing several different levels of network access using VPNs involves deploying multiple VPNs. Suppose Bob works at Acme Inc. in accounting, Carol works in sales, and Alice works in engineering. Managing their access at the network level involves setting up three VPNs: 1) an accounting VPN to provide access to the accounting database, 2) a sales VPN for the customer database, and 3) an engineering VPN for the codebase. Not only is this difficult for IT to manage, it is also less secure: anyone who gains access to the accounting VPN, for instance, can now access the financial information of Acme Inc. If Bob accidentally gives his login credentials to Carol, then security is compromised — and IT may not even be aware of it.

Now imagine a fourth person: David, the CFO of Acme Inc. David needs access to both the accounting database and the customer database. Should David have to log in to two separate VPNs in order to do his work? Or should Acme's IT department set up a new VPN that provides access to both accounting and the customer database? Both options are unwieldy to manage, and the second option introduces a high degree of risk: an attacker who compromises this new VPN with broad access across two databases is able to do twice as much damage as before.

SDPs, on the other hand, are much more granular. There is no overall VPN that everyone who accesses the same resources logs in to; instead, a separate network connection is established for each user. It is almost as if everyone has their own private VPN. In addition, SDPs verify devices as well as users, making it much more difficult for an attacker to breach the system with stolen credentials alone.

A couple other key features separate SDPs from VPNs: SDPs are location- and infrastructure-agnostic. Because they are based on software rather than hardware, SDPs can be deployed anywhere to protect on-premise infrastructure, cloud infrastructure, or both. SDPs also easily integrate with [multi-cloud](https://www.cloudflare.com/learning/cloud/what-is-multicloud/) and [hybrid cloud](https://www.cloudflare.com/learning/cloud/what-is-hybrid-cloud/) deployments. And finally, SDPs can connect users in any location; they do not need to be within a company's physical network perimeter. This makes SDPs useful for [managing remote teams](https://www.cloudflare.com/learning/access-management/what-is-remote-access-security/) that do not work within a corporate office.

## How do SDPs relate to Zero Trust security?

As the name implies, there is no trust in Zero Trust security; no user, device, or network is considered trustworthy by default. Zero Trust security is a security model that requires strict identity verification for every person and device trying to access internal resources, no matter whether they are sitting inside or outside the network perimeter (or, the software-defined perimeter).

An SDP is one way to [implement Zero Trust security](https://www.cloudflare.com/learning/access-management/how-to-implement-zero-trust/). Users and devices must both be verified before they can connect, and they have only the minimum network access they need. No device, not even a CEO's laptop, can form a network connection with a resource it is not authorized to use.

[Learn more about Zero Trust security.](https://www.cloudflare.com/learning/security/glossary/what-is-zero-trust/)

## FAQs

#### What is a software-defined perimeter (SDP)?

An SDP is a security solution that hides Internet-connected infrastructure like servers and routers so that unauthorized parties and attackers cannot connect to it. It creates a virtual boundary around company assets, defining a "perimeter" by software rather than physical hardware. Because the infrastructure is hidden, it becomes more difficult for bad actors to launch attacks.

#### How does an SDP verify users before granting access?

Unlike traditional security that focuses on network location, an SDP grants access based on identity. Before a connection is established, the SDP verifies the user's identity and assesses the state of their device. Once the user is authenticated, the SDP creates an individual, encrypted network connection between that specific user and the resources they are authorized to use.

#### How do SDPs support a Zero Trust security model?

SDPs are one way to implement Zero Trust because they operate on the principle that no user or device should be trusted by default. By requiring verification for every single person and device before allowing them to connect to any part of the network, an SDP ensures that the perimeter is everywhere a user might be.

#### What is the difference between an SDP and a traditional VPN?

While both SDPs and VPNs provide remote access, they handle security very differently, a VPN often gives a user access to an entire local network, whereas an SDP only grants access to specific, authorized applications. VPNs also leave some resources visible to the network, while an SDP keeps all infrastructure hidden until authentication is complete.

#### What are the main use cases for deploying an SDP?

Organizations use SDPs to secure remote access for employees working from home or outside the office, manage access for third-party contractors and vendors without giving them full network entry, and protect multi-cloud or hybrid cloud environments where resources are spread across different providers.
