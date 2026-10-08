---
url: https://blog.cloudflare.com/ja-jp/python-workers-advancements/
title: Python Workers\u5197\u9577\u5316\uff1a\u9ad8\u901f\u30b3\u30fc\u30eb\u30c9\u30b9\u30bf\u30fc\u30c8\u3001\u30d1\u30c3\u30b1\u30fc\u30b8\u3001uv\u30d5\u30a1\u30fc\u30b9\u30c8\u30ef\u30fc\u30af\u30d5\u30ed\u30fc | Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:46:47.870335+00:00
---

# Python Workers冗長化：高速コールドスタート、パッケージ、uvファーストワークフロー | Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/python-workers-advancements/

[ブログ](https://blog.cloudflare.com/ja-jp/)

[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[Python](https://blog.cloudflare.com/ja-jp/tag/python/)

2 タグタグを2件表示

  * 投稿タグ
  * [Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[Python](https://blog.cloudflare.com/ja-jp/tag/python/)
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



[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[Python](https://blog.cloudflare.com/ja-jp/tag/python/)

2025年12月8日

# Python Workers再考：高速コールドスタート、パッケージ、およびuvファーストなワークフロー

![Dominik Picheta](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46P5G8RRA9GKFZA6BYERZ1.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Hood Chatham](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DGCR56ZBCN9NTBRE18MF.webp&w=64&h=64&f=webp&fit=cover&position=center)![Mike Nomitch](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW462B7XNRB3FQ030XK95Y0H.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Dominik Picheta](https://blog.cloudflare.com/ja-jp/author/dominik/)、[Hood Chatham](https://blog.cloudflare.com/ja-jp/author/hood/)、[Mike Nomitch](https://blog.cloudflare.com/ja-jp/author/mike-nomitch/)

16分で読了

URLをコピー

この記事は以下でも利用可能です [English](https://blog.cloudflare.com/python-workers-advancements/)、[한국어](https://blog.cloudflare.com/ko-kr/python-workers-advancements/)、[繁體中文](https://blog.cloudflare.com/zh-tw/python-workers-advancements/)、[简体中文](https://blog.cloudflare.com/zh-cn/python-workers-advancements/).

![BLOG-2925 Hero Image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46SJ3N46YQKDZYJ6Q7M0S4.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///////97e/z3eLu2+Lx4+n26+3y7uvp////////6u3119/w1eD04Oj56e317evs////////6O3509710eD53un96e/67e3w////////6/D+1eL61OT+4e7/7fP/8fH1////////8/j/3+v/3u3/6/b/9fn/9/b7/////////f//7fb/7fj/9/7//v////3/////////////+P//+P///////////////////////////P///P//////////////)

_このコンテンツは自動機械翻訳サービスによる翻訳版であり、皆さまの便宜のために提供しています。原本の英語版と異なる誤り、省略、解釈の微妙な違いが含まれる場合があります。ご不明な点がある場合は、英語版原本をご確認ください。_

 _注：この投稿は、AWS Lambdaに関する追加の詳細で更新されました。_

昨年、当社は[ _Python Workersの基本的なサポート_](https://blog.cloudflare.com/python-workers/)を発表しました。これにより、Python開発者は単一のコマンドでPythonを地球全体に配信し、[ _Workersプラットフォーム_](https://workers.cloudflare.com/)を活用できるようになります。

それ以来、私たちは[ _WorkersでのPython体験を素晴らしいものにする_](https://developers.cloudflare.com/workers/languages/python/)ことに懸命に取り組んできました。当社は、パッケージサポートをプラットフォームにもたらすことに注力し、超高速コールドスタートとPythonネイティブの開発者体験を実現しました。

これは、パッケージがPython Workerに組み込まれる方法の変更を意味します。限られた組み込みパッケージのセットを提供する代わりに、Python Workersを支えるWebAssemblyランタイムである[ _Pyodideがサポート_](https://pyodide.org/en/stable/usage/packages-in-pyodide.html)する任意のパッケージをサポートするようになりました。これには、すべての純粋なPythonパッケージと、動的ライブラリに依存する多くのパッケージが含まれます。また、パッケージのインストールを簡単にするために、[ _uv_](https://docs.astral.sh/uv/) 関連のツールも構築しました。

また、コールドスタート時間を短縮するために、専用のメモリスナップショットを実装しました。これらのスナップショットは、他のサーバーレスPythonベンダーよりも大幅な速度向上をもたらします。一般的なパッケージを使用したコールドスタートテストでは、Cloudflare Workersは、**SnapStartを使用しない** AWS **Lambdaよりも2.4倍以上** 、Googleクラウド**Runよりも3倍速く起動します** 。

このブログ記事では、Python Workersの独自性とは何かを説明し、上述の成功をどのように実現したかについての技術的な詳細をご紹介します。しかし、まず、Workersやサーバーレスプラットフォームをよく知らない人、特にPythonのバックグラウンドを持つ人のために、Workersを使いたいと思う理由を共有しましょう。

### Pythonを2分間でグローバルにデプロイ

Workersの魔法の一部として、シンプルなコードと簡単なグローバルデプロイメントがあります。まず、2分以内の高速コールドスタートで、FastAPIアプリを世界中にデプロイする方法を示します。

FastAPIを使用した単純なWorkerは、いくつかの行で実装できます。
    
    
    from fastapi import FastAPI
    from workers import WorkerEntrypoint
    import asgi
    
    app = FastAPI()
    
    @app.get("/")
    async def root():
       return {"message": "This is FastAPI on Workers"}
    
    class Default(WorkerEntrypoint):
       async def fetch(self, request):
           return await asgi.fetch(app, request.js_object, self.env)

同様のことをデプロイするには、`uv`と`npm`がインストールされていることを確認してから、以下を実行してください。
    
    
    $ uv tool install workers-py
    $ pywrangler init --template \
        https://github.com/cloudflare/python-workers-examples/03-fastapi
    $ pywrangler deploy

ほんの少しのコードとPythonでのデプロイで、[ _125か国、330か所に広がる_](https://www.cloudflare.com/network/)Cloudflareのエッジネットワーク全体にアプリケーションを`デプロイ`できました。インフラストラクチャやスケーリングを心配する必要はありません。

また、多くの場合、Python Workersは完全に無料です。当社の無料枠では、1日あたりリクエスト100,000件、呼び出し1回あたりのCPU時間10ミリ秒を保証しています。詳しくは、[ _当社のドキュメントで価格設定_](https://developers.cloudflare.com/workers/platform/pricing/)をご覧ください。

その他の例については、[ _GitHubのリポジトリをご覧ください_](https://github.com/cloudflare/python-workers-examples)。Python Workersの詳細について、さらにお読みください。

### では、Python Workersでは何ができるのでしょうか。

Workerを手に入れたら、どんなことも可能になります。コードを書くから、決定を決められます。Python WorkerはHTTPリクエストを受信し、パブリックインターネット上の任意のサーバーにリクエストを行うことができます。

Cronトリガーを設定できるため、Workerが定期的に実行されます。さらに、より複雑な要件がある場合は、[ _Python Workers用Workflows_](https://blog.cloudflare.com/python-workflows/)を使用することも、[ _Durable Objectsを使用_](https://developers.cloudflare.com/durable-objects/get-started/)して長期間実行されているWebSocketサーバーやクライアントでも使用することができます。

以下では、Python Workersを使用してできることの追加の例を紹介します。

  * [ _サーバーから直接動的コンテンツをフェッチしながら、Jinjaのようなライブラリを使ってエッジでHTMLテンプレートをレンダリングします。_](https://github.com/cloudflare/python-workers-examples/tree/main/03-fastapi)
  * [ _サーバーからのレスポンスを変更する。たとえば、リクエストされたコンテンツに応じて、opengraphタグをHTMLに動的に挿入することができます。_](https://github.com/cloudflare/python-workers-examples/tree/main/11-opengraph)
  * [ _Durable ObjectsとWebSocketsを使用してチャットルームを構築する_](https://github.com/cloudflare/python-workers-examples/tree/main/15-chatroom)
  * [ _Bluesky消火栓などのWebSocket接続からデータを消費_](https://github.com/cloudflare/python-workers-examples/tree/main/14-websocket-stream-consumer)
  * [ _Pillow Pythonパッケージを使用した画像の生成_](https://github.com/cloudflare/python-workers-examples/tree/main/12-image-gen)
  * [ _PythonパッケージのAPIを公開する小さなPython Workerを書き、RPCを使ってJavaScript Workerからアクセスする_](https://github.com/cloudflare/python-workers-examples/tree/main/13-js-api-pygments)



### パッケージのコールドスタートの高速化

Workersのようなサーバーレスプラットフォームは、必要な時だけコードを実行することで、コストを節約します。つまり、Workerがリクエストを受信しない場合、Workerはシャットダウンされる可能性があり、新しいリクエストが入ってくると、再起動する必要があります。これは通常、「コールドスタート」と呼ばれるリソースのオーバーヘッドが発生します。エンドユーザーの遅延を最小限に抑えるためには、これらをできるだけ短くすることが重要です。

標準的なPythonでは、ランタイムの起動にコストがかかるため、Python Workersの初期実装は、 _ランタイム_ の起動を高速化することに重点を置きました。しかし、これだけでは不十分であることにすぐに気付きました。Pythonランタイムがすばやく起動したとしても、現実世界のシナリオでは、通常、初期起動はパッケージからのモジュールの読み込みを含むのが通常で、残念ながら、Pythonでは多くの人気のあるパッケージは読み込みに数秒かかることがあります。

私たちは、パッケージが読み込まれているかどうかに関係なく、コールドスタートを高速化することにしました。

現実的なコールドスタートパフォーマンスを測定するために、一般的なパッケージをインポートするベンチマークと、ベアPythonランタイムを使用して「hello world」を実行するベンチマークを設定しました。Standard Lambdaは[ _ランタイムだけを素早く起動する_](https://cold.picheta.me/#bare)ことができますが、パッケージをインポートする必要があると、コールドスタート時間が長くなります。パッケージでのより速いコールドスタートを最適化するには、LambdaでSnapStartを使用することができます（間もなくリンクされたベンチマークに追加されます）。これには、スナップショットの保存コストと、復元のたびに追加のコストが発生します。Python Workersは、すべてのPython Workerに無料でメモリスナップショットを自動的に適用します。

3つの一般的なパッケージ（[ _httpx_](https://www.python-httpx.org/)、[ _fastapi_](https://fastapi.tiangolo.com/)、[ _pydantic_](https://docs.pydantic.dev/latest/)）を読み込む際の平均コールドスタート時間は以下の通りです。

プラットフォーム| 平均コールドスタート（秒）  
---|---  
Cloudflare Python Workers| 1.027  
AWS Lambda（SnapStartなし）| 2.502  
Google クラウド Run| 3.069  
  
この場合、**Cloudflare Python Workersは、SnapStartを使用しないAWS Lambdaよりも2.4倍、Google Cloud Runよりも3倍速いコールドスタートを実現しています。** この低いコールドスタート数は、メモリスナップショットを使用することで実現しました。後のセクションではその方法について説明します。

これらのベンチマークは定期的に実行しています。当社のテスト方法に関する最新のデータや詳細情報は、[ _こちら_](https://cold.picheta.me/#bare)からご覧いただけます。

当社はアーキテクチャ的に他のプラットフォームと異なります。つまり、[ _Workersは分離ベース_](https://developers.cloudflare.com/workers/reference/how-workers-works/)です。そのため、私たちの目標は高いものであり、ゼロコールドスタートの未来に向けて計画を立てています。

### パッケージツールをuvと統合

多様なパッケージエコシステムは、Pythonを素晴らしいものにしている理由の大部分です。そのため、Workersでパッケージをできるだけ簡単に使用できるように懸命に取り組んできました。

私たちは、既存のPythonツールと連携することが、優れた開発体験を実現するための最善の方法であると考えました。そこで私たちは、高速で成熟し、Pythonエコシステムで勢いを増している`uv`パッケージとプロジェクトマネージャーを選びました。

Cloudflareは、[ _pywrangler_](https://github.com/cloudflare/workers-py#pywrangler)と呼ばれる`uv`を中心とした独自のツールを構築しました。このツールは、基本的に次のアクションを実行します。

  * Workerのpyproject.tomlファイルを読み込んで、そのファイルで指定された依存関係を判断する
  * Workerにある`python_modules`フォルダーに依存関係を含める



Pywranglerは`uv`に呼び出して、Python Workersと互換性のある方法で依存関係をインストールし、ローカル開発やWorkersをデプロイする際には`wrangler`に呼び出します。

実際は、`pywrangler dev`と`pywrangler` `deploy`を実行して、Workerをローカルでテストし、デプロイするだけでいいのです。

### タイプのヒント

pywrangler型を使って、Wrangler設定で定義されたすべての[ _バインディング_](https://developers.cloudflare.com/workers/runtime-apis/bindings/)に対し、`型ヒント`を生成することができます。これらの型ヒントは、[ _Pylance_](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)または[ _mypy_](https://mypy-lang.org/)の最新バージョンで動作します。

型を生成するには、[ _wrangler types_](https://developers.cloudflare.com/workers/wrangler/commands/#types)を使用してTypescriptの型ヒントを作成し、次にTypescriptコンパイラを使用して、型の抽象構文ツリーを生成します。最後に、JSオブジェクトに反復子フィールドがあるかどうかなど、TypeScriptのヒントを使用して、Pyodide外部関数インタフェースで動作する`mypy`型ヒントを生成します。

### スナップショットを使ったコールドスタート時間の短縮

Pythonの起動は一般的に非常に遅く、Pythonモジュールのインポートは大量の作業をトリガーする可能性があります。メモリスナップショットを使って、コールドスタート中のPython起動実行を回避します。

Workerがデプロイされると、Workerのトップレベルスコープが実行され、メモリスナップショットが作成され、Workerと一緒に保存されます。Workerの新しい分離を開始するたびに、メモリスナップショットを復元し、Workerはリクエストを処理する準備ができており、準備としてPythonコードを実行する必要はありません。これにより、コールドスタート時間が大幅に改善されます。たとえば、スナップショットなしで、`fastapi`、`httpx`、`pydantic`をインポートするWorkerを起動するには、約10秒かかります。スナップショットの場合、1秒で完了します。

PyodideがWebAssembly上に構築されているという事実、それを可能にしています。ランタイムの線形メモリをすべてキャプチャし、復元することができます。

#### メモリスナップショットとエントロピー

WebAssemblyランタイムは、セキュリティのためにアドレス空間レイアウトのランダム化などの機能を必要としないため、最新のオペレーティングシステムでは、メモリスナップショットの問題のほとんどは発生しません。ネイティブメモリスナップショットと同様に、[ _XKCD乱数ジェネレーター_](https://xkcd.com/221/)の使用を避けるために、起動時にエントロピーの処理に慎重に注意する必要があります（私たちは[ _実際のランダム性に大きな関心を持っています_](https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/)）。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2925 Image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW459DS22T0KYDPDJGGEAW3H.png&w=400&h=144&f=webp&fit=cover&position=center)

メモリのスナップショットを作成することで、ランダム性のためにシード値を誤ってロックしてしまうかもしれません。この場合、将来の「ランダム」数字の呼び出しは、多くのリクエストで一貫して同じ値のシーケンスを返すことになります。

Pythonは起動時に多くのエントロピーを使用するため、これを回避することは特に困難です。これには、libc関数`getentropy()`と`getrandom()`、および`/dev/random`と`/dev/urandom`からの読み取りが含まれます。これらの関数はすべて、JavaScript `crypto.getRandomValues()` 関数に関して同じ実装を共有しています。

Cloudflare Workersでは、`crypto.getRandomValues()`将来的にメモリスナップショットの使用に切り替えることができるように、起動時に常に無効になっています。残念ながら、Pythonインタプリタはこの関数を呼び出さず、ブートストラップができません。また、多くのパッケージは起動時にエントロピーを必要とします。このエントロピーには、大きく分けて2つの目的があります。

  * ハッシュランダム化用のハッシュシード
  * 擬似乱数発生器用シード



ハッシュのランダム化は起動時に行い、各Workerが固定のハッシュシードを持つコストを受け入れます。Pythonには、起動後にハッシュシードを交換できる仕組みがありません。

擬似乱数発生器（PRNG）に対して、当社は次のアプローチをとっています。

デプロイ時：

  1. PRNGに固定の「ポイズニングシード」をシードし、PRNGの状態を記録します。
  2. PRNGを呼び出すすべてのAPIを、ユーザーエラーでデプロイに失敗するオーバーレイに置き換える。
  3. ユーザーコードのトップレベルスコープを実行する。
  4. スナップショットをキャプチャする。



実行時：

  1. PRNGの状態が変更されていないことを保証します。変更していただければ、何らかのメソッドのためのオーバーレイを忘れていました。内部エラーにより、デプロイに失敗する。
  2. スナップショットを復元したら、ハンドラーを実行する前に乱数ジェネレーターを再シードします。



これにより、Workerの実行中にPRNGを使用できるようにしますが、初期化とプリスナップショットの実行中はWorkersがPRNGを使用しないようにできます。

#### メモリスナップショットとWebAssemblyの状態

WebAssembly上でメモリスナップショットを作成するときに、さらなる困難が発生します。保存しているメモリスナップショットは、WebAssemblyリニアメモリのみで構成されていますが、Pyodide WebAssemblyインスタンスの完全な状態はリニアメモリに含まれていません。

このメモリの外側には2つのテーブルがあります。

1つのテーブルが関数ポインタの値を保持します。従来のコンピュータは「Von Neumann」アーキテクチャを使用しています。つまり、コードはデータと同じメモリ空間に存在するため、関数ポインタを呼び出すことは、何らかのメモリアドレスにジャンプすることになります。WebAssemblyには、コードが別のアドレス空間に存在する「ハーバードアーキテクチャ」があります。これは、WebAssemblyのセキュリティ保証のほとんどにおいて重要なことであり、特にWebAssemblyがアドレス空間レイアウトのランダム化を必要としない理由です。WebAssemblyの関数ポインタは、関数ポインタテーブルへのインデックスです。

2番目のテーブルは、Pythonから参照されるすべてのJavaScriptオブジェクトを保持します。JavaScript仮想マシンはJavaScriptオブジェクトへのポインタを直接取得することを禁止しているため、JavaScriptオブジェクトをメモリに直接保存することはできません。その代わり、それらはテーブルに格納され、WebAssemblyでテーブルのインデックスとして表現されます。

スナップショットを復元した後のこれらのテーブルの両方が、スナップショットを取得したときとまったく同じ状態になっていることを確認する必要があります。

WebAssemblyインスタンスが初期化されるとき、関数ポインタテーブルは常に同じ状態にあり、動的ライブラリ（numpyのようなネイティブPythonパッケージ）を読み込むときに動的ローダーによって更新されます。

動的読み込みを処理するには：

  1. スナップショットを取得するときに、ローダーにパッチを適用して、動的ライブラリの読み込み順、各ライブラリのメタデータが割り当てられるメモリ内のアドレス、および再配置用の関数ポインタテーブルのベースアドレスを記録します。
  2. スナップショットを復元するとき、同じ順序で動的ライブラリを再ロードし、パッチを適用したメモリアロケーターを使用して、メタデータを同じ場所に配置します。関数ポインタテーブルの現在のサイズが、動的ライブラリに対して記録した関数ポインタテーブルベースと一致することを保証します。



これにより、スナップショットを復元した後も、各関数のポインターが、スナップショット取得時と同じ意味を持つことが保証されます。

JavaScriptの参照を処理するために、かなり限定的なシステムを実装しました。JavaScriptオブジェクトがグローバルからアクセス可能な場合は、一連のプロパティアクセスによって、それらのプロパティアクセスを記録し、スナップショットを復元する時に再生します。この方法でアクセスできないJavaScriptオブジェクトへの参照が存在する場合、Workerのデプロイに失敗します。これは、Pyodideサポートを持つすべての既存のPythonパッケージを扱うのに十分です。Pyodideは、次のようなトップレベルのインポートを行います。
    
    
    from js import fetch

### シャーディングによるコールドスタートの頻度の低減

Python Workersのパフォーマンス戦略におけるもう1つの重要な特徴は、シャーディングです。実装の経緯については、[ _こちら_](https://blog.cloudflare.com/eliminating-cold-starts-2-shard-and-conquer/)に詳しく説明されています。簡単に言うと、以前は新しいインスタンスを開始することを選択していたかもしれませんが、既存のWorkerインスタンスにリクエストをルーティングするようになりました。

シャーディングは実際にPython Workersで最初に有効になり、そのための素晴らしいテスト層であることが証明されました。PythonではJavaScriptよりもコールドスタートがはるかにコスト高になるため、リクエストが既に実行中の分離にルーティングされるようにすることが特に重要です。

### ここからどこにいくのか？

これは始まりにすぎません。Python Workersをより良くするための計画はたくさんあります：

  * 開発者が使いやすいツール
  * 分離アーキテクチャを活用して、コールドスタートをさらに高速化
  * より多くのパッケージをサポート
  * ネイティブTCPソケット、ネイティブWebSockets、より多くのバインディングをサポート



Python Workersの詳細については、[ _こちら_](https://developers.cloudflare.com/workers/languages/python/)からドキュメントをご覧ください。サポートが必要な場合は、ぜひ[ _Discord_](https://discord.cloudflare.com/)に参加してください。

このページ

オンラインで議論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fpython-workers-advancements%2F&t=Python%20Workers%E5%86%8D%E8%80%83%EF%BC%9A%E9%AB%98%E9%80%9F%E3%82%B3%E3%83%BC%E3%83%AB%E3%83%89%E3%82%B9%E3%82%BF%E3%83%BC%E3%83%88%E3%80%81%E3%83%91%E3%83%83%E3%82%B1%E3%83%BC%E3%82%B8%E3%80%81%E3%81%8A%E3%82%88%E3%81%B3uv%E3%83%95%E3%82%A1%E3%83%BC%E3%82%B9%E3%83%88%E3%81%AA%E3%83%AF%E3%83%BC%E3%82%AF%E3%83%95%E3%83%AD%E3%83%BC)[](https://x.com/intent/post?text=Python+Workers%E5%86%8D%E8%80%83%EF%BC%9A%E9%AB%98%E9%80%9F%E3%82%B3%E3%83%BC%E3%83%AB%E3%83%89%E3%82%B9%E3%82%BF%E3%83%BC%E3%83%88%E3%80%81%E3%83%91%E3%83%83%E3%82%B1%E3%83%BC%E3%82%B8%E3%80%81%E3%81%8A%E3%82%88%E3%81%B3uv%E3%83%95%E3%82%A1%E3%83%BC%E3%82%B9%E3%83%88%E3%81%AA%E3%83%AF%E3%83%BC%E3%82%AF%E3%83%95%E3%83%AD%E3%83%BC&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fpython-workers-advancements%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fpython-workers-advancements%2F)[](https://bsky.app/intent/compose?text=Python+Workers%E5%86%8D%E8%80%83%EF%BC%9A%E9%AB%98%E9%80%9F%E3%82%B3%E3%83%BC%E3%83%AB%E3%83%89%E3%82%B9%E3%82%BF%E3%83%BC%E3%83%88%E3%80%81%E3%83%91%E3%83%83%E3%82%B1%E3%83%BC%E3%82%B8%E3%80%81%E3%81%8A%E3%82%88%E3%81%B3uv%E3%83%95%E3%82%A1%E3%83%BC%E3%82%B9%E3%83%88%E3%81%AA%E3%83%AF%E3%83%BC%E3%82%AF%E3%83%95%E3%83%AD%E3%83%BC+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fpython-workers-advancements%2F)[](https://mastodonshare.com/?text=Python+Workers%E5%86%8D%E8%80%83%EF%BC%9A%E9%AB%98%E9%80%9F%E3%82%B3%E3%83%BC%E3%83%AB%E3%83%89%E3%82%B9%E3%82%BF%E3%83%BC%E3%83%88%E3%80%81%E3%83%91%E3%83%83%E3%82%B1%E3%83%BC%E3%82%B8%E3%80%81%E3%81%8A%E3%82%88%E3%81%B3uv%E3%83%95%E3%82%A1%E3%83%BC%E3%82%B9%E3%83%88%E3%81%AA%E3%83%AF%E3%83%BC%E3%82%AF%E3%83%95%E3%83%AD%E3%83%BC&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fpython-workers-advancements%2F)[](https://www.threads.net/intent/post?text=Python+Workers%E5%86%8D%E8%80%83%EF%BC%9A%E9%AB%98%E9%80%9F%E3%82%B3%E3%83%BC%E3%83%AB%E3%83%89%E3%82%B9%E3%82%BF%E3%83%BC%E3%83%88%E3%80%81%E3%83%91%E3%83%83%E3%82%B1%E3%83%BC%E3%82%B8%E3%80%81%E3%81%8A%E3%82%88%E3%81%B3uv%E3%83%95%E3%82%A1%E3%83%BC%E3%82%B9%E3%83%88%E3%81%AA%E3%83%AF%E3%83%BC%E3%82%AF%E3%83%95%E3%83%AD%E3%83%BC+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fpython-workers-advancements%2F)

## 関連するタグ

[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[Python](https://blog.cloudflare.com/ja-jp/tag/python/)

SNS をフォロー

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 新しい投稿のお知らせを受け取るように登録する

メールアドレス

また、あなたのメールアドレスを共有したりすることはございません。

登録する

ご購読ありがとうございます！受信箱を確認して登録してください。
