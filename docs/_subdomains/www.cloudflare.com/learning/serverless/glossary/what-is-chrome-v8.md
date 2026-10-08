---
url: https://www.cloudflare.com/learning/serverless/glossary/what-is-chrome-v8/
title: What is Chrome V8?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:19.808450+00:00
---

# What is Chrome V8?

> Source: https://www.cloudflare.com/learning/serverless/glossary/what-is-chrome-v8/

[ Learning Center ](https://www.cloudflare.com/learning/) / serverless

##  What is Chrome V8? 

Chrome V8 executes JavaScript code. Node.js is built on top of Chrome V8 and is a widely used runtime environment for serverless JavaScript functions. However, there are advantages to running functions directly on V8. 

[Learning Center](https://www.cloudflare.com/learning)/serverless/[What is BaaS? | Backend-as-a-Service vs. serverless](https://www.cloudflare.com/learning/serverless/glossary/backend-as-a-service-baas/)[What do client side and server side mean? | Client side vs. server side](https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/)[What is Function-as-a-Service (FaaS)?](https://www.cloudflare.com/learning/serverless/glossary/function-as-a-service-faas/)[Can mobile applications use a serverless architecture?](https://www.cloudflare.com/learning/serverless/glossary/mobile-apps-serverless-backend/)[What is Platform-as-a-Service (PaaS)?](https://www.cloudflare.com/learning/serverless/glossary/platform-as-a-service-paas/)[The Serverless Framework and Cloudflare Workers | What is the Serverless Framework?](https://www.cloudflare.com/learning/serverless/glossary/serverless-and-cloudflare-workers/)[What is a serverless microservice? | Serverless microservices explained](https://www.cloudflare.com/learning/serverless/glossary/serverless-microservice/)[How are serverless computing and Platform-as-a-Service different?](https://www.cloudflare.com/learning/serverless/glossary/serverless-vs-paas/)[What is Chrome V8?](https://www.cloudflare.com/learning/serverless/glossary/what-is-chrome-v8/)[What is continuous integration and continuous delivery (CI/CD)?](https://www.cloudflare.com/learning/serverless/glossary/what-is-ci-cd/)[What is edge computing?](https://www.cloudflare.com/learning/serverless/glossary/what-is-edge-computing/)[How to build and deploy your web app fast](https://www.cloudflare.com/learning/serverless/how-to-deploy-app-or-website/)[How does serverless JavaScript work? | Service workers and Cloudflare Workers](https://www.cloudflare.com/learning/serverless/serverless-javascript/)[How can serverless computing improve performance? | Lambda performance](https://www.cloudflare.com/learning/serverless/serverless-performance/)[Serverless computing vs. containers | How to choose](https://www.cloudflare.com/learning/serverless/serverless-vs-containers/)[What is serverless computing?](https://www.cloudflare.com/learning/serverless/what-is-serverless/)[Why use serverless?](https://www.cloudflare.com/learning/serverless/why-use-serverless/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define JavaScript engine 
  * Learn about Chrome V8 and Node.js 
  * Understand the role Chrome V8 can play in serverless architectures 



Related content  [ What is serverless computing? ](https://www.cloudflare.com/learning/serverless/what-is-serverless/)[ Why use serverless? ](https://www.cloudflare.com/learning/serverless/why-use-serverless/)

On this page

  * What is Chrome V8?

  * What does compiling mean?

  * What is sandboxing?

  * What is Node.js?

  * Why are V8 and Node.js important for serverless computing?




## What is Chrome V8?

Chrome V8 is a JavaScript engine, which means that it executes JavaScript code. Originally, JavaScript was written to be executed by web browsers. Chrome V8, or just V8, can execute JavaScript code either within or outside of a browser, which makes [server-side scripting](https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/) possible.

Like a V8 (eight-cylinder) car engine, Chrome V8 is fast and powerful. V8 translates JavaScript code directly into machine code* so that computers can actually understand it, then it executes the translated, or compiled, code. V8 optimizes JavaScript execution as well.

*Machine code is a language that CPUs can understand. It is purely digital, meaning made up of digits.

## What does compiling mean?

Compiling is a process that translates code from one programming language into another. Typically a compiler translates the code from a higher level of abstraction to a lower level of abstraction from human-usable languages like JavaScript into machine-readable code.

Chrome V8 performs what is called just-in-time compilation. Instead of compiling JavaScript in advance, it compiles the code at the same time that it is executed.

## What is sandboxing?

![Chrome V8 Sandboxing](https://www.cloudflare.com/img/learning/serverless/glossary/what-is-chrome-v8/chrome-v8-engine-sandboxed-processes.svg)Chrome V8 Sandboxing

A 'sandbox' is an environment for executing software that is isolated and partitioned off from other environments, even those on the same machine.

Sandboxing is a key feature of Chrome V8. Each process is sandboxed, which ensures that JavaScript functions run separately on it and the execution of one piece of code does not affect any other piece of code. (Unlike many sandboxing enterprise products, which open and run executable files within isolated virtual machines, V8 sandboxing does not slow performance.)

## What is Node.js?

Node.js is a runtime environment* for executing JavaScript code, and it is built on the Chrome V8 engine. It is asynchronous, which means that it does not have to wait for one process to complete before starting another one. Like V8, Node.js is free and open-source. Unlike V8, it does not have built-in sandboxing.

(Those familiar with JavaScript will note the '.js' file extension; however, this is purely an aesthetic choice for the runtime environment's name to indicate its association with JavaScript and does not mean that Node.js is a JavaScript file.)

*A runtime environment is the software environment in which code is executed.

## Why are V8 and Node.js important for serverless computing?

[Serverless functions](https://www.cloudflare.com/learning/serverless/glossary/function-as-a-service-faas/) need a way to execute when they are triggered. Several serverless computing vendors offer Node.js as a runtime for [serverless JavaScript](https://www.cloudflare.com/learning/serverless/serverless-javascript/) functions (other runtimes are used for other languages).

[Cloudflare Workers](https://www.cloudflare.com/products/cloudflare-workers/), however, run directly on V8. There are a few reasons for this. One reason is speed of execution for functions that have not been used recently. Cold starts are an issue in serverless computing, but running functions on V8 means that the functions can be 'spun up' and executed, typically, within 5 milliseconds or less. (Node.js has more overhead and usually takes a few milliseconds longer.) Another reason is that V8 sandboxes JavaScript functions automatically, which increases [security](https://www.cloudflare.com/learning/security/what-is-web-application-security/).
