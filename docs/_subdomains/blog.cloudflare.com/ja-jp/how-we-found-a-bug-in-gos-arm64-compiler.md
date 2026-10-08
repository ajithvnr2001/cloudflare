---
url: https://blog.cloudflare.com/ja-jp/how-we-found-a-bug-in-gos-arm64-compiler/
title: Go\u306eARM64\u30b3\u30f3\u30d1\u30a4\u30e9\u306b\u30d0\u30b0\u304c\u767a\u898b\u3055\u308c\u305f\u7d4c\u7def | Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:51:44.436883+00:00
---

# GoのARM64コンパイラにバグが発見された経緯 | Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/how-we-found-a-bug-in-gos-arm64-compiler/

[ブログ](https://blog.cloudflare.com/ja-jp/)

[Go](https://blog.cloudflare.com/ja-jp/tag/go/)[プログラミング](https://blog.cloudflare.com/ja-jp/tag/programming/)[詳細情報](https://blog.cloudflare.com/ja-jp/tag/deep-dive/)

3 タグタグを3件表示

  * 投稿タグ
  * [Go](https://blog.cloudflare.com/ja-jp/tag/go/)[プログラミング](https://blog.cloudflare.com/ja-jp/tag/programming/)[詳細情報](https://blog.cloudflare.com/ja-jp/tag/deep-dive/)
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



[Go](https://blog.cloudflare.com/ja-jp/tag/go/)[プログラミング](https://blog.cloudflare.com/ja-jp/tag/programming/)[詳細情報](https://blog.cloudflare.com/ja-jp/tag/deep-dive/)

2025年10月8日

# GoのARM64コンパイラにバグが発見された経緯

![Thea Heinen](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44CYSDFZQ7AE7FQYJ5JVNT.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Thea Heinen](https://blog.cloudflare.com/ja-jp/author/thea-heinen/)

16分で読了

URLをコピー

この記事は以下でも利用可能です [English](https://blog.cloudflare.com/how-we-found-a-bug-in-gos-arm64-compiler/).

![BLOG-2906 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44Z05J142VJQZBGB2SYBG0.png&w=2000&h=1140&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/////v3+8fHz6ers7Ozv8/Lz8vHz6+vt////////8/Lx6+nm7unm9O7r8/Dv7e3u////////9vXx7uni8Oje9uzk9vDs8PDw////////+/n08u3j9Ore+u7l+/Pu9fX1///////////7+PPs+vHo//bu//n2+vr6/////////////fv4//v4///9////////////////////////////////////////////////////////////////////////)

Cloudflareの330都市に広がるデータセンター全体で、毎秒8400万件のHTTPリクエストが送信されています。そのため、稀なバグでも頻繁に発生する可能性があります。実際、最近、GoのARM64コンパイラでバグが発見され、生成されたコードで競合状態が発生するのは当社のスケールが原因でした。

この記事では、私たちが最初にバグを発見し、調査し、最終的に根本原因を特定した経緯について説明します。

## 奇妙なパニックを調査する

[ _Magic Transit_](https://www.cloudflare.com/network-services/products/magic-transit/)や[ _Magic WAN_](https://www.cloudflare.com/network-services/products/magic-wan/)などの一部の製品のトラフィックを処理するためにカーネルを設定するサービスをネットワーク内で実行しています。Cloudflareの監視により、Arm64マシン上で非常に散発的なパニックが観測されるようになりました。

最初に目にしたのは、[ _トレースバックが完全にアンウィンドにならなかった_](https://github.com/golang/go/blob/c0ee2fd4e309ef0b8f4ab6f4860e2626c8e00802/src/runtime/traceback.go#L566)という重大なエラーです。このエラーは、おそらくスタックの破損が原因で、スタックを横断する際に不変量が侵害されたことを示唆しています。簡単な調査の後、これはおそらく稀なスタックメモリの破損であると判断されました。これは概してアイドル状態のコントロールプレーンサービスであり、計画外の再起動による影響はごくわずかでした。そのため、それを継続する限り、フォローアップは優先事項ではないと考えました。

そして、それが続くのです。

#### 1 時間あたりのコアダンプ

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2906 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48ZNQJN6BEDR97MYX9VGVP.png&w=715&h=188&f=webp&fit=cover&position=center)

最初にこのバグを回復した時、重大なエラーがパニックと相関があることがわかりました。これらは、パニック/リカバリをエラー処理として使用していた一部の古いコードが原因でした。

この時点で、当社の理論は次のとおりでした。

  1. 重大なパニックはすべてスタックアンファイル内で起こります。
  2. 回復したパニックの量の増加と、これらの重大なパンデミックの発生と相関関係にありました。
  3. パニックを回復することで、遅延された関数を呼び出すために、ルーティングスタックが解除されます。
  4. [ _Goに関連する問題（#73259）_](https://github.com/golang/go/issues/73259)では、ARM64スタックのアンウィンドクラッシュが報告されました。
  5. エラー処理にpanic/recoverの使用をやめて、アップストリームの修正を待ちましょう？



そこで、当社はこれを実行し、リリースがロールアウトするにつれて重大なパニックが発生するのを防ぎました。致命的なパニックはなくなり、理論上の軽減策が有効になっているようで、これはもはや私たちの問題ではなくなりました。私たちはアップストリームの問題を購読し、問題が解決されたら更新し、それを念頭から置くことにしました。

しかし、これは予想以上に奇妙なバグであることが判明しました。同じクラスの致命的なパニックがはるかに高い割合で再び出現してきたため、それを考えることは時期尚早でした。1か月後、実際に識別可能な原因のない、重大なパニックが毎日30件以上発生しました。データセンターの1日あたり1台のマシンしか使用していないかもしれませんが、私たちが原因を理解していないのは懸念点です。最初に確認したのは、以前のパターンと一致させるために、回復されたパニックの数でしたが、ありませんでした。さらに興味深いことに、重大なパニック的割合の増加が他と相関することはありませんでした。リリース？インフラストラクチャの変更Marsの役職 

私たちはこの時点で、根本的な原因を理解するためにさらに深く掘り下げる必要があると感じました。パターンマッチングと期待が明らかに不十分でした。

このバグには、無効なメモリにアクセスした際のクラッシュと、明示的に確認された重大なエラーという2つのクラスのバグが見られました。

#### 重大なエラー
    
    
    goroutine 153 gp=0x4000105340 m=324 mp=0x400639ea08 [GC worker (active)]:
    /usr/local/go/src/runtime/asm_arm64.s:244 +0x6c fp=0x7ff97fffe870 sp=0x7ff97fffe860 pc=0x55558d4098fc
    runtime.systemstack(0x0)
           /usr/local/go/src/runtime/mgc.go:1508 +0x68 fp=0x7ff97fffe860 sp=0x7ff97fffe810 pc=0x55558d3a9408
    runtime.gcBgMarkWorker.func2()
           /usr/local/go/src/runtime/mgcmark.go:1102
    runtime.gcDrainMarkWorkerIdle(...)
           /usr/local/go/src/runtime/mgcmark.go:1188 +0x434 fp=0x7ff97fffe810 sp=0x7ff97fffe7a0 pc=0x55558d3ad514
    runtime.gcDrain(0x400005bc50, 0x7)
           /usr/local/go/src/runtime/mgcmark.go:212 +0x1c8 fp=0x7ff97fffe7a0 sp=0x7ff97fffe6f0 pc=0x55558d3ab248
    runtime.markroot(0x400005bc50, 0x17e6, 0x1)
           /usr/local/go/src/runtime/mgcmark.go:238 +0xa8 fp=0x7ff97fffe6f0 sp=0x7ff97fffe6a0 pc=0x55558d3ab578
    runtime.markroot.func1()
           /usr/local/go/src/runtime/mgcmark.go:887 +0x290 fp=0x7ff97fffe6a0 sp=0x7ff97fffe560 pc=0x55558d3acaa0
    runtime.scanstack(0x4014494380, 0x400005bc50)
           /usr/local/go/src/runtime/traceback.go:447 +0x2ac fp=0x7ff97fffe560 sp=0x7ff97fffe4d0 pc=0x55558d3eeb7c
    runtime.(*unwinder).next(0x7ff97fffe5b0?)
           /usr/local/go/src/runtime/traceback.go:566 +0x110 fp=0x7ff97fffe4d0 sp=0x7ff97fffe490 pc=0x55558d3eed40
    runtime.(*unwinder).finishInternal(0x7ff97fffe4f8?)
           /usr/local/go/src/runtime/panic.go:1073 +0x38 fp=0x7ff97fffe490 sp=0x7ff97fffe460 pc=0x55558d403388
    runtime.throw({0x55558de6aa27?, 0x7ff97fffe638?})
    runtime stack:
    fatal error: traceback did not unwind completely
           stack=[0x4015d6a000-0x4015d8a000
    runtime: g8221077: frame.sp=0x4015d784c0 top=0x4015d89fd0

#### セグメント化の問題
    
    
    goroutine 187 gp=0x40003aea80 m=13 mp=0x40003ca008 [GC worker (active)]:
           /usr/local/go/src/runtime/asm_arm64.s:244 +0x6c fp=0x7fff2afde870 sp=0x7fff2afde860 pc=0x55557e2d98fc
    runtime.systemstack(0x0)
           /usr/local/go/src/runtime/mgc.go:1489 +0x94 fp=0x7fff2afde860 sp=0x7fff2afde810 pc=0x55557e279434
    runtime.gcBgMarkWorker.func2()
           /usr/local/go/src/runtime/mgcmark.go:1112
    runtime.gcDrainMarkWorkerDedicated(...)
           /usr/local/go/src/runtime/mgcmark.go:1188 +0x434 fp=0x7fff2afde810 sp=0x7fff2afde7a0 pc=0x55557e27d514
    runtime.gcDrain(0x4000059750, 0x3)
           /usr/local/go/src/runtime/mgcmark.go:212 +0x1c8 fp=0x7fff2afde7a0 sp=0x7fff2afde6f0 pc=0x55557e27b248
    runtime.markroot(0x4000059750, 0xb8, 0x1)
           /usr/local/go/src/runtime/mgcmark.go:238 +0xa8 fp=0x7fff2afde6f0 sp=0x7fff2afde6a0 pc=0x55557e27b578
    runtime.markroot.func1()
           /usr/local/go/src/runtime/mgcmark.go:887 +0x290 fp=0x7fff2afde6a0 sp=0x7fff2afde560 pc=0x55557e27caa0
    runtime.scanstack(0x40042cc000, 0x4000059750)
           /usr/local/go/src/runtime/traceback.go:458 +0x188 fp=0x7fff2afde560 sp=0x7fff2afde4d0 pc=0x55557e2bea58
    runtime.(*unwinder).next(0x7fff2afde5b0)
    goroutine 0 gp=0x40003af880 m=13 mp=0x40003ca008 [idle]:
    PC=0x55557e2bea58 m=13 sigcode=1 addr=0x118
    SIGSEGV: segmentation violation

これで、いくつかの明確なパターンが観察されるようになりました。`(*unwinder).next`でスタックを解除する際に、両方のエラーが発生します。あるケースでは、ランタイムがアンウィンドを完了できず、スタックが悪性状態にあることを識別し、意図的な[ _重大なエラー_](https://github.com/golang/go/blob/b3251514531123d7fd007682389bce7428d159a0/src/runtime/traceback.go#L566)が発生しました。別のケースでは、スタックを解約しようとしているときに、直接メモリアクセスエラーが発生しました。このセグメント違反は [_GitHub の問題_](https://github.com/golang/go/issues/73259#issuecomment-2786818812)で議論され、Go エンジニアはこれを、アンワインド時の Go スケジューラ構造体 [_m_](https://github.com/golang/go/blob/924fe98902cdebf20825ab5d1e4edfc0fed2966f/src/runtime/runtime2.go#L536) の逆参照であると[ _特定しました_](https://github.com/golang/go/blob/b3251514531123d7fd007682389bce7428d159a0/src/runtime/traceback.go#L458)。 

### Go Scheduler structsのレビュー

Goは、軽量ユーザー空間スケジューラを使用して、同時実行性を管理します。多くのゴルーチンは、より少数のカーネルスレッドでスケジュールされます。これはしばしばM:Nスケジューリングと呼ばれます。どんなカーネルスレッドでも、個々のgoroutingをスケジュールすることができます。スケジューラには3つのコアタイプがあります。[` _g_`](https://github.com/golang/go/blob/924fe98902cdebf20825ab5d1e4edfc0fed2966f/src/runtime/runtime2.go#L394)（ゴルーチン）、[` _m_`](https://github.com/golang/go/blob/924fe98902cdebf20825ab5d1e4edfc0fed2966f/src/runtime/runtime2.go#L536)（カーネルスレッド「マシン」）、[` _p_`](https://github.com/golang/go/blob/924fe98902cdebf20825ab5d1e4edfc0fed2966f/src/runtime/runtime2.go#L644)（物理的実行コンテキスト「プロセッサ」）です。ゴルーチンをスケジュールするには、無料の`m`が無料の`p`を取得し、それがgを実行する必要があります。各`g`には、現在実行中の場合はmのフィールドが含まれ、それ以外の場合は**nil** になります。この記事に必要なコンテキストはこれだけですが、[ _Goのランタイムドキュメント_](https://github.com/golang/go/blob/master/src/runtime/HACKING.md#gs-ms-ps)ではさらに包括的に考察しています。

この時点で、何が起こっているかについて推論し始めることができます。プログラムがクラッシュするのは、無効なゴルーチンスタックを解除しようとするからです。最初のバックトレースにおいて、[ _リターンアドレスがNULLの場合、スタックが完全にアンワインドされていないため、`finishInternal`を呼び出してアボートする_](https://github.com/golang/go/blob/b3251514531123d7fd007682389bce7428d159a0/src/runtime/traceback.go#L446)。2番目のバックトレースのセグメンテーション違反のケースは、少し興味深いものです。代わりに、リターンアドレスがゼロ以外の場合、unwinderコードは、goroutineが現在実行中であると仮定します。次に、`m.incgo`にアクセスすることでmとaultを解除します（`struct m`と`incgo`のオフセットは0x118であり、メモリアクセスが故障しています）。 

では、何が原因で実現したのでしょうか？トレースから有用なものを得るのは困難でした。当社のサービスには、何千ものアクティブなガルーチンがあり、何百もあるのです。パニックが実際のバグから離れたものであることは最初から明らかでした。クラッシュはすべて、スタックを復元する際に観測されたものであり、これが問題だというなら、スタックがARM64上で復元されたときに、さらに多くのサービスで問題が発生するでしょう。スタックのアンウィンドが正しく行われていると確信していましたが、無効なスタック上にあると私たちは確信していました。

この時点で、私たちの調査は、推測を続けたり、推測をしたり、パニック発生率が上がったかどうか、あるいは何も変化していないかを推測しようとする中で、しばらく停滞してしまいました。GoのGitHubのIssue Trackerで[ _既知の問題_](https://github.com/golang/go/issues/73259)があり、それがほぼ当社の症状と一致するものの、彼らが議論した内容はほとんど当社がすでに把握していたものでした。ある時点で、リンクされたスタックトレースを調べてみたところ、そのクラッシュが私たちも使用していたライブラリの古いバージョン「Go Netlink」を参照していることに気づきました。
    
    
    goroutine 1267 gp=0x4002a8ea80 m=nil [runnable (scan)]:
    runtime.asyncPreempt2()
            /usr/local/go/src/runtime/preempt.go:308 +0x3c fp=0x4004cec4c0 sp=0x4004cec4a0 pc=0x46353c
    runtime.asyncPreempt()
            /usr/local/go/src/runtime/preempt_arm64.s:47 +0x9c fp=0x4004cec6b0 sp=0x4004cec4c0 pc=0x4a6a8c
    github.com/vishvananda/netlink/nl.(*NetlinkSocket).Receive(0x14360300000000?)
            /go/pkg/mod/github.com/!data!dog/netlink@v1.0.1-0.20240223195320-c7a4f832a3d1/nl/nl_linux.go:803 +0x130 fp=0x4004cfc710 sp=0x4004cec6c0 pc=0xf95de0
    

いくつかのスタックトレースをスポットチェックし、このNetlinkライブラリの存在を確認しました。ログを照会したところ、ライブラリを共有しただけでなく、当社が観測したセグメンテーションの不具合がすべて、[ `_NetlinkSocket.Receive_`](https://github.com/vishvananda/netlink/blob/e1e260214862392fb28ff72c9b11adc84df73e2c/nl/nl_linux.go#L880)をプリエンプトしている間に発生していたことがわかりました。

### （非同期）プリエンプションとは？

Go（以前は1.13以下）の時代には、ランタイムは協同組合でスケジュール設定されていました。ゴルーチンは、スケジューラに収束する準備ができたと判断するまで実行されます。これは通常、`runtime.Gosched()`への明示的な呼び出しや、関数呼び出し/IO操作に離脱点が注入されているためです。[ _Go 1.14_](https://go.dev/doc/go1.14#runtime)以降は、ランタイムは代わりにasyncプリエンプションを行います。Goランタイムには、ゴルーチンの実行時間を追跡するスレッド`sysmon`があり、（書き込み時点で）10ms以上実行されたものをプリエンプトします。これは、`SIGURG`をOSスレッドに送信することで行われます。シグナルハンドラはプログラムカウンターとスタックを変更し、`asyncPreempt`への呼び出しを模倣します。

この時点で、私たちは2つの大きな理論がありました。

  * これはGo Netlinkのバグです。おそらく`unsafe.Pointer`の使用が未定義動作を引き起こしたためですが、実際に動作しないのはarm64アーキテクチャのみです。
  * これはGoのランタイムのバグであり、`NetlinkSocket.Receive`でのみトリガーしているだけです。



アップストリームで公表されている同じバグを見つけた後、私たちはこのバグがGoランタイムのバグによって引き起こされていると確信しました。しかし、両方の問題が同じ機能を示唆していることを知り、私たちはより懐疑的と感じました。特に、Go Netlinkライブラリは安全でないものを使用しているのです。では、その理由は不明でしたが、メモリ破損は妥当な説明かもしれませんでした。

コード監査が失敗した後に、私たちは壁に突き当たりました。クラッシュは稀で、根本原因からは程遠いものでした。これらのクラッシュは、ランタイムのバグによって引き起こされたかもしれませんし、Go Netlinkのバグによって引き起こされたかもしれません。明らかにコードのこの領域に何か問題があるように思われましたが、コード監査はうまくいきませんでした。 

## ブレイクスルー

この時点で、私たちはクラッシュしているものが何かをよく理解していましたが、**なぜ** それが起きているのかについてはほとんど理解していませんでした。スタックアンウィンダーのクラッシュの根本的な原因が、実際のクラッシュからリモートであり、`(*NetlinkSocket).` receivedに関係していることは明らかですが、なぜでしょう？本番環境のクラッシュの**コアダンプ** をキャプチャし、デバッガーで表示することができました。バックトレースは、私たちがすでに知っていたことを確認しました。つまり、スタックを解凍する際にセグメンテーションの欠陥があるということです。この問題の核心は、`(*NetlinkSocket).Receive`を呼び出す中に先制されているゴルーチンを調べた時に明らかになりました。 
    
    
    (dlv) bt
    0  0x0000555577579dec in runtime.asyncPreempt2
       at /usr/local/go/src/runtime/preempt.go:306
    1  0x00005555775bc94c in runtime.asyncPreempt
       at /usr/local/go/src/runtime/preempt_arm64.s:47
    2  0x0000555577cb2880 in github.com/vishvananda/netlink/nl.(*NetlinkSocket).Receive
       at
    /vendor/github.com/vishvananda/netlink/nl/nl_linux.go:779
    3  0x0000555577cb19a8 in github.com/vishvananda/netlink/nl.(*NetlinkRequest).Execute
       at 
    /vendor/github.com/vishvananda/netlink/nl/nl_linux.go:532
    4  0x0000555577551124 in runtime.heapSetType
       at /usr/local/go/src/runtime/mbitmap.go:714
    5  0x0000555577551124 in runtime.heapSetType
       at /usr/local/go/src/runtime/mbitmap.go:714
    ...
    (dlv) disass -a 0x555577cb2878 0x555577cb2888
    TEXT github.com/vishvananda/netlink/nl.(*NetlinkSocket).Receive(SB) /vendor/github.com/vishvananda/netlink/nl/nl_linux.go
            nl_linux.go:779 0x555577cb2878  fdfb7fa9        LDP -8(RSP), (R29, R30)
            nl_linux.go:779 0x555577cb287c  ff430191        ADD $80, RSP, RSP
            nl_linux.go:779 0x555577cb2880  ff434091        ADD $(16<<12), RSP, RSP
            nl_linux.go:779 0x555577cb2884  c0035fd6        RET
    

関数エピローチの2つのオプコード間で、ゴルーチンが一時停止されていました。スタックを解約するプロセスは、スタックフレームが一貫した状態にあることに依存しているため、スタックポインターを調整する途中で先回りしたのは即座に疑わしく感じました。ゴルーチンは、`ADD $80, RSP, RSP と ADD $(16<<12), RSP, RSP` の間、0x555577cb2880で一時停止されていました。

私たちは、この理論を確認するためにサービスログを照会しました。これは分離されたものではありません。スタックトレースの大半は、この同じオプコードがプリエンプトされていることを示していました。これはもう、再現不可能な本番環境のクラッシュではありませんでした。この2つのスタックポインタの調整の間、Goランタイムがプリエンプトした時にクラッシュが発生しました。Cloudflareには我々よりもユースケースが必要でした。

## 最小限の複製の構築

この時点で、私たちは、これは実際には実行時のバグであり、依存関係なく、隔離された環境で再現できるはずだとかなり確信していました。この時点の理論は次のとおりです。

  1. ガベージコレクションによってスタックのアンウィンドがトリガーされます
  2. スプリットスタックポインター調整間の非同期プリエンプションによりクラッシュが発生
  3. 調整を分割する関数を作って、ループの中で呼び出すはどうなるでしょうか。


    
    
    package main
    
    import (
    	"runtime"
    )
    
    //go:noinline
    func big_stack(val int) int {
    	var big_buffer = make([]byte, 1 << 16)
    
    	sum := 0
    	// prevent the compiler from optimizing out the stack
    	for i := 0; i < (1<<16); i++ {
    		big_buffer[i] = byte(val)
    	}
    	for i := 0; i < (1<<16); i++ {
    		sum ^= int(big_buffer[i])
    	}
    	return sum
    }
    
    func main() {
    	go func() {
    		for {
    			runtime.GC()
    		}
    	}()
    	for {
    		_ = big_stack(1000)
    	}
    }
    

この関数は、16ビットで表現できるよりも少し大きなスタックフレームになります。そのため、ARM64は、スタックポインタ調整を2つのオプコードに分割します。これらのオプコード間でランタイムがプリエンプトする場合、スタックアンウィンダーは無効なスタックポインターを読み取り、クラッシュします。
    
    
    ; epilogue for main.big_stack
    ADD $8, RSP, R29
    ADD $(16<<12), R29, R29
    ADD $16, RSP, RSP
    ; preemption is problematic between these opcodes
    ADD $(16<<12), RSP, RSP
    RET
    

これを数分間実行した後、プログラムは予想通りにパニックになりました！
    
    
    SIGSEGV: segmentation violation
    PC=0x60598 m=8 sigcode=1 addr=0x118
    
    goroutine 0 gp=0x400019c540 m=8 mp=0x4000198708 [idle]:
    runtime.(*unwinder).next(0x400030fd10)
            /home/thea/sdk/go1.23.4/src/runtime/traceback.go:458 +0x188 fp=0x400030fcc0 sp=0x400030fc30 pc=0x60598
    runtime.scanstack(0x40000021c0, 0x400002f750)
            /home/thea/sdk/go1.23.4/src/runtime/mgcmark.go:887 +0x290 
    
    [...]
    
    goroutine 1 gp=0x40000021c0 m=nil [runnable (scan)]:
    runtime.asyncPreempt2()
            /home/thea/sdk/go1.23.4/src/runtime/preempt.go:308 +0x3c fp=0x40003bfcf0 sp=0x40003bfcd0 pc=0x400cc
    runtime.asyncPreempt()
            /home/thea/sdk/go1.23.4/src/runtime/preempt_arm64.s:47 +0x9c fp=0x40003bfee0 sp=0x40003bfcf0 pc=0x75aec
    main.big_stack(0x40003cff38?)
            /home/thea/dev/stack_corruption_reproducer/main.go:29 +0x94 fp=0x40003cff00 sp=0x40003bfef0 pc=0x77c04
    Segmentation fault (core dumped)
    
    real    1m29.165s
    user    4m4.987s
    sys     0m43.212s

Standardライブラリのみで再現可能なクラッシュ？これは、私たちの問題がランタイムのバグであることを決定的に証明したように感じられました。

これは非常に特殊な再現ツールでした。バグとその修正について十分に理解したとしても、それでも理解できない動作もあります。これは1つの指示による競合状態であり、小さな変更が大きな影響を与えることは当然のことです。たとえば、この再現者は当初、Go 1.23.4で書かれ、テストされました。1.23.9（本番稼働中のバージョン）でコンパイルした時にクラッシュすることはありませんでした。バイナリをオブジェクトダンプして、分割ADDがまだ存在しているのを見ることができたのです！この挙動については明確な説明ができません。バグが存在しても、競合状態に遭遇する可能性に影響する未知の変数がいくつかあります。

## 単一命令の競合状態ウィンドウ

Arm64は、固定長の4バイトの命令セットアーキテクチャです。これはコード生成に多くの影響を与えますが、このバグに最も関連しているのは、直接の長さが制限されているという事実です。 [`_add_`](https://developer.arm.com/documentation/ddi0596/2020-12/Base-Instructions/ADD--immediate---Add--immediate--)では12-bitimmediadを取得し、[` _mov_`](https://developer.arm.com/documentation/dui0802/a/A64-General-Instructions/MOV--wide-immediate-)では16-bitimmediadなどになります。演算子が合致しない場合、アーキテクチャはこれにどのように対処するのでしょうか。場合によってです。特に、`ADD`は「12バイトまでにシフトする」ためのビットを確保しているため、24ビットの加算は2つのオプコードに分解できます。他の指示も同様に分解され、単に最初にレジスタに即時読み込む必要があります。

マシンコードを生成する前のGoコンパイラーの最後のステップには、プログラムを`obj.Prog` structsに変換することが含まれます。これは非常に低レベルの中間表現（IR）であり、ほとんどの場合、マシンコードに変換されます。
    
    
    //https://github.com/golang/go/blob/fa2bb342d7b0024440d996c2d6d6778b7a5e0247/src/cmd/internal/obj/arm64/obj7.go#L856
    
    // Pop stack frame.
    // ADD $framesize, RSP, RSP
    p = obj.Appendp(p, c.newprog)
    p.As = AADD
    p.From.Type = obj.TYPE_CONST
    p.From.Offset = int64(c.autosize)
    p.To.Type = obj.TYPE_REG
    p.To.Reg = REGSP
    p.Spadj = -c.autosize
    

特に、このIRは直接の長さの制限を認識していません。その代わり、これは[ _asm7.go_](https://github.com/golang/go/blob/2f653a5a9e9112ff64f1392ff6e1d404aaf23e8c/src/cmd/internal/obj/arm64/asm7.go)で発生し、Goの内部中間表現がam64マシンコードに変換されます。アセンブラはビットサイズに基づいて[ _コンクラス_](https://github.com/golang/go/blob/2f653a5a9e9112ff64f1392ff6e1d404aaf23e8c/src/cmd/internal/obj/arm64/asm7.go#L1905)の即時を分類し、必要に応じて追加で指示を発行する際にそれを使用します。

Goアクセシビリティは、16ビットの即値に適合する一部のaddに対して（`mov, add` ）オペコードの組み合わせを使用し、16ビット以上の即時にとって（`add, add + lsl 12`）オプコードを優先します。 

`1<<15`より少し大きいスタックを比較する：
    
    
    ; //go:noinline
    ; func big_stack() byte {
    ; 	var big_stack = make([]byte, 1<<15)
    ; 	return big_stack[0]
    ; }
    MOVD $32776, R27
    ADD R27, RSP, R29
    MOVD $32784, R27
    ADD R27, RSP, RSP
    RET
    

`1<<16`のスタックの場合：
    
    
    ; //go:noinline
    ; func big_stack() byte {
    ; 	var big_stack = make([]byte, 1<<16)
    ; 	return big_stack[0]
    ; } 
    ADD $8, RSP, R29
    ADD $(16<<12), R29, R29
    ADD $16, RSP, RSP
    ADD $(16<<12), RSP, RSP
    RET
    

より大きなスタックのケースでは、`ADD x, RSP, RSP` オプコードの間に、スタックポインタがスタックフレームの先端を指していないポイントがあります。私たちは当初、これはメモリの破損の問題だと考えました。非同期のプリエンプションを処理する際に、ランタイムが関数呼び出しをスタックにプッシュし、スタックの中央を破損させるのではないかと思いました。しかし、このゴルーチンはすでに関数エキサイティングにあり、私たちが破損したデータはすべて積極的に破棄されます。では、何が問題なのでしょうか？ 

Goのランタイムは、スタックを**解除する** 必要があることが多いです。それは、関数呼び出しのチェーンを逆方向にたどることを意味します。例えば、ガベージコレクションは、スタック上のライブリファレンスを見つけるために使用し、パニックは`待機`関数を評価するために使用し、スタックトレースを生成するにはコールスタックを表示する必要があります。これが機能するには、スタックポインターが**アンウィンド時に正確でなければなりません** 。これは、golang dereferencesspが呼び出し関数を決定する方法だからです。スタックポインターが部分的に変更された場合、アンウィンダーはスタックの中央にある呼び出し関数を探します。基礎となるデータは、親スタックフレームへの指示として解釈されると意味がなく、その場合ランタイムがクラッシュする可能性が高くなります。
    
    
    //https://github.com/golang/go/blob/66536242fce34787230c42078a7bbd373ef8dcb0/src/runtime/traceback.go#L373
    
    if innermost && frame.sp < frame.fp || frame.lr == 0 {
        lrPtr = frame.sp
        frame.lr = *(*uintptr)(unsafe.Pointer(lrPtr))
    }
    

非同期プリエンプションが発生すると、関数呼び出しをスタックにプッシュしますが、プリエンプションが発生したときspが部分的に調整されただけなので、親スタックフレームは正しくありません。クラッシュのフローは次のようになります： 

  1. 非同期プリエンプションは、`xを追加する`2つのオプコード間で発生し、rspは
  2. ガートナーコレクションがスタックを解読する（Heapオブジェクトの有効性を確認するため）
  3. Unwinderは、問題のあるゴルーチンのスタックを横断し始め、問題のある関数まで正しくアンロックされます。
  4. Unwinder Dereference `sp`設定を用いて親関数を決定
  5. ほぼ間違いなく `sp` の背後にあるデータは関数ではない
  6. クラッシュ



![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2906 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47CNDJH3384G94F2CM4PSM.png&w=715&h=448&f=webp&fit=cover&position=center)

先ほど、`(*NetlinkSocket).Receive` で終了するスタックトレースの異常を確認しました。この場合は、親フレームを決定しようとしている間に、スタックを Cloudflareで仕組みを入手することができました。 
    
    
    goroutine 90 gp=0x40042cc000 m=nil [preempted (scan)]:
    runtime.asyncPreempt2()
    /usr/local/go/src/runtime/preempt.go:306 +0x2c fp=0x40060a25d0 sp=0x40060a25b0 pc=0x55557e299dec
    runtime.asyncPreempt()
    /usr/local/go/src/runtime/preempt_arm64.s:47 +0x9c fp=0x40060a27c0 sp=0x40060a25d0 pc=0x55557e2dc94c
    github.com/vishvananda/netlink/nl.(*NetlinkSocket).Receive(0xff48ce6e060b2848?)
    /vendor/github.com/vishvananda/netlink/nl/nl_linux.go:779 +0x130 fp=0x40060b2820 sp=0x40060a27d0 pc=0x55557e9d2880
    

根本的な原因を特定した後は、それを再現ツールに報告し、バグはすぐに修正されました。このバグは、[ _go1.23.12_](https://github.com/golang/go/commit/e8794e650e05fad07a33fb6e3266a9e677d13fa8)、[ _go1.24.6_](https://github.com/golang/go/commit/6e1c4529e4e00ab58572deceab74cc4057e6f0b6)、および[ _go1.25.0_](https://github.com/golang/go/commit/f7cc61e7d7f77521e073137c6045ba73f66ef902)で修正されています。以前は、goコンパイラーは単一の`add x, rsp`命令を出力し、アセンブラに依存して、必要に応じて即時を複数のopcodeに分割しました。この変更の後、1<<12を超えるスタックは一時的なレジスタにオフセットを構築し、それを単一の不可分なオペコードで`rsp`に加算します。ゴルーチンは、スタックポインタの変更前または変更後にプリエンプションすることができますが、変更中は決して先述できません。つまり、スタックポインターは常に有効であり、競合状態は発生しません。
    
    
    LDP -8(RSP), (R29, R30)
    MOVD $32, R27
    MOVK $(1<<16), R27
    ADD R27, RSP, RSP
    RET

これはデバッグがとても楽しい問題でした。コンパイラーを正確に非難できるバグはあまり見られません。デバッグに数週間かかり、私たちは通常、人が考える必要のないGoランタイムの領域について学びなければなりませんでした。これは、稀な競合状態の良い例であり、大規模でしか定量化できないバグの一種です。

私たちは、このような捜査が好きな人を常に探しています。[ _当社のエンジニアリングチームは募集を行っています_](https://www.cloudflare.com/careers/jobs/?department=Engineering)。 

このページ

オンラインで議論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fhow-we-found-a-bug-in-gos-arm64-compiler%2F&t=Go%E3%81%AEARM64%E3%82%B3%E3%83%B3%E3%83%91%E3%82%A4%E3%83%A9%E3%81%AB%E3%83%90%E3%82%B0%E3%81%8C%E7%99%BA%E8%A6%8B%E3%81%95%E3%82%8C%E3%81%9F%E7%B5%8C%E7%B7%AF)[](https://x.com/intent/post?text=Go%E3%81%AEARM64%E3%82%B3%E3%83%B3%E3%83%91%E3%82%A4%E3%83%A9%E3%81%AB%E3%83%90%E3%82%B0%E3%81%8C%E7%99%BA%E8%A6%8B%E3%81%95%E3%82%8C%E3%81%9F%E7%B5%8C%E7%B7%AF&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fhow-we-found-a-bug-in-gos-arm64-compiler%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fhow-we-found-a-bug-in-gos-arm64-compiler%2F)[](https://bsky.app/intent/compose?text=Go%E3%81%AEARM64%E3%82%B3%E3%83%B3%E3%83%91%E3%82%A4%E3%83%A9%E3%81%AB%E3%83%90%E3%82%B0%E3%81%8C%E7%99%BA%E8%A6%8B%E3%81%95%E3%82%8C%E3%81%9F%E7%B5%8C%E7%B7%AF+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fhow-we-found-a-bug-in-gos-arm64-compiler%2F)[](https://mastodonshare.com/?text=Go%E3%81%AEARM64%E3%82%B3%E3%83%B3%E3%83%91%E3%82%A4%E3%83%A9%E3%81%AB%E3%83%90%E3%82%B0%E3%81%8C%E7%99%BA%E8%A6%8B%E3%81%95%E3%82%8C%E3%81%9F%E7%B5%8C%E7%B7%AF&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fhow-we-found-a-bug-in-gos-arm64-compiler%2F)[](https://www.threads.net/intent/post?text=Go%E3%81%AEARM64%E3%82%B3%E3%83%B3%E3%83%91%E3%82%A4%E3%83%A9%E3%81%AB%E3%83%90%E3%82%B0%E3%81%8C%E7%99%BA%E8%A6%8B%E3%81%95%E3%82%8C%E3%81%9F%E7%B5%8C%E7%B7%AF+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fhow-we-found-a-bug-in-gos-arm64-compiler%2F)

## 関連するタグ

[Go](https://blog.cloudflare.com/ja-jp/tag/go/)[プログラミング](https://blog.cloudflare.com/ja-jp/tag/programming/)[詳細情報](https://blog.cloudflare.com/ja-jp/tag/deep-dive/)

SNS をフォロー

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 新しい投稿のお知らせを受け取るように登録する

メールアドレス

また、あなたのメールアドレスを共有したりすることはございません。

登録する

ご購読ありがとうございます！受信箱を確認して登録してください。
