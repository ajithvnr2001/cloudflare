---
url: https://blog.cloudflare.com/pl-pl/location-aware-ddos-protection/
title: Przedstawiamy system Location-Aware DDoS Protection | Blog Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:44:29.482836+00:00
---

# Przedstawiamy system Location-Aware DDoS Protection | Blog Cloudflare

> Source: https://blog.cloudflare.com/pl-pl/location-aware-ddos-protection/

[Blog](https://blog.cloudflare.com/pl-pl/)

[Advanced DDoS](https://blog.cloudflare.com/pl-pl/tag/advanced-ddos/)[Attacks](https://blog.cloudflare.com/pl-pl/tag/attacks/)[DDoS](https://blog.cloudflare.com/pl-pl/tag/ddos/)+2Pokaż 2 więcej tagów

5 tagówPokaż 5 tagów

  * Tagi wpisu
  * [DDoS](https://blog.cloudflare.com/pl-pl/tag/ddos/)[Managed Rules (PL)](https://blog.cloudflare.com/pl-pl/tag/managed-rules/)[Produkty](https://blog.cloudflare.com/pl-pl/tag/product-news/)
  * Wszystkie tagi
  * Pasujące tagi
  * Nie znaleziono tagów
  * [1.1.1.1](https://blog.cloudflare.com/pl-pl/tag/1-1-1-1/)
  * [Agenty](https://blog.cloudflare.com/pl-pl/tag/agents/)
  * [SI](https://blog.cloudflare.com/pl-pl/tag/ai/)
  * [Zarządzanie ruchem botów](https://blog.cloudflare.com/pl-pl/tag/bot-management/)
  * [Cloudflare One](https://blog.cloudflare.com/pl-pl/tag/cloudflare-one/)
  * [Code Orange](https://blog.cloudflare.com/pl-pl/tag/code-orange/)
  * [Usługi dla konsumentów](https://blog.cloudflare.com/pl-pl/tag/consumer-services/)
  * [DDoS](https://blog.cloudflare.com/pl-pl/tag/ddos/)
  * [DDoS Alerts (PL)](https://blog.cloudflare.com/pl-pl/tag/ddos-alerts/)
  * [Raporty dotyczące ataków DDoS](https://blog.cloudflare.com/pl-pl/tag/ddos-reports/)
  * [Programiści](https://blog.cloudflare.com/pl-pl/tag/developers/)
  * [DNS](https://blog.cloudflare.com/pl-pl/tag/dns/)
  * [Życie w Cloudflare](https://blog.cloudflare.com/pl-pl/tag/life-at-cloudflare/)
  * [Managed Rules (PL)](https://blog.cloudflare.com/pl-pl/tag/managed-rules/)
  * [Micro-frontends (PL)](https://blog.cloudflare.com/pl-pl/tag/micro-frontends/)
  * [Awaria](https://blog.cloudflare.com/pl-pl/tag/outage/)
  * [Partnerzy](https://blog.cloudflare.com/pl-pl/tag/partners/)
  * [Polityka i prawo](https://blog.cloudflare.com/pl-pl/tag/policy/)
  * [Analiza przypadku](https://blog.cloudflare.com/pl-pl/tag/post-mortem/)
  * [Prywatność](https://blog.cloudflare.com/pl-pl/tag/privacy/)
  * [Produkty](https://blog.cloudflare.com/pl-pl/tag/product-news/)
  * [Radar](https://blog.cloudflare.com/pl-pl/tag/cloudflare-radar/)
  * [Bezpieczeństwo](https://blog.cloudflare.com/pl-pl/tag/security/)
  * [Szybkość i niezawodność](https://blog.cloudflare.com/pl-pl/tag/speed-and-reliability/)
  * [Przejrzystość](https://blog.cloudflare.com/pl-pl/tag/transparency/)
  * [Zero Trust](https://blog.cloudflare.com/pl-pl/tag/zero-trust/)



[Managed Rules (PL)](https://blog.cloudflare.com/pl-pl/tag/managed-rules/)[Produkty](https://blog.cloudflare.com/pl-pl/tag/product-news/)

[Advanced DDoS](https://blog.cloudflare.com/pl-pl/tag/advanced-ddos/)[Attacks](https://blog.cloudflare.com/pl-pl/tag/attacks/)[DDoS](https://blog.cloudflare.com/pl-pl/tag/ddos/)[Managed Rules (PL)](https://blog.cloudflare.com/pl-pl/tag/managed-rules/)[Produkty](https://blog.cloudflare.com/pl-pl/tag/product-news/)

11 lipca 2022

# Przedstawiamy system Location-Aware DDoS Protection

![Omer Yoachimik](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW485W0MZ0R9VGWD75RQN9ZH.png&w=64&h=64&f=webp&fit=cover&position=center)![Julien Desgats](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW490NXEPS0Y3GYM6MEBDP98.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Omer Yoachimik](https://blog.cloudflare.com/pl-pl/author/omer/) i [Julien Desgats](https://blog.cloudflare.com/pl-pl/author/julien-desgats/)

3 min czytania

KOPIUJ URL

Ten wpis jest również dostępny w [English](https://blog.cloudflare.com/location-aware-ddos-protection/), [Español](https://blog.cloudflare.com/es-es/location-aware-ddos-protection/), [繁體中文](https://blog.cloudflare.com/zh-tw/location-aware-ddos-protection/), [简体中文](https://blog.cloudflare.com/zh-cn/location-aware-ddos-protection/) i [Русский](https://blog.cloudflare.com/ru-ru/location-aware-ddos-protection/).

![Introducing Location-Aware DDoS Protection](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44XYSQSGS8HMQZY1RKA9A3.png&w=1801&h=1013&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////////8u/u6eXg7Oro8/P28vT66+3y/////v7/6+Ti39PP4tjZ6ufu6uv14uXv/////vz/5trX1sC82cfK49zm5OTy2t7t////////6NnV1ry22cTH5Nvm5eX029/u////////8eTg4szF5dTT8Onw8PD85un1/////////vfw8+bd9+3p//3/////9vn+//////////////vx///7///////////////////////////4////////////////)

Z przyjemnością prezentujemy rozpoznający lokalizację system ochrony przed atakami DDoS od Cloudflare.

[Ataki typu „rozproszona odmowa usługi” (DDoS)](https://www.cloudflare.com/en-gb/learning/ddos/what-is-a-ddos-attack/) to rodzaj cyberataków, których celem jest zablokowanie zasobu internetowego poprzez wysłanie więcej żądań, niż jest on w stanie obsłużyć. Dlatego sprawcy zwykle generują jak największy ruch z jak największej liczby lokalizacji. To, że jest to _rozproszony_ atak, działa więc na korzyść cyberprzestępcy, jednak nasz rozpoznający lokalizację system ochrony wykorzystuje ten fakt przeciwko niemu.

System Location‑Aware DDoS Protection jest teraz dostępny w fazie beta dla klientów Cloudflare korzystających z planu Enterprise z subskrypcją usługi Advanced DDoS.

### Rozproszone ataki tracą przewagę

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![A diagram of a DDoS attack denying service to legitimate users](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW472HXAC4PA7D5EEXCTTT76.png&w=715&h=378&f=webp&fit=cover&position=center)

System Location‑Aware DDoS Protection od Cloudflare wykorzystuje przewagę sprawcy ataku przeciwko niemu. Nasz system uczy się, skąd pochodzi ruch na Twojej stronie, dzięki czemu rozpoznaje lokalizacje i, wykrywając nowy ruch, stale zadaje pytanie: „Czy to ma sens dla _tej_ strony internetowej?”.

Na przykład jeśli prowadzisz stronę e‑commerce skierowaną głównie do niemieckiech konsumentów, większość ruchu prawdopodobnie pochodzi z Niemiec, niewielka jego część z sąsiednich krajów europejskich, a jeszcze mniejsza część z pozostałych regionów świata. Jeśli nagle wrośnie ruch pochodzący z nietypowych dla tej strony obszarów geograficznych, system oflaguje i złagodzi niechciany ruch.

System Location-Aware DDoS Protection wykorzystuje także [modele uczenia maszynowego](https://developers.cloudflare.com/bots/concepts/bot-score/#machine-learning) Cloudflare do identyfikacji ruchu, który prawdopodobnie jest zautomatyzowany. Stanowi to dodatkowy sygnał w celu zapewnienia dokładniejszej ochrony.

### Włączenie ochrony rozpoznającej lokalizację

Klienci korzystający z planu Enterprise z subskrypcją usługi Advanced DDoS mogą spersonalizować i włączyć system Location‑Aware DDoS Protection. Domyślnie system będzie pokazywać jedynie podejrzany ruch zidentyfikowany na podstawie wartości w 95. percentylu z ostatnich 7 dni, podzielonych według kraju i regionu klienta. Wartości są kalkulowane ponownie co 24 godziny.

Klienci mogą sprawdzić, co zostało oflagowane, na [**pulpicie nawigacyjnym zabezpieczeń**](https://dash.cloudflare.com/?to=/:account/:zone/security).

System Location-Aware DDoS Protection jest dostępny dla klientów jako nowa reguła zarządzana DDoS HTTP wewnątrz istniejącego zestawu reguł. Aby go włączyć, należy zmienić działanie na _Managed Challenge_ lub _Block_. Klienci mogą dostosować poziom czułości systemu, by dopuścić mniejszą lub większą ilość ruchu różniącego się od typowych obszarów geograficznych. Im niższa czułość, tym wyższa tolerancja.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Screenshot of Cloudflare’s Security Overview analytics dashboard showing the traffic that was flagged by the Location-Aware DDoS Protection rule](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45YDD115NQ5PRVJ2141X1V.png&w=715&h=685&f=webp&fit=cover&position=center)

Aby dowiedzieć się, gdzie zobaczyć oflagowany ruch i jak skonfigurować system Location-Aware DDoS Protection, odwiedź naszą [stronę z dokumentacją dla deweloperów](https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/location-aware-protection/).

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Screenshot of Cloudflare’s dashboard showing the Location-Aware DDoS Protection rule](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49NPQJDGYYKANPX1XXBT2P.png&w=715&h=418&f=webp&fit=cover&position=center)

### Ryzyko ataków DDoS przejdzie do historii

Misją Cloudflare jest pomóc budować lepszy Internet. Na tej podstawie powstała wizja zespołu odpowiedzialnego za ochronę przed DDoS — chcemy sprawić, by ryzyko ataków DDoS przeszło do historii. System Location-Aware DDoS Protection to dopiero pierwszy krok na drodze do jeszcze bardziej inteligentnej, wyrafinowanej i dostosowanej do indywidualnych potrzeb ochrony przed atakami DDoS.

Nie korzystasz jeszcze z rozwiązań Cloudflare? [Zacznij teraz](https://dash.cloudflare.com/sign-up) i zabezpiecz swoje strony internetowe [planem](https://www.cloudflare.com/plans/) Free lub Pro albo [skontaktuj się z nami](https://www.cloudflare.com/magic-transit/), by dowiedzieć się więcej o pakiecie Advanced DDoS Protection dla klientów Enterprise.

Na tej stronie

Dyskutuj online

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Flocation-aware-ddos-protection%2F&t=Przedstawiamy%20system%20Location-Aware%20DDoS%20Protection)[](https://x.com/intent/post?text=Przedstawiamy+system+Location-Aware+DDoS+Protection&url=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Flocation-aware-ddos-protection%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Flocation-aware-ddos-protection%2F)[](https://bsky.app/intent/compose?text=Przedstawiamy+system+Location-Aware+DDoS+Protection+https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Flocation-aware-ddos-protection%2F)[](https://mastodonshare.com/?text=Przedstawiamy+system+Location-Aware+DDoS+Protection&url=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Flocation-aware-ddos-protection%2F)[](https://www.threads.net/intent/post?text=Przedstawiamy+system+Location-Aware+DDoS+Protection+https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Flocation-aware-ddos-protection%2F)

## Powiązane tagi

[Advanced DDoS](https://blog.cloudflare.com/pl-pl/tag/advanced-ddos/)[Attacks](https://blog.cloudflare.com/pl-pl/tag/attacks/)[DDoS](https://blog.cloudflare.com/pl-pl/tag/ddos/)[Managed Rules (PL)](https://blog.cloudflare.com/pl-pl/tag/managed-rules/)[Produkty](https://blog.cloudflare.com/pl-pl/tag/product-news/)

Śledź nas w mediach społecznościowych

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Zapisz się, aby otrzymywać powiadomienia o nowych postach

Adres e-mail

Nigdy nie udostępnimy Twojego adresu e-mail.

Subskrybuj

Dziękujemy za subskrypcję! Sprawdź skrzynkę odbiorczą, aby ją potwierdzić.
