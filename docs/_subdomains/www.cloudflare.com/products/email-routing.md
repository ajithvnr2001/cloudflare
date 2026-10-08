---
url: https://www.cloudflare.com/products/email-routing/
title: Cloudflare Email Routing - Private Email Address Management
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:03:11.189434+00:00
---

# Cloudflare Email Routing - Private Email Address Management

> Source: https://www.cloudflare.com/products/email-routing/

Email Routing 

## Efficient Email Routing with Custom Addresses

### Cloudflare Email Routing is a free, private service for creating custom email addresses and forwarding messages to any inbox, protecting your primary email from spam. It's ideal for individuals, families, and businesses seeking to simplify their inboxes and safeguard their email addresses.

[ Start building for free ](https://dash.cloudflare.com/sign-up) [ View docs ](https://developers.cloudflare.com/email-routing/)

**Private by Design**

Cloudflare Email Routing ensures 100% privacy, storing and accessing no email content. Our service includes phishing detection to prevent spam from being forwarded to destination mailboxes.

**Effortless Configuration**

Creating custom addresses and forwarding messages to your inbox is free and easy. DNS records are automatically created and protected from accidental changes.

**Insightful Analytics**

Gain access to detailed analytics, including the number of emails sent, forwarded, or dropped, and delivery success rates at your destination mailbox.

### Visualizing Email Routing

Streamline email management with Cloudflare Email Routing

Faster

Slower

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

`Email Routing`

####  You can use Email Routing to: 

See real-world examples of Cloudflare Email Routing 

[ Start with Email Routing  ](https://developers.cloudflare.com/email-routing/)

Personal Inbox Organization 

Create custom email addresses for various needs, like newsletters or business communications, without exposing your primary email address. This helps individuals manage their inbox efficiently and keep their personal email private.

Family Communication Organization 

Designate custom email addresses for family members or specific purposes, such as household bills or school communications. This keeps family email communications organized and easy to manage.

Business Email Management 

Route emails for different types of inquiries, like sales or support, and easily control who receives these messages. This helps businesses manage their email communications more efficiently and provide better customer service.

Custom Email Processing 

Route emails to Cloudflare Workers for custom processing logic. This enables advanced email processing and automation, allowing businesses to integrate their email communications with existing workflows.

### Email Routing Code Examples

Integrate Cloudflare Email Routing with your applications

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

create_email_address.sh  email_worker.js  email_analytics.py  dns_records.html 

1  2  3  4  5 
    
    
    curl -X POST \  https://api.cloudflare.com/client/v4/zones/:zone_identifier/email_routing/addresses \  -H 'Content-Type: application/json' \  -H 'Authorization: Bearer YOUR_API_TOKEN' \  -d '{"address": "custom@example.com", "forward_to": "your_email@example.com"}'

1  2  3  4  5  6  7  8  9 
    
    
    addEventListener('email', async (event) => {  const { message } = event;  // Process the email message  const response = await fetch(    'https://api.cloudflare.com/client/v4/zones/:zone_identifier/email_routing/addresses',    {      method: 'POST',      headers: { 'Content-Type': 'application/json' },      body: JSON.stringify({        address: 'custom@example.com',        forward_to: 'your_email@example.com',      }),    },  );});

1  2  3  4  5  6  7  8  9 
    
    
    import requests
    zone_identifier = 'your_zone_identifier'api_token = 'your_api_token'
    response = requests.get(f'https://api.cloudflare.com/client/v4/zones/{zone_identifier}/email_routing/analytics',                         headers={'Authorization': f'Bearer {api_token}'})
    print(response.json())

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17 
    
    
    <table>  <tr>    <th>Type</th>    <th>Name</th>    <th>Value</th>  </tr>  <tr>    <td>MX</td>    <td>@</td>    <td>mail.cloudflare.com</td>  </tr>  <tr>    <td>TXT</td>    <td>@</td>    <td>v=spf1 include:_spf.cloudflare.com ~all</td>  </tr></table>

Create a Custom Email Address 

Use cURL to create a custom email address for your domain and route messages to your preferred inbox.

Route Emails to Cloudflare Workers 

Use Cloudflare Workers to programmatically process incoming emails and route them to your preferred inbox.

Fetch Email Routing Analytics 

Use Python to fetch analytics data for your routed emails, including delivery success rates and spam filtering metrics.

Configure Email Routing with DNS 

Configure email routing for your domain using DNS records.

###  Powerful primitives, seamlessly integrated 

#####  Built on systems powering 20% of the Internet, Email Routing runs on the same infrastructure Cloudflare uses to build Cloudflare. Enterprise-grade reliability, security, and performance are standard. 

[ Compute ](https://www.cloudflare.com/products/#compute)

[ Browser Run  Automated browsers  ](https://www.cloudflare.com/products/browser-run/)

[ Containers  Any language, anywhere  ](https://www.cloudflare.com/products/containers/)

[ Durable Objects  Stateful compute  ](https://www.cloudflare.com/products/durable-objects/)

[ Sandboxes  Secure code execution  ](https://www.cloudflare.com/products/sandboxes/)

[ Workers  Global serverless functions  ](https://www.cloudflare.com/products/workers/)

[ Workers for Platforms  Programmable Platform Solutions  ](https://www.cloudflare.com/products/workers-for-platforms/)

[ Workflows  Process orchestration  ](https://www.cloudflare.com/products/workflows/)

[ Storage ](https://www.cloudflare.com/products/#storage)

[ Artifacts  Git-native versioned storage  ](https://www.cloudflare.com/products/artifacts/)

[ D1  Serverless SQL  ](https://www.cloudflare.com/products/d1/)

[ Basin  Ingest, catalog & query data  ](https://www.cloudflare.com/products/data-platform/)

[ Hyperdrive  Global databases  ](https://www.cloudflare.com/products/hyperdrive/)

[ K2  Publish and subscribe to durable, ordered event streams  ](https://www.cloudflare.com/products/k2/)

[ Queues  Message processing  ](https://www.cloudflare.com/products/queues/)

[ R2  Egress-free storage  ](https://www.cloudflare.com/products/r2/)

[ KV  Ultra-fast key-value storage  ](https://www.cloudflare.com/products/kv/)

[ AI ](https://www.cloudflare.com/products/#ai)

[ Agents  Build stateful AI agents  ](https://www.cloudflare.com/products/agents/)

[ AI Gateway  AI observability  ](https://www.cloudflare.com/products/ai-gateway/)

[ AI Search  Instant retrieval  ](https://www.cloudflare.com/products/ai-search/)

[ Vectorize  Vector database  ](https://www.cloudflare.com/products/vectorize/)

[ Workers AI  Edge AI models  ](https://www.cloudflare.com/products/workers-ai/)

[ SASE / Zero Trust ](https://www.cloudflare.com/products/#sase)

[ SASE  Cloudflare SASE platform  ](https://www.cloudflare.com/sase/)

[ Access  Zero trust access to private resources  ](https://www.cloudflare.com/products/access/)

[ CASB  SaaS and cloud posture  ](https://www.cloudflare.com/products/casb/)

[ Data Loss Prevention  Protect sensitive data  ](https://www.cloudflare.com/products/dlp/)

[ Gateway  Web filtering  ](https://www.cloudflare.com/products/gateway/)

[ Browser Isolation  Secure web browsing  ](https://www.cloudflare.com/products/browser-isolation/)

[ WAN  Cloud-delivered networking  ](https://www.cloudflare.com/products/wan/)

[ Email Security  Phishing protection  ](https://www.cloudflare.com/products/email-security/)

[ Security ](https://www.cloudflare.com/products/#security)

[ DDoS Protection  Mitigation Solutions  ](https://www.cloudflare.com/products/ddos/)

[ Rate Limiting  Abuse prevention  ](https://www.cloudflare.com/products/rate-limiting/)

[ SSL  Secure Your Site with SSL  ](https://www.cloudflare.com/products/ssl/)

[ Turnstile  A CAPTCHA Replacement Solution  ](https://www.cloudflare.com/products/turnstile/)

[ WAF  Web Application Firewall  ](https://www.cloudflare.com/products/waf/)

[ Magic Transit  DDoS Protection for Networks  ](https://www.cloudflare.com/products/magic-transit/)

[ Client-Side Security  Prevent browser supply chain attacks  ](https://www.cloudflare.com/products/client-side-security/)

[ Bot Management  Block bad bots  ](https://www.cloudflare.com/products/bot-management/)

[ Network & Content Delivery ](https://www.cloudflare.com/products/#network)

[ CDN  Faster delivery & caching  ](https://www.cloudflare.com/products/cdn/)

[ DNS  Fast DNS  ](https://www.cloudflare.com/products/dns/)

[ Load Balancing  Zero downtime  ](https://www.cloudflare.com/products/load-balancing/)

[ TURN / SFU  Real-time infra  ](https://www.cloudflare.com/products/turn-sfu/)

[ Analytics  Web Performance & Security  ](https://www.cloudflare.com/products/analytics/)

# Build without boundaries

Join thousands of developers who've eliminated infrastructure complexity and deployed globally with Cloudflare. Start building for free — no credit card required. 

[ Start building for free  ](https://dash.cloudflare.com/sign-up)[ View docs  ](https://developers.cloudflare.com/)

No cold starts or region complexity  SASE and Zero Trust without the complexity  Deploy to 330+ cities instantly  Defend against the Internet's biggest DDoS attacks  Predictable pricing without surprises  Identity-aware Zero Trust access that retires your VPN  Battle-tested infrastructure powering millions  CDN, WAF, and DNS faster than the public Internet  No cold starts or region complexity  SASE and Zero Trust without the complexity  Deploy to 330+ cities instantly  Defend against the Internet's biggest DDoS attacks  Predictable pricing without surprises  Identity-aware Zero Trust access that retires your VPN  Battle-tested infrastructure powering millions  CDN, WAF, and DNS faster than the public Internet 
