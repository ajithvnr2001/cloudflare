---
url: https://blog.cloudflare.com/ru-ru/october-2021-facebook-outage/
title: \u041a\u0430\u043a Facebook \u0438\u0441\u0447\u0435\u0437 \u0438\u0437 \u0418\u043d\u0442\u0435\u0440\u043d\u0435\u0442\u0430 | \u0411\u043b\u043e\u0433 Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:42:59.632070+00:00
---

# Как Facebook исчез из Интернета | Блог Cloudflare

> Source: https://blog.cloudflare.com/ru-ru/october-2021-facebook-outage/

[Блог](https://blog.cloudflare.com/ru-ru/)

[BGP](https://blog.cloudflare.com/ru-ru/tag/bgp/)[DNS](https://blog.cloudflare.com/ru-ru/tag/dns/)[Facebook](https://blog.cloudflare.com/ru-ru/tag/facebook/)+2Показать ещё 2 тегов

5 теговПоказать 5 тегов

  * Теги публикации
  * [DNS](https://blog.cloudflare.com/ru-ru/tag/dns/)[Сбой](https://blog.cloudflare.com/ru-ru/tag/outage/)
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



[Trends](https://blog.cloudflare.com/ru-ru/tag/trends/)[Сбой](https://blog.cloudflare.com/ru-ru/tag/outage/)

[BGP](https://blog.cloudflare.com/ru-ru/tag/bgp/)[DNS](https://blog.cloudflare.com/ru-ru/tag/dns/)[Facebook](https://blog.cloudflare.com/ru-ru/tag/facebook/)[Trends](https://blog.cloudflare.com/ru-ru/tag/trends/)[Сбой](https://blog.cloudflare.com/ru-ru/tag/outage/)

4 октября 2021 г.

# Как Facebook исчез из Интернета

![Celso Martinho](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45K1GG0634XMEFX9CSSGM2.png&w=64&h=64&f=webp&fit=cover&position=center)![Tom Strickx](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46SA24D9KSWM8WR9ZTW1BJ.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Celso Martinho](https://blog.cloudflare.com/ru-ru/author/celso/) и [Tom Strickx](https://blog.cloudflare.com/ru-ru/author/tom-strickx/)

7 мин. чтения

КОПИРОВАТЬ URL

Этот пост также доступен на [English](https://blog.cloudflare.com/october-2021-facebook-outage/), [Deutsch](https://blog.cloudflare.com/de-de/october-2021-facebook-outage/), [Español](https://blog.cloudflare.com/es-es/october-2021-facebook-outage/), [Français](https://blog.cloudflare.com/fr-fr/october-2021-facebook-outage/), [Italiano](https://blog.cloudflare.com/it-it/october-2021-facebook-outage/), [日本語](https://blog.cloudflare.com/ja-jp/october-2021-facebook-outage/), [한국어](https://blog.cloudflare.com/ko-kr/october-2021-facebook-outage/), [繁體中文](https://blog.cloudflare.com/zh-tw/october-2021-facebook-outage/), [简体中文](https://blog.cloudflare.com/zh-cn/october-2021-facebook-outage/) и [Português](https://blog.cloudflare.com/pt-br/october-2021-facebook-outage/).

![Understanding how Facebook disappeared from the Internet](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49302W8F0CG37JWQ2N1424.png&w=896&h=466&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/////f397u7u5OTk5eXl6urq7Ozs6enp/////v7+7u7u4+Pj5eXl7Ozs7+/v7Ozs////////7+/v4+Pj5ubm7+/v8vLy7+/v////////8/Pz5+fn6enp8/Pz9/f38/Pz////////+fn57e3t7+/v+Pj4+/v7+Pj4////////////9fX19vb2/Pz8/////Pz8////////////+/v7+/v7/////////////////////////f39/f39////////////)

«Не мог же Фейсбук упасть?» – подумали мы на какое-то мгновение.

Сегодня в 15:51 UTC мы открыли внутренний инцидент под названием "DNS-поиск для Facebook возвращает SERVFAIL", поскольку забеспокоились, что что-то не так с нашим DNS-резолвером [1.1.1.1](https://developers.cloudflare.com/warp-client/). Мы уже собирались сделать пост на нашей публичной [странице состояния](https://www.cloudflarestatus.com/), но тут стало ясно, что происходит нечто более серьезное.

Социальные сети взорвались сообщениями, которые и наши инженеры быстро подтвердили. Facebook, а также принадлежащие ему сервисы WhatsApp и Instagram, действительно упали. Их DNS-имена перестали разрешаться, а IP-адреса инфраструктуры стали недоступны. Словно кто-то разом «выдернул кабели» из их центров обработки данных и отключил их от Интернета.

Это не было проблемой DNS, однако сбой DNS стал первым симптомом более масштабного сбоя в работе Facebook.

Как такое вообще возможно?

### Сообщение Facebook

Facebook [опубликовал у себя в блоге сообщение](https://engineering.fb.com/2021/10/04/networking-traffic/outage/) с некоторыми подробностями того, что произошло внутри компании. Со стороны мы наблюдали проблемы с BGP и DNS, описанные в данном посте, но на самом деле проблема началась с изменения конфигурации, которое затронуло всю внутреннюю магистральную сеть. Это вызвало целую цепочку последствий, Facebook и другие ресурсы исчезли из сети, при этом собственные сотрудники Facebook столкнулись с трудностями, пытаясь восстановить работу сервиса.

Facebook опубликовал [еще одну запись в блоге](https://engineering.fb.com/2021/10/05/networking-traffic/outage-details/) с гораздо более подробной информацией о том, что произошло. В их посте – взгляд изнутри, в нашем – взгляд со стороны.

Теперь перейдем к тому, что мы увидели со своей стороны.

### Знакомьтесь с BGP

[BGP](https://www.cloudflare.com/learning/security/glossary/what-is-bgp/) расшифровывается как Border Gateway Protocol (Протокол граничного шлюза). Это механизм обмена информацией о маршрутизации между автономными системами (AS) в Интернете. Крупные маршрутизаторы, обеспечивающие работу Интернета, имеют огромные, постоянно обновляемые списки возможных маршрутов, по которым каждый сетевой пакет может быть доставлен в конечный пункт назначения. Без BGP маршрутизаторы Интернета не знали бы, что им делать, и Интернет не смог бы работать.

Интернет – это в буквальном смысле сеть сетей, и они связаны между собой при помощи BGP. BGP позволяет одной сети (скажем, Facebook) анонсировать свое присутствие другим сетям, образующим Интернет. В данный момент Facebook не анонсирует свое присутствие, интернет-провайдеры и другие сети не могут найти сеть Facebook, и поэтому она недоступна.

Каждая отдельная сеть имеет свой ASN: Autonomous System Number (Номер автономной системы). Автономная система (AS) – это отдельная сеть с единой политикой внутренней маршрутизации. AS может формировать собственные префиксы (означающие, что она контролирует группу IP-адресов), а также транзитные префиксы (означающие, что она знает путь к определенной группе IP-адресов).

Cloudflare имеет ASN [AS13335](https://www.peeringdb.com/asn/13335). Каждый ASN должен анонсировать в Интернете маршруты к своим префиксам с помощью BGP, иначе никто не будет знать, как подключиться и где нас найти.

В нашем [учебном центре](https://www.cloudflare.com/learning/) имеется подробный обзор [BGP](https://www.cloudflare.com/learning/security/glossary/what-is-bgp/) и [ASN](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/) и принципа их работы.

На этой упрощенной схеме изображены шесть автономных систем в Интернете и два возможных маршрута, по которым пакет может пройти от начала до конца. AS1 → AS2 → AS3 – наиболее быстрый маршрут, а AS1 → AS6 → AS5 → AS4 → AS3 – наиболее медленный, но его можно использовать, если первый не сработает.

В 15:58 UTC мы заметили, что Facebook перестал анонсировать маршруты к своим префиксам DNS. Это означало, что, как минимум, DNS-серверы Facebook недоступны. Поэтому DNS-резолвер Cloudflare 1.1.1.1 больше не мог отвечать на запросы, требующие сообщить IP-адрес домена facebook.com.

Тем временем другие IP-адреса Facebook по-прежнему маршрутизировались, но от них не было особой пользы, поскольку без DNS Facebook и связанные с ним сервисы были фактически недоступны:

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-748 Embedded Image - wRTugX](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45QV6QN6HCR7TCAPRRKXSV.png&w=715&h=333&f=webp&fit=cover&position=center)

Мы отслеживаем все обновления и анонсы BGP, поступающие в нашу глобальную сеть. Благодаря масштабу нашей сети собираемые данные дают нам представление о связях в Интернете и о том, откуда и куда должен направляться трафик в любой точке планеты.
    
    
    route-views>show ip bgp 185.89.218.0/23
    % Network not in table
    route-views>
    
    route-views>show ip bgp 129.134.30.0/23
    % Network not in table
    route-views>

Сообщение BGP UPDATE информирует маршрутизатор о любых изменениях в анонсе префикса или полностью отзывает префикс. Если обратиться к нашей базе данных временных рядов BGP, хорошо видно количество обновлений, полученных нами от Facebook. Обычно этот график довольно спокойный: Facebook не вносит изменения в свою сеть ежеминутно.
    
    
    route-views>show ip bgp 129.134.30.0   
    BGP routing table entry for 129.134.0.0/17, version 1025798334
    Paths: (24 available, best #14, table default)
      Not advertised to any peer
      Refresh Epoch 2
      3303 6453 32934
        217.192.89.50 from 217.192.89.50 (138.187.128.158)
          Origin IGP, localpref 100, valid, external
          Community: 3303:1004 3303:1006 3303:3075 6453:3000 6453:3400 6453:3402
          path 7FE1408ED9C8 RPKI State not found
          rx pathid: 0, tx pathid: 0
      Refresh Epoch 1
    route-views>

Но примерно в 15:40 UTC мы увидели резкий всплеск изменений маршрутизации со стороны Facebook. Тогда-то и начались проблемы.

Если разбить этот график на анонсы и отзывы маршрутов, станет еще яснее, что произошло. Маршруты были отозваны, DNS-серверы Facebook ушли в офлайн, и уже через минуту после возникновения проблемы инженеры Cloudflare сидели и недоумевали, почему 1.1.1.1 не выдает IP для facebook.com, и беспокоились, что это вызвано каким-то сбоем в наших системах.

В результате отзыва маршрутов Facebook и его сайты фактически отключились от Интернета.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-748 Embedded Image - L5L3lR](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47THAPEAR479FRS31Z47ZY.png&w=715&h=238&f=webp&fit=cover&position=center)

### DNS тоже пострадал

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-748 Embedded Image - nvy16f](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48HXX238XJCMQDZ2YYK843.png&w=715&h=92&f=webp&fit=cover&position=center)

Прямым следствием произошедшего стало то, что DNS-резолверы по всему миру перестали выдавать IP-адреса этих доменных имен.

Это произошло потому, что DNS, как и многие другие системы в Интернете, также имеет свой механизм маршрутизации. Когда кто-либо набирает в браузере URL [https://facebook.com](https://facebook.com/), DNS-резолвер, отвечающий за преобразование доменных имен в IP-адреса, с которыми устанавливается соединение, сначала проверяет, нет ли IP-адреса у него в кэше, и если есть, использует его. Если нет, он пытается получить ответ от сервера имен соответствующего домена, расположенного, как правило, в организации, которой домен принадлежит.

Если серверы имен недоступны или не отвечают по какой-либо другой причине, возвращается ответ SERVFAIL, и браузер выдает пользователю ошибку.
    
    
    ➜  ~ dig @1.1.1.1 facebook.com
    ;; ->>HEADER<<- opcode: QUERY, status: SERVFAIL, id: 31322
    ;facebook.com.			IN	A
    ➜  ~ dig @1.1.1.1 whatsapp.com
    ;; ->>HEADER<<- opcode: QUERY, status: SERVFAIL, id: 31322
    ;whatsapp.com.			IN	A
    ➜  ~ dig @8.8.8.8 facebook.com
    ;; ->>HEADER<<- opcode: QUERY, status: SERVFAIL, id: 31322
    ;facebook.com.			IN	A
    ➜  ~ dig @8.8.8.8 whatsapp.com
    ;; ->>HEADER<<- opcode: QUERY, status: SERVFAIL, id: 31322
    ;whatsapp.com.			IN	A

Опять-таки, в нашем учебном центре имеется [подробное объяснение](https://www.cloudflare.com/learning/dns/what-is-dns/) принципа работы DNS.

Поскольку Facebook перестал анонсировать по BGP маршруты к своим префиксам DNS, наши и все прочие DNS-резолверы утратили возможность подключаться к его серверам имен. Соответственно, 1.1.1.1, 8.8.8.8 и другие крупные публичные DNS-резолверы начали выдавать (и кэшировать) ответы SERVFAIL.

Но это еще не все. Теперь в дело вступает человеческий фактор и логика работы приложений, вызывая еще один экспоненциальный эффект. Возникает цунами дополнительного DNS-трафика.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-748 Embedded Image - IgzFBP](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49DET92BASKTZJXN8917AC.png&w=715&h=178&f=webp&fit=cover&position=center)

Это происходит отчасти потому, что приложения не принимают ошибку за ответ и начинают повторять попытки, порой очень интенсивно, а отчасти потому, что конечные пользователи также не принимают ошибку за ответ и начинают перезагружать страницы или закрывать и перезапускать приложения, иногда тоже весьма интенсивно.

Вот рост трафика (по числу запросов), который мы наблюдали на 1.1.1.1:

Таким образом, поскольку Facebook и его сайты привлекают огромный трафик, DNS-резолверы по всему миру теперь вынуждены обрабатывать в 30 раз больше запросов, чем обычно, что чревато задержками и таймаутами для других платформ.

К счастью, 1.1.1.1 — бесплатный, приватный, быстрый (что может подтвердить независимый DNS-монитор [DNSPerf](https://www.dnsperf.com/#!dns-resolvers)) и масштабируемый сервис, что позволило нам продолжать обслуживать пользователей практически в штатном режиме.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-748 Embedded Image - hTDAlR](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW497HENY4XCCDJABGN68JAW.png&w=715&h=195&f=webp&fit=cover&position=center)

Время ответа на подавляющее большинство наших DNS-запросов составило менее 10 мс. В то же время у крайне небольшой части перцентилей p95 и p99 время отклика увеличилось — вероятно, из-за того, что истекшие TTL вынуждали обращаться к серверам имен Facebook с последующим таймаутом. 10-секундный таймаут в системе DNS хорошо известен инженерам.

### Влияние на другие сервисы

Пользователи начинают искать альтернативы, хотят узнать подробности или обсудить происходящее. Когда Facebook стал недоступен, мы увидели рост числа DNS-запросов к Twitter, Signal и другим платформам обмена сообщениями и социальным сетям.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-748 Embedded Image - EENGLi](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48QYAJWRMW35XT4C0Z8VJC.png&w=715&h=365&f=webp&fit=cover&position=center)

Еще один побочный эффект недоступности сказался на нашем WARP-трафике к сети Facebook (ASN 32934) и обратно. Этот график показывает, как изменился трафик в каждой стране с 15:45 UTC до 16:45 UTC по сравнению с тремя часами ранее. По всему миру WARP-трафик к сети Facebook и обратно просто исчез.

### Интернет

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-748 Embedded Image - s2ixow](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46NC41GF5RJ2AMJ76TRRW6.png&w=715&h=238&f=webp&fit=cover&position=center)

Сегодняшние события – мягкое напоминание о том, что Интернет представляет собой очень сложную и взаимозависимую систему, состоящую из миллионов систем и протоколов, работающих вместе. Доверие, стандартизация и сотрудничество между организациями являются ключевыми факторами, обеспечивающими его работоспособность для почти пяти миллиардов активных пользователей по всему миру.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-748 Embedded Image - TVyw87](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48DM95BTETHDBN7CHBJE3M.png&w=715&h=358&f=webp&fit=cover&position=center)

### Обновление

Примерно в 21:00 UTC мы заметили возобновление активности BGP со стороны сети Facebook, она достигла пика в 21:17 UTC.

На данном графике показана доступность DNS-имени facebook.com на DNS-резолвере Cloudflare 1.1.1.1. Доступность пропала примерно в 15:50 UTC и восстановилась в 21:20 UTC.

Сервисам Facebook, WhatsApp и Instagram наверняка потребуется еще какое-то время, чтобы вернуться в строй, но по состоянию на 21:28 UTC Facebook, похоже, восстановил подключение к глобальному Интернету, и его DNS вновь работает.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-748 Embedded Image - x3F1Fn](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46GFAV9E0ZN65A7GGTDAC7.png&w=715&h=136&f=webp&fit=cover&position=center)

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-748 Embedded Image - 9q2aQ7](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47TFW3V94EGYKZEDED645A.png&w=715&h=183&f=webp&fit=cover&position=center)

На этой странице

Обсудить онлайн

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2Foctober-2021-facebook-outage%2F&t=%D0%9A%D0%B0%D0%BA%20Facebook%20%D0%B8%D1%81%D1%87%D0%B5%D0%B7%20%D0%B8%D0%B7%20%D0%98%D0%BD%D1%82%D0%B5%D1%80%D0%BD%D0%B5%D1%82%D0%B0)[](https://x.com/intent/post?text=%D0%9A%D0%B0%D0%BA+Facebook+%D0%B8%D1%81%D1%87%D0%B5%D0%B7+%D0%B8%D0%B7+%D0%98%D0%BD%D1%82%D0%B5%D1%80%D0%BD%D0%B5%D1%82%D0%B0&url=https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2Foctober-2021-facebook-outage%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2Foctober-2021-facebook-outage%2F)[](https://bsky.app/intent/compose?text=%D0%9A%D0%B0%D0%BA+Facebook+%D0%B8%D1%81%D1%87%D0%B5%D0%B7+%D0%B8%D0%B7+%D0%98%D0%BD%D1%82%D0%B5%D1%80%D0%BD%D0%B5%D1%82%D0%B0+https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2Foctober-2021-facebook-outage%2F)[](https://mastodonshare.com/?text=%D0%9A%D0%B0%D0%BA+Facebook+%D0%B8%D1%81%D1%87%D0%B5%D0%B7+%D0%B8%D0%B7+%D0%98%D0%BD%D1%82%D0%B5%D1%80%D0%BD%D0%B5%D1%82%D0%B0&url=https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2Foctober-2021-facebook-outage%2F)[](https://www.threads.net/intent/post?text=%D0%9A%D0%B0%D0%BA+Facebook+%D0%B8%D1%81%D1%87%D0%B5%D0%B7+%D0%B8%D0%B7+%D0%98%D0%BD%D1%82%D0%B5%D1%80%D0%BD%D0%B5%D1%82%D0%B0+https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2Foctober-2021-facebook-outage%2F)

## Связанные теги

[BGP](https://blog.cloudflare.com/ru-ru/tag/bgp/)[DNS](https://blog.cloudflare.com/ru-ru/tag/dns/)[Facebook](https://blog.cloudflare.com/ru-ru/tag/facebook/)[Trends](https://blog.cloudflare.com/ru-ru/tag/trends/)[Сбой](https://blog.cloudflare.com/ru-ru/tag/outage/)

Подписывайтесь в социальных сетях

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)

  * ![Celso Martinho](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45K1GG0634XMEFX9CSSGM2.png&w=64&h=64&f=webp&fit=cover&position=center)[Celso Martinho](https://blog.cloudflare.com/ru-ru/author/celso/)

[](https://celso.io/)




## Подпишитесь на уведомления о новых публикациях

Электронная почта

Мы никогда не передаем ваш адрес электронной почты третьим лицам.

Подписаться

Спасибо за подписку! Проверьте папку «Входящие», чтобы подтвердить подписку.
