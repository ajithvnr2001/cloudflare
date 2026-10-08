---
url: https://blog.cloudflare.com/ru-ru/announcing-workers-smart-placement/
title: Smart Placement \u0443\u0441\u043a\u043e\u0440\u044f\u0435\u0442 \u0440\u0430\u0431\u043e\u0442\u0443 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0439 \u0437\u0430 \u0441\u0447\u0435\u0442 \u043f\u0435\u0440\u0435\u043c\u0435\u0449\u0435\u043d\u0438\u044f \u043a\u043e\u0434\u0430 \u0431\u043b\u0438\u0436\u0435 \u043a \u0432\u0430\u0448\u0435\u0439 \u0441\u0435\u0440\u0432\u0435\u0440\u043d\u043e\u0439 \u0447\u0430\u0441\u0442\u0438, \u043f\u0440\u0438 \u044d\u0442\u043e\u043c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u043d\u0435 \u0442\u0440\u0435\u0431\u0443\u0435\u0442\u0441\u044f. | \u0411\u043b\u043e\u0433 Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:39:56.516974+00:00
---

# Smart Placement ускоряет работу приложений за счет перемещения кода ближе к вашей серверной части, при этом настройка не требуется. | Блог Cloudflare

> Source: https://blog.cloudflare.com/ru-ru/announcing-workers-smart-placement/

[Блог](https://blog.cloudflare.com/ru-ru/)

[Cloudflare Workers](https://blog.cloudflare.com/ru-ru/tag/workers/)[Database](https://blog.cloudflare.com/ru-ru/tag/database/)[Developer Platform](https://blog.cloudflare.com/ru-ru/tag/developer-platform/)+3Показать ещё 3 тегов

6 теговПоказать 6 тегов

  * Теги публикации
  * [Разработчики](https://blog.cloudflare.com/ru-ru/tag/developers/)
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



[Developer Week](https://blog.cloudflare.com/ru-ru/tag/developer-week/)[Serverless](https://blog.cloudflare.com/ru-ru/tag/serverless/)[Разработчики](https://blog.cloudflare.com/ru-ru/tag/developers/)

[Cloudflare Workers](https://blog.cloudflare.com/ru-ru/tag/workers/)[Database](https://blog.cloudflare.com/ru-ru/tag/database/)[Developer Platform](https://blog.cloudflare.com/ru-ru/tag/developer-platform/)[Developer Week](https://blog.cloudflare.com/ru-ru/tag/developer-week/)[Serverless](https://blog.cloudflare.com/ru-ru/tag/serverless/)[Разработчики](https://blog.cloudflare.com/ru-ru/tag/developers/)

16 мая 2023 г.

# Smart Placement ускоряет работу приложений за счет перемещения кода ближе к вашей серверной части, при этом настройка не требуется.

![Michael Hart](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44Y5FGZZS90ZJA5EFQW15Q.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Serena Shah-Simpson](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45E4TK6GHZXWH66VF37ZEZ.PNG&w=64&h=64&f=webp&fit=cover&position=center)![Tanushree Sharma](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46NT9GBM742JJW1W4G7ND8.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Michael Hart](https://blog.cloudflare.com/ru-ru/author/michael-hart/), [Serena Shah-Simpson](https://blog.cloudflare.com/ru-ru/author/serena/) и [Tanushree Sharma](https://blog.cloudflare.com/ru-ru/author/tanushree/)

7 мин. чтения

КОПИРОВАТЬ URL

Этот пост также доступен на [English](https://blog.cloudflare.com/announcing-workers-smart-placement/), [Español](https://blog.cloudflare.com/es-es/announcing-workers-smart-placement/), [日本語](https://blog.cloudflare.com/ja-jp/announcing-workers-smart-placement/), [한국어](https://blog.cloudflare.com/ko-kr/announcing-workers-smart-placement/), [繁體中文](https://blog.cloudflare.com/zh-tw/announcing-workers-smart-placement/), [简体中文](https://blog.cloudflare.com/zh-cn/announcing-workers-smart-placement/), [Português](https://blog.cloudflare.com/pt-br/announcing-workers-smart-placement/) и [Polski](https://blog.cloudflare.com/pl-pl/announcing-workers-smart-placement/).

![Smart Placement speeds up applications by moving code close to your backend — no config needed](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW463REMTYFQ9WDSW6E67JH9.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///////+9PPv7ezk7+7l9PPs8vPv7O3s////////9fTu7erg7uvf8/Dm8vHs7u7t////////9/Xw7ure7+na8u7h8/Hr8PDw////////+vj08ezh8evc9fDj9vPu9PP1//////////379vLq9vHl+vXs+/n1+fj6////////////+/n1+/jz//35///+/f7////////////////+///+////////////////////////////////////////////)

Мы все сталкивались с медленной загрузкой веб-сайтов или с приложением, которое зависает, когда ему нужно вызвать API для обновления. Когда все происходит не мгновенно, ваши мысли отвлекаются на что-то другое...

Один из способов ускорить работу — максимально приблизить ресурсы к пользователю. Именно это Cloudflare осуществляет с вычислительными ресурсами, работая в миллисекундах от большей части населения мира. Но, как бы парадоксально это ни звучало, иногда приближение вычислений к пользователю может на самом деле замедлять работу приложений. Если вашему приложению необходимо подключиться к API, базам данных или другим ресурсам, которые не расположены рядом с конечным пользователем, может быть более эффективным запускать приложения поблизости от ресурсов, а не от пользователя.

Итак, сегодня мы рады представить Smart Placement (Интеллектуальное размещение) для Workers и Pages Functions, позволяющие максимально ускорить каждое взаимодействие. С помощью Smart Placement Cloudflare переносит бессерверные вычисления в Супероблако, перемещая вычислительные ресурсы в оптимальные местоположения для ускорения работы приложений. Самое лучшее здесь то, что это осуществляется полностью автоматически, без необходимости какого-либо дополнительного ввода (например, ужасного «региона»).

Интеллектуальное размещение уже сейчас доступно в открытой бета-версии для всех клиентов Workers и Pages!

[Посмотрите нашу демонстрацию о принципе работы Smart Placement!](https://smart-placement-demo.pages.dev/)

## Бессерверный переход

Сеть Anycast Cloudflare создана для _мгновенной обработки запросов и расположена близко к пользователю_. Это то, что делает Cloudflare Workers, наше предложение бессерверных вычислений, для вас таким привлекательным, как для разработчика. Конкуренты ограничены «регионами», в то время как Workers работают повсюду, поэтому у нас есть один регион: Земля. Запросы, полностью обрабатываемые Workers, могут обрабатываться прямо тут же, даже без обращения к серверу-источнику.

Хотя изначально считалось, что такая концепция бессерверных вычислений предназначена для легких задач, в последние годы бессерверные вычисления претерпевают существенные изменения. Такое решение используется для замены традиционной архитектуры, которая опирается на серверы-источники и самоуправляемую инфраструктуру, а не просто для ее дополнения. Мы наблюдаем все больше и больше таких вариантов использования с пользователями Workers и Pages.

### Состояние потребностей в отношении бессерверных систем

С переходом на бессерверные технологии и созданием целых приложений на Workers возникает потребность в данных. Хранение информации о предыдущих действиях или событиях позволяет создавать персонализированные интерактивные приложения. Допустим, вам нужно создать профили пользователей, сохранить, на какой странице пользователь остановился, какие SKU у пользователя есть в корзине — все это сопоставляется с точками данных, используемыми для хранения состояния. Сервисы серверной части, такие как реляционные базы данных, хранилища «ключ-значение», хранилище BLOB-объектов и API, позволяют создавать приложения с отслеживанием состояния.

### Cloudflare вычисления + хранилище: мощный дуэт

У нас есть собственный растущий набор предложений хранилищ: Workers KV, Durable Objects, D1, [R2](https://www.cloudflare.com/developer-platform/r2/). Совершенствуя наши продукты обработки данных, мы глубоко продумываем их взаимодействие с Workers, чтобы вам не пришлось этого делать! Например, еще один подход, который в некоторых случаях дает более высокую производительность, заключается в перемещении хранилища, а не вычислений рядом с пользователями. Если вы используете Durable Objects для создания игры в реальном времени, мы можем переместить Durable Objects, чтобы свести к минимуму задержку для всех пользователей.

Наша цель в отношении будущего состояния заключается в том, чтобы вы установили режим = "smart", и мы оценили оптимальное размещение всех ваших ресурсов без необходимости дополнительной настройки.

### Cloudflare вычисления + ${backendService}

Сегодня основным вариантом использования Smart Placement (Интеллектуальное размещение) является использование для ваших приложений сервисов, отличных от Cloudflare, таких как внешние базы данных или сторонние API.

Многие серверные сервисы, независимо от того, размещаются они на собственных серверах или управляются, являются централизованными, а это означает, что данные хранятся и управляются в одном месте. Ваши пользователи глобальны, и Workers глобальны, но ваша серверная часть централизована.

Если ваш код отправляет несколько запросов к вашим сервисам сервисной части, они могут несколько раз пересекать земной шар, что серьезно сказывается на производительности. Некоторые сервисы предлагают репликацию и кэширование, которые помогают повысить производительность, но также сопряжены с такими компромиссами, как согласованность данных и более высокие затраты, которые следует взвесить с учетом вашего варианта использования.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![A map of the globe illustrating global users, global workers and a centralized database. ](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4877KTAFZ54HDMT6TVBXPP.png&w=715&h=402&f=webp&fit=cover&position=center)

Сеть Cloudflare находится на расстоянии [~50 мс от 95 % подключенного населения мира](https://www.cloudflare.com/network/). Кроме того, мы находимся очень близко к вашим сервисам серверной части.

## Производительность приложений — это удобство использования

Давайте разберемся, как перемещение вычислений ближе к сервисам серверной части может уменьшить сетевую задержку приложений, на следующем примере:

Допустим, у вас есть пользователь в Сиднее, Австралия, который получает доступ к приложению, работающему на Workers. Это приложение совершает три цикла обращения к базе данных, расположенной во Франкфурте, Германия, чтобы обслужить запрос пользователя.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1787 Embedded Image - krvyST](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46K0J7CQVHJM69K0X2F7HW.png&w=715&h=254&f=webp&fit=cover&position=center)

Интуитивно можно догадаться, что узким местом будет время, которое требуется Worker для выполнения нескольких циклов обращения к вашей базе данных. Что, если бы Worker вызывался не рядом с пользователем, а в центре обработки данных, ближайшем к базе данных?

![wAAAABJRU5ErkJggg==](https://blog.cloudflare.com/_emdash/api/media/file/01KW46JG8Q61D0TYTP363C4KP2)

Давайте протестируем это.

Мы измерили продолжительность запроса для Worker без Smart Placement и сравнили ее с длительностью запроса с включенной функцией Smart Placement. Для обоих тестов мы отправили 3500 запросов из Сиднея на Worker, который совершает три цикла обращения к экземпляру [Upstash](https://upstash.com/) (уровень бесплатного пользования), расположенному в eu-central-1 (Франкфурт).

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![A graph showing request duration with and without Smart Placement enabled. ](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4768M6PTQMJX5HNQCQ2S8V.png&w=715&h=432&f=webp&fit=cover&position=center)

Результаты очевидны! В данном примере перемещение Worker ближе к серверной части **повысилопроизводительность приложения в 4–8 раз**.

## Сетевые решения не должны приниматься людьми

Как разработчик, вы должны сосредоточиться на том, что у вас получается лучше всего — создании приложений, не беспокоясь о сетевых решениях, которые ускорят ваше приложение.

Cloudflare обладает уникальным выгодным позиционированием: наша сеть собирает аналитические данные об оптимальных путях между пользователями, центрами обработки данных Cloudflare и внутренними серверами. У нас большой опыт в этой области с [Argo Smart Routing (Интеллектуальная маршрутизация по технологии Argo)](https://blog.cloudflare.com/argo/). Интеллектуальное размещение учитывает эти факторы, чтобы автоматически размещать ваш Worker в наилучшем месте, чтобы свести к минимуму общую продолжительность запроса.

Итак, как работает Smart Placement?

Smart Placement можно включить отдельно для каждого Worker на вкладке “Settings” (Настройки) или в файле wrangler.toml:
    
    
    [placement]
    mode = "smart"

После включения Smart Placement в Worker или Pages Function алгоритм Smart Placement анализирует запросы на выборку (также известные как подзапросы), отправляемые вашим Worker, в режиме реального времени. Затем он сравнивает их с данными о задержке, агрегированными нашей сетью. Если мы обнаружим, что в среднем ваш Worker отправляет более одного подзапроса к ресурсу серверной части, тогда ваш Worker будет автоматически вызван из оптимального центра обработки данных!

Есть некоторые сервисы сервисной части, которые по уважительной причине не учитываются алгоритмом Smart Placement:

  * Глобально распределенные сервисы: если сервисы, с которыми взаимодействует ваш Worker, географически распределены во многих регионах, Smart Placement не подходит. Мы автоматически исключаем их из оптимизации Smart Placement.
  * Сервисы аналитики или журналирования: запросы к сервисам аналитики или журналирования не обязательно должны находиться на критическом пути вашего приложения. [`WaitUntil()`](https://developers.cloudflare.com/workers/runtime-apis/fetch-event/?ref=blog.cloudflare.com#waituntil) следует использовать, чтобы ответ пользователям не блокировался при инструментировании вашего кода. Поскольку `метод waitUntil()` не влияет на продолжительность запроса с точки зрения пользователя, мы автоматически исключаем сервисы аналитики/журналирования из процесса оптимизации Smart Placement.



В нашей [документации](https://developers.cloudflare.com/workers/platform/smart-placement/#supported-backends) приведен список сервисов, не учитываемых алгоритмом Smart Placement.

Как только Smart Placement начнет функционировать, вы сможете увидеть новую вкладку “Request Duration” (Продолжительность запроса) в вашем Worker. Мы направляем 1 % запросов без включенного Smart Placement, чтобы вы могли увидеть его влияние на продолжительность запроса.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Request duration with and without Smart Placement shown on the Workers dashboard. ](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW456H2J1AGEQ2GCCPGS38ZS.png&w=715&h=388&f=webp&fit=cover&position=center)

И да, это действительно так просто!

Попробуйте Smart Placement, ознакомившись с нашей [демонстрацией](https://smart-placement-demo.pages.dev/) (с ней очень весело играть!). Чтобы узнать больше, посетите раздел с нашей [документацией для разработчиков](https://developers.cloudflare.com/workers/platform/smart-placement/).

## Что дальше с Smart Placement?

Мы только начинаем! У нас есть множество идей по улучшению Smart Placement:

  * Поддержка расчета оптимального местоположения, когда приложение использует несколько серверных частей
  * Точно настроенное размещение (например, если ваш Worker использует несколько серверных частей в зависимости от пути. Мы рассчитываем оптимальное размещение для каждого пути, а не для каждого Worker)
  * Поддержка соединений на основе TCP



Мы хотели бы узнать ваше мнение! Если у вас есть отзывы или пожелания, обращайтесь через [Cloudflare Developer в Discord](https://discord.com/invite/cloudflaredev).

### Посмотреть на Cloudflare TV

На этой странице

Обсудить онлайн

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2Fannouncing-workers-smart-placement%2F&t=Smart%20Placement%20%D1%83%D1%81%D0%BA%D0%BE%D1%80%D1%8F%D0%B5%D1%82%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%83%20%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9%20%D0%B7%D0%B0%20%D1%81%D1%87%D0%B5%D1%82%20%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%BA%D0%BE%D0%B4%D0%B0%20%D0%B1%D0%BB%D0%B8%D0%B6%D0%B5%20%D0%BA%20%D0%B2%D0%B0%D1%88%D0%B5%D0%B9%20%D1%81%D0%B5%D1%80%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D0%B9%20%D1%87%D0%B0%D1%81%D1%82%D0%B8%2C%20%D0%BF%D1%80%D0%B8%20%D1%8D%D1%82%D0%BE%D0%BC%20%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0%20%D0%BD%D0%B5%20%D1%82%D1%80%D0%B5%D0%B1%D1%83%D0%B5%D1%82%D1%81%D1%8F.)[](https://x.com/intent/post?text=Smart+Placement+%D1%83%D1%81%D0%BA%D0%BE%D1%80%D1%8F%D0%B5%D1%82+%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%83+%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9+%D0%B7%D0%B0+%D1%81%D1%87%D0%B5%D1%82+%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F+%D0%BA%D0%BE%D0%B4%D0%B0+%D0%B1%D0%BB%D0%B8%D0%B6%D0%B5+%D0%BA+%D0%B2%D0%B0%D1%88%D0%B5%D0%B9+%D1%81%D0%B5%D1%80%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D0%B9+%D1%87%D0%B0%D1%81%D1%82%D0%B8%2C+%D0%BF%D1%80%D0%B8+%D1%8D%D1%82%D0%BE%D0%BC+%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0+%D0%BD%D0%B5+%D1%82%D1%80%D0%B5%D0%B1%D1%83%D0%B5%D1%82%D1%81%D1%8F.&url=https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2Fannouncing-workers-smart-placement%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2Fannouncing-workers-smart-placement%2F)[](https://bsky.app/intent/compose?text=Smart+Placement+%D1%83%D1%81%D0%BA%D0%BE%D1%80%D1%8F%D0%B5%D1%82+%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%83+%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9+%D0%B7%D0%B0+%D1%81%D1%87%D0%B5%D1%82+%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F+%D0%BA%D0%BE%D0%B4%D0%B0+%D0%B1%D0%BB%D0%B8%D0%B6%D0%B5+%D0%BA+%D0%B2%D0%B0%D1%88%D0%B5%D0%B9+%D1%81%D0%B5%D1%80%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D0%B9+%D1%87%D0%B0%D1%81%D1%82%D0%B8%2C+%D0%BF%D1%80%D0%B8+%D1%8D%D1%82%D0%BE%D0%BC+%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0+%D0%BD%D0%B5+%D1%82%D1%80%D0%B5%D0%B1%D1%83%D0%B5%D1%82%D1%81%D1%8F.+https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2Fannouncing-workers-smart-placement%2F)[](https://mastodonshare.com/?text=Smart+Placement+%D1%83%D1%81%D0%BA%D0%BE%D1%80%D1%8F%D0%B5%D1%82+%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%83+%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9+%D0%B7%D0%B0+%D1%81%D1%87%D0%B5%D1%82+%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F+%D0%BA%D0%BE%D0%B4%D0%B0+%D0%B1%D0%BB%D0%B8%D0%B6%D0%B5+%D0%BA+%D0%B2%D0%B0%D1%88%D0%B5%D0%B9+%D1%81%D0%B5%D1%80%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D0%B9+%D1%87%D0%B0%D1%81%D1%82%D0%B8%2C+%D0%BF%D1%80%D0%B8+%D1%8D%D1%82%D0%BE%D0%BC+%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0+%D0%BD%D0%B5+%D1%82%D1%80%D0%B5%D0%B1%D1%83%D0%B5%D1%82%D1%81%D1%8F.&url=https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2Fannouncing-workers-smart-placement%2F)[](https://www.threads.net/intent/post?text=Smart+Placement+%D1%83%D1%81%D0%BA%D0%BE%D1%80%D1%8F%D0%B5%D1%82+%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%83+%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9+%D0%B7%D0%B0+%D1%81%D1%87%D0%B5%D1%82+%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F+%D0%BA%D0%BE%D0%B4%D0%B0+%D0%B1%D0%BB%D0%B8%D0%B6%D0%B5+%D0%BA+%D0%B2%D0%B0%D1%88%D0%B5%D0%B9+%D1%81%D0%B5%D1%80%D0%B2%D0%B5%D1%80%D0%BD%D0%BE%D0%B9+%D1%87%D0%B0%D1%81%D1%82%D0%B8%2C+%D0%BF%D1%80%D0%B8+%D1%8D%D1%82%D0%BE%D0%BC+%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0+%D0%BD%D0%B5+%D1%82%D1%80%D0%B5%D0%B1%D1%83%D0%B5%D1%82%D1%81%D1%8F.+https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2Fannouncing-workers-smart-placement%2F)

## Связанные теги

[Cloudflare Workers](https://blog.cloudflare.com/ru-ru/tag/workers/)[Database](https://blog.cloudflare.com/ru-ru/tag/database/)[Developer Platform](https://blog.cloudflare.com/ru-ru/tag/developer-platform/)[Developer Week](https://blog.cloudflare.com/ru-ru/tag/developer-week/)[Serverless](https://blog.cloudflare.com/ru-ru/tag/serverless/)[Разработчики](https://blog.cloudflare.com/ru-ru/tag/developers/)

Подписывайтесь в социальных сетях

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Подпишитесь на уведомления о новых публикациях

Электронная почта

Мы никогда не передаем ваш адрес электронной почты третьим лицам.

Подписаться

Спасибо за подписку! Проверьте папку «Входящие», чтобы подтвердить подписку.
