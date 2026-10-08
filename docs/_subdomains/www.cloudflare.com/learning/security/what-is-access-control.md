---
url: https://www.cloudflare.com/learning/security/what-is-access-control/
title: What is access control? | Authorization vs authentication | Cloudflare
method: crawl4ai+scrapegraph (scrapling: scrapling thin content (155 chars), fallback to crawl4ai)
fetched_at: 2026-10-08T08:04:53.067441+00:00
---

# What is access control? | Authorization vs authentication | Cloudflare

> Source: https://www.cloudflare.com/learning/security/what-is-access-control/

# What is access control? | Authorization vs authentication
Access control is a set of rules designed to determine who is granted access to a restricted location or restricted information.
#### Learning Objectives
After reading this article you will be able to:
  * Define access control
  * Differentiate between physical access control and information access control
  * Explain the difference between a VPN and a Zero Trust security solution


Related Content
* * *
[What is web application security?](https://www.cloudflare.com/learning/security/what-is-web-application-security/)[Buffer overflow attack](https://www.cloudflare.com/learning/security/threats/buffer-overflow/)[KRACK attack](https://www.cloudflare.com/learning/security/what-is-a-krack-attack/)[On-path attack](https://www.cloudflare.com/learning/security/threats/on-path-attack/)[Phishing attack](https://www.cloudflare.com/learning/access-management/phishing-attack/)
#### Want to keep learning?
Subscribe to theNET, Cloudflare's monthly recap of the Internet's most popular insights!
Subscribe to theNET
Refer to Cloudflare's [Privacy Policy](https://www.cloudflare.com/privacypolicy/) to learn how we collect and process your personal data.
Copy article link
## Article Summary:
  * Access control is a fundamental security process that regulates who can view or use resources, effectively mitigating data breach risks by authenticating and authorizing user identities.
  * Organizations implement various access control models, such as Role-Based (RBAC) or Mandatory (MAC), to manage permissions and protect sensitive information within physical and digital environments.
  * Modern access control systems often utilize Zero Trust security and Single Sign-On (SSO) to continuously verify users, ensuring only authorized individuals reach internal applications and data.


## What is access control?
![Access Control](https://cf-assets.www.cloudflare.com/slt3lc6tev37/YiKHwui8iUBOpAWIAvvmX/5cbff68eb37d189e8a6f093223c4477f/access-control.png)
Access control is a security term used to refer to a set of policies for restricting access to information, tools, and physical locations.
## What is physical access control?
Although this article focuses on information access control, physical access control is a useful comparison for understanding the overall concept.
Physical access control is a set of policies to control who is granted access to a physical location. Real-world examples of physical access control include the following:
  * Bar-room bouncers
  * Subway turnstiles
  * Airport customs agents
  * Keycard or badge scanners in corporate offices


In all of these examples, a person or device is following a set of policies to decide who gets access to a restricted physical location. For example, a hotel keycard scanner only grants access to authorized guests who have a hotel key.
## What is information access control?
Information access control restricts access to data and the software used to manipulate that data. Examples include the following:
  * Signing into a laptop using a password
  * Unlocking a smartphone with a thumbprint scan
  * Remotely accessing an employer’s internal network using a VPN


In all of these cases, software is used to authenticate and grant authorization to users who need to access digital information. [Authentication and authorization](https://www.cloudflare.com/learning/access-management/authn-vs-authz/) are integral components of information access control.
## What’s the difference between authentication and authorization?
[Authentication](https://www.cloudflare.com/learning/access-management/what-is-authentication/) is the security practice of confirming that someone is who they claim to be, while authorization is the process of determining which level of access each user is granted.
For example, think of a traveller checking into a hotel. When they register at the front desk, they are asked to provide a passport to verify that they are the person whose name is on the reservation. This is an example of authentication.
Once the hotel employee has authenticated the guest, the guest receives a keycard with limited privileges. This is an example of authorization. The guest’s keycard grants them access to their room, the guest elevator, and the pool — but not other guests’ rooms or the service elevator. Hotel employees, on the other hand, are authorized to access more areas of the hotel than guests are.
Computer and networking systems have similar authentication and authorization controls. When a user signs into their email or online banking account, they use a login and password combination that only they are supposed to know. The software uses this information to authenticate the user. Some applications have much stricter authorization requirements than others; while a password is enough for some, others may require [two-factor authentication](https://www.cloudflare.com/learning/access-management/what-is-two-factor-authentication/) or a biometrical confirmation, such as a thumbprint or face ID scan.
Once authenticated, a user can only see the information they are authorized to access. In the case of an online banking account, the user can only see information related to their personal banking account. Meanwhile, a fund manager at the bank can log in to the same application and see data on the bank’s overall financial holdings. Since the bank handles very sensitive personal information, it’s entirely possible that no one has unrestricted access to the data. Even the bank’s president or head of security may need to go through a security protocol to access the full data of individual customers.
## What are the primary types of access control?
After the authentication process has been completed, user authorization can be determined in one of several ways:
**Mandatory access control (MAC):** Mandatory access control establishes strict security policies for individual users and the resources, systems, or data they are allowed to access. These policies are controlled by an administrator; individual users are not given the authority to set, alter, or revoke permissions in a way that contradicts existing policies.
Under this system, both the subject (user) and the object (data, system, or other resource) must be assigned similar security attributes in order to interact with each other. Returning to the previous example, the bank’s president would not only need the correct security clearance to access customer data files, but the system administrator would need to specify that those files can be viewed and altered by the president. While that process may seem redundant, it ensures that users cannot perform unauthorized actions simply by gaining access to certain data or resources.
**Role-based access control (RBAC):** [Role-based access control](https://www.cloudflare.com/learning/access-management/role-based-access-control-rbac/) establishes permissions based on groups (defined sets of users, such as bank employees) and roles (defined sets of actions, like those that a bank teller or a branch manager might perform). Individuals can perform any action that is assigned to their role, and may be assigned multiple roles as necessary. Like MAC, users are not permitted to change the level of access control that has been assigned to their role.
For instance, any bank employee assigned to the role of bank teller might be given the authorization to process account transactions and open new customer accounts. A branch manager, on the other hand, might hold several roles, authorizing them to process account transactions, open customer accounts, assign the role of bank teller to a new employee, and so on.
**Discretionary access control (DAC):** Once a user is given permission to access an object (usually by a system administrator or through an existing access control list), they can grant access to other users on an as-needed basis. This may introduce security vulnerabilities, however, as users are able to determine security settings and share permissions without strict oversight from the system administrator.
When evaluating which method of user authorization is most appropriate for an organization, security needs must be taken into account. Typically, organizations that require a high level of data confidentiality (e.g. government organizations, banks, etc.) will opt for more stringent forms of access control, like MAC, while those that favor more flexibility and user or role-based permissions will tend toward RBAC and DAC systems.
## What are some methods for implementing access control?
A popular tool for information access control is a [virtual private network (VPN)](https://www.cloudflare.com/learning/access-management/what-is-a-vpn/). A VPN is a service that allows remote users to access the Internet as though they were connected to a private network. Corporate networks will often use VPNs to manage access control to their internal network across a geographic distance.
For example, if a company has an office in San Francisco and another office in New York, as well as remote employees scattered across the globe, they can use a VPN so that all of their employees can securely log into their internal network, regardless of their physical location. Connecting to the VPN will also help protect the employees against [on-path attacks](https://www.cloudflare.com/learning/security/threats/on-path-attack/) if they are connected to a public WiFi network.
VPNs also come with some drawbacks. For example, VPNs negatively impact performance. When connected to a VPN, every data packet a user sends or receives has to travel an extra distance before arriving at its destination, as each request and response has to hit the VPN server before reaching its destination. This process often increases [latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/).
VPNs generally provide an all-or-nothing approach to network security. VPNs are great at providing authentication, but not great at providing granular authorization controls. If an organization wants to grant different levels of access to different employees, they have to use multiple VPNs. This creates a lot of complexity, and still doesn’t satisfy the requirements of [Zero Trust security](https://www.cloudflare.com/learning/security/glossary/what-is-zero-trust/).
## What is Zero Trust security?
Zero Trust security is an IT security model that requires strict identity verification for every person and device trying to access resources on a private network, regardless of whether they are sitting within or outside of the [network perimeter](https://www.cloudflare.com/learning/access-management/what-is-the-network-perimeter/). Zero Trust networks also utilize [microsegmentation](https://www.cloudflare.com/learning/access-management/what-is-microsegmentation/). Microsegmentation is the practice of breaking up security perimeters into small zones to maintain separate access for separate parts of the network.
Today many organizations are replacing VPNs with [SASE solutions](https://www.cloudflare.com/sase/use-cases/) like [Cloudflare One](https://www.cloudflare.com/zero-trust/). A SASE security solution can be used to manage access control both for in-office and remote employees, while avoiding the major drawbacks of using a VPN.
## FAQs
#### What is access control?
Access control refers to policies that limit who can enter locations or interact with digital information and tools. It acts as a safeguard to ensure only authorized individuals can reach restricted areas.
#### What is the difference between authentication and authorization?
Authentication is the practice of verifying that a person is truly who they claim to be. Authorization is the subsequent process of determining what specific resources or areas that person is allowed to access.
#### How does mandatory access control (MAC) function?
Mandatory access control relies on strict security policies set by a central administrator rather than individual users. For a user to interact with a specific resource, both the person and the data must have matching security attributes assigned to them.
#### What is role-based access control (RBAC)?
This method assigns permissions based on specific roles and groups within an organization. An employee assigned a given role can perform actions associated with that role, but they cannot change the access levels inherent to that role.
#### How does discretionary access control (DAC) differ from other methods?
In a DAC system, users who have been granted access to a certain object can pass that permission along to others as they see fit. While flexible, this approach can lead to security gaps because it lacks the centralized oversight found in MAC or RBAC.
#### Why are organizations moving from VPNs to Zero Trust security?
While VPNs enforce authentication, they often lack granular authorization controls. They also can slow down performance by requiring data to travel extra distances to VPN servers. Zero Trust security addresses these issues by requiring strict verification for every person and device, and by enforcing security policies at the network edge, instead of via remote VPN servers.
#### What is the benefit of microsegmentation in access control?
Microsegmentation is the security practice of dividing a network into smaller, isolated zones. This allows an organization to maintain separate authorization for different parts of the network, ensuring that a user only reaches the specific resources they need.
GETTING STARTED
  * [Free plans](https://www.cloudflare.com/plans/free/)
  * [Small business plans](https://www.cloudflare.com/small-business/)
  * [For enterprises](https://www.cloudflare.com/enterprise/)
  * [Get a recommendation](https://www.cloudflare.com/about-your-website/)
  * [Request a demo](https://www.cloudflare.com/plans/enterprise/demo/)
  * [Contact sales](https://www.cloudflare.com/plans/enterprise/contact/)


About Access Management 
  * [What is IAM? ](https://www.cloudflare.com/learning/access-management/what-is-identity-and-access-management/)
  * [Access control](https://www.cloudflare.com/learning/access-management/what-is-access-control/)
  * [Network perimeter](https://www.cloudflare.com/learning/access-management/what-is-the-network-perimeter/)


About Zero Trust
  * [Zero Trust security](https://www.cloudflare.com/learning/security/glossary/what-is-zero-trust/)
  * [Two-factor authentication ](https://www.cloudflare.com/learning/access-management/what-is-two-factor-authentication/)
  * [Role-based access control (RBAC)](https://www.cloudflare.com/learning/access-management/role-based-access-control-rbac/)
  * [Multi-factor authentication](https://www.cloudflare.com/learning/access-management/what-is-multi-factor-authentication/)
  * [What is SAML?](https://www.cloudflare.com/learning/access-management/what-is-saml/)
  * [Remote workforce security](https://www.cloudflare.com/learning/access-management/remote-workforce-security/)
  * [What is OAuth?](https://www.cloudflare.com/learning/access-management/what-is-oauth/)
  * [Browser isolation](https://www.cloudflare.com/learning/access-management/what-is-browser-isolation/)
  * [Castle-and-moat security](https://www.cloudflare.com/learning/access-management/castle-and-moat-network-security/)
  * [Mutual TLS (mTLS)](https://www.cloudflare.com/learning/access-management/what-is-mutual-tls/)
  * [What is ZTNA?](https://www.cloudflare.com/learning/access-management/what-is-ztna/)
  * [Principle of least privilege](https://www.cloudflare.com/learning/access-management/principle-of-least-privilege/)
  * [Security service edge (SSE)](https://www.cloudflare.com/learning/access-management/security-service-edge-sse/)
  * [Microsegmentation](https://www.cloudflare.com/learning/access-management/what-is-microsegmentation/)
  * [How to implement Zero Trust](https://www.cloudflare.com/learning/access-management/how-to-implement-zero-trust/)


VPN Resources
  * [VPN](https://www.cloudflare.com/learning/access-management/what-is-a-vpn/)
  * [Business VPN ](https://www.cloudflare.com/learning/access-management/what-is-a-business-vpn/)
  * [VPN security](https://www.cloudflare.com/learning/access-management/vpn-security/)
  * [VPN speed](https://www.cloudflare.com/learning/access-management/vpn-speed/)


Glossary
  * [What is account takeover?](https://www.cloudflare.com/learning/access-management/account-takeover/)
  * [What is authentication?](https://www.cloudflare.com/learning/access-management/what-is-authentication/)
  * [Authn vs. Authz](https://www.cloudflare.com/learning/access-management/authn-vs-authz/)
  * [What is a CASB?](https://www.cloudflare.com/learning/access-management/what-is-a-casb/)
  * [Data loss prevention (DLP)](https://www.cloudflare.com/learning/access-management/what-is-dlp/)
  * [DNS filtering](https://www.cloudflare.com/learning/access-management/what-is-dns-filtering/)
  * [GDPR remote access](https://www.cloudflare.com/learning/access-management/gdpr-remote-access/)
  * [Identity](https://www.cloudflare.com/learning/access-management/what-is-identity/)
  * [Identity as a service](https://www.cloudflare.com/learning/access-management/what-is-identity-as-a-service/)
  * [Identity provider (IdP)](https://www.cloudflare.com/learning/access-management/what-is-an-identity-provider/)
  * [What is an insider threat?](https://www.cloudflare.com/learning/access-management/what-is-an-insider-threat/)
  * [Mutual authentication](https://www.cloudflare.com/learning/access-management/what-is-mutual-authentication/)
  * [Network segmentation](https://www.cloudflare.com/learning/access-management/what-is-network-segmentation/)
  * [Phishing attack](https://www.cloudflare.com/learning/access-management/phishing-attack/)
  * [What is the RDP?](https://www.cloudflare.com/learning/access-management/what-is-the-remote-desktop-protocol/)
  * [RDP security](https://www.cloudflare.com/learning/access-management/rdp-security-risks/)
  * [Secure web gateway](https://www.cloudflare.com/learning/access-management/what-is-a-secure-web-gateway/)
  * [What is shadow IT?](https://www.cloudflare.com/learning/access-management/what-is-shadow-it/)
  * [Software-defined perimeter](https://www.cloudflare.com/learning/access-management/software-defined-perimeter/)
  * [Spear phishing](https://www.cloudflare.com/learning/access-management/spear-phishing/)
  * [What is SSO?](https://www.cloudflare.com/learning/access-management/what-is-sso/)
  * [Token-based authentication](https://www.cloudflare.com/learning/access-management/token-based-authentication/)
  * [URL filtering](https://www.cloudflare.com/learning/access-management/what-is-url-filtering/)
  * [Coffee shop networking](https://www.cloudflare.com/learning/access-management/coffee-shop-networking/)
  * [Smishing](https://www.cloudflare.com/learning/access-management/smishing/)
  * [Whale phishing](https://www.cloudflare.com/learning/access-management/whaling-attack/)
  * [Risk-based authentication](https://www.cloudflare.com/learning/access-management/risk-based-authentication/)
  * [DNS filtering for AI security](https://www.cloudflare.com/learning/access-management/dns-filtering-for-ai-security/)
  * [DNS filtering for guest WiFi](https://www.cloudflare.com/learning/access-management/how-to-secure-guest-wifi-dns-filtering/)
  * [DNS filtering for IoT](https://www.cloudflare.com/learning/access-management/dns-filtering-for-iot/)


Learning Center Navigation
  * [Learning Center Home](https://www.cloudflare.com/learning/)
  * [DDoS Learning Center](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/)
  * [CDN Learning Center](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)
  * [What is DNS Learning Center](https://www.cloudflare.com/learning/dns/what-is-dns/)
  * [Serverless Learning Center](https://www.cloudflare.com/learning/serverless/what-is-serverless/)
  * [SSL Learning Center](https://www.cloudflare.com/learning/ssl/what-is-ssl/)
  * [Security Learning Center](https://www.cloudflare.com/learning/security/what-is-web-application-security/)
  * [Performance Learning Center](https://www.cloudflare.com/learning/performance/why-site-speed-matters/)
  * [Cloud Learning Center](https://www.cloudflare.com/learning/cloud/what-is-the-cloud/)
  * [Bots Learning Center](https://www.cloudflare.com/learning/bots/what-is-a-bot/)
  * [Network Layer Learning Center](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)
  * [Privacy Learning Center](https://www.cloudflare.com/learning/privacy/what-is-data-privacy/)
  * [Video Streaming Learning Center](https://www.cloudflare.com/learning/video/what-is-streaming/)
  * [What is SASE?](https://www.cloudflare.com/learning/access-management/what-is-sase/)
  * [Email Security Learning Center](https://www.cloudflare.com/learning/email-security/what-is-email-security/)
  * [AI Learning Center](https://www.cloudflare.com/learning/ai/what-is-artificial-intelligence/)


[](https://www.facebook.com/cloudflare "Facebook")[](https://x.com/cloudflare "X")[](https://www.linkedin.com/company/cloudflare "LinkedIn")[](https://www.youtube.com/cloudflare "Youtube")[](https://instagram.com/cloudflare "Instagram")
© 2026 Cloudflare, Inc.[Privacy Policy](https://www.cloudflare.com/privacypolicy/)[Terms of Use](https://www.cloudflare.com/website-terms/)[Report Security Issues](https://www.cloudflare.com/disclosure/)![privacy options](https://www.cloudflare.com/img/privacyoptions.svg)Cookie Preferences[Trademark](https://www.cloudflare.com/trademark/)
