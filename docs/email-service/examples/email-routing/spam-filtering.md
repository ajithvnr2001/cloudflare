---
url: https://developers.cloudflare.com/email-service/examples/email-routing/spam-filtering/
title: Spam filtering \u00b7 Cloudflare Email Service docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:13.751042+00:00
---

# Spam filtering · Cloudflare Email Service docs

> Source: https://developers.cloudflare.com/email-service/examples/email-routing/spam-filtering/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Email Service](https://developers.cloudflare.com/email-service/)
  3. /…

Examples

  4. /Email routing
  5. /Spam filtering



# Spam filtering

Implement intelligent spam detection with keyword analysis, domain reputation, and machine learning techniques

Last updated Jun 9, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/email-service/examples/email-routing/spam-filtering/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBasic spam filterAdvanced spam detection with AINext steps

Build spam filtering systems with keyword matching, domain validation, and intelligent detection methods for effective email security.

## Basic spam filter

Simple spam detection with keyword matching and domain validation:
    
    
    interface Env {
    	EMAIL: SendEmail;
    	EMAIL_ANALYTICS: AnalyticsEngine;
    }
    
    interface SpamFilter {
    	checkSpam(
    		message: any,
    	): Promise<{ isSpam: boolean; score: number; reasons: string[] }>;
    }
    
    class SimpleSpamFilter implements SpamFilter {
    	private spamKeywords = [
    		"buy now",
    		"limited time",
    		"act fast",
    		"click here",
    		"free money",
    		"guaranteed",
    		"risk free",
    		"urgent",
    		"winner",
    		"congratulations",
    		"inheritance",
    		"lottery",
    	];
    
    	private trustedDomains = ["example.com", "trusted-partner.com", "vendor.net"];
    
    	async checkSpam(
    		message,
    	): Promise<{ isSpam: boolean; score: number; reasons: string[] }> {
    		let score = 0;
    		const reasons = [];
    
    		const sender = message.from;
    		const subject = message.headers.get("subject") || "";
    		const senderDomain = sender.split("@")[1];
    
    		// Check sender domain
    		if (this.trustedDomains.includes(senderDomain)) {
    			score -= 2; // Trusted sender
    		}
    
    		// Check subject for spam keywords
    		const subjectLower = subject.toLowerCase();
    		for (const keyword of this.spamKeywords) {
    			if (subjectLower.includes(keyword)) {
    				score += 1;
    				reasons.push(`Spam keyword: ${keyword}`);
    			}
    		}
    
    		// Check for excessive capitalization
    		const capsRatio = (subject.match(/[A-Z]/g) || []).length / subject.length;
    		if (capsRatio > 0.7 && subject.length > 10) {
    			score += 1;
    			reasons.push("Excessive capitalization");
    		}
    
    		// Check for suspicious patterns
    		if (subject.includes("!!!") || subject.includes("$$$")) {
    			score += 1;
    			reasons.push("Suspicious punctuation");
    		}
    
    		// Check for suspicious sender patterns
    		if (
    			sender.includes("noreply") &&
    			subject.toLowerCase().includes("urgent")
    		) {
    			score += 2;
    			reasons.push("Suspicious noreply + urgent combination");
    		}
    
    		return {
    			isSpam: score >= 2,
    			score,
    			reasons,
    		};
    	}
    }
    
    const spamFilter = new SimpleSpamFilter();
    
    export default {
    	async email(message, env, ctx): Promise<void> {
    		const startTime = Date.now();
    
    		// Check for spam
    		const spamCheck = await spamFilter.checkSpam(message);
    
    		// Track spam check metrics
    		env.EMAIL_ANALYTICS?.writeDataPoint({
    			blobs: [
    				"spam_check_completed",
    				message.from,
    				message.to,
    				spamCheck.isSpam ? "spam" : "legitimate",
    			],
    			doubles: [
    				1, // Count
    				spamCheck.score,
    				Date.now() - startTime,
    			],
    			indexes: [
    				`spam_detected:${spamCheck.isSpam}`,
    				`score_range:${getScoreRange(spamCheck.score)}`,
    			],
    		});
    
    		if (spamCheck.isSpam) {
    			console.log(
    				`Rejected spam email from ${message.from}: ${spamCheck.reasons.join(", ")}`,
    			);
    			message.setReject(`Message rejected: ${spamCheck.reasons[0]}`);
    			return;
    		}
    
    		// Add spam score headers and forward
    		const headers = new Headers();
    		headers.set("X-Spam-Score", spamCheck.score.toString());
    		headers.set("X-Spam-Reasons", spamCheck.reasons.join(", "));
    		headers.set("X-Spam-Check-Time", (Date.now() - startTime).toString());
    
    		await message.forward("inbox@example.com", headers);
    	},
    };
    
    function getScoreRange(score: number): string {
    	if (score < 0) return "trusted";
    	if (score === 0) return "neutral";
    	if (score === 1) return "suspicious";
    	return "spam";
    }

## Advanced spam detection with AI

For more sophisticated spam detection, you can enhance the basic filter using [Workers AI](https://developers.cloudflare.com/workers-ai/) to analyze email content with machine learning models. This approach can identify subtle spam patterns that keyword-based filters might miss.

## Next steps

  * [Email handler](https://developers.cloudflare.com/email-service/api/route-emails/email-handler/) — reference for `setReject()` and `forward()` actions used here.
  * [Hard bounce handling](https://developers.cloudflare.com/email-service/examples/email-routing/hard-bounce-handling/) — detect bounce notifications that often originate from spam infrastructure.
  * [Email storage and processing](https://developers.cloudflare.com/email-service/examples/email-routing/email-storage/) — log filtered emails to KV for later review.



[PreviousEmail storage and processing](https://developers.cloudflare.com/email-service/examples/email-routing/email-storage/)[NextHandle hard bounce emails](https://developers.cloudflare.com/email-service/examples/email-routing/hard-bounce-handling/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/email-service/examples/email-routing/spam-filtering.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
