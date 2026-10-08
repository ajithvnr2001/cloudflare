---
url: https://blog.cloudflare.com/pl-pl/replace-your-email-gateway-with-area-1/
title: Jak zast\u0105pi\u0107 bram\u0119 poczty elektronicznej rozwi\u0105zaniem Cloudflare Area 1 | Blog Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:42:42.691217+00:00
---

# Jak zastąpić bramę poczty elektronicznej rozwiązaniem Cloudflare Area 1 | Blog Cloudflare

> Source: https://blog.cloudflare.com/pl-pl/replace-your-email-gateway-with-area-1/

[Blog](https://blog.cloudflare.com/pl-pl/)

[Bezpieczeństwo](https://blog.cloudflare.com/pl-pl/tag/security/)[Cloud Email Security](https://blog.cloudflare.com/pl-pl/tag/cloud-email-security/)[Cloudflare One Week](https://blog.cloudflare.com/pl-pl/tag/cloudflare-one-week/)+4Pokaż 4 więcej tagów

7 tagówPokaż 7 tagów

  * Tagi wpisu
  * [Bezpieczeństwo](https://blog.cloudflare.com/pl-pl/tag/security/)[Zero Trust](https://blog.cloudflare.com/pl-pl/tag/zero-trust/)
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



[Cloudflare Zero Trust](https://blog.cloudflare.com/pl-pl/tag/cloudflare-zero-trust/)[Email Security](https://blog.cloudflare.com/pl-pl/tag/email-security/)[Phishing](https://blog.cloudflare.com/pl-pl/tag/phishing/)[Zero Trust](https://blog.cloudflare.com/pl-pl/tag/zero-trust/)

[Bezpieczeństwo](https://blog.cloudflare.com/pl-pl/tag/security/)[Cloud Email Security](https://blog.cloudflare.com/pl-pl/tag/cloud-email-security/)[Cloudflare One Week](https://blog.cloudflare.com/pl-pl/tag/cloudflare-one-week/)[Cloudflare Zero Trust](https://blog.cloudflare.com/pl-pl/tag/cloudflare-zero-trust/)[Email Security](https://blog.cloudflare.com/pl-pl/tag/email-security/)[Phishing](https://blog.cloudflare.com/pl-pl/tag/phishing/)[Zero Trust](https://blog.cloudflare.com/pl-pl/tag/zero-trust/)

20 czerwca 2022

# Jak zastąpić bramę poczty elektronicznej rozwiązaniem Cloudflare Area 1

![Shalabh Mohan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW491RFMJARF117EF2268NPG.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Tarika Srinivasan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47RDAN04NY6SWQ4F3NCWQ3.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Shalabh Mohan](https://blog.cloudflare.com/pl-pl/author/shalabh/) i [Tarika Srinivasan](https://blog.cloudflare.com/pl-pl/author/tarika/)

10 min czytania

KOPIUJ URL

Ten wpis jest również dostępny w [English](https://blog.cloudflare.com/replace-your-email-gateway-with-area-1/), [Español](https://blog.cloudflare.com/es-es/replace-your-email-gateway-with-area-1/), [日本語](https://blog.cloudflare.com/ja-jp/replace-your-email-gateway-with-area-1/), [한국어](https://blog.cloudflare.com/ko-kr/replace-your-email-gateway-with-area-1/), [简体中文](https://blog.cloudflare.com/zh-cn/replace-your-email-gateway-with-area-1/), [Русский](https://blog.cloudflare.com/ru-ru/replace-your-email-gateway-with-area-1/) i [Svenska](https://blog.cloudflare.com/sv-se/replace-your-email-gateway-with-area-1/).

![How to replace your email gateway with Cloudflare Area 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48MP9PWCM9EYY08KRM8GEW.png&w=1800&h=1013&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/vnn+fTi7urY6eTR7ebT8unY7+jY5uLT//vp+/bk8OrY6+PR7uTS8+jX8ejY6ePV//7s//jn8+za7ePR8OPR9ejW9OnZ7ObY///w//3q+PDe8ebV9ObU+erZ+O3c8evc///z///u/fbk9u3b+e3a/vHe/PLg9fDh///2///y//zq/PTj//Xi//jk//nl+fbl///4///1///u//vp//vo///p//7p/Prn///4///2///w//3r//7q///q///q/fvo)

Liderzy i praktycy odpowiedzialni za bezpieczeństwo poczty elektronicznej codziennie mają do czynienia z kilkoma faktami. Pierwszym jest to, że ich poczta elektroniczna jest prawdopodobnie dostarczana w chmurze i ma wbudowane zabezpieczenia, które jako tako radzą sobie z blokowaniem spamu i standardowego złośliwego oprogramowania. Prawdopodobnie także poświęcili sporo czasu i pieniędzy oraz zatrudnili personel w celu konfiguracji bezpiecznej bramy poczty elektronicznej (SEG), by bronić się przed phishingiem, złośliwym oprogramowaniem i innymi zagrożeniami, które mogą nieść z sobą e‑maile. Mimo to poczta elektroniczna nadal jest najczęstszym źródłem zagrożeń w Internecie — według badań firmy Deloitte aż 91% wszystkich cyberataków zaczyna się od phishingu.

Skoro usługi antyphishingowe i SEG istnieją od tak dawna, dlaczego nadal otrzymujemy tyle wiadomości phishingowych? Miłośnicy zasady [brzytwy Ockhama](https://pl.wikipedia.org/wiki/Brzytwa_Ockhama) powiedzą, że bramy poczty elektronicznej nie zaprojektowano do ochrony dzisiejszych środowisk poczty e‑mail i nie jest ona skutecznym sposobem powstrzymywania współczesnych ataków phishingowych.

Jeśli jednak szukasz lepszego wyjaśnienia, czytaj dalej.

### Dlaczego świat odszedł od SEG

Najważniejsza zmiana na rynku poczty e‑mail jest również czynnikiem, przez który brama poczty elektronicznej stała się zbędna — przejście do usług pocztowych natywnych dla chmury. [Gartner® przewiduje](https://www.gartner.com/en/newsroom/press-releases/2021-11-10-gartner-says-cloud-will-be-the-centerpiece-of-new-digital-experiences), że do 2025 roku ponad 85% organizacji będzie korzystać przede wszystkim z rozwiązań w chmurze. Organizacje, które oczekują od swoich zabezpieczeń skali, wytrzymałości i elastyczności stosownych do tej strategii, nie znajdą ich w starszych urządzeniach takich jak SEG.

Jeśli chodzi konkretnie o pocztę e‑mail, [Gartner® stwierdza](https://www.gartner.com/document/4006566), że zaawansowane zabezpieczenia poczty elektronicznej są coraz częściej wdrażane jako zintegrowane rozwiązania w chmurze, a nie jako bramy. Do roku 2023 co najmniej 40% organizacji ma korzystać z wbudowanych zabezpieczeń dostarczanych przez dostawców poczty w chmurze zamiast SEG. Dziś e‑maile przychodzą z najróżniejszych miejsc i trafiają w różne miejsca — ustawianie bramy przed serwerem Exchange jest więc anachronizmem, a ustawianie jej przed skrzynkami odbiorczymi w chmurze w mobilnym, zdalnym świecie jest niepraktyczne i uciążliwe. [Zabezpieczenia poczty e‑mail](https://www.cloudflare.com/learning/email-security/what-is-email-security/) w dzisiejszym świcie powinny być tam, gdzie użytkownik, blisko skrzynki odbiorczej i po prostu wszędzie.

SEG oprócz tego, że wykorzystuje przestarzałą architekturę, nie sprawdza się także w wykrywaniu zaawansowanych ataków phishingowych i tych wykorzystujących inżynierię społeczną. To dlatego, że SEG zaprojektowano w celu blokowania spamu — ogromnej liczby e‑maili, do których wykrycia i unieszkodliwienia potrzeba również sporej próby ataków. Natomiast dzisiejsze ataki phishingowe są bardziej jak strzały snajperskie niż strzał śrutem ze strzelby. Używają stosunkowo niewielu e‑maili, które są kierowane do konkretnych osób, i wykorzystują zaufanie, jakie mamy do poczty e‑mail, w celu kradzieży pieniędzy i danych. Do identyfikacji nowoczesnych ataków phishingowych konieczne są zaawansowana analiza wiadomości e‑mail i algorytmy wykrywania zagrożeń, które wymagają ogromnej mocy obliczeniowej i których SEG nie może zapewnić na większą skalę.

Przestarzałą filozofię wykrywania zagrożeń SEG najlepiej obrazuje uciążliwe zadanie administratorów, jakim jest tworzenie i dostosowywanie całej góry zasad. W przeciwieństwie do większości innych cyberataków phishing i [naruszenia bezpieczeństwa służbowej poczty e‑mail (BEC)](https://www.cloudflare.com/learning/email-security/business-email-compromise-bec/) mają zbyt wiele „rozmytych” sygnałów, przez co nie można ich wykryć, korzystając z deterministycznych zasad typu „jeżeli… to”. Co więcej, cyberprzestępcy nie czekają, aż stworzysz nowe zasady poczty — szybko się dostosowują i zmieniają swoje techniki, by obejść stworzone przez Ciebie reguły. Powierzenie SEG obrony przed phishingiem jest więc jak zabawa w kotka i myszkę.

### By powstrzymać phishing, trzeba patrzeć w przyszłość

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1155 Embedded Image - lnOHVY](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49AHBZ8WE55RJQTHW1N55Y.png&w=715&h=745&f=webp&fit=cover&position=center)

Tradycyjne zabezpieczenia poczty e‑mail wykrywają nowe ataki na podstawie znajomości charakterystyk poprzednich ataków, takich jak dane o reputacji i sygnatury zagrożeń, a więc nie są w stanie skutecznie chronić przed nowoczesnymi atakami phishingowymi, które są stale doskonalone.

Konieczna jest przyszłościowa technologia, która nie tylko rozpoznaje ładunki, strony internetowe i techniki wykorzystywane w poprzednich atakach, ale i potrafi przewidzieć następne kroki cyberprzestępców. Które strony i konta chcą zaatakować lub wykorzystać w kolejnym ataku? Jakie przygotowują ładunki i techniki? Co sondują przed atakiem?

Cloudflare Area 1 proaktywnie skanuje Internet w poszukiwaniu infrastruktury źródeł zagrożeń i przygotowywanych kampanii phishingowych. Skupiające się na zagrożeniach przeszukiwarki Area 1 dynamicznie analizują podejrzane strony internetowe i ładunki wraz z rozwojem taktyk sprawców stale uaktualniają modele wykrywania — wszystko to, by powstrzymać ataki phishingowe na długo, zanim dotrą do skrzynki odbiorczej.

W połączeniu z ponad bilionem żądań DNS wykrywanych przez [Cloudflare Gateway](https://www.cloudflare.com/products/zero-trust/gateway/) każdego dnia, ta baza informacji na temat zagrożeń pozwala klientom zatrzymywać zagrożenia phishingowe na możliwie najwcześniejszym etapie cyklu ataku. Dodatkowo zastosowanie głębokiej analizy kontekstowej tych danych w celu zrozumienia tonu, wydźwięku, ogólnego znaczenia wiadomości i różnic w wątkach pozwala Area 1 zrozumieć i rozróżnić prawdziwe wiadomości związane z procesami biznesowymi od naśladujących je wyrafinowanych kampanii phishingowych.

Choć jesteśmy zwolennikami nakładania dopełniających się warstw zabezpieczeń, żadna z warstw nie powinna być zbędna. SEG duplikuje wiele funkcji, które obecnie są dostarczane klientom razem z pocztą w chmurze. Natomiast Area 1 rozszerza — a nie duplikuje — natywne zabezpieczenia i zatrzymuje ataki phishingowe, które przedostają się przez pierwszą warstwę ochrony.

### Planowanie projektu zastąpienia SEG

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1155 Embedded Image - dVe4kK](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49N17T976H10Q30BXGMNJ8.png&w=715&h=493&f=webp&fit=cover&position=center)

Najlepiej rozpocząć projekt zastąpienia SEG od decyzji, czy ma to być bezpośrednia zamiana, czy rozszerzenie, które z czasem zastąpi obecne rozwiązanie. Cloudflare Area 1 ma wielu klientów, którzy od razu zastąpili swoją bramę poczty elektronicznej naszym rozwiązaniem (więcej na ten temat poniżej), jednak widzieliśmy też scenariusze, w przypadku których klienci woleli na początek wdrożyć Cloudflare Area 1 za bramą, ocenić skuteczność obu usług, a potem podjąć ostateczną decyzję. W obu przypadkach proces jest bardzo prosty!

Na początku projektu należy zaangażować odpowiednich interesariuszy. Potrzebny będzie przede wszystkim administrator IT, który dopilnuje, by nie ucierpiały dostarczanie poczty i produktywność, oraz by był administrator zabezpieczeń, monitorujący skuteczność wykrywania zagrożeń. Warto także zaangażować partnera handlowego, jeśli to Twój preferowany proces zaopatrzenia oraz kogoś z zespołu ds. prywatności i zgodności, kto zweryfikuje sposób obsługi danych.

Następny krok to wybór preferowanej architektury wdrożenia Cloudflare Area 1. Cloudflare Area 1 można wdrożyć jako rekord MX, przez interfejsy API, a nawet łącząc różne tryby. Zalecamy wdrożenie Cloudflare Area 1 jako rekordu MX w celu uzyskania najskuteczniejszej ochrony przeciw zewnętrznym zagrożeniom, jednak nasza usługa dopasowuje się do świata klienta wraz z jego własną logiką biznesową i indywidualnymi potrzebami.

Ostatni element przygotowań to mapowanie przepływu wiadomości e‑mail. Jeśli Twoja organizacja ma kilka domen, należy ustalić, dokąd przekierowywane są wiadomości z każdej z nich. Sprawdź poszczególne warstwy routingu (np. czy są serwery poczty elektronicznej przekazujące wiadomości przychodzące). Zrozumienie logicznych i fizycznych warstw SMTP wewnątrz organizacji zagwarantuje odpowiednie przekierowywanie wiadomości. Zdecyduj, jaki typ ruchu Cloudflare Area 1 ma skanować (północ‑południe, wschód‑zachód czy oba) oraz jak ma współgrać z istniejącymi zasadami poczty e‑mail.

### Realizacja planu zamiany

**Etap 1: implementacja ochrony poczty e‑mail**

Oto przybliżony zarys kolejnych kroków, jeśli Cloudflare Area 1 jest konfigurowane jako rekord MX (szacowany czas: ok. 30 minut):

  * Skonfiguruj usługę podrzędną, by przyjmowała pocztę e‑mail z Cloudflare Area 1.
  * Upewnij się, że adresy IP ruchu wychodzącego Cloudflare Area 1 nie są blokowane ani poddawane ograniczeniom przepustowości — to wpłynęłoby na dostarczanie wiadomości.
  * W przypadku lokalnego serwera poczty e‑mail zaktualizuj reguły zapory, by zezwalały Cloudflare Area 1 na dostarczanie wiadomości do tych systemów.
  * Skonfiguruj reguły naprawcze (np. kwarantanna, dodanie prefiksu tematu lub treści wiadomości itp.).
  * Przetestuj przepływ wiadomości poprzez iniekcję wiadomości do Cloudflare Area 1, by potwierdzić ich poprawne dostarczenie (nasz zespół może w tym pomóc).
  * Zaktualizuj rekordy MX, by wskazywały Cloudflare Area 1.



Oto przybliżony zarys kolejnych kroków, jeśli Cloudflare Area 1 jest konfigurowane poniżej istniejącego rozwiązania zabezpieczającego pocztę e‑mail (szacowany czas: ok. 30 minut):

  * Skonfiguruj odpowiednie przeskoki w Cloudflare Area 1, by umożliwić wykrywanie adresu IP oryginalnego nadawcy.
  * W przypadku lokalnego serwera poczty e‑mail zaktualizuj reguły zapory, by zezwalały Cloudflare Area 1 na dostarczanie wiadomości do serwera.
  * Skonfiguruj reguły naprawcze (np. kwarantanna, dodanie prefiksu tematu lub treści wiadomości itp.).
  * Przetestuj przepływ wiadomości poprzez iniekcję wiadomości do Cloudflare Area 1, by potwierdzić ich poprawne dostarczenie (nasz zespół może w tym pomóc).
  * Zaktualizuj trasy poczty w bramie poczty elektronicznej, by cała poczta była dostarczana do Cloudflare Area 1 zamiast do serwerów poczty e‑mail.



**Etap 2: integracja DNS** Jednym z najczęstszych kroków po konfiguracji poczty e‑mail jest integracja Cloudflare Area 1 z usługą DNS. Jeśli korzystasz już z Cloudflare Gateway, mamy dobrą wiadomość — Cloudflare Area 1 wykorzystuje teraz Cloudflare Gateway jako [cykliczny DNS](https://www.cloudflare.com/learning/dns/what-is-recursive-dns/) w celu ochrony użytkowników końcowych przed dostępem do złośliwych i phishingowych stron przez linki w wiadomościach lub podczas przeglądania Internetu.

**Etap 3: integracja z usługami podrzędnymi monitorowania i naprawy** Szczegółowe i konfigurowalne raportowanie Cloudflare Area 1 pozwala na szybki wgląd w zagrożenia. Integracja z systemami SIEM przez nasze niezawodne interfejsy API umożliwia bezproblemową korelację wykryć Cloudflare Area 1 z wydarzeniami z narzędzi ochrony sieci, punktów końcowych i innych, co upraszcza zarządzanie incydentami.

Cloudflare Area 1 zapewnia wbudowane funkcje naprawy i wycofywania wiadomości, dzięki czemu klienci mogą reagować na zagrożenia bezpośrednio z pulpitu nawigacyjnego Cloudflare Area 1. Jednak wiele organizacji decyduje się także na integrację z narzędziami do orkiestracji, co pozwala na tworzenie zindywidualizowanych podręczników reagowania. Wielu klientów wykorzystuje punkty zaczepienia naszych interfejsów API do integracji z usługami SOAR, by zarządzać procesami reagowania w całej organizacji.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1155 Embedded Image - StP8R8](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4874W3FP54E9361FM0MB0R.png&w=715&h=298&f=webp&fit=cover&position=center)

### Wskaźniki sukcesu

Skąd wiedzieć, czy projekt zastąpienia bezpiecznej bramy poczty elektronicznej się powiódł i miał pożądany efekt? Zalecamy wskaźniki pomiaru dotyczące zarówno skuteczności wykrywania, jak i prostoty obsługi.

Pod względem wykrywania oczywistym wskaźnikiem będzie liczba i rodzaj zablokowanych ataków phishingowych przed zmianą oraz po niej. Czy blokowane są nowe rodzaje ataków phishingowych, które nie pojawiały się we wcześniejszych raportach? Czy widzisz kampanie, które atakują wiele skrzynek odbiorczych? Ważna jest również liczba wyników fałszywie dodatnich.

Pod względem obsługi niezwykle istotne jest to, by nie spadła produktywność. Powinna to odzwierciedlać liczba zgłoszeń IT związanych z dostarczaniem poczty e‑mail. Kolejny ważny wskaźnik to dostępność i czas pracy usługi ochrony poczty e‑mail.

Ostatnim i, być może, najważniejszym czynnikiem jest czas, jaki zespół ds. bezpieczeństwa poświęca ochronie poczty e‑mail. Mamy nadzieję, że jest go znacznie mniej niż poprzednio! Bezpieczna brama poczty elektronicznej jest uważana za czasochłonną usługę, od wdrożenia poprzez obsługę. Jeśli Cloudflare Area 1 może zaoszczędzić Twojemu zespołowi czas, pozwalając mu skupić się na innych ważnych aspektach bezpieczeństwa, jest to równie ważne jak zatrzymanie ataków phishingowych.

### Masz liczne towarzystwo

Przedstawiamy ten plan zastąpienia bezpiecznej bramy poczty elektronicznej dlatego, że wielu naszych klientów już podjęło ten krok i są oni bardzo zadowoleni z rezultatów.

Na przykład jedna z 50 największych amerykańskich firm, która dostarcza ubezpieczenia 90 milionom klientów z ponad 60 krajów, uznała, że jej rozwiązanie SEG nie jest skuteczne w zatrzymywaniu ataków phishingowych. Szczególnie problematyczne było pracochłonne i uciążliwe wyszukiwanie ataków, które przedostały się przez zabezpieczenia i dotarły do skrzynki odbiorczej. Ta firma potrzebowała usługi ochrony poczty e‑mail, która wyłapałaby wszystkie te ataki i obsługiwała architekturę hybrydową ze skrzynkami odbiorczymi lokalnymi oraz w chmurze.

Po wdrożeniu Cloudflare Area 1 podrzędnie do warstw Microsoft 365 i bezpiecznej bramy poczty elektronicznej nasz klient uniknął ponad 14 000 zagrożeń phishingowych tylko w ciągu pierwszego miesiąca; żadna z tych wiadomości nie dotarła do skrzynki odbiorczej użytkownika. Integracja w jednym kroku z istniejącą infrastrukturą pocztową ograniczyła problemy z obsługą prawie do zera. Wbudowany w Cloudflare Area 1 zautomatyzowany system wycofywania i ochrony po dostarczeniu wiadomości pozwolił także wyszukać pominięte ataki i zastosować procesy naprawcze.

Jeśli chcesz dowiedzieć się więcej bezpośrednio od naszych klientów, którzy wykorzystali Cloudflare Area 1 do wzmocnienia lub zastąpienia dotychczasowego rozwiązania SEG, skontaktuj się z zespołem opiekującym się Twoim kontem. Jeśli chcesz zobaczyć Cloudflare Area 1 w akcji, poproś o ocenę ryzyka phishingu [tutaj](https://www.cloudflare.com/lp/emailsecurity/).

Zastąpienie bezpiecznej bramy poczty elektronicznej to świetne przedsięwzięcie na [drodze do modelu Zero Trust](https://zerotrustroadmap.org/). Aby zapoznać się z podsumowaniem tygodnia Cloudflare One i wszystkich nowości, obejrzyj nasze [webinarium podsumowujące](https://gateway.on24.com/wcc/eh/2153307/lp/3824611/the-evolution-of-cloudflare-one).

1Komunikat prasowy Gartner, „[Gartner Says Cloud Will Be the Centerpiece of New Digital Experiences](https://www.gartner.com/en/newsroom/press-releases/2021-11-10-gartner-says-cloud-will-be-the-centerpiece-of-new-digital-experiences)”, 11 listopada 2021 r.2Gartner, „Market Guide for Email Security”, 7 października 2021 r., Mark Harris, Peter Firstbrook, Ravisha Chugh, Mario de Boer.GARTNER jest zarejestrowanym znakiem towarowym i znakiem usługowym firmy Gartner, Inc. i/lub jej spółek zależnych w Stanach Zjednoczonych i na całym świecie i jest używana w niniejszym dokumencie za zgodą. Wszelkie prawa zastrzeżone.

Na tej stronie

Dyskutuj online

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Freplace-your-email-gateway-with-area-1%2F&t=Jak%20zast%C4%85pi%C4%87%20bram%C4%99%20poczty%20elektronicznej%20rozwi%C4%85zaniem%20Cloudflare%20Area%201)[](https://x.com/intent/post?text=Jak+zast%C4%85pi%C4%87+bram%C4%99+poczty+elektronicznej+rozwi%C4%85zaniem+Cloudflare+Area+1&url=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Freplace-your-email-gateway-with-area-1%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Freplace-your-email-gateway-with-area-1%2F)[](https://bsky.app/intent/compose?text=Jak+zast%C4%85pi%C4%87+bram%C4%99+poczty+elektronicznej+rozwi%C4%85zaniem+Cloudflare+Area+1+https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Freplace-your-email-gateway-with-area-1%2F)[](https://mastodonshare.com/?text=Jak+zast%C4%85pi%C4%87+bram%C4%99+poczty+elektronicznej+rozwi%C4%85zaniem+Cloudflare+Area+1&url=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Freplace-your-email-gateway-with-area-1%2F)[](https://www.threads.net/intent/post?text=Jak+zast%C4%85pi%C4%87+bram%C4%99+poczty+elektronicznej+rozwi%C4%85zaniem+Cloudflare+Area+1+https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Freplace-your-email-gateway-with-area-1%2F)

## Powiązane tagi

[Bezpieczeństwo](https://blog.cloudflare.com/pl-pl/tag/security/)[Cloud Email Security](https://blog.cloudflare.com/pl-pl/tag/cloud-email-security/)[Cloudflare One Week](https://blog.cloudflare.com/pl-pl/tag/cloudflare-one-week/)[Cloudflare Zero Trust](https://blog.cloudflare.com/pl-pl/tag/cloudflare-zero-trust/)[Email Security](https://blog.cloudflare.com/pl-pl/tag/email-security/)[Phishing](https://blog.cloudflare.com/pl-pl/tag/phishing/)[Zero Trust](https://blog.cloudflare.com/pl-pl/tag/zero-trust/)

Śledź nas w mediach społecznościowych

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Zapisz się, aby otrzymywać powiadomienia o nowych postach

Adres e-mail

Nigdy nie udostępnimy Twojego adresu e-mail.

Subskrybuj

Dziękujemy za subskrypcję! Sprawdź skrzynkę odbiorczą, aby ją potwierdzić.
