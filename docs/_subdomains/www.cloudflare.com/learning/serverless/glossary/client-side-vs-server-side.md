---
url: https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/
title: What Do Client-Side and Server-Side Mean? | Client Side vs. Server Side
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:12.088828+00:00
---

# What Do Client-Side and Server-Side Mean? | Client Side vs. Server Side

> Source: https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/

[ Learning Center ](https://www.cloudflare.com/learning/) / serverless

##  What do client side and server side mean? | Client side vs. server side 

Client side and server side describe where web application code runs. 

[Learning Center](https://www.cloudflare.com/learning)/serverless/[What is BaaS? | Backend-as-a-Service vs. serverless](https://www.cloudflare.com/learning/serverless/glossary/backend-as-a-service-baas/)[What do client side and server side mean? | Client side vs. server side](https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/)[What is Function-as-a-Service (FaaS)?](https://www.cloudflare.com/learning/serverless/glossary/function-as-a-service-faas/)[Can mobile applications use a serverless architecture?](https://www.cloudflare.com/learning/serverless/glossary/mobile-apps-serverless-backend/)[What is Platform-as-a-Service (PaaS)?](https://www.cloudflare.com/learning/serverless/glossary/platform-as-a-service-paas/)[The Serverless Framework and Cloudflare Workers | What is the Serverless Framework?](https://www.cloudflare.com/learning/serverless/glossary/serverless-and-cloudflare-workers/)[What is a serverless microservice? | Serverless microservices explained](https://www.cloudflare.com/learning/serverless/glossary/serverless-microservice/)[How are serverless computing and Platform-as-a-Service different?](https://www.cloudflare.com/learning/serverless/glossary/serverless-vs-paas/)[What is Chrome V8?](https://www.cloudflare.com/learning/serverless/glossary/what-is-chrome-v8/)[What is continuous integration and continuous delivery (CI/CD)?](https://www.cloudflare.com/learning/serverless/glossary/what-is-ci-cd/)[What is edge computing?](https://www.cloudflare.com/learning/serverless/glossary/what-is-edge-computing/)[How to build and deploy your web app fast](https://www.cloudflare.com/learning/serverless/how-to-deploy-app-or-website/)[How does serverless JavaScript work? | Service workers and Cloudflare Workers](https://www.cloudflare.com/learning/serverless/serverless-javascript/)[How can serverless computing improve performance? | Lambda performance](https://www.cloudflare.com/learning/serverless/serverless-performance/)[Serverless computing vs. containers | How to choose](https://www.cloudflare.com/learning/serverless/serverless-vs-containers/)[What is serverless computing?](https://www.cloudflare.com/learning/serverless/what-is-serverless/)[Why use serverless?](https://www.cloudflare.com/learning/serverless/why-use-serverless/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand the client-server model 
  * Learn the types of processes that take place on clients and servers 
  * Explore how clients and servers relate to the application frontend and backend 
  * Discover how using a serverless architecture affects server-side processes 



Related content  [ How does serverless JavaScript work? | Service workers and Cloudflare Workers ](https://www.cloudflare.com/learning/serverless/serverless-javascript/)[ Serverless computing vs. containers | How to choose ](https://www.cloudflare.com/learning/serverless/serverless-vs-containers/)[ What is serverless computing? ](https://www.cloudflare.com/learning/serverless/what-is-serverless/)

On this page

  * What are client side and server side?

  * What is the client-server model?

  * What does client side mean?

  * What does server side mean?

  * What is client-side scripting? What is server-side scripting?

  * How do server-side processes work in a serverless architecture?

  * Do Cloudflare Workers run server-side or client-side?




## What are client side and server side?

Client side and server side are web development terms that describe where application code runs. Web developers will also refer to this distinction as the frontend vs. the backend, although client-side/server-side and frontend/backend aren't quite the same. In a [serverless architecture](https://www.cloudflare.com/learning/serverless/what-is-serverless/), the serverless vendor hosts and assigns resources to all server-side processes, and the processes scale up as application usage increases.

## What is the client-server model?

Much of the Internet is based on the client-server model. In this model, user devices communicate via a network with centrally located servers to get the data they need, instead of communicating with each other. End user devices such as laptops, smartphones, and desktop computers are considered to be 'clients' of the servers, as if they were customers obtaining services from a company. Client devices send requests to the servers for webpages or applications, and the servers serve up responses.

The client-server model is used because servers are typically more powerful and more reliable than user devices. They also are constantly maintained and kept in controlled environments to make sure they're always on and available; although individual servers may go down, there are usually other servers backing them up. Meanwhile, users can turn their devices on and off, or lose or break their devices, and it should not impact Internet service for other users.

Servers can serve multiple client devices at once, and each client device sends requests to multiple servers in the course of accessing and browsing the Internet.

Multiple clients and servers interact:

![Many-to-many relationship within the client-server model](https://www.cloudflare.com/img/learning/serverless/glossary/client-side-vs-server-side/many-to-many-client-server-relationship.svg)Many-to-many relationship within the client-server model

Each client will communicate with multiple servers, and vice versa.

Suppose a user is browsing the Internet and types 'netflix.com' into their browser bar. This results in a request to [DNS](https://www.cloudflare.com/learning/dns/what-is-dns/) servers for the [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/) of netflix.com, and the DNS servers respond to this request by serving the IP address to the browser. Next, the user's browser makes a request to Netflix servers (using the IP address) for the content that appears on the page, such as the movie thumbnail images, the Netflix logo, and the search bar. Netflix servers deliver this to the browser, and the browser loads the page on the client device.

## What does client side mean?

In web development, 'client side' refers to everything in a web application that is displayed or takes place on the client (end user device). This includes what the user sees, such as text, images, and the rest of the UI, along with any actions that an application performs within the user's browser.

Markup languages like HTML and CSS are interpreted by the browser on the client side. In addition, many contemporary developers are including client-side processes in their application architecture and moving away from doing everything on the server side; business logic for dynamic webpages*, for instance, usually runs client side in a modern web application. Client-side processes are almost always written in JavaScript.

In the netflix.com example above, the HTML, CSS, and JavaScript that dictate how the Netflix main page appears to the user are interpreted by the browser on the client side. The page can also respond to 'events': For instance, if the user's mouse hovers over one of the movie thumbnail images, the image expands and adjacent thumbnails move slightly to one side to make room for the larger image. This is an example of a client-side process; the code within the webpage itself responds to the user's mouse and initiates this action without communicating with the server.

The client side is also known as the frontend, although these two terms do not mean precisely the same thing. Client-side refers solely to the location where processes run, while frontend refers to the kinds of processes that run client-side.

*A dynamic webpage is a webpage that does not display the same content for all users and changes based on user input. The Facebook homepage is a dynamic page; the Facebook login page is for the most part static.

## What does server side mean?

Much like with client side, 'server side' means everything that happens on the server, instead of on the client. In the past, nearly all business logic ran on the server side, and this included rendering dynamic webpages, interacting with databases, identity authentication, and push notifications.

The problem with hosting all of these processes on the server side is that each request involving one of them has to travel all the way from the client to the server, every time. This introduces a great deal of [latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/). For this reason, contemporary applications run more code on the client side; one use case is rendering dynamic webpages in real time by running scripts within the browser that make changes to the content a user sees.

Like with 'frontend' and 'client-side,' backend is also a term for the processes that take place on the server, although backend only refers to the types of processes and server-side refers to the location where processes run.

## What is client-side scripting? What is server-side scripting?

Client-side scripting simply means running scripts, such as JavaScript, on the client device, usually within a browser. All kinds of scripts can run on the client side if they are written in JavaScript, because JavaScript is universally supported. Other scripting languages can only be used if the user's browser supports them.

Server-side scripts run on the server instead of the client, often in order to deliver dynamic content to webpages in response to user actions. Server-side scripts don't have to be written in JavaScript, since the server may support a variety of languages.

Scripts run client-side and server-side:

![Client side scripting and server side scripting](https://www.cloudflare.com/img/learning/serverless/glossary/client-side-vs-server-side/client-side-scripts-server-side-scripts.svg)Client side scripting and server side scripting

Data passes back and forth between the client and server, and scripts can run on both sides.

## How do server-side processes work in a serverless architecture?

In serverless computing, all server-side or backend processes still run on servers instead of client devices, but they are not deployed on any specific server or set of servers. Backend processes are broken up into [functions](https://www.cloudflare.com/learning/serverless/glossary/function-as-a-service-faas/), which run on demand, and scale up automatically. Developers can still build all the functionality that normally runs server-side within a serverless architecture.

## Do Cloudflare Workers run server-side or client-side?

Cloudflare Workers are [serverless JavaScript](https://www.cloudflare.com/learning/serverless/serverless-javascript/) functions that run on demand, and they run on the edge network Cloudflare uses for CDN caching, in between the client and the origin server. This enables developers to build serverless backends that, while technically server-side, are located as close as possible to the client device, which reduces latency and causes applications to respond more quickly to user interactions.

To get started with Cloudflare Workers, see our [Developer documentation](https://developers.cloudflare.com/workers/).
