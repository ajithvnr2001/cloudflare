---
url: https://blog.cloudflare.com/pl-pl/code-orange-fail-small-complete/
title: Inicjatywa Code Orange: Fail Small dobieg\u0142a ko\u0144ca, a jej rezultatem jest silniejsza sie\u0107 Cloudflare. | Blog Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:36:55.158366+00:00
---

# Inicjatywa Code Orange: Fail Small dobiegła końca, a jej rezultatem jest silniejsza sieć Cloudflare. | Blog Cloudflare

> Source: https://blog.cloudflare.com/pl-pl/code-orange-fail-small-complete/

[Blog](https://blog.cloudflare.com/pl-pl/)

[Analiza przypadku](https://blog.cloudflare.com/pl-pl/tag/post-mortem/)[Awaria](https://blog.cloudflare.com/pl-pl/tag/outage/)[Code Orange](https://blog.cloudflare.com/pl-pl/tag/code-orange/)

3 tagówPokaż 3 tagów

  * Tagi wpisu
  * [Analiza przypadku](https://blog.cloudflare.com/pl-pl/tag/post-mortem/)[Awaria](https://blog.cloudflare.com/pl-pl/tag/outage/)[Code Orange](https://blog.cloudflare.com/pl-pl/tag/code-orange/)
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



[Analiza przypadku](https://blog.cloudflare.com/pl-pl/tag/post-mortem/)[Awaria](https://blog.cloudflare.com/pl-pl/tag/outage/)[Code Orange](https://blog.cloudflare.com/pl-pl/tag/code-orange/)

1 maja 2026

# Inicjatywa Code Orange: Fail Small dobiegła końca, a jej rezultatem jest silniejsza sieć Cloudflare.

![Jeremy Hartman](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44YJSKH239C2RVYTF2NVMJ.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Jeremy Hartman](https://blog.cloudflare.com/pl-pl/author/jeremy-hartman/)

10 min czytania

KOPIUJ URL

Ten wpis jest również dostępny w [English](https://blog.cloudflare.com/code-orange-fail-small-complete/), [Deutsch](https://blog.cloudflare.com/de-de/code-orange-fail-small-complete/), [Español](https://blog.cloudflare.com/es-es/code-orange-fail-small-complete/), [Español (Latinoamérica)](https://blog.cloudflare.com/es-la/code-orange-fail-small-complete/), [Français](https://blog.cloudflare.com/fr-fr/code-orange-fail-small-complete/), [Italiano](https://blog.cloudflare.com/it-it/code-orange-fail-small-complete/), [日本語](https://blog.cloudflare.com/ja-jp/code-orange-fail-small-complete/), [한국어](https://blog.cloudflare.com/ko-kr/code-orange-fail-small-complete/), [繁體中文](https://blog.cloudflare.com/zh-tw/code-orange-fail-small-complete/), [简体中文](https://blog.cloudflare.com/zh-cn/code-orange-fail-small-complete/) i [Português](https://blog.cloudflare.com/pt-br/code-orange-fail-small-complete/).

![BLOG-3278 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46DJMKR2Y3SATEJPH3N13P.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////+/z77e/w5ejr6evw8PL28fLz6uvq/////P7+6e3y3OLt3+Xy6e757vH27O3t////////5+z21d7x1+H25Oz87fL67vDx////////6vD81uH21+P75e7/8PX/8/X2////////8/j/4uv84+3/7/f/9/z/+Pr7////////////8/j/9fv//f///////v//////////////////////////////////////////////////////////////////)

W ciągu ostatnich nieco ponad dwóch kwartałów podjęliśmy intensywne działania inżynieryjne (wewnętrznie nazwane kodowo „[ _Code Orange: Fail Small_](https://blog.cloudflare.com/fail-small-resilience-plan/)”) skoncentrowane na zwiększeniu odporności, bezpieczeństwa i niezawodności infrastruktury Cloudflare dla każdego klienta.

Na początku tego miesiąca zespół Cloudflare zakończył te prace.

Choć zwiększanie odporności nigdy nie będzie „zadaniem zakończonym” i zawsze pozostanie najwyższym priorytetem w całym naszym cyklu rozwoju, ukończyliśmy już prace, które pozwoliłyby uniknąć globalnych awarii z [_18 listopada_](https://blog.cloudflare.com/18-november-2025-outage/) i [_5 grudnia 2025 roku_](https://blog.cloudflare.com/5-december-2025-outage/).

Prace te koncentrowały się na kilku kluczowych obszarach: bezpieczniejszych zmianach konfiguracji, ograniczaniu skutków awarii oraz przeglądzie naszych procedur awaryjnych „break glass” i zarządzania incydentami. Wprowadziliśmy również środki zapobiegające narastaniu odchyleń i regresjom w czasie oraz usprawniliśmy sposób komunikacji z klientami podczas awarii.

W tym miejscu szczegółowo wyjaśniamy, co wdrożyliśmy i co to oznacza w praktyce.

### Bezpieczniejsze zmiany konfiguracji

 _**Co to oznacza w praktyce** : w większości przypadków wewnętrzne zmiany konfiguracji Cloudflare nie trafiają już natychmiast do naszej sieci, lecz są wdrażane stopniowo z monitorowaniem kondycji w czasie rzeczywistym. Dzięki temu nasze narzędzia obserwowalności mogą wykrywać problemy i wycofywać błędne zmiany, zanim wpłyną na Twój ruch._

Aby wykrywać potencjalnie niebezpieczne wdrożenia, zanim trafią na etap produkcyjny, zidentyfikowaliśmy potoki konfiguracji wysokiego ryzyka i stworzyliśmy nowe narzędzia do lepszego zarządzania zmianami konfiguracji.

W przypadku produktów działających w naszej sieci, przetwarzających ruch klientów i otrzymujących zmiany konfiguracji, nie wdrażamy już tych zmian natychmiast w całej sieci. Zamiast tego odpowiednie zespoły przyjęły metodologię „wdrożeń zależnych od stanu kondycji” (tę samą, [_której używamy przy wydawaniu oprogramowania_](https://blog.cloudflare.com/safe-change-at-any-scale/)) dla wszystkich wdrożeń konfiguracji. Obejmuje to między innymi zespoły produktowe, których bezpośrednio dotknęły incydenty.

Kluczową rolę odgrywa tu nowy komponent wewnętrzny, który nazywamy Snapstone i który stworzyliśmy, aby objąć zmiany konfiguracji wdrożeniami zależnymi od stanu kondycji. Snapstone to system, który łączy zmianę konfiguracji w pakiet, a następnie umożliwia jej stopniowe wdrażanie zgodnie z zasadami wdrożeń zależnych od stanu kondycji. Przed wprowadzeniem Snapstone zastosowanie tej metodologii do konfiguracji było możliwe, ale trudne. Wymagało to znacznego nakładu pracy ze strony poszczególnych zespołów i nie było konsekwentnie stosowane w całej sieci. Snapstone wypełnia tę lukę, domyślnie zapewniając ujednolicony sposób wprowadzania stopniowych wdrożeń, monitorowania kondycji w czasie rzeczywistym oraz automatycznego wycofywania zmian we wdrożeniach konfiguracji.

Szczególną siłą Snapstone jest jego elastyczność. Snapstone nie jest poprawką przygotowaną z myślą o konkretnych wcześniejszych awariach, lecz umożliwia zespołom dynamiczne definiowanie dowolnej jednostki konfiguracji wymagającej wdrożeń zależnych od stanu kondycji, bez względu na to, czy jest to plik danych podobny do tego, który spowodował [_awarię z 18 listopada_](https://blog.cloudflare.com/18-november-2025-outage/), czy flaga kontrolna w naszym globalnym systemie konfiguracji, taka jak ta związana z [_awarią z 5 grudnia_](https://blog.cloudflare.com/5-december-2025-outage/). Zespoły tworzą te jednostki konfiguracji na żądanie, a Snapstone zapewnia ich bezpieczne wdrażanie wszędzie tam, gdzie są używane.

Daje nam to coś, czego wcześniej nie mieliśmy: gdy przegląd ryzyka lub doświadczenie operacyjne wskaże niebezpieczny wzorzec konfiguracji, rozwiązanie jest proste: wystarczy włączyć go do Snapstone, a ten wzorzec natychmiast dziedziczy bezpieczny mechanizm wdrażania. 

### Ograniczanie skutków awarii

 _**Co to oznacza w praktyce** : jeśli w naszej sieci zostanie wykryty problem, nasze systemy będą teraz degradować się w bardziej kontrolowany sposób. Znacząco ogranicza to potencjalny zasięg oddziaływania problemu, aby zapewnić dostarczanie Twojego ruchu nawet w najgorszych scenariuszach._

Zespoły produktowe starannie przeanalizowały, zarówno ręcznie, jak i programowo, potencjalne tryby awarii produktów krytycznych dla obsługi ruchu klientów. Usunęły niekluczowe zależności wykonywane w czasie działania i wdrożyły lepsze tryby obsługi awarii. Tam, gdzie to możliwe, będziemy teraz używać ostatniej znanej poprawnej konfiguracji („fail stale”), a jeśli nie będzie to możliwe, przeanalizujemy każdy przypadek awarii i wdrożymy mechanizmy „fail open” lub „fail close”, w zależności od tego, czy obsługa ruchu z ograniczoną funkcjonalnością jest lepsza niż brak obsługi ruchu.

Zobaczmy na przykładzie, jak to działa. Awaria z listopada 2025 roku została wywołana nieudanym wdrożeniem klasyfikatora uczenia maszynowego do wykrywania w ramach usługi Bot Management. Zgodnie z naszymi nowymi procedurami, gdyby ponownie wygenerowano dane, których nasz system nie mógłby odczytać, system odmówiłby użycia zaktualizowanej konfiguracji i zamiast tego zastosowałby starą. Gdyby z jakiegoś powodu stara konfiguracja była niedostępna, system przeszedłby w tryb „fail open”, aby zapewnić dalszą obsługę produkcyjnego ruchu klientów, co jest znacznie lepszym rozwiązaniem niż przestój.

W rezultacie, gdyby ta sama zmiana w usłudze Bot Management, która spowodowała awarię w listopadzie, została wprowadzona teraz, system wykryłby problem na wczesnym etapie wdrożenia, zanim wpłynąłby on na więcej niż niewielki odsetek ruchu.

Zaczęliśmy również dalej segmentować nasz system, tak aby niezależne kopie usług obsługiwały różne kohorty ruchu. Cloudflare już dziś wykorzystuje te kohorty klientów do ograniczania zasięgu oddziaływania awarii za pomocą technik zarządzania ruchem, a dodatkowe prace nad segmentacją procesów zapewnią nam w przyszłości istotne możliwości zwiększania niezawodności. 

Na przykład system środowiska wykonawczego Workers jest podzielony na wiele niezależnych usług obsługujących różne kohorty ruchu, z których jedna obsługuje wyłącznie ruch naszych klientów korzystających z planu Free. Zmiany są wdrażane w tych segmentach według kohort klientów, zaczynając od klientów korzystających z planu Free. Aktualizacje również wysyłamy szybciej i częściej do najmniej krytycznych segmentów, a wolniej — do najbardziej krytycznych.

W rezultacie, gdyby zmiana została wdrożona w systemie środowiska wykonawczego Workers i zakłóciła ruch, obecnie wpłynęłaby tylko na niewielki odsetek naszych klientów korzystających z planu Free, zanim zostałaby automatycznie wykryta i wycofana.

Pozostając przy systemie środowiska wykonawczego Workers jako przykładzie, w ciągu siedmiu dni na początku tego miesiąca proces wdrożeniowy został uruchomiony ponad 50 razy. Można zaobserwować, jak każde z nich przebiega „falami” w miarę propagacji zmiany do brzegu sieci, często równolegle z kolejnymi i wcześniejszymi wydaniami:

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Edge-worker module change deployment graph -- over 50 changes in less than a week.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4526WAP987XRN6NCSE4DBD.png&w=715&h=476&f=webp&fit=cover&position=center)

Pracujemy nad rozszerzeniem tego wzorca wdrażania na znacznie większą liczbę naszych systemów w przyszłości.

### Zmienione procedury awaryjne „break glass” i zarządzania incydentami

 _**Co to oznacza w praktyce** : jeśli incydent jednak wystąpi, dysponujemy narzędziami i zespołami, które pozwalają komunikować się jaśniej i rozwiązywać problem szybciej, minimalizując przestoje._

Cloudflare bazuje na własnych rozwiązaniach. Korzystamy z własnych produktów Zero Trust, aby zabezpieczać naszą infrastrukturę, ale tworzy to zależność: jeśli awaria obejmująca całą sieć wpłynie na te narzędzia, tracimy właśnie te ścieżki dostępu, których potrzebujemy, aby je naprawić. Przed rozpoczęciem inicjatywy Code Orange nasze awaryjne ścieżki dostępu „break glass” były ograniczone do niewielkiej grupy osób i zapewniały ograniczony dostęp do narzędzi. Potrzebne było szersze udostępnienie tych narzędzi i ścieżek dostępu na czas awarii.

Aby rozwiązać ten problem, przeprowadziliśmy kompleksowy audyt narzędzi niezbędnych do zapewnienia widoczności systemów, debugowania i wprowadzania zmian produkcyjnych. Ostatecznie opracowaliśmy zapasowe ścieżki autoryzacji dla 18 kluczowych usług, wspierane przez nowe skrypty awaryjne i serwery proxy.

W ramach całego programu Code Orange przeszliśmy od teorii do praktyki. Po ćwiczeniach w małych zespołach 7 kwietnia 2026 roku przeprowadziliśmy ogólnofirmowy test inżynieryjny z udziałem ponad 200 członków zespołu. Automatyzacja utrzymuje sprawność tych ścieżek dostępu, ale tego typu ćwiczenia zapewniają inżynierom pamięć proceduralną potrzebną do korzystania z nich pod presją.

Działania te koncentrowały się również na przepływie informacji. Gdy wewnętrzna widoczność zostaje zakłócona, nasze reagowanie na incydenty spowalnia, a zdolność komunikowania się ze światem zewnętrznym pogarsza się. W przeszłości obserwacje techniczne dokonywane w trakcie incydentu nie zawsze przekładały się na jasne aktualizacje dla klientów.

Aby wypełnić tę lukę, powołaliśmy do życia dedykowany zespół komunikacyjny, który podczas poważnych zdarzeń ściśle współpracuje z osobami odpowiedzialnymi za reagowanie na incydenty. Tak jak nasi inżynierowie ćwiczyli procedury awaryjne „break glass”, zespół ten wykorzystał program Code Orange do przećwiczenia usprawniania częstotliwości i przejrzystości aktualizacji dla klientów. Zapewniając zarówno narzędzia pozwalające obserwować sytuację, jak i strukturę umożliwiającą komunikację, możemy szybciej reagować na incydenty i usuwać ich skutki oraz lepiej informować klientów.

### Sformalizowaliśmy wprowadzone usprawnienia

 _**Co to oznacza w praktyce** : będziemy pamiętać o wnioskach wyciągniętych z naszych incydentów i sformalizowaliśmy już sposoby reagowania na podobne sytuacje. Nasza sieć będzie tylko coraz bardziej odporna._

Aby z czasem uniknąć narastania odchyleń i ponownego wprowadzania regresji do prac wykonanych w ramach Code Orange, zespół stworzył wewnętrzny kodeks, który utrwala wszystkie nasze wytyczne w formie jasnych i zwięzłych reguł.

Kodeks jest teraz obowiązkowy dla wszystkich zespołów inżynieryjnych i produktowych oraz stał się centralnym elementem wewnętrznych procedur Cloudflare. Zawarte w nim reguły są egzekwowane za pomocą przeglądów kodu wspieranych przez SI, które automatycznie wskazują wszystkie przypadki mogące odbiegać od wytycznych i wymagające dodatkowych przeglądów wykonywanych ręcznie. Jest to stosowane bez wyjątku w całej naszej bazie kodu. Cel jest prosty: zbudować pamięć instytucjonalną, która sama egzekwuje swoje zasady.

Awarie w listopadzie i grudniu łączył wspólny tryb — kod, który zakładał, że dane wejściowe zawsze będą poprawne, bez mechanizmu kontrolowanej degradacji działania, gdy to założenie okazało się błędne. Usługa napisana w języku Rust wywołała metodę `.unwrap()` zamiast obsłużyć błąd, a kod Lua odwołał się do nieistniejącego obiektu. Obydwu wzorcom można zapobiec, jeśli wnioski zostaną utrwalone i będą egzekwowane.

Kodeks jest częścią naszej odpowiedzi. To żywe repozytorium standardów inżynieryjnych tworzonych przez ekspertów dziedzinowych w ramach naszego procesu Request For Comments (RFC), a następnie sprowadzanych do praktycznych reguł. Najlepsze praktyki, które wcześniej funkcjonowały w głowach starszych inżynierów albo były odkrywane dopiero po incydencie, stają się teraz wspólną wiedzą dostępną dla wszystkich. Każda reguła ma prosty format: „jeśli potrzebujesz X, użyj Y”, wraz z linkiem do dokumentu RFC wyjaśniającego dlaczego.

Na przykład jeden z dokumentów RFC stanowi teraz: „Nie używaj metody `.unwrap()` poza testami i `build.rs.`”. Inny utrwala szerszą zasadę: „Przed rozpoczęciem przetwarzania usługi MUSZĄ sprawdzać, czy zależności nadrzędne są w oczekiwanym stanie”.

Gdyby te reguły były egzekwowane wcześniej, zmiany odpowiedzialne za awarie w listopadzie i grudniu zostałyby odrzucone już na etapie zgłoszeń do scalenia kodu (merge requests), zamiast doprowadzić do globalnych incydentów.

Reguły bez egzekwowania są jedynie sugestiami. Kodeks integruje się z agentami wspieranymi przez SI na każdym etapie cyklu życia tworzenia oprogramowania, od przeglądu projektu, przez wdrożenie, po analizę incydentów. Przenosi to egzekwowanie zasad w lewo, od „globalnej awarii” do „odrzuconego zgłoszenia do scalenia kodu”. Zasięg oddziaływania naruszenia kurczy się z milionów objętych nim żądań do pojedynczego programisty otrzymującego praktyczną informację zwrotną, zanim jego kod kiedykolwiek trafi na produkcję.

Kodeks jest stale rozwijanym dokumentem i z czasem będzie systematycznie udoskonalany. Eksperci dziedzinowi tworzą dokumenty RFC, aby kodyfikować najlepsze praktyki. Incydenty ujawniają luki, które stają się podstawą nowych dokumentów RFC. Każdy zatwierdzony dokument RFC generuje reguły kodeksu, które następnie zasilają agenty sprawdzające kolejne zgłoszenie do scalenia kodu. To mechanizm samonapędzający się: wiedza ekspercka przekształca się w standardy, standardy w egzekwowanie zasad, a egzekwowanie zasad podnosi poprzeczkę dla wszystkich.

### Nie chodzi tylko o kod – kluczowa jest komunikacja

 _**Co to oznacza w praktyce** : transparentność jest dla nas ważna. Jeśli coś pójdzie nie tak, zobowiązujemy się informować na bieżąco o każdym etapie działań, aby można było skupić się na tym, co najważniejsze._

Globalne awarie skłoniły nas do przeglądu kluczowych procesów i podejść kulturowych, wykraczających nawet poza inżynierię i rozwój produktów. W ramach szerszych inicjatyw Code Orange wprowadziliśmy dodatkowe cele dotyczące poziomu usług (SLO) dla wszystkich naszych usług, wymusiliśmy stosowanie globalnego rejestru zmian, wdrożyliśmy wszystkie zespoły do naszego systemu koordynacji prac serwisowych oraz zwiększyliśmy przejrzystość w całej firmie w zakresie zaległych zgłoszeń dotyczących działań zapobiegających incydentom. 

Usprawniliśmy również sposób komunikacji z klientami podczas awarii. Naszym celem jest informowanie o problemie natychmiast po jego potwierdzeniu, zanim stanie się on zauważalny. Zanim opóźnienie lub błąd staną się zauważalne, naszym celem jest, aby aktualizacja już czekała w powiadomieniach.

Podczas aktywnego incydentu przekazujemy teraz aktualizacje w przewidywalnych odstępach, np. co 30 lub 60 minut, nawet jeśli aktualizacja brzmi po prostu: „Nadal testujemy poprawkę, brak nowych zmian”. Dzięki temu można planować dzień, zamiast stale odświeżać stronę statusu.

Nasza praca nie kończy się, gdy status wraca do normy. Publikujemy szczegółowe analizy post-mortem wyjaśniające, co się wydarzyło, dlaczego do tego doszło i jakie konkretne zmiany strukturalne wprowadzamy, aby zapobiec ponownemu wystąpieniu danej sytuacji.

### Ta inicjatywa została zakończona, lecz nasze prace nad odpornością nigdy się nie kończą.

Bardzo poważnie podchodzimy do tych incydentów i przyjęliśmy zasadę współodpowiedzialności w całej organizacji Cloudflare, prosząc każdy zespół o odpowiedź na pytanie: co można było zrobić lepiej? To wyznaczyło kierunek prac, które prowadziliśmy przez ostatnie dwa kwartały.

Choć te prace nigdy tak naprawdę się nie kończą, jesteśmy przekonani, że znajdujemy się dziś w znacznie lepszej sytuacji, a firma Cloudflare jest dzięki nim znacznie silniejsza.

Na tej stronie

Dyskutuj online

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fcode-orange-fail-small-complete%2F&t=Inicjatywa%20Code%20Orange%3A%20Fail%20Small%20dobieg%C5%82a%20ko%C5%84ca%2C%20a%20jej%20rezultatem%20jest%20silniejsza%20sie%C4%87%20Cloudflare.)[](https://x.com/intent/post?text=Inicjatywa+Code+Orange%3A+Fail+Small+dobieg%C5%82a+ko%C5%84ca%2C+a+jej+rezultatem+jest+silniejsza+sie%C4%87+Cloudflare.&url=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fcode-orange-fail-small-complete%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fcode-orange-fail-small-complete%2F)[](https://bsky.app/intent/compose?text=Inicjatywa+Code+Orange%3A+Fail+Small+dobieg%C5%82a+ko%C5%84ca%2C+a+jej+rezultatem+jest+silniejsza+sie%C4%87+Cloudflare.+https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fcode-orange-fail-small-complete%2F)[](https://mastodonshare.com/?text=Inicjatywa+Code+Orange%3A+Fail+Small+dobieg%C5%82a+ko%C5%84ca%2C+a+jej+rezultatem+jest+silniejsza+sie%C4%87+Cloudflare.&url=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fcode-orange-fail-small-complete%2F)[](https://www.threads.net/intent/post?text=Inicjatywa+Code+Orange%3A+Fail+Small+dobieg%C5%82a+ko%C5%84ca%2C+a+jej+rezultatem+jest+silniejsza+sie%C4%87+Cloudflare.+https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fcode-orange-fail-small-complete%2F)

## Powiązane tagi

[Analiza przypadku](https://blog.cloudflare.com/pl-pl/tag/post-mortem/)[Awaria](https://blog.cloudflare.com/pl-pl/tag/outage/)[Code Orange](https://blog.cloudflare.com/pl-pl/tag/code-orange/)

Śledź nas w mediach społecznościowych

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Zapisz się, aby otrzymywać powiadomienia o nowych postach

Adres e-mail

Nigdy nie udostępnimy Twojego adresu e-mail.

Subskrybuj

Dziękujemy za subskrypcję! Sprawdź skrzynkę odbiorczą, aby ją potwierdzić.
