---
url: https://developers.cloudflare.com/cloudflare-challenges/reference/challenge-solve-rate/
title: Challenge solve rate (CSR) \u00b7 Cloudflare challenges docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:59.102056+00:00
---

# Challenge solve rate (CSR) · Cloudflare challenges docs

> Source: https://developers.cloudflare.com/cloudflare-challenges/reference/challenge-solve-rate/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Challenges](https://developers.cloudflare.com/cloudflare-challenges/)
  3. /Reference
  4. /Challenge solve rate (CSR)



# Challenge solve rate (CSR)

Last updated Aug 3, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-challenges/reference/challenge-solve-rate/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewChallenge actions in Security EventsFailed Challenges

The Challenge solve rate (CSR) is the percentage of issued challenges — Non-Interactive Challenge, Managed Challenge, or Interactive Challenge actions — that were solved.

Every challenge involves two separate events:

  * **Challenge trigger** : The original request matches a WAF rule with a challenge action. Cloudflare issues a challenge to the visitor's browser.
  * **Challenge solved** : The visitor's browser completes the challenge and sends back a validated response. This event is logged as challenge Solved.



Most automated traffic abandons immediately upon encountering the challenge script and never reaches the second event. This is why the count of unsolved challenges is typically very large — those abandonments count as failures in the formula.
    
    
    CSR = number of challenges solved / number of challenges issued

CSR indicates the false positive percentage of a rule. A high CSR means a large share of issued challenges were solved by real visitors, which may indicate the rule is matching too much legitimate traffic. Use CSR to evaluate whether your rule's criteria or action needs adjustment.

You can find the CSR of a rule by going to its corresponding dashboard page:

For [custom rules](https://developers.cloudflare.com/waf/custom-rules/) or [rate limiting rules](https://developers.cloudflare.com/waf/rate-limiting-rules/), go to your zone > **Security** > **Security rules**.

* * *

## Challenge actions in Security Events

If you find a Challenge Solved action, such as `[js]challengeSolved` or `challengeSolved`, in your Security Events that does not match the underlying rule criteria, it is because this action refers to the successful mitigation of a previous request — not a re-match of the original rule.

The parameters of the solved request may no longer match the original rule's expression. For example, if a challenge was issued due to a low bot score, the score for the solved request may have already changed to a non-suspicious value upon successful verification.

The Challenge Solved action is an informative signal that a previously issued challenge was answered, allowing the visitor's traffic to proceed.

* * *

## Failed Challenges

You will not find a dedicated metric for failed challenges in Security Analytics because Cloudflare calculates failure indirectly, based on the difference between challenges issued and challenges solved.

The system views any issued challenge that does not result in a successful clearance cookie as a failure. This is why the number of failed challenges may appear exceptionally high: the majority of issued challenges are never completed.

The official calculation for failures is:
    
    
    Failed Challenges = Total Challenges Issued − Total Challenges Solved

The large number of unmatched challenges is primarily due to automated traffic (bots or scrapers) that abandon the process immediately upon encountering the initial challenge script.

Key reasons a challenge may be issued but never solved:

  * The visitor gives up on the challenge or navigates away from the page.
  * The visitor attempts to solve the challenge but cannot provide a valid answer.
  * The system receives an invalid or malformed answer from the client.
  * The script environment (often a bot's controlled browser) fails to run the necessary client-side checks.



[PreviousChallenge solve issues](https://developers.cloudflare.com/cloudflare-challenges/troubleshooting/challenge-solve-issues/)[NextPrivate Access Tokens (PAT)](https://developers.cloudflare.com/cloudflare-challenges/reference/private-access-tokens/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-challenges/reference/challenge-solve-rate.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
