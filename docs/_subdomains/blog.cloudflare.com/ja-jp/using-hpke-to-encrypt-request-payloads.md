---
url: https://blog.cloudflare.com/ja-jp/using-hpke-to-encrypt-request-payloads/
title: HPKE\u3092\u4f7f\u7528\u3057\u305f\u30ea\u30af\u30a8\u30b9\u30c8\u30da\u30a4\u30ed\u30fc\u30c9\u306e\u6697\u53f7\u5316 | Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:52:24.984732+00:00
---

# HPKEを使用したリクエストペイロードの暗号化 | Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/using-hpke-to-encrypt-request-payloads/

[ブログ](https://blog.cloudflare.com/ja-jp/)

[WAF](https://blog.cloudflare.com/ja-jp/tag/waf/)[WAF Rules](https://blog.cloudflare.com/ja-jp/tag/waf-rules/)[セキュリティ](https://blog.cloudflare.com/ja-jp/tag/security/)2件2件タグを表示

5 タグタグを5件表示

  * 投稿タグ
  * [WAF](https://blog.cloudflare.com/ja-jp/tag/waf/)[セキュリティ](https://blog.cloudflare.com/ja-jp/tag/security/)[ファイアウォール](https://blog.cloudflare.com/ja-jp/tag/firewall/)[暗号](https://blog.cloudflare.com/ja-jp/tag/cryptography/)
  * 全てのタグ
  * 一致するタグ
  * 該当するタグはありません
  * [1.1.1.1](https://blog.cloudflare.com/ja-jp/tag/1-1-1-1/)
  * [Access](https://blog.cloudflare.com/ja-jp/tag/access/)
  * [アクセシビリティ](https://blog.cloudflare.com/ja-jp/tag/accessibility/)
  * [M&A](https://blog.cloudflare.com/ja-jp/tag/acquisitions/)
  * [アドレス指定](https://blog.cloudflare.com/ja-jp/tag/addressing/)
  * [高度なDDoS攻撃対策](https://blog.cloudflare.com/ja-jp/tag/advanced-ddos/)
  * [広告](https://blog.cloudflare.com/ja-jp/tag/advertising/)
  * [Aegis](https://blog.cloudflare.com/ja-jp/tag/aegis/)
  * [エージェント準備度](https://blog.cloudflare.com/ja-jp/tag/agent-readiness/)
  * [エージェント](https://blog.cloudflare.com/ja-jp/tag/agents/)
  * [Agents Week](https://blog.cloudflare.com/ja-jp/tag/agents-week/)
  * [AI](https://blog.cloudflare.com/ja-jp/tag/ai/)
  * [AIボット](https://blog.cloudflare.com/ja-jp/tag/ai-bots/)
  * [AI Gateway](https://blog.cloudflare.com/ja-jp/tag/ai-gateway/)
  * [AI検索](https://blog.cloudflare.com/ja-jp/tag/ai-search/)
  * [AI Week](https://blog.cloudflare.com/ja-jp/tag/ai-week/)
  * [AI-SPM](https://blog.cloudflare.com/ja-jp/tag/ai-spm/)
  * [AMD](https://blog.cloudflare.com/ja-jp/tag/amd/)
  * [分析](https://blog.cloudflare.com/ja-jp/tag/analytics/)
  * [API](https://blog.cloudflare.com/ja-jp/tag/api/)
  * [APIセキュリティ](https://blog.cloudflare.com/ja-jp/tag/api-security/)
  * [アプリケーションセキュリティ](https://blog.cloudflare.com/ja-jp/tag/application-security/)
  * [アプリケーションサービス](https://blog.cloudflare.com/ja-jp/tag/application-services/)
  * [攻撃](https://blog.cloudflare.com/ja-jp/tag/attacks/)
  * [監査ログ](https://blog.cloudflare.com/ja-jp/tag/audit-logs/)
  * [Auto Rag](https://blog.cloudflare.com/ja-jp/tag/auto-rag/)
  * [自動化](https://blog.cloudflare.com/ja-jp/tag/automation/)
  * [AWS](https://blog.cloudflare.com/ja-jp/tag/aws/)
  * [より良いインターネット](https://blog.cloudflare.com/ja-jp/tag/better-internet/)
  * [BGP](https://blog.cloudflare.com/ja-jp/tag/bgp/)
  * [バースデーウィーク](https://blog.cloudflare.com/ja-jp/tag/birthday-week/)
  * [ボット管理](https://blog.cloudflare.com/ja-jp/tag/bot-management/)
  * [ボット](https://blog.cloudflare.com/ja-jp/tag/bots/)
  * [BPF](https://blog.cloudflare.com/ja-jp/tag/bpf/)
  * [Browser Rendering](https://blog.cloudflare.com/ja-jp/tag/browser-rendering/)
  * [Browser Run](https://blog.cloudflare.com/ja-jp/tag/browser-run/)
  * [BYOIP](https://blog.cloudflare.com/ja-jp/tag/byoip/)
  * [キャッシュ](https://blog.cloudflare.com/ja-jp/tag/cache/)
  * [キャッシュパージ](https://blog.cloudflare.com/ja-jp/tag/cache-purge/)
  * [CASB](https://blog.cloudflare.com/ja-jp/tag/casb/)
  * [CDN](https://blog.cloudflare.com/ja-jp/tag/cdn/)
  * [認定](https://blog.cloudflare.com/ja-jp/tag/certification/)
  * [質問ページ](https://blog.cloudflare.com/ja-jp/tag/challenge-page/)
  * [Chrome](https://blog.cloudflare.com/ja-jp/tag/chrome/)
  * [CIO Week](https://blog.cloudflare.com/ja-jp/tag/cio-week/)
  * [ClickHouse](https://blog.cloudflare.com/ja-jp/tag/clickhouse/)
  * [クライアントレス](https://blog.cloudflare.com/ja-jp/tag/clientless/)
  * [Cloud Email Security](https://blog.cloudflare.com/ja-jp/tag/cloud-email-security/)
  * [Cloudflare Access](https://blog.cloudflare.com/ja-jp/tag/cloudflare-access/)
  * [Cloudflare Calls](https://blog.cloudflare.com/ja-jp/tag/cloudflare-calls/)
  * [Cloudflare for Startups](https://blog.cloudflare.com/ja-jp/tag/cloudflare-for-startups/)
  * [Cloudflare Gateway](https://blog.cloudflare.com/ja-jp/tag/gateway/)
  * [Cloudflare Images](https://blog.cloudflare.com/ja-jp/tag/cloudflare-images/)
  * [Cloudflareのメディアプラットフォーム](https://blog.cloudflare.com/ja-jp/tag/cloudflare-media-platform/)
  * [Cloudflare One](https://blog.cloudflare.com/ja-jp/tag/cloudflare-one/)
  * [Cloudflare Pages](https://blog.cloudflare.com/ja-jp/tag/cloudflare-pages/)
  * [Cloudflare Queues](https://blog.cloudflare.com/ja-jp/tag/cloudflare-queues/)
  * [Cloudflare Stream](https://blog.cloudflare.com/ja-jp/tag/cloudflare-stream/)
  * [Cloudflare Tunnel](https://blog.cloudflare.com/ja-jp/tag/cloudflare-tunnel/)
  * [Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)
  * [Cloudflare Workers KV](https://blog.cloudflare.com/ja-jp/tag/cloudflare-workers-kv/)
  * [Cloudflare Zero Trust](https://blog.cloudflare.com/ja-jp/tag/cloudflare-zero-trust/)
  * [Cloudforce One](https://blog.cloudflare.com/ja-jp/tag/cloudforce-one/)
  * [コードオレンジ](https://blog.cloudflare.com/ja-jp/tag/code-orange/)
  * [コンプライアンス](https://blog.cloudflare.com/ja-jp/tag/compliance/)
  * [圧縮](https://blog.cloudflare.com/ja-jp/tag/compression/)
  * [コンフィギュレーション管理](https://blog.cloudflare.com/ja-jp/tag/configuration-management/)
  * [輻輳制御](https://blog.cloudflare.com/ja-jp/tag/congestion-control/)
  * [コネクティビティクラウド](https://blog.cloudflare.com/ja-jp/tag/connectivity-cloud/)
  * [コンシューマーサービス](https://blog.cloudflare.com/ja-jp/tag/consumer-services/)
  * [コンテナ](https://blog.cloudflare.com/ja-jp/tag/containers/)
  * [Content Independence Day](https://blog.cloudflare.com/ja-jp/tag/content-independence-day/)
  * [コンテキスト](https://blog.cloudflare.com/ja-jp/tag/context/)
  * [コア](https://blog.cloudflare.com/ja-jp/tag/core/)
  * [クローラーヒント](https://blog.cloudflare.com/ja-jp/tag/crawler-hints/)
  * [暗号](https://blog.cloudflare.com/ja-jp/tag/cryptography/)
  * [カスタマーゼロ](https://blog.cloudflare.com/ja-jp/tag/customer-zero/)
  * [CVE](https://blog.cloudflare.com/ja-jp/tag/cve/)
  * [D1](https://blog.cloudflare.com/ja-jp/tag/d1/)
  * [ダッシュボード](https://blog.cloudflare.com/ja-jp/tag/dashboard-tag/)
  * [データ](https://blog.cloudflare.com/ja-jp/tag/data/)
  * [データカタログ](https://blog.cloudflare.com/ja-jp/tag/data-catalog/)
  * [データプラットフォーム](https://blog.cloudflare.com/ja-jp/tag/data-platform/)
  * [データ保護](https://blog.cloudflare.com/ja-jp/tag/data-protection/)
  * [データベース](https://blog.cloudflare.com/ja-jp/tag/database/)
  * [DDoS](https://blog.cloudflare.com/ja-jp/tag/ddos/)
  * [DDoSアラート](https://blog.cloudflare.com/ja-jp/tag/ddos-alerts/)
  * [DDoSレポート](https://blog.cloudflare.com/ja-jp/tag/ddos-reports/)
  * [デバッグ](https://blog.cloudflare.com/ja-jp/tag/debugging/)
  * [詳細情報](https://blog.cloudflare.com/ja-jp/tag/deep-dive/)
  * [デザイン](https://blog.cloudflare.com/ja-jp/tag/design/)
  * [開発者向けドキュメント](https://blog.cloudflare.com/ja-jp/tag/developer-documentation/)
  * [開発者プラットフォーム](https://blog.cloudflare.com/ja-jp/tag/developer-platform/)
  * [Developer Week](https://blog.cloudflare.com/ja-jp/tag/developer-week/)
  * [開発者](https://blog.cloudflare.com/ja-jp/tag/developers/)
  * [開発者ストレージ](https://blog.cloudflare.com/ja-jp/tag/developers-storage/)
  * [DEX](https://blog.cloudflare.com/ja-jp/tag/dex/)
  * [デジタルフォレンジック](https://blog.cloudflare.com/ja-jp/tag/digital-forensics/)
  * [DLP](https://blog.cloudflare.com/ja-jp/tag/dlp/)
  * [DNS](https://blog.cloudflare.com/ja-jp/tag/dns/)
  * [DNSSEC](https://blog.cloudflare.com/ja-jp/tag/dnssec/)
  * [ドッグフーディング](https://blog.cloudflare.com/ja-jp/tag/dogfooding/)
  * [DOH](https://blog.cloudflare.com/ja-jp/tag/doh/)
  * [耐久性のある実行](https://blog.cloudflare.com/ja-jp/tag/durable-execution/)
  * [Durable Objects](https://blog.cloudflare.com/ja-jp/tag/durable-objects/)
  * [eBPF](https://blog.cloudflare.com/ja-jp/tag/ebpf/)
  * [エッジ](https://blog.cloudflare.com/ja-jp/tag/edge/)
  * [エッジコンピューティング](https://blog.cloudflare.com/ja-jp/tag/edge-computing/)
  * [エグレス](https://blog.cloudflare.com/ja-jp/tag/egress/)
  * [メール](https://blog.cloudflare.com/ja-jp/tag/email/)
  * [メールセキュリティ](https://blog.cloudflare.com/ja-jp/tag/email-security/)
  * [Emissions](https://blog.cloudflare.com/ja-jp/tag/emissions/)
  * [エンジニアリング](https://blog.cloudflare.com/ja-jp/tag/engineering/)
  * [Enterprise](https://blog.cloudflare.com/ja-jp/tag/enterprise/)
  * [エントロピー](https://blog.cloudflare.com/ja-jp/tag/entropy/)
  * [機能フラグ](https://blog.cloudflare.com/ja-jp/tag/feature-flags/)
  * [ファイアウォール](https://blog.cloudflare.com/ja-jp/tag/firewall/)
  * [Forrester](https://blog.cloudflare.com/ja-jp/tag/forrester/)
  * [創業者よりご挨拶](https://blog.cloudflare.com/ja-jp/tag/founders-letter/)
  * [詐欺](https://blog.cloudflare.com/ja-jp/tag/fraud/)
  * [フロントエンド](https://blog.cloudflare.com/ja-jp/tag/front-end/)
  * [フルスタック](https://blog.cloudflare.com/ja-jp/tag/full-stack/)
  * [全体的な使いやすさ](https://blog.cloudflare.com/ja-jp/tag/general-availability/)
  * [生成AI](https://blog.cloudflare.com/ja-jp/tag/generative-ai/)
  * [GitHub](https://blog.cloudflare.com/ja-jp/tag/github/)
  * [Go](https://blog.cloudflare.com/ja-jp/tag/go/)
  * [Google](https://blog.cloudflare.com/ja-jp/tag/google/)
  * [Google Cloud](https://blog.cloudflare.com/ja-jp/tag/google-cloud/)
  * [ハードウェア](https://blog.cloudflare.com/ja-jp/tag/hardware/)
  * [HTTP3](https://blog.cloudflare.com/ja-jp/tag/http3/)
  * [ハイブリッドクラウド](https://blog.cloudflare.com/ja-jp/tag/hybrid-cloud/)
  * [Hyperdrive](https://blog.cloudflare.com/ja-jp/tag/hyperdrive/)
  * [ID](https://blog.cloudflare.com/ja-jp/tag/identity/)
  * [IETF](https://blog.cloudflare.com/ja-jp/tag/ietf/)
  * [画像の最適化](https://blog.cloudflare.com/ja-jp/tag/image-optimization/)
  * [画像リサイズ](https://blog.cloudflare.com/ja-jp/tag/image-resizing/)
  * [影響](https://blog.cloudflare.com/ja-jp/tag/impact/)
  * [インシデント対応](https://blog.cloudflare.com/ja-jp/tag/incident-response/)
  * [インフラストラクチャ](https://blog.cloudflare.com/ja-jp/tag/infrastructure/)
  * [コードとしてのインフラストラクチャ](https://blog.cloudflare.com/ja-jp/tag/infrastructure-as-code/)
  * [インサイト](https://blog.cloudflare.com/ja-jp/tag/insights/)
  * [Intel](https://blog.cloudflare.com/ja-jp/tag/intel/)
  * [Interconnection](https://blog.cloudflare.com/ja-jp/tag/interconnection/)
  * [インターネットのパフォーマンス](https://blog.cloudflare.com/ja-jp/tag/internet-performance/)
  * [インターネット品質](https://blog.cloudflare.com/ja-jp/tag/internet-quality/)
  * [インターネット遮断](https://blog.cloudflare.com/ja-jp/tag/internet-shutdown/)
  * [インターネットトラフィック](https://blog.cloudflare.com/ja-jp/tag/internet-traffic/)
  * [インターネットトレンド](https://blog.cloudflare.com/ja-jp/tag/internet-trends/)
  * [インターンシップ体験](https://blog.cloudflare.com/ja-jp/tag/internship-experience/)
  * [IPv4](https://blog.cloudflare.com/ja-jp/tag/ipv4/)
  * [IPv6](https://blog.cloudflare.com/ja-jp/tag/ipv6/)
  * [JavaScript](https://blog.cloudflare.com/ja-jp/tag/javascript/)
  * [Kafka](https://blog.cloudflare.com/ja-jp/tag/kafka/)
  * [キーバリュー](https://blog.cloudflare.com/ja-jp/tag/key-value/)
  * [KeyTrap](https://blog.cloudflare.com/ja-jp/tag/keytrap/)
  * [Kubernetes](https://blog.cloudflare.com/ja-jp/tag/kubernetes/)
  * [LangChain](https://blog.cloudflare.com/ja-jp/tag/langchain/)
  * [中南米](https://blog.cloudflare.com/ja-jp/tag/latin-america/)
  * [Life at Cloudflare](https://blog.cloudflare.com/ja-jp/tag/life-at-cloudflare/)
  * [Linux](https://blog.cloudflare.com/ja-jp/tag/linux/)
  * [ライブストリーミング](https://blog.cloudflare.com/ja-jp/tag/live-streaming/)
  * [LLM](https://blog.cloudflare.com/ja-jp/tag/llm/)
  * [Load Balancing](https://blog.cloudflare.com/ja-jp/tag/loadbalancing/)
  * [ログ](https://blog.cloudflare.com/ja-jp/tag/logging/)
  * [ログ](https://blog.cloudflare.com/ja-jp/tag/logs/)
  * [Magic Transit](https://blog.cloudflare.com/ja-jp/tag/magic-transit/)
  * [悪意のあるJavaScript](https://blog.cloudflare.com/ja-jp/tag/malicious-javascript/)
  * [マルウェア](https://blog.cloudflare.com/ja-jp/tag/malware/)
  * [MASQUE](https://blog.cloudflare.com/ja-jp/tag/masque/)
  * [MCP](https://blog.cloudflare.com/ja-jp/tag/mcp/)
  * [マイクロフロントエンド](https://blog.cloudflare.com/ja-jp/tag/micro-frontends/)
  * [Microsoft](https://blog.cloudflare.com/ja-jp/tag/microsoft/)
  * [Microsoft Azure](https://blog.cloudflare.com/ja-jp/tag/microsoft-azure/)
  * [Mirai](https://blog.cloudflare.com/ja-jp/tag/mirai/)
  * [モデルコンテキストプロトコル](https://blog.cloudflare.com/ja-jp/tag/model-context-protocol/)
  * [MySQL](https://blog.cloudflare.com/ja-jp/tag/mysql/)
  * [ネットワーク](https://blog.cloudflare.com/ja-jp/tag/network/)
  * [ネットワークパフォーマンス更新](https://blog.cloudflare.com/ja-jp/tag/network-performance-update/)
  * [ネットワークサービス](https://blog.cloudflare.com/ja-jp/tag/network-services/)
  * [ネットワーキング](https://blog.cloudflare.com/ja-jp/tag/networking/)
  * [NGINX](https://blog.cloudflare.com/ja-jp/tag/nginx/)
  * [NIST](https://blog.cloudflare.com/ja-jp/tag/nist/)
  * [Node.js](https://blog.cloudflare.com/ja-jp/tag/node-js/)
  * [Notebook](https://blog.cloudflare.com/ja-jp/tag/notebooks/)
  * [OAuth](https://blog.cloudflare.com/ja-jp/tag/oauth/)
  * [Observability](https://blog.cloudflare.com/ja-jp/tag/observability/)
  * [オープンソース](https://blog.cloudflare.com/ja-jp/tag/open-source/)
  * [OpenTelemetry ](https://blog.cloudflare.com/ja-jp/tag/opentelemetry/)
  * [最適化](https://blog.cloudflare.com/ja-jp/tag/optimization/)
  * [障害](https://blog.cloudflare.com/ja-jp/tag/outage/)
  * [パートナー](https://blog.cloudflare.com/ja-jp/tag/partners/)
  * [パスワード](https://blog.cloudflare.com/ja-jp/tag/passwords/)
  * [クロールごとに課金](https://blog.cloudflare.com/ja-jp/tag/pay-per-crawl/)
  * [パフォーマンス](https://blog.cloudflare.com/ja-jp/tag/performance/)
  * [Pingora](https://blog.cloudflare.com/ja-jp/tag/pingora/)
  * [PlanetScale](https://blog.cloudflare.com/ja-jp/tag/planetscale/)
  * [プラットフォームエンジニアリング](https://blog.cloudflare.com/ja-jp/tag/platform-engineering/)
  * [ポリシーと法務](https://blog.cloudflare.com/ja-jp/tag/policy/)
  * [事後検証](https://blog.cloudflare.com/ja-jp/tag/post-mortem/)
  * [ポスト量子](https://blog.cloudflare.com/ja-jp/tag/post-quantum/)
  * [Postgres](https://blog.cloudflare.com/ja-jp/tag/postgres/)
  * [プライバシー](https://blog.cloudflare.com/ja-jp/tag/privacy/)
  * [プライバシーパス](https://blog.cloudflare.com/ja-jp/tag/privacy-pass/)
  * [プライベートネットワーク](https://blog.cloudflare.com/ja-jp/tag/private-network/)
  * [製品デザイン](https://blog.cloudflare.com/ja-jp/tag/product-design/)
  * [製品ニュース](https://blog.cloudflare.com/ja-jp/tag/product-news/)
  * [プログラミング](https://blog.cloudflare.com/ja-jp/tag/programming/)
  * [プロジェクトGalileo](https://blog.cloudflare.com/ja-jp/tag/project-galileo/)
  * [Prometheus](https://blog.cloudflare.com/ja-jp/tag/prometheus/)
  * [プロトコル](https://blog.cloudflare.com/ja-jp/tag/protocols/)
  * [公共部門](https://blog.cloudflare.com/ja-jp/tag/public-sector/)
  * [Python](https://blog.cloudflare.com/ja-jp/tag/python/)
  * [キュー](https://blog.cloudflare.com/ja-jp/tag/queues/)
  * [QUIC](https://blog.cloudflare.com/ja-jp/tag/quic/)
  * [QUIC](https://blog.cloudflare.com/ja-jp/tag/quiche/)
  * [Quicksilver](https://blog.cloudflare.com/ja-jp/tag/quicksilver/)
  * [R2](https://blog.cloudflare.com/ja-jp/tag/r2/)
  * [R2 Super Slurper](https://blog.cloudflare.com/ja-jp/tag/r2-super-slurper/)
  * [Radar](https://blog.cloudflare.com/ja-jp/tag/cloudflare-radar/)
  * [ランダム性](https://blog.cloudflare.com/ja-jp/tag/randomness/)
  * [ランサム攻撃](https://blog.cloudflare.com/ja-jp/tag/ransom-attacks/)
  * [レート制限](https://blog.cloudflare.com/ja-jp/tag/rate-limiting/)
  * [リアルタイム](https://blog.cloudflare.com/ja-jp/tag/real-time/)
  * [レジストラ](https://blog.cloudflare.com/ja-jp/tag/registrar/)
  * [信頼性](https://blog.cloudflare.com/ja-jp/tag/reliability/)
  * [リモートデスクトッププロトコル ](https://blog.cloudflare.com/ja-jp/tag/remote-desktop-protocol/)
  * [リモートワーク](https://blog.cloudflare.com/ja-jp/tag/remote-work/)
  * [研究](https://blog.cloudflare.com/ja-jp/tag/research/)
  * [リゾルバ](https://blog.cloudflare.com/ja-jp/tag/resolver/)
  * [リバースエンジニアリング](https://blog.cloudflare.com/ja-jp/tag/reverse-engineering/)
  * [リスク管理](https://blog.cloudflare.com/ja-jp/tag/risk-management/)
  * [ルーティング](https://blog.cloudflare.com/ja-jp/tag/routing/)
  * [ルーティングセキュリティ](https://blog.cloudflare.com/ja-jp/tag/routing-security/)
  * [RPKI](https://blog.cloudflare.com/ja-jp/tag/rpki/)
  * [Rust](https://blog.cloudflare.com/ja-jp/tag/rust/)
  * [Rust Workers](https://blog.cloudflare.com/ja-jp/tag/rust-workers/)
  * [SaaSセキュリティ](https://blog.cloudflare.com/ja-jp/tag/saas-security/)
  * [ソルト](https://blog.cloudflare.com/ja-jp/tag/salt/)
  * [Sandbox](https://blog.cloudflare.com/ja-jp/tag/sandbox/)
  * [SASE](https://blog.cloudflare.com/ja-jp/tag/sase/)
  * [SDK](https://blog.cloudflare.com/ja-jp/tag/sdk/)
  * [検索エンジン](https://blog.cloudflare.com/ja-jp/tag/search-engine/)
  * [セキュアWebゲートウェイ](https://blog.cloudflare.com/ja-jp/tag/secure-web-gateway/)
  * [セキュリティ](https://blog.cloudflare.com/ja-jp/tag/security/)
  * [セキュリティセンター](https://blog.cloudflare.com/ja-jp/tag/security-center/)
  * [セキュリティ体制](https://blog.cloudflare.com/ja-jp/tag/security-posture/)
  * [セキュリティ態勢管理](https://blog.cloudflare.com/ja-jp/tag/security-posture-management/)
  * [Security Week](https://blog.cloudflare.com/ja-jp/tag/security-week/)
  * [サーバーレス](https://blog.cloudflare.com/ja-jp/tag/serverless/)
  * [サーバー](https://blog.cloudflare.com/ja-jp/tag/servers/)
  * [SIEM](https://blog.cloudflare.com/ja-jp/tag/siem/)
  * [Smart Shield](https://blog.cloudflare.com/ja-jp/tag/smart-shield/)
  * [Spectrum](https://blog.cloudflare.com/ja-jp/tag/spectrum/)
  * [速度](https://blog.cloudflare.com/ja-jp/tag/speed/)
  * [スピードと信頼性](https://blog.cloudflare.com/ja-jp/tag/speed-and-reliability/)
  * [SQL](https://blog.cloudflare.com/ja-jp/tag/sql/)
  * [SRE](https://blog.cloudflare.com/ja-jp/tag/sre/)
  * [標準](https://blog.cloudflare.com/ja-jp/tag/standards/)
  * [ストレージ](https://blog.cloudflare.com/ja-jp/tag/storage/)
  * [サプライチェーン攻撃](https://blog.cloudflare.com/ja-jp/tag/supply-chain-attacks/)
  * [TCP](https://blog.cloudflare.com/ja-jp/tag/tcp/)
  * [チーム](https://blog.cloudflare.com/ja-jp/tag/team/)
  * [Terraform](https://blog.cloudflare.com/ja-jp/tag/terraform/)
  * [脅威データ](https://blog.cloudflare.com/ja-jp/tag/threat-data/)
  * [脅威インテリジェンス](https://blog.cloudflare.com/ja-jp/tag/threat-intelligence/)
  * [脅威オペレーション](https://blog.cloudflare.com/ja-jp/tag/threat-operations/)
  * [脅威](https://blog.cloudflare.com/ja-jp/tag/threats/)
  * [TLS](https://blog.cloudflare.com/ja-jp/tag/tls/)
  * [トレース](https://blog.cloudflare.com/ja-jp/tag/tracing/)
  * [トラフィック](https://blog.cloudflare.com/ja-jp/tag/traffic/)
  * [透明性](https://blog.cloudflare.com/ja-jp/tag/transparency/)
  * [傾向](https://blog.cloudflare.com/ja-jp/tag/trends/)
  * [TURNサーバー](https://blog.cloudflare.com/ja-jp/tag/turn-server/)
  * [Turnstile](https://blog.cloudflare.com/ja-jp/tag/turnstile/)
  * [TypeScript](https://blog.cloudflare.com/ja-jp/tag/typescript/)
  * [ユーザー調査](https://blog.cloudflare.com/ja-jp/tag/user-research/)
  * [VDI](https://blog.cloudflare.com/ja-jp/tag/vdi/)
  * [動画](https://blog.cloudflare.com/ja-jp/tag/video/)
  * [VPC](https://blog.cloudflare.com/ja-jp/tag/vpc/)
  * [WAF](https://blog.cloudflare.com/ja-jp/tag/waf/)
  * [WARP](https://blog.cloudflare.com/ja-jp/tag/warp/)
  * [WASM](https://blog.cloudflare.com/ja-jp/tag/wasm/)
  * [Webアプリケーション ファイアウォール](https://blog.cloudflare.com/ja-jp/tag/web-application-firewall/)
  * [WebAssembly](https://blog.cloudflare.com/ja-jp/tag/webassembly/)
  * [WebRTC](https://blog.cloudflare.com/ja-jp/tag/webrtc/)
  * [Workers AI](https://blog.cloudflare.com/ja-jp/tag/workers-ai/)
  * [Workers Launchpad](https://blog.cloudflare.com/ja-jp/tag/workers-launchpad/)
  * [Workers VPC](https://blog.cloudflare.com/ja-jp/tag/workers-vpc/)
  * [Workflows](https://blog.cloudflare.com/ja-jp/tag/workflows/)
  * [Wrangler](https://blog.cloudflare.com/ja-jp/tag/wrangler/)
  * [1年の振り返り](https://blog.cloudflare.com/ja-jp/tag/year-in-review/)
  * [Z3](https://blog.cloudflare.com/ja-jp/tag/z3/)
  * [Zero Trust](https://blog.cloudflare.com/ja-jp/tag/zero-trust/)



[ファイアウォール](https://blog.cloudflare.com/ja-jp/tag/firewall/)[暗号](https://blog.cloudflare.com/ja-jp/tag/cryptography/)

[WAF](https://blog.cloudflare.com/ja-jp/tag/waf/)[WAF Rules](https://blog.cloudflare.com/ja-jp/tag/waf-rules/)[セキュリティ](https://blog.cloudflare.com/ja-jp/tag/security/)[ファイアウォール](https://blog.cloudflare.com/ja-jp/tag/firewall/)[暗号](https://blog.cloudflare.com/ja-jp/tag/cryptography/)

2021年2月19日

# HPKEを使用したリクエストペイロードの暗号化

![Miguel de Moura](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW469GP192YFYYEYAD222W8R.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Andre Bluehs](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46FSDNFHZ8XM1WXN8QWRP1.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Miguel de Moura](https://blog.cloudflare.com/ja-jp/author/miguel/)、[Andre Bluehs](https://blog.cloudflare.com/ja-jp/author/andre-bluehs/)

12分で読了

URLをコピー

この記事は以下でも利用可能です [English](https://blog.cloudflare.com/using-hpke-to-encrypt-request-payloads/).

![HPKE: Standardizing public-key encryption \(finally!\)](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44J1G75Z100YAJ3KFKVPFV.png&w=1600&h=800&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/////Pv68PDx6ens7Ozu8fHz8fHx7Ozr/////f3+7/D05uju5urx7e/17/D07e3u////////8PP44+ny4+n06u/57/L48PDy////////9Pf95u335e367PP+8/b99fX3////////+/7/7/T97vX/9fr/+/3/+/v9////////////+v3/+///////////////////////////////////////////////////////////////////////////////)

管理ルールチームには最近、ルールに合うリクエストの箇所をみて、[ファイアウォールルールのデバック](https://blog.cloudflare.com/encrypt-waf-payloads-hpke/)をEnterpriseのユーザーに許可するというタスクが与えられました。これにより、ルールが中止している特定の攻撃を特定したり、リクエストが誤検知された理由や、ルールをどのように改良すればこれを改善できるのかがより簡単にわかるようになります。

しかし、根本的な問題は、このデバックデータをどのように安全に保存するかということでした。送信データ、Cookie、リクエストの他の部分から、個人を特定できる情報などの機密データが含まれてしまう可能性があるためです。このデータにアクセスを許可された人だけがデータを扱うことができるように、データを保存する必要がありました。当社の哲学である、当社ネットワークを通過する個人を特定できる情報は[有害なアセット](https://blog.cloudflare.com/welcome-to-privacy-and-compliance-week/)であるという考え方に従うと、Cloudflareでさえ、このデータを見れる状態であるべきではないのです。

つまり、Cloudflareではなく、ユーザーがそれを復号化できるようにデータを暗号化する必要がありました。これは[公開鍵暗号化](https://www.cloudflare.com/ja-jp/learning/ssl/how-does-public-key-encryption-work/)を意味しました。

今度は、使用する暗号化アルゴリズムを決定する必要がありました。私たちはいくつかの質問をつくり、どのアルゴリズムを使うべきかを決めることにしました。

  * アルゴリズムにはどのような要件があるか？
  * 実装にはどの言語を使うか？
  * ユーザーのために可能な限り安全にこれを行う方法は？



Cloudflareが出した結論を以下に記します。

### **アルゴリズムの要件**

[公開鍵暗号化](https://www.cloudflare.com/ja-jp/learning/ssl/how-does-public-key-encryption-work/)を使用する必要があることはわかっていましたが、パフォーマンスを維持する必要がありました。このため、当社では早い段階で[ハイブリット公開鍵暗号化](https://tools.ietf.org/html/draft-irtf-cfrg-hpke-06)（HPKE）を選択することしました。HPKEがパフォーマンス向上のために、対称暗号化と公開鍵暗号化の両方で最良のアプローチを提供していたためです。両方のいい面を提供するというアプローチは、新しいものではありませんが [[1](https://nacl.cr.yp.to/box.html)][[2](https://github.com/google/tink)][[3](https://age-encryption.org/)]、HPKEでは、一般的な鍵カプセル化メカニズムと対称暗号化アルゴリズムを組み合わせた、単一の、将来性もあり、堅牢で、相互運用可能な仕組みを提供することを目指しています。

HPKEは、Crypto Forum Research Group (CFRG)という、インターネット標準の開発をサポートする[IETF](http://ietf.org/)の研究機関により開発された新しい標準です。CFRGは、RFC（楕円曲線のための[RFC7748](https://tools.ietf.org/html/rfc7748)など）と呼ばれる仕様をつくります。RFCは、上位レベルのプロトコルで使用されます。以前のブログ投稿でも2つのプロトコル、[ODoH](https://blog.cloudflare.com/oblivious-dns/)と[ECH](https://blog.cloudflare.com/encrypted-client-hello/)を取りあげました。Cloudflareもインターネット標準のサポート役として長い間活躍してきたので、この機能のためにHPKEを選んだことは自然な選択でした。さらに、HPKEについて、Cloudflareの同僚の一人は共著を出しています。

### **HPKEの仕組み**

HPKEは、[ディフィー・ヘルマンの楕円曲線](https://en.wikipedia.org/wiki/Elliptic-curve_Diffie%E2%80%93Hellman)などの非対象アルゴリズムと、AESなどの対称暗号を組み合わせます。HPKEの利点の一つは、実装者はアルゴリズムからの影響を受けないが、それが[証明できるほど安全](https://en.wikipedia.org/wiki/Provable_security#In_cryptography)で、開発者の「セキュリティは重要だ」という直感的な概念を満たす点です。開発者が、スキームが何をするのかを十分に理解することなく、スキームを使いはじめ、セキュリティの脆弱性が生じることがあまりにも多すぎます。

HPKEは、一般的な方法でハイレベルのセキュリティを提供し、生成したコンテキストにメッセージを結びつけるために必要なフックを提供することで、これらの問題を解決します。これは、正しいセキュリティ概念とスキームの関する数十年の研究を応用したものです。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![HPKE overview](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47KK357X830WG21WFKWGK9.png&w=624&h=285&f=webp&fit=cover&position=center)

HPKEの構築は数段階に分けられています。まず、ディフィー・ヘルマンのキー合意をキーカプセル化メカニズムに変換します。キーカプセル化メカニズムには、EncapとDecapの2つのアルゴリズムがあります。Encapアルゴリズムは、対称秘密を作成し、パブリックキーで包みます。これにより、プライベートキーの所有者だけがそれを開くことができます。カプセル化が使用されている場合攻撃者は、ランダムキーを修復できません。Decapは、パブリックキーに関連付けられたカプセル化とプライベートキーを受け取り、同じランダムキーを計算します。この変換により、HPKEは、あらゆる種類の公開鍵暗号化または鍵合意アルゴリズムでほとんど動作を変更させることなく、柔軟に対応することができるのです。

HPKEは、この鍵にオプションの情報引数と、各側で費用される暗号化パラメータに関する情報とを組み合わせます。これにより、攻撃者はコンテキストから外すことで、メッセージの意味を変更できないようになります。はがきに、「近々お会いできるのを楽しみにしています」と書かれていた場合、送り主が歯科医だったら不吉に感じますが、送り主が自分のおばあさんからだったら愛おしく思いますね。

HPKEの仕様は公開されていて、[IETFのWebサイト](https://tools.ietf.org/html/draft-irtf-cfrg-hpke-06)で入手することができます。HPKEは、CFRGの暗号の専門家による複数のレビューと分析を経てRFCとして認定される途中です。HPKEは、ODoH、ECH、そして新しい[メッセージングレイヤーセキュリティ（MLS）](https://messaginglayersecurity.rocks/)プロトコルなど、IETFプロトコルで既に採用されています。HPKEはまた、[ポスト量子の未来](https://blog.cloudflare.com/securing-the-post-quantum-world/)に向けてつくられたものです。これは、ポスト量子公開鍵暗号化の[NISTフィナリストすべて](https://csrc.nist.gov/News/2020/pqc-third-round-candidate-announcement)を含むKEMと動作するように設計されているためです。

### **実装言語**

暗号化スキームを選択したら、次は実装について決める必要がありました。HPKEはまだかなり新しいので、ライブラリはそれほど充実していません。[リファレンス実装](https://github.com/cisco/go-hpke)はありますが、[CIRCL](https://github.com/cloudflare/circl)の一部としてGoで実装を開発している途中です。しかしながら、実装言語については、ベストなものとして認知されていて、明らかに「これだ」というものがなかったので、[実装には](https://github.com/rozbb/rust-hpke)CloudflareのEdgeにあるファイアウォールで既に多く使用されている[Rust](https://blog.cloudflare.com/building-fast-interpreters-in-rust/)を使うことにしました。

これとは別に、Rustという言語にはネイティブプリミティブのような機能と、重要な[WebAssembly (WASM)](https://developer.mozilla.org/en-US/docs/WebAssembly)に簡単にコンパイルできるという利点がありました。

[以前のブログ記事](https://blog.cloudflare.com/encrypt-waf-payloads-hpke/)でも述べたように、顧客はキーペアを生成し、ダッシュボードUIまたはCLI からペイロードを復号化できます。これらに対して 2 つの異なるコードベースを作成して維持する代わりに、ペイロードを暗号化するエッジコンポーネントと、それらを復号化するUIとCLI で同じ実装を再利用することを選択しました。これを実現するために、ブラウザで実行されるダッシュボード UI コードで使用できるように、ライブラリをコンパイルしてWASMをターゲットにします。このアプローチでは、JavaScript バンドルのサイズがやや大きくなり、計算オーバーヘッドは比較的小さくなりますが、JavaScript [WebCrypto](https://developer.mozilla.org/en-US/docs/Web/API/Web_Crypto_API)プリミティブを使用して HPKE を安全に再実装するのに多くの時間を費やす方が望ましいと考えました。

当社で決定したHPKEの実装には、正式な監査がいまだ行われていないという警告が表示されます。そのため、Cloudflareでは独自の内部セキュリティレビューを行いました。そして、使用されている暗号プリミティブと対応するライブラリを分析しました。上述したプリミティブの構成と、メモリを正しくゼロにしたり、乱数ジェネレーターを使うなど、安全なプログラミングプラクティスとの間にセキュリティ上の問題は見つかりませんでした。

### **ユーザーの安全性を確保する**

ユーザーの代わりに当社が暗号化するには、ユーザーから当社にパブリックキーを提供してもらう必要があります。これをできるだけ簡単にするために、CLIツールと、ブラウザでこれを正しく行う機能を構築しました。どちらのオプションでも、ユーザーはCloudflareサーバーにまったく連絡することなく、パブリックキー/プライベートキーのペアを作成することができます。

当社のAPIでは、特にキーペアのプライベートキーを受け付けません。—むしろ受け付けたくない！当社が保存しているデータを復号化できるようにする必要はありませんし、当社としては、そうしたくないでのす。

ダッシュボードでは、ユーザーが復号化のためにプライベートキーを提供すると、当該キーは一時的なJavaScript 変数として保存され、ブラウザ内復号化に使用されます。これにより、ファイアウォールイベントログを参照している間、ユーザーは常にキーを提供する必要がありません。また、プライベートキーはいかなる方法でもブラウザに残されることはありません。このため、ページの更新や移動など、ページを更新するアクションでは、ユーザーはもう一度、キーを提供する必要があります。使いやすさの面では少々落ちますが、これはセキュリティ強化のためには必要なことだと考えています。

### **ペイロード抽出の仕組み**

データを暗号化する方法を決定したら、暗号化するデータ、保存および送信方法、ユーザーが復号化できるようにする方法など、残りの機能を決める必要がありました。

HTTPリクエストがL7ファイアウォールに到達すると、一連のルールセットを使って評価されます。これらのルールセットは、[wirefilter](https://github.com/cloudflare/wirefilter)構文で書かれたいくつかのルールが含まれています。

これらのルールの例としては、次のようなものがあります。
    
    
    http.request.version eq "HTTP/1.1"
    and
    (
        http.request.uri.path matches "\n+."
        or
        http.request.uri.query matches "\x00+."
    )

この式では、1つまたは複数の改行の後にリクエストパスの1文字が続くか、1つまたは複数のNULLバイトの後にクエリ文字で書かれた文字が続くいずれかの形式で表示されるHTTP/1.1リクエストのブール値を「true」と評価します。

それでは、上記のルールに一致する次のリクエストがあったとしましょう。
    
    
    GET /cms/%0Aadmin?action=%00post HTTP/1.1
    Host: example.com

一致したデータログが有効になっている場合、一致したルールは、実行中にアクセスされたすべてのフィールドにタグを付ける特別なコンテキストで再び実行されます。このタグ付けによって計算オーバーヘッドが顕著になり、大多数のリクエストではルールがまったくトリガーされず、各リクエストにオーバーヘッドを不必要に追加するため、この2回目の実行を行います。ルールに一致するリクエストは、いくつかのルールにのみ一致するため、ルールセットの大部分を再実行する必要はありません。

`http.request.uri.query matches "\x00+."`は、このリクエストをtrue と評価するのに、実行されないことにお気づきかもしれません。なぜなら、この式は、最初に、もしくは一致するコンディションを使って、ショートカットされるからです。この結果、 `http.request.versionとhttp.request.uri.path`はアクセス済みであるとタグ付けされます。
    
    
    http.request.version -> HTTP/1.1
    http.request.uri.path -> /cms/%0Aadmin

アクセスされたフィールドを集めた後、ファイアウォールエンジンは、他のサブセット（クエリ文字列や完全な URI など）であるフィールドの削除、または特定の文字数（長さ）を超えるフィールドの切り捨てなど、いくつかの後処理を行います。

最後に、これらはJSONとしてシリアル化され、お客様のパブリックキーで暗号化されます。そして、バイトセットとして再びシリアル化されて、将来的に変更/更新の必要がある場合は、バージョン番号がプレフィックスとして付加されます。これらのブロブの消費を簡素化するために、APIはBase64でエンコードされたバイトのバージョンを表示します。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Using HPKE to Encrypt Request Payloads Embedded Image - bnLtIB](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45X7CTVZZPP4YQZPEYY652.png&w=715&h=591&f=webp&fit=cover&position=center)

Edgeでデータを暗号化し、[ClickHouse](https://blog.cloudflare.com/tag/clickhouse/)でそれを保存したので、今度はユーザーが復号化できるようにする必要があります。この機能を有効にするセットアップの一環として、ユーザーはキーペアを作成しました。キーペアはペイロードの暗号化に使用されるパブリックキーと、それらを復号化するために使用されるプライベートキーです。復号化は、[cloudflare/matched-data-cli](https://github.com/cloudflare/matched-data-cli)を使ったコマンドラインを使用して完全にオフラインで行われるか：
    
    
    $ MATCHED_DATA=AkjQDktMX4FudxeQhwa0UPNezhkgLAUbkglNQ8XVCHYqPgAAAAAAAACox6cEwqWQpFVE2gCFyOFsSdm2hCoE0/oWKXZJGa5UPd5mWSRxNctuXNtU32hcYNR/azLjsGO668Jwk+qCdFvmKjEqEMJgI+fvhwLQmm4=
    $ matched-data-cli decrypt -d $MATCHED_DATA -k $PRIVATE_KEY
    {"http.request.version": "HTTP/1.1", "http.request.uri.path": "/cms/%0Aadmin"}

または、ダッシュボードUIを使用して行われます。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Using HPKE to Encrypt Request Payloads Embedded Image - 9EO0J7](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46QYB2Y3AN5G0WKH0AP97Q.png&w=715&h=526&f=webp&fit=cover&position=center)

当社のCLIツールはオープンソースであり、HPKEは相互運用性があるため、セキュリティ情報およびイベント管理（SIEM）ソフトウェアなど、ユーザーのロギングパイプラインの一部として、他のツールでも使用できます。

### **まとめ**

これは、プロセス全体を通して、当社の研究チームとセキュリティチームの協力で達成できたことでした。当社は、アルゴリズムを評価するのに最適な方法についての助言や、使用したいライブラリを審査する際に、チームからのサポートを受けました。

実装のしやすさとパフォーマンスの観点から、HPKEのこれまでの働きに非常に満足しています。セキュリティの標準化が求められている状況の中で、セキュリティとパフォーマンスの両方の機能を最大限に生かすことを考えると、当社にとっては簡単な選択でした。

このページ

オンラインで議論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fusing-hpke-to-encrypt-request-payloads%2F&t=HPKE%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%97%E3%81%9F%E3%83%AA%E3%82%AF%E3%82%A8%E3%82%B9%E3%83%88%E3%83%9A%E3%82%A4%E3%83%AD%E3%83%BC%E3%83%89%E3%81%AE%E6%9A%97%E5%8F%B7%E5%8C%96)[](https://x.com/intent/post?text=HPKE%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%97%E3%81%9F%E3%83%AA%E3%82%AF%E3%82%A8%E3%82%B9%E3%83%88%E3%83%9A%E3%82%A4%E3%83%AD%E3%83%BC%E3%83%89%E3%81%AE%E6%9A%97%E5%8F%B7%E5%8C%96&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fusing-hpke-to-encrypt-request-payloads%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fusing-hpke-to-encrypt-request-payloads%2F)[](https://bsky.app/intent/compose?text=HPKE%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%97%E3%81%9F%E3%83%AA%E3%82%AF%E3%82%A8%E3%82%B9%E3%83%88%E3%83%9A%E3%82%A4%E3%83%AD%E3%83%BC%E3%83%89%E3%81%AE%E6%9A%97%E5%8F%B7%E5%8C%96+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fusing-hpke-to-encrypt-request-payloads%2F)[](https://mastodonshare.com/?text=HPKE%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%97%E3%81%9F%E3%83%AA%E3%82%AF%E3%82%A8%E3%82%B9%E3%83%88%E3%83%9A%E3%82%A4%E3%83%AD%E3%83%BC%E3%83%89%E3%81%AE%E6%9A%97%E5%8F%B7%E5%8C%96&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fusing-hpke-to-encrypt-request-payloads%2F)[](https://www.threads.net/intent/post?text=HPKE%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%97%E3%81%9F%E3%83%AA%E3%82%AF%E3%82%A8%E3%82%B9%E3%83%88%E3%83%9A%E3%82%A4%E3%83%AD%E3%83%BC%E3%83%89%E3%81%AE%E6%9A%97%E5%8F%B7%E5%8C%96+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fusing-hpke-to-encrypt-request-payloads%2F)

## 関連するタグ

[WAF](https://blog.cloudflare.com/ja-jp/tag/waf/)[WAF Rules](https://blog.cloudflare.com/ja-jp/tag/waf-rules/)[セキュリティ](https://blog.cloudflare.com/ja-jp/tag/security/)[ファイアウォール](https://blog.cloudflare.com/ja-jp/tag/firewall/)[暗号](https://blog.cloudflare.com/ja-jp/tag/cryptography/)

SNS をフォロー

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)

  * ![Miguel de Moura](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW469GP192YFYYEYAD222W8R.jpg&w=64&h=64&f=webp&fit=cover&position=center)[Miguel de Moura](https://blog.cloudflare.com/ja-jp/author/miguel/)

[](https://migueldemoura.com)




## 新しい投稿のお知らせを受け取るように登録する

メールアドレス

また、あなたのメールアドレスを共有したりすることはございません。

登録する

ご購読ありがとうございます！受信箱を確認して登録してください。
