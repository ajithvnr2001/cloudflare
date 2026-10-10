---
url: https://developers.cloudflare.com/changelog/post/2026-06-30-gateway-granular-permissions/
title: New permissions and roles for Gateway policies and lists \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:35.835059+00:00
---

# New permissions and roles for Gateway policies and lists · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-30-gateway-granular-permissions/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 30, 2026

## New permissions and roles for Gateway policies and lists

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now assign granular, resource-scoped roles for [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) firewall policies and [Zero Trust lists](https://developers.cloudflare.com/cloudflare-one/reusable-components/lists/). Administrators can delegate access to specific policy types or list management without granting account-wide or product-wide control.

#### What is new

When you [add a member](https://developers.cloudflare.com/fundamentals/manage-members/manage/) or create a [permission policy](https://developers.cloudflare.com/fundamentals/manage-members/policies/), the following resource-scoped roles are now available:

Role | Description  
---|---  
Zero Trust Gateway Firewall Policies Admin | Can view and edit all Gateway firewall policies, including DNS, HTTP, and Network policies.  
Zero Trust Gateway DNS Policies Admin | Can view and edit Gateway DNS policies.  
Zero Trust Gateway HTTP Policies Admin | Can view and edit Gateway HTTP policies.  
Zero Trust Gateway Network Policies Admin | Can view and edit Gateway Network policies.  
Zero Trust Gateway Egress Policies Admin | Can view and edit Gateway Egress policies.  
Zero Trust Gateway Resolver Policies Admin | Can view and edit Gateway Resolver policies.  
Zero Trust Gateway Policies Admin | Can view and edit all Gateway policies.  
Zero Trust Gateway Policies Read | Can view all Gateway policies.  
Zero Trust Gateway Read Only | Can view all Gateway resources.  
Zero Trust DNS Locations Admin | Can view and edit DNS locations.  
Zero Trust Proxy Endpoints Admin | Can view and edit Gateway Proxy Endpoints.  
Zero Trust Account Lists Admin | Can view and edit all Gateway and Access lists.  
Zero Trust Account Lists Read | Can view all Gateway and Access lists.  
  
These roles allow you to:

  * Grant a network engineer write access to Network policies only, without exposing DNS or HTTP policy configuration.
  * Allow a security analyst to view all Gateway policies in read-only mode for auditing purposes.
  * Delegate list management to a team that maintains block and allow lists without giving them access to policy configuration.



You can also now assign _Resource-scoped roles_. These roles are complementary to existing account-level roles, and allow you to grant access to a specific resource, like an individual Gateway policy or Cloudflare One list. **Existing account-level roles continue to work.** A member with the `Cloudflare Gateway` or `Cloudflare Zero Trust` role retains full access to all Gateway resources. This ensures backward compatibility for existing automation and API tokens.

#### Get started

  * Refer to [Granular permissions for Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/granular-permissions/) for setup instructions and supported resources.
  * Learn how to [create permission policies](https://developers.cloudflare.com/fundamentals/manage-members/policies/) that use these roles.


