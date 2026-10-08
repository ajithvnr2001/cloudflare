---
url: https://developers.cloudflare.com/changelog/post/2026-06-08-smtp-submission/
title: Authenticated SMTP submission now available in beta \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:56.761813+00:00
---

# Authenticated SMTP submission now available in beta · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-08-smtp-submission/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 8, 2026

## Authenticated SMTP submission now available in beta

[Email Service](https://developers.cloudflare.com/email-service/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-08-smtp-submission/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now send emails through **Cloudflare Email Service** using authenticated [SMTP submission](https://developers.cloudflare.com/email-service/api/send-emails/smtp/) on `smtp.mx.cloudflare.net:465`. SMTP joins the [REST API](https://developers.cloudflare.com/email-service/api/send-emails/rest-api/) and the [Workers binding](https://developers.cloudflare.com/email-service/api/send-emails/workers-api/) as a third way to send transactional email — useful for existing applications that already speak SMTP and language-native SMTP libraries (Nodemailer, `smtplib`, PHPMailer, JavaMail).

Setting | Value  
---|---  
Host | `smtp.mx.cloudflare.net`  
Port | `465` (implicit TLS)  
AUTH | `PLAIN` or `LOGIN`  
Username | `api_token`  
Password | A Cloudflare API token (account-owned or user-owned) with **Email Sending: Edit**  
  
Submissions enter the same delivery pipeline as the REST API and Workers binding: identical [limits](https://developers.cloudflare.com/email-service/platform/limits/), automatic DKIM and ARC signing, and shared dashboard logs.

Send your first email with a single command:
    
    
    curl --ssl-reqd \
      --url "smtps://smtp.mx.cloudflare.net:465" \
      --user "api_token:<API_TOKEN>" \
      --mail-from "welcome@yourdomain.com" \
      --mail-rcpt "user@example.com" \
      --upload-file mail.txt

Refer to the [SMTP reference](https://developers.cloudflare.com/email-service/api/send-emails/smtp/) for authentication details, response codes, and language-specific examples.
