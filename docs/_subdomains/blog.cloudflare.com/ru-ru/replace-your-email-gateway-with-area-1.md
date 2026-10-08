---
url: https://blog.cloudflare.com/ru-ru/replace-your-email-gateway-with-area-1/
title: \u041a\u0430\u043a \u0437\u0430\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u043e\u0447\u0442\u043e\u0432\u044b\u0439 \u0448\u043b\u044e\u0437 \u043d\u0430 Cloudflare Area 1 | \u0411\u043b\u043e\u0433 Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:42:42.857690+00:00
---

# Как заменить почтовый шлюз на Cloudflare Area 1 | Блог Cloudflare

> Source: https://blog.cloudflare.com/ru-ru/replace-your-email-gateway-with-area-1/

[Блог](https://blog.cloudflare.com/ru-ru/)

[Cloud Email Security](https://blog.cloudflare.com/ru-ru/tag/cloud-email-security/)[Cloudflare One Week](https://blog.cloudflare.com/ru-ru/tag/cloudflare-one-week/)[Cloudflare Zero Trust](https://blog.cloudflare.com/ru-ru/tag/cloudflare-zero-trust/)+4Показать ещё 4 тегов

7 теговПоказать 7 тегов

  * Теги публикации
  * [Zero Trust](https://blog.cloudflare.com/ru-ru/tag/zero-trust/)[Безопасность](https://blog.cloudflare.com/ru-ru/tag/security/)
  * Все теги
  * Подходящие теги
  * Теги не найдены
  * [1.1.1.1](https://blog.cloudflare.com/ru-ru/tag/1-1-1-1/)
  * [ИИ](https://blog.cloudflare.com/ru-ru/tag/ai/)
  * [Безопасность приложений](https://blog.cloudflare.com/ru-ru/tag/application-security/)
  * [Прикладные сервисы](https://blog.cloudflare.com/ru-ru/tag/application-services/)
  * [AWS](https://blog.cloudflare.com/ru-ru/tag/aws/)
  * [Управление ботами](https://blog.cloudflare.com/ru-ru/tag/bot-management/)
  * [Потребительские услуги](https://blog.cloudflare.com/ru-ru/tag/consumer-services/)
  * [DDoS](https://blog.cloudflare.com/ru-ru/tag/ddos/)
  * [DDoS Alerts (RU)](https://blog.cloudflare.com/ru-ru/tag/ddos-alerts/)
  * [Отчеты о DDoS](https://blog.cloudflare.com/ru-ru/tag/ddos-reports/)
  * [Разработчики](https://blog.cloudflare.com/ru-ru/tag/developers/)
  * [DNS](https://blog.cloudflare.com/ru-ru/tag/dns/)
  * [Мошенничество](https://blog.cloudflare.com/ru-ru/tag/fraud/)
  * [Воздействие](https://blog.cloudflare.com/ru-ru/tag/impact/)
  * [Жизнь в Cloudflare](https://blog.cloudflare.com/ru-ru/tag/life-at-cloudflare/)
  * [Сбой](https://blog.cloudflare.com/ru-ru/tag/outage/)
  * [Партнеры](https://blog.cloudflare.com/ru-ru/tag/partners/)
  * [Политика и право](https://blog.cloudflare.com/ru-ru/tag/policy/)
  * [Анализ после инцидента](https://blog.cloudflare.com/ru-ru/tag/post-mortem/)
  * [Конфиденциальность](https://blog.cloudflare.com/ru-ru/tag/privacy/)
  * [Новости](https://blog.cloudflare.com/ru-ru/tag/product-news/)
  * [Проект «Галилео»](https://blog.cloudflare.com/ru-ru/tag/project-galileo/)
  * [Radar](https://blog.cloudflare.com/ru-ru/tag/cloudflare-radar/)
  * [Безопасность](https://blog.cloudflare.com/ru-ru/tag/security/)
  * [Скорость и надежность](https://blog.cloudflare.com/ru-ru/tag/speed-and-reliability/)
  * [Прозрачность](https://blog.cloudflare.com/ru-ru/tag/transparency/)
  * [WAF](https://blog.cloudflare.com/ru-ru/tag/waf/)
  * [Zero Trust](https://blog.cloudflare.com/ru-ru/tag/zero-trust/)



[Email Security](https://blog.cloudflare.com/ru-ru/tag/email-security/)[Phishing](https://blog.cloudflare.com/ru-ru/tag/phishing/)[Zero Trust](https://blog.cloudflare.com/ru-ru/tag/zero-trust/)[Безопасность](https://blog.cloudflare.com/ru-ru/tag/security/)

[Cloud Email Security](https://blog.cloudflare.com/ru-ru/tag/cloud-email-security/)[Cloudflare One Week](https://blog.cloudflare.com/ru-ru/tag/cloudflare-one-week/)[Cloudflare Zero Trust](https://blog.cloudflare.com/ru-ru/tag/cloudflare-zero-trust/)[Email Security](https://blog.cloudflare.com/ru-ru/tag/email-security/)[Phishing](https://blog.cloudflare.com/ru-ru/tag/phishing/)[Zero Trust](https://blog.cloudflare.com/ru-ru/tag/zero-trust/)[Безопасность](https://blog.cloudflare.com/ru-ru/tag/security/)

20 июня 2022 г.

# Как заменить почтовый шлюз на Cloudflare Area 1

![Shalabh Mohan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW491RFMJARF117EF2268NPG.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Tarika Srinivasan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47RDAN04NY6SWQ4F3NCWQ3.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Shalabh Mohan](https://blog.cloudflare.com/ru-ru/author/shalabh/) и [Tarika Srinivasan](https://blog.cloudflare.com/ru-ru/author/tarika/)

10 мин. чтения

КОПИРОВАТЬ URL

Этот пост также доступен на [English](https://blog.cloudflare.com/replace-your-email-gateway-with-area-1/), [Español](https://blog.cloudflare.com/es-es/replace-your-email-gateway-with-area-1/), [日本語](https://blog.cloudflare.com/ja-jp/replace-your-email-gateway-with-area-1/), [한국어](https://blog.cloudflare.com/ko-kr/replace-your-email-gateway-with-area-1/), [简体中文](https://blog.cloudflare.com/zh-cn/replace-your-email-gateway-with-area-1/), [Polski](https://blog.cloudflare.com/pl-pl/replace-your-email-gateway-with-area-1/) и [Svenska](https://blog.cloudflare.com/sv-se/replace-your-email-gateway-with-area-1/).

![How to replace your email gateway with Cloudflare Area 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48MP9PWCM9EYY08KRM8GEW.png&w=1800&h=1013&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/vnn+fTi7urY6eTR7ebT8unY7+jY5uLT//vp+/bk8OrY6+PR7uTS8+jX8ejY6ePV//7s//jn8+za7ePR8OPR9ejW9OnZ7ObY///w//3q+PDe8ebV9ObU+erZ+O3c8evc///z///u/fbk9u3b+e3a/vHe/PLg9fDh///2///y//zq/PTj//Xi//jk//nl+fbl///4///1///u//vp//vo///p//7p/Prn///4///2///w//3r//7q///q///q/fvo)

Руководители и специалисты, ответственные за безопасность электронной почты, ежедневно существуют в следующих реалиях. Электронная почта, скорее всего, доставляется через облако и имеет встроенную защиту, которая неплохо справляется со спамом и распространенным вредоносным ПО. Потрачено, вероятно, немало времени и средств, выделен персонал для обслуживания безопасного шлюза электронной почты (SEG), чтобы обеспечить защиту от фишинга, вредоносного ПО и других угроз, связанных с электронной почтой. Несмотря на это, электронная почта по-прежнему остается основным источником интернет-угроз: исследование Deloitte показало, что 91 % всех кибератак начинается с фишинга.

SEG и сервисы защиты от фишинга существуют уже давно, почему же до сих пор такое количество фишинговых сообщений попадает в почтовые ящики? Если воспользоваться [бритвой Оккама](https://en.wikipedia.org/wiki/Occam's_razor), причина в том, что SEG разрабатывались не для современных почтовых сред и не способны надежно блокировать современные фишинговые атаки.

Если же вам нужны более веские доводы, чем бритва Оккама, читайте дальше.

### Почему мир отказывается от SEG

Наиболее заметное изменение на рынке электронной почты, делающее ненужным традиционные SEG — переход к облачно-ориентированным почтовым сервисам. [По сведениям Gartner](https://www.gartner.com/en/newsroom/press-releases/2021-11-10-gartner-says-cloud-will-be-the-centerpiece-of-new-digital-experiences)®, к 2025 году более 85 % организаций возьмут на вооружение стратегию «облако в первую очередь». Организации, ожидающие от своих средств безопасности облачной масштабируемости, отказоустойчивости и гибкости, не могут рассчитывать на традиционные устройства, такие как SEG.

Говоря конкретнее об электронной почте, [Gartner® отмечает](https://www.gartner.com/document/4006566), что «передовые средства безопасности электронной почты все чаще представляют собой интегрированные облачные решения для защиты почты, а не шлюз». К 2023 году по меньшей мере 40 % организаций будут использовать вместо SEG встроенные средства защиты облачных почтовых сервисов. Сегодня электронная почта приходит отовсюду и рассылается повсюду, SEG перед сервером Exchange является анахронизмом, а поместить SEG перед облачными почтовыми ящиками — едва ли выполнимая задача в мобильном мире, где приоритет за удаленной работой. [Защита электронной почты](https://www.cloudflare.com/learning/email-security/what-is-email-security/) сегодня должна следовать за пользователем, находиться рядом с почтовым ящиком и присутствовать буквально повсюду.

SEG не только отстают от времени с точки зрения архитектуры, они также не справляются с обнаружением сложных атаках, использующих фишинг и социальную инженерию. Это связано с тем, что SEG изначально разрабатывались с целью предотвращения спама, для которого характерны большие объемы и для обнаружения и устранения которого требуются большие выборки. Но сегодняшние фишинговые атаки больше похожи на снайперские выстрелы, а не на пальбу по площадям. Они имеют небольшой объем, узконаправлены и эксплуатируют наше интуитивное доверие к почтовым сообщениям с целью кражи денег и данных. Для обнаружения современных фишинговых атак требуются сложные и ресурсоемкие средства анализа электронной почты и алгоритмы обнаружения угроз, которые SEG не способны обеспечить в больших масштабах.

Устаревшая методология обнаружения, используемая в SEG, ярче всего проявляется в том, что администраторам приходится создавать и настраивать огромное количество политик почтовых угроз. В отличие от большинства других кибератак, фишинг и [компрометация корпоративной электронной почты (Business Email Compromise, BEC)](https://www.cloudflare.com/learning/email-security/business-email-compromise-bec/) содержат слишком много «нечетких» сигналов и не могут быть обнаружены с помощью одних только детерминистических выражений «если... то». Кроме того, злоумышленники не стоят на месте: пока вы создаете политики почтовых угроз, они быстро адаптируются и меняют методы, чтобы обойти только что созданные вами правила. Полагаться для предотвращения фишинга на настройки SEG — все равно, что играть в игру, где преимущество заведомо на стороне злоумышленника.

### Чтобы предотвратить фишинг, нужно двигаться вперед

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1155 Embedded Image - lnOHVY](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49AHBZ8WE55RJQTHW1N55Y.png&w=715&h=745&f=webp&fit=cover&position=center)

Традиционные средства защиты электронной почты полагаются на знание характеристик прошлых атак (данные о репутации, сигнатуры угроз) для обнаружения следующей кибератаки, и потому не могут обеспечить надежную защиту от современных, постоянно меняющихся фишинговых атак.

Необходима технология превентивной безопасности, которая не только обладает информацией о вредоносном коде, веб-сайтах и методах, использовавшихся в целях фишинга в прошлом, но и способна упредить следующие действия злоумышленников. Какие сайты и учетные записи они компрометируют или создают для использования в завтрашних атаках? Что и каким образом они готовятся использовать в ходе этих атак? Где они «прощупывают почву» перед атакой?

Cloudflare Area 1 превентивно сканирует Интернет для выявления инфраструктуры злоумышленников и фишинговых кампаний, находящихся в стадии разработки. Поисковые роботы Area 1, ориентированные на обнаружение угроз, динамически анализируют подозрительные веб-страницы и вредоносный код, а также постоянно обновляют модели обнаружения по мере развития тактики злоумышленников. Все это делается для того, чтобы предотвращать фишинговые атаки еще за несколько дней до того, как они доберутся до почтового ящика.

В сочетании с 1+ трлн DNS-запросов, наблюдаемых [Cloudflare Gateway](https://www.cloudflare.com/products/zero-trust/gateway/), данный корпус аналитических данных об угрозах позволяет клиентам предотвращать попытки фишинга на самой ранней стадии цикла атаки. Кроме того, использование глубокой контекстной аналитики для понимания тональности, тона, смысловой направленности и вариативности сообщений позволяет Area 1 отличать нормальную деловую переписку от изощренных фальсификаций.

Мы являемся убежденными сторонниками многоуровневой системы безопасности, однако уровни не должны быть избыточными. SEG дублирует множество функций, которые теперь предоставляются клиентам облачными почтовыми сервисами. Area 1 предназначена для усиления, а не дублирования, встроенной защиты электронной почты и для блокирования фишинговых атак, которым удается преодолеть начальные уровни защиты.

### План замены SEG

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1155 Embedded Image - dVe4kK](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49N17T976H10Q30BXGMNJ8.png&w=715&h=493&f=webp&fit=cover&position=center)

Лучше всего начать работу по замене SEG с принятия решения, будет ли это полная замена или поэтапная замена, которая начнется с подключения в качестве дополнительного компонента. Многие клиенты Cloudflare Area 1 уже осуществили замену своих SEG (подробнее об этом ниже), однако в некоторых случаях клиенты предпочитают вначале подключить Cloudflare Area 1 в качестве дополнительного звена в цепочке после SEG, чтобы оценить эффективность обоих сервисов, а затем принять окончательное решение. Мы обеспечиваем простоту процесса в любом случае!

Начиная проект, важно привлечь к нему все заинтересованные стороны. Как минимум, необходимо привлечь ИТ-администратора, чтобы не допустить сбоев доставки электронной почты и снижения производительности, а также администратора информационной безопасности для контроля эффективности обнаружения угроз. В число заинтересованных сторон может входить реселлер, если вы используете его в процессе закупок, а также специалист по защите данных и соблюдению нормативных требований, контролирующий процедуру обработки данных.

Далее вам следует определиться с архитектурой подключения Cloudflare Area 1. Cloudflare Area 1 может подключаться с помощью записи MX через API, возможно также одновременное использование нескольких режимов подключения. Мы рекомендуем подключить Cloudflare Area 1 с помощью записи MX, это обеспечит наиболее эффективную защиту от внешних угроз и позволит сервису вписаться в вашу среду в соответствии с вашей бизнес-логикой и конкретными потребностями.

Последний этап подготовки — составление схемы потоков электронной почты. Если у вас несколько доменов, определите, куда направляются электронные письма с каждого из ваших доменов. Проверьте различные уровни маршрутизации, например: не используются ли агенты передачи почты (MTA) для перенаправления входящих сообщений? Хорошее понимание логических и физических уровней SMTP в организации обеспечит надлежащую маршрутизацию сообщений. Обсудите, какой почтовый трафик должен сканироваться с помощью Cloudflare Area 1 (север-юг, восток-запад, оба) и как это согласуется с существующими политиками электронной почты.

### Реализация плана перехода

**Шаг 1. Внедрение защиты электронной почты** Основные шаги, которые необходимо выполнить при подключении Cloudflare Area 1 с помощью записи MX (требуемое время: ~30 минут):

  * Настройте ваш почтовый сервис для приема почты из Cloudflare Area 1.
  * Убедитесь, что для исходящих IP-адресов Cloudflare Area 1 не установлено ограничение числа запросов или блокировка, поскольку это может повлиять на доставку сообщений.
  * Если ваш сервер электронной почты размещен в локальной инфраструктуре, обновите правила межсетевого экрана, чтобы разрешить доставку почты на него из Cloudflare Area 1.
  * Настройте правила реагирования (например, помещать в карантин, добавлять префикс к теме или тексту сообщения и т. д.).
  * Протестируйте почтовый поток, отправляя сообщения через Cloudflare Area 1, чтобы убедиться в правильности доставки. (Наши специалисты могут оказать вам помощь на данном этапе).
  * Обновите записи MX, чтобы они указывали на Cloudflare Area 1.



Ниже приведена последовательность шагов при подключении Cloudflare Area 1 в качестве дополнительного звена в цепочке после другого средства защиты электронной почты (требуемое время: ~ 30 минут):

  * Выполните правильную настройку обратного просмотра в Cloudflare Area 1, чтобы Cloudflare Area 1 могла обнаруживать исходный IP-адрес отправителя.
  * Если ваш сервер электронной почты размещен в локальной инфраструктуре, обновите правила межсетевого экрана, чтобы разрешить доставку почты на него из Cloudflare Area 1.
  * Настройте правила реагирования (например, помещать в карантин, добавлять префикс к теме или тексту сообщения и т. д.).
  * Протестируйте почтовый поток, отправляя сообщения через Cloudflare Area 1, чтобы убедиться в правильности доставки. (Наши специалисты могут оказать вам помощь на данном этапе).
  * Обновите маршруты доставки на SEG, чтобы вся почта направлялась в Cloudflare Area 1, а не на почтовые серверы.



**Шаг 2. Интеграция DNS** Следующий шаг, который обычно выполняется после настройки электронной почты, — интеграция Cloudflare Area 1 в сервис DNS. Если вы являетесь клиентом Cloudflare Gateway, у нас для вас хорошая новость: Cloudflare Area 1 теперь использует Cloudflare Gateway в качестве [рекурсивного DNS](https://www.cloudflare.com/learning/dns/what-is-recursive-dns/), что позволяет предотвратить доступ конечных пользователей к фишинговым и вредоносным сайтам по ссылкам в письмах или при просмотре веб-страниц.

**Шаг 3. Интеграция с сервисами мониторинга и реагирования на проблемы безопасности** Подробная настраиваемая отчетность Cloudflare Area 1 дает возможность оперативного мониторинга угроз. Интеграции с SIEM через отказоустойчивые API позволяет легко соотнести обнаруженные Cloudflare Area 1 угрозы с событиями в сети, на конечных точках и в других инструментах безопасности, что упрощает управление инцидентами.

Cloudflare Area 1 имеет встроенные средства реагирования и изъятия сообщений, позволяющие клиентам противодействовать угрозам непосредственно на информационной панели Cloudflare Area 1. Помимо этого, многие организации осуществляют интеграцию со средствами оркестрации, что дает возможность настройки пользовательских схем реагирования. Многие клиенты используют наши перехватчики API, обеспечивающие интеграцию с сервисами SOAR, для управления процессами реагирования на угрозы в своей организации.

### Показатели для измерения успеха

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1155 Embedded Image - StP8R8](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4874W3FP54E9361FM0MB0R.png&w=715&h=298&f=webp&fit=cover&position=center)

Как убедиться, что замена SEG прошла успешно и дала желаемый эффект? Мы рекомендуем измерять показатели, касающиеся эффективности обнаружения и простоты эксплуатации.

Что касается обнаружения, самый очевидный показатель — количество и характер блокируемых фишинговых атак до и после внедрения. Наблюдаете ли вы новые типы блокируемых фишинговых атак, которых вы не отмечали ранее? Есть ли у вас возможность мониторинга кампаний, затрагивающих сразу несколько почтовых ящиков? Еще один связанный с обнаружением показатель, о котором следует помнить, — количество ложных срабатываний.

С эксплуатационной точки зрения крайне важно, чтобы не снижалась производительность электронной почты. Хорошим косвенным индикатором может служить количество заявок в службу поддержки, связанных с доставкой электронной почты. Доступность и время бесперебойной работы сервиса защиты электронной почты — еще один ключевой показатель, на который следует обратить внимание.

Наконец — и это, возможно, самое важное — посчитайте, сколько времени ваша служба безопасности тратит на защиту электронной почты. Будем надеяться, гораздо меньше, чем раньше! Как известно, SEG представляет собой весьма трудозатратное решение с точки зрения текущего технического обслуживания. Если Cloudflare Area 1 позволит высвободить время ваших специалистов для работы над другими неотложными проблемами безопасности, это не менее значимо, чем предотвращение фишинга.

### Вы в хорошей компании

Мы предлагаем вашему вниманию план замены SEG, поскольку многие наши клиенты уже провели такую замену и довольны результатами.

Так, например, глобальная страховая компания из списка Fortune 50, обслуживающая 90 миллионов клиентов в более чем 60 странах, обнаружила, что ее SEG недостаточно эффективен для предотвращения фишинговых атак. В частности, приходилось тратить немало усилий на поиск "просочившихся" фишинговых писем, которым удалось пройти через SEG и попасть в папку «Входящие». Им требовался сервис защиты электронной почты, который смог бы перехватывать такие фишинговые атаки, поддерживая при этом гибридную архитектуру, включающую как облачные, так и локальные почтовые ящики.

После развертывания Cloudflare Area 1 в качестве дополнительного звена в цепочке доставки после Microsoft 365 и SEG наш клиент за первый месяц смог заблокировать более 14 000 фишинговых угроз, при этом ни одно из этих фишинговых сообщений не достигло почтового ящика пользователя. Благодаря одномоментной интеграции с существующей инфраструктурой электронной почты не возникло практически никаких проблем с обслуживанием и эксплуатацией. Кроме того, автоматическое изъятие сообщений и средства защиты после доставки, обеспечиваемые Cloudflare Area 1, позволили страховой компании с легкостью находить и нейтрализовывать пропущенные фишинговые письма.

Если вы хотите связаться с кем-либо из наших клиентов, которые уже воспользовались Cloudflare Area 1 в качестве дополнения или замены SEG, обратитесь к вашему менеджеру по работе с клиентами, чтобы узнать подробнее. Если вы хотите увидеть Cloudflare Area 1 в действии, [здесь](https://www.cloudflare.com/lp/emailsecurity/) вы можете отправить запрос на оценку риска фишинга.

Замену SEG имеет смысл включить в ваш общий [план внедрения Zero Trust](https://zerotrustroadmap.org/). Чтобы получить полную информацию о Cloudflare One Week и новых возможностях, посетите наш [итоговый вебинар](https://gateway.on24.com/wcc/eh/2153307/lp/3824611/the-evolution-of-cloudflare-one).

1Пресс-релиз Gartner, «[По мнению Gartner, облако станет центральным элементом новых цифровых ресурсов](https://www.gartner.com/en/newsroom/press-releases/2021-11-10-gartner-says-cloud-will-be-the-centerpiece-of-new-digital-experiences)», 11 ноября 2021 г.2Gartner, «Справочник по рынку средств защиты электронной почты», 7 октября 2021 г., Марк Харрис, Питер Фёстбрук, Равиша Чуг, Марио де БурGARTNER является зарегистрированным товарным знаком и знаком обслуживания Gartner, Inc. и/или аффилированных с ней компаний в США и других странах и используется здесь с разрешения владельца. Все права сохраняются.

На этой странице

Обсудить онлайн

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2Freplace-your-email-gateway-with-area-1%2F&t=%D0%9A%D0%B0%D0%BA%20%D0%B7%D0%B0%D0%BC%D0%B5%D0%BD%D0%B8%D1%82%D1%8C%20%D0%BF%D0%BE%D1%87%D1%82%D0%BE%D0%B2%D1%8B%D0%B9%20%D1%88%D0%BB%D1%8E%D0%B7%20%D0%BD%D0%B0%20Cloudflare%20Area%201)[](https://x.com/intent/post?text=%D0%9A%D0%B0%D0%BA+%D0%B7%D0%B0%D0%BC%D0%B5%D0%BD%D0%B8%D1%82%D1%8C+%D0%BF%D0%BE%D1%87%D1%82%D0%BE%D0%B2%D1%8B%D0%B9+%D1%88%D0%BB%D1%8E%D0%B7+%D0%BD%D0%B0+Cloudflare+Area+1&url=https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2Freplace-your-email-gateway-with-area-1%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2Freplace-your-email-gateway-with-area-1%2F)[](https://bsky.app/intent/compose?text=%D0%9A%D0%B0%D0%BA+%D0%B7%D0%B0%D0%BC%D0%B5%D0%BD%D0%B8%D1%82%D1%8C+%D0%BF%D0%BE%D1%87%D1%82%D0%BE%D0%B2%D1%8B%D0%B9+%D1%88%D0%BB%D1%8E%D0%B7+%D0%BD%D0%B0+Cloudflare+Area+1+https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2Freplace-your-email-gateway-with-area-1%2F)[](https://mastodonshare.com/?text=%D0%9A%D0%B0%D0%BA+%D0%B7%D0%B0%D0%BC%D0%B5%D0%BD%D0%B8%D1%82%D1%8C+%D0%BF%D0%BE%D1%87%D1%82%D0%BE%D0%B2%D1%8B%D0%B9+%D1%88%D0%BB%D1%8E%D0%B7+%D0%BD%D0%B0+Cloudflare+Area+1&url=https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2Freplace-your-email-gateway-with-area-1%2F)[](https://www.threads.net/intent/post?text=%D0%9A%D0%B0%D0%BA+%D0%B7%D0%B0%D0%BC%D0%B5%D0%BD%D0%B8%D1%82%D1%8C+%D0%BF%D0%BE%D1%87%D1%82%D0%BE%D0%B2%D1%8B%D0%B9+%D1%88%D0%BB%D1%8E%D0%B7+%D0%BD%D0%B0+Cloudflare+Area+1+https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2Freplace-your-email-gateway-with-area-1%2F)

## Связанные теги

[Cloud Email Security](https://blog.cloudflare.com/ru-ru/tag/cloud-email-security/)[Cloudflare One Week](https://blog.cloudflare.com/ru-ru/tag/cloudflare-one-week/)[Cloudflare Zero Trust](https://blog.cloudflare.com/ru-ru/tag/cloudflare-zero-trust/)[Email Security](https://blog.cloudflare.com/ru-ru/tag/email-security/)[Phishing](https://blog.cloudflare.com/ru-ru/tag/phishing/)[Zero Trust](https://blog.cloudflare.com/ru-ru/tag/zero-trust/)[Безопасность](https://blog.cloudflare.com/ru-ru/tag/security/)

Подписывайтесь в социальных сетях

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Подпишитесь на уведомления о новых публикациях

Электронная почта

Мы никогда не передаем ваш адрес электронной почты третьим лицам.

Подписаться

Спасибо за подписку! Проверьте папку «Входящие», чтобы подтвердить подписку.
