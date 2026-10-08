---
url: https://blog.cloudflare.com/ja-jp/migrating-cdnjs-to-serverless-with-workers-kv/
title: Workers KV\u3092\u4f7f\u3063\u3066\u3001cdnjs\u3092\u30b5\u30fc\u30d0\u30fc\u30ec\u30b9\u306b\u79fb\u884c\u3059\u308b | Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:48:39.337510+00:00
---

# Workers KVを使って、cdnjsをサーバーレスに移行する | Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/migrating-cdnjs-to-serverless-with-workers-kv/

[ブログ](https://blog.cloudflare.com/ja-jp/)

[CDNJS](https://blog.cloudflare.com/ja-jp/tag/cdnjs/)[Cloudflare Workers KV](https://blog.cloudflare.com/ja-jp/tag/cloudflare-workers-kv/)[オープンソース](https://blog.cloudflare.com/ja-jp/tag/open-source/)2件2件タグを表示

5 タグタグを5件表示

  * 投稿タグ
  * [Cloudflare Workers KV](https://blog.cloudflare.com/ja-jp/tag/cloudflare-workers-kv/)[オープンソース](https://blog.cloudflare.com/ja-jp/tag/open-source/)[サーバーレス](https://blog.cloudflare.com/ja-jp/tag/serverless/)[スピードと信頼性](https://blog.cloudflare.com/ja-jp/tag/speed-and-reliability/)
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



[サーバーレス](https://blog.cloudflare.com/ja-jp/tag/serverless/)[スピードと信頼性](https://blog.cloudflare.com/ja-jp/tag/speed-and-reliability/)

[CDNJS](https://blog.cloudflare.com/ja-jp/tag/cdnjs/)[Cloudflare Workers KV](https://blog.cloudflare.com/ja-jp/tag/cloudflare-workers-kv/)[オープンソース](https://blog.cloudflare.com/ja-jp/tag/open-source/)[サーバーレス](https://blog.cloudflare.com/ja-jp/tag/serverless/)[スピードと信頼性](https://blog.cloudflare.com/ja-jp/tag/speed-and-reliability/)

2020年9月10日

# Workers KVを使って、cdnjsをサーバーレスに移行する

![Tyler Caslin](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48PE9E2K1F7K33FKX1N2NN.JPG&w=64&h=64&f=webp&fit=cover&position=center)

[Tyler Caslin](https://blog.cloudflare.com/ja-jp/author/tyler/)

15分で読了

URLをコピー

この記事は以下でも利用可能です [English](https://blog.cloudflare.com/migrating-cdnjs-to-serverless-with-workers-kv/)、[简体中文](https://blog.cloudflare.com/zh-cn/migrating-cdnjs-to-serverless-with-workers-kv/).

![Migrating cdnjs to serverless with Workers KV](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4576BK2TKQG81VD605TZ1W.png&w=1200&h=713&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///////+9vf37/Lz8fX09vn29ffy8O/r/////Pz97e734uXz4+fx6u3x7e7u6+rp///++fj85uf41tr01dnw3uHt5ebq5+bo////+/r/5uj81Nj309fz3d/v5ubs6ejr////////7/H/4OT94OT66ev38PD08fDx/////////v//9Pf/9fn//P///////Pv6////////////////////////////////////////////////////////////////)

Cloudflareは[cdnjs](https://cdnjs.com/)を運用しています。cdnjsは、オープンソースプロジェクトで、人気のJavaScriptライブラリとリソースを[Cloudflare Workersのネットワーク](https://www.cloudflare.com/cdn/)を経由して配信することで、Webサイトを加速させます。[12月に本格的なアップデートをしてから](https://blog.cloudflare.com/an-update-on-cdnjs/)、スケーラビリティと耐障害性を求めて、cdnjsのモデルチェンジに重点を置きました。本日、Cloudflareがcdnjsを配信する方法を発表できることを嬉しく思います。これは[Cloudflare Workers](https://developers.cloudflare.com/workers/)と分散キーバリューストア[Workers KV](https://developers.cloudflare.com/workers/reference/storage)を用いるサーバーレスインフラストラクチャへの移行です。

cdnjsとは？

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Migrating cdnjs to serverless with Workers KV Embedded Image - FiO5Hb](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW497NYNR078HBR44EV2BV6V.png&w=715&h=213&f=webp&fit=cover&position=center)

詳しくない方のためにご説明すると、cdnjsとは「コンテンツ配信ネットワーク（CDN）for JavaScript（JS）」の頭文字語です。[CDN](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)は、単にインターネットミームや猫の動画、またはHTMLページなどインターネットコンテンツを提供するサーバーの地理的に分散されたネットワークのことです。当社の場合、CDNはCloudflareのグローバルに分散された200以上のデータセンターの[ネットワークの拡大](https://blog.cloudflare.com/cloudflare-network-expands-to-more-than-100-countries/)を指します。

では、これとみなさまがどのように関わっていくのかをご説明します。まず、ページ読み込み時間が超高速になります。事実上これを含めて、どのWebサイトでも読み込むためにJSライブラリを取得する必要があります。たとえば、シドニーを拠点にするWebサイトを訪れるとします。このサイトは、[76.2%](https://w3techs.com/technologies/details/js-jquery)のWebサイトで見られる人気ライブラリであるjQueryからのローカルファイルを含んでいます。New Yorkからこのサイトにアクセスした場合、遅延に気づくかもしれません。TLSハンドシェイク を含むラウンドトリップにかかる時間はもちろん、ファイルの取得するために300ミリ秒を軽く超えてしまうからです。しかし、このWebサイトがcdnj.cloudflare.comを使ってjQueryを参照すると、バッファローにある直近のCloudflareデータセンターからファイルを取り出すことができて、レイテンシーが驚きの20ミリ秒まで短縮します。

cdnjsは水面下で稼働していますが、[11%以上](https://w3techs.com/technologies/overview/content_delivery)のWebサイトで使用され、インターネットをはるかに速くし、さらに信頼性の高い場所に変えてくれています。7月、cdnjsはおよそ190億件ものリクエストを処理しました。データの量は3.46PB（ペタバイト）です。

### ファイルの保存場所

![](http://staging.blog.mrk.cfdata.org/content/images/2020/09/image5-2.png)

cdnjsがインターネットのスピードアップさせていますが、もちろん魔法ではありません。

これまでは、Cloudflareのコアデータセンター１か所で[負荷分散された](https://www.cloudflare.com/load-balancing/)マシンの多くは、cdnjs.cloudflare.comのオリジンとして機能する補助記憶装置から定期的にcdnjsファイルをプルしてきました。新しいファイルがリクエストされると、Cloudflareが[キャッシュ](https://www.cloudflare.com/learning/cdn/what-is-caching/)して、どのデータセンターからでも迅速に取得できるようにしました。

補助記憶装置は、オープンソースの[GitHub](https://github.com/)リポジトリの形式で、JS、CSSや他のWebライブラリのカタログです。ということは、みなさんも含めて、誰でもレビューやその他のプロセスの対象として貢献できるということです。

しかし最近まで、こうした既存の作業は労働集約型で脆弱なものでした。

このブログ記事では、cdnjsの背後にあるインフラストラクチャをより高速で確実、維持が簡単になるように変えたのか、その理由を説明していきます。まず、旧システムに関する問題と懸念を概説して、コミュニティがどのようにcdnjsに貢献したのかを考えます。そして、Workers KVへの移行によってもたらされるメリットを見ていきます。そのあとで、新しいアーキテクチャだけではなく、Webサイトとcdnjs APIへのアップグレードにも触れていきます。最後に、cdnjsの歴史を振り返り、これからどこに向かっていくのかについて、検討していきます。

### 勘違いしていませんか、PRの方法を

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Migrating cdnjs to serverless with Workers KV Embedded Image - PNpgyB](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48510XP89XK4P61KNB9N68.png&w=715&h=643&f=webp&fit=cover&position=center)

専門家ではない読者の方にとって、プルリクエスト（PR）とは、リポジトリで行った変更とマージするリクエストのことです。従来、cdnjsにJavaScfriptライブラリを含めたいと思ったら、まずGitHub上でパッケージを記述したJSONファイルと、含めたいバージョンの追加ファイルで[cdnjs/cdnjs](https://github.com/cdnjs/cdnjs)にPRを作成していました。当社の[古いボット](https://github.com/PeterBot)がPRを承認すると、手動でレビューされ、メ‑ンテナーがマージします。そしてパッケージがcdnjsと統合されます。

簡単そうですよね？そのリポジトリをフォークしてクローン、そしてファイルをいくつかコピペするだけですね？

その通りです。もし書き込みにかけられる時間が何時間あったり、大文字と小文字を区別するファイルシステムや300 GBリポジトリを[git clone](https://git-scm.com/docs/git-clone)（リポジトリを複製）するためのディスクの空きスペースが数百ギガバイトもあったりすれば、コントリビュートするのは簡単です。しかし、時間が足りない場合でも大丈夫です。[git sparse-checkout](https://git-scm.com/docs/git-sparse-checkout)（リポジトリの一部をチェックアウト）してこの作業を終わらせることができます。gitをご存知ありませんか？GitHubのUIを使って手動で1回に1つのファイルを手動で追加するだけです。

これで、大事なことはお分かりになったと思います。macOSがデフォルトで大文字と小文字を区別しないことを発見するためだけに、無邪気にリポジトリのクローニングに10時間も費やしたことを確かに覚えています。

しかし、cdnjsの更新はコントリビュータにとってだけでなく、メンテナーにとっても難しいのです。歴史的に、コミュニティはバージョンファイルに直接コントリビュートできていましたが、これは悪意のあるものになる可能性がありました。各ファイルを手動で確認する必要があり、公式ライブラリソースとファイルを[diff](https://man7.org/linux/man-pages/man1/diff.1.html)し、マルウェアチェックを実行するため、メンテナーの作業を大量に増やしていました。

すでにcdnjsにあるパッケージをどのようにアップデートしたのでしょうか。各パッケージを記述したJSONファイルにライブラリの新バージョンを探す場所をボットに指示する自動更新の定義がオプションであります。存在する場合は、パッケージがnpmまたはGitHubから新バージョンをリリースした時に、ボットがダウンロードし、ファイルを[cdnjs/cdnjs](https://github.com/cdnjs/cdnjs)に、そして算出された[サブリソース完全性](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity)（SRI）のハッシュを[cdnjs/SRI](https://github.com/cdnjs/SRIs)にプッシュします。自動更新のプロパティがない場合は、手動PRを作ってcdnjsを新バージョンに更新するのは、みなさんの責任となります。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Migrating cdnjs to serverless with Workers KV Embedded Image - zfYiq2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW453YW4QHFP208HT4W8AP37.png&w=715&h=271&f=webp&fit=cover&position=center)

### cdnjsの注意喚起

4月、当社のコアデータセンターの1つでメンテナンス中に技術者が、他のデータセンターとの外部接続すべてを供給するケーブルを切断してしまう事故があり、そのデータセンターが約4時間オフラインになってしまいました。特に、影響を受けたデータセンターがプライマリcdnjsオリジンWebサーバーをハウジングしていたため、[この出来事](https://blog.cloudflare.com/cloudflare-dashboard-and-api-outage-on-april-15-2020/)が、cdnjsに対する最初の警鐘となりました。この場合では、外部プロバイダーで実行するバックアップがありましたが、当社を救ったのは、実はCloudflareのグローバルキャッシュでした。キャッシュされていないプロパティだけが読み込みされていなかったため、停止の影響を最小限に抑えることができました。

cdnjsの提供方法をめぐり、信頼性とパフォーマンスの両方をどのように改善できるかを考え始めました。そこで、すぐに目を向けたのが、エッジでの開発に向けた当社独自のプラットフォームである[Cloudflare Workers](https://workers.cloudflare.com/)です。そして、Workersに構築された強力なツールの1つが[Workers KV](https://developers.cloudflare.com/workers/reference/storage)です。高度な読み取りアプリケーションのために最適化され、低レイテンシーでグローバルに分散されたキーバリューストアです。

当社はあれこれと考え合わせ、[cdnjs/cdnjs](https://github.com/cdnjs/cdnjs)リポジトリをプルし、ディスクからファイルを処理する代わりに、物理的マシンを完全に省き、世界中にデータを分散してエッジから直接ファイルを処理することができると気が付きました。この方法ならば、cdnjsは拡張性を高めつつ、オリジンデータセンターの障害から回復することができます。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Migrating cdnjs to serverless with Workers KV Embedded Image - e4r84j](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48943QPE0AVV66JXMBS2M4.png&w=715&h=366&f=webp&fit=cover&position=center)

### Workers KVが救う

一見したところ、Workers KVの利用を決定するのは、簡単なことでした。cdnjsのファイルを変更することは決してありませんが、頻繁な読み取りが必要となるため、Workers KVは完璧でした。

しかし、移行を計画しているうちに、cdnjsにある700万以上のアセットがあると、[Workers KVの10 MiB値制限](https://developers.cloudflare.com/workers/about/limits/)を超えるファイルが間違いなく存在するという懸念が出てきました。調査した後、数百ものcdnjsファイルが大容量で、大半が[JavaScriptソースマップ](https://developer.mozilla.org/en-US/docs/Tools/Debugger/How_to/Use_a_source_map)であることが明らかになりました。

そして、このアイディアが頭に浮かびました。Workers KVに圧縮されたバージョンのcdnjsファイルを保管することができ、容量の大きいファイル問題を解決するだけでなく、ファイルの処理方法も最適化できます。

インターネット料金を支払っている場合、[帯域幅が高額](https://blog.cloudflare.com/the-relative-cost-of-bandwidth-around-the-world/)になってしまうのはお分かりでしょう。そのため、すべての最新ブラウザで、利用可能なときは常に、[圧縮されたWebコンテンツ](https://blog.cloudflare.com/efficiently-compressing-dynamically-generated-53805/)を取得することにします。同様にCloudflare内でも、帯域幅を削減するために、可能な時は常に徹底して圧縮されたコンテンツを処理して[オンザフライ圧縮を試行](https://blog.cloudflare.com/results-experimenting-brotli/)してみました。その結果、[Brotli](https://github.com/google/brotli) フォームと[gzip](https://www.gzip.org/)フォームの両方でWorkers KVに書き込んで、早めにすべてのcdnjsファイルを圧縮することに決めました。そうすることで、レイテンシー要件がなくなり、オンザフライ圧縮よりも圧力レベルを高くすることができました。

つまり今、cdnjsファイルは速くてコンパクトに処理できているということです！

[![](http://staging.blog.mrk.cfdata.org/content/images/2020/09/image7-1.png)](http://staging.blog.mrk.cfdata.org/content/images/2020/09/image7-1.png)

### cdnjsの大変身

今日では、cdnjsのJavaScriptライブラリを含めたい場合にまず、GitHub上のPRを当社の新しいリポジトリ[cdnjs/package](https://github.com/cdnjs/packages)に作成します。リポジトリは50MBで簡単にクローンでき、何千ものJSONファイルで構成されます。JSONファイルはそれぞれcdnjsパッケージとnpmまたはgitからどのように自動更新されるかを記述します。ファイルが（[新規ボット](https://github.com/cdnjs/tools)によって）自動化されたCIに検証されると、メンテナーがマージし、パッケージは自動的に、自動更新サービスでエンロールされます。

新システムでは、セキュリティと保守性が優先されます。まず始めとして、cdnjsバージョンファイルは新バージョンとマージする際、当社のボットが作成して人によるエラーを最小限に抑えます。[cdnjs/package](https://github.com/cdnjs/packages)のJSONファイルを間違えを起こしやすい人間が追加しますが、メンテナーに承認される前に当社のボットで検査します。各ファイルは、自動的に[JSONスキーマ](https://github.com/cdnjs/tools/blob/master/schema_human.json)が検証され、npmまたはGitHubの人気度もチェックされます。

ボットは、新しいリリースを検出すると、Brotliとgzipで圧縮されたバージョンのファイルをWorkers KV内のファイルネームスペースへプッシュします。各エントリで、ボットは[Workers KVのメタデータ](https://blog.cloudflare.com/catching-up-with-workers-kv/)を[Etag](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag)と[Last-Modified](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Last-Modified) HTTPヘッダーのために書きます。以前のように、ボットは圧縮されていないファイルの[サブリソース完全性](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity)（SRI）ハッシュも算出しますが、今ではWorkers KVのSRIネームスペースの代わりにそれをプッシュします。

次に、cdnjs.cloudflare.comから新規ファイルがリクエストされると、[Cloudflare Worker](https://developers.cloudflare.com/workers/)がクライアントの[Accept-Encoding](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Encoding)ヘッダーを検査し、ETagとLast-Modified メタデータをWorkers KVとともに、Brotliまたはgzip圧縮バージョンのどちらかを取得します。圧縮されたファイルがCloudflareを介して戻るため、今後のリクエストと、必要とあれば、圧縮していないオンザフライがキャッシュされます。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Migrating cdnjs to serverless with Workers KV Embedded Image - vmYm4e](https://blog.cloudflare.com/_emdash/api/media/file/01KW45K24P6V4PZD433M522FCE.gif)

現時点では、Workers KVのサイズ制限を超えるファイルがまだ若干あります。したがって、Cloudflare WorkersがWorkers KVからのファイルの取得に失敗すると、オリジナルのgitリポジトリにバックアップされたオリジンから取得されることになります。今後数ヶ月で、徐々にこのインフラストラクチャをなくしていく予定です。

### WebサイトとAPIの拡張

コアのcdnjsインフラストラクチャに加えて、他の多くのコンポーネントもアップグレードされました！

cdnjsプロジェクトの[ホームページ](https://cdnjs.com/)では、[Matt](https://github.com/mattipv4)が構築したカッコいい[新ベータWebサイト](https://github.com/cdnjs/static-website)がみなさんをお迎えします。[Vue](https://vuejs.org/)と[Nuxt](https://nuxtjs.org/)で構成されているベータWebサイトは、完全に[cdnjs API](https://cdnjs.com/api)で運用されています。結果として、最新パッケージ情報で常に最新のものであり、このサイトの提供で必要とされるリソースの使用量が少なくて済みます。このサイトは、最初のページの読み取り以降、クライアント側で完全に実行されており、cdnjsの終わりのない成長に合わせて、当社が拡張するために役立ちます。

実際に、cdnjs APIもその拡張性を強化し、cdnjsとWorkers KVで見てきたものに近いサーバーレスアーキテクチャから恩恵を受けてきました。

Workers KVに移行する前に、cdnjs APIは約300MBのメタデータを生成する定期的なプロセスに依存してきました。cdnjs APIのバックエンドでは、この巨大な「package.min.js」ファイルをメモリーに取得し、それを用いてAPIを操作しました。もし気になるのであれば、ファイルはまだ[こちら](https://storage.googleapis.com/cdnjs-assets/package.min.js)でホストされていますので、どうぞ。ただし、ひとこと言っておきますが、みなさんのブラウザに遅れが出るかもしれません！同様に、SRIは[cdnjs/SRI](https://github.com/cdnjs/SRIs)へとプッシュされ、ローカルでAPIにクローンされ、SRI応答に提供されました。

すべてのcdnjsファイルが（許可されたサイズ制限内で）Workers KVへと移された後、こうしたレガシープロセスは持続不可能となり、何百万もの読み取りとあり得ないほど長い時間が必要となりました。そのため、当社はWorkers KVで見つかったすべてのメタデータをアップロードすることにしました。メタデータを4つのネームスペースに分けました。1つ目はパッケージレベルのメタデータで、2つ目はバージョン固有のメタデータ、3つ目は集約された1つのメタデータ、最後はファイルSRIです。

cdnjsのサーバーレスデザインのように、Cloudflare Workerは[metadata.speedcdnjs.com](http://metadata.speedcdnjs.com/packages)上にあり、いくつものパブリックエンドポイントを使って、Workers KVからデータを提供します。現在のところ、cdnjs APIは完全にこうしたエンドポイントと統合され、cdnjsの拡張にしたがって、明確なソリューションを提供します。

### cdnjsの透明性と将来性

2011年1月の誕生以来、cdnjsは常に透明性に深く根ざし、コミュニティから強さを引き出しています。たとえcdnjsが大規模になって、2011年7月に創設者のRyan KirkmanとThomas Davisが[当社と手を組んだ](https://blog.cloudflare.com/cdnjs-community-moderated-javascript-librarie/)時でも、プロジェクトは完全に[GitHub](https://github.com/cdnjs/)でオープンソースのままであり続けました。

時が経つにつれて、創設者が積極的に活動するのが難しくなり、サポートをコミュニティに頼るようになりました。ほとんど存在しない予算とリポジトリへのわずかなアクセスで、コアcdnjsのメンテナーは毎日プロジェクトを進めるために駆け回りました。

昨年、これが創設者に連絡を取るきっかけとなりました。[2人ともプロジェクトの支援を受けることを喜んでくれました](https://news.ycombinator.com/item?id=21416614)。Cloudflareの役割が大きくなり、cdnjsはこれまで以上に安定し、[活発に参加するメンバー達](https://cdnjs.com/about)がCloudflareとコミュニティの両方から集まりました。

しかし、レガシーシステムへの依存を排除し、ファイルをWorkers KVへと保存するようになると、cdnjsが専有になるのではないかという懸念の声が上がりました。しかし、どうぞご心配なく。cdnjsがこれまで通りの透明性を維持し、限りなくオープンソースであることを保証するために当社は懸命に作業してきました。コミュニティが監査の更新をWorkers KVでできるように、新規リポジトリの[cdnjs/ログ](https://github.com/cdnjs/logs)があります。これはボットがすべてのWorkers KV関連イベントを記録するために利用するものです。さらに誰でも、cdnjs APIからSRIを取得して、cdnjsファイルの整合性を検証することができます。

### まとめ

概して、この1年間はcdnjsにとって波乱の年でしたが、その弱点すべてが危険信号として機能し、当社がより良いシステムを構築する手助けとなっています。最近では、1か所で物理的なマシンに依存することのリスクを軽減でき、[Workers KV](https://developers.cloudflare.com/workers/reference/storage)でファイルが保管されるサーバーレスインフラストラクチャへと移行しました。

現在、cdnjsは何も心配することなく、どこかに消えてしまうことはありません。特にメンテナーの[Sven](https://github.com/xtuc)と[Matt](https://github.com/mattipv4)にはこのプロジェクトに勢いを提供し、cdnjsの拡張からこのブログ記事の編集まで、すべてをしてくれたことに感謝の気持ちを送ります。

将来に向けて、cdnjsの透明性を可能な限り高めるために尽力します。cdnjsが向上するにしたがって、さらにブログ記事を通して、コミュニティに最新情報をリリースしていきます。関心がおありの場合は、当社のブログをサブスクライブしてください。結局、cndjsを可能にしているのは、コミュニティです！積極的に活動するGitHubコントリビュータのみなさん、[cdnjsコミュニティフォーラムのメンバ](https://github.com/cdnjs/cdnjs/discussions/)ーのみなさん、これからもよろしくお願いします！

このページ

オンラインで議論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fmigrating-cdnjs-to-serverless-with-workers-kv%2F&t=Workers%20KV%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%80%81cdnjs%E3%82%92%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC%E3%83%AC%E3%82%B9%E3%81%AB%E7%A7%BB%E8%A1%8C%E3%81%99%E3%82%8B)[](https://x.com/intent/post?text=Workers+KV%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%80%81cdnjs%E3%82%92%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC%E3%83%AC%E3%82%B9%E3%81%AB%E7%A7%BB%E8%A1%8C%E3%81%99%E3%82%8B&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fmigrating-cdnjs-to-serverless-with-workers-kv%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fmigrating-cdnjs-to-serverless-with-workers-kv%2F)[](https://bsky.app/intent/compose?text=Workers+KV%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%80%81cdnjs%E3%82%92%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC%E3%83%AC%E3%82%B9%E3%81%AB%E7%A7%BB%E8%A1%8C%E3%81%99%E3%82%8B+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fmigrating-cdnjs-to-serverless-with-workers-kv%2F)[](https://mastodonshare.com/?text=Workers+KV%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%80%81cdnjs%E3%82%92%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC%E3%83%AC%E3%82%B9%E3%81%AB%E7%A7%BB%E8%A1%8C%E3%81%99%E3%82%8B&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fmigrating-cdnjs-to-serverless-with-workers-kv%2F)[](https://www.threads.net/intent/post?text=Workers+KV%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%80%81cdnjs%E3%82%92%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC%E3%83%AC%E3%82%B9%E3%81%AB%E7%A7%BB%E8%A1%8C%E3%81%99%E3%82%8B+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fmigrating-cdnjs-to-serverless-with-workers-kv%2F)

## 関連するタグ

[CDNJS](https://blog.cloudflare.com/ja-jp/tag/cdnjs/)[Cloudflare Workers KV](https://blog.cloudflare.com/ja-jp/tag/cloudflare-workers-kv/)[オープンソース](https://blog.cloudflare.com/ja-jp/tag/open-source/)[サーバーレス](https://blog.cloudflare.com/ja-jp/tag/serverless/)[スピードと信頼性](https://blog.cloudflare.com/ja-jp/tag/speed-and-reliability/)

SNS をフォロー

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)

  * ![Tyler Caslin](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48PE9E2K1F7K33FKX1N2NN.JPG&w=64&h=64&f=webp&fit=cover&position=center)[Tyler Caslin](https://blog.cloudflare.com/ja-jp/author/tyler/)

[](https://github.com/tc80)




## 新しい投稿のお知らせを受け取るように登録する

メールアドレス

また、あなたのメールアドレスを共有したりすることはございません。

登録する

ご購読ありがとうございます！受信箱を確認して登録してください。
