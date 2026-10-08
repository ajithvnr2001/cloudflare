---
url: https://www.cloudflare.com/learning/serverless/glossary/serverless-microservice/
title: What Is a Serverless Microservice? | Serverless Microservices Explained
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:17.302735+00:00
---

# What Is a Serverless Microservice? | Serverless Microservices Explained

> Source: https://www.cloudflare.com/learning/serverless/glossary/serverless-microservice/

[ Learning Center ](https://www.cloudflare.com/learning/) / serverless

##  What is a serverless microservice? | Serverless microservices explained 

Microservices are smaller segments of an application that run independently of each other, and they can be deployed in a variety of ways. A serverless microservice is deployed within a serverless architecture. 

[Learning Center](https://www.cloudflare.com/learning)/serverless/[What is BaaS? | Backend-as-a-Service vs. serverless](https://www.cloudflare.com/learning/serverless/glossary/backend-as-a-service-baas/)[What do client side and server side mean? | Client side vs. server side](https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/)[What is Function-as-a-Service (FaaS)?](https://www.cloudflare.com/learning/serverless/glossary/function-as-a-service-faas/)[Can mobile applications use a serverless architecture?](https://www.cloudflare.com/learning/serverless/glossary/mobile-apps-serverless-backend/)[What is Platform-as-a-Service (PaaS)?](https://www.cloudflare.com/learning/serverless/glossary/platform-as-a-service-paas/)[The Serverless Framework and Cloudflare Workers | What is the Serverless Framework?](https://www.cloudflare.com/learning/serverless/glossary/serverless-and-cloudflare-workers/)[What is a serverless microservice? | Serverless microservices explained](https://www.cloudflare.com/learning/serverless/glossary/serverless-microservice/)[How are serverless computing and Platform-as-a-Service different?](https://www.cloudflare.com/learning/serverless/glossary/serverless-vs-paas/)[What is Chrome V8?](https://www.cloudflare.com/learning/serverless/glossary/what-is-chrome-v8/)[What is continuous integration and continuous delivery (CI/CD)?](https://www.cloudflare.com/learning/serverless/glossary/what-is-ci-cd/)[What is edge computing?](https://www.cloudflare.com/learning/serverless/glossary/what-is-edge-computing/)[How to build and deploy your web app fast](https://www.cloudflare.com/learning/serverless/how-to-deploy-app-or-website/)[How does serverless JavaScript work? | Service workers and Cloudflare Workers](https://www.cloudflare.com/learning/serverless/serverless-javascript/)[How can serverless computing improve performance? | Lambda performance](https://www.cloudflare.com/learning/serverless/serverless-performance/)[Serverless computing vs. containers | How to choose](https://www.cloudflare.com/learning/serverless/serverless-vs-containers/)[What is serverless computing?](https://www.cloudflare.com/learning/serverless/what-is-serverless/)[Why use serverless?](https://www.cloudflare.com/learning/serverless/why-use-serverless/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define a serverless microservice 
  * Understand how serverless microservices work 
  * Differentiate between microservices, containers, and functions 



Related content  [ What is serverless computing? ](https://www.cloudflare.com/learning/serverless/what-is-serverless/)[ Why use serverless? ](https://www.cloudflare.com/learning/serverless/why-use-serverless/)

On this page

  * What is a microservice?

  * Advantages of microservices

  * Can microservices be part of a serverless architecture?

  * What are serverless microservices? How does a serverless microservices architecture work?

  * What is the difference between a microservice and a serverless function?

  * Are Cloudflare Workers microservices?




## What is a microservice?

Imagine taking an application, chopping it up into pieces, and running it as a collection of smaller parts instead of one monolithic whole. That's basically what a microservices architecture is. Each piece of the application is called a 'microservice,' and it performs one service only, runs independently of the other parts of the application, operates in its own environment, and stores its own data. Despite the name, microservices do not have to be small. What makes them 'micro' is that they only handle one service and are part of a larger application.

Think of an application constructed of microservices as being like an American football team, in which each player performs a distinct role, but the players together form a team (the whole application) that collectively accomplishes a goal. Or, think of microservices as the different systems in the human body (circulatory, respiratory, etc.), and the application as the entire body.

From the user's perspective, an application built with microservices has a single interface and should work just the same as an application designed as one stack. However, behind the scenes each microservice has its own database and runs separately from the rest of the application. In addition, microservices within the same application can be written in different languages and use different libraries.

![Monolithic architecture vs. microservices architecture](https://www.cloudflare.com/img/learning/serverless/glossary/serverless-microservice/monolithic-architecture-vs-microservices-architecture.svg)Monolithic architecture vs. microservices architecture

Microservices are often contrasted against monolithic architecture. Monolithic architecture is the classic way of building an application. A monolithic application is a single stack, with the user interface on top, the business logic in the middle, and the database on the bottom. Usually a monolithic application is hosted on a specific server or set of servers. One of the downsides of constructing an application in this way is that any small change to the application means the entire stack has to be updated. Another downside is that if one part of the application breaks, the whole application might fail.

## Advantages of microservices

  * **Resilience:** Because the application is divided up, one part of the application breaking or crashing does not necessarily affect the rest of the application

  * **Selective scalability:** Instead of scaling the entire application, only the microservices that receive a great deal of usage can be scaled

  * **Easier to add or update features:** Features can be rolled out or updated one at a time, instead of updating the entire application stack

  * **Flexibility for developers:** Microservices can be written in different languages and each have their own libraries




## Can microservices be part of a serverless architecture?

Microservices can be deployed in a variety of ways; they can be part of a serverless architecture, hosted in containers, developed using [PaaS](https://www.cloudflare.com/learning/serverless/glossary/platform-as-a-service-paas/), or, theoretically, used to build a locally hosted application. However, the advantages of building an application out of microservices are perhaps most apparent when the application is hosted in the cloud, either using [containers](https://www.cloudflare.com/learning/serverless/serverless-vs-containers/) or in a serverless architecture.

## What are serverless microservices? How does a serverless microservices architecture work?

Serverless microservices are deployed within a serverless vendor's infrastructure and only run when they are needed by the application. Depending on the size of a microservice, it may also be broken up into even smaller [functions](https://www.cloudflare.com/learning/serverless/glossary/function-as-a-service-faas/). To learn more about how serverless computing works, see [What is Serverless Computing?](https://www.cloudflare.com/learning/serverless/what-is-serverless/)

## What is the difference between a microservice and a serverless function?

This distinction is still being defined by the tech community, but typically, a microservice is larger and can do more than a function. A function is a relatively small bit of code that performs only one action in response to an event. Depending on how developers have divided up an application, a microservice may be equivalent to a function (meaning it performs only one action), or it may be made up of multiple functions.

Extending the football metaphor, consider all the duties of a quarterback: throwing passes, handing the ball off to the running back, and so on. If the quarterback is like a microservice within the context of the team (providing the service of 'quarterbacking'), then each of these smaller activities is a function. However, the line between a microservice and a function can be blurred at times, just as there are certain players on a football team who perform one action only, like the kicker.

## Are Cloudflare Workers microservices?

[Cloudflare Workers](https://www.cloudflare.com/products/cloudflare-workers/) are pieces of JavaScript code that are hosted within the Cloudflare edge network and run in response to HTTP requests. Workers behave more like functions but offer the flexibility to also work as microservices; Cloudflare does not limit the size or type of Workers that developers can build and deploy.
