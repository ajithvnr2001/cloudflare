---
url: https://www.cloudflare.com/learning/serverless/glossary/serverless-and-cloudflare-workers/
title: The Serverless Framework and Cloudflare Workers | What is the Serverless Framework?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:17.320959+00:00
---

# The Serverless Framework and Cloudflare Workers | What is the Serverless Framework?

> Source: https://www.cloudflare.com/learning/serverless/glossary/serverless-and-cloudflare-workers/

[ Learning Center ](https://www.cloudflare.com/learning/) / serverless

##  The Serverless Framework and Cloudflare Workers | What is the Serverless Framework? 

The Serverless Framework enables developers to write provider-agnostic serverless architectures, and one of the providers it supports is Cloudflare Workers. 

[Learning Center](https://www.cloudflare.com/learning)/serverless/[What is BaaS? | Backend-as-a-Service vs. serverless](https://www.cloudflare.com/learning/serverless/glossary/backend-as-a-service-baas/)[What do client side and server side mean? | Client side vs. server side](https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/)[What is Function-as-a-Service (FaaS)?](https://www.cloudflare.com/learning/serverless/glossary/function-as-a-service-faas/)[Can mobile applications use a serverless architecture?](https://www.cloudflare.com/learning/serverless/glossary/mobile-apps-serverless-backend/)[What is Platform-as-a-Service (PaaS)?](https://www.cloudflare.com/learning/serverless/glossary/platform-as-a-service-paas/)[The Serverless Framework and Cloudflare Workers | What is the Serverless Framework?](https://www.cloudflare.com/learning/serverless/glossary/serverless-and-cloudflare-workers/)[What is a serverless microservice? | Serverless microservices explained](https://www.cloudflare.com/learning/serverless/glossary/serverless-microservice/)[How are serverless computing and Platform-as-a-Service different?](https://www.cloudflare.com/learning/serverless/glossary/serverless-vs-paas/)[What is Chrome V8?](https://www.cloudflare.com/learning/serverless/glossary/what-is-chrome-v8/)[What is continuous integration and continuous delivery (CI/CD)?](https://www.cloudflare.com/learning/serverless/glossary/what-is-ci-cd/)[What is edge computing?](https://www.cloudflare.com/learning/serverless/glossary/what-is-edge-computing/)[How to build and deploy your web app fast](https://www.cloudflare.com/learning/serverless/how-to-deploy-app-or-website/)[How does serverless JavaScript work? | Service workers and Cloudflare Workers](https://www.cloudflare.com/learning/serverless/serverless-javascript/)[How can serverless computing improve performance? | Lambda performance](https://www.cloudflare.com/learning/serverless/serverless-performance/)[Serverless computing vs. containers | How to choose](https://www.cloudflare.com/learning/serverless/serverless-vs-containers/)[What is serverless computing?](https://www.cloudflare.com/learning/serverless/what-is-serverless/)[Why use serverless?](https://www.cloudflare.com/learning/serverless/why-use-serverless/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand what the Serverless Framework is 
  * Understand how Cloudflare Workers integrates with the Serverless Framework 



Related content  [ What is serverless computing? ](https://www.cloudflare.com/learning/serverless/what-is-serverless/)[ Why use serverless? ](https://www.cloudflare.com/learning/serverless/why-use-serverless/)

On this page

  * What is the Serverless Framework?

  * How does Cloudflare Workers integrate with the Serverless Framework?




## What is the Serverless Framework?

The Serverless Framework is a tool that helps developers create [serverless](https://www.cloudflare.com/learning/serverless/what-is-serverless/) applications that can be deployed via any serverless provider. Applications do not have to be written to the specifications of any particular vendor, and the framework will translate the code into the form necessary for deployment through whichever vendor the developer chooses. The Serverless Framework supports most major serverless computing vendors.

Although serverless providers are all slightly different in their deployment processes, their [access controls](https://www.cloudflare.com/learning/access-management/what-is-access-control/), the programming languages they support, the tools they provide, and so on, applications built using the Serverless Framework are provider-agnostic, meaning they will perform as expected no matter which provider hosts the deployed software.

A developer can deploy their serverless application using the framework, which helps by adapting the code for the selected provider, and then by packaging and deploying the code.

In addition, the Serverless Framework provides features for building serverless architectures that the providers themselves may not offer, including version control, boilerplate code, and templates. As a result, developers are able to build products that have the [benefits of serverless](https://www.cloudflare.com/learning/serverless/why-use-serverless/) computing without having to do some of the grunt work associated with setting up the application and deploying the code.

![Serverless and Workers](https://www.cloudflare.com/img/learning/serverless/glossary/serverless-and-cloudflare-workers/serverless-framework-cloudflare-workers.svg)Serverless and Workers

## How does Cloudflare Workers integrate with the Serverless Framework?

Cloudflare provides serverless compute services via [Cloudflare Workers](https://www.cloudflare.com/products/cloudflare-workers/), a platform for building and deploying JavaScript functions that run on the Cloudflare [edge network](https://www.cloudflare.com/learning/serverless/glossary/what-is-edge-computing/). Running code at the edge, as close to the end user as possible, helps to reduce latency and increase application performance. Each Worker can modify and respond to HTTP requests.

Cloudflare Workers is one of the providers supported by the Serverless Framework. Developers are able to build serverless applications that are then deployed as Cloudflare Workers. For developers whose applications run code in multiple places, using the Serverless Framework may be more efficient than writing their Workers within the Cloudflare Workers UI. This integration enables developers to take advantage of the benefits of both Workers and the Serverless Framework.

To read the technical details of how the integration works, [see these docs](https://developers.cloudflare.com/workers/).
