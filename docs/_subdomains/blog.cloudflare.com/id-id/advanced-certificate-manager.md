---
url: https://blog.cloudflare.com/id-id/advanced-certificate-manager/
title: Memperkenalkan: Manajer Sertifikat Tingkat Lanjut | Blog Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:48:30.217290+00:00
---

# Memperkenalkan: Manajer Sertifikat Tingkat Lanjut | Blog Cloudflare

> Source: https://blog.cloudflare.com/id-id/advanced-certificate-manager/

[Blog](https://blog.cloudflare.com/id-id/)

[Advanced Certificate Manager](https://blog.cloudflare.com/id-id/tag/advanced-certificate-manager/)[Berita Produk](https://blog.cloudflare.com/id-id/tag/product-news/)[Keamanan](https://blog.cloudflare.com/id-id/tag/security/)+1Tampilkan 1 tag lainnya

4 TagTampilkan 4 tag

  * Tag Post
  * [Berita Produk](https://blog.cloudflare.com/id-id/tag/product-news/)[Keamanan](https://blog.cloudflare.com/id-id/tag/security/)[Security Week](https://blog.cloudflare.com/id-id/tag/security-week/)
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

[Advanced Certificate Manager](https://blog.cloudflare.com/id-id/tag/advanced-certificate-manager/)[Berita Produk](https://blog.cloudflare.com/id-id/tag/product-news/)[Keamanan](https://blog.cloudflare.com/id-id/tag/security/)[Security Week](https://blog.cloudflare.com/id-id/tag/security-week/)

27 Maret 2021

# Memperkenalkan: Manajer Sertifikat Tingkat Lanjut

![Dina Kozlov](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49DZ20ZY95S71GB0FPG6GC.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Dina Kozlov](https://blog.cloudflare.com/id-id/author/dina/)

7 menit dibaca

SALIN URL

Artikel ini juga tersedia dalam [English](https://blog.cloudflare.com/advanced-certificate-manager/), [日本語](https://blog.cloudflare.com/ja-jp/advanced-certificate-manager/), dan [ภาษาไทย](https://blog.cloudflare.com/th-th/advanced-certificate-manager/).

![Introducing: Advanced Certificate Manager](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW493PPCSQWNQXXK4NQ29KAB.png&w=1999&h=959&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////+/z68O/r6uXf7eTd8uji8Ovn6Ovo/////v798vHv6+fj7ebh8urm8e3r6u3r////////9fX07evp7+no9e7t9PHx7vHw////////+fr68e/w8+7v+fP0+fb38/b2////////////9vT2+PP2/vj7//z++fz9////////////+/j7/vf7//3///////////////////////v///r+//////////////////////////z///v/////////////)

Pada tahun 2016, kami meluncurkan [Sertifikat Khusus](https://blog.cloudflare.com/dedicated-ssl-certificates/). Hari ini, kami dengan senang hati mengumumkan bahwa sertifikat khusus mendapatkan peningkatan… dan nama baru… memperkenalkan Manajer Sertifikat Tingkat Lanjut! Manajer Sertifikat Tingkat Lanjut adalah cara yang fleksibel dan dapat disesuaikan untuk mengelola sertifikat Anda di Cloudflare.

### Sertifikat

Sertifikat TLS adalah alasan Anda dapat menjelajahi Internet dengan aman, mentransfer uang secara online dengan aman, dan menjaga kerahasiaan kata sandi Anda. Sertifikat TLS melakukannya dengan mengenkripsi pesan sensitif Anda menggunakan kriptografi kunci publik yang secara kriptografi ditautkan ke sertifikat itu sendiri. Tetapi lebih dari itu, sertifikat TLS digunakan untuk membuat pernyataan tentang identitas — yakni memverifikasi bahwa server sesuai sebagaimana yang diklaim. Sertifikat Server — digunakan oleh setiap situs web — mencantumkan nama situs web pada sertifikat dan dikeluarkan oleh otoritas sertifikat (CA) pihak ketiga yang memverifikasi bahwa informasi sertifikat sudah benar dan akurat.

Browser hanya mengizinkan Anda mengunjungi situs web apabila situs web dienkripsi menggunakan TLS setelah berhasil memvalidasi sertifikat yang diberikan oleh server — seperti cara keamanan memeriksa ID Anda untuk naik pesawat.

Saat ini, kami berfokus untuk mengamankan Internet lebih dari sebelumnya. Kami ingin membuatnya semudah mungkin bagi setiap pelanggan untuk menjadi pelanggan yang sadar akan keamanan. Inilah mengapa kami beralih ke sistem manajemen sertifikat, sehingga mudah untuk menyesuaikan sertifikat dan pengaturan TLS Anda. Kami melakukan ini dengan memberi Anda alat yang tepat agar secara proaktif meningkatkan keamanan domain Anda.

Mari kita mulai dengan membahas cara mengubah masa berlaku sertifikat Anda, perubahan kecil yang dapat membuat perbedaan besar.

### Mengurangi Masa Berlaku Sertifikat Anda

[Forum Browser Otoritas Sertifikasi](https://cabforum.org/) — grup sukarela yang menetapkan pedoman industri untuk sertifikat — telah mempersingkat masa berlaku maksimum untuk sertifikat yang dipercaya publik selama beberapa tahun terakhir. Sebelumnya, Anda bisa mendapatkan sertifikat dengan masa berlaku hingga tiga tahun, tetapi sekarang Anda hanya bisa mendapatkan sertifikat dengan masa berlaku hanya satu tahun. Mengapa mereka melakukan ini?

Merotasi sertifikat lebih sering akan — tetapi tidak selalu harus dilakukan — berarti Anda merotasi kunci privat Anda lebih sering. Mengubah rahasia lebih sering berarti bahwa jika rahasia (dalam hal ini kunci privat) pernah dibobol, pembobolan tersebut memiliki umur maksimum yang lebih kecil. Hal ini secara luas dianggap sebagai postur keamanan yang lebih baik dan membantu meminimalkan risiko yang terkait dengan pembobolan kunci.

Ini juga memiliki bonus tambahan guna [mendorong otomatisasi](https://letsencrypt.org/2015/11/09/why-90-days.html) — semakin sering Anda harus melakukan tugas, semakin besar kemungkinan Anda ingin mengotomatiskannya. Otomatisasi berarti Anda cenderung tidak membiarkan sertifikat kedaluwarsa selama produksi atau memberi seseorang akses ke materi kunci.

Dengan Manajer Sertifikat Tingkat Lanjut, Anda dapat mengatur masa berlaku sertifikat menjadi sesingkat 14 hari. Dengan memperpendek siklus hidup sertifikat, Anda secara proaktif meningkatkan postur keamanan Anda. Karena Anda terus merotasi sertifikat dan kunci privat setelah pembaruan, Anda mengurangi risiko paparan.

Bagi sebagian orang, menetapkan masa berlaku yang singkat dapat meningkatkan risiko waktu henti. Ini karena masa berlaku yang singkat memerlukan penerbitan sertifikat yang sering dan dapat membebani server.

Di Cloudflare, hal tersebut tidak menjadi masalah. Masa berlaku yang lebih pendek mendorong kami untuk terus meningkatkan jalur penerbitan dan perpanjangan sertifikat. Dengan ~4,5 juta sertifikat yang diterbitkan setiap hari, kami dapat dengan yakin mengatakan bahwa setiap pelanggan dapat menetapkan masa berlaku 14 hari dan kami akan menanganinya.

Secara keseluruhan, [industri sedang bergerak menuju pemendekan](https://www.websecurity.digicert.com/blog/cabforum-votes-shorten-certificate-lifetime-validity-periods-impacts#:~:text=This%20topic%20led%20to%20a,also%20had%20an%20unintended%20consequence.&text=However%2C%20effective%20April%2022%2C%202017,unless%20a%20corrective%20ballot%20passes.) siklus sertifikat, jadi kami sangat bersemangat untuk menjadikan ini pilihan yang mudah bagi pelanggan kami.

Beberapa pelanggan ingin melangkah lebih jauh dan mengontrol cipher suite yang digunakan untuk TLS. Sekarang, dengan ACM, Anda bisa melakukannya!

### Mengatur Cipher Suite

Cipher suite adalah satu set algoritme yang membantu mengamankan koneksi jaringan yang menggunakan TLS. Set algoritme yang berisi cipher suite adalah:

  * Algoritme Pertukaran Kunci
  * Algoritme Autentikasi
  * Algoritme enkripsi massal
  * Algoritme Kode Autentikasi Pesan (MAC)



Ketika dua server ingin berkomunikasi satu sama lain dengan aman melalui TLS, mereka akan mengawalinya dengan memulai jabat tangan TLS. Selama jabat tangan TLS, klien dan server menetapkan algoritme enkripsi mana yang akan mereka gunakan. Klien memulai jabat tangan ini dengan pesan Halo Klien yang menunjukkan cipher suite — atau algoritme enkripsi — yang didukungnya. Server kemudian merespons dengan pesan Server Halo yang berisi pilihan cipher berdasarkan daftar cipher yang didukung yang dikirim klien.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-445 Embedded Image - IuPmIr](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW466Z91CVHWNT4C8C8HM5F1.png&w=715&h=205&f=webp&fit=cover&position=center)

Saat pengguna terhubung ke situs web di jaringan Cloudflare, Cloudflare bertanggung jawab untuk memilih cipher. Di masa lalu, kami [telah membahas tentang](https://blog.cloudflare.com/staying-on-top-of-tls-attacks/) bagaimana server Cloudflare lebih memilih cipher tertentu. Misalnya, kami memprioritaskan cipher yang menggunakan ECDHE daripada yang dimulai dengan RSA. Seperti yang dibahas dalam postingan blog kami sebelumnya, RSA lebih rentan terhadap kerentanan keamanan, terutama jika kunci privat server SSL bocor.

Sambil memprioritaskan cipher tertentu di atas yang lain dengan menawarkan tingkat keamanan yang lebih tinggi, kami melangkah lebih jauh dan memberi pelanggan kami kemampuan untuk memilih cipher suite mana dari daftar cipher [yang disetujui Cloudflare](https://support.cloudflare.com/hc/en-us/articles/203041594-Cloudflare-SSL-cipher-browser-and-protocol-support) yang mereka inginkan untuk didukung situs web mereka. Bagi mereka yang ingin menghapus cipher yang lemah dan hanya mengizinkan cipher terkuat yang tersedia, mereka sekarang dapat melakukannya melalui satu panggilan API. Untuk melakukan ini, mereka akan menggunakan [titik akhir Pengaturan Cipher Suite](https://api.cloudflare.com/#zone-settings-change-ciphers-setting) dan menunjukkan daftar izin cipher untuk penghentian TLS.

Pelanggan seperti [OneTrust](https://onetrust.com/) dan [Report URI](https://report-uri.com/) menggunakan fungsi ini untuk meningkatkan postur keamanan mereka:

> Manajer Sertifikat Tingkat Lanjut telah menyederhanakan cara kami dalam mengelola sertifikat di berbagai domain kami, sambil tetap memungkinkan kami untuk memenuhi persyaratan keamanan kami yang ketat. Kemampuan untuk mengelola cipher suite, serta pembaruan otomatis dalam parameter kami, menciptakan lingkungan yang tersedia dan aman.- **Colin Henderson, Kepala Keamanan Informasi, OneTrust**
> 
> Kami telah menggunakan Manajer Sertifikat Tingkat Lanjut untuk kontrol detail atas cipher suite yang digunakan dalam koneksi TLS kami dan guna mengurangi masa pakai sertifikat yang diterbitkan untuk domain kami. Dengan cipher suite yang lebih kuat dan sertifikat dengan masa berlaku yang lebih pendek, kami lebih mampu melindungi koneksi yang dibuat ke situs kami dan data di dalamnya.- **Scott Helme, Pendiri, Report URI**

### Permintaan Penandatanganan Kustom

Beberapa pelanggan ingin memperoleh sertifikat SSL mereka sendiri dari otoritas sertifikat (CA), tetapi ingin Cloudflare membuat dan menyimpan kunci privat terkait. Pelanggan ini sekarang dapat menggunakan Manajer Sertifikat Tingkat Lanjut untuk membuat Permintaan Penandatanganan Sertifikat (CSR) dengan nama organisasi, lokasi, dll. Kemudian, mereka akan membawanya ke CA pilihan mereka, mendapatkan sertifikat, dan meng-uploadnya ke Cloudflare. Cloudflare menangani manajemen kunci dengan serius, dengan perangkat lunak manajemen kunci yang sangat aman dan [kontrol perangkat keras](https://blog.cloudflare.com/introducing-cloudflare-geo-key-manager/). Dengan dukungan CSR, pelanggan bisa mendapatkan sertifikat dari CA pilihan mereka, semua tanpa kunci privat meninggalkan jaringan kami, sehingga mereka tidak perlu khawatir tentang penanganan yang tidak aman.

### Fitur tambahan

Terlepas dari fitur keamanan yang ditawarkan ACM, kami dengan senang hati memberikan solusi manajemen sertifikat yang mudah digunakan dan dikonfigurasikan kepada pelanggan kami. Dengan ACM, pelanggan kini dapat menerbitkan hingga 100 sertifikat edge per zona, yang mencakup puncak zona dan hingga 50 nama host. Ini berarti sertifikat Anda sekarang memiliki dukungan multilevel, sehingga Anda dapat membuat sertifikat untuk nama host tingkat kedua dan ketiga. Selain itu, pelanggan akan dapat memilih metode validasi pilihan mereka (HTTP, TXT, atau Email) dan otoritas sertifikat mereka (Let's Encrypt atau Digicert).

> Dibandingkan dengan CDN kami sebelumnya, menggunakan Cloudflare memberi kami keuntungan seumur hidup dalam membuat dan memelihara sertifikat wildcard. Hanya dengan beberapa baris kode Terraform, Cloudflare melakukan semua pekerjaan untuk Anda.- **Nikita Ponomarev,Insinyur DevOps di Spark Networks**

Untuk mempelajari cara mengonfigurasikan pengaturan ACM, lihat [dokumen pengembang kami](https://developers.cloudflare.com/ssl/advanced-certificate-manager).

### Meningkatkan dari Sertifikat Khusus

Untuk pelanggan kami yang telah menggunakan sertifikat khusus, dengan senang hati kami umumkan bahwa kami akan meningkatkannya ke Manajer Sertifikat Tingkat Lanjut di bulan depan.

Ini akan menjadi migrasi tanpa waktu henti dan Anda akan melihat perubahan Jenis Sertifikat Anda di dasbor dari **Khusus** menjadi **Tingkat Lanjut**.

Selain itu, jika Anda telah menggunakan API kami untuk menerbitkan sertifikat khusus, Anda harus beralih ke [titik akhir API](https://api.cloudflare.com/#certificate-packs-order-advanced-certificate-manager-certificate-pack) penerbitan sertifikat ACM yang baru. Satu perubahan yang perlu diperhatikan adalah bahwa di bidang respons API, "tipe" akan berubah dari "Khusus" menjadi "Tingkat Lanjut".

Pelanggan yang telah membeli Sertifikat Khusus akan dikecualikan dari harga saat ini. Untuk semua pelanggan Gratis, Pro, dan Bisnis lainnya, Manajer Sertifikat Tingkat Lanjut akan dikenakan biaya sebesar $10/bulan per zona. Ini berarti pelanggan akan mendapatkan semua manfaat Sertifikat Khusus, dengan fitur-fitur yang ditawarkan ACM tanpa biaya tambahan.
    
    
    {
      "success": true,
      "errors": [],
      "messages": [],
      "result": {
        "id": "3822ff90-ea29-44df-9e55-21300bb9419b",
        "type": "advanced",
        "hosts": [
          "example.com",
          "*.example.com",
          "www.example.com"
        ],
        "status": "initializing",
        "validation_method": "txt",
        "validity_days": 365,
        "certificate_authority": "digicert",
        "cloudflare_branding": false
      }
    }

Jika Anda adalah pelanggan Perusahaan yang tertarik dengan Manajer Sertifikat Tingkat Lanjut, bicarakan dengan tim akun Anda.

Di halaman ini

Diskusikan Online

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fadvanced-certificate-manager%2F&t=Memperkenalkan%3A%20Manajer%20Sertifikat%20Tingkat%20Lanjut)[](https://x.com/intent/post?text=Memperkenalkan%3A+Manajer+Sertifikat+Tingkat+Lanjut&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fadvanced-certificate-manager%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fadvanced-certificate-manager%2F)[](https://bsky.app/intent/compose?text=Memperkenalkan%3A+Manajer+Sertifikat+Tingkat+Lanjut+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fadvanced-certificate-manager%2F)[](https://mastodonshare.com/?text=Memperkenalkan%3A+Manajer+Sertifikat+Tingkat+Lanjut&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fadvanced-certificate-manager%2F)[](https://www.threads.net/intent/post?text=Memperkenalkan%3A+Manajer+Sertifikat+Tingkat+Lanjut+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fadvanced-certificate-manager%2F)

## Tag terkait

[Advanced Certificate Manager](https://blog.cloudflare.com/id-id/tag/advanced-certificate-manager/)[Berita Produk](https://blog.cloudflare.com/id-id/tag/product-news/)[Keamanan](https://blog.cloudflare.com/id-id/tag/security/)[Security Week](https://blog.cloudflare.com/id-id/tag/security-week/)

Ikuti di Media Sosial

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Berlangganan untuk menerima pemberitahuan postingan baru

Alamat email

Kami tidak akan pernah membagikan alamat email Anda.

Berlangganan

Terima kasih telah berlangganan! Periksa kotak masuk Anda untuk mengonfirmasi.
