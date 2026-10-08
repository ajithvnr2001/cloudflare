---
url: https://blog.cloudflare.com/id-id/account-takeover-protection/
title: Keamanan Pengguna Akhir: Perlindungan Pengambilalihan Akun dengan Cloudflare | Blog Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:46:27.374746+00:00
---

# Keamanan Pengguna Akhir: Perlindungan Pengambilalihan Akun dengan Cloudflare | Blog Cloudflare

> Source: https://blog.cloudflare.com/id-id/account-takeover-protection/

[Blog](https://blog.cloudflare.com/id-id/)

[Berita Produk](https://blog.cloudflare.com/id-id/tag/product-news/)[Cloudflare Access](https://blog.cloudflare.com/id-id/tag/cloudflare-access/)[Cloudflare Gateway](https://blog.cloudflare.com/id-id/tag/gateway/)+2Tampilkan 2 tag lainnya

5 TagTampilkan 5 tag

  * Tag Post
  * [Berita Produk](https://blog.cloudflare.com/id-id/tag/product-news/)[Cloudflare Access](https://blog.cloudflare.com/id-id/tag/cloudflare-access/)[Cloudflare Gateway](https://blog.cloudflare.com/id-id/tag/gateway/)[Keamanan](https://blog.cloudflare.com/id-id/tag/security/)[Security Week](https://blog.cloudflare.com/id-id/tag/security-week/)
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



[Keamanan](https://blog.cloudflare.com/id-id/tag/security/)[Security Week](https://blog.cloudflare.com/id-id/tag/security-week/)

[Berita Produk](https://blog.cloudflare.com/id-id/tag/product-news/)[Cloudflare Access](https://blog.cloudflare.com/id-id/tag/cloudflare-access/)[Cloudflare Gateway](https://blog.cloudflare.com/id-id/tag/gateway/)[Keamanan](https://blog.cloudflare.com/id-id/tag/security/)[Security Week](https://blog.cloudflare.com/id-id/tag/security-week/)

30 Maret 2021

# Keamanan Pengguna Akhir: Perlindungan Pengambilalihan Akun dengan Cloudflare

![Michael Tremante](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47VPCZP5RNHE8YF2FDVBTK.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Michael Tremante](https://blog.cloudflare.com/id-id/author/michael-tremante/)

9 menit dibaca

SALIN URL

Artikel ini juga tersedia dalam [English](https://blog.cloudflare.com/account-takeover-protection/), [日本語](https://blog.cloudflare.com/ja-jp/account-takeover-protection/), [繁體中文](https://blog.cloudflare.com/zh-tw/account-takeover-protection/), [简体中文](https://blog.cloudflare.com/zh-cn/account-takeover-protection/), dan [ภาษาไทย](https://blog.cloudflare.com/th-th/account-takeover-protection/).

![End User Security: Account Takeover Protections with Cloudflare](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49A679KQA3930WJX5B76K6.png&w=1585&h=755&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////+/v87e7v5eTn6eHn8OXs7+ns5+no/////v3+7+/t6OPh7OHi8+bq8+vt6uzq////////9PHs7OPc8eLe+Onp9+/v7/Du////////+fXu8ebc9ubf/u/s/fX09fb0//////////v09+zi/O3m//fz//37+/35///////////7/fPs//Xw///9///////+//////////////n0//z5//////////////////////////v3//78////////////)

Keamanan akun pengguna akhir selalu menjadi prioritas utama, tetapi hal tersebut adalah masalah yang sulit dipecahkan. Lebih buruk lagi, mengautentikasi pengguna itu adalah hal yang sulit. Dengan pelanggaran terhadap kumpulan data kredensial [menjadi hal yang lumrah](https://haveibeenpwned.com/PwnedWebsites), dan bot yang lebih canggih merayapi web yang mencoba serangan penjelajahan kredensial, melindungi dan memantau titik akhir autentikasi menjadi tantangan bagi tim yang berfokus pada keamanan. Selain itu, banyak titik akhir autentikasi yang masih mengandalkan penyediaan nama pengguna dan kata sandi yang benar, membuat penjelajahan kredensial yang tidak terdeteksi menyebabkan pengambilalihan akun oleh aktor jahat.

Berbagai fitur platform Cloudflare dapat membantu menerapkan perlindungan pengambilalihan akun. Dalam postingan ini kami akan membahas beberapa contoh serta mengumumkan sejumlah fitur baru. Termasuk dalam fitur ini adalah:

  * [Daftar terkelola Proxy Terbuka](https://blog.cloudflare.com/protecting-apis-from-abuse-and-data-exfiltration/) (BARU): memastikan upaya autentikasi ke aplikasi Anda tidak berasal dari layanan proxy;
  * [Super Bot Fight Mode](https://blog.cloudflare.com/super-bot-fight-mode/) (BARU): menjauhkan lalu lintas otomatis dari titik akhir autentikasi Anda;
  * Pemeriksaan Kredensial yang Terekspos (BARU): dapatkan peringatan setiap kali pengguna login dengan kredensial yang disusupi. Fitur ini dapat digunakan untuk memulai aliran autentikasi dua faktor atau reset kata sandi;
  * Cloudflare Access: menambah layer autentikasi tambahan dengan mengintegrasikan secara mudah dengan layanan OATH pihak ketiga, segera; [dengan penerapan opsional perangkat terkelola](https://blog.cloudflare.com/zero-trust-with-managed-devices/) (BARU);
  * Pembatasan Tingkat pada login yang gagal: menghentikan upaya penjelajahan kredensial paksa terhadap aplikasi Anda;



Apabila digunakan bersama, fitur-fitur ini dapat menjadi alat yang kuat dan mudah digunakan untuk meningkatkan keamanan akun pengguna akhir.

### **Daftar Proxy Terbuka Cloudflare**

Pada Juli 2020, kami memperkenalkan [daftar IP](https://blog.cloudflare.com/introducing-ip-lists/) \- daftar IP yang dapat digunakan kembali yang dapat dibuat dan dipelihara pengguna sebagai primitif saat menulis Aturan Firewall kustom. Meskipun ini adalah alat yang hebat untuk administrator Firewall, seperti daftar IP yang digunakan untuk kontrol akses daftar IP ini dengan cepat menjadi usang.

Dengan[daftar Terkelola Proxy Terbuka Cloudflare baru kami](https://blog.cloudflare.com/protecting-apis-from-abuse-and-data-exfiltration/) \- Anda sekarang dapat menulis aturan firewall kustom dan mencocokkannya dengan daftar yang sepenuhnya dikelola dan diperbarui secara berkala (setiap jam) oleh Cloudflare. Daftar tersebut diisi berdasarkan lalu lintas jaringan yang diamati dan pencarian proaktif atas titik akhir proxy yang terbuka.

The new Open Proxies managed list - can be found under Account Home → Configurations → Lists or used directly in a custom rule

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare Open Proxies managed list can be used directly in the Firewall rule builder.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45RXVK8Y3HNQY66EK6YQ2B.png&w=715&h=404&f=webp&fit=cover&position=center)

Daftar terkelola Proxy Terbuka baru - dapat ditemukan di Account Home → Configurations → Lists atau digunakan langsung dalam aturan kustom

Dengan menggabungkan daftar IP dengan filter tambahan saat menulis Aturan Firewall khusus, Anda dapat mengurangi risiko upaya login berbahaya ke titik akhir autentikasi Anda. Dalam menulis aturan yang memanfaatkan daftar baru dengan menggunakan sintaks wirefilter akan terlihat seperti ini:
    
    
    http.request.uri.path contains "/login" and (not ip.src in $cf.open_proxies and cf.bot_management.score < 30)

Setiap upaya autentikasi kemudian akan DIBLOKIR atau DIPERTENTANGKAN sesuai dengan tindakan yang dipilih pada aturan.

Daftar SOCK dan IP Proxy tersedia untuk semua pelanggan Perusahaan.

### **Super Bot Fight Mode dan Deteksi Penyalahgunaan API**

Titik akhir login memberikan peluang bagi bot. Dan bot jahat memanfaatkan waktu dengan sangat baik dengan menguji ribuan, bahkan jutaan, kredensial hanya dalam beberapa detik. Bot ini akan bertahan sampai mereka mengekstrak suatu nilai dari situs Anda.

Untungnya, kami baru saja merilis [Super Bot Fight Mode](https://blog.cloudflare.com/super-bot-fight-mode/) . Fitur ini disertakan dalam semua paket Pro dan Bisnis, dan kami telah memasangkannya dengan analitik waktu riil sehingga Anda dapat melihat serangan saat terjadi. Super Bot Fight Mode dibuat untuk menghentikan penjejalan kredensial. Di latar belakang, kami menjalankan banyak mesin pendeteksi yang sama yang mendukung [produk Manajemen Bot Perusahaan](https://www.cloudflare.com/products/bot-management) kami.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Our new Super Bot Fight Mode. Can be found under Firewall → Bots](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW496PDXSBT7A2TM3KQFA5ZV.png&w=715&h=503&f=webp&fit=cover&position=center)

Our new Super Bot Fight Mode. Can be found under Firewall → Bots

Super Bot Fight Mode baru kami. Dapat ditemukan pada Firewall → Bot

Bagian terbaiknya: Anda dapat segera menambahkan perlindungan. Pengguna pro dapat memilih untuk mengizinkan, memblokir, atau menantang "bot tertentu" di Internet. Pengguna bisnis bahkan dapat menargetkan "kemungkinan bot", yang cenderung lebih canggih dan sulit dikenali. Pengguna Gratis kami dapat terus menggunakan tombol Bot Fight Mode untuk perlindungan dasar.

### **Pemeriksaan Kredensial yang Terekspos**

Penyerang penjejalan kredensial mencoba login ke akun target dengan pasangan nama pengguna/sandi - kredensial pengguna - yang sebelumnya dicuri dalam pelanggaran suatu layanan lain. Sayangnya, ini sering kali berhasil karena [lebih dari 50% pengguna menggunakan kembali kata sandi yang sama untuk beberapa akun](https://www.ndss-symposium.org/ndss2014/programme/tangled-web-password-reuse/) \- dan hasilnya adalah akan ada sejumlah besar akun yang dilanggar. Oleh karena itu, keamanan akun pengguna akhir Anda sendiri tidak hanya bergantung pada keamanan sistem Anda sendiri, tetapi juga pada keamanan semua sistem lain yang digunakan oleh pengguna Anda. Dan meski autentikasi multifaktor dapat memberikan pertahanan yang mendalam, banyak layanan autentikasi dan pengguna belum menggunakannya dan, meskipun demikian, kami ingin dapat memperingatkan layanan dan penggunanya apabila pasangan nama pengguna/sandi mereka rentan.

Selain pendekatan lain seperti deteksi bot, praktik terbaik baru di industri adalah layanan login untuk memeriksa sendiri apakah salah satu kredensial pengguna mereka dalam pelanggaran data yang diketahui. Hal ini membutuhkan serangkaian pasangan nama pengguna/kata sandi yang diketahui dilanggar. Layanan seperti [Have I Been Pwned](https://haveibeenpwned.com/) dan [Google’s Password Breach Alerting](https://security.googleblog.com/2020/10/new-password-protections-and-more-in.html) mengumpulkan database yang besar dari pasangan nama pengguna/sandi yang diketahui dilanggar, dan memungkinkan perusahaan atau pengguna akhir melakukan pencarian untuk menentukan kerentanan. Tetapi integrasi dapat menjadi tantangan, dan idealnya organisasi dapat mengaktifkan perlindungan pemeriksaan kredensial dengan menekan satu tombol.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Exposed Credential Checks can be easily enabled with our Managed Ruleset. Alternatively, you can write your own custom rules.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47XGTH6WPD8QAV1WTMF7NH.png&w=715&h=459&f=webp&fit=cover&position=center)

Kami melakukannya. Hari ini, kami meluncurkan fitur baru dari [Firewall Aplikasi Web (WAF)](https://www.cloudflare.com/waf/): Pemeriksaan Kredensial yang Terekspos.

Exposed Credential Checks can be easily enabled with our Managed Ruleset. Alternatively, you can write your own custom rules.‌‌

Pemeriksaan Kredensial yang Terekspos dapat dengan mudah diaktifkan dengan Ruleset Terkelola kami. Atau, Anda dapat menulis aturan kustom Anda sendiri.‌‌

Permintaan login untuk setiap aplikasi yang dilindungi oleh Cloudflare dirutekan melalui WAF, dan perutean ini memberikan kesempatan untuk pemeriksaan kredensial yang terekspos "di jalur". Apabila diaktifkan, pada setiap upaya autentikasi, WAF akan secara otomatis memeriksa kredensial pengguna akhir berdasarkan database kredensial bocor yang dikumpulkan dan dikelola oleh Cloudflare. Jika kecocokan ditemukan, WAF akan menambahkan header ke asal, sehingga aplikasi Anda dapat diperingatkan tentang kredensial yang rentan dan, misalnya, memicu aliran penyetelan ulang sandi untuk pengguna tersebut atau tantangan autentikasi faktor kedua.

Dalam menangani nama pengguna dan kata sandi, paling tidak, yang sangat sensitif sehingga kami telah merancang fitur pemeriksaan kredensial yang terekspos untuk melindungi kredensial pengguna. Prinsip desain utama adalah bahwa pasangan nama pengguna/sandi tidak boleh diekspos di luar batas proses WAF, sehingga memastikan kami dapat melakukan pemeriksaan tanpa menambahkan risiko tambahan apa pun. Hal ini berarti fitur tersebut tidak pernah mengirimkan nama pengguna atau kata sandi di luar proses WAF atau menyimpan log-nya1 karena kami tidak tertarik untuk mengetahui apa isi kredensial ini -- hanya jika kredensial tersebut menimbulkan risiko bagi keamanan jaringan Anda. Tetapi bahkan lebih dari itu, kami telah membangun protokol kriptografi yang menjaga privasi untuk melakukan pencarian database. Secara kasar, kami menerapkan fungsi hash kriptografi yang dikunci ke pasangan nama pengguna/sandi dalam proses WAF dan memeriksa apakah nilai hash yang dihasilkan cocok dengan pasangan hash yang dikunci dari database kami tentang kredensial yang diketahui telah dilanggar. Kami akan menjelaskan topik ini lebih lanjut dalam pendalaman teknis lanjutan.

Mulai hari ini, pelanggan Perusahaan dapat meminta akses ke fitur ini dengan menghubungi tim kami di [halaman ini](https://www.cloudflare.com/waf/exposed-credential-checks/). Pemeriksaan kredensial yang terekspos disediakan baik sebagai ruleset terkelola, yang akan berfungsi "di luar standar" untuk sistem umum seperti WordPress, Joomla, dan lainnya, dan sebagai filter untuk aturan kustom sehingga semua aplikasi dapat didukung.

### **Cloudflare Access dengan Perangkat Terkelola**

Dengan [Cloudflare Access](https://www.cloudflare.com/teams/access/) Anda dapat memberikan layer autentikasi tambahan di depan aplikasi yang dilindungi oleh Cloudflare. Access melindungi aplikasi dengan memverifikasi identitas pengguna, lokasi, dan jaringan pada setiap permintaan. Fitur ini secara alami meningkatkan keamanan pada akun pengguna akhir.

Namun, perangkat yang digunakan pengguna mungkin masih belum aman. Sesi autentikasi yang valid dengan perangkat yang disusupi dapat menyebabkan pemusnahan data, atau lebih buruk lagi, penyusupan total pada akun atau aplikasi pengguna akhir. Perusahaan mencoba mengurangi risiko ini dengan mengelola dan menerbitkan perangkat perusahaan di mana kebijakan keamanan dapat diterapkan melalui solusi manajemen perangkat seluler (MDM).

Untuk mengatasi masalah ini, kami meningkatkan Cloudflare Access untuk memastikan bahwa hanya perangkat perusahaan yang dapat mengakses aplikasi sensitif. Melalui aturan access, sekarang dimungkinkan untuk memverifikasi nomor seri perangkat terhadap daftar perangkat yang dikelola sebelum mengizinkan akses. Meski kredensial pengguna diekspos, akses tidak sah akan diblokir karena perangkat memiliki nomor seri di luar daftar perangkat yang dikelola. Untuk informasi lebih lanjut, lihat [pengumuman terbaru kami](https://blog.cloudflare.com/zero-trust-with-managed-devices/).

### **Pembatasan Tingkat pada Login yang Gagal**

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![The rule above rate limits any IP after 5 consecutive failed login attempts in a minute for 1 hour.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW485EBYQBFAT9EDAC985HAF.png&w=715&h=822&f=webp&fit=cover&position=center)

Serangan masuk paksa sangat efektif, terutama ketika dilakukan dengan mengulangi database kredensial yang bocor. Untuk menghentikan serangan ini, biasanya cukup dengan memperlambatnya sampai pada titik yang terlalu mahal untuk dieksekusi.

Pada upaya login yang gagal, banyak formulir nama pengguna/sandi akan mengeluarkan kode status HTTP 403 Forbidden atau pesan kesalahan lain yang dapat dikenali2. Kode status ini dapat digunakan sebagai sinyal yang sangat efektif untuk mengeluarkan respons batas tingkat, sehingga menghindari potensi efek samping bagi pengguna yang sah.

The rule above rate limits any IP after 5 consecutive failed login attempts in a minute for 1 hour.

Aturan di atas membatasi tingkat IP setelah 5 kali upaya login yang gagal berturut-turut dalam satu menit selama 1 jam.

Respons pembatas tingkat dapat disesuaikan seperlunya untuk mendukung API dengan payload JSON atau titik akhir berbasis HTML standar.

Pembatasan tingkat tersedia untuk semua pelanggan layanan mandiri sebagai add on berbayar.

### **Rencana masa depan**

Kami menghabiskan banyak waktu untuk memikirkan cara terbaik dalam mengamankan akun pengguna akhir dengan solusi satu klik yang mudah.

Dengan memanfaatkan visibilitas jaringan kami, kami mulai mendapatkan wawasan berharga yang hanya didapatkan dengan skala Cloudflare. Daftar proxy terbuka terkelola kami adalah salah satu contohnya, tetapi kami telah bereksperimen dengan deteksi berbasis anomali yang jauh melampaui postur perangkat sederhana atau batas tingkat. Selain itu, kami sedang memikirkan kasus penggunaan dan skenario tentang cara membagikan anomali terverifikasi secara lebih luas di seluruh basis pelanggan kami, membawa kami kembali ke pendekatan berbasis perlindungan komunitas asli yang dibangun di atas Cloudflare.

.....

1Fitur Cloudflare lainnya, seperti Pencatatan Log Payload WAF Terenkripsi, dapat mencatat log komponen permintaan, tetapi akan dienkripsi dengan kunci publik yang disediakan pelanggan

2Banyak laporan pengujian penetrasi akan menyoroti semua perbedaan dalam menanggapi upaya login yang gagal sebagai kerentanan pengungkapan informasi.

Di halaman ini

Diskusikan Online

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Faccount-takeover-protection%2F&t=Keamanan%20Pengguna%20Akhir%3A%20Perlindungan%20Pengambilalihan%20Akun%20dengan%20Cloudflare)[](https://x.com/intent/post?text=Keamanan+Pengguna+Akhir%3A+Perlindungan+Pengambilalihan+Akun+dengan+Cloudflare&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Faccount-takeover-protection%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Faccount-takeover-protection%2F)[](https://bsky.app/intent/compose?text=Keamanan+Pengguna+Akhir%3A+Perlindungan+Pengambilalihan+Akun+dengan+Cloudflare+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Faccount-takeover-protection%2F)[](https://mastodonshare.com/?text=Keamanan+Pengguna+Akhir%3A+Perlindungan+Pengambilalihan+Akun+dengan+Cloudflare&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Faccount-takeover-protection%2F)[](https://www.threads.net/intent/post?text=Keamanan+Pengguna+Akhir%3A+Perlindungan+Pengambilalihan+Akun+dengan+Cloudflare+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Faccount-takeover-protection%2F)

## Tag terkait

[Berita Produk](https://blog.cloudflare.com/id-id/tag/product-news/)[Cloudflare Access](https://blog.cloudflare.com/id-id/tag/cloudflare-access/)[Cloudflare Gateway](https://blog.cloudflare.com/id-id/tag/gateway/)[Keamanan](https://blog.cloudflare.com/id-id/tag/security/)[Security Week](https://blog.cloudflare.com/id-id/tag/security-week/)

Ikuti di Media Sosial

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Berlangganan untuk menerima pemberitahuan postingan baru

Alamat email

Kami tidak akan pernah membagikan alamat email Anda.

Berlangganan

Terima kasih telah berlangganan! Periksa kotak masuk Anda untuk mengonfirmasi.
