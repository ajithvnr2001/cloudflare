---
url: https://blog.cloudflare.com/pl-pl/adaptive-ddos-protection/
title: Przedstawiamy Cloudflare Adaptive DDoS Protection \u2014 nasz nowy system profilowania ruchu w celu \u0142agodzenia atak\u00f3w DDoS | Blog Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:36:24.122347+00:00
---

# Przedstawiamy Cloudflare Adaptive DDoS Protection — nasz nowy system profilowania ruchu w celu łagodzenia ataków DDoS | Blog Cloudflare

> Source: https://blog.cloudflare.com/pl-pl/adaptive-ddos-protection/

[Blog](https://blog.cloudflare.com/pl-pl/)

[Advanced DDoS](https://blog.cloudflare.com/pl-pl/tag/advanced-ddos/)[DDoS](https://blog.cloudflare.com/pl-pl/tag/ddos/)[DDoS Alerts (PL)](https://blog.cloudflare.com/pl-pl/tag/ddos-alerts/)+5Pokaż 5 więcej tagów

8 tagówPokaż 8 tagów

  * Tagi wpisu
  * [DDoS](https://blog.cloudflare.com/pl-pl/tag/ddos/)[DDoS Alerts (PL)](https://blog.cloudflare.com/pl-pl/tag/ddos-alerts/)[Produkty](https://blog.cloudflare.com/pl-pl/tag/product-news/)
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



[GA Week](https://blog.cloudflare.com/pl-pl/tag/ga-week/)[General Availability](https://blog.cloudflare.com/pl-pl/tag/general-availability/)[Magic Transit](https://blog.cloudflare.com/pl-pl/tag/magic-transit/)[Produkty](https://blog.cloudflare.com/pl-pl/tag/product-news/)[Spectrum](https://blog.cloudflare.com/pl-pl/tag/spectrum/)

[Advanced DDoS](https://blog.cloudflare.com/pl-pl/tag/advanced-ddos/)[DDoS](https://blog.cloudflare.com/pl-pl/tag/ddos/)[DDoS Alerts (PL)](https://blog.cloudflare.com/pl-pl/tag/ddos-alerts/)[GA Week](https://blog.cloudflare.com/pl-pl/tag/ga-week/)[General Availability](https://blog.cloudflare.com/pl-pl/tag/general-availability/)[Magic Transit](https://blog.cloudflare.com/pl-pl/tag/magic-transit/)[Produkty](https://blog.cloudflare.com/pl-pl/tag/product-news/)[Spectrum](https://blog.cloudflare.com/pl-pl/tag/spectrum/)

19 września 2022

# Przedstawiamy Cloudflare Adaptive DDoS Protection — nasz nowy system profilowania ruchu w celu łagodzenia ataków DDoS

![Omer Yoachimik](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW485W0MZ0R9VGWD75RQN9ZH.png&w=64&h=64&f=webp&fit=cover&position=center)

[Omer Yoachimik](https://blog.cloudflare.com/pl-pl/author/omer/)

4 min czytania

KOPIUJ URL

Ten wpis jest również dostępny w [English](https://blog.cloudflare.com/adaptive-ddos-protection/), [Español](https://blog.cloudflare.com/es-es/adaptive-ddos-protection/) i [Русский](https://blog.cloudflare.com/ru-ru/adaptive-ddos-protection/).

![Introducing Cloudflare Adaptive DDoS Protection - our new traffic profiling system for mitigating DDoS attacks](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46VQ6MHFZN3NG1P2RF3RZK.png&w=1801&h=1013&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////+/3/8/Xz7+/o8vDo9fPt9PPw7vDu9v3/9Pn/7/Dx7uvk8evi8+/o8vDu7e/v7/n/7vX/7e3x7ujh8ejd8+zk8e/s7e/w7/v/7/f/8O/z8uni9One9u3m9PHv8fL0+v//+f//+Pb5+O/o++/l/fPt+/f19/j5//////////////jx//jw//33///9//7+///////////////5///5///////////////////////////8///9////////////)

Każdy zasób internetowy jest wyjątkowy, ma własne zachowania i wzorce ruchu. Na przykład na stronie internetowej można spodziewać się ruchu użytkowników tylko z określonych obszarów geograficznych, a w danej sieci wyłącznie ograniczonego zestawu protokołów.

Rozumiejąc, że wzorce ruchu każdego zasobu internetowego są inne, opracowaliśmy Adaptive DDoS Protection — system adaptacyjnej ochrony przed DDoS. Adaptive DDoS Protection dołącza do naszego pakietu [zautomatyzowanych zabezpieczeń przed DDoS](https://blog.cloudflare.com/deep-dive-cloudflare-autonomous-edge-ddos-protection/) i wznosi go na wyższy poziom. Nowy system uczy się unikatowych wzorców ruchu i dostosowuje się do nich, zapewniając ochronę przed wyrafinowanymi atakami DDoS.

System Adaptive DDoS Protection jest teraz ogólnie dostępny dla klientów korzystających z planu Enterprise:

  * **HTTP Adaptive DDoS Protection —** dostępny dla klientów WAF/CDN korzystających z planu Enterprise, którzy mają również subskrypcję usługi Adaptive DDoS Protection.
  * **L3/4 Adaptive DDoS Protection —** dostępny dla klientów Magic Transit i Spectrum korzystających z planu Enterprise.



### Adaptive DDoS Protection uczy się Twoich wzorców ruchu

System Adaptive DDoS Protection tworzy profil ruchu na podstawie maksymalnej prędkości ruchu klienta każdego z ostatnich siedmiu dni. Profile są codziennie kalkulowane na nowo na podstawie historii z ostatniego tygodnia. Następnie przechowujemy maksymalne prędkości ruchu odnotowane dla każdej wstępnie zdefiniowanej wartości wymiaru. Każdy profil wykorzystuje jeden wymiar. Wymiary stanowią kraj źródłowy żądania, kraj centrum danych Cloudflare, które otrzymało pakiet IP, agent użytkownika, protokół IP, port docelowy i nie tylko.

Przykładowo w [profilu, którego wymiarem jest kraj źródłowy](https://blog.cloudflare.com/location-aware-ddos-protection/), system odnotuje maksymalne prędkości ruchu z danego kraju, np. 2000 żądań na sekundę (RPS) z Niemiec, 3000 RPS z Francji, 10 000 RPS z Brazylii itd. Ten przykład dotyczy ruchu HTTP, ale Adaptive DDoS Protection profiluje też ruch L3/4 dla naszych klientów korzystających z Magic Transit i Spectrum z planem Enterprise.

Przy wyliczaniu prędkości maksymalnych bierzemy pod uwagę percentyl 95. Oznacza to, że odnotowujemy wszystkie prędkości maksymalne i odrzucamy najwyższe 5%. Ma to na celu wykluczenie z kalkulacji wartości skrajnie wysokich.

Kalkulowanie profili ruchu jest przeprowadzane asynchronicznie, co oznacza, że nie powoduje opóźnień w ruchu naszych klientów. Następnie system rozprasza kompaktową reprezentację profilu po naszej sieci, gdzie konsumują ją nasze systemy ochrony przed DDoS w celu wykrywania i łagodzenia ataków DDoS w bardziej ekonomiczny sposób.

Oprócz profili ruchu system Adaptive DDoS Protection wykorzystuje także generowane prez [uczenie maszynowe](https://developers.cloudflare.com/bots/concepts/bot-score/#machine-learning) [wskaźniki prawdopodobieństwa, że żądanie pochodzi od bota](https://developers.cloudflare.com/bots/concepts/bot-score/), jako dodatkowy sygnał pozwalający rozróżnić zautomatyzowany ruch od ruchu użytkowników. Ma to na celu rozróżnienie między faktycznym wzrostem ruchu użytkowników, który odbiega od profilu, a wzrostem zautomatyzowanego i potencjalnie złośliwego ruchu.

### Gotowy do działania i łatwy w użyciu

System Adaptive DDoS Protection działa od razu i automatycznie tworzy profile, a klienci mogą później modyfikować ustawienia według potrzeb za pośrednictwem [zarządzanych reguł DDoS](https://developers.cloudflare.com/ddos-protection/managed-rulesets/). Klienci mogą zmienić poziom wrażliwości, wykorzystać pola wyrażenia do tworzenia zastąpień (np. wykluczenia _tego_ typu ruchu) i zmienić działanie łagodzące, by dostosować zachowanie systemu do własnych potrzeb i wzorców ruchu.

Adaptive DDoS Protection dopełnia istniejący system ochrony przed atakami DDoS, który wykorzystuje dynamiczne tworzenie odcisków cyfrowych do wykrywania i łagodzenia ataków DDoS. Systemy współpracują w celu zapewnienia naszym klientom ochrony przed atakami DDoS. Kiedy klienci dodają nowy zasób do Cloudflare, dynamiczne tworzenie odcisków cyfrowych chroni ich automatycznie, nie wymagając żadnych działań użytkownika. Gdy system Adaptive DDoS Protection nauczy się wzorców ruchu użytkowników i utworzy profil, klienci mogą go włączyć w celu zapewnienia dodatkowej warstwy ochrony.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![A screenshot of Cloudflare Adaptive DDoS Protection rules](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW488BDSTA1SXG8JJ4ADJJQ4.png&w=715&h=474&f=webp&fit=cover&position=center)

### Reguły zawarte w systemie Adaptive DDoS Protection

Mamy przyjemność ogłosić, że obecna wersja systemu Adaptive DDoS Protection Cloudflare zawiera następujące funkcje:

Wymiar profilowania | Dostępność  
---|---  
Klienci WAF/CDN na planie Enterprise z zaawansowaną ochroną przed DDoS | Klienci Magic Transit i Spectrum na planie Enterprise  
Błędy źródła | ✅ | ❌  
Kraj i region adresu IP klienta | ✅ | Wkrótce  
Agent użytkownika (globalnie, nie na klienta*) | ✅ | ❌  
Protokół IP | ❌ | ✅  
Połączenie protokołu IP i portu docelowego | ❌ | Wkrótce  
  
*Funkcja rozpoznająca agenta użytkownika analizuje, uczy się i profiluje wszystkich najważniejszych agentów użytkowników, jakich widzimy w sieci Cloudflare. Ta funkcja pomaga nam wykrywać ataki DDoS wykorzystujące starszych lub niepoprawnie skonfigurowanych agentów użytkownika.

Za wyjątkiem ochrony przed DDoS rozpoznającej agenta użytkownika wszystkie reguły systemu Adaptive DDoS Protection są wdrażane w trybie dziennika. Klienci mogą obserwować oflagowany ruch, w razie konieczności zmienić wrażliwość i wdrożyć reguły w trybie łagodzenia ryzyka. Szczegółowe instrukcje znajdują się w [tym przewodniku](https://developers.cloudflare.com/ddos-protection/managed-rulesets/adjust-rules/false-positive/).

### Ryzyko ataków DDoS przejdzie do historii

Misją Cloudflare jest pomóc budować lepszy Internet. Na tej podstawie powstała wizja zespołu odpowiedzialnego za ochronę przed DDoS — chcemy sprawić, by ryzyko ataków DDoS przeszło do historii. System Adaptive DDoS Protection Cloudflare przybliża nas o jeden krok do realizacji tej wizji. Sprawia, że nasza ochrona przed DDoS jest jeszcze bardziej inteligentna, wyrafinowana i dostosowana do unikatowych wzorców ruchu oraz potrzeb naszych klientów.

Chcesz dowiedzieć się więcej o systemie Adaptive DDoS Protection Cloudflare? Odwiedź naszą [witrynę dewelopera](https://developers.cloudflare.com/ddos-protection/managed-rulesets/adaptive-protection/).

Chcesz przejść z obecnego systemu na Adaptive DDoS Protection? Skontaktuj się z zespołem opiekującym się Twoim kontem.

Nie jesteś jeszcze klientem Cloudflare? [Porozmawiaj z jednym z naszych ekspertów](https://www.cloudflare.com/plans/enterprise/discover/contact/).

### Obejrzyj na Cloudflare TV

Na tej stronie

Dyskutuj online

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fadaptive-ddos-protection%2F&t=Przedstawiamy%20Cloudflare%20Adaptive%20DDoS%20Protection%20%E2%80%94%20nasz%20nowy%20system%20profilowania%20ruchu%20w%20celu%20%C5%82agodzenia%20atak%C3%B3w%20DDoS)[](https://x.com/intent/post?text=Przedstawiamy+Cloudflare+Adaptive+DDoS+Protection+%E2%80%94+nasz+nowy+system+profilowania+ruchu+w+celu+%C5%82agodzenia+atak%C3%B3w+DDoS&url=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fadaptive-ddos-protection%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fadaptive-ddos-protection%2F)[](https://bsky.app/intent/compose?text=Przedstawiamy+Cloudflare+Adaptive+DDoS+Protection+%E2%80%94+nasz+nowy+system+profilowania+ruchu+w+celu+%C5%82agodzenia+atak%C3%B3w+DDoS+https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fadaptive-ddos-protection%2F)[](https://mastodonshare.com/?text=Przedstawiamy+Cloudflare+Adaptive+DDoS+Protection+%E2%80%94+nasz+nowy+system+profilowania+ruchu+w+celu+%C5%82agodzenia+atak%C3%B3w+DDoS&url=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fadaptive-ddos-protection%2F)[](https://www.threads.net/intent/post?text=Przedstawiamy+Cloudflare+Adaptive+DDoS+Protection+%E2%80%94+nasz+nowy+system+profilowania+ruchu+w+celu+%C5%82agodzenia+atak%C3%B3w+DDoS+https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fadaptive-ddos-protection%2F)

## Powiązane tagi

[Advanced DDoS](https://blog.cloudflare.com/pl-pl/tag/advanced-ddos/)[DDoS](https://blog.cloudflare.com/pl-pl/tag/ddos/)[DDoS Alerts (PL)](https://blog.cloudflare.com/pl-pl/tag/ddos-alerts/)[GA Week](https://blog.cloudflare.com/pl-pl/tag/ga-week/)[General Availability](https://blog.cloudflare.com/pl-pl/tag/general-availability/)[Magic Transit](https://blog.cloudflare.com/pl-pl/tag/magic-transit/)[Produkty](https://blog.cloudflare.com/pl-pl/tag/product-news/)[Spectrum](https://blog.cloudflare.com/pl-pl/tag/spectrum/)

Śledź nas w mediach społecznościowych

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Zapisz się, aby otrzymywać powiadomienia o nowych postach

Adres e-mail

Nigdy nie udostępnimy Twojego adresu e-mail.

Subskrybuj

Dziękujemy za subskrypcję! Sprawdź skrzynkę odbiorczą, aby ją potwierdzić.
