---
url: https://blog.cloudflare.com/ja-jp/programmable-packet-filtering-with-magic-firewall/
title: Cloudflare\u304cMagic Firewall\u3067\u3001\u30d7\u30ed\u30b0\u30e9\u30e0\u53ef\u80fd\u306a\u30d1\u30b1\u30c3\u30c8\u30d5\u30a3\u30eb\u30bf\u30fc\u3092eBPF\u3092\u4f7f\u3063\u3066\u3069\u306e\u3088\u3046\u306b\u69cb\u7bc9\u3057\u3066\u3044\u308b\u304b | Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:46:15.810305+00:00
---

# CloudflareがMagic Firewallで、プログラム可能なパケットフィルターをeBPFを使ってどのように構築しているか | Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/programmable-packet-filtering-with-magic-firewall/

[ブログ](https://blog.cloudflare.com/ja-jp/)

[CIO Week](https://blog.cloudflare.com/ja-jp/tag/cio-week/)[eBPF](https://blog.cloudflare.com/ja-jp/tag/ebpf/)[Magic Firewall](https://blog.cloudflare.com/ja-jp/tag/magic-firewall/)3件3件タグを表示

6 タグタグを6件表示

  * 投稿タグ
  * [CIO Week](https://blog.cloudflare.com/ja-jp/tag/cio-week/)[eBPF](https://blog.cloudflare.com/ja-jp/tag/ebpf/)[Magic Transit](https://blog.cloudflare.com/ja-jp/tag/magic-transit/)[セキュリティ](https://blog.cloudflare.com/ja-jp/tag/security/)
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



[Magic Transit](https://blog.cloudflare.com/ja-jp/tag/magic-transit/)[VoIP](https://blog.cloudflare.com/ja-jp/tag/voip/)[セキュリティ](https://blog.cloudflare.com/ja-jp/tag/security/)

[CIO Week](https://blog.cloudflare.com/ja-jp/tag/cio-week/)[eBPF](https://blog.cloudflare.com/ja-jp/tag/ebpf/)[Magic Firewall](https://blog.cloudflare.com/ja-jp/tag/magic-firewall/)[Magic Transit](https://blog.cloudflare.com/ja-jp/tag/magic-transit/)[VoIP](https://blog.cloudflare.com/ja-jp/tag/voip/)[セキュリティ](https://blog.cloudflare.com/ja-jp/tag/security/)

2021年12月6日

# CloudflareがMagic Firewallで、プログラム可能なパケットフィルターをeBPFを使ってどのように構築しているか

![Chris J Arges](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4865BZM73VVEYNTQ0VZBR4.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Chris J Arges](https://blog.cloudflare.com/ja-jp/author/arges/)

8分で読了

URLをコピー

この記事は以下でも利用可能です [English](https://blog.cloudflare.com/programmable-packet-filtering-with-magic-firewall/)、[简体中文](https://blog.cloudflare.com/zh-cn/programmable-packet-filtering-with-magic-firewall/)、[Bahasa Indonesia](https://blog.cloudflare.com/id-id/programmable-packet-filtering-with-magic-firewall/)、[ภาษาไทย](https://blog.cloudflare.com/th-th/programmable-packet-filtering-with-magic-firewall/).

![How We Used eBPF to Build Programmable Packet Filtering in Magic Firewall](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44K5JZN9SGZA4NJKEMXA99.png&w=1801&h=1013&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/////v3/9PLz7+vp8u3p9vLu8/Dv6+rs////////9fPz7+zo8e3n9fHt8/Hv7Ovt////////+Pf18e/p8u/n9fPs9PPw7u7w////////+/z59PPt9fPr+Pfw9/f08vP1////////////+vr0+vrz/f34/P379/j6///////////////8///9////////+/7/////////////////////////////////////////////////////////////////)

クラウドフレアは、日々巧妙な攻撃から積極的にサービスを守っています。Magic Transitのユーザーの場合、DDoS保護対策が攻撃を検知してドロップする一方で、[Magic Firewall](https://www.cloudflare.com/ja-jp/magic-firewall/)によってパケットレベルのカスタムルールが可能なため、お客様はハードウェアファイアウォール機器を廃止してCloudflareのネットワークで悪意のあるトラフィックをブロックできるようになります。[Session Initiation Protocol](https://en.wikipedia.org/wiki/Session_Initiation_Protocol)(SIP) などのプロトコルを標的とした攻撃が示すように、VoIPに[対する攻撃](https://blog.cloudflare.com/ja-jp/attacks-on-voip-providers-ja-jp/)の種類は最近のDDos攻撃やリフレクター攻撃として進化し続けています。このような攻撃に対抗するためには、従来のファイアウォールでは不可能なパケットフィルタリングの限界に挑戦する必要があります。私たちは、クラス最高の技術を取り入れ、それらを新しい方法で組み合わせることで、Magic Firewallを最も巧妙な攻撃にも耐えることができる、非常に高速で完全にプログラム可能なファイアウォールに変身させることができました。

### **マジカルウォール・オブ・ファイヤー**

[Magic Firewall](https://blog.cloudflare.com/ja-jp/introducing-magic-firewall-ja-jp/)は、Linuxのnftablesをベースに構築された分散型ステートレスパケットファイアウォールです。世界中のCloudflareデータセンターにあるすべてのサーバーで稼働しています。分離と柔軟性を提供するため、各お客様のnftablesルールはLinuxネットワークの名前空間内で構成されます。

この図は、Magic Firewallを組み込んだ [Magic Transit](https://blog.cloudflare.com/ja-jp/magic-transit-network-functions-ja-jp/)を使用した場合のパケットの一例を示しています。まず、パケットはサーバーに入り、DDoS防御が適用され、攻撃を可能な限り早期にドロップします。次に、パケットはお客様専用のネットワークネームスペースにルーティングされ、nftablesのルールがパケットに適用されます。この後、パケットはGREトンネルを経由して元の場所にルートバックされます。Magic Firewallのユーザーは、柔軟な[Wirefilter構文](https://github.com/cloudflare/wirefilter)を使用して[シングルAPI](https://developers.cloudflare.com/magic-firewall)からファイアウォール文を構築することができます。さらに、ルールはCloudflareダッシュボードから、使いやすいUIのドラッグ＆ドロップ要素を使用して設定することができます。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![This diagram shows how packets are processed by Magic Firewall on a Cloudflare server.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48R9WMZ6CW711ZX84DH9QX.png&w=715&h=372&f=webp&fit=cover&position=center)

Magic Firewallは、様々なパケットパラメータにマッチする非常に強力な構文を提供しますが、nftablesが提供するマッチにも制限されます。多くのユースケースではこれで十分すぎるほどなのですが、私たちが望む高度なパケット解析やコンテンツマッチングを実装するには十分な柔軟性を備えているとは言えません。私たちはもっと大きな力を必要としていました。

### **eBPFの皆さん、こんにちは！Nftablesです。**

Linux のネットワークにさらなるパワーを求める場合、Extended Berkeley Packet Filter ( [eBPF](https://ebpf.io/) ) は当然の選択と言えます。eBPFでは、カーネル内で実行されるパケット処理プログラム _を挿入でき、_カーネル内実行の速度と、使い慣れたプログラミングパラダイムによる柔軟性を提供します。Cloudflareは[eBPF が大好きで](https://blog.cloudflare.com/tag/ebpf/)、このテクノロジーは当社の多くの製品を実現する上で大きな変革をもたらしています。私たちがeBPFを使ってMagic Firewallのnftablesの使い方を拡張する方法を見つけたのも当然のことと言えます。つまり、テーブルの中でeBPFプログラムを使ってマッチングし、ルールとして連鎖させることができるようになるのです。こうすることで、既存のインフラとコードを維持したまま、さらに拡張することができます。私たちはケーキを持ちながら、さらにそれを食べることができるのです。

もしnftablesがeBPFをネイティブに活用できれば、この話はもっと短くなるはずですが、残念ながら、私たちは探求を続けなければなりませんでした。探索を始めるにあたって、iptablesがeBPFと統合されていることは知っています。例えば、次のコマンドでパケットをドロップするためにiptablesと固定されたeBPFプログラムを使用することができます。

このヒントのおかげで、正しい道に進むことができました。Iptablesは [xt_bpf](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/net/netfilter/xt_bpf.c#n60)拡張を使用して、eBPFプログラムでマッチングします。この拡張機能はBPF_PROG_TYPE_SOCKET_FILTER eBPFプログラムタイプを使用し、ソケットバッファからパケット情報をロードして、コードに基づいた値を返すことができます。
    
    
    iptables -A INPUT -m bpf --object-pinned /sys/fs/bpf/match -j DROP

iptablesがeBPFを使えることが分かっているのだから、それを使えばいいのでは？Magic Firewallは現在 nftablesを利用していますが、これは構文の柔軟性とプログラム可能なインターフェイスのため、私たちのユースケースには最適な選択です。したがって、xt_bpf拡張をnftablesで使用する方法を見つける必要があります。

この[図](https://developers.redhat.com/blog/2020/08/18/iptables-the-two-variants-and-their-relationship-with-nftables#using_iptables_nft)は、iptables、nftables、カーネル間の関係を説明するのに役立ちます。nftables APIはiptablesとnftの両方のユーザー空間プログラムで使用でき、 xtablesのマッチ（xt_bpf を含む）と通常のnftablesのマッチの両方を設定できます。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-849 Embedded Image - BzET9q](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46K5HWGDGVFGANF0A6D7MF.png&w=715&h=536&f=webp&fit=cover&position=center)

つまり、正しいAPIコール（netlink/netfilterメッセージ）があれば、nftablesルール内にxt_bpfマッチを埋め込むことができるのです。これを行うには、どのnetfilterメッセージを送信する必要があるかを理解する必要があります。straceやWiresharkなどのツールを使い、特に[ソース](https://github.com/torvalds/linux/blob/master/net/netfilter/xt_bpf.c)を使って、テーブルとチェーンを指定してeBPFルールを追加できるメッセージを作成することができました。

eBPFマッチを追加するためのnetlink/netfilterメッセージの構造は、上記の例のようになるはずです。もちろん、このメッセージは適切に埋め込まれ、一致したときの評決などの条件付きステップを含む必要があります。次のステップは、下の例のように `ebpf_bytes` の形式をデコードすることでした。
    
    
    NFTA_RULE_TABLE table
    NFTA_RULE_CHAIN chain
    NFTA_RULE_EXPRESSIONS | NFTA_MATCH_NAME
    	NFTA_LIST_ELEM | NLA_F_NESTED
    	NFTA_EXPR_NAME "match"
    		NLA_F_NESTED | NFTA_EXPR_DATA
    		NFTA_MATCH_NAME "bpf"
    		NFTA_MATCH_REV 1
    		NFTA_MATCH_INFO ebpf_bytes	

バイトのフォーマットは、[struct xt_bpf_info_v1](https://git.netfilter.org/iptables/tree/include/linux/netfilter/xt_bpf.h#n27)のカーネルヘッダー定義にあります。上記のコード例は、構造体の関連部分を示しています。
    
    
     struct xt_bpf_info_v1 {
    	__u16 mode;
    	__u16 bpf_program_num_elem;
    	__s32 fd;
    	union {
    		struct sock_filter bpf_program[XT_BPF_MAX_NUM_INSTR];
    		char path[XT_BPF_PATH_MAX];
    	};
    };

xt_bpfモジュールは生のバイトコードと、ピン留めされたebpfプログラムへのパスの両方をサポートしています。後者のモードは、ebpfプログラムをnftablesと結合するために使用した手法です。

この情報をもとに、ネットリンクメッセージを作成し、関連するデータフィールドを適切にシリアライズするコードを作成することができました。このアプローチは最初のステップに過ぎません。私たちは、カスタムのネットフィルタメッセージを送る代わりに、これを適切なツールに取り入れることも検討しています。

### **eBPFを追加するだけ**

あとは、eBPFのプログラムを組み立てて、既存のnftablesのテーブルとチェーンにロードする必要がありました。eBPFを使い始めるのは少し難しいかもしれません。どのプログラムタイプを使えばいいのか？eBPFのプログラムをどのようにコンパイルし、ロードすればよいのか？私たちは、このプロセスを、いくつかの調査と研究によって開始しました。

まず、試しにサンプルプログラムを構築してみました。

ご紹介したのは、ペイロードの末尾にマジック文字列を持つパケットのみを受け付けるeBPFプログラムの一例です。これは、検索を開始する場所を見つけるために、パケットの全長をチェックする必要があります。わかりやすくするために、この例ではエラーチェックとヘッダーを省略しています。
    
    
    SEC("socket")
    int filter(struct __sk_buff *skb) {
      /* get header */
      struct iphdr iph;
      if (bpf_skb_load_bytes(skb, 0, &iph, sizeof(iph))) {
        return BPF_DROP;
      }
    
      /* read last 5 bytes in payload of udp */
      __u16 pkt_len = bswap_16(iph.tot_len);
      char data[5];
      if (bpf_skb_load_bytes(skb, pkt_len - sizeof(data), &data, sizeof(data))) {
        return BPF_DROP;
      }
    
      /* only packets with the magic word at the end of the payload are allowed */
      const char SECRET_TOKEN[5] = "xyzzy";
      for (int i = 0; i < sizeof(SECRET_TOKEN); i++) {
        if (SECRET_TOKEN[i] != data[i]) {
          return BPF_DROP;
        }
      }
    
      return BPF_OK;
    }

プログラムができたら、次はそれを我々のツールに統合することでした。プログラムをロードするために、BCCやlibbpfなどいくつかの技術を試し、カスタムのローダーも作りました。最終的には、 [ciliumのebpfライブラリ](https://github.com/cilium/ebpf/)を使うことにしました。私たちは制御プレーンのプログラムにGolangを使っており、このライブラリによってeBPFプログラムの生成、埋め込み、読み込みが簡単にできるからです。

プログラムをコンパイルしてピン留めすれば、netlinkコマンドを使ってnftablesにマッチを追加することができます。ルールセットをリストアップすると、マッチが存在することがわかります。これは信じられないことです。Magic Firewallのルールセット内に高度なマッチングを提供するカスタムCプログラムをデプロイできるようになったのです!
    
    
    # nft list ruleset
    table ip mfw {
    	chain input {
    		#match bpf pinned /sys/fs/bpf/mfw/match drop
    	}
    }

### **その他のマジック**

eBPFをツールキットに加えることで、Magic Firewallはあなたのネットワークを悪者から守るための、より柔軟で強力な方法となります。パケットをより深く調べ、nftablesだけでは実現できないような複雑なマッチングロジックを実装することができるようになりました。私たちのファイアウォールはすべてのCloudflareサーバー上でソフトウェアとして動作しているため、迅速に反復して機能を更新することができます。

このプロジェクトの成果のひとつが、現在ベータ版として公開されているSIPプロテクションです。これはまだ始まりに過ぎません。現在、プロトコルの検証、高度なフィールドマッチング、ペイロードの調査、さらに大規模なIPリストのセットのサポートにeBPFを使用することを検討しています。

こちらもぜひご協力をお願いします。他の使用例やアイデアがある場合は、担当のアカウントチームに相談してください。この技術に興味を持たれた方は、ぜひ [私たちのチームに参加してください](https://www.cloudflare.com/ja-jp/careers/) !

**[Twitterでつぶやく](https://twitter.com/intent/tweet?in_reply_to=1467870195343634433)[Hacker Newsで話し合う](https://news.ycombinator.com/item?id=29459826)[Redditで話し合う](https://reddit.com/r/CloudFlare/comments/ra8cno/how_we_used_ebpf_to_build_programmable_packet/)**

[CIO Week](https://blog.cloudflare.com/tag/cio-week/) [Magic Firewall](https://blog.cloudflare.com/tag/magic-firewall/) [Magic Transit](https://blog.cloudflare.com/tag/magic-transit/) [セキュリティ](https://blog.cloudflare.com/tag/security/) [VoIP](https://blog.cloudflare.com/tag/voip/)

Twitterでフォロー

Chris J Arges |[@ChrisArges](https://twitter.com/@ChrisArges)

Cloudflare |[Cloudflare](https://twitter.com/Cloudflare)

このページ

オンラインで議論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fprogrammable-packet-filtering-with-magic-firewall%2F&t=Cloudflare%E3%81%8CMagic%20Firewall%E3%81%A7%E3%80%81%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0%E5%8F%AF%E8%83%BD%E3%81%AA%E3%83%91%E3%82%B1%E3%83%83%E3%83%88%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF%E3%83%BC%E3%82%92eBPF%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%81%A9%E3%81%AE%E3%82%88%E3%81%86%E3%81%AB%E6%A7%8B%E7%AF%89%E3%81%97%E3%81%A6%E3%81%84%E3%82%8B%E3%81%8B)[](https://x.com/intent/post?text=Cloudflare%E3%81%8CMagic+Firewall%E3%81%A7%E3%80%81%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0%E5%8F%AF%E8%83%BD%E3%81%AA%E3%83%91%E3%82%B1%E3%83%83%E3%83%88%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF%E3%83%BC%E3%82%92eBPF%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%81%A9%E3%81%AE%E3%82%88%E3%81%86%E3%81%AB%E6%A7%8B%E7%AF%89%E3%81%97%E3%81%A6%E3%81%84%E3%82%8B%E3%81%8B&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fprogrammable-packet-filtering-with-magic-firewall%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fprogrammable-packet-filtering-with-magic-firewall%2F)[](https://bsky.app/intent/compose?text=Cloudflare%E3%81%8CMagic+Firewall%E3%81%A7%E3%80%81%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0%E5%8F%AF%E8%83%BD%E3%81%AA%E3%83%91%E3%82%B1%E3%83%83%E3%83%88%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF%E3%83%BC%E3%82%92eBPF%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%81%A9%E3%81%AE%E3%82%88%E3%81%86%E3%81%AB%E6%A7%8B%E7%AF%89%E3%81%97%E3%81%A6%E3%81%84%E3%82%8B%E3%81%8B+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fprogrammable-packet-filtering-with-magic-firewall%2F)[](https://mastodonshare.com/?text=Cloudflare%E3%81%8CMagic+Firewall%E3%81%A7%E3%80%81%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0%E5%8F%AF%E8%83%BD%E3%81%AA%E3%83%91%E3%82%B1%E3%83%83%E3%83%88%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF%E3%83%BC%E3%82%92eBPF%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%81%A9%E3%81%AE%E3%82%88%E3%81%86%E3%81%AB%E6%A7%8B%E7%AF%89%E3%81%97%E3%81%A6%E3%81%84%E3%82%8B%E3%81%8B&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fprogrammable-packet-filtering-with-magic-firewall%2F)[](https://www.threads.net/intent/post?text=Cloudflare%E3%81%8CMagic+Firewall%E3%81%A7%E3%80%81%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0%E5%8F%AF%E8%83%BD%E3%81%AA%E3%83%91%E3%82%B1%E3%83%83%E3%83%88%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF%E3%83%BC%E3%82%92eBPF%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%81%A9%E3%81%AE%E3%82%88%E3%81%86%E3%81%AB%E6%A7%8B%E7%AF%89%E3%81%97%E3%81%A6%E3%81%84%E3%82%8B%E3%81%8B+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fprogrammable-packet-filtering-with-magic-firewall%2F)

## 関連するタグ

[CIO Week](https://blog.cloudflare.com/ja-jp/tag/cio-week/)[eBPF](https://blog.cloudflare.com/ja-jp/tag/ebpf/)[Magic Firewall](https://blog.cloudflare.com/ja-jp/tag/magic-firewall/)[Magic Transit](https://blog.cloudflare.com/ja-jp/tag/magic-transit/)[VoIP](https://blog.cloudflare.com/ja-jp/tag/voip/)[セキュリティ](https://blog.cloudflare.com/ja-jp/tag/security/)

SNS をフォロー

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 新しい投稿のお知らせを受け取るように登録する

メールアドレス

また、あなたのメールアドレスを共有したりすることはございません。

登録する

ご購読ありがとうございます！受信箱を確認して登録してください。
