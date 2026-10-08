---
url: https://blog.cloudflare.com/ja-jp/pingora-oss-smuggling-vulnerabilities/
title: Pingora OSS\u30c7\u30d7\u30ed\u30a4\u306b\u304a\u3051\u308b\u30ea\u30af\u30a8\u30b9\u30c8\u30b9\u30cb\u30c3\u30d5\u30a3\u30f3\u30b0\u306e\u8106\u5f31\u6027\u3092\u4fee\u6b63\u3059\u308b | Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:49:43.780976+00:00
---

# Pingora OSSデプロイにおけるリクエストスニッフィングの脆弱性を修正する | Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/pingora-oss-smuggling-vulnerabilities/

[ブログ](https://blog.cloudflare.com/ja-jp/)

[Pingora](https://blog.cloudflare.com/ja-jp/tag/pingora/)[アプリケーションセキュリティ](https://blog.cloudflare.com/ja-jp/tag/application-security/)[オープンソース](https://blog.cloudflare.com/ja-jp/tag/open-source/)1件1件タグを表示

4 タグタグを4件表示

  * 投稿タグ
  * [Pingora](https://blog.cloudflare.com/ja-jp/tag/pingora/)[アプリケーションセキュリティ](https://blog.cloudflare.com/ja-jp/tag/application-security/)[オープンソース](https://blog.cloudflare.com/ja-jp/tag/open-source/)[セキュリティ](https://blog.cloudflare.com/ja-jp/tag/security/)
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



[セキュリティ](https://blog.cloudflare.com/ja-jp/tag/security/)

[Pingora](https://blog.cloudflare.com/ja-jp/tag/pingora/)[アプリケーションセキュリティ](https://blog.cloudflare.com/ja-jp/tag/application-security/)[オープンソース](https://blog.cloudflare.com/ja-jp/tag/open-source/)[セキュリティ](https://blog.cloudflare.com/ja-jp/tag/security/)

2026年3月9日

# Pingora OSSデプロイにおけるリクエストスニッフィングの脆弱性を修正する

![Edward Wang](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW461JESP3W5FAGRMPYV23AR.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Fei Deng](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48NSR5MVS5T6CKN7613095.webp&w=64&h=64&f=webp&fit=cover&position=center)![Andrew Hauck](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44PMGPP5RFKJT72RPHZAYC.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Edward Wang](https://blog.cloudflare.com/ja-jp/author/edward-h-wang/)、[Fei Deng](https://blog.cloudflare.com/ja-jp/author/fei-deng/)、[Andrew Hauck](https://blog.cloudflare.com/ja-jp/author/andrew-hauck/)

13分で読了

URLをコピー

この記事は以下でも利用可能です [English](https://blog.cloudflare.com/pingora-oss-smuggling-vulnerabilities/)、[한국어](https://blog.cloudflare.com/ko-kr/pingora-oss-smuggling-vulnerabilities/).

![BLOG-3181 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW489743F8DBXPFBDQBPWAFQ.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA//////r97u3x3uHp297r4eHw6Obv6+jq/////fv/5ej00NjszdPs2Nnw4+Lw6efs/////f3/3ub4w9DxwMrw0dPy4ODy6Onv////////4On+w9L3ws321Nj35eX26+7z////////7fP/1eD91N395Of+8fH99Pb5/////////v//7fP/7vP/+fr////////+////////////////////////////////////////////////////////////////)

_このコンテンツは自動機械翻訳サービスによる翻訳版であり、皆さまの便宜のために提供しています。原本の英語版と異なる誤り、省略、解釈の微妙な違いが含まれる場合があります。ご不明な点がある場合は、英語版原本をご確認ください。_

2025年12月、CloudflareはHTTP/1.xの報告を受けました。Pingoraをイングレスプロキシの構築に使用する際の、[ _Pingoraオープンソース_](https://github.com/cloudflare/pingora)フレームワークにおけるリクエストスマグリングの脆弱性。本日は、これらの脆弱性の仕組みと、[ _Pingora 0.8.0_](https://github.com/cloudflare/pingora/releases/tag/0.8.0)でどのようにパッチを適用したかについてお話しします。

脆弱性は[ _CVE-2026-2833_](https://www.cve.org/CVERecord?id=CVE-2026-2833)、[ _CVE-2026-2835_](https://www.cve.org/CVERecord?id=CVE-2026-2835)、および[ _CVE-2026-2836_](https://www.cve.org/CVERecord?id=CVE-2026-2836)です。これらの問題は、当社の[ _バグバウンティプログラム_](https://www.cloudflare.com/disclosure/)を通じてRajat Raghav氏（xclow3n）から責任を持って報告されました。

**CloudflareのCDNと顧客トラフィックに影響はなかった** ことが、当社の調査でわかりました。**Cloudflareのお客様は、何もする必要がなく、影響も検出されませんでした。**

Cloudflareのネットワークのアーキテクチャにより、これらの脆弱性は悪用されませんでした。Pingoraは、CloudflareのCDNのイングレスプロキシとして使用されていません。

しかし、これらの問題は、インターネットに公開されるスタンドアロンのPingoraデプロイメントに影響を与え、攻撃者に以下を可能にする可能性があります。

  * Pingoraプロキシ層セキュリティ制御をバイパス
  * クロスユーザーハイジャック攻撃（セッションまたは資格情報の盗難）のために、HTTPリクエスト/レスポンスをバックエンドと非同期化する
  * Pingoraプロキシ層キャッシュで共有バックエンドからコンテンツを取得



修正とハードニングを加えた[ _Pingora 0.8.0_](https://github.com/cloudflare/pingora/releases/tag/0.8.0)をリリースしました。Cloudflareのお客様は影響を受けませんでしたが、Pingoraフレームワークのユーザーは**できるだけ早くアップグレードする** ことを強くお勧めします。

## 脆弱性とは？

レポートには、非同期攻撃を引き起こす可能性のあるいくつかの異なるHTTP/1攻撃悪意のあるペイロードについて説明されています。このようなリクエストは、リクエスト本文がどこで終わるかについて、プロキシとバックエンドとの不一致を引き起こす可能性があり、2番目のリクエストがプロキシ層のチェックを通過して「スニッフィング」される可能性があります。研究者は、基本的なPingoraリバースプロキシがリクエスト本文長をどのように誤って解釈し、それらのリクエストをNode/Expressやuvicornなどのサーバーバックエンドに転送するかを検証するための概念実証を提供しました。

報告を受けた当社のエンジニアリングチームは、直ちに調査を行い、報告者自身も確認したように、Cloudflare CDN自体に脆弱性がないことを確認しました。しかし、チームは、Pingoraが共有バックエンドのイングレスプロキシとして機能するときに脆弱性が存在することも検証しました。

設計上、Pingoraフレームワークは、RFCに厳密に準拠していないエッジケースのHTTPリクエストまたはレスポンスを[ _許可しています_](https://blog.cloudflare.com/how-we-built-pingora-the-proxy-that-connects-cloudflare-to-the-internet/#design-decisions)。これは、レガシーHTTPスタックを持つお客様のために、この種のトラフィックを受け入れなければならないためです。しかし、可能性にも制限を受けますが、Cloudflare自体が脆弱性にさらされることを避けるためには限界があります。

この場合、Pingoraは、HTTP/1スタック内でリクエストボディがRFC非準拠の解釈をするため、こうした非同期攻撃が可能でした。Cloudflare内のPingoraデプロイメントは、イングレストラフィックの影響に直接さらされず、Pingoraサービスに到着した本番用トラフィックは、こうした誤解の影響を受けないことが確認されました。したがって、2025年5月に公開された[ _以前のPingora密輸の脆弱性_](https://blog.cloudflare.com/resolving-a-request-smuggling-vulnerability-in-pingora/)とは異なり、Cloudflareのトラフィック自体を悪用することはできませんでした。

これらの攻撃悪意のあるペイロードがどのように機能したかを、ケースバイケースで説明します。

### 1\. 101ハンドシェイクなしの早期アップグレード

最初のレポートでは、`Upgrade` ヘッダー値を持つリクエストが、バックエンドがアップグレードを受け入れる前に（`101 Switching Protocols` を返すことで）、PingoraがHTTP接続上の後続のバイトを即座に通過させることが示されました。このように、攻撃者は同じ接続上で、アップグレードリクエストの後に、2つ目のHTTPリクエストをパイプライン化することができます。
    
    
    GET / HTTP/1.1
    Host: example.com
    Upgrade: foo
    
    
    GET /admin HTTP/1.1
    Host: example.com

Pingoraは、最初のリクエストだけを解析し、残りのバッファリングされたバイトを「アップグレードされた」ストリームとして扱い、[ _Upgradeヘッダーにより_](https://github.com/cloudflare/pingora/blob/ef017ceb01962063addbacdab2a4fd2700039db5/pingora-core/src/protocols/http/v1/server.rs#L797)「パススルー」モードでバックエンドに直接転送します（レスポンスが[ _受信されるまで_](https://github.com/cloudflare/pingora/blob/ef017ceb01962063addbacdab2a4fd2700039db5/pingora-core/src/protocols/http/v1/server.rs#L523)）。

これは、[ _RFC 9110_](https://datatracker.ietf.org/doc/html/rfc9110#field.upgrade)に準拠したHTTP/1.1アップグレードプロセスの意図された動作とは全く異なります。後続のバイトは、`101 Switching Protocols`ヘッダーが受信された場合、アップグレードされたストリームの一部として _のみ_ 解釈されます。代わりに、`200 OK`レスポンスが受信された場合、後続のバイトはHTTPとして引き続き解釈されます。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3181 image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW456EC4HTCKZHH1YK0JCJE0.png&w=715&h=458&f=webp&fit=cover&position=center)

 _アップグレードリクエストを送信し、部分的なHTTPリクエストをパイプラインで行う攻撃者は、非同期攻撃を引き起こす可能性があります。Pingoraは、バックエンドサーバーが200でアップグレードを拒否した場合でも、両方を同じアップグレードされたリクエストとして誤って解釈します。_

不適切なパススルーを介して、101以外のレスポンスを受信したPingoraデプロイは、2番目の部分的なHTTPリクエストをそのまま上流に転送し、Pingoraユーザー定義のACL処理またはWAFロジックをバイパスして、上流への接続をポイズニングする可能性があります。これにより、別のユーザーからの後続のリクエストが`/admin`レスポンスを不適切に受け取る可能性があります。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3181 image 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49J66B2GBQK2GEXF3HGR7G.png&w=715&h=264&f=webp&fit=cover&position=center)

 _攻撃悪意のあるペイロードの後、Pingoraとバックエンドサーバーは「非同期」状態になっています。バックエンドサーバーは、Pingoraが転送した部分的な/attackリクエストヘッダーの残りが完了したと考えるまで待ちます。Pingoraが別のユーザーのリクエストを転送すると、バックエンドサーバーから見ると2つのヘッダーが組み合わされ、攻撃者はそのユーザーの応答をポイズニングしています。_

それ以来、Pingoraに[ _パッチを適用_](https://github.com/cloudflare/pingora/commit/824bdeefc61e121cc8861de1b35e8e8f39026ecd)して、アップストリームが`101 Switching Protocols`で応答すると、後続のバイトの解釈を切り替えるようにしました。

Cloudflareが**影響を受けなかった** ことを2つの理由で確認しました。

  1. イングレスのCDNプロキシは、このような不適切な動作をしません。
  2. 内部Pingoraサービスへのクライアントは、HTTP/1リクエストを[ _パイプライン化_](https://en.wikipedia.org/wiki/HTTP_pipelining)しようとしません。さらに、これらのクライアントが直接通信するPingoraサービスは、`Connection: close`ヘッダーを挿入することで、これらの`アップグレード`リクエストでキープアライブを無効化します。これにより、同じ接続を介して送信される追加のリクエストが送信され、その後、維持されることを防ぎます。



### 2\. HTTP/1.0、クローズドリミット、転送エンコーディング

レポーターは、 _思われる_ より典型的な「CL.TE」デシンク型攻撃も実証しました。この攻撃では、PingoraプロキシがContent-Lengthをフレーミングとして使用し、バックエンドがTransfer-Encodingをフレーミングとして使用します。
    
    
    GET / HTTP/1.0
    Host: example.com
    Connection: keep-alive
    Transfer-Encoding: identity, chunked
    Content-Length: 29
    
    0
    
    GET /admin HTTP/1.1
    X:
    

レポーティングの例では、Pingoraは最初のGET /リクエストヘッダーの後に後続のバイトをすべてそのリクエスト本文の一部として扱いますが、node.jsバックエンドサーバーは本文がチャンク化された、長さゼロのチャンクで終わると解釈します。実際には、いくつかの事が起こっています。

  1. Pingoraのチャンク化されたエンコーディングの認識は非常に最低限であり（`Transfer-Encoding`が「[ _chunked_](https://github.com/cloudflare/pingora/blob/9ac75d0356f449d26097e08bf49af14de6271727/pingora-core/src/protocols/http/v1/common.rs#L146)」であるかどうかの確認のみ）、エンコーディングまたは`Transfer-Encoding`ヘッダーは1つしか存在しないと仮定しました。しかし、RFCは、チャンク化されたフレーミングを適用するために、[ _最終_](https://datatracker.ietf.org/doc/html/rfc9112#section-6.3-2.4.1)エンコーディングが _チャンク化_ されることを`義務付けている`にすぎません。そのため、RFCによると、このリクエストにはメッセージ本文がチャンク化されている必要があります（HTTP/1.0—これについては後述します）。
  2. Pingoraは、 _また_ 、実際には`Content-Length`を使用していませんでした（転送エンコーディングが[ _RFCの規定により_](https://datatracker.ietf.org/doc/html/rfc9112#section-6.3-2.3)Content-Lengthをオーバーライドしたため）。Transfer-Encodingが認識されず、HTTP/1.0バージョンであるため、リクエストボディは、[ _代わりにクローズ区切りとして扱われました_](https://github.com/cloudflare/pingora/blob/ef017ceb01962063addbacdab2a4fd2700039db5/pingora-core/src/protocols/http/v1/server.rs#L817)（つまり、レスポンスボディの終了は、基となるトランスポート接続の終了によってマークされます）。フレーミングヘッダーの欠如は、HTTP/1.0でも同じ誤解を引き起こす可能性があります。レスポンス本文はクローズ区切りにできますが、リクエスト本文は _決して_ クローズ区切りにすることはできません。実際、この明確化は、[ _RFC 9112_](https://datatracker.ietf.org/doc/html/rfc9112#section-6.3-4.1)で別の注記として明示的に言及されています。
  3. これはHTTP/1.0転送エンコーディングを[ _定義しないリクエストです_](https://datatracker.ietf.org/doc/html/rfc9112#appendix-C.2.3-1)。RFCでは、転送エンコーディングを含むHTTP/1.0リクエストは、「フレーミングに欠陥があるかのようにメッセージを扱って」接続を閉じる必要があると[義務付けています](https://datatracker.ietf.org/doc/html/rfc9112#section-6.1-16)。nginxやhyperなどのパーサーは、曖昧なフレーミングを避けるために、これらのリクエストを拒否するだけです。



![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3181 image 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44RVNZNMVZM9AWKQN5CB66.png&w=715&h=441&f=webp&fit=cover&position=center)

 _攻撃者がHTTP/1.0ドメインの後に部分的なHTTPリクエストヘッダーを+ Transfer-Encodingリクエストでは、Pingoraはその部分的なヘッダーを別個のリクエストとしてではなく、同じリクエストの一部として誤って解釈します。これにより、時期尚早なアップグレードの例で説明したと同じ種類の非同期攻撃が可能になります。_

これは、特にレスポンスとリクエストのメッセージのフレーミングという点で、RFCのより根本的な誤解を招くものです。それ以来、不適切な[ _多重のTransfer-Encodingの解析_](https://github.com/cloudflare/pingora/commit/7f7166d62fa916b9f11b2eb8f9e3c4999e8b9023)を修正し、HTTPリクエストボディが[ _クローズ区切りと見なされることがない_](https://github.com/cloudflare/pingora/commit/40c3c1e9a43a86b38adeab8da7a2f6eba68b83ad)ように、リクエスト長のガイドラインに厳密に準拠し、[ _不正なContent-Length_](https://github.com/cloudflare/pingora/commit/fc904c0d2c679be522de84729ec73f0bd344963d)および[ _HTTP/1.0 + Transfer-Encoding_](https://github.com/cloudflare/pingora/commit/87e2e2fb37edf9be33e3b1d04726293ae6bf2052)のリクエストメッセージを拒否しました。さらに、追加した保護には、デフォルトで[ _拒否する_](https://github.com/cloudflare/pingora/commit/d3d2cf5ef4eca1e5d327fe282ec4b4ee474350c6) [_CONNECT_](https://datatracker.ietf.org/doc/html/rfc9110#name-connect)リクエストが含まれます。これは、HTTPプロキシロジックは現在、CONNECTアップグレードプロキシの目的でCONNECTを特別なものとして扱わないためであり、これらのリクエストには特別な[ _メッセージフレーミングルール_](https://datatracker.ietf.org/doc/html/rfc9112#section-6.3-2.2)があります。（受信のCONNECTリクエストはCloudflare CDNによって[ _拒否される_](https://developers.cloudflare.com/fundamentals/concepts/traffic-flow-cloudflare/#cloudflares-network)ことに注意してください。）

当社のサービスを内部で調査・計測したところ、Pingoraサービスに到着したリクエストが誤って解釈されることはなかったと考えました。CDNのダウンストリームのプロキシレイヤーはHTTP/1.1のみとして転送し、無効なContent-Lengthなどの曖昧なフレーミングを拒否し、チャンク化されたリクエストに対しては、単一の`Transfer-Encoding: chunked`ヘッダーのみを転送することがわかりました。

### 3\. キャッシュキーの構築

この調査者は、デフォルトの`CacheKey`の構築に関する別のキャッシュポイズニングの脆弱性も報告しています。[ _素朴なデフォルト実装_](https://github.com/cloudflare/pingora/blob/ef017ceb01962063addbacdab2a4fd2700039db5/pingora-cache/src/key.rs#L218)は、URI パスのみを考慮に入れており（ホストヘッダーやアップストリームサーバーのHTTPスキームなどの他の要素を含まず）、そのため、同じHTTPパスを使用する異なるホストが競合し、互いのキャッシュを汚染する可能性がありました。

これは、デフォルトの`CacheKey`実装を使用することを選択したアルファ版プロキシキャッシング機能のユーザーに影響を与えます。その後、このデフォルトは[ _削除しました_](https://github.com/cloudflare/pingora/commit/257b59ada28ed6cac039f67d0b71f414efa0ab6e)。HTTPスキーム + ホスト + URIのようなものを使用することは多くのアプリケーションにとって理にかなっていますが、ユーザーにはキャッシュキーを構築する際に注意を払っていただきたいためです。たとえば、プロキシロジックがアップストリームリクエストのURIやメソッドを条件付きに調整する場合、そのロジックもポイズニングを回避するためにキャッシュキースキームに要因を組み込む必要があります。

内部的には、Cloudflareの[ _デフォルトのキャッシュキー_](https://developers.cloudflare.com/cache/how-to/cache-keys/)は、キャッシュキーポイズニングを防止するために多くの要素を使用しており、以前に提供されていたデフォルトを使用することはありません。

## 推奨事項

Pingoraをプロキシとして使用する場合は、できるだけ早い段階で[ _Pingora 0.8.0_](https://github.com/cloudflare/pingora/releases/tag/0.8.0)にアップグレードしてください。

この脆弱性により、Pingoraユーザーに多大な影響を与えたことをお詫び申し上げます。PingoraがCloudflareを超える重要なインターネットインフラストラクチャとしての地位を確立するに伴い、厳格なRFCコンプライアンスの使用をデフォルトで促進することがフレームワークにとって重要であると考えており、今後もこの取り組みを継続していきます。フレームワークのユーザーは、Cloudflareと同じ「ワイルドインターネット」に悩まされる必要はほとんどないはずです。私たちの意図は、デフォルトで最新のRFC基準に厳格に準拠することで、Pingoraユーザーのセキュリティを強化し、インターネット全体をベストプラクティスに向けて移行することです。

## 情報開示と対応のタイムライン

\- 2025年12月2日：バグバウンティ経由でアップグレードベースのスニッフィングが報告される。

\- 2026年1月13日：転送エンコーディング / HTTP/1.0の解析に関する問題が報告されています。

\- 2026年1月18日：デフォルトのキャッシュキー構築の問題が報告されました。

\- 2026年1月29日から2026年2月13日：修正に関する報告者が確認済み。さらなるRFCコンプライアンスチェックに取り組みます。

\- 2026年2月25日：キャッシュキーのデフォルトの削除と追加のRFCチェックがリサーチャーと検証済み。

\- 2026年3月2日：Pingora 0.8.0をリリース

\- 2026-03-04: CVEアドバイザリーを公開

## 謝辞

レポート、詳細な複製、そしてバグバウンティプログラムを通じて修正を確認してくださったRajat Raghav氏（xclow3n）に感謝いたします。詳細については、研究者の[対応するブログ記事](https://xclow3n.github.io/post/6)をご覧ください。

また、Pingoraオープンソースコミュニティの積極的な関与、レポートの発行、フレームワークへの貢献に心からの謝意を表します。Cloudflareは、より良いインターネットの構築をサポートしてくれる存在です。

このページ

オンラインで議論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fpingora-oss-smuggling-vulnerabilities%2F&t=Pingora%20OSS%E3%83%87%E3%83%97%E3%83%AD%E3%82%A4%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8B%E3%83%AA%E3%82%AF%E3%82%A8%E3%82%B9%E3%83%88%E3%82%B9%E3%83%8B%E3%83%83%E3%83%95%E3%82%A3%E3%83%B3%E3%82%B0%E3%81%AE%E8%84%86%E5%BC%B1%E6%80%A7%E3%82%92%E4%BF%AE%E6%AD%A3%E3%81%99%E3%82%8B)[](https://x.com/intent/post?text=Pingora+OSS%E3%83%87%E3%83%97%E3%83%AD%E3%82%A4%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8B%E3%83%AA%E3%82%AF%E3%82%A8%E3%82%B9%E3%83%88%E3%82%B9%E3%83%8B%E3%83%83%E3%83%95%E3%82%A3%E3%83%B3%E3%82%B0%E3%81%AE%E8%84%86%E5%BC%B1%E6%80%A7%E3%82%92%E4%BF%AE%E6%AD%A3%E3%81%99%E3%82%8B&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fpingora-oss-smuggling-vulnerabilities%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fpingora-oss-smuggling-vulnerabilities%2F)[](https://bsky.app/intent/compose?text=Pingora+OSS%E3%83%87%E3%83%97%E3%83%AD%E3%82%A4%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8B%E3%83%AA%E3%82%AF%E3%82%A8%E3%82%B9%E3%83%88%E3%82%B9%E3%83%8B%E3%83%83%E3%83%95%E3%82%A3%E3%83%B3%E3%82%B0%E3%81%AE%E8%84%86%E5%BC%B1%E6%80%A7%E3%82%92%E4%BF%AE%E6%AD%A3%E3%81%99%E3%82%8B+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fpingora-oss-smuggling-vulnerabilities%2F)[](https://mastodonshare.com/?text=Pingora+OSS%E3%83%87%E3%83%97%E3%83%AD%E3%82%A4%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8B%E3%83%AA%E3%82%AF%E3%82%A8%E3%82%B9%E3%83%88%E3%82%B9%E3%83%8B%E3%83%83%E3%83%95%E3%82%A3%E3%83%B3%E3%82%B0%E3%81%AE%E8%84%86%E5%BC%B1%E6%80%A7%E3%82%92%E4%BF%AE%E6%AD%A3%E3%81%99%E3%82%8B&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fpingora-oss-smuggling-vulnerabilities%2F)[](https://www.threads.net/intent/post?text=Pingora+OSS%E3%83%87%E3%83%97%E3%83%AD%E3%82%A4%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8B%E3%83%AA%E3%82%AF%E3%82%A8%E3%82%B9%E3%83%88%E3%82%B9%E3%83%8B%E3%83%83%E3%83%95%E3%82%A3%E3%83%B3%E3%82%B0%E3%81%AE%E8%84%86%E5%BC%B1%E6%80%A7%E3%82%92%E4%BF%AE%E6%AD%A3%E3%81%99%E3%82%8B+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fpingora-oss-smuggling-vulnerabilities%2F)

## 関連するタグ

[Pingora](https://blog.cloudflare.com/ja-jp/tag/pingora/)[アプリケーションセキュリティ](https://blog.cloudflare.com/ja-jp/tag/application-security/)[オープンソース](https://blog.cloudflare.com/ja-jp/tag/open-source/)[セキュリティ](https://blog.cloudflare.com/ja-jp/tag/security/)

SNS をフォロー

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 新しい投稿のお知らせを受け取るように登録する

メールアドレス

また、あなたのメールアドレスを共有したりすることはございません。

登録する

ご購読ありがとうございます！受信箱を確認して登録してください。
