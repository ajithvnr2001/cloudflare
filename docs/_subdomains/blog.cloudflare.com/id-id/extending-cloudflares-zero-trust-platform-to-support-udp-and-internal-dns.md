---
url: https://blog.cloudflare.com/id-id/extending-cloudflares-zero-trust-platform-to-support-udp-and-internal-dns/
title: Memperluas platform Zero Trust Cloudflare untuk mendukung UDP dan DNS Internal | Blog Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:46:13.258007+00:00
---

# Memperluas platform Zero Trust Cloudflare untuk mendukung UDP dan DNS Internal | Blog Cloudflare

> Source: https://blog.cloudflare.com/id-id/extending-cloudflares-zero-trust-platform-to-support-udp-and-internal-dns/

[Blog](https://blog.cloudflare.com/id-id/)

[Berita Produk](https://blog.cloudflare.com/id-id/tag/product-news/)[CIO Week](https://blog.cloudflare.com/id-id/tag/cio-week/)[Cloudflare One](https://blog.cloudflare.com/id-id/tag/cloudflare-one/)+3Tampilkan 3 tag lainnya

6 TagTampilkan 6 tag

  * Tag Post
  * [Berita Produk](https://blog.cloudflare.com/id-id/tag/product-news/)[Cloudflare Tunnel](https://blog.cloudflare.com/id-id/tag/cloudflare-tunnel/)[Zero Trust](https://blog.cloudflare.com/id-id/tag/zero-trust/)
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



[Cloudflare Tunnel](https://blog.cloudflare.com/id-id/tag/cloudflare-tunnel/)[UDP](https://blog.cloudflare.com/id-id/tag/udp/)[Zero Trust](https://blog.cloudflare.com/id-id/tag/zero-trust/)

[Berita Produk](https://blog.cloudflare.com/id-id/tag/product-news/)[CIO Week](https://blog.cloudflare.com/id-id/tag/cio-week/)[Cloudflare One](https://blog.cloudflare.com/id-id/tag/cloudflare-one/)[Cloudflare Tunnel](https://blog.cloudflare.com/id-id/tag/cloudflare-tunnel/)[UDP](https://blog.cloudflare.com/id-id/tag/udp/)[Zero Trust](https://blog.cloudflare.com/id-id/tag/zero-trust/)

8 Desember 2021

# Memperluas platform Zero Trust Cloudflare untuk mendukung UDP dan DNS Internal

![Abe Carryl](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46JJ6YPQY3M4A69P72QXE8.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Abe Carryl](https://blog.cloudflare.com/id-id/author/abe/)

8 menit dibaca

SALIN URL

Artikel ini juga tersedia dalam [English](https://blog.cloudflare.com/extending-cloudflares-zero-trust-platform-to-support-udp-and-internal-dns/), [日本語](https://blog.cloudflare.com/ja-jp/extending-cloudflares-zero-trust-platform-to-support-udp-and-internal-dns/), [简体中文](https://blog.cloudflare.com/zh-cn/extending-cloudflares-zero-trust-platform-to-support-udp-and-internal-dns/), dan [ภาษาไทย](https://blog.cloudflare.com/th-th/extending-cloudflares-zero-trust-platform-to-support-udp-and-internal-dns/).

![Extending Cloudflare’s Zero Trust platform to support UDP and Internal DNS](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW458X27BH42R38GENAX3HNY.png&w=1801&h=1013&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////////9e3p693R7NvN8uTa9e3q8/Dz////////7+Xd4cq54MSu6dPC7+Xd8fDv///////+697S2Lee1qyL4MKp697R8fHs////////7ODS17WZ1KeC37+k7ODR8/bu////////9Ovg4Mey3r2j6NG89Ovf+f33/////////vv07+PX7t7P9+vf/vv0/////////////////Pny/Pjw///7///////////////////////8///8////////////)

Pada akhir tahun 2020, Cloudflare memberdayakan organisasi untuk mulai [membangun jaringan pribadi](https://blog.cloudflare.com/build-your-own-private-network-on-cloudflare/) di atas jaringan kami. Dengan menggunakan Cloudflare Tunnel di sisi server, dan Cloudflare WARP di sisi klien, kebutuhan akan VPN lama dihilangkan. Hari ini, ribuan organisasi telah melakukan proses ini bersama kami — mencabut konsentrator VPN lama, firewall internal, dan penyeimbang beban mereka. Mereka tidak perlu lagi memelihara semua perangkat keras lama ini; mereka telah meningkatkan kecepatan pengguna akhir secara drastis; dan mereka dapat mempertahankan aturan Zero Trust di seluruh organisasi.

Kami memulai dengan TCP yang sangat kuat karena dapat menangani berbagai kasus penggunaan yang penting. Namun, untuk benar-benar mengganti VPN, Anda juga harus bisa mencakup UDP. Mulai hari ini, kami dengan senang hati menyediakan akses awal ke UDP di platform Zero Trust Cloudflare. Dan yang lebih baik lagi: karena mendukung UDP, kami dapat menawarkan DNS Internal — sehingga tidak perlu memigrasikan ribuan nama host pribadi secara manual untuk mengganti aturan DNS. Anda dapat memulai Cloudflare for Teams gratis hari ini dengan mendaftar [di sini](https://dash.cloudflare.com/sign-up/teams); dan jika Anda ingin bergabung dalam daftar tunggu untuk mendapatkan akses awal ke UDP dan DNS Internal, silakan kunjungi [di sini](https://cloudflare.com/zero-trust/lp/private-dns-waitlist).

## **Topologi jaringan pribadi di Cloudflare**

Membangun jaringan pribadi memiliki dua komponen primer: sisi infrastruktur dan sisi klien.

Sisi infrastruktur persamaan ini didukung oleh Cloudflare Tunnel, yang hanya menghubungkan infrastruktur Anda (baik aplikasi tunggal, banyak aplikasi, maupun seluruh segmen jaringan) ke Cloudflare. Ha ini terjadi dengan menjalankan daemon baris perintah sederhana di lingkungan Anda untuk membuat beberapa tautan aman, hanya keluar, dan load balancing ke Cloudflare. Sederhananya, Tunnel adalah yang menghubungkan jaringan Anda ke Cloudflare.

Di sisi lain dari persamaan ini, kami ingin pengguna akhir Anda dapat dengan mudah terhubung ke Cloudflare dan, yang lebih penting, jaringan Anda. Koneksi ini ditangani oleh klien perangkat kami yang tangguh, [Cloudflare WARP](https://blog.cloudflare.com/warp-for-desktop/). Klien dapat diluncurkan ke seluruh organisasi Anda hanya dalam beberapa menit menggunakan alat MDM internal Anda, dan ini membuat koneksi berbasis WireGuard yang aman dari perangkat pengguna Anda ke jaringan Cloudflare.

Sekarang setelah infrastruktur dan pengguna Anda terhubung ke Cloudflare, menjadi mudah untuk memberi tag aplikasi dan layer Anda pada kontrol keamanan Zero Trust untuk memverifikasi identitas dan aturan yang berpusat pada perangkat untuk setiap permintaan di jaringan Anda.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-860 Embedded Image - jQyQ7J](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45HM63YMWAAD3TWM6XH83F.png&w=715&h=340&f=webp&fit=cover&position=center)

Sampai sekarang, hanya TCP yang didukung.

## **Memperluas Zero Trust Cloudflare untuk mendukung UDP**

Selama setahun terakhir, dengan makin banyak pengguna yang mengadopsi platform Zero Trust Cloudflare, kami telah mengumpulkan data seputar semua kasus penggunaan yang membuat VPN tetap terhubung. Dari semua itu, kebutuhan yang paling umum adalah dukungan menyeluruh untuk traffic berbasis UDP. Protokol modern seperti QUIC memanfaatkan arsitektur ringan UDP — dan di Cloudflare, kami yakin ini adalah bagian dari misi kami untuk memajukan standar baru ini guna membantu membangun Internet yang lebih baik.

Hari ini, kami dengan senang hati membuka daftar tunggu resmi bagi mereka yang menginginkan akses awal ke Cloudflare for Teams dengan dukungan UDP.

### **Apa itu UDP dan mengapa penting?**

UDP adalah komponen penting dari Internet. Tanpa itu, banyak aplikasi akan menjadi sangat tidak memadai untuk penggunaan modern. Aplikasi yang bergantung pada komunikasi yang hampir secara waktu riil seperti streaming video atau layanan VoIP adalah contoh utama mengapa kita membutuhkan UDP dan perannya untuk Internet. Intinya, TCP dan UDP mencapai hasil yang sama — hanya melalui cara yang sangat berbeda. Masing-masing memiliki kelebihan dan kekurangan yang unik, yang selalu dirasakan oleh aplikasi yang memanfaatkannya.

Berikut adalah contoh singkat tentang cara kerja keduanya, jika Anda mengajukan pertanyaan kepada seseorang, sebagai metafora. TCP akan terlihat cukup familier: Anda biasanya akan menyapa, menunggu mereka menyapa balik, menanyakan kabar mereka, menunggu tanggapan mereka, lalu menanyakan apa yang Anda inginkan.

Di sisi lain, UDP sama halnya seperti berjalan menuju seseorang dan menanyakan apa yang Anda inginkan tanpa memastikan apakah mereka mendengarkan. Dengan pendekatan ini, beberapa pertanyaan Anda mungkin terlewatkan, tetapi tidak apa-apa selama Anda mendapatkan jawaban.

Seperti percakapan di atas, dengan UDP banyak aplikasi yang sebenarnya tidak peduli jika ada data yang hilang; streaming video atau server game adalah contoh yang tepat di sini. Jika Anda kehilangan paket saat transit saat streaming, Anda tidak ingin seluruh streaming terputus hingga paket ini diterima — Anda lebih baik membuang paket dan melanjutkan. Alasan lain pengembang aplikasi dapat menggunakan UDP adalah karena mereka lebih suka mengembangkan kontrol mereka sendiri di sekitar koneksi, transmisi, dan kontrol kualitas daripada menggunakan yang standar TCP.

Untuk Cloudflare, dukungan ujung ke ujung untuk traffic berbasis UDP akan membuka sejumlah kasus penggunaan baru. Berikut adalah beberapa hal yang menurut kami cukup menarik bagi Anda.

### **Resolver DNS Internal**

Sebagian besar jaringan perusahaan memerlukan resolver DNS internal untuk menyebarkan akses ke sumber daya yang tersedia melalui Intranet mereka. Intranet Anda memerlukan resolver DNS internal untuk banyak alasan yang sama seperti Internet membutuhkan resolver DNS publik. Singkatnya, manusia pandai dalam banyak hal, tetapi mengingat deretan angka yang panjang (dalam hal ini alamat IP) bukanlah salah satunya. Resolver DNS publik dan internal dirancang untuk memecahkan masalah ini (dan [banyak lagi](https://www.cloudflare.com/learning/dns/what-is-dns/)) bagi kami.

Di dunia korporat, tidak ada gunanya meminta pengguna internal untuk menavigasi, katakanlah, 192.168.0.1 untuk hanya mencapai Sharepoint atau OneDrive. Alih-alih, jauh lebih mudah untuk membuat entri DNS untuk setiap sumber daya dan membiarkan resolver internal Anda menangani semua pemetaan untuk pengguna Anda karena ini adalah sesuatu yang sebenarnya cukup dikuasai manusia.

Di latar belakang, permintaan DNS umumnya terdiri dari satu permintaan UDP dari klien. Server kemudian dapat mengembalikan satu balasan ke klien. Karena permintaan DNS tidak terlalu besar, mereka sering dapat dikirim dan diterima dalam satu paket. Hal ini menjadikan dukungan untuk UDP di seluruh platform Zero Trust kami sebagai pendukung utama untuk menarik steker pada VPN Anda.

### **Aplikasi Thick Client**

Kasus penggunaan umum lainnya untuk UDP adalah aplikasi thick client. Salah satu manfaat dari UDP yang telah kita bahas sejauh ini adalah bahwa itu adalah protokol lean. Ini ramping karena [handshake tiga arah](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/) TCP dan ukuran keandalan lainnya telah dihilangkan oleh desain. Dalam banyak kasus, pengembang aplikasi masih menginginkan kontrol keandalan ini, tetapi sangat akrab dengan aplikasi mereka dan mengetahui bahwa kontrol ini dapat ditangani dengan lebih baik dengan menyesuaikannya dengan aplikasi mereka. Aplikasi thick client ini sering melakukan fungsi bisnis penting dan harus didukung ujung ke ujung untuk bermigrasi. Sebagai contoh, versi lama Outlook dapat diterapkan melalui thick client di mana sebagian besar operasi dilakukan oleh mesin lokal, dan hanya interaksi sinkronisasi dengan server Exchange yang terjadi melalui UDP.

Sekali lagi, dengan dukungan UDP pada platform Zero Trust kami, tidak ada lagi alasan bagi jenis aplikasi ini untuk tetap berada di VPN lama Anda.

### **Lainnya**

Sebagian besar lalu lintas Internet dunia diangkut melalui UDP. Sering kali, orang menyamakan aplikasi peka waktu dengan UDP, di mana kadang-kadang menjatuhkan paket akan lebih baik daripada menunggu — tetapi ada sejumlah kasus penggunaan lain, dan kami senang dapat memberikan dukungan menyeluruh.

## **Bagaimana saya dapat memulainya hari ini?**

Anda sudah dapat mulai membangun jaringan pribadi di Cloudflare dengan tutorial dan panduan kami di dokumentasi pengembang kami. Di bawah ini adalah jalur kritisnya. Dan jika Anda sudah menjadi pelanggan, dan Anda tertarik untuk bergabung dengan daftar tunggu untuk akses UDP dan DNS Internal, silakan lewati ke akhir postingan ini!

### **Menghubungkan jaringan Anda ke Cloudflare**

Pertama, Anda perlu [menginstal cloudflared](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation) di jaringan Anda dan mengautentikasinya dengan perintah di bawah ini:

Selanjutnya, Anda akan membuat tunnel dengan nama yang mudah digunakan untuk mengidentifikasi jaringan atau lingkungan Anda.
    
    
    cloudflared tunnel login

Terakhir, Anda ingin mengonfigurasi tunnel Anda dengan rentang IP/CIDR dari jaringan pribadi Anda. Dengan melakukan ini, Anda membuat agen WARP Cloudflare menyadari bahwa setiap permintaan ke rentang IP ini perlu dirutekan ke tunnel baru kami.
    
    
    cloudflared tunnel create acme-network

Kemudian, yang perlu Anda lakukan hanyalah menjalankan tunnel Anda!
    
    
    cloudflared tunnel route ip add 192.168.0.1/32

### **Menghubungkan pengguna ke jaringan Anda**

Untuk menghubungkan pengguna pertama Anda, mulailah dengan mengunduh agen WARP Cloudflare di perangkat yang akan mereka hubungkan, lalu ikuti langkah-langkah di penginstal kami.

Selanjutnya, Anda akan mengunjungi [Dasbor Tim](https://dash.teams.cloudflare.com/) dan menentukan siapa yang diizinkan mengakses jaringan kami dengan membuat kebijakan pendaftaran. Kebijakan ini dapat dibuat di Pengaturan > Perangkat > Pendaftaran Perangkat. Pada contoh di bawah, Anda dapat melihat bahwa kami mengharuskan pengguna berada di Kanada dan memiliki alamat email yang diakhiri dengan @cloudflare.com.

Setelah Anda membuat kebijakan ini, Anda dapat mendaftarkan perangkat pertama Anda dengan mengeklik ikon desktop WARP di komputer Anda dan membuka Preferensi > Akun > Login dengan Tim.

Terakhir, kami akan menghapus rentang IP yang kami tambahkan ke Tunnel kami dari daftar Kecualikan di Pengaturan > Jaringan > Split Tunnels. Ini akan memastikan traffic ini, pada kenyataannya, dialihkan ke Cloudflare dan kemudian dikirim ke Tunnel jaringan pribadi kami sebagaimana dimaksud.

Selain tutorial di atas, kami juga memiliki panduan dalam produk di Dasbor Teams yang menjelaskan lebih detail tentang setiap langkah dan memberikan validasi di sepanjang prosesnya.

Untuk membuat Tunnel pertama Anda, buka [Akses > Tunnel](https://dash.teams.cloudflare.com/access/tunnels).

Untuk mendaftarkan perangkat pertama Anda ke WARP, buka [Tim Saya > Perangkat](https://dash.teams.cloudflare.com/team/devices).

## **Apa Selanjutnya?**

Kami sangat bersemangat untuk merilis [daftar tunggu](https://cloudflare.com/zero-trust/lp/private-dns-waitlist) kami hari ini dan bahkan lebih bersemangat untuk meluncurkan fitur ini dalam beberapa minggu mendatang. Kami baru saja memulai tunnel jaringan pribadi dan berencana untuk terus menambahkan lebih banyak dukungan untuk aturan akses Zero Trust untuk setiap permintaan ke setiap nama host DNS internal setelah peluncuran. Kami juga sedang mengerjakan sejumlah upaya untuk mengukur kinerja dan untuk memastikan kami tetap menjadi platform Zero Trust tercepat — menjadikan penggunaan kami sebagai kesenangan bagi pengguna Anda, dibandingkan dengan kesulitan menggunakan VPN lama.

Di halaman ini

Diskusikan Online

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fextending-cloudflares-zero-trust-platform-to-support-udp-and-internal-dns%2F&t=Memperluas%20platform%20Zero%20Trust%20Cloudflare%20untuk%20mendukung%20UDP%20dan%20DNS%20Internal)[](https://x.com/intent/post?text=Memperluas+platform+Zero+Trust+Cloudflare+untuk+mendukung+UDP+dan+DNS+Internal&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fextending-cloudflares-zero-trust-platform-to-support-udp-and-internal-dns%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fextending-cloudflares-zero-trust-platform-to-support-udp-and-internal-dns%2F)[](https://bsky.app/intent/compose?text=Memperluas+platform+Zero+Trust+Cloudflare+untuk+mendukung+UDP+dan+DNS+Internal+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fextending-cloudflares-zero-trust-platform-to-support-udp-and-internal-dns%2F)[](https://mastodonshare.com/?text=Memperluas+platform+Zero+Trust+Cloudflare+untuk+mendukung+UDP+dan+DNS+Internal&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fextending-cloudflares-zero-trust-platform-to-support-udp-and-internal-dns%2F)[](https://www.threads.net/intent/post?text=Memperluas+platform+Zero+Trust+Cloudflare+untuk+mendukung+UDP+dan+DNS+Internal+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fextending-cloudflares-zero-trust-platform-to-support-udp-and-internal-dns%2F)

## Tag terkait

[Berita Produk](https://blog.cloudflare.com/id-id/tag/product-news/)[CIO Week](https://blog.cloudflare.com/id-id/tag/cio-week/)[Cloudflare One](https://blog.cloudflare.com/id-id/tag/cloudflare-one/)[Cloudflare Tunnel](https://blog.cloudflare.com/id-id/tag/cloudflare-tunnel/)[UDP](https://blog.cloudflare.com/id-id/tag/udp/)[Zero Trust](https://blog.cloudflare.com/id-id/tag/zero-trust/)

Ikuti di Media Sosial

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Berlangganan untuk menerima pemberitahuan postingan baru

Alamat email

Kami tidak akan pernah membagikan alamat email Anda.

Berlangganan

Terima kasih telah berlangganan! Periksa kotak masuk Anda untuk mengonfirmasi.
