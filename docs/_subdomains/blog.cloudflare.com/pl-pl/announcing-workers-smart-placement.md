---
url: https://blog.cloudflare.com/pl-pl/announcing-workers-smart-placement/
title: Smart Placement przyspiesza dzia\u0142anie aplikacji, przenosz\u0105c kod w pobli\u017ce zaplecza \u2014 nie jest wymagana konfiguracja | Blog Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:39:55.884848+00:00
---

# Smart Placement przyspiesza działanie aplikacji, przenosząc kod w pobliże zaplecza — nie jest wymagana konfiguracja | Blog Cloudflare

> Source: https://blog.cloudflare.com/pl-pl/announcing-workers-smart-placement/

[Blog](https://blog.cloudflare.com/pl-pl/)

[Cloudflare Workers](https://blog.cloudflare.com/pl-pl/tag/workers/)[Database](https://blog.cloudflare.com/pl-pl/tag/database/)[Developer Platform](https://blog.cloudflare.com/pl-pl/tag/developer-platform/)+3Pokaż 3 więcej tagów

6 tagówPokaż 6 tagów

  * Tagi wpisu
  * [Programiści](https://blog.cloudflare.com/pl-pl/tag/developers/)
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



[Developer Week](https://blog.cloudflare.com/pl-pl/tag/developer-week/)[Programiści](https://blog.cloudflare.com/pl-pl/tag/developers/)[Serverless](https://blog.cloudflare.com/pl-pl/tag/serverless/)

[Cloudflare Workers](https://blog.cloudflare.com/pl-pl/tag/workers/)[Database](https://blog.cloudflare.com/pl-pl/tag/database/)[Developer Platform](https://blog.cloudflare.com/pl-pl/tag/developer-platform/)[Developer Week](https://blog.cloudflare.com/pl-pl/tag/developer-week/)[Programiści](https://blog.cloudflare.com/pl-pl/tag/developers/)[Serverless](https://blog.cloudflare.com/pl-pl/tag/serverless/)

16 maja 2023

# Smart Placement przyspiesza działanie aplikacji, przenosząc kod w pobliże zaplecza — nie jest wymagana konfiguracja

![Michael Hart](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44Y5FGZZS90ZJA5EFQW15Q.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Serena Shah-Simpson](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45E4TK6GHZXWH66VF37ZEZ.PNG&w=64&h=64&f=webp&fit=cover&position=center)![Tanushree Sharma](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46NT9GBM742JJW1W4G7ND8.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Michael Hart](https://blog.cloudflare.com/pl-pl/author/michael-hart/), [Serena Shah-Simpson](https://blog.cloudflare.com/pl-pl/author/serena/) i [Tanushree Sharma](https://blog.cloudflare.com/pl-pl/author/tanushree/)

7 min czytania

KOPIUJ URL

Ten wpis jest również dostępny w [English](https://blog.cloudflare.com/announcing-workers-smart-placement/), [Español](https://blog.cloudflare.com/es-es/announcing-workers-smart-placement/), [日本語](https://blog.cloudflare.com/ja-jp/announcing-workers-smart-placement/), [한국어](https://blog.cloudflare.com/ko-kr/announcing-workers-smart-placement/), [繁體中文](https://blog.cloudflare.com/zh-tw/announcing-workers-smart-placement/), [简体中文](https://blog.cloudflare.com/zh-cn/announcing-workers-smart-placement/), [Português](https://blog.cloudflare.com/pt-br/announcing-workers-smart-placement/) i [Русский](https://blog.cloudflare.com/ru-ru/announcing-workers-smart-placement/).

![Smart Placement speeds up applications by moving code close to your backend — no config needed](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW463REMTYFQ9WDSW6E67JH9.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///////+9PPv7ezk7+7l9PPs8vPv7O3s////////9fTu7erg7uvf8/Dm8vHs7u7t////////9/Xw7ure7+na8u7h8/Hr8PDw////////+vj08ezh8evc9fDj9vPu9PP1//////////379vLq9vHl+vXs+/n1+fj6////////////+/n1+/jz//35///+/f7////////////////+///+////////////////////////////////////////////)

Wszyscy doświadczyliśmy frustracji związanej z wolno ładującymi się witrynami internetowymi lub aplikacjami, które wydają się blokować, gdy muszą wywołać interfejs API w celu pobrania aktualizacji. coś krótszego niż natychmiastowe, a Twój umysł błądzi do czegoś innego...

Jednym ze sposobów na przyspieszenie pracy jest przybliżenie zasobów jak najbliżej użytkownika — to właśnie robi firma Cloudflare w zakresie mocy obliczeniowych, przekraczając milisekundy mniej niż większość populacji na świecie. Jednak, jakkolwiek może się to wydawać sprzeczne z intuicją, czasami zbliżenie mocy obliczeniowej do użytkownika może w rzeczywistości spowolnić aplikacje. Jeśli Twoja aplikacja musi łączyć się z interfejsami API, bazami danych lub innymi zasobami, które nie znajdują się w pobliżu użytkownika końcowego, bardziej wydajne może być uruchomienie aplikacji w pobliżu zasobów zamiast użytkownika.

Dlatego dzisiaj mamy przyjemność ogłosić, że rozwiązania Smart Placement for Workers i Pages Functions przyspieszą każdą interakcję. Dzięki Smart Placement Cloudflare przenosi przetwarzanie bezserwerowe do superchmury, przenosząc zasoby obliczeniowe w optymalne lokalizacje w celu przyspieszenia aplikacji. Najlepsze jest to, że jest całkowicie zautomatyzowana, bez żadnych dodatkowych danych (takich jak budzący grozę „region”).

Usługa Smart Placement jest teraz dostępna, w otwartej wersji beta, dla wszystkich klientów Workers i Pages!

[Obejrzyj naszą prezentację, jak działa inteligentne rozmieszczanie!](https://smart-placement-demo.pages.dev/)

## Zmiana bezserwerowe

Sieć Anycast Cloudflare jest stworzona do natychmiastowego przetwarzania żądań,_blisko użytkownika_. Dlatego jesteś programistą i dlatego właśnie Cloudflare Workers, nasza oferta bezserwerowe obliczeniowej, jest tak przekonująca. Konkurenci są ograniczeni przez „regiony”, podczas gdy Workers biegną wszędzie — stąd mamy jeden region: Ziemię. Żądania obsługiwane w całości przez Workers mogą być przetwarzane od razu, bez konieczności docierania do serwer pochodzenia.

Chociaż początkowo uważano, że ta koncepcja bezserwerowe działania dotyczy lekkich zadań, w ostatnich latach nastąpiła zmiana. Jest ona wykorzystywana do zastąpienia tradycyjnej architektury, która opiera się na serwerach pochodzenia i infrastrukturze samozarządzającej, zamiast tylko ją rozszerzać. Obserwujemy coraz więcej takich przypadków użycia w przypadku użytkowników Workers i Pages.

### Bezserwerowy stan potrzeb

W związku z przechodzeniem do modelu bezserwerowe i budowaniem całych aplikacji na platformie Workers pojawiła się potrzeba danych. Przechowywanie informacji o wcześniejszych działaniach i zdarzeniach umożliwia budowanie spersonalizowanych, interaktywnych aplikacji. Załóżmy, że musisz tworzyć profile użytkowników, zapisywać stronę, którą użytkownik przerwał, które kody SKU użytkownik ma w koszyku – wszystko to jest przypisywane do punktów danych używanych do utrzymywania stanu. Usługi zaplecza, takie jak relacyjne bazy danych, magazyny kluczwartość, magazyny blobów i interfejsy API, umożliwiają tworzenie aplikacji stanowych.

### Cloudflare przetwarzanie + pamięć masowa: potężny duet

Mamy nasz własny, rosnący pakiet ofert w zakresie pamięci masowej: Workers KV, Durable Objects, D1, [R2](https://www.cloudflare.com/developer-platform/r2/). Podczas dojrzewania naszych produktów związanych z danymi starannie zastanawiamy się nad ich interakcjami z Workers , abyś nie musiał tego robić! Na przykład innym podejściem, które w niektórych przypadkach zapewnia lepszą wydajność, jest przenoszenie magazynu zamiast przetwarzania blisko użytkowników. Jeśli używasz Durable Objects do tworzenia gry w czasie rzeczywistym, możemy przenieść Durable Objects , aby zminimalizować opóźnienie dla wszystkich użytkowników.

Chcemy, aby na przyszły stan użytkownik ustawił tryb = "smart",a my ocenimy optymalne rozmieszczenie wszystkich Twoich zasobów bez konieczności dodatkowej konfiguracji.

### Cloudflare + {backendService}USD

Obecnie głównym przypadkiem użycia Smart Placement jest korzystanie z usług innych niż Cloudflare, takich jak zewnętrzne bazy danych lub interfejsy API innych firm.

Wiele usług zaplecza, niezależnie od tego, czy są to usługi z własnym hostingiem, czy usługi zarządzane, jest scentralizowanych, co oznacza, że dane są przechowywane i zarządzane w jednym miejscu. Twoi użytkownicy są globalni, a Workers działają globalnie, ale zaplecze jest scentralizowane.

Jeśli Twój kod wysyła wiele żądań do Twoich usług zaplecza, mogą one wiele razy przemierzać świat, mając na uwadze wydajność. Niektóre usługi oferują replikację i zapisywanie w zapisywanie w pamięci podręcznej , co pomaga poprawić wydajność, ale wiąże się również z kompromisami, takimi jak spójność danych i wyższe koszty, które należy rozważyć w odniesieniu do Twojego przypadku użycia.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![A map of the globe illustrating global users, global workers and a centralized database. ](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4877KTAFZ54HDMT6TVBXPP.png&w=715&h=402&f=webp&fit=cover&position=center)

Sieć sieć Cloudflare [~50 ms, docierając do 95% światowej populacji połączonej](https://www.cloudflare.com/network/) z Internetem. Stawiamy na głowie, ale jesteśmy również bardzo bliscy komunikowania się z Twoimi usługami zaplecza.

## Wydajność aplikacji zależy od doświadczenie użytkownika

Aby zrozumieć, jak przeniesienie mocy obliczeniowej do usług zaplecza mogłoby zmniejszyć opóźnienie aplikacji, zapoznajmy się z przykładem:

Załóżmy, że masz użytkownika w Sydney w Australii, który uzyskuje dostęp do aplikacji działającej na platformie Workers. Ta aplikacja wykonuje trzy podróże w obie strony do bazy danych znajdującej się we Frankfurcie w Niemczech, aby obsłużyć żądanie użytkownika.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1787 Embedded Image - krvyST](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46K0J7CQVHJM69K0X2F7HW.png&w=715&h=254&f=webp&fit=cover&position=center)

Intuicyjnie można odgadnąć, że wąskim gardłem będzie czas, przez który pracownik wykonuje wielokrotne podróże po sieci do Twojej bazy danych. Zamiast tego, że proces Worker jest wywoływany blisko użytkownika, co by było, gdyby był wywoływany w centrum danych znajdującym się najbliżej bazy danych?

![wAAAABJRU5ErkJggg==](https://blog.cloudflare.com/_emdash/api/media/file/01KW46JG8Q61D0TYTP363C4KP2)

Wystawmy to na próbę.

Zmierzyliśmy czas trwania żądania dla pracownika Worker bez Smart Placement i porównaliśmy go z żądaniem z włączoną opcją Smart Placement. W przypadku obu testów wysłaliśmy 3500 żądań z Sydney do platformy Worker, która wykonuje trzy podróże w obie strony do instancji [Upstash](https://upstash.com/) (warstwa bezpłatna) znajdującej się w eu-central-1 (Frankfurt).

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![A graph showing request duration with and without Smart Placement enabled. ](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4768M6PTQMJX5HNQCQ2S8V.png&w=715&h=432&f=webp&fit=cover&position=center)

Rezultaty są jasne! W tym przykładzie przeniesienie procesu roboczego do zaplecza **poprawiłowydajność aplikacji o 4-8 razy**.

## Decyzje dotyczące sieci nie powinny być decyzjami ludzkimi

Jako programista powinieneś skupić się na tym, co robisz najlepiej – na budowaniu aplikacji – nie martwiąc się o decyzje sieciowe, które przyspieszą Twoje aplikacje.

Cloudflare ma wyjątkowy uprzywilejowany punkt: nasza sieć gromadzi informacje na temat optymalnych ścieżek między użytkownikami, centrami danych Cloudflare i serwerami zaplecza – mamy w tym zakresie duże doświadczenie z [usługą Argo Smart Routing](https://blog.cloudflare.com/argo/). Smart Placement bierze te czynniki pod uwagę, aby automatycznie umieścić Twoją platformę Worker w najlepszym miejscu, aby zminimalizować całkowity czas trwania żądań.

Jak więc działa Inteligentne rozmieszczanie?

Smart Placement można włączyć dla każdego pracownika na karcie Ustawienia lub w pliku wrangler.toml:
    
    
    [placement]
    mode = "smart"

Gdy włączysz funkcję Smart Placement w rozwiązaniu Worker lub Pages Function, algorytm Smart Placement analizuje żądania fetch (znane również jako żądania podrzędne), które wysyłany jest przez platformę Worker w czasie rzeczywistym. Następnie porównuje je z danymi o opóźnienie agregowanymi przez naszą sieć. Jeśli wykryjemy, że Twoja platforma Worker wykonuje średnio więcej niż jedno podżądanie do zasobu zaplecza, zostanie ona automatycznie wywoływana z poziomu optymalnego centrum danych!

Istnieje kilka usług zaplecza, które nie bez powodu nie są uwzględniane przez algorytm Smart Placement:

  * Usługi rozproszone globalnie: jeśli usługi, z którymi komunikuje się platforma Worker, są rozproszone geograficznie w wielu regionach, Smart Placement nie jest dobrym rozwiązaniem. Automatycznie wykluczamy je z optymalizacji inteligentnego rozmieszczania.
  * Usługi analizy i rejestrowania żądań do usług analizy lub rejestrowania nie muszą znajdować się ścieżką krytyczną Twojej aplikacji. Powinna być używana, aby odpowiedź zwrotna do użytkowników nie była blokowana podczas instrumentacji kodu. Ponieważ `waitUntil()` nie wpływa na czas trwania żądania z perspektywy użytkownika, automatycznie wykluczamy usługi analizy/rejestrowania poza optymalizacją Inteligentne rozmieszczenie.



Listę usług nieuwzględnionych w algorytmie Smart Placement można znaleźć w naszej dokumentacji.

Po uruchomieniu inteligentnego rozmieszczania w narzędziu Worker będzie widoczna nowa zakładka Czas trwania żądania. 1% żądań przekierowujemy bez włączonego inteligentnego rozmieszczania, dzięki czemu można sprawdzić jego wpływ na czas trwania żądania.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Request duration with and without Smart Placement shown on the Workers dashboard. ](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW456H2J1AGEQ2GCCPGS38ZS.png&w=715&h=388&f=webp&fit=cover&position=center)

I owszem, to naprawdę takie proste!

Wypróbuj Smart Placement, zapoznając się z naszą [wersją demonstracyjną](https://smart-placement-demo.pages.dev/) (to świetna zabawa!). Aby dowiedzieć się więcej, zapoznaj się z naszą [dokumentacją dla programistów](https://developers.cloudflare.com/workers/platform/smart-placement/).

## Co dalej z inteligentnym rozmieszczaniem?

Dopiero zaczynamy! Mamy wiele pomysłów, jak możemy ulepszyć Smart Placement:

  * pomoc w obliczaniu optymalnej lokalizacji w przypadku, gdy aplikacja korzysta z wielu zapleczy
  * Rozmieszczenie precyzyjne (np. jeśli platforma Worker korzysta z wielu zapleczy w zależności od ścieżki. Obliczamy optymalne rozmieszczenie na ścieżkę zamiast na pracowników)
  * Wsparcie dla połączeń TCP



Skontaktuj się z nami! Jeśli masz uwagi lub prośby o dodanie funkcji, skontaktuj się z [Discord z deweloperami Cloudflare](https://discord.com/invite/cloudflaredev).

### Obejrzyj na Cloudflare TV

Na tej stronie

Dyskutuj online

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fannouncing-workers-smart-placement%2F&t=Smart%20Placement%20przyspiesza%20dzia%C5%82anie%20aplikacji%2C%20przenosz%C4%85c%20kod%20w%20pobli%C5%BCe%20zaplecza%20%E2%80%94%20nie%20jest%20wymagana%20konfiguracja)[](https://x.com/intent/post?text=Smart+Placement+przyspiesza+dzia%C5%82anie+aplikacji%2C+przenosz%C4%85c+kod+w+pobli%C5%BCe+zaplecza+%E2%80%94+nie+jest+wymagana+konfiguracja&url=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fannouncing-workers-smart-placement%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fannouncing-workers-smart-placement%2F)[](https://bsky.app/intent/compose?text=Smart+Placement+przyspiesza+dzia%C5%82anie+aplikacji%2C+przenosz%C4%85c+kod+w+pobli%C5%BCe+zaplecza+%E2%80%94+nie+jest+wymagana+konfiguracja+https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fannouncing-workers-smart-placement%2F)[](https://mastodonshare.com/?text=Smart+Placement+przyspiesza+dzia%C5%82anie+aplikacji%2C+przenosz%C4%85c+kod+w+pobli%C5%BCe+zaplecza+%E2%80%94+nie+jest+wymagana+konfiguracja&url=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fannouncing-workers-smart-placement%2F)[](https://www.threads.net/intent/post?text=Smart+Placement+przyspiesza+dzia%C5%82anie+aplikacji%2C+przenosz%C4%85c+kod+w+pobli%C5%BCe+zaplecza+%E2%80%94+nie+jest+wymagana+konfiguracja+https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fannouncing-workers-smart-placement%2F)

## Powiązane tagi

[Cloudflare Workers](https://blog.cloudflare.com/pl-pl/tag/workers/)[Database](https://blog.cloudflare.com/pl-pl/tag/database/)[Developer Platform](https://blog.cloudflare.com/pl-pl/tag/developer-platform/)[Developer Week](https://blog.cloudflare.com/pl-pl/tag/developer-week/)[Programiści](https://blog.cloudflare.com/pl-pl/tag/developers/)[Serverless](https://blog.cloudflare.com/pl-pl/tag/serverless/)

Śledź nas w mediach społecznościowych

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Zapisz się, aby otrzymywać powiadomienia o nowych postach

Adres e-mail

Nigdy nie udostępnimy Twojego adresu e-mail.

Subskrybuj

Dziękujemy za subskrypcję! Sprawdź skrzynkę odbiorczą, aby ją potwierdzić.
