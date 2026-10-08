---
url: https://www.cloudflare.com/learning/access-management/security-service-edge-sse/
title: What is security service edge (SSE)?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:37.567059+00:00
---

# What is security service edge (SSE)?

> Source: https://www.cloudflare.com/learning/access-management/security-service-edge-sse/

[ Learning Center ](https://www.cloudflare.com/learning/) / access management

##  What is security service edge (SSE)? 

Security service edge (SSE) refers to the security components of the secure access service edge (SASE) model. SSE secures access to the Internet and to applications for remote users. 

[Learning Center](https://www.cloudflare.com/learning)/access management/[How to implement Zero Trust security](https://www.cloudflare.com/learning/access-management/how-to-implement-zero-trust/)[What is the principle of least privilege?](https://www.cloudflare.com/learning/access-management/principle-of-least-privilege/)[What is security service edge (SSE)?](https://www.cloudflare.com/learning/access-management/security-service-edge-sse/)[What is a software-defined perimeter? | SDP vs. VPN](https://www.cloudflare.com/learning/access-management/software-defined-perimeter/)[What is browser isolation?](https://www.cloudflare.com/learning/access-management/what-is-browser-isolation/)[What is microsegmentation?](https://www.cloudflare.com/learning/access-management/what-is-microsegmentation/)[What is ZTNA?](https://www.cloudflare.com/learning/access-management/what-is-ztna/)[What is a CASB?](https://www.cloudflare.com/learning/access-management/what-is-a-casb/)[SASE vs. SSE](https://www.cloudflare.com/learning/access-management/sase-vs-sse/)[What is data loss prevention?](https://www.cloudflare.com/learning/access-management/what-is-dlp/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand SSE and SASE 
  * List the three core components of SSE 
  * Learn about Cloudflare One 



Related content  [ What is ZTNA? ](https://www.cloudflare.com/learning/access-management/what-is-ztna/)[ What is a CASB? ](https://www.cloudflare.com/learning/access-management/what-is-a-casb/)[ What is browser isolation? ](https://www.cloudflare.com/learning/access-management/what-is-browser-isolation/)

On this page

  * Article Summary:

  * What is security service edge?

  * The networking side of SASE: WAN edge services

  * The security side of SASE: SSE

  * How does Cloudflare help organizations adopt SSE?

  * FAQs

    * What is security service edge?

    * What are the three core components of SSE?

    * How does SSE relate to the SASE model?

    * Why is SSE considered more effective than traditional network security?

    * What is the role of Zero Trust within an SSE framework?

    * In addition to the core components, what other features are often included in SSE?

    * How does Cloudflare assist businesses with SSE adoption?




## Article Summary:

  * SSE (security service edge) constitutes the security component of the larger SASE framework, designed specifically to protect access to the cloud for the remote workforce.

  * The security service edge architecture is built around three core components: Zero Trust Network Access (ZTNA), Secure Web Gateway (SWG), and Cloud Access Security Broker (CASB).

  * SSE enables the implementation of a strong Zero Trust security model by applying consistent security policies, like identity- and context-based access, regardless of user location.




## What is security service edge (SSE)?

Security service edge (SSE) is the security aspect of [secure access service edge (SASE)](https://www.cloudflare.com/learning/access-management/what-is-sase/). SASE is a [cloud](https://www.cloudflare.com/learning/cloud/what-is-the-cloud/)-native IT model that combines [wide area network (WAN)](https://www.cloudflare.com/learning/network-layer/what-is-a-wan/) edge networking and security services in a way that is better suited, compared to traditional network architectures, for how modern businesses operate.

SASE can be divided into two sets of interwoven capabilities: networking services and security services.

## The networking side of SASE: WAN edge services

Gartner, the research and advisory firm that first coined the term "SASE," considers wide area network (WAN) edge services, including [software-defined wide area networking (SD-WAN)](https://www.cloudflare.com/learning/network-layer/what-is-an-sd-wan/), to be the networking capability upon which SASE is built. WANs connect local networks across vast distances. Moving those capabilities to the edge better serves [branch offices](https://www.cloudflare.com/learning/network-layer/what-is-branch-networking/), mobile users, and cloud infrastructure. Edge-delivered WAN services are also more scalable and flexible than traditional, [MPLS](https://www.cloudflare.com/learning/network-layer/what-is-mpls/)-based WANs.

## The security side of SASE: SSE

SSE includes three core components, along with some additional capabilities:

  * [Zero Trust Network Access (ZTNA)](https://www.cloudflare.com/learning/access-management/what-is-ztna/): ZTNA, [according to Gartner](https://www.gartner.com/en/information-technology/glossary/zero-trust-network-access-ztna-), "creates an identity- and context-based, logical access boundary around an application or set of applications."

  * [Cloud access security broker (CASB)](https://www.cloudflare.com/learning/access-management/what-is-a-casb/): Includes a number of different [cloud security](https://www.cloudflare.com/learning/cloud/what-is-cloud-security/) technologies to protect [software as a service (SaaS)](https://www.cloudflare.com/learning/cloud/what-is-saas/) applications.

  * [Secure web gateway (SWG)](https://www.cloudflare.com/learning/access-management/what-is-a-secure-web-gateway/): Sits in between remote and office users and the Internet to apply acceptable use and security policies for threat and data protection.




Together, these areas make up SSE — with other security capabilities like [firewall-as-a-service (FWaaS)](https://www.cloudflare.com/learning/cloud/what-is-a-cloud-firewall/) and [remote browser isolation (RBI)](https://www.cloudflare.com/learning/access-management/what-is-browser-isolation/) often included as well. When cloud-centric edge WAN services and SSE are delivered from the same network architecture, an organization can fully deploy a SASE model.

## How does Cloudflare help organizations adopt SSE?

Cloudflare has a network with over 335+ locations around the world, and Cloudflare has long been a leader in security, network performance, and edge computing. The Cloudflare One platform includes all the aspects of SSE listed above, and it combines this with [network-as-a-service](https://www.cloudflare.com/learning/network-layer/network-as-a-service-naas/) for a full SASE [deployment](https://www.cloudflare.com/the-net/sase-network-transformation/).

[Learn more about Cloudflare One](https://www.cloudflare.com/cloudflare-one/).

## FAQs

#### What is security service edge (SSE)?

SSE is the specialized security component of the larger secure access service edge (SASE) framework. It is a cloud-based architecture designed to protect remote workers and branch offices. While SASE as a whole includes networking services, SSE focuses specifically on the security tools required to maintain a safe and reliable digital environment.

#### What are the three core components of SSE?

A standard SSE architecture is built on three primary pillars: Zero Trust Network Access (ZTNA), secure web gateway (SWG), and cloud access security broker (CASB).

#### How does SSE relate to the SASE model?

Think of SASE as a complete toolkit for modern business connectivity. It is divided into two halves: the networking side (often involving SD-WAN or WAN edge services) and the security side (SSE). When an organization combines these edge-delivered networking capabilities with the security protections of SSE within a single network architecture, they have achieved a full SASE deployment.

#### Why is SSE considered more effective than traditional network security?

Traditional security models often rely on a "castle-and-moat" approach that assumes anyone inside the office network is trustworthy. SSE is better suited for modern work because it is cloud-native and delivered at the edge, closer to where users actually are. This allows for more scalable, flexible protection that follows the user regardless of whether they are in a central office, at home, or traveling.

#### What is the role of Zero Trust within an SSE framework?

SSE is the primary vehicle for implementing a Zero Trust security model. SSE ensures that no user or device is trusted by default. Instead, access is strictly controlled through identity- and context-based policies, meaning a user only gets access to the specific applications they need to do their job, and only after their identity has been thoroughly verified.

#### In addition to the core components, what other features are often included in SSE?

Beyond the three main pillars, many SSE solutions include advanced security features such as firewall-as-a-service (FWaaS) and remote browser isolation (RBI). These tools provide additional layers of defense by filtering network traffic and executing web browsing in a contained cloud environment to prevent malware from reaching a user’s local device.

#### How does Cloudflare assist businesses with SSE adoption?

Cloudflare offers a comprehensive platform that delivers all the essential elements of SSE through a global network. By integrating these security services with its existing network-as-a-service capabilities, Cloudflare allows organizations to fully deploy a SASE model that optimizes both security and performance.
