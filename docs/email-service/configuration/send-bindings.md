---
url: https://developers.cloudflare.com/email-service/configuration/send-bindings/
title: Configure send bindings \u00b7 Cloudflare Email Service docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:12.904026+00:00
---

# Configure send bindings · Cloudflare Email Service docs

> Source: https://developers.cloudflare.com/email-service/configuration/send-bindings/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Email Service](https://developers.cloudflare.com/email-service/)
  3. /Configuration
  4. /Configure send bindings



# Configure send bindings

Last updated Jun 9, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/email-service/configuration/send-bindings/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBinding typesNext steps

When you add a `send_email` binding to a Worker, you can restrict which addresses it may send from and to. Configure these restrictions in your Wrangler configuration file. For the binding API itself, refer to the [Workers API](https://developers.cloudflare.com/email-service/api/send-emails/workers-api/).

## Binding types

Each entry in `send_email` can be configured to restrict what the binding can do. The sender address must always belong to a domain you have onboarded to Email Service.

  * **No restriction attribute** : The binding can send to any verified destination address in your account.
  * **`destination_address`** : The binding can only send to the single destination address configured here. If you call `send()` with `to` set to `null` or `undefined`, the configured address is used.
  * **`allowed_destination_addresses`** : The binding can only send to addresses listed in this allowlist.
  * **`allowed_sender_addresses`** : The binding can only send from the addresses listed in this allowlist.


    
    
    {
    	"send_email": [
    		// Send to any verified destination
    		{ "name": "EMAIL" },
    		// Send only to a single fixed destination
    		{
    			"name": "NOTIFY_OPS",
    			"destination_address": "ops@yourdomain.com",
    		},
    		// Send only to addresses on an allowlist
    		{
    			"name": "EMAIL_TEAM",
    			"allowed_destination_addresses": [
    				"alice@yourdomain.com",
    				"bob@yourdomain.com",
    			],
    		},
    		// Send only from addresses on an allowlist
    		{
    			"name": "RESTRICTED_EMAIL",
    			"allowed_sender_addresses": [
    				"noreply@yourdomain.com",
    				"support@yourdomain.com",
    			],
    		},
    	],
    }
    
    
    [[send_email]]
    name = "EMAIL"
    
    [[send_email]]
    name = "NOTIFY_OPS"
    destination_address = "ops@yourdomain.com"
    
    [[send_email]]
    name = "EMAIL_TEAM"
    allowed_destination_addresses = [ "alice@yourdomain.com", "bob@yourdomain.com" ]
    
    [[send_email]]
    name = "RESTRICTED_EMAIL"
    allowed_sender_addresses = [ "noreply@yourdomain.com", "support@yourdomain.com" ]

## Next steps

  * [Workers API](https://developers.cloudflare.com/email-service/api/send-emails/workers-api/) — send emails from a Worker using the binding.
  * [Domain configuration](https://developers.cloudflare.com/email-service/configuration/domains/) — onboard the domains you send from.



[PreviousConfigure MTA-STS](https://developers.cloudflare.com/email-service/configuration/mta-sts/)[NextManage suppressions](https://developers.cloudflare.com/email-service/configuration/suppressions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/email-service/configuration/send-bindings.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
