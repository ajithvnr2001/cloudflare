---
url: https://blog.cloudflare.com/ru-ru/threats-lurking-office-365-cloudflare-email-retro-scan/
title: \u0423\u0437\u043d\u0430\u0439\u0442\u0435, \u043a\u0430\u043a\u0438\u0435 \u0443\u0433\u0440\u043e\u0437\u044b \u0442\u0430\u044f\u0442\u0441\u044f \u0432 \u0432\u0430\u0448\u0435\u043c Office 365, \u0441 \u043f\u043e\u043c\u043e\u0449\u044c\u044e \u0440\u0435\u0442\u0440\u043e-\u0441\u043a\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u043e\u0439 \u043f\u043e\u0447\u0442\u044b Cloudflare | \u0411\u043b\u043e\u0433 Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:37:01.889548+00:00
---

# Узнайте, какие угрозы таятся в вашем Office 365, с помощью ретро-сканирования электронной почты Cloudflare | Блог Cloudflare

> Source: https://blog.cloudflare.com/ru-ru/threats-lurking-office-365-cloudflare-email-retro-scan/

[Блог](https://blog.cloudflare.com/ru-ru/)

[Birthday Week](https://blog.cloudflare.com/ru-ru/tag/birthday-week/)

1 теговПоказать 1 тегов

  * Теги публикации
  *   * Все теги
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



[Birthday Week](https://blog.cloudflare.com/ru-ru/tag/birthday-week/)

29 сентября 2023 г.

# Узнайте, какие угрозы таятся в вашем Office 365, с помощью ретро-сканирования электронной почты Cloudflare

![Ayush Kumar](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW449VZTK4C95VB94E47SS8C.png&w=64&h=64&f=webp&fit=cover&position=center)

[Ayush Kumar](https://blog.cloudflare.com/ru-ru/author/ayush/)

3 мин. чтения

КОПИРОВАТЬ URL

Этот пост также доступен на [English](https://blog.cloudflare.com/threats-lurking-office-365-cloudflare-email-retro-scan/), [Deutsch](https://blog.cloudflare.com/de-de/threats-lurking-office-365-cloudflare-email-retro-scan/), [Español](https://blog.cloudflare.com/es-es/threats-lurking-office-365-cloudflare-email-retro-scan/), [Français](https://blog.cloudflare.com/fr-fr/threats-lurking-office-365-cloudflare-email-retro-scan/), [日本語](https://blog.cloudflare.com/ja-jp/threats-lurking-office-365-cloudflare-email-retro-scan/), [한국어](https://blog.cloudflare.com/ko-kr/threats-lurking-office-365-cloudflare-email-retro-scan/), [繁體中文](https://blog.cloudflare.com/zh-tw/threats-lurking-office-365-cloudflare-email-retro-scan/), [简体中文](https://blog.cloudflare.com/zh-cn/threats-lurking-office-365-cloudflare-email-retro-scan/), [Português](https://blog.cloudflare.com/pt-br/threats-lurking-office-365-cloudflare-email-retro-scan/), [Polski](https://blog.cloudflare.com/pl-pl/threats-lurking-office-365-cloudflare-email-retro-scan/) и [עברית](https://blog.cloudflare.com/he-il/threats-lurking-office-365-cloudflare-email-retro-scan/).

![See what threats are lurking in your Office 365 with Cloudflare Email Retro Scan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44HXTZY6W122ZVDFV058YX.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA//////387vDw4efr4env6e/07/Dy7+3p/////v7/7PH03Ofv2ebz4ev46e717u3s////////7PP62uj11OX42+n95u367e/x////////8Pf/3uz62Oj+3uz/6fD/8fL2////////+f3/6vP/5vH/6/T/8/f/+Pj7////////////+fz/+Pz//f////////3+////////////////////////////////////////////////////////////////)

Теперь мы объявляем о возможности для клиентов Cloudflare сканировать старые сообщения в своих почтовых ящиках Office 365 на наличие угроз. Ретро-сканирование позволит вам вернуться на семь дней назад и просмотреть, какие угрозы пропустил ваш текущий инструмент защиты электронной почты.

## Зачем запускать ретро-сканирование

Общаясь с клиентами, мы часто слышим, что они не знают о состоянии почтовых ящиков своей организации. У организаций есть инструмент защиты электронной почты или они используют встроенную защиту Microsoft, но не понимают, насколько эффективно их текущее решение. Мы обнаружили, что эти инструменты часто пропускают вредоносные электронные письма через свои фильтры, что увеличивает риск компрометации внутри компании.

В рамках наших усилий по улучшению Интернета мы предоставляем клиентам Cloudflare возможность бесплатно использовать инструмент ретро-сканирования (Retro Scan) для сканирования сообщений в соответствующих почтовых ящиках с использованием наших передовых моделей машинного обучения. Наше инструмент ретро-сканирования обнаружит и выделит все обнаруженные нами угрозы, чтобы клиенты могли очистить свои почтовые ящики, обратившись к ним в своих учетных записях электронной почты. Используя эту информацию, клиенты также могут внедрить дополнительные средства контроля, такие как использование Cloudflare или предпочитаемого ими решения, чтобы предотвратить попадание подобных угроз в их почтовый ящик в будущем.

## Запуск ретро-сканирования

Клиенты могут перейти на панель управления Cloudflare, где на вкладке Area 1 они увидят пункт "Retro Scan":

Чтобы иметь доступ к сообщениям для сканирования, Cloudflare необходима авторизация для сканирования сообщений. Данный процесс начинается с предоставления Cloudflare соответствующих разрешений на сканирование сообщений. Вторая авторизация позволит приложению Cloudflare получить доступ к Active Directory. Это необходимо для того, чтобы понять, какие пользователи находятся в организации и к каким группам они принадлежат. Это помогает нашим алгоритмам лучше оценить, является ли сообщение вредоносным.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2087 Embedded Image - z1Mw1W](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45B0P1WD7XHRVCXSTT5YKK.png&w=715&h=402&f=webp&fit=cover&position=center)

После получения всех разрешений вам останется сделать последний шаг — выбрать, какие домены мы хотим сканировать, а также предоставить нам информацию о других поставщиках средств обеспечения безопасности электронной почты, которые защищают ваши почтовые ящики.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2087 Embedded Image - Ub1GiP](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47C2WNHKCCAWM6KSJ7117Y.png&w=715&h=501&f=webp&fit=cover&position=center)

Наконец, клиенты могут нажать “Generate Retro Scan” («Сгенерировать ретро-сканирование»), после чего Area 1 Email Security от Cloudflare начнет сканирование старых сообщений. Поскольку для выполнения этого процесса требуется некоторое время, мы уведомляем клиентов по электронной почте после завершения сканирования.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2087 Embedded Image - wp2rvP](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46JFBDCB4HTZ5DK09EC6N7.png&w=715&h=585&f=webp&fit=cover&position=center)

## Analyzing The Results

Вам будет представлена краткая информация о том, какие угрозы мы обнаружили в почтовых ящиках электронной почты вашей организации. В верхнем разделе все наши обнаружения разбиты по типам. Здесь вы можете найти подсчет вредоносных, подозрительных, спуфинговых, спам- и массовых сообщений. Мы также выделяем наиболее важные из них, на которые следует обратить внимание в категории фишинговых писем. В любой момент вы можете нажать кнопку "Search" («Поиск»), чтобы получить дополнительную информацию об электронных письмах с этими ярлыками.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2087 Embedded Image - tuhT7z](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45DX4AHP4SCPW7VD0YT901.png&w=715&h=659&f=webp&fit=cover&position=center)

В отчете также показаны наиболее уязвимые сотрудники, а также наиболее распространенные места, откуда исходят угрозы. Вся эта статистика предназначена для лучшего понимания того, что происходит в почтовом ящике вашей компании.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2087 Embedded Image - 4CE93n](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45K7CD9047JJ6P0YCK7WRA.png&w=715&h=415&f=webp&fit=cover&position=center)

## Как зарегистрироваться

Ретро-сканирование в настоящее время находится в стадии закрытого бета-тестирования. Если вы заинтересованы в запуске ретро-сканирования своих доменов электронной почты Office 365, обратитесь к своему контактному лицу в Cloudflare, и мы добавим его в вашу учетную запись.

После запуска ретро-сканирования и просмотра результатов вы можете либо приобрести Cloudflare Area 1, чтобы предотвратить попадание будущих угроз в ваш почтовый ящик, либо настроить оценку риска фишинга, которая представляет собой 30-дневную бесплатную пробную версию продукта Area 1. Хотя ретро-сканирование — отличный инструмент для выявления существующих скрытых угроз, оценка рисков фишинга может помочь вам получить более обширное представление о всех инструментах, которые у нас имеются для поддержания чистоты почтовых ящиков.

Чтобы начать работу, вы можете нажать кнопку “Request Trial” («Запросить пробную версию») в нижней части отчета о ретро-сканировании, заполнить соответствующую форму, и сотрудник Cloudflare свяжется с вами, либо вы можете связаться напрямую со своим контактным лицом в Cloudflare.

На этой странице

Обсудить онлайн

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2Fthreats-lurking-office-365-cloudflare-email-retro-scan%2F&t=%D0%A3%D0%B7%D0%BD%D0%B0%D0%B9%D1%82%D0%B5%2C%20%D0%BA%D0%B0%D0%BA%D0%B8%D0%B5%20%D1%83%D0%B3%D1%80%D0%BE%D0%B7%D1%8B%20%D1%82%D0%B0%D1%8F%D1%82%D1%81%D1%8F%20%D0%B2%20%D0%B2%D0%B0%D1%88%D0%B5%D0%BC%20Office%20365%2C%20%D1%81%20%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E%20%D1%80%D0%B5%D1%82%D1%80%D0%BE-%D1%81%D0%BA%D0%B0%D0%BD%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F%20%D1%8D%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%BE%D0%BD%D0%BD%D0%BE%D0%B9%20%D0%BF%D0%BE%D1%87%D1%82%D1%8B%20Cloudflare)[](https://x.com/intent/post?text=%D0%A3%D0%B7%D0%BD%D0%B0%D0%B9%D1%82%D0%B5%2C+%D0%BA%D0%B0%D0%BA%D0%B8%D0%B5+%D1%83%D0%B3%D1%80%D0%BE%D0%B7%D1%8B+%D1%82%D0%B0%D1%8F%D1%82%D1%81%D1%8F+%D0%B2+%D0%B2%D0%B0%D1%88%D0%B5%D0%BC+Office+365%2C+%D1%81+%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E+%D1%80%D0%B5%D1%82%D1%80%D0%BE-%D1%81%D0%BA%D0%B0%D0%BD%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F+%D1%8D%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%BE%D0%BD%D0%BD%D0%BE%D0%B9+%D0%BF%D0%BE%D1%87%D1%82%D1%8B+Cloudflare&url=https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2Fthreats-lurking-office-365-cloudflare-email-retro-scan%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2Fthreats-lurking-office-365-cloudflare-email-retro-scan%2F)[](https://bsky.app/intent/compose?text=%D0%A3%D0%B7%D0%BD%D0%B0%D0%B9%D1%82%D0%B5%2C+%D0%BA%D0%B0%D0%BA%D0%B8%D0%B5+%D1%83%D0%B3%D1%80%D0%BE%D0%B7%D1%8B+%D1%82%D0%B0%D1%8F%D1%82%D1%81%D1%8F+%D0%B2+%D0%B2%D0%B0%D1%88%D0%B5%D0%BC+Office+365%2C+%D1%81+%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E+%D1%80%D0%B5%D1%82%D1%80%D0%BE-%D1%81%D0%BA%D0%B0%D0%BD%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F+%D1%8D%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%BE%D0%BD%D0%BD%D0%BE%D0%B9+%D0%BF%D0%BE%D1%87%D1%82%D1%8B+Cloudflare+https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2Fthreats-lurking-office-365-cloudflare-email-retro-scan%2F)[](https://mastodonshare.com/?text=%D0%A3%D0%B7%D0%BD%D0%B0%D0%B9%D1%82%D0%B5%2C+%D0%BA%D0%B0%D0%BA%D0%B8%D0%B5+%D1%83%D0%B3%D1%80%D0%BE%D0%B7%D1%8B+%D1%82%D0%B0%D1%8F%D1%82%D1%81%D1%8F+%D0%B2+%D0%B2%D0%B0%D1%88%D0%B5%D0%BC+Office+365%2C+%D1%81+%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E+%D1%80%D0%B5%D1%82%D1%80%D0%BE-%D1%81%D0%BA%D0%B0%D0%BD%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F+%D1%8D%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%BE%D0%BD%D0%BD%D0%BE%D0%B9+%D0%BF%D0%BE%D1%87%D1%82%D1%8B+Cloudflare&url=https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2Fthreats-lurking-office-365-cloudflare-email-retro-scan%2F)[](https://www.threads.net/intent/post?text=%D0%A3%D0%B7%D0%BD%D0%B0%D0%B9%D1%82%D0%B5%2C+%D0%BA%D0%B0%D0%BA%D0%B8%D0%B5+%D1%83%D0%B3%D1%80%D0%BE%D0%B7%D1%8B+%D1%82%D0%B0%D1%8F%D1%82%D1%81%D1%8F+%D0%B2+%D0%B2%D0%B0%D1%88%D0%B5%D0%BC+Office+365%2C+%D1%81+%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E+%D1%80%D0%B5%D1%82%D1%80%D0%BE-%D1%81%D0%BA%D0%B0%D0%BD%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F+%D1%8D%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%BE%D0%BD%D0%BD%D0%BE%D0%B9+%D0%BF%D0%BE%D1%87%D1%82%D1%8B+Cloudflare+https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2Fthreats-lurking-office-365-cloudflare-email-retro-scan%2F)

## Связанные теги

[Birthday Week](https://blog.cloudflare.com/ru-ru/tag/birthday-week/)

Подписывайтесь в социальных сетях

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Подпишитесь на уведомления о новых публикациях

Электронная почта

Мы никогда не передаем ваш адрес электронной почты третьим лицам.

Подписаться

Спасибо за подписку! Проверьте папку «Входящие», чтобы подтвердить подписку.
