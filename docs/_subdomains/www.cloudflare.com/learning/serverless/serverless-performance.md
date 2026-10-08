---
url: https://www.cloudflare.com/learning/serverless/serverless-performance/
title: How Can Serverless Computing Improve Performance? | Lambda Performance
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:38.038074+00:00
---

# How Can Serverless Computing Improve Performance? | Lambda Performance

> Source: https://www.cloudflare.com/learning/serverless/serverless-performance/

[ Learning Center ](https://www.cloudflare.com/learning/) / serverless

##  How can serverless computing improve performance? | Lambda performance 

In a serverless architecture, having more points of presence makes a large positive impact on performance. 

[Learning Center](https://www.cloudflare.com/learning)/serverless/[What is BaaS? | Backend-as-a-Service vs. serverless](https://www.cloudflare.com/learning/serverless/glossary/backend-as-a-service-baas/)[What do client side and server side mean? | Client side vs. server side](https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/)[What is Function-as-a-Service (FaaS)?](https://www.cloudflare.com/learning/serverless/glossary/function-as-a-service-faas/)[Can mobile applications use a serverless architecture?](https://www.cloudflare.com/learning/serverless/glossary/mobile-apps-serverless-backend/)[What is Platform-as-a-Service (PaaS)?](https://www.cloudflare.com/learning/serverless/glossary/platform-as-a-service-paas/)[The Serverless Framework and Cloudflare Workers | What is the Serverless Framework?](https://www.cloudflare.com/learning/serverless/glossary/serverless-and-cloudflare-workers/)[What is a serverless microservice? | Serverless microservices explained](https://www.cloudflare.com/learning/serverless/glossary/serverless-microservice/)[How are serverless computing and Platform-as-a-Service different?](https://www.cloudflare.com/learning/serverless/glossary/serverless-vs-paas/)[What is Chrome V8?](https://www.cloudflare.com/learning/serverless/glossary/what-is-chrome-v8/)[What is continuous integration and continuous delivery (CI/CD)?](https://www.cloudflare.com/learning/serverless/glossary/what-is-ci-cd/)[What is edge computing?](https://www.cloudflare.com/learning/serverless/glossary/what-is-edge-computing/)[How to build and deploy your web app fast](https://www.cloudflare.com/learning/serverless/how-to-deploy-app-or-website/)[How does serverless JavaScript work? | Service workers and Cloudflare Workers](https://www.cloudflare.com/learning/serverless/serverless-javascript/)[How can serverless computing improve performance? | Lambda performance](https://www.cloudflare.com/learning/serverless/serverless-performance/)[Serverless computing vs. containers | How to choose](https://www.cloudflare.com/learning/serverless/serverless-vs-containers/)[What is serverless computing?](https://www.cloudflare.com/learning/serverless/what-is-serverless/)[Why use serverless?](https://www.cloudflare.com/learning/serverless/why-use-serverless/)

######  Learning objectives 

After reading this article you will be able to: 

  * Learn about AWS Lambda, Lambda@Edge, and Cloudflare Workers 
  * See the differences in performance between the platforms 
  * Understand latency and points of presence 



Related content  [ What is serverless computing? ](https://www.cloudflare.com/learning/serverless/what-is-serverless/)[ Why use serverless? ](https://www.cloudflare.com/learning/serverless/why-use-serverless/)

On this page

  * How can serverless improve performance?

  * What is AWS Lambda?

  * Where is AWS Lambda deployed?

  * What is AWS Lambda@Edge?

  * AWS Lambda@Edge vs. Cloudflare Workers

  * What is latency? How does latency affect user behavior?

  * What are points of presence?

  * How quickly do serverless functions respond on average?

  * Serverless cold starts: How quickly do new processes respond in a serverless architecture?




## How can serverless improve performance?

One of the advantages of [serverless computing](https://www.cloudflare.com/learning/serverless/what-is-serverless/) is the ability to run application code from anywhere. By definition, in a serverless architecture there are no [origin servers](https://www.cloudflare.com/learning/cdn/glossary/origin-server/); therefore, it is possible for code to run on [edge locations](https://www.cloudflare.com/learning/serverless/glossary/what-is-edge-computing/) close to end users. Two serverless platforms that take advantage of this ability and the resulting reduction in [latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/) are AWS Lambda@Edge and [Cloudflare Workers](https://www.cloudflare.com/products/cloudflare-workers/). By measuring Lambda performance compared to the performance of Cloudflare Workers and Lambda@Edge, it is possible to observe the effects of deploying serverless applications at the edge. Test results (below) indicate that Cloudflare Workers usually have a faster response.

## What is AWS Lambda?

AWS Lambda is a serverless infrastructure service provided by Amazon Web Services. Lambda hosts event-driven application [functions](https://www.cloudflare.com/learning/serverless/glossary/function-as-a-service-faas/) written in a variety of languages, and it starts up and runs them when they are needed.

## Where is AWS Lambda deployed?

AWS offers a number of regions for deployment around the world. Typically a Lambda-hosted application will be hosted in only one of these regions.

## What is AWS Lambda@Edge?

AWS Lambda@Edge is Lambda deployed on all globally distributed AWS regions instead of in one local geographic region. While Lambda supports multiple languages, Lambda@Edge functions run on Node.js, a run-time environment for executing JavaScript. When a Lambda@Edge function is triggered, it runs within the AWS region closest to the source of the triggering event, meaning that it runs as close as possible to the person or machine using the application.

For example, suppose a user in Chicago requests some information using an application with a serverless architecture. If the serverless application's infrastructure is hosted using AWS Lambda within the US-East-1 region (in Virginia), the request will have to travel all the way to an AWS center in Virginia, and the response will travel all the way from there back to Chicago. But if the application is hosted using AWS Lambda@Edge, then the request and response will only have to travel to and from the closest AWS region, US-East-2, which is in Ohio. This decrease in distance reduces latency compared to AWS Lambda.

## AWS Lambda@Edge vs. Cloudflare Workers

Similar to AWS Lambda@Edge, Cloudflare Workers are event-driven JavaScript functions hosted from data centers around the world. However, there are many important differences between the two serverless infrastructure services. Cloudflare Workers run on [Chrome V8](https://www.cloudflare.com/learning/serverless/glossary/what-is-chrome-v8/) directly rather than Node.js, and Cloudflare has data centers in 200 cities around the world. Because they use V8 directly, Cloudflare Workers can start much faster and consume much fewer resources than other serverless platforms. In the example above, if the user in Chicago were trying to get a response from an application built with Cloudflare Workers, the request would travel to the Cloudflare PoP in Chicago rather than Ohio.

## What is latency? How does latency affect user behavior?

In networking, 'latency' is the length of the delay before requested information loads. As latency increases, the amount of users who leave the webpage increases as well.

Even small decreases in load time greatly increase user engagement. For example, a study by Walmart showed that each improvement of one second in page load time increased conversions by 2%. Conversely, as latency increases, users are more likely to stop using a website or an application. Latency becomes lower as the distance information has to travel is reduced.

## What are points of presence (PoP)?

A point of presence (PoP) is a place where communications networks interconnect, and in the context of the Internet it's a place where the hardware (routers, switches, servers, and so on) that allows people to connect to the Internet lives. When speaking about an edge network, a point of presence is an edge server location. More PoPs on the edge result in faster responses for a greater number of users, because the likelihood that a PoP is geographically near a user increases with more PoPs.

## How quickly do serverless functions respond on average?

Cloudflare performed tests comparing AWS Lambda, Lambda@Edge, and Cloudflare Workers in order to demonstrate serverless responsiveness and test the effectiveness of deploying serverless functions across multiple PoPs. (The test functions were simple scripts that responded with the current time of day when they were run.)

The chart below displays function response times from AWS Lambda (blue), AWS Lambda@Edge (green), and Cloudflare Workers (red). For this test, the AWS Lambda functions were hosted in the US-East-1 region.

![aws-lambda-vs-cloudflare-workers](https://www.cloudflare.com/img/learning/serverless/serverless-performance/aws-lambda-lambda-edge-workers-performance-graph-1.svg)aws-lambda-vs-cloudflare-workers

In a serverless architecture, where code runs (geographically speaking) has an impact on latency. If application code runs closer to the user, the application's performance improves because information does not have to travel as far, and the application responds more quickly. Though response times varied for all three services, Cloudflare Workers responses were usually the quickest. Lambda@Edge was next-fastest, exemplifying the benefits of running serverless functions in multiple locations.

Although AWS regions are spread out across the globe, Cloudflare has more total PoPs. Cloudflare also performed tests that were limited to North America, and delays caused by DNS resolving were filtered out. The results, displayed below, are another example of how more PoPs reduce latency and improve performance. Note that Cloudflare Workers responses take the least amount of time.

![lambda-vs-workers](https://www.cloudflare.com/img/learning/serverless/serverless-performance/aws-lambda-lambda-edge-workers-performance-graph-2.svg)lambda-vs-workers

## Serverless cold starts: How quickly do new processes respond in a serverless architecture?

In serverless computing, a 'cold start' refers to when a function that has not been run recently has to respond to an event. Such functions need to be 'spun up' before they can run, which takes a few milliseconds typically. This can cause additional latency issues.

Cloudflare Workers has eliminated cold starts entirely, meaning they need zero spin up time. This is the case in every location in Cloudflare's global network. In contrast, both Lambda and Lambda@Edge functions can take over a second to respond from a cold start.

The differences are largely due to the fact that Cloudflare Workers run on Chrome V8 rather than Node.js. Node.js is built on top of Chrome V8, takes longer to spin up, and has more memory overhead. Usually V8 instances take less than 5 milliseconds to spin up.

Learn more about [Cloudflare Workers](https://www.cloudflare.com/products/cloudflare-workers/).
