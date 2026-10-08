---
url: https://blog.cloudflare.com/ja-jp/hyper-bug/
title: \u30cf\u30a4\u30d1\u30fcHTTP\u30e9\u30a4\u30d6\u30e9\u30ea\u306e\u30d0\u30b0\u306e\u767a\u898b\u65b9\u6cd5 | Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:36:41.772370+00:00
---

# ハイパーHTTPライブラリのバグの発見方法 | Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/hyper-bug/

[ブログ](https://blog.cloudflare.com/ja-jp/)

[Cloudflare Images](https://blog.cloudflare.com/ja-jp/tag/cloudflare-images/)[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[オープンソース](https://blog.cloudflare.com/ja-jp/tag/open-source/)3件3件タグを表示

6 タグタグを6件表示

  * 投稿タグ
  * [Cloudflare Images](https://blog.cloudflare.com/ja-jp/tag/cloudflare-images/)[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[オープンソース](https://blog.cloudflare.com/ja-jp/tag/open-source/)[画像の最適化](https://blog.cloudflare.com/ja-jp/tag/image-optimization/)[開発者](https://blog.cloudflare.com/ja-jp/tag/developers/)[開発者プラットフォーム](https://blog.cloudflare.com/ja-jp/tag/developer-platform/)
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



[画像の最適化](https://blog.cloudflare.com/ja-jp/tag/image-optimization/)[開発者](https://blog.cloudflare.com/ja-jp/tag/developers/)[開発者プラットフォーム](https://blog.cloudflare.com/ja-jp/tag/developer-platform/)

[Cloudflare Images](https://blog.cloudflare.com/ja-jp/tag/cloudflare-images/)[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[オープンソース](https://blog.cloudflare.com/ja-jp/tag/open-source/)[画像の最適化](https://blog.cloudflare.com/ja-jp/tag/image-optimization/)[開発者](https://blog.cloudflare.com/ja-jp/tag/developers/)[開発者プラットフォーム](https://blog.cloudflare.com/ja-jp/tag/developer-platform/)

2026年6月22日

# ハイパーHTTPライブラリのバグの発見方法

![Deanna Lam](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47KFXCHBMAHQ4B20STFNCC.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Diretnan Domnan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47Q4B9ZYMXFBZ5X354KFW2.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Matt Lewis](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW9WMRANK371K7W3Y3CXQT0M.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Deanna Lam](https://blog.cloudflare.com/ja-jp/author/deanna/)、[Diretnan Domnan](https://blog.cloudflare.com/ja-jp/author/diretnan-domnan/)、[Matt Lewis](https://blog.cloudflare.com/ja-jp/author/matt-lewis-2/)

21分で読了

URLをコピー

この記事は以下でも利用可能です [English](https://blog.cloudflare.com/hyper-bug/)、[한국어](https://blog.cloudflare.com/ko-kr/hyper-bug/).

![BLOG-3318 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW9WKWXBGMT7K0V773578D1B.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAAQAAaRgAeUBQtVyxBWDVRVDJVUCBKTQAyQQAbUAsmajQ7ekdPfE5bc0dbYjROUxQ3QwAaWiErfkZGlFtal2BjiVdgcUJRWCU5RQAUXygrhk5JnmJdoWdlkl1gd0dOWio3RwABXiQkgUpEll5YmWJfildYcUFGWCUuSQAAWBUScT04gU9LgVNRdEhKYjM4UhIdSgAAUQAAXSooZDw8YT5BWDQ7UBwnTAAASgAATgAAUx8eVDE0TzM6SCgzRgseSgAA)

[_Images_](https://developers.cloudflare.com/images/)サービスは、Rustで構築され[ _Workers_](https://developers.cloudflare.com/workers/)上で動作しており、Cloudflareのエッジネットワーク上のすべてのマシンで実行されています。クライアント接続を処理するために、Rust用のオープンソースHTTPライブラリである[ _hyper_](https://github.com/hyperium/hyper)を使用しています。

昨年、私たちは[ _Imagesバインディングを導入し_](https://blog.cloudflare.com/improve-your-media-pipelines-with-the-images-binding-for-cloudflare-workers/)、Workersでリモート画像を処理するためのカスタムのプログラムワークフローを可能にしました。2025年末には、WorkersランタイムとImagesサービス間のより直接的なローカル接続を提供するために、バインディングを再設計しました。

ロールアウト直後、バインディングからのTransformationsリクエストが失敗しているという報告を受けましたが、それは断続的かつ大きな画像のみでした。さらに奇妙なことに、これらのリクエストに対する応答は、エラーがログに記録されることなく、`200` ステータスを返しました。画像データは単に切り捨てられ、2メガバイトになるはずの応答が数百キロバイトで届くことがあります。

私たちは6週間、特定の条件下でのみ発生する競合状態である、Imagesバインディングが処理した画像データをクライアントに返す方法に影響を与えるハイパーライブラリのバグを追跡することに費やしました。最終的に、その修正には4行のコードが必要になりました。

### ホップ、ハンドオフ、ハイパー

Cloudflare上で開発を行う場合、開発者はバインディングを通じてWorkersからアクセスできる一連のプラットフォームサービスからフルスタックアプリケーションを作成します。[ _バインディング_](https://developers.cloudflare.com/workers/runtime-apis/bindings/)は、[ _コンピューティング_](https://www.cloudflare.com/products/#compute)、[ _ストレージ_](https://www.cloudflare.com/products/#storage)、[ _AI推論_](https://www.cloudflare.com/products/#ai)、[ _メディア処理_](https://www.cloudflare.com/products/#media)など、開発者プラットフォーム上のリソースに直接APIを提供します。

Imagesのバインディングは、画像の最適化を配信から切り離します。出力をHTTPレスポンスとして返すことなく、画像のトランスコード、合成、操作を行うことができます。また、[ _最適化パラメーター_](https://developers.cloudflare.com/images/optimization/features/)を、[ _URLインターフェース_](https://developers.cloudflare.com/images/optimization/features/#url-interface)によって課される固定された順序に従うのではなく、任意の順序で適用することもできます。ここでは、Workerは画像データをImages APIに直接渡し、操作を連鎖させ、処理された結果をストリームとして返すことができます。
    
    
    const result = await env.IMAGES
      .input(image)
      .transform({ width: 800, rotate: 90 })
      .output({ format: "image/avif" });
    return result.response();

大まかにいうと、このように画像データはさまざまなサービスを介して移動します。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3318 image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW9WM1JKG14FT6JFWG5YX2QK.png&w=715&h=400&f=webp&fit=cover&position=center)

 _パイプは、中間者とImagesの間のソケット接続を表し、データはカーネルのバッファを介して、あるプロセスから次のプロセスに引き渡されます。_

バインディングは、Workersランタイムによって管理されるソケット接続を介してImagesと通信します。ソケット接続は、2つのプロセス間の通信チャネルです。ソケットの各エンドには、オペレーティングシステムのカーネルによって管理されるバッファがあります。これらのバッファは、データの一方が書き込んだ後、他方の読み取り前に位置する一時的な保持領域です。

HyperはImagesサービス側の接続を管理し、ソケットから届いたリクエストを読み取り、レスポンスを書き込みます。

リクエストがImagesバインディングを使用する場合、Imagesサービスは入力を読み取り、要求された最適化操作を実行し、結果をエンコードします。そして、エンコードされた画像全体を単一のメモリ内ブロックとしてhyperに渡します。

Hyperは、このレスポンスデータを自身の内部バッファに書き込みます。この時点で、ハイパーは送信する必要のあるすべてのバイトがあるため、エンコーディングの作業が完了したと判断します。次のステップは、内部バッファをソケットのアウトバウンドバッファに消去し、データをImagesサービスから反対側の仲介者に移動することです。

相手側のリーダーが高速である場合、ハイパーフラッドは一度のパスですべてを消去できます。リーダーは到着するのと同じくらいの速さでデータを消費するため、アウトバウンドバッファに余地があるでしょう。すべてのデータが送信されると、hyperはソケット上で`シャットダウン`を発行し、接続が終了し、それ以上データが書き込まれないことを通知します。しかし、Readerの速度が数ミリ秒でも遅いと、アウトバウンドバッファがいっぱいになり、ハイパーは書き込みを続けるための余地ができるまで待たなければなりません。

### ローカルの

Cloudflareネットワーク上のすべての着信トラフィックは、FLを通過します。FLは、セキュリティ機能とパフォーマンス機能を実行し、リクエストを適切なバックエンドにルーティングする内部仲介サービスです。バインディングを最初にローンチしたとき、画像データはWorkersランタイムからFLを経由してImagesサービスへ流れてきました。

このパスは当社の最初のリリースに自然に適合しており、URLインターフェースと同じアーキテクチャに従います。しかし、時が経つにつれて、このFLとの組み合わせが制約になりました。バインディングに変更を加えるたびに、FLのリリースサイクルに従わなければならないという制約があったのです。

2025年12月、ImagesチームはFLを同じマシン上で動作する新しい中間サービスである内部Workerバインディングに置き換えました。元のアーキテクチャでは、データはFLを介してネットワークソケットを経由して移動していました。このパスは、DNSルックアップやルーティングなど、FLの完全な処理パイプラインのオーバーヘッドをもたらしました。

内部バインディングは、これらをUnixソケットに置き換えて、同じマシン上のサービスを直接接続し、FLとネットワークスタックのオーバーヘッドをバイパスします。これにより、Imagesへのリクエストパスが高速化され、チームはバインディングリリースを独立して制御できるようになりました。

ロールアウト後数日以内に、最初のお客様からの報告を受けました。

### 200 OK (OKではありません)

最初のトラブルの兆候は、あるお客様からでした。非標準設定は、1つのパイプラインの中に別のパイプラインがネストされている、2つの画像処理レイヤーでした。

まず、WorkerはImagesバインディングを使用して、R2の複数大きなソース画像（JPEG背景とPNGオーバーレイレイヤー）を1つの結合JPEGに結合しました。次に、URLインタフェースを介して結果をさらに圧縮し、トランスコードし、サイズ変更します。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3318 image 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW9WM3D5WAMWP2BB8FW0YNMW.png&w=715&h=400&f=webp&fit=cover&position=center)

 _このバグは、内部パイプラインのリターンパスで発生し、応答が外部パイプラインに到達する前に切り捨てられました。_

内部パイプライン（変換バインディング）が、コンポジットを処理しました。外側のパイプライン（Transformations URL）は、スケーリングやフォーマット変換といった配信の最適化を処理しました。この階層型アプローチは、内部パイプラインがサイレントに切り捨てられたレスポンスを返した時に、1レベル上の唯一の目に見えるエラーが現れることを意味します。
    
    
    error reading a body from connection: end of file before message length reached

外側のパイプラインは、内側のパイプラインからHTTP `200` を受け取り、`Content-Length` ヘッダーは数メガバイトを約束しました。実際の本文はそのほんの一部でした。1回のリクエストでは、予定されている3.3MBのうち、約200KBしか到着しなかったのです。エラーは外側のパイプラインで表面化しましたが、切り捨てはバインディング、中間サービス、Imagesサービス、またはそれらの間のどこかで発生した可能性があります。

ブラウザが切り捨てられた画像を受信すると、結果が表示されます。フォーマットによって、画像は部分的にレンダリングするか（例：下の半分がない、またはグレー）、または完全にデコードされず、壊れた画像が表示されます。

### 秘密環境でのデバッグ

ここから、リクエストパスをたどって内部的な作業を行い、各層をテストして、切り捨てが発生している場所を分離しました。こうした取り組みのいくつかは行き詰りました。また、検索を絞り込んだブリーフクラムを残している人もいます。

  * **複製の作成。** お客様のネストされたセットアップを模倣したワーカーを作成し、バインディングだけでバグをトリガーできるようになるまでレイヤーを取り除きました。小さなスクリプトでリクエストをバッチ処理することができます。初期の1回の実行では、25のリクエストのうち19件が失敗しました。到着したデータの量は—およそ200KB—は、本番環境のソケットバッファのサイズに疑わしいほど悪用されました。これにより、問題は顧客の設定に限定されないことが確認され、オンデマンドでバグをトリガーする確実な方法が得られたのです。
  * **タイムアウトの調査中。** 当初、切り捨てがタイムアウト動作（つまり、時間制限後に接続がクローズされている）に関連しているのではないかと疑いました。切り捨てはリクエスト期間と相関しないため、この理論は成り立ちません。
  * **ハイパーバージョンを更新中。** 最初にバグが報告された当時、当社は0.14.xを実行していましたが、最新のハイパーバージョンは約1.8.xでした。当社では、ハイパーバージョン0.14、1.7、1.8でテストを行いましたが、最も明白な答えが正しい（そして最も簡単な）答えであった場合に備えて、しかし、バグは各バージョンで発生するもので、アップストリームへの修正プログラムが存在しないということです。
  * **ローカルでの再現。** macOSとDebian仮想マシンでローカル統合テストを実施しました。かなりの負荷がかかっているにもかかわらず、当社のローカルリクエストが障害を引き起こすことはありません。バインディングソケットに直接curlリクエストを行い、キャプチャされたリクエストを再生することが、常に動作しているように見えました。バグは、ソケットの反対側に実際の同時実行と実際のWorkersランタイムクライアントがある場合にのみ、完全な本番パスで発生しました。このため、ランタイム自体を疑うことになりました。
  * **Workersランタイムを除外。** Workersランタイムがバインディングソケットを介してImagesと通信するために使用するHTTPクライアントを調査しました。接続の両側のトレースのいずれにも、予期しないクローズまたは早期の終了を示すsyscallが示されませんでした。クライアントは正しく動作し、他の複数のサービスが同じクライアントを問題なく使用していることが確認されました。
  * **分散トレース。** エンドツーエンドのリクエストトレースを検査することで、切り捨てられた本文がお客様のセットアップの外部Transformations層に到達する前にすでに存在していることを確認しました。これにより、問題は内部パイプライン、つまりImagesサービスを介したバインディングパスに狭められました。
  * **仲介サービスのインストルメンテーション。** 仲介サービスに、レスポンスデータを転送する前にボディサイズを測定するためのインスツルメンテーションを追加しました。本文はImagesサービスを離れる時点ですでに切り捨てられていたため、仲介者は除外されました。
  * **Imagesサービス内のより深いトレース。** サービスレベルでは、リクエストが処理され、画像は適切にエンコードされ、レスポンスはHTTP `200`で送信されました。



唯一一貫した兆候は、バグがタイミングに依存するということでした。それは本番パスで、実際に同時実行されている上にだけ、より大きな画像に対してのみ現れました。

### 情報の核

アプリケーションレベルのデバッグ用ツールには、システムが実行していると考えていることだけを伝えました。しかし、システムによるとすべて問題ありませんでした。トレースは、レスポンスが送信されたと述べました。ログ記録はエラーを報告せず、Imagesサービスはすべてのリクエストで`200`を返しました。

システムが実際に行っていたことを確認するために、Imagesサービスに`strace`をアタッチしました。`strace`は、プロセスがカーネルに行うsyscallを記録します。これにより、どのバイトが書かれたか、いつシャットダウンが呼び出されたか、そしてクライアントが終了シグナルを送信したかどうかを正確に示すことができます。

トレースの設定は繊細でした。`strace`は、syscallが発生したときにそれを傍受することで機能し、それぞれにわずかなタイミングオーバーヘッドが追加されます。狭い範囲のsyscallのセットをフィルタリングすることで、そのオーバーヘッドを最小限に抑えることができました。しかし、フィルターの幅を広げることで、消去とシャットダウンチェックのタイミングを変えるのに十分なほどプロセスを遅らせ、バグを完全に消えさせることができました。これだけでも、問題はタイミングを重要視するという私たちの理論を裏付けるものです。

Replicated Workerを使用して、バグをトリガーし、リクエストが成功した場合と失敗した場合のsyscallの出力を比較しました。

リクエストが成功した場合、レスポンスはソケットバッファが許可するようにチャンクで書かれ、すべてのデータが送信された後にのみシャットダウンが呼び出されます。例えば、これは次のようになります：
    
    
    sendto(42, "HTTP/1.1 200 OK\r\nContent-Length: 14991808\r\n...", ...) = 219264
    sendto(42, "\xff\xd8\xff\xe0...", 292352) = 292352
    // ... keeps writing until buffer drains ...
    sendto(42, "...", 292352) = 292352
    shutdown(42, SHUT_WR) = 0

このバグを再現したところ、失敗したリクエストは次のようになりました。
    
    
    sendto(42, "HTTP/1.1 200 OK\r\nContent-Length: 14991808\r\n...", ...) = 219264
    shutdown(42, SHUT_WR) = 0

ここでは、シャットダウンがすぐに呼び出される前に、1回の書き込み（ヘッダーと本文のほんの一部）しかありません。14.9MBのレスポンスのうち、約219KBしか送信されなかったのです。残りの約14.8 MBの画像データがhyperの内部バッファを離れることはなく、書き込みとシャットダウンの間にクライアントからの終了信号もありませんでした。その代わりに、Imagesサービスは、接続が完了したと信じて、自ら接続を急いでシャットダウンしました。

失敗したリクエストにより、バグが断続的にトリガーされる競合状態であることが確認されました。リクエストが成功するか失敗するかは、消去とシャットダウンの操作がリクエストからリクエストへと変化するかどうかによって決まります。ハイパーが接続が終了したと判断した瞬間、バッファがまだ満杯になっていたとき、データは失われました。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3318 image 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW9WMQYFZ5QYQVP0826XYCS2.png&w=715&h=400&f=webp&fit=cover&position=center)

 _リーダーの消費がハイパー書き込みより遅いと、アウトバウンドバッファがいっぱいになります。バッファが枯渇する前にハイパーが接続を遮断すると、仲介者に到達するのはレスポンスのごく一部だけです。この不完全なデータは、Workersランタイムとクライアントに転送されます。_

12月の再構築では、複数のメジャーバージョンにわたって何年も前から存在していたバグを発見しませんでした。しかし、新しい仲介者によって、ソケットの応答側で読み取る人が変更されました。私たちの実用的な理論は、以前の仲介者であるFLが十分な速度でデータを消費したため、ソケットバッファが応答中にほとんど満たされないということです。新しいリーダーは、より大きな応答の中にバッファが一杯になるようなペースで読むことがあります。

この数ミリ秒のバックプレッシャーは、他のすべてを高速化する改善によってもたらされ、潜在的に隠れていた欠陥を表面化させるのに必要な全てでした。

### ディスパッチループ内

HyperのHTTP/1接続ライフサイクルは、`dispatch.rs`というファイル内のステートマシンによって駆動されます。リクエストを読み取り、応答を書き込み、書き込みバッファをソケットに消去し、シャットダウンのタイミングを決定するループを実行します。簡略化された形式：
    
    
    fn poll_loop(&mut self, cx: &mut Context<'_>) -> Poll<Result<(), Error>> {
        loop {
            let _ = self.poll_read(cx)?;
            let _ = self.poll_write(cx)?;
            let _ = self.poll_flush(cx)?;
    
            if !self.conn.wants_read_again() {
                return Poll::Ready(Ok(()));
            }
        }
    }

より正確には、`poll_flash`の前の`let_`がバグがある場所です。

Rustでは、`let _ = expr`は、`Poll::Pending`（フラッシュがまだ完了していないことを示すシグナル）を含め、式の結果を破棄します。フラッシュのバッファにはまだバイトがバッファにあるかもしれませんが、ループはそれを見つけることはありません。

リクエストが失敗した場合の正確なイベントシーケンスは次の通りです。

  1. Imagesサービスは、画像のエンコーディングを完了し、Hyperへのレスポンス全体を単一のメモリ内ブロックとして引き渡します。
  2. Hyperはブロックを内部バッファに書き込み、書き込み状態を`Writing::Closed`としてマークします。エンコーディングの観点から見ると、作業が完了しました。エンコードすることは何もありません。
  3. Hyperは`poll_flush`を呼び出し、バッファリングされたデータをソケットに移動します。先ほどの例では、ソケットは約219KBを受け入れました。残りの約14.8MBはハイパーのバッファに留まります。ソケットがフルになっているため、カーネルは`Poll::Pending`を返します。
  4. `poll_loop`は`Poll::Pending`を`let _`と共に破棄します。
  5. `wants_read_again()`を確認します。完全なリクエストはすでに受信しているため、これは`false`を返します。
  6. `poll_loop`は`Poll::Ready(Ok(()))`を返し、フラッシュが完了していないにもかかわらず、ループが終了したことを知らせます。
  7. `poll_shutdown()`が起動します。`SHUT_WR`システムコールが発行されます。
  8. クライアントは、14.9 MBを想定しているにもかかわらず、接続がクローズされていることを示す219KBとEOF（end-of-file）を受け取ります。



2番目のステップでは、ハイパーはレスポンス本文が実際に消去されたときではなく、バッファリングされた瞬間（つまり、エンコーディングが終了したとき）に書き込み操作が完了したものとしてマークします。ほとんどの場合、消去はシングルパスで完了するため、この区別は見えません。稀なケースでは、ソケットバッファがフルの場合、flashは待機しなければなりません。ハイパーは待機しなくても、です。バイトはまだハイパーのバッファにあり、ソケットにプッシュされるのを待ちます。Hyperは、このデータをまだバッファにある状態で、接続をシャットダウンします。

これは、curlがバグをトリガーしなかった理由も説明しています。curlは到着と同じ速さでデータを読み取ります。ソケットバッファは決して満たされず、消去は常に即座に完了し、破棄される戻り値は無害です。本番環境のパスは読み取りが数ミリ秒間一時停止することもあり、バッファが間違った瞬間に収まったのは唯一の設定でした。

### コンプライアンスを忘れない

数週間に及ぶ調査の後、修正自体は概念的にシンプルでした。Hyperは、移動する前に、消去が実際に行われたかどうかを確認する必要がありました。

当社のレプリケーションワーカーはバグの存在を確認しましたが、あるリクエストが失敗した理由を知ることはできませんでした。修正を書く前に、hyper内の正確なソケット条件をトリガーできるテストが必要でした。

私たちは、データのチャンクを受け入れてからブロックするソケットが、バグのトリガーとなる条件を把握していました。制御されたシナリオでテストするために、完全なソケットバッファをシミュレートするTCPストリームの周りのカスタムラッパーを構築しました。ラッパーは最初の書き込みで8KBを受け入れ、それ以降の書き込みごとに`Poll::Pending`を返し、バッファの消費を止めたリーダーを模倣しました。

テストでは、この制約のあるソケットを介して500KBのレスポンスを送信し、492KBがまだバッファリングされている間に、シャットダウンと呼ばれるハイパーリングが実行されるかどうかを確認しました。修正せず対処してしまう可能性はありました。修正後は、待ちました。

当初、ハイパーのディスパッチループに修正を適用しました。`poll_flush`の結果を破棄する代わりに、実際にフラッシュが行われたかどうかを確認しました。
    
    
    let flush_result = self.poll_flush(cx)?;
    
    if flush_result.is_pending() {
        return Poll::Pending;
    }
    
    if !self.conn.wants_read_again() {
        return Poll::Ready(Ok(()));
    }

消去が完了していない場合、ループは非同期ランタイムに`Poll::Pending`を返します。ランタイムはソケットが書き込み可能になるのを待ち、キャッシュを消去するためにバックアップを起動します。すべてのデータが送信された後にのみ、接続はシャットダウンします。

この修正をデプロイした場合、すべてのバイトが書き込まれ、バッファが実際に空になった後にのみシャットダウンが呼び出されたことが確認されました。最初の報告を行ったお客様も、問題が解消したことを確認しています。

最初のソリューションは機能していましたが、ディスパッチループは修正には適切な場所ではありませんでした。早期に`Poll::Pending`を返すと、読み取りのポーリング頻度が減り、同じ接続上の他の操作が遅くなり、意図しないバックプレッシャーが発生する可能性があります。また、単一の接続が複数のリクエストを順番に処理するキープアライブ接続を正しく処理できません。これらは、前のレスポンスがまだ削除されている間でも、再利用可能である必要があります。どちらの問題も（キープアライブが無効になっている場合）特定のサービスには影響を与えませんでしたが、修正がアップストリームに貢献した場合は、他のハイパーユーザーに影響を与える可能性があります。

弊社は、Hyperの接続ライフサイクルを追跡し、より的を絞ったアプローチを発見しました。ディスパッチループの動作を変更するのではなく、実際にシャットダウンが呼び出された時点で修正を適用しました。ソケットをシャットダウンする前に、ハイパーはバッファに残っているデータをすべて消去します。
    
    
    pub(crate) fn poll_shutdown(
        &mut self,
        cx: &mut Context<'_>,
    ) -> Poll<io::Result<()>> {
        ready!(self.poll_flush(cx)?);
        Pin::new(&mut self.io).poll_shutdown(cx)
    }

これにより、ディスパッチループは変更されません。過負荷状態であれば、データ損失が発生するであろうポイント、つまり、シャットダウンの直前にのみフラッシュを追加します。

### Cloudflareに残されたもの

アプリケーションレベルのツールは、いずれも有用な手がかりとなるエラーやクラッシュ、ログエントリーを表面化するものではありませんでした。アプリケーションレベルの可観測性は、認識以下に存在するバグの盲点を生じる可能性があります。

この障害は断続的に発生し、レスポンスのサイズによって拡大し、curlのような簡単なツールでは再現できず、システムをより詳しく観察した時には消失しました。これらのシグナルは、アプリケーションのロジックではなく、接続層のタイミング依存のバグを指摘していました。

私たちのブレイクスルーは、カーネルレベルのツールである`strace`を使用することで実現しました。straceは、ソケット上で実際に起こったことを記録する1つのレイヤーです。根本的なバグは、部分的なフラッシュから時期尚早なシャットダウンまでの数ミリ秒の間に発生しました。このウィンドウは、システムを高速化した後に初めて開いたのです。

[ _PR #4018_](https://github.com/hyperium/hyper/pull/4018)で、修正と決定論的テストを`hyperium/hyper`に統合しました。これは将来のハイパーリリースで利用可能になる予定で、ハイパーのHTTP/1実装を使用するサービスは同じ競合状態でレスポンスデータを失うことはありません。

同時に、パッチを適用した内部フォークを実行しています。この修正により、バインディングのアーキテクチャが安定し、機能を拡張するための信頼性の高い基盤ができました。

Imagesのバインディングは当初、リモートImagesのTransformationsだけをカバーしていました。今月初め、[ _Imagesバインディングがホストされた画像の操作に対応しました_](https://developers.cloudflare.com/changelog/post/2026-06-10-hosted-images-binding/)と発表しました。これにより、開発者はCloudflare上でメディアリッチなアプリケーションを構築するための統一された方法を利用できるようになります。

バインディングの仕組みについて詳しくは、[ _当社のドキュメント_](https://developers.cloudflare.com/images/storage/binding/)をご覧ください。

  


このページ

オンラインで議論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fhyper-bug%2F&t=%E3%83%8F%E3%82%A4%E3%83%91%E3%83%BCHTTP%E3%83%A9%E3%82%A4%E3%83%96%E3%83%A9%E3%83%AA%E3%81%AE%E3%83%90%E3%82%B0%E3%81%AE%E7%99%BA%E8%A6%8B%E6%96%B9%E6%B3%95)[](https://x.com/intent/post?text=%E3%83%8F%E3%82%A4%E3%83%91%E3%83%BCHTTP%E3%83%A9%E3%82%A4%E3%83%96%E3%83%A9%E3%83%AA%E3%81%AE%E3%83%90%E3%82%B0%E3%81%AE%E7%99%BA%E8%A6%8B%E6%96%B9%E6%B3%95&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fhyper-bug%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fhyper-bug%2F)[](https://bsky.app/intent/compose?text=%E3%83%8F%E3%82%A4%E3%83%91%E3%83%BCHTTP%E3%83%A9%E3%82%A4%E3%83%96%E3%83%A9%E3%83%AA%E3%81%AE%E3%83%90%E3%82%B0%E3%81%AE%E7%99%BA%E8%A6%8B%E6%96%B9%E6%B3%95+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fhyper-bug%2F)[](https://mastodonshare.com/?text=%E3%83%8F%E3%82%A4%E3%83%91%E3%83%BCHTTP%E3%83%A9%E3%82%A4%E3%83%96%E3%83%A9%E3%83%AA%E3%81%AE%E3%83%90%E3%82%B0%E3%81%AE%E7%99%BA%E8%A6%8B%E6%96%B9%E6%B3%95&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fhyper-bug%2F)[](https://www.threads.net/intent/post?text=%E3%83%8F%E3%82%A4%E3%83%91%E3%83%BCHTTP%E3%83%A9%E3%82%A4%E3%83%96%E3%83%A9%E3%83%AA%E3%81%AE%E3%83%90%E3%82%B0%E3%81%AE%E7%99%BA%E8%A6%8B%E6%96%B9%E6%B3%95+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fhyper-bug%2F)

## 関連するタグ

[Cloudflare Images](https://blog.cloudflare.com/ja-jp/tag/cloudflare-images/)[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[オープンソース](https://blog.cloudflare.com/ja-jp/tag/open-source/)[画像の最適化](https://blog.cloudflare.com/ja-jp/tag/image-optimization/)[開発者](https://blog.cloudflare.com/ja-jp/tag/developers/)[開発者プラットフォーム](https://blog.cloudflare.com/ja-jp/tag/developer-platform/)

SNS をフォロー

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 新しい投稿のお知らせを受け取るように登録する

メールアドレス

また、あなたのメールアドレスを共有したりすることはございません。

登録する

ご購読ありがとうございます！受信箱を確認して登録してください。
