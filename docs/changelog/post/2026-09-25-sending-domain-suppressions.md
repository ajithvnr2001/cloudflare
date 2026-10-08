---
url: https://developers.cloudflare.com/changelog/post/2026-09-25-sending-domain-suppressions/
title: Suppress recipients for one sending domain \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:16.272342+00:00
---

# Suppress recipients for one sending domain · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-25-sending-domain-suppressions/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 25, 2026

## Suppress recipients for one sending domain

[Email Service](https://developers.cloudflare.com/email-service/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-25-sending-domain-suppressions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Email Sending suppressions](https://developers.cloudflare.com/email-service/concepts/suppressions/) now have a **scope** :

  * **`account`** : The suppression applies to every sending domain and subdomain in your account. This is the default.
  * **`sending_domain`** : The suppression applies to one sending domain only. A suppression for `mail.myappexample.com` does not block mail from `myappexample.com`.



Most importantly, Email Sending now automatically creates bounce and complaint suppressions at the sending-domain level. This provides greater granularity by preventing an issue with one sending domain from suppressing the recipient across your entire account.

To add a suppression for one sending domain in the dashboard, go to **Email Sending** > **Suppressions** and select **Sending domain** in **Scope**. Imports can also set a scope for each row or a default scope.

In the API, pass `scope` when you create the suppression:
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/email/sending/suppressions \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "email": "user@example.net",
        "scope": { "type": "sending_domain", "value": "mail.myappexample.com" }
      }'

The [suppressions API](https://developers.cloudflare.com/api/resources/email_sending/subresources/suppressions/) returns `scope` on every suppression. To list the suppressions for one domain, use `scope_type=sending_domain&scope_value=mail.myappexample.com`. If you omit `scope`, the API creates an `account` suppression, so existing integrations continue to work.

Refer to [Suppression lists](https://developers.cloudflare.com/email-service/concepts/suppressions/#suppression-scope) and [Manage suppressions](https://developers.cloudflare.com/email-service/configuration/suppressions/) for details.
