---
url: https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/entrust-nshield-connect/
title: Entrust nShield Connect \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:42.202668+00:00
---

# Entrust nShield Connect · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/entrust-nshield-connect/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /…

[Keyless SSL](https://developers.cloudflare.com/ssl/keyless-ssl/)

  4. /[Hardware security modules](https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/)
  5. /Entrust nShield Connect



# Entrust nShield Connect

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/entrust-nshield-connect/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Note

This example assumes you have already configured the nShield Connect device and generated or imported your private keys.

Since the keys are already in place, we merely need to build the configuration file that the key server will read on startup. In this example the device contains a single RSA key pair.

We ask `pkcs11-tool` (provided by the `opensc` package) to display the objects stored in the token:
    
    
    pkcs11-tool --module /opt/nfast/toolkits/pkcs11/libcknfast.so -O
    
    
    Using slot 0 with a present token (0x1d622495)
    Private Key Object; RSA
      label:      rsa-privkey
      ID:         105013281578de42ea45f5bfac46d302fb006687
      Usage:      decrypt, sign, unwrap
    warning: PKCS11 function C_GetAttributeValue(ALWAYS_AUTHENTICATE) failed: rv = CKR_ATTRIBUTE_TYPE_INVALID (0x12)
    
    Public Key Object; RSA 2048 bits
      label:      rsa-privkey
      ID:         105013281578de42ea45f5bfac46d302fb006687
      Usage:      encrypt, verify, wrap

The key piece of information is the label of the object, `rsa-privkey`. Open up `/etc/keyless/gokeyless.yaml` and immediately after
    
    
    private_key_stores:
      - dir: /etc/keyless/keys

add
    
    
    - uri: pkcs11:token=accelerator;object=rsa-privkey?module-path=/opt/nfast/toolkits/pkcs11/libcknfast.so&max-sessions=4

Save the config file, restart `gokeyless`, and verify it started successfully.
    
    
    sudo systemctl restart gokeyless.service
    sudo systemctl status gokeyless.service -l

[PreviousAzure Managed HSM](https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/azure-managed-hsm/)[NextFortanix DSM](https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/fortanix-dsm/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/keyless-ssl/hardware-security-modules/entrust-nshield-connect.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
