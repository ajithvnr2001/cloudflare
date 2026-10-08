---
url: https://blog.cloudflare.com/ja-jp/dns-build-improvement/
title: DNS\u30ec\u30b3\u30fc\u30c9\u306e\u30d3\u30eb\u30c9\u901f\u5ea6\u30924,000\u500d\u4ee5\u4e0a\u5411\u4e0a\u3055\u305b\u305f\u65b9\u6cd5 | Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:47:15.652473+00:00
---

# DNSレコードのビルド速度を4,000倍以上向上させた方法 | Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/dns-build-improvement/

[ブログ](https://blog.cloudflare.com/ja-jp/)

[DNS](https://blog.cloudflare.com/ja-jp/tag/dns/)[Kafka](https://blog.cloudflare.com/ja-jp/tag/kafka/)[スピードと信頼性](https://blog.cloudflare.com/ja-jp/tag/speed-and-reliability/)1件1件タグを表示

4 タグタグを4件表示

  * 投稿タグ
  * [DNS](https://blog.cloudflare.com/ja-jp/tag/dns/)[Kafka](https://blog.cloudflare.com/ja-jp/tag/kafka/)[スピードと信頼性](https://blog.cloudflare.com/ja-jp/tag/speed-and-reliability/)[製品ニュース](https://blog.cloudflare.com/ja-jp/tag/product-news/)
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



[製品ニュース](https://blog.cloudflare.com/ja-jp/tag/product-news/)

[DNS](https://blog.cloudflare.com/ja-jp/tag/dns/)[Kafka](https://blog.cloudflare.com/ja-jp/tag/kafka/)[スピードと信頼性](https://blog.cloudflare.com/ja-jp/tag/speed-and-reliability/)[製品ニュース](https://blog.cloudflare.com/ja-jp/tag/product-news/)

2022年5月25日

# DNSレコードのビルド速度を4,000倍以上向上させた方法

![Alex Fattouche](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48H0J66VY9AP4Y8GXCS4RZ.png&w=64&h=64&f=webp&fit=cover&position=center)

[Alex Fattouche](https://blog.cloudflare.com/ja-jp/author/alex-fattouche/)

13分で読了

URLをコピー

この記事は以下でも利用可能です [English](https://blog.cloudflare.com/dns-build-improvement/)、[Español](https://blog.cloudflare.com/es-es/dns-build-improvement/)、[简体中文](https://blog.cloudflare.com/zh-cn/dns-build-improvement/).

![How we improved DNS record build speed by more than 4,000x](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW460DFB62WWX8FM8D2AWF1Y.png&w=1800&h=1013&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/vzn+Pfj7u3Z6efU7enY8ezc7+va5ubT//zo+vbj7+vX6eLQ7eLS8ubW8OfX5+TS//3p/ffj8enX697N7tzM9OHR8uTU6uTT///s//rm9evY797N8tzL9+HR9ubV7+fW///w///q+/Dd9OXS+OPS/OnX++3b9O3b///1///v//ji++7a/u7c//Ti//bj+PTg///5///z//7n//fh//jk//3r//3q/Pnk///6///0///p//rj//zo///u///t/fzm)

以前、私がセカンダリDNSについての[ブログ](https://blog.cloudflare.com/secondary-dns-deep-dive/)を書いて以来、CloudflareのDNSトラフィックは、月間15.8兆DNSクエリーから38.7兆へと倍以上に増加しています。当社のネットワークは現在、100カ国以上270都市以上に広がり、世界中で10,000万以上のネットワークと相互接続しています。[w3 stats](https://w3techs.com/technologies/overview/dns_server)によると、「Cloudflareは全Webサイトの15.3%にDNSサーバープロバイダーとして利用されている」とのことです。これは、可能な限り最速かつ最も信頼性の高い方法でDNSを提供するために、当社が大きな責任を担っていることを意味しています。

DNSクエリーの応答時間は最も重要なパフォーマンス指標ですが、時として注目されない別の指標があります。DNSレコードの伝達時間は、当社のAPIに送信された変更が当社のDNSクエリーの応答に反映されるまでの時間です。DNSレコードの伝達時間は、お客様が素早く設定を変更し、システムをより俊敏にするために、1ミリ秒単位で重要視されます。当社のDNS伝達パイプラインはすでに非常に高速であることが知られていましたが、実装すればパフォーマンスを大幅に改善できるいくつかの改善点を特定しました。このブログでは、DNSレコードの伝達速度を劇的に改善した方法と、それがお客様に与える影響について説明します。

### DNSレコードの伝達方法

Cloudflareは、お客様のDNSレコードの変更を多段階のパイプラインで受け取り、当社のグローバルネットワークにプッシュするため、世界中で利用することができます。

上図に示す手順：

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1054 Embedded Image - oLXFYa](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47VWX98TP9Q9DM92JXC7AA.png&w=715&h=157&f=webp&fit=cover&position=center)

  1. お客様がDNS Records API(またはUI)を使ってレコードを変更します。
  2. 変更内容はデータベースに永続化されます。
  3. データベースイベントは、Zone Builderによって消費されるKafkaメッセージをトリガーします。
  4. Zone Builderはメッセージを受け取り、データベースからゾーンの内容を収集し、分散KVストアであるQuicksilverにプッシュします。
  5. そして、Quicksilverはこの情報をネットワークに伝達させます。



もちろん、これは起きていることを簡略化したものです。実際には、当社のAPIは1秒間に何千ものリクエストを受け取っています。すべてのPOST/PUT/PATCH/DELETEリクエストは、最終的にDNSレコードの変更につながります。APIやCloudflareダッシュボードに表示される情報が、DNSクエリーに応答するために使用する情報と最終的に一致するように、これらの各変更を処理する必要があります。

これまで、DNSの伝達パイプラインにおける最大のボトルネックの1つは、上記の手順4で示したZone Builderでした。グローバルネットワークに書き込まれるレコードの収集と整理を担うZone Builderは、特に大きなゾーンの伝達時間の大半を占めていました。スケールを拡大していく上で、システムに存在する可能性のあるボトルネックを取り除くことは重要であり、これはそのようなボトルネックの1つとして明確に認識されていました。

### 産みの苦しみ

上記のパイプラインが[最初に発表された](https://blog.cloudflare.com/how-we-made-our-dns-stack-3x-faster/)とき、Zone Builderは1秒間におよそ5から10件のDNSレコードの変更を受け取っていました。当時のZone Builderは以前のシステムより大幅に改善されましたが、Cloudflareが経験していた成長および今なお経験している成長を考えると、長く続くことはありませんでした。現在では、1秒間に平均250件のDNSレコードが変更されており、これはZone Builderが最初に発表されたときの25倍という驚異的な伸びを示しています。

Zone Builderが最初に設計された方法は、非常にシンプルなものでした。ゾーンが変更されると、Zone Builderはそのゾーンのデータベースからすべてのレコードを取得し、Quicksilverに保存されているレコードと比較します。違いがあれば修正し、データベースとQuicksilverの間の一貫性を維持します。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1054 Embedded Image - IRU8w6](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW498JGZR23TEGT8WNM87YS0.png&w=715&h=305&f=webp&fit=cover&position=center)

これは、フルビルドとして知られています。フルビルドは、各DNSレコードの変更が1つのゾーン変更イベントに対応するため、非常に効果的です。これは、複数のイベントをバッチ処理し、その後必要に応じてドロップできることを意味します。例えば、ユーザーが自分のゾーンに10回変更を加えた場合、これは10個のイベントになります。Zone Builderはとにかくゾーンの全レコードを取得するので、ゾーンを10回ビルドする必要はありません。最終的な変更が送信された後に、1回ビルドすれば良いだけなのです。

ゾーンに100万レコードや1,000万レコードが含まれる場合はどうなるのでしょうか？これは非常に現実的な問題です。Cloudflareがスケーリングしているだけでなく、我々の顧客も一緒にスケーリングしているからです。今日、当社最大のゾーンは現在数百万レコードを有しています。当社のデータベースはパフォーマンスのために最適化されていますが、100万レコードを含むフルビルドでさえ、最大で**35秒** を要し、これは主にデータベースクエリーの遅延によるものです。さらに、Zone Builderがゾーンの内容をQuicksilverに保存されているレコードと比較する際に、Quicksilverからゾーンのすべてのレコードを取得する必要があり、時間がかかってしまいます。しかし、その影響は一人の顧客だけにとどまりません。データベースから読み込む他のサービスのリソースも消費し、Zone Builderが他のゾーンをビルドする速度も遅くなってしまうのです。

### レコード単位のビルド：新しいビルドタイプ

この問題のソリューションは、すでに頭の中にある方も多いのではないでしょうか。

 _なぜ、Zone Builderは、変更されたレコードをデータベースにクエリ―し、単一のレコードだけを伝達させないのでしょう_

もちろん、これが正しいソリューションであり、最終的に行き着いた先でもあります。しかし、そこに至るまでの道のりは、見かけほど単純なものではありませんでした。

まず、当社のデータベースは、ゾーンタッチ時にPostgreSQL Queue(PGQ)イベントを作成し、最終的にKafkaイベントに変換する一連の関数を使用しています。当初、当社は個々のレコードイベントを区別していなかったため、Zone Builderはデータベースにクエリ―するまで、実際に何が変更されたのかが分かりませんでした。

次に、Zone Builderはレコードに加えて、依然としてDNSゾーンの設定を担います。DNSゾーン設定の例としては、カスタムネームサーバーコントロールやDNSSECコントロールなどがあります。そのため、当社のZone Builderは、特定のビルドタイプを意識して、互いに踏み込まないようにする必要がありました。さらに、レコード単位のビルドは、各イベントを個別に処理する必要があるため、ゾーンのビルドと同じようにバッチ処理することができません。

その結果、全く新しいスケジューリングシステムを書く必要がありました。最後に、異なるスケジューラの種類に対応するため、Quicksilverのインタラクションを書き直す必要がありました。これらの問題は、以下に内訳できます：

  1. 変更されたレコードの情報を含む、レコード変更用の新しいKafkaイベントパイプラインを作成する。
  2. Zone Builderを、ある定義されたスケジューラインタフェースを実装する新しいタイプのスケジューラに分離する。
  3. イベントを正しい順序で1つずつ読み込むために、レコード単位のスケジューラを実装する。
  4. レコード単位のスケジューラのための新しいQuicksilverインターフェイスを実装する。



以下は、新しいスケジューラタイプを持つ新しいZone Builderの内部を表したハイレベルな図です。

この2つのスケジューラ間でロックをかけることは非常に重要です。そうしないと、フルビルドスケジューラがレコード単位のスケジューラの変更を古いデータで上書きしてしまう可能性があるからです。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1054 Embedded Image - auTPl2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW450GBKBGMQ33BVMSQYESNP.png&w=715&h=917&f=webp&fit=cover&position=center)

このレコード単位のアーキテクチャは、DNSSECによる否定的回答に対するCloudflareの[ブラック・ライ・アプローチ](https://blog.cloudflare.com/black-lies/)を使用しなければ、何も実現できないことに注意することが重要です。通常、DNSSECによる否定的回答を適切に提供するためには、ゾーン内のすべてのレコードが正規にソートされていなければなりません。これはApexレコードからゾーン内の全レコードへの参照リストを維持するために必要です。否定的回答に対するこの通常のアプローチでは、ゾーンに追加された単一のレコードは、このソートされた名前のリスト内での挿入ポイントを決定するために全てのレコードを収集する必要があります。

### バグ

すべてが順調に進んだCloudflareブログを書ければいいのですが、決してそうはいきません。バグは起こるものですから、それに対応し、次回はこの特定のバグが起こらないように自分自身をセットアップする準備が必要です。

今回発見された大きなバグは、Quicksilverの古いレコードのクリーンアップに関連するものでした。Zone Builderをフル活用すれば、データベースとQuicksilverの両方に存在するレコードを正確に把握できる贅沢があります。このため、書き込みとクリーンアップがかなり簡単な作業になります。

レコード単位のビルドが導入されたとき、作成、更新、削除などのレコードイベントはすべて異なる方法で処理される必要がありました。作成と削除は、Quicksilverからレコードを追加するか削除するかのどちらかであるため、非常に単純です。更新は、PGQがKafkaイベントを生成する方法によって、予期せぬ問題を引き起こしました。レコードの更新には新しいレコードの情報しか含まれていないため、レコード名が変更されたときに、古いレコードをクリーンアップするためにQuicksilverで何をクエリーすればよいかを知る術がありませんでした。つまり、お客様がDNS Records APIでレコードの名前を変更しても、古いレコードは削除されないということでした。最終的には、これらの特定の更新イベントを作成と削除の両方のイベントに置き換えることで、この問題は解決され、Zone Builderは古いレコードをクリーンアップするために必要な情報を得ることができました。

どれもロケット手術のようなものではありませんが、当社はCloudflareのスケーリングに合わせて成長するよう、エンジニアリングの労力を費やしてソフトウェアを継続的に改良しています。そして、何百万ものドメインが当社に頼っているときに、Cloudflareのこのような基本的な低レベルの部分を変更することは困難なことなのです。

### 結果

今日、すべてのDNS Records APIのレコード変更は、Zone Builderによってレコード単位のビルドとして扱われます。以前述べたように、フルビルドを完全に取り除くことはできていませんが、現在ではDNSビルド全体の約13%を占めています。この13%は、ゾーン全体の内容を知る必要があるDNS設定に加えられた変更に相当します。

以下のように2つのビルドタイプを比較すると、レコード単位のビルドはフルビルドよりも平均して**150倍** 速いことがわかります。以下のビルド時間には、データベースクエリー時間とQuicksilverの書き込み時間の両方が含まれています。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1054 Embedded Image - CzlOa2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44SX52V7RC2BBVBM84DZWJ.png&w=715&h=352&f=webp&fit=cover&position=center)

そこからQuicksilverを通じて、当社のレコードがグローバルネットワークに伝達されるのです。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1054 Embedded Image - NKwjND](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46GWVRGJXV92HYE1JRX330.png&w=715&h=441&f=webp&fit=cover&position=center)

上記の150倍は平均値に対する改善ですが、冒頭で述べた4000倍はどうでしょうか。ご想像の通り、ゾーンのサイズが大きくなればなるほど、フルビルド時間とレコード単位のビルド時間の差も大きくなります。100万レコードのテストゾーンを使用してレコード単位のビルドを何度か行い、その後フルビルドを何度か行いました。その結果を以下の表に示します。

ビルドタイプ

ビルド時間 (ms)

レコード単位#1

6

レコード単位#2

7

レコード単位#3

6

レコード単位#4

8

レコード単位#5

6

フル#1

34032

フル#2

33953

フル#3

34271

フル#4

34121

フル#5

34093

レコード単位のビルドを5回行った場合、ビルド時間は8ミリ秒以下であることが分かります。しかし、フルビルドを実行した場合、ビルド時間は平均34秒でした。これは、**4250倍** のビルド時間の短縮になります！

平均的なサイズのゾーンと大規模なゾーンの両方のビルド時間を考えると、Cloudflareのすべてのお客様がこのパフォーマンス向上の恩恵を受けていることは明らかであり、恩恵はゾーンのサイズが大きくなる場合にのみ向上します。さらに、Zone BuilderはデータベースとQuicksilverのリソースをあまり使用しないので、他のCloudflareシステムは、向上した処理能力での稼働が可能となるのです。

### 次のステップ

この結果は非常にインパクトのあるものでしたが、当社はさらに良い結果を出すことができると考えています。将来的には、フルビルドを完全に排除し、ゾーン設定のビルドに置き換えることを計画しています。すべてのレコードに加えてゾーン設定を取得する代わりに、ゾーン設定ビルダーはゾーンの設定を取得し、それをQuicksilver経由でグローバルネットワークに伝達させるだけでよいのです。レコード単位のビルドと同様に、ゾーン設定の複雑さとそれに触れるアクターの数のために、これは困難な課題です。最終的にこれが実現できれば、フルビルドを正式に引き上げて、当社が長年にわたって成長させてきたスケールのgitの履歴にリマインダーとしてそれを残すことができます。

また、レコードの変更をグループにまとめて、データベースやQuicksilverに問い合わせる回数を最小限にするバッチシステムを導入する予定です。

このような技術的・運用的な課題を解決することにワクワクするでしょうか？Cloudflareは[エンジニアリング](https://www.cloudflare.com/ja-jp/careers/jobs/?department=Engineering&location=default)や[他のチーム](https://www.cloudflare.com/ja-jp/careers/)において常に才能あるスペシャリストやゼネラリストを採用しています。

このページ

オンラインで議論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fdns-build-improvement%2F&t=DNS%E3%83%AC%E3%82%B3%E3%83%BC%E3%83%89%E3%81%AE%E3%83%93%E3%83%AB%E3%83%89%E9%80%9F%E5%BA%A6%E3%82%924%2C000%E5%80%8D%E4%BB%A5%E4%B8%8A%E5%90%91%E4%B8%8A%E3%81%95%E3%81%9B%E3%81%9F%E6%96%B9%E6%B3%95)[](https://x.com/intent/post?text=DNS%E3%83%AC%E3%82%B3%E3%83%BC%E3%83%89%E3%81%AE%E3%83%93%E3%83%AB%E3%83%89%E9%80%9F%E5%BA%A6%E3%82%924%2C000%E5%80%8D%E4%BB%A5%E4%B8%8A%E5%90%91%E4%B8%8A%E3%81%95%E3%81%9B%E3%81%9F%E6%96%B9%E6%B3%95&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fdns-build-improvement%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fdns-build-improvement%2F)[](https://bsky.app/intent/compose?text=DNS%E3%83%AC%E3%82%B3%E3%83%BC%E3%83%89%E3%81%AE%E3%83%93%E3%83%AB%E3%83%89%E9%80%9F%E5%BA%A6%E3%82%924%2C000%E5%80%8D%E4%BB%A5%E4%B8%8A%E5%90%91%E4%B8%8A%E3%81%95%E3%81%9B%E3%81%9F%E6%96%B9%E6%B3%95+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fdns-build-improvement%2F)[](https://mastodonshare.com/?text=DNS%E3%83%AC%E3%82%B3%E3%83%BC%E3%83%89%E3%81%AE%E3%83%93%E3%83%AB%E3%83%89%E9%80%9F%E5%BA%A6%E3%82%924%2C000%E5%80%8D%E4%BB%A5%E4%B8%8A%E5%90%91%E4%B8%8A%E3%81%95%E3%81%9B%E3%81%9F%E6%96%B9%E6%B3%95&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fdns-build-improvement%2F)[](https://www.threads.net/intent/post?text=DNS%E3%83%AC%E3%82%B3%E3%83%BC%E3%83%89%E3%81%AE%E3%83%93%E3%83%AB%E3%83%89%E9%80%9F%E5%BA%A6%E3%82%924%2C000%E5%80%8D%E4%BB%A5%E4%B8%8A%E5%90%91%E4%B8%8A%E3%81%95%E3%81%9B%E3%81%9F%E6%96%B9%E6%B3%95+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fdns-build-improvement%2F)

## 関連するタグ

[DNS](https://blog.cloudflare.com/ja-jp/tag/dns/)[Kafka](https://blog.cloudflare.com/ja-jp/tag/kafka/)[スピードと信頼性](https://blog.cloudflare.com/ja-jp/tag/speed-and-reliability/)[製品ニュース](https://blog.cloudflare.com/ja-jp/tag/product-news/)

SNS をフォロー

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 新しい投稿のお知らせを受け取るように登録する

メールアドレス

また、あなたのメールアドレスを共有したりすることはございません。

登録する

ご購読ありがとうございます！受信箱を確認して登録してください。
