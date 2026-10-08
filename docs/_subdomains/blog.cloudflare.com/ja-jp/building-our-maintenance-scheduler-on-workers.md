---
url: https://blog.cloudflare.com/ja-jp/building-our-maintenance-scheduler-on-workers/
title: Workers\u304c\u793e\u5185\u30e1\u30f3\u30c6\u30ca\u30f3\u30b9\u30b9\u30b1\u30b8\u30e5\u30fc\u30eb\u30d1\u30a4\u30d7\u30e9\u30a4\u30f3\u3092\u5f37\u5316\u3059\u308b\u65b9\u6cd5 | Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:45:15.066087+00:00
---

# Workersが社内メンテナンススケジュールパイプラインを強化する方法 | Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/building-our-maintenance-scheduler-on-workers/

[ブログ](https://blog.cloudflare.com/ja-jp/)

[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[Prometheus](https://blog.cloudflare.com/ja-jp/tag/prometheus/)[インフラストラクチャ](https://blog.cloudflare.com/ja-jp/tag/infrastructure/)1件1件タグを表示

4 タグタグを4件表示

  * 投稿タグ
  * [Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[Prometheus](https://blog.cloudflare.com/ja-jp/tag/prometheus/)[インフラストラクチャ](https://blog.cloudflare.com/ja-jp/tag/infrastructure/)[信頼性](https://blog.cloudflare.com/ja-jp/tag/reliability/)
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



[信頼性](https://blog.cloudflare.com/ja-jp/tag/reliability/)

[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[Prometheus](https://blog.cloudflare.com/ja-jp/tag/prometheus/)[インフラストラクチャ](https://blog.cloudflare.com/ja-jp/tag/infrastructure/)[信頼性](https://blog.cloudflare.com/ja-jp/tag/reliability/)

2025年12月22日

# Workersが社内メンテナンススケジュールパイプラインを強化する方法

![Kevin Deems](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DYXVM2ZEP0CAPVRVBRSS.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Michael Hoffmann](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46FZ19DMV4JVQ1GXNF27JJ.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Kevin Deems](https://blog.cloudflare.com/ja-jp/author/kevin-deems/)、[Michael Hoffmann](https://blog.cloudflare.com/ja-jp/author/michael-hoffmann/)

16分で読了

URLをコピー

この記事は以下でも利用可能です [English](https://blog.cloudflare.com/building-our-maintenance-scheduler-on-workers/)、[한국어](https://blog.cloudflare.com/ko-kr/building-our-maintenance-scheduler-on-workers/)、[繁體中文](https://blog.cloudflare.com/zh-tw/building-our-maintenance-scheduler-on-workers/)、[简体中文](https://blog.cloudflare.com/zh-cn/building-our-maintenance-scheduler-on-workers/).

![BLOG-3017 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49MH5G11Z4TPXRMZT8FJXD.png&w=1016&h=635&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAAO1yFQGCLTWmWWXWgX36jXH2gT3OaPWWUQ2mQU3OWbIakeZSydpe5aJC3WIOrT3eeS3acYoSjhJ6zk67Ei63OdKHLYZK8XoepT3+nao+tkKq9oLvOl7nYfqvVaZrGZpCxUIOuapGzj6rAobnNmrjVhKrTbpvFZZG0TYKyY4y1hKC9l63Flq3JhqPGcJW9XYy0Sn+zWYa1dZO5ip27kJ+6hpm3cI60U4SySH6zVYO1boy3g5W2jJmzhpWwcIuvT4Cx)

_このコンテンツは自動機械翻訳サービスによる翻訳版であり、皆さまの便宜のために提供しています。原本の英語版と異なる誤り、省略、解釈の微妙な違いが含まれる場合があります。ご不明な点がある場合は、英語版原本をご確認ください。_

Cloudflareは[ _世界330都市以上_](https://www.cloudflare.com/network/)にデータセンターを擁しており、データセンターの運営を計画する際には、ユーザーが気づかないうちに、いつでも簡単にサービスを停止できると思うかもしれません。しかし、実際のところ、[ _破壊的メンテナンス_](https://developers.cloudflare.com/support/disruptive-maintenance/)には慎重な計画が必要であり、Cloudflareが成長するにつれて、インフラストラクチャとネットワーク運用の専門家との間の手動調整を通してこうした複雑さを管理することは、ほぼ不可能になりました。

人間が重複するメンテナンスリクエストすべてを追跡し、顧客固有のルーティングルールすべてをリアルタイムで把握することは不可能です。手動による監視だけでは、世界のある地域における日常的なハードウェアの更新が、別の地域の重要なパスと誤って競合しないことを保証できない時点に達していました。

そして、安全策として機能する一元化された自動化された「頭脳」が必要だと考えました。つまり、ネットワーク全体の状態を一度に確認できるシステムが必要だったのです。このスケジューラーを[ _Cloudflare Workers_](https://workers.cloudflare.com/)上に構築することで、プログラム的に安全制限を強制する方法を作り、どれだけ迅速に進めても、お客様が頼りにするサービスの信頼性を犠牲にすることはありません。

このブログ記事では、その構築方法と、現在の結果についてお伝えします。

## 重要なメンテナンス作業のリスクを軽減するシステムの構築

都市圏で運用されている多くのCloudflareデータセンターにパブリックインターネットをまとめて接続する、小規模で冗長なゲートウェイグループの1つとして機能するエッジルーターを想像してみてください。人口の多い都市では、この小さなルーター群の背後にある複数のデータセンターが、ルーターが同時にオフライン状態にされたために遮断されないようにする必要があります。

もう一つの保守上の課題は、当社のZero Trust製品である専用CDNエグレスIPです。これは、お客様がユーザートラフィックがCloudflareから出る特定のデータセンターを選択し、低遅延のために地理的に近い配信元サーバーに送信するものです。（この記事では簡潔にするために、専用CDNエグレスIP製品を「Aegis」と呼びます。これは、以前の名前でした。）お客様が選択したすべてのデータセンターが一度にオフラインになると、遅延が大きくなり、5xxエラーが発生する可能性がありますが、これは回避しなければなりません。

当社の保守スケジューラーは、こうした問題を解決します。当社は、常に特定のエリアで少なくとも1つのエッジルーターをアクティブにすることができます。また、メンテナンスを計画する際に、複数の予定イベントの組み合わせによって、お客様のAegisプールのすべてのデータセンターが同時にオフラインになるかどうかを確認できます。

スケジューラを作成する前は、こうした同時発生による障害が発生すると、お客様にダウンタイムが発生する可能性がありました。現在、スケジューラは内部オペレーターに競合の可能性を通知し、関連する他のデータセンターメンテナンスイベントとの重複を避けるための新しい時間を提案できるようになりました。

当社では、エッジルーターの可用性や顧客ルールなどの運用シナリオを保守制約として定義し、より予測可能で安全な保守計画を可能にします。

## メンテナンスの制約

すべての制約は、ネットワークルーターやサーバーリストなど、提案されたメンテナンス項目のセットから始まります。そして、提案されたメンテナンス期間と重複するカレンダー上のすべてのメンテナンスイベントを見つけます。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3017 image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45N24BK9S5N2GJ6VGMRCGQ.png&w=715&h=385&f=webp&fit=cover&position=center)

次に、Aegisのお客様のIPプールのリストなど、製品APIを集約します。Aegisは、お客様が特定のデータセンターIDからエグレスを要求したIP範囲のセットを返します（以下に示す）。
    
    
    [
        {
          "cidr": "104.28.0.32/32",
          "pool_name": "customer-9876",
          "port_slots": [
            {
              "dc_id": 21,
              "other_colos_enabled": true,
            },
            {
              "dc_id": 45,
              "other_colos_enabled": true,
            }
          ],
          "modified_at": "2023-10-22T13:32:47.213767Z"
        },
    ]

このシナリオでは、データセンター21とデータセンター45が互いに関連しています。Aegisの顧客である9876がCloudflareからのエグレストラフィックを受け取るために、少なくとも1つのデータセンターがオンラインである必要があるからです。データセンター21と45を同時にダウンさせようとすると、コーディネーターは、その顧客のワークロードに意図しない結果が発生する可能性があることを警告します。

当初は、すべてのデータを1つのWorkerに読み込むような単純なソリューションでした。これには、すべてのサーバー関係、製品設定、および製品とインフラの健全性に関するメトリクスが含まれ、制約を計算することができました。概念実証段階でも、「メモリ不足」エラーの問題に直面しました。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3017 image 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44X5J4KQRSH4Q5YRX5JNQC.png&w=715&h=226&f=webp&fit=cover&position=center)

Workers[ _プラットフォームの制限_](https://developers.cloudflare.com/workers/platform/limits/)をより明確に認識する必要がありました。この方法では、制約のビジネスロジックを処理するために絶対に必要な分だけのデータを読み込む必要がありました。ドイツのフランクフルトでルーターのメンテナンスリクエストが来た場合、地域間の重複がないため、オーストラリアで何が起きているかはどうでもよいことです。したがって、ドイツの隣接するデータセンターにのみデータをロードする必要があります。当社では、データセット内の関係をより効率的に処理する方法が必要でした。

## Workers上でのグラフ処理

制約を検討するうちに、それぞれの制約がオブジェクトとアソシエーションという2つの概念に集約されるパターンが出現しました。グラフの理論では、これらのコンポーネントはそれぞれ垂直とエッジと呼ばれます。オブジェクトはネットワークルーターで、関連付けはルーターがオンラインである必要があるデータセンター内のAegisプールのリストです。Facebookの[ _TAO_](https://research.facebook.com/publications/tao-facebooks-distributed-data-store-for-the-social-graph/)に関する調査論文を参考に、製品とインフラストラクチャのデータを基にグラフインターフェースを構築しました。APIは以下のようなものです：
    
    
    type ObjectID = string
    
    interface MainTAOInterface<TObject, TAssoc, TAssocType> {
      object_get(id: ObjectID): Promise<TObject | undefined>
    
      assoc_get(id1: ObjectID, atype: TAssocType): AsyncIterable<TAssoc>
    }

核となるインサイトは、関連付けが入力されていることです。例えば、制約はグラフインターフェースを呼び出してAegis製品データを取得することなどがあります。
    
    
    async function constraint(c: AppContext, aegis: TAOAegisClient, datacenters: string[]): Promise<Record<string, PoolAnalysis>> {
      const datacenterEntries = await Promise.all(
        datacenters.map(async (dcID) => {
          const iter = aegis.assoc_get(c, dcID, AegisAssocType.DATACENTER_INSIDE_AEGIS_POOL)
          const pools: string[] = []
          for await (const assoc of iter) {
            pools.push(assoc.id2)
          }
          return [dcID, pools] as const
        }),
      )
    
      const datacenterToPools = new Map<string, string[]>(datacenterEntries)
      const uniquePools = new Set<string>()
      for (const pools of datacenterToPools.values()) {
        for (const pool of pools) uniquePools.add(pool)
      }
    
      const poolTotalsEntries = await Promise.all(
        [...uniquePools].map(async (pool) => {
          const total = aegis.assoc_count(c, pool, AegisAssocType.AEGIS_POOL_CONTAINS_DATACENTER)
          return [pool, total] as const
        }),
      )
    
      const poolTotals = new Map<string, number>(poolTotalsEntries)
      const poolAnalysis: Record<string, PoolAnalysis> = {}
      for (const [dcID, pools] of datacenterToPools.entries()) {
        for (const pool of pools) {
          poolAnalysis[pool] = {
            affectedDatacenters: new Set([dcID]),
            totalDatacenters: poolTotals.get(pool),
          }
        }
      }
    
      return poolAnalysis
    }

上記のコードでは、2つのアソシエーションタイプを使用しています：

  1. DATACENTER_INSIDE_AEGIS_POOL：データセンターがあるAegis顧客プールを取得します。
  2. AEGIS_POOL_CONTAINS_DATACENTERは、Aegisプールがトラフィックに対応する必要があるデータセンターを取得します。



アソシエーションは、互いに矛盾する状態を示すものです。アクセスパターンは以前とまったく同じですが、グラフの実装により、クエリするデータ量をより細かく制御できるようになりました。以前は、すべてのAegisプールをメモリにロードし、制約のあるビジネスロジック内でフィルタリングする必要がありました。現在は、アプリケーションにとって重要なデータだけを直接取得することができます。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3017 image 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46V747SXCQBJ3NZGGBWH72.png&w=715&h=313&f=webp&fit=cover&position=center)

グラフの実装によって、ビジネスロジックを複雑にすることなく、舞台裏でパフォーマンスを向上させることができるため、インターフェースは強力です。これにより、WorkersとCloudflareのCDNのスケーラビリティを利用して、内部システムから非常に迅速にデータを取得することができます。

## フェッチパイプライン

新しいグラフ実装の使用に切り替え、より的を絞ったAPI呼び出しを送信します。一晩で応答サイズは100倍減少し、ほんの数件の大規模リクエストの読み込みから多数の小さなリクエストに切り替えました。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3017 image 4](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48J28W9JDW5V667ENB9QRH.png&w=715&h=344&f=webp&fit=cover&position=center)

これにより、メモリに過剰に読み込む問題は解決しますが、いくつかの大規模なHTTPリクエストではなく、桁違いに小さなリクエストを送信するため、サブリクエストの問題が発生します。一晩で、サブリクエストの制限をすばやく突破するようになりました。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3017 image 5](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45SB0HD85RBHA7KBXDD3TD.png&w=715&h=346&f=webp&fit=cover&position=center)

この問題を解決するために、グラフ実装と`fetch` APIの間にスマートミドルウェアレイヤーを構築しました。
    
    
    export const fetchPipeline = new FetchPipeline()
      .use(requestDeduplicator())
      .use(lruCacher({
        maxItems: 100,
      }))
      .use(cdnCacher())
      .use(backoffRetryer({
        retries: 3,
        baseMs: 100,
        jitter: true,
      }))
      .handler(terminalFetch);

Goに慣れている人なら、以前に[ _シングルフライト_](https://pkg.go.dev/golang.org/x/sync/singleflight)のパッケージを見たことがあるかもしれません。このアイデアから着想を得るや、フェッチパイプラインの最初のミドルウェアコンポーネントは、実行されるHTTPリクエストを消去するため、同じWorkerで重複したリクエストを生成するのではなく、すべて同じPromiseを使用してデータを待機します。次に、軽量のLeast Recently Used（LRU）キャッシュを使用して、以前にすでに確認されたリクエストを内部にキャッシュします。

これらの両方が完了したら、Cloudflareの`caches.default.match`機能を使用して、Workerが実行されている地域のすべてのGETリクエストをキャッシュします。パフォーマンス特性が異なる複数のデータソースがあるため、有効期限（TTL）の値を慎重に選択します。例えば、リアルタイムデータは1分間しかキャッシュされません。比較的静的なインフラストラクチャデータは、データのタイプに応じて、1～24時間キャッシュできます。電力管理データは手動で頻繁に変更される可能性があるため、エッジでより長い期間キャッシュすることができます。

これらのレイヤーに加えて、当社では標準的な指数関数的バックオフ、リトライ、ジッターがあります。これにより、ダウンストリームのリソースが一時的に利用できない可能性のある`フェッチ`コールの無駄を減らすことができます。わずかに後退することで、次のリクエストが正常に取得される可能性が高まります。逆に、Workerがバックオフなしで常にリクエストを送信すると、オリジンが5xxエラーを返し始めた時に、簡単にサブリクエスト制限を突破してしまいます。

総合的に、キャッシュヒット率は最大99%でした。[ _キャッシュヒット率_](https://www.cloudflare.com/learning/cdn/what-is-a-cache-hit-ratio/)は、Cloudflareの高速キャッシュメモリから提供されたHTTPリクエスト（「ヒット」）と、当社のコントロールプレーンで実行されるデータソースへの低速なリクエスト（「ミス」）に対する割合であり、（ヒット / （ヒット＋ミス））として計算されます。レートが高いほど、HTTPリクエストのパフォーマンスが向上し、コストが低くなります。これは、Workerでキャッシュからデータをクエリする方が、別の地域の配信元サーバーからフェッチするよりも桁違いに速いためです。設定を調整した後、メモリとCDNキャッシュのキャッシュヒット率が劇的に上昇しました。当社のワークロードの多くはリアルタイムであるため、1分あたり少なくとも1回は新しいデータをリクエストしなければならないため、ヒット率が100%になることはありません。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![image1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44RXG38NESXHB4QMTCNP2J.png&w=715&h=691&f=webp&fit=cover&position=center)

フェッチングレイヤーの改善についてお話しましたが、オリジンのHTTPリクエストをどのように高速化したかについては触れませんでした。当社の保守コーディネーターは、ネットワークの劣化やデータセンター内の機器の故障にリアルタイムで対応する必要があります。当社の分散型[ _Prometheus_](https://blog.cloudflare.com/how-cloudflare-runs-prometheus-at-scale/)クエリエンジン、Thanosを使って、エッジからコーディネーターへ高性能なメトリクスを届けます。

## Thanosでリアルタイムに

グラフ処理インターフェースの使用という選択がリアルタイムクエリにどのように影響したかを説明するために、例を挙げながら説明します。エッジルーターの正常性を分析するために、次のクエリを送信します。
    
    
    sum by (instance) (network_snmp_interface_admin_status{instance=~"edge.*"})

当初、Prometheusメトリクスを保存するThanosサービスに、各エッジルーターの現在の正常性ステータスのリストを提供し、Worker内のメンテナンスに関連するルーターを手動でフィルタリングする予定でした。これは、多くの理由から最適とは言えません。例えば、Thanosは、デコードとエンコードに必要なマルチMBのレスポンスを返しました。Workerは、特定のメンテナンスリクエストを処理している間、データの大部分をフィルタリングするためだけに、こうした大きなHTTPレスポンスをキャッシュしてデコードする必要もありました。TypeScriptはシングルスレッドで、JSONデータの解析はCPUバウンドであるため、2つの大きなHTTPリクエストを送信すると、一方がブロックされることは、解析が完了するのを待つことになります。

代わりに、グラフを使用して、エッジルーターとスパインルーター間のインターフェースリンクなどの対象となる関係を見つけるだけで、`EDGE_ROUTER_NETWORK_CONNECTS_TO_SPINE`と表されます。
    
    
    sum by (lldp_name) (network_snmp_interface_admin_status{instance=~"edge01.fra03", lldp_name=~"spine.*"})

結果は、複数のMBではなく、平均1Kb、または約1000倍小さいものです。デシリアル化のほとんどをThomasに任せるため、Worker内部で必要となるCPUの量も大幅に削減されます。以前説明したように、これは、これらの小さなフェッチリクエストをより多く作成する必要があることを意味しますが、Thanosの前のロードバランサーは、リクエストを均等に分散して、このユースケースのスループットを向上させることができます。

グラフの実装とフェッチパイプラインは、何千もの小さなリアルタイムリクエストの「大量の攻撃」を制御することに成功しました。しかし、履歴の分析によっては、異なるI/Oの課題が浮き彫りになっています。小さく特定の関係を取得するのではなく、数か月のデータをスキャンして、競合するメンテナンス期間を見つける必要があります。以前は、Thanosはオブジェクトストアである[R2](https://www.cloudflare.com/developer-platform/products/r2/)に大量のランダムリードを発行していました。パフォーマンスを失うことなく、この膨大な帯域幅のペナルティを解決するため、今年、Observabilityチームが社内で開発した新しいアプローチを採用しました。

## 過去のデータ分析

当社のソリューションが正確で、Cloudflareネットワークの成長に合わせて拡張できるかどうかを判断するには、過去のデータに頼らなければならないメンテナンスユースケースが十分にあります。インシデントを引き起こしたくないですし、提案された物理的なメンテナンスが不必要にブロックされることも避けたいと考えています。この2つの優先事項のバランスをとるために、2か月前、あるいは1年前に発生した保守イベントに関する時系列データを使用して、保守イベントがどの程度の頻度で当社の制約の一つに違反しているかを把握することができます。エッジルーターの可用性やAegisなどです。今年初め、私たちはThanosを使用して、[ _ソフトウェアをエッジに自動的にリリースおよび元に戻す_](https://blog.cloudflare.com/safe-change-at-any-scale/)ことについてブログを書きました。

Thanosは主にPrometheusにファンアウトしますが、Prometheusのリテンションがクエリーに応答するには不十分な場合、オブジェクトストレージ（この場合はR2）からデータをダウンロードする必要があります。Prometheus TSDBブロックはもともとローカルSSD用に設計されたもので、ランダムなアクセスパターンに依存していますが、オブジェクトストレージに移行するとボトルネックになります。スケジューラが矛盾する制約を特定するために、数か月分の過去のメンテナンスデータを分析する必要がある場合、オブジェクトストレージからのランダムな読み取りには多額のI/Oペナルティが発生します。これを解決するために、これらのブロックを[ _Apache Parquet_](https://parquet.apache.org/)ファイルに変換する変換レイヤーを実装しました。Parquetは、ビッグデータ分析にネイティブな列形式で、データを行ではなく列ごとに整理し、豊富な統計と併せて、必要なデータだけを取得することができます。

さらに、TSDBブロックをParquetファイルに書き換えているため、数回の大きな連続チャンクでデータを読み取れるような方法でデータを保存することもできます。
    
    
    sum by (instance) (hmd:release_scopes:enabled{dc_id="45"})

上記の例では、タプル「(__name__, dc_id)」をプライマリソートキーとして選択し、名前「hmd:release_scopes:enabled」と「dc_id」の同じ値が近くにソートされるようにします。

Parquetゲートウェイは、クエリに関連する特定のカラムのみをフェッチするために、正確なR2範囲のリクエストを発行するようになりました。これにより、ペイロードがメガバイトからキロバイトに削減されます。さらに、これらのファイルセグメントは不変であるため、Cloudflare CDNで積極的にキャッシュすることができます。

これにより、R2は低遅延のクエリエンジンになり、長期的な傾向に対して複雑な保守シナリオを即座にバックテストすることができ、元のTSDBフォーマットで見られたタイムアウトや高いテール遅延を回避できます。下のグラフは最近の負荷テストを示しています。Parquetは、同じクエリーパターンで旧システムと比較して、最大15倍のP90パフォーマンスを達成しました。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![image8](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48BX8FVSJG36HNQHC5YCNS.png&w=715&h=222&f=webp&fit=cover&position=center)

Parquetの実装の仕組みをより深く理解するには、PromCon EU 2025でのこの講演「[ _Beyond TSDB: Unlocking Prometheus with Parquet for Modern Scale_](https://www.youtube.com/watch?v=wDN2w2xN6bA&list=PLoz-W_CUquUlHOg314_YttjHL0iGTdE3O&index=16)」をご覧ください。

## 拡張を想定して構築する

Cloudflare Workersを活用することで、メモリ不足のシステムから、データをインテリジェントにキャッシュし、効率的な可観測性ツールで製品とインフラのデータをリアルタイムで分析できるシステムへと移行することができました。ネットワーク成長と製品パフォーマンスのバランスをとる保守スケジューラーを構築しました。

ただし、「バランス」は動く標的です。

日々、世界中にハードウェアが追加され、お客様のトラフィックを妨げずに保守を行うために必要なロジックは、製品や保守作業の種類が増えるにつれて指数関数的に困難になっています。これまでは一連の課題を乗り越えてきましたが、今はこの大規模なスケールでしか現れない、より微妙で複雑な課題に直面しています。

難しい問題を恐れないエンジニアが必要です。当社の[ _インフラストラクチャチーム_](https://www.cloudflare.com/careers/jobs/?department=Infrastructure)に参加して、私たちと共に構築しましょう。

このページ

オンラインで議論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fbuilding-our-maintenance-scheduler-on-workers%2F&t=Workers%E3%81%8C%E7%A4%BE%E5%86%85%E3%83%A1%E3%83%B3%E3%83%86%E3%83%8A%E3%83%B3%E3%82%B9%E3%82%B9%E3%82%B1%E3%82%B8%E3%83%A5%E3%83%BC%E3%83%AB%E3%83%91%E3%82%A4%E3%83%97%E3%83%A9%E3%82%A4%E3%83%B3%E3%82%92%E5%BC%B7%E5%8C%96%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95)[](https://x.com/intent/post?text=Workers%E3%81%8C%E7%A4%BE%E5%86%85%E3%83%A1%E3%83%B3%E3%83%86%E3%83%8A%E3%83%B3%E3%82%B9%E3%82%B9%E3%82%B1%E3%82%B8%E3%83%A5%E3%83%BC%E3%83%AB%E3%83%91%E3%82%A4%E3%83%97%E3%83%A9%E3%82%A4%E3%83%B3%E3%82%92%E5%BC%B7%E5%8C%96%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fbuilding-our-maintenance-scheduler-on-workers%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fbuilding-our-maintenance-scheduler-on-workers%2F)[](https://bsky.app/intent/compose?text=Workers%E3%81%8C%E7%A4%BE%E5%86%85%E3%83%A1%E3%83%B3%E3%83%86%E3%83%8A%E3%83%B3%E3%82%B9%E3%82%B9%E3%82%B1%E3%82%B8%E3%83%A5%E3%83%BC%E3%83%AB%E3%83%91%E3%82%A4%E3%83%97%E3%83%A9%E3%82%A4%E3%83%B3%E3%82%92%E5%BC%B7%E5%8C%96%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fbuilding-our-maintenance-scheduler-on-workers%2F)[](https://mastodonshare.com/?text=Workers%E3%81%8C%E7%A4%BE%E5%86%85%E3%83%A1%E3%83%B3%E3%83%86%E3%83%8A%E3%83%B3%E3%82%B9%E3%82%B9%E3%82%B1%E3%82%B8%E3%83%A5%E3%83%BC%E3%83%AB%E3%83%91%E3%82%A4%E3%83%97%E3%83%A9%E3%82%A4%E3%83%B3%E3%82%92%E5%BC%B7%E5%8C%96%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fbuilding-our-maintenance-scheduler-on-workers%2F)[](https://www.threads.net/intent/post?text=Workers%E3%81%8C%E7%A4%BE%E5%86%85%E3%83%A1%E3%83%B3%E3%83%86%E3%83%8A%E3%83%B3%E3%82%B9%E3%82%B9%E3%82%B1%E3%82%B8%E3%83%A5%E3%83%BC%E3%83%AB%E3%83%91%E3%82%A4%E3%83%97%E3%83%A9%E3%82%A4%E3%83%B3%E3%82%92%E5%BC%B7%E5%8C%96%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fbuilding-our-maintenance-scheduler-on-workers%2F)

## 関連するタグ

[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[Prometheus](https://blog.cloudflare.com/ja-jp/tag/prometheus/)[インフラストラクチャ](https://blog.cloudflare.com/ja-jp/tag/infrastructure/)[信頼性](https://blog.cloudflare.com/ja-jp/tag/reliability/)

SNS をフォロー

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 新しい投稿のお知らせを受け取るように登録する

メールアドレス

また、あなたのメールアドレスを共有したりすることはございません。

登録する

ご購読ありがとうございます！受信箱を確認して登録してください。
