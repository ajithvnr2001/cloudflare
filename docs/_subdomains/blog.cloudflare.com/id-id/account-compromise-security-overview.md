---
url: https://blog.cloudflare.com/id-id/account-compromise-security-overview/
title: Di dalam Cloudflare: Mencegah Pengambilalihan Akun | Blog Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:52:22.561781+00:00
---

# Di dalam Cloudflare: Mencegah Pengambilalihan Akun | Blog Cloudflare

> Source: https://blog.cloudflare.com/id-id/account-compromise-security-overview/

[Blog](https://blog.cloudflare.com/id-id/)

[Cloudflare Access](https://blog.cloudflare.com/id-id/tag/cloudflare-access/)[Cloudflare Gateway](https://blog.cloudflare.com/id-id/tag/gateway/)[Keamanan](https://blog.cloudflare.com/id-id/tag/security/)+1Tampilkan 1 tag lainnya

4 TagTampilkan 4 tag

  * Tag Post
  * [Cloudflare Access](https://blog.cloudflare.com/id-id/tag/cloudflare-access/)[Cloudflare Gateway](https://blog.cloudflare.com/id-id/tag/gateway/)[Keamanan](https://blog.cloudflare.com/id-id/tag/security/)[Security Week](https://blog.cloudflare.com/id-id/tag/security-week/)
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

[Cloudflare Access](https://blog.cloudflare.com/id-id/tag/cloudflare-access/)[Cloudflare Gateway](https://blog.cloudflare.com/id-id/tag/gateway/)[Keamanan](https://blog.cloudflare.com/id-id/tag/security/)[Security Week](https://blog.cloudflare.com/id-id/tag/security-week/)

30 Maret 2021

# Di dalam Cloudflare: Mencegah Pengambilalihan Akun

![Julie A. Sparks](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44BAJVDRPB1FB1M1Z9V77K.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Julie A. Sparks](https://blog.cloudflare.com/id-id/author/julie/)

8 menit dibaca

SALIN URL

Artikel ini juga tersedia dalam [English](https://blog.cloudflare.com/account-compromise-security-overview/) dan [ภาษาไทย](https://blog.cloudflare.com/th-th/account-compromise-security-overview/).

![Inside Cloudflare: Preventing Account Takeovers](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW485JWNNH1XYV6F9WJBYZXW.png&w=1585&h=740&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA+ffe9PLb6+bU5t3O59zN6t/N6OHM4t/I/fvj+Pbg7+ra6uHV7OHU7+XU7ebS5uPN///p/fvn9O/h7+bd8ufd9uvd8+zZ6+jT///w///t+fPm9erj+ezj/fLk+vPh8e7a///2///x//bp+u3l/vDn//fp//jm9/Lf///6///0//jp/u7j//Ln//rs//zq/Pbi///8///1//no/+/h//Pm//zt//7s//jk///9///2//no/+/g//Pm//3t//7t//jk)

Selama seminggu terakhir, Cloudflare telah menerbitkan postingan blog tentang produk yang dibuat untuk mengamankan pelanggan kami dari [bot penjejalan kredensial](https://blog.cloudflare.com/super-bot-fight-mode/), [mendeteksi pengguna dengan kredensial yang disusupi](https://blog.cloudflare.com/account-takeover-protection), dan [memblokir pengguna dari layanan proxy](https://blog.cloudflare.com/protecting-apis-from-abuse-and-data-exfiltration/). Tapi apa yang kami lakukan di dalam Cloudflare untuk mencegah pengambilalihan akun pada aplikasi kami sendiri? Tim Keamanan menggunakan produk Cloudflare untuk secara proaktif mencegah penyusupan akun. Selain itu, kami membangun deteksi dan otomatisasi sebagai layer kedua untuk memperingatkan kami jika akun karyawan disusupi. Ini memastikan kami dapat menangkap perilaku yang mencurigakan, menyelidikinya, dan memulihkannya dengan cepat.

Tujuan kami adalah mencegah penyerang otomatis dan tertarget terlepas dari teknik pengambilalihan akun: serangan membabi buta, penjejalan kredensial, botnet, rekayasa sosial, atau pengelabuan.

### Siklus Hidup Pengambilalihan Akun Klasik

Pertama, mari kita telusuri siklus hidup umum akun yang disusupi.

Dalam skenario umum, satu set kata sandi dan alamat email telah dilanggar. Kredensial ini digunakan kembali melalui penjejalan kredensial dalam upaya untuk mendapatkan akses ke semua akun (pada semua platform) di mana pengguna mungkin telah menggunakan kembali kombinasi tersebut. Setelah penyerang memiliki akses awal, yang berarti kombinasi berhasil, mereka dapat memperoleh informasi tentang sistem tersebut dan beralih ke sistem lain melalui beberapa metode. Ini diklasifikasikan sebagai gerakan lateral. Dengan bocornya satu kata sandi, ada potensi perusahaan yang sama sekali tidak terkait untuk melakukan pelanggaran di mana pengguna yang tidak sah masuk dan mencuri data.

Vektor lain untuk pengambilalihan akun adalah email pengelabuan dengan tautan yang dikirim ke karyawan dengan tujuan untuk mengumpulkan kredensial. Taktik umum yang digunakan oleh penyerang adalah Evilginx, kerangka serangan man-in-the-middle yang digunakan untuk mengelabui kredensial dan cookie sesi layanan web. Dengan membuat halaman yang mirip dengan portal login perusahaan, penyerang dapat mencegat lalu lintas dan mendapatkan kredensial yang dimasukkan ke dalam halaman. Setelah kredensial didapatkan, mereka segera login sebagai pengguna, mencuri informasi, dan mencoba berkompromi dengan sistem/akun terkait. Karena pemfilteran email pengelabuan telah meningkat, penyerang berusaha untuk '"vish", yaitu metode rekayasa sosial melalui panggilan telepon, agar karyawan mengunjungi situs web berbahaya seperti yang disebutkan di atas.

Dua cara paling umum untuk menambahkan verifikasi tambahan adalah dengan menggunakan Time-based One-Time Password (TOTP) atau kode verifikasi melalui pesan teks (SMS) sebagai opsi autentikasi multifaktor. TOTP membuat kata sandi satu kali yang menggunakan waktu saat ini sebagai sumber keunikan. Kata sandi tersebut biasanya diperoleh dari aplikasi seluler seperti Google Authenticator. Tak satu pun dari metode autentikasi multifaktor ini akan melindungi dari pengambilalihan akun karena penyerang dapat menggunakan taktik rekayasa sosial untuk meyakinkan karyawan agar memberikan TOTP atau SMS. Selain itu, penyerang dapat melakukan pertukaran SIM, sebuah taktik di mana operator telepon ditipu untuk memberikan nomor telepon orang lain ke perangkat baru, untuk mendapatkan kode verifikasi yang dikirim ke perangkat yang mereka miliki.

Pengambilalihan akun adalah ancaman nyata bagi perusahaan dan penggunanya. Mari kita telusuri beberapa contoh nyata dari kompromi dan bagaimana mereka dapat dicegah di berbagai level menggunakan Cloudflare.

## Tindakan Pengambilalihan Akun

Pada tahun 2020, contoh dampak pengambilalihan akun ditunjukkan ketika penyerang dapat [membajak kredensial login karyawan Twitter](https://www.wsj.com/articles/the-teenager-behind-the-twitter-hack-and-how-he-did-it-11596563449) lalu mengakses banyak akun Twitter yang terverifikasi. Seorang remaja di Florida memalsukan nomor telepon karyawan dengan menukar SIM, sebuah taktik di mana operator telepon ditipu untuk memberikan nomor telepon orang lain ke perangkat baru. Kemudian dia merekayasa sosial seorang karyawan Twitter dengan berpura-pura menjadi anggota departemen TI mereka. Setelah karyawan tersebut yakin, dia mengarahkan mereka ke halaman pengelabuan yang menyerupai portal login Okta Twitter. Setelah karyawan memasukkan kredensial mereka ke halaman yang kelihatannya sah, penyerang dapat menggunakannya untuk mendapatkan akses ke sistem Twitter. Serangan ini dimungkinkan karena penggunaan SMS dan/atau TOTP untuk autentikasi multifaktor. Jika karyawan Twitter memiliki token keamanan perangkat keras U2F, misalnya YubiKey, penyerang akan memasukkan kredensial yang dicuri kemudian diminta untuk menyentuh kunci fisik untuk mendapatkan akses, yang tidak mungkin dilakukan tanpa kunci karyawan.

Dalam skenario ini, perusahaan dapat mengadopsi [Cloudflare Access](https://www.cloudflare.com/en-gb/teams/access) untuk mengunci akses ke sistem internal ke perangkat yang dikeluarkan perusahaan dan menggunakan kebijakan akses detail untuk membatasi akun mana yang dapat diakses oleh setiap grup pengguna. Kebijakan tersebut dapat digunakan untuk memaksa karyawan mengautentikasi dengan token keamanan perangkat keras U2F dan memblokir semua peristiwa yang menggunakan TOTP/SMS.

Pada tahun 2018, pelanggaran data membahayakan data pengguna MyFitnessPal termasuk kata sandi. Dua tahun kemudian, data yang dilanggar digunakan untuk mengoordinasikan serangan penjejalan kredensial terhadap dua perusahaan asuransi: [Independence Blue Cross](https://www.prnewswire.com/news-releases/independence-blue-cross-provides-notice-of-a-privacy-incident-301087638.html) dan [AmeriHealth New Jersey](https://www.prnewswire.com/news-releases/amerihealth-hmo-inc-and-amerihealth-insurance-company-of-new-jersey-provides-notice-of-a-privacy-incident-301087643.html). Serangan penjejalan kredensial mengakibatkan akses tidak sah ke informasi asuransi pengguna termasuk klaim. Contoh ini menjelaskan bagaimana setiap perusahaan dapat menjadi target taktik pengambilalihan akun.

Solusi bot Cloudflare —termasuk [Super Bot Fight Mode](https://blog.cloudflare.com/super-bot-fight-mode/), yang diluncurkan hari ini — solusi ini dapat digunakan oleh perusahaan asuransi untuk memblokir penjejalan kredensial secara proaktif. Secara internal, perusahaan asuransi yang disebutkan dapat mengaktifkan [Pemeriksaan Kredensial yang Terekspos di WAF](https://blog.cloudflare.com/account-takeover-protection/) guna memeriksa kata sandi pengguna yang dilanggar dan meminta mereka untuk mengganti kata sandi.

### Menggunakan Cloudflare untuk Mengamankan Cloudflare

Melalui produk Cloudflare, banyak vektor pengambilalihan akun tipikal diblokir. Ini membantu Tim Keamanan memfokuskan perhatian kami dalam membangun pertahanan internal kami terhadap serangan khusus Cloudflare.

Misalnya, dengan [Gateway Cloudflare](https://www.cloudflare.com/en-gb/teams/gateway/) kami dapat secara proaktif memblokir domain yang berpotensi berbahaya di pembuat aturan UI yang sederhana. Dengan memblokir kategori ini di titik akhir perusahaan, kami menurunkan risiko seorang karyawan akan mengunjungi ancaman yang diketahui.

Ketika ada domain baru yang diamati oleh Tim Keamanan mencoba serangan pengambilan kredensial, kami kemudian dapat memblokirnya secara proaktif menggunakan daftar blokir di Gateway. Tindakan ini mencegah titik akhir menyelesaikan situs web meski karyawan secara tidak sengaja menavigasi ke sana. Banyak alat keamanan menyediakan kemampuan untuk memblokir berdasarkan alamat IP; namun, selain pemblokiran IP, kami juga memblokir berdasarkan nama domain untuk merespons serangan dengan cepat. Dengan memblokir domain, jika penyerang memberlakukan situs web yang sama pada alamat IP baru, kami telah mengurangi risiko seseorang mengunjungi situs tersebut.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![img](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45MVRH4RPH04MXATTX5MHX.png&w=715&h=166&f=webp&fit=cover&position=center)

Secara internal, semua karyawan Cloudflare diharuskan menggunakan token keamanan perangkat keras FIDO2 untuk mengautentikasi ke sumber daya perusahaan. Token ini melindungi sistem internal dari berbagai jebakan yang membuat pengambilalihan akun lebih mudah.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-403 Embedded Image - hXDAQM](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46BQE16882E9RXWBMQ97A9.png&w=715&h=104&f=webp&fit=cover&position=center)

Selain persyaratan token perangkat keras, Tim Keamanan menggunakan [Cloudflare Access](https://www.cloudflare.com/en-gb/teams/access) untuk menerapkan hanya [perangkat perusahaan terkelola](https://blog.cloudflare.com/zero-trust-with-managed-devices/) yang dapat terhubung ke sistem internal. Aturan terkelola dapat dikonfigurasikan untuk mengizinkan atau memblokir berdasarkan kombinasi faktor seperti metode multifaktor dan geografi alamat IP yang digunakan. Tim Keamanan dapat beralih dari pendekatan reaktif ke proaktif dengan memblokir peristiwa autentikasi dari perangkat nonperusahaan, negara di mana kami tidak memiliki karyawan, atau peristiwa yang menggunakan SMS/TOTP alih-alih token keamanan perangkat keras U2F.

### Menambahkan Layer Perlindungan Internal

Selain fitur Gateway, Tim Deteksi & Respons mengekspor log [Gateway](https://www.cloudflare.com/en-gb/teams/gateway/) & [Access](https://www.cloudflare.com/en-gb/teams/access) untuk lebih memperkaya, menghubungkan, dan mengembangkan deteksi pada peristiwa mentah bersama dengan log sistem internal lainnya. Dengan menggabungkan semua log kami ke dalam saluran internal, kami memiliki kesempatan untuk membangun deteksi kustom dan otomatisasi respons terhadap insiden.

Terkait dengan pengambilalihan akun, tim kami berfokus untuk membangun deteksi yang berfokus pada [teknik akses awal](https://attack.mitre.org/tactics/TA0001/) sebagai layer kedua perlindungan pada akun karyawan.

Beberapa contoh deteksi yang berfokus pada penyusupan akun adalah:

  * Login atau peristiwa autentikasi lainnya ke sistem internal dari VPN.
  * Perubahan token autentikasi multifaktor karyawan dan penggunaan perangkat baru.
  * Login atau peristiwa autentikasi dari alamat IP yang tidak dikenal.
  * Login atau peristiwa autentikasi dari alamat IP yang terletak di negara berisiko tinggi.
  * Peristiwa autentikasi dengan token perangkat lunak autentikasi multifaktor ke sistem internal.
  * Setiap peristiwa dari alamat IP yang terkait dengan pelaku ancaman yang diketahui.



Namun, ada banyak variasi pola perilaku yang dapat menandakan bahwa sebuah akun sedang disusupi. Alih-alih menggunakan aturan deteksi statis untuk semuanya, Tim Deteksi & Respons telah memprioritaskan pembuatan model pembelajaran mesin yang membantu mendeteksi perilaku autentikasi anomali untuk akun karyawan.

Sinyal risiko adalah pola yang _dapat_ menunjukkan perilaku jahat dan digunakan untuk menentukan seberapa besar kemungkinan perilaku tersebut benar-benar berbahaya. Setiap perusahaan memiliki beberapa sinyal risiko keamanan yang sama untuk mendeteksi penyusupan akun; namun, penggunaan sinyal bisa sangat berbeda tergantung pada infrastruktur mereka. Dengan menggabungkan produk Keamanan Cloudflare dengan rekayasa kami sendiri kami dapat memiliki perlindungan tanpa batas untuk sistem eksternal dan internal.

### Mempengaruhi Peta Rencana Produk

Saat Cloudflare memperluas rangkaian produk keamanan mereka, Tim Keamanan secara keseluruhan bekerja erat dalam memengaruhi peta rencana produk. Kami dapat memberikan wawasan yang dapat ditindaklanjuti ke dalam semua kontrol dan deteksi yang diperlukan untuk secara efektif memitigasi dan merespons serangan siber saat ini. Melalui komunikasi dan kolaborasi umpan balik, kami membagikan strategi internal dengan tim produk lalu melakukan dogfood pada produk yang dibuat di Cloudflare guna memastikan produk tersebut membantu dalam melindungi data karyawan dan pelanggan kami.

Cloudflare adalah tempat di mana ide-ide baru disambut dan didiskusikan untuk memastikan produk kami merupakan aset bagi tim Keamanan & TI yang menggunakannya. Tindakan ini memberdayakan guna menjadi bagian dari perjalanan tersebut!

### Langkah selanjutnya

Pengambilalihan akun adalah salah satu serangan keamanan siber yang paling umum, tetapi Anda dapat dengan cepat meningkatkan kematangan program keamanan Anda dengan menerapkan mitigasi yang berfokus pada akses awal. Mitigasi ini menghentikan penyerang pada tahap “pengintaian” dari rantai pembunuhan siber, model fase serangan yang dibuat oleh Lockheed Martin dan diperluas melalui [kerangka kerja MITER ATT&CK](https://attack.mitre.org/tactics/enterprise/).

Jadi, apa strategi terbaik yang dapat Anda ambil untuk melindungi keamanan perusahaan organisasi Anda?

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-403 Embedded Image - AswhIQ](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45Q6Z6ACKAHV0QPTJCSMJG.png&w=715&h=1019&f=webp&fit=cover&position=center)

_Membuat serangan pengambilalihan akun sesulit mungkin untuk dieksekusi._

Di Cloudflare, kami menerapkan kebijakan keamanan yang berfokus pada keamanan akun, ini termasuk penerapan token keamanan perangkat keras untuk autentikasi multifaktor, kompleksitas kata sandi yang kuat, pemblokiran proaktif dari domain buruk yang diketahui serta perlindungan bot di situs eksternal. Masing-masing mitigasi ini ditujukan untuk mengganggu fase awal rantai pembunuhan penyerang.

Di halaman ini

Diskusikan Online

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Faccount-compromise-security-overview%2F&t=Di%20dalam%20Cloudflare%3A%20Mencegah%20Pengambilalihan%20Akun)[](https://x.com/intent/post?text=Di+dalam+Cloudflare%3A+Mencegah+Pengambilalihan+Akun&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Faccount-compromise-security-overview%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Faccount-compromise-security-overview%2F)[](https://bsky.app/intent/compose?text=Di+dalam+Cloudflare%3A+Mencegah+Pengambilalihan+Akun+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Faccount-compromise-security-overview%2F)[](https://mastodonshare.com/?text=Di+dalam+Cloudflare%3A+Mencegah+Pengambilalihan+Akun&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Faccount-compromise-security-overview%2F)[](https://www.threads.net/intent/post?text=Di+dalam+Cloudflare%3A+Mencegah+Pengambilalihan+Akun+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Faccount-compromise-security-overview%2F)

## Tag terkait

[Cloudflare Access](https://blog.cloudflare.com/id-id/tag/cloudflare-access/)[Cloudflare Gateway](https://blog.cloudflare.com/id-id/tag/gateway/)[Keamanan](https://blog.cloudflare.com/id-id/tag/security/)[Security Week](https://blog.cloudflare.com/id-id/tag/security-week/)

Ikuti di Media Sosial

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Berlangganan untuk menerima pemberitahuan postingan baru

Alamat email

Kami tidak akan pernah membagikan alamat email Anda.

Berlangganan

Terima kasih telah berlangganan! Periksa kotak masuk Anda untuk mengonfirmasi.
