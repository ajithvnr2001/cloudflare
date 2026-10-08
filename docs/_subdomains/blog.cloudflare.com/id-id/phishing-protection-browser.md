---
url: https://blog.cloudflare.com/id-id/phishing-protection-browser/
title: Kontrol input pada situs yang mencurigakan dengan Cloudflare Browser Isolation | Blog Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:47:22.922508+00:00
---

# Kontrol input pada situs yang mencurigakan dengan Cloudflare Browser Isolation | Blog Cloudflare

> Source: https://blog.cloudflare.com/id-id/phishing-protection-browser/

[Blog](https://blog.cloudflare.com/id-id/)

[Berita Produk](https://blog.cloudflare.com/id-id/tag/product-news/)[CIO Week](https://blog.cloudflare.com/id-id/tag/cio-week/)[Cloudflare Zero Trust](https://blog.cloudflare.com/id-id/tag/cloudflare-zero-trust/)+3Tampilkan 3 tag lainnya

6 TagTampilkan 6 tag

  * Tag Post
  * [Berita Produk](https://blog.cloudflare.com/id-id/tag/product-news/)[Keamanan](https://blog.cloudflare.com/id-id/tag/security/)[Zero Trust](https://blog.cloudflare.com/id-id/tag/zero-trust/)
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



[Keamanan](https://blog.cloudflare.com/id-id/tag/security/)[Remote Browser Isolation](https://blog.cloudflare.com/id-id/tag/remote-browser-isolation/)[Zero Trust](https://blog.cloudflare.com/id-id/tag/zero-trust/)

[Berita Produk](https://blog.cloudflare.com/id-id/tag/product-news/)[CIO Week](https://blog.cloudflare.com/id-id/tag/cio-week/)[Cloudflare Zero Trust](https://blog.cloudflare.com/id-id/tag/cloudflare-zero-trust/)[Keamanan](https://blog.cloudflare.com/id-id/tag/security/)[Remote Browser Isolation](https://blog.cloudflare.com/id-id/tag/remote-browser-isolation/)[Zero Trust](https://blog.cloudflare.com/id-id/tag/zero-trust/)

7 Desember 2021

# Kontrol input pada situs yang mencurigakan dengan Cloudflare Browser Isolation

![Tim Obezuk](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW493E1Z2ETFY5MBFNHC8RJD.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Tim Obezuk](https://blog.cloudflare.com/id-id/author/tim-obezuk/)

4 menit dibaca

SALIN URL

Artikel ini juga tersedia dalam [English](https://blog.cloudflare.com/phishing-protection-browser/), [日本語](https://blog.cloudflare.com/ja-jp/phishing-protection-browser/), dan [简体中文](https://blog.cloudflare.com/zh-cn/phishing-protection-browser/).

![BLOG-668 Embedded Image - 0uFcuP](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4801R1V7DYNCF8074X8VNK.png&w=1600&h=900&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/v/r9/jg5+LG2s6t28uq4ta65+LK5+jT///p9/bf59/F2sqt2caq4dK45t7I5+bR///p+fXf6d7G28iu2sOq4c6459zI6eXR///s/vfi7eDJ38my3cSu5NC7697L7efU///y//3o8uXO5c+35Mu069fC8uXR8+3Z///6///v+O3V69i969W79OHK+e3Z+fPh///////1/fPZ8N/C8t3B+unR//Xg/vnn///////3//Xb8uHD9ODD/e3T//fi//vp)

Tim Anda sekarang dapat menggunakan layanan Cloudflare [Browser Isolation](https://www.cloudflare.com/teams/browser-isolation/) untuk melindungi dari serangan phishing dan pencurian kredensial di dalam browser web. Pengguna dapat menjelajahi lebih banyak Internet tanpa mengambil risiko. Administrator dapat menentukan kebijakan Zero Trust untuk melarang input keyboard dan transmisi file selama aktivitas penjelajahan berisiko tinggi.

Awal tahun ini, Cloudflare Browser Isolation memperkenalkan [kontrol perlindungan data](https://blog.cloudflare.com/data-protection-browser/) yang memanfaatkan kemampuan browser jarak jauh untuk mengelola semua input dan output antara pengguna dan situs web mana pun. Kami senang untuk memperluas fungsionalitas itu untuk menerapkan lebih banyak kontrol seperti melarang input keyboard dan unggahan file untuk mencegah serangan phishing dan pencurian kredensial di situs web berisiko tinggi dan tidak dikenal.

### **Tantangan bertahan melawan ancaman yang tidak diketahui**

Administrator yang melindungi tim mereka dari ancaman di Internet terbuka biasanya menerapkan Secure Web Gateway (SWG) untuk memfilter lalu lintas Internet berdasarkan umpan intelijen ancaman. Ini efektif untuk memitigasi ancaman yang diketahui. Pada kenyataannya, tidak semua situs web dapat dimasukkan dalam kategori berbahaya atau tidak berbahaya.

Misalnya, domain terparkir dengan perbedaan salah ketik ke properti web yang sudah ada dapat didaftarkan secara sah untuk produk yang tidak terkait atau dijadikan senjata sebagai serangan phishing. Positif palsu ditoleransi oleh administrator yang menghindari risiko tetapi mengorbankan produktivitas karyawan. Menemukan keseimbangan antara kebutuhan ini adalah seni yang bagus, dan bila diterapkan terlalu agresif akan menyebabkan frustrasi pengguna dan beban dukungan yang meningkat dari pengecualian micromanaging untuk traffic yang diblokir.

Gateway web aman lawas adalah instrumen tumpul yang memberikan opsi terbatas kepada tim keamanan untuk melindungi tim mereka dari ancaman di Internet. Mengizinkan atau memblokir situs web saja tidak cukup, dan tim keamanan modern memerlukan alat yang lebih canggih untuk sepenuhnya melindungi tim mereka tanpa mengorbankan produktivitas.

### **Pemfilteran cerdas dengan Cloudflare Gateway**

[Cloudflare Gateway](https://www.cloudflare.com/teams/gateway/) menyediakan gateway web yang aman bagi pelanggan di mana pun penggunanya bekerja. Administrator dapat membuat aturan yang mencakup pemblokiran risiko keamanan, pemindaian virus, atau pembatasan penjelajahan berdasarkan identitas grup SSO di antara opsi lainnya. Traffic pengguna meninggalkan perangkat mereka dan tiba di pusat data Cloudflare yang dekat dengan mereka, memberikan keamanan dan pencatatan tanpa memperlambat mereka.

Berbeda dengan instrumen konvensional di masa lalu, Cloudflare Gateway menerapkan kebijakan keamanan berdasarkan skala unik dari proses jaringan data Cloudflare. Misalnya, Cloudflare melihat lebih dari satu triliun kueri DNS setiap hari. Kami menggunakan data tersebut untuk membuat model komprehensif tentang tampilan kueri DNS yang "baik" — dan kueri DNS mana yang berbeda dan dapat mewakili tunneling DNS untuk eksfiltrasi data, misalnya. Kami menggunakan jaringan kami untuk membangun pemfilteran yang lebih cerdas dan mengurangi kesalahan positif. Anda dapat meninjau penelitian itu juga dengan [Cloudflare Radar](https://radar.cloudflare.com/).

Namun, kami tahu beberapa pelanggan ingin mengizinkan pengguna menavigasi ke tujuan di semacam zona "netral". Domain yang baru didaftarkan, atau baru dilihat oleh DNS resolver, dapat menjadi rumah bagi layanan baru yang hebat bagi tim Anda atau serangan mendadak untuk mencuri kredensial. Cloudflare bekerja untuk mengategorikan ini sesegera mungkin, tetapi pada menit-menit awal itu pengguna harus meminta pengecualian jika tim Anda langsung memblokir kategori ini.

### **Menjelajahi situs web yang tidak dikenal dengan aman**

Cloudflare Browser Isolation mengalihkan risiko menjalankan kode situs web yang tidak tepercaya atau berbahaya dari titik akhir pengguna ke browser jarak jauh yang dihosting di pusat data latensi rendah. Alih-alih memblokir situs web yang tidak dikenal secara agresif, dan berpotensi memengaruhi produktivitas karyawan, Cloudflare Browser Isolation memberikan kontrol kepada administrator tentang _bagaimana_ pengguna dapat berinteraksi dengan situs web yang berisiko.

Kecerdasan jaringan Cloudflare melacak properti Internet berisiko lebih tinggi seperti Typosquatting dan Domain Baru. Situs web dalam kategori ini bisa berupa situs web jinak, atau serangan phishing yang menunggu untuk dimanfaatkan. Administrator yang menghindari risiko dapat melindungi tim mereka tanpa memperkenalkan positif palsu dengan mengisolasi situs web ini dan menyajikan situs web dalam mode hanya-baca dengan menonaktifkan unggahan file, unduhan, dan input keyboard.

Pengguna dapat menjelajahi situs web yang tidak dikenal dengan aman tanpa risiko bocornya kredensial, mengirimkan file, dan menjadi korban serangan phishing. Jika pengguna memiliki alasan yang sah untuk berinteraksi dengan situs web yang tidak dikenal, mereka disarankan untuk menghubungi administrator mereka untuk mendapatkan izin yang lebih tinggi saat menjelajahi situs web.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![HTTP Policy rule builder with download, upload and keyboard settings disabled.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW469KZ3FE5NW8VGTSDPQF5Q.png&w=715&h=697&f=webp&fit=cover&position=center)

[Lihat dokumentasi pengembang kami untuk mempelajari lebih lanjut tentang kebijakan browser jarak jauh.](https://developers.cloudflare.com/cloudflare-one/policies/browser-isolation)

### **Memulai**

Cloudflare Browser Isolation terintegrasi secara native ke dalam layanan Secure Web Gateway dan Zero Trust Network Access Cloudflare, dan tidak seperti solusi isolasi browser jarak jauh yang lama, Cloudflare Browser Isolation tidak memerlukan tim TI untuk mengumpulkan beberapa solusi yang berbeda atau memaksa pengguna untuk mengubah browser web pilihan mereka.

Ancaman Zero Trust dan perlindungan data yang diberikan oleh Isolasi Browser menjadikannya ekstensi alami bagi perusahaan mana pun yang memercayai gateway web yang aman untuk melindungi bisnis mereka. Saat ini kami menyertakannya dengan Paket Perusahaan Cloudflare for Teams kami tanpa biaya tambahan.1[Mulailah di halaman web Zero Trust kami](https://www.cloudflare.com/teams/browser-isolation/).

* * *

1. Untuk 2.000 kursi pertama hingga 31 Des 2021

Di halaman ini

Diskusikan Online

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fphishing-protection-browser%2F&t=Kontrol%20input%20pada%20situs%20yang%20mencurigakan%20dengan%20Cloudflare%20Browser%20Isolation)[](https://x.com/intent/post?text=Kontrol+input+pada+situs+yang+mencurigakan+dengan+Cloudflare+Browser+Isolation&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fphishing-protection-browser%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fphishing-protection-browser%2F)[](https://bsky.app/intent/compose?text=Kontrol+input+pada+situs+yang+mencurigakan+dengan+Cloudflare+Browser+Isolation+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fphishing-protection-browser%2F)[](https://mastodonshare.com/?text=Kontrol+input+pada+situs+yang+mencurigakan+dengan+Cloudflare+Browser+Isolation&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fphishing-protection-browser%2F)[](https://www.threads.net/intent/post?text=Kontrol+input+pada+situs+yang+mencurigakan+dengan+Cloudflare+Browser+Isolation+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fphishing-protection-browser%2F)

## Tag terkait

[Berita Produk](https://blog.cloudflare.com/id-id/tag/product-news/)[CIO Week](https://blog.cloudflare.com/id-id/tag/cio-week/)[Cloudflare Zero Trust](https://blog.cloudflare.com/id-id/tag/cloudflare-zero-trust/)[Keamanan](https://blog.cloudflare.com/id-id/tag/security/)[Remote Browser Isolation](https://blog.cloudflare.com/id-id/tag/remote-browser-isolation/)[Zero Trust](https://blog.cloudflare.com/id-id/tag/zero-trust/)

Ikuti di Media Sosial

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Berlangganan untuk menerima pemberitahuan postingan baru

Alamat email

Kami tidak akan pernah membagikan alamat email Anda.

Berlangganan

Terima kasih telah berlangganan! Periksa kotak masuk Anda untuk mengonfirmasi.
