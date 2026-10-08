---
url: https://developers.cloudflare.com/cloudflare-one/access-controls/policies/require-purpose-justification/
title: Require purpose justification after login \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:23.372381+00:00
---

# Require purpose justification after login · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/access-controls/policies/require-purpose-justification/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Access controls](https://developers.cloudflare.com/cloudflare-one/access-controls/)

  4. /[Policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)
  5. /Require purpose justification



# Require purpose justification

Last updated Apr 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/require-purpose-justification/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Access allows security and IT teams to present users with a purpose justification screen directly after they log in to an Access application. This allows organizations to audit not only for who is accessing their resources, but also for why they are requesting access.

The purpose justification screen will show for any new sessions of an application. For example, if an Access application has a session time of eight hours, a user will see the purpose justification screen once every eight hours.

Configuring a purpose justification screen is done as part of configuring an Access policy.

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Access controls** > **Applications**.
  2. Choose an application and select **Configure**.
  3. Go to **Policies**.
  4. Choose an **Allow** policy and select **Configure**.
  5. Under **Additional settings** , turn on **Purpose justification**.
  6. (Optional) Set a custom purpose justification message. This will appear on the purpose justification screen and will be visible to the user.
  7. Save the policy.



Users who match this policy will see the following screen:

![Finalized purpose justification screen displaying custom message.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1192,height=652,format=webp/_astro/purpose-justification.Bgv25E7i.png)

[PreviousRule groups](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/groups/)[NextExternal Evaluation rules](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/external-evaluation/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/access-controls/policies/require-purpose-justification.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
