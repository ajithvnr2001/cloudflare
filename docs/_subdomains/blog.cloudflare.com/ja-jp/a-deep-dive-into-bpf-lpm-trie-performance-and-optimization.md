---
url: https://blog.cloudflare.com/ja-jp/a-deep-dive-into-bpf-lpm-trie-performance-and-optimization/
title: BPF LPM\u306e\u30d1\u30d5\u30a9\u30fc\u30de\u30f3\u30b9\u3068\u6700\u9069\u5316\u3092\u6df1\u6398\u308a | Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:51:42.509279+00:00
---

# BPF LPMのパフォーマンスと最適化を深掘り | Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/a-deep-dive-into-bpf-lpm-trie-performance-and-optimization/

[ブログ](https://blog.cloudflare.com/ja-jp/)

[eBPF](https://blog.cloudflare.com/ja-jp/tag/ebpf/)[IPv4](https://blog.cloudflare.com/ja-jp/tag/ipv4/)[IPv6](https://blog.cloudflare.com/ja-jp/tag/ipv6/)3件3件タグを表示

6 タグタグを6件表示

  * 投稿タグ
  * [eBPF](https://blog.cloudflare.com/ja-jp/tag/ebpf/)[IPv4](https://blog.cloudflare.com/ja-jp/tag/ipv4/)[IPv6](https://blog.cloudflare.com/ja-jp/tag/ipv6/)[Linux](https://blog.cloudflare.com/ja-jp/tag/linux/)[パフォーマンス](https://blog.cloudflare.com/ja-jp/tag/performance/)[詳細情報](https://blog.cloudflare.com/ja-jp/tag/deep-dive/)
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



[Linux](https://blog.cloudflare.com/ja-jp/tag/linux/)[パフォーマンス](https://blog.cloudflare.com/ja-jp/tag/performance/)[詳細情報](https://blog.cloudflare.com/ja-jp/tag/deep-dive/)

[eBPF](https://blog.cloudflare.com/ja-jp/tag/ebpf/)[IPv4](https://blog.cloudflare.com/ja-jp/tag/ipv4/)[IPv6](https://blog.cloudflare.com/ja-jp/tag/ipv6/)[Linux](https://blog.cloudflare.com/ja-jp/tag/linux/)[パフォーマンス](https://blog.cloudflare.com/ja-jp/tag/performance/)[詳細情報](https://blog.cloudflare.com/ja-jp/tag/deep-dive/)

2025年10月21日

# BPF LPMのパフォーマンスと最適化を深掘り

![Matt Fleming](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW469GS9NZP4VYY003HA8XEA.webp&w=64&h=64&f=webp&fit=cover&position=center)![Jesper Brouer](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW499RS2WW80VBYFGEW0TADD.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Matt Fleming](https://blog.cloudflare.com/ja-jp/author/matt-fleming/)、[Jesper Brouer](https://blog.cloudflare.com/ja-jp/author/jesper-brouer/)

12分で読了

URLをコピー

この記事は以下でも利用可能です [English](https://blog.cloudflare.com/a-deep-dive-into-bpf-lpm-trie-performance-and-optimization/).

![BLOG-2984 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW452X656JCQSKB3SYSHDSJ7.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////+vv+2uDswsvixdDp2eLz5+v06err/////v//4eTvydDly9Tq3eT06u317e3u////////6erz09fp1Nnu4+f27/H48vLx////////8fL43ODv3OHy6u369fb8+Pf2////////+fr+5er14+r47/T/+vv//vz6/////////v//6/L76fL+8/r//f/////+////////////7/j/7Pf/9v//////////////////////8Pr/7fn/9///////////)

_このコンテンツは自動機械翻訳サービスによる翻訳版であり、皆さまの便宜のために提供しています。原本の英語版と異なる誤り、省略、解釈の微妙な違いが含まれる場合があります。ご不明な点がある場合は、英語版原本をご確認ください。_

それは、本番環境の不可解なソフトロックアップメッセージから始まりました。当社が使用している最も基本的なデータ構造の1つであるBPF LPMトリ

BPFトライマップ（[BPF_MAP_TYPE_LPM_TRIE](https://docs.ebpf.io/linux/map-type/BPF_MAP_TYPE_LPM_TRIE/)）は、ネットワークパケットをルーティングする際のIPおよびIP+ポートのマッチングなどのために多用され、リクエストが結果を返す前に適切なサービスを通過するようにします。このデータ構造のパフォーマンスはお客様にサービスを提供するために重要ですが、現在の実装のスピードは多くの不満を残しています。BPF LPMトライマップに数百万のエントリーを保存する際、エントリーの検索時間が数百ミリ秒かかったり、マップが10秒以上にわたってCPUをロックアップするなど、いくつかのボトルネックに遭遇しました。たとえば、BPFマップは、Cloudflareの[ _Magic Firewall_](https://www.cloudflare.com/network-services/products/magic-firewall/)ルールを評価する際に使用されますが、これらのボトルネックが、一部のお客様ではトラフィックパケット損失につながっています。

この記事では、試行とプレフィックスの一致の仕組み、ベンチマークの結果、そして現在のBPF LPMトライの実装の欠点のリストについて再確認します。

## 試行の簡単な要約

最後にトライデータ構造を見てからしばらく経った場合（あるいは、これまでご覧になったことがない場合）、トライはツリーデータ構造（バイナリツリーと同様）で、データを保存し、検索することができます。指定されたキーを処理し、各ノードがいくつかのキービットを保存します。

検索はパスを横断することによって実行されます。つまり、ノードはトラバーサルパスからキーを再構築するため、ノードはフルキーを保存する必要がありません。この点は、左子ノードが現在のノードより小さいキーを持ち、右子ノードがより大きいキーを持つという一次不変量が存在する従来のバイナリ検索ツリー（BST）とは異なります。BSTでは、検索ステップごとに比較ができるように、各ノードが完全なキーを保存する必要があります。

以下は、BSTがキーの値をどのように保存するかを示す例です。

  * ABC
  * ABCD
  * ABCDEFGH
  * DEF



![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2984 image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44WZ3AXEGWMVBH06YMF9EF.png&w=715&h=605&f=webp&fit=cover&position=center)

ちなみに、同じキーのセットを保存しようとすると、これは次のようになります。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2984 image 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW461ZJ1JK8NHFBQ430PDQ98.png&w=715&h=700&f=webp&fit=cover&position=center)

このようにビットを分割する方法は、データに冗長性がある場合、たとえば、共有データに必要なノードのセットは1つだけであるため、キーには一般的なものがあります。このため、文字列を効率的に格納するために、試行がよく使用されます。例：単語の辞書。文字列「ABC」と「ABCD」の格納には、3バイト＋4バイト（ASCIIを仮定）の必要はなく、3バイト＋1バイトで済みます。これは、「ABC」が両者（正確なビット数）で共有されるためです。実装によって異なる）。

また、試行することで、より効率的な検索が可能になります。たとえば、キー「CAR」がBSTに存在したかどうかを知りたい場合、ルートの正しい子（キー「DEF」を持つノード）に移動し、その左子をチェックする必要があります。存在すれば、なおさらです。トライはプレフィックス順に検索するため、より効率的です。この例では、トライはそのキーがトライにあるかどうかをルートで知ることができます。

この設計は、最も長いプレフィックスの一致を実行したり、CIDRを使用したIPルーティングで作業するのに最適です。CIDRは、IPアドレス空間をより効率的に使用するために導入されました（クラスを8ビットの4バケットに分類する必要がなくなりました）が、IPアドレスのネットワーク部分がどこにでも位置づけられる可能性があるため、複雑さが増しています。IPルーティングテーブルでCIDRスキームを処理するには、完全一致の検索を実行するのではなく、テーブル内の最も長い（最も具体的な）プレフィックスのマッチングが必要です。

トライを検索する際に各ノードでシングルビットの比較を行う場合、それはバイナリトライです。検索でより多くのビットを比較する場合、これを** _マルチビットトライ_** と呼びます。IPやサブネットアドレスなど、何でもわかります。すべて、0と1だけになります。

マルチビットトライアルのノードは、バイナリトライのノードよりも多くのメモリを使用しますが、コンピューターはいずれにせよマルチビットワードで動作するため、マイクロアーキテクチャの観点からは、マルチビットトライを使用した方がビットをより速く横断することができ、比較する回数を減らすことができるため、より効率的です検索に使用できますこれは古典的なスペースと時間のトレードオフです。

ほかにも、試行で使用できる最適化があります。トリガーに保存するデータの分布は一様ではなく、人口がまばらな地域である可能性があります。例えば、文字列「A」と「BCDEFGHI」をマルチビットトライアルに格納した場合、ノードの数が想定されていますか？ASCIIを使用している場合、ルートノードと左にある「A」または右にある「B」の分岐でバイナリトライを構築することができます。8ビットノードの場合、「C」、「D」、「E」、「F」、「G」、「H」、「I」を格納するには、さらに7つのノードが必要です。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2984 image 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4984Q0AHYKNJH51MYM4SXQ.png&w=715&h=1196&f=webp&fit=cover&position=center)

トライアルには他の文字列がないので、これはかなり最適とは言えません。「B」で一致した後最初のレベルに到達すると、そのプレフィックスを持つトライ新しい文字列が1つだけであることがわかり、** _パス圧縮_** を使用することで、他のすべてのノードを作成することなく回避できます。パス圧縮は、ノード「C」、「D」、「E」などを「I」のような単一のノードに置き換えます。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2984 image 4](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44BB97B9GVC123EYHZSPFK.png&w=715&h=887&f=webp&fit=cover&position=center)

ツリーを横断して「I」をヒットした場合でも、検索キーをスキップしたビットと比較して、検索キーが文字列と一致することを確認する必要があります。スキップされたビットをどこにどのように格納するかは実装によって異なります。BPF LPMは、単純にキー全体をリークノードに格納しようとします。データの密度が増すにつれて、パス圧縮の効果が低下します。

データ分布が密度で、たとえば、トライアルの最初の3レベルがすべて完全に入力されている場合はどうなるでしょうか。その場合は、** _レベル圧縮_** を使用して、そのレベルのすべてのノードを2**3個の子を持つ単一ノードに置き換えることができます。これは、Linuxカーネルで[IPルートルックアップ](https://vincent.bernat.ch/en/blog/2017-ipv4-route-lookup-linux)に使用されるLevel-Compressed Triesの動作の仕組みです（[ _net/ipv4/fib_trie.c_](https://elixir.bootlin.com/linux/v6.12.43/source/net/ipv4/fib_trie.c)を参照）。

他の最適化もありますが、この記事ではこの簡単な迂回は、カーネルのBPF LPMトライ実装は先ほど説明した3つの方法を十分に使用していないため、この記事では十分です。

## BPF LPMのトライアルマップの速さは？

ここでは、AMD EPYC 9684X 96-Coreマシンで[ _BPFセルフテストベンチマーク_](https://lore.kernel.org/bpf/20250827140149.1001557-1-matt@readmodwrite.com/)を実行したときの数字をいくつか紹介します。ここでは、トライは10,000のエントリー、32ビットのプレフィックス長、範囲[0, 10,000]内のすべてのキーのエントリーがあります。

業務| スループット| Stddev| 遅延  
---|---|---|---  
ルックアップ| 742.3万ops/秒| 0.02.3百万ps/秒| 134.710 ns/op  
更新| 264.3万ops/秒| 0.01.5万ops/秒| 378.310 ns/op  
削除| 071.2万ops/秒| 0.008万ops/秒| 1405.152 ns/op  
free| 0.57.3万ops/s| 0.574,000 pps/s| 1.743 ms/op  
  
1万件のエントリーがあるBPF LPMトライアルを解放するまでの時間が非常に大きいです。最近、これに時間がかかりすぎ、[ _ソフトロックアップメッセージ_](https://lore.kernel.org/lkml/20250616095532.47020-1-matt@readmodwrite.com/)が本番環境で大量に発生する問題が発生しました。

このベンチマークから、最悪の場合の動作がある程度想定できます。キーは非常に密接に使用されているため、パス圧縮はまったく効果がありません。次のセクションでは、関連するボトルネックを理解するために、ルックアップ操作について説明します。

## BPF LPM試行が遅い理由は？

[ _kernel/bpf/lpm_trie.c_](https://elixir.bootlin.com/linux/v6.12.43/source/kernel/bpf/lpm_trie.c) の LPM トライの実装には、冒頭で説明した最適化が2つあります。エッジノードでマルチビットの比較が可能ですが、各内部ノードには子ポインタが2つしかないため、ツリーが1ビットしか異なる多くのデータが密に挿入されている場合、これらのマルチビット比較は1ビットの比較にまで劣化します。

ここで例を紹介します。0、1、3の数字をBPF LPMトライに格納するとします。これらの値は32ビットまたは64ビットの機械語に収まるため、単一の比較で、トライの中の次のノードを決めることができると思うかもしれません。しかし、これは、trie実装に3つの子ポインタが現在のノードに3つの子ポインタがある場合にのみ可能です（これは当然のことながら、ほとんどのtrie実装で行われています）。言い換えると、3方向の分岐を決定したいのに、BPF LPMには2つの子しか与えないため、2方向の分岐に限定されます。

この2-サブネットの図を以下に示します。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2984 image 5](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44PK8NSZQ1RFJT8G6YDPVQ.png&w=715&h=605&f=webp&fit=cover&position=center)

リークノードは緑で表示され、キーはバイナリ文字列として中央に表示されます。8ビットの比較だけでも、どのノードがそのキーを持つかを知ることはできますが、BPF LPMの実装では、中間ノード（青）を挿入して、パストラバーサルに2通りのブランチの決定を挿入します。オレンジ色のルートノードには2つの子しかいません。リークノードに到達すると、BPF LPMはマルチビット比較を実行して鍵をチェックします。ノードがより多くの子をサポートする場合、上記のトライはこのように見え、3ウェイ分岐を許可し、検索時間を短縮します。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2984 image 6](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44AB3DHS16V20WFQH3SFKW.png&w=715&h=453&f=webp&fit=cover&position=center)

この2取得が3つの高さに影響を与えます。最悪の場合、完全なトライは基本的に高さlog2(nr_entries)を持つバイナリ検索ツリーになり、トライの高さはキーを検索するために必要な比較の回数に影響します。

上記の例は、BPF LPMがどのようにパス圧縮を実装しようとするかを示しています。キーが1ビットだけ異なる2つのノードがある中間ノードを挿入するだけです。3の代わりに15のキー（0b1111）を挿入した場合でも、トライのレイアウトは変わりません。ルートの正しい子に単一のノードが必要なだけです。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2984 image 7](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45EW3P996EBB4QXJA5C6ER.png&w=715&h=605&f=webp&fit=cover&position=center)

そして最後に、BPF LPMはレベル圧縮を実装しません。これも、3型のノードが子を2人しか保有できないという事実に起因しています。IPルートテーブルは、共通のプレフィックスを多く持つ傾向があり、通常、上位レベルで密に詰め込まれた試行が見られるため、IPルートを含むトライのレベル圧縮は非常に効果的です。

下記は、LPMのルックアップスループット（百万ops/秒で測定）が、エントリー数の増加（1エントリーから最大10万エントリーまで測定）に伴って低下することを示したグラフです。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2984 image 9](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45R613DN57QZYHDKGNQ7YA.png&w=715&h=443&f=webp&fit=cover&position=center)

エントリが100万に達すると、スループットは約150万op/秒で、エントリ数が増えるにつれて減少し続けます。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2984 image 8](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46PPKDMBF8M97TCB169HSA.png&w=715&h=443&f=webp&fit=cover&position=center)

なぜでしょうか？当初、これはL1のDCキャッシュのミス率のためです。トライアルで通過する必要のあるノードはすべて、キャッシュミスの可能性があります。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2984 image 10](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47AWD24R50E30HCEXJTXGT.png&w=715&h=443&f=webp&fit=cover&position=center)

グラフからわかるように、L1のDCキャッシュミス率は比較的安定しており、それでも、スループットは減少し続けています。8万前後になると、dTLBのミス率がボトルネックになります。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2984 image 11](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46MWTGZTHEK5TA21GBD0X4.png&w=715&h=443&f=webp&fit=cover&position=center)

BPF LPMはカーネルメモリのフリーリストから個々のノードを動的に割り当てようとするため、これらのノードは任意のアドレスに存在する可能性があります。つまり、トライアルを通過すると、ほぼ確実にキャッシュミスが発生し、dTLBミスが発生する可能性があります。エントリーの数とトライの高さが増加するにつれ、この状況はさらに悪化します。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2984 image 12](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47ZVHCQ171FG99NH9HDZA8.png&w=715&h=443&f=webp&fit=cover&position=center)

## ここからの発展

BPF LPMトライの現在の限界を理解することで、インターネットの将来に向けて、よりパフォーマンスと効率的なソリューションの構築に取り組むことができます。

私たちはすでにこれらのベンチマークをアップストリームのLinuxカーネルに貢献していますが、それは始まりに過ぎません。BPM LPM試行のパフォーマンス、特にワークロードによく使用されるルックアップ関数のパフォーマンスを改善する計画があります。この記事では、すでに[ _net/ipv4/fib_trie.c_](https://elixir.bootlin.com/linux/v6.12.43/source/net/ipv4/fib_trie.c)で使用されている多くの最適化を取り上げています。自然な最初のステップは、一般的なLevel Compressed tryの実装が利用できるように、そのコードをリファクタリングすることです。今後のブログ記事で、本研究を深く掘り下げてみましょう。

より多くのパフォーマンス数値をご覧になりたい方は、[Jesper Brouer](https://wiki.cfdata.org/display/~jesper)がこちらでいくつか記録しています：<https://github.com/xdp-project/xdp-project/blob/main/areas/bench/bench02_lpm-trie-lookup.org>.

###### _Linuxカーネル、パフォーマンス、またはデータ構造の最適化に興味がある方は、[当社のエンジニアリングチームが募集しています](https://www.cloudflare.com/en-gb/careers/jobs/?department=Engineering&location=default)。_

このページ

オンラインで議論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fa-deep-dive-into-bpf-lpm-trie-performance-and-optimization%2F&t=BPF%20LPM%E3%81%AE%E3%83%91%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%B3%E3%82%B9%E3%81%A8%E6%9C%80%E9%81%A9%E5%8C%96%E3%82%92%E6%B7%B1%E6%8E%98%E3%82%8A)[](https://x.com/intent/post?text=BPF+LPM%E3%81%AE%E3%83%91%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%B3%E3%82%B9%E3%81%A8%E6%9C%80%E9%81%A9%E5%8C%96%E3%82%92%E6%B7%B1%E6%8E%98%E3%82%8A&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fa-deep-dive-into-bpf-lpm-trie-performance-and-optimization%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fa-deep-dive-into-bpf-lpm-trie-performance-and-optimization%2F)[](https://bsky.app/intent/compose?text=BPF+LPM%E3%81%AE%E3%83%91%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%B3%E3%82%B9%E3%81%A8%E6%9C%80%E9%81%A9%E5%8C%96%E3%82%92%E6%B7%B1%E6%8E%98%E3%82%8A+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fa-deep-dive-into-bpf-lpm-trie-performance-and-optimization%2F)[](https://mastodonshare.com/?text=BPF+LPM%E3%81%AE%E3%83%91%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%B3%E3%82%B9%E3%81%A8%E6%9C%80%E9%81%A9%E5%8C%96%E3%82%92%E6%B7%B1%E6%8E%98%E3%82%8A&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fa-deep-dive-into-bpf-lpm-trie-performance-and-optimization%2F)[](https://www.threads.net/intent/post?text=BPF+LPM%E3%81%AE%E3%83%91%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%B3%E3%82%B9%E3%81%A8%E6%9C%80%E9%81%A9%E5%8C%96%E3%82%92%E6%B7%B1%E6%8E%98%E3%82%8A+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fa-deep-dive-into-bpf-lpm-trie-performance-and-optimization%2F)

## 関連するタグ

[eBPF](https://blog.cloudflare.com/ja-jp/tag/ebpf/)[IPv4](https://blog.cloudflare.com/ja-jp/tag/ipv4/)[IPv6](https://blog.cloudflare.com/ja-jp/tag/ipv6/)[Linux](https://blog.cloudflare.com/ja-jp/tag/linux/)[パフォーマンス](https://blog.cloudflare.com/ja-jp/tag/performance/)[詳細情報](https://blog.cloudflare.com/ja-jp/tag/deep-dive/)

SNS をフォロー

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 新しい投稿のお知らせを受け取るように登録する

メールアドレス

また、あなたのメールアドレスを共有したりすることはございません。

登録する

ご購読ありがとうございます！受信箱を確認して登録してください。
