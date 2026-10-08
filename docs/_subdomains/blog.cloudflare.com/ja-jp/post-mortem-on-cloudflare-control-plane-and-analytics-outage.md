---
url: https://blog.cloudflare.com/ja-jp/post-mortem-on-cloudflare-control-plane-and-analytics-outage/
title: Cloudflare\u306e\u30b3\u30f3\u30c8\u30ed\u30fc\u30eb\u30d7\u30ec\u30fc\u30f3\u3068\u5206\u6790\u969c\u5bb3\u306b\u95a2\u3059\u308b\u4e8b\u5f8c | Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:39:46.962140+00:00
---

# Cloudflareのコントロールプレーンと分析障害に関する事後 | Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/post-mortem-on-cloudflare-control-plane-and-analytics-outage/

[ブログ](https://blog.cloudflare.com/ja-jp/)

[事後検証](https://blog.cloudflare.com/ja-jp/tag/post-mortem/)[障害](https://blog.cloudflare.com/ja-jp/tag/outage/)

2 タグタグを2件表示

  * 投稿タグ
  * [事後検証](https://blog.cloudflare.com/ja-jp/tag/post-mortem/)[障害](https://blog.cloudflare.com/ja-jp/tag/outage/)
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



[事後検証](https://blog.cloudflare.com/ja-jp/tag/post-mortem/)[障害](https://blog.cloudflare.com/ja-jp/tag/outage/)

2023年11月4日

# Cloudflareのコントロールプレーンと分析障害に関する事後

![Matthew Prince](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44KQ4Z9PY1TR0ERGW96HZR.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Matthew Prince](https://blog.cloudflare.com/ja-jp/author/matthew-prince/)

20分で読了

URLをコピー

この記事は以下でも利用可能です [English](https://blog.cloudflare.com/post-mortem-on-cloudflare-control-plane-and-analytics-outage/)、[Deutsch](https://blog.cloudflare.com/de-de/post-mortem-on-cloudflare-control-plane-and-analytics-outage/)、[Español](https://blog.cloudflare.com/es-es/post-mortem-on-cloudflare-control-plane-and-analytics-outage/)、[Français](https://blog.cloudflare.com/fr-fr/post-mortem-on-cloudflare-control-plane-and-analytics-outage/)、[한국어](https://blog.cloudflare.com/ko-kr/post-mortem-on-cloudflare-control-plane-and-analytics-outage/)、[繁體中文](https://blog.cloudflare.com/zh-tw/post-mortem-on-cloudflare-control-plane-and-analytics-outage/)、[简体中文](https://blog.cloudflare.com/zh-cn/post-mortem-on-cloudflare-control-plane-and-analytics-outage/)、[Português](https://blog.cloudflare.com/pt-br/post-mortem-on-cloudflare-control-plane-and-analytics-outage/).

![Post mortem on the Cloudflare Control Plane and Analytics Outage](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45FSBWC0D25T68JD98V477.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////+vz/8e/v7Obi7ujj8u3q8O7u6ent/////f7/8+7q7eLa7+Ta9Ozk8u/s7Ozt////////9u7n8ODT8uPT9+3h9vLs8fDv////////+/Lq9OPU9+bV/PLk/Pfw9vXz//////////ny++zf/e/h//rv//74/Pr5///////////+//fv//vy///9///////////////////////9////////////////////////////////////////////////)

2023年11月2日（木）11:43（UTC）より、Cloudflareのコントロールプレーンと分析サービスに障害が発生しました。Cloudflareのコントロールプレーンは、主にWebサイトやAPIを含むすべてのサービスに関するお客様向けインターフェースで構成されています。当社の分析サービスには、ロギングと分析レポートが含まれます。

このインシデントは11月2日11時44分（UTC）から11月4日4時25分（UTC）まで続きました。11月2日17時57分（UTC）の時点で、災害復旧施設にてコントロールプレーンの大部分を復旧することができました。多くのお客様は、災害復旧施設が稼働した後、ほとんどの製品でトラブルを経験しなかったと思われます。しかし、その他のサービスは復旧に時間がかかり、ご利用いただいたお客様の中には、インシデントが完全に解決するまで、問題が発生している可能性があります。当社の未加工ログサービスは、インシデントの間、ほとんどのお客様にご利用いただけませんでした。

現在、すべてのお客様に対して、サービスが復旧しています。このインシデントの間中、Cloudflareのネットワークとセキュリティサービスは期待どおりに機能し続けました。お客様がこれらのサービスに変更を加えることができない期間がありましたが、当社のネットワーク経由のトラフィックに影響はありませんでした。

この投稿では、このインシデントの原因となったイベント、このような問題を防ぐために当社が構築したアーキテクチャ、何が失敗し、何が機能したのか、そしてその理由、過去36時間で学んだことに基づいて行っている変更について概説します。

そもそも、こんなことはあってはならないことでした。 当社は、コアデータセンタープロバイダーのひとつが壊滅的な障害に見舞われた場合でも、高可用性システムを構築しているため、このような障害を食い止めることができたはずだと考えていました。設計どおりにオンライン状態を維持しているシステムも多かったのですが、一部の重要なシステムには、明らかでない依存関係により、利用できなくなってしまいました。このような事態を招き、お客様やチームに多大なご迷惑をおかけしたことをお詫びするとともに、情けなく思っております。

### 意図した設計

Cloudflareのコントロールプレーンと分析システムは、主にオレゴン州ヒルズボロ周辺の3つのデータセンターのサーバー上で稼働しています。3つのデータセンターは互いに独立しており、それぞれに複数の商用電源供給があり、複数の冗長かつ独立したネットワーク接続があります。

これらの施設は、自然災害が3つすべてに影響を与える可能性を最小限に抑える距離にあるように意図的に選択されましたが、すべての施設がアクティブ-アクティブ冗長化データクラスターを実行できる程度に十分近い距離にあります。これは、3つの施設間で継続的にデータを同期させていることを意味します。設計上、いずれかの施設がオフラインになっても、残りの施設は稼働し続けることができます。

これは4年前から実装しているシステム設計です。当社の重要なコントロールプレーンシステムのほとんどは高可用性クラスターに移行されていましたが、一部のサービス、特に一部の新製品については、まだ高可用性クラスターに追加されていませんでした。

さらに、当社のロギングシステムは、意図的に高可用性クラスターの一部ではありませんでした。その決定の論理は、ロギングはすでに分散された問題であり、ログはネットワークの端でキューに入れられ、その後オレゴン州のコア（またはロギングに地域サービスを使用しているお客様向けの別の地域施設）に送り返されるというものでした。ロギング施設がオフラインの場合、分析ログはオンラインに戻るまでネットワークの端でキューに入れられます。分析の遅延は許容できると判断しました。

### Flexentialデータセンターの停電

オレゴン州にある3つの施設のうち最大の施設は、Flexentialが運営しています。当社はこの施設を「PDX-DC04」と呼んでいます。Cloudflareは、PDX-04のスペースをリースしており、そこに当社最大の分析クラスターと高可用性クラスター用のマシンが3分の1を超え、収容されています。これは、高可用性クラスターにまだオンボードされていないサービスのデフォルトの場所でもあります。当社はこの施設の比較的大規模な顧客であり、その総容量の約10パーセントを消費しています。

11月2日8時50分（UTC）、PDX-04にサービスを提供している電力会社であるポートランドゼネラルエレクトリック（PGE）は、建物への独立した電源供給の1つに影響を与える予期せぬメンテナンスイベントが発生しました。このイベントにより、PDX-04への供給路が1本停止しました。データセンターには、施設に電力を供給できる、ある程度の独立性を備えた複数の供給路があります。しかし、Flexentialは、ダウンした供給路を効果的に補うために発電機をパワーアップしました。

ベストプラクティスに反して、FlexentialはCloudflareに発電機への電力供給に切り替えたことを通知しませんでした。どの可観測性ツールも、電源が変わったことを検出することはできませんでした。もしFlexentialが当社に知らせてくれていたら、当社はチームを立ち上げて施設を注意深く監視し、施設の障害が続く間に、その施設に依存していたコントロールプレーンサービスを別の場所に移動させることができたでしょう。

また、Flexentialが残り1つの電力供給路と発電機の両方を同時に実行したことも異常です。電力需要が高い場合、電力会社がデータセンターに対して送電網から切り離し、発電機のみで稼働するよう要請することは珍しいことではありません。Flexentialは、冗長ユニットを含め、全負荷時に施設をサポートできる発電機10台を稼働させています。また、Flexentialが残りの電力供給路からのみ施設を運営することも可能でした。なぜ商用電源と発電機の電源を使用したのか、明確な答えは得られていません。

### 次に何が起こったかについての情報に基づいた推測

この決定以降、Flexentialからは、根本的な原因や彼らの判断、またこの事象に関する明確な情報はまだ提供されていません。FlexentialおよびPGEから何が起こったのか、詳しい情報が入り次第、この記事を更新します。以下の内容の一部は、最も可能性の高い一連の事象と、個々のFlexential従業員が非公式に当社と共有した情報に基づいた推測です。

電力回線を動作したままにしていた可能性の一つは、FlexentialがPGEと呼ばれるプログラムの一部であったことです。DSGによって、地域の電力会社はデータセンターの発電機を動かし、送電網へ追加の電力供給を行うことができます。その代わり、発電会社は発電機のメンテナンスや燃料供給を支援しています。FlexentialがDSGプログラムについて当社に知らせた記録の場所は見つかりませんでした。当時、DSGはアクティブだったのかと尋ねましたが、回答は得られませんでした。それがFlexentialの決定に寄与したかどうかはわかりませんが、発電機が起動した後も電力回線がオンラインのままであった理由を説明することはできます。

11時40分頃（UTC）、PDX-04のPGE変圧器に地絡が発生しました。当社は、FlexentialやPGEから確認を取れていませんが、この変圧器が、データセンターに入るときにまだ稼働していた2番目の給電路のために、送電網から電源を降圧したものだと考えています。FlexentialやPGEに確認を取れていませんが、この地絡はPGEが行っていた予定外のメンテナンスが原因で、最初の給電路に影響が出たようです。あるいは、とても不運な偶然の一致だったのかもしれません。

高圧（12,470ボルト）送電線での地絡は非常に危険です。電気システムは、問題が発生した場合に損傷を防ぐため、即座に停止するように設計されています。残念ながら、この場合、保護措置により、PDX-04のすべての発電機も停止しました。これは、施設の2つの発電源—冗長な電力回線と10台の発電機の両方—がオフラインになったことを意味します。

幸いなことに、発電機に加え、PDX-04はUPSバッテリーバンクも備えられています。これらのバッテリーは、施設に約10分間電源を供給するのに十分だと考えられています。この時間は、停電してから発電機が自動的に起動するまでの時間を埋めるのに十分なはずです。Flexentialが10分以内に発電機または電力供給路を復旧できれば、中断することはありません。実際には、自社機器の不具合から観測したところ、バッテリーはわずか4分後に故障し始めました。そして、Flexentialが発電機を復旧させるのにかかった時間は10分をはるかに超えていました。

### 電源復旧の試み

正式な確認は取れていませんが、従業員から発電機のオンライン復帰を妨げている要因は、3つあると聞いています。まず、地絡によって回路が遮断されたため、物理的にアクセスし、手動で再起動する必要がありました。第二に、Flexentiaのアクセス制御システムはバッテリーバックアップから電力供給を受けていなかったため、オフライン状態でした。そして第三に、現場の夜間の人員配置には、操作に経験豊富、または電気の専門家がおりませんでした—夜勤シフトは警備員と、勤務してわずか1週間の技術者1人でした。

11時44分から12時1分（UTC）の間、発電機が完全に再起動していない状態で、UPSのバッテリーが切れ、データセンターのすべてのお客様が停電しました。この間、Flexentialは施設に問題があったことをCloudflareに一切知らせませんでした。データセンターの問題について最初に通知を受けたのは、施設を世界中に接続する2台のルーターが11時44分（UTC）にオフラインになったときでした。ルーターに直接、または帯域外管理で連絡が取れない場合は、Flexentialに連絡し、現地チームを派遣して施設に物理的に移動しました。Flexentialから当社へ、問題が発生しているという最初のメッセージは、12時28分（UTC）でした。

>  _現在、[PDX-04]の電源に問題が発生しています。この問題は、午前5時（PT）（12:00 UTC）頃に発生しました。エンジニアは問題を解決し、サービスを回復するために積極的に取り組んでいます。30分ごと、あるいは復旧予定時間に関する情報が入り次第、進捗状況をお知らせします。ご不憫おかけしますが、ご理解のほどよろしくお願いいたします。_

### データセンター・レベルの障害に対する設計

PDX-04の設計は建設前にTier IIIの認定を受けており、高い可用性SLAを提供することが期待されていますが、当社はオフラインになる可能性も想定しています。うまく運営されている施設でさえ、悪い日があります。当社は、そのための計画を立てました。この場合に予想されることは、分析がオフラインになり、ログがエッジでキューに入れられて遅延し、高可用性クラスターに統合されていない特定の優先度の低いサービスが、別の施設で復旧されるまで一時的にオフラインになることです。

この地域で稼働している他の2つのデータセンターが、高可用性クラスタの責任を引き継ぎ、重要なサービスをオンラインに維持します。一般的にはプランされたとおりに機能しました。残念なことに、高可用性クラスタに属するはずの一部のサービスが、PDX-04でのみ稼働しているサービスに依存していることが判明しました。

特に、ログを処理し、分析を強化する2つの重要なサービス—KafkaとClickHouse—は、PDX-04でのみ利用可能でしたが、これらのサービスに依存する他のサービスが高可用性クラスターで実行されていました。これらの依存関係はそれほど緊密ではなく、より柔軟にエラーを処理すべきであり、その依存関係を把握すべきでした。

他の2つのデータセンター施設をそれぞれ（および両方）完全にオフラインにして、高可用性クラスターのテストを実施しました。また、PDX-04の高可用性部分をオフラインにするテストも行いました。しかし、PDX-04の施設全体を完全にオフラインにしてテストしたことはありませんでした。その結果、データプレーンにおけるこれらの依存関係の重要性の一部を見落としていました。

また、新製品とそれに関連するデータベースの要件があまりにも緩すぎたため、高可用性クラスターと統合できませんでした。Cloudflareにより、複数のチームが迅速にイノベーションを起こすことができます。そのため、製品は初期アルファ版に向けてさまざまな経路を取ることがよくあります。時間の経過とともに、これらのサービスのバックエンドを当社のベストプラクティスに移行させるのが当社の慣行ですが、製品が一般に利用可能（GA）と宣言される前に、その移行を正式に要求することはありませんでした。それは、当社が導入した冗長保護が製品によっては一貫して機能しないことを意味するため、間違いでした。

さらに、当社のサービスの多くはコア施設の可用性に依存しています。これは多くのソフトウェアサービスを作成する方法ですが、Cloudflareの強みを生かすことはできません。当社は分散システムを得意としています。このインシデントの間、当社のグローバルネットワークは期待どおりに機能し続けました。当社の製品や機能の中には、コアを必要とせずにネットワークのエッジを介して構成および保守できるものもありますが、コアが利用できない場合、現在、あまりにも多くの障害が発生しています。当社は、すべてのお客様に提供している分散システム製品をすべてのサービスに使用する必要があるため、コア施設が中断された場合でも、分散システム製品はほぼ通常どおり機能し続けます。

### 災害復旧

12時48分（UTC）、Flexentialは発電機を再起動させることができました。施設の一部に電源が戻りました。システムに負荷がかからないように、データセンターの電源が復旧するときは、通常、一度に1つの回路への電源供給を徐々に再開します。住宅の回路ブレーカーと同様に、それぞれのお客様は冗長ブレーカーでサービスを受けます。FlexentialがCloudflareの回路に電源を供給しようとしたところ、サーキットブレーカーに欠陥があることが判明しました。ブレーカーが地絡やインシデントの結果としてその他のサージによって故障したのか、あるいは以前から故障していて電源を切った後に初めてブレーカーが故障したのかはわかりません。

Flexentialは、故障したブレーカーの交換プロセスを開始しました。そのため、施設内の手元にあるブレーカーよりも多くのブレーカーが不良品であったため、新しいブレーカーを調達する必要がありました。予想以上に多くのサービスがオフラインになり、Flexentialではサービスを復旧する時間を伝えることができなかったため、13時40分（UTC）にヨーロッパにあるCloudflareの災害復旧サイトにフェイルオーバーするよう電話をかけました。ありがたいことに、Cloudflareの全体的なコントロールプレーンのほんの一部をフェイルオーバーするだけで済みました。当社のサービスのほとんどは、2つのアクティブなコアデータセンター間の高可用性システム全体で引き続き実行されました。

当社は13時43分（UTC）に災害復旧サイトで最初のサービスを開始しました。Cloudflareの災害復旧サイトは、災害時に重要なコントロールプレーンサービスを提供します。災害復旧サイトは、ログ処理サービスの一部をサポートしていませんが、コントロールプレーンの他の部分をサポートするように設計されています。

そこでサービスが開始された際、API呼び出しの失敗が、当社のサービスに大打撃を与え、非常に深刻な問題を引き起こしました。リクエスト量を制御するためにレート制限を実装しました。この期間中、ダッシュボードやAPIを使用して変更を加える際に、ほとんどの製品のお客様に、断続的なエラーが発生していました。17時57分（UTC）までに、災害復旧サイトへの移行に成功したサービスは安定し、ほとんどのお客様は直接影響を受けることはなくなりました。しかし、一部のシステム（例：Magic WAN）は依然として手動設定が必要であり、主にログ処理と一部の特注APIに関連するその他のサービスは、PDX-04の復旧が完了するまで利用できない状態が続きました。

### 一部の製品および機能の再起動が遅延

当社の災害復旧サイトで適切に立ち上げられなかった製品は、わずかでした。適切に立ち上げられなかった製品は、災害復旧手順が完全に実装およびテストされていない新しい製品の傾向がありました。その中には、新しい動画をアップロードするためのStreamサービスやその他のサービスが含まれていました。当社のチームは、これらのサービスを復旧させるために2つの同時作業を行いました。1）災害復旧サイトで再実装すること。2）それらを高可用性クラスターに移行すること。

Flexentialは故障したサーキットブレーカーを交換し、両方の電力供給路を復旧し、22時48分（UTC）にクリーンな電力を確認しました。当社のチームは全員が総力を挙げて緊急対応に一日中取り組んでいました。そのため、私はほとんどのメンバーが少し休息をとり、午前中にPDX-04に戻り、開始するという決断を下しました。この決断により完全な回復は遅れましたが、さらなるミスでこの状況を悪化させる可能性は低くなったと思います。

11月3日の朝一番から、当社のチームはPDX-04のサービスの復旧を開始しました。それは、ネットワーク関連機器を物理的に起動することから始め、次に数千台のサーバーの電源を入れてサービスを復元しました。インシデントの間、複数回の電源サイクルが発生した可能性が高いと考えられたため、データセンター内のサービスの状態は不明でした。復旧するための唯一の安全なプロセスは、施設全体の完全なブートストラップに従うことでした。

これには、施設の復旧を開始するために構成管理サーバーをオンラインにする手動プロセスが含まれていました。これらの再構築には3時間かかりました。そこから、当社のチームは、残りのサーバーがサービスに電力を供給するための再構築をブートストラップすることができました。各サーバーが再構築するのに、10分から2時間かかりました。これを複数のサーバー間で並行して実行することはできましたが、サービス間には固有の依存関係があり、一部のサービスを順次オンラインに戻す必要がありました。

2023年11月4日午前4時25分（UTC）現在、サービスは完全に復旧しています。ほとんどのお客様にとって、ヨーロッパのコアデータセンターにも分析を保存しているため、ダッシュボードとAPI全体のほとんどの分析でデータの損失は見られません。しかし、EUで複製されていない一部のデータセットには、永続的なギャップがあります。ログプッシュ機能を使用しているお客様の場合、イベントの大部分でログが処理されないため、受信しなかったものは復元されません。

### 教訓と改善策

Flexentialから回答が必要な質問が多数あります。しかし、データセンター全体が故障する可能性も想定しなければなりません。Googleには、重大なイベントや危機が発生した場合に、コードイエローまたはコードレッドを呼び出すことができるプロセスがあります。このような場合、エンジニアリングリソースのほとんどまたはすべてが、目前の問題の処理にシフトされます。

過去にはそのようなプロセスはありませんでしたが、現在では、コードオレンジというバージョンがあり、自身で実装する必要があることは明らかです。当社は、重要でないエンジニアリング機能をすべて、コントロールプレーンの高い信頼性の確保に重点を置くことにシフトしています。その一環として、以下の変更を予定しています：

  * すべてのサービスのコントロールプレーン構成をコアデータセンターに依存することをやめ、分散ネットワークから最初に電源供給される場所にコントロールプレーン構成を移動します
  * すべてのコアデータセンターがオフラインであっても、ネットワーク上で実行されているコントロールプレーンが機能し続けることを確認します
  * 一般提供に指定されているすべての製品と機能は、特定の施設にソフトウェアを依存させることなく、高可用性クラスターに依存する必要があります（コアデータセンターいずれかに依存する場合）
  * 一般提供に指定されているすべての製品と機能には、テスト済みの信頼性の高い災害復旧プランが必要です
  * システム障害の影響範囲をテストし、障害の影響を受けるサービスの数を最小限に抑えます
  * 各コアデータセンター施設の完全な撤去を含め、すべてのデータセンター機能に対してより厳格なカオステストを実施します
  * すべてのコアデータセンターの徹底的な監査と、それらが当社の基準に準拠していることを確認するための再監査プラン
  * すべてのコア施設に障害が発生した場合でも、ログがドロップされないようにするロギングおよび分析の災害復旧プラン



先ほど申し上げたように、このような事態を招き、お客様やチームに多大なご迷惑をおかけしたことをお詫びするとともに、情けなく思っております。当社は、データセンタープロバイダーで発生した連鎖的な一連の障害にも耐えられる適切なシステムと手順を構築していますが、それらに従い、未知の依存関係をテストすることをより厳格に実施する必要があります。これには私も大変注目しており、今年の残り期間を通じてチームの大部分が注目することになるでしょう。そして、ここ数日の痛みがより成長させてくれるでしょう。

このページ

オンラインで議論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fpost-mortem-on-cloudflare-control-plane-and-analytics-outage%2F&t=Cloudflare%E3%81%AE%E3%82%B3%E3%83%B3%E3%83%88%E3%83%AD%E3%83%BC%E3%83%AB%E3%83%97%E3%83%AC%E3%83%BC%E3%83%B3%E3%81%A8%E5%88%86%E6%9E%90%E9%9A%9C%E5%AE%B3%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E4%BA%8B%E5%BE%8C)[](https://x.com/intent/post?text=Cloudflare%E3%81%AE%E3%82%B3%E3%83%B3%E3%83%88%E3%83%AD%E3%83%BC%E3%83%AB%E3%83%97%E3%83%AC%E3%83%BC%E3%83%B3%E3%81%A8%E5%88%86%E6%9E%90%E9%9A%9C%E5%AE%B3%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E4%BA%8B%E5%BE%8C&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fpost-mortem-on-cloudflare-control-plane-and-analytics-outage%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fpost-mortem-on-cloudflare-control-plane-and-analytics-outage%2F)[](https://bsky.app/intent/compose?text=Cloudflare%E3%81%AE%E3%82%B3%E3%83%B3%E3%83%88%E3%83%AD%E3%83%BC%E3%83%AB%E3%83%97%E3%83%AC%E3%83%BC%E3%83%B3%E3%81%A8%E5%88%86%E6%9E%90%E9%9A%9C%E5%AE%B3%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E4%BA%8B%E5%BE%8C+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fpost-mortem-on-cloudflare-control-plane-and-analytics-outage%2F)[](https://mastodonshare.com/?text=Cloudflare%E3%81%AE%E3%82%B3%E3%83%B3%E3%83%88%E3%83%AD%E3%83%BC%E3%83%AB%E3%83%97%E3%83%AC%E3%83%BC%E3%83%B3%E3%81%A8%E5%88%86%E6%9E%90%E9%9A%9C%E5%AE%B3%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E4%BA%8B%E5%BE%8C&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fpost-mortem-on-cloudflare-control-plane-and-analytics-outage%2F)[](https://www.threads.net/intent/post?text=Cloudflare%E3%81%AE%E3%82%B3%E3%83%B3%E3%83%88%E3%83%AD%E3%83%BC%E3%83%AB%E3%83%97%E3%83%AC%E3%83%BC%E3%83%B3%E3%81%A8%E5%88%86%E6%9E%90%E9%9A%9C%E5%AE%B3%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E4%BA%8B%E5%BE%8C+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fpost-mortem-on-cloudflare-control-plane-and-analytics-outage%2F)

## 関連するタグ

[事後検証](https://blog.cloudflare.com/ja-jp/tag/post-mortem/)[障害](https://blog.cloudflare.com/ja-jp/tag/outage/)

SNS をフォロー

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 新しい投稿のお知らせを受け取るように登録する

メールアドレス

また、あなたのメールアドレスを共有したりすることはございません。

登録する

ご購読ありがとうございます！受信箱を確認して登録してください。
