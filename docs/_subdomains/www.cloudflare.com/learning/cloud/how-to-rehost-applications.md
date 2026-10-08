---
url: https://www.cloudflare.com/learning/cloud/how-to-rehost-applications/
title: How to rehost applications
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:27.760754+00:00
---

# How to rehost applications

> Source: https://www.cloudflare.com/learning/cloud/how-to-rehost-applications/

[ Learning Center ](https://www.cloudflare.com/learning/) / the cloud

##  How to rehost applications 

​​To rehost an application, migrate it between environments — typically from on-premises to cloud, or in some cases, back to on-premises for specialized workloads — without altering its core architecture or code. 

[Learning Center](https://www.cloudflare.com/learning)/the cloud/[What is application modernization?](https://www.cloudflare.com/learning/cloud/application-modernization/)[What is cloud-native security?](https://www.cloudflare.com/learning/cloud/cloud-native-security/)[How Cloudflare works with any cloud infrastructure](https://www.cloudflare.com/learning/cloud/cloudflare-and-the-cloud/)[What is a cloud-native application protection platform (CNAPP)?](https://www.cloudflare.com/learning/cloud/cnapp/)[How does hybrid cloud architecture work?](https://www.cloudflare.com/learning/cloud/how-does-hybrid-cloud-architecture-work/)[How to refactor applications](https://www.cloudflare.com/learning/cloud/how-to-refactor-applications/)[How to rehost applications](https://www.cloudflare.com/learning/cloud/how-to-rehost-applications/)[How to replatform applications](https://www.cloudflare.com/learning/cloud/how-to-replatform-applications/)[Multi-cloud vs. hybrid cloud: What's the difference?](https://www.cloudflare.com/learning/cloud/multicloud-vs-hybrid-cloud/)[Next-generation firewall (NGFW) vs. firewall-as-a-service (FWaaS)](https://www.cloudflare.com/learning/cloud/ngfw-vs-fwaas/)[Object storage vs. block storage: How are they different?](https://www.cloudflare.com/learning/cloud/object-storage-vs-block-storage/)[What are data egress fees?](https://www.cloudflare.com/learning/cloud/what-are-data-egress-fees/)[What is a connectivity cloud? | Connectivity cloud definition](https://www.cloudflare.com/learning/cloud/what-is-a-connectivity-cloud/)[What is a data lake?](https://www.cloudflare.com/learning/cloud/what-is-a-data-lake/)[What is a private cloud? | Private cloud vs. public cloud](https://www.cloudflare.com/learning/cloud/what-is-a-private-cloud/)[What is a public cloud? | Public vs. private cloud](https://www.cloudflare.com/learning/cloud/what-is-a-public-cloud/)[What is a virtual machine?](https://www.cloudflare.com/learning/cloud/what-is-a-virtual-machine/)[What is a virtual private cloud (VPC)?](https://www.cloudflare.com/learning/cloud/what-is-a-virtual-private-cloud/)[What is AWS data transfer pricing? ](https://www.cloudflare.com/learning/cloud/what-is-aws-data-transfer-pricing/)[What is blob storage?](https://www.cloudflare.com/learning/cloud/what-is-blob-storage/)[What is block storage?](https://www.cloudflare.com/learning/cloud/what-is-block-storage/)[What is cloud migration? | Cloud migration strategy](https://www.cloudflare.com/learning/cloud/what-is-cloud-migration/)[What is cloud networking?](https://www.cloudflare.com/learning/cloud/what-is-cloud-networking/)[How does cloud security work? | Cloud computing security](https://www.cloudflare.com/learning/cloud/what-is-cloud-security/)[What is cloud storage?](https://www.cloudflare.com/learning/cloud/what-is-cloud-storage/)[What is cloud security posture management (CSPM)?](https://www.cloudflare.com/learning/cloud/what-is-cspm/)[What is a cloud workload protection platform (CWPP)?](https://www.cloudflare.com/learning/cloud/what-is-cwpp/)[What is data migration? | Definition and common processes](https://www.cloudflare.com/learning/cloud/what-is-data-migration/)[What is digital transformation?](https://www.cloudflare.com/learning/cloud/what-is-digital-transformation/)[What is data security posture management (DSPM)?](https://www.cloudflare.com/learning/cloud/what-is-dspm/)[What is IaaS (infrastructure-as-a-service)?](https://www.cloudflare.com/learning/cloud/what-is-iaas/)[What is multi-cloud management?](https://www.cloudflare.com/learning/cloud/what-is-multicloud-management/)[What is multitenancy? | Multitenant architecture](https://www.cloudflare.com/learning/cloud/what-is-multitenancy/)[What is object storage?](https://www.cloudflare.com/learning/cloud/what-is-object-storage/)[What is SaaS? | SaaS definition](https://www.cloudflare.com/learning/cloud/what-is-saas/)[What is a SaaS management platform (SMP)? ](https://www.cloudflare.com/learning/cloud/what-is-smp/)[What is SaaS security posture management (SSPM)?](https://www.cloudflare.com/learning/cloud/what-is-sspm/)[What is the cloud?](https://www.cloudflare.com/learning/cloud/what-is-the-cloud/)[What is vendor lock-in? | Vendor lock-in and cloud computing](https://www.cloudflare.com/learning/cloud/what-is-vendor-lock-in/)[What is multicloud?](https://www.cloudflare.com/learning/cloud/what-is-multicloud/)[What is hybrid cloud?](https://www.cloudflare.com/learning/cloud/what-is-hybrid-cloud/)[What is a cloud firewall?](https://www.cloudflare.com/learning/cloud/what-is-a-cloud-firewall/)

######  Learning objectives 

After reading this article you will be able to: 

  * Identify ideal scenarios for rehosting applications to the cloud 
  * Learn best practices for planning and executing rehosting 
  * Understand infrastructure needs beyond compute during rehosting 



Related content  [ How to replatform applications ](https://www.cloudflare.com/learning/cloud/how-to-replatform-applications/)[ How to refactor applications ](https://www.cloudflare.com/learning/cloud/how-to-refactor-applications/)[ What is application modernization? ](https://www.cloudflare.com/learning/cloud/application-modernization/)[ What is cloud migration? | Cloud migration strategy ](https://www.cloudflare.com/learning/cloud/what-is-cloud-migration/)[ What is digital transformation? ](https://www.cloudflare.com/learning/cloud/what-is-digital-transformation/)

On this page

  * What is application rehosting?

    * Why organizations migrate applications to the cloud

    * How rehosting supports application modernization

    * Rehosting vs. replatforming vs. refactoring

  * What are some best practices for rehosting?

    * Assessment and planning

    * Identifying application dependencies

    * Evaluating cloud infrastructure needs

    * Choosing the right cloud provider

    * Testing and validation post-migration

    * Monitoring and scaling cloud resources

  * When to rehost applications

    * Ideal scenarios for rehosting

    * Business and technical factors that influence rehosting

    * Cost optimization in cloud migration

    * Managing cloud expenses post-migration

    * Security considerations in migration

    * The importance of preparation before rehosting

  * How Cloudflare supports application modernization

  * FAQs

    * What is application rehosting?

    * Why do organizations migrate applications to the cloud?

    * How does rehosting support application modernization?

    * What are the key differences between rehosting, replatforming, and refactoring applications?

    * What are some best practices for rehosting applications?

    * What are the ideal scenarios for rehosting?

    * How does rehosting impact cost optimization in cloud migration?

    * What are the security considerations during application rehosting?

    * Why is preparation important before rehosting an application?




## What is application rehosting?

Application rehosting, also referred to as “lift and shift,” is the process of moving an application from an on-premises environment to [the cloud](https://www.cloudflare.com/learning/cloud/what-is-the-cloud/) with little or no modification to its underlying architecture. This approach allows organizations to migrate workloads quickly without having to re-engineer or deeply modify their applications.

By relocating applications to cloud platforms, businesses can reduce their reliance on physical hardware, cut operational costs, and improve scalability and resilience.

#### Why organizations migrate applications to the cloud

There are several key drivers behind the shift to cloud environments:

  * **Scalability:** Cloud platforms offer elastic resources that adjust to demand

  * **Cost efficiency:** Moving to the cloud reduces overhead expenditures and shifts spending to a more flexible, pay-as-you-go model

  * **Resilience and availability:** Cloud infrastructure often provides built-in redundancy and disaster recovery capabilities

  * **Security and compliance:** Major cloud providers offer security features and certifications to support [compliance](https://www.cloudflare.com/learning/privacy/what-is-data-compliance/) needs

  * **Innovation:** [Cloud migration](https://www.cloudflare.com/learning/cloud/what-is-cloud-migration/) enables faster development cycles, easier integrations, and access to services like [AI, analytics, and serverless computing](https://www.cloudflare.com/learning/ai/what-is-artificial-intelligence/)




While most organizations migrate to the cloud to unlock these benefits, a significant minority — typically large enterprises with specialized workloads — are rehosting certain applications back to on-premises environments to meet unique performance, compliance, or cost considerations.

#### How rehosting supports application modernization

[Application modernization](https://www.cloudflare.com/learning/cloud/application-modernization/) refers to the process of updating and migrating existing software applications — and their underlying infrastructure — to better [support](https://www.cloudflare.com/the-net/modernizing-cloud-applications/) an organization's security, performance, and scalability needs. One common approach within this broader effort is rehosting.

While rehosting does not involve significant changes to the application itself, it unlocks the benefits of the cloud and helps support additional modernization efforts — like containerization, microservices adoption, or re-architecting.

In some cases, rehosting is the final step for legacy applications that do not require significant upgrades. In others, it serves as a transitional phase before deeper transformation.

#### Rehosting vs. replatforming vs. refactoring

There are several different ways to [approach](https://www.cloudflare.com/the-net/application-modernization-strategies-for-cxos/) modernizing applications, including:

  * **Rehosting:** Moving an application to the cloud (with minimal changes)

  * [Replatforming](https://www.cloudflare.com/learning/cloud/how-to-replatform-applications/): Making a few cloud-optimized changes — such as moving from a self-managed database to a managed cloud service — without altering core application code

  * [Refactoring](https://www.cloudflare.com/learning/cloud/how-to-refactor-applications/): Redesigning or rewriting an application to take advantage of cloud-native features, like containers or serverless computing




Each approach has trade-offs in terms of time, cost, and complexity. Rehosting offers speed and simplicity, making it a practical choice for organizations looking to reduce risk while accelerating their cloud adoption.

## What are some best practices for rehosting?

Rehosting is more than just moving application code from a server in a data center to a [virtual machine](https://www.cloudflare.com/learning/cloud/what-is-a-virtual-machine/) in the cloud. It is a structured process that includes planning, automation, testing, and scaling — not just of compute resources, but of the entire application infrastructure.

#### Assessment and planning

Before rehosting an application in cloud infrastructure, take time to understand what needs to be moved and how it interacts with other systems.

#### Identifying application dependencies

During the discovery phase, map out key application components and dependencies, such as a monolithic application binary (a single deployable unit containing all logic, like a JAR, WAR, or EXE), a server-rendered presentation layer (e.g., JSP, ASP.NET), business logic embedded directly in the application, and a [relational database](https://www.cloudflare.com/developer-platform/products/d1/) — often a single RDBMS like Oracle, SQL Server, or MySQL.

Also consider common dependencies including application servers (such as Tomcat, WebLogic, or IIS), external APIs, authentication systems, networking rules, hardcoded IPs or endpoints, and any other connected services. This list is not exhaustive, but it captures many of the typical elements found in traditional application architectures.

This step helps prevent surprises during migration and ensures all moving parts are accounted for.

#### Evaluating cloud infrastructure needs

Once key dependencies have been mapped, evaluate what the application needs in its new environment:

  * Compute and storage requirements

  * Latency sensitivity

  * Backup and recovery objectives

  * Regional availability zones

  * Bandwidth expectations under peak load




This is also the time to assess the supporting stack: [DNS](https://www.cloudflare.com/learning/dns/what-is-dns/), [CDN](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/), [DDoS protection](https://www.cloudflare.com/learning/ddos/ddos-mitigation/), and [observability](https://www.cloudflare.com/developer-platform/products/workers-observability/). Rehosting is an opportunity to modernize those layers, too.

#### Choosing the right cloud provider

Cloud providers play a major role in the long-term success of migration efforts. While compute pricing is often the first comparison point, look deeper.

When evaluating cloud or modernization partners, it is important to look for a provider that offers a comprehensive set of capabilities to support performance, security, and operational efficiency. This includes scalable backend services that can grow with demand without introducing unpredictable cost spikes, as well as integrated network-level security features like [web application firewalls (WAF)](https://www.cloudflare.com/learning/ddos/glossary/web-application-firewall-waf/), DDoS protection, and granular access controls.

A global content delivery network (CDN) is also essential to ensure fast, consistent delivery of both static and dynamic assets to users around the world. Providers should offer built-in DNS services that are not only fast and reliable, but also programmable to support automation and resilience.

Finally, native observability tools — or seamless integration with existing logging and monitoring stacks — are critical for maintaining visibility and control as applications scale and evolve.

#### Testing and validation post-migration

Migration success is when an application runs correctly, securely, and efficiently. After rehosting, it is important to benchmark key performance indicators like latency and throughput against the on-premises baseline to ensure the application meets user expectations. Running load tests can help simulate real-world demand and uncover issues that might not appear under normal conditions. Reviewing logs and alerts is also critical for identifying anomalies or misconfigurations that could impact reliability or security.

Beyond application performance, teams should also validate supporting infrastructure components — including DNS resolution, CDN behavior, [TLS](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/) configurations, and [firewall](https://www.cloudflare.com/learning/security/what-is-a-firewall/) rules — to confirm they are functioning as intended in the new environment.

As part of the migration cutover, traffic steering plays a key role in ensuring a smooth transition with no customer-facing downtime. Techniques such as DNS-based traffic shifting, weighted load balancing, and canary deployments can help gradually migrate users from the on-premises environment to the cloud-based version of the application. This allows teams to monitor system behavior in real time, identify issues early, and roll back changes if needed — all without disrupting end-user experience. Careful coordination of DNS TTLs, health checks, and monitoring coverage is essential to maintain service continuity during this critical phase.

#### Monitoring and scaling cloud resources

Scaling should be proactive. Consider autoscaling groups or serverless options if appropriate for current workloads. And monitor cloud spend — cost optimization in cloud migration doesn’t stop after applications are launched in the cloud.

Post-migration, [continuous observability](https://www.cloudflare.com/learning/performance/what-is-observability/) can help:

  * Detect performance issues early

  * Manage resource utilization

  * Identify security events




Implement cloud-native or third-party monitoring to support:

  * Application metrics (CPU, memory, errors)

  * Network flow and traffic anomalies

  * DNS performance and cache hit rates

  * CDN effectiveness (edge cache vs. origin pulls)




## When to rehost applications

Rehosting is often ideal when organizations need to migrate quickly, avoid heavy development effort, or extend the lifespan of a legacy system. It can also be the right fit for organizations looking to reduce physical infrastructure dependencies while beginning a broader IT infrastructure transformation.

#### Ideal scenarios for rehosting

Rehosting is most effective in scenarios where organizations have stable but expensive legacy applications that are becoming burdensome to maintain on-premises. It is also a strong fit when there is a need to exit a data center quickly, or when the priority is to move to the cloud with minimal disruption to the existing application codebase.

For teams planning broader modernization efforts down the line, rehosting can serve as a strategic first step — enabling foundational changes today while preserving flexibility for future refactoring. In these cases, rehosting helps extend the value of legacy applications without requiring immediate rewrites, effectively buying time to modernize further when the organization is ready.

#### Business and technical factors that influence rehosting

When evaluating rehosting as an application modernization path, consider:

  * **Time-to-cloud:** How quickly the organization needs to move applications to a new environment

  * **Budget constraints:** Whether current financial resources allow for rehosting efforts or setting the stage for replatforming or refactoring efforts in the future

  * **Operational continuity:** The organization’s tolerance for potential service interruptions during migration

  * **Staffing:** The availability of internal skills required to support deeper modernization initiatives




Rehosting can help manage risk and resource constraints by providing a relatively low-friction path to the cloud.

#### Cost optimization in cloud migration

Rehosting can deliver short-term cost optimization in cloud migration by reducing hardware maintenance and licensing costs, data center overhead, and infrastructure provisioning time. However, rehosting alone may not fully optimize long-term costs. Without refactoring or replatforming, applications may not use cloud-native efficiencies like autoscaling, serverless, or managed services.

In the short term, organizations can achieve fast ROI by eliminating capital expenditures and removing the need for physical infrastructure. Over the long term, however, realizing true cost efficiency requires deeper optimization — such as tuning compute usage, rightsizing instances, and decoupling monolithic services to improve scalability and resource allocation.

#### Managing cloud expenses post-migration

While rehosting can reduce some security risks, like reliance on patching vulnerable and outdated infrastructure, it also creates new ones. Applications that were secure in a controlled on-premises environment might be exposed in a less controlled cloud setting unless steps are taken to secure them properly via a [cloud-native security](https://www.cloudflare.com/learning/cloud/cloud-native-security/) platform.

Cost is another key consideration. Without proactive management, rehosted applications can generate higher-than-expected cloud bills. For example, [egress fees](https://www.cloudflare.com/learning/cloud/what-are-data-egress-fees/) — charges for moving data out of a cloud provider’s environment — can add up quickly, especially for data-intensive applications.

To avoid unexpected costs after migrating to the cloud, organizations should take a proactive approach to resource and cost management. This includes closely monitoring usage trends to identify patterns and anomalies, and establishing clear cost governance policies to define ownership and accountability. Automating tasks like rightsizing and scheduling of underutilized resources can help reduce waste and optimize spend. Additionally, setting budgets and alerts within cloud platforms provides early warning signals before costs exceed acceptable thresholds, helping teams stay in control as environments scale.

#### Security considerations in migration

Every migration strategy should incorporate security as a core consideration throughout the process, including:

  * [Encryption](https://www.cloudflare.com/learning/ssl/what-is-encryption/) of data in transit and at rest

  * [Access control and identity management](https://www.cloudflare.com/learning/access-management/what-is-identity-and-access-management/)

  * Compliance with relevant industry standards




#### The importance of preparation before rehosting

A successful rehost requires more than copying an app to the cloud. Poorly executed cutovers can result in:

  * Broken user experiences

  * Downtime during DNS propagation

  * [Latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/) or [availability](https://www.cloudflare.com/learning/performance/glossary/application-availability/) issues

  * Missed dependencies or outdated configuration




One common issue: customers or partners may rely on static [IP addresses](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/) tied to an application’s old data center. If those IP addresses are not updated on their side, traffic fails. Organizations must anticipate these dependencies and proactively coordinate with stakeholders to ensure a smooth cutover.

A well-planned rehost includes:

  * Communication plans with customers and partners

  * Testing environments and rollback options

  * Clear documentation of endpoint or infrastructure changes




## How Cloudflare supports application modernization

Cloudflare accelerates application modernization by transforming video and images, load balancing apps, and resolving DNS globally for fast, reliable performance. Automated protection defends against bots, DDoS, and zero-day attacks, while integrated observability ensures compliance across cloud environments. With these capabilities, Cloudflare strengthens every layer of the application stack for secure, high-performing, and future-ready modernization.

Learn more about [application modernization](https://www.cloudflare.com/learning/cloud/application-modernization/).

## FAQs

#### What is application rehosting?

Rehosting, also known as the "lift and shift" process, involves moving an application from one environment (typically from on-premises infrastructure) to a cloud platform, with minimal changes to its core architecture or code. Rehosting allows for rapid migration of workloads.

#### Why do organizations migrate applications to the cloud?

Organizations migrate applications to the cloud for several reasons, including: increased scalability due to elastic resources; improved cost efficiency through reduced overhead and a pay-as-you-go model; enhanced resilience and availability through built-in redundancy; robust security features and compliance certifications offered by major cloud providers; and accelerated innovation through access to advanced services like AI and serverless computing.

#### How does rehosting support application modernization?

Rehosting supports application modernization by moving existing applications to the cloud, enabling access to cloud benefits. While this process doesn't involve significant application changes, it can serve as a foundational step for further modernization efforts like containerization or rearchitecting. Or it can be a final step for legacy applications that don't require major upgrades.

#### What are the key differences between rehosting, replatforming, and refactoring applications?

Rehosting involves moving an application to the cloud with minimal changes. Replatforming entails making some cloud-optimized modifications, such as shifting from a self-managed database to a managed cloud service, without altering the core application code. Refactoring, on the other hand, means redesigning or rewriting an application to fully leverage cloud-native features like containers or serverless computing.

#### What are some best practices for rehosting applications?

Best practices for rehosting include: thorough assessment and planning to identify application dependencies; evaluation of cloud infrastructure needs (compute, storage, latency, backup, regional availability, bandwidth); selection of the right cloud provider based on comprehensive capabilities (not just pricing); rigorous testing and validation post-migration; and continuous monitoring and scaling of cloud resources.

#### What are the ideal scenarios for rehosting?

Rehosting is ideal when an organization needs to quickly migrate stable but expensive legacy applications from on-premises environments, or when the organization needs to exit a data center rapidly with minimal disruption to the existing codebase. It's also suitable as a strategic first step for teams planning more extensive modernization later, providing time and flexibility for future transformations.

#### How does rehosting impact cost optimization in cloud migration?

Rehosting can achieve short-term cost optimization by reducing hardware maintenance costs, licensing fees, data center overhead, and infrastructure provisioning time. However, to realize long-term cost efficiency, deeper optimization efforts like tuning compute usage, rightsizing instances, and decoupling services may be necessary, as rehosting alone doesn't fully leverage all cloud-native efficiencies.

#### What are the security considerations during application rehosting?

During application rehosting, it's crucial to consider new security risks that may arise in a less controlled cloud environment. Teams should ensure data encryption (both in transit and at rest); implement robust access control and identity management; and maintain compliance with relevant industry standards. A proactive approach with a cloud-native security platform is recommended.

#### Why is preparation important before rehosting an application?

Thorough preparation before rehosting is crucial to avoid issues like broken user experiences, downtime during domain name system (DNS) propagation, latency or availability problems, and missed dependencies. Preparation involves planning for potential challenges such as outdated IP addresses that customers or partners might rely on. A well-prepared rehosting strategy includes communicating plans with stakeholders, establishing testing environments with rollback options, and producing clear documentation with all changes.
