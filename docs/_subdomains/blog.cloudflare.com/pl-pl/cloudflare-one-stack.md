---
url: https://blog.cloudflare.com/pl-pl/cloudflare-one-stack/
title: Przedstawiamy stos Cloudflare One \u2014 wdro\u017cenie oparte na agentach | Blog Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:36:46.052549+00:00
---

# Przedstawiamy stos Cloudflare One — wdrożenie oparte na agentach | Blog Cloudflare

> Source: https://blog.cloudflare.com/pl-pl/cloudflare-one-stack/

[Blog](https://blog.cloudflare.com/pl-pl/)

[Agenty](https://blog.cloudflare.com/pl-pl/tag/agents/)[Cloudflare One](https://blog.cloudflare.com/pl-pl/tag/cloudflare-one/)[Zero Trust](https://blog.cloudflare.com/pl-pl/tag/zero-trust/)

3 tagówPokaż 3 tagów

  * Tagi wpisu
  * [Agenty](https://blog.cloudflare.com/pl-pl/tag/agents/)[Cloudflare One](https://blog.cloudflare.com/pl-pl/tag/cloudflare-one/)[Zero Trust](https://blog.cloudflare.com/pl-pl/tag/zero-trust/)
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



[Agenty](https://blog.cloudflare.com/pl-pl/tag/agents/)[Cloudflare One](https://blog.cloudflare.com/pl-pl/tag/cloudflare-one/)[Zero Trust](https://blog.cloudflare.com/pl-pl/tag/zero-trust/)

17 czerwca 2026

# Przedstawiamy stos Cloudflare One: wdrożenie oparte na agentach

![AJ Gerstenhaber](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45AC8ST716E4F0Q7NWHHKA.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Abe Carryl](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46JJ6YPQY3M4A69P72QXE8.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[AJ Gerstenhaber](https://blog.cloudflare.com/pl-pl/author/aj/) i [Abe Carryl](https://blog.cloudflare.com/pl-pl/author/abe/)

6 min czytania

KOPIUJ URL

Ten wpis jest również dostępny w [English](https://blog.cloudflare.com/cloudflare-one-stack/), [简体中文](https://blog.cloudflare.com/zh-cn/cloudflare-one-stack/) i [Português](https://blog.cloudflare.com/pt-br/cloudflare-one-stack/).

![BLOG-3315 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW9WKZ9GJQY8S7W209ZJ8YNT&w=1200&h=675&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA//////369fLx7ezs8u7u+fPx9/Lw7uzp//////z77u3y4uTt5+fv8e7z8vDx6+vr//////v86On0193w3ODy6ev27u/06evu//////7/6Or41dz02OD35+z77vH56+/y////////7/H+3eT64Oj97vP/9Pf/8fT4////////+vz/7PH/7/T/+v3//f//+fv9////////////+fz//P///////////////////////////v//////////////////)

Przyjęcie architektury sieciowej Zero Trust lub migracja do niej może być trudnym zadaniem. Zanim zmieni się choć jedna zasada, zespoły muszą sobie przypomnieć, jak faktycznie zbudowana jest ich sieć: jakie aplikacje istnieją, jakie mechanizmy uwierzytelniania i autoryzacji wykorzystują, jak przepływa między nimi ruch oraz jakie założenia przyjęto w aktualnej architekturze. Ten praktyczny proces wymaga od specjalistów odczytania intencji stojących za każdą obowiązującą zasadą bezpieczeństwa i routingu.

Dziś udostępniamy stos Cloudflare One, [_zestaw umiejętności_](https://github.com/cloudflare/skills), który można przekazać agentowi, aby konfigurował, wdrażał i zarządzał środowiskiem Zero Trust. Ten zestaw narzędzi zaprojektowano tak, aby pomóc zautomatyzować proces poznawania całkowicie nowego pakietu zabezpieczeń i odwzorowywania dotychczasowego środowiska w Cloudflare.

Właśnie w taki sposób firma Cloudflare współpracowała z tysiącami klientów. Ta powtarzalność pozwoliła zbudować wiedzę o tym, gdzie migracje się zatrzymują, jakie pytania pojawiają się za każdym razem i czego potrzeba, aby ruszyć dalej. Stos Cloudflare One skupia tę wiedzę i sprawia, że jest ona dostępna szerzej niż kiedykolwiek. 

### Luka agentowa w bezpieczeństwie sieci

Zespoły już wykorzystują agenty do pisania kodu, klasyfikowania alertów i automatyzowania przepływów pracy. Organizacje coraz częściej oczekują narzędzi dostarczanych przez Cloudflare, które pomogą agentom wykonywać przepływy pracy związane z bezpieczeństwem. Same agenty nie są wytrenowane pod kątem niuansów konkretnej topologii sieci organizacji ani konfiguracji dostawców.

Dzięki preskryptywnym i autorytatywnym wskazówkom organizacje mogą dodać ten kontekst do swojego obecnego zestawu narzędzi, aby lepiej wykorzystywać aktualnie wdrażane produkty zabezpieczające.

Cloudflare od dawna należy do dostawców rozwiązań SASE najłatwiejszych do wdrożenia. Stos rozszerza tę filozofię na agenty: zapewnia im kontekst, narzędzia i uporządkowane rozumowanie potrzebne do działania w obrębie infrastruktury bezpieczeństwa.

## Czym jest stos Cloudflare One?

Stos Cloudflare One to [_zbiór umiejętności_](https://github.com/cloudflare/skills), których można używać z dowolnym agentem. Podobnie jak w przypadku [_każdej umiejętności_](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills), można używać ich samodzielnie, dodawać własny kontekst albo budować na ich podstawie narzędzia. Rozwiązanie opracowano specjalnie po to, aby wspierać specjalistów ds. bezpieczeństwa w całym procesie oceny, wdrażania i zarządzania [_Cloudflare One_](https://developers.cloudflare.com/cloudflare-one/).

Stos powstał poprzez syntezę ręcznie dobranej wiedzy pracowników mających dziesiątki tysięcy godzin doświadczenia we współpracy z klientami korzystającymi z produktów Cloudflare One. Zawiera narzędzia do planowania, zarządzania i wdrażania infrastruktury bezpieczeństwa użytkowników i agentów w Cloudflare. Obejmuje także starannie dobraną logikę migracji od starszych dostawców, takich jak [_Zscaler_](https://blog.cloudflare.com/descaler-program/) i Palo Alto Networks.

W połączeniu z [_serwerem MCP trybu kodu Cloudflare_](https://developers.cloudflare.com/agents/model-context-protocol/mcp-servers-for-cloudflare/) stos zapewnia agentom uporządkowany dostęp do API Cloudflare z jasno zdefiniowanymi typami danych. Agenty mogą wykonywać zapytania dotyczące aktywnego konta, sprawdzać konfiguracje i wprowadzać zmiany za pomocą starannie dobranego zestawu przepływów pracy rekomendowanych przez Cloudflare, zamiast korzystać z doraźnych wywołań interfejsu API.

## Co znajduje się w stosie?

Stos Cloudflare One jest dostarczany w postaci dwóch lekkich plików umiejętności: cloudflare-one i cloudflare-one-migration. Razem obejmują one migrację do Cloudflare One, tworzenie implementacji, zarządzanie nią oraz rozwiązywanie problemów:

  * **Dostęp zdalny i zastąpienie VPN** dzięki Cloudflare Access
  * **Bezpieczeństwo użytkowników, sieci, urządzeń i danych** dzięki Cloudflare Gateway
  * **Łączność** z usługami Cloudflare Tunnel, Cloudflare Mesh i Cloudflare WAN
  * **Wytyczne dotyczące migracji** ze szczegółowymi informacjami o przejściu od innych dostawców SASE
  * **Interpretowanie i generowanie diagramów sieciowych** , aby można było wizualizować proponowane zmiany w sieci w sposób łatwy do zrozumienia dla zespołu
  * **Tłumaczenie pojęć między dostawcami** , które odwzorowuje pojęcia stosowane przez różnych dostawców SASE w celu zmniejszenia bariery utrudniającej ocenę i zmianę dostawców
  * **Rozwiązywanie problemów i działania operacyjne** z zestawem narzędzi Digital Experience Monitoring (DEX) oraz automatycznymi rekomendacjami reguł



## Jak to działa?

Stos jest dostępny w repozytorium [_Cloudflare Skills_](https://github.com/cloudflare/skills). Każdy plik umiejętności obejmuje uporządkowaną wiedzę, drzewa decyzyjne i definicje narzędzi, które agenty automatycznie wczytują, gdy kontekst jest zgodny. Przekaż to agentowi, aby pomógł Ci w konfigurowaniu, ustawianiu oraz zarządzaniu środowiskiem Zero Trust:

Umiejętność cloudflare-one obejmuje ogólne wskazówki dotyczące produktów. Jeśli na przykład zapytanie do agenta dotyczy najlepszego sposobu zastąpienia infrastruktury VPN za pomocą Cloudflare Tunnel lub Cloudflare Mesh, ta umiejętność podpowie agentowi, jak:

  1. Przeprowadzić inwentaryzację istniejących aplikacji VPN i określić, jakiego modelu łączności wymaga każda z nich
  2. Odwzorować każdą aplikację na odpowiedni element podstawowy Cloudflare — aplikację Access z własnym hostingiem, usługę połączoną przez Tunnel albo segment sieci połączony przez Mesh
  3. Wygenerować zalecaną sekwencję wdrożenia, która minimalizuje zakłócenia podczas przełączenia
  4. Przygotować podsumowanie konfiguracji, które zespół może przejrzeć przed wprowadzeniem jakichkolwiek zmian



Umiejętność cloudflare-one-migration obejmuje tłumaczenie pojęć między dostawcami. Jeśli na przykład zapytanie do agenta dotyczy migracji aplikacji Zscaler Private Access do Cloudflare Access, ta umiejętność podpowie agentowi, jak:

  1. Odwzorować definicje aplikacji Zscaler na definicje aplikacji Cloudflare Access
  2. Przekształcić grupy użytkowników i zasady Zscaler w zasady Cloudflare Access
  3. Użyć interfejsu API Cloudflare do utworzenia równoważnych zasobów na koncie
  4. Wygenerować podsumowanie tego, co zostało przeniesione, oraz tego, co wymaga ręcznego sprawdzenia



Logika migracji w stosie jest taka sama jak logika stosowana w programach Cloudflare [_Descaler_](https://blog.cloudflare.com/descaler-program/) i [_Deskope_](https://blog.cloudflare.com/deskope-program-and-asdp-for-descaler/). Programy te umożliwiły już klientom firmowym przejście z rozwiązań Zscaler i Netskope na Cloudflare One w ciągu godzin, a nie miesięcy. Stos zapewnia tę możliwość każdemu klientowi lub partnerowi, w dowolnym momencie, bez czekania na zaplanowane wsparcie.

### Więcej sposobów korzystania ze stosu

Stos Cloudflare One może również:

  * Rekomendować reguły zabezpieczeń na podstawie ruchu obserwowanego na aktywnym koncie
  * Automatycznie migrować istniejące aplikacje Zscaler Private Access do aplikacji Cloudflare Access z własnym hostingiem
  * Badać anomalie w dziennikach HTTP bramy SWG oraz tworzyć reguły rozwiązujące problemy zgłaszane przez użytkowników
  * Opracowywać raporty na temat stabilności po stronie użytkowników za pomocą zestawu narzędzi DEX oraz podejmować działania w celu zmniejszenia opóźnień w kluczowych scenariuszach



Niezależnie od tego, czy umiejętność jest ładowana z poziomu agenta, czy stanowi podstawę do tworzenia narzędzi niestandardowych, stos Cloudflare One obsługuje wszystkie te przypadki użycia i wiele innych.

## Także dla partnerów

Choć upraszcza to bieżące zarządzanie klientom, którzy już wdrożyli pakiet produktów Cloudflare One, jest to również narzędzie dla sieci partnerskiej Cloudflare. Partnerzy mogą go używać, aby pomagać swoim klientom szybciej wdrażać rozwiązania, skuteczniej nimi zarządzać, dokładniej diagnozować problemy oraz doprowadzać do ich rozwiązania.

## Co dalej

Ze stosu Cloudflare One można zacząć korzystać już dziś. Aby w pełni wykorzystać możliwości stosu, warto połączyć go z [_serwerem MCP trybu kodu Cloudflare_](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#code-mode). Serwer MCP zapewnia agentowi bieżący dostęp do API Cloudflare przez pojedynczy, skompresowany interfejs, który utrzymuje dane uwierzytelniające poza kontekstem modelu. 

Stos Cloudflare One będzie nadal rozwijany wraz z ewolucją produktów Cloudflare One. Trwają już prace nad nowymi umiejętnościami dla dodatkowych źródeł migracji i bardziej zaawansowanych przepływów pracy związanych z rozwiązywaniem problemów.

W miarę jak będziemy dowiadywać się więcej o tym, jak klienci i partnerzy korzystają z tych plików umiejętności, planujemy tworzyć wokół nich bardziej rozbudowane narzędzia. Klienci i partnerzy, którzy chcą przekazać opinię na temat tego, co stos powinien obsługiwać w następnej kolejności, mogą skontaktować się ze swoim zespołem ds. obsługi klienta lub otworzyć zgłoszenie w repozytorium.

Na tej stronie

Dyskutuj online

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fcloudflare-one-stack%2F&t=Przedstawiamy%20stos%20Cloudflare%20One%3A%20wdro%C5%BCenie%20oparte%20na%20agentach)[](https://x.com/intent/post?text=Przedstawiamy+stos+Cloudflare+One%3A+wdro%C5%BCenie+oparte+na+agentach&url=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fcloudflare-one-stack%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fcloudflare-one-stack%2F)[](https://bsky.app/intent/compose?text=Przedstawiamy+stos+Cloudflare+One%3A+wdro%C5%BCenie+oparte+na+agentach+https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fcloudflare-one-stack%2F)[](https://mastodonshare.com/?text=Przedstawiamy+stos+Cloudflare+One%3A+wdro%C5%BCenie+oparte+na+agentach&url=https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fcloudflare-one-stack%2F)[](https://www.threads.net/intent/post?text=Przedstawiamy+stos+Cloudflare+One%3A+wdro%C5%BCenie+oparte+na+agentach+https%3A%2F%2Fblog.cloudflare.com%2Fpl-pl%2Fcloudflare-one-stack%2F)

## Powiązane tagi

[Agenty](https://blog.cloudflare.com/pl-pl/tag/agents/)[Cloudflare One](https://blog.cloudflare.com/pl-pl/tag/cloudflare-one/)[Zero Trust](https://blog.cloudflare.com/pl-pl/tag/zero-trust/)

Śledź nas w mediach społecznościowych

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Zapisz się, aby otrzymywać powiadomienia o nowych postach

Adres e-mail

Nigdy nie udostępnimy Twojego adresu e-mail.

Subskrybuj

Dziękujemy za subskrypcję! Sprawdź skrzynkę odbiorczą, aby ją potwierdzić.
