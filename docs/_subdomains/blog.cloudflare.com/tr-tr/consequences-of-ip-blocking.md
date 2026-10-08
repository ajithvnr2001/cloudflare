---
url: https://blog.cloudflare.com/tr-tr/consequences-of-ip-blocking/
title: IP adreslerini engellemenin istenmeyen sonu\u00e7lar\u0131 | Cloudflare Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:37:04.915285+00:00
---

# IP adreslerini engellemenin istenmeyen sonuçları | Cloudflare Blog

> Source: https://blog.cloudflare.com/tr-tr/consequences-of-ip-blocking/

[Blog](https://blog.cloudflare.com/tr-tr/)

[Better Internet](https://blog.cloudflare.com/tr-tr/tag/better-internet/)[Impact Week](https://blog.cloudflare.com/tr-tr/tag/impact-week/)[Internet Performance](https://blog.cloudflare.com/tr-tr/tag/internet-performance/)+11 etiket daha göster

4 Etiket4 etiketi göster

  * Gönderi Etiketleri
  * [Politika ve Hukuk](https://blog.cloudflare.com/tr-tr/tag/policy/)
  * Tüm etiketler
  * Eşleşen etiketler
  * Etiket bulunamadı
  * [Yapay zeka](https://blog.cloudflare.com/tr-tr/tag/ai/)
  * [Geliştiriciler](https://blog.cloudflare.com/tr-tr/tag/developers/)
  * [Cloudflare'de Yaşam](https://blog.cloudflare.com/tr-tr/tag/life-at-cloudflare/)
  * [Ortaklar](https://blog.cloudflare.com/tr-tr/tag/partners/)
  * [Politika ve Hukuk](https://blog.cloudflare.com/tr-tr/tag/policy/)
  * [Ürün Haberleri](https://blog.cloudflare.com/tr-tr/tag/product-news/)
  * [Radar](https://blog.cloudflare.com/tr-tr/tag/cloudflare-radar/)
  * [Güvenlik](https://blog.cloudflare.com/tr-tr/tag/security/)
  * [Hız ve Güvenilirlik](https://blog.cloudflare.com/tr-tr/tag/speed-and-reliability/)
  * [Sıfır Güven](https://blog.cloudflare.com/tr-tr/tag/zero-trust/)



[Politika ve Hukuk](https://blog.cloudflare.com/tr-tr/tag/policy/)

[Better Internet](https://blog.cloudflare.com/tr-tr/tag/better-internet/)[Impact Week](https://blog.cloudflare.com/tr-tr/tag/impact-week/)[Internet Performance](https://blog.cloudflare.com/tr-tr/tag/internet-performance/)[Politika ve Hukuk](https://blog.cloudflare.com/tr-tr/tag/policy/)

16 Aralık 2022

# IP adreslerini engellemenin istenmeyen sonuçları

![Alissa Starzak](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4751R7AC038HBQRXJWSDR3.png&w=64&h=64&f=webp&fit=cover&position=center)![Marwan Fayed](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4975XAXEZ77Q31PP9FF3ME.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Alissa Starzak](https://blog.cloudflare.com/tr-tr/author/alissa-starzak/) ve [Marwan Fayed](https://blog.cloudflare.com/tr-tr/author/marwan/)

19 dk okuma süresi

URL KOPYALA

Bu yazı ayrıca şu dillerde mevcut: [English](https://blog.cloudflare.com/consequences-of-ip-blocking/), [Deutsch](https://blog.cloudflare.com/de-de/consequences-of-ip-blocking/), [Español](https://blog.cloudflare.com/es-es/consequences-of-ip-blocking/), [Français](https://blog.cloudflare.com/fr-fr/consequences-of-ip-blocking/), [Italiano](https://blog.cloudflare.com/it-it/consequences-of-ip-blocking/), [日本語](https://blog.cloudflare.com/ja-jp/consequences-of-ip-blocking/), [한국어](https://blog.cloudflare.com/ko-kr/consequences-of-ip-blocking/), [繁體中文](https://blog.cloudflare.com/zh-tw/consequences-of-ip-blocking/), [简体中文](https://blog.cloudflare.com/zh-cn/consequences-of-ip-blocking/), [Português](https://blog.cloudflare.com/pt-br/consequences-of-ip-blocking/), [Русский](https://blog.cloudflare.com/ru-ru/consequences-of-ip-blocking/), [العربية](https://blog.cloudflare.com/ar-ar/consequences-of-ip-blocking/) ve [עברית](https://blog.cloudflare.com/he-il/consequences-of-ip-blocking/).

![The unintended consequences of blocking IP addresses](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW449XJ04Y3QH60682M0WYX7.png&w=1800&h=1013&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAAgSgAhzMAkkUAmlIxmVU9kU4xhj8AfS0AiSsAk0YAp2xOt4ZxuY59roR0m2lSiEEAkC4AnlUyuodwz6iV07Ojx6eZroV1k1AvlTAApVo+wpB62bSh3sCw0LOmtY6Bl1U8lzIApFcyv4hv0qmU1rSjyaiZsIZ2lVEvlTMAnksAsXBMvolwv5F9s4d1n2tTjUQAkzMAmDwAoU0Aplkto1s9mVQ0jEUAhDMAkjMAlDQAmjYAmzYAlTEAjCwAgykAfykA)

Ağustos ayı sonunda Cloudflare’ın müşteri destek ekibi, ağımızdaki sitelerin Avusturya’da kapalı olduğu hakkında şikayetler almaya başladı. Ekibimiz, Avusturya’da dışarıdan kısmi İnternet kesintisi gibi görünen şeyin kaynağını belirlemeye çalışmak için derhal harekete geçti. Bunun yerel Avusturya İnternet Servis Sağlayıcıları ile ilgili bir sorun olduğunu hemen fark ettik.

Ancak hizmet kesintisi teknik bir sorunun sonucu değildi. Daha sonra [medya raporlarından](https://www.derstandard.de/story/2000138619757/ueberzogene-netzsperre-sorgt-fuer-probleme-im-oesterreichischen-internet) öğrendiğimiz üzere, gördüğümüz şey bir mahkeme kararının sonucuydu. Bir Avusturya mahkemesi, Cloudflare’a herhangi bir bildirimde bulunmaksızın, Avusturya İnternet Servis Sağlayıcılarına (İSS’ler) Cloudflare’ın IP adreslerinin 11’ini bloke etmeleri talimatını vermişti.

Telif hakkı sahiplerinin telif hakkını ihlal ettiğini iddia ettiği 14 web sitesini engelleme girişiminde mahkeme tarafından verilen IP engeli, Avusturya’daki sıradan İnternet kullanıcılarının iki günlük bir süre boyunca binlerce web sitesine erişememesine yol açtı. Bu diğer binlerce sitenin hatası neydi? Hiçbir şey. Bunlar, internetin gerçek mimarisini yansıtan yasal çözüm ve sistemlerin inşa edilememesinden geçici olarak muzdarip oldu.

Bugün, IP engelleme üzerine bir tartışmaya gireceğiz: bunu neden görürüz, bu nedir, ne yapar, kimi etkiler ve içeriği çevrimiçi olarak ele almanın neden bu kadar sorunlu bir yoludur?

## İkincil etkiler, büyük ve küçük

En akıl almaz olanı, bu tür bir engellemenin dünyanın her yerinde düzenli olarak gerçekleşmesidir. Ancak bu engelleme Avusturya’da olanlar ölçeğinde gerçekleşmediği veya birisi bunu aydınlatmaya karar vermediği sürece, genellikle dış dünya tarafından görülemez. Kapsamlı teknik uzmanlığı bulunan ve engellemenin nasıl işlediğini anlayan Cloudflare dahi bir IP adresinin ne zaman engellendiğini rutin olarak göremez.

İnternet kullanıcıları için bu durum daha da opaktır. Genellikle neden belirli bir web sitesine bağlanamadıklarını, bağlantı sorununun nereden geldiğini veya nasıl ele alınacağını bilmezler. Sadece ziyaret etmeye çalıştıkları siteye erişemediklerini bilirler. Ve bu, IP adresi engellemesi nedeniyle siteler erişilemez hale geldiğinde durumun belgelendirilmesini zorlaştırabilir.

Engelleme uygulamaları da yaygındır. Freedom House, İnternette Özgürlük raporunda yakın zamanda inceledikleri 70 ülkeden 40’ının - Rusya, İran ve Mısır gibi ülkelerden Birleşik Krallık ve Almanya gibi Batı demokrasilerine kadar - bazı web sitelerini engellediğini [bildirmiştir](https://freedomhouse.org/report/freedom-net/2022/key-internet-controls). Rapor, bu ülkelerin engellemeyi tam olarak nasıl yaptığını incelemese de birçoğu Avusturya’da gördüğümüz kısmi İnternet kapatması için aynı potansiyel etkilerle IP engelleme biçimlerini kullanır.

IP engellemeden kaynaklanan ikincil zararın miktarını değerlendirmek zor olsa da kuruluşların bunu nicelleştirmeye çalıştığı örneklere sahibiz. Avrupa İnsan Hakları Mahkemesi’nin gördüğü bir dava ile, Slovakya merkezli kâr amacı gütmeyen bir kuruluş olan Avrupa Bilgi Topluluğu Enstitüsü, Rusya’nın 2017’de web sitesi engelleme rejimini incelemiştir. Rusya, içeriği engellemek için yalnızca IP adreslerini kullanmıştır. Avrupa Bilgi Topluluğu Enstitüsü, IP engellemenin “ _büyük ölçekte ikincil web sitesi engellemeye_ ” yol açtığı sonucuna varmış ve 28 Haziran 2017 itibarıyla “6.522.629 İnternet kaynağının Rusya’da engellendiğini ve bunun 6.335.850’sinin veya %97’sinin ikincil olarak, yani yasal bir gerekçe olmadan engellendiğini” belirtmiştir.

Birleşik Krallık’ta, son derece yaygın olan engelleme uygulaması, kâr amacı gütmeyen Open Rights Group’u [Blocked.org.uk](https://www.blocked.org.uk/) web sitesini oluşturmaya itmiştir. Web sitesinde, kullanıcıların ve site sahiplerinin son derece yaygın engelleme hakkında rapor vermesini ve İSS’lerin engelleri kaldırmasını talep etmesini sağlayan bir araç bulunmaktadır. Grupta ayrıca, engellemenin hayır kurumlarından küçük işletme sahiplerine kadar, web siteleri uygunsuz bir şekilde engellenmiş olanlar üzerindeki etkisi hakkında yüzlerce bireysel hikayeye sahip. Hangi engelleme yöntemlerinin kullanıldığı her zaman net olmasa da, genel olarak böyle bir sitenin gerekli olması fazladan engellemenin ne düzeyde yapıldığına dair bilgi vermektedir. Web sitesi ile hizmetlerinin reklamını yapmak ve potansiyel olarak yeni müşteriler kazanmak isteyen bir terzi, saatçi veya araba satıcısını düşünün. Yerel kullanıcılar siteye erişemezse bu hiçbir işe yaramaz.

Tepkilerden biri, “O zaman, kısıtlanmamış sitelerle aynı adresi paylaşan kısıtlı bir site olmadığından emin olun” olabilir. Ancak daha ayrıntılı olarak ele alacağımız gibi, bu, olası etki alanı adlarının sayısı ile mevcut IP adreslerinin sayısı arasındaki büyük farkı göz ardı eder ve İnterneti güçlendiren çok teknik özelliklere aykırı şekilde işler. Ayrıca kısıtlanmış ve kısıtlanmamış tanımları uluslar, topluluklar ve kuruluşlar arasında farklılık gösterir. Tüm kısıtlamaları bilmek mümkün olsa bile, protokollerin tasarımları -- İnternet’in kendisi -- her kurumun kısıtlamalarını karşılamanın imkansız olmasa bile mümkün olmadığı anlamına gelir.

## Hukuk ve insan hakları ile ilgili endişeler

Web sitelerinin son derece yaygın olarak engellenmesi sadece kullanıcılar için bir sorun değildir; yasal sonuçları da vardır. Haklarını çevrimiçi kullanmak isteyen sıradan vatandaşlar üzerindeki etkisi nedeniyle, devlet kurumları (hem mahkemeler hem de düzenleyici kurumlar) kararlarının gerekli ve orantılı olmasını sağlamak konusunda yasal bir yükümlülüğe sahiptir ve zarara katkıda bulunmayanları gereksiz yere etkilememelidir.

Örneğin, iddia edilen yanlış davranışa yanıt olarak bir mahkemenin, söz konusu adres tek bir aile evi, altı birimli bir apartman dairesi bina veya yüzlerce ayrı birimle yüksek bir apartman için olsaydı, yalnızca bir sokak adresine dayalı olarak bir arama emrini vereceğini ya da rastgele bir arama emri vereceğini hayal etmek zor olurdu. Ancak IP adreslerinde bu tür uygulamalar yaygın görünmektedir.

2020 yılında Avrupa Konseyi’nin İnsan Hakları Avrupa Sözleşmesi’nin uygulanmasını denetleyen mahkeme olan Avrupa İnsan Hakları Mahkemesi (AİHM), Rusya hükümeti tarafından hedef alındığı için değil, engellenmiş bir web sitesi ile aynı IP adresini paylaştığı için Rusya’da engellenmiş olan bir web sitesini içeren bir davayı değerlendirdi. Web sitesi sahibi engel ile ilgili olarak bir dava açtı. AİHM, sitenin yasal içeriğine yapılan engellemenin “ _bu tür web sitelerinin sahiplerinin haklarına keyfi müdahaleye karşılık geldiğine_ ” karar vererek, ayrımcılık içermeyen engellemeye izin verilmediği sonucuna varmıştır. Başka bir deyişle, AİHM bir devletin hedeflenmeyen sitelerin engellenmesiyle sonuçlanan emirler vermesinin uygunsuz olduğuna karar vermiştir.

## İçerik zorluklarını ele almak için İnternet altyapısını kullanma

Sıradan İnternet kullanıcıları, çevrimiçi olarak erişmeye çalıştıkları içeriğin kendilerine nasıl sunulduğu hakkında pek düşünmezler. Tarayıcılarına bir etki alanı adı yazdıklarında, içeriğin otomatik olarak açılacağını varsayarlar. Ve açılmazsa, tüm İnternette bağlantı kopması olmadığı sürece web sitesinin kendisinin sorun yaşadığını varsayma eğilimindedirler. Ancak bu temel varsayımlar, bir web sitesine yönlendiren bağlantıların çevrimiçi içeriğe erişimi sınırlamak için sıklıkla kullanıldığı gerçeğini göz ardı eder.

Ülkeler web sitelerine yönlendiren bağlantıları neden engelliyor? Kendi vatandaşlarının dünyanın başka yerlerinde izin verilen çevrimiçi kumar veya açık materyal gibi yasa dışı içerik olduğunu düşündükleri alanlara erişimini sınırlandırmak istiyor olabilirler. Belki de esasen yanlış bilgi verdiğine inandıkları bir yabancı haber kaynağının görüntülenmesini önlemek istiyor olabilirler. Veya fikri mülkiyetlerini ihlal ettiğine inandıkları içeriğin görüntülenmesini sınırlandırmak üzere bir web sitesine erişimi engellemek isteyen telif hakkı sahiplerini desteklemek istiyor olabilirler.

Açık olmak gerekirse, **erişimi engellemek içeriği İnternetten kaldırmakla aynı şey değildir**. Yasa dışı içeriğin fiili olarak kaldırılmasına izin vermek için tasarlanmış çeşitli yasal yükümlülükler ve makamlar vardır. Gerçekten de, birçok ülkede yasal beklenti, kaynaktaki içeriği kaldırma girişimlerinde bulunulduktan sonra engellemenin son çare olmasıdır.

Engelleme yalnızca belirli tarafları etkiler; internet erişimi engellemesini gerçekleştiren İSS’ye bağlı olan belirli izleyicilerin web sitelerine erişebilmesini engeller. Sitenin kendisi çevrimiçi olarak var olmaya ve herkes tarafından erişilebilmeye devam eder. Ancak içerik farklı bir yerden geldiğinde ve kolayca kaldırılamadığında, bir ülke engellemeyi en iyi veya tek yaklaşım olarak görebilir.

Bazen ülkeleri engellemeyi uygulamaya iten endişelerin farkındayız. Ancak temel olarak, kullanıcıların erişmeye çalıştıkları web sitelerinin ne zaman engellendiğini ve mümkün olduğu ölçüde kimlerin bunları görmesinin neden engellendiğini bilmelerinin önemli olduğuna inanıyoruz. Ayrıca başkalarının haklarını ihlal etmekten kaçınmak için, içerik üzerindeki kısıtlamaların mümkün olduğunca zararı ele almakla sınırlı tutulması çok önemlidir.

Kaba kuvvetle IP adresinin engellenmesi buna izin vermez. Bu, İnternet kullanıcıları için tamamen opaktır. Uygulamanın diğer içerikler üzerinde istenmeyen, kaçınılmaz sonuçları vardır. Ve İnternetin yapısı gereği bir IP engellemesi öncesinde veya sırasında başka web sitelerinin etkilenmesinin olası olup olmadığını belirlemenin iyi bir yolu yoktur.

Avusturya’da ve IP adreslerinin körlüğü ile içeriği engellemeye çalışan dünyanın diğer pek çok ülkesinde neler yaşandığını anlamak için sahne arkasında neler olduğunu anlamamız gerekiyor. Bu da bazı teknik ayrıntılara inilmesi anlamına geliyor.

## Kimlik adlara eklidir, adreslere değil

Engellemenin teknik gerçeklerini açıklamaya başlamadan önce, içerikle başa çıkmak için ilk ve en iyi seçeneğin kaynakta olduğunu vurgulamak önemlidir. Bir web sitesi sahibi veya yer sağlayıcı, web sitesinin tamamını indirmek zorunda kalmadan içeriği granüler düzeyde kaldırma seçeneğine sahiptir. Daha teknik bir tarafta, bir etki alanı adı kaydedici ya da sicili potansiyel olarak bir etki alanı adını ve dolayısıyla bir web sitesini İnternetten tamamen geri çekebilir.

Ancak herhangi bir nedenle içerik sahibi veya içerik kaynağı ilgili içeriği internetten kaldıramıyorsa veya kaldırmak istemiyorsa, bir web sitesine erişimi nasıl engellersiniz? Yalnızca üç olası kontrol noktası vardır.

Birincisi, sitenin bulunabilmesi için etki alanı adlarını IP adreslerine çeviren Etki Alanı Adı Sistemi (DNS) aracılığıyladır. DNS çözücüsü, bir etki alanı adı için geçerli bir IP adresi vermek yerine yalan söyleyerek “böyle bir ad yoktur” anlamına gelen NXDOMAIN kodu ile yanıt verebilir. Engellenen için hata 15, sansürlenen için hata 16, filtrelenen için 17 veya yasaklanan için 18 dahil olmak üzere [2020’de standardize edilen](https://datatracker.ietf.org/doc/rfc8914/) dürüst hata numaralarından birini kullanmak daha iyi bir yaklaşım olacaktır ancak bunlar şu anda yaygın olarak kullanılmamaktadır.

İlginç bir şekilde, DNS’nin bir kontrol noktası olarak hassasiyeti ve etkinliği, DNS çözücüsünün özel veya genel olmasına bağlıdır. Özel veya ‘dahili’ DNS çözücüleri, İSS’ler ve kurumsal ortamlar tarafından kendi bilinen istemcileri için çalıştırılır, bu da operatörlerin içerik kısıtlamalarını uygulama konusunda hassas olabileceği anlamına gelir. Bunun aksine, bu hassasiyet seviyesi, yalnızca yönlendirme ve adreslemenin küresel olması ve İnternet haritasında sürekli olarak değişmesi ve sabit bir posta veya sokak haritasındaki adres ve rotaların tam tersi olması nedeniyle, açık veya genel çözümleyiciler için kullanılamaz. Örneğin, özel DNS çözümleyicileri, genel DNS çözümleyicilerinin yapamayacağı şekilde en azından belirli coğrafi bölgelerdeki web sitelerine erişimi engelleyebilir ve bu da dünya genelindeki farklı (ve tutarsız) engelleme rejimleri göz önüne alındığında çok önemli hale gelir.

İkinci yaklaşım, kısıtlı bir etki alanı adına yönelik bireysel bağlantı isteklerini engellemektir. Bir kullanıcı veya istemci bir web sitesini ziyaret etmek istediğinde, istemciden bir sunucu _adına_ , yani etki alanı adına bir bağlantı başlatılır. Bir ağ veya yoldaki cihaz sunucu adını gözlemleyebiliyorsa, bağlantı sonlandırılabilir. DNS’nin aksine, sunucu adına erişimin engellendiğine dair kullanıcı ile iletişim kurma mekanizması yoktur.

Üçüncü yaklaşım, etki alanı adının bulunabileceği bir IP adresine erişimi engellemektir. Bu, tüm postaların fiziksel bir adrese gönderilmesini engellemek gibidir. Örneğin, bu adresin pek çok ilgisiz ve bağımsız sakini olan bir gökdelen olduğunu düşünün. Gökdelen adresine posta gönderiminin durdurulması, o adresteki tüm tarafları sürekli olarak etkileyerek ikincil zarara neden olur. IP adresleri de aynı şekilde çalışır.

IP adresi, üç seçenek arasında tek etki alanı adına bağlı olmayandır. Web sitesi alan adı, veri paketlerinin yönlendirilmesi ve iletilmesi için gerekli değildir; aslında tamamen göz ardı edilir. Bir web sitesi, herhangi bir IP adresinde ve hatta birçok IP adresinde aynı anda sunulabilir. Ve bir web sitesinin açık olduğu IP adresleri kümesi herhangi bir zamanda değiştirilebilir. IP adresleri kümesi, [1995](https://datatracker.ietf.org/doc/rfc1794/)‘ten bu yana herhangi bir zamanda herhangi bir nedenle herhangi bir geçerli adresi geri getirebilen DNS sorgulamasıyla _kesin olarak_ bilinememektedir.

Bir adresin bir kimliği temsil ettiği fikri, İnternet tasarımına yönelik bir yaklaşımdır çünkü adresin addan ayrılması, aşağıda açıklandığı gibi İnternet standartlarına ve protokollerine derinlemesine gömülüdür.

## İnternet bir politika veya bakış açısı değil, bir dizi protokoldür

Birçok kişi yine de yanlış bir şekilde bir IP adresinin tek bir web sitesini temsil ettiğini varsayar. İnternetin en erken bağlanan bileşenlerinin tek bir bilgisayar, tek bir arayüz, tek bir adres ve tek bir ad olarak görünmesi nedeniyle adlar ve adresler arasındaki ilişkinin anlaşılabilir olduğunu daha önce [belirtmiştik](https://blog.cloudflare.com/addressing-agility/). Bu birebir ilişki, İnternet Protokolünün dağıtıldığı ekosistemin bir yapay olgusuydu ve zamanın ihtiyaçlarını karşıladı.

İnternetin ilk zamanlarındaki bire bir adlandırma uygulamasına rağmen, bir sunucuya (veya ‘ana bilgisayara’) birden fazla ad atamak her zaman mümkün olmuştur. Örneğin, bir sunucu sıklıkla ‘`mail.example.com`’ ve ‘`www.example.com`’ gibi hizmet tekliflerini yansıtacak şekilde isimlerle yapılandırılırdı (ve hala bu şekilde yapılandırılmaktadır) ancak bunlar bir temel etki alanı adını paylaşırdı. Tamamen farklı web sitelerini tek bir sunucuda bir araya getirme ihtiyacı duyulana kadar tamamen farklı etki alanı adlarına sahip olmak için birkaç neden vardı. Bu uygulama, 2003 yılında [TLS uzantısında](https://datatracker.ietf.org/doc/rfc3546/) SNI alanı tarafından korunan bir özellik olan [HTTP/1.1](https://datatracker.ietf.org/doc/rfc2068/)‘deki Ana bilgisayar üst bilgisi ile 1997 yılında daha kolay hale getirildi.

Bu değişiklikler boyunca, İnternet Protokolü ve ayrıca DNS protokolü sadece hızı korumakla kalmadı aynı zamanda temel olarak değişmeden kaldı. İnternetin ölçeklendirilebilmesinin ve gelişebilmesinin nedeni budur çünkü adresler, erişilebilirlik ve IP adresi ilişkileri için rastgele ad ile ilgilidirler.

IP ve DNS tasarımları da tamamen bağımsızdır, bu da yalnızca adların adreslerden ayrı olduğu savını güçlendirmektedir. Protokollerin tasarım öğelerinin daha yakından incelenmesi, günümüzde yaygın hale gelen IP adreslerini engelleyerek içeriğe erişimi kontrol etme uygulamasına yol açan politikaların yanlış algılarını aydınlatır.

### IP, tasarım gereği yalnızca erişilebilirlik içindir ve başka hiçbir amaç taşımaz

Büyük kamu inşaat mühendisliği projelerinin yapı kurallarına ve en iyi uygulamalara dayandığı gibi, İnternet de deneyimlere dayalı olarak ve uluslararası fikir birliği ile kabul edilen bir dizi _açık_ standart ve spesifikasyon kullanılarak oluşturulmuştur. Donanım ve uygulamaları birbirine bağlayan İnternet standartları, Internet Engineering Task Force ([IETF](https://www.ietf.org/)) tarafından “Yorum Talebi” veya [RFC’ler](https://www.ietf.org/standards/rfcs/) şeklinde yayınlanır -- bu adlandırma, standartların eksiklik olmadığını gösterme amacı taşımaz, bu standartların bilgi ve deneyimle gelişebileceğini yansıtmayı amaçlar. IETF ve RFC’leri, iletişimin yapı temelinde yer alır; örneğin, ilk RFC 1 1969’da yayınlanmıştır. İnternet Protokolü (IP) spesifikasyonu 1981 yılında [RFC durumuna](https://datatracker.ietf.org/doc/rfc791/) ulaştı.

Standartlarla ilgili kuruluşların yanı sıra, İnternet’in başarısına, yıllarca süren deneme ve yanılma [deneyimine](https://en.wikipedia.org/wiki/End-to-end_principle) dayalı olarak 1981 yılında da [kodlanan](https://web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdf), uçtan uca (e2e) ilkesi olarak bilinen temel bir fikir yardımcı olmuştur. Uçtan uca ilkesi, birçok şekilde olmasına rağmen İnternet Protokolü spesifikasyonunun temel bir kavramını ortaya koyan güçlü bir soyutlamadır: ağın tek sorumluluğu erişilebilirliği belirlemektir ve diğer olası tüm özelliklerin maliyeti veya riski vardır.

İnternet Protokolünde “ulaşılabilirlik” fikri de IP adreslerinin kendi tasarımında yer almaktadır. İnternet Protokolü spesifikasyonu olan [RFC 791](https://www.rfc-editor.org/rfc/rfc791)‘e bakıldığında, Bölüm 2.3’ten aşağıdaki alıntı, adlar, arayüzler veya başka herhangi bir unsurla hiçbir ilişkisi olmayan IP adresleri hakkında açıktır.

Tıpkı fiziksel dünyadaki gökdelenlerin posta adresleri gibi, IP adresleri de bir kağıda yazılmış sokak adreslerinden daha fazlası değildir. Kağıt üzerindeki bir sokak adresi gibi, bir IP adresinin ardında bulunan varlıklar veya kuruluşlar hakkında da asla emin olunamaz. Cloudflare’ınki gibi bir ağda, herhangi bir tek IP adresi [binlerce sunucuyu](https://blog.cloudflare.com/cloudflare-architecture-and-how-bpf-eats-the-world/) temsil eder ve İnternet Protokolü bunu sağlamak için tasarlandığından, bazı durumlarda sayısı [milyonlara](https://blog.cloudflare.com/addressing-agility/) ulaşan daha fazla web sitesine ve hizmete sahip olabilir.
    
    
    Addressing
    
        A distinction is made between names, addresses, and routes [4].   A
        name indicates what we seek.  An address indicates where it is.  A
        route indicates how to get there.  The internet protocol deals
        primarily with addresses.  It is the task of higher level (i.e.,
        host-to-host or application) protocols to make the mapping from
        names to addresses.   The internet module maps internet addresses to
        local net addresses.  It is the task of lower level (i.e., local net
        or gateways) procedures to make the mapping from local net addresses
        to routes.
                                [ RFC 791, 1981 ]

İşte ilginç bir soru: biz veya herhangi bir içerik hizmeti sağlayıcısı, her IP adresinin tek bir adla eşleştiğinden emin olabilir miyiz? Yanıt, kesin bir **hayırdır** ve burada da bunun nedeni protokol tasarımı -- bu durumda DNS’dir.

### DNS’deki ad sayısı her zaman kullanılabilir adresleri aşar

İnternet spesifikasyonları gereği fiziksel dünyada mümkün olmadığı gibi adlar ve adresler arasında da birebir ilişki kurulması mümkün değildir. Bir an için insanların ve kuruluşların adresleri değiştirebileceğini göz ardı edin. Temel olarak, gezegendeki insan ve kuruluşların sayısı posta adresi sayısını aşmaktadır. Yalnızca İnternetin adreslerden daha fazla ad barındırmasını istemiyoruz, aynı zamanda buna _ihtiyacımız var_.

Adlar ve adresler arasındaki büyüklük farkı da spesifikasyonlarda kodlanmıştır. IPv4 adresleri 32 bit, IPv6 adresleri 128 bittir. DNS tarafından sorgulanabilecek bir etki alanı adının boyutu 253 sekiz bitli bayt veya 2.024 bit’e kadardır (1987 yılında yayınlanan [RFC 1035](https://datatracker.ietf.org/doc/rfc1035/)‘te Bölüm 2.3.4’ten). Aşağıdaki tablo bu farklılıkların perspektife yerleştirilmesine yardımcı olur:

15 Kasım 2022’de Birleşmiş Milletler, Dünya nüfusunun sekiz milyar insanı aştığını duyurdu. Sezgisel olarak, bu kadar çok sayıda posta adresinin olamayacağını biliyoruz. Gezegendeki olası isim sayısı ile benzer şekilde internetteki isim sayısı arasındaki fark, kullanılabilir adres sayısını aşmaktadır ve aşmalıdır.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1551 Embedded Image - hPqYbc](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45909CPT6GR2D09QV1G0HN.png&w=715&h=413&f=webp&fit=cover&position=center)

## Kanıt değer isimlerinde!

Uluslararası standartlarda IP adresleri ve DNS adları hakkındaki bu iki ilgili ilke anlaşıldığına göre, IP adresi ve alan adlarının farklı amaçlara hizmet ettiği ve ikisi arasında teke tek bir ilişki olmadığı anlaşıldığından, IP adreslerinin kullanıldığı yakın tarihli bir içerik engelleme vakasının incelenmesi, bunun sorunlu olmasının nedenlerini görmeye yardımcı olabilir. Örneğin, Ağustos 2022’nin sonunda Avusturya’da IP engelleme olayını ele alalım. Amaç, 11 IP adresini engelleyerek 14 hedef etki alanına erişimi kısıtlamaktı (kaynak: RTR.Telekom. [İnternet Arşivi](https://web.archive.org/web/20220828220559/http://netzsperre.liwest.at/) aracılığıyla yayınlanan gönderi) -- bu iki sayı arasındaki uyumsuzluk, IP engellemenin istenen etkiye sahip olmayabileceğine dair bir uyarı işareti olmalıdır.

Analojiler ve uluslararası standartlar, IP engellemesinin önlenmesinin nedenlerini açıklayabilir ancak internet ölçeğindeki verilere bakarak sorunun ne ölçekte olduğunu görebiliriz. IP engellemenin ciddiyetini daha iyi anlamak ve açıklamak için, etki alanı adlarının ve IP adreslerinin global bir görünümünü oluşturmaya karar verdik (bu çalışma için bir doktora araştırma stajyeri olan Sudheesh Singanamalla’ya teşekkür ederiz). Eylül 2022’de, üst düzey etki alanları (TLD’ler) .com, .net, .info ve .org için yetkili bölge dosyalarını, en üst düzey 1 milyon web sitesi listesiyle birlikte toplam 255.315.270 benzersiz ad bulmak için kullandık. Daha sonra beş bölgenin her birinden DNS sorgulaması yaptık ve geri dönen IP adresleri kümesini kaydettik. Aşağıdaki tablo bulgularımızı özetlemektedir:

Yukarıdaki tablo, gezegendeki herhangi bir bölgeden 255.315.270 milyon ada ulaşmak için en fazla 10,7 milyon adres gerektiğini ve bu adlar için her yerden toplam IP adresi kümesinin yaklaşık 16 milyon olduğunu açıkça belirtmektedir -- adların IP adreslerine oranı Avrupa’da yaklaşık 24 kat ve küresel olarak 16 kattır.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1551 Embedded Image - vSW7R3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4683YP7SEMSDBQY92FA1K1.png&w=715&h=285&f=webp&fit=cover&position=center)

Yukarıdaki sayılar hakkında dişe dokunur bir ayrıntı daha vardır: IP adresleri, hem IPv4 hem de IPv6 adreslerinin birleşik toplamlarıdır, yani 255 milyon web sitesinin tümüne ulaşmak için çok daha az adres gerekir.

Ayrıca bazı ilginç gözlemleri bulmak için verileri birkaç farklı şekilde inceledik. Örneğin, aşağıdaki şekil her bir ek IP adresi ile ziyaret edilebilecek web sitelerinin oranının kümülatif dağılımını (CDF) göstermektedir. Y ekseninde, bazı IP adreslerine ulaşılabilecek web sitelerinin oranı vardır. X ekseninde, 16 milyon IP adresi soldaki en fazla etki alanından sağdaki en az etki alanına kadar sıralanır. Bu kümedeki herhangi bir IP adresinin DNS’den gelen bir yanıt olduğunu ve bu nedenle en az bir etki alanı adına sahip olması gerektiğini ancak küme numarasındaki IP adreslerindeki en yüksek etki alanı sayısının 8 basamaklı milyonlar olduğunu unutmayın.

CDF’ye bakıldığında acı birkaç gözlem vardır:

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1551 Embedded Image - fhYNQJ](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44N1QXY0M60YVQWSBF2YVC.png&w=715&h=298&f=webp&fit=cover&position=center)

  * Kümedeki alanların %20’sine veya yaklaşık 51 milyonuna ulaşmak için 10’dan az IP adresine ihtiyaç vardır;
  * 100 IP, etki alanlarının neredeyse %50’sine ulaşmak için yeterlidir;
  * 1000 IP, etki alanlarının %60’ına ulaşmak için yeterlidir;
  * 10.000 IP, %80 oranda veya yaklaşık 204 milyon etki alanına ulaşmak için yeterlidir.



Aslında, toplam 16 milyon adreslik kümeden, veri kümesindeki adreslerin yarısından azı, 7,1 milyonu (%43,7) tek bir ada sahipti. Bu noktada ek olarak açık olmamız gerekir: bu adreslerde yalnızca bir ad olup olmadığını belirleyemiyoruz çünkü yalnızca .com, .org, .info. ve .net’te bulunanlardan daha fazla alan adı var, yani bu adreslerde başka adlar da olabilir.

Tek bir IP adresinde bir dizi etki alanına sahip olmanın yanı sıra, herhangi bir IP adresi bu etki alanlarının herhangi biri için zaman içinde değişebilir. IP adreslerinin periyodik olarak değiştirilmesi, belirli güvenlik ve performans uygulamaları için ve web sitelerinin güvenilirliğini artırmak için faydalı olabilir. Birçok işlemde kullanılan yaygın bir örnek yük dengelemedir. Bu, DNS sorgularının aynı web siteleri için zaman içinde veya farklı yerlerde farklı IP adresleri getirebileceği anlamına gelir. Bu, IP adreslerine dayalı engellemenin zaman içinde amacına hizmet etmemesinin daha başka ve ayrı bir nedenidir.

Nihayetinde, DNS’deki tüm adları, gezegendeki her konumdan, her zaman denetlemeden **bir IP adresindeki etki alanlarının sayısını bilmenin güvenilir bir yolu yoktur** , bu tamamen olanaksızdır.

Bir IP adresi üzerindeki herhangi bir eylemin, İnterneti yöneten ve güçlendiren protokollerin tam tanımları gereği, ikincil etkilere sahip olması beklenmelidir.

## IP engellemede şeffaflık eksikliği

Bir IP adresinin engellenmesi ikincil etkileri beraberinde getiriyorsa ve genellikle üzerinde birden fazla etki alanı bulunan IP adreslerini engelleyerek yaygın engellemenin uygunsuz veya hatta yasal olarak izinsiz olduğu kabul ediliyorsa neden hala bu uygulamaya başvuruluyor? Bunu kesin olarak bilmek zordur bu nedenle sadece tahminde bulunabiliriz. Bu bazen, özellikle teknoloji uzmanı olmayan yargıçlar gibi tüzel kişilerden kaynaklanan olası etkiler hakkında teknik bir anlayış eksikliğini yansıtır. Bazen devletler, internet kapatmalarında olduğu gibi ikincil zararları göz ardı ederler çünkü engellemeyi kendi çıkarları için gerekli görürler. Ve ikincil zarar oluştuğunda, genellikle dış dünya için fark edilir değildir bu nedenle ele alınmasına yönelik çok az dış baskı olabilir.

Bu noktanın vurgulanması önemlidir. Bir IP engellendiğinde, bir kullanıcı yalnızca başarısız bir bağlantı görür. Bağlantının neden başarısız olduğunu veya kimin başarısız olmasına neden olduğunu bilmezler. Öte yandan web sitesi adına hareket eden sunucu, kullanılamadığı hakkında şikayetler almaya başlayana kadar engellendiğini bile bilmez. Yaygın engellemede neredeyse hiçbir şeffaflık veya hesap verebilirlik yoktur. Ve bir web sitesi sahibinin bir engele itiraz etmesi veya uygunsuz bir şekilde engellendiği için telafi istemesi imkansız olmasa bile zor olabilir.

[Avusturya](https://www.rtr.at/TKP/was_wir_tun/telekommunikation/weitere-regulierungsthemen/netzneutralitaet/nn_blockings.de.html) da dahil olmak üzere bazı hükümetler, şeffaflık için önemli bir adım olan aktif engel listeleri yayınlamaktadır. Ancak tartıştığımız tüm nedenlerden dolayı, bir IP adresi yayınlamak, istemeden engellenmiş olabilecek tüm siteleri ortaya çıkarmaz. Ayrıca, etkilenenlere yaygın engellemeye meydan okumaları için bir yol sağlamaz. Yine, fiziksel dünya örneğinde, bir gökdelen ile ilgili olarak kapıda ilan edilmeyecek bir mahkeme emri verilebileceğini hayal etmek zordur ancak genellikle sanal alanda bu tür gerekli süreçleri ve bildirim gerekliliklerini atlarız.

IP engellemenin sorunlu sonuçları hakkında konuşmanın her zamankinden daha önemli olduğunu düşünüyoruz çünkü giderek artan sayıda ülke içeriği çevrimiçi olarak engellemeye çalışıyor. Ne yazık ki, İSS’ler bu gereklilikleri uygulamak için sıklıkla IP engellerini kullanıyor. İSS’nin daha büyük muadillerinden daha yeni veya daha az sağlam olması söz konusu olabilir ancak daha büyük İSS’ler de uygulamada yer alır ve bu anlaşılırdır çünkü IP engelleme en az çabayı gerektirir ve çoğu donanımda kolayca kullanılabilir.

Ve aynı sayıda IP adresine her geçen gün daha fazla etki alanı dahil edildiğinden, sorun daha da kötüleşecektir.

## Sonraki adımlar

Peki ne yapabiliriz?

İlk adımın, IP engelleme kullanımı konusunda şeffaflığı artırmak olduğuna inanıyoruz. IP engellemenin neden olduğu ikincil zararı belgelemenin kapsamlı bir yolunu bilmesek de uygulama hakkında farkındalığı artırmak için atabileceğimiz adımlar olduğuna inanıyoruz. Cloudflare Radar Outage Center ile yaptığımız gibi, bu içgörüleri vurgulayan yeni girişimler üzerinde çalışmaya kararlıyız.

Ayrıca bunun özünde bir İnternet sorunu olduğunu ve bu nedenle daha geniş bir çabanın parçası olması gerektiğini de biliyoruz. IP adresini engellemenin, ilgisiz (ve hedeflenmemiş) bir dizi etki alanına erişimi kısıtlaması ile sonuçlanma olasılığı, bu uygulamayı herkes için umutsuz bir girişim haline getirmelidir. Bu nedenle, içerik zorluklarını ele almanın bir yolu olarak IP adreslerini engellemenin kullanılmasına itiraz etmek ve gördüklerinde ikincil zararı belirtmek için seslerini duyurmak üzere sivil toplum ortakları ve benzer düşünce yapısına sahip şirketlerle iş birliği yapıyoruz.

Açık olmak gerekirse, çevrimiçi olarak yasa dışı içeriğin zorluklarını ele almak için, ülkeler içeriğin haklara saygı gösteren bir şekilde kaldırılmasını veya kısıtlanmasını sağlayan yasal mekanizmalara ihtiyaç duyar. İçeriği kaynakta ele almanın neredeyse her zaman en iyi ve gerekli ilk adım olduğuna inanıyoruz. AB’nin yeni Dijital Hizmetler Yasası veya Dijital Binyıl Telif Hakkı Yasası gibi yasalar, önemli gerekli süreç ilkelerine saygı gösterirken, kaynaktaki yasa dışı içeriği ele almak için kullanılabilecek araçlar sağlar. Hükümetler, insan hakları beklentileriyle tutarlı olarak, diğer insanların haklarını asgari düzeyde etkileyecek şekilde yasal mekanizmalar oluşturmaya ve uygulamaya odaklanmalıdır.

Çok açık bir şekilde, bu ihtiyaçlar IP adresleri engellenerek karşılanamaz.

Özellikle erişimde gereksiz sınırlamalara yol açtığında, ağ faaliyeti ve aksaklık hakkında konuşmanın yeni yollarını aramaya devam edeceğiz. Çevrimiçi olarak gördüklerimiz hakkında daha fazla bilgi için [Cloudflare Radar](https://radar.cloudflare.com/)‘a göz atın.

Bu sayfada

Çevrimiçi tartış

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Ftr-tr%2Fconsequences-of-ip-blocking%2F&t=IP%20adreslerini%20engellemenin%20istenmeyen%20sonu%C3%A7lar%C4%B1)[](https://x.com/intent/post?text=IP+adreslerini+engellemenin+istenmeyen+sonu%C3%A7lar%C4%B1&url=https%3A%2F%2Fblog.cloudflare.com%2Ftr-tr%2Fconsequences-of-ip-blocking%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Ftr-tr%2Fconsequences-of-ip-blocking%2F)[](https://bsky.app/intent/compose?text=IP+adreslerini+engellemenin+istenmeyen+sonu%C3%A7lar%C4%B1+https%3A%2F%2Fblog.cloudflare.com%2Ftr-tr%2Fconsequences-of-ip-blocking%2F)[](https://mastodonshare.com/?text=IP+adreslerini+engellemenin+istenmeyen+sonu%C3%A7lar%C4%B1&url=https%3A%2F%2Fblog.cloudflare.com%2Ftr-tr%2Fconsequences-of-ip-blocking%2F)[](https://www.threads.net/intent/post?text=IP+adreslerini+engellemenin+istenmeyen+sonu%C3%A7lar%C4%B1+https%3A%2F%2Fblog.cloudflare.com%2Ftr-tr%2Fconsequences-of-ip-blocking%2F)

## İlgili etiketler

[Better Internet](https://blog.cloudflare.com/tr-tr/tag/better-internet/)[Impact Week](https://blog.cloudflare.com/tr-tr/tag/impact-week/)[Internet Performance](https://blog.cloudflare.com/tr-tr/tag/internet-performance/)[Politika ve Hukuk](https://blog.cloudflare.com/tr-tr/tag/policy/)

Sosyal Medyada Takip Edin

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Yeni yazılardan haberdar olmak için abone olun

E-posta adresi

E-posta adresinizi asla paylaşmayacağız.

Abone Ol

Abone olduğunuz için teşekkürler! Onaylamak için gelen kutunuzu kontrol edin.
