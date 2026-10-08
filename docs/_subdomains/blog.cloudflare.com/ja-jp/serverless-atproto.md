---
url: https://blog.cloudflare.com/ja-jp/serverless-atproto/
title: Serverless Statusphere\uff1aCloudflare\u306e\u958b\u767a\u8005\u30d7\u30e9\u30c3\u30c8\u30d5\u30a9\u30fc\u30e0\u4e0a\u3067\u30b5\u30fc\u30d0\u30fc\u30ec\u30b9ATProto\u30a2\u30d7\u30ea\u30b1\u30fc\u30b7\u30e7\u30f3\u3092\u69cb\u7bc9\u3059\u308b\u624b\u9806 | Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:35:48.248787+00:00
---

# Serverless Statusphere：Cloudflareの開発者プラットフォーム上でサーバーレスATProtoアプリケーションを構築する手順 | Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/serverless-atproto/

[ブログ](https://blog.cloudflare.com/ja-jp/)

[Durable Objects](https://blog.cloudflare.com/ja-jp/tag/durable-objects/)[Rust](https://blog.cloudflare.com/ja-jp/tag/rust/)[Wrangler](https://blog.cloudflare.com/ja-jp/tag/wrangler/)

3 タグタグを3件表示

  * 投稿タグ
  * [Durable Objects](https://blog.cloudflare.com/ja-jp/tag/durable-objects/)[Rust](https://blog.cloudflare.com/ja-jp/tag/rust/)[Wrangler](https://blog.cloudflare.com/ja-jp/tag/wrangler/)
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



[Durable Objects](https://blog.cloudflare.com/ja-jp/tag/durable-objects/)[Rust](https://blog.cloudflare.com/ja-jp/tag/rust/)[Wrangler](https://blog.cloudflare.com/ja-jp/tag/wrangler/)

2025年7月24日

# Serverless Statusphere：Cloudflareの開発者プラットフォーム上でサーバーレスATProtoアプリケーションを構築する手順

![Inanna Malick](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47SJ7VTDH3QFFKFA26KM6J.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Inanna Malick](https://blog.cloudflare.com/ja-jp/author/inanna-malick/)

14分で読了

URLをコピー

この記事は以下でも利用可能です [English](https://blog.cloudflare.com/serverless-atproto/)、[简体中文](https://blog.cloudflare.com/zh-cn/serverless-atproto/).

![BLOG-2813 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47G8K4GKNHP2FDHR8RR263.png&w=1600&h=900&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA//7/+Pj95+rx3uHr5OTt7uvx7uvu5eTm////+fr+3+XyzNbr0tjt4uLx6ufu5+bn////+/3/2eP1vM3twMzv1try5+bw6+no////////3Of5u8/xvczy1dv26en08e/s////////6fL/zt73z9v54uf98/L6+ffy////////+///6vL+6vH/9vj///7////5///////////////////////////////+////////////////////////////////)

_このコンテンツは自動機械翻訳サービスによる翻訳版であり、皆さまの便宜のために提供しています。原本の英語版と異なる誤り、省略、解釈の微妙な違いが含まれる場合があります。ご不明な点がある場合は、英語版原本をご確認ください。_

ソーシャルメディアユーザーは、プラットフォームがシャットダウンしたり、ピボットしたりするたびにIDとデータを失うのにうんざりしています。ATProtoのエコシステム（[ _Authenticated Transfer プロトコル_](https://atproto.com/)の略）では、ユーザーが自分のデータとIDを所有します。彼らが公開するものはすべて、暗号署名されたグローバルなソーシャルWebの一部となります。[ _Bluesky_](https://bsky.social/)は最初の大きな例ですが、分散型ソーシャルネットワークの新しい波は始まったばかりです。この記事では、Cloudflareの開発者用プラットフォーム上で、完全なサーバーレスのATProtoアプリケーションを構築してデプロイする方法を紹介します。

なぜ[ _サーバーレス_](https://www.cloudflare.com/learning/serverless/what-is-serverless/)なのか？VMの管理、データベースのスケーリング、CIパイプラインの維持、可用性ゾーン全体へのデータの配信、[ _DDoS攻撃に対するAPIの保護_](https://www.cloudflare.com/learning/security/api/what-is-api-security/)などのオーバーヘッドが実際の構築から目をそらさせます。

そこでCloudflareの出番です。当社の[ _Developer Platform_](https://www.cloudflare.com/developer-platform/)を活用して、当社のグローバルネットワーク上で動作するアプリケーションを構築できます。[ _Workers_](https://workers.cloudflare.com/)は数ミリ秒でグローバルにコードをデプロイし、[ _KV_](https://developers.cloudflare.com/kv/)は高速でグローバルに分散されたキャッシングを提供し、[ _D1_](https://developers.cloudflare.com/d1/)は[分散型リレーショナルデータベース](https://www.cloudflare.com/developer-platform/products/d1/)を提供し、[ _Durable Objects_](https://developers.cloudflare.com/durable-objects/)はWebSocketsを管理し、リアルタイムの調整を処理します。何より素晴らしいのは、サーバーレスATProtoアプリケーションの構築に必要なものすべてが無料枠で利用できるため、追加費用なしで始められることです。コードは[ _こちらのGitHubリポジトリ_](https://github.com/inanna-malick/statusphere-serverless/tree/main)で確認できます。

## ATProtoエコシステム：簡単にご紹介します

まず、ATProtoエコシステムにおけるデータの流れの概念的な概要から始めましょう：

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2813 image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46959Z09VP70W37XYGZQ9B.png&w=715&h=757&f=webp&fit=cover&position=center)

ユーザーはアプリを操作し、アプリが個人[ _リポジトリ_](https://atproto.com/specs/repository)に更新を書き込みます。これらの更新が変更イベントをトリガーし、リレーに公開され、グローバルイベントストリームを通じて配信されます。元のアップデートを公開していないアプリでも、こうしたイベントに購読することができます。ATProtoでは、リポジトリ、リレー、アプリはすべて独立したコンポーネントであり、異なるオペレーターによって実行され得る（そして実行される）からです。

### ID

ユーザーIDは、[ _アカウント_](https://atproto.com/specs/handle)で始まり、`alice.example.com`のような人間が読める名前です。プロトコルがDNSを活用して、誰がどのアカウントを所有しているかというグローバルな可視性を提供できる、各ハンドリングは有効なドメイン名でなければなりません。ユーザーの[ _パーソナルデータサーバー（PDS）_](https://atproto.com/specs/account)の場所を含む、ユーザーの[ _分散型識別子（DID）_](https://atproto.com/specs/did)にマップを処理します。

### 認証

ユーザーのPDSは、キーとリポジトリを管理します。認証を処理し、リポジトリを通じてデータの権威あるビューを提供します。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2813 image 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45WQDKYGCNC503HBB26TKP.png&w=715&h=569&f=webp&fit=cover&position=center)

さらに詳しく知りたい方は、こちらの[ _分散システムエンジニア向けのATProtoの記事_](https://atproto.com/articles/atproto-for-distsys-engineers)をご覧ください。

ここでの違いは、そして見落とされやすい点は、このスタックのどの部分も単一のサービスの信頼に依存していることはほとんどないことです。DID解決は検証可能。PDSはユーザーが選択できます。クライアントアプリは単なるインターフェイスです。

データを公開したり取得したりする際には、署名と自己検証が行われます。つまり、他のアプリは、許可を求めることなく、また当社のバックエンドを信頼することなく、その上にすべての他のアプリを使用したり、その上に構築したりすることができます。

## 私たちのアプリケーションは、

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2813 image 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46WKR01SM8NXK4GANF3QZS.png&w=715&h=692&f=webp&fit=cover&position=center)

ATProtoチームが構築した小さいながらも完全なデモアプリ、[** _Statusphere_**](https://atproto.com/guides/applications)を使って作業します。これは可能な限りシンプルなソーシャルメディアアプリで、ユーザーは単一絵文字のステータス更新を投稿します。非常に最小限であるため、Statusphereは、分散型ATProtoアプリがどのように機能し、Cloudflareのサーバーレススタック上で動作するように適応させるかについて、最適な出発点となります。

### Statussphereスキーマ

ATProtoでは、すべてのリポジトリデータがJSON-Schemaに似た共有スキーマ言語であるLexiconを使用して型付けされます。Statusphereには、ATProtoチームが定義した`xyz.statusphere.status`レコードを使用します。
    
    
    {
      "type": "record",
      "key": "tid", # timestamp-based id
      "record": {
        "type": "object",
        "required": ["status", "createdAt"],
        "properties": {
          "status": { "type": "string", "maxGraphemes": 1 },
          "createdAt": { "type": "string", "format": "datetime" }
        }
      }
    }

辞書は厳密に型付けされているため、アプリ間の相互運用性が容易です。

## 構築の仕組み

このセクションでは、認証からリポジトリの読み込みおよび書き込み、リアルタイム更新まで、Statusphere内のデータの流れをたどり、サーバーレスインフラストラクチャ上でライブイベントストリームの処理方法を紹介します。

### 1\. 言語の選択

ATProtoのコアライブラリはTypeScriptで記述されており、Cloudflare WorkersはFirst-classのTypeScriptのサポートを提供します。Cloudflare Workers上にATProtoサービスを構築する際の自然な出発点となります。

ただし、ATProto TypeScriptライブラリは、[ _バックエンド_](https://www.npmjs.com/package/@atproto/oauth-client-node)または[ _ブラウザ_](https://www.npmjs.com/package/@atproto/oauth-client-browser)のコンテキストを想定しています。Cloudflare Workersはサーバーレスコンテキストで[ _Node.js APIの使用_](https://developers.cloudflare.com/workers/runtime-apis/nodejs/)をサポートしていますが、ATProtoライブラリの[ _使用_](https://github.com/bluesky-social/atproto/blob/f476003709d43b5e2474218cd48a9e1d7ebf3089/packages/internal/did-resolver/src/methods/plc.ts#L51)は、[ _「エラー」リダイレクト処理モード_](https://developer.mozilla.org/en-US/docs/Web/API/Request/redirect)の使用は、エッジランタイムと互換性がありません。

Cloudflareは、[ _WASM クロスコンピレーション_](https://developers.cloudflare.com/workers/runtime-apis/webassembly/)を介してWorkersのRustもサポートしているので、次にそれを試してみました。[ _ATProto Rust クレート_](https://github.com/atrium-rs/atrium)とコード生成ツールは、Rustの型システムを大いに活用し、ツールを構築しますが、まだ活発に開発中です。それでも、RustのWASMエコシステムは堅固であるので、[ _Statusphereの既存のRust実装_](https://github.com/fatfingers23/rusty_statusphere_example_app)を適応させることで、すぐに作業可能なプロトタイプを動作させることができました。（もともとBailey Townsendが書いたものです）。コードは、[ _このGitHub repo_](https://github.com/inanna-malick/statusphere-serverless/tree/main)でご覧いただけます。

Cloudflare Workers上にATProtoアプリを構築しているなら、TypeScriptライブラリに貢献して、サーバーレスランタイムのサポートを強化することをお勧めします。このアプリのTypeScriptバージョンは、素晴らしい次のステップになります。構築にご興味のある方は、[ _Cloudflare Developer Discordサーバー_](https://discord.com/invite/cloudflaredev)経由でご連絡ください。

### 2\. 追随する

この「Deploy to Cloudflare（Cloudflareにデプロイ）」ボタンを使用して、リポジトリを複製し、独自のKVおよびD1インスタンスとCIパイプラインを設定します。

[![Cloudflareへデプロイ](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https%3A%2F%2Fgithub.com%2Finanna-malick%2Fstatusphere-serverless%2Ftree%2Fmain%2Fworker)

このリンクの手順に従い、デフォルト値を使用するか、カスタム名を選択すると、独自のStatusphere Workerを構築し、デプロイします。

**注：このプロジェクトには、パブリックイベントストリームから読み取られるスケジュールコンポーネントが含まれています。リソースを節約するために、実験が終わったら削除するべきかもしれません。**

### 3\. ユーザーのハンドリングを解決する

ユーザーのデータとやりとりするには、まず、_atprotoサブドメインに登録されているレコードを使用して、DIDのハンドリングを解決します。例えば、私の処理は`inanna.recursion.wtf`で、そのため、私のDIDレコードは [`__atproto.inanna.recursion.wtf_`](https://digwebinterface.com/?hostnames=_atproto.inanna.recursion.wtf&type=TXT&ns=resolver&useresolver=1.1.1.1&nameservers=) に保存されます。そのレコードの値は、`d:plc:p2sm7vlwgcbbdjpfy6qajd4g` です。

次に、DIDを対応する[ _DIDドキュメント_](https://atproto.com/specs/did#did-documents)に解決します。DIDドキュメントには、ユーザーの個人データサーバーの場所を含むIDメタデータが含まれます。DID方法に応じて、この解決はDNS（dd:web識別子の場合）を介して直接処理され、より多くの場合、dod:plc識別子の場合は資格情報の公開台帳を介して処理されます。

これらの値は頻繁に変更されないため、[ _Cloudflare KV_](https://developers.cloudflare.com/kv/)を使用してキャッシュします。このような場合には、更新頻度は低いものの、低遅延でグローバルに利用できるようにする必要があるKey-Valueマッピングがある場合に最適です。

DIDドキュメントから、ユーザーの個人データサーバーの場所を抽出します。私の場合は、`bsky.social`で、独自のPDSをセルフホストしたり、別のプロバイダーを利用したりすることもあります。

OAuthフローの詳細についてはここでは重要ではありません。[ _私が実装に使用したコードを読む_](https://github.com/inanna-malick/statusphere-serverless/blob/main/worker/src/services/oauth.rs)ことも、[ _OAuthの仕様を掘り下げる_](https://datatracker.ietf.org/doc/html/rfc6749)こともできます。しかし、簡単に言うと、ユーザーはPDSを介してサインインし、署名鍵を使用して、アプリに代わって行動する許可を与えます。

[ _タワーセッション_](https://docs.rs/tower-sessions/latest/tower_sessions/#implementation)を使ってセキュアなセッションCookieにセッションデータを保持します。つまり、クライアント側では不透明なセッションIDのみが保存され、すべてのセッション/認証状態データはCloudflare KVに保存されます。このユースケースにも、自然に適合したと言えます。

### 4\. ステータスとプロファイルデータの取得

セッションCookieに保存されたDIDを使用して、ユーザーのOAuthセッションを復元し、[ _認証されたエージェントをスピンアップします_](https://github.com/inanna-malick/statusphere-serverless/blob/ca6e5ecd3a81dcfc80d9a9d976bac6efdad3a312/worker/src/frontend_worker/endpoints.rs#L111-L118)。
    
    
    let agent = state.oauth.restore_session(&did).await?;

エージェントの準備が完了すると、[ _ユーザーの最新のStatusphe投稿とBlueskyプロファイルを取得します_](https://github.com/inanna-malick/statusphere-serverless/blob/ca6e5ecd3a81dcfc80d9a9d976bac6efdad3a312/worker/src/frontend_worker/endpoints.rs#L120-L140)。
    
    
    let current_status = agent.current_status().await?;
    let profile = agent.bsky_profile().await?;

従業員のステータスとプロフィール情報が手元にあるので、[ _ホームページをレンダリング_](https://github.com/inanna-malick/statusphere-serverless/blob/ca6e5ecd3a81dcfc80d9a9d976bac6efdad3a312/worker/src/frontend_worker/endpoints.rs#L142-L150)できます：
    
    
    Ok(HomeTemplate {
        status_options: &STATUS_OPTIONS,
        profile: Some(Profile {
            did: did.to_string(),
            display_name: Some(username),
        }),
        my_status: current_status,
    })

### 5\. アップデートの公開

ユーザーが新しいe品ステータスを投稿すると、個人リポジトリに新しいレコードを作成します。データの取得に使用したのと同じ認証済みエージェントを使用します。今回は、読み取りの代わりに、[ _レコードの**作成操作** を実行_](https://github.com/inanna-malick/statusphere-serverless/blob/ca6e5ecd3a81dcfc80d9a9d976bac6efdad3a312/worker/src/frontend_worker/endpoints.rs#L183)します。
    
    
    let uri = agent.create_status(form.status.clone()).await?.uri;

この操作は、新しいレコードの正規の識別子であるURIを返します。

そして、ステータスアップデートをD1に書き、すぐにUIに反映できるようにします。

### 6\. Durable Objectsを使用して更新を送信

アクティブなホームページは全て、Durable ObjectへのWebSocket接続を維持し、Durable Objectは軽量のリアルタイムメッセージブローカーとして機能します。アイドル状態では、Durable Objectは[ _ハイバネーション_](https://developers.cloudflare.com/durable-objects/best-practices/websockets/#websocket-hibernation-api)し、WebSocket 接続を維持しながらリソースを節約します。Durable Objectにメッセージを送信して、[ _それを起動し、新しい更新をブロードキャストします_](https://github.com/inanna-malick/statusphere-serverless/blob/ca6e5ecd3a81dcfc80d9a9d976bac6efdad3a312/worker/src/frontend_worker/endpoints.rs#L192)。
    
    
    state.durable_object.broadcast(status).await?;

その後、Durable Objectが[ _接続されているすべてのホームページに新しい更新をブロードキャストします_](https://github.com/inanna-malick/statusphere-serverless/blob/ca6e5ecd3a81dcfc80d9a9d976bac6efdad3a312/worker/src/durable_object/server.rs#L88-L92)。
    
    
    for ws in self.state.get_websockets() {
        ws.send(&status);
    }

その後、すべてのライブWebSocketを反復処理して、更新を送信します。

実際の実用的注意点：Durable Objectsは**インスタンス間でシャーディングされた場合** にパフォーマンスが向上します。 簡単にするために、すべてが**1つのDurable Object** を介してすべてを実行するケースを説明しました。

それ以上の拡張のために、次のステップは、ロケーションヒントを用いて、サポートされているロケーションごとに複数のDurableObjectインスタンスを使用することで、世界中のユーザーの遅延を最小限に抑え、単一のロケーションに多数の同時ユーザーが発生した場合のボトルネックを回避することになります。最初はこのパターンの実装を検討しましたが、ATProtoの開発者がアプリのテンプレートとして使用できるような簡潔な「hello world」スタイルの例を作成するという私の目標と競合していました。

### 7.ライブ変化の変化に耳を傾ける

#### 課題：リアルタイムフィードとサーバーレス

自社のアプリ内で更新を公開するのは簡単ですが、ATProtoエコシステムでは、**他のアプリケーション** がユーザー向けにステータス更新を公開することが可能です。Statussphereを完全に統合したい場合は、これらのイベントも選択する必要があります。

ライブイベント更新のリッスンには、ATProto [_Jetstream_](https://github.com/bluesky-social/jetstream)サービスへのWebSocket接続が永続的に必要です。従来のサーバーベースのアプリは、WebSocket クライアントソケットを無期限に開いたままにすることができますが、サーバーレスプラットフォームはできません。Workersは永遠に実行できません。

ライブサーバーを実行せずに「リッスン」する方法が必要です。

#### ソリューション：Cloudflare Worker Cron Triggers

これを解決するために、私たちはリッスンロジックを[** _Cron Trigger_**](https://developers.cloudflare.com/workers/configuration/cron-triggers/)に移動しました。ライブソケットを開いておくのではなく、この機能を使用して、定期的なジョブを使用して、小さなバッチで更新を読み取ります。

スケジュールされたworker呼び出しが開始されると、永続ストレージから最後に確認されたカーソルがロードされます。次に、[ _接続_](https://github.com/inanna-malick/statusphere-serverless/blob/ca6e5ecd3a81dcfc80d9a9d976bac6efdad3a312/worker/src/services/jetstream.rs#L98-L101)して、[ _Jetstream_](https://github.com/bluesky-social/jetstream)（ATProtoレポジトリイベントのストリーミングサービス）に接続します。xyz.statusphere.statusコレクションでフィルタリングされ、最後に確認されたカーソルが始まります。
    
    
    let ws = WebSocket::connect("wss://jetstream1.us-east.bsky.network/subscribe?wantedCollections=xyz.statusphere.status&cursor={cursor}").await?;

**カーソル** （マイクロ秒のタイムスタンプ）をDurable Objectの永続ストレージに保存するため、オブジェクトが再起動しても、再開場所が正確に把握できます。開始時間より新しいイベントを処理するとすぐに、WebSocket 接続を閉じ、Durable Objectをスリープ状態に戻します。

トレードオフ：更新は最大で1分も遅れる可能性がありますが、システムは完全にサーバーレスのままです。これは、インフラストラクチャの複雑さを最小限に抑えることが、完璧なリアルタイム配信を実現することよりも重要な、初期段階のアプリやプロトタイプに最適です。

## オプションでアップグレード：リアルタイムイベントリスナー

リアルタイム更新が必要で、**サーバーレスモデルを少し変えたい** という場合は、JetstreamへのライブWebSocket接続を維持する軽量のリスナープロセスをデプロイできます。

このプロセスは、1分に1回ポーリングする代わりに、xyz.statusphere.statusコレクションの新しいイベントをリッスンし、到着するとすぐにCloudflare Workerに更新をプッシュします。このリスナープロセスのスケッチは[ _こちら_](https://github.com/inanna-malick/statusphere-serverless/tree/main/firehose_listener)と、それからの更新を処理するエンドポイントは[ _こちら_](https://github.com/inanna-malick/statusphere-serverless/blob/ca6e5ecd3a81dcfc80d9a9d976bac6efdad3a312/worker/src/frontend_worker/endpoints.rs#L211-L238)で確認できます。

結果は、依然として従来型のサーバーではありません。

  * Webへの公開禁止
  * 開いているHTTPポートなし
  * 永続的データベースなし



単一目的のステートレスリスナーであり、アプリが大きくなり、より深刻なインフラストラクチャが必要になるまで、ホームサーバーで実行するのに十分なシンプルなものです。

後で、[ _Cloudflare Queues_](https://developers.cloudflare.com/queues/)のようなツールを使用して、この設計をよりスケーラブルなものに置き換え、[ _バッチ処理や再試行_](https://developers.cloudflare.com/queues/configuration/batching-retries/)を提供できますが、小規模から中規模のアプリケーションでは、この軽量なリスナーが簡単で効果的なアップグレードです。

## 将来を見据える

現在、Durable Objectsは長期間のWebSocket**サーバー接続** を保持しながらハイバネーションすることができますが、長期間のWebSocket**クライアント接続** を保持する場合はハイバネーションをサポートしません（Jetstreamリスナーのように）。そのため、Statusphereでは、ネットワークと同期を維持するために、Cron Triggerを介したWorker呼び出しや軽量の外部リスナーを使用して回避策を講じています。

Durable Objectsに将来的な改善（アクティブなWebSocketクライアントのハイバネーションのサポートを追加するなど）を行うことで、こうした回避策の必要性を完全に排除する可能性があります。

## 独自のATProtoアプリを構築する

これは、サーバーゼロで運用コストを最小限に抑えながら、Cloudflareで完全に実行されるフル機能のatprotoアプリです。Workersはほとんどのユーザーから[ _50ミリ秒以内_](https://www.cloudflare.com/network/)でコードを実行し、KVとD1はデータの可用性を維持し、Durable ObjectsはWebSocketのファンアウトとライブ調整を処理します。

**Cloudflareにデプロイボタン** を使用して、[ _リポジトリ_](https://github.com/inanna-malick/statusphere-serverless/tree/main)を複製し、サーバーレス環境を設定します。そして、あなたが構築したものを私たちに見せてください。[ _当社のDiscord_](https://discord.com/invite/cloudflaredev)にリンクをドロップするか、Blueskyで[ _@cloudflare.social_](https://bsky.app/profile/cloudflare.social)またはXで[ _@CloudflareDev_](https://x.com/cloudflaredev)のタグを付けてください。ぜひご覧ください。

[![Cloudflareへデプロイ](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https%3A%2F%2Fgithub.com%2Finanna-malick%2Fstatusphere-serverless%2Ftree%2Fmain%2Fworker)

このページ

オンラインで議論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fserverless-atproto%2F&t=Serverless%20Statusphere%EF%BC%9ACloudflare%E3%81%AE%E9%96%8B%E7%99%BA%E8%80%85%E3%83%97%E3%83%A9%E3%83%83%E3%83%88%E3%83%95%E3%82%A9%E3%83%BC%E3%83%A0%E4%B8%8A%E3%81%A7%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC%E3%83%AC%E3%82%B9ATProto%E3%82%A2%E3%83%97%E3%83%AA%E3%82%B1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%82%92%E6%A7%8B%E7%AF%89%E3%81%99%E3%82%8B%E6%89%8B%E9%A0%86)[](https://x.com/intent/post?text=Serverless+Statusphere%EF%BC%9ACloudflare%E3%81%AE%E9%96%8B%E7%99%BA%E8%80%85%E3%83%97%E3%83%A9%E3%83%83%E3%83%88%E3%83%95%E3%82%A9%E3%83%BC%E3%83%A0%E4%B8%8A%E3%81%A7%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC%E3%83%AC%E3%82%B9ATProto%E3%82%A2%E3%83%97%E3%83%AA%E3%82%B1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%82%92%E6%A7%8B%E7%AF%89%E3%81%99%E3%82%8B%E6%89%8B%E9%A0%86&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fserverless-atproto%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fserverless-atproto%2F)[](https://bsky.app/intent/compose?text=Serverless+Statusphere%EF%BC%9ACloudflare%E3%81%AE%E9%96%8B%E7%99%BA%E8%80%85%E3%83%97%E3%83%A9%E3%83%83%E3%83%88%E3%83%95%E3%82%A9%E3%83%BC%E3%83%A0%E4%B8%8A%E3%81%A7%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC%E3%83%AC%E3%82%B9ATProto%E3%82%A2%E3%83%97%E3%83%AA%E3%82%B1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%82%92%E6%A7%8B%E7%AF%89%E3%81%99%E3%82%8B%E6%89%8B%E9%A0%86+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fserverless-atproto%2F)[](https://mastodonshare.com/?text=Serverless+Statusphere%EF%BC%9ACloudflare%E3%81%AE%E9%96%8B%E7%99%BA%E8%80%85%E3%83%97%E3%83%A9%E3%83%83%E3%83%88%E3%83%95%E3%82%A9%E3%83%BC%E3%83%A0%E4%B8%8A%E3%81%A7%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC%E3%83%AC%E3%82%B9ATProto%E3%82%A2%E3%83%97%E3%83%AA%E3%82%B1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%82%92%E6%A7%8B%E7%AF%89%E3%81%99%E3%82%8B%E6%89%8B%E9%A0%86&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fserverless-atproto%2F)[](https://www.threads.net/intent/post?text=Serverless+Statusphere%EF%BC%9ACloudflare%E3%81%AE%E9%96%8B%E7%99%BA%E8%80%85%E3%83%97%E3%83%A9%E3%83%83%E3%83%88%E3%83%95%E3%82%A9%E3%83%BC%E3%83%A0%E4%B8%8A%E3%81%A7%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC%E3%83%AC%E3%82%B9ATProto%E3%82%A2%E3%83%97%E3%83%AA%E3%82%B1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%82%92%E6%A7%8B%E7%AF%89%E3%81%99%E3%82%8B%E6%89%8B%E9%A0%86+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fserverless-atproto%2F)

## 関連するタグ

[Durable Objects](https://blog.cloudflare.com/ja-jp/tag/durable-objects/)[Rust](https://blog.cloudflare.com/ja-jp/tag/rust/)[Wrangler](https://blog.cloudflare.com/ja-jp/tag/wrangler/)

SNS をフォロー

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 新しい投稿のお知らせを受け取るように登録する

メールアドレス

また、あなたのメールアドレスを共有したりすることはございません。

登録する

ご購読ありがとうございます！受信箱を確認して登録してください。
