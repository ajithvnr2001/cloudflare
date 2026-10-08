---
url: https://blog.cloudflare.com/id-id/heartbleed-revisited/
title: Heartbleed Ditinjau Kembali | Blog Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:51:03.469213+00:00
---

# Heartbleed Ditinjau Kembali | Blog Cloudflare

> Source: https://blog.cloudflare.com/id-id/heartbleed-revisited/

[Blog](https://blog.cloudflare.com/id-id/)

[Security Week](https://blog.cloudflare.com/id-id/tag/security-week/)[TLS](https://blog.cloudflare.com/id-id/tag/tls/)

2 TagTampilkan 2 tag

  * Tag Post
  * [Security Week](https://blog.cloudflare.com/id-id/tag/security-week/)
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



[Security Week](https://blog.cloudflare.com/id-id/tag/security-week/)[TLS](https://blog.cloudflare.com/id-id/tag/tls/)

27 Maret 2021

# Heartbleed Ditinjau Kembali

![Nick Sullivan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44NXK9203HP874YB09STY7.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Nick Sullivan](https://blog.cloudflare.com/id-id/author/nick-sullivan/)

7 menit dibaca

SALIN URL

Artikel ini juga tersedia dalam [English](https://blog.cloudflare.com/heartbleed-revisited/) dan [ภาษาไทย](https://blog.cloudflare.com/th-th/heartbleed-revisited/).

![Heartbleed Revisited](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45RG1TJ1Y7WGGPC78AD8QV.png&w=1513&h=708&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////+/3/7u/w5uXl5+bn7e3u7vDx6+3u/////f//7evs4Nzc4Nvc6OTl7ezt7e7v////////7err3NTV2tHS5N3e7err8PHy////////8e7v3tbX3NHS597f8e3u9vb3////////+ff46OLj597g8enr+fb3/P39////////////9vP09vLz/vr8////////////////////////////////////////////////////////////////////////)

Pada tahun 2014, sebuah bug ditemukan di OpenSSL, perpustakaan enkripsi populer yang digunakan untuk mengamankan sebagian besar server di Internet. Bug ini memungkinkan penyerang menyalahgunakan fitur tidak jelas yang disebut detak jantung TLS untuk membaca memori dari server yang terpengaruh. Heartbleed adalah berita besar karena memungkinkan penyerang mengekstrak rahasia terpenting di server: kunci privat sertifikat TLS/SSL-nya. Setelah mengonfirmasikan bahwa bug tersebut [mudah dieksploitasi,](https://blog.cloudflare.com/the-results-of-the-cloudflare-challenge/), kami mencabut dan menerbitkan kembali lebih dari [100.000 sertifikat](https://blog.cloudflare.com/the-heartbleed-aftermath-all-cloudflare-certificates-revoked-and-reissued/), yang menyoroti beberapa masalah utama tentang cara mengamankan Internet.

Meskipun Heartbleed dan [peristiwa kompromi penting lainnya](https://www.bankinfosecurity.com/private-keys-for-23000-digital-certificates-leaked-a-10689) menyakitkan bagi tim keamanan dan operasi di seluruh dunia, peristiwa itu juga memberikan kesempatan belajar bagi industri. Selama tujuh tahun terakhir, Cloudflare telah mengambil pelajaran dari Heartbleed dan menerapkannya untuk meningkatkan desain sistem dan ketahanan Internet kami secara keseluruhan. Baca terus untuk mengetahui cara menggunakan Cloudflare untuk mengurangi risiko kompromi kunci dan mengurangi biaya pemulihan jika kejadian tersebut terjadi.

### **Menjaga kunci tetap aman**

Prinsip penting dari desain sistem keamanan adalah pertahanan mendalam. Hal-hal penting harus dilindungi dengan beberapa layer pertahanan. Inilah sebabnya mengapa orang yang sadar akan keamanan menyimpan kunci rumah cadangan di kotak kunci yang aman bukan di bawah keset. Untuk sistem kriptografi yang menghadap ke Internet, pertahanan mendalam berarti merancang sistem Anda sehingga kunci tidak dicuri dengan satu eksploitasi saja. Ini tidak berlaku untuk OpenSSL dan Heartbleed. Kunci privat dimuat ke dalam memori ke dalam proses menghadap ke Internet yang tidak aman untuk memori, jadi hanya satu bug pengungkapan memori yang diperlukan untuk mencurinya.

Keyless SSL: menjaga server tetap terpisah dari kunci

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Keyless SSL: keeping the server separate from the key](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW472YA43T5NRSR7C5HFMB0G.png&w=715&h=296&f=webp&fit=cover&position=center)

Strategi pertahanan mendalam yang efektif untuk melindungi kunci pribadi TLS/SSL adalah dengan membagi proses menjadi dua bagian: bagian kunci pribadi/autentikasi, dan bagian enkripsi/deskripsi. Inilah tepatnya mengapa kami mengembangkan Keyless SSL, untuk memungkinkan pelanggan tetap mengontrol kunci privat mereka sekaligus memungkinkan Cloudflare menangani detail koneksi lainnya. [Keyless SSL](https://blog.cloudflare.com/keyless-ssl-the-nitty-gritty-technical-details/) menyediakan pemisahan fisik antara tempat kunci yang sedang digunakan dan tempat penyimpanannya. Kami mendukung Keyless SSL baik untuk modul keamanan perangkat lunak maupun perangkat keras (HSM), dan hari ini kami mengumumkan bahwa kami sekarang mendukung [beberapa HSM berbasis cloud](https://blog.cloudflare.com/keyless-ssl-supports-fips-140-2-l3-hsm).

Geo Key Manager: manajemen kunci yang dapat dikonfigurasi berdasarkan geografi

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Geo Key Manager: configurable key management by geography](https://blog.cloudflare.com/_emdash/api/media/file/01KW46J3EN9BBN0M4BRXK3Y7RN.gif)

Heartbleed menunjukkan kepada kami bahwa strategi ini juga dapat berguna dalam menambahkan layer keamanan ekstra untuk kunci privat yang kami kelola untuk pelanggan kami. Pada tahun 2017, kami meluncurkan [Geo Key Manager](https://blog.cloudflare.com/geo-key-manager-how-it-works/), sebuah fitur yang memungkinkan pelanggan untuk memilih lokasi mana di dunia yang mereka inginkan untuk menyimpan kunci mereka. Geo Key Manager melindungi kunci dari kompromi fisik server di berbagai geografi. Pada tahun 2019, kami melangkah lebih jauh dengan menerapkan strategi yang disebut [Keyless Everywhere](https://blog.cloudflare.com/going-keyless-everywhere/), yang memindahkan semua kunci terkelola ke sistem yang menyediakan pemisahan logis antara Internet dan kunci privat.

Kredensial yang Didelegasikan: pemisahan kunci tanpa latensi

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Delegated Credentials: key separation with no latency](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW490APX1HK0ET9YQWKKRS7V.jpg&w=512&h=292&f=webp&fit=cover&position=center)

Keyless SSL adalah solusi keamanan yang hebat, tetapi tergantung di mana kunci disimpan, Keyless SSL dapat menimbulkan beberapa latensi. Karena itu, kami bekerja dengan IETF untuk mengembangkan standar baru yang disebut [Kredensial yang Didelegasikan](https://blog.cloudflare.com/keyless-delegation/), yang memungkinkan koneksi menggunakan kunci berumur pendek yang ditandatangani oleh sertifikat alih-alih sertifikat itu sendiri di TLS. Ini menghilangkan latensi tambahan yang diakibatkan oleh Keyless SSL. Kami mendukung Kredensial yang Didelegasikan untuk semua pelanggan Keyless SSL dan Geo Key Manager; dan Firefox 89 (Mei 2021) akan mengaktifkan dukungan Delegated Credential secara default.

### **Membuat pencabutan berfungsi**

Ketika Heartbleed terjadi dan ratusan ribu sertifikat dianggap berpotensi disusupi, hal logis yang harus dilakukan adalah mencabut dan menerbitkan kembali sertifikat tersebut. Melakukan hal tersebut dapat menyebabkan beberapa konsekuensi yang tidak terduga.

Konsekuensi pertama dari pencabutan adalah lonjakan lalu lintas jaringan yang besar terkait dengan informasi pencabutan. Pada tahun 2014, ada tiga mekanisme utama pencabutan sertifikat:

  * Daftar Pencabutan Sertifikat (CRL)
    * Daftar nomor seri yang dicabut untuk otoritas sertifikat tertentu
  * Protokol Status Sertifikat Online(OCSP)
    * Protokol untuk menanyakan otoritas sertifikat tentang status pencabutan sertifikat
    * OCSP dapat ditanyakan oleh browser atau respons dapat dimasukkan oleh server pada waktu koneksi "stapel OCSP"
  * CRLSets — Sistem pencabutan kustom Chrome
    * Daftar meta nomor seri yang dicabut, terbatas pada sertifikat yang bernilai tinggi



Puluhan ribu sertifikat dicabut sekaligus karena potensi kompromi dari Heartbleed. Setelah ini, CRL untuk CA terkemuka, GlobalSign, meningkat dari [22KB menjadi 4,7MB dalam sehari](https://blog.cloudflare.com/the-hard-costs-of-heartbleed/). Ini menyebabkan gangguan besar pada infrastruktur caching internal Cloudflare dan lonjakan bandwidth yang memengaruhi Internet secara luas karena semua klien yang mengandalkan CRL memeriksa validasi sertifikat (sebagian besar Microsoft Windows) mengunduh file.

Setelah peristiwa pencabutan ini, menjadi jelas bahwa ada alasan lain mengapa pencabutan bukan merupakan sistem yang fungsional. Di Firefox, jika pengguna membuat koneksi ke situs dan respons OCSP yang distapel tidak disediakan, Firefox akan menanyakan server OCSP untuk mendapatkan respons. Namun, Firefox menerapkan strategi gagal-terbuka: jika respons OCSP terlalu lama, pemeriksaan pencabutan akan dilewati dan halaman dirender. Penyerang dengan posisi jaringan dengan hak istimewa dapat menggunakan sertifikat yang disusupi _dan dicabut_ untuk menyerang pengguna hanya dengan memblokir permintaan OCSP dan membiarkan browser melewati pemeriksaan pencabutan. Staple OCSP adalah cara bagi server untuk mendapatkan respons OCSP ke browser dengan cara yang andal, tetapi karena staple bukan persyaratan untuk klien, penyerang tidak dapat menyertakan staple sehingga browser akan gagal terbuka, yang membuat pengguna rentan untuk diserang. OCSP juga tidak memberikan perlindungan yang kuat terhadap penyusupan kunci dalam mode gagal-terbuka (ditambah, OCSP adalah [kebocoran privasi](https://www.eff.org/deeplinks/2020/11/macos-leaks-application-usage-forces-apple-make-hard-decisions), tapi itu masalah lain).

Situasi di Chrome bahkan lebih buruk dari perspektif keamanan. Karena baik OCSP maupun CRL tidak diperiksa untuk sebagian besar sertifikat (CRLSet hanya berisi sertifikat "Validasi Diperluas" yang dicabut), sebagian besar sertifikat dipercaya tanpa memeriksa status pencabutan. Solusi untuk mencabut kumpulan sertifikat yang dikelola Cloudflare di Chrome untuk Heartbleed sebenarnya adalah patch singkat ke basis kode Chromium. Jelas ini bukanlah solusi yang dapat ditingkatkan!

Pencabutan sertifikat secara massal pada tahun 2014 jelas tidak berhasil. Sebagian sertifikat pada saat itu berlaku hingga lima tahun, jadi kunci yang disusupi menjadi masalah untuk waktu yang lama.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-405 Embedded Image - zbUHgD](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44MPE0YGV21V5F2ZNH0NX0.png&w=715&h=228&f=webp&fit=cover&position=center)

Pada tahun 2015, standar baru muncul yang tampaknya memberikan solusi yang masuk akal untuk masalah ini: [OCSP Must-staple](https://scotthelme.co.uk/ocsp-must-staple/). Sertifikat yang diterbitkan dengan fitur must-staple hanya dapat dipercaya jika disertai dengan staple OCSP yang valid. Jika sertifikat must-staple disusupi dan dicabut, maka sertifikat tersebut hanya dapat digunakan untuk menyerang pengguna selama masa pakai OCSP yang diterbitkan terakhir (biasanya 10 hari atau kurang). Ini adalah peningkatan besar dan memungkinkan pemilik sertifikat untuk membatasi risiko mereka secara keseluruhan.

Cloudflare telah mendukung staple OCSP dengan upaya yang terbaik [sejak 2012](https://blog.cloudflare.com/ocsp-stapling-how-cloudflare-just-made-ssl-30/). Pada tahun 2017, kami mulai meningkatkan keandalan staple OCSP kami sehingga kami dapat mendukung sertifikat OCSP must-staple. Hasil dari pekerjaan ini adalah [staple OCSP dengan keandalan tinggi](https://blog.cloudflare.com/high-reliability-ocsp-stapling/) dan studi penelitian yang diterbitkan [di IMC](https://dl.acm.org/doi/10.1145/3278532.3278543) yang menunjukkan kelayakan OCSP must-staple secara lebih luas di Internet. Cloudflare sekarang mendukung sertifikat OCSP must-staple, yang menyediakan jaring pengaman tambahan jika terjadi kompromi kunci di masa mendatang.

### **2014 vs. sekarang**

Kami telah membuat banyak kemajuan dalam tujuh tahun. Cloudflare terus berinovasi dalam perlindungan kunci dan ruang keamanan TLS/SSL. Inilah yang berubah selama beberapa tahun terakhir:

2014

  * Sertifikat lima tahun
  * Opportunistic OCSP stapling
  * Tidak ada OCSP must-staple
  * Kunci dalam proses yang menghadap ke Internet
  * Tidak ada Keyless SSL
  * Tidak ada Kredensial yang Didelegasikan



2021

  * Sertifikat seumur hidup yang dapat dikonfigurasi (dari satu tahun hingga dua minggu dengan [ACM](https://blog.cloudflare.com/advanced-certificate-manager))
  * 100% dukungan stapel OCSP
  * Dukungan OCSP Must-staple
  * Keyless di mana saja
  * Dukungan Keyless SSL + Cloud HSM! (baru)
  * Geo Key Manager
  * Dukungan Kredensial yang Didelegasikan



Peningkatan ini dan lebih banyak lagi adalah alasan besar mengapa Cloudflare adalah pemimpin dalam ruang keamanan dan mengapa Heartbleed berikutnya akan lebih baik.

Di halaman ini

Diskusikan Online

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fheartbleed-revisited%2F&t=Heartbleed%20Ditinjau%20Kembali)[](https://x.com/intent/post?text=Heartbleed+Ditinjau+Kembali&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fheartbleed-revisited%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fheartbleed-revisited%2F)[](https://bsky.app/intent/compose?text=Heartbleed+Ditinjau+Kembali+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fheartbleed-revisited%2F)[](https://mastodonshare.com/?text=Heartbleed+Ditinjau+Kembali&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fheartbleed-revisited%2F)[](https://www.threads.net/intent/post?text=Heartbleed+Ditinjau+Kembali+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fheartbleed-revisited%2F)

## Tag terkait

[Security Week](https://blog.cloudflare.com/id-id/tag/security-week/)[TLS](https://blog.cloudflare.com/id-id/tag/tls/)

Ikuti di Media Sosial

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)

  * ![Nick Sullivan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44NXK9203HP874YB09STY7.jpg&w=64&h=64&f=webp&fit=cover&position=center)[Nick Sullivan](https://blog.cloudflare.com/id-id/author/nick-sullivan/)

[](https://crypto.dance)




## Berlangganan untuk menerima pemberitahuan postingan baru

Alamat email

Kami tidak akan pernah membagikan alamat email Anda.

Berlangganan

Terima kasih telah berlangganan! Periksa kotak masuk Anda untuk mengonfirmasi.
