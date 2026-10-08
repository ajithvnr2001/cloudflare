---
url: https://developers.cloudflare.com/email-service/api/send-emails/rest-api/
title: REST API \u00b7 Cloudflare Email Service docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:12.397088+00:00
---

# REST API · Cloudflare Email Service docs

> Source: https://developers.cloudflare.com/email-service/api/send-emails/rest-api/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Email Service](https://developers.cloudflare.com/email-service/)
  3. /…

API reference

  4. /Send emails
  5. /REST API



# REST API

Last updated Jun 9, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/email-service/api/send-emails/rest-api/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAuthenticationSend an emailAttachmentsCustom headersResponseError handlingNext steps

The REST API allows you to send emails from any application using a standard HTTP request to `POST /accounts/{account_id}/email/sending/send`. Use it from any backend, serverless function, or CI/CD pipeline — no Cloudflare Workers binding is required.

For the full OpenAPI specification, refer to the [Email Sending API reference](https://developers.cloudflare.com/api/resources/email_sending/methods/send/).

Cloudflare also provides official SDKs for the REST API: [Node](https://developers.cloudflare.com/api/node/), [Python](https://developers.cloudflare.com/api/python/), and [Go](https://developers.cloudflare.com/api/go/).

## Authentication

Authenticate with a [Cloudflare API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) that has permission to send emails. Include it in the `Authorization` header:
    
    
    Authorization: Bearer <API_TOKEN>

## Send an email
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/{account_id}/email/sending/send" \
      --header "Authorization: Bearer <API_TOKEN>" \
      --header "Content-Type: application/json" \
      --data '{
        "to": "recipient@example.com",
        "from": "welcome@yourdomain.com",
        "subject": "Welcome to our service!",
        "html": "<h1>Welcome!</h1><p>Thanks for signing up.</p>",
        "text": "Welcome! Thanks for signing up."
      }'

For multiple recipients, CC/BCC, and named addresses, see [Specify recipients](https://developers.cloudflare.com/email-service/examples/email-sending/recipients/).

## Attachments

Send files by including base64-encoded content in the `attachments` array. The total message size must not exceed **5 MiB** (including attachments).
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/{account_id}/email/sending/send" \
      --header "Authorization: Bearer <API_TOKEN>" \
      --header "Content-Type: application/json" \
      --data '{
        "to": "customer@example.com",
        "from": "invoices@yourdomain.com",
        "subject": "Your Invoice",
        "html": "<h1>Invoice attached</h1><p>Please find your invoice attached.</p>",
        "attachments": [
          {
            "content": "JVBERi0xLjQKJeLjz9MK...",
            "filename": "invoice-12345.pdf",
            "type": "application/pdf",
            "disposition": "attachment"
          }
        ]
      }'

For inline images and file uploads, see [Email attachments](https://developers.cloudflare.com/email-service/examples/email-sending/email-attachments/).

## Custom headers

Set custom headers for threading, list management, or tracking. Refer to the [email headers reference](https://developers.cloudflare.com/email-service/reference/headers/) for the full list of allowed headers.
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/{account_id}/email/sending/send" \
      --header "Authorization: Bearer <API_TOKEN>" \
      --header "Content-Type: application/json" \
      --data '{
        "to": "user@example.com",
        "from": "notifications@yourdomain.com",
        "subject": "Your weekly digest",
        "html": "<h1>Weekly Digest</h1>",
        "headers": {
          "List-Unsubscribe": "<https://yourdomain.com/unsubscribe?id=abc123>",
          "List-Unsubscribe-Post": "List-Unsubscribe=One-Click",
          "X-Campaign-ID": "weekly-digest-2026-03"
        }
      }'

## Response

A successful response returns the delivery status for each recipient:
    
    
    {
    	"success": true,
    	"errors": [],
    	"messages": [],
    	"result": {
    		"delivered": ["recipient@example.com"],
    		"permanent_bounces": [],
    		"queued": []
    	}
    }

  * `delivered` \- Email addresses to which the message was delivered immediately
  * `permanent_bounces` \- Email addresses that permanently bounced
  * `queued` \- Email addresses for which delivery was queued for later



Workers binding vs REST API responses

The REST API returns recipient-grouped delivery status. The [Workers binding](https://developers.cloudflare.com/email-service/api/send-emails/workers-api/) returns a single `messageId` per `send()` call instead.

## Error handling

The REST API returns standard Cloudflare API error responses. A failed request returns an `errors` array with numeric error codes and machine-readable messages:
    
    
    {
    	"success": false,
    	"errors": [
    		{
    			"code": 10001,
    			"message": "email.sending.error.invalid_request_schema"
    		}
    	],
    	"messages": [],
    	"result": null
    }

REST API error codes:

HTTP Status | Code | Message | Description  
---|---|---|---  
400 | 10001 | `email.sending.error.invalid_request_schema` | Invalid request format  
400 | 10200 | `email.sending.error.email.too_big` | Email exceeds size limit  
400 | 10201 | `email.sending.error.email.no_content_length` | Missing content length  
400 | 10202 | `email.sending.error.email.invalid` | Invalid email content  
401 | 10101 | `email.sending.error.authentication.unauthorized` | Missing or invalid API token  
401 | 10103 | `email.sending.error.authentication.bad_token_type` | Wrong token type for this endpoint  
403 | 10102 | `email.sending.error.authentication.forbidden` | Token lacks permission to send  
403 | 10105 | `email.sending.error.authentication.not_entitled` | Account not entitled to use Email Sending  
403 | 10203 | `email.sending.error.email.sending_disabled` | Sending disabled for this zone or account  
404 | 10000 | `email.sending.error.not_found` | Resource not found  
429 | 10004 | `email.sending.error.throttled` | Rate limit exceeded  
500 | 10002 | `email.sending.error.internal_server` | Internal server error  
500 | 10003 | `email.sending.error.not_implemented` | Operation not implemented  
503 | 10100 | `email.sending.error.authentication.upstream` | Authentication service temporarily unavailable  
  
Workers binding vs REST API errors

The REST API returns standard Cloudflare API numeric error codes, while the [Workers binding](https://developers.cloudflare.com/email-service/api/send-emails/workers-api/) throws errors with string codes (for example, `E_SENDER_NOT_VERIFIED`). Refer to the [Workers API error codes table](https://developers.cloudflare.com/email-service/api/send-emails/workers-api/#error-codes) for the string error codes.

## Next steps

  * Refer to the [Email Sending API reference](https://developers.cloudflare.com/api/resources/email_sending/methods/send/) for the full request and response schemas.
  * See the [Workers API](https://developers.cloudflare.com/email-service/api/send-emails/workers-api/) for sending emails directly from Cloudflare Workers using bindings.
  * See [SMTP](https://developers.cloudflare.com/email-service/api/send-emails/smtp/) for sending from any SMTP-capable application or mail client.
  * Review [email headers](https://developers.cloudflare.com/email-service/reference/headers/) for threading, list management, and custom tracking headers.



[PreviousWorkers API](https://developers.cloudflare.com/email-service/api/send-emails/workers-api/)[NextSMTP](https://developers.cloudflare.com/email-service/api/send-emails/smtp/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/email-service/api/send-emails/rest-api.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
