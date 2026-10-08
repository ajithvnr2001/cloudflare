---
url: https://developers.cloudflare.com/changelog/post/2026-02-26-markdown-responses-for-1xxx-errors/
title: Markdown responses for Cloudflare 1xxx errors \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:38.908424+00:00
---

# Markdown responses for Cloudflare 1xxx errors · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-26-markdown-responses-for-1xxx-errors/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 26, 2026

## Markdown responses for Cloudflare 1xxx errors

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-26-markdown-responses-for-1xxx-errors/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare now returns structured Markdown responses for Cloudflare-generated 1xxx errors when clients send `Accept: text/markdown`.

Each response includes YAML frontmatter plus guidance sections (`What happened` / `What you should do`) so agents can make deterministic retry and escalation decisions without parsing HTML.

In measured 1,015 comparisons, Markdown reduced payload size and token footprint by over 98% versus HTML.

Included frontmatter fields:

  * `error_code`, `error_name`, `error_category`, `http_status`
  * `ray_id`, `timestamp`, `zone`
  * `cloudflare_error`, `retryable`, `retry_after` (when applicable), `owner_action_required`



Default behavior is unchanged: clients that do not explicitly request Markdown continue to receive HTML error pages.

#### Negotiation behavior

Cloudflare uses standard HTTP content negotiation on the `Accept` header.

  * `Accept: text/markdown` -> Markdown
  * `Accept: text/markdown, text/html;q=0.9` -> Markdown
  * `Accept: text/*` -> Markdown
  * `Accept: */*` -> HTML (default browser behavior)



When multiple values are present, Cloudflare selects the highest-priority supported media type using `q` values. If Markdown is not explicitly preferred, HTML is returned.

#### Availability

Available now for Cloudflare-generated 1xxx errors.

#### Get started
    
    
    curl -H "Accept: text/markdown" https://<your-domain>/cdn-cgi/error/1015

Reference: [Cloudflare 1xxx error documentation](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/)
