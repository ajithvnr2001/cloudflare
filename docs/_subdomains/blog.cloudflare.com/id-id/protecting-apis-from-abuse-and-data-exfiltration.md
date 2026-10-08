---
url: https://blog.cloudflare.com/id-id/protecting-apis-from-abuse-and-data-exfiltration/
title: Melindungi API Anda dari penyalahgunaan dan pencurian data | Blog Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:47:36.837712+00:00
---

# Melindungi API Anda dari penyalahgunaan dan pencurian data | Blog Cloudflare

> Source: https://blog.cloudflare.com/id-id/protecting-apis-from-abuse-and-data-exfiltration/

[Blog](https://blog.cloudflare.com/id-id/)

[API Shield](https://blog.cloudflare.com/id-id/tag/api-shield/)[DLP](https://blog.cloudflare.com/id-id/tag/dlp/)[Firewall](https://blog.cloudflare.com/id-id/tag/firewall/)+1Tampilkan 1 tag lainnya

4 TagTampilkan 4 tag

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



[Security Week](https://blog.cloudflare.com/id-id/tag/security-week/)

[API Shield](https://blog.cloudflare.com/id-id/tag/api-shield/)[DLP](https://blog.cloudflare.com/id-id/tag/dlp/)[Firewall](https://blog.cloudflare.com/id-id/tag/firewall/)[Security Week](https://blog.cloudflare.com/id-id/tag/security-week/)

24 Maret 2021

# Melindungi API Anda dari penyalahgunaan dan pencurian data

![Daniele Molteni](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW464793D50Z8QJQK451PK2A.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Daniele Molteni](https://blog.cloudflare.com/id-id/author/daniele/)

11 menit dibaca

SALIN URL

Artikel ini juga tersedia dalam [English](https://blog.cloudflare.com/protecting-apis-from-abuse-and-data-exfiltration/), [日本語](https://blog.cloudflare.com/ja-jp/protecting-apis-from-abuse-and-data-exfiltration/), [繁體中文](https://blog.cloudflare.com/zh-tw/protecting-apis-from-abuse-and-data-exfiltration/), [简体中文](https://blog.cloudflare.com/zh-cn/protecting-apis-from-abuse-and-data-exfiltration/), dan [ภาษาไทย](https://blog.cloudflare.com/th-th/protecting-apis-from-abuse-and-data-exfiltration/).

![Protecting your APIs from abuse and data exfiltration](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48AEAJPZKXEE30QZSDB5ZR.png&w=1513&h=757&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/////v/98PLw5+np6Ovr7vDx7/Dx6urt///////+8fHv5ubl5ubm7Ozt7u7w6+vt////////8/Lw5uTj5eLi6+nq7+3w7u7w////////+Pb06+fm6eXl7+vt8/Hz8/L0//////////378/Dv8e/v9/T2+vn7+fn7/////////////Pv7+/v7////////////////////////////////////////////////////////////////////////////)

Lalu lintas API berkembang pesat. Tahun lalu saja, lalu lintas API meningkat 300% lebih cepat di tepi jaringan kami daripada lalu lintas web. Karena API memperkuat aplikasi seluler dan web dengan mengirim instruksi beragam seperti "pesan pizza dari restoran favorit saya menggunakan kartu kredit ini" atau "pasang posisi berdagang mata uang kripto dan berikut informasi pribadi saya", maka API menjadi sasaran empuk dari pencurian dan penyalahgunaan data. Eksposur data tercantum sebagai salah satu ancaman utama untuk lalu lintas API oleh OWASP; eksposur data mencakup kebocoran dan pencurian data dari respons yang diberikan oleh sumber [(10 TERATAS Ancaman Keamanan API tahun 2019)](https://owasp.org/www-project-api-security/). Peningkatan lalu lintas API dan makin seringnya serangan data membutuhkan solusi keamanan baru.

Kit alat keamanan dari Cloudflare selalu dirancang untuk melindungi lalu lintas web dan API. Akan tetapi, setelah berbicara dengan ratusan pelanggan, kami menyadari bahwa ada kebutuhan untuk alat keamanan yang mudah disebarkan dan mudah dibuat konfigurasinya untuk lalu lintas API di dalam satu antarmuka tunggal. Untuk memenuhi permintaan ini, pada Oktober 2020 kami meluncurkan [API ShieldTM](https://blog.cloudflare.com/introducing-api-shield/), produk baru yang ditujukan untuk menggabungkan semua solusi keamanan yang dirancang untuk lalu lintas API. Kami memulai dengan menyediakan autentikasi mTLS untuk semua pengguna Cloudflare secara gratis, juga dukungan gRPC, dan Validasi Skema dalam versi Beta. Selama peluncuran, kami menyusun rencana untuk rilis di masa mendatang dengan fungsionalitas keamanan yang lebih canggih. Kini kami sangat senang mampu memperluas penawaran kami dengan fitur-fitur baru yang dirancang untuk melindungi API Anda agar tidak mengekspos data sensitif.

Hari ini kami meluncurkan empat fitur untuk membantu mengurangi dampak serangan pencurian data: Schema Validation atau Validasi Skema untuk semua pelanggan Perusahaan, Daftar IP terkelola yang memungkinkan Anda memblokir lalu lintas dari Proxy Terbuka, kontrol lebih besar terhadap siklus hidup sertifikat, dan solusi Pencegahan Kehilangan Data. Nanti di minggu ini kami juga akan mengumumkan kemampuan untuk membantu Anda menemukan API yang bekerja di jaringan Anda yang mungkin tidak Anda sadari, dan cara mengidentifikasi permintaan tidak wajar yang menyimpang dari tujuan penggunaan API.

### Validasi Skema tersedia secara umum

Selama peluncuran API Shield, kami memperkenalkan Validasi Skema dan merilisnya untuk beberapa pelanggan terpilih. Selama beberapa bulan terakhir, kami telah bekerja sama dengan para pengguna awal kami untuk menambahkan lebih banyak kemampuan dan membangun antarmuka yang mudah digunakan ke dalam dasbor kami secara langsung. Anda kini dapat membuka tab 'API Shield' untuk menyebarkan produk keamanan API secara langsung dari UI. Aliran penyebaran akan segera diperluas untuk menyertakan kemampuan tambahan yang terdapat di tempat lain di dasbor, seperti mTLS dan Pembatasan Tingkat. Kami juga akan mengintegrasikan fitur baru seperti deteksi anomali API untuk loop umpan balik yang mudah.

Validasi Skema bekerja dengan membuat model keamanan positif berdasarkan "skema" API, yang merupakan kontrak yang menentukan penggunaan API dan memandu para pengembang untuk mengintegrasikannya ke dalam sistem mereka. Sebaliknya, untuk model keamanan negatif (di mana aturan menentukan karakteristik apa yang harus dimiliki permintaan untuk memicu suatu tindakan, seperti pemblokiran), Validasi Skema dirancang untuk mengizinkan permintaan yang telah diverifikasi kesesuaiannya sambil mengambil tindakan pada semua permintaan lainnya. Validasi Skema menerima skema yang mematuhi Spesifikasi OpenAPI v3 (juga dikenal sebagai Spesifikasi Swagger), yang merupakan standar untuk mendefinisikan antarmuka RESTful ([pelajari lebih lanjut di halaman ini](https://swagger.io/solutions/getting-started-with-oas/)).

Validasi Skema mengevaluasi setiap permintaan terhadap catatan log Skema API atau permintaan pemblokiran yang tidak sesuai dengan itu.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Schema Validation evaluates each request against an API Schema logging or blocking requests that do not comply with it.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4999JT849QWCP3JPY8VFSX.png&w=715&h=625&f=webp&fit=cover&position=center)

API Shield menawarkan UI yang mudah digunakan yang dapat menjadi tempat bagi para pengguna untuk meng-upload skema mereka ke Firewall dan secara otomatis membuat aturan yang memvalidasi setiap permintaan terhadap definisi API. Jika permintaan itu sesuai maka akan diteruskan ke sumber. Sebaliknya, jika format atau konten data permintaan tidak sesuai dengan yang diharapkan oleh API Shield, maka panggilan itu akan dibuat log atau dihapus untuk melindungi sumber dari permintaan yang tidak valid atau muatan berbahaya. Permintaan dengan masukan yang tidak berhubungan mungkin tidak diantisipasi oleh pengembang API, dan dapat memicu perilaku aplikasi yang tidak terduga, seperti kebocoran data.

API Shield dengan Validasi Skema sedang disebarkan menggunakan skema OpenAPI Cloudflare Rulesets.‌‌

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![API Shield with Schema Validation being deployed using the Cloudflare Rulesets OpenAPI schema.](https://blog.cloudflare.com/_emdash/api/media/file/01KW47MPZN1X4W79VKPX4D3HFR.gif)

UI memandu pengguna melalui langkah yang berbeda, termasuk mendefinisikan nama hos dan jalur basis API yang menjadi tempat API Shield akan disebarkan dan meng-upload file skema. Segera setelah API Shield dengan Validasi Skema disebarkan, dapat diperiksa titik ujung yang telah diproses oleh Firewall dan tingkat perlindungan yang diberikan. Di halaman tinjauan, terdapat dua kelompok titik ujung: dilindungi dan tidak dilindungi. Kelompok pertama mencantumkan semua titik ujung dan metode yang skemanya didukung, sedangkan kelompok yang disebutkan terakhir menunjukkan titik ujung yang definisinya tidak didukung atau belum jelas. Untuk menghindari pemutusan lalu lintas yang diarahkan ke titik ujung yang tidak tercantum dalam file skema, kami menyertakan sebuah aturan akhir yang mencocokkan lalu lintas yang tidak diarahkan ke titik ujung apa pun yang dilindungi.

Setiap kali Validasi Skema mengidentifikasi permintaan yang tidak sesuai dan diambil tindakan seperti pemblokiran atau pembuatan log, maka satu peristiwa baru yang diberi tag dengan sumber 'API Shield' akan dibuat dan ditambahkan ke log Firewall. Pengguna dapat mengakses analitik dan log dengan membuka halaman Overview (Ikhtisar) untuk menelusuri data menggunakan fleksibilitas dari dasbor kami yang diperkuat oleh GraphQL.

Validasi skema melakukan pemeriksaan pada jalur, variabel jalur, parameter kueri, header, dan cookie, serta memungkinkan pembuatan log dari lalu lintas yang tidak sesuai. Validasi skema Beta sekarang tersedia secara luas untuk pelanggan Perusahaan — [isi formulir ini](http://www.cloudflare.com/waf/api-shield) untuk mendapatkan akses.

### Pencegahan Kehilangan Data

Kehilangan data adalah salah satu masalah keamanan terbesar yang memengaruhi organisasi kecil dan besar serta juga berdampak pada individu dan privasinya. Kehilangan data sensitif dapat berdampak besar pada perusahaan dalam hal dampak finansial, penurunan nilai merek, dan kepatuhan terhadap undang-undang terbaru tentang perlindungan data. Akhirnya, hilangnya data sensitif milik individu dapat memiliki efek yang merugikan dalam hal kerugian moneter dan masalah privasi.

Sebelumnya pada hari ini, kami telah mengumumkan paket produk Pencegahan Kehilangan Data atau Data Loss Prevention (DLP) kami; kini kami memperluas produk ini untuk mengidentifikasi data sensitif yang meninggalkan sumber Anda dalam fase respons terhadap permintaan HTTP atau API. Solusi ini mengevaluasi lalu lintas egress atau keluar, memeriksa muatan terhadap pola umum dari data sensitif. Pemeriksaan itu termasuk informasi pribadi yang dapat diidentifikasi seperti nomor Jaminan Sosial dan informasi keuangan, termasuk nomor kartu kredit, detail bank, dll. Untuk rilis pertama, pengguna akan dapat membuat log dari semua kecocokan yang dipicu oleh DLP. Kami berencana menambahkan tindakan lain seperti mengaburkan dan memblokir data sensitif yang meninggalkan sumber di belakang Cloudflare. Berikutnya, kami bermaksud membiarkan para pelanggan melakukan kustomisasi pada aturan untuk mengidentifikasi data sensitif yang spesifik untuk aplikasi mereka.

Kami mengembangkan DLP dengan mempertimbangkan kesederhanaan agar setiap pelanggan dapat dilindungi tanpa memerlukan jangka waktu penyiapan yang rumit dan memakan waktu. Kami merilis DLP sebagai kumpulan aturan terkelola yang dapat diaktifkan melalui tab Firewall Managed Rules (Aturan yang Dikelola Firewall). DLP dapat digunakan sebagai bagian dari WAF sebuah proxy terbalik, tetapi juga dapat digunakan sebagai bagian dari Cloudflare for Teams yang mengintegrasikan perlindungan data dalam konfigurasi Zero Trust. Integrasi yang ketat ini memungkinkan kontrol yang lebih baik terhadap orang yang dapat mengakses informasi sensitif dalam organisasi Anda.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-424 Embedded Image - Ew1rId](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48KJTRYYMM8458BQDTRRN0.png&w=715&h=343&f=webp&fit=cover&position=center)

DLP saat ini dalam versi beta dan kami merilisnya untuk pelanggan pengguna awal terpilih. [Isilah formulir ini](http://www.cloudflare.com/waf/api-shield) untuk bergabung dalam daftar tunggu.

Perlindungan Kehilangan Data dapat diaktifkan sebagai Kumpulan Aturan Terkelola.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Data Loss Protection can be turned on as a Managed Ruleset.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46VMJ3Q4E38K8HACD27MZQ.png&w=715&h=403&f=webp&fit=cover&position=center)

### Managed IP List (Daftar IP Terkelola): kecerdasan ancaman oleh Cloudflare

Kami meluncurkan Managed IP List atau Daftar IP Terkelola pertama kami yang akan tersedia untuk digunakan dalam Aturan Firewall. Pada Juli 2020, [kami merilis IP List](https://blog.cloudflare.com/introducing-ip-lists/) atau Daftar IP, yang memungkinkan pelanggan meng-upload daftar IP berukuran besar yang dapat digunakan saat menulis Aturan Firewall. Hari ini kami meluncurkan daftar yang dipilih dengan saksama oleh Cloudflare dan yang dapat digunakan oleh para pelanggan pada aturan mereka dengan cara yang sama seperti mereka menggunakan Daftar khusus yang di-upload.

'Proxy Terbuka Cloudflare' berisi IP dari Open SOCKS dan Proxy HTTP yang ditentukan oleh Cloudflare dengan menganalisis lalu lintas di tepi jaringannya. Hal itu tidak hanya terbatas pada permintaan API; aturan dapat berlaku untuk semua jenis lalu lintas yang dievaluasi oleh Firewall.

Daftar ini adalah feed pertama yang kami buat untuk umum berdasarkan kecerdasan ancaman Cloudflare yang mengoptimalkan skala dan jangkauan jaringan kami. Bagaimana kami mengisi daftar ini? Kami melihat permintaan dari setiap alamat IP yang dapat dirutekan secara publik di Internet. Cloudflare menggabungkan daftar sumber terbuka dengan jaringannya yang luas untuk mengidentifikasi proxy terbuka. Setelah memverifikasi proxy, Cloudflare menentukan IP keluar dan membuat daftar. Kemudian kami memasukkan data reputasi ini kembali ke sistem keamanan kami dan membuatnya tersedia untuk pelanggan dalam bentuk daftar IP terkelola.

Daftar ini tersedia untuk semua paket Perusahaan dan dapat digunakan dengan memilih 'Cloudflare Open Proxy' (Proxy Terbuka Cloudflare) di menu menurun yang mengumpulkan semua Daftar IP yang tersedia (lihat gambar di bawah).

Daftar terkelola Proxy Terbuka Cloudflare dapat digunakan langsung pada alat pembuat aturan Firewall.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare Open Proxies managed list can be used directly in the Firewall rule builder.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45RXVK8Y3HNQY66EK6YQ2B.png&w=715&h=404&f=webp&fit=cover&position=center)

### Kontrol lebih besar pada sertifikat klien

Kami meluncurkan mTLS dengan rilis pertama API Shield dengan mempertimbangkan aplikasi seluler dan perangkat IoT. Menjalankan autentikasi yang kuat dengan sertifikat sisi klien adalah langkah yang sangat efektif untuk melindungi lalu lintas dari pencurian dan penyalahgunaan data secara umum. Namun, jika perangkat IoT atau telepon seluler dicuri, hilang, atau diambil alih kendalinya oleh pelaku berbahaya, pengguna Cloudflare memerlukan cara untuk mencabut sertifikat yang dianggap berpotensi menimbulkan risiko keamanan. Memiliki kemampuan untuk secara permanen mengecualikan lalu lintas dari perangkat yang diserang adalah cara efektif untuk mencegah kehilangan data dan serangan berbahaya.

Banyak pelanggan kami yang mulai menanam sertifikat API Shield di dalam aplikasi mereka telah menerapkan solusi pencabutan menggunakan Workers dengan Workers KV. Meskipun memungkinkan kontrol granular pada sertifikat, solusi ini membutuhkan upaya pengembangan yang besar dari pelanggan kami dan tidak mudah ditingkatkan skalanya.

Untuk Security Week, kami merilis solusi terkelola lengkap untuk mencabut (dan memulihkan) sertifikat tanpa perlu menulis kode satu baris pun. Kami membangun antarmuka langsung untuk mengelola keseluruhan siklus hidup sertifikat Anda di tepi jaringan kami, mulai dari penerbitan hingga pencabutan. Kami menangani ini untuk Anda agar Anda dapat berfokus pada membangun aplikasi Anda tanpa khawatir harus menyiapkan Infrastruktur Kunci Publik (PKI) yang rumit dan mahal serta mengelola pencabutan pada perangkat yang berpotensi risiko. Titik sentuh pelanggan adalah tombol baru 'Revoke' (Cabut) dan 'Restore' (Pulihkan) di tab sertifikat klien, panggilan API pendukungnya, dan medan atau field baru untuk Aturan Firewall.

Setiap permintaan yang memberikan sertifikat ke tepi jaringan Cloudflare akan memiliki dua medan atau field Firewall dengan nilai yang ditetapkan: cf.tls_client_auth.cert_verified dan cf.tls_client_auth.cert_revoked. Permintaan itu diproses oleh Firewall di mana pengguna dapat menggabungkan kedua medan atau field ini dengan semua fungsionalitas Firewall yang lain. Hal itu memungkinkan pelanggan untuk menetapkan perilaku yang berbeda berdasarkan kondisi sertifikat yang telah diverifikasi atau telah diverifikasi tetapi dicabut. Hal itu juga memungkinkan Anda menerapkan kebijakan keamanan yang diperlukan sekaligus memberikan pengalaman yang memuaskan bagi pengguna akhir. Konfigurasi klasik adalah dengan hanya mengizinkan permintaan dengan sertifikat terverifikasi sambil meneruskan permintaan dari sertifikat yang telah dicabut ke halaman atau titik ujung yang berbeda untuk menangani pengecualian itu seperti dipersyaratkan oleh rancangan dari pengguna Anda.

Pengguna dapat mencabut sertifikat dengan membuka tab Client Certificate (Sertifikat Klien).

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Users can revoke certificates by visiting the Client Certificates tab.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45K8895H405YXRB4WDXEA5.png&w=715&h=638&f=webp&fit=cover&position=center)

### Apa yang sedang dipersiapkan

Tim Cloudflare sedang bekerja untuk merilis fitur tambahan dalam kategori API Shield. Kami berbicara dengan ratusan pelanggan yang menggunakan Cloudflare untuk lalu lintas API, dan muncul tiga fitur sebagai prioritas utama: Analytics API yang mendalam, alat Pembatasan Tingkat yang lebih fleksibel, dan integrasi dengan Deteksi Anomali API.

Validasi Skema dan Pencegahan Kehilangan Data dirilis hari ini dengan integrasi penuh pada mesin log dan analitik kami. Di masa mendatang kami berencana memperluas kemampuan menganalisis lalu lintas dan menyediakan peralatan bagi pelanggan untuk mengidentifikasi dan mengelola serangan yang secara spesifik diarahkan ke titik akhir API.

Pembatasan tingkat dari Cloudflare dirancang untuk bekerja dengan optimal untuk lalu lintas web yang memungkinkan Anda menulis aturan berdasarkan URL dan metode permintaan. Kini kami berupaya mengintegrasikan kekuatan Aturan Firewall dengan kontrol yang disediakan oleh pembatasan tingkat. Hal itu akan memungkinkan pengguna untuk melakukan segmentasi pada lalu lintas mereka dengan mengoptimalkan logika kuat yang tersedia di Firewall. Kami juga memperluas mekanisme penghitungan untuk menyertakan kemampuan untuk menilai batasan berdasarkan kunci API dan ID Pengguna.

Saat menargetkan lalu lintas API, pola serangan bisa sangat bervariasi, yang membuat solusi Pengelolaan Bot tradisional bukan bakal solusi ideal untuk mengidentifikasi perilaku yang mencurigakan. Pada hari Jumat ini kami akan mengumumkan dua fitur utama yang berfokus pada perlindungan lebih lanjut terhadap aplikasi Anda: API Discovery atau Penemuan API dan Anomaly Detection atau Deteksi Anomali. Penemuan API memungkinkan para pelanggan memetakan titik ujung mereka dan mendapatkan visibilitas mengenai area permukaan dari API mereka. Deteksi Anomali adalah solusi Cloudflare untuk memisahkan secara independen lalu lintas API yang baik dari aktivitas yang berbahaya secara andal dan dalam skala besar. Pelanggan akan dapat mengatur fitur ini bersama dengan mTLS, Validasi Skema, dan Pembatasan Tingkat untuk memaksimalkan tingkat perlindungan. Lihat blog kami pada hari Jumat ini untuk mempelajari lebih lanjut tentang produk baru ini.

Di halaman ini

Diskusikan Online

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fprotecting-apis-from-abuse-and-data-exfiltration%2F&t=Melindungi%20API%20Anda%20dari%20penyalahgunaan%20dan%20pencurian%20data)[](https://x.com/intent/post?text=Melindungi+API+Anda+dari+penyalahgunaan+dan+pencurian+data&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fprotecting-apis-from-abuse-and-data-exfiltration%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fprotecting-apis-from-abuse-and-data-exfiltration%2F)[](https://bsky.app/intent/compose?text=Melindungi+API+Anda+dari+penyalahgunaan+dan+pencurian+data+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fprotecting-apis-from-abuse-and-data-exfiltration%2F)[](https://mastodonshare.com/?text=Melindungi+API+Anda+dari+penyalahgunaan+dan+pencurian+data&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fprotecting-apis-from-abuse-and-data-exfiltration%2F)[](https://www.threads.net/intent/post?text=Melindungi+API+Anda+dari+penyalahgunaan+dan+pencurian+data+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fprotecting-apis-from-abuse-and-data-exfiltration%2F)

## Tag terkait

[API Shield](https://blog.cloudflare.com/id-id/tag/api-shield/)[DLP](https://blog.cloudflare.com/id-id/tag/dlp/)[Firewall](https://blog.cloudflare.com/id-id/tag/firewall/)[Security Week](https://blog.cloudflare.com/id-id/tag/security-week/)

Ikuti di Media Sosial

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Berlangganan untuk menerima pemberitahuan postingan baru

Alamat email

Kami tidak akan pernah membagikan alamat email Anda.

Berlangganan

Terima kasih telah berlangganan! Periksa kotak masuk Anda untuk mengonfirmasi.
