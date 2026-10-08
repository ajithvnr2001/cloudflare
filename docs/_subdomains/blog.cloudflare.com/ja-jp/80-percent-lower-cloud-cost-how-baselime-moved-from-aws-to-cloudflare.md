---
url: https://blog.cloudflare.com/ja-jp/80-percent-lower-cloud-cost-how-baselime-moved-from-aws-to-cloudflare/
title: Baselime\u3092AWS\u304b\u3089Cloudflare\u3078\u79fb\u884c\uff1a\u30a2\u30fc\u30ad\u30c6\u30af\u30c1\u30e3\u304c\u30b7\u30f3\u30d7\u30eb\u3001\u30d1\u30d5\u30a9\u30fc\u30de\u30f3\u30b9\u304c\u6539\u5584\u3001\u30af\u30e9\u30a6\u30c9\u30b3\u30b9\u30c8\u304c80%\u4ee5\u4e0a\u524a\u6e1b | Cloudflare \u30d6\u30ed\u30b0
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:53:29.491461+00:00
---

# BaselimeをAWSからCloudflareへ移行：アーキテクチャがシンプル、パフォーマンスが改善、クラウドコストが80%以上削減 | Cloudflare ブログ

> Source: https://blog.cloudflare.com/ja-jp/80-percent-lower-cloud-cost-how-baselime-moved-from-aws-to-cloudflare/

[ブログ](https://blog.cloudflare.com/ja-jp/)

[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[Observability](https://blog.cloudflare.com/ja-jp/tag/observability/)[パフォーマンス](https://blog.cloudflare.com/ja-jp/tag/performance/)1件1件タグを表示

4 タグタグを4件表示

  * 投稿タグ
  * [Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[Observability](https://blog.cloudflare.com/ja-jp/tag/observability/)[パフォーマンス](https://blog.cloudflare.com/ja-jp/tag/performance/)[開発者プラットフォーム](https://blog.cloudflare.com/ja-jp/tag/developer-platform/)
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



[開発者プラットフォーム](https://blog.cloudflare.com/ja-jp/tag/developer-platform/)

[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[Observability](https://blog.cloudflare.com/ja-jp/tag/observability/)[パフォーマンス](https://blog.cloudflare.com/ja-jp/tag/performance/)[開発者プラットフォーム](https://blog.cloudflare.com/ja-jp/tag/developer-platform/)

2024年10月31日

# BaselimeをAWSからCloudflareへ移行：よりシンプルなアーキテクチャでより優れたパフォーマンスを実現し、クラウドコストを80%以上削減

![Boris Tane](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4776DVTF41B4B1HEER22V8.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Boris Tane](https://blog.cloudflare.com/ja-jp/author/boris-tane/)

16分で読了

URLをコピー

この記事は以下でも利用可能です [English](https://blog.cloudflare.com/80-percent-lower-cloud-cost-how-baselime-moved-from-aws-to-cloudflare/).

![image8](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49P7F9DRA4PZ177SR5ZVFB.png&w=1800&h=1013&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///////87vHy4ebt4ebx6O317O/x6+zn///////+6u301t7v1d7z4Of36u3z7e7p////////5+v3zdjzytf32eP76e348PDu////////6u78z9n4zNj83OX/7fH99vXz////////9Pb/3uT93OP/6e//9vj//Pr5////////////8/P/8vT/+/z////////+////////////////////////////////////////////////////////////////)

## はじめに

2024年4月に[ _BaselimeがCloudflareの傘下に加わった_](https://blog.cloudflare.com/cloudflare-acquires-baselime-expands-observability-capabilities/)とき、当社のアーキテクチャには数百のAWS Lambda関数、数十のデータベース、そして大量のキューが溢れていました。複雑さが足かせとなり、クラウドのコストは急速に増大していました。現在、当社はCloudflare上に[ _Baselime_](https://baselime.io/)と[ _Workers Observability_](https://developers.cloudflare.com/workers/observability/logs/workers-logs/)を構築しており、クラウドコンピューティング料金を80%以上節約できる見込みです。Cloudflareの想定コストは、スタンドアロンサービスであるBaselimeに対するもので、[ _Workers有料プラン_](https://developers.cloudflare.com/workers/platform/pricing/)に基づいて算出されています。大幅なコスト削減を実現しただけでなく、アーキテクチャを簡素化し、全体的な遅延、スケーラビリティ、信頼性を向上させました。

コスト（日あたり）| 移行前（AWS）| 移行後（Cloudflare）  
---|---|---  
コンピューティング| $650 - AWS Lambda| $25 - Cloudflare Workers  
CDN| $140 - Cloudfront| $0 - 無料  
データストリームと分析データベース| $1,150 - Kinesis Data Stream + EC2| $300 - Workers Analytics Engine  
合計（日あたり）| $1,940| $325  
全体（年あたり）| $708,100| $118,625（83%のコスト削減）  
  
 _表1：AWSとWorkersのコスト比較（米ドル）_

Cloudflareの傘下となった際、すぐに利用量が急増し、発表後1週間のうちに、毎日10億件以上のイベントを処理することとなり、アクティブユーザー数は3倍に増えました。

プラットフォームが拡大するにつれて、スケーラビリティ、信頼性、コストに関する新たな考慮事項とともに、リアルタイムでの可観測性を管理するという課題も深刻化の一途をたどりました。これを受け、Cloudflare開発者プラットフォーム上でBaselimeを再構築した結果、運用上のオーバーヘッドを削減しながら、迅速にイノベーションを実現することができました。

## 初期アーキテクチャ — すべてAWS上

当社のアーキテクチャは当初、すべてAmazon Web Services（AWS）上に構築されていました。ここでは、毎日数百億件のイベントの取り込み、処理、保存に対応するデータパイプラインに焦点を当てて説明します。

このパイプラインは、AWS Lambda、Cloudfront、Kinesis、EC2、DynamoDB、ECS、ElastiCache上に構築されていました。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![image1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44VVZHW3G3BK73Q7AJ5GEQ.png&w=715&h=417&f=webp&fit=cover&position=center)

 _図1：初期データパイプラインアーキテクチャ_

主な要素は次の通りです。

  * **データレセプター** ：OpenTelemetry、Cloudflare Logpush、CloudWatch、Vercelなどの複数のソースからのテレメトリデータを受信します。データの検証、認証、そして各ソースからのデータの共通内部フォーマットへの変換についても対応します。データレセプターは、データソースに応じて、AWS Lambda（関数URLとCloudfrontを使用）またはECS Fargateのいずれかにデプロイされました。
  * **Kinesis Data Stream** ：データレセプターからのデータを、次のステップであるデータ処理に向けて転送します。
  * **プロセッサー** ：ストレージ用データの拡充と変換に対応する単一のAWS Lambda関数。この関数は、リアルタイムのエラー追跡とログのパターン検出も実行していました。
  * **ClickHouseクラスター** ：すべてのテレメトリデータは最終的にインデックス化され、EC2のセルフホスト型ClickHouseクラスタに保存されました。



これらの主な要素に加え、エラー処理、再試行、メタデータの保存に対応するため、既存スタックではFirehose、S3バケット、SQS、DynamoDB、RDSとのオーケストレーションも必要でした。

このアーキテクチャは、はじめのうちはうまく機能していましたが、より多くのお客様に対応するためにソリューションを拡張するにつれ、大きな問題が生じるようになりました。

データレセプターとKinesis Data Stream間のインターフェースでの再試行処理は複雑で、Firehose、S3バケット、SQS、別のLambda関数の導入とオーケストレーションを必要としました。

セルフホスト型のClickHouseでも、コストをコントロールしながらも増大するユーザーベースに対応するために、継続的に容量を計画し、設定を更新しなければならないため、重大な課題が大規模で生じることとなりました。

また、ワークロードの増大に伴い、特にAWS Lambda、Kinesis、EC2において、予測不可能な勢いでコストが増大し始めました。Cloudfront（Lambda関数URLの前に付加するカスタムドメインのために必要）やDynamoDBなどでも、AWS Lambda、Kinesis、EC2と比較するとそれほど明白ではないものの、コストが増大していました。具体的には、AWS LambdaのI/O操作に費やす時間が特に高コストでした。データレセプターからClickHouseクラスターまで、すべてのステップでデータを次の段階に移すには、ネットワークリクエストが完了するのを待つ必要があり、Lambda関数のウォールタイムの70%以上を占めていました。

一言で言えば、私たちは常にアラートに悩まされ、イノベーションのペースは遅く、コストは制御不能に陥っていました。

さらに、このソリューション全体は単一のAWSリージョン（eu-west-1）に展開されていました。その結果、ヨーロッパ大陸以外の開発者がBaselimeにログやトレースを送信する際には長い遅延が発生しました。

## 最新アーキテクチャ — Cloudflareへの移行

[ _Cloudflare開発者プラットフォーム_](https://www.cloudflare.com/en-gb/developer-platform/products/)への移行により、コスト、簡素さ、俊敏性に妥協することなく、極めて高速かつグローバルに分散され、高いスケーラビリティを備えたアーキテクチャを実現するにはどうすればよいかを改めて考えることができました。この新しいアーキテクチャは、Cloudflareのプリミティブ上に構築されています。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![image5](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44A1WKEMKYB67WAZ1FC243.png&w=715&h=453&f=webp&fit=cover&position=center)

 _図2：最新データパイプラインアーキテクチャ_

### Cloudflare Workers：Baselimeの中核

[ _Cloudflare Workers_](https://www.cloudflare.com/developer-platform/workers/)は今や、私たちが行うすべての中核となっています。すべてのデータレセプターとプロセッサはWorkers内で実行されます。Workersはコールドスタート時間を最小限に抑え、デフォルトでグローバルにデプロイされます。そのため、開発者がBaselimeにイベントを送信する際も、遅延は常に短いものです。

さらに、パイプラインのステップ間のデータ転送には[ _JavaScriptネイティブのRPC_](https://blog.cloudflare.com/javascript-native-rpc/)を多用しています。低遅延で軽量であり、コンポーネント間の通信を簡素化します。これにより、別々のコンポーネントが完全に別々のアプリケーションとしてではなく、同じプロセス内の関数のように機能するため、アーキテクチャがさらに簡素化されます。
    
    
    export default {
      async fetch(request: Request, env: Bindings, ctx: ExecutionContext): Promise<Response> {
          try {
            const { err, apiKey } = auth(request);
            if (err) return err;
    
            const data = {
              workspaceId: apiKey.workspaceId,
              environmentId: apiKey.environmentId,
              events: request.body
            };
            await env.PROCESSOR.ingest(data);
    
            return success({ message: "Request Accepted" }, 202);
          } catch (error) {
            return failure({ message: "Internal Error" });
          }
      },
    };

_コードブロック1：JavaScriptネイティブRPCを使ってプロセッサを実行する簡素化されたデータレセプター。_

Workersは、[ _Rate Limitingバインディング_](https://developers.cloudflare.com/workers/runtime-apis/bindings/rate-limit/)も公開しているため、サービスにレート制限を自動的に追加できるようになりました。これまでは、DynamoDBとElastiCacheを組み合わせて自分たちで構成する必要がありました。

さらに、Worker呼び出し内で`ctx.waitUntil`を多用して、リクエスト/レスポンスパスの外にデータ変換をオフロードしています。これにより、開発者がデータレセプターに送信する呼び出しの遅延がさらに短縮されます。

### Durable Objects：ステートフルなデータ処理

[ _Durable Objects_](https://www.cloudflare.com/en-gb/developer-platform/durable-objects/)は、サーバーレス環境でステートフルなアプリケーションを構築できるようにする、Cloudflare開発者プラットフォーム内にある独自のサービスです。当社では、リアルタイムのエラー追跡とログのパターン検出の両方のために、データパイプラインでDurable Objectsを使用しています。

例えば、リアルタイムでエラーを追跡するために、私たちは新しいタイプのエラーごとにDurable Objectを作成します。そしてこのDurable Objectが、エラーの頻度、お客様に通知するタイミング、およびエラーの通知チャネルを追跡する役割を担います。**このような単一ビルディングブロックでの実装により、ElastiCache、Kinesis、複数のLambda関数がRDSデータベースを高頻度のエラーによる過負荷から保護するためにオーケストレーションを行う必要がなくなります。**

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![image4](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW448XXCVWF6R3PTDZPAY0K1.png&w=715&h=382&f=webp&fit=cover&position=center)

 _図3：リアルタイムエラー検出アーキテクチャの比較_

Durable Objectsを使用すると、データパイプライン内の状態管理の一貫性と同時実行性を正確に制御することができます。

データパイプラインに加えて、当社ではDurable Objectsをアラートに使用しています。以前のアーキテクチャでは、EventBridge Scheduler、SQS、DynamoDB、複数のAWS Lambda関数をオーケストレーションする必要がありましたが、Durable Objectsでは、すべて`alarm`ハンドラ内で処理されます。

### Workers Analytics Engine：大規模な高カーディナリティ分析

当社独自のClickHouseクラスタの管理は技術的に興味深いものの困難であり、開発者は最高の可観測性をもって作業にあたることはできませんでした。今回の移行により、サーバーインスタンスの管理に時間を費やす必要がなくなり、私たちは製品をよりよいものにするために多くの時間を割けるようになりました。

[ _Workers Analytics Engine_](https://developers.cloudflare.com/analytics/analytics-engine/)により、スケーラブルな高カーディナリティ分析データベースに同期的にイベントを書き込むことができます。データベースは、Workers Analytics Engineを支える技術と同じ技術の上に構築しました。また高カーディナリティに加え、高次元性をネイティブに有効にするために、Workers Analytics Engineに内部変更を加えました。

さらに、Workers Analytics Engineと当社のソリューションは[ _CloudflareのABR分析_](https://blog.cloudflare.com/explaining-cloudflares-abr-analytics/)を活用しています。ABRはAdaptive Bit Rateの略で、テレメトリデータを異なる解像度（100％～0.0001％）で複数のテーブルに保存することができます。0.0001%のデータを含むテーブルに対してクエリを実行する場合、すべてのデータを持つテーブルよりもはるかに高速になります。ただし、精度がトレードオフとなります。そのため、システムにクエリが送信されると、Workers Analytics Engineはクエリを実行するのに最も適切なテーブルを動的に選択し、クエリ時間と精度の両方を最適化します。ユーザーは、データセットのサイズやクエリの所要時間に関係なく、最適なクエリ時間で最も正確な結果を得られます。常にすべてのデータセットに対してクエリを実行していた旧システムと比較して、新しいシステムは全ユーザーベースとユースケースで高速なクエリを提供できるようになりました _。_

これらのコアサービス（Workers、Durable Objects、Workers Analytics Engine）に加えて、新しいアーキテクチャはCloudflare開発者プラットフォームのその他のビルディングブロックを活用しています。具体的には、非同期メッセージ、サービスの分離、イベント駆動型アーキテクチャを可能にする[ _Queues_](https://www.cloudflare.com/en-gb/developer-platform/products/cloudflare-queues/)、トランザクションデータ（クエリ、アラート、ダッシュボード、構成など）のメインデータベースである[ _D1_](https://www.cloudflare.com/en-gb/developer-platform/d1/)、迅速な分散型ストレージを実現する[ _Workers KV_](https://www.cloudflare.com/en-gb/developer-platform/workers-kv/)、そして当社のすべてのAPI用の[ _Hono_](https://hono.dev/)などです。

## 移行の方法

Baselimeはイベント駆動型アーキテクチャに基づいており、すべてのユーザーアクションがイベントをトリガーします。つまり、ユーザーの作成、ダッシュボードの編集、その他のアクションの実行など、すべてのユーザーアクションがイベントとして記録され、システムの残りの部分に出力されるという原則に基づいて動作します。そのため、Cloudflareへの移行には、アップタイムとデータの一貫性を損なうことなく、イベント駆動型アーキテクチャを移行することが含まれました。以前はAWS EventBridgeとSQSで稼働していましたが、Cloudflare Queuesに完全に移行しました。

その際、[ _ストラングラーフィグパターン_](https://martinfowler.com/bliki/StranglerFigApplication.html)に従い、ソリューションをAWSからCloudflareに段階的に移行していきました。システムの中断を最小限に抑えながら、システムの特定の部分を新しいサービスに徐々に置き換えていく方式です。プロセスの初期段階で、移行中のすべてのトランザクションイベント処理のバックボーンとして機能する中央のCloudflare Queueを作成しました。新規ユーザーの登録であろうとダッシュボードの編集であろうと、すべてのイベントがこのQueueに集約されました。そこから、イベントは動的にルーティングされ、各イベントはアプリケーションの関連する部分に動的にルーティングされます。ユーザーアクションはD1とKVに同期され、移行中もAWSとCloudflareの両方ですべてのユーザーアクションがミラーリングされます。

この同期メカニズムにより、一貫性を維持し、ユーザーがBaselimeを操作する中でデータが失われることは一切ありませんでした。

以下は、イベントがどのように処理されるかを示した例です。
    
    
    export default {
      async queue(batch, env) {
        for (const message of batch.messages) {
          try {
            const event = message.body;
            switch (event.type) {
              case "WORKSPACE_CREATED":
                await workspaceHandler.create(env, event.data);
                break;
              case "QUERY_CREATED":
                await queryHandler.create(env, event.data);
                break;
              case "QUERY_DELETED":
                await queryHandler.remove(env, event.data);
                break;
              case "DASHBOARD_CREATED":
                await dashboardHandler.create(env, event.data);
                break;
              //
              // Many more events...
              //
              default:
                logger.info("Matched no events", { type: event.type });
            }
            message.ack();
          } catch (e) {
            if (message.attempts < 3) {
              message.retry({ delaySeconds: Math.ceil(30 ** message.attempts / 10), });
            } else {
              logger.error("Failed handling event - No more retrys", { event: message.body, attempts: message.attempts }, e);
            }
          }
        }
      },
    } satisfies ExportedHandler<Env, InternalEvent>;

_コードブロック2：簡素化された、移行中の内部イベント処理_

当社は、データパイプラインをAWSからCloudflareに、アウトサイドイン方式で移行しました。データレセプターから始め、段階的にデータプロセッサとClickHouseクラスタを新しいアーキテクチャに移行しました。テレメトリデータ（ログ、メトリクス、トレース、ワイドイベントなど）は、ClickHouse（AWS内）とWorkers Analytics Engineの両方に、保持期間は30日間で同時に書き込みました。

最後のステップは、これまでAWS LambdaとECSコンテナでホストされていたすべてのエンドポイントを、Cloudflare Workersに書き換えることでした。これらのWorkersの準備ができたら、既存のLambda関数ではなくWorkersを参照するようにDNSレコードを切り替えるだけです。

複雑な作業にもかかわらず、データパイプラインからすべてのAPIエンドポイントの書き換えまで、移行プロセス全体は、3人のエンジニアからなるチームが3か月足らずで完了できました。

## 最終的にクラウド料金を80%以上削減

### データレセプター関連コストの削減

2024年6月上旬にデータレセプターをAWSからCloudflareに切り替えた後、AWS Lambdaのコストが85%以上削減されました。これらのコストは主に、データレセプターが同じリージョン内にあるKinesis Data Streamにデータを送信するのに費やしたI/O時間によって発生していました。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![image3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW484DNMCX9V8TXH9AK1S0E1.png&w=715&h=442&f=webp&fit=cover&position=center)

 _図4：Baselimeの1日あたりのAWS Lambdaコスト[注：データのギャップは、クラウドアカウントの親組織が変更された際にAWS Cost Explorerでデータ損失が発生したことによります。]_

さらに、Cloudfrontを使用して、データレセプターを参照するカスタムドメインを有効にしていました。データレセプターをCloudflareに移行した後、Cloudfrontは必要なくなりました。それに応じて、Cloudfrontの費用は0ドルまで削減されました。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![image2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44XFTX0HDX2CBQX7C038FN.png&w=715&h=443&f=webp&fit=cover&position=center)

 _図5：Baselimeの1日あたりのCloudfrontコスト[注：データのギャップは、クラウドアカウントの親組織が変更された際にAWS Cost Explorerでデータ損失が発生したことによります。]_

私たちがCloudflareを利用していた場合、Cloudflare Workersの費用は、1日あたり25ドルほどになると推定されます。これはAWSでの1日あたり790ドルと比較して、95%以上のコスト削減となります。このような削減は主に、Workersの価格設定モデルによってもたらされます。WorkersはCPU時間に対して課金し、レセプターは主にデータを移動するだけで、コスト増大の主な原因はI/Oバウンドであったためです。

### ClickHouseクラスタ関連コストの削減

セルフホスト型のClickHouseからWorkers Analytics Engineへの切り替えによるコストへの影響を評価するには、EC2インスタンスだけでなく、ディスクスペース、ネットワーキング、Kinesis Data Streamのコストも考慮する必要があります。

当社は8月下旬にこの切り替えを完了し、KiKinesis Data StreamとすべてのEC2関連コストの両方で95%以上のコスト削減を実現しました。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![image9](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46792FM5HQJ1EWJFRC2C4Y.png&w=715&h=443&f=webp&fit=cover&position=center)

 _図6：Baselimeの1日あたりのKinesis Data Streamコスト[注：データのギャップは、クラウドアカウントの親組織が変更された際にAWS Cost Explorerでデータ損失が発生したことによります。]_

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![image6](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48T1RBAQCB1GPG5BP2NEGC.png&w=715&h=442&f=webp&fit=cover&position=center)

_図7：Baselimeの1日あたりのEC2コスト[注：データのギャップは、クラウドアカウントの親組織が変更された際にAWS Cost Explorerでデータ損失が発生したことによります。]_

私たちがCloudflareを利用していた場合、Workers Analytics Engineの費用は1日あたり300ドルほどになると推定されます。これはAWSでの1日あたり1150ドルと比較して、70%以上のコスト削減となります。

Cloudflareに移行することで、大幅なコスト削減を実現できただけでなく、パフォーマンスも全体的に改善しました。Cloudflareのネットワーク全体でユーザーにより近い場所でリアルタイムのイベント取り込みが行われるようになり、ユーザーへの応答はより迅速になりました。ユーザーがデータをクエリする際の応答も、ClickHouseを大規模に運用するCloudflareの深い専門知識のおかげで、はるかに迅速になっています。

最も重要なのは、スループットやスケールの制限に縛られなくなったことです。当社は2024年9月26日に[ _Workers Logs_](https://developers.cloudflare.com/workers/observability/logs/workers-logs)をリリースしました。現在、当社のシステムは、速度や信頼性を犠牲にすることなく、以前よりもはるかに多くのイベントを処理できるようになりました。

実現されたコスト削減はそれだけで素晴らしいものであり、それらのシステムの総所有コストは含まれません。プラットフォームがより多くのことを管理してくれるようになったため、システムとコードベースを大幅に簡素化できました。アラートが減り、インフラストラクチャの監視に費やす時間が減り、製品改善に集中できるようになりました。

## まとめ

CloudflareへのBaselimeの移行は、当社がプラットフォームを構築してスケーリングする方法を変革しました。Workers、Durable Objects、Workers Analytics Engine、その他のサービスを活用することで、当社は完全にサーバーレスでグローバルに分散したシステムを稼働することができ、さらにはコスト効率と俊敏性を向上させることができました。運用オーバーヘッドが大幅に削減され、イテレーションが迅速になり、ユーザーにより優れた可観測性ツールを提供できるようになりました。

[ _Workers Logs_](https://developers.cloudflare.com/workers/observability/logs/workers-logs/)があれば、今すぐにでもCloudflare Workersの監視に着手できます。今後については、リアルタイムのエラー追跡、アラート通知、高カーディナリティや次元性イベントに対するクエリビルダーなど、Cloudflareダッシュボードで直接提供する予定の機能について胸躍らせています。2025年初頭までにすべてリリースできる予定です。

このページ

オンラインで議論

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2F80-percent-lower-cloud-cost-how-baselime-moved-from-aws-to-cloudflare%2F&t=Baselime%E3%82%92AWS%E3%81%8B%E3%82%89Cloudflare%E3%81%B8%E7%A7%BB%E8%A1%8C%EF%BC%9A%E3%82%88%E3%82%8A%E3%82%B7%E3%83%B3%E3%83%97%E3%83%AB%E3%81%AA%E3%82%A2%E3%83%BC%E3%82%AD%E3%83%86%E3%82%AF%E3%83%81%E3%83%A3%E3%81%A7%E3%82%88%E3%82%8A%E5%84%AA%E3%82%8C%E3%81%9F%E3%83%91%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%B3%E3%82%B9%E3%82%92%E5%AE%9F%E7%8F%BE%E3%81%97%E3%80%81%E3%82%AF%E3%83%A9%E3%82%A6%E3%83%89%E3%82%B3%E3%82%B9%E3%83%88%E3%82%9280%25%E4%BB%A5%E4%B8%8A%E5%89%8A%E6%B8%9B)[](https://x.com/intent/post?text=Baselime%E3%82%92AWS%E3%81%8B%E3%82%89Cloudflare%E3%81%B8%E7%A7%BB%E8%A1%8C%EF%BC%9A%E3%82%88%E3%82%8A%E3%82%B7%E3%83%B3%E3%83%97%E3%83%AB%E3%81%AA%E3%82%A2%E3%83%BC%E3%82%AD%E3%83%86%E3%82%AF%E3%83%81%E3%83%A3%E3%81%A7%E3%82%88%E3%82%8A%E5%84%AA%E3%82%8C%E3%81%9F%E3%83%91%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%B3%E3%82%B9%E3%82%92%E5%AE%9F%E7%8F%BE%E3%81%97%E3%80%81%E3%82%AF%E3%83%A9%E3%82%A6%E3%83%89%E3%82%B3%E3%82%B9%E3%83%88%E3%82%9280%25%E4%BB%A5%E4%B8%8A%E5%89%8A%E6%B8%9B&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2F80-percent-lower-cloud-cost-how-baselime-moved-from-aws-to-cloudflare%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2F80-percent-lower-cloud-cost-how-baselime-moved-from-aws-to-cloudflare%2F)[](https://bsky.app/intent/compose?text=Baselime%E3%82%92AWS%E3%81%8B%E3%82%89Cloudflare%E3%81%B8%E7%A7%BB%E8%A1%8C%EF%BC%9A%E3%82%88%E3%82%8A%E3%82%B7%E3%83%B3%E3%83%97%E3%83%AB%E3%81%AA%E3%82%A2%E3%83%BC%E3%82%AD%E3%83%86%E3%82%AF%E3%83%81%E3%83%A3%E3%81%A7%E3%82%88%E3%82%8A%E5%84%AA%E3%82%8C%E3%81%9F%E3%83%91%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%B3%E3%82%B9%E3%82%92%E5%AE%9F%E7%8F%BE%E3%81%97%E3%80%81%E3%82%AF%E3%83%A9%E3%82%A6%E3%83%89%E3%82%B3%E3%82%B9%E3%83%88%E3%82%9280%25%E4%BB%A5%E4%B8%8A%E5%89%8A%E6%B8%9B+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2F80-percent-lower-cloud-cost-how-baselime-moved-from-aws-to-cloudflare%2F)[](https://mastodonshare.com/?text=Baselime%E3%82%92AWS%E3%81%8B%E3%82%89Cloudflare%E3%81%B8%E7%A7%BB%E8%A1%8C%EF%BC%9A%E3%82%88%E3%82%8A%E3%82%B7%E3%83%B3%E3%83%97%E3%83%AB%E3%81%AA%E3%82%A2%E3%83%BC%E3%82%AD%E3%83%86%E3%82%AF%E3%83%81%E3%83%A3%E3%81%A7%E3%82%88%E3%82%8A%E5%84%AA%E3%82%8C%E3%81%9F%E3%83%91%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%B3%E3%82%B9%E3%82%92%E5%AE%9F%E7%8F%BE%E3%81%97%E3%80%81%E3%82%AF%E3%83%A9%E3%82%A6%E3%83%89%E3%82%B3%E3%82%B9%E3%83%88%E3%82%9280%25%E4%BB%A5%E4%B8%8A%E5%89%8A%E6%B8%9B&url=https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2F80-percent-lower-cloud-cost-how-baselime-moved-from-aws-to-cloudflare%2F)[](https://www.threads.net/intent/post?text=Baselime%E3%82%92AWS%E3%81%8B%E3%82%89Cloudflare%E3%81%B8%E7%A7%BB%E8%A1%8C%EF%BC%9A%E3%82%88%E3%82%8A%E3%82%B7%E3%83%B3%E3%83%97%E3%83%AB%E3%81%AA%E3%82%A2%E3%83%BC%E3%82%AD%E3%83%86%E3%82%AF%E3%83%81%E3%83%A3%E3%81%A7%E3%82%88%E3%82%8A%E5%84%AA%E3%82%8C%E3%81%9F%E3%83%91%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%B3%E3%82%B9%E3%82%92%E5%AE%9F%E7%8F%BE%E3%81%97%E3%80%81%E3%82%AF%E3%83%A9%E3%82%A6%E3%83%89%E3%82%B3%E3%82%B9%E3%83%88%E3%82%9280%25%E4%BB%A5%E4%B8%8A%E5%89%8A%E6%B8%9B+https%3A%2F%2Fblog.cloudflare.com%2Fja-jp%2F80-percent-lower-cloud-cost-how-baselime-moved-from-aws-to-cloudflare%2F)

## 関連するタグ

[Cloudflare Workers](https://blog.cloudflare.com/ja-jp/tag/workers/)[Observability](https://blog.cloudflare.com/ja-jp/tag/observability/)[パフォーマンス](https://blog.cloudflare.com/ja-jp/tag/performance/)[開発者プラットフォーム](https://blog.cloudflare.com/ja-jp/tag/developer-platform/)

SNS をフォロー

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 新しい投稿のお知らせを受け取るように登録する

メールアドレス

また、あなたのメールアドレスを共有したりすることはございません。

登録する

ご購読ありがとうございます！受信箱を確認して登録してください。
