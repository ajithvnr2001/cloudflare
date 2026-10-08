---
url: https://blog.cloudflare.com/id-id/route-leak-detection/
title: Melindungi Pelanggan Cloudflare dari Ketidakamanan BGP dengan Deteksi Kebocoran Rute | Blog Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:51:05.613497+00:00
---

# Melindungi Pelanggan Cloudflare dari Ketidakamanan BGP dengan Deteksi Kebocoran Rute | Blog Cloudflare

> Source: https://blog.cloudflare.com/id-id/route-leak-detection/

[Blog](https://blog.cloudflare.com/id-id/)

[BGP](https://blog.cloudflare.com/id-id/tag/bgp/)[Keamanan](https://blog.cloudflare.com/id-id/tag/security/)[RPKI](https://blog.cloudflare.com/id-id/tag/rpki/)+1Tampilkan 1 tag lainnya

4 TagTampilkan 4 tag

  * Tag Post
  * [Keamanan](https://blog.cloudflare.com/id-id/tag/security/)[Security Week](https://blog.cloudflare.com/id-id/tag/security-week/)
  * Semua tag
  * Tag yang cocok
  * Tidak ada tag yang ditemukan
  * [AI](https://blog.cloudflare.com/id-id/tag/ai/)
  * [Serangan](https://blog.cloudflare.com/id-id/tag/attacks/)
  * [Pekan Ulang Tahun](https://blog.cloudflare.com/id-id/tag/birthday-week/)
  * [Bot Management](https://blog.cloudflare.com/id-id/tag/bot-management/)
  * [Tanpa klien](https://blog.cloudflare.com/id-id/tag/clientless/)
  * [Cloudflare Access](https://blog.cloudflare.com/id-id/tag/cloudflare-access/)
  * [Cloudflare Gateway](https://blog.cloudflare.com/id-id/tag/gateway/)
  * [Cloudflare Tunnel](https://blog.cloudflare.com/id-id/tag/cloudflare-tunnel/)
  * [Cloud Konektivitas](https://blog.cloudflare.com/id-id/tag/connectivity-cloud/)
  * [Kriptografi](https://blog.cloudflare.com/id-id/tag/cryptography/)
  * [DDoS](https://blog.cloudflare.com/id-id/tag/ddos/)
  * [Peringatan DDoS](https://blog.cloudflare.com/id-id/tag/ddos-alerts/)
  * [Laporan DDoS](https://blog.cloudflare.com/id-id/tag/ddos-reports/)
  * [Developer](https://blog.cloudflare.com/id-id/tag/developers/)
  * [DNS (ID)](https://blog.cloudflare.com/id-id/tag/dns/)
  * [dosd (ID)](https://blog.cloudflare.com/id-id/tag/dosd/)
  * [Dampak](https://blog.cloudflare.com/id-id/tag/impact/)
  * [Lalu Lintas Internet](https://blog.cloudflare.com/id-id/tag/internet-traffic/)
  * [Kehidupan di Cloudflare](https://blog.cloudflare.com/id-id/tag/life-at-cloudflare/)
  * [Mirai](https://blog.cloudflare.com/id-id/tag/mirai/)
  * [Mitra](https://blog.cloudflare.com/id-id/tag/partners/)
  * [Kebijakan & Hukum](https://blog.cloudflare.com/id-id/tag/policy/)
  * [Pascakuantum](https://blog.cloudflare.com/id-id/tag/post-quantum/)
  * [Berita Produk](https://blog.cloudflare.com/id-id/tag/product-news/)
  * [Project Galileo](https://blog.cloudflare.com/id-id/tag/project-galileo/)
  * [Radar](https://blog.cloudflare.com/id-id/tag/cloudflare-radar/)
  * [Keamanan](https://blog.cloudflare.com/id-id/tag/security/)
  * [Security Week](https://blog.cloudflare.com/id-id/tag/security-week/)
  * [Kecepatan & Keandalan](https://blog.cloudflare.com/id-id/tag/speed-and-reliability/)
  * [Tren](https://blog.cloudflare.com/id-id/tag/trends/)
  * [Zero Trust](https://blog.cloudflare.com/id-id/tag/zero-trust/)



[Security Week](https://blog.cloudflare.com/id-id/tag/security-week/)

[BGP](https://blog.cloudflare.com/id-id/tag/bgp/)[Keamanan](https://blog.cloudflare.com/id-id/tag/security/)[RPKI](https://blog.cloudflare.com/id-id/tag/rpki/)[Security Week](https://blog.cloudflare.com/id-id/tag/security-week/)

25 Maret 2021

# Melindungi Pelanggan Cloudflare dari Ketidakamanan BGP dengan Deteksi Kebocoran Rute

![David Tuber](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47E8A7R1CB3C4YH862R2QY.png&w=64&h=64&f=webp&fit=cover&position=center)

[David Tuber](https://blog.cloudflare.com/id-id/author/tubes/)

8 menit dibaca

SALIN URL

Artikel ini juga tersedia dalam [English](https://blog.cloudflare.com/route-leak-detection/), [日本語](https://blog.cloudflare.com/ja-jp/route-leak-detection/), dan [ภาษาไทย](https://blog.cloudflare.com/th-th/route-leak-detection/).

![Protecting Cloudflare Customers from BGP Insecurity with Route Leak Detection](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45A6QSW66D06DRH2K9XW0W.png&w=1852&h=926&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////+vr87u7v5+bn6+nq8O/w7+/w6Ojq/////f3+8fDw6+jn7uvp8/Hv8vHx6+vt////////9vXz8Ozo8u7q9/Tx9vX08PDx/////////Pv59vLt+PPu/fn1/Pr59vb3/////////////fn2//v3///9////+/v9////////////////////////////////////////////////////////////////////////////////////////////////)

Kebocoran dan pembajakan rute Protokol Batas Gerbang atau Border Gateway Protocol (BGP) dapat merusak hari Anda — BGP [secara perancangan memang tidak aman](https://blog.cloudflare.com/is-bgp-safe-yet-rpki-routing-security-initiative/), dan informasi perutean yang salah dan tersebar di Internet dapat sangat mengganggu dan berbahaya bagi fungsi normal jaringan pelanggan, dan Internet pada umumnya. Saat ini, kami dengan senang hati mengumumkan Deteksi Kebocoran Rute, fitur peringatan jaringan baru yang memberi tahu pelanggan saat prefiks yang dimilikinya dan terpasang ke Cloudflare mengalami kebocoran, yaitu diiklankan oleh pihak yang tidak berwenang. Deteksi Kebocoran Rute membantu melindungi rute Anda di Internet: fitur ini memberi tahu Anda saat lalu lintas Anda menuju ke tempat yang tidak seharusnya, yang merupakan indikator kemungkinan serangan, dan mengurangi waktu untuk memitigasi kebocoran dengan informasi tepat waktu untuk melengkapi Anda.

Pada blog ini, kami akan menjelaskan apa yang dimaksud kebocoran rute, cara kerja Deteksi Kebocoran Rute Cloudflare, dan apa yang kami lakukan untuk membantu melindungi Internet dari kebocoran rute.

## Apa itu kebocoran rute dan mengapa kita harus peduli?

Kebocoran rute terjadi ketika suatu jaringan di Internet memberi tahu seluruh jaringan Internet untuk merutekan lalu lintas melalui jaringan mereka, meskipun secara normal lalu lintas itu tidak seharusnya menuju ke sana. [Contoh yang sangat baik](https://blog.cloudflare.com/how-verizon-and-a-bgp-optimizer-knocked-large-parts-of-the-internet-offline-today/) dari itu berikut dampak yang dapat ditimbulkannya adalah sebuah insiden di bulan Juni 2019, yaitu satu ISP kecil di Pennsylvania mulai mengiklankan rute untuk sebagian Internet termasuk Cloudflare, Amazon, dan Linode. Bagian cukup besar dari lalu lintas yang ditujukan untuk berbagai jaringan itu salah dirutekan ke jaringan ISP itu, membocorkan prefiks dari Cloudflare, Amazon, dan Linode, serta menyebabkan kemacetan dan kesalahan jaringan tak dapat dicapai bagi pengguna akhir. Kebocoran rute cenderung terjadi karena sesi peering atau router pelanggan yang mengalami kesalahan konfigurasi, bug perangkat lunak di router pelanggan atau pihak ketiga, serangan man-in-the-middle, ataupun pelanggan atau pihak ketiga yang berbahaya.

Beberapa kebocoran rute tidak berbahaya. Tetapi beberapa kebocoran rute lain dapat berbahaya dan memiliki dampak keamanan yang sangat nyata. Penyerang dapat mengiklankan rute tertentu demi tujuan cepat untuk mengarahkan pengguna ke jaringannya dan melakukan hal-hal seperti [mencuri mata uang kripto](https://blog.cloudflare.com/bgp-leaks-and-crypto-currencies/) dan data penting lainnya, atau mencoba menerbitkan sertifikat SSL/TLS yang dapat digunakan untuk menirukan berbagai domain. Dengan mengiklankan rute yang lebih spesifik, penyerang dapat menipu Anda untuk mengakses situs yang tidak Anda tuju, dan jika situs tersebut terlihat tepat sama dengan situs yang Anda harapkan, tanpa sadar Anda dapat memasukkan data pribadi sehingga berisiko terkena serangan. Berikut diagram yang menunjukkan lalu lintas tanpa kebocoran rute:

Dan berikut lalu lintas setelah kebocoran rute:

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Here’s a diagram representing traffic without a route leak](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46ZC0B3XDZ5D7FTXPB4NHQ.png&w=715&h=374&f=webp&fit=cover&position=center)

Jadi, selain membuat pengguna kesal karena banyak lalu lintas Internet yang melalui jalur yang tidak dapat menanganinya, kebocoran rute dapat mengakibatkan kebocoran data yang sangat nyata.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![And here’s traffic after a route leak](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44EW74YA2BQ6YG3RX68QGN.png&w=715&h=374&f=webp&fit=cover&position=center)

Deteksi Kebocoran Rute dari Cloudflare memungkinkan Anda menerima notifikasi dengan cepat saat rute Anda bocor sehingga Anda tahu saat potensi serangan sedang terjadi.

## Bagaimana Deteksi Kebocoran Rute dari Cloudflare melindungi jaringan saya?

### Cara membuat konfigurasi Deteksi Kebocoran Rute

Untuk membuat konfigurasi Deteksi Kebocoran Rute, Anda harus menjadi pelanggan Cloudflare yang telah ["membawa alamat IP Anda sendiri" (BYOIP)](https://developers.cloudflare.com/byoip/)—termasuk pelanggan Magic Transit (L3), Spectrum (L4), dan WAF (L7). Hanya prefiks yang diiklankan oleh Cloudflare yang memenuhi syarat untuk Deteksi Kebocoran Rute.

Membuat konfigurasi Deteksi Kebocoran Rute dapat dilakukan dengan menyiapkan pesan di tab Notifikasi di akun Anda.

Cloudflare kemudian akan mulai memantau semua prefiks terpasang Anda untuk memeriksa kebocoran dan pembajakan. Cloudflare akan mengirimi Anda peringatan saat hal-hal itu terjadi melalui [email atau alat panggilan khusus seperti PagerDuty](https://support.cloudflare.com/hc/en-us/articles/360047358211-Connecting-PagerDuty-to-Cloudflare).

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Configuring Route Leak Detection can be done by setting up a message in the Notifications tab in your account.](https://blog.cloudflare.com/_emdash/api/media/file/01KW499YT8E6BES1Y1GT8MVJDM.gif)

Sistem notifikasi peringatan Cloudflare mendukung webhook, email, dan PagerDuty, sehingga tim Anda selalu mendapat informasi terbaru di seluruh media yang diinginkan tim Anda dengan perubahan rute jaringan dan agar tim dapat merespons dan mengambil tindakan korektif bila diperlukan.

### Contoh skenario serangan

Pihak berbahaya mencoba menggunakan rute untuk memperoleh akses ke data pelanggan dan mulai mengiklankan subnet dari prefiks terpasang untuk salah satu pelanggan Magic Transit kami. Serangan itu, jika tidak ditemukan dan diperbaiki dengan cepat, dapat berdampak besar pada pelanggan. Saat penyerang mulai mengiklankan prefiks tanpa sepengetahuan pelanggan, pembaruan BGP dan perubahan rute mulai terjadi dengan cepat di tabel perutean global—biasanya dalam waktu 60 detik.

Mari kita melihat bagaimana pelanggan dapat menerapkan Deteksi Kebocoran Rute. Pelanggan Acme Corp. memiliki prefiks IP 203.0.113.0/24. Acme telah memasang 203.0.113.0/24 ke Cloudflare, dan Cloudflare memberi tahu seluruh Internet bahwa prefiks ini dapat dijangkau melalui jaringan Cloudflare.

Begitu Acme mengaktifkan Deteksi Kebocoran Rute, Cloudflare secara terus-menerus memantau informasi perutean di Internet untuk 203.0.113.0/24. Target kami adalah mendeteksi kebocoran dalam waktu lima menit setelah informasi perutean yang salah menyebar di Internet.

Melihat kembali ke skenario serangan. Pihak berbahaya yang mencoba menyerang jaringan Acme membajak iklan untuk 203.0.113.0/24, mengalihkan pengguna yang sah dari jalur jaringan tujuan ke Acme (melalui jaringan Cloudflare) dan malah dialihkan ke sebuah faksimile dari jaringan Acme yang dimaksudkan untuk menangkap informasi dari pengguna tanpa disadari.

Karena Acme telah mengaktifkan Deteksi Kebocoran Rute, sebuah peringatan dikirim ke administrator Acme.

Peringatan tersebut mencakup semua ASN yang melihat prefiks yang diiklankan oleh pihak yang berpotensi berbahaya itu. Acme dapat memperingatkan penggunanya bahwa mereka mungkin berisiko terkena serangan pencurian data dan mereka harus waspada terhadap perilaku yang mencurigakan.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Because Acme has enabled Route Leak Detection, an alert is sent to Acme’s administrators.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46P9FYXK95HSTCP2SZKRZG.png&w=715&h=798&f=webp&fit=cover&position=center)

Acme juga dapat dengan cepat menghubungi penyedia layanan yang tercantum dalam peringatan agar berhenti memperhatikan rute yang bernilai lebih kecil. Saat ini, proses memitigasi kebocoran rute merupakan proses yang sangat manual, yang memerlukan dihubunginya penyedia layanan secara langsung menggunakan informasi kontak yang dipublikasikan di [database publik](https://www.peeringdb.com/). Di masa mendatang, kami berencana membangun fitur yang mengotomatiskan proses pencarian bantuan dan mitigasi ini untuk lebih mengurangi waktu memitigasi peristiwa kebocoran rute yang mungkin berdampak pada pelanggan kami.

## Bagaimana Cloudflare mendeteksi kebocoran rute?

Cloudflare menggunakan beberapa sumber data perutean untuk membuat sintesis dari cara Internet melihat rute ke pelanggan BYOIP kami. Cloudflare kemudian memperhatikan tampilan ini untuk melacak setiap perubahan mendadak yang terjadi di Internet. Jika kami dapat mengorelasikan berbagai perubahan itu dengan tindakan yang telah kami ambil, maka kami tahu bahwa perubahan itu tidak berbahaya dan merupakan hal yang wajar. Akan tetapi, jika kami tidak melakukan perubahan apa pun, kami segera mengambil tindakan untuk memberi tahu Anda bahwa rute dan pengguna Anda mungkin sedang mengalami risiko.

### Saluran penyerapan dari luar ke dalam Cloudflare

Sumber data utama Cloudflare berasal dari repositori yang dipelihara secara eksternal seperti [feed RIS RIPE](https://ris-live.ripe.net/), [RouteViews](http://www.routeviews.org/), dan [feed BMP publik Caida](https://bgpstream.caida.org/data#!caida-bmp). Penting untuk menggunakan beberapa pandangan eksternal dari tabel perutean Internet agar dapat seakurat mungkin saat membuat kesimpulan tentang keadaan Internet. Cloudflare melakukan panggilan API ke berbagai sumber tersebut untuk menyerap data dan menganalisis perubahan pada rute BGP. Berbagai feed ini memungkinkan kami menyerap data perutean untuk seluruh Internet. Cloudflare memfilter semua itu hingga ke prefiks Anda yang sebelumnya telah Anda masukkan ke Cloudflare.

Setelah data ini diserap dan difilter, Cloudflare memulai pembaruan referensi silang ke tabel perutean global dengan metrik yang menunjukkan kemungkinan pembajakan, seperti jumlah ASN yang langsung melihat rute Anda, jumlah pembaruan BGP yang terjadi selama periode waktu singkat , dan jumlah subnet yang diiklankan. Jika jumlah ASN yang langsung melihat rute Anda atau jumlah pembaruan berubah drastis, itu dapat berarti prefiks Anda sedang bocor. Jika satu subnet dari prefiks yang Anda iklankan mengalami jumlah perubahan yang drastis dalam tabel perutean global, ada kemungkinan prefiks Anda sedang bocor di suatu tempat.

Cloudflare sudah membuat konfigurasi ini pada prefiks kami sendiri saat ini. Berikut adalah contoh dari apa yang kami lihat ketika sistem kami memutuskan ada sesuatu yang salah:

Cloudflare memiliki rentang prefiks 2606:4700:50::/44 karena merupakan subnet dari salah satu rentang [yang tercantum di situs kami di sini](https://www.cloudflare.com/ips/). Dalam satu jam, kami melihat seseorang mencoba mengiklankan subnet pada rentang tersebut ke 38 jaringan lain. Untungnya, karena kami telah [menyebarkan RPKI](https://blog.cloudflare.com/rpki-details/), kami tahu bahwa sebagian besar jaringan akan menolak iklan rute dari penyerang ini daripada menerimanya.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare already has this configured on our own prefixes today. Here’s an example of what we see when our system determines that something is wrong:](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW462F218HHM4DVGF38GBY83.png&w=715&h=142&f=webp&fit=cover&position=center)

## Apa yang dapat saya lakukan untuk mencegah kebocoran rute di masa mendatang?

Cara terbaik untuk mencegah kebocoran rute adalah dengan menyebarkan [RPKI](https://blog.cloudflare.com/rpki-details/) di jaringan Anda, dan mendesak penyedia Internet Anda untuk melakukannya juga. RPKI memungkinkan Anda dan penyedia Anda untuk menandatangani rute yang Anda iklankan ke Internet sehingga tak ada seorang pun yang dapat mencurinya. Jika seseorang mengiklankan rute RPKI Anda, penyedia mana pun yang mendukung RPKI tidak akan meneruskan rute itu ke pelanggan lain sehingga memastikan kebocoran yang diupayakan itu ditahan sedekat mungkin dengan si penyerang.

Cloudflare [dengan dukungan terus-menerus](https://isbgpsafeyet.com/) untuk RPKI telah membuahkan hasil dalam tiga bulan terakhir saja. Penyedia seperti Amazon, Google, Telstra, Cogent, dan bahkan Netflix telah mulai mendukung RPKI dan memfilter serta menghapus prefiks yang tidak valid. Bahkan, lebih dari 50% penyedia Internet teratas kini mendukung RPKI dalam beberapa cara:

Deteksi Kebocoran Rute Cloudflare dikombinasikan dengan semakin banyak penyedia yang menerapkan RPKI membantu memastikan kehilangan data dan waktu henti akibat kebocoran rute menjadi bagian dari masa lalu. Jika Anda pelanggan Cloudflare Magic Transit atau BYOIP, coba buat konfigurasi peringatan kebocoran rute di dasbor Anda hari ini. Jika Anda bukan pelanggan Magic Transit atau BYOIP, hubungi [tim penjualan](https://www.cloudflare.com/en-gb/plans/enterprise/contact/) kami untuk memulai proses menjaga jaringan Anda tetap aman — hingga ke rutenya.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![In fact, over 50% of the top Internet providers now support RPKI in some fashion:](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45RAWTD6NJGMZ17CKQJFQA.png&w=715&h=988&f=webp&fit=cover&position=center)

Di halaman ini

Diskusikan Online

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Froute-leak-detection%2F&t=Melindungi%20Pelanggan%20Cloudflare%20dari%20Ketidakamanan%20BGP%20dengan%20Deteksi%20Kebocoran%20Rute)[](https://x.com/intent/post?text=Melindungi+Pelanggan+Cloudflare+dari+Ketidakamanan+BGP+dengan+Deteksi+Kebocoran+Rute&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Froute-leak-detection%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Froute-leak-detection%2F)[](https://bsky.app/intent/compose?text=Melindungi+Pelanggan+Cloudflare+dari+Ketidakamanan+BGP+dengan+Deteksi+Kebocoran+Rute+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Froute-leak-detection%2F)[](https://mastodonshare.com/?text=Melindungi+Pelanggan+Cloudflare+dari+Ketidakamanan+BGP+dengan+Deteksi+Kebocoran+Rute&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Froute-leak-detection%2F)[](https://www.threads.net/intent/post?text=Melindungi+Pelanggan+Cloudflare+dari+Ketidakamanan+BGP+dengan+Deteksi+Kebocoran+Rute+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Froute-leak-detection%2F)

## Tag terkait

[BGP](https://blog.cloudflare.com/id-id/tag/bgp/)[Keamanan](https://blog.cloudflare.com/id-id/tag/security/)[RPKI](https://blog.cloudflare.com/id-id/tag/rpki/)[Security Week](https://blog.cloudflare.com/id-id/tag/security-week/)

Ikuti di Media Sosial

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Berlangganan untuk menerima pemberitahuan postingan baru

Alamat email

Kami tidak akan pernah membagikan alamat email Anda.

Berlangganan

Terima kasih telah berlangganan! Periksa kotak masuk Anda untuk mengonfirmasi.
