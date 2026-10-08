---
url: https://blog.cloudflare.com/ja-jp/shift-left-enterprise-scale/
title: \u30a8\u30f3\u30bf\u30fc\u30d7\u30e9\u30a4\u30ba\u898f\u6a21\u3067\u306e\u30b7\u30d5\u30c8\u30ec\u30d5\u30c8\uff1a\u30b3\u30fc\u30c9\u3068\u3057\u3066\u306e\u30a4\u30f3\u30d5\u30e9\u30b9\u30c8\u30e9\u30af\u30c1\u30e3\u3067Cloudflare\u3092\u7ba1\u7406\u3059\u308b\u65b9\u6cd5 | Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:49:46.950283+00:00
---

# エンタープライズ規模でのシフトレフト：コードとしてのインフラストラクチャでCloudflareを管理する方法 | Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/shift-left-enterprise-scale/

[ブログ](https://blog.cloudflare.com/ja-jp/)

[Terraform](https://blog.cloudflare.com/ja-jp/tag/terraform/)[カスタマーゼロ](https://blog.cloudflare.com/ja-jp/tag/customer-zero/)[コードとしてのインフラストラクチャ](https://blog.cloudflare.com/ja-jp/tag/infrastructure-as-code/)1件1件タグを表示

4 タグタグを4件表示

  * 投稿タグ
  * [Terraform](https://blog.cloudflare.com/ja-jp/tag/terraform/)[カスタマーゼロ](https://blog.cloudflare.com/ja-jp/tag/customer-zero/)[コードとしてのインフラストラクチャ](https://blog.cloudflare.com/ja-jp/tag/infrastructure-as-code/)[ドッグフーディング](https://blog.cloudflare.com/ja-jp/tag/dogfooding/)
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



[ドッグフーディング](https://blog.cloudflare.com/ja-jp/tag/dogfooding/)

[Terraform](https://blog.cloudflare.com/ja-jp/tag/terraform/)[カスタマーゼロ](https://blog.cloudflare.com/ja-jp/tag/customer-zero/)[コードとしてのインフラストラクチャ](https://blog.cloudflare.com/ja-jp/tag/infrastructure-as-code/)[ドッグフーディング](https://blog.cloudflare.com/ja-jp/tag/dogfooding/)

2025年12月9日

# エンタープライズ規模でのシフトレフト：コードとしてのインフラストラクチャでCloudflareを管理する方法

![Chase Catelli](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4920AJ222N7ZYMTG9J5S4R.png&w=64&h=64&f=webp&fit=cover&position=center)![Ryan Pesek](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48KFX6XYAA2G7BPBB2SJAX.png&w=64&h=64&f=webp&fit=cover&position=center)![Derek Pitts](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46384YHDK7BZNAPKRR6A3X.png&w=64&h=64&f=webp&fit=cover&position=center)

[Chase Catelli](https://blog.cloudflare.com/ja-jp/author/chase-catelli/)、[Ryan Pesek](https://blog.cloudflare.com/ja-jp/author/ryan-pesek/)、[Derek Pitts](https://blog.cloudflare.com/ja-jp/author/derek-pitts/)

11分で読了

URLをコピー

この記事は以下でも利用可能です [English](https://blog.cloudflare.com/shift-left-enterprise-scale/)、[한국어](https://blog.cloudflare.com/ko-kr/shift-left-enterprise-scale/).

![BLOG-3074 Hero Image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44NKTGQ2WV3CDCEX3SYCG6.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/////fv97ezx4eDq4eDs6efx7evx7ert/////vz/7u7z4+Pr4+Ps6uny7u3z7ezu////////8fH15+ft6Ofu7u708fH17+/y////////9vb57Ozw7u3y9PT49vf68/T2/////////fz+8/L19fT3+/r9/f3++fr7////////////+vn7/Pr8//////////////////////////3///7///////////////////////////7/////////////////)

_このコンテンツは自動機械翻訳サービスによる翻訳版であり、皆さまの便宜のために提供しています。原本の英語版と異なる誤り、省略、解釈の微妙な違いが含まれる場合があります。ご不明な点がある場合は、英語版原本をご確認ください。_

Cloudflareプラットフォームは、Cloudflareにとって極めて重要なシステムです。当社は自社のカスタマーゼロであり、自社の製品を使って自社サービスを安全にし、最適化しています。

セキュリティ部門では、専任のCustomer Zeroチームが独自のポジションを活かして、常に忠実度の高いフィードバックループを製品およびエンジニアリングに提供し、製品の継続的改善を推進しています**。** そして、これはグローバル規模で行われますので、1つの設定ミスが数秒でエッジ全体に伝播し、意図しない結果につながる可能性があります。たった1つの小さなミスが重要なアプリケーションから従業員をロックアウトしたり、本番サービスを停止させたりする可能性があることを知って、本番環境への変更を躊躇したことがあるなら、その気持ちはわかります。意図しない結果のリスクは現実的であり、夜も眠れません。

これには興味深い課題があります。人的ミスを最小限に抑えながら、数百もの内部本番Cloudflareアカウントを一貫して保護する方法は？

Cloudflareのダッシュボードは[可観測性](https://www.cloudflare.com/learning/performance/what-is-observability/)と分析には優れているものの、数百ものアカウントを手動でクリックしてセキュリティ設定が同じであることを確認するのは間違いです。私たちの健全性とセキュリティを維持するために、設定を手作業のポイントアンドクリックタスクとして扱うのを止め、コードとして扱うようになりました。当社は、「シフトレフト」の原則を採用し、セキュリティチェックを開発の最も早い段階に移動させました。

これは当社にとって抽象的な企業目標ではありません。インシデントが起こる前にエラーをキャッチするためのサバイバルメカニズムであり、ガバナンスアーキテクチャを根本的に変える必要がありました。

## Shiftレフトが私たちにとって意味すること

「シフトレフト（Shift left）」は、ソフトウェア開発ライフサイクル（SDLC）において検証手順をより早い段階で移動させることを指します。現実的には、テスト、セキュリティ監査、ポリシーコンプライアンスチェックを、[継続的インテグレーションおよび継続的デプロイメント（CI/CD）パイプライン](https://www.cloudflare.com/learning/serverless/glossary/what-is-ci-cd/)に直接統合することを意味します。マージリクエストの段階で問題や設定ミスを検知することで、デプロイ後に発見するのではなく、修正コストが最も少ない時に問題を特定します。

Cloudflareでシフトレフトの原則を適用する際、4つの重要な原則が注目されます。

  * **一貫性** : 設定はアカウント間で簡単にコピーして再利用できる必要があります。
  * **スケーラビリティ** ：大規模な変更は、複数のアカウントに迅速に適用できます。
  * **Observability** ：設定は、現在の状態、正確性、セキュリティを誰でも監査できる必要があります。
  * **ガバナンス** ：Guardrailsは事前予防的である必要があります。つまり、インシデントを避けるために、デプロイ前に強制適用するのです。



## 本番IaC運用モデル

このモデルをサポートするために、すべての本番アカウントをInfrastructure as Code（IaC）で管理するように移行しました。すべての変更は追跡され、ユーザー、コミット、および内部チケットに結びつけられます。チームは引き続きダッシュボードを使用して分析やインサイトを確保しますが、本番環境での重大な変更はすべてコードで行われます。

このモデルは、すべての変更をピアレビューすることを保証し、ポリシーはセキュリティチームによって設定されますが、所有するエンジニアリングチームによって実装されます。

このセットアップは、[ _Terraform_](https://developer.hashicorp.com/terraform)とカスタムCI/CDパイプラインの2つの主要なテクノロジーに基づいています。

## 当社のエンタープライズIaCスタック

当社がTerraformを選択した理由は、成熟したオープンソースエコシステム、強力なコミュニティサポート、Policy as Codeツールとの深い統合にあります。さらに、[ _Cloudflare Terraform Provider_](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)を社内で使用することで、ユーザーのために積極的に[ _ドッグフーディングし_](https://blog.cloudflare.com/tag/dogfooding/)、ユーザーのために体験を改善することができます。

数百のアカウントと1日あたり約30件のマージリクエスト規模に対応するため、CI/CDパイプラインは[ _GitLab_](https://about.gitlab.com/)と統合された[ _Atlantis_](https://www.runatlantis.io/)で稼働しています。また、ステートファイルを安全に保存するためのブローカーとして機能するカスタムgoプログラムであるtfstate-butlerを使用することもできます。

tfstate-butlerは、TerraformのHTTPバックエンドとして動作します。設計の主な推進要因はセキュリティでした。ステートファイルごとに一意の暗号化キーを確保し、潜在的な侵害の影響範囲を制限することができるからです。

すべての内部アカウント構成は、中央管理型の[ _monorepo_](https://developers.cloudflare.com/pages/configuration/monorepos/)で定義されます。個々のチームが特定の設定を所有およびデプロイし、この中央リポジトリの各セクションの指定されたコード所有者であることから、説明責任を確保します。この構成の詳細については、[ _CloudflareがTerraformを使用してCloudflareを管理する方法_](https://blog.cloudflare.com/terraforming-cloudflare-at-cloudflare/)をご覧ください。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3074 Image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44A7NW34R9Z3J0D3667THE.png&w=715&h=388&f=webp&fit=cover&position=center)

コードとしてのインフラストラクチャのデータフロー図

## コードとしてのベースラインとポリシー

シフトレフト戦略全体の要点は、すべての社内本番Cloudflareアカウントの強力なセキュリティベースラインを確立することです。ベースラインは、コードで定義されたセキュリティポリシーの集合です（Policy as Code）。このベースラインは単なるガイドラインではなく、当社がプラットフォーム全体に適用する必要なセキュリティ設定（最大セッション長、必要なログ、特定のWAF設定など）です。

このセットアップでは、ポリシーの適用が手動による監査から自動化されたゲートに移行します。当社では、Atlantis Conftest Policy Checking機能を通じて、[ _Open Policy Agent (OPA)_](https://www.openpolicyagent.org/)フレームワークとそのポリシー言語である[ _Rego_](https://www.openpolicyagent.org/docs/policy-language#what-is-rego)を使用しています。

## コードとしてポリシーを定義

Regoポリシーは、すべてのCloudflareプロバイダーリソースのベースラインを構成する特定のセキュリティ要件を定義します。現在、約50のポリシーを維持しています。

たとえば、アクセスポリシーで使用を許可される@cloudflare.comのメールのみを検証するRegoポリシーがあります。
    
    
    # validate no use of non-cloudflare email
    warn contains reason if {
        r := tfplan.resource_changes[_]
        r.mode == "managed"
        r.type == "cloudflare_access_policy"
    
        include := r.change.after.include[_]
        email_address := include.email[_]
        not endswith(email_address, "@cloudflare.com")
    
        reason := sprintf("%-40s :: only @cloudflare.com emails are allowed", [r.address])
    }
    warn contains reason if {
        r := tfplan.resource_changes[_]
        r.mode == "managed"
        r.type == "cloudflare_access_policy"
    
        require := r.change.after.require[_]
        email_address := require.email[_]
        not endswith(email_address, "@cloudflare.com")
    
        reason := sprintf("%-40s :: only @cloudflare.com emails are allowed", [r.address])
    }

## ベースラインの強化

ポリシーチェックはすべてのマージリクエスト（MR）に対して実行され、デプロイ _前に_ 設定が準拠していることを確認します。ポリシーチェックの出力は、GitLab MRのコメントスレッドに直接表示されます。

ポリシーの適用は2つのモードで動作します。

  1. **警告：** MRにコメントを残しますが、マージは許可されます。
  2. **拒否：** デプロイメントを完全にブロックします。



ポリシーチェックが、MRで適用されている設定がベースラインから逸脱していると判断した場合、出力はどのリソースがコンプライアンス違反になっているかを返します。

以下の例は、マージリクエストの3つの不一致を特定するポリシーチェックの出力を示しています。
    
    
    WARN - cloudflare_zero_trust_access_application.app_saas_xxx :: "session_duration" must be less than or equal to 10h
    
    WARN - cloudflare_zero_trust_access_application.app_saas_xxx_pay_per_crawl :: "session_duration" must be less than or equal to 10h
    
    WARN - cloudflare_zero_trust_access_application.app_saas_ms :: you must have at least one require statement of auth_method = "swk"
    
    41 tests, 38 passed, 3 warnings, 0 failures, 0 exception

## ポリシー例外の処理

例外が必要であることは理解していますが、ポリシー自体と同じ厳格さで管理する必要があります。チームで例外が必要な場合は、Jira経由でリクエストを提出します。

Customer Zeroチームによって承認されると、中央例外.regoリポジトリにプルリクエストを送信することで、例外が正式化されます。さまざまなレベルで例外が発生する場合があります：

  * **アカウント** ：account_xをポリシーyから除外します。
  * **リソースカテゴリ** : account_xのすべてのリソース_aをポリシーyから除外します。
  * **特定のリソース** : account_xのリソース_a_1をポリシーyから除外します。



この例では、2つの個別のCloudflareアカウントの下にある5つの特定のアプリケーションでのセッション長の例外を示しています。
    
    
    {  
        "exception_type": "session_length",
        "exceptions": [
            {
                "account_id": "1xxxx",
                  "tf_addresses": [
                    "cloudflare_access_application.app_identity_access_denied",
                    "cloudflare_access_application.enforcing_ext_auth_worker_bypass",
                    "cloudflare_access_application.enforcing_ext_auth_worker_bypass_dev",
                ],
            },
            {
                "account_id": "2xxxx",
                  "tf_addresses": [
                    "cloudflare_access_application.extra_wildcard_application",
                    "cloudflare_access_application.wildcard",
                ],
            },
        ],
    }

## 課題と学んだ教訓

私たちの道のりは障害がなかったわけではありません。何年ものクリック操作（ダッシュボード内で直接行う手動変更）が、何百ものアカウントに散在していました。既存のカオスをコードシステムとして厳格なインフラストラクチャにインポートしようとすることは、まるで動いている車のタイヤを交換しようとしているような感じでした。現在まで、リソースのインポートは継続的なプロセスとして続いています。

自社ツールの限界にも直面しました。Cloudflare Terraformプロバイダーには、この規模のインフラストラクチャを管理しようとする場合にのみ発生するエッジケースが見つかりました。これは、ほんのわずかな速度のバンプではありませんでした。彼らは、自社のドッグフーディングの必要性を痛感させられ、それにより、より良いソリューションを構築することができました。

この摩擦によって、私たちが立ち位置が何であるかが明確になり、3つの努力の教訓につながりました。

## 教訓1：高い参入障壁が原因で導入が進まない

大規模なIaCの展開における最初の課題は、手動で設定された既存のリソースのオンボーディングです。チームには、Terraformリソースを手動で作成してブロックをインポートする方法と、[ _cf-terraforming_](https://github.com/cloudflare/cf-terraforming)を使用する方法の2つの選択肢がありました。

Terraformの流暢性はチームによって異なることがすぐにわかり、既存のリソースを手動でインポートするための学習曲線は、私たちが予想していたよりもはるかに急であることが判明しました。

幸いなことに、cf-terraformingコマンドラインユーティリティは、Cloudflare APIを使用して、必要なTerraformコードとimportステートメントを自動的に生成し、移行プロセスを大幅に加速します。

また、経験豊富なエンジニアがチームをガイドしてプロバイダーの微妙な違いなどを説明し、複雑なインポートを解除する手助けをする社内コミュニティも形成しました。

## レッスン2：ドリフトが発生する

また、緊急の変更を促すためにIaCプロセスがバイパスされるときに発生する設定のドリフトにも対処しなければなりませんでした。ダッシュボードで直接編集を行うと、インシデント発生時に迅速に作業できますが、Terraformの状態を現実と同期したままではありません。

Terraformで定義された状態と、Cloudflare APIを介して実際にデプロイされた状態を常に比較する、カスタムドリフト検出サービスを実装しました。ドリフトが検出されると、自動システムが内部チケットを作成し、さまざまなサービスレベル契約（SLA）とともに所有チームに割り当てて修正します。

## レッスン3：自動化が重要

Cloudflareは革新が速く、製品やAPIは増え続けています。残念ながら、それは私たちのTerraformプロバイダーが製品との機能パリティの観点で後れを取ることがあったことを意味しました。

この問題は、OpenAPI仕様に基づいてTerraformプロバイダーを自動生成する[ _v5プロバイダー_](https://blog.cloudflare.com/automatically-generating-cloudflares-terraform-provider/)のリリースにより解決しました。この移行には、コード生成へのアプローチを強化したため、問題が生じましたが、このアプローチにより、APIとTerraformが同期され、機能がドリフトする可能性が減ります。

## 核教訓：プロアクティブ>リアクティブ

セキュリティベースラインを一元化し、ピアレビューを義務付け、変更を本番環境に適用する前にポリシーを適用することで、設定ミス、偶発的な削除、ポリシー違反の可能性を最小限に抑えます。このアーキテクチャは手作業によるミスを防ぐだけでなく、チームが変更をコンプライアンスに準拠していると確信できるため、エンジニアリングのベロシティを向上させるのに役立ちます。

Customer Zeroとの取り組みから得られた重要な教訓は次のとおりです。Cloudflareダッシュボードは日常的な運用には優れているものの、エンタープライズレベルの規模と一貫したガバナンスを実現するには、異なるアプローチが必要であるということです。Cloudflare設定を実行するコードとして扱うことで、安全かつ自信を持ってスケーリングできます。

コードとしてのインフラストラクチャに関するご意見をお聞かせください[ _community.cloudflare.com_](http://community.cloudflare.com)で会話を続け、あなたの経験を共有してください。

このページ

オンラインで議論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fshift-left-enterprise-scale%2F&t=%E3%82%A8%E3%83%B3%E3%82%BF%E3%83%BC%E3%83%97%E3%83%A9%E3%82%A4%E3%82%BA%E8%A6%8F%E6%A8%A1%E3%81%A7%E3%81%AE%E3%82%B7%E3%83%95%E3%83%88%E3%83%AC%E3%83%95%E3%83%88%EF%BC%9A%E3%82%B3%E3%83%BC%E3%83%89%E3%81%A8%E3%81%97%E3%81%A6%E3%81%AE%E3%82%A4%E3%83%B3%E3%83%95%E3%83%A9%E3%82%B9%E3%83%88%E3%83%A9%E3%82%AF%E3%83%81%E3%83%A3%E3%81%A7Cloudflare%E3%82%92%E7%AE%A1%E7%90%86%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95)[](https://x.com/intent/post?text=%E3%82%A8%E3%83%B3%E3%82%BF%E3%83%BC%E3%83%97%E3%83%A9%E3%82%A4%E3%82%BA%E8%A6%8F%E6%A8%A1%E3%81%A7%E3%81%AE%E3%82%B7%E3%83%95%E3%83%88%E3%83%AC%E3%83%95%E3%83%88%EF%BC%9A%E3%82%B3%E3%83%BC%E3%83%89%E3%81%A8%E3%81%97%E3%81%A6%E3%81%AE%E3%82%A4%E3%83%B3%E3%83%95%E3%83%A9%E3%82%B9%E3%83%88%E3%83%A9%E3%82%AF%E3%83%81%E3%83%A3%E3%81%A7Cloudflare%E3%82%92%E7%AE%A1%E7%90%86%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fshift-left-enterprise-scale%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fshift-left-enterprise-scale%2F)[](https://bsky.app/intent/compose?text=%E3%82%A8%E3%83%B3%E3%82%BF%E3%83%BC%E3%83%97%E3%83%A9%E3%82%A4%E3%82%BA%E8%A6%8F%E6%A8%A1%E3%81%A7%E3%81%AE%E3%82%B7%E3%83%95%E3%83%88%E3%83%AC%E3%83%95%E3%83%88%EF%BC%9A%E3%82%B3%E3%83%BC%E3%83%89%E3%81%A8%E3%81%97%E3%81%A6%E3%81%AE%E3%82%A4%E3%83%B3%E3%83%95%E3%83%A9%E3%82%B9%E3%83%88%E3%83%A9%E3%82%AF%E3%83%81%E3%83%A3%E3%81%A7Cloudflare%E3%82%92%E7%AE%A1%E7%90%86%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fshift-left-enterprise-scale%2F)[](https://mastodonshare.com/?text=%E3%82%A8%E3%83%B3%E3%82%BF%E3%83%BC%E3%83%97%E3%83%A9%E3%82%A4%E3%82%BA%E8%A6%8F%E6%A8%A1%E3%81%A7%E3%81%AE%E3%82%B7%E3%83%95%E3%83%88%E3%83%AC%E3%83%95%E3%83%88%EF%BC%9A%E3%82%B3%E3%83%BC%E3%83%89%E3%81%A8%E3%81%97%E3%81%A6%E3%81%AE%E3%82%A4%E3%83%B3%E3%83%95%E3%83%A9%E3%82%B9%E3%83%88%E3%83%A9%E3%82%AF%E3%83%81%E3%83%A3%E3%81%A7Cloudflare%E3%82%92%E7%AE%A1%E7%90%86%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fshift-left-enterprise-scale%2F)[](https://www.threads.net/intent/post?text=%E3%82%A8%E3%83%B3%E3%82%BF%E3%83%BC%E3%83%97%E3%83%A9%E3%82%A4%E3%82%BA%E8%A6%8F%E6%A8%A1%E3%81%A7%E3%81%AE%E3%82%B7%E3%83%95%E3%83%88%E3%83%AC%E3%83%95%E3%83%88%EF%BC%9A%E3%82%B3%E3%83%BC%E3%83%89%E3%81%A8%E3%81%97%E3%81%A6%E3%81%AE%E3%82%A4%E3%83%B3%E3%83%95%E3%83%A9%E3%82%B9%E3%83%88%E3%83%A9%E3%82%AF%E3%83%81%E3%83%A3%E3%81%A7Cloudflare%E3%82%92%E7%AE%A1%E7%90%86%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2Fshift-left-enterprise-scale%2F)

## 関連するタグ

[Terraform](https://blog.cloudflare.com/ja-jp/tag/terraform/)[カスタマーゼロ](https://blog.cloudflare.com/ja-jp/tag/customer-zero/)[コードとしてのインフラストラクチャ](https://blog.cloudflare.com/ja-jp/tag/infrastructure-as-code/)[ドッグフーディング](https://blog.cloudflare.com/ja-jp/tag/dogfooding/)

SNS をフォロー

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 新しい投稿のお知らせを受け取るように登録する

メールアドレス

また、あなたのメールアドレスを共有したりすることはございません。

登録する

ご購読ありがとうございます！受信箱を確認して登録してください。
