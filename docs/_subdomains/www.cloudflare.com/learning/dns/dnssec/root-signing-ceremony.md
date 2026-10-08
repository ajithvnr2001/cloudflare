---
url: https://www.cloudflare.com/learning/dns/dnssec/root-signing-ceremony/
title: The DNSSEC Root Signing Ceremony
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:09.085351+00:00
---

# The DNSSEC Root Signing Ceremony

> Source: https://www.cloudflare.com/learning/dns/dnssec/root-signing-ceremony/

[ Learning Center ](https://www.cloudflare.com/learning/) / DNS

##  The DNSSEC Root Signing Ceremony 

The root DNS zone contains information about how to query the top-level domain (TLD) name servers (.com, .edu, .org, etc). It enables Internet users to access domain names in all TLDs, even brand new ones like .software and .bank, making it an integral part of the global Internet. 

[Learning Center](https://www.cloudflare.com/learning)/DNS/[Common DNS issues and how to fix them](https://www.cloudflare.com/learning/dns/common-dns-issues/)[What is DNS cache poisoning? | DNS spoofing](https://www.cloudflare.com/learning/dns/dns-cache-poisoning/)[What is DNS fast flux?](https://www.cloudflare.com/learning/dns/dns-fast-flux/)[DNS over TLS vs. DNS over HTTPS | Secure DNS](https://www.cloudflare.com/learning/dns/dns-over-tls/)[DNS A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/)[DNS AAAA record](https://www.cloudflare.com/learning/dns/dns-records/dns-aaaa-record/)[What is a DNS CNAME record?](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/)[What is a DNS DKIM record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/)[What is a DNS DMARC record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/)[What is a DNS MX record?](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/)[DNS NS record](https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/)[What is a DNS PTR record?](https://www.cloudflare.com/learning/dns/dns-records/dns-ptr-record/)[What is a DNS SOA record?](https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/)[What is a DNS SPF record?](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/)[What is a DNS SRV record?](https://www.cloudflare.com/learning/dns/dns-records/dns-srv-record/)[What is a DNS TXT record?](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/)[DNS DNSKEY and DS Records](https://www.cloudflare.com/learning/dns/dns-records/dnskey-ds-records/)[How to protect domains that do not send email ](https://www.cloudflare.com/learning/dns/dns-records/protect-domains-without-email/)[ECDSA: The missing piece of DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/ecdsa-and-dnssec/)[How does DNSSEC work?](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/)[The DNSSEC Root Signing Ceremony](https://www.cloudflare.com/learning/dns/dnssec/root-signing-ceremony/)[Universal DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/universal-dnssec/)[How to choose the best domain name registrar](https://www.cloudflare.com/learning/dns/glossary/choose-the-best-domain-name-registrar/)[DNS root server](https://www.cloudflare.com/learning/dns/glossary/dns-root-server/)[What is a DNS zone?](https://www.cloudflare.com/learning/dns/glossary/dns-zone/)[Dynamic DNS](https://www.cloudflare.com/learning/dns/glossary/dynamic-dns/)[What happens to expired domains?](https://www.cloudflare.com/learning/dns/glossary/expired-domains/)[What is a premium domain?](https://www.cloudflare.com/learning/dns/glossary/premium-domains/)[Primary vs secondary DNS](https://www.cloudflare.com/learning/dns/glossary/primary-secondary-dns/)[What is reverse DNS?](https://www.cloudflare.com/learning/dns/glossary/reverse-dns/)[What is round-robin DNS?](https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/)[What is a domain name? | Domain name vs. URL](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/)[What is a domain name registrar?](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name-registrar/)[What is my IP address?](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/)[How much does a domain name cost?](https://www.cloudflare.com/learning/dns/how-much-does-a-domain-name-cost/)[How to buy a domain name](https://www.cloudflare.com/learning/dns/how-to-buy-a-domain-name/)[How to transfer a domain name](https://www.cloudflare.com/learning/dns/how-to-transfer-a-domain-name/)[What is a top-level domain (TLD)?](https://www.cloudflare.com/learning/dns/top-level-domain/)[What is 1.1.1.1?](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1)[What is a DNS server?](https://www.cloudflare.com/learning/dns/what-is-a-dns-server/)[What is a DNS server? (1) (PAYGO TEST)](https://www.cloudflare.com/learning/dns/what-is-a-dns-server-1-paygo-test/)[What is Anycast DNS? | How Anycast works with DNS](https://www.cloudflare.com/learning/dns/what-is-anycast-dns/)[What is cybersquatting?](https://www.cloudflare.com/learning/dns/what-is-cybersquatting/)[What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)[What is domain hijacking?](https://www.cloudflare.com/learning/dns/what-is-domain-hijacking/)[What is domain privacy?](https://www.cloudflare.com/learning/dns/what-is-domain-privacy/)[What is recursive DNS?](https://www.cloudflare.com/learning/dns/what-is-recursive-dns/)[DNS security](https://www.cloudflare.com/learning/dns/dns-security/)[DNS server types](https://www.cloudflare.com/learning/dns/dns-server-types/)[DNS records](https://www.cloudflare.com/learning/dns/dns-records/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand what the Root Signing Ceremony is 
  * Identify the key individuals involved in the Root Signing Ceremony 
  * Explore the Root Signing Ceremony procedure 



On this page

  * Where Is the Root-Signing Key?

  * Ceremony Participants

  * Ceremony Preparations

  * A Guy Walks Into a Room with Two Safes

  * The Credentials Safe

  * The Hardware Safe

  * Equipment Setup

  * Signing the Root DNS Keys

  * Public Record

  * Let’s See Those Signed Keys!

  * Summary




In [How DNSSEC Works](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/), we explained how trust in DNSSEC is derived from the parent zone’s DS resource record. However, the root DNS zone has no parent, so how can we trust the integrity and authenticity of its information?

![official ceremony photo](https://www.cloudflare.com/img/products/official-ceremony-photo.jpg)official ceremony photo

Photo courtesy of IANA

That’s the purpose of the Root Signing Ceremony—a rigorous procedure around signing the root DNS zone’s public keying information for the next few months. The private signing key used in this process is quite literally the key to the entire DNSSEC-protected Internet. A public, audited, and tightly controlled ceremony around accessing this key is a necessity for DNSSEC to succeed as a global standard.

Ólafur Guðmundsson, an engineering manager at Cloudflare and Crypto Officer at ICANN, participated in the ceremony this August. These are his reflections on the Root Signing Ceremony.

## Where Is the Root-Signing Key?

There are two geographically distinct locations that safeguard the root key-signing key: El Segundo, CA and Culpeper, VA. Both are secure facilities, and they contain redundant copies of the key. The ceremony alternates between the El Segundo and Culpeper locations.

## Ceremony Participants

  * The Ceremony Administrator

  * An Internal Witness

  * The Credentials Safe Controller

  * The Hardware Safe Controller

  * Crypto Officer #1

  * Crypto Officer #2

  * Crypto Officer #3




Each of these participants can only perform certain parts of the ceremony. Their roles are divided in a way that ensures less than a 1:1,000,000 chance that a group of conspirators could compromise the root-signing key, assuming a 5% dishonesty rate (yes, that’s formally in the specification) amongst these individuals.

The first four of these individuals are ICANN staff members, while the three crypto officers are trusted volunteers from the Internet community. Verisign also plays an important role, as they are the root zone maintainer responsible for generating the root zone-signing key that is signed during the ceremony. In addition, the entire procedure is audited by two Big Four auditing firms that are not associated with either Verisign or ICANN.

## Ceremony Preparations

There are only 14 available Crypto Officers in the world (7 are affiliated with each location), and at least three of them must attend the ceremony. So, the first step is to poll the Crypto Officers to find a two-day window when 4-5 of them can attend. We usually try to find a period where more than the minimum three are available, as emergencies or travel problems can cause a ceremony cancellation.

The last ceremony took place on August 13th at the El Segundo facility. To get into the facility, I had to show a government issued ID and show the contents of my bag. In return, I got an ID strip attached to my shirt. Then, I waited for an ICANN staffer to escort me inside. To get through the door, he had to swipe an access card and place his hand on a scanner.

The first stop was a conference room where lunch was being served. We mingled there while waiting for the rest of the ceremony participants to arrive. Being Crypto Officers, most of the small talk revolved around trying to steal root-signing key. We figured it would only take a half hour or so to blast a hole in the wall and walk out with the safe; however, that would probably trip the seismic sensors, so we would know that the key was compromised.

Once everybody showed up, we were escorted to the ceremony room in small groups as the entrance room only holds about 8 people. In this room we sign a log before we are allowed into the main key ceremony room. To access the entrance room, an ICANN staff member needs to use a smart card; to enter the main room a retina scan is needed of said staffer.

## A Guy Walks Into a Room with Two Safes

The ceremony room has a cage on the side of it that contains two safes. These safes store all of the sensitive material used during the ceremony. The cage can only be entered in the presence of the Ceremony Administrator and an Internal Witness. This is enforced by a second retina scan and access cards from both the Ceremony Administrator and Internal Witness.

However, neither the Ceremony Administrator or Internal Witness can actually open the safes. For that, we need the Safe Controllers

## The Credentials Safe

The Credentials Safe Controller opens the first safe, and inside we find several safe deposit boxes, each requiring two keys. The Ceremony Administrator has one of those keys, and each of the Crypto Officers has a key to a different box. Together (and in the presence of the Internal Witness and Credentials Safe Controller), the Ceremony Administrator and the Crypto Officers open three safe deposit boxes.

Each safe deposit box contains an operator card and a security permissions card for the Hardware Security Module (HSM), which we’ll discuss in the next section. Three operator cards are required to unlock the HSM, which is why three Crypto Officers must attend the ceremony. The security permissions cards are only used when we need to transfer the root-signing key, so we usually leave those in the safe deposit box.

Both cards are stored inside plastic cases wrapped in tamper-evident bags (most of the ceremony revolves around detecting foul-play, if you couldn’t tell already). These cards stay in the safe when not in use, which means the last time someone touched them was at the previous Root Signing Ceremony. The tamper-evident bags help ensure that they haven’t been altered in the interim.

The plastic cases are also very important, as someone discovered that it was possible to manipulate the cards by poking needles through the tamper evident bag, which would not necessarily be noticeable when inspecting the bag. This is a good example of how the security procedures around the ceremony are constantly evolving.

## The Hardware Safe

The Hardware Safe Controller then enters the safe room and opens up the second safe, which contains a tamper-proof hardware security module (HSM). The HSM is a physical computing device designed specifically for working with sensitive cryptographic material. You can think of it as a digital lock-box for the root-signing key. It can only be accessed with the three operator cards that we collected from the credentials safe.

The HSM can’t be operated without an external interface, so the hardware safe also contains a special laptop that can send commands to the HSM. This laptop has no battery, hard disk, or even a clock backup battery, and thus can’t store state once it’s unplugged. The goal is to eliminate any possibility of the root-signing key leaving the HSM after the ceremony ends.

We now have the hardware to perform the Root Signing Ceremony. Notice that the presence of all 7 participants is required to physically access the materials for the ceremony. Again, the idea is to minimize the risk of malicious conspirators by separating access to the HSM from access to the operator cards that activate the HSM.

A USB containing logs from each of the prior ceremonies and a DVD used to boot the laptop (both in their own tamper-evident bags) are also removed from this safe.

## Equipment Setup

We’re now ready to perform the actual Root Signing Ceremony. All of the equipment is laid out on a table in full view of all those attending, as well as the camera used to audit the proceedings.

One by one, each of the three Crypto Officers is called up to the table and asked to hand over the HSM operator card they took out of their safe deposit box. Before doing so, they verify that the tamper-evident bag is in the same condition as when they placed it in the safe deposit box at the end of the previous ceremony. Once they hand it over, only the Ceremony Administrator is allowed to touch the card.

The Ceremony Administrator boots the laptop from a DVD and initializes the USB that records the ceremony logs. Remember that the laptop has no clock battery backup, which means the time needs to be set manually from a special wall clock in the ceremony room. It’s the same clock used since the first ceremony five years ago, and it’s completely isolated from the rest of the world. It’s drifted slightly, but that’s fine, as it’s only used for logging purposes.

Ceremony table, before equipment setup

Next, the Ceremony Administrator needs to activate the HSM by placing the three operator cards collected from the Crypto Officers into the machine. Then, the HSM is connected to the laptop via ethernet cable. The Ceremony Administrator now has access to the root-signing key.

## Signing the Root DNS Keys

There are two geographically distinct locations that safeguard the root key-signing key: El Segundo, CA and Culpeper, VA. Both are secure facilities, and they contain redundant copies of the key. The ceremony alternates between the El Segundo and Culpeper locations.

The laptop/HSM system is air-gapped, meaning it is physically isolated from any potentially insecure computer networks (e.g., the Internet). The only way to move information from the outside world into the laptop/HSM is via USB drive. Accordingly, the key-signing request is loaded into the laptop via USB. To ensure that the correct key is being signed, a PGP hash of the key-signing request is computed, and Verisign verifies that it is identical to the one they provided.

Finally, the Ceremony Administrator can sign the KSR with the private key-signing key. He enters “Y” on a command prompt, and the dramatic portion of the ceremony is complete. The result is a collection of digital signatures, otherwise known in DNSSEC as the RRSIG record, which we’ll explore in a moment.

Note that the KSR actually contains a bundle of zone-signing keys that are rotated out every 15-16 days. There are enough keys in the bundle to last until the next Root Signing Ceremony three months from now.

## Public Record

Every tiny detail is recorded by auditors and [videotaped](https://www.iana.org/dnssec/ceremonies/22), making the whole ceremony a matter of public record. This is crucial if the entire DNSSEC-protected Internet is to trust the root name servers’ signatures.

This video is streamed live during the ceremony, and we were able to track how many people were watching the ceremony in real time. We had a record-breaking number of viewers this time, probably due to better publicity than previous ceremonies. We were even able to have a participant relay questions from the audience via chatroom. We were very happy about all this engagement.

At the end of the ceremony, logs are printed out and given to anybody in the room that wants a copy. Verisign is given a copy of the signed key set on a USB stick, and they will use these signed DNSKEY RRsets in the root zone during Q4 this year. All materials are put back into tamper-evident bags and placed in their respective safes.

## Let’s See Those Signed Keys!

There are two geographically distinct locations that safeguard the root key-signing key: El Segundo, CA and Culpeper, VA. Both are secure facilities, and they contain redundant copies of the key. The ceremony alternates between the El Segundo and Culpeper locations.

`dig . dnskey +dnssec`

This requests the dnskey records from the root DNS name servers. The interesting part of the response should look something like the following:

`. 20868 IN DNSKEY 257 3 8 AwEAAagAIKlVZrpC6Ia7gEzahOR+9W29euxhJhVVLOyQbSEW0O8gcCjF FVQUTf6v58fLjwBd0YI0EzrAcQqBGCzh/RStIoO8g0NfnfL2MTJRkxoX bfDaUeVPQuYEhg37NZWAJQ9VnMVDxP/VHL496M/QZxkjf5/Efucp2gaD X6RS6CXpoY68LsvPVjR0ZSwzz1apAzvN9dlzEheX7ICJBBtuA6G3LQpz W5hOA2hzCTMjJPJ8LbqF6dsV6DoBQzgul0sGIcGOYl7OyQdXfZ57relS Qageu+ipAdTTJ25AsRTAoub8ONGcLmqrAmRLKBP1dfwhYB4N7knNnulq QxA+Uk1ihz0= . 20868 IN DNSKEY 256 3 8 AwEAAa67bQck1JjopOOFc+iMISFcp/osWrEst2wbKbuQSUWu77QC9UHL ipiHgWN7JlqVAEjKITZz49hhkLmOpmLK55pTq+RD2kwoyNWk9cvpc+tS nIxT7i93O+3oVeLYjMWrkDAz7K45rObbHDuSBwYZKrcSIUCZnCpNMUtn PFl/04cb . 20868 IN RRSIG DNSKEY 8 0 172800 20150913235959 20150830000000 19036 . QKU/YSUHNXa0coshORV2r8o0PWZ43dn/u1ml4DglqLXTi2WJh+OyMFgi w4Xc7cF4T8Eab5TLbwqDHOrE87fmvcdSgQQOVwYN6jwStHAliuEICs6X rd+sqanyyMpaynLI630k5PuuQVOWxHn/Hyn4yFN5MJoQG9Pz+gn8FjCB oNGs0vu1TQm2m6DSGfjRTd7tRIchXAbOUvEVVnDWaTNPX3c35xqoHlUZ Ta00N9FvKqEwZDjdR1e0BCaDLL/Pk+CRygzOyfSKiuULzKEecsp3jPYY nXfKZmTuMuaQNRmcyJD+WSFwi5XyRgqrnxWUYmFcum4zw1NXdyp0mlGO slQ6NQ==`

The first record is the public counterpart to the private key-signing key in the HSM, the second is the zone-signing key provided by Verisign, and the third RRSIG record is what we created during the Root Signing Ceremony. Without that last one, the worldwide DNSSEC system wouldn’t work.

## Summary

The Root Signing Ceremony turns the root DNS name servers into a trust anchor. Instead of trust being derived from a parent zone, trust is assumed. This whole ceremony is designed to reinforce that trust. It’s a very human side of securing the Internet: the reason you can trust the root DNS servers is because you can trust the people signing it. And, the reason you can trust the people signing it is because of the strict protocols they follow while doing so. That’s what the Root Signing Ceremony is all about.
