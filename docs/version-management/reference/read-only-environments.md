---
url: https://developers.cloudflare.com/version-management/reference/read-only-environments/
title: Read-only environments \u00b7 Cloudflare Version Management docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:15.021928+00:00
---

# Read-only environments · Cloudflare Version Management docs

> Source: https://developers.cloudflare.com/version-management/reference/read-only-environments/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Version Management](https://developers.cloudflare.com/version-management/)
  3. /Reference
  4. /Read-only environments



# Read-only environments

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/version-management/reference/read-only-environments/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

When an environment is read-only, versions deployed to this environment will permanently become read-only. This configuration protects sensitive environments from accidental changes.

**Version Zero** is an exception to this rule and is always editable.

**Production** is a read-only environment by default. This means that any version associated with **Production** also becomes read-only. This configuration prevents another member of your account from accidentally editing the version associated with your live traffic. You can change this configuration by editing the environment.

  


For similar reasons, some organizations may make **Staging** a read-only environment. Otherwise, another member of your account could make changes to a version in **Staging** _after_ your organization has performed the validation tests prior to promoting to **Production**. Without having a read-only **Staging** environment, this change could be released into **Production** without testing and might cause an issue with live traffic.

To change the read-only status of an environment, [edit the environment](https://developers.cloudflare.com/version-management/how-to/environments/#edit-environment).

[PreviousTraffic filters](https://developers.cloudflare.com/version-management/reference/traffic-filters/)[NextChangelog](https://developers.cloudflare.com/version-management/changelog/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/version-management/reference/read-only-environments.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
