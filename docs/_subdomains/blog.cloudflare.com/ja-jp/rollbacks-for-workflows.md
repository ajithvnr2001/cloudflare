---
url: https://blog.cloudflare.com/ja-jp/rollbacks-for-workflows/
title: \u5f53\u793e\u304cCloudflare Workflows\u306e\u9632\u5fa1\u30ed\u30fc\u30eb\u30d0\u30c3\u30af\u3092\u3069\u306e\u3088\u3046\u306b\u69cb\u7bc9\u3057\u305f\u304b | Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:36:40.073911+00:00
---

# 当社がCloudflare Workflowsの防御ロールバックをどのように構築したか | Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/rollbacks-for-workflows/

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

2026年6月25日

# 当社がCloudflare Workflowsの防御ロールバックをどのように構築したか

![Vaishnav Kavitha](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW9WMMZ8JJQ1SE783SASV4PJ.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Mia Malden](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4559TC07A12MQHAEK8YM1R.jpg&w=64&h=64&f=webp&fit=cover&position=center)![André Venceslau](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45TZTSTWQ6JMKEC8GX38NE.png&w=64&h=64&f=webp&fit=cover&position=center)

[Vaishnav Kavitha](https://blog.cloudflare.com/ja-jp/author/vaishnav-kavitha/)、[Mia Malden](https://blog.cloudflare.com/ja-jp/author/mia/)、[André Venceslau](https://blog.cloudflare.com/ja-jp/author/andre-venceslau/)

16分で読了

URLをコピー

この記事は以下でも利用可能です [English](https://blog.cloudflare.com/rollbacks-for-workflows/)、[한국어](https://blog.cloudflare.com/ko-kr/rollbacks-for-workflows/)、[繁體中文](https://blog.cloudflare.com/zh-tw/rollbacks-for-workflows/)、[简体中文](https://blog.cloudflare.com/zh-cn/rollbacks-for-workflows/).

![BLOG-3317 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW9WMM3AX6SCQ1TVSR6M8NMX.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////+P/84u3z1uPw4Onz8PP39fX07u3s////+v/+4+320+Dy1+L15ez57fD27O3u/////f//5+/509/1z9742uX85uz57O3x////////7vT+2eP50d/82OX/5ez97/D1////////+Pz/5ez+3ef/4uv/7fL/9fb6////////////9Pf/7/P/8vf/+fv//fz+/////////////////f3/////////////////////////////////////////////)

Cloudflare Workflowsは、長期間実行されるプロセス全体で、組み込みのリトライ処理と状態の永続性を備えた、耐久性のあるマルチステップアプリケーションを構築することができます。[ _Workflow_](https://developers.cloudflare.com/workflows/)が実行されると、各ステップは外部システムを呼び出し、失敗を再試行し、再起動時に状態を保持することができます。しかし、1つのステップが失敗すると、完了したステップから以前の作業が一貫性のない、または部分的な状態になる可能性があります。

本日、Workflowsのサガロールバックを出荷します。これにより、障害が発生した場合に、ステップ自体でロールバックロジックを宣言できるようになります。

たとえば、2つの異なる銀行の口座間で資金移動を行うワークフローがあるとします。

  1. A銀行の口座からの借方
  2. B銀行の口座に振り込み
  3. 両方のアカウント所有者に確認メールを送信する



ステップ2（B銀行の口座への貸方）が失敗した場合はどうなりますか？A銀行で借方に成功すると、取引がコミットされ、お金がシステムを離れます。取引のオーケストレーターとして、A銀行のシステムで操作を単純に「元に戻す」ことはできません。この代わりに、最初の操作と逆の操作を意味する新しい操作を通じて、A銀行の口座に返金する必要があります。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3317 image6](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW9WKYMHAWC2FCMBSGG1XMKT.png&w=715&h=681&f=webp&fit=cover&position=center)

  
このような操作と報酬ロジックの組み合わせは、[ _サガパターン_](https://www.youtube.com/watch?v=xDuwrtwYHu8)と呼ばれます。

今日まで、開発者は、ステップの直接的な定義以外に、何が成功し、何が失敗し、失敗した場合にどのような行動をとるべきかを追跡するために、独自の報酬ロジックを実装する必要がありました。これで、各`step.do()`に対して報酬ロジックを定義できるようになりました。ステップ自体内の引数として、ロールバックに対するワークフローの耐久性を維持します。
    
    
    // track what completed so we know what to undo
    let debitA;
    let creditB;
    try {
      debitA = await step.do("debit-bank-a", () => bankA.debit(from, amount));
      creditB = await step.do("credit-bank-b", () => bankB.credit(to, amount));
      await step.do("notify", () => notifyBoth(from, to, amount));
    } catch (error) {
      // unwind in reverse. each undo is its own durable step,
      // must be idempotent, and must keep going if one fails.
      if (creditB) {
        try {
          await step.do("reverse-credit-b", () => bankB.debit(to, amount, creditB.id));
        } catch (e) {
          await alertOnCall("reverse-credit-b failed", e);
        }
      }
      if (debitA) {
        try {
          await step.do("refund-debit-a", () => bankA.credit(from, amount, debitA.id));
        } catch (e) {
          await alertOnCall("refund-debit-a failed", e);
        }
      }
      throw error;
    }

_ロールバックなし_
    
    
     // each step ships with its own undo. add a step,
    // add its rollback right here. no growing catch
    // block, no manual ordering, no replay logic.
    await step.do("debit-bank-a", () => bankA.debit(from, amount), {
      rollback: async ({ output }) => bankA.credit(from, amount, output.id),
    });
    await step.do("credit-bank-b", () => bankB.credit(to, amount), {
      rollback: async ({ output }) => bankB.debit(to, amount, output.id),
    });
    await step.do("notify", () => notifyBoth(from, to, amount));

_ロールバック機能あり_

## 試してみる

ロールバックを使用するには、`rollback`関数を含むオプションオブジェクトを、`step.do()`の最後の引数として渡すだけです。
    
    
    const debit = await step.do(
      "debit-account-a",
      async () => {
        return await bankA.debit({
          accountId: fromAccountId,
          amount,
          idempotencyKey: `${transferId}:debit-account-a`,
        });
      },
      {
        rollback: async () => {
          await bankA.credit({
            accountId: fromAccountId,
            amount,
            idempotencyKey: `${transferId}:rollback-debit-account-a`,
          });
        },
      }
    );
    
    // The idempotency keys make both the forward operations and rollback operations safe to retry without duplicating the transfer
    
    const credit = await step.do(
      "credit-account-b",
      async () => {
        return await bankB.credit({
          accountId: toAccountId,
          amount,
          idempotencyKey: `${transferId}:credit-account-b`,
        });
      },
      {
        rollback: async ({ output }) => {
          if (output === undefined) {
            return;
          }
    
          await bankB.debit({
            accountId: toAccountId,
            amount,
            idempotencyKey: `${transferId}:rollback-credit-account-b`,
          });
        },
      }
    );
    
    
    // If we fail here, we may want to revert all previous payments. Users should not have to wrap their code in complex try-catch logic just to revert two small payments (see below)
    
    await step.do("send-confirmation", async () => {
      await sendTransferConfirmation({ ... });
    });

ロールバック関数は、通常のWorkflowステップと同様に、か部門である必要があります。料金を払い戻しる場合は、支払プロバイダーの識別キーを使用します。インベントリをリリースする場合、リリースを複数回呼び出すことができるようにします。

いずれかのステップが失敗すると、ロールバックハンドラは逆の`ステップ-開始`順序で実行されます。それはシンプルに聞こえます。何かが失敗する時に、元に戻すステップを実行するだけです。実際には、APIと実行モデルを重要にする詳細がいくつかあります。

1.**失敗したステップは、まだロールバックが必要である場合があります。** 失敗した`step.do()`ロールバックハンドラを登録すれば、ロールバック対象になることができます。

ユーザーコードがエラーを検知してWorkflowが続行する場合は、ロールバックは開始されませんが、ステップエラーが検知されて、その後Workflowが別の理由で失敗した場合、ロールバックは以前登録されたハンドラに対してまだ実行できます。これは逆の`step-start`順序で実行されます。

なぜでしょうか？このステップは、外部システムと部分的に対話している可能性があります。たとえば、決済プロバイダーは請求をキャプチャできますが、Workflowsに`chargeId`を返す前に、このステップが失敗することがあります。そのため、ロールバックハンドラーは`output`を受け取りますが、`output === undefined`を処理しなければなりません。

2\. **ロールバックは、Workflowが失敗した場合にのみ始まります。** ロールバックハンドラーを追加しても、すべてのステップエラーがロールバックをトリガーするわけではありません。ユーザーコードがエラーを検知して続行する場合、Workflowは続行します。ロールバックは、Workflow自体が最終的に障害に直面しつつある時点から始まります。

ロールバックが開始されると、Workflowsは条件を満たす`step.do()`を見つけますロールバックハンドラを実行し、最終的なWorkflowの障害を記録します。

3\. **順序は予測可能である必要があります。** 時系列のWorkflowsでは、ロールバック順序は当然のことのように感じられます：

  1. 在庫確保。
  2. 請求カード。
  3. 配送を作成します。
  4. 出荷に失敗した場合は、カードを返金し、在庫をリリースします。



パラレルステップを踏むことで、これはより巧妙になります。完了順序は開始順序と異なる場合があるため、Workflowsは、逆の完了順序ではなく、逆のステップ開始順序を使用します。

実用的なルールは次のとおりです。

  1. ロールバックハンドラを使用して開始または完了したステップが対象です。
  2. ロールバックハンドラーを登録されている場合、失敗した`step.do()`も対象となります。
  3. ハンドラは完了順ではなく、逆のステップ開始順で実行されます。



## APIの設計方法

想定される動作を想定したら、この新しいパターンをWorkflows APIに追加する必要がありました。ロールバックは、`ロールバックオプション`にたどり着くまでに、いくつかのイテレーションを経ました。

### なぜAPIが流暢またはビルダーのAPIではないのか？

最初のアプローチは、流暢な形式でした。`step.do(...).rollback(...)` 読みやすいです。フォワードアクションと報酬は隣にあり、呼び出しサイトは通常のJavaScriptの連鎖のように見えます。

問題は、`step.do()` です。耐久性のあるステップを開始し、ステップ出力のPromiseを返すため、すでに重要な意味を持っています。Workersでは、Workers RPCが[ _Cap'n Proto_](https://capnproto.org/rpc.html#time-travel-promise-pipelining) のようなシステムから継承されたパターンである[ _promise pipelining_](https://blog.cloudflare.com/capnweb-javascript-rpc-library/#chained-calls-promise-pipelining)をサポートしているため、promiseのような値が特に意味を持ちます。

約束パイプラインを使用すると、コードは将来の値が呼び出し元に完全に返される前に、将来の値に対してメソッドを呼び出すことができます。たとえば：
    
    
    const session = api.authenticate(apiKey);
    const name = await session.whoami();

ここでは、`セッション`はまだ実際のセッションオブジェクトではありません。これは、まもなく存在するセッションのハンドラーのようなものです。`session.whoami()`を呼び出すと、Workersは、この呼び出しをリモート側に早く送信して、「認証がセッションを作成したら、`whoami()`を呼び出してください」と言うことができます。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3317 image4](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW9WMVWKS68D8HCFGVRZQ2RA.png&w=715&h=476&f=webp&fit=cover&position=center)

これにより、ラウンドトリップが節約できます。呼び出し元は、`authenticate()`が完全に終了するのを待ってから`whoami()`を問い合わせる必要がありません。

Cloudflareは、流暢なAPIと考えました。
    
    
    step.do("charge-card", chargeCard).rollback(refundCharge);

  
読者には、それが「`charge-card`の結果に対して`.rollback()` を呼び出す」ことのように見えるかもしれません。ただし、ロールバックはステップの出力の一部ではありません。これは、`step.do()`の一部です。ステップが開始する前に登録されているため、Workflowsは、後のステップが失敗した場合にそのステップを修正する方法を知っています。

また、流暢なAPIは、ステップのタイミングを考えるのを難しくします。現在、`step.do()`呼び出されたときにステップを開始するため、開発者はステップを開始してから他の作業を行い、後で最初のステップを待つことができます。
    
    
    const first = step.do("first", () => serviceA.call());
    
    await step.do("second", () => serviceB.call());
    
    await first;

現在の実行モデルでは、`1つ目`はすぐに始まり、`2番目`です。流暢なAPIはそれをさらに複雑にします。Workflowsは、`.rollback()` を実行するかどうかを確認するために待機する必要があります。完全なステップ定義を知る前に付加されます。それにより、ステップがエンジンに送信される時間が遅れる可能性があります。

先の例では、`second`の完了後、`first`は`step.do("first", ...)`からではなく、`await first`から開始される可能性があります。

このため、同時実行されるWorkflowsの理解が難しくなります。ステップのタイミングは、返された`Promise`が消費されるタイミングだけでなく、`step.do()`が呼び出される場所にも依存することになります。

また、ビルダースタイルのAPIも検討しました。
    
    
    const charge = await step
    	.saga("charge")
    	.do(() => chargeCard())
    	.rollback(() => refundCharge())
    	.run();

ビルダーAPIは、`Promise`の曖昧さを回避します。また、将来のステップレベルの選択肢が明確で、フォワードアクションとロールバックアクションが同じ収集ステップに属していることも明確になっています。

しかし、それはセレモニーを増すことにもなります。各ステップの最後には必ず`.run()`を記述する必要があります。`.run()`を書き忘れることは容易ですが、ツールを使わなければそのミスに気づくのは困難であり、単純な1ステップのケースでさえ、設定の連鎖のように見えてしまうようになります。また、新しい`step.saga()`ビルダーが導入され、従来の`step.`パターンから脱却しています。何よりも重要なのは、これにより`step.do()`が、Workflowsの主要なプリミティブというよりは、むしろ古いAPIのように感じられてしまう点です。ロールバックの目的は、`step.do()`を拡張することであり、置き換えることではありませんでした。

### ステップメタデータとしてロールバック
    
    
    step.do(..., { rollback })

最終的に、ロールバックがステップのメタデータになる明示的な形式を選びました。

このように、各ロールバックは前進ステップ自体の中で定義されます。各ハンドラは、ロールバック開始の原因となったエラー、[ _ステップコンテキスト_](https://developers.cloudflare.com/workflows/build/step-context/)、および出力を受け取ります。これらは、フォワードステップによって返された永続的な値（未定義である場合があります）、またはステップが値を永続化する前に失敗した場合は未定義となります。

ロールバックはライフサイクルイベントを発生させるため、代替が開始されたか、どのロールバックハンドラが失敗したか、そしてロールバックが正常に完了したかを把握できます。

重要なのは、元のWorkflowの障害が別個に残っていることです。ロールバックは障害発生後にWorkflowsが行うことであり、Workflowの障害が発生した理由ではありません。

`WorkflowStepConfig`を介して[ _ステップ設定_](https://developers.cloudflare.com/workflows/build/workers-api/#workflowstepconfig)でカスタムの再試行動作とタイムアウト動作を定義できるのと同様に、`rollbackConfig`にロールバック固有の値を追加します。
    
    
    {
      rollback: async ({ output }) => {
        await bankA.credit({ accountId: fromAccountId, amount, transferId: `${transferId}-reversal` });
      },
      rollbackConfig: {
        retries: { limit: 10, delay: '30 seconds', backoff: 'exponential' },
        timeout: '2 minutes',
      },
    }

これは、当社が求めていたライフサイクルイベントのメンタルモデルに一致しています。`step.do()`は、Workflowsが記録し、再試行し、そして後でログに表示する耐久性のある作業単位をすでに記述しています。ロールバックは、同じ作業単位の別のライフサイクル動作です。別のラッパーやビルダー内ではなく、ステップ定義と共に移動する必要があります。

  * ステップは、`step.do()`が通常開始されるときに開始されます。
  * 返された約束は、依然としてステップの出力を表します。
  * 同時実行Workflowコードは、同じ実行モデルを保持します。
  * ロールバックハンドラの横にあるロールバックライブのリトライとタイムアウトのオプション。
  * 既存の`step.do()`の呼び出しは、現在とまったく同じように動作し続けます。



この形は、流暢なAPIよりも若干明示的ですが、この明確さは便利です。オペレーションとその報酬は依然として一箇所にあり、APIは新しいステップビルダーや新しい種類のプロミスを導入するものではありません。すでに`step.do()`を理解している開発者は、追加で`options`オブジェクトを1つ学ぶだけで済みます。

これは魔法のようではありませんが、採用が簡単で、理解しやすいのです。

## 内部の仕組み

ロールバックは小さなAPIの追加のように感じられますが、各ステップについてWorkflowsが記録する必要があるものが変化します。

定期的な`step.do()`すでに耐久性のあるレコードがあります。Workflowsは、ステップが開始されたか、完了したか、返されたか、またWorkflowが後で再開された場合に繰り返されるべきかどうかを記録します。

ロールバックは、そのレコードにもう1つ、ステップが報酬ロジックを登録済みかどうかを追加します。

つまり、Workflowsが失敗した場合に、Workflowsは2つの情報をまとめなければなりません。

1つ目は、**耐久性のあるステップ履歴** です。Workflowエンジンは、実行された内容、完了した内容、保存された出力内容、ロールバックが登録されたかどうかを把握するためのデータを保存します。

2つ目は、**ロールバックハンドラ** 自体で、そのステップを補完するために書かれた関数です。Workflowsは、その関数のテキストをデータとして保存しません。その代わり、Workflowの実行中に、ハンドラへの呼び出し可能な参照を保持します。

Workers RPCでは、この種の呼び出し可能な参照を[** _スタブ_**](https://developers.cloudflare.com/workers/runtime-apis/rpc/lifecycle)と呼びます。スタブリ込みとは、システムの一部が、別の場所で実行中のコードを呼び出すことを可能にします。また、スタブには有効期限があり、呼び出しや実行のコンテキストが終了すると処分できるようになっています。その時点を超えてスタブを保持する必要がある場合、Workers RPCは、同じターゲットに別のハンドルを作成する[` _dup()_`](https://developers.cloudflare.com/workers/runtime-apis/rpc/lifecycle/#the-dup-method)メソッドを提供します。

ロールバックには、このモデルが便利です。耐久性のあるステップ履歴に、報酬が必要なものを記録。ロールバックスタブにより、Workflowsは報酬コードを呼び出す方法を得ることができます。また、ロールバックハンドラーは、即時の`step.do()`よりも長く存続する必要があるため、Workflowsは、ロールバックフェーズのハンドラへの独自の呼び出し可能な参照を保持します。

一般的なケースでは、Workflowが同じエンジン有効期間内にロールバックに入る時、Workflowsには既に必要なロールバックスタブがあります。耐久性のあるステップ履歴を使用して対象となるステップを見つけ、フォワード実行中に登録されたロールバックスタブを呼び出すことができます。

これは、再起動後にWorkflowsが**回復する** 必要がある場合、より微妙になります。

ロールバックが必要な時にエンジンがエビクション、クラッシュ、または再起動した場合、Workflowsにはまだ耐久性のあるステップ履歴がありますが、メモリ内ロールバックスタブはなくなる可能性があります。Workflowsは、回復するために、**リプレイ** を使用します。これは、完了したフォワードステップ本文を再実行することなく、Workflowコードを再実行できるリカバリーモードです。

リプレイが完了した`step.do()`に達すると、Workflowsは、ステップ本文を再度実行する代わりに、永続化された結果を読み取ります。ロールバックリカバリーの場合、Workflowsは、ロールバックが付加されたステップのリビルドハンドラのみを必要とします。これらの`step.do()`はロールバックオプションにより、呼び出し可能なスタブを再び登録できます。

これにより、Workflowsは、元の外部のサイド効果を重複させることなく、必要なロールバックハンドラを回復することができます。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3317 image5](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW9WMK8HE1XEHVNX1B4RNK9W.png&w=715&h=699&f=webp&fit=cover&position=center)

これらの要素が整っていれば、ハンドラがメモリ上にまだ存在している場合でも、リカバリ中に再構築する必要がある場合でも、ロールバックは正常に機能します。

ワークフローが失敗しそうになった場合、Workflowsはアプリケーションに対して、何が起きたのかを再現するよう要求することはありません。すでにステップ履歴があります。保持された記録を見て、重要な質問に答えることができます。

  * どのステップから始まりましたか？
  * 完了したステップは？
  * 失敗したステップのどれが、まだクリーンアップが必要かもしれませんか？
  * 登録されたロールバックハンドラはどのステップか？
  * 各ロールバックハンドラはどの出力を受信すべきか？
  * 報酬はどのような順序で実行されるべきか？



次に、Workflowsは、ロールバックコンテキスト（オリジナルエラー、ステップコンテキスト、ステップ出力（永続化されている場合））を使用して、各ロールバックスタブを呼び出します。

順序の細部が重要です。通常のJavaScript、特に`Promise.all()`では、完了順序は、開始順序と同じではありません。ステップAが最初に始まり、ステップBが2番目に始まる場合、ステップBが最初に完了するかもしれません。ロールバックの際、Workflowsは、保存された開始順序を安定した信頼できる情報源として使用し、逆に展開します。

ロールバックハンドラーは、Workflowsの通常のステップ機械も実行します。つまり、報酬は、Workflowsに期待されるのと同じ運用プロパティ（リトライ、タイムアウト、ライフサイクルイベント、ログ、記録された最終的な結果）が得られるということです。ロールバックハンドラーが設定されたリトライ後に失敗し続けると、Workflowsはロールバックの結果を失敗として記録し、残りのロールバックハンドラの実行を停止し、Workflowインスタンスは最終的に`Errored`状態になります。

これは、サガロールバックと`キャッチ`ブロックの主な違いです。Catchブロックは、JavaScript実行の正確な時点でまだメモリにあるもの`だけ`がわかります。Workflowsのロールバックは、残っているステップ履歴を使用して、すでに何が起こったかを判断し、一般的なケースではすでにあるスタブを呼び出し、必要な場合はリカバリ中に不足しているスタブリを安全に再構築します。

また、それが理由で、このAPIでは`step.do()`自体にロールバック機能が実装されています。ロールバックは、別のグローバルなエラーハンドラーではありません。これは、Workflowsがすでに理解しているワークの耐久性のある単位にメタデータが付加されるものです。

## 今後の展開は？

ロールバックの最初のイテレーションには以下の内容が含まれます：

  * `step.do()`の明示的なステップごとのロールバックハンドラ
  * 順次ロールバック実行
  * 修正のための設定再試行とタイムアウト



次に、以下を探ります。

  * [` _waitForEvent_`](https://developers.cloudflare.com/workflows/build/events-and-parameters/#wait-for-events) のロールバックサポート
  * 並列ロールバック実行のサポート
  * [ _Python Workflows_](https://developers.cloudflare.com/workflows/python/)のサポートをロールバックする



マルチステップのアプリケーションが途中で失敗したとき、最も大変なのは、失敗した _こと_ に気づいていないことが多いのです。すでに何が起こったのか、次に何が起こる必要があるのかを _知る_ ことです。

SaaSロールバックを使用すると、その答えを各ステップの横に直接配置することができます。Workflowsでマルチステップのアプリケーションを構築している場合、s頻度のロールバックを試し、次に必要な報酬パターンを教えてください。[ _Workflowsドキュメント_](https://developers.cloudflare.com/workflows/)の利用を開始し、[ _Cloudflareコミュニティ_](https://community.cloudflare.com/)でフィードバックを共有してください。

このページ

オンラインで議論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Frollbacks-for-workflows%2F&t=%E5%BD%93%E7%A4%BE%E3%81%8CCloudflare%20Workflows%E3%81%AE%E9%98%B2%E5%BE%A1%E3%83%AD%E3%83%BC%E3%83%AB%E3%83%90%E3%83%83%E3%82%AF%E3%82%92%E3%81%A9%E3%81%AE%E3%82%88%E3%81%86%E3%81%AB%E6%A7%8B%E7%AF%89%E3%81%97%E3%81%9F%E3%81%8B)[](https://x.com/intent/post?text=%E5%BD%93%E7%A4%BE%E3%81%8CCloudflare+Workflows%E3%81%AE%E9%98%B2%E5%BE%A1%E3%83%AD%E3%83%BC%E3%83%AB%E3%83%90%E3%83%83%E3%82%AF%E3%82%92%E3%81%A9%E3%81%AE%E3%82%88%E3%81%86%E3%81%AB%E6%A7%8B%E7%AF%89%E3%81%97%E3%81%9F%E3%81%8B&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Frollbacks-for-workflows%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Frollbacks-for-workflows%2F)[](https://bsky.app/intent/compose?text=%E5%BD%93%E7%A4%BE%E3%81%8CCloudflare+Workflows%E3%81%AE%E9%98%B2%E5%BE%A1%E3%83%AD%E3%83%BC%E3%83%AB%E3%83%90%E3%83%83%E3%82%AF%E3%82%92%E3%81%A9%E3%81%AE%E3%82%88%E3%81%86%E3%81%AB%E6%A7%8B%E7%AF%89%E3%81%97%E3%81%9F%E3%81%8B+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Frollbacks-for-workflows%2F)[](https://mastodonshare.com/?text=%E5%BD%93%E7%A4%BE%E3%81%8CCloudflare+Workflows%E3%81%AE%E9%98%B2%E5%BE%A1%E3%83%AD%E3%83%BC%E3%83%AB%E3%83%90%E3%83%83%E3%82%AF%E3%82%92%E3%81%A9%E3%81%AE%E3%82%88%E3%81%86%E3%81%AB%E6%A7%8B%E7%AF%89%E3%81%97%E3%81%9F%E3%81%8B&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Frollbacks-for-workflows%2F)[](https://www.threads.net/intent/post?text=%E5%BD%93%E7%A4%BE%E3%81%8CCloudflare+Workflows%E3%81%AE%E9%98%B2%E5%BE%A1%E3%83%AD%E3%83%BC%E3%83%AB%E3%83%90%E3%83%83%E3%82%AF%E3%82%92%E3%81%A9%E3%81%AE%E3%82%88%E3%81%86%E3%81%AB%E6%A7%8B%E7%AF%89%E3%81%97%E3%81%9F%E3%81%8B+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Frollbacks-for-workflows%2F)

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
