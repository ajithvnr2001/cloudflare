---
url: https://www.cloudflare.com/learning/cloud/what-is-multitenancy/
title: What Is Multitenancy? | Multitenant Architecture
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:07.943507+00:00
---

# What Is Multitenancy? | Multitenant Architecture

> Source: https://www.cloudflare.com/learning/cloud/what-is-multitenancy/

[ Learning Center ](https://www.cloudflare.com/learning/) / the cloud

##  What is multitenancy? | Multitenant architecture 

Multitenancy is when several different cloud customers are accessing the same computing resources, such as when several different companies are storing data on the same physical server. 

[Learning Center](https://www.cloudflare.com/learning)/the cloud/[What is application modernization?](https://www.cloudflare.com/learning/cloud/application-modernization/)[What is cloud-native security?](https://www.cloudflare.com/learning/cloud/cloud-native-security/)[How Cloudflare works with any cloud infrastructure](https://www.cloudflare.com/learning/cloud/cloudflare-and-the-cloud/)[What is a cloud-native application protection platform (CNAPP)?](https://www.cloudflare.com/learning/cloud/cnapp/)[How does hybrid cloud architecture work?](https://www.cloudflare.com/learning/cloud/how-does-hybrid-cloud-architecture-work/)[How to refactor applications](https://www.cloudflare.com/learning/cloud/how-to-refactor-applications/)[How to rehost applications](https://www.cloudflare.com/learning/cloud/how-to-rehost-applications/)[How to replatform applications](https://www.cloudflare.com/learning/cloud/how-to-replatform-applications/)[Multi-cloud vs. hybrid cloud: What's the difference?](https://www.cloudflare.com/learning/cloud/multicloud-vs-hybrid-cloud/)[Next-generation firewall (NGFW) vs. firewall-as-a-service (FWaaS)](https://www.cloudflare.com/learning/cloud/ngfw-vs-fwaas/)[Object storage vs. block storage: How are they different?](https://www.cloudflare.com/learning/cloud/object-storage-vs-block-storage/)[What are data egress fees?](https://www.cloudflare.com/learning/cloud/what-are-data-egress-fees/)[What is a connectivity cloud? | Connectivity cloud definition](https://www.cloudflare.com/learning/cloud/what-is-a-connectivity-cloud/)[What is a data lake?](https://www.cloudflare.com/learning/cloud/what-is-a-data-lake/)[What is a private cloud? | Private cloud vs. public cloud](https://www.cloudflare.com/learning/cloud/what-is-a-private-cloud/)[What is a public cloud? | Public vs. private cloud](https://www.cloudflare.com/learning/cloud/what-is-a-public-cloud/)[What is a virtual machine?](https://www.cloudflare.com/learning/cloud/what-is-a-virtual-machine/)[What is a virtual private cloud (VPC)?](https://www.cloudflare.com/learning/cloud/what-is-a-virtual-private-cloud/)[What is AWS data transfer pricing? ](https://www.cloudflare.com/learning/cloud/what-is-aws-data-transfer-pricing/)[What is blob storage?](https://www.cloudflare.com/learning/cloud/what-is-blob-storage/)[What is block storage?](https://www.cloudflare.com/learning/cloud/what-is-block-storage/)[What is cloud migration? | Cloud migration strategy](https://www.cloudflare.com/learning/cloud/what-is-cloud-migration/)[What is cloud networking?](https://www.cloudflare.com/learning/cloud/what-is-cloud-networking/)[How does cloud security work? | Cloud computing security](https://www.cloudflare.com/learning/cloud/what-is-cloud-security/)[What is cloud storage?](https://www.cloudflare.com/learning/cloud/what-is-cloud-storage/)[What is cloud security posture management (CSPM)?](https://www.cloudflare.com/learning/cloud/what-is-cspm/)[What is a cloud workload protection platform (CWPP)?](https://www.cloudflare.com/learning/cloud/what-is-cwpp/)[What is data migration? | Definition and common processes](https://www.cloudflare.com/learning/cloud/what-is-data-migration/)[What is digital transformation?](https://www.cloudflare.com/learning/cloud/what-is-digital-transformation/)[What is data security posture management (DSPM)?](https://www.cloudflare.com/learning/cloud/what-is-dspm/)[What is IaaS (infrastructure-as-a-service)?](https://www.cloudflare.com/learning/cloud/what-is-iaas/)[What is multi-cloud management?](https://www.cloudflare.com/learning/cloud/what-is-multicloud-management/)[What is multitenancy? | Multitenant architecture](https://www.cloudflare.com/learning/cloud/what-is-multitenancy/)[What is object storage?](https://www.cloudflare.com/learning/cloud/what-is-object-storage/)[What is SaaS? | SaaS definition](https://www.cloudflare.com/learning/cloud/what-is-saas/)[What is a SaaS management platform (SMP)? ](https://www.cloudflare.com/learning/cloud/what-is-smp/)[What is SaaS security posture management (SSPM)?](https://www.cloudflare.com/learning/cloud/what-is-sspm/)[What is the cloud?](https://www.cloudflare.com/learning/cloud/what-is-the-cloud/)[What is vendor lock-in? | Vendor lock-in and cloud computing](https://www.cloudflare.com/learning/cloud/what-is-vendor-lock-in/)[What is multicloud?](https://www.cloudflare.com/learning/cloud/what-is-multicloud/)[What is hybrid cloud?](https://www.cloudflare.com/learning/cloud/what-is-hybrid-cloud/)[What is a cloud firewall?](https://www.cloudflare.com/learning/cloud/what-is-a-cloud-firewall/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand what multitenancy is, and how it makes cloud computing possible 
  * Explore the benefits and risks of multitenancy 
  * Learn about the technical details of multitenant architecture 



Related content  [ What is the cloud? ](https://www.cloudflare.com/learning/cloud/what-is-the-cloud/)[ What is hybrid cloud? ](https://www.cloudflare.com/learning/cloud/what-is-hybrid-cloud/)[ What is cloud storage? ](https://www.cloudflare.com/learning/cloud/what-is-cloud-storage/)[ What is cloud migration? | Cloud migration strategy ](https://www.cloudflare.com/learning/cloud/what-is-cloud-migration/)[ What is a public cloud? | Public vs. private cloud ](https://www.cloudflare.com/learning/cloud/what-is-a-public-cloud/)

On this page

  * What is multitenancy?

  * What is cloud computing?

  * What are the benefits of multitenancy?

  * What are the drawbacks of multitenancy?

  * How does Cloudflare help companies with cloud deployments?

  * How does multitenancy work?

    * In public cloud computing

    * In container architecture

    * In serverless computing

    * In private cloud computing




## What is multitenancy?

In [cloud computing](https://www.cloudflare.com/learning/cloud/what-is-the-cloud/), multitenancy means that multiple customers of a cloud vendor are using the same computing resources. Despite the fact that they share resources, cloud customers are not aware of each other, and their data is kept totally separate. Multitenancy is a crucial component of cloud computing; without it, cloud services would be far less practical. Multitenant architecture is a feature in many types of public cloud computing, including [IaaS](https://www.cloudflare.com/learning/cloud/what-is-iaas/), [PaaS](https://www.cloudflare.com/learning/serverless/glossary/platform-as-a-service-paas/), [SaaS](https://www.cloudflare.com/learning/cloud/what-is-saas/), [containers](https://www.cloudflare.com/learning/serverless/serverless-vs-containers/), and [serverless computing](https://www.cloudflare.com/learning/serverless/what-is-serverless/).

![Hybrid Cloud Multitenancy](https://images.ctfassets.net/slt3lc6tev37/3DYKyWexhZXIhFd622jgPE/2a7757f1049ac83d8d51696e1c0cf1c9/what-is-multitenancy.svg)Hybrid Cloud Multitenancy

To understand multitenancy, think of how banking works. Multiple people can store their money in one bank, and their assets are completely separate even though they are stored in the same place. Customers of the bank do not interact with each other, do not have access to other customers' money, and are not even aware of each other. Similarly, in [public cloud](https://www.cloudflare.com/learning/cloud/what-is-a-public-cloud/) computing, customers of the cloud vendor use the same infrastructure – the same servers, typically – while still keeping their data and their business logic separate and secure.

The classic definition of multitenancy was a single software instance* that served multiple users, or tenants. However, in modern cloud computing, the term has taken on a broader meaning, referring to shared cloud infrastructure instead of just a shared software instance.

*_A software instance is a copy of a running program loaded into random access memory (RAM)._

## What is cloud computing?

In cloud computing, applications and data are hosted in remote servers in various data centers and accessed over the Internet. Data and applications are centralized in the cloud instead of being located on individual client devices (like laptops or smartphones) or in servers within a company's offices.

Many modern applications are cloud-based, which is why, for example, a user can access their Facebook account and upload content from multiple devices.

## What are the benefits of multitenancy?

Many of the benefits of cloud computing are only possible because of multitenancy. Here are two crucial ways multitenancy improves cloud computing:

**Better use of resources:** One machine reserved for one tenant is not efficient, as that one tenant is not likely to use all of the machine's computing power. By sharing machines among multiple tenants, use of available resources is maximized.

**Lower costs:** With multiple customers sharing resources, a cloud vendor can offer their services to many customers at a much lower cost than if each customer required their own dedicated infrastructure.

## What are the drawbacks of multitenancy?

**Possible security risks and compliance issues:** Some companies may not be able to store data within shared infrastructure, no matter how secure, due to regulatory requirements. Additionally, security problems or corrupted data from one tenant could spread to other tenants on the same machine, although this is extremely rare and should not occur if the cloud vendor has configured their infrastructure correctly. These security risks are somewhat mitigated by the fact that cloud vendors typically are able to invest more in their security than individual businesses can.

**The "noisy neighbor" effect:** If one tenant is using an inordinate amount of computing power, this could slow down performance for the other tenants. Again, this should not occur if the cloud vendor has set up their infrastructure correctly.

## How does Cloudflare help companies with cloud deployments?

Cloudflare helps companies with any type of cloud deployment keep their data secure and their web properties fast. The Cloudflare product stack sits in front of any type of infrastructure and makes web properties more secure, more reliable, and faster. To learn more about how Cloudflare integrates with cloud deployments, see [How Cloudflare works with any cloud infrastructure](https://www.cloudflare.com/learning/cloud/cloudflare-and-the-cloud/).

## How does multitenancy work?

Here we will take a more in-depth look at the technical principles that make multitenancy possible in different kinds of cloud computing.

#### In public cloud computing

Imagine a special car engine that could be shared easily between multiple cars and car owners. Each car owner needs the engine to behave slightly differently: some car owners require a powerful 8-cylinder engine, while others require a more fuel-efficient 4-cylinder engine. Now imagine that this special engine is able to morph itself each time it starts up so that it can better meet the car owner's needs.

This is similar to the way many public cloud providers implement multitenancy. Most cloud providers define multitenancy as a shared software instance. They store metadata* about each tenant and use this data to alter the software instance at runtime to fit each tenant's needs. The tenants are isolated from each other via permissions. Even though they all share the same software instance, they each use and experience the software differently.

*_Metadata is information about a file, somewhat like the description on the back of a book._

#### In container architecture

Containers are self-contained bundles of software that include an application, system libraries, system settings, and everything else the application needs in order to run. Containers help ensure that an application runs the same no matter where it is hosted.

Containers are partitioned from each other into different user space environments, and each container runs as if it were the only system on that host machine. Because containers are self-contained, multiple containers created by different cloud customers can run on a single host machine.

#### In serverless computing

Serverless computing is a model in which applications are broken up into smaller pieces called functions, and each function only runs on demand, separately from the other functions. (This model of cloud computing is also known as [function-as-a-service, or FaaS](https://www.cloudflare.com/learning/serverless/glossary/function-as-a-service-faas/).)

As the name implies, serverless functions do not run on dedicated servers, but rather on any available machine in the serverless provider's infrastructure. Because companies are not assigned their own discrete physical servers, serverless providers will often be running code from several of their customers on a single server at any given time – another example of multitenancy.

Some serverless platforms use Node.js for executing serverless code. The Cloudflare serverless platform, [Cloudflare Workers](https://www.cloudflare.com/products/cloudflare-workers/), uses [Chrome V8](https://www.cloudflare.com/learning/serverless/glossary/what-is-chrome-v8/), in which each function runs in its own sandbox, or separate environment. This keeps serverless functions totally separate from each other even when they’re running on the same infrastructure.

#### In private cloud computing

[Private cloud](https://www.cloudflare.com/learning/cloud/what-is-a-private-cloud/) computing uses multitenant architecture in much the same way that public cloud computing does. The difference is that the other tenants are not from external organizations. In public cloud computing, Company A shares infrastructure with Company B. In private cloud computing, different teams within Company A share infrastructure with each other.
