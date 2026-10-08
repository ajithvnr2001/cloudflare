---
url: https://blog.cloudflare.com/ru-ru/mantis-botnet/
title: Mantis \u2014 \u0441\u0430\u043c\u044b\u0439 \u043c\u043e\u0449\u043d\u044b\u0439 \u0431\u043e\u0442\u043d\u0435\u0442 \u0437\u0430 \u0432\u0441\u0435 \u0432\u0440\u0435\u043c\u044f \u043d\u0430\u0431\u043b\u044e\u0434\u0435\u043d\u0438\u0439 | \u0411\u043b\u043e\u0433 Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:44:28.771557+00:00
---

# Mantis — самый мощный ботнет за все время наблюдений | Блог Cloudflare

> Source: https://blog.cloudflare.com/ru-ru/mantis-botnet/

[Блог](https://blog.cloudflare.com/ru-ru/)

[Botnet](https://blog.cloudflare.com/ru-ru/tag/botnet/)[DDoS](https://blog.cloudflare.com/ru-ru/tag/ddos/)[Trends](https://blog.cloudflare.com/ru-ru/tag/trends/)

3 теговПоказать 3 тегов

  * Теги публикации
  * [DDoS](https://blog.cloudflare.com/ru-ru/tag/ddos/)
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



[Botnet](https://blog.cloudflare.com/ru-ru/tag/botnet/)[DDoS](https://blog.cloudflare.com/ru-ru/tag/ddos/)[Trends](https://blog.cloudflare.com/ru-ru/tag/trends/)

14 июля 2022 г.

# Mantis — самый мощный ботнет за все время наблюдений

![Omer Yoachimik](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW485W0MZ0R9VGWD75RQN9ZH.png&w=64&h=64&f=webp&fit=cover&position=center)

[Omer Yoachimik](https://blog.cloudflare.com/ru-ru/author/omer/)

4 мин. чтения

КОПИРОВАТЬ URL

Этот пост также доступен на [English](https://blog.cloudflare.com/mantis-botnet/), [Español](https://blog.cloudflare.com/es-es/mantis-botnet/), [繁體中文](https://blog.cloudflare.com/zh-tw/mantis-botnet/), [简体中文](https://blog.cloudflare.com/zh-cn/mantis-botnet/) и [Polski](https://blog.cloudflare.com/pl-pl/mantis-botnet/).

![Mantis - the most powerful botnet to date](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44D3QXVC54AT00X2AV2FHT.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAAixsAjjgAlFkhmGY6mGA2k00bjDsAhjgAiyIAkkgAoHFFq4NarHxVpGU7lk0RikQAjCgAl1QYrIRbu5lxvZFqs3ZOoVoqj04PjioAmVkjsIpjwZ95xJdxuHtUpV0vkVEbkCgAmVMarIFeupVzvIxqsnBLoVQkkUwRkyIAl0UAoWtMqHpfqXBVo1YymEAAjkAAlBsAlTMAlU0ylFVEk0c2kS4AjiEAizEAlRcAkykAjzwhiz41iSsgiQAAigMAiikA)

В июне 2022 года мы сообщили о крупнейшей DDoS-атаке по HTTPS, которую нам удалось нейтрализовать — [кибератаке мощностью 26 миллионов запросов в секунду](https://blog.cloudflare.com/26m-rps-ddos/), самой крупной за все время наблюдений. Наши системы автоматически обнаружили и нейтрализовали ее, как и многие другие DDoS-атаки. С тех пор мы отслеживаем этот [ботнет](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-botnet/) (мы назвали его **Mantis**), а также осуществляемые с его помощью атаки, направленные против почти тысячи клиентов Cloudflare.

Клиенты Cloudflare [WAF](https://www.cloudflare.com/waf/)/[CDN](https://www.cloudflare.com/cdn/) защищены от DDoS-атак по HTTP, в т. ч. от атак Mantis. В нижней части этого блога вы найдете дополнительные рекомендации, как наилучшим образом защитить свои интернет-ресурсы от DDoS-атак.

### Вы знакомы с Mantis?

Мы назвали ботнет, запустивший DDoS-атаку мощностью 26 млн запросов в секунду, Mantis (Богомол), по аналогии с [раком-богомолом](https://en.wikipedia.org/wiki/Mantis_shrimp), который имеет небольшой размер, но при этом обладает большой силой. Раки-богомолы, известные своей способностью откусить человеку палец, очень маленькие. Их длина не превышает 10 см, однако их клешни настолько мощные, что способны создавать ударную волну в 1500 [ньютонов](https://en.wikipedia.org/wiki/Newton_\(unit\)) на скорости 83 км/ч из неподвижного состояния. Аналогичным образом, ботнет Mantis управляет небольшим «парком» из примерно 5000 ботов, но с их помощью может генерировать огромную мощность, позволяющую осуществлять самые крупные DDoS-атаки по HTTP за все время наблюдений.

Рак-богомол. Источник: [Wikipedia](https://en.wikipedia.org/wiki/File:OdontodactylusScyllarus2.jpg).

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Image of the Mantis shrimp from Wikipedia](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44KPTQ080QEXHTQN4SW8JZ.png&w=715&h=354&f=webp&fit=cover&position=center)

Ботнет Mantis смог провести атаку мощностью 26 млн HTTPS-запросов в секунду, используя **всего** 5000 ботов. Повторяем: 26 млн HTTPS-запросов в секунду с помощью **всего** 5000 ботов. Это в среднем 5200 HTTPS-запросов в секунду на одного бота. Сгенерировать 26 млн HTTP-запросов достаточно сложно и без дополнительных затрат ресурсов на установление безопасного соединения, однако Mantis использовал [HTTPS](https://www.cloudflare.com/learning/ssl/what-is-https/). DDoS-атаки по HTTPS обходятся дороже с точки зрения требуемых вычислительных ресурсов за счет более высоких затрат на установление защищенного зашифрованного [TLS](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)-соединения. Это подчеркивает необычность и уникальную силу этого ботнета.

В отличие от «традиционных» ботнетов, которые формируются на основе устройств [Интернета вещей (IoT)](https://www.cloudflare.com/learning/ddos/glossary/internet-of-things-iot/), таких как видеорегистраторы, камеры видеонаблюдения или детекторы дыма, Mantis использует взломанные виртуальные машины и мощные серверы. Это означает, что каждый бот имеет гораздо больше вычислительных ресурсов, что в совокупности и обеспечивает такую исключительную мощность.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Graph of the 26 million requests per second DDoS attack](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48HHHY8YMMV9MB1QW97E4N.png&w=715&h=328&f=webp&fit=cover&position=center)

Mantis — результат эволюции ботнета Meris. Ботнет Meris использовал устройства MikroTik, а Mantis расширил свой арсенал за счет целого ряда других платформ виртуальных машин; помимо этого, он позволяет запускать различные HTTP-прокси, которые используются для проведения атак. Название "Mantis" («Богомол») было выбрано по аналогии с "Meris"(«Чума»), чтобы отразить его происхождение, а также потому, что эта новая модификация наносит более мощный и быстрый удар. В последние несколько недель Mantis проявил особую активность, направив всю свою мощь против почти 1000 клиентов Cloudflare.

### Кого атакует Mantis?

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Graphic design of a botnet](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW465CFR2ZRCJDS7WAJ5KA89.png&w=715&h=402&f=webp&fit=cover&position=center)

В нашем недавнем [отчете о тенденциях DDoS-атак](https://blog.cloudflare.com/ddos-attack-trends-for-2022-q2/) мы отметили рост числа DDoS-атак по HTTP. В прошлом квартале количество таких атак возросло на 72 %, и Mantis, безусловно, способствовал этому росту. За последний месяц Mantis осуществил более 3000 DDoS-атак по HTTP против клиентов Cloudflare.

Анализируя мишени атак Mantis, мы видим, что отрасль, наиболее подвергшаяся атакам — Интернет и телекоммуникации, на нее пришлось 36 % атак. На втором месте — новости, СМИ и издательское дело, затем следуют игровая индустрия и финансы.

Анализируя местоположение этих компаний, мы видим, что более 20 % DDoS-атак были направлены на компании в США, более 15 % — на компании в России, и менее пяти процентов включали Турцию, Францию, Польшу, Украину и другие страны.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1262 Embedded Image - h1TeRG](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4592FE886Y6TBY00GK30GE.png&w=715&h=455&f=webp&fit=cover&position=center)

### Как защититься от Mantis и других DDoS-атак

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1262 Embedded Image - z8E1QS](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44FM0AZTSS4SCAHTFGNPRB.png&w=715&h=444&f=webp&fit=cover&position=center)

[Автоматизированная система DDoS-защиты](https://www.cloudflare.com/ddos/) Cloudflare использует для обнаружения и нейтрализации DDoS-атак метод динамического формирования цифровых отпечатков. Система доступна клиентам в виде [набора правил HTTP DDoS Managed](https://blog.cloudflare.com/http-ddos-managed-rules/). Набор правил по умолчанию активирован и выполняет действия по нейтрализации атак. Соответственно, если вы не вносили каких-либо изменений, вам не нужно предпринимать никаких действий, вы защищены. Кроме того, вы можете ознакомиться с нашими руководствами [Рекомендации: меры по предотвращению DDoS-атак](https://support.cloudflare.com/hc/en-us/articles/200170166) и [Реагирование на DDoS-атаки](https://support.cloudflare.com/hc/en-us/articles/200170196-Responding-to-DDoS-attacks), которые содержат дополнительные советы и рекомендации относительно оптимизации ваших конфигураций Cloudflare.

Если вы используете только [Magic Transit](https://www.cloudflare.com/magic-transit/) или [Spectrum](https://www.cloudflare.com/products/cloudflare-spectrum/), но у вас также имеются HTTP-приложения, которые не находятся под защитой Cloudflare, рекомендуем [подключить их к сервису Cloudflare WAF/CDN](https://developers.cloudflare.com/fundamentals/get-started/setup/add-site/), чтобы воспользоваться защитой уровня L7.

На этой странице

Обсудить онлайн

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2Fmantis-botnet%2F&t=Mantis%20%E2%80%94%20%D1%81%D0%B0%D0%BC%D1%8B%D0%B9%20%D0%BC%D0%BE%D1%89%D0%BD%D1%8B%D0%B9%20%D0%B1%D0%BE%D1%82%D0%BD%D0%B5%D1%82%20%D0%B7%D0%B0%20%D0%B2%D1%81%D0%B5%20%D0%B2%D1%80%D0%B5%D0%BC%D1%8F%20%D0%BD%D0%B0%D0%B1%D0%BB%D1%8E%D0%B4%D0%B5%D0%BD%D0%B8%D0%B9)[](https://x.com/intent/post?text=Mantis+%E2%80%94+%D1%81%D0%B0%D0%BC%D1%8B%D0%B9+%D0%BC%D0%BE%D1%89%D0%BD%D1%8B%D0%B9+%D0%B1%D0%BE%D1%82%D0%BD%D0%B5%D1%82+%D0%B7%D0%B0+%D0%B2%D1%81%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F+%D0%BD%D0%B0%D0%B1%D0%BB%D1%8E%D0%B4%D0%B5%D0%BD%D0%B8%D0%B9&url=https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2Fmantis-botnet%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2Fmantis-botnet%2F)[](https://bsky.app/intent/compose?text=Mantis+%E2%80%94+%D1%81%D0%B0%D0%BC%D1%8B%D0%B9+%D0%BC%D0%BE%D1%89%D0%BD%D1%8B%D0%B9+%D0%B1%D0%BE%D1%82%D0%BD%D0%B5%D1%82+%D0%B7%D0%B0+%D0%B2%D1%81%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F+%D0%BD%D0%B0%D0%B1%D0%BB%D1%8E%D0%B4%D0%B5%D0%BD%D0%B8%D0%B9+https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2Fmantis-botnet%2F)[](https://mastodonshare.com/?text=Mantis+%E2%80%94+%D1%81%D0%B0%D0%BC%D1%8B%D0%B9+%D0%BC%D0%BE%D1%89%D0%BD%D1%8B%D0%B9+%D0%B1%D0%BE%D1%82%D0%BD%D0%B5%D1%82+%D0%B7%D0%B0+%D0%B2%D1%81%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F+%D0%BD%D0%B0%D0%B1%D0%BB%D1%8E%D0%B4%D0%B5%D0%BD%D0%B8%D0%B9&url=https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2Fmantis-botnet%2F)[](https://www.threads.net/intent/post?text=Mantis+%E2%80%94+%D1%81%D0%B0%D0%BC%D1%8B%D0%B9+%D0%BC%D0%BE%D1%89%D0%BD%D1%8B%D0%B9+%D0%B1%D0%BE%D1%82%D0%BD%D0%B5%D1%82+%D0%B7%D0%B0+%D0%B2%D1%81%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F+%D0%BD%D0%B0%D0%B1%D0%BB%D1%8E%D0%B4%D0%B5%D0%BD%D0%B8%D0%B9+https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2Fmantis-botnet%2F)

## Связанные теги

[Botnet](https://blog.cloudflare.com/ru-ru/tag/botnet/)[DDoS](https://blog.cloudflare.com/ru-ru/tag/ddos/)[Trends](https://blog.cloudflare.com/ru-ru/tag/trends/)

Подписывайтесь в социальных сетях

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Подпишитесь на уведомления о новых публикациях

Электронная почта

Мы никогда не передаем ваш адрес электронной почты третьим лицам.

Подписаться

Спасибо за подписку! Проверьте папку «Входящие», чтобы подтвердить подписку.
