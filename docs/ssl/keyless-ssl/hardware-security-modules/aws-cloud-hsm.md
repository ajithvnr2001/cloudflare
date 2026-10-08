---
url: https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/aws-cloud-hsm/
title: AWS cloud HSM \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:42.040456+00:00
---

# AWS cloud HSM · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/aws-cloud-hsm/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /…

[Keyless SSL](https://developers.cloudflare.com/ssl/keyless-ssl/)

  4. /[Hardware security modules](https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/)
  5. /AWS cloud HSM



# AWS cloud HSM

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/aws-cloud-hsm/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBefore you start1\. Import the public and private key to the HSM2\. Modify the gokeyless config file and restart the service

Note

This example imports an existing key pair, but you may prefer to [generate your key on the HSM ↗︎](https://docs.aws.amazon.com/cloudhsm/latest/userguide/manage-keys.html).

* * *

## Before you start

Make sure you have:

  * Provisioned an [AWS CloudHSM cluster ↗︎](https://docs.aws.amazon.com/cloudhsm/latest/userguide/getting-started.html) .
  * Installed the [appropriate software library for PKCS#11 ↗︎](https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-library-install.html).



* * *

## 1\. Import the public and private key to the HSM

Before importing the public key, extract it from the certificate provided by your CA. Place the contents of your private key in `privkey.pem` and then run the following (replacing certificate.pem with your actual certificate) to populate `pubkey.pm`.
    
    
    keyserver$ openssl x509 -pubkey -noout -in certificate.pem > pubkey.pem

Log in to the CloudHSM using a previously created [crypto user ↗︎](https://docs.aws.amazon.com/cloudhsm/latest/userguide/hsm-users.html#crypto-user) (CU) account and generate a key encryption key that will be used to import your private key.
    
    
    keyserver$ /opt/cloudhsm/bin/key_mgmt_util
    Command: loginHSM -u CU -s patrick -p donahue
    Command: genSymKey -t 31 -s 16 -sess -l import-wrapping-key
    ...
    Symmetric Key Created.  Key Handle: 658
    ...

Referencing the key handle returned above, import the private and public key and then log out of the HSM:
    
    
    Command: importPrivateKey -f privkey.pem -l mykey -id 1 -w 658
    ...
    Cfm3WrapHostKey returned: 0x00 : HSM Return: SUCCESS
    Cfm3CreateUnwrapTemplate returned: 0x00 : HSM Return: SUCCESS
    Cfm3UnWrapKey returned: 0x00 : HSM Return: SUCCESS
    ...
    Private Key Unwrapped.  Key Handle: 658
    
    
    Command: importPubKey -f pubkey.pem -l mykey -id 1
    Cfm3CreatePublicKey returned: 0x00 : HSM Return: SUCCESS
    ...
    Public Key Handle: 941
    
    
    Command: logoutHSM
    Command: exit

* * *

## 2\. Modify the gokeyless config file and restart the service

Now that the keys are in place, we need to modify the configuration file that the key server will read on startup. Change the `object=mykey` and `pin-value=username:password` values to match the key label you provided and CU user you created.

Open `/etc/keyless/gokeyless.yaml` and immediately after:
    
    
    private_key_stores:
      - dir: /etc/keyless/keys

add:
    
    
    - uri: pkcs11:token=cavium;object=mykey?module-path=/opt/cloudhsm/lib/libcloudhsm_pkcs11_standard.so&pin-value=patrick:donahue&max-sessions=1

With the config file saved, restart `gokeyless` and verify it started successfully.
    
    
    sudo systemctl restart gokeyless.service
    sudo systemctl status gokeyless.service -l

[PreviousConfiguration](https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/configuration/)[NextAzure Dedicated HSM](https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/azure-dedicated-hsm/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/keyless-ssl/hardware-security-modules/aws-cloud-hsm.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
