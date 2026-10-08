---
url: https://developers.cloudflare.com/security-center/intel-apis/manage-miscategorization-reports/
title: Manage miscategorization reports \u00b7 Cloudflare Security Center docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:30.123577+00:00
---

# Manage miscategorization reports · Cloudflare Security Center docs

> Source: https://developers.cloudflare.com/security-center/intel-apis/manage-miscategorization-reports/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Security Center](https://developers.cloudflare.com/security-center/)
  3. /[Threat Intelligence APIs](https://developers.cloudflare.com/security-center/intel-apis/)
  4. /Manage miscategorization reports



# Manage miscategorization reports

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/security-center/intel-apis/manage-miscategorization-reports/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This guide will show you how to manage miscategorization of reports. To complete this guide, you will need to generate an [API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/).

  1. Create an [API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) if you do not have one already.
  2. Choose **Custom Token**.
  3. Name the token, and grant permissions.
  4. Send a `POST` request to the miscategorization [API endpoint ↗︎](https://developers.cloudflare.com/api/resources/intel/subresources/miscategorizations/methods/create/). You can find an example below:

Example of a POST request to miscategorization APIjson
    
    
    export URL="https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/intel/miscategorization"
    curl -X POST "$URL" \
         -H "Authorization: Bearer $TOKEN" \
         -H "Content-Type:application/json" \
    --data '{
      "content_adds": [
      ],
      "content_removes": [
      ],
      "indicator_type": "domain",
      "ip": null,
      "security_adds": [
        115
      ],
      "security_removes": [
      ],
      "url": "cloudflare.com"
    }'

You should receive a response with the value `"success": true`:
    
    
    {
      "result": "",
      "success": true,
      "errors": [],
      "messages": []
    }

Once you send the request, the Cloudflare Support team will receive it and will be able to take action.

[PreviousOverview](https://developers.cloudflare.com/security-center/intel-apis/)[NextLimits](https://developers.cloudflare.com/security-center/intel-apis/limits/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/security-center/intel-apis/manage-miscategorization-reports.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
