---
url: https://developers.cloudflare.com/ai-gateway/features/
title: Features \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:29.437574+00:00
---

# Features · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/features/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /Features



# Features

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/features/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCore Features Performance & Cost Optimization Security & Safety Observability & Analytics Advanced ConfigurationFeature Comparison by Use CaseGetting Started with Features

AI Gateway provides a comprehensive set of features to help you build, deploy, and manage AI applications with confidence. From performance optimization to security and observability, these features work together to create a robust AI infrastructure.

## Core Features

### Performance & Cost Optimization

[Caching](https://developers.cloudflare.com/ai-gateway/features/caching/)

Serve identical requests directly from Cloudflare's global cache, reducing latency by up to 90% and significantly cutting costs by avoiding repeated API calls to AI providers.

**Key benefits:**

  * Reduced response times for repeated queries
  * Lower API costs through cache hits
  * Configurable TTL and per-request cache control
  * Works across all supported AI providers



Use Caching

[Spend Limits](https://developers.cloudflare.com/ai-gateway/features/spend-limits/)

Set cost-based budgets that track cumulative dollar spend across requests. Scope limits by model, provider, or custom metadata dimensions like user, team, or application.

**Key benefits:**

  * Per-provider or per-model budgets
  * Per-user or per-team budgets using [custom metadata](https://developers.cloudflare.com/ai-gateway/observability/custom-metadata/)
  * Configurable time windows (daily, weekly, monthly)
  * Automatic request blocking when budget is exceeded



Use Spend Limits

[Rate Limiting](https://developers.cloudflare.com/ai-gateway/features/rate-limiting/)

Control application scaling and protect against abuse with flexible rate limiting options. Set limits based on requests per time window with sliding or fixed window techniques.

**Key benefits:**

  * Prevent API quota exhaustion
  * Control costs and usage patterns
  * Configurable per gateway or per request
  * Multiple rate limiting techniques available



Use Rate Limiting

[Auto Router](https://developers.cloudflare.com/ai-gateway/features/auto-router/)

Automatically route each request to the most cost-effective model that can handle the task while maintaining response quality.

**Key benefits:**

  * Content-aware model selection
  * Cost optimization across models
  * Automatic fallback when a model is unavailable
  * Session affinity to support caching



Use Auto Router

[Dynamic Routing](https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/)

Create sophisticated request routing flows without code changes. Route requests based on user segments, geography, content analysis, or A/B testing requirements through a visual interface.

**Key benefits:**

  * Visual flow-based configuration
  * User-based and geographic routing
  * A/B testing and fractional traffic splitting
  * Context-aware routing based on request content
  * Dynamic rate limiting with automatic fallbacks



Use Dynamic Routing

### Security & Safety

[Guardrails](https://developers.cloudflare.com/ai-gateway/features/guardrails/)

Deploy AI applications safely with real-time content moderation. Automatically detect and block harmful content in both user prompts and model responses across all providers.

**Key benefits:**

  * Consistent moderation across all AI providers
  * Real-time prompt and response evaluation
  * Configurable content categories and actions
  * Compliance and audit capabilities
  * Enhanced user safety and trust



Use Guardrails

[Data Loss Prevention (DLP)](https://developers.cloudflare.com/ai-gateway/features/dlp/)

Protect your organization from inadvertent exposure of sensitive data through AI interactions. Scan prompts and responses for PII, financial data, and other sensitive information.

**Key benefits:**

  * Real-time scanning of AI prompts and responses
  * Detection of PII, financial, healthcare, and custom data patterns
  * Configurable actions: flag or block sensitive content
  * Integration with Cloudflare's enterprise DLP solution
  * Compliance support for GDPR, HIPAA, and PCI DSS



Use Data Loss Prevention (DLP)

[Authentication](https://developers.cloudflare.com/ai-gateway/configuration/authentication/)

Secure your AI Gateway with token-based authentication. Control access to your gateways and protect against unauthorized usage.

**Key benefits:**

  * Token-based access control
  * Configurable per gateway
  * Integration with Cloudflare's security infrastructure
  * Audit trail for access attempts



Use Authentication

[Bring Your Own Keys (BYOK)](https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/)

Securely store and manage AI provider API keys in Cloudflare's encrypted infrastructure. Remove hardcoded keys from your applications while maintaining full control.

**Key benefits:**

  * Encrypted key storage at rest and in transit
  * Centralized key management across providers
  * Easy key rotation without code changes
  * Support for 20+ AI providers
  * Enhanced security and compliance



Use Bring Your Own Keys (BYOK)

### Observability & Analytics

[Analytics](https://developers.cloudflare.com/ai-gateway/observability/analytics/)

Gain deep insights into your AI application usage with comprehensive analytics. Track requests, tokens, costs, errors, and performance across all providers.

**Key benefits:**

  * Real-time usage metrics and trends
  * Cost tracking and estimation across providers
  * Error monitoring and troubleshooting
  * Cache hit rates and performance insights
  * GraphQL API for custom dashboards



Use Analytics

[Logging](https://developers.cloudflare.com/ai-gateway/observability/logging/)

Capture detailed logs of all AI requests and responses for debugging, compliance, and analysis. Configure log retention and export options.

**Key benefits:**

  * Complete request/response logging
  * Configurable log retention policies
  * Export capabilities via Logpush
  * Custom metadata support
  * Compliance and audit support



Use Logging

[Custom Metadata](https://developers.cloudflare.com/ai-gateway/observability/custom-metadata/)

Enrich your logs and analytics with custom metadata. Tag requests with user IDs, team information, or any custom data for enhanced filtering and analysis.

**Key benefits:**

  * Enhanced request tracking and filtering
  * User and team-based analytics
  * Custom business logic integration
  * Improved debugging and troubleshooting



Use Custom Metadata

### Advanced Configuration

[Custom Costs](https://developers.cloudflare.com/ai-gateway/configuration/custom-costs/)

Override default pricing with your negotiated rates or custom cost models. Apply custom costs at the request level for accurate cost tracking.

**Key benefits:**

  * Accurate cost tracking with negotiated rates
  * Per-request cost customization
  * Better budget planning and forecasting
  * Support for enterprise pricing agreements



Use Custom Costs

## Feature Comparison by Use Case

Use Case | Recommended Features  
---|---  
**Cost Optimization** | Caching, Auto Router, Spend Limits, Rate Limiting, Custom Costs  
**High Availability** | Fallbacks using Dynamic Routing  
**Security & Compliance** | Guardrails, DLP, Authentication, BYOK, Logging  
**Performance Monitoring** | Analytics, Logging, Custom Metadata  
**A/B Testing** | Dynamic Routing, Custom Metadata, Analytics  
  
## Getting Started with Features

  1. **Start with the basics** : Enable [Caching](https://developers.cloudflare.com/ai-gateway/features/caching/) and [Analytics](https://developers.cloudflare.com/ai-gateway/observability/analytics/) for immediate benefits
  2. **Add reliability** : Configure Fallbacks and Rate Limiting using [Dynamic routing](https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/)
  3. **Enhance security** : Implement [Guardrails](https://developers.cloudflare.com/ai-gateway/features/guardrails/), [DLP](https://developers.cloudflare.com/ai-gateway/features/dlp/), and [Authentication](https://developers.cloudflare.com/ai-gateway/configuration/authentication/)



* * *

_All features work seamlessly together and across all 20+ supported AI providers. Get started with[AI Gateway](https://developers.cloudflare.com/ai-gateway/get-started/) to begin using these features in your applications._

[PreviousNon-realtime WebSockets API](https://developers.cloudflare.com/ai-gateway/usage/websockets-api/non-realtime-api/)[NextUnified Billing](https://developers.cloudflare.com/ai-gateway/features/unified-billing/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/features/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
