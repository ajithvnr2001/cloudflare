---
url: https://blog.cloudflare.com/ja-jp/how-waiting-room-queues/
title: Cloudflare\u306e\u9ad8\u5ea6\u306b\u5206\u6563\u3055\u308c\u305f\u30cd\u30c3\u30c8\u30ef\u30fc\u30af\u4e0a\u3067\u306e\u3001Waiting Room\u306b\u3088\u308b\u30ad\u30e5\u30fc\u30a4\u30f3\u30b0\u6c7a\u5b9a\u306e\u69d8\u5b50 | Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:43:26.481036+00:00
---

# Cloudflareの高度に分散されたネットワーク上での、Waiting Roomによるキューイング決定の様子 | Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/how-waiting-room-queues/

[ブログ](https://blog.cloudflare.com/ja-jp/)

[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[Durable Objects](https://blog.cloudflare.com/ja-jp/tag/durable-objects/)[Waiting Room](https://blog.cloudflare.com/ja-jp/tag/waiting-room/)3件3件タグを表示

6 タグタグを6件表示

  * 投稿タグ
  * [Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[Durable Objects](https://blog.cloudflare.com/ja-jp/tag/durable-objects/)[ネットワーク](https://blog.cloudflare.com/ja-jp/tag/network/)[開発者](https://blog.cloudflare.com/ja-jp/tag/developers/)[開発者プラットフォーム](https://blog.cloudflare.com/ja-jp/tag/developer-platform/)
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



[ネットワーク](https://blog.cloudflare.com/ja-jp/tag/network/)[開発者](https://blog.cloudflare.com/ja-jp/tag/developers/)[開発者プラットフォーム](https://blog.cloudflare.com/ja-jp/tag/developer-platform/)

[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[Durable Objects](https://blog.cloudflare.com/ja-jp/tag/durable-objects/)[Waiting Room](https://blog.cloudflare.com/ja-jp/tag/waiting-room/)[ネットワーク](https://blog.cloudflare.com/ja-jp/tag/network/)[開発者](https://blog.cloudflare.com/ja-jp/tag/developers/)[開発者プラットフォーム](https://blog.cloudflare.com/ja-jp/tag/developer-platform/)

2023年9月20日

# Cloudflareの高度に分散されたネットワーク上での、Waiting Roomによるキューイング決定の様子

![George Thomas](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48RNGYPD0NP89KE7WB4CS7.png&w=64&h=64&f=webp&fit=cover&position=center)

[George Thomas](https://blog.cloudflare.com/ja-jp/author/george/)

30分で読了

URLをコピー

この記事は以下でも利用可能です [English](https://blog.cloudflare.com/how-waiting-room-queues/)、[Deutsch](https://blog.cloudflare.com/de-de/how-waiting-room-queues/)、[Français](https://blog.cloudflare.com/fr-fr/how-waiting-room-queues/)、[繁體中文](https://blog.cloudflare.com/zh-tw/how-waiting-room-queues/)、[简体中文](https://blog.cloudflare.com/zh-cn/how-waiting-room-queues/).

![How Waiting Room makes queueing decisions on Cloudflare's highly distributed network](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45Q291SVQX0YQV3V9MYAHM.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///////88/Pw6ujq6Ofs6+vx6+3w5+zp/////v377Ovu3d3m2tvo4eLv5unv5urp//////395+bt0dLkzdHm2Nzu4+bw5+rr////////6efy0dPnzdLq2t7y5ur07O7v////////8/L73uDy3eD06Oz78fX89Pf3////////////8/P/9PX//P7//////v//////////////////////////////////////////////////////////////////)

ほぼ3年前、弊社はサイトをダウンさせる可能性のある正規トラフィックの圧倒的な急増から顧客のサイトを保護するため、[Cloudflare Waiting Roomを立ち上げました](https://blog.cloudflare.com/cloudflare-waiting-room/)。Waiting Roomは、過剰なトラフィックをカスタマイズ可能なオンブランドの待機室に配置することで、トラフィックが集中する時間帯でもサイトで空き枠ができると同時に動的にユーザーを接続し、ユーザーエクスペリエンスをコントロールできるようにします。待機室のリリース以来、[モバイルアプリ対応](https://blog.cloudflare.com/waiting-room-random-queueing-and-custom-web-mobile-apps/)、[アナリティクス](https://blog.cloudflare.com/understand-the-impact-of-your-waiting-rooms-settings-with-waiting-room-analytics/)、[Waiting Roomバイパスルール](https://blog.cloudflare.com/waiting-room-bypass-rules/)さらに[その他](https://blog.cloudflare.com/tag/waiting-room/)を含め、顧客からのフィードバックに基づいて機能を拡張し続けています。

弊社は新機能を発表し、待機室の機能を拡張することで顧客の問題の解決に意欲的に取り組んでいます。今回は、私たちの製品のコアとなるメカニズムが進化してきた過程、つまり、トラフィックの急増に対応してキューに入れる仕組みについて、その舞台裏をお話しします。

## Waiting Roomが構築される過程での課題

下の図は、顧客が自社WebサイトでWaiting Roomを有効にしたときの配置を簡単に示した概要図です。

Waiting RoomはCloudflareデータセンターのグローバルネットワーク上で動作する[Workers](https://workers.cloudflare.com/)上に構築されます。顧客のWebサイトへのリクエストは、さまざまなCloudflareデータセンターに送られる可能性があります。最小限の[遅延](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/)を実現しパフォーマンスの強化を最適化するため、これらのリクエストは地理的に最も近いデータセンターにルーティングされます。新しいユーザーがWaiting Roomがカバーするホスト/パスにリクエストを行うと、Waiting Room Workerはユーザーをオリジンに送るか待機室に送るかを決定します。この決定は、待機室の状態からどれだけのユーザーがオリジン上にいるかを読み取ることで行われます。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Waiting Room overview](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49ER0HAP6FBMK03EQF3R8Y.png&w=715&h=504&f=webp&fit=cover&position=center)

待機室の状態は、世界中のトラフィックに基づいて絶えず変化します。この情報は、中心的場所に保存される場合もあり、さらに変化が最終的に世界中に伝播することもあります。この情報を中心的場所に保存すると、中心的場所がリクエストの発信元から非常に遠くなる可能性があるため、各リクエストに大幅な遅延が発生する可能性があります。このため、どのデータセンターも、ある時点で利用可能な世界中のWebサイトのトラフィック・パターンのスナップショットである個別の待機室の状態で動作します。ユーザーをWebサイトに入れる前に世界中のあらゆる場所からの情報を待つことになると、リクエストに大きな遅延を発生させることになるので、避けなければなりません。この理由により、中心的場所は設けず、代わりにトラフィックの変化が最終的に世界中に伝搬されるパイプラインを持つことにしたのです。

バックグラウンドで待機室の状態を集約するこのパイプラインは、Cloudflareの[Durable Objects](https://blog.cloudflare.com/introducing-workers-durable-objects/)上に構築しています。アグリゲーション・パイプラインがどのように機能するのか、そしてそこで弊社が取った様々な設計上の決定について紹介した2021年の[ブログ](https://blog.cloudflare.com/building-waiting-room-on-workers-and-durable-objects/)記事で詳細を説明しています。このパイプラインでは、すべてのデータセンターがトラフィックの変化に関する更新情報を数秒以内に取得できるようにしています。

Wainting Roomは、その時点で見えている状態に基づき、ユーザーをWebサイトに送るかキューに入れるかを判断することになります。顧客のWebサイトが過負荷にならないよう、適切なタイミングでキューに入れるようにしなければなりません。また、誤ってトラフィックが急増したと判断した場合にキューに入れることになるかもしれないため、キューに入れるのが早急すぎるのも問題になります。キューに入れられることで、Webサイトに到達するのを断念するユーザーも出てくるかもしれません。Wainting Roomは、100カ国以上、300以上の都市にまたがる[Cloudflareのネットワーク](https://www.cloudflare.com/network/)内のすべてのサーバーで実行されています。すべての新規ユーザーに対して、Webサイトに行くかキューとして待つかの決定を最小限の遅延で行えることを弊社は目指しています。いつキューに入れるかという決断は、Waiting Roomにとって難題です。このブログでは、そのトレードオフにどのようにアプローチしたかを紹介します。弊社のアルゴリズムは、顧客の設定した制限を尊重し続けながら、誤検出を減らすように進化してきました。

## 待機室がユーザーをキューに入れるか否かを決定する仕組み

待機室がいつキューイングを開始するかを決定するうえで最も重要になる要因は、トラフィック構成の仕方になります。待機室のコンフィグを行う際に設定するトラフィック制限は2種類あり、それぞれ_総アクティブユーザー数_と_1分当たりの新規ユーザー数_となります。_総アクティブユーザー数_は、待機室がカバーするページで同時に許可したいユーザー数の目標しきい値となります。_1分当たりの新規ユーザー数_は、1分あたりのWebサイトへのユーザー流入の最大速度の目標しきい値の定義となります。これらの値のいずれかが急上昇すると、キューが発生します。_総アクティブユーザー数_の計算方法に影響するもう1つの設定に、_セッション時間_があります。待機室がカバーするあらゆるページに対して行われたリクエスト以降、ユーザーは_セッション時間_でアクティブであるとみなされます。

下のグラフは、ある顧客の社内モニタリングツールによるもので、該当の顧客の2日間のトラフィック・パターンを示したものです。この顧客では、_1分あたりの新規ユーザー数_と_アクティブユーザー総数_数の上限をそれぞれどちらも200に設定しています。

トラフィックを見ると、9月11日の11時45分頃にユーザーのキューが作られているのがわかります。その時点では、_総アクティブユーザー数_は約200人でした。 _総アクティブユーザー数_が減少するにつれ（12:30頃）_ 、_キューに入れられたユーザー数は0になっています。この時間帯にユーザーがキューに入れられたことで、Webサイトへのトラフィックが顧客によって設定された制限値に収まっていたことになります。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Customer traffic for 2 days between September 9th to 11th with 2 spikes in traffic](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44SH6VVAQWD238ZTPDJ6F0.png&w=715&h=414&f=webp&fit=cover&position=center)

ユーザーがWebサイトにアクセスすると、暗号化された[クッキー](https://www.cloudflare.com/learning/privacy/what-are-cookies/)が渡されます。クッキーの内容は、次のようなものとなります。

クッキーは、待機室への入室を示すチケットのようなものです。_bucketId_は、このユーザーがどのクラスタに属しているかを示しています。_acceptedAt_時間と_lastCheckIn_時間は、Workerとの最後のやりとりがいつ行われたかを示しています。この情報は、顧客が待機室を設定するときに設定した_セッション持続時間_の値と比較する際、チケットが入室するために有効かどうかを確認できます。クッキーが有効であれば、ユーザーを通過させ、WebサイトにいるユーザーがWebサイトを閲覧し続けられるようにします。クッキーが無効な場合、そのユーザーを新しいユーザーとして扱い新たにクッキーを作成し、Webサイト上で待ち行列が発生している場合はそのユーザーはキューの後ろに回されます。次の節では、ユーザーをキューに入れるタイミングの決定方法を見ていきます。
    
    
    {  
      "bucketId": "Mon, 11 Sep 2023 11:45:00 GMT",
      "lastCheckInTime": "Mon, 11 Sep 2023 11:45:54 GMT",
      "acceptedAt": "Mon, 11 Sep 2023 11:45:54 GMT"
    }

これをさらに理解するために、待機室ステートの内容を見てみます。上で説明した顧客の場合、"Mon, 11 Sep 2023 11:45:54 GMT"時点で、状態は次のようになっていました。

前述のとおり、この顧客のコンフィギュレーションでは、 _1分あたりの新規ユーザー数は200_ 、_総アクティブユーザー数は_200であったことが分かります。
    
    
    {  
      "activeUsers": 50,
    }

つまり、200人に対応できるところにアクティブユーザーが50人しかいないため、新しいユーザーのためのスペースがあることを示しています。したがって、あと150人分のスペースがあることになります。この50人のユーザーが、サンノゼ（20人）とロンドン（30人）の2つのデータセンターから来たと仮定します。また弊社では、全世界で活動しているWorkerの数と、状態が計算されるデータセンターで活動しているWorkerの数も記録しています。下のキーはサンノゼで計算されたものです。

"Mon, 11 Sep 2023 11:45:54 GMT",の時点で、サンノゼのデータセンターでその待機室へのリクエストがあったとします。
    
    
    {  
      "activeUsers": 50,
      "globalWorkersActive": 10,
      "dataCenterWorkersActive": 3,
      "trafficHistory": {
        "Mon, 11 Sep 2023 11:44:00 GMT": {
           San Jose: 20/200, // 10%
           London: 30/200, // 15%
           Anywhere: 150/200 // 75%
        }
      }
    }

サンノゼに到達したユーザーがオリジンに到達できるか確認するために、まず過去1分間のトラフィック履歴をチェックし、その時点でのトラフィックの分布を見ます。というのも、世界の特定の地域で人気があるWebサイトが多くあるためです。これらのWebサイトの多くでは、同じデータセンターからトラフィックが来る傾向があります。

"Mon, 11 Sep 2023 11:44:00 GMT"時点のトラフィック履歴を見ると、サンノゼにはその時点で200人中20人（10％）のユーザーがアクセスしていることがわかります。最新の時刻"Mon, 11 Sep 2023 11:45:54 GMT"では、過去1分間のトラフィック履歴と同じ比率でWebサイトで利用可能なスロットを分割します。つまり、サンノゼから送れるのは150スロットの10%、つまり15ユーザーということになります。また"dataCenterWorkersActive"は3なので、アクティブなWorkerが3つあることもわりかます。

データセンターで利用可能なスロットの数は、データセンターのWorkerで均等に分けられます。したがって、サンノゼのすべてのWorkerである15/3のユーザーをWebサイトに送ることができます。もしトラフィックを受け取ったWorkerがその時点でオリジンにユーザーを送っていなければ、最大_5人_（15÷3）まで送ることができます。

同じ時刻（"Mon, 11 Sep 2023 11:45:54 GMT"）に、デリーのデータセンターにリクエストがあったとします。デリーのデータセンターのWorkerはtrafficHistoryをチェックし、そのために割り当てられたスロットがないことを確認します。このようなトラフィックのために、弊社はAnywhereスロットを用意しておきました。

世界中のWorkerがこの全量の一部を利用できるため、Aynwereスロットは世界中のアクティブなWorkerすべての間で割り振られます残りの150スロットの75%は、113となります。
    
    
    {  
      "activeUsers":50,
      "globalWorkersActive": 10,
      "dataCenterWorkersActive": 1,
      "trafficHistory": {
        "Mon, 11 Sep 2023 11:44:00 GMT": {
           San Jose: 20/200, // 10%
           London: 30/200, // 15%
           Anywhere: 150/200 // 75%
        }
      }
    }

ステートキーはまた、世界中で湧き出るように発生したWorkerの数（globalWorkersActive）も記録しています。割り当てられたAnywhereスロットは、利用可能であれば世界中のすべてのアクティブWorkerに分配されます。待機室の状態を見ると、globalWorkersActiveは10となっています。つまり、アクティブなWorkerごとに、113÷10≒11人ものユーザーを送ることができます。つまり、Mon, 11 Sep 2023 11:45:00 GMTにWorkerに来た最初の11人のユーザーはオリジンに受け入れられます。余分なユーザーは、キューに入れられます。前述したMon, 11 Sep 2023 11:45: 00 GMTの時点でのサンノゼでの余剰スロット（5）により、サンノゼのWorkerからWebサイトに最大16（5＋11）ユーザを確実に受け入れることができることになります。

## Workerレベルでのキューイングは、データセンターで利用可能なスロットの前にユーザーをキューに入れてしまう可能性があります。

上の例からわかるように、キューに入れるかどうかはWorkerレベルで決まります。世界中のWorkerのもとへ行く新規ユーザーの数は、一様ではありません。トラフィックが2つのWorkerに一様に分配されない場合に起こることの理解のため、下の図を見てください。

サンノゼのデータセンターの空き枠が_10_だとします。サンノゼでは2つのWorkerが稼働しています。_7_人のユーザーがWorker1に行き、_1_人のユーザーがWorker2に行きます。この状況ではWorker1の_7_人のユーザーのうち_5_人をWebサイトに投入し、Workerには_5_枠しかないため、残りの_2_人はキューに入れられます。Worker2に現れた_1_人のユーザーもオリジンに行けます。こうして、実際には_8_人のユーザーしか現れていない中、_10_人のユーザーがサンノゼのデータセンターから送られることが可能であるのに_2_人のユーザをキューに入れることになります。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Side effect of dividing slots at worker level](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4566Q054EWGNADWPDE844M.png&w=715&h=453&f=webp&fit=cover&position=center)

作業員間でスロットを均等に分割するこの問題により、待機室の設定されたトラフィック制限（通常は設定された制限の20～30％以内）より前に待ち行列ができることになります。このアプローチには、次に述べる利点があります。弊社は、この20～30％のキューイング発生頻度を減らし、可能な限り限界に近く引き上げ、Waiting Roomがそれでもトラフィック急増に備えられるよう、アプローチを変更しました。このブログの後半では、スロットの割り当てとカウントの方法を更新することでこれを実現した方法を紹介していきます。

### Workerがこのような決断を下すことにおける利点

上記の例では、サンノゼとデリーのWorkerがユーザーをオリジンに通すかどうか決定する仕組みについて説明しました。Workerレベルで決断を下すことの利点は、リクエストに大きな遅延をもたらすことなく決断を下せる点にあります。常にデータセンターで現在利用可能な状態で作業しているため、決断を下すためにデータセンターから離れる必要なく待機室に関する情報を得ることができるためです。キューイングが始まるのは、Worker内のスロットがなくなった時点です。遅延が加わらないため、顧客はユーザーへの余分な遅延を心配することなく、常に待機室をオンにすることができます。

Waiting Roomの最優先事項は、予期せぬ圧倒的なトラフィックの急増に直面しても、顧客のサイトが常に稼働し続けられるようにすることです。そのためには、待機室がその部屋に対して顧客が設定したトラフィック制限に近い、またはそれ以下にとどまることを優先することが大切になります。世界各地であるデータセンター、たとえばサンノゼでトラフィックの急増が発生した場合、データセンター現地の状態がデリーに届くには、数秒かかります。

Worker間でスロットを分割すると、多少古いデータで作業しても、全体的な上限を影響のある量で超えてしまうことがないようになります。例えば、activeUsersの数がサンノゼのデータセンターでは26で、スパイクが起きているもう一つのデータセンターでは100になることがあります。その時点では、デリーから追加ユーザーを送っても、デリーには全体の余剰分の一部しかないため、全体の上限をそれほどオーバーしません。したがって、全体の上限に達する前にキューに入れることは、全体の上限が尊重されるようにするための設計の一部なのです。次の段落では、トラフィック制限を超過するリスクを増大させることなく、可能な限り制限に近いところでキューに入れるために実装したアプローチについて説明します。

## 待機室の制限に比べトラフィックが少ない場合にスロットを多く割当てる

弊社で真っ先に対処したかったケースは、トラフィックが限界から遠く離れたときに発生するキューイングでした。キューに入れられたエンドユーザーにとってこの状況に直面するのはまれなことであり、通常は1回のリフレッシュ・インターバル（20秒）となるものの、キューイング・アルゴリズムを更新する際の最優先事項箱のことでした。これを解決するために、スロットを割り当てる際に利用率（トラフィックの限界からどれだけ離れているか）を見て、トラフィックが限界から非常に距離が離れている場合はより多くのスロットを割り当てるようにしました。この背景には、より多くのユーザーがオリジンにいるときに、Workerごとで利用可能なスロットを再調整できるようにしながらも、低い制限値で起こるキューイングを防ぎたいとの狙いがありました。

これを理解するために、2つのWorkerにトラフィックが不均一に分配される例をもう一度見てみます。前に説明したのと似たような、2つのWorkerが以下の通りあるとします。この場合、稼働率は低くなっています（10％）。つまり、限界までかなりの余裕があることになります。割り当てられたスロット（8）は、サンノゼデータセンターのslotsAvailableの10に近くなっています。下図を見ればわかるように、Workerのどちらかにアクセスする8人のユーザー全員が、この変更後のスロット割り当てでWebサイトにアクセスできるようになりました。Workerあたりにより多くのスロットを低い利用率で提供していることがその理由です。

下図は、Workerあたり割り当てられるスロットが利用率（限界からどれだけ離れているか）によって変化する様子を示したものです。ここでわかるように、利用率が低いほどWorkerに多くのスロットが割り当てられています。利用率が上がるにつれて、Workerあたり割り当てられるスロットは減少していきます。限界に近づきつつあり、トラフィックの急増に備えることができるためです。利用率10％の場合、すべてのWorkerがデータセンターで利用可能なスロットに近づくことになります。利用率が100％に近くなると、利用可能なスロットをデータセンターのWorker数で割った値に近くなります。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Division of slots among workers at lower utilization](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW493CN0541Y792T082FBHJ8.png&w=715&h=453&f=webp&fit=cover&position=center)

### 低い稼働率でより多くのスロットを達成する方法

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Allotting more slots at lower limits](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45KC4XG240Q6FSQXE6FB1T.png&w=715&h=661&f=webp&fit=cover&position=center)

このセクションでは、目的を達成するための数学について掘り下げていきます。もし詳細に関心がない場合、「過剰プロビジョニングのリスク」の章へとお進みください。

理解を深めるため、デリーデータセンターにリクエストが来る前の例をもう一度見てみましょう。activeUsersの値は50なので、利用率は50÷200で約25%となります。

ここでは、より低い利用レベルでより多くのスロットを割り当てることを目指しています。これにより、トラフィックが上限まで遠く離れている際、顧客が予期せぬキューの挙動に出くわさないようになります。Mon, 11 Sep 2023 11:45:54 GMTの時点で、Delhiへのリクエストは、ローカルのステートキーに基づき、25%の使用率となっています。
    
    
    {
      "activeUsers": 50,
      "globalWorkersActive": 10,
      "dataCenterWorkersActive": 1,
      "trafficHistory": {
        "Mon, 11 Sep 2023 11:44:00 GMT": {
           San Jose: 20/200, // 10%
           London: 30/200, // 15%
           Anywhere: 150/200 // 75%
        }
      }
    }

利用率が低いときに利用できるスロットを増やすことを狙い、利用率に比例して動くworkerMultiplierを追加しました。利用率が低いと倍率は低くなり、利用率が高いと1に近くなります。

utilization - 限界からどれだけ離れているか。
    
    
    workerMultiplier = (utilization)^curveFactor
    adaptedWorkerCount = actualWorkerCount * workerMultiplier

curveFactor - _curveFactor_は調整可能な指数で、Workerのカウントが低いときに、どれだけ積極的に余分な予算を配分するかを決定します。これを理解するために、y = xとy = x^2が値0と1の間でどのように見えるかを示すグラフを見てみましょう。

y=xのグラフは、(0, 0)と(1, 1)を通る直線になります。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Graph for y=x^curveFactor](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW473GSP0VZ963TYQHND0VAD.png&w=715&h=661&f=webp&fit=cover&position=center)

y=x^2 のグラフは、x が< 1 のとき、y が x よりも遅く増加し、(0, 0) と (1, 1) を通る曲線になります

ここで、曲線の仕組みを用い、_y=workerCountMultiplier、x=utilization_の指揮を導き出しました。_curveFactor_は、Workerの数が少ないときにどれだけ積極的に余分な予算を配分するかを決定する調整可能なパワーとなります。curveFactorが1のとき、workerMultiplierは利用率と等しくなります。

前に議論した例に戻り、カーブファクターの値がどうなるか見てみましょう。Mon, 11 Sep 2023 11:45:54 GMTの時点で、デリーへのリクエストはローカルのステートキーに基づき25%の使用率となっています。世界中のあらゆるWorkerがこの余剰分の一部を利用できるので、Anywhereスロットは世界中のすべてのアクティブなWorker、すなわち残りの150スロットの75%に相当する113個で分けられます。

待機室の状態を見ると、globalWorkersActiveは10となっています。この場合、113スロットを10で割るのではなく、調整したWorkerの数であるglobalWorkersActive**×** workerMultiplierのカウントで割ります。curveFactorが1の場合、workerMultiplierは25%または0.25の稼働率に等しくなります。

実質的なWrokerCountは、10 × 0.25 = 2.5 となります。

つまり、アクティブなWorkerは、113÷2.5、つまり約45人のユーザーを送ることができることになります。Mon, 11 Sep 2023 11:45:00 GMTの時点でWorker来た45人のユーザーが、オリジンに受け入れられ、超過したユーザーはキューに入れられます。

したがって、利用率が低い場合（トラフィックが上限まで遠い場合）には、各Workerがさらに多くのスロットを得ることになります。しかし、スロットの合計を合算した場合では、全体の上限を超える可能性が高まります。

### 過剰プロビジョニングのリスク

より低い上限でより多くのスロットをもたらす方法により、トラフィックがトラフィック上限に対して低い場合にキューが発生する可能性を減少させます。ただし、より低い利用率レベルでは、世界中で一様なスパイクが発生し多彩に予想以上に多くのユーザーがオリジンに入る可能性があります。下図は、これが問題となるケースを示しています。ご覧の通り、利用できるデータセンターのスロットは_10_です。前に説明した10%の利用率では、それぞれ_8_つのスロットを持つことができます。あるWorkerに_8_人のユーザーが現れ、別のWorkerに_7_人のユーザーが現れた場合、データセンターで利用可能なスロットは最大_10_個しかないのにも関わらず、_15_人のユーザーをWebサイトに送ることになります。

さまざまな顧客やトラフィックの種類に対応する弊社では、これが問題になるケースを検証することが可能でした。低い利用水準からのトラフィックスパイクは、グローバルでのリミットのオーバーシュートを引き起こす可能性があります。低い制限値で過剰にプロビジョニングしているため、トラフィック制限を大幅に超過するリスクが高まるのがその理由です。交通量が制限に比して少ないときに待ち行列ができる可能性を減らすと同時に、制限を超えないより安全なアプローチを導入する必要がありました。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Risk of over provisioning at lower utilization](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW464DJ7YZVCP2T7F0R4NHWE.png&w=715&h=453&f=webp&fit=cover&position=center)

少し戻って弊社のアプローチについて考えてみると、データセンター内のトラフィックは、データセンター内に見られるWorkerの数に直接相関することを前提としていました。実際には、これはすべての顧客に当てはまるわけではないことがわかったのです。たとえトラフィックがWorkerの数と相関していたとしても、データセンターのWorkerに向かう新規ユーザーは相関しないかもしれないのです。というのも、弊社が割り当てるスロットは新規ユーザーのためのものであるものの、データセンターが目にするトラフィックは、すでにWebサイトにアクセスしているユーザーとWebサイトにアクセスしようとする新規ユーザーの両方で構成されているためです。

次のセクションでは、Workerの数を用いず、代わりにWorkerがデータセンター内の他のWorkerと通信するアプローチについてお話しします。これに際し、弊社ではDurable Objectカウンターという新しいサービスを導入しました。

## データセンターカウンターを導入することで、スロット分割回数を減らす

上記の例から、Workerレベルでのオーバープロビジョニングは、データセンターに割り当てられている以上のスロットを使用するリスクがあることがわかりました。低レベルで過剰供給しなければ、最初に説明したように、設定された上限に達する前にユーザーがキューに入るリスクがあります。この両方を達成できる解決策が必要となります。

オーバープロビジョニングは、不均等な数の新規ユーザーがWorkerに達した際、Workerがすぐにスロットを使い果たさないようにするために行われていました。データセンター内の2つのWorker間での通信方法があれば、データセンター内のWorker間でスロットを分ける必要はありません。その通信を実現するため、カウンターを導入しました。カウンターは、データセンター内のWorkerをカウントする、一群の小型のdurable objectです。

Workerカウントが使用されることを回避するに当たりどのように役立つかを理解するため、下図を見てみましょう。下の_データセンターカウンター_には2つのWorkerが通信しています。先ほど説明したように、Workerは待機室の状態に基づいてユーザーをWebサイトに通しています。この際、通過させたユーザーの数はWorkerのメモリに保存されます。カウンターを導入することで、これが_データセンターカウンター_で行われるようになります。新しいユーザーがWorkerに要求を出すたびに、Workerはカウンターに通信し、カウンターの現在値を知ることになります。以下の例では、Workerに対する最初の新しいリクエストに対し、受信したカウンターの値は9となっています。データセンターに10スロットの空きがある場合、そのユーザーはWebサイトにアクセスできることになります。次のWorkerが新しいユーザーを受信し、その直後にリクエストした場合10の値が得られ、Workerの利用可能なスロット数に基づきユーザーがキューに入れられようになります。

_データセンターカウンター_は、待機室のWorkerの同期ポイントとして機能すします。基本的に、これはWorker同士が直接通信することなくやり取りできるようにするものです。発券カウンターの仕組みに似ています。あるWorkerが誰かを入場させるたびに、カウンターからチケットを要求します。そのため、別のWorkerがカウンターからチケットを要求しても、同じチケット番号を得ることはない。チケットの持つ価値が有効であれば、新しいユーザーはWebサイトに行くことができます。そのため、Workerに異なる数の新規ユーザーが現れても、データセンター用のカウンターが使用スロット数を計算するため、Workerに対し過剰に割り当てたり、不足したりすることは起こりません。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Counters helping workers communicate with each other](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49MAB046HP7KBZWSNN02TT.png&w=715&h=523&f=webp&fit=cover&position=center)

下図は、Workerに届く新規ユーザーの数が不均等な場合の動作を示したものです。1つは_7_人の新規ユーザーを獲得し、もう1つのWorker は_1_人の新規ユーザーを獲得します。下図のWorkerに現れた_8_人のユーザーは、データセンターで利用可能なスロットが_10_であり、_10_を下回っているため、すべてWebサイトにアクセスできます。

カウンターの値がデータセンターのslotsAvailableと等しい場合は余分なユーザーを送らないため、これも余分なユーザーをWebサイトに送る原因とはなりません。下図のWorkerに現れた_15_人のユーザーのうち、_10_人がWebサイトにアクセスし、_5_人がキューに入れられることになります。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Uneven number of requests to workers does not cause queueing](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49DZCMXWDQ58PNXWYJSRCA.png&w=715&h=453&f=webp&fit=cover&position=center)

カウンターがWorker同士の意思疎通を助けるため、稼働率が低くても過剰なプロビジョニングを行うリスクは発生しません。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2026 Embedded Image - yq9u67](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48R4F31G3TC7X9GY5WM3KQ.png&w=715&h=453&f=webp&fit=cover&position=center)

これをさらに理解するために、先に説明した例に戻り、実際の待機室状態でどのように機能するかを見てみましょう。

顧客の待機室の状態は、以下の通りとなっています。

状況からのこの情報を使う必要がないように、労働者間で枠を分けないことが目的となります。Mon, 11 Sep 2023 11:45:54 GMTの時点で、サンノゼにリクエストが来ています。つまり、サンノゼから送れる枠は150のうち10%の15となります。
    
    
    {  
      "activeUsers": 50,
      "globalWorkersActive": 10,
      "dataCenterWorkersActive": 3,
      "trafficHistory": {
        "Mon, 11 Sep 2023 11:44:00 GMT": {
           San Jose: 20/200, // 10%
           London: 30/200, // 15%
           Anywhere: 150/200 // 75%
        }
      }
    }

サンノゼのDurable Objectカウンターは、データセンターに新しいユーザーが来るたびに、その時点のカウンターの値を返し続けます。Workerに戻った後、値を1増やします。つまり、Workerに最初に来た15人の新規ユーザーは、ユニークなカウンターの値を得ることになります。したがって、あるユーザーの受信値が15未満の場合、そのユーザーはデータセンターのスロットを使用することができることになります。

データセンターで利用可能なスロットがなくなると、ユーザーはAnywhereデータセンターに割り当てられたスロットを利用することができます。サンノゼのWorkerのチケットの値が15となった時点で、サンノゼのスロットを使ってWebサイトにアクセスすることは不可能だとわかります。

Anywhereスロットは、地球上のすべてのアクティブなWorker、つまり残りの150スロットの75％に相当する113か所で利用できます。AnywhereスロットはDurable Objectによって処理され、異なるデータセンターのWorkerがAnywhereスロットを使用したいときに通信できます。128人（113人＋15人）のユーザーがこの顧客の同じWorkerに殺到した場合でさえ、キューに入れることはありません。これにより、世界中のWorkerに向かう新規ユーザーの数が不均等でも待機室が処理できるようになり、その結果、顧客が設定された上限に近い数までキューに入れられるようになります。

### カウンターが発揮する威力

弊社が待機室を構築したとき、Webサイトへのエントリーの決定は、リクエストがWebサイトに対し実行されているときに他のサービスと通信することなく、Worker自体のレベルで行われるようにした糸感が手ました。ユーザーのリクエストに遅延が加わるのを避けるために、これが必要だったのです。耐久性のあるオブジェクトカウンターに同期ポイントを導入することは、Durable Objectカウンターへの呼び出しを導入することになり、それから逸脱していることになります。

しかし、データセンターのDurable Objectは同じデータセンター内に留まります。このため、追加で発生する遅延は最小となり、通常は10 ms未満となります。Anywhereデータセンターを処理するDurable Objectへの呼び出しの場合、Workerは海を渡ったり長距離を横断したりする必要があります。このような場合、遅延は約60msまたは70msになる可能性があります。より遠距離のデータセンターに向かうコールのため、以下に示す95パーセンタイルの値はより高くなります。

設計上カウンターを追加するとの決断は、Webサイトに初めてアクセスするユーザーにとって、若干の余分な遅延が発生することになります。上限に達する前にキューに入れられるユーザー数を減らすことができるため、トレードオフは許容範囲と判断しました。さらに、カウンターは新規ユーザーがWebサイトに入ろうとするときにのみ必要となります。新規の利用者がオリジンに到達すると、Workerから直接、入ることを許可されます。入場の証明は利用者が持ってきたクッキーに記載されているため、これをもとに入場を許可できます。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Graph showing percentile distribution of counter latencies from our production dashboard](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47CKWXRKRVYN9H44AMMH6P.png&w=715&h=307&f=webp&fit=cover&position=center)

カウンターは至極シンプルなサービスであり、単純なカウントを行う以外、他には何もしません。これにより、カウンターのメモリとCPUフットプリントは非常に小さくなります。さらに、弊社は世界中に多くのカウンターを配置し、Workerのサブセット間の調整を処理しています。これにより、Workerからの同期要求の負荷をカウンターがうまく処理できます。これらの要素が積み重なり、カウンターは弊社のユースケースにとって実行可能なソリューションとなったのです。

## まとめ

Waiting Roomは、合法的なトラフィックの量や急増に関係なく、顧客のサイトを確実に稼働させることを第一に考えて設計しています。Waiting Roomは、100カ国300以上の都市にまたがるCloudflareのネットワーク内のすべてのサーバーで稼働しています。弊社は、すべての新規ユーザーに対して、Webサイトに行くかキューに行くかの決定を、最小限の遅延で適切なタイミングにて行えるようにしたいと考えています。データセンターであまり早くキューイングすると、顧客が設定した上限よりも早くキューイングしてしまう可能性があるため、この判断は難しくなります。キューイングが遅すぎると、顧客が設定したリミットをオーバーシュートしてしまう可能性があります。

弊社の当初のアプローチでは、Workerに均等に枠を割り振っていたためキューに入れるのが早すぎることもあったものの、顧客が設定した上限の尊重においてはかなり優れた結果が得られました。次のアプローチでは、利用率が低いとき（顧客の制限に比べトラフィックレベルが低いとき）により多くのスロットを与えることにより、顧客の設定した上限よりも早くキューに入れたケースでもWorkerの各スロットがより多く使えるため、さらに優れた結果が得られました。しかしこれまで見てきたように、利用率が低い期間が続いた後に突然トラフィックが急増した場合、オーバーシュートする可能性が高くなりました。

カウンターを使えば、Worker カウントによるスロットの分割を避けることができ、両者の長所を得ることができます。カウンターの使用により、顧客が設定した上限に基づき、早すぎたり遅すぎたりすることなくキューを設けることができます。新しいユーザーからのリクエストに対しわずかな遅延の犠牲を払うことになるものの、それはごくわずかであり、早くからキューに入れられるよりも優れたユーザーエクスペリエンスを生み出すことがわかりました。

弊社は、常に適切なタイミングでユーザーをキューイングし、何よりも顧客のWebサイトを保護するため、このアプローチを反復し続けていきます。より多くの顧客がWaiting Roomを利用するにつれ、弊社はさまざまなトラフィックのタイプについてより多くのことを学んでおり、あらゆる方面にとってより優れた製品の構築に役立っています。

このページ

オンラインで議論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fhow-waiting-room-queues%2F&t=Cloudflare%E3%81%AE%E9%AB%98%E5%BA%A6%E3%81%AB%E5%88%86%E6%95%A3%E3%81%95%E3%82%8C%E3%81%9F%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E4%B8%8A%E3%81%A7%E3%81%AE%E3%80%81Waiting%20Room%E3%81%AB%E3%82%88%E3%82%8B%E3%82%AD%E3%83%A5%E3%83%BC%E3%82%A4%E3%83%B3%E3%82%B0%E6%B1%BA%E5%AE%9A%E3%81%AE%E6%A7%98%E5%AD%90)[](https://x.com/intent/post?text=Cloudflare%E3%81%AE%E9%AB%98%E5%BA%A6%E3%81%AB%E5%88%86%E6%95%A3%E3%81%95%E3%82%8C%E3%81%9F%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E4%B8%8A%E3%81%A7%E3%81%AE%E3%80%81Waiting+Room%E3%81%AB%E3%82%88%E3%82%8B%E3%82%AD%E3%83%A5%E3%83%BC%E3%82%A4%E3%83%B3%E3%82%B0%E6%B1%BA%E5%AE%9A%E3%81%AE%E6%A7%98%E5%AD%90&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fhow-waiting-room-queues%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fhow-waiting-room-queues%2F)[](https://bsky.app/intent/compose?text=Cloudflare%E3%81%AE%E9%AB%98%E5%BA%A6%E3%81%AB%E5%88%86%E6%95%A3%E3%81%95%E3%82%8C%E3%81%9F%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E4%B8%8A%E3%81%A7%E3%81%AE%E3%80%81Waiting+Room%E3%81%AB%E3%82%88%E3%82%8B%E3%82%AD%E3%83%A5%E3%83%BC%E3%82%A4%E3%83%B3%E3%82%B0%E6%B1%BA%E5%AE%9A%E3%81%AE%E6%A7%98%E5%AD%90+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fhow-waiting-room-queues%2F)[](https://mastodonshare.com/?text=Cloudflare%E3%81%AE%E9%AB%98%E5%BA%A6%E3%81%AB%E5%88%86%E6%95%A3%E3%81%95%E3%82%8C%E3%81%9F%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E4%B8%8A%E3%81%A7%E3%81%AE%E3%80%81Waiting+Room%E3%81%AB%E3%82%88%E3%82%8B%E3%82%AD%E3%83%A5%E3%83%BC%E3%82%A4%E3%83%B3%E3%82%B0%E6%B1%BA%E5%AE%9A%E3%81%AE%E6%A7%98%E5%AD%90&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fhow-waiting-room-queues%2F)[](https://www.threads.net/intent/post?text=Cloudflare%E3%81%AE%E9%AB%98%E5%BA%A6%E3%81%AB%E5%88%86%E6%95%A3%E3%81%95%E3%82%8C%E3%81%9F%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E4%B8%8A%E3%81%A7%E3%81%AE%E3%80%81Waiting+Room%E3%81%AB%E3%82%88%E3%82%8B%E3%82%AD%E3%83%A5%E3%83%BC%E3%82%A4%E3%83%B3%E3%82%B0%E6%B1%BA%E5%AE%9A%E3%81%AE%E6%A7%98%E5%AD%90+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fhow-waiting-room-queues%2F)

## 関連するタグ

[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[Durable Objects](https://blog.cloudflare.com/ja-jp/tag/durable-objects/)[Waiting Room](https://blog.cloudflare.com/ja-jp/tag/waiting-room/)[ネットワーク](https://blog.cloudflare.com/ja-jp/tag/network/)[開発者](https://blog.cloudflare.com/ja-jp/tag/developers/)[開発者プラットフォーム](https://blog.cloudflare.com/ja-jp/tag/developer-platform/)

SNS をフォロー

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 新しい投稿のお知らせを受け取るように登録する

メールアドレス

また、あなたのメールアドレスを共有したりすることはございません。

登録する

ご購読ありがとうございます！受信箱を確認して登録してください。
