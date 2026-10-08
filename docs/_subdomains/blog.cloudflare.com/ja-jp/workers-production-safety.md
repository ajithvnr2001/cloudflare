---
url: https://blog.cloudflare.com/ja-jp/workers-production-safety/
title: \u30d7\u30ed\u30c0\u30af\u30b7\u30e7\u30f3\u306e\u5b89\u5168\u306e\u305f\u3081\u306e\u65b0\u305f\u306a\u30c4\u30fc\u30eb \u2014 Gradual Deployments\u3001\u30bd\u30fc\u30b9\u30de\u30c3\u30d7\u3001Rate Limiting\u3001\u305d\u3057\u3066\u65b0\u305f\u306aSDK | Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:41:28.243397+00:00
---

# プロダクションの安全のための新たなツール — Gradual Deployments、ソースマップ、Rate Limiting、そして新たなSDK | Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/workers-production-safety/

[ブログ](https://blog.cloudflare.com/ja-jp/)

[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[Developer Week](https://blog.cloudflare.com/ja-jp/tag/developer-week/)[Observability](https://blog.cloudflare.com/ja-jp/tag/observability/)2件2件タグを表示

5 タグタグを5件表示

  * 投稿タグ
  * [Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[Developer Week](https://blog.cloudflare.com/ja-jp/tag/developer-week/)[Observability](https://blog.cloudflare.com/ja-jp/tag/observability/)[SDK](https://blog.cloudflare.com/ja-jp/tag/sdk/)[レート制限](https://blog.cloudflare.com/ja-jp/tag/rate-limiting/)
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



[SDK](https://blog.cloudflare.com/ja-jp/tag/sdk/)[レート制限](https://blog.cloudflare.com/ja-jp/tag/rate-limiting/)

[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[Developer Week](https://blog.cloudflare.com/ja-jp/tag/developer-week/)[Observability](https://blog.cloudflare.com/ja-jp/tag/observability/)[SDK](https://blog.cloudflare.com/ja-jp/tag/sdk/)[レート制限](https://blog.cloudflare.com/ja-jp/tag/rate-limiting/)

2024年4月4日

# プロダクションの安全のための新たなツール — Gradual Deployments、ソースマップ、Rate Limiting、そして新たなSDK

![Tanushree Sharma](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46NT9GBM742JJW1W4G7ND8.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Jacob Bednarz](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49K001G8XNDQ04C9HC4S4S.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Tanushree Sharma](https://blog.cloudflare.com/ja-jp/author/tanushree/)、[Jacob Bednarz](https://blog.cloudflare.com/ja-jp/author/jacob-bednarz/)

16分で読了

URLをコピー

この記事は以下でも利用可能です [English](https://blog.cloudflare.com/workers-production-safety/)、[Deutsch](https://blog.cloudflare.com/de-de/workers-production-safety/)、[Español](https://blog.cloudflare.com/es-es/workers-production-safety/)、[Français](https://blog.cloudflare.com/fr-fr/workers-production-safety/)、[한국어](https://blog.cloudflare.com/ko-kr/workers-production-safety/)、[繁體中文](https://blog.cloudflare.com/zh-tw/workers-production-safety/)、[简体中文](https://blog.cloudflare.com/zh-cn/workers-production-safety/).

![New tools for production safety — Gradual deployments, Source maps, Rate Limiting, and new SDKs](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45FR4MNGHSCH0P7DD7P68W.png&w=1800&h=1013&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///+//769vXz8fDw8vHx9PLy8u7u6+fl/////vz98vT16+7y6+7z7u/17ezw5+Tm/////f3/8PP55u315ez36O356Orz5OPq////////8vb+5/D65e/85+/+6Oz55Obv////////+f3/7/f/7Pb/7fb/7fL/6uz2////////////+///+P7/9/7/9fr/8vT8/////////////////////////P//+Pv/////////////////////////////+/3/)

2024のDeveloper Weekは、弊社製品のプロダクションレディの状況に特化してお届けしています。4月1日月曜日、弊社は[D1](https://developers.cloudflare.com/d1/)、[Queues](https://developers.cloudflare.com/queues/)、[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)、および[Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/)がプロダクションレディとなり、一般に利用可能になったことを[発表](https://blog.cloudflare.com/ja-jp/making-full-stack-easier-d1-ga-hyperdrive-queues-ja-jp/)しました。4月2日火曜日には、推論プラットフォームである弊社Workers AIでも同様の[発表](https://blog.cloudflare.com/ja-jp/workers-ai-ga-huggingface-loras-python-support-ja-jp/)を行いました。さらに今後も、弊社からの発表が続く予定です。

一方で、プロダクションレディ対応は、構築するサービスのスケールと信頼性にとどまるものではありません。変更を安全かつ確実に行うためのツールも必要になります。Cloudflareが提供するものだけでなく、お客様のアプリケーションのニーズに合わせたCloudflareの挙動を正確に制御および調整できることも大切になります。

本日は、漸進的なデプロイメント、新しいTail Workersでのソースマップスタックトレース、新たなレート制限API、新たなAPI SDK、Durable Objectsのアップデートなど、ミッションクリティカルな本番環境サービスを念頭に置いた構築について5つのアップデートを発表します。弊社は、Workers、[Access](https://developers.cloudflare.com/cloudflare-one/policies/access/)、[R2](https://developers.cloudflare.com/r2/)、[KV](https://developers.cloudflare.com/kv/)、[Waiting Room](https://developers.cloudflare.com/waiting-room/)、[Vectorize](https://developers.cloudflare.com/vectorize/)、[Queues](https://developers.cloudflare.com/queues/)、[Stream](https://developers.cloudflare.com/stream/)など、独自の製品を構築しています。これらの新機能は、弊社自身が本番環境への対応を確実にするに当たり活用しているもので、これを一般開放できるようになったことをうれしく思っています。

### WorkersとDurable Objectsに漸次的にデプロイする変更

Workerのデプロイは、ほぼ瞬時で完了します。ほんの数秒で、変更が[あらゆる場所で](https://www.cloudflare.com/network/)ライブになります。

本番スケールに到達すると、変更を加えるたびに、量的にも期待値的にもリスクが大きくなります。99.99%のアベイラビリティのSLAを達成する必要があったり、または要求内容が高いP90の遅延のSLOが必要になったりします。トラフィックの100%に対して45秒間ライブになるような質の悪いデプロイでは、何百万ものリクエストが失敗することを意味します。微妙なコード変更であっても、一挙に展開すれば、圧倒されたバックエンドにリトライの大群がどっと押し寄せることになり得ます。これらのリスクは、Workersを基盤とする自社サービスにおいて、弊社自身が対処および軽減しています。

これらのリスクを軽減する方法となるのは、一般にローリングデプロイメントと呼ばれる、変更の段階で来な展開です。

  1. その時点のアプリケーションのバージョンが本番環境で動作を継続。
  2. アプリケーションの新バージョンを本番環境にデプロイするものの、トラフィックのごく一部だけをこの新バージョンにルーティングし、リグレッションやバグを監視しながら、本番環境に「浸透」するのを待つ。もし何か不具合が発生しても、それを早期かつトラフィックのうちに占める割合が小規模（1％など）のうちに把握でき、すぐに元に戻すことが可能。
  3. トラフィックの割合を新バージョンのトラフィックが100%となるまで徐々に増やしていき、その時点で完全にロールアウトします。



本日は、[Cloudflare API](https://developers.cloudflare.com/api/operations/worker-deployments-list-deployments)または[Wrangler CLI](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/gradual-deployments/#via-wrangler)、もしくは[Workersダッシュボード](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/gradual-deployments/#via-the-cloudflare-dashboard)からWorkersとDurable Objectsにコードの変更を徐々にデプロイするファーストクラスの方法を公開します。Gradual Deploymentsは、オープンベータとなります。[Workers Freeプラン](https://developers.cloudflare.com/workers/platform/pricing/#workers)のCloudflareアカウントでGradual Deploymentsを利用でき、まもなく[Workers Paid](https://developers.cloudflare.com/workers/platform/pricing/#workers)およびEnterpriseプランのアカウントでもGradual Deploymentsを利用できるようになります。アカウントがアクセスできるようになると、ダッシュボードにバナーが表示されます。

本番環境でWorkerまたはDurable Objectの2つのバージョンを同時に実行する場合、ほとんどの場合、メトリクス、例外、およびログをバージョン別にフィルタリングできるようにしたいと思うでしょう。これは、新バージョンがトラフィックのごく一部にしかロールアウトされない場合、またはトラフィックを半々に分割した場合のパフォーマンス指標を比較する際、本番環境で発生する問題を早期に発見するのに役立ちます。また、プラットフォーム全体にわたり、バージョンレベルでの可観測性を追加しました。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Splitting traffic between different versions of a Worker.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4792EFMEWR5SFVJAMDC49A.png&w=715&h=353&f=webp&fit=cover&position=center)

  * Workersダッシュボードおよび[GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/)では、バージョンによって分析をフィルタリングできます。
  * [Workers Trace Events](https://developers.cloudflare.com/workers/observability/logging/logpush/)と[Tail Workers](https://developers.cloudflare.com/workers/observability/logging/tail-workers/)イベントには、WorkerのバージョンIDと、オプションのバージョン・メッセージとバージョン・タグ・フィールドが含まれます。
  * [wrangler tailを](https://developers.cloudflare.com/workers/wrangler/commands/#tail)使用してライブログを表示する場合、特定のバージョンのログを表示できます。
  * [Version Metadata](https://developers.cloudflare.com/workers/runtime-apis/bindings/version-metadata/)バインディングを設定することで、Workerのコード内からバージョンID、メッセージ、タグにアクセスできます。



また、各クライアントやユーザーがWorkerの一貫したバージョンしか見ないようにしたい場合もあるでしょう。特定の識別子（ユーザー、セッション、または一意のIDなど）に関連付けられたリクエストが、常に一貫したバージョンのWorkerによって処理されるように、[Version Affinity](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/gradual-deployments/#version-keys-and-session-affinity)を追加しました。[Ruleset Engine](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/gradual-deployments/#setting-cloudflare-workers-version-key-using-ruleset-engine)と一緒に使用すると、[Session Affinity](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/gradual-deployments/#version-keys-and-session-affinity)は「粘着性」を確保するために使用されるメカニズムと識別子の両方を完全に制御できます。

Gradual Deploymentsは、オープンベータとなります。GAに向け、弊社では次のサポートに取り組んでいます。

  * **バージョンの上書き** －本番トラフィックを提供する前にテストするため、Workerの特定のバージョンを起動します。これにより、ブルーグリーンデプロイメントを作成できます。
  * **Cloudflare Pages** －Cloudflare PagesのCI/CDシステムに、デプロイを自動的に進行させられるようになります。
  * **自動ロールバック** －Workerの新しいバージョンでエラー率が急増した場合、デプロイメントを自動的にロールバックします。



フィードバックをお待ちしています！[こちら](https://www.cloudflare.com/lp/developer-week-deployments/)のフィードバックフォームからご意見をお聞かせいただくか、[開発者向けDiscord](https://discord.gg/HJvPcPcN)の#workers-gradual-deployments-betaチャンネルまでご連絡ください。

### Tail Workersのソースマップスタックトレース

生産準備とは、エラーや例外を追跡し、それらをゼロにすることを意味します。エラーが発生した際、一般的にはエラーの[スタックトレース](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stack)、つまり、どの関数が、どの順番で、どの行から、どのファイルから、どの引数で呼び出されたかを最初に確認することになります。

ほとんどのJavaScriptコードは、Workers上だけでなくプラットフォーム全体において、本番環境にデプロイされる前にまずバンドルされ、多くの場合トランスパイルされ、そしてミニファイされます。これは、パフォーマンスを最適化するために小さなバンドルを作成し、必要に応じてTypescriptからJavascriptに変換するために、舞台裏で行われます。

例外が/src/index.js:1:342のようなスタックトレースを返すとしたら、関数のミニファイされたコードの342文字目でエラーが発生したことを意味しています。これは、デバッグにはあまり役に立たたないのは明らかです。

[ソースマップ](https://web.dev/articles/source-maps)が、これを解決します。まず、コンパイルされ最小化されたコードを、記述した元のコードにマップします。ソースマップは、JavaScriptランタイムが返すスタックトレースと組み合わされ、人間が読めるスタックトレースを表示します。たとえば、次のスタックトレースは、Workerがdown.tsファイルの30行目で予期しないnull値を受け取ったことを示しています。このように、デバッグのための便利な出発点となるため、スタックトレースを下に移動すればnull値が設定された関数が呼び出されたことが分かります。

仕組みは次の通りです：
    
    
    Unexpected input value: null
      at parseBytes (src/down.ts:30:8)
      at down_default (src/down.ts:10:19)
      at Object.fetch (src/index.ts:11:12)

  1. [wrangler.toml](https://developers.cloudflare.com/workers/wrangler/configuration/)でupload_source_maps = trueを設定すると、[wrangler deploy](https://developers.cloudflare.com/workers/wrangler/commands/#deploy)または[wrangler versions upload](https://developers.cloudflare.com/workers/wrangler/commands/#versions)を実行した際、Wranglerが自動的にソースマップファイルを生成してアップロードします。
  2. Workerが捕捉されない例外をスローすると、ソースマップを取得し、それを使って例外のスタックトレースをWorkerの元のソースコードの行にマッピングします。
  3. そして、この難読化されたスタックトレースを[リアルタイムログ](https://developers.cloudflare.com/workers/observability/logging/real-time-logs/)または[Tail Workers](https://developers.cloudflare.com/workers/observability/logging/tail-workers/)で見ることができます。



本日よりオープンベータとして、Workerをデプロイする際にソースマップをCloudflareにアップロードできるようになります。4月15日から、Workersランタイムはソースマップを使用してスタックトレースの難読化を解除します。[ドキュメントをお読みになり、さっそくお試しください](https://developers.cloudflare.com/workers/observability/source-maps)。4月15日以降、Workersランタイムがソースマップされたスタックトレースを利用し始めます。ソースマップされたスタックとレースが利用可能になった時点で、Cloudflareダッシュボードに通知を掲載し、[Cloudflare Developers X](https://twitter.com/CloudflareDev?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor)アカウントに投稿します。

### 新しいレート制限API Workers

APIは、適切な[レート制限があって](https://www.cloudflare.com/learning/bots/what-is-rate-limiting/)初めて本番稼動が可能になります。そして成長するにつれ、特定の顧客のニーズのバランスを取ったり、サービスの健全性を保護したり、特定のシナリオで制限を実施したり調整したりするために、実施する必要のある制限の複雑さと多様性が増していきます。CloudflareのAPIにはこのような課題があります。Cloudflareの数十の製品それぞれに多くのAPIエンドポイントがあり、それぞれ異なるレート制限を実施する必要があります。

2017年以降、Cloudflareで[レート制限ルールを](https://developers.cloudflare.com/waf/rate-limiting-rules/)設定できるようになりました。しかし今日まで、ダッシュボードまたはCloudflare APIを介してのみ制御できる状況でした。_ランタイム_中に動作を定義したり、レート制限と直接やりとりするコードをWorkerに書いたりすることはできませんでした。リクエストがWorkerにアクセスする前にレート制限されるかどうかのみしか制御できなかったのです。

本日、オープンベータ版として、Workerからレート制限に直接アクセスできる新しいAPIを発表します。非常に早く、memcachedによって支えらされ、ご利用中のWorkerに非常に簡単に追加できます。例えば、以下は60秒間に100リクエストのレート制限を定義する設定を例示したものです。

次に、Worker内でRATE_LIMITERバインディングのlimitメソッドを呼び出します。上記の設定だと、60秒以内に特定のパスへのリクエストが100回を超えると、このコードは[HTTP 429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429)レスポンスステータスコードを返します。
    
    
    [[unsafe.bindings]]
    name = "RATE_LIMITER"
    type = "ratelimit"
    namespace_id = "1001" # An identifier unique to your Cloudflare account
    
    # Limit: the number of tokens allowed within a given period, in a single Cloudflare location
    # Period: the duration of the period, in seconds. Must be either 60 or 10
    simple = { limit = 100, period = 60 } 

このように、Workers、memcachedのようなデータストアに直接接続できるようになりました。他に、カウンター、ロック、[インメモリ・キャッシュ](https://github.com/cloudflare/workerd/pull/1666)など、実現できるものはあるかと思われるかもしれません。Rate Limitingは、Workerの多くの[分離](https://developers.cloudflare.com/workers/reference/how-workers-works/#isolates)の中でも、今後の提供を検討している多くの初歩的な段階の最初のものとなっています。現在、Workerのグローバルスコープに大きく依存している場合、弊社では特定のユースケースに特化したより良いプリミティブの開発に取り組んでいます。
    
    
    export default {
      async fetch(request, env) {
        const { pathname } = new URL(request.url)
    
        const { success } = await env.RATE_LIMITER.limit({ key: pathname })
        if (!success) {
          return new Response(`429 Failure – rate limit exceeded for ${pathname}`, { status: 429 })
        }
    
        return new Response(`Success!`)
      }
    }

WorkersのRate Limiting APIはオープンベータ化済で、[ドキュメントをお読みいただき](https://developers.cloudflare.com/workers/runtime-apis/bindings/rate-limit)すぐにご利用いただけます。

### CloudflareのAPI用に自動生成された新たなSDK

プロダクションレディ対応とは、ダッシュボードのボタンをクリックして変更を加えることから、[Terraform](https://github.com/cloudflare/terraform-provider-cloudflare)や[Pulumi](https://github.com/pulumi/pulumi-cloudflare)などのインフラストラクチャー・アズ・コード・アプローチを使用したり、独自またはSDK経由でAPIを直接呼び出し、プログラムで変更を加えることを意味します。

[Cloudflare API](https://developers.cloudflare.com/api/)は大規模のもので、常に新しい機能を追加しています。平均して[1日に20～30回APIスキーマを更新](https://github.com/cloudflare/api-schemas/activity)しています。一方、これまで弊社のAPI SDKは手作業で構築・保守されてきたため、これを自動化する必要がありました。

そして本日、弊社でこの取り組みが完了し、[Typescript](https://github.com/cloudflare/cloudflare-typescript)、[Python](https://github.com/cloudflare/cloudflare-python)、[Go](https://github.com/cloudflare/cloudflare-go)の3つの言語で新たなCloudflare API向けクライアントSDKを発表します。

各SDKは、当社の各APIエンドポイントの構造と機能を定義する[OpenAPIスキーマ](https://github.com/cloudflare/api-schemas)に基づき、[Stainless APIを](https://www.stainlessapi.com/)使用して自動的に生成されます。つまり、Cloudflare APIに新しい機能が追加されると、どのCloudflare製品においてもこれらのAPI SDKは自動的に再生成され新しいバージョンが発行されるため、正確で最新の状態に保たれます。

以下のいずれかのコマンドを実行し、SDKをインストールできます。

TerraformやPulumiを使う場合、Cloudflare'のTerraform Providerは現在、自動化されていない既存の[Go SDK](https://github.com/cloudflare/cloudflare-go)を使っています。terraform applyを実行すると、Cloudflare Terraform ProviderがどのAPIをどの順番で作るかを決定し、Go SDKを使って実行します。
    
    
    // Typescript
    npm install cloudflare
    
    // Python
    pip install cloudflare
    
    // Go
    go get -u github.com/cloudflare/cloudflare-go/v2

新しく自動生成されたGo SDKは、すべてのCloudflare製品に対して、より包括的なTerraformサポートへの道を開き、最新のAPIの変更に対応した、正確で最新であると信頼できるツールの基本セットを提供します。弊社では、Cloudflareの製品チームがCloudflare APIを介して公開される新機能を構築するたびに、SDKによって自動的にサポートされる未来を描いて構築しています。2024年中の続報にご期待ください。

### Durable Objectのネームスペース分析とWebSocketハイバネーションGA

[Waiting Room](https://developers.cloudflare.com/waiting-room/)、[R2](https://developers.cloudflare.com/r2/)、[Queues](https://developers.cloudflare.com/queues/)、そして[PartyKitの](https://www.partykit.io/)などのプラットフォームを含む多くの弊社製品は、[Durable Objects](https://developers.cloudflare.com/durable-objects/)使用して構築しています。新しく追加されたオセアニア向けサポートを含め、グローバルに展開されているDurable Objectsは、一枚岩のWorkersとも言え、単一の調整ポイントを提供するとともに、[状態を永続化](https://developers.cloudflare.com/durable-objects/api/transactional-storage-api/)できます。インタラクティブなチャットや共同編集など、リアルタイムでのユーザー連携を必要とするアプリに最適です。アトラシアンはこれについて、次のように述べています。

>  _弊社で実現した新たな能力として、担当部署がより正式に文書化する前に、ブレーンストーミングや初期計画のような非構造化作業を自由形式で記録でき[Confluenceホワイトボード](https://www.atlassian.com/software/confluence/whiteboards)が挙げられます。担当部署では、リアルタイムのコラボレーションのために多くの選択肢を検討し、最終的にCloudflareのDurable Objectsの採用を決定しました。Durable Objectsは、インフラストラクチャを大幅に簡素化し、多数のユーザーに簡単に拡張できるユニークな機能性の組み合わせを備えており、この問題領域に見事にフィットすることが証明されました。 -_ [_アトラシアン_](https://www.atlassian.com/software/confluence/whiteboards)

これまではダッシュボードで関連する分析傾向を公開していなかったため、[GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/)を直接使用しない限り、[Durable Objects](https://developers.cloudflare.com/durable-objects/configuration/access-durable-object-from-a-worker/#generate-ids-randomly)ネームスペース内の使用パターンやエラー率を理解することは困難でした。[Durable Objectsダッシュボード](https://dash.cloudflare.com/?to=/:account/workers/durable-objects)が刷新され、メトリクスをドリルダウンして必要なだけ深く掘り下げることができるようになりました。

Durable Objectsは、初日から[WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)をサポートし、多くのクライアントがDurable Objectに直接接続してメッセージを送受信できるようになります。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2305 Embedded Image - tUWMOW](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45NGJQ7SMHCNME7M5TATPN.png&w=715&h=557&f=webp&fit=cover&position=center)

しかし、時にクライアントアプリケーションはWebSocket接続を開いた後、最終的に何もしなくなることがあります。5時間にわたり、ブラウザーで開いたまま触っていないタブを想像してみてください。メッセージの送受信にWebSocketsを使用している場合、実際には何も使用されていないTCP接続が長時間保たれることになります。この接続がDurable Objectへのものである場合、Durable Objectは実行され続け、何かが起こるのを待たなければならず、メモリを消費し、コストがかかります。

弊社ではこの問題を解決するため、[WebSocketハイバネーション](https://blog.cloudflare.com/workers-pricing-scale-to-zero)を初めて導入し、本日、この機能がベータ版から一般利用可能になったことを発表します。WebSocketハイバネーションでは、ハイバネーション中に使用する自動応答を設定し、状態をシリアライズしてハイバネーションに耐えられるようにします。これによりCloudflareは、クライアントからのオープンなWebSocket接続を維持しながら、Durable Objectをアクティブに実行しないように「ハイバネーション」するために必要なインプットを得ることができます。その結果、実際にステートが必要なときには常にインメモリで利用できるようになり、そうでないときには不必要に保持されなくなります。Durable Objectがハイバネーションしている間は、たとえアクティブなクライアントがその時点でWebSocket経由で接続しているとしても、その間は課金されません。

さらに、Durable ObjectsへのWebSocketメッセージの受信にかかるコストについて、リアルタイム通信のため、より小さくより頻繁なメッセージが好ましいとの開発者からのフィードバックを聞いてきました。本日より、これまでのように1メッセージが1リクエストに相当するのではなく、受信WebSocketメッセージへの課金はリクエストの20分の1相当となります。[価格設定](https://developers.cloudflare.com/durable-objects/platform/pricing/#example-4)の例を以下に示します。

.tg {border-collapse:collapse;border-color:#ccc;border-spacing:0;} .tg td{background-color:#fff;border-color:#ccc;border-style:solid;border-width:1px;color:#333; font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;word-break:normal;} .tg th{background-color:#f0f0f0;border-color:#ccc;border-style:solid;border-width:1px;color:#333; font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;} .tg .tg-0lax{text-align:left;vertical-align:top} .tg .tg-4kyp{color:#0E101A;text-align:left;vertical-align:top} .tg .tg-bhdc{color:#0E101A;font-weight:bold;text-align:left;vertical-align:top}

| WebSocket Connection Requests | Incoming WebSocket Messages | Billed Requests | Request Billing  
---|---|---|---|---  
Before | 10K | 432M | 432,010,000 | $64.65  
After | 10K | 432M | 21,610,000 | $3.09  
  
WebSocket接続リクエスト

受信WebSocketメッセージ

課金対象リクエスト

課金リクエスト

使用前

10千

432百万

432,010,000

$64.65

使用後

10千

432百万

21,610,000

$3.09

### 複雑な本番設定を必要とせず、プロダクションレディ

前世代のクラウドプラットフォームでプロダクションレディになるということは、出荷速度を落とすことを意味しました。つまり、バラバラのツールをつなぎ合わせたり、チーム全体を立ち上げて社内のプラットフォームに取り組ませたりしていました。障害物が立ちはだかるプラットフォームに、独自の生産性レイヤーを後付けしなければならなかったのです。

Cloudflare Developer Platformは成長し、プロダクションレディとなりました。製品が直感的に連動し、同じことをする上で無数の異なる方法を存在させず、連動し合うものを理解するのに役立つ互換性マトリックスが不要な統合プラットフォームであり続けます。アップデートはそれぞれ、Cloudflareの製品やプラットフォームの一部に新機能を統合し、前述の思想を体現しています。

弊社では、お客様に次に求められているものが何かだけではなく、さらにシンプルにできると思う点、もしくは弊社製品がさらに優れた在り方で連携できると思う点について、皆さまからのご意見をお待ちしています。いつでも、[Cloudflare Developers Discord](https://discord.cloudflare.com/)にてお知らせください。

このページ

オンラインで議論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fworkers-production-safety%2F&t=%E3%83%97%E3%83%AD%E3%83%80%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%E3%81%AE%E5%AE%89%E5%85%A8%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E6%96%B0%E3%81%9F%E3%81%AA%E3%83%84%E3%83%BC%E3%83%AB%20%E2%80%94%20Gradual%20Deployments%E3%80%81%E3%82%BD%E3%83%BC%E3%82%B9%E3%83%9E%E3%83%83%E3%83%97%E3%80%81Rate%20Limiting%E3%80%81%E3%81%9D%E3%81%97%E3%81%A6%E6%96%B0%E3%81%9F%E3%81%AASDK)[](https://x.com/intent/post?text=%E3%83%97%E3%83%AD%E3%83%80%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%E3%81%AE%E5%AE%89%E5%85%A8%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E6%96%B0%E3%81%9F%E3%81%AA%E3%83%84%E3%83%BC%E3%83%AB+%E2%80%94+Gradual+Deployments%E3%80%81%E3%82%BD%E3%83%BC%E3%82%B9%E3%83%9E%E3%83%83%E3%83%97%E3%80%81Rate+Limiting%E3%80%81%E3%81%9D%E3%81%97%E3%81%A6%E6%96%B0%E3%81%9F%E3%81%AASDK&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fworkers-production-safety%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fworkers-production-safety%2F)[](https://bsky.app/intent/compose?text=%E3%83%97%E3%83%AD%E3%83%80%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%E3%81%AE%E5%AE%89%E5%85%A8%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E6%96%B0%E3%81%9F%E3%81%AA%E3%83%84%E3%83%BC%E3%83%AB+%E2%80%94+Gradual+Deployments%E3%80%81%E3%82%BD%E3%83%BC%E3%82%B9%E3%83%9E%E3%83%83%E3%83%97%E3%80%81Rate+Limiting%E3%80%81%E3%81%9D%E3%81%97%E3%81%A6%E6%96%B0%E3%81%9F%E3%81%AASDK+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fworkers-production-safety%2F)[](https://mastodonshare.com/?text=%E3%83%97%E3%83%AD%E3%83%80%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%E3%81%AE%E5%AE%89%E5%85%A8%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E6%96%B0%E3%81%9F%E3%81%AA%E3%83%84%E3%83%BC%E3%83%AB+%E2%80%94+Gradual+Deployments%E3%80%81%E3%82%BD%E3%83%BC%E3%82%B9%E3%83%9E%E3%83%83%E3%83%97%E3%80%81Rate+Limiting%E3%80%81%E3%81%9D%E3%81%97%E3%81%A6%E6%96%B0%E3%81%9F%E3%81%AASDK&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fworkers-production-safety%2F)[](https://www.threads.net/intent/post?text=%E3%83%97%E3%83%AD%E3%83%80%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%E3%81%AE%E5%AE%89%E5%85%A8%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E6%96%B0%E3%81%9F%E3%81%AA%E3%83%84%E3%83%BC%E3%83%AB+%E2%80%94+Gradual+Deployments%E3%80%81%E3%82%BD%E3%83%BC%E3%82%B9%E3%83%9E%E3%83%83%E3%83%97%E3%80%81Rate+Limiting%E3%80%81%E3%81%9D%E3%81%97%E3%81%A6%E6%96%B0%E3%81%9F%E3%81%AASDK+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fworkers-production-safety%2F)

## 関連するタグ

[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[Developer Week](https://blog.cloudflare.com/ja-jp/tag/developer-week/)[Observability](https://blog.cloudflare.com/ja-jp/tag/observability/)[SDK](https://blog.cloudflare.com/ja-jp/tag/sdk/)[レート制限](https://blog.cloudflare.com/ja-jp/tag/rate-limiting/)

SNS をフォロー

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)

  * ![Jacob Bednarz](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49K001G8XNDQ04C9HC4S4S.jpg&w=64&h=64&f=webp&fit=cover&position=center)[Jacob Bednarz](https://blog.cloudflare.com/ja-jp/author/jacob-bednarz/)

[](https://jacobbednarz.com)




## 新しい投稿のお知らせを受け取るように登録する

メールアドレス

また、あなたのメールアドレスを共有したりすることはございません。

登録する

ご購読ありがとうございます！受信箱を確認して登録してください。
