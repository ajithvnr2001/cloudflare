---
url: https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/detect-response/
title: Detect a Challenge Page response \u00b7 Cloudflare challenges docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:58.656493+00:00
---

# Detect a Challenge Page response · Cloudflare challenges docs

> Source: https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/detect-response/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Challenges](https://developers.cloudflare.com/cloudflare-challenges/)
  3. /…

Available Challenges

  4. /[Interstitial Challenge Pages](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/)
  5. /Detect a Challenge Page response



# Detect a Challenge Page response

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/detect-response/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

When a request encounters a Cloudflare Challenge Page instead of the originally anticipated response, the Challenge Page response (regardless of the Challenge Page type) will have the `cf-mitigated` header present and set to `challenge`. This header can be leveraged to detect if a response was challenged when making fetch/XHR requests. This header provides a reliable way to identify whether a response is a Challenge or not, enabling a web application to take appropriate action based on the result. For example, a front-end application encountering a response from the backend may check the presence of this header value to handle cases where Challenge Pages encountered unexpectedly.

Note

Regardless of the requested resource-type, the content-type of a challenge will be `text/html`.

For the `cf-mitigated` header, `challenge` is the only valid value. The header is set for all Challenge Page types.

To illustrate, here is a JavaScript code snippet that demonstrates how to use the `cf-mitigated` header to detect whether a response was challenged:
    
    
    fetch("/my-api-endpoint").then((response) => {
    	if (response.headers.get("cf-mitigated") === "challenge") {
    		// Handle challenged response
    	} else {
    		// Process response as usual
    	}
    });

[PreviousChallenge Passage](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/challenge-passage/)[NextResolve a Challenge](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/resolve-challenge/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-challenges/challenge-types/challenge-pages/detect-response.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
