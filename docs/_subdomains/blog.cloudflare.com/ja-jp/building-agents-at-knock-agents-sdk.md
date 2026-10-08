---
url: https://blog.cloudflare.com/ja-jp/building-agents-at-knock-agents-sdk/
title: Knock\u3068Cloudflare\u306e\u30a8\u30fc\u30b8\u30a7\u30f3\u30c8SDK\u3067\u4eba\u9593\u3092\u30eb\u30fc\u30d7\u306b\u5165\u308c\u308bAI\u30a8\u30fc\u30b8\u30a7\u30f3\u30c8\u306e\u69cb\u7bc9 | Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:51:56.076587+00:00
---

# KnockとCloudflareのエージェントSDKで人間をループに入れるAIエージェントの構築 | Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/building-agents-at-knock-agents-sdk/

[ブログ](https://blog.cloudflare.com/ja-jp/)

[AI](https://blog.cloudflare.com/ja-jp/tag/ai/)[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[Durable Objects](https://blog.cloudflare.com/ja-jp/tag/durable-objects/)3件3件タグを表示

6 タグタグを6件表示

  * 投稿タグ
  * [AI](https://blog.cloudflare.com/ja-jp/tag/ai/)[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[Durable Objects](https://blog.cloudflare.com/ja-jp/tag/durable-objects/)[エージェント](https://blog.cloudflare.com/ja-jp/tag/agents/)[開発者](https://blog.cloudflare.com/ja-jp/tag/developers/)[開発者プラットフォーム](https://blog.cloudflare.com/ja-jp/tag/developer-platform/)
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



[エージェント](https://blog.cloudflare.com/ja-jp/tag/agents/)[開発者](https://blog.cloudflare.com/ja-jp/tag/developers/)[開発者プラットフォーム](https://blog.cloudflare.com/ja-jp/tag/developer-platform/)

[AI](https://blog.cloudflare.com/ja-jp/tag/ai/)[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[Durable Objects](https://blog.cloudflare.com/ja-jp/tag/durable-objects/)[エージェント](https://blog.cloudflare.com/ja-jp/tag/agents/)[開発者](https://blog.cloudflare.com/ja-jp/tag/developers/)[開発者プラットフォーム](https://blog.cloudflare.com/ja-jp/tag/developer-platform/)

2025年6月3日

# KnockとCloudflareのエージェントSDKで人間をループに入れるAIエージェントの構築

![Chris Bell](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44TJTR2HDGVYJM38MT7A3B.png&w=64&h=64&f=webp&fit=cover&position=center)

[Chris Bell](https://blog.cloudflare.com/ja-jp/author/chris-bell/)

13分で読了

URLをコピー

この記事は以下でも利用可能です [English](https://blog.cloudflare.com/building-agents-at-knock-agents-sdk/)、[简体中文](https://blog.cloudflare.com/zh-cn/building-agents-at-knock-agents-sdk/).

![hero-knock-cloudflare-agents](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46QCKTCHGAPJHB839D0TS6.png&w=2000&h=1126&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAAaE+cZmSwZIXQapjedpjSfom5fXendWynaWmsZ3i9ZpLYbqPjfaPYhpfAg4eveHquan27aYjIap3fdavohq3cj6PGipS2fYe0aoTCa43NcJ/ffq3mja7alKXFkJi2g4y2aHu/bIXIeJfYh6TckqXPl5y7kpCwioezZWW0bnG9f4fLjpTNlZO/lYqsk4ClkHurY0aob1iwhXS9k4K+loCvk3WckmyZlGykYjSib0urh2u4lXq4l3eokmuWkWOUlWah)

_このコンテンツは自動機械翻訳サービスによる翻訳版であり、皆さまの便宜のために提供しています。原本の英語版と異なる誤り、省略、解釈の微妙な違いが含まれる場合があります。ご不明な点がある場合は、英語版原本をご確認ください。_

 _[_これは、KnockのCTOであるChris_](https://knock.app/) Bell氏によるゲスト投稿です_

今、[AIエージェント](https://www.cloudflare.com/learning/ai/what-is-agentic-ai/)の構築についてはよく話題になっていますが、AIエージェントを真に _有用_ にするために必要なことについてはあまり知られていません。

エージェントは、人間の介入なしに、特定の目標または一連の目標を達成するために意思決定を行い、アクションを実行するように設計された自律システムです。

エージェントがどれほど意思決定が優れていても、エージェントが目標に向けて進む道のりについてガイダンスやインプットを提供する人が必要になります。結局、外部の世界とそれを管理するシステムとの対話や応答ができないエージェントは、解決できる問題が限定的になります。

そこで登場するのが「ヒューマン・イン・ザ・ループ」と呼ばれる対話パターンです。人間をエージェントのループ _に入れて_ 、エージェントがタスクを継続する前に、その人間からの入力を必要とします。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2809 image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4898YAFZHB7GEBXJW520N4.png&w=625&h=565&f=webp&fit=cover&position=center)

このブログ記事では、[ _Knock_](https://knock.app/)とCloudflare[ _Agents SDK_](https://developers.cloudflare.com/agents/)を使用して、新規カードがリクエストされた際に人間の承認が必要な仮想カード発行ワークフロー用のAIエージェントを構築します。

この例の完全なコードは、[ _リポジトリで_](https://github.com/knocklabs/ai-agent-examples/tree/main/card-issue-agent)確認できます。

## Knockとは？

[ _Knock_](https://knock.app/)はメッセージングインフラストラクチャで、統合コードを書くことなく、アプリ内、メール、SMS、プッシュ、Slackでマルチチャンネルメッセージを送信することができます。

Knockを使用すると、ユーザーに送信されるメッセージを完全に可視化できると同時に、信頼性の高い配信やユーザー通知の設定などの処理が可能になります。

Knockを使用して、KnockのAPIとメッセージ機能をAIエージェントに公開する一連のツールであるKnockの[ _エージェントツールキット_](https://docs.knock.app/developer-tools/agent-toolkit/overview)を使用して、エージェントのヒューマンインザループフローを強化することができます。

## AIエージェントの基盤としてエージェントSDKを使用する

Agents SDKは、[ _Durable Objects_](https://developers.cloudflare.com/durable-objects/)上にステートフルなリアルタイムエージェントを構築するための抽象化を提供します。Durable Objectsは、グローバルにアドレス指定でき、埋め込まれた、[ _ゼロ遅延_](https://blog.cloudflare.com/sqlite-in-durable-objects/)のSQLiteデータベースを使って状態を保持します。

Agents SDKとCloudflareプラットフォームの外でAIエージェントを構築する場合、WebSocketサーバー、状態の永続性、サービスを水平に拡張する方法を考慮する必要があります。Durable ObjectがAgents SDKをサポートしているため、これらのメリットを無料で享受できます。また、ストレージが組み込まれたグローバルでアドレス指定可能なコンピュートを持つことができます。これは完全にサーバーレスで、ゼロに拡張できます。

例では、これらの機能を使って、ユーザーがチャットを介してリアルタイムでやり取りし、必要に応じて一時停止や再開が可能なエージェントを構築します。Agents SDKは、ヒューマンインザループ（Human-in-the-Loop）対話で必要となるような非同期のエージェントワークフローを実行するのに理想的なプラットフォームです。

## Knockメッセージングのワークフローを設定する

Knock内では、Visual Workflow Builderを使って承認ワークフローを設計し、クロスチャネルメッセージのロジックを作成しています。次に、メッセージを送信する各チャンネルに関連付けた通知テンプレートを作成します。

Knockは、ワークフローの実行の一部として[ _ユーザーの環境設定_](https://docs.knock.app/concepts/preferences)を自動的に適用し、ユーザーの通知設定を確実に反映します。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2809 image 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47KQYJHW2XNJSRTDKKM1Y3.png&w=715&h=465&f=webp&fit=cover&position=center)

このデモ用にすでに作成したワークフロー例をリポジトリで確認できます。この[ _Knock CLI_](https://docs.knock.app/cli)を介してこのワークフローテンプレートを使用して、アカウントにインポートすることができます。

## チャットUIの構築

CloudflareのエージェントSDK（ドキュメント ）の` AIChatAgent の抽象化の上に、チャットインターフェースとしてAIエージェントを構築しました。`ここのAgents SDKは複雑さの大部分を処理し、私たちはプロンプトでLLM呼び出しコードを実装するだけです。
    
    
    // src/index.ts
    
    import { AIChatAgent } from "agents/ai-chat-agent";
    import { openai } from "@ai-sdk/openai";
    import { createDataStreamResponse, streamText } from "ai";
    
    export class AIAgent extends AIChatAgent {
      async onChatMessage(onFinish) {
        return createDataStreamResponse({
          execute: async (dataStream) => {
            try {
              const stream = streamText({
                model: openai("gpt-4o-mini"),
                system: `You are a helpful assistant for a financial services company. You help customers with credit card issuing.`,
                messages: this.messages,
                onFinish,
                maxSteps: 5,
              });
    
              stream.mergeIntoDataStream(dataStream);
            } catch (error) {
              console.error(error);
            }
          },
        });
      }
    }

クライアント側では、` agents/ai-react` パッケージの` useAgentChat` フックを使用して、ユーザーとエージェントのリアルタイムチャットを強化します。

`エージェントをユーザーごとのチャットとしてモデル化しました。ユーザーIdとしてプロセス名を指定し、` `useAgentフックを使用してセットアップします。`
    
    
    // src/index.ts
    
    import { useAgent } from "agents/react";
    import { useAgentChat } from "agents/ai-react";
    
    function Chat({ userId }: { userId: string }) {
      const agent = useAgent({ agent: "AIAgent", name: userId });
      const { messages, input, handleInputChange, handleSubmit, isLoading } = useAgentChat({ agent });
      // ... 
    }

これはつまり、ユーザーごとにエージェントプロセスがあり、耐久性のあるオブジェクトがあるということです。ヒューマン・イン・ザ・ループのユースケースでは、これは後に、遅延したツール呼び出しを再開することについて説明する際に重要になります。

## ツールの呼び出しをKnockに先延ばしに

弊社では`issueCard`ツールを公開することで、エージェントにカード発行機能を提供します。しかし、承認フローとクロスチャネルロジックを自分たちで書くのではなく、問題カードツールを`必要とするHumanInput`メソッドでラップすることによって、すべてをKnockに委任しました。

今、ユーザーが新しいカードを要求すると、Knockにカード要求を開始するための呼び出しを行い、Knockは組織内の適切な管理者に通知して承認を要求します。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2809 image 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46BDGT06TG0S4E18SD780X.png&w=715&h=237&f=webp&fit=cover&position=center)

これを設定するには、Knockのエージェントツールキットを使用する必要があります。このキットは、AIエージェントでKnockと連携し、クロスチャネルメッセージングを強化する方法を公開します。
    
    
    import { createKnockToolkit } from "@knocklabs/agent-toolkit/ai-sdk";
    import { tool } from "ai";
    import { z } from "zod";
    
    import { AIAgent } from "./index";
    import { issueCard } from "./api";
    import { BASE_URL } from "./constants";
    
    async function initializeToolkit(agent: AIAgent) {
      const toolkit = await createKnockToolkit({ serviceToken: agent.env.KNOCK_SERVICE_TOKEN });
    
      const issueCardTool = tool({
        description: "Issue a new credit card to a customer.",
        parameters: z.object({
          customerId: z.string(),
        }),
        execute: async ({ customerId }) => {
          return await issueCard(customerId);
        },
      });
    
      const { issueCard } = toolkit.requireHumanInput(
        { issueCard: issueCardTool },
        {
          workflow: "approve-issued-card",
          actor: agent.name,
          recipients: ["admin_user_1"],
          metadata: {
            approve_url: `${BASE_URL}/card-issued/approve`,
            reject_url: `${BASE_URL}/card-issued/reject`,
          },
        }
      );
      
      return { toolkit, tools: { issueCard } };  
    }

多くのことが行われているため、主要な部分について順に説明しましょう。

  * `IsissueCard`ツールを`recreedHumanInput`メソッドでラップし、Knock Agentツールキットから公開されます。
  * メッセージングのワークフローを`カード発行承認`のワークフローにする
  * `リクエストのアクター`としてagent.nameを渡します。これはユーザーIDに変換されます。
  * このワークフローの受信者をユーザー`admin_user_1`に設定します。
  * メッセージテンプレートで使用できるように、承認URLと拒否URLを渡します
  * ラップされたツールが`issueCard`として返される



内部では、これらのオプションが[ _KnockワークフロートリガーAPI_](https://docs.knock.app/api-reference/workflows/trigger)に渡され、受信者ごとにワークフローを呼び出します。ここに一覧化されている受信者のセットは動的であるか、[ _KnockのサブスクリプションAPI_](https://docs.knock.app/concepts/subscriptions)を通じてユーザーグループに送られているかもしれません。

そして、ラップされた発行カードツールをエージェントの`onChatMessage`メソッドでLLMコールに渡すことができ、エージェントとのインタラクションの一部としてツールコールを呼び出すことができます。
    
    
    export class AIAgent extends AIChatAgent {
      // ... other methods
    
      async onChatMessage(onFinish) {
        const { tools } = await initializeToolkit(this);
    
        return createDataStreamResponse({
          execute: async (dataStream) => {
            const stream = streamText({
              model: openai("gpt-4o-mini"),
              system: "You are a helpful assistant for a financial services company. You help customers with credit card issuing.",
              messages: this.messages,
              onFinish,
              tools,
              maxSteps: 5,
            });
    
            stream.mergeIntoDataStream(dataStream);
          },
        });
      }
    }

エージェントが`issueCardTool`を呼び出すと、Knockを呼び出して承認通知を送信し、承認を受けるまでカードを発行するツールコールを遅らせます。Knockのワークフローは、指定された受信者グループへのメッセージの送信を処理し、各ユーザーの好みに合わせてメッセージを生成・配信します。

当社の承認メッセージにKnockワークフローを使用することで、ユーザーのコミュニケーションプリファレンスに合わせたクロスチャネルメッセージングを簡単に構築することができます。また、[ _遅延_](https://docs.knock.app/designing-workflows/delay-function)、[ _スロットル_](https://docs.knock.app/designing-workflows/throttle-function)、[ _バッチ_](https://docs.knock.app/designing-workflows/batch-function)、[ _条件_](https://docs.knock.app/designing-workflows/step-conditions)を利用して、より複雑なメッセージングを調整することもできます。

## 承認の処理

メッセージが承認者に送信されたら、次のステップは、返されてくる承認の処理を行い、人間をエージェントのループに入れることです。

承認リクエストは非同期的です。つまり、将来の時点はいつでも応答可能です。幸いなことに、Knockがここでの面倒な作業を担い、基盤となるメッセージとのインタラクションを追跡する[ _Webhook_](https://docs.knock.app/developer-tools/outbound-webhooks/overview)を介してエージェントWorkerにイベントをルーティングします。この場合は、「承認」または「却下」ボタンをクリックします。

まず、Knockダッシュボード内に`message.interacted` webhookハンドラーを設定し、インタラクションをWorkerに、そして最終的にはエージェントプロセスに転送します。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2809 image 4](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW479AD0WTM2T84DFCQX20T9.png&w=715&h=465&f=webp&fit=cover&position=center)

ここの例では、承認のクリックをWorkerにルーティングして処理し、`確認用URL`と`排除_URL`の最後にKnockメッセージIDを追加して、送信された特定のメッセージに対してエンゲージメントを追跡します。これは、Knockのメッセージテンプレートの中にあるリキッドを介して行っています： `{{ data.approve_url }}?messageId={{ current_message.id }} `。ここで注意すべき点は、これが本番アプリケーションの場合、このエージェントが実行しているわけではなく、別のアプリケーションで承認のクリックを処理する可能性があるということです。このデモのためだけに、こちらに設置しました。

リンクがクリックされると、workerにハンドラーがあり、Knockの[ _メッセージインタラクションAPI_](https://docs.knock.app/api-reference/messages/mark_as_interacted)を使ってメッセージが対話済みであるとマークし、ステータスをメタデータとして通過させて、後で使用できるようにします。
    
    
    import Knock from '@knocklabs/node';
    import { Hono } from "hono";
    
    const app = new Hono();
    const client = new Knock();
    
    app.get("/card-issued/approve", async (c) => {
      const { messageId } = c.req.query();
      
      if (!messageId) return c.text("No message ID found", { status: 400 });
    
      await client.messages.markAsInteracted(messageId, {
        status: "approved",
      });
    
      return c.text("Approved");
    });

メッセージの対話は、当社が設定したWebhookを介してKnockからworkerに流れ、プロセスが完全に非同期であるようにします。Webhookの悪意のあるペイロードには、元のリクエストを生成したユーザーに関するメタデータを含む完全なメッセージが含まれ、リクエスト自体（この場合はツール呼び出しを含む）に関する詳細を保持します。
    
    
    import { getAgentByName, routeAgentRequest } from "agents";
    import { Hono } from "hono";
    
    const app = new Hono();
    
    app.post("/incoming/knock/webhook", async (c) => {
      const body = await c.req.json();
      const env = c.env as Env;
    
      // Find the user ID from the tool call for the calling user
      const userId = body?.data?.actors[0];
    
      if (!userId) {
        return c.text("No user ID found", { status: 400 });
      }
    
      // Find the agent DO for the user
      const existingAgent = await getAgentByName(env.AIAgent, userId);
    
      if (existingAgent) {
        // Route the request to the agent DO to process
        const result = await existingAgent.handleIncomingWebhook(body);
    
        return c.json(result);
      } else {
        return c.text("Not found", { status: 404 });
      }
    });

名前付きの識別子によってアドレス指定されるエージェントの能力を利用して、リクエストをworkerからエージェントにルーティングします。この場合、これは `userId` です。エージェントは耐久性のあるオブジェクトで支えられているため、incoming workerリクエストからエージェントを見つけて再開するまでのプロセスは簡単です。

## 遅延したツール呼び出しを再開します

次に、元のツール呼び出しに関するコンテキストを使用し、Knockに渡してエージェントにラウンドトリップし、ツールの実行を再開し、カードを発行します。
    
    
    export class AIAgent extends AIChatAgent {
      // ... other methods
    
      async handleIncomingWebhook(body: any) {
        const { toolkit } = await initializeToolkit(this);
    
        const deferredToolCall = toolkit.handleMessageInteraction(body);
    
        if (!deferredToolCall) {
          return { error: "No deferred tool call given" };
        }
    
        // If we received an "approved" status then we know the call was approved 
        // so we can resume the deferred tool call execution
        if (result.interaction.status === "approved") {
          const toolCallResult = 
    	      await toolkit.resumeToolExecution(result.toolCall);
    
          const { response } = await generateText({
            model: openai("gpt-4o-mini"),
            prompt: `You were asked to issue a card for a customer. The card is now approved. The result was: ${JSON.stringify(toolCallResult)}.`,
          });
    
          const message = responseToAssistantMessage(
            response.messages[0],
            result.toolCall,
            toolCallResult
          );
    
          // Save the message so that it's displayed to the user
          this.persistMessages([...this.messages, message]);
        }
    
        return { status: "success" };
      }
    }

ここでも多くのことが行われているため、重要な部分について順に説明します。

  * 本文（Knockからのwebhookペイロード）を`handleMessageInteraction`メソッドを介して遅延ツール呼び出しに変換しようとします。
  * 先ほどインタラクション呼び出しに渡したメタデータのステータスが「承認」ステータスの場合、`ResumeToolExecution`メソッドを介してツール呼び出しを再開します
  * 最後に、LLMからメッセージを生成して保持し、ユーザーに承認されたカードについて知らせます



この最後のピースが配置されたことで、新しいカードの発行をリクエストし、エージェントから承認リクエストを送付し、承認メッセージを送信し、その承認をエージェントにルーティングして処理することができます。エージェントはカード発行リクエストを非同期的に処理し、遅延ツールコールはほとんど少ないコードで再開されます。

## 重複承認から保護

上記の実装の問題の1つは、誰かが承認ボタンを複数回クリックすると、複数のカードが発行される傾向があることです。この問題を是正するために、発行されているツールコールを追跡し、呼び出しが最も一度に処理されるようにしたいと考えています。

これを強化するために、データベースやRedisのような他の永続ストアに到達することなく、情報を保持することができる[ _エージェントのビルトインステート_](https://developers.cloudflare.com/agents/api-reference/store-and-sync-state/)を活用しますが、その気になれば絶対にそうすることもできます。エージェントプロセスの中で、IDによってツールの呼び出しを追跡し、現在のステータスを把握することができます。
    
    
    type ToolCallStatus = "requested" | "approved" | "rejected";
    
    export interface AgentState {
      toolCalls: Record<string, ToolCallStatus>;
    }
    
    class AIAgent extends AIChatAgent<Env, AgentState> {
      initialState: AgentState = {
        toolCalls: {},
      };
      
      setToolCallStatus(toolCallId: string, status: ToolCallStatus) {
        this.setState({
          ...this.state,
          toolCalls: { ...this.state.toolCalls, [toolCallId]: status },
        });
      } 
      // ... 
    }

ここでは、ツール呼び出しの初期状態を空のオブジェクトとして作成します。また、クイックセクターヘルパーメソッドを追加して、インタラクションを容易にします。

次に、ツールの呼び出しを記録する必要があります。これを行うには、` requireHumanInput` `ヘルパーのonAfterCallKnockオプションを使って、ツール呼び出しがユーザーにリクエストされたことをキャプチャします。`
    
    
    const { issueCard }  = toolkit.requireHumanInput(
      { issueCard: issueCardTool },
      {
        // Keep track of the tool call state once it's been sent to Knock
        onAfterCallKnock: async (toolCall) => 
          agent.setToolCallStatus(toolCall.id, "requested"),
        // ... as before
      }
    );

最後に、受信webhookを処理しているときに状態をチェックし、ツール呼び出しを承認としてマークする必要があります（簡潔にするために一部のコードを省略しています）。
    
    
    export class AIAgent extends AIChatAgent {
      async handleIncomingWebhook(body: any) {
        const { toolkit } = await initializeToolkit(this);
        const deferredToolCall = toolkit.handleMessageInteraction(body);
        const toolCallId = result.toolCall.id;
    
        // Make sure this is a tool call that can be processed
        if (this.state.toolCalls[toolCallId] !== "requested") {
          return { error: "Tool call is not requested" };
        }
    
        if (result.interaction.status === "approved") {
          const toolCallResult = await toolkit.resumeToolExecution(result.toolCall);
          this.setToolCallStatus(toolCallId, "approved");
          // ... rest as before
        }
      }
    }

## まとめ

Agents SDKとKnockを使用すれば、ツールの呼び出しを遅らせる高度なヒューマンインザループエクスペリエンスを簡単に構築できます。

Knockのワークフロービルダーと通知エンジンは、エージェントに洗練されたクロスチャンネルメッセージを作成するためのビルディングブロックを提供します。SMS、プッシュ、メール、Slackでメッセージを送信し、ユーザーの通知設定を尊重するエスカレーションフローを簡単に作成することができます。また、Knockはユーザーが受信しているメッセージを完全に可視化することもできます。

Agents SDKの下にあるDurable Object抽象化は、中断や再開が簡単にできるグローバルにアドレス指定できるエージェントプロセスを提供することを意味します。Durable Objectの永続ストレージは、ユーザーごとの完全なチャット履歴や、エージェントを再開するために必要なその他の状態（ツール呼び出しなど）を保持できることを意味します。最後に、基盤となるDurable Objectのサーバーレス性質により、労力をかけずに水平方向に拡張し、多数のユーザーをサポートします。

マルチプレイヤーのヒューマンインザループ体験で独自のAIエージェントチャット体験を構築することをお考えの方は、このガイドに掲載されている完全なコードが[ _GitHubで利用可能です_](https://github.com/knocklabs/ai-agent-examples/tree/main/card-issue-agent)。

このページ

オンラインで議論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fbuilding-agents-at-knock-agents-sdk%2F&t=Knock%E3%81%A8Cloudflare%E3%81%AE%E3%82%A8%E3%83%BC%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%88SDK%E3%81%A7%E4%BA%BA%E9%96%93%E3%82%92%E3%83%AB%E3%83%BC%E3%83%97%E3%81%AB%E5%85%A5%E3%82%8C%E3%82%8BAI%E3%82%A8%E3%83%BC%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%88%E3%81%AE%E6%A7%8B%E7%AF%89)[](https://x.com/intent/post?text=Knock%E3%81%A8Cloudflare%E3%81%AE%E3%82%A8%E3%83%BC%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%88SDK%E3%81%A7%E4%BA%BA%E9%96%93%E3%82%92%E3%83%AB%E3%83%BC%E3%83%97%E3%81%AB%E5%85%A5%E3%82%8C%E3%82%8BAI%E3%82%A8%E3%83%BC%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%88%E3%81%AE%E6%A7%8B%E7%AF%89&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fbuilding-agents-at-knock-agents-sdk%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fbuilding-agents-at-knock-agents-sdk%2F)[](https://bsky.app/intent/compose?text=Knock%E3%81%A8Cloudflare%E3%81%AE%E3%82%A8%E3%83%BC%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%88SDK%E3%81%A7%E4%BA%BA%E9%96%93%E3%82%92%E3%83%AB%E3%83%BC%E3%83%97%E3%81%AB%E5%85%A5%E3%82%8C%E3%82%8BAI%E3%82%A8%E3%83%BC%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%88%E3%81%AE%E6%A7%8B%E7%AF%89+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fbuilding-agents-at-knock-agents-sdk%2F)[](https://mastodonshare.com/?text=Knock%E3%81%A8Cloudflare%E3%81%AE%E3%82%A8%E3%83%BC%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%88SDK%E3%81%A7%E4%BA%BA%E9%96%93%E3%82%92%E3%83%AB%E3%83%BC%E3%83%97%E3%81%AB%E5%85%A5%E3%82%8C%E3%82%8BAI%E3%82%A8%E3%83%BC%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%88%E3%81%AE%E6%A7%8B%E7%AF%89&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fbuilding-agents-at-knock-agents-sdk%2F)[](https://www.threads.net/intent/post?text=Knock%E3%81%A8Cloudflare%E3%81%AE%E3%82%A8%E3%83%BC%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%88SDK%E3%81%A7%E4%BA%BA%E9%96%93%E3%82%92%E3%83%AB%E3%83%BC%E3%83%97%E3%81%AB%E5%85%A5%E3%82%8C%E3%82%8BAI%E3%82%A8%E3%83%BC%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%88%E3%81%AE%E6%A7%8B%E7%AF%89+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fbuilding-agents-at-knock-agents-sdk%2F)

## 関連するタグ

[AI](https://blog.cloudflare.com/ja-jp/tag/ai/)[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[Durable Objects](https://blog.cloudflare.com/ja-jp/tag/durable-objects/)[エージェント](https://blog.cloudflare.com/ja-jp/tag/agents/)[開発者](https://blog.cloudflare.com/ja-jp/tag/developers/)[開発者プラットフォーム](https://blog.cloudflare.com/ja-jp/tag/developer-platform/)

SNS をフォロー

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 新しい投稿のお知らせを受け取るように登録する

メールアドレス

また、あなたのメールアドレスを共有したりすることはございません。

登録する

ご購読ありがとうございます！受信箱を確認して登録してください。
