---
url: https://blog.cloudflare.com/id-id/zero-trust-with-managed-devices/
title: Membuat aturan Zero Trust dengan perangkat terkelola | Blog Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:51:03.072635+00:00
---

# Membuat aturan Zero Trust dengan perangkat terkelola | Blog Cloudflare

> Source: https://blog.cloudflare.com/id-id/zero-trust-with-managed-devices/

[Blog](https://blog.cloudflare.com/id-id/)

[Cloudflare Access](https://blog.cloudflare.com/id-id/tag/cloudflare-access/)[Cloudflare Zero Trust](https://blog.cloudflare.com/id-id/tag/cloudflare-zero-trust/)[Keamanan](https://blog.cloudflare.com/id-id/tag/security/)+3Tampilkan 3 tag lainnya

6 TagTampilkan 6 tag

  * Tag Post
  * [Cloudflare Access](https://blog.cloudflare.com/id-id/tag/cloudflare-access/)[Keamanan](https://blog.cloudflare.com/id-id/tag/security/)[Security Week](https://blog.cloudflare.com/id-id/tag/security-week/)[Zero Trust](https://blog.cloudflare.com/id-id/tag/zero-trust/)
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



[Security Week](https://blog.cloudflare.com/id-id/tag/security-week/)[Teams Dashboard](https://blog.cloudflare.com/id-id/tag/teams-dashboard/)[Zero Trust](https://blog.cloudflare.com/id-id/tag/zero-trust/)

[Cloudflare Access](https://blog.cloudflare.com/id-id/tag/cloudflare-access/)[Cloudflare Zero Trust](https://blog.cloudflare.com/id-id/tag/cloudflare-zero-trust/)[Keamanan](https://blog.cloudflare.com/id-id/tag/security/)[Security Week](https://blog.cloudflare.com/id-id/tag/security-week/)[Teams Dashboard](https://blog.cloudflare.com/id-id/tag/teams-dashboard/)[Zero Trust](https://blog.cloudflare.com/id-id/tag/zero-trust/)

30 Maret 2021

# Membuat aturan Zero Trust dengan perangkat terkelola

![Kenny Johnson](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW471W94YNK8KYMJEK8P7RHD.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Kenny Johnson](https://blog.cloudflare.com/id-id/author/kenny/)

4 menit dibaca

SALIN URL

Artikel ini juga tersedia dalam [English](https://blog.cloudflare.com/zero-trust-with-managed-devices/) dan [ภาษาไทย](https://blog.cloudflare.com/th-th/zero-trust-with-managed-devices/).

![Build Zero Trust rules with managed devices](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45BRTFF1KH73XXP3T3RKY9.png&w=1614&h=794&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////+/z77u/w5ufp6enp7vDt7vDt6erq/////f798O/v6OXk6+fi8e7n8fDr6+zs////////9PHw7Obh7+fd9e7j9fHr8O/w////////+vb08uvk9Ovf+vLm+/bv9fT1//////////78+fPu/PXr//vx//34+/r8//////////////78///7////////////////////////////////////////////////////////////////////////////)

Mulai hari ini, tim Anda dapat menggunakan Cloudflare Access untuk membuat aturan yang hanya mengizinkan pengguna terhubung ke aplikasi dari perangkat yang dikelola perusahaan Anda. Anda dapat menggabungkan persyaratan ini dengan aturan lain di platform Zero Trust Cloudflare, termasuk identitas, metode multifaktor, dan geografi.

Seiring dengan semakin banyaknya organisasi yang memakai model keamanan Zero Trust dengan Cloudflare Access, kami mendengar dari pelanggan yang ingin mencegah koneksi dari perangkat yang tidak mereka miliki atau kelola. Untuk beberapa bisnis, tenaga kerja jarak jauh meningkatkan risiko kehilangan data saat pengguna mana pun dapat login ke aplikasi sensitif dari tablet yang tidak terkelola. Perusahaan lain harus memenuhi persyaratan kepatuhan baru yang membatasi pekerjaan hanya pada perangkat perusahaan.

Kami senang membantu tim dengan berbagai ukuran dalam menerapkan model keamanan ini, meskipun organisasi Anda tidak memiliki platform pengelolaan perangkat atau pengelola perangkat seluler (MDM) saat ini. Teruslah membaca untuk mempelajari bagaimana Cloudflare Access memecahkan masalah ini dan bagaimana Anda dapat memulai.

### **Tantangan perangkat yang tidak terkelola**

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![We’re excited to help teams of any size apply this security model, even if your organization does not have a device management platform or mobile device manager \(MDM\) today.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW448MCQR43C6G72TZH00QF0.png&w=715&h=352&f=webp&fit=cover&position=center)

Perusahaan yang mempunyai perangkat perusahaan memiliki suatu tingkat kendali atas perangkat tersebut. Administrator dapat menetapkan, mencabut, memeriksa, dan mengelola perangkat di inventaris mereka. Baik tim yang mengandalkan platform manajemen atau spreadsheet sederhana, bisnis dapat memperlakukan perangkat perusahaan sebagai milik mereka.

Visibilitas dan pengelolaan tersebut tidak berlaku untuk perangkat pribadi — dan kami semua senang bahwa hal tersebut adalah benar. Namun, nilai yang sama menyebabkan masalah ketika perusahaan perlu membatasi data atau akses ke aplikasi khusus perangkat perusahaan. Jika saya dapat login ke sistem dan men-download data di perangkat pribadi, saya telah menyebabkan masalah baru untuk tim TI dan keamanan.

Penyedia Single Sign-On (SSO) dan aplikasi SaaS mempermudah kesalahan tersebut terjadi, baik sengaja atau tidak. Pengguna dapat login ke aplikasi perusahaan hanya dengan menggunakan kembali kata sandi mereka. Meski organisasi menerapkan metode multifaktor seperti autentikasi hard key, pengguna cukup mencolokkan hard key mereka ke perangkat pribadi.

### **Solusi Cloudflare**

Kami senang memberi tim kemampuan untuk mempertahankan kontrol atas data dengan memastikannya tetap berada di perangkat perusahaan. Cloudflare Access adalah platform Zero Trust komprehensif yang dapat digunakan oleh administrator untuk membuat aturan berdasarkan identitas dan sinyal lainnya. Tim dapat membuat aturan untuk aplikasi yang dikelola sendiri dan SaaS. Setiap permintaan dan login ditangkap dan semuanya dibuat lebih cepat untuk pengguna akhir di jaringan global Cloudflare.

Anda sekarang dapat menggunakan platform Zero Trust Cloudflare untuk membangun jenis aturan baru: hanya mengizinkan koneksi atau login dari perangkat milik perusahaan. Anda dapat menggunakan sistem inventaris Anda sendiri, apakah itu spreadsheet sederhana atau API dari platform MDM. Agen Cloudflare for Teams kami berjalan di perangkat dan mengumpulkan detail tentang perangkat keras, memeriksanya dengan membandingkannya dengan inventaris Anda, dan dengan edge Cloudflare langsung membuat keputusan.

### **Bagaimana cara kerjanya**

Menerapkan perangkat perusahaan di Access membutuhkan waktu sekitar 20 menit untuk setup dan hanya mengharuskan Anda memiliki daftar nomor seri perangkat perusahaan.

Langkah pertama adalah membuat dan mengimpor daftar nomor seri perangkat terkelola Anda. Daftar nomor seri dapat di-upload secara massal atau dibuat secara manual langsung di Dasbor Teams. Banyak alat inventaris dan manajemen aset menyediakan cara mudah untuk mengekspor nomor seri perangkat.

Meng-upload nomor seri baru melalui API juga dapat dilakukan yang memungkinkan otomatisasi saat perangkat baru dibeli.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-450 Embedded Image - ZWCSGE](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW447NYNEDMGBSKTC76DNR9E.png&w=715&h=349&f=webp&fit=cover&position=center)

Langkah selanjutnya adalah memberlakukan klien WARP di seluruh mesin perusahaan Anda. Pengguna dapat [men-download](https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/warp/download-warp) dan menginstal klien sendiri atau klien dapat diinstal melalui [solusi MDM](https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/warp/deployment).

Itulah yang diperlukan untuk mulai menerapkan akses Zero Trust yang dikhususkan untuk perangkat perusahaan! Anda sekarang dapat membuat Aturan Access yang memeriksa apakah nomor seri perangkat ada dalam daftar perangkat terkelola.

Sekarang, meski pengguna memindahkan hard-key mereka dan menginstal WARP di perangkat pribadi, mereka tetap diblokir karena tidak ada dalam daftar nomor seri perusahaan.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![You will now be able to build Access rules that check if a device’s serial number is in the managed devices list.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47VZR810Y6B5NZG1DBPB9R.png&w=715&h=345&f=webp&fit=cover&position=center)

### **Memulai**

Jika Anda ingin mulai mengunci aplikasi khusus untuk perangkat perusahaan, [daftar](https://www.cloudflare.com/teams/access/) akun Teams gratis hingga 50 pengguna. Jika Anda sudah menjadi pelanggan, fitur ini tersedia di Dasbor Teams Anda hari ini dan dapat disiapkan melalui [panduan berikut](https://developers.cloudflare.com/cloudflare-one/tutorials/corp-device-tag).

Di halaman ini

Diskusikan Online

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fzero-trust-with-managed-devices%2F&t=Membuat%20aturan%20Zero%20Trust%20dengan%20perangkat%20terkelola)[](https://x.com/intent/post?text=Membuat+aturan+Zero+Trust+dengan+perangkat+terkelola&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fzero-trust-with-managed-devices%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fzero-trust-with-managed-devices%2F)[](https://bsky.app/intent/compose?text=Membuat+aturan+Zero+Trust+dengan+perangkat+terkelola+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fzero-trust-with-managed-devices%2F)[](https://mastodonshare.com/?text=Membuat+aturan+Zero+Trust+dengan+perangkat+terkelola&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fzero-trust-with-managed-devices%2F)[](https://www.threads.net/intent/post?text=Membuat+aturan+Zero+Trust+dengan+perangkat+terkelola+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fzero-trust-with-managed-devices%2F)

## Tag terkait

[Cloudflare Access](https://blog.cloudflare.com/id-id/tag/cloudflare-access/)[Cloudflare Zero Trust](https://blog.cloudflare.com/id-id/tag/cloudflare-zero-trust/)[Keamanan](https://blog.cloudflare.com/id-id/tag/security/)[Security Week](https://blog.cloudflare.com/id-id/tag/security-week/)[Teams Dashboard](https://blog.cloudflare.com/id-id/tag/teams-dashboard/)[Zero Trust](https://blog.cloudflare.com/id-id/tag/zero-trust/)

Ikuti di Media Sosial

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Berlangganan untuk menerima pemberitahuan postingan baru

Alamat email

Kami tidak akan pernah membagikan alamat email Anda.

Berlangganan

Terima kasih telah berlangganan! Periksa kotak masuk Anda untuk mengonfirmasi.
