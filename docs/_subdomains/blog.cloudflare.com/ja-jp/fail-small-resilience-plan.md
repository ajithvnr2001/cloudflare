---
url: https://blog.cloudflare.com/ja-jp/fail-small-resilience-plan/
title: \u30b3\u30fc\u30c9\u30aa\u30ec\u30f3\u30b8\uff1a\u30d5\u30a7\u30a4\u30eb\u30b9\u30e2\u30fc\u30eb \u2014 \u6700\u8fd1\u306e\u30a4\u30f3\u30b7\u30c7\u30f3\u30c8\u767a\u751f\u5f8c\u306e\u5f53\u793e\u306e\u30ec\u30b8\u30ea\u30a8\u30f3\u30b9\u8a08\u753b | Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:38:41.335685+00:00
---

# コードオレンジ：フェイルスモール — 最近のインシデント発生後の当社のレジリエンス計画 | Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/fail-small-resilience-plan/

[ブログ](https://blog.cloudflare.com/ja-jp/)

[コードオレンジ](https://blog.cloudflare.com/ja-jp/tag/code-orange/)[事後検証](https://blog.cloudflare.com/ja-jp/tag/post-mortem/)[障害](https://blog.cloudflare.com/ja-jp/tag/outage/)

3 タグタグを3件表示

  * 投稿タグ
  * [コードオレンジ](https://blog.cloudflare.com/ja-jp/tag/code-orange/)[事後検証](https://blog.cloudflare.com/ja-jp/tag/post-mortem/)[障害](https://blog.cloudflare.com/ja-jp/tag/outage/)
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



[コードオレンジ](https://blog.cloudflare.com/ja-jp/tag/code-orange/)[事後検証](https://blog.cloudflare.com/ja-jp/tag/post-mortem/)[障害](https://blog.cloudflare.com/ja-jp/tag/outage/)

2025年12月19日

# コードオレンジ：フェイルスモール — 最近のインシデント発生後の当社のレジリエンス計画

![Dane Knecht](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45BN3R68K90TS6F0H9P7YQ.png&w=64&h=64&f=webp&fit=cover&position=center)

[Dane Knecht](https://blog.cloudflare.com/ja-jp/author/dane-knecht/)

13分で読了

URLをコピー

この記事は以下でも利用可能です [English](https://blog.cloudflare.com/fail-small-resilience-plan/)、[Deutsch](https://blog.cloudflare.com/de-de/fail-small-resilience-plan/)、[Español (Latinoamérica)](https://blog.cloudflare.com/es-la/fail-small-resilience-plan/)、[Français](https://blog.cloudflare.com/fr-fr/fail-small-resilience-plan/)、[한국어](https://blog.cloudflare.com/ko-kr/fail-small-resilience-plan/)、[繁體中文](https://blog.cloudflare.com/zh-tw/fail-small-resilience-plan/)、[简体中文](https://blog.cloudflare.com/zh-cn/fail-small-resilience-plan/)、[Português](https://blog.cloudflare.com/pt-br/fail-small-resilience-plan/).

![BLOG-3079 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46GNZJ7D2BGC4T3BKJ7HHJ.png&w=1800&h=1013&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///////97/Hz4+nu5ezy7fL28fLz7uvp////////6+713OPv3Obz5u346+706unr////////6e341uDy1eH13+n65+346Onv////////6/D92OL21uP64Ov/6e/86+30////////8/j/4uv84ez/6/T/8vf/8/T5/////////v//8Pf/8fn/+f///v///fz+/////////////P///v//////////////////////////////////////////////)

[_2025年11月18日_](https://blog.cloudflare.com/18-november-2025-outage/)、Cloudflareのネットワークは、約2時間10分にわたり、ネットワークトラフィックの配信に重大な障害を経験しました。約3週間後の[ _2025年12月5日_](https://blog.cloudflare.com/5-december-2025-outage/)、当社のネットワークは再度、ネットワークに接続されたアプリケーションの28%に対し、約25分間トラフィックを処理できませんでした。

2件のインシデントに関し、詳細な事後分析ブログ記事を公開いたしましたが、お客様からの信頼回復のため、更なる努力が必要であると認識しています。本日、このような障害の再発防止のため、Cloudflareで進行中の取り組みについて詳しくご紹介します。

当社は、このプランを「**コードオレンジ：フェイルスモール** 」と呼んでいます。これは、大規模な障害につながる可能性のあるエラーや間違いに対するネットワークのレジリエンスを高めるという目標を反映したものです。「コードオレンジ」とは、このプロジェクトの作業が何よりも優先されるという意味です。背景として、Cloudflareは[ _以前にも一度_](https://blog.cloudflare.com/major-data-center-power-failure-again-cloudflare-code-orange-tested/)「コードオレンジ」を発令したことがあります。これは、全社を挙げて最優先で対応すべき別の大規模なインシデントが発生した後のことでした。最近の出来事についても、同様の取り組みが必要があると考えます。コードオレンジとは、それを実現するための手段であり、チームが必要に応じて部門横断的に連携して業務を遂行し、他の作業を一時停止できるようにするものです。

コードオレンジ作業の主要な3つの分野：

  * ソフトウェアバイナリのリリースに対して現在行っているように、ネットワークに伝播されるすべての構成変更に対して、制御されたロールアウトを要求します。
  * ネットワークトラフィックを処理するすべてのシステムの障害モードをレビュー、改善、テストし、予期しないエラー状態を含む、すべての条件下で明確に定義された動作を示すことを確認します。
  * 社内の「ブレイクグラス」*手順を変更し、循環依存関係を解消することで、インシデント発生時に弊社とお客様が迅速に行動し、問題なくすべてのシステムにアクセスできるようにします。



これらのプロジェクトは、完了時に「ビッグバン」型の変更を一度に行うのではなく、進行に伴い反復的な改善を実現します。個々の更新は、Cloudflareのより高いレジリエンスに貢献します。最終的には、過去2か月間に発生した世界的インシデントの原因となった問題などを含め、Cloudflareのネットワークのレジリエンスが大幅に向上すると見ています。

これらのインシデントがお客様とインターネット全体にとって苦痛であることを理解しております。当社はこのことを非常に心苦しく思っており、この取り組みをCloudflare全員にとっての最優先事項といたしました。

 _***** Cloudflareのブレークグラス手順では、特定の状況下において、特定の個人が権限を昇格させ、重大なシナリオを解決するために緊急措置を実行できます。_

## 何が問題だったのでしょうか？

最初のインシデントでは、Cloudflareの顧客サイトにアクセスしたユーザーに、Cloudflareがリクエストに応答できないことを示すエラーページが表示されました。2つ目は、空白のページでした。

どちらの障害も同様のパターンでした。各インシデントが発生する直前に、当社は瞬時に世界数百都市のデータセンターにおいて構成変更をデプロイしました。

11月の変更は、ボット管理分類子の自動更新として自動的に行われました。当社は、ネットワークを流れるトラフィックから学習する様々な人工知能モデルを実行し、ボットを識別する検出機能を構築しています。これらのシステムは、常に更新され、セキュリティ保護を回避してお客様のサイトに到達しようとする悪意のある行為者に先手を打っています。

12月のインシデントにおいて、一般的なオープンソースフレームワークであるReactの脆弱性からお客様を保護する目的で、セキュリティアナリストが使用するセキュリティツールに変更をデプロイし、署名の改善を図りました。新しいボット管理更新の重要性と同様に、脆弱性を悪用しようとする攻撃者よりも先に行動する必要がありました。その変更がインシデントの開始の引き金となりました。

このパターンは、Cloudflareにおける構成変更のデプロイ方法と、ソフトウェア更新のリリース方法との間に、重大な隔たりがあることを明らかにしました。ソフトウェアのバージョン更新をリリースする際は、管理および監視された方法で実行します。デプロイメントは、新しいバイナリリリースごとに、グローバルトラフィックを処理できるようになる前に、複数のゲートを正常に完了する必要があります。まず従業員のトラフィックにデプロイし、その後、無料ユーザーから開始し、世界中のお客様に対して段階的に変更を適用していきます。いずれかの段階で異常が検出された場合、人手を介さずにリリースを元に戻すことができます。

その方法論は、構成の変更には適用されていません。ネットワークを支えるコアソフトウェアのリリースとは異なり、構成変更を行う場合、ソフトウェアの動作方法の値を変更することになり、即座に実行できます。この機能はお客様にも提供されています。Cloudflareで設定を変更すると、変更内容は数秒で世界中に反映されます。

そのスピードにはメリットがあるとはいえ、対処が必要なリスクも伴います。過去2件のインシデントから、ネットワークにおけるトラフィックの処理方法に適用される変更は、ソフトウェア自体の変更に適用するのと同等の、テスト済みの慎重さをもって扱う必要があることが示されました。

## Cloudflareは、構成更新のデプロイ方法を刷新します

両インシデントに共通する本質的な要因として、設定変更が数秒でグローバルにデプロイされるという能力が挙げられます。どちらの事象においても、誤った構成によってネットワークは数秒で停止してしまいました。

ソフトウェアリリースで** _既に実施_** しているように、構成の段階的導入を導入することが、コードオレンジ計画における最重要の作業領域です。

Cloudflareの構成変更は、非常に迅速にネットワークに反映されます。ユーザーが新しいDNSレコードを作成するか、新しいセキュリティルールを作成すると、数秒以内にネットワーク上のサーバーの90%に到達します。これは、社内でQuicksilverと呼んでいるソフトウェアコンポーネントによって実現されています。

Quicksilverは、社内チームが必要とする構成変更にも使用されます。そのスピードは、当社のネットワークの動作を非常にすばやく反応してグローバルに更新することができる点です。しかし、どちらのインシデントでも、これにより破壊的変更がテストのためにゲートを通過するよりもむしろ、数秒でネットワーク全体に伝播しました。

ネットワークへの変更をほぼ瞬時にデプロイできる機能は多くの場合に役立ちますが、必須となるケースは稀です。現在、Quicksilver内で構成変更に対して管理されたデプロイメントを導入することで、コードと同様に構成を扱うための作業が進行中です。

当社では、Health Mediated Deployments（HMD）システムを通じて、1日に複数回、ネットワークにソフトウェア更新をリリースしています。このフレームワークにおいて、サービス（ネットワークにデプロイされたソフトウェア）を所有するCloudflareの各チームは、デプロイメントの成否を示す指標、ロールアウト計画、および失敗した場合の対応策を定義する必要があります。

サービスによって変数は若干異なります。別のデータセンターに移動する前に長い待ち時間が必要となる人もいれば、誤検出シグナルが発生した場合でも、エラー率に対する許容度が低い人もいます。

デプロイされると、当社のHMDツールキットは、各ステップを監視しながら、計画に沿って慎重に進行を開始します。いずれかのステップが失敗した場合、ロールバックが自動的に開始され、必要に応じてチームに通知されます。

コードオレンジ終了までに、構成更新も同様のプロセスに従います。これにより、過去の2件のインシデントで発生したような問題を、広範囲に拡大する前に迅速に発見できるようになると期待されます。

## サービス間の障害モードにどのように対処するか？

構成変更の管理を強化することで、インシデントが発生する前に多くの問題を捕捉できると期待していますが、ミスは起こり得るものと認識しています。どちらのインシデントでも、当社のネットワークのある部分におけるエラーが、お客様がCloudflareの利用方法を設定するために使用するコントロールプレーンを含め、当社の技術スタックの大部分で問題となりました。

地理的な拡大（より多くのデータセンターへの展開）や対象者（従業員や顧客タイプ）の拡大といった観点だけでなく、慎重かつ段階的なロールアウトについて検討する必要があります。また、サービスプログレッションによる障害（ボット管理サービスのようなある製品から、ダッシュボードのような関連性のない製品への拡散など）を含む、より安全なデプロイメントを計画する必要があります。

そのために、当社は、当社ネットワークを構成するすべての重要な製品とサービス間のインターフェース契約を見直しを行っております。これにより、a) 各インターフェース間で**障害発生を前提とする** こと、b) その障害を**可能な限り最も合理的な方法** で処理することを確実にするのです。 

ボット管理サービスの障害についてですが、少なくとも2つの重要なインターフェースがあり、そこで障害が発生することを想定していれば、お客様に影響が及ばない程度まで適切に対処できたはずです。1つ目は、破損した構成ファイルを読み取るインターフェースにありました。パニックに陥るのではなく、トラフィックがネットワークを通過できるようにする、検証済みの適切なデフォルト設定を用意すべきでした。そうすれば、最悪の場合でも、ボット検出の機械学習モデルに供給されるリアルタイムの微調整機能を失うだけで済んだはずです。  
  
2番目のインターフェースは、当社のネットワークを実行するコアソフトウェアとボット管理モジュール自体の間にありました。ボット管理モジュールが故障した場合（発生したように）、デフォルトでトラフィックをドロップすべきではありませんでした。その代わりに、通過できる分類でトラフィックを許可するという、より控えめなデフォルトを考えることもできました。

## 緊急事態に、どうすればより迅速に対応できるか？

インシデント発生時に、問題の解決に時間がかかりすぎました。いずれの場合も、セキュリティシステムが原因で、チームメンバーが問題解決に必要なツールにアクセスできなくなったこと、また、一部の内部システムが利用できなくなったことで、循環的な依存関係が発生し、遅延が発生しました。

セキュリティ企業として、当社のすべてのツールは、顧客データの安全を確保し、不正アクセスを防止するために、きめ細かいアクセス制御を備えた認証レイヤーによって保護されています。これは正しいことではあるものの、同時に、スピードが最優先事項であったにもかかわらず、現行のプロセスとシステムが対応を遅らせてしまったのです。

循環依存も顧客体験に影響しました。例えば、11月18日のインシデントの際、当社のNo CAPTCHAボットソリューションであるTurnstileが利用できなくなりました。CloudflareダッシュボードのログインフローでTurnstileを使用しているため、有効なセッションまたはAPIサービストークンを持たないお客様は、重大な変更を行う必要に迫られた際にCloudflareにログインできませんでした。

当社のチームは、緊急時における適切なツールへの迅速なアクセスを確保しつつ、セキュリティ要件を維持するため、すべてのブレイクグラス手順と技術の見直しおよび改善を行います。これには、循環依存関係の見直しと削除、またはインシデント発生時に迅速に「バイパス」できるようにすることが含まれます。また、訓練の頻度を増やし、将来起こりうる災害シナリオに先立ち、全チームがプロセスを十分に理解できるようにします。

## いつ完了しますか？

この記事は、社内で行われているすべての作業を網羅しているわけではありませんが、上記のワークストリームは、チームが注力すべき最優先事項を示しています。これらのワークストリームはそれぞれ、Cloudflareのほぼすべての製品およびエンジニアリングチームに影響を与える詳細な計画に対応しています。まだまだ、やることがたくさんあります。

第1四半期終了日までに、そしてそれよりもずっと前に、以下を行います。

  * すべての運用システムが、構成管理のためにHealth Mediated Deployments（HMD）によって確実にカバーされているようにする。
  * 各製品セットに応じて適切な故障モードに準拠するように、システムを更新する。
  * 緊急時に適切な担当者が適切な修復を提供できるよう、適切なプロセスを整備する。



これらの目標の中には、恒久的に継続するものがあります。新しいソフトウェアをリリースする際には、常に循環依存関係をより適切に処理する必要があります。また、当社のセキュリティ技術の経時的な変化を反映するために、緊急避難手順を更新する必要があります。

過去2回のインシデントにおいて、当社はユーザーとインターネット全体に対し、ご迷惑をかけてしまいました。やるべき対応がまだあります。この作業の進捗に伴い、最新情報を共有していきます。また、お客様やパートナーから受け取った質問やフィードバックに感謝いたします。

このページ

オンラインで議論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Ffail-small-resilience-plan%2F&t=%E3%82%B3%E3%83%BC%E3%83%89%E3%82%AA%E3%83%AC%E3%83%B3%E3%82%B8%EF%BC%9A%E3%83%95%E3%82%A7%E3%82%A4%E3%83%AB%E3%82%B9%E3%83%A2%E3%83%BC%E3%83%AB%20%E2%80%94%20%E6%9C%80%E8%BF%91%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B7%E3%83%87%E3%83%B3%E3%83%88%E7%99%BA%E7%94%9F%E5%BE%8C%E3%81%AE%E5%BD%93%E7%A4%BE%E3%81%AE%E3%83%AC%E3%82%B8%E3%83%AA%E3%82%A8%E3%83%B3%E3%82%B9%E8%A8%88%E7%94%BB)[](https://x.com/intent/post?text=%E3%82%B3%E3%83%BC%E3%83%89%E3%82%AA%E3%83%AC%E3%83%B3%E3%82%B8%EF%BC%9A%E3%83%95%E3%82%A7%E3%82%A4%E3%83%AB%E3%82%B9%E3%83%A2%E3%83%BC%E3%83%AB+%E2%80%94+%E6%9C%80%E8%BF%91%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B7%E3%83%87%E3%83%B3%E3%83%88%E7%99%BA%E7%94%9F%E5%BE%8C%E3%81%AE%E5%BD%93%E7%A4%BE%E3%81%AE%E3%83%AC%E3%82%B8%E3%83%AA%E3%82%A8%E3%83%B3%E3%82%B9%E8%A8%88%E7%94%BB&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Ffail-small-resilience-plan%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Ffail-small-resilience-plan%2F)[](https://bsky.app/intent/compose?text=%E3%82%B3%E3%83%BC%E3%83%89%E3%82%AA%E3%83%AC%E3%83%B3%E3%82%B8%EF%BC%9A%E3%83%95%E3%82%A7%E3%82%A4%E3%83%AB%E3%82%B9%E3%83%A2%E3%83%BC%E3%83%AB+%E2%80%94+%E6%9C%80%E8%BF%91%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B7%E3%83%87%E3%83%B3%E3%83%88%E7%99%BA%E7%94%9F%E5%BE%8C%E3%81%AE%E5%BD%93%E7%A4%BE%E3%81%AE%E3%83%AC%E3%82%B8%E3%83%AA%E3%82%A8%E3%83%B3%E3%82%B9%E8%A8%88%E7%94%BB+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Ffail-small-resilience-plan%2F)[](https://mastodonshare.com/?text=%E3%82%B3%E3%83%BC%E3%83%89%E3%82%AA%E3%83%AC%E3%83%B3%E3%82%B8%EF%BC%9A%E3%83%95%E3%82%A7%E3%82%A4%E3%83%AB%E3%82%B9%E3%83%A2%E3%83%BC%E3%83%AB+%E2%80%94+%E6%9C%80%E8%BF%91%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B7%E3%83%87%E3%83%B3%E3%83%88%E7%99%BA%E7%94%9F%E5%BE%8C%E3%81%AE%E5%BD%93%E7%A4%BE%E3%81%AE%E3%83%AC%E3%82%B8%E3%83%AA%E3%82%A8%E3%83%B3%E3%82%B9%E8%A8%88%E7%94%BB&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Ffail-small-resilience-plan%2F)[](https://www.threads.net/intent/post?text=%E3%82%B3%E3%83%BC%E3%83%89%E3%82%AA%E3%83%AC%E3%83%B3%E3%82%B8%EF%BC%9A%E3%83%95%E3%82%A7%E3%82%A4%E3%83%AB%E3%82%B9%E3%83%A2%E3%83%BC%E3%83%AB+%E2%80%94+%E6%9C%80%E8%BF%91%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B7%E3%83%87%E3%83%B3%E3%83%88%E7%99%BA%E7%94%9F%E5%BE%8C%E3%81%AE%E5%BD%93%E7%A4%BE%E3%81%AE%E3%83%AC%E3%82%B8%E3%83%AA%E3%82%A8%E3%83%B3%E3%82%B9%E8%A8%88%E7%94%BB+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Ffail-small-resilience-plan%2F)

## 関連するタグ

[コードオレンジ](https://blog.cloudflare.com/ja-jp/tag/code-orange/)[事後検証](https://blog.cloudflare.com/ja-jp/tag/post-mortem/)[障害](https://blog.cloudflare.com/ja-jp/tag/outage/)

SNS をフォロー

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 新しい投稿のお知らせを受け取るように登録する

メールアドレス

また、あなたのメールアドレスを共有したりすることはございません。

登録する

ご購読ありがとうございます！受信箱を確認して登録してください。
