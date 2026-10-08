---
url: https://blog.cloudflare.com/ja-jp/how-we-built-spectrum/
title: Linux\u306e\u30d5\u30a1\u30a4\u30a2\u30a6\u30a9\u30fc\u30eb\u306e\u4e71\u7528\uff1aSpectrum\u306e\u69cb\u7bc9\u3092\u53ef\u80fd\u306b\u3057\u305f\u88cf\u6280\u306b\u3064\u3044\u3066 | Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:48:25.329679+00:00
---

# Linuxのファイアウォールの乱用：Spectrumの構築を可能にした裏技について | Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/how-we-built-spectrum/

[ブログ](https://blog.cloudflare.com/ja-jp/)

[DDoS](https://blog.cloudflare.com/ja-jp/tag/ddos/)[Linux](https://blog.cloudflare.com/ja-jp/tag/linux/)[Spectrum](https://blog.cloudflare.com/ja-jp/tag/spectrum/)3件3件タグを表示

6 タグタグを6件表示

  * 投稿タグ
  * [DDoS](https://blog.cloudflare.com/ja-jp/tag/ddos/)[Linux](https://blog.cloudflare.com/ja-jp/tag/linux/)[Spectrum](https://blog.cloudflare.com/ja-jp/tag/spectrum/)[スピードと信頼性](https://blog.cloudflare.com/ja-jp/tag/speed-and-reliability/)[セキュリティ](https://blog.cloudflare.com/ja-jp/tag/security/)[製品ニュース](https://blog.cloudflare.com/ja-jp/tag/product-news/)
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



[スピードと信頼性](https://blog.cloudflare.com/ja-jp/tag/speed-and-reliability/)[セキュリティ](https://blog.cloudflare.com/ja-jp/tag/security/)[製品ニュース](https://blog.cloudflare.com/ja-jp/tag/product-news/)

[DDoS](https://blog.cloudflare.com/ja-jp/tag/ddos/)[Linux](https://blog.cloudflare.com/ja-jp/tag/linux/)[Spectrum](https://blog.cloudflare.com/ja-jp/tag/spectrum/)[スピードと信頼性](https://blog.cloudflare.com/ja-jp/tag/speed-and-reliability/)[セキュリティ](https://blog.cloudflare.com/ja-jp/tag/security/)[製品ニュース](https://blog.cloudflare.com/ja-jp/tag/product-news/)

2018年4月12日

# Linuxのファイアウォールの乱用：Spectrumの構築を可能にした裏技について

![Marek Majkowski](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44F10W94YWR7RW8E70MQW4.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Marek Majkowski](https://blog.cloudflare.com/ja-jp/author/marek-majkowski/)

9分で読了

URLをコピー

この記事は以下でも利用可能です [English](https://blog.cloudflare.com/how-we-built-spectrum/)、[Deutsch](https://blog.cloudflare.com/de-de/how-we-built-spectrum/)、[Español](https://blog.cloudflare.com/es-es/how-we-built-spectrum/)、[Français](https://blog.cloudflare.com/fr-fr/how-we-built-spectrum/)、[한국어](https://blog.cloudflare.com/ko-kr/how-we-built-spectrum/)、[简体中文](https://blog.cloudflare.com/zh-cn/how-we-built-spectrum/).

![13334109713_0b32435032_z](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44E12BDNQKMKCCGSM4BXZA.jpg&w=640&h=425&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAAmZacm5menJyglpebioqQg4KKioqRmJqflZCUlpKWlJOViomLeHZ6cGx0f3yDlZWYjoeKjomKioiGenh2YFpdV0tUcWpvj42Ph3+Bh4GBgn98cG1pUEdIQy46ZFpgh4SFgXp8gn19f357cG9sVk9RSDZEX1RefXl8fHd8fnx+gIKBeXt6aWZrXFJgYlpncnB3eXd+fX2Cg4eIg4eIenqAbWh2Z2Jyamp0eHd/fX6DhYqLh4yOgIGIdHB+amZ2Z2h0)

Cloudflareは本日、[Spectrumの提供を開始](https://blog.cloudflare.com/spectrum/)します。Spectrumは、TCPベースのプロトコル向けのCloudflareの新たな機能で、DDoS攻撃に対する防御、ロードバランシング、およびコンテンツ高速化を実現します。

[CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/) [画像](https://www.flickr.com/photos/liftarn/13334109713)作者[Staffan Vilcans](https://www.flickr.com/photos/liftarn)

Spectrumの構築を開始した直後、私たちは大きな技術的障害にぶつかりました。Spectrumでは、有効なTCPポート（1～65535）で接続を受け入れる必要があります。当社のLinuxエッジサーバーでは、「_任意の_ポート番号で着信接続を受け入れる」ことは不可能です。これはLinux固有の制限ではなく、ほとんどのオペレーティングシステムのネットワークアプリケーションの基礎である、BSDソケットAPIの特性です。実は、Spectrumを提供するために解決しなければならなかった、以下の2つの互いに関わりあう問題がありました。

  * 1～65535のすべてのポート番号でTCP接続を受け入れる方法
  * 単一Linuxサーバーに、きわめて多数のIPアドレスでの接続を受け入れるよう設定する方法（当社のエニーキャスト範囲内には数千のIPアドレスが存在）



### **サーバーへの数百万IPの割り当て**

Cloudflareでは、すべてのエッジサーバーがほぼ同じ設定になっています。当社の初期の頃には、ループバックネットワークインタフェースに一定の/32（および/128）IPアドレスを割り当てていました[[1]](https://blog.cloudflare.com/how-we-built-spectrum/#fn1)。IPアドレスの単位が数十のうちは上手くいきましたが、会社の成長に伴って規模の拡張に失敗しました。

同時に[「AnyIP」のトリック](https://blog.widodh.nl/2016/04/anyip-bind-a-whole-subnet-to-your-linux-machine/)も問題になりました。AnyIPを使用すると、一定のIPアドレスから拡張し、IPプレフィックス（サブネット）全体のループバックインタフェースへの割り当てが可能になります。すでにAnyIPは広く利用されており、皆さんのコンピューターにはループバックインタフェースに127.0.0.0/8が割り当てられています。ユーザーのコンピューター側から見た場合、127.0.0.1から127.255.255.254までのすべてのIPアドレスはローカルマシンに属しています。

このトリックは、127.0.0.1/8ブロック以外にも適用可能です。192.0.2.0/24の範囲全体をローカルに割り当てたものとして扱うには、次を実行します。
    
    
    ip route add local 192.0.2.0/24 dev lo

`ip route add local 192.0.2.0/24 dev lo`
    
    
    nc -l 192.0.2.1 8080

次に、これらのIPアドレスの1つでポート8080にバインドすることができます。
    
    
    ip route add local 2001:db8::/64 dev lo

`nc -l 192.0.2.1 8080`

IPv6を動作させるのは少し難しくなります。
    
    
    $ ip addr show
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536
        inet 1.1.1.0/24 scope global lo
           valid_lft forever preferred_lft forever
        inet 104.16.0.0/16 scope global lo
           valid_lft forever preferred_lft forever
    ...

`ip route add local 2001:db8::/64 dev lo`

残念ながら、これらのアタッチされたv6IPアドレスには、v4の例のようにバインドすることはできません。これを機能させるには、さらに上の権限が必要な `IP_FREEBIND` ソケットオプションを使用する必要があります。完全性を確保するためにsysctl `net.ipv6.ip_nonlocal_bind`を使う方法もありますが、ここで触れることはお勧めしません。

このAnyIPのトリックを使用すると、数百万のIPアドレスを各サーバーにローカルに割り当てることができます。

### **すべてのポートへのバインド**

2つ目の大きな問題は、任意のポート番号に対してTCPソケットを開く機能です。Linuxおよび、一般にBSDソケットAPIをサポートしている任意のシステムでは、特定のTCPポート番号へのバインドは、単一のバインドシステム呼び出しでしか行うことができません。単一操作で複数ポートへのバインドは不可能です。
    
    
    /* Yes, really, this is all you need. */
    #define INET_LHTABLE_SIZE       32

単純に考えると、65535のポートに、1回ずつ、65535回バインドすることになります。確かにこのような方法もあったかもしれませんが、これは次のような酷い結果につながります。

  * [リスニングソケットの復讐](https://blog.cloudflare.com/revenge-listening-sockets/)



内部的には、Linuxカーネルは、正確に32バケットを使用して、ポート番号でインデックスを指定したリスニングソケットをハッシュテーブル[LHTABLE](https://elixir.bootlin.com/linux/latest/source/include/net/inet_hashtables.h#L118)に保存します。

`/* はい、本当に、これが必要なすべてです。 */`

`#define INET_LHTABLE_SIZE 32`

65,000のポートを開いていたら、このテーブルのルックアップには長い長い時間がかかったでしょう。ハッシュテーブルの各バケットには2,000のアイテムが入っているからです。

問題を解決するもう1つの方法は、iptablesの豊富なNAT機能の使用です。一部の特定のアドレス／ポートへの着信パケットの宛先を書き換えて、アプリケーションをそれにバインドさせることができます。

しかし、これにはiptablesのconntrackモジュールを有効にする必要があるため、この方法は採りませんでした。過去には[パフォーマンスエッジケース](http://patchwork.ozlabs.org/cover/810566/)があり、conntrackは当社が被った大規模なDDoS攻撃の一部には対処できませんでした。

さらに、NATアプローチでは、宛先IPアドレス情報が失われる可能性があります。これを緩和するためにあまり知られていないSO_ORIGINAL_DSTソケットオプションもありますが、[あまり使いたくなるようなコードではありません](https://github.com/torvalds/linux/blob/b5dbc28762fd3fd40ba76303be0c7f707826f982/net/ipv4/netfilter/nf_conntrack_l3proto_ipv4.c)。

幸い、65000のポートすべてをバインドするもしくは `conntrack`を使用する以外の方法で、目標を達成する方法があります。

### **ファイアウォールで対応**

先に進む前に、オペレーティングシステム上でのネットワークパケットの流れについて復習しておきましょう。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![upload-1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45V16KF1141QKP2QTJM6F1.jpg&w=640&h=360&f=webp&fit=cover&position=center)

一般に、受信パケットの経路には次の2つの異なる層があります。

  * IPファイアウォール
  * ネットワークスタック


    
    
    TPROXY
    This target is only valid in the mangle table, in the 
    PREROUTING chain and user-defined chains which are only 
    called from this chain.  It redirects the packet to a local 
    socket without changing the packet header in any way. It can
    also change the mark value which can then be used in 
    advanced routing rules. 

これらは概念的に異なるものです。IPファイアウォールは通常、ステートレスなソフトウェアです（ここでは、conntrackとIPフラグメントの再構築は無視します）。ファイアウォールはIPパケットを分析し、それらを受け入れるかドロップするかを決定します。注意：この層では、_アプリケーションやソケットではなく、パケットとポート番号_を話題にしています。

次に、ネットワークスタックがあります。ここには多くの状態が維持されています。ネットワークスタックの主なタスクは、受信するIPパケットを_ソケット_にディスパッチすることで、パケットはユーザー空間の_アプリケーション_によって処理されます。ネットワークスタックは、ユーザー空間と共有される抽象化を管理しています。TCPフローを再構成し、ルーティングを処理し、ローカルなIPアドレスを認識します。

### **魔法の粉**

出典：[こちらもYouTube](https://www.youtube.com/watch?v=9CS7j5I6aOc)

ある時点で、TPROXY iptablesモジュールに偶然行き当たりました。[公式ドキュメント](http://ipset.netfilter.org/iptables-extensions.man.html)は見落としてしまいやすいです。

カーネルには、別に、次のドキュメントもあります。
    
    
    case NFT_LOOKUP_LISTENER:
      sk = inet_lookup_listener(net, &tcp_hashinfo, skb,
    				    ip_hdrlen(skb) +
    				      __tcp_hdrlen(tcph),
    				    saddr, sport,
    				    daddr, dport,
    				    in->ifindex, 0);

  * [docs/networking/tproxy.txt](https://www.kernel.org/doc/Documentation/networking/tproxy.txt)



考えるほど、もっと知りたくなりました。

つまり...TPROXYは実際に何を_する_のかということです。
    
    
    skb->sk = sk;

### **魔法のトリックを明らかにする**

TPROXYコードは[驚くほど単純](https://elixir.bootlin.com/linux/v4.16.1/source/net/netfilter/xt_TPROXY.c#L119)です。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![3649474619_3b800400e9_z-1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW475B6E6KWBFRMM268YX25R.jpg&w=640&h=424&f=webp&fit=cover&position=center)

声に出して読み上げます。ファイアウォールの一部であるiptablesモジュールでは、私たちはinet_lookup_listenerと呼んでいます。この機能はsrc/dst port/IP 4-tupleを使い、接続を受け入れることのできるリスニングソケットを戻します。これは、ネットワークスタックのソケットディスパッチのコア機能です。

繰り返します。ファイアウォールコードはソケットディスパッチルーチンを呼び出します。
    
    
    # Set 192.0.2.0/24 to be routed locally with AnyIP.
    # Make it explicit that the source IP used for this network
    # when connecting locally should be in 127.0.0.0/8 range.
    # This is needed since otherwise the TPROXY rule would match
    # both forward and backward traffic. We want it to catch 
    # forward traffic only.
    sudo ip route add local 192.0.2.0/24 dev lo src 127.0.0.1
    
    # Set the magical TPROXY routing
    sudo iptables -t mangle -I PREROUTING \
            -d 192.0.2.0/24 -p tcp \
            -j TPROXY --on-port=1234 --on-ip=127.0.0.1

この後、[TPROXYは実際にソケットディスパッチを_行います_](https://elixir.bootlin.com/linux/v4.16.1/source/net/netfilter/xt_TPROXY.c#L299)。
    
    
    IP_TRANSPARENT (since Linux 2.6.24)
    Setting this boolean option enables transparent proxying on
    this socket.  This socket option allows the calling applica‐
    tion to bind to a nonlocal IP address and operate both as a
    client and a server with the foreign address as the local
    end‐point.  NOTE: this requires that routing be set up in
    a way that packets going to the foreign address are routed 
    through the TProxy box (i.e., the system hosting the 
    application that employs the IP_TRANSPARENT socket option).
    Enabling this socket option requires superuser privileges
    (the CAP_NET_ADMIN capability).
    
    TProxy redirection with the iptables TPROXY target also
    requires that this option be set on the redirected socket.

`skb->sk = sk;`
    
    
    import socket
    
    IP_TRANSPARENT = 19
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setsockopt(socket.IPPROTO_IP, IP_TRANSPARENT, 1)
    
    s.bind(('127.0.0.1', 1234))
    s.listen(32)
    print("[+] Bound to tcp://127.0.0.1:1234")
    while True:
        c, (r_ip, r_port) = s.accept()
        l_ip, l_port = c.getsockname()
        print("[ ] Connection from tcp://%s:%d to tcp://%s:%d" % (r_ip, r_port, l_ip, l_port))
        c.send(b"hello world\n")
        c.close()

この行は、 socket `struct sock`をインバウンドパケットに割り当てて、ディスパッチを完了します。
    
    
    $ nc -v 192.0.2.1 9999
    Connection to 192.0.2.1 9999 port [tcp/*] succeeded!
    hello world

### **帽子からウサギを取り出す**
    
    
     $ sudo python3 transparent2.py
    [+] Bound to tcp://127.0.0.1:1234
    [ ] Connection from tcp://127.0.0.1:60036 to tcp://192.0.2.1:9999

[CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/) [画像](https://www.flickr.com/photos/angelaboothroyd/3649474619)作者[Angela Boothroyd](https://www.flickr.com/photos/angelaboothroyd)

TPROXYで武装することで、bind-to-all-portsのトリックをきわめて容易に実行することができます。構成を次に示します。

この設定に加えて、魔法のIP_TRANSPARENTソケットオプションでTCPサーバーを起動する必要があります。次の例は、tcp://127.0.0.1:1234でリッスンする必要があります。[IP_TRANSPARENTのマニュアルページ](http://man7.org/linux/man-pages/man7/ip.7.html)には、次のように掲載されています。

シンプルなPythonサーバーを次に示します。

サーバーの実行後は、任意のIPアドレスからサーバーに接続できます。

最も重要なのは、サーバーは接続をレポートし、_誰もそのIPアドレスおよびポートをリッスンしていないにも関わらず、_192.0.2.1ポート9999にダイレクトされたことです。

いかがでしょう！これが、conntrackを使用せずにLinux上の任意のポートに_バインドする方法です。_

### **これがすべてです**

この記事では、元々透過的プロキシ用に設計されたものを少し違う用途で使用するための、目立たないiptablesモジュールの使用方法を説明しました。このモジュールを借りて、標準のBSDソケットAPIを使用して不可能と思われたことを実行することができ、カスタムのカーネルによるパッチを使う必要性も回避することができます。

TPROXYモジュールは非常に珍しく、Linuxのファイアウォールの文脈では基本的にLinuxのネットワークスタックが実行することを実行します。公式ドキュメントが幾分不足しており、このモジュールの本当の力を理解しているLinuxユーザーはそれほど多くないと思われます。

TPROXYにより、vanillaカーネル上で当社のSpectrum製品がスムーズに動作すると言って良いでしょう。。また、iptablesとネットワークスタックについて理解することが、いかに重要かについても覚えておくとよいでしょう。

* * *

 _低レベルのソケットの作業に興味をお持ちですか？ロンドン、オースティン、サンフランシスコの[世界的に有名なチーム](https://boards.greenhouse.io/cloudflare/jobs/589572)、ポーランドのワルシャワの精鋭部隊に、ぜひご参加ください。_

* * *

  1. IPアドレスを、appropriate rp_filterおよびBGP構成でループバックインタフェースに割り当てることで、任意のIP範囲を当社エッジサーバーで処理することができます。[↩︎](https://blog.cloudflare.com/how-we-built-spectrum/#fnref1)



このページ

オンラインで議論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fhow-we-built-spectrum%2F&t=Linux%E3%81%AE%E3%83%95%E3%82%A1%E3%82%A4%E3%82%A2%E3%82%A6%E3%82%A9%E3%83%BC%E3%83%AB%E3%81%AE%E4%B9%B1%E7%94%A8%EF%BC%9ASpectrum%E3%81%AE%E6%A7%8B%E7%AF%89%E3%82%92%E5%8F%AF%E8%83%BD%E3%81%AB%E3%81%97%E3%81%9F%E8%A3%8F%E6%8A%80%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6)[](https://x.com/intent/post?text=Linux%E3%81%AE%E3%83%95%E3%82%A1%E3%82%A4%E3%82%A2%E3%82%A6%E3%82%A9%E3%83%BC%E3%83%AB%E3%81%AE%E4%B9%B1%E7%94%A8%EF%BC%9ASpectrum%E3%81%AE%E6%A7%8B%E7%AF%89%E3%82%92%E5%8F%AF%E8%83%BD%E3%81%AB%E3%81%97%E3%81%9F%E8%A3%8F%E6%8A%80%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fhow-we-built-spectrum%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fhow-we-built-spectrum%2F)[](https://bsky.app/intent/compose?text=Linux%E3%81%AE%E3%83%95%E3%82%A1%E3%82%A4%E3%82%A2%E3%82%A6%E3%82%A9%E3%83%BC%E3%83%AB%E3%81%AE%E4%B9%B1%E7%94%A8%EF%BC%9ASpectrum%E3%81%AE%E6%A7%8B%E7%AF%89%E3%82%92%E5%8F%AF%E8%83%BD%E3%81%AB%E3%81%97%E3%81%9F%E8%A3%8F%E6%8A%80%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fhow-we-built-spectrum%2F)[](https://mastodonshare.com/?text=Linux%E3%81%AE%E3%83%95%E3%82%A1%E3%82%A4%E3%82%A2%E3%82%A6%E3%82%A9%E3%83%BC%E3%83%AB%E3%81%AE%E4%B9%B1%E7%94%A8%EF%BC%9ASpectrum%E3%81%AE%E6%A7%8B%E7%AF%89%E3%82%92%E5%8F%AF%E8%83%BD%E3%81%AB%E3%81%97%E3%81%9F%E8%A3%8F%E6%8A%80%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fhow-we-built-spectrum%2F)[](https://www.threads.net/intent/post?text=Linux%E3%81%AE%E3%83%95%E3%82%A1%E3%82%A4%E3%82%A2%E3%82%A6%E3%82%A9%E3%83%BC%E3%83%AB%E3%81%AE%E4%B9%B1%E7%94%A8%EF%BC%9ASpectrum%E3%81%AE%E6%A7%8B%E7%AF%89%E3%82%92%E5%8F%AF%E8%83%BD%E3%81%AB%E3%81%97%E3%81%9F%E8%A3%8F%E6%8A%80%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fhow-we-built-spectrum%2F)

## 関連するタグ

[DDoS](https://blog.cloudflare.com/ja-jp/tag/ddos/)[Linux](https://blog.cloudflare.com/ja-jp/tag/linux/)[Spectrum](https://blog.cloudflare.com/ja-jp/tag/spectrum/)[スピードと信頼性](https://blog.cloudflare.com/ja-jp/tag/speed-and-reliability/)[セキュリティ](https://blog.cloudflare.com/ja-jp/tag/security/)[製品ニュース](https://blog.cloudflare.com/ja-jp/tag/product-news/)

SNS をフォロー

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 新しい投稿のお知らせを受け取るように登録する

メールアドレス

また、あなたのメールアドレスを共有したりすることはございません。

登録する

ご購読ありがとうございます！受信箱を確認して登録してください。
