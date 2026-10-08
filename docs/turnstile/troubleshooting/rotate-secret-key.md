---
url: https://developers.cloudflare.com/turnstile/troubleshooting/rotate-secret-key/
title: Rotate secret key \u00b7 Cloudflare Turnstile docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:08.768636+00:00
---

# Rotate secret key · Cloudflare Turnstile docs

> Source: https://developers.cloudflare.com/turnstile/troubleshooting/rotate-secret-key/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Turnstile](https://developers.cloudflare.com/turnstile/)
  3. /Troubleshooting
  4. /Rotate secret key



# Rotate secret key

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/turnstile/troubleshooting/rotate-secret-key/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can rotate the secret key using the following steps:

  1. In the Cloudflare dashboard, go to the **Turnstile** page.

[ Go to **Turnstile** ↗ ](https://dash.cloudflare.com/?to=/:account/turnstile)
  2. [Create a new Turnstile widget](https://developers.cloudflare.com/turnstile/get-started/).

  3. In the widget overview, select **Settings** > **Rotate Secret Key**.

  4. Configure your website to use the new secret key.




The rotation occurs over the course of two hours. During this time, both the old secret key and the new secret key are valid. This allows you to swap the secret key while avoiding any issues with your website.

[PreviousTesting](https://developers.cloudflare.com/turnstile/troubleshooting/testing/)[NextOverview](https://developers.cloudflare.com/turnstile/troubleshooting/client-side-errors/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/turnstile/troubleshooting/rotate-secret-key.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
