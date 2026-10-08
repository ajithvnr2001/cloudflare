---
url: https://developers.cloudflare.com/turnstile/additional-configuration/hostname-management/any-hostname/
title: Any Hostname (Enterprise only) \u00b7 Cloudflare Turnstile docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:06.201830+00:00
---

# Any Hostname (Enterprise only) · Cloudflare Turnstile docs

> Source: https://developers.cloudflare.com/turnstile/additional-configuration/hostname-management/any-hostname/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Turnstile](https://developers.cloudflare.com/turnstile/)
  3. /…

Additional configurations

  4. /[Hostname management](https://developers.cloudflare.com/turnstile/additional-configuration/hostname-management/)
  5. /Any Hostname



# Any Hostname (Enterprise only)

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/turnstile/additional-configuration/hostname-management/any-hostname/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewImplementationUse cases

The Any Hostname feature removes the requirement to specify hostnames during widget creation, allowing widgets to function on any domain.

By default, hostname validation is a security feature that prevents unauthorized use of your widgets. The Any Hostname entitlement removes this restriction, making the hostname field optional during widget creation.

When enabled, widgets can be created without the required hostname specification and used on any domain without pre-configuration. Hostname validation protection is also removed.

## Implementation

To reduce security risks when using Any Hostname, monitor widget usage through [Turnstile Analytics](https://developers.cloudflare.com/turnstile/turnstile-analytics/) to identify unexpected patterns, implement server-side validation with hostname checking in your application code, and use `action` and `cData` parameters to track widget usage sources and identify where widgets are being deployed.

When using the Any Hostname feature, it is essential to implement additional validation in your server-side code to maintain security controls. Always validate the `hostname` field in Siteverify responses.

Example responsejs
    
    
    async function validateTurnstileWithHostname(token, expectedHostnames = []) {
      const response = await fetch('https://challenges.cloudflare.com/turnstile/v0/siteverify', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          secret: process.env.TURNSTILE_SECRET,
          response: token
        })
      });
    
      const result = await response.json();
    
      if (!result.success) {
        return { valid: false, error: 'Token validation failed' };
      }
    
      // Additional hostname validation when using Any Hostname
      if (expectedHostnames.length > 0 && !expectedHostnames.includes(result.hostname)) {
        return { 
          valid: false, 
          error: 'Hostname not in allowed list',
          hostname: result.hostname 
        };
      }
    
      return { valid: true, data: result };
    }

You should regularly review Turnstile Analytics for unexpected usage patterns and monitor the hostname field in Siteverify responses. You can set up alerts for widget usage on unexpected domains.

Use `action` and `cData` parameters to track widget usage sources.
    
    
    <!-- Widget with tracking information -->
    <div class="cf-turnstile" 
         data-sitekey="your-site-key"
         data-action="customer-portal"
         data-cdata="tenant-123"></div>

* * *

## Use cases

The Any Hostname feature is particularly valuable for customers with:

  * Large domain portfolios with many domains to manage individually.
  * Dynamic subdomain creation and frequently create subdomains or customer-specific domains.
  * Multi-tenant applications such as SaaS platforms serving multiple customer domains.
  * Development environments that test across various staging and development domains.



[PreviousPre-clearance configuration](https://developers.cloudflare.com/turnstile/additional-configuration/hostname-management/pre-clearance/)[NextPre-clearance support ↗︎](https://developers.cloudflare.com/cloudflare-challenges/concepts/clearance/#pre-clearance-support-in-turnstile)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/turnstile/additional-configuration/hostname-management/any-hostname.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
