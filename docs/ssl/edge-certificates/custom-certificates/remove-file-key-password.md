---
url: https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/remove-file-key-password/
title: Remove key file password \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:40.407836+00:00
---

# Remove key file password · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/remove-file-key-password/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /…

[Edge certificates](https://developers.cloudflare.com/ssl/edge-certificates/)

  4. /[Custom certificates](https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/)
  5. /Remove key file password



# Remove key file password

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/remove-file-key-password/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You cannot upload a custom certificate with a password-protected key file.

The process for removing the password depends on your operating system. The following examples remove the password from `example.com.key`.

Linux

  1. Open a command console.

  2. Go to the directory containing the `example.com.key` file.

  3. Copy the original key.
         
         cp example.com.key temp.key

  4. Run the following command (if using an ECDSA certificate, replace `rsa` with `ec`).
         
         openssl rsa -in temp.key -out example.com.key

  5. When prompted in the console window, enter the original key password.

  6. [Upload the file contents](https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/uploading/#upload-a-custom-certificate) to Cloudflare.




Windows

  1. Go to <https://indy.fulgan.com/SSL/>[ ↗︎](https://indy.fulgan.com/SSL/) and download the latest version of OpenSSL for your x86 or x86_64 operating system.

  2. Open the `.zip` file and extract it.

  3. Select **openssl.exe**.

  4. In the command window that appears, run:
         
         rsa -in C:\Path\To\example.com.key -out key.pem

  5. Enter the original key password when prompted by the **openssl.exe** command window.

  6. [Upload](https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/uploading/#upload-a-custom-certificate) the contents of the `key.pem` file to Cloudflare.




[PreviousBundle methodologies](https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/bundling-methodologies/)[NextTroubleshooting](https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/troubleshooting/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/edge-certificates/custom-certificates/remove-file-key-password.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
