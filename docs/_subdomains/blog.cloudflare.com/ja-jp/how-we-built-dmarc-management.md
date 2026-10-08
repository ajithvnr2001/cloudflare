---
url: https://blog.cloudflare.com/ja-jp/how-we-built-dmarc-management/
title: Cloudflare Workers\u3092\u4f7f\u7528\u3057\u305fDMARC\u7ba1\u7406\u306e\u69cb\u7bc9\u65b9\u6cd5 | Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:42:18.171193+00:00
---

# Cloudflare Workersを使用したDMARC管理の構築方法 | Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/how-we-built-dmarc-management/

[ブログ](https://blog.cloudflare.com/ja-jp/)

[DMARC](https://blog.cloudflare.com/ja-jp/tag/dmarc/)[Security Week](https://blog.cloudflare.com/ja-jp/tag/security-week/)[セキュリティ](https://blog.cloudflare.com/ja-jp/tag/security/)1件1件タグを表示

4 タグタグを4件表示

  * 投稿タグ
  * [Security Week](https://blog.cloudflare.com/ja-jp/tag/security-week/)[セキュリティ](https://blog.cloudflare.com/ja-jp/tag/security/)[メールセキュリティ](https://blog.cloudflare.com/ja-jp/tag/email-security/)
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



[メールセキュリティ](https://blog.cloudflare.com/ja-jp/tag/email-security/)

[DMARC](https://blog.cloudflare.com/ja-jp/tag/dmarc/)[Security Week](https://blog.cloudflare.com/ja-jp/tag/security-week/)[セキュリティ](https://blog.cloudflare.com/ja-jp/tag/security/)[メールセキュリティ](https://blog.cloudflare.com/ja-jp/tag/email-security/)

2023年3月17日

# Cloudflare Workersを使用したDMARC管理の構築方法

![André Cruz](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46FAFHK5DDQ0GQPPQ92C3B.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Nelson Duarte](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49P72CGQX08FQC903Q0E4F.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[André Cruz](https://blog.cloudflare.com/ja-jp/author/andre-cruz/)、[Nelson Duarte](https://blog.cloudflare.com/ja-jp/author/nelson-duarte/)

12分で読了

URLをコピー

この記事は以下でも利用可能です [English](https://blog.cloudflare.com/how-we-built-dmarc-management/)、[Deutsch](https://blog.cloudflare.com/de-de/how-we-built-dmarc-management/)、[Español](https://blog.cloudflare.com/es-es/how-we-built-dmarc-management/)、[Français](https://blog.cloudflare.com/fr-fr/how-we-built-dmarc-management/)、[한국어](https://blog.cloudflare.com/ko-kr/how-we-built-dmarc-management/)、[繁體中文](https://blog.cloudflare.com/zh-tw/how-we-built-dmarc-management/)、[简体中文](https://blog.cloudflare.com/zh-cn/how-we-built-dmarc-management/).

![How we built DMARC Management using Cloudflare Workers](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45VEZPBHGFF89NHRCXR27K.png&w=1201&h=676&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/vvo+fbi7uvV6ObO6ujQ7+3W7+zW6ebQ//vp+vXj7ujW5uDO6OPR7ujX7+nW6uTQ//3r/fbl7+bX5tzP6N3S7uXY8OfY7OTR///v//jo8+ja6dzS6t3V8OXb8+jb8ObU///z//3s+O7f7uPX7+TZ9evf+O7f9evZ///3///x/vXk9ezc9u7e/PPj/fXj+vHe///6///0//zo+vXg/Pbh//vm//vn/ffi///7///2//7p/fjh/vrj//3o//3o//jj)

### DMARCレポートとは

[DMARC](https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-dmarc-record/)は、 Domain-based Message Authentication, Reporting, and Conformance の略です。これは、電子メール[フィッシング](https://www.cloudflare.com/en-gb/learning/access-management/phishing-attack/) および [スプーフィング](https://www.cloudflare.com/en-gb/learning/email-security/what-is-email-spoofing/)に対する保護に役立つ電子メール認証プロトコルです。

電子メールの送信時に、DMARCにより、ドメイン所有者は、[SPF](https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-spf-record/) (Sender Policy Framework) や [DKIM](https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-dkim-record/) (DomainKeys Identified Mail)など、どの認証方式を使用して、電子メールの信頼性を検証するかを指定するDNSレコードを設定できます。電子メールがこれらの認証チェックに失敗した場合、DMARCは、受信者の電子メールプロバイダーに、そのメッセージを隔離するか、完全に拒否するかのいずれかの処理方法を指示します。

電子メールのフィッシングやスプーフィング攻撃がより巧妙化し、蔓延している今日のインターネットにおいて、DMARCは、ますます重要になってきています。DMARCを導入することで、ドメイン所有者は、信頼の喪失、風評被害、金銭的損失など、これらの攻撃による悪影響から自社ブランドと顧客を保護できます。

DMARCは、フィッシングやスプーフィング攻撃からの保護に加え、 [レポート](https://www.rfc-editor.org/rfc/rfc7489)の機能も提供します。ドメイン所有者は、どのメッセージがDMARCチェックに合格したか、不合格になったか、およびこれらのメッセージの発信元など、メール認証アクティビティに関するレポートを受け取ることができます。

DMARC管理では、ドメインに対するDMARCポリシーの設定とメンテナンスを行います。効果的なDMARC管理には、メール認証活動の継続的な監視と分析、および必要に応じてDMARCポリシーの調整と更新を行う機能が必要です。

効果的なDMARC管理の主要な要素には、以下のものがあります：

  * DMARCポリシーの設定：ドメインのDMARCレコードを設定し、認証チェックに失敗したメッセージを処理するための適切な認証方法とポリシーを指定することが含まれます。DMARC DNSレコードとは、どのようなものかは、以下の通りです：



`v=DMARC1; p=reject; rua=mailto:dmarc@example.com`

これは、DMARCバージョン1を使用すること、DMARCチェックに失敗した場合、ポリシーは、メールを拒否すること、プロバイダーがDMARCレポートを送信するメールアドレスを指定します。

  * 電子メール認証アクティビティの監視：電子メールのセキュリティと配信到達性を確保し、業界標準や規制に準拠するために、DMARCレポートは、ドメイン所有者にとって重要なツールです。DMARCレポートを定期的に監視、分析することで、ドメイン所有者はメールの脅威を特定し、メールキャンペーンを最適化し、メール認証全体を改善できます。
  * 必要に応じた調整：DMARCレポートの分析に基づき、ドメイン所有者は、メールメッセージが適切に認証され、フィッシングやスプーフィング攻撃から確実に保護されるように、DMARCポリシーや認証方法を調整する必要がある場合があります。
  * メールプロバイダーやサードパーティベンダーとの連携：効果的なDMARC管理には、DMARCポリシーが適切に実装、実施されるように、メールプロバイダーやサードパーティベンダーとの協力が必要な場合があります。



本日、 [DMARC管理](https://blog.cloudflare.com/ja-jp/dmarc-management-ja-jp/)を開始しました。これが、構築方法です。

### 構築方法

クラウドベースのセキュリティおよびパフォーマンスソリューションのリーディングプロバイダーとして、私たちCloudflareは、製品のテストに特定のアプローチを採用しています。私たちは、当社独自のツールやサービスを「ドッグフーディング」し、つまり、そのツールやサービスを使用して、ビジネスを運営しているのです。これにより、お客様に影響を与える前に、問題やバグを特定できます。

開発者が当社のグローバルネットワーク上でコードを実行できるサーバーレスプラットフォームである[Cloudflare Workers](https://workers.cloudflare.com/)などの当社独自の製品を社内で使用しています。2017年の発売以来、Workersのエコシステムは大きく成長しました。現在、数千人もの開発者がこのプラットフォーム上でアプリを構築し、デプロイしています。Workersエコシステムの威力は、これまで、クライアントの近くで実行することが不可能、あるいは非現実的であった高度なアプリを開発者が構築できるようにする能力にあります。Workersは、APIの構築、動的コンテンツの生成、画像の最適化、リアルタイム処理の実行など、さまざまに使用することができます。その可能性は、事実上無限です。Workersを使用して、[Radar 2.0](https://blog.cloudflare.com/ja-jp/technology-behind-radar2-ja-jp/)などのサービスや、[Wildebeest](https://blog.cloudflare.com/welcome-to-wildebeest-the-fediverse-on-cloudflare/)などのソフトウェアパッケージを提供しました。

最近、当社の [Email Routing](https://developers.cloudflare.com/email-routing/)の製品が Workers と提携し、Workersスクリプトを介し、[受信メールを処理](https://blog.cloudflare.com/announcing-route-to-workers/)できるようになりました。 [ドキュメント](https://developers.cloudflare.com/email-routing/email-workers/) に記載されている通りです：「Email Workersで、Cloudflare Workersの力を活用して、メールを処理し、複雑なルールを作成するために必要なロジックを実装できます。これらのルールは、お客様がメールを受信したときに何が起こるかを決定します。」ルールと検証済みアドレスはすべて、当社の [API](https://developers.cloudflare.com/api/operations/email-routing-destination-addresses-list-destination-addresses)を介して設定できます。

簡単なEmail Workerとは、どのようなものかは、以下の通りです：

かなり簡単ですよね？
    
    
    export default {
      async email(message, env, ctx) {
        const allowList = ["friend@example.com", "coworker@example.com"];
        if (allowList.indexOf(message.headers.get("from")) == -1) {
          message.setReject("Address not allowed");
        } else {
          await message.forward("inbox@corp");
        }
      }
    }

プログラムに、受信メールを処理する機能が備わっているため、スケーラブルかつ効率的な方法で、DMARCレポートメールの受信を処理するのに最適な方法のように思えました。Email RoutingとWorkersは、世界中から無限の数のメールを受信するという激務をこなすことができます。必要なものの概要は以下の通りです：

  1. メール受信とレポート抽出
  2. 関連する詳細を分析プラットフォームに公開
  3. 生レポートを保存



Email Workerにより、#1を簡単に行うことができます。メール()ハンドラーを使用してワーカーを作成するだけです。このハンドラーは [SMTP](https://www.rfc-editor.org/rfc/rfc5321) エンベロープ要素、メールヘッダーを事前に解析したバージョン、生の電子メール全体を読み取るストリームを受け取ります。

#2では、Workersプラットフォームも、調べることができ、[Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/)を見つけることができます。適切なスキーマを定義する必要がありますが、これはレポートの中に含まれるものと、後で行う予定のクエリの両方に依存します。その後、[GraphQL](https://developers.cloudflare.com/analytics/graphql-api/)または[SQL](https://developers.cloudflare.com/analytics/analytics-engine/sql-api/)API のいずれかを使用してデータをクエリーできます。

#3では、 [R2](https://www.cloudflare.com/en-gb/products/r2/)オブジェクトストレージ以上のものを探す必要はありません。WorkersからR2にアクセスするのは[簡単](https://developers.cloudflare.com/r2/examples/demo-worker/)です。電子メールからレポートを抽出した後、今後のためにR2に保存します。

これをゾーンで有効にできるマネージドサービスとして構築し、利便性のためにダッシュボードインターフェイスを追加しましたが、実際にはすべてのツールが利用可能で、サーバー、スケーラビリティ、パフォーマンスを心配することなく、お客様自身のアカウントで、Cloudflare Workers上に独自のDMARCレポートプロセッサをデプロイできます。

### アーキテクチャ

[Email Workers](https://developers.cloudflare.com/email-routing/email-workers/) は、Email Routingの製品の機能です。Email Routingコンポーネントは全てのノードで実行されるため、ノードのうちのいずれかが、受信メールを処理できます。これは、全てのデータセンターからEmailイングレスBGPプレフィックスをアナウンスするため、重要です。Email Workerへのメールの送信は、Email Routingのダッシュボードでルールを設定するのと同じくらい簡単です。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1751 Embedded Image - qUt3Zo](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW465JK1BXGCB56J3DVNFMVG.png&w=715&h=410&f=webp&fit=cover&position=center)

Email Routingコンポーネントが、Workerに配信されるルールに一致する電子メールを受信すると、最近、オープンソース化された [workerd](https://github.com/cloudflare/workerd) ランタイムの内部バージョンに接続し、すべてのノード上で実行されます。このインタラクションを管理するRPCスキーマは、 [Capnproto](https://github.com/capnproto/capnproto) スキーマで定義されており、電子メールの本文の読み上げ時に、Edgeworkerにストリーミングできるようにします。Workerスクリプトがこの電子メールを転送することを決定した場合、Edgeworkerは、元のリクエストで送信された機能を使用して、Email Routingに接続します。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1751 Embedded Image - xo7GIP](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW472EZF80K47ZMXFN76TXDC.png&w=715&h=139&f=webp&fit=cover&position=center)

DMARCレポートのコンテキスでは、受信メールを処理する方法は、以下の通りです：
    
    
    jsg::Promise<void> ForwardableEmailMessage::forward(kj::String rcptTo, jsg::Optional<jsg::Ref<Headers>> maybeHeaders) {
      auto req = emailFwdr->forwardEmailRequest();
      req.setRcptTo(rcptTo);
    
      auto sendP = req.send().then(
          [](capnp::Response<rpc::EmailMetadata::EmailFwdr::ForwardEmailResults> res) mutable {
        auto result = res.getResponse().getResult();
        JSG_REQUIRE(result.isOk(), Error, result.getError());
      });
      auto& context = IoContext::current();
      return context.awaitIo(kj::mv(sendP));
    }
    

  1. 処理中のメールの受信者を取得します。これは使用されたRUAです。 RUAは、特定のドメインに関する、集約されたDMARC処理フィードバックをどこに報告する必要があるかを示すDMARC構成パラメータです。 この受信者は、メッセージの「to」属性で確認することができます。
  2. const ruaID = message.to
  3. DMARCのレポートを処理するドメイン数は無限なので、Workers KVを使用して各ドメインに関する情報を保存し、この情報をRUAでキーにしています。 また、このようなレポートを受け取る必要があるかどうか知ることができます。
  4. const accountInfoRaw = await env.KV_DMARC_REPORTS.get(dmarc:${ruaID})
  5. この時点で、解析するために電子メール全体をarrayBufferに読み込みます。レポートのサイズによっては、無料のWorkersプランの制限に引っかかるかもしれません。このような場合、この問題のない[Workers Unbound](https://www.cloudflare.com/en-gb/workers-unbound-beta/)リソースモデルに切り替えることをお勧めします。
  6. const rawEmail = new Response(message.raw)  
const arrayBuffer = await rawEmail.arrayBuffer()
  7. 生の電子メールを解析するには、特にMIME部分の解析が含まれます。これを可能にするライブラリが複数利用可能です。例えば、[postal-mime](https://www.npmjs.com/package/postal-mime)を使用することができます：
  8. const parser = new PostalMime.default()  
const email = await parser.parse(arrayBuffer)
  9. 電子メールを解析した結果、その添付ファイルにアクセスできるようになりました。これらの添付ファイルはDMARCレポートそのものであり、圧縮できます。最初にやることは、長期保存用に圧縮形式で[R2](https://developers.cloudflare.com/r2/data-access/workers-api/workers-api-usage/)に保存します。後日、再処理や興味深いレポートの調査に役立ちます。これは、R2バインディングでput()を呼び出すのと同じくらい簡単です。後で検索しやすくするために、レポートファイルは現在の時刻に基づいて、ディレクトリに分散しておくことをお勧めします。
  10. await env.R2_DMARC_REPORTS.put(  
`${date.getUTCFullYear()}/${date.getUTCMonth() + 1}/${attachment.filename}`,  
attachment.content  
)
  11. ここで、添付ファイルの MIME タイプを調べる必要があります。DMARCレポートの生の形式はXMLですが、圧縮することができます。この場合、最初に解凍する必要があります。DMARCレポーターファイルは、複数の圧縮アルゴリズムを使用することができます。MIMEタイプを使用して、どの圧縮アルゴリズムを使用すべきか、判断します。[Zlib](https://en.wikipedia.org/wiki/Zlib)で圧縮されたレポートには、[pako](https://www.npmjs.com/package/pako)が使用可能で、ZIPで圧縮されたレポートには、[unzipit](https://www.npmjs.com/package/unzipit)が、良い選択です。
  12. レポートの生の XML 形式を取得したので、[fast-xml-parser](https://www.npmjs.com/package/fast-xml-parser)は、それらを解析する上でうまく機能しました。以下は、DMARCレポートのXMLがどういうものかは、以下の通りです：
  13. これで、レポート内のすべてのデータがすぐに利用できるようになりました。これからどうするかは、データをどのように表示したいかに大きく依存します。当社の場合、目標は、レポートから抽出した有意義なデータをダッシュボードに表示することでした。そのため、エンリッチされたデータをプッシュできる分析プラットフォームが必要でした。[Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/)に入ります。Analytics Engineにより、Workersからデータを[送信](https://developers.cloudflare.com/analytics/analytics-engine/get-started/#3-write-data-from-your-worker)できるようになるため、このタスクに最適です。[GraphQL API](https://developers.cloudflare.com/analytics/graphql-api/)を公開し、その後、データとやりとりができます。このようにして、ダッシュボードに表示するデータを取得します。



将来的には、ワークフローに [Queues](https://developers.cloudflare.com/queues/)を統合して、レポートを非同期的に処理し、クライアントがレポートの完成を待つのを回避することも検討しています。
    
    
    const ruaID = message.to

Workersインフラストラクチャのみに依存してこのプロジェクトをエンドツーエンドで何とか実装を成し遂げ、スケーラビリティ、パフォーマンス、ストレージ、セキュリティの問題を心配することなく、重要なアプリケーションを構築することが可能であり、有利であることを証明できました。
    
    
    const accountInfoRaw = await env.KV_DMARC_REPORTS.get(dmarc:${ruaID})

### オープンソーシング
    
    
    const rawEmail = new Response(message.raw)
    const arrayBuffer = await rawEmail.arrayBuffer()

先に述べたように、お客様が有効化して、利用できるマネージドサービスを構築し、当社が、お客様に代わり、それを管理します。しかし、当社が行ったことはすべて、お客様のアカウントでデプロイできるため、お客様自身のDMARCレポートを管理できます。これは簡単で、無料です。これを支援するために、上記の方法でDMARCレポートを処理するWorkerのオープンソースバージョンを公開しています。 <https://github.com/cloudflare/dmarc-email-worker>
    
    
    const parser = new PostalMime.default()
    const email = await parser.parse(arrayBuffer)

データを表示するダッシュボードがない場合は、 WorkerからAnalytics Engineに[クエリー](https://developers.cloudflare.com/analytics/analytics-engine/worker-querying/)を行うことも可能です。また、リレーショナルデータベースに保存したい場合は、 [D1](https://developers.cloudflare.com/d1/platform/client-api/) が役立ちます。可能性は無限であり、これらのツールで何を構築するのかを見いだせたら嬉しく思います。
    
    
    await env.R2_DMARC_REPORTS.put(
        `${date.getUTCFullYear()}/${date.getUTCMonth() + 1}/${attachment.filename}`,
        attachment.content
      )

投稿してください、自身のものを作ってください、私たちは耳を傾けます。
    
    
    <feedback>
      <report_metadata>
        <org_name>example.com</org_name>
        <emaildmarc-reports@example.com</email>
       <extra_contact_info>http://example.com/dmarc/support</extra_contact_info>
        <report_id>9391651994964116463</report_id>
        <date_range>
          <begin>1335521200</begin>
          <end>1335652599</end>
        </date_range>
      </report_metadata>
      <policy_published>
        <domain>business.example</domain>
        <adkim>r</adkim>
        <aspf>r</aspf>
        <p>none</p>
        <sp>none</sp>
        <pct>100</pct>
      </policy_published>
      <record>
        <row>
          <source_ip>192.0.2.1</source_ip>
          <count>2</count>
          <policy_evaluated>
            <disposition>none</disposition>
            <dkim>fail</dkim>
            <spf>pass</spf>
          </policy_evaluated>
        </row>
        <identifiers>
          <header_from>business.example</header_from>
        </identifiers>
        <auth_results>
          <dkim>
            <domain>business.example</domain>
            <result>fail</result>
            <human_result></human_result>
          </dkim>
          <spf>
            <domain>business.example</domain>
            <result>pass</result>
          </spf>
        </auth_results>
      </record>
    </feedback>

### 最後に

この記事で、Workersのプラットフォームの理解を深めていただけたら幸いです。 今日、Cloudflareはこのプラットフォームを活用して、ほとんどのサービスを構築しています。お客様もそうすべきだと思います。

自由にオープンソースバージョンへ投稿して、それでお客様ができることを私たちに教えてください。

Email Routingは、Email Workers APIをより機能的に拡張することにも取り組んでいますが、これについては、近いうちに別のブログでお話しします。

このページ

オンラインで議論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fhow-we-built-dmarc-management%2F&t=Cloudflare%20Workers%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%97%E3%81%9FDMARC%E7%AE%A1%E7%90%86%E3%81%AE%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95)[](https://x.com/intent/post?text=Cloudflare+Workers%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%97%E3%81%9FDMARC%E7%AE%A1%E7%90%86%E3%81%AE%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fhow-we-built-dmarc-management%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fhow-we-built-dmarc-management%2F)[](https://bsky.app/intent/compose?text=Cloudflare+Workers%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%97%E3%81%9FDMARC%E7%AE%A1%E7%90%86%E3%81%AE%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fhow-we-built-dmarc-management%2F)[](https://mastodonshare.com/?text=Cloudflare+Workers%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%97%E3%81%9FDMARC%E7%AE%A1%E7%90%86%E3%81%AE%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fhow-we-built-dmarc-management%2F)[](https://www.threads.net/intent/post?text=Cloudflare+Workers%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%97%E3%81%9FDMARC%E7%AE%A1%E7%90%86%E3%81%AE%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fhow-we-built-dmarc-management%2F)

## 関連するタグ

[DMARC](https://blog.cloudflare.com/ja-jp/tag/dmarc/)[Security Week](https://blog.cloudflare.com/ja-jp/tag/security-week/)[セキュリティ](https://blog.cloudflare.com/ja-jp/tag/security/)[メールセキュリティ](https://blog.cloudflare.com/ja-jp/tag/email-security/)

SNS をフォロー

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 新しい投稿のお知らせを受け取るように登録する

メールアドレス

また、あなたのメールアドレスを共有したりすることはございません。

登録する

ご購読ありがとうございます！受信箱を確認して登録してください。
