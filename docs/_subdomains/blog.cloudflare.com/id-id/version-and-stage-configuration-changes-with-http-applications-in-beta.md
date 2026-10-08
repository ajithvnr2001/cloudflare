---
url: https://blog.cloudflare.com/id-id/version-and-stage-configuration-changes-with-http-applications-in-beta/
title: Perubahan Konfigurasi Versi dan Tahap dengan Aplikasi HTTP dalam Beta | Blog Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:47:20.476153+00:00
---

# Perubahan Konfigurasi Versi dan Tahap dengan Aplikasi HTTP dalam Beta | Blog Cloudflare

> Source: https://blog.cloudflare.com/id-id/version-and-stage-configuration-changes-with-http-applications-in-beta/

[Blog](https://blog.cloudflare.com/id-id/)

[CIO Week](https://blog.cloudflare.com/id-id/tag/cio-week/)

1 TagTampilkan 1 tag

  * Tag Post
  *   * Semua tag
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



[CIO Week](https://blog.cloudflare.com/id-id/tag/cio-week/)

11 Desember 2021

# Perubahan Konfigurasi Versi dan Tahap dengan Aplikasi HTTP dalam Beta

![Garrett Galow](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48YN0EJVE0CEXVNHMJRJ6Q.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Garrett Galow](https://blog.cloudflare.com/id-id/author/garrett/)

8 menit dibaca

SALIN URL

Artikel ini juga tersedia dalam [English](https://blog.cloudflare.com/version-and-stage-configuration-changes-with-http-applications-in-beta/), [日本語](https://blog.cloudflare.com/ja-jp/version-and-stage-configuration-changes-with-http-applications-in-beta/), [简体中文](https://blog.cloudflare.com/zh-cn/version-and-stage-configuration-changes-with-http-applications-in-beta/), dan [ภาษาไทย](https://blog.cloudflare.com/th-th/version-and-stage-configuration-changes-with-http-applications-in-beta/).

![Version and Stage Configuration Changes with HTTP Applications in Beta](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46VR753WR50W3XEB355FSQ.png&w=1200&h=676&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/////f7/8vHz7evt8PDy9fb48vP16ens////////8/Dx7Ofo7+3t9fX28/T17Ovs////////9fHw7eXl8Ovq9vX19vb27+7u////////+fTz8Ojn8+3t+vj4+vr69PPy//////////v69+/v+fT0//7+////+fj4/////////////vn7//7//////////v3+////////////////////////////////////////////////////////////////)

Hari ini, kami mengumumkan beta tertutup Aplikasi HTTP: cara baru untuk menguji dan memberlakukan perubahan pada lalu lintas HTTP Anda dengan aman. Aplikasi HTTP memperkenalkan penetapan versi konfigurasi dan kemampuan kontrol saat perubahan diluncurkan pada lalu lintas HTTP di jaringan edge global Cloudflare. Pelanggan perusahaan yang menginginkan kontrol lebih besar harus menghubungi Manajer Customer Success mereka untuk mendapatkan akses.

### **Masalah yang Dijumpai saat Mengelola Konfigurasi**

Sejak awal Cloudflare didirikan, manajemen situs web dan aplikasi web telah dilakukan lewat hal yang kami sebut sebagai Zona, yang berasal dari konsep [Zona DNS](https://www.cloudflare.com/learning/dns/glossary/dns-zone/). Meski telah berfungsi baik selama bertahun-tahun bagi pelanggan, model ini menghadirkan kesulitan dalam mengelola konfigurasi edge, yaitu:

  1. Pelanggan perlu mengerahkan upaya manual untuk melakukan setup lingkungan staging.
  2. Risiko penyimpangan dalam konfigurasi antara produksi dan staging.



Dalam pengembangan perangkat lunak, Anda perlu menguji perubahan dalam lingkungan yang aman untuk memvalidasinya sebelum diproduksi atau memengaruhi lalu lintas langsung. Dalam banyak siklus pengembangan perangkat lunak umum, ini berarti memberlakukan perubahan pada lingkungan staging atau praproduksi untuk pengujian dan validasi. Cara paling umum yang dilakukan pelanggan dalam Cloudflare saat ini adalah menggunakan dua Zona yang ditandai dengan nama host zona tersebut, misalnya: satu untuk staging bernama _staging.example.com_ dan satu untuk produksi bernama _example.com_. Ini menyelesaikan masalah inti, sebab mereka memberikan insulasi perubahan. Kesalahan dalam zona staging tidak akan memengaruhi lalu lintas produksi.

Namun, agar dapat diterapkan dalam produksi, perubahan yang berhasil diverifikasi dalam staging harus disalin secara manual oleh pelanggan — atau membuat automasi melalui [Penyedia Terraform](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs) Cloudflare. Bagi banyak orang, ini mengikuti proses 'perubahan permintaan' manual saat tiket dicatat dengan perubahan yang akan dibuat. Kemudian, seseorang (kerap kali orang yang berbeda) mengambil tiket dan harus secara akurat menggandakan perubahan yang sama berdasarkan instruksi manual. Rentan terjadi kesalahan dalam proses ini; dan kesalahan dalam proses ini dapat mengakibatkan penghentian, tergantung pada perubahannya. Selain itu, penyimpangan konfigurasi antara konfigurasi staging dan produksi dapat menghasilkan kerumitan lebih lanjut.

Kami ingin memberikan keamanan dan keandalan bagi pelanggan dalam mengelola layanan mereka pada Cloudflare. Untuk mengatasi masalah yang dijelaskan sebelumnya, kami mengumumkan Aplikasi HTTP beserta Aturan Perutean.

### **Aplikasi HTTP**

Aplikasi HTTP adalah cara untuk mengelola konfigurasi edge dengan kasus penggunaan, bukan dengan nama host. Setiap Aplikasi HTTP memiliki tujuan, baik menangani konfigurasi situs web pemasaran Anda maupun aplikasi internal. Setiap Aplikasi HTTP terdiri dari beberapa versi konfigurasi, di mana setiap versi mewakili cuplikan pengaturan untuk mengelola lalu lintas — page rule, aturan firewall, pengaturan cache, dll. Setiap versi konfigurasi dalam Aplikasi HTTP terpisah dari satu sama lain, tetapi apabila versi baru dibuat, versi ini dimulai sebagai salinan versi sebelumnya.

### **Aturan Perutean**

Tidak seperti zona, setiap versi Aplikasi HTTP tidak tergantung pada nama host tertentu. Oleh karena itu, jika versi tidak terkait dengan nama host, seperti zona, bagaimana Anda dapat menentukan versi Aplikasi HTTP yang akan memengaruhi rangkaian lalu lintas tertentu? Jawabannya adalah Aturan Perutean. Dengan Aturan Perutean, Anda dapat menentukan versi Aplikasi HTTP yang diterapkan pada lalu lintas tertentu, atau nama host. Aturan Perutean didukung oleh [Kumpulan Aturan Teknis](https://developers.cloudflare.com/ruleset-engine/) Cloudflare dan mengandalkan penggunaan aturan "jika demikian" kondisional untuk memetakan nama host yang dikontrol dalam akun Cloudflare Anda ke versi konfigurasi tertentu. Sebagai contoh, jika nama host permintaan cocok dengan '[www.example.com](http://www.example.com)', terapkan versi 2 Aplikasi HTTP Pemasaran saya. Saat aturan dilaksanakan dalam edge kami, alih-alih menerapkan konfigurasi zona reguler [www.example.com](http://www.example.com/), edge akan menggunakan konfigurasi yang ditetapkan dalam versi 2 Aplikasi HTTP.

Aturan Perutean mendukung dua jenis aturan — aturan staging dan aturan produksi. Keduanya menggunakan daftar nama host, sebagaimana dijelaskan, tetapi saat membuat aturan staging, kami menambahkan filter agar aturan hanya akan dijalankan saat lalu lintas dikirimkan ke IP khusus pada edge kami. Ini artinya Anda dapat menguji perubahan secara aman dengan mengirimkan lalu lintas ke [www.example.com](http://www.example.com/) pada IP staging tanpa berdampak pada pelanggan. Lebih baik lagi, setelah Anda memvalidasi perubahan dengan pembuatan aturan perutean produksi, konfigurasi yang sama persis akan diterapkan dalam produksi untuk semua pelanggan Anda.

Cukup sudah penjelasannya — mari melihatnya langsung!

### **Menggunakan Aplikasi HTTP untuk menguji dan memberlakukan perubahan dengan aman**

Untuk panduan ini, saya akan berperan sebagai pelanggan lama. Saya memiliki zona yang melayani pelanggan dan ingin membuat beberapa perubahan untuk mengganti aturan agar dapat menulis ulang lokasi aset saya. Tetapi, saya tidak terlalu menguasai regex dan situs semua pelanggan saya akan rusak jika terjadi kesalahan! Daripada membuat perubahan langsung dalam zona, kami akan menggunakan Aplikasi HTTP dan Aturan Perutean untuk membuat, menguji, dan meluncurkan perubahan.

Pertama-tama, saya login ke Dasbor Cloudflare. Setelah memilih akun, saya melihat Aplikasi HTTP yang tersedia pada bilah samping. Selepas memilihnya, saya dapat memilih untuk membuat Aplikasi HTTP pertama saya.

Dasbor Cloudflare menunjukkan halaman kondisi kosong untuk Aplikasi HTTP

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![The Cloudflare Dashboard showing the empty state page for HTTP Applications](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW458EKZ2S3MRA5PVPCQ9GTS.png&w=715&h=508&f=webp&fit=cover&position=center)

Untuk membuat Aplikasi HTTP pertama saya, saya perlu menamai dan memilih zona yang ada sebelumnya, dalam hal ini example.com. Cloudflare akan menggunakan zona itu untuk mengawali konfigurasi versi pertama Aplikasi HTTP. Dengan menyalinnya pada pengaturan yang ada dari zona, saya memiliki salinan aman untuk dikerjakan dan tidak perlu menyusun ulang konfigurasi secara manual.

Layar "Create an Application” (Buat Aplikasi) yang menunjukkan bahwa Aplikasi HTTP akan dibuat dengan nama "Example application (Aplikasi Contoh)" dan dimulai dari example.com

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![The “Create an Application” screen showing that an HTTP Application will be created named “Example Application” and initialized from example.com.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46SZ1YT1QX8DK9DE6SV6RM.png&w=715&h=597&f=webp&fit=cover&position=center)

Setelah memilih "Create” (Buat), Aplikasi HTTP pertama saya sudah jadi! Sekarang, versi pertama sedang dibuat. Di balik layar, Cloudflare akan mengambil konfigurasi example.com yang ada dan menyalinnya ke Versi 1 Aplikasi HTTP ini. Setelah berhasil disalin, saya dapat mulai mengedit konfigurasi ini.

Daftar versi Aplikasi Contoh, yang menunjukkan Versi 1 sedang dibuat.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![The Version list of the Example Application, showing Version 1 being created.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46S9XE345HJ7DW2D5D1SK9.png&w=715&h=509&f=webp&fit=cover&position=center)

Saya dapat mengedit versi ini seperti yang saya lakukan dalam zona apa saja. Namun, terdapat dua perbedaan penting. Pertama: perubahan yang saya lakukan sekarang tidak akan memengaruhi lalu lintas langsung pada edge Cloudflare, sebab kami belum membuat aturan perutean untuk mengirimkan lalu lintas ke konfigurasi versi ini. Kedua: kami tidak mengizinkan segala hal yang terhubung dengan zona untuk dikontrol melalui Aplikasi HTTP, yaitu: catatan DNS, Sertifikat SSL, Spectrum, atau Load Balancing.

Aturan transformasi Versi 1 menunjukkan bahwa tidak ada aturan yang dibuat.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Transform rules of Version 1 showing a new rule named “Rewrite Assets” has been created.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4650766PWVQKE2S1CH0ZPT.png&w=715&h=508&f=webp&fit=cover&position=center)

Dalam bagian Aturan pada [Aturan Transformasi](https://blog.cloudflare.com/introducing-transform-rules-with-url-rewriting-at-the-edge/), saya membuat aturan baru untuk menulis ulang jalur aset ke lokasi yang benar. Untuk semua permintaan ke example.com/assets/*, kami akan menulis ulang jalur menjadi example.com/internal/files/assets/*.

Membuat aturan transformasi untuk Versi 1 bernama "Rewrite Assets (Tulis Ulang Aset)"

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Creating a transform rule for Version 1 named “Rewrite Assets”. This rule replaces the path for requests starting with “/assets/” with “internal/files/assets/”.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW456C7EFJVX26E4WG8HKEME.png&w=715&h=692&f=webp&fit=cover&position=center)

. Aturan ini menggantikan jalur permintaan yang dimulai dengan “/assets/*” dengan “internal/files/assets/*”.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Transform rules of Version 1 showing a new rule named “Rewrite Assets” has been created.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4650766PWVQKE2S1CH0ZPT.png&w=715&h=508&f=webp&fit=cover&position=center)

Aturan transformasi Versi 1 yang menunjukkan aturan baru bernama "Rewrite Assets (Tulis Ulang Aset)" telah dibuat.

Pada saat ini, saya telah membuat perubahan, dan sekarang ingin mengujinya. Untuk melakukannya, saya dapat keluar dari bagian pengeditan versi dan menuju Aturan Perutean untuk Aplikasi HTTP ini. Di sini, saya dapat membuat aturan yang akan mengizinkan lalu lintas yang ada untuk dirutekan melalui konfigurasi versi ini.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![An empty list of Routing Rules for the Example Application.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47YCJHBA4CE79D6EBGWXBB.png&w=715&h=509&f=webp&fit=cover&position=center)

Daftar kosong dari Aturan Perutean untuk Aplikasi Contoh.

Saya akan membuat aturan staging, sebab saya ingin menjadi satu-satunya yang menguji perubahan ini tanpa berdampak pada pelanggan. Perhatikan, saat membuat aturan staging, IP yang dapat digunakan untuk menguji versi ini akan ditampilkan pada layar pembuatan aturan.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Creating a staging Routing Rule that will match when requests match example.com and the edge IP is 192.168.1.1 or 192.168.2.2 and apply the configuration of Version 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48EYHVEC962GBGCXS4G320.png&w=715&h=555&f=webp&fit=cover&position=center)

Membuat Aturan Perutean staging yang akan cocok apabila permintaan cocok dengan example.com dan IP edge adalah 192.168.1.1 atau 192.168.2.2 dan menerapkan konfigurasi Versi 1

Setelah membuat aturan, saya dapat mengonfigurasikan komputer untuk mengirimkan permintaan ke IP tersebut untuk example.com. Rackspace memiliki [panduan lengkap](https://docs.rackspace.com/support/how-to/modify-your-hosts-file/) mengenai cara mengubah file host mesin lokal Anda untuk melakukannya. Sekarang, saat saya mengunjungi example.com, aturan transformasi baru dijalankan, tetapi tidak ada yang berubah bagi orang lain yang mengunjungi situs tersebut.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Routing Rules for the Example Application showing one rule for staging has been created.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW483QYWQGJSYASW3SB1J6MZ.png&w=715&h=508&f=webp&fit=cover&position=center)

Aturan Perutean untuk Aplikasi Contoh yang menunjukkan satu aturan staging telah dibuat.

Setelah saya yakin perubahan berfungsi, saya dapat membuat Aturan Perutean produksi yang akan menerapkan perubahan ini bagi semua lalu lintas pada example.com — dan semuanya selesai!

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Routing Rule creation screen showing the creation of a production rule that will apply Version 1 when requests match example.com](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW483PNM5H34VA0H6R114BEG.png&w=715&h=555&f=webp&fit=cover&position=center)

Layar pembuatan Aturan Perutean yang menunjukkan pembuatan aturan produksi yang akan menerapkan Versi 1 apabila permintaan cocok dengan example.com

Setelah diperbarui, jalur aset untuk situs saya akan ditulis ulang untuk semua permintaan ke _example.com_.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Routing Rules for the Example Application showing both a staging and production rule for Version 1.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4516H63F0TYZDA9GN20TKW.png&w=715&h=508&f=webp&fit=cover&position=center)

Aturan Perutean untuk Aplikasi Contoh yang menunjukkan aturan staging dan produksi untuk Versi 1.

Apa yang terjadi selanjutnya? Apabila saya siap membuat rangkaian perubahan lainnya, saya dapat membuka Aplikasi HTTP dan menggandakan Versi 1 untuk membuat Versi 2. Awalnya, Versi 2 akan sama persis dengan konfigurasi Versi 1, tetapi karena tidak ada Aturan Perutean yang cocok, ini tidak akan diterapkan ke lalu lintas.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![The list of versions for the Example Application showing Version 1 being applied to staging and production, and Version 2 ready to edit, but not being used anywhere.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44FBHN5DK9W8Q5HNG6A450.png&w=715&h=509&f=webp&fit=cover&position=center)

Daftar versi Aplikasi Contoh yang menunjukkan Versi 1 diterapkan ke staging dan produksi, dan Versi 2 siap diedit, tetapi tidak digunakan di mana pun.

Sekarang saya dapat mengedit Versi 2 dengan aman seperti yang saya lakukan sebelumnya dengan Versi 1. Kali ini, saya ingin mengubah aturan firewall agar saya dapat mencegah lalu lintas yang mungkin berbahaya agar tidak mengakses situs saya. Mengubah Versi 2 tidak akan mengubah lalu lintas di edge hingga saya memperbarui Aturan Perutean staging saya untuk menggunakan Versi 2. Ini memungkinkan saya membuat perubahan dengan penuh keyakinan, kemudian mengujinya dengan aman.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![The list of routing rules for the Example Application showing Version 2 being used for staging, while Version 1 is still used in production.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46KH032ZQ7EY8QQ0WJZR34.png&w=715&h=508&f=webp&fit=cover&position=center)

Daftar aturan perutean untuk Aplikasi Contoh menunjukkan Versi 2 yang digunakan untuk staging, sedangkan Versi 1 masih digunakan dalam produksi.

Setelah memvalidasi rangkaian perubahan ini, saya dapat mendorong Versi 2 ke semua lalu lintas dengan memperbarui Aturan Perutean produksi untuk menggunakan Versi 2. Proses yang sama dapat dilakukan untuk setiap rangkaian perubahan berikutnya yang ingin saya buat.

### **Aplikasi HTTP Kini Tersedia dalam Beta Tertutup**

Dengan kekuatan Aplikasi HTTP dan Aturan Perutean, pelanggan kini dapat lebih mengontrol cara dan waktu perubahan konfigurasi dibuat. Ini mengurangi kekhawatiran membuat perubahan buruk yang mungkin merusak situs Anda. Kapabilitas ini tersedia dalam beta tertutup untuk pelanggan perusahaan, tetapi jika Anda tertarik, hubungi tim akun Cloudflare Anda untuk mempelajari cara mendapatkan akses!

Di halaman ini

Diskusikan Online

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fversion-and-stage-configuration-changes-with-http-applications-in-beta%2F&t=Perubahan%20Konfigurasi%20Versi%20dan%20Tahap%20dengan%20Aplikasi%20HTTP%20dalam%20Beta)[](https://x.com/intent/post?text=Perubahan+Konfigurasi+Versi+dan+Tahap+dengan+Aplikasi+HTTP+dalam+Beta&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fversion-and-stage-configuration-changes-with-http-applications-in-beta%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fversion-and-stage-configuration-changes-with-http-applications-in-beta%2F)[](https://bsky.app/intent/compose?text=Perubahan+Konfigurasi+Versi+dan+Tahap+dengan+Aplikasi+HTTP+dalam+Beta+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fversion-and-stage-configuration-changes-with-http-applications-in-beta%2F)[](https://mastodonshare.com/?text=Perubahan+Konfigurasi+Versi+dan+Tahap+dengan+Aplikasi+HTTP+dalam+Beta&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fversion-and-stage-configuration-changes-with-http-applications-in-beta%2F)[](https://www.threads.net/intent/post?text=Perubahan+Konfigurasi+Versi+dan+Tahap+dengan+Aplikasi+HTTP+dalam+Beta+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fversion-and-stage-configuration-changes-with-http-applications-in-beta%2F)

## Tag terkait

[CIO Week](https://blog.cloudflare.com/id-id/tag/cio-week/)

Ikuti di Media Sosial

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Berlangganan untuk menerima pemberitahuan postingan baru

Alamat email

Kami tidak akan pernah membagikan alamat email Anda.

Berlangganan

Terima kasih telah berlangganan! Periksa kotak masuk Anda untuk mengonfirmasi.
