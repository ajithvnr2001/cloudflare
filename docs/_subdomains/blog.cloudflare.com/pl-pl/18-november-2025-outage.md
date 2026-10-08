---
url: https://blog.cloudflare.com/pl-pl/18-november-2025-outage/
title: Awaria Cloudflare z 18 listopada 2025\u00a0r. | Blog Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:36:34.678448+00:00
---

# Awaria Cloudflare z 18 listopada 2025 r. | Blog Cloudflare

> Source: https://blog.cloudflare.com/pl-pl/18-november-2025-outage/

[Blog](https://blog.cloudflare.com/pl-pl/)

[Analiza przypadku](https://blog.cloudflare.com/pl-pl/tag/post-mortem/)[Awaria](https://blog.cloudflare.com/pl-pl/tag/outage/)[Zarządzanie ruchem botów](https://blog.cloudflare.com/pl-pl/tag/bot-management/)

3 tagówPokaż 3 tagów

  * Tagi wpisu
  * [Analiza przypadku](https://blog.cloudflare.com/pl-pl/tag/post-mortem/)[Awaria](https://blog.cloudflare.com/pl-pl/tag/outage/)[Zarządzanie ruchem botów](https://blog.cloudflare.com/pl-pl/tag/bot-management/)
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



[Analiza przypadku](https://blog.cloudflare.com/pl-pl/tag/post-mortem/)[Awaria](https://blog.cloudflare.com/pl-pl/tag/outage/)[Zarządzanie ruchem botów](https://blog.cloudflare.com/pl-pl/tag/bot-management/)

18 listopada 2025

# Awaria Cloudflare z 18 listopada 2025 r.

![Matthew Prince](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44KQ4Z9PY1TR0ERGW96HZR.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Matthew Prince](https://blog.cloudflare.com/pl-pl/author/matthew-prince/)

12 min czytania

KOPIUJ URL

Ten wpis jest również dostępny w [English](https://blog.cloudflare.com/18-november-2025-outage/), [Deutsch](https://blog.cloudflare.com/de-de/18-november-2025-outage/), [Español](https://blog.cloudflare.com/es-es/18-november-2025-outage/), [Español (Latinoamérica)](https://blog.cloudflare.com/es-la/18-november-2025-outage/), [Français](https://blog.cloudflare.com/fr-fr/18-november-2025-outage/), [日本語](https://blog.cloudflare.com/ja-jp/18-november-2025-outage/), [한국어](https://blog.cloudflare.com/ko-kr/18-november-2025-outage/), [繁體中文](https://blog.cloudflare.com/zh-tw/18-november-2025-outage/), [简体中文](https://blog.cloudflare.com/zh-cn/18-november-2025-outage/), [Português](https://blog.cloudflare.com/pt-br/18-november-2025-outage/), [Русский](https://blog.cloudflare.com/ru-ru/18-november-2025-outage/) i [Nederlands](https://blog.cloudflare.com/nl-nl/18-november-2025-outage/).

![BLOG-3110 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45W9Z3GWMFF7Y7B77R3KW7.png&w=1600&h=900&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///////87u/x4uPt5ebx7u/28fHz7e3q////////6uz12d3w2uD05ur57e/27e3t////////5+v50Nn10Nr43+f96u/57u7w////////6e3+0dv60Nz93+n/7fL+8vL1////////8fX/2+T/2+b/6vL/9fn/+Pj6/////////P7/6/D/7fP/+f7///////7+////////////+Pv//P///////////////////////////f//////////////////)

18 listopada 2025 roku o godz. 11:20 UTC (wszystkie podane godziny odnoszą się do UTC) w sieci Cloudflare zaczęły występować poważne zakłócenia w obsłudze kluczowego ruchu sieciowego. Dla użytkowników Internetu próbujących uzyskać dostęp do witryn internetowych naszych klientów problem ten objawiał się stroną błędu sygnalizującą awarię w ramach sieci Cloudflare. 

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![HTTP error page displayed during the incident](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46A2BAVX0VJV0ZTS4X81PR.png&w=715&h=485&f=webp&fit=cover&position=center)

**Przyczyną problemu nie był, ani bezpośrednio, ani pośrednio, cyberatak czy jakakolwiek forma złośliwej aktywności.** Zamiast tego problem został wywołany zmianą uprawnień w jednym z naszych systemów bazodanowych, która spowodowała wygenerowanie wielu wpisów w „pliku cech” (feature file) wykorzystywanego przez nasz system zarządzania ruchem botów. W rezultacie ten plik cech podwoił swoją objętość. Większy niż zakładano plik cech został następnie rozpropagowany na wszystkie maszyny tworzące naszą sieć.

Oprogramowanie działające na tych maszynach, odpowiedzialne za przekierowywanie ruchu w naszej sieci, odczytuje ten plik cech, aby utrzymać system zarządzania ruchem botów w pełnej aktualności wobec stale ewoluujących zagrożeń. Oprogramowanie miało ograniczenie dotyczące maksymalnej wielkości tego pliku cech, a jego nowy, podwojony rozmiar przekraczał ten limit. To spowodowało awarię oprogramowania.

Po tym, jak początkowo błędnie założyliśmy, że obserwowane symptomy wynikają z hiperskalowego ataku DDoS, właściwie zidentyfikowaliśmy źródło problemu i zdołaliśmy zatrzymać propagację pliku cech o większym niż oczekiwano rozmiarze, zastępując go wcześniejszą wersją. Zasadniczy ruch sieciowy w dużej mierze wrócił do normy około 14:30. Przez kolejne kilka godzin pracowaliśmy nad ograniczeniem zwiększonego obciążenia różnych elementów naszej sieci, gdy ruch gwałtownie wracał do trybu online. O godzinie 17:06 wszystkie systemy Cloudflare działały już normalnie.

Przepraszamy naszych klientów oraz całą społeczność Internetu za skutki tego incydentu. Biorąc pod uwagę rolę Cloudflare w ekosystemie Internetu, jakakolwiek przerwa w działaniu któregokolwiek z naszych systemów jest nie do przyjęcia. To, że przez pewien czas nasza sieć nie była w stanie prawidłowo kierować ruchu, jest dla każdego członka naszego zespołu wyjątkowo bolesne. Wiemy, że dziś Państwa zawiedliśmy.

Niniejszy wpis stanowi szczegółowy opis przebiegu zdarzeń oraz wskazuje, które systemy i procesy zawiodły. Jest to również początek, choć nie koniec, działań planowanych po to, aby zapewnić, że podobna awaria nie wystąpi ponownie.

## Awaria

Poniższy wykres przedstawia liczbę kodów odpowiedzi HTTP z grupy 5xx zwracanych przez sieć Cloudflare. Zazwyczaj wartość ta powinna być bardzo niska — i taka pozostawała aż do chwili wystąpienia awarii. 

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Volume of HTTP 5xx requests served by the Cloudflare network](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48QJPQKY6M0ZGYW9BEGTXJ.png&w=715&h=348&f=webp&fit=cover&position=center)

Wolumen odnotowany przed 11:20 stanowi oczekiwany poziom bazowy błędów 5xx występujących w naszej sieci. Nagły skok i późniejsze fluktuacje odzwierciedlają awarię naszego systemu spowodowaną wczytaniem nieprawidłowego pliku cech. Co istotne, system potrafił okresowo samoczynnie wracać do normalnego działania. Było to bardzo nietypowe zachowanie jak na błąd wewnętrzny.

Wyjaśnienie okazało się następujące: plik był generowany co pięć minut przez zapytanie uruchamiane na klastrze bazy danych ClickHouse, który był stopniowo aktualizowany w celu usprawnienia zarządzania uprawnieniami. Nieprawidłowe dane były generowane wyłącznie wtedy, gdy zapytanie wykonywało się na tej części klastra, która została już zaktualizowana. W efekcie co pięć minut istniało ryzyko wygenerowania i szybko rozpropagowania w sieci albo poprawnego, albo wadliwego zestawu plików konfiguracyjnych.

Ta zmienność utrudniała ustalenie, co dokładnie się dzieje, ponieważ cały system potrafił wracać do normalnego działania, po czym ponownie ulegał awarii — w zależności od tego, czy w danej iteracji do naszej sieci trafiały poprawne, czy wadliwe pliki konfiguracyjne. Początkowo skłoniło nas to do przypuszczenia, że przyczyną może być atak. Ostatecznie każdy węzeł ClickHouse zaczął generować wadliwy plik konfiguracyjny, a wahania ustabilizowały się w stanie awarii.

Błędy utrzymywały się aż do momentu zidentyfikowania i usunięcia źródła problemu, co rozpoczęto około 14:30. Rozwiązaliśmy problem, zatrzymując generowanie i propagację wadliwego pliku cech oraz ręcznie wprowadzając sprawdzony, poprawny plik do kolejki jego dystrybucji. Następnie wymuszono ponowne uruchomienie naszego głównego serwera proxy.

Pozostały „długi ogon” widoczny na powyższym wykresie odzwierciedla pracę naszego zespołu polegającą na ponownym uruchamianiu pozostałych usług, które znalazły się w stanie nieprawidłowym. Wolumen błędów 5xx wrócił do normy o 17:06.

Incydent miał wpływ na następujące usługi:

Usługa/produkt| Opis wpływu  
---|---  
Podstawowe usługi CDN i bezpieczeństwa| Kody odpowiedzi HTTP z grupy 5xx. Zrzut ekranu na początku wpisu przedstawia typową stronę błędu wyświetlaną użytkownikom końcowym.  
Turnstile| Nie można załadować Turnstile.  
Workers KV| Usługa Workers KV zwróciła istotnie podwyższony poziom błędów HTTP 5xx, ponieważ żądania kierowane do bramy „front end” KV kończyły się niepowodzeniem wskutek awarii głównego serwera proxy.  
Pulpit nawigacyjny| Choć pulpit nawigacyjny pozostawał w dużej mierze sprawny, większość użytkowników nie mogła się zalogować, ponieważ usługa Turnstile była niedostępna na stronie logowania.  
Email Security| Choć przetwarzanie i dostarczanie poczty elektronicznej przebiegało bez zakłóceń, odnotowaliśmy chwilową utratę dostępu do źródła reputacji adresów IP. Spowodowało to obniżenie skuteczności wykrywania spamu oraz uniemożliwiło uruchamianie niektórych mechanizmów wykrywania opartych na wieku domen, przy czym nie stwierdzono żadnego istotnego wpływu na klientów. Zaobserwowaliśmy również nieprawidłowe działanie części operacji Auto Move; wszystkie objęte nimi wiadomości zostały przeanalizowane i odpowiednio skorygowane.  
Access| U większości użytkowników występowały powszechne błędy uwierzytelniania — zaczęły się wraz z początkiem incydentu i utrzymywały aż do rozpoczęcia wycofywania zmian o 13:05. Istniejące sesje Access pozostały niezakłócone.  
Wszystkie nieudane próby uwierzytelnienia kończyły się wyświetleniem strony błędu, co oznacza, że żaden z tych użytkowników nie uzyskał dostępu do aplikacji docelowej w okresie, gdy mechanizm uwierzytelniania nie działał poprawnie. Pomyślne logowania w tym okresie były prawidłowo rejestrowane w trakcie incydentu.   
Wszelkie próby aktualizacji konfiguracji Access podjęte w tym czasie kończyłyby się niepowodzeniem albo propagowałyby się bardzo wolno. Wszystkie aktualizacje konfiguracji zostały już przywrócone.  
  
Oprócz zwracania błędów HTTP 5xx zaobserwowaliśmy istotne zwiększenie opóźnień odpowiedzi z naszej sieci CDN w okresie trwania incydentu. Było to spowodowane znacznym wykorzystaniem zasobów CPU przez nasze systemy debugowania i obserwowalności, które automatycznie wzbogacają nieprzechwycone błędy o dodatkowe informacje diagnostyczne.

## Jak Cloudflare przetwarza żądania i w jaki sposób doszło dziś do nieprawidłowości

Każde żądanie kierowane do Cloudflare przechodzi jasno zdefiniowaną ścieżkę w naszej sieci. Może pochodzić z przeglądarki ładującej stronę internetową, z aplikacji mobilnej wywołującej interfejs API albo z ruchu automatycznego generowanego przez inną usługę. Takie żądania najpierw trafiają do naszej warstwy HTTP i TLS, następnie przechodzą do naszego głównego systemu proxy (określanego jako FL — „Frontline”), a na końcu do systemu Pingora, który wykonuje wyszukiwanie w pamięci podręcznej lub — jeśli to konieczne — pobiera dane z serwera pochodzenia.

Szczegółowy opis działania naszego głównego serwera proxy udostępniliśmy wcześniej [_tutaj_](https://blog.cloudflare.com/20-percent-internet-upgrade/.). 

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Diagram of our reverse proxy architecture](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48E04GF44VW0S1HCTJT5EC.png&w=715&h=303&f=webp&fit=cover&position=center)

Gdy żądanie przechodzi przez główny serwer proxy, uruchamiane są różne produkty zabezpieczające i optymalizujące wydajność dostępne w naszej sieci. Serwer proxy stosuje unikalną konfigurację i ustawienia dla każdego klienta — od egzekwowania reguł WAF i ochrony przed atakami DDoS po kierowanie ruchu do Developer Platform i R2. Realizuje to za pomocą zestawu modułów specyficznych dla danej domeny, które stosują konfigurację oraz reguły dotyczące zasad do ruchu przechodzącego przez nasz serwer proxy.

Jeden z tych modułów, zarządzanie ruchem botów, był przyczyną dzisiejszej awarii. 

Oferowana przez Cloudflare funkcja [_zarządzania ruchem botów_](https://www.cloudflare.com/application-services/products/bot-management/) obejmuje między innymi model uczenia maszynowego, który nadaje oceny botom dla każdego żądania przechodzącego przez naszą sieć. Nasi klienci wykorzystują te oceny do kontrolowania, które boty mogą uzyskiwać dostęp do ich witryn internetowych, a które nie.

Model jako dane wejściowe wykorzystuje plik konfiguracyjny zawierający zestaw „cech”. W tym kontekście „cecha” oznacza pojedynczy atrybut wykorzystywany przez model uczenia maszynowego do przewidywania, czy dane żądanie zostało wygenerowane automatycznie, czy nie. Plik konfiguracyjny cech stanowi zbiór poszczególnych cech.

Ten plik cech jest odświeżany co kilka minut i publikowany w całej naszej sieci, co umożliwia nam reagowanie na zmiany w przepływach ruchu w Internecie. Pozwala nam to również reagować na nowe typy botów oraz nowe formy ataków z wykorzystaniem botów. Z tego względu kluczowe jest, aby był on wdrażany często i szybko, ponieważ cyberprzestępcy bardzo szybko zmieniają swoją taktykę.

Zmiana w sposobie działania zapytania ClickHouse (wyjaśniona poniżej), które generuje ten plik, spowodowała pojawienie się w nim dużej liczby zduplikowanych wierszy „cech”. Zmiana ta wpłynęła na rozmiar pliku konfiguracyjnego cech (dotychczas o stałej wielkości), co spowodowało wywołanie błędu w module zarządzania ruchem botów.

W efekcie system głównego serwera proxy, który obsługuje przetwarzanie ruchu dla naszych klientów, zwracał kody błędów HTTP 5xx dla każdego ruchu zależnego od modułu zarządzania ruchem botów. Wpłynęło to również na usługi Workers KV i Access, które polegają na działaniu głównego serwera proxy.

Niezależnie od tego incydentu prowadziliśmy — i nadal prowadzimy — migrację ruchu naszych klientów do nowej wersji usługi proxy, wewnętrznie znanej jako [_FL2_](https://blog.cloudflare.com/20-percent-internet-upgrade/). Obie wersje zostały dotknięte tym problemem, choć obserwowany wpływ był w ich przypadku różny.

Klienci korzystający z nowego silnika proxy FL2 obserwowali błędy HTTP 5xx. Klienci korzystający ze starszego silnika proxy, znanego jako FL, nie obserwowali błędów, jednak oceny botów nie były generowane prawidłowo, wskutek czego cały ruch uzyskiwał wskaźnik dotyczący botów równy zero. Klienci, którzy mieli wdrożone reguły blokujące boty, obserwowali dużą liczbę fałszywych alarmów. Z kolei klienci, którzy nie wykorzystywali wskaźnika dotyczącego botów w swoich regułach, nie odnotowali żadnego wpływu.

Kolejnym wyraźnym symptomem, który wprowadził nas w błąd i skłonił do podejrzeń o możliwy atak, był fakt, że strona statusu Cloudflare przestała działać. Strona statusu jest hostowana całkowicie poza infrastrukturą Cloudflare i nie ma żadnych zależności od naszych usług. Choć okazało się to być jedynie zbiegiem okoliczności, doprowadziło to niektórych członków zespołu diagnozującego problem do przypuszczenia, że atakujący może celować zarówno w nasze systemy, jak i w naszą stronę statusu. Odwiedzający stronę statusu w tym czasie widzieli komunikat o błędzie:

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Error on the Cloudflare status page](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48SDRSCKYVGTKDJ2G4GGXG.png&w=715&h=171&f=webp&fit=cover&position=center)

Na wewnętrznym czacie dotyczącym incydentów wyrażaliśmy swoje obawy, że może to być kontynuacja niedawnej serii [_ataków DDoS_](https://blog.cloudflare.com/defending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos/) na dużą skalę, prowadzonych z sieci botów [_Aisuru_](https://techcommunity.microsoft.com/blog/azureinfrastructureblog/defending-the-cloud-azure-neutralized-a-record-breaking-15-tbps-ddos-attack/4470422):

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Internal chat screenshot](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW460AE6F151MG2AFHC53YGK.png&w=715&h=167&f=webp&fit=cover&position=center)

### Zmiana w sposobie działania zapytań

Wspomniałem powyżej, że zmiana w sposobie działania zapytania bazowego spowodowała, iż plik cech zawierał dużą liczbę zduplikowanych wierszy. Przedmiotowy system bazodanowy opiera się na oprogramowaniu ClickHouse.

Aby poznać kontekst, warto zrozumieć, w jaki sposób działają zapytania rozproszone w ClickHouse. Klaster ClickHouse składa się z wielu shardów. Aby zapytać o dane ze wszystkich shardów, korzystamy z tzw. tabel rozproszonych (opartych na silniku tabel `Distributed`) w bazie danych o nazwie `default`. Silnik Distributed odpytuje tabele bazowe znajdujące się w bazie danych `r0`. Tabele bazowe to miejsce przechowywania danych na każdym shardzie klastra ClickHouse.

Zapytania kierowane do tabel rozproszonych są wykonywane za pośrednictwem współdzielonego konta systemowego. W ramach działań mających na celu zwiększenie bezpieczeństwa i niezawodności zapytań rozproszonych trwają prace nad tym, aby zamiast tego były one uruchamiane pod pierwotnymi kontami użytkowników.

Do tej pory użytkownicy ClickHouse, podczas wykonywania zapytań o metadane z tabel systemowych ClickHouse, takich jak `system.tables` lub `system.columns`, widzieli wyłącznie tabele znajdujące się w bazie `default`.

Ponieważ użytkownicy mieli już niejawny dostęp do tabel bazowych w `r0`, wprowadziliśmy o 11:05 zmianę, aby dostęp ten był jawny, dzięki czemu użytkownicy mogli również zobaczyć metadane tych tabel. Zapewnienie, że wszystkie zapytania podrzędne w ramach zapytań rozproszonych mogą być uruchamiane pod pierwotnym użytkownikiem, umożliwia bardziej precyzyjną ocenę limitów zapytań i przyznanych uprawnień, zapobiegając sytuacji, w której nieprawidłowe zapytanie podrzędne danego użytkownika wpływa na innych.

Opisana powyżej zmiana spowodowała, że wszyscy użytkownicy uzyskiwali poprawne metadane dotyczące tabel, do których mieli dostęp. Niestety, w przeszłości przyjęto założenie, że lista kolumn zwracana przez takie zapytanie będzie obejmować wyłącznie bazę danych `default`:

`SELECT  
name,  
type  
FROM system.columns  
WHERE  
table = 'http_requests_features'  
order by name;`

Należy zwrócić uwagę, że zapytanie nie filtruje według nazwy bazy danych. Wraz ze stopniowym wdrażaniem jawnych uprawnień dla użytkowników danego klastra ClickHouse, po zmianie wprowadzonej o 11:05 powyższe zapytanie zaczęło zwracać „duplikaty” kolumn, ponieważ dotyczyły one tabel bazowych przechowywanych w bazie r0.

Niestety tego typu zapytanie było wykonywane przez logikę generowania pliku cech na potrzeby zarządzania ruchem botów w celu utworzenia każdej wejściowej „cechy” dla pliku, o którym mowa na początku tej sekcji. 

Powyższe zapytanie zwracało tabelę kolumn podobną do przedstawionej poniżej (uproszczony przykład):

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Example of code block](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49D1ADZJSH7WHD06XCEAMM.png&w=548&h=121&f=webp&fit=cover&position=center)

Jednak w ramach dodatkowych uprawnień przyznanych użytkownikowi odpowiedź zaczęła zawierać pełne metadane schematu `r0`, co w praktyce więcej niż podwoiło liczbę zwracanych wierszy. W konsekwencji zwiększyło to także liczbę wierszy (czyli cech) w finalnym pliku wynikowym. 

### Wstępna alokacja pamięci

Każdy moduł działający w naszej usłudze proxy posiada zestaw ograniczeń mających zapobiegać niekontrolowanemu zużyciu pamięci oraz umożliwiać jej wstępną alokację jako mechanizm optymalizacji wydajności. W tym konkretnym przypadku system zarządzania ruchem botów ma ograniczenie dotyczące liczby cech wykorzystywanych przez modele uczenia maszynowego w trakcie działania. Obecnie limit ten wynosi 200, czyli znacznie powyżej naszego bieżącego wykorzystania na poziomie około 60 cech. Limit ten istnieje, ponieważ ze względów wydajnościowych wstępnie alokujemy pamięć na potrzeby obsługi cech.

Gdy wadliwy plik zawierający ponad 200 cech został rozpropagowany na nasze serwery, osiągnięto ten limit — co spowodowało awaryjne przerwanie działania systemu. Kod modułu FL2 w języku Rust, który wykonuje to sprawdzenie i był źródłem nieobsłużonego błędu, przedstawiono poniżej:

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![code that generated the error](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47WGY8GKFJ60E93AX233VZ.png&w=715&h=221&f=webp&fit=cover&position=center)

Doprowadziło to do następującej paniki, co z kolei skutkowało błędem 5xx:

`thread fl2_worker_thread panicked: called Result::unwrap() on an Err value`

### Inne skutki podczas incydentu

Inne systemy oparte na naszym głównym serwerze proxy zostały również dotknięte skutkami incydentu. Dotyczyło to m.in. usług Workers KV oraz Cloudflare Access. Zespół zdołał ograniczyć wpływ na te systemy o 13:04, kiedy w usłudze Workers KV wprowadzono poprawkę pozwalającą ominąć główny serwer proxy. W konsekwencji wszystkie systemy zależne od usługi Workers KV (w tym Access) zaczęły odnotowywać niższy wskaźnik błędów. 

To również wpłynęło na pulpit nawigacyjny Cloudflare, ponieważ wewnętrznie wykorzystywano usługę Workers KV, a mechanizm Cloudflare Turnstile był używany jako element procesu logowania.

Omawiana awaria miała wpływ na mechanizm Turnstile, w wyniku czego klienci bez aktywnej sesji w pulpicie nawigacyjnym nie mogli się zalogować. Objawiało się to obniżoną dostępnością w dwóch przedziałach czasowych: od 11:30 do 13:10 oraz między 14:40 a 15:30, co widać na poniższym wykresie.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![availability of Cloudflare internal APIs during the incident](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49HVBRCES9NW26RAKCYSPW.png&w=715&h=241&f=webp&fit=cover&position=center)

Pierwszy okres, od 11:30 do 13:10, wynikał z wpływu incydentu na usługę Workers KV, od której zależą niektóre funkcje płaszczyzny zarządzania oraz pulpitu nawigacyjnego. Dostępność została przywrócona o 13:10, gdy usługa Workers KV zaczęła omijać system głównego serwera proxy.  
  
Drugi okres obniżonej dostępności pulpitu nawigacyjnego wystąpił po przywróceniu danych konfiguracyjnych dotyczących cech. Zaległość prób logowania zaczęła przeciążać pulpit nawigacyjny. Ta zaległość, w połączeniu z ponawianymi próbami logowania, spowodowała zwiększone opóźnienia, co przełożyło się na obniżoną dostępność pulpitu nawigacyjnego. Zwiększenie współbieżności na płaszczyźnie zarządzania skutkowało przywróceniem dostępności około 15:30.

## Działania naprawcze i kolejne kroki

Teraz, gdy nasze systemy ponownie działają w trybie online i funkcjonują normalnie, rozpoczęliśmy już prace nad ich wzmocnieniem na wypadek podobnych awarii w przyszłości. W szczególności skupiamy się na następujących kwestiach:

  * Wzmocnienie procesu przyjmowania plików konfiguracyjnych generowanych przez Cloudflare w taki sam sposób, w jaki zabezpieczamy dane wprowadzane przez użytkowników
  * Uwzględnienie większej liczby globalnych mechanizmów wyłączania cech (global kill switches)
  * Wyeliminowanie możliwości przeciążenia zasobów systemowych przez zrzuty pamięci (core dumps) lub inne raporty o błędach
  * Przegląd trybów awarii związanych z warunkami błędów we wszystkich głównych modułach proxy



Dzisiejsza awaria była najpoważniejszym incydentem Cloudflare [_od 2019 roku_](https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/). Zdarzały się awarie powodujące [_niedostępność pulpitu nawigacyjnego_](https://blog.cloudflare.com/post-mortem-on-cloudflare-control-plane-and-analytics-outage/), a także takie, które sprawiały, że [_nowsze funkcje_](https://blog.cloudflare.com/cloudflare-service-outage-june-12-2025/) były czasowo niedostępne. Jednak w ciągu ostatnich ponad 6 lat nie mieliśmy awarii, która spowodowałaby zatrzymanie większości podstawowego ruchu przepływającego przez naszą sieć.

Awaria taka jak dzisiejsza jest niedopuszczalna. Nasze systemy zostały zaprojektowane tak, aby były wysoce odporne na awarie i gwarantowały nieprzerwane przekazywanie ruchu. Każdy wcześniejszy incydent prowadził nas do tworzenia nowych, jeszcze bardziej odpornych rozwiązań.

W imieniu całego zespołu Cloudflare chciałbym przeprosić za zakłócenia, jakie dziś spowodowaliśmy w działaniu Internetu. 

Czas (UTC)| Status| Opis  
---|---|---  
11:05| Normalne działanie.| Wdrożono zmianę w mechanizmie kontroli dostępu do bazy danych.  
11:28| Zaczyna być widoczny wpływ incydentu.| Wdrożenie dociera do środowisk klientów; pojawiają się pierwsze błędy w ruchu HTTP klientów.  
11:32–13:05| Zespół przeanalizował podwyższony poziom ruchu oraz błędy dotyczące usługi Workers KV.  
  
| Początkowym objawem wydawała się obniżona szybkość odpowiedzi usługi Workers KV, co miało wtórny wpływ na inne usługi Cloudflare.  
Podjęto działania zaradcze, takie jak manipulacja ruchem oraz ograniczenia na poziomie kont, aby przywrócić usługę Workers KV do normalnych parametrów pracy.  
Pierwszy test automatyczny wykrył problem o 11:31, a analiza ręczna rozpoczęła się o 11:32. Połączenie dotyczące incydentu nawiązano o 11:35.  
13:05| Wdrożono obejście dla usług Workers KV i Cloudflare Access — wpływ incydentu został ograniczony.| Podczas dochodzenia wykorzystaliśmy wewnętrzne mechanizmy obejścia dla Workers KV i Cloudflare Access, dzięki czemu usługi te przełączyły się na wcześniejszą wersję naszego głównego serwera proxy. Choć problem występował również w poprzednich wersjach naszego serwera proxy, jego wpływ był mniejszy, co opisano poniżej.  
13:37| Prace skoncentrowano na wycofaniu pliku konfiguracyjnego modułu zarządzania ruchem botów do ostatniej znanej, poprawnie działającej wersji.| Byliśmy przekonani, że to plik konfiguracyjny modułu zarządzania ruchem botów był przyczyną incydentu. Zespoły pracowały nad przywróceniem działania usługi w kilku równoległych strumieniach, z których najszybszym było odtworzenie poprzedniej wersji pliku.  
14:24| Wstrzymano tworzenie i propagację nowych plików konfiguracyjnych modułu zarządzania ruchem botów.| Ustaliliśmy, że moduł zarządzania ruchem botów był źródłem błędów 500, a przyczyną — nieprawidłowy plik konfiguracyjny. Wstrzymaliśmy automatyczne wdrażanie nowych plików konfiguracyjnych modułu zarządzania ruchem botów.  
14:24| Ukończono test nowego pliku.| Zaobserwowaliśmy skuteczne przywrócenie działania po użyciu starej wersji pliku konfiguracyjnego, a następnie skoncentrowaliśmy się na przyspieszeniu wdrożenia poprawki w skali globalnej.  
14:30| Usunięto główny wpływ incydentu. Usługi zależne zaczęły odnotowywać spadek liczby błędów.| Prawidłowy plik konfiguracyjny modułu zarządzania ruchem botów został wdrożony globalnie, a większość usług zaczęła działać poprawnie.  
17:06| Wszystkie usługi przywrócono do pełnej sprawności. Wpływ incydentu ustąpił.| Wszystkie usługi zależne zostały ponownie uruchomione, a pełna funkcjonalność — przywrócona.  
  
Na tej stronie

Dyskutuj online

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2F18-november-2025-outage%2F&t=Awaria%20Cloudflare%20z%2018%20listopada%202025%C2%A0r.)[](https://x.com/intent/post?text=Awaria+Cloudflare+z+18+listopada+2025%C2%A0r.&url=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2F18-november-2025-outage%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2F18-november-2025-outage%2F)[](https://bsky.app/intent/compose?text=Awaria+Cloudflare+z+18+listopada+2025%C2%A0r.+https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2F18-november-2025-outage%2F)[](https://mastodonshare.com/?text=Awaria+Cloudflare+z+18+listopada+2025%C2%A0r.&url=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2F18-november-2025-outage%2F)[](https://www.threads.net/intent/post?text=Awaria+Cloudflare+z+18+listopada+2025%C2%A0r.+https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2F18-november-2025-outage%2F)

## Powiązane tagi

[Analiza przypadku](https://blog.cloudflare.com/pl-pl/tag/post-mortem/)[Awaria](https://blog.cloudflare.com/pl-pl/tag/outage/)[Zarządzanie ruchem botów](https://blog.cloudflare.com/pl-pl/tag/bot-management/)

Śledź nas w mediach społecznościowych

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Zapisz się, aby otrzymywać powiadomienia o nowych postach

Adres e-mail

Nigdy nie udostępnimy Twojego adresu e-mail.

Subskrybuj

Dziękujemy za subskrypcję! Sprawdź skrzynkę odbiorczą, aby ją potwierdzić.
