---
url: https://blog.cloudflare.com/ja-jp/technical-breakdown-http2-rapid-reset-ddos-attack/
title: HTTP/2 Rapid Reset\uff1a\u8a18\u9332\u7684\u52e2\u3044\u306e\u653b\u6483\u3092\u7121\u52b9\u5316 | Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:36:17.946439+00:00
---

# HTTP/2 Rapid Reset：記録的勢いの攻撃を無効化 | Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/technical-breakdown-http2-rapid-reset-ddos-attack/

[ブログ](https://blog.cloudflare.com/ja-jp/)

[DDoS](https://blog.cloudflare.com/ja-jp/tag/ddos/)[Vulnerabilities](https://blog.cloudflare.com/ja-jp/tag/vulnerabilities/)[セキュリティ](https://blog.cloudflare.com/ja-jp/tag/security/)2件2件タグを表示

5 タグタグを5件表示

  * 投稿タグ
  * [DDoS](https://blog.cloudflare.com/ja-jp/tag/ddos/)[セキュリティ](https://blog.cloudflare.com/ja-jp/tag/security/)[傾向](https://blog.cloudflare.com/ja-jp/tag/trends/)[攻撃](https://blog.cloudflare.com/ja-jp/tag/attacks/)
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



[傾向](https://blog.cloudflare.com/ja-jp/tag/trends/)[攻撃](https://blog.cloudflare.com/ja-jp/tag/attacks/)

[DDoS](https://blog.cloudflare.com/ja-jp/tag/ddos/)[Vulnerabilities](https://blog.cloudflare.com/ja-jp/tag/vulnerabilities/)[セキュリティ](https://blog.cloudflare.com/ja-jp/tag/security/)[傾向](https://blog.cloudflare.com/ja-jp/tag/trends/)[攻撃](https://blog.cloudflare.com/ja-jp/tag/attacks/)

2023年10月10日

# HTTP/2 Rapid Reset：記録的勢いの攻撃を無効化

![Lucas Pardue](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44S1ZEGFAAY82ZM1A53KHB.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Julien Desgats](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW490NXEPS0Y3GYM6MEBDP98.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Lucas Pardue](https://blog.cloudflare.com/ja-jp/author/lucas/)、[Julien Desgats](https://blog.cloudflare.com/ja-jp/author/julien-desgats/)

25分で読了

URLをコピー

この記事は以下でも利用可能です [English](https://blog.cloudflare.com/technical-breakdown-http2-rapid-reset-ddos-attack/)、[Deutsch](https://blog.cloudflare.com/de-de/technical-breakdown-http2-rapid-reset-ddos-attack/)、[Español](https://blog.cloudflare.com/es-es/technical-breakdown-http2-rapid-reset-ddos-attack/)、[Français](https://blog.cloudflare.com/fr-fr/technical-breakdown-http2-rapid-reset-ddos-attack/)、[한국어](https://blog.cloudflare.com/ko-kr/technical-breakdown-http2-rapid-reset-ddos-attack/)、[繁體中文](https://blog.cloudflare.com/zh-tw/technical-breakdown-http2-rapid-reset-ddos-attack/)、[简体中文](https://blog.cloudflare.com/zh-cn/technical-breakdown-http2-rapid-reset-ddos-attack/).

![BLOG-2023 Embedded Image - mLN7qf](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48WDXXVR9MBXJX2BC6M78M.png&w=1600&h=901&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////////9PLz5+br4uPt5Ofz6O3z6+/v////////7Orx19bm0NHn2Nvu5Ojx6+/w////////5OPxxsXivsDiztHq4eTx7fDy////////4+P0wcHkurzjztDs5Of08fT2////////7Oz6z9Dty8zt29307fD69/r7////////+vr/5uf65OX67/D/+fz//v//////////////+vv/+fr/////////////////////////////////////////////)

2023年8月25日以降、当社では、多くのお客様を襲った異常に大規模なHTTP攻撃を目撃し始めました。これらの攻撃は当社の自動DDoSシステムによって検知され、軽減されました。しかし、これらの攻撃が記録的な規模に達するまで、それほど時間はかかりませんでした。その規模は、[過去に記録された最大の攻撃](https://blog.cloudflare.com/ja-jp/cloudflare-mitigates-record-breaking-71-million-request-per-second-ddos-attack-ja-jp/)の約3倍にも達したのです。

 _攻撃を受けているか、追加の防御が必要ですか？[支援を受けるには、こちらをクリックしてください](https://www.cloudflare.com/h2/)。_  


懸念となるのは、攻撃者がわずか2万台のボットネットでこの攻撃を実行できたという事実です。今日、数万台から数百万台のマシンで構成されるボットネットが存在しています。Web上では全体として通常1秒間に10億から30億のリクエストしかないことを考えると、この方法を使えば、Webのリクエスト全体を少数のターゲットに集中させることができます。

## 検出と軽減

これは前例のない規模の斬新な攻撃ベクトルでしたが、Cloudflareの既存の保護システムは攻撃の矛先をほぼ吸収することができました。当初はお客様のトラフィックに若干の影響が見られたものの（攻撃の初期波ではリクエストのおよそ1％に影響）、現在では緩和方法を改良し、当社のシステムに影響を与えることなく、Cloudflareのすべてのお客様に対する攻撃を阻止することができるようになりました。

当社は、業界の最大手であるGoogleとAWSの2社と同時に、この攻撃に気づきました。当社はCloudflareのシステムを強化し、今日ではすべてのお客様がこの新しいDDoS攻撃手法から保護され、お客様への影響がないことを確認しました。当社はまた、グーグルやAWSとともに、影響を受けるベンダーや重要インフラストラクチャプロバイダーへの攻撃に関する協調的な情報開示に参加しました。

この攻撃は、HTTP/2プロトコルのいくつかの機能とサーバー実装の詳細を悪用することで行われました（詳細は、[CVE-2023-44487](https://www.cve.org/CVERecord?id=CVE-2023-44487)をご覧ください）。この攻撃はHTTP/2プロトコルにおける根本的な弱点を悪用しているため、HTTP/2を実装しているすべてのベンダーがこの攻撃の対象になると考えられます。これには、すべての最新のWebサーバーも含まれます。当社は、GoogleとAWSとともに、Webサーバーベンダーがパッチを実装できるよう、攻撃方法を開示しました。一方で、Webに面したWebやAPIサーバーの前段階に設置されるCloudflareのようなDDoS軽減サービスを利用するのが最善の防御策とります。

この投稿では、HTTP/2プロトコルの詳細、攻撃者がこれらの大規模な攻撃を発生させるために悪用した機能、およびすべてのお客様が保護されていることを保証するために当社が講じた緩和策について詳細を掘り下げて紹介します。これらの詳細を公表することで、影響を受ける他のWebサーバーやサービスが緩和策を実施するために必要な情報を得られることを期待しています。そしてさらに、HTTP/2プロトコル規格チームや、将来のWeb規格に取り組むチームには、こうした攻撃を防ぐためHTTP/2プロトコルの設計改善に役立てていただければと思っています。

## RST攻撃の詳細

HTTPは、Webを稼働するにあたって用いられるアプリケーションプロトコルです。[HTTPセマンティクス](https://www.rfc-editor.org/rfc/rfc9110.html)とは、リクエストとレスポンスメッセージ、メソッド、ステータスコード、ヘッダーフィールドとトレーラフィールド、メッセージコンテンツなど、全体的なアーキテクチャ、用語、プロトコルの側面に関し、あらゆるバージョンに共通しています。個々のHTTPバージョンでは、セマンティクスをインターネット上でやりとりするための「ワイヤーフォーマット」に変換する方法を定義しています。例えば、クライアントはリクエストメッセージをバイナリデータにシリアライズして送信し、サーバーがこれを解析して処理可能なメッセージに戻します。

[HTTP/1.1](https://www.rfc-editor.org/rfc/rfc9112.html)は、テキスト形式のシリアライズを使用します。リクエストメッセージとレスポンスメッセージはASCII文字のストリームとしてやりとりされ、TCPのような信頼性の高いトランスポートレイヤーを介して、以下の[フォーマット](https://www.rfc-editor.org/rfc/rfc9112.html#section-2.1)で送信されます（「CRLF」はキャリッジリターンとラインフィードを意味します）：
    
    
     HTTP-message   = start-line CRLF
                       *( field-line CRLF )
                       CRLF
                       [ message-body ]

例えば、ワイヤ上の非常に簡単なGETリクエストは、`https://blog.cloudflare.com/`となります：

`GET / HTTP/1.1 CRLFHost: blog.cloudflare.comCRLFCRLF`

そして、応答は次のようなものになります：

`HTTP/1.1 200 OK CRLFServer: cloudflareCRLFContent-Length: 100CRLFtext/html; charset=UTF-8CRLFCRLF<100 bytes of data>`

このフォーマットは、ワイヤ上でメッセージを**フレーム** 化します。つまり、1つのTCP接続を使って複数のリクエストとレスポンスをやり取りすることが可能になります。しかし、このフォーマットでは、各メッセージがまとめて送信される必要があります。さらに、リクエストと応答を正しく関連付けるために、厳密な順序が要求されます。つまり、メッセージは順序だてて交換され、多重化することはできません。`https://blog.cloudflare.com/`、`https://blog.cloudflare.com/page/2/`の2つのGETリクエストは、次のようになります：

`GET / HTTP/1.1 CRLFHost: blog.cloudflare.comCRLFCRLFGET /page/2/ HTTP/1.1 CRLFHost: blog.cloudflare.comCRLFCRLF`

レスポンスは、次のようになります：

`HTTP/1.1 200 OK CRLFServer: cloudflareCRLFContent-Length: 100CRLFtext/html; charset=UTF-8CRLFCRLF<100 bytes of data>CRLFHTTP/1.1 200 OK CRLFServer: cloudflareCRLFContent-Length: 100CRLFtext/html; charset=UTF-8CRLFCRLF<100 bytes of data>`

Webページでは、これらの例よりも複雑なHTTPインタラクションが必要となります。Cloudflareブログにアクセスすると、ブラウザは複数のスクリプト、スタイル、メディアアセットを読み込みます。HTTP/1.1を使ってトップページを訪れ、すぐに2ページ目に移動した場合、ブラウザは2つの選択肢から選ぶことになります。ページ2が始まる前に、ページに対するキューに入れられたものでもう必要のないものすべての応答を待つか、TCP接続を閉じて新しい接続を開くことで、実行中のリクエストをキャンセルすることのいずれかとなります。どちらも、あまり現実的ではありません。ブラウザは、TCP接続のプール（ホストあたり最大6つ）を管理し、プール上で複雑なリクエストディスパッチロジックを実装することによって、これらの制限を回避する傾向があります。

[HTTP/2](https://www.rfc-editor.org/rfc/rfc9113)は、HTTP/1.1の多くの問題に対処しています。各HTTPメッセージは、型、長さ、フラグ、ストリーム識別子（ID）と悪意のあるペイロードを持つ**HTTP/2フレーム** のセットにシリアライズされます。ストリームIDは、ワイヤ上のどのバイトがどのメッセージに適用されるかを明確にし、安全な多重化と同時実行を可能にします。ストリームは、双方向となります。クライアントはフレームを送信し、サーバーは同じIDを使ったフレームを返信します。

HTTP/2では、`https://blog.cloudflare.com`への当社のGETリクエストはストリームID 1でやり取りされ、クライアントは1つの[HEADERS](https://www.rfc-editor.org/rfc/rfc9113#name-headers)フレームを送信し、サーバーは1つのHEADERSフレームと、それに続く1つ以上の[DATA](https://www.rfc-editor.org/rfc/rfc9113#name-data)フレームで応答します。クライアントのリクエストは常に奇数番号のストリームIDを使用するので、後続のリクエストはストリームID 3、5、...を使用することになります。レスポンスはどのような順番でも提供することができ、異なるストリームからのフレームをインターリーブすることもできます。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - x9QxRg](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49B9T4FFZW2YJF9EFMJGRE.png&w=715&h=221&f=webp&fit=cover&position=center)

ストリーム多重化と同時実行は、HTTP/2の強力な機能です。これらは、単一のTCP接続をより効率的に使用することを可能にします。HTTP/2は、特に[優先順位付け](https://blog.cloudflare.com/better-http-2-prioritization-for-a-faster-web/)と組み合わせると、リソースの取得を最適化します。反面、クライアントが大量の並列作業を簡単に開始できるようにすることは、HTTP/1.1と比くらべサーバーリソースに対するピーク需要を増加させる可能性があります。これは明らかに、サービス拒否のベクトルです。

複数の防護策を提供するため、HTTP/2は最大アクティブ[同時ストリーム](https://www.rfc-editor.org/rfc/rfc9113#section-5.1.2)の概念を活用します。[SETTINGS_MAX_CONCURRENT_STREAMS](https://www.rfc-editor.org/rfc/rfc9113#SETTINGS_MAX_FRAME_SIZE)パラメータにより、サーバーは同時処理数の上限をアドバタイズできます。例えば、サーバーが上限を100とした場合、常時アクティブにできるのは100リクエストだけになります。クライアントがこの制限を超えてストリームを開こうとした場合、[RST_STREAM](https://www.rfc-editor.org/rfc/rfc9113#section-6.4)フレームを使用してサーバーに拒否される必要があります。ストリーム拒否は、接続中の他のストリームには影響しません。

本当のところはもう少し複雑になります。ストリームには、[ライフサイクル](https://www.rfc-editor.org/rfc/rfc9113#section-5.1)があります。下図はHTTP/2ストリームのステートマシンの図です。クライアントとサーバーはストリームの状態をそれぞれ管理します。HEADERS、DATA、RST_STREAMフレームが送受信されると遷移が発生します。ストリームの状態のビューは独立していますが、同期しています。

HEADERSとDATAフレームはEND_STREAMフラグを含み、このフラグが値1（true）にセットされると、ステート遷移のトリガーとなります。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - dgpLal](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45G749M08PSFAAXZRQE5DQ.png&w=715&h=515&f=webp&fit=cover&position=center)

メッセージコンテンツを持たないGETリクエストの例で説明します。クライアントはまずストリームを**アイドル** 状態からオープン状態に、続いて即座にハーフ**クローズ** 状態に遷移させます。クライアントの**ハーフクローズ** 状態は、もはやHEADERSやDATAを送信できないことを意味し、[WINDOW_UPDATE](https://www.rfc-editor.org/rfc/rfc9113.html#section-6.9)、[PRIORITY](https://www.rfc-editor.org/rfc/rfc9113.html#section-6.3)、RST_STREAMフレームのみを送信できます。ただし、任意のフレームを受信することができます。

サーバーがHEADERSフレームを受信して解析すると、ストリームの状態をアイドル状態からオープン状態、そしてハーフクローズ状態に遷移させ、クライアントと一致させます。サーバーがハーフクローズ状態であれば、どんなフレームでも送信できますが、WINDOW_UPDATE、PRIORITY、またはRST_STREAMフレームしか受信できないことを意味します。

そのため、サーバーはEND_STREAMフラグを0に設定したHEADERSを送信し、次にEND_STREAMフラグを1に設定したDATAを送信します。DATAフレームは、サーバーで**ハーフクローズ** ドから**クローズ** ドへのストリームの遷移をトリガーします。クライアントがこのフレームを受信すると、ストリームもクローズドに遷移します。ストリームがクローズされると、フレームの送受信はできなくなります。

このライフサイクルを今カレンシーの文脈に当てはめ直し、HTTP/2は次のように[記述](https://www.rfc-editor.org/rfc/rfc9113#section-5.1.2-2)します：

 _「オープン」状態にあるストリーム、または「ハーフクローズド」状態のいずれかにあるストリームは、エンドポイントが開くことを許可されるストリームの最大数にカウントされます。これら3つの状態のいずれかにあるストリームは、[SETTINGS_MAX_CONCURRENT_STREAMS](https://www.rfc-editor.org/rfc/rfc9113#SETTINGS_MAX_CONCURRENT_STREAMS)設定でアドバタイズされる制限にカウントされます。_

理論的には、コンカレンシーの制限は、有用です。しかし、その効果を妨げる現実的な要因があります。詳細は、このブログの後半で開設します。

### HTTP/2リクエストの取り消し

前段で、クライアントからの実行中のリクエストのキャンセルについて説明しました。HTTP/2は、HTTP/1.1よりもはるかに効率的な方法でこれをサポートしています。接続全体を切断するのではなく、クライアントは1つのストリームに対してRST_STREAMフレームを送信することができます。サーバーにリクエストの処理を中止し、レスポンスを中止するよう指示するものです。これによって、Free 、サーバーのリソースを節約し、帯域幅の浪費を避けることができます。

先ほどの3つのリクエストの例を考えてみます。このときクライアントは、すべてのHEADERSが送信された後に、ストリーム1のリクエストをキャンセルします。サーバーは、応答を提供する準備ができる前にこのRST_STREAMフレームを解析し、代わりにストリーム3と5にのみ応答します：

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - alylDM](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48VGZF708M4TQDMQVJN3F2.png&w=715&h=225&f=webp&fit=cover&position=center)

リクエストのキャンセルは、便利な機能です。たとえば、複数の画像を含むウェブページをスクロールするとき、Webブラウザはビューポートの外にある画像をキャンセルすることができ、ビューポートに入る画像をより速く読み込むことができます。HTTP/2は、HTTP/1.1に比べてこの動作をより効率的にしています。

キャンセルされたリクエストストリームは、ストリームのライフサイクルを急速に遷移していきます。END_STREAMフラグが1に設定されたクライアントのHEADERSは、状態を**アイドル** から**オープン** 、**ハーフクローズ** へと遷移させ、RST_STREAMは直ちに**ハーフクローズ** から**クローズ** へと遷移させます。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - FOxdTz](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46SPXM07R6QG2B8FEXJCHJ.png&w=715&h=515&f=webp&fit=cover&position=center)

ストリームの同時実行数制限に寄与するのは、オープン状態またはハーフクローズ状態にあるストリームだけであることを思い出してください。クライアントがストリームをキャンセルすると、そのクライアントは即座に別のストリームをオープンできるようになり、すぐに別のリクエストを送信できるようになります。これが[CVE-2023-44487](https://www.cve.org/CVERecord?id=CVE-2023-44487)を機能させる要諦なのです。

### サービス拒否につながるRapid Reset

HTTP/2リクエストのキャンセルは、制限のない数のストリームを急速にリセットするために悪用される可能性があります。HTTP/2サーバーがクライアントから送信されたRST_STREAMフレームを処理し、十分に迅速に状態を取りやめることができる場合、こうした迅速なリセットは問題を引き起こしません。問題が発生し始めるのは、片付ける際に何らかの遅延やタイムラグがある場合です。クライアントは非常に多くのリクエストを処理するため、作業のバックログが蓄積され、サーバーのリソースを過剰に消費することになります。

一般的なHTTPデプロイメントアーキテクチャは、HTTP/2プロキシやロードバランサーを他のコンポーネントの前で実行することになっています。クライアントのリクエストが到着すると、それはすぐにディスパッチされ、実際の作業は非同期アクティビティとして別の場所で行われます。これにより、プロキシはクライアントのトラフィックを非常に効率的に処理することができます。しかし、このような懸念の層別は、プロキシが処理中のジョブを片付けることを難しくします。そのため、これらのデプロイでは、急速なリセットによる問題が発生しやすくなります。

Cloudflareの[リバースプロキシ](https://www.rfc-editor.org/rfc/rfc9110#section-3.7-6)は、HTTP/2クライアントのトラフィックを処理する際、接続ソケットからデータをバッファにコピーし、バッファリングされたデータを順番に処理していきます。各リクエストが読み込まれると（HEADERSとDATAフレーム）、アップストリームサービスにディスパッチされます。RST_STREAMフレームが読み込まれると、リクエストのローカル状態が破棄され、リクエストがキャンセルされたことがアップストリームに通知されます。バッファ全体が消費されるまで、これが繰り返されます。しかしながら、このロジックは悪用される可能性があります。悪意のあるクライアントが膨大なリクエストの連鎖を送信し始め、接続の開始時にリセットされると、当社のサーバーはそれらすべてを熱心に読み込み、新しい着信リクエストを処理できなくなるほどのストレスをアップストリームサーバーにもたらすでしょう。

強調すべき重要な点は、ストリームの同時実行性だけでは急激なリセットを緩和できないということです。サーバーが[SETTINGS_MAX_CONCURRENT_STREAMS](https://www.rfc-editor.org/rfc/rfc9113#SETTINGS_MAX_CONCURRENT_STREAMS)の値を選んだとしても、クライアントは高いリクエストレートを生成するためにリクエストを繰り返すことができます。

### Rapid Resetの全貌

以下、合計1000リクエストを試みる概念実証クライアントを使用して再現された高速リセットの例を示します。軽減策は一切設けず、市販品のサーバーを用いたテスト環境で、443番ポートを用いています。トラフィックはWiresharkを使って分解され、わかりやすくするためにHTTP/2トラフィックだけを表示するようにフィルタリングされています。進めるには、[pcapをダウンロードしてください](http://staging.blog.mrk.cfdata.org/content/images/rapidreset.pcapng)。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - WbJayy](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46CJJHBWXXWMSQCY94SYWG.png&w=715&h=35&f=webp&fit=cover&position=center)

コマ数が多いので、ちょっと見づらいかもしれません。WiresharkのStatistics> HTTP2ツールで簡単な要約をまとめています：

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - hiRPjv](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44JCSEZW1GJBEZC3CJVBK1.png&w=715&h=219&f=webp&fit=cover&position=center)

このトレースの最初のフレームであるパケット14はサーバーのSETTINGSフレームであり、最大ストリーム同時実行数100をアドバタイズしています。パケット15では、クライアントはいくつかの制御フレームを送信し、その後、急速にリセットするリクエストを開始します。最初のHEADERSフレームは26バイト長ですが、それ以降のHEADERSはすべて9バイトです。このサイズの違いは、[HPACK](https://blog.cloudflare.com/hpack-the-silent-killer-feature-of-http-2/)と呼ばれる圧縮技術によるものです。パケット15は合計で525のリクエストを含み、ストリーム1051まで増やされます。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - 4zuXCV](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW497JBM72881G9RYDWRT2C6.png&w=619&h=593&f=webp&fit=cover&position=center)

興味深いことに、ストリーム1051のRST_STREAMはパケット15に適合しないため、パケット16ではサーバーが404応答しているのがわかります。その後、残りの475リクエストの送信に移る前に、パケット17でクライアントがRST_STREAMを送信しています。

サーバーは100の同時ストリームをアドバタイズしていますが、クライアントが送信したパケットはいずれも、それよりも多くのHEADERSフレームを送信しています。クライアントはサーバーからの折り返しのトラフィックを待つ必要がなく、送信できるパケットのサイズによってのみ制限されています。このトレースにはサーバーのRST_STREAMフレームは見られず、サーバーは同時ストリーム違反を観測していないことを示しています。

## 顧客への影響

上述したように、リクエストがキャンセルされると、アップストリームサービスは通知を受け、多くのリソースを浪費する前にリクエストを中止することができます。今回の攻撃では、ほとんどの悪意あるリクエストが配信元サーバーに転送されることはありませんでした。しかし、これらの攻撃の規模が大きいため、何らかの影響が引き起こされます。

まず、リクエストの着信率がこれまでにないピークに達したため、クライアントが目にする502エラーのレベルが上昇したという報告がありました。これは、最も影響を受けたデータセンターで発生しており、すべてのリクエストを処理するのに難儀しました。当社のネットワークは大規模な攻撃にも対応できるようになっているものの、今回の脆弱性は当社のインフラストラクチャの弱点を露呈するものでした。データセンターのひとつに届いたリクエストがどのように処理されるかを中心に、詳細をもう少し掘り下げてみましょう：

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - ZsURSu](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45571VPJA9ST5WBRH9KPG8.png&w=715&h=269&f=webp&fit=cover&position=center)

Cloudflareのインフラストラクチャは、役割の異なるプロキシサーバのチェーンで構成されていることがわかります。特に、クライアントがHTTPSトラフィックを送信するためにCloudflareに接続すると、まずTLS復号化プロキシに当たります。このプロキシはTLSトラフィックを復号化し、HTTP 1、2、または3トラフィックを処理した後、「ビジネスロジック」プロキシに転送します。このプロキシは、各顧客のすべての設定をロードし、リクエストを他のアップストリームサービスに正しくルーティングする役割を担っており、**さらに当社の場合ではセキュリティ機能も担っています** 。このプロキシで、L7攻撃緩和の処理が行われます。

この攻撃ベクトルでの問題点は、すべての接続で非常に多くのリクエストを素早く送信することになります。当社がブロックするチャンスを得る前に、そのひとつひとつがビジネスロジックプロキシに転送されなければならなりませんでした。リクエストのスループットがプロキシのキャパシティを上回るようになると、この2つのサービスをつなぐパイプは、いくつかのサーバーで飽和レベルに達しました。

これが起こると、TLSプロキシはアップストリームプロキシに接続できなくなり、最も深刻な攻撃時に「502 Bad Gateway」エラーが表示されるクライアントがあるのは、これが理由です。重要なのは、現在ではHTTP分析の作成に使用されるログは、ビジネスロジックプロキシからも出力されることになります。その結果、これらのエラーはCloudflareのダッシュボードには表示されません。当社内部のダッシュボードによると、（緩和策を実施する前の）最初の攻撃波では、リクエストの約1％が影響を受け、8月29日の最も深刻な攻撃では数秒間で約12％のピークが見られました。次のグラフは、この現象が起きていた2時間にわたるエラーの割合を示したものです：

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - cDLXgV](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49H86FX527NRYXEFG5HNZH.png&w=715&h=442&f=webp&fit=cover&position=center)

当社では、この記事の後半で詳述するとおり、その後の数日間でこの数を劇的に減らすことに努めました。当社によるスタックの変更と軽減策により、こうした攻撃の規模が大幅に縮小されたおかげで、この数は今日では事実上ゼロになっています：

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - AfViXl](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW484F1GN0TB062910TF1AD8.png&w=715&h=442&f=webp&fit=cover&position=center)

### 499エラーとHTTP/2ストリーム同時実行の課題

一部の顧客から報告されたもう一つの症状に、499エラーの増加がありました。この理由は少し違っており、この投稿で前述したHTTP/2接続の最大ストリームの同時実行数に関連しています。

HTTP/2の設定は、SETTINGSフレームを使用して接続の開始時に交換されます。明示的なパラメータを受け取らない場合、デフォルト値が適用されます。クライアントがHTTP/2接続を確立すると、サーバーの設定を待つ（遅い）か、デフォルト値を想定してリクエストを開始（速い）することになります。SETTINGS_MAX_CONCURRENT_STREAMSでは、デフォルトでは事実上無制限となります（ストリームIDは31ビットの数値空間を使用し、リクエストは奇数を使用するため、実際の制限は1073741824となります）。仕様では、サーバーが提供するストリーム数は100を下回らないようにすることを推奨しています。クライアントは一般的にスピードを重視するため、サーバーの設定を待つ傾向がなく、ちょっとした競合状態が発生します。つまり、クライアントは、サーバーがどのリミットを選択するかという賭けに出ているのです。もし間違ったリミットを選択すれば、リクエストは拒否され、再試行しなければならなくなります。1073741824ストリームに賭けるギャンブルは、賢明ではありません。その代わり、多くのクライアントは、サーバーが仕様の推奨に従うことを期待し、同時ストリーム発行数を100に制限することにしています。サーバーが100以下のものを選んだ場合、このクライアントのギャンブルは失敗し、ストリームはリセットされます。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - VLKjcD](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46456QGGZGE6J54D0S0W49.png&w=715&h=246&f=webp&fit=cover&position=center)

サーバーによるストリームのリセットには、同時実行数の上限を超えた場合など、たくさんの理由があります。HTTP/2は厳格であり、構文解析やロジックエラーが発生した場合はストリームを閉じる必要があります。2019年、Cloudflareは[HTTP/2のDoS脆弱性](https://blog.cloudflare.com/on-the-recent-http-2-dos-attacks/)に対応して複数の緩和策を開発しました。これらの脆弱性のいくつかは、クライアントが誤動作を起こし、サーバーがストリームをリセットすることによって引き起こされていました。そのようなクライアントを取り締まるための非常に効果的な戦略は、接続中のサーバーリセットの回数をカウントし、それがある閾値を超えたら[GOAWAY](https://www.rfc-editor.org/rfc/rfc9113#section-6.8)フレームで接続を閉じることになります。正当なクライアントは、接続中に1つか2つのミスをするかもしれないものの、それは許容範囲内となります。あまりにも多くのミスをするクライアントは、おそらく壊れているか悪意のあるクライアントであり、接続を閉じることで両方のケースに対処できます。

[CVE-2023-44487](https://www.cve.org/CVERecord?id=CVE-2023-44487)によるDoS攻撃に対応している間、Cloudflareはストリームの最大同時実行数を64に減らしました。この変更を行う前、当社はクライアントがSETTINGSを待たず、代わりに100の同時実行を想定していることを知りませんでした。画像ギャラリーのような一部のWebページでは、接続開始時にブラウザがすぐに100リクエストを送信することがあります。残念ながら、制限を超えた36のストリームはすべてリセットする必要があり、これがカウント緩和のトリガーとなりました。つまり、正当なクライアントの接続を閉じてしまい、ページのロードが完全に失敗してしまったのです。この相互運用性の問題に気づいてすぐに、ストリームの最大同時接続数を100に変更しました。

## Cloudflare側での対応

2019年、HTTP/2の実装に関連する複数の[DoS脆弱性](https://blog.cloudflare.com/on-the-recent-http-2-dos-attacks/)が発覚しました。Cloudflareはこれを受けて一連の検出と緩和策を開発し、デプロイしました。[CVE-2023-44487](https://www.cve.org/CVERecord?id=CVE-2023-44487)は、HTTP/2の脆弱性の異なる症状です。しかし、この脆弱性を緩和するために、クライアントから送信されるRST_STREAMフレームを監視し、不正に使用されている場合は接続を閉じるよう、既存の保護を拡張することができました。RST_STREAMの正当なクライアント利用への影響はありませんでした。

直接的な修正に加え、サーバーのHTTP/2フレーム処理とリクエストディスパッチコードにいくつかの改善を実装しました。さらに、ビジネスロジックサーバーではキューイングとスケジューリングを改善し、不要な作業が減り、キャンセルの応答性が向上しました。これらを組み合わせることで、様々な悪用パターンの可能性の影響を軽減し、サーバーに飽和する前にリクエストを処理するための余裕を与えることができました。

### 攻撃の早期軽減

Cloudflareはすでに、より安価な方法で非常に大規模な攻撃を効率的に軽減するシステムを導入していました。その一つが、「IP Jail」というものです。ハイパー帯域幅消費型攻撃の場合、このシステムは攻撃に参加しているクライアントIPを収集し、攻撃されたプロパティへの接続をIPレベルまたは当社のTLSプロキシで阻止します。この貴重な数秒の間にオリジンはすでに保護されているものの、当社のインフラストラクチャはまだすべてのHTTPリクエストを吸収する必要があります。この新しいボットネットには事実上立ち上がり期間がないため、問題になる前に攻撃を無力化する必要があります。

これを実現するため、当社はIP Jailシステムを拡張してインフラストラクチャ全体を保護しました。IPが「ジェイル」（投獄）されると、攻撃されたプロパティへの接続がブロックされるだけでなく、対応するIPがCloudflare上の他のドメインに対してHTTP/2を使用することも、しばらくの間禁止されます。このようなプロトコルは、HTTP/1.xでの悪用は不可能です。このため、攻撃者による大規模な攻撃の実行は制限されるものの、同じIPを共有する正当なクライアントであればその間のパフォーマンスの低下はごくわずかなものとなります。IPベースの攻撃軽減策は、非常に鈍感なツールです。このため、このような規模で使用する場合、細心の注意を払い、誤検知をできるだけ避けるようにしなければなりません。さらに、ボットネット内の特定のIPの寿命は通常短いため、長期的な緩和策は良いことよりも悪いことの方が多い可能性が高くなります。以下のグラフは、我々が目撃した攻撃におけるIPの入れ替わりを示したものです：

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - zEcUBs](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46BMWNAXCMETHFB5FB79WB.png&w=715&h=348&f=webp&fit=cover&position=center)

このように、ある日に発見された多くの新規IPは、その後すぐに消えてしまいます。

これらの動作は、すべてHTTPSパイプラインの最初にあるTLSプロキシで行われるため、通常のL7攻撃低減システムと比較してかなりのリソースを節約できます。これにより、これらの攻撃をはるかにスムーズに切り抜けることができるようになり、現在ではこれらのボットネットによって引き起こされるランダムな502エラーの数は、ゼロになりました。

### 可観測性の向上

当社が変革しようとしているもうひとつの地平に、観測可能性があります。顧客分析で捉えられることなく、クライアントにエラーを返してしまうのは、不満につながります。幸いなことに、今回の攻撃のはるか以前から、これらのシステムをオーバーホールするプロジェクトが進行中でした。最終的には、ビジネスロジックプロキシがログ・データを統合して出力する代わりに、インフラ内の各サービスが独自にデータをログできるようになります。今回の事件は、この取り組みの重要性を浮き彫りにしました。

また、接続レベルのロギングの改善にも取り組んでおり、このようなプロトコルの乱用をより迅速に発見し、DDoS軽減能力を向上させることができます。

## まとめ

今回の攻撃は記録的な規模であったものの、これが最後ではないことは明白です。攻撃がますます巧妙化する中、Cloudflareでは新たな脅威を能動的に特定し、当社のグローバル・ネットワークに対策をデプロイすることで、数百万人の顧客が即座に自動的に保護されるようたゆまぬ努力を続けています。

Cloudflareは、2017年以来すべてのお客様に無料、従量制、無制限のDDoS攻撃対策を提供してきました。さらに、あらゆる規模の組織のニーズに合わせて、さまざまな追加のセキュリティ機能を提供しています。保護されているかどうかわからない場合、または保護方法をお知りになりたい場合、[当社にお問い合わせ](https://www.cloudflare.com/ja-jp/h2/)ください。

このページ

オンラインで議論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Ftechnical-breakdown-http2-rapid-reset-ddos-attack%2F&t=HTTP%2F2%20Rapid%20Reset%EF%BC%9A%E8%A8%98%E9%8C%B2%E7%9A%84%E5%8B%A2%E3%81%84%E3%81%AE%E6%94%BB%E6%92%83%E3%82%92%E7%84%A1%E5%8A%B9%E5%8C%96)[](https://x.com/intent/post?text=HTTP%2F2+Rapid+Reset%EF%BC%9A%E8%A8%98%E9%8C%B2%E7%9A%84%E5%8B%A2%E3%81%84%E3%81%AE%E6%94%BB%E6%92%83%E3%82%92%E7%84%A1%E5%8A%B9%E5%8C%96&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Ftechnical-breakdown-http2-rapid-reset-ddos-attack%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Ftechnical-breakdown-http2-rapid-reset-ddos-attack%2F)[](https://bsky.app/intent/compose?text=HTTP%2F2+Rapid+Reset%EF%BC%9A%E8%A8%98%E9%8C%B2%E7%9A%84%E5%8B%A2%E3%81%84%E3%81%AE%E6%94%BB%E6%92%83%E3%82%92%E7%84%A1%E5%8A%B9%E5%8C%96+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Ftechnical-breakdown-http2-rapid-reset-ddos-attack%2F)[](https://mastodonshare.com/?text=HTTP%2F2+Rapid+Reset%EF%BC%9A%E8%A8%98%E9%8C%B2%E7%9A%84%E5%8B%A2%E3%81%84%E3%81%AE%E6%94%BB%E6%92%83%E3%82%92%E7%84%A1%E5%8A%B9%E5%8C%96&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Ftechnical-breakdown-http2-rapid-reset-ddos-attack%2F)[](https://www.threads.net/intent/post?text=HTTP%2F2+Rapid+Reset%EF%BC%9A%E8%A8%98%E9%8C%B2%E7%9A%84%E5%8B%A2%E3%81%84%E3%81%AE%E6%94%BB%E6%92%83%E3%82%92%E7%84%A1%E5%8A%B9%E5%8C%96+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Ftechnical-breakdown-http2-rapid-reset-ddos-attack%2F)

## 関連するタグ

[DDoS](https://blog.cloudflare.com/ja-jp/tag/ddos/)[Vulnerabilities](https://blog.cloudflare.com/ja-jp/tag/vulnerabilities/)[セキュリティ](https://blog.cloudflare.com/ja-jp/tag/security/)[傾向](https://blog.cloudflare.com/ja-jp/tag/trends/)[攻撃](https://blog.cloudflare.com/ja-jp/tag/attacks/)

SNS をフォロー

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 新しい投稿のお知らせを受け取るように登録する

メールアドレス

また、あなたのメールアドレスを共有したりすることはございません。

登録する

ご購読ありがとうございます！受信箱を確認して登録してください。
