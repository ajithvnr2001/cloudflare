---
url: https://blog.cloudflare.com/id-id/pii-and-selective-logging-controls-for-cloudflares-zero-trust-platform/
title: Kontrol PII dan Log Selektif untuk Platform Zero Trust Cloudflare | Blog Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:46:18.439943+00:00
---

# Kontrol PII dan Log Selektif untuk Platform Zero Trust Cloudflare | Blog Cloudflare

> Source: https://blog.cloudflare.com/id-id/pii-and-selective-logging-controls-for-cloudflares-zero-trust-platform/

[Blog](https://blog.cloudflare.com/id-id/)

[CIO Week](https://blog.cloudflare.com/id-id/tag/cio-week/)[Cloudflare Gateway](https://blog.cloudflare.com/id-id/tag/gateway/)[Cloudflare One](https://blog.cloudflare.com/id-id/tag/cloudflare-one/)+3Tampilkan 3 tag lainnya

6 TagTampilkan 6 tag

  * Tag Post
  * [Cloudflare Gateway](https://blog.cloudflare.com/id-id/tag/gateway/)[Keamanan](https://blog.cloudflare.com/id-id/tag/security/)
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



[Firewall](https://blog.cloudflare.com/id-id/tag/firewall/)[Keamanan](https://blog.cloudflare.com/id-id/tag/security/)[Logs](https://blog.cloudflare.com/id-id/tag/logs/)

[CIO Week](https://blog.cloudflare.com/id-id/tag/cio-week/)[Cloudflare Gateway](https://blog.cloudflare.com/id-id/tag/gateway/)[Cloudflare One](https://blog.cloudflare.com/id-id/tag/cloudflare-one/)[Firewall](https://blog.cloudflare.com/id-id/tag/firewall/)[Keamanan](https://blog.cloudflare.com/id-id/tag/security/)[Logs](https://blog.cloudflare.com/id-id/tag/logs/)

6 Desember 2021

# Kontrol PII dan Log Selektif untuk Platform Zero Trust Cloudflare

![Ankur Aggarwal](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47NKH772PAS2QKG6BFKRHR.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Abe Carryl](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46JJ6YPQY3M4A69P72QXE8.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Ankur Aggarwal](https://blog.cloudflare.com/id-id/author/ankur/) dan [Abe Carryl](https://blog.cloudflare.com/id-id/author/abe/)

5 menit dibaca

SALIN URL

Artikel ini juga tersedia dalam [English](https://blog.cloudflare.com/pii-and-selective-logging-controls-for-cloudflares-zero-trust-platform/), [日本語](https://blog.cloudflare.com/ja-jp/pii-and-selective-logging-controls-for-cloudflares-zero-trust-platform/), [简体中文](https://blog.cloudflare.com/zh-cn/pii-and-selective-logging-controls-for-cloudflares-zero-trust-platform/), dan [ภาษาไทย](https://blog.cloudflare.com/th-th/pii-and-selective-logging-controls-for-cloudflares-zero-trust-platform/).

![PII and Selective Logging controls for Cloudflare’s Zero Trust platform](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW464M9Q06RY516BXK2535GP.png&w=964&h=537&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA//rq+/Lh8ePR69vK7uPU8+3e8ezc6eLP//7t/PXk7+PT59rN7OPZ8u7l8e7i6uTT///y/vnp7uXX5dvT6uTh8/Ht8/Lp7OjX///3//3u8One59/b7Ono9vb09/fv8O3d///7///z9vHm7ujj8/Hv/Pz4/Pzz9fLi///9///4/vnt9/Lr+/rz///6///0+vfl///////7///z//rx///2///6///0/vrn///////8///1//3z///3///6///0//vo)

Di Cloudflare, kami percaya Anda tak perlu kompromi dengan privasi demi keamanan. Tahun lalu, kami meluncurkan Gateway Cloudflare — Secure Web Gateway komprehensif dengan kontrol penelusuran Zero Trust bawaan bagi organisasi Anda. Hari ini, kami dengan gembira membagikan rangkaian fitur privasi terkini yang disediakan bagi administrator guna memasukkan log dan mengaudit peristiwa berdasarkan kebutuhan tim Anda.

### **Melindungi organisasi Anda**

Gateway Cloudflare membantu organisasi mengganti firewall lama sekaligus menerapkan kontrol Zero Trust bagi pengguna mereka. Gateway menemui Anda di mana pun pengguna Anda berada serta mengizinkan mereka terhubung ke Internet atau bahkan jaringan pribadi Anda yang ada di Cloudflare. Hal ini memperluas perimeter keamanan Anda tanpa perlu membeli atau memelihara kotak tambahan.

Organisasi juga diuntungkan dengan peningkatan kinerja pengguna, yang lebih dari sekadar menghilangkan backhaul lalu lintas ke kantor atau pusat data. Jaringan Cloudflare menghadirkan filter keamanan yang lebih dekat dengan pengguna di lebih dari 250 kota di dunia. Pelanggan akan memulai koneksi mereka menggunakan [resolver DNS tercepat di dunia](https://blog.cloudflare.com/announcing-1111/). Setelah terhubung, Cloudflare dengan cerdas merutekan lalu lintas mereka melalui jaringan kami dengan filter jaringan layer 4 dan layer 7 HTTP.

Untuk memulai, administrator memberlakukan klien Cloudflare (WARP) pada perangkat pengguna, baik macOS, Windows, iOS, Android, ChromeOS, maupun Linux. Klien kemudian mengirimkan semua lalu lintas layer 4 keluar ke Cloudflare, beserta identitas pengguna pada perangkat.

Dengan mengaktifkan proxy dan deskripsi TLS, Cloudflare akan memasukkan log semua lalu lintas yang dikirimkan melalui Gateway, lalu menampilkannya pada dasbor Cloudflare berupa raw log dan analitik agregat. Akan tetapi, dalam sejumlah kasus, administrator mungkin tidak ingin menyimpan log atau mengizinkan akses ke semua anggota tim keamanannya.

Alasannya beragam, tetapi hasil akhirnya sama: administrator harus mampu mengontrol cara data pengguna dikumpulkan dan siapa yang dapat mengaudit catatan tersebut.

Biasanya, solusi lama memberi administrator penyelesaian yang kurang efisien dan tanpa titik tengah. Organisasi dapat mengaktifkan atau menonaktifkan semua penyimpanan log. Tanpa penyimpanan log, layanan tersebut tidak merekam informasi identitas pribadi (PII). Dengan menghindari PII, administrator tak lagi perlu mengkhawatirkan izin kendali atau akses, tetapi mereka kehilangan semua visibilitas untuk menyelidiki peristiwa keamanan.

Kurangnya visibilitas kian menyulitkan keadaan saat tim perlu menangani tiket dari pengguna mereka untuk menjawab pertanyaan seperti "mengapa saya terblokir?", "mengapa permintaan itu gagal?", atau "bukankah itu seharusnya sudah diblokir?". Tanpa log terkait peristiwa tersebut, tim Anda tidak dapat membantu pengguna akhir mendiagnosis jenis masalah ini.

### **Melindungi data Anda**

Mulai sekarang, tim Anda memiliki lebih banyak opsi untuk menentukan jenis informasi yang disimpan ke log oleh Gateway Cloudflare dan siapa yang dapat meninjaunya dalam organisasi Anda. Kami meluncurkan akses dasbor berbasis peran untuk halaman penyimpanan log dan analitik, serta penyimpanan log selektif peristiwa. Dengan akses berbasis peran, informasi PII mereka yang dapat mengakses akun Anda akan dihapus dari dasbor mereka secara default.

Kami dengan gembira membantu organisasi menyusun kontrol dengan hak paling rendah dalam cara mereka mengelola pemberlakuan Gateway Cloudflare. Anggota tim keamanan dapat terus mengelola kebijakan atau menyelidiki serangan agregat. Namun, sejumlah peristiwa perlu diselidiki lebih lanjut. Dengan perilisan hari ini, tim Anda dapat mendelegasikan kemampuan untuk meninjau dan mencari menggunakan PII bagi anggota tim tertentu.

Kami tahu sejumlah pelanggan ingin mengurangi log yang disimpan, dan kami pun dengan senang hati membantu mereka mengatasinya. Kini administrator dapat memilih tingkat log yang akan disimpan Cloudflare bagi mereka. Mereka dapat mengendalikannya untuk setiap komponen, DNS, Jaringan, atau HTTP dan bahkan dapat memilih untuk hanya menyimpan log peristiwa blokir.

Pengaturan ini bukan berarti semua log Anda hilang — hanya saja Cloudflare tidak pernah menyimpannya. Penyimpanan log selektif, apabila digabungkan dengan [layanan Logpush](https://blog.cloudflare.com/export-logs-from-cloudflare-gateway-with-logpush/) yang dirilis sebelumnya, memungkinkan pengguna menghentikan penyimpanan log pada Cloudflare, lalu mengaktifkan tugas Logpush pada tujuan di lokasi yang mereka pilih.

### **Cara Memulai**

Untuk memulai, pelanggan Gateway Cloudflare dapat mengunjungi [dasbor Cloudflare for Teams](https://dash.teams.cloudflare.com/settings/network) dan membuka Pengaturan >Jaringan. Opsi pertama pada halaman akan berfungsi untuk menetapkan preferensi Anda bagi penyimpanan log aktivitas. Gateway secara default akan menyimpan log semua peristiwa, termasuk kueri DNS, permintaan HTTP, dan sesi Jaringan. Dalam halaman pengaturan jaringan, Anda dapat menyempurnakan jenis peristiwa yang log-nya ingin disimpan. Anda akan menemukan tiga opsi untuk setiap komponen Gateway:

  1. Rekam semua
  2. Hanya rekam yang diblokir
  3. Jangan rekam



Selain itu, ada juga opsi untuk secara default menghilangkan semua PII dari log. Ini akan menghilangkan semua informasi yang mungkin dapat digunakan untuk mengenali pengguna, termasuk Nama Pengguna, Email Pengguna, ID Pengguna, ID Perangkat, IP sumber, URL, referrer, dan agen pengguna.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-840 Embedded Image - O7t3C0](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW475DN2QFSC1V9W4KPEDEJJ.png&w=715&h=278&f=webp&fit=cover&position=center)

Kami juga menyertakan peran baru dalam [dasbor Cloudflare](https://dash.cloudflare.com/), yang memberikan granularitas lebih baik saat membagi akses Administrator ke komponen Access atau Gateway. Peran baru ini akan diluncurkan pada Januari 2022 dan dapat diubah pada akun perusahaan dengan mengunjungi Beranda Akun → Anggota.

Apabila Anda belum siap membuat akun tetapi ingin menelusuri layanan Zero Trust kami, [tengok demo interaktif kami](https://www.cloudflare.com/teams/self-guided-tour-of-zero-trust-platform/) di mana Anda dapat mengikuti tur mandiri pada platform dengan narasi panduan kasus penggunaan utama, termasuk mengatur DNS dan filter HTTP dengan Gateway Cloudflare.

### **Apa Selanjutnya**

Ke depannya, kami bersemangat untuk terus menambahkan lebih banyak fitur privasi yang akan memberi Anda dan tim Anda lebih banyak kontrol granular terhadap lingkungan Anda. Fitur yang diumumkan hari ini tersedia bagi pengguna pada semua paket; tim Anda dapat membuka tautan ini untuk [memulai sekarang](https://dash.cloudflare.com/sign-up/teams).

Di halaman ini

Diskusikan Online

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fpii-and-selective-logging-controls-for-cloudflares-zero-trust-platform%2F&t=Kontrol%20PII%20dan%20Log%20Selektif%20untuk%20Platform%20Zero%20Trust%20Cloudflare)[](https://x.com/intent/post?text=Kontrol+PII+dan+Log+Selektif+untuk+Platform+Zero+Trust+Cloudflare&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fpii-and-selective-logging-controls-for-cloudflares-zero-trust-platform%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fpii-and-selective-logging-controls-for-cloudflares-zero-trust-platform%2F)[](https://bsky.app/intent/compose?text=Kontrol+PII+dan+Log+Selektif+untuk+Platform+Zero+Trust+Cloudflare+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fpii-and-selective-logging-controls-for-cloudflares-zero-trust-platform%2F)[](https://mastodonshare.com/?text=Kontrol+PII+dan+Log+Selektif+untuk+Platform+Zero+Trust+Cloudflare&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fpii-and-selective-logging-controls-for-cloudflares-zero-trust-platform%2F)[](https://www.threads.net/intent/post?text=Kontrol+PII+dan+Log+Selektif+untuk+Platform+Zero+Trust+Cloudflare+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fpii-and-selective-logging-controls-for-cloudflares-zero-trust-platform%2F)

## Tag terkait

[CIO Week](https://blog.cloudflare.com/id-id/tag/cio-week/)[Cloudflare Gateway](https://blog.cloudflare.com/id-id/tag/gateway/)[Cloudflare One](https://blog.cloudflare.com/id-id/tag/cloudflare-one/)[Firewall](https://blog.cloudflare.com/id-id/tag/firewall/)[Keamanan](https://blog.cloudflare.com/id-id/tag/security/)[Logs](https://blog.cloudflare.com/id-id/tag/logs/)

Ikuti di Media Sosial

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Berlangganan untuk menerima pemberitahuan postingan baru

Alamat email

Kami tidak akan pernah membagikan alamat email Anda.

Berlangganan

Terima kasih telah berlangganan! Periksa kotak masuk Anda untuk mengonfirmasi.
