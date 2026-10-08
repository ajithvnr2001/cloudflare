---
url: https://blog.cloudflare.com/ru-ru/26m-rps-ddos/
title: Cloudflare \u043d\u0435\u0439\u0442\u0440\u0430\u043b\u0438\u0437\u043e\u0432\u0430\u043b\u0430 DDoS-\u0430\u0442\u0430\u043a\u0443 \u043c\u043e\u0449\u043d\u043e\u0441\u0442\u044c\u044e 26 \u043c\u043b\u043d \u0437\u0430\u043f\u0440\u043e\u0441\u043e\u0432 \u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0443 | \u0411\u043b\u043e\u0433 Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:37:36.662551+00:00
---

# Cloudflare нейтрализовала DDoS-атаку мощностью 26 млн запросов в секунду | Блог Cloudflare

> Source: https://blog.cloudflare.com/ru-ru/26m-rps-ddos/

[Блог](https://blog.cloudflare.com/ru-ru/)

[Attacks](https://blog.cloudflare.com/ru-ru/tag/attacks/)[Botnet](https://blog.cloudflare.com/ru-ru/tag/botnet/)[DDoS](https://blog.cloudflare.com/ru-ru/tag/ddos/)+1Показать ещё 1 тегов

4 теговПоказать 4 тегов

  * Теги публикации
  * [DDoS](https://blog.cloudflare.com/ru-ru/tag/ddos/)[Безопасность](https://blog.cloudflare.com/ru-ru/tag/security/)
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



[Безопасность](https://blog.cloudflare.com/ru-ru/tag/security/)

[Attacks](https://blog.cloudflare.com/ru-ru/tag/attacks/)[Botnet](https://blog.cloudflare.com/ru-ru/tag/botnet/)[DDoS](https://blog.cloudflare.com/ru-ru/tag/ddos/)[Безопасность](https://blog.cloudflare.com/ru-ru/tag/security/)

14 июня 2022 г.

# Cloudflare нейтрализовала DDoS-атаку мощностью 26 млн запросов в секунду

![Omer Yoachimik](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW485W0MZ0R9VGWD75RQN9ZH.png&w=64&h=64&f=webp&fit=cover&position=center)

[Omer Yoachimik](https://blog.cloudflare.com/ru-ru/author/omer/)

4 мин. чтения

КОПИРОВАТЬ URL

Этот пост также доступен на [English](https://blog.cloudflare.com/26m-rps-ddos/), [Deutsch](https://blog.cloudflare.com/de-de/26m-rps-ddos/), [Español](https://blog.cloudflare.com/es-es/26m-rps-ddos/), [Français](https://blog.cloudflare.com/fr-fr/26m-rps-ddos/), [Italiano](https://blog.cloudflare.com/it-it/26m-rps-ddos/), [日本語](https://blog.cloudflare.com/ja-jp/26m-rps-ddos/), [한국어](https://blog.cloudflare.com/ko-kr/26m-rps-ddos/), [繁體中文](https://blog.cloudflare.com/zh-tw/26m-rps-ddos/), [简体中文](https://blog.cloudflare.com/zh-cn/26m-rps-ddos/), [Português](https://blog.cloudflare.com/pt-br/26m-rps-ddos/) и [Polski](https://blog.cloudflare.com/pl-pl/26m-rps-ddos/).

![Cloudflare mitigates 26 million request per second DDoS attack](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44WF2925PZM0DDZZ9CTCZY.png&w=1830&h=850&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA8e/z29nln5/DZmuqf4SzsbTLycnXysjW9/f54+PssbHOkZG9q6vJ0tLd4ODl19fe////7vD1yMjeuLbT09Dh8vDy9/f05+nq////+v3/3t7t19Tn8Oz0////////9ff0////////8fH67Or2//3////////////9/////////v7/+fn/////////////////////////////////////////////////////////////////////////////////)

_**Обновление от 24 июня 2022 года:** Мы назвали ботнет, осуществивший DDoS-атаку мощностью 26 млн запросов в секунду, Mantis (Богомол), поскольку он имеет сходство с_ _[раком-богомолом](https://en.wikipedia.org/wiki/Mantis_shrimp): он невелик по размеру, но обладает очень большой силой. Mantis проявил особенную активность на прошлой неделе, осуществив DDoS-атаки по HTTP, нацеленные на интернет-ресурсы в сфере VoIP и криптовалют, мощностью 9 млн запросов в секунду._

На прошлой неделе Cloudflare автоматически обнаружила и нейтрализовала [DDoS-атаку](https://www.cloudflare.com/en-gb/learning/ddos/what-is-a-ddos-attack/) мощностью 26 млн запросов в секунду — самую крупную DDoS-атаку по HTTPS за все время наблюдений.

Мишенью атаки стал один из клиентов Cloudflare, использующий план Free. Как и при прошлой [атаке мощностью 15 млн запросов в секунду](https://blog.cloudflare.com/15m-rps-ddos-attack/), источниками трафика в основном служили поставщики облачных сервисов, а не домашние интернет-провайдеры, что указывает на использование для проведения атаки взломанных виртуальных машин и мощных серверов, а не гораздо менее производительных устройств Интернета вещей (IoT).

### Атаки бьют рекорды

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Graph of the 26 million request per second DDoS attack](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44GBBN0SYPNE31Q00ATYYN.png&w=715&h=328&f=webp&fit=cover&position=center)

В течение прошедшего года мы регистрировали одну за другой рекордные атаки. В августе 2021 года мы сообщили о [DDoS-атаке по HTTP мощностью 17,2 млн запросов/сек.](https://blog.cloudflare.com/cloudflare-thwarts-17-2m-rps-ddos-attack-the-largest-ever-reported/), а в апреле имела место [DDoS-атака по HTTPS мощностью 15 млн запросов/сек](https://blog.cloudflare.com/15m-rps-ddos-attack/). Все они были автоматически обнаружены и нейтрализованы с помощью нашего [набора правил HTTP DDoS Managed](https://blog.cloudflare.com/http-ddos-managed-rules/), в основе которого лежит наша [автономная периферийная система DDoS-защиты](https://blog.cloudflare.com/deep-dive-cloudflare-autonomous-edge-ddos-protection/).

DDoS-атака мощностью 26 млн запросов/сек. была осуществлена небольшим, но мощным ботнетом, насчитывающим 5067 устройств. На пике каждый узел генерировал в среднем 5200 запросов/сек. Для сравнения, другой, гораздо более крупный, но менее мощный ботнет, который мы отслеживаем, насчитывает более 730 000 устройств. Однако этот более крупный ботнет генерирует не более 1 млн запросов/сек., т. е. в среднем примерно 1,3 запроса/сек. на устройство. Другими словами, этот ботнет в среднем в 4000 раз мощнее за счет использования виртуальных машин и серверов.

Также следует заметить, что данная атака производилась по [HTTPS](https://www.cloudflare.com/learning/ssl/what-is-https/). DDoS-атаки по HTTPS более затратны с точки зрения вычислительных ресурсов, поскольку требуется установить защищенное соединение с [TLS](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)-шифрованием. Поэтому для злоумышленника осуществление такой атаки затратнее, так же как и для жертвы затратнее ее нейтрализация. В прошлом мы не раз наблюдали очень мощные атаки по HTTP (без шифрования), однако данная атака особо выделяется своей ресурсозатратностью с учетом ее масштаба.

Менее чем за 30 секунд данный ботнет сгенерировал более 212 млн HTTPS-запросов из более чем 1500 сетей в 121 стране. Основные страны-источники — Индонезия, США, Бразилия и Россия. Примерно 3 % трафика атаки поступило с узлов Tor.

Основные сети-источники: OVH во Франции (ASN 16276), Telkomnet в Индонезии (ASN 7713), iboss в США (ASN 137922) и Ajeel в Ливии (ASN 37284).

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Chart of the top source countries of the attack](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45A0WAK3HK3K1DDPGRSZJC.png&w=715&h=442&f=webp&fit=cover&position=center)

### Ландшафт угроз в сфере DDoS

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Chart of the top source networks of the attack](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW447X816Q1A93RCEPWG5HGQ.png&w=715&h=442&f=webp&fit=cover&position=center)

Планируя DDoS-защиту, важно иметь представление о ландшафте угроз. Если заглянуть в наш [отчет о тенденциях в сфере DDoS](https://blog.cloudflare.com/ddos-attack-trends-for-2022-q1/), можно увидеть, что большинство атак маломощные, т.е. это кибервандализм. Однако даже небольшие атаки могут серьезно повлиять на работу незащищенных интернет-ресурсов. С другой стороны, растет мощность и частота крупных атак, но они — короткие и быстрые. Злоумышленники концентрируют мощность своего ботнета, стремясь причинить ущерб одним коротким нокаутирующим ударом — и при этом избежать обнаружения.

DDoS-атаки инициируют люди, однако генерируют их машины. К тому времени, когда люди отреагируют на атаку, она может уже закончиться. При этом, даже если атака была короткой, перебои в работе сети и приложений могут продолжаться долгое время после окончания атаки, нанося финансовый и репутационный ущерб. Поэтому для защиты интернет-ресурсов рекомендуется использовать автоматическую, постоянно включенную систему защиты, которая способна обнаруживать и нейтрализовывать атаки без участия человека.

### Наш вклад в дальнейшее развитие и совершенствование Интернета

В Cloudflare все, что мы делаем, подчинено нашей основной миссии — способствовать развитию и совершенствованию Интернета. Задачи отдела DDoS-защиты также определяются этой миссией: наша цель — лишить DDoS-атаки возможности причинять ущерб. Мы обеспечиваем [неограниченную защиту без тарификации трафика](https://blog.cloudflare.com/unmetered-mitigation/): она не ограничена мощностью атак, их числом, количеством и продолжительностью. Сейчас это особенно важно, поскольку, как мы видим в последнее время, [и мощность, и частота атак растут](https://blog.cloudflare.com/ddos-attack-trends-for-2022-q1/).

Еще не используете Cloudflare? [Начните сейчас](https://dash.cloudflare.com/sign-up), воспользовавшись нашими планами Free и Pro для защиты веб-сайтов или [свяжитесь с нами](https://www.cloudflare.com/magic-transit/), если вам необходима комплексная DDoS-защита всей вашей сети с помощью Magic Transit.

На этой странице

Обсудить онлайн

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2F26m-rps-ddos%2F&t=Cloudflare%20%D0%BD%D0%B5%D0%B9%D1%82%D1%80%D0%B0%D0%BB%D0%B8%D0%B7%D0%BE%D0%B2%D0%B0%D0%BB%D0%B0%20DDoS-%D0%B0%D1%82%D0%B0%D0%BA%D1%83%20%D0%BC%D0%BE%D1%89%D0%BD%D0%BE%D1%81%D1%82%D1%8C%D1%8E%2026%20%D0%BC%D0%BB%D0%BD%20%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%81%D0%BE%D0%B2%20%D0%B2%20%D1%81%D0%B5%D0%BA%D1%83%D0%BD%D0%B4%D1%83)[](https://x.com/intent/post?text=Cloudflare+%D0%BD%D0%B5%D0%B9%D1%82%D1%80%D0%B0%D0%BB%D0%B8%D0%B7%D0%BE%D0%B2%D0%B0%D0%BB%D0%B0+DDoS-%D0%B0%D1%82%D0%B0%D0%BA%D1%83+%D0%BC%D0%BE%D1%89%D0%BD%D0%BE%D1%81%D1%82%D1%8C%D1%8E+26+%D0%BC%D0%BB%D0%BD+%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%81%D0%BE%D0%B2+%D0%B2+%D1%81%D0%B5%D0%BA%D1%83%D0%BD%D0%B4%D1%83&url=https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2F26m-rps-ddos%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2F26m-rps-ddos%2F)[](https://bsky.app/intent/compose?text=Cloudflare+%D0%BD%D0%B5%D0%B9%D1%82%D1%80%D0%B0%D0%BB%D0%B8%D0%B7%D0%BE%D0%B2%D0%B0%D0%BB%D0%B0+DDoS-%D0%B0%D1%82%D0%B0%D0%BA%D1%83+%D0%BC%D0%BE%D1%89%D0%BD%D0%BE%D1%81%D1%82%D1%8C%D1%8E+26+%D0%BC%D0%BB%D0%BD+%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%81%D0%BE%D0%B2+%D0%B2+%D1%81%D0%B5%D0%BA%D1%83%D0%BD%D0%B4%D1%83+https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2F26m-rps-ddos%2F)[](https://mastodonshare.com/?text=Cloudflare+%D0%BD%D0%B5%D0%B9%D1%82%D1%80%D0%B0%D0%BB%D0%B8%D0%B7%D0%BE%D0%B2%D0%B0%D0%BB%D0%B0+DDoS-%D0%B0%D1%82%D0%B0%D0%BA%D1%83+%D0%BC%D0%BE%D1%89%D0%BD%D0%BE%D1%81%D1%82%D1%8C%D1%8E+26+%D0%BC%D0%BB%D0%BD+%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%81%D0%BE%D0%B2+%D0%B2+%D1%81%D0%B5%D0%BA%D1%83%D0%BD%D0%B4%D1%83&url=https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2F26m-rps-ddos%2F)[](https://www.threads.net/intent/post?text=Cloudflare+%D0%BD%D0%B5%D0%B9%D1%82%D1%80%D0%B0%D0%BB%D0%B8%D0%B7%D0%BE%D0%B2%D0%B0%D0%BB%D0%B0+DDoS-%D0%B0%D1%82%D0%B0%D0%BA%D1%83+%D0%BC%D0%BE%D1%89%D0%BD%D0%BE%D1%81%D1%82%D1%8C%D1%8E+26+%D0%BC%D0%BB%D0%BD+%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%81%D0%BE%D0%B2+%D0%B2+%D1%81%D0%B5%D0%BA%D1%83%D0%BD%D0%B4%D1%83+https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2F26m-rps-ddos%2F)

## Связанные теги

[Attacks](https://blog.cloudflare.com/ru-ru/tag/attacks/)[Botnet](https://blog.cloudflare.com/ru-ru/tag/botnet/)[DDoS](https://blog.cloudflare.com/ru-ru/tag/ddos/)[Безопасность](https://blog.cloudflare.com/ru-ru/tag/security/)

Подписывайтесь в социальных сетях

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Подпишитесь на уведомления о новых публикациях

Электронная почта

Мы никогда не передаем ваш адрес электронной почты третьим лицам.

Подписаться

Спасибо за подписку! Проверьте папку «Входящие», чтобы подтвердить подписку.
