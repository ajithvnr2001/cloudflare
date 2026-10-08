---
url: https://blog.cloudflare.com/zh-cn/rss/
title: Cloudflare \u535a\u5ba2
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:12:41.106121+00:00
---

# Cloudflare 博客

> Source: https://blog.cloudflare.com/zh-cn/rss/

Cloudflare 博客技术深度解析、产品更新，以及来自助力构建更美好互联网的团队的洞察。https://blog.cloudflare.com/zh-cn/ zh-cnhttps://blog.cloudflare.com/favicon.icoCloudflare 博客https://blog.cloudflare.com Thu, 08 Oct 2026 08:12:36 GMT互联网拥有第二类受众https://blog.cloudflare.com/zh-cn/agentic-web/ Thu, 08 Oct 2026 07:40:32 GMT到达 Cloudflare 上各网站的流量，如今已有超过一半来自自动化访问，而 AI 智能体是其中增长最快的部分。我们正在为网站所有者提供工具，帮助他们了解谁在访问、决定谁能进入，以及对访问收费。AIAI SearchAI 机器人智能体生日周在互联网的大部分历史中，只有一类受众负责支付运营成本：人类。我们阅读文章、浏览广告、购买订阅。机器人一直存在，但它们大多是大规模的自动化操作，既不查看广告，也不为任何内容付费，也不以任何有意义的方式阅读内容。

这种状况正在迅速改变。2024 年底，Cloudflare 平均每秒处理 6300 万次HTTP 请求。如今，这一数字几乎翻倍，达到 1.15 亿次，峰值超过 1.5 亿次。过去一年，我们网络上AI 智能体的每日请求量增长了逾 1700%。今年，历史上首次，超过半数的互联网流量不再来自人类。

人类互联网并未萎缩来为此让路。第二类受众随之而来：智能体（agent）——代表人类行动的软件。它们介于人类与传统机器人之间。它们不响应广告，但背后通常有一个需要完成任务的人。对于学会服务智能体并从中捕获价值的企业而言，智能体是增值性的；而对于那些尚未学会的企业，智能体则是消耗性的。

我们的客户所需要的没有改变：被发现、讲好故事、打造优质体验和实现销售。改变的是，您的访客中已有超过一半是软件。我们的使命是帮助您同时服务这两类受众。

## 流量增多，收益减少

三十年来，互联网遵循着同一套逻辑运转：您让搜索引擎抓取您的网站，搜索引擎为您带来访客，而您再将这些访客转化为商业价值。被找到和获得收益是一回事。

AI 打破了这一微妙的平衡。如今，答案引擎读取页面并向用户提供摘要。这消耗了网站的带宽，却并未将人类引导至产生广告收益或付费行为的网站。机器人持续涌入，而为互联网买单的受众却再也无法到达那些网站。零售、计算机软件、IT 与服务、金融服务等被爬取最频繁的类别，在不到一年的时间里，人类流量下降了多达 40%。

结果是，每次请求的收益不断下降，而成本却在上升。每个自动化请求仍然消耗带宽、算力和源站容量，而这些请求中越来越多的比例既没有引流，也没有广告展示，更没有带来订阅。我们最初的反应是封锁所有自动化流量。去年，我们建议在新域名上屏蔽 AI 训练爬虫，让网站所有者至少能对其内容被用于构建模型说“不”。2025 年春，我们观察到的爬虫请求中 22% 用于AI训练（根据爬虫声明的目的）。到 2026 年 6 月，这一比例升至 52%。问题在于，一概而论的“不”并不足够精细，无法应对当前正在形成的互联网经济。

迎合智能体的机会就在眼前。做对了，您将站在新商业模式的前沿；做错了，结果将与历代曾站在搜索引擎算法变化错误一侧的网站相同。

## 部分流量来自客户

一个为研究人员预订餐厅、比较保险报价或购买数据集的智能体，就是一个客户——只不过不是人类客户。

自动化流量中增长最快的部分已不再是爬虫，而是智能体：代表个人获取页面的软件，通常是因为用户向聊天机器人提出了问题。智能体流量遵循人类的规律，呈现出每周的节奏，并在暑假期间有所下降。拒绝智能体，可能意味着拒绝了派遣它的那个人。

智能体的行为方式也与训练爬虫不同。训练爬虫收集您的页面来构建模型；智能体则会在有人询问相关内容时反复返回，因此这类流量随着人们提问的频率增长，而非随发布量增长。

您无法与一类看不见、无法区分、无法设定条款、也无法收费的受众做生意。直到最近，对于互联网上大多数非人类流量，这四件事中没有任何一件是可能的。

### 了解真正在访问的是谁

**「AI 机器人」这个说法已不再有实质意义。** 重要的是机器人做了什么。Cloudflare 的 **AI Crawl Control** 、**Business Insights** 和 **BotBase** 向网站所有者呈现谁在爬取、取走了什么、带来了什么，以及哪些URL最受关注。

机器人的名字只有在可信的情况下才有意义。借助 **Web Bot Auth** ，包括 OpenAI、Google 和 AWS 在内的运营商对其智能体请求进行加密签名，让网站无需通过 IP 地址或用户代理字符串猜测，即可辨别真正的智能体与仿冒者。我们每周看到超过 5000 亿次经过验证的机器人请求。

### 设定您的条款

7 月，我们将单一的「屏蔽 AI 机器人」开关替换为独立的[搜索、智能体和训练控制](https://blog.cloudflare.com/content-independence-day-ai-options/)，适用于包括免费版在内的所有方案。数据表明为何需要这种区分：Cloudflare 上不足 1% 的网站屏蔽搜索爬虫，而 17% 的网站屏蔽训练。网站所有者从来没有试图隐藏。但随着代理流量的兴起以及智能体使用信息的新方式，他们突然对内容的使用方式既没有透明度，也没有选择权。被找到不再意味着能获得收益，他们希望在不被剥削的前提下被发现。

在混合用途爬虫的情况下，这尤为棘手。当一个机器人同时执行搜索和训练任务时，拒绝其中一项就意味着拒绝另一项。9月15日，我们推出了[Disallow AI Training](https://blog.cloudflare.com/accountable-mixed-use-ai-crawlers/)。它让您保持搜索索引，同时利用爬虫专属机制指示运营商不得将您的数据用于训练。Apple、Google 和 Microsoft 均已承诺遵守该要求。[Cloudflare Radar](https://radar.cloudflare.com/ai-insights#ai-bot-transparency) 也公开追踪爬虫行为。

新域名现在会根据网站的盈利方式而非访客软件的类型，获得推荐配置。对于广告支持的网站，您可以轻松禁止训练，并在承载广告的页面上屏蔽智能体——因为广告只有在真人看到时才会产生收益。您可以随时更改这些设置。

### 获取收益

2026 年 8 月，我们将[正在构建的智能体互联网](https://blog.cloudflare.com/the-agentic-internet/)描述为：可读、可发现、可调用、可支付。最后一个词——可支付——决定着开放网络能否实现自我造血。互联网需要一种方式说“ _可以，但需要付费_ ”，而不是非此即彼的“ _可以_ ”或“ _不可以_ ”。

授权许可市场既揭示了巨大的需求，也揭示了差距所在。自2023年以来，已有逾50份出版商与AI之间的协议签订。几乎所有协议都是定制化的双边协议，发生在大型出版商与大型AI公司之间。它们证明内容具有价值。但它们并未覆盖大多数网络，也未触及大多数买家。

并非所有资产都应以同一方式出售。高价值内容和数据集需要一个可信网络，在其中买家可被识别，并报告作品的使用方式。API 和 MCP 工具等服务不以此方式运作：每次请求即为一次使用。

因此，我们正在为两者同时构建。

[Pay Per Use](http://blog.cloudflare.com/pay-per-use) 触达了直接授权许可无法到达的网站。大多数出版商永远不会与每家 AI 公司达成定制化协议，而任何 AI 公司都无法与数百万个网站逐一谈判。Pay Per Use 是这座桥梁。它不对爬取收费，而在内容被实际使用时付款。每位买家都是经过验证的爬虫——这正是其成为可信网络的原因——每位买家自行定义何为使用以及愿意支付的金额。

出版商看到报价后，可选择是否加入，并可在不再适合时随时退出。买家报告每次使用，Cloudflare 核实这些报告，随后向买家收费并向出版商付款。报告与付款同等重要。出版商可以看到哪些内容被使用、何时使用、赚取了多少，以及在买家报告时，哪些问题触发了对其作品的引用。授权许可协议几乎从不提供这些信息。这形成了一个反馈循环：出版商了解到人们真正在问什么，并据此决定报道什么、更新什么，以及向智能体开放哪些内容。

使用的定义不会只有一种。引用来源的搜索引擎、引用段落的研究智能体和完成购买的购物智能体，各自创造了不同类型的价值，且每种类型都需要自己的商业模式。买家可通过同一套基础设施参与多种商业模式，无需出版商进行新的技术集成。以一本面向海洋工程师、拥有数千订阅用户且几乎不可能获得AI授权许可协议的专业刊物为例——它将从每一家使用其内容的参与AI公司处获得付款。

[Monetization Gateway ](https://blog.cloudflare.com/monetization-gateway-beta)捕获了此前从未有途径实现价值转移的场景。账户、API密钥和订阅适用于您已知的客户，而非一个从未使用过某服务、只需一次查询的智能体。我们的封闭测试版允许符合条件的美国Cloudflare 客户，使用他们已熟悉的规则语言，为经过我们的任何内容定价。当规则匹配时，我们使用开放的 x402 协议返回 HTTP 402 Payment Required，智能体直接向卖方付款。

这不仅仅是找回失去的收益。智能体本身就是客户：无论请求是一次完整购买还是更大任务中的一个步骤，它们都会为所使用的数据、API 和工具付费。

Monetization Gateway 按请求、按查询或按 token 计费，支持固定价格或上限价格。一个依靠广告运营的体育数据网站，可以在每次智能体询问「谁在助攻榜领先？」时收取极小额的费用。我们宣布 Monetization Gateway 时，数千名卖家加入了候补名单，最常见的需求是「向智能体收费，而非人类」。我们也是自己的第一个客户——Cloudflare 的 AI Gateway 使用 Monetization Gateway，让智能体为推理付费，这样我们就能在客户之前发现问题所在。

对买家而言，两款产品都优于拦截页面：提供可靠访问，以及一次性触达数百万网站的方式，而不是逐一签订授权许可协议或申请API密钥。每次付费请求都留有收据，表明购买了什么以及已完成付款。

Pay Per Use 和 Monetization Gateway 都是押注，与客户共同构建于共同的基础元素之上：身份、计量、定价、结算和分析。它们协同工作，让出版商能够从一个控制台禁止训练、允许搜索、从 AI 回答中获利，并按文章向智能体收费。定价和可发现性尚未解决，因此两者均以测试版形式推出，由真实客户和真实交易塑造。

### 降低每次请求的成本

付款是应对收益下滑的答案。成本上升是另一个问题，而其中很大一部分纯属浪费。大多数爬虫仍在一遍遍地下载为人类构建的页面，只为提取几段文字。机器人频繁爬取自上次访问以来毫无变化的网站。这在任何答案尚未生成之前，就已为网站消耗了带宽、为爬虫消耗了算力。我们正与客户和爬虫合作开发相关工具。如今，您可以在我们的控制台中查看每个运营商的带宽消耗。

7月，我们宣布了[与 OpenAI 的联合研究项目](https://www.cloudflare.com/press/press-releases/2026/cloudflare-announces-research-pilot-with-openai/)——这是一项开创性的试点，旨在探索Cloudflare全球网络的洞察如何帮助AI搜索引擎更高效、更有效地发现和索引开放网络上的相关内容。我们计划在未来几周内分享初步结果。

我们正在为客户推出工具和一键式体验，帮助其网站针对这种新型流量进行优化。[Markdown for Agents](https://blog.cloudflare.com/markdown-for-agents/) 让智能体无需处理为人眼设计的额外样式即可读取页面，[WebMCP](https://blog.cloudflare.com/webmcp/) 让网站直接公开操作，而不是让智能体猜测该按哪个按钮。

## 为何选择在 Cloudflare 上构建

超过 20% 的互联网流量经由 Cloudflare 网络传输，近 80% 的主要 AI 公司也不例外。我们能看到这个市场的两面。我们构建了可见性、身份、管控和结算的基础设施，让市场决定事物的价值。

旧的合约已经终结，新的合约仍在书写之中。我们可以共同塑造接下来将发生的事情。

在一种版本中，少数公司掌控着智能体如何寻找信息、如何证明身份并完成支付，其他所有人都须经由它们路由。在另一种版本中，这些要素是任何人都可以实现的开放标准，任何规模的网站都能设定自己的条款并获得报酬。我们更倾向于后者。

这就是为什么这些基础设施运行在 x402 和 Web Bot Auth 等开放标准之上，以便任何人都能在此基础上构建。域名所有者可以自主选择身份提供商、支付处理商和智能体合作伙伴。Cloudflare 是其中一个选择，而非整个技术栈。

几十年来，互联网由访问它的人们来买单。如今，代表他们访问的软件也可以支付属于自己的那份费用了。

]]>01M4D6XYBGSE15EYJJWQ73JWRV利用 Merkle Tree Certificates 构建后量子证书颁发机构https://blog.cloudflare.com/zh-cn/pq-ca-with-mtcs/ Thu, 08 Oct 2026 05:11:06 GMT随着后量子签名可能导致 TLS 握手和证书透明度日志急剧膨胀，Merkle Tree Certificates 提供了一条通往紧凑、可审计身份验证的路径。Cloudflare 的新证书颁发机构将支持大规模 MTC 颁发。TLS后量子安全密码学生日周证书透明度当你在浏览器中输入一个地址时，如何确认你访问的是正确的网站？Web 公钥基础设施（Web PKI）是由策略、协议和基础设施运营商构成的复杂分布式生态系统，帮助你相信自己没有被引导至错误或恶意的网站。过去几十年里，这一生态系统经历了深刻变革。其中之一是透明度的引入：如今已强制要求所有证书记录在公开的证书透明度日志中。现在，它又面临新的挑战：量子计算机的到来已迫在眉睫，促使我们加快推进，[在 2029 年前](https://blog.cloudflare.com/post-quantum-roadmap/)完成向后量子（PQ）密码学的升级。

这一过渡并不简单：仅仅将后量子密码学套用到互联网规模的证书上，将导致无法接受的性能下降。这一时刻呼唤 Web PKI 的全新方案——将透明度作为一等属性而非附加功能，设计出能夠高效扩展后量子签名的新系统。

在获得业界广泛支持后，[Merkle Tree Certificates](https://datatracker.ietf.org/doc/draft-ietf-plants-merkle-tree-certs/?cf_target_id=530455EAF4CCDEFFAA66FDA17EA48FEC)（MTC）已成为前进的方向。今年，在与 Chrome 完成成功的实验性[部署](https://blog.cloudflare.com/bootstrap-mtc/)后，Cloudflare 正全力推进 MTC 的落地。

随着今天 Cloudflare 宣布成为[证书颁发机构 (CA)](https://blog.cloudflare.com/cloudflare-certificate-authority/)，我们很高兴地宣布，该 CA 将支持 MTC 颁发，目标是在 2027 年初纳入 Chrome 新推出的[抗量子根证书库](https://googlechrome.github.io/chromerootprogram/index.html?cf_target_id=9E0C966308CF01FB4BE392ACFAE8D6FC)。秉持帮助构建更好互联网的使命，以及 Cloudflare 免费提供最强加密算法的一贯传统，我们将[免费](https://blog.cloudflare.com/post-quantum-crypto-should-be-free/)提供标准 MTC 颁发服务。拥有一个同时支持传统证书和 MTC 颁发的 CA，使我们能够默认采用最安全的可用身份验证方式，为互联网的大部分提供顺畅、高性能的 PQ 升级路径。

## **当前的信任生态系统**

为了理解 MTC 如何改变游戏规则，让我们先了解一下当今网络中信任的运作方式。

在客户端，浏览器——在此语境中称为“TLS 客户端”——维护根证书计划，规定 CA 必须遵守的一套策略才能获得信任。在服务器端，CA 是受信任的把关人：它们运营证书颁发基础设施，验证域名所有权，并证明域名与该域名所有权的公钥之间的绑定关系。

但我们如何核实 CA 是否遵守规则？这就引出了证书透明度（CT）——它使证书颁发过程可以被公开审计。CA 颁发证书时，还必须将该证书提交至至少两个公开日志。Cloudflare 自 2016 年起运营 [Nimbus](https://blog.cloudflare.com/introducing-certificate-transparency-and-nimbus/) CT 日志家族，并正在推出新的[静态 CT 日志](https://blog.cloudflare.com/azul-certificate-transparency-log/)家族 Raio。

CT 生态系统让证书可以被公开查看，但这并不意味着它们被正确颁发或可以安全使用。监控通过将这些日志记录与域名所有者的预期进行比对并报告可疑活动来提供帮助。Cloudflare 于 2019 年推出了[证书透明度监控](https://blog.cloudflare.com/introducing-certificate-transparency-monitoring/)，并于近期实现了[正式上线](https://blog.cloudflare.com/certificate-transparency-monitoring-ga/)。我们还在 Radar（前身为 Merkle Town）的[证书透明度](https://radar.cloudflare.com/certificate-transparency?cf_page=pq-ca-with-mtcs%2F&cf_target_id=2BE65B6D9FE30BAB66680F620DC5CB3F)页面发布关于证书的大规模统计数据。

随着各组织开始将服务器升级以使用 PQ 身份验证，证书透明度监控将在检测潜在后量子降级攻击中发挥更加重要的作用。已将域名升级至后量子身份验证的域名所有者应监控 CT 日志中意外核发的传统证书，以防止客户端落入恶意降级路径。

当前系统的部分问题在于透明度是后期追加的，因而衍生扩展性瓶颈。证书往往在多个日志中以不同形式被多次记录，要求监控方下载并处理每个日志以免遗漏颁发记录。这代价高昂，使得在互联网规模上激励多元化的日志运营商更加困难。据我们估算，PQ 签名将使 CT 日志需要存储的数据量膨胀 40 倍。这一扩展性挑战及其背后的激励机制失衡，正是后量子扩展性问题的核心所在。

## **后量子扩展性问题**

我们已就[后量子密码学扩展的挑战](https://blog.cloudflare.com/bootstrap-mtc/)进行了深入探讨，简而言之：要在互联网规模上支持服务器身份验证，Web PKI 必须在不向每个客户端预先加载每台服务器公钥的情况下，对约十亿台 TLS 服务器进行身份验证。传统上，CA 通过使用证书链作为信任分发机制来解决这个问题。然而随着时间推移，密钥和证书透明度等附加内容增加了更多的公钥和签名——典型的 TLS 握手需要五个签名和两个密钥。PQ 签名约是传统签名的 40 倍大，在规模上对客户端、CA、日志和监控方而言将产生难以承受的额外负担。

[Merkle Tree Certificates](https://datatracker.ietf.org/doc/search?name=draft-ietf-transcert-merkle-tree-certs&rfcs=on&activedrafts=on&olddrafts=on&cf_target_id=5F5E28805999E0FF57071216A5BFB801) (MTC) 由此登场。这是 [IETF PLANTS](https://datatracker.ietf.org/group/plants/about/?cf_target_id=6572C02B176105794F14BB1E548E562D) 工作组的草案规范，描述了一种面向紧凑、高效、后量子证书的架构。MTC 将证书批量放入仅追加的 Merkle 树，CA 只需对树的根签名而无需对大量单独证书签名。浏览器或其他客户端可透过紧凑的包含证明——一系列密码哈希——对签名树头进行验证，而无需逐一验证每张证书。MTC 背后的[核心理念](https://datatracker.ietf.org/meeting/124/materials/slides-124-plants-solution-space-and-dispatched-work-00?cf_target_id=04339F11523E963B5E2FA7E33D00541F)是“不要记录你颁发的内容，而是通过记录来颁发”。将颁发与记录相结合，透明度便成为运营的必要条件而非附加功能。

## **重新设计的 PKI 中证书颁发机构的角色**

我们正将 MTC 颁发能力的建设作为创设 Cloudflare CA 的核心组成部分。这意味着在跟踪新的 PQ 根证书计划要求的同时，还要在构建传统 CA 的设施、运营和合规功能的同时，开发颁发和镜像软件堆栈，任务不可谓不艰巨！

好处在于，我们可以从第一天起就优先考虑这一新后量子 PKI 的需求与架构，以符合 Cloudflare 价值观和全球网络的方式建立我们的体系，并在这段新旅程中尽可能保持透明。

让我们来看看为 MTC 更新后的架构：

与传统的 CA 生态系统相比，你会发现 CA 的职责大体相同：验证对域名的控制权、将其与公钥绑定、颁发证书。主要区别在于，在 MTC 生态系统中，CA 不再直接对证书签名再记录，而是维护一个由 Merkle 树支撑的透明度日志，证明证书确实在树中的包含证明充当信任锚。CA 还将运营 _镜像共同签名者_ ，存储颁发日志的副本，验证其仅追加的一致性，并确保这些日志对更广泛生态系统的透明度和可用性。

### **颁发 MTC**

MTC 有两种形式，两者都可以编码为当今客户端软件能识别的 X.509 证书格式——只是使用了“特殊”的签名算法。在 _独立_ 形式中，证书的签名值包含颁发日志的共同签名树头以及包含证明（一系列哈希值），证明该证书包含在该日志中。如果客户端能够以带外方式取得共同签名树头（例如通过浏览器更新机制），证书可改以 _相对 landmark_ 形式提供，此时签名值仅包含轻量包含证明，完全不含繁重的后量子签名。

为便于理解，让我们看一个独立证书颁发的示例。当网站需要为其域名申请证书时，可通过 Automatic Certificate Management Environment（ACME）协议向 CA 提出请求，该协议处理证书请求、域控验证和颁发流程。Cloudflare 的 ACME 基础设施将是 [Boulder](https://github.com/letsencrypt/boulder?cf_target_id=9121E6BFA84E7D615734CA16BE595A25) 的分支版本，Boulder 是驱动 Let’s Encrypt 的广泛部署且久经验证的 ACME 软件。Let’s Encrypt 正积极在 Boulder 中开发 [MTC 支持](https://letsencrypt.org/2026/06/03/pq-certs?cf_target_id=E47C9A045BB492F240564610929A240E)，我们计划维护自己的分支，纳入这些上游变更以及 Cloudflare 特有的修改，并在可能的情况下向上游贡献代码。

当 MTC CA 收到证书颁发请求时，CA 的 ACME 服务器会核实服务器确实控制该域名。核实通过后，CA 将数据序列化并添加到仅追加日志中。

将 MTC 条目添加到颁发日志后，CA 计算日志的更新状态，然后对该状态签署检查点。该检查点证明 CA 已在该时间点之前颁发了日志 Merkle 树中包含的每一条目。

CA 随后将更新的日志状态和新检查点发送给受信任的共同签名者。共同签名者持久存储 CA 颁发日志的副本，并验证每个新状态是否仅追加、与之前的树保持一致且格式正确。这一额外的共同签名让客户端和监控方确信另一个受信任的方已观察到相同的日志状态，并验证了 CA 没有向生态系统的不同部分呈现不同的颁发视图。它还确保了即使 CA 颁发日志不可用，颁发的证书也可用于监控。

Chrome 的[抗量子根证书计划草案策略](https://googlechrome.github.io/chromerootprogram/cqrp/draft-policy/?cf_target_id=6C2741F0FEC85CD362C4476A587905E7)要求至少两个共同签名：一个来自由独立组织运营的 Chrome 认可镜像共同签名者，一个来自颁发 MTC 的 CA 本身。因此，我们将为其他试点 CA 运营镜像，并要求我们自己颁发的证书至少获得一个独立的共同签名。

Cloudflare 将在 [Azul](https://github.com/cloudflare/azul?cf_target_id=ABE6B9BCDB657DB0F467712557546EC4)（我们的开源 Rust 透明度日志）中实现镜像共同签名者，并为实现最大互操作性，实现 [c2sp 的 tlog 镜像](https://c2sp.org/tlog-mirror@v0.1.0?cf_target_id=D6308458E63256543752212AC9614CD2)协议。

最终，在成功从镜像共同签名者处获得共同签名后，CA 用共同签名、服务器公钥和包含证明构建 MTC，并将其发送给服务器，服务器此后即可将其用于 TLS。

### **高效分发 PQ 签名：landmark 优化**

虽然独立证书可以正常工作，但它们在 TLS 握手过程中仍需传输大量 PQ 签名，限制了效率。MTC 设计带来的真正性能提升来自相对 landmark 证书。

CA 不必在每张证书中发送共同签名，而是可以将覆盖日志中所有活跃证书的子树序列指定为 landmark，并通过带外更新服务将这些子树（及用于验证它们的数据）分发给客户端。在 TLS 握手期间，对服务器的实际身份验证通过浏览器检查服务器的证书数据——包括其域名和公钥——是否出现在 CA 日志的受信任子树中来完成。如果包含证明将该证书与经过共同签名的 landmark 相连接，并且公钥在 TLS 握手期间证明了所有权，客户端便确认自己正在与正确的服务器通信。

通过定期以带外方式将这些签名和树元数据传输给 TLS 客户端，少量的 MTC 批次签名就能高效覆盖特定 CA 颁发的数十亿张证书。虽然 landmark 在规模上更高效，但并不能消除对独立 MTC 的需求——客户端可能是新安装的、处于离线状态，或缺少相关的 landmark 更新。因此，服务器保留独立证书作为回退方案至关重要。

## **MTC 的实战表现：与 Chrome 实验的结果**

今年，我们与 Chrome 进行了一次实验，测试客户端和服务器之间 MTC 的可行性。我们运营了一个“引导 CA”（模拟颁发流程的虚假 CA），为 Cloudflare“免费”套餐中部分 Cloudflare 域名颁发了由传统证书链支持的 MTC，并向 Chrome Beta 146 的 50% 用户提供服务。实验期间，我们成功提供了数十亿张 MTC。

对于 TLS，我们发现常见情况相当高效：使用相对 landmark 证书时，握手只需传输一个公钥、一个签名以及不到 1 kB 的包含证明。在实验中，当无法与客户端协商相对 landmark 证书时，我们回退到传统证书链而非独立证书。在 CT 方面，MTC 也改变了透明度的扩展特性：日志只需保存公钥哈希；没有按条目的签名，树头上的签名涵盖整个日志。这防止了证书爆炸，因为 CA 颁发日志是 CA 所颁发的所有证书的唯一可信来源，日志使用者只需获取每张证书的单一副本。

结果：MTC 确实有效！以中位数计，使用相对 landmark MTC 比传统签名链快 9%（诚然，这一性能优势大部分来自中间证书的省略）。由于我们是用传统签名测试 MTC 的，预计采用后量子签名后改善幅度将更大。对这些结果以及 IETF [PLANTS WG](https://datatracker.ietf.org/wg/plants/documents/?cf_target_id=B922C9B45DF940BA8B824ACFF261569C) 中 MTC 跨行业合作水平感到满意，我们于上个月（2026 年 8 月）开始逐步结束实验。

## **MTC 的未来之路**

我们很高兴，与 Chrome 的实验证明了 MTC 在实践中可以运作，更对能够以真正的 CA 身份颁发证书感到振奋。

然而，还有一些更宏观的问题，只能通过与整个 PKI 生态系统开展这场大规模实验来回答。独立监控方能否在生产规模下[消费并验证](https://transparency.dev/summit2025/talks/verifiable-indexes.html?cf_target_id=14325B9FFDB5B09C9647F58D28A555C1) MTC 颁发日志？是否会出现多个 CA 与共同签名者，使系统获得韧性所需的多样性？浏览器应如何在紧凑 landmark MTC 的性能优势与缺少最新 landmark 的客户端所需的回退路径之间取得平衡？MTC 已成为后量子身份验证的权威设计，但要在生产互联网规模上加以验证，需要多元化的根证书计划、浏览器厂商、CA、镜像、监控方以及更广泛社区的参与。

我们将参与 Web PKI 下一阶段的机会视为荣耀，并认真对待运营 CA 基础设施的责任。CA 在信任生态系统中占据特殊地位——浏览器、域名所有者和普通用户都依赖它们正确验证身份、保护签名密钥、遵守策略并可靠运行。在 Cloudflare 的 CA 被浏览器信任以颁发 MTC 之前，我们需要向 Chrome 的 Quantum Resistant Root Store 提出申请并经过严格的评估流程。我们欢迎这种审查，并期望让自己达到其他任何被信任、承担保障互联网安全职责的 CA 的同等高标准。我们希望有更多 CA 涌现以支持 MTC 的采用，也期待与任何有意部署 MTC 的浏览器展开合作。

]]>01M4CYJ5FD7JGVZQTP07K12GX8为整个互联网构建证书颁发机构https://blog.cloudflare.com/zh-cn/cloudflare-certificate-authority/ Thu, 08 Oct 2026 02:46:37 GMT在推出 Universal SSL 十二年后，Cloudflare 正式申请成为证书颁发机构。通过将成熟的根证书、ACME 优先方法与 Merkle Tree Certificates 相结合，我们正在为开放网络构建一个后量子 CA。TLS后量子安全密码学生日周十二年前，在2014年 Birthday Week 期间，[我们开启了Universal SSL](https://blog.cloudflare.com/introducing-universal-ssl/)，一夜之间将网络上的加密网站数量几乎翻了一番，为 Cloudflare 背后的每一个网站提供免费 TLS——包括那些从未向我们支付过任何费用的网站。加密不再是一项昂贵、耗时的工作，而是成为了默认选项。

在今年的 Birthday Week，我们在这条路上迈出了下一步。十多年来，我们一直是互联网上公开可信证书的最大消费者之一，却从未自行颁发过一张证书。这一局面即将改变。 Cloudflare 宣布有意成为一家公共证书颁发机构（CA）。

今天，我们宣布这项工作的首批具体里程碑：我们已申请加入 Chrome、Apple、Microsoft 和 Mozilla 的根计划，并签署了最终协议，将从 GlobalSign 收购一个成熟且广受信任的根证书，以便在开始颁发的第一天就能提供设备触达范围最广的证书 。我们还宣布计划成为首批提供后量子证书的CA之一，目标是 Chrome 近期发布的[抗量子根计划](https://blog.google/security/cultivating-a-robust-and-efficient-quantum-safe-https/)。

我们目前尚未颁发证书，还需要一段时间才会开始。我们现在所做的，是公开承诺推进这项工作，在各个里程碑达成时及时分享进展，并在与根计划及 WebPKI 社区其他成员合作的同时，向大家如实介绍我们正在构建的内容。

## **通往信任的两条路**

一个全新的根证书需要多年时间才能广泛发挥作用。即使被某个根计划接受，该根证书也必须在全球的操作系统、浏览器和设备中逐步传播，并且永远无法覆盖那些已停止接收更新或从未接收过更新的大量设备。这批老旧客户端的长尾正是全球互联网流量的重要发源地，也是大量本可避免的故障所在之处。我们认为，无论设备的制造商、操作系统或上次更新的时间如何，所有客户端都应享有尽可能高的安全保障。

收购一个在信任存储中对多元化客户群具有高度覆盖的现有根证书，可以从第一天起就解决这个问题。现有的 GlobalSign 根证书自2012年起就获得了浏览器、操作系统和设备的信任，并能触达新根证书永远无法到达的老旧客户端。我们将提交加入根密钥计划的新根证书，是为生态系统的未来方向而打造的，开始对可信根证书的最长可信年限设上限 。成熟的根证书为我们带来对过去设备的覆盖能力；新的根证书则使我们在未来的政策下具备立足资格 。两者兼备，才能确保我们 CA 颁发的证书为客户提供最广泛的兼容性。

## **免费证书的新来源**

免费、自动化的证书模式如今支撑着加密网络的大部分运转，其中很大一部分通过一家出色的运营商处理。Let's Encrypt 每天颁发约一千万张证书，服务超过 5 亿个网站，并在2025年突破了40亿张活跃证书。作为其最大用户之一，我们认为这是过去二十年里互联网发生的最好的事情之一。

这一成功也带来了一定的系统性风险：如果占主导地位的免费证书颁发机构遭遇一段糟糕时期，网络的大部分将没有类似的免费、自动化替代方案来承接压力。在证书包层面，我们多年来一直在为自身客户构建此类冗余能力。每张 Cloudflare Universal SSL 证书都附带一张备用证书，使用独立密钥封装，由不同机构颁发，一旦主证书被吊销或遭到攻击，可立即自动部署。公共CA正是同样的理念，只是规模扩展到了整个互联网。

为了便于采用，我们将优先支持 [ACME](https://www.globalsign.com/en/acme-automated-certificate-management)（Automated Certificate Management Environment，自动化证书管理环境）——这是一个被广泛接受的开放标准协议。通过ACME进行自动化颁发和续期，将是从我们这里获取证书的方式。这意味着任何已指向现有免费CA的用户，只需更改一个目录URL即可切换到我们，无需新的工具，也无需重新设计架构。

## **证书增长预测非常庞大**

Cloudflare 处于全球超过20%的互联网请求流量之前，为数百万个域终止TLS，每年依赖数百万张证书来实现这一点。我们通过多个CA来调配这些证书，并设有主备路径，以确保在CA中断和吊销事件期间客户服务不受影响。

这不仅让我们了解了 WebPKI 生态系统的运作方式，也让我们从消费者的视角以惨痛的方式体验到了它偶尔的失效。我们处理过速率限制、验证边界情况、吊销延迟、证书链构建以及根分发滞后等问题。我们经历了近年CA格局的变动，并通过客户切身感受到了它的影响。我们深知可靠颁发从外部看应该是什么样的，因为我们客户的正常运行时间依赖于我们在颁发机构遭遇困难时保持韧性并快速响应。

随着未来几年[证书最大有效期缩短](https://cabforum.org/2025/04/11/ballot-sc081v3-introduce-schedule-of-reducing-validity-and-data-reuse-periods/#ballot-contents)、智能体活动增加以及后量子证书走向主流，我们预计每年所依赖的证书绝对数量将继续快速增长——而我们并不是孤例。我们希望不仅为自身解决这一问题，还能成为向互联网提供这一基础能力的一部分，并确保我们客户的证书供应链拥有更多供应商。

## **为韧性而设计：透明度与“fail small”**

承担起成为自身CA的这项新责任，我们致力于打造尽可能可靠、有韧性的CA。我们打算构建一个证书颁发机构，其可靠性不仅取决于避免错误，还要像 Cloudflare 的其他产品一样践行“fail small”原则，将任何单一问题的影响降至最低。

这意味着要在任何事故发生之前制定流程来设计和测试恢复能力。举例而言，我们将把续期自动化作为颁发的前提条件。我们仅向支持在RFC 9773中标准化的[ACME Renewal Information](https://www.rfc-editor.org/info/rfc9773/)（ARI）的客户端颁发证书。订阅者必须维护能够轮询我们续期端点、响应我们发布的续期窗口并识别待替换证书的自动化机制。

我们也在从过去16年的观察中汲取经验。我们见过一些证书颁发机构陷入两难困境——既要及时吊销，又要维持订阅者网站的正常运行，原因是太多订阅者来不及快速替换证书。当证书需要退役时——无论是因为合规问题还是安全事件——我们可以提前为受影响的证书设置续期窗口，将替换操作分散到可用时间内，并跟踪替换证书的颁发情况。

这只是我们构建方式的诸多体现之一。我们将对颁发堆栈和运营保持透明，发布对证书进行签名的软件的可复现构建版本，证明持有我们密钥的硬件安全模块，并运营一个关于颁发健康状况和事故的公开仪表板。审计具有时间点性质，只能告诉你某家CA通过了审计，而无法反映它在普通星期二的实际运营情况。我们希望根计划、研究人员以及普通网站所有者都能观察到现代CA在两次审计之间的真实运营方式。

## **面向后量子互联网的证书颁发机构**

我们还打算引领证书的发展方向，而不仅仅停留在现状。我们计划成为首批在生产环境中颁发 Merkle Tree Certificates（MTC）的 CA 之一，首批证书将于2027年第一季度颁发。

MTC是一种全新且更为紧凑的公开可信证书交付方式，专为后量子世界设计——在那个世界中，传统证书链会增长到足以给TLS握手带来压力的程度。我们一直在IETF积极推动MTC的[基于标准的提案](https://datatracker.ietf.org/doc/draft-ietf-plants-merkle-tree-certs/)，今年早些时候，[Chrome将MTC列为后量子身份验证的首选路径](https://blog.google/security/cultivating-a-robust-and-efficient-quantum-safe-https/)。在生产环境中颁发MTC，使我们得以保护 Cloudflare 客户以及更广泛的互联网免受后量子威胁，并以真实的规模推动整个网络都必须完成的这场过渡。我们已在[一篇关于该主题的博客文章](http://blog.cloudflare.com/pq-ca-with-mtcs)中分享了更多关于 MTC 以及这一新型 Web 公钥基础设施（PKI）将呈现怎样面貌的内容。

我们预计这场过渡不会是突然发生的。互联网的很大一部分在未来多年内仍将依赖经典证书和现有的WebPKI。但在这段时间内，我们预计MTC将占据颁发量中稳步增长的份额，这也是我们构建一项兼顾两者的服务的原因。通过将经典证书和Merkle Tree Certificates统一在一个CA之下，以单一的生命周期和一套保障，客户可以按照自己的节奏采用，并帮助网络在不进行硬切换的情况下完成过渡。客户不应该被迫在一场历时数十年的迁移中站队，也不必同时运营两套系统，更不必在格局转变时重新构建。

## **一如既往，Cloudflare将成为Customer Zero**

除了通过 Universal SSL 为客户提供证书包，Cloudflare 还从众多不同的CA获取证书来运行我们的系统和内部业务。与我们其他产品一样，我们将成为新CA及其证书（包括WebPKI和MTC）的 [Customer Zero](https://www.cloudflare.com/the-net/top-of-mind-security/customer-zero/)，确保新系统和流程的各个方面均达到我们的高内部标准，并确保我们CA的基础设施在Cloudflare规模下得到充分验证。

## **接下来会发生什么**

我们正在与各主要Web根密钥计划推进申请和审批流程。这些流程公开进行，我们将随着进展持续分享更多更新，直至2027年初的首批 Merkle Tree Certificates。如果您希望关注这项工作，或希望成为未来最先使用Cloudflare CA证书的用户之一，可以[注册获取最新资讯](http://cloudflare.com/resource/certificate-authority)。如果您希望参与在 Cloudflare 内部构建这项新能力，我们正在[招聘](https://boards.greenhouse.io/cloudflare/jobs/8237801?gh_jid=8237801)！

在我们拓展这项新能力的同时，我们将继续与多年来——确切地说是16年——所依赖的合作公共CA网络紧密协作，共同致力于维护一个可信、开放的互联网。

当年推出 Universal SSL 时，我们的理由很简单：互联网上每一个加密传输的字节，都让拦截、限速和审查变得更加困难；开放的网络是我们共同构建的。一个公开、冗余、透明的证书颁发机构，正是这个理由向下推进了一层——直抵让加密网络成为可能的信任本身。为此我们已努力了很长时间，很高兴终于踏上了这段旅程。

Happy Birthday Week!

]]>01M4CPB9QTQ5TSAD39QQM1C1NY隆重推出 Forge：用于生成 SDK、CLI、文档等的开源生成流水线https://blog.cloudflare.com/zh-cn/forge-open-source-generation-pipeline/ Thu, 01 Oct 2026 13:01:39 GMTForge 是一款开源的可插拔生成流水线，在 CI 中运行，可直接从 API 定义生成 SDK、CLI 和文档。通过将生成流程上移至各团队独立的代码仓库，Forge 使开发人员工具持续保持同步。APICLISDK开发人员智能体生日周今天，我们推出 [Forge](https://github.com/cloudflare/forge)——一种生成 SDK、CLI、文档和库的全新方式。Forge 是一款开源的可插拔生成流水线，任何人都可以免费部署和运行。

Forge 尚处于早期阶段，但已经能够生成 [cf CLI](https://blog.cloudflare.com/cloudflare-cf-cli-launch/) 所需的输出，并将在未来几个月内为 Cloudflare 的 API 文档、SDK 以及更多内容提供支持。

我们构建 Forge 是因为我们自己需要它，以便将 AI 智能体视为我们的客户。现在，我们将其开源，因为我们认为每个人都应该能够生成 AI 智能体所需的所有接口。过去，只有面向开发者的产品才需要 CLI、API SDK 和 MCP 服务器，以及与之配套的出色文档。如今，这些已成为每个产品的基本门槛。

## **我们的 API 超出了生成器的处理能力**

Cloudflare 的 API 拥有超过 3,500 个操作，驱动这些 API 的数百个服务以多种语言编写，包括 Rust、Go、TypeScript 和 Python。当我们着手为整个 Cloudflare API（包括 SDK 和 API 文档）构建一个 CLI 时，我们需要一个能够应对这种规模的代码生成流水线。该流水线需要足够灵活，能够跨语言工作，并适应我们各个工程团队的运作方式。

我们需要一种方法来减少团队之间的协调开销。当 Cloudflare 产品团队进行 API 变更时，他们需要在合并变更并发布给客户之前，能够使用即将生成的 Cloudflare 全局 CLI、SDK 和文档站点的预览版本。我们需要一种方式确保他们不会无意中破坏生成流水线。我们还需要一个可以扩展的系统，用于生成不仅仅是 SDK 的内容——从 Cap'n Web 到 MCP，乃至更多。

我们试用过几款试图解决此问题的托管产品，并在生产中依赖了其中一些。但没有一款真正为我们解决了这个问题，部分甚至已经完全关闭。一个团队合并了一个无意中破坏生成流水线的变更，另一个团队在发布时才发现问题，我们浪费了太多时间在无法掌控的托管工具中逆流而上，协调团队与供应商之间的变更。

这就是我们开始构建 Forge 的起因。

Forge 旨在解决所有这些问题：它在 CI 中运行，在每个团队的 API 仓库上运行，就像我们的 AI 代码审查员和测试流水线一样。它对每次变更进行 lint 检查，然后生成 CLI、文档和 SDK 的预览版本，仅突出显示您的变更，您可以安装并测试。这与 [Workers Previews](https://blog.cloudflare.com/worker-previews/) 的理念相同：为每次变更提供完整的预览版本构建，但应用于大规模的 SDK 生成——即使 API 接口分布在数百个服务和仓库中也不例外。这就是 Forge 致力于实现的目标。

## **Forge 转换器可以生成任何内容，包括 Cap'n Web**

Cloudflare 比大多数公司更有理由需要一个能够远超常规语言目标的生成器。[Cap'n Web](https://capnweb.com/) 是 Cloudflare 的 RPC 系统，它让 TypeScript 可以像调用本地方法一样调用远端 API。

借助 Forge，可以获取一份 OpenAPI 规范并直接生成 Cap'n Web。这为从 Workers 到其他 API 的[绑定](https://developers.cloudflare.com/workers/runtime-apis/bindings/)生成打开了大门。毕竟，Workers 运行时中的绑定是作为暴露 RPC 方法的 Workers 来实现的。

这并非 Cap'n Web 独有的需求：您可能已经依赖的其他热门工具也有同样的需求。如果您使用 [TanStack Query](https://tanstack.com/query/)，理想情况下，您会希望能够直接从 API 本身生成适合您应用的 TanStack Query 绑定。始终保持最新，始终根据您的真实 API 进行验证。生成 Zod 或 Valibot 模式、MCP 服务器，或任何其他让 API 更易消费的内容，道理也是一样。

这之所以可行，是因为 Forge 代码生成器足够灵活。它们天生就是为了将信息从一个输出流向另一个输出而构建的。

## **Forge 转换器可以链式调用：从其他输出生成输出**

我们将 Forge 设计成可插拔的，并支持多种输入和输出类型。Forge 提供 CLI、SDK 和文档生成器，但没有什么能阻止您添加一个生成特定库包甚至完整仪表板或应用程序的转换器。Forge 目前支持 OpenAPI 作为输入类型，但我们的设计允许未来支持 [AsyncAPI](http://asyncapi.com)、GraphQL、Cap'n Proto、Protobuf 或其他输入格式。

这不仅仅是兼容性问题：它让您可以链接目标，使用一个目标的输出来生成其他目标。这在其他生成器中很常见，例如 CLI 和 Terraform 目标从 Go SDK 生成。但缺少的——也是 Forge 所提供的——是一种让用户自己控制这个链式系统的方式。

我们自己也需要这个解决方案，因为我们的 cf CLI 是用 TypeScript 编写的，而其他 SDK 生成器通常不会将 TypeScript 作为 CLI 的链式来源。但我们自身的处境让我们认识到了更深层的问题：为什么 SDK 生成器工具要替您做这个决定？也许您是一个 Python 团队，希望 CLI 也用 Python 编写。

如果您在想“这有什么关系，Python 还是不是 Python？代码是自动生成的”——原因在于 CLI 是不同的。CLI 往往会引入一些只在本地有意义的行为，这些行为在 SDK 中并不合适。这些行为需要手动编写，因为它们本质上不是由任何 API 调用支撑的。例如，cf CLI 有 cf dev 和 cf build 这样的命令，它们是在其余生成输出之上额外添加的。这些命令需要调用其他包（如 Vite）中的 TypeScript API。

现在，我们再把文档加入其中。如果您纯粹从 OpenAPI 规范生成 CLI 和文档，您如何将那些手写命令重新融入文档，使它们能与其余内容一起得到记录？

我们找不到目前能做到这一点的现有工具，然而这正是我们为 cf 所需要的。所以我们将它内置到 Forge 中。

## **在不影响用户的情况下更改您的 API**

Forge 也在为我们更好的 API 版本管理奠定基础。Cloudflare 的 v4 API 10 年来一直是我们 API 的唯一主要版本。在此期间，表面上我们似乎没有发布任何新的主要版本，但按照 SemVer 的定义，我们其实进行了不少值得新主要版本的变更。与此同时，API 中的多个操作带有内部的“v2”标签或“beta”标识，而这些标签早已超出了产品生命周期的那个阶段。

经历了这么多年的 v4 API，我们深知一个全新的大版本 v5 会让很多客户无法跟进。这就是为什么在 Forge 持续发布产物的同时，我们正在研究一种 API 版本管理方案，使我们能够发布新的主要 API 版本，而不破坏旧的客户端或 SDK。

关于我们的 SDK（包括 TypeScript、Rust、Python、Go、PHP 和 Terraform），我们很快会有更多消息分享。尤其是 Terraform。我们知道升级任何 Terraform 提供商都有其独特的严格性要求，我们将为 Terraform 的过渡倾注格外细致的心力。

## **关键工具应向所有人开放**

我们相信，为 API 构建工具是互联网的核心组成部分，您应该能够在无需 SaaS 产品的情况下做到这一点。您应该拥有自己的 SDK、CLI 和文档。如果您自己生成这些，那么您应该能够随心所欲地使用它们，在任何地方，免费。

这就是为什么我们在宽松的 Apache 2.0 许可证下将 [Forge 以开源方式发布](https://github.com/cloudflare/forge)。我们希望大家能加入我们的这段旅程，共同贡献。

或者不参与也可以？也许您想把一切都据为己有。没问题！您可以出于任何目的、进行自定义修改、免费、私下运行 Forge。

 _致谢：本项目也得益于 Dan Carter、Steven Chong、Krishna Paritala 和 Shelley Jones 的设计与实现工作。_

]]>01M3VQFGCS6DRT4JH47W2B2MV0隆重推出 The Cold Start：在 Cloudflare Connect 现场为你的初创公司路演https://blog.cloudflare.com/zh-cn/introducing-the-cold-start/ Thu, 01 Oct 2026 12:36:09 GMTCloudflare 正式推出 The Cold Start——一项创业竞赛，为五家早期阶段初创公司提供在 Cloudflare Connect 舞台上各五分钟的展示机会。大奖得主将获得价值 $500,000 的信用额度、San Francisco 的一块广告牌，以及我们 VIP 演讲者晚宴的邀请函。Cloudflare for Startups开发人员生日周十六年前，Cloudflare 还是一千多家初创公司中的一员，怀抱着在 TechCrunch Disrupt 舞台上亮相的梦想。

从表面上看，我们并不是显而易见的选择。Cloudflare 做的是基础设施：让网站跑得更快，并保护它们免受攻击——而这在当时并不被大众市场所理解。基础设施往往是隐形的，直到它变得至关重要的那一刻。

然而，在 2010年9月27日，Matthew Prince 和 Michelle Zatlyn 走上 Startup Battlefield 的舞台，向公众正式发布了 Cloudflare。演讲进行中，人们开始陆续注册。随后更多人涌入。当评委的提问结束时，已有数百个网站加入了 Cloudflare，我们最初的五个数据中心正经受着实时的考验。此后七天，流经我们网络的流量增长了近 10 倍，Cloudflare 从全球第 1000 大网站跃升至前 50 名。

那一天，Cloudflare 没有赢得主奖杯。在颁奖典礼上，TechCrunch 创始人 Mike Arrington 把我们的工作形容为类似“给互联网修消音器”——说实话，他说的不无道理。但随后，他将我们评为最具创新力的公司。正如 Matthew 后来所写：「你或许拿不到那座奖杯，但你将收获另一样远比它重要的东西。」

在一家公司的生命历程中，某些时刻，有人给你一个房间、一支麦克风和少许时间，让你讲述那件你已魂牵梦萦了数月乃至数年的事情。大多数时候，什么魔法都不会发生。但有时，恰当的人在恰当的时机听到了它，一个原本只存在于少数人脑海中的想法，便开始在世界上流动起来。

今年十月，Cloudflare 迎来 16 周年。我们希望给五家早期阶段的初创公司一个属于自己的舞台。

## **隆重介绍 The Cold Start**

[The Cold Start](https://www.cloudflare.com/connect/cold-start/) 是一场真实的路演竞赛，将于下月在 San Francisco 的 Cloudflare Connect 举行。我们将从中遴选五家早期阶段企业，为每家提供五分钟的舞台，讲清楚他们在做什么、为什么它需要存在，以及为什么他们是应该去做这件事的人。

比起完美的路演演示文稿，我们更希望看到条理清晰、表达有力的有趣想法。你不需要三十张幻灯片、一个精确得可疑的 TAM 测算，也不需要一个精心排练的故事——讲述你的童年如何为颠覆应收账款产业做好了铺垫 。我们想要理解的是愿景：世界发生了什么改变使它成为可能，你看到了别人错过的什么，以及为什么你无法停止思考它。

五位决赛入围者将在 Cloudflare Connect 的观众面前，以及三位在公司、基础设施与互联网 领域深耕多年的人面前，阐述各自的主张：

  * Matthew Prince，Cloudflare 联合创始人兼 CEO
  * Michelle Zatlyn，Cloudflare 联合创始人兼总裁
  * Dane Knecht，Cloudflare 首席技术官



评审将选出一家初创公司，奖励 $500,000 的 Cloudflare 积分、在 San Francisco 接管一块广告牌，并获得当晚 VIP 演讲者晚宴的邀请函。

五家公司，各五分钟，台下坐满全神贯注的聆听者。

### **我们在寻找什么？**

The Cold Start 面向美国和加拿大的早期阶段雄心勃勃的初创公司，融资额须低于 1000 万美元。除此之外，我们有意将范围定义得足够宽泛——最有趣的公司，很少会以整齐划一的分类形式出现。

我们希望看到那种一旦有人终于把它做出来就显得理所当然的想法，以及那些乍听之下略显异想天开的想法。我们希望看到看似无聊、却总有一天人人都离不开的基础设施；几年前根本无法存在的产品；奇妙的新型交互界面；全新的软件构建方式；既有针对庞大现有市场的，也有面向尚无人命名的市场的。

最重要的是，我们想遇见那些发现了世界上某件事并决心有所行动的人。

在申请过程中，我们会请你介绍自己，提供一句话路演，解释你在构建什么以及为什么，说明你的融资和收入阶段，展示 Cloudflare 如何融入你的技术栈，并指向任何能帮助我们了解你和你工作的信息。

目标很简单：让我们明白你所构建的东西为何应该存在。

[申请](https://www.cloudflare.com/connect/cold-start/)**[The Cold Start](https://www.cloudflare.com/connect/cold-start/)。**

** _申请现已开放，截止日期为 2026年10月2日（周五）。_**

## **San Francisco 的五分钟**

The Cold Start 将作为 [Cloudflare Connect](https://www.cloudflare.com/connect/) 的一部分，于 2026年10月19日（周一）太平洋夏令时下午 4 时至 5 时，在 San Francisco 的 Moscone West 举行。Cloudflare 将为五位决赛选手报销飞往 San Francisco 参赛的机票费用。

Connect 将致力于构建互联网未来并思考其发展方向的人们聚集在一起。今年的演讲嘉宾包括 AI 先驱李飞飞博士；Idealab 创始人比尔·格罗斯；组织心理学家和作家亚当·格兰特；AMD 首席技术官马克·佩珀马斯特；Vue.js 和 Vite 的创作者尤雨溪；Lovable 联合创始人兼首席技术官法比安·赫丁；以及 OpenAI 技术人员、OpenClaw 的创建者彼得·斯坦伯格。

我们为五家年轻公司保留了部分舞台时间。每家初创公司将有 5 分钟进行路演，随后由评委提问 3 至 5 分钟。

我们很喜欢这种对称的意味。十六年前，Cloudflare 需要有人愿意为一家有着难以讲述的故事的基础设施企业冒险，给我们几分钟站在合适的观众面前。今天，我们有幸拥有了自己的舞台，而我们希望把同样的机会传递给那些刚刚起步的公司。

## **从小处出发，成就非凡。**

Cloudflare 花如此多的时间与初创公司合作，有其务实的理由：非常小的团队往往有着挑战非常宏大事业的惊人能力。

问题在于，雄心勃勃的软件越来越依赖于一种基础设施，而就在不久前，只有全球最大的科技公司才负担得起自建这些基础设施。全球计算能力、存储、网络、安全、实时系统、AI 推理，以及在你做的东西突然爆火时也能扛住的能力——这些都不应该要求一家公司先变得庞大才能拥有。

我们认为，你应该从第一天起就能获取这些能力。

这正是 [Cloudflare for Startups](https://www.cloudflare.com/startups/) 背后的初衷之一——符合条件的早期阶段公司可获得最长一年、价值最高 $350,000 的 Cloudflare 积分。这也是我们持续扩展 Cloudflare 开发人员平台的原因之一：一个小团队应该能在周二构建出某个东西，如果互联网在周三决定喜欢它，那么周四就应该专注于产品本身，而不是仓促地成为全球基础设施专家。

Cloudflare 从一个略显大胆的前提起步：让互联网最大企业所拥有的性能、安全与全球计算能力，从第一天起就能为所有人所用。2010年，我们在一个舞台上获得了解释这件事为何重要的机会。

十六年后，我们拥有了规模大得多的网络、略大一些的团队，以及性能卓越得多的断路器。

现在，我们想听听你在构建什么。

[申请**The Cold Start**](https://www.cloudflare.com/connect/cold-start/)**。**

]]>01M3VQ1DTDAZNQ7GXHHMGNTSEJcf 正式发布：面向整个 Cloudflare API 的智能体驱动的 CLIhttps://blog.cloudflare.com/zh-cn/cloudflare-cf-cli-launch/ Thu, 01 Oct 2026 12:28:40 GMT我们正式发布 cf——我们的新命令行工具，完整映射 Cloudflare API，并支持以 TypeScript 进行程序化配置。同时，我们也将内部 SDK 生成器 Forge 开源发布。APIcf开发人员智能体生日周在过去一年里，AI 智能体对 Wrangler 的使用量急剧攀升。

2026 年 3 月，AI 智能体贡献了 Wrangler 使用量的四分之一，而前一年的占比还是个位数百分比。上周，智能体的使用率已达到 48%。

AI 智能体是更高产的用户，每天使用的不同命令数量几乎翻倍，使用六个或更多命令的可能性几乎是四倍。

AI 智能体喜爱 CLI。但 Wrangler 仅提供约 280 种操作的命令，而 Cloudflare 提供的操作多达数千种。

今年早些时候，我们曾预告过[我们的解决方案](https://blog.cloudflare.com/cf-cli-local-explorer)。今天，我们正式推出全新 CLI：cf，让 AI 智能体能够使用每一个 Cloudflare 产品。

cf 是专为下一代软件开发打造的 CLI：

  * AI 智能体可以通过专属搜索和引导找到所需的命令，完成任何想做的事情。
  * JSON 是默认接口，对人类友好地美化输出，对 AI 智能体则进行压缩，以实现最大限度的上下文节省。
  * cloudflare.config.ts 是 Cloudflare 全平台的全新配置格式，从 Workers 开始，将 TypeScript 的安全性和准确性带给您以及您的智能体的语言服务器协议（LSP）。
  * Vite 成为默认工具，带来业界最佳的本地开发服务器，以及面向开发者和框架作者的插件套件。



立即全球安装公开测试版，随时随地运行：

**Copy prompt**
    
    
    Please update your global agent instructions, so you use Cloudflare's new `cf` CLI.
    
    Add the Markdown below to the user-level instructions file that you load in every project – not this repository's AGENTS.md or CLAUDE.md. Use the file for the agent you are: Claude Code `~/.claude/CLAUDE.md`, Codex `~/.codex/AGENTS.md`, OpenCode `~/.config/opencode/AGENTS.md`, Pi `~/.pi/agent/AGENTS.md`. For any other agent, use its equivalent global rules file; if your global rules can only be set in a settings screen, tell me what to paste there instead. Create the file if it doesn't exist. Keep everything already in it, but replace any existing instruction about Wrangler or the Cloudflare CLI instead of adding a conflicting one. If the same guidance is already there, leave the file as it is. When you're done, tell me the path of the file you changed.
    
    ```markdown
    ## Cloudflare CLI - cf - v20260928
    
    `cf` is Cloudflare's current CLI and covers the whole Cloudflare platform. Prefer it over Wrangler: create projects with `cf init`, develop with `cf dev`, deploy with `cf deploy`, and manage account resources with `cf <product> …` (for example `cf d1 list`).
    
    Wrangler is only for projects that already use it – a `wrangler.jsonc`, `wrangler.json` or `wrangler.toml` file – or when the user asks for it. Keep using Wrangler in those projects unless asked to migrate, and use `cf migrate` in this case.
    
    `cf` commands differ from Wrangler's; check `cf --help` or `cf cli search <what you want to do>` instead of guessing. If a `cf` command fails in a project that doesn't use Wrangler, don't fall back to Wrangler (including `npx wrangler`) without offering to report it.

## **cf 让您的智能体访问整个 Cloudflare API**

如果您的 AI 智能体能做到 Cloudflare 能做的一切，会怎样？这正是我们今年初产生兴趣的问题：智能体变得越来越强大，但它们通过 Cloudflare CLI 所能完成的事情仍然有限。

Wrangler 是手工构建的，每个产品团队都以自己的方式为命令开发者体验做出贡献。即便只有约 280 条命令路径，在团队之间推行统一模式几乎不可能。`d1 info`、`hyperdrive get`、`workflows describe` 之间的术语不一致，因为每个团队在不同时期制定了各自的实践方式。部分团队花费数千行代码构建了完全自定义的体验，但这些体验极少被使用，而且各团队对同一问题采用了不同的解决方案。

我们希望在标准化现有内容的同时，一次性完成大规模扩展。[Forge](https://blog.cloudflare.com/forge-open-source-generation-pipeline)——Cloudflare 全新的统一 API 生成流水线——让我们得以实现这一目标。其核心理念是直接从支持 API 文档和 SDK 生成的 API 模式中生成 CLI 命令。我们提供的所有内容都有 OpenAPI 模式，只需添加一点额外信息进行注解，即可将其作为 Forge 生成 CLI 的来源。

这使我们能够将 `cf` 从 Wrangler 多年积累的约 280 个功能，扩展到涵盖 Cloudflare API 全部超过 3,000 个操作。

现在，只需将 `cf` 交给您的 AI 智能体，让它设置 worker、部署、监控、使用 Cloudflare Access 进行保护、购买域名，并通过 Cloudflare WAF 进行防护——全部通过单一工具完成。

## **为从未使用过 cf 的智能体而构建**

cf 是为软件工程的发展轨迹而构建的，智能体驱动的开发正在从根本上改变软件的构建和部署方式。今年，我们专注于提供支持这一转变的工具，cf 是这一努力的集大成之作。cf 从零开始以智能体为核心进行构建，包含用于智能体驱动命令发现的创新工具，我们认为这些工具将在不久的将来成为更多 CLI 的标准。

Wrangler 有一个优势：多年的文档、博客和第三方指南已被纳入 LLM 的训练过程。但这也带来了同样的劣势：改变 Wrangler 的工作方式现在与已学习的行为相悖，而鉴于我们希望实现的改进规模，重大变更是不可避免的。

引入一个 AI 智能体从未见过的新 CLI 听起来像是一次巨大的颠覆性变化——但实际上这是我们能做的最干净的事情。由于我们所做的设计决策、我们可以进行的上下文注入以及我们可以追加的 AGENTS.md 文件，以这种方式进行切换实际上比让智能体理解它所熟悉的工具的两个版本之间的主要差异更少令人困惑。我们在发布时内置了几项此类面向智能体的功能，更多功能即将推出。

## **智能体需要过滤 JSON，而不是查看表格**

当 AI 智能体使用 Wrangler 时，它们会在每个命令后附加 `--json`，然后经常用 `jq` 过滤输出以提取字段子集。但 Wrangler 中只有部分命令支持 `--json`；许多命令返回的是专为人类在终端查看而设计的 Unicode 表格。智能体能够解读这些表格，但代价是比 `jq` 过滤器更多的时间和 token。

在 cf 中，我们采取了相反的立场：智能体只需要 JSON，如果智能体是这个工具未来的主要用户，那么 JSON 就应该是默认值。对于极少由人类访问的绝大多数命令来说，这显然是正确的选择。

作为这个 CLI 的人类用户，您实际上与直接使用它隔了一层。让 AI 智能体能够轻松过滤其结果，然后以您要求的任何格式返回该过滤后的列表，比提供您可能永远不会直接阅读的表格更为可取。

但如果您想做一些可能需要真实个人输入的事情，比如搜索要购买的域名，该怎么办？

对于您的 AI 智能体可以通过在长而繁琐的序列中链接命名参数来访问的命令，您只需填写表单即可。cf 将 API 的要求分解为一系列经过验证的输入，因此购买域名——即使是有复杂要求的域名——也简单易懂。

或者，如果您坚持，直接让您的智能体来做。

## **您的智能体可以自行找到正确的命令**

在一个有 3,000 条可能路径的 CLI 中，您的 AI 智能体如何才能快速找到所需操作而不会让您的上下文爆炸？为此，我们还添加了 `cf cli search`。

这个命令允许您的 AI 智能体用自然语言询问需要做什么，一个小型搜索索引将根据 API 描述和参数提供合适命令的列表。当智能体第一次运行 `--help` 时，我们会自动告知它这个命令。

## **对智能体进行类型检查的配置**

我们的新配置格式基于 TypeScript，人类和 AI 智能体都易于解析，并允许您以编程方式编写配置。

类型化配置对 AI 智能体极为有用。我们发现，即使没有对编程配置格式的任何先验背景，智能体也能够轻松识别并按需编辑配置，即便是像 `env` 这样相比 Wrangler 中同名特性已发生重大变化的元素也不例外。所有使用 LSP 插件的智能体，例如 Claude Code 和 Codex，都能从在上下文中解读更多配置文件格式信息中获益，并因此给出更精准的建议。

相比之下，TOML 没有可访问的模式，JSONC 虽然有关联模式，但 AI 智能体很少使用。

Cloudflare 内部的一些 Wrangler 配置文件已从超过 5,000 行（每位开发者有许多自定义环境）压缩了 40%，成为能更高效地构建每位开发者配置的工厂文件。

这是通过从同一通用基础以编程方式定义每个环境来实现的，而不是像 Wrangler 中常见的那样复制 `env` 块。具有多个环境的简单 Worker 只需切换 Vite 原生`模式`参数即可在不同配置集之间切换。

现在，实现此功能的一个简单配置如下所示：

您可以通过 `cf migrate` 将您的 Cloudflare Worker 迁移到此新格式。

我们还提供了一些辅助函数，使构建您的 Worker 变得轻而易举。

通过 `bindings`，您的智能体可以便捷地发现开发人员平台提供的各项能力。包括环境变量、存储、数据库和队列在内的一切都可以由您的编辑器自动完成并进行解释。

同样，我们包含了一个`触发器`提供了一个辅助函数，这是一种为 Worker 定义路由、队列、计划和邮件触发器的新方式。所有可能触发 Worker 运行的操作现在集中在单一配置块中，而不是以往那样零散地分布在配置文件各处。

`defineConfig.worker` 只是一个开始。我们创建 cloudflare.config.ts 的初衷，是让它成为您统一管理整个 Cloudflare 的方式。您所需的每一款产品——连同通过 cf 向其开放的 API——都将能够以类型安全的配置方式来表达。很快您将能够通过此配置文件配置整个策略、设置区域、配置 DNS 等。

## **同类最佳的开发体验**

当 Wrangler 开始构建 JavaScript Workers 时，[Vite](https://vite.dev/) 还不存在。我们在 Wrangler 中使用 esbuild 来打包您的 Workers。Wrangler 在 :8787 上提供的开发服务器是 Wrangler 团队自己构建的，对其进行任何修改都意味着要深入 Miniflare 等 Cloudflare 专属本地工具的内部。

Vite 在这方面是一个巨大的进步，它拥有丰富的插件生态系统，提供具备 HMR（热模块替换）的同类最佳开发服务器，并使用基于 Rust 的库 Rolldown 进行 tree-shaking 构建。您用 Vite 能做的一切，都可以用 Cloudflare Vite Plugin 来实现。

Cloudflare Vite Plugin 是我们建议您构建 Workers 的推荐方式，无论您在构建什么：无论是以前端为主的项目还是后端 API。结合我们的 Vitest 插件，它提供了一个与 Cloudflare Workers runtime 相匹配的一体化开发和测试环境，让您直接访问绑定和平台 API。

cf 默认基于 Vite 构建。您的大多数 Workers 将在 AI 智能体的协助下轻松迁移。其他的可能需要更多时间，这就是为什么 cf 将继续把需要继续使用 esbuild 的 JavaScript Workers 以及 Rust 和 Python Workers 的开发和部署委托给 Wrangler。

## **从 Wrangler 迁移**

将 Worker 从 Wrangler 迁移就像运行 cf migrate 一样简单。

已经使用 Vite 构建的 Workers 将自动转换为 cloudflare.config.ts。如果您的 Worker 依赖 Wrangler 的 esbuild，cf 将继续把构建委托给 Wrangler。

当公开测试版结束时，我们将发布 Wrangler 的最终主要版本，引导您和您的 AI 智能体使用 cf。在测试版结束后，我们将继续为 Wrangler 提供 18 个月的维护支持，以便您有时间进行迁移。

您也可以运行 `cf init/deploy` 来自动为 Cloudflare 配置新项目，它将为您安装 Cloudflare Vite Plugin 并创建配置文件。

静态网站仍然不需要配置文件即可启动，部署它们就像在您的项目中运行 `cf deploy` 一样简单。

要使用 cf 启动一个新的 Hello World 项目，请使用 `cf init`。

 _cf 是开源项目，如有问题请[ 反馈至我们的 GitHub 仓库](https://github.com/cloudflare/cf)_。

]]>01M3VNYNVX3K8QX4370PSFX4H5Cloudflare 2026年度创始人致函https://blog.cloudflare.com/zh-cn/cloudflares-2026-annual-founders-letter/ Tue, 29 Sep 2026 09:43:38 GMT自 2010 年 9 月 27 日 Cloudflare 成立以来，互联网经历了前所未有的变化。随着自动化流量超过人类活动，我们思考 AI 智能体的崛起、新一代创作者的出现，以及我们如何帮助 Web 构建一个公平、可持续的未来。AI互联网趋势创始人的信开发人员平台生日周本周，Cloudflare迎来16岁生日。就像许多16岁少年一样，我们环顾着自己成长的世界，感受到一种夹在过去与未来之间的心情。也像许多16岁少年一样，面对世界的种种变化，我们有时会看到风险。但总体而言，我们对未来充满乐观。驱动我们乐观、也带来隐忧的，是同一种认识：变革必然伴随着颠覆。

今天，互联网正在经历自 Cloudflare 于 2010 年 9 月 27 日创立以来最剧烈的变化。 其中一些变化，看起来无疑是好的；另一些则在颠覆我们对互联网运作方式的认知。 

一个显著的变化，是互联网自身的增长速度。从 2012 年到 2025 年，互联网整体停滞，某些指标甚至有所萎缩。到 2025 年中，这一局面发生了转变——新网站数量呈爆炸式增长。流行的说法是，这一增长由 AI 生成的“垃圾内容”所驱动。这种情况确实存在，但并不是我们所观察到的主流。

相反，AI 释放了一批新的创作者。那些有想法却缺乏编程技能的人，借助所谓的“氛围编程”工具，将自己的创意变为现实。我们感到自豪的是，这些工具中的大多数都将 Cloudflare 的开发人员平台作为首选的部署目标创纪录的速度涌现。如今，超过 700 万名开发者正在 Cloudflare 开发人员平台上构建未来。 技术最美好的样子，就是让更多人得以表达创造力。我们坐在前排，见证世界各地的学生开发应用、解决现实问题；见证怀揣新商业点子的初创企业以创纪录的速度成立。

过去一年，互联网的使用者——乃至越来越多的“使用方式”——也在发生变化。我们最初预测，自动化流量将在 2027 年下半年超过人类流量。但 AI 智能体和 AI 爬虫的兴起，将这一时间点提前到了2026 年 5 月。如果当前趋势持续下去——这甚至算是保守估计——五年后自动化流量将达到人类流量的1000倍。不是因为我们认为人类流量会减少，而是来自 AI 智能体的流量正在爆炸式增长。

对于使用者来说，这些 AI 智能体已经令人叹为观止。让某个智能体帮你查询航班、搜索承包商或找到更便宜的手机套餐，它一分钟内就能阅读比你一整个下午能查看到的更多页面内容，然后给你一个答案。 它代替你完成所有跑腿。

但这些跑腿不是免费的。如果你让 AI 智能体推荐午餐地点，它可能要翻遍周边 1000 家餐厅的菜单，最终只推荐一家。那一家餐厅或许得到了你的惠顾，但其他 999 家却不得不承受接待这个 AI 智能体的负荷，而什么也没得到。这里的风险是一个公地悲剧式的问题：从 AI 智能体及其流量中获益的用户，并不为自己给系统造成的负荷承担成本，因而也不会对自己的使用做出适度节制。

AI 让学生和初创企业比以往任何时候都更容易构建产品。而 AI 智能体却可能让任何人都更难被找到。今天，小企业靠情感或便利性赢得顾客。你光顾某家小店，是因为柜台后面的人记得你的名字，或者因为那是你生活方式的一部分。你在路边的杂货店购物，即便知道那里的选品和价格未必最优，但它就在你回家的路上。

你的 AI 智能体不在乎谁记得你的名字，它也不会在回家路上经过你家附近的那家店。它挑的是自己掌握信息最多的那一家——而那往往是开店最久的那家。随着 AI 智能体经手的交易越来越多，风险在于它们会让新进入者愈发难以挤进市场。这反过来很可能导致市场向少数玩家集中，商业生态也不再那么有韧性。 

我们曾经也是新进入者。十六年前的这一周，我们在 TechCrunch Disrupt 的舞台上发布了 Cloudflare，工程师们正坐在台下修复 bug。我们走上舞台时，还剩 8 个 bug 未解决。走下舞台时，全部修复完毕——我们已在三大洲的五个数据中心正式上线。当时没有任何 AI 智能体会推荐我们。但人们还是给了我们机会。我们希望下一批新进入者也能拥有同样的机会。

这就是我们奋斗的目标。不是一个由五家 AI 公司主导的未来，而是一个由遍布全球各地的 50 万家公司构成的未来。不是一个内容创作者因无法获得报酷而凋零消亡的未来，而是一个任何人都能创作内容、触达全球受众并从中获得回报的未来。不是一个少数巨头预设胜出的未来，而是一个拥有更好产品的新进入者能够出色服务客户、赢得市场的未来。

去年，我们写了 AI 对出版商的冲击。今年，同样的变化正在蔓延至餐厅和熟食店。什么将取代互联网旧有的商业模式，是未来五年最值得关注的问题。本周，我们再次尝试回答这个问题。

就像每个生日一样，我们的庆祝方式是送礼，而不是收礼——其中一些礼物，是送给那 999 家餐厅的。AI 智能体抓取网络的方式和搜索引擎历来一样：什么都抓，一遍又一遍，不管内容有没有变化。 我们的数据表明，良性机器人抓取的内容中，一半以上自上次访问以来从未变化。我们一直在努力，让爬虫只抓取更新过的内容，反而因此看到更广的网络世界，同时也减轻了所爬取网站的负担。而且，我们正在为任何在网上发布内容或应用的人提供一条途径，让他们在 AI 智能体使用其成果时获得报酬。

Cloudflare 的使命不是构建更好的互联网，而是帮助构建更好的互联网。这意味着我们无法独自完成。因此，本周我们也将宣布与那些与我们志同道合、共同期待这一未来的企业和组织建立合作伙伴关系。

就像这个 AI 新时代里其他 16 岁少年一样，我们也得以发布我们的观点。我们把这些观点发布出去，是为了一个仍然容得下这些人的互联网：某个刚发布自己第一款应用的少年，那家记得你名字的熟食店，以及正在构建下一个 Cloudflare 的人。 

对此，我们从未如此激动。

]]>01M3P8MES046PPBTRQKYSNQBTJ当扫描器漏掉攻击时：Cloudflare Client-Side Security 如何保护网店https://blog.cloudflare.com/zh-cn/client-side-security-finds-4-malicious-campaigns/ Tue, 29 Sep 2026 08:04:43 GMT现代网店的页面看起来可能一切正常，而恶意 JavaScript 却在暗中悄然窃取收益、劫持点击或篡改 Analytics 数据。了解 Cloudflare 的机器学习 (ML) 模型如何揭示隐蔽的客户端攻击，以供分析师深入调查。AIClient-Side SecurityCybersecurityeCommerceMachine LearningPage ShieldWorkers AI应用程序安全开发人员开发人员平台恶意 JavaScript现代网店的页面看起来可能一切正常，而恶意 JavaScript 却在暗中运作：窃取联盟营销佣金、劫持搜索和点击、篡改 Analytics，或向远程服务器请求下一步执行的指令。页面正常加载，商品正常展示，结账流程也毫无异常，然而浏览器可能正在悄然执行网站所有者从未授权的操作。

这正是我们 Client-Side Security [机器学习 (ML) 模型](https://blog.cloudflare.com/client-side-security-open-to-everyone/)要揭示的盲点。本文将追溯四种恶意操作，涵盖八个恶意有效负载，均由 Page Shield ML 在真实流量中发现。

这些恶意有效负载的检测均为自动完成，人工验证仅在系统标记之后才介入。事后，我们使用安全扫描工具对这些活动进行复查，发现八个有效负载中有七个在 VirusTotal 上完全查无记录，URLScan 对其中任何一个均未给出恶意判定。**与此同时，[ Page Shield ML](https://www.cloudflare.com/products/client-side-security/?cf_page=client-side-security-finds-4-malicious-campaigns%2F) 却在实时流量中捕获了全部八个负载**。

以 [Lnkr](https://www.netskope.com/blog/ad-injector-dulls-chromes-luster) 家族为例，虽然安全研究早在数年前已记录了这个更广泛的恶意软件家族，但其中一个特定的负载版本在 URLScan 上被索引了近两年半，始终处于“未分类”状态，包括在 2024 年 1 月的一次直接扫描中也是如此。在这一案例中，VirusTotal 较早收录了该有效负载：目前已将该脚本标记为恶意，但公开历史记录并未显示该判定最初是何时给出的。与此同时，Page Shield ML 独立地在一家在线零售商的网店实时流量中发现了完全相同的代码。更普遍的情况是：一个哈希值可能早已被收录，但其背后的代码被判定为恶意却要晚得多。如果您的防御依赖于这一标签，那您已然落后一步。您需要能够解析 JavaScript 本身并大规模判断的 ML 能力。

能看到一个文件，并不等于理解它。难点在于：这四种操作没有共同的通用签名，也没有统一的隐藏手法。其中一个除非设备、国家、时间、引荐来源或浏览器状态符合其预设条件，否则始终保持休眠。另一个将无点击联盟请求藏在不可见的 iframe 中。还有一些拦截点击、压制监控，或有条件地从远程服务器加载额外代码。要捕获它们，必须观察这些组件如何协同工作：脚本何时激活、隐藏了什么、拦截了什么、接下来又获取了什么。仅扫描页面一次是不够的；正如这些案例所示，此类脚本的设计目标就是保持静默，直到合适的受害者出现。**这正是持续的浏览器可见性能够决定是否抓住攻击的关键所在。**

## **我们如何大规模检测和标记 JavaScript**

本文中标记四种操作的图神经网络 (GNN)，此前已成功检测出[恶意 npm 包](https://blog.cloudflare.com/how-cloudflares-client-side-security-made-the-npm-supply-chain-attack-a-non/#finding-needles-in-a-3-5-billion-script-haystack)以及[在真实网络环境中活跃的 Magecart 支付窃取脚本](https://blog.cloudflare.com/navigating-the-maze-of-magecart/#proactive-detection)。GNN 不将 JavaScript 视为扁平的文本块，而是将代码作为图来推理：通过[语法树](https://blog.cloudflare.com/how-we-train-ai-to-uncover-malicious-javascript-intent-and-make-web-surfing-safer/#using-syntax-trees-to-classify-malicious-code)连接代码符号，揭示调用关系、攻击者试图隐藏的内容，以及仍在"回拨"的部分。这种结构使其能够在代码经过压缩、重命名乃至部分混淆之后，依然识别出可疑模式，而无需依赖已知 URL 或字节签名。

系统会将 GNN 标记为恶意的少数脚本（在所有分析流量中占比不足 0.3%）发送至 Workers AI 上的轻量级[大语言模型 (LLM)](https://www.cloudflare.com/learning/ai/what-is-large-language-model/?cf_page=client-side-security-finds-4-malicious-campaigns%2F) 进行[实时复核](https://blog.cloudflare.com/client-side-security-open-to-everyone/#adding-an-llm-based-second-opinion-for-triage)。这一环节在保持高召回率的同时进一步降低了误报率。当 LLM 与 GNN 的判断一致时，系统便会向客户发出警报。

为了大规模调查最复杂的脚本，我们使用一组前沿模型，称之为"教师"（一个由自动化评判者组成的集成）。该组合涵盖约六个不同模型家族的领先成员，其中包括在 Workers AI 上运行的开放权重模型。我们将每个模型作为独立 Agent 启动，在各自全新、独立的会话中分析同一可疑脚本。必要时，其智能体工具访问权限允许它们使用受限 JavaScript 求值器来解包小段代码，揭示隐藏行为。我们很快会将 [Cloudflare Sandbox](https://developers.cloudflare.com/sandbox/?cf_page=client-side-security-finds-4-malicious-campaigns%2F) 整合到这个工作流程，以便在隔离环境中进行更深入的分析。

前沿模型有时会产生分歧，尤其是在最复杂的脚本上。我们将这种分歧视为信号，而非噪声。每个标记相当于一张“选票”，并根据该模型在“[人工智能分析指数](https://artificialanalysis.ai/leaderboards/models)”中的评分进行加权；由此生成四类标签的概率分布：良性脚本、支付数据窃取 ([magecart](https://blog.cloudflare.com/navigating-the-maze-of-magecart/))、其他恶意软件，以及加密货币挖矿。因此，人工审查员只需检查被标记为恶意或未达到明确三分之二多数的脚本。我们随后将这些标签分布反馈回 GNN 训练，使其能够区分越来越细微的案例。这一反馈循环目前仍部分依赖人工操作，但我们正在逐步实现自动化。

## **我们捕获的四种恶意 JavaScript 操作**

这四种操作的目的各不相同，从佣金盗窃到窃取商店已付费获取的购物者 Analytics 数据，不一而足。盗窃佣金与盗刷信用卡不同，劫持搜索与窃取密码也截然不同。如果 ML 模型只识别其中一种手法，面对其他手法就会"睡着"。因此，我们的 Page Shield ML 必须对各种恶意行为保持敏感。

接下来，让我们深入剖析每种恶意操作及其运作机制。

**操作**| **对客户的影响**| **脚本行为**  
---|---|---  
**1) 非工作时段联盟营销佣金劫持器**|  劫持联盟营销佣金| 移动设备与时间门控；动态页面监控；点击拦截；多日冷却期  
**2) 无点击联盟盗窃**|  无需用户点击即可窃取联盟营销佣金| 屏幕外 iframe；自动点击隐藏链接兜底；虚假 IP 查询请求与时间门控；每小时联盟轮换  
**3) 旧式搜索破坏者，现转型为网店后门**|  追踪用户并开设任意远程 JavaScript 执行后门| 遗留关键词屏蔽；localStorage 退出；遥测；远程代码加载  
**4) 付费移动端伪装器**|  屏蔽商店对带活动标签移动访客的可见性，试图替换广告和 Analytics，并隐藏客服支持| 主机、视口与 UTM 标签门控；325 条 IP 子串列表；禁用 9 个监控/Analytics 工具；零像素追踪信标  
  
## **操作一：非工作时段联盟营销佣金劫持器**

设想一个安静的周日下午：一位购物者用手机点击了一件商品。脚本并不正常响应这次点击，而是从攻击者预先选定的列表中打开一个商品或活动落地页到新标签页，同时将原始标签页通过联盟路由引导。网店表面上看起来运转正常。如果购物者完成了购买（无论是当时还是之后），这次"绕路"就劫持了归因，将销售（及由此产生的佣金）记入一个并未带来这位购物者的账户。

### 商店的损失

商店可能向一个未带来购物者的账户支付了不应得的佣金。更糟糕的是，如果确实有合法合作伙伴促成了引荐，这次强制请求可能导致归因错误，将本应属于真正付出努力的合作伙伴的信用和潜在报酬转移走。损失可能不止一笔佣金：一旦合作伙伴对归因系统失去信任，也可能对背后的零售商失去信任。

### 攻击链

`符合条件的移动访客 → 拦截商品点击 → 脚本选定页面在新标签页打开 + 原始标签页沿攻击者联盟路由跳转`

### **如何保持隐蔽**

我们发现了五个相关脚本版本：捕获时两个处于活跃状态，三个处于暂停状态。每个活跃变体在采取行动前使用一组不同的门控条件，检查内容包括：访客设备、本地时间、近期是否已执行过该操作、页面上是否出现了商品按钮，以及是否有人实际点击了它。这套繁复的规则使恶意行为在简短的自动化访问期间无法显现，除非满足该变体的特定条件。活跃脚本使用 MutationObserver（一种 JavaScript API）监视页面首次加载后动态出现的商品卡片和按钮，从而拦截这些后加载元素上的点击——而仅加载一次 HTML 就停止的爬网程序可能完全错过这条重定向路径。

在较新的活跃变体中，脚本拦截到符合条件的点击后，会向 `localStorage` 写入为期三天的冷却期记录（在该设备上休眠数天）。随后执行双标签页操作：在新标签页弹出攻击者选定的商品页面以留住购物者，同时让原始标签页悄无声息地经由攻击者的联盟追踪链接快速跳转并返回商店，在后台植入攻击者的归因 Cookie。控制台屏蔽和源码自我防御检查使分析更为困难，而冷却期和严格的时间窗口则限制了恶意路径在正常购物过程中出现的频率。

以下经过脱敏处理的代码片段展示了有效负载如何挂钩动态商品卡片并执行双标签页绕路操作。 _我们简化了标识符，重新格式化了代码，并对目标 URL 进行了中性化处理以便阅读。_

暂停的版本展示了该活动如何在不移除脚本的情况下"销声匿迹"。其内嵌配置将 status 设为 "`paused`"，因此脚本在安装点击处理程序之前就已退出。这些暂停的脚本携带了不同的每访客冷却期配置（分别为 3、4 和 5 天）。其中一个暂停脚本甚至记录了版本历史注释，明确说明该活动在黑色星期五之后暂停。

为了触达访客，该操作利用了网站的营销供应链：电商网站为追踪广告活动和 Analytics 而嵌入的第三方脚本和标签管理器。一条已确认的投递路径经由两个本身正常的标签管理器：Google Tag Manager → 另一个标签管理器 → 恶意脚本。这是有效负载到达浏览器的方式，并不能证明任何一个标签管理器遭到了入侵。

攻击者甚至伪装了托管脚本的域名，以通过快速营销审查。一个投递主机藏在明处：`adtargett[.]com` 与 1998 年注册的广告域名 `adtarget[.]com` 仅差一个字母"t"。这个仿冒的域名在 2025 年注册，而且经我们核实，其主页自称为“[Adtarget.com](http://Adtarget.com) \- Performance Marketing Agency”。这是一种域名抢注手法：通过模仿正规的广告代理机构，该主机混入了常规营销标签，悄然投递劫持购物者点击并将其引入联盟支付链接的恶意有效负载。

## **操作二：无点击联盟盗窃**

第一种骗局至少还需要一次点击，而这一种连点击都不需要。购物者可以打开一个预订页面，仔细浏览商品选项，却从未点击任何广告。然而在后台，脚本可能已经发出了一个联盟请求，足以让之后的一笔销售看起来像是由其他人引荐了这位购物者。当脚本的触发条件满足时，有效负载会通过隐藏的 iframe 或一个自动点击的链接发送该请求。

### 商店的损失

对于受影响的旅游业务而言，此次攻击可能扭曲客户获取的经济逻辑：一笔合法的预订或购买可能被归因到一个不应得佣金的联盟账户。代码证明存在隐蔽的自动联盟请求，但实际上是否有具体请求导致了归因完成、账户记账或佣金支付，目前尚无法确认。

### 攻击链

`时间门控浏览器 → 隐蔽联盟请求（屏幕外 iframe）→ 1 小时节流 Cookie → 被阻止时自动点击隐藏链接兜底`

### **如何保持隐蔽**

脚本通过两层机制隐藏联盟请求：选择性执行（预检网络门控与小时级调度）和隐蔽投递（屏幕外 iframe）。第一层令人意外，因为其国家标签与实际地理位置毫无关联：既不取决于购物者所在地，也不取决于商店所在地。

首先，脚本调用一个公开的基于 IP 的地理位置服务，但完全忽略返回的所有数据，包括购物者所在国家。我们无法确定为何它需要成功的响应却又忽略返回的数据；这可能是为了迷惑调查人员，也可能只是早期版本的遗留代码。值得注意的是，如果地理位置请求失败，脚本会静默停止——其 Promise 链以 .catch(() => {}) 结尾。虽然意图无法证实，但这种"失败即关闭"的行为可能有助于脚本规避受网络限制的沙盒环境。

接下来，脚本并未使用获取到的地理位置数据，而是内嵌了三个 TradeDoubler（一个联盟营销网络）配置对象，分别标记为 {`AU`, `US`, `UK`}。这些配置块硬编码在代码中，每个包含一个联盟 URL 及起止时间。脚本用 JavaScript 计算 `Asia/Kolkata` 时间，检查这些配置的时间窗口，再应用固定的奇偶小时规则来选择三者之一，或跳过本次联盟请求。选择过程是确定性的。

调度机制与浏览器状态检查共同构成了时间门控选择性执行，这是一种伪装技术。当这些条件不满足时，联盟行为保持休眠，使得单次检查可能完全错过它。

一旦脚本选定配置，就会写入一个名为 `affiliateClicked_<market>` 的本地 Cookie，作为一小时的重试节流，避免立即对同一地区重复触发（这是一个客户端节流机制，用于减少噪声，而非联盟网络的归因 Cookie）。随后，脚本在关闭了引荐来源的屏幕外 iframe 中加载该联盟 URL。iframe 是主要投递路径，但附带一个激进的兜底机制：如果 iframe 报错或在一至两秒内未能完成加载，脚本会创建一个没有 target 属性的隐藏链接（`<a>`）并以编程方式点击它，这可能会导航用户的当前活动标签页。对于符合条件的购物者而言，一切看起来毫无异常：他们从未看到广告，无需点击任何内容，关闭标签页时也不会察觉任何异样。

脚本的混淆手法简单却有效：甚至属性名都是逐字符拼接而成。以下经过脱敏处理的代码片段展示了有效负载如何创建不可见的屏幕外 iframe。 _我们重命名了关键标识符并重新格式化了代码以提高可读性。已移除目标地址。_

## **操作三：原先的搜索劫持恶意脚本，如今变成植入电商网站的后门**

多年前，[Lnkr](https://www.netskope.com/blog/ad-injector-dulls-chromes-luster) 恶意软件家族因藏身于可疑浏览器扩展程序而成为新闻报道的焦点；它们通过拦截 Google 和 Bing 搜索请求来重定向结果并窃取广告收益。如今，攻击者重新利用该代码库，将其改造成植入某在线零售商网站的后门。

由于脚本运行在商店页面而非搜索引擎上，其旧有的重定向功能保持休眠。这一次，脚本被用于向攻击者回传遥测数据。更危险的是，它为攻击者提供了一扇远程大门，可以随时在客户浏览器中任意下载并执行新的 JavaScript，而无需修改服务器上的任何文件。它甚至保留了一个来自其扩展程序时代的老把戏：如果有人在 Google 中输入"virus"或"popup"等词语，脚本就会自动关闭。从外部来看，商店照常运营，丝毫看不出任何异常。

### 商店的损失

商店失去了对在客户浏览器中运行代码的控制权。攻击者在暗中追踪访客会话，并拥有一扇直接的后门，可以随时向网店推送并运行任意 JavaScript。

### 攻击链

`HTML 引用脚本 → 分析规避门控 → 并行主机门控分支（休眠搜索模块 vs. 活跃后门）→ 任意远程 JavaScript 执行`

### **如何保持隐蔽**

与通过标签管理器投递的活动不同，该脚本被直接嵌入商家的 HTML 中。我们无法确定最初的入侵途径；实际上，直接 HTML 插入通常通过入侵商店管理员凭据、未经授权的模板编辑，或受感染的第三方主题或插件来实现。

在底层，该脚本是一个模块化工具包，同时携带活跃代码和休眠代码。其旧模块（透明点击叠加层、搜索引擎查询拦截器、扩展程序商店链接改写器，以及针对仿冒域名的重定向，如用 `buking[.]com` 代替 `booking[.]com`）仅在特定目标网站上激活，因此在这家网店上保持关闭。几个内嵌域名（`sugabit[.]net`、`votetoda[.]com`、`cdnpps[.]us` 以及遥测端点 `hanstrackr[.]com`）位于这些禁用模块内。

在该商店上，活跃分支专注于规避、遥测和远程控制：

  * **对安全研究人员装死。** 继承自浏览器扩展时代的规避手法：脚本监控搜索输入和 URL 查询中的广告软件特征词。搜索到一个安全关键词，脚本在本次访问中暂停运行；搜索到两个或更多，则向 `localStorage` 写入持久退出记录，在该分析人员的设备上永久屏蔽脚本，使重复测试一无所获。尽管最初是为了躲避搜索引擎上的分析人员而构建，但据我们所知，该检查被硬编码为专门针对 Google 搜索 URL，在商家网店上保持休眠状态。
  * **动态远程代码执行。** 脚本无需修改网店即可改变其行为。虽然硬编码的域名（`scrprime[.]com`、`youronlinesearches[.]com`、`jullyambery[.]net`）与早期捕获版本完全相同，但这些端点返回的内容完全由攻击者决定。脚本可以将访客遥测数据回传给这些服务器，向其请求新指令，并将全新 JavaScript 直接拉取到购物者的浏览器中执行。这实际上为攻击者提供了一扇可在网店上运行任意代码的实时后门。我们无法确定实际投递了哪些二阶段有效负载。



总而言之，网站的静态快照只显示正常的网店页面，而底层的状态检查、反分析陷阱和远程加载分支则暴露了后门的存在。

## **操作四：付费移动端伪装器**

商店已为这位来自移动广告或营销活动的访客付费获取流量。恶意脚本放行了这次访问，随即切断商家的可见性。Analytics 数据陷入黑暗，在线客服聊天消失，而一个流氓观察者开始对这个商店刚刚花钱买来的会话录制遥测数据。

在幕后，除非访问满足一套精细的条件，有效负载才会运行：确切的目标网店、狭窄的移动屏幕尺寸，以及在访问前两个页面期间带有活动标签。在笔记本电脑、企业网络、云服务商和 VPN 上，脚本保持休眠——而最有可能调试页面的工程师恰恰使用这些设备，因此他们永远无法看到脚本触发。脚本还依托一份包含 325 条 IP 字符串的手工拒绝名单，在指定的美国城市和地区保持休眠，以规避自动扫描器和安全分析人员。只有在所有条件都满足之后，脚本才会尝试拆除商店的监控体系、替换广告和 Analytics 标识，并回传信息。从错误的设备或网络进行的二次检查永远不会触发它。与此同时，网店照常营业。

### **商店的损失**

对于直接面向消费者的零售商而言，该恶意软件专门针对商店通过付费搜索和营销活动（`ppc`、`cpc`、`sms`、`paid`）花钱获取的高价值流量。这些客户仍然可以正常购买。然而商店面临三重明确威胁：广告归因被转移、发布商获得不应得的报酬；九个可观测性工具丧失关键的会话 Analytics 数据；客服聊天和联系表单被屏蔽（导致购物者无法提问或报告异常）。在沙盒化浏览器环境中进行的动态分析证实，替换的 Analytics 脚本加载并触发了一个追踪信标（一个不可见的网络请求，用于记录访客活动），但攻击者在实践中是否成功获取了会话遥测数据或转移了广告收益，目前仍无法证实。

### 攻击链

`带活动标签的移动端访问 → 多层伪装与网络门控 → 监控被破坏 → 广告、Analytics 和客服支持控制被改写 `

### **如何保持隐蔽**

为了融入商店的营销供应链，攻击者从 `sdk-amazonaws[.]com` 投递有效负载。该仿冒域名注册于 2024 年，与官方 Amazon Web Services 域名（[`amazonaws.com`](http://amazonaws.com)，注册于 2005 年）毫无关联。为进一步加深迷惑，攻击者还在该域名前添加了一个模仿知名电商营销平台的子域名。这种叠加了双重可信品牌的仿冒域名，构造出一个极具欺骗性的伪装，专门设计用于在快速标签审查中蒙混过关。Amazon Web Services 及被模仿的营销平台均未参与此次攻击，也未受到任何入侵。

脚本加载到浏览器后，在触发主要有效负载之前，执行了一套极为密集的伪装门控：

  * **目标主机与浏览上下文。** 脚本验证 `window.location.hostname` 是否与其构建目标的特定商家主机匹配（在其他任何地方立即退出），确认当前窗口为顶层窗口（非嵌套 iframe），并检查路径中是否不含 `/challenge`。还验证追踪标记 Cookie（`_cart_dr` 和 `_logo_ alt`）是否尚未在浏览器中存在。
  * **设备与活动过滤。** 访客视口宽度必须小于 `477` 像素（手持智能手机）。此外，访客必须通过"首次接触"（初始引荐）的方式到达，且活动标签须包含六种特定 UTM 媒介（Urchin Tracking Module，用于追踪营销活动的标准 URL 标签）之一：`ppc`、`cpc`、`sms`、`paid`、`flow` 或 `campaign`。同时必须是该会话的第一或第二次页面加载。值得注意的是，代码中包含一条名义上的非 UTM 路径，但它要求会话页面计数同时大于 -1 且小于 -2（数学上不可能成立），致使该分支完全无法到达。这可能是又一种转移注意力的手法，也可能是代码变更的遗留产物。
  * **那个"随机"门控，实则永远通过。** 代码中出现了一个看似概率节流的逻辑（`Math.random() <= threshold`），意图让执行看起来是间歇性的。然而，当我们对反混淆后的算式求解时，发现阈值恰好等于 1。由于 JavaScript 的 `Math.random()` 返回值始终严格小于 1，该门控始终判定为 true。与那条不可达的非活动分支一样，这是一个实际上从不起任何决定作用的条件。它可能是遗留的节流代码，也可能是故意设置的伪装，用于迷惑阅读混淆数学算式的人。无论如何，捕获的有效负载从未用它来跳过符合条件的访客。
  * **第三方 IP 情报。** 脚本使用内嵌密钥查询外部第三方 IP 情报 API，要求连接来自美国移动消费者网络，同时若响应标记为企业网络、托管设施、云服务商、bogon、Tor 出口节点、VPN、代理、中继或一般威胁指标，则立即退出。
  * **地理排除。** 有效负载不对来自特定地区（`US-NY`、`US-CA `和 `US-NHDD`）或特定城市（San Francisco、Plymouth、Compton、Hopkinton 和 Lafayette）的访客激活。
  * **325 条 IP 子串陷阱。** 脚本将访客 IP 与一份包含 325 条完整 IPv4 地址字符串的内嵌拒绝名单进行比对。去重后，这些地址代表 249 个不同三段前缀下的 313 个唯一地址。作者没有采用结构化的 CIDR（无类别域际路由）子网匹配，而是简单地截去访客 IPv4 地址的最后一段，进行原始子串搜索：`!denylistString.includes(visitorPrefix)`。



精简后的伪代码展示了多层主激活漏斗的逻辑如下：

**破坏可观测性并劫持标识**

只有在所有主要门控全部通过之后，脚本才执行其有效负载：

  * **致盲监控工具。** 脚本搜索 DOM，移除九个可观测性和 Analytics 服务的 script 标签：Lucky Orange、Segment、Optimizely、New Relic、Bugsnag、LogRocket、Hotjar、Microsoft Clarity，以及商店的 Google Tag Manager 容器（`GTM-<redacted>`）。在剩余的内联脚本中，脚本将对这些工具的引用字符串替换为无效的虚假标识符（`hji0`），使对这些工具的调用静默失败，试图致盲商店的错误报告和监控功能。
  * **屏蔽客服支持。** 脚本注入 CSS 并移除相关元素以隐藏客服聊天和联系表单容器，切断客户与商店支持的直接联系。
  * **替换广告与 Analytics 标识。** 脚本清除 Google Ads 全局变量（`google_ad_modifications`、`adsbygoogle`），拆除现有广告位（`ca-pub-<original>`），并以替换的发布商 ID（`ca-pub-<replacement>`）加载 Google Ads。随后注入一个配置了流氓替换项目 ID 的新 Microsoft Clarity 会话回放脚本。



**更简单的独立信标与 600 天标记**

与精密的主伪装逻辑形成鲜明对比，有效负载还包含若干独立的次级信标分支（独立例程，向外部服务器静默发送 ping 以确认访问），这些分支完全绕过了视口、主机名、活动、地理和 IP 门控。如果访客处于第二个页面或更后续页面，脚本会写入一个有效期恰好为 600 天（51,840,000,000 毫秒）的持久 Cookie（`_cart_dr=1`），并向 `maper[.]info` 上的远程遥测端点发送一个不可见的零像素图片请求（一个追踪信标，用于记录浏览器到达此步骤的事实）。

另一条分支检查备用标记（`_logo_alt`），若存在则触发第二个遥测 `.png` 信标（这是脚本会查找但自身从不写入的 Cookie，很可能由配套脚本植入）。这为攻击者提供了一个简单、持久的命中计数器，用于记录整个商店所有访客的基本流量（在端点记录 IP 和 User-Agent），同时将高风险的广告劫持例程严格隐藏在移动端伪装背后（针对高价值付费到访流量）。这说明了为何仅分析一种可见效果并不能揭示多功能有效负载的完整影响范围。

## **入侵指标 (IOC)**

我们公布这些指标，以帮助安全团队和研究人员在自己的环境中检测和追踪这些活动。所有指标均直接来源于捕获的有效负载及其网络连接。列出的 URL 已进行反激活处理。部分指标因公开后可能无意中暴露受影响组织的身份而被隐去或做了泛化处理。列出的域名反映了在这些攻击的投递、重定向或遥测链中观察到的基础设施；列入名单并不意味着共享服务或托管服务商本身完全是恶意的。

**操作**| **指标**| **类型与作用**  
---|---|---  
**1) 非工作时段联盟营销佣金劫持器**|  adtargett[.]com| 脚本投递与联盟重定向仿冒域名  
**1) 非工作时段联盟营销佣金劫持器**|  gdataroute[.]com| 攻击链中观察到的联盟重定向短链接服务  
**3) 原先的搜索劫持恶意脚本，如今变成植入电商网站的后门**|  scrprime[.]com| 浏览器劫持脚本投递域名  
**3) 原先的搜索劫持恶意脚本，如今变成植入电商网站的后门**|  searchvalidation[.]com| 搜索劫持与流量重定向域名  
**3) 原先的搜索劫持恶意脚本，如今变成植入电商网站的后门**|  sugabit[.]net| 强制搜索重定向域名  
**3) 原先的搜索劫持恶意脚本，如今变成植入电商网站的后门**|  youronlinesearches[.]com| 条件性远程脚本投递域名  
**3) 原先的搜索劫持恶意脚本，如今变成植入电商网站的后门**|  hublosk[.]com| 远程脚本投递域名  
**3) 原先的搜索劫持恶意脚本，如今变成植入电商网站的后门**|  jullyambery[.]net| 远程 JavaScript API 与命令域名  
**3) 原先的搜索劫持恶意脚本，如今变成植入电商网站的后门**|  votetoda[.]com| 注入有效负载投递域名  
**3) 原先的搜索劫持恶意脚本，如今变成植入电商网站的后门**|  hanstrackr[.]com| 隐藏访客遥测域名  
**3) 原先的搜索劫持恶意脚本，如今变成植入电商网站的后门**|  adrs[.]me| 攻击链中观察到的仿冒流量重定向服务  
**3) 原先的搜索劫持恶意脚本，如今变成植入电商网站的后门**|  youradexchange[.]com| 攻击链中观察到的变现重定向服务  
**3) 原先的搜索劫持恶意脚本，如今变成植入电商网站的后门**|  cdnpps[.]us| 注入广告框架投递域名  
**4) 付费移动端伪装器**|  sdk-amazonaws[.]com| 滥用品牌信任的仿冒脚本投递域名  
**4) 付费移动端伪装器**|  maper[.]info| 条件性访客遥测信标域名  
  
## **给防御者的四点启示**

综合来看，这四种操作构成一个不断升级的故事：攻击者改变了目标、投递路径和伪装方式，但浏览器仍然必须执行其逻辑。四点核心启示如下。

**行为胜过特征码。** 这些操作追求不同形式的变现和操控，但每个有效负载仍然必须在浏览器中采取行动：监听事件、检查状态、修改页面、调度任务、发起网络请求或加载下一阶段。这正是结构分析所关注的重点：无论 URL、特征码或攻击目标如何变化，恶意载荷必然包含的逻辑特征。

**选择性执行是攻击的核心环节，不是补充说明。** 设备、时间、地理位置、引荐来源、会话、网络和冷却机制，都能轻易击败仅访问一次并获取静态快照的爬网程序。持续可见性至关重要，因为攻击可能只对特定浏览器、特定状态、在特定时刻显现。

**代码混淆提高了分析成本，但在这些案例中并未阻止检测。** 自我防御循环、控制台抑制、调试器陷阱、旋转字符串表和死代码分支，这些因素都导致分析更加复杂。尽管如此，Page Shield ML 仍然成功识别了全部四种恶意操作。快速的内部模型进行大规模可疑代码筛查，前沿模型则负责分析最复杂的案例。模型之间分析结果的差异，往往会揭示最隐蔽的混淆手法与逻辑，从而帮助我们锁定重点关注对象。

**上下文信息还原全貌。** 某些代码单独看可能平淡无奇，但一旦防御者将静态分析与动态上下文结合起来，即：考察代码的来源、触发它的浏览器状态、它建立的连接以及它在运行时的实际行为，其恶意本质便会暴露无遗。

## **对客户端执行的持续可见性**

虽然这四种操作依赖多种叠加的欺骗策略和误导手法，但它们都都面临一个共同的制约因素：其 JavaScript 必须在浏览器中执行。公开扫描器和静态爬取可能漏掉那些受特定条件触发的行为。持续观察有助于明确当真实访客与页面交互时，代码的实际运行情况。

Cloudflare [Client-Side Security](https://developers.cloudflare.com/client-side-security/?cf_page=client-side-security-finds-4-malicious-campaigns%2F) 在所有方案中提供这种可见性。您可以在安全设置下开启持续脚本监控，追踪网店上的第一方和第三方脚本；自动恶意脚本检测和告警则在 [Client-Side Security Advanced](https://developers.cloudflare.com/client-side-security/?cf_page=client-side-security-finds-4-malicious-campaigns%2F#availability) 中提供。您可以直接在 [Cloudflare 控制台](https://dash.cloudflare.com/?to=/:account/:zone/security/web-assets&cf_page=client-side-security-finds-4-malicious-campaigns%2F)中查看脚本活动并管理检测结果。

]]>01M3P21MMAW8PH30ZA3VDYABQB既要又要：拒绝 AI 训练而不影响搜索可发现性https://blog.cloudflare.com/zh-cn/accountable-mixed-use-ai-crawlers/ Wed, 23 Sep 2026 02:34:19 GMTCloudflare 面向网站所有者提供全新方法，既能保持可发现性，又能禁止 AI 训练。通过全新控制手段和 Accountable 类别，与 Apple、Google 和 Microsoft 建立了共享模型。AIAI 机器人Bot Management产品新闻安全网络服务在缺乏适当控制措施的情况下，网站所有者长期面临一个艰难的权衡：要么允许其内容用于 AI AI 训练，要么就可能面临在搜索中失去可被发现性的风险。之所以会出现这种权衡，原因在于：互联网上部分规模最大的组织会采用混合用途爬虫（mixed-use crawlers），即单个爬虫同时承担搜索抓取与 AI 训练数据获取任务。拒绝其中一个，就等于拒绝了另一方。

今天，Cloudflare 宣布推出新的[Disallow AI Training（禁止 AI 训练）](https://blog.cloudflare.com/bot-preference-sync/)设置，让您能够轻松确保内容可用于搜索目的的索引，同时拒绝让同一爬虫使用您的内容进行 AI 训练。Apple、Google 和 Microsoft 已经或承诺（在指定时间范围内）遵循此设置。

混合用途爬虫是训练问题中的难点。AI Summaries 是下一步。全站范围的“是”或“否”过于粗略：您的内容在 AI 摘要中出现了多少，跟它是否能够被收录一样重要。允许选择退出 AI 摘要已经是我们针对混合用途爬虫运营商设定的要求之一。到明年初，我们的目标是让您控制：您的内容中有多少会被纳入——只需在 Cloudflare 上设置一次，无需分别通过每个运营商分别处理。

## 为什么光问并不足够

大多数网站所有者希望人类、智能体和（良性）机器人能够找到他们。然而，开放互联网中相当一部分内容是通过广告、订阅或与访问者的直接关系来获得资金支持的；此类模式只有在用户真正访问页面时才会支付。

几乎每个网站所有者都认为搜索是有益的：不到 1%的 Cloudflare 网站选择屏蔽搜索机器人。然而，训练则是另一回事：17% 的站点选择启用某种机制来阻止训练。正因为如此，我们认为网站所有者需要更精细化的控制选项，而不是一刀切“禁止 AI”。

仅靠 robots.txt 指令无法解决这个问题。任何网站都可以发布一份，但它无法识别谁在爬取、确定爬取的目的，或阻止忽略指令的爬虫。

然而，一个网络可以解决这个问题：我们发布偏好，识别谁在爬取，分类爬取目的，并阻止那些忽略偏好的爬虫，然后在 [Radar](https://radar.cloudflare.com/ai-insights#ai-bot-transparency)上报告每个运营商的实际行为。

但阻止会赶走爬虫。它不会改变爬虫的行为。更好的结果是：运营商不需要您进行选择。因此自 7 月起，我们一直与他们进行直接对话。反馈令人鼓舞：几乎所有运营商都同意，站点所有者应当对其内容如何被使用拥有控制权，并获得相关透明度；同时也要有保证，即他们的选择将会被尊重。为了帮助网站所有者理解这一点，我们创建了一个称号：Accountable。

Accountable 称号：既包括目前可用的能力，也包括落实并交付这些能力的具体承诺。若要获得这个称号，机器人运营商必须满足或承诺满足以下要求：

  1. 网站所有者通过 robots.txt 或类似标准选择不参与 AI 训练的机制。
  2. 一种面向网站所有者的机制，让网站所有者能够直接在运营商处选择退出 AI 摘要。这样功能将于明年通过 Cloudflare 实现（详见下方章节）。
  3. URL 级别的可见性，了解哪些页面被用于训练，以及显示内容如何出现在搜索中的指标。
  4. 确保选择退出 AI 训练不会影响传统搜索结果。



苹果、谷歌和微软均证明符合 Accountable 的资格。每一家都把目前可用的能力与针对仍在研发中的内容的限期承诺结合起来。每家公司的爬虫详细信息如下。

## 新的安全设置选项

Cloudflare 根据行为对机器人进行分类，一个机器人可能表现出多种行为。提供了三种行为作为控制：

  * **搜索** \- 爬网以建立搜索索引。
  * **训练** \- 爬取数据以训练或微调模型。
  * **智能体** \- 受用户指示的智能体，代表人类访问网页，例如 chat fetch bots 和 browser-use agents。



混合用途爬虫是一个同时执行搜索和训练的抓取工具。如果缺少这些控制措施，这一双重功能将带来前面提到的权衡取舍：站点所有者无法在不同时拒绝另一用途的前提下拒绝其中一种用途。

为避免阻止 Accountable 混合用途爬虫——这些爬虫不会强迫网站所有者承担上述权衡取舍——我们正在引入一个新的设置：Disallow AI Training（阻止 AI 训练）。“Disallow AI Training”是根据其在 robots.txt 中发布的 Disallow: 指令命名的。

### “Block” 设置的含义现在已经发生了变化。

“Block”和“Block on pages with ads” 以前不适用于混合用途爬虫，因为对它们进行阻止也可能影响搜索可发现性。鉴于新增 Disallow AI Training 设置，“Block” 以及 “Block on pages with ads” 现在适用于 _所有_ 训练爬虫，包括混合用途爬虫。

训练、搜索和智能体控制在域名级别应用。新增“Disallow AI Training”后，可用设置包括：

  1. **Allow** ：允许所有爬虫，除非被其他设置或 WAF 规则阻止。
  2. **Disallow AI Training** ：Bot Preference Sync 会在 robots.txt 中发布适用的“禁止训练”偏好。Accountable 混合用途爬虫仍然被允许用于搜索。所有其他训练爬虫均被阻止，包括由 Amazon、Anthropic、Meta 和 OpenAI 运营仅用于培训的爬虫。禁止 AI 训练仅作为训练的设置提供，不适用于搜索或代理。
  3. **Block on pages with ads** ：爬虫——包括混合用途爬虫——仅在检测到广告的页面上被阻止。
  4. **Block** ：所有爬虫，包括混合用途爬虫，均被阻止。



Disallow AI Training 通过在 robots.txt 中发布偏好来实现。“仅广告偏好（ads-only preference）”无法使用该方式表示：Cloudflare 能识别哪些页面用于投放广告，但这些页面清单规模太大，并且变化频繁，无法在 robots.txt 中枚举。因此不能针对有广告的页面设置 Disallow AI Training。

智能体不会像混合用途爬虫那样造成相同的搜索可发现性权衡，而互联网尚未为智能体表达 Disallow 偏好提供成熟的指令。目前，我们尚未提供针对智能体的 Disallow 设置。随着 [ai-prefs](https://datatracker.ietf.org/wg/aipref/documents/) 等标准的成熟，我们将重新审视这个做法。

## 9 月 15 日发生了哪些变化？

我们对 Bot Management 和 AI Crawl Control 进行以下更改：

  1. 现在，“Block” 和 “Block on pages with ads” 适用于混合用途爬虫，包括 Applebot、 Bingbot 和 Googlebot；因此，无论启用哪一个设置，都同时影响搜索以及训练。要阻止训练但 _维持_ 搜索可发现性，请使用 Disallow AI Training。
  2. “Block AI Bots”（阻止 AI 机器人）将被弃用，转而使用更细粒度的 Search、Training 以及 Agent控制设置。
  3. 托管 Robots.txt 将被弃用，代之以 Bot Preference Sync。启用托管 Robots.txt 的客户将迁移到新系统。
  4. Disallow AI Training 将成为特定新域推荐配置的一部分。
  5. 现有客户的偏好设置将迁移到下面描述的新控制措施。



### 您需要做什么

几乎所有情况下都不需要做任何事情。您的当前设置会自动保存。

如果您希望完全阻止混合用途的爬虫，现在必须明确表示。选择“Block”。这将阻止 Applebot、 Bingbot 和 Googlebot 访问您的网站——包含搜索在内。

#### 从未使用搜索/训练/智能体控制的现有域名。

从未配置更精细控制的站点所有者将在其旧版“Block AI Bots ”设置的基础上迁移到新设置：

#### 已配置 Search/Training/Agent 控制设置的现有域名

对于之前配置了精细化控制设置的域名，我们将在新定义下保留其选择的实际效果。此前选择的 Block 或 Block on pages with ads 将迁移到 Disallow AI Training（禁止 AI 训练）。

### 对新域的建议

从 9 月 15 日开始，客户在加入新域名时，将提供两种预设配置之一，取决于网站是否通过广告获取收入。广告收入取决于是否有真人实际看到该页面。AI 训练用一个答案替代了访问；智能体抓取页面，实际上没有真人看到广告。因此，针对以来广告支持的网站，预设配置更加严格。您可以在加入期间或之后的任何时间更改这些设置。

 _新域名的推荐设置_

## 这对特定的混合用途爬虫意味着什么？

Applebot、Bingbot 和 Googlebot 均属于 Accountable 类别。Apple、Google 和 Microsoft 承诺遵循相同的发布者选择权与透明度原则。在选择 Disallow AI Training 设置时，它们仍然可以继续爬取您的网站以用于搜索。选择 Block 将完全阻止它们。

我们还将来自 Amazon、Anthropic、Meta 和 OpenAI 的相关爬虫归类为 Accountable。这些组织将其搜索和训练爬虫分开，因此 Cloudflare 可以阻止训练爬虫而不影响搜索。

### Applebot

Applebot 允许网站所有者通过在 robots.txt 中添加针对 “Applebot-Extended” 的 Disallow 规则来选择退出训练。站点所有者目前还可以通过他们的页面 HTML 中的 nosnippet [ 指令](https://support.apple.com/en-us/119829#:~:text=nosnippet%3A%20Applebot,products%20and%20services.)来表达对 AI 摘要的偏好。内容还可以标记为[付费墙内容](https://support.apple.com/en-us/119829#:~:text=Marking%20paywalled%20content,the%20next%20section.)，以将其排除在生成式输出之外。Applebot 尚未提供用于 URL 级别检查的工具。然而，我们已经与他们的团队会面；他们分享了其为明年推进的解决方案的细节。Apple 还表示，禁止训练[不会影响搜索排名](https://support.apple.com/en-us/119829#:~:text=Applebot%2DExtended%20and%20controlling%20data%20usage)。

### Googlebot

Googlebot 允许网站所有者通过在 robots.txt 中为 “Google-Extended” 添加 Disallow 规则来选择退出训练，并在其网站管理员门户中提供一个切换按钮，以便将网站内容排除在生成式搜索结果以外。Googlebot 还为网站所有者提供关于搜索结果和 AI 摘要结果的指标和报告。Google 已分享其现有以及最近推出的控制项信息，以及他们正在推进的工作内容，包括：为与 Google-Extended 相关的网站所有者提供额外的 URL 级透明度工具；Google 预计将在未来几周内上线这些工具。Google 还指出，不允许 Google-Extended [不会影响搜索排名](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers#google-extended:~:text=Google%2DExtended%20does%20not%20impact%20a%20site%27s%20inclusion%20in%20Google%20Search%20nor%20is%20it%20used%20as%20a%20ranking%20signal%20in%20Google%20Search.)。

### Bingbot

Bingbot 在其 [Webmaster Tools](https://www.bing.com/webmasters/help/ai-performance-9f8e7d6c) 中提供精细控制和透明度。网站所有者目前可以通过 Bing 的 `NOARCHIVE` [元标记](https://blogs.bing.com/webmaster/september-2023/Announcing-new-options-for-webmasters-to-control-usage-of-their-content-in-Bing-Chat#:~:text=Content%20tagged%20NOARCHIVE%20will%20not%20be%20included%20in%20Bing%20Chat%20answers%2C%20not%20be%20linked%20to%20in%20the%20answers.%20Going%20forward%2C%20for%20content%20in%20our%20Bing%20Index%20that%20is%20labeled%20NOARCHIVE%2C%20we%20will%20not%20use%20the%20content%20for%20training%20Microsoft%E2%80%99s%20generative%20AI%20foundation%20models.) 表达 AI 训练偏好。Microsoft 正在扩展这些功能，并正在构建机制以支持在域/站点级别的 robots.txt 中的“不训练”偏好，目标是在 2027 年初完成。对于希望今天退出 Bing 训练的 Cloudflare 客户，网站所有者除了使用 `NOARCHIVE` 标签外，还可以使用 [Block URLs 或内容移除工具](https://www.bing.com/webmasters/help/block-urls-from-bing-264e560a)。Microsoft 还表示，使用 `NOARCHIVE` [不会影响搜索排名](https://blogs.bing.com/webmaster/september-2023/Announcing-new-options-for-webmasters-to-control-usage-of-their-content-in-Bing-Chat#:~:text=We%20also%20heard%20from%20publishers%20that%20they%20want%20to%20exercise%20these%20choices%20without%20impacting%20how%20Bing%20users%20can%20discover%20web%20content%20on%20Bing%E2%80%99s%20search%20results%20page.%20We%20can%20assure%20publishers%20that%20content%20with%20the%20NOCACHE%20tag%20or%20NOARCHIVE%20tag%20will%20still%20appear%20in%20our%20search%20results.)。

以上支持推出之前，选择 Disallow AI Training 将不会通过 robots.txt 自动传达 no-training 偏好至 Bing。这与之前的训练 Block 设置具有相同的实际行为，但不适用于混合用途爬虫，如 Bingbot。

### 持续推进中

随着这些能力不断演进，我们将继续与所有 AI 爬虫的运营商进行沟通并开展协作。Cloudflare [Radar](https://radar.cloudflare.com/ai-insights#ai-bot-transparency) 公开页面跟踪 Accountable 爬虫运营商提供的控制项、透明度以及报告内容。 

让互联网变得更好，需要双方都拥有能动性：爬虫需要访问开放网络，而创建这些网络内容的人也需要对其作品如何被使用拥有切实有效的控制。今天的公告体现了在这一平衡上取得的实质性进展。

向前推进需要基础设施供应商、内容创作者、科技公司以及像 Internet Engineering Task Force (IETF) 这样的标准组织共同协作，把这些原则转化为开放、可互操作的标准。

## 预告：AI Summaries

训练和 AI 摘要给网站所有者提出了不同的问题。训练涉及内容是否可用于构建 AI 模型。摘要影响人们如何发现、评估并最终访问企业网站。两者都很重要，但它们对企业的影响方式不同。

选择不参与 AI 摘要的控制措施是第一步。被认定为 Accountable 的运营商已经提供或正完成相关工作来实现该能力，并建立了重要的基线：网站所有者可以选择拒绝。

不过，整站范围允许或禁止 AI 摘要的二元选择的工具仍然过于粗略。正确的决定取决于网站、内容以及业务结果。对发布方来说，训练提出了有关控制、补偿与原创内容可持续性等基础性问题。AI 摘要引出一个独立且往往更直接的分发问题：人们访问发布方的站点，还是会在搜索或 AI 体验中直接获取答案？对于许多其他企业而言，AI 摘要越来越多地成为潜在客户与网站之间的中间环节。它们可回答问题、比较替代方案、推荐产品，或者帮助某人决定是否访问。

数据表现出混合影响。[超过一半](https://www.pewresearch.org/chart/a-majority-of-americans-say-they-read-ai-summaries-at-the-top-of-search-results/)的消费者会在搜索中阅读摘要，而且这些消费者在阅读后[结束搜索](https://www.bain.com/insights/goodbye-clicks-hello-ai-zero-click-search-redefines-marketing/)[可能性高出 40% 以上](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/)。这会减少网站的访问量。但由 AI 搜索推荐的消费者转化率是传统搜索推荐消费者的[三倍](https://aisearch.similarweb.com/blog/ai-visibility-roi/)到[五倍以上](https://quickseo.ai/blog/ai-search-vs-google-search-in-2026-40-stats-that-show-why-your-brand-needs-to-track-both#:~:text=AI%20search%20traffic%20converts%20at%2014.2%25%2C%20compared%20to%20Google%E2%80%99s%202.8%25)。AI 可能减少访问次数，但会带来意向更明确的客户。

这并不是本质上的好或坏。由广告资助的发布方可能会优化受众数量。零售商可能更倾向于更少但更有可能购买的访客。Cloudflare 的作用不是替他们做选择，而是提供做出明智决策所需的可见性和控制。

退出 AI 摘要是一个良好的开端，但并不是最终状态。我们的下一个重点是帮助网站所有者了解摘要如何影响他们的业务，并让他们更好地掌控内容可被使用的范围与程度。诸如 [ai-prefs](https://datatracker.ietf.org/wg/aipref/documents/) 之类的开放标准将是实现这一目标的重要组成部分。

如果您希望参与此对话或提供反馈，请联系 [crawlercontrols@cloudflare.com](mailto:crawlercontrols@cloudflare.com)。

这些新控制措施适用于所有客户和所有计划，并可以在域（区域）[安全设置](https://dash.cloudflare.com/?to=/:account/:zone/security/settings)中进行配置。尚未使用 Cloudflare？[免费开始使用](https://www.cloudflare.com/lp/pg-one-platform/)，即可配置您所需的流量控制策略。

]]>01M360R0YZYEQKKVYN7MHSMSRM借助 Cloudflare Managed Defense 与 OpenAI Daybreak 模型，实现情境感知漏洞发现与修复https://blog.cloudflare.com/zh-cn/vulnerability-discovery-remediation/ Tue, 15 Sep 2026 02:21:44 GMT利用生产环境流量与安全信号对发现结果进行优先排序，在条件允许时准备边缘缓解措施，并提出代码补丁。通过将 WAF 数据与 OpenAI Daybreak 模型相结合，Vulnerability Discovery and Remediation 帮助团队优先识别并修复最关键的威胁。Artificial IntelligenceWorkers产品新闻安全开发人员您的扫描器刚刚标记出 4,000 个新漏洞，其中 78 个为严重等级。您会先修复哪一个？

为了回答这个问题，Cloudflare 宣布推出 Vulnerability Discovery and Remediation 抢先体验版，该功能现已纳入 [Cloudflare Managed Defense](https://www.cloudflare.com/managed-defense/)。Vulnerability Discovery and Remediation 是一项仅限受邀的全新 Cloudflare 服务，帮助客户检测并修复其代码库中的漏洞。

通过 OpenAI [Daybreak Defense Network](https://openai.com/index/putting-frontier-cyber-models-in-more-trusted-hands/)，我们使用 OpenAI Daybreak 模型（包括 GPT-5.6 Cyber），针对您授权我们访问的代码库开展侦察、探测和验证工作。一旦检测到漏洞，我们将向您提出解决方案，在将每个补丁建议及随附的缓解方案提交审查之前，自动对其进行检验。重要的是，您始终掌握主动权：我们可能会提出代码补丁和其他缓解措施，但是否实施由您决定。

确定修复优先顺序历来是一大难题，如今更是愈发困难。大型语言模型现在可以在[数分钟内](https://openai.com/index/the-defenders-window/)扫描整个代码库中的弱点，这意味着发现的问题数量持续攀升。但真正的问题在于速度。攻击者可以借助 AI 加速漏洞发现和利用的部分环节，留给安全团队和开发者判断优先级、采取行动的时间越来越少。

设想一下：您的扫描器告诉您某个处理程序存在漏洞，却没有告诉您该代码是否已部署、是否有人真正访问过该路由、周边存在哪些安全活动，或者您已有哪些防护措施。您必须在没有生产环境暴露证据、也不了解现有防护的情况下对该发现进行优先排序。

这正是我们能够提供帮助的地方。凭借我们的全球网络，我们可以看到哪些路由处于活跃状态、承载多少流量，以及周边发生了哪些安全事件。当客户在启用 Vulnerability Discovery and Remediation 的同时启用 Web Application Firewall (WAF)，我们还能看到已应用了哪些规则，以及哪些规则正在主动拦截攻击。这些情境将一个通用发现转化为具体的优先级判断：该漏洞存在于正在运行的代码中、位于高流量路由上、近期有攻击活动且尚无现有防护。我们还可以通过提出量身定制的自定义 WAF 缓解措施和代码补丁，帮助您修复该漏洞。

如果这听起来似曾相识，那是有原因的。在[《构建您自己的漏洞检测框架》](https://blog.cloudflare.com/build-your-own-vulnerability-harness/)一文中，我们描述了一套与模型无关的流水线，用于扫描 Cloudflare 整个系统、对每个发现进行对抗性验证，并将原始模型输出转化为工程师可信赖的修复方案。该内部系统是 Vulnerability Discovery and Remediation 的核心支柱之一。漏洞检测框架使我们能够在系统规模上发现漏洞；Vulnerability Discovery and Remediation 则将这一发现流程延伸至客户授权我们审查的代码，并将发现结果与生产环境流量、安全事件以及能够对其采取行动的边缘控制手段相关联。

下图概述了我们的流程，我们将在下文中进行详细说明。

## **为漏洞检测框架添加情境**

我们的解决方案适用于 Cloudflare Workers 和被代理的应用程序。漏洞检测流程从收集 [Web Assets](https://developers.cloudflare.com/security/web-assets/) 和 [WAF](https://www.cloudflare.com/products/waf/) 的流量与安全数据快照开始。该快照显示哪些路由处于活跃状态、它们接收多少流量，以及是否有近期安全事件与其关联。例如，某个呈现大量[检测触发](https://blog.cloudflare.com/attack-signature-detection/)的路径，也可能出于安全情境目的被认定为关键路径。Web Assets 和 WAF 本身分别是 Vulnerability Discovery and Remediation 的第一和第二支柱。

接下来，我们使用源代码漏洞分析来识别代码中的潜在弱点。但该分析无法显示哪些路由能够访问它、这些路由承载多少流量、是否收到可疑请求，或哪些防护措施已经生效。我们将承载大量请求的路由视为热门路径，部署到这些路由的源代码将接受更严格的安全剖析。综合这些信号，可以提供关于 API 使用方式以及漏洞可能暴露位置的证据。

对于 Workers，我们检索 Worker 的最新源代码版本及其已配置的路由，以识别该 Worker 所服务的端点。接下来，我们将 Worker 的路由与 Web Assets 进行匹配，并从 [Workers Observability](https://developers.cloudflare.com/workers/observability/) 获取请求元数据，将审查中的确切源代码与其在生产环境中处理的端点关联起来。收集到的网络情境在整个调查过程中始终可用，允许代理在需要时随时调取。

随后，漏洞检测框架启动运行。它首先使用侦察代理将请求路径映射到代码库中处理这些路径的具体部分。侦察代理利用该映射关系，将探测代理派入客户授权代码的特定区段，让它们搜寻漏洞，并在需要时调取相关网络情境。这些情境可以帮助探测代理更多关注活跃路由或近期被攻击路由背后的代码，但并不能直接证明漏洞的存在。每一个漏洞发现都必须有源代码中的证据加以佐证。

探测代理返回其发现结果后，验证阶段会先检查拟议的缓解措施，然后再根据源代码为每个漏洞分配初始风险评级。如果我们收集的网络证据显示受影响的端点承载了大量流量或呈现出遭受主动探测的迹象，则漏洞风险评级可能会进一步提高。

最终生成一份按优先级排列的发现清单，每项发现都附有推荐的代码补丁，以及在证据支持时提出的 Cloudflare WAF 自定义规则，可在代码修复方案审查期间降低暴露风险。如果您已授权我们的 VDR 为您的区域提供防护，我们将部署这些规则，并围绕到达漏洞代码所需的方法、路径及其他请求细节进行保守范围界定。如果某个路由模式仅包含变量和通配符，我们将不建议任何规则。我们宁可错过一个可能的关联，也不愿声称证据无法支持的结论。

上述 HTTP 方法覆盖绕过示例展示了这些信号如何协同发挥作用。漏洞检测框架将源代码发现映射到生产路由，利用流量和安全活动对其进行优先排序，并将提议的 WAF 规则范围界定在能够访问漏洞代码的请求上。该规则可在工程团队审查并发布代码补丁期间降低暴露风险。

## **模型在哪里运行**

如果您授权启动调查，Vulnerability Discovery and Remediation 会在 Cloudflare 平台上运行漏洞检测框架，并通过 Cloudflare AI Gateway 将模型提示词从 Workers 发送至 OpenAI 服务器上的 OpenAI Daybreak 模型。在侦察、探测和验证阶段会使用 GPT-5.6 Cyber 模型，模型的响应会返回给框架，以便在 Cloudflare 上继续运行工作流。不在 Cloudflare 边缘节点运行模型推理，模型也无法擅自应用其提出的任何补丁或规则。

我们通过将调查范围限定在客户授权的源代码和证据范围内，确保每次调查保持精准边界。在这些情境传递给模型之前，Vulnerability Discovery and Remediation 会移除调查不需要的内容，并应用为本次合作配置的脱敏控制措施。漏洞检测框架将源代码、日志和请求元数据视为待审查的证据，而非待执行的指令。

工具访问权限遵循相同的边界原则：每次调用在执行前均会被记录并与调查的访问策略进行核对，每项补丁或规则提案都必须通过在模型外部实施的检验。如果其中一项检验失败，工作流将在提案提交客户审核之前停止。

在通过检验并经我们团队验证输出结果之前，不会有任何内容提交审核。对于边缘防御建议，这意味着要验证规则语法，并针对代表预期请求的合成测试用例运行规则，而非针对客户的真实流量。如果某项检验失败或结果仍存在歧义，我们将保留该输出并转交诊断处理。

通过这些检验并不意味着会改变您的环境。经我们团队验证后，Vulnerability Discovery and Remediation 才会准备源代码补丁和 WAF 规则。

## **加入抢先体验**

Vulnerability Discovery and Remediation 在抢先体验期间通过我们的 Managed Defense 团队向部分经遴选的客户发出邀请。每次合作从一个应用程序开始，其代码库须由客户授权我们进行调查。为将发现结果与生产环境关联，Vulnerability Discovery and Remediation 使用经授权的只读访问权限，访问 Web Assets 运营资产清单、相关 WAF 控制措施，以及（在可用情况下的）Workers Trace Events Logpush 日志推送数据。调查为半自动化流程，但每项结果均需要由您审核，然后决定是否进行测试或部署变更。

如有兴趣进一步了解，请联系您的 Cloudflare 客户团队。

]]>01M2HDP414XB2E6STHAFM0EJEKAdaptive Intelligence 简介：颠覆每一次机器人攻击的成本逻辑https://blog.cloudflare.com/zh-cn/introducing-adaptive-intelligence/ Tue, 15 Sep 2026 02:08:26 GMT机器人运营者历来在经济上占据优势，他们借助廉价代理绕过静态确定性检测规则，并不断更换工具。Cloudflare 全新的自适应智能引擎通过自主学习实时流量的元信号并部署一次性规则，彻底扭转了这一局面，使自动化攻击的成本高到难以为继。Bot ManagementMachine Learning产品新闻应用程序安全现代机器人威胁越来越多地由意志坚定、手段高超的攻击者驱动。往往不是单个个体，而是一个相互交流技术的团体，或是一项向任何愿意付费者开放的商业服务。对其中许多人而言，突破机器人检测本身就是一份他们乐在其中的全职工作。阻断他们，他们就会立即着手寻找新的绕过方式。AI 的普及进一步降低了攻击门槛，让攻击者更轻松地搭建复杂的攻击配置，降低了攻击的运营成本。

这种转变使防御方处于经济上的劣势。响应和适应新攻击需要审慎、取证和付出，以确保封堵攻击者的努力不会波及正常用户。攻击者则没有这些顾虑，他们的限制主要来自时间成本、代理池规模，以及如何防止基础设施提供商关停其账户。

他们的优势在于适应的成本。攻击者可以随时、持续地调整策略，而大多数防御措施是以离散、受控的版本发布方式部署的。Cloudflare 每天分析逾一万亿次请求，寻找自动化滥用的迹象，因此我们清楚地看到攻击者的战术变换有多快。响应能力上的差距正在不断扩大。

残酷的现实：业界的机器人检测往往建立在一个侥幸的假设之上——只要把墙垒得足够高，攻击者就会望而却步。现实中，意志坚定的攻击者总会找到突破口。**问题不在于他们能否突破，而在于突破之后会发生什么** 。

今天，我们正式推出 Adaptive Intelligence，这是一款全新的机器人检测引擎，出发点截然相反。它不是押注于一堵将所有攻击者拒之门外的高墙，而是让突破本身变得如此缓慢、代价如此高昂，使攻击失去继续运行的价值。

我们相信，业界尚无其他机器人检测系统以这种方式运作。

### **一个攻击者，多副面孔**

并非所有攻击都显而易见。最复杂的攻击，恰恰是专门为了消融进普通流量而设计的。

攻击者可以将请求分散到大规模住宅代理网络中，将每个地址的请求频率压得很低，耐心地在登录、结账或账户恢复流程中逐步推进。每个请求来自不同的地址，通常配备全新的 User Agent 或新的机器人指纹，看起来都像一位新访客。没有任何单一来源会触碰速率限制。

这正是这种模式难以遏制的原因。阈值收得太紧，真实用户就会被拒之门外——而这恰恰是您最不愿发生的结果。攻击就潜伏在两次请求之间的空隙，孤立地审视每一个请求的防御体系，永远无法察觉它的存在。

### **确定性检测的缺陷**

基于规则的系统的问题在于，它给攻击者提供了一个静止的靶子。攻击者在数天内就能迭代，而模型要等上数月才能完成下一次更新——等到追上之时，工具链早已演进。

机器人检测的传统做法，一直是针对新的攻击手法编写规则加以应对。这种方法有效，直到攻击者研究了信号、学会了规避方法，并迫使防御方再写一条新规则。最高级的攻击者甚至开发出工具，将这一过程半自动化。防御方看似永远处于被动。

这种检测方法属于“确定性”检测，即相同的输入始终产生相同的输出。一个从不改变的防御体系，实际上是在教攻击者如何击败它，并间接推动机器人操纵者构建更强大的自动化攻击工具。面对确定性防御，自动化探测会返回明确的“是”或“否”结果，经过足够多次的尝试后，这些反馈让攻击者可以精准地掌握系统的防御边界。这种态势使攻击者在经济效益上占据了优势。

## **扭转攻击的经济逻辑**

Adaptive Intelligence 的目标，正是逆转这一经济逻辑，将主动权还给防御方。

持续变化的防御能够扭转这一计算，但前提是两个条件同时成立：第一，防御方的响应成本必须低于攻击者的绕过成本；第二，攻击者必须被剥夺赖以适应的反馈，使其无法简单地"学习"回来。两者兼备，攻击者自身的循环就会反噬自己：所有学到的东西都失去了效力，每一次新的尝试代价都比上一次更高，直到攻击不再值得运行。

其中一部分在于让攻击者减少学习的机会。Adaptive Intelligence 可以从一个信号中识别出机器人，但不会对此产生明显反应，因此攻击者会继续依赖一个他们并不知道我们已能看穿的破绽。同时，它将检测视为统计判断而非固定规则，使其具有不确定性——它同时权衡多个信号，攻击者无法孤立出任何单一的逻辑加以击破。

## **全新检测引擎**

机器人评分数源于多种检测方法的协同作用：机器学习、行为验证、JavaScript 指纹识别、启发式规则库，以及识别搜索爬网程序等已知且已验证的机器人的检查。

Adaptive Intelligence 是一个全新的机器人检测引擎，运行于机器人分数之后。其他所有系统的设计目标是通过累积规则将攻击者拒之门外，而 Adaptive Intelligence 的设计前提是攻击者终将进入，并使这一尝试的代价尽可能高昂。

下文将介绍Adaptive Intelligence 检测引擎的三个组件，这些组件与传统模型截然不同：自我改进、生成一次性规则，以及**从所保护流量中学习** 。今天正式上线的是第一个组件：机器人分数背后的机器学习，现在以持续重训练取代固定版本发布。它汇聚 Cloudflare 全网的网络信号，评估每个请求发生自动化滥用的概率。固定模型原地不动，Adaptive Intelligence 则持续演进。第二和第三个组件将随后推出。

### 1\. **自我改进**

引擎在实时流量上持续重训练。随着新的绕过工具和机器人框架出现，它从中学习，将这些知识融入机器人分数背后的模型，无需等待计划发布。本周出现的技术，本周即可被引擎识别。您已经建立在其上的分数，始终贴近攻击者的实际行动，而非在两次更新之间与现实渐行渐远。

### 2\. **生成一次性规则**

一次性规则，是一种我们预料攻击者会适应的规则，但这种适应并不会使攻击者的机器人因此变得更强。Adaptive Intelligence 被设计为针对特定攻击创建一次性规则，在随机时间间隔内部署和撤销，绝不将它们保留到足以成为固定靶子的程度。由于这些规则不断出现又消失，它们向攻击者赖以对抗我们的训练信号中注入了噪声，使攻击者无法获得静态防御所泄露的稳定"是"或"否"。没有任何单条规则必须完美无缺或无懈可击。它只需持续足够长的时间完成自己的使命，然后为下一条让路。当攻击者逆向工程出某个特定模式时，引擎早已前进，令其工程努力付诸东流。

### 3\. **从所保护流量中学习**

Adaptive Intelligence 还将从跨数百万站点看到的模式中学习。当客户标记出一个我们误判的真实访客，或我们自身的测量发现漏洞时，该修正就会成为训练信号。随着时间推移，引擎将调校到 Cloudflare 客户实际面临的问题，使您获得的保护反映当前的威胁态势，而非某个过时快照。

## **工作原理**

Adaptive Intelligence以“**观测、训练、部署、验证** ”的循环方式运行。随着我们将更多网络资源接入该系统，它利用的信号范围也不断扩展。

**观测** 。引擎汇聚 Cloudflare 网络信号，例如 JA4 TLS 指纹、请求结构、质询结果、会话行为、网络信誉，以及更高层次的元信号，同时结合来自 Turnstile 和 Precursor 的客户端遥测数据。在单个请求上看起来平平无奇，却在整个会话中表现出脚本行为模式的客户端，会被其跨时间的行为所暴露——即便每个请求单独看来都合法。| **训练** 。我们在实时流量上持续重训练 ML 系统，包括野外出现的最新绕过工具和机器人框架。训练集频繁刷新，使系统能够对新型攻击技术做出更快响应。  
  
---|---  
**部署** 。新的模型权重自动在全网推出，无需选择版本，无需安排升级，一旦接入便无需任何操作。为您流量评分的模型，反映的是我们当下正在观察的威胁。| **验证** 。在新版本成为您的主要防线之前，它会以影子模式与当前版本并行运行，对实时流量评分而不影响任何访客。我们比对两者，观察质询通过率等信号。若新版本会对真实用户产生更差的评分，则不予上线。  
  
Cloudflare 多年来一直针对 DDoS 攻击运行这种自动化循环：采样流量、对攻击背后的模式进行 TLS 指纹识别、将防护措施推送至全网，并持续测量以便随流量变化进行调整或撤销。机器人是该问题的更难版本，因为信号更为微弱，故事只会随时间推移才浮现。任何单一信号单独看来都可能完全正常。是信号之间的关联，以及它们相互映衬的上下文，才揭示出隐藏于正常流量中的机器人。

Adaptive Intelligence 同时在多个时间窗口内评估流量。短窗口在突发流量发展之时即时捕捉。长窗口揭示跨越数千个地址、客户端和会话——这些来源之间本无理由表现相似——重复出现的行为模式，并将这些分散的请求归因到单一来源。同一引擎，既能发现明显的抓取流量峰值，也能浮现出缓慢的、分布式的撞库攻击——后者从每个地址只发送寥寥几个请求。

### **自动构建新检测**

随着 Adaptive Intelligence 的后续组件上线，挖掘系统将在近期已标注的流量中搜索能够将新兴攻击与真实用户区分开来的信号组合。

有用的检测往往来自我们已知信号之间的关联，而非一个从未见过的全新信号。客户端可能声称自己是某种浏览器，却产生另一种浏览器的网络或 JavaScript 信号。一个请求单独看来可能正常，但与会话中其他请求放在一起却形成奇异的序列。自动化挖掘让我们能够测试这些组合的众多变体，并将最强有力的候选项转化为检测方案。

这些候选检测刻意设计得很窄。它们不需要捕获互联网上所有的机器人，甚至不需要捕获当前攻击中的每一个请求。这使它们能够快速构建，并在攻击改变战术时易于替换。

### **它具备记忆功能**

攻击者不只攻击一次。他们会暂停、更换工具，然后卷土重来。停用某项检测，并不意味着遗忘它背后的模式。即使针对某次攻击的检测已停止触发，引擎仍会保留过去攻击的记忆；因此，攻击者无法仅靠在两个配置文件之间切换、寄希望于第二个看起来是新面孔的配置文件来逃避检测。

这种记忆让系统在熟悉的攻击回归，或相关攻击出现时获得先机。一个检测可以在不再发挥作用时过期，而其背后的证据仍可用于构建下一个检测。生产环境中不会积累陈旧规则，系统也永远不必从头学习一个老旧的攻击。

结果是一个自动化的循环，既能响应明显的峰值，也能悄然收集针对一次耐心、分布式攻击的证据——后者始终游走在传统阈值之下。

### **安全部署**

持续变化只有在每一次变化都安全的前提下才真正有价值，而标准很高。客户可以接受偶尔漏过一个机器人，但一个真实访客被错误拒绝才是真正造成损失的失败。正是这种担忧使团队对自动更新保持谨慎，因此新检测必须在影响任何人之前证明自己的价值。

我们针对近期真实流量对每个候选检测进行测试，衡量它能捕获多少已知自动化流量，以及它会以多高的频率误判真实访客。它以对机器人分数的输入身份逐步推出，期间我们持续观察分数分布、质询结果和客户反馈，并能在影响到您的整个网络之前暂停或回滚。每一次更新都必须证明自身至少与所替换的版本一样出色——以对这类系统真正重要的指标衡量，包括精确率和召回率。

## **一个愿景：Adaptive Intelligence 与 Precursor**

这个引擎并非单独运作。上个月我们推出了 [Precursor](https://blog.cloudflare.com/introducing-precursor/)——一款为 Bot Management 打造的、以隐私为先的持续行为验证引擎，它根据访客到达浏览器后的行为表现来衡量自动化滥用：时序、动作，以及自动化难以伪造的细微人类信号。Precursor 与 Adaptive Intelligence 作为同一理念的两个组成部分而构建，共同检测恶意自动化。Precursor 通过持续的会话行为测量实现这一目标；Adaptive Intelligence 则从整个网络的机器人检测信号中学习，而一方的信号使另一方更难被欺骗。

这也反映了我们思考这一问题的方式：机器人检测引擎应当减少漏网之鱼，并持续比对面的攻击者更快地适应。

## **后续展望**

持续重训练是基础，引擎的更多组件将从这里逐步上线。我们正在扩展针对机器人的自动检测生成，将 Cloudflare 在网络、质询和浏览器层面看到的信息整合为对会话的单一视图，并为您提供更多基于引擎发现采取行动的方式。

清楚地认识到没有任何防御能够将每一个意志坚定的攻击者拒之门外，让我们得以瞄准更实用的目标：让每一次攻击都难以持续，同时让攻击者付出远超回报的代价。Adaptive Intelligence 对新技术的响应速度更快，并在每次变化时给攻击者留下更少可供学习的内容。那个从不放弃的攻击者，如今面对的是一道每次归来都面目全非的防线——他们的坚持，将不再有所回报。

## **立即开始**

企业客户应在 [Bot Management 仪表板](https://dash.cloudflare.com/?to=/:account/:zone/security/settings?tabs=bot-traffic)中开启"Auto Update Machine Learning"。开启后，您将自动获得 Adaptive Intelligence，无需迁移版本，无需任何配置，您已经建立在其上的机器人分数将继续正常运行。如果您不确定是否已启用，请立即检查，确保从第一天起即受到保护。

]]>01M2HCWMCD6ZQ58RTP8NWG5383只需声明一次，始终保持一致：隆重推出 Bot Preference Synchttps://blog.cloudflare.com/zh-cn/bot-preference-sync/ Wed, 09 Sep 2026 03:26:19 GMTCloudflare 全新的 Bot Preference Sync 可自动将您的 robots.txt 文件与适用于搜索、Agent 和训练的 AI 自动程序策略保持同步。轻松管理哪些自动程序可访问您的内容，无需维护静态文件。AI 机器人Bot Management产品新闻机器人网络服务我们始终致力于满足客户的多样化需求。有些客户希望优化内容发现，另一些客户则希望以最严格的安全策略保护内容。在这些不同策略中，有多种方法可以缓解机器人流量： 有些机制仅声明您的意愿，默认爬网程序出于善意；另一些则通过 Bot Management 解决方案直接阻止，从根本上锁定内容访问。

我们深知，在网站上维护多重防护层十分繁琐。例如，可能出现这样的情况：您的 robots.txt 声明某个爬网程序被禁止访问您的网站，但实际的执行规则并未将其阻止。当您声明的意愿与实际执行的规则相悖时，部分爬网程序可能将此视为无视您意愿或绕过规则的依据。

几年前，Cloudflare 推出了一种更便捷的方式，允许网站所有者禁止 AI 训练抓取，同时兼顾两个防护层：一个受管理的 robots.txt 值，明确告知固定名单中的主要训练类爬网程序不得抓取您的内容进行训练；以及针对训练类爬网程序的边缘执行阻止。2026 年 7 月 1 日，我们进一步推出了更灵活的选项，让您能够分别管理搜索、代理及训练类 AI 流量的访问策略。

今天，我们正式宣布推出 **Bot Preference Sync** ，面向从免费计划到企业计划的 _所有_ 客户开放。Bot Preference Sync 能够根据您在 AI 机器人配置中的设置，自动更新 robots.txt 中的对应偏好，并可随时开启或关闭。不再为单一用例维护静态文件：我们将帮助您**定制 robots.txt 文件，反映您针对不同 AI 机器人类别所做的配置** 。

## **互联网面临的新议题**

多年来，这一领域最迫切的问题始终是："我的内容是否在未经许可的情况下被用于训练 AI 模型？"这是一个重要问题，且不会消失。与此同时，我们越来越多地听到关于可发现性与用户互动的议题：当有人向 AI 助手提问而我的网站能够解答时，我该如何出现在搜索结果中？有多少流量来自 AI 爬网程序，有多少流量来自真实用户？哪些内容真正带来了引荐流量，其价值几何？

答案因商业模式而异。可发现性与用户互动是所有希望在现代网络中立足的企业的核心关切，但其转化路径各异：电商网站可能希望所有内容都被抓取并用于训练，以便当购物者向聊天机器人询问"小户型最佳沙发"时，其产品能够出现在推荐结果中。而依靠广告变现的媒体发布商则可能恰恰相反：希望保留在能为页面带来读者的搜索索引中，同时让文章内容远离模型训练——并且至关重要的是，能够核实其内容确实未被未经授权地使用。

关键在于，没有唯一正确答案。您的管控策略应当反映您的业务战略，这也是我们一直致力于为您提供全链路可见性与选择权的原因。Bot Preference Sync 将这些层面融为一体，让您 _设置_ 的偏好就是您 _对外发布_ 的偏好。

## **透明度的呼声**

2026 年 7 月 1 日，我们提出：混合用途爬网程序——即“以单一用户代理身份，混合执行搜索、智能体使用和训练任务的机器人”——使网站所有者处于不利地位，因为这让用户难以区分自己想要什么和不想要什么。这一判断至今未变，我们对网站所有者透明度的立场也未曾动摇。

但实现透明度的方式不止一种。我们希望奖励那些明确声明身份和数据使用方式的运营商。为了进行机器人[验证](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/)，**同时执行搜索和训练的机器人所有者需要提供额外信息** ，以免在启用“禁止训练”时遭到屏蔽。具体要求如下：

  * 机器人必须通过某种机制，遵守 robots.txt 中的"禁止训练"偏好
  * 为网站所有者提供退出 AI 摘要的方式
  * 提供哪些页面被用于训练的 URL 级别可见性，以及搜索结果的相关指标，让网站所有者能够了解其内容在搜索和训练中的使用情况
  * 能够公开证明：禁止训练不会损害其传统搜索结果排名



Cloudflare Radar 的[ AI 机器人透明度](https://radar.cloudflare.com/ai-insights#ai-bot-transparency)部分公开追踪符合上述标准的主流 AI 模型及服务提供商的机器人，其中包括遵循最佳实践的示例以及违反最佳实践的示例。未能提供透明度的爬网程序将不会获得"善意推定"——在您禁止训练时，它们仍将被阻止。换言之，这是将透明度作为准入门槛的一种方式。

## **Bot Preference Sync 详解**

Bot Preference Sync 是一项新功能，能够让您的 robots.txt 始终与您在 Cloudflare 区域级别仪表板中为搜索、代理和训练类 AI 机器人所做的偏好设置保持同步。如果网站所有者已有 robots.txt 文件，Bot Preference Sync 添加的内容将 _附加到_ 现有内容之前，原有的任何禁止指令均予以保留。

网站所有者无需再单独维护静态文件——Cloudflare 将根据您的配置生成或更新 robots.txt，使您向外界声明的内容与边缘执行的策略始终保持一致。

对于搜索和代理，我们在 7 月 1 日宣布的三个选项依然有效：允许、仅在投放广告的页面上阻止，或全站阻止。对于**训练** ，我们进一步细化了阻止内容被用于模型训练的选项，推出禁止选项：

**禁止** ：在 robots.txt 中写入“禁止训练”偏好，使采取额外透明度措施的合规混合用途爬网程序仍可访问您的内容用于搜索索引——因为这些爬网程序允许网站所有者直接核实其数据的使用方式。合规爬网程序将遵守 robots.txt 中的偏好，您在合规爬网程序中的搜索可见性不受影响。

以下面的示例为例：某网站所有者将 AI 机器人策略配置为"允许搜索、允许代理、禁止训练"。

由于该示例网站已开启 Bot Preference Sync，其 robots.txt 将在开头附加类似如下内容（为示例起见，已做简化和匿名处理）：

我们将利用[ BotBase](https://developers.cloudflare.com/bots/botbase/) 中追踪的机器人，定期更新当您选择阻止或禁止某类别时添加到 robots.txt 中的机器人列表。分类为搜索、智能体和训练的已验证机器人，可随时在我们的[公开机器人目录](https://radar.cloudflare.com/bots/directory)中查看。

对于所有新客户，Bot Preference Sync 将 _默认开启_ ，以便更轻松地管理体现同一策略的阻止设置和偏好设置。对于正在使用旧版受管理 robots.txt 功能的现有客户，我们将在 Bot Preference Sync 正式上线时提示您审查并确认偏好，以完成迁移。

部分客户可能希望或需要对偏好声明进行更精细的控制，例如希望为特定公司设置例外。由于 Bot Preference Sync 的设计目的是处理 _按类别_ 制定的策略决策，而非逐条处理含复杂逻辑的自定义规则，因此它不会直接读取个别自定义规则。偏好设置更精细的客户，始终可以选择关闭用于设置组级别策略的同步功能，并自行定制 robots.txt 文件以匹配其自定义策略。

我们还针对发布商或依赖广告的网站进行了调整，为其提供与其他网站所有者不同的默认设置。我们为依赖广告变现、并希望广告位保留给真实访客的发布类网站创建了一个默认选项。此类客户在接入时可选择"我通过该域名上页面的广告进行变现"，系统将自动将训练设置默认为禁止。（客户可随时更改此设置。）这样，您既能保留在搜索结果中的露出，又能让内容远离模型训练。

对于非发布商客户，新客户在接入域名时， _默认不会_ 添加任何阻止或禁止：选择权在您。您可以随时选择阻止搜索、智能体或训练流量，但初始状态不会代您添加任何阻止设置。

## **下一步计划**

Bot Preference Sync 将在未来一周内向 _所有_ 客户、所有计划开放。请关注我们的 Changelog 了解具体上线时间并留意仪表板（及收件箱）中的提示，以确认您的偏好设置！ 

这只是一项长期工作的开端。我们将继续与大型机器人运营商合作，确保在应对现有挑战（例如未经同意的训练抓取）和新兴议题（例如可发现性与用户互动）时不做妥协。所有这些努力的最终目标，是促进网站所有者提高透明度与增加掌控权。

]]>01M2230E7G49XKPQS3X28M5ZSK从全有或全无到基于任务的 OAuth 授权https://blog.cloudflare.com/zh-cn/task-based-oauth-consent/ Wed, 09 Sep 2026 03:12:46 GMTCloudflare OAuth 现已支持可选范围，让用户对应用程序的访问权限拥有更多控制权，同时帮助开发者围绕具体任务构建安全的授权流程。APIInternship ExperienceOAuth产品新闻开发人员开发人员平台智能体身份自六月以来，开发人员已在 Cloudflare 上创建了数千个[第三方 OAuth 应用](https://blog.cloudflare.com/oauth-for-all/)，至今授权次数已超过一百万次。

OAuth 实现了委托访问。它允许应用代表用户执行操作，而无需用户处理长期有效的凭据或交出密码。当应用能够以少量权限范围描述其访问需求时，这一模型运作良好。

开发人员将 OAuth 用于 SaaS 集成、内部工具、CLI 工具以及 AI 代理。随着时间推移，我们的权限模型已变得更加精细，以便更好地划定这些不同工作流的权限边界。这对安全性大有裨益，但也使纯粹的全有或全无授权同意页面愈发难以为继。

Cloudflare OAuth 已允许客户端请求其已配置权限范围的子集。但一旦客户端发出请求，用户就无法在授权同意页面上进一步缩小范围。对于授权同意页面上的用户而言，体验仍然是全有或全无。如果应用请求的访问权限超出用户愿意授予的范围，用户只有两个选择：批准全部请求，或直接拒绝。

MCP 服务器就是一个典型例子。MCP 服务器可能会请求一组宽泛的权限，因为理论上 AI 代理可能用到所有这些权限。但大多数用户并不希望 AI 代理拥有如此广泛的访问权限。在此功能推出之前，处理这一问题的唯一方式，是让应用开发人员在将用户引导至我们的授权同意流程之前，自行构建一个自定义权限范围选择页面。

今天，我们正式推出 OAuth 权限范围自定义功能。客户端所有者在配置 OAuth 客户端时，可以将特定权限范围标记为可选，从而让用户能够在授权时仅授予应用所请求访问权限的一个更窄子集。

OAuth 规范已允许授权服务器授予比请求范围更窄的权限范围集合。我们在这一灵活性基础上加以构建，使其能够为每个现有应用干净利落地运作。

## **更多掌控权，而不令用户不知所措**

引入权限范围选择功能的目标，是为注重安全的用户提供更大的灵活性，让其能够针对自身使用场景做出正确选择——同时不将授权同意页面变成冗长的权限范围清单。

借助权限范围自定义功能： 

  * 开发人员可以将 OAuth 客户端上的特定权限范围标记为必选或可选
  * 在授权时，用户可以从请求的权限范围集合中取消勾选可选权限范围
  * 必选和可选权限范围仅针对该次授权流程所请求的权限范围进行评估
  * 如果未请求任何可选权限范围，授权同意体验保持不变
  * 默认情况下，授权同意页面仍将授予所有被请求的权限范围



## **权限范围限定于授权请求**

一个重要细节是：必选和可选权限范围仅针对特定授权流程中所请求的权限范围进行评估，而不是根据客户端配置的所有权限范围进行评估。这一点至关重要，因为 OAuth 客户端并非总是请求其配置的全部权限范围。

例如，某客户端可能配置了 [user-details.read](http://user-details.read)、workers-scripts.write、workers-kv-storage.write 和 [zone.read](http://zone.read) 权限，同时将 workers-kv-storage.write 和 [zone.read](http://zone.read) 标记为可选。如果该客户端发起授权流程并请求全部四个权限范围，授权同意页面将对所有四个权限范围进行评估。在这种情况下，[user-details.read](http://user-details.read) 和 workers-scripts.write 仍是必需权限，但用户可以选择是否授予 workers-kv-storage.write 和 [zone.read](http://zone.read) 权限。

但是，如果该客户端稍后仅请求 workers-scripts.write 和 [zone.read](http://zone.read) 权限，则该授权流程仅考虑这两个权限范围。[user-details.read](http://user-details.read) 和 workers-kv-storage.write 将不会显示，也不会强制执行，因为它们不在请求范围之列。

这使授权同意页面聚焦于当前任务，而非应用可能请求的所有功能。这也意味着现有 OAuth 客户端的行为默认保持不变：如果客户端未选择启用可选权限范围，授权流程将维持原状。

## **配置 OAuth 客户端以使用可选权限范围**

开发人员可以在配置 OAuth 客户端时选择启用权限范围自定义功能。权限范围的配置方式与现在相同，客户端现在还可以额外指定哪些权限范围为可选：

在上述示例中，客户端可以请求全部四个权限范围，但用户在授权同意时只能取消 `workers-kv-storage.write` 和 `zone.read` 这两个权限范围。`user-details.read` 和 `workers-scripts.write` 一旦包含在授权请求中，将保持为必选。

如果该客户端后续仅请求 `workers-scripts.write` 和 `zone.read` 权限，则该授权流程仅考虑这两个权限范围。`user-details.read` 和 `workers-kv-storage.write` 将不会显示，也不会强制执行，因为它们不在请求范围之列。

## **在开发时考虑部分授权的情况**

当用户取消勾选任何可选权限范围并完成授权流程后，生成的访问令牌将只包含其同意授予的权限范围。对开发人员而言，这意味着在交换授权码之后，需要检查实际授予的权限范围集合，而不能假定所有被请求的权限范围均已获批。

一个能够优雅处理较窄授权的应用——例如，一个在其获得的任意权限范围子集内正常运作的 AI 代理——会让用户更放心地授权。仅请求必要的权限并将其余权限标记为可选，这是向用户表明应用尊重其访问决策的良好信号。

## **覆盖每款产品的权限范围**

未来几周内，我们将扩展账户和区域级别的角色体系，覆盖几乎所有 Cloudflare 产品。这意味着将有更多 API 令牌角色、账户成员选项以及 OAuth 权限范围，让客户能够以恰当的访问级别保护其工作负载。

## **立即使用可选权限范围构建**

通过可选 OAuth 权限范围，让开发人员和用户能够更精细地限制访问权限，是朝着在 Cloudflare 上实现更灵活、更可信的授权同意体验迈出的重要一步。借助可选权限范围，开发人员可以构建更细粒度的授权流程，用户也能对其批准的内容拥有更多掌控权。

如需开始使用第三方 OAuth，请参阅我们的[文档](https://developers.cloudflare.com/fundamentals/oauth/)，或直接前往仪表板中的 OAuth 应用页面，[创建您的第一个 OAuth 应用](https://dash.cloudflare.com/?to=/:account/oauth-clients)。

## **感谢我们出色的实习生**

此功能是我们在 [1111 名实习生](https://blog.cloudflare.com/cloudflare-1111-intern-program/)的协助下构建的众多功能之一。祝贺 Miller Vargas 和 José Enrique Rodriguez 在此项目中做出的卓越贡献。Miller 是德克萨斯大学奥斯汀分校计算机科学与数学专业的大四学生；José 是墨西哥泛美大学工程学、数据智能与网络安全专业的大四学生。

]]>01M221W4T0ZG2TKEQ3DHW867ZZ重新审视针对 Cloudflare Workers 的远程 Spectre 攻击https://blog.cloudflare.com/zh-cn/revisiting-spectre-attacks-on-workers/ Wed, 09 Sep 2026 02:45:51 GMT2024 年至 2025 年间，我们对针对 Workers 基础设施的远程 Spectre 攻击进行了重新评估。本文分享了 Spectre gadget、远程计时器、共同部署等新型攻击原语的详情，以及进一步强化 Cloudflare Workers 的新防御措施。Edge攻击漏洞研究2021 年，我们评估了针对 Cloudflare Workers 的[远程 Spectre 攻击](https://blog.cloudflare.com/spectre-research-with-tu-graz/)，并基于评估结果在生产环境中部署了名为[动态进程隔离](https://blog.cloudflare.com/spectre-research-with-tu-graz/)（Dynamic Process Isolation，DyPrIs）的防御机制——该机制能够识别行为可疑的脚本，并将其隔离至独立进程。此后，用于稳定 Spectre 攻击的新技术不断涌现。为评估这些技术是否对 Workers 生产环境构成威胁，我们决定在内部对远程 Spectre 攻击进行重新评估。通过在生产环境中构建更新版的概念验证，我们能够在实际生产负载下对 Spectre 攻击风险进行实证评估。

在生产环境中发动成功的侧信道攻击，外部攻击者还需克服额外障碍，包括共享硬件资源上的活动、中断、上下文切换以及粗粒度计时器等。我们的研究发现了 DyPrIs 实现中的一处缺陷，并成功在 Cloudflare Workers 生产环境中演示了一次远程 Spectre 攻击，可靠地以 99% 的准确率泄露最高达 12 bit/s 的数据。基于这项研究，我们改进了 DyPrIs，集成了 V8 Sandbox 和[进程内隔离机制](https://blog.cloudflare.com/safe-in-the-sandbox-security-hardening-for-cloudflare-workers/)，以进一步降低内存泄露攻击的风险。

今天，我们[发表了一篇论文](https://arxiv.org/pdf/2608.17043)，详细描述了上述研究发现，论文由 Albert Pedersen、Haocheng Xiao、Sam Ainsworth、Nigel Topham 和 Martin Schwarzl 共同撰写，涵盖 2024 年至 2025 年初的研究工作。

请注意，由于 Cloudflare Workers Runtime 团队已部署相应对策，文中所描述的攻击在生产系统中已得到缓解。过去三年间，我们未发现任何主动利用的迹象。

## **Cloudflare Workers 安全模型**

Cloudflare Workers 在边缘节点上运行不受信任的 JavaScript 代码。借助 V8 隔离区提供的语言层隔离，数以万计的租户可共享同一操作系统进程。每个 Worker 拥有各自独立的 JavaScript 堆。这一设计既能降低启动延迟，又能相比完整进程隔离方案更高效地运行大量租户。在运行时层面，我们部署了多层防御机制，例如自动化 V8 补丁管道、由 Linux 命名空间和 seccomp 过滤器构成的双层沙箱、Cap'n Proto RPC，以及将特定脚本调度至独立进程沙箱的功 能。尽管如此，Worker 进程内的单个任意读取漏洞仍然 可能导致跨租户数据泄露。其中一种漏洞非常难以缓解，它利用了推测执行的特性，即进程内 **Spectre** 漏洞。

## Spectre

推测执行的原理可以用登山来类比。在某个路口，您需要预判前行方向。若预判正确，您节省了时间，可以在山间小屋享受阳光和冷饮。然而，若预判方向错误，您不得不折返。山路看起来完好如初，但您的脚印仍留在泥土里。

CPU 的推测执行与此类似。分支预测（branch prediction）会提前对分支结果作出预判，CPU 随即推测性地执行该分支。若预测正确，推测执行节省了时间；若预测错误，CPU 则需丢弃结果、回滚并执行另一分支。由于这些推测执行的指令仅在 CPU 流水线中短暂存在，从未被永久退休或提交，学术界将其称为瞬态指令（transient instructions），并将该概念概括为瞬态执行（transient execution）。

然而，瞬态执行仍会在微架构状态中留下痕迹，例如残留在 CPU 缓存中的数据。因此，攻击者可利用 Spectre 以瞬态方式越界访问内存，将单个比特的信息编码至缓存状态，并通过测量重新访问数据的延迟来推断该比特是否被置位。

为[缓解进程内 Spectre 攻击](https://blog.cloudflare.com/spectre-research-with-tu-graz/)，Cloudflare Workers 冻结本地计时器，禁止多线程和共享内存，并主动检测可疑脚本、定期对内存进行随机化，同时将行为可疑的脚本隔离至独立进程。

## **攻击原语**

Cloudflare Workers 平台有意[限制计时器](https://blog.cloudflare.com/mitigating-spectre-and-other-security-threats-the-cloudflare-workers-security-model/)的精度。在仅使用 CPU 执行期间，时间实际上处于冻结状态：`[Date.now](http://Date.now)()` 和 `[performance.now](http://performance.now)()` 无法提供持续推进的高精度时钟。由于没有共享内存且不支持多线程，经典的基于 `SharedArrayBuffer` 的计数线程计时器也无从使用。

要成功发动攻击，需要克服几个挑战：首先，Workers 运行时间有限，必须确保攻击者与受害者位于同一位置；其次，必须找到一个可靠的、理想情况下位于同一位置的远程计时器，以进行稳定的计时测量；其三，攻击在生产条件下运行，因此还需要额外的稳定性措施，例如可靠的 Spectre gadget 以实现瞬态 64 位越界访问、应对系统和网络噪声的稳健信号放大机制，以及可靠地将数据从缓存中驱逐的原语。

### Spectre gadget

 _推测类型混淆 Spectre gadget_

借助正确的 Spectre gadget（如上方代码片段所示），攻击者可以瞬态方式越界访问内存，并将单个比特编码至缓存 (`probeArray`) 中。攻击者随后测量内存访问延迟，以确认数据是否已被缓存：访问较快意味着该缓存行已缓存，对应比特为 1；访问较慢则意味着未缓存，对应比特为 0。

在我们的攻击中，使用了两种不同类型的 Spectre gadget。第一种用于泄露压缩堆指针，例如隔离区的堆基地址（根地址）；第二种则利用推测类型混淆，从攻击者精心构造的用户空间 64 位指针处读取数据。在开展研究时，V8 Sandbox 尚未在 Cloudflare Workers 上实现。在指针压缩模式下，大多数对象使用 32 位压缩指针，而 `TypedArray` 是少数仍存储原始 64 位指向其后备存储的指针的例外——这正是我们的 gadget 所利用的。

分支 `obj instanceof ObjP `执行类型检查，即一次分支操作。为误训分支预测，我们多次以真实的 `ObjP` 实例调用该 gadget，然后以具有攻击者控制内存布局的不同对象 `ObjI` 调用它。CPU 随即推测性地执行该分支，从 `obj.ptr[0]` 读取数据，尽管该对象实际上是不同类型。为泄露单个比特，我们屏蔽出一个比特位，并用其选择 `probeArray` 中的两个缓存行之一，该缓存行是否被缓存即编码了该比特。

利用堆泄露 gadget，我们映射相邻对象并定位一个攻击者控制的数组。第二个 gadget 混淆两个跨越多个缓存行的大型对象，使类型字段落在与被读取字段不同的缓存行上。驱逐类型字段可打开推测窗口，同时目标字段保持缓存状态，瞬态读取随即跟随攻击者控制的 64 位值，从而将泄露转化为任意地址读取。该技术的更详细描述可参见论文原文。

**本地演示：泄露任意 64 位地址。**

### **信号放大**

缓存命中与缓存未命中之间仅相差数纳秒，而远程计时器的噪声量级则在数微秒至数毫秒之间。因此，需要某种形式的信号放大才能区分缓存命中与未命中。Stephen Röttger 和 Artur Janc 发现了一种[放大单次内存访问](https://security.googleblog.com/2021/03/a-spectre-proof-of-concept-for-spectre.html)的方法，其原理是利用 L1 缓存中基于树的伪最近最少使用（PLRU）缓存替换策略。基于树的 PLRU 将每个缓存组织为一棵二叉树，树节点指向最近最少使用的一侧，CPU 通过沿指针方向驱逐数据。利用特定的访问模式，攻击者可以在指针转向目标时持续触及其树邻居，从而使目标缓存行无限期保持缓存状态。这一思路颇为精妙：借助该行为，单次缓存事件的时序差异可被任意放大——与反向情形（大量 L1 未命中）相比，正向情形将产生大量 L1 命中（访问更快）。

下图展示了内存地址 X 是否处于缓存状态的两种情况。若未缓存，该访问模式将产生大量缓存命中；若已缓存，它占据树中的一个节点，导致四条缓存行竞争三个节点，从而引发大量 L1 未命中。

### **远程计时器**

只要信号能够被放大，嘈杂的远程计时器便足以区分编码的比特。例如，连接到提供高精度时间戳的外部服务器的 WebSocket 连接即可满足需求。该计时器可托管于 Cloudflare，或部署于与运行 Worker 的目标数据中心共同部署的数据中心。Worker 请求远程计时器为某一事件标记时间戳，并在事件结束后计算另一请求的时间差。

在论文中，我们评估了多种不同的计时器配置，即便在较大的拓扑距离下，仅凭少量样本便能稳定地实现中位数亚毫秒级精度。下图展示了使用基于树的 PLRU 放大后的缓存事件。

### **可重复测量**

单次测量不足以可靠地区分时序编码数据。生产机器噪声较大，因此攻击者需要对每次测量至少重复若干次，并使用某种统计判别器。在我们的方案中，重复测量意味着每轮重置缓存状态。每轮开始前需驱逐两类数据：推测分支所依赖的值必须被驱逐，使分支解析停顿足够长的时间以打开推测窗口；编码泄露比特的探测缓存行也必须被驱逐，以便下一次瞬态访问能够重新将其缓存。

由于 JavaScript 中没有直接可用的驱逐指令，经典方法是构建驱逐集（eviction set）——一组映射到与目标相同缓存组的地址集合。以正确的模式访问这些地址可将目标从缓存中驱逐。Stephen Röttger 和 Artur Janc 在其攻击中使用驱逐列表，可靠地将数据至少驱逐至 L2 缓存。这种方法有效，但代价较高：构建精确的驱逐集需要大量时序测量，而我们的计时器是一个嘈杂的远程计时器。此前针对 Workers 的远程攻击绕过了这一搜索过程，改为在每轮中遍历一个大于 L1 和 L2 缓存之和的数组——这是一种可行方案，但速度更慢。

Dougall Johnson 在其关于[可移植 JavaScript Spectre 利用](https://dougallj.wordpress.com/2021/03/16/another-approach-to-portable-javascript-spectre-exploitation/)的精彩博文中介绍了一种更优雅的方式，其思路直接源自鸽巢原理。若分配的数据量远超缓存容量，随机选取的缓存行几乎可以确定不在缓存中。对于 256 KB 的 L2 缓存，分配 64 MB 数据后，随机缓存行仍处于 L2 缓存的概率最多为 1/256。因此，无需驱逐特定缓存行，只需选取一个以压倒性概率已被驱逐的全新随机位置即可。频繁循环遍历该对象数组的副作用是产生自动驱逐效果。

为在 JavaScript 中利用这一特性，我们分配了一个超过末级缓存容量的攻击者-受害者对象对大型池。每轮测量选取一个全新的随机对，该对象的 map 指针——即推测类型检查所读取的隐藏类描述符——因此几乎可以确定已被驱逐。

### **实现攻击者与受害者隔离区位于同一位置**

要使攻击奏效，攻击者与受害者的隔离区必须被调度在同一边缘服务器的同一进程中。直觉上，这似乎并不容易——毕竟 Cloudflare 运营着数以万计的边缘服务器。然但实际上在 Cloudflare Workers 上实现二者共位相当简单。 由于 Cloudflare Workers 设计为可在任意 Cloudflare 边缘服务器上执行，在攻击者脚本中通过 `fetch("https://victim.example")` 调用受害者脚本，在大多数情况下会促使调度器在完全相同的进程中启动受害者 Worker 的实例。通过以固定时间间隔持续向受害者发送 子请求，可保持受害者隔离区持续存活。

此外，由于攻击稳定性在很大程度上取决于运行 Worker 脚本的边缘服务器的 CPU 负载，攻击者可以策略性地选择在非高 峰时段的托管数据中心发动攻击（例如在欧洲工作时间选择澳大利亚的数据中心），此时流量水平相对较低。

### **突破隔离区资源限制**

Cloudflare Workers 运行时对所有隔离区[强制执行一组限制](https://developers.cloudflare.com/workers/platform/limits/)，以保护平台并防止滥用。就本次攻击而言，相关限制为每次调用 30 秒 CPU 时间和 1,000 次子请求。这些限制此后已[提高](https://developers.cloudflare.com/workers/platform/limits/#account-plan-limits)，但以下原则仍然适用。

对于普通 Worker，每个 HTTP 请求（即 fetch 事件）都是一次新调用，会重置上述限制。难点在于如何让连续请求落在同一边缘服务器上——负载平衡和网络状况的变化使这一点难以保证。Durable Objects 为我们解决了这一问题。

[Durable Objects](https://developers.cloudflare.com/durable-objects/) 专为客户端间的实时协调而构建，运行时将每条传入的 WebSocket 消息视为一次新调用并重置 CPU 时间和请求限制。攻击者向一个 Durable Object Worker 建立持久 WebSocket 连接，并定期发送保活消息。这使单个隔离区持续存活，并为我们提供了一个持久的双向通道来执行攻击。

其中有一个细节耗费了我们不少时间。由于隔离区是单线程的，传入的 WebSocket 消息只有在脚本将控制权交还给事件循环时才会被处理。在同步代码执行期间，运行时不会感知到保活消息，因此不会重置 CPU 时间。若线程持续阻塞超过 30 秒，运行时将终止隔离区。这为单次同步执行突发中的放大量设定了上限。在各次突发之间定期让出控制权，使我们能够将隔离区保持存活长达 5 小时至 20 余小时。

### **综合运用**

此前的攻击主要依靠重复来放大单次缓存访问，因此泄露速率较低，约为 120 比特/小时。我们将基于树的 PLRU 放大机制与测量循环相结合：每次迭代重建缓存状态，从而累积更大的时序差异。即便某次迭代中中断破坏了缓存状态，后续迭代也能将其抵消。这使信号强度足以通过远程 WebSocket 计时器对比特进行分类。总体思路如下：

我们在 Cloudflare Workers 生产环境中，针对我们自己控制的 Worker，完整演示了端到端攻击。我们首先从攻击者 Worker 泄露内存，继而从一个共同部署的受害者 Worker（我们事先在其中放置了秘密数据）中泄露数据。

第一步，在攻击者 Worker、我们拥有的受害者 Worker 和远程计时器之间建立共同部署关系。Durable Objects 为我们提供了长期执行上下文，WebSocket 消息提供了可重复的时序来源，`/cdn-cgi/trace` 端点通过查看 _fl_ 字段帮助我们确认机器部署位置。

第二步，增加校准步骤，以推测可达的值探测计时器。这一步骤至关重要，因为生产机器噪声较大。逐次调用的校准使我们能够根据 0 分布和 1 分布之间的相对差异对比特进行分类，最终应产生两个可清晰区分的分布。

第一阶段，我们从一个 Worker 泄露了隔离区根地址；在另一个 Worker 中，我们使用基于 64 位指针的推测类型混淆，从该根地址处读取数据。

作为中间验证步骤，我们通过读取 vDSO 区域的内存确认了第二个 gadget 的 64 位泄露能力。vDSO 是一个便于验证的目标，因为其中包含 `gettimeofday` 等人类可读字符串。

**演示视频：从 JavaScript 堆泄露数据**

最终，我们在受害者 Worker 中放置了一个 JWT 令牌，并逐比特泄露。第一个字节为字符"e"，二进制表示为 0b01100101。下图展示了该字节的逐比特分类结果。分类过程使用双侧检验同时测试两种结果，并通过多数投票和基于百分位的阈值推断比特值。在生产环境中，我们实现了最高 12 bit/s 的泄露速率，准确率超过 99%。需要注意的是，更高的泄露速率以牺牲准确率为代价。

### **鲁棒性**

随着一天中时段的不同，机器利用率会显著上升，进而拖慢攻击速度——因为需要采样更多数据。然而即便在 CPU 利用率较高的情况下，攻击依然可行。

## **为何未被检测到？**

DyPrIs 监测硬件性能计数器，一旦脚本行为疑似 Spectre 攻击，便将其隔离至独立进程。以下两点使本次攻击得以躲避检测。

其一，DyPrIs 仅在脚本调用结束后才会触发隔离，而我们在攻击中使用的 Durable Object 保活技巧可持续运行数小时乃至一天。WebSocket 保活消息使单次调用持续开放数小时，泄露早在隔离机制介入之前便已完成。

其二，DyPrIs 通过 iTLB 访问次数对分支预测错误进行归一化处理。我们的远程计时器是一个大型 I/O 循环，WebSocket 流量会显著增加 iTLB 活动量。归一化后的比率降至检测阈值以下，使该攻击看起来与普通的 I/O 密集型 Worker 无异。

## **我们的改进措施**

我们重点从三个方面持续推进改进：V8 深度加固、提供更强的进程内隔离，以及改进检测机制。

### **V8 Sandbox**

V8 内存沙箱的最终目标是从 JavaScript 堆的大部分区域移除原始 64 位指针，从而降低众多内存破坏原语的利用价值。这也使本研究中特定推测类型混淆 gadget 的复用难度大幅提升，因为 typed-array 后备存储不再暴露相同的原始指针结构。

V8 Sandbox 并非针对 Spectre 的完整缓解方案。尽管文中所述的 64 位泄露 gadget 不再适用，但仍可能存在其他 Spectre 变体或 gadget 可被利用，以实现任意越界内存访问。

### **硬件辅助进程内隔离**

2025 年 9 月，我们为 Workers 部署了基于内存保护密钥（Memory Protection Keys，MPK）的[进程内隔离](https://blog.cloudflare.com/safe-in-the-sandbox-security-hardening-for-cloudflare-workers/)机制。MPK 允许进程将内存划分为保护域，并以低成本切换访问权限。Workers 利用该机制保护每个堆，防止其被同一进程内的其他隔离区访问。

这从根本上改变了 Spectre 的风险模型。每个隔离区的堆现在受到硬件强制访问边界的保护：对受错误密钥保护的页面的内存访问，将在硬件层面被拒绝。这阻断了本研究所依赖的直接跨隔离区堆读取路径。

然而，MPK 并非缓解 Spectre 的完整答案，但它严格收窄了泄露面。其局限性包括：硬件域数量有限，以及需要谨慎管理保护密钥状态。

### **改进 DyPrIs**

我们改进了 DyPrIs，将长期执行和 I/O 密集型工作负载作为一类安全问题来处理。检测不能仅在脚本结束后才触发。Durable Object 或 WebSocket 密集型 Worker 可能运行时间很长，以至于执行后隔离机制介入时为时已晚。

我们目前正在研究是否可将远程时序行为作为 DyPrIs 的额外检测维度。尽管我们无法阻断与攻击者控制基础设施的远程通信，但时序数据揭示了极具特征性的数据泄露比特模式。更好的做法是将计算密集型代码段周围重复出现的类计时器 I/O 纳入行为信号，而非将其视为背景噪声。

## **致谢**

特别感谢爱丁堡大学的 Haocheng Xiao 及其导师 Sam Ainsworth 和 Nigel Topham，感谢他们在提升 JavaScript 中 Spectre 攻击可靠性方面所作的贡献。

## **参与邀请**

我们始终欢迎您通过我们的[漏洞赏金计划](https://hackerone.com/cloudflare)提交高质量报告。运行时内存安全漏洞是高价值目标。您可以在 GitHub 上找到 [workerd 的 Fuzzilli 集成](https://github.com/cloudflare/workerd/pull/4917)及 [workerd 源代码](https://github.com/cloudflare/workerd)。

]]>01M2200RQ4MGJA58XGS5S2SAX7Cloudflare 如何检测 MCP 流量并助力安全防护https://blog.cloudflare.com/zh-cn/mcp-security-updates/ Wed, 09 Sep 2026 02:07:31 GMTCloudflare Gateway 利用协议层启发式方法识别 MCP 请求。安全团队可借助该信号发现影子 MCP 流量、对已批准服务器强制执行仅限 Portal 的访问，并阻止受管网络路径上的直接连接请求。AICloudflare OneMCPSASEZero Trust产品新闻大多数企业在设计资源权限时，考虑的对象是人类用户。一位高级工程师可能拥有部署到生产环境、查询敏感数据库或撤销其他用户访问权限的权限。这些权限本身存在风险，但传统上该风险受到两个前提的约束：工程师会运用人类判断力，且工程师每天的操作速度有其上限。

工程师看到异常结果时，通常会停下来重新审视自己的操作。任何人每天能够点击、输入和审阅的内容都是有限的。AI 智能体的引入改变了这两个阈值。它们的决策具有不确定性，且可以无限次执行同一操作（或调用同一工具），既不会疲倦，也不需要休息。一个看似合理却错误的决策，可能在人类察觉之前已演变为数以千计的错误操作。

今天，我们宣布推出全新 [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) 功能，用于识别经过检测的 MCP 流量、显示流量的生成用户和服务器，以及管控受管网络路径上的直接连接请求。结合 [MCP Server Portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/)，这些管控机制帮助管理员判断智能体是否正在使用已批准的访问路径，还是以某种方式绕过了它。

[模型上下文协议](https://www.cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/) (MCP) 服务器为智能体提供了一种通用方式，用于发现和调用由第三方 SaaS 产品、内部应用程序及 API 支撑的工具。底层权限逻辑大多并不陌生；真正改变的是 _谁_ 在做每个决策，以及错误决策扩散的速度。

将智能体连接到其中某个工具，可能只需一行配置。员工可以将 Claude Code、Codex、Cursor、OpenCode、VS Code 或任何 AI 工具指向某个 MCP 服务器，而无需检查该服务器是否已获批准。由此产生的流量没有明显特征。模型上下文协议不使用固定主机名，也不要求路径中包含 /mcp，因此，直接连接看起来可能与任何其他 HTTPS API 调用相似。

为了说明这些管控机制如何协同运作，我们将从工具调用的结构及其暴露的信息入手，然后比较安全团队可采取行动的三个位置：客户端内部、网络层和 MCP 服务器。在此基础上，我们将展示 [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) 如何利用协议信号发现影子 MCP 流量，并对受信任的 MCP 服务器强制执行仅限 MCP Portal 的访问。

## **MCP 工具调用的结构**

同一个 MCP 工具调用在经过系统的过程中呈现三种形态。在客户端内部，它是调用某个工具并附带一组参数的决策；在网络层，它是一个承载 [JSON-RPC](https://www.jsonrpc.org/specification) 消息的 HTTP 事务；在服务器端，它变为对工具处理程序的调用，该调用可能读取数据、改变状态或完成其他操作。

设想一个智能体想要查询奥斯汀的天气。一个远程 MCP 请求的形式如下：

这个请求中包含多个有用的信号。主机名和路径标识了目标服务器。当服务器要求认证时，Authorization 标头携带用于验证调用方身份的凭据。`MCP-Protocol-Version` 标头标识协议版本，而 `Mcp-Method` 和 `Mcp-Name` 则在新的无状态协议中暴露了操作类型和工具名称。JSON-RPC 信封重复了方法信息，通过 `id` 字段让客户端能够将请求与响应匹配，并在 `params` 中携带工具参数。

参数是最敏感的部分，可能包含搜索查询、源代码、客户数据，或创建工单、变更基础设施等操作指令。工具名称说明了智能体打算调用什么；参数则揭示了它将发送哪些数据，以及希望服务器执行什么操作。

调用成功后，服务器返回携带相同 ID 和工具结果的 JSON-RPC 响应。该响应同样可能包含敏感数据。请求检测可以在执行前阻止不安全的操作，而响应检测和日志记录则记录工具向智能体返回了什么内容。

## **管控 MCP 请求的三个位置**

该请求为安全团队提供了三个可观测或管控调用的位置。

### **MCP 客户端内部**

[ 客户端钩子](https://code.claude.com/docs/en/hooks)可在模型选定工具之后、客户端序列化请求之前运行。在此阶段，无需解密网络流量，即可获取目标服务器、工具名称和参数信息。

这是请求链中最早可施加管控的阶段。客户端可以拒绝不在允许列表中的服务器、要求用户确认敏感操作，或在数据离开设备之前将其从参数中移除。客户端钩子还可以覆盖本地 `stdio`（即本地）MCP 服务器，这类服务器不产生任何网络流量。

这一方式存在标准化挑战。要使安全团队从中受益，需要在员工使用的每个客户端上复现相同的管控逻辑。客户端侧的管控在组织同时管理客户端和设备时效果最佳，但来自单个客户端的遥测数据永远无法完整呈现 MCP 的使用全貌。

### **设备的网络边界**

[ 安全 Web 网关](https://www.cloudflare.com/learning/access-management/what-is-a-secure-web-gateway/)可在请求离开客户端后对 HTTP 请求进行观测。借助 [TLS 解密](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/tls-decryption/)，它可以将请求与用户和设备关联，检测目标及协议标头，并在不依赖特定 MCP 客户端的情况下应用策略。

网络层具有最广泛的视角，能够检测受管路径上的远程 MCP 流量。它可以识别直接连接至已批准 Portal 之外服务器的请求，并在请求到达目标之前予以阻止。在支持[数据丢失防护](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)扫描的场景下，代理还可以检查请求体中的 JSON-RPC 方法和参数是否含有敏感数据。然而，代理无法查看本地` stdio `调用或网络外流量。

### **MCP 服务器调用工具之前**

服务器拥有最丰富的执行上下文：它已完成调用方的身份验证、解析了 MCP 消息、将 `get_weather `解析到对应的处理程序，并针对工具输入 schema 验证了所提供的参数。这是工具运行前最后一个可以拒绝请求的位置。

[Agents SDK](https://developers.cloudflare.com/agents/model-context-protocol/) 处理程序或类似的服务器中间件可以针对特定工具对调用方进行授权、应用速率限制、检测参数，并记录执行结果。服务器应在调用处理程序之前完成这些检查，尤其是针对写入数据或触发外部操作的工具。仅在执行后记录日志只能解释已发生的事情，但无法加以阻止。

Cloudflare 的 [WriteGuard](https://blog.cloudflare.com/mcp-portal-writeguard-private-beta/) 正是在我们内部的 MCP 服务器中采用了这一模式。每个工具都有对应的风险等级和启用/禁用状态。WriteGuard 可以放行读取操作、为允许的写入操作添加智能体归因信息和审计事件，或在关键操作的处理程序运行之前予以阻止。由于管控逻辑位于服务器端，终端用户无法通过切换客户端或禁用本地钩子来绕过它。

服务器端管控仅能保护已实现该机制的服务器，而客户端和服务器拥有最深的请求可见性；网络层则覆盖最广泛的远程连接范围。三者协同使用，可以在敏感数据离开设备前予以拦截、发现未受管的 MCP 流量，并在工具执行前阻止未经授权的操作。

网络管控点覆盖范围最广，但首先需要将 MCP 流量与普通 HTTPS 流量区分开来，用户还必须运行代理，且 MCP 服务器（或 Portal）必须验证连接中使用了该代理。

Cloudflare One 提供了该链路中的网络组件。[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/) 将受管设备的流量通过 Gateway 传输。Gateway 可以在协议层对 MCP 请求进行分类，并区分流量是来自 MCP Portal 还是绕过了已批准的管控路径。管理员随后可以对不遵循已批准路径的连接进行报告或阻止。这一过程始于对请求的可靠识别。

## **URL 无法告诉您请求是否使用了 MCP**

我们最初检测 MCP 流量的方法，是使用 GraphQL Analytics API 在 [Gateway HTTP 日志](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/)中搜索包含 `mcp` 的主机名以及 `/mcp`、`/sse `等常见路径。我们的 [MCP 流量检测教程](https://developers.cloudflare.com/cloudflare-one/tutorials/detect-mcp-traffic-gateway-logs/#2-build-the-mcp-detection-query)包含了相关查询，同时说明了如何为请求体中的 MCP JSON-RPC 方法（如 `initialize、tools/call、resources/read`）[创建数据丢失防护模式](https://developers.cloudflare.com/cloudflare-one/tutorials/detect-mcp-traffic-gateway-logs/#4-create-dlp-profiles-for-mcp-json-rpc-detection)。

这些信号对于检测旧版客户端流量和提供历史可见性仍然有用，但也相当基础。它们会漏检普通 URL（例如[ ](https://tools.example.com/api)[https://tools.example.com/api）中的](https://tools.example.com/api%EF%BC%89%E4%B8%AD%E7%9A%84) MCP 服务器，这种情况并不少见。

此外，这些信号还可能误匹配恰好在主机名或路径中使用了 mcp 的无关服务（虽然概率较低，但我们确实遇到过）。对于符合规范的 Streamable HTTP 客户端，协议标头是更为精确的信号。[MCP 2025-11-25 规范](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports#protocol-version-header)要求客户端在初始化之后的每个 HTTP 请求中必须包含 `MCP-Protocol-Version`。[MCP 2026-07-28 规范](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http#protocol-version-header)则进一步要求在每个 POST 请求中均包含该信息。

但这并不意味着该标头是完备的检测手段。旧版客户端的初始请求可能不含该标头，2025-06-18 之前的协议版本并未定义它，而本地 `stdio`、自定义传输或不符合规范的流量也可能从不携带该标头。标头的存在是 MCP 的强正向指示；其缺失并不能证明请求不是 MCP。

## **协议在网络层愈发易于识别**

旧版 MCP 流程以不含 `MCP-Protocol-Version` HTTP 标头的 `initialize` 请求开始，因此网络管控可能无法仅凭该标头对首次请求到未知端点的流量进行分类。该信号在客户端和服务器完成初始化之后才会出现。

后续的工具调用形式如下：

[MCP 2026-07-28 规范](https://modelcontextprotocol.io/specification/2026-07-28)对此模型进行了重大更改。核心协议变为无状态，完全移除了 `initialize` 握手，而是将协议版本和操作信息添加到每个请求中：

`Mcp-Method` 和 `Mcp-Name `标头使普通 HTTP 基础设施无需解析请求体即可识别操作类型。负载均衡器可据此路由请求，速率限制器可区分 `tools/list `与 `tools/call`，安全产品也能在每个请求中获取更多信息。

这些协议信号为 Cloudflare Gateway 提供了具体可评估的依据，无需依赖预先维护的 MCP URL 列表。

## **影子 MCP 与已批准路径绕过是两个独立的问题**

Gateway 能够识别 MCP 流量后，您随即可以评估某个连接对安全态势的具体影响。

影子 MCP 是指连接到组织未批准的服务器。员工在代码仓库、产品文档或同事消息中发现该服务器后，直接将其添加到 MCP 客户端。安全团队对该服务器暴露了哪些工具、员工向其发送了哪些数据一无所知。

Portal 绕过则不同：它始于一个已获批准并被纳入 MCP Portal 的服务器，但员工直接连接其上游 URL，跳过了 Portal 的 Access 策略、精选工具目录、数据丢失防护和工具级审计追踪。

Gateway 是受管网络路径上针对影子 MCP 的主要管控手段——它识别经 TLS 检测的 MCP 流量，显示目标和用户，并可应用策略。应对 Portal 绕过则需要在网络管控的基础上，辅以能够拒绝直接连接请求的源站——无论是通过 Access 策略、源 IP 限制，还是由 MCP 服务器本身发起的企业级授权机制。

## **检测 Gateway 中的 MCP 流量**

对于已采用 Cloudflare Gateway 并启用 TLS 检测的客户，我们正在新增一项检测启发式机制，针对每个经过检测的请求回答一个简单问题： _这是 MCP 流量吗？_

对于基于会话的 Streamable HTTP 连接，MCP 客户端在初始化之后会发送 `MCP-Protocol-Version `标头。Gateway 对每个经过 TLS 检测的请求检查该标头并据此对流量进行分类，其检测机制基于我们从每天穿越 Cloudflare 网络的数百万请求中观测到的模式构建而成。该分类能够在不预先掌握特定主机或 URL 的情况下识别 MCP 协商和代理请求。

**即日起，所有 Cloudflare Zero Trust 客户均可在 Gateway HTTP 日志中查看 MCP 流量标记，并且可以使用以下新增 Gateway 选择器明确地阻止或允许该流量：**

`experimental.is_mcp == true`

该选择器为布尔值。若 Gateway 在经过 TLS 检测的请求中检测到 `MCP-Protocol-Version` 标头，则值为` true`，管理员可以在允许或阻止策略中使用它，而无需自行维护 MCP 域名列表。

直接加密的流量必须先通过 [TLS 解密](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/tls-decryption/)，Gateway 才能检测这些标头；本地 `stdio `服务器、网络外连接、[Do Not Inspect](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#do-not-inspect) 流量以及未经 Gateway 传输的请求，均不在此检测范围之内。

## **全网 MCP 流量可见性**

今天，我们推出专属 MCP 流量仪表板，展示网络内哪些主机正在提供 MCP 服务、哪些用户正在产生流量，以及请求是通过 Cloudflare MCP Portals 传输还是完全绕过了它们。

仪表板显示：

  * 可配置时间窗口内的 MCP 请求总量、唯一用户数及唯一服务器数
  * 各服务器随时间变化的 MCP 请求量及逐服务器请求计数
  * 按流量来源（on-ramp）分类的流量明细，区分 MCP Portal 流量与设备客户端直接连接请求
  * Portal 之外访问量最高的 MCP 服务器——即最需要关注的影子 MCP 流量
  * 按 MCP 请求量排名的活跃用户



管理员可按特定服务器、用户或流量来源类型进行筛选，并可直接跳转至按相关主机或用户过滤的 Gateway HTTP 日志，以便深入调查。

## **将已发现的服务器纳入 MCP Portal**

MCP 发现功能将未知流量转化为管理员可供调查的清单。当组织批准其中某个服务器时，可将其置于 Cloudflare MCP 服务器 Portal 之后。Portal 为员工提供统一的受管端点，并在上游服务器前置 [Access](https://developers.cloudflare.com/cloudflare-one/access-controls/) 身份验证、精选工具目录和日志记录。管理员可[将兼容的上游调用通过 Gateway 路由](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#route-portal-traffic-through-gateway)，以实现 HTTP 策略、可预测的出站流量和数据丢失防护，范围覆盖整个 Portal 或单个服务器。工具活动还可以[通过 Logpush 导出](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#export-logs-with-logpush)。发现仪表板随后可以区分经由 Portal 传输的请求与直接连接到同一服务器的请求。

这构建了一条从发现到治理的完整路径：发现服务器、决定是否批准、将已批准的使用迁移至 Portal，并调查持续绕过 Portal 的流量。最后一步尤为重要，因为未经批准的服务器与已批准服务器被绕过，是两个性质不同的问题。

## **强制执行仅限 Portal 的访问**

我们正在 Gateway 网络和[ HTTP 策略](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/)中新增流量来源选择器，让管理员能够根据 MCP 流量是否源自 MCP Portal 来编写规则，以控制 MCP 流量。

当 MCP Portal 流量通过 Gateway 路由时，会携带 `mcp_portal` 流量来源标记，从而使策略能够区分经由 Portal 代理的请求与员工直接连接请求。一条基础的强制执行规则如下：

所有检测到的 MCP 流量，凡未经由 Portal 传入的均予以阻止；经由 Portal 传入的流量则不受影响。对于希望先观察再执行的组织，流量来源和 MCP 检测结果现已出现在已解密流量的 HTTP 日志中，无需创建策略即可监控代理流量的行为。

## **更多 MCP 服务器现可使用受管路径**

已批准路径只有在能够连接到员工实际需要的足够数量的服务器时，才具有实际价值。

早期 MCP 规范推荐使用[动态客户端注册](https://datatracker.ietf.org/doc/html/rfc7591)，允许客户端在无需 OAuth 应用的情况下向授权服务器注册自身。然而，许多常见的 OAuth 提供商采用不同的模型：要求管理员使用固定的客户端 ID、客户端密钥、回调 URL 和权限范围注册应用程序。`MCP 2026-07-28` 规范近期也已弃用动态注册。

为帮助解决这一问题，MCP Portal 现已支持预注册的 OAuth 客户端。管理员可以[配置手动 OAuth 凭据](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#configure-manual-oauth-credentials)，在上游提供商处注册仪表板中显示的回调 URL，并输入客户端凭据。Portal 在可用时会自动发现标准 OAuth 元数据；当发现功能不可用时，管理员可手动提供授权、令牌、撤销和颁发者端点。

每位用户仍需自行授权访问其上游数据源，存储的客户端密钥仅用于获取更新的工具和提示列表。

手动 OAuth 支持现已帮助覆盖众多 OAuth 实现的排列组合。部分提供商要求自定义标头、个人访问令牌或明确的客户端允许列表，这些属于独立的兼容性问题。我们将在未来数月持续扩展 MCP Portals 的 OAuth 支持。

## **将专用 MCP 服务器纳入统一 Portal**

公共 SaaS 工具只是企业 MCP 目录的一部分。企业依赖的大多数安全信息并非来自公共互联网；它们存在于公有云或私有云基础设施中，或托管于本地，只能通过接入专用网络才可访问。

目前，MCP Portal 必须能够通过公共互联网解析并访问上游服务器。这意味着仅在专用网络中可用的服务器——通过[私有 DNS](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/private-dns/) 或私有 IP 空间访问的服务器——尚无法被 Portal 访问。我们正在推进让 MCP Portals 通过 Cloudflare Gateway 路由和 Cloudflare One 网络连接专用服务器，该网络已被广泛用于其他专用应用程序。

专用服务器保留其私有主机名；Portal 通过 Cloudflare 的私有路由访问它，并将其工具与公共上游服务器并列呈现；Access 策略、Portal 日志记录和工具管控在同一入口处继续生效。

将 Portal 流量通过 Gateway 路由，还会为其打上 mcp_portal 流量来源标记，使 Gateway 策略能够区分 Portal 请求与员工直接连接请求。MCP 服务器的专用连接功能正在积极开发中；请关注[ Changelog](https://developers.cloudflare.com/changelog/) 获取更多信息。

## **Agents SDK 支持新的无状态模型**

几周前，MCP 项目发布了 `2026-07-28 `规范——这是一次重要修订，以无状态的逐请求模型取代了基于连接范围的初始化机制。我们在“[下一代 MCP](https://blog.cloudflare.com/mcp-v2)”一文中介绍了协议变更和迁移路径。

[Cloudflare Agents SDK](https://developers.cloudflare.com/agents/model-context-protocol/) v0.20.0 以客户端和服务器双重身份支持 MCP `2026-07-28`。对于每个连接，客户端首先通过 `server/discover` 探测新的无状态协议；若服务器不支持，则在同一连接上继续使用旧版 `initialize `握手流程。现有的 `addMcpServer `调用无需单独配置协议设置或切换客户端。

在服务器端，`createMcpHandler` 可从 [Worker](https://developers.cloudflare.com/workers/) 无状态地提供工具、提示、资源和 elicitation，无需创建传输会话或 [Durable Object](https://developers.cloudflare.com/durable-objects/)：

向下兼容至关重要，因为协议迁移鲜少一蹴而就。新版客户端仍需访问现有服务器，新版服务器也仍需处理尚未完成迁移的客户端请求。Agents SDK 在生态系统完成过渡期间同时支持两种路径。

## **首先提高可见性，然后关闭不应存在的访问路径**

切实可行的 MCP 安全方案，始于理解用户流量特征和 MCP 使用情况，并就已批准的工具集与访问方式达成共识。

首先，检测经由 Gateway 传输的 MCP 流量，将其目标与组织已批准的服务器进行比对，并将更多已批准服务器迁移至 MCP Portal。

随后，在可管控边界上执行策略。结合 MCP 检测条件、流量来源和目标条件，构建 Gateway 策略，阻止受管设备和站点上的 MCP 直接连接请求，并尽可能将自托管上游服务器限制为仅接受 Portal 流量。

我们即将推出更细粒度的 MCP 流量可见性与管控功能，包括对特定工具使用的管控，以及对您环境中所有 MCP 服务器工具使用情况的全新报告——无论这些服务器是否已被您的安全团队掌握。

我们的[ MCP 流量检测教程](https://developers.cloudflare.com/cloudflare-one/tutorials/detect-mcp-traffic-gateway-logs/)涵盖了 Gateway 日志目前可用的主机名、路径和 JSON-RPC 启发式方法。新信号正式发布后，我们将更新文档，介绍协议选择器的详细信息。  


]]>01M21XWD4CVM73Y8VTQ8CC6ZGC一键保护所有内部应用，无论是否经过“氛围编码”https://blog.cloudflare.com/zh-cn/workers-protected-by-access/ Wed, 09 Sep 2026 01:45:16 GMT全新推出 Cloudflare Access for Workers。将 Access 策略直接绑定到 Worker，即可在该 Worker 运行的所有位置自动生效——路由、自定义域、workers.dev 及预览环境，全面覆盖。AICloudflare AccessCloudflare WorkersInternship ExperienceSASEZero Trust产品新闻开发人员开发人员平台AI 让各团队员工能够比以往更快地构建应用程序。

然而，这种高速发展也让每位 CISO 夜不能寐：任何员工都可以构建应用程序、将其部署到公共互联网，并在不经意间暴露内部工作成果或公司数据。

今天，我们推出全新工具，让您轻松将托管在 Workers 上的应用程序保持私密。现在，您可以将 Cloudflare Access 直接应用于单个 Worker 或账户内的所有 Worker，如此一来，默认情况下应用会受到公司登录的保护，无需依赖于每个开发人员自行设置。 

您现在可以：

  * **在账户层级设置策略** ，确保所有[预览](https://developers.cloudflare.com/pages/configuration/preview-deployments/)环境和生产环境的部署默认受公司登录保护。
  * **为单个应用程序设置策略** ，确保在与该应用程序关联的每个域上都强制执行身份验证，无论以何种方式部署。
  * **精确掌握应用程序的访问者信息** 。直接在代码中获取每位已认证用户的电子邮件、姓名和所属群组——无需进行 JWT（JSON Web Token）验证。
  * **部署一个每次部署默认私密的内部平台** 。我们已开源一个[示例](https://github.com/cloudflare/templates/tree/main/internal-sites-template)：一个内部静态站点平台，其中每个已部署的 Worker 均默认保持私密。



## **Access on Workers 的工作原理**

为 Worker 启用 Access 后，Cloudflare 会在任何请求到达应用程序代码之前强制执行身份验证。无论请求通过何种方式到达 Worker——自定义域、路由、[workers.dev](http://workers.dev) 子域还是预览 URL——只要启用了 Access，用户就必须先完成身份验证。

此前，您需要在主机名层级进行配置，这意味着要在 Worker 所可达的每个域上分别设置 Access 策略。如果您希望为 Worker 新增自定义域，则必须先更新 Access 策略，否则该主机名将在无需身份验证的情况下可被访问。  
现在，策略直接绑定到 Worker 本身，因此与该 Worker 关联的任何域或 URL 均会自动受到保护。您可以选择保护范围：仅预览 URL，或所有主机名。

若设置为仅保护预览环境，则每次部署新版本时，为该应用程序创建的所有预览 URL——无论是 [workers.dev](http://workers.dev) 预览 URL，还是用于预览的自定义域——都将要求身份验证。若设置为保护所有主机名，则与该 Worker 关联的每个域均受保护——自定义域、路由、[workers.dev](http://workers.dev) 子域及预览 URL，一概涵盖。

Access 让您掌控用户的身份验证方式。您可以接入现有的标识提供程序，让员工使用已有凭据登录；也可以将访问权限限制为特定电子邮件地址、电子邮件域或群组。对于代理，可通过服务令牌授予访问权限。

如需了解更多详情，请参阅 [Cloudflare Access for Workers 文档](http://developers.cloudflare.com/workers/configuration/cloudflare-access/)。

## **默认让账户内所有 Worker 保持私密**

如果组织中有多个开发人员部署 Workers，您不会希望依赖于每个开发人员都记得启用 Access，而是希望默认设置为私密。

在账户层级设置一次 Access 策略，账户内所有 Workers——无论当前已有的还是未来新建的——都将从创建之时起保持私密。

您可以选择策略的覆盖范围：仅预览 URL 流量、所有生产流量，或两者兼顾。仅预览环境模式适用于生产 Workers 有意公开，但您不希望进行中的部署被暴露的场景。

需要某个 Worker 对外公开？在该 Worker 上绕过账户层级策略即可。

### **保护特定 Worker**

如果您不需要账户层级的默认策略，只想锁定某个特定 Worker，可以直接将 Access 应用于该 Worker。

Worker 视图中新增的 Access 选项卡清晰展示了哪些策略适用于该应用程序。若存在多条策略，优先级最高者将生效：主机名策略优先，其次是 Worker 策略，最后是账户策略。

## **查看应用程序的访问者信息**

当 Access 保护您的 Worker 时，您可以获取每个请求的发起者信息——电子邮件、姓名及所属群组——从而实现内容个性化、权限管控或按用户记录访问日志。

这一功能通过 [Worker 的 context 对象 (ctx) ](https://developers.cloudflare.com/workers/runtime-apis/context/)实现。每个发往 Worker 的请求都携带一个 ctx，其中包含该请求的元数据。启用 Access 后，我们会将已认证用户的身份信息附加到 ctx 上，即 `ctx.access`。调用 `ctx.access.getIdentity()`，即可获取用户的电子邮件、姓名及[更多信息](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/)。

此前，这意味着需要自行验证 JWT——解析令牌、验证签名并提取声明。现在，只要在 Worker 上启用了 Access，每个已认证请求均自动包含 `ctx.access`。

获取用户身份只需以下代码：

## **在部署前进行本地测试**

我们演示了如何使用 `ctx.access.getIdentity() `让 Worker 获取请求发起者的信息——电子邮件、姓名及所属群组。

您可以在使用 `wrangler dev` 进行本地开发时使用此功能。在 `wrangler.jsonc` 中添加一个 `access` 配置块，以模拟已认证用户：

您的 Worker 会通过 `ctx.access.getIdentity() `获取该配置——返回的身份对象与生产环境中的结构一致。修改配置中的电子邮件，即可模拟不同用户进行测试。

这意味着您无需每次修改后都重新部署并通过 Access 登录，即可验证不同用户能否看到正确内容。

## **部署一个每次部署默认私密的内部平台**

如果您管理着一个内部平台，供员工快速构建和部署应用程序，则需要每个应用程序在无需逐一配置访问控制的情况下保持私密。

[Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/) 支持大规模部署 Workers。每个 Worker 都位于一个命名空间内，所有进入该命名空间的流量均通过调度 Worker 这个单一入口点传递。

在调度 Worker 上设置 Access 策略，则通过该平台部署的每个 Worker 默认设置为私密。

我们还提供了一个[开源示例](https://github.com/cloudflare/templates/tree/main/internal-sites-template)，帮助您部署自己的内部拖放式部署平台——只需在调度 Worker 上配置一次 Access，通过该平台部署的每个站点默认设置为私密。

点击下方按钮，立即部署！

如需了解完整架构，请参阅 [Workers for Platforms 参考架构](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/)。

## **坚实的技术基础**

这项功能得益于 FL2，它是一款全新[基于 Rust 的模块化代理](https://blog.cloudflare.com/20-percent-internet-upgrade/)，为 Cloudflare 边缘提供支持。Access 是应用程序的前置门卫，因此传统上在请求管道中，它在所有 Workers 逻辑之前执行。但是，为了让 Access 应用程序能够直接定位到特定 Workers 而不是其主机名，Access 需要知道给定请求的目标 Worker。为此，我们需要将 Workers _路由_ 与 Workers _执行_ 分离，并将路由逻辑前移，使其能够在 Access 之前运行。

在我们旧有的基于 NGINX 和 Lua 模块构建的 FL1 系统中，这一改动将既复杂又存在风险。产品间的交互可能极为微妙，将逻辑移至请求管道的更早阶段，若该逻辑依赖于另一产品所修改的共享状态，则可能引入安全隐患。

FL2 让这一切变得简单。其严格的模块系统将逻辑划分为定义清晰、顺序一致的各个阶段，并通过静态声明各阶段的输入与输出。我们得以借助编译器发现各阶段间潜在的交互问题，并有把握地逐步推进这一重构。

## **立即体验**

此功能现已向所有用户开放。欢迎在[仪表板](https://dash.cloudflare.com/account/workers-and-pages)中试用，或查阅 [Cloudflare Access for Workers 文档](http://developers.cloudflare.com/workers/configuration/cloudflare-access/)以开始使用。

## **致谢**

感谢 Jesse Li、Brandon Strittmatter、Kyle Hiller、Kenny Johnson、Matt "TK" Taylor、Brendan Irvine-Broque、Yomna Shousha 以及 Mike Aizatsky 在工程与设计方面付出的努力，使这一功能得以实现！

]]>01M21WZCWR238E6M0R8TMDYYZ7互联网的日全食：冰岛、西班牙和葡萄牙的流量冲击https://blog.cloudflare.com/zh-cn/total-eclipse-internet-traffic-iceland-spain-portugal/ Wed, 09 Sep 2026 01:35:56 GMTCloudflare 的数据显示，2026 年 8 月 12 日发生日全食期间，Internet 流量受到了明显影响，路径从冰岛延伸至西班牙和葡萄牙，与日全食全食带走向一致。Radar互联网流量互联网趋势Cloudflare 的数据清楚显示，2026 年 8 月 12 日发生的日全食，沿着全食带路径，对冰岛至西班牙、葡萄牙的互联网流量造成了明显影响。

在如今低头看电子屏幕已成为日常习惯的年代，一个能让人们共同抬头仰望的自然现象显得尤为珍贵。8 月 12 日星期三，一场日全食从北大西洋掠过欧洲，途经冰岛、西班牙北部和葡萄牙，西欧其余地区也在接近当地日落时分迎来了深度的日偏食。这是二十年来首次横跨欧洲大陆的日全食，吸引了数百万人走到户外，亲眼见证月球运行至地球与太阳之间的壮观景象。

正如我们[在 2026 年世界杯](https://blog.cloudflare.com/2026-world-cup-internet-traffic/)以及 [2024 年上一次日全食期间](https://blog.cloudflare.com/2026-world-cup-internet-traffic/)所见，当发生如此大规模的事件时，网络行为会受到显著影响。在这篇博客文章中，我们将使用 [Cloudflare Radar](https://radar.cloudflare.com/) 数据，探讨互联网流量如何随着日月运行而发生变化。

## **互联网流量下降与日食最大遮蔽时刻完全吻合**

在上图中，我们以五分钟为单位，测量了日食当天受影响各个国家/地区的 HTTP 请求量，并将其与正常日基准进行了比较。每一行代表一个国家（阿拉斯加除外）/地区，每一列代表 2026 年 8 月 12 日（日食当天）的五分钟时段。图中各个国家/地区按其日食发生的先后顺序排列 。

黑色菱形标记代表日食最大遮蔽时刻，颜色则表示 HTTP 流量相对基准的百分比变化（红色 = 低于正常，蓝色 = 高于正常）。我们可以非常清楚地看到，黑色菱形几乎完美叠加在最深的红色区域之上，这表明随着日食加深，**互联网流量随之下降** 。沿着全食带及日偏食最深的国家（冰岛、爱尔兰、英国、法国、西班牙和葡萄牙），流量下降最为显著；而在太阳几乎未被遮蔽的地区（瑞典、丹麦、波兰、瑞士），流量几乎未见变化。

在日食最大遮蔽区域，红色深度与黑色菱形相互映照：当遮蔽率达到峰值时，流量陷入低谷； 在太阳重新出现后迅速回升，因为通常在食甚 （太阳被遮蔽最多） 后数分钟内，随着人们重新回到屏幕前，流量恢复正常。

  
上方的散点图显示，这些流量下降并非出于偶然。每个数据点代表一个国家/地区的太阳最大遮蔽率（x 轴）对应该地区的流量下降幅度（y 轴）。流量下降幅度以日食最大遮蔽时刻前后 15 分钟窗口内的流量相对于基准的 平均百分比变化来衡量。图中 虚线的下降趋势表明，**日全食路径沿线区域流量降幅约为 15% 至 30%，而仅经历浅度日偏食的区域流量降幅小得多，** 甚至未见下降。尽管人口密度、当地时间和云量等局部因素会导致特定覆盖水平的数据出现波动，但总体趋势仍保持一致。 结合流量下降的精确时间点，数据趋势表明，日食本身是此次流量下降的主要原因 。

## **冰岛、西班牙和葡萄牙的流量降幅最大**

上图呈现各个国家/地区的流量 趋势线。灰色三角形代表日食遮蔽率的进程，红色线条则追踪流量相对于正常基准的变化量。在几乎所有受日食影响的国家和地区，流量均出现了显著变化，降幅介于 9.3% 至 -46.7%。

"y2"轴右侧的数字代表遮蔽率，根据太阳与月球的精确位置计算得出。我们针对每个地点，找到了太阳与月球的视直径以及二者的圆心距，然后通过两圆的几何重叠计算出每 5 分钟太阳圆面被月球遮蔽的比例。这样便可得出每个地点的最大遮蔽率（即日食深度，0–100%）及食甚时刻。随后，我们汇总每个国家/地区各区域的流量得到总和，并取各区域遮蔽率的平均值，以此确定每个国家/地区的食甚时刻。

为了将日食的影响与普通的周三晚上区分开来，我们将日食当天与之前三个周三的中位数进行了比较并逐个时段比对。使用中位数可以避免单周数据对比较结果造成偏差。所有数字均以相对于基准的百分比变化表示。在左侧 y 轴上，0% 表示"完全正常"，负值则表示"低于平常水平"。

我们可以看到，流量变化大约从 UTC 15:35 开始出现在阿拉斯加，即日食路径的起点。冰岛、西班牙和葡萄牙的流量降幅最大，而波兰和丹麦的流量则迅速恢复至日食前水平。挪威和瑞典的流量实际上略高于基准，而丹麦的总体变化最小。

最终，这些结果揭示了日食路径与人类网络行为之间存在明显关联。虽然流量下降的严重程度和持续时间因区域而异，但 Cloudflare Radar 的 HTTP 流量数据表明，一个共享的物理事件如何暂时重塑整个大洲的数字活动。

## **通过 Cloudflare Radar 追踪世界大事对网络流量的影响**

现实世界中的重大事件提醒我们，数字流量本质上是人类注意力的直接反映。当月球在欧洲各地遮蔽太阳时，互联网速度下降并非因为网络故障，而是因为人们暂停了网络活动去观看日食。随着日食过后网络流量迅速恢复正常，留下的数据为我们提供了一个引人入胜的视角，展现了一场宇宙奇景如何瞬间重塑网络世界。

如需探索更多互动式流量见解，并追踪重大世界事件如何影响每日互联网活动，请访问 Cloudflare Radar 或在社交媒体上关注我们：@CloudflareRadar (X)、noc.social/@cloudflareradar (Mastodon)，以及 @[radar.cloudflare.com](http://radar.cloudflare.com) (Bluesky)。

]]>01M21WHVZTWP256DPQM7SC3SCC为什么我们无法坐等更优秀的后量子签名算法出现https://blog.cloudflare.com/zh-cn/ml-dsa-will-have-to-do/ Tue, 25 Aug 2026 09:15:26 GMT美国国家标准与技术研究院 (NIST) 正在推进九种新的后量子签名算法，作为未来标准化的潜在候选方案。我们仔细研究了所有这些算法，并且认为，虽然这些算法正在研发中且展现出巨大的潜力，但我们应该立即使用 ML-DSA，这是目前可用的最佳算法。后量子安全密码学研究RSA 和 ECC 是人们几十年来一直依赖的加密算法，但它们[容易受到](https://blog.cloudflare.com/the-quantum-menace/)足够先进的量子计算机攻击。这种量子计算机目前尚不存在，但它们似乎会比预期出现得[更早](https://scottaaronson.blog/?p=9718)。幸运的是，已有可用解决方案：迁移到 ML-KEM 加密并使用 ML-DSA 签名，二者的设计用途是抵御量子攻击。经过八年的公开国际竞争，美国国家标准与技术研究院 (NIST) [在 2024 年](https://blog.cloudflare.com/nists-first-post-quantum-standards/)已将它们标准化。

向后量子加密技术的迁移正全面展开。在撰写本文时，Cloudflare 处理的大部分流量已采用 ML-KEM 加密，因此，能够防范对数据构成威胁的[先收集后解密](https://en.wikipedia.org/wiki/Harvest_now,_decrypt_later)攻击。但加密只是问题的一部分：为了完全防范能够破解经典密码技术的量子计算机，我们的目标是部署后量子签名，保护身份验证系统免遭未经授权的访问。我们[的目标是 2029 年](https://blog.cloudflare.com/post-quantum-roadmap)实现 Cloudflare 全面后量子安全。

ML-DSA 是目前最全面的标准化后量子签名技术方案，但也存在一些缺点：传输中的数据量大得多，而且我们过去在 RSA 和 ECC 中使用的许多[技巧](https://github.com/fancy-cryptography/fancy-cryptography)在 ML-DSA 中无法实现。更优秀的后量子签名方案仍在不断出现：上个月，NIST [宣布](https://groups.google.com/a/list.nist.gov/g/pqc-forum/c/LXoTAe5AN78/m/ZXgBCNlgDAAJ)将推动九个后量子签名方案进入“[签名准入计划](https://csrc.nist.gov/projects/pqc-dig-sig)”第三轮。此外，从上一轮竞争中脱颖而出的 [FN-DSA](https://falcon-sign.info/)（原名 Falcon）标准草案预计很快就会发布。

Cloudflare 一直以来非常关注后量子签名算法取得的进步，并在 [2021](https://blog.cloudflare.com/sizing-up-post-quantum-signatures/)、[2022](https://blog.cloudflare.com/nist-post-quantum-surprise/)、[2024](https://blog.cloudflare.com/another-look-at-pq-signatures/) 和 [2025](https://blog.cloudflare.com/pq-2025/#signatures-on-the-horizon) 年撰写了相关文章。在这篇博客文章中，我们将详细介绍最新进展。

但是，我们首先必须正视一个显而易见问题：这些新的签名算法无法及时完成后量子过渡，甚至差得很远，下文将会详述。问题来得太快，我们无法坐等。ML-DSA 目前已可用，将用于首次迁移。正如 Eric Rescorla 在 2024 年[所写](https://educatedguesswork.org/posts/pq-emergency/)：

> 你只能用现有的算法去打仗，而不是你原本期望拥有的算法。

尽管如此，出于多种原因，寻找更优秀的后量子签名算法至关重要，我们坚信这仍然是充分利用 NIST 有限资源的做法。

让我们一起详细了解一下这些签名算法。然后，我们将探讨它们的可用时间表，以及我们仍然需要它们的原因。

# 签名算法

在下表中，我们对进入第三轮的候选签名算法（标记为 🤔）、易受量子攻击的经典算法（标记为 ❌），以及已经标准化 (✅) 或即将标准化的后量子算法 (📝) 进行了比较。每种候选签名算法提出了多个变体。我们列出了与 TLS 最相关的变体，TLS 是用于保护互联网连接的协议。若要查看所有变体，请访问 [Thom Wiggers](https://thomwiggers.nl/) 的[签名库](https://pqshield.github.io/nist-sigs-zoo/)。

关于此表的补充说明：大多数候选签名算法在每个安全级别都有多个变体。我们展示了 128 位安全级别（安全黄金标准）上与 TLS 最相关的变体。CPU 时间取自 2026 年 6 月的[签名库](https://pqshield.github.io/nist-sigs-zoo/)，该库收集了第二轮提交文档及后续进展的数据。允许更改第三轮的候选签名算法，这将会影响上表涉及的数字。有些算法会改进（计算能力和规模），另一些算法则会退步，以应对新的攻击。请查看签名库，获取最新数据。我们用 ⚠️ 标记了 FN-DSA 和 SQIsign 签名算法，因为两者都很难以快速且[时序侧信道安全](https://blog.cloudflare.com/kyber-isnt-broken/#side-channel-attacks)的方式实现。LMS 签名算法也标记了 ⚠️，因为安全的 LMS 签名需要在签名过程中保持状态，而且列出的签名时间假设使用 32MB 缓存。SLH-DSA 签名算法的 128-24 变体标记了 ⚠️️，因为其设计旨在生成少于 224 个签名。

## 没有“全明星”算法

显而易见的一点是，虽然 Ed25519 椭圆曲线签名算法容易受到量子计算机攻击，但它无疑是最全面的方案（暂且忽略其易受量子攻击）：它在几乎所有指标方面的表现最佳，包括公钥大小、签名大小和签名时间。仅在验证时间上略逊一筹，但对于绝大多数应用来说，其速度已绰绰有余。

这与后量子签名算法列表截然不同。后量子签名算法列表不使用单一的“全能型”算法，而是将签名方案大致分为两类：一类是专业算法，它们在某些指标方面的表现接近可靠的椭圆曲线特征，但在其他指标方面存在问题，这使得它们在合适的部署场景下表现出色。其次是通用算法，例如 ML-DSA，虽然其所有指标方面的表现都不如椭圆曲线，但就缺点而言，它们的整体表现相当均衡。

## 专业算法

我们先来了解一下专业算法。

### SQIsign：签名小/签名速度慢

如果只看传输的字节数，**SQIsign** 看起来几乎可以完美取代椭圆曲线加密技术。它的签名大小为 148 字节，公钥大小为 65 字节，优于 RSA-2048。遗憾的是，天下没有免费的午餐：SQIsign 有三个弱点。首先，它是所有算法中最复杂的算法。其次，它的签名生成和验证速度相当慢。最后，它很难以时序侧信道安全的方式生成签名，而且这样做会产生一些性能损失。

目前看来情况不太乐观，但更糟糕的是：当我们[回顾 2024 年](https://blog.cloudflare.com/another-look-at-pq-signatures/#sqisign)，当时还没有任何时序侧信道安全的实现，签名验证速度也慢了 20 倍。此外，方案简化方面也取得了可喜的进展。

虽然取得了这些显著的改进，但在可预见的未来，（侧信道安全）签名的速度可能仍不足以用于典型的 _在线_ 场景，例如 TLS 握手。然而，对于 CA 签名或 DNSSEC 等 _离线_ 场景，验证时间比签名时间更重要，在这种情况下，SQIsign 或许可以派上用场。

但我们真正应该讨论的主题是安全性。SQIsign 基于[同源](https://blog.cloudflare.com/sidh-go/)。众所周知，基于同源的另一种算法 SIKE 在 NIST 首届后量子加密技术竞赛（该竞赛实现了 ML-DSA 标准化）的后期阶段遭到[严重](https://eprint.iacr.org/2022/975.pdf)破解。SIKE 经常被提及，作为后量子加密技术可能突然失效的警示案例。这需要一些细致入微的分析。首先，人们当时就已经对 SIKE 的安全性表示担忧，尤其是导致其被破解的 _挠点_ 。由于这些担忧，SIKE 没有入选标准化项目，而是被推迟到额外的[评估轮次](https://nvlpubs.nist.gov/nistpubs/ir/2022/NIST.IR.8413-upd1.pdf)，之后才被破解。（事实上，这正是 NIST 流程有效运作的一个实例。）SQIsign 不使用挠点，因此，没有像 SIKE 那样的类似担忧。

另一个值得注意的安全特性是，针对 SQIsign 最著名的攻击是通用暴力破解，就像针对精心选择的椭圆曲线的经典攻击一样。这与 RSA、格加密和多元加密大不相同，其攻击算法一直在缓慢改进，进而导致密码学家不断增加参数来构建更大的签名。尽管如此，同源算法背后的数学原理非常复杂，与其他算法相比，它存在很多 _数学攻击面_ 。不过，它的安全性似乎仍然比我们稍后将讨论的结构化多元算法更可靠。

SQIsign 是一种极具潜力的算法。过早地将其标准化实属可惜。我们想与各位作者分享以下几点：

  * 理想情况下，验证时间应该进一步缩短，即使这会影响签名时间和签名大小：SQIsign 签名已经足够小，而且离线签名时间也有一定的余量。
  * 如果能够进一步缩短签名时间，则时序侧信道安全实现应成为默认选项，因为这可能会吸引一些在线签名应用。
  * 但最重要的是，我们希望 SQIsign 能够得到简化。



### UOV：签名小/公钥大

**UOV** （非平衡油醋）是一种经典的多元签名算法，最初于 1999 年提出。它的签名很小：只有 96 字节。但代价是什么？巨大的公钥：66kB。这对 TLS 服务器证书来说没什么用，因为其公钥在建立连接时通过网络传输；但对于公钥预先分发的情况会有所帮助。

以 WebPKI 为例。一个典型的浏览器信任大约一百个根证书和 30 个证书透明度日志，如果使用 UOV，其公钥大小总计约为 8MB。

由于根证书通过带外方式传输给客户端，因此，一种想法是在那里使用 UOV 签名。但这并不是轻而易举的事情；由于 UOV 根证书体积较大，如果将其用作中间证书，则进行交叉签名是不切实际的。同时，对于任何更大的后量子签名，交叉签名和中间证书的吸引力都会降低。这促使更多根证书包含在客户端中。这再次有利于 UOV，但仅限于一定程度：如果根证书数量增长到超过一千个，我们将处理超过 66MB 的密钥材料，这会占据浏览器下载大小的很大一部分（例如，Firefox 151 的下载大小为 90MB）。

**多元算法安全性**

那么，安全性如何？多年来，人们提出了许多 UOV 变体，这些变体利用一些额外的数学结构来减小公钥的大小。这些 _结构化多元_ 方案的安全性记录并不稳定，例如 [Rainbow](https://eprint.iacr.org/2022/214) 和 [GeMMS](https://eprint.iacr.org/2021/1677) 等方案都曾被严重破解。区分这些与 UOV 本身至关重要，UOV 的安全性记录好得多，但并非完美无缺。

与许多加密方案一样，UOV 在早期也经历了成长的阵痛，因为人们发现了各种基本攻击和参数化陷阱。事实上，UOV 中的“U”正是这种阵痛的残余，它代表 _不平衡_ ，这反映了对 1997 年油醋方案（UOV 的基础）中一个参数设置错误的修正：原始方案在用作公钥的二次方程组中， _油_ 和 _醋_ 的变量数量相等，这最终导致了[攻击](https://weizmann.elsevierpure.com/en/publications/cryptanalysis-of-the-oil-and-vinegar-signature-scheme-2/)的发生。如果您对这个有趣的名称感到好奇，不妨这样想：方程组包含醋 × 醋项以及油 × 醋项，但不包含油 × 油项。它就像是就像油醋汁里分散的小油滴。回顾其历史沿革：从 2005 年到 2020 年，多元签名技术处于相对平静期：人们对 UOV 的理解不断加深，但针对典型参数的攻击却鲜有出现。

随着 _交集攻击_ 的[发现](https://eprint.iacr.org/2020/1343.pdf)，这种情况在 2020 年发生了改变。交集攻击基于最初针对平衡油醋攻击的思路。它移除了当时提议的 128 位参数集中大约 30 位安全性。这是一个相当大的打击，但不致命：稍微调整参数即可彻底缓解攻击，只需略微增加密钥和签名大小。

更大的冲击是 2025 年[发表](https://eprint.iacr.org/2025/1143.pdf)了利用[ _楔形_](https://en.wikipedia.org/wiki/Exterior_algebra)攻击多元签名方案的概念。对 UOV 的初步影响很小：只有几比特（也是在 128 位安全级别）。人们担心的是，这个概念突然出现，而且不清楚这种方法可能会应用到什么程度。这种担忧在一定程度上是合理的：楔形攻击的构想很有成效，之后出现了几次基于此的攻击，导致安全性降低了约 15 位。然而，我们逐渐[意识](https://eprint.iacr.org/2026/298)到，楔形攻击及其推广可被视为现有攻击的特例，例如截断环上的 _交集攻击_ ，因此，它比想象的要常见得多。同样，只需略微增加密钥和签名大小即可缓解这些攻击。

如何理解这一切呢？这类攻击历史并不罕见：在过去 25 年里，虽然近年来有所缓和，但格加密的安全性已显著降低。尽管如此，目前生产环境中部署的格加密仍然使用远高于 128 位的保守参数集，以防范未来的密码分析。我们也希望对 UOV 采取同样的做法。签名大小仅随安全级别线性增长，即使在 256 位安全级别也只有 260 字节。遗憾的是，公钥大小与安全级别呈立方关系：256 位的公钥大小为 446kB。UOV（如同大多数多元加密方案一样）可以灵活地选择不同中间安全级别的参数集，非常方便。

UOV 是一种基础加密方案，虽然应用场景不多，但却实用可行。展望未来，我们希望看到一个参数集，其长度略超过 128 位，例如 160 位，以应对未来可能的密码分析技术改进。

### QR-UOV：签名小/公钥大

与下文将讨论的 SNOVA 和 MAYO 类似，**QR-UOV** 是一种结构化多元签名方案：它是一种 UOV 变体，通过为公钥添加更多结构来减小其大小。但改进效果有限：最理想的情况下，公钥大小为 12kB，但对于该参数集，签名验证速度非常慢，更实际的参数集从 24kB 公钥开始。

就安全性而言，QR-UOV 是唯一无需调整其原始（第一轮）参数，即可应对新攻击的多元签名方案。这有点出乎意料，因为任何针对 UOV 的攻击也同样适用于 QR-UOV。原因在于这些攻击确实存在，但 QR-UOV 的自然参数恰好使其失效。另一方面，已知有几种攻击利用了 QR-UOV 添加的特定额外结构：事实上，对于某些参数集，针对特定结构的攻击是最优攻击。这与 MAYO 形成鲜明对比，目前尚无针对 MAYO 添加的额外结构的已知攻击。（本文后续部分会论述 MAYO 和 SNOVA。）

与上一轮相比，QR-UOV 的签名和验证时间显著缩短，但仍然相对较慢。总而言之，QR-UOV 难以推广：它为 UOV 增加了可被漏洞利用的结构，但并没有将密钥长度降低到通用长度。

### 基于哈希函数的签名

**基于哈希函数的有状态签名**

最早标准化的后量子签名算法是基于哈希函数的有状态 [LMS、HSS](https://www.rfc-editor.org/rfc/rfc8554.html) 和 [XMSS(MT)](https://datatracker.ietf.org/doc/html/rfc8391)。它们的公钥非常小，而且对于许多参数集，其签名比 ML-DSA-44 的签名小得多。此外，它们的安全性基于哈希函数，这已为人熟知且是加密技术的基础。这使得基于哈希函数的签名算法成为一种非常保守的选择，无需通过提高安全级别来规避风险。

那么，有什么陷阱呢？

有两个问题。一个重要问题是保持同名状态。这些基于哈希函数的有状态签名方案由一次性签名密钥构成，密钥被收集到默克尔 (Merkle) 树中。签名者必须跟踪哪些一次性签名密钥已被使用，这很简单，通过计数器就能完成。但是，如果签名者出了错，不小心在不同消息中两次使用了同一个一次性签名密钥，则任何人都[可能](https://eprint.iacr.org/2016/1042)利用这两个签名在任何消息中创建自己的签名。要保持正确的状态，需要考虑很多因素。一些注意事项：确保在分发签名之前将更新写入存储；不希望从备份中恢复旧状态；如果没有就如何拆分或保持状态达成一致，则无法将私钥从一个地方导出/导入到另一个地方。正如几年前 Adam Langley [指出](https://www.imperialviolet.org/2013/07/18/hashsig.html)的那样，状态隐藏着巨大的陷阱。

另一个缺点是，即便是最具有竞争力的参数集，也只能生成数量有限的签名。如前文表中所示，1112 字节的签名只能生成大约一百万个签名。您可以使用[计算器](https://westerbaan.name/~bas/hashcalc/)来权衡各种因素。

综上所述，基于哈希函数的有状态签名应用范围非常有限：签名者必须能够保持状态；签名大小必须是一个实际真正考虑的问题；以及签名者必须接受签名数量的硬性限制。

**SLH-DSA：保守的安全性/大型且缓慢**

**SLH-DSA** 是一种基于哈希函数的签名技术，它没有签名数量限制，并且避免了保持状态的问题。基本理念是生成足够多的一次性签名密钥，以便可以随机选择一个密钥，而不用担心重复使用，因为两次选到相同密钥的概率会递减。SLH-DSA 的效率略微更高，因为它用多次签名密钥替换了一次性签名密钥作为构建模块，即使因密钥偶尔被重复使用导致安全性温和地降低。它仍然需要付出一定的代价。SLH-DSA 有两个变体，一个优化签名大小，另一个优化签名速度。优化后的签名大小达到 8kB，并不小；而优化后的签名速度甚至比 SQIsign 更慢。

SLH-DSA 的签名变体更少

NIST 已[提议](https://csrc.nist.gov/pubs/sp/800/230/ipd)为 SLH-DSA 标准化一个额外的参数集，它可以生成更小的签名，但只能生成大约 1600 万个签名，超过这个数量后安全性会降低。但这个签名的大小为 3.8kB，仍然比 ML-DSA-44 的签名大，不过公钥和签名的组合大小非常接近。选择该参数集是为了提高签名验证速度，但以牺牲签名时间为代价。签名时间确实非常慢。

**应用场景**

那为什么还要使用 SLH-DSA 呢？它的优势在于其保守的安全性。对于难以替代的长期可信密钥，如果应用能够接受标准化变体较大的签名大小和较慢的验证速度，或者接受新提议变体较慢的签名速度，则使用 SLH-DSA 是合理的。还有两点需要注意。首先，最好将密钥算法设计成不会“烧录”在系统中，而是可以事后替换。其次，在大多数情况下，系统（例如使用 TLS 的安全连接）不仅依赖于签名，还依赖于密钥协商。目前没有基于哈希函数的密钥协商机制，因此，我们最终还是需要信任一些不那么保守的机制，例如格。

### FN-DSA：小密钥和签名/精妙的签名

从数据上看，FN-DSA-512（原名 Falcon）几乎在所有指标方面的表现都远胜于 ML-DSA-44：验证速度更快、公钥更小、签名也小得多，仅为 666 字节。签名速度虽然慢了三倍，但仍然比 RSA-2048 快 25 倍。更重要的是，它已被选为 FIPS 206 标准。那么，为什么我们不把 FN-DSA 视为通用算法呢？

这是因为安全地实现 FN-DSA 签名非常困难。FN-DSA 最显著的优势是，使用硬件加速的[浮点运算](https://en.wikipedia.org/wiki/Floating-point_arithmetic)完成最自然、高效的实现。这在加密标准中尚属首次。一个重大挑战是，我们缺乏在不泄露侧信道的情况下，安全实现快速浮点运算的经验。据我们目前所知，这种方法比较精妙且不太稳健：在一个处理器上使用浮点单元 (FPU) 实现的 FN-DSA 签名方案，在其他处理器上可能并不安全。与其依赖 FPU，不如模拟浮点运算。虽然这种方法更容易实现，但速度慢大约 20 倍，与 RSA-2048 的速度差不多。最近在使用定点运算安全地实现 FN-DSA 签名方面取得了一些令人欣喜的[进展](https://github.com/fixed-point-fndsa/fxp-falcon-py)，这比浮点模拟快得多。那么只需使用定点运算，就可以放心使用 FN-DSA 了吗？这种假定预设了用户对相关问题的认知水平，而这种认知水平可能并不合理。在会议上，我们经常看到演讲者在基准测试中比较后量子签名算法（包括 FN-DSA）时，他们无法回答是否使用了浮点模拟。

使用浮点运算的另一个后果是，难以生成用于签名的测试向量。一个例子是，只能保证 _a+(b+c)_ 和 _(a+b)+c_ 的结果接近，但并不完全相同。这意味着，为了获得有效的测试向量，FN-DSA 规范需要非常精确地定义浮点运算的顺序。另一个例子是 _a*b+c_ ，可以通过两个步骤计算（先乘后加），或者使用[融合乘加](https://en.wikipedia.org/wiki/Multiply%E2%80%93accumulate_operation) (FMA) 一步完成。后者速度更快，但由于只进行一次舍入，因此，给出的答案略有不同。并非所有处理器都支持 FMA，但对于那些支持 FMA 的处理器，编译器通常会自动使用 FMA 来提升性能。同时，一些数学优化也会带来问题。例如，参考实现使用[帕塞瓦尔定理](https://en.wikipedia.org/wiki/Parseval%27s_theorem)，以更快速的迂回方式计算一个值（范数）。从数学上讲，答案是完全相同的，但由于浮点数只是近似值，结果会略有不同。同样，安全的定点运算实现也会产生略微不同的结果。

为什么这是个问题？因为在实践中，仍然只有简单的测试向量才能捕获大多数实现错误。其他更精细的方法，例如形式化验证，当然可以捕获更多错误，但测试向量的简洁性难以匹敌。

没有固定实现方式的另一个令人惊讶的优势如下。通过两个由略有不同的实现方式使用同一私钥生成的确定性签名，可以[推导出部分私钥](https://eprint.iacr.org/2024/1709)。FN-DSA 不使用确定性签名，而是添加了一个随机函数生成器来避免这种情况。测试中存在一个矛盾：需要一个确定性的接口来测试签名，但又不希望它被用于生成实际的签名。

如何处理 FN-DSA 规范中的回旋余地无疑将成为讨论的重点。不同实现之间的差异或许也有其积极的一面：NIST 可以决定使用定点算法实现来生成测试向量 ([CAVP](https://csrc.nist.gov/projects/cryptographic-algorithm-validation-program))。风险更高的浮点实现无法通过测试向量，这反而是一种优势而非缺陷，因为它会引导实现转向更安全的定点版本！

您可以阅读[这篇博客文章，](https://keymaterial.net/2026/05/13/so-you-want-to-deploy-fn-dsa/)了解一些其他有趣的细节。抛开具体细节不谈，关键在于 FN-DSA 本身就是一个复杂的方案。不难想象，NIST 花了[几年时间](https://csrc.nist.gov/csrc/media/presentations/2025/fips-206-fn-dsa-\(falcon\)/images-media/fips_206-perlner_2.1.pdf)（还不包括目前的停滞期）撰写草案标准，这并不令人意外。最终标准的发布以及添加支持的密码库所需的时间将比平常更长。FN-DSA 的发布比看起来晚得多。我们将在本文稍后部分比较时间表。

如果这些数字仍然非常诱人，那么还有最后一点需要注意：FN-DSA-512 的参数化安全级别为 128 位，而 ML-DSA-44 的安全级别为 160 位。如果格加密技术有所改进，则没有中间安全级别：下一个级别将直接达到 256 位的 FN-DSA-1024。FN-DSA-1024 的密钥和签名大小、签名时间和验证时间均为 FN-DSA-512 的两倍。FN-DSA-1024 签名大小仍然是 ML-DSA-44 签名大小的一半，但 _公钥+签名_ 的大小仅相差约 20%。

在结束对 FN-DSA 的讨论之前，需要强调的是，FN-DSA 的所有难点都在于签名方面：FN-DSA 签名的验证非常简单。 

## 通用算法

现在我们来看一看那些旨在作为 ML-DSA 替代方案的通用算法。

### HAWK

**HAWK** 是个有趣的示例。它在许多方面与 FN-DSA 类似：是一种结构化格哈希然后签名方案，签名和公钥的大小相近，但缺少中间层安全级别。与 FN-DSA 相比，HAWK 的主要优势在于签名速度极快，且不使用浮点运算，虽然它本身也不是一个简单的算法。这带来了一个需要权衡的问题：HAWK 基于并引入了一个新的安全假设，即 _格同构问题_ (LIP)。2024 年，也就是 HAWK 推出两年后，人们发现，在全实数域的特殊情况下，[容易解决](https://eprint.iacr.org/2024/441)该问题，但 HAWK 或任何其他加密算法均未使用全实数域。2025 年，这种攻击已[扩展](https://eprint.iacr.org/2025/280.pdf)到更广泛的数域类别。虽然目前尚未针对 HAWK 发起攻击，但这种情况正在逐渐逼近。2026 年 6 月[发表](https://eprint.iacr.org/2026/1318.pdf)的一篇新论文指出，存在一种将这种攻击扩展到 HAWK 的方法。该论文中发现了一个错误，但目前尚不清楚错误对该方法的影响程度。无论如何，这种发展趋势令人担忧。

即使不考虑潜在攻击，HAWK 也面临一些阻力：其额外的安全假设使其无法取代 FN-DSA，但其实际优势（尤其考虑到缺乏中间安全级别）不及结构化多元方案。它也没有增加安全假设的多样性，而这正是 NIST 所期望的结果。

### 知识证明方案

FAEST、MQOM 和 SDitH 的整体结构相似。它们的公钥是某个难题的实例，而私钥是该难题的解。

  * **FAEST** 公钥是使用私钥对已知明文进行 AES 加密的结果。
  * **MQOM** 的名称来源于多元二次问题，该问题与多元方案的加密假设密切相关（但更加保守）。公钥是一个二次方程组，私钥是该方程组的解。
  * **SDitH** 基于随机线性码的故障译码的特定数学难题。这个问题与最初提交给 NIST 竞赛的基于码的方案相关，但这些方案在第三轮均被淘汰。



在所有情况下，签名都是一个[零知识证明](https://en.wikipedia.org/wiki/Zero-knowledge_proof)，表明签名者知道该难题的解，同时（几乎是顺带地）承认待签名消息也是证明的一部分。

许多签名方案在底层都采用了这种零知识证明，尤其是 ML-DSA、SQIsign 和 Ed25519。我们为什么不把它们也归入 _知识证明_ 方案呢？

区别在于普适性：用于 ML-DSA 的[零知识证明](https://blog.cloudflare.com/lattice-crypto-primer/#warm-up)只能证明 ML-DSA 中使用的特定 LWE 问题：证明利用了密钥中的数学结构。虽然有[方法](https://eprint.iacr.org/2022/1341.pdf)可以使用格创建零知识证明来验证任何常规陈述，但这些证明体系与 ML-DSA 截然不同，并且会生成大约 50kB 的较大签名。

相比之下，FAEST、MQOM 和 SDitH 使用的证明体系可用于证明任意陈述。例如，可以修改 FAEST，使其使用 MQOM 难题。这便产生了一种更高效的方案，称为 [KuMQuat](https://eprint.iacr.org/2024/490.pdf)。（稍后我们将讨论一些性能数据。）反之，MQOM 也可以进行调整，使用 AES 作为难题。

这种灵活性有两个好处。首先，它不需要难题具有任何特定数学结构，因此，我们可以选择一个非常保守的难题，例如破解 AES。有些难题比其他难题更容易产生高效的签名，就像我们在 MQOM 中使用的 MQ 一样。MQ 仍然是一个相当保守的假设：它不包含 UOV 中使用的隐藏子空间，因此，也不包含其他多元签名。交集攻击或楔形攻击都不适用。事实上，二次方程组属于 NP 难计算问题。为了确保安全，仍然需要选择合适的问题规模，尽管已研究 MQ 问题相当长一段时间，但它显然没有像 AES 等已部署的算法那样受到严格的审查。

第二个更重要的优点是，我们能够根据通用的零知识证明体系创建远不止简单的签名方案：我们可以创建[盲签名](https://eprint.iacr.org/2026/109.pdf)，甚至是功能齐全的匿名凭证。

这里需要注意一个限制：这三种方案的证明规模都会随着被证明的陈述线性增长。从技术角度上讲：它们不像 [STARK](https://aszepieniec.github.io/stark-anatomy/) 和 [LaBRADOR](https://eprint.iacr.org/2022/1341.pdf) 那样 _简洁_ ，后者在处理大规模陈述时远远胜于它们。这再次说明，有时选择渐近意义上并非最优的方法反而更好。

回到优势：除了所选的难题和哈希函数的安全性之外，这三种方案不需要任何其他安全假设。这使得 FAEST 与 SLH-DSA 一样保守。

那么除了选择的难题之外，它们之间还有什么区别？这些方案的初始设计截然不同，但自第一轮以来一直在改进和趋同。MQOM 中的证明体系比 FAEST 略微简单一些，但其性能也逊色一些：[KuMQuat](https://eprint.iacr.org/2024/490.pdf) (FAEST+MQ) 的性能优于 MQOM。

谈到性能，我们先与 SLH-DSA 进行比较。这三种方案都有一些变体，其性能优于任何标准化 SLH-DSA 参数集，而且通常优势显著。SLH-DSA 的确有一个明显的优势：验证例程更容易实现。

与 ML-DSA-44 相比，则更有意思。所有方案在运行时间和签名大小之间实现了丝滑的权衡。例如，以下是 KuMQuatt (FAEST+MQ) [报告](https://eprint.iacr.org/2024/490.pdf)的权衡，验证时间与签名时间接近。

KuMQuat 可以通过参数化实现比 ML-DSA-44 更小的签名，代价是签名（和验证）运行时间较长。另一方面，它可以实现与 ML-DSA-44 类似的签名时间，代价是签名更大，不过公钥和签名的总大小仍然相似。

这些方案多年来已显著改进，我们预计未来还会进一步改进。虽然它们对 ML-DSA 的改进不如其他一些方案那么显著，但它们保守的安全性，尤其是在匿名凭证等更广泛应用方面的潜力，使它们极具吸引力。为了展示底层零知识证明系统的灵活性，我们希望此类别中的每个方案都展示它们在应对不同底层难题时的性能表现。

### 结构化多元签名：MAYO 与 SNOVA 的对比

如前文所述的类似 QR-UOV，MAYO 和 SNOVA 都是 UOV 变体，通过为公钥添加额外的结构来减小其大小。但 MAYO 和 SNOVA 采取两种不同的方法：SNOVA 采取激进的策略以获得最佳性能，而 MAYO 则采用保守的设计，谨慎行事。

SNOVA 的性能确实令人印象深刻。它的主要参数集使用 248 字节签名（比 RSA-2048 还小！），而公钥只有 1kB。在公钥+签名大小方面，它胜过所有其他后量子方案（除了 SQIsign 之外），并且运行时间也很短。

MAYO 的性能同样不容小觑。MAYOone 的验证时间最短，其 454 字节的签名仍然比 FN-DSA-512、HAWK-512 和 RSA-4096 的签名更小。如果加上其 1420 字节的公钥，MAYOone 确实略逊于 FN-DSA-512 和 HAWK-512。然而，如果考虑到更高的安全性，MAYO 再次脱颖而出。FN-DSA 和 HAWK 缺少中间安全级别，因此，需要提升到 256 位安全级别，而 MAYO 的精细化设计可以在略微增加公钥和签名大小的情况下，增加额外的安全性。

  
| **安全**| **公钥** | **签名**| **公钥 + 签名**  
---|---|---|---|---  
HAWK-1024| 256| 2,440| 1,221| 3,661  
FN-DSA-1024| 256| 1,793| 1,280| 3,073  
MAYO 在 174 位安全性| 174| 1,600| 550| 2,150  
  
如果这还不够好，MAYO 和 SNOVA 都允许在签名大小与公钥大小之间进行权衡。因此，对于预先传输的公钥，我们甚至可以获得更小的签名。如果将 MAYO 推向极致，它就变成了 UOV。

到目前为止，我们讨论的是性能。那么，安全性呢？MAYO 在 UOV 的基础上增加了一个“whipping”结构：任何针对 UOV 的攻击也适用于 MAYO，但可能存在针对 MAYO whipping 结构的特定攻击。到目前为止，尚未发现针对 whipping 结构（因此也包括针对 MAYO 本身）的攻击。最糟糕的情况是，由于 MAYO 的 UOV 参数选择是其固有特性，某些 UOV 攻击对某些 MAYO 变体的影响比典型的 UOV 参数集的影响更大。

这与 SNOVA 形成了鲜明对比。SNOVA 的特定结构曾多次遭受重创。为了应对这种情况，SNOVA 团队不仅调整了参数，而且还不断改变其实际结构。他们每次都会取得突破，提出性能更优的新版 SNOVA。我们[去年](https://blog.cloudflare.com/pq-2025/#the-fight-between-mayo-versus-snova)指出了这一点，而且这种模式仍在继续，而 MAYO 的基本设计保持稳定。

此外，SNOVA 使用的结构[可以](https://eprint.iacr.org/2024/1297.pdf)[被视为](https://eprint.iacr.org/2026/659) MAYO 使用的 whipping 映射的一种特殊形式。这意味着任何针对 MAYO 的攻击都适用于 SNOVA，但反之则不然。

总的来说，我们在理解多元安全性方面取得了长足的进步。NIST [指出](https://csrc.nist.gov/pubs/ir/8610/final)，他们预计在标准化多元方案之前还需要进行一轮额外的讨论。这似乎是谨慎的做法。目前，我们还不清楚 SNOVA 届时是否准备就绪，但 MAYO 目前看来已经相当成熟。

## 时间表

现在，让我们展望并设想一下这些新的签名算法何时能够投入使用。

### 目前 ML-DSA 的进展

ML-DSA 的进展情况值得我们关注。

2017 年 11 月| 提交至竞赛  
---|---  
2019 年 1 月| 进入第二轮  
2020 年 7 月| 进入第三轮  
2022 年 7 月| 入选标准化  
2023 年 8 月| 初步公开草案  
2024 年 8 月| NIST 最终标准  
2025 年 10 月| ML-DSA 证书标准 (RFC 9881)  
2025 年 4 月| OpenSSL 3.5.0 新增对 ML-DSA 的支持  
2025 年 8 月| Debian Trixie 发布，并支持 OpenSSL 3.5.0  
2025 年 12 月| ML-DSA 的 TLS IANA 代码点注册  
2026 年 3 月| 首个 ML-DSA 模块的 CMVP 认证  
2026 年 7 月（预计）| 混合 ML-DSA 证书标准  
2026 年 8 月（预计）| 供在 TLS 中使用 ML-DSA 的 RFC  
2027 年初（预计）| WebPKI 中首批 ML-DSA 证书可用  
  
NIST 选择了 Dilithium 作为 ML-DSA 后，用了一年时间起草标准提案，然后再花了一年时间才发布算法标准。算法标准还不够：协议需要就如何集成 ML-DSA 达成一致。证书的集成又花了一年时间。但这还没完：软件还需要添加对 ML-DSA 的支持，并将其集成到协议中。

这些步骤并非完全按顺序进行：ML-DSA 的软件实现工作在最终标准发布之前就已启动。此外，协议集成标准通常在最终标准发布之前就已经“完成”。例如，TLS 中的 ML-DSA 使用已经完成，但截至撰写本文时，相关的 RFC 规范还需要几个月才能发布。值得注意的是，OpenSSL 抢先一步，在 IANA 代码点分配之前添加了对 ML-DSA 的支持。目前仍未就 TLS 中应使用哪些混合签名（[或是否应该使用](https://keymaterial.net/2026/06/18/on-hybrid-signatures/)）达成一致意见，截至撰写本文时，IANA 尚未为这些混合签名分配代码点。

### 这些新的签名算法何时可以投入使用？

那么，新签名算法的未来发展方向是什么？如果 **FN-DSA** 草案今天发布，并且进展与 ML-DSA 相同，我们或许能在 2029 年初获得一些早期的软件支持，但不会有大量的部署。考虑到 FN-DSA 草案标准的编写耗时，最终标准、协议集成和软件支持的进展也可能较为缓慢。我们预计，FN-DSA 在 2033 年之前不会广泛应用。

关于**多元** 方案的密码分析进展令 NIST 感到担忧：他们表示，预计多元加密方案至少还需要再进行大约两年的相关研究。另一方面，多元方案相对容易实现。这意味着我们可能会在 2031 年看到 NIST 出台多元加密标准，而更广泛的产品应用最早也要到 2034 年。

与多元加密相比，NIST 对 **SQIsign** 的安全性更有信心。与 FN-DSA 类似，SQIsign 是一个难以标准化和实施的方案。同时，SQIsign 在简化方面取得了长足的进步。SQIsign 可能会在第三轮评估中做出重大改动，因此，需要进行第四轮评估。无论如何，在 2035 年之前广泛应用的可能性似乎不大。

如[上文](https://docs.google.com/document/d/1cpaUq1BcT1jRNE-V6oEV5szHC2HDDRfE3upTw6-zFgI/edit#bookmark=id.740pyrlsw8nt)所述，**HAWK** 处于 FN-DSA 与结构化多元签名方案之间的一个尴尬中间地带。即使在最近的密码分析取得进展之前，它的标准化似乎也不大可能实现，我们预计最早也要到 2034 年才会发布。

这样一来， _知识证明_ 算法就只剩下 **MQOM** 、**SDitH** 和 **FAEST** 。我们已经看到，这些方案在几轮迭代中取得了显著改进。如果保持这种改进速度，将需要进行新一轮迭代调整；但如果现在已经稳定，知识证明算法将成为 2030 年首个发布的 NIST 新标准。如果这么早发布，其性能可能不会显著超越 ML-DSA。尽管如此，它仍然非常适用于构建匿名凭证以及签名之外的其他基本功能。

那么，您是否应该等待这些签名签名算法发布之后，再推动后量子迁移？鉴于量子硬件和软件的最新进展，我们认为我们无法再等待。Cloudflare 的目标是[在 2029 年完成全面迁移](https://blog.cloudflare.com/post-quantum-roadmap)。但这些签名算法都无法及时发布。大多数监管机构设定的最后期限在 2030 年至 2035 年之间。这些期限并未考虑近期的进展，我们预计它们将会进行调整。我们看到 [2026 年 6 月美国行政令](https://blog.cloudflare.com/post-quantum-eo-2026/)将最后期限设定为 2031 年。即使最后期限没有改变，我们也不建议等待。

为什么？仅仅在 2035 年截止日期前的 2034 年部署后量子签名是不够的。任何合理规模的系统都无法一次性升级所有功能。您需要一个过渡期，在此期间同时支持后量子签名和传统签名。同时支持两者会导致降级攻击。防范此类降级攻击最直接的方法是禁用经典加密算法。这需要时间，而且坦白说，对于像 WebPKI 这样分布足够广泛的系统来说，这甚至不是一个可行的选择。我们将在未来的博客文章中介绍如何处理降级问题。如果您感兴趣，请阅读[此处](https://www.chromium.org/Home/chromium-security/post-quantum-auth-roadmap/)的一些资料。不管怎样，处理降级都需要时间。

显然，这些新的后量子签名算法无法在首次迁移之前准备就绪。为什么还要这样费心？

### 为什么我们仍然需要它们

人们已经用了 [50 年](https://ee.stanford.edu/~hellman/publications/24.pdf)时间将公钥加密技术融入整个数字社会。我们只剩下短短几年时间来使其实现量子安全。对于大多数此类升级，流程很明确：直接采用后量子密码技术。说起来容易做起来难：这是一个艰巨的任务。但有些情况从根本上来说更加困难。在后量子时代，不存在万能的签名，而且在某些情况下，ML-DSA 的规模大小是个问题。只要拥有足够的资源并获得利益相关者的同意，才可以重新设计系统，使其能够很好地处理这些更大的签名。事实上，得益于持续的重构，后量子时代的 WebPKI 正朝着[优于](https://blog.cloudflare.com/bootstrap-mtc)当前易受量子攻击的 WebPKI 的方向发展。期望所有系统在为时已晚之前都实现这一点是不现实的。一些系统将不得不接受性能上的损失。另一些系统则需要通过其他方式来应对安全漏洞，例如限制访问、隧道技术、加强监控，或者采取其他各种成本高昂的措施。一旦更小的后量子签名出现，就可以移除这些补偿性控制措施，从而恢复系统的效率和安全性。

  


NIST 竞赛的一个间接但同样重要的益处是，它有助于推动后量子加密技术超越其基本原语：并非只有密钥协商和签名易受量子攻击。还有许多在生产环境中使用的[ _高级_ 加密原语](https://github.com/fancy-cryptography/fancy-cryptography)，例如匿名凭证、PAKE 和阈值签名等。对于大多数人来说，后量子变体并不容易获得，或者认识不足。对于某些人来说，无需复杂的加密也能实现相同的目标，但代价是遗憾地在微妙的隐私目标上出现倒退。NIST 无法针对每一种特定的原语举办后量子标准定义竞赛，但幸运的是，签名竞赛在这方面提供了极大的帮助。

  


最明显的示例是 FAEST。虽然 FAEST 的设计初衷是作为签名方案，但其底层机制 (VOLEitH) 可与 MAYO 等多元方案搭配使用，从而创建高效的[后量子匿名凭证](https://www.usenix.org/system/files/conference/usenixsecurity26/sec26_prepub_baum.pdf)。如果没有签名竞赛，VOLEitH 不会像今天这样发展完善且经过充分验证。

许多候选加密签名方案简要介绍了其各自在签名之外的其他用途。我们希望看到更多此类方案的间接应用取得突出进展。

尽管未来将会出现更强大的签名和更先进的加密技术，但我们不应忘记眼前的任务：确保在不久的未来保持安全。

]]>5wMIF1Oa7DES2YNRpqiVB0Worker 现在可以在前端拥有其专属缓存https://blog.cloudflare.com/zh-cn/workers-cache/ Mon, 24 Aug 2026 06:00:43 GMT我们将推出 Workers Cache，这是一个区域分层缓存，它直接位于您的 Worker 前端。可无限组合，通过标准 HTTP 标头进行配置。Cloudflare WorkersTiered Cache开发人员性能无服务器缓存今天我们将推出 **Workers Cache** ：这是一个[分层缓存](https://developers.cloudflare.com/cache/how-to/tiered-cache/)，它位于您的 Worker 前端，只需一行 Wrangler 配置以及您已熟悉的 Cache-Control 标头即可进行配置。

启用 Workers 缓存后，所有发送到您 Worker 的[可缓存](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.3)请求都会首先命中 Cloudflare 的缓存。如果有最新缓存的响应，Cloudflare 会直接将其返回，您的 Worker 不会运行，您也无需为此支付 CPU 时间。如果未命中缓存，您的 Worker 会运行，如果响应可缓存，Cloudflare 会将其存储以备下一个请求使用。来自全球任何位置的下一个请求都可以直接从缓存中获取服务。

整个流程是一个配置块：

之后，您可以通过在响应中设置标头，以 HTTP 一直希望的方式控制缓存：

当内容发生变化时，Worker 会清除自己的缓存：

这就是整个 API。无需配置任何区域，无需设置任何规则引擎，无需提供单独的缓存，也无需登录任何其他产品。Worker 的代码就是配置界面，缓存会跟随 Worker 运行，无论它是在自定义域、`workers.dev`、在服务绑定后端、预览版还是[Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/) 租户中运行。一个 Worker，一个缓存，一次配置。

这只是表面层。底层技术非常强大：覆盖整个网络的分层缓存、完全支持 [stale-while-revalidate](https://developers.cloudflare.com/changelog/post/2026-02-26-async-stale-while-revalidate/) 以确保过期响应不会阻塞用户，通过 [Vary](https://developers.cloudflare.com/workers/cache/#content-negotiation-with-vary) 进行内容协商，通过 [ctx.props](https://developers.cloudflare.com/workers/runtime-apis/context/#props) 接收多租户安全缓存键，按标签或路径前缀进行程序化清除；以及我们认为最关键的一点，在每个 Worker 入口点前端设置缓存，不仅仅是公共入口点，并且可以针对每个入口点单独控制缓存哪些入口点，不缓存哪些入口点。最后一点意味着您可以将缓存直接集成到应用架构：这是一系列入口点，缓存阶段可以插入您所需的任何位置，由入口点两端的代码进行配置。我们将在下文详细介绍相关信息。

Workers 缓存现已面向任何 Cloudflare 计划中的所有 Worker 开放，并可通过 Wrangler 使用。

这是我们一直以来希望 Workers 拥有的缓存 API。下文将阐述我们为什么花了这么长时间才推出此功能，它带来了哪些可能性，以及未来的发展方向。

## 为什么服务器端渲染的应用需要前置缓存

我们在 2017 年[推出了 Workers](https://blog.cloudflare.com/introducing-cloudflare-workers/)，当时的营销用语是：您可以在 Cloudflare 网络上运行代码，在请求到达源服务器之前对其进行转换。Worker 位于缓存与源服务器的 _前端_ ：

这正是我们当时所针对的使用场景的理想模型。如果您想在每个请求中添加标头、重写 URL、进行 A/B 测试，或在流量到达源服务器之前过滤流量，则将 Worker 置于缓存与源服务器的前端，您就可以完全控制缓存哪些内容，不缓存哪些内容。客户利用它构建了许多令人惊叹的应用。

但局面很快发生变化。Workers 逐渐不再是附加在源服务器上的组件，而是成为了 _源_ 本身。[Astro](https://developers.cloudflare.com/workers/framework-guides/web-apps/astro/)、[TanStack Start](https://developers.cloudflare.com/workers/framework-guides/web-apps/tanstack-start/)、[Next.js](https://developers.cloudflare.com/workers/framework-guides/web-apps/nextjs/)、[Remix](https://developers.cloudflare.com/workers/framework-guides/web-apps/remix/) 和 [SvelteKit](https://developers.cloudflare.com/workers/framework-guides/web-apps/svelte/) 等框架提供了 Cloudflare 适配器，可以将你的应用构建为 Worker。它们背后没有源服务器。Worker _就是_ 服务器。

Worker 成为源服务器之后，原始架构没有任何内容可以缓存。每个请求都会执行代码，即使响应与您一秒之前返回的响应每个字节完全相同。[Workers 运行时速度快得足以处理每个请求](https://x.com/KentonVarda/status/1783996343813652801)（我们经常运行每秒处理数千万个请求的服务器，而且毫不费力），但“快得足以处理每个请求”仍然会在每次页面加载时带来延迟，并在每次调用时增加 CPU 时间。因为在服务器端渲染的应用中，根据定义，每次页面加载都是一次渲染。

Workers 缓存颠覆了这种架构。Cloudflare 的缓存现在位于 Worker 的前端：

如果缓存命中，Worker 根本不会运行。Cloudflare 会返回已缓存的响应，您的 CPU 计费保持为零。如果缓存未命中，Worker 会运行一次，填充缓存，然后下一个请求（无论来自何处）都将从缓存中获取服务，而无需调用代码。

这是 Workers 服务器端渲染缺少的内容。过去，您不得不在两个不尽如人意的选项中做出选择：

  * **在构建时预渲染所有内容** （“静态网站生成”）。页面加载速度快，但每次更改都需要完全重建和重新部署。对于一个拥有几千页的文档网站，这需要 5-10 分钟。对于大型电子商务网站来说，情况更糟，每次执行任何操作时，构建版本都会运行。
  * **在每次请求时渲染每个页面。** 内容实时更新，但每次页面加载都会产生渲染成本，每个访客都遭受延迟。



Workers 缓存为您提供第三种选择：按需服务器端渲染，缓存已渲染的响应，并根据您选择的生存时间 ([TTL](https://developers.cloudflare.com/cache/how-to/edge-browser-cache-ttl/)) 刷新。首次请求新页面时，页面仍会渲染。在缓存过期之前，后续的每个请求都会像静态页面一样渲染。如果缓存过期，下一个请求会触发重新渲染，而使用 `stale-while-revalidate` 指令，即使是重新渲染的请求也不会等待。

您可以获得静态网站的速度，但不会耗费构建时间；以及获得服务器端渲染的新鲜度，而无需承担额外的成本。没有类似增量静态再生那样的框架专用机制。仅使用 HTTP 缓存，按照其设计初衷运行，位于原本设计为源服务器的代码前端。

## `stale-while-revalidate` 指令让人感觉响应速度感觉非常快

[stale-while-revalidate](https://datatracker.ietf.org/doc/html/rfc5861#section-3) 指令告诉 Cloudflare，当缓存的响应过期时，它可以立即提供过期的页面副本并 _在后台刷新响应_ 。Cloudflare 今年早些时候[推出了对 stale-while-revalidate 的全面支持](https://developers.cloudflare.com/changelog/post/2026-02-26-async-stale-while-revalidate/)，这个指令将“我们缓存您的 Worker”变成“您的 Worker 网站带来如同静态页面的体验。”

如果没有该指令，缓存条目过期后的第一个请求必须等待 Worker 从头开始渲染页面。用户会感受到这种延迟。因此，过期后的第一个请求会立即获得过期的页面（带有 `Cf-Cache-Status: UPDATING `标头），而 Worker 则在后台运行以重新填充缓存。每个用户，包括触发刷新操作的用户，都会获得缓存速度的响应。

在实践中，这看起来是这样的：

实现此功能的逻辑模型如下：

  * **新鲜窗口** (`max-age`)：Cloudflare 提供缓存响应。您的 Worker 不会运行。
  * **过期窗口** （`stale-while-revalidate`）：Cloudflare 提供缓存响应。您的 Worker 在后台运行以刷新缓存。用户无需等待。
  * **在两个窗口之外** ：Cloudflare 运行您的 Worker 以生成新的响应，用户等待渲染。



您可以自行选择窗口。对于每隔几分钟更新一次的产品目录，`max-age=300`, `stale-while-revalidate=3600` 意味着访客几乎无需等待，同时您的 Worker 仍然会频繁运行，以保持内容新鲜。对于几乎从不更改的博客存档，`max-age=86400`, `stale-while-revalidate=2592000` 意味着您的 Worker 每个页面每天运行一次。

只有首次请求全新页面时，才会支付完整的渲染费用。之后，页面对访客而言就像静态输出一样，而 Worker 仍然负责页面的生成方式。

## 一个 URL，多种表现形式：`Vary` 发挥作用

实际应用极少会向每个客户端返回同一字节。同一产品页面对浏览器可能是 HTML 格式，对于 API 客户端则可能是 JSON 格式。同一图像对于支持 WebP 的客户端可能是 WebP 格式，对于不支持 WebP 的客户端则可能是 JPEG 格式。同一主页可能会以英语、法语或日语返回，具体取决于用户。

不使用缓存很容易实现这一点，Worker 只需读取请求标头并返回正确的内容。而 _使用_ 缓存通常会出现问题。大多数缓存提供两个糟糕的选择：要么不缓存具有多种表现形式的 URL，要么缓存一种表现形式并将其提供给所有用户。

Workers 缓存支持标准的 HTTP `Vary` 标头，这是解决该问题的正确方法。当 Worker 返回的响应包含 `Vary: Accept-Encoding`（或者 `Accept`，或 `Accept-Language` 或任何其他请求标头）时，Cloudflare 会根据这些标头的不同组合存储一个单独的缓存变体，并且仅返回存储值与传入请求匹配的变体。

一个 URL，两种缓存变体。发送 `Accept: image/webp,*/*` 的浏览器会获得 WebP 格式。发送 `Accept: image/jpeg` 的浏览器会获得 JPEG 格式。两者都来自缓存。Worker 会在首次请求时写入两种变体，之后这两种变体不再运行。

这是常用的 HTTP 内容协商标准，Workers 缓存按照 [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html#name-vary) 和 [RFC 9111](https://www.rfc-editor.org/rfc/rfc9111.html#name-calculating-cache-keys-with) 所述的方式实现它。没有允许列表来定义哪些标头可以执行 `Vary` 操作。您列出所需的标头，Cloudflare 会根据这些标头的逐字值生成不同的变体。文档涵盖了[各种特殊情况](https://developers.cloudflare.com/workers/cache/configuration/#vary)：如何在网关 Worker 中通过规范化标头来控制变体的传播，为什么清除操作会使 URL 的所有变体一起失效，以及唯一一种会完全禁用缓存的情况 (`Vary: *`)。

## 这是 Worker 缓存，不是区域缓存

在探讨这一切带来哪些可能实现的变化之前，有一个值得注意的命名概念转变。

Cloudflare 一直以来都有缓存。它是在区域级别配置：缓存规则、Page Rules、缓存文件扩展名列表、Cache Reserve、分层缓存拓扑、自定义缓存键。所有这些都是根据每个区域设置，过去，Worker 不得不适应该区域的配置或找到变通方法。

Workers 缓存则不同。这是 **Worker 缓存** ，它属于 Worker，而不是某个区域。这会产生一系列重要影响：

  * **没有要管理的区域配置。** 缓存规则、缓存级别设置、文件扩展名列表、Page Rules 都不适用于 Workers 缓存。Worker 的 `Cache-Control` 标头就是配置。
  * **缓存跟随 Worker，而不是主机名。** 绑定到 `api.example.com`、`api.example.net` 以及通过服务绑定调用的 Worker 共享同一个缓存。无论请求来自哪个源，对 /users/42 的请求都会命中同一个缓存条目。
  * **缓存适用于**`workers.dev`**。** 它适用[预览版 URL](https://developers.cloudflare.com/workers/configuration/previews/)（每个预览版有各自的缓存，因此，测试更改不会影响生产环境）。它适用 [Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/)（每个用户 Worker 有各自的缓存，与调度程序和其他租户隔离）。所有这些曾经在缓存中都处于次要地位。现在情况已经不同了。
  * **清除操作范围限定在 Worker 的入口点。** 如果调用 `ctx.cache.purge({ purgeEverything: true })`，则仅清除 Worker 入口点的缓存。不存在清空区域的其他内容的风险。不存在部署一个 Worker 导致另一个 Worker 数据失效的风险。



缓存相关的配置都在代码中完成：哪些路径需要更长的 TTL（根据路径进行分支并设置不同的 `max-age` 值）、哪些请求会绕过缓存（返回 `Cache-Control: private`）、缓存键如何构建（控制哪些内容进入 `ctx.props`，在网关 Worker 分发请求之前规范化 URL）。您已经编写的 Worker 就是配置界面。

完整文档详细介绍了这一点，请参阅 [Workers 缓存：您的 Worker 缓存](https://developers.cloudflare.com/workers/cache/)。

## 两层结构，每个 Worker 各司其职，无需配置

Workers 缓存**默认按区域分层** 。共有两层：

  * **底层缓存** 位于距离用户最近的 Cloudflare 数据中心。每个接收 Worker 流量的数据中心都有其各自的底层缓存。
  * **上层缓存** 聚合整个网络的填充缓存。上层缓存数量较少，当未命中缓存时，每个底层缓存会询问上层缓存。



请求首先到达底层缓存。如果命中，则提供响应，请求结束。如果未命中，则底层缓存会询问上层缓存。如果上层缓存命中，则返回响应，并在返回过程中将其存储在底层缓存中。只有当底层缓存和上层缓存都未命中时，Worker 才会实际运行，并且该运行生成的响应会同时存储在这两层缓存中。

这一点至关重要，因为**全球任何地方的第一个请求** 都会填充上层缓存。后续来自任何数据中心的请求均可直接从上层缓存处理，无需运行 Worker，即使该数据中心的底层缓存之前从未处理过该请求。缓存命中率远高于单一扁平缓存层，这正是 Worker 作为源服务器时所需的功能。

这与目前区域[分层缓存](https://developers.cloudflare.com/cache/how-to/tiered-cache/)的拓扑结构相同，只是您无需进行任何配置。没有“为我的 Worker 服务器启用分层缓存”的对话框。每个已启用缓存的 Worker 都会免费获得分层缓存功能。

如果 Worker 使用 [Smart Placement](https://developers.cloudflare.com/workers/configuration/placement/)，则缓存可与之顺利配合：首先查询所有层级的缓存，只有在二者都未命中的情况下，Smart Placement 才会将执行路由到靠近源服务器的位置。关于这些层如何交互，包括我们[计划改进](https://developers.cloudflare.com/workers/cache/#smart-placement-and-the-cache)的一些不足之处，将在文档中进行更详细的说明。

## 靠近用户 _且_ 靠近数据运行应用

Web 性能领域一直存在一个尚未完全解决的对立难题：您希望代码靠近用户运行（因为用户与服务器之间的往返在关键路径中），您也希望代码靠近数据运行（因为每个数据库查询也都是一次往返）。但是，选择其中之一，另一个就会变慢。

多年来，我们一直在努力兼顾两者。Cloudflare 网络将我们与全球约 95% 的互联网用户之间的延迟控制在 [50 毫秒以内](https://www.cloudflare.com/network/)。[Smart Placement](https://blog.cloudflare.com/announcing-workers-smart-placement/) 和 [Placement Hints](https://developers.cloudflare.com/changelog/post/2026-01-22-explicit-placement-hints/) 让您可以将代码始终置于数据附近，无需考虑云区域。但直到现在，这两者仍然无法完美结合。您可以选择“靠近用户”或“靠近数据”，如果您希望自己的应用兼顾二者，则必须成为 Cloudflare 专家。[我们知道，我们可以做得更好。](https://sunilpai.dev/posts/spatial-compute/)

Workers 缓存正是弥合这一差距的关键。由于缓存属于 Worker 而不是区域，并且由于[服务绑定](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/)以及 Workers 之间的 [ctx.exports](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/rpc/) 调用通过缓存进行，因此，您可以将应用构建成一个 Worker 链（每个 Worker 都在其应该运行的位置运行），缓存是这些 Worker 的连接点。

架构如下：

  * **Worker A** 在靠近用户的位置运行。它处理每个请求中那些廉价的、延迟敏感环节：身份验证、速率限制、路由、标头规范化，渲染不依赖数据的 HTML 页面[外壳](https://developers.cloudflare.com/workers/examples/spa-shell/)。
  * **Worker B** 由于 Smart Placement 或显式 Placement Hint 的帮助，在靠近数据的位置运行。它负责处理繁重的工作：服务器端渲染获取数据的页面、读取产品目录、生成搜索结果、聚合 API 以及执行昂贵的转换。
  * **Workers 缓存位于 Worker B 的前端。** 当 Worker A 通过服务绑定调用 Worker B 时，Cloudflare 首先检查 Worker B 的缓存。如果命中，Worker A 收到响应，而 Worker B 完全不会运行，这种情况下无需数据中心跳转、无需数据库查询、无需渲染工作。



缓存命中路径变为：用户 → 靠近用户的 Worker A → Worker B 的缓存命中 → 响应。只有在缓存未命中时，才会为数据跳转付费。您的热门页面以代码直接面向用户的速度运行，而冷门页面在执行时也能受益于靠近数据的运行。

无需进行任何特殊的架构设计，即可实现这一点。只需将您的应用编写成两个 Worker，通过服务绑定将其中一个 Worker 指向另一个 Worker，在 Worker B 的 `wrangler.jsonc` 文件中启用缓存，这样就完成了。

## 默认支持多租户，并带有 `ctx.props` 属性

如果您要缓存返回用户特定数据的 Worker，例如，为每个登录用户提供不同内容的 API，则需要一种方法来确保一个用户绝不会看到另一个用户的缓存响应。标准解决方案是“不缓存已经过身份验证的请求”，Cloudflare 的[自动绕过](https://developers.cloudflare.com/cache/concepts/cache-responses/#bypass) `Authorization `标头机制正是如此。但是，“不缓存任何内容”会完全失去性能优势。

Workers Cache 通过将调用方的 [ctx.props](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/rpc/#ctxprops) 属性作为缓存键的一部分，解决了这个问题。当一个 Worker 通过服务绑定调用另一个 Worker，并传递 `ctx.props`（包括用户 ID、租户 ID 或任何其他标识符）时，拥有不同 props 属性的调用方会获得单独的缓存条目。一个用户的响应绝不会泄露到另一个用户的缓存中。

典型模式是在网关 Worker 中对请求进行身份验证，移除 `Authorization` 标头，将已验证用户的 ID 设置到 `ctx.props `中，然后调用缓存的后端 Worker。网关在每个请求上运行（为了进行身份验证，必须这样做），但昂贵的后端只有在尚未为该用户创建缓存条目时才运行。经过身份验证的 API 从“不可缓存”变为“已按用户缓存且完全安全”，缓存键负责执行隔离。文档在“[使用 ctx.props](https://developers.cloudflare.com/workers/cache/cache-keys/#multi-tenant-safety-with-ctxprops) 实现多租户安全性”以及“[按用户已进行身份验证的响应](https://developers.cloudflare.com/workers/cache/examples/#per-user-authenticated-responses)”示例中对此进行了详细介绍。

其他 CDN 要求您在正确性与命中率之间做出选择：要么使用每个用户的令牌来缓存数据，要么将每个请求发送回源服务器获取授权。Workers 缓存让您可以在边缘共享已缓存的 API 响应，同时保留每个请求的授权边界。我们目前尚未发现其他 CDN 为经过身份验证的多租户 API 提供这样的内置模型。我们为 Cloudflare 做到这一点感到非常自豪。

## 每个 Worker 入口点之间的缓存

这是我们认为 Workers 缓存中最重要的突破，如果您将其理解为“恰好在 Worker 前端运行的 CDN 缓存”，那么这部分可能最难理解。

**Workers 缓存位于每个 Worker 入口点前端** ：默认导出、每个已命名的 [WorkerEntrypoint](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/rpc/#named-entrypoints)，以及同一 Worker 中入口点之间通过 [ctx.exports](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/rpc/) 进行的每一次调用。正是最后这一点改变了您可以构建的内容。

当一个入口点通过 `ctx.exports `调用另一个入口点时，缓存会像评估来自浏览器的请求同样的方式评估该调用。如果命中，则返回缓存的响应，被调用方不会运行。如果未命中，则被调用方运行，并将其响应存储在自己的缓存键下，由被调用方的入口点、路径、查询字符串和 `ctx.props` 作为键码。调用方仍然会在每一次请求时运行，但其传递给被调用方的任何内容都会独立地存储。

您可以决定每个入口点缓存哪些内容。在 Wrangler 配置中，`exports` 映射让您可以按名称为每个入口点启用或禁用缓存（“default”表示默认导出）。选择**启用** 即可缓存入口点生成的响应；选择**禁用** 即会使其在每次请求时运行。网关或路由器入口点（任何进行身份验证、标准化或分发的入口点）都应选择禁用，以便始终运行，并且决不会从缓存中提供其自身的输出。

这将为您提供可编排的基础组件。您可以将 Worker 编写成一系列小型入口点：身份验证、标准化、路由、昂贵的读取、数据层，并让 Workers 缓存插入您想要的位置。每个缓存的入口点都是一个记忆单元，拥有自己的键、生存时间以及用于清除缓存的专属标签命名空间。任何您想要配置的缓存信息，例如运行时间、基于的键值、失效时间，都可以使用普通 Worker 代码表示：调用哪个入口点、转发哪个请求、传递哪些 `ctx.props` 属性，以及设置哪些 `Cache-Control` 参数。

为了更具体地说明这一点，请看这个 Worker 示例，它完成了在其他平台难以同时实现的三项任务：对每个请求进行身份验证，在多租户安全的缓存键后面缓存昂贵的后端，以及在数据更改后使该缓存失效。

按入口点配置缓存。网关之所以必须在每次请求时运行，既是为了进行身份验证，也是因为已缓存的网关响应会跳过身份验证检查；因此，我们在默认入口点禁用缓存，并且只在内部入口点启用缓存：

整套方案只有一个 Worker。一个源文件。一次部署。但有两个执行阶段，也就是在一个小型` exports `块中，关闭网关缓存，启用后端缓存，二者之间有一个缓存，它由用户键控，根据写入路径失效，并在后台刷新期间提供过期数据。缓存阶段并非附加组件。它是程序的一层，用代码编写。

由此组合形成的模式是开放的。同样的特征也适用于：

  * **缓存 Durable Object。** 将 Durable Object 包装在入口点之后，在响应中设置 `Cache-Control`，如果命中，则读取操作停止访问 Durable Object。写入操作直接写入 DO 并按标签清除缓存。DO 不会感知到正在进行缓存。
  * **在**`Vary`**之前标准化**`Accept-Encoding`。外部入口点从 `request.cf.clientAcceptEncoding` 恢复原始编码（Cloudflare 前端会对其进行标准化处理以提高缓存效率），然后转发到随实际值而变化的已缓存入口点。命中率居高不下；客户端获得正确的编码。
  * **在缓存之前，移除跟踪参数。** 外部入口点会标准化 URL 



或者在 `ctx.exports` 调用中使用 `cf.cacheKey `设置[自定义缓存键](https://developers.cloudflare.com/workers/cache/cache-keys/#custom-cache-keys)，因此，缓存的内部入口点只能看到标准的形式，而 `?utm_source=anything `会折叠到一个单独的缓存条目。

堆叠这些缓存。单个 Worker 可能拥有一个外部入口点用于身份验证和路由、一个标准化化入口点用于移除跟踪参数并恢复编码标头、一个缓存的入口点位于 Durable Object 前端，以及一个单独的已缓存入口点用于访问未经身份验证的公共 API，每个入口点通过一个缓存阶段连接，您无需配置，只需决定放置位置。[文档中的“示例”页面](https://developers.cloudflare.com/workers/cache/examples/)完整演示了几个示例。

我们目前尚未发现其他平台能够做到这一点。CDN 缓存位于源服务器前面。函数平台运行函数。我们目前还没有发现其他平台可以在应用各部分之间提供这样一个缓存，该缓存位于单个可部署单元内部，并且每个缓存阶段由其两侧的代码进行配置。这就是 Workers 缓存的功能。而且，由于它可以与平台提供的其他各项功能（Smart Placement、Durable Objects、服务绑定、`ctx.props`、`ctx.exports`）结合，因此，您可以构建的模式是开放的。本文只涉及问题的表面，没有深入探究。

## 提供框架内一流支持

如果使用 Astro 构建应用，Cloudflare 适配器会自动为您连接 Workers 缓存。只需将 [cacheCloudflare 提供程序](https://docs.astro.build/en/guides/caching/#cloudflare)添加到配置中：

适配器会启用缓存，在 Astro 生成的响应中设置正确的标头，附加用于使缓存失效的 `Cache-Tag `值，并提供 `cache.invalidate()` 辅助函数，用于在内容更改后清除标签。选择服务器端渲染的 Astro 页面会自动进入上述“渲染一次，缓存，后台刷新”流程，无需针对每个路由进行配置，也无需学习特定框架的运行时层。

我们将与其他框架的维护者合作，以实现相同的集成。如果您构建 Cloudflare 框架适配器，[Workers 缓存 API](https://developers.cloudflare.com/workers/cache/) 正好适配您的需求，基于标头的配置、程序化清除，无需对平台特定的概念进行建模。

## 在与 Worker 相同的仪表板中查看缓存信息

只有当您能够看到缓存的运行情况时，它才真正有用。[Workers Observability 仪表板](https://developers.cloudflare.com/workers/observability/)现在会显示每次调用的缓存命中信息：

您可以查看每个 Worker 的：

  * **高速缓存命中率** 随时间的变化。启用缓存后，您希望看到数值上升的趋势。
  * **命中、未命中、更新、绕过** 次数的细分。如果命中率低，可以在这里找到原因：`BYPASS` 响应过多（因为某些程序正在设置 Cookie？）、`MISS `响应过多（因为缓存键的分区比预想的更多？），或是 `UPDATING` 响应过多（因为 `max-age `比流量间隔时间更短？）。



由于这些信息与 Worker 的其他可观测性（日志、异常、CPU 时间、请求计数）都在同一个仪表板中，因此，您不必在查看区域和 Worker 之间切换上下文就能了解正在发生的事情。

## 账单

缓存命中不会运行 Worker，CPU 时间也不会计费。它们按标准 [Workers 请求率](https://developers.cloudflare.com/workers/platform/pricing/)计费，与其他任何调用相同。缓存未命中与绕过会正常计费（请求 + CPU 时间），与不使用缓存时完全相同。

Outcome| Request charge| CPU time charge  
---|---|---  
缓存 HIT（Worker 不运行）| 标准费率| 不计费  
缓存 MISS（Worker 运行）| 标准费率| 计费  
缓存 BYPASS（Worker 运行）| 标准费率| 计费  
静态资产请求| 标准费率| 不计费  
Worker 之间的调用| 标准费率| 如果 Worker 运行，则收费  
  
没有单独的 Workers 缓存 SKU，也没有按 GB 计费的缓存存储费用。分层缓存、清除、`stale-while-revalidate` 以及上述分析功能均已包含。如果请求原本会触发 Worker 运行，但 Workers 缓存将其作为缓存命中处理，您仍需支付标准请求费用，但无需为请求的 CPU 时间付费。因此，缓存命中比在 Worker 中渲染相同响应的成本更低。

需要注意的是：启用缓存后，通常免费的请求（例如[静态资产请求](https://developers.cloudflare.com/workers/static-assets/billing-and-limitations/) 以及通过服务绑定或 `ctx.exports`[ 进行的 Worker 之间的调用](https://developers.cloudflare.com/workers/platform/pricing/#service-bindings)）将按标准费率计费，因为这些请求现在都会查询 Worker 前端的缓存。

## 下一步

我们接下来要做的事情：

  * **利用 Smart Placement 实现更智能的托管。** 目前，Cloudflare 会分别选择上层缓存和 Smart Placement 缓存目标。在完全未命中的情况下，请求可能会在 Cloudflare 各个位置之间往返两次：一次用于检查上层缓存，另一次用于在靠近数据的地方运行 Worker。我们正在努力协调这些选择，以便缓存未命中时，请求只需进行一次长途传输。
  * **提高响应大小限制。** 在发布初期，所有响应都遵循 [Free 计划的可缓存大小限制](https://developers.cloudflare.com/cache/concepts/default-cache-behavior/#cacheable-size-limits) (512 MB)，无论账户类型是什么。这只是暂时的措施，一旦我们完成一些推广步骤，将执行每种计划的标准缓存限制。
  * **添加更多框架集成。** Astro 具有[内置的 Workers 缓存集成](https://docs.astro.build/en/guides/caching/#cloudflare)。我们将与维护者合作，通过 [Vinext](https://vinext.dev/) 将类似的集成添加到其他框架中，包括 [TanStack Start](https://developers.cloudflare.com/workers/framework-guides/web-apps/tanstack-start/) 和 Next.js。
  * **开发用于标记缓存响应过期的 API。** ctx.cache.purge() 会从缓存中移除匹配的响应。我们将开发 ctx.cache.invalidate() API，使匹配的响应表现为已过期，这样一来，即使 Worker 在后台刷新缓存，下一个请求仍然可以通过 stale-while-revalidate 快速获取过期的响应。



## 立即试用

Workers 缓存现已面向所有计划中的每一个 Worker 开放。

若要开始使用，请将 `"cache": { "enabled": true } `添加到 `wrangler.jsonc` 文件，重新部署，然后开始设置 `Cache-Control` 标头。[Workers 缓存文档](https://developers.cloudflare.com/workers/cache/)详细介绍了完整的功能，包括[快速入门](https://developers.cloudflare.com/workers/cache/#quickstart)、[缓存键](https://developers.cloudflare.com/workers/cache/cache-keys/)、[清除](https://developers.cloudflare.com/workers/cache/purge/)、[组合模式和示例](https://developers.cloudflare.com/workers/cache/examples/)，以及[调试](https://developers.cloudflare.com/workers/cache/debugging/)。

过去，Workers 在缓存的前端运行。现在，它们也可以在缓存后端运行。您可以根据需要，选择在任意一侧运行，或者通过服务绑定，在缓存两侧同时运行。

我们迫不及待想看到您构建的成果。

]]>1WYEYtVwQSo4H3jKHTcKmO隆重推出 Monetization Gateway：使用 x402 对受 Cloudflare 保护的资源使用收费https://blog.cloudflare.com/zh-cn/monetization-gateway/ Mon, 24 Aug 2026 05:23:17 GMT我们将开放 Monetization Gateway 等候名单，该工具将支持您对受 Cloudflare 保护的任何网页、数据集、API 或 MCP 工具收费。费用将通过 x402 开放协议以稳定币结算，无需您自行构建任何支付技术栈。AIAI 机器人Paymentsx402内容独立日机器人今天，我们宣布推出 Cloudflare Monetization Gateway，这款引擎将让 Cloudflare 客户能够对受 Cloudflare 保护的任何资产（包括网页、数据集、API 或 MCP 工具）收费。 

它将提供单个统一的控制平面，用于管理应用中的支付策略和访问控制措施，同时通过在边缘处理支付验证和强制执行，保护您的源站免受大量支付交易额的影响。上线初期，支付将通过 [x402](https://www.x402.org/) 使用稳定币结算，这是我们通过 [x402 Foundation](https://blog.cloudflare.com/x402/) 与 25 家以上行业领导者组成的联盟[共同构建](https://www.linuxfoundation.org/press/linux-foundation-is-launching-the-x402-foundation-and-welcoming-the-contribution-of-the-x402-protocol)的开放协议。 

### 不断演变的网络商业模式

30 年来，网络依靠一个简单的经济交易规则运行：用内容换取用户的注意力。这种注意力已通过广告、订阅和电子商务实现了变现。这种交易为我们熟知的互联网提供了资金支持。 

但随着智能体成为互联网的主要用户，这种模式正在瓦解。智能体无需浏览广告，也无需维持月度订阅来访问所需的各种工具。它只需读取页面或使用数据馈送一次，获取所需信息并继续访问其他内容。整个网络中，AI 爬网程序已经对每位[返回](https://blog.cloudflare.com/ai-crawler-traffic-by-purpose-and-industry/)的访客进行了从一百次到数万次的内容请求。 

这种现实需要一个全新的模式：所有服务均采用基于使用量的定价。如果注意力和电子商务正在从网站转移到 AI 驱动的平台和 AI 编写的软件，则智能体应为其所需的输入支付费用，包括训练数据、推理内容、开发工具和 API 使用。软件的自然支付单位是请求、令牌或结果，而不是席位或月份。示例如下：

  * 每次网络搜索几美分，按调用次数计费
  * 0.001 美元基础费，外加每 MB 0.01 美元的端点上传费
  * 每次解决的支持升级服务费为 0.99 美元，仅在成功完成工作后支付



这与[问答引擎使用创作者的内容后向其付费](https://blog.cloudflare.com/making-ai-search-smarter)的转变如出一辙：每次使用内容或资源时进行公平的价值交换，价格基于以此目的构建的中立渠道。人们通常设想智能体购买高价资产，例如域名，但智能体支付的大部分费用都在结算流程的上游，而且价格也低得多。

部分互联网已经采用这种方式运作。多年来，云服务和 API 一直按调用次数和小时数计费，但仅限于已知的买家：用户注册后，他们会获得一个 API 密钥，并产生基于使用量的计量计费。内容大多跳过了付费环节，而是依靠广告收入。这些商业模式从未能为未经验证的买家提供低于美分的交易服务，因为[支付渠道](https://stripe.com/resources/more/what-are-payment-rails#what-are-payment-rails)成本过高且结算时间过长。低于某个价格时，收款成本甚至超过了付款本身的价值。

过去，按使用量计费的模式难以实施。企业需要有效地转型为支付公司，管理其帐目，以稳健且可审计的方式跟踪内部使用情况。跟踪这些使用情况需要对后端系统进行重大改造。许多企业转而选择按席位计费的模式，因为它更简单，而且通常利润更高。 

智能体颠覆了这种模式。单个智能体可以全天候完成整个团队的工作，导致一次性固定费用与实际使用量脱节。与此同时，智能体可以毫不费力地处理成千上万笔小额支付，而让用户逐笔审批则极其繁琐。基于使用量计费的价格点是智能体的生存之道，也是基于稳定币的小额支付的亮点。这是因为稳定币（例如 [Open USD](https://joinopenstandard.com/) 和 [USDC](https://www.circle.com/usdc)）允许买家通过互联网转账小额资金，手续费几乎可以忽略不计，且不到一秒就完成结算。这是目前其他支付渠道无法实现的。

这正是我们能够提供帮助的地方。Cloudflare 多年来一直在为自有计费系统和客户的分析系统构建基于使用量的计费方式。得益于我们作为买卖双方代理层的地位，我们可以显著简化基于使用量的 Web 资产计费的实施。如下所示，凭借 Cloudflare 对基于使用量计费模式的支持，付款证据可以集成到请求本身，支付验证与请求路径得以合并。

这对您的好处是：计量、支付交换和结算从源站转移出去。保留下来的是真正重要的任务：规则、价格和营收。您无需引导买家完成入驻或建立计费系统。只需编写规则，智能体买家将为其使用的内容付费。

### 复习 x402

在去年的[内容独立日](https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/)，我们让网站所有者只需点击一下即可决定哪些 AI 爬网程序可以访问其内容，并通过[按抓取付费](https://blog.cloudflare.com/introducing-pay-per-crawl/)功能，让他们可以向爬网程序收费。Monetization Gateway 是下一步：与仅向爬网程序收取内容访问费用不同，还可以向任何调用者收取资源使用费，从 API 到数据再到 MCP 工具调用，且无需自行构建支付机制。

x402 是一种开放协议，它支持通过 HTTP 进行支付，其名称源自它最终使用的 402 状态码。x402 交易流程很简单：客户端请求需要付费才能访问的资源。服务器没有提供所需资源，而是返回 402 Payment Required 响应，并附带一个简短的有效负载，说明价格、可接受的资产以及支付渠道。客户端完成支付，然后再次发送请求并附上付款证明。支付服务商进行验证，然后服务器返回资源。所有操作在普通的 HTTP 请求和响应中完成，无需重定向到结账页面，也无需调用单独的支付 API。结算采用点对点方式，因此，买家发送给卖家的任何资金都会直接存入卖家的钱包。我们正在设计 Monetization Gateway 以维持低的支付开销，并力争实现亚秒级的支付结算。

 _x402 支付流程: AI 智能体 ↔ API 服务器 ↔ 区块链，来源：[ GitHub 上的 x402 自述文件](https://github.com/coinbase/x402#typical-x402-flow) _

x402 的两个特性使其非常适合机器支付。支付金额可能很小，低至几美分，因为该协议几乎不会增加任何开销。买家无需在卖家处开设账户，因为付款本身就是凭证。x402 与支付渠道无关，但它非常适合稳定币，稳定币可以在不到一秒的时间内完成几美分的结算，且零拒付。

### Monetization Gateway 的功能

Monetization Gateway 将提供一个灵活的支付规则 API，让您可以精确地指定何时要求调用方付费才能访问您的数字资源。

其工作原理如下所述：令牌、API、MCP 工具调用和数据已经通过该路径流动。您可以根据需要，精确地决定哪些流量需要付费。您将能够通过在简洁的专用产品 API 中编写表达式来执行决策，这些表达式与您为其他 Cloudflare 规则编写的表达式类似。Monetization Gateway 将随着覆盖 330 多个城市的 Cloudflare 全球网络而扩展，这意味着 x402 握手将在您买家附近的地方进行。这将缩短请求延迟并保护您的源站。 

以下是一些计划的功能示例：

  * 对特定 REST 动词收费：要求对特定路由的调用收取费用，例如，对每个发送到 /api/premium/* 的 GET 或 POST 请求收取 0.01 美元。
  * 差异化浮动定价：根据任务的复杂程度收取不同的费用，例如，图像生成任务可能根据使用的计算资源收取不超过 2 美元的费用。
  * 仅向未经身份验证的调用方收费：拦截来自源站的 HTTP 401“Unauthorized”响应，改为返回 402“Payment Required”响应，并提供定价和付款说明。



如果请求匹配，Monetization Gateway 会验证付款，然后允许请求通过。您将能够在仪表板中设置这些规则，或者通过 Cloudflare API 和 Terraform 以代码方式进行管理，因此，付费端点只是您基础设施配置的一部分。

Monetization Gateway 最初支持用户要求买家以稳定币为服务和资源付费。卖家将能够使用其累积的稳定币进行自己的交易，或者将稳定币兑换成等值的法定货币存入其银行账户。使用 Monetization Gateway 可以扩大您产品的潜在可拓展市场。通过 Gateway，智能体可以请求访问您的资源，获取价格信息，支付费用并获得响应。无需注册，无需 API 密钥，无需先前关系。您可以决定需要了解买家多少信息，灵活地要求智能体使用 [Web Bot Auth](https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/) 进行身份验证，并对其已有的账户应用基于使用量的定价。

### 后续发展方向

Monetization Gateway 将请求转化为支付，并为 Cloudflare 客户带来新的营收机会，但其发展潜力远不止于此。

智能体是一种代表用户自主行动的软件，而智能体开始逐渐走向独立行动。在不久的将来，它们将拥有自己的“钱包”，无需人工干预即可购买所需资源：数据集、API 调用、工具、计算块。部分资源将免费提供，但某些资源则需要通过已获验证的智能体身份来证明智能体的确切身份及其代表的用户。许多资源需要身份验证和支付，Cloudflare 是少数几个能够在单个请求中完成所有结算的平台之一。它的具体做法是验证智能体、应用规则，并在源端收到调用之前检查支付情况。智能体将成为互联网上的主要买家，请求会变成交易。

如今，互联网上流动着大量未变现或变现价值不足的大量内容，这并不是因为无人愿意付费，而是因为缺乏相应的收费工具。智能体发出的每一个有用的 API 调用、每一个响应、每一次工具调用都有价值，但如今几乎没有任何价值得到付费。这是摆在我们面前的机遇，也是 Monetization Gateway 即将释放的潜力。

这是我们正在努力的方向：一个智能体优先的互联网，内置互联网规模的结算机制。在这个互联网中，那些创造有价值内容的人将自动获得使用其内容的软件支付的费用。即便是最小型的新 API 也可能以与互联网上最大型的公司相同的条件触达相同的买家，而独立创作者则可以从使用其作品的大语言模型中获得收益。这就是互联网的下一个商业模式，我们正在构建其支持体系。

### 注册加入我们的等候名单

Cloudflare 客户现在可以加入 Monetization Gateway 等候名单。如果您有兴趣使用按使用量计费模式实现您的网页、数据集、API 或 MCP 工具变现，[请请加入我们的提前体验名单](https://docs.google.com/forms/d/e/1FAIpQLSfq6yaIgp57FCGFg7riXlSWTeD8d8Adur2c8tWaKY4SuzweiQ/viewform?usp=header)。

]]>6dNg0U03j4cnbacP8txDok
