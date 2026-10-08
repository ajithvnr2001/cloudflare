---
url: https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/
title: Hardware security modules \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:41.854124+00:00
---

# Hardware security modules · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /[Keyless SSL](https://developers.cloudflare.com/ssl/keyless-ssl/)
  4. /Hardware security modules



# Hardware security modules

Last updated Jun 8, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhy use Keyless SSL with an HSM?Communicating using PKCS#11 Initial configuration Compatibility

In addition to private keys stored on disk, Keyless SSL supports keys stored in a Hardware Security Module (HSM) via the PKCS#11 standard. Keyless uses PKCS#11 for signing and decrypting payloads without having direct access to the private keys.

* * *

## Why use Keyless SSL with an HSM?

Hardware Security Modules (HSMs) facilitate a higher level of protection for your private keys over storing them directly on your key server. The primary responsibility of an HSM is safeguarding private keys and performing operations such as signing or encryption internally. In addition to access control, that means the physical device must offer some degree of tamper-resistance in order to be compliant with government or [industry regulations such as FIPS 140 ↗︎](https://csrc.nist.gov/pubs/fips/140-3/final).

Moreover, many HSMs are also capable of generating keys and producing cryptographically secure randomness. Some are purpose-built to perform cryptographic computations more efficiently.

* * *

## Communicating using PKCS#11

The key server communicates with HSMs via PKCS#11, so any HSM supporting the standard can be used with Keyless SSL.

### Initial configuration

For more details on initializing your PKCS#11 token, refer to [Configuration](https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/configuration/).

### Compatibility

Keyless SSL has interoperability with the following modules:

  * [Entrust nShield Connect ↗︎](https://www.entrust.com/digital-security/hsm)
  * [Gemalto SafeNet Luna ↗︎](https://cpl.thalesgroup.com/compliance/fips-common-criteria-validations)
  * [SoftHSMv2 ↗︎](https://github.com/opendnssec/SoftHSMv2)
  * [YubiKey Neo ↗︎](https://www.yubico.com/product/yubikey-neo/)



Also, the following cloud HSM offerings have been tested with Keyless SSL:

  * [AWS CloudHSM](https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/aws-cloud-hsm/)
  * [Azure Dedicated HSM](https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/azure-dedicated-hsm/)
  * [Azure Managed HSM](https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/azure-managed-hsm/)
  * [Fortanix DSM](https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/fortanix-dsm/)
  * [IBM Cloud HSM](https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/ibm-cloud-hsm/)
  * [Google Cloud HSM](https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/google-cloud-hsm/)



[PreviousRun with Docker](https://developers.cloudflare.com/ssl/keyless-ssl/configuration/run-with-docker/)[NextConfiguration](https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/configuration/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/keyless-ssl/hardware-security-modules/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
