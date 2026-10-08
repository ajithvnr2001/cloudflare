---
url: https://developers.cloudflare.com/learning-paths/dns-best-practices/concepts/phase-3/
title: Phase 3: Execution (Migration window) \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:47.904097+00:00
---

# Phase 3: Execution (Migration window) · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/dns-best-practices/concepts/phase-3/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Dns Best Practices

  4. /[Concepts](https://developers.cloudflare.com/learning-paths/dns-best-practices/concepts/)
  5. /Phase 3: Execution (Migration window)



# Phase 3: Execution (Migration window)

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/dns-best-practices/concepts/phase-3/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview1\. Final verification2\. Update nameservers at your registrar3\. Monitor propagation4\. Initial testing

Phase 3 is when you make the actual switch to Cloudflare.

## 1\. Final verification

Complete one last check of all DNS records in your Cloudflare dashboard for accuracy and ensure your BIND servers are still operational as a fallback if needed.

## 2\. Update nameservers at your registrar

  1. Log in to your domain registrar's control panel for each domain.
  2. Navigate to the section for managing nameservers.
  3. Replace your current on-prem BIND nameserver entries with your Cloudflare nameservers.
  4. Add the Cloudflare nameservers assigned to your domain (Cloudflare will provide at least two).
  5. Save the changes.



## 3\. Monitor propagation

  * DNS nameserver changes can take time to propagate globally, typically anywhere from a few minutes to 48 hours (though often much faster due to lowered TTLs).

  * Use the commands exemplified below, replacing `yourdomain.com` by your actual domain.

    * `dig yourdomain.com NS @8.8.8.8` (query Google's DNS)
    * `dig yourdomain.com NS @1.1.1.1` (query Cloudflare's DNS)
    * `whois yourdomain.com`
    * `dig yourdomain.com @tld.nameserver.com` (`tld.nameserver.com` is the nameserver of your domain's TLD. You can find this information by querying it as `dig com ns +short` where `.com` is the example.)

You are looking for the Cloudflare nameservers to be reported consistently.




## 4\. Initial testing

Once propagation appears to be widespread, perform basic resolution tests for critical records (for example, your website's `A` record and any `MX` records, if you had them set up).

  * `dig yourdomain.com A +short`
  * `dig yourdomain.com MX +short`



[PreviousPhase 2: Preparation](https://developers.cloudflare.com/learning-paths/dns-best-practices/concepts/phase-2/)[NextPhase 4: Post-migration and DNSSEC Re-activation](https://developers.cloudflare.com/learning-paths/dns-best-practices/concepts/phase-4/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/dns-best-practices/concepts/phase-3.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
