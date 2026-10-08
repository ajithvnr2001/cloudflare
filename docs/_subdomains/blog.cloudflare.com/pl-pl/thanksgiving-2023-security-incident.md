---
url: https://blog.cloudflare.com/pl-pl/thanksgiving-2023-security-incident/
title: Incydent bezpiecze\u0144stwa w \u015awi\u0119to Dzi\u0119kczynienia 2023 | Blog Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:37:30.172952+00:00
---

# Incydent bezpieczeństwa w Święto Dziękczynienia 2023 | Blog Cloudflare

> Source: https://blog.cloudflare.com/pl-pl/thanksgiving-2023-security-incident/

[Blog](https://blog.cloudflare.com/pl-pl/)

[Bezpieczeństwo](https://blog.cloudflare.com/pl-pl/tag/security/)

1 tagówPokaż 1 tagów

  * Tagi wpisu
  * [Bezpieczeństwo](https://blog.cloudflare.com/pl-pl/tag/security/)
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



[Bezpieczeństwo](https://blog.cloudflare.com/pl-pl/tag/security/)

1 lutego 2024

# Incydent bezpieczeństwa w Święto Dziękczynienia 2023

![Matthew Prince](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44KQ4Z9PY1TR0ERGW96HZR.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![John Graham-Cumming](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47SEV81RPKWD16DDB0V03K.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Grant Bourzikas](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46SJJRBDYVMHZKVGKTMJ08.png&w=64&h=64&f=webp&fit=cover&position=center)

[Matthew Prince](https://blog.cloudflare.com/pl-pl/author/matthew-prince/), [John Graham-Cumming](https://blog.cloudflare.com/pl-pl/author/john-graham-cumming/) i [Grant Bourzikas](https://blog.cloudflare.com/pl-pl/author/grant/)

14 min czytania

KOPIUJ URL

Ten wpis jest również dostępny w [English](https://blog.cloudflare.com/thanksgiving-2023-security-incident/), [Deutsch](https://blog.cloudflare.com/de-de/thanksgiving-2023-security-incident/), [Español](https://blog.cloudflare.com/es-es/thanksgiving-2023-security-incident/), [Français](https://blog.cloudflare.com/fr-fr/thanksgiving-2023-security-incident/), [日本語](https://blog.cloudflare.com/ja-jp/thanksgiving-2023-security-incident/), [한국어](https://blog.cloudflare.com/ko-kr/thanksgiving-2023-security-incident/), [繁體中文](https://blog.cloudflare.com/zh-tw/thanksgiving-2023-security-incident/), [简体中文](https://blog.cloudflare.com/zh-cn/thanksgiving-2023-security-incident/) i [Português](https://blog.cloudflare.com/pt-br/thanksgiving-2023-security-incident/).

![Thanksgiving 2023 security incident Meta Image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW466GXW4XNNS66SC21Y79M5.png&w=1200&h=628&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA//////769vTs7+3l7e3p7u/v7e3t6Ojl/f7/+/v79fPt7Orl4OLo2N/u2N/t3ODl9/v/+Pn99vTv6ujn1Nnqwc/wwtHuz9nm+Pz/+vz/+/j17uzt09rwu831vM70ztrs///////////9+Pb24uf5ztv+zdz82+X1////////////////9/n/7PP/6vL/7/X+////////////////////////////////////////////////////////////////)

W Święto Dziękczynienia, 23 listopada 2023 roku, Cloudflare wykryła aktywność cyberprzestępcy na naszym samodzielnie hostowanym serwerze Atlassian. Nasz zespół ds. bezpieczeństwa niezwłocznie rozpoczął dochodzenie i odciął cyberprzestępcy dostęp, a w niedzielę, 26 listopada, zleciliśmy technikom CrowdStrike przeprowadzenie własnej niezależnej analizy.

Wczoraj firma CrowdStrike zakończyła swoje dochodzenie, a my publikujemy niniejszy wpis na blogu, aby omówić szczegóły tego incydentu bezpieczeństwa.

Chcemy podkreślić naszym klientom, że to zdarzenie nie miało wpływu na żadne dane dotyczące klientów Cloudflare ani na nasze systemy. Dzięki naszym środkom kontroli dostępu, regułom zapory oraz stosowaniu silnych kluczy bezpieczeństwa, co wymuszają nasze własne narzędzia Zero Trust, możliwości wykonywania przez cyberprzestępcę ruchów bocznych były ograniczone. W incydent nie były zamieszane żadne usługi, ani nie wprowadzono żadnych zmian w naszych globalnych systemach sieciowych bądź w konfiguracji. To właśnie cecha architektury typu Zero Trust — podobnie jak w przypadku grodzi na statku, skutki ataku w jednym systemie są ograniczone, aby nie narażać całej organizacji.

Między 14 a 17 listopada cyberprzestępca przeprowadził rozpoznanie, a następnie uzyskał dostęp do naszych wewnętrznych stron wiki (korzystających z narzędzia Atlassian Confluence) oraz naszej bazy danych dotyczącej błędów (Atlassian Jira). W dniach 20 i 21 listopada zaobserwowaliśmy dodatkowy dostęp wskazujący, że cyberprzestępca mógł powrócić w celu przetestowania dostępu i zapewnienia sobie łączności.

Następnie powrócił 22 listopada i zapewnił sobie stały dostęp do naszego serwera Atlassian, używając aplikacji ScriptRunner for Jira, uzyskał dostęp do naszego systemu zarządzania kodem źródłowym (używającego narzędzia Atlassian Bitbucket) oraz bez powodzenia próbował zdobyć dostęp do serwera konsolowego z dostępem do centrum danych Cloudflare w São Paulo, w Brazylii, które nie zostało jeszcze oddane do eksploatacji.

Dokonał tego, używając jednego tokena dostępu oraz trzech poświadczeń kont usług, które zostały przejęte, a których nie zmieniliśmy po [pokonaniu zabezpieczeń systemów Okta w październiku 2023 roku](https://blog.cloudflare.com/how-cloudflare-mitigated-yet-another-okta-compromise). Wszystkie próby dostępu i połączenia cyberprzestępcy zakończyły się 24 listopada, a firma CrowdStrike potwierdziła, że ostatnie dowody jego aktywności wykryto 24 listopada o godzinie 10:44.

(W całym tym wpisie na blogu wszystkie daty i godziny są podane w czasie uniwersalnym UTC).

Chociaż rozumiemy, że wpływ operacyjny incydentu był niezwykle ograniczony, potraktowaliśmy to zdarzenie bardzo poważnie, ponieważ cyberprzestępca użył skradzionych poświadczeń, aby uzyskać dostęp do naszego serwera Atlassian, jak również zdobył dostęp do pewnej dokumentacji oraz ograniczonej ilości kodu źródłowego. Na podstawie współpracy z kolegami z branży i władzami uważamy, że atak ten został przeprowadzony na zlecenie państwa narodowego z zamiarem uzyskania trwałego i powszechnego dostępu do globalnej sieci Cloudflare.

### Naprawcze i wzmacniające działania zespołu „Code Red”

24 listopada, po pozbyciu się cyberprzestępcy z naszego środowiska, nasz zespół ds. bezpieczeństwa zaangażował wszystkie niezbędne osoby z całej firmy w celu zbadania wtargnięcia i upewnienia się, że cyberprzestępca został całkowicie pozbawiony dostępu do naszych systemów, a także w celu poznania skali uzyskanego dostępu lub prób jego uzyskania.

Następnie, od 27 listopada, przekierowaliśmy wysiłki dużej części personelu technicznego Cloudflare (w ramach zespołu ds. bezpieczeństwa i poza nim) do pracy nad jednorazowym projektem o nazwie „Code Red”. Skupiliśmy się na wzmocnieniu, weryfikacji i naprawie wszelkich mechanizmów kontrolnych w naszym środowisku, aby zabezpieczyć nas przed przyszłymi wtargnięciami oraz potwierdzić, że cyberprzestępca nie mógł uzyskać dostępu do naszego środowiska. Ponadto kontynuowaliśmy dochodzenie dotyczące każdego systemu, konta i dziennika, aby upewnić się, że cyberprzestępca nie miał stałego dostępu oraz że w pełni zrozumieliśmy, które systemy zostały zinfiltrowane i do których próbowano uzyskać dostęp.

Firma CrowdStrike dokonała niezależnej oceny zakresu i zasięgu działalności cyberprzestępcy, w szczególności zaś przeprowadziła poszukiwania jakichkolwiek dowodów na to, że nadal infiltruje on nasze systemy. Dochodzenie przeprowadzone przez CrowdStrike stanowiło cenne potwierdzenie i wsparcie dla naszego śledztwa, lecz nie ujawniło żadnych aktywności, które mogliśmy przeoczyć. Ten wpis na blogu szczegółowo opisuje wszystko, co zostało odkryte przez firmy Cloudflare i CrowdStrike na temat działalności cyberprzestępcy.

Jedynym systemem produkcyjnym, do którego cyberprzestępca mógł uzyskać dostęp za pomocą skradzionych poświadczeń, było nasze środowisko Atlassian. Po analizie stron wiki, do których uzyskał dostęp, zgłoszeń w bazie danych dotyczącej błędów oraz repozytoriów kodu źródłowego można przypuszczać, że szukał on informacji na temat architektury, zabezpieczeń i zarządzania naszą siecią globalną, niewątpliwie z zamiarem zdobycia lepszego punktu zaczepienia. Z tego względu postanowiliśmy podjąć ogromny wysiłek na rzecz dodatkowego wzmocnienia naszych protokołów bezpieczeństwa, aby uniemożliwić cyberprzestępcy uzyskanie takiego punktu zaczepienia w sytuacji, gdybyśmy przeoczyli coś w naszych plikach dziennika.

Naszym celem było uniemożliwienie atakującemu wykorzystania informacji technicznych na temat działania naszej sieci jako sposobu na ponowne włamanie. Mimo że wierzyliśmy, a później potwierdziliśmy, że atakujący miał ograniczony dostęp, podjęliśmy kompleksowe działania, aby zmienić każde poświadczenie produkcyjne (ponad 5000 indywidualnych poświadczeń) oraz fizycznie oddzielić systemy testowe i pomostowe. Co więcej, przeprowadzono triaże kryminalistyczne w odniesieniu do 4893 systemów, a także usunięto całe oprogramowanie, ponownie je zainstalowano i uruchomiono na każdym komputerze w naszej sieci globalnej, co w szczególności dotyczyło wszystkich systemów, do których cyberprzestępca miał dostęp, oraz wszystkich produktów Atlassian (Jira, Confluence i Bitbucket).

Cyberprzestępca próbował również uzyskać dostęp do serwera konsolowego w naszym nowym, nieoddanym jeszcze do eksploatacji centrum danych w São Paulo. Wszystkie próby uzyskania dostępu zakończyły się niepowodzeniem. Aby zapewnić pełne bezpieczeństwo tym systemom, sprzęt w brazylijskim centrum danych został zwrócony producentom. Technicy producentów zbadali wszystkie nasze systemy, aby upewnić się, że nie uzyskano dostępu ani trwałej obecności. Niczego nie znaleziono, ale mimo to wymieniliśmy sprzęt.

Poszukiwaliśmy również niezaktualizowanych pakietów oprogramowania, potencjalnie utworzonych kont użytkownika oraz nieużywanych aktywnych kont pracowników. Zabraliśmy się za szukanie sekretów, które mogły zostać pozostawione w zgłoszeniach Jira lub kodzie źródłowym, jak również przeanalizowaliśmy i usunęliśmy wszystkie przesłane do wiki pliki HAR na wypadek, gdyby zawierały jakiekolwiek tokeny. W razie jakichkolwiek wątpliwości zakładaliśmy najgorszy scenariusz i wprowadzaliśmy zmiany, aby zapewnić, że wszystko, do czego cyberprzestępca mógł uzyskać dostęp, nie będzie już używane i tym samym nie będzie już dla niego cenne.

Wszyscy członkowie zespołu byli zachęcani do wskazywania obszarów, które mogły zostać zinfiltrowane przez cyberprzestępcę, abyśmy mogli zbadać pliki dziennika i określić zakres takiego nieuprawnionego dostępu. Celem uwzględnienia w tych pracach tak wielu osób z całej firmy było przetrząśnięcie każdego zakamarka w poszukiwaniu dowodów na dostęp lub zmian, które trzeba wprowadzić, aby poprawić bezpieczeństwo.

Bezpośrednie działania zespołu „Code Red” zakończyły się 5 stycznia, lecz prace dotyczące m.in. zarządzania poświadczeniami, wzmacniania oprogramowania, zarządzania podatnościami czy dodatkowych alertów są kontynuowane w całej firmie.

### Oś czasu ataku

Atak rozpoczął się w październiku od pokonania zabezpieczeń systemów Okta, ale dopiero od połowy listopada cyberprzestępca zaczął atakować nasze systemy z wykorzystaniem poświadczeń zdobytych podczas tego naruszenia.

Na poniższej osi czasu przedstawiono najważniejsze zdarzenia:

### 18 października — pokonanie zabezpieczeń systemów Okta

[Pisaliśmy już o tym wcześniej](https://blog.cloudflare.com/how-cloudflare-mitigated-yet-another-okta-compromise), ale, mówiąc w skrócie, staliśmy się (po raz drugi) ofiarami pokonania zabezpieczeń systemów Okta, co skutkowało uzyskaniem przez cyberprzestępcę dostępu do zestawu poświadczeń. Wszystkie te poświadczenia miały zostać zmienione.

Niestety, nie udało nam się zmienić jednego tokena usługi oraz trzech kont usług (spośród tysięcy) dotyczących poświadczeń, które wyciekły z chwilą pokonania zabezpieczeń systemów Okta.

Jednym z nich był token usługi Moveworks, który zapewniał dostęp zdalny do naszego systemu Atlassian. Drugim poświadczeniem było konto usług używane przez aplikację Smartsheet opartą na rozwiązaniu SaaS, które miało dostęp administracyjny do naszej instancji bazy danych Atlassian Jira, trzecie konto było kontem usług narzędzia Bitbucket używanym do dostępu do naszego systemu zarządzania kodem źródłowym, natomiast czwarte było środowisko AWS niemające dostępu do sieci globalnej i niezawierające żadnych danych klientów ani danych wrażliwych.

Jeden token usługi i trzy konta nie zostały zmienione, ponieważ błędnie uznano, że nie są używane. Właśnie przez tę pomyłkę cyberprzestępca po raz pierwszy dostał się do naszych systemów i uzyskał trwały dostęp do naszych produktów Atlassian. Należy zauważyć, że w żadnym razie nie był to błąd AWS, Moveworks ani Smartsheet. Były to po prostu poświadczenia, których nie zmieniliśmy.

### 14 listopada, godz. 09:22:49 — cyberprzestępca rozpoczyna sondowanie

Nasze dzienniki pokazują, że 14 listopada cyberprzestępca rozpoczął sondowanie i przeprowadzanie rozpoznania naszych systemów, szukając sposobu wykorzystania poświadczeń oraz wykrycia dostępnych systemów. Podejmował próby zalogowania się do naszej instancji Okta oraz uzyskania dostępu do pulpitu nawigacyjnego Cloudflare, ale w obydwu przypadkach spotkał się z odmową dostępu.

Cyberprzestępca uzyskał ponadto dostęp do środowiska AWS wykorzystywanego do obsługi rynku Cloudflare Apps. To środowisko było posegmentowane, bez dostępu do sieci globalnej lub danych dotyczących klientów. Konto usługi zapewniające dostęp do tego środowiska zostało unieważnione, a następnie przeprowadzono weryfikację integralności tego środowiska.

### 15 listopada, godz. 16:28:38 — cyberprzestępca uzyskuje dostęp do usług Atlassian

15 listopada cyberprzestępca uzyskał pomyślnie dostęp do Atlassian Jira i Confluence, wykorzystując token usługi Moveworks do uwierzytelnienia przejścia przez naszą bramę, a następnie użył konta usług Smartsheet, aby uzyskać dostęp do pakietu Atlassian. Następnego dnia zaczął szukać informacji o konfiguracji i zarządzaniu naszą siecią globalną oraz uzyskał dostęp do różnych zgłoszeń Jira.

Na stronach wiki cyberprzestępca wyszukiwał takie frazy jak „remote access”, „secret”, „client-secret”, „openconnect”, „cloudflared” i „token”. Uzyskał dostęp do 36 zgłoszeń Jira (z łącznej liczby 2059357 zgłoszeń) oraz 202 stron wiki (z łącznej liczby 14099 stron).

Cyberprzestępca uzyskał dostęp do zgłoszeń Jira dotyczących zarządzania podatnościami, rotacji sekretów, obejścia MFA, dostępu do sieci, a nawet naszej reakcji na incydent dotyczący platformy Okta.

Przeszukiwania wiki i strony, do których uzyskano dostęp, wskazują, że cyberprzestępca był bardzo zainteresowany wszelkimi aspektami dostępu do naszych systemów: resetowaniem haseł, dostępem zdalnym, konfiguracją, naszym wykorzystaniem produktu Salt, lecz jego celem nie były dane ani konfiguracje dotyczące klientów.

### 16 listopada, godz. 14:36:37 — cyberprzestępca tworzy konto użytkownika Atlassian

Cyberprzestępca wykorzystał poświadczenie Smartsheet do utworzenia konta Atlassian, które wyglądało jak zwykłe konto użytkownika Cloudflare. Dodał tego użytkownika do wielu grup w ramach Atlassian, aby zapewnić sobie trwały dostęp do tego środowiska na wypadek usunięcia konta usług Smartsheet.

### Od 17 listopada, godz. 14:33:52 do 20 listopada, godz. 09:26:53 — cyberprzestępca czasowo zaprzestaje prób uzyskania dostępu do systemów Cloudflare

W tym okresie atakujący zrobił przerwę w przeprowadzaniu prób uzyskania dostępu do naszych systemów (poza krótkim, pozornym testowaniem, czy nadal ma dostęp), a następnie powrócił tuż przed Świętem Dziękczynienia.

### 22 listopada, godz. 14:18:22 — cyberprzestępca zyskuje trwały dostęp

Ponieważ konto usług Smartsheet miało dostęp administracyjny do bazy danych Atlassian Jira, cyberprzestępca był w stanie zainstalować narzędzie Sliver Adversary Emulation Framework, które jest powszechnie wykorzystywane przez zespoły testujące zabezpieczenia oraz atakujących do zapewnienia sobie łączności C2 (command and control) pozwalającej uzyskać trwały i ukryty dostęp do komputera, na którym jest ono zainstalowane. Narzędzie Sliver zainstalowano przy użyciu wtyczki ScriptRunner for Jira.

To zapewniło mu ciągły dostęp do serwera Atlassian, którego używał przy próbach ruchu bocznego. Dzięki temu dostępowi cyberprzestępca próbował uzyskać dostęp do nieprodukcyjnego serwera konsolowego w naszym centrum danych w São Paulo, w Brazylii, a powodem tego była nieegzekwowana lista kontroli dostępu (ACL). Po odmowie dostępu nie mógł się on przedostać do sieci globalnej.

W ciągu następnego dnia cyberprzestępca przejrzał 120 repozytoriów kodu (z łącznej liczby 11904 repozytoriów). W ramach tej grupy wykorzystał funkcję archiwizacji git narzędzia Atlassian Bitbucket w odniesieniu do 76 repozytoriów, aby pobrać je na serwer Atlassian. Mimo że nie byliśmy w stanie potwierdzić, czy zostały one poddane eksfiltracji, postanowiliśmy traktować je tak, jakby eksfiltracja miała miejsce.

Prawie wszystkie spośród 76 repozytoriów kodu źródłowego były związane z tym, jak tworzone są kopie zapasowe, jak jest konfigurowana i zarządzana sieć globalna, jak odbywa się identyfikacja w Cloudflare, na czym polega dostęp zdalny oraz w jaki sposób korzystamy z usług Terraform i Kubernetes. Niewielka liczba repozytoriów zawierała zaszyfrowane sekrety, które zostały natychmiast zmienione, nawet jeśli same były silnie zaszyfrowane.

W szczególności skoncentrowaliśmy się na tych 76 repozytoriach kodu źródłowego, aby szukać wbudowanych sekretów (tj. sekretów przechowywanych w kodzie, które zostały zmienione), luk oraz sposobów, przy użyciu których atakujący mógłby przeprowadzić kolejny atak. Prace te zostały przeprowadzone priorytetowo przez zespoły inżynierskie w całej firmie w ramach zespołu „Code Red”.

Jako firma oferująca rozwiązania SaaS od dawna uważamy, że nasz kod źródłowy sam w sobie nie jest tak cenny, jak kod źródłowy producentów oprogramowania dystrybuowanego do użytkowników końcowych. Prawdę mówiąc, dużą część naszego kodu źródłowego udostępniliśmy na zasadach open source, a na naszym blogu otwarcie mówimy o używanych przez nas algorytmach i technikach. Z tego względu skupiliśmy się nie na tym, czy ktoś ma dostęp do kodu źródłowego, lecz na tym, czy ten kod źródłowy zawiera wbudowane sekrety (takie jak klucz lub token) oraz luki.

### 23 listopada — wykrycie cyberprzestępcy i początek procesu blokowania mu dostępu

Nasz zespół ds. bezpieczeństwa został zaalarmowany o obecności cyberprzestępcy o godzinie 16:00, a 35 minut później dezaktywował konto usług Smartsheet. 48 minut później znaleziono i dezaktywowano konto użytkownika utworzone przez cyberprzestępcę. Oto szczegółowa oś czasu głównych działań podjętych w celu zablokowania cyberprzestępcy po wszczęciu pierwszego alarmu.

15:58 — cyberprzestępca dodaje konto usług Smartsheet do grupy administratorów.16:00 — zespół ds. bezpieczeństwa otrzymuje automatyczny alert o zmianie wprowadzonej o godz. 15:58.16:12 — centrum operacji bezpieczeństwa (SOC) firmy Cloudflare rozpoczyna dochodzenie w sprawie alertu.16:35 — konto usług Smartsheet zostaje dezaktywowane przez SOC Cloudflare.17:23 — znaleziono i dezaktywowano konto użytkownika Atlassian utworzone przez cyberprzestępcę.17:43 — ogłoszono wewnętrzny incydent Cloudflare.21:31 — wprowadzono reguły zapory, aby zablokować znane adresy IP cyberprzestępcy.

### 24 listopada — usunięto narzędzie Sliver; zablokowano cyberprzestępcy wszystkie możliwości dostępu

10:44 — ostatnia znana aktywność cyberprzestępcy.11:59 — usunięto narzędzie Sliver.

W ramach tej osi czasu cyberprzestępca próbował uzyskać dostęp do wielu innych systemów Cloudflare, ale nie udało mu się to za sprawą naszych kontroli dostępu, reguł zapory oraz stosowania trudnych do złamania kluczy bezpieczeństwa, egzekwowanych za pomocą naszych własnych narzędzi Zero Trust.

Dla jasności, nie znaleźliśmy żadnych dowodów na to, że cyberprzestępca uzyskał dostęp do naszej sieci globalnej, centrów danych, kluczy SSL, baz danych klientów lub informacji konfiguracyjnych, platformy Cloudflare Workers wdrożonej przez nas lub klientów, modeli sztucznej inteligencji, infrastruktury sieciowej czy jakichkolwiek naszych magazynów danych, takich jak Workers KV, R2 lub Quicksilver. Jego dostęp był ograniczony wyłącznie do pakietu Atlassian i serwera, na którym on działa.

Znaczna część naszych działań w ramach zespołu „Code Red” miała na celu zrozumienie, do czego cyberprzestępca uzyskał dostęp i do czego próbował go uzyskać. Analizując dane logowania dotyczące różnych systemów, byliśmy w stanie prześledzić próby dostępu do naszych wewnętrznych danych statystycznych, konfiguracji sieci, systemu kompilacji, systemów alarmowych oraz systemu zarządzania wydaniami. Nasza inspekcja wykazała, że żadna z prób dostępu do tych systemów nie zakończyła się powodzeniem. Firma CrowdStrike przeprowadziła niezależną ocenę zakresu i zasięgu aktywności cyberprzestępcy, która nie ujawniła przeoczonych przez nas działań, jak również doszła do wniosku, że ostatni dowód aktywności związanej z zagrożeniem wystąpił 24 listopada o godzinie 10:44.

Jesteśmy przekonani, że dzięki naszemu dochodzeniu oraz ocenie CrowdStrike w pełni poznaliśmy działania cyberprzestępcy i że były one ograniczone do systemów, na których zaobserwowaliśmy jego aktywność.

### Wnioski

Był to incydent bezpieczeństwa z udziałem wyrafinowanego sprawcy, prawdopodobnie państwa narodowego, który działał w sposób przemyślany i metodyczny. Dzięki podjętym przez nas działaniom trwałe skutki incydentu były ograniczone, a także dowiedliśmy, że jesteśmy dobrze przygotowani do odparcia wszelkich zaawansowanych ataków w przyszłości. Wymagało to wysiłków znacznej liczby pracowników inżynieryjnych Cloudflare i przez ponad miesiąc miało najwyższy priorytet w naszej firmie. Cały zespół Cloudflare pracował nad zapewnieniem bezpieczeństwa naszych systemów, poznaniem metod dostępu wykorzystywanych przez cyberprzestępcę, zrealizowaniem bezpośrednich priorytetów (takich jak masowa rotacja poświadczeń) oraz opracowaniem planu długoterminowych działań mających na celu poprawę ogólnego stanu bezpieczeństwa (na podstawie obszarów wymagających poprawy wykrytych w trakcie tego procesu).

Jesteśmy niezmiernie wdzięczni wszystkim osobom w firmie Cloudflare, które szybko zareagowały podczas weekendu Świąt Dziękczynienia, przeprowadzając wstępną analizę i blokując działania cyberprzestępcy, a także wszystkim tym, którzy przyczynili się do tych starań. Niemożliwe byłoby wymienienie wszystkich zaangażowanych osób, lecz długie godziny ich pracy i poświęcenie umożliwiły przeprowadzenie niezbędnej inspekcji oraz wprowadzenie zmian dotyczących bezpieczeństwa Cloudflare, przy jednoczesnym utrzymaniu działania naszej globalnej sieci i dostępności usług dla naszych klientów.

Jesteśmy wdzięczni firmie CrowdStrike za natychmiastową gotowość do przeprowadzenia niezależnej oceny. Teraz, gdy ukończony jest jej raport końcowy, mamy pewność co do naszej wewnętrznej analizy i naprawy skutków włamania oraz publikujemy ten wpis na blogu.

#### Oznaki pokonania zabezpieczeń

Poniżej znajdują się oznaki pokonania zabezpieczeń (IOC), które zaobserwowaliśmy w przypadku tego cyberprzestępcy. Publikujemy je, aby inne organizacje, w szczególności te, które mogły odczuć negatywne skutki naruszenia zabezpieczeń systemów Okta, mogły przeszukać swoje dzienniki w celu potwierdzenia, że ten sam cyberprzestępca nie uzyskał dostępu do ich systemów.

Indicator | Indicator Type | SHA256 | Description  
---|---|---|---  
193.142.58[.]126  | IPv4 | N/A | Primary threat actor  
Infrastructure, owned by  
M247 Europe SRL (Bucharest,  
Romania)  
198.244.174[.]214  | IPv4 | N/A | Sliver C2 server, owned by  
OVH SAS (London, England)  
idowall[.]com | Domain | N/A | Infrastructure serving Sliver  
payload  
jvm-agent | Filename | bdd1a085d651082ad567b03e5186d1d4  
6d822bb7794157ab8cce95d850a3caaf | Sliver payload  
  
Wskaźnik

Typ wskaźnika

SHA256

Opis

193.142.58[.]126 

IPv4

Nie dotyczy

Główna infrastruktura

cyberprzestępcy, właściciel:

M247 Europe SRL (Bukareszt,

Rumunia

198.244.174[.]214 

IPv4

Nie dotyczy

Serwer C2 narzędzia Sliver, właściciel:

OVH SAS (Londyn, Anglia)

idowall[.].com

Domena

Nie dotyczy

Infrastruktura obsługująca

payload narzędzia Sliver

jvm-agent

Nazwa pliku

bdd1a085d651082ad567b03e5186d1d46d822bb7794157ab8cce95d850a3caaf

Payload narzędzia Sliver

Na tej stronie

Dyskutuj online

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fthanksgiving-2023-security-incident%2F&t=Incydent%20bezpiecze%C5%84stwa%20w%20%C5%9Awi%C4%99to%20Dzi%C4%99kczynienia%202023)[](https://x.com/intent/post?text=Incydent+bezpiecze%C5%84stwa+w+%C5%9Awi%C4%99to+Dzi%C4%99kczynienia+2023&url=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fthanksgiving-2023-security-incident%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fthanksgiving-2023-security-incident%2F)[](https://bsky.app/intent/compose?text=Incydent+bezpiecze%C5%84stwa+w+%C5%9Awi%C4%99to+Dzi%C4%99kczynienia+2023+https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fthanksgiving-2023-security-incident%2F)[](https://mastodonshare.com/?text=Incydent+bezpiecze%C5%84stwa+w+%C5%9Awi%C4%99to+Dzi%C4%99kczynienia+2023&url=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fthanksgiving-2023-security-incident%2F)[](https://www.threads.net/intent/post?text=Incydent+bezpiecze%C5%84stwa+w+%C5%9Awi%C4%99to+Dzi%C4%99kczynienia+2023+https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fthanksgiving-2023-security-incident%2F)

## Powiązane tagi

[Bezpieczeństwo](https://blog.cloudflare.com/pl-pl/tag/security/)

Śledź nas w mediach społecznościowych

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)

  * ![Grant Bourzikas](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46SJJRBDYVMHZKVGKTMJ08.png&w=64&h=64&f=webp&fit=cover&position=center)[Grant Bourzikas](https://blog.cloudflare.com/pl-pl/author/grant/)

[](https://www.linkedin.com/in/grantbourzikas/)




## Zapisz się, aby otrzymywać powiadomienia o nowych postach

Adres e-mail

Nigdy nie udostępnimy Twojego adresu e-mail.

Subskrybuj

Dziękujemy za subskrypcję! Sprawdź skrzynkę odbiorczą, aby ją potwierdzić.
