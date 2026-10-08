---
url: https://developers.cloudflare.com/rules/cloud-connector/examples/serve-static-assets-from-azure/
title: Serve /static-assets from Azure Blob Storage \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:46.268464+00:00
---

# Serve /static-assets from Azure Blob Storage · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/cloud-connector/examples/serve-static-assets-from-azure/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Cloud Connector](https://developers.cloudflare.com/rules/cloud-connector/)

  4. /[Examples](https://developers.cloudflare.com/rules/cloud-connector/examples/)
  5. /Serve /static-assets from Azure Blob Storage



# Serve /static-assets from Azure Blob Storage

Route requests with a URI path starting with `/static-assets` to an Azure Blob Storage container using Cloud Connector.

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/cloud-connector/examples/serve-static-assets-from-azure/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

To serve static assets from an Azure Blob Storage container:

  1. In the Cloudflare dashboard, go to the **Cloud Connector** page.

[ Go to **Cloud Connector** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/rules/cloud-connector)
  2. Select **Microsoft Azure** as your [cloud provider](https://developers.cloudflare.com/rules/cloud-connector/providers/).

  3. Enter the bucket URL. Use the following URL structure:

     * **Subdomain-style URL** : Set the hostname to `<BUCKET_NAME>.blob.core.windows.net`. In this case, your bucket should include a folder named `static-assets`, and files should be placed inside this folder. For example, `https://<YOUR_HOSTNAME>/static-assets/style.css` will map to `https://<BUCKET_NAME>.blob.core.windows.net/static-assets/style.css`.
  4. (Optional) Use [URL Rewrite Rules](https://developers.cloudflare.com/rules/transform/url-rewrite/) to adjust the URL structure. For example, you can [create a URL rewrite](https://developers.cloudflare.com/rules/transform/url-rewrite/create-dashboard/) that changes `/static-assets` to `/my-pages-project/static-assets` to match the file structure of your object storage bucket.

  5. (Optional) Use [Cache Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/) to adjust the caching behavior for objects returned from the bucket. For example, you can [create a cache rule](https://developers.cloudflare.com/cache/how-to/cache-rules/create-dashboard/) that caches every returned object matching the `/static-assets` URI path for seven days (defined through the **Edge TTL** setting).

  6. Click **Next** and enter a descriptive name like `Serve static assets from Azure` in **Cloud Connector name**.

  7. Under **If** , select **Custom filter expression** and enter the following expression: `http.request.full_uri wildcard "http*://<YOUR_HOSTNAME>/static-assets/*"`  


  8. Select **Deploy** to activate the rule.




This setup ensures that all traffic matching `http*://<YOUR_HOSTNAME>/static-assets/*` (HTTPS and HTTP requests) is served from your Azure Blob Storage container. Make sure to replace `<YOUR_HOSTNAME>` with your actual hostname and adjust the example paths according to your setup.

[PreviousSend EU visitors to a Google Cloud Storage bucket](https://developers.cloudflare.com/rules/cloud-connector/examples/send-eu-visitors-to-gcs/)[NextOverview](https://developers.cloudflare.com/rules/custom-errors/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/cloud-connector/examples/serve-static-assets-from-azure.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
