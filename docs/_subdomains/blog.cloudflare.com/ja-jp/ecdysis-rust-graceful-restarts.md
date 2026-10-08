---
url: https://blog.cloudflare.com/ja-jp/ecdysis-rust-graceful-restarts/
title: Equinix\u306b\u3088\u308b\u53e4\u3044\u30b3\u30fc\u30c9\u306e\u5ec3\u68c4\uff1aCloudflare\u306b\u304a\u3051\u308bRust\u30b5\u30fc\u30d3\u30b9\u306e\u30b0\u30ec\u30fc\u30b9\u30d5\u30eb\u30ea\u30b9\u30bf\u30fc\u30c8 | Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:49:45.026038+00:00
---

# Equinixによる古いコードの廃棄：CloudflareにおけるRustサービスのグレースフルリスタート | Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/ecdysis-rust-graceful-restarts/

[ブログ](https://blog.cloudflare.com/ja-jp/)

[Rust](https://blog.cloudflare.com/ja-jp/tag/rust/)[アプリケーションサービス](https://blog.cloudflare.com/ja-jp/tag/application-services/)[インフラストラクチャ](https://blog.cloudflare.com/ja-jp/tag/infrastructure/)5件5件タグを表示

8 タグタグを8件表示

  * 投稿タグ
  * [Rust](https://blog.cloudflare.com/ja-jp/tag/rust/)[アプリケーションサービス](https://blog.cloudflare.com/ja-jp/tag/application-services/)[インフラストラクチャ](https://blog.cloudflare.com/ja-jp/tag/infrastructure/)[エッジ](https://blog.cloudflare.com/ja-jp/tag/edge/)[エンジニアリング](https://blog.cloudflare.com/ja-jp/tag/engineering/)[オープンソース](https://blog.cloudflare.com/ja-jp/tag/open-source/)[開発者](https://blog.cloudflare.com/ja-jp/tag/developers/)[開発者プラットフォーム](https://blog.cloudflare.com/ja-jp/tag/developer-platform/)
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



[エッジ](https://blog.cloudflare.com/ja-jp/tag/edge/)[エンジニアリング](https://blog.cloudflare.com/ja-jp/tag/engineering/)[オープンソース](https://blog.cloudflare.com/ja-jp/tag/open-source/)[開発者](https://blog.cloudflare.com/ja-jp/tag/developers/)[開発者プラットフォーム](https://blog.cloudflare.com/ja-jp/tag/developer-platform/)

[Rust](https://blog.cloudflare.com/ja-jp/tag/rust/)[アプリケーションサービス](https://blog.cloudflare.com/ja-jp/tag/application-services/)[インフラストラクチャ](https://blog.cloudflare.com/ja-jp/tag/infrastructure/)[エッジ](https://blog.cloudflare.com/ja-jp/tag/edge/)[エンジニアリング](https://blog.cloudflare.com/ja-jp/tag/engineering/)[オープンソース](https://blog.cloudflare.com/ja-jp/tag/open-source/)[開発者](https://blog.cloudflare.com/ja-jp/tag/developers/)[開発者プラットフォーム](https://blog.cloudflare.com/ja-jp/tag/developer-platform/)

2026年2月13日

# Equinixによる古いコードの廃棄：CloudflareにおけるRustサービスのグレースフルリスタート

![Manuel Olguín Muñoz](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45MRZQBM4H5K19ZVS98WTD.png&w=64&h=64&f=webp&fit=cover&position=center)

[Manuel Olguín Muñoz](https://blog.cloudflare.com/ja-jp/author/manuel-olguin-munoz/)

13分で読了

URLをコピー

この記事は以下でも利用可能です [English](https://blog.cloudflare.com/ecdysis-rust-graceful-restarts/)、[한국어](https://blog.cloudflare.com/ko-kr/ecdysis-rust-graceful-restarts/).

![BLOG-3121 Hero Image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47APEZTY8GYKA04QBEVEE0.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/////f/97fLy4uft4+jy6e/37fHz6u7p/////v//6+702t/u1t3y3uX45+v27O3s////////6uz21NjvzNP01dz75Of57u7w////////7+7419jxztP3193/5+r+8/H1////////+PX75uPz4OD75+r/8vT/+vj6///////////9+PL29/T//P3////////+//////////////73///////////////////////////////4////////////////)

_このコンテンツは自動機械翻訳サービスによる翻訳版であり、皆さまの便宜のために提供しています。原本の英語版と異なる誤り、省略、解釈の微妙な違いが含まれる場合があります。ご不明な点がある場合は、英語版原本をご確認ください。_

> ecdysis | _ˈekdəsəs_ |
> 
> noun
> 
> 古い表請求書を移行したり、虫組やを見るような説明行為を移行するために、外請求ケースに移行することです。 

1つの接続も中断させることなく、世界中で1秒あたり数百万のリクエストを処理するネットワークサービスをアップグレードするにはどうすればよいでしょうか？

この大きな課題に対するCloudflareのソリューションの1つが、長年にわたり[** _ecdysis_**](https://github.com/cloudflare/ecdysis)です。これは、ライブ接続がドロップされず、新しい接続が拒否されないグレースフルプロセスリスタートを実装するRustライブラリです。

先月、**私たちはECサイトをオープンソース化し** 、誰でも利用できるようにしました。Cloudflareで5年間本番運用されているecdysisは、当社の重要なRustインフラストラクチャ全体でダウンタイムゼロのアップグレードを可能にし、Cloudflareの[ _グローバルネットワーク_](https://www.cloudflare.com/network/)全体で、再起動のたびに数百万のリクエストを節約することで、その有効性を実証しました。

こうしたアップグレードを正しく行うことの重要性は、特にCloudflareのネットワークの規模では、強調することの難しさです。当社のサービスの多くは、トラフィックルーティング、[ _TLSライフサイクル管理_](https://www.cloudflare.com/application-services/solutions/certificate-lifecycle-management/)、ファイアウォールルールの適用など、重要なタスクを実行し、継続的に稼働しなければなりません。それらのサービスの1つが一時的にもダウンすれば、壊滅的な影響を受ける可能性があります。接続の切断やリクエストの失敗は、すぐに顧客のパフォーマンス低下とビジネスへの影響につながります。

これらのサービスの更新が必要になった場合、セキュリティパッチの適用を待つことはできません。バグ修正にはデプロイが必要で、新機能をロールアウトする必要があります。

古いプロセスが停止するのを待ってから新しいプロセスを起動する必要がありますが、これにより、接続が拒否され、リクエストがドロップされる時間枠ができます。単一の場所で毎秒数千のリクエストを処理するサービスが、数百のデータセンター全体で処理されるリクエスト数を掛け合わせると、簡単な再起動で世界中で何百万ものリクエストが失敗します。

問題を掘り下げ、ECdysisが私たちにとってどのようにソリューションとなったか、そして貴社にも役立つかもしれません。 

**リンク** : [GitHub](https://github.com/cloudflare/ecdysis) **|** [crates.io](https://crates.io/crates/ecdysis) **|** [docs.rs](https://docs.rs/ecdysis)

### グレースフルリスタートが難しい理由

前述したように、サービスを再起動する際の単純なアプローチは、古いプロセスを止めて新しいプロセスを開始することです。これは、リアルタイム要求を処理しないシンプルなサービスであれば問題なく機能しますが、ライブ接続を処理するネットワークサービスでは、このアプローチには重大な制限があります。

まず、単純なアプローチでは、着信接続を待機するプロセスが作成されます。古いプロセスが停止すると、リッスンソケットを閉じ、OSは `ECONNREFUSED` との新しい接続を即座に拒否します。新しいプロセスがすぐに開始されたとしても、ミリ秒か数秒かにかかわらず、接続を受け入れないギャップが常にあります。1秒あたり数千のリクエストを処理するサービスでは、100ミリ秒のギャップでさえ、何百もの接続が切断されることを意味します。

第二に、古いプロセスを停止すると、すでに確立された接続がすべて消失します。大きなファイルをアップロードしたり、動画をストリーミングしたりするクライアントが突然切断されます。WebSocketsやgRPCストリームのような長期間の接続は、運用の途中で終了します。クライアントから見れば、サービスは失われただけです。

古いプロセスをシャットダウンする前に新しいプロセスをバインディングすると、これは解決するように見えますが、さらなる問題も引き起こします。カーネルは通常、1つのプロセスのみを1つのアドレス:ポートの組み合わせにバインドできますが、[ _SO_REUSEPORTソケットオプション_](https://man7.org/linux/man-pages/man7/socket.7.html)では複数のバインドが可能です。しかし、これはプロセスの移行中に問題が発生するため、グレースフルリスタートには適していません。

`SO_REUSEPORT`を使用すると、カーネルは各プロセスに対して個別のリッスンソケットを作成し、[ _これらのソケット間で新しい接続を負荷分散します_](https://lwn.net/Articles/542629/)。接続の最初の`SYN`パケットが受信されると、カーネルはそれをリッスンプロセスの1つに割り当てます。最初のハンドシェイクが完了すると、接続はプロセスが受け入れるまでプロセスの`accept()`キューにあります。その後、プロセスがこの接続を受け入れる前に終了すると、オーファン、カーネルによって終了されます。GitHubのエンジニアリングチームは、[ _GLB Directorロードバランサーを構築する際に_](https://github.blog/2020-10-07-glb-director-zero-downtime-load-balancer-updates/)、この問題を広範囲に文書化しました。

### Edysisの仕組み

Equinixのデザインと構築に着手した際、私たちはライブラリの4つの主要目標を特定しました。

  1. **古いコードはアップグレード後に完全にシャットダウンできます** 。
  2. **新しいプロセスには、初期化の猶予期間があります** 。
  3. **初期化中に新しいコードがクラッシュしても許容されます** 。実行中のサービスに影響を与えるべきではありません。
  4. **カスケード障害を回避するために、一度のアップグレードだけが** 並行で実行されます。



ecdysisは、初期の頃からグレースフルアップグレードをサポートしてきたNGINXが開拓したアプローチに従って、これらの要件を満たしています。アプローチは簡単です。

  1. 親プロセスは新しい子プロセスを `fork()` します。
  2. 子プロセスは、`execve()` を使用して、コードの新しいバージョンに置き換わります。
  3. 子プロセスは、親と共有される名前付きパイプを介してソケットファイル記述子を引き継ぎます。
  4. 親プロセスは、子プロセスが準備完了を知らせるのを待ち、シャットダウンします。



![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3121 Image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46QD03TCDXHTGDDCMT2B4Z.png&w=695&h=750&f=webp&fit=cover&position=center)

重要なのは、移行中もソケットがオープンのままであることです。子プロセスは、名前付きパイプを介して共有されるファイル記述子として、親から待機中のソケットを引き継ぎます。子のプロセスの初期化中、両方のプロセスが同じ基盤となるカーネルデータ構造を共有するため、親は新規および既存の接続を引き続き受け入れて処理します。子が初期化を完了すると、親に通知し、接続の受け入れを開始します。この準備完了通知を受け取ると、親はリッスンソケットのコピーを即座にクローズし、既存の接続のみの処理を続けます。

このプロセスにより、子供に安全な初期化期間を提供しながら、適用範囲のギャップを排除します。親と子が同時に接続を受け入れることがあります。これは意図的なものであり、親によって受け入れられた接続は、枯渇プロセスの一環として完了するまで単純に処理されます。

このモデルは、必要な衝突安全性も提供します。子プロセスが初期化中に失敗した場合（例えば、設定エラーが原因で）は、単に終了するだけです。親が待機を停止したことはないため、接続が切断されることはなく、問題が修正されればアップグレードを再度試行することができます。

ecdysisは、[ _Tokio_](https://tokio.rs)と`systemd`統合による非同期プログラミングの一流のサポートを通じて、フォークモデルを実装します。

  * **Tokioの統合** ：Tokioのネイティブ非同期ストリームラッパー。引き出されたソケットは、グルーコードを追加することなくリスナーになります。同期サービスの場合、ecdysisは非同期ランタイム要件なしの操作をサポートします。
  * **systemd-notify サポート** : `systemd_notify` 機能を有効にすると、ecdysis は systemd のプロセスライフサイクル通知と自動的に統合されます。サービスユニットファイルで`Type=notify-reload`を設定すると、systemdがアップグレードを正しく追跡できるようになります。
  * **systemd named sockets** : `systemd_sockets`機能によって、ecdysisはsystemdでアクティブ化されたソケットを管理することができます。サービスはソケットでアクティブ化し、グレースフルリスタートを同時にサポートできます。



プラットフォームの注意：ecdysisは、ソケットの継承とプロセス管理のためにUnix固有のsyscallに依存しています。Windowsでは動作しません。これは、フォーク手法の基本的な制限です。

### セキュリティの考慮事項

グレースフルリスタートには、セキュリティ上の考慮事項があります。フォークモデルでは、2つのプロセス世代が共存する短いウィンドウが作成されます。両方が同じリッスンソケットと潜在的に機密性のあるファイル記述子にアクセスできます。

ecdysisは、設計を通じてこれらの懸念に対処しています。

**Fork-then-exec** : ecdysisは、`fork()`の後に`execve()`が続く従来のUnixパターンに従います。これにより、子プロセスは、新しいアドレス空間、新しいコード、およびメモリを引き継ぎない状態で開始されます。明示的に渡されたファイル記述子のみが境界を越えます。

**明示的な引き継ぎ** ：リッスンソケットと通信パイプのみが引き継がれます。その他のファイル記述子は、`CLOEXEC`フラグを介してクローズされます。これにより、機密性の高いアドレスの偶発的な漏洩を防ぐことができます。

**seccompの互換性** : seccompフィルタを使用するサービスは、`fork()`と`execve()`を許可しなければなりません。グレースフルリスタートにはシステムコールが必要なため、ブロックすることはできません。

ほとんどのネットワークサービスでは、こうしたトレードオフは許容されます。フォーク実行モデルのセキュリティはよく理解されており、NGINXやApacheなどのソフトウェアで数十年にわたって実地テストが行われています。

### コード例

実際の例を見てみましょう。以下は、グレースフルリスタートをサポートする簡略化されたTCPエコーサーバーです。
    
    
    use ecdysis::tokio_ecdysis::{SignalKind, StopOnShutdown, TokioEcdysisBuilder};
    use tokio::{net::TcpStream, task::JoinSet};
    use futures::StreamExt;
    use std::net::SocketAddr;
    
    #[tokio::main]
    async fn main() {
        // Create the ecdysis builder
        let mut ecdysis_builder = TokioEcdysisBuilder::new(
            SignalKind::hangup()  // Trigger upgrade/reload on SIGHUP
        ).unwrap();
    
        // Trigger stop on SIGUSR1
        ecdysis_builder
            .stop_on_signal(SignalKind::user_defined1())
            .unwrap();
    
        // Create listening socket - will be inherited by children
        let addr: SocketAddr = "0.0.0.0:8080".parse().unwrap();
        let stream = ecdysis_builder
            .build_listen_tcp(StopOnShutdown::Yes, addr, |builder, addr| {
                builder.set_reuse_address(true)?;
                builder.bind(&addr.into())?;
                builder.listen(128)?;
                Ok(builder.into())
            })
            .unwrap();
    
        // Spawn task to handle connections
        let server_handle = tokio::spawn(async move {
            let mut stream = stream;
            let mut set = JoinSet::new();
            while let Some(Ok(socket)) = stream.next().await {
                set.spawn(handle_connection(socket));
            }
            set.join_all().await;
        });
    
        // Signal readiness and wait for shutdown
        let (_ecdysis, shutdown_fut) = ecdysis_builder.ready().unwrap();
        let shutdown_reason = shutdown_fut.await;
    
        log::info!("Shutting down: {:?}", shutdown_reason);
    
        // Gracefully drain connections
        server_handle.await.unwrap();
    }
    
    async fn handle_connection(mut socket: TcpStream) {
        // Echo connection logic here
    }

主要ポイント：

  1. **`build_listen_tcp`** は、子プロセスに引き継がれるリスナーを作成します。
  2. **`ready()`** は、初期化が完了し、安全に終了できることを親プロセスに通知します。
  3. **`shutdown_fut.await`** は、アップグレードまたは停止が要求されるまでブロックします。この未来は、アップグレード/リロードが正常に実行された、またはシャットダウンシグナルを受信したために、プロセスをシャットダウンする必要がある場合にのみ発生します。



このプロセスに`SIGHUP`を送信すると、ecdysisは次のような動作をします。

 _…親プロセス上：_

  * バイナリの新しいインスタンスをフォークして実行します。
  * リッスンソケットを子に渡します。
  * 子が`ready()`を呼び出すのを待ちます。
  * 既存の接続を実行し、その後、出口を出します。



 _...子プロセス上：_

  * 親と同じ実行フローに従って自身を初期化しますが、ecdysisが所有するソケットは継承され、子にバインドされません。
  * `ready()`を呼び出して、親に準備完了を知らせます。
  * シャットダウンまたはアップグレードシグナル待ちのブロック。



### 大規模な本番環境

ECdysisはCloudflareで2021年から稼働しています。120か国以上、330以上のデータセンターにデプロイされた重要なRustのインフラストラクチャサービスを支えています。これらのサービスは、1日あたり数十億件のリクエストを処理し、セキュリティパッチ、機能リリース、設定変更のための頻繁な更新を必要としています。

Ecdysisを使用して再起動を行うたびに、単純なStop/Startサイクルではドロップされる可能性がある何十万ものリクエストが保存されます。グローバルフットプリント全体で、これは何百万もの接続の維持とお客様のための信頼性の向上につながります。

### ECサイトとその代わり

いくつかのエコシステム用のグレースフルリスタートライブラリが存在します。適切なツールを選択するためには、ECサイトを使用するタイミングと代替ツールを理解することが重要です。

[** _tableflip_**](https://github.com/cloudflare/tableflip) は、ecdysisの着想元となった当社のGoライブラリです。Goサービスと同じフォークとインジェクションモデルを実装しています。Goが必要なら、tableflipをお勧めします！

[** _shellflip_**](https://github.com/cloudflare/shellflip) は、CloudflareのRustベースのプロキシであるOxy用に特別に設計された、Cloudflareの他のRustグレースフルリスタートライブラリです。Shellflipは、システム化と時発生を想定し、親と子の間で任意のアプリケーション状態を転送することに焦点を当てています。これは、複雑なステートフルサービスや、独自のソケットを開くことさえできない積極的なサンドボックスを適用したいサービスに優れていますが、より単純なケースではオーバーヘッドが追加されます。

### 構築を開始する

ecdysisは、Rustのエコシステムに5年間にわたる本番ハードウェアとしてのグレースフルリスタート機能を提供します。これは、Cloudflareのグローバルネットワーク全体の何百万もの接続を保護しているのと同じ技術で、現在オープンソース化され、誰でも利用できるようになっています。

完全なドキュメントは、[ _docs.rs/ecdysis_](https://docs.rs/ecdysis)でご覧いただけます。API参照、一般的なユースケースの例、`systemd`との統合手順など。

リポジトリの[ _サンプルディレクトリ_](https://github.com/cloudflare/ecdysis/tree/main/examples)には、TCPリスナー、Unixソケットリスナー、およびsystemd統合を示す動作コードが含まれています。

このライブラリは、Argo Smart Routing & Orpheusチームによって積極的に保守されており、Cloudflare全体のチームの貢献も受けています。[ _GitHub_](https://github.com/cloudflare/ecdysis)での貢献、バグ報告、機能リクエストを歓迎します。

高性能プロキシを構築する場合でも、長期間維持されるAPIサーバーでも、稼働率が重要なネットワークサービスであっても、ECdysisはダウンタイムゼロの運用基盤を提供できます。

構築を開始する:[ _github.com/cloudflare/ecdysis_](https://github.com/cloudflare/ecdysis)

このページ

オンラインで議論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fecdysis-rust-graceful-restarts%2F&t=Equinix%E3%81%AB%E3%82%88%E3%82%8B%E5%8F%A4%E3%81%84%E3%82%B3%E3%83%BC%E3%83%89%E3%81%AE%E5%BB%83%E6%A3%84%EF%BC%9ACloudflare%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8BRust%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9%E3%81%AE%E3%82%B0%E3%83%AC%E3%83%BC%E3%82%B9%E3%83%95%E3%83%AB%E3%83%AA%E3%82%B9%E3%82%BF%E3%83%BC%E3%83%88)[](https://x.com/intent/post?text=Equinix%E3%81%AB%E3%82%88%E3%82%8B%E5%8F%A4%E3%81%84%E3%82%B3%E3%83%BC%E3%83%89%E3%81%AE%E5%BB%83%E6%A3%84%EF%BC%9ACloudflare%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8BRust%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9%E3%81%AE%E3%82%B0%E3%83%AC%E3%83%BC%E3%82%B9%E3%83%95%E3%83%AB%E3%83%AA%E3%82%B9%E3%82%BF%E3%83%BC%E3%83%88&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fecdysis-rust-graceful-restarts%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fecdysis-rust-graceful-restarts%2F)[](https://bsky.app/intent/compose?text=Equinix%E3%81%AB%E3%82%88%E3%82%8B%E5%8F%A4%E3%81%84%E3%82%B3%E3%83%BC%E3%83%89%E3%81%AE%E5%BB%83%E6%A3%84%EF%BC%9ACloudflare%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8BRust%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9%E3%81%AE%E3%82%B0%E3%83%AC%E3%83%BC%E3%82%B9%E3%83%95%E3%83%AB%E3%83%AA%E3%82%B9%E3%82%BF%E3%83%BC%E3%83%88+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fecdysis-rust-graceful-restarts%2F)[](https://mastodonshare.com/?text=Equinix%E3%81%AB%E3%82%88%E3%82%8B%E5%8F%A4%E3%81%84%E3%82%B3%E3%83%BC%E3%83%89%E3%81%AE%E5%BB%83%E6%A3%84%EF%BC%9ACloudflare%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8BRust%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9%E3%81%AE%E3%82%B0%E3%83%AC%E3%83%BC%E3%82%B9%E3%83%95%E3%83%AB%E3%83%AA%E3%82%B9%E3%82%BF%E3%83%BC%E3%83%88&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fecdysis-rust-graceful-restarts%2F)[](https://www.threads.net/intent/post?text=Equinix%E3%81%AB%E3%82%88%E3%82%8B%E5%8F%A4%E3%81%84%E3%82%B3%E3%83%BC%E3%83%89%E3%81%AE%E5%BB%83%E6%A3%84%EF%BC%9ACloudflare%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8BRust%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9%E3%81%AE%E3%82%B0%E3%83%AC%E3%83%BC%E3%82%B9%E3%83%95%E3%83%AB%E3%83%AA%E3%82%B9%E3%82%BF%E3%83%BC%E3%83%88+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fecdysis-rust-graceful-restarts%2F)

## 関連するタグ

[Rust](https://blog.cloudflare.com/ja-jp/tag/rust/)[アプリケーションサービス](https://blog.cloudflare.com/ja-jp/tag/application-services/)[インフラストラクチャ](https://blog.cloudflare.com/ja-jp/tag/infrastructure/)[エッジ](https://blog.cloudflare.com/ja-jp/tag/edge/)[エンジニアリング](https://blog.cloudflare.com/ja-jp/tag/engineering/)[オープンソース](https://blog.cloudflare.com/ja-jp/tag/open-source/)[開発者](https://blog.cloudflare.com/ja-jp/tag/developers/)[開発者プラットフォーム](https://blog.cloudflare.com/ja-jp/tag/developer-platform/)

SNS をフォロー

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 新しい投稿のお知らせを受け取るように登録する

メールアドレス

また、あなたのメールアドレスを共有したりすることはございません。

登録する

ご購読ありがとうございます！受信箱を確認して登録してください。
