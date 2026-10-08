---
url: https://blog.cloudflare.com/ja-jp/clickhouse-query-plan-contention/
title: \u8acb\u6c42\u30d1\u30a4\u30d7\u30e9\u30a4\u30f3\u304c\u7a81\u7136\u9045\u304f\u306a\u3063\u305f\u306e\u3067\u3059\u3002\u539f\u56e0\u306fClickHouse\u306e\u96a0\u308c\u305f\u30dc\u30c8\u30eb\u30cd\u30c3\u30af\u3067\u3057\u305f | Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:43:03.433240+00:00
---

# 請求パイプラインが突然遅くなったのです。原因はClickHouseの隠れたボトルネックでした | Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/clickhouse-query-plan-contention/

[ブログ](https://blog.cloudflare.com/ja-jp/)

[ClickHouse](https://blog.cloudflare.com/ja-jp/tag/clickhouse/)[エンジニアリング](https://blog.cloudflare.com/ja-jp/tag/engineering/)[オープンソース](https://blog.cloudflare.com/ja-jp/tag/open-source/)2件2件タグを表示

5 タグタグを5件表示

  * 投稿タグ
  * [ClickHouse](https://blog.cloudflare.com/ja-jp/tag/clickhouse/)[エンジニアリング](https://blog.cloudflare.com/ja-jp/tag/engineering/)[オープンソース](https://blog.cloudflare.com/ja-jp/tag/open-source/)[データベース](https://blog.cloudflare.com/ja-jp/tag/database/)[パフォーマンス](https://blog.cloudflare.com/ja-jp/tag/performance/)
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



[データベース](https://blog.cloudflare.com/ja-jp/tag/database/)[パフォーマンス](https://blog.cloudflare.com/ja-jp/tag/performance/)

[ClickHouse](https://blog.cloudflare.com/ja-jp/tag/clickhouse/)[エンジニアリング](https://blog.cloudflare.com/ja-jp/tag/engineering/)[オープンソース](https://blog.cloudflare.com/ja-jp/tag/open-source/)[データベース](https://blog.cloudflare.com/ja-jp/tag/database/)[パフォーマンス](https://blog.cloudflare.com/ja-jp/tag/performance/)

2026年5月14日

# 請求パイプラインが突然遅くなったのです。原因はClickHouseの隠れたボトルネックでした

![James Morrison](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DJ4SH6R0522V96RWBCS5.webp&w=64&h=64&f=webp&fit=cover&position=center)![Christian Endres](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW446RYCN9GFDAVP4BR4X64Q.webp&w=64&h=64&f=webp&fit=cover&position=center)

[James Morrison](https://blog.cloudflare.com/ja-jp/author/james-morrison/)、[Christian Endres](https://blog.cloudflare.com/ja-jp/author/christian-endres/)

15分で読了

URLをコピー

この記事は以下でも利用可能です [English](https://blog.cloudflare.com/clickhouse-query-plan-contention/)、[한국어](https://blog.cloudflare.com/ko-kr/clickhouse-query-plan-contention/)、[繁體中文](https://blog.cloudflare.com/zh-tw/clickhouse-query-plan-contention/)、[简体中文](https://blog.cloudflare.com/zh-cn/clickhouse-query-plan-contention/).

![BLOG-3299 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4999A46M2F3BCY3QF5F258.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA//////789PLy7evs7+3t8/Hx8/Hv7ezp///////+8vL06Oju5+jv7O3y7+/x7e3s////////8vP45Ofx4eXx5+r17O707u/v////////9ff95+r14+f26Oz57/H48vP0/////////P3/7/L77fD78vT/9/j++Pn6////////////+/v//Pv//////////v/+////////////////////////////////////////////////////////////////)

_このコンテンツは自動機械翻訳サービスによる翻訳版であり、皆さまの便宜のために提供しています。原本の英語版と異なる誤り、省略、解釈の微妙な違いが含まれる場合があります。ご不明な点がある場合は、英語版原本をご確認ください。_

Cloudflareでは、オープンソースのオンライン分析処理（OLAP）データベースであるClickHouseのヘビーユーザーです。Cloudflare製品の使用に対するユーザーの課金方法を決めるために、Cloudflareは毎日何百万ものClickHouseに問い合わせます。迅速にこれらの作業を終了させなければ、請求書の調整は非常に困難になります。

このパイプラインは、数億ドルの使用料、詐欺システムなどを支えているため、遅延が下流に大きな影響を与えます。

このような理由から、Cloudflareの請求額を処理するクリックハウスの日次集計ジョブが、移行後に遅くなった時に、大きな問題となりました。I/O、メモリ、スキャンされた行、読み取り部分など、通常の疑わしいものはすべてクリーンに見えました。ClickHouseのクエリーが遅い時に通常チェックするはずのすべてが、正常なようです。

これは、ClickHouseの内部に深く潜む隠れたボトルネックを発見した経緯と、それを修正するために書いた3つのパッチについてです。

## セットアップ：ペタバイト規模の分析プラットフォーム

当社は、数十のクラスターにわたって100ペタバイトを超えるデータを保存するためにClickHouseを使用します。多くの社内チームのオンボーディングを簡素化するために、2022年初頭、「Ready-Analytics」と呼ばれるシステムを構築しました。

前提はシンプルです。新しいテーブルを設計する代わりに、チームは単一の巨大なテーブルにデータをストリーミングできます。データセットは`名前空間`によって識別され、各レコードは標準スキーマ（例：20個の浮動小数点フィールド、20個の文字列型フィールド、タイムスタンプ、および`インデックスID`）を使用します。

ClickHouseでは、クエリパフォーマンスを最適化するために、データのソート方法が重要です。そこで登場するのが`indexID`です。これは文字列フィールドであり、プライマリキーの一部を形成します。つまり、個々のネームスペースは、そのネームスペースの所有者が実行していると予想されるクエリに最適な方法でデータをソートできます。( `namespace`,`indexID`, `timestamp` )このようなプライマリキーになります。

このシステムは人気があり、何百ものアプリケーションが使っています。2024年12月までに、すでに2PiBを超えるデータ、および毎秒数百万行の取り込み速度にまで成長しました。しかし、Cloudflareには重大な欠陥がひとつありました。それは、保持ポリシーです。

## 問題：単一の保持ポリシーですべてを管理

Cloudflareは、ネイティブの有効期限（TTL）機能が実装される以前から、何年もClickHouseを使用しています。その結果、パーティショニングに基づく独自のリテンションシステムを構築したのです。Ready-Analyticsテーブルは`日`単位でパーティション分割され、保持ジョブは31日より古いパーティションを削除するだけです。

この「画一的」な31日間の保持期間は大きな制限でした。法的または契約上の義務により、何年もデータを保存する必要があるチームもあれば、わずか数日でデータを保存する必要があるチームもありました。この制限により、これらのユースケースはReady-Analyticsを使用できず、オンボーディングプロセスがはるかに複雑な従来のセットアップを選択せざるを得なくなりました。

当社では、**ネームスペースごとの保持** を可能にする新しいシステムが必要でした。

## 解決策：新しい分割スキーム

当社は主要なアプローチとして2つ検討しました。

  1. **ネームスペースごとのテーブル：** これにより保持の問題は当然解決されますが、何千ものテーブルをオンデマンドで管理するには大幅な新しい自動化が必要になります。
  2. **新しい分割キー：** 分割キーは`（日）`から`（ネームスペース、日）`に変更できます。



私たちは2つ目の選択肢を選びました。これにより、既存の保持システムは引き続きパーティションを管理できますが、ネームスペースごとに粒度の細かい管理が可能になります。

これによって、テーブル内のデータコンポーネントの総数が増えることはわかっていましたが、重要な仮定がありました。**すべてのクエリは特定のネームスペースによってフィルタリングされているため、 _単一のクエリで読み込まれる部分の数_ は変化しないはずです。**これなら、パフォーマンスに影響を与えないと私たちは考えました。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3299 image4](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4893FX4WFRGPEECQSTGMYN.png&w=715&h=709&f=webp&fit=cover&position=center)

 _これは、パーティショニングを変更し、単一のネームスペースのデータを安価にドロップできる方法を示しています。_

この新しいシステムにより、高度なストレージ管理レイヤーも構築できました。[ _最大最小公平性アルゴリズム_](https://en.wikipedia.org/wiki/Max-min_fairness)を使用することで、目標ディスク使用率（例：90%）を設定し、利用可能なスペースを自動的に「共有」できます。公正なシェアを下回るネームスペースは、使われていない容量を、より多く必要なネームスペースに振り分けることになります。これにより、クラスターを90%の稼働率で自信を持って稼働できるようになりました。

2025年1月に移行を開始しました。ClickHouseの`Merge`テーブル機能を使用して、古いテーブルと新しいテーブルを結合し、古いデータが順次削除されるようにしながら、すべての新しいデータを新しいパーティションテーブルに書き込みました。

## 謎：請求が発生するのはいつか

それから2か月後、2025年3月下旬、請求チームから日々の集計業務が遅くなっているという報告がありました。これらの仕事はタイムクリティカルです。終了しないと、請求書は発生しません。作業は徐々に遅くなり、期限に近づいていました。

調査をしましたが、通常の疑わしい人は全員責任を負うものではありませんでした。I/Oは問題ありませんでした。メモリは問題ありませんでした。個々のクエリの指標は、以前よりも多くのデータや多くの部分を読み取ってい _ない_ ことを示しました。最初の仮定は正しいように見えましたが、システムは急停止に追い込まれていました。

理論的な話が出るまでに数日かかりました。最後に、クラスター内の _合計パート数_ に対するクエリ時間をプロットしました。この相関関係は否定できません。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3299 image2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47YV50ASJA17DM0BX4JXF3.png&w=715&h=235&f=webp&fit=cover&position=center)

 _Ready Analytics ClickHouseクラスターの平均SELECTクエリ時間。段階的なパフォーマンス低下を示しています。_

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3299 image1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45HY9NE8VMFT5Z5RMHRVCM.png&w=715&h=233&f=webp&fit=cover&position=center)

 _新しい（ネームスペース、日）分割スキームに従って、テーブルレプリカごとの総データ部数が直線的に増加します。_

でも、 _なぜ_ でしょうか？余分な部分を _読んでい_ ないのに、なぜ余分な部分があるだけの状態だったのでしょうか？

## 調査：フレアグラフでボトルネックを検出

そこで、ClickHouseに組み込まれた[` _trace_log_`](https://clickhouse.com/docs/operations/system-tables/trace_log)を使用してフレームグラフを作成しました。これは、実行中のClickHouseサーバーからのトレースを記録する組み込みテーブルです。つまり、実行されているコードのトレースだけでなく、これらを特定のユーザー、クエリID、その他のメタデータに関連付けることができるため、必要に応じて正確なイベントセットまでフィルタリングできます。今回の場合、特に _リーフSELECTクエリ_ に注目したいと思いました。このテーブルにメタデータがあったため、これは簡単でした。

最初のCPUベースのフレームグラフは、**クエリの計画** に膨大な時間が費やされているという疑念をすぐに裏付けるものです。これは、ClickHouseがどの部分を読むかを決定する、実行 _前の_ フェーズです。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3299 image7](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46RG580ZDKK07KCTRDD0MK.png&w=715&h=368&f=webp&fit=cover&position=center)

 _フレームグラフ：リフレクションクエリーのCPU時間の45%が、パーティションIDに基づいたパーツのベクトルのフィルタリングに費やされていることを示すフレームワーク_

火災グラフは明白で、サンプリングされたCPU時間の45%が、`filterPartsByPartition`と呼ばれる単一の関数に費やされていることがわかりました。

私たちが最初に修正を試みたのは、この正確なコードパスへの小さなパッチでした。プランナーはヒューリスティックを評価してパーツを剪定しますが、私たちのテーブルにとって最適な順序で評価されていないと考えたのです。当社のパッチは順序を変え、5%小さな改善をもたらしました。私たちは正しい道に進めていましたが、本当の問題を見逃していました。

それまでは、アクティブなスレッドのみをサンプリングする「CPU」トレースを生成していました。非アクティブまたは待機中のスレッドを含む、 _すべての_ スレッドをサンプリングする"Real"トレースに切り替えました。新しいフレームグラフは啓示を与えてくれました。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3299 image10](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48HV7ET9Z7PXF66NF9GT9Y.png&w=715&h=351&f=webp&fit=cover&position=center)

 _フレームグラフ：リフレクション攻撃時間の半分以上がアクティブ部のリストを保護するミュートを待つことに費やされていることを示すフレームワーク_

問題はCPUに縛られる作業ではなく、**大規模なロック競合** でした。クエリ時間の半分以上は、テーブルの部分リストを保護する単一のミューテックス（`MergeTreeData`）の取得を _待つ_ のに費やされていました。クエリを計画するには、すべてのスレッドは次の必要があります：

  1. このミュートの**専用ロック** を取得します。
  2. 表内の _すべて_ の部品のリストを完全にコピーします。
  3. ロックを解除します。
  4. 関連部分までフィルタリングします。



何万ものコンポーネント、何百もの同時クエリーがあり、それらはすべて単一ファイルの行に並んでいるのです。

## 修正：3つのパッチ

このインサイトは、これらのホットスポットを軽減するための一連の最適化を計画するのに役立ちました。ClickHouseに作るすべてのパッチと同様に、汎用的なものにして、最終的にはアップストリームのコードベースに貢献させることを試みます。そうすることで、フォークを維持するのがより簡単になり、私たちの変更はコミュニティにも利益をもたらします。

### 最適化1：共有ロックの使用

クエリプランナーは、パーツリストを _変更_ しません。単に _読み取る_ だけです。専用ロックを使うケースはありませんでした。

**修正:** 代わりに、**共有ロック** (`std::shared_lock`) を取得するようにコードを変更しました。これにより、すべてのクエリプラン担当者が同時にクリティカルセクションに入ることができました。

**結果：** クエリー時間が大幅に短縮されました。ロックコンテンツが消失しました。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3299 image8](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47CCVN8NX5N7V0Q8SYKEFN.png&w=715&h=235&f=webp&fit=cover&position=center)

 _共有ロック最適化（最適化1）の平均SELECTクエリ時間への影響の即時分析、ロックコンテンツの解決を示す。_

### 最適化2：ベクトルのコピーを阻止

パフォーマンスは大幅に改善されましたが、まだベースラインには戻りませんでした。トレースログに戻って、別の「リアル」なフレームグラフを作成しました。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3299 image5](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48M55TB5PVRTEDJNTSB64J.png&w=715&h=351&f=webp&fit=cover&position=center)

 _フレームグラフは、リフレクションクエリー期間の4分の1ですべての部品のベクトルをコピーし、別の四半期でフィルタリング（再度コピー）していることを示しています。_

新しいフレアグラフは、ボトルネックが単に移動しただけであることを示しました。今では、共有ロックがあるにもかかわらず、巨大なパーツのベクトルを _コピー_ するのに時間が費やされていました。直感的に、ベクトルのコピーは安価に聞こえますが、数万の要素が含まれており、1秒間に数百回行うと、コストが積み上がります。

**修正版：** コピーの作成を完全に遅らせました。当社は、部品リストの「共有コピー」を作成しました。読み取り専用操作（クエリ計画など）は、このコピーから読み取るだけです。パーツのセットを _変更する_ 操作（新規挿入など）は、キャッシュを再生成します。プランナーは、実際に必要な部品の _フィルター済み_ リストのみをコピーするようになりました。

**結果：** もう1つ、大幅なパフォーマンス改善が見られます。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3299 image6](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44PPRSHYTZ68EXGM666V41.png&w=715&h=236&f=webp&fit=cover&position=center)

 _ベクトルコピーの最適化（最適化2）を展開した後のさらなるパフォーマンス改善。_

このように大幅なコスト削減を社内で確認した後、私たちはこの変化をコミュニティにも提供することにしました。ClickHouse Inc.のメンテナーとのいくつかの小さなデザインの反復の後、変更は[ _PR #85535_](https://github.com/ClickHouse/ClickHouse/pull/85535) _の下で_ マージされました。[ _ClickHouseのバージョン25.11_](https://clickhouse.com/docs/whats-new/changelog/2025#performance-improvement-1)から利用可能です。

### 最適化3：パートナーのバイナリ検索

これで終わりではありません。部品の数が増加しても、パフォーマンスは _それでも_ ずっとゆっくりと低下します。部数との相関関係は依然ありました。数か月後に戻ると、新しいフレームグラフ（図3と同じ）は、フィルタリングのコードパス（私たちが最初に修正しようとしたもの）で費やされている時間を示しています。このコードは、すべてのパーツに対して**線形スキャン** を実行し、それぞれに対する述語を評価します。数か月かけて、最適化前からの期間選択に戻りました。

しかし、このコンポーネントのリストは分割キーでソートされることがわかっています。パーティションキーの最初の列は名前空間であることを覚えておいてください。名前空間はクエリの大部分でフィルタリングされ、「テナント」を識別するためです。これをどのように活用できるか？

**修正方法：** パーティションIDの`ネームスペース`の部分に基づいてバイナリ検索を実装しました。これが機能するのは、ベクトルがソートされているため、実際にそれらを見なくても多くのエントリをフィルタリングできるからです。`ネームスペース`はソートキーの最初の部分であるため、これは特に効果的です。このバイナリ検索の最初の通過後、調査する必要のある部分の範囲ははるかに小さくなり、それらについては、以前と同じロジックを適用して他の条件に基づいて部分を除外します。

**結果:** 2026年3月にこのパッチをデプロイした後、クエリ時間が50%短縮されました（図8を参照）。さらに重要なのは、これによりクエリ期間と部数の相関関係が解消されることです。残念ながら、このソリューションは任意のクエリー条件（例：`namespace in (5,10)` のような条件。部分フィルタリングをカバーするために、[ _クエリ条件キャッシュ_](https://clickhouse.com/blog/introducing-the-clickhouse-query-condition-cache)を拡張するなど、より一般的なアプローチを検討しています。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3299 image3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46ZC0AXABREP5Q1ES3D0CS.png&w=715&h=239&f=webp&fit=cover&position=center)

 _バイナリ検索のパート削除（最適化3）の実装後の持続的な遅延削減。_

## 不安の種

こうした最適化により、請求システムに関する差し迫った問題は解決されました。しかし、今回の訪問で、分割を選択した場合の目に見えない深刻なコストが明らかになりました。

その他の問題も残っています。このブログ記事では、選択した期間でパートカウントが増加する問題についてのみ述べてきましたが、それはClickHouse内のすべてのパートのメタデータを追跡するZooKeeperにとっても問題になりました。おそらく、いつかという日が、100ギガバイトのZooKeeperクラスターの話をすることになるでしょう。

私たちは自分たちに大きな余裕をもたらしましたが、根本的な疑問は残っています。この分割スキームが長期的に正しい選択だったのでしょうか？あるいは、最終的には中断させて、別のアーキテクチャに移行する必要があるのでしょうか？今現在はパッチが適用されている状態ですが、この経験は、十分に計画された変更であっても、誤った思い込みにつながる可能性があることを示す明確な例でした。

請求チームがこの問題を最初に報告したとき、当社ではレプリカ1つあたり30,000件の部品がありました。パート率は増加を続けることがなく、1年後はレプリカあたり16万パートに達しましたが、ここで行った最適化のおかげでクエリ時間は安定しています。

Cloudflareでは、複雑なエンジニアリング問題を大規模に解決します。ここで説明したデバッグと最適化が、あなたが求めている課題のように思われる場合は、当社が募集している[ _いくつかのオープンな職種_](https://www.cloudflare.com/careers/jobs/?department=Engineering)をご確認ください。

このページ

オンラインで議論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fclickhouse-query-plan-contention%2F&t=%E8%AB%8B%E6%B1%82%E3%83%91%E3%82%A4%E3%83%97%E3%83%A9%E3%82%A4%E3%83%B3%E3%81%8C%E7%AA%81%E7%84%B6%E9%81%85%E3%81%8F%E3%81%AA%E3%81%A3%E3%81%9F%E3%81%AE%E3%81%A7%E3%81%99%E3%80%82%E5%8E%9F%E5%9B%A0%E3%81%AFClickHouse%E3%81%AE%E9%9A%A0%E3%82%8C%E3%81%9F%E3%83%9C%E3%83%88%E3%83%AB%E3%83%8D%E3%83%83%E3%82%AF%E3%81%A7%E3%81%97%E3%81%9F)[](https://x.com/intent/post?text=%E8%AB%8B%E6%B1%82%E3%83%91%E3%82%A4%E3%83%97%E3%83%A9%E3%82%A4%E3%83%B3%E3%81%8C%E7%AA%81%E7%84%B6%E9%81%85%E3%81%8F%E3%81%AA%E3%81%A3%E3%81%9F%E3%81%AE%E3%81%A7%E3%81%99%E3%80%82%E5%8E%9F%E5%9B%A0%E3%81%AFClickHouse%E3%81%AE%E9%9A%A0%E3%82%8C%E3%81%9F%E3%83%9C%E3%83%88%E3%83%AB%E3%83%8D%E3%83%83%E3%82%AF%E3%81%A7%E3%81%97%E3%81%9F&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fclickhouse-query-plan-contention%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fclickhouse-query-plan-contention%2F)[](https://bsky.app/intent/compose?text=%E8%AB%8B%E6%B1%82%E3%83%91%E3%82%A4%E3%83%97%E3%83%A9%E3%82%A4%E3%83%B3%E3%81%8C%E7%AA%81%E7%84%B6%E9%81%85%E3%81%8F%E3%81%AA%E3%81%A3%E3%81%9F%E3%81%AE%E3%81%A7%E3%81%99%E3%80%82%E5%8E%9F%E5%9B%A0%E3%81%AFClickHouse%E3%81%AE%E9%9A%A0%E3%82%8C%E3%81%9F%E3%83%9C%E3%83%88%E3%83%AB%E3%83%8D%E3%83%83%E3%82%AF%E3%81%A7%E3%81%97%E3%81%9F+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fclickhouse-query-plan-contention%2F)[](https://mastodonshare.com/?text=%E8%AB%8B%E6%B1%82%E3%83%91%E3%82%A4%E3%83%97%E3%83%A9%E3%82%A4%E3%83%B3%E3%81%8C%E7%AA%81%E7%84%B6%E9%81%85%E3%81%8F%E3%81%AA%E3%81%A3%E3%81%9F%E3%81%AE%E3%81%A7%E3%81%99%E3%80%82%E5%8E%9F%E5%9B%A0%E3%81%AFClickHouse%E3%81%AE%E9%9A%A0%E3%82%8C%E3%81%9F%E3%83%9C%E3%83%88%E3%83%AB%E3%83%8D%E3%83%83%E3%82%AF%E3%81%A7%E3%81%97%E3%81%9F&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fclickhouse-query-plan-contention%2F)[](https://www.threads.net/intent/post?text=%E8%AB%8B%E6%B1%82%E3%83%91%E3%82%A4%E3%83%97%E3%83%A9%E3%82%A4%E3%83%B3%E3%81%8C%E7%AA%81%E7%84%B6%E9%81%85%E3%81%8F%E3%81%AA%E3%81%A3%E3%81%9F%E3%81%AE%E3%81%A7%E3%81%99%E3%80%82%E5%8E%9F%E5%9B%A0%E3%81%AFClickHouse%E3%81%AE%E9%9A%A0%E3%82%8C%E3%81%9F%E3%83%9C%E3%83%88%E3%83%AB%E3%83%8D%E3%83%83%E3%82%AF%E3%81%A7%E3%81%97%E3%81%9F+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fclickhouse-query-plan-contention%2F)

## 関連するタグ

[ClickHouse](https://blog.cloudflare.com/ja-jp/tag/clickhouse/)[エンジニアリング](https://blog.cloudflare.com/ja-jp/tag/engineering/)[オープンソース](https://blog.cloudflare.com/ja-jp/tag/open-source/)[データベース](https://blog.cloudflare.com/ja-jp/tag/database/)[パフォーマンス](https://blog.cloudflare.com/ja-jp/tag/performance/)

SNS をフォロー

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 新しい投稿のお知らせを受け取るように登録する

メールアドレス

また、あなたのメールアドレスを共有したりすることはございません。

登録する

ご購読ありがとうございます！受信箱を確認して登録してください。
