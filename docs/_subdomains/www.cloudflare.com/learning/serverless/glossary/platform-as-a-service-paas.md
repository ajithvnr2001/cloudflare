---
url: https://www.cloudflare.com/learning/serverless/glossary/platform-as-a-service-paas/
title: What Is Platform-as-a-Service (PaaS)?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:16.146901+00:00
---

# What Is Platform-as-a-Service (PaaS)?

> Source: https://www.cloudflare.com/learning/serverless/glossary/platform-as-a-service-paas/

[ Learning Center ](https://www.cloudflare.com/learning/) / serverless

##  What is Platform-as-a-Service (PaaS)? 

Platform-as-a-Service (PaaS) vendors provide a cloud-based platform for building and running applications. 

[Learning Center](https://www.cloudflare.com/learning)/serverless/[What is BaaS? | Backend-as-a-Service vs. serverless](https://www.cloudflare.com/learning/serverless/glossary/backend-as-a-service-baas/)[What do client side and server side mean? | Client side vs. server side](https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/)[What is Function-as-a-Service (FaaS)?](https://www.cloudflare.com/learning/serverless/glossary/function-as-a-service-faas/)[Can mobile applications use a serverless architecture?](https://www.cloudflare.com/learning/serverless/glossary/mobile-apps-serverless-backend/)[What is Platform-as-a-Service (PaaS)?](https://www.cloudflare.com/learning/serverless/glossary/platform-as-a-service-paas/)[The Serverless Framework and Cloudflare Workers | What is the Serverless Framework?](https://www.cloudflare.com/learning/serverless/glossary/serverless-and-cloudflare-workers/)[What is a serverless microservice? | Serverless microservices explained](https://www.cloudflare.com/learning/serverless/glossary/serverless-microservice/)[How are serverless computing and Platform-as-a-Service different?](https://www.cloudflare.com/learning/serverless/glossary/serverless-vs-paas/)[What is Chrome V8?](https://www.cloudflare.com/learning/serverless/glossary/what-is-chrome-v8/)[What is continuous integration and continuous delivery (CI/CD)?](https://www.cloudflare.com/learning/serverless/glossary/what-is-ci-cd/)[What is edge computing?](https://www.cloudflare.com/learning/serverless/glossary/what-is-edge-computing/)[How to build and deploy your web app fast](https://www.cloudflare.com/learning/serverless/how-to-deploy-app-or-website/)[How does serverless JavaScript work? | Service workers and Cloudflare Workers](https://www.cloudflare.com/learning/serverless/serverless-javascript/)[How can serverless computing improve performance? | Lambda performance](https://www.cloudflare.com/learning/serverless/serverless-performance/)[Serverless computing vs. containers | How to choose](https://www.cloudflare.com/learning/serverless/serverless-vs-containers/)[What is serverless computing?](https://www.cloudflare.com/learning/serverless/what-is-serverless/)[Why use serverless?](https://www.cloudflare.com/learning/serverless/why-use-serverless/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define PaaS 
  * Explore the advantages and disadvantages of PaaS 
  * Compare PaaS to serverless computing 



Related content  [ What is serverless computing? ](https://www.cloudflare.com/learning/serverless/what-is-serverless/)[ Serverless computing vs. containers | How to choose ](https://www.cloudflare.com/learning/serverless/serverless-vs-containers/)[ Why use serverless? ](https://www.cloudflare.com/learning/serverless/why-use-serverless/)

On this page

  * What is Platform-as-a-Service?

  * What are the three service models of cloud computing?

  * How does PaaS compare to internally hosted development environments?

  * What is included in PaaS?

    * Development tools

    * Middleware

    * Operating systems

    * Databases

    * Infrastructure

  * Why do developers use PaaS?

    * Faster time to market

    * One environment from start to finish

    * Price

    * Ease of licensing

  * What are the potential drawbacks of using PaaS?

    * Vendor lock-in

    * Vendor dependency

    * Security and compliance challenges

  * How is Platform-as-a-Service different from serverless computing?




## What is Platform-as-a-Service (PaaS)?

In the Platform-as-a-Service (PaaS) model, developers essentially rent everything they need to build an application, relying on a cloud provider for development tools, infrastructure, and operating systems. This is one of the three service models of cloud computing. PaaS vastly simplifies web application development; from the developer's perspective, all backend management takes place behind the scenes. Although PaaS has some similarities with [serverless computing](https://www.cloudflare.com/learning/serverless/what-is-serverless/), there are many critical differences between them.

## What are the three service models of cloud computing?

![SaaS, PaaS, and IaaS Service Models](https://www.cloudflare.com/img/learning/serverless/glossary/platform-as-a-service-paas/saas-paas-iaas-diagram.svg)SaaS, PaaS, and IaaS Service Models

The three models of [cloud computing](https://www.cloudflare.com/learning/cloud/what-is-the-cloud/) are PaaS, [SaaS (Software-as-a-Service)](https://www.cloudflare.com/learning/cloud/what-is-saas/), and [IaaS (Infrastructure-as-a-Service)](https://www.cloudflare.com/learning/cloud/what-is-iaas/). IaaS refers to cloud computing infrastructure – servers, [storage](https://www.cloudflare.com/learning/cloud/what-is-cloud-storage/), etc. – managed by a cloud vendor, while SaaS refers to full applications that are hosted in the cloud and maintained by the SaaS vendor. If a SaaS customer is like someone renting a house, then a PaaS customer is like someone renting all the heavy equipment and power tools necessary to rapidly build a house, if the tools and equipment were continually maintained and repaired by their owner.

## How does PaaS compare to internally hosted development environments?

PaaS can be accessed over any internet connection, making it possible to build an entire application in a web browser. Because the development environment is not hosted locally, developers can work on the application from anywhere in the world. This enables teams that are spread out across geographic locations to collaborate. It also means developers have less control over the development environment, though this comes with far less overhead.

## What is included in PaaS?

The main offerings included by PaaS vendors are:

  * Development tools

  * Middleware

  * Operating systems

  * Database management

  * Infrastructure




Different vendors may include other services as well, but these are the core PaaS services.

#### Development tools

PaaS vendors offer a variety of tools that are necessary for software development, including a source code editor, a debugger, a compiler, and other essential tools. These tools may be offered together as a framework. The specific tools offered will depend on the vendor, but PaaS offerings should include everything a developer needs to build their application.

#### Middleware

Platforms offered as a service usually include middleware, so that developers don't have to build it themselves. Middleware is software that sits in between user-facing applications and the machine's operating system; for example, middleware is what allows software to access input from the keyboard and mouse. Middleware is necessary for running an application, but end users don't interact with it.

#### Operating systems

A PaaS vendor will provide and maintain the operating system that developers work on and the application runs on.

#### Databases

PaaS providers administer and maintain databases. They will usually provide developers with a database management system as well.

#### Infrastructure

PaaS is the next layer up from IaaS in the cloud computing service model, and everything included in IaaS is also included in PaaS. A PaaS provider either manages servers, storage, and physical data centers, or purchases them from an IaaS provider.

![SaaS, PaaS, IaaS, and Cloud as a Pyramid](https://www.cloudflare.com/img/learning/serverless/glossary/platform-as-a-service-paas/saas-paas-iaas-cloud-pyramid.svg)SaaS, PaaS, IaaS, and Cloud as a Pyramid

## Why do developers use PaaS?

#### Faster time to market

PaaS is used to build applications more quickly than would be possible if developers had to worry about building, configuring, and provisioning their own platforms and backend infrastructure. With PaaS, all they need to do is write the code and test the application, and the vendor handles the rest.

#### One environment from start to finish

PaaS permits developers to build, test, debug, deploy, host, and update their applications all in the same environment. This enables developers to be sure a web application will function properly as hosted before they release, and it simplifies the application development lifecycle.

#### Price

PaaS is more cost-effective than leveraging IaaS in many cases. Overhead is reduced because PaaS customers don't need to manage and provision virtual machines. In addition, some providers have a pay-as-you-go pricing structure, in which the vendor only charges for the computing resources used by the application, usually saving customers money. However, each vendor has a slightly different pricing structure, and some platform providers charge a flat fee per month.

#### Ease of licensing

PaaS providers handle all licensing for operating systems, development tools, and everything else included in their platform.

## What are the potential drawbacks of using PaaS?

#### Vendor lock-in

It may become hard to switch PaaS providers, since the application is built using the vendor's tools and specifically for their platform. Each vendor may have different architecture requirements. Different vendors may not support the same languages, libraries, APIs, architecture, or operating system used to build and run the application. To [switch vendors](https://www.cloudflare.com/learning/cloud/what-is-vendor-lock-in/), developers may need to either rebuild or heavily alter their application.

#### Vendor dependency

The effort and resources involved in changing PaaS vendors may make companies more dependent on their current vendor. A small change in the vendor's internal processes or infrastructure could have a huge impact on the performance of an application designed to run efficiently on the old configuration. Additionally, if the vendor changes their pricing model, an application may suddenly become more expensive to operate.

#### Security and compliance challenges

In a PaaS architecture, the external vendor will store most or all of an application's data, along with hosting its code. In some cases the vendor may actually store the databases via a further third party, an IaaS provider. Though most PaaS vendors are large companies with strong security in place, this makes it difficult to fully assess and test the security measures protecting the application and its data. In addition, for companies that have to comply with strict data security regulations, verifying the compliance of additional external vendors will add more hurdles to going to market.

## How is Platform-as-a-Service different from serverless computing?

PaaS and [serverless computing](https://www.cloudflare.com/developer-platform/workers-kv/) are similar in that for both, all a developer has to worry about is writing and uploading code, and the vendor handles all backend processes. However, scaling is vastly different when using the two models. Applications built using serverless computing, or FaaS, will scale automatically, while PaaS applications will not unless programmed to do so. Startup times also vary greatly; serverless applications can be up and running almost instantly, but PaaS applications are more like traditional applications and have to be running most of the time or all of the time in order to be immediately available for users.

Another difference is that serverless vendors do not provide development tools or frameworks, as PaaS vendors do. And finally, pricing separates the two models. PaaS billing is not nearly as precise as in serverless computing, in which charges are broken down to the number of seconds or fractions of a second each instance of a function runs.
