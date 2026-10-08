---
url: https://developers.cloudflare.com/rules/transform/examples/rewrite-archive-urls-new-format/
title: Rewrite blog archive URLs \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:56.074434+00:00
---

# Rewrite blog archive URLs · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/transform/examples/rewrite-archive-urls-new-format/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Transform Rules](https://developers.cloudflare.com/rules/transform/)

  4. /[Examples](https://developers.cloudflare.com/rules/transform/examples/)
  5. /Rewrite blog archive URLs



# Rewrite blog archive URLs

Create a transform rule to rewrite the URL format `/posts/<YYYY>-<MM>-<DD>-<TITLE>` to the new format `/posts/<YYYY>/<MM>/<DD>/<TITLE>`.

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/transform/examples/rewrite-archive-urls-new-format/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

To rewrite the URLs of a blog archive that follow the URL format `/posts/<YYYY>-<MM>-<DD>-<TITLE>` to the new format `/posts/<YYYY>/<MM>/<DD>/<TITLE>`, create the following URL rewrite rule:

Text in **Expression Editor** :
    
    
    http.request.uri.path ~ "^/posts/[0-9]+-[0-9]+-[0-9]+-.*"

Text after **Path** > **Rewrite to** > _Dynamic_ :
    
    
    regex_replace(http.request.uri.path, "^/posts/([0-9]+)-([0-9]+)-([0-9]+)-(.*)$", "/posts/${1}/${2}/${3}/${4}")

The function `regex_replace()` also allows you to extract parts of the URL using regular expressions' capture groups. Create capture groups by putting part of the regular expression in parentheses. Then, reference a capture group using `${<NUMBER>}` in the replacement string, where `<NUMBER>` is the number of the capture group.

[PreviousRemove a response header](https://developers.cloudflare.com/rules/transform/examples/remove-response-header/)[NextRewrite image paths with several URL segments](https://developers.cloudflare.com/rules/transform/examples/rewrite-several-url-different-url/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/transform/examples/rewrite-archive-urls-new-format.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
