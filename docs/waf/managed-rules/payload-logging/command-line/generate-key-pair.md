---
url: https://developers.cloudflare.com/waf/managed-rules/payload-logging/command-line/generate-key-pair/
title: Generate a key pair in the command line \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:44.191765+00:00
---

# Generate a key pair in the command line · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/managed-rules/payload-logging/command-line/generate-key-pair/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Managed rules](https://developers.cloudflare.com/waf/managed-rules/)[Log the payload of matched rules](https://developers.cloudflare.com/waf/managed-rules/payload-logging/)

  4. /[Command-line operations](https://developers.cloudflare.com/waf/managed-rules/payload-logging/command-line/)
  5. /Generate a key pair



# Generate a key pair

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/managed-rules/payload-logging/command-line/generate-key-pair/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewTroubleshooting macOS errors

Generate a public/private key pair using the Cloudflare [`matched-data-cli` ↗︎](https://github.com/cloudflare/matched-data-cli) command-line tool. After generating a key pair, enter the generated public key in the payload logging configuration.

Do the following:

  1. [Download ↗︎](https://github.com/cloudflare/matched-data-cli/releases) the `matched-data-cli` tool for your platform from the **Releases** page on GitHub, under **Assets**.

  2. Extract the content of the downloaded `.tar.gz` file to a local folder.

  3. Open a terminal and go to the local folder containing the `matched-data-cli` tool.
         
         cd matched-data-cli

  4. Run the following command:
         
         ./matched-data-cli generate-key-pair
         
         {
         	"private_key": "uBS5eBttHrqkdY41kbZPdvYnNz8Vj0TvKIUpjB1y/GA=",
         	"public_key": "Ycig/Zr/pZmklmFUN99nr+taURlYItL91g+NcHGYpB8="
         }




After generating the key pair, copy the public key value and enter it in the payload logging configuration.

## Troubleshooting macOS errors

If you are using macOS, the operating system may block the `matched-data-cli` tool, depending on your security settings.

For instructions on how to execute unsigned binaries like the `matched-data-cli` tool in macOS, refer to the [Safely open apps on your Mac ↗︎](https://support.apple.com/en-us/102445#openanyway) page in Apple Support.

[PreviousOverview](https://developers.cloudflare.com/waf/managed-rules/payload-logging/command-line/)[NextDecrypt the payload content](https://developers.cloudflare.com/waf/managed-rules/payload-logging/command-line/decrypt-payload/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/managed-rules/payload-logging/command-line/generate-key-pair.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
