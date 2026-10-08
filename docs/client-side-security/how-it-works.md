---
url: https://developers.cloudflare.com/client-side-security/how-it-works/
title: How client-side security works \u00b7 Client-side security docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:57.275349+00:00
---

# How client-side security works · Client-side security docs

> Source: https://developers.cloudflare.com/client-side-security/how-it-works/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Client-side security](https://developers.cloudflare.com/client-side-security/)
  3. /How it works



# How client-side security works

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/client-side-security/how-it-works/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewComparison of CSP headersHeader used for resource monitoringHeaders related to content security rulesLearn more

Cloudflare's client-side security helps manage client-side resources (which include scripts and their connections) loaded by your website visitors, and provides visibility on the [cookies ↗︎](https://www.cloudflare.com/learning/privacy/what-are-cookies/) recently detected in HTTP traffic. Client-side security can trigger alert notifications when resources change or are considered malicious.

Client-side security works by adding [Content Security Policy (CSP)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) HTTP headers to your site's responses. CSP is a browser-native mechanism that controls which resources a page is allowed to load and where to send reports when a resource violates the policy. Cloudflare uses two types of CSP headers for different purposes:

  * For resource monitoring (scripts and connections)
  * To enforce content security rules or log violations of these rules



## Comparison of CSP headers

The following table compares the CSP HTTP headers used for monitoring resources and applying content security rules:

Resource monitoring HTTP header | Content security rules HTTP headers  
---|---  
`content-security-policy-report-only` | `content-security-policy-report-only` (log rules)  
`content-security-policy` (allow rules)  
Automatic — on when monitoring is enabled | Manual — created via rules you define  
Added to a sample of HTML responses | Added to 100% of matching responses (not sampled)  
Reports all detected scripts and connections | CSP directives come from your allowlist  
Browser sends violation reports to Cloudflare | Log rules report violations only  
Allow rules block disallowed resources  
  
## Header used for resource monitoring

When you turn on resource monitoring, Cloudflare automatically adds a `content-security-policy-report-only` HTTP header to a sample of HTML responses. This report-only header does not block anything. It uses CSP directives that cause browsers to generate violation reports for detected scripts and connections. For details on the header format, refer to [CSP HTTP header format](https://developers.cloudflare.com/client-side-security/reference/csp-header/).

Based on these reports, Cloudflare builds a list of all scripts running on your application and the connections they make to third-party endpoints. Cloudflare also monitors ingress and egress HTTP traffic for cookies, whether set by origin servers or by the visitor's browser.

You cannot turn off the monitoring header while resource monitoring is enabled. Because the header is added to a sample of responses, there may be a [small delay](https://developers.cloudflare.com/client-side-security/troubleshooting/#cloudflare-does-not-show-any-client-side-resources-after-activation) between deploying a script or cookie and having its data displayed in the resource monitoring dashboards.

The client-side resource monitoring dashboard shows the list of [active](https://developers.cloudflare.com/client-side-security/reference/script-statuses/#available-statuses) scripts, connections, and cookies. The **All Reported Scripts** and **All Reported Connections** dashboards show the full list of detected scripts and connections in your domain, respectively, including infrequent and inactive ones.

## Headers related to content security rules

When you create [content security rules](https://developers.cloudflare.com/client-side-security/rules/), Cloudflare generates CSP directives based on your allow and log rules:

  * **Log rules** add directives to the `content-security-policy-report-only` HTTP header, reporting violations without blocking resources.
  * **Allow rules** add directives to the `content-security-policy` HTTP header, actively blocking resources not present in your allowlist.



Unlike headers used for resource monitoring, these HTTP headers apply only to responses matching the expression you define in each rule and are not sampled. You have full control over these headers through your [content security rules](https://developers.cloudflare.com/client-side-security/rules/) configuration.

Customers with Client-Side Security Advanced have access to additional classification mechanisms based on threat feeds to determine if a script, or a connection made by a script, is malicious. For more information, refer to [Malicious script and connection detection](https://developers.cloudflare.com/client-side-security/how-it-works/malicious-script-detection/).

* * *

## Learn more

For more background on client-side security and resource monitoring, refer to our [blog post ↗︎](https://blog.cloudflare.com/page-shield-generally-available/).

[PreviousGet started](https://developers.cloudflare.com/client-side-security/get-started/)[NextMalicious script and connection detection](https://developers.cloudflare.com/client-side-security/how-it-works/malicious-script-detection/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/client-side-security/how-it-works/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
