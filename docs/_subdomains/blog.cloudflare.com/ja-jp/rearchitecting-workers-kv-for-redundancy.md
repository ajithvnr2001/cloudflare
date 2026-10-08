---
url: https://blog.cloudflare.com/ja-jp/rearchitecting-workers-kv-for-redundancy/
title: Workers KV\u3092\u518d\u8a2d\u8a08\u3057\u3001\u53ef\u7528\u6027\u3068\u30d1\u30d5\u30a9\u30fc\u30de\u30f3\u30b9\u3092\u9ad8\u901f\u5316 | Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:49:59.047718+00:00
---

# Workers KVを再設計し、可用性とパフォーマンスを高速化 | Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/rearchitecting-workers-kv-for-redundancy/

[ブログ](https://blog.cloudflare.com/ja-jp/)

[Cloudflare Workers KV](https://blog.cloudflare.com/ja-jp/tag/cloudflare-workers-kv/)[事後検証](https://blog.cloudflare.com/ja-jp/tag/post-mortem/)

2 タグタグを2件表示

  * 投稿タグ
  * [Cloudflare Workers KV](https://blog.cloudflare.com/ja-jp/tag/cloudflare-workers-kv/)[事後検証](https://blog.cloudflare.com/ja-jp/tag/post-mortem/)
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



[Cloudflare Workers KV](https://blog.cloudflare.com/ja-jp/tag/cloudflare-workers-kv/)[事後検証](https://blog.cloudflare.com/ja-jp/tag/post-mortem/)

2025年8月8日

# Workers KVを再設計し、可用性とパフォーマンスを高速化

![Alex Robinson](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW479T0YHMKPZQQ2VAYMDQ3A.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Tyson Trautmann](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49JRJ6AFZ9F9S4V69Z9MFD.png&w=64&h=64&f=webp&fit=cover&position=center)

[Alex Robinson](https://blog.cloudflare.com/ja-jp/author/alex-robinson/)、[Tyson Trautmann](https://blog.cloudflare.com/ja-jp/author/tyson-trautmann/)

24分で読了

URLをコピー

この記事は以下でも利用可能です [English](https://blog.cloudflare.com/rearchitecting-workers-kv-for-redundancy/)、[简体中文](https://blog.cloudflare.com/zh-cn/rearchitecting-workers-kv-for-redundancy/).

![BLOG-2880 Hero Image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46AZKR183RVBSR2QYVMMKV.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA//////787/Dx4ubs4ufu6ezy7u/w7uzq//////7+7O3z3eDs2+Du5Ojz7O3y7u3s////////6+z12Nzt1tvv4OT16+z18O7w////////7u/52t3x19zz4ub57u/68/L1////////9fX+4ub24OX46+/+9fb/+fj6/////////f7/7vH87fL+9/r//v////7+////////////+Pv/+P3//////////////////////////P///f//////////////)

_このコンテンツは自動機械翻訳サービスによる翻訳版であり、皆さまの便宜のために提供しています。原本の英語版と異なる誤り、省略、解釈の微妙な違いが含まれる場合があります。ご不明な点がある場合は、英語版原本をご確認ください。_

2025年6月12日、Cloudflareでは大規模なサービス障害が発生し、重要なサービスの大規模なサービスに影響が出ました。[ _このインシデントに関するブログ記事_](https://blog.cloudflare.com/cloudflare-service-outage-june-12-2025/)で説明した通り、原因はWorkers KVサービスが使用している基盤となるストレージインフラストラクチャの障害でした。Workers KVは、多くのお客様から信頼されているだけでなく、他の多くのCloudflare製品の重要なインフラストラクチャとして機能し、影響を受けるサービス全体の設定、認証、アセット配信を処理しています。このインフラストラクチャの一部は、サードパーティのクラウドプロバイダーによって支えられており、6月12日に障害が発生し、KVサービスの可用性に直接影響がありました。

本日、同様の障害が再び発生しないように、Workers KVに行われた改善の最新情報を提供します。現在、すべてのデータを自社のインフラに保存しています。また、冗長性のために使用されるサードパーティのクラウドプロバイダーに加え、自社インフラストラクチャからのすべてのリクエストに対応し、高可用性を確保し、単一障害点を排除しています。最後に、パフォーマンスが有意義に改善され、冗長なバックアップとしてサードパーティプロバイダーに依存することを排除するための明確な道筋が示されました。

## 背景：オリジナルアーキテクチャ

Workers KVは、低遅延で大量の読み取りをサポートするグローバルなキーバリューストアです。水面下では、このサービスはデータを地域ストレージに保存し、Cloudflareのネットワーク全体でデータをキャッシュすることで優れた読み取りパフォーマンスを提供し、世界中で瞬時に利用できる必要のある設定データ、静的アセット、ユーザープリファレンスに最適です。

Workers KVは2018年9月にリリースされ、Durable ObjectsやR2などのCloudflareネイティブストレージサービスに先んじています。その結果、Workers KVの当初の設計では、複数のサードパーティクラウドサービスプロバイダーが提供するオブジェクトストレージを活用し、プロバイダーの冗長性によって可用性を最大化しました。このシステムはアクティブ-アクティブ構成で稼働し、プロバイダーの1つが利用できなくなったり、エラーが発生したり、パフォーマンスが低下したりする場合でも、リクエストに正常に対応していました。

Workers KVへのリクエストは、Cloudflare Workers上で動作するサービスであるStorage Gateway Worker（SGW）によって処理されていました。書き込みリクエストを受信すると、SGWはキーバリューペアを2つの異なるサードパーティオブジェクトストレージプロバイダーに同時に書き込み、複数の独立したソースからデータが常に利用できるようにします。削除も同様に処理され、オブジェクトの代わりに特別なtombstone値を書き込んでキーを削除済みとしてマークし、これらのtombstoneのガベージは後で収集されました。

Workers KVからの読み取りは通常、Cloudflareのキャッシュから提供でき、信頼性の高い低遅延を実現します。キャッシュにないデータの読み取りの場合、システムは両方のプロバイダーとリクエストを競合し、最初に到着した応答（通常は地理的に近いプロバイダーから）を返します。このレースアプローチは、プロバイダーの問題に対するレジリエンスを提供しながら、常に最速の応答を取ることで、読み取り遅延を最適化します。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2880 Image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46GEZ8SPK7ZX2PMRBEH9NF.png&w=715&h=644&f=webp&fit=cover&position=center)

独立したストレージプロバイダー2社を同期させることの難しさから、このアーキテクチャには、バックエンド間のデータの一貫性の問題に対処するための高度なマシンが含まれていました。このようなマシンにもかかわらず、一貫性のあるエッジケースは依然として、コンシューマーの必要性よりも頻繁に起こるものでした。これは、アップストリームのオブジェクトストレージシステムの可用性が本質的に完璧ではないことと、独立プロバイダー間で完全な同期を維持することの課題が原因でした。

長年にわたりシステムの実装は大幅に進化し、[ _昨年お話したさまざまなパフォーマンス改善_](https://blog.cloudflare.com/faster-workers-kv/)も見られましたが、基本的なデュアルプロバイダーアーキテクチャは変わりませんでした。これにより、Workers KVの利用が大幅に増加したための信頼できる基盤となり、グローバルアプリケーションにとって価値のあるパフォーマンス特性が維持されていました。

## スケーリングの課題とアーキテクチャ上のトレードオフ

Workers KVの利用が劇的に拡大し、アクセスパターンが多様化するにつれ、デュアルプロバイダーアーキテクチャは運用上の課題が増大しています。プロバイダーは根本的に異なる制限、障害モード、API、運用手順を持ち、常に適応する必要がありました。

スケーリングの問題は、プロバイダーの信頼性にとどまりませんでした。KVトラフィックが増加すると、IOPSの総数がローカルキャッシュインフラストラクチャに書き込みできる数を超え、データがオリジンストレージからフェッチされる際に従来のキャッシングアプローチに頼らざるを得なくなりました。この変化により、キャッシングの動作が予測しにくく、アップストリームプロバイダーのパフォーマンス特性に依存するようになったため、これまで小規模な規模では見られなかった整合性エッジケースが追加されることになりました。

最終的に、一貫性の問題、プロバイダーの信頼性の格差、運用上のオーバーヘッドの組み合わせから、今年初めに単一のオブジェクトストレージプロバイダーに移行して複雑さを軽減するという戦略的な決定につながりました。この決定は、リスクプロファイルの増加を認識して行われましたが、運用上のメリットがリスクを上回ると考えたため、これは独自のストレージインフラストラクチャを開発するまでの一時的な中間状態と見なしていました。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2880 Image 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW487STDNJZX5XSNYK30FGG9.png&w=715&h=644&f=webp&fit=cover&position=center)

残念ながら、2025年6月12日、残りの第三者クラウドプロバイダーが世界的な障害を経験したことでそのリスクが表面化し、2時間以上にわたりWorkers KVリクエストの大部分が失敗しました。お客様や他のCloudflareサービスへの連鎖的な影響は深刻でした。AccessはすべてのIDベースのログインに失敗し、Gatewayプロキシが利用できなくなり、WARPクライアントは接続できず、その他数十のサービスで大きな障害が発生しました。

## ソリューションの設計

インシデント発生後の直接の目標は、少なくとも1つを完全に冗長化したプロバイダーをオンラインにすることで、別の単一プロバイダーの障害がKVをダウンさせないようにすることでした。この新しいプロバイダーは、何千億ものキーと値のペア、保存されたデータのペタバイト、1秒あたり数百万件のGETリクエスト、1秒あたり数万件の定常状態のPUT/DELETEリクエスト、そして数十のスケールに沿って大規模なスケールを処理する必要がありました。ギガビット/秒のスループット—すべてが高可用性と1桁ミリ秒未満の内部遅延で実現。

明らかな選択肢の1つは、今年初めに無効にしたプロバイダーを戻すことでした。しかし、単純にスイッチを切り替えることができませんでした。以前のサードパーティストレージプロバイダーのデュアルバックエンド構成で動作するインフラストラクチャがなくなり、コードが少し破損していたため、以前のデュアルプロバイダーのセットアップに迅速に戻すことは不可能でした。

さらに、このプロバイダーはしばしば、独自の運用上の問題を引き起こすことが多く、エラー率が比較的高く、リクエストのスループット制限が低いため、再度依存することは躊躇されていました。最終的に、2番目のプロバイダーはCloudflareがすべて所有し、運営することにしました。

次の選択肢は、[Cloudflare R2](https://www.cloudflare.com/developer-platform/products/r2/)上に直接構築することでした。すでにR2でWorkers KVのプライベートベータ版を動作させていましたが、この経験を踏まえてWorkers KV独自のストレージ要件をより深く理解することができました。Workers KVのトラフィックパターンは、中央値がわずか288バイトの何千億もの小さなオブジェクトによって特徴付けられており、大きなファイルサイズを前提とした一般的なオブジェクトストレージワークロードとは大きく異なります。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2880 Image 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48R0NVZQWBCCR3FDZ6QFNB.png&w=715&h=536&f=webp&fit=cover&position=center)

この規模の1KB未満のオブジェクトで占められるワークロードの場合、データベースストレージは従来のオブジェクトストレージよりもはるかに効率的で費用対効果が高くなります。値ごとのオーバーヘッドを最小限に抑えながら、非常に小さな値を数十億も保存する必要がある場合、データベースは自然なアーキテクチャとして適しています。当社では、小さなオブジェクトをメタデータでインライン化して、小さなオブジェクトのパフォーマンスを向上させる追加の検索ホップを排除するなど、R2の最適化に取り組んでいますが、緊急のニーズに対し、データベースに支えられたソリューションが最も有望な道となりました。

可能性のあるオプションを徹底的に評価した結果、Cloudflareですでに本番稼働している分散データベースを使用することにしました。この同じデータベースは、R2とDurable Objectsの両方によって水面下で使用されており、当社にはいくつかの主要な利点があります。社内で深い専門知識とデプロイと運用のための既存の自動化があり、その信頼性とパフォーマンスの特性に大規模に依存できることを認識していました。

当社は、複数のデータベースクラスターにデータをシャーディングし、それぞれに3ウェイレプリケーションを採用して、耐久性と可用性を確保しました。このアプローチにより、各シャード内では強力な一貫性保証を維持しながら、容量を水平方向に拡張することができます。当社は、大規模なシステムではなく、複数のクラスターを実行することを選択しました。これは、どのクラスターが不健全になった場合の影響範囲を小さくするため、そして、Workers KVが成長を続ける中で、単一クラスターのスケーラビリティの現実的な限界を押し上げることを避けるためです。

## ソリューションの実装

システムを実装する際に直面した課題の1つが接続性でした。SGWは、当社のコアデータセンターで実行されているデータベースクラスターと通信する必要がありましたが、データベースは通常、持続的なTCP接続上でバイナリプロトコルを使用し、グローバルネットワーク上で効率的に機能するHTTPベースの通信パターンではありません。

当社はこのギャップを埋めるためにKVストレージプロキシ（KVSP）を構築しました。KVSPは、複雑なデータベースの接続性、認証、シャードルーティングを舞台裏で管理しながら、SGWが使用できるHTTPインターフェースを提供するサービスです。KVSPは、一貫したハッシュを用いて、複数のクラスターにまたがるネームスペースを取り除き、人気のあるネームスペースが単一のクラスターを圧倒する可能性のあるホットスポットを防ぎ、うるさい隣人の問題を排除し、容量制限が集中するのではなく分散されるようにします。

Workers KVのストレージに分散データベースを使う最大の欠点は、KVトラフィックを制する小さなオブジェクトの処理には優れているものの、一部のユーザーが保存する最大25MiBといった大きな値には最適ではないことです。私たちは、どちらのユースケースでも妥協するのではなく、KVSPを拡張して、より大きなオブジェクトをCloudflare R2に自動的にルーティングし、オブジェクトの特性に基づいてバックエンドの選択を最適化するハイブリッドストレージアーキテクチャを構築しました。SGWの観点からは、この複雑さは完全に透明です。サイズに関係なく、すべてのオブジェクトに対して同じHTTP APIが機能します。

また、KVの以前のアーキテクチャからストレージプロバイダー間のデュアルプロバイダー機能を復元し、単一プロバイダーにドロップダウンして以来、KVの実装に行われた変更と連携して、うまく機能するようにしました。変更されたシステムは両方のバックエンドへの書き込みを同時にレースすることで動作しますが、最初のバックエンドが書き込みを確認するとすぐに、クライアントに成功が返されます。

これにより、両方のシステムで耐久性を確保しながら、遅延を最小限に抑えることができます。1つのバックエンドが成功しても、他のバックエンドが失敗した場合（一時的なネットワーク問題、レート制限、サービスの低下が原因で）、失敗した書き込みはバックエンドの調整のためにキューに入れられます。これは、以下で詳しく説明する同期マシンの一部として機能します。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2880 Image 4](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45KJ2Y35VN07E7C94MJZV8.png&w=715&h=882&f=webp&fit=cover&position=center)

## ソリューションのデプロイ

ハイブリッドアーキテクチャを実装した後は、サービスの可用性を維持しながら新しいシステムを検証するために設計された慎重なロールアウトプロセスを開始しました。

最初のステップは、SGWから新しいCloudflareバックエンドへのバックグラウンド書き込みの導入でした。これにより、読み取りトラフィックやユーザーエクスペリエンスに影響を与えることなく、実際の本番負荷の下で書き込みパフォーマンスとエラー率を検証できるようになりました。また、すべてのデータを新しいバックエンドにコピーするために必要なステップでした。

次に、サードパーティプロバイダーから既存のデータをCloudflareのインフラストラクチャで動作する新しいバックエンドにコピーし、そのデータをKVSPを経由してルーティングします。これにより、重要なマイルストーンに到達しました。別のプロバイダーの障害が発生した場合、すべてのオペレーションを新しいバックエンドに手動でフェイルオーバーできる状態でした。6月のインシデントを引き起こした単一障害点は排除されています。

フェイルオーバー機能に自信を持って、高度な監視を行い、ワークロードを深く理解しているCloudflareサービスから始めて、最初のネームスペースをアクティブ-アクティブモードで有効化しました。トラフィックを非常にゆっくりとダイヤルし、バックエンド間での結果を慎重に比較しました。SGWは、すでにユーザーに応答を返した後、非同期的に両方のバックエンドからの応答を見ることができるため、ユーザー向けの遅延に影響を与えることなく、詳細な比較を行い、矛盾を検出することができました。

テスト中に、単一プロバイダーの設定と比較して、重要な一貫性の低下を発見しました。これにより、ネームスペースをアクティブ-アクティブモードにする変更を一時的に元に戻しました。設計上、Workers KVは[ _瞬時に一貫性を確保するものではありません_](https://developers.cloudflare.com/kv/concepts/how-kv-works/)。キャッシュされたバージョンがタイムすると、変更をグローバルに伝播するのに最大60秒かかります。ですが私たちはうっかり、同じCloudflareのポイントオブプレゼンスを通じてルーティングされたリクエストに対し、 書き込んだデータの読み取り（RYOW）の一貫性を低下させてしまいました。

以前のデュアルプロバイダーのアクティブ-アクティブセットアップでは、アップストリームストレージの前にある従来のキャッシュシステムに依存するのではなく、PUT操作をローカルキャッシュに直接書き込んだため、各PoP内にRYOWが提供されていました。しかし、KVのスループットはキャッシュインフラストラクチャがサポートできるIOPSの数を上回っていたため、このアプローチに頼ることはできなくなりました。これは、Workers KVのドキュメント化されたプロパティではありませんが、一部のお客様がアプリケーションで採用するようになりました。

この問題の範囲を理解するために、私たちは世界中のわずかな場所から小さなキーのセットに読み書きを迅速に分散させることで、エッジケースにヒットする可能性を最大化する敵対的テストフレームワークを作成しました。このフレームワークにより、RYOWの一貫性違反が観察された読み込みの割合を測定することができました。つまり、同じポイントオブプレゼンスからの書き込みの直後に、書き込まれた値ではなく、古いデータが返されるシナリオでした。これにより、KVによるキャッシュへのデータの入力と無効化に対する新しいアプローチを設計、検証することができました。お客様が期待するRYOWの動作を復元し、一方で、Workers KVが高読み取りのワークロードに対して効果的であるためのパフォーマンス特性を維持しました。

## KVが複数のバックエンドにまたがり一貫性を維持する方法

書き込みと読み取りの両方で加速し、異なる結果を返す可能性があるため、独立したストレージプロバイダー間でデータの一貫性を維持するには、高度な多層防御のアプローチが必要です。詳細は時が経つにつれて進化してきましたが、KVは常に同じ基本的なアプローチを採用しています。3つの補完的なメカニズムで構成され、それらが連携して不整合の可能性を減らし、データの相違のオリジンを最小限に抑えることができるようにしています。

防御の最初の一手は書き込み操作時に行われます。SGWが両方のバックエンドに同時に書き込みを送信した場合、どちらかのプロバイダーが永続性を確認するとすぐに、書き込みが成功したものとして扱われます。ネットワークの問題、レート制限、または一時的なサービス低下が原因で、プロバイダーと一方のプロバイダーで書き込みが成功した場合、もう一方のプロバイダーでは失敗した場合、失敗した書き込みはキャプチャされ、バックグラウンド調整システムに送信されます。このシステムでは、失敗したキーの重複を排除し、同期プロセスを開始して不整合を解決します。

2つ目のメカニズムは、読み取り操作中にアクティブになります。SGWレースが両方のプロバイダーに対して読み取りを行い、異なる結果に気づいた場合、同じバックグラウンド同期プロセスをトリガーします。これにより、不整合になったキーが無期限に多様なままではなく、最初にアクセスされたときに整合に戻るようにすることができます。

3層目は、プロバイダー両方で継続的にデータをスキャンし、以前のメカニズムで見落とされていた不整合を特定して修正するバックグラウンドクローラーで構成されます。また、これらのクローラーは一貫性の移動率に関する貴重なデータを提供し、キーがどの程度の頻度でリアクティブメカニズムをすり抜けるかを把握し、根本的な問題を解決するのに役立ちます。

同期プロセス自体は、すべてのキーと値のペアに付加するバージョンメタデータに依存します。書き込みのたびに、高精度のタイムスタンプとランダムなnonceで構成される新しいバージョンが自動的に生成され、実際のデータと一緒に保存されます。プロバイダー間の値を比較するときは、これらのタイムスタンプに基づいて、どのバージョンが新しいかを判断できます。その後、新しい値が古いバージョンのプロバイダーにコピーされます。

タイムスタンプが互いに数ミリ秒以内にある場合は、クロックのスキューが理論的には順序付けの不正を引き起こす可能性がありますが、[ _Cloudflare Time Services_](https://www.cloudflare.com/time/)を介してクロックに維持している厳しい制限や、通常の書き込み遅延を考えると、このような競合は、ほぼ同時のオーバーラップ書き込みの場合にのみ発生します。

同期中のデータ損失を防ぐために、防御的に値を上書きするのではなく、書き込み前に最後のタイムスタンプが古いことを検証する条件付き書き込みを使用します。これにより、近接するリクエストが異なるバックエンドに成功し、同期プロセスが古い値を新しい値上にコピーする場合に、新たな一貫性の問題が発生することを回避できます。

同様に、ユーザーが要求したデータを単に削除することはできません。削除が1つのバックエンドでのみ成功した場合、同期プロセスはこれを欠落していると見なし、他のバックエンドからそれをコピーしてしまうためです。代わりに、新しいタイムスタンプを持つ、実際のデータのないトークンで値を上書きします。両方のプロバイダーがトークンを所有した後でのみ、ストレージからキーを実際に削除します。

この階層型一貫性アーキテクチャは、強力な一貫性を保証するものではありません が、実際には、バックエンド間のほとんどの不一致を排除し、Workers KVが遅延の影響を受けやすい高読み取りワークロード向けに魅力的なパフォーマンスプロファイルを維持すると同時に、あらゆる場合に高可用性を提供します。エラーを迅速化することです。分散システムで言えば、KVは[ _CAP定理_](https://en.wikipedia.org/wiki/CAP_theorem)で一貫性（CP）より可用性（AP）を選択し、さらに興味深いことに、パーティションがない場合は一貫性より遅延を選択します。つまり、[ _PACELC定理_](https://en.wikipedia.org/wiki/PACELC_design_principle)に基づくPA/ELです。ほとんどの不整合はリアクティブなメカニズムを使って数秒以内に解決しますが、バックグラウンドクローラーはエッジケースでも通常は時間をかけて修正します。

上記の説明は、従来のデュアルプロバイダーのセットアップと現在の実装の両方に適用されますが、現行のアーキテクチャでは2つの重要な改善が行われているため、一貫性が大幅に向上しています。まず、KVSPはこれまでのサードパーティプロバイダーに比べて定常状態のエラー率をかなり低く抑えており、そもそも不整合を引き起こす書き込み失敗の頻度を減らします。第二に、コストと遅延の最適化を行っていた従来のシステムでは、最初の学習期間後に読み取りを単一プロバイダーに優先的にルーティングすることで、コストと遅延の最適化を行っていたのに対し、現在はすべての読み取りで両者のバックエンドで競合するようになっています。

従来のデュアルプロバイダーアーキテクチャでは、各SGWインスタンスは当初、両方のプロバイダーに対して読み取りの競合を行い、ベースラインのパフォーマンス特性を確立していました。インスタンスが、地理的にどちらのプロバイダーよりも優れていると判断すると、後続の読み取りはより速いプロバイダーにのみルーティングされ、プライマリで障害や異常な遅延が発生した場合にのみ、より遅いプロバイダーにフォールバックします。このアプローチはサードパーティプロバイダーのコストと最適化された読み取りパフォーマンスを効果的に管理しましたが、一貫性検出メカニズムに大きな盲点ができてしまいました。読み取りが1つのバックエンドから一貫して提供される場合、プロバイダー間の不整合が無期限に続く可能性があります。

## 結果：パフォーマンスと可用性の向上

これらの一貫性メカニズムを導入し、内部サービスを通じて慎重にロールアウト戦略を検証した後、私たちは内部と外部のワークロードの両方で追加のネームスペースにアクティブアクティブな運用を拡張し続けました。新しいアーキテクチャは、Workers KVに必要だった可用性を向上させただけでなく、パフォーマンスを大幅に改善しました。

これらのパフォーマンスの向上は、新しいストレージバックエンドが配置されているヨーロッパで特に顕著でしたが、その効果は地理的な局所性だけで説明できる範囲を超えるものでした。並行して書き込みを行っていたサードパーティ製のオブジェクトストアと比較した内部遅延の改善は、顕著でした。

例えば、KVSPへの読み込みのp99の内部遅延は5ミリ秒以下でした。比較のために、最も近い場所からサードパーティオブジェクトストアへのキャッシュされていない読み取りは、同じ条件で比較を作成するために転送時間を正規化した後、通常p50で約80ms、p99では約200msでした。

下のグラフは、同じ条件の比較の最も近い結果を示しています。KVSPへのリクエストの内部遅延と、キャッシュミスになり、外部サービスプロバイダーに転送されたリクエストの遅延を比較したものです。最も近いポイントオブプレゼンスで、5～10ミリ秒のリクエスト転送時間が発生します。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2880 Image 5](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW483RS4DV6QADAXAD3G6HBA.png&w=715&h=413&f=webp&fit=cover&position=center)

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2880 Image 6](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46DHWAAT9MQMN1437121N6.png&w=715&h=417&f=webp&fit=cover&position=center)

これらのパフォーマンス改善は、Workers KVに依存している多くのCloudflareサービスの応答時間の短縮に直接結びつき、プラットフォーム全体で連鎖的なメリットを生み出します。データベースに最適化されたストレージは、Workers KVトラフィックを占める小さなオブジェクトのアクセスパターンに特に効果的であることが証明されました。

このようなプラスの結果を確認した後、ロールアウトを拡大し続け、データをコピーして、内部のお客様と外部のお客様のネームスペースのグループを有効にしました。可用性向上とパフォーマンス向上の組み合わせは、当社のアーキテクチャ的アプローチの妥当性が確認され、重要インフラストラクチャを独自プラットフォームで構築することの価値を実証しました。

## 今後の展開は？

当社の当面の計画は、このハイブリッドアーキテクチャを拡張して、Workers KVにさらに高い耐障害性とパフォーマンスを提供することに焦点を当てています。当社は、KVSPソリューションを追加の拠点に展開し、自社インフラストラクチャからトラフィック全体を提供できる真にグローバルな分散型バックエンドを構築するとともに、プロバイダー間の一貫性と書き込み後のキャッシュの一貫性をさらに向上させる取り組みを進めています。

最終目標は、残っているサードパーティのストレージへの依存を完全に排除し、Workers KVのインフラストラクチャの完全な独立性を実現することです。これにより、6月のインシデントにつながった外部の単一障害点を排除し、ストレージレイヤーのパフォーマンスと信頼性の特性を完全に制御できるようになります。

Workers KVを超えて、このプロジェクトは、異なるストレージ技術の最高の点を組み合わせたハイブリッドアーキテクチャの力を実証しました。KVSPを翻訳層として使用し、サイズの特性に基づいてオブジェクトを自動的にルーティングし、既存のデータベースの専門知識を活用して開発したパターンを、グローバルなスケールと強力な一貫性要件のバランスを必要とする他のサービスで活用することができます。シングルプロバイダーによる設定からCloudflareのインフラストラクチャ上で動作する回復力のあるハイブリッドアーキテクチャへの移行は、綿密なエンジニアリングによって運用上の課題を競争優位性に変えることができることを示しています。劇的に向上したパフォーマンスとアクティブアクティブ冗長性を備えたWorkers KVは、増え続けるお客様にとって、より信頼性の高い基盤として機能します。

このページ

オンラインで議論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Frearchitecting-workers-kv-for-redundancy%2F&t=Workers%20KV%E3%82%92%E5%86%8D%E8%A8%AD%E8%A8%88%E3%81%97%E3%80%81%E5%8F%AF%E7%94%A8%E6%80%A7%E3%81%A8%E3%83%91%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%B3%E3%82%B9%E3%82%92%E9%AB%98%E9%80%9F%E5%8C%96)[](https://x.com/intent/post?text=Workers+KV%E3%82%92%E5%86%8D%E8%A8%AD%E8%A8%88%E3%81%97%E3%80%81%E5%8F%AF%E7%94%A8%E6%80%A7%E3%81%A8%E3%83%91%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%B3%E3%82%B9%E3%82%92%E9%AB%98%E9%80%9F%E5%8C%96&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Frearchitecting-workers-kv-for-redundancy%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Frearchitecting-workers-kv-for-redundancy%2F)[](https://bsky.app/intent/compose?text=Workers+KV%E3%82%92%E5%86%8D%E8%A8%AD%E8%A8%88%E3%81%97%E3%80%81%E5%8F%AF%E7%94%A8%E6%80%A7%E3%81%A8%E3%83%91%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%B3%E3%82%B9%E3%82%92%E9%AB%98%E9%80%9F%E5%8C%96+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Frearchitecting-workers-kv-for-redundancy%2F)[](https://mastodonshare.com/?text=Workers+KV%E3%82%92%E5%86%8D%E8%A8%AD%E8%A8%88%E3%81%97%E3%80%81%E5%8F%AF%E7%94%A8%E6%80%A7%E3%81%A8%E3%83%91%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%B3%E3%82%B9%E3%82%92%E9%AB%98%E9%80%9F%E5%8C%96&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Frearchitecting-workers-kv-for-redundancy%2F)[](https://www.threads.net/intent/post?text=Workers+KV%E3%82%92%E5%86%8D%E8%A8%AD%E8%A8%88%E3%81%97%E3%80%81%E5%8F%AF%E7%94%A8%E6%80%A7%E3%81%A8%E3%83%91%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%B3%E3%82%B9%E3%82%92%E9%AB%98%E9%80%9F%E5%8C%96+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Frearchitecting-workers-kv-for-redundancy%2F)

## 関連するタグ

[Cloudflare Workers KV](https://blog.cloudflare.com/ja-jp/tag/cloudflare-workers-kv/)[事後検証](https://blog.cloudflare.com/ja-jp/tag/post-mortem/)

SNS をフォロー

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 新しい投稿のお知らせを受け取るように登録する

メールアドレス

また、あなたのメールアドレスを共有したりすることはございません。

登録する

ご購読ありがとうございます！受信箱を確認して登録してください。
