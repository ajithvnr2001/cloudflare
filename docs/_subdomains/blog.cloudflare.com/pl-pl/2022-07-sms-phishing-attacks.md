---
url: https://blog.cloudflare.com/pl-pl/2022-07-sms-phishing-attacks/
title: Jak przeprowadzono wyrafinowany atak phishingowy \u2014 i jak go powstrzymali\u015bmy | Blog Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:45:53.441115+00:00
---

# Jak przeprowadzono wyrafinowany atak phishingowy — i jak go powstrzymaliśmy | Blog Cloudflare

> Source: https://blog.cloudflare.com/pl-pl/2022-07-sms-phishing-attacks/

[Blog](https://blog.cloudflare.com/pl-pl/)

[Analiza przypadku](https://blog.cloudflare.com/pl-pl/tag/post-mortem/)[Bezpieczeństwo](https://blog.cloudflare.com/pl-pl/tag/security/)[Cloudflare Access](https://blog.cloudflare.com/pl-pl/tag/cloudflare-access/)+2Pokaż 2 więcej tagów

5 tagówPokaż 5 tagów

  * Tagi wpisu
  * [Analiza przypadku](https://blog.cloudflare.com/pl-pl/tag/post-mortem/)[Bezpieczeństwo](https://blog.cloudflare.com/pl-pl/tag/security/)
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



[Cloudflare Gateway](https://blog.cloudflare.com/pl-pl/tag/gateway/)[Phishing](https://blog.cloudflare.com/pl-pl/tag/phishing/)

[Analiza przypadku](https://blog.cloudflare.com/pl-pl/tag/post-mortem/)[Bezpieczeństwo](https://blog.cloudflare.com/pl-pl/tag/security/)[Cloudflare Access](https://blog.cloudflare.com/pl-pl/tag/cloudflare-access/)[Cloudflare Gateway](https://blog.cloudflare.com/pl-pl/tag/gateway/)[Phishing](https://blog.cloudflare.com/pl-pl/tag/phishing/)

9 sierpnia 2022

# Jak przeprowadzono wyrafinowany atak phishingowy — i jak go powstrzymaliśmy

![Matthew Prince](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44KQ4Z9PY1TR0ERGW96HZR.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Daniel Stinson-Diess](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44BSD1SAVED23QC64BJ0XP.png&w=64&h=64&f=webp&fit=cover&position=center)![Sourov Zaman](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48PWM9TRAJ8WPBBS7J2SPN.png&w=64&h=64&f=webp&fit=cover&position=center)

[Matthew Prince](https://blog.cloudflare.com/pl-pl/author/matthew-prince/), [Daniel Stinson-Diess](https://blog.cloudflare.com/pl-pl/author/daniel-stinson-diess/) i [Sourov Zaman](https://blog.cloudflare.com/pl-pl/author/sourov/)

9 min czytania

KOPIUJ URL

Ten wpis jest również dostępny w [English](https://blog.cloudflare.com/2022-07-sms-phishing-attacks/), [Español](https://blog.cloudflare.com/es-es/2022-07-sms-phishing-attacks/), [日本語](https://blog.cloudflare.com/ja-jp/2022-07-sms-phishing-attacks/), [简体中文](https://blog.cloudflare.com/zh-cn/2022-07-sms-phishing-attacks/) i [Русский](https://blog.cloudflare.com/ru-ru/2022-07-sms-phishing-attacks/).

![The mechanics of a sophisticated phishing scam and how we stopped it](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44XYVSV0Q80CXCW0QHC2NE.png&w=1600&h=900&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAAgwBEiyZHn1JTtnJlxIJ0wX92qGdogjdNiTI+kE5WoXh9tJabvqGnuZifpHuDhlBZjkk2lWZipJOasrG/uLnKsqu8oIuXi2Jjkk8vmG5lp5yjtLrKuMHVsLHFoJCdjmdlkkUtmmRdqpKXua+6vbXEtqa1pIaQj11dkCQvmUlMrXV1v5KQx5mZwI2Oqm9yjURKjgAymA82rkw/xGpLz3VSyW1Rr1FGjBcyjQA0lwAprzAAxlMA0mEAzFwSsUAjiwAj)

Wczoraj, 8 sierpnia 2022 roku, firma Twilio ogłosiła, że padła [ofiarą ukierunkowanego ataku phishingowego](https://www.twilio.com/blog/august-2022-social-engineering-attack). Mniej więcej w rym samym czasie zaatakowano w zbliżony sposób pracowników Cloudflare. Choć kilka osób dało się oszukać, zdołaliśmy zatrzymać atak, ponieważ stosujemy [produkty Cloudflare One](https://www.cloudflare.com/cloudflare-one/), a wszystkie nasze aplikacje wymagają od pracowników używania fizycznych kluczy zabezpieczeń.

Potwierdziliśmy, że nie naruszono bezpieczeństwa żadnego z systemów Cloudflare. Nasz [zespół Cloudforce One, odpowiedzialny za dane dot. zagrożeń](https://blog.cloudflare.com/introducing-cloudforce-one-threat-operations-and-threat-research/), przeprowadził dodatkową analizę ataku, co pozwoliło określić jego sposób działania i zebrać istotne dowody, które przyczynią się do znalezienia sprawcy.

Była to wyrafinowana operacja atakująca pracowników i systemy w taki sposób, że większość firm prawdopodobnie nie byłaby w stanie się przed nią ochronić. Ponieważ sprawca wziął na cel wiele organizacji, postanowiliśmy podzielić się naszymi spostrzeżeniami, by pomóc innym firmom rozpoznać i złagodzić ten atak.

## Ukierunkowane SMS‑y

20 lipca 2022 roku zespół ds. bezpieczeństwa w Cloudflare otrzymał doniesienia o wysyłanych do pracowników SMS‑ach, które wyglądały na autentyczne, Zawierały one link, który zdawał się przekierowywać na stronę logowania Cloudflare w portalu Okta. Pierwsze wiadomości wysłano 20 lipca 2022 roku o godzinie 22:50 czasu UTC. W ciągu niecałej minuty co najmniej 76 pracowników otrzymało takie wiadomości na numery osobiste i służbowe. W niektórych przypadkach wiadomość wysłano nawet do członków rodzin pracowników. Nie udało nam się jeszcze ustalić, jak sprawca ataku zdobył numery telefonów pracowników. Sprawdziliśmy dzienniki dostępu do naszego katalogu pracowników i nie znaleźliśmy w nich śladów naruszenia bezpieczeństwa.

W Cloudlare zespół reagowania na incydenty bezpieczeństwa (SIRT) działa 24 godziny na dobę, 7 dni w tygodniu. Wszyscy nasi pracownicy zostali nauczeni, by zgłaszać SIRT wszystko, co wydaje im się podejrzane. W ponad 90% przypadków zgłoszone do SIRT incydenty okazują się nie być zagrożeniami. To dlatego, że pracownicy są zachęcani do wysyłania zgłoszeń i nigdy nie są za to krytykowani. W tym przypadku zgłoszenia dotyczyły jednak prawdziwego zagrożenia.

Tak wyglądały otrzymane przez pracowników wiadomości:

Zostały wysłane z czterech numerów powiązanych z kartami SIM wydanymi przez T‑Mobile: (754) 268-9387, (205) 946-7573, (754) 364-6683 i (561) 524-5989. Podana w nich domena wyglądała na oficjalną: cloudflare-okta.com. Zarejestrowano ją w rejestratorze domeny Porkbun 20 lipca 2022 roku o godzinie 22:13:04 czasu UTC, a więc niecałe 40 minut przed rozpoczęciem kampanii phishingowej.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1279 Embedded Image - mzDQx2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW458M23R42VF210NMM8NBN6.png&w=715&h=601&f=webp&fit=cover&position=center)

Cloudflare zbudowało nasz [bezpieczny rejestrator](https://www.cloudflare.com/products/registrar/custom-domain-protection/) między innymi po to, by monitorować, kiedy są rejestrowane domeny wykorzystujące markę Cloudflare, aby szybko je usuwać. Ponieważ tę domenę zarejestrowano tuż przed atakiem, nie została jeszcze opublikowana, przez co nie zdążyliśmy jej wykryć i usunąć.

Link w wiadomości prowadził do strony wyłudzającej informacje. Strona ta była hostowana na DigitalOcean i wyglądała tak:

Fałszywa strona wyglądała identycznie jak prawdziwa strona logowania Okta — systemu uwierzytelniania, z którego korzysta Cloudflare, i prosiła odwiedzającego o podanie nazwy użytkownika i hasła.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1279 Embedded Image - 5SXCpt](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45QS52KCAFCN2KSPGK32J4.png&w=715&h=536&f=webp&fit=cover&position=center)

## Phishing w czasie rzeczywistym

Udało nam się przeanalizować ładunek [ataku phishingowego](https://www.cloudflare.com/learning/email-security/what-is-email-security/) na podstawie wiadomości wysłanych do naszych pracowników oraz treści opublikowanej na takich portalach, jak VirusTotal, przez inne zaatakowane firmy. Gdy ofiara ataku wypełniła pola na stronie, dane logowania były natychmiast przekazywane sprawcy za pośrednictwem komunikatora internetowego Telegram. Ten ostatni punkt jest istotny, ponieważ fałszywa strona prosiła także o podanie hasła jednorazowego opartego na czasie (kod TOTP).

Przypuszczamy, że sprawca ataku otrzymywał dane logowania w czasie rzeczywistym i wprowadzał je na prawdziwej stronie logowania firmy ofiary, co w przypadku wielu organizacji powodowało wygenerowanie kodu wysyłanego pracownikowi SMS‑em lub wyświetlanego w generatorze haseł. Pracownik następnie wprowadzał kod TOTP na fałszywej stronie, która przekazywała go sprawcy ataku. Ten mógł wówczas, zanim wygasł kod TOTP, wykorzystać go do zalogowania na prawdziwej stronie logowania firmy — obchodząc w ten sposób najczęstszy sposób zabezpieczenia uwierzytelnianiem dwuskładnikowym.

## Sprawna ochrona mimo potknięć

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1279 Embedded Image - y0kAKQ](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48BDTY0D16K46QEKFRZ8VJ.png&w=715&h=250&f=webp&fit=cover&position=center)

Ustaliliśmy, że troje pracowników Cloudflare dało się oszukać i wprowadziło swoje dane na fałszywej stronie. Cloudflare nie korzysta jednak z kodów TOTP. Zamiast tego każdy pracownik otrzymuje zgodny ze standardem FIDO2 klucz zabezpieczeń od takiego dostawcy, jak YubiKey. To fizyczne klucze, które są powiązane z konkretnymi pracownikami i implementują [powiązanie ze źródłem](https://www.yubico.com/blog/creating-unphishable-security-key/). Dzięki temu nawet wyrafinowana operacja phishingowa przeprowadzana w czasie rzeczywistym nie pozwoliłaby zebrać informacji koniecznych do zalogowania się do któregokolwiek z naszych systemów. Choć sprawca ataku próbował zalogować się do naszych systemów z wykorzystaniem skradzionych nazw użytkownika i haseł, nie mógł obejść wymagania fizycznego klucza.

Celem tej fałszywej strony nie było jednak samo wyłudzanie poświadczeń i kodów TOTP. Jeśli ktoś wprowadził wszystkie te dane, strona inicjowała pobieranie ładunku zawierającego oprogramowanie AnyDesk do zdalnego dostępu. Zainstalowanie tego oprogramowania pozwoliłoby sprawcy ataku zdalnie kontrolować komputer ofiary. Żaden z naszych pracowników nie doszedł do tego etapu. Gdyby tak jednak się stało, nasza ochrona punktów końcowych powstrzymałaby instalację oprogramowania do zdalnego dostępu.

## **Jak zareagowaliśmy na atak?**

Oto najważniejsze z działań podjętych przez nas w odpowiedzi na ten incydent:

### 1\. Zablokowanie fałszywej domeny za pomocą Cloudflare Gateway

Cloudflare Gateway to [bezpieczna brama internetowa (SWG)](https://www.cloudflare.com/learning/access-management/what-is-a-secure-web-gateway/) zapewniająca ochronę przez zagrożeniami internetowymi oraz ochronę danych z filtrowaniem DNS/HTTP i natywnie zintegrowanym [Zero Trust](https://www.cloudflare.com/learning/security/glossary/what-is-zero-trust/). Korzystamy z tego rozwiązania w naszej firmie, aby zapobiegawczo blokować domeny, które określiliśmy jako złośliwe. Nasz zespół dodał złośliwą domenę do Cloudflare Gateway, by zablokować do niej dostęp wszystkim pracownikom.

Funkcja automatycznego wykrywania złośliwych domen zidentyfikowała domenę i ją zablokowała, jednak ponieważ zarejestrowano ją krótki czas przed wysłaniem wiadomości, system nie zdążył podjąć działań, zanim kilkoro pracowników kliknęło link. Mając na względzie ten incydent, pracujemy nad przyspieszeniem procesu wykrywania i blokowania złośliwych domen. Implementujemy także kontrole dostępu do nowo zarejestrowanych domen — jest to opcja, którą oferujemy klientom, a z której sami dotychczas nie korzystaliśmy.

### 2\. Zidentyfikowanie wszystkich dotkniętych problemem pracowników i zresetowanie wykradzionych poświadczeń

Porównaliśmy odbiorców SMS-ów z aktywnością logowania i wykryliśmy próby uwierzytelnienia kont pracowników w ramach ataku. Wykryliśmy próby logowania zablokowane dzięki wymaganiu fizycznego klucza (U2F), co oznacza, że użyto prawidłowego hasła, ale nie udało się zweryfikować drugiego składnika. Zresetowaliśmy dane logowania oraz wszystkie aktywne sesje trojga pracowników, których dane logowania zostały skradzione. Przeskanowaliśmy również ich urządzenia.

### 3\. Identyfikacja i usunięcie infrastruktury źródła zagrożenia

Domena wykorzystana w ataku była nowa, zarejestrowana przez Porkbun i hostowana na DigitalOcean. Założono ją niecałą godzinę przez pierwszą falą ataku. Strona miała front-end Nuxt.js i back-end Django. W wyniku naszego zgłoszenia DigitalOcean zamknęło serwer źródła zagrożenia. Podobnie Porkbun przejęło kontrolę nad złośliwą domeną.

Na podstawie nieudanych prób logowania ustaliliśmy, że sprawca ataku korzystał z oprogramowania VPN Mullvad i używał przeglądarki Google Chrome oraz systemu Windows 10. Adresy IP VPN sprawcy ataku to 198.54.132.88 oraz 198.54.135.222. Są one przypisane Tzulo, dostawcy serwerów z siedzibą w USA, który podaje na swojej stronie internetowej, że ma serwery w Los Angeles i Chicago. W rzeczywistości wygląda jednak na to, że pierwszy adres był powiązany z serwerem w okolicach Toronto, a drugi z serwerem w okolicach Waszyngtonu (DC). Zablokowaliśmy tym adresom IP dostęp do naszych usług.

### 4\. Aktualizacja wykrywania zagrożeń w celu identyfikacji kolejnych prób ataku

Na podstawie zebranych informacji o tym ataku włączyliśmy do naszego istniejącego systemu wykrywania dodatkowe sygnały ostrzegawcze, odnoszące się do tego sprawcy. Do czasu publikacji tego artykułu nie zaobserwowaliśmy kolejnych fal ataku na naszą firmę. Dane z serwera wskazują jednak, że sprawca zaatakował również inne organizacje, w tym Twilio. Skontaktowaliśmy się z tymi organizacjami i przekazaliśmy im zebrane przez nas informacje.

### 5\. Inspekcja dzienników dostępu do usługi pod kątem innych oznak ataku

Po ataku sprawdziliśmy wszystkie dzienniki systemu pod kątem dodatkowych śladów cyfrowych sprawcy. Ponieważ Cloudflare Access stanowi punkt kontroli wszystkich aplikacji Cloudflare, możemy przeszukać dzienniki i wykryć wszelkie ślady naruszenia bezpieczeństwa systemów. Ponieważ w ataku wykorzystano telefony pracowników, starannie przeanalizowaliśmy także dzienniki dostawców usług dla pracowników. Nie znaleźliśmy dowodów naruszenia bezpieczeństwa.

## Wyciągnięte wnioski i plan dodatkowych działań

Każdy atak jest dla nas lekcją. Choć ten był nieudany, wprowadzamy dodatkowe zmiany na podstawie zebranych przez nas informacji. Modyfikujemy ustawienia Cloudflare Gateway, by ograniczyć lub odizolować dostęp do stron internetowych na domenach zarejestrowanych w ciągu ostatniej doby. Wszelkie strony, które nie są na liście dozwolonych, a zawierają terminy takie jak „cloudflare”, „okta”, „sso” i „2fa”, będą obsługiwane w odizolowanej przeglądarce. Zwiększamy także wykorzystanie [technologii Cloudflare Area 1 rozpoznające ataki phishingowe](https://www.cloudflare.com/products/zero-trust/email-security/) do skanowania sieci Web w poszukiwaniu stron, które mają służyć do zaatakowania Cloudflare. Na koniec wzmacniamy implementację Access, by zapobiegać logowaniom z nieznanych sieci VPN, lokalnych serwerów proxy i dostawców infrastruktury. Są to standardowe funkcje produktów, które oferujemy naszym klientom.

Atak pokazał także istotność trzech rzeczy, które robimy dobrze. Po pierwsze, dostęp do każdej aplikacji wymaga fizycznego klucza. [Podobnie jak Google](https://krebsonsecurity.com/2018/07/google-security-keys-neutralized-employee-phishing/), od czasu wprowadzenia tej metody uwierzytelniania nie mieliśmy do czynienia z ani jednym udanym atakiem phishingowym. Narzędzia takie jak Cloudflare Access ułatwiają wsparcie fizycznych kluczy nawet w starszych aplikacjach. Jeśli Twoja organizacja jest zainteresowana, jak wdrożyliśmy te klucze, skontaktuj się z nami pod adresem [cloudforceone-irhelp@cloudflare.com](mailto:cloudforceone-irhelp@cloudflare.com), a nasz zespół ds. bezpieczeństwa chętnie podzieli się dobrymi praktykami, których nauczyliśmy się w tym procesie.

Po drugie, używamy własnej technologii do ochrony naszych pracowników i systemów. Rozwiązania Cloudflare One, takie jak Access i Gateway, były kluczowe w ochronie przed tym atakiem. Skonfigurowaliśmy implementację Access tak, by każda aplikacja wymagała fizycznego klucza. Access tworzy także jedno miejsce logowania do uwierzytelniania wszystkich aplikacji. W razie konieczności umożliwia także zakończenie sesji użytkownika z potencjalnie naruszonymi zabezpieczeniami. Gateway pozwala nam szybko zablokować złośliwe strony i ustalić, którzy pracownicy mogli zostać oszukani. Wszystkie te funkcje są dostępne dla klientów Cloudflare w ramach pakietu Cloudflare One, a ten atak dowodzi ich skuteczności.

Po trzecie, kultura podejrzliwości bez obwiniania pracowników ma zasadnicze znaczenie dla bezpieczeństwa. Trzy osoby, które dały się oszukać w ataku, nie otrzymały nagany. Wszyscy jesteśmy ludźmi i popełniamy czasem błędy. To niezmiernie ważne, żeby je zgłaszać, a nie tuszować. Ten incydent jest kolejnym przykładem tego, że bezpieczeństwo jest częścią pracy każdego członka zespołu Cloudflare.

## Szczegółowa oś czasu wydarzeń

.tg {border-collapse:collapse;border-spacing:0;} .tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px; overflow:hidden;padding:10px 5px;word-break:normal;} .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px; font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;} .tg .tg-0lax{text-align:left;vertical-align:top}

2022-07-20 22:49 UTC

Sprawca wysyła ponad 100 SMS‑ów do pracowników Cloudflare i ich rodzin.

2022-07-20 22:50 UTC

Pracownicy zaczynają zgłaszać SMS-y zespołowi ds. bezpieczeństwa.

2022-07-20 22:52 UTC

Blokujemy w Cloudflare Gateway domenę źródła zagrożenia na urządzeniach służbowych.

2022-07-20 22:58 UTC

Wszyscy pracownicy otrzymują ostrzeżenia przez chat i pocztę e‑mail.

2022-07-20 22:50 UTC to2022-07-20 23:26 UTC

Monitorowanie telemetrii w dzienniku systemu Okta i dziennikach HTTP Cloudflare Gateway w celu zidentyfikowania naruszenia bezpieczeństwa poświadczeń. Wyczyszczenie sesji logowania i zawieszenie dotkniętych kont.

2022-07-20 23:26 UTC

Dostawca hostingu zamyka stronę wyłudzającą dane.

2022-07-20 23:37 UTC

Reset skradzionych poświadczeń.

2022-07-21 00:15 UTC

Analiza infrastruktury i możliwości sprawcy.

## Wskaźniki naruszenia bezpieczeństwa

.tg {border-collapse:collapse;border-spacing:0;} .tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px; overflow:hidden;padding:10px 5px;word-break:normal;} .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px; font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;} .tg .tg-nr0u{border-color:inherit;font-family:inherit;font-size:100%;text-align:left;vertical-align:top} .tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}

Value | Type | Context and MITRE Mapping  
---|---|---  
cloudflare-okta[.]com hosted on 147[.]182[.]132[.]52 | Phishing URL | [T1566.002](https://attack.mitre.org/techniques/T1566/002/): Phishing: Spear Phishing Link sent to users.  
64547b7a4a9de8af79ff0eefadde2aed10c17f9d8f9a2465c0110c848d85317a | SHA-256 | [T1219](https://attack.mitre.org/techniques/T1219/): Remote Access Software being distributed by the threat actor  
  
Wartość

Typ

Kontekst i mapowanie MITRE

cloudflare-okta[.]com hosted on 147[.]182[.]132[.]52

Adres URL strony

[T1566.002](https://attack.mitre.org/techniques/T1566/002/): phishing: link spear phishing wysłany do użytkowników

64547b7a4a9de8af79ff0eefadde2aed10c17f9d8f9a2465c0110c848d85317a

SHA-256

[T1219](https://attack.mitre.org/techniques/T1219/): oprogramowanie do dostępu zdalnego rozpowszechniane przez sprawcę

## Co możesz zrobić

Jeśli w Twoim środowisku zdarzają się podobne ataki, zachęcamy do kontaktu pod adresem [cloudforceone-irhelp@cloudflare.com](mailto:cloudforceone-irhelp@cloudflare.com). Chętnie podzielimy się dobrymi praktykami w zakresie bezpieczeństwa Twojej firmy. A może chcesz pracować z nami nad wykrywaniem i łagodzeniem kolejnych ataków? Prowadzimy rekrutację do zespołu wykrywania i reagowania. [Dołącz do nas](https://boards.greenhouse.io/cloudflare/jobs/4364485?gh_jid=4364485)!

Na tej stronie

Dyskutuj online

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2F2022-07-sms-phishing-attacks%2F&t=Jak%20przeprowadzono%20wyrafinowany%20atak%20phishingowy%20%E2%80%94%20i%20jak%20go%20powstrzymali%C5%9Bmy)[](https://x.com/intent/post?text=Jak+przeprowadzono+wyrafinowany+atak+phishingowy+%E2%80%94+i+jak+go+powstrzymali%C5%9Bmy&url=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2F2022-07-sms-phishing-attacks%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2F2022-07-sms-phishing-attacks%2F)[](https://bsky.app/intent/compose?text=Jak+przeprowadzono+wyrafinowany+atak+phishingowy+%E2%80%94+i+jak+go+powstrzymali%C5%9Bmy+https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2F2022-07-sms-phishing-attacks%2F)[](https://mastodonshare.com/?text=Jak+przeprowadzono+wyrafinowany+atak+phishingowy+%E2%80%94+i+jak+go+powstrzymali%C5%9Bmy&url=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2F2022-07-sms-phishing-attacks%2F)[](https://www.threads.net/intent/post?text=Jak+przeprowadzono+wyrafinowany+atak+phishingowy+%E2%80%94+i+jak+go+powstrzymali%C5%9Bmy+https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2F2022-07-sms-phishing-attacks%2F)

## Powiązane tagi

[Analiza przypadku](https://blog.cloudflare.com/pl-pl/tag/post-mortem/)[Bezpieczeństwo](https://blog.cloudflare.com/pl-pl/tag/security/)[Cloudflare Access](https://blog.cloudflare.com/pl-pl/tag/cloudflare-access/)[Cloudflare Gateway](https://blog.cloudflare.com/pl-pl/tag/gateway/)[Phishing](https://blog.cloudflare.com/pl-pl/tag/phishing/)

Śledź nas w mediach społecznościowych

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Zapisz się, aby otrzymywać powiadomienia o nowych postach

Adres e-mail

Nigdy nie udostępnimy Twojego adresu e-mail.

Subskrybuj

Dziękujemy za subskrypcję! Sprawdź skrzynkę odbiorczą, aby ją potwierdzić.
