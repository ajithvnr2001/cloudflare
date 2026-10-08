---
url: https://blog.cloudflare.com/id-id/data-exfiltration-prevention/
title: Menggunakan Cloudflare untuk Pencegahan Kehilangan Data | Blog Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:46:28.054915+00:00
---

# Menggunakan Cloudflare untuk Pencegahan Kehilangan Data | Blog Cloudflare

> Source: https://blog.cloudflare.com/id-id/data-exfiltration-prevention/

[Blog](https://blog.cloudflare.com/id-id/)

[Cloudflare One](https://blog.cloudflare.com/id-id/tag/cloudflare-one/)[Data Loss Prevention](https://blog.cloudflare.com/id-id/tag/data-loss-prevention/)[Security Week](https://blog.cloudflare.com/id-id/tag/security-week/)

3 TagTampilkan 3 tag

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



[Cloudflare One](https://blog.cloudflare.com/id-id/tag/cloudflare-one/)[Data Loss Prevention](https://blog.cloudflare.com/id-id/tag/data-loss-prevention/)[Security Week](https://blog.cloudflare.com/id-id/tag/security-week/)

24 Maret 2021

# Menggunakan Cloudflare untuk Pencegahan Kehilangan Data

![Misha Yalavarthy](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW492FTNDM76E8SFJW5K9591.png&w=64&h=64&f=webp&fit=cover&position=center)

[Misha Yalavarthy](https://blog.cloudflare.com/id-id/author/misha/)

7 menit dibaca

SALIN URL

Artikel ini juga tersedia dalam [English](https://blog.cloudflare.com/data-exfiltration-prevention/), [Español](https://blog.cloudflare.com/es-es/data-exfiltration-prevention/), [日本語](https://blog.cloudflare.com/ja-jp/data-exfiltration-prevention/), [한국어](https://blog.cloudflare.com/ko-kr/data-exfiltration-prevention/), [简体中文](https://blog.cloudflare.com/zh-cn/data-exfiltration-prevention/), dan [ภาษาไทย](https://blog.cloudflare.com/th-th/data-exfiltration-prevention/).

![Using Cloudflare for Data Loss Prevention](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44JTYQQVKKKYR0QCYWWTXT.png&w=1870&h=984&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////+/3/8vLy7uvo8u7o9vPv8/Px7O3t////+v3/7+3u6eLe7OTc8uvk8/Dr7e7t////+v7/7Orr5NrV6drQ8eTa8+7m8PHt/////P//7uzt5tvW69rP8+Xa9/Do9PXx////////9fP37+Xi8+be++/n/ffy+fn4/////////v3/+/X1//fz//76/////v7/////////////////////////////////////////////////////////////////)

Pencurian data, atau kehilangan data, bisa menjadi pengalaman berat yang sangat memakan waktu dan mahal yang menyebabkan kerugian finansial, asosiasi negatif pada merek, dan sangsi dari hukum yang berfokus pada privasi. Sebagai contoh, sebuah insiden di mana informasi pengetahuan Litbang yang sensitif yang dimiliki jaringan dan meteran listrik pintar dari [sistem kontrol industri sebuah perusahaan utilitas listrik Amerika Utara](https://www.power-grid.com/td/what-we-learned-from-a-data-exfiltration-incident-at-an-electric-utility/#gref) dicuri melalui serangan yang diduga berasal dari dalam jaringan. Akses tanpa otorisasi ke data dari sebuah perusahaan utilitas dapat mengakibatkan serangan pada jaringan listrik pintar atau mati listrik.

Pada contoh lain, seorang peneliti keamanan menemukan titik akhir API yang terekspos dan tidak dikenal (tidak terdokumentasi) untuk [Gateway Cadangan Tesla](https://blog.rapid7.com/2020/11/17/dont-put-it-on-the-internet-tesla-backup-gateway-edition/) yang mungkin telah digunakan untuk mengekspor data atau melakukan perubahan tanpa otorisasi. Hal itu mungkin akan memiliki konsekuensi fisik yang sangat nyata apabila titik akhir API yang tidak memiliki autentikasi itu digunakan oleh penyerang untuk merusak baterai atau jaringan listrik yang terhubung.

Sumber: Laporan Penyelidikan Pelanggaran Data Tahun 2020 di Verizon

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Source: Verizon 2020 Data Breach Investigations Report](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44JXVW3E4W8DAJXXQM4B61.png&w=715&h=161&f=webp&fit=cover&position=center)

Kedua contoh ini menekankan pentingnya mempertimbangkan ancaman internal dan eksternal saat memikirkan tentang cara melindungi jaringan dari pencurian data. Ancaman orang-dalam tidak harus pengguna yang dengan sengaja melakukan tindakan merugikan: menurut Laporan Ancaman Orang-Dalam Tahun 2019 dari Fortinet, 71% dari beberapa organisasi yang disurvei merasa khawatir tentang pengguna ceroboh yang menyebabkan pelanggaran tidak disengaja dan 65% khawatir tentang pengguna yang mengabaikan kebijakan, tetapi tanpa niat jahat. Penyerang yang berhasil melakukan [peretasan Twitter pada tahun 2020](https://www.dfs.ny.gov/Twitter_Report) untuk mengakses akun orang terkemuka dimulai dengan serangan rekayasa sosial terhadap karyawannya. Penyerang kemudian meningkatkan serangan dengan alat administratif internal untuk mengubah pengaturan pada akun-akun pelanggan, termasuk membuat pos atas nama mereka atau membuat modifikasi pada email dan 2FA mereka.

Di permukaan mungkin terlihat seperti penipuan Bitcoin, tetapi penyerang juga [mengunduh dan mencuri data dari tujuh akun](https://blog.twitter.com/en_us/topics/company/2020/an-update-on-our-security-incident.html). Jika akun pengguna internal berhasil diserang melalui upaya vishing (bentuk serangan rekayasa sosial yang menggunakan phishing berbasis suara), maka menambahkan kunci yang sulit atau menerapkan izin akun yang terperinci ke peralatan administratif dapat menghalangi jangkauan penyerang. Di Security Week nanti kami menjelaskan peretasan Twitter itu dari sudut serangan pengambilalihan akun dan bagaimana hal itu sebenarnya dapat dimitigasi.

Pencurian data tidak memerlukan teknik canggih atau alat yang tidak dikenal. Pengguna yang terkena phishing digabung kebijakan yang terlalu permisif pada titik ujung, bukan sebaliknya terhadap suatu akun, dapat memberikan akses yang diperlukan penyerang untuk mencuri data. Memblokir domain berbahaya pada solusi perlindungan email adalah langkah yang diandalkan banyak tim keamanan untuk merespons serangan rekayasa sosial. Tetapi bagaimana jika sumber daya berbahaya dibagikan secara lateral dan bukan dari sumber eksternal ke sumber internal? Domain berbahaya dapat dibagikan di antara karyawan dalam obrolan atau melalui beberapa bentuk komunikasi lain yang bukan email. Hal ini dapat meninggalkan celah yang tidak menguntungkan bagi tim keamanan saat melindungi pengguna dan data internal.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-401 Embedded Image - hEAYC0](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44S40W838XYEXXDAJ2J1QA.png&w=715&h=248&f=webp&fit=cover&position=center)

Kami selalu menekankan penggunaan pendekatan banyak layer untuk pencegahan dan pemantauan. Untuk alat internal, kami memiliki kontrol akses yang berbasis peran dan berbasis risiko. Kami menempatkan aplikasi kami di belakang Access untuk layer otorisasi tambahan di atas autentikasi. Penambahan aplikasi SaaS di belakang Access memungkinkan kami menghubungkan pengguna secara aman dengan apa pun yang mereka butuhkan baik yang terletak di lokal ataupun di cloud. Dengan tenaga kerja jarak jauh, Access memungkinkan kami membuat konfigurasi kebijakan berdasarkan lokasi, jenis perangkat, postur perangkat, dan metode MFA. Saat kami beralih ke lingkungan tanpa VPN, Access bertindak pada tempatnya sebagai terowongan yang aman. Tim deteksi dan respons kami memantau log Access dan log aplikasi SaaS untuk mencari anomali. Dalam waktu dekat kami akan menambahkan pembuatan log pada Access dalam aplikasi SaaS, yang selanjutnya akan meningkatkan log dan membuatnya kontekstual.

Melindungi titik ujung menggunakan Cloudflare juga mencakup sebuah klien yang digunakan untuk menerapkan kebijakan. Aturan firewall Gateway dapat digunakan dengan Access untuk mengambil pendekatan yang lebih menyeluruh pada layer L4 (jaringan) dan L7 (HTTP). Kami menggunakan lokasi Gateway untuk membatasi kueri DNS ke domain berbahaya.

Dengan para karyawan yang bekerja jarak jauh, perusahaan tidak dapat menjalankan kebijakan jaringan bagi mereka di titik egress atau keluar kantor perusahaan. Dengan menggunakan klien desktop WARP kami dan Gateway di titik ujung pengguna kami, tim keamanan dapat memiliki visibilitas ke dalam log DNS dengan kemampuan menjalankan kebijakan yang sebelumnya pernah bisa digunakan di kantor perusahaan dengan sambil menjaga privasi. Gateway berfungsi sebagai penerjemah DNS pada perangkat perusahaan. Hal itu tidak hanya memungkinkan tim merespons insiden dan mengidentifikasi akar masalah secara lebih efisien, tetapi juga membantu pencegahan dengan mengidentifikasi mesin yang diserang karena telah membuka domain berbahaya. WARP memastikan bahwa lalu lintas DNS terenkripsi untuk melindungi privasi dari pengguna.

Alat Isolasi Browser kami memberikan perlindungan pada layer yang paling dekat dengan pengguna dan tempat mereka mungkin menghabiskan sebagian besar waktunya mengakses aplikasi berbasis cloud. Alat itu menjadi berguna baik untuk pencegahan maupun merespons. Alat itu dapat digunakan untuk menghilangkan akses ke aplikasi SaaS tertentu, mencegah pengguna menyalin/menempel, membatasi pencetakan, dan memblokir pengunduhan file. Dengan kata lain, data yang di-hos di layanan cloud dapat dilindungi di banyak titik penting yang akan membuatnya lebih sulit untuk dicuri. Melalui kebijakan, Isolasi Browser dapat dibuat konfigurasi untuk masing-masing domain, pengguna dan atau kategori situs web yang luas. Isolasi Browser juga memungkinkan alat perespons untuk dengan cepat mengidentifikasi titik ujung yang mungkin telah diserang karena mengunjungi domain yang dikenal berbahaya atau mengunduh file tertentu melalui browser.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-401 Embedded Image - wW9Ppy](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW485X2T19A08SP41SVPG8WE.png&w=715&h=373&f=webp&fit=cover&position=center)

Di sinilah model Zero Trust benar-benar berperan. Jika Anda belum pernah mendengarnya sebelumnya, berikut adalah [pengantar](https://www.cloudflare.com/learning/security/glossary/what-is-zero-trust/) yang sangat baik. Cloudflare Access adalah bagian penting dari kumpulan peralatan Cloudflare One yang membantu organisasi menerapkan model Zero Trust di jaringannya. Kami menggunakan Cloudflare Access untuk mengelola pendekatan yang seragam untuk kebijakan sumber daya internal. Sebagai Teknisi Keamanan di tim Deteksi dan Respons yang menanggapi insiden yang mengharuskan kami membuat perubahan akses yang berlaku di seluruh perusahaan, aplikasi Cloudflare Access dan Cloudflare Access for SaaS membuat kami mampu secara efisien mendorong kebijakan dan berfokus pada butir prioritas yang lebih tinggi tanpa harus khawatir tentang perubahan di tingkat aplikasi. Mengelola akses di satu titik pusat untuk aplikasi yang jika tidak harus dikelola secara tersendiri dapat meningkatkan waktu respons kita secara drastis.

Beralih ke layer API, API Shield Cloudflare bertindak sebagai titik primer untuk mengelola kontrol keamanan API. Bayangkan perangkat IoT yang terekspos melalui berbagai API, seperti Gateway Tesla. API Shield menyediakan pendekatan banyak layer untuk membatasi eksposur data secara tidak disengaja. Sebagai contoh, skema dapat divalidasi untuk meminimalkan kemungkinan sebuah sistem di hilir diserang oleh input yang tidak terduga; permintaan ke titik ujung dapat dibatasi untuk klien yang memegang sertifikat SSL/TLS klien yang valid; dan lalu lintas tidak diinginkan yang berasal dari sumber seperti proxy Open SOCKS dapat disaring, bersama dengan permintaan yang berasal dari perangkat atau wilayah yang seharusnya tidak berkomunikasi dengan API. Pengumuman hari ini mencakup kemampuan baru pengaburan data, dan nantinya di minggu ini kami akan mengumumkan cara untuk menemukan API "bayangan" yang mungkin tidak disadari oleh tim keamanan Anda serta menemukan aktivitas panggilan yang tidak wajar.

Sebagai teknisi Deteksi dan Respons, terdapat berbagai insiden pada masalah keamanan yang mengharuskan kami memahami dengan segera cara kerja dari akses untuk berbagai sistem ini. Sistem berbeda dikelola secara berbeda dan peran-peran tidak selalu didefinisikan secara seragam. Hal itu sangat menyulitkan untuk merespons dengan segera dan sering kali kami harus berdiskusi dengan pemilik sistem untuk lebih memahami akses itu. Menggunakan perlindungan banyak layer yang disediakan oleh Cloudflare One, Isolasi Browser, dan API Shield, tim keamanan ditempatkan pada posisi yang memungkinkan mereka berfokus pada pencegahan daripada bereaksi.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-401 Embedded Image - XmfgWu](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW490CNAXGQ5K7X0GMEVYM6P.png&w=715&h=298&f=webp&fit=cover&position=center)

Di halaman ini

Diskusikan Online

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fdata-exfiltration-prevention%2F&t=Menggunakan%20Cloudflare%20untuk%20Pencegahan%20Kehilangan%20Data)[](https://x.com/intent/post?text=Menggunakan+Cloudflare+untuk+Pencegahan+Kehilangan+Data&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fdata-exfiltration-prevention%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fdata-exfiltration-prevention%2F)[](https://bsky.app/intent/compose?text=Menggunakan+Cloudflare+untuk+Pencegahan+Kehilangan+Data+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fdata-exfiltration-prevention%2F)[](https://mastodonshare.com/?text=Menggunakan+Cloudflare+untuk+Pencegahan+Kehilangan+Data&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fdata-exfiltration-prevention%2F)[](https://www.threads.net/intent/post?text=Menggunakan+Cloudflare+untuk+Pencegahan+Kehilangan+Data+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fdata-exfiltration-prevention%2F)

## Tag terkait

[Cloudflare One](https://blog.cloudflare.com/id-id/tag/cloudflare-one/)[Data Loss Prevention](https://blog.cloudflare.com/id-id/tag/data-loss-prevention/)[Security Week](https://blog.cloudflare.com/id-id/tag/security-week/)

Ikuti di Media Sosial

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Berlangganan untuk menerima pemberitahuan postingan baru

Alamat email

Kami tidak akan pernah membagikan alamat email Anda.

Berlangganan

Terima kasih telah berlangganan! Periksa kotak masuk Anda untuk mengonfirmasi.
