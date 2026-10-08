---
url: https://www.cloudflare.com/learning/ssl/connection-not-private-explained/
title: What Does 'Your Connection Is Not Private' Mean? | How to Fix SSL Errors
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:04.134467+00:00
---

# What Does 'Your Connection Is Not Private' Mean? | How to Fix SSL Errors

> Source: https://www.cloudflare.com/learning/ssl/connection-not-private-explained/

[ Learning Center ](https://www.cloudflare.com/learning/) / SSL

##  What does 'Your connection is not private' mean? 

If a website's SSL certificate is invalid or not available, users may see an error message when they attempt to load it. 

[Learning Center](https://www.cloudflare.com/learning)/SSL/[SSL certificate errors and how to fix them](https://www.cloudflare.com/learning/ssl/common-errors/)[What does 'Your connection is not private' mean?](https://www.cloudflare.com/learning/ssl/connection-not-private-explained/)[How does public key cryptography work?](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/)[How does SSL work? | SSL certificates and TLS](https://www.cloudflare.com/learning/ssl/how-does-ssl-work/)[How does keyless SSL work?](https://www.cloudflare.com/learning/ssl/keyless-ssl/)[How do lava lamps help with Internet encryption?](https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/)[What is post-quantum cryptography (PQC)?](https://www.cloudflare.com/learning/ssl/quantum/what-is-post-quantum-cryptography/)[What is quantum computing?](https://www.cloudflare.com/learning/ssl/quantum/what-is-quantum-computing/)[What is TLS (Transport Layer Security)?](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)[Types of SSL certificates: SSL certificate types explained](https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/)[What happens in a TLS handshake? | SSL handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)[What is a cryptographic key?](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/)[What is a session key? Session keys and TLS handshakes](https://www.cloudflare.com/learning/ssl/what-is-a-session-key/)[What is asymmetric encryption?](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/)[What is domain spoofing? | Website and email spoofing](https://www.cloudflare.com/learning/ssl/what-is-domain-spoofing/)[What is encrypted SNI? | How ESNI works](https://www.cloudflare.com/learning/ssl/what-is-encrypted-sni/)[What is encryption?](https://www.cloudflare.com/learning/ssl/what-is-encryption/)[What is mixed content?](https://www.cloudflare.com/learning/ssl/what-is-mixed-content/)[What is mutual TLS (mTLS)?](https://www.cloudflare.com/learning/ssl/what-is-mutual-tls/)[What is SNI? How TLS server name indication works](https://www.cloudflare.com/learning/ssl/what-is-sni/)[What is SSL?](https://www.cloudflare.com/learning/ssl/what-is-ssl/)[Why is HTTP not secure? | HTTP vs. HTTPS](https://www.cloudflare.com/learning/ssl/why-is-http-not-secure/)[Why use HTTPS?](https://www.cloudflare.com/learning/ssl/why-use-https/)[Why use TLS 1.3?](https://www.cloudflare.com/learning/ssl/why-use-tls-1.3)[What is TLS?](https://www.cloudflare.com/learning/ssl/what-is-tls/)[What is an SSL certificate?](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)[What is HTTPS?](https://www.cloudflare.com/learning/ssl/what-is-https/)

######  Learning objectives 

After reading this article you will be able to: 

  * Learn what "Your connection is not private/secure" error messages mean in a browser 
  * Understand how problems with an SSL certificate can cause these errors 
  * Learn how to fix these errors 



Related content  [ What is HTTPS? ](https://www.cloudflare.com/learning/ssl/what-is-https/)[ Why use HTTPS? ](https://www.cloudflare.com/learning/ssl/why-use-https/)[ How does SSL work? | SSL certificates and TLS ](https://www.cloudflare.com/learning/ssl/how-does-ssl-work/)[ Types of SSL certificates: SSL certificate types explained ](https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/)[ What happens in a TLS handshake? | SSL handshake ](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)

On this page

  * What does the &#39

  * What is an SSL certificate? What is HTTPS?

  * What causes this SSL error?

  * How to fix &#39

    * For users

    * For website owners

  * What does &#39

  * How does Cloudflare help prevent these kinds of errors?




## What does the 'Your connection is not private' error mean?

Users may occasionally find themselves blocked from reaching a website by a "Your connection is not private" message. This error means that the connection between the [client](https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/) (the user's device, such as a laptop or tablet) and the server (the website host) is not encrypted, even though the client device expected it to be encrypted.

![Connection Not Private](https://images.ctfassets.net/slt3lc6tev37/7sPeJvuqzm4sb3Sz1TYcOX/6fbfe5bc7e7b056464cb0e11a3c59f6f/connection-not-private.png)Connection Not Private

As a result, attackers will be able to see what the user does on the website – messages between the client and the server are sent in plaintext, instead of being scrambled via [encryption](https://www.cloudflare.com/learning/ssl/what-is-encryption/). In addition, the client is unable to verify that it is connected to the correct server.

This is why the browser will say "Your connection is not private" or "Your connection is not secure": it can't verify the web server, and it can't encrypt messages to stop attackers from reading them.

This error is caused by an issue with the website's [SSL certificate](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/) – it's missing, or it's expired, or it wasn't issued by a legitimate certificate authority, or the client can't access it for some other reason. SSL certificates are necessary for serving websites over secure [HTTPS](https://www.cloudflare.com/learning/ssl/what-is-https/) connections.

An invalid or missing SSL certificate is almost the cryptographic equivalent of a cashier at a corner store asking a man for identification in order to prove he's old enough to purchase alcohol, and instead of producing a government-issued ID card, he pulls out a piece of paper on which someone has written, "This man is named Jeff, and he is 22 years old." This, of course, is not legitimate identification. The man may not in fact be 22 years old, and for that matter the man might not even be named Jeff. The cashier is right to respond with suspicion and terminate the transaction altogether.

Much like Jeff, a website without an SSL certificate cannot prove its identity. On top of that, a website without an SSL certificate can't encrypt communications – imagine if Jeff's lack of an ID card meant that anyone around the world could suddenly hear the conversation between Jeff and the cashier.

  * In Google Chrome, the error message is: "Your connection is not private," followed by "Attackers might be trying to steal your information from [website]"

  * In Mozilla Firefox, it's: "Your connection is not secure"

  * In Microsoft Edge, it's also "Your connection is not secure"




Often users can still continue on to the page in spite of this message, although this is not recommended. Without HTTPS, a variety of cyber attacks are possible.

## What is an SSL certificate? What is HTTPS?

An SSL certificate verifies ownership of a website and makes opening a secure, encrypted connection possible. It's a text file installed on a web server with information like:

  * Expiration date of the certificate

  * The [domain name](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/) that the certificate was issued for

  * Which person, organization, or device owns the domain

  * The certificate authority that issued the certificate

  * The [public key](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/)




An SSL certificate is necessary for encrypting communications to and from a website using [SSL](https://www.cloudflare.com/learning/ssl/what-is-ssl/), or [TLS](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/), encryption. This is also known as [HTTPS.](https://www.cloudflare.com/learning/ssl/what-is-https/)

If data is encrypted with TLS/SSL, when someone intercepts the data going back and forth between client and server, it just looks like random nonsense to them. If data is not encrypted, someone can intercept the data and easily read it. Encryption is like an envelope protecting the contents of a personal letter as it goes through the mail.

## What causes this SSL error?

A number of [issues with the SSL certificate](https://www.cloudflare.com/learning/ssl/common-errors/) can cause the "Your connection is not private" error:

**The website's SSL certificate isn't valid or is missing.** This could be the case for a number of reasons. It can mean that the SSL certificate presented lists the wrong website, that the SSL certificate has expired, or that there's no SSL certificate at all when one was expected – for instance, if a user types <https://www.example.com> into a browser, but example.com doesn't have HTTPS.

**The SSL certificate doesn't list variations on the domain name.** For example, the SSL certificate may list [www.example.com](http://www.example.com), but not example.com (without the "www"). This happens when the Subject Alternative Name (SAN) section of an SSL certificate is not filled out properly. As a result, the website has a working SSL certificate, but there's a mismatch between the URL the user typed in and what's listed on the certificate. The browser therefore considers the certificate invalid.

**The web server presented an SSL certificate for the wrong website.** This can happen when multiple websites are hosted at one [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/). If each of those websites has its own SSL certificate, the server may not know which SSL certificate to show when a client device tries to securely connect to one of the websites – much like when a package is mailed to an apartment complex but the apartment number is not included in the address. An [extension to the TLS protocol called SNI](https://www.cloudflare.com/learning/ssl/what-is-sni/) helps prevent this error.

Other possible causes include:

  * The certificate is self-signed, meaning it was generated by the website operator instead of a third-party certificate authority

  * The browser doesn't recognize the certificate authority that issued the certificate

  * Symantec issued the SSL certificate (all Symantec-issued SSL certificates are not trusted by the major browsers)

  * The SSL certificate may have unsupported features (like using SHA-1 hashing instead of SHA-256)

  * The client device's clock is inaccurate, and consequently it isn't able to verify whether or not the SSL certificate has expired




## How to fix 'Your connection is not private' errors

#### For users

  * _Refresh the page:_ Network connections involve a lot of back-and-forth communication between client and server that mostly goes unnoticed by the user. Any number of these communications may not go correctly. For this reason, a variety of errors can be solved by trying again and reloading the page.

  * _Clear browser cache:_ A browser stores some information and content from websites users have visited before in a temporary storage location known as a "[cache.](https://www.cloudflare.com/learning/cdn/what-is-caching/)" Clearing the browser cache and trying to load the page again can have a similar effect to refreshing the page: the website has a clean slate from the browser's perspective, and the browser can try to make the proper connections again. Alternatively, users can also open the page in Incognito mode (Chrome), Private mode (Firefox and Safari), or InPrivate mode (Edge); in these modes the browser does not access the cache.

  * _Reset the clock:_ Users can also try resetting their computer's clock, which may be inaccurate, causing the device to incorrectly reject an SSL certificate as expired or invalid.

  * _Add 'www':_ To circumvent SAN errors, users can try retyping the domain name so that it includes "www" (or whatever the domain prefix is).

  * _Use a different browser, or update the browser:_ Old versions of browsers may not support necessary features for TLS encryption (such as SNI). Make sure to use the latest versions of browsers.




#### For website owners

  * _Obtain a new SSL certificate:_ If the certificate is expired, outmoded, or self-signed, a website will need to obtain a new one from a certificate authority. (Cloudflare offers [free SSL certificates](https://www.cloudflare.com/application-services/products/ssl/), along with customized certificates for enterprise customers).

  * _Make sure SAN is filled out, and subdomains are included:_ If the SSL certificate is otherwise valid, be sure all legitimate variations on the domain are listed. Also, subdomains – blog.example.com in addition to [www.example.com](http://www.example.com) – should be listed.

  * _If a website doesn't have HTTPS, make sure all backlinks are HTTP only:_ If a user inadvertently tries to load a URL over HTTPS when the website only uses HTTP, they may get this error, because the browser has tried to obtain the website's SSL certificate when there isn't one. In addition to fixing backlinks, a website should set up redirects to HTTP in the event someone tries to load it over HTTPS. **Also, it is highly recommended that such websites obtain SSL certificates.**




## What does 'Your connection to this site is not secure' mean?

In Chrome, this message appears when clicking on the "Not Secure" in the browser bar when on an HTTP site. It means that the website does not have an SSL certificate and does not use SSL/TLS for encrypting traffic to and from the site. Browsers won't typically block websites that don't have HTTPS, but users should avoid entering personal data, like login credentials, credit card data, or government-issued ID numbers, on non-HTTPS websites.

## How does Cloudflare help prevent these kinds of errors?

Cloudflare offers free SSL/TLS encryption for any website. Websites with Cloudflare TLS encryption should not encounter most of these errors, although improperly configured client devices could still cause them to pop up from time to time. [Learn more about free SSL certificates from Cloudflare](https://www.cloudflare.com/application-services/products/ssl/).

Cloudflare offers free SSL/TLS encryption for any website. Websites with Cloudflare TLS encryption should not encounter most of these errors, although improperly configured client devices could still cause them to pop up from time to time. Learn more about [free SSL certificates from Cloudflare](https://www.cloudflare.com/application-services/products/ssl/).
