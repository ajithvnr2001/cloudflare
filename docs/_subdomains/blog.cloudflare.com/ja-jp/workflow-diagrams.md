---
url: https://blog.cloudflare.com/ja-jp/workflow-diagrams/
title: Workflows\u306e\u30b3\u30fc\u30c9\u3092\u8996\u899a\u7684\u306a\u56f3\u306b\u5909\u63db\u3059\u308b\u305f\u3081\u306b\u3001\u62bd\u8c61\u69cb\u6587\u30c4\u30ea\u30fc\uff08AST\uff09\u3092\u4f7f\u7528\u3059\u308b\u65b9\u6cd5 | Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:35:38.941792+00:00
---

# Workflowsのコードを視覚的な図に変換するために、抽象構文ツリー（AST）を使用する方法 | Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/workflow-diagrams/

[ブログ](https://blog.cloudflare.com/ja-jp/)

[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[Workflows](https://blog.cloudflare.com/ja-jp/tag/workflows/)[開発者](https://blog.cloudflare.com/ja-jp/tag/developers/)

3 タグタグを3件表示

  * 投稿タグ
  * [Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[Workflows](https://blog.cloudflare.com/ja-jp/tag/workflows/)[開発者](https://blog.cloudflare.com/ja-jp/tag/developers/)
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



[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[Workflows](https://blog.cloudflare.com/ja-jp/tag/workflows/)[開発者](https://blog.cloudflare.com/ja-jp/tag/developers/)

2026年3月27日

# Workflowsのコードを視覚的な図に変換するために、抽象構文ツリー（AST）を使用する方法 

![André Venceslau](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45TZTSTWQ6JMKEC8GX38NE.png&w=64&h=64&f=webp&fit=cover&position=center)![Mia Malden](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4559TC07A12MQHAEK8YM1R.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[André Venceslau](https://blog.cloudflare.com/ja-jp/author/andre-venceslau/)、[Mia Malden](https://blog.cloudflare.com/ja-jp/author/mia/)

11分で読了

URLをコピー

この記事は以下でも利用可能です [English](https://blog.cloudflare.com/workflow-diagrams/)、[한국어](https://blog.cloudflare.com/ko-kr/workflow-diagrams/).

![BLOG-3163 Hero Image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47AEP95R4WVM6YM3WW23XZ.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///////88O/y4+Xu4+jx6u/27/Hz7uzr////////6+712uLw2eX04+346/D27e3u////////6O/50uH00OP43e386fH67e7y////////6fL+0eT50Ob83/D/7PX+8PL2////////7/f/2+r+3O7/6/j/9fv/9vf7////////+f7/6fP/7fj/+v///////fz+////////////9vr//P//////////////////////////+/3/////////////////)

[_Cloudflare Workflows_](https://www.cloudflare.com/developer-platform/products/workflows/)は、ステップを連鎖させ、失敗時に再試行し、長期間実行されるプロセス全体で状態を保持できる耐久性のある実行エンジンです。開発者はWorkflowsを使用して、バックグラウンドエージェントの強化、データパイプラインの管理、ヒューマンインザループ承認システムなどを構築します。

先月、Cloudflareにデプロイされたすべてのワークフローのダッシュボードに完全なビジュアル図が表示されるようになったことを[ _発表しました_](https://developers.cloudflare.com/changelog/post/2026-02-03-workflows-visualizer/)。

これは、アプリケーションを可視化することがこれまで以上に重要になっているためです。コーディングエージェントが書いているコードは、あなたが読んでいるかどうかに関係なく、しかし、ステップがどのようにつながり、どこに分岐するか、実際に何が起こっているかなど、構築されるものの形は依然として重要です。

以前、ビジュアルワークフロービルダーの図を見たことがあるとしたら、それらは通常、JSON設定、YAML、ドラッグ＆ドロップなどの宣言的なものから動作しています。しかし、Cloudflare Workflowsは単なるコードです。これらには、[ _Promise、Promise.all、ループ、条件式_](https://developers.cloudflare.com/workflows/build/workers-api/)を含めることができ、また関数やクラスにネストすることもできます。この動的実行モデルでは、図のレンダリングが少し複雑になります。

Cloudflareでは、抽象構文ツリー（AST）を使用してグラフを静的に取得し、`Promise`と`await`の関係を追跡し、何が並列に実行され、何がブロックし、各要素がどのように連携するかを把握します。

この図の作成方法について、この記事を続けてご覧ください。あるいは、最初のワークフローをデプロイして、図をご覧ください。

[![Cloudflareへデプロイ](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/workflows-starter-template)

以下は、Cloudflare Workflowsのコードから生成された図の例です：

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3163 Image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46FCEK2SHE8ZKJ2DZXJ9SH.png&w=715&h=912&f=webp&fit=cover&position=center)

### 動的ワークフローの実行

一般的に、ワークフローエンジンは、動的実行順序またはシーケンシャル（静的）実行順序のいずれかに従って実行できます。順次実行は、ワークフローをトリガー → ステップA → ステップB → ステップC、エンジンがステップAを完了した直後にステップBが実行、といった形で実行されます。

[ _Cloudflare Workflows_](https://developers.cloudflare.com/workflows/)は、動的実行モデルに従っています。ワークフローは単なるコードなので、ランタイムが遭遇するとステップが実行されます。ランタイムがステップを検出すると、そのステップはワークフローエンジンに引き渡され、ワークフローエンジンはその実行を管理します。このステップは、待機されていない限り、本質的に順次処理されるものではありません。エンジンは、待機中のステップをすべて並行して実行します。こうすることで、追加のラッパーやディレクティブなしで、ワークフローコードをフロー制御として記述することができます。引き渡しの仕組みは次のとおりです。

  1. そのインスタンスの「スーパーバイザー」Durable Objectである _エンジン_ が起動されます。エンジンは、実際のワークフロー実行のロジックを担当します。
  2. エンジンは、[ _ユーザーWorker_](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#user-workers)を[ _動的ディスパッチ_](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/dynamic-dispatch/)を介してトリガーし、Workersランタイムに制御を渡します。
  3. ランタイムが`step.do`に遭遇すると、実行をエンジンに渡します。
  4. エンジンはステップを実行し、結果を保持します（該当する場合はエラーを発生させます）。そして、ユーザーWorkerを再びトリガーします。



このアーキテクチャでは、エンジンは実行中のステップの順序を本質的に「知る」ことはできませんが、図にとっては、ステップの順序は重要な情報になります。ここでの課題は、ワークフローの大部分を診断に有用なグラフに正確に変換することにあります。ベータ版の図を使って、これらの表現を繰り返し、改善し続けます。

### コードの解析

実行時ではなく、[ _デプロイ時_](https://developers.cloudflare.com/workers/get-started/guide/#4-deploy-your-project)にスクリプトを取得することで、ワークフロー全体を解析して静的に図を生成することができます。

一歩下がって、ワークフローデプロイメントの概略を説明すると、次のようになります：

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3163 Image 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44Z4PFGJR15RR2B45KXVTM.png&w=715&h=1033&f=webp&fit=cover&position=center)

図を作成するために、Workersをデプロイする内部設定サービスによってバンドルされたスクリプトを取得します（Workflowデプロイのステップ2）。次に、パーサーを使用してワークフローを表す抽象構文ツリー（AST）を作成し、内部サービスがすべてのWorkflowErrorpointsとワークフローステップへの呼び出しを含む中間グラフを生成して横断します。APIの最終結果に基づいて図をレンダリングします。

Workerがデプロイされると、設定サービスは（[ _esbuild_](https://esbuild.github.io/)をデフォルトで使用して）コードをバンドルし、[ _特に指定がない限り_](https://developers.cloudflare.com/workers/wrangler/configuration/#inheritable-keys)圧縮します。これには別の課題があります。TypeScriptのWorkflowsは直感的なパターンに従いますが、圧縮されたJavascript（JS）は緻密で消費しにくい可能性があります。また、バンドルによって、コードの圧縮方法も異なります。

これは、**エージェントが並行して実行することを示す** Workflowコードの例です。
    
    
    const summaryPromise = step.do(
             `summary agent (loop ${loop})`,
             async () => {
               return runAgentPrompt(
                 this.env,
                 SUMMARY_SYSTEM,
                 buildReviewPrompt(
                   'Summarize this text in 5 bullet points.',
                   draft,
                   input.context
                 )
               );
             }
           );
            const correctnessPromise = step.do(
             `correctness agent (loop ${loop})`,
             async () => {
               return runAgentPrompt(
                 this.env,
                 CORRECTNESS_SYSTEM,
                 buildReviewPrompt(
                   'List correctness issues and suggested fixes.',
                   draft,
                   input.context
                 )
               );
             }
           );
            const clarityPromise = step.do(
             `clarity agent (loop ${loop})`,
             async () => {
               return runAgentPrompt(
                 this.env,
                 CLARITY_SYSTEM,
                 buildReviewPrompt(
                   'List clarity issues and suggested fixes.',
                   draft,
                   input.context
                 )
               );
             }
           );

[_rspack_](https://rspack.rs/)とバンドルした場合、縮小コードのスニペットは次のようになります。
    
    
    class pe extends e{async run(e,t){de("workflow.run.start",{instanceId:e.instanceId});const r=await t.do("validate payload",async()=>{if(!e.payload.r2Key)throw new Error("r2Key is required");if(!e.payload.telegramChatId)throw new Error("telegramChatId is required");return{r2Key:e.payload.r2Key,telegramChatId:e.payload.telegramChatId,context:e.payload.context?.trim()}}),s=await t.do("load source document from r2",async()=>{const e=await this.env.REVIEW_DOCUMENTS.get(r.r2Key);if(!e)throw new Error(`R2 object not found: ${r.r2Key}`);const t=(await e.text()).trim();if(!t)throw new Error("R2 object is empty");return t}),n=Number(this.env.MAX_REVIEW_LOOPS??"5"),o=this.env.RESPONSE_TIMEOUT??"7 days",a=async(s,i,c)=>{if(s>n)return le("workflow.loop.max_reached",{instanceId:e.instanceId,maxLoops:n}),await t.do("notify max loop reached",async()=>{await se(this.env,r.telegramChatId,`Review stopped after ${n} loops for ${e.instanceId}. Start again if you still need revisions.`)}),{approved:!1,loops:n,finalText:i};const h=t.do(`summary agent (loop ${s})`,async()=>te(this.env,"You summarize documents. Keep the output short, concrete, and factual.",ue("Summarize this text in 5 bullet points.",i,r.context)))...

または、[ _vite_](https://vite.dev/) とバンドルすると、以下に縮小版のスニペットを示します。
    
    
    class ht extends pe {
      async run(e, r) {
        b("workflow.run.start", { instanceId: e.instanceId });
        const s = await r.do("validate payload", async () => {
          if (!e.payload.r2Key)
            throw new Error("r2Key is required");
          if (!e.payload.telegramChatId)
            throw new Error("telegramChatId is required");
          return {
            r2Key: e.payload.r2Key,
            telegramChatId: e.payload.telegramChatId,
            context: e.payload.context?.trim()
          };
        }), n = await r.do(
          "load source document from r2",
          async () => {
            const i = await this.env.REVIEW_DOCUMENTS.get(s.r2Key);
            if (!i)
              throw new Error(`R2 object not found: ${s.r2Key}`);
            const c = (await i.text()).trim();
            if (!c)
              throw new Error("R2 object is empty");
            return c;
          }
        ), o = Number(this.env.MAX_REVIEW_LOOPS ?? "5"), l = this.env.RESPONSE_TIMEOUT ?? "7 days", a = async (i, c, u) => {
          if (i > o)
            return H("workflow.loop.max_reached", {
              instanceId: e.instanceId,
              maxLoops: o
            }), await r.do("notify max loop reached", async () => {
              await J(
                this.env,
                s.telegramChatId,
                `Review stopped after ${o} loops for ${e.instanceId}. Start again if you still need revisions.`
              );
            }), {
              approved: !1,
              loops: o,
              finalText: c
            };
          const h = r.do(
            `summary agent (loop ${i})`,
            async () => _(
              this.env,
              et,
              K(
                "Summarize this text in 5 bullet points.",
                c,
                s.context
              )
            )
          )...

縮小コードは、かなり危険な状態になっており、バンドラーによっては、さまざまな方向に向かってバラバラになる可能性があります。

当社には、さまざまな形態のミニファイされたコードを素早く正確に解析する方法が必要でした。私たちは、[ _JavaScript Oxidation Compiler_](https://oxc.rs/) （OXC）の` oxc-parser `がこの仕事に最適であると判断しました。Cloudflareはまず、Rustを実行するコンテナでこのアイデアをテストしました。すべてのスクリプトIDが[ _Cloudflare Queue_](https://developers.cloudflare.com/queues/)に送信され、その後、メッセージが取り出され、処理のためにコンテナに送信されました。このアプローチが有効であることを確認すると、Rustで書かれたWorkerに移行しました。Workersは[ _WebAssemblyを介したRustの実行_](https://developers.cloudflare.com/workers/languages/rust/)をサポートしており、パッケージはこれを簡単にするのに十分な小ささでした。

Rust Workerは、まず圧縮されたJSをASTノードタイプに変換し、次にASTノードタイプをダッシュボード上にレンダリングされるワークフローのグラフィカルバージョンに変換します。そのために、各ワークフローに対して事前に定義された[ _ノードタイプ_](https://developers.cloudflare.com/workflows/build/visualizer/)のグラフを生成し、一連のノードマッピングを通してグラフ表現に変換します。

### 図のレンダリング

ワークフローの図バージョンをレンダリングするためには、ステップと関数の関係を正しく追跡する方法と、すべての攻撃対象領域をカバーしながら、ワークフローのノードタイプをできるだけシンプルに定義する方法という2つの課題がありました。

ステップと関数の関係を正しく追跡することを保証するには、関数とステップの両方の名前を収集する必要がありました。先に述べたように、エンジンはステップに関する情報しかありませんが、ステップが関数に依存することもあれば、その逆も同様です。例えば、開発者は関数の中にステップを含めたり、関数をステップとして定義することがあります。異なる[ _モジュール_](https://blog.cloudflare.com/workers-javascript-modules/)からの関数内のステップを呼び出すことも、ステップ名を変更することもできます。

ライブラリはASTを与えることで最初の課題は克服できるものの、まだそれをどのように解析するかを決定する必要があります。コードパターンによっては、さらなる創造性が必要になります。例えば、関数 — `WorkflowEntrypoint`内では、ステップを直接、間接的に、またはまったく呼び出さない関数を使用することができます。`functionA` を考えてみましょう。これは、`console.log(await functionB(), await functionC()`) を含み、その中で `functionB` が `step.do()` を呼び出します。その場合、`functionA`と`functionB`の両方をワークフロー図に含める必要があります。しかし、`functionC`はそうすべきではありません。直接および間接のステップ呼び出しを含むすべての関数を捕捉するために、各関数のサブグラフを作成し、ステップ呼び出し自体が含まれているか、あるいは別の関数を呼び出す可能性があるのかを確認します。これらのサブグラフは、関連するすべてのノードを含む関数ノードによって表されます。関数ノードがグラフの緑の場合、その中に直接または間接のワークフローステップがない場合は、最終出力から切り詰めます。

私たちは、最大10の異なる方法で定義された、ワークフロー図や変数を推測できる静的ステップのリストなど、他のパターンもチェックします。スクリプトに複数のワークフローが含まれる場合、関数用に作成されたサブグラフと同様のパターンに従い、1レベル上に抽象化されます。

ASTノードタイプごとに、ループ、ブランチ、プロミス、パラレル、await、アロー関数など、ワークフロー内で使用できるあらゆる方法を検討しなければなりませんでした。こうした経路の中にさえ、何十もの可能性があります。ループにする方法をいくつか考えてみましょう。
    
    
    // for...of
    for (const item of items) {
    	await step.do(`process ${item}`, async () => item);
    }
    // while
    while (shouldContinue) {
    	await step.do('poll', async () => getStatus());
    }
    // map
    await Promise.all(
    	items.map((item) => step.do(`map ${item}`, async () => item)),
    );
    // forEach
    await items.forEach(async (item) => {
    	await step.do(`each ${item}`, async () => item);
    });

また、ループ処理に加えて、ブランチングの処理方法についてもお話します。
    
    
    // switch / case
    switch (action.type) {
    	case 'create':
    		await step.do('handle create', async () => {});
    		break;
    	default:
    		await step.do('handle unknown', async () => {});
    		break;
    }
    
    // if / else if / else
    if (status === 'pending') {
    	await step.do('pending path', async () => {});
    } else if (status === 'active') {
    	await step.do('active path', async () => {});
    } else {
    	await step.do('fallback path', async () => {});
    }
    
    // ternary operator
    await (cond
    	? step.do('ternary true branch', async () => {})
    	: step.do('ternary false branch', async () => {}));
    
    // nullish coalescing with step on RHS
    const myStepResult =
    	variableThatCanBeNullUndefined ??
    	(await step.do('nullish fallback step', async () => 'default'));
    
    // try/catch with finally
    try {
    	await step.do('try step', async () => {});
    } catch (_e) {
    	await step.do('catch step', async () => {});
    } finally {
    	await step.do('finally step', async () => {});
    }

私たちの目標は、開発者が知っておくべきことを、過度に複雑にすることなく伝える簡潔なAPIを作ることでした。しかし、ワークフローを図に変換するということは、あらゆるパターン（ベストプラクティスに従っているかどうか）と可能なエッジケースを考慮することを意味します。先に説明したように、各ステップはデフォルトでは他のステップと明示的に続くものではありません。ワークフローが`await`と`Promise.all()`を使用しない場合、ステップが発生した順に実行されると仮定します。しかし、ワークフローに`await`、`Promise`、または`Promise.all()`が含まれている場合、これらの関係を追跡する方法が必要だったのです。

各ノードに`starts:`と`resolves:`フィールドがある実行順序を追跡することにしました。`starts`と`resolves`のインデックスは、約束がいつ実行され始めたか、すぐに続く結論なしに開始された最初の約束と比較して、いつ終了するかを示します。これは、図UIの縦長の配置（`starts:1`を持つすべてのステップがインラインになります）に相関しています。ステップが宣言されたときに待機している場合、`starts`と`resolves`は未定義となり、ワークフローはランタイムにステップが表示された順番で実行されます。

解析中に、未解決の`Promise`または`Promise.all()`に遭遇すると、そのノード（または複数のノード）にはエントリー番号が付けられ、`starts`フィールドに表示されます。その約束に `await` が発生した場合、エントリー番号は1つインクリメントされ、出口番号（`resolves` の値）として保存されます。これにより、同時に実行されるPromiseと、相互の関係においていつ完了するかを知ることができます。
    
    
    export class ImplicitParallelWorkflow extends WorkflowEntrypoint<Env, Params> {
     async run(event: WorkflowEvent<Params>, step: WorkflowStep) {
       const branchA = async () => {
         const a = step.do("task a", async () => "a"); //starts 1
         const b = step.do("task b", async () => "b"); //starts 1
         const c = await step.waitForEvent("task c", { type: "my-event", timeout: "1 hour" }); //starts 1 resolves 2
         await step.do("task d", async () => JSON.stringify(c)); //starts 2 resolves 3
         return Promise.all([a, b]); //resolves 3
       };
    
       const branchB = async () => {
         const e = step.do("task e", async () => "e"); //starts 1
         const f = step.do("task f", async () => "f"); //starts 1
         return Promise.all([e, f]); //resolves 2
       };
    
       await Promise.all([branchA(), branchB()]);
    
       await step.sleep("final sleep", 1000);
     }
    }

図でステップの整合性を確認できます。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3163 Image 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW480NNEVSMK7AVV6RGRF4T0.png&w=715&h=611&f=webp&fit=cover&position=center)

これらのパターンをすべて考慮した結果、次のようなノードタイプのリストに落ち着きました。 
    
    
    | StepSleep
    | StepDo
    | StepWaitForEvent
    | StepSleepUntil
    | LoopNode
    | ParallelNode
    | TryNode
    | BlockNode
    | IfNode
    | SwitchNode
    | StartNode
    | FunctionCall
    | FunctionDef
    | BreakNode;

さまざまな動作に対するAPI出力のサンプルをいくつか示します。

`function` call:
    
    
    {
      "functions": {
        "runLoop": {
          "name": "runLoop",
          "nodes": []
        }
      }
    }

`if` 条件分岐による `step.do`:
    
    
    {
      "type": "if",
      "branches": [
        {
          "condition": "loop > maxLoops",
          "nodes": [
            {
              "type": "step_do",
              "name": "notify max loop reached",
              "config": {
                "retries": {
                  "limit": 5,
                  "delay": 1000,
                  "backoff": "exponential"
                },
                "timeout": 10000
              },
              "nodes": []
            }
          ]
        }
      ]
    }

`step.do`および`waitForEvent`と`waitForEvent`：
    
    
    {
      "type": "parallel",
      "kind": "all",
      "nodes": [
        {
          "type": "step_do",
          "name": "correctness agent (loop ${...})",
          "config": {
            "retries": {
              "limit": 5,
              "delay": 1000,
              "backoff": "exponential"
            },
            "timeout": 10000
          },
          "nodes": [],
          "starts": 1
        },
    ...
        {
          "type": "step_wait_for_event",
          "name": "wait for user response (loop ${...})",
          "options": {
            "event_type": "user-response",
            "timeout": "unknown"
          },
          "starts": 3,
          "resolves": 4
        }
      ]
    }

### 今後の展開は？

最終的に、これらのWorkflow図の目標は、フルサービスのデバッグツールとして機能することです。つまり、以下が可能になるということです。

  * グラフを通じて実行をリアルタイムで追跡する
  * エラーを発見し、ヒューマンインザループの承認を待ち、テストのステップを省略する
  * ローカル開発におけるアクセスの可視化



[ _Workflow概要ページ_](https://dash.cloudflare.com/?to=/:account/workers/workflows)で図を確認してください。機能リクエストがある場合、またはバグにお気づきの点がある場合は、[ _DiscordのCloudflare開発者コミュニティ_](https://discord.cloudflare.com/)に参加して、Cloudflareチームに直接フィードバックを共有してください。

このページ

オンラインで議論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fworkflow-diagrams%2F&t=Workflows%E3%81%AE%E3%82%B3%E3%83%BC%E3%83%89%E3%82%92%E8%A6%96%E8%A6%9A%E7%9A%84%E3%81%AA%E5%9B%B3%E3%81%AB%E5%A4%89%E6%8F%9B%E3%81%99%E3%82%8B%E3%81%9F%E3%82%81%E3%81%AB%E3%80%81%E6%8A%BD%E8%B1%A1%E6%A7%8B%E6%96%87%E3%83%84%E3%83%AA%E3%83%BC%EF%BC%88AST%EF%BC%89%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95%20)[](https://x.com/intent/post?text=Workflows%E3%81%AE%E3%82%B3%E3%83%BC%E3%83%89%E3%82%92%E8%A6%96%E8%A6%9A%E7%9A%84%E3%81%AA%E5%9B%B3%E3%81%AB%E5%A4%89%E6%8F%9B%E3%81%99%E3%82%8B%E3%81%9F%E3%82%81%E3%81%AB%E3%80%81%E6%8A%BD%E8%B1%A1%E6%A7%8B%E6%96%87%E3%83%84%E3%83%AA%E3%83%BC%EF%BC%88AST%EF%BC%89%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95+&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fworkflow-diagrams%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fworkflow-diagrams%2F)[](https://bsky.app/intent/compose?text=Workflows%E3%81%AE%E3%82%B3%E3%83%BC%E3%83%89%E3%82%92%E8%A6%96%E8%A6%9A%E7%9A%84%E3%81%AA%E5%9B%B3%E3%81%AB%E5%A4%89%E6%8F%9B%E3%81%99%E3%82%8B%E3%81%9F%E3%82%81%E3%81%AB%E3%80%81%E6%8A%BD%E8%B1%A1%E6%A7%8B%E6%96%87%E3%83%84%E3%83%AA%E3%83%BC%EF%BC%88AST%EF%BC%89%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95++https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fworkflow-diagrams%2F)[](https://mastodonshare.com/?text=Workflows%E3%81%AE%E3%82%B3%E3%83%BC%E3%83%89%E3%82%92%E8%A6%96%E8%A6%9A%E7%9A%84%E3%81%AA%E5%9B%B3%E3%81%AB%E5%A4%89%E6%8F%9B%E3%81%99%E3%82%8B%E3%81%9F%E3%82%81%E3%81%AB%E3%80%81%E6%8A%BD%E8%B1%A1%E6%A7%8B%E6%96%87%E3%83%84%E3%83%AA%E3%83%BC%EF%BC%88AST%EF%BC%89%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95+&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fworkflow-diagrams%2F)[](https://www.threads.net/intent/post?text=Workflows%E3%81%AE%E3%82%B3%E3%83%BC%E3%83%89%E3%82%92%E8%A6%96%E8%A6%9A%E7%9A%84%E3%81%AA%E5%9B%B3%E3%81%AB%E5%A4%89%E6%8F%9B%E3%81%99%E3%82%8B%E3%81%9F%E3%82%81%E3%81%AB%E3%80%81%E6%8A%BD%E8%B1%A1%E6%A7%8B%E6%96%87%E3%83%84%E3%83%AA%E3%83%BC%EF%BC%88AST%EF%BC%89%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95++https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fworkflow-diagrams%2F)

## 関連するタグ

[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[Workflows](https://blog.cloudflare.com/ja-jp/tag/workflows/)[開発者](https://blog.cloudflare.com/ja-jp/tag/developers/)

SNS をフォロー

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 新しい投稿のお知らせを受け取るように登録する

メールアドレス

また、あなたのメールアドレスを共有したりすることはございません。

登録する

ご購読ありがとうございます！受信箱を確認して登録してください。
