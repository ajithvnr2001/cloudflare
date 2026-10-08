---
url: https://developers.cloudflare.com/turnstile/migration/hcaptcha/
title: Migrate from hCaptcha \u00b7 Cloudflare Turnstile docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:07.885393+00:00
---

# Migrate from hCaptcha · Cloudflare Turnstile docs

> Source: https://developers.cloudflare.com/turnstile/migration/hcaptcha/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Turnstile](https://developers.cloudflare.com/turnstile/)
  3. /[Migration](https://developers.cloudflare.com/turnstile/migration/)
  4. /Migrate from hCaptcha



# Migrate from hCaptcha

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/turnstile/migration/hcaptcha/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewClient-side integrationServer-side integration

If you are using hCaptcha today, you can switch seamlessly to Cloudflare Turnstile by following the step-by-step guide below to assist with the upgrade process.

To complete the migration, you must obtain the [sitekey and secret key](https://developers.cloudflare.com/turnstile/get-started/widget-management/).

## Client-side integration

  1. Update the client-side integration by inserting the Turnstile script snippet in your HTML's `<head>` element:

Turnstile script snippethtml
         
         <script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer></script>

  2. Locate the `hcaptcha.render()` calls and replace the sitekey with your Turnstile sitekey and the API.

Renderjs
         
         // before
           hcaptcha.render(element, {
               sitekey: "00000000-0000-0000-0000-000000000000"
           })
           // after
           turnstile.render(element, {
               sitekey: "1x00000000000000000000AA"
           })




Note

Turnstile supports:

  * the `render()` call
  * hCaptcha invisible mode with the `execute()` call



## Server-side integration

  1. Update the server-side integration by replacing the Siteverify URL.

Replace: `https://hcaptcha.com/siteverify` with the following:
         
         https://challenges.cloudflare.com/turnstile/v0/siteverify

  2. Replace the `h-captcha-response` input name with the following:
         
         cf-turnstile-response




[PreviousMigrate from reCAPTCHA](https://developers.cloudflare.com/turnstile/migration/recaptcha/)[NextTutorials](https://developers.cloudflare.com/turnstile/tutorials/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/turnstile/migration/hcaptcha.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
