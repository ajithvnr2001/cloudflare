---
url: https://blog.cloudflare.com/ja-jp/making-rust-workers-reliable/
title: Rust Workers\u3092\u4fe1\u983c\u6027\u3092\u9ad8\u3081\u308b\uff1aWasm-bindgen\u3067\u306e\u30d1\u30cb\u30c3\u30af\u3068\u56de\u5fa9\u3092\u4e2d\u65ad\u3059\u308b | Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:34:40.379013+00:00
---

# Rust Workersを信頼性を高める：Wasm-bindgenでのパニックと回復を中断する | Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/making-rust-workers-reliable/

[ブログ](https://blog.cloudflare.com/ja-jp/)

[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[Rust](https://blog.cloudflare.com/ja-jp/tag/rust/)[Rust Workers](https://blog.cloudflare.com/ja-jp/tag/rust-workers/)8件8件タグを表示

11 タグタグを11件表示

  * 投稿タグ
  * [Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[Rust](https://blog.cloudflare.com/ja-jp/tag/rust/)[Rust Workers](https://blog.cloudflare.com/ja-jp/tag/rust-workers/)[WASM](https://blog.cloudflare.com/ja-jp/tag/wasm/)[WebAssembly](https://blog.cloudflare.com/ja-jp/tag/webassembly/)[インターンシップ体験](https://blog.cloudflare.com/ja-jp/tag/internship-experience/)[エンジニアリング](https://blog.cloudflare.com/ja-jp/tag/engineering/)[オープンソース](https://blog.cloudflare.com/ja-jp/tag/open-source/)[信頼性](https://blog.cloudflare.com/ja-jp/tag/reliability/)[開発者](https://blog.cloudflare.com/ja-jp/tag/developers/)[開発者プラットフォーム](https://blog.cloudflare.com/ja-jp/tag/developer-platform/)
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



[WASM](https://blog.cloudflare.com/ja-jp/tag/wasm/)[WebAssembly](https://blog.cloudflare.com/ja-jp/tag/webassembly/)[インターンシップ体験](https://blog.cloudflare.com/ja-jp/tag/internship-experience/)[エンジニアリング](https://blog.cloudflare.com/ja-jp/tag/engineering/)[オープンソース](https://blog.cloudflare.com/ja-jp/tag/open-source/)[信頼性](https://blog.cloudflare.com/ja-jp/tag/reliability/)[開発者](https://blog.cloudflare.com/ja-jp/tag/developers/)[開発者プラットフォーム](https://blog.cloudflare.com/ja-jp/tag/developer-platform/)

[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[Rust](https://blog.cloudflare.com/ja-jp/tag/rust/)[Rust Workers](https://blog.cloudflare.com/ja-jp/tag/rust-workers/)[WASM](https://blog.cloudflare.com/ja-jp/tag/wasm/)[WebAssembly](https://blog.cloudflare.com/ja-jp/tag/webassembly/)[インターンシップ体験](https://blog.cloudflare.com/ja-jp/tag/internship-experience/)[エンジニアリング](https://blog.cloudflare.com/ja-jp/tag/engineering/)[オープンソース](https://blog.cloudflare.com/ja-jp/tag/open-source/)[信頼性](https://blog.cloudflare.com/ja-jp/tag/reliability/)[開発者](https://blog.cloudflare.com/ja-jp/tag/developers/)[開発者プラットフォーム](https://blog.cloudflare.com/ja-jp/tag/developer-platform/)

2026年4月22日

# Rust Workersを信頼性を高める：Wasm-bindgenでのパニックと回復を中断する

![Guy Bedford](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46EK56GG251YRHAXKS587V.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Hood Chatham](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DGCR56ZBCN9NTBRE18MF.webp&w=64&h=64&f=webp&fit=cover&position=center)![Logan Gatlin](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47MBZXTSY5013HEJC8611B.png&w=64&h=64&f=webp&fit=cover&position=center)

[Guy Bedford](https://blog.cloudflare.com/ja-jp/author/guy-bedford/)、[Hood Chatham](https://blog.cloudflare.com/ja-jp/author/hood/)、[Logan Gatlin](https://blog.cloudflare.com/ja-jp/author/logan-gatlin/)

13分で読了

URLをコピー

この記事は以下でも利用可能です [English](https://blog.cloudflare.com/making-rust-workers-reliable/)、[한국어](https://blog.cloudflare.com/ko-kr/making-rust-workers-reliable/)、[繁體中文](https://blog.cloudflare.com/zh-tw/making-rust-workers-reliable/)、[简体中文](https://blog.cloudflare.com/zh-cn/making-rust-workers-reliable/).

![BLOG-3145 Hero Image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48HQEZP84STFXFD0H3EBY7.png&w=2048&h=1152&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///////88O7x3uLt3eXz6e758/L19u/r//////7+5Ofzx9XuxNb01uP66ez38u7t//////7/2OH2rsjwqMj2w9j93+f77+3x////////1eL6psf0nsX6vdf/3uj/8PD2////////4Oz/t9T6sdT/y+P/5/H/9/f7////////8fr/1en/0ur/5Pb/9v7/////////////////7fr/7Pz/+P//////////////////////9///9v//////////////)

[_Rust Workers_](https://developers.cloudflare.com/workers/languages/rust/)は、RustをWebAssemblyにコンパイルすることでCloudflare Workersプラットフォーム上で動作しますが、私たちが発見したように、WebAssemblyにはいくつかの課題があります。パニックや予期せぬ中断が発生した場合、ランタイムが未定義の状態になることがあります。Rust Workersのユーザーにとって、パニックは従来から重大なことであり、インスタンスを汚染し、場合によってはWorkerを一定期間停止させる可能性さえありました。

これらの問題を検出して軽減することはできましたが、Rust Workerが予期せず失敗し、他のリクエストが失敗する可能性はわずかに残りました。Workerで処理されていないRustが1つのリクエストに影響を与えると、より広範な障害に発展して、同じ接続リクエストに影響を与えるか、あるいは新しい着信リクエストに影響を与え続ける可能性があります。この根本的な原因は、Rust Workersが依存するRustからJavaScriptへのバインディングを生成するコアプロジェクトwasm-bindgenと、組み込みの復旧セマンティックスの欠如でした。

この記事では、Rust Workersの最新バージョンが、この中断によるサンドボックスポイズニングを解決する包括的なWasmエラーリカバリをどのように処理するかをご紹介します。この成果は、[ _昨年_](https://blog.rust-lang.org/inside-rust/2025/07/21/sunsetting-the-rustwasm-github-org/)発足したwasm-bindgen組織内での共同作業の一環として、[ _wasm-bindgen_](https://github.com/wasm-bindgen/wasm-bindgen)に還元されました。まず、`panic=unwind`サポートにより、単一の失敗したリクエストが他のリクエストに悪影響を及ぼすことがないようにし、次に、Wasm上のRustコードが中断後に再実行されないことを保証するアボートリカバリーメカニズムを備えています。 

## 復旧時の初期緩和策

この分野における信頼性に対処するための最初の試みは、本番Rust WorkersでのRustパニックや中断によって引き起こされる障害を把握し、封じ込めることに焦点を当てました。Cloudflareでは、Worker内の障害状態を追跡し、後続のリクエストを処理する前にアプリケーション全体の再初期化をトリガーするカスタムRustパニックハンドラーを導入しました。JavaScript側では、これは、プロキシベースの間接費を使用して、RustとJavaScriptの呼び出し境界をラップし、すべてのエントリポイントが一貫してカプセル化されるようにする必要がありました。また、障害発生後にWebAssemblyモジュールを正しく再初期化するために、生成されたバインディングに的を絞った変更を行いました。

このアプローチはカスタムJavaScriptロジックに依存していましたが、信頼できる復旧が可能であることを実証し、実際に見られる永続的な障害モードを排除することができました。このソリューションは、バージョン0.6から開始するすべてのWorkersユーザーにデフォルトで出荷され、次のセクションで説明するより一般的なアップストリーム型の中断復旧メカニズムの基礎を築きました。

## WebAssembly Exception Handlingを使用した`pananc=unwind`の実装

上記の中断リカバリメカニズムは、Workerが障害に耐えられることを保証しますが、それはアプリケーション全体を再初期化することで実現されます。ステートレスなリクエストハンドラであれば、これで問題ありません。しかし、Durable Objectsのように、メモリに意味のある状態を保持するワークロードにとっては、再初期化はその状態を完全に失うことを意味します。1つのリクエストの1つのパニックが、他の同時リクエストで使用されているメモリ内の状態を消去する可能性があります。

ほとんどのネイティブRust環境では、パニックが解消されるため、デストラクチャが実行され、プログラムは状態を失うことなく回復することができます。WebAssemblyでは、従来は全く異なるものでした。`wasm32-unknown-unknown`経由で Wasm にコンパイルされた Rust は、デフォルトで`panic=abort`となるため、そのため、Rust Worker 内でパニックが発生すると、`unreachable`命令によって突然トラップが発生し、`WebAssembly.RuntimeError`と共にWasm から JS へ戻ります。

インスタンスの状態を破棄せずにパニックから回復するには、2023年にエンジンで広くサポートされるようになったWebAssembly 例外処理提案によって可能になったwasm-bindgenの`panic=unwind`サポートが`wasm32-unknown-unknown`に必要でした。

まず、`RUSTFLAGS='-Cpanic=unwind' cargo build -Zbuild-std`でコンパイルします。これにより、アンワインドをサポートする標準ライブラリが再構築され、適切なパニックアンワインドでコードが生成されます。たとえば：
    
    
    struct HasDropA;
    struct HasDropB;
    extern "C" {
        fn imported_func();
    }
    
    fn some_func() {
        let a = HasDropA;
        let b = HasDropB;
        imported_func();
    }

WebAssemblyをコンパイルします：
    
    
    try
      call <imported_func>
    catch_all
      call <drop_b>
      call <drop_a>
      rethrow
    end
    call <drop_b>
    call <drop_a>

これにより、`imported_func()` がパニックに陥っても、デストラクタは引き続き実行されます。同様に、`std::panic::catch_unwind(|| some_func())` は次のようにコンパイルされます。
    
    
    try
      call <some_func>
      ;; set result to Ok(return value)
    catch
      try
        call <std::panicking::catch_unwind::cleanup>
        ;; set result to Err(panic payload)
      catch_all
        call <core::panicking::cannot_unwind>
        unreachable
      end
    end

エンドツーエンドで機能させるには、wasm-bindgenツールチェーンにいくつかの変更を必要としました。WebAssemblyパーサーWalrusは、try/catch指示の処理方法を持っていなかったので、サポートを追加しました。また、記述子インタープリターにも、例外処理ブロックを含むコードを評価する方法を教育する必要がありました。その時点で、完全なアプリケーションは`panic=unwind`で構築することができます。

最後のステップは、wasm-bindgenによって生成されたエクスポートを修正し、Rust-JavaScriptの境界でパニックをキャッチして、JavaScript `PanicError` 例外として表面化させることでした。微妙な点に、Rustは`extern "C"`関数を使って解凍するときに外部の例外をキャッチして中断するため、エクスポートは`extern "C-unwind"`とマークして、境界を越えた解除を明示的に許可する必要があります。未来のために、パニックが`PanicError`でJavaScript`プロミス`を拒否します。

Closuresは、`panic=unwind`で構築された場合のみ`UnwindSafe`をチェックする新しい`MaybeUnwindSafe`トレイトによって、アンウィンドの安全性が適切にチェックされるように特別な注意が必要でした。しかし、これにより問題がすぐに浮き彫りになりました。多くのクロージャは、解除された後も残る参照を捕捉するため、本質的に安全でない参照をリクエストすることができるのです。ユーザーがコンパイラを満足させるためだけに、`AssertUnwindSafe` でクロージャーを誤ってラップするよう奨励される状況を回避するために、`Closure::new_aborting` バリアントを追加しました。これは、アンワインドの安全性が保証できない場合に、アンワインドする代わりにパニックで終了するものです。

パニック解除有効化：

  * エクスポートされたRust関数のパニックはWasm-bindgenで捕捉されます。
  * JavaScriptに対するパニック領域。PanicError 例外
  * 非同期エクスポートは、PanicErrorを使用して、返された約束を拒否します
  * Rustデストラクチャが正しく動作する
  * WebAssemblyインスタンスは有効で再利用可能なまま



このアプローチの詳細とwasm-bindgenでの使用方法については、[ _Wasm Bindgen: Catching Panics_](https://wasm-bindgen.github.io/wasm-bindgen/reference/catch-unwind.html)の最新ガイドページで取り上げられています。

## リカバリーを中断

`panic=unwind`をサポートしても、中断は依然として発生します。メモリ不足エラーは、よくある原因の一つです。ボットは解除できないため、ステートが回復できる可能性はまったくありませんが、少なくとも将来の操作のためにボットを検出して回復し、無効なステートが後続のリクエストをエラーにすることを回避することができます。

パニックに戻るサポートにより、リカバリーを中断する新しい問題が生じました。Wasmからエラーを受け取った場合、それが`extern “C-unwind”`外部エラーによるものなのか、それとも本物のAbortなのかはわかりません。WebAssemblyでは、Abortは様々な形を取ることができます。

これを技術的に解決する選択肢は2つありました。確実に中断されるすべてのエラーをマークするか、確実に解除されるすべてのエラーをマークするかのどちらかです。どちらも実現できましたが、私たちは後者を選択しました。既に私たちの海外例外処理は、生のWATレベル（WebAssemblyテキストフォーマット）の例外処理命令を直接使用していたため、外部例外の例外タグを実装することで、アンウィンド安全でない例外と区別する方が簡単であることがわかりました。

WebAssemblyの例外処理におけるこの`Exception.Tag`機能のおかげで、回復可能なエラーと回復不可能なエラーを明確に区別できるようになり、新しいアボートハンドラーとアボート再入可能ガードの両方を統合することができました。  
  
新しいAbortフック、`set_on_abort`を初期化時に使用し、プラットフォーム埋め込みのニーズに応じて回復するハンドラをアタッチできます。

無効な実行状態を回避するには、パニックと中断処理の強化が重要です。WebAssemblyを使用すると、コールスタックが深く相互作用し、WasmがJavaScriptを呼び出すことができ、JavaScriptが任意の深さでWasmに再侵入することができますが、これとともに複数のタスクを同じインスタンスで機能させることができます。以前は、1つのタスクやネストされたスタックで発生した中断が、JSを通じて上位のスタックを無効化することが保証されず、未定義の動作につながる可能性がありました。実行モデルを保証できるように注意を払う必要があり、この分野での貢献は継続的に続いています。

中断は決して理想的ではなく、障害発生時の再初期化は絶対に最悪のシナリオですが、最終防御線としてクリティカルエラーリカバリーを実装することで、実行の正確性を確保し、将来の操作を成功させることができます。無効な状態は持続しないため、単一の障害が複数の障害につながることはありません。

## 拡張：wasm-bindgenライブラリの再初期化を中断する

これに取り組んでいるうちに、これはwasm-bindgenで構築されたJSが使用するライブラリに共通する問題であり、回復を実行できるようにABORTハンドラーを付加することで恩恵を受けることがわかりました。

しかし、WasmをESモジュールとして構築して直接インポートする場合（例：import` { func }from 'wasm-dep'` ）、Wasm abortの復旧メカニズムは明確ではなく、すでにリンクされた`func()`を呼び出します。学習したと思いました。

厳密にはRust Workersのユースケースではありませんが、CloudflareのチームはRustに支えられたWasmライブラリの依存関係を実行する、JSベースのWorkersユーザーもサポートしています。この問題を同時に解決できれば、Cloudflare WorkersプラットフォームでのWasmの使用にも間接的に利益をもたらす可能性があります。

Wasmライブラリユースケースの自動中断リカバリをサポートするために、wasm-bindgen、`--reset-state-function`に実験的な再初期化メカニズムのサポートを追加しました。これにより、Rustアプリケーションが、生成されたバインディングのコンシューマーがそれらを再インポートまたは作成する必要なく、次の呼び出しのために内部のWasmインスタンスを初期の状態にリセットすることを効果的にリクエストできる関数が公開されます。古いインスタンスのクラスインスタンスは、ハンドリングがオーファンになると破棄されますが、その後、新しいクラスを構築することができます。Wasmライブラリを使用したJSアプリケーションはエラーになりますが、ブリッキングされていません。

この機能の技術的な詳細とwasm-bindgenでの使用方法については、新しいwasm-bindgenガイドのセクション[ _Wasm Bindgen: Handling Aborts_](https://wasm-bindgen.github.io/wasm-bindgen/reference/handling-aborts.html)で説明されています。

## Rust Wasm例外処理エコシステムの成熟

この取り組みのアップストリームの貢献は、wasm-bindgenプロジェクトだけにとどまりませんでした。`panwind=unwind`を使用したWasmの構築には、実験的な夜間のRustターゲットが必要です。そのため、当社はRustのWasmのWebAssembly Exception処理のサポートを発展させ、安定したRustに移行することにも取り組んできました。

WebAssemblyの例外処理の仕様策定過程において、最終段階での仕様変更により、2つのバリエーションが生まれました。それは、[ _従来の例外処理_](https://github.com/WebAssembly/exception-handling/blob/main/proposals/exception-handling/legacy/Exceptions.md)と、最終的に採用された最新の[ _「exnref」を用いた例外処理_](https://github.com/WebAssembly/exception-handling/blob/main/proposals/exception-handling/Exceptions.md)です。現在も、RustのWebAssemblyターゲットは依然としてレガシーバリアントのコードをデフォルトで生成しています。従来の例外処理は広くサポートされていますが、現在は非推奨となっています。

最新のWebAssembly例外処理は、以下のJSプラットフォームリリースにてサポートされています:

ランタイム| バージョン| リリース日  
---|---|---  
v8| 13.8.1| 2025年4月28日  
workerd| v1.20250620.0| 2025年6月19日  
Chrome| 138| 2025年6月28日  
Firefox| 131| 2024年10月1日  
Safari| 18.4| 2025年3月31日  
Node.js| 25.0.0| 2025年10月15日  
  
サポートマトリックスを調査していたところ、最大の懸念はNode.js 24 LTSのリリーススケジュールでした。これにより、エコシステム全体は2028年4月まで従来のWebAssembly例外処理から抜け出せません。

この矛盾を発見したことで、最新の例外処理をNode.js 24リリースにバックポートし、Node.js 22リリースラインでこのターゲットのサポートを確実にするために必要な修正をバックポートすることができました。これにより、最新の例外処理提案が来年のデフォルトのターゲットになるはずです。

今後数ヶ月の間に、安定した`panic=unwind`と最新の例外処理への移行を、エンドユーザーに可能な限り見えないようにする作業を進めます。

エコシステムへのこのような長期的な投資には時間がかかりますが、Rust WebAssemblyコミュニティ全体のより強力な基盤を構築するのに役立ちます。こうして改善に貢献できることを嬉しく思います。

## Rust Workersでパニック・アンワンドを使用する

Rust Workersのバージョン0.8.0より、新しい`--panic-unwind`フラグが利用可能になり、[ _こちらの指示_](https://github.com/cloudflare/workers-rs?tab=readme-ov-file#panic-recovery-with---panic-unwind)に従ってビルドコマンドに追加できます。

このフラグにより、パニックは完全に回復することができ、ボットリカバリーは新しいボット分類とリカバリーフックメカニズムを使用します。より安定したRust Workersの環境を実現するため、アップグレードして試してみることを強くお勧めします。また、今後のリリースでは`panic=unwind`をデフォルト設定にする予定です。`panic=abort` を引き続き使用するユーザーは、0.6.0 からの以前のカスタムリカバリーラッパー処理を引き続き利用できます。

## Rust Workersの安定性確保への取り組み

この作業は、Rust Workersの安定版リリースに向けた継続的な取り組みの一部です。Wasmプラットフォーム基盤のこれらの急激なエッジを根本から解決し、それが理にかなっているエコシステムに貢献することで、当社のプラットフォームだけでなく、Rust、JS、Wasmのエコシステム全体のより強固な基盤を構築します。

Rust Workersについては今後、数多くの改善を計画しており、まもなくこれらの追加機能に関する最新情報をお伝えする予定です。これには、先月、当チームのGuy Bedfordが[ _Wasm.ioでの「Rust & JS Interoperability」_](https://www.youtube.com/watch?v=zlSJY8Qv5XI)という講演で概要を紹介した、wasm-bindgenのジェネリクスや自動bindgenなども含まれます。

**#rust‑on‑workers** の[ _Cloudflare Discord_](https://discord.com/invite/cloudflaredev)でお会いしましょう。また、フィードバックや議論、特に[ _workers-rs_](https://github.com/cloudflare/workers-rs)と[ _wasm-bindgen_](https://github.com/wasm-bindgen/wasm-bindgen)のGitHubプロジェクトへの新しいコントリビューターも歓迎します。

このページ

オンラインで議論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fmaking-rust-workers-reliable%2F&t=Rust%20Workers%E3%82%92%E4%BF%A1%E9%A0%BC%E6%80%A7%E3%82%92%E9%AB%98%E3%82%81%E3%82%8B%EF%BC%9AWasm-bindgen%E3%81%A7%E3%81%AE%E3%83%91%E3%83%8B%E3%83%83%E3%82%AF%E3%81%A8%E5%9B%9E%E5%BE%A9%E3%82%92%E4%B8%AD%E6%96%AD%E3%81%99%E3%82%8B)[](https://x.com/intent/post?text=Rust+Workers%E3%82%92%E4%BF%A1%E9%A0%BC%E6%80%A7%E3%82%92%E9%AB%98%E3%82%81%E3%82%8B%EF%BC%9AWasm-bindgen%E3%81%A7%E3%81%AE%E3%83%91%E3%83%8B%E3%83%83%E3%82%AF%E3%81%A8%E5%9B%9E%E5%BE%A9%E3%82%92%E4%B8%AD%E6%96%AD%E3%81%99%E3%82%8B&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fmaking-rust-workers-reliable%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fmaking-rust-workers-reliable%2F)[](https://bsky.app/intent/compose?text=Rust+Workers%E3%82%92%E4%BF%A1%E9%A0%BC%E6%80%A7%E3%82%92%E9%AB%98%E3%82%81%E3%82%8B%EF%BC%9AWasm-bindgen%E3%81%A7%E3%81%AE%E3%83%91%E3%83%8B%E3%83%83%E3%82%AF%E3%81%A8%E5%9B%9E%E5%BE%A9%E3%82%92%E4%B8%AD%E6%96%AD%E3%81%99%E3%82%8B+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fmaking-rust-workers-reliable%2F)[](https://mastodonshare.com/?text=Rust+Workers%E3%82%92%E4%BF%A1%E9%A0%BC%E6%80%A7%E3%82%92%E9%AB%98%E3%82%81%E3%82%8B%EF%BC%9AWasm-bindgen%E3%81%A7%E3%81%AE%E3%83%91%E3%83%8B%E3%83%83%E3%82%AF%E3%81%A8%E5%9B%9E%E5%BE%A9%E3%82%92%E4%B8%AD%E6%96%AD%E3%81%99%E3%82%8B&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fmaking-rust-workers-reliable%2F)[](https://www.threads.net/intent/post?text=Rust+Workers%E3%82%92%E4%BF%A1%E9%A0%BC%E6%80%A7%E3%82%92%E9%AB%98%E3%82%81%E3%82%8B%EF%BC%9AWasm-bindgen%E3%81%A7%E3%81%AE%E3%83%91%E3%83%8B%E3%83%83%E3%82%AF%E3%81%A8%E5%9B%9E%E5%BE%A9%E3%82%92%E4%B8%AD%E6%96%AD%E3%81%99%E3%82%8B+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fmaking-rust-workers-reliable%2F)

## 関連するタグ

[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[Rust](https://blog.cloudflare.com/ja-jp/tag/rust/)[Rust Workers](https://blog.cloudflare.com/ja-jp/tag/rust-workers/)[WASM](https://blog.cloudflare.com/ja-jp/tag/wasm/)[WebAssembly](https://blog.cloudflare.com/ja-jp/tag/webassembly/)[インターンシップ体験](https://blog.cloudflare.com/ja-jp/tag/internship-experience/)[エンジニアリング](https://blog.cloudflare.com/ja-jp/tag/engineering/)[オープンソース](https://blog.cloudflare.com/ja-jp/tag/open-source/)[信頼性](https://blog.cloudflare.com/ja-jp/tag/reliability/)[開発者](https://blog.cloudflare.com/ja-jp/tag/developers/)[開発者プラットフォーム](https://blog.cloudflare.com/ja-jp/tag/developer-platform/)

SNS をフォロー

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 新しい投稿のお知らせを受け取るように登録する

メールアドレス

また、あなたのメールアドレスを共有したりすることはございません。

登録する

ご購読ありがとうございます！受信箱を確認して登録してください。
