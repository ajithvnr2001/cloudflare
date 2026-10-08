---
url: https://blog.cloudflare.com/ja-jp/making-super-slurper-five-times-faster/
title: Workers\u3001Durable Objects\u3001Queues\u306b\u3088\u308a\u3001Super Slurper\u30925\u500d\u9ad8\u901f\u5316 | Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:41:01.692379+00:00
---

# Workers、Durable Objects、Queuesにより、Super Slurperを5倍高速化 | Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/making-super-slurper-five-times-faster/

[ブログ](https://blog.cloudflare.com/ja-jp/)

[Cloudflare Queues](https://blog.cloudflare.com/ja-jp/tag/cloudflare-queues/)[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[Developer Week](https://blog.cloudflare.com/ja-jp/tag/developer-week/)4件4件タグを表示

7 タグタグを7件表示

  * 投稿タグ
  * [Cloudflare Queues](https://blog.cloudflare.com/ja-jp/tag/cloudflare-queues/)[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[Developer Week](https://blog.cloudflare.com/ja-jp/tag/developer-week/)[Durable Objects](https://blog.cloudflare.com/ja-jp/tag/durable-objects/)[R2](https://blog.cloudflare.com/ja-jp/tag/r2/)[R2 Super Slurper](https://blog.cloudflare.com/ja-jp/tag/r2-super-slurper/)[キュー](https://blog.cloudflare.com/ja-jp/tag/queues/)
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



[Durable Objects](https://blog.cloudflare.com/ja-jp/tag/durable-objects/)[R2](https://blog.cloudflare.com/ja-jp/tag/r2/)[R2 Super Slurper](https://blog.cloudflare.com/ja-jp/tag/r2-super-slurper/)[キュー](https://blog.cloudflare.com/ja-jp/tag/queues/)

[Cloudflare Queues](https://blog.cloudflare.com/ja-jp/tag/cloudflare-queues/)[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[Developer Week](https://blog.cloudflare.com/ja-jp/tag/developer-week/)[Durable Objects](https://blog.cloudflare.com/ja-jp/tag/durable-objects/)[R2](https://blog.cloudflare.com/ja-jp/tag/r2/)[R2 Super Slurper](https://blog.cloudflare.com/ja-jp/tag/r2-super-slurper/)[キュー](https://blog.cloudflare.com/ja-jp/tag/queues/)

2025年4月10日

# Workers、Durable Objects、Queuesにより、Super Slurperを5倍高速化

![Connor Maddox](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44GJCDNCNMKRFZB06B4MZ6.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Siddhant Sinha](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44XJ1R2S5DZS8B6TDZBZ25.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Prasanna Sai Puvvada](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44SJHBSH635BDQ2W9VQA8G.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Connor Maddox](https://blog.cloudflare.com/ja-jp/author/connor-maddox/)、[Siddhant Sinha](https://blog.cloudflare.com/ja-jp/author/siddhant/)、[Prasanna Sai Puvvada](https://blog.cloudflare.com/ja-jp/author/prasanna-sai-puvvada/)

13分で読了

URLをコピー

この記事は以下でも利用可能です [English](https://blog.cloudflare.com/making-super-slurper-five-times-faster/)、[Deutsch](https://blog.cloudflare.com/de-de/making-super-slurper-five-times-faster/)、[Español](https://blog.cloudflare.com/es-es/making-super-slurper-five-times-faster/)、[Français](https://blog.cloudflare.com/fr-fr/making-super-slurper-five-times-faster/)、[한국어](https://blog.cloudflare.com/ko-kr/making-super-slurper-five-times-faster/)、[繁體中文](https://blog.cloudflare.com/zh-tw/making-super-slurper-five-times-faster/)、[简体中文](https://blog.cloudflare.com/zh-cn/making-super-slurper-five-times-faster/).

![BLOG-2731 Feature Image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49756SEE9TPQPR5FT8SAFG.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///////85OjwydfryNrx2eb36u308ezr///////+3+byvtHtu9Pz0eL65u338e7t////////3OX2tM7xr8/3yuD+5e378/Hx////////3+n7ttH2sdL8y+P/5/H/9vX2////////6fH/xtz7wt3/1+v/7vf/+/r7////////9fv/3Ov/2ev/6Pb/+P7/////////////////7vf/6/f/9f7/////////////////////9Pv/8vv/+///////////)

[_Super Slurper_](https://developers.cloudflare.com/r2/data-migration/super-slurper/)は、クラウドオブジェクトストレージプロバイダーと[ _Cloudflare R2_](https://developers.cloudflare.com/r2/)間の大規模なデータ転送を簡単に行うために設計された、Cloudflareのデータ移行ツールです。ローンチ以来、何千もの開発者がSuper Slurperを使って、AWS S3、Google Cloud Storage、[ _その他のS3互換サービス_](https://developers.cloudflare.com/r2/data-migration/super-slurper/#supported-cloud-storage-providers)からR2へ、数ペタバイトに及ぶデータを移行してきました。

しかし、当社は移行をさらに高速化する機会を見出しました。Cloudflareの開発者プラットフォームを使い、[ _Cloudflare Workers_](https://developers.cloudflare.com/workers/)、[ _Durable Objects_](https://developers.cloudflare.com/durable-objects/)、[ _Queues_](https://developers.cloudflare.com/queues/)を土台としてSuper Slurperのアーキテクチャを一から再構築し、転送速度を最大5倍に上げました。この記事では、オリジナルのアーキテクチャ、特定されたパフォーマンスのボトルネック、その解決方法、それらの改善が実世界にもたらす影響について掘り下げます。

## 当初のアーキテクチャとパフォーマンスのボトルネック

Super Slurperは当初、[ _SourcingKit_](https://developers.cloudflare.com/images/upload-images/sourcing-kit/)とアーキテクチャを共有していました。SourcingKitは、AWS S3から[ _Cloudflare Images_](https://developers.cloudflare.com/images/)へ画像を一括インポートするために構築されたツールです。SourcingKitはKubernetes上にデプロイされ、[ _Images_](https://developers.cloudflare.com/images/)サービスと共に稼働しました。当社はSuper Slurperの構築を始めた時に、Super Slurperを独自のKubernetesネームスペースに分割し、いくつかの新しいAPIを導入して、オブジェクトストレージのユースケースで使いやすくしました。このセットアップはうまく機能し、何千人もの開発者がR2へデータを移行するのに役に立ちました。

しかし、課題がなかったわけではありません。SourcingKitは、ペタバイト級の大容量転送に必要なスケールを処理するように設計されていませんでした。SourcingKitもSuper Slurperも、当社のコアデータセンターの1つにあるKubernetesクラスタ上で稼働していました。つまり、計算リソースと帯域幅をCloudflareのコントロールプレーン、分析、その他のサービスと共用しなければならなかったのです。こうしたリソースの制約は、移行件数が増えるにつれて明らかなボトルネックになりました。

オブジェクトストレージプロバイダー間でデータを転送するサービスの場合、ジョブはシンプルです。ソースからオブジェクトをリスト化し、宛先にコピーし、それを繰り返すだけです。これがまさに当初のSuper Slurperの仕組みです。ソースバケットからオブジェクトをリスト化し、そのリストをPostgresベースのキュー（`pg_queue`）へプッシュし、このキューから一定のペースでオブジェクトをコピーしていました。オブジェクトストレージ移行の規模を考えると、必然的に帯域幅の使用量が高くなる傾向にありました。そのため、スケーリングが困難でした。

当社のコアデータセンターだけでは帯域幅の制約があったため、それに対処するために[ _Cloudflare Workers_](https://developers.cloudflare.com/workers/)を導入しました。コアデータセンターでデータのコピーを処理するのではなく、Workerを呼び出して実際のコピーを行うようにしたのです：

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2731 Image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44D530YYFHF6VPDT2G2NT5.png&w=715&h=498&f=webp&fit=cover&position=center)

Super Slurperの利用が増えるにつれて、Kubernetesリソースの消費量も増加しました。データ転送中のかなりの時間が、計算集約型のタスクの実行にではなく、ネットワークI/Oやストレージを待つのに費やされていました。そこで必要だったのはメモリやCPUの増設ではなく、コンカレンシーを高めることだったのです。

レプリカの数を増やし続けて需要に対応しましたが、終いには壁に突き当たりました。問題はスケーラビリティでした。数十ポッドで稼働していましたが、それを数桁上回る規模が必要だったのです。

私たちは、継承したアーキテクチャに依拠するのではなく、第一原理からアプローチ全体を再考することにしました。[ _Cloudflare Workers_](https://developers.cloudflare.com/workers/)、[ _Durable Objects_](https://developers.cloudflare.com/durable-objects/)、[ _Queuesを使った大まかな概念実証を一週間ほどで作成しました。_](https://developers.cloudflare.com/queues/)ソースバケットからオブジェクトをリスト化し、キューへプッシュし、キューからメッセージを消費して転送を開始しました。最初の実装の仕組みとよく似ているように聞こえますが、Cloudflareの開発者プラットフォーム上で構築したことにより、以前より数桁大きな規模の自動スケーリングが可能になりました。

  * **Cloudflare Queues** ：非同期的なオブジェクト転送と、移行するオブジェクトの数に合わせた自動スケーリングが可能です。
  * **Cloudflare Workers** ：Kubernetesのオーバーヘッドなしで軽量の計算タスクを実行し、プロセスの各部分の実行場所を最適化することで、遅延を短縮し、パフォーマンスを向上させます。
  * **SQLiteベースのDurable Objects（DO）** ：完全に分散されたデータベースとして機能し、単一のPostgreSQLインスタンスの制限を排除します。
  * **Hyperdrive** ：オリジナルのPostgreSQLデータベースからジョブ履歴に高速アクセスし、アーカイブストアとして保持します。



いくつかのテストを実施した結果、小規模な転送（数百のオブジェクト）では、概念実証のスピードが当初の実装よりも遅いことがわかりました。しかし、転送が数百万オブジェクトにスケールアップすると、当初実装のパフォーマンスに匹敵するレベルに達し、最終的にはそれを上回りました。これこそ、当社が概念実証から本番環境への移行に時間を投資する必要があるというサインでした。

当社は概念実証のハックを取り除き、安定性の確保に取り組み、転送をさらに高いコンカレンシーに拡張する新しい方法を見つけました。数回のイテレーションの後に、満足のいくものにたどり着きました。

## 新しいアーキテクチャ： Workers、Queues、Durable Objects

#### 処理層：移行フローの管理

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2731 Image 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49GAXDNPXMT21H1Q8CNN7M.png&w=715&h=251&f=webp&fit=cover&position=center)

処理層の中心となるのは、**キュー、コンシューマー、ワーカー** です。プロセスは次のようになります：

#### 移行を開始

クライアントが移行をトリガーする際は、当社の**API Worker** にリクエストが送信されることから始まります。このワーカーは移行の詳細を取得してデータベースに保存し、**List Queue** にメッセージを追加してプロセスを開始します。

#### ソースバケットオブジェクトのリスト

事が速く進み始めるのは**List Queue Consumer** においてです。List Queue Consumerはキューからメッセージをプルし、ソースバケットからオブジェクトリストを取得し、必要なフィルタを適用し、重要なメタデータをデータベースに保存します。次に、オブジェクト転送メッセージを **Transfer Queue** のキューに入れることにより、新しいタスクを作成します。

新しい作業のバッチをすぐにキューに入れ、コンカレンシー（同時実行数）を最大化します。スロットリングメカニズムが組み込まれており、依存関係するシステムがダウンするなどの予期せぬ障害が発生した時にキューにメッセージを追加できなくなっています。これにより、障害中も安定性を維持し過負荷を防ぐことができます。

#### 効率的なオブジェクト転送

**Transfer Queue Consumer** Workersは、オブジェクト転送メッセージをキューからプルし、データベースのオブジェクトキーをロックすることによって、各オブジェクトが一度だけ処理されるようにします。転送が終了するとオブジェクトのロックは解除されます。大きなオブジェクトの場合は管理可能なチャンクに分割し、マルチパートアップロードとして転送します。

#### スムーズな障害対応

どの分散システムでも障害は避けられず、確実な対応をする必要がありました。一時的な障害が発生した場合の自動リトライを実装したため、問題によって移行の流れが妨げられることはありません。しかし、リトライで解決できない場合は、メッセージは**Dead Letter Queue（DLQ）** に送られ、そこで後のレビューと解決のために記録されます。

#### ジョブ完了とライフサイクル管理

すべてのオブジェクトがリストにされ、転送が進行中になると、**Lifecycle Queue Consumer** はすべてを監視します。進行中の転送を監視し、オブジェクトが取り残されないようにします。すべての転送が完了すると、ジョブが完了とマークされ、移行プロセスが終了します。

### データベース層：耐久性の高いストレージとレガシーデータの取得

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2731 Image 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46PPCT7KRZD27PS744HKQT.png&w=715&h=479&f=webp&fit=cover&position=center)

私たちは新しいアーキテクチャを構築するにあたり、膨大なデータセットを処理できてジョブ履歴の取得が可能な堅牢なソリューションが必要であることを認識していました。そこで使ったのが**Durable Objects（DO）** と**Hyperdrive** の組み合わせです。

#### Durable Objects

移行ジョブを追跡するため、各アカウントに専用のDurable Objectを与えました。各**ジョブのDO** には、バケット名、ユーザーオプション、ジョブの状態などの重要な詳細が保存されます。これにより、すべてが整理され、簡単に管理できるようになりました。また、大規模な移行をサポートするために、転送のためにキューに入れられたすべてのオブジェクトを管理し、転送状態、オブジェクトキー、追加のメタデータを保存する**Batch DO** も追加しました。

移行が**数十億ものオブジェクト** にスケールアップしたため、ストレージに関してもクリエイティブになる必要がありました。リクエストの負荷を分散するシャーディング戦略を実装してボトルネックを防止し、**SQLite DOの10 GB** のストレージ制限を回避しました。オブジェクトが転送されると、その詳細をクリーンアップし、その過程でストレージスペースを最適化します。10億のオブジェクトキーの保存に、びっくりするほどのストレージが必要なのです。

#### Hyperdrive

何年もの移行履歴のあるシステムの再構築でしたので、過去の移行の詳細をすべて保存し、アクセス可能にする方法が必要でした。Hyperdriveは、レガシーシステムへのブリッジとして機能し、当社のコア**PostgreSQL** データベースからジョブ履歴をシームレスに取得することを可能にします。これは単なるデータ検索メカニズムではなく、複雑な移行シナリオのためのアーカイブです。

## 結果：Super Slurperは最大5倍の速さでR2へデータを転送

結局、データ転送を高速化するという目標は実際に達成できたのでしょうか？

AWS S3からR2へ75,000個のオブジェクトを移行するテストを実施しました。前の実装では転送に15分30秒かかりました。パフォーマンス改善の後は、同じ移行がわずか3分25秒で完了しました。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2731 Image 4](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW477CPDAB1K3Y0SNDE0Z0SJ.png&w=715&h=360&f=webp&fit=cover&position=center)

2月に新サービスを利用した本番移行がスタートした時、特にオブジェクトサイズの分布によって、さらに大きな改善が見られたケースもありました。Super Slurperは[ _約2年前_](https://blog.cloudflare.com/r2-super-slurper-ga/)からありますが、パフォーマンスが向上し、より多くのデータを移行できるようになりました。Super Slurperがコピーした全オブジェクトの35%が、ここ2か月の移行です。

## 課題

新しいアーキテクチャの最大の課題の1つは、重複メッセージの処理でした。重複が発生する可能性はいくつかあります：

  * Queuesは少なくとも1回の配信を行います。つまり、配信を保証するために、コンシューマーは同じメッセージを複数回受信する場合があるということです。
  * 失敗と再試行で、明らかな重複が発生する場合があります。例えば、オブジェクトが既に転送された後にDurable Objectへのリクエストが失敗した場合、リトライで同じオブジェクトが再処理される可能性があります。



正しく処理されないと、同じオブジェクトが複数回転送されることになります。これを解決するために、各オブジェクトが正確に記録され、転送が一度だけ行われるようにするいくつかの戦略を実装しました：

  1. リストは順次処理されるため（例えば、オブジェクト2の取得にはオブジェクト1のリストからの継続トークンが必要）、各リスト化操作にシークエンスIDを割り当てています。これにより、重複するリストを検出し、複数のプロセスが同時に開始されることを防げます。データベースやキューの操作完了を待たずとも次のバッチをリスト化できるため、特に有用です。リスト2が失敗すれば再試行できます。リスト3が既に開始されている場合は、不要な再試行を省くことができます。
  2. 転送が開始されると各オブジェクトはロックされ、同じオブジェクトの並列転送を防ぎます。転送が正常に完了すると、データベースからそのオブジェクトのキーを削除することでロックが解除されます。そのオブジェクトのメッセージが後で再び表示されたとしても、キーがもはや存在しなければ、既に転送されたと考えて大丈夫です。
  3. カウントの正確性の維持は、データベースのトランザクションに依存しています。オブジェクトがロック解除されなければ、カウントは変わりません。同様に、データベースへのオブジェクトキー追加が失敗すればカウントは更新されず、操作は後で再試行されます。
  4. 最後の安全策として、オブジェクトが既にターゲットバケットに存在し、移行開始後に公開されたことを確認します。確認できれば、当社のプロセス（または別のプロセス）によって転送されたと想定し、スキップします。



![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2731 Image 5](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44AHGCDWRPKVF577ESK4QA.png&w=715&h=228&f=webp&fit=cover&position=center)

## Super Slurperの今後の展開は？

私たちは、Super Slurperをより速く、よりスケーラブルにし、さらに使いやすくする方法を常に模索しています。今回の改善はほんの始まりに過ぎません。

  * 当社は最近、どの[ _S3互換ストレージプロバイダー_](https://developers.cloudflare.com/changelog/2025-02-24-r2-super-slurper-s3-compatible-support/)からでも移行できる機能をローンチしました！
  * データ移行は、現在のところアカウントあたり同時移行3回に制限されていますが、この制限を引き上げたいと考えています。それにより、オブジェクトのプレフィックスを別の移行に分割して並列処理することができ、バケットの移行速度を大幅に向上させることができます。Super Slurperの詳細と既存のオブジェクトストレージからR2へのデータ移行の方法については、当社の[ _ドキュメント_](https://developers.cloudflare.com/r2/data-migration/super-slurper/)をご覧ください。



P.S.今回のアップデートの一環として、APIとのやり取りを簡素化したため、移行を[ _プログラムで管理_](https://developers.cloudflare.com/api/resources/r2/subresources/super_slurper/)できるようになりました！

このページ

オンラインで議論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fmaking-super-slurper-five-times-faster%2F&t=Workers%E3%80%81Durable%20Objects%E3%80%81Queues%E3%81%AB%E3%82%88%E3%82%8A%E3%80%81Super%20Slurper%E3%82%925%E5%80%8D%E9%AB%98%E9%80%9F%E5%8C%96)[](https://x.com/intent/post?text=Workers%E3%80%81Durable+Objects%E3%80%81Queues%E3%81%AB%E3%82%88%E3%82%8A%E3%80%81Super+Slurper%E3%82%925%E5%80%8D%E9%AB%98%E9%80%9F%E5%8C%96&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fmaking-super-slurper-five-times-faster%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fmaking-super-slurper-five-times-faster%2F)[](https://bsky.app/intent/compose?text=Workers%E3%80%81Durable+Objects%E3%80%81Queues%E3%81%AB%E3%82%88%E3%82%8A%E3%80%81Super+Slurper%E3%82%925%E5%80%8D%E9%AB%98%E9%80%9F%E5%8C%96+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fmaking-super-slurper-five-times-faster%2F)[](https://mastodonshare.com/?text=Workers%E3%80%81Durable+Objects%E3%80%81Queues%E3%81%AB%E3%82%88%E3%82%8A%E3%80%81Super+Slurper%E3%82%925%E5%80%8D%E9%AB%98%E9%80%9F%E5%8C%96&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fmaking-super-slurper-five-times-faster%2F)[](https://www.threads.net/intent/post?text=Workers%E3%80%81Durable+Objects%E3%80%81Queues%E3%81%AB%E3%82%88%E3%82%8A%E3%80%81Super+Slurper%E3%82%925%E5%80%8D%E9%AB%98%E9%80%9F%E5%8C%96+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fmaking-super-slurper-five-times-faster%2F)

## 関連するタグ

[Cloudflare Queues](https://blog.cloudflare.com/ja-jp/tag/cloudflare-queues/)[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[Developer Week](https://blog.cloudflare.com/ja-jp/tag/developer-week/)[Durable Objects](https://blog.cloudflare.com/ja-jp/tag/durable-objects/)[R2](https://blog.cloudflare.com/ja-jp/tag/r2/)[R2 Super Slurper](https://blog.cloudflare.com/ja-jp/tag/r2-super-slurper/)[キュー](https://blog.cloudflare.com/ja-jp/tag/queues/)

SNS をフォロー

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 新しい投稿のお知らせを受け取るように登録する

メールアドレス

また、あなたのメールアドレスを共有したりすることはございません。

登録する

ご購読ありがとうございます！受信箱を確認して登録してください。
