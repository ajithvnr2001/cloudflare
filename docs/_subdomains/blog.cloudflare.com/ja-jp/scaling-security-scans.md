---
url: https://blog.cloudflare.com/ja-jp/scaling-security-scans/
title: \u30bb\u30ad\u30e5\u30ea\u30c6\u30a3\u30a4\u30f3\u30b5\u30a4\u30c8\u306e\u62e1\u5f35\uff1a\u30b0\u30ed\u30fc\u30d0\u30eb\u30b9\u30ad\u30e3\u30f3\u5bb9\u91cf\u309210\u500d\u306b\u62e1\u5927\u3057\u305f\u65b9\u6cd5 | Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:35:20.710959+00:00
---

# セキュリティインサイトの拡張：グローバルスキャン容量を10倍に拡大した方法 | Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/scaling-security-scans/

[ブログ](https://blog.cloudflare.com/ja-jp/)

[Kafka](https://blog.cloudflare.com/ja-jp/tag/kafka/)[Postgres](https://blog.cloudflare.com/ja-jp/tag/postgres/)[アプリケーションセキュリティ](https://blog.cloudflare.com/ja-jp/tag/application-security/)2件2件タグを表示

5 タグタグを5件表示

  * 投稿タグ
  * [Kafka](https://blog.cloudflare.com/ja-jp/tag/kafka/)[Postgres](https://blog.cloudflare.com/ja-jp/tag/postgres/)[アプリケーションセキュリティ](https://blog.cloudflare.com/ja-jp/tag/application-security/)[エンジニアリング](https://blog.cloudflare.com/ja-jp/tag/engineering/)[セキュリティ態勢管理](https://blog.cloudflare.com/ja-jp/tag/security-posture-management/)
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



[エンジニアリング](https://blog.cloudflare.com/ja-jp/tag/engineering/)[セキュリティ態勢管理](https://blog.cloudflare.com/ja-jp/tag/security-posture-management/)

[Kafka](https://blog.cloudflare.com/ja-jp/tag/kafka/)[Postgres](https://blog.cloudflare.com/ja-jp/tag/postgres/)[アプリケーションセキュリティ](https://blog.cloudflare.com/ja-jp/tag/application-security/)[エンジニアリング](https://blog.cloudflare.com/ja-jp/tag/engineering/)[セキュリティ態勢管理](https://blog.cloudflare.com/ja-jp/tag/security-posture-management/)

2026年6月12日

# セキュリティインサイトの拡張：グローバルスキャン容量を10倍に拡大した方法

![Dave Baxter](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46GGX3X5MXWP1Q0BBVAMCR.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Dave Baxter](https://blog.cloudflare.com/ja-jp/author/dave-baxter/)

14分で読了

URLをコピー

この記事は以下でも利用可能です [English](https://blog.cloudflare.com/scaling-security-scans/)、[한국어](https://blog.cloudflare.com/ko-kr/scaling-security-scans/).

![BLOG-3307 image6](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW455GF2NCFC9V7H6F5JSR8H.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/////vz78u7w6Obq6ers7fHx7fHx6err////+/v97Orx4ODq4OXs5u3y6e7y5ujt////+vr/5+j02Nzs2OHu4Ov05e315ejw/////f7/6ev52t/x2uTz4u756PH56Ov1////////8/T/5ur45u767ff/8fn/8PP7////////////9/j/9/v//P///f//+vz/////////////////////////////////////////////////////////////////)

_このコンテンツは自動機械翻訳サービスによる翻訳版であり、皆さまの便宜のために提供しています。原本の英語版と異なる誤り、省略、解釈の微妙な違いが含まれる場合があります。ご不明な点がある場合は、英語版原本をご確認ください。_

[ _セキュリティインサイト_](https://developers.cloudflare.com/security/security-insights/)は、すべてのCloudflareアカウントに対して実用的なセキュリティ推奨事項を提供します。これらの洞察を検出するために、すべてのアカウント、ゾーン、DNSレコードの定期スキャンを実施し、潜在的なセキュリティリスクや設定ミスを探します。  


しかし、2つの重要な問題が浮上しています。第一に、スキャンの頻度が低すぎました。スキャンは1～2週間に一度しか実行されていなかったため、新たに発生したセキュリティリスクは検出されないままとなる可能性があったのです。第二に、多くのFreeプランアカウントで自動スキャンがオプトインされており、多くのアカウントがまったくスキャンされていません。

スキャンの頻度が低い、または存在しないリスクが高まっています。自動化された攻撃が加速するにつれ、セキュリティの設定ミスを発見するためのウィンドウは縮小していきます。 _すべて_ のお客様についてこうした問題を発見することは、すべての人のためのより良いインターネットを構築するという当社の目的からみても重要なことです。

スキャン頻度を増やし、すべてのアカウントの自動スキャンを有効にするには、スキャンスループットを平均で約10倍、つまり毎秒10回から1秒あたり100回に増加させる必要があると計算しました。しかし、当社のシステムはすでに、その負荷に悩まされていました。数百万のイベントが処理待ちのバックログを満杯になっていたのです。 APIが頻繁にタイムアウトしていました。プロセスはクラッシュしていました。システムを修正し、 _拡張できるようにする_ 必要がありました。

これは、Security Insightsのスキャンスループットを10倍以上に向上させ、数百万のお客様に対するセキュリティインサイトを提供し、すべてのお客様に対するスキャン頻度を2倍にした方法についてです。この改善をどのように実現したかについて、以下で説明します。

## セキュリティインサイトのスキャン方法

大まかに説明すると、Cloudflareの自動セキュリティスキャンはスケジューラによってトリガーされます。アカウントまたはゾーンがスキャンの対象になると、スケジューラは[ _Apache Kafka_](https://blog.cloudflare.com/using-apache-kafka-to-process-1-trillion-messages/)（オープンソースの分散型イベントストリーミングプラットフォーム）にメッセージ（またはメッセージ）を公開します。これらのメッセージは、特定のアセットや設定をスキャンする専用のGoマイクロサービスなど、多くのチェッカーに向けられます。

すべてのメッセージに対し、各チェッカーはその結果（検出したセキュリティインサイト）を内部APIに送信し、APIはこれらをPostgresデータベースに永続化します。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3307 image2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44XA08C1D2X1ERGR4EQW9X.jpg&w=715&h=1163&f=webp&fit=cover&position=center)

## スケーリングする

### Kafkaのスケーリング

Apache Kafkaは厳密には _キュー_ ではありません。分割されたイベントストリームです（最近になって[ _キューのセマンティクス_](https://www.confluent.io/blog/kafka-queue-semantics-share-consumer-ga/)も獲得しましたが）。パーティション内では、メッセージは順番に消費され、 _処理され_ なければなりません。これは、メッセージが順番に消費される可能性がありますが、順不同で処理される一般的なキューとは異なります。したがって、 _コンシューマーグループ_ 内では、パーティションごとに1つのアクティブコンシューマーのみを持つことができます。

これは、当社にとって以下の2つの結果をもたらします。

  * 処理が遅いメッセージは、コンシューマーが次のメッセージに移ることを妨げます。
  * 各チェッカーには、パーティションの数だけのコンシューマーを持つことができます（各チェッカーには独自のコンシューマーグループがあります）



![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3307 image1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44G4BXDMSJ2RQWZAXHMFVV.jpg&w=715&h=585&f=webp&fit=cover&position=center)

パーティションをさらに追加することで、スケーリングを試みることもできました。しかし、これは他の多くのサービスと共有するKafkaブローカー自体のリソースの使用量が増加することになります。これは、最初にコードとアーキテクチャの改善を目的とした、最後の手段として確保しました。

### 並列処理の導入

メッセージを順番に消費するしかありませんが、複数のメッセージを一度に消費することを防ぐものはありません。

メッセージを _バッチ_ で消費するようにチェッカーを変更し、各メッセージを個別のゴルーチンで処理しました。その代償として、プロセスの途中でプロセスがクラッシュした場合、やり直す作業が増え、メモリ使用量がわずかに増加することになります。当社では、どちらも許容できる範囲でした。

### ヘッドオブラインブロッキングの回避

一部のチェッカーによって処理されるメッセージの中には、他のメッセージよりも処理に時間がかかるものがあります。たとえば、あるアカウント/ゾーンが、別のアカウント/ゾーンよりもはるかに多くのアセットを持つことがあります。最悪の場合、これらのメッセージは、数秒または数ミリ秒の平均的な処理と比較して、数分から数時間かかることがあります。

当社が選択したのは、非常にシンプルなアプローチで、消費者グループとチェッカーを「低速レーン」と「高速レーン」の2つに分けました。メッセージの処理が遅いか、速いかを迅速に判断できます。「高速レーン」チェッカーが遅いメッセージを遭遇した場合、それをスキップします。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3307 image9](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4681CBHS27WJTHBKZAKJSS.jpg&w=715&h=318&f=webp&fit=cover&position=center)

これにより問題が解決されました。遅いメッセージは専用のリソースと時間を確保することができ、最小限の遅延で処理され、速いメッセージは通常の高速ペースで進めることができました。

## データベースクエリの最適化

当社が見つけたインサイトはすべて、Postgresデータベースに書き込まれます。これは、チェッカーがインサイトのリストを使用して呼び出す単一のAPIエンドポイントによって処理されます。実装は次のようになりました：
    
    
    for _, issue := range issues {
    	_, err = tx.Exec(ctx, `INSERT INTO table ... VALUES ($1, $2, ...) ON CONFLICT DO UPDATE ...`, ...)
    	if err != nil {
    		return err
    	}
    }

情報通の読者であれば、このコードは大量のインサイトの場合、インサイトごとにデータベースとの往復を行うことに気づくでしょう。観測された最大規模は50万で、これは1回のAPI呼び出しで500万回のラウンドトリップ、クエリ、トランザクションを行ったことに相当します。

私たちは当初、Postgresにおける一括挿入の絶対的基準であるCOPYを一時テーブルに転送することを試みました。しかし、この方法ではPostgresシステムのテーブルが肥大化していることが判明しました。

当社は、ハイブリッド型のアプローチにたどり着きました。

  * 問題数が閾値を下回った場合はUNUNESTを使用
  * 問題数がこの閾値を超えた場合はCOPYを使用



これにより、膨大なインサイトのための比較的高速な挿入（秒）と、小さなインサイトのセットに対するより高速な挿入（ミリ秒）の両方の長所が得られました。

## APIタイムアウトの調査

スケーリングを試みた際、内部APIにおけるいくつかの奇妙な動作に気付きました。

  * 大量のリクエストがクライアント側のタイムアウトをトリガーしていた
  * 多くのチェッカーが、処理時間の20～90%を単一のAPI呼び出しに費やしていました
  * 大量のスキャンをトリガーすると、スループットが高くなり始め、\n低下する



これらの問題はすべて同じ根本原因がありました：**遅延** 。

当社のプライマリデータベースは、オレゴン州ポートランドにあります。しかし、当社のAPIはポートランドとアムステルダムの両方でアクティブに実行されていました。光速であっても、ポートランドとアムステルダムの間の往復遅延は50ミリ秒です。

この遅延の結果、アムステルダムのAPIインスタンスからのデータベースクエリーに大幅な時間がかかり、クライアント側の接続プールからの接続が開いた状態が保たれるようになりました。APIに大量のリクエストを送信すると、接続プールはすぐに使い果たされる可能性があり、無料の接続を待機するタイムアウトが発生しました。当社の平均API呼び出しはポートランドでは10ミリ秒で完了しますが、アムステルダムではほぼ3秒でした。

しかし、なぜメッセージスループットが低下するのでしょうか？各チェッカープロセスは、消費するKafkaストリームのパーティションのセットを割り当てられます。当社のAPIは負荷分散されています。プロセスの存続時間を通じて接続を開いておくので、一部のプロセスはAmsterdam APIに接続し、あるプロセスはポートランドAPIに接続しました。ポートランドにリンクされたパーティションはすぐに処理されましたが、アムステルダムに向かうプロセスで消費されたものは遅れていました。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3307 image7](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46HWWDWTHZ7T3R6W61H15N.png&w=715&h=327&f=webp&fit=cover&position=center)

 _Kafkaラグ（単一のコンシューマーグループ内での処理待ちのメッセージ数）を分割します。この場合、30のパーティションがあることに注意してください。正確に15のパーティションが遅れているのがわかります（3月10日03:00頃より遅くゼロに到達するか、ゼロに近づいている行）。これは、ロードバランサーがAPIエンドポイント間でトラフィックを均等に分割するためです。_

これは簡単な修正でした。APIを[ _アクティブ-パッシブ_](https://developers.cloudflare.com/load-balancing/load-balancers/common-configurations/#active---passive-failover)に切り替え、アクティブAPIがプライマリデータベースに従うようにしました。遅延の問題は一夜にして解決しました。

## スケジューラーの再考

Kafkaを拡張したのです。データベースクエリーを最適化しました。APIを修正したのです。しかし、まだ問題がありました。スキャンが時間内にほぼ均等に分散されることを確認する必要があるのです。Kafkaトピックは、時間ベースの保持ポリシーを使用しているため、すべてのスキャンを同時にキューに入れることはできませんでした。スキャンはKafkaに蓄積され、最終的に処理される前に削除されます。

スケジューラーは、スキャンを均一に配布するのが得意ではありませんでした。一度に起動されるスキャンの数は、急増し、予測不可能でした。1週間を通してある時点で、何十万ものスキャンが数分以内に相互トリガーされるのです。何が起こっていたのでしょうか？

スケジューラは、固定された繰り返し期間でスキャンをトリガーします。擬似コードでは、スケジューラは次のようになります：
    
    
    Loop forever:
        Find accounts where last_scheduled_at + scanning frequency <= now
        For each account:
            Trigger scan for account
            Trigger scan for all zones in the account
            Update last_scheduled_at = now

last_scheduled_atがデータベース内の多くのアカウントと類似しており、これが不均一な原因になっていたことにすぐ気付きました。

しかし、完全に均等な分布であっても、スキャン頻度を増やすと、この問題はさらに悪化したでしょう。たとえば、スキャン頻度を15日ごとから7日ごとに変更した場合、53%のアカウントが突然スキャンの対象になることを意味します。

このロジックにはさらに問題がありました。アカウントによっては、非常に多くのゾーンを持つものもあります。これらのアカウントがスケジュールされた時は、すべてのゾーンのスキャンが連鎖的に行われました。このため、Kafkaパーティションが飽和状態になり、はるかに小さなアカウントのスキャンに遅れが生じていました。

こうした問題を解決するために、当社は3つの重要な変更を行いました。

  * アカウントから独立してゾーンをスケジュール：各ゾーンは、独自のlast_scheduled_atフィールドを取得します。
  * 既存のアカウントとゾーンについて、最後の_scheduled_at時刻をランダム化します。
  * スキャンスケジュールに、適応型レート制限を導入。



ゾーンを個別にスケジュールすることは、大規模なアカウントの問題を解決する明らかな方法でした。last_scheduled_at時間をランダム化することで（そして、このプロセス中にスキャンが遅延しないことを確認する）、データベースに存在する不均一な状態を修正することができました。

適応型レート制限は少し興味深いものです。レート制限を使用することで、スキャン頻度を変更した場合のスキャンの急増の問題を解決できます。たとえば、スキャン頻度を7日ごとに増やしたい場合、5,000万件のアカウントがある場合、レート制限を最大83スキャン/秒に設定することで、7日間に均等に分散させることができます。

しかし、さらに1,000万件のアカウントを追加した場合はどうでしょうか？そして、このレート制限により、これらすべてのアカウントをスキャンするのに _8日_ かかります。ここで、 _適応_ 部分が活躍します。レート制限は、アカウントとゾーンの総数、およびスキャン頻度に基づいて、30分ごとに非同期的に再計算されます。これにより、何千、何百万ものアカウントやゾーンをオンボードできても、オンボードでスキャンを継続することができます。
    
    
    func computeRate(free, pro, biz, ent int64) rate.Limit {
       r := float64(free)/freeScanInterval.Seconds() +
          float64(pro)/proScanInterval.Seconds() +
          float64(biz)/bizScanInterval.Seconds() +
          float64(ent)/entScanInterval.Seconds()
    
    
       // Guard against zero counts. We always want to schedule at least one scan per second.
       if r < 1 {
          r = 1
       }
    
    
       // Increase rate limit beyond the 'perfect' value, to have a buffer in case of any downtime
       // or spikes in load.
       r *= rateLimitBufferFactor
    
    
       return rate.Limit(r)
    }

## 現在の状況

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3307 image8](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW469VYB4FFXZ8WJTD15TBTZ.png&w=715&h=324&f=webp&fit=cover&position=center)

 _これらの修正により、チェッカーあたり7日間移動する平均スループットが、時間の経過とともに10倍以上増加しました。_

今回の改善前は、1秒あたり約10回のスキャンを実行していました。目標とするスループットの1秒あたり100スキャンとのギャップは大きいように感じられました。私たちは、この問題にさらに多くのリソースを投入することや、Kafkaのトピックにさらに多くのパーティションを分割すること、つまりアーキテクチャ全体を放棄することについて議論しました。

しかし、当社の修正プログラムは違いをもたらしました。現在、Security Insightsは、ピーク時のスケジュール時に1秒あたり120回以上のスキャンを維持しており、当社の10倍の改善目標を上回っています。内部APIはタイムアウトしなくなり、Kafkaラグのメトリクスもずっと健全になりました。こうしたスケーラビリティの改善により、 _すべて_ の無料アカウントとゾーンの自動スキャンを有効にし、すべてのお客様のスキャン頻度を高めることができました。

  * Free：7日ごと
  * ProプランおよびBusinessプラン：3日ごと
  * Enterprise：毎日



システムの安定性が向上したことで、これまで制約があった新機能の構築に自信が持てました。きめ細かなオンデマンドスキャンを実行する機能を追加しました。Cloudflareアカウント、ゾーン、インサイト、またはインサイトタイプを手動で再スキャンできるようになりました。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3307 image3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW487T27G7ZW0EH3AM50T7R5.png&w=715&h=477&f=webp&fit=cover&position=center)

 _Cloudflareダッシュボードの[ _セキュリティ概要ページ_](https://blog.cloudflare.com/security-overview-dashboard/)から、詳細なオンデマンドスキャンを開始します_

私たちが学んだ教訓は、何かを廃棄する前に、既存のシステムを深く理解することが重要であるということです。コード、SQLクエリ、ログ、メトリクス（ _特に_ メトリクス）を精査することで、ポッドやパーティションを追加するだけで容量を増やすことができました。私たちの仮定を疑い、奇妙に見えるメトリクスを調べ、簡単な近道（APIクライアント側のタイムアウトを増やすなど）を拒否することで、より安定した耐障害性の高いシステムを構築しました。

問題により多くのリソースを投入することが _時には_ 解決策になるかもしれませんが、Cloudflareでは、エンジニアリングが問題を解決する方法だと考えています。

セキュリティインサイトのスキャンは、すべてのCloudflareプランでデフォルトで有効になっています。今すぐ[ _Cloudflareダッシュボード_](https://dash.cloudflare.com/?to=/:account/security-center)にログインして、セキュリティインサイトを確認し、管理しましょう。

このページ

オンラインで議論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fscaling-security-scans%2F&t=%E3%82%BB%E3%82%AD%E3%83%A5%E3%83%AA%E3%83%86%E3%82%A3%E3%82%A4%E3%83%B3%E3%82%B5%E3%82%A4%E3%83%88%E3%81%AE%E6%8B%A1%E5%BC%B5%EF%BC%9A%E3%82%B0%E3%83%AD%E3%83%BC%E3%83%90%E3%83%AB%E3%82%B9%E3%82%AD%E3%83%A3%E3%83%B3%E5%AE%B9%E9%87%8F%E3%82%9210%E5%80%8D%E3%81%AB%E6%8B%A1%E5%A4%A7%E3%81%97%E3%81%9F%E6%96%B9%E6%B3%95)[](https://x.com/intent/post?text=%E3%82%BB%E3%82%AD%E3%83%A5%E3%83%AA%E3%83%86%E3%82%A3%E3%82%A4%E3%83%B3%E3%82%B5%E3%82%A4%E3%83%88%E3%81%AE%E6%8B%A1%E5%BC%B5%EF%BC%9A%E3%82%B0%E3%83%AD%E3%83%BC%E3%83%90%E3%83%AB%E3%82%B9%E3%82%AD%E3%83%A3%E3%83%B3%E5%AE%B9%E9%87%8F%E3%82%9210%E5%80%8D%E3%81%AB%E6%8B%A1%E5%A4%A7%E3%81%97%E3%81%9F%E6%96%B9%E6%B3%95&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fscaling-security-scans%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fscaling-security-scans%2F)[](https://bsky.app/intent/compose?text=%E3%82%BB%E3%82%AD%E3%83%A5%E3%83%AA%E3%83%86%E3%82%A3%E3%82%A4%E3%83%B3%E3%82%B5%E3%82%A4%E3%83%88%E3%81%AE%E6%8B%A1%E5%BC%B5%EF%BC%9A%E3%82%B0%E3%83%AD%E3%83%BC%E3%83%90%E3%83%AB%E3%82%B9%E3%82%AD%E3%83%A3%E3%83%B3%E5%AE%B9%E9%87%8F%E3%82%9210%E5%80%8D%E3%81%AB%E6%8B%A1%E5%A4%A7%E3%81%97%E3%81%9F%E6%96%B9%E6%B3%95+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fscaling-security-scans%2F)[](https://mastodonshare.com/?text=%E3%82%BB%E3%82%AD%E3%83%A5%E3%83%AA%E3%83%86%E3%82%A3%E3%82%A4%E3%83%B3%E3%82%B5%E3%82%A4%E3%83%88%E3%81%AE%E6%8B%A1%E5%BC%B5%EF%BC%9A%E3%82%B0%E3%83%AD%E3%83%BC%E3%83%90%E3%83%AB%E3%82%B9%E3%82%AD%E3%83%A3%E3%83%B3%E5%AE%B9%E9%87%8F%E3%82%9210%E5%80%8D%E3%81%AB%E6%8B%A1%E5%A4%A7%E3%81%97%E3%81%9F%E6%96%B9%E6%B3%95&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fscaling-security-scans%2F)[](https://www.threads.net/intent/post?text=%E3%82%BB%E3%82%AD%E3%83%A5%E3%83%AA%E3%83%86%E3%82%A3%E3%82%A4%E3%83%B3%E3%82%B5%E3%82%A4%E3%83%88%E3%81%AE%E6%8B%A1%E5%BC%B5%EF%BC%9A%E3%82%B0%E3%83%AD%E3%83%BC%E3%83%90%E3%83%AB%E3%82%B9%E3%82%AD%E3%83%A3%E3%83%B3%E5%AE%B9%E9%87%8F%E3%82%9210%E5%80%8D%E3%81%AB%E6%8B%A1%E5%A4%A7%E3%81%97%E3%81%9F%E6%96%B9%E6%B3%95+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fscaling-security-scans%2F)

## 関連するタグ

[Kafka](https://blog.cloudflare.com/ja-jp/tag/kafka/)[Postgres](https://blog.cloudflare.com/ja-jp/tag/postgres/)[アプリケーションセキュリティ](https://blog.cloudflare.com/ja-jp/tag/application-security/)[エンジニアリング](https://blog.cloudflare.com/ja-jp/tag/engineering/)[セキュリティ態勢管理](https://blog.cloudflare.com/ja-jp/tag/security-posture-management/)

SNS をフォロー

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 新しい投稿のお知らせを受け取るように登録する

メールアドレス

また、あなたのメールアドレスを共有したりすることはございません。

登録する

ご購読ありがとうございます！受信箱を確認して登録してください。
