---
url: https://developers.cloudflare.com/waf/managed-rules/payload-logging/command-line/decrypt-payload/
title: Decrypt the payload content in the command line \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:44.134536+00:00
---

# Decrypt the payload content in the command line · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/managed-rules/payload-logging/command-line/decrypt-payload/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Managed rules](https://developers.cloudflare.com/waf/managed-rules/)[Log the payload of matched rules](https://developers.cloudflare.com/waf/managed-rules/payload-logging/)

  4. /[Command-line operations](https://developers.cloudflare.com/waf/managed-rules/payload-logging/command-line/)
  5. /Decrypt the payload content



# Decrypt the payload content

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/managed-rules/payload-logging/command-line/decrypt-payload/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewExample

Use the `matched-data-cli` tool to decrypt a payload in the command line.

  1. [Download ↗︎](https://github.com/cloudflare/matched-data-cli/releases) the `matched-data-cli` tool for your platform from the **Releases** page on GitHub, under **Assets**.

  2. Extract the content of the downloaded `.tar.gz` file to a local folder.

  3. Open a command line window and change to the local folder containing the `matched-data-cli` binary.
         
         cd matched-data-cli

  4. Create two files: one with your private key and another one with the encrypted payload:
         
         printf "<PRIVATE_KEY>" > private_key.txt && chmod 400 private_key.txt
         
         printf "<ENCRYPTED_PAYLOAD>" > encrypted_payload.txt

Replace `<PRIVATE_KEY>` with your private key and `<ENCRYPTED_PAYLOAD>` with the encrypted payload.

Note: The first `printf` command will make your private key visible in your command history.

  5. Run the following command to decrypt the payload:
         
         decrypt -k private_key.txt encrypted_payload.txt




Note

If you are using macOS and you get an error when running the `matched-data-cli` tool, refer to [Troubleshooting macOS errors](https://developers.cloudflare.com/waf/managed-rules/payload-logging/command-line/generate-key-pair/#troubleshooting-macos-errors).

## Example

The following example creates two files — one with the private key and another one with the encrypted payload — and runs the `matched-data-cli` tool to decrypt the payload in the `encrypted_payload.txt` file:
    
    
    ~ cd matched-data-cli
    
    printf "uBS5eBttHrqkdY41kbZPdvYnNz8Vj0TvKIUpjB1y/GA=" > private_key.txt && chmod 400 private_key.txt
    
    printf "AzTY6FHajXYXuDMUte82wrd+1n5CEHPoydYiyd3FMg5IEQAAAAAAAAA0lOhGXBclw8pWU5jbbYuepSIJN5JohTtZekLliJBlVWk=" > encrypted_payload.txt
    
    decrypt -k private_key.txt encrypted_payload.txt
    
    
    test matched data

Encryption formats

The format of the encrypted payload can change over time. The `matched-data-cli` tool returns an error if it cannot decrypt a new encryption format.

To fix this error, [download ↗︎](https://github.com/cloudflare/matched-data-cli/releases) a newer version of the tool from GitHub and try again.

[PreviousGenerate a key pair](https://developers.cloudflare.com/waf/managed-rules/payload-logging/command-line/generate-key-pair/)[NextOverview](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/managed-rules/payload-logging/command-line/decrypt-payload.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
