---
url: https://www.cloudflare.com/learning/cloud/what-is-a-virtual-machine/
title: What Is a Virtual Machine?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:49.762407+00:00
---

# What Is a Virtual Machine?

> Source: https://www.cloudflare.com/learning/cloud/what-is-a-virtual-machine/

[ Learning Center ](https://www.cloudflare.com/learning/) / the cloud

##  What is a virtual machine? 

Virtual machines (VMs) are computers that run inside of other computers using a process known as virtualization. 

[Learning Center](https://www.cloudflare.com/learning)/the cloud/[What is application modernization?](https://www.cloudflare.com/learning/cloud/application-modernization/)[What is cloud-native security?](https://www.cloudflare.com/learning/cloud/cloud-native-security/)[How Cloudflare works with any cloud infrastructure](https://www.cloudflare.com/learning/cloud/cloudflare-and-the-cloud/)[What is a cloud-native application protection platform (CNAPP)?](https://www.cloudflare.com/learning/cloud/cnapp/)[How does hybrid cloud architecture work?](https://www.cloudflare.com/learning/cloud/how-does-hybrid-cloud-architecture-work/)[How to refactor applications](https://www.cloudflare.com/learning/cloud/how-to-refactor-applications/)[How to rehost applications](https://www.cloudflare.com/learning/cloud/how-to-rehost-applications/)[How to replatform applications](https://www.cloudflare.com/learning/cloud/how-to-replatform-applications/)[Multi-cloud vs. hybrid cloud: What's the difference?](https://www.cloudflare.com/learning/cloud/multicloud-vs-hybrid-cloud/)[Next-generation firewall (NGFW) vs. firewall-as-a-service (FWaaS)](https://www.cloudflare.com/learning/cloud/ngfw-vs-fwaas/)[Object storage vs. block storage: How are they different?](https://www.cloudflare.com/learning/cloud/object-storage-vs-block-storage/)[What are data egress fees?](https://www.cloudflare.com/learning/cloud/what-are-data-egress-fees/)[What is a connectivity cloud? | Connectivity cloud definition](https://www.cloudflare.com/learning/cloud/what-is-a-connectivity-cloud/)[What is a data lake?](https://www.cloudflare.com/learning/cloud/what-is-a-data-lake/)[What is a private cloud? | Private cloud vs. public cloud](https://www.cloudflare.com/learning/cloud/what-is-a-private-cloud/)[What is a public cloud? | Public vs. private cloud](https://www.cloudflare.com/learning/cloud/what-is-a-public-cloud/)[What is a virtual machine?](https://www.cloudflare.com/learning/cloud/what-is-a-virtual-machine/)[What is a virtual private cloud (VPC)?](https://www.cloudflare.com/learning/cloud/what-is-a-virtual-private-cloud/)[What is AWS data transfer pricing? ](https://www.cloudflare.com/learning/cloud/what-is-aws-data-transfer-pricing/)[What is blob storage?](https://www.cloudflare.com/learning/cloud/what-is-blob-storage/)[What is block storage?](https://www.cloudflare.com/learning/cloud/what-is-block-storage/)[What is cloud migration? | Cloud migration strategy](https://www.cloudflare.com/learning/cloud/what-is-cloud-migration/)[What is cloud networking?](https://www.cloudflare.com/learning/cloud/what-is-cloud-networking/)[How does cloud security work? | Cloud computing security](https://www.cloudflare.com/learning/cloud/what-is-cloud-security/)[What is cloud storage?](https://www.cloudflare.com/learning/cloud/what-is-cloud-storage/)[What is cloud security posture management (CSPM)?](https://www.cloudflare.com/learning/cloud/what-is-cspm/)[What is a cloud workload protection platform (CWPP)?](https://www.cloudflare.com/learning/cloud/what-is-cwpp/)[What is data migration? | Definition and common processes](https://www.cloudflare.com/learning/cloud/what-is-data-migration/)[What is digital transformation?](https://www.cloudflare.com/learning/cloud/what-is-digital-transformation/)[What is data security posture management (DSPM)?](https://www.cloudflare.com/learning/cloud/what-is-dspm/)[What is IaaS (infrastructure-as-a-service)?](https://www.cloudflare.com/learning/cloud/what-is-iaas/)[What is multi-cloud management?](https://www.cloudflare.com/learning/cloud/what-is-multicloud-management/)[What is multitenancy? | Multitenant architecture](https://www.cloudflare.com/learning/cloud/what-is-multitenancy/)[What is object storage?](https://www.cloudflare.com/learning/cloud/what-is-object-storage/)[What is SaaS? | SaaS definition](https://www.cloudflare.com/learning/cloud/what-is-saas/)[What is a SaaS management platform (SMP)? ](https://www.cloudflare.com/learning/cloud/what-is-smp/)[What is SaaS security posture management (SSPM)?](https://www.cloudflare.com/learning/cloud/what-is-sspm/)[What is the cloud?](https://www.cloudflare.com/learning/cloud/what-is-the-cloud/)[What is vendor lock-in? | Vendor lock-in and cloud computing](https://www.cloudflare.com/learning/cloud/what-is-vendor-lock-in/)[What is multicloud?](https://www.cloudflare.com/learning/cloud/what-is-multicloud/)[What is hybrid cloud?](https://www.cloudflare.com/learning/cloud/what-is-hybrid-cloud/)[What is a cloud firewall?](https://www.cloudflare.com/learning/cloud/what-is-a-cloud-firewall/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define virtual machine 
  * Understand how virtualization and virtual hardware work 
  * Outline several use cases for virtual machines 



Related content  [ What is the cloud? ](https://www.cloudflare.com/learning/cloud/what-is-the-cloud/)[ What is hybrid cloud? ](https://www.cloudflare.com/learning/cloud/what-is-hybrid-cloud/)[ What is cloud migration? | Cloud migration strategy ](https://www.cloudflare.com/learning/cloud/what-is-cloud-migration/)[ What is a public cloud? | Public vs. private cloud ](https://www.cloudflare.com/learning/cloud/what-is-a-public-cloud/)[ What is a private cloud? | Private cloud vs. public cloud ](https://www.cloudflare.com/learning/cloud/what-is-a-private-cloud/)

On this page

  * What is a virtual machine?

  * What is an operating system?

  * Can you have two or more operating systems on one computer?

  * What are virtual machines used for?

  * How does cloud computing use virtual machines?

  * Cloudflare and virtual machines




## What is a virtual machine?

A virtual machine (VM) is a software-based computer that exists within another computer’s operating system, often used for the purposes of testing, backing up data, or running [SaaS](https://www.cloudflare.com/learning/cloud/what-is-saas/) applications. To grasp how VMs work, it’s important to first understand how computer software and hardware are typically integrated by an operating system.

## What is an operating system?

Traditional computers are built out of physical hardware, including hard disk drives, processor chips, RAM, and more. In order to utilize this hardware, computers rely on a type of software known as an operating system (OS). Some common examples of OSes are Mac OSX, Microsoft Windows, Linux, and Android.

The OS is what manages the computer’s hardware in ways that are useful to the user. For example, if the user wants to access the Internet, the OS directs the network interface card to make the connection. If the user wants to download a file, the OS will partition space on the hard drive for that file. The OS also runs and manages other pieces of software. For example, it can run a web browser and provide the browser with enough random access memory (RAM) to operate smoothly.

Typically, operating systems exist within a physical computer at a one-to-one ratio. for each machine there is a single OS managing its physical resources.

## Can you have two or more operating systems on one computer?

It is possible to run multiple operating systems on one computer. This can be achieved through a process called virtualization. In virtualization, a piece of software behaves as if it were an independent computer. This piece of software is called a virtual machine, also known as a ‘guest’ computer. (The computer on which the VM is running is called the ‘host’.) The guest has an OS as well as its own virtual hardware.

‘Virtual hardware’ may sound like an oxymoron. In fact, a VM's 'hard drive' is really just a file on the host computer’s hard drive. However, a virtual hard drive fulfills the same function as a physical one.

The number of VMs that can run on one host is limited only by the host’s available resources. The user can run the OS of a VM in a window like any other program, or they can run it in fullscreen so that it looks and feels like a genuine host OS.

## What are virtual machines used for?

Common use cases for virtual machines on single computers include:

  * **Testing** \- Software developers often want to test their applications in different environments. They can use virtual machines to run their applications in various OSes on one computer. This is simpler and more cost-effective than testing on several different physical machines.

  * **Running software designed for other OSes** \- Although certain software applications are only available for a single platform, a VM can run software designed for a different OS. For example, a Mac user who wants to run software designed for Windows can run a Windows VM on their Mac host.

  * **Running outdated software** \- Some pieces of older software can’t be run in modern OSes. Users who want to run these applications can run an old OS on a virtual machine.

  * **Browser isolation** \- [Browser isolation](https://www.cloudflare.com/learning/access-management/what-is-browser-isolation/) is the practice of 'isolating' web browser activity away from the rest of a computer's operating system to keep malware from affecting the computer's other files and programs. Some browser isolation tools use VMs to establish this isolation — though this approach can slow down browsing activity.




## How does cloud computing use virtual machines?

Several cloud providers offer virtual machines to their customers. These virtual machines typically live on powerful servers that can act as a host to multiple VMs and can be used for a variety of reasons that wouldn’t be practical with a locally-hosted VM. These include:

  * **Running SaaS applications** \- [Software-as-a-service](https://www.cloudflare.com/learning/cloud/what-is-saas/), or SaaS for short, is a cloud-based method of providing software to users, in which an application is served to user over the Internet rather than running on their computers. Often, it is virtual machines in [the cloud](https://www.cloudflare.com/learning/cloud/what-is-the-cloud/) that do the computation for SaaS applications as well as delivering them to users. If the cloud provider has a geographically distributed [network edge](https://www.cloudflare.com/learning/serverless/glossary/what-is-edge-computing/), then the application will run closer to the user, resulting in faster performance.

  * **Backing up data** \- Cloud-based VM services are popular for backing up data, because the data can be accessed from anywhere. Plus, cloud VMs provide better redundancy, require less maintenance, and generally scale better than physical data centers. (For example, it’s relatively easy to buy an extra gigabyte of storage space from a cloud VM provider, but much more difficult to build a new local data server for that extra gigabyte of data.)

  * **Hosting services like email and access management** \- Hosting these services on cloud VMs is generally faster and more cost-effective, and helps minimize maintenance and offload security concerns as well.

  * **Browser isolation** \- Some browser isolation tools use cloud VMs to run web browsing activity and deliver safe content to users via a secure Internet connection




## Cloudflare and virtual machines

Cloudflare helps protect and manage any type of cloud deployment, including cloud VMs. SaaS providers can use [Cloudflare for SaaS](https://www.cloudflare.com/saas/) to improve their application's peformance, protect custom domains for end-users, and more.

Additionally, for users who want the functionality of running code on the edge without the overhead of virtual machines, the [Cloudflare Workers](https://www.cloudflare.com/products/cloudflare-workers/) a [serverless](https://www.cloudflare.com/learning/serverless/what-is-serverless/) platform provides edge computation to customers in a completely scalable way, allowing developers to augment existing applications or create entirely new ones without configuring or maintaining infrastructure.
