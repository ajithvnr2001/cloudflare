---
url: https://www.cloudflare.com/learning/ddos/smurf-ddos-attack/
title: Smurf DDoS Attack
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:38.147871+00:00
---

# Smurf DDoS Attack

> Source: https://www.cloudflare.com/learning/ddos/smurf-ddos-attack/

[ Learning Center ](https://www.cloudflare.com/learning/) / DDoS attacks

##  Smurf DDoS attack 

A smurf attack is a type of DDoS attack where a victim is flooded with ICMP requests. 

[Learning Center](https://www.cloudflare.com/learning)/DDoS attacks/[Application layer DDoS attack](https://www.cloudflare.com/learning/ddos/application-layer-ddos-attack/)[Cryptocurrency DDoS attacks](https://www.cloudflare.com/learning/ddos/cryptocurrency-ddos-attacks/)[What is a DDoS booter/IP stresser? | DDoS attack tools](https://www.cloudflare.com/learning/ddos/ddos-attack-tools/ddos-booter-ip-stresser/)[What is the High Orbit Ion Cannon (HOIC)?](https://www.cloudflare.com/learning/ddos/ddos-attack-tools/high-orbit-ion-cannon-hoic/)[How to DDoS | DoS and DDoS attack tools](https://www.cloudflare.com/learning/ddos/ddos-attack-tools/how-to-ddos/)[What is the low orbit ion cannon (LOIC)?](https://www.cloudflare.com/learning/ddos/ddos-attack-tools/low-orbit-ion-cannon-loic/)[R U Dead Yet? (R.U.D.Y.) attack](https://www.cloudflare.com/learning/ddos/ddos-attack-tools/r-u-dead-yet-rudy/)[Slowloris DDoS attack](https://www.cloudflare.com/learning/ddos/ddos-attack-tools/slowloris/)[What is a low and slow attack?](https://www.cloudflare.com/learning/ddos/ddos-low-and-slow-attack/)[What is DDoS mitigation?](https://www.cloudflare.com/learning/ddos/ddos-mitigation/)[DNS amplification attack](https://www.cloudflare.com/learning/ddos/dns-amplification-ddos-attack/)[Famous DDoS attacks: The largest DDoS attacks of all time](https://www.cloudflare.com/learning/ddos/famous-ddos-attacks/)[What is the Aisuru-Kimwolf botnet?](https://www.cloudflare.com/learning/ddos/glossary/aisuru-kimwolf-botnet/)[What is Anonymous Sudan?](https://www.cloudflare.com/learning/ddos/glossary/anonymous-sudan/)[What is blackhole routing?](https://www.cloudflare.com/learning/ddos/glossary/ddos-blackhole-routing/)[What is a denial-of-service (DoS) attack?](https://www.cloudflare.com/learning/ddos/glossary/denial-of-service/)[What is DNS](https://www.cloudflare.com/learning/ddos/glossary/domain-name-system-dns/)[What is HTTP?](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/)[What is the Internet Control Message Protocol (ICMP)?](https://www.cloudflare.com/learning/ddos/glossary/internet-control-message-protocol-icmp/)[What is the Internet of Things (IoT)?](https://www.cloudflare.com/learning/ddos/glossary/internet-of-things-iot/)[What is IP spoofing? ](https://www.cloudflare.com/learning/ddos/glossary/ip-spoofing/)[What is malware?](https://www.cloudflare.com/learning/ddos/glossary/malware/)[What is the Mirai Botnet?](https://www.cloudflare.com/learning/ddos/glossary/mirai-botnet/)[What is the OSI Model?](https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/)[What is TCP/IP?](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/)[What is UDP?](https://www.cloudflare.com/learning/ddos/glossary/user-datagram-protocol-udp/)[What is a WAF? | Web Application Firewall explained](https://www.cloudflare.com/learning/ddos/glossary/web-application-firewall-waf/)[How to prevent DDoS attacks | Methods and tools](https://www.cloudflare.com/learning/ddos/how-to-prevent-ddos-attacks/)[HTTP flood attack](https://www.cloudflare.com/learning/ddos/http-flood-ddos-attack/)[How do layer 3 DDoS attacks work? | L3 DDoS](https://www.cloudflare.com/learning/ddos/layer-3-ddos-attacks/)[Memcached DDoS attack](https://www.cloudflare.com/learning/ddos/memcached-ddos-attack/)[NTP amplification DDoS attack](https://www.cloudflare.com/learning/ddos/ntp-amplification-ddos-attack/)[Ping (ICMP) flood DDoS attack](https://www.cloudflare.com/learning/ddos/ping-icmp-flood-ddos-attack/)[Ping of death DDoS attack](https://www.cloudflare.com/learning/ddos/ping-of-death-ddos-attack/)[What is a ransom DDoS attack? ](https://www.cloudflare.com/learning/ddos/ransom-ddos-attack/)[Smurf DDoS attack](https://www.cloudflare.com/learning/ddos/smurf-ddos-attack/)[SSDP DDoS attack](https://www.cloudflare.com/learning/ddos/ssdp-ddos-attack/)[SYN flood attack](https://www.cloudflare.com/learning/ddos/syn-flood-ddos-attack/)[UDP flood attack](https://www.cloudflare.com/learning/ddos/udp-flood-ddos-attack/)[What is a DDoS attack?](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/)[What is a QUIC flood DDoS attack? | QUIC and UDP floods](https://www.cloudflare.com/learning/ddos/what-is-a-quic-flood/)[What is an ACK flood DDoS attack? | Types of DDoS attacks](https://www.cloudflare.com/learning/ddos/what-is-an-ack-flood/)[What is layer 7? | How layer 7 of the Internet works](https://www.cloudflare.com/learning/ddos/what-is-layer-7/)[What is a DDoS botnet?](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-botnet/)[DNS flood DDoS attack](https://www.cloudflare.com/learning/ddos/dns-flood-ddos-attack/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define a Smurf attack 
  * Understand how a Smurf attack works 
  * Implement a mitigation strategy for Smurf attacks 



Related content  [ Ping of death DDoS attack ](https://www.cloudflare.com/learning/ddos/ping-of-death-ddos-attack/)[ What is DDoS mitigation? ](https://www.cloudflare.com/learning/ddos/ddos-mitigation/)[ DNS flood DDoS attack ](https://www.cloudflare.com/learning/ddos/dns-flood-ddos-attack/)[ Cryptocurrency DDoS attacks ](https://www.cloudflare.com/learning/ddos/cryptocurrency-ddos-attacks/)

On this page

  * What is a Smurf attack?

  * How does a Smurf attack work?

    * Here&#39

  * How can a Smurf attack be mitigated?




## What is a Smurf attack?

A Smurf attack is a [distributed denial-of-service (DDoS) attack](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/) in which an attacker attempts to flood a targeted server with [Internet Control Message Protocol (ICMP)](https://www.cloudflare.com/learning/ddos/glossary/internet-control-message-protocol-icmp/) packets. By making requests with the [spoofed IP](https://www.cloudflare.com/learning/ddos/glossary/ip-spoofing/) address of the targeted device to one or more computer networks, the computer networks then respond to the targeted server, amplifying the initial attack traffic and potentially overwhelming the target, rendering it inaccessible. This attack vector is generally considered a solved vulnerability and is no longer prevalent.

## How does a Smurf attack work?

While ICMP packets can be utilized in a DDoS attack, normally they serve valuable functions in network administration. The ping application, which utilizes ICMP packets, is used by network administrators to test networked hardware devices such as computers, printers or routers. A ping is commonly used to see if a device is operational, and to track the amount of time it takes for the message to go round trip from the source device to the target and back to the source. Unfortunately, because the ICMP protocol does not include a handshake, hardware devices receiving requests are unable to verify if the request is legitimate.

This type of DDoS attack can be thought of metaphorically as a prankster calling an office manager and pretending to be the company’s CEO. The prankster asks the manager to tell each employee to call the executive back on his private number and give him an update on how they’re doing. The prankster gives the callback number of a targeted victim, who then receives as many unwanted phone calls as there are people in the office.

#### Here's how a Smurf attack works:

  * First the Smurf malware builds a spoofed packet that has its source address set to the real [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/) of the targeted victim.

  * The packet is then sent to an IP broadcast address of a router or [firewall](https://www.cloudflare.com/learning/security/what-is-a-firewall/), which in turn sends requests to every host device address inside the broadcasting network, increasing the number of requests by the number of networked devices on the network.

  * Each device inside the network receives the request from the broadcaster and then responds to the spoofed address of the target with an ICMP Echo Reply packet.

  * The target victim then receives a deluge of ICMP Echo Reply packets, potentially becoming overwhelmed and resulting in denial-of-service to legitimate traffic.




## How can a Smurf attack be mitigated?

Several mitigation strategies for this attack vector have been developed and implemented over the years, and the exploit is largely considered solved. On a limited number of legacy systems, mitigation techniques may still need to be applied. A simple solution is to disable IP broadcasting addresses at each network router and firewall. Older routers are likely to enable broadcasting by default, while newer routers will likely already have it disabled. In the event that a Smurf attack occurs, Cloudflare eliminates the attack traffic by preventing the ICMP packets from reaching the targeted [origin server](https://www.cloudflare.com/learning/cdn/glossary/origin-server/). Learn more about how Cloudflare's[DDoS Protection](https://www.cloudflare.com/ddos/) works.
