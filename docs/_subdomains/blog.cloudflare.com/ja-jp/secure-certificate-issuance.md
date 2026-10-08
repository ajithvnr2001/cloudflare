---
url: https://blog.cloudflare.com/ja-jp/secure-certificate-issuance/
title: \u30de\u30eb\u30c1\u30d1\u30b9\u30c9\u30e1\u30a4\u30f3\u8a8d\u8a3c\uff08Multipath Domain Control Validation\uff09\u3092\u4f7f\u7528\u3057\u305f\u8a3c\u660e\u66f8\u767a\u884c\u306e\u4fdd\u8b77 | Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:49:04.085762+00:00
---

# マルチパスドメイン認証（Multipath Domain Control Validation）を使用した証明書発行の保護 | Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/secure-certificate-issuance/

[ブログ](https://blog.cloudflare.com/ja-jp/)

[BGP](https://blog.cloudflare.com/ja-jp/tag/bgp/)[CFSSL](https://blog.cloudflare.com/ja-jp/tag/cfssl/)[Crypto Week](https://blog.cloudflare.com/ja-jp/tag/crypto-week/)6件6件タグを表示

9 タグタグを9件表示

  * 投稿タグ
  * [BGP](https://blog.cloudflare.com/ja-jp/tag/bgp/)[DNS](https://blog.cloudflare.com/ja-jp/tag/dns/)[TLS](https://blog.cloudflare.com/ja-jp/tag/tls/)[スピードと信頼性](https://blog.cloudflare.com/ja-jp/tag/speed-and-reliability/)[セキュリティ](https://blog.cloudflare.com/ja-jp/tag/security/)[暗号](https://blog.cloudflare.com/ja-jp/tag/cryptography/)
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



[DNS](https://blog.cloudflare.com/ja-jp/tag/dns/)[HTTPS](https://blog.cloudflare.com/ja-jp/tag/https/)[TLS](https://blog.cloudflare.com/ja-jp/tag/tls/)[スピードと信頼性](https://blog.cloudflare.com/ja-jp/tag/speed-and-reliability/)[セキュリティ](https://blog.cloudflare.com/ja-jp/tag/security/)[暗号](https://blog.cloudflare.com/ja-jp/tag/cryptography/)

[BGP](https://blog.cloudflare.com/ja-jp/tag/bgp/)[CFSSL](https://blog.cloudflare.com/ja-jp/tag/cfssl/)[Crypto Week](https://blog.cloudflare.com/ja-jp/tag/crypto-week/)[DNS](https://blog.cloudflare.com/ja-jp/tag/dns/)[HTTPS](https://blog.cloudflare.com/ja-jp/tag/https/)[TLS](https://blog.cloudflare.com/ja-jp/tag/tls/)[スピードと信頼性](https://blog.cloudflare.com/ja-jp/tag/speed-and-reliability/)[セキュリティ](https://blog.cloudflare.com/ja-jp/tag/security/)[暗号](https://blog.cloudflare.com/ja-jp/tag/cryptography/)

2019年6月18日

# マルチパスドメイン認証（Multipath Domain Control Validation）を使用した証明書発行の保護

![Dina Kozlov](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49DZ20ZY95S71GB0FPG6GC.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Gabbi Fisher](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48AWARSGXCZQZ5Y1WSQE8K.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Dina Kozlov](https://blog.cloudflare.com/ja-jp/author/dina/)、[Gabbi Fisher](https://blog.cloudflare.com/ja-jp/author/gabbi/)

19分で読了

URLをコピー

この記事は以下でも利用可能です [English](https://blog.cloudflare.com/secure-certificate-issuance/)、[Deutsch](https://blog.cloudflare.com/de-de/secure-certificate-issuance/)、[Español](https://blog.cloudflare.com/es-es/secure-certificate-issuance/)、[Français](https://blog.cloudflare.com/fr-fr/secure-certificate-issuance/)、[简体中文](https://blog.cloudflare.com/zh-cn/secure-certificate-issuance/).

![Securing Certificate Issuance using Multipath Domain Control Validation](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW470A3NY83V3JFPW6N7Q7GJ.png&w=922&h=644&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/////f//7Ovs4tvZ5t/b7+zp8fLz7O/0/////P7+6eDb3Me83su+6N3V7urp7Ozw/////Pz659XJ1rOZ17Wb48/B6+Pg7ert//////766dTF2K6P2LCR5M297uTf8Ozv////////8eDV4cGr4sOu7dvP9e3q9vP1////////+vLt7t7V8OHZ+vHs/vv6/fv+////////////+fX1/fn5/////////////////////////v3/////////////////)

このブログ記事は、[暗号化ウィーク 2019](https://blog.cloudflare.com/welcome-to-crypto-week-2019/)の内容です。

インターネット上の信頼性は、公開鍵暗号基盤（PKI）に支えられています。PKIがデジタル証明書を発行することでサーバーはWebサイトをセキュアに保つことができ、暗号化された信頼できる通信の基盤を提供します。

証明書を利用する場合、証明書内の公開鍵を使用してサーバーIDを検証することにより、HTTPSの暗号化が可能になります。HTTPSは、銀行のログイン情報や個人的なメッセージなどのセンシティブデータを通信するWebサイトでは特に重要です。ありがたいことに、Google Chromeなどの最新のブラウザでは、HTTPSを使用して保護されていないWebサイトに「保護されていない通信」と表示して、ユーザーが自分がアクセスしているWebサイトのセキュリティについて意識を高めることができるようにしています。

このブログ記事では、CloudflareがCAに提供する、証明書の発行をさらに確実に保護する新しい無料ツールを紹介します。まず、詳細の説明に進む前に、証明書の発行元について説明しましょう。

### 認証局

認証局（CA）は、証明書の発行を担当する機関です。

任意のドメインに証明書を発行する際、CAはドメイン認証（DCV）を使用して、当該ドメインの証明書を要求するエンティティがドメインの正当な所有者であることを確認します。ドメインの所有者は、DCVを使用して次のいずれかの操作を行います。

  1. ドメインのDNSリソースレコードを作成する。
  2. そのドメインにあるWebサーバーにドキュメントをアップロードする。
  3. ドメインの管理者用電子メールアカウントの所有権を証明する。



DCVプロセスにより、悪意のある第三者が要求元が所有していないドメインの秘密鍵と証明書の組み合わせを取得するのを防ぎます。

悪意のある第三者がこの組み合わせを取得するのを防ぐことは、非常に重要です。不適切に発行された証明書と秘密鍵の組み合わせが相手側に入手された場合、被害者のドメインになりすまして、機密性の高い HTTPSトラフィックを処理してしまう可能性があります。これは、インターネットに対する既存の信頼を損なうもので、個人データが大規模に侵害されるおそれがあります。

たとえば、CAをだましてgmail.comの証明書を誤発行させた場合、GoogleになりすましてTLSハンドシェイクを実行し、Cookieとログイン情報を取得して被害者の Gmailアカウントにアクセスできます。証明書の誤発行のリスクは明らかに深刻です。

### **ドメイン認証（DCV:Domain Control Validation）**

このような攻撃を防ぐために、CAはDCVを実行した後でのみ証明書を発行します。ドメインの所有権を確認する1つの方法は、HTTP認証によるもので、これは、セキュリティ保護したいWebサーバー上の特定の HTTPエンドポイントにテキストファイルをアップロードして行います。 もう一つのDCVメソッドは、電子メールを利用するもので、検証コードへのリンクを含む電子メールを、当該ドメインの管理者の連絡先に送信する方法です。

### **HTTP認証**

例えば、アリスという人がドメイン名aliceswonderland.comを購入し、このドメイン専用の証明書を取得しようとしているとします。アリスは、認証局としてLet's Encryptを使用することを選択します。まず、アリスは独自の秘密鍵を生成し、証明書署名要求（CSR）を作成する必要があります。彼女はCSRをLet's Encryptに送信しますが、CAはアリスがaliceswonderland.comを所有していると確認できるまで、そのCSRの証明書と秘密鍵を発行しません。次にアリスは、HTTP認証を通じて、このドメインを所有していることを証明できます。

Let's EncryptがHTTP経由でDCVを実行する場合、アリスは、Webサイトの /.well-known/acme-challengeパスにランダムな名前の付いたファイルを配置する必要があります。CAは、<http://aliceswonderland.com/.well-known/acme-challenge/><random_filename>に対してHTTP GET要求を送信して、このファイルを取得する必要があります。このエンドポイントに予期された値が存在すれば、DCVは成立します。

HTTP認証の場合、アリスはファイルを[http://aliceswonderland.com/.well-known/acme-challenge/YnV0dHNzにアップロードします。](http://aliceswonderland.com/.well-known/acme-challenge/YnV0dHNz%E3%81%AB%E3%82%A2%E3%83%83%E3%83%97%E3%83%AD%E3%83%BC%E3%83%89%E3%81%97%E3%81%BE%E3%81%99%E3%80%82)

ファイル本文に以下を含みます。
    
    
    curl http://aliceswonderland.com/.well-known/acme-challenge/YnV0dHNz
    
    GET /.well-known/acme-challenge/YnV0dHNz
    Host: aliceswonderland.com
    
    HTTP/1.1 200 OK
    Content-Type: application/octet-stream
    
    YnV0dHNz.TEST_CLIENT_KEY

CAは、Base64トークン `YnV0dHNz`を使用するように指示します。 `TEST_CLIENT_KEY`は、アカウントにリンクされたキーにあり、証明書の要求者とCAだけが知っています。CAは、このフィールドの組み合わせを使用して、証明書の要求者が実際に当該ドメインを所有していることを確認します。その後、アリスは自身のWebサイト用の証明書を取得することができます。

### **DNS認証**

ユーザーがドメインの所有権を検証するもう 1 つの方法は、ドメインのリソースレコードにCAからの確認文字列、_トークン_を含むDNS TXTレコードを追加する方法です。たとえば、これは、Googleに対して認証を行っている企業のドメインの例です。
    
    
    $ dig TXT aliceswonderland.com
    aliceswonderland.com.	 28 IN TXT "google-site-verification=COanvvo4CIfihirYW6C0jGMUt2zogbE_lC6YBsfvV-U"

ここでは、アリスは特定のトークン値を持つTXT DNSリソースレコードの作成を選択しています。GoogleのCAは、このトークンの存在を確認して、アリスが本当に自分のWebサイトを所有していることを検証できます。

### **BGPハイジャック攻撃の種類**

サーバーがクライアントと安全に通信するためには、証明書の発行が必要です。このため、証明書の発行を担当するプロセスもセキュアであることが、とても重要なのです。残念ながら、これは常に当てはまるとは限りません。

プリンストン大学の研究者が最近、一般的なDCVメソッドには、悪意のある第三者がネットワークレベルで実施する攻撃に対する脆弱性があることを発見しました。ボーダーゲートウェイプロトコル（BGP）が、インターネットの「郵便サービス」として、最も効率的なルートを介してデータを配信する責任を王とすると、自律システム（AS）は1 組織が運営するインターネットネットワークの業務を担う個々の郵便局の支店に相当します。ネットワークレベルの悪意のある第三者は、そのトラフィックにドメインの証明書のような重要な内容が含まれているような場合にBGP経由で不正なルートをアドバタイズしてトラフィックを盗もうとすることがあります。

[ _BGPにより認証局を欺く_](https://www.princeton.edu/~pmittal/publications/bgp-tls-usenix18.pdf)は、DCVプロセスの間に企てられる可能性のある、悪意のある第三者が所有していないドメインの証明書を入手しようとする5種の攻撃を取り上げています。これらの攻撃を実装した後、作者は（倫理的に）、自分が所有していないドメインの証明書を下記の、上位5つのCAから取得できました。Let’s Encrypt、GoDaddy、Comodo、Symantec、GlobalSignですがどのように行ったのでしょうか？

### **DCVプロセスへの攻撃**

BGPハイジャックを使用したDCVプロセスの攻撃方法には、主に次の2通りの方法があります。

  1. Sub-Prefix（サブプレフィックス）攻撃
  2. Equally-Specific-Prefix（等価特定プレフィックス）攻撃



これらの攻撃は、悪意のある第三者が被害者のドメインに対する証明書署名要求をCAに送信した場合の脆弱性を生みます。CAがHTTP GETリクエストを使用して（前述のように）ネットワークリソースを検証すると、悪意のある第三者はBGP攻撃を利用してトラフィックを乗っ取り、CAの要求がドメイン所有者ではなく第三者に再ルーティングします。これらの攻撃がどのように行われるかを理解するには、まず少し計算を行う必要があります。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Securing Certificate Issuance using Multipath Domain Control Validation Embedded Image - pcGer6](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW476DD64X5Q5DKY173ZT0DQ.png&w=715&h=307&f=webp&fit=cover&position=center)

インターネット上のすべてのデバイスは、数値による識別子としてIP（インターネットプロトコル）アドレスを使用しています。IPv6アドレスには128ビットが含まれ、スラッシュ表記の後にプレフィックスのサイズが続きます。したがってネットワークアドレス2001:DB8:1000::/48の場合、「/48」がネットワークに含まれるビット数を示します。つまり、残りの80ビットの部分にホストアドレスが含まれ、合計で10,240 個のホストアドレスがあるということになります。プレフィックス番号が小さいほど、ネットワークに残るホストアドレスが多くなります。この知識を元に、攻撃について考えていきましょう。

#### **攻撃1：Sub-Prefix（サブプレフィックス）攻撃**

BGPがルートをアナウンスするとき、ルーターは常により具体的なルートに従うことを優先します。そのため、2001:DB8::/32および2001:DB8:1000::/48がアドバタイズされた場合、ルーターはより具体的なプレフィックスの後者を使用します。このことは、悪意のある第三者が被害者のドメインのIPアドレスを使用して、特定のIPアドレスに対してBGPアナウンスを行う場合に、問題になります。被害者のleagueofentropy.comのIPアドレスが2001:DB8:1000::1で、2001:DB8::/32としてアナウンスされるとします。悪意のある第三者がプレフィックス2001:DB8:1000::/48をアナウンスした場合、被害者のトラフィックを捕らえて、_サブプレフィックスハイジャック_攻撃を開始します。

2018年4月中に発生したようなIPv4[攻撃](https://blog.cloudflare.com/bgp-leaks-and-crypto-currencies/)の場合は、/24と/23がアナウンスされ、より具体的な/24が不正なエンティティによってアナウンスされました。IPv6の場合は、/48 および/47のアナウンスになります。いずれのシナリオでも、/24と/48が、グローバルにルーティングできる最小のブロックです。次の図では、/47はテキサス州、/48はより具体的なテキサス州オースティンです。新しい（しかし不正な）ルートは、インターネットの一部の既存のルートを上書きしました。次に、攻撃者は、DNSレコードを持つ通常のIPアドレス上で不正なDNSサーバーを実行し、既存のサーバーの代わりに新規の不正なWebサーバーに向けます。これにより、不正なルートが伝播されていたエリア内の、犠牲者のドメインに向けられていたトラフィックが引き寄せられました。この攻撃が成功した理由は、受信側ルーターがより具体的なプレフィックスを常に優先するためです。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Securing Certificate Issuance using Multipath Domain Control Validation Embedded Image - em8gbM](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44WRWD7FATMQVYHMTE8FSB.png&w=715&h=334&f=webp&fit=cover&position=center)

#### **攻撃2：Equally-Specific-Prefix（等価特定プレフィックス）攻撃**

前回の攻撃では、悪意のある第三者はより具体的なアナウンスを提供することでトラフィックをハイジャックすることができましたが、被害者のプレフィックスが/48 で、サブプレフィックス攻撃が実行可能ではない場合は、どうでしょうか？この場合、攻撃者はequally-specific-prefix（等価特定プレフィックス）ハイジャックを開始し、攻撃者は被害者と同じプレフィックスをアナウンスします。つまり、ASは、パスの長さなどのプロパティに基づいて、被害者と悪意のある第三者のアナウンスの間で優先ルートを選択します。この攻撃は、トラフィックの一部のみを傍受します。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Securing Certificate Issuance using Multipath Domain Control Validation Embedded Image - DsOGh5](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45V6A2D0N9JZ2BN40GRR5J.png&w=715&h=365&f=webp&fit=cover&position=center)

この論文内では、より高度な攻撃についても詳細に述べられています。この攻撃は根本的には同類の攻撃ですが、もっとステルス性の高いものです。

攻撃者は、自分が所有していないドメインの偽の証明書の取得に成功すると、被害者のドメインを装って説得力のある攻撃を実行し、被害者のTLS トラフィックを復号化して傍受することができます。TLSトラフィックの復号化が可能なことで、悪意のある第三者は暗号化されたTLSトラフィックに対して中間者攻撃（MITM）を実行し、被害者のドメイン宛てのインターネットトラフィックを自分宛に再ルーティングすることができます。攻撃のステルス性を高めるために、悪意のある第三者は引き続き被害者のドメインを通じてトラフィックを転送し、検出不能な方法で攻撃を実行します。

### **DNSスプーフィング**

悪意のある第三者がドメインを制御するもう 1 つの方法は、DNSネームサーバーに属する送信元IPアドレスを使用した、DNSトラフィックのスプーフィングです。誰でも自分のパケットの送信IPアドレスを変更できるため、悪意のある第三者は被害者のドメインの解決に関与するすべてのDNSネームサーバーのIPアドレスを偽装してCAに応答する際にネームサーバーを偽装できます。

これは、単にDNSの応答を改ざんしてCAを攻撃するよりも高度な攻撃です。各DNSクエリにはそれぞれランダム化されたクエリ識別子と送信元ポートがあるため、偽のDNS応答は、DNSクエリの識別子と一致しないと説得力を持ちません。これらのクエリ識別子はランダムであるため、正しい識別子を使用してスプーフィングされた応答を行うことはきわめて困難になります。

悪意のある第三者は、ユーザーデータグラムプロトコル（UDP）DNSパケットをフラグメント化して、識別するDNS応答情報（ランダムDNSクエリ識別子など）を1つのパケットで配信し、実際の回答セクションは別のパケットに続けることができます。このようにして、悪意のある第三者は正当なDNSクエリに対するDNS応答をスプーフィングします。

たとえば、悪意ある第三者が、victim.comの証明書を誤発行させるために、パケットのフラグメント化を強制し、DNS認証のスプーフィングを試みるとします。悪意のある第三者は、victim.comのDNSネームサーバーに、小さな最大転送単位または最大バイトサイズで、ICMPの「フラグメント化が必要な」パケットを送信します。こうして、DNS応答のフラグメント化を開始するネームサーバーを取得します。CAがvictim.comのTXTレコードを要求するvictim.comのDNSクエリをネームサーバーに送信すると、ネームサーバーは上記の 2 つのパケットに応答をフラグメント化します。1つ目のパケットには悪意のある第三者がスプーフィングできないクエリIDと送信元ポートが、2つ目のパケットには、悪意のある第三者がスプーフィングできる回答セクションが含まれています。悪意ある第三者は、DNS認証プロセスの間中ずっとCAに対してスプーフィング回答を送信し続け、CAがネームサーバーから実際の回答を受け取る前にスプーフィング回答を滑り込ませようとすることがあります。

その際、DNS応答の回答セクション（重要な部分）が改ざんされ、悪意のある第三者がCAをだまして証明書を誤発行させる可能性があります。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Securing Certificate Issuance using Multipath Domain Control Validation Embedded Image - OQVnvJ](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48SCWYFBR0Y0D9VKKXRPHP.png&w=715&h=679&f=webp&fit=cover&position=center)

### **解決策**

一見すると、証明書透過性ログが誤発行された証明書を公開して、CAが証明書をすばやく取り消せるようにできるようにも思えます。ただし、CTログには、新しく発行された証明書が含まれるまでに最大24時間かかる場合があり、証明書の失効は異なるブラウザー間では統一されない可能性があります。攻撃が起きてから対処するのではなく、CAが積極的に攻撃をあらかじめ防ぐことができるソリューションが必要です。

Cloudflareは、CA向けの無料APIの提供を発表します。これによりグローバルなネットワークを活用して世界中の複数のバンテージポイントからDCVを実行できます。このAPIは、BGPハイジャックおよびオフパスDNS攻撃に対してするDCVプロセスを強化します。

Cloudflareが世界中で175以上のデータセンターを運営していることから、当社は複数のバンテージポイントからDCVを実行できるという他にない立場にあります。各データセンターはDNSネームサーバーまたは HTTPエンドポイントへの固有のパスがあります。つまり、BGPルートのハイジャックが成功しても、DCVリクエストの一部にしか影響を与えず、BGPのハイジャックをさらに抑制できることを意味します。また、CloudflareではRPKIを使用しているため、実際にBGPルートに署名と検証を行っています。

このDCVチェッカーは、オフパスのDNSスプーフィング攻撃からCAを追加的に保護します。オフパスの攻撃者からの保護用に、サービスに組み込んだ新しい機能が、DNSクエリの送信元IPのランダム化です。送信元IPを攻撃者にとって予測不能にすると、DCV認証エージェントに対して偽のDNS応答の 2 番目のフラグメントをスプーフィングすることがより困難になります。

当社のDCV APIは、複数のパスから収集する複数のDCV結果を比較することで、悪意ある第三者が、実際に所有していないドメインを所有しているとCAに誤解させることはほとんど不可能になります。CAは、当社のツールを使用することにより、正当なドメイン所有者にのみ証明書を発行することを確実にできます。

CloudflareのマルチパスDCVチェッカーは、次の2つのサービスで構成されています。

  1. 特定のデータセンターからのDCV実行を担当するDCVエージェント
  2. CAからのマルチパスDCV要求を処理し、DCVエージェントの一部に発送するDCVオーケストレーター



CAは、傍受されることなくDCVが実施できたことを確認したい場合、実行するDCVの種類とそのパラメーターを指定して当社APIに要請できます。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Securing Certificate Issuance using Multipath Domain Control Validation Embedded Image - vLqWmt](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48GWBG3GR262EBG24APYMM.png&w=715&h=792&f=webp&fit=cover&position=center)

続いてDCVオーケストレーターは、各要求を、異なるデータセンター内にある20を超えるDCVエージェントのうちランダムに抽出する一部に転送します。各DCVエージェントはDCVリクエストを実行し、その結果をDCVオーケストレーターに転送し、そこで各エージェントが監視した内容が集計されてCAに戻されます。

この方式を一般化すると、認証局認定（CAA）レコードなどのDNSレコードに対してマルチパスクエリを実行することもできます。CAAレコードは、CAがドメインに対して証明書を発行することを認定するため、これをスプーフィングして認定されていないCAをだまし、証明書を発行させることは、マルチパス監視が防ぐもう 1 つの攻撃方法です。

マルチパスチェッカーの開発中、BGPハイジャック攻撃を通じて証明書の誤発行の概念実証（PoC）を紹介したプリンストンの研究グループと連絡を取り合っていました。_BGPにより認証局を欺くこと_と題する論文の共同執筆者である、Prateek Mittal氏は、

> 「分析から、複数のバンテージポイントからドメイン認証を行うことで、局所的なBGP攻撃の影響を著しく軽減することが示されました。当社ではWebセキュリティを強化するため、すべての認証局でこのアプローチを採用することをお勧めします。Cloudflareが実装するこの防御の特に魅力的な特徴は、Cloudflareがインターネット上の膨大な数のバンテージポイントを利用可能であり、DCVの堅牢性を大幅に向上させることができる点です。」と書いています。

当社のDCVチェッカーは、インターネットの信頼性を広めるべきであるとの当社の信念に基づいて、第三者による分析（Cloudflareが提供するような）によって徹底的に吟味して、安定性とセキュリティを確保しています。このツールは、当社の[既存の証明書透過性モニター](https://blog.cloudflare.com/introducing-certificate-transparency-and-nimbus/)をサービス一式としてまとめたものであり、CAが証明書発行の責任向上のために使用することができます。

### **試用の機会**

マルチパスDCVチェッカーの構築においては、複数のCloudflare製品を[ _ドッグフーディング（試用）_](https://en.wikipedia.org/wiki/Eating_your_own_dog_food)することができました。

シンプルな収集および集計ツールとしてのDCVオーケストレーターは、[Cloudflare Workers](https://developers.cloudflare.com/workers/)の優秀な候補でした。[こちらの記事](https://blog.cloudflare.com/generating-documentation-for-typescript-projects/)を参考にこのオーケストレーターをTypeScriptに実装し、展開および繰り返しが容易な、型指定された信頼性の高いオーケストレーターサービスを作成しました。当社独自のDCVオーケストレーター用サーバーの維持が不要なことには、たいへん満足しています。

当社では[Argo Tunnel](https://developers.cloudflare.com/argo-tunnel/)を使用し、Cloudflare WorkersがDCVエージェントと通信できるようにしています。Argo Tunnelを使用することで、当社のDCVエージェントをWorkers環境に容易かつセキュアに公開することができます。CloudflareにはDCVエージェントを実行するデータセンターが約175か所あるため、Argo Tunnelを通して多数のサービスを公開しており、パワーユーザーとして様々な送信元からArgo Tunnelの負荷をテストする機会がありました。Argo Tunnelは、しっかりとこの新しい送信元からの流入を処理してくれました。

### **マルチパスDCVチェッカーへのアクセス取得**

個人や企業でDCVチェッカーにご興味のある方は、[dcv@cloudflare.com](mailto:dcv@cloudflare.com)までお問い合わせください。当社では、皆様の証明書発行に関するセキュリティを、このマルチパスクエリや認証でいかに向上できるかについて、皆様からのご意見をお待ちしています。

新しい種類のBGPおよびIPスプーフィング攻撃は、PKIの基盤を損なう恐れがあり、Webサイトの所有者が、証明書の発行を受ける時にマルチパス検証を求めることも重要です。Cloudflareによるか、自社かに関わらず、すべてのCAでマルチパス検証を使用することをお勧めします。Let’s Encryptのテクニカルリード、Jacob Hoffman-Andrewsが、次のように書いています。

> 「BGPハイジャックは、Web PKIがまだ解決する必要がある大きな課題の1つであり、マルチパス検証はこの解決策の一端を担えると考えています。我々は独自に実装テストを実施し、他のCAにもマルチパスに目を向けるようお勧めしています。」

将来的には、Webサイトの所有者が、CA選択時にマルチパス検証のサポートの有無を確認するようになって欲しい、と願っています。

[暗号化ウィーク](https://blog.cloudflare.com/tag/crypto-week/) [Crypto](https://blog.cloudflare.com/tag/crypto/) [暗号化](https://blog.cloudflare.com/tag/cryptography/) [DNS](https://blog.cloudflare.com/tag/dns/) [BGP](https://blog.cloudflare.com/tag/bgp/)

このページ

オンラインで議論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fsecure-certificate-issuance%2F&t=%E3%83%9E%E3%83%AB%E3%83%81%E3%83%91%E3%82%B9%E3%83%89%E3%83%A1%E3%82%A4%E3%83%B3%E8%AA%8D%E8%A8%BC%EF%BC%88Multipath%20Domain%20Control%20Validation%EF%BC%89%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%97%E3%81%9F%E8%A8%BC%E6%98%8E%E6%9B%B8%E7%99%BA%E8%A1%8C%E3%81%AE%E4%BF%9D%E8%AD%B7)[](https://x.com/intent/post?text=%E3%83%9E%E3%83%AB%E3%83%81%E3%83%91%E3%82%B9%E3%83%89%E3%83%A1%E3%82%A4%E3%83%B3%E8%AA%8D%E8%A8%BC%EF%BC%88Multipath+Domain+Control+Validation%EF%BC%89%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%97%E3%81%9F%E8%A8%BC%E6%98%8E%E6%9B%B8%E7%99%BA%E8%A1%8C%E3%81%AE%E4%BF%9D%E8%AD%B7&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fsecure-certificate-issuance%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fsecure-certificate-issuance%2F)[](https://bsky.app/intent/compose?text=%E3%83%9E%E3%83%AB%E3%83%81%E3%83%91%E3%82%B9%E3%83%89%E3%83%A1%E3%82%A4%E3%83%B3%E8%AA%8D%E8%A8%BC%EF%BC%88Multipath+Domain+Control+Validation%EF%BC%89%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%97%E3%81%9F%E8%A8%BC%E6%98%8E%E6%9B%B8%E7%99%BA%E8%A1%8C%E3%81%AE%E4%BF%9D%E8%AD%B7+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fsecure-certificate-issuance%2F)[](https://mastodonshare.com/?text=%E3%83%9E%E3%83%AB%E3%83%81%E3%83%91%E3%82%B9%E3%83%89%E3%83%A1%E3%82%A4%E3%83%B3%E8%AA%8D%E8%A8%BC%EF%BC%88Multipath+Domain+Control+Validation%EF%BC%89%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%97%E3%81%9F%E8%A8%BC%E6%98%8E%E6%9B%B8%E7%99%BA%E8%A1%8C%E3%81%AE%E4%BF%9D%E8%AD%B7&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fsecure-certificate-issuance%2F)[](https://www.threads.net/intent/post?text=%E3%83%9E%E3%83%AB%E3%83%81%E3%83%91%E3%82%B9%E3%83%89%E3%83%A1%E3%82%A4%E3%83%B3%E8%AA%8D%E8%A8%BC%EF%BC%88Multipath+Domain+Control+Validation%EF%BC%89%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%97%E3%81%9F%E8%A8%BC%E6%98%8E%E6%9B%B8%E7%99%BA%E8%A1%8C%E3%81%AE%E4%BF%9D%E8%AD%B7+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fsecure-certificate-issuance%2F)

## 関連するタグ

[BGP](https://blog.cloudflare.com/ja-jp/tag/bgp/)[CFSSL](https://blog.cloudflare.com/ja-jp/tag/cfssl/)[Crypto Week](https://blog.cloudflare.com/ja-jp/tag/crypto-week/)[DNS](https://blog.cloudflare.com/ja-jp/tag/dns/)[HTTPS](https://blog.cloudflare.com/ja-jp/tag/https/)[TLS](https://blog.cloudflare.com/ja-jp/tag/tls/)[スピードと信頼性](https://blog.cloudflare.com/ja-jp/tag/speed-and-reliability/)[セキュリティ](https://blog.cloudflare.com/ja-jp/tag/security/)[暗号](https://blog.cloudflare.com/ja-jp/tag/cryptography/)

SNS をフォロー

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 新しい投稿のお知らせを受け取るように登録する

メールアドレス

また、あなたのメールアドレスを共有したりすることはございません。

登録する

ご購読ありがとうございます！受信箱を確認して登録してください。
