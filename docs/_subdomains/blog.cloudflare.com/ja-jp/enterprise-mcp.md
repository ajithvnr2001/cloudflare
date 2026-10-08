---
url: https://blog.cloudflare.com/ja-jp/enterprise-mcp/
title: MCP\u306e\u30c7\u30d7\u30ed\u30a4\u306e\u62e1\u5f35\uff1a\u4f01\u696d\u3067\u306e\u30b7\u30f3\u30d7\u30eb\u3067\u5b89\u5168\u3001\u304b\u3064\u4f4e\u30b3\u30b9\u30c8\u306eMCP\u306e\u30c7\u30d7\u30ed\u30a4\u5411\u3051\u306e\u5f53\u793e\u306e\u30ea\u30d5\u30a1\u30ec\u30f3\u30b9\u30a2\u30fc\u30ad\u30c6\u30af\u30c1\u30e3 | Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:51:34.015448+00:00
---

# MCPのデプロイの拡張：企業でのシンプルで安全、かつ低コストのMCPのデプロイ向けの当社のリファレンスアーキテクチャ | Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/enterprise-mcp/

[ブログ](https://blog.cloudflare.com/ja-jp/)

[Agents Week](https://blog.cloudflare.com/ja-jp/tag/agents-week/)[AI](https://blog.cloudflare.com/ja-jp/tag/ai/)[Cloudflare Access](https://blog.cloudflare.com/ja-jp/tag/cloudflare-access/)7件7件タグを表示

10 タグタグを10件表示

  * 投稿タグ
  * [Agents Week](https://blog.cloudflare.com/ja-jp/tag/agents-week/)[AI](https://blog.cloudflare.com/ja-jp/tag/ai/)[Cloudflare Access](https://blog.cloudflare.com/ja-jp/tag/cloudflare-access/)[Cloudflare Gateway](https://blog.cloudflare.com/ja-jp/tag/gateway/)[Cloudflare One](https://blog.cloudflare.com/ja-jp/tag/cloudflare-one/)[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[MCP](https://blog.cloudflare.com/ja-jp/tag/mcp/)[セキュリティ](https://blog.cloudflare.com/ja-jp/tag/security/)[開発者](https://blog.cloudflare.com/ja-jp/tag/developers/)[開発者プラットフォーム](https://blog.cloudflare.com/ja-jp/tag/developer-platform/)
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



[Cloudflare Gateway](https://blog.cloudflare.com/ja-jp/tag/gateway/)[Cloudflare One](https://blog.cloudflare.com/ja-jp/tag/cloudflare-one/)[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[MCP](https://blog.cloudflare.com/ja-jp/tag/mcp/)[セキュリティ](https://blog.cloudflare.com/ja-jp/tag/security/)[開発者](https://blog.cloudflare.com/ja-jp/tag/developers/)[開発者プラットフォーム](https://blog.cloudflare.com/ja-jp/tag/developer-platform/)

[Agents Week](https://blog.cloudflare.com/ja-jp/tag/agents-week/)[AI](https://blog.cloudflare.com/ja-jp/tag/ai/)[Cloudflare Access](https://blog.cloudflare.com/ja-jp/tag/cloudflare-access/)[Cloudflare Gateway](https://blog.cloudflare.com/ja-jp/tag/gateway/)[Cloudflare One](https://blog.cloudflare.com/ja-jp/tag/cloudflare-one/)[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[MCP](https://blog.cloudflare.com/ja-jp/tag/mcp/)[セキュリティ](https://blog.cloudflare.com/ja-jp/tag/security/)[開発者](https://blog.cloudflare.com/ja-jp/tag/developers/)[開発者プラットフォーム](https://blog.cloudflare.com/ja-jp/tag/developer-platform/)

2026年4月14日

# MCPのデプロイの拡張：企業でのシンプルで安全、かつ低コストのMCPのデプロイ向けの当社のリファレンスアーキテクチャ

![Sharon Goldberg](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW488S3YN4RV24QXC7PM57EC.png&w=64&h=64&f=webp&fit=cover&position=center)![Matt Carey](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46BHQSGCBKVGAAVQVS4V3E.png&w=64&h=64&f=webp&fit=cover&position=center)![Ivan Anguiano](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45DFHN0957GZ44YYTH8QXY.png&w=64&h=64&f=webp&fit=cover&position=center)

[Sharon Goldberg](https://blog.cloudflare.com/ja-jp/author/goldbe/)、[Matt Carey](https://blog.cloudflare.com/ja-jp/author/matt-carey/)、[Ivan Anguiano](https://blog.cloudflare.com/ja-jp/author/ivan-anguiano/)

17分で読了

URLをコピー

この記事は以下でも利用可能です [English](https://blog.cloudflare.com/enterprise-mcp/)、[한국어](https://blog.cloudflare.com/ko-kr/enterprise-mcp/).

![BLOG-3252 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW454CX3XEX9FFQW4WC9AYVQ.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///6/vn37Ozx4OTu4uXx7Ovz8O3v7+rn///9/vv65uv01eHy2eT15+z37+/07uzs//////794uz4zeD30uT65O797/P57u/x////////5fD8z+T71ej+6PP/8/f98vT2////////8ff/3+3+5PD/9Pr//P3/+fj5////////////9Pf/+Pr///////////37///////////////////////////////8///////////////////////////////8)

_このコンテンツは自動機械翻訳サービスによる翻訳版であり、皆さまの便宜のために提供しています。原本の英語版と異なる誤り、省略、解釈の微妙な違いが含まれる場合があります。ご不明な点がある場合は、英語版原本をご確認ください。_

Cloudflareは、AI戦略の中核として[ _モデルコンテキストプロトコル（MCP）_](https://modelcontextprotocol.io/)を積極的に導入しています。この変化は、エンジニアリング組織だけでなく、製品、営業、マーケティング、財務チームの従業員がエージェンティックワークフローを使って日々の業務を効率化しています。しかし、MCPとエージェンティックワークフローの導入には、[セキュリティリスク](https://www.cloudflare.com/learning/ai/what-is-ai-security/)がないわけではありません。これには、承認の乱立、[ _プロンプトインジェクション_](https://www.cloudflare.com/learning/ai/prompt-injection/)、および[ _サプライチェーンのリスク_](https://www.cloudflare.com/learning/security/what-is-a-supply-chain-attack/)などがあります。この広範な全社的採用を確実にするために、当社は[ _Cloudflare One (SASE) プラットフォーム_](https://www.cloudflare.com/sase/)と[ _Cloudflare Developer プラットフォーム_](https://workers.cloudflare.com/)の両方から一連のセキュリティ制御を統合し、従業員の作業速度を落とすことなくMCPでAIの使用を管理できるようにしました。 

このブログでは、当社プラットフォームのさまざまな部分を組み合わせて、自律的AIの時代に対応した統一されたセキュリティアーキテクチャを構築することによって、MCPワークフローを保護するための独自のベストプラクティスについて説明します。また、企業向けMCPのデプロイをサポートする2つの新しいコンセプトも紹介します：

  * MCPの使用に関連するトークンコストを大幅に削減するため、[ _MCPサーバーポータルでコードモード_](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#code-mode)を開始します。
  * [ _Cloudflare Gateway_](https://developers.cloudflare.com/cloudflare-wan/zero-trust/cloudflare-gateway/)を使用して、不正なリモートMCPサーバーの使用を検出する、シャドーMCP検出。



また、当社がMCPの導入にどのように取り組み、[ _リモートMCPサーバー_](https://developers.cloudflare.com/agents/guides/remote-mcp-server/)、[ _Cloudflare Access_](https://www.cloudflare.com/sase/products/access/)、[ _MCPサーバーポータル_](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/)、[ _AI Gateway_](https://www.google.com/search?q=https://www.cloudflare.com/developer-platform/ai-gateway/)などのCloudflare製品を使用してMCPセキュリティアーキテクチャを構築したかについても説明します。

## リモートMCPサーバーが可視性と制御性を向上

[ _MCP_](https://www.cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/)は、開発者がAIアプリケーションとアクセスする必要のあるデータソースとの間に双方向の接続を構築できるオープンスタンダードです。このアーキテクチャでは、MCPクライアントは[ _LLM_](https://www.cloudflare.com/learning/ai/what-is-large-language-model/)または他の[ _AIエージェント_](https://www.cloudflare.com/learning/ai/what-is-agentic-ai/)との統合ポイントであり、MCPサーバーは[ _MCPクライアント_](https://www.cloudflare.com/learning/ai/mcp-client-and-server/)と企業リソースの間に位置します。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3252 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48JVG0ATW0C59FP7XMB9AH.png&w=715&h=293&f=webp&fit=cover&position=center)

MCPクライアントとMCPサーバーが分離されることにより、エージェントはAI（MCPクライアントで統合）と企業リソースの認証情報とAPI（MCPサーバーで統合）の明確な境界を維持しながら、自律的に目標を追求し、行動を起こすことができます。

Cloudflareの社員は、プロジェクト管理プラットフォーム、社内Wiki、ドキュメントおよびコード管理プラットフォームなど、さまざまな社内リソースの情報にアクセスするために、MCPサーバーを常に使用しています。

ローカルでホストされたMCPサーバーがセキュリティ上の負担であることを、早い段階から認識していました。ローカルMCPサーバーのデプロイメントは、未検証のソフトウェアソースやバージョンに依存する場合があり、[ _サプライチェーン攻撃_](https://owasp.org/www-project-mcp-top-10/2025/MCP04-2025%E2%80%93Software-Supply-Chain-Attacks&Dependency-Tampering)や[ _ツールインジェクション攻撃_](https://owasp.org/www-community/attacks/MCP_Tool_Poisoning)のリスクが高まります。ITおよびセキュリティ管理者がこれらのサーバーを管理することはできなくなり、どのMCPサーバーを実行するか、どのように最新の状態に維持するかは、個々の従業員や開発者に委ねられます。これは失敗ゲームです。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3252 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46ZP0X5VTHYW9N6N84SSEN.png&w=715&h=137&f=webp&fit=cover&position=center)

その代わり、Cloudflareには、企業全体へのMCPサーバーのデプロイメントを管理する中央集中型チームがあり、このチームは、管理されたインフラストラクチャをすぐに提供する共有MCPプラットフォームをMonorepo内に構築しました。従業員がMCP経由で内部リソースを公開したい場合、まずAIガバナンスチームから承認を得て、テンプレートをコピーし、ツール定義を記述してデプロイします。その際、監査ログ付きのデフォルト拒否の書き込み制御、自動生成された[ _CI/CDパイプライン_](https://www.cloudflare.com/learning/serverless/glossary/what-is-ci-cd/)、および[ _シークレット管理_](https://www.cloudflare.com/learning/security/glossary/secrets-management/)を無料で継承できます。つまり、新しい管理対象MCPサーバーの立ち上げにかかる数分であることを意味します。プラットフォーム自体にガバナンスが組み込まれているため、導入が急速に広がることが可能です。

当社のCI/CDパイプラインは、[ _リモートMCPサーバー_](https://developers.cloudflare.com/agents/guides/remote-mcp-server/)として[ _Cloudflare_](https://www.cloudflare.com/developer-platform/)の開発者プラットフォーム上のバニティドメインにデプロイします。これにより、従業員がどのMCPサーバーを使用しているかを可視化し、ソフトウェアソースの制御を維持することができます。さらに、Cloudflare開発者プラットフォーム上のすべてのリモートMCPサーバーは、データセンターのグローバルネットワーク上に自動的にデプロイされるため、世界のどこにいても、従業員がMCPサーバーに低遅延でアクセスできます。

### Cloudflare Accessは認証を提供します

当社のMCPサーバーの一部は、[ _CloudflareドキュメントMCPサーバー_](https://docs.mcp.cloudflare.com/mcp)や[ _Cloudflare Radar MCPサーバー_](https://radar.mcp.cloudflare.com/mcp)のようなパブリックリソースの前に配置されているため、誰でもアクセスできるようにする必要があります。しかし、当社の従業員が使用するMCPサーバーの多くは、当社のプライベート企業リソースの前に配置されています。これらのMCPサーバーは、権限のあるCloudflare従業員以外のすべてのユーザーがアクセスできないようにするため、ユーザー認証を必要とします。これを実現するために、MCPサーバー用のMonorepoテンプレートは、[ _Cloudflare Access_](https://www.cloudflare.com/sase/products/access/)をOAuthプロバイダーとして統合します。Cloudflare Accessは、ログインフローを保護し、リソースへのアクセストークンを発行すると同時に、エンドユーザーの[ _シングルサインオン（SSO）_](https://www.cloudflare.com/learning/access-management/what-is-sso/)、[ _多要素認証（MFA）_](https://www.cloudflare.com/learning/access-management/what-is-multi-factor-authentication/)、およびIPアドレス、ロケーション、デバイス証明書などのさまざまなコンテキスト属性を検証するIDアグリゲーターとして機能します。

## MCPサーバーポータルは、検出とガバナンスを一元化

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3252 4](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48HRARPT78DD6XPWCPCFHV.png&w=715&h=405&f=webp&fit=cover&position=center)

 _MCPサーバーポータルは、すべてのAIアクティビティのガバナンスと制御を統合します。_

リモートMCPサーバーの数が増えるにつれて、新たな壁、つまり検出という新たな壁に直面しました。当社は、すべての従業員（特にMCPを初めて使う従業員）が、利用可能なすべてのMCPサーバーを簡単に見つけて利用できるようにしたいと考えました。私たちのMCPサーバーポータル製品は、便利なソリューションを提供してくれました。従業員はMCPクライアントをMCPサーバーポータルに接続するだけで、ポータルは使用を許可された社内およびサードパーティのMCPサーバーをすぐに表示します。

さらに、当社のMCPサーバーポータルは、一元化されたロギング、一貫したポリシーの適用、[ _データ損失防止_](https://www.cloudflare.com/learning/access-management/what-is-dlp/)（DLPガードレール）を提供します。当社の管理者は、誰がどのMCPポータルにログインしているかを確認し、個人を特定できるデータ（PII）などの特定のデータが特定のMCPサーバーと共有されることを防止するDLPルールを作成することができます。

また、ポータル自体に誰がアクセスできるか、各MCPサーバーのどのツールを公開するかを制御するポリシーを作成することもできます。たとえば、社内コードリポジトリの前にあるMCPサーバーの読み取り専用ツールのみを公開する、当社の _財務_ グループに属する従業員のみがアクセスできるMCPサーバーポータルを1つ設定できます。一方、当社の _エンジニアリング_ チームに所属する会社のノートパソコンを使用する従業員のみがアクセスできる別のMCPサーバーポータルは、より強力な読み取り/書き込みツールをコードリポジトリMCPサーバーに公開する可能性があります。

当社のMCPサーバーポータルアーキテクチャの概要を上に示します。このポータルは、CloudflareにホストされたリモートMCPサーバーと、Cloudflare以外の場所でホストされたサードパーティのMCPサーバーの両方をサポートしています。このアーキテクチャのパフォーマンスがユニークなのは、これらのセキュリティコンポーネントとネットワーキングコンポーネントが、すべてグローバルネットワーク内の同じ物理マシン上で実行される点です。従業員のリクエストがMCPサーバーポータル、CloudflareがホストするリモートMCPサーバー、Cloudflare Access間を移動する場合、従業員のトラフィックは同じ物理マシンから離れる必要はありません。

## MCPサーバーポータルのコードモードがコストを削減

数か月にわたる大量のMCPのデプロイ後、公正なトークンの支払いが完了しました。また、ほとんどの人がMCPのやり方を間違っていると考え始めました。

MCPへの標準的なアプローチは、MCPサーバー経由で公開されるAPI操作ごとに個別のツールを定義する必要があります。しかし、この静的で網羅的なアプローチは、特に何千ものエンドポイントを持つ大規模なプラットフォームでは、エージェントのコンテキストウィンドウをすぐに使い果たさせます。

以前、サーバー側の[ _コードモードを使用してCloudflareのMCPサーバーを稼働させ_](https://blog.cloudflare.com/code-mode-mcp/)、トークン使用量を99.9%削減しながら、[ _Cloudflare APIの何千ものエンドポイントを公開した_](https://developers.cloudflare.com/api/?cf_target_id=C3927C0A6A2E9B823D2DF3F28E5F0D30)方法について書きました。Cloudflare MCPサーバーは、次の2つのツールを公開します。1つの検索ツールは、モデルが利用可能なものを調べるためにJavaScriptを書くことを可能にし、実行ツールは、JavaScriptを書くことで見つけたツールを呼び出すことを可能にします。``このモデルは、すべてを事前に受け取るのではなく、オンデマンドで必要なものを発見します。

このパターンがとても気に入っているので、すべての人に提供する必要がありました。そこで、[ _MCPサーバーポータル_](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/)で「コードモード」パターンを使用する機能をリリースしました。お客様は、すべてのMCPサーバーの前に、監査制御や段階的なツール開示を行う中央集中型ポータルを設置して、トークンコストを削減できるようになります。

仕組みは次の通りです。すべてのツール定義をクライアントに公開する代わりに、基盤となるすべてのMCPサーバーは、`portal_codemode_search`と`portal_codemode_execute`の2つのMCPポータルツールに集約されます。検索ツールは、モデルに`検索`ツールは、モデルに`codemode.tools()`へのアクセスを提供します。接続されたすべてのアップストリームMCPサーバーからすべてのツール定義を返す関数です。モデルは次に、これらの定義をフィルタリングおよび調査するためにJavaScriptを書き、すべてのスキーマがコンテキストに読み込まれることなく、必要なツールを見つけます。`実行`ツールは、各アップストリームツールが呼び出し可能な関数として利用できる`コードモード`のプロキシオブジェクトを提供します。モデルは、これらのツールを直接呼び出し、複数の操作を連鎖させ、結果をフィルタリングし、コード内でエラーを処理するJavaScriptを書きます。これらはすべて、[ _Dynamic Workers_](https://developers.cloudflare.com/dynamic-workers/)によって提供されるMCPサーバーポータル上のサンドボックス環境で実行されます。

以下は、Jiraチケットを検索し、Google Driveからの情報を使用して更新する必要があるエージェントの例です。まず、次のような適切なツールを探します。
    
    
    // portal_codemode_search
    async () => {
     const tools = await codemode.tools();
     return tools
      .filter(t => t.name.includes("jira") || t.name.includes("drive"))
      .map(t => ({ name: t.name, params: Object.keys(t.inputSchema.properties || {}) }));
    }
    

モデルは、ツールの完全なスキーマがそのコンテキストに入力されることなく、必要な正確なツール名とパラメータを把握できるようになりました。そして、操作を連鎖させるために、単一の`実行`呼び出しを書き込みます。
    
    
    // portal_codemode_execute
    async () => {
     const tickets = await codemode.jira_search_jira_with_jql({
      jql: ‘project = BLOG AND status = “In Progress”’,
      fields: [“summary”, “description”]
     });
     const doc = await codemode.google_workspace_drive_get_content({
      fileId: “1aBcDeFgHiJk”
     });
     await codemode.jira_update_jira_ticket({
      issueKey: tickets[0].key,
      fields: { description: tickets[0].description + “\n\n” + doc.content }
     });
     return { updated: tickets[0].key };
    }
    

これは2つのツール呼び出しです。1人が利用可能なものを発見し、2人が作業を行います。コードモードがなければ、この同じワークフローでモデルは両方のMCPサーバーから全ツールの完全なスキーマを受け取り、3つの個別のツール呼び出しを行う必要があったでしょう。

節約効果を見てみましょう。内部MCPサーバーポータルが4つの内部MCPサーバーに接続されている場合、定義のためだけで約9,400トークンのコンテキストを消費する52のツールが公開されることになります。コードモードを有効にすると、この52個のツールが2つのポータルツールに崩壊し、約600トークンが消費されます。これは94%削減されます。そして重要なことに、このコストは固定されています。ポータルに接続するMCPサーバーが増えても、コードモードのトークンコストは増えません。

コードモードは、URLにクエリパラメータを追加することにより、MCPサーバーポータルで有効化できます。通常のURL（例：`https://myportal.example.com/mcp`)、URLに `?codemode=search_and_execute`を付加します (例:`https://myportal.example.com/mcp?codemode=search_and_execute`).

## AI Gatewayは拡張性とコスト管理を提供します

これで終わりではありません。MCPクライアントとLLMの間の接続に[ _AI Gateway_](https://www.cloudflare.com/developer-platform/products/ai-gateway/)を配置することで、弊社のアーキテクチャに接続します。これにより、さまざまなLLMプロバイダーをすばやく切り替えたり（ベンダーロックインを防ぐため）、（各従業員が消費できるトークンの数を制限することで）コスト管理を実施できます。アーキテクチャ全体を以下に示します。 

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3252 5](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4665999SJ4K5HQZBW2ZJDT.png&w=715&h=405&f=webp&fit=cover&position=center)

## Cloudflare GatewayがシャドーMCPを検出しブロック

これまで、許可されたMCPサーバーに管理されたアクセスを提供してきましたが、ここでは不正なMCPサーバーへの対処について見ていきましょう。[ _Cloudflare Gateway_](https://developers.cloudflare.com/cloudflare-wan/zero-trust/cloudflare-gateway/)を使用して、シャドーMCPの検出を実行できます。Cloudflare Gatewayは、企業のセキュリティチームが従業員のインターネットトラフィックを可視化し、制御できるようにする、包括的なセキュアWebゲートウェイです。

Cloudflare Gateway APIを使用して多層スキャンを実行し、MCPサーバーポータル経由でアクセスされていないリモートMCPサーバーを見つけることができます。これは、次のような既存のGatewayとData Loss Prevention（DLP）セレクタを使用することができます。

  * Gateway `httpHost` セレクタを使用してスキャンする
    * （[ _mcp.stripe.com_](http://mcp.stripe.com)など）を使用した、既知のMCPサーバーのホスト名
    * ワイルドカードホスト名パターンを使用したmcp.*サブドメイン
  * Gatewayの`httpRequestURI`セレクタを使用して、/mcpや/mcp/sseなどのMCP固有のURLパスをスキャン
  * DLPベースのボディ検査を使用してMCPトラフィックを検出します。これは、そのトラフィックが`mcp`や`sse`の明らかな言及を含まないURIを使用している場合でも同様です。具体的には、MCPがHTTP経由でJSON-RPCを使用しているという事実を利用しています。つまり、すべてのリクエストに「tools/call」、「プロンプト/get」、「initialize」などの値を持つ「method」フィールドが含まれるのです。HTTP本文内のMCPトラフィックを検出するために使用できる正規表現ルールのいくつかを以下に示します。


    
    
    const DLP_REGEX_PATTERNS = [
      {
        name: "MCP Initialize Method",
        regex: '"method"\\s{0,5}:\\s{0,5}"initialize"',
      },
      {
        name: "MCP Tools Call",
        regex: '"method"\\s{0,5}:\\s{0,5}"tools/call"',
      },
      {
        name: "MCP Tools List",
        regex: '"method"\\s{0,5}:\\s{0,5}"tools/list"',
      },
      {
        name: "MCP Resources Read",
        regex: '"method"\\s{0,5}:\\s{0,5}"resources/read"',
      },
      {
        name: "MCP Resources List",
        regex: '"method"\\s{0,5}:\\s{0,5}"resources/list"',
      },
      {
        name: "MCP Prompts List",
        regex: '"method"\\s{0,5}:\\s{0,5}"prompts/(list|get)"',
      },
      {
        name: "MCP Sampling Create Message",
        regex: '"method"\\s{0,5}:\\s{0,5}"sampling/createMessage"',
      },
      {
        name: "MCP Protocol Version",
        regex: '"protocolVersion"\\s{0,5}:\\s{0,5}"202[4-9]',
      },
      {
        name: "MCP Notifications Initialized",
        regex: '"method"\\s{0,5}:\\s{0,5}"notifications/initialized"',
      },
      {
        name: "MCP Roots List",
        regex: '"method"\\s{0,5}:\\s{0,5}"roots/list"',
      },
    ];
    

Gateway APIは、追加の自動化をサポートしています。たとえば、上記で定義したカスタムDLPプロファイルを使用して、トラフィックをブロックしたり、リダイレクトしたり、MCPペイロードをログに記録して検査することができます。これらの機能を組み合わせることで、Gatewayは、企業ネットワーク経由でアクセスされる不正なリモートMCPサーバーを包括的に検出することができます。

構築方法の詳細については、この[ _チュートリアル_](https://developers.cloudflare.com/cloudflare-one/tutorials/detect-mcp-traffic-gateway-logs/)を参照してください。

## 外部公開されたMCPサーバーは、AI Security for Appsで保護

これまでは、従業員による社内MCPサーバーへのアクセスの保護に重点を置いていました。しかし、他の多くの組織と同様に、当社もお客様がCloudflare製品をエージェント的に管理・運用するために利用できる外部公開のMCPサーバーを保有しています。これらのMCPサーバーは、Cloudflareの開発者プラットフォーム上でホストされています。（特定の製品の個々のMCPのリストは[ _こちら_](https://developers.cloudflare.com/agents/model-context-protocol/mcp-servers-for-cloudflare/)でご覧いただけます。または、[ _コードモード_](https://blog.cloudflare.com/code-mode/)を使用してCloudflare API全体へのより効率的なアクセスを実現するための新しいアプローチを参照してください。）

私たちは、すべての組織が製品に対して公式なファーストパーティのMCPサーバーを公開すべきだと考えています。代替案として、顧客が公開リポジトリから未検証のサーバーをソースしてしまう可能性があり、パッケージには[ _危険な信頼前提_](https://www.docker.com/blog/mcp-horror-stories-the-supply-chain-attack/)、未公開のデータ収集、あらゆる種類の承認されていない動作が含まれている可能性があります。自社のMCPサーバーを公開することで、顧客が使用するツールのコード、更新頻度、セキュリティ体制を制御できます。

リモートMCPサーバーはすべてHTTPエンドポイントであるため、[ _Cloudflare Web Application ファイアウォール (WAF)_](https://www.cloudflare.com/application-services/products/waf/)の内側に配置することができます。お客様はWAF内で[ _AI Security for Apps_](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/)機能を有効にして、インバウンドMCPトラフィックを自動的に検査し、プロンプトインジェクションの試み、機密データの漏洩、トピック分類を検出できます。公開されているMCPは、他のWeb APIと同様に保護されています。

## 企業におけるMCPの未来

MCPの全社的導入に向けて独自の努力を続ける他の組織にとって、当社の経験、製品、リファレンスアーキテクチャが有用になることを願っています。

当社独自のMCPワークフローは、次の方法で保護しています：

  * 開発者向けに、認証にCloudflare Accessを使用した開発者向けプラットフォーム上でリモートMCPサーバーを構築・デプロイするためのテンプレート化されたフレームワークを提供しています
  * ワークフォース全体をMCPサーバーポータルに接続することで、認証されたMCPサーバーへのセキュアなIDベースのアクセスを確保
  * 従業員のMCPクライアントを支えるLLMへのアクセスをAI Gatewayで仲介してコストを管理し、MCPサーバーポータルでコードモードを使用してトークン消費とコンテキストの肥大化を削減
  * [ _検出_](https://developers.cloudflare.com/cloudflare-one/tutorials/detect-mcp-traffic-gateway-logs/)Cloudflare GatewayによるシャドーMCPの使用



企業向けMCPの導入を進める企業は、まずは既存のリモートMCPサーバーやサードパーティMCPサーバーを[ _Cloudflare MCPサーバーポータル_](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/)の背後に配置し、コードモードを有効にすることで、より安価で安全、かつシンプルな企業向けMCPデプロイメントのメリットを享受できるようにすることをお勧めします。 

_謝辞：このリファレンスアーキテクチャとブログは、Cloudflare内のさまざまな役割やビジネスユニットの多くの人々の仕事を代表するものです。これは貢献者の一部に過ぎません：Ann Ming Samborski、Kate Reznykova、Mike Nomitch、James Royal、Liam Reese、Yumna Moazzam、Simon Thorpe、Rian van der Merwe、Rajesh Bhatia、Ayush Thakur、Gonzalo Chavarri、Maddy Onyehara、Haley Campbell氏_

このページ

オンラインで議論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fenterprise-mcp%2F&t=MCP%E3%81%AE%E3%83%87%E3%83%97%E3%83%AD%E3%82%A4%E3%81%AE%E6%8B%A1%E5%BC%B5%EF%BC%9A%E4%BC%81%E6%A5%AD%E3%81%A7%E3%81%AE%E3%82%B7%E3%83%B3%E3%83%97%E3%83%AB%E3%81%A7%E5%AE%89%E5%85%A8%E3%80%81%E3%81%8B%E3%81%A4%E4%BD%8E%E3%82%B3%E3%82%B9%E3%83%88%E3%81%AEMCP%E3%81%AE%E3%83%87%E3%83%97%E3%83%AD%E3%82%A4%E5%90%91%E3%81%91%E3%81%AE%E5%BD%93%E7%A4%BE%E3%81%AE%E3%83%AA%E3%83%95%E3%82%A1%E3%83%AC%E3%83%B3%E3%82%B9%E3%82%A2%E3%83%BC%E3%82%AD%E3%83%86%E3%82%AF%E3%83%81%E3%83%A3)[](https://x.com/intent/post?text=MCP%E3%81%AE%E3%83%87%E3%83%97%E3%83%AD%E3%82%A4%E3%81%AE%E6%8B%A1%E5%BC%B5%EF%BC%9A%E4%BC%81%E6%A5%AD%E3%81%A7%E3%81%AE%E3%82%B7%E3%83%B3%E3%83%97%E3%83%AB%E3%81%A7%E5%AE%89%E5%85%A8%E3%80%81%E3%81%8B%E3%81%A4%E4%BD%8E%E3%82%B3%E3%82%B9%E3%83%88%E3%81%AEMCP%E3%81%AE%E3%83%87%E3%83%97%E3%83%AD%E3%82%A4%E5%90%91%E3%81%91%E3%81%AE%E5%BD%93%E7%A4%BE%E3%81%AE%E3%83%AA%E3%83%95%E3%82%A1%E3%83%AC%E3%83%B3%E3%82%B9%E3%82%A2%E3%83%BC%E3%82%AD%E3%83%86%E3%82%AF%E3%83%81%E3%83%A3&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fenterprise-mcp%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fenterprise-mcp%2F)[](https://bsky.app/intent/compose?text=MCP%E3%81%AE%E3%83%87%E3%83%97%E3%83%AD%E3%82%A4%E3%81%AE%E6%8B%A1%E5%BC%B5%EF%BC%9A%E4%BC%81%E6%A5%AD%E3%81%A7%E3%81%AE%E3%82%B7%E3%83%B3%E3%83%97%E3%83%AB%E3%81%A7%E5%AE%89%E5%85%A8%E3%80%81%E3%81%8B%E3%81%A4%E4%BD%8E%E3%82%B3%E3%82%B9%E3%83%88%E3%81%AEMCP%E3%81%AE%E3%83%87%E3%83%97%E3%83%AD%E3%82%A4%E5%90%91%E3%81%91%E3%81%AE%E5%BD%93%E7%A4%BE%E3%81%AE%E3%83%AA%E3%83%95%E3%82%A1%E3%83%AC%E3%83%B3%E3%82%B9%E3%82%A2%E3%83%BC%E3%82%AD%E3%83%86%E3%82%AF%E3%83%81%E3%83%A3+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fenterprise-mcp%2F)[](https://mastodonshare.com/?text=MCP%E3%81%AE%E3%83%87%E3%83%97%E3%83%AD%E3%82%A4%E3%81%AE%E6%8B%A1%E5%BC%B5%EF%BC%9A%E4%BC%81%E6%A5%AD%E3%81%A7%E3%81%AE%E3%82%B7%E3%83%B3%E3%83%97%E3%83%AB%E3%81%A7%E5%AE%89%E5%85%A8%E3%80%81%E3%81%8B%E3%81%A4%E4%BD%8E%E3%82%B3%E3%82%B9%E3%83%88%E3%81%AEMCP%E3%81%AE%E3%83%87%E3%83%97%E3%83%AD%E3%82%A4%E5%90%91%E3%81%91%E3%81%AE%E5%BD%93%E7%A4%BE%E3%81%AE%E3%83%AA%E3%83%95%E3%82%A1%E3%83%AC%E3%83%B3%E3%82%B9%E3%82%A2%E3%83%BC%E3%82%AD%E3%83%86%E3%82%AF%E3%83%81%E3%83%A3&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fenterprise-mcp%2F)[](https://www.threads.net/intent/post?text=MCP%E3%81%AE%E3%83%87%E3%83%97%E3%83%AD%E3%82%A4%E3%81%AE%E6%8B%A1%E5%BC%B5%EF%BC%9A%E4%BC%81%E6%A5%AD%E3%81%A7%E3%81%AE%E3%82%B7%E3%83%B3%E3%83%97%E3%83%AB%E3%81%A7%E5%AE%89%E5%85%A8%E3%80%81%E3%81%8B%E3%81%A4%E4%BD%8E%E3%82%B3%E3%82%B9%E3%83%88%E3%81%AEMCP%E3%81%AE%E3%83%87%E3%83%97%E3%83%AD%E3%82%A4%E5%90%91%E3%81%91%E3%81%AE%E5%BD%93%E7%A4%BE%E3%81%AE%E3%83%AA%E3%83%95%E3%82%A1%E3%83%AC%E3%83%B3%E3%82%B9%E3%82%A2%E3%83%BC%E3%82%AD%E3%83%86%E3%82%AF%E3%83%81%E3%83%A3+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fenterprise-mcp%2F)

## 関連するタグ

[Agents Week](https://blog.cloudflare.com/ja-jp/tag/agents-week/)[AI](https://blog.cloudflare.com/ja-jp/tag/ai/)[Cloudflare Access](https://blog.cloudflare.com/ja-jp/tag/cloudflare-access/)[Cloudflare Gateway](https://blog.cloudflare.com/ja-jp/tag/gateway/)[Cloudflare One](https://blog.cloudflare.com/ja-jp/tag/cloudflare-one/)[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[MCP](https://blog.cloudflare.com/ja-jp/tag/mcp/)[セキュリティ](https://blog.cloudflare.com/ja-jp/tag/security/)[開発者](https://blog.cloudflare.com/ja-jp/tag/developers/)[開発者プラットフォーム](https://blog.cloudflare.com/ja-jp/tag/developer-platform/)

SNS をフォロー

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 新しい投稿のお知らせを受け取るように登録する

メールアドレス

また、あなたのメールアドレスを共有したりすることはございません。

登録する

ご購読ありがとうございます！受信箱を確認して登録してください。
