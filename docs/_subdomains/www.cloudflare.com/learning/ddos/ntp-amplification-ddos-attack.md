---
url: https://www.cloudflare.com/learning/ddos/ntp-amplification-ddos-attack/
title: NTP Amplification DDoS Attack
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:32.523974+00:00
---

# NTP Amplification DDoS Attack

> Source: https://www.cloudflare.com/learning/ddos/ntp-amplification-ddos-attack/

[ Learning Center ](https://www.cloudflare.com/learning/) / DDoS attacks

##  NTP amplification DDoS attack 

A volumetric DDoS attack that takes advantage of a vulnerability in NTP protocol, with a goal of flooding a server with UDP traffic. 

[Learning Center](https://www.cloudflare.com/learning)/DDoS attacks/[Application layer DDoS attack](https://www.cloudflare.com/learning/ddos/application-layer-ddos-attack/)[Cryptocurrency DDoS attacks](https://www.cloudflare.com/learning/ddos/cryptocurrency-ddos-attacks/)[What is a DDoS booter/IP stresser? | DDoS attack tools](https://www.cloudflare.com/learning/ddos/ddos-attack-tools/ddos-booter-ip-stresser/)[What is the High Orbit Ion Cannon (HOIC)?](https://www.cloudflare.com/learning/ddos/ddos-attack-tools/high-orbit-ion-cannon-hoic/)[How to DDoS | DoS and DDoS attack tools](https://www.cloudflare.com/learning/ddos/ddos-attack-tools/how-to-ddos/)[What is the low orbit ion cannon (LOIC)?](https://www.cloudflare.com/learning/ddos/ddos-attack-tools/low-orbit-ion-cannon-loic/)[R U Dead Yet? (R.U.D.Y.) attack](https://www.cloudflare.com/learning/ddos/ddos-attack-tools/r-u-dead-yet-rudy/)[Slowloris DDoS attack](https://www.cloudflare.com/learning/ddos/ddos-attack-tools/slowloris/)[What is a low and slow attack?](https://www.cloudflare.com/learning/ddos/ddos-low-and-slow-attack/)[What is DDoS mitigation?](https://www.cloudflare.com/learning/ddos/ddos-mitigation/)[DNS amplification attack](https://www.cloudflare.com/learning/ddos/dns-amplification-ddos-attack/)[Famous DDoS attacks: The largest DDoS attacks of all time](https://www.cloudflare.com/learning/ddos/famous-ddos-attacks/)[What is the Aisuru-Kimwolf botnet?](https://www.cloudflare.com/learning/ddos/glossary/aisuru-kimwolf-botnet/)[What is Anonymous Sudan?](https://www.cloudflare.com/learning/ddos/glossary/anonymous-sudan/)[What is blackhole routing?](https://www.cloudflare.com/learning/ddos/glossary/ddos-blackhole-routing/)[What is a denial-of-service (DoS) attack?](https://www.cloudflare.com/learning/ddos/glossary/denial-of-service/)[What is DNS](https://www.cloudflare.com/learning/ddos/glossary/domain-name-system-dns/)[What is HTTP?](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/)[What is the Internet Control Message Protocol (ICMP)?](https://www.cloudflare.com/learning/ddos/glossary/internet-control-message-protocol-icmp/)[What is the Internet of Things (IoT)?](https://www.cloudflare.com/learning/ddos/glossary/internet-of-things-iot/)[What is IP spoofing? ](https://www.cloudflare.com/learning/ddos/glossary/ip-spoofing/)[What is malware?](https://www.cloudflare.com/learning/ddos/glossary/malware/)[What is the Mirai Botnet?](https://www.cloudflare.com/learning/ddos/glossary/mirai-botnet/)[What is the OSI Model?](https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/)[What is TCP/IP?](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/)[What is UDP?](https://www.cloudflare.com/learning/ddos/glossary/user-datagram-protocol-udp/)[What is a WAF? | Web Application Firewall explained](https://www.cloudflare.com/learning/ddos/glossary/web-application-firewall-waf/)[How to prevent DDoS attacks | Methods and tools](https://www.cloudflare.com/learning/ddos/how-to-prevent-ddos-attacks/)[HTTP flood attack](https://www.cloudflare.com/learning/ddos/http-flood-ddos-attack/)[How do layer 3 DDoS attacks work? | L3 DDoS](https://www.cloudflare.com/learning/ddos/layer-3-ddos-attacks/)[Memcached DDoS attack](https://www.cloudflare.com/learning/ddos/memcached-ddos-attack/)[NTP amplification DDoS attack](https://www.cloudflare.com/learning/ddos/ntp-amplification-ddos-attack/)[Ping (ICMP) flood DDoS attack](https://www.cloudflare.com/learning/ddos/ping-icmp-flood-ddos-attack/)[Ping of death DDoS attack](https://www.cloudflare.com/learning/ddos/ping-of-death-ddos-attack/)[What is a ransom DDoS attack? ](https://www.cloudflare.com/learning/ddos/ransom-ddos-attack/)[Smurf DDoS attack](https://www.cloudflare.com/learning/ddos/smurf-ddos-attack/)[SSDP DDoS attack](https://www.cloudflare.com/learning/ddos/ssdp-ddos-attack/)[SYN flood attack](https://www.cloudflare.com/learning/ddos/syn-flood-ddos-attack/)[UDP flood attack](https://www.cloudflare.com/learning/ddos/udp-flood-ddos-attack/)[What is a DDoS attack?](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/)[What is a QUIC flood DDoS attack? | QUIC and UDP floods](https://www.cloudflare.com/learning/ddos/what-is-a-quic-flood/)[What is an ACK flood DDoS attack? | Types of DDoS attacks](https://www.cloudflare.com/learning/ddos/what-is-an-ack-flood/)[What is layer 7? | How layer 7 of the Internet works](https://www.cloudflare.com/learning/ddos/what-is-layer-7/)[What is a DDoS botnet?](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-botnet/)[DNS flood DDoS attack](https://www.cloudflare.com/learning/ddos/dns-flood-ddos-attack/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define a NTP amplification DDoS attack 
  * Explain how a NTP amplification attack works 
  * Understand several mitigation strategies for this type of DDoS attack 



Related content  [ DNS flood DDoS attack ](https://www.cloudflare.com/learning/ddos/dns-flood-ddos-attack/)[ DNS amplification attack ](https://www.cloudflare.com/learning/ddos/dns-amplification-ddos-attack/)[ What is DDoS mitigation? ](https://www.cloudflare.com/learning/ddos/ddos-mitigation/)

On this page

  * What is a NTP amplification attack?

  * How does a NTP amplification attack work?

    * An NTP amplification attack can be broken down into four steps:

  * How is a NTP amplification attack mitigated?

    * Disable monlist - reduce the number of NTP servers which support the monlist command.

    * Source IP verification – stop spoofed packets leaving the network.

  * How does Cloudflare mitigate NTP amplification attacks?




## What is a NTP amplification attack?

An NTP amplification attack is a reflection-based volumetric [distributed denial-of-service (DDoS)](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/) attack in which an attacker exploits a Network Time Protocol (NTP) server functionality in order to overwhelm a targeted network or server with an amplified amount of [UDP](https://www.cloudflare.com/learning/ddos/glossary/user-datagram-protocol-udp/) traffic, rendering the target and its surrounding infrastructure inaccessible to regular traffic.

## How does a NTP amplification attack work?

All amplification attacks exploit a disparity in bandwidth cost between an attacker and the targeted web resource. When the disparity in cost is magnified across many requests, the resulting volume of traffic can [disrupt network infrastructure](https://www.cloudflare.com/the-net/network-infrastructure/). By sending small queries that result in large responses, the malicious user is able to get more from less. When multiplying this magnification by having each [bot](https://www.cloudflare.com/learning/bots/what-is-a-bot/) in a [botnet](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-botnet/) make similar requests, the attacker is both obfuscated from detection and reaping the benefits of greatly increased attack traffic.

[DNS flood attacks](https://www.cloudflare.com/learning/ddos/dns-flood-ddos-attack/) differ from [DNS amplification attacks](https://www.cloudflare.com/learning/ddos/dns-amplification-ddos-attack/). Unlike DNS floods, DNS amplification attacks reflect and amplify traffic off unsecured [DNS](https://www.cloudflare.com/learning/dns/what-is-dns/) servers in order to hide the origin of the attack and increase its effectiveness. DNS amplification attacks use devices with smaller bandwidth connections to make numerous requests to unsecured DNS servers. The devices make many small requests for very large [DNS records](https://www.cloudflare.com/learning/dns/dns-records/), but when making the requests, the attacker forges the return address to be that of the intended victim. The amplification allows the attacker to take out larger targets with only limited attack resources.

NTP amplification, much like DNS amplification, can be thought of in the context of a malicious teenager calling a restaurant and saying “I’ll have one of everything, please call me back and tell me my whole order.” When the restaurant asks for a callback number, the number given is the targeted victim’s phone number. The target then receives a call from the restaurant with a lot of information that they didn’t request.

The Network Time Protocol is designed to allow internet connected devices to synchronize their internal clocks, and serves an important function in internet architecture. By exploiting the monlist command enabled on some NTP servers, an attacker is able to multiply their initial request traffic, resulting in a large response. This command is enabled by default on older devices, and responds with the last 600 source IP addresses of requests which have been made to the NTP server. The monlist request from a server with 600 addresses in its memory will be 206 times larger than the initial request. This means that an attacker with 1 GB of internet traffic can deliver a 200+ gigabyte attack - a massive increase in the resulting attack traffic.

#### An NTP amplification attack can be broken down into four steps:

  * The attacker uses a botnet to send UDP packets with [spoofed IP](https://www.cloudflare.com/learning/ddos/glossary/ip-spoofing/) addresses to a NTP server which has its monlist command enabled. The spoofed IP address on each packet points to the real IP address of the victim.

  * Each UDP packet makes a request to the NTP server using its monlist command, resulting in a large response.

  * The server then responds to the spoofed address with the resulting data.

  * The IP address of the target receives the response and the surrounding network infrastructure becomes overwhelmed with the deluge of traffic, resulting in a [denial-of-service](https://www.cloudflare.com/learning/ddos/glossary/denial-of-service/).


![NTP Amplification DDoS Attack](https://www.cloudflare.com/img/learning/ddos/ntp-amplification-ddos-attack/ntp-amplification-attack-ddos-attack-diagram-2.png)NTP Amplification DDoS Attack

As a result of the attack traffic looking like legitimate traffic coming from valid servers, mitigating this sort of attack traffic without blocking real NTP servers from legitimate activity is difficult. Because UDP packets do not require a handshake, the NTP server will send large responses to the targeted server without verifying that the request is authentic. These facts coupled with a built-in command, which by default sends a large response, makes NTP servers an excellent reflection source for DDoS amplification attacks.

## How is a NTP amplification attack mitigated?

For an individual or company running a website or service, mitigation options are limited. This comes from the fact that the individual’s server, while it might be the target, is not where the main effect of a volumetric attack is felt. Due to the high amount of traffic generated, the infrastructure surrounding the server feels the impact. The Internet Service Provider (ISP) or other upstream infrastructure providers may not be able to handle the incoming traffic without becoming overwhelmed. As a result, the ISP may [blackhole](https://www.cloudflare.com/learning/ddos/glossary/ddos-blackhole-routing/) all traffic to the targeted victim’s IP address, protecting itself and taking the target’s site off-line. Mitigation strategies, aside from offsite protective services like Cloudflare DDoS protection, are mostly preventative internet infrastructure solutions.

#### Disable monlist - reduce the number of NTP servers which support the monlist command.

A simple solution to patching the monlist vulnerability is to disable the command. All version of the NTP software prior to version 4.2.7 are vulnerable by default. By upgrading a NTP server to 4.2.7 or above, the command is disabled, patching the vulnerability. If upgrading is not possible, following the US-CERT instructions will allow a server’s admin to make the necessary changes.

#### Source IP verification – stop spoofed packets leaving the network.

Because the UDP requests being sent by the attacker’s botnet must have a source [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/) spoofed to the victim’s IP address, a key component in reducing the effectiveness of UDP-based amplification attacks is for internet service providers (ISPs) to reject any internal traffic with spoofed IP addresses. If a packet is being sent from inside the network with a source address that makes it appear like it originated outside the network, it’s likely a spoofed packet and can be dropped. Cloudflare highly recommends that all providers implement ingress filtering, and at times will reach out to ISPs who are unknowingly taking part in DDoS attacks (in violation of BCP38) and help them realize their vulnerability.

The combination of disabling monlist on NTP servers and implementing ingress filtering on networks which presently allow IP spoofing is an effective way to stop this type of attack before it reaches its intended network.

## How does Cloudflare mitigate NTP amplification attacks?

With a properly configured [firewall](https://www.cloudflare.com/learning/security/what-is-a-firewall/) and sufficient network capacity (which isn't always easy to come by unless you are the size of Cloudflare), it's trivial to block reflection attacks such as NTP amplification attacks. Although the attack will target a single IP address, our [Anycast network](https://blog.cloudflare.com/a-brief-anycast-primer/) will scatter all attack traffic to the point where it is no longer disruptive. Cloudflare is able to use our advantage of scale to distribute the weight of the attack across many Data Centers, balancing the load so that service is never interrupted and the attack never overwhelms the targeted server’s infrastructure. During a recent six-month window, our DDoS mitigation system "Gatebot" detected 6,329 simple reflection attacks (that's one every 40 minutes), and the network successfully mitigated all of them. Learn more about Cloudflare's advanced [DDoS Protection.](https://www.cloudflare.com/ddos/)
