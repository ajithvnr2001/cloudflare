---
url: https://blog.cloudflare.com/ja-jp/investigating-multi-vector-attacks-in-log-explorer/
title: Log Explorer\u3067\u30de\u30eb\u30c1\u30d9\u30af\u30c8\u30eb\u578b\u653b\u6483\u3092\u8abf\u67fb\u3059\u308b | Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:51:36.115104+00:00
---

# Log Explorerでマルチベクトル型攻撃を調査する | Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/investigating-multi-vector-attacks-in-log-explorer/

[ブログ](https://blog.cloudflare.com/ja-jp/)

[R2](https://blog.cloudflare.com/ja-jp/tag/r2/)[SIEM](https://blog.cloudflare.com/ja-jp/tag/siem/)[コネクティビティクラウド](https://blog.cloudflare.com/ja-jp/tag/connectivity-cloud/)5件5件タグを表示

8 タグタグを8件表示

  * 投稿タグ
  * [R2](https://blog.cloudflare.com/ja-jp/tag/r2/)[SIEM](https://blog.cloudflare.com/ja-jp/tag/siem/)[コネクティビティクラウド](https://blog.cloudflare.com/ja-jp/tag/connectivity-cloud/)[ストレージ](https://blog.cloudflare.com/ja-jp/tag/storage/)[セキュリティ](https://blog.cloudflare.com/ja-jp/tag/security/)[ログ](https://blog.cloudflare.com/ja-jp/tag/logs/)[分析](https://blog.cloudflare.com/ja-jp/tag/analytics/)[製品ニュース](https://blog.cloudflare.com/ja-jp/tag/product-news/)
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



[ストレージ](https://blog.cloudflare.com/ja-jp/tag/storage/)[セキュリティ](https://blog.cloudflare.com/ja-jp/tag/security/)[ログ](https://blog.cloudflare.com/ja-jp/tag/logs/)[分析](https://blog.cloudflare.com/ja-jp/tag/analytics/)[製品ニュース](https://blog.cloudflare.com/ja-jp/tag/product-news/)

[R2](https://blog.cloudflare.com/ja-jp/tag/r2/)[SIEM](https://blog.cloudflare.com/ja-jp/tag/siem/)[コネクティビティクラウド](https://blog.cloudflare.com/ja-jp/tag/connectivity-cloud/)[ストレージ](https://blog.cloudflare.com/ja-jp/tag/storage/)[セキュリティ](https://blog.cloudflare.com/ja-jp/tag/security/)[ログ](https://blog.cloudflare.com/ja-jp/tag/logs/)[分析](https://blog.cloudflare.com/ja-jp/tag/analytics/)[製品ニュース](https://blog.cloudflare.com/ja-jp/tag/product-news/)

2026年3月10日

# Log Explorerでマルチベクトル型攻撃を調査する

![Jen Sells](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49JMAH0P8SVDYZSBSAS4EK.JPG&w=64&h=64&f=webp&fit=cover&position=center)![Claudio Jolowicz](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW456R2CFXKBCA2T8XEE5FMB.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Nico Gutierrez](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48HB96WV2J3TRWVDQY4X8E.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Jen Sells](https://blog.cloudflare.com/ja-jp/author/jen-sells/)、[Claudio Jolowicz](https://blog.cloudflare.com/ja-jp/author/claudio/)、[Nico Gutierrez](https://blog.cloudflare.com/ja-jp/author/nico-gutierrez/)

11分で読了

URLをコピー

この記事は以下でも利用可能です [English](https://blog.cloudflare.com/investigating-multi-vector-attacks-in-log-explorer/)、[한국어](https://blog.cloudflare.com/ko-kr/investigating-multi-vector-attacks-in-log-explorer/).

![BLOG-3164 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44T2Y7DY06GACRR2JF6RQM.png&w=1999&h=1126&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA//////798PHz5uru5+3x7/P28vPy7+3p/////vv96+zz3OLt3uXx5+z27u/z7erp/////vr/5+j01Nvu1d7z4ej36+z07enq//////3/6en41dzy1d/24+n77e/48O3u////////8fL+4Ob44en97fP/9vf+9/T1/////////v//8PX/8vj/+/////////37/////////////v//////////////////////////////////////////////////)

_このコンテンツは自動機械翻訳サービスによる翻訳版であり、皆さまの便宜のために提供しています。原本の英語版と異なる誤り、省略、解釈の微妙な違いが含まれる場合があります。ご不明な点がある場合は、英語版原本をご確認ください。_

サイバーセキュリティの世界では、単一のデータポイントがすべてになることはほとんどありません。最新の攻撃者は、玄関を玄関を開けるだけではありません。 APIを探り、ネットワークを「ノイズ」であふれさせてチームの注意をそらし、盗んだ資格情報を使ってアプリケーションやサーバーをすり抜けようとします。

こうしたマルチベクトル型攻撃を阻止するには、全体像が必要です。Cloudflare Log Explorerを使用してセキュリティフォレンジックを行うと、14の新しいデータセットを統合し、CloudflareのアプリケーションサービスとCloudflare One製品ポートフォリオの全体をカバーする360度の可視性が得られます。セキュリティアナリストは、アプリケーション層のHTTPリクエスト、ネットワーク層のDDoSおよびファイアウォールログ、Zero Trustアクセスイベントのテレメトリを相関させることで、平均検出時間（MTTD）を大幅に短縮し、高度な多層攻撃を効果的に明らかにすることができます。

以下では、Log Explorerがセキュリティチームに、迅速で詳細なフォレンジックのための究極の環境を提供する方法について詳しく解説します。

## スタック全体を守るフライトクロック

現代のデジタル環境では、複数の攻撃ベクトルを使用する敵から防御するために、深く関連付けられたテレメトリが必要です。未加工ログは、アプリケーションの「フライト従量課金」のような役割を果たし、すべてのインタラクション、攻撃の試み、パフォーマンスのボトルネックを捕捉します。また、Cloudflareはユーザーとサーバーの間のエッジに位置しているため、こうしたイベントはすべて、リクエストがインフラストラクチャに到達する前に記録されます。

Cloudflare Log Explorerは、これらのログを統一されたインターフェースに集約し、迅速に調査できるようにします。

### サポートされているログタイプ

#### ゾーンスコープ付きログ

 _焦点：Webサイトトラフィック、セキュリティイベント、エッジパフォーマンス_

HTTPリスクエスト数| 最も包括的なデータセットとして、すべてのアプリケーション層トラフィックの「プライマリレコード」として機能し、セッションアクティビティ、悪用の試行、ボットパターンの再構築を可能にします。  
---|---  
ファイアウォールイベント| ブロックされた、またはチャレンジが必要な脅威の重要な証拠を提供するため、アナリストは攻撃を傍受した特定のWAFルール、IPレピュテーション、またはカスタムフィルターを特定することができます。  
DNSログ| 権威エッジで解決されたすべてのクエリを追跡することで、キャッシュポイズニングの試み、ドメインハイジャック、インフラストラクチャレベルの偵察を特定します。  
NEL（ネットワークエラーログ）レポート| クライアント側のブラウザエラーを追跡することで、協調的なアプリケーション層 DDoS攻撃と正当なネットワーク接続の問題を区別します。  
Spectrumイベント| 非Webアプリケーションの場合、これらのログはL4トラフィック（TCP/UDP）を可視化し、SSH、RDP、またはカスタムゲーミングトラフィックなどのプロトコルに対する異常や総当たりパスワード攻撃を特定するのに役立ちます。  
Page Shield| JavaScript、アウトバウンド接続など、サイトのクライアントサイド環境への不正変更を追跡し、監査します。  
Zaraz イベント| サードパーティのツールや追跡者がユーザーデータとどのようにやり取りしているかを調査します。これは、プライバシーコンプライアンスの監査や無許可のスクリプトの動作の検出に不可欠です。  
  
#### アカウントスコープ指定ログ

 _焦点：内部セキュリティ、Zero Trust、管理変更、ネットワークアクティビティ_

アクセスリクエスト| IDベースの認証イベントを追跡して、どのユーザーが特定の内部アプリケーションにアクセスしたか、そしてそれらの試みが承認されるかどうかを判断します。  
---|---  
監査ログ| Cloudflareダッシュボード内の設定変更の証跡を提供し、無許可の管理アクションや変更を特定します。  
CASBの発見事項| SaaSアプリケーション（Google DriveやMicrosoft 365など）内のセキュリティ設定ミスやデータリスクを特定し、不正なデータ漏洩を防止します。  
Magic Transit / IPSecログ| ネットワークエンジニアが、トンネルの健全性の確認やBGPルーティング変更の表示など、ネットワークレベル（L3）の監視を行うのに役立ちます。  
ブラウザ分離ログ| 信頼できないサイトでのデータ漏洩を防ぐため、分離されたブラウザセッションの内部でユーザーアクション（コピー＆ペースト、印刷、ファイルのアップロードなど）を追跡する  
デバイスポスチャー結果| ネットワークに接続したデバイスのセキュリティの健全性とコンプライアンスステータスを詳細に確認し、侵害されたエンドポイントや非準拠のエンドポイントを特定するのに役立ちます。  
DEXアプリケーションテスト| ユーザーの視点からアプリケーションパフォーマンスを監視することで、セキュリティ関連の障害と通常的なパフォーマンス低下を区別することができます。  
DEXデバイス状態イベント| ユーザーデバイスの物理的な状態に関するテレメトリを提供し、ハードウェアまたはOSレベルの異常と潜在的なセキュリティインシデントを関連付けるのに役立ちます。  
DNSファイアウォールログ| DNSファイアウォールを介してフィルタリングされたDNSクエリを追跡し、既知の悪意のあるドメインまたはコマンド＆コントロール（C2）サーバーとの通信を特定します。  
Email Securityアラート| ゲートウェイで検出された悪意あるメール活動やフィッシング試行をログに記録し、メールベースの侵入ベクトルの送信元を追跡します。  
Gateway DNS| ネットワーク上のユーザーが行ったすべてのDNSクエリを監視し、シャドーIT、マルウェアコールバック、ドメイン生成アルゴリズム（DGA）を特定します。  
ゲートウェイHTTP| 暗号化されたWebトラフィックと暗号化されていないWebトラフィックを完全に可視化し、隠れた悪意のあるペイロードや悪意のあるファイルのダウンロード、SaaSの不正使用を検出します。  
ゲートウェイネットワーク| L3/L4ネットワークトラフィック（非HTTP）を追跡し、不正なポートの使用、プロトコルの異常、ネットワーク内のラテラルムーブメントを特定します。  
IPSecログ| 暗号化されたサイト間トンネルのステータスとトラフィックを監視し、安全なネットワーク接続の完全性と可用性を確保します。  
Magic IDS検出| 侵入検知シグネチャとの一致を表面化し、調査者に既知のエクスプロイトパターンやネットワークを通過するマルウェアの動作を警告します。  
ネットワーク分析ログ| パケットレベルのデータをハイレベルで可視化し、帯域幅消費型DDoS攻撃や特定のインフラストラクチャを標的とした異常なトラフィックスパイクを特定します。  
シンクホールHTTPログ| 「シンクホール化」されたIPアドレスに向けられたトラフィックをキャプチャし、どの内部デバイスが既知のボットネットインフラストラクチャと通信しようとしているかを確認します。  
WARP設定変更| エンドユーザーデバイスのWARPクライアント設定の変更を追跡し、セキュリティエージェントが改ざんされたり、無効化されていないことを確認します。  
WARPのトグル変更| 具体的には、ユーザーが安全な接続を有効または無効にしたときのログを記録し、デバイスが保護されていない期間を特定するのに役立ちます。  
Zero Trustネットワークセッションログ| 認証されたユーザーセッションの期間とステータスを記録し、保護された境界内でのユーザーアクセスの全ライフサイクルをマッピングします。  
  
## Log Explorerは、各段階で悪意のあるアクティビティを特定できます

**HTTPリクエスト** 、**ファイアウォールイベント** 、**DNSログ** でアプリケーション層を詳細に可視化し、トラフィックがどのように公開プロパティに到達しているかを正確に把握します。**アクセス要求** 、**Gatewayログ** 、および**監査ログ** で内部的な移動を追跡します。認証情報が侵害された場合、その行き先を確認できます。**Magic IDS** と**ネットワーク分析のログ** を使用して、帯域幅消費型攻撃やプライベートネットワーク内の「East-West」ラテラルムーブメントを特定します。

### 偵察を識別

攻撃者は、スキャナーやその他のツールを使用して、侵入口、隠れたディレクトリ、またはソフトウェアの脆弱性を探します。これを特定するには、Log Explorer を使用して、単一の IP からの 401、403、または 404 の` EdgeResponseStatus コード、または機密パス (例: http_requests) のリクエストをクエリできます。/.env`, `/.git`, `/wp-admin`)。

さらに、`magic_ids_detections` ログも、ネットワーク層でのスキャンを特定するために使用することができます。これらのログは、ネットワークを標的とする脅威をパケットレベルで可視化します。標準的なHTTPログとは異なり、これらのログは、ネットワーク層およびトランスポート層（IP、TCP、UDP）における**シグネチャベースの検出** に重点を置いています。単一の`SourceIP`が短時間の時間枠で幅広い`DestinationPort`値にわたる複数のユニーク検出をトリガーするケースを検出するクエリー。Magic IDS署名は、特にNmapスキャンやSYNステルススキャンなどのアクティビティにフラグを立てることができます。

### 迂回の確認

攻撃者は偵察を行っている間も、同時にネットワークフラッドを仕掛けてこれを偽装しようとするかもしれません。`network_analytics_logs` にピボットして、ボリューメトリック攻撃が煙幕として使用されているかどうかを確認します。

### アプローチを識別する

攻撃者が潜在的な脆弱性を特定すると、武器を作り始めます。攻撃者は、悪意のあるペイロード（SQLインジェクションや大きなファイル、破損したファイルのアップロードなど）を使用して脆弱性を確認するよう求められます。`http_requests`や`fw_events`を確認して、トリガーされたCloudflare検出ツールを特定します。Cloudflareは、これらのデータセットのセキュリティシグナルをログに記録し、`WAFAttackScore`、`WAFSQLiAttackScore`、`FraudAttack`、`ContentScanJobResults`などのフィールドを使って、悪意のあるペイロードを持つリクエストを容易に識別します。これらのフィールドを十分に理解するには、[ _当社のドキュメント_](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/http_requests/)をご覧ください。`fw_events`ログは、`action`、`source`、および`ruleID`フィールドを調べることで、これらのリクエストがCloudflareの防御を通過したかどうかを判断するために使用できます。Cloudflareのマネージドルールは、デフォルトでこれらの悪意のあるペイロードの多くをブロックします。アプリケーションセキュリティの概要を確認して、アプリケーションが保護されているかどうかを確認します。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Showing the Managed rules Insight that displays on Security Overview if the current zone does not have Managed Rules enabled](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44Z4WGGKCCC271C8VZ259Q.png&w=715&h=79&f=webp&fit=cover&position=center)

 _現在のゾーンでマネージドルールが有効になっていない場合、セキュリティの概要に表示されるマネージドルールインサイトを表示する_

### IDを監査する

その不審なIPはログインに成功したのでしょうか？`ClientIP`を使用して`access_requests`を検索します。機密性の高い内部アプリに対して"`決定：許可`"と表示されれば、アカウントが侵害されていることがわかります。

### 漏洩（データ流出）を阻止する

攻撃者は、DNSトンネリングを使用して、機密データ（パスワードやSSHキーなど）をDNSクエリにエンコードすることにより、ファイアウォールを回避することがあります。`google.com`のような通常のリクエストではなく、ログにはエンコードされた長い文字列が表示されます。フィールドを調べて、独自で長い、高エントロピーのサブドメインに対する異常に多いクエリを探しましょう: `QueryName`: [`_h3ldo293js92.example.com_`](http://h3ldo293js92.example.com) のような文字列を探します。`QueryType`: 悪意のあるペイロードの転送に`TXT`、`CNAME`、または`NULL`レコードを使用することが多く、`ClientIP`: 単一の内部ホストが数千の固有リクエストを生成しているかどうかを識別します。

さらに、攻撃者は、非標準のプロトコル内に機密データを隠したり、一般的なプロトコル（DNSやICMPなど）を使用して標準的なファイアウォールをバイパスすることで、機密データを漏えいさせようとすることがあります。`magic_ids_detections`ログをクエリして、`SignatureMessage`の「ICMPトンネリング」や「DNSトンネリング」など、プロトコルの異常にフラグを立てるシグネチャを探して、これを見つけてください。

ゼロデイ脆弱性を調査する場合でも、高度なボットネットを追跡する場合でも、必要なデータがすぐ利用できるようになっています。

## データセット間の相関分析

複数の同時検索を切り替えて、複数のデータセットにわたる悪意のあるアクティビティを調査します。Log Explorerでは、新しいタブ機能で複数のクエリーを同時に操作できるようになりました。タブを切り替えてデータセットをクエリしたり、クエリ結果を介してフィルタリングしてクエリを調整したりすることもできます。

複数のCloudflareログソースのデータを相関させると、分離して表示すると良性に見える高度な複数段階の攻撃を検出することができます。このデータセット横断的な分析により、偵察から流出まで、攻撃の連鎖の全体像を把握できます。

### セッションハイジャック（トークンの盗難）

**シナリオ:** ユーザーがCloudflare Accessを介して認証しますが、後続のHTTP_requestトラフィックはボットのように見えます。

**ステップ1：** `http_requests`内の高リスクセッションを特定します。
    
    
    SELECT RayID, ClientIP, ClientRequestUserAgent, BotScore
    FROM http_requests
    WHERE date = '2026-02-22' 
      AND BotScore < 20 
    LIMIT 100

**ステップ2：** `RayID`をコピーし、`access_requests`を検索して、その不審なボットアクティビティに関連付けられているユーザーアカウントを確認します。
    
    
    SELECT Email, IPAddress, Allowed
    FROM access_requests
    WHERE date = '2026-02-22' 
      AND RayID = 'INSERT_RAY_ID_HERE'

### フィッシング後C2ビーコン

**シナリオ：** 従業員がフィッシングメールのリンクをクリックした結果、ワークステーションが侵害されました。このワークステーションは、既知の悪意のあるドメインに対してDNSクエリーを送信し、その後すぐにIDSアラートをトリガーします。

**ステップ1：** email_security_alertsの違反を調べて、フィッシング攻撃を見つけます。
    
    
    SELECT Timestamp, Threatcategories, To, Alertreason
    FROM email_security_alerts
    WHERE date = '2026-02-22' 
      AND Threatcategories LIKE 'phishing'

**ステップ2：** アクセスログを使用して、ユーザーのメール（To）をIPアドレスと関連付けます。
    
    
    SELECT Email, IPAddress
    FROM access_requests
    WHERE date = '2026-02-22' 

**ステップ3：** `gateway_dns`ログで、特定の悪意のあるドメインにクエリを実行している内部IPを見つけます。
    
    
    SELECT SrcIP, QueryName, DstIP, 
    FROM gateway_dns
    WHERE date = '2026-02-22' 
      AND SrcIP = 'INSERT_IP_FROM_PREVIOUS_QUERY'
      AND QueryName LIKE '%malicious_domain_name%'

### ラテラルムーブメント（Access → ネットワークプロービング）

**シナリオ：** ユーザーはZero Trust経由でログインし、内部ネットワークをスキャンしようとします。

**ステップ1:** ``access_requestsの予期しない場所からのログインが成功した場所をaccess_requestsで検索します。
    
    
    SELECT IPAddress, Email, Country
    FROM access_requests
    WHERE date = '2026-02-22' 
      AND Allowed = true 
      AND Country != 'US' -- Replace with your HQ country

**ステップ2：** その`IPアドレス`が`magic_ids_detections`でネットワークレベルの署名をトリガーしているかどうかを確認します。
    
    
    SELECT SignatureMessage, DestinationIP, Protocol
    FROM magic_ids_detections
    WHERE date = '2026-02-22' 
      AND SourceIP = 'INSERT_IP_ADDRESS_HERE'

### より多くのデータへの扉を開く

Log Explorerは、最初から拡張性を念頭に設計されています。すべてのデータセットスキーマは、JSONデータの構造とタイプを記述するための広く採用されている標準であるJSONスキーマを使用して定義されます。この設計上の決定により、HTTPリクエストとファイアウォールイベントを超えて、Cloudflareの幅広いテレメトリに容易に拡張できるようになりました。初期のデータセットを支えていたのと同じスキーマ駆動型のアプローチは、Zero Trustログ、ネットワーク分析、メールセキュリティアラート、そしてその間のあらゆる機能に対応するために、自然に拡張することができました。

さらに重要なのは、この標準化により、Cloudflareのネイティブのテレメトリを超えたデータ取り込みが可能になることです。当社の取り込みパイプラインはハードコードされていないスキーマ駆動型であるため、JSON形式で表現できるどのような構造化データでも受け付けることができます。これは、ハイブリッド環境を管理するセキュリティチームにとって、Log Explorerは最終的には単一の管理画面として機能し、Cloudflareのエッジテレメトリとサードパーティソースからのログを相関させ、すべて同じSQLインターフェースを介してクエリーを可能にすることを意味します。本日のリリースは、Cloudflareの製品ポートフォリオを網羅することに焦点を当てていますが、アーキテクチャ上の基盤は、お客様がカスタムスキーマで独自のデータソースを持ち込める将来に向けたものです。

### より迅速なデータ、より迅速なレスポンス：アーキテクチャのアップグレード

マルチベクトル型攻撃を効果的に調査するには、タイミングがすべてです。ログの可用性が数分遅れるだけでも、事前予防的な防御と事後対応型の被害制御の違いにつながる可能性があります。

そこで、取り込みを最適化して、速度と耐障害性を向上させました。取り込みパスの一部でコンカレンシーを高めることで、「うるさい隣人」問題を引き起こす可能性のあるボトルネックを排除し、あるクライアントのデータ急増が別のクライアントの可視性を低下させないようにしました。このアーキテクチャ作業により、P99の取り込み遅延が約55%、P50は25%短縮され、エッジのイベントがSQLクエリに利用できるようになるまでの時間を短縮することができました。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Grafana chart displaying the drop in ingest latency after architectural upgrades](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46E6JRTK5WZV8TQXJ49P3R.png&w=715&h=315&f=webp&fit=cover&position=center)

 _アーキテクチャのアップグレード後の取り込み遅延の減少を示すGrafanaグラフ_

## 最新情報をフォローしましょう

これは始まりにすぎません。当社は、カスタム定義スケジュールでこれらの検出クエリを実行する機能など、Log Explorerエクスペリエンスをさらに向上させるために、さらに強力な機能の開発に積極的に取り組んでいます。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Scheduled Queries List](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW456P12SSMET3N8VJFCQH67.png&w=715&h=432&f=webp&fit=cover&position=center)

 _今後のLog Explorerのスケジュールされたクエリー機能の設計モックアップ_

[ _ブログの配信登録_](https://blog.cloudflare.com/)を行い、[ _変更ログ_](https://developers.cloudflare.com/changelog/product/log-explorer/)でLog Explorerのさらなる更新情報にまもなくご注目ください。

## Log Explorerへのアクセスを取得

Log Explorerにアクセスするには、ダッシュから直接セルフサービスを購入するか、契約顧客の場合は[ _コンサルテーション_](https://www.cloudflare.com/application-services/products/log-explorer/)をご依頼いただくか、アカウントマネージャーにご連絡ください。詳細は[ _開発者向けドキュメント_](https://developers.cloudflare.com/logs/log-explorer/)をご覧ください。

このページ

オンラインで議論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Finvestigating-multi-vector-attacks-in-log-explorer%2F&t=Log%20Explorer%E3%81%A7%E3%83%9E%E3%83%AB%E3%83%81%E3%83%99%E3%82%AF%E3%83%88%E3%83%AB%E5%9E%8B%E6%94%BB%E6%92%83%E3%82%92%E8%AA%BF%E6%9F%BB%E3%81%99%E3%82%8B)[](https://x.com/intent/post?text=Log+Explorer%E3%81%A7%E3%83%9E%E3%83%AB%E3%83%81%E3%83%99%E3%82%AF%E3%83%88%E3%83%AB%E5%9E%8B%E6%94%BB%E6%92%83%E3%82%92%E8%AA%BF%E6%9F%BB%E3%81%99%E3%82%8B&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Finvestigating-multi-vector-attacks-in-log-explorer%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Finvestigating-multi-vector-attacks-in-log-explorer%2F)[](https://bsky.app/intent/compose?text=Log+Explorer%E3%81%A7%E3%83%9E%E3%83%AB%E3%83%81%E3%83%99%E3%82%AF%E3%83%88%E3%83%AB%E5%9E%8B%E6%94%BB%E6%92%83%E3%82%92%E8%AA%BF%E6%9F%BB%E3%81%99%E3%82%8B+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Finvestigating-multi-vector-attacks-in-log-explorer%2F)[](https://mastodonshare.com/?text=Log+Explorer%E3%81%A7%E3%83%9E%E3%83%AB%E3%83%81%E3%83%99%E3%82%AF%E3%83%88%E3%83%AB%E5%9E%8B%E6%94%BB%E6%92%83%E3%82%92%E8%AA%BF%E6%9F%BB%E3%81%99%E3%82%8B&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Finvestigating-multi-vector-attacks-in-log-explorer%2F)[](https://www.threads.net/intent/post?text=Log+Explorer%E3%81%A7%E3%83%9E%E3%83%AB%E3%83%81%E3%83%99%E3%82%AF%E3%83%88%E3%83%AB%E5%9E%8B%E6%94%BB%E6%92%83%E3%82%92%E8%AA%BF%E6%9F%BB%E3%81%99%E3%82%8B+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Finvestigating-multi-vector-attacks-in-log-explorer%2F)

## 関連するタグ

[R2](https://blog.cloudflare.com/ja-jp/tag/r2/)[SIEM](https://blog.cloudflare.com/ja-jp/tag/siem/)[コネクティビティクラウド](https://blog.cloudflare.com/ja-jp/tag/connectivity-cloud/)[ストレージ](https://blog.cloudflare.com/ja-jp/tag/storage/)[セキュリティ](https://blog.cloudflare.com/ja-jp/tag/security/)[ログ](https://blog.cloudflare.com/ja-jp/tag/logs/)[分析](https://blog.cloudflare.com/ja-jp/tag/analytics/)[製品ニュース](https://blog.cloudflare.com/ja-jp/tag/product-news/)

SNS をフォロー

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 新しい投稿のお知らせを受け取るように登録する

メールアドレス

また、あなたのメールアドレスを共有したりすることはございません。

登録する

ご購読ありがとうございます！受信箱を確認して登録してください。
