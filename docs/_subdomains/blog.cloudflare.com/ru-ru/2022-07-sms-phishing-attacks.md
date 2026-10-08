---
url: https://blog.cloudflare.com/ru-ru/2022-07-sms-phishing-attacks/
title: \u041c\u0435\u0445\u0430\u043d\u0438\u043a\u0430 \u0438\u0437\u043e\u0449\u0440\u0435\u043d\u043d\u043e\u0433\u043e \u0444\u0438\u0448\u0438\u043d\u0433\u043e\u0432\u043e\u0433\u043e \u043c\u043e\u0448\u0435\u043d\u043d\u0438\u0447\u0435\u0441\u0442\u0432\u0430: \u043a\u0430\u043a \u043d\u0430\u043c \u0443\u0434\u0430\u043b\u043e\u0441\u044c \u0435\u0433\u043e \u043f\u0440\u0435\u0434\u043e\u0442\u0432\u0440\u0430\u0442\u0438\u0442\u044c | \u0411\u043b\u043e\u0433 Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:45:53.756701+00:00
---

# Механика изощренного фишингового мошенничества: как нам удалось его предотвратить | Блог Cloudflare

> Source: https://blog.cloudflare.com/ru-ru/2022-07-sms-phishing-attacks/

[Блог](https://blog.cloudflare.com/ru-ru/)

[Cloudflare Access](https://blog.cloudflare.com/ru-ru/tag/cloudflare-access/)[Cloudflare Gateway](https://blog.cloudflare.com/ru-ru/tag/gateway/)[Phishing](https://blog.cloudflare.com/ru-ru/tag/phishing/)+2Показать ещё 2 тегов

5 теговПоказать 5 тегов

  * Теги публикации
  * [Анализ после инцидента](https://blog.cloudflare.com/ru-ru/tag/post-mortem/)[Безопасность](https://blog.cloudflare.com/ru-ru/tag/security/)
  * Все теги
  * Подходящие теги
  * Теги не найдены
  * [1.1.1.1](https://blog.cloudflare.com/ru-ru/tag/1-1-1-1/)
  * [ИИ](https://blog.cloudflare.com/ru-ru/tag/ai/)
  * [Безопасность приложений](https://blog.cloudflare.com/ru-ru/tag/application-security/)
  * [Прикладные сервисы](https://blog.cloudflare.com/ru-ru/tag/application-services/)
  * [AWS](https://blog.cloudflare.com/ru-ru/tag/aws/)
  * [Управление ботами](https://blog.cloudflare.com/ru-ru/tag/bot-management/)
  * [Потребительские услуги](https://blog.cloudflare.com/ru-ru/tag/consumer-services/)
  * [DDoS](https://blog.cloudflare.com/ru-ru/tag/ddos/)
  * [DDoS Alerts (RU)](https://blog.cloudflare.com/ru-ru/tag/ddos-alerts/)
  * [Отчеты о DDoS](https://blog.cloudflare.com/ru-ru/tag/ddos-reports/)
  * [Разработчики](https://blog.cloudflare.com/ru-ru/tag/developers/)
  * [DNS](https://blog.cloudflare.com/ru-ru/tag/dns/)
  * [Мошенничество](https://blog.cloudflare.com/ru-ru/tag/fraud/)
  * [Воздействие](https://blog.cloudflare.com/ru-ru/tag/impact/)
  * [Жизнь в Cloudflare](https://blog.cloudflare.com/ru-ru/tag/life-at-cloudflare/)
  * [Сбой](https://blog.cloudflare.com/ru-ru/tag/outage/)
  * [Партнеры](https://blog.cloudflare.com/ru-ru/tag/partners/)
  * [Политика и право](https://blog.cloudflare.com/ru-ru/tag/policy/)
  * [Анализ после инцидента](https://blog.cloudflare.com/ru-ru/tag/post-mortem/)
  * [Конфиденциальность](https://blog.cloudflare.com/ru-ru/tag/privacy/)
  * [Новости](https://blog.cloudflare.com/ru-ru/tag/product-news/)
  * [Проект «Галилео»](https://blog.cloudflare.com/ru-ru/tag/project-galileo/)
  * [Radar](https://blog.cloudflare.com/ru-ru/tag/cloudflare-radar/)
  * [Безопасность](https://blog.cloudflare.com/ru-ru/tag/security/)
  * [Скорость и надежность](https://blog.cloudflare.com/ru-ru/tag/speed-and-reliability/)
  * [Прозрачность](https://blog.cloudflare.com/ru-ru/tag/transparency/)
  * [WAF](https://blog.cloudflare.com/ru-ru/tag/waf/)
  * [Zero Trust](https://blog.cloudflare.com/ru-ru/tag/zero-trust/)



[Анализ после инцидента](https://blog.cloudflare.com/ru-ru/tag/post-mortem/)[Безопасность](https://blog.cloudflare.com/ru-ru/tag/security/)

[Cloudflare Access](https://blog.cloudflare.com/ru-ru/tag/cloudflare-access/)[Cloudflare Gateway](https://blog.cloudflare.com/ru-ru/tag/gateway/)[Phishing](https://blog.cloudflare.com/ru-ru/tag/phishing/)[Анализ после инцидента](https://blog.cloudflare.com/ru-ru/tag/post-mortem/)[Безопасность](https://blog.cloudflare.com/ru-ru/tag/security/)

9 августа 2022 г.

# Механика изощренного фишингового мошенничества: как нам удалось его предотвратить

![Matthew Prince](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44KQ4Z9PY1TR0ERGW96HZR.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Daniel Stinson-Diess](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44BSD1SAVED23QC64BJ0XP.png&w=64&h=64&f=webp&fit=cover&position=center)![Sourov Zaman](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48PWM9TRAJ8WPBBS7J2SPN.png&w=64&h=64&f=webp&fit=cover&position=center)

[Matthew Prince](https://blog.cloudflare.com/ru-ru/author/matthew-prince/), [Daniel Stinson-Diess](https://blog.cloudflare.com/ru-ru/author/daniel-stinson-diess/) и [Sourov Zaman](https://blog.cloudflare.com/ru-ru/author/sourov/)

11 мин. чтения

КОПИРОВАТЬ URL

Этот пост также доступен на [English](https://blog.cloudflare.com/2022-07-sms-phishing-attacks/), [Español](https://blog.cloudflare.com/es-es/2022-07-sms-phishing-attacks/), [日本語](https://blog.cloudflare.com/ja-jp/2022-07-sms-phishing-attacks/), [简体中文](https://blog.cloudflare.com/zh-cn/2022-07-sms-phishing-attacks/) и [Polski](https://blog.cloudflare.com/pl-pl/2022-07-sms-phishing-attacks/).

![The mechanics of a sophisticated phishing scam and how we stopped it](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44XYVSV0Q80CXCW0QHC2NE.png&w=1600&h=900&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAAgwBEiyZHn1JTtnJlxIJ0wX92qGdogjdNiTI+kE5WoXh9tJabvqGnuZifpHuDhlBZjkk2lWZipJOasrG/uLnKsqu8oIuXi2Jjkk8vmG5lp5yjtLrKuMHVsLHFoJCdjmdlkkUtmmRdqpKXua+6vbXEtqa1pIaQj11dkCQvmUlMrXV1v5KQx5mZwI2Oqm9yjURKjgAymA82rkw/xGpLz3VSyW1Rr1FGjBcyjQA0lwAprzAAxlMA0mEAzFwSsUAjiwAj)

Вчера, 8 августа 2022 года, компания Twilio сообщила, что она [подверглась целевой фишинговой атаке](https://www.twilio.com/blog/august-2022-social-engineering-attack). Примерно в то же время, когда была атакована Twilio, мы наблюдали атаку с очень похожими характеристиками, направленную также на сотрудников Cloudflare. Несмотря на то, что отдельные сотрудники «клюнули» на фишинговые сообщения, мы смогли предотвратить атаку с помощью собственных [продуктов Cloudflare One](https://www.cloudflare.com/cloudflare-one/) и благодаря физическим ключам безопасности, выдаваемым каждому сотруднику, которые необходимы для доступа ко всем нашим приложениям.

Мы подтвердили, что ни одна из систем Cloudflare не была скомпрометирована. Наша [команда Cloudforce One по сбору и анализу информации об угрозах](https://blog.cloudflare.com/introducing-cloudforce-one-threat-operations-and-threat-research/) смогла провести дополнительный анализ, чтобы более углубленно проанализировать механизм атаки и собрать важные доказательства для помощи в отслеживании злоумышленника.

Это была изощренная атака, нацеленная на сотрудников и системы таким образом, который, по нашему мнению, привел бы к взлому большинства организаций. Учитывая, что целью злоумышленников являлось несколько организаций, мы хотели поделиться здесь кратким и точным изложением того, что именно мы наблюдали, с тем, чтобы помочь другим компаниям распознать и нейтрализовать эту атаку.

## Целевые текстовые сообщения

20 июля 2022 года команда безопасности Cloudflare получила сообщения о том, что сотрудники получают выглядящие легитимными текстовые сообщения, ведущие на якобы страницу входа в Cloudflare Okta. Сообщения начали поступать 20.07.2022 в 22:50 UTC. В течение менее одной минуты по меньшей мере 76 сотрудников получили текстовые сообщения на свои личные и рабочие телефоны. Некоторые сообщения были также отправлены членам семей сотрудников. Мы пока не смогли определить, как злоумышленнику удалось собрать список телефонных номеров сотрудников, но проверили журналы доступа к нашим службам каталогов сотрудников и не обнаружили никаких признаков компрометации.

Cloudflare имеет группу реагирования на инциденты безопасности (SIRT — от англ. Security Incident Response Team), работающую в режиме 24x7. Каждый сотрудник Cloudflare проинструктирован сообщать обо всех подозрительных действиях в SIRT. Более 90 процентов сообщений, поступающих в SIRT, на деле оказываются не связанными с настоящими угрозами. Тем не менее, сотрудников поощряют сообщать обо всем, что им кажется подозрительным, и чрезмерное информирование никогда не является причиной неодобрения. Однако в данном случае сообщения в SIRT относились к реальной угрозе.

Текстовые сообщения, полученные сотрудниками, выглядели следующим образом:

Они поступили с четырех телефонных номеров, привязанных к СИМ-картам, выпущенным T-Mobile: (754) 268-9387, (205) 946-7573, (754) 364-6683 и (561) 524-5989. Текстовые сообщения включали официально выглядящий домен: cloudflare-okta.com. Этот домен был зарегистрирован через Porkbun, регистратор доменов, 20.07.2022 в 22:13:04 UTC — менее чем за 40 минут до начала фишинговой кампании.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1279 Embedded Image - mzDQx2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW458M23R42VF210NMM8NBN6.png&w=715&h=601&f=webp&fit=cover&position=center)

Cloudflare создала наш [продукт по безопасной регистрации](https://www.cloudflare.com/products/registrar/custom-domain-protection/) частично для того, чтобы иметь возможность отслеживать, когда домены, использующие бренд Cloudflare, были зарегистрированы, и принудительно закрывать их. Однако, поскольку этот домен был зарегистрирован совсем недавно, он еще не был опубликован как новая регистрация .com, поэтому наши системы не обнаружили его.

Нажимая на ссылку, пользователь попадал на фишинговую страницу. Фишинговая страница была размещена на DigitalOcean и выглядела следующим образом:

Cloudflare использует Okta в качестве нашего сервиса авторизации. Фишинговая страница была разработана таким образом, чтобы выглядеть идентично легитимной странице входа в Okta. Фишинговая страница запрашивала имя пользователя и пароль у каждого посещающего ее пользователя.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1279 Embedded Image - 5SXCpt](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45QS52KCAFCN2KSPGK32J4.png&w=715&h=536&f=webp&fit=cover&position=center)

## Фишинг в режиме реального времени

Мы смогли проанализировать код фишинговой атаки, основываясь на данных, полученных нашими сотрудниками, а также на контенте атаки, размещенном в таких сервисах, как VirusTotal, другими компаниями, подвергшимися атаке. После того как фишинговая страница заполнялась жертвой, учетные данные немедленно передавались злоумышленнику через службу обмена сообщениями Telegram. Эта передача в реальном времени имела важное значение, поскольку фишинговая страница также запрашивала код одноразового пароля с ограниченным сроком действия (TOTP — от англ. Time-based One Time Password).

Предположительно, злоумышленник получал учетные данные в режиме реального времени, вводил их на реальной странице входа в систему компании-жертвы, и для многих организаций это действие инициировало генерирование кода, отправляемого сотруднику через SMS или отображаемого в генераторе паролей. Затем сотрудник вводил код TOTP на фишинговом сайте, и он также передавался злоумышленнику. Затем, до истечения срока действия кода TOTP, злоумышленник мог использовать его для доступа к реальной странице входа в систему компании, что позволяло обойти большинство систем двухфакторной аутентификации.

## Обеспечение защиты, даже если она не является совершенной

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1279 Embedded Image - y0kAKQ](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48BDTY0D16K46QEKFRZ8VJ.png&w=715&h=250&f=webp&fit=cover&position=center)

Мы подтвердили, что трое сотрудников Cloudflare попались на фишинговое сообщение и ввели свои учетные данные. Однако Cloudflare не использует коды TOTP. Вместо этого каждому сотруднику компании выдается ключ безопасности, соответствующий FIDO2, от такого поставщика, как, в частности, YubiKey. Поскольку аппаратные ключи привязаны к пользователям и реализуют [привязку к источнику](https://www.yubico.com/blog/creating-unphishable-security-key/), даже такая изощренная фишинговая операция в режиме реального времени не может обеспечить сбор информации, необходимой для входа в любую из наших систем. Хотя злоумышленник попытался войти в наши системы, используя скомпрометированные данные имени пользователя и пароля, он не смог пройти проверку на основе аппаратного ключа.

Но эта фишинговая страница была создана не просто для получения учетных данных и кодов TOTP. Если тот или иной пользователь проходил эти этапы, фишинговая страница затем инициировала загрузку фишингового вредоносного кода, который включал программное обеспечение удаленного доступа AnyDesk. Это программное обеспечение, если оно установлено, позволит злоумышленнику удаленно управлять компьютером жертвы. Мы подтвердили, что никто из членов нашей команды не дошел до этого этапа. Однако, даже если бы кому-либо из них это удалось, наша система безопасности конечных точек остановила бы установку программного обеспечения для удаленного доступа.

## Как мы отреагировали?

Ниже перечислены основные меры реагирования, которые мы предприняли в связи с этим инцидентом:

### 1\. **Блокировка фишингового домена с помощью Cloudflare Gateway**

Cloudflare Gateway — это защищенный веб-шлюз, решение, обеспечивающее защиту от угроз и данных с помощью фильтрации DNS / HTTP и нативно интегрированной функции Zero Trust. Мы используем это решение внутри компании для превентивного выявления вредоносных доменов и их блокировки. Наша команда добавила вредоносный домен в Cloudflare Gateway, чтобы заблокировать доступ к нему для всех сотрудников.

Автоматическое обнаружение вредоносных доменов с помощью Gateway также позволило идентифицировать домен и заблокировать его, но тот факт, что домен был зарегистрирован и сообщения были отправлены в течение такого короткого промежутка времени, означал, что система не предприняла автоматических действий до того, как некоторые сотрудники перешли по ссылкам. Учитывая этот инцидент, мы работаем над тем, чтобы ускорить идентификацию и блокировку вредоносных доменов. Мы также внедряем средства контроля доступа к недавно зарегистрированным доменам, которые мы предлагаем клиентам, но не внедрили сами.

### 2\. **Определение всех затронутых сотрудников Cloudflare и сброс скомпрометированных учетных данных**

Мы смогли сравнить получателей фишинговых сообщений с действиями при входе в систему и выявить попытки злоумышленников пройти аутентификацию в учетных записях наших сотрудников. Мы идентифицировали попытки входа в систему, заблокированные на основе требований к наличию аппаратного ключа (U2F), указывающие на то, что был использован правильный пароль, но второй фактор не прошел проверку. В связи с утечкой учетных данных трех наших сотрудников мы сбросили их учетные данные и все активные сеансы, и инициировали сканирование их устройств.

### 3\. Выявление и устранение инфраструктуры злоумышленника

Фишинговый домен злоумышленника был недавно зарегистрирован через Porkbun и размещен на DigitalOcean. Фишинговый домен, использованный для атаки на Cloudflare, был создан менее чем за час до начала первой волны фишинговой атаки. Сайт имел клиентскую часть на Nuxt.js, а серверную часть — на Django. Мы работали с DigitalOcean над отключением сервера злоумышленника. Мы также сотрудничали с компанией Porkbun, чтобы взять под контроль вредоносный домен.

По неудачным попыткам входа в систему мы смогли определить, что злоумышленник воспользовался программным обеспечением Mullvad VPN и очевидно использовал браузер Google Chrome на компьютере с Windows 10. Злоумышленник использовал следующие IP-адреса VPN: 198.54.132.88 и 198.54.135.222. Эти IP-адреса присвоены Tzulo, американскому поставщику выделенных серверов, при этом согласно информации, представленной на их веб-сайте, у них имеются серверы, расположенные в Лос-Анджелесе и Чикаго. На самом же деле оказалось, что первый IP-адрес фактически работал на сервере в районе Торонто, а второй — на сервере в районе Вашингтона, округ Колумбия. Мы заблокировали для этих IP-адресов доступ к любым нашим сервисам.

### 4\. Обновление обнаружений для выявления последующих попыток атаки

С учетом того, что нам удалось выяснить об этой атаке, мы включили дополнительные сигналы в наши уже существующие обнаружения, с тем, чтобы конкретно идентифицировать этого злоумышленника. На момент написания статьи мы не наблюдали никаких дополнительных волн атак, нацеленных на наших сотрудников. Однако аналитическая информация с сервера показала, что злоумышленник нацеливался на другие организации, включая Twilio. Мы связались с этими организациями и поделились аналитической информацией о кибератаке.

### 5\. Аудит журналов доступа к сервисам для выявления дополнительных признаков атаки

После атаки мы проверили все наши журналы системы на наличие каких-либо дополнительных цифровых отпечатков этого конкретного злоумышленника. Поскольку Cloudflare Access служит центральной точкой управления для всех приложений Cloudflare, мы можем искать в журналах любые признаки взлома злоумышленником каких-либо систем. Учитывая, что объектом атаки стали телефоны сотрудников, мы также тщательно проверили журналы наших поставщиков каталогов сотрудников. Мы не нашли никаких доказательств компрометации.

## Извлеченные уроки и дополнительные шаги, которые мы предпринимаем

Мы извлекаем уроки из каждой атаки. Несмотря на то, что злоумышленник не добился успеха, мы вносим дополнительные коррективы на основе полученных сведений. Мы корректируем настройки Cloudflare Gateway, чтобы ограничить или изолировать доступ к сайтам, работающим на доменах, которые были зарегистрированы в течение последних 24 часов. Мы также будем запускать любые сайты, находящиеся в списке запрещенных сайтов, содержащие такие термины, как “cloudflare”, “okta”, “sso” и “2fa”, с помощью нашей технологии изоляции браузера. Кроме того, мы все чаще используем технологию идентификации фишинга Cloudflare Area 1 для сканирования Интернета и поиска любых страниц, нацеленных на Cloudflare. Наконец, мы ужесточаем нашу реализацию Access, чтобы предотвратить любые входы в систему из неизвестных VPN, резидентных прокси-серверов и поставщиков инфраструктуры. Все это на основе тех же стандартных функций, которые мы предлагаем клиентам.

Атака также подчеркнула важность трех аспектов, которые мы успешно реализуем. Первый аспект — требование аппаратных ключей для доступа ко всем приложениям. [Как и в Google](https://krebsonsecurity.com/2018/07/google-security-keys-neutralized-employee-phishing/), мы не наблюдали успешных фишинговых атак с момента развертывания аппаратных ключей. Такие инструменты, как Cloudflare Access, упростили поддержку аппаратных ключей даже в устаревших приложениях. Если вы представляете организацию, которая хотела бы получить дополнительную информацию по внедрению нами аппаратных ключей, вы можете обратиться по адресу [cloudforceone-irhelp@cloudflare.com](mailto:cloudforceone-irhelp@cloudflare.com), и наш отдел ИБ будет рад поделиться практическими рекомендациями, разработанными нами на основании этого процесса.

Второй аспект — использование собственной технологии Cloudflare для защиты наших сотрудников и систем. Решения Cloudflare One, такие как Access и Gateway, имели решающее значение для предотвращения этой атаки. Мы настроили нашу реализацию Access так, чтобы для каждого приложения требовались аппаратные ключи. Также в рамках этой реализации создается центральная локация журналирования для всех аутентификаций приложения. И, при необходимости, место, из которого мы можем прекратить сеансы потенциально скомпрометированного сотрудника. Gateway позволяет нам быстро закрывать вредоносные сайты, подобные этому, и понимать, какие сотрудники могли подвергнуться атаке. Все вышеперечисленные функциональные возможности представляются нами клиентам Cloudflare в составе пакета Cloudflare One, и эта атака демонстрирует их высокую эффективность.

Третий аспект — «сверхподозрительная», но при этом не связанная с порицанием культура имеет критическую важность для обеспечения безопасности. Трое сотрудников, попавшихся на фишинговую «удочку», не получили выговоров. Мы все люди, и мы совершаем ошибки. При этом крайне важно, что когда это с нами происходит, мы сообщали об ошибках и не скрывали их. Этот инцидент стал еще одним примером того, почему безопасность является частью работы каждого члена команды Cloudflare.

## Подробная хронология событий

.tg {border-collapse:collapse;border-spacing:0;} .tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px; overflow:hidden;padding:10px 5px;word-break:normal;} .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px; font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;} .tg .tg-0lax{text-align:left;vertical-align:top}

2022-07-20 22:49 UTC

Злоумышленник отправил более 100 SMS-сообщений сотрудникам Cloudflare и их семьям.

2022-07-20 22:50 UTC

Сотрудники начали сообщать о SMS-сообщениях в службу безопасности Cloudflare.

2022-07-20 22:52 UTC

Проверка блокировки домена злоумышленника в Cloudflare Gateway для корпоративных устройств.

2022-07-20 22:58 UTC

Предупреждающее сообщение отправлено всем сотрудникам через чат и электронную почту.

2022-07-20 22:50 UTC to2022-07-20 23:26 UTC

Мониторинг телеметрии в журнале системы Okta и журналах HTTP Cloudflare Gateway с целью обнаружения компрометации учетных данных. Очистка сеансов входа и приостановка учетных записей при обнаружении.

2022-07-20 23:26 UTC

Фишинговый сайт удален провайдером хостинга.

2022-07-20 23:37 UTC

Сброс скомпрометированных учетных данных сотрудников.

2022-07-21 00:15 UTC

Глубокий анализ инфраструктуры и возможностей злоумышленника.

## Индикаторы компрометации

.tg {border-collapse:collapse;border-spacing:0;} .tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px; overflow:hidden;padding:10px 5px;word-break:normal;} .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px; font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;} .tg .tg-nr0u{border-color:inherit;font-family:inherit;font-size:100%;text-align:left;vertical-align:top} .tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}

Value | Type | Context and MITRE Mapping  
---|---|---  
cloudflare-okta[.]com hosted on 147[.]182[.]132[.]52 | Phishing URL | [T1566.002](https://attack.mitre.org/techniques/T1566/002/): Phishing: Spear Phishing Link sent to users.  
64547b7a4a9de8af79ff0eefadde2aed10c17f9d8f9a2465c0110c848d85317a | SHA-256 | [T1219](https://attack.mitre.org/techniques/T1219/): Remote Access Software being distributed by the threat actor  
  
Значение

Тип

Контекст и сопоставление MITRE

cloudflare-okta[.]com с размещением на 147[.]182[.]132[.]52

Фишинговый URL-адрес

[T1566.002](https://attack.mitre.org/techniques/T1566/002/): Фишинг: целевая фишинговая ссылка, отправленная пользователям.

64547b7a4a9de8af79ff0eefadde2aed10c17f9d8f9a2465c0110c848d85317a

SHA-256

[T1219](https://attack.mitre.org/techniques/T1219/): Программное обеспечение для удаленного доступа, распространяемое злоумышленником

## Что вы можете предпринять

Если вы наблюдаете подобные атаки в своей среде, вы можете обратиться по адресу [cloudforceone-irhelp@cloudflare.com](mailto:cloudforceone-irhelp@cloudflare.com), и мы будем рады поделиться практическими рекомендациями по обеспечению безопасности вашего бизнеса. Если же вам интересно узнать больше о том, как мы внедрили ключи безопасности, ознакомьтесь с нашей [публикацией в блоге](https://blog.cloudflare.com/how-cloudflare-implemented-fido2-and-zero-trust/) или обратитесь по адресу: [securitykeys@cloudflare.com](mailto:securitykeys@cloudflare.com).

Возможно, вы хотите работать вместе с нами над обнаружением и нейтрализацией следующих атак? Мы набираем команду по обнаружению и реагированию. [Присоединяйтесь к нам](https://boards.greenhouse.io/cloudflare/jobs/4364485?gh_jid=4364485)!

На этой странице

Обсудить онлайн

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2F2022-07-sms-phishing-attacks%2F&t=%D0%9C%D0%B5%D1%85%D0%B0%D0%BD%D0%B8%D0%BA%D0%B0%20%D0%B8%D0%B7%D0%BE%D1%89%D1%80%D0%B5%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE%20%D1%84%D0%B8%D1%88%D0%B8%D0%BD%D0%B3%D0%BE%D0%B2%D0%BE%D0%B3%D0%BE%20%D0%BC%D0%BE%D1%88%D0%B5%D0%BD%D0%BD%D0%B8%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%B0%3A%20%D0%BA%D0%B0%D0%BA%20%D0%BD%D0%B0%D0%BC%20%D1%83%D0%B4%D0%B0%D0%BB%D0%BE%D1%81%D1%8C%20%D0%B5%D0%B3%D0%BE%20%D0%BF%D1%80%D0%B5%D0%B4%D0%BE%D1%82%D0%B2%D1%80%D0%B0%D1%82%D0%B8%D1%82%D1%8C)[](https://x.com/intent/post?text=%D0%9C%D0%B5%D1%85%D0%B0%D0%BD%D0%B8%D0%BA%D0%B0+%D0%B8%D0%B7%D0%BE%D1%89%D1%80%D0%B5%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE+%D1%84%D0%B8%D1%88%D0%B8%D0%BD%D0%B3%D0%BE%D0%B2%D0%BE%D0%B3%D0%BE+%D0%BC%D0%BE%D1%88%D0%B5%D0%BD%D0%BD%D0%B8%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%B0%3A+%D0%BA%D0%B0%D0%BA+%D0%BD%D0%B0%D0%BC+%D1%83%D0%B4%D0%B0%D0%BB%D0%BE%D1%81%D1%8C+%D0%B5%D0%B3%D0%BE+%D0%BF%D1%80%D0%B5%D0%B4%D0%BE%D1%82%D0%B2%D1%80%D0%B0%D1%82%D0%B8%D1%82%D1%8C&url=https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2F2022-07-sms-phishing-attacks%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2F2022-07-sms-phishing-attacks%2F)[](https://bsky.app/intent/compose?text=%D0%9C%D0%B5%D1%85%D0%B0%D0%BD%D0%B8%D0%BA%D0%B0+%D0%B8%D0%B7%D0%BE%D1%89%D1%80%D0%B5%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE+%D1%84%D0%B8%D1%88%D0%B8%D0%BD%D0%B3%D0%BE%D0%B2%D0%BE%D0%B3%D0%BE+%D0%BC%D0%BE%D1%88%D0%B5%D0%BD%D0%BD%D0%B8%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%B0%3A+%D0%BA%D0%B0%D0%BA+%D0%BD%D0%B0%D0%BC+%D1%83%D0%B4%D0%B0%D0%BB%D0%BE%D1%81%D1%8C+%D0%B5%D0%B3%D0%BE+%D0%BF%D1%80%D0%B5%D0%B4%D0%BE%D1%82%D0%B2%D1%80%D0%B0%D1%82%D0%B8%D1%82%D1%8C+https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2F2022-07-sms-phishing-attacks%2F)[](https://mastodonshare.com/?text=%D0%9C%D0%B5%D1%85%D0%B0%D0%BD%D0%B8%D0%BA%D0%B0+%D0%B8%D0%B7%D0%BE%D1%89%D1%80%D0%B5%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE+%D1%84%D0%B8%D1%88%D0%B8%D0%BD%D0%B3%D0%BE%D0%B2%D0%BE%D0%B3%D0%BE+%D0%BC%D0%BE%D1%88%D0%B5%D0%BD%D0%BD%D0%B8%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%B0%3A+%D0%BA%D0%B0%D0%BA+%D0%BD%D0%B0%D0%BC+%D1%83%D0%B4%D0%B0%D0%BB%D0%BE%D1%81%D1%8C+%D0%B5%D0%B3%D0%BE+%D0%BF%D1%80%D0%B5%D0%B4%D0%BE%D1%82%D0%B2%D1%80%D0%B0%D1%82%D0%B8%D1%82%D1%8C&url=https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2F2022-07-sms-phishing-attacks%2F)[](https://www.threads.net/intent/post?text=%D0%9C%D0%B5%D1%85%D0%B0%D0%BD%D0%B8%D0%BA%D0%B0+%D0%B8%D0%B7%D0%BE%D1%89%D1%80%D0%B5%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE+%D1%84%D0%B8%D1%88%D0%B8%D0%BD%D0%B3%D0%BE%D0%B2%D0%BE%D0%B3%D0%BE+%D0%BC%D0%BE%D1%88%D0%B5%D0%BD%D0%BD%D0%B8%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%B0%3A+%D0%BA%D0%B0%D0%BA+%D0%BD%D0%B0%D0%BC+%D1%83%D0%B4%D0%B0%D0%BB%D0%BE%D1%81%D1%8C+%D0%B5%D0%B3%D0%BE+%D0%BF%D1%80%D0%B5%D0%B4%D0%BE%D1%82%D0%B2%D1%80%D0%B0%D1%82%D0%B8%D1%82%D1%8C+https%3A%2F%2Fblog.cloudflare.com%2Fru-ru%2F2022-07-sms-phishing-attacks%2F)

## Связанные теги

[Cloudflare Access](https://blog.cloudflare.com/ru-ru/tag/cloudflare-access/)[Cloudflare Gateway](https://blog.cloudflare.com/ru-ru/tag/gateway/)[Phishing](https://blog.cloudflare.com/ru-ru/tag/phishing/)[Анализ после инцидента](https://blog.cloudflare.com/ru-ru/tag/post-mortem/)[Безопасность](https://blog.cloudflare.com/ru-ru/tag/security/)

Подписывайтесь в социальных сетях

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Подпишитесь на уведомления о новых публикациях

Электронная почта

Мы никогда не передаем ваш адрес электронной почты третьим лицам.

Подписаться

Спасибо за подписку! Проверьте папку «Входящие», чтобы подтвердить подписку.
