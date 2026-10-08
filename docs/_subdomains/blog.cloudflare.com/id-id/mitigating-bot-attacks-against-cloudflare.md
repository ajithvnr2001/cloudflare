---
url: https://blog.cloudflare.com/id-id/mitigating-bot-attacks-against-cloudflare/
title: Mengurangi Serangan Bot terhadap Cloudflare | Blog Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:51:03.925366+00:00
---

# Mengurangi Serangan Bot terhadap Cloudflare | Blog Cloudflare

> Source: https://blog.cloudflare.com/id-id/mitigating-bot-attacks-against-cloudflare/

[Blog](https://blog.cloudflare.com/id-id/)

[Bot Management](https://blog.cloudflare.com/id-id/tag/bot-management/)[Bots](https://blog.cloudflare.com/id-id/tag/bots/)[Security Week](https://blog.cloudflare.com/id-id/tag/security-week/)+1Tampilkan 1 tag lainnya

4 TagTampilkan 4 tag

  * Tag Post
  * [Bot Management](https://blog.cloudflare.com/id-id/tag/bot-management/)[Security Week](https://blog.cloudflare.com/id-id/tag/security-week/)[Serangan](https://blog.cloudflare.com/id-id/tag/attacks/)
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



[Serangan](https://blog.cloudflare.com/id-id/tag/attacks/)

[Bot Management](https://blog.cloudflare.com/id-id/tag/bot-management/)[Bots](https://blog.cloudflare.com/id-id/tag/bots/)[Security Week](https://blog.cloudflare.com/id-id/tag/security-week/)[Serangan](https://blog.cloudflare.com/id-id/tag/attacks/)

26 Maret 2021

# Mengurangi Serangan Bot terhadap Cloudflare

![Sergi Isasi](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44GA2M8TX4RHAHVAP55XN1.png&w=64&h=64&f=webp&fit=cover&position=center)

[Sergi Isasi](https://blog.cloudflare.com/id-id/author/sergi/)

8 menit dibaca

SALIN URL

Artikel ini juga tersedia dalam [English](https://blog.cloudflare.com/mitigating-bot-attacks-against-cloudflare/) dan [ภาษาไทย](https://blog.cloudflare.com/th-th/mitigating-bot-attacks-against-cloudflare/).

![Mitigating Bot Attacks against Cloudflare](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4895BES3KE5TVJ0RKV6CWB.png&w=1382&h=668&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/////fz+7+/w5ufo6ujq8e3w8O7x6Ont/////v3+7+/u5uXi6+bi8uzp8u7t6uvr////////8fDt6OXe7ebd9u3k9vDr7u7r////////9vXw7enh8+rf/PLn/PXu8/Pw/////////fz59fLr+/Pr//vy//34+fr4/////////////vz5///7////////////////////////////////////////////////////////////////////////////)

Kata "bot" di Internet mempunyai banyak makna. Pengalaman pertama saya dengan 'bot' adalah [di IRC](https://en.wikipedia.org/wiki/IRC_bot), di mana bot cukup membantu dalam memastikan kanal favorit Anda tidak diambil alih oleh pengguna berbahaya dan memungkinkan bermain game ringan yang seru. Sekitar lima tahun yang lalu, “bot” seringkali merujuk pada obrolan teks yang dikombinasikan dengan AI dan platform/apps pengiriman pesan sebagai cara baru untuk berinteraksi dengan pelanggan. Kini kebanyakan konotasi mengenai bot di Internet, khususnya di bidang keamanan, seringkali negatif dan sejumlah vendor kami menawarkan cara baru untuk mendeteksi dan memblokir bot.

Bentuk paling sederhana dari bot adalah sepotong perangkat lunak otomatis yang menggantikan interaksi manusia. Pada contoh di atas, hal itu dilakukan untuk meningkatkan skala sebuah proses agar lebih cepat atau lebih luas dibandingkan jika dilakukan dengan satu tindakan manual tunggal. [Bot Mesin Pencari](https://help.duckduckgo.com/duckduckgo-help-pages/results/duckduckbot/) ada karena tidak mungkin (atau setidaknya, tidak praktis) untuk merangkak di situs Internet satu per satu. Manfaat peningkatan skala ini dapat digunakan untuk tujuan baik dan buruk dengan menyerang suatu properti di Internet. Bot digunakan untuk serangan berskala besar — bot dapat diterapkan untuk menyerang API yang tidak diatur konfigurasinya dengan benar, melumpuhkan situs, atau mengambil daftar kredensial yang dimiliki orang lain dan memeriksa kredensial yang berfungsi di titik ujung login sebelum [mengambil data](https://blog.cloudflare.com/protecting-apis-from-abuse-and-data-exfiltration/).

Pandemi global telah menyebabkan [kekurangan mikrocip secara global](https://hbr.org/2021/02/why-were-in-the-midst-of-a-global-semiconductor-shortage). Pada tahun 2020, Microsoft, Nvidia, dan Sony bersama-sama meluncurkan perangkat gaming atau kartu video dengan permintaan tinggi dan pasokan rendah yang tetap menjadi langka beberapa bulan kemudian. Jenis lingkungan ini sesuai untuk semua jenis aktivitas bot — mulai dari pehobi yang mencoba memperoleh akses ke salah satu butir di atas untuk pemakaian sendiri, hingga penimbun yang secara aktif mencoba membeli sebanyak mungkin dengan harga eceran untuk dijual kembali di pasar terbuka dengan harga jauh lebih tinggi. Bot akan mengambil semua data inventaris dan kemudian menggunakan skrip untuk proses penambahan ke keranjang/pembelian dengan jauh lebih cepat daripada pengguna biasa yang menggunakan browser. Hal ini setidaknya dapat menyebabkan frustrasi dan juga menyebabkan serangan DDoS di Layer 7 pada aplikasi yang memperparah masalahnya. Sebagai akibatnya, Nvidia pernah terpaksa [melakukan pembatalan penjualan kepada bot](https://www.theverge.com/2020/9/21/21449353/nvidia-apology-rtx-3080-gpu-preorder-shortage-issues) secara manual dan surut ke belakang dalam salah satu rilisnya. Meskipun bermain game adalah selingan yang menyenangkan, rangkaian keadaan seperti ini sayangnya juga dapat memengaruhi [distribusi vaksin](https://www.capitalgazette.com/coronavirus/ac-cn-maryland-vaccine-bots-20210324-ngcmoadnwne6peb3fv6iu2hbri-story.html).

### Menggunakan Pengelolaan Bot di cloudflare.com

Generasi saat ini dari Pengelolaan Bot Cloudflare dirilis pada tahun 2019. Produk ini awalnya tercipta dari eksperimen internal untuk mengetahui jika kami dapat memprediksi apakah permintaan yang diberikan akan menyelesaikan tantangan menggunakan data jaringan dan model [pembelajaran mesin (ML) kami](https://blog.cloudflare.com/stop-the-bots-practical-lessons-in-machine-learning/). Eksperimen ini akhirnya menghasilkan Skor Bot dan produk Pengelolaan Bot pertama kami yang lengkap, yang telah melalui sejumlah peningkatan dan iterasi serta telah menjadi produk yang sangat berhasil dalam kit alat keamanan pelanggan kami. Kini kami telah meningkatkannya lebih baik lagi untuk paket Pro dan Bisnis dengan [Super Bot Fight Mode (Mode Super Tarung Bot)](https://blog.cloudflare.com/super-bot-fight-mode).

Selama tahap pengembangan internal awal, kami menemukan masalah pada salah satu situs kami yang berinteraksi langsung dengan pelanggan. Untuk alasan yang masih belum jelas sama sekali (tetapi cenderung berbahaya), penyerang telah memasukkan data sampah ke dalam formulir di berbagai halaman arahan Cloudflare, yaitu formulir yang digunakan pengguna sah untuk memasukkan informasi mereka untuk mendaftar ke suatu acara atau promosi, atau agar dihubungi oleh tim penjualan kami. Awalnya ini hanya mengganggu karena menyebabkan tim kami harus memilah dan menghapus data yang tidak berkaitan. Kami juga harus memeriksa kembali dan mengidentifikasi data kiriman yang sah. Seiring perkembangannya, masalah itu menjadi sangat besar sehingga berdampak pada penyedia backend kami (di tempat formulir dikorelasikan) dan masuk ke dalam CRM kami. Gangguan ini berubah dari gangguan menjadi suatu bentuk DDoS aplikasi yang harus dihentikan dengan hati-hati untuk menghindari data positif palsu, yaitu terblokirnya data kiriman yang sah.

Berita tentang masalah tersebut sampai ke tim teknik kami dan menjadi jelas bahwa ini saat yang tepat untuk meluncurkan produk pelanggan pertama kami dan menguji coba produk kami. Awalnya, penyerang tidak berupaya terlalu banyak untuk menyembunyikan diri. Mereka menggunakan skrip siap pakai dan seringkali bahkan tidak mencoba untuk mengubah tanda yang jelas seperti header Agen Pengguna atau menyebarkan serangannya melalui sejumlah besar IP atau ASN. Ketika kami menambahkan metode heuristik ke dalam sistem dan menyetel model pembelajaran mesin, penyerang pun menyesuaikan taktik mereka. Seiring waktu, seluruh alat kami menjadi diperlukan karena penyerang terus-menerus beradaptasi. Berikut contoh serangan yang terjadi belum lama ini; selama serangan, lalu lintas yang bersifat otomatis meningkat menjadi 7 kali lipat dari biasanya selama sekitar 30 menit. Penyekalaan mungkin menjadi masalah bagi penyedia di hilir jaringan kami, di mana kami pada akhirnya mengirim panggilan API untuk menangani pengiriman formulir. Selama serangan ini, Anomaly Detection (Deteksi Anomali) kami (yang merupakan dasar untuk [deteksi penyalahgunaan API](https://blog.cloudflare.com/api-abuse-detection/) baru kami) melakukan sebagian besar tindakan pembersihan yang berat, yang mencapai 42% dari pendeteksian.

Kami juga berjuang mengatasi bot di dasbor kami di berbagai API yang berinteraksi langsung dengan pengguna. Pola umum penyalahgunaan yang terlihat selama bertahun-tahun adalah pengguna berbahaya mendaftarkan diri di banyak domain, sering kali dari TLD gratis, dan sering tersebar di banyak akun. Pengguna itu mengambil beberapa domain ini dan terlibat dalam suatu bentuk spam Optimisasi Mesin Pencari (SEO). Ada anggapan bahwa satu cara untuk meningkatkan peringkat pencarian Anda adalah dengan menautkan banyak situs ke domain Anda. Para pengirim spam SEO mendaftarkan diri ke banyak domain dan membuat ribuan catatan nama host di dalamnya dan kemudian menarik bayaran dari pemilik situs web yang tidak bermoral untuk menautkan silang dari setiap domain ini.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-458 Embedded Image - Syp88E](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46TAWZT307SNZGNFAG586A.png&w=715&h=240&f=webp&fit=cover&position=center)

Selain perilaku buruk SEO itu, hal itu menimbulkan dua masalah teknis pada sistem kami. Pertama: jika domain dan catatan ini dihasilkan dalam jumlah cukup banyak pada saat yang sama, maka hal itu dapat menyebabkan [DNS Pump (Pemompaan DNS)](https://blog.cloudflare.com/how-we-made-our-dns-stack-3x-faster/), sistem kami dirancang untuk mendorong catatan DNS pelanggan ke 200 lebih lokasi dalam hitungan detik. Kami membanggakan diri karena berhasil membuat propagasi DNS seperti sulap dan pelanggan kami sudah terbiasa dan mengandalkan kecepatan ini. Kedua, ada biaya praktis untuk menyimpan catatan ini di setiap server tepi jaringan kami dengan bertujuan hanya untuk kemungkinan mengelabui mesin pencari agar menganggap satu situs itu populer.

Jenis penyalahgunaan ini hanya bekerja melalui skala yang tepat. Seorang pengirim spam SEO harus mampu mendaftarkan diri di banyak domain dengan cara yang efisien dan otomatis untuk bisa menjual layanan mereka. Jadi kami mengeluarkan Pengelolaan Bot untuk mengatasi masalah itu. Awalnya kami memperlambat masalah itu melalui Pembatasan Tingkat (Rate Limiting) serta mencegah alamat IP tertentu untuk mendaftarkan banyak akun dalam waktu singkat, tetapi penyerang tetap bersikeras. Kami memasukkan tantangan pada pendaftaran akun baru yang terlihat muncul secara otomatis melalui produk Pengelolaan Bot kami dan dengan segera masalah itu hilang.

Bagian lain dari dasbor Cloudflare yang berhubungan dengan bot adalah sistem penagihan kami. Penyerang akan menggunakan sistem pemrosesan kartu pembayaran kami untuk menguji validitas nomor kartu kredit yang dicuri, yang memungkinkan mereka menggunakan atau menjual kembali kartu itu untuk melakukan transaksi lain yang lebih mahal di situs berbeda. Sekali lagi, kecepatan dan skala menjadi hal terpenting di sini. Penyerang tidak ingin menguji satu atau dua nomor kartu — mereka ingin menguji lusinan atau ratusan kartu dan mengotomatiskan prosesnya. Tim teknik penagihan kami menggunakan Pengelolaan Bot untuk memicu tantangan atau pemblokiran saat pengguna menambahkan atau mengubah metode pembayaran untuk menghentikan serangan ini. Tim penagihan juga meneruskan skor bot ke sistem deteksi penipuan dari penyedia pembayaran pihak ketiga kami sendiri (melalui [Cloudflare Workers](https://developers.cloudflare.com/bots/bot-management-enterprise#bot-management-variables)), yang memasukkan skor ke dalam analisisnya untuk tinjauan transaksi manual.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-458 Embedded Image - 9QJk02](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48AAZ25NM38TA213DN0DA1.png&w=715&h=151&f=webp&fit=cover&position=center)

### Membangun berdasarkan Fondasi Data Global

Produk Pengelolaan Bot kami berhasil karena banyaknya jumlah pelanggan dan besarnya lalu lintas di jaringan kami. Dengan sekitar 25 juta properti Internet yang dilindungi Cloudflare, kami secara unik ditempatkan untuk mengumpulkan berbagai sinyal ini dan menafsirkannya menjadi data cerdas yang dapat ditindaklanjuti. Rilis Mode Super Bot Fight kini tidak hanya memperluas kemampuan ini kepada versi Pro dan Bisnis tetapi juga akan memberikan dorongan bagi semua pengguna Pengelola Bot. Saat zona Pro dan Bisnis mulai memberi tantangan dan memblokir bot secara langsung berdasarkan sinyal bot, data ini melatih pemodelan kami secara lebih langsung dibandingkan dengan data hasil kesimpulan yang kami gunakan untuk tantangan dan pemblokiran yang tidak terkait bot. Keragaman sinyal dan skala data pada platform global ini memberikan kami keyakinan atas kemampuan kami memblokir bot tidak hanya untuk saat ini, tetapi juga di masa depan.

Kami sangat antusias mendapatkan umpan balik mengenai akses secara dini dari pelanggan Perusahaan kami mengenai model deteksi dan penyalahgunaan API kami. API menghadirkan tantangan berbeda dengan yang ditimbulkan oleh properti yang berinteraksi langsung dengan web, tetapi pengalaman kami membangun [platform Deteksi Anomali](https://blog.cloudflare.com/lessons-learned-from-scaling-up-cloudflare-anomaly-detection-platform/) untuk Pengelolaan Bot memungkinkan kami menggunakan beberapa teknik yang berkaitan untuk mengidentifikasi titik ujung API dan mendeteksi anomali dalam lalu lintas yang otomatis. Penyertaan berbagai teknik baru ini pada portofolio keamanan yang telah ada merupakan bagian dari komitmen kami untuk menyediakan alat terbaik bagi pelanggan kami di satu platform tunggal, apa pun lalu lintas yang mereka miliki di domain mereka. Kombinasi semua alat kami juga memungkinkan respons yang fleksibel — pelanggan dapat memblokir serangan DDoS dan bot tertentu, menantang lalu lintas yang mirip bot, dan menggunakan pembatasan tingkat kami untuk menargetkan lalu lintas API yang mencurigakan.

Di halaman ini

Diskusikan Online

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fmitigating-bot-attacks-against-cloudflare%2F&t=Mengurangi%20Serangan%20Bot%20terhadap%20Cloudflare)[](https://x.com/intent/post?text=Mengurangi+Serangan+Bot+terhadap+Cloudflare&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fmitigating-bot-attacks-against-cloudflare%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fmitigating-bot-attacks-against-cloudflare%2F)[](https://bsky.app/intent/compose?text=Mengurangi+Serangan+Bot+terhadap+Cloudflare+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fmitigating-bot-attacks-against-cloudflare%2F)[](https://mastodonshare.com/?text=Mengurangi+Serangan+Bot+terhadap+Cloudflare&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fmitigating-bot-attacks-against-cloudflare%2F)[](https://www.threads.net/intent/post?text=Mengurangi+Serangan+Bot+terhadap+Cloudflare+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fmitigating-bot-attacks-against-cloudflare%2F)

## Tag terkait

[Bot Management](https://blog.cloudflare.com/id-id/tag/bot-management/)[Bots](https://blog.cloudflare.com/id-id/tag/bots/)[Security Week](https://blog.cloudflare.com/id-id/tag/security-week/)[Serangan](https://blog.cloudflare.com/id-id/tag/attacks/)

Ikuti di Media Sosial

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Berlangganan untuk menerima pemberitahuan postingan baru

Alamat email

Kami tidak akan pernah membagikan alamat email Anda.

Berlangganan

Terima kasih telah berlangganan! Periksa kotak masuk Anda untuk mengonfirmasi.
