---
url: https://developers.cloudflare.com/cache/cache-security/avoid-web-poisoning/
title: Avoid Web Cache Poisoning \u00b7 Cloudflare Cache (CDN) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:40.863024+00:00
---

# Avoid Web Cache Poisoning · Cloudflare Cache (CDN) docs

> Source: https://developers.cloudflare.com/cache/cache-security/avoid-web-poisoning/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cache / CDN](https://developers.cloudflare.com/cache/)
  3. /Cache security
  4. /Avoid web cache poisoning



# Avoid web cache poisoning

Last updated May 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cache/cache-security/avoid-web-poisoning/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewLearn about Cache PoisoningOnly cache files that are truly staticDo not trust data in HTTP headersDo not trust GET request bodiesMonitor web security advisories

A cache poisoning attack uses an HTTP request to trick an origin web server into responding with a harmful resource that has the same cache key as a clean request. As a result, the poisoned resource gets cached and served to other users.

A Content Delivery Network (CDN) like Cloudflare relies on cache keys to compare new requests against cached resources. The CDN then determines whether the resource should be served from the cache or requested directly from the origin web server.

## Learn about Cache Poisoning

To deepen your understanding of the risks and vulnerabilities associated with cache poisoning, consult the following resources:

  * [Practical Web Cache Poisoning ↗︎](https://portswigger.net/blog/practical-web-cache-poisoning)
  * [How Cloudflare protects customers from cache poisoning ↗︎](https://blog.cloudflare.com/cache-poisoning-protection/)



## Only cache files that are truly static

Review the caching configuration for your origin web server and ensure you are caching files that are static and do not depend on user input in any way. To learn more about Cloudflare caching, review:

  * [Which file extensions does Cloudflare cache for static content?](https://developers.cloudflare.com/cache/concepts/default-cache-behavior/)
  * [How Do I Tell Cloudflare What to Cache?](https://developers.cloudflare.com/cache/how-to/cache-rules/)



## Do not trust data in HTTP headers

Attackers can exploit HTTP headers to inject malicious content into cached responses. For example, if your application reflects an untrusted header value in the response body, an attacker could use this to perform cross-site scripting (XSS) through the cache. To reduce this risk:

  * Do not rely on values in HTTP headers if they are not part of your [cache key](https://developers.cloudflare.com/cache/how-to/cache-keys/).
  * Do not include untrusted header values in your response body.



## Do not trust GET request bodies

Cloudflare caches contents of GET request bodies, but they are not included in the cache key. GET request bodies should be considered untrusted and should not modify the contents of a response. If a GET body can change the contents of a response, consider bypassing cache or using a POST request.

## Monitor web security advisories

To keep informed about Internet security threats, Cloudflare recommends that you monitor web security advisories on a regular basis. Some of the more popular advisories include:

  * [Drupal Security Advisories ↗︎](https://www.drupal.org/security)
  * [Symfony Security Advisories ↗︎](https://symfony.com/blog/category/security-advisories)
  * [Laminas Security Advisories ↗︎](https://getlaminas.org/security/advisories)



[PreviousCache performance](https://developers.cloudflare.com/cache/performance-review/cache-performance/)[NextCache Deception Armor](https://developers.cloudflare.com/cache/cache-security/cache-deception-armor/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cache/cache-security/avoid-web-poisoning.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
