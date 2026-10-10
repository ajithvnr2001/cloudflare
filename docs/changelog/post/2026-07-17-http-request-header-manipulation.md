---
url: https://developers.cloudflare.com/changelog/post/2026-07-17-http-request-header-manipulation/
title: New header control options for Gateway HTTP policies \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:34.573482+00:00
---

# New header control options for Gateway HTTP policies · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-17-http-request-header-manipulation/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 17, 2026

## New header control options for Gateway HTTP policies

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Gateway now supports advanced header control on [Allow policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#allow). Administrators can add, overwrite, or delete headers on matching requests using static values or dynamic variables.

#### Header operations

Gateway HTTP policies using the Allow action support three operations in `rule_settings`:

Operation | API field | Behavior  
---|---|---  
Add | `add_headers` | Appends a value to the header. Existing values are preserved.  
Overwrite | `set_headers` | Replaces the header value. Creates the header if it does not exist.  
Delete | `delete_headers` | Removes the header from the request.  
  
Gateway applies operations in order: delete, then overwrite, then add.

#### Dynamic variables

Header values can include dynamic variables using the `@{...}` syntax. Gateway resolves variables at request time from identity, device, and network context.

Variable | Description  
---|---  
`@{identity.email}` | User email from the identity provider  
`@{identity.name}` | User display name from the identity provider  
`@{identity.id}` | Cloudflare identity UUID  
`@{identity.groups}` | Identity provider group memberships  
`@{identity.SAML}` | SAML attributes (if configured)  
`@{identity.OIDC}` | OIDC claims (if configured)  
`@{source.ip}` | Source IP of the connection  
`@{destination.ip}` | Destination IP of the request  
`@{device.id}` | Cloudflare One Client device UUID  
`@{device.posture}` | Device posture check results (JSON string)  
  
You can mix static text and dynamic variables in a single header value. For example, `user-@{identity.email}` resolves to `user-jdoe@example.com`.

For more information, refer to [Custom headers](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/tenant-control/).
