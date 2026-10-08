---
url: https://blog.cloudflare.com/pl-pl/threats-lurking-office-365-cloudflare-email-retro-scan/
title: Sprawd\u017a, jakie zagro\u017cenia czaj\u0105 si\u0119 w Twoich skrzynkach pocztowych us\u0142ugi Office 365, korzystaj\u0105c ze skanowania wstecznego w narz\u0119dziu Cloudflare Email Retro Scan | Blog Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:37:01.387028+00:00
---

# Sprawdź, jakie zagrożenia czają się w Twoich skrzynkach pocztowych usługi Office 365, korzystając ze skanowania wstecznego w narzędziu Cloudflare Email Retro Scan | Blog Cloudflare

> Source: https://blog.cloudflare.com/pl-pl/threats-lurking-office-365-cloudflare-email-retro-scan/

[Blog](https://blog.cloudflare.com/pl-pl/)

[Birthday Week](https://blog.cloudflare.com/pl-pl/tag/birthday-week/)

1 tagówPokaż 1 tagów

  * Tagi wpisu
  *   * Wszystkie tagi
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



[Birthday Week](https://blog.cloudflare.com/pl-pl/tag/birthday-week/)

29 września 2023

# Sprawdź, jakie zagrożenia czają się w Twoich skrzynkach pocztowych usługi Office 365, korzystając ze skanowania wstecznego w narzędziu Cloudflare Email Retro Scan

![Ayush Kumar](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW449VZTK4C95VB94E47SS8C.png&w=64&h=64&f=webp&fit=cover&position=center)

[Ayush Kumar](https://blog.cloudflare.com/pl-pl/author/ayush/)

4 min czytania

KOPIUJ URL

Ten wpis jest również dostępny w [English](https://blog.cloudflare.com/threats-lurking-office-365-cloudflare-email-retro-scan/), [Deutsch](https://blog.cloudflare.com/de-de/threats-lurking-office-365-cloudflare-email-retro-scan/), [Español](https://blog.cloudflare.com/es-es/threats-lurking-office-365-cloudflare-email-retro-scan/), [Français](https://blog.cloudflare.com/fr-fr/threats-lurking-office-365-cloudflare-email-retro-scan/), [日本語](https://blog.cloudflare.com/ja-jp/threats-lurking-office-365-cloudflare-email-retro-scan/), [한국어](https://blog.cloudflare.com/ko-kr/threats-lurking-office-365-cloudflare-email-retro-scan/), [繁體中文](https://blog.cloudflare.com/zh-tw/threats-lurking-office-365-cloudflare-email-retro-scan/), [简体中文](https://blog.cloudflare.com/zh-cn/threats-lurking-office-365-cloudflare-email-retro-scan/), [Português](https://blog.cloudflare.com/pt-br/threats-lurking-office-365-cloudflare-email-retro-scan/), [Русский](https://blog.cloudflare.com/ru-ru/threats-lurking-office-365-cloudflare-email-retro-scan/) i [עברית](https://blog.cloudflare.com/he-il/threats-lurking-office-365-cloudflare-email-retro-scan/).

![See what threats are lurking in your Office 365 with Cloudflare Email Retro Scan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44HXTZY6W122ZVDFV058YX.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA//////387vDw4efr4env6e/07/Dy7+3p/////v7/7PH03Ofv2ebz4ev46e717u3s////////7PP62uj11OX42+n95u367e/x////////8Pf/3uz62Oj+3uz/6fD/8fL2////////+f3/6vP/5vH/6/T/8/f/+Pj7////////////+fz/+Pz//f////////3+////////////////////////////////////////////////////////////////)

Informujemy, że klienci Cloudflare mają już możliwość skanowania starych wiadomości w skrzynkach odbiorczych Office 365 pod kątem zagrożeń. Narzędzie Retro Scan do skanowania wstecznego pozwala przyjrzeć się wiadomościom z ostatnich siedmiu dni w celu sprawdzenia, jakie zagrożenia zostały pominięte przez aktualnie używanie narzędzie zabezpieczające pocztę e-mail.

## Dlaczego warto uruchamiać narzędzie Retro Scan?

W rozmowach z klientami często słyszymy, że nie znają stanu skrzynek pocztowych swojej organizacji. Organizacje korzystają z narzędzi do zabezpieczenia poczty e-mail lub z wbudowanych zabezpieczeń firmy Microsoft, ale nie wiedzą, na ile skuteczne są te bieżące rozwiązania. Okazuje się, że używane narzędzia często przepuszczają przez swoje filtry złośliwe wiadomości e-mail, zwiększając w ten sposób ryzyko naruszenia bezpieczeństwa w firmie.

Dążąc do celu, jakim jest wsparcie procesów budowania lepszego Internetu, umożliwiamy klientom Cloudflare bezpłatne korzystanie z narzędzia Retro Scan do wstecznego skanowania wiadomości w skrzynkach odbiorczych w oparciu o zaawansowane modele uczenia maszynowego. Podczas skanowania wstecznego z użyciem narzędzia Retro Scan wyróżniane są wszelkie wykryte zagrożenia, dzięki czemu klienci mogą wyczyścić skrzynki odbiorcze z poziomu swoich kont poczty e-mail. Te informacje pozwalają również klientom wdrożyć dodatkowe środki kontroli oferowane przez Cloudflare lub udostępniane w ramach preferowanego rozwiązania, aby zapobiec pojawianiu się w przyszłości podobnych zagrożeń dotyczących skrzynki pocztowej.

## Uruchamianie narzędzia Retro Scan

Klienci mogą znaleźć opcję uruchomienia narzędzia Retro Scan na pulpicie nawigacyjnym Cloudflare, na karcie Area 1:

Cloudflare potrzebuje autoryzacji, aby uzyskać dostęp do wiadomości przeznaczonych do przeskanowania. W celu uruchomienia tego procesu należy udzielić Cloudflare odpowiednich uprawnień do skanowania wiadomości. Druga autoryzacja zapewni aplikacji Cloudflare dostęp do usługi Active Directory. Jest to niezbędne do zrozumienia przynależności użytkowników do organizacji i grup, co z kolei pomaga naszym algorytmom dokonać lepszej oceny w zakresie tego, czy dana wiadomość jest złośliwa.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2087 Embedded Image - z1Mw1W](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45B0P1WD7XHRVCXSTT5YKK.png&w=715&h=402&f=webp&fit=cover&position=center)

Po udzieleniu wszystkich autoryzacji ostatnim krokiem jest wybranie domen do przeskanowania, a także przekazanie nam informacji o ewentualnych innych dostawcach zabezpieczeń poczty e-mail zapewniających ochronę Twoim skrzynkom odbiorczym.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2087 Embedded Image - Ub1GiP](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47C2WNHKCCAWM6KSJ7117Y.png&w=715&h=501&f=webp&fit=cover&position=center)

Na koniec klienci mogą kliknąć przycisk „Generate Retro Scan” (Generuj skanowanie wsteczne), a narzędzie Cloudflare Area 1 Email Security rozpocznie skanowanie starszych wiadomości. Ten proces jest czasochłonny, dlatego po ukończeniu skanowania klienci otrzymują alert w postaci wiadomości e-mail.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2087 Embedded Image - wp2rvP](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46JFBDCB4HTZ5DK09EC6N7.png&w=715&h=585&f=webp&fit=cover&position=center)

## Analizowanie wyników

Prezentowany jest przegląd zagrożeń wykrytych w ramach skrzynek odbiorczych w organizacji klienta. W górnej sekcji znajduje się podział wykrytych zagrożeń według rodzaju. Można tutaj znaleźć informacje o liczbie wiadomości złośliwych, podejrzanych, oszukańczych, stanowiących spam i masowych. W sekcji phishingowych wiadomości e-mail zaznaczone są także najważniejsze obszary wymagające uwagi. W dowolnym momencie można kliknąć przycisk „Search” (Wyszukaj), aby uzyskać więcej informacji na temat wiadomości e-mail z danymi etykietami.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2087 Embedded Image - tuhT7z](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45DX4AHP4SCPW7VD0YT901.png&w=715&h=659&f=webp&fit=cover&position=center)

The report also showcases the top targeted employees as well as the most common places where threats originate from. All these statistics are meant to provide a better understanding of what is going on within your company inbox.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2087 Embedded Image - 4CE93n](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45K7CD9047JJ6P0YCK7WRA.png&w=715&h=415&f=webp&fit=cover&position=center)

W raporcie prezentowani są także pracownicy stanowiący najczęstszy cel ataków, jak również najbardziej typowe miejsca, z których pochodzą zagrożenia. Dzięki tym statystykom można lepiej zrozumieć, co dzieje się w ramach firmowej skrzynki odbiorczej.

## Jak się zarejestrować

Skanowanie wsteczne jest aktualnie dostępne w formie zamkniętej wersji beta. Osoby zainteresowane uruchomieniem skanowania wstecznego w swoich domenach poczty e-mail Office 365 powinny skontaktować się z firmą Cloudflare, aby zlecić jej dodanie tego narzędzia do swojego konta.

Po uruchomieniu narzędzia Retro Scan i zapoznaniu się z wynikami można wybrać zakup rozwiązania Cloudflare Area 1, aby uniemożliwić przyszłym zagrożeniom przedostanie się do skrzynki odbiorczej, bądź zdecydować się na skonfigurowanie oceny ryzyka phishingu, która jest 30-dniową, bezpłatną wersją próbną produktu Area 1. Retro Scan to doskonałe narzędzie umożliwiające wykrycie istnienia ukrytych zagrożeń, natomiast ocena ryzyka phishingu pozwala uzyskać lepszy przegląd wszystkich narzędzi oferowanych przez nas w celu utrzymania czystości skrzynek pocztowych.

Aby rozpocząć, kliknij przycisk „Request Trial” (Poproś o licencję próbną) u dołu raportu wygenerowanego przez narzędzie Retro Scan i wypełnij odpowiedni formularz, a pracownik Cloudflare skontaktuje się z Tobą (można także skontaktować się bezpośrednio z pracownikiem Cloudflare).

Na tej stronie

Dyskutuj online

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fthreats-lurking-office-365-cloudflare-email-retro-scan%2F&t=Sprawd%C5%BA%2C%20jakie%20zagro%C5%BCenia%20czaj%C4%85%20si%C4%99%20w%20Twoich%20skrzynkach%20pocztowych%20us%C5%82ugi%20Office%20365%2C%20korzystaj%C4%85c%20ze%20skanowania%20wstecznego%20w%20narz%C4%99dziu%20Cloudflare%20Email%20Retro%20Scan)[](https://x.com/intent/post?text=Sprawd%C5%BA%2C+jakie+zagro%C5%BCenia+czaj%C4%85+si%C4%99+w+Twoich+skrzynkach+pocztowych+us%C5%82ugi+Office+365%2C+korzystaj%C4%85c+ze+skanowania+wstecznego+w+narz%C4%99dziu+Cloudflare+Email+Retro+Scan&url=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fthreats-lurking-office-365-cloudflare-email-retro-scan%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fthreats-lurking-office-365-cloudflare-email-retro-scan%2F)[](https://bsky.app/intent/compose?text=Sprawd%C5%BA%2C+jakie+zagro%C5%BCenia+czaj%C4%85+si%C4%99+w+Twoich+skrzynkach+pocztowych+us%C5%82ugi+Office+365%2C+korzystaj%C4%85c+ze+skanowania+wstecznego+w+narz%C4%99dziu+Cloudflare+Email+Retro+Scan+https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fthreats-lurking-office-365-cloudflare-email-retro-scan%2F)[](https://mastodonshare.com/?text=Sprawd%C5%BA%2C+jakie+zagro%C5%BCenia+czaj%C4%85+si%C4%99+w+Twoich+skrzynkach+pocztowych+us%C5%82ugi+Office+365%2C+korzystaj%C4%85c+ze+skanowania+wstecznego+w+narz%C4%99dziu+Cloudflare+Email+Retro+Scan&url=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fthreats-lurking-office-365-cloudflare-email-retro-scan%2F)[](https://www.threads.net/intent/post?text=Sprawd%C5%BA%2C+jakie+zagro%C5%BCenia+czaj%C4%85+si%C4%99+w+Twoich+skrzynkach+pocztowych+us%C5%82ugi+Office+365%2C+korzystaj%C4%85c+ze+skanowania+wstecznego+w+narz%C4%99dziu+Cloudflare+Email+Retro+Scan+https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fthreats-lurking-office-365-cloudflare-email-retro-scan%2F)

## Powiązane tagi

[Birthday Week](https://blog.cloudflare.com/pl-pl/tag/birthday-week/)

Śledź nas w mediach społecznościowych

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Zapisz się, aby otrzymywać powiadomienia o nowych postach

Adres e-mail

Nigdy nie udostępnimy Twojego adresu e-mail.

Subskrybuj

Dziękujemy za subskrypcję! Sprawdź skrzynkę odbiorczą, aby ją potwierdzić.
