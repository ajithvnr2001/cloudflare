---
url: https://blog.cloudflare.com/rss/
title: Cloudflare Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:46.703333+00:00
---

# Cloudflare Blog

> Source: https://blog.cloudflare.com/rss/

Cloudflare BlogTechnical deep dives, product updates, and insights from the teams that are helping to build a better Internet.https://blog.cloudflare.com/ en-ushttps://blog.cloudflare.com/favicon.icoCloudflare Bloghttps://blog.cloudflare.com Thu, 08 Oct 2026 08:05:45 GMTBuilding an evidence-grounded agentic security operations harness on Cloudflarehttps://blog.cloudflare.com/agentic-security-operations/ Wed, 07 Oct 2026 16:30:36 GMTCloudflare Managed Defense uses a team of specialized AI agents built on Workers and global network telemetry to analyze security alerts. By separating deterministic evidence collection from model inference, the system delivers grounded recommendations to Managed Defense Analysts.Deanna TranJavier CastroJacob CrispBlake DarchéArtificial IntelligenceCloudforce OneDevelopersEngineeringSecuritySecurity alerts rarely arrive one at a time. A single alert can cause a spike across the environment, requiring a human analyst to decide which alerts are related and what they mean. When multiple arrive at the same time, it can quickly overwhelm even a seasoned security analyst. Enter the alert paradox. Now, our built-in, multi-AI-agent security operations harness can handle more of this work at Cloudflare scale.

Our [Cloudflare Managed Defense](https://www.cloudflare.com/managed-defense/) AI agent harness speeds up the process of gathering data, connecting and aggregating detections, and accounting for missing sources while new alerts continue to arrive. To further analyze context, we make use of the [OpenAI Daybreak Defense Network](https://openai.com/daybreak/partners/) and our partnership with Anthropic. Cloudflare uses approved OpenAI Daybreak and Anthropic models, including GPT-5.6 Cyber and Mythos, for deeper model-backed analysis. Initial analysis and scoring is done with [Clef](https://blog.cloudflare.com/clef-decision-models/), Cloudflare’s open-source decision model.

Collecting evidence to understand what each alert means requires a lot of time. Even in a highly sophisticated Security Information and Event Management (SIEM), too much is still left for a human to review. Human analysts must gather data, connect and aggregate detections, and account for missing sources while new alerts continue to arrive.

Think about every time a human analyst reviews an alert: "Which should we silence? Which action should we take? Which alert should we ignore? Which should we resolve as false positives? Which should we resolve as true positives? Which should trigger our incident team?" We address this predicament with our AI agent strategy. Our approach reduces all of those questions and gives Managed Defense Analysts a quick and consolidated view, directly providing insight into related alerts, admitted evidence, visible gaps, and recommended next steps. The result: cutting back on the time needed to analyze, and creating a hyper focus on actually getting security alerts resolved and mitigations deployed.

## Why a single agent fails

Our first prototype showed the limits of one general-purpose agent. We provided the AI agent the whole investigation. It produced useful analysis, but it also hallucinated claims the evidence did not support. Telemetry, detector descriptions, policies, and threat intelligence were flattened into one prompt, which caused their distinct roles to merge together.

We saw three recurring problems with our first single-shot AI agent harness:

  * **Context became authority**. A detection is a hypothesis, not proof that an exploit succeeded or an attack occurred. A broad AI agent can blur that distinction.
  * **Scope drifted.** An AI agent can query the wrong account, time range, or source. You can’t rely on a language model prompt to be a boundary.
  * **Failure disappeared.** If a lookup times out, the result may not distinguish "not checked" from "checked and not found."



To address these challenges we moved evidence collection and scope enforcement into application code, before model analysis begins.

## Recon first, inference second

It's tempting to put an AI agent at every step. The front half of our harness has none.

Before we even call inference, deterministic code runs a fixed set of reconnaissance workflows with versioned API calls. It collects the customer's identity, detection history, traffic baseline, enforcement outcome, and network observations. Each piece of data is stored with its source, version, and timestamp.

Cloudflare sees both the request and the action applied to it. That lets the investigation connect the behavior that triggered an alert with both the control that fired and its outcome.

The fixed recon snapshot also makes evaluation reproducible. If AI agents fetch their own data, two runs may disagree because their inputs changed. Here, the same snapshot can be replayed, so differences between specialist AI agents’ findings come from interpretation rather than retrieval.

## Filter noise early

Most alerts are not incidents. The same rule often fires repeatedly on a known traffic pattern, and paging Managed Defense Analysts every time makes it easier to miss a real security incident.

We needed a lightweight triage model to compare each alert with its reconnaissance data: Has this event been detected for the customer before? What did Managed Defense Analysts decide previously? Does the traffic look consistent with normal human behavior? Alerts scored with a high likelihood to be false positives skip analysis by the specialist AI agents.

[Clef](https://blog.cloudflare.com/clef-decision-models/), running on Workers AI, was the perfect fit for this type of fast agentic reasoning. 

Known high-volume noise is deterministically classified as passive when it arrives. It remains available as context but does not enter the active queue.

## Specialist AI agents handle the investigation

For alerts that need deeper review, a coordinator AI agent runs four specialist AI agents in parallel:

  * **Traffic analysis** reviews request behavior, historical changes, and enforcement.
  * **Customer context** reviews earlier alerts, dispositions, and Managed Defense Analysts’ decisions.
  * **Global telemetry** compares the activity with privacy-preserving Internet-wide signals.
  * **Threat intelligence** checks indicators already admitted to the alert or case.



A synthesis AI agent combines their typed findings into one advisory; it can’t fetch new evidence or choose a classification outside the approved vocabulary. Keeping each task narrow makes unsupported claims easier to catch, and recommendations easier to audit.

## Global context without customer data

A security tool knows what happened inside the environment it is deployed in, but little about the world beyond it. Cloudflare compares an alert with patterns seen across its global network.

For example, an IP may be targeting one site, scanning thousands of sites, or appearing for the first time. Those patterns carry different weights. To preserve customer privacy, the global telemetry specialist works only with aggregates; it never receives another customer's individual records or identity.

This view combines features from Cloudflare's [CDN](https://www.cloudflare.com/products/cdn/), [WAF](https://www.cloudflare.com/products/waf/), [DDoS](https://www.cloudflare.com/products/ddos/), [Turnstile](https://www.cloudflare.com/products/turnstile/), [Rate Limiting](https://www.cloudflare.com/products/rate-limiting/), and [Cloudforce One threat intelligence](https://www.cloudflare.com/cloudforce-one/services/threat-intelligence/). The synthesis AI agent weighs both global reputation and customer history. This ensures a globally common pattern can still be used on a per-customer basis, but does not automatically imply a widespread campaign for all customers.

## History is evidence

Every evaluation is conscious of what came before it: the alert, the pattern, and which customer. The recon dossier records the alert's own track record including how many times this service alert has fired, how many of those were dispositioned as false positives, and what the Managed Defense Analyst concluded. An attack pattern that has been benign every time your Managed Defense Analysts have seen it is a very different object from the first sighting of something new, and the specialist AI agents are told which one they are looking at. Approved background context is retrieved from previous alerts and cases, so yesterday's conclusions are carried into today's decision, instead of being rebuilt from scratch.

Our system aggregates related alerts into a consolidated case. In each case, we store evidence, findings, and recommendations. Our system deterministically joins and correlates this data, but we leave it to a Managed Defense Analyst to confirm the actual scope. Over time, a case can connect network, application, and Zero Trust evidence together, while tracking the source of the evidence for additional context and reference purposes.

## From evidence to decision

Before analysis, the system creates a versioned evidence package with the subject, scope, time anchor, admitted evidence, policy versions, sources, and coverage gaps. Specialists must cite items in that package. Application code checks that every citation exists, belongs to the investigation, and supports the attached claim. Invalid findings are corrected or recorded as limitations.

We lean on Clef a second time to score our evidence. Is the collected evidence enough for a decision? Does any of our collected evidence contradict? Based on this evidence, Clef picks from a deterministically reduced list of attack classifications and dispositions.

Cloudflare's developer platform runs this process. Application code on Workers admits evidence and validates results; [Workflows](https://developers.cloudflare.com/workflows/) coordinates each stage and saves completed work before the next begins, so a failed stage reuses evidence and findings that already passed validation instead of starting over. [D1](https://developers.cloudflare.com/d1/) keeps investigation and advisory state, [R2](https://developers.cloudflare.com/r2/) holds bounded context and evidence artifacts. Case-chat state persists in [Durable Objects](https://developers.cloudflare.com/durable-objects/), uses [Flue](https://flueframework.com/), and is enriched with [AI Search](https://developers.cloudflare.com/ai-search/).

Finally, an LLM-powered agent produces an advisory report using terms that Managed Defense Analysts already work with: affected surface, enforcement outcome, relevant controls, and next step. Managed Defense Analysts can inspect evidence, investigate further, revise the recommendation, or group alerts into a case. Application code fixes the customer scope before any model sees results, and gives each specialist only the evidence it needs. The model never receives authority to cross tenant boundaries or act for the Managed Defense Analysts.

## Handling incomplete evidence

At network scale, a source will sometimes fail. A comparison may time out, metadata may be missing, or a threat intelligence lookup may return no match. The system keeps evidence already collected and records the gap.

The advisory distinguishes three states:

  * Not checked
  * Checked, with no matching result
  * Checked, with evidence supporting absence



If global telemetry is unavailable, the system can describe what is unusual for the customer but cannot say whether the pattern is widespread. When the evidence is insufficient, it makes no classification or disposition recommendation.

## Remediation

A useful recommendation should lead to a solution, rather than a ticket. The advisory might suggest a rate limiting rule for an abusive path, a WAF custom rule for a signature, or a DDoS protection change. For fully managed customers, Managed Defense Analysts can apply the suggested rules; other customers will receive their recommendations in the dashboard and through their chosen alert path.

In the end, the Managed Defense Analyst remains responsible for the decision and any mitigation. Each alert and case includes the evidence behind the AI agent’s recommendation, which empowers the Managed Defense Analyst to reach a conclusion by accepting or updating the AI agent’s advice.

## What comes next

Managed Defense Analysts remain responsible for judgment. The AI agent harness handles more of the repetitive work: assembling investigations, connecting related events, and showing the evidence behind each recommendation. Over the next few quarters, we plan to add a Custom Managed level with more flexibility for each organization.

We also plan to explore continuous AI agents that monitor Cloudflare traffic and surface patterns that fixed rules and thresholds may miss.

The early beta is available in[ Cloudflare Managed Defense](https://www.cloudflare.com/managed-defense/) for eligible application-security alerts and cases. If you already use Cloudflare WAF, DDoS protection, Magic Transit, or[ another supported product](https://www.cloudflare.com/managed-defense/), talk to your enterprise account team about adding Managed Defense.

]]>01M49SJF5QT2EPN5CTQ3C99EZWThe keys to the Internet change on October 11. Are you ready?https://blog.cloudflare.com/root-ksk-2024-rollover/ Tue, 06 Oct 2026 17:50:11 GMTOn October 11, 2026, the DNS root switches to a new key-signing key (KSK-2024). Learn what this means for you, and how RFC 8509 trust anchor sentinels allow you to test whether your DNS resolver is ready for the rollover.Sebastiaan NeuteboomJames Godlewski1.1.1.1CryptographyDNSDNSSECReliabilityOn October 11, 2026, the DNS root is scheduled to change its key-signing key (KSK) for only the second time ever. This key anchors DNSSEC’s chain of trust, which lets DNS resolvers authenticate answers using cryptographic signatures. The change is called a KSK rollover. Validating resolvers need to trust the new key before the switch, as otherwise healthy websites could become unreachable.

When we [wrote about the first root KSK rollover in 2018](https://blog.cloudflare.com/its-hard-to-change-the-keys-to-the-internet-and-it-involves-destroying-hsms/), we had seen resolvers lose their learned trust in the new key during software upgrades or moves between machines. Publishing the key well in advance was only part of the job. We also needed to know whether resolvers had retained it, and we couldn’t give users a practical way to check.

Most website operators do not need to make any changes for this rollover. If you run a DNSSEC-validating resolver, check that it trusts the new root key, KSK-2024, and follow your software vendor’s instructions to update its trust anchors if the key is missing. If you use Cloudflare for your domain's DNS or rely on 1.1.1.1 and Gateway DNS, you do not need to take any action — our systems already trust KSK-2024.

To check ahead of time, visit our [rollover readiness test](https://dnstest.dev/ksk-2024/). It asks the resolver your browser uses whether it trusts the new key. The test uses [RFC 8509: A Root Key Trust Anchor Sentinel for DNSSEC](https://datatracker.ietf.org/doc/html/rfc8509), which we’ve implemented in 1.1.1.1 ahead of the rollover.

## Where DNSSEC trust begins

A DNS resolver looks up the addresses of websites and other services for your device. DNSSEC lets it check digital signatures on DNS records to verify that they are authentic and have not been changed. The resolver also needs to check that the public keys used to verify those signatures belong to the right domains.

For `cloudflare.com`, this follows a chain of trust from the DNS root to `.com`, then to `cloudflare.com`. Each parent publishes a Delegation Signer (DS) record containing a fingerprint of its child’s public key. For example, `.com` publishes the DS record for `cloudflare.com`, allowing the resolver to check that domain’s key.

That chain needs a starting point. The root, however, has no parent to confirm which keys belong to it. Instead, a resolver checking DNSSEC starts with a root public key, or its fingerprint, that it already trusts. This is called a trust anchor.

The root’s signing keys have two different jobs. The zone-signing key (ZSK) signs the root’s DNS records, including the DS records for top-level domains such as `.com`. The key-signing key (KSK) signs the list of public keys published by the root, called the DNSKEY record set. The resolver uses its trusted KSK to verify that list, then uses the ZSK from the list to verify the root’s other records.

The diagram below shows the arrangement for a typical signed zone. For the root, trust comes from the resolver’s trust anchor rather than a DS record in a parent zone.

Our posts about the [.de](https://blog.cloudflare.com/de-tld-outage-dnssec/) and the [.al](https://blog.cloudflare.com/dnssec-nta-ede-33/) rollover failures showed the consequence of failed DNSSEC checks: websites can be working normally but still be unreachable. The root KSK rollover changes the starting point of those checks. If a resolver does not trust the replacement key, its users may be unable to reach websites under **any** top-level domain.

The new key is [KSK-2024](https://www.icann.org/resources/pages/ksk-rollover-en), identified by key tag `38696`. It will replace KSK-2017, key tag `20326`, as the signer of the root’s DNSKEY set. Validating resolvers need to trust the new key before that switch.

## How resolvers get the new root key

[RFC 5011](https://datatracker.ietf.org/doc/html/rfc5011) lets resolvers learn a new root trust anchor automatically. The root publishes the new KSK alongside the existing one in its DNSKEY set. The existing KSK continues signing that set, so a resolver can use the key it already trusts to verify the records containing the replacement.

Before accepting the new key as a trust anchor, the resolver waits at least 30 days and keeps checking the root’s signed DNSKEY records. The new key must remain in the records it checks during that period. After the wait, the resolver must successfully verify the records containing the new key again before accepting it.

For this rollover, [KSK-2024 has been published in the root’s DNSKEY set since January 11, 2025](https://www.iana.org/dnssec/files). That gave resolvers with automatic trust-anchor updates time to discover and accept it ahead of the scheduled October 11, 2026 signing change. Each resolver’s waiting period starts when it first sees and verifies the new key.

For our resolver, we added KSK-2024 directly to the software’s built-in trust anchors in July 2024, alongside KSK-2017. A resolver running the updated software therefore has the new anchor available from startup.

We chose this approach because of our experience during preparations for the first rollover. As described in [our 2018 post](https://blog.cloudflare.com/its-hard-to-change-the-keys-to-the-internet-and-it-involves-destroying-hsms/#operational-reality-vs-the-protocol-design), software upgrades and moves between machines caused some resolvers to lose their learned trust-anchor state. We fixed that by updating the software to include the new anchor by default. Including KSK-2024 in the software likewise avoids depending on each resolver retaining a key it learned automatically.

Even though we added KSK-2024 to our resolver’s built-in trust anchors in July 2024, users of 1.1.1.1 and [Gateway DNS](https://www.cloudflare.com/products/gateway/) had no direct way to check whether the resolver answering their queries trusted the new key.

## This time, ask the resolver

[RFC 8509](https://datatracker.ietf.org/doc/html/rfc8509) defines the root key trust anchor sentinel, a way to ask a supporting resolver whether it trusts a particular root key. It uses ordinary DNS queries with specially named domains.

[Our readiness test website](https://dnstest.dev/ksk-2024/) uses this protocol to check for KSK-2024. Two names ask opposite questions: `is-ta-38696` asks whether the key is trusted, `not-ta-38696` asks whether it is not trusted.

Both names have valid DNSSEC-signed address records. A resolver that supports the sentinel first validates those records, then either returns the response directly or replaces the answer with `SERVFAIL`, depending on whether it trusts the key.

For a validating resolver with sentinel support, the expected results are:

Query| KSK-2024 is trusted| KSK-2024 is not trusted  
---|---|---  
`is-ta-38696`| Returns a valid response| Returns `SERVFAIL`  
`not-ta-38696`| Returns `SERVFAIL`| Returns a valid response  
  
For a validating resolver with sentinel support, `SERVFAIL` for `not-ta-38696` is expected when KSK-2024 is trusted. The resolver deliberately rejects the “not trusted” query.

Sentinel labels such as `root-key-sentinel-is-ta-38696` can be used under any DNSSEC-signed domain. We use `dnstest.dev` for our tests. You can run the two queries directly against 1.1.1.1:

The website also checks that an ordinary signed name resolves, that a deliberately invalid DNSSEC name is rejected, and that the resolver responds to a sentinel query for the current root key. These controls help distinguish a meaningful result from a failed lookup or unsupported protocol. If sentinel support cannot be established, the result is inconclusive; it does not mean the new key is missing.

The browser test checks the resolver your browser uses, which may be affected by Secure DNS or a VPN. The `dig` commands above explicitly query 1.1.1.1. Both provide a snapshot of the resolver path answering those requests.

## New key, same algorithm

KSK-2017 and KSK-2024 both use RSA/SHA-256. The rollover replaces the key pair while keeping the same method for creating and verifying signatures.

In [our 2018 post](https://blog.cloudflare.com/its-hard-to-change-the-keys-to-the-internet-and-it-involves-destroying-hsms/#why-are-we-rolling-the-root-key-trust-anchor), we wrote that a successful rollover would open the door to discussing an algorithm change. Eight years later, the root still uses RSA.

Replacing the key remains useful. It limits how long a single private key stays in use and exercises the process of distributing new trust anchors, updating resolvers, and retiring old keys. As the first rollover showed, those steps can fail even when the cryptography itself works correctly.

[The Internet Assigned Numbers Authority (IANA) plans an idealized three-year rollover interval](https://www.iana.org/dnssec/files), balancing regular practice against the work and risk of changing the root key too frequently. The gap since 2018 has been longer. [The Internet Corporation for Assigned Names and Numbers (ICANN) attributes the delay](https://www.icann.org/en/blogs/details/preparing-for-the-root-zone-ksk-rollover-what-you-need-to-know-27-07-2026-en) to pandemic disruption and upgrades to the hardware that protects the private signing keys.

Changing algorithms means resolvers need both a new trust anchor and software that can verify the new signatures. Regular key rollovers let operators test the trust-anchor updates while keeping the algorithm the same.

## What comes after October

The October 11 switch changes which KSK signs the root’s DNSKEY set. The rollover continues into 2027, when [ICANN plans to revoke KSK-2017, remove it from the root zone, and delete its private key](https://www.icann.org/en/system/files/files/root-zone-ksk-rollover-faq-22may26-en.pdf). Stopping a key from signing and removing trust in that key are separate steps.

ICANN has also [proposed a future root algorithm rollover to ECDSA P-256](https://itp.cdn.icann.org/en/files/domain-name-system-dns-engineering/proposal-for-root-zone-ksk-algorithm-rollover-03-02-2026-en.pdf). [ECDSA](https://www.cloudflare.com/learning/dns/dnssec/ecdsa-and-dnssec/) produces smaller keys and signatures than the RSA algorithm used today. That proposal is separate from this October’s key replacement, and ECDSA is not a post-quantum algorithm.

[1.1.1.1 now validates ML-DSA-44 signatures](https://blog.cloudflare.com/post-quantum-dnssec-1111/), which are designed to remain secure against attacks using quantum computers. For DNSSEC’s whole chain of trust to become post-quantum secure, signed domains, their parent zones, and the root must adopt post-quantum cryptography too. At the root, that means introducing a post-quantum KSK and getting resolvers to trust it.

That will require another root key rollover. The rollovers we perform now let operators test how they distribute replacement trust anchors, check that resolvers have accepted them, and retire the old keys. This October’s rollover keeps RSA, but exercises the trust-anchor updates we will need when the root moves to post-quantum cryptography. The sentinel gives us a way to check whether resolvers followed those updates.

We encourage DNS providers and resolver developers to support [RFC 8509 trust anchor sentinels](https://datatracker.ietf.org/doc/html/rfc8509). If your resolver does not support them, ask your provider or software vendor to add support. Users should be able to check whether their resolver trusts the next root key before a rollover.

For now, the next deadline is October 11. You can check your resolver’s readiness at [https://dnstest.dev/ksk-2024](https://dnstest.dev/ksk-2024). If you operate a DNSSEC-validating resolver, confirm that it trusts KSK-2024, key tag `38696`, and follow [ICANN’s guidance](https://www.icann.org/resources/pages/ksk-rollover-en) and your software vendor’s instructions if the key is missing.

]]>01M490D3EE2TBV2NFMN6FXMMQ8Everything we launched during Birthday Week 2026https://blog.cloudflare.com/birthday-week-2026-wrap-up/ Mon, 05 Oct 2026 13:00:00 GMTWe celebrated our 16th birthday with 46 announcements across open source, post-quantum security, AI agents, and developer platform upgrades. Here’s a day-by-day roundup of everything we shipped.Carlos ArmadaMeagan GamacheAgentsAIBirthday WeekcfProduct NewsWorkersWe celebrated our 16th birthday last week by sharing how we’re building a better Internet for today’s world. As Matthew and Michelle reflected in [this year’s Founders’ Letter](https://blog.cloudflare.com/cloudflares-2026-annual-founders-letter/), this year saw some of the most consequential changes in the history of the Internet.

For the first time, automated traffic surpassed human activity. AI is empowering people to build like never before, leading the Internet to grow massively in scale and unlocking more ambition and creativity. As we witnessed the influence that agent-driven recommendations have on consumer choices, we identified the need for a new approach that creates space for new businesses to succeed.

Each day of Birthday Week explored a different way we are helping to build the future of the Internet. We began on Monday by strengthening our commitment to open source. Tuesday focused on application security and the post-quantum transition. On Wednesday, we explored new economic models for the agentic Internet. Thursday, we expanded the Developer Platform with new tools for data analysis, storage, AI, and agent development. Finally, we closed out the week by launching features that make Cloudflare faster, easier to operate, and more accessible to everyone. As a special Birthday Week follow-up, we [shared an update](http://blog.cloudflare.com/one-year-later-1111-interns) on our intern program, [one year after announcing our goal to hire 1,111 interns](https://blog.cloudflare.com/one-year-later-1111-interns/). Interns directly contributed to many of the projects launched this week, including EmDash, post-quantum visibility, CryptoLabe, and Protected Quick Tunnels.

We shipped 46 announcements this week. In case you missed any, here’s the full list of everything we announced during Birthday Week 2026.

### Monday, September 28 - Commitment to open source

With the announcement of our new CLI, which we released alongside the pipeline we use to generate it and our SDKs and docs, we shared how we’re building to support agents and developers as they use Cloudflare — and supporting the projects that you rely on, too.

**What**| **In a sentence…**  
---|---  
[Introducing cf: the agentic CLI for the entire Cloudflare API](https://blog.cloudflare.com/cloudflare-cf-cli-launch/)| The new cf CLI mirrors the Cloudflare API, uses JSON-first output and typed configuration, and gives people and agents one consistent command-line interface.  
[Introducing Forge: the open source pipeline for generating SDKs, CLIs, docs, and more](https://blog.cloudflare.com/forge-open-source-generation-pipeline/)| Forge is a pluggable, open-source pipeline that runs in CI to generate SDKs, CLIs, documentation, and other interfaces directly from API definitions.  
[Introducing EmDash - the spiritual successor to WordPress that solves plugin security](https://blog.cloudflare.com/emdash-cms-plugin-registry)| EmDash is an open-source, Astro-based serverless CMS that runs plugins in isolated Worker sandboxes with explicitly approved capabilities.  
[Four months of VoidZero at Cloudflare: making the open-source JavaScript toolchain faster for all humans and agents](https://blog.cloudflare.com/voidzero-update/)| Since joining Cloudflare, VoidZero has delivered more than 80 releases across the Vite ecosystem, and its previously commercial Void platform will become fully open source.  
[Next.js applications, powered by Vite: introducing Vinext 1.0](https://blog.cloudflare.com/vinext-nextjs-on-vite/)| Vinext 1.0 turns an AI-built experiment into a production-ready, portable way to run Next.js applications on Vite.  
[The road to the agentic browser: A Kitesurf update](https://blog.cloudflare.com/kitesurf-update/)| Kitesurf, our Workers-based browser for agents, adds WebMCP support, faster DOM operations, broader web compatibility, and terminal-based rendering.  
[How fast is the web? Explore billions of real-user measurements with BEACON](https://blog.cloudflare.com/how-fast-is-the-web/)| BEACON makes billions of anonymized real-user performance measurements from 10,000 major websites available as a public BigQuery dataset.  
[Supporting native Rust in Workers with the new Emscripten target for wasm-bindgen](https://blog.cloudflare.com/rust-workers-emscripten-target/)| Experimental Emscripten target support lets developers bring more native Rust libraries and applications, including progress toward Tokio support, to Workers.  
[Introducing The Cold Start: pitch your startup live at Cloudflare Connect](https://blog.cloudflare.com/introducing-the-cold-start/)| The Cold Start gives five early-stage companies the opportunity to pitch live at Cloudflare Connect and compete for resources to help them grow.  
  
### Tuesday, September 29 - Helping secure the agentic Internet

Technological progress is rapidly changing how we think about application security. We announced our intention to become a certificate authority, as well as how we’re preparing foundational Internet cryptography for the post-quantum era and adapting application security to counter AI-driven attacks.

**What**| **In a sentence…**  
---|---  
[Building a certificate authority for the whole Internet](https://blog.cloudflare.com/cloudflare-certificate-authority/)| Twelve years after launching Universal SSL, Cloudflare announced its intention to become a public certificate authority (CA) and add resilience to free, automated certificate issuance.  
[Building a post-quantum certificate authority with Merkle Tree Certificates](https://blog.cloudflare.com/pq-ca-with-mtcs/)| Our planned CA will issue free Merkle Tree Certificates designed to make post-quantum authentication practical without imposing large certificate and handshake costs.  
[Using AI to chart a course for our post-quantum migration](https://blog.cloudflare.com/ai-driven-cryptography-discovery/)| CryptoLabe uses AI to find and classify cryptography across our codebase as Cloudflare works toward completing its post-quantum migration by 2029.  
[Preventing quantum downgrade attacks against IPsec](https://blog.cloudflare.com/ipsec-downgrade-protection/)| Cloudflare helped develop an IETF extension that authenticates the full IKEv2 transcript and prevents attackers from downgrading post-quantum IPsec tunnels.  
[Is your domain using post-quantum encryption? Now you can see for yourself](https://blog.cloudflare.com/post-quantum-visibility/)| HTTP Analytics, Log Explorer, and Logpush now show whether requests negotiated post-quantum key exchange, giving customers evidence they can inspect and report.  
[Enforce positive security with Cloudflare Application Profiles](https://blog.cloudflare.com/application-profiles/)| Application Profiles learns the expected structure of HTTP requests so customers can identify deviations and enforce what valid application traffic should look like.  
[We tested our own WAF with frontier AI models. Here's what we found](https://blog.cloudflare.com/adaptive-ai-waf-testing/)| An adaptive AI red-team system found WAF detection gaps across six attack categories, helping us improve normalization and managed rules for customers.  
[Introducing Threat Signals: agentic skills for open-source threat intelligence, free for every Cloudflare account](https://blog.cloudflare.com/threat-signals/)| Threat Signals turns open-source reporting into structured indicators and connects the context to WAF rules, while the Threat Events Platform expands to every account.  
[Adaptive application security for the AI era: how Cloudflare connects code, traffic, and intelligence to stop attacks](https://blog.cloudflare.com/ai-era-framework/)| Our application-security framework connects discovery, governance, runtime protection, investigation, and response in a continuous learning loop.  
  
### Wednesday, September 30 - Powering the agent economy

With our announcements of Pay Per Use and the release of our Monetization Gateway in beta, we shared how we’re building support for a new economic model that empowers creators to monetize their content and services.

**What**| **In a sentence…**  
---|---  
[The Internet has a second audience](https://blog.cloudflare.com/agentic-web/)| AI agent requests have grown rapidly, and our strategy helps creators see agents, set terms for access, and get paid when agents use their work.  
[Cloudflare Containers, rebuilt to scale agent sandboxes](https://blog.cloudflare.com/faster-agent-sandboxes/)| Containers now has faster startup, flexible image and instance selection, new scheduling controls, and filesystem snapshots for persistent agent workspaces.  
[Monetization Gateway beta: charge AI agents for consumption with HTTP 402](https://blog.cloudflare.com/monetization-gateway-beta/)| Monetization Gateway lets sellers put a price on resources behind Cloudflare and collect agent payments using HTTP 402 and x402.  
[Pay Per Use: when AI uses your work, you should get paid](https://blog.cloudflare.com/pay-per-use/)| Pay Per Use gives enrolled publishers usage reports, billing, and payouts when verified AI buyers use their content.  
[Simplifying domains for people and agents](https://blog.cloudflare.com/simplifying-domains/)| A new domain-search experience and expanded Registrar APIs make it easier for both people and agents to search, register, transfer, and manage domains.  
[Identify AI model overuse with User Insights](https://blog.cloudflare.com/ai-model-overuse-user-insights/)| AI Gateway User Insights identifies tasks, model fit, and overuse, so teams can understand where a smaller or less expensive model may work.  
[Detect and send production issues straight to your agent](https://blog.cloudflare.com/real-time-issue-detection/)| Issues groups Workers errors and sends the relevant stack traces, logs, and traces to coding agents or any webhook for faster investigation.  
[Cut your AI spend with AI Gateway's Auto Router](https://blog.cloudflare.com/auto-router/)| Auto Router classifies each request at the edge and sends it to a suitable model, reducing cost while preserving response quality.  
[Cloudflare Impact reaches $100 million in donations](https://blog.cloudflare.com/100-million-donations/)| Initiatives including Project Galileo, the Athenian Project, and Cloudflare for Campaigns have now delivered more than $100 million in donated services.  
  
### Thursday, October 1 - Bringing more of the developer stack to Cloudflare

We expanded what is possible to achieve on Cloudflare’s platform with the general availability launch of Cloudflare Basin, our data analytics platform, the launch of K2, a durable serverless event stream, and the announcement of our new contest — inviting developers to build a Git platform designed for agentic development.

**What**| **In a sentence…**  
---|---  
[Introducing Cloudflare Basin: an open, serverless data platform, now generally available](https://blog.cloudflare.com/cloudflare-basin/)| Basin is now generally available, giving developers a serverless platform built on Apache Iceberg and R2 for ingesting, managing, and querying large datasets.  
[Support for modern cryptographic algorithms in Workers](https://blog.cloudflare.com/workers-ml-kem-ml-dsa-support/)| Workers adds opt-in native Web Crypto support for ML-KEM and ML-DSA, giving developers post-quantum primitives without bundling their own implementations.  
[AI Search is now generally available](https://blog.cloudflare.com/ai-search-ga/)| AI Search reaches general availability with visual search, OCR for scanned PDFs, larger files, and support for any chat model.  
[We want you to build the next Git platform on Cloudflare](https://blog.cloudflare.com/next-git-platform-on-cloudflare/)| Artifacts enters open beta and a new competition invites developers to build a Git platform designed for the era of AI agents.  
[Announcing Cloudflare K2: serverless event streams](https://blog.cloudflare.com/cloudflare-k2-streams/)| K2 provides durable, ordered event streams on R2, separating producers and consumers without the operational overhead of managing broker clusters.  
[Cloudflare OS: your company's agent workspace, managed for you](https://blog.cloudflare.com/managed-cloudflare-os/)| Cloudflare OS provides an agent workspace connected to an organization’s data and systems, with a waitlist open for fully managed deployments.  
[Introducing Workers KV Instant - powered by Quicksilver](https://blog.cloudflare.com/workers-kv-instant/)| Workers KV Instant delivers sub-two-millisecond p99 reads and fast global replication across more than 300 locations using the familiar Workers KV API.  
[One year later: Sovereign AI and the fight for choice](https://blog.cloudflare.com/sovereign-ai-choice-one-year-later/)| We are expanding local open-source model choice and model-agnostic security tools, so nations can pursue AI sovereignty without isolation.  
[Introducing Clef: our open-source decision models, and new RL fine-tuning platform](https://blog.cloudflare.com/clef-decision-models/)| Clef and Clef-flash are open-source decision models for fast classification and agent workflows, accompanied by a platform for reinforcement-learning fine-tuning.  
  
### Friday, October 2 - Delivering a faster, simpler Internet for everyone

We wrapped up the week with major updates to Cloudflare Observability, alongside adding Cloudflare Traces, network performance improvements that make Cloudflare faster, and an announcement on how we’re supporting civil society organizations.

**What**| **In a sentence…**  
---|---  
[8 major updates to Cloudflare Observability](https://blog.cloudflare.com/one-observability-platform/)| Eight updates bring logs, traces, analytics, alerts, dashboards, querying, and telemetry export into one observability platform with simpler pricing.  
[Introducing Cloudflare Traces: follow requests through our entire platform](https://blog.cloudflare.com/cloudflare-tracing/)| Cloudflare Traces provides request-level visibility across security rules, transformations, cache, Workers, services, and origins without requiring an agent or SDK.  
[Updates on our pledge to make Cloudflare features accessible to everyone](https://blog.cloudflare.com/enterprise-for-all-update/)| One year after our pledge, Logpush, multi-account governance, higher platform limits, and other capabilities are available to more customers across plans.  
[Announcing Cloudflare OHTTP Gateway - expanding access to Cloudflare's privacy-preserving infrastructure](https://blog.cloudflare.com/announcing-cloudflare-ohttp-gateway/)| A self-serve OHTTP Gateway enters closed beta, while Privacy Gateway becomes Cloudflare OHTTP Relay to distinguish the two roles.  
[Follow the thread: a new dashboard to investigate account abuse](https://blog.cloudflare.com/account-abuse-protection-dashboard/)| Account Abuse Protection uses stateful analysis and privacy-preserving Hashed User IDs to help teams investigate credential stuffing and fake-account creation.  
[Protected Quick Tunnels: simple accountless authentication for your next dev project](https://blog.cloudflare.com/protected-quick-tunnels/)| Quick Tunnels now support email authentication, letting developers share a local application with selected people or domains without requiring Cloudflare accounts.  
[Building for good: How civil society organizations are automating on Cloudflare](https://blog.cloudflare.com/civil-society-automation/)| Civil society organizations are using Cloudflare’s developer platform to automate and scale work that protects human rights and the public interest.  
[2026 Birthday week: network performance update](https://blog.cloudflare.com/network-performance-birthday-week-2026/)| Using an expanded real-user measurement methodology, Cloudflare now ranks as the fastest provider across 74% of the top 1,000 networks.  
[Introducing Web Search API via AI Gateway](https://blog.cloudflare.com/introducing-web-search-api/)| AI Gateway’s Web Search API brings current web context from multiple providers into model calls through REST APIs, Workers bindings, or customer-managed keys.  
[Streamline: custom video pipelines with Cloudflare Stream and Workers](https://blog.cloudflare.com/streamline/)| Streamline is an open-source example for building continuous video pipelines by combining Workers, Durable Objects, and a containerized media engine.  
  
### Building the Internet’s next chapter together

Across this week’s announcements, we kept returning to a consistent theme: the Internet should continue to open up more opportunities for people to create, contribute, and succeed. That means open tools developers can shape, security that keeps pace with new threats, a fairer exchange between agents and the people whose work they use, and infrastructure designed for the agentic Internet.

For 16 years, we have been building alongside developers, creators, researchers, customers, partners, and open-source communities. Your ideas, feedback, and willingness to challenge us have shaped Cloudflare, and that collaboration matters now more than ever.

]]>01M45M6M9H2C1A45G0S8EC3KW9One year later: the power of 1.1.1.1 internshttps://blog.cloudflare.com/one-year-later-1111-interns/ Mon, 05 Oct 2026 13:00:00 GMTA year after announcing our goal to hire 1,111 interns, more than 750 early-career builders have shipped real products across 48 teams at Cloudflare. From Birthday Week launches to post-quantum security, our interns prove that AI amplifies human potential instead of replacing it. Kelly RussellAllan LeinwandJudy CheongBirthday WeekInternship ExperienceA year ago, many companies were [cutting intern and new-graduate hiring](https://www.nytimes.com/2025/08/10/technology/coding-ai-jobs-students.html). We went the other way. We [announced](https://blog.cloudflare.com/cloudflare-1111-intern-program/) a goal to hire as many as 1,111 interns in 2026, a number that’s a nod to 1.1.1.1, our public DNS resolver.

The bet was that AI makes early-career talent more valuable and able to make an impact faster. The best AI tools help people learn a system faster, try more ideas, and take on harder problems. They don’t supply the energy, curiosity and fresh eyes a new person brings to a team.

A year in, and our interns are shipping to our internal teams and to millions of customers.

If you’re reading this on the Cloudflare Blog, you’re already using some of their work. The blog runs on [EmDash](https://blog.cloudflare.com/emdash-cms-plugin-registry/), and EmDash’s second maintainer started at Cloudflare as an intern this past summer. 

## A new generation of builders

We’re still working toward 1,111. So far, we’ve hosted 750 internships across 48 teams in nine offices: Austin, San Francisco, London, Lisbon, New York, Singapore, Bengaluru, Washington DC, and Sydney. And we’re still hiring.

From their first day, interns joined active teams and worked on real problems. Each was expected to leave something behind: a shipped product improvement, a better process, a new piece of infrastructure, or an insight that changes how a team approaches its work.

That work reached far beyond engineering. An internal audit intern built an AI-assisted pipeline to automate ISO compliance control testing and documentation. A product manager intern worked on an API, dashboard, and migration tooling to modernize credit management for our Startup Program. A people team software engineering intern improved background-verification workflows for new hires. A customer support intern explored ways to use AI to trigger troubleshooting commands from case descriptions.

## AI-native interns, real-world results

AI was a key theme through the whole program, but it wasn’t a shortcut around learning or accountability. Interns used AI to understand unfamiliar codebases and systems, compare product requirements with implementation, prototype ideas, automate repetitive work, and accelerate the path from a question to a working solution. Managers and mentors remained essential in setting direction, reviewing decisions, and ensuring that what shipped met Cloudflare’s standards.

For many interns, AI moved the starting line. They could map a new project in days instead of weeks, create a working scaffold quickly, and spend more time on the hard questions: What should we build? Who will use it? How do we know it is correct? What happens when it reaches production?

One intern put it more bluntly: “ _How did previous interns ship anything in 12 weeks without AI?_ ”

## Interns ship at Cloudflare

Last year’s announcement had a section with that title. This year, the interns wrote the posts:

**More cache from the same hardware.** RAM and disk prices have climbed sharply over the past year, so our intern Aashi asked whether Cloudflare could get [more cache capacity out of the servers it already has](https://blog.cloudflare.com/cache-transcoding/). Aashi built Cache Transcoding, which compresses eligible assets with Zstandard inside our primary proxy before they’re written to disk. In initial testing, it shrank them to a third of their original on-disk size on average. That points toward petabytes of effective cache capacity and less data moving between our data centers.

**The CMS behind this blog.** Noah joined as an intern and became [EmDash’s](https://blog.cloudflare.com/emdash-cms-plugin-registry/) second maintainer, contributing changes across the media library, content editor, and admin interface. EmDash 1.0 shipped during Birthday Week.

**Getting ready for post-quantum.** Cloudflare is targeting 2029 for post-quantum security, and you can’t migrate what you can’t see. Tiago helped build CryptoLabe, an internal AI tool that [finds cryptography across our codebase](https://blog.cloudflare.com/ai-driven-cryptography-discovery/) and maps what depends on it. Sophie helped bring [per-connection post-quantum visibility](https://blog.cloudflare.com/post-quantum-visibility/) to Logpush, Log Explorer, and HTTP Traffic Analytics, so customers can check their own progress too.

**Fixing the Internet’s plumbing.** Some intern work goes beyond our products. Iliana measured how often networks rewrite BGP’s ORIGIN attribute to pull traffic their way, and found it on [roughly 70% of observed paths](https://blog.cloudflare.com/bgp-origin-attribute/). Then she publicly advocated for taking ORIGIN out of route selection altogether. She also tracked the [adoption of RFC 9234](https://blog.cloudflare.com/rfc9234-bgp-role-model/), which lets routers reject route leaks on their own. Helping build a better Internet includes work like this: measuring a problem no single network owns, publishing the data, and proposing a fix.

Our interns didn't just help with Birthday Week, they shipped impactful work! Several of this year's [Birthday Week](https://www.cloudflare.com/birthday-week/) launches included intern-authored and intern-engineered work:

  * [Protected Quick Tunnels:simple accountless authentication for your next dev project](https://blog.cloudflare.com/protected-quick-tunnels/)
  * [Using AI to chart a course for our post-quantum migration](https://blog.cloudflare.com/ai-driven-cryptography-discovery/)
  * [Is your domain using post-quantum encryption? Now you can see for yourself](https://blog.cloudflare.com/post-quantum-visibility/)
  * [EmDash 1.0: the stable CMS with a secure plugin registry](https://blog.cloudflare.com/emdash-cms-plugin-registry/)
  * [Supporting native Rust in Workers with the new Emscripten target for wasm-bindgen](https://blog.cloudflare.com/rust-workers-emscripten-target/)
  * [How fast is the web? Explore billions of real-user measurements with BEACON](https://blog.cloudflare.com/how-fast-is-the-web/)
  * [Cloudflare Containers, rebuilt to scale agent sandboxes](https://blog.cloudflare.com/faster-agent-sandboxes/)



See more on the [Cloudflare Blog](https://blog.cloudflare.com/tag/internship-experience/).

## Building community together

An internship is also about the people you meet. Across our offices, interns shared meals, volunteered together, and made friends. Our CEO, Matthew Prince, hosted dinners with interns in offices around the world to hear directly about what they were working on and learning.

Executives also joined Q&A sessions where interns could ask candid questions about Cloudflare, strategy, technology, and careers. These sessions complemented the day-to-day support of managers and mentors, and gave interns a view of how the whole company works and where it’s going.

## What comes next

We’ll keep growing the program next year, with a new cohort of interns, more teams taking part, and more learning about how early career people do their best work with AI and with the people around them.

And many of this year’s interns are coming back to Cloudflare full-time. A good summer is nice, but the outcome we want is a career and a new generation of people helping build a better Internet.

If you’re a student or early-career technologist, and you want your first project to ship to millions of people, [apply to our internship program](https://www.cloudflare.com/careers/early-talent/). We’ll keep opening up roles throughout the year.

]]>01M40C00BDZBKANZ5QVXW0AD7X8 major updates to Cloudflare Observabilityhttps://blog.cloudflare.com/one-observability-platform/ Fri, 02 Oct 2026 18:00:00 GMTCloudflare is launching eight major updates that bring logs, traces, analytics, alerts, dashboards, querying, and telemetry export into one observability platform, with simpler and more predictable pricing.Nevi ShahArti KumarTom BennSahidya DevadossBirthday WeekLogsObservabilityProduct NewsTracingWorkersToday, we’re launching eight major updates that bring your logs, traces, analytics, alerts, dashboards, and exporting into [one observability platform](https://developers.cloudflare.com/observability/), with simpler and more predictable pricing.

**Here's what's launching:**

  * One place to explore logs from across Cloudflare
  * End-to-end tracing from Cloudflare's edge to your origin
  * One unified SQL API for querying Cloudflare data
  * One pricing model for observability data ingested and stored across Cloudflare
  * Custom alerts on your observability data
  * All analytics for your domain in one place, with 30 days of data retention
  * Custom dashboards built from your observability data
  * Export your data with Logpush -- now available on self-serve plans



## One observability platform for all of Cloudflare

Understanding an issue often requires data from more than one Cloudflare product. A spike in 5xx responses could come from a Worker, from your origin, or from Cloudflare failing to connect to your origin globally or regionally. But investigating it today requires knowing which product owns each signal and how to query it.

Observability should be a platform-wide capability: it should reflect how applications actually behave and give you the complete context needed to resolve an issue. Over the coming months, you’ll see more Cloudflare products, datasets, and workflows become part of this shared observability platform, with more consistent pricing, product experiences, and features. These eight updates are the first step into a more unified Observability problem.

## 1\. Investigate all your logs in one place

The [new Logs home ](https://developers.cloudflare.com/observability/logs/)combines [Workers Observability](https://developers.cloudflare.com/workers/observability/) (for debugging Workers applications and its connected resources) with [Log Explorer ](https://developers.cloudflare.com/log-explorer/)(for searching across security logs). You can now choose from log datasets like HTTP events, firewall events, Workers, Containers, R2, and AI Gateway, and use the same investigative tools and capabilities for each.

Start with an increase in request latency, group it by hostname or data center, narrow the results to affected paths, and inspect individual requests by Ray ID. If the investigation leads to another Cloudflare product, switch datasets without leaving Logs. Support for querying across multiple datasets is coming soon, making it possible to connect related events across products in a single query.  
  
You can query your logs with raw SQL or with built-in filters to narrow down on specific events. Create visualizations with natural language, and easily investigate and understand detected anomalies.

**Copy prompt**
    
    
    Use cf cli (https://developers.cloudflare.com/cf/) to query my Worker logs/traces using the sql API and tell me about any unusual patterns or trends. If there is nothing unusual, give me a rundown of the past few days of my traffic. If I am not logged in bring me through the auth flow.

## 2\. Trace requests through our **entire** platform — now in open beta

We’re launching [Cloudflare Traces in open beta](http://blog.cloudflare.com/cloudflare-tracing), giving you a request-level view of supported security rules, transformations, cache decisions, routing, Workers, and origin handling. You get to see how your traffic moved through our platform, and connect the dots between how you’ve configured Cloudflare, and how this influences request processing time, routing decisions, and more.

[Set a baseline sampling rate](https://developers.cloudflare.com/observability/traces/configuration/) for continuous visibility, then use [Trace Rules](https://developers.cloudflare.com/observability/traces/configuration/#trace-rules) to capture specific traffic at a higher rate during an investigation. Target hostnames, paths, IP addresses, or headers, search by [Ray ID](https://developers.cloudflare.com/fundamentals/reference/cloudflare-ray-id), and inspect the resulting spans directly in the Cloudflare dashboard.

You can export traces over [OpenTelemetry](https://opentelemetry.io/), while [W3C trace context propagation](https://www.w3.org/TR/trace-context/) lets you accept incoming trace context and pass along context to your origin. Check out the [full blog post to learn more about Cloudflare Tracing](http://blog.cloudflare.com/cloudflare-tracing) or give this command to your agent to get started:

**Copy prompt**
    
    
    Using the Cloudflare cf CLI, configure Tracing for my zone with a 10% sampling rate and persist traces in Cloudflare. If I have multiple zones, ask me which one to use.

## 3\. Have your agent query observability data with one unified SQL API

Agents also need a consistent way to sift through your observability data, investigate issues, correlate signals, and verify fixes. We’re launching [a unified SQL API,](https://developers.cloudflare.com/analytics/sql-api/) now in beta, for querying telemetry across Cloudflare. Instead of integrating separately with Workers logs, Containers security events, HTTP request logs, and analytics data, people and agents can query them using one SQL dialect, authentication model, and API.

Your agent can use the new [Cloudflare CLI](https://blog.cloudflare.com/cloudflare-cf-cli-launch/), `cf`, to find and run queries from the command line or connect through [Cloudflare’s Observability MCP](https://github.com/cloudflare/mcp) server to investigate logs, traces and analytics. [Dataset schemas, fields, and example queries](https://developers.cloudflare.com/analytics/sql-api/datasets/) are available to help both people and agents build queries.

Additionally, we’re also bringing the SQL interface directly into Workers with a [native binding.](https://developers.cloudflare.com/workers/runtime-apis/bindings/analytics-sql/) Your Worker can now do things like query [Analytics Engine ](https://developers.cloudflare.com/analytics/analytics-engine/)data to meter customer usage and power billing workflows, build customer-facing analytics dashboards, generate health reports, or automate incident investigation without configuring a separate API client.

## 4\. New pricing for all ingested and stored logs and traces

For all logs and traces ingested and stored on Cloudflare, we are moving to one unified Observability subscription and pricing. Beginning **December 1, 2026** , this pricing model will apply across all plans (effective upon renewal for all Enterprise customers) and cover existing Developer Platform logs, including Workers, Containers, AI Gateway, as well as all tracing data.

Because logs and traces can vary dramatically in size, the new model is based on the **volume you ingest and store** rather than an event-based count. This pricing adjustment will be. Check out our [documentation ](https://developers.cloudflare.com/observability/pricing/)for more details on pricing.

Plan| Included Usage| Retention| Additional usage  
---|---|---|---  
Free| 0.5 GB of ingestion per day| 7 days| Not available  
Paid and Enterprise| 50 GB of ingestion   
10 GB-month of storage per billing cycle| Up to 1 year   
(coming soon)| $0.25 per GB ingested  
$0.10 per GB-month stored  
  
## 5\. Configure custom alerts on your observability data – now in beta

Notifications ([now called “Alerts”](https://developers.cloudflare.com/notifications/)) just got a major upgrade. You can now define custom alerts directly on anything supported by our new unified SQL API, including HTTP request logs, Workers events, Workers Analytics Engine datasets, analytics datasets, traces, and security events.

Choose a dataset in the dashboard or define the condition using custom SQL. Then select a threshold, anomaly, or SLO, set the evaluation window, and choose where the alert should go. You might alert when origin 5xx responses exceed a threshold for five minutes, a Container repeatedly fails, Worker errors increase after a deployment, or trace latency crosses an expected limit. 

You can send alerts right to tools your teams are already using, including incident management tools, chat platforms, and webhooks. [Webhooks are now available on all plans](https://developers.cloudflare.com/notifications/get-started/configure-webhooks/), allowing you to route alerts to custom services or even your agent to begin investigating immediately. To get started check out our [documentation](https://developers.cloudflare.com/notifications/) or give this command to your agent:

**Copy prompt**
    
    
    Use cf cli (https://developers.cloudflare.com/cf/) to query my HTTP and Worker analytics using the sql API. Then setup an alert to alert me on bad state (high 5xx, high exception rate, anomalous TTFB/wall time, etc.)
    
    If I am not logged into cf cli bring me through the auth flow.
    

## 6\. See your domain analytics in one place — now with 30 days retention

Understanding what is happening on your domain has often meant piecing together metrics from different Cloudflare products. We’re bringing traffic, performance, security, cache, origin, and DNS data together so you can see how they relate. If latency increases, you can quickly see whether it is tied to a specific Cloudflare data center, hostname, or origin.

In addition, you now get [30 days of domain analytics on every plan.](https://developers.cloudflare.com/analytics/account-and-zone-analytics/zone-analytics/) A full month of history gives you time to investigate issues after they happen, compare today with the same day in previous weeks, and tell the difference between a one-time spike and a longer trend.

## 7\. Build custom dashboards

Prebuilt dashboards cover common use cases, but applications often use several parts of Cloudflare. With [Custom Dashboards](https://developers.cloudflare.com/analytics/custom-dashboards/), you can bring together analytics from across Cloudflare, logs and traces from the Workers platform, and security events in one view. Track request volume, errors, latency, storage, and blocked traffic, then share the dashboard with your team. Instead of rebuilding queries during every investigation, you have one place to monitor the signals that matter to your application.

## 8\. Logpush is now available on all self-serve plans

[Logpush](https://developers.cloudflare.com/logs/logpush/), previously available only to Enterprise, is now available on all self-serve plans, letting you export all Cloudflare logs to the tools and destinations you already use. Need to apply filters, perform redaction, enrich events or reshape output before delivery? [Transformers](https://developers.cloudflare.com/logs/logpush/transformers/) is now generally available, letting you apply any SQL transformation without operating a separate ETL pipeline.   
  
We’re introducing [usage-based pricing](https://developers.cloudflare.com/changelog/post/2026-09-30-logpush-usage-based-pricing/) for Logpush and Transformers. Each includes a free monthly allowance, with simple pricing for additional usage:

Export usage| Included each month| Additional usage  
---|---|---  
Exports to Cloudflare destinations| 25 GB| $0.03 per GB  
Exports to external destinations| 25 GB| $0.10 per GB  
Logpush Transformers| 1 GB| $0.04 per GB  
  
Visit the [documentation](https://developers.cloudflare.com/logs/logpush/) to get started with Logpush and explore complete pricing details.

**Copy prompt**
    
    
    Use cf CLI (https://developers.cloudflare.com/cf/) to set up a Logpush job that sends my Worker logs/traces to an existing R2 bucket.
    Check for existing R2 buckets and Logpush jobs first to avoid duplicates. If multiple buckets exist, ask me which one to use. If none exist, guide me through creating one and setting up the required credentials.
    If I am not logged in, bring me through the authentication flow. Confirm with me before creating or modifying resources, and verify the Logpush job afterward. Never expose credentials or secrets.
    

## What's coming up:

  * **Longer retention for your observability data:** You’ll be able to retain logging and tracing data for up to one year, making it easier to investigate recurring issues, compare historical behavior, and analyze long-term trends.
  * **OpenTelemetry API support in Workers:** We’ll continue building out our OpenTelemetry APIs to enable adding attributes to existing spans or getting trace context.
  * **Easier metrics export with OpenTelemetry:** You’ll be able to send Cloudflare metrics to OpenTelemetry-compatible destinations and analyze them alongside telemetry from the rest of your stack.
  * **New pricing takes effect December 1, 2026:** If you ingest or store observability data on Cloudflare, the unified pricing plan will apply to your usage. We’ll notify you before the change takes effect.



## Ready to start investigating?

We hear you when you say Cloudflare can feel like a black box. These updates are just the beginning of exposing what’s happening, making the underlying data accessible, and giving you the context that you need to act. That transparency matters even more as agents move from writing software to operating it. An agent can only close the loop between a change and its outcome if it can query what happened, identify the failure, and verify the fix.

By building around [OpenTelemetry](https://opentelemetry.io/), [W3C Trace Context,](https://www.w3.org/TR/trace-context/) and SQL, we are committed to giving you and your agents standard, portable interfaces to that context. Check out our new [Observability documentation ](https://developers.cloudflare.com/observability/)home to learn more.

]]>01M3XHCB64KZ1NTN3N83GY590BStreamline: custom video pipelines with Cloudflare Stream and Workershttps://blog.cloudflare.com/streamline/ Fri, 02 Oct 2026 16:13:45 GMTStreamline demonstrates how to build long-running, continuous video processing pipelines by pairing Cloudflare Workers and Durable Objects with a containerized media engine.Willi GeigerTaylor SmithBirthday WeekCloudflare StreamContainersDeveloper PlatformDurable ObjectsWorkersCloudflare Stream is [a powerful broadcasting platform](https://www.cloudflare.com/products/stream/) that, for many of our customers, just works. But what if you wanted to render dynamic annotations on a livestream or create an alternate version of a hosted video with burned-in subtitles? You would need to run a custom video pipeline.

Today, we’re releasing a new developer playground, Streamline, that demonstrates how you can build a system to deliver these bespoke video experiences on Cloudflare’s Developer Platform. We’ll walk you through how Streamline leverages Workers, Containers, and several media protocols to modify video — and immediately publish that output as livestream or new hosted video. You’ll also have the opportunity to try it for your projects.

A processing pipeline needs a durable, long-running environment that can run specialized, compiled code with predictable memory and CPU capacity. Video streams can run for minutes or hours, so the media process needs a lifecycle independent of the request that started it. An application should be able to start a pipeline, send its input, inspect it, and stop it without needing to keep a single request open for the entire duration.

Cloudflare provides the primitives we need. Containers are long-lived runtimes suitable for media processing. Durable Objects help with orchestration. Finally, Workers are perfect for control signaling and monitoring.

For Streamline, we built a media engine running in a Container to handle media processing in real-time. The Container is controlled by a Worker exposing control, preview, and testing to an agent or user. Processing will continue even if the Worker disconnects. We've architected Streamline with modular components so that the media engine could be replaced with dedicated encoding products in the future.

## **Architecture**

A Streamline deployment consists of two components: the **Media Engine** , which handles media input/output and processing, and a controlling **Application** , which creates, configures, observes, and stops media sessions.

**Media Engine**

The Media Engine has two components:

  * **Controller.** This is a control harness written in Go that implements an HTTP server, receives incoming requests, and translates them into operations that can be executed by the media engine.
  * **Processor** that performs the actual media processing. The current implementation uses FFmpeg, but that is an internal implementation detail rather than part of the user-facing API.



The Media Engine is hosted in a Container, and handles all media input/output as well as processing. It can pull RTMPS playback over the network from one Stream Live input and publish RTMPS output to another Stream Live input. It can pull a Cloudflare Stream HLS manifest and its segments to use hosted videos as input. It can accept video input from a source supplied by the controlling application, for example a webcam. It can publish preview video over an outbound WebSocket to a Durable Object relay. An application that needs preview can connect to that relay through its own WebSocket.

### **Application**

The application is built using Workers, and can be a full-stack browser application, an agent, or an embedded system. It consists of:

  * **User interface (UI)** including client logic, identity and access policy. This post uses a browser application as its concrete example, so it also includes a browser interface.
  * **Orchestrator** coordinates the session, the Container lifecycle, and preview relay. The orchestrator is implemented by a Durable Object.



It is possible to run the system locally during development, in which case the container is just a local Docker instance and the Durable Object is not used: there is a single user, the controlling application does not require authorization for local access, and the video preview can connect directly to a WebSocket on localhost.

When these components are deployed to Cloudflare, an authorized user or agent can visit the Worker to start a new session. This spins up a new Streamline container if needed, manages its lifecycle automatically, exposes an API to perform a number of video manipulation operations, and routes inputs from and outputs back to Cloudflare Stream.

Time for a technical deep dive on how the system works.

## **Container lifecycle and session management**

The controlling Worker application initiates a long-running media processing session. After starting the session, the application can disconnect and reconnect safely, while the Container continues processing until the controlling application stops it. We also include a maximum duration to ensure a session is always eventually closed down and can’t run indefinitely, even without external control. While a media processing session is running, the container instance is unavailable for other applications to use.

A Cloudflare Container will automatically sleep if it has not received any incoming requests since a defined interval. However, in our case, once the pipeline is running, it must continue even if the controlling application disconnects and it receives no requests. We can implement this behavior by overriding the `onActivityExpired()` callback on the container. If the expiry time has not been reached, then we renew the activity, otherwise we destroy the container.

## **API**

The HTTP server implemented by the Go harness and the Durable Object associated with the Container together define the low-level interface to the system. However, we wanted to provide an abstraction over this, so the system is as agnostic as possible to who or what is controlling the session and any unnecessary details of the backend implementation.

We implement this by exporting two packages from Streamline:

  * `@cloudflare/streamline/client` Defines a high-level, session-based API.
  * `@cloudflare/streamline/` Exposes the Durable Object base class associated with the container. This routes the API requests, implements the preview relay server described below, and provides hooks for security and access policy.



In a remote deployment, the controlling Worker is expected to import `@streamline/cloudflare` and define a concrete subclass of the Durable Object exposed by the container that can be used for application-specific logic and storage.

In local mode, where there is no Durable Object, the frontend defines a thin adapter layer that maintains the session-based API, but connects directly to the local Docker instance with no access controls, etc.

The example below shows how the controlling application can use the API to access Streamline, prepare a session, and start a video processing pipeline.

`config` is a JSON object that defines the processing pipeline to be executed, described more in subsequent sections.

The table below shows the complete list of all API calls.

Client method| Function  
---|---  
`createStreamline()`| Creates a new Streamline instance.  
`streamline.sessions.create()`| Creates a new processing session.  
`streamline.sessions.resume(id)`| Reconnects to an existing session.  
`session.start(config)`| Starts a new processing pipeline.  
`session.ingest(chunk)`| Sends a chunk of video data in “webcam” mode.  
`session.annotation(png)`| Updates the transparent annotation overlay.  
`session.metrics()`| Receives metrics about the current session.  
`session.stop()`| Stops the processing in the current session.  
  
## **Defining and running a video processing pipeline**

`session.start()` constructs and runs a processing pipeline. It takes a single argument which is a JSON configuration object defining the processing to be performed:

  * Input(s)
  * Operations
  * Output



The example below starts a pipeline that takes an RTMP (real-time messaging protocol) broadcast as input (for example, a feed of a Stream Live input receiving an inbound livestream), applies an overlay image with transparency, and sends the output to an RTMP destination (for example, to another Stream Live input for recording or broadcast). This allows the Worker application to create a modified version of a livestream in real time.

## **Video-on-demand input via HLS**

Streamline can also ingest streaming video input via HLS (HTTP live streaming), for example a video hosted on Cloudflare Stream. The example below shows how a Worker application could run a pipeline that ingests a Stream video, reads the embedded closed caption subtitles and renders them as text on the video, and sends the output via RTMP, for example to a Stream Live Input for broadcasting or recording of the modified version.

## **Sending video to Streamline**

It’s often useful to be able to quickly preview a processing pipeline by sending video data directly to Streamline, for example from a webcam. An agent or embedded device application may also want to use this capability, for example to send footage from factory cameras for AI analysis, or to combine multiple camera feeds into a composite view.

The example below creates a pipeline that expects input from the Worker application and produces a preview video output available over a WebSocket (we’ll talk more about the WebSocket preview video below). It applies two filters and an “annotation,” which is an overlay specified as a PNG image that can be updated while the processing is running, for example to implement an animated graphic.

The code snippet above just starts the pipeline. The controlling Worker is not sending any media to Streamline yet. We’ll discuss the `openViewer()` function below.

The Worker application sends video data to Streamline using the `session.ingest()` call. The example below shows how a web browser application might receive chunks from the webcam and forward them to Streamline.

## **Animated overlay**

The annotation overlay can be updated using the `session.annotation()` call. The example below shows how the Worker application could snapshot a canvas and send it to Streamline. This could be done on an animation loop, although the update rate may be limited in practice by the size of the PNG overlay images, the available bandwidth, and processing power.

## **Receiving preview video from Streamline**

Streamline can also produce preview video output, by specifying `output: { mode: 'websocket' }`.

Streamline uses WebSockets for low-latency preview video delivery back to the controlling application: the container publishes fMP4 fragments to the Durable Object, which forwards them to an output relay available over a WebSocket on the URL `/relay/view`, relative to the application origin. The application must connect a WebSocket to this URL, and will then receive video data pushed to it as it becomes available from Streamline. The code snippet below shows how a web browser application might display the preview video feed.

A production MediaSource player must queue fragments while SourceBuffer.updating is true. In local development, the browser or other controlling application simply opens a WebSocket connection directly on the local container.

## **Currently supported operations**

In the configuration object passed to `session.start()` in the examples above, `pipeline` is an array of operations from the set supported by the underlying media engine. The operation order is currently fixed by the engine; the order specified in the array is not significant. The list of currently supported operations and the order in which they are applied is below.

Operation name| Function  
---|---  
`filter`| Applies filtering operations, e.g. blur, saturation.  
`overlay`| Overlays an image referenced by URL or a binary PNG specified separately in a call to `annotation()`.  
`subtitle`| Burns in subtitles.  
`encode`| Specifies output encoding parameters.  
  
## **Security**

This is Cloudflare, so it is important that security is part of the design rather than an addition at the end. We need to ensure that only authorized users can create a new session or take control of an existing one, and that sessions are isolated from each other. We must treat Stream RTMPS input/output keys as secrets that shouldn’t be leaked to the controlling application. We must ensure that resource use is bounded.

The owner deployment is kept private using Workers’ [Access integration](https://developers.cloudflare.com/workers/configuration/cloudflare-access/). The configured owner identity and other allowed users can edit the same shared profiles and start a session while the singleton is idle. The Worker verifies the Access session before accepting control requests and binds the active session to the verified principal. Only one session can run at a time, and a different principal cannot stop or replace the active session.

Stream Live Input keys are stored in Worker secrets or as write-only shared overrides in Durable Object storage. They are never returned by the settings API or placed in browser storage. The controlling application specifies RTMPS input and output by referring to a named profile. The Worker resolves the profile before contacting the container.

The preview video stream has two credentials with separate purposes. A Cloudflare Access service token authenticates the container workload to the publisher endpoint. A random per-session capability authorizes publishing only for the currently active relay. The service token is injected by the container's outbound Worker and never enters container memory. The initial deployment uses a temporary path-specific Access Bypass while the per-session capability remains enforced; after deployment and a successful smoke test, the rollout replaces Bypass with Service Auth.

The owner deployment is intentionally private and singleton-routed. It is not the security model for a public multi-user service.

## **Playground and open source**

We want you to try out Streamline and start building! So together with this post, we are releasing the system as open source and deploying a public playground.

The Streamline container can be run locally or deployed on your account. It exports the Worker API for your control application to use.

There is also an example Worker application with an Astro web frontend that demonstrates Streamline functionality with a few common use cases, including overlays, subtitle decoding, filters and picture-in-picture. There is probe functionality that provides performance metrics and system tracing, and can be useful for debugging the system when developing new features. The example application can be run on a local Astro server, or is set up to be deployed behind Cloudflare Access, so you can control who has access to your Streamline instance.

Both repositories are available as open source on Cloudflare’s GitHub:

  * <https://github.com/cloudflare/streamline> \- Media engine, and package exports for applications.
  * <https://github.com/cloudflare/streamline-demo> \- Example application Worker, Astro frontend, deployment profiles, and Access tooling.



We have published a public playground deployment of the example application. This is also something a user can deploy if desired. It uses its own Access configuration, one container identity per verified user, one active session per user, global admission control, concurrency, media and session limits, and no ability for one user to replace another user's session.

You can try the public playground at:

  * <https://playground.streamline-video.workers.dev>



## **Where we go from here**

Streamline demonstrates one way to combine existing managed services, like Stream, with lower-level primitives to build highly customizable media pipelines. In this iteration, Streamline uses Container CPU for media processing, which introduces a bottleneck at higher qualities or frame-rates.

Moving forward, we’re excited to see how we and our developer community can extend this architecture to build new support for computer vision pipelines, hardware-accelerated media processing, realtime experiences with next generation protocols like WebRTC and MoQ, and ultimately video encoding and decoding primitives natively in Workers.

Today, we invite you to check out our hosted demo of Streamline to see how powerful these tools can be. From there, check out the codebases we’ve open sourced to see how easy it is to deploy Streamline into your own account and use it to create your own experiences.

]]>01M3XKBJCTDTMBBCNNHA141F04Introducing Web Search API via AI Gatewayhttps://blog.cloudflare.com/introducing-web-search-api/ Fri, 02 Oct 2026 13:28:10 GMTCloudflare AI Gateway now supports native web search API integration in partnership with Ceramic.ai, Exa, and Linkup. Developers can now inject real-time web context into model inference calls via AI Gateway, REST APIs, or Workers bindings.Michelle ChenSam ElseGabriel MassadasAIAI GatewayBirthday WeekDeveloper PlatformFun fact: when you use an agent and it needs to fetch a live web page, the agent usually just guesses the URL of the page and then makes a tool call to curl it. This is why you’ll sometimes see web fetches come back with a 404 Not Found, which happens if the agent incorrectly guesses the URL of that information. As you can imagine, it’s not super efficient to randomly guess URLs all the time.

There is a better way. What if your agent can actually browse the Internet, just like how humans start with a search engine query when we’re looking for information? This is what web search is designed to do — it enables agents to search for relevant data on the Internet and grounds an agent’s responses based on live information.

Today, we’re announcing Cloudflare’s partnership with web search providers to bring you grounded intelligence via AI Gateway. We’re kicking off this launch with our partners from Ceramic.ai, Exa, and Linkup.

## What can I do with the Web Search API?

AI models are only as good as the context you feed them. Models are typically trained and then frozen at a point in time, operating only on information that existed before their knowledge cut off date. This makes it quite hard to engage with models about recent events, changing APIs, or fast-evolving news.

Integrating Web Search API directly into your inference pipeline equips your agents with a dynamic context layer. Your applications get fresh, structured snippets from the web injected straight into context, which gives your models access to live information.

For example, if your agent was building with Cloudflare developer tools, it might miss all the new products and features we’re releasing during this [Birthday Week](https://www.cloudflare.com/birthday-week/)! With web search, you’ll be able to retrieve the latest and greatest documentation and releases, so you can build faster and smarter.

## Elevating the industry standard for web search

At Cloudflare, we believe that crawlers should be honest, transparent, and respect all bot rules and preferences, and that site owners should have meaningful transparency and control over how their content is used. With our launch today, we’re excited to announce that our partners have committed to meeting Cloudflare’s bot crawling standards.  
  
The crawler used by the web search provider must comply with Cloudflare’s publicly stated requirements for “Verified bots” as [defined in our developer documentation](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/), and web search responses must include a link to the location of crawled content. These rules are net-positive for a fair Internet, and allow creators to decide what they want to do with their data.

We’re extremely excited to be taking another step in setting the bar for what it means to be a good crawler on the Internet, and even more proud of the web search partners who have risen to the challenge to uphold these standards with us. When you use web search on Cloudflare, you choose to consume search knowledge from operators committed to providing the transparency, control, and visibility that helps build a better Internet, by identifying their crawlers, respecting robots.txt, and providing the source of search results.

## Using Web Search API via AI Gateway

Cloudflare’s AI Gateway is the flagship integration point for our new Web Search API product. AI Gateway is designed to be the control plane for your applications, with observability, unified billing, security, and access controls all built-in. Naturally, we thought web search would fit right in: you can consume web search with your AI Gateway credits; collect logs and request data on web search calls; and control who gets access to what web search providers.

Requests show up in your normal AI Gateway observability logs, and web search queries draw down from your AI Gateway credit balance. We will identify partners supporting Zero Data Retention (ZDR), so that you know that your data is not retained. We also offer web search directly at list API pricing from our partners, without any additional markup. More details can be found on the [web search developer docs](https://developers.cloudflare.com/web-search).

We also support Bring-Your-Own-Key (BYOK) with web search providers, as we do with model inference providers. This way, you’re able to bring your existing organizational setup and get started with AI Gateway and web search in a few simple steps.

#### Direct REST API

If you’re making HTTP calls from an existing backend, mobile app, or external service, you can query web search directly through a standard REST endpoint. Simply pass your AI Gateway authentication token, specify your preferred provider in the payload, and it will return web search results.

#### Workers Bindings

For developers building directly on Cloudflare Workers, integration takes just a line of code. We also have a standalone worker binding that you can use to do web search for your agent:

#### Coming soon: Server tools

We are actively building native Server Tools directly into AI Gateway. Soon, you won’t need to define tools yourself: they will come built into our control plane so you can spend more time building rather than orchestrating the harness. Web search will be one of the first tools we incorporate into our stack of server tools, and we’re excited for you to try it.

However, if you’d like to orchestrate web search as a server tool yourself today, you can easily do so with the following Worker code snippet:

## Try it out today!

We’re excited to bring web search to our platform and to be doing this with wonderful partners who are championing what it means to be a good steward of the Internet. Please give our new web search tools a try via AI Gateway, the standalone REST API, and other formats in the future. Get started with our [developer docs](https://developers.cloudflare.com/web-search) today, or try it out on the [AI Playground](https://playground.ai.cloudflare.com/) with your AI Gateway account and key.

]]>01M3XM9KVCRB6JKE07Q88EPGD2Introducing Cloudflare Traces: follow requests through our entire platformhttps://blog.cloudflare.com/cloudflare-tracing/ Fri, 02 Oct 2026 13:00:00 GMTCloudflare Traces shows how a request moves through security rules, transformations, cache, routing, Workers, and your origin, then follows it across services running anywhere in your stack.Mar WitekDan LapidNevi ShahDaniel WalshBirthday WeekDeveloper PlatformObservabilityTracingWorkersToday, we’re introducing [Cloudflare Traces](https://developers.cloudflare.com/observability/traces/) in open beta, extending [automatic tracing beyond Workers](https://blog.cloudflare.com/workers-tracing-now-in-open-beta/) to the rest of the request path. In one trace, you can see supported security rules, transformations, cache decisions, routing, Worker execution, and origin handling, then continue that trace through services running on Cloudflare, at your origin, or elsewhere in your stack. This is a long-term investment in [OpenTelemetry](https://opentelemetry.io/) and in making Cloudflare the most observable part of your stack.

You can now:

  * **[Automatically trace requests across Cloudflare](https://developers.cloudflare.com/observability/traces/spans/): **Capture supported platform operations in one request-level timeline, no additional set up required.
  * **Control which requests are traced** : Set a baseline sampling rate, then use [Trace Rules](https://developers.cloudflare.com/observability/traces/configuration/#trace-rules) to override it for matching traffic.
  * **End-to-end trace context propagation:** Accept and forward [W3C traceparent headers](https://www.w3.org/TR/trace-context-1/#traceparent-header)
  * **[Investigate traces in Cloudflare](https://developers.cloudflare.com/observability/traces/#inspect-a-trace): **View request timelines and span details directly in the Cloudflare dashboard.
  * **[Export traces with OpenTelemetry](https://developers.cloudflare.com/observability/export/opentelemetry/#enable-export-for-cloudflare-traces):** Send your spans to any destination with a compatible Open Telemetry Protocol (OTLP) [endpoint](https://opentelemetry.io/docs/specs/otlp/).



You can [enable tracing in the Cloudflare dashboard](https://developers.cloudflare.com/observability/traces/#enable-tracing) on any domain or let your agent set up for you:

**Copy prompt**
    
    
    Using the Cloudflare cf CLI, configure Tracing for my zone with a 10% sampling rate and persist traces in Cloudflare. If I have multiple zones, ask me which one to use.

## Giving you the visibility we use to debug Cloudflare

When our own teams investigate, we use our own internal traces, which often include thousands of spans for a single trace, generated by dozens of services and features. This lets us dig deep into every detail of a given request. We don’t think that visibility should stop at our internal systems.   
  
[Workers Tracing](https://blog.cloudflare.com/workers-tracing-now-in-open-beta/) was our first step toward exposing what happens on our platform. Last year, we launched automatic instrumentation for Worker invocations, including [outbound fetches and calls to KV, R2, D1, Durable Objects, and other Workers](https://developers.cloudflare.com/workers/observability/traces/spans-and-attributes/). It shows the work performed inside the Workers runtime without requiring tracing code for every operation.

The goal of Cloudflare Traces is to bring the same level of visibility to **everyone** using Cloudflare, whether you’re building on Cloudflare or just have Cloudflare in front of an origin. You get to see how your traffic moved through our platform, and connect the dots between how you’ve configured Cloudflare, and how this influences request processing time, routing decisions, and more. 

## Follow one request end to end

A request’s path through Cloudflare can be complicated! It might pass through security rules, transformations, routing, caching, or proxied to another service entirely. Cloudflare Traces [records each supported step as a span](https://developers.cloudflare.com/observability/traces/spans/), including its timing, outcome, and relevant attributes. Instead of reconstructing the request from separate logs and configuration, you can see the request’s path through our system in one place.

You can answer questions like:

### Why was the request blocked or challenged, and which security rule took action?

See when [custom or managed rules](https://developers.cloudflare.com/observability/traces/spans/#ruleset-phase-spans) evaluated the request, how long evaluation took, and the resulting action. Identify the rule responsible for a block or challenge through its span events.

### Was the URL rewritten by a Transform Rule before it reached the application?

You can open the `http_request_transform` span to see each change, the request component it affected, and the rule responsible. You can also see where the transformation occurred relative to routing and origin handling.

### Which Page Rules, Snippets, or Workers handled or changed the request?

The `workers_routing` span shows whether a route matched, which routing type was used, and the matching route pattern.

### Was the response served from cache, and where was time spent between Cloudflare, the origin connection, and the application?

You can expand nested cache, upstream, and origin spans to see where the request spent its time. Here, you can see there was a cache miss that went to origin and spent 527ms of the 539ms getting a response.

## Configure your tracing

There is no special instrumentation, config, or plugins required. Once tracing is enabled for a domain, Cloudflare generates these spans automatically. This lets you extend the trace through third-party services and back again by adhering to [open standards](https://www.w3.org/TR/trace-context-1/#traceparent-header). From there, you can control which requests are traced using a baseline sampling rate and [Trace Rules](https://developers.cloudflare.com/observability/traces/configuration/#trace-rules).

### Set a baseline sampling rate

You can enable tracing on any domain and [set a baseline sampling rate](https://developers.cloudflare.com/observability/traces/configuration/#head-sampling) to balance visibility, data volume, and cost. You might trace 1% of requests during normal operation, giving you a continuous view of request behavior without collecting a trace for every request.

### Configure Trace Rules

[Trace Rules](https://developers.cloudflare.com/observability/traces/configuration/#trace-rules) let you keep a low baseline sampling rate while capturing complete traces for a specific investigation. If one customer reports a problem, you can trace 100% of traffic for their hostname, source IP, or identifying request header while leaving everyone else at 1%. Or during an investigation, you could trace 100% of requests carrying a temporary debug header, while leaving all other traffic at the baseline. This lets you reproduce an issue without increasing tracing across the entire domain.

Trace Rules use the same [Cloudflare Rules language](https://developers.cloudflare.com/ruleset-engine/rules-language/), so you can target paths, methods, headers, IP addresses, geographies, or combinations of those properties.

### Accept and propagate trace context

One of the most common requests we hear is for true distributed tracing: a single trace that follows a request into Cloudflare, through our platform, and onward through the rest of your stack.

Cloudflare Traces can accept a [W3C traceparent header](https://www.w3.org/TR/trace-context-1/#traceparent-header) from an incoming request, allowing Cloudflare spans to join a trace that began before the request reached our platform. An [incoming propagation policy](https://developers.cloudflare.com/observability/traces/configuration/#incoming-trace-context) controls whether Cloudflare accepts that context.

Cloudflare can also [forward a new traceparent header to your origin](https://developers.cloudflare.com/observability/traces/configuration/#forward-context-to-your-origin). Any other instrumented services can extract that context and continue the trace through APIs, databases, and services running on Cloudflare or elsewhere. To view everything as one connected trace, you can send both Cloudflare and application spans to the same OpenTelemetry-compatible backend.

## Export traces to your observability platform

You can export Cloudflare spans over [OTLP](https://opentelemetry.io/docs/specs/otlp/) to a compatible observability platform, where they appear alongside telemetry from the rest of your stack. [Configure an account-level destination](https://developers.cloudflare.com/observability/export/opentelemetry/#create-a-destination), then choose which domains send traces to it. This is part of our commitment to [OpenTelemetry](https://opentelemetry.io/docs/what-is-opentelemetry/): Cloudflare represents request activity as OpenTelemetry spans and delivers them using OTLP, keeping the data portable across observability tools.

## Let your agent investigate Cloudflare Traces

When you ask a coding agent to debug a production issue, it might inspect your code and run tests, but it may not be able to see what happened to the request in production. With the [Cloudflare Observability MCP server](https://github.com/cloudflare/mcp), your agent can leverage our [SQL API](https://developers.cloudflare.com/analytics/sql-api/) to query your traces (and all of your [observability data](http://blog.cloudflare.com/one-observability-platform)!), giving it access to your investigation production telemetry.

Let your agent find the right requests, comparing failed traces with successful ones, and identifying where their spans diverge. Since the agent can also inspect your repository, it can connect those findings to the relevant code, narrow down what needs to change, and help put up a fix for you to review.

## Pricing

Cloudflare Traces will be a part of the [unified Cloudflare Observability pricing model](https://developers.cloudflare.com/observability/pricing/). Instead of charging by the number of spans/events, pricing is based on how much observability data you ingest and how long you retain it. New pricing will take effect across Cloudflare Tracing (and Workers Tracing!) starting December 1, 2026.

Plan| Included Usage| Retention| Additional Usage  
---|---|---|---  
Free| 0.5 GB of ingestion per day| 7 Days| Not available  
Paid and Enterprise| 50 GB of ingestion   
10 GB-month of storage per billing cycle| Up to 1 year   
(coming soon)| $0.25 per GB ingested  
$0.10 per GB-month stored  
  
## What's next

Following the open beta, we plan to launch:

  * **Broader automatic instrumentation:** Add more spans across both the HTTP request path (e.g. [DDoS rules](https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/), [Access](https://developers.cloudflare.com/cloudflare-one/access-controls/)) and the Workers execution path (e.g. Workflows, Queues, Pipelines).
  * **Authenticated context propagation:** Let trusted callers continue an existing trace without accepting context from every incoming request.
  * **Ad hoc tracing:** Capture a specific request on demand without changing the baseline sampling rate.
  * **OpenTelemetry API support in Workers:** [Continue building out our OpenTelemetry APIs](https://developers.cloudflare.com/workers/observability/traces/custom-spans/) to enable adding attributes to existing spans or getting trace context.
  * **Longer retention:** Keep trace data available for up to 365 days for longer-running investigations.



## Get started

Follow the [Cloudflare Traces documentation](https://developers.cloudflare.com/observability/traces/) to trace your first request and tune sampling with Trace Rules. Cloudflare Traces is available in open beta from the dashboard, through the API, or with Terraform, with support for exporting to an OTLP destination.

]]>01M3XE7G2V6JJXPKX92B1D4080Updates on our pledge to make Cloudflare features accessible to everyonehttps://blog.cloudflare.com/enterprise-for-all-update/ Fri, 02 Oct 2026 13:00:00 GMTA year after pledging to eliminate two-tier product access, Cloudflare has expanded Logpush, multi-account governance, and higher platform limits to all accounts. Here is an update on our progress, how we dogfood these tools internally, and what is coming next.Oliver RoupJustin HutchingsChase CatelliBirthday WeekDevelopersProduct NewsTerraformA year ago, Cloudflare CTO Dane Knecht announced our intention to make [every Cloudflare feature available to everyone](https://blog.cloudflare.com/enterprise-grade-features-for-all/). Cloudflare launched an Enterprise tier years ago when larger customers came to us looking for procurement options beyond a credit card, like invoices, custom contracts, and dedicated support. Those offerings met a customer need but over time, a two-tier system developed where some of our most advanced and powerful features were only available to Enterprise customers. Our goal was to close that gap.

Today, teams of every size use Cloudflare, from Fortune 100 enterprises to small businesses, open-source projects, and individuals. Across the platform, we’re committed to ensuring that every user or team can make use of all of Cloudflare’s capabilities in a way that helps their organization thrive.

The underlying philosophy is that Cloudflare should offer products suitable for our most demanding customers — and make those capabilities available to everyone. Large or small, every customer would prefer not to have to call support. Building products that are easy to buy, configure, and consume means more of our products in use and a step closer to a better Internet for everybody.

Every generally available (GA) feature we launched this week that is available on an Enterprise plan is also available to Pay-as-you-go customers, and most are available on the free tier. Where our plans differ, it's in how much you can use, not what you can use. While we haven’t yet met our goal that every feature be available to everyone, in the year since Dane’s announcement, we’ve made great progress.

Here are a few products and features making the transition today from Enterprise to everyone.

## Logpush and Logpush Transformers now available to all plans

Flexibility on pushing logs to third parties and how logs are formatted expanded this week from Enterprise-only to all customers.

[Logpush](https://developers.cloudflare.com/logs/logpush/) delivers Cloudflare logs to storage, security, and analytics destinations, helping customers monitor traffic, investigate issues, and analyze their data using existing tools. Previously available only to Enterprise customers, Logpush is now available to Free, Pro, and Business customers through self-service, pay-as-you-go pricing. Datasets available to Logpush have been expanding as well. We’ve recently added account-scoped firewall events, WebSocket analytics and per-zone post-quantum visibility.

[Transformers](https://developers.cloudflare.com/logs/logpush/transformers/) is also becoming generally available to all customers. With Transformers, customers can use SQL to filter unnecessary records, redact sensitive information, enrich events, and reformat logs before delivery without operating a separate extraction, transformation and loading (ETL) pipeline. Together, Logpush and Transformers give every customer greater control over how their Cloudflare data is prepared and delivered.

In addition, [Custom Dashboards](https://developers.cloudflare.com/changelog/post/2026-04-22-custom-dashboards-ga/) which let customers create personalized views highlighting the metrics most critical to them, is now available to all customers.

## New tools for managing Cloudflare at scale

### Expanding RBAC

Over the last year, we’ve dramatically expanded the availability of Role-Based Access Control (RBAC) across all Cloudflare products and for all customers. Today, nearly all products have RBAC roles available at the account and zone level. Recently, Workers joined R2 and Access in having RBAC roles available at the individual resource level as well, so Administrators can decide who on their team gets specific access to individual Workers.

### Multiple Accounts

While fine-grained RBAC lets customers manage subsets of an account, this setup still relies on a small number of super administrators making choices about who gets access to what. Centralized authority works great when your problem space is small, but as the number of teams and projects being managed on Cloudflare grows, it can turn into an organizational bottleneck.

The single account model is excellent in its simplicity, but it can start to feel a little crowded for customers maintaining hundreds or thousands of zones, workers, and storage products. That’s why we’ve been expanding our capabilities around managing multiple accounts.

#### New Account button

Last month, we quietly [launched](https://developers.cloudflare.com/changelog/post/2026-08-04-free-dashboard-button/) the **New Account** button on the dashboard that, for the first time, lets users create additional accounts directly. The response has been overwhelmingly positive, and we’re seeing thousands of customers branching out into additional accounts every week. When you use this button, it creates a new, free, Cloudflare account that you can use to segment your open source projects, or segment the work of multiple teams in your organization. Each of these accounts is independently billed, so you can segment spending across multiple cost-centers directly. Safeguards are in place to prevent fraud and abuse.

#### New Accounts for Enterprises

While the New Account button is for everyone, for the time being, we recommend that Enterprise customers reach out to their account team to get new accounts provisioned instead. This lets you reuse your existing enterprise agreement and subscriptions across all of your accounts. There is no preset limit on how many accounts an enterprise can request. We will be adding additional features in the future that make this process self-serve for enterprises too.

### Organizations

Once you’ve created multiple accounts, how do you organize and track them all? [Organizations](https://blog.cloudflare.com/organizations-beta/) allow customers to group accounts together with a single analytics and shared configuration surface. It’s in beta for Enterprise customers now, will be GA in October, and will be rolling out to free accounts in early 2027. Adding your multiple accounts to a single organization makes managing them easier by providing a unified surface for visibility and management. Organizations provide shared administrators with unified analytics and audit logging as well as shared WAF, Gateway, and Access IdP configurations.

Enterprises are eligible for exactly one organization. We limit enterprises to a single organization, so there’s a single pane of glass that shows all the company’s assets in one place. This makes life easier, so you can invite the CISO, CTO, or other executive stakeholders and give them unified visibility. If you’re an Enterprise customer and haven’t tried organizations yet, you can [set one up](https://developers.cloudflare.com/fundamentals/organizations/for-enterprise/#set-up-your-organization) directly as long as you are a super administrator of at least one account and nobody else has already created the organization. If the organization has already been started, talk to the other Cloudflare administrators in your company to get your accounts added to it. This process ensures that there’s never an elevation of privilege as we layer on this new management plane.

### Terraform and Tags

Once a customer has created multiple accounts, an organization to manage them, and set RBAC rules for the products and resources they contain, they need to be able to manage them in a way that’s auditable and repeatable. Terraform lets customers use Infrastructure as Code to manage everything using version-controlled code rather than clicking on the dashboard in a way that may not be repeatable. In the last year, Cloudflare has made dramatic progress creating a Terraform provider that is built programmatically, so it’s always up-to-date with the latest version of the Cloudflare API. Terraform, like the other features mentioned in this post, is available to all customers, Enterprise and not.

Additionally, [Resource Tagging](https://developers.cloudflare.com/changelog/product/resource-tagging/) lets customers apply key value tags to a very broad set of resources within the Accounts and Organizations. Today tags can be produced interactively or via API and are useful for organizing resources in the dashboard. In the future we intend to make tags useful in billing and access control scenarios and to be manageable via Terraform.

## How we use it all at Cloudflare

With the increasing menu of enterprise-ready options for everyone, one of the top questions we get is “What does Cloudflare do internally?” Within Cloudflare, we create accounts per team, or per service, depending on the nature of the team. We then use Terraform to manage account access and production configuration, giving teams a peer-reviewed, auditable path for changes. Because the scope of each account is narrow, we can grant broader permissions to the engineers responsible for that account while keeping the blast radius contained. This lets teams grow their accounts organically without bottlenecking on a small number of central administrators, and it makes operational work like on-call response faster and safer.

Every account at Cloudflare lives within Cloudflare’s organization, which provides our security team with administrative access to every account within the organization, as well as analytics, policy management, and shared configurations. This makes it easier to align every account in the organization to our security standards. Our teams have the right blend of autonomy and centralized control to go fast.

Enabling teams to quickly sort, organize, and filter their resources is critical in our production environments. While it’s still early, Resource Tagging is enabled internally and teams have begun to roll out tags to make finding the WAF rule, R2 bucket, etc. that they need to interact with easier.

### More features for everyone

We launched support for the [Authentik](https://developers.cloudflare.com/changelog/post/2026-03-17-scim-authentik-support/) identity provider (IdP), [SCIM Audit logging](https://developers.cloudflare.com/changelog/post/2026-03-18-scim-audit-logging/), and SCIM 2.0 Group Sync. [MCP Server Portals](https://developers.cloudflare.com/changelog/post/2026-09-24-mcp-portals-ga/) moved into general availability. All these features were once in some way Enterprise-only. Even network management is going self-serve: the [Network Overview page](https://developers.cloudflare.com/changelog/post/2026-04-21-network-overview-page/) and [Unified Routing](https://developers.cloudflare.com/changelog/post/2026-09-18-unified-routing-ga/) both recently became available for all.

### Starting with free

Solving big problems starts with first ensuring they aren’t getting any larger. This year, as part of [Code Orange: Fail Small](https://blog.cloudflare.com/code-orange-fail-small-complete/), we announced a commitment to rolling new code out by traffic cohort, starting with our free customers. As a result, today we are committed to introducing **no new Enterprise-only features**. Naturally there will be some carve-outs for things like [Cloudflare for Government](https://blog.cloudflare.com/fedramp-class-d-certification/) that are inherently Enterprise-oriented in nature.

## Other progress for free and pay-as-you-go customers

Beyond making previously enterprise-only features available to everyone, we’ve also done a lot of work to make Cloudflare more powerful and accessible for everyone

### Billable Usage Dashboard and API

In August, we introduced the [billable usage dashboard and API](https://blog.cloudflare.com/billable-usage-api/) which lets non-Enterprise customers see how much they’ve spent and download their consumption data to use offline directly or through third-party tools like Vantage. We also introduced budget alerts, which are on by default to prevent unpleasant billing surprises. We're prototyping hard spending caps now, with early availability in Q4 2026. Because Enterprise customers have dramatically more variation on contract terms and how they pay, this experience is not yet available to Enterprise customers, but we are hard at work and expect to have an announcement in 2027.

### Higher limits available to all customers

Over the past year we’ve increased limits across Cloudflare products. We’re constantly working to increase these defaults, and keep our front door as open as possible to people building the next big thing.

  * **Workers:** Your Worker can now use [1 second of startup time](https://developers.cloudflare.com/changelog/post/2025-10-10-increased-startup-time/) (up from 400 ms), send and receive [32 MiB WebSocket messages](https://developers.cloudflare.com/changelog/post/2025-10-31-increased-websocket-message-size-limit/) (up from 1 MiB), and make up to [1 millions subrequests per request](https://developers.cloudflare.com/changelog/post/2026-02-11-subrequests-limit/) (up from 1,000). Workers can now be up to [64 MiB uncompressed](https://developers.cloudflare.com/changelog/post/2026-09-04-increased-worker-size-limit/) (previously 10 MB), and we’ve [relaxed the concurrent connection limit](https://developers.cloudflare.com/changelog/post/2026-04-09-relaxed-connection-limiting/).
  * **Dynamic Workers:** Your paid Workers account can now [use Dynamic Workers](https://developers.cloudflare.com/changelog/post/2026-03-24-dynamic-workers-open-beta/) (previously restricted to prerelease access), and each Durable Object can now run [ten Dynamic Workers with in-flight requests](https://developers.cloudflare.com/changelog/post/2026-08-28-durable-objects-dynamic-workers-limit/) (up from four).
  * **Containers:** You can now use [6 TiB of memory, 1,500 vCPU, and 30 TB of disk](https://developers.cloudflare.com/changelog/post/2026-02-25-higher-container-resource-limits/) (up from 400 GiB, 100 vCPU, and 2 TB). Every Containers account can now [create custom instance sizes](https://developers.cloudflare.com/changelog/post/2026-01-05-custom-instance-types/) (previously limited to select Enterprise accounts), and each custom instance can now use [up to 20 GB of disk with any supported memory size](https://developers.cloudflare.com/changelog/post/2026-09-29-remove-disk-to-memory-ratio/) (previously limited to 2 GB of disk per 1 GiB of memory).
  * **Workflows:** Your account can now run [50,000 concurrent instances and create 300 instances per second](https://developers.cloudflare.com/changelog/post/2026-04-15-workflows-limits-raised/) (up from 4,500 and 10), and each Workflow can now queue 2 million instances (up from 1 million). Each instance can now run [up to 25,000 steps](https://developers.cloudflare.com/changelog/post/2026-03-03-step-limits-to-25k/) (up from 1,024) and stream output [up to its instance storage limit](https://developers.cloudflare.com/changelog/post/2026-04-21-step-context-and-readable-streams/) (up from 1 MiB).
  * **Browser Run:** Your account can now run [200 concurrent browsers, launch three per second, and issue 30 Quick Actions per second](https://developers.cloudflare.com/changelog/post/2026-08-20-limits-increase/) (up from 30 browsers, 30 launches per minute, and 10 Quick Actions per second). You can now make [ten REST API requests per second](https://developers.cloudflare.com/changelog/post/2026-03-04-br-rest-api-limit-increase/) (up from three), and each session can now accept [multiple concurrent clients](https://developers.cloudflare.com/changelog/post/2026-09-29-concurrent-session-connections/) (up from one).
  * **Vectorize:** Your Vectorize database can now have [20 million vectors per index](https://developers.cloudflare.com/changelog/post/2026-08-04-index-capacity-20-million/) (up from 5 million), and `topK` can now [return up to 50 values](https://developers.cloudflare.com/changelog/post/2026-03-16-topk-limit-increased-to-50/) (up from 20).
  * **Pages:** Your Pages project can now have up to [100,000 static assets](https://developers.cloudflare.com/changelog/post/2026-01-23-pages-file-limit-increase/) (up from 20,000).
  * **AI Search:** Your AI Search vector can now have [up to 10 KiB of metadata](https://developers.cloudflare.com/changelog/post/2026-08-25-larger-custom-metadata-values/) (replacing the 500-character limit for each text field).
  * **Header sizes:** [HTTP headers can now be up to 128 KB](https://developers.cloudflare.com/changelog/post/2025-10-16-header-limit-increase/) (previously 32 KB)
  * **Rules Engine:** `concat()`[ now supports up to 32 arguments](https://developers.cloudflare.com/changelog/post/2026-09-22-concat-argument-limit/) (up from 16)
  * **API Shield:** Your zone can now have [32 JSON Web Token validation configurations with 16 keys each](https://developers.cloudflare.com/changelog/post/2026-08-27-jwt-validation-limits/) (up from four configurations with four keys each).
  * **Durable Objects:** Your Durable Object can now stay alive for [up to 15 minutes while it has an active outbound connection](https://developers.cloudflare.com/changelog/post/2026-06-19-outbound-connections-keep-dos-alive/) (previously eligible for eviction after 70–140 seconds without incoming traffic), and the search API can now accept [names up to 128 characters](https://developers.cloudflare.com/changelog/post/2026-09-24-durable-object-name-search-limit/) (up from 20).
  * **Security Insights:** Your account can now receive [security scans every seven days on Free, every three days on Pro and Business, and daily on Enterprise](https://developers.cloudflare.com/changelog/post/2026-05-29-security-insights-default-scans/), and you can run on-demand scans on every plan (previously not available to all).



## Looking to the future

Between exposing formerly enterprise-only features to everyone and increasing the power of features that were already available to everyone, Cloudflare is committed to building the most powerful and accessible platform for customers large and small without the need for a contract. We still have much work to do on Dane’s pledge from a year ago, but we are committed to getting there and are delighted to be able to highlight our progress over the last year.

## Take advantage of these new offerings

  * Create additional accounts to partition the concerns of your organization.
  * Use RBAC to define security policies at the zone and account level.
  * If you’re an Enterprise customer, create an Organization and onboard these accounts. For other customers, we’ll see you in early 2027.
  * Use Terraform to manage the state across your whole organization. 
  * Attend [Cloudflare Connect](https://www.cloudflare.com/connect/) next month to learn more about everything discussed here and meet the team that built it.



]]>01M3XD0M307DCDJ5QYA2RFTW87Announcing Cloudflare OHTTP Gateway – expanding access to Cloudflare’s privacy-preserving infrastructurehttps://blog.cloudflare.com/announcing-cloudflare-ohttp-gateway/ Fri, 02 Oct 2026 13:00:00 GMTWe’re announcing the closed beta of a self-serve Cloudflare OHTTP Gateway. We’re also renaming our Privacy Gateway to Cloudflare OHTTP Relay to better distinguish the two products.Lara SchullAkshat MahajanBirthday WeekPrivacyProtocolsStandardsToday, end users carry too much of the burden of online privacy. To avoid third-party trackers or targeted ads, users are instructed to use a VPN, disable cookies, or install adblockers. Meanwhile, some app developers end up knowing more about their users than they’d care to: a typical client-server exchange creates a trail of user data, like the client’s IP address or TLS fingerprint. This level of visibility can be a burden.

That’s why Cloudflare builds infrastructure that helps developers bake privacy into their apps. Oblivious HTTP (OHTTP) is an [IETF standard](https://www.rfc-editor.org/rfc/rfc9458.html) designed to enable app backends to receive HTTP requests without seeing user IP addresses.

This fall, we’re launching the Cloudflare OHTTP Gateway. Customers will be able to enable our new OHTTP Gateway as a paid add-on to their zone and start receiving OHTTP traffic with just a few clicks. Register through [our form](https://www.cloudflare.com/lp/privacy-edge/) to join our waitlist. Read on to learn more.

## Expanding our OHTTP product suite

With OHTTP, requests travel through two independently-operated hops: a relay and a gateway. An OHTTP relay blindly forwards encrypted requests in order to hide client identifiers from app servers. An OHTTP gateway performs the cryptographic work of decapsulating encrypted requests and encapsulating responses such that app servers can handle OHTTP requests as if they were plain HTTP. The separation of trust between relay and gateway is critical: it ensures that no single party sees both client identifiers and request contents.

In 2022, we launched an OHTTP relay product, [Privacy Gateway](https://blog.cloudflare.com/building-privacy-into-internet-standards-and-how-to-make-your-app-more-private-today/). Privacy Gateway enables our customers to offer more privacy-preserving experiences to their users. For example, Flo Health uses OHTTP for their app’s [Anonymous Mode](https://www.theverge.com/2022/9/14/23351957/flo-period-tracker-privacy-anonymous-mode?cf_target_id=3398BA9F2A5670DBF3A1B9D158C4F3B0), and Apple’s [Private Cloud Compute](https://security.apple.com/documentation/private-cloud-compute/requestflow#Network-transport) uses OHTTP to disassociate AI inference requests from user identities. But customers who are already protecting their servers behind Cloudflare can’t also use a Cloudflare-operated relay — they need an OHTTP gateway instead.

In our experience running OHTTP relays, we’ve seen how difficult it can be to build and operate a secure, performant OHTTP gateway at scale. Today, we’re launching the closed beta for our self-serve Cloudflare OHTTP Gateway. We’re also renaming our “Privacy Gateway” to “Cloudflare OHTTP Relay” to better distinguish the two products. 

Now, customers who want an OHTTP architecture with the necessary separation of trust have two options:

  1. **Use Cloudflare’s OHTTP Relay (formerly Cloudflare Privacy Gateway) and run your gateway yourself**. This is best if your application servers are hosted off Cloudflare, and you’re able to run your own OHTTP gateway.
  2. **Use Cloudflare’s new OHTTP Gateway with a third-party relay**. This is best if your app servers are already behind Cloudflare (on our CDN or Workers, for example), if you’re accepting OHTTP requests from a third party (like Apple’s [LiveCallerID](https://developer.apple.com/documentation/identitylookup/understanding-how-live-caller-id-lookup-preserves-privacy)), or if you want a managed gateway to minimize latency and operational overhead. 



We’re working to raise the bar for privacy across the Internet, and we believe that protocols like OHTTP can help — if we make them easy enough to adopt. It’s always been our goal to expand our OHTTP product suite and make our trusted privacy infrastructure accessible to a broader swath of the Internet.

## Why we built the Cloudflare OHTTP Gateway

Since we launched our OHTTP Relay product, we’ve observed a few things.

First, we’ve seen that there's a growing appetite among developers for accessible, usable privacy infrastructure. Developers of privacy-oriented apps want to bake network privacy into their applications by default, but doing so remains harder than it should be. 

Second, we’ve learned that building and operating an OHTTP gateway can be tough for customers. Any proxying architecture introduces some latency because requests must travel an extra hop or two around the Internet. Combine that with the cost to decrypt requests and encrypt responses, and the latency hit of a homegrown OHTTP setup can be significant. We’re well-positioned to solve this problem: the same building blocks that enable us to operate fast, reliable privacy infrastructure for products like [1.1.1.1](https://blog.cloudflare.com/1111-privacy-examination-2026/) and [iCloud Private Relay](https://blog.cloudflare.com/icloud-private-relay/) make us a good home for an OHTTP gateway. Because of Cloudflare’s [anycast](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/) approach, our OHTTP Gateway will run on every server on Cloudflare’s global edge network, minimizing latency in relay-to-gateway hops. If you use our CDN, user requests can be decrypted by our Gateway and resolved by your app servers on the same Cloudflare metals, saving gateway-to-origin latency.

Finally, recall that OHTTP’s [privacy model](https://www.rfc-editor.org/rfc/rfc9458.html#section-6-8) requires that the relay and app server be operated by separate, non-colluding parties. We want to provide our customers with the best possible range of options for their privacy infrastructure. Before, developers who protected their app servers behind Cloudflare weren’t able to use our OHTTP Relay, because Cloudflare would see both client metadata and the decrypted contents of requests, breaking OHTTP’s privacy model. Now, developers can choose whether a Cloudflare OHTTP Relay or Gateway is a better fit for their architecture.

## A primer on OHTTP

A typical interaction between a client and application server reveals information about the client. When a client and app server talk to one another, the app server learns the client’s IP address because each packet in which data is sent is labeled with a source IP — similar to the “from” label on an envelope. App servers can also “fingerprint” a client based on attributes like supported TLS versions or cipher suites. These signals make it possible for app servers to link multiple requests back to the same user.

But what if I wanted to build an app that really doesn’t know much about my users? For example: Flo Health wanted to build an [Anonymous Mode](https://flo.health/product-tour/anonymous-mode) to enable users to access personal health data without it being linkable to possible user identifiers. 

OHTTP introduces a proxy, called a “relay,” that forwards requests and responses between client and app server to obfuscate the client’s identity from the app server. The relay sees client identifiers like IP address and TLS fingerprint, but strips them before forwarding on requests. This prevents app servers from linking multiple requests back to the same user, and means that request contents can’t be associated with the user’s IP address.

For example, a regular client-server exchange might reveal the following information about a client:

A request first sent through an OHTTP relay would reveal only the relay’s information to the app server receiving the request:

This means that for each request, the app server doesn’t learn the location and TLS fingerprint of the end user. Plus, if many different users are sending requests through the relay, the app server won’t be able to distinguish which requests are coming from whom, limiting their ability to trace app activity back to a single end user. This creates a strong privacy boundary.

What really differentiates OHTTP from a basic forwarding proxy, however, is the encryption of data between client and app server. Requests and responses are encapsulated using Hybrid Public Key Encryption ([HPKE](https://datatracker.ietf.org/doc/html/rfc9180?cf_target_id=152DBCAD3C19D59A5009B6363B375D67)) such that only the client and app server can see plaintext, and the relay sees only a jumble of ciphertext. A “gateway” sits between the relay and app server to handle all of this cryptography — decapsulating requests, encapsulating responses — and the app server handles only plain HTTP. 

This creates a “double-blind” privacy model: the relay sees only client identifiers; the gateway and app server see only request contents; no party sees both.

## How we built the OHTTP Gateway

In building our OHTTP gateway-as-a-service, our goal is to bring our secure, performant privacy infrastructure to a broader swath of the Internet. Performance and easy onboarding are critical. So, we built our Gateway as a flexible service deployed across our global network. With just a couple of clicks, you can enable the Gateway on your zone and start sending OHTTP to _https://your-zone.com/.well-known/ohttp-gateway_. We’ll scale the service up and down automatically, so you don’t need to worry about capacity.

We had a few other user needs in mind, informed by the pain points we’d seen OHTTP Relay customers run into when operating their own OHTTP gateways.

First: We wanted to abstract away as much of the complexity of OHTTP as possible for your app servers. We wanted developers to be able to start receiving OHTTP while continuing to accept regular HTTP traffic if they chose. So, we designed the Gateway as a feature of your zone, where clients send [well-formatted](https://www.iana.org/assignments/media-types#message) OHTTP requests to a _/.well-known/ohttp-gateway_ endpoint on your zone. We support both standard and [chunked OHTTP](https://www.ietf.org/archive/id/draft-ietf-ohai-chunked-ohttp-08.html) — and we recommend using chunked OHTTP for better performance, because it enables us to process requests incrementally (in “chunks”).

Our Gateway service will intercept each request, decrypt it, issue a subrequest to your app server, and return an encrypted response to the client. All non-OHTTP requests will travel to your server without invoking the Gateway.

Binding your Gateway to your zone also enables us to protect your Gateway from abuse. A client sending requests to your zone `[example.com](http://example.com)` may send to `[foo.example.com](http://foo.example.com)` or `[bar.example.com](http://bar.example.com)`, but not [wikipedia.com](http://wikipedia.com). Without you needing to worry about it, this prevents unauthorized clients from using your zone as a way to target other domains.

Second: Seamless key management is critical. Gateways need to maintain a public HPKE key configuration to enable clients to encrypt requests, but managing keys securely is a challenge. So, we designed the Gateway to fully manage all keys for customers, and to serve public keys as responses to GET requests to  _/.well-known/ohttp-gateway_. For stronger privacy, clients can download keys over a different IP than they request the gateway.

Third: Gateways need to be able to authenticate relays. Because the Gateway (by design) knows very little about the client sending a given request, it places trust in the relay to authenticate clients and forward traffic responsibly. But how do you ensure that only trusted relays can send traffic to your gateway?

We designed the Gateway such that [Cloudflare Access](https://www.cloudflare.com/sase/products/access/), Cloudflare’s zero trust network access product, runs _before_ requests are decrypted, enabling you to use any standard Access [policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/#cloudflare-access-selectors) to authenticate incoming traffic and protect your Gateway from abuse. Options include mutual TLS, static service credentials, and custom external logic.

Finally: Mistakes happen, and we anticipated that customers might accidentally break OHTTP’s privacy model by running both their relay and gateway on Cloudflare. So, to preserve OHTTP’s separation of trust and ensure that Cloudflare never sees _both_ client identities and decrypted inner requests, our Gateway will refuse __ to decrypt requests sent from Cloudflare Workers or from proxied hosts on Cloudflare.

## When is the OHTTP Gateway a better fit than the OHTTP Relay?

If you want to use Cloudflare’s OHTTP product suite, but you’re wondering why you’d pick Cloudflare’s OHTTP Gateway instead of the OHTTP Relay, here are a couple of considerations.

First, do you want your app servers on Cloudflare – behind our CDN or built on Workers, for example? If so, the OHTTP Gateway is a better fit to ensure adherence to OHTTP’s privacy model.

Second, what’s your use case? If you want to receive OHTTP requests from a third-party client and relay — to use Apple’s [LiveCallerID](https://developer.apple.com/documentation/identitylookup/understanding-how-live-caller-id-lookup-preserves-privacy) SDK, for example — then the OHTTP Gateway is likely the better solution for you. 

## Getting started

If you have a feature request or would like to register for our waitlist, so we can notify you when the product launches, [sign up here](https://www.cloudflare.com/lp/privacy-edge/).

Then, you’ll need to implement an OHTTP client. See [ohttp.info](http://ohttp.info) or our [sample client library](https://github.com/cloudflare/privacy-gateway-client-library?cf_target_id=65688FBA2DD5198BC64D2DD5FD645B07) for some examples to help you get started. One flag as you build the client: OHTTP provides privacy at the network level, and doesn’t touch the inner request body. So, to preserve user privacy, it’s up to you not to send identifying information (e.g. a user’s email address or username) in the request body.

Next, you’ll need to bring your own relay. Relays can run on any infrastructure provider, and they’re simple: here’s some [sample code](https://github.com/thibmeu/ohttp-relay). The challenge and the reason you might want a dedicated OHTTP relay provider, is to verifiably promise to your users that you won’t inspect logs with client identifiers. Otherwise, you’d be able to correlate clients at the relay with decrypted requests at your app servers. 

Finally, once your OHTTP deployment is live, check out our [pvcli client](https://blog.cloudflare.com/open-sourcing-our-privacy-proxy-cli/) to help with testing and debugging.   
  
We’re excited to bring accessible privacy infrastructure to developers everywhere. [Reach out to us](https://www.cloudflare.com/lp/privacy-edge/) if you’d like to try out the new OHTTP Gateway and raise the bar for privacy online. 

]]>01M3WRXHGNF2ZH02N0GWY6FHVVFollow the thread: a new dashboard to investigate account abusehttps://blog.cloudflare.com/account-abuse-protection-dashboard/ Fri, 02 Oct 2026 13:00:00 GMTFraudsters are increasingly using AI to bypass stateless security checks. Cloudflare's new Account Abuse Protection dashboard uses stateful analysis and edge-generated Hashed User IDs to help teams investigate and block account abuse.Nicole JustusApplication SecurityBirthday WeekBot ManagementProduct NewsSecurityTraditionally, preventing online fraud relied on point-in-time proof of identity: enter the correct password, complete a biometric verification, or pass a liveness check, and gain access. To defeat these controls, fraudsters had to steal credentials and other identity evidence from a real user, which was difficult to execute and scale. Today, widespread access to AI enables fraudsters to fabricate or imitate legitimate identities by combining exposed credentials with synthetic media designed to evade identity verification. Consequently, identity checks are no longer sufficient as they capture a moment in time. Even when someone passes a check, it does not mean the account itself can be trusted.

One convincing interaction can be faked. A consistent pattern of legitimate behavior is much harder to manufacture. Modern fraud prevention must move beyond stateless decisions toward a stateful trust model. Traditional identity verification asks, “Can this person pass the check right now?” A stateful approach additionally asks, “Does it fit what we know about this account and its established behavior?” At Cloudflare, trust is continually earned and reassessed at each interaction against historical behavioral, network, and device patterns.

Cloudflare’s Account Abuse Protection (AAP) creates stateful account overviews to help website owners detect and investigate abuse across login and signup activity. Customers configure an identifier from their existing login or signup flow, such as an email address, username, or phone number. Cloudflare cryptographically hashes that value to create a privacy-preserving, per-domain [Hashed User ID](https://developers.cloudflare.com/bots/account-abuse-protection/). Within AAP, a Hashed User ID represents an account and anchors its activity. With each login or signup, AAP adds the event and relevant network and device signals observed at Cloudflare’s edge. Over time, this accumulated history establishes context for the account’s typical behavior, making meaningful deviations easier to identify and giving fraud teams (i.e., the designated personnel for Security Intelligence, Investigations, Trust & Safety, or Risk & Compliance) a stronger foundation for investigation.

Today, we are introducing a new fraud dashboard for Account Abuse Protection, available first to Early Access customers. The workspace brings together account overviews built from activity observed across a website’s configured login and signup flows. It allows fraud analysts to view their entire user population, identify suspicious trends, and move from aggregate activity patterns into specific account investigations.

## Dashboard overview: From population visibility to individual account depth

The dashboard is designed as an investigative funnel. When a suspicious event has been identified, fraud teams can review the account population overview to understand the scale and shape of suspicious patterns without needing to investigate every account individually.

Teams can review total login and signup volume, see how many accounts generated those events, and view the unique IP addresses and devices observed across those accounts. Country and ASN breakdowns provide additional context about where the activity was observed.

The account population overview helps fraud teams answer questions such as:

  * Did login or signup volume change unexpectedly?
  * Are failed logins or leaked credential matches increasing?
  * Which accounts show the highest login failure rates?
  * Are events concentrated in particular countries, ASNs, or times of day?
  * Did a sudden signup increase coincide with shared characteristics?
  * Which accounts may have been affected by the attack?



From there, fraud teams can determine the campaign’s scope, prioritize accounts for manual review, reconstruct what happened within those accounts, and decide how to respond.

### AAP in Action: Investigating a credential stuffing attack

Consider a fraud prevention or security analyst team investigating unusual login activity. The team opens the Account Abuse Protection dashboard to determine how broadly a credential stuffing attack may have affected its users. The dashboard allows analysts to investigate from total event traffic all the way to individual accounts that warrant review. The individual account view provides the history and context needed to reconstruct what happened and determine the appropriate response.

**1\. Spot the anomaly**. The investigation begins in the account population overview, where the fraud team determines whether suspicious activity is isolated or part of a broader campaign. An increase in failed login activity prompts the team to examine Leaked credential check results on login events.

In this example, a leaked credential summary shows that approximately 2.4K events produced a leaked username or password result, compared with 11.7K events where credentials were classified as clean. This pattern is an investigative lead, not confirmation that every affected account was compromised.

The team can now focus on accounts associated with leaked credential matches. Are multiple accounts connected to the same IP addresses or ASNs? Does an individual account suddenly appear across an unusually high number of IP addresses? These relationships help define the potential scope of the credential stuffing campaign and identify the accounts that should be prioritized for review. Analysts can also look at the dashboard for concentration across particular IP addresses, ASNs, locations, or devices.

**2\. Narrow the field of investigation.** Filters help narrow the account population to specific accounts with the most concerning combination of signals and identify which ones warrant manual review. For example, filters can be set to look at accounts with at least three failed logins, at least three leaked credential matches, and observed from at least five unique IP addresses.

From this filtered cohort, analysts can select the specific Hashed User IDs, whose recent activity requires the most urgent attention.

**3\. Investigate an account.** Analysts can review login attempts, identify new devices or locations, and reconstruct how activity unfolded. Using the event table, they can compare earlier clear events with later suspicious activity, pinpoint when the pattern began, and determine whether it was a single event or a series of repeated attempts. Each event includes a Ray ID that analysts can use to look up associated information in Security Events.

**4\. Decide how to respond**. If review confirms that an account was compromised, analysts can begin their established recovery process. They can also use the Hashed User ID in a WAF rule to challenge or block future requests associated with it.

### A closer look at an individual account

An individual account view provides another layer of depth for investigation. It summarizes the login and signup activity observed for that account, including its login success rate, leaked credential matches, and most frequently associated networks, locations, and devices. Analysts can then examine the individual events behind the account summary. Each event includes its timestamp, Ray ID, and any mitigation applied. A Cloudflare Ray ID is an identifier given to every request that goes through Cloudflare, that teams can use to look up associated information in Security Events.

This detailed summary and event log helps answer questions such as:

  * Was this a single login event or part of a series of repeated attempts?
  * Did that login introduce a new country, network, IP address, or device?
  * Did the user’s behavior change afterward?
  * What happened before and after a suspicious event?
  * Did concentrated login activity follow shortly after signup?
  * Did signup and subsequent login activity use different network or device characteristics?



Viewed together, these signals help fraud teams determine whether an account requires recovery, restricting access, or another response, depending on how the customer wants to treat these accounts. When there is enough evidence, analysts can use the Hashed User ID in a WAF rule to challenge or block future requests associated with that identifier.

### Designed to minimize unnecessary data exposure

Account Abuse Protection provides account level context while also giving Cloudflare customers control over who can access account information. This launch introduces two new roles (i.e., access levels): Account Abuse Protection and Account Abuse Protection PII. The Account Abuse Protection role controls access to the dashboard, while the Account Abuse Protection PII role controls access to additional account-level PII (e.g., email) . We encourage Customer Administrators to assign these roles on a need-to-know basis, based on what each team member needs to investigate.

The Account Abuse Protection PII role is also required to create or update Logpush jobs containing PII. Separating these permissions helps customers apply least privilege access to both dashboard and data export workflows.

### Take the next step in account protection today

The new dashboard is available first to Account Abuse Protection Early Access customers. Bot Management Enterprise customers interested in these capabilities can [sign up for Early Access](https://www.cloudflare.com/lp/account-abuse-protection/). Prospective Bot Management Enterprise customers can use the same form to contact our team.

Bot detections help customers understand whether activity is automated. Account Abuse Protection adds account level overview to help fraud teams investigate whether login and signup activity appears authentic and consistent with legitimate use. Together, these capabilities help website owners address automated and human-driven abuse across account creation and login.

]]>01M3WNK9KTV3615MEM25RN3E4HProtected Quick Tunnels: simple accountless authentication for your next dev projecthttps://blog.cloudflare.com/protected-quick-tunnels/ Fri, 02 Oct 2026 13:00:00 GMTQuick Tunnels now support email authentication. Add --allowed-mail to one cloudflared command, and only the addresses or domains you list can reach your local app. No Cloudflare account required on either side.Nikita CanoHugo VicenteAlessandro FrigerioAgentsBirthday WeekCloudflare AccessCloudflare TunnelDevelopersInternship ExperienceProduct NewsSecurityWe launched [Quick Tunnels](https://blog.cloudflare.com/quick-tunnels-anytime-anywhere/) in 2021 to give developers an easy way to share their latest service, application, or project running in their local development environment. A lot has changed since then, but the core use case remains the same.

Your coding agent has just finished the feature. The dev server is up on `localhost:5173`, and before you ask, the agent offers to let you try it on your phone. It runs one command and hands you a link:

That command starts a [Quick Tunnel](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/). `cloudflared`, Cloudflare's lightweight connector, publishes your local service at a random `trycloudflare.com` URL. No account, no domain, no cost. Agents now use Quick Tunnels for the same reason people do: they are the shortest path from a local port to a URL.

The catch has always been the same. Anyone with the link can open it.

Starting with `cloudflared` 2026.9.3, you can add `--allowed-mail` to the command, and your Quick Tunnel only lets in the email addresses and domains you choose. Visitors prove they own one of those addresses with a one-time PIN from [Cloudflare Access](https://www.cloudflare.com/sase/products/access/). Nobody, on either side, needs a Cloudflare account.

## Agents made Quick Tunnels more popular than ever

Agents that write code need somewhere to show you the result. Agents that live on a Mac mini at home need to be reachable from your phone. Model Context Protocol servers on a laptop need a public endpoint before a hosted assistant can call them. Each of these needs a URL, and a Quick Tunnel produces one from a single command an agent can run by itself. There is no signup form for it to get stuck on. Add `--[output json](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/run-parameters/#output)` and every log line becomes a JSON object, so the agent can pick out the URL without scraping text.

Since agents took off, Cloudflare Tunnel and Quick Tunnels adoption has grown exponentially. On September 18, 2026, a link to the Quick Tunnels page climbed to the top of [Hacker News](https://news.ycombinator.com/item?id=49754785) and gathered more than 800 points and 300 comments. The thread reads like a catalog of agent workflows. One person's AI had found Quick Tunnels on its own to publish a site it had just built. Another called them "insanely helpful when doing agentic work on the go."

And one [commenter](https://news.ycombinator.com/item?id=49756881) asked this post answers: _"how long until someone's agent sets up a tunnel for the world to see one's most sensitive, private and embarrassing information or insecure work-in-progress app?"_

## Control who can access your service

Pass an email address to `--allowed-mail`:

Alice opens the URL, enters her email address, types in the code sent to her inbox, and reaches your app. Anyone else is stopped before a single request reaches your machine. You still don't create a DNS record, write a configuration file, or open a dashboard.

To let in more people, repeat the flag or allow an entire domain:

If you leave out `--allowed-mail`, nothing changes. Public Quick Tunnels behave exactly as they always have.

To change who can get in, stop `cloudflared` and start a new tunnel. Access ends for everyone the moment the process exits.

For a stable hostname or richer rules, such as identity provider groups, use [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/get-started/) with Cloudflare Access. To reach an agent at home from your own devices without any public URL and establish bidirectional connectivity, use [Cloudflare Mesh](https://blog.cloudflare.com/mesh/).

### Make it your agent's default

Because protection is a single flag, agents can use it as easily as people can. Add one line to the instructions file your coding agent reads, such as `AGENTS.md`:

From then on, the previews your agent shares should open only for you. Agents don't always follow instructions, so check what it ran: `cloudflared` prints whether a tunnel uses email authentication and how many rules it holds, without printing the addresses.

### Start a protected tunnel from Wrangler

If you build on Workers, you can start the same kind of tunnel from the latest version of `wrangler`:

Wrangler supports repeated flags, comma-separated values, and wildcard domains, and it removes `--allowed-mail` values from its debug logs.

## Cloudflare verifies the email. Your machine decides who gets in.

When someone opens a protected URL, they land on the Cloudflare Access sign-in page. They enter their email address, then the one-time PIN sent to that mailbox. Email sign-in is built for people using a browser.

That step answers one question only: does this person control this email address? It doesn't decide whether they're welcome. `cloudflared` makes that decision on your machine by comparing the verified address with the rules you typed.

## Where does a policy live when there is no account?

Separating those two questions is the core of the design. Authentication proves who a visitor is. Authorization decides whether that visitor gets in. Every Cloudflare product that enforces access rules keeps the authorization half in the same place: your Cloudflare account. A Quick Tunnel doesn't have one. So the hard part was never sending someone a code. It was deciding where the guest list should live.

We started with four requirements. The design had to:

  * Keep Quick Tunnels accountless, because a signup step would defeat the point of a one-command tunnel.
  * Leave the request path for public Quick Tunnels untouched.
  * Avoid a central policy lookup on every request after a visitor signs in.
  * Protect the privacy of the email addresses developers type into their terminals.



Our first idea was to put a Cloudflare Access application in front of every Quick Tunnel hostname. Access already checks visitors before traffic reaches `cloudflared`, so reusing it looked like the shortest path. But hundreds of thousands of Quick Tunnels can be running at once, many for only a few minutes, and each would need its own application and policy. With no account to own them, we would have had to invent a new namespace and route applications dynamically, just to store a list that lives for an afternoon.

Our second idea was to build the whole flow. `cloudflared` would hold the rules, and a Tunnel service would send and check the codes. The authorization half of this idea was good: each connector checks its own list, which scales naturally and keeps the rules on the developer's machine. The authentication half was not. Sending a code is the easy part of email login. The hard parts are getting email delivered, stopping abuse, building secure challenges, managing sessions, and serving a sign-in page that is accessible and translated, then operating all of it safely for years. Cloudflare Access has already solved those problems.

So we kept the best half of each idea. Access verifies that the visitor controls the email address. A small authentication broker running on [Cloudflare Workers](https://www.cloudflare.com/products/workers/) turns that verified identity into a short-lived, signed handoff. The broker is stateless by design. It stores no tunnel policies, no visitor sessions, and no identity records, and it never sees a tunnel's guest list. `cloudflared` checks the handoff and makes the authorization decision itself, in memory, against the rules you typed.

The result is the property we cared about most: your guest list never leaves your machine. Cloudflare learns that a tunnel requires email authentication. It doesn't learn who you invited.

## Following a request through a protected Quick Tunnel

A protected tunnel is created the same accountless way as a public one. The only extra thing `cloudflared` sends is the authentication mode, never your rules. If the service doesn't confirm that mode, `cloudflared` refuses to start rather than hand you a public URL by mistake.

The first time a visitor opens the URL:

  1. `cloudflared` sees a request with no session. It redirects the browser to `login.trycloudflare.com` with a random, single-use state tied to that browser and valid for 10 minutes.
  2. Cloudflare Access sends a one-time PIN to the visitor's email address and verifies it.
  3. The broker checks the Access identity and returns a short-lived, signed assertion bound to the tunnel hostname and to that state. The browser delivers it in a form POST, so it never lands in a URL, browser history, or logs.
  4. `cloudflared` verifies the assertion, uses up the state, and checks the email against your rules. On a match, it creates a local session and sends the visitor to the page they asked for. Otherwise, the visitor gets a generic response that reveals nothing about the list.
  5. Later requests use that session for up to four hours (less if the visitor's Access sign-in expires sooner), or until you stop `cloudflared`. There is no central lookup and no policy service.



The session cookie holds a random value and an expiry time, and nothing about who the visitor is. `cloudflared` strips authentication credentials before forwarding requests, so your app never sees them and never has to implement a login flow. If any check fails, the request never reaches your local service. A protected tunnel never falls back to public mode.

## Built by interns

Protected Quick Tunnels were shipped by two interns: Hugo Vicente on product and Alessandro Frigerio on engineering. They took it from the product requirements to the authentication broker to the `cloudflared` release. That's how [internships](https://blog.cloudflare.com/cloudflare-1111-intern-program/) work at Cloudflare: interns own real problems and deliver solutions to production.

## Try it on your next demo

Email protection for Quick Tunnels is free, like Quick Tunnels themselves. [Install or update ](https://developers.cloudflare.com/tunnel/downloads/)`cloudflared`, start your local server, and add the `--allowed-mail` flag: 

Setup details, matching rules, and limits are in the [Quick Tunnels documentation](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/).

The next time you or your agent shares what you're building, the link will only open for the people you chose.

]]>01M3WEQR3N79CDBSMHD5V067HABuilding for good: How civil society organizations are automating on Cloudflarehttps://blog.cloudflare.com/civil-society-automation/ Fri, 02 Oct 2026 13:00:00 GMTSome of the world's leading organizations are building the future of non-profit work with Cloudflare.Allie FunkJocelyn WoolbrightAIBirthday WeekDevelopersHuman RightsImpactPolicy & LegalProject GalileoTracking how governments target dissidents living in exile. Helping people in crisis find mental health support. Advocating for legislation that protects free expression online. These are a few examples of how some of the world's leading organizations are building the future of non-profit work with Cloudflare.

AI is changing how people do their work. The goal of Cloudflare Impact is to help ensure that non-profit organizations are among the first to benefit. Today, we’re sharing what dozens of civil society organizations have built using our developer services with more than $7.5 million of Cloudflare credits. These stories show what is possible when AI applications are accessible, secure, and affordable to build and run.

## From "keep us secure" to "help us build"

We believe a better Internet is one that allows people to express themselves online and access a diverse range of viewpoints. A key part of Cloudflare's mission has been making security services available for everyone and helping ensure that individuals and organizations working for the public interest are not forced offline by those more powerful. Today, [Project Galileo](https://www.cloudflare.com/galileo/), which provides free cybersecurity services to civil society organizations, protects more than 3,400 domains across more than 120 countries.

Through these partnerships, organizations have shared with us how their needs have evolved from not only wanting to secure existing applications, but wanting to build new ones. AI has allowed non-technical teams to design, build, and scale tools tailored specifically for their workstreams and to advance their mission.

This opportunity is arriving at a challenging moment for the sector. Many organizations [report](https://www.ifes.org/publications/assessing-impact-foreign-aid-rollbacks-civil-society) operating under financial [strain](https://www.article19.org/wp-content/uploads/2026/04/ARTICLE-19_Targeted_FINAL_April-2026.pdf) after major reductions in government funding contributed to [layoffs](https://freedomhouse.org/effects-us-foreign-aid-freeze-freedom-house) and closing of programs. As groups rebuild their work in a new environment, some have [reported](https://539405.fs1.hubspotusercontent-na1.net/hubfs/539405/AI%20Report/Virtuous%202026%20Nonprofit%20AI%20Adoption%20Report.pdf) using AI to help do more with less. But adoption remains ad hoc. In a CIVICUS [survey](https://publications.civicus.org/publications/ai-and-civil-society-threats-and-obstacles-to-deployment-and-advocacy/), more than half of civil society respondents viewed privacy concerns as a barrier to use. These groups hold sensitive data, like the location of activists or the identities of anonymous sources, and are disproportionately at risk of cyberattacks, according to our own [Cloudflare data](https://cf-assets.www.cloudflare.com/dzlvafdwdttg/5YmIHaAURvy8ZKjJ1CcQo6/1335a737054c44915ace715348e62697/BDES-9187_Cyberattacks_against_civil_society_Project_Galileo_Anniversary_Report.pdf?cf_target_id=E986CECBA6610B2E317B3BA41593B9B7). Additionally, the cost of building and running complex automation workflows can be prohibitive. Among those surveyed by CIVICUS, 48% cited financial constraints limiting their adoption.

Cloudflare helps address these concerns. Our developer services incorporate security and privacy protections from the outset. By running on our global network, applications are automatically protected from [distributed denial-of-service](https://www.cloudflare.com/products/ddos/) attacks and attempts to gain unauthorized access to internal systems. Civil society groups can also build and run applications more cost effectively. Our lightweight and serverless architecture scales with demand without requiring organizations to provision or pay for idle infrastructure. [Workers AI](https://www.cloudflare.com/products/workers-ai/) also removes the need to operate dedicated GPU infrastructure, while [AI Gateway](https://www.cloudflare.com/products/ai-gateway/) provides rate limits, observability into how teams are using AI, and intelligent model routing to reduce unnecessary model calls and keep costs under control.

## Awarding $7.5 million for the next generation of civil society work

During Birthday Week last year, we [expanded](https://blog.cloudflare.com/expanding-startups-for-nonprofits/) Cloudflare for Startups to include non-profit and public interest organizations, providing each of them with up to $250,000 in credits for our developer services. We are proud to announce that we selected 30 organizations to participate in our first non-profit, startup cohort, and we have been thrilled to watch their ideas and tools designed to tackle problems in climate science, humanitarian aid, mental health, civic engagement, and education come to life.

Here is what a few of these non-profits have built.

  * **LebTown — local news, rebuilt on automation:** [LebTown](https://lebtown.com/) is an independent non-profit newsroom covering Lebanon County, Pennsylvania. Until this year, the editorial team ran its entire operation across two Google Docs, a Google Calendar, Discord, and Gmail. LebTown is replacing that with a custom-built editorial management system that follows stories from pitch to publication, tracks audience reach, and lets reporters log community impact directly from their app or via Discord. The team has also built tools that convert county real-estate transfer records from PDF exports into structured data, and a real-time copyeditor agent that integrates with LebTown's WordPress site.


  * **Kaya Guides — scaling mental health support:** [Kaya Guides](https://kayaguides.com/) built a WhatsApp-based mental health application that pairs people experiencing depression in India with trained lay counselors, making support accessible without the cost or waitlists of traditional therapy. As of September 2026, the application has supported 10,439 people, with 2,325 currently enrolled. To keep pace with demand, the team migrated its care management system to Cloudflare and now processes around 500,000 WhatsApp messages a month. They built a live AI system that listens to counseling calls and gives counselors real-time feedback to keep sessions on track. According to Kaya, these tools have helped develop a program that is more consistent and self-correcting as it scales, without significant additional cost or complexity.
  * **The Snorkelling Society — mapping the world’s snorkeling sites.**[ The Snorkelling Society](https://snorkellingsociety.org/), is a UK non-profit building a web and mobile application for the global snorkeling community called [SnorkelMap](https://snorkelmap.com/). This tool will help people discover new places to snorkel, explore information about different locations, and allow users to contribute their experiences. Because the application is built and maintained by volunteers, the Snorkeling Society uses Cloudflare to secure storage to allow for community contributions and uploaded images while also safeguarding against cyberattacks.



## Working together to build automation tools for human rights

We also heard from larger civil society organizations who wanted to build complex workflows and welcomed extra engineering support. These projects included several variations of the same problem: large amounts of manually-collected, dispersed information that needed to be integrated, reviewed, and structured in order for effective analysis to be conducted. The data involved was also sensitive, like the names of human rights abuse victims, and the risk of unauthorized access, data leakage, or hallucinations in an output could have serious consequences.

Cloudflare not only provided free access to its developer service to support the development of each of these tools, but also assembled a team of volunteer engineers — product experts, front-end designers, back-end builders, and security advisors — to design and build them. Questions we’re exploring include where automation is helpful, which models align best with each task, how to incorporate the necessary security controls, and where a person must remain involved.

  * **Freedom House — tracking transnational repression:** [Freedom House](https://freedomhouse.org/) was founded in 1941 to advance democracy and freedom globally. They created and maintain the world's most comprehensive database of [transnational repression](https://freedomhouse.org/report/transnational-repression) incidents, which is when governments reach across borders to silence dissent among diaspora and exile communities. Manually identifying incidents and coding patterns of transnational repression — which involves looking at thousands of potential cases — is labor intensive and time consuming. To help automate this process, we are creating an interactive dashboard that can ingest, structure, and flag potential cases of transnational repression from public reporting. The tool is fine-tuned on the organization’s methodology to improve accuracy, with Freedom House involved in every step of the process. Given the sensitivity of the topic, security and data minimization have been priorities in every decision. Automating this initial stage in the research process can help staff focus on deeper analysis, producing reports, and working with policymakers to address transnational repression.



_Prototype of Freedom House’s tool tracking transnational repression_

  * **Global Network Initiative — protecting free expression and privacy online:** The [Global Network Initiative](https://globalnetworkinitiative.org/) (GNI) is a membership organization of civil society groups, academics, investors, and tech companies (including Cloudflare) working to advance free expression and privacy online. To do this, GNI tracks and responds to a rapidly evolving landscape of regulatory proposals, policy developments, and legal trends across dozens of jurisdictions, from online transparency requirements in the European Union to data localization mandates in the Asia Pacific region. We are building a dashboard that identifies these proposals and recommends opportunities for advocacy based on GNI’s mission and previous work. It surfaces, describes, and categorizes relevant news, calls for comment, and legislative activity. The tool also helps manage each opportunity by tracking the internal review process and alerting staff of upcoming deadlines.



_Prototype of GNI’s dashboard that tracks the status of engagement opportunities_

  * **Article One — assessing human rights risk:**[ Article One](https://articleoneadvisors.com/) is a specialized strategy and management consultancy that advises companies on understanding and mitigating the human rights impacts of their policies, products, and operations. This involves reviewing and summarizing large amounts of documentation, from factory audits to country-context reports. We are working with Article One to build a risk assessment tool that processes and structures this information, identifies salient human rights risks, and generates draft recommendations that staff can review and refine. AI helps structure information, but Article One makes all judgments.



## What’s next? Apply to join our second cohort

It’s incredible to see how civil society organizations are evolving their work in an era of AI. Cloudflare is excited to play a small role in this process. Working directly alongside these organizations not only helps advance their missions, but also helps inform how we think about the security and privacy in high-risk environments and how we can scale similar programs moving forward.

Our first non-profit startup cohort shows how automation can help the next generation of community service organizations use AI and automation to serve the public, and how they can do this securely and affordably. 

**We’re excited to announce that starting today we are officially opening our startup program to our second cohort of non-profit organizations.**

If your organization is interested, [**apply here**](https://www.cloudflare.com/startups/) and select the non-profit checkbox. We’d love to build with you!

]]>01M3W899F5N6P98MYP180WJMS42026 Birthday week: network performance updatehttps://blog.cloudflare.com/network-performance-birthday-week-2026/ Fri, 02 Oct 2026 13:00:00 GMTCloudflare now ranks as the fastest provider across 74% of the top 1,000 global networks. By incorporating background telemetry from Cloudflare Challenge Pages, we have expanded our real-user measurement scale while maintaining user privacy.Lai Yi OhlsenBirthday WeekNetwork Performance UpdatePerformanceTurnstileCloudflare is now the fastest provider in 74% of the 1,000 largest networks around the world, [up from 60%](https://blog.cloudflare.com/network-performance-agents-week/) in April 2026. This huge improvement matters because every millisecond affects how quickly users can reach the applications, APIs, and websites they rely on. In this Birthday Week performance update, we’ll review how we get our measurements, introduce a new measurement methodology using Cloudflare Challenge Pages, and discuss where these improvements have had the biggest impact for customers.

## Cloudflare is fastest in 74% of top networks

In August, Cloudflare was the fastest provider in 74% of top networks, up 14 percentage points from our last update during Agents Week in April. The figure below shows the countries where Cloudflare is the fastest provider.

We improved from 60% to 74% by becoming the fastest provider in an additional 150 networks out of that top 1,000, and there are 38 additional countries where Cloudflare now ranks as the fastest. We measure this by looking at the fastest provider for users on the networks serving the largest number of users in each country.

The graphic below shows countries where Cloudflare has become the fastest provider across those networks since April.

Here you see the number of additional networks on which Cloudflare is now the fastest.

## How do we get these measurements?

Our analysis begins with the 1,000 largest networks in the world, ranked by estimated user population using data from [APNIC](https://stats.labs.apnic.net/cgi-bin/aspopjson). Because these networks cover users across a wide range of geographies and access environments, they give us a useful view into how people actually experience the Internet.

For each network, we evaluate performance using connection time: the amount of time required for a user’s device to complete a TCP handshake when requesting content. We use this because it maps closely to what people think of as a “fast” user experience. It reflects real-world factors such as distance, routing, and congestion, while still being specific enough for us to compare providers and identify where performance can improve.

To rank providers, we calculate the trimean of connection times. The trimean combines the 25th percentile, 50th percentile, and 75th percentile into a weighted average. Using this method helps reduce the influence of unusual outliers while still representing the range of experiences that most users see. You can read [previous posts](https://blog.cloudflare.com/introducing-radar-internet-quality-page/) to learn more about why we chose this metric.

When someone reaches a Cloudflare-branded error page, their browser can run a small background measurement that fetches lightweight files from several providers, including Cloudflare, Amazon CloudFront, Google, Fastly, and Akamai. We then record how long each connection takes from that user’s browser, on that user’s network, at that moment. This gives us a picture of performance under real Internet conditions, not just in controlled test environments.

Since 2021, Cloudflare-branded error pages have provided a reliable source of real-user performance data, and they remain an important part of how we measure performance. But measurement gets better with scale. The more data we collect, and the more networks we observe, the more accurately we can understand how users experience the Internet. Since our last update, we have expanded our performance data collection by adding measurements using Cloudflare Challenge Pages.

## Introducing performance benchmarking with Challenge Pages

If you're not already familiar, Cloudflare Challenge Pages are full-page screens that verify visitors before they reach a website. When a challenge is actioned — typically by a Web Application Firewall rule — the Challenge Page acts as a gate: it holds the request, evaluates the browser environment for automated signals, and only lets legitimate visitors through, usually with no interaction required. Challenge Pages are delivered by [Cloudflare Turnstile](https://www.cloudflare.com/products/turnstile/), our privacy-preserving, risk-based challenge technology that runs directly in the visitor's browser.

Because Challenge Pages run across a broad set of websites and real-world network conditions, they present a novel way to collect performance measurements from the places where people actually use the Internet. If you want to add Challenge Pages to your own website, you can get started with the [Cloudflare Challenge Pages documentation](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/).

### How does it work?

From an end user's perspective, Challenge Page-based measurement works much like our existing error-page measurements: it runs quietly in the browser and does not require the user to do anything extra. While the visitor is on a Challenge Page a small, non-interactive measurement runs in the background. It fetches lightweight files from a fixed set of endpoints, including Cloudflare, Amazon CloudFront, Google, Fastly, and Akamai, and records whether each request completed and how long it took.

While we care about measuring performance, we care even more about improving it. That includes making sure our measurements do not negatively affect the user experience. We designed the Challenge Page measurement to avoid adding noticeable latency for visitors, while preserving the privacy-focused properties that Turnstile brings to Challenge Pages and that make them different from traditional CAPTCHAs.

For now, we are running measurements on only a small fraction of eligible free Challenge Pages, in addition to continuing to collect data from Cloudflare-branded error pages. We will limit these measurements to free Challenge Pages and we will only increase the sampling rate if the additional data improves measurement quality and end-user performance remains unaffected.

### Challenge Pages’ reach helps measurements scale

The main upgrade from the error-page method alone is reach. Cloudflare-branded error pages have given us high-quality measurements from a narrower set of use cases, while Challenge Pages let us collect similar measurements during everyday interactions, wherever a challenge is already being served. That means more measurements from more networks, without requiring users to take any additional action. By collecting measurements on Challenge Pages, we are dramatically increasing the volume of data we collect and improving the diversity of users, networks, and geographies we measure. From a data quality perspective, this takes an already informative dataset to the next level.

### More measurement, more possibilities

Even though the initial results from Challenge Pages measurements are promising, we have even more ideas for how to improve the dataset. First, we want our measurements to describe the experience of as many users as possible. Because Challenge Pages runs across such a broad set of websites and visitors, it gives us measurements from networks well beyond the top 1,000 and far more samples within each one, especially as we increase our test volume. That breadth gives us more analytical options: we can explore views that a network-count ranking alone cannot support, such as weighting performance by the number of people who experience it, grouping results by country or worldwide instead of by network, and quantifying how much of total user traffic our measured networks represent. 

Second, more measurements give us sharper resolution where the race is closest. In many networks, the top providers are separated by only a millisecond or two of trimean connection time such as Cloudflare at 50 ms and Fastly at 51 ms, which is a gap small enough that ordinary day-to-day variation can flip the ranking. As Challenge Pages add measurement volume, the confidence interval around each provider's trimean will narrow, letting us distinguish a genuine lead from statistical noise. The results we are sharing today are early, but as the dataset becomes larger, we expect future movement in these rankings to further reflect real changes in performance.

### Improved measurements show Cloudflare as #1

This significant improvement coincides with the addition of our new measurement methodology described above. By increasing measurement volume, Cloudflare has more opportunities to compare performance against other top providers across a broader set of networks and user conditions. In practice, this gives us a clearer signal in networks where performance among top providers is very close.

For example, Cloudflare may have previously ranked second in some networks even though our trimean connection time was only 1 or 2 ms slower than the fastest provider. With more measurements, the results are less sensitive to outliers and day-to-day variation. That makes rankings more stable, especially in countries and networks where the fastest provider may have previously changed from one day to the next. As the dataset becomes larger and more representative, we get a more consistent view of which provider is actually fastest in each network.

## Performance is a process

Improving performance is a continuous process, and so is improving how we measure it. This year’s results show meaningful progress: Cloudflare is now the fastest provider in 74% of the top networks we measure, and our new Challenge Pages-based methodology gives us a broader, more stable view of Internet performance around the world. We’ll keep using that data to find where we can be faster, validate the impact of our improvements, and make the Internet better for the customers and users who rely on Cloudflare every day.

Follow our blog for more [performance updates](https://blog.cloudflare.com/tag/network-performance-update/) as we continue to make the Internet faster.

###### 

]]>01M3T5GMDCTRDCS7CFJSMSJ2TSIntroducing Clef: our open-source decision models, and new RL fine-tuning platformhttps://blog.cloudflare.com/clef-decision-models/ Thu, 01 Oct 2026 15:34:02 GMTWe are introducing Clef and Clef-flash, open-source decision models hosted on Workers AI for high-speed classification and agentic workflows. Also launching: a new reinforcement learning platform that allows developers to fine-tune decision models using their own data.Michelle ChenAlex ReneauKevin FlansburgAIBirthday WeekDevelopersMachine LearningOpen SourceWorkers AIOver the last few weeks, there has been lots of buzz around decision models such as [Typesafe AI’s Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) System One model. While classifier models have been around for some time, Jev introduces a new decision model concept into the world of AI — a model that produces bounded structured outputs cheaply, quickly and consistently that can be added into a workflow when a decision is required. These models are capable enough to work over any set of inputs without constantly retraining the model to incorporate new classification categories. This contrasts with the world of Large Language Models (LLMs), which are largely non-deterministic, but are open-ended enough to reason and generate text and tool calls for agentic workloads. 

Today, we’re releasing two Cloudflare-trained decision models, Clef and Clef-flash, [hosted on Workers AI](https://developers.cloudflare.com/workers-ai/models/clef). Clef is currently the leader when evaluated against the [Jev Decision Index](https://huggingface.co/spaces/multimodalart/jev-decision-index), you can view full results on the [live benchmark demo site](https://clef-evals.workers-ai-mle.workers.dev). These models are smarter, faster, and fully Jev-API compatible, so you can experiment with these hosted models easily. We’re fully open-sourcing these [models on Hugging Face](https://huggingface.co/Cloudflare/clef) under an Apache 2.0 license for you to run locally and experiment with yourselves. 

Lastly, we’re excited to debut our new reinforcement learning (RL) product, which allows customers to fine-tune Clef to suit their use cases as well.

## What is a decision model?

A decision model makes classifications to help agents decide how to act, based on certain probabilities. For example, you can pass in a customer support message (inputs) and ask if it is urgent and which team should handle it. A decision model will return typed answers with probabilities (outputs), which your code can use to route the ticket, trigger an escalation, or defer to a human. This means that a human does not necessarily need to be in the loop for agentic decisions anymore — agents can programmatically gather context, make decisions, and take actions on tasks, or defer to a human when needed.

Specifically at Cloudflare, we’ve been testing our new Clef model on our Threat Intelligence team to help us classify website domains. By giving a domain to Clef (with Browser Run) it can quickly identify categories that the domain falls under — for example, it might classify a domain with a 95% chance it is a fashion website, 85% ecommerce, <1% phishing, etc. This classification took our Clef model 2.2s to fetch, render, and classify the website. In contrast, our fastest general LLM gpt-oss-120b took 4.7s in the same workflow, and only returned two classifications. As a user, you can imagine how a 2x savings in latency and results can help us improve our threat intelligence workflows and be faster in identifying malicious or legitimate domains. Generalize this to any use case where you need to make quick programmatic decisions, and you unlock powerful agentic workflows that are able to autonomously decide, reason, and execute.

In music theory, a clef is a symbol placed at the beginning of a musical staff that assigns specific pitch names to the lines and spaces. A decision model is analogous to a music clef because it helps define the domain of the context and the subsequent notes (actions) that follow it. We chose Clef as the name of our family of decision models, as it serves similar purposes, and the CF hearkens to Cloudflare.

## How is Clef different from other decision models?

Although the market is getting increasingly saturated with decision models, Clef has some unique properties that make us excited to release it to the public. First, it has a vision encoder so it’s able to take in images and classify visual content. This is different from Jev, which only does text classification today. Secondly, our model has a 64k context window (compared to Jev’s 32k), which allows users to squeeze more input state for the model to classify against.

Third, our model is accurate and powerful, scoring competitively against other decision models on the market across various quality benchmarks. We shortlisted some evaluations below that are important for decision-making as defined by the [Jev Decision Index](https://huggingface.co/spaces/multimodalart/jev-decision-index) and scored some of the more popular models on the market for it. Check out the table below for benchmarks, or view the scores on our [live decision index demo site](https://clef-evals.workers-ai-mle.workers.dev):

**Benchmark**| [**Clef**](https://huggingface.co/Cloudflare/clef)| [**Clef-flash**](https://huggingface.co/Cloudflare/clef-flash)| [**Jev**](https://typesafe.ai/blog/introducing-system-one-models-and-jev)| **DiffusionGemma Jev**| [**Kev 9B**](https://huggingface.co/jaredpalmer/kev-9b)| [**Laya**](https://huggingface.co/convaiinnovations/laya)  
---|---|---|---|---|---|---  
BFCL · case exact| 98.47| **98.76**|  95.75| 96.52| 94.51| 38.13  
ToolRet · nDCG@10| **69.19**|  66.43| 65.28| 61.21| 64.26| 12.69  
API-Bank · accuracy| 91.93| **93.11**|  88.19| 83.66| 56.30| 11.41  
Home appliances · case exact| 82.95| **97.73**|  52.27| 42.05| 25.00| 0.00  
When2Call · accuracy| 72.37| 65.58| **80.97**|  75.44| 49.62| 11.94  
BANKING77 · macro-F1| **94.20**|  90.93| 79.74| 74.28| 84.83| 14.29  
CLINC150+OOS · macro-F1| **97.43**|  66.77| 89.27| 83.49| 79.03| 3.19  
BRIGHT · nDCG@10| 45.91| 39.26| **47.52**|  42.94| 38.53| 19.90  
Amazon ESCI · macro-F1| **57.48**|  57.39| 55.21| 53.37| 49.22| 24.40  
PhishNChips · accuracy| 79.60| 75.05| 62.55| **85.35**|  50.75| 50.15  
  
We also ran benchmarks across [Typesafe’s own eval suite](https://huggingface.co/collections/typesafe/workflowevals) and our Clef models fared well, beating Jev in 3 out of 4 areas. Notably, our Clef-flash performs exceptionally well, given how much faster it is.

**Workflow**| [**Clef**](https://huggingface.co/Cloudflare/clef)| [**Clef-flash**](https://huggingface.co/Cloudflare/clef-flash)| [**Jev**](https://typesafe.ai/blog/introducing-system-one-models-and-jev)  
---|---|---|---  
Invoice processing| **64.7**|  57.1| 61.8  
Customer service| 76.3| **77**|  76.0  
Security incidents| **62.9**|  61.7| 61.7  
Agent trace observability| 68.5| 69.8| **71.6**  
  
Across the 43 eval benchmarks that we ran, our Clef models beat the decision models on latency (except for Laya which is very fast but trades off quality in the benchmarks above):

**Benchmark**| [**Clef**](https://huggingface.co/Cloudflare/clef)| [**Clef-flash**](https://huggingface.co/Cloudflare/clef-flash)| [**Jev**](https://typesafe.ai/blog/introducing-system-one-models-and-jev)| **DiffusionGemma Jev**| [**Kev-9B**](https://huggingface.co/jaredpalmer/kev-9b)| [**Laya**](https://huggingface.co/convaiinnovations/laya)  
---|---|---|---|---|---|---  
Median latency · ms| 209.3| 38.8| 524.1| 84.4  
| 51.4| **5.8**  
p95 latency · ms| 238.6| **122.4**|  536.0| 211.2  
| 187.9| 222.5  
  
On top of the latency benefits from the model itself, our Clef models are hosted on Workers AI. Because they are hosted on Cloudflare’s infrastructure, we’re able to take advantage of our GPUs at the edge, leading to low network latency and faster decisions. This means that you could put Clef into the hot path for agents to make decisions and combine that with one of our LLMs on Workers AI to take action. 

  
Clef also produces strictly typed outputs similar to Jev and is fully API-compatible, so you can make the swap extremely easily. The larger Clef model is your more powerful precision model, while the Clef-Flash model is great for latency-critical decisions. The models are enterprise-ready with our guarantee that we don’t read, store, or train on your requests or responses (unless you want to use our fine-tuning product, which we go into below). You can get started with the Clef models today, starting with our [developer documentation](https://developers.cloudflare.com/workers-ai/models/clef) or play around with the [open-source model on the Hugging Face repo.](https://huggingface.co/Cloudflare/clef)

If you’d like help tuning Clef for a specific workload, we are also offering fine-tuning services — first as a hands-on partner with our forward-deployed engineer (FDE) team, and then later as a self-serve fine-tuning platform for customers to train and redeploy the model onto Cloudflare.

### How we trained Clef

In the same week that Jev came out, we [posted about some experiments](https://x.com/michellechen/status/2101091012559151480) we had with our own homegrown decision model. Our demo goes into how we adapted the DiffusionGemma model to output deterministic probabilities by exposing the logprobs that are generated by a large language model. Our initial approach built upon independent research by [Matt Mastracci](https://x.com/mmastrac), who has been active in the machine learning (ML) community with sharing new ideas and [pull requests to vLLM](https://github.com/vllm-project/vllm/pull/57250) inference engine to make DiffusionGemma support stronger.

Clef builds upon this concept, but uses a different base model as the backbone. We currently use Qwen as the base model and post-trained it to suit decision model use cases. During inference, Clef uses Qwen for a prefill-only pass, then scores the valid schema choices in parallel. The decision step is non-autoregressive, so there’s no intermediate text to generate token by token, making Clef significantly faster than autoregressive LLMs. Rather than generating intermediate text to produce structured answers, Clef and Clef-flash derive schema choices directly from internal backbone representations. This approach relies on a specialized two-stage attention routing process: every valid choice extracts context relevant to the prompt, allowing individual field parameters to cross-attend with other fields and back to the original payload prior to scoring. By leveraging a lexical prior, the model preserves semantic intent across options. Ultimately, the architecture unites option-specific evidence routing, joint cross-field attention, and schema-bound scoring.

By freezing Qwen3.8-27B for Clef and Qwen3.5-9B for Clef-flash, we jointly optimized the routing head alongside rank-256 low-rank adapters. Our post-training utilizes label-smoothed cross-entropy for valid schema outputs paired with a Brier loss to refine probability calibration. This training leverages our own internal synthetic datasets permutating field orders, prompts, and schema structures. We also developed Reinforcement Learning for Calibrated Decisions (RLCD) to serve as a secondary optimization target, granting partial credit to adjacent ordinal choices, rewarding fully precise record outputs, and applying a reference penalty to prevent distribution shift, giving us better accuracy and generalization.

This means that we were able to achieve a few novel things with Clef: we improved accuracy of the model in classification, constrained it to output only probabilities instead of text generation, and made it faster than Jev and the base Qwen models.

### How fine-tuning can extend the capabilities of Clef

We heard a lot of internal use cases that required fine-tuning our Clef model to be built into our agentic workflows at Cloudflare. For example, internal teams want a classifier model to be able to evaluate Trust & Safety submissions, help us triage Cloudflare Support requests, or even to be built-in to our Bot products to decide if a crawler is a good bot or bad bot.

These use cases are incredibly specific and we have had many years of labelled decisions that we could use to train a specific classifier. When you fine-tune a model, you may give up some general purpose performance in exchange for higher accuracy in a specific domain.. Because Cloudflare has more than 15 years of network data across different domains, we can fine-tune a model to fit these specific use cases which is more accurate and faster than our generic Clef model. We’re working with internal teams already to figure out how we can post-train Clef to create powerful ML models that boost our impact and improve workflows across Cloudflare. These internal teams and use cases are the next remit of our new FDE fine-tuning team and basis for our reinforcement learning (RL) product.

### Our new RL service

We are offering a service to help customers fine-tune Clef to suit their workloads with our hands-on FDE team. From that, we’ll learn from our hands-on experiences to build a self-serve platform that customers can use to capture data, fine-tune, and redeploy the model, all on Cloudflare.

This has actually been a long time coming — we’ve been building our AI platform to have the right primitives where we could be building a custom RL product. The interest in Jev shows the need for a fast, small, specific, classifier model, and we chose this to be our niche to start experimenting with RL environments.

To do this, we leverage the primitives that we already have built on our Cloudflare platform:

  * Cloudflare AI Gateway – pass all your AI traffic through AI Gateway and automatically create a dataset of requests for your use case
  * Cloudflare Workers AI – generate rollouts against the base Clef model
  * Cloudflare Containers – RL sandbox for scoring and replaying agent actions
  * [NEW] Trainer – update weights of fine-tuned Clef model
  * Cloudflare Workers AI + BYO Model – redeploy the fine-tuned model on Workers AI



This combines a few work-in-progress pieces of the AI Platform that we’ve been working on, including AI Gateway that captures your AI traffic so you can leverage your own request/response data, Containers for RL Sandboxes, and Workers AI’s Bring Your Own Model (Cog) work that has been progressing since our acquisition of Replicate. 

### Try it out today

We’re excited to launch our first Cloudflare-trained ML model from the Workers AI team today. We’re still early here and have a lot more improvements in store, but it is a wonderful first showcase of the hard work we’ve been doing on the AI Platform team. We believe that Clef has the ability to disrupt the way we use agents, which fits naturally into Cloudflare’s mission of being the agent cloud.

If you have specific use cases and are already customers of these products — [we’d love to chat with you and be design partners as we experiment in this space.](https://www.cloudflare.com/resource/clef-rl-interest)

Try out the Clef models hosted on Workers AI, download the [weights on Hugging Face ](https://huggingface.co/Cloudflare/clef)if you’d like to explore for yourself, and reach out if you have fine-tuning use cases you’d like us to help with.

Our ML team has been growing in impact, from model optimizations to model training research. If you’re interested in joining our mission, [check out our open roles](https://www.cloudflare.com/careers/). 

###### 

]]>01M3TJPSZAN4TKGKX6HWSNQWEPOne year later: Sovereign AI and the fight for choicehttps://blog.cloudflare.com/sovereign-ai-choice-one-year-later/ Thu, 01 Oct 2026 13:04:19 GMTAI sovereignty is not a zero-sum game, but many governments now believe it is. Cloudflare's answer: more local open-source models, model-agnostic security tools, and a commitment to giving nations genuine choice.Carly RamseySmrithi RameshPetra ArtsAIBirthday WeekOpen SourcePolicy & LegalSecurityIt's Birthday Week, when we traditionally ship presents to the Internet. This year, two of them come from Europe: EuroLLM, which covers all 24 official EU languages, and Apertus, Switzerland's fully open model, trained on more than 1,500 languages. Both were built by public universities and research institutions. Both are coming to Workers AI, and you can request access today.

We're also launching hands-on workshops that help government cyber agencies and critical infrastructure operators build AI defenses that work with any model. The first runs in Singapore in October.

Today's announcements follow from an argument we made [a year ago](https://blog.cloudflare.com/sovereign-ai-and-choice/), when questions about AI access and sovereignty were swirling in national capitals. Our answer was choice: the freedom to pick the right tools for the job, and to switch when you need to.

Since then, those conversations have hardened. Attackers have used frontier models to run cyber attacks. Access to some frontier models now depends on where you are. Calls to restrict open models are getting louder. Put it all together and it's easy to conclude that AI sovereignty is zero-sum: every model another country controls is one you can't count on, so the safe move is to build walls.

We think the past year can point the other way. India, Japan and Singapore focused on open-sourced models, and people across Asia-Pacific built tools on them for rural citizens, elderly patients and the nurses who care for them. Our own security team built AI defenses that work with any model, so losing access to one doesn't mean losing your defenses.

Helping build a better Internet has always meant more options, not fewer. That's why we work on open standards that prevent [vendor lock-in](https://www.cloudflare.com/learning/cloud/what-is-vendor-lock-in/), why so much of what we build is free to start with, and why our [network](https://www.cloudflare.com/network/) runs in more than 335 cities across 125+ countries, with GPUs for AI inference in more than 230 of them. We don't think any country should have to depend on one company for its AI. That includes us.

## Two European open models on Workers AI

In February, Matthew Prince told the India AI Impact Summit 2026 in New Delhi that decentralized, affordable access to AI is a matter of national resilience. The models from India, Japan and Singapore we'd added a few months earlier were our first proof. The summit series moves to [Geneva](https://genevaaisummit.swiss/) in June 2027, with a mission of "prosperity and progress for all."

[EuroLLM](http://eurollm.io/) supports 35 languages, including all 24 official EU languages, many of which are underserved by existing open models. It was developed with support from Horizon Europe, the European Research Council and EuroHPC by a consortium that includes Instituto Superior Técnico, the University of Edinburgh, Instituto de Telecomunicações, Université Paris-Saclay, Unbabel, Sorbonne University, Naver Labs and the University of Amsterdam. It was trained on the MareNostrum 5 supercomputer and, according to the consortium, outperforms similar-sized models on EU multilingual benchmarks and machine translation.

You can request access to EuroLLM on Workers AI [here](https://developers.cloudflare.com/workers-ai/models/eurollm-9b-it/).

[Apertus](https://apertus-ai.org/) (Latin for "open") is Switzerland's first large-scale, fully open, multilingual language model. It was trained on more than 15 trillion tokens across more than 1,500 languages, with 40% of training data in languages other than English. It was developed by ETH Zurich, EPFL and the Swiss National Supercomputing Centre (CSCS) as part of the [Swiss AI Initiative](https://www.swiss-ai.org/): built by public institutions, for the public good. Its architecture, weights, training data and methods are all published. It was designed with Swiss and European rules such as the EU AI Act and GDPR in mind, which means respecting training opt-outs, removing personal data and preventing memorization. It was trained on CSCS's Alps supercomputer (more than 10,000 GH200 GPUs), and its developers report that it significantly outperforms leading closed and open models on rare and regional languages, from Romansh and Swiss German to low-resource languages across Asia and Africa.

You can request access to Apertus on Workers AI [here.](https://developers.cloudflare.com/workers-ai/models/apertus-v1.5-8b)

## What people built last year

Last year's national models didn't sit on a shelf. Since we added them to Workers AI, hundreds of students, startups, small businesses and public servants across Asia-Pacific have built on them, many at buildathons we ran with local partners. Three of them:

  * Government forms, no reading required – [Form Mitra](https://pdf-form-filler.devansh-654.workers.dev/) (India): Benefit forms written in dense English shut out many of the rural, low-literacy and visually impaired citizens they're meant for. Students at the Indian Institute of Technology Delhi built Form Mitra at a buildathon we ran with [CyberPeace](https://cyberpeace.org/): a voice-guided assistant that walks people through the form in any of 22 Indian languages, using [AI4Bharat's IndicTrans2](https://developers.cloudflare.com/workers-ai/models/indictrans2-en-indic-1B/) model.
  * Care in the patient's own dialect – [MedBridge](https://www.linkedin.com/posts/ajith-sreelekshmi_aiops-agenticai-healthtech-ugcPost-7464567178646941696-Wi9f/) (Singapore): Many of the nurses caring for Singapore's elderly patients come from across Southeast Asia and don't speak the local dialects, so critical clinical information can get lost in translation. MedBridge guides patients through health conversations in 14 languages, including Hokkien and Cantonese.
  * The right public service, in one tap – Anshin Concierge (Japan): For elderly residents, people with disabilities and anyone less comfortable with digital tools, working out which public service to call in a moment of need can be overwhelming. Built as a hackathon prototype, Anshin Concierge lets people describe the problem in their own words ("_my knees hurt_ ", "_a strange screen appeared on my phone_ ") and connects them to the right Tokyo Metropolitan Government support desk, by phone or web page, in one tap. 



## AI defenses that don't depend on one model

Governments want to use AI to defend essential services and national infrastructure. The frontier models that can find vulnerabilities at scale can find them for [defenders](https://blog.cloudflare.com/vulnerability-discovery-remediation/) too. But a defense built on one model is only as dependable as your access to that model, and governments have watched access to critical models get constrained with little warning.

We had the same problem, and in security we are always our own first customer. Over the past year, our Security team, working with teams across the company, set out to build AI defenses that don't depend on any one model. We built a harness: an orchestration layer that coordinates multiple AI models working in parallel to hunt for vulnerabilities, verify findings and prioritize threats. We [published what we learned](https://blog.cloudflare.com/cyber-frontier-models/) about using frontier and open models together, [open-sourced the harness](https://blog.cloudflare.com/build-your-own-vulnerability-harness/) so any organization can run it with the models of its choice, and laid out the [layered architecture](https://blog.cloudflare.com/frontier-model-defense/) we use to stop attackers armed with frontier models from finding vulnerabilities in the first place.

Because the harness works with any model, closed or open, losing access to one provider doesn't switch your defenses off. When we walked governments through it, the most common reaction was relief. Then came the practical questions: how to stand it up in their own environments, under their own rules. Briefings quickly turned into requests for hands-on training.

So today we're launching a program of hands-on workshops for government cybersecurity agencies and critical infrastructure operators. Participants build their own AI security harness and layered defenses, and leave knowing how to adapt both to their organization. The modules are plug-and-play, designed to slot into national AI skilling and cyber resilience programs. The first workshop runs in Singapore this October, at Singapore International Cyber Week.

## Come build with us

None of this happened alone. Partners like [CyberPeace](https://cyberpeace.org/) in India and [Code for Japan](https://www.code4japan.org/en) helped turn open models into working tools. If you run a national AI program, a cyber agency or critical infrastructure, and you'd like more options than you have today, write to us at policy-team@cloudflare.com. Request access to EuroLLM and Apertus, or start with the [harness](https://blog.cloudflare.com/build-your-own-vulnerability-harness/).

A year ago, we said choice is the path to AI sovereignty. This year showed it's the path to AI security, too.

]]>01M3TESBKM9T71XXXK1XMDP4PZIntroducing Workers KV Instant — powered by Quicksilverhttps://blog.cloudflare.com/workers-kv-instant/ Thu, 01 Oct 2026 13:00:00 GMTWorkers KV Instant delivers sub-2ms p99 read latencies and 250ms global replication across Cloudflare’s 300+ edge locations. KV Instant eliminates cold-read penalties and uses the familiar Workers KV API.Rob SutterBirthday WeekCloudflare Workers KVQuicksilverStorageToday, we’re introducing Workers KV Instant, a new mode for Workers KV that pushes your changes globally for instant availability without cold read penalties.

[Workers KV](https://developers.cloudflare.com/kv/) has been one of our most popular services on the Developer Platform since [launching during Birthday Week in 2018](https://blog.cloudflare.com/introducing-workers-kv/). It’s great for quickly accessing data like static assets and user configuration that is written occasionally but read frequently. We use it ourselves across many Cloudflare products.

We also have another key-value store, Quicksilver, which we’ve [blogged about](https://blog.cloudflare.com/quicksilver-v2-evolution-of-a-globally-distributed-key-value-store-part-1/) many times since [introducing it in 2020](https://blog.cloudflare.com/introducing-quicksilver-configuration-distribution-at-internet-scale/). We designed Quicksilver for incredibly fast global replication and low-latency access, and nearly every request to Cloudflare looks up at least one key in Quicksilver. People have asked us for years, but we’ve never made Quicksilver available to our customers.

We’re changing that today with Workers KV Instant. KV Instant mode provides the same API as Workers KV, but powers it using Quicksilver. KV Instant offers 100 times faster p99 reads and immediate updates, with no need to wait for a TTL to expire. It’s not for every type of data, but, for infrequently updated application configuration data — the same thing we use Quicksilver for ourselves — KV Instant shines. 

## 100x faster reads than Workers KV

KV Instant offers read latency that is over 100 times faster than classic mode, with reads resolving in under two milliseconds even at the 99th percentile of response time (p99), and 95th percentile (p95) times measured in microseconds. Writes are pushed to the edge over 20 times faster, with 99% of all writes replicating in around 250ms.

These high-performance characteristics of KV Instant make it ideal for reading data in the hot path of your applications, especially flags and settings that should be available globally nearly instantly after they’ve been written.

**Mode**| **p99 reads (cached)**| **p99 reads (all)**| **median write replication**| **p95 write replication**| **p99 write replication**  
---|---|---|---|---|---  
Instant| N/A| 1.62 ms| 107 ms (1)| 181ms (1)| 256 ms (1)  
Classic| 160 ms| 287 ms| < 1 s (2, 3)| < 1 s (2, 3)| 4.38 s (2)  
  
_Table notes:_

  1. _Time to replicate to all edge locations (over 300 as of publication)_
  2. _Time to replicate across all required storage backends_
  3.  _We do not have sub-second fidelity for replication lag in classic mode_



KV Instant is powered by [Quicksilver v2](https://blog.cloudflare.com/quicksilver-v2-evolution-of-a-globally-distributed-key-value-store-part-1/), a key-value store developed internally by Cloudflare to enable fast global replication and low-latency access on a planet scale.

## The same simple API as Workers KV — get(), put() list(), delete()

KV Instant uses the familiar [Workers KV API](https://developers.cloudflare.com/kv/api/) you build with today.

For example, let’s say you’re working on a big product launch, and need to be able to switch what’s on the homepage right at 10:13 AM when the product is introduced at the keynote on stage. You need some key that you can read, that introduces near zero latency, you can read on every request no matter the scale, and updates instantly when you change it.

Most binding operations are compatible with the Workers KV classic equivalents. There are three key differences when working with KV Instant:

  * You must specify KV Instant mode when creating a KV namespace. (pass the `”mode”`: `“instant”` attribute)
  * Metadata is not supported, so `getWithMetadata` calls always return `null` and there is no support for passing metadata in `put`.
  * `list` operations in KV Instant return _all_ matching keys in a namespace; there is no pagination.



For additional API examples, see [the Workers KV docs](https://developers.cloudflare.com/kv/api/read-key-value-pairs/).

## Pricing — reads cost 60% less than classic Workers KV

KV Instant is priced to fit the read-heavy, small data workloads it excels at serving. Because we propagate data to every Cloudflare location, using the same [Quicksilver](https://blog.cloudflare.com/quicksilver-v2-evolution-of-a-globally-distributed-key-value-store-part-1/) key-value store we’ve spent years learning how to operate at scale on the hot path of every request, we can offer pricing for reads that is 60% less than Workers KV, and much less than other global configuration products.

Conversely, storage and Class A operations are significantly more expensive than Workers KV. If you need to store large amounts of data, or update it frequently, Workers KV continues to be a great fit. Each mode is designed for a very different type of data and access pattern.

KV Instant namespaces are priced in three dimensions: data storage, class A operations, and class B operations.

| **Class B operations (reads)**| **Class A operations (put, delete, list)**| **Storage**  
---|---|---|---  
**Workers KV Instant**|  $0.20 per million| $0.10 per operation| $100 per MB, per month  
**Workers KV**|  $0.50 per million| $5.00 per million| $0.50 per GB, per month  
  
**Storage**

Storage is billed at $100 per MB, per month. Each key can be up to 300 bytes, and values can be any size that does not cause the namespace to exceed one megabyte in total size. KV Instant namespaces can contain up to 10,000 key value pairs of any type.

**Class A operations**

Class A operations (`put`, `delete`, and `list`) are charged at $0.10 per operation. Each key written or deleted counts as one Class A operation. Each list request counts as one Class A operation, _regardless of how many keys are returned in the response._ A single `list` operation can return all the key value pairs in a namespace in a single page.

Because writes must pass through a single system of record, KV Instant also restricts write frequency to one write per namespace per second. This is similar to classic Workers KV’s restriction of one write per key per second, and makes it easier for you to reason about update order in your application.

**Class B operations**

Class B operations (`get`) are charged at $0.20 per million keys requested, 60% **cheaper** than Workers KV default mode. When requesting multiple keys in a single `get` operation, each requested key is billed as one class B operation. For example, the following approaches both incur three class B operations and are equivalent from a billing perspective.

## Workers KV Instant is in private beta

KV Instant is launching today in private beta. We’re excited to start working with customers who want to try it, then open it up more widely, and would love to hear from you. You can sign up for the private beta [here](https://www.cloudflare.com/resource/workers-kv-instant-beta/). Tell us what you’re building!

]]>01M3VEGEH98DJT6FTGDT1MHP5MCloudflare OS: your company’s agent workspace, managed for youhttps://blog.cloudflare.com/managed-cloudflare-os/ Thu, 01 Oct 2026 13:00:00 GMTCloudflare OS gives everyone in your organization an agent workspace that knows how your company works and connects to its data and systems. We’re opening the waitlist for fully managed deployments that you’ll be able to launch in a few clicks.Phillip JonesAIBirthday WeekCloudflare OneDevelopersOpen SourceWorkers[Cloudflare OS](https://os.cloudflare.app/) gives everyone in your organization an agent workspace that knows how your company works and connects to its data and systems. Today, we're opening the [waitlist](http://cloudflare.com/resource/cloudflare-os-managed/) for fully managed Cloudflare OS deployments.

If I asked you to prepare for an important customer meeting later today, what would you do? You might learn how your company typically runs customer meetings, review the account in your CRM, check recent support tickets and product usage, then turn it into a short presentation to review with the group. Now imagine doing that another 100 times this month.

Every team has work like this. With Cloudflare OS, you can ask your agent to handle the work for you, build a tool for your team, or move between the two as the work evolves.

Last month, we [announced](https://blog.cloudflare.com/cloudflare-os/) Cloudflare OS and shared the [open source repository](https://github.com/cloudflare/cloudflare-os). Since then, thousands of organizations have started using it to work with company data, produce docs and slides, build tools for their teams, and automate work with agents.

With a few clicks in the Cloudflare dashboard, you’ll be able to launch your organization’s own agent workspace. Just tell us what custom domain you want to use, what [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) policies apply, and which [AI Gateway](https://www.cloudflare.com/products/ai-gateway/) to connect. We’ll handle the rest.

## Cloudflare OS, managed for you

Every company has its own terminology, procedures, systems, and requirements. We made Cloudflare OS [open source](https://github.com/cloudflare/cloudflare-os) so you can customize it around how your company works.

You can already deploy Cloudflare OS into your own Cloudflare account from the [open-source repository](https://github.com/cloudflare/cloudflare-os). That gives you full control, but it also means someone has to configure the deployment, operate it, and keep it up to date.

With the fully managed option, you decide who can access Cloudflare OS, which organizational skills and context are available, and which systems it can reach. You can leave the rest to us.

If you want Cloudflare OS fully managed for your organization, [join the waitlist](http://cloudflare.com/resource/cloudflare-os-managed/) and we’ll reach out.

## What’s new in Cloudflare OS

We’ve also spent the last month expanding what people and agents can do in Cloudflare OS. Here are a few highlights.

### Mount Git repos and work with code

When we launched Cloudflare OS, we focused first on work outside software development: creating documents and slides, automating tasks, and building collaborative tools. Agents could write code for an app, but they could not work with code in an existing Git repository.

You can now connect an existing GitHub repository to Cloudflare OS. Ask your agent to explore the codebase, fix a bug, add a feature, or open a pull request. It can search and edit files, review its changes, create commits, and push them to GitHub.

### Work across Google Workspace

For many organizations, work starts and ends in Google Workspace. Decisions live in email threads, context lives in Google Drive, analysis happens in Sheets, and teams coordinate through Calendar. Agents need to do work across those systems too.

We’ve made significant improvements to the Google Workspace [Gatekeeper](https://blog.cloudflare.com/cloudflare-os/#gatekeepers-govern-resources-and-actions) (a service-specific [Worker](https://developers.cloudflare.com/workers/?_gl=1*1pzndf6*_gcl_au*MzM2MDkxNTQzLjE3ODQ4NDczOTM.*_ga*MWVkZWU3OTctMzJjNC00YWE1LWI2ZDUtZTJkNTY1NzYxYWQ0*_ga_SQCRB0TXZW*czE3ODUyMTk3NjMkbzckZzAkdDE3ODUyMTk3NjMkajYwJGwwJGgwJGRQeHAyTUEtdzgtVUFETUEzOGwtVFVhajVDd2laRWYxSC1R&cf_page=cloudflare-os%2F) that sits between Cloudflare OS and an external service). Cloudflare OS can now read and research Gmail threads, create drafts, and send emails. You can also connect your entire Google Drive, a specific folder, or an individual doc or sheet.

### Export work in the formats your team uses

Work often needs to move into the formats your team already uses. Finance may need an Excel spreadsheet, and a report may need to become a PDF before sending to a customer.

The built-in document, presentation, and spreadsheet experiences can now export work to familiar formats. Depending on what you create, you can export to Microsoft Excel (.xlsx), CSV, PDF, Markdown, or HTML. Microsoft Word (.docx) and PowerPoint (.pptx) export is coming soon.

Tools you build can also define their own export formats. Tell the agent what you need, like “let me download this schedule as a calendar file (.ics)”, and it’ll add the option to the tool’s export menu.

## Sign up for the waitlist

Cloudflare OS is open source and available today. You can check out the [source code](https://github.com/cloudflare/cloudflare-os) or deploy it into your own Cloudflare account.

If you want Cloudflare OS fully managed for your organization, [join the waitlist](http://cloudflare.com/resource/cloudflare-os-managed/) and we’ll reach out with more information.

]]>01M3T6X21KEDC6DH8GGSGV13HRAnnouncing Cloudflare K2: serverless event streamshttps://blog.cloudflare.com/cloudflare-k2-streams/ Thu, 01 Oct 2026 13:00:00 GMTCloudflare K2 is a serverless event streaming service built directly on top of R2 object storage for high-scale data movement and long-term retention. By decoupling producers and consumers at the edge, K2 enables durable, ordered log streams without the operational overhead of traditional broker clusters.Micah WyldeMarc SelwanBirthday WeekDeveloper PlatformProduct NewsServerlessWorkersWith traditional Remote Procedure Call (RPC) architectures, there exists a core challenge: producers and consumers must align in scale and in time. If your producers send too much data for your consumers to handle or if your consumers or downstream services become unavailable, events are dropped. This problem is compounded with multiple consumers that need to independently process the data. For example, an ecommerce backend may emit events when transactions are completed, which need to be read by an analytics system and a fraud detection service.

We can solve this by _decoupling_ our producers and consumers — inserting a service in the middle that absorbs writes while allowing independent readers to consume at their own pace.

Today we are launching Cloudflare K2 in public beta to solve this problem. K2 is a durable event streaming primitive on the Developer Platform. You send events to a K2 stream, which stores them as an ordered log. Consumers can read them in a variety of ways, for example by splitting up reads across a set of consumers, or delivering all messages to all consumers. It's fully serverless, scales to vast quantities of data, and supports long-term retention, so even long periods of consumer downtime do not lose data.

Under the hood, K2 implements a partitioned, durable log on top of R2 object storage, which allows it to scale to huge volumes of storage.

If you’re ready to get started, you can create your first stream in seconds by following [the guide here](https://developers.cloudflare.com/k2/get-started/).

## Streams on the edge

We first built K2 because _we_ needed a durable buffer on the edge, initially to serve as the ingestion layer for [Basin Pipelines](https://developers.cloudflare.com/pipelines/). Pipelines is powered by a [stream processing engine](https://www.arroyo.dev) that operates on a pull-based model, which means some other system has to store events before they are read, transformed, and written to R2. And because we commit to never dropping events once they’re accepted into the Pipelines Stream, that storage has to be durable — meaning it can’t lose data — over potentially long periods of time.

This is where most companies would deploy Apache Kafka. However, Pipelines runs on the Cloudflare edge, which spans a huge number of servers across over 335 cities. Our unique architecture means we often cannot run traditional distributed systems software like Kafka, and need to rethink how these systems are built and operated.

For stateful services, in particular, Cloudflare’s global infrastructure presents some challenges: we get relatively small slices of machines, those machines are relatively ephemeral, and networking is often over the public Internet. But our infrastructure also has a few superpowers: it’s close to users wherever they are in the world and has an incredible capacity to scale horizontally.

In designing the durable buffering system that became K2, we decided to rely on the powerful state primitive we already have: R2. Object storage systems like R2 combine extremely durable storage ([11 9s!](https://developers.cloudflare.com/r2/reference/durability/)) with strongly consistent APIs. Offloading replication and consensus to the storage layer allows us to make the application layer (K2 in this case) radically simpler, cheaper, and higher performance. A secondary benefit is that it separates compute and storage, meaning each can be scaled independently. This allows us to store vast quantities of historical data at low cost.

How do we build a log on top of object storage? An immediate issue is that R2 — like other object stores — does not support appends, the standard operation on a log. Instead, we must write complete files, or segments, that are large enough to overcome the cost of writing and reading each one. We do this by first accumulating writes in-memory on an edge service. After waiting a short period for data to arrive, we write all events as a segment file. We achieve ordering and strictly incrementing offsets using R2’s atomic operations without needing a separate coordination service.

While building on R2 has many advantages, there is one downside: higher produce latencies. Writing to object storage is slower than a local disk, and we have to wait for the local batch to accumulate before starting the write. In our initial release of K2, this adds up to about 1 second of produce latency at the 99th percentile of response times.

We will be sharing more details on the design of K2 in an upcoming technical deep dive.

## Streams, Queues, or Pipelines?

Cloudflare has several existing asynchronous delivery primitives, including [Queues](https://developers.cloudflare.com/queues/) and [Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/). When should you reach for K2 instead of these existing products?

There are some superficial similarities between Queues and K2 Streams: both receive events, durably store them, and deliver them to consumers. Queues are designed around tracking individual items of expensive or time consuming work that need to be asynchronously completed. For example, an image processing application may enqueue a user request to be handled by the actual image processing service. They support complex logic on the grain of a particular work item, like retries, delays, and dead-letter queues for failed attempts.

K2, by contrast, is designed for high-scale data movement, long-term retention, and fan-out consumption. Messages are produced and consumed as batches — enabling efficient processing at the expense of message-level retries. This batching also drives higher producer latency than for queues.

Basin Pipelines is a serverless ingestion service. You can send your Pipeline JSON events, which can be transformed and written to R2 or a Basin Catalog. We recommend Pipelines when the end result is writing your events to object storage or Iceberg tables, and K2 when doing custom processing or writing to other destinations.

## Getting started

Using K2 involves first creating a stream. You can have many streams across your account for different use cases or types of events. Streams can be created via [cf](https://blog.cloudflare.com/cloudflare-cf-cli-launch/), Wrangler, the dashboard, or API.

Let's take the example of collecting and processing product analytics. First, we'll create a stream with cf:

Once we have a stream, we can start producing to it, via an HTTP API or Worker binding. For example, we can [configure a Worker binding](https://developers.cloudflare.com/k2/features/produce/#produce-from-a-worker) and then produce to it like this:

K2 represents data as bytes, so you can use whatever format or encoding makes sense for your application.

Now that we have events in a stream, we can create a subscription. Subscriptions divide up work between consumers, enabling _read parallelism_ — scaling out to multiple readers to handle more load than a single server can manage.

We can create a subscription via the HTTP API.

With the subscription created, we can then poll it from each of our consumers:

When a client calls `consume`, they receive a _lease_ for that particular batch of events for 5 minutes. The client can do one of three things:

  * _ack_ the batch, which marks it as processed and ensures it will not be redelivered
  *  _nack_ (negative ack) it, meaning we’ve failed to process it and would like it to be redelivered
  *  _extend_ its lease, in case it needs more time to complete processing



This is one way to consume from K2: splitting work amongst multiple consumers such that each consumer gets a portion of the data. Another way to read is with a separate subscription for each consumer — the pub/sub pattern — in which case each consumer sees all of the messages. Or you can mix-and-match between these two approaches, having multiple independent consumer pools.

See the [K2 docs](https://developers.cloudflare.com/k2/) for full details on the APIs.

## Pricing and Availability

K2 is available today in public beta for accounts with Workers Paid subscriptions, within these limits:

  * Maximum of 10GB of storage used
  * 30 MB/s produce per stream



If you need higher limits, please reach out to the team on Discord or fill out the [limit increase form](https://docs.google.com/forms/d/e/1FAIpQLSf1_eGOxXFGsh4O72fqdvDbYBjzpV3Q6Vf5X3fqpoTHObGFIA/viewform).

Usage of K2 will not be billed during the beta period. Once we begin billing, we anticipate this pricing:

| Pricing  
---|---  
Data Produced| $0.04 / GB  
Data Consumed| $0.04 / GB  
Data Retained| $0.02 / GB / month  
  
## What’s next

We have an exciting roadmap for K2 over the coming months, including:

  * Higher write parallelism, up to multi-GB/s streams
  * Message keys and key-based ordering guarantees
  * Push-based worker consumers
  * Express tier with lower produce and end-to-end latencies
  * Drop-in support for Apache Kafka clients



We’re excited to see what you build on K2! Share your feedback on the [Cloudflare Discord](https://discord.com/invite/cloudflaredev).

]]>01M3SXWQS68A0MY0GS33S6DJQJWe want you to build the next Git platform on Cloudflarehttps://blog.cloudflare.com/next-git-platform-on-cloudflare/ Thu, 01 Oct 2026 13:00:00 GMTCloudflare is hosting a competition to see who will build the next Git platform for an era of AI agents. Artifacts is in open beta, with Workers bindings, data jurisdiction controls, and event subscriptions for repository changes.Dina KozlovDillon MulroyZebulon PiaseckiBirthday WeekDevelopersWorkersGitHub was built for a world where humans write code, organize it into repositories, and collaborate through branches, commits, issues, and pull requests.

But the next generation of software is going to be built differently because it is going to be built by a different kind of developer: agents.

Agents are already writing more code than ever before — they’re fixing bugs, building features, writing tests, reviewing changes, updating dependencies, and doing the routine maintenance required to keep an application running.

So in this new world where you have hundreds, or even thousands, of agents working on the same codebase at the same time, what does the foundation look like?

How do agents know what other agents are working on? What happens when they make conflicting changes? How do you review everything they produce? How do you keep track of not just what changed, but _why_ a change was made?

And so the burning question is: **What does the next GitHub look like?**

We want you to help us answer it, by building it out.

Earlier this year, we launched [Artifacts](https://blog.cloudflare.com/artifacts-git-for-agents-beta/), a versioned filesystem that speaks Git and can scale to millions of repositories. From the start, we designed Artifacts as a set of programmable primitives that developers could use to build their own products, workflows, and abstractions.

Artifacts provides the foundation: repositories that can be created and forked programmatically, versioned storage for code and agent context, and the Git operations agents already know how to use.

With that foundation in place, you can focus on the layer above it: how agents coordinate their work, how changes are reviewed and merged, and what the developer experience should look like when hundreds or thousands of agents are working on the same codebase.

That is the layer we want you to build.

Now that Artifacts is in open beta, [we’re holding a competition](http://cloudflare.com/git-competition) to see who can build the next Git platform on Cloudflare using Workers and Artifacts.

## Artifacts is in open beta. Here’s why you should build on it

When we launched Artifacts, our goal was to make it possible to create a repository for every agent, session, task, or user — and to do that at the scale agents require.

Since then, we’ve seen developers use Artifacts in a range of ways: Vibe-coding platforms are using it to store the projects their users create. Developers are using it to persist the code and context from agent sessions. Others are creating isolated repositories, so multiple agents can safely work from the same starting point and compare or merge the results later.

Here are some new capabilities we’ve added since the initial launch.

### Deploy Artifacts repos to Workers

You can now connect an Artifacts repository to a Worker through [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/artifacts-integration/). When you or an agent pushes code to the Artifacts repository, Cloudflare will build the project and, for the production branch, deploy the updated Worker. Pushes to other branches automatically create or update [Workers Previews](https://developers.cloudflare.com/workers/previews/), giving you an isolated, shareable version of your Worker where you can test changes before they go live.

You can connect an existing Worker to an Artifacts repository or start a new project and automatically store it in Artifacts.

### Manage Artifacts directly from Workers

You can interact with Artifacts repositories directly from a Worker using an [Artifacts binding](https://developers.cloudflare.com/artifacts/api/workers-binding/) to create or fork repos, inspect files and commits, and issue repo-scoped Git tokens. This makes your Git workflow programmable. When a new task arrives, a Worker can fork the project for an agent, read the files it needs for context, and give it a repository to work in. When the agent pushes a change, your automation can inspect the result and start a review. You define those steps in code to fit how your agents work.

For example, here’s how to fork a project for a new agent task and read its `AGENTS.md` for instructions:

### React to every change with event subscriptions

Artifacts publishes events whenever a repository is created, imported, forked, deleted, pushed to, cloned, or fetched. You can subscribe to these events to decide what happens next: run CI, kick off a code review agent, or deploy a change.

For example, you can subscribe to Artifacts push events and have a Worker start a code review workflow for each push. The Worker passes the repository, branch, and new commit to the Workflow, giving a review agent the context it needs to inspect the change:

### Data jurisdiction for Artifacts repos

You can now [choose where Artifacts stores and processes](https://developers.cloudflare.com/artifacts/guides/data-localization/) your repository data. Set a U.S. or EU jurisdiction when you create a namespace, and every repository created in that namespace will automatically follow the same restriction.

### View Artifacts metrics

You can now see metrics for your Artifacts repositories in the Cloudflare dashboard. For each repository, you can now see total operations, pulls, pushes, errors, and error rate, helping you understand how the repository is being used and spot failures. You can also query [Artifacts metrics](https://developers.cloudflare.com/artifacts/observability/metrics/) directly to build your own dashboards or monitoring.

### Pricing

Artifacts pricing is based on repository operations and the amount of data stored. We will begin billing for Artifacts usage on October 15, 2026.

## Competition: Build the next Git platform on Cloudflare

We want you to build your vision for the Git platform of the agentic era using Cloudflare Workers and Artifacts.

You could rethink repositories, branches, pull requests, worktrees, code review, and merge conflicts — or build new ways to preserve agent context, compare multiple changes at the same time, and decide which one should ship.

We aren’t looking for GitHub as it exists today with agents added on top. At a minimum, we want to see multiple agents working on changes concurrently. Beyond that, we want you to get creative — what you think comes next.

### How to enter

Submit:

  * A 5-10 minute video demonstrating what you built, what it enables agents and developers to do, and how it works
  * A link to the source code, which must be provided under a permissive open source license (MIT, Apache, BSD)
  * Instructions for running or trying the project



### Deadline

[Submissions](http://cloudflare.com/git-competition) are open until October 14, 2026.

### Why should you participate?

We’ll select the top three projects and fly up to two members from each team to San Francisco to attend [Cloudflare Connect](https://www.cloudflare.com/connect/) and show what they built.

The first-place team will also receive $25,000 in Cloudflare credits, along with invitations to the VIP speaker dinner on Monday night at Connect.

## Get started

Artifacts is available in open beta to customers on the Workers Paid plan.

Get started with your coding agent:**** copy the prompt below to set up your first Artifacts repository and start pushing code to it.

**Copy prompt**
    
    
    Set me up with Cloudflare Artifacts so I can start pushing code to my first repository. Read https://developers.cloudflare.com/artifacts/llms.txt and https://developers.cloudflare.com/cf/llms.txt for current instructions. Use the Cloudflare cf CLI, installing it if needed. Help me authenticate, confirm my account and namespace, and verify Artifacts access. Create a new TypeScript Worker project with an ARTIFACTS binding and use it locally to create a repository on Cloudflare. Push an initial README commit and clone the repository separately to verify it works. Give me the repository's Git remote and instructions for pushing my own code. Keep credentials out of source control, Git configuration, remote URLs, and logs. Do not deploy or change billing settings. Stop the local server afterward. If anything fails, explain the blocker rather than claiming setup is complete.

You can view or create the Artifacts repositories in the [dashboard](https://dash.cloudflare.com/?to=/:account/workers/artifacts) or if you’re looking to learn more, check out the [documentation](https://developers.cloudflare.com/artifacts/).

]]>01M3SQCB0ZE7ZPK6M13HGY41T3
