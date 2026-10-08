---
url: https://blog.cloudflare.com/id-id/zero-trust-private-networking-rules/
title: Aturan Jejaring Pribadi Zero Trust | Blog Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:47:22.403384+00:00
---

# Aturan Jejaring Pribadi Zero Trust | Blog Cloudflare

> Source: https://blog.cloudflare.com/id-id/zero-trust-private-networking-rules/

[Blog](https://blog.cloudflare.com/id-id/)

[CIO Week](https://blog.cloudflare.com/id-id/tag/cio-week/)[Zero Trust](https://blog.cloudflare.com/id-id/tag/zero-trust/)

2 TagTampilkan 2 tag

  * Tag Post
  * [Zero Trust](https://blog.cloudflare.com/id-id/tag/zero-trust/)
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



[CIO Week](https://blog.cloudflare.com/id-id/tag/cio-week/)[Zero Trust](https://blog.cloudflare.com/id-id/tag/zero-trust/)

8 Desember 2021

# Aturan Jejaring Pribadi Zero Trust

![Kenny Johnson](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW471W94YNK8KYMJEK8P7RHD.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Kenny Johnson](https://blog.cloudflare.com/id-id/author/kenny/)

5 menit dibaca

SALIN URL

Artikel ini juga tersedia dalam [English](https://blog.cloudflare.com/zero-trust-private-networking-rules/), [日本語](https://blog.cloudflare.com/ja-jp/zero-trust-private-networking-rules/), [简体中文](https://blog.cloudflare.com/zh-cn/zero-trust-private-networking-rules/), dan [ภาษาไทย](https://blog.cloudflare.com/th-th/zero-trust-private-networking-rules/).

![Zero Trust Private Networking Rules](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47MRF88GZPB88K0SDC99KC.png&w=1761&h=1011&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA//rm+fTj7OXd4tva493c6ePd6ubZ5eTS//3q/Pbl7uTb5NbT5dbS6t7W6+XX6OXV///v//np8uTa6NPN6NHK7dvQ7+TW7OjZ///0//3t9+nc7dfO7dTL8t7S9OjZ8O3d///3///x/fDj9OHY9ODW+ejc+fDg9fLh///5///1//ns++/m/O/n//Xq//np+vjl///6///4///z//ny//v1///2///x/fzn///7///5///2//72///6///7///0/v3o)

Tahun ini, kami [mengumumkan](https://blog.cloudflare.com/private-networking/) kemampuan untuk membangun jaringan pribadi di jaringan Cloudflare dengan kontrol akses berbasis identitas. Kami dengan senang hati menyampaikan bahwa hal ini juga akan diterapkan ke sesi dan interval login.

### **Jaringan pribadi gagal beradaptasi**

Jaringan pribadi selama bertahun-tahun menjadi tulang punggung untuk aplikasi perusahaan. Tim keamanan menggunakannya untuk membangun perimeter keamanan yang ketat pada aplikasi. Untuk mengakses data sensitif, pengguna harus secara fisik berada di jaringan. Ini artinya mereka harus berada di kantor, terhubung dengan perangkat yang dikelola perusahaan. Ini bukan solusi yang sempurna — akses jaringan dapat dibobol melalui koneksi fisik atau Wi-Fi, tetapi alat, seperti sertifikat dan firewall fisik, siap mencegah ancaman ini.

Batasan ini menjadi tantangan seiring bekerja jarak jauh makin jamak dilakukan. Kantor cabang, pusat data, dan karyawan jarak jauh membutuhkan akses ke aplikasi, jadi organisasi mulai mengandalkan Jaringan Pribadi Virtual (VPN) untuk memasukkan pengguna jarak jauh ke jaringan yang sama dengan aplikasi mereka.

Bersama masalah akibat pengguna yang terhubung dari berbagai tepat, model keamanan jaringan pribadi menjadi masalah yang makin berbahaya. Setelah berada di jaringan pribadi, pengguna dapat mengakses semua sumber daya secara default kecuali jika secara tegas dilarang. Kontrol dan log berbasis identitas dinilai sulit atau bahkan tidak mungkin diterapkan.

Selain itu, jaringan pribadi memiliki biaya overhead operasional. Jaringan pribadi dirutekan sesuai dengan ruang IP terdaftar RFC 1918, yang terbatas dan dapat menyebabkan alamat IP yang tumpang-tindih dan berbenturan. Administrator juga perlu mempertimbangkan total beban yang dapat ditampung jaringan pribadi mereka, beban yang makin berat karena karyawan melakukan panggilan video atau bahkan menonton video saat senggang dengan VPN aktif.

### **Alternatif modern tidak memecahkan semua kasus penggunaan**

Aplikasi SaaS dan solusi Jaringan Zero Trust seperti [Cloudflare Access](https://www.cloudflare.com/teams/access/) memudahkan penyediaan pengalaman yang aman tanpa VPN. Administrator dapat mengonfigurasikan kontrol, seperti autentikasi multifaktor dan peringatan log untuk login yang janggal bagi setiap aplikasi. Kontrol keamanan untuk aplikasi yang dirilis ke publik telah jauh melampaui kontrol aplikasi di jaringan pribadi.

Namun demikian, beberapa aplikasi masih membutuhkan jaringan pribadi yang lebih tradisional. Kasus penggunaan yang melibatkan klien tebal di luar browser atau TCP arbitrer atau protokol UDP masih lebih cocok untuk model konektivitas yang berada di luar browser.

Kami mendengar bahwa ada pelanggan yang bersemangat menerapkan model Zero Trust, tetapi masih ingin mendukung kasus penggunaan jaringan pribadi yang lebih konvensional. Untuk memecahkannya, kami mengumumkan kemampuan untuk membangun jaringan pribadi di jaringan global kami. Administrator dapat menyusun aturan Zero Trust bagi mereka yang dapat mencapai IP atau tujuan tertentu. Pengguna akhir yang terhubung dari agen Cloudflare yang sama yang memberdayakan jaringan terbatas mereka ke Internet di seluruh dunia. Namun, satu aturan belum ada.

### **Membawa kontrol sesi ke jaringan pribadi Cloudflare**

Jaringan global Cloudflare membuat hal ini dapat dilakukan dengan kecepatan tinggi. Langkah pertama adalah menghubungkan jaringan pribadi apa pun ke Cloudflare. Hal ini dapat dilakukan dengan membuat tunnel aman untuk koneksi keluar saja menggunakan Cloudflare Tunnel, atau menerapkan pendekatan koneksi yang lebih tradisional, seperti tunnel GRE atau IPSec.

Setelah koneksi tunnel dibuat, rentang IP pribadi tertentu dapat diiklankan di instans Cloudflare. Hal ini dilakukan dengan serangkaian perintah untuk memetakan tunnel ke blok alamat IP CIDR. Dalam cuplikan layar di bawah ini, rentang CIDR dipetakan ke Cloudflare Tunnel yang unik -- masing-masing dengan pengidentifikasi dan nama unik yang ditetapkan.isolationisolation

Setelah aplikasi dapat dikenali oleh jaringan Cloudflare, pengguna perlu cara untuk mengakses rentang IP pribadi ini. Di sini, VPN umumnya digunakan untuk memasukkan pengguna ke jaringan yang sama dengan aplikasi. Alih-alih, klien WARP Cloudflare digunakan untuk menghubungkan lalu lintas Internet pengguna ke jaringan Cloudflare.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-872 Embedded Image - InYG4l](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4892H4GVY7X131YK9JHGNN.png&w=715&h=109&f=webp&fit=cover&position=center)

Administrator kemudian dapat mengontrol lalu lintas dari klien perangkat pengguna. Mereka dapat membuat kebijakan granular berbasis identitas untuk mengontrol pengguna mana yang dapat mengakses aplikasi tertentu di alamat IP pribadi tertentu atau, nantinya, nama host.

Ini adalah langkah maju yang besar untuk tim TI dan Keamanan, karena dapat menghilangkan latensi yang mengganggu, masalah manajemen, dan backhaul yang disebabkan oleh VPN. Namun, setelah pengguna mengautentikasi satu kali, mereka dapat terus terhubung tanpa batas waktu, kecuali jika akses dicabut. Kami tahu beberapa pelanggan perlu memaksa login setiap 24 jam, misalnya, atau mengatur batas waktu setelah satu minggu. Kami senang dapat memberikan fitur tersebut bagi pelanggan.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-872 Embedded Image - gtsZD4](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45AD7M9P909ZRNWDZT66RC.png&w=604&h=670&f=webp&fit=cover&position=center)

Dengan meluncurkan beta, administrator dapat menambahkan aturan sesi ke sumber daya yang tersedia dalam model jaringan pribadi ini. Administrator akan dapat mengonfigurasikan durasi sesi tertentu untuk kebijakan mereka, dan mewajibkan pengguna melakukan autentikasi ulang dengan autentikasi multifaktor.

### **Apa selanjutnya?**

Pengumuman ini hanya merupakan satu faktor yang membuat jaringan pribadi Zero Trust Cloudflare menjadi lebih hebat bagi organisasi Anda. Dukungan UDP untuk model ini juga diumumkan minggu ini. Teams akan dapat menggunakan server nama DNS pribadi yang sudah ada untuk memetakan nama host aplikasi mereka di domain lokal. Hal ini mencegah masalah akibat benturan IP atau alamat IP pribadi sementara untuk aplikasi.

Kami senang dapat menawarkan versi beta untuk kedua fitur ini. Jadi jika Anda ingin mencobanya sebelum tahun depan, gunakan [tautan pendaftaran](https://cloudflare.com/zero-trust/lp/private-dns-waitlist) ini untuk mengetahui kapan beta tersedia.

Jika Anda ingin mulai mencoba kontrol Zero Trust untuk jaringan pribadi Anda, solusi Cloudflare gratis untuk 50 pengguna pertama. Buka dash.teams.cloudflare.com untuk memulai!

Di halaman ini

Diskusikan Online

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fzero-trust-private-networking-rules%2F&t=Aturan%20Jejaring%20Pribadi%20Zero%20Trust)[](https://x.com/intent/post?text=Aturan+Jejaring+Pribadi+Zero+Trust&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fzero-trust-private-networking-rules%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fzero-trust-private-networking-rules%2F)[](https://bsky.app/intent/compose?text=Aturan+Jejaring+Pribadi+Zero+Trust+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fzero-trust-private-networking-rules%2F)[](https://mastodonshare.com/?text=Aturan+Jejaring+Pribadi+Zero+Trust&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fzero-trust-private-networking-rules%2F)[](https://www.threads.net/intent/post?text=Aturan+Jejaring+Pribadi+Zero+Trust+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fzero-trust-private-networking-rules%2F)

## Tag terkait

[CIO Week](https://blog.cloudflare.com/id-id/tag/cio-week/)[Zero Trust](https://blog.cloudflare.com/id-id/tag/zero-trust/)

Ikuti di Media Sosial

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Berlangganan untuk menerima pemberitahuan postingan baru

Alamat email

Kami tidak akan pernah membagikan alamat email Anda.

Berlangganan

Terima kasih telah berlangganan! Periksa kotak masuk Anda untuk mengonfirmasi.
