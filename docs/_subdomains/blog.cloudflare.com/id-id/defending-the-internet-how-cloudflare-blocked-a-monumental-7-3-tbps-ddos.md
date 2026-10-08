---
url: https://blog.cloudflare.com/id-id/defending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos/
title: Melindungi Internet: Cara Cloudflare memblokir serangan DDoS 7,3 Tbps yang monumental | Blog Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:37:49.208524+00:00
---

# Melindungi Internet: Cara Cloudflare memblokir serangan DDoS 7,3 Tbps yang monumental | Blog Cloudflare

> Source: https://blog.cloudflare.com/id-id/defending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos/

[Blog](https://blog.cloudflare.com/id-id/)

[DDoS](https://blog.cloudflare.com/id-id/tag/ddos/)[Laporan DDoS](https://blog.cloudflare.com/id-id/tag/ddos-reports/)

2 TagTampilkan 2 tag

  * Tag Post
  * [DDoS](https://blog.cloudflare.com/id-id/tag/ddos/)[Laporan DDoS](https://blog.cloudflare.com/id-id/tag/ddos-reports/)
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



[DDoS](https://blog.cloudflare.com/id-id/tag/ddos/)[Laporan DDoS](https://blog.cloudflare.com/id-id/tag/ddos-reports/)

19 Juni 2025

# Melindungi Internet: cara Cloudflare memblokir serangan DDoS 7,3 Tbps yang monumental

![Omer Yoachimik](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW485W0MZ0R9VGWD75RQN9ZH.png&w=64&h=64&f=webp&fit=cover&position=center)

[Omer Yoachimik](https://blog.cloudflare.com/id-id/author/omer/)

12 menit dibaca

SALIN URL

Artikel ini juga tersedia dalam [English](https://blog.cloudflare.com/defending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos/), [Deutsch](https://blog.cloudflare.com/de-de/defending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos/), [Español](https://blog.cloudflare.com/es-es/defending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos/), [Français](https://blog.cloudflare.com/fr-fr/defending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos/), [日本語](https://blog.cloudflare.com/ja-jp/defending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos/), [한국어](https://blog.cloudflare.com/ko-kr/defending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos/), [Português](https://blog.cloudflare.com/pt-br/defending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos/), [ภาษาไทย](https://blog.cloudflare.com/th-th/defending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos/), dan [Nederlands](https://blog.cloudflare.com/nl-nl/defending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos/).

![BLOG-2834 Hero Image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46Y2ZG1G9298P8YPT052PY.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///////88/Hx5+br5ujt7e7y8PHx7+/r///////+8O/z4OLs3eLu5Onz6+7z7u/t////////7u712d/u1d3w3eX16O317vDw////////8PH52uHy1d/03uf56vD58fP1////////9vf+4+n33+f56O/+8vf+9/n5////////////8fP87/T+9/v//f///f7+/////////////Pz//f7/////////////////////////////////////////////)

Pada pertengahan Mei 2025, Cloudflare memblokir serangan DDoS terbesar yang pernah tercatat, yaitu serangan 7,3 terabita per detik (Tbps) yang mencengangkan. Hal ini terjadi tak lama setelah penerbitan [_laporan ancaman DDoS kami untuk Kuartal 1 2025_](https://blog.cloudflare.com/ddos-threat-report-for-2025-q1/) pada tanggal 27 April 2025, yang dalam laporan tersebut, kami menyoroti serangan yang mencapai 6,5 Tbps dan 4,8 miliar paket per detik (pps). Serangan 7,3 Tbps ini 12% lebih besar dari rekor kami sebelumnya dan 1 Tbps lebih besar dari serangan terbaru yang dilaporkan oleh reporter keamanan siber Brian Krebs di [_KrebsOnSecurity_](https://krebsonsecurity.com/2025/05/krebsonsecurity-hit-with-near-record-6-3-tbps-ddos/).

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2834 Image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW453A53NCMWX5CDMSCDQ6TM.png&w=715&h=322&f=webp&fit=cover&position=center)

_Rekor dunia baru: Serangan DDoS 7,3 Tbps diblokir secara otonom oleh Cloudflare_

Serangan tersebut menargetkan pelanggan Cloudflare, sebuah penyedia hosting yang menggunakan [_Magic Transit_](https://www.cloudflare.com/network-services/products/magic-transit/) untuk melindungi jaringan IP mereka. Makin banyak penyedia hosting dan infrastruktur penting Internet yang telah menjadi target serangan DDoS, sebagaimana yang kami laporkan dalam [_laporan ancaman DDoS terbaru_](https://blog.cloudflare.com/ddos-threat-report-for-2025-q1/#attacks-target-the-cloudflare-network-and-internet-infrastructure) kami. Gambar di bawah adalah kampanye serangan pada bulan Januari dan Februari 2025 yang melancarkan lebih dari 13,5 juta serangan DDoS terhadap infrastruktur Cloudflare dan penyedia hosting yang dilindungi oleh Cloudflare.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2834 Image 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44QFH41JXA01MWKJA4WNCN.png&w=715&h=278&f=webp&fit=cover&position=center)

_Kampanye serangan DDoS menargetkan infrastruktur Cloudflare dan penyedia hosting yang dilindungi oleh Cloudflare_

Mari kita mulai dengan beberapa data statistik, lalu menyelami cara sistem kami mendeteksi dan memitigasi serangan ini.

## Serangan 7,3 Tbps menghasilkan 37,4 terabita serangan dalam 45 detik

Angka 37,4 terabita bukan nilai yang mencengangkan dalam skala dewasa ini, tetapi menghasilkan 37,4 terabita serangan hanya dalam waktu 45 detik adalah hal yang luar biasa. Hal tersebut setara dengan membanjiri jaringan Anda dengan lebih dari 9.350 film HD berdurasi penuh, atau melakukan streaming 7.480 jam video definisi tinggi secara nonstop (hampir setara dengan satu tahun menonton film seri secara terus-menerus) dalam waktu hanya 45 detik. Jika seandainya data tersebut adalah musik, maka jumlah itu setara dengan mengunduh sekitar 9,35 juta lagu dalam waktu kurang dari satu menit, yang cukup untuk mengisi waktu pendengar selama 57 tahun berturut-turut. Bayangkan mengambil 12,5 juta foto beresolusi tinggi pada smartphone Anda dengan media penyimpanan yang tidak pernah habis. Jika Anda mengambil satu foto setiap hari, maka jumlah tersebut setara dengan pengambilan foto selama 4.000 tahun, tetapi dilakukan dalam 45 detik. 

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2834 Image 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW457QHPAPNF2MEMJSSTM5B1.png&w=715&h=495&f=webp&fit=cover&position=center)

 _Serangan DDoS 7,3 Tbps yang memecahkan rekor menghasilkan 37,4 TB dalam 45 detik_

## Detail serangan

Serangan tersebut membombardir rata-rata 21.925 port tujuan dari satu alamat IP yang dimiliki dan digunakan oleh pelanggan kami, dengan puncaknya pada 34.517 port tujuan per detik. Serangan tersebut juga berasal dari distribusi port sumber yang serupa. 

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2834 Image 4](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW496M1N59288D47J4QMFG9F.png&w=715&h=319&f=webp&fit=cover&position=center)

 _Distribusi port tujuan_

### Vektor serangan

Serangan 7,3 Tbps adalah serangan DDoS multivektor. Sekitar 99,996% lalu lintas serangan dikategorikan sebagai banjir UDP. Namun, sisanya sebesar 0,004%, yang mencakup 1,3 GB lalu lintas serangan, diidentifikasi sebagai serangan pantulan QOTD, serangan pantulan Echo, serangan pantulan NTP, serangan banjir UDP Mirai, banjir Portmap, dan serangan amplifikasi RIPv1.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2834 Image 5](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW447QBH13SB1BGGGNYCM2RJ.png&w=715&h=420&f=webp&fit=cover&position=center)

_Vektor serangan selain banjir UDP_

### Perincian vektor serangan

Berikut detail tentang berbagai vektor serangan yang teridentifikasi dalam serangan ini, cara organisasi dapat menghindari menjadi peserta pemantulan dan amplifikasi serangan, serta rekomendasi cara untuk melindungi diri dari berbagai serangan ini sambil menghindari dampak terhadap lalu lintas yang sah. Pelanggan Cloudflare dilindungi dari serangan ini.

#### Serangan DDoS UDP

  * **Tipe** : Flood (Banjir data)
  * **Cara kerjanya:** Sejumlah besar paket UDP dikirim ke berbagai port yang acak atau spesifik pada satu atau beberapa alamat IP target. Serangan ini dapat berupaya membuat sambungan Internet menjadi jenuh atau membanjiri peralatan dalam jalur Internet dengan jumlah paket yang melebihi kemampuan penanganan peralatan tersebut.
  * **Cara melindungi diri dari serangan:** Sebarkan perlindungan DDoS volumetrik berbasis cloud, terapkan pembatasan tingkat yang cerdas pada lalu lintas UDP, dan buang seluruh lalu lintas UDP yang tidak diinginkan.
  * **Cara menghindari dampak yang tidak diinginkan:** Pemfilteran agresif dapat mengganggu layanan UDP yang sah seperti VoIP, konferensi video, atau game online. Terapkan ambang batas dengan hati-hati.



#### Serangan DDoS QOTD

  * **Tipe:** Pantulan + Amplifikasi
  * **Cara kerjanya:** Menyalahgunakan Protokol Quote of the Day (QOTD), yang aktif pada port UDP 17 dan merespons dengan kutipan atau pesan singkat. Penyerang mengirim permintaan QOTD ke server yang terekspos dari alamat IP yang dipalsukan sehingga menyebabkan korban dibanjiri oleh respons yang diamplifikasi.
  * **Cara mencegah menjadi elemen pantulan/amplifikasi:** Nonaktifkan layanan QOTD dan blokir port UDP/17 pada semua server dan firewall.
  * **Cara melindungi diri dari serangan:** Blokir lalu lintas masuk di UDP/17. Buang lonjakan permintaan UDP paket kecil yang tidak normal.
  * **Cara menghindari dampak yang tidak diinginkan:** QOTD adalah protokol diagnostik/debugging yang sudah usang dan tidak digunakan oleh aplikasi modern. Menonaktifkan layanan tersebut tidak akan berakibat negatif pada layanan yang sah.



#### Serangan DDoS Echo

  * **Tipe:** Pantulan + Amplifikasi
  * **Cara kerjanya:** Memanfaatkan protokol Echo (port UDP/TCP 7) yang membalas data yang diterima dengan data yang sama. Penyerang memalsukan alamat IP korban sehingga menyebabkan perangkat memantulkan kembali data tersebut sehingga mengamplifikasi serangan.
  * **Cara mencegah menjadi elemen pantulan/amplifikasi:** Nonaktifkan layanan Echo di semua perangkat. Blokir port UDP/TCP 7 di jaringan tepi.
  * **Cara melindungi diri dari serangan:** Nonaktifkan layanan Echo dan blokir port TCP/UDP 7 pada perimeter jaringan.
  * **Cara menghindari dampak yang tidak diinginkan:** Echo adalah alat diagnostik yang sudah usang; menonaktifkan atau memblokirnya tidak akan berakibat negatif pada sistem modern.



#### Serangan DDoS NTP

  * **Tipe:** Pantulan + Amplifikasi
  * **Cara kerjanya:** Menyalahgunakan protokol NTP (Network Time Protocol) yang digunakan untuk menyinkronkan waktu melalui Internet. Penyerang mengeksploitasi perintah monlist pada server NTP versi lama (UDP/123) yang mengembalikan daftar besar berisi koneksi terbaru. Permintaan yang dipalsukan menyebabkan amplifikasi pantulan.
  * **Cara mencegah menjadi elemen pantulan/amplifikasi:** Tingkatkan atau konfigurasikan server NTP untuk menonaktifkan monlist. Batasi permintaan NTP hanya untuk alamat IP yang dipercaya.
  * **Cara melindungi diri dari serangan:** Nonaktifkan perintah monlist, perbarui perangkat lunak NTP, dan filter atau batasi laju lalu lintas UDP/123.
  * **Cara menghindari dampak yang tidak diinginkan:** Menonaktifkan monlist tidak berpengaruh terhadap sinkronisasi waktu. Namun, pemfilteran atau pemblokiran UDP/123 dapat memengaruhi sinkronisasi waktu jika dilakukan terlalu meluas. Pastikan hanya sumber tidak tepercaya atau eksternal yang diblokir.



#### Serangan UDP Mirai

  * **Tipe:** Flood (Banjir data)
  * **Cara kerjanya:**[_Botnet Mirai_](https://www.cloudflare.com/learning/ddos/glossary/mirai-botnet/), yang terdiri dari perangkat IoT yang telah dikuasai, membanjiri korban dengan menggunakan paket UDP acak atau yang spesifik untuk layanan tertentu (misalnya, DNS, layanan game).
  * **Cara mencegah agar tidak menjadi bagian dari botnet:** Amankan perangkat IoT Anda, ubah kata sandi default, tingkatkan firmware ke versi terbaru, lalu ikuti [_praktik terbaik keamanan IoT_](https://www.cloudflare.com/en-gb/learning/security/glossary/iot-security/) agar terhindar dari menjadi bagian botnet. Jika memungkinkan, pantau lalu lintas keluar untuk mendeteksi kejanggalan.
  * **Cara melindungi diri dari serangan:** Terapkan perlindungan DDoS volumetrik berbasis cloud dan pembatasan tingkat untuk lalu lintas UDP.
  * **Cara menghindari dampak yang tidak diinginkan:** Pertama, pahami jaringan Anda dan jenis lalu lintas yang Anda terima, khususnya protokol, sumbernya, dan tujuannya. Identifikasikan layanan yang berjalan melalui UDP yang perlu dilindungi dari dampak. Setelah mengidentifikasi layanan tersebut, Anda dapat menerapkan pembatasan tingkat dengan cara yang dapat mengecualikan berbagai titik akhir tersebut, atau memperhitungkan tingkat lalu lintas normal Anda. Jika tidak, pembatasan tingkat laju lalu lintas UDP secara agresif dapat berdampak terhadap lalu lintas sah Anda dan berdampak terhadap layanan yang berjalan melalui UDP seperti panggilan VoIP dan lalu lintas VPN.



#### Serangan DDoS Portmap

  * **Tipe:** Pantulan + Amplifikasi
  * **Cara kerjanya:** Menargetkan layanan Portmapper (UDP/111) yang digunakan oleh aplikasi berbasis Remote Procedure Call (RPC) untuk mengidentifikasi layanan yang tersedia. Permintaan yang dipalsukan menghasilkan respons pantulan.
  * **Cara mencegah menjadi elemen pantulan/amplifikasi:** Nonaktifkan layanan Portmapper jika tidak diperlukan. Jika diperlukan secara internal, batasi hanya untuk alamat IP yang dipercaya.
  * **Cara melindungi diri dari serangan:** Nonaktifkan layanan Portmapper jika tidak diperlukan, blokir lalu lintas masuk di port UDP/111. Gunakan Daftar Kontrol Akses (ACL/Access Control List) atau firewall untuk membatasi akses ke layanan RPC yang sudah diketahui.
  * **Cara menghindari dampak yang tidak diinginkan:** Menonaktifkan Portmapper dapat mengganggu aplikasi yang mengandalkan RPC (misalnya, protokol Network File System). Validasikan ketergantungan layanan sebelum dihapus.



#### Serangan DDoS RIPv1

  * **Tipe:** Pantulan + Amplifikasi (Rendah)
  * **Cara kerjanya:** Memanfaatkan protokol Informasi Perutean versi 1 (RIPv1), yaitu protokol perutean jarak-vektor model lama yang tanpa autentikasi dan menggunakan port UDP/520. Penyerang mengirimkan pembaruan perutean yang dipalsukan untuk membanjiri atau mengacaukan jaringan.
  * **Cara mencegah menjadi elemen pantulan/amplifikasi:** Nonaktifkan RIPv1 pada router. Gunakan RIPv2 dengan autentikasi apabila perutean diperlukan.
  * **Cara melindungi diri dari serangan:** Blokir lalu lintas masuk UDP/520 dari jaringan yang tidak tepercaya. Pantau pembaruan perutean yang tidak diharapkan.
  * **Cara menghindari dampak yang tidak diinginkan:** Sebagian besar RIPv1 sudah usang; penonaktifan protokol ini umumnya aman. Jika sistem lama mengandalkan protokol ini, validasikan perilaku perutean sebelum melakukan perubahan.



Semua rekomendasi di sini harus dipertimbangkan dengan konteks dan perilaku dari setiap jaringan atau aplikasi yang unik untuk menghindari dampak yang tidak diinginkan terhadap lalu lintas yang sah.

### Asal serangan

Serangan yang berasal dari 122.145 lebih alamat IP sumber yang mencakup 5.433 Sistem Otonom (AS/Autonomous System) di 161 negara. 

Hampir separuh dari lalu lintas serangan berasal dari Brasil dan Vietnam, yang masing-masing berjumlah sekitar seperempat. Sepertiga lainnya, secara gabungan, bersumber dari Taiwan, Tiongkok, Indonesia, Ukraina, Ekuador, Thailand, Amerika Serikat, dan Arab Saudi.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2834 Image 6](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47990F484HK1HQJB53YVE6.png&w=715&h=407&f=webp&fit=cover&position=center)

_Peringkat 10 teratas negara sumber lalu lintas serangan_

Jumlah rata-rata alamat IP sumber yang unik per detik adalah 26.855 dengan nilai puncak 45.097. 

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2834 Image 7](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47BMPT8HAWVMA1W1W6K9ZQ.png&w=715&h=304&f=webp&fit=cover&position=center)

 _Distribusi alamat IP sumber yang unik_

Serangan bersumber dari 5.433 jaringan ([_AS_](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/)) yang berbeda. Telefonica Brazil ([_AS27699_](https://radar.cloudflare.com/as27699)) menyumbang porsi terbesar lalu lintas serangan DDoS, yakni bertanggung jawab atas 10,5% dari keseluruhan serangan. Viettel Group ([_AS7552_](https://radar.cloudflare.com/as7552)) menyusul dengan angka yang mendekati, yaitu 9,8%, sedangkan China Unicom ([_AS4837_](https://radar.cloudflare.com/as4837)) dan Chunghwa Telecom ([_AS3462_](https://radar.cloudflare.com/as3462)) masing-masing menyumbang sebesar 3,9% dan 2,9%. China Telecom ([_AS4134_](https://radar.cloudflare.com/as4134)) menyumbang 2,8% dari lalu lintas tersebut. ASN lainnya dalam peringkat 10 teratas meliputi Claro NXT ([_AS28573_](https://radar.cloudflare.com/as28573)), VNPT Corp ([_AS45899_](https://radar.cloudflare.com/as45899)), UFINET Panama ([_AS52468_](https://radar.cloudflare.com/as52468)), STC ([_AS25019_](https://radar.cloudflare.com/as25019)), dan FPT Telecom Company ([_AS18403_](https://radar.cloudflare.com/as18403)), yang masing-masing menyumbang antara 1,3% dan 1,8% dari total lalu lintas serangan DDoS.  


![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2834 Image 8](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48CFW161VF8EB5SPKE4BDH.png&w=715&h=401&f=webp&fit=cover&position=center)

_Peringkat 10 teratas sistem otonom sumber_

### Feed gratis tentang ancaman botnet

Untuk membantu para penyedia hosting, penyedia komputasi cloud, dan semua penyedia layanan Internet dalam mengidentifikasi dan menghentikan akun pelaku penyalahgunaan yang melancarkan berbagai serangan ini, kami memanfaatkan perspektif unik Cloudflare guna menyediakan [_Feed gratis tentang Ancaman Botnet DDoS bagi Para Penyedia Layanan_](https://developers.cloudflare.com/ddos-protection/botnet-threat-feed/). Lebih dari 600 organisasi di seluruh dunia telah mendaftar untuk feed ini. Feed ini memberikan daftar alamat IP penyerang kepada para penyedia layanan dari dalam Nomor Sistem Otonom (ASN) penyedia tersebut yang teridentifikasi oleh kami sebagai pelaku yang melancarkan serangan DDoS HTTP. Feed ini sepenuhnya gratis dan dapat diperoleh cukup dengan membuka akun gratis Cloudflare, melakukan autentikasi Nomor Sistem Otonom (ASN) melalui [_PeeringDB_](https://docs.peeringdb.com/howto/authenticate/), kemudian [_mengambil feed melalui API_](https://developers.cloudflare.com/ddos-protection/botnet-threat-feed/#get-full-report).

## Cara serangan dideteksi dan dimitigasi

### Menggunakan sifat terdistribusi dari serangan DDoS untuk melawannya

Alamat IP yang diserang disiarkan dari jaringan Cloudflare menggunakan [_anycast_](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/) global. Artinya, paket serangan yang menargetkan IP dirutekan ke pusat data Cloudflare yang terdekat. Dengan menggunakan anycast global, kami dapat menyebarkan lalu lintas serangan dan menggunakan sifat terdistribusi serangan untuk melawan serangan itu sendiri sehingga kami dapat memitigasi serangan di dekat node botnet sambil tetap melayani pengguna dari pusat data yang terdekat dengan pengguna. Dalam kasus serangan ini, serangan terdeteksi dan dimitigasi di 477 pusat data di 293 lokasi di seluruh dunia. Di lokasi dengan lalu lintas tinggi, kami hadir di beberapa pusat data. 

### Deteksi dan mitigasi DDoS otonom

Jaringan global Cloudflare menjalankan setiap layanan di setiap pusat data. Layanan tersebut mencakup sistem deteksi dan mitigasi DDoS kami. Artinya, serangan dapat dideteksi dan dimitigasi sepenuhnya secara otonom, terlepas dari sumber asal serangan. 

### Sidik jari real-time

Saat paket masuk ke pusat data kami, paket tersebut akan mengalami [_penyeimbangan beban secara cerdas_](https://blog.cloudflare.com/unimog-cloudflares-edge-load-balancer/) ke server yang tersedia. Kami kemudian mengambil sampel paket secara langsung dari dalam kernel Linux, dari [__eXpress Data Path_ (XDP)_](https://en.wikipedia.org/wiki/Express_Data_Path) dengan menggunakan program [_Berkley Packer Filter yang diperluas (eBPF)_](https://en.wikipedia.org/wiki/EBPF) untuk mengarahkan sampel paket ke ruang pengguna tempat kami menjalankan analisis.

Sistem kami menganalisis sampel paket untuk mengidentifikasi pola yang mencurigakan berdasarkan mesin heuristik unik kami yang bernama _dosd_ (denial of service daemon). Dosd mencari pola dalam sampel paket, seperti menemukan kesamaan di bidang header paket dan mencari anomali paket, serta menerapkan teknik eksklusif lainnya.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2834 Image 9](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47KVQNE2FNZY927RQ17RBN.png&w=715&h=220&f=webp&fit=cover&position=center)

 _Diagram alir pembuatan sidik jari secara real-time_

Bagi pelanggan kami, sistem sidik jari yang kompleks ini dienkapsulasi sebagai kelompok _aturan terkelola_ yang mudah digunakan, [_Aturan Terkelola Perlindungan DDoS_](https://developers.cloudflare.com/ddos-protection/managed-rulesets/). 

Saat pola dideteksi oleh dosd, sistem akan menghasilkan beberapa permutasi dari sidik jari tersebut untuk menemukan sidik jari paling akurat yang akan memiliki efektivitas dan akurasi mitigasi tertinggi, yaitu untuk mencoba mencocokkan secara tepat dengan lalu lintas serangan tanpa berdampak pada lalu lintas yang sah. 

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2834 Image 10](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46TQCFDQQGJ1N78T9JE7FZ.png&w=715&h=532&f=webp&fit=cover&position=center)

 _Diagram sistem Perlindungan DDoS Cloudflare_

## Mitigasi

Kami menghitung berbagai sampel paket yang cocok dengan setiap permutasi sidik jari, lalu dengan menggunakan algoritma streaming data, kami menampilkan sidik jari dengan hit yang terbanyak. Ketika ambang batas aktivasi terlampaui, untuk menghindari positif palsu, aturan mitigasi yang menggunakan sintaksis sidik jari dikompilasi sebagai program eBPF untuk membuang paket yang cocok dengan pola serangan. Setelah serangan berakhir, aturan tersebut akan habis waktunya dan otomatis dihapus.

## Bertukar informasi tentang serangan

Sebagaimana yang kami sebutkan, setiap server mendeteksi dan memitigasi serangan secara otonom penuh sehingga menjadikan jaringan kami sangat efisien, tangguh, dan cepat dalam memblokir serangan. Selain itu, setiap server _menyebarkan informasi_ ([__multicast__](https://www.cloudflare.com/en-gb/learning/network-layer/what-is-igmp/#:~:text=What%20is%20multicasting%3F)) tentang permutasi sidik jari teratas di dalam pusat data, dan secara global. Pembagian intelijen ancaman real-time ini membantu meningkatkan efektivitas mitigasi di dalam pusat data dan secara global. 

## Melindungi Internet

Sistem kami berhasil memblokir serangan DDoS 7,3 Tbps, yang memecahkan rekor, secara otonom sepenuhnya tanpa membutuhkan campur tangan manusia, tanpa memicu peringatan apa pun, dan tanpa menyebabkan insiden apa pun. Hal ini menunjukkan efektivitas sistem perlindungan DDoS kami yang terdepan di dunia. Kami membangun sistem ini sebagai bagian dari misi kami untuk membantu mengembangkan Internet yang lebih baik, dengan komitmen menyediakan perlindungan DDoS secara gratis tanpa batasan kuota.

Di halaman ini

Diskusikan Online

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fdefending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos%2F&t=Melindungi%20Internet%3A%20cara%20Cloudflare%20memblokir%20serangan%20DDoS%207%2C3%20Tbps%20yang%20monumental)[](https://x.com/intent/post?text=Melindungi+Internet%3A+cara+Cloudflare+memblokir+serangan+DDoS+7%2C3+Tbps+yang+monumental&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fdefending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fdefending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos%2F)[](https://bsky.app/intent/compose?text=Melindungi+Internet%3A+cara+Cloudflare+memblokir+serangan+DDoS+7%2C3+Tbps+yang+monumental+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fdefending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos%2F)[](https://mastodonshare.com/?text=Melindungi+Internet%3A+cara+Cloudflare+memblokir+serangan+DDoS+7%2C3+Tbps+yang+monumental&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fdefending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos%2F)[](https://www.threads.net/intent/post?text=Melindungi+Internet%3A+cara+Cloudflare+memblokir+serangan+DDoS+7%2C3+Tbps+yang+monumental+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fdefending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos%2F)

## Tag terkait

[DDoS](https://blog.cloudflare.com/id-id/tag/ddos/)[Laporan DDoS](https://blog.cloudflare.com/id-id/tag/ddos-reports/)

Ikuti di Media Sosial

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Berlangganan untuk menerima pemberitahuan postingan baru

Alamat email

Kami tidak akan pernah membagikan alamat email Anda.

Berlangganan

Terima kasih telah berlangganan! Periksa kotak masuk Anda untuk mengonfirmasi.
