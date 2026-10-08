---
url: https://blog.cloudflare.com/ja-jp/building-jetflow-a-framework-for-flexible-performant-data-pipelines-at-cloudflare/
title: Jetflow\u306e\u69cb\u7bc9\uff1aCloudflare\u306b\u304a\u3051\u308b\u67d4\u8edf\u3067\u9ad8\u6027\u80fd\u306a\u30c7\u30fc\u30bf\u30d1\u30a4\u30d7\u30e9\u30a4\u30f3\u306e\u30d5\u30ec\u30fc\u30e0\u30ef\u30fc\u30af | Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:49:58.761789+00:00
---

# Jetflowの構築：Cloudflareにおける柔軟で高性能なデータパイプラインのフレームワーク | Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/building-jetflow-a-framework-for-flexible-performant-data-pipelines-at-cloudflare/

[ブログ](https://blog.cloudflare.com/ja-jp/)

[Go](https://blog.cloudflare.com/ja-jp/tag/go/)[エンジニアリング](https://blog.cloudflare.com/ja-jp/tag/engineering/)[データ](https://blog.cloudflare.com/ja-jp/tag/data/)2件2件タグを表示

5 タグタグを5件表示

  * 投稿タグ
  * [Go](https://blog.cloudflare.com/ja-jp/tag/go/)[エンジニアリング](https://blog.cloudflare.com/ja-jp/tag/engineering/)[データ](https://blog.cloudflare.com/ja-jp/tag/data/)[デザイン](https://blog.cloudflare.com/ja-jp/tag/design/)[パフォーマンス](https://blog.cloudflare.com/ja-jp/tag/performance/)
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



[デザイン](https://blog.cloudflare.com/ja-jp/tag/design/)[パフォーマンス](https://blog.cloudflare.com/ja-jp/tag/performance/)

[Go](https://blog.cloudflare.com/ja-jp/tag/go/)[エンジニアリング](https://blog.cloudflare.com/ja-jp/tag/engineering/)[データ](https://blog.cloudflare.com/ja-jp/tag/data/)[デザイン](https://blog.cloudflare.com/ja-jp/tag/design/)[パフォーマンス](https://blog.cloudflare.com/ja-jp/tag/performance/)

2025年7月23日

# Jetflowの構築：Cloudflareにおける柔軟で高性能なデータパイプラインのフレームワーク

![Harry Hough](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47C0JMBM7Y7F2GNX2R8X3Q.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Rebecca Walton-Jones](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47P62GPSPWQJMX49XBJ9PK.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Andy Fan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44WD6HZHWZDZ6D51EB2YHJ.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Ricardo Margalhau](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4692VQ40ERSW2HS1VWGJ06.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Uday Sharma](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45ZJ46DGX82MAJPNK0SWE0.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Harry Hough](https://blog.cloudflare.com/ja-jp/author/harry-hough/)、[Rebecca Walton-Jones](https://blog.cloudflare.com/ja-jp/author/rebecca-walton-jones/)、[Andy Fan](https://blog.cloudflare.com/ja-jp/author/andy-fan/)、[Ricardo Margalhau](https://blog.cloudflare.com/ja-jp/author/ricardo-margalhau/)、[Uday Sharma](https://blog.cloudflare.com/ja-jp/author/uday-sharma/)

15分で読了

URLをコピー

この記事は以下でも利用可能です [English](https://blog.cloudflare.com/building-jetflow-a-framework-for-flexible-performant-data-pipelines-at-cloudflare/)、[简体中文](https://blog.cloudflare.com/zh-cn/building-jetflow-a-framework-for-flexible-performant-data-pipelines-at-cloudflare/).

![BLOG-2837 Hero Image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW462TCT85Q26AWRTEYW6ZAB.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/////Pv78fHw6Onr6Orv6+307O3x6uno/////f7/7vHz4ebs4Obw5ev16e3z6uvr////////7PL33OXv2eTy4Or46O/37O/v////////7/b73Ofz2eX24e386/P78PT0////////9vv/5e744uz76vP/8/n/9/r6////////////8fb97/X/9/v//f/////+////////////+/3/+/3/////////////////////////////////////////////)

_このコンテンツは自動機械翻訳サービスによる翻訳版であり、皆さまの便宜のために提供しています。原本の英語版と異なる誤り、省略、解釈の微妙な違いが含まれる場合があります。ご不明な点がある場合は、英語版原本をご確認ください。_

CloudflareのBusiness Intelligenceチームは、[ _ペタバイト_](https://simple.wikipedia.org/wiki/Petabyte)規模の[ _データレイク_](https://www.cloudflare.com/learning/cloud/what-is-a-data-lake/)を管理し、多くの異なるソースから毎日数千のテーブルを取り込みます。これには、PostgresやClickHouseなどの内部データベースや、Salesforceのような外部SaaSアプリケーションが含まれます。これらのタスクはしばしば複雑で、テーブルは毎日何億行もの新しいデータ行があることがあります。また、製品の決定、成長計画、社内の監視にもビジネス上の重要な役割を担っています。毎日合計**約1410億行** が取り込まれています。

Cloudflareが成長するにつれ、データはこれまで以上に大きく複雑になりました。既存の[ _抽出負荷変換（ELT）_](https://www.ibm.com/think/topics/elt)ソリューションでは、技術面とビジネス面での要件を満たすことができなくなりました。他の一般的なELTソリューションを評価した結果、そのパフォーマンスも概ね現行システムを上回らないという結論に至りました。

そして、当社独自の要件に対処するために独自のフレームワークを構築する必要があることが明らかになりました。そして、**Jetflow** が誕生したのです。

## 当社が実現したこと

**100倍以上の効率向上（GB-S）** ：

  * 190億行で最も長時間実行されているジョブは、**300 GBのメモリ** を使用して**48時間** かかっていましたが、**4 GBのメモリ** を使用して**5.5時間で完了します**
  * Cloudflareでは、クラウドプロバイダーが発表した料金を基に、**Jetflow** 経由でPostgresから50TBのコストを取り込む場合、100ドル未満のコストが発生すると推定されています。



**10倍以上のパフォーマンス向上：**

  * 最大のデータセットは毎秒**60～80,000** 行を取り込んでおり、今ではデータベース接続ごとに毎秒**200万～500万** 行になっています。
  * さらに、これらの数はデータベースによっては複数のデータベース接続を使っても拡張性があります。



**拡張性：**

  * モジュラー設計により、拡張やテストが容易になります**。** 現在、**Jetflow** はClickHouse、Postgres、Kafka、多くの異なるSaaS APIs、Google BigQuery、その他多くの企業と連携しています。新たなユースケースの追加にも柔軟に対応し続けてきました。



## これを実現した方法

### 要件

新しいフレームワークを設計するための第一歩は、解決しようとしている問題を明確に理解し、新しいものを作るのです。

##### パフォーマンスと効率性

取り込みジョブによっては最大24時間かかることもあり、データは増加の一途になるため、より多くのデータをより短い時間で移動できるようにする必要がありました。データはストリーミング形式で取り込まれ、既存のソリューションよりも少ないメモリと計算リソースを使用する必要があります。

##### 後方互換性

毎日何千ものテーブルが取り込まれることを考えると、このソリューションは必要に応じて個々のテーブルの移行を可能にする必要がありました。[ _Spark_](https://spark.apache.org/)ダウンストリームの使用と、異なる[ _Parquet_](https://parquet.apache.org/)スキーマのマージにおけるSparkの制限により、選択したソリューションは、レガシーと一致するために各ケースに必要な正確なスキーマを生成する柔軟性を提供する必要がありました。

また、依存関係チェックとジョブステータス情報に使用されるカスタムメタデータシステムとのシームレスな統合も必要でした。

##### 使いやすさ

同時変更が多いリポジトリにボトルネックが発生することなく、バージョン管理できる設定ファイルが求められています。

チーム内の異なる役割のためのアクセシビリティを高めるために、もう1つの要件はノーコード（またはコードとしての構成）です。ユーザーは、ソースシステムとターゲットシステム間でデータタイプの可用性や変換を心配したり、新しい取り込みのたびに新しいコードを書く必要はありません。必要な設定も最小限に抑える必要があります。たとえば、データスキーマはソースシステムから推測できるものであり、ユーザーからの提供は必要ありません。

##### カスタマイズ可能

上記のノーコード要件とバランスを取るために、参入のハードルを低く抑えながら、柔軟でオプションの設定レイヤーで、必要に応じてオプションを調整し、オーバーライドできるオプションを持ちたいと考えています。例えば、Parquetファイルの書き込みは、データベースからの読み取りよりもコストが高いことが多いので、必要に応じて、より多くのリソースやコンカレンシーを割り当てることができるようにしたいのです。

さらに、私たちは別のスレッド、異なるコンテナ、または異なるマシンで同時Workerをスピンアップする機能によって、作業が実行される場所を制御できるようにしたいと考えました。Workersの実行とデータの通信はインターフェースで抽象化され、ジョブ設定によってさまざまな実装を書いて注入し、制御することができます。

##### テスト可能

私たちは、パイプラインのすべての段階でテストを書くことができる、コンテナ化された環境でローカルで実行できるソリューションを求めていました。「ブラックボックス」ソリューションでは、テストは変更を加えた後の出力の検証を意味することが多いですが、これはフィードバックループが遅く、すべてのコードパスの可視性が社内にないと、すべてのエッジケースをテストしないリスクがあり、デバッグが面倒になります。

### 柔軟な枠組みを設計する

真に柔軟なフレームワークを構築するために、パイプラインを異なるステージに分割し、設定レイヤーを作成して、これらのステージからのパイプラインのコンポジションと、あらゆる設定のオーバーライドを定義します。論理的に意味のあるパイプライン設定はすべて正しく実行されなければならず、ユーザーは機能しないパイプライン設定を作成することができないはずです。

##### パイプラインの構成

これが以下の意味を持つ異なるカテゴリーに応じて分類された段階を作る設計になりました。

  * 消費者
  * トランスフォーマー（Transformers）
  * ローダー



![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2837 Image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44BCCZX621VT1MJRYZ0A3P.png&w=715&h=339&f=webp&fit=cover&position=center)

パイプラインは、コンシューマー、0つ以上のトランスフォーマー、少なくとも1つのローダーを必要とする[ _YAML_](https://yaml.org/)ファイルを介して構築されました。コンシューマーは（ソースシステムからの読み取りで）データストリームを作成し、トランスフォーマー（データTransformations、検証など）は、同じAPIに準拠するデータストリームを入力／出力することで連鎖できるようにします。ローダーは同じデータストリーミングインターフェースを持ちますが、永続的な影響を持つステージ（つまり、データが保存されるステージ）です外部システムに提供することになります

このモジュラー設計は、各ステージが独立してテスト可能であり、共有動作（エラー処理やコンカレンシーなど）は共有ベースステージから受け継がれており、新たなユースケースの開発時間を大幅に短縮し、コードの正確性の信頼性を高めます。

##### データ分割

次に、パイプライン全体の再実行と、一時的なエラーによるデータパーティションの内部リトライの両方で、パイプラインが偽装されることを可能にするデータ内訳を設計しました。私たちは、パイプラインが再試行に必要なデータのクリーンアップを実行できるような有意義なデータ分割を維持しながら、処理を並列化できる設計を決定しました。

  * **RunInstance** ：パイプラインの1回の実行に対応するビジネスユニットに対応する最も細かい分類（1か月/日/1時間のデータなど）。
  * **パーティション** ：RunInstanceの分割で、外部状態なしに行データから決定論的かつ自明な方法で各行がパーティションに割り当てられるようにするため、再試行と偽装する必要がありません。（例：accountId範囲、10分間隔）
  * **バッチ** ：非決定的な利用傾向で、ストリーミング/パラレル処理のためにデータをより小さなチャンクに分割し、より少ないリソースで高速処理を実現するためにのみ使用されます。（例：1万行、50MB）



ユーザーがコンシューマーステージYAMLで設定するオプションは、ソースシステムからデータを取得するために使用されるクエリを構築し、また、システムに依存しない方法でこのデータ区分の意味をエンコードし、これが何であるかを後続のステージが理解できるようにします。データが表します。例えば、このパーティションには、すべてのアカウントID 0～500のデータが含まれます。これは、標的を絞ったデータクリーンアップを行い、たとえば、エラーにより1つのデータパーティションが再試行される場合、重複するデータエントリを回避できることを意味します。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2837 Image 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44GBYT52XJDX6Y4K3B7CF6.png&w=715&h=369&f=webp&fit=cover&position=center)

### フレームワークの実装

##### ステージ互換性のためのStandard内部状態

最も一般的なユースケースは、データベースから読み取り、Parquetフォーマットに変換、そしてオブジェクトストレージに保存するようなもので、これらのステップはそれぞれ別個の段階となります。**Jetflow** にオンボードされるユースケースが増えるにつれ、誰かが新しいステージを書いた場合、それが他のステージと互換性があることを確認しなければなりませんでした。出力フォーマットやターゲットシステムごとに新しいコードを書く必要があるような状況を生み出したり、異なるユースケースごとにカスタムパイプラインを構築することになりたくありません。

この問題を解決する方法は、ステージ抽出クラスに単一形式でのデータ出力のみを許可することです。つまり、ダウンストリームのステージがこのフォーマットをサポートしている限り、入出力フォーマットでは、パイプラインの残りの部分と互換性があります。これは今にしては当たり前のことのように思えますが、当初、私たちはカスタム型システムを作成し、ステージの相互運用性に苦労していたため、社内では苦痛な学びを経験しました。

この内部フォーマットには、メモリ内の列挙データフォーマットである[ _Arrow_](https://arrow.apache.org/) を使うことを選びました。この形式の主な利点は次のとおりです。

  * **Arrowエコシステム** ：現在、多くのデータプロジェクトがアウトプットフォーマットとしてArrowをサポートしています。つまり、新しいデータソースのために抽出ステージを書く場合、Arrow出力を生成するのはたいてい些細なことです。
  * **直列化のオーバーヘッドなし** ：これにより、最小限のオーバーヘッドで、マシンやプログラミング言語間でArrowデータを簡単に移動することができます。**Jetflow** は、ジョブコントローラーのインターフェイスを介して幅広いシステムで実行できる柔軟性を持つように最初から設計されており、データ転送のこの効率性により、分散実装を作成する際のパフォーマンス上の妥協が最小限に抑えられます。
  * **メモリ割り当てを避けるために、大きな固定サイズのバッチにメモリを確保する** ：Goはガベージコレクション（GC）言語であり、GCサイクルタイムはオブジェクトのサイズではなくオブジェクト数によって主に影響を受けるため、ヒープオブジェクトが少なくなり、CPUに費やされる時間が減少します合計サイズが同じであっても、大幅にガベージを収集しています。GCサイクル中にスキャンし、収集するオブジェクトの数は、割り当て数に応じて増加するため、各10列を持つ8192行がある場合、Arrowは10回の割り当てを行うだけで、ほとんどのドライバーは8192回の割り当てを行うだけです。行ごとに割り当てるため、Arrowでオブジェクトをより少なく、GCサイクルタイムを短縮できます。



##### 行を列に変換する

もう1つの重要なパフォーマンス最適化は、データの読み取りや処理時に発生するコンバージョンステップの数を減らすことでした。ほとんどのデータ取り込みのフレームワークは、内部的にはデータを行として表現します。当社の場合、データは主にParquet形式で書き込んでいます。これは列ベースです。列ベースのソース（例：ClickHouse（ほとんどのドライバーがRowBinary形式を受信します）、特定の言語実装のために行ベースのメモリ表現に変換するのは非効率的です。これをさらに行から列に変換し、Parquetファイルを書きます。これらのコンバージョンは、パフォーマンスに大きな影響を与えます。

**Jetflow** は、その代わりに、列ベースのソースからカラム形式（例：ClickHouse-native Blockフォーマット）でデータを読み取り、このデータをArrow列フォーマットにコピーします。解析ファイルは、矢印列から直接書き込まれます。このプロセスが簡素化されることで、パフォーマンスが向上します。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2837 Image 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47B0K4932GXQGBA82F563N.png&w=715&h=322&f=webp&fit=cover&position=center)

### 各パイプライン段階の書き込み

##### 導入事例：ClickHouse

**Jetflow** の最初のバージョンをテストした時、ClickHouseのアーキテクチャ上、ClickHouseはデータを受信するよりも読み取りが速いため、追加の接続を使用してもメリットがないことがわかりました。そうすれば、より最適化されたデータベースドライバーによって、その単一の接続を活かして、追加の接続を必要とせずに、毎秒はるかに大きな行数を読み取ることが可能になるはずです。

当初、カスタムデータベースドライバはClickHouse用に書かれていましたが、最終的には優れた[ _ch-go 低レベルライブラリ_](https://github.com/ClickHouse/ch-go)に切り替えられました。ch-goはカラムフォーマットでClickHouseから[ _ブロック_](https://clickhouse.com/docs/development/architecture#block)を直接読み取るものです。これは、標準的なGoドライバーと比較してパフォーマンスに多大な効果がありました。上記のフレームワーク最適化と組み合わせて、1つのClickHouse接続で、**毎秒数百万行を取り込みます** 。

学んだ貴重な教訓は、他のソフトウェアと同様に、利便性や一般的なユースケースのために、自分のものと一致しない可能性があるということです。ほとんどのデータベースドライバは、行の大量のバッチを読み取るために最適化されていない傾向があり、行ごとのオーバーヘッドが高いです。

##### 導入事例：Postgres

For Postgresには、優れた[ _jackc/pgx_](https://github.com/jackc/pgx)ドライバーを使用していますが、database/sql Scanインターフェースを使用する代わりに、各行の未加工バイトを直接受信し、Postgres OID（オブジェクト識別子）タイプごとにack/pgx内部スキャン関数を使用します。 .

Goのdatabase/sql Scanインターフェースは、リフレクションを使用して関数に渡される型を理解し、リフレクションを使用して、Postgresから受け取った列の値で各フィールドを設定します。典型的なシナリオでは、これは十分に高速で使いやすいのですが、パフォーマンスの点では、今回のユースケースには不十分です。[ _jackc/pgx_](https://github.com/jackc/pgx)ドライバは、次のPostgres行が要求されるたびに生成された行バイトを再利用するため、行ごとの割り当てはゼロになります。これにより、Jetflow内で高性能で低割り当てのコードを書くことができます。この設計により、メモリ使用量を非常に低く抑えながら、ほとんどのテーブルでPostgres接続ごとに毎秒**60万行** 近くの行を実現できます。

## まとめ

2025年7月初旬、同チームは**Jetflow** を通じて1日あたり**770億** 件のレコードを取り込んでいます。残りのジョブは**Jetflow** への移行が進んでおり、1日あたりの総取り込みレコード数は1410億レコードになります。このフレームワークにより、他の方法では不可能だったケースでテーブルを取り込むことが可能になり、また、少ない時間と少ないリソースで取り込みを実行できるため、大幅なコスト削減が実現しました。

将来的には、プロジェクトをオープンソース化する予定です。このようなツールの開発に取り組むことに興味がある方は、[ _https://www.cloudflare.com/careers/jobs/_](https://www.cloudflare.com/en-gb/careers/jobs/)で募集中の職種をご覧いただけます。

このページ

オンラインで議論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fbuilding-jetflow-a-framework-for-flexible-performant-data-pipelines-at-cloudflare%2F&t=Jetflow%E3%81%AE%E6%A7%8B%E7%AF%89%EF%BC%9ACloudflare%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8B%E6%9F%94%E8%BB%9F%E3%81%A7%E9%AB%98%E6%80%A7%E8%83%BD%E3%81%AA%E3%83%87%E3%83%BC%E3%82%BF%E3%83%91%E3%82%A4%E3%83%97%E3%83%A9%E3%82%A4%E3%83%B3%E3%81%AE%E3%83%95%E3%83%AC%E3%83%BC%E3%83%A0%E3%83%AF%E3%83%BC%E3%82%AF)[](https://x.com/intent/post?text=Jetflow%E3%81%AE%E6%A7%8B%E7%AF%89%EF%BC%9ACloudflare%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8B%E6%9F%94%E8%BB%9F%E3%81%A7%E9%AB%98%E6%80%A7%E8%83%BD%E3%81%AA%E3%83%87%E3%83%BC%E3%82%BF%E3%83%91%E3%82%A4%E3%83%97%E3%83%A9%E3%82%A4%E3%83%B3%E3%81%AE%E3%83%95%E3%83%AC%E3%83%BC%E3%83%A0%E3%83%AF%E3%83%BC%E3%82%AF&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fbuilding-jetflow-a-framework-for-flexible-performant-data-pipelines-at-cloudflare%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fbuilding-jetflow-a-framework-for-flexible-performant-data-pipelines-at-cloudflare%2F)[](https://bsky.app/intent/compose?text=Jetflow%E3%81%AE%E6%A7%8B%E7%AF%89%EF%BC%9ACloudflare%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8B%E6%9F%94%E8%BB%9F%E3%81%A7%E9%AB%98%E6%80%A7%E8%83%BD%E3%81%AA%E3%83%87%E3%83%BC%E3%82%BF%E3%83%91%E3%82%A4%E3%83%97%E3%83%A9%E3%82%A4%E3%83%B3%E3%81%AE%E3%83%95%E3%83%AC%E3%83%BC%E3%83%A0%E3%83%AF%E3%83%BC%E3%82%AF+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fbuilding-jetflow-a-framework-for-flexible-performant-data-pipelines-at-cloudflare%2F)[](https://mastodonshare.com/?text=Jetflow%E3%81%AE%E6%A7%8B%E7%AF%89%EF%BC%9ACloudflare%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8B%E6%9F%94%E8%BB%9F%E3%81%A7%E9%AB%98%E6%80%A7%E8%83%BD%E3%81%AA%E3%83%87%E3%83%BC%E3%82%BF%E3%83%91%E3%82%A4%E3%83%97%E3%83%A9%E3%82%A4%E3%83%B3%E3%81%AE%E3%83%95%E3%83%AC%E3%83%BC%E3%83%A0%E3%83%AF%E3%83%BC%E3%82%AF&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fbuilding-jetflow-a-framework-for-flexible-performant-data-pipelines-at-cloudflare%2F)[](https://www.threads.net/intent/post?text=Jetflow%E3%81%AE%E6%A7%8B%E7%AF%89%EF%BC%9ACloudflare%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8B%E6%9F%94%E8%BB%9F%E3%81%A7%E9%AB%98%E6%80%A7%E8%83%BD%E3%81%AA%E3%83%87%E3%83%BC%E3%82%BF%E3%83%91%E3%82%A4%E3%83%97%E3%83%A9%E3%82%A4%E3%83%B3%E3%81%AE%E3%83%95%E3%83%AC%E3%83%BC%E3%83%A0%E3%83%AF%E3%83%BC%E3%82%AF+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fbuilding-jetflow-a-framework-for-flexible-performant-data-pipelines-at-cloudflare%2F)

## 関連するタグ

[Go](https://blog.cloudflare.com/ja-jp/tag/go/)[エンジニアリング](https://blog.cloudflare.com/ja-jp/tag/engineering/)[データ](https://blog.cloudflare.com/ja-jp/tag/data/)[デザイン](https://blog.cloudflare.com/ja-jp/tag/design/)[パフォーマンス](https://blog.cloudflare.com/ja-jp/tag/performance/)

SNS をフォロー

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 新しい投稿のお知らせを受け取るように登録する

メールアドレス

また、あなたのメールアドレスを共有したりすることはございません。

登録する

ご購読ありがとうございます！受信箱を確認して登録してください。
