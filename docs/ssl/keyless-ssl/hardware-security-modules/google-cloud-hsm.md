---
url: https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/google-cloud-hsm/
title: Google Cloud HSM \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:42.362026+00:00
---

# Google Cloud HSM · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/google-cloud-hsm/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /…

[Keyless SSL](https://developers.cloudflare.com/ssl/keyless-ssl/)

  4. /[Hardware security modules](https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/)
  5. /Google Cloud HSM



# Google Cloud HSM

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/google-cloud-hsm/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBefore you start1\. Create a key ring2\. Create a key3\. Import the private key4\. Modify your gokeyless config file and restart the service

This tutorial uses [Google Cloud HSM ↗︎](https://cloud.google.com/kms/docs/hsm) — a FIPS 140-2 Level 3 certified implementation.

* * *

## Before you start

Make sure that you have:

  * Set up your [Google Cloud project ↗︎](https://cloud.google.com/kms/docs/quickstart#before-you-begin)



* * *

## 1\. Create a key ring

To set up the Google Cloud HSM, [create a key ring ↗︎](https://cloud.google.com/kms/docs/hsm#kms-create-key-hsm-web) and indicate its location.

Note:

Only [certain locations ↗︎](https://cloud.google.com/kms/docs/locations#hsm-regions) support Google Cloud HSM.

* * *

## 2\. Create a key

Create a key, including the following information:

Field| Value  
---|---  
Key ring| The key ring you created in **Step 2**  
Protection level| HSM  
Purpose| Asymmetric Encrypt  
  
* * *

## 3\. Import the private key

After creating a key ring and key, [import the private key ↗︎](https://cloud.google.com/kms/docs/importing-a-key).

Note:

You need to [convert your key ↗︎](https://cloud.google.com/kms/docs/formatting-keys-for-import#formatting_asymmetric_keys) from a PEM to DER format.

* * *

## 4\. Modify your gokeyless config file and restart the service

Once you’ve imported the key, copy the **Resource name** from the UI. Then, add this value to the `gokeyless` YAML file under `private_key_stores`.

With the config file saved, restart `gokeyless` and verify it started successfully.
    
    
    sudo systemctl restart gokeyless.service
    sudo systemctl status gokeyless.service -l

[PreviousFortanix DSM](https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/fortanix-dsm/)[NextIBM Cloud HSM](https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/ibm-cloud-hsm/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/keyless-ssl/hardware-security-modules/google-cloud-hsm.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
