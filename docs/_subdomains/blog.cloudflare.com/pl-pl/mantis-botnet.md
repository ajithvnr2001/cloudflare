---
url: https://blog.cloudflare.com/pl-pl/mantis-botnet/
title: Mantis \u2014 najpot\u0119\u017cniejszy botnet w historii | Blog Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:44:28.912800+00:00
---

# Mantis — najpotężniejszy botnet w historii | Blog Cloudflare

> Source: https://blog.cloudflare.com/pl-pl/mantis-botnet/

[Blog](https://blog.cloudflare.com/pl-pl/)

[Botnet](https://blog.cloudflare.com/pl-pl/tag/botnet/)[DDoS](https://blog.cloudflare.com/pl-pl/tag/ddos/)[Trends](https://blog.cloudflare.com/pl-pl/tag/trends/)

3 tagówPokaż 3 tagów

  * Tagi wpisu
  * [DDoS](https://blog.cloudflare.com/pl-pl/tag/ddos/)
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



[Botnet](https://blog.cloudflare.com/pl-pl/tag/botnet/)[DDoS](https://blog.cloudflare.com/pl-pl/tag/ddos/)[Trends](https://blog.cloudflare.com/pl-pl/tag/trends/)

14 lipca 2022

# Mantis — najpotężniejszy botnet w historii

![Omer Yoachimik](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW485W0MZ0R9VGWD75RQN9ZH.png&w=64&h=64&f=webp&fit=cover&position=center)

[Omer Yoachimik](https://blog.cloudflare.com/pl-pl/author/omer/)

4 min czytania

KOPIUJ URL

Ten wpis jest również dostępny w [English](https://blog.cloudflare.com/mantis-botnet/), [Español](https://blog.cloudflare.com/es-es/mantis-botnet/), [繁體中文](https://blog.cloudflare.com/zh-tw/mantis-botnet/), [简体中文](https://blog.cloudflare.com/zh-cn/mantis-botnet/) i [Русский](https://blog.cloudflare.com/ru-ru/mantis-botnet/).

![Mantis - the most powerful botnet to date](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44D3QXVC54AT00X2AV2FHT.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAAixsAjjgAlFkhmGY6mGA2k00bjDsAhjgAiyIAkkgAoHFFq4NarHxVpGU7lk0RikQAjCgAl1QYrIRbu5lxvZFqs3ZOoVoqj04PjioAmVkjsIpjwZ95xJdxuHtUpV0vkVEbkCgAmVMarIFeupVzvIxqsnBLoVQkkUwRkyIAl0UAoWtMqHpfqXBVo1YymEAAjkAAlBsAlTMAlU0ylFVEk0c2kS4AjiEAizEAlRcAkykAjzwhiz41iSsgiQAAigMAiikA)

W czerwcu 2022 roku poinformowaliśmy o największym ataku DDoS przez HTTPS, z jakim mieliśmy do czynienia — [wysyłał on 26 milionów żądań na sekundę](https://blog.cloudflare.com/26m-rps-ddos/) i był największym tego typu atakiem w historii. Nasze systemy automatycznie wykryły i złagodziły ten i wiele innych ataków. Od tamtej pory śledzimy ten [botnet](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-botnet/), który nazwaliśmy „Mantis”, oraz ataki, które przeprowadził przeciw tysiącowi klientom Cloudflare.

Klienci Cloudflare korzystający z rozwiązań [WAF](https://www.cloudflare.com/waf/)/[CDN](https://www.cloudflare.com/cdn/) są chronieni przed atakami DDoS przez HTTP, w tym ataki Mantis. Na końcu tego artykułu dostępne są dodatkowe porady, jak chronić zasoby internetowe przed atakami DDoS.

### Czy znasz już Mantis?

Botnet, który w ramach ataku DDoS wysyłał 26 milionów RPS (żądań na sekundę), nazwaliśmy „Mantis”, ponieważ przypomina tak zwane [ustonogi (ang. mantis shrimp)](https://pl.wikipedia.org/wiki/Ustonogi) — niewielkie stworzenie o ogromnej mocy. Ustonogi mają niecałe 10 cm długości, ale ich szczypce są tak mocne, że potrafią stworzyć falę uderzeniową o sile 1500 [N](https://en.wikipedia.org/wiki/Newton_\(unit\)) przy prędkości 83 km/h ze startu zatrzymanego. Podobnie botnet Mantis dysponuje niewielką flotą około 5000 botów, jednak jest w stanie wygenerować ogromną moc, odpowiedzialną za największe ataki DDoS przez HTTP, jakich byliśmy świadkiem.

Ustonog. Źródło: [Wikipedia](https://en.wikipedia.org/wiki/File:OdontodactylusScyllarus2.jpg).

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Image of the Mantis shrimp from Wikipedia](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44KPTQ080QEXHTQN4SW8JZ.png&w=715&h=354&f=webp&fit=cover&position=center)

Botnet Mantis był w stanie wygenerować 26 milionów żądań HTTPS na sekundę z użyciem **jedynie** 5000 botów. Powtórzę: 26 milionów żądań HTTPS na sekundę z użyciem **jedynie** 5000 botów. To średnio 5200 HTTPS żądań na sekundę na jednego bota. Już samo wygenerowanie 26 milionów żądań HTTP jest trudne, a Mantis zrobił to przez [HTTPS](https://www.cloudflare.com/learning/ssl/what-is-https/), co wymagało dodatkowo ustanowienia bezpiecznego połączenia. Ataki DDoS przez HTTPS są kosztowniejsze z punktu widzenia wymaganych zasobów obliczeniowych, ze względu na wyższy koszt ustanowienia bezpiecznego połączenia szyfrowanego [TLS](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/). To zdecydowanie wyróżnia ten botnet i jego moc.

W przeciwieństwie do „tradycyjnych” botnetów, na które składają się [urządzenia Internetu rzeczy (IoT)](https://www.cloudflare.com/learning/ddos/glossary/internet-of-things-iot/), takie jak cyfrowe rejestratory wideo, kamery CCTC czy czujniki dymu, Mantis wykorzystuje przejęte maszyny wirtualne i potężne serwery. Dzięki temu każdy bot ma znacznie więcej zasobów obliczeniowych, co daje temu botnetowi porażającą moc.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Graph of the 26 million requests per second DDoS attack](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48HHHY8YMMV9MB1QW97E4N.png&w=715&h=328&f=webp&fit=cover&position=center)

Mantis to następstwo botnetu Meris. Meris wykorzystywał urządzenia MikroTik, natomiast Mantis poszedł dalej i obejmuje rozmaite platformy maszyn wirtualnych, a także wspiera uruchomienie wielu serwerów proxy HTTP w celu przeprowadzenia ataku. Nazwę „Mantis” wybrano także ze względu na podobieństwo do „Meris”, by przypominała o pochodzeniu tego botnetu oraz o jego niespodziewanej sile. W ciągu ostatnich kilku tygodni Mantis był szczególnie aktywny, wykorzystując swoją moc przeciwko prawie 1000 klientów Cloudflare.

### Kogo atakuje Mantis?

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Graphic design of a botnet](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW465CFR2ZRCJDS7WAJ5KA89.png&w=715&h=402&f=webp&fit=cover&position=center)

W ostatnim [raporcie nt. trendów w atakach DDoS](https://blog.cloudflare.com/ddos-attack-trends-for-2022-q2/) omówiliśmy rosnącą liczbę ataków DDoS przez HTTP. W ostatniej kwarcie liczba tego typu ataków wzrosła o 72%, a Mantis zdecydowaniu przyczynił się do tego wzrostu. W ostatnim miesiącu Mantis przeprowadził ponad 3000 ataków DDoS przez HTTP przeciw klientom Cloudflare.

Przyglądając się celom Mantis, widzimy, że najczęściej atakowaną branżą, stanowiącą cel aż 36% ataków, był Internet i telekomunikacja. Na drugim miejscu znajduje się branża medialno‑wydawnicza, natomiast na trzecim są gry oraz finanse.

Jeśli chodzi o lokalizację tych firm, celem ponad 20% ataków były firmy położone w USA, a ponad 15% — w Rosji. Niecałe 5% ataków celowało w firmy w Turcji, Francji, Polsce, Ukrainie i innych krajach.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1262 Embedded Image - h1TeRG](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4592FE886Y6TBY00GK30GE.png&w=715&h=455&f=webp&fit=cover&position=center)

### Jak chronić się przed Mantis i innymi atakami DDoS

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1262 Embedded Image - z8E1QS](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44FM0AZTSS4SCAHTFGNPRB.png&w=715&h=444&f=webp&fit=cover&position=center)

System [zautomatyzowanej ochrony przed atakami DDoS](https://www.cloudflare.com/ddos/) Cloudflare wykorzystuje dynamiczne tworzenie odcisków cyfrowych do wykrywania i łagodzenia DDoS. System jest dostępny dla klientów jako [zarządzane zestawy reguł DDoS HTTP](https://blog.cloudflare.com/http-ddos-managed-rules/). Domyślnie zestaw reguł jest włączony i przeprowadza działania łagodzące, więc jeśli w Twoim systemie nie wprowadzono żadnych zmian, nie musisz nic robić — Twoja organizacja jest chroniona. Możesz także zapoznać się z naszymi poradnikami na temat [zapobiegania atakom DDoS](https://support.cloudflare.com/hc/en-us/articles/200170166) i [reagowania na ataki DDoS](https://support.cloudflare.com/hc/en-us/articles/200170196-Responding-to-DDoS-attacks), gdzie znajdziesz dodatkowe rady i zalecenia, jak zoptymalizować swoją konfigurację usług Cloudflare.

Jeśli korzystasz jedynie z [Magic Transit](https://www.cloudflare.com/magic-transit/) lub [Spectrum](https://www.cloudflare.com/products/cloudflare-spectrum/), ale jednocześnie prowadzisz aplikacje HTTP niechronione przez Cloudflare, zalecamy [dodać je do usługi WAF/CDN Cloudflare](https://developers.cloudflare.com/fundamentals/get-started/setup/add-site/) w celu zapewnienia ochrony warstwy 7.

Na tej stronie

Dyskutuj online

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fmantis-botnet%2F&t=Mantis%20%E2%80%94%20najpot%C4%99%C5%BCniejszy%20botnet%20w%20historii)[](https://x.com/intent/post?text=Mantis+%E2%80%94+najpot%C4%99%C5%BCniejszy+botnet+w+historii&url=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fmantis-botnet%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fmantis-botnet%2F)[](https://bsky.app/intent/compose?text=Mantis+%E2%80%94+najpot%C4%99%C5%BCniejszy+botnet+w+historii+https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fmantis-botnet%2F)[](https://mastodonshare.com/?text=Mantis+%E2%80%94+najpot%C4%99%C5%BCniejszy+botnet+w+historii&url=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fmantis-botnet%2F)[](https://www.threads.net/intent/post?text=Mantis+%E2%80%94+najpot%C4%99%C5%BCniejszy+botnet+w+historii+https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fmantis-botnet%2F)

## Powiązane tagi

[Botnet](https://blog.cloudflare.com/pl-pl/tag/botnet/)[DDoS](https://blog.cloudflare.com/pl-pl/tag/ddos/)[Trends](https://blog.cloudflare.com/pl-pl/tag/trends/)

Śledź nas w mediach społecznościowych

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Zapisz się, aby otrzymywać powiadomienia o nowych postach

Adres e-mail

Nigdy nie udostępnimy Twojego adresu e-mail.

Subskrybuj

Dziękujemy za subskrypcję! Sprawdź skrzynkę odbiorczą, aby ją potwierdzić.
