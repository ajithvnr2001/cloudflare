---
url: https://www.cloudflare.com/learning/access-management/what-is-browser-isolation/
title: What is browser isolation?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:54.886131+00:00
---

# What is browser isolation?

> Source: https://www.cloudflare.com/learning/access-management/what-is-browser-isolation/

[ Learning Center ](https://www.cloudflare.com/learning/) / access management

##  What is browser isolation? 

Browser isolation protects users from untrusted, potentially malicious websites and web content applications by confining browsing activity to a secured, remote environment. 

[Learning Center](https://www.cloudflare.com/learning)/access management/[How to implement Zero Trust security](https://www.cloudflare.com/learning/access-management/how-to-implement-zero-trust/)[What is the principle of least privilege?](https://www.cloudflare.com/learning/access-management/principle-of-least-privilege/)[What is security service edge (SSE)?](https://www.cloudflare.com/learning/access-management/security-service-edge-sse/)[What is a software-defined perimeter? | SDP vs. VPN](https://www.cloudflare.com/learning/access-management/software-defined-perimeter/)[What is browser isolation?](https://www.cloudflare.com/learning/access-management/what-is-browser-isolation/)[What is microsegmentation?](https://www.cloudflare.com/learning/access-management/what-is-microsegmentation/)[What is ZTNA?](https://www.cloudflare.com/learning/access-management/what-is-ztna/)[What is a CASB?](https://www.cloudflare.com/learning/access-management/what-is-a-casb/)[SASE vs. SSE](https://www.cloudflare.com/learning/access-management/sase-vs-sse/)[What is data loss prevention?](https://www.cloudflare.com/learning/access-management/what-is-dlp/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define browser isolation 
  * Explain the risks of using a web browser 
  * Describe the different types of browser isolation, including remote browser isolation 
  * Understand key use cases for RBI 



On this page

  * What is browser isolation?

  * Why do organizations use browser isolation?

    * Key benefits of browser isolation:

  * What is remote browser isolation?

    * How does remote browser isolation work?

  * What are the other types of browser isolation?

    * How does client-side browser isolation work?

  * What threats can RBI defend against?

  * Can RBI block threats that do not contain malicious web scripts?

  * How does Cloudflare Browser Isolation help?




## What is browser isolation?

Browser isolation (also known as remote browsing) is the cyber security approach of separating Internet browsing activity from the process of loading and displaying webpages locally.

Typically, a website visitor loads webpage content and code directly on the browser running on local devices. From a security perspective, this makes Internet browsing fairly risky, as this content and code often comes from unknown sources (e.g. cloud hosting and web servers). However, remote browser isolation (RBI) — the technology underpinning browser isolation — loads and executes web content in the cloud, away from local devices.

Just as machines can be used to monitor hazardous environments to keep humans away from harm, remote browsing “outsources” the detection of hazardous web content. This insulates Internet users (and the networks they connect to) from risky websites that carry [malware](https://www.cloudflare.com/learning/ddos/glossary/malware/) and other threats.

## Why do organizations use browser isolation?

Business processes no longer take place mostly within an [internal corporate network](https://www.cloudflare.com/learning/network-layer/enterprise-networking/). Instead, employees (whether onsite, fully remote, or hybrid) spend most of their time accessing websites and cloud-based applications such as email to perform their work — and they rely on web browsers to do so.

Just as [firewalls](https://www.cloudflare.com/learning/security/what-is-a-firewall/), [VPNs](https://www.cloudflare.com/learning/access-management/what-is-a-vpn/), and network [access control](https://www.cloudflare.com/learning/access-management/what-is-access-control/) help stop attacks directed at internal networks, browser isolation helps stop attacks originating from the browser.

Browser isolation is an important component of the [Zero Trust security](https://www.cloudflare.com/learning/security/glossary/what-is-zero-trust/) model, in which no connection request is inherently trusted by default. In this case, applying that Zero Trust principle to browsing means no website code should be trusted to run on devices by default.

#### Key benefits of browser isolation:

  * Preventing local downloads or execution of malware, [ransomware](https://www.cloudflare.com/learning/security/ransomware/what-is-ransomware/), and other malicious scripts

  * Blocking malicious web content without having to block entire websites

  * Minimizing the risk of [zero-day](https://www.cloudflare.com/learning/security/threats/zero-day-exploit/)* browser vulnerabilities




*_A zero-day exploit is an attack that uses a vulnerability that has not previously been identified or patched. Though rare, zero-day exploits are nearly impossible to stop._

## What is remote browser isolation (RBI)?

Remote browser isolation (RBI) technology, also called “cloud-hosted browser isolation, loads webpages and executes any associated code on a [cloud](https://www.cloudflare.com/learning/cloud/what-is-the-cloud/) server, far removed from users’ local devices and organizations' internal networks. The user's browsing session is deleted when it ends, so any malicious cookies or downloads associated with the session are eliminated.

#### How does remote browser isolation (RBI) work?

![Remote browser isolation: website code executed on remote server removed from client laptop](https://images.ctfassets.net/slt3lc6tev37/3xRG4dU3ErkppmbqnyMDVA/92ae8a2a2d75df950d2d4c7c149a17e5/remote_browser_isolation.png)Remote browser isolation: website code executed on remote server removed from client laptop

RBI technology keeps untrusted browser activity as far away as possible from user devices and corporate networks. It commonly does so by conducting a user’s web browsing activities on a cloud server controlled by an RBI vendor. The RBI service then transmits the resulting output to the user's device so that the user can interact with the webpages like normal, but without actually loading the full webpages on their local browser and device. Any user actions, such as mouse clicks, keyboard inputs, or form submissions, are transmitted to the cloud server, where further controls can be applied.

There are three ways a remote browser isolation server can send web content to a user's device:

**Stream the browser from the cloud:** This approach, also known as “pixel pushing,” renders and processes web content on a remote server instead of the user’s device. The server then sends a visual representation of the webpage to the user’s device as an interactive image or video stream. The high network bandwidth required can introduce [latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/) to the end-user’s browsing experience; however, this method can help ensure that malicious content remains confined to the remote server.

  * **Rewrite each webpage in the cloud to remove malicious content, then send to the local user browser.** With this method, referred to as Document Object Model ([DOM](https://www.cloudflare.com/learning/performance/how-dcl-and-fcp-affect-seo/)) reconstruction, webpages are loaded in an isolated environment and rewritten to remove potential attacks. Once the content is sanitized, it is sent to the user's device, where the webpage code loads and executes a second time. This approach can still send untrusted third-party code to local devices, but it is better than pixel pushing at maintaining the original webpage’s experience.

  * **Stream “draw” commands instead of actual website code.** Skia is the graphics engine that works across Android, Google Chrome, Chrome OS, Mozilla Firefox, and many other hardware and software platforms. In an RBI technique called network vector rendering (NVR), Skia “draw” commands are intercepted, [encrypted](https://www.cloudflare.com/learning/ssl/what-is-encryption/), then “streamed” to the web browser running locally on the user’s device. Because NVR streams draw commands rather than actual website code, it can be faster and more secure than pixel pushing and DOM reconstruction.




## What are the other types of browser isolation?

Common alternatives to RBI include _on-premise_ and _client-side_ browser isolation:

  * **On-premise browser isolation** performs the same activities as remote browser isolation, but on a server that an organization fully administers and manages internally.

  * **Client-side browser isolation** loads webpages on a user device on which special software has been installed. This software uses virtualization or sandboxing to keep all browsing activity on the virtual machine.




#### How does client-side browser isolation work?

![Client-side browser isolation: website code executed in sandbox within endpoint device](https://images.ctfassets.net/slt3lc6tev37/1L8Wq5uR42xA00XfnOqrB1/81193ed224cd482fefe0f53e0b0ecd77/client-side_browser_isolation.png)Client-side browser isolation: website code executed in sandbox within endpoint device

Client-side browser isolation virtualizes browser sessions; unlike remote and on-premise browser isolation, client-side browser isolation does this on the user device itself. It attempts to keep browsing separate from the rest of the device using either virtualization or sandboxing.

**Virtualization:** Virtualization is the process of dividing a computer into separate [virtual machines](https://www.cloudflare.com/learning/cloud/what-is-a-virtual-machine/) without physically altering the computer. This is done at a layer of software below the operating system called the "hypervisor." Theoretically, what happens on one virtual machine should not affect adjacent virtual machines, even when they are on the same device. By loading webpages on a separate virtual machine within the user's computer, the rest of the computer remains secure.

**Sandboxing:** A sandbox is similar to a virtual machine. It is a separate, contained virtual environment where testing can safely take place. Sandboxing is a common malware detection technique: many anti-malware tools open and execute potentially malicious files in a sandbox to see what they do. Some client-side browser isolation products use sandboxes to keep web browsing activity safely contained within the sandbox.

Because client-side browser isolation involves actually loading potentially malicious content on the user device, it still poses a risk to users and networks. Physical separation of harmful code from the device is a core concept of the other types of browser isolation; client-side browser isolation does not have this separation.

## What threats can RBI defend against?

All webpages and web apps are composed of HTML, CSS, and JavaScript code. While HTML and CSS are markup languages, meaning they only provide formatting instructions, JavaScript is a full programming language. While JavaScript is very useful for enabling many web application features, it can also be used maliciously.

Several different types of browser-based attacks are possible using JavaScript. Some of the most common include:

  * **Drive-by downloads:** Simply loading a webpage initiates the download of a malicious payload. Drive-by downloads usually take advantage of an unpatched vulnerability in a browser.

  * **Malvertising:** Malicious code is injected into legitimate ad networks. When the malicious ads are displayed, the code executes. The result is that visitors are redirected to malicious websites.

  * **Click-jacking:** A webpage is designed so that a user is fooled into clicking on something they did not intend to. Click-jacking can be used to generate fake ad revenue, send a user to an unsafe website, or even initiate a malware download.




Some other common in-browser attacks (that may or may not involve JavaScript) include:

  * **Redirect attacks:** A user attempts to load a legitimate URL but is then redirected to a URL controlled by an attacker.

  * **On-path browser attacks:** An [on-path](https://www.cloudflare.com/learning/security/threats/on-path-attack/) attacker exploits browser vulnerabilities to compromise a user's browser, at which point they can alter the web content shown to the user or even impersonate the user.

  * **Cross-site scripting:** [Malicious code](https://www.cloudflare.com/learning/security/threats/cross-site-scripting/) is injected into a website or web app. This allows attackers to carry out a variety of malicious activities, including stealing session [cookies](https://www.cloudflare.com/learning/privacy/what-are-cookies/) or login [tokens](https://www.cloudflare.com/learning/access-management/token-based-authentication/) and then impersonating legitimate users.




By isolating browser sessions in a controlled environment, malicious content and code is kept off user devices and away from the organization's network. For example, a drive-by download attack would have no effect on a user within an organization that uses browser isolation. The download would take place on a remote server or in a sandbox and would be destroyed at the end of the browsing session.

## Can RBI block threats that do not contain malicious web scripts?

In addition to stopping in-browser attacks, other emerging use cases for RBI include:

  * **Insulating users from malware:** RBI integration with [HTTPS inspection](https://www.cloudflare.com/learning/security/what-is-https-inspection/), a secure web gateway ([SWG](https://www.cloudflare.com/learning/access-management/what-is-a-secure-web-gateway/)), and other [Zero Trust security services](https://www.cloudflare.com/sase/use-cases/) can block the spread of viruses, worms, Trojans, ransomware, and other malware.

  * **Stopping multi-channel phishing attacks:** Attackers often use embedded email links as the initial means to expose users to account compromise or [data exfiltration](https://www.cloudflare.com/learning/security/what-is-data-exfiltration/). When integrated with Zero Trust cloud [email security](https://www.cloudflare.com/learning/email-security/what-is-email-security/), RBI can eliminate the risk of these “multi-channel” [phishing attacks](https://www.cloudflare.com/learning/access-management/phishing-attack/).

  * **Managing third-party permissions:** RBI integration with cloud-based identity and access management ([IAM](https://www.cloudflare.com/learning/access-management/what-is-identity-and-access-management/)) solutions can automate RBI policies for higher-risk, third-party users (such as blocking contractors from entering credentials onto certain webpages).




## How does Cloudflare Browser Isolation help?

A Zero Trust security model assumes that even though a user has safely loaded a website 99 times, the website might be compromised on the 100th time. Browser isolation is one way to [implement](https://www.cloudflare.com/learning/access-management/how-to-implement-zero-trust/) this assumption in practice.

As part of Cloudflare’s Zero Trust platform, [Cloudflare Browser Isolation](https://www.cloudflare.com/sase/products/browser-isolation/) applies this “never trust” mindset to Internet browsing. Zero Trust browsing insulates users from untrusted web content and protects data in browser interactions from untrusted users and devices.

Cloudflare’s RBI service applies NVR to stream safe draw commands to the device, which ensures compatibility with any webpage in any browser, stops transmissions of malicious web page code, and minimizes latency. Cloudflare Browser Isolation is included in Cloudflare One, a [SASE](https://www.cloudflare.com/learning/access-management/what-is-sase/) platform that combines network connectivity services with Zero Trust security services on a purpose-built global network.
