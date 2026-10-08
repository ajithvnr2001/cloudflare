---
url: https://blog.cloudflare.com/ja-jp/connecting-to-production-the-architecture-of-remote-bindings/
title: \u672c\u756a\u74b0\u5883\u3078\u306e\u63a5\u7d9a\uff1a\u30ea\u30e2\u30fc\u30c8\u30d0\u30a4\u30f3\u30c7\u30a3\u30f3\u30b0\u306e\u30a2\u30fc\u30ad\u30c6\u30af\u30c1\u30e3 | Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:51:39.713033+00:00
---

# 本番環境への接続：リモートバインディングのアーキテクチャ | Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/connecting-to-production-the-architecture-of-remote-bindings/

[ブログ](https://blog.cloudflare.com/ja-jp/)

[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[D1](https://blog.cloudflare.com/ja-jp/tag/d1/)[R2](https://blog.cloudflare.com/ja-jp/tag/r2/)

3 タグタグを3件表示

  * 投稿タグ
  * [Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[D1](https://blog.cloudflare.com/ja-jp/tag/d1/)[R2](https://blog.cloudflare.com/ja-jp/tag/r2/)
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



[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[D1](https://blog.cloudflare.com/ja-jp/tag/d1/)[R2](https://blog.cloudflare.com/ja-jp/tag/r2/)

2025年11月12日

# 本番環境への接続：リモートバインディングのアーキテクチャ

![Samuel Macleod](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW498X1ZVM0N111DBDKB3MM1.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Dario Piotrowicz](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW450K2XVXFFD2EJ6JZZ2SDE.png&w=64&h=64&f=webp&fit=cover&position=center)

[Samuel Macleod](https://blog.cloudflare.com/ja-jp/author/samuel/)、[Dario Piotrowicz](https://blog.cloudflare.com/ja-jp/author/dario/)

10分で読了

URLをコピー

この記事は以下でも利用可能です [English](https://blog.cloudflare.com/connecting-to-production-the-architecture-of-remote-bindings/)、[한국어](https://blog.cloudflare.com/ko-kr/connecting-to-production-the-architecture-of-remote-bindings/).

![BLOG 2840 Hero Image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48XZE1XZ7YJGDM6ZHMR24M.png&w=1201&h=676&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA9/j96+z20dHnvL3fvsHlztLu2dvu29rm+vv/7vD51NTpv7/fwsPl0dPu293v3d3p////9Pb/29ztyMfiysrm2Nnw4eLz4ePt/////f//5ujz1tbo2Nfs5OT26+z46uzz////////9fb85+jy6ur29PP++Pn/9ff5////////////+Pr9+/z/////////////////////////////////////////////////////////////////////////////)

リモートバインディングは、ローカルでシミュレートされたリソース _ではなく_ 、Cloudflareアカウント上にデプロイされたリソースに接続するバインディングです。当社は最近、[ _リモートバインディングが一般に利用可能になった_](https://blog.cloudflare.com/cloudflare-developer-platform-keeps-getting-better-faster-and-more-powerful/#connect-to-production-services-and-resources-from-local-development-with-remote-bindings-now-ga)ことを発表しました。

このリリースにより、ローカルマシンでWorkerコードを実行しながら、[ _R2バケット_](https://developers.cloudflare.com/r2/)や[ _D1データベース_](https://www.cloudflare.com/developer-platform/products/d1/)などのデプロイされたリソースに接続できるようになりました。つまり、反復ごとにデプロイするオーバーヘッドをかけずに、実際のデータやサービスに対してローカルコードの変更をテストできるのです。

このブログ記事では、当社がどのようにしてシームレスなローカル開発体験を実現したかについて、技術的な詳細を掘り下げます。

### Workersプラットフォームでの開発

[ _Cloudflare Workersプラットフォーム_](https://www.cloudflare.com/developer-platform/products/workers/)の重要な部分は、何かをテストしたいたびにコードをデプロイすることなく、ローカルにコードを開発できる能力です。しかし、これをサポートする方法は、数年にわたって大きく変化しました。

リモートモードで`wrangler`開発を始めることから始めました。これは、コードに変更を加えるたびにCloudflareのネットワーク上で実行されるWorkerのプレビューバージョンをデプロイして接続することで機能し、開発時にテストすることができます。ただし、リモートモードは完璧ではありません。複雑で保守が難しいのです。イテレーション速度が遅い、デバッグ接続が不安定、マルチWorkerシナリオのサポートがないなど、開発者体験には多くのものが含まれています。

これらの問題などをきっかけに、Workersの完全ローカル開発環境への多額の投資が動機となりました。2023年半ばにリリースされたこの開発環境は、[ _wrangler開発のデフォルト体験になりました_](https://blog.cloudflare.com/wrangler3/)。それ以来、当社はCloudflare Viteプラグイン、[ _Wrangler_](https://developers.cloudflare.com/workers/wrangler/)、[ _Cloudflare Viteプラグイン_](https://developers.cloudflare.com/workers/vite-plugin/)（[ _@cloudflare/vitest-pool-workers_](https://developers.cloudflare.com/workers/testing/vitest-integration/)とともに）と[ _Miniflare_](https://developers.cloudflare.com/workers/testing/miniflare/)を使って、ローカル開発エクスペリエンスに膨大な努力を費やしてきました。

それでも、元のリモートモードは、フラグ `wrangler dev --remote` を介してアクセス可能なままでした。リモートモードを使用すると、完全にローカルな体験とここ数年にわたって行ってきた改善がバイパスされてしまいます。では、なぜいまだに使われているのでしょうか？Cloudflareのユニークな特徴は、ローカルで開発しながら、リモートリソースへのバインディングです。ローカルモードを使用してWorkerをローカルに開発する場合、すべての[ _バインディング_](https://developers.cloudflare.com/workers/runtime-apis/bindings/)がローカルの（最初は空の）データを使用してローカルでシミュレートされます。これは、テストデータを使用してアプリのロジックを反復処理するのに最適ですが、チーム全体でリソースを共有したい、実際のデータに関連したバグを再現したい、または実際のリソースを使用して本番環境でアプリが動作することを確認したい場合など、不十分です。 .

そこで、当社は好機だと考えました。リモートモードの優れた部分（つまり、リモートリソースへのアクセスなど）を`wrangler dev`に知らせるための単一のフローがあり、ローカル開発の進歩をユーザーにロックアウトすることなく、多くのユースケースを可能にします。そして、それが私たちの取り組みです。

Wrangler v4.37.0現在、バインディングがリモートリソースを使用するか、ローカルリソースを使用するか、バインディングごとに`選択`できるようになりました。リモートオプションを指定するだけです。これを再度強調することが重要です。`remote: true!` を追加するだけで済みます。API キーや認証情報の複雑な管理は必要ありません。すべては、Wrangler の既存の Oauth 接続を使用して Cloudflare API に機能します。
    
    
    {
      "name": "my-worker",
      "compatibility_date": "2025-01-01",
      "kv_namespaces": [{
        "binding": "KV",
        "id": "my-kv-id",
      },{
        "binding": "KV_2",
        "id": "other-kv-id",
        "remote": true
      }],
      "r2_buckets": [{
        "bucket_name": "my-r2-name",
        "binding": "R2"
      }]
    }

鋭い方は、ローカル開発者からリモートリソースにアクセスして、すでにいくつかのバインディングが機能していることに気づいているかもしれません。最も顕著なのは、[ _AIバインディング_](https://developers.cloudflare.com/workers-ai/configuration/bindings/)が、一般的なリモートバインディングソリューションがどのようなものかを示す先駆者でした。Workers AIで使用できるすべての異なるモデルをサポートする真のローカル体験は現実的ではなく、AIモデルの膨大な事前ダウンロードが必要だからです。

Workers内のさまざまな製品がリモートバインディングに似たものを必要としていることに気づくと（たとえば、ImagesとHyperdriveなど）、異なるソリューションの寄せ集めのようなものになりました。現在、すべてのバインディングタイプに対して機能する、単一のリモートバインディングソリューションに統合されています。

### 構築方法

私たちは、本番用のWorkersコードを変更することなく、開発者が本当に簡単にリモートリソースにアクセスできるようにしたかったのです。そこで、Workerで使用する時点でリモートリソースからデータを取得するというソリューションを使いました。
    
    
    const value = await env.KV.get("some-key")

_上記のコードスニペットは、env.KV[ _KVネームスペース_](https://developers.cloudflare.com/kv/api/read-key-value-pairs/)の「some-key」値にアクセスすることを示しています。これは、ローカルでは利用できず、ネットワーク経由で取得する必要があります。_

では、それが私たちの望む要件だとしたら、どのようにして関係を構築するのでしょうか？例えば、Workerで`env.KV.put(「key」、「value」`）を呼び出すユーザーから、実際にリモートKVストアに保存するにはどうすればいいでしょうか。明らかな解決策は、[ _Cloudflare API_](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/subresources/values/methods/update/)を使うことかもしれませんでした。ローカルにEnv全体をAPI呼び出しを行うスタブオブジェクトで置き換え、`env.KV.put()`をPUT `http:///accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}`に変換することもできました。

これは、KV、R2、D1など、成熟したHTTP APIを持つバインディングではうまく機能したでしょうが、実装と保守がかなり複雑なソリューションになったでしょう。バインディングAPIサーフェス全体を複製し、バインディング上で可能なすべての操作を同等のAPI呼び出しに変換しなければならなかったでしょう。さらに、バインディング操作の中には同等のAPI呼び出しがないため、この戦略ではサポートできません。

むしろ、すぐに使えるAPIがあったことに気づきました。私たちがプロダクションで使っているのです。

### 本番環境におけるバインディングの仕組み

Workersプラットフォームのほとんどのバインディングは、本質的に[ _サービスバインディング_](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/)に集約されます。サービスバインディングは、2つのWorkers間のリンクであり、HTTPまたは[ _JSRPC_](https://blog.cloudflare.com/javascript-native-rpc/)（JSRPCについては後ほど説明します）経由で通信できます。

例えば、KVバインディングは、認可されたWorkerとプラットフォームWorkerの間のサービスバインディングとして実装され、HTTPの話となります。KVバインディング用のJS APIはWorkersランタイムに実装されており、`env.KV.get()`のようなコールをKVサービスを実装するWorkerへのHTTPコールに変換します。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG 2840 Image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46Q87QEAZ2T40R2PF2VVMK.png&w=715&h=299&f=webp&fit=cover&position=center)

 _本番環境におけるKVバインディングの仕組みを示す簡略モデルを示す図_

`env.KV.get()`呼び出しを翻訳するランタイムと、KVサービスを実装するWorkerの間に、自然な非同期ネットワーク境界があることに気づくかもしれません。そして、その自然なネットワーク境界を利用して、リモートバインディングを実装できることに気づきました。 _本番環境_ ランタイムが `env.KV.get()` を HTTP 呼び出しに変換する代わりに、 _ローカル_ ランタイム ([_workerd_](https://github.com/cloudflare/workerd)) が `env.KV.get()` を HTTP 呼び出しに変換し、本番環境ランタイムをバイパスして KV サービスに直接送信することができます。Cloudflareはこれを実現したのです！

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG 2840 Image 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48RHXWQ74T21SNQVVKFPQQ.png&w=715&h=295&f=webp&fit=cover&position=center)

 _単一のKVバインディングでローカルで実行されるworkerを示す図。リモートプロキシサーバーに通信する1つのリモートプロキシクライアントがあり、そのクライアントがリモートKVと通信する_

上の図は、リモートKVバインディングで実行されているローカルWorkerを示しています。ローカルKVシミュレーションではなく、リモートプロキシクライアントによって処理されるようになりました。次に、このWorkerは、実際のリモートKVリソースに接続されたリモートプロキシサーバーと通信し、最終的にローカルWorkerはリモートKVデータとシームレスに通信できます。

各バインディングは、リモートプロキシクライアント（すべて同じリモートプロキシサーバーに接続されている）またはローカルシミュレーションによって独立して処理でき、図のように、一部のバインディングはローカルでシミュレートされ、他のバインディングは実際のリモートリソースに接続する、非常に動的なワークフローが可能になります。下の例にあるものです：

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG 2840 Image 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48GXD2S8761JB6KWM17YM6.png&w=707&h=360&f=webp&fit=cover&position=center)

 _上の図と設定は、2つのローカル（KVとR2）、1つのリモート（KV_2）という3つの異なるリソースにバインドされたWorker（お客様のコンピューター上で実行）を示しています。_

### JSRPC との関係

上記のセクションでは、HTTP接続（KVやR2など）に支えられたバインディングについて説明していますが、最新のバインディングは[ _JSRPC_](https://blog.cloudflare.com/javascript-native-rpc/)を使用しています。つまり、ローカルで実行している`workerd`が本番ランタイムインスタンスにJSRPCを通信するための方法が必要だったのです。

その時、幸運なことに、[ _Cap'n Webのブログ_](https://blog.cloudflare.com/capnweb-javascript-rpc-library/)で詳述するように、これを可能にするための並行プロジェクトが進行していました。ローカル`workerd`インスタンスとリモートランタイムインスタンス間の接続を[ _Cap'n Webを使ってwebsocketで通信する_](https://github.com/cloudflare/capnweb)ことで、これを統合し、JSRPCに支えられたバインディングが機能するようにしました。これには、[ _画像_](https://developers.cloudflare.com/images/transform-images/transform-via-workers/)のような新しいバインディングや、独自のWorkersへのJSRPCサービスバインディングが含まれます。

### Vite、Vite、JavaScriptエコシステムとのリモートバインディング

このエキサイティングな新機能を`Wrangler開発`だけに限定したくありませんでした。Cloudflare Viteプラグインとvitest-pool-workersパッケージでサポートし、JavaScriptエコシステムの他の潜在的なツールやユースケースにも恩恵を受けられるようにしたいと考えました。

これを実現するために、wranglerパッケージは`startRemoteProxySession`などのユーティリティをエクスポートし、`wrangler開発`を活用しないツールもリモートバインディングをサポートできるようになりました。[ _公式のリモートバインディングドキュメント_](https://developers.cloudflare.com/workers/development-testing/#remote-bindings)に詳細を記載しています。

### 試用方法

`Wrangler開発`を使うだけ！Wrangler v4.37.0（`@cloudflare/vite-plugin` v1.13.0、`@cloudflare/vitest-pool-workers` v0.9.0）より、リモートバインディングはすべてのプロジェクトで利用可能で、バインディングごとに追加することで有効にすることができます。`remote: true`は、[ _Wrangler設定ファイル_](https://developers.cloudflare.com/workers/wrangler/configuration/)のバインディング定義に当てはまります。

このページ

オンラインで議論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fconnecting-to-production-the-architecture-of-remote-bindings%2F&t=%E6%9C%AC%E7%95%AA%E7%92%B0%E5%A2%83%E3%81%B8%E3%81%AE%E6%8E%A5%E7%B6%9A%EF%BC%9A%E3%83%AA%E3%83%A2%E3%83%BC%E3%83%88%E3%83%90%E3%82%A4%E3%83%B3%E3%83%87%E3%82%A3%E3%83%B3%E3%82%B0%E3%81%AE%E3%82%A2%E3%83%BC%E3%82%AD%E3%83%86%E3%82%AF%E3%83%81%E3%83%A3)[](https://x.com/intent/post?text=%E6%9C%AC%E7%95%AA%E7%92%B0%E5%A2%83%E3%81%B8%E3%81%AE%E6%8E%A5%E7%B6%9A%EF%BC%9A%E3%83%AA%E3%83%A2%E3%83%BC%E3%83%88%E3%83%90%E3%82%A4%E3%83%B3%E3%83%87%E3%82%A3%E3%83%B3%E3%82%B0%E3%81%AE%E3%82%A2%E3%83%BC%E3%82%AD%E3%83%86%E3%82%AF%E3%83%81%E3%83%A3&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fconnecting-to-production-the-architecture-of-remote-bindings%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fconnecting-to-production-the-architecture-of-remote-bindings%2F)[](https://bsky.app/intent/compose?text=%E6%9C%AC%E7%95%AA%E7%92%B0%E5%A2%83%E3%81%B8%E3%81%AE%E6%8E%A5%E7%B6%9A%EF%BC%9A%E3%83%AA%E3%83%A2%E3%83%BC%E3%83%88%E3%83%90%E3%82%A4%E3%83%B3%E3%83%87%E3%82%A3%E3%83%B3%E3%82%B0%E3%81%AE%E3%82%A2%E3%83%BC%E3%82%AD%E3%83%86%E3%82%AF%E3%83%81%E3%83%A3+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fconnecting-to-production-the-architecture-of-remote-bindings%2F)[](https://mastodonshare.com/?text=%E6%9C%AC%E7%95%AA%E7%92%B0%E5%A2%83%E3%81%B8%E3%81%AE%E6%8E%A5%E7%B6%9A%EF%BC%9A%E3%83%AA%E3%83%A2%E3%83%BC%E3%83%88%E3%83%90%E3%82%A4%E3%83%B3%E3%83%87%E3%82%A3%E3%83%B3%E3%82%B0%E3%81%AE%E3%82%A2%E3%83%BC%E3%82%AD%E3%83%86%E3%82%AF%E3%83%81%E3%83%A3&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fconnecting-to-production-the-architecture-of-remote-bindings%2F)[](https://www.threads.net/intent/post?text=%E6%9C%AC%E7%95%AA%E7%92%B0%E5%A2%83%E3%81%B8%E3%81%AE%E6%8E%A5%E7%B6%9A%EF%BC%9A%E3%83%AA%E3%83%A2%E3%83%BC%E3%83%88%E3%83%90%E3%82%A4%E3%83%B3%E3%83%87%E3%82%A3%E3%83%B3%E3%82%B0%E3%81%AE%E3%82%A2%E3%83%BC%E3%82%AD%E3%83%86%E3%82%AF%E3%83%81%E3%83%A3+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fconnecting-to-production-the-architecture-of-remote-bindings%2F)

## 関連するタグ

[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[D1](https://blog.cloudflare.com/ja-jp/tag/d1/)[R2](https://blog.cloudflare.com/ja-jp/tag/r2/)

SNS をフォロー

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 新しい投稿のお知らせを受け取るように登録する

メールアドレス

また、あなたのメールアドレスを共有したりすることはございません。

登録する

ご購読ありがとうございます！受信箱を確認して登録してください。
