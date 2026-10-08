---
url: https://developers.cloudflare.com/changelog/post/2025-10-30-member-management-improvements/
title: Revamped Member Management UI \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:27.608564+00:00
---

# Revamped Member Management UI · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-10-30-member-management-improvements/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 30, 2025

## Revamped Member Management UI

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-30-member-management-improvements/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

As Cloudflare's platform has grown, so has the need for precise, role-based access control. We’ve redesigned the Member Management experience in the Dashboard to help administrators more easily discover, assign, and refine permissions for specific principals.

#### What's New

**Refreshed member invite flow**

We overhauled the Invite Members UI to simplify inviting users and assigning permissions.

![Updated Invite Flow UX](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=800,height=435,format=webp/_astro/2025-10-30-invite-experience.B7F3VQ_y.gif)

**Refreshed Members Overview Page**

We've updated the Members Overview Page to clearly display:

  * Member 2FA status
  * Which members hold Super Admin privileges
  * API access settings per member
  * Member onboarding state (accepted vs pending invite)

![Updated Member Management Overview](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3016,height=1424,format=webp/_astro/2025-10-30-member-management-screen.BLc2lx98.png)

**New Member Permission Policies Details View**

We've created a new member details screen that shows all permission policies associated with a member; including policies inherited from group associations to make it easier for members to understand the effective permissions they have.

![Updated Permission Policies Details Screen](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=800,height=435,format=webp/_astro/2025-10-30-permission-policies-screen.pMj53si2.gif)

**Improved Member Permission Workflow**

We redesigned the permission management experience to make it faster and easier for administrators to review roles and grant access.

![Updated Member Permission Management UX](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=800,height=435,format=webp/_astro/2025-10-30-permission-policies-screen.pMj53si2.gif)

**Account-scoped Policies Restrictions Relaxed**

Previously, customers could only associate a single account-scoped policy with a member. We've relaxed this restriction, and now Administrators can now assign multiple account-scoped policies to the same member; bringing policy assignment behavior in-line with user-groups and providing greater flexibility in managing member permissions.
