---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/
title: Fields reference \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:02.589255+00:00
---

# Fields reference · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules language](https://developers.cloudflare.com/ruleset-engine/rules-language/)

  4. /[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)
  5. /Fields reference



# Fields reference

Last updated Aug 12, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

CategoriesBodyBotsGeolocationHeadersJWT validationRaw fieldsRequestResponseSSL/TLSURImTLS

[cf.api_gateway.auth_id_presentIndicates whether the request contained an API session authentication token, as defined by API Shield's saved session identifiers.

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.api_gateway.auth_id_present/)[cf.api_gateway.fallthrough_detectedIndicates whether the request matched a saved endpoint in Endpoint Management.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.api_gateway.fallthrough_detected/)[cf.bot_management.corporate_proxyIndicates whether the incoming request comes from an identified Enterprise-only cloud-based corporate proxy or secure web gateway.

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.bot_management.corporate_proxy/)[cf.bot_management.detection_idsList of IDs that correlate to the Bot Management heuristic detections made on a request.

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.bot_management.detection_ids/)[cf.bot_management.ja3_hashProvides an SSL/TLS fingerprint to help you identify potential bot requests.

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.bot_management.ja3_hash/)[cf.bot_management.ja4Provides an SSL/TLS fingerprint to help you identify potential bot requests.

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.bot_management.ja4/)[cf.bot_management.js_detection.passedIndicates whether the visitor has previously passed a JS Detection.

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.bot_management.js_detection.passed/)[cf.bot_management.scoreRepresents the likelihood that a request originates from a bot using a score from 1–99.

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.bot_management.score/)[cf.bot_management.signed_agentIndicates whether or not the request originated from a known agent that self-identifies with Web Bot Auth, now classified as a verified bot or agent labeled as intermediary.

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.bot_management.signed_agent/)[cf.bot_management.static_resourceIndicates whether static resources should be included when you create a rule using `cf.bot_management.score`.

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.bot_management.static_resource/)[cf.bot_management.tagsProvides the tags associated with bot traffic.

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.bot_management.tags/)[cf.bot_management.verified_botIndicates whether the request originated from a known good bot or crawler.

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.bot_management.verified_bot/)[cf.client.botIndicates whether the request originated from a known good bot or crawler.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.client.bot/)[cf.edge.client_tcpIndicates if the request was made over TCP.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.edge.client_tcp/)[cf.edge.l4.delivery_rateThe most recent data delivery rate estimate for the client connection, in bytes per second.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.edge.l4.delivery_rate/)[cf.edge.server_ipRepresents the global network's IP address to which the HTTP request has resolved.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.edge.server_ip/)[cf.edge.server_portRepresents the port number at which the Cloudflare global network received the request.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.edge.server_port/)[cf.hostname.metadataReturns the string representation of the per-hostname custom metadata JSON object set by SSL for SaaS customers.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.hostname.metadata/)[cf.llm.prompt.custom_topic_categoriesA map of custom topic labels to relevance scores (1–99) for the LLM prompt in the request.

  * Enterprise

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.custom_topic_categories/)[cf.llm.prompt.detectedIndicates whether Cloudflare detected an LLM prompt in the incoming request.

  * Enterprise

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.detected/)[cf.llm.prompt.injection_scoreA score from 1–99 that represents the likelihood that the LLM prompt in the request is trying to perform a prompt injection attack.

  * Enterprise

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.injection_score/)[cf.llm.prompt.pii_categoriesArray of string values with the personally identifiable information (PII) categories found in the LLM prompt included in the request.

  * Enterprise

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.pii_categories/)[cf.llm.prompt.pii_detectedIndicates whether any personally identifiable information (PII) has been detected in the LLM prompt included in the request.

  * Enterprise

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.pii_detected/)[cf.llm.prompt.token_countAn estimated token count for the LLM prompt in the request.

  * Enterprise

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.token_count/)[cf.llm.prompt.unsafe_topic_categoriesArray of string values with the type of unsafe topics detected in the LLM prompt.

  * Enterprise

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.unsafe_topic_categories/)[cf.llm.prompt.unsafe_topic_detectedIndicates whether the incoming request includes any unsafe topic category in the LLM prompt.

  * Enterprise

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.unsafe_topic_detected/)[cf.random_seedReturns per-request random bytes that you can use in the `uuidv4()` function.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.random_seed/)[cf.ray_idThe Ray ID of the current request.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.ray_id/)[cf.response.1xxx_codeContains the specific code for 1XXX Cloudflare errors.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.response.1xxx_code/)[cf.response.error_typeA string with the type of error in the response being returned.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.response.error_type/)[cf.schema_validation.learned.body.violated_parametersThe JSON path of a detected request body violation of the learned schema.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.schema_validation.learned.body.violated_parameters/)[cf.schema_validation.learned.cookies.violated_parametersNames of cookies detected as violating the learned schema.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.schema_validation.learned.cookies.violated_parameters/)[cf.schema_validation.learned.headers.violated_parametersNames of request headers detected as violating the learned schema.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.schema_validation.learned.headers.violated_parameters/)[cf.schema_validation.learned.path.violated_parametersNames of path parameters detected as violating the learned schema.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.schema_validation.learned.path.violated_parameters/)[cf.schema_validation.learned.query.undeclared_parametersNames of query parameters detected in the request but not declared in the learned schema.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.schema_validation.learned.query.undeclared_parameters/)[cf.schema_validation.learned.query.violated_parametersNames of query parameters detected as violating the learned schema.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.schema_validation.learned.query.violated_parameters/)[cf.schema_validation.learned.violatedReturns `true` when an evaluated request violates the learned profile.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.schema_validation.learned.violated/)[cf.schema_validation.uploaded.body.violated_parametersThe JSON path of a detected request body violation of the uploaded schema.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.schema_validation.uploaded.body.violated_parameters/)[cf.schema_validation.uploaded.cookies.violated_parametersNames of cookies detected as violating the uploaded schema.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.schema_validation.uploaded.cookies.violated_parameters/)[cf.schema_validation.uploaded.headers.violated_parametersNames of request headers detected as violating the uploaded schema.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.schema_validation.uploaded.headers.violated_parameters/)[cf.schema_validation.uploaded.path.violated_parametersNames of path parameters detected as violating the uploaded schema.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.schema_validation.uploaded.path.violated_parameters/)[cf.schema_validation.uploaded.query.undeclared_parametersNames of query parameters detected in the request but not declared in the uploaded schema.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.schema_validation.uploaded.query.undeclared_parameters/)[cf.schema_validation.uploaded.query.violated_parametersNames of query parameters detected as violating the uploaded schema.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.schema_validation.uploaded.query.violated_parameters/)[cf.schema_validation.uploaded.violatedReturns `true` when an evaluated request violates the supplied schema.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.schema_validation.uploaded.violated/)[cf.threat_scoreRepresents a Cloudflare threat score.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.threat_score/)[cf.timings.client_quic_rtt_msecThe smoothed QUIC round-trip time (RTT) between Cloudflare and the client in milliseconds.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.timings.client_quic_rtt_msec/)[cf.timings.client_tcp_rtt_msecThe smoothed TCP round-trip time (RTT) between Cloudflare and the client in milliseconds.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.timings.client_tcp_rtt_msec/)[cf.timings.edge_msecThe time spent processing a request within the Cloudflare global network in milliseconds.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.timings.edge_msec/)[cf.timings.origin_ttfb_msecThe round-trip time (RTT) between the Cloudflare global network and the origin server in milliseconds.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.timings.origin_ttfb_msec/)[cf.timings.worker_msecThe time spent executing a Cloudflare Worker in milliseconds.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.timings.worker_msec/)[cf.tls_cipherThe cipher for the connection to Cloudflare.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_cipher/)[cf.tls_ciphers_sha1The SHA-1 fingerprint of the client TLS cipher list in received order, encoded in Base64 using big-endian format.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_ciphers_sha1/)[cf.tls_client_auth.cert_chain_rfc9440The mTLS client certificate chain (excluding the leaf certificate) encoded as a structured field list per RFC 9440.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_chain_rfc9440/)[cf.tls_client_auth.cert_chain_rfc9440_too_largeReturns `true` when the RFC 9440 encoded client certificate chain exceeds the 16 KiB size limit.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_chain_rfc9440_too_large/)[cf.tls_client_auth.cert_fingerprint_sha1The SHA-1 fingerprint of the mTLS client certificate.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_fingerprint_sha1/)[cf.tls_client_auth.cert_fingerprint_sha256The SHA-256 fingerprint of the mTLS client certificate.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_fingerprint_sha256/)[cf.tls_client_auth.cert_issuer_dnThe Distinguished Name (DN) of the Certificate Authority (CA) that issued the mTLS client certificate.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_issuer_dn/)[cf.tls_client_auth.cert_issuer_dn_legacyThe Distinguished Name (DN) of the Certificate Authority (CA) that issued the mTLS client certificate in a legacy format.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_issuer_dn_legacy/)[cf.tls_client_auth.cert_issuer_dn_rfc2253The Distinguished Name (DN) of the Certificate Authority (CA) that issued the mTLS client certificate in RFC 2253 format.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_issuer_dn_rfc2253/)[cf.tls_client_auth.cert_issuer_serialSerial number of the direct issuer of the mTLS client certificate.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_issuer_serial/)[cf.tls_client_auth.cert_issuer_skiThe Subject Key Identifier (SKI) of the direct issuer of the mTLS client certificate.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_issuer_ski/)[cf.tls_client_auth.cert_not_afterThe mTLS client certificate is not valid after this date.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_not_after/)[cf.tls_client_auth.cert_not_beforeThe mTLS client certificate is not valid before this date.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_not_before/)[cf.tls_client_auth.cert_presentedReturns `true` when an mTLS client presents a certificate (valid or not).](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_presented/)[cf.tls_client_auth.cert_revokedIndicates whether the mTLS client presented a valid but revoked client certificate.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_revoked/)[cf.tls_client_auth.cert_rfc9440The mTLS client certificate encoded as a Structured Fields Byte Sequence per RFC 9440.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_rfc9440/)[cf.tls_client_auth.cert_rfc9440_too_largeReturns `true` when the RFC 9440 encoded mTLS client certificate exceeds the 10 KiB size limit.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_rfc9440_too_large/)[cf.tls_client_auth.cert_serialSerial number of the mTLS client certificate.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_serial/)[cf.tls_client_auth.cert_skiThe Subject Key Identifier (SKI) of the mTLS client certificate.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_ski/)[cf.tls_client_auth.cert_subject_dnThe Distinguished Name (DN) of the owner (or requester) of the mTLS client certificate.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_subject_dn/)[cf.tls_client_auth.cert_subject_dn_legacyThe Distinguished Name (DN) of the owner (or requester) of the mTLS client certificate in a legacy format.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_subject_dn_legacy/)[cf.tls_client_auth.cert_subject_dn_rfc2253The Distinguished Name (DN) of the owner (or requester) of the mTLS client certificate in RFC 2253 format.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_subject_dn_rfc2253/)[cf.tls_client_auth.cert_verifiedReturns `true` when an mTLS client presents a valid client certificate.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_verified/)[cf.tls_client_extensions_sha1The SHA-1 fingerprint of TLS client extensions, encoded in Base64 using big-endian format.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_extensions_sha1/)[cf.tls_client_extensions_sha1_leThe SHA-1 fingerprint of TLS client extensions, encoded in Base64 using little-endian format.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_extensions_sha1_le/)[cf.tls_client_hello_lengthThe length of the client hello message sent in a TLS handshake.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_hello_length/)[cf.tls_client_randomThe value of the 32-byte random value provided by the client in a TLS handshake, encoded in Base64.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_client_random/)[cf.tls_versionThe TLS version of the connection to Cloudflare.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.tls_version/)[cf.verified_bot_categoryProvides the type and purpose of a verified bot.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.verified_bot_category/)[cf.waf.auth_detectedIndicates whether the Cloudflare WAF detected authentication credentials in the request.

  * Enterprise

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.auth_detected/)[cf.waf.content_scan.has_failedIndicates whether the file scanner was unable to scan any of the content objects detected in the request.

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.content_scan.has_failed/)[cf.waf.content_scan.has_malicious_objIndicates whether the request contains at least one malicious content object.

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.content_scan.has_malicious_obj/)[cf.waf.content_scan.has_objIndicates whether the request contains at least one content object.

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.content_scan.has_obj/)[cf.waf.content_scan.num_malicious_objThe number of malicious content objects detected in the request (zero or greater).

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.content_scan.num_malicious_obj/)[cf.waf.content_scan.num_objThe number of content objects detected in the request (zero or greater).

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.content_scan.num_obj/)[cf.waf.content_scan.obj_resultsAn array of scan results in the order the content objects were detected in the request.

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.content_scan.obj_results/)[cf.waf.content_scan.obj_sizesAn array of file sizes in bytes, in the order the content objects were detected in the request.

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.content_scan.obj_sizes/)[cf.waf.content_scan.obj_typesAn array of file types in the order the content objects were detected in the request.

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.content_scan.obj_types/)[cf.waf.content_scan.truncatedIndicates whether the request body exceeded the size limit for content scanning and was truncated before scanning.

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.content_scan.truncated/)[cf.waf.credential_check.password_leakedIndicates whether the password detected in the request was previously leaked.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.credential_check.password_leaked/)[cf.waf.credential_check.username_and_password_leakedIndicates whether the auth credentials detected in the request (username-password pair) were previously leaked.

  * Pro or above

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.credential_check.username_and_password_leaked/)[cf.waf.credential_check.username_leakedIndicates whether the username detected in the request was previously leaked.

  * Enterprise

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.credential_check.username_leaked/)[cf.waf.credential_check.username_password_similarIndicates whether a similar version of the username and password credentials detected in the request were previously leaked.

  * Enterprise

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.credential_check.username_password_similar/)[cf.waf.scoreA global score from 1–99 that combines the score of each WAF attack vector into a single score.

  * Enterprise

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.score/)[cf.waf.score.classThe attack score class of the current request, based on the WAF attack score.

  * Business or above

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.score.class/)[cf.waf.score.rceAn attack score from 1–99 classifying the command injection or Remote Code Execution (RCE) attack vector.

  * Enterprise

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.score.rce/)[cf.waf.score.sqliAn attack score from 1–99 classifying the SQL injection (SQLi) attack vector.

  * Enterprise

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.score.sqli/)[cf.waf.score.xssAn attack score from 1–99 classifying the cross-site scripting (XSS) attack vector.

  * Enterprise

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.score.xss/)[cf.waf.signature.request.categoriesAn array of categories associated with attack signatures that matched the request.

  * Early Access

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.signature.request.categories/)[cf.waf.signature.request.confidenceAn array of confidence values associated with attack signatures that matched the request.

  * Early Access

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.signature.request.confidence/)[cf.waf.signature.request.refsAn array containing up to 10 Refs for attack signatures that matched the request.

  * Early Access

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.signature.request.refs/)[cf.web_asset.labelsAn array of labels associated with the operation matched by the request.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.web_asset.labels/)[cf.worker.upstream_zoneIdentifies whether a request comes from a worker or not.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.worker.upstream_zone/)[http.cookieThe entire cookie as a string.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.cookie/)[http.hostThe hostname used in the full request URI.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.host/)[http.refererThe HTTP `Referer` request header, which contains the address of the web page that linked to the currently requested page.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.referer/)[http.request.accepted_languagesList of language tags provided in the `Accept-Language` HTTP request header.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.accepted_languages/)[http.request.body.formThe HTTP request body of a form represented as a Map (or associative array).

  * Enterprise

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.form/)[http.request.body.form.namesThe names of the form fields in an HTTP request.

  * Enterprise

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.form.names/)[http.request.body.form.valuesThe values of the form fields in an HTTP request.

  * Enterprise

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.form.values/)[http.request.body.mimeThe MIME type of the request detected from the request body.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.mime/)[http.request.body.multipartA Map (or associative array) representation of multipart names to multipart values in the request body.

  * Enterprise

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.multipart/)[http.request.body.multipart.content_dispositionsList of `Content-Disposition` headers for each part in the multipart body.

  * Enterprise

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.multipart.content_dispositions/)[http.request.body.multipart.content_transfer_encodingsList of `Content-Transfer-Encoding` headers for each part in the multipart body.

  * Enterprise

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.multipart.content_transfer_encodings/)[http.request.body.multipart.content_typesList of `Content-Type` headers for each part in the multipart body.

  * Enterprise

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.multipart.content_types/)[http.request.body.multipart.filenamesList of filenames for each part in the multipart body.

  * Enterprise

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.multipart.filenames/)[http.request.body.multipart.namesList of multipart names for every part in the multipart body.

  * Enterprise

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.multipart.names/)[http.request.body.multipart.valuesList of multipart values for every part in the multipart body.

  * Enterprise

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.multipart.values/)[http.request.body.rawThe unaltered HTTP request body.

  * Enterprise

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.raw/)[http.request.body.sizeThe total size of the HTTP request body (in bytes).

  * Enterprise

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.size/)[http.request.body.truncatedIndicates whether the HTTP request body is truncated.

  * Enterprise

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.truncated/)[http.request.cookiesThe `Cookie` HTTP header associated with a request represented as a Map (associative array).

  * Pro or above

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.cookies/)[http.request.full_uriThe full URI as received by the web server.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.full_uri/)[http.request.headersThe HTTP request headers represented as a Map (or associative array).](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers/)[http.request.headers.namesThe names of the headers in the HTTP request.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers.names/)[http.request.headers.truncatedIndicates whether the HTTP request contains too many headers.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers.truncated/)[http.request.headers.valuesThe values of the headers in the HTTP request.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers.values/)[http.request.jwt.claims.audThe `aud` (audience) claim identifies the recipients that the JSON Web Token (JWT) is intended for.

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.jwt.claims.aud/)[http.request.jwt.claims.aud.namesThe `aud` (audience) claim identifies the recipients that the JSON Web Token (JWT) is intended for.

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.jwt.claims.aud.names/)[http.request.jwt.claims.aud.valuesThe `aud` (audience) claim identifies the recipients that the JSON Web Token (JWT) is intended for.

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.jwt.claims.aud.values/)[http.request.jwt.claims.iat.secThe `iat` (issued at) claim identifies the time (number of seconds) at which the JWT was issued.

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.jwt.claims.iat.sec/)[http.request.jwt.claims.iat.sec.namesThe `iat` (issued at) claim identifies the time (number of seconds) at which the JWT was issued.

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.jwt.claims.iat.sec.names/)[http.request.jwt.claims.iat.sec.valuesThe `iat` (issued at) claim identifies the time (number of seconds) at which the JWT was issued.

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.jwt.claims.iat.sec.values/)[http.request.jwt.claims.issThe `iss` (issuer) claim identifies the principal that issued the JWT.

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.jwt.claims.iss/)[http.request.jwt.claims.iss.namesThe `iss` (issuer) claim identifies the principal that issued the JWT.

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.jwt.claims.iss.names/)[http.request.jwt.claims.iss.valuesThe `iss` (issuer) claim identifies the principal that issued the JWT.

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.jwt.claims.iss.values/)[http.request.jwt.claims.jtiThe `jti` (JWT ID) claim provides a unique identifier for the JWT.

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.jwt.claims.jti/)[http.request.jwt.claims.jti.namesThe `jti` (JWT ID) claim provides a unique identifier for the JWT.

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.jwt.claims.jti.names/)[http.request.jwt.claims.jti.valuesThe `jti` (JWT ID) claim provides a unique identifier for the JWT.

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.jwt.claims.jti.values/)[http.request.jwt.claims.nbf.secThe `nbf` (not before) claim identifies the time (number of seconds) before which the JWT must not be accepted for processing.

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.jwt.claims.nbf.sec/)[http.request.jwt.claims.nbf.sec.namesThe `nbf` (not before) claim identifies the time (number of seconds) before which the JWT must not be accepted for processing.

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.jwt.claims.nbf.sec.names/)[http.request.jwt.claims.nbf.sec.valuesThe `nbf` (not before) claim identifies the time (number of seconds) before which the JWT must not be accepted for processing.

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.jwt.claims.nbf.sec.values/)[http.request.jwt.claims.subThe `sub` (subject) claim identifies the principal that is the subject of the JWT.

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.jwt.claims.sub/)[http.request.jwt.claims.sub.namesThe `sub` (subject) claim identifies the principal that is the subject of the JWT.

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.jwt.claims.sub.names/)[http.request.jwt.claims.sub.valuesThe `sub` (subject) claim identifies the principal that is the subject of the JWT.

  * Enterprise add-on

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.jwt.claims.sub.values/)[http.request.methodThe HTTP method, returned as a string of uppercase characters.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.method/)[http.request.timestamp.msecThe millisecond when Cloudflare received the request, between 0–999.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.timestamp.msec/)[http.request.timestamp.secThe timestamp when Cloudflare received the request, expressed as UNIX time in seconds.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.timestamp.sec/)[http.request.uriThe URI path and query string of the request.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri/)[http.request.uri.argsThe HTTP URI arguments associated with a request represented as a Map (associative array).](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.args/)[http.request.uri.args.namesThe names of the arguments in the HTTP URI query string.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.args.names/)[http.request.uri.args.valuesThe values of arguments in the HTTP URI query string.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.args.values/)[http.request.uri.pathThe URI path of the request.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.path/)[http.request.uri.path.extensionThe lowercased file extension in the URI path without the dot (`.`) character.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.path.extension/)[http.request.uri.queryThe entire query string, without the `?` delimiter.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.query/)[http.request.versionThe version of the HTTP protocol used. Use this field when different checks are needed for different versions.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.version/)[http.response.codeThe HTTP status code returned to the client, either set by a Cloudflare product or returned by the origin server.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.response.code/)[http.response.content_type.media_typeThe lowercased content type (including subtype and suffix) without any extra parameters, based on the response's `Content-Type` header.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.response.content_type.media_type/)[http.response.headersThe HTTP response headers represented as a Map (or associative array).](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.response.headers/)[http.response.headers.namesThe names of the headers in the HTTP response.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.response.headers.names/)[http.response.headers.valuesThe values of the headers in the HTTP response.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.response.headers.values/)[http.user_agentThe HTTP `User-Agent` request header, which contains a characteristic string to identify the client operating system and web browser.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.user_agent/)[http.x_forwarded_forThe full value of the `X-Forwarded-For` HTTP header.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.x_forwarded_for/)[ip.srcThe client TCP IP address, which may be adjusted to reflect the actual address of the client using HTTP headers such as `X-Forwarded-For` or `X-Real-IP`.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src/)[ip.src.asnumThe 16-bit or 32-bit integer representing the Autonomous System (AS) number associated with the client IP address.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.asnum/)[ip.src.cityThe city associated with the client IP address.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.city/)[ip.src.continentThe continent code associated with the client IP address.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.continent/)[ip.src.countryThe 2-letter country code in ISO 3166-1 Alpha 2 format.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.country/)[ip.src.is_in_european_unionWhether the request originates from a country in the European Union (EU).

  * Business or above

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.is_in_european_union/)[ip.src.latThe latitude associated with the client IP address.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.lat/)[ip.src.lonThe longitude associated with the client IP address.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.lon/)[ip.src.metro_codeThe metro code or Designated Market Area (DMA) code associated with the incoming request.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.metro_code/)[ip.src.postal_codeThe postal code associated with the incoming request.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.postal_code/)[ip.src.regionThe region name associated with the incoming request.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.region/)[ip.src.region_codeThe region code associated with the incoming request.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.region_code/)[ip.src.subdivision_1_iso_codeThe ISO 3166-2 code for the first-level region associated with the IP address.

  * Business or above

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.subdivision_1_iso_code/)[ip.src.subdivision_2_iso_codeThe ISO 3166-2 code for the second-level region associated with the IP address.

  * Business or above

](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.subdivision_2_iso_code/)[ip.src.timezone.nameThe name of the timezone associated with the incoming request.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.timezone.name/)[raw.http.request.full_uriThe raw full URI as received by the web server without any transformation.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.request.full_uri/)[raw.http.request.uriThe URI path and query string of the request without any transformation.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.request.uri/)[raw.http.request.uri.argsThe raw HTTP URI arguments associated with a request represented as a Map (associative array).](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.request.uri.args/)[raw.http.request.uri.args.namesThe raw names of the arguments in the HTTP URI query string.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.request.uri.args.names/)[raw.http.request.uri.args.valuesThe raw values of arguments in the HTTP URI query string.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.request.uri.args.values/)[raw.http.request.uri.pathThe raw URI path of the request without any transformation.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.request.uri.path/)[raw.http.request.uri.path.extensionThe raw file extension in the request URI path without any transformation.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.request.uri.path.extension/)[raw.http.request.uri.queryThe entire query string without the `?` delimiter and without any transformation.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.request.uri.query/)[raw.http.response.headersThe HTTP response headers without any transformation represented as a Map (or associative array).](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.response.headers/)[raw.http.response.headers.namesThe names of the headers in the HTTP response without any transformation.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.response.headers.names/)[raw.http.response.headers.valuesThe values of the headers in the HTTP response without any transformation.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.response.headers.values/)[sslReturns `true` when the HTTP connection to the client is encrypted.](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ssl/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ruleset-engine/rules-language/fields/reference/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
