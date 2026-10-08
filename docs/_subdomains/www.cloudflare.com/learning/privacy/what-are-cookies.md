---
url: https://www.cloudflare.com/learning/privacy/what-are-cookies/
title: What are cookies? | Learning Center
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:43.069614+00:00
---

# What are cookies? | Learning Center

> Source: https://www.cloudflare.com/learning/privacy/what-are-cookies/

[ Learning Center ](https://www.cloudflare.com/learning/) / privacy

##  What are cookies? 

HTTP cookies are small pieces of data stored on a user's device by web browsers to remember stateful information and track browsing activity. 

[Learning Center](https://www.cloudflare.com/learning)/privacy/[Why is encryption important for privacy?](https://www.cloudflare.com/learning/privacy/encryption-and-privacy/)[What is the right to be forgotten?](https://www.cloudflare.com/learning/privacy/right-to-be-forgotten/)[What are the Fair Information Practices? | FIPPs](https://www.cloudflare.com/learning/privacy/what-are-fair-information-practices-fipps/)[What is data compliance?](https://www.cloudflare.com/learning/privacy/what-is-data-compliance/)[What is data governance?](https://www.cloudflare.com/learning/privacy/what-is-data-governance/)[What is data localization?](https://www.cloudflare.com/learning/privacy/what-is-data-localization/)[What is data privacy?](https://www.cloudflare.com/learning/privacy/what-is-data-privacy/)[What is data sovereignty?](https://www.cloudflare.com/learning/privacy/what-is-data-sovereignty/)[What is end-to-end encryption (E2EE)?](https://www.cloudflare.com/learning/privacy/what-is-end-to-end-encryption/)[What is the ePrivacy Directive?](https://www.cloudflare.com/learning/privacy/what-is-eprivacy-directive/)[What is FedRAMP?](https://www.cloudflare.com/learning/privacy/what-is-fedramp/)[What is HIPAA compliance?](https://www.cloudflare.com/learning/privacy/what-is-hipaa-compliance/)[What is PCI DSS compliance? | PCI DSS definition](https://www.cloudflare.com/learning/privacy/what-is-pci-dss-compliance/)[What is personal information? | Personal data](https://www.cloudflare.com/learning/privacy/what-is-personal-information/)[What is PII (personally identifiable information)?](https://www.cloudflare.com/learning/privacy/what-is-pii/)[What is pseudonymization?](https://www.cloudflare.com/learning/privacy/what-is-pseudonymization/)[What is SOX compliance?](https://www.cloudflare.com/learning/privacy/what-is-sox-compliance/)[What is the CAN-SPAM Act?](https://www.cloudflare.com/learning/privacy/what-is-the-can-spam-act/)[What is the CCPA (California Consumer Privacy Act)?](https://www.cloudflare.com/learning/privacy/what-is-the-ccpa/)[What is the GDPR?](https://www.cloudflare.com/learning/privacy/what-is-the-gdpr/)[What are cookies?](https://www.cloudflare.com/learning/privacy/what-are-cookies/)[What is a warrant canary?](https://www.cloudflare.com/learning/privacy/what-is-warrant-canary/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define HTTP cookies 
  * Understand different types of cookies 
  * Know the privacy implications of cookies 



Related content  [ What is data privacy? ](https://www.cloudflare.com/learning/privacy/what-is-data-privacy/)

On this page

  * What are cookies on websites?

  * Where are cookies stored?

  * What are cookies used for?

  * What are the different types of cookies?

    * Session cookies

    * Persistent cookies

    * Authentication cookies

    * Tracking cookies

    * Zombie cookies

  * What is a third-party cookie?

  * How do cookies affect user privacy?




## What are cookies on websites?

Cookies are small files of information that a web server generates and sends to a web browser. Web browsers store the cookies they receive for a predetermined period of time, or for the length of a user's session on a website. They attach the relevant cookies to any future requests the user makes of the web server.

Cookies help inform websites about the user, enabling the websites to personalize the user experience. For example, [ecommerce websites](https://www.cloudflare.com/ecommerce/) use cookies to know what merchandise users have placed in their shopping carts. In addition, some cookies are necessary for security purposes, such as authentication cookies (see below).

The cookies that are used on the Internet are also called "HTTP cookies." Like much of the web, cookies are sent using the [HTTP protocol](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/).

Sign up

Security & speed with any Cloudflare plan

[Start for free](https://www.cloudflare.com/plans/)

## Where are cookies stored?

Web browsers store cookies in a designated file on users' devices. The Google Chrome web browser, for instance, stores all cookies in a file labeled "Cookies." Chrome users can view the cookies stored by the browser by [opening developer tools](https://developers.google.com/web/tools/chrome-devtools/open), clicking the "Application" tab, and clicking on "Cookies" in the left side menu.

## What are cookies used for?

**User sessions:** Cookies help associate website activity with a specific user. A session cookie contains a unique string (a combination of letters and numbers) that matches a user session with relevant data and content for that user.

Suppose Alice has an account on a shopping website. She logs into her account from the website's homepage. When she logs in, the website's server generates a session cookie and sends the cookie to Alice's browser. This cookie tells the website to load Alice's account content, so that the homepage now reads, "Welcome, Alice."

Alice then clicks to a product page displaying a pair of jeans. When Alice's web browser sends an HTTP request to the website for the jeans product page, it includes Alice's session cookie with the request. Because the website has this cookie, it recognizes the user as Alice, and she does not have to log in again when the new page loads.

**Personalization:** Cookies help a website "remember" user actions or user preferences, enabling the website to customize the user's experience.

If Alice logs out of the shopping website, her username can be stored in a cookie and sent to her web browser. Next time she loads that website, the web browser sends this cookie to the web server, which then prompts Alice to log in with the username she used last time.

**Tracking:** Some cookies record what websites users visit. This information is sent to the server that originated the cookie the next time the browser has to load content from that server. With third-party tracking cookies, this process takes place anytime the browser loads a website that uses that tracking service.

If Alice has previously visited a website that sent her browser a tracking cookie, this cookie may record that Alice is now viewing a product page for jeans. The next time Alice loads a website that uses this tracking service, she may see ads for jeans.

However, advertising is not the only use for tracking cookies. Many analytics services also use tracking cookies to anonymously record user activity. ([Cloudflare Web Analytics](https://www.cloudflare.com/web-analytics/) is one of the few services that does not use cookies to provide analytics, helping to protect user [privacy](https://www.cloudflare.com/learning/privacy/what-is-data-privacy/).)

Ebook

Overcoming 3 major data compliance challenges

[Read the ebook](https://www.cloudflare.com/lp/data-anywhere-compliance-ebook/)

## What are the different types of cookies?

Some of the most important types of cookies to know include:

#### Session cookies

A session cookie helps a website track a user's session. Session cookies are deleted after a user's session ends — once they log out of their account on a website or exit the website. Session cookies have no expiration date, which signifies to the browser that they should be deleted once the session is over.

#### Persistent cookies

Unlike session cookies, persistent cookies remain in a user's browser for a predetermined length of time, which could be a day, a week, several months, or even years. Persistent cookies always contain an expiration date.

#### Authentication cookies

Authentication cookies help manage user sessions; they are generated when a user logs into an account via their browser. They ensure that sensitive information is delivered to the correct user sessions by associating user account information with a cookie identifier string.

#### Tracking cookies

Tracking cookies are generated by tracking services. They record user activity, and browsers send this record to the associated tracking service the next time they load a website that uses that tracking service.

#### Zombie cookies

Like the "zombies" of popular fiction, zombie cookies regenerate after they are deleted. Zombie cookies create backup versions of themselves outside of a browser's typical cookie storage location. They use these backups to reappear within a browser after they are deleted. Zombie cookies are sometimes used by unscrupulous ad networks, and even by cyber attackers.

## What is a third-party cookie?

A third-party cookie is a cookie that belongs to a [domain](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/) other than the one displayed in the browser. Third-party cookies are most often used for tracking purposes. They contrast with first-party cookies, which are associated with the same domain that appears in the user's browser.

When Alice does her shopping at jeans.example.com, the jeans.example.com [origin server](https://www.cloudflare.com/learning/cdn/glossary/origin-server/) uses a session cookie to remember that she has logged into her account. This is an example of a first-party cookie. However, Alice may not be aware that a cookie from example.ad-network.com is also stored in her browser and is tracking her activity on jeans.example.com, even though she is not currently accessing example.ad-network.com. This is an example of a third-party cookie.

## How do cookies affect user privacy?

As described above, cookies can be used to record browsing activity, including for advertising purposes. However, many users do not want their online behavior to be tracked. Users also lack visibility or control over what tracking services do with the data they collect.

Even when cookie-based tracking is not tied to a specific user's name or device, with some types of tracking it could still be possible to link a record of a user's browsing activity with their real identity. This information could be used in any number of ways, from unwanted advertising to the monitoring, stalking, or harassment of users. (This is not the case with all cookie usage.)

Some privacy laws, like the EU's [ePrivacy Directive](https://www.cloudflare.com/learning/privacy/what-is-eprivacy-directive/), address and govern the use of cookies. Under this directive, users have to provide "informed consent" — they have to be notified of how the website uses cookies and agree to this usage — before the website can use cookies. (The exception to this is cookies that are "strictly necessary" for the website to function.) The EU's [General Data Protection Regulation (GDPR)](https://www.cloudflare.com/learning/privacy/what-is-the-gdpr/) considers cookie identifiers to be personal data, so its rules apply to cookie usage in the EU as well. Also, any personal data collected by cookies falls under the GDPR's jurisdiction.

Largely because of these laws, many websites now display cookie banners that allow users to review and control the cookies those websites use.
