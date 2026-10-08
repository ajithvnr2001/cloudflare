---
url: https://blog.cloudflare.com/ja-jp/quic-death-spiral-fix/
title: \u300cidle\u300d\u304c\u30a2\u30a4\u30c9\u30eb\u3067\u306f\u306a\u3044\u5834\u5408\uff1aLinux\u30ab\u30fc\u30cd\u30eb\u306e\u6700\u9069\u5316\u304cQUIC\u30d0\u30b0\u306b\u306a\u3063\u305f\u7d4c\u7def | Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:46:37.912919+00:00
---

# 「idle」がアイドルではない場合：Linuxカーネルの最適化がQUICバグになった経緯 | Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/quic-death-spiral-fix/

[ブログ](https://blog.cloudflare.com/ja-jp/)

[HTTP3](https://blog.cloudflare.com/ja-jp/tag/http3/)[QUIC](https://blog.cloudflare.com/ja-jp/tag/quiche/)[QUIC](https://blog.cloudflare.com/ja-jp/tag/quic/)4件4件タグを表示

7 タグタグを7件表示

  * 投稿タグ
  * [HTTP3](https://blog.cloudflare.com/ja-jp/tag/http3/)[QUIC](https://blog.cloudflare.com/ja-jp/tag/quiche/)[QUIC](https://blog.cloudflare.com/ja-jp/tag/quic/)[Rust](https://blog.cloudflare.com/ja-jp/tag/rust/)[デバッグ](https://blog.cloudflare.com/ja-jp/tag/debugging/)[ネットワーキング](https://blog.cloudflare.com/ja-jp/tag/networking/)[輻輳制御](https://blog.cloudflare.com/ja-jp/tag/congestion-control/)
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



[Rust](https://blog.cloudflare.com/ja-jp/tag/rust/)[デバッグ](https://blog.cloudflare.com/ja-jp/tag/debugging/)[ネットワーキング](https://blog.cloudflare.com/ja-jp/tag/networking/)[輻輳制御](https://blog.cloudflare.com/ja-jp/tag/congestion-control/)

[HTTP3](https://blog.cloudflare.com/ja-jp/tag/http3/)[QUIC](https://blog.cloudflare.com/ja-jp/tag/quiche/)[QUIC](https://blog.cloudflare.com/ja-jp/tag/quic/)[Rust](https://blog.cloudflare.com/ja-jp/tag/rust/)[デバッグ](https://blog.cloudflare.com/ja-jp/tag/debugging/)[ネットワーキング](https://blog.cloudflare.com/ja-jp/tag/networking/)[輻輳制御](https://blog.cloudflare.com/ja-jp/tag/congestion-control/)

2026年5月12日

# 「idle」がアイドルではない場合：Linuxカーネルの最適化がQUICバグになった経緯

![Esteban Carisimo](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44VSSKPEBK3K5ND6JZ67YP.webp&w=64&h=64&f=webp&fit=cover&position=center)![Antonio Vicente](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW487NFE7AY4B70WNGYX9WZ9.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Esteban Carisimo](https://blog.cloudflare.com/ja-jp/author/esteban-carisimo/)、[Antonio Vicente](https://blog.cloudflare.com/ja-jp/author/antonio-vicente/)

16分で読了

URLをコピー

この記事は以下でも利用可能です [English](https://blog.cloudflare.com/quic-death-spiral-fix/)、[한국어](https://blog.cloudflare.com/ko-kr/quic-death-spiral-fix/).

![BLOG-3260 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45VSCEX3RARQSM9H9JQNVR.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA//////787/Hy5enu6uzy8vL28/Ly7Ozp////////7PH14Ojx5Ov17/L58fP16+3s////////6/L53Oj14Ov57fP98fT57PDw////////7fb+3ev54e397vX/8/f+7/P0////////9Pv/5fD+6PL/9Pn/+Pv/8/f5/////////P//8Pb/8/f/+/7//v//+fv9////////////+fv/+/z//////////f7//////////////f3///7//////////v//)

[_RFC 9438_](https://www.rfc-editor.org/rfc/rfc9438.html)で標準化されたCUBICは、Linuxのデフォルトの輻輳制御アルゴリズムであり、その結果、パブリックインターネット上のほとんどのTCPおよびQUIC接続が、利用可能な帯域幅を探索し、損失を検出した際にバックオフし、その後回復する方法を管理します。Cloudflareでは、オープンソースのQUIC実装である[ _quiche_](https://github.com/cloudflare/quiche)は、CUBICをデフォルトの輻輳コントローラーとして使用しています。つまり、このコードは、当社が提供するトラフィックの大部分のクリティカルパスにあります。

この記事では、CUBICの輻輳ウィンドウ（cwnd）が最小値で永続的にピン留めされ、輻輳が崩壊するイベントから回復できないというバグについてお話します。

話は、[ _RFC 9438 §4.2-12_](https://www.rfc-editor.org/rfc/rfc9438.html#section-4.2-12)に記載されているアプリ制限の除外に沿った[ _Linuxカーネルの変更_](https://github.com/torvalds/linux/commit/30927520dbae297182990bb21d08762bcc35ce1d)から始まります。CUBICは、QUICの実装に移植された際に予期しない動作が表面化した、TCPの実際の問題に対する修正です。開発者に明らかになりました。末尾は、理想的な（ほぼ）1行の修正でサイクルを断ち切りました。

## CUBICのロジックを簡潔に

核心的な問題に入る前に、輻輳制御アルゴリズム（CCA）について簡単におさらいしておきたいと思います。

CCAが回す中心的なボタンは、**輻輳ウィンドウ** （`cwnd`）です。これは、送信者が一度に送信できる（送信済みだが未確認の）バイト数の上限を示します。`cwnd`が大きいほど、送信者はラウンドトリップでより多くのデータをプッシュできます。小さい`cwnd`がそれをスロットルします。CUBICを含めた損失ベースのCCAは、究極的にはネットワークが健全に見える時に`cwnd`をどのように成長させ、不健全な場合は縮小するかを決定するためのポリシーなのです。

基本的に、CCAはネットワークの「利用可能な帯域幅」を推測することで、データ転送を最大化することを目的としています。 1Gbpsのサブスクリプションの支払いをして、そのほんの一部しか使いたくはないからです。CUBICが属する損失ベースのアルゴリズムのファミリーは、（1）パケットロスがない場合は、送信レートを高める（つまり、帯域幅利用率を高める）という基本的な前提で動作します。 (2) 損失がある場合、損失ベースのアルゴリズムは、ネットワークの容量を超えていると想定するため、送信者はバックバックする必要があります（つまり、帯域幅使用率の低減など）です。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3273 image5](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45F1EAW72WCHZ78GX5HT44.png&w=715&h=310&f=webp&fit=cover&position=center)

このロジックは、ここ数年にわたって再考されたいくつかの前提に基づいて構築されています。しかし、その説明はまた別の機会に持ちたいと思います。

## 症状：61%が失敗するテスト

当社の調査は、イングレスプロキシ統合テストパイプラインでの予期せぬ障害の報告から始まりました。この不安定な動作は、CUBICの接続初期に大幅な損失が発生するシナリオで評価されたテストで現れました。

輻輳崩壊後の復旧はとてつもない体制ですが、まさに輻輳コントローラーが対処すべき体制といえます。ほとんどの輻輳制御テストは、アルゴリズムの定常状態と成長段階で行われます。接続が切断された後、最小cwndで起こることを調査することは、はるかに少ないことになります。ステート空間のこの角のバグは、スループットダッシュボードでは見えず、静的レビューでは検出できません。CCAを意図的に起動して、後退するかどうかを監視することで初めて表面化します。これは、まさにこのテストが行ったのです。

シミュレートされたテストセットアップには、以下の詳細が含まれます：

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3273 image6](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47XTRR7C32QNFXD4R2P2QP.png&w=715&h=224&f=webp&fit=cover&position=center)

  * ローカル（localhost）でQuiche HTTP/3クライアントとサーバーが実行
  * RTT = 10ミリ秒（設定で設定）
  * HTTP/3でダウンロードした10MBファイル
  * CUBICの輻輳制御を使用する
  * 最初の2秒の間に30%のランダムなパケットロスが発生
  * 2秒後には損失が完全に停止
  * このテストではダウンロードが完了するまでのタイムアウトは10秒と余裕があるため、4〜5秒で完了することが予想されます。



予想される動作は単純です。CUBICは、損失フェーズ中にいくつかのヒットを受け、輻輳ウィンドウを減らし、損失が停止したら、着実に増加し、タイムアウト内にダウンロードを完了します。しかし、複数の100回の実行で、テストの約60%が、余裕のある10秒のタイムアウト以内にダウンロードを完了できていないことが確認されました。

## 異常：損失ゼロの999状態遷移

私たちは[ _quicheのqlog_](https://github.com/cloudflare/quiche)出力にパケットロスイベントを組み込み、輻輳コントローラー内で何が起こっているかを理解するための視覚化を構築しました。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3273 image10](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44FRE5WJ50JFBR32K8E6Y2.png&w=715&h=459&f=webp&fit=cover&position=center)

 _失敗したテストの接続概要。T=2s後には、パケット損失が完全に停止しますが、cwndは最低フロアでピン留めされたままで、輻輳の状態は回復と輻輳回避の間でおよそ14ミリ秒ごとに変動します。_

2秒（2000ミリ秒）を超えると、パケットの損失は完全に停止します。しかし、実行中のバイト数は横ばいのままであり、これはCUBICアルゴリズムのコアロジックに矛盾します。損失がなければ、より多くのガスを供給してスロットルを増加させます（私たちの世界では、より多くのバイト数を増やします）。 _ここで、疑問が生じます。ネットワークがパケットをドロップしなくなったのであれば、なぜ輻輳ウィンドウは拡大できないのでしょうか？_

この領域にズームインすると、CUBICは急速な変動に達し、プロットに示されているように、輻輳回避状態（運用体制フェーズ）と復旧状態（パケット損失の復旧状態）の間で999の遷移が起き、 6.7秒で完了しましたこれは、~14msごとに1回の遷移が行われており、接続のRTT（10ms）に疑わしいほど近い値です。この期間全体を通して、cwndは最小フロアの2700バイト、つまり2つのフルサイズパケットでロックされます。

明らかに何かがCUBICのロジックの何かが、接続の状態を誤って解釈しています。重要なヒントは、往復時間（~14ms）がRTTと一致していることです。回復/回避の反転をトリガーするものは、接続のACKクロックによるロックステップで、ラウンドトリップごとに一度発生します。クライアントからの各往復のACKがサーバーの次の送信をトリガーする、セルフクロックアルゴリズム。これはダウンロード（サーバーからクライアントへ）であるため、問題のACKはクライアントからサーバーに移動し、CUBICのステートマシンはサーバー側で実行されます。それらのACKが到達するたびに、bytes_in_flightがゼロになり、サーバーは次の2つのパケットバーストを送信しますバグのトリガーとなるものです。

この動作がCUBIC固有のものであることを確認するため、損失ベースのファミリーの別のメンバーですが、異なる増加率を持つ[ _Reno_](https://dl.acm.org/doi/10.1145/235160.235162)でも同じテストを実行しました。結果は確信的なものでした：パス率は100%で、損失フェーズ後にRenoはきれいに回復し、これがCUBIC関連のバグであることを明らかにしました。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3273 image8](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44TV8WPG06X3CYZXY26X0G.png&w=715&h=505&f=webp&fit=cover&position=center)

 _Renoは、T=2sで損失フェーズが終了した後正常に回復し、約5sでダウンロードを完了します。_

## 根本原因を追跡する

ロスベースアルゴリズムには、ガスとブレーキという2つのペダルがあり、加速方法が異なります。CUBICには追加の機能があります。ここでは、bytes_in_flight == 0に焦点を当てます。

### アイドル中TCP CUBIC（Linux、2017年）

バグを理解するには、まず最適化から来たものを理解する必要があります。2017年、LinuxカーネルのCUBIC実装に問題が見つかりました。[ _コミットメッセージ_](https://github.com/torvalds/linux/commit/30927520dbae297182990bb21d08762bcc35ce1d)は次のように説明します：

> エポックは最初と損失が発生した時にのみ更新/リセットされます。`now - epoch_start`のデルタ"t"は、アプリのアイドル後に任意に大きくなることができ、`bic_target`も同様です。結果的に、曲線（`ca->cnt`の逆）は非常に大きくなり、最終的に`ca->cnt`は遅延が生じ、2につながる
> 
> これは、`slow_start_after_idle`が無効になっている場合に特に顕著で、アイドル状態の数秒後に危険なcwndインフレーション（1.5倍のRTT）が発生します。

**epoch** は、CUBICが成長曲線を定着させるために使用する参照タイムスタンプです。`W_cubic(delta_t)`は、`delta_t = now - epoch_start`によってパラメータ化され、epochはCUBICが成長関数を再起動するたびにリセットされます。特に損失イベントが発生して`cwnd`が減少した後です。リセットの間、`delta_t`は経過時間と共に単調に増加します。

アプリケーションがしばらくの間アイドル状態（送信を停止）になり、その後再開すると、CUBIC成長関数 `W_cubic(delta_t)` は、下図に示すように、`delta_t` を `now - epoch_start` として計算します。アイドル中にエポックが更新されなかったので、`delta_t`は巨大で、巨大なターゲットウィンドウを生成し、CUBICはすぐに`cwnd`を不当な値まで膨らませようとします。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3273 image7](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45PX0PXQBDHX7JSR6WBDTA.png&w=715&h=452&f=webp&fit=cover&position=center)

Jana Iyengarの最初の修正は、アプリケーションが送信を再開した時に`epoch_start`をリセットすることでした。しかし、ニール・カードウェル氏は、そのアプローチの欠陥を[ _指摘しました_](https://github.com/torvalds/linux/commit/30927520dbae297182990bb21d08762bcc35ce1d)。

> ...CUBICアルゴリズムに曲線の再計算を依頼して、cwndが現在の場所から再び急上昇し始めるようにします（CUBICは喪失直後に行うように）。理想的には、Cwndの成長曲線は同じ形になり、アイドル期間だけ分だけ後で移動するだけです。

Eric Dumazet、Yuchung Cheng、Neal Cardwell氏が考案した高性能ソリューションは、リセットするのではなく、アイドル期間によってエポックを前進させるものでした。これにより、CUBICの成長曲線の形が保たれ、代わりにスライディングが行われるため、アルゴリズムが先に作業を別の場所に到達させることができます。

### クイッチするポート（2020年）

CUBICがquicheに[ _初めて実装された_](https://blog.cloudflare.com/cubic-and-hystart-support-in-quiche/)時に、このアイドル期間の調整は移植されました。ただし、ユーザー空間で動作するQUICには、TCPのカーネルレベルの[` _CA_EVENT_TX_START_`](https://github.com/torvalds/linux/commit/30927520dbae297182990bb21d08762bcc35ce1d)コールバックがありません。その代わりに、quicheの実装は`on_packet_sent()`内のアイドル状態をチェックします。
    
    
    // cubic.rs — on_packet_sent() (simplified)
    /// Updates the state when a packet is sent.
    fn on_packet_sent(&mut self, bytes_in_flight: usize, now: Instant, ...) {
        // If the sending burst is restarting (i.e., bytes_in_flight was zero before this send),
        // adjust the congestion recovery start time to account for the gap in sending.
        if bytes_in_flight == 0 {
            let delta = now - self.last_sent_time;
            self.congestion_recovery_start_time += delta;
        }
        // Record the time of this send event.
        self.last_sent_time = now;
    }

### どこが問題点か：QUICの違い

quicheに移植された修正には、元のカーネル変更のバグが含まれていましたが、約1週間後に[ _kernel cubicモジュールへのフォローアップ変更_](https://github.com/torvalds/linux/commit/c2e7204d180f8efc80f27959ca9cf16fa17f67db)で修正されました。2つ目の修正のコミットメッセージは次のように説明しています：

> `tcp_cubic`: `epoch_start`を将来に設定しないでください  
> `bictcp_cwnd_event()`でのアイドル時間の追跡は不正確です。`epoch_start`は  
>  通常、送信時ではなくACK処理時に設定されるためです。
> 
> 適切な修正を行うには、ステート変数を追加する必要がありますが、  
>  CUBICのバグに気付く前にずっとそこにあることを考えると、この  
>  手間のかからないように見えます。
> 
> 将来、`epoch_start`を設定しないようにしましょう。さもないと、  
> `bictcp_update()`がオーバーフローし、CUBICが再び  
> `cwnd`を急速に増加させてしまう可能性があります。

コミットメッセージに記載されているように、回復開始時刻はACK処理中に設定されており、送信時間に基づく調整の計算により、回復開始時刻を押し出すことができるのです。これは、テストで見られた回復と輻輳回避の遅れを説明しています。このトラップは、すべての着信ACKがbytes_in_flightがゼロになるまで一貫してトリガーされます。これは、実際には、Cwndが最小（2パケット）まで崩壊し、アプリケーションがACKが到着した瞬間に別の完全なウィンドウを送信する準備があることを意味します。この体制外では、bytes_in_flight == 0がすべての送信で保持される可能性は低いため、バグがトリガーされる可能性は低くなるのです。

接続開始時にもこうしたことが行われないのはなぜか？このバグは、接続がスロースタートを終了し、輻輳回避に切り替わった場合にのみトリガーされます。スロースタートを終了する前に、`congestion_recovery_start_time`が設定されていないため、`on_packet_sent`のバグのあるブランチには進めるリカバリ境界がありません。スロースタート中、CUBICの`cwnd`は、すべての損失ベースの CCA に共通する Reno スタイルの ack ベースのルールに従って増加します。つまり、接続が輻輳回避状態になったときにのみ、立方曲線と`congestion_recovery_start_time`に対する感度が考慮されるようになります。つまり、トラップには、回復境界を設定するための実際の損失イベント、輻輳回避が実行されていること、および`cwnd`が 2 パケットのフロアに縮退しているという 3 つのことが同時に必要です。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3273 image3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45TRJWX5RY1QFR0DK4FV15.png&w=715&h=533&f=webp&fit=cover&position=center)

 _自己永続的な回復の罠。最小cwndでは、ACKサイクルごとにアイドル期間の調整をトリガーし、デルタを増大させます。_

最小cwnd（2パケット）では、接続のダイナミクスは「ゼロスパイラル」にシフトし、アイドル期間の最適化が自己実現的な予測をたどります。このトラップは継続的なループで動作します。

  1. **パケットの送信とACK:** 送信者は2つのパケットウィンドウ全体を送信します。1つのRTT（～14ms）後に、両方のパケットがACKされるため、bytes_in_flightがゼロになります。
  2. **アイドル中の誤検出：** 次のバーストが送信されると、on_packet_sent()はbytes_in_flight == 0を見て、接続がアイドル状態であったと判断しますが、輻輳は制限されていました。
  3. **膨張したデルタ:** 計算は now - last_sent_time を使用してアイドル期間を決定します。輻輳ウィンドウ（`cwnd`）が最小の時、`last_sent_time`は前回のRTTサイクル _開始_ のタイムスタンプです。したがって、結果のデルタは約14ミリ秒（接続のRTT＋追加のラウンドトリップエラー）です。このRTTサイズのデルタは、「アイドル」タイムとして誤って適用されます。接続がアイドル状態だった _実際の_ 時間（最後のACKが到着してから次のパケットが送信されるまでの処理ギャップ）は、事実上0です。真のギャップではなく完全なRTTを測定することで、デルタは大幅に膨らみ、回復開始時間を積極的に前倒しし、場合によっては未来にまでシフトさせます。
  4. **認識された復旧：** 復旧開始時刻は将来のことになるため、`in_congestion_recovery()`チェックはすべての着信ACKに対してtrueを返します。次のACKの処理が回復を出て、回復開始をlast_sent_timeよりも長い時刻に設定することで、輻輳コントローラーが次の送信をするときに、回復時間を遅らせる可能性が高くなります。
  5. **停止:** CUBICは、回復期間中と認識されるパケットの`cwnd`の増加をスキップするため、ウィンドウは2つのパケットでピン留めされたままとなり、次のACKでパイプが完全に消費されることを確認し、サイクルを再起動します。



そして、このループは、スケジューラのジッタやACK処理のばらつきから生じる小さな逸脱の蓄積が何千回も繰り返され、`in_congestion_recovery()`の<=境界が次のパケットの送信時間より遅れて、サイクルが断たれるのです。

## 修正方法：アイドル状態を適切な瞬間から測定する

デススパイラルを修正するには、送信された最後のパケットではなく、bytes_in_flightが実際にゼロに移行した時点（ACKが処理された後）からアイドル期間を測定する必要があります。

### コード変更

  1. CUBICの状態にlast_ack_timeタイムスタンプを追加します。
  2. ACKが到着したら、そのタイムスタンプを更新します。
  3. アイドル当社のデルタ計算に使用


    
    
    // cubic.rs — on_packet_sent()
    fn on_packet_sent(&mut self, bytes_in_flight: usize, now: Instant, ...) {
        // Check if the connection was idle before this packet was sent.
        if bytes_in_flight == 0 {
            if let Some(recovery_start_time) = r.congestion_recovery_start_time {
                // Measure idle from the most recent activity: either the
                // last ACK (approximating when bif hit 0) or the last data
                // send, whichever is later. Using last_sent_time alone
                // would inflate the delta by a full RTT when cwnd is small
                // and bif transiently hits 0 between ACK and send.
                let idle_start = cmp::max(cubic.last_ack_time, cubic.last_sent_time);
    
                if let Some(idle_start) = idle_start {
                    if idle_start < now {
                        let delta = now - idle_start;
                        r.congestion_recovery_start_time =
                            Some(recovery_start_time + delta);
                    }
                }
            }
    }

直近のACKからの実際のギャップを遅れてデルタが反映するようになり、リカバリー境界は送信時間を追い求めなくなります。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3273 image2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48ASH8GZ33QEC3H67W7MMJ.png&w=715&h=369&f=webp&fit=cover&position=center)

 _古いコード：境界はサイクルごとに1RTTを送り、常に次の送信、またはその前にランディングします。_

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3273 image1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4655NBGY57G0JX3FXN88XF.png&w=715&h=369&f=webp&fit=cover&position=center)

 _修正: 境界はほとんど移動しません。次の送信がその前に到達すると、cwndが成長します。_

完全にアイドル状態の接続の場合、`last_ack_time`は遠く過去のものとなり、同じ式がアイドル期間全体を取得するため、元のepoch-shiftの動作は保持されます。

## 検証

修正を適用すると、QRフィッシングテストスイートの通過率が100%に戻りました。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3273 image11](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48KFFNQ428RM6AY394S59B.png&w=715&h=506&f=webp&fit=cover&position=center)

 _修正後、cwndは予想されるCUBIC曲線に沿って成長し、ダウンロードは最大4～5秒で完了します。_

接続末尾での損失を心配することはありません。これは、ルーターに割り当てられたバッファを完全に活用するため、予想されることです。つまり、このテストケースでは、利用可能な帯域幅をフルに活用しています。

## 要点

  * **「アイドル」は言葉にするよりも定義するのが難しいです。** 小さなウィンドウでの通常のパイプライン遅延は、単純なチェックではアイドル状態に見えるかもしれません。
  * **最小Cwndダイナミクスは、ユニークなケースです。** バグは高速では見えず、深刻な損失の発生後にトリガーされました。
  * **動作の複雑さに比べ、修正は驚くほど小さいものでした。** Qログのインストゥルメントと視覚化の分析で根本原因を突き止めた結果、わずか3行のコード変更が必要なソリューションになりました。調査中に述べたように、バグを見つけるための労力は膨大なものでしたが、修正自体は基本的に1行のロジックでした。



この記事で説明している修正は、**` _Cloudflare/quiche_`** 、Cloudflareのオープンソース実装QUICとHTTP/3に貢献しています。当社のCCAへの取り組みは、ロスベースのアルゴリズムだけにとどまりません。quicheのモジュラー型輻輳制御設計を使用して、モデルベースの[ _BBRv3_](https://blog.cloudflare.com/new-standards/#congestion-control)実装の実験と調整を行っており、現在、QUICデプロイの割合が増加している環境で有効になっています。QUIC輻輳制御の実装とパフォーマンスについての最新情報は、今後の動きにご注目ください。 

輻輳制御、トランスポートプロトコル、またはオープンソースネットワーキングコードへの貢献に興味がある方は、**quiche** リポジトリをご覧ください。当社では、このような問題を掘り下げることが好きな才能のあるエンジニアを常に募集しています。ぜひ、当社の[ _求人情報_](https://www.cloudflare.com/careers/)をご覧ください。

このページ

オンラインで議論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fquic-death-spiral-fix%2F&t=%E3%80%8Cidle%E3%80%8D%E3%81%8C%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB%E3%81%A7%E3%81%AF%E3%81%AA%E3%81%84%E5%A0%B4%E5%90%88%EF%BC%9ALinux%E3%82%AB%E3%83%BC%E3%83%8D%E3%83%AB%E3%81%AE%E6%9C%80%E9%81%A9%E5%8C%96%E3%81%8CQUIC%E3%83%90%E3%82%B0%E3%81%AB%E3%81%AA%E3%81%A3%E3%81%9F%E7%B5%8C%E7%B7%AF)[](https://x.com/intent/post?text=%E3%80%8Cidle%E3%80%8D%E3%81%8C%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB%E3%81%A7%E3%81%AF%E3%81%AA%E3%81%84%E5%A0%B4%E5%90%88%EF%BC%9ALinux%E3%82%AB%E3%83%BC%E3%83%8D%E3%83%AB%E3%81%AE%E6%9C%80%E9%81%A9%E5%8C%96%E3%81%8CQUIC%E3%83%90%E3%82%B0%E3%81%AB%E3%81%AA%E3%81%A3%E3%81%9F%E7%B5%8C%E7%B7%AF&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fquic-death-spiral-fix%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fquic-death-spiral-fix%2F)[](https://bsky.app/intent/compose?text=%E3%80%8Cidle%E3%80%8D%E3%81%8C%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB%E3%81%A7%E3%81%AF%E3%81%AA%E3%81%84%E5%A0%B4%E5%90%88%EF%BC%9ALinux%E3%82%AB%E3%83%BC%E3%83%8D%E3%83%AB%E3%81%AE%E6%9C%80%E9%81%A9%E5%8C%96%E3%81%8CQUIC%E3%83%90%E3%82%B0%E3%81%AB%E3%81%AA%E3%81%A3%E3%81%9F%E7%B5%8C%E7%B7%AF+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fquic-death-spiral-fix%2F)[](https://mastodonshare.com/?text=%E3%80%8Cidle%E3%80%8D%E3%81%8C%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB%E3%81%A7%E3%81%AF%E3%81%AA%E3%81%84%E5%A0%B4%E5%90%88%EF%BC%9ALinux%E3%82%AB%E3%83%BC%E3%83%8D%E3%83%AB%E3%81%AE%E6%9C%80%E9%81%A9%E5%8C%96%E3%81%8CQUIC%E3%83%90%E3%82%B0%E3%81%AB%E3%81%AA%E3%81%A3%E3%81%9F%E7%B5%8C%E7%B7%AF&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fquic-death-spiral-fix%2F)[](https://www.threads.net/intent/post?text=%E3%80%8Cidle%E3%80%8D%E3%81%8C%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB%E3%81%A7%E3%81%AF%E3%81%AA%E3%81%84%E5%A0%B4%E5%90%88%EF%BC%9ALinux%E3%82%AB%E3%83%BC%E3%83%8D%E3%83%AB%E3%81%AE%E6%9C%80%E9%81%A9%E5%8C%96%E3%81%8CQUIC%E3%83%90%E3%82%B0%E3%81%AB%E3%81%AA%E3%81%A3%E3%81%9F%E7%B5%8C%E7%B7%AF+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fquic-death-spiral-fix%2F)

## 関連するタグ

[HTTP3](https://blog.cloudflare.com/ja-jp/tag/http3/)[QUIC](https://blog.cloudflare.com/ja-jp/tag/quiche/)[QUIC](https://blog.cloudflare.com/ja-jp/tag/quic/)[Rust](https://blog.cloudflare.com/ja-jp/tag/rust/)[デバッグ](https://blog.cloudflare.com/ja-jp/tag/debugging/)[ネットワーキング](https://blog.cloudflare.com/ja-jp/tag/networking/)[輻輳制御](https://blog.cloudflare.com/ja-jp/tag/congestion-control/)

SNS をフォロー

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 新しい投稿のお知らせを受け取るように登録する

メールアドレス

また、あなたのメールアドレスを共有したりすることはございません。

登録する

ご購読ありがとうございます！受信箱を確認して登録してください。
