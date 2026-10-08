---
url: https://blog.cloudflare.com/ar-ar/expanding-regional-services-configuration-flexibility-for-customers/
title: \u062a\u062d\u0633\u064a\u0646 \u0645\u0631\u0648\u0646\u0629 \u062a\u0643\u0648\u064a\u0646 \u0627\u0644\u062e\u062f\u0645\u0627\u062a \u0627\u0644\u0625\u0642\u0644\u064a\u0645\u064a\u0629 \u0644\u0644\u0639\u0645\u0644\u0627\u0621 | \u0645\u062f\u0648\u0646\u0629 Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:41:17.062057+00:00
---

# تحسين مرونة تكوين الخدمات الإقليمية للعملاء | مدونة Cloudflare

> Source: https://blog.cloudflare.com/ar-ar/expanding-regional-services-configuration-flexibility-for-customers/

[المدوّنة](https://blog.cloudflare.com/ar-ar/)

[Data Localization (AR)](https://blog.cloudflare.com/ar-ar/tag/data-localization/)

1 وسومعرض 1 وسوم

  * وسوم المنشور
  * [Data Localization (AR)](https://blog.cloudflare.com/ar-ar/tag/data-localization/)
  * جميع الوسوم
  * الوسوم المطابقة
  * لم يُعثر على وسم
  * [الذكاء الاصطناعي](https://blog.cloudflare.com/ar-ar/tag/ai/)
  * [Data Localization (AR)](https://blog.cloudflare.com/ar-ar/tag/data-localization/)
  * [المطورون](https://blog.cloudflare.com/ar-ar/tag/developers/)
  * [الحياة في Cloudflare](https://blog.cloudflare.com/ar-ar/tag/life-at-cloudflare/)
  * [الشركاء](https://blog.cloudflare.com/ar-ar/tag/partners/)
  * [السياسة والشؤون القانونية](https://blog.cloudflare.com/ar-ar/tag/policy/)
  * [تحليل ما بعد الحادثة](https://blog.cloudflare.com/ar-ar/tag/post-mortem/)
  * [أخبار المنتجات](https://blog.cloudflare.com/ar-ar/tag/product-news/)
  * [رادار](https://blog.cloudflare.com/ar-ar/tag/cloudflare-radar/)
  * [الأمن](https://blog.cloudflare.com/ar-ar/tag/security/)
  * [السرعة والموثوقية](https://blog.cloudflare.com/ar-ar/tag/speed-and-reliability/)
  * [نموذج أمان Zero Trust](https://blog.cloudflare.com/ar-ar/tag/zero-trust/)



[Data Localization (AR)](https://blog.cloudflare.com/ar-ar/tag/data-localization/)

22 مايو 2024

# تحسين مرونة تكوين الخدمات الإقليمية للعملاء

![Wesley Evans](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48NY89SHS2051YPQ8PN11B.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Wesley Evans](https://blog.cloudflare.com/ar-ar/author/wesley/)

متوسط وقت القراءة 7 دقائق

نسخ الرابط

هذا المنشور متوفر أيضًا بـ [English](https://blog.cloudflare.com/expanding-regional-services-configuration-flexibility-for-customers/) و[Deutsch](https://blog.cloudflare.com/de-de/expanding-regional-services-configuration-flexibility-for-customers/) و[Español](https://blog.cloudflare.com/es-es/expanding-regional-services-configuration-flexibility-for-customers/) و[Français](https://blog.cloudflare.com/fr-fr/expanding-regional-services-configuration-flexibility-for-customers/) و[Português](https://blog.cloudflare.com/pt-br/expanding-regional-services-configuration-flexibility-for-customers/) و[Nederlands](https://blog.cloudflare.com/nl-nl/expanding-regional-services-configuration-flexibility-for-customers/).

![Expanding Regional Services configuration flexibility for customers](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW447XKQX5P6J0X8QQTSJRVT.png&w=1800&h=1013&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///////98fLx5ejr5uru7vD08fHy7+3q////////7vDz4OTs4eTv6ez17u/07ezs////////7O723N/v29/y5Oj47O737e3v////////7e/72d702N734uj87O/77/D0////////8PT/2+L62eL95ez/8PT/9fb5////////9vr/4On/3ej/6vP/9vv/+/z+////////+///5O//4e7/7vj/+////////////////f//5vH/4/H/8Pv//f//////)

عندما [أطلقنا](https://blog.cloudflare.com/introducing-regional-services/) الخدمات الإقليمية في يونيو 2020، كان مفهوم [تحديد موقع البيانات وسيادة البيانات](https://www.cloudflare.com/learning/privacy/what-is-data-localization/) راسخًا بشدة في اللوائح الأوروبية. وبمرور الوقت حتى يومنا الحالي، لا تزال مسألة توطين البيانات ملحة: تطبق العديد من الدول قوانين تفرض توطين البيانات بأشكال مختلفة، كما أن متطلبات المناقصات في القطاع العام في العديد من الدول تقتضي من الموردين تقييد موقع معالجة البيانات، وبعض العملاء يتفاعلون مع التطورات الجيوسياسية بالسعي إلى استبعاد معالجة البيانات من بعض الاختصاصات القضائية.

ولهذا يسعدنا اليوم أن نعلن عن إمكانيات موسّعة تسمح لك بإعداد الخدمات الإقليمية وتكوينها لمجموعة أكبر من المناطق المُحدّدة مسبقًا، وذلك لمساعدتك على تلبية متطلباتك الخاصة بالتحكم في مكان معالجة حركة البيانات الخاصة بك. هذه المناطق الجديدة متاحة للوصول المبكر ابتداءً من أواخر شهر مايو 2024، ونخطط لإتاحتها بشكل عام في يونيو 2024.

لطالما كان هدفنا تزويدكم بمجموعة أدوات الحلول التي تلبي احتياجاتكم فيما يتعلق بمعالجة المخاوف الأمنية والأداء، كما نسعى دائمًا لمساعدتكم على الوفاء بالتزاماتكم القانونية. وعندما يتعلق الأمر بتوطين البيانات، نعلم أن بعضكم يحتاج إلى بقاء البيانات في اختصاص قضائي مُعيّن، بينما يحتاج البعض الآخر إلى تجنب وجود البيانات في اختصاصات قضائية مُعيّنة. واستجابة لهذه الاحتياجات، قمنا بتوسيع مجموعة أدوات خدماتنا الإقليمية لمساعدتكم على تحديد موقع فحص حركة البيانات بشكل أكثر دقة. تتيح لكم بعض خدماتنا الإقليمية الجديدة تقييد فحص البيانات ليقتصر فقط على مراكز البيانات الموجودة ضمن حدود اختصاصات قضائية مُعيّنة مثل: البرازيل والمملكة العربية السعودية وسويسرا. في حين تتيح لكم بعض خدماتنا الأخرى السماح بفحص البيانات في أي مكان باستثناء اختصاصات قضائية مُعيّنة، على سبيل المثال خدمتنا الجديدة التي تستبعد هونج كونج وماكاو وتلك التي تستبعد روسيا وبيلاروس. واستمعنا أيضًا إلى العملاء الذين يتوقون إلى إظهار التزامهم بالاستدامة من خلال الحل الخاص بمنطقة الطاقة الخضراء من CloudFlare، والذي يقصر فحص البيانات على مراكز البيانات التي تلتزم بتشغيل عملياتها باستخدام الطاقة المتجددة.

تتضمن المناطق الجديدة بعضًا من أكثر المناطق والمواصفات طلبًا لدينا:

النمسا والبرازيل والطاقة الخضراء من Cloudflare، باستثناء هونغ كونغ وماكاو، وباستثناء روسيا وبيلاروس، وفرنسا، وهونغ كونغ، وإيطاليا، وحلف شمال الأطلسي، وهولندا، وروسيا، والمملكة العربية السعودية، وجنوب إفريقيا، وإسبانيا، وسويسرا، وتايوان.

يمكن الاطلاع على قائمة كاملة بعروض خدماتنا الإقليمية [هنا.](https://developers.cloudflare.com/data-localization/region-support/)

### ملاحظة حول إطار عملنا لتوطين البيانات في المستقبل

خلال العام المقبل، سترون طرقًا جديدة ومثيرة لاستخدام منتجات CloudFlare للمساعدة في الحفاظ على توطين بياناتك. ولكن ألا يتعارض هذا مع مبدأ العمل الأساسي لشركة Cloudflare؟ ألسنا شبكة Anycast عالمية تؤمن بمناطق الأرض؟

نؤكد أنه ليس بالضرورة أن يكون هذا خيارًا أحاديًا. فبينما نؤمن دائمًا بأن توطين البيانات لا ينبغي أن يكون بديلاً للخصوصية، وأن القيود المفروضة على نقل البيانات عبر الحدود [تضر بالتجارة العالمية](https://itif.org/publications/2021/07/19/how-barriers-cross-border-data-flows-are-spreading-globally-what-they-cost/)، إلا أننا نلتزم بدعم جميع المستخدمين الذين يحتاجون إلى حلول توطين البيانات لمواجهة التزاماتهم القانونية وتحمّل المخاطر.

للأسف، قرر العديد من مقدمي الخدمات السحابية المختلفين أن الطريقة الأفضل لتلبية احتياجات عملائهم فيما يتعلق بالامتثال هي إنشاء عمليات نشر للبنية التحتية الثابتة تُسمّى السحب السيادية. وتكمن المشكلة في عمليات نشر البنية التحتية هذه في أنه يتعيّن عليك الالتزام بأن تكون جميع حركة بياناتك إقليمية، وذلك بغض النظر عما إذا كانت كل حركة البيانات هذه تحتاج بالفعل إلى الاقتصار على مركز بيانات مُحدّد في منطقة مُعيّنة.

ومع استمرارنا في تعزيز تطوير مجموعة أدوات توطين البيانات الخاصة بنا، أود أن أوضح الأسئلة التي توجه عملية تفكيرنا:

ماذا لو كانت هناك طريقة أفضل مستقبلاً تسمح لك بتقسيم ما تحتاجه بالضبط حسب المنطقة، دون الحاجة إلى توطين كل شيء، مما يمنحك أفضل امتثال وأداء؟ ما الذي يمكن أن يبنيه العملاء إذا استطاعوا تحديد موقع واجهات برمجة التطبيقات التي تتعامل مع معلومات العملاء الخاصة، مع استضافة أصولهم الثابتة عالميًا؟ كيف يمكننا زيادة التوافق والخصوصية في نظام أمان [Zero Trust](https://www.cloudflare.com/learning/security/glossary/what-is-zero-trust/) الذي ينشره عملاؤنا، إذا سمحنا لهم باختيار مكان معالجة إجراءات الأمان الخاصة بهم؟ ماذا لو استطاع العملاء تعريف مناطق مُخصّصة وتطبيقها على أسماء مضيفات مُحدّدة ومنتجات Cloudflare، مع القدرة على استخدام [عناوين IP خاصة بهم (BYOIP)](https://developers.cloudflare.com/byoip/) أو [عناوين IP ثابتة](https://developers.cloudflare.com/spectrum/about/static-ip/)؟

نطلق على هذا النهج اسم التقسيم الإقليمي المُعرّف للبرمجيات (SDR)، ونعتقد بأنه يمثل مستقبل توطين البيانات. وبالاستفادة من شبكتنا العالمية كأساس، يمكّن التقسيم الإقليمي المُعرّف للبرمجيات عملاءنا من اتخاذ خيارات دقيقة للغاية حول حركة البيانات التي يريدون تقسيمها إقليميًا والمكان الذي يريدون تقسيمها فيه. يمنحك هذا القدرة على بناء تطبيقات سريعة وموثوقة ومتوافقة دون الحاجة إلى نشر بنية تحتية مادية جديدة أو استخدام عمليات نشر سحابية متعددة لنفس التطبيق.

وبالمضي قدمًا، يتيح لك التقسيم الإقليمي المُعرّف للبرمجيات تكييف خدمات Cloudflare لتلبية احتياجاتك الحالية والمستقبلية. كما يمنحك هذا التقسيم المرونة اللازمة للاستجابة السريعة للتحديات الجديدة في عالم سريع التغيّر. وبتحديدك لخيارات التوطين عبر البرمجيات، لا تكون مقيدًا بالقيود المادية لمنطقة شبكتك الحالية أو مواقع عمليات النشر السحابي الخاصة بك.

نرى أن التقسيم الإقليمي المُعرّف للبرمجيات يمثل مستقبل توطين البيانات، ونحن متحمسون لكوننا في طليعة تطويره.

### كيف تضمن الخدمات الإقليمية معالجة بياناتك في المنطقة الصحيحة

لا يمكن الامتثال للمتطلبات الخاصة بتوطين البيانات بدون تشفير قوي؛ وإلا، يمكن لأي شخص التجسس على بيانات عملائك، بغض النظر عن مكان تخزينها. التشفير القوي هو أساس الخدمات الإقليمية.

تُوصف البيانات عادةً بأنها "في حالة نقل" و"في حالة السكون". ومن المهم للغاية أن يتم تشفير كليهما. وتشير البيانات التي تُوصف بأنها "في حالة نقل" إلى تلك – البيانات أثناء تحركها عبر الأسلاك، سواءً كانت شبكة محلية أو شبكة الإنترنت العامة. أما البيانات التي تُوصف بأنها "في حالة سكون" فتعني بشكل عام أنها مُخزّنة على قرص في مكان ما، سواءً كان قرصًا صلبًا دوارًا أو قرصًا حديثًا ذا حالة صلبة.

أثناء النقل، يمكن لشركة Cloudflare فرض استخدام جميع حركة البيانات لبروتوكول [TLS](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/) الحديث والحصول على أعلى مستوى ممكن من التشفير. كما يمكننا دائمًا فرض تشفير جميع حركة البيانات التي تعود إلى خوادم خارجية خاصة بالعملاء. ويتم تشفير الاتصال دائمًا بين جميع مراكز البيانات الصغيرة والأساسية الخاصة بنا.

تشفّر CloudFlare جميع البيانات التي نتعامل معها في حالة السكون، باستخدام تشفير على مستوى القرص. بداية من الملفات المُخزّنة مؤقتًا على شبكتنا الصغيرة وصولاً إلى حالة التكوين في قواعد البيانات الموجودة في مراكز البيانات الأساسية لدينا – يتم تشفير كل بايت في حالة السكون.

كيف إذَنْ يمكننا أيضًا تقسيم حركة البيانات حسب المنطقة إذا كانت مشفرة؟ تعلن جميع مراكز بيانات Cloudflare عن نفس عناوين IP من خلال [بروتوكول بوابة الحدود (BGP)](https://www.cloudflare.com/learning/security/glossary/what-is-bgp/). أيهما أقرب مركز بيانات إلى المستخدم النهائي من وجهة نظر الشبكة هو الذي سيصله المستخدم.

هذا الأمر رائع لسببين؛ الأول هو أنه كلما كان مركز البيانات أقرب إلى المستخدم، كانت الاستجابة أسرع. والثاني هو أن هذا مفيد جدًا عند التعامل مع [الهجمات الكبيرة لحجب الخدمة الموزع (DDoS)](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/). وتلقي هجمات DDoS الكبيرة كمية ضخمة من حركة البيانات المزيفة على تطبيق مُعيّن، مما يؤدي إلى إرهاق سعة الشبكة. وتُعد شبكة Anycast من Cloudflare رائعة في التصدي لهذه الهجمات لأن حركة البيانات يتم توزيعها عبر الشبكة بأكملها، ويتم التخفيف منها بالقرب من مصدرها.

لا تراعي شبكة Anycast الحدود الإقليمية – فهي حتى لا تعلم عنها شيء. بسبب ذلك، لا يمكن لشركة Cloudflare، بشكل افتراضي، ضمان خدمة حركة البيانات من داخل بلد ما هناك أيضًا. وتصل الطلبات عادةً إلى مركز بيانات داخل الدولة المُصدّرة، ولكن من المحتمل أن يرسل مزود خدمة الإنترنت الخاص بالمستخدم حركة البيانات إلى شبكة قد تقوم بتوجيهها إلى بلد مختلف.

تحل الخدمات الإقليمية هذه المشكلة: فعند التشغيل، يصبح كل مركز بيانات على علم بالحدود المحددة بالخدمات الإقليمية التي تعمل فيها. إذا وصل مستخدم نهائي للعميل إلى مركز بيانات Cloudflare لا يتطابق مع المنطقة التي حددها العميل، فإننا ببساطة نقوم بتوجيه تدفق TCP الخام في شكل مشفّر. وبمجرد وصولها إلى مركز بيانات داخل المنطقة الصحيحة، نقوم بفك تشفير البيانات وتطبيق جميع منتجاتنا من الطبقة 7. وهذا يشمل منتجات مثل [CDN](https://www.cloudflare.com/application-services/products/cdn/)، [وWAF](https://www.cloudflare.com/application-services/products/waf/)، [وBot Management](https://www.cloudflare.com/application-services/products/bot-management/)، [وWorkers](https://www.cloudflare.com/developer-platform/workers/).

فلنضرب مثالاً. يوجد مستخدم نهائي للعميل في مدينة كيرالا بالهند، وقد حدد بروتوكول بوابة الحدود (BGP) أن مركز البيانات الأمثل لطلب المستخدم النهائي موجود في بمدينة كولمبو بسريلانكا. في هذا المثال، ربما يكون العميل قد اختار الهند كمنطقة وحيدة يجب خدمة حركة البيانات فيها. يرى مركز البيانات في كولمبو أن هذه الحركة مُخصّصة لمنطقة الهند. لا يقوم بفك تشفير البيانات، ولكن يقوم بدلاً من ذلك بإعادة توجيهها إلى مركز بيانات داخل الهند. وهناك نقوم بفك تشفير البيانات واستخدام منتجات مثل WAF وWorkers كما لو كانت حركة البيانات قد وصلت إلى مركز البيانات مباشرة. تستعيد الاستجابات من مركز البيانات داخل المنطقة نفس المسار عائدة إلى العميل.

تتوفر الإمكانات التي تقدمها خدماتنا الإقليمية الموسعة للوصول المبكر في أواخر شهر مايو 2024، ونخطط لإتاحتها بشكل عام في يونيو 2024. نحن متحمسون جدًا لقدرتنا على تطوير مجموعة أدوات توطين البيانات الخاصة بنا من أجل مساعدتك على تلبية احتياجات توطين البيانات الخاصة بك.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2412 Embedded Image - Lk4ngY](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45BDBTW12RERFBPF92Z66D.png&w=715&h=417&f=webp&fit=cover&position=center)

للتعرّف على هذه الإمكانات الموسعة أو إذا كنت مهتمًا باستخدام [مجموعة أدوات توطين البيانات](https://www.cloudflare.com/data-localization/)، يُرجى التواصل مع فريق حسابك.

في هذه الصفحة

ناقش عبر الإنترنت

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Far-ar%2Fexpanding-regional-services-configuration-flexibility-for-customers%2F&t=%D8%AA%D8%AD%D8%B3%D9%8A%D9%86%20%D9%85%D8%B1%D9%88%D9%86%D8%A9%20%D8%AA%D9%83%D9%88%D9%8A%D9%86%20%D8%A7%D9%84%D8%AE%D8%AF%D9%85%D8%A7%D8%AA%20%D8%A7%D9%84%D8%A5%D9%82%D9%84%D9%8A%D9%85%D9%8A%D8%A9%20%D9%84%D9%84%D8%B9%D9%85%D9%84%D8%A7%D8%A1)[](https://x.com/intent/post?text=%D8%AA%D8%AD%D8%B3%D9%8A%D9%86+%D9%85%D8%B1%D9%88%D9%86%D8%A9+%D8%AA%D9%83%D9%88%D9%8A%D9%86+%D8%A7%D9%84%D8%AE%D8%AF%D9%85%D8%A7%D8%AA+%D8%A7%D9%84%D8%A5%D9%82%D9%84%D9%8A%D9%85%D9%8A%D8%A9+%D9%84%D9%84%D8%B9%D9%85%D9%84%D8%A7%D8%A1&url=https%3A%2F%2Fblog.cloudflare.com%2Far-ar%2Fexpanding-regional-services-configuration-flexibility-for-customers%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Far-ar%2Fexpanding-regional-services-configuration-flexibility-for-customers%2F)[](https://bsky.app/intent/compose?text=%D8%AA%D8%AD%D8%B3%D9%8A%D9%86+%D9%85%D8%B1%D9%88%D9%86%D8%A9+%D8%AA%D9%83%D9%88%D9%8A%D9%86+%D8%A7%D9%84%D8%AE%D8%AF%D9%85%D8%A7%D8%AA+%D8%A7%D9%84%D8%A5%D9%82%D9%84%D9%8A%D9%85%D9%8A%D8%A9+%D9%84%D9%84%D8%B9%D9%85%D9%84%D8%A7%D8%A1+https%3A%2F%2Fblog.cloudflare.com%2Far-ar%2Fexpanding-regional-services-configuration-flexibility-for-customers%2F)[](https://mastodonshare.com/?text=%D8%AA%D8%AD%D8%B3%D9%8A%D9%86+%D9%85%D8%B1%D9%88%D9%86%D8%A9+%D8%AA%D9%83%D9%88%D9%8A%D9%86+%D8%A7%D9%84%D8%AE%D8%AF%D9%85%D8%A7%D8%AA+%D8%A7%D9%84%D8%A5%D9%82%D9%84%D9%8A%D9%85%D9%8A%D8%A9+%D9%84%D9%84%D8%B9%D9%85%D9%84%D8%A7%D8%A1&url=https%3A%2F%2Fblog.cloudflare.com%2Far-ar%2Fexpanding-regional-services-configuration-flexibility-for-customers%2F)[](https://www.threads.net/intent/post?text=%D8%AA%D8%AD%D8%B3%D9%8A%D9%86+%D9%85%D8%B1%D9%88%D9%86%D8%A9+%D8%AA%D9%83%D9%88%D9%8A%D9%86+%D8%A7%D9%84%D8%AE%D8%AF%D9%85%D8%A7%D8%AA+%D8%A7%D9%84%D8%A5%D9%82%D9%84%D9%8A%D9%85%D9%8A%D8%A9+%D9%84%D9%84%D8%B9%D9%85%D9%84%D8%A7%D8%A1+https%3A%2F%2Fblog.cloudflare.com%2Far-ar%2Fexpanding-regional-services-configuration-flexibility-for-customers%2F)

## الوسوم ذات الصلة

[Data Localization (AR)](https://blog.cloudflare.com/ar-ar/tag/data-localization/)

تابعنا على وسائل التواصل الاجتماعي

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## اشترك لتلقي إشعارات المنشورات الجديدة

عنوان البريد الإلكتروني

لن نشارك عنوان بريدك الإلكتروني أبدًا.

اشتراك

شكرًا لاشتراكك! راجع صندوق الوارد للتأكيد.
