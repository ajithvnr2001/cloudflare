---
url: https://blog.cloudflare.com/pl-pl/26m-rps-ddos/
title: Cloudflare \u0142agodzi atak DDoS generuj\u0105cy 26 milion\u00f3w \u017c\u0105da\u0144 na sekund\u0119 | Blog Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:37:36.064030+00:00
---

# Cloudflare łagodzi atak DDoS generujący 26 milionów żądań na sekundę | Blog Cloudflare

> Source: https://blog.cloudflare.com/pl-pl/26m-rps-ddos/

[Blog](https://blog.cloudflare.com/pl-pl/)

[Attacks](https://blog.cloudflare.com/pl-pl/tag/attacks/)[Bezpieczeństwo](https://blog.cloudflare.com/pl-pl/tag/security/)[Botnet](https://blog.cloudflare.com/pl-pl/tag/botnet/)+1Pokaż 1 więcej tagów

4 tagówPokaż 4 tagów

  * Tagi wpisu
  * [Bezpieczeństwo](https://blog.cloudflare.com/pl-pl/tag/security/)[DDoS](https://blog.cloudflare.com/pl-pl/tag/ddos/)
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



[DDoS](https://blog.cloudflare.com/pl-pl/tag/ddos/)

[Attacks](https://blog.cloudflare.com/pl-pl/tag/attacks/)[Bezpieczeństwo](https://blog.cloudflare.com/pl-pl/tag/security/)[Botnet](https://blog.cloudflare.com/pl-pl/tag/botnet/)[DDoS](https://blog.cloudflare.com/pl-pl/tag/ddos/)

14 czerwca 2022

# Cloudflare łagodzi atak DDoS generujący 26 milionów żądań na sekundę

![Omer Yoachimik](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW485W0MZ0R9VGWD75RQN9ZH.png&w=64&h=64&f=webp&fit=cover&position=center)

[Omer Yoachimik](https://blog.cloudflare.com/pl-pl/author/omer/)

4 min czytania

KOPIUJ URL

Ten wpis jest również dostępny w [English](https://blog.cloudflare.com/26m-rps-ddos/), [Deutsch](https://blog.cloudflare.com/de-de/26m-rps-ddos/), [Español](https://blog.cloudflare.com/es-es/26m-rps-ddos/), [Français](https://blog.cloudflare.com/fr-fr/26m-rps-ddos/), [Italiano](https://blog.cloudflare.com/it-it/26m-rps-ddos/), [日本語](https://blog.cloudflare.com/ja-jp/26m-rps-ddos/), [한국어](https://blog.cloudflare.com/ko-kr/26m-rps-ddos/), [繁體中文](https://blog.cloudflare.com/zh-tw/26m-rps-ddos/), [简体中文](https://blog.cloudflare.com/zh-cn/26m-rps-ddos/), [Português](https://blog.cloudflare.com/pt-br/26m-rps-ddos/) i [Русский](https://blog.cloudflare.com/ru-ru/26m-rps-ddos/).

![Cloudflare mitigates 26 million request per second DDoS attack](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44WF2925PZM0DDZZ9CTCZY.png&w=1830&h=850&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA8e/z29nln5/DZmuqf4SzsbTLycnXysjW9/f54+PssbHOkZG9q6vJ0tLd4ODl19fe////7vD1yMjeuLbT09Dh8vDy9/f05+nq////+v3/3t7t19Tn8Oz0////////9ff0////////8fH67Or2//3////////////9/////////v7/+fn/////////////////////////////////////////////////////////////////////////////////)

_Aktualizacja z 24 czerwca 2022 r.: Botnetowi, który przeprowadził ten atak, nadaliśmy nazwę „Mantis”, ponieważ jest zupełnie jak_ [_ustonóg (ang. mantis shrimp)_](https://pl.wikipedia.org/wiki/Ustonogi) _— niewielki, a bardzo potężny. Mantis był szczególnie aktywny minionego tygodnia, kiedy to przeprowadził ataki DDoS na zasoby internetowe typu VoIP oraz powiązane z kryptowalutami z użyciem nawet 9 milionów żądań HTTP na sekundę._

W zeszłym tygodniu Cloudflare automatycznie wykryło i osłabiło [atak DDoS](https://www.cloudflare.com/en-gb/learning/ddos/what-is-a-ddos-attack/) wysyłający 26 milionów żądań HTTPS na sekundę — największy tego typu atak w historii.

Atak wymierzono w stronę internetową jednego z naszych klientów, który korzysta z darmowego planu ochrony. Podobnie jak wcześniejszy [atak generujący 15 milionów RPS (żądań na sekundę)](https://blog.cloudflare.com/15m-rps-ddos-attack/), i ten pochodził głównie od dostawców usług w chmurze, a nie dostawców domowych usług internetowych. To wskazuje, że wykorzystano w nim przejęte maszyny wirtualne i potężne serwery — a nie znacznie słabszych urządzeń Internetu rzeczy.

### Rekordowe ataki

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Graph of the 26 million request per second DDoS attack](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44GBBN0SYPNE31Q00ATYYN.png&w=715&h=328&f=webp&fit=cover&position=center)

W ciągu ostatniego roku przeprowadzono kolejne rekordowe ataki. W sierpniu 2021 roku ujawniliśmy [atak DDoS generujący 17,2 miliona żądań HTTP na sekundę](https://blog.cloudflare.com/cloudflare-thwarts-17-2m-rps-ddos-attack-the-largest-ever-reported/), a w kwietniu 2022 roku [atak DDoS z 15 milionami żądań HTTPS na sekundę](https://blog.cloudflare.com/15m-rps-ddos-attack/). Wszystkie zostały automatycznie wykryte i zminimalizowane przez [zarządzany zestaw reguł DDoS HTTP](https://blog.cloudflare.com/http-ddos-managed-rules/), wykorzystujący nasz [autonomiczny system ochrony krawędzi przed DDoS](https://blog.cloudflare.com/deep-dive-cloudflare-autonomous-edge-ddos-protection/).

Niewielki, ale potężny botnet składający się z 5067 urządzeń przeprowadził atak generujący 26 milionów żądań na sekundę. To oznacza, że średnio każdy węzeł wysyłał nawet 5200 RPS. Dla porównania — śledzimy także znacznie większy, ale mniej potężny botnet, utworzony przez ponad 730 000 urządzeń. Ten większy botnet nie był w stanie wygenerować więcej niż miliona żądań na sekundę, co daje średnio 1,3 RPS na jedno urządzenie. Innymi słowy, mniejszy botnet był średnio 4000 razy silniejszy — dzięki wykorzystaniu maszyn wirtualnych i serwerów.

Warto również zauważyć, że atak przeprowadzono z wykorzystaniem [HTTPS](https://www.cloudflare.com/learning/ssl/what-is-https/). Takie ataki wymagają więcej zasobów obliczeniowych ze względu na wyższy koszt ustanowienia bezpiecznego połączenia szyfrowanego za pomocą protokołu [TLS](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/). Są więc kosztowniejsze dla sprawcy, jak i dla ofiary ograniczającej skutki ataku. W przeszłości zaobserwowaliśmy bardzo duże ataki przez niezaszyfrowane HTTP, ale ten atak wyróżnia się spośród innych właśnie ze względu na zasoby wymagane przy tej skali.

W ciągu mniej niż 30 sekund ten botnet wygenerował więcej niż 212 milionów żądań HTTPS z ponad 1500 sieci w 121 krajach. Największy ruch pochodził z Indonezji, Stanów Zjednoczonych, Brazylii i Rosji. Około 3% ataku przeszło przez węzły sieci Tor.

Najczęściej wykorzystywanymi sieciami były francuska OVH (numer systemu autonomicznego: 16276), indonezyjska Telkomnet (numer SA 7713), amerykańska iboss (numer SA: 137922) i libijska Ajeel (numer SA: 37284).

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Chart of the top source countries of the attack](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45A0WAK3HK3K1DDPGRSZJC.png&w=715&h=442&f=webp&fit=cover&position=center)

### Rozmiar zagrożeń DDoS

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Chart of the top source networks of the attack](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW447X816Q1A93RCEPWG5HGQ.png&w=715&h=442&f=webp&fit=cover&position=center)

Myśląc o ochronie przed DDoS, należy zrozumieć zagrożenia, z jakimi mamy do czynienia. Jak wskazuje nasz raport na temat trendów DDoS, większość przypadków to niewielkie ataki, na przykład akty cyberwandalizmu. Jednak nawet mały atak może mieć poważny wpływ na niechronione zasoby internetowe. Jednocześnie duże ataki są coraz większe i częstsze, za to przeprowadzane szybko i nagle. To dlatego, że sprawcy skupiają moc botnetów, by wyrządzić szkody jednym mocnym ciosem, próbując uniknąć wykrycia.

Ataki DDoS są inicjowane przez ludzi, ale generują je maszyny. Zanim więc ofierze ataku uda się zareagować, może być już po wszystkim. A nawet, jeśli atak był szybki, następujące problemy w sieci i aplikacji mogą trwać jeszcze długo po nim — na czym ucierpią zarówno Twoje przychody, jak i reputacja. Z tego powodu zaleca się chronić zasoby internetowe zautomatyzowaną, zawsze aktywną usługą ochrony, która wykrywa i łagodzi ataki bez udziału ludzi.

### Pomagamy budować lepszy Internet

Cloudflare we wszystkich działaniach kieruje się misją budowania lepszego Internetu. Wizją zespołu odpowiedzialnego za ochronę przed DDoS jest sprawienie, by ryzyko tego typu ataków przeszło do historii. Dlatego oferowana przez nas ochrona jest [nieograniczona](https://blog.cloudflare.com/unmetered-mitigation/) — obowiązuje bez względu na rozmiar, liczbę czy czas trwania ataków. Jest to szczególnie istotne w dzisiejszych czasach, ponieważ jak widzieliśmy, ataki są coraz [większe i częstsze](https://blog.cloudflare.com/ddos-attack-trends-for-2022-q1/).

Nie korzystasz jeszcze z rozwiązań Cloudflare? Zacznij teraz i zabezpiecz swoje strony internetowe planem Free lub Pro, albo skontaktuj się z nami, by dowiedzieć się więcej o kompleksowej ochronie całej sieci przed atakami DDoS, którą zapewnia rozwiązanie Magic Transit.

Na tej stronie

Dyskutuj online

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2F26m-rps-ddos%2F&t=Cloudflare%20%C5%82agodzi%20atak%20DDoS%20generuj%C4%85cy%2026%20milion%C3%B3w%20%C5%BC%C4%85da%C5%84%20na%20sekund%C4%99)[](https://x.com/intent/post?text=Cloudflare+%C5%82agodzi+atak+DDoS+generuj%C4%85cy+26+milion%C3%B3w+%C5%BC%C4%85da%C5%84+na+sekund%C4%99&url=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2F26m-rps-ddos%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2F26m-rps-ddos%2F)[](https://bsky.app/intent/compose?text=Cloudflare+%C5%82agodzi+atak+DDoS+generuj%C4%85cy+26+milion%C3%B3w+%C5%BC%C4%85da%C5%84+na+sekund%C4%99+https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2F26m-rps-ddos%2F)[](https://mastodonshare.com/?text=Cloudflare+%C5%82agodzi+atak+DDoS+generuj%C4%85cy+26+milion%C3%B3w+%C5%BC%C4%85da%C5%84+na+sekund%C4%99&url=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2F26m-rps-ddos%2F)[](https://www.threads.net/intent/post?text=Cloudflare+%C5%82agodzi+atak+DDoS+generuj%C4%85cy+26+milion%C3%B3w+%C5%BC%C4%85da%C5%84+na+sekund%C4%99+https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2F26m-rps-ddos%2F)

## Powiązane tagi

[Attacks](https://blog.cloudflare.com/pl-pl/tag/attacks/)[Bezpieczeństwo](https://blog.cloudflare.com/pl-pl/tag/security/)[Botnet](https://blog.cloudflare.com/pl-pl/tag/botnet/)[DDoS](https://blog.cloudflare.com/pl-pl/tag/ddos/)

Śledź nas w mediach społecznościowych

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Zapisz się, aby otrzymywać powiadomienia o nowych postach

Adres e-mail

Nigdy nie udostępnimy Twojego adresu e-mail.

Subskrybuj

Dziękujemy za subskrypcję! Sprawdź skrzynkę odbiorczą, aby ją potwierdzić.
