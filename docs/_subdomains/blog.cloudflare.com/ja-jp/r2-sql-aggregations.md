---
url: https://blog.cloudflare.com/ja-jp/r2-sql-aggregations/
title: R2 SQL\u3067\u306eGROUP BY\u3001SUM\u3001\u305d\u306e\u4ed6\u306e\u96c6\u7d04\u30af\u30a8\u30ea\u306e\u30b5\u30dd\u30fc\u30c8\u3092\u767a\u8868 | Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:46:46.915914+00:00
---

# R2 SQLでのGROUP BY、SUM、その他の集約クエリのサポートを発表 | Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/r2-sql-aggregations/

[ブログ](https://blog.cloudflare.com/ja-jp/)

[R2](https://blog.cloudflare.com/ja-jp/tag/r2/)[Rust](https://blog.cloudflare.com/ja-jp/tag/rust/)[SQL](https://blog.cloudflare.com/ja-jp/tag/sql/)3件3件タグを表示

6 タグタグを6件表示

  * 投稿タグ
  * [R2](https://blog.cloudflare.com/ja-jp/tag/r2/)[Rust](https://blog.cloudflare.com/ja-jp/tag/rust/)[SQL](https://blog.cloudflare.com/ja-jp/tag/sql/)[エッジコンピューティング](https://blog.cloudflare.com/ja-jp/tag/edge-computing/)[サーバーレス](https://blog.cloudflare.com/ja-jp/tag/serverless/)[データ](https://blog.cloudflare.com/ja-jp/tag/data/)
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



[エッジコンピューティング](https://blog.cloudflare.com/ja-jp/tag/edge-computing/)[サーバーレス](https://blog.cloudflare.com/ja-jp/tag/serverless/)[データ](https://blog.cloudflare.com/ja-jp/tag/data/)

[R2](https://blog.cloudflare.com/ja-jp/tag/r2/)[Rust](https://blog.cloudflare.com/ja-jp/tag/rust/)[SQL](https://blog.cloudflare.com/ja-jp/tag/sql/)[エッジコンピューティング](https://blog.cloudflare.com/ja-jp/tag/edge-computing/)[サーバーレス](https://blog.cloudflare.com/ja-jp/tag/serverless/)[データ](https://blog.cloudflare.com/ja-jp/tag/data/)

2025年12月18日

# R2 SQLでのGROUP BY、SUM、その他の集約クエリのサポートを発表

![Jérôme Schneider](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47478FBJFPA57ZWACE3FDC.png&w=64&h=64&f=webp&fit=cover&position=center)![Nikita Lapkov](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46GWQBCE99JFFMKC6GVZEX.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Marc Selwan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW455H274J0ZYJ6K4KHKJT25.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Jérôme Schneider](https://blog.cloudflare.com/ja-jp/author/jerome/)、[Nikita Lapkov](https://blog.cloudflare.com/ja-jp/author/nikita-lapkov/)、[Marc Selwan](https://blog.cloudflare.com/ja-jp/author/marc-selwan/)

13分で読了

URLをコピー

この記事は以下でも利用可能です [English](https://blog.cloudflare.com/r2-sql-aggregations/)、[한국어](https://blog.cloudflare.com/ko-kr/r2-sql-aggregations/)、[繁體中文](https://blog.cloudflare.com/zh-tw/r2-sql-aggregations/)、[简体中文](https://blog.cloudflare.com/zh-cn/r2-sql-aggregations/).

![BLOG-3082 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45417DV5EYZK6BB5T2Z60B.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/////f395OPwzs7ry9Dx2N745uj17urq////////5+bz0dLuztT02uH66Ov37+zs////////6+z31tny0tr43uf+6/D78vHw////////8PL83OH32OL94+7/8Pb/9/b1////////9vn/4un83+r/6fX/9fz/+/z6////////+///6PD/5fL/7/z/+f/////+/////////v//7PX/6ff/8////f//////////////////7ff/6/n/9P///v//////)

_このコンテンツは自動機械翻訳サービスによる翻訳版であり、皆さまの便宜のために提供しています。原本の英語版と異なる誤り、省略、解釈の微妙な違いが含まれる場合があります。ご不明な点がある場合は、英語版原本をご確認ください。_

大量のデータを扱うとき、簡単な概要を把握するのが役立ちます。これはまさにSQLで集約が提供するものです。「GROUP クエリ」と呼ばれる集約は全体像が示されるため、膨大な量のデータからインサイトを素早く得ることができます。

Cloudflareのサーバーレス分散型分析クエリエンジンである[ _R2 SQL_](https://blog.cloudflare.com/r2-sql-deep-dive/)での集約対応を発表できることを嬉しく思います。R2 SQLは、[ _R2データカタログ_](https://developers.cloudflare.com/r2/data-catalog/)に格納されたデータに対してSQLクエリを実行することができます。集約により、[ _R2 SQL_](https://developers.cloudflare.com/r2-sql/)のユーザーはデータの重要な傾向や変化を見極め、レポートを作成し、ログの異常を発見することができます。

このリリースは、すでにサポートされているフィルタクエリに基づいており、分析ワークロードの基盤となり、ユーザーが[ _Apache Parquet_](https://parquet.apache.org/)ファイルの干し草の山から針を見つけることができるようになります。

この記事では、集約の有用性と特異性を解き放ち、R2データカタログに保存された膨大な量のデータに対するクエリーの実行をサポートするために、どのようにR2SQLを拡張したかを掘り下げます。

## 分析における集約の重要性

集約（「クエリ別グループ」）で、元データの短い要約を生成します。

集約の一般的な使用例は、レポートの生成です。「売上」と呼ばれる表を想像してみてください。これには、ある企業のさまざまな国と部門の全売上の履歴データが含まれています。この集計クエリを使って、部門別の売上高に関するレポートを簡単に作成することができます。
    
    
    SELECT department, sum(value)
    FROM sales
    GROUP BY department

  
「GROUP BY」文を使用することで、テーブル行をバケットに分割することができます。各バケットには、特定の部署に対応するラベルが付いています。バケットが満杯になると、各バケットの全行の「合計（value）」を計算し、対応する部門で行われる売上の総量を求めることができます。

レポートによっては、量が最も多い部門だけに関心があるかもしれません。そこで登場するのが「ORDER BY」文です。
    
    
    SELECT department, sum(value)
    FROM sales
    GROUP BY department
    ORDER BY sum(value) DESC
    LIMIT 10

ここでは、すべての部門バケットを合計売上高で降順にソートし、上位10件のみを返すようにクエリーエンジンに指示しています。

最後に、異常をフィルタリングすることに関心があるかもしれません。たとえば、売上合計が5件を超える部門のみをレポートに含めたい場合があります。「HAVING」ステートメントを使うことで、簡単にそれを行うことができます。
    
    
    SELECT department, sum(value), count(*)
    FROM sales
    GROUP BY department
    HAVING count(*) > 5
    ORDER BY sum(value) DESC
    LIMIT 10

ここでは、クエリに新しい集計関数「count(*)」を追加しています。これは、各バケットの最終行数を計算するものです。これは、各部門の売上数に直接対応するため、「HAVING」ステートメントに予測条件を追加し、5行以上のバケットのみを残りするようにしました。

## 集約には2つのアプローチがあります：早い段階での計算

集計クエリには、どこにも保存されていない列を参照することができるという興味深い特性があります。「sum(value)」について考えてみましょう。このカラムは、R2に保存されたParquetファイルから取得される「部署」列とは異なり、クエリーエンジンによってその場で計算されます。この微妙な違いは、「sum」、「count」などの集計を参照するクエリは、2つのフェーズに分割する必要があることを意味します。

最初のフェーズは、新しい列を計算します。「ORDER BY」文を使って「count(*)」列でデータをソートしたり、「HAVING」文を使って行をフィルタリングする場合は、この列の値を知る必要があります。「count(*)」などの列の値が把握できたら、残りのクエリ実行に移ることができます。

クエリがHAVINGまたはORDER BY”で集約関数を参照せず、“SELECT”でそれらを使用している場合、騙すことができることに注意してください。集計関数の値は最後まで必要ないため、ユーザーに返す前に、それらを部分的に計算し、結果を統合することができます。

2つのアプローチの重要な違いは、集約関数を事前に、後で追加の計算を行う場合、その場で、ユーザーが必要とする結果を反復的に構築することもできるのです。

まず、その場で結果を構築していきます。これは「スキャッター集約」と呼ばれるテクニックです。そしてその上に、集計関数の上で「HAVING」や「ORDER BY」などの追加の計算を実行できる「シャッフル集約」を導入します。

## スキャッター集約

「HAVING」と「ORDER BY」を使用しない集約クエリは、フィルタクエリに似た方法で実行できます。フィルタクエリの場合、R2 SQLはクエリ実行のコーディネーターとなるノードを1つ選択します。このノードはクエリを分析し、R2データカタログを参照して、どのParquet行グループにクエリに関連するデータが含まれているかを把握します。Parquetの各行グループは、単一のコンピューティングノードが処理できる比較的小さな作業を表します。コーディネーターノードは多くのWorkerノードに作業を分散し、結果を収集してユーザーに返します。

集約されたクエリを実行するために、すべて同じ手順に従い、Workerノード間で小さな作業を分散します。しかし今回は、「WHERE」ステートメントの前提条件に基づいて行をフィルタリングするだけでなく、Workerノードは**事前集約** も計算します。

プリ集約は、集約の中間状態を表します。これは、データのサブセット上で部分的に計算された集計関数を表すデータの不完全な断片です。複数の事前集約を結合して、集約関数の最終値を計算することができます。集約関数を事前集約に分割することで、集約の計算を水平にスケールすることができ、Cloudflareのネットワークにある膨大な計算リソースを活用することができます。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3082 Image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45BPPXJKC47WPRR8TQZR5H.png&w=715&h=674&f=webp&fit=cover&position=center)

例えば、「count(*)」の事前集計は、データのサブセットの行数を表す数値です。最終的な「count(*)」の計算は、これらの数字を加算するのと同じくらい簡単です。「avg(値)」の事前集計は、「合計(値)」と「カウント(*)」の2つの数値で構成されています。「avg(value)」の値は、すべての「sum(value)」値を足し合わせ、すべての「count(*)」値を足し合わせ、最後に1つの数字を他の数字で割ることによって計算できます。

ワーカーノードは事前集計の計算を終えると、結果をコーディネーターノードにストリーミングします。コーディネーターノードは、すべての結果を収集し、事前集約から集計関数の最終値を計算し、結果をユーザーに返します。

## 寄せ集めの限界を超えたシャッフル

スキャッターギャンブルは、コーディネーターがWorkerから小さな部分的な状態をマージすることで最終結果を計算できる場合、非常に効率的です。`SELECT sum(sales) FROM orders`のようなクエリーを実行すると、コーディネーターは各workerから単一の数字を受け取り、それらを合計します。R2に存在するデータの量に関係なく、コーディネーターのメモリフットプリントは無視できます。

しかし、クエリが集計の _結果_ に基づいてソートやフィルタリングを必要とする場合、この方法は非効率になります。売上高の上位2つの部門を見つけるクエリーについて考えてみましょう。
    
    
    SELECT department, sum(sales)
    FROM sales
    GROUP BY department
    ORDER BY sum(sales) DESC
    LIMIT 2

グローバルトップ2を正しく判断するには、データセット全体の各部門の合計売上を知る必要があります。データは基盤となるParquetファイル全体にランダムに効果的に分散されるため、特定の部門の売上が多くの異なるWorkerに分割される可能性があります。同じ部署は、個々の労働者の売上が低い場合があり、ローカルトップ2リストから除外すれば、それらの労働者の合計売上がグローバルでは最高売上になります。

次の図は、このクエリに対して分散型収集アプローチが機能しないことを示しています。「Dept A」はグローバルなセールスリーダーですが、売上が従業員全体に均等に行き渡るため、ローカルのトップ2リストにランクインせず、コーディネーターから破棄されてしまいます。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3082 Image 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW463ZP69R3N5R25QG4E9T0V.png&w=715&h=674&f=webp&fit=cover&position=center)

したがって、クエリのグローバル集計による順序の結果がある場合、コーディネーターはWorkerからの事前フィルタリングされた結果に依存することはできません。分類する前に、 _全_ ワーカーから _各部門_ の合計カウントをリクエストして、グローバル合計を計算する必要があります。IPアドレスやユーザーIDのような高カーディナリティ列でグループ化している場合、コーディネーターは何百万行もの行を取り込んでマージしなければならないため、単一のノードでリソースのボトルネックが発生します。

これを解決するためには、最終的な集計が行われる前に、特定のグループのデータを同じ場所に配置する方法である**シャッフル** が必要になります。

### 集計データのシャッフル

そこで、ランダムなデータ分散の問題を解決するために、**シャッフルステージ** を導入しました。コーディネーターに結果を送信する代わりに、Workerは互いに直接データを交換し、グループ化キーに基づいて行を同じ場所に配置します。

このルーティングは、**決定論的なハッシュ分割** に依存しています。Workerが行を処理する際、`GROUP BY`列をハッシュし、宛先Workerを識別します。このハッシュは決定性があるため、クラスター内のすべてのworkerが個別に特定のデータの送信先に同意します。「Engineering」ハッシュがWorker 5に送信された場合、すべてのWorkerは「Engineering」行をWorker 5にルーティングすることを知っています。中央レジストリは不要です。

下図は、この流れを示したものです。「Dept A」がWorkers 1、2、3上で始まることに注目してください。ハッシュ関数は「Dept A」をWorker 1にマッピングするため、すべてのWorkerはそれらの行を同じ宛先にルーティングします。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3082 Image 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45ZD7B5A4ZRR0NG4HHEKV4.png&w=715&h=622&f=webp&fit=cover&position=center)

集計をシャッフルすると、正しい結果が得られます。しかし、この全面的な交換はタイミングの依存関係を生み出します。Worker 3がデータの送信を完了する前に、Worker 1が「Dept A」の最終合計を計算し始めた場合、結果は不完全になります。

これに対処するために、当社では厳格な**同期バリア** を適用しています。コーディネーターはクラスター全体の進行状況を追跡し、Workerは発信データをバッファリングし、[ _gRPC_](https://grpc.io/)ストリーム経由でピアにフラッシュします。すべてのWorkerが入力ファイルの処理が完了したことを確認してからシャッフルバッファを消去すると、コーディネーターは続行するコマンドを発行します。このバリアにより、次のステージが開始された時に、各Workerのデータセットが完全かつ正確であることを保証します。

### ローカルファイリング

同期バリアが取り去られると、すべてのworkerは割り当てられたグループの完全なデータセットを保持するようになります。Worker 1は「Dept A」の売上記録の100%を持ち、最終的な合計を確実に計算できるようになりました。

これにより、コーディネーターに負担をかけるのではなく、フィルタリングやソートのような計算ロジックをworkerにプッシュすることができます。例えば、クエリに`HAVING count(*) > 5`が含まれている場合、Workerは集約直後にこの基準を満たさないグループを除外できます。

この段階の終了時に、各Workerは所有するグループに対してソートされた最終的な結果のストリームを生成します。

### ストリーミングマージ

パズルの最後のピースは、コーディネーターです。分散型収集モデルでは、コーディネーターがデータセット全体の集計とソートという費用のかかるタスクを担当しました。シャッフルモデルでは、その役割は変わります。

Workerはすでに最終的な集計を計算し、ローカルでソートしているため、コーディネーターは**k-wayマージ** を実行するだけで済みます。すべてのWorkerにストリームを開き、結果を行ごとに読み込んでいきます。各workerからの現在の行を比較し、ソート順に基づいて「winner」を選択し、ユーザーに送信されるクエリ結果に追加します。

このアプローチは、特に`LIMIT`クエリに強力なアプローチとなります。ユーザーが上位10の部署を要求すると、コーディネーターは上位10の項目を見つけるまでストリームを統合し、その後すぐに処理を停止します。残りの数百万行をロードまたはマージする必要はなく、計算リソースを過剰に消費することなく、運用の規模を拡大できます。

## 膨大なデータセットを処理するための強力なエンジン

集約の追加により、[ _R2 SQL_](https://developers.cloudflare.com/r2-sql/?cf_target_id=84F4CFDF79EFE12291D34EF36907F300)は、データのフィルタリングに優れたツールから、膨大なデータセットのデータ処理が可能な強力なエンジンに変貌します。これは、スクレイピング、シャッフルなどの分散型実行戦略を実装することで実現します。Cloudflareのグローバルな計算能力とネットワークの規模を使って、データがある場所にコンピューティングをプッシュすることができるのです。

レポートの作成、大量のログの異常の監視、単にデータの傾向を見極めるなど、複雑なOLAPインフラストラクチャの管理やR2からのデータ移動にかかるオーバーヘッドなしに、そのすべてをCloudflareの開発者プラットフォーム内で簡単にできるようになりました。

## 今すぐお試しください！

R2 SQLの集約のサポートは、本日よりご利用いただけます。これらの新機能を、R2 Data Catalogのデータでどのように活用するか、楽しみにしています。

  * **開始する:** 集約クエリの実行に関する例と構文ガイドについては、[ _ドキュメント_](https://developers.cloudflare.com/r2-sql/sql-reference/)をご覧ください。
  * **会話に参加する：** 質問、フィードバック、または構築しているものを共有したい場合は、Cloudflare [_Developer Discord_](https://discord.com/invite/cloudflaredev)に参加してください。



このページ

オンラインで議論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fr2-sql-aggregations%2F&t=R2%20SQL%E3%81%A7%E3%81%AEGROUP%20BY%E3%80%81SUM%E3%80%81%E3%81%9D%E3%81%AE%E4%BB%96%E3%81%AE%E9%9B%86%E7%B4%84%E3%82%AF%E3%82%A8%E3%83%AA%E3%81%AE%E3%82%B5%E3%83%9D%E3%83%BC%E3%83%88%E3%82%92%E7%99%BA%E8%A1%A8)[](https://x.com/intent/post?text=R2+SQL%E3%81%A7%E3%81%AEGROUP+BY%E3%80%81SUM%E3%80%81%E3%81%9D%E3%81%AE%E4%BB%96%E3%81%AE%E9%9B%86%E7%B4%84%E3%82%AF%E3%82%A8%E3%83%AA%E3%81%AE%E3%82%B5%E3%83%9D%E3%83%BC%E3%83%88%E3%82%92%E7%99%BA%E8%A1%A8&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fr2-sql-aggregations%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fr2-sql-aggregations%2F)[](https://bsky.app/intent/compose?text=R2+SQL%E3%81%A7%E3%81%AEGROUP+BY%E3%80%81SUM%E3%80%81%E3%81%9D%E3%81%AE%E4%BB%96%E3%81%AE%E9%9B%86%E7%B4%84%E3%82%AF%E3%82%A8%E3%83%AA%E3%81%AE%E3%82%B5%E3%83%9D%E3%83%BC%E3%83%88%E3%82%92%E7%99%BA%E8%A1%A8+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fr2-sql-aggregations%2F)[](https://mastodonshare.com/?text=R2+SQL%E3%81%A7%E3%81%AEGROUP+BY%E3%80%81SUM%E3%80%81%E3%81%9D%E3%81%AE%E4%BB%96%E3%81%AE%E9%9B%86%E7%B4%84%E3%82%AF%E3%82%A8%E3%83%AA%E3%81%AE%E3%82%B5%E3%83%9D%E3%83%BC%E3%83%88%E3%82%92%E7%99%BA%E8%A1%A8&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fr2-sql-aggregations%2F)[](https://www.threads.net/intent/post?text=R2+SQL%E3%81%A7%E3%81%AEGROUP+BY%E3%80%81SUM%E3%80%81%E3%81%9D%E3%81%AE%E4%BB%96%E3%81%AE%E9%9B%86%E7%B4%84%E3%82%AF%E3%82%A8%E3%83%AA%E3%81%AE%E3%82%B5%E3%83%9D%E3%83%BC%E3%83%88%E3%82%92%E7%99%BA%E8%A1%A8+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fr2-sql-aggregations%2F)

## 関連するタグ

[R2](https://blog.cloudflare.com/ja-jp/tag/r2/)[Rust](https://blog.cloudflare.com/ja-jp/tag/rust/)[SQL](https://blog.cloudflare.com/ja-jp/tag/sql/)[エッジコンピューティング](https://blog.cloudflare.com/ja-jp/tag/edge-computing/)[サーバーレス](https://blog.cloudflare.com/ja-jp/tag/serverless/)[データ](https://blog.cloudflare.com/ja-jp/tag/data/)

SNS をフォロー

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 新しい投稿のお知らせを受け取るように登録する

メールアドレス

また、あなたのメールアドレスを共有したりすることはございません。

登録する

ご購読ありがとうございます！受信箱を確認して登録してください。
