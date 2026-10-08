---
url: https://blog.cloudflare.com/ja-jp/connection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections/
title: ORIGIN\u30d5\u30ec\u30fc\u30e0\u3092\u4f7f\u7528\u3057\u305fconnection-coalescing\uff1aDNS\u30af\u30a8\u30ea\u56de\u6570\u4f4e\u6e1b\u3001\u63a5\u7d9a\u56de\u6570\u4f4e\u6e1b | Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:42:02.841632+00:00
---

# ORIGINフレームを使用したconnection-coalescing：DNSクエリ回数低減、接続回数低減 | Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/connection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections/

[ブログ](https://blog.cloudflare.com/ja-jp/)

[DNS](https://blog.cloudflare.com/ja-jp/tag/dns/)[HTTP2](https://blog.cloudflare.com/ja-jp/tag/http2/)[TLS](https://blog.cloudflare.com/ja-jp/tag/tls/)3件3件タグを表示

6 タグタグを6件表示

  * 投稿タグ
  * [DNS](https://blog.cloudflare.com/ja-jp/tag/dns/)[TLS](https://blog.cloudflare.com/ja-jp/tag/tls/)[インターンシップ体験](https://blog.cloudflare.com/ja-jp/tag/internship-experience/)[スピードと信頼性](https://blog.cloudflare.com/ja-jp/tag/speed-and-reliability/)[研究](https://blog.cloudflare.com/ja-jp/tag/research/)
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



[インターンシップ体験](https://blog.cloudflare.com/ja-jp/tag/internship-experience/)[スピードと信頼性](https://blog.cloudflare.com/ja-jp/tag/speed-and-reliability/)[研究](https://blog.cloudflare.com/ja-jp/tag/research/)

[DNS](https://blog.cloudflare.com/ja-jp/tag/dns/)[HTTP2](https://blog.cloudflare.com/ja-jp/tag/http2/)[TLS](https://blog.cloudflare.com/ja-jp/tag/tls/)[インターンシップ体験](https://blog.cloudflare.com/ja-jp/tag/internship-experience/)[スピードと信頼性](https://blog.cloudflare.com/ja-jp/tag/speed-and-reliability/)[研究](https://blog.cloudflare.com/ja-jp/tag/research/)

2023年9月4日

# ORIGINフレームを使用したconnection-coalescing：DNSクエリ回数低減、接続回数低減

![Suleman Ahmad](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44MCC5WJ427B6XCV7Z59EV.png&w=64&h=64&f=webp&fit=cover&position=center)![Jonathan Hoyland](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45WSR1Z35ZHN4AZE03JA0Z.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Sudheesh Singanamalla](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44QXR5DHNZQWQ7DTBSWGM7.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Suleman Ahmad](https://blog.cloudflare.com/ja-jp/author/suleman/)、[Jonathan Hoyland](https://blog.cloudflare.com/ja-jp/author/jonathan-hoyland/)、[Sudheesh Singanamalla](https://blog.cloudflare.com/ja-jp/author/sudheesh/)

20分で読了

URLをコピー

この記事は以下でも利用可能です [English](https://blog.cloudflare.com/connection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections/)、[Deutsch](https://blog.cloudflare.com/de-de/connection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections/)、[Français](https://blog.cloudflare.com/fr-fr/connection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections/)、[한국어](https://blog.cloudflare.com/ko-kr/connection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections/)、[繁體中文](https://blog.cloudflare.com/zh-tw/connection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections/)、[简体中文](https://blog.cloudflare.com/zh-cn/connection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections/).

![Connection coalescing with ORIGIN Frames: fewer DNS queries, fewer connections](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48HDJ2ZAZ6FJXTRPX0N4CN.png&w=1600&h=889&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/vfi+fHe7eTV593R6+LU8OrZ7unW5eHN//vn+/Xi8Oja6uHW7eXZ8uzc8OvZ6OTS///s//ro9O3h7ubd8enf9e/i8+/f7OnX///y///u+fPn8+zj9e7l+vTo+PTl8e7d///2///z/vfr+PHn+vTq//nt/fnq9fLi///5///1//vt/PTq//ju//7x//3u+fbl///7///3//3v//fs//vw///0///w/Pnn///8///3//3v//js//zx///1///x/fno)

_このブログでは、ACM_ _[Internet Measurement Conference](https://conferences.sigcomm.org/imc/2022/program/)で発表された、ORIGINフレームを使用したconnection coalescing（接続の結束）を計測しプロトタイプ化したCloudflareの[研究論文](https://research.cloudflare.com/publications/Singanamalla2022/)の内容を要約して紹介します。_

読者の中には、1回のWebページへのアクセスで、ブラウザが何十回、時には何百回ものWeb接続を行うことがあると聞いて驚く方もいるでしょう。このブログを例にお話しします。Cloudflareのブログに初めてアクセスした場合、あるいは前回のアクセスからしばらく時間が経っている場合、ブラウザはページを描画するために複数の接続を行います。ブラウザは、blog.cloudflare.comに対応するIPアドレスを見つけるためにDNSクエリを実行し、その後、完全なページを正しく描画するために必要なWebページ上の必要なサブリソースを取得するためのリクエストを行います。その回数は？下図を見ると、この記事の執筆時点で、Cloudflareのブログの読み込みには32のホスト名が使用されています。これはクライアント側がこれらの接続の一部を再利用（または結束）できない限り、32回のDNSクエリと_最低_32回のTCP（またはQUIC）接続が発生することを意味します。

新しいWeb接続が発生するたびに、サーバーの処理能力に新たな負荷がかかる（利用がピークに達する時間帯にはスケーラビリティの問題につながる可能性があります）だけでなく、クライアントのメタデータ（個人がアクセスしている平文のホスト名など）がネットワークに公開されます。平文で公開されるメタデータは、ネットワーク経路上に敵対者や盗み見ようとする者に、ユーザーのオンライン活動や閲覧行動が知られてしまう可能性があります！

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1422 Embedded Image - ckxTYV](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47N3FXQ0TE0F5BAWC0YQTS.png&w=715&h=409&f=webp&fit=cover&position=center)

このブログでは、「connection coalescing（接続の結束）」技術について詳しく見ていきます。[2021年にIP-based coalescing（IPベースの結束）](https://blog.cloudflare.com/connection-coalescing-experiments/)を最初に見て以来、私たちはインターネット全体でさらに大規模な測定とモデリングを行い、結束が機能する場所やその可能性について理解し、予測するための取り組みを行ってきました。IP coalescingは大規模に管理することが難しいため、昨年、「[HTTP/2 ORIGINフレーム拡張](https://datatracker.ietf.org/doc/rfc8336/)」と呼ばれる将来性のある標準（これを利用するとIPアドレスの管理を気にすることなくエッジへの接続を結束できる）を実装し、実験を行いました。

つまり、多くの大手プロバイダーがチャンスを逃しているのです。このブログ（ACM IMC 2022での詳細を掲載した[出版物](https://research.cloudflare.com/publications/Singanamalla2022/)）が、サーバーとクライアントがORIGINフレーム標準を活用するための第一歩となることを願っています。

### ステージの設定

大まかに言うと、ユーザーがWebを移動すると、ブラウザは依存するサブリソースを取得してWebページを描画して完全なWebページを構築します。このプロセスは、工場で物理的な製品を組み立てる様子に酷似しています。その意味で、現代のWebページは組立工場のようなものだと考えることができます。組立工場の場合、最終製品を生産するために必要な資源を供給する「サプライチェーン」に依存しています。

現実世界の組立工場では、1度の注文で複数種類の部品を注文して、1回の出荷でサプライヤーからそれらを受け取ることができます（送料などの無駄なコストを抑え、時間を短縮するための[キッティング・プロセス](https://www.sciencedirect.com/science/article/abs/pii/092552739290109K)のようなものです）。部品の製造元や製造場所を気にすることなく、サプライヤ1社との「取引関係」があれば十分です。サプライヤーから組立工場への1台のトラックに、複数のメーカーの部品を積み込むことができます。

Webの設計により、通常、ブラウザはこの逆の性質の動作をします。Webページの画像やJavaScript、その他のリソース（部品）を取得するために、Webクライアント（組み立て工場）は、サーバー（サプライヤー）から返されたHTMLに定義されたすべてのホスト名（製造元）に対して_少なくとも_1つの接続を行う必要があります。これらのホスト名への接続が同じサーバーに接続されているかどうかは関係ありません。例えばCloudflareのような[リバースプロキシ](https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/)に接続することもあります。同じサプライヤーから組立工場に材料を配送するために製造業者ごとの「新しい」トラックが必要になります。より正式には、同じWebページ上のホスト名からサブリソースを要求するために新しい接続を行う必要があります。

接続の結束なし

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Without connection coalescing](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46818DS1DBPGY0C4DKT15E.png&w=715&h=305&f=webp&fit=cover&position=center)

Webページを読み込むために使用する接続の数は、驚くほど多くなることがあります。また、先行の接続の結果として新しい接続が発生するサブリソースが他のサブリソースを必要とすることもよくあります。また、多くの場合ホスト名を使用したHTTP接続には、接続前にDNSクエリが発生します。Connection coalescing（接続の結束）技術を使用することで、使用する接続の数を減らすことができます。 _つまり、同じトラックのセットを「再利用」して、サプライヤー1社から複数のメーカーの部品を配送することが可能になります。_

接続の結束あり

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![With connection coalescing](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49GJXTQ9MV673E7RD0JDJG.png&w=715&h=305&f=webp&fit=cover&position=center)

### Connection coalescing（接続の結束）技術の原理

Connection coalescing（接続の結束）技術は[HTTP/2で導入](https://datatracker.ietf.org/doc/html/rfc7540)され、[HTTP/3](https://www.rfc-editor.org/rfc/rfc9114.html#name-connection-reuse)に引き継がれました。私たちは[以前](https://blog.cloudflare.com/connection-coalescing-experiments/)、Connection coalescing（接続の結束）についてのブログを書いています（基礎に関する詳しい内容は、そのブログを読むことをお勧めします）。アイデアは単純ですが、それを実装することは多くの設計上の課題が生じる可能性があります。例えば、あなたが今読んでいるこのWebページを読み込むために必要なホスト名が32個（執筆時点）あることを思い出してください。32のホスト名の中には、ユニークな16のドメイン（「有効な[TLD+1](https://www.cloudflare.com/learning/dns/top-level-domain/)」と定義）があります。各ユニークドメインごとに作成する接続の数を減らしたり、既存の接続を「まとめる」ことはできるでしょうか？「 _できます。ただし、状況によります_ 」が答えになります。

ブログページを読み込むのに必要な接続数を正確に知ることはほぼ不可能です。16のドメインに32のホスト名が関連付けられているかもしれませんが、「ユニークな接続数」が16であるとは限りません。すべてのホスト名が1台のサーバー上でホストされていれば必要な接続は_1_となり、それぞれのホスト名がそれぞれ別のサーバーでホストされていれば必要な接続数は32となります。

接続の再利用には様々な形態があるため、HTTP空間における「connection coalescing（接続の結束）」を定義することは重要です。例えば、ホスト名への既存の[TCP](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/)またはTLS接続を再利用して、_**同じ** _ホスト名から複数のサブリソースをリクエストすることは「接続の再利用」ですが、「結束」ではありません。

Coalescing（結束）は、あるホスト名に対する既存のTLSチャネルを再利用したり、_**別の** _ホスト名への接続に転用する場合に発生します。例えば、アクセスしたblog.Cloudflare.comのHTMLがcdnjs.Cloudflare.comのサブリソースを指しているとします。サブリソースに同じTLS接続を再利用するには、TLS証明書の[「Server Alternative Name（SAN）」](https://en.wikipedia.org/wiki/Subject_Alternative_Name)リストに両方のホスト名が一緒に記載されている必要がありますが、このステップだけではブラウザに結束を指示するには不十分です。結局のところ、cdnjs.Cloudflare.comサービスは、同じ証明書上にあっても、blog.Cloudflare.comと同じサーバー上でホストされている場合とそうでない場合があります。では、ブラウザはどのように知ることができるのでしょうか？coalescing（結束）は、サーバが適切な条件を設定した場合にのみ機能しますが、結束するかどうかの判断はクライアント側がする必要があります。先ほどの例に戻ると、組立工場は、サプライヤーがすでに倉庫に同じ部品を持っていることを知らずに、部品をメーカーに直接注文するかもしれません。

ブラウザが結束の可否を判断するための材料は2つあり、1つはIPベース、もう一つはORIGINフレームベースです。前者は、サーバオペレータがサーバ上で利用可能なHTTPリソースにDNSレコードをバインドしておく必要があります。この方法では、すべてのリソースを特定のセットまたは1つのIPアドレスの背後に配置する必要があるため、管理と展開が困難であり、実際には危険な依存関係が作成されてしまいます。IPアドレスが結束の可否に影響を与える方法は[ブラウザによって異なり](https://daniel.haxx.se/blog/2016/08/18/http2-connection-coalescing/)、より保守的なものを選ぶものもあれば、より寛容なものもあります。また、HTTP ORIGINフレームはサーバーにとって調整しやすい判断材料であり、柔軟性があり、（仕様に準拠した実装であれば）サービスを中断しないグレースフル・フェイラーが可能です。

この2つの結束の可否を示す判断材料の基本的な違いは、IPベースのものは暗黙的で、偶発的であり、クライアント側が推測する必要があります（IPアドレスは[名前と実際の関係を持たない](https://blog.cloudflare.com/addressing-agility/)ように設計されているため、当然と言えます）が、それとは対照的に、ORIGINフレームはサーバーからクライアント側に提供される結束の可否を示す明示的なシグナルです（特定のホスト名に対するDNSのレスポンスは関係ありません）。

私たちは[以前、IPベースの結束について実験](https://blog.cloudflare.com/connection-coalescing-experiments/)を行いました。このブログではORIGINフレームベースの結束について詳しく見ていきます。

### ORIGINフレームの規格は？

ORIGINフレームは[HTTP/2](https://www.rfc-editor.org/rfc/rfc8336)と[HTTP/3](https://www.rfc-editor.org/rfc/rfc9412)仕様を拡張したものです。それぞれ接続のストリーム0または制御ストリームで送信される特別なフレームであり、このフレームを使うことで、サーバーは_既存の_確立されたTLS接続でクライアントに‘origin-set’を送信することができます。これには、承認されており、[HTTP 421エラー](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/421)が発生しないホスト名が記載されています。origin-setに記載のあるホスト名は、たとえDNSからそのホスト名を異なるIPアドレスでアナウンスされたとしても、サーバーの証明書SANリストにも記載されている必要があります。

具体的には、2つの異なるステップが必要です：

  1. WebサーバーがORIGINフレーム拡張を使用して配信元のセット（指定された接続が使用される可能性のあるホスト名）を列挙したリストを送信するように設定する必要があります。
  2. 送信されたORIGINフレームにある追加のホスト名を、Webサーバーから返されるTLS証明書のDNS名のSANエントリに記載する必要があります。



大まかに言えば、ORIGINフレームはTLS証明書を補完するものであり、オペレータはこれを付加して「ちょっと待って！クライアントさん、この接続で利用可能なSANの名前はこれで、結束できますよ！」と伝えることができます。ORIGINフレームは証明書自体の一部ではないため、その内容を独自に変更することができます。新しい証明書は必要ありません。また、IPアドレスに依存することもありません。ホスト名が結束可能な場合、新しい接続やDNSクエリを必要とせずに既存のTCP/QUIC+TLS接続を再利用することができます。

[現在の多くのWebサイト](https://w3techs.com/technologies/overview/proxy)は、Cloudflare CDNサービスのようなCDNによって提供されるコンテンツに依存しています。Webサイトの提供に外部のCDNサービスを利用することで、高速性、信頼性を高めながらコンテンツを提供する[配信元サーバー](https://www.cloudflare.com/learning/cdn/glossary/origin-server/)の負荷を軽減することができます。同じCDNが提供することで、Webサイトとリソースがどちらも異なるホスト名、異なるエンティティによって所有されている場合も、CDNオペレータは、証明書管理とORIGINフレームを送信するための接続要求の両方を本物の配信元サーバーに代わって制御することができるため、接続を再利用し、結束させることができます。

残念ながら、ORIGINフレームが生み出した可能性を実践に移す方法はありませんでした。私たちの知る限り、今日までORIGINフレームをサポートするサーバー実装はありませんでした。数あるブラウザの中でORIGINフレームに対応しているのは唯一Firefoxだけです。IPベースの結束は、ORIGINフレームにはサポートが導入されておらず、困難が伴います。結束をより適切にサポートするために必要なエンジニアリング時間と労力は投資に見合うものでしょうか？私たちは、その機会を理解し、可能性を予測するために、インターネット全体の大規模な測定で調べることにし、ORIGINフレームを実装して、実動トラフィックでの実験を行いました。

### 実験1：必要な変更の規模は？

2021年2月、私たちは100台の仮想マシン上で修正した[Webページテスト](https://github.com/WPO-Foundation/webpagetest)を使用し、インターネット上で[最も人気のあるWebページ](https://radar.cloudflare.com/domains)50万件分の[データを収集](https://blog.cloudflare.com/connection-coalescing-experiments/)しました。キャッシングの影響を排除するため（キャッシングではなく、結束を理解するため）、Webページへのアクセスの都度、自動化されたChrome（v88）ブラウザのインスタンスを起動しました。各セッションの正常完了後、Chromeの開発者ツールを使用して、イベントの完全なタイムラインと、証明書とその検証に関する追加情報を含むページ読み込みデータをHTTPアーカイブ形式（HAR）ファイルとして取得し、これを記録しました。さらに、ルートWebページの証明書チェーンとサブリソースリクエストによってトリガーされた新しいTLS接続を解析し、(i) ホスト名の証明書発行者の特定、(ii) Subject Alternative Name（SAN）拡張の存在の検査、(iii) DNS名が使用されたIPアドレスに解決されていることの検証、を行いました。方法と結果の詳細については、テクニカル[ペーパー](https://research.cloudflare.com/publications/Singanamalla2022/)をご覧ください。

最初のステップは、コンテンツを正常に描画するためにWebページが要求するリソースと、それらが存在する場所を把握することでした。接続の結束は、サブリソースのドメインが同じ場所でホストされている場合に可能になります。ドメインの場所は、対応する自律システム（AS）を見つけることで、おおよその位置を推定しました。たとえば、[cdnjs](https://cdnjs.cloudflare.com/https://cdnjs.cloudflare.com/)にアタッチされたドメインは、BGPルーティングテーブルのAS 13335経由で到達可能であり、そのAS番号はCloudflareに属しているとします。下図は、Webページの割合と、Webページを完全に読み込むために必要な一意のASの数を示しています。

Webページの約14%は、完全に読み込むために2つのASを必要とします。つまり、サブリソースをもう1つのASから読み込む必要があるページです。50%以上が、必要なサブリソースをすべて取得するために最大6つのASに問い合わせが必要なページです。上記のプロットで示されているこの結果から、ORIGINフレームを使用する場合、意図した結果を実現するために必要な人員と変更は比較的少なくて済むことが推測されます。したがって、connection coalescing（接続の結束）技術を使用できる可能性は、Webページのすべてのサブリソースを取得するのに必要なユニークなASの数と同等と見積もることができます。しかし実際には、これはSLAなどの運用要因に置き換わる可能性があります、また、[Cloudflareで以前取り組んでいた](https://research.cloudflare.com/publications/Fayed2021/)ソケット、名前、IPアドレス間の柔軟なマッピングが有効に働く場合もあります。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1422 Embedded Image - 3Dlhpw](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45X8GDMJVMT39D8F70E2T1.png&w=715&h=349&f=webp&fit=cover&position=center)

私たちは次に、結束が接続メトリクスに与える影響を理解しようとしました。Webページを読み込むために必要なDNSクエリ数とTLS接続数の実測値と理想値を、それぞれのCDFでまとめると下図のようになります。

モデリングと広範な分析を通じて、ORIGINフレームによる接続の結束によって、ブラウザが行うDNSとTLS接続の数を中央値で60%以上削減できることを確認しました。このモデリングは、クライアントがDNSレコードを要求した回数を特定し、それを理想的なORIGINフレームと組み合わせることで行いました。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1422 Embedded Image - DZcmqU](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48T1Y598J42C2CVMPC1M33.png&w=715&h=394&f=webp&fit=cover&position=center)

[CDN](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)によって運営されるような複数の配信元サーバーが存在する多くは、証明書を再利用し、同じ証明書に複数のDNS SANエントリを記載する傾向があります。これにより、運用者は、作成および更新する証明書の数を減らすことができます。理論的には、証明書に数百万以上の名前を記載することができますが、合理性に欠け、効果的に管理することはできなくなります。既存の証明書を引き続き使用することで、私たちのモデリング測定は完璧な統合を実現するために必要な変更の量を示し、以下の図に示されているように、必要な変更の規模に関する情報を提供します。

Webサイトで提供されている証明書の60%以上は修正することなく、ORIGINフレームの恩恵を受けられることを特定し、証明書に10件以下のDNS SAN名を追加することで、測定対象のWebサイトの92%以上への接続を成功させることを特定しました。CDNプロバイダーは、各証明書に最も人気のある3つまたは4つのホスト名を追加することで、最も効果的な変更を行うことができます。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1422 Embedded Image - 3Eev4N](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47R6AZHNG2GYF9CH2S97M9.png&w=715&h=398&f=webp&fit=cover&position=center)

### 実験2：ORIGINフレームの動作

私たちのモデリングへの期待を検証するため、2022年初頭、私たちはより積極的なアプローチを取りました。私たちの次の実験は、_cdnjs.Cloudflare.com_をサブリソースとして広範に使用する5,000のWebサイトに焦点を当てました。実験的なTLSエンドポイントを修正することで、[RFC標準](https://datatracker.ietf.org/doc/rfc8336/)に定義されているHTTP/2 ORIGINフレームサポートを展開しました。これは、私たちがオープンソース化しているGolangの_net_と_http_依存モジュールの内部フォークを変更する必要がありました（[こちら](https://github.com/cloudflare/go-originframe)と[こちら](https://github.com/cloudflare/net-originframe)を参照してください）。

実験中、実験セット内のWebサイトに接続すると、ORIGINフレームに_cdnjs.Cloudflare.com_が返されましたが、コントロールセットでは任意の（未使用の）ホスト名が返されました。5,000のWebサイトのすべての既存のエッジ証明書も変更されました。実験グループについては、対応する証明書のSANに_cdnjs.Cloudflare.com_が追加されて更新されました。コントロールセットと実験セット間の整合性を確保するため、コントロールグループのドメイン証明書も、いずれのコントロールドメインでも使用されていない、有効で同一サイズのサードパーティドメインで更新されました。これは、証明書の相対的なサイズの変化を一定に保ち、異なる証明書サイズに起因する潜在的なバイアスを回避するために行われました。結果は驚くべきものでした！

実験でFirefoxからWebサイトに届いたリクエストの1%をサンプリングしたところ、**1秒あたりの新しいTLS接続が50%以上減少** していることが確認されました。これは、クライアントとサーバーの両方で実行される暗号検証操作の数が少なくなり、計算オーバーヘッドが減少したことを示しています。予想通り、CDNやサーバーのオペレータによる接続の再利用の有効性を示すコントロールセットには違いはありませんでした。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1422 Embedded Image - q0fWGU](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45GKTR9B46ZHYNCDK42GGC.png&w=715&h=399&f=webp&fit=cover&position=center)

### 議論と洞察

私たちのモデリング測定では、ある程度のパフォーマンス向上が期待できることが示されましたが、実際には大幅な向上は見られませんでした。そのため、パフォーマンスに関しては「悪化しない」ことが適切なメンタルモデルであると言えます。リソースオブジェクトのサイズ、競合接続、輻輳制御の間の微妙な相互作用は、ネットワーク状況に左右されます。例えば、ボトルネックの共有量は、ネットワークリンクのボトルネックリソースを競合する接続が少なくなるにつれて減少します。より多くの事業者によるORIGINフレームのサーバーサポートが広まるにつれて、これらの測定を再検討してみたいと思いました。

パフォーマンスとは別に、ORIGINフレームにはプライバシーの面で大きな利点があります。結束することで、結束されていない接続では公開されていたクライアントのメタデータを隠蔽します。Webページ上の特定のリソースは、Webサイトとの対話方法に従って読み込まれます。つまり、サーバーから何らかのリソースを取得するための新しい接続が発生するたびに、[SNI](https://www.cloudflare.com/learning/ssl/what-is-sni/)（[Encrypted Client Hello](https://blog.cloudflare.com/encrypted-client-hello/)がない場合）のようなTLSの平文のメタデータや、ポート53のUDPまたはTCPで送信される場合、少なくとも1つの平文のDNSクエリがネットワークに公開されます。接続を結束させることで、ブラウザが新しいTLS接続を開く必要がなくなり、余分なDNSクエリを実行する必要がなくなります。これにより、ネットワーク上で盗聴している人物からメタデータの漏えいを防ぐことができます。ORIGINフレームはネットワーク経路からのこれらの信号を最小化させ、ネットワーク盗聴者に経路上で漏れる平文情報の量を減らすことでプライバシーを向上させます。

ブラウザが複数の証明書を検証するために必要な暗号計算を削減する利点もありますが、主な利点は、エンドポイント（ブラウザおよび配信元サーバー）のリソースを考える際の非常に興味深い将来の可能性が開かれることです。これには、[優先順位付け](https://blog.cloudflare.com/better-http-3-prioritization-for-a-faster-web/)や[HTTPアーリーヒント](https://blog.cloudflare.com/early-hints/)のような最近の提案が含まれており、クライアントによる接続過多の発生や、リソースを競合させたりすることなく、より良い体験を提供できるようになります。また、[CERTIFICATEフレーム](https://datatracker.ietf.org/doc/html/draft-ietf-httpbis-http2-secondary-certs-06#section-3.4)のIETF draftと組み合わせることで、WebサイトのTLS証明書にSANエントリを追加することなく、接続確立後にサーバーがホスト名の権威を証明できるため、手作業による証明書の修正の必要性をさらに排除することができます。

### 結論と実施要請

まとめると、現在のインターネットエコシステムには、証明書とそのサーバーインフラストラクチャにわずかな変更を加えるだけで、接続を結束できる多くの機会があります。サーバーは、TLSハンドシェイクの数を約50%と大幅に削減し、描画を阻害するDNSクエリの数を60%以上削減することができます。さらに、クライアントは、ネットワークを覗き見ようとする者にさらされる平文のDNS情報を減らすことで、プライバシーの面でもメリットを享受することができます。

これを実現するために、私たちは現在HTTP/2とHTTP/3の両方のORIGINフレームのサポートを追加する予定です。また、インターネットのエコシステムを改善するために、ORIGINフレームをサポートするようサードパーティのリソースを管理する他の事業者にも働きかけています。私たちの論文投稿がACMインターネット測定会議2022に受理され、[ダウンローダが可能になりました](https://research.cloudflare.com/publications/Singanamalla2022/)。このようなプロジェクトに携わり、新たな標準規格の重要な場面をご自身の目で確認したい方は、当社の[キャリアページ](https://www.cloudflare.com/careers/)へアクセスしてください！

このページ

オンラインで議論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fconnection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections%2F&t=ORIGIN%E3%83%95%E3%83%AC%E3%83%BC%E3%83%A0%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%97%E3%81%9Fconnection-coalescing%EF%BC%9ADNS%E3%82%AF%E3%82%A8%E3%83%AA%E5%9B%9E%E6%95%B0%E4%BD%8E%E6%B8%9B%E3%80%81%E6%8E%A5%E7%B6%9A%E5%9B%9E%E6%95%B0%E4%BD%8E%E6%B8%9B)[](https://x.com/intent/post?text=ORIGIN%E3%83%95%E3%83%AC%E3%83%BC%E3%83%A0%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%97%E3%81%9Fconnection-coalescing%EF%BC%9ADNS%E3%82%AF%E3%82%A8%E3%83%AA%E5%9B%9E%E6%95%B0%E4%BD%8E%E6%B8%9B%E3%80%81%E6%8E%A5%E7%B6%9A%E5%9B%9E%E6%95%B0%E4%BD%8E%E6%B8%9B&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fconnection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fconnection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections%2F)[](https://bsky.app/intent/compose?text=ORIGIN%E3%83%95%E3%83%AC%E3%83%BC%E3%83%A0%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%97%E3%81%9Fconnection-coalescing%EF%BC%9ADNS%E3%82%AF%E3%82%A8%E3%83%AA%E5%9B%9E%E6%95%B0%E4%BD%8E%E6%B8%9B%E3%80%81%E6%8E%A5%E7%B6%9A%E5%9B%9E%E6%95%B0%E4%BD%8E%E6%B8%9B+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fconnection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections%2F)[](https://mastodonshare.com/?text=ORIGIN%E3%83%95%E3%83%AC%E3%83%BC%E3%83%A0%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%97%E3%81%9Fconnection-coalescing%EF%BC%9ADNS%E3%82%AF%E3%82%A8%E3%83%AA%E5%9B%9E%E6%95%B0%E4%BD%8E%E6%B8%9B%E3%80%81%E6%8E%A5%E7%B6%9A%E5%9B%9E%E6%95%B0%E4%BD%8E%E6%B8%9B&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fconnection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections%2F)[](https://www.threads.net/intent/post?text=ORIGIN%E3%83%95%E3%83%AC%E3%83%BC%E3%83%A0%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%97%E3%81%9Fconnection-coalescing%EF%BC%9ADNS%E3%82%AF%E3%82%A8%E3%83%AA%E5%9B%9E%E6%95%B0%E4%BD%8E%E6%B8%9B%E3%80%81%E6%8E%A5%E7%B6%9A%E5%9B%9E%E6%95%B0%E4%BD%8E%E6%B8%9B+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fconnection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections%2F)

## 関連するタグ

[DNS](https://blog.cloudflare.com/ja-jp/tag/dns/)[HTTP2](https://blog.cloudflare.com/ja-jp/tag/http2/)[TLS](https://blog.cloudflare.com/ja-jp/tag/tls/)[インターンシップ体験](https://blog.cloudflare.com/ja-jp/tag/internship-experience/)[スピードと信頼性](https://blog.cloudflare.com/ja-jp/tag/speed-and-reliability/)[研究](https://blog.cloudflare.com/ja-jp/tag/research/)

SNS をフォロー

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)

  * ![Sudheesh Singanamalla](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44QXR5DHNZQWQ7DTBSWGM7.jpg&w=64&h=64&f=webp&fit=cover&position=center)[Sudheesh Singanamalla](https://blog.cloudflare.com/ja-jp/author/sudheesh/)

[](https://sudheesh.info/)




## 新しい投稿のお知らせを受け取るように登録する

メールアドレス

また、あなたのメールアドレスを共有したりすることはございません。

登録する

ご購読ありがとうございます！受信箱を確認して登録してください。
