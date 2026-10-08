---
url: https://developers.cloudflare.com/ssl/keyless-ssl/troubleshooting/
title: Troubleshooting Keyless SSL \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:43.040926+00:00
---

# Troubleshooting Keyless SSL · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/keyless-ssl/troubleshooting/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /[Keyless SSL](https://developers.cloudflare.com/ssl/keyless-ssl/)
  4. /Troubleshooting



# Troubleshooting

Last updated Aug 18, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/keyless-ssl/troubleshooting/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCheck the logsEnable debug loggingBrowsers are seeing a TLS connection failure after trying to connectClients are connecting, but immediately abortingThe gokeyless binary cannot load the CA fileKeyless is affecting to unanticipated hostsKey servers on WindowsKey server multi-domain supportAdditional questions

## Check the logs

To check logs, use a command similar to the following.

  * systemd: `sudo journalctl -f -u gokeyless`
  * upstart/sysvinit: `sudo tail -f /var/log/gokeyless.log`



## Enable debug logging

To enable debug logging, use a command similar to the following.
    
    
    cd /etc/keyless
    sudo -u keyless gokeyless --loglevel 0

When running in a container, `gokeyless` is the container's main process (PID 1), so the host/systemd command above does not apply. Instead, set the log level when you start the container and read logs from the container runtime:
    
    
    # Set verbosity via environment variable
    docker run ... -e KEYLESS_LOGLEVEL=0 ghcr.io/cloudflare/gokeyless:latest
    
    # Read logs
    docker logs -f <CONTAINER>   # or: kubectl logs -f <POD>

## Browsers are seeing a TLS connection failure after trying to connect

  1. Make sure your key server is accessible from outside your network (tcp/2407).
  2. Provide a packet capture: `sudo tcpdump -nni <interface> -s 0 -w keyless-$(date +%s).pcap port 2407`



## Clients are connecting, but immediately aborting

If you run `gokeyless` with debug logging enabled, and you see logs like this:
    
    
    [DEBUG] connection 162.158.57.220:37490: reading half closed by client
    [DEBUG] connection 162.158.57.220:37490: server closing connection
    [DEBUG] connection 162.158.57.220:37490 removed
    [DEBUG] spawning new connection: 162.158.57.220:37862
    [DEBUG] connection 162.158.57.220:37862: reading half closed by client
    [DEBUG] connection 162.158.57.220:37862: server closing connection
    [DEBUG] connection 162.158.57.220:37862 removed

These logs likely indicate that the key server is not using an appropriate server or .`PEM` file and the client is aborting the connection after the certificate exchange. The certificate must be signed by the keyless CA and the SANs must include the hostname of the keyless server. Here is a valid example for a keyless server located at `11aa40b4a5db06d4889e48e2f.example.com` (note the Subject Alternative Name and Authority Key Identifier):
    
    
    openssl x509 -in server.pem -noout -text -certopt no_subject,no_header,no_version,no_serial,no_signame,no_validity,no_subject,no_issuer,no_pubkey,no_sigdump,no_aux | sed -e 's/^        //'
    
    
    X509v3 extensions:
        X509v3 Key Usage: critical
            Digital Signature, Key Encipherment
        X509v3 Extended Key Usage:
            TLS Web Server Authentication
        X509v3 Basic Constraints: critical
            CA:FALSE
        X509v3 Subject Key Identifier:
            DD:24:97:F1:A9:F1:4C:73:D9:1B:44:EC:A1:C3:10:E9:F0:41:98:BB
        X509v3 Authority Key Identifier:
            keyid:29:CE:8F:F1:9D:4C:BA:DE:55:78:D7:A6:29:E9:C5:FD:1D:9D:21:48
    
        X509v3 Subject Alternative Name:
            DNS:11aa40b4a5db06d4889e48e2f.example.com
        X509v3 CRL Distribution Points:
    
            Full Name:
              URI:http://ca.cfdata.org/api/v1/crl/key_server

## The gokeyless binary cannot load the CA file

Ensure permissions are correct on all keys and certificates installed on the server.

## Keyless is affecting to unanticipated hosts

You will need to either provide a certificate for only those hosts or change the priority of the certificate in the **SSL/TLS** app of your Cloudflare dashboard.

## Key servers on Windows

Cloudflare currently only provide packages for the supported GNU/Linux distributions as per the [Cloudflare package repository ↗︎](https://pkg.cloudflare.com/).

However, the key server is open source so you may attempt to build and deploy a binary, but running on Windows is not a supported configuration so you may experience problems that Cloudflare will not be able to help with.

## Key server multi-domain support

A single key server can serve multiple domains. Add each certificate's private key to the `private_key_stores` block in `gokeyless.yaml`, or pass them with `--private-key-dirs` / `--private-key-files`. Refer to [Serve multiple private keys](https://developers.cloudflare.com/ssl/keyless-ssl/configuration/run-with-docker/#serve-multiple-private-keys) for details.

The `hostname` and `zone_id` fields are single string values used only during enrollment. You do not need to update them for additional domains.

## Additional questions

Contact your account team or [Cloudflare Support](https://developers.cloudflare.com/support/contacting-cloudflare-support/).

[PreviousGlossary](https://developers.cloudflare.com/ssl/keyless-ssl/glossary/)[NextAbout PQC](https://developers.cloudflare.com/ssl/post-quantum-cryptography/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/keyless-ssl/troubleshooting.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
