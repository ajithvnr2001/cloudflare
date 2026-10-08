---
url: https://www.cloudflare.com/learning/ddos/ddos-attack-tools/slowloris/
title: Slowloris DDoS Attack
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:05.533363+00:00
---

# Slowloris DDoS Attack

> Source: https://www.cloudflare.com/learning/ddos/ddos-attack-tools/slowloris/

[ Learning Center ](https://www.cloudflare.com/learning/) / DDoS attacks

##  Slowloris DDoS attack 

The slowloris attack attempts to overwhelm a targeted server by opening and maintaining many simultaneous HTTP connections to the target. 

[Learning Center](https://www.cloudflare.com/learning)/DDoS attacks/[Application layer DDoS attack](https://www.cloudflare.com/learning/ddos/application-layer-ddos-attack/)[Cryptocurrency DDoS attacks](https://www.cloudflare.com/learning/ddos/cryptocurrency-ddos-attacks/)[What is a DDoS booter/IP stresser? | DDoS attack tools](https://www.cloudflare.com/learning/ddos/ddos-attack-tools/ddos-booter-ip-stresser/)[What is the High Orbit Ion Cannon (HOIC)?](https://www.cloudflare.com/learning/ddos/ddos-attack-tools/high-orbit-ion-cannon-hoic/)[How to DDoS | DoS and DDoS attack tools](https://www.cloudflare.com/learning/ddos/ddos-attack-tools/how-to-ddos/)[What is the low orbit ion cannon (LOIC)?](https://www.cloudflare.com/learning/ddos/ddos-attack-tools/low-orbit-ion-cannon-loic/)[R U Dead Yet? (R.U.D.Y.) attack](https://www.cloudflare.com/learning/ddos/ddos-attack-tools/r-u-dead-yet-rudy/)[Slowloris DDoS attack](https://www.cloudflare.com/learning/ddos/ddos-attack-tools/slowloris/)[What is a low and slow attack?](https://www.cloudflare.com/learning/ddos/ddos-low-and-slow-attack/)[What is DDoS mitigation?](https://www.cloudflare.com/learning/ddos/ddos-mitigation/)[DNS amplification attack](https://www.cloudflare.com/learning/ddos/dns-amplification-ddos-attack/)[Famous DDoS attacks: The largest DDoS attacks of all time](https://www.cloudflare.com/learning/ddos/famous-ddos-attacks/)[What is the Aisuru-Kimwolf botnet?](https://www.cloudflare.com/learning/ddos/glossary/aisuru-kimwolf-botnet/)[What is Anonymous Sudan?](https://www.cloudflare.com/learning/ddos/glossary/anonymous-sudan/)[What is blackhole routing?](https://www.cloudflare.com/learning/ddos/glossary/ddos-blackhole-routing/)[What is a denial-of-service (DoS) attack?](https://www.cloudflare.com/learning/ddos/glossary/denial-of-service/)[What is DNS](https://www.cloudflare.com/learning/ddos/glossary/domain-name-system-dns/)[What is HTTP?](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/)[What is the Internet Control Message Protocol (ICMP)?](https://www.cloudflare.com/learning/ddos/glossary/internet-control-message-protocol-icmp/)[What is the Internet of Things (IoT)?](https://www.cloudflare.com/learning/ddos/glossary/internet-of-things-iot/)[What is IP spoofing? ](https://www.cloudflare.com/learning/ddos/glossary/ip-spoofing/)[What is malware?](https://www.cloudflare.com/learning/ddos/glossary/malware/)[What is the Mirai Botnet?](https://www.cloudflare.com/learning/ddos/glossary/mirai-botnet/)[What is the OSI Model?](https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/)[What is TCP/IP?](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/)[What is UDP?](https://www.cloudflare.com/learning/ddos/glossary/user-datagram-protocol-udp/)[What is a WAF? | Web Application Firewall explained](https://www.cloudflare.com/learning/ddos/glossary/web-application-firewall-waf/)[How to prevent DDoS attacks | Methods and tools](https://www.cloudflare.com/learning/ddos/how-to-prevent-ddos-attacks/)[HTTP flood attack](https://www.cloudflare.com/learning/ddos/http-flood-ddos-attack/)[How do layer 3 DDoS attacks work? | L3 DDoS](https://www.cloudflare.com/learning/ddos/layer-3-ddos-attacks/)[Memcached DDoS attack](https://www.cloudflare.com/learning/ddos/memcached-ddos-attack/)[NTP amplification DDoS attack](https://www.cloudflare.com/learning/ddos/ntp-amplification-ddos-attack/)[Ping (ICMP) flood DDoS attack](https://www.cloudflare.com/learning/ddos/ping-icmp-flood-ddos-attack/)[Ping of death DDoS attack](https://www.cloudflare.com/learning/ddos/ping-of-death-ddos-attack/)[What is a ransom DDoS attack? ](https://www.cloudflare.com/learning/ddos/ransom-ddos-attack/)[Smurf DDoS attack](https://www.cloudflare.com/learning/ddos/smurf-ddos-attack/)[SSDP DDoS attack](https://www.cloudflare.com/learning/ddos/ssdp-ddos-attack/)[SYN flood attack](https://www.cloudflare.com/learning/ddos/syn-flood-ddos-attack/)[UDP flood attack](https://www.cloudflare.com/learning/ddos/udp-flood-ddos-attack/)[What is a DDoS attack?](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/)[What is a QUIC flood DDoS attack? | QUIC and UDP floods](https://www.cloudflare.com/learning/ddos/what-is-a-quic-flood/)[What is an ACK flood DDoS attack? | Types of DDoS attacks](https://www.cloudflare.com/learning/ddos/what-is-an-ack-flood/)[What is layer 7? | How layer 7 of the Internet works](https://www.cloudflare.com/learning/ddos/what-is-layer-7/)[What is a DDoS botnet?](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-botnet/)[DNS flood DDoS attack](https://www.cloudflare.com/learning/ddos/dns-flood-ddos-attack/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define a Slowloris DoS attack 
  * Explain how a Slowloris attack works 
  * Understand several mitigation strategies for a Slowloris attack 



Related content  [ What is a low and slow attack? ](https://www.cloudflare.com/learning/ddos/ddos-low-and-slow-attack/)[ What is a DDoS attack? ](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/)[ NTP amplification DDoS attack ](https://www.cloudflare.com/learning/ddos/ntp-amplification-ddos-attack/)

On this page

  * What is a Slowloris DDoS attack?

  * How does a Slowloris attack work?

    * A Slowloris attack occurs in 4 steps:

  * How is a Slowloris attack mitigated?

  * How does Cloudflare mitigate a Slowloris attack?




## What is a Slowloris DDoS attack?

Slowloris is a [denial-of-service](https://www.cloudflare.com/learning/ddos/glossary/denial-of-service/) attack program which allows an attacker to overwhelm a targeted server by opening and maintaining many simultaneous [HTTP](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/) connections between the attacker and the target.

![Slowloris Attack Diagram](https://www.cloudflare.com/img/learning/ddos/ddos-slowloris-attack/slowloris-attack-diagram.png)Slowloris Attack Diagram

## How does a Slowloris attack work?

Slowloris is an [application layer](https://www.cloudflare.com/learning/ddos/what-is-layer-7/) attack which operates by utilizing partial HTTP requests. The attack functions by opening connections to a targeted Web server and then keeping those connections open as long as it can.

Slowloris is not a category of attack but is instead a specific attack tool designed to allow a single machine to take down a server without using a lot of bandwidth. Unlike bandwidth-consuming reflection-based [DDoS attacks](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/) such as [NTP amplification](https://www.cloudflare.com/learning/ddos/ntp-amplification-ddos-attack/), this type of attack uses a low amount of bandwidth, and instead aims to use up server resources with requests that seem slower than normal but otherwise mimic regular traffic. It falls in the category of attacks known as [“low and slow” attacks](https://www.cloudflare.com/learning/ddos/ddos-low-and-slow-attack/). The targeted server will only have so many threads available to handle concurrent connections. Each server thread will attempt to stay alive while waiting for the slow request to complete, which never occurs. When the server’s maximum possible connections has been exceeded, each additional connection will not be answered and denial-of-service will occur.

#### A Slowloris attack occurs in 4 steps:

  * The attacker first opens multiple connections to the targeted server by sending multiple partial HTTP request headers.

  * The target opens a thread for each incoming request, with the intent of closing the thread once the connection is completed. In order to be efficient, if a connection takes too long, the server will timeout the exceedingly long connection, freeing the thread up for the next request.

  * To prevent the target from timing out the connections, the attacker periodically sends partial request headers to the target in order to keep the request alive. In essence saying, “I’m still here! I’m just slow, please wait for me.”

  * The targeted server is never able to release any of the open partial connections while waiting for the termination of the request. Once all available threads are in use, the server will be unable to respond to additional requests made from regular traffic, resulting in denial-of-service.




The key behind a Slowloris is its ability to cause a lot of trouble with very little bandwidth consumption.

## How is a Slowloris attack mitigated?

For web servers that are vulnerable to Slowloris, there are ways to mitigate some of the impact. Mitigation options for vulnerable servers can be broken down into 3 general categories:

  * **Increase server availability** \- Increasing the maximum number of clients the server will allow at any one time will increase the number of connections the attacker must make before they can overload the server. Realistically, an attacker may scale the number of attacks to overcome server capacity regardless of increases.

  * **Rate limit incoming requests** \- Restricting access based on certain usage factors will help mitigate a Slowloris attack. Techniques such as limiting the maximum number of connections a single [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/) is allowed to make, restricting slow transfer speeds, and limiting the maximum time a client is allowed to stay connected are all approaches for limiting the effectiveness of low and slow attacks.

  * **Cloud-based protection** \- Use a service that can function as a [reverse proxy](https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/), protecting the origin server.




## How does Cloudflare mitigate a Slowloris attack?

Cloudflare buffers incoming requests before starting to send anything to the [origin server](https://www.cloudflare.com/learning/cdn/glossary/origin-server/). As a result, “low and slow” attack traffic like Slowloris attacks never reach the intended target. Learn more about how Cloudflare's [DDoS protection](https://www.cloudflare.com/ddos/) stops slowloris attacks.
