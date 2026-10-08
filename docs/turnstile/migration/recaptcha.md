---
url: https://developers.cloudflare.com/turnstile/migration/recaptcha/
title: Migrate from reCAPTCHA \u00b7 Cloudflare Turnstile docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:07.465960+00:00
---

# Migrate from reCAPTCHA · Cloudflare Turnstile docs

> Source: https://developers.cloudflare.com/turnstile/migration/recaptcha/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Turnstile](https://developers.cloudflare.com/turnstile/)
  3. /[Migration](https://developers.cloudflare.com/turnstile/migration/)
  4. /Migrate from reCAPTCHA



# Migrate from reCAPTCHA

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/turnstile/migration/recaptcha/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewClient-side integrationServer-side integration

If you are using reCAPTCHA today, you can switch seamlessly to Cloudflare Turnstile by following the step-by-step guide below to assist with the upgrade process.

To complete the migration, you must obtain the [sitekey and secret key](https://developers.cloudflare.com/turnstile/get-started/widget-management/).

Note

Turnstile migration is currently compatible up to reCAPTCHA v2.

## Client-side integration

  1. Update the client-side integration by inserting the Turnstile script snippet in your HTML's `<head>` element.

Turnstile script snippethtml
         
         <script
         	src="https://challenges.cloudflare.com/turnstile/v0/api.js?compat=recaptcha"
         	async
         	defer
         ></script>

Note

Adding `?compat=recaptcha` runs Turnstile in compatibility mode, which enables the following features:

     * implicit rendering for reCAPTCHA
     * `g-recaptcha-response` input name for forms
     * register the Turnstile API as `grecaptcha`

  2. Locate the `grecaptcha.render()` calls and replace the sitekey with your Turnstile sitekey.

Note

Turnstile supports:

     * the `render()` call
     * reCAPTCHA v2 invisible mode with the `execute()` call




## Server-side integration

Update the server-side integration by replacing the Siteverify URL.

Replace `https://www.google.com/recaptcha/api/siteverify` with the following:
    
    
    https://challenges.cloudflare.com/turnstile/v0/siteverify

Differences to reCAPTCHA's Siteverify

reCAPTCHA supports `GET` requests using query parameters, such as `GET /siteverify?response=<response>&secret=<secret>`.

Turnstile's Siteverify endpoint does _not_ support this and only accepts `POST` requests with a FormData or JSON body.

Refer to [server-side validation](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/) for more information.

[PreviousOverview](https://developers.cloudflare.com/turnstile/migration/)[NextMigrate from hCaptcha](https://developers.cloudflare.com/turnstile/migration/hcaptcha/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/turnstile/migration/recaptcha.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
