---
url: https://blog.cloudflare.com/ru-ru/location-aware-ddos-protection/
title: \u041f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u043c \u0441\u0438\u0441\u0442\u0435\u043c\u0443 DDoS-\u0437\u0430\u0449\u0438\u0442\u044b \u0441 \u0443\u0447\u0435\u0442\u043e\u043c \u0433\u0435\u043e\u0433\u0440\u0430\u0444\u0438\u0438 \u0442\u0440\u0430\u0444\u0438\u043a\u0430 | \u0411\u043b\u043e\u0433 Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:44:30.124455+00:00
---

# Представляем систему DDoS-защиты с учетом географии трафика | Блог Cloudflare

> Source: https://blog.cloudflare.com/ru-ru/location-aware-ddos-protection/

[Блог](https://blog.cloudflare.com/ru-ru/)

[Advanced DDoS](https://blog.cloudflare.com/ru-ru/tag/advanced-ddos/)[Attacks](https://blog.cloudflare.com/ru-ru/tag/attacks/)[DDoS](https://blog.cloudflare.com/ru-ru/tag/ddos/)+2Показать ещё 2 тегов

5 теговПоказать 5 тегов

  * Теги публикации
  * [DDoS](https://blog.cloudflare.com/ru-ru/tag/ddos/)[Новости](https://blog.cloudflare.com/ru-ru/tag/product-news/)
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



[Managed Rules](https://blog.cloudflare.com/ru-ru/tag/managed-rules/)[Новости](https://blog.cloudflare.com/ru-ru/tag/product-news/)

[Advanced DDoS](https://blog.cloudflare.com/ru-ru/tag/advanced-ddos/)[Attacks](https://blog.cloudflare.com/ru-ru/tag/attacks/)[DDoS](https://blog.cloudflare.com/ru-ru/tag/ddos/)[Managed Rules](https://blog.cloudflare.com/ru-ru/tag/managed-rules/)[Новости](https://blog.cloudflare.com/ru-ru/tag/product-news/)

11 июля 2022 г.

# Представляем систему DDoS-защиты с учетом географии трафика

![Omer Yoachimik](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW485W0MZ0R9VGWD75RQN9ZH.png&w=64&h=64&f=webp&fit=cover&position=center)![Julien Desgats](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW490NXEPS0Y3GYM6MEBDP98.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Omer Yoachimik](https://blog.cloudflare.com/ru-ru/author/omer/) и [Julien Desgats](https://blog.cloudflare.com/ru-ru/author/julien-desgats/)

3 мин. чтения

КОПИРОВАТЬ URL

Этот пост также доступен на [English](https://blog.cloudflare.com/location-aware-ddos-protection/), [Español](https://blog.cloudflare.com/es-es/location-aware-ddos-protection/), [繁體中文](https://blog.cloudflare.com/zh-tw/location-aware-ddos-protection/), [简体中文](https://blog.cloudflare.com/zh-cn/location-aware-ddos-protection/) и [Polski](https://blog.cloudflare.com/pl-pl/location-aware-ddos-protection/).

![Introducing Location-Aware DDoS Protection](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44XYSQSGS8HMQZY1RKA9A3.png&w=1801&h=1013&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////////8u/u6eXg7Oro8/P28vT66+3y/////v7/6+Ti39PP4tjZ6ufu6uv14uXv/////vz/5trX1sC82cfK49zm5OTy2t7t////////6NnV1ry22cTH5Nvm5eX029/u////////8eTg4szF5dTT8Onw8PD85un1/////////vfw8+bd9+3p//3/////9vn+//////////////vx///7///////////////////////////4////////////////)

Мы рады представить разработанную Cloudflare систему DDoS-защиты с учетом географии трафика

[Распределенные атаки типа «отказ в обслуживании» (DDoS)](https://www.cloudflare.com/en-gb/learning/ddos/what-is-a-ddos-attack/) представляют собой кибератаки, цель которых — сделать ваш интернет-ресурс недоступным, бомбардируя его большим объемом трафика, с которым он окажется не в состоянии справиться. По этой причине злоумышленники обычно стремятся сгенерировать максимум трафика из как можно большего числа различных мест. Наша система DDoS-защиты с учетом географии трафика использует _рассредоточенный_ характер атак, считающийся преимуществом для злоумышленников, выворачивая его «наизнанку», превращая в недостаток.

DDoS-защита с учетом географии трафика теперь доступна в бета-версии для клиентов Cloudflare Enterprise, подписанных на сервис Advanced DDoS (Расширенная защита от DDoS).

### Распределенные атаки теряют свое преимущество

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![A diagram of a DDoS attack denying service to legitimate users](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW472HXAC4PA7D5EEXCTTT76.png&w=715&h=378&f=webp&fit=cover&position=center)

Наша система DDoS-защиты с учетом географии трафика обращает преимущество злоумышленника против него самого. Зная, откуда приходит ваш трафик, система становится способной учитывать его географию и при появлении нового трафика немедленно задается вопросом: «Нормально ли это для _вашего_ сайта?».

Например, если у вас сайт электронной коммерции, который в основном обслуживает потребителей из Германии, большая часть вашего трафика, скорее всего, будет поступать из Германии, часть из соседних европейских стран, меньше — из других стран и регионов мира, и тем меньше, чем больше их удаленность. При появлении внезапных всплесков трафика из неожиданных мест за пределами вашей основной географии система пометит нежелательный трафик и нейтрализует его.

Система DDoS-защиты с учетом географии трафика также использует [модели машинного обучения](https://developers.cloudflare.com/bots/concepts/bot-score/#machine-learning) Cloudflare для обнаружения автоматизированного трафика. Это служит в качестве дополнительного сигнала для обеспечения более точной защиты.

### Включение DDoS-защиты с учетом географии трафика

Клиенты Enterprise, подписанные на сервис Advanced DDoS, могут настроить и включить систему DDoS-защиты с учетом географии трафика. По умолчанию система лишь показывает, какой трафик она посчитала подозрительным, основываясь на вашей статистике за последние 7 дней (95-й процентиль) с разбивкой по странам и регионам клиентов (пересчитывается каждые 24 часа).

Клиенты могут просматривать помеченный системой трафик на [информационной панели Security Overview (Обзор безопасности)](https://dash.cloudflare.com/?to=/:account/:zone/security).

DDoS-защита с учетом географии трафика предоставляется клиентам в виде нового правила в наборе правил HTTP DDoS Managed. Для его включения измените действие на _Managed Challenge (Управляемый тест)_ или _Block (Блокировка)_. Вы можете настроить уровень чувствительности, чтобы определить, насколько допустим трафик, отклоняющийся от наблюдаемого на вашем сайте географического распределения. Чем ниже чувствительность, тем выше допустимость отклонений.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Screenshot of Cloudflare’s Security Overview analytics dashboard showing the traffic that was flagged by the Location-Aware DDoS Protection rule](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45YDD115NQ5PRVJ2141X1V.png&w=715&h=685&f=webp&fit=cover&position=center)

Чтобы узнать, как просматривать помеченный трафик и как настроить DDoS-защиту с учетом географии трафика, посетите наш [сайт документации для разработчиков](https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/location-aware-protection/).

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Screenshot of Cloudflare’s dashboard showing the Location-Aware DDoS Protection rule](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49NPQJDGYYKANPX1XXBT2P.png&w=715&h=418&f=webp&fit=cover&position=center)

### Наша цель: лишить DDoS-атаки возможности причинять ущерб

Миссия Cloudflare — способствовать развитию и совершенствованию Интернета. Задачи наших специалистов по защите от DDoS вытекают из этой миссии. Наша цель состоит в том, чтобы лишить DDoS-атаки возможности причинять ущерб. Защита с учетом географии трафика — только первый шаг, мы постоянно работаем над тем, чтобы сделать DDoS-защиту Cloudflare еще более интеллектуальной, комплексной и адаптированной к индивидуальным потребностям.Еще не используете Cloudflare? [Начните сейчас](https://dash.cloudflare.com/sign-up), воспользовавшись нашими [планами](https://www.cloudflare.com/ru-ru/plans/#price-matrix) Free и Pro для защиты ваших веб-сайтов, или [свяжитесь с нами](https://www.cloudflare.com/magic-transit/), чтобы узнать подробнее о пакете Advanced DDoS плана Enterprise.

На этой странице

Обсудить онлайн

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2Flocation-aware-ddos-protection%2F&t=%D0%9F%D1%80%D0%B5%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%BB%D1%8F%D0%B5%D0%BC%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%83%20DDoS-%D0%B7%D0%B0%D1%89%D0%B8%D1%82%D1%8B%20%D1%81%20%D1%83%D1%87%D0%B5%D1%82%D0%BE%D0%BC%20%D0%B3%D0%B5%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D0%B8%20%D1%82%D1%80%D0%B0%D1%84%D0%B8%D0%BA%D0%B0)[](https://x.com/intent/post?text=%D0%9F%D1%80%D0%B5%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%BB%D1%8F%D0%B5%D0%BC+%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%83+DDoS-%D0%B7%D0%B0%D1%89%D0%B8%D1%82%D1%8B+%D1%81+%D1%83%D1%87%D0%B5%D1%82%D0%BE%D0%BC+%D0%B3%D0%B5%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D0%B8+%D1%82%D1%80%D0%B0%D1%84%D0%B8%D0%BA%D0%B0&url=https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2Flocation-aware-ddos-protection%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2Flocation-aware-ddos-protection%2F)[](https://bsky.app/intent/compose?text=%D0%9F%D1%80%D0%B5%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%BB%D1%8F%D0%B5%D0%BC+%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%83+DDoS-%D0%B7%D0%B0%D1%89%D0%B8%D1%82%D1%8B+%D1%81+%D1%83%D1%87%D0%B5%D1%82%D0%BE%D0%BC+%D0%B3%D0%B5%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D0%B8+%D1%82%D1%80%D0%B0%D1%84%D0%B8%D0%BA%D0%B0+https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2Flocation-aware-ddos-protection%2F)[](https://mastodonshare.com/?text=%D0%9F%D1%80%D0%B5%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%BB%D1%8F%D0%B5%D0%BC+%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%83+DDoS-%D0%B7%D0%B0%D1%89%D0%B8%D1%82%D1%8B+%D1%81+%D1%83%D1%87%D0%B5%D1%82%D0%BE%D0%BC+%D0%B3%D0%B5%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D0%B8+%D1%82%D1%80%D0%B0%D1%84%D0%B8%D0%BA%D0%B0&url=https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2Flocation-aware-ddos-protection%2F)[](https://www.threads.net/intent/post?text=%D0%9F%D1%80%D0%B5%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%BB%D1%8F%D0%B5%D0%BC+%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%83+DDoS-%D0%B7%D0%B0%D1%89%D0%B8%D1%82%D1%8B+%D1%81+%D1%83%D1%87%D0%B5%D1%82%D0%BE%D0%BC+%D0%B3%D0%B5%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D0%B8+%D1%82%D1%80%D0%B0%D1%84%D0%B8%D0%BA%D0%B0+https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2Flocation-aware-ddos-protection%2F)

## Связанные теги

[Advanced DDoS](https://blog.cloudflare.com/ru-ru/tag/advanced-ddos/)[Attacks](https://blog.cloudflare.com/ru-ru/tag/attacks/)[DDoS](https://blog.cloudflare.com/ru-ru/tag/ddos/)[Managed Rules](https://blog.cloudflare.com/ru-ru/tag/managed-rules/)[Новости](https://blog.cloudflare.com/ru-ru/tag/product-news/)

Подписывайтесь в социальных сетях

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Подпишитесь на уведомления о новых публикациях

Электронная почта

Мы никогда не передаем ваш адрес электронной почты третьим лицам.

Подписаться

Спасибо за подписку! Проверьте папку «Входящие», чтобы подтвердить подписку.
