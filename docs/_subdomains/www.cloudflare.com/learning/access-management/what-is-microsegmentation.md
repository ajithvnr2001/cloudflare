---
url: https://www.cloudflare.com/learning/access-management/what-is-microsegmentation/
title: What is microsegmentation?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:06.161883+00:00
---

# What is microsegmentation?

> Source: https://www.cloudflare.com/learning/access-management/what-is-microsegmentation/

[ Learning Center ](https://www.cloudflare.com/learning/) / access management

##  What is microsegmentation? 

Microsegmentation is a technique for dividing a network into separate segments at the application layer in order to increase security and reduce the impact of a breach. 

[Learning Center](https://www.cloudflare.com/learning)/access management/[How to implement Zero Trust security](https://www.cloudflare.com/learning/access-management/how-to-implement-zero-trust/)[What is the principle of least privilege?](https://www.cloudflare.com/learning/access-management/principle-of-least-privilege/)[What is security service edge (SSE)?](https://www.cloudflare.com/learning/access-management/security-service-edge-sse/)[What is a software-defined perimeter? | SDP vs. VPN](https://www.cloudflare.com/learning/access-management/software-defined-perimeter/)[What is browser isolation?](https://www.cloudflare.com/learning/access-management/what-is-browser-isolation/)[What is microsegmentation?](https://www.cloudflare.com/learning/access-management/what-is-microsegmentation/)[What is ZTNA?](https://www.cloudflare.com/learning/access-management/what-is-ztna/)[What is a CASB?](https://www.cloudflare.com/learning/access-management/what-is-a-casb/)[SASE vs. SSE](https://www.cloudflare.com/learning/access-management/sase-vs-sse/)[What is data loss prevention?](https://www.cloudflare.com/learning/access-management/what-is-dlp/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define microsegmentation 
  * Explain how microsegmentation improves security 
  * Describe how microsegmentation fits into a Zero Trust architecture 



Related content  [ What is ZTNA? ](https://www.cloudflare.com/learning/access-management/what-is-ztna/)[ What is the principle of least privilege? ](https://www.cloudflare.com/learning/access-management/principle-of-least-privilege/)

On this page

  * What is microsegmentation?

  * Where does microsegmentation occur?

  * How does microsegmentation work?

    * Application layer visibility

    * Software-based, not hardware-based

    * Use of next-generation firewalls

    * Security policies differ across segments

    * Visibility of all network traffic

  * How does microsegmentation improve security?

  * What are the other components of a Zero Trust network?

  * FAQs

    * What is network segmentation?

    * What is Zero Trust architecture?

    * How does microsegmentation prevent lateral movement?

    * What is application layer visibility in microsegmentation?

    * How do next-generation firewalls support microsegmentation?

    * What is workload isolation in microsegmentation?




## What is microsegmentation?

Microsegmentation divides a [network](https://www.cloudflare.com/learning/network-layer/enterprise-networking/) into small, discrete sections, each of which has its own security policies and is accessed separately. The goal of microsegmentation is to [increase network security](https://www.cloudflare.com/network-security/) by confining threats and [breaches](https://www.cloudflare.com/learning/security/what-is-a-data-breach/) to the compromised segment, without impacting the rest of the network.

Large ships are often divided into compartments below deck, each of which is watertight and can be sealed off from the others. This way, even if a leak fills one compartment with water, the rest of the compartments remain dry, and the ship stays afloat. The concept of network microsegmentation is similar: one segment of the network may become compromised, but it can be easily sealed off from the rest of the network.

Microsegmentation is a key component of a [Zero Trust](https://www.cloudflare.com/learning/security/glossary/what-is-zero-trust/) architecture. Such an architecture assumes that any traffic moving into, out of, or within a network could be a threat. Microsegmentation makes it possible to isolate those threats before they spread, preventing [lateral movement](https://www.cloudflare.com/learning/security/glossary/what-is-lateral-movement/).

## Where does microsegmentation occur?

Organizations can microsegment both on-premises data centers and [cloud computing](https://www.cloudflare.com/learning/cloud/what-is-the-cloud/) deployments — any place where workloads run. Servers, [virtual machines](https://www.cloudflare.com/learning/cloud/what-is-a-virtual-machine/), [containers](https://www.cloudflare.com/learning/serverless/serverless-vs-containers/), and [microservices](https://www.cloudflare.com/learning/serverless/glossary/serverless-microservice/) can all be segmented in this fashion, each with their own security policy.

Microsegmentation can occur on extremely granular levels in a network, all the way down to isolating individual workloads (as opposed to isolating applications, devices, or networks), with a "workload" being any program or application that uses some amount of memory and CPU.

## How does microsegmentation work?

Techniques for microsegmenting a network vary slightly. But a few key principles almost always apply:

#### Application layer visibility

Microsegmentation solutions are aware of the applications that are sending traffic on the network. Microsegmentation provides context into which applications are communicating with each other and how network traffic flows between them. This is one of the aspects that makes microsegmentation distinct from dividing a network using virtual [local area networks](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/) (VLANs) or another [network layer](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/) method.

#### Software-based, not hardware-based

Microsegmentation is configured via software. Segmentation is virtual, so admins do not need to adjust [routers](https://www.cloudflare.com/learning/network-layer/what-is-a-router/), [switches](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/), or other network equipment in order to implement it.

#### Use of next-generation firewalls (NGFWs)

Most microsegmentation solutions use [next-generation firewalls (NGFWs)](https://www.cloudflare.com/learning/security/what-is-next-generation-firewall-ngfw/) to separate out their segments. NGFWs, unlike traditional [firewalls](https://www.cloudflare.com/learning/security/what-is-a-firewall/), have application awareness, enabling them to analyze network traffic at the [application layer](https://www.cloudflare.com/learning/ddos/what-is-layer-7/), not just the network and transport layers.

In addition, [cloud-based firewalls](https://www.cloudflare.com/learning/cloud/what-is-a-cloud-firewall/) may be used to microsegment cloud computing deployments. Some cloud hosting providers offer this ability using their built-in firewall services.

#### Security policies differ across segments

Admins can customize security policies for each workload if desired. One workload can allow broad access, while another can be highly restricted, depending on the given workload's importance and the data it processes. One workload can accept [API](https://www.cloudflare.com/learning/security/api/what-is-an-api/) queries from a range of [endpoints](https://www.cloudflare.com/learning/security/api/what-is-api-endpoint/); another may only communicate with a specific server.

#### Visibility of all network traffic

Typical network logging provides network and transport layer information such as [ports](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/) and [IP addresses](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/). Microsegmentation also provides application and workload context. By monitoring all network traffic and adding application context, organizations can consistently apply segmentation and security policies across their networks. This also provides the information needed to tweak security policies as needed.

## How does microsegmentation improve security?

Microsegmentation prevents threats from spreading across an entire network, limiting the damage from a cyber attack. Attackers' access is limited and they may not be able to reach confidential data.

For example, a network with workloads running in a microsegmented data center may contain dozens of separate, secure zones. A user with access to one zone needs separate authorization for each of the other zones. This minimizes the risks of privilege escalation (when a user has too much access) and [insider threats](https://www.cloudflare.com/learning/access-management/what-is-an-insider-threat/) (when users knowingly or unknowingly compromise the security of confidential data).

As another example, suppose one container has a vulnerability. The attacker exploits this vulnerability via malicious code and can now alter data within the container. In a network protected only on the [perimeter](https://www.cloudflare.com/learning/access-management/what-is-the-network-perimeter/), the attacker could move laterally to other parts of the network, escalate privileges, and eventually extract or alter highly valuable data. In a microsegmented network, the attacker more than likely cannot do so without finding a separate entry point.

## What are the other components of a Zero Trust network?

_Zero Trust_ is a philosophy and approach to [network security](https://www.cloudflare.com/the-net/future-of-networking/) that assumes threats are already present both inside and outside of a secure environment. Many organizations are adopting a Zero Trust architecture in order to both prevent attacks and minimize the damage from successful attacks.

While microsegmentation is a key component of a Zero Trust strategy, it is not the only one. Other Zero Trust principles include:

  * **Continuous monitoring and validation:** No devices or users are trusted automatically, even those that have already been [authenticated](https://www.cloudflare.com/learning/access-management/what-is-authentication/). Logins and connections time out periodically, continuously re-verifying users and devices

  * [Principle of least privilege:](https://www.cloudflare.com/learning/access-management/principle-of-least-privilege/) Users only have access to the systems and data that are absolutely necessary

  * **Device access control:** Device access is tracked and restricted just like user access

  * [Multi-factor authentication (MFA):](https://www.cloudflare.com/learning/access-management/what-is-multi-factor-authentication/) Authentication takes place using at least two [identity](https://www.cloudflare.com/learning/access-management/what-is-identity/) factors, instead of only relying on passwords, security questions, or other knowledge-based methods




To learn about how Cloudflare helps organizations [implement these components](https://www.cloudflare.com/learning/access-management/how-to-implement-zero-trust/), read about the [Cloudflare Zero Trust](https://www.cloudflare.com/zero-trust/) platform.

## FAQs

#### What is network segmentation?

Network segmentation is the process of dividing a network into smaller, isolated sections with separate security policies. This helps contain threats so that they do not spread across the rest of the network.

#### What is Zero Trust architecture?

Zero Trust architecture is a security approach that assumes threats are likely present both inside and outside an organization's network. It implements principles and techniques such as microsegmentation, continuous validation, least-privilege access, and multi-factor authentication (MFA) in order to both prevent and contain cyber attacks..

#### How does microsegmentation prevent lateral movement?

Microsegmentation creates isolated network segments, so even if attackers gain access to one segment, they cannot easily move to others. This limits the attacker's ability to spread to other accounts, systems, and devices within the network.

#### What is application layer visibility in microsegmentation?

Microsegmentation solutions have application layer visibility: they are aware of which applications are communicating and how network traffic flows between them. This enables more precise monitoring and enforcement of security policies compared to network-layer approaches that are application-agnostic, like the use of VLANs.

#### How do next-generation firewalls (NGFWs) support microsegmentation?

Next-generation firewalls (NGFWs) provide application-layer awareness, allowing organizations to segment networks more effectively.

#### What is workload isolation in microsegmentation?

Workload isolation refers to the ability to segment and protect individual programs or applications within a network, so each has its own tailored security policy. This prevents threats from spreading between workloads.
