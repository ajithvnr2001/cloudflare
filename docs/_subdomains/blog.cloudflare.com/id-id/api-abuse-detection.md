---
url: https://blog.cloudflare.com/id-id/api-abuse-detection/
title: Mengumumkan Deteksi Penyalahgunaan API | Blog Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:51:04.833360+00:00
---

# Mengumumkan Deteksi Penyalahgunaan API | Blog Cloudflare

> Source: https://blog.cloudflare.com/id-id/api-abuse-detection/

[Blog](https://blog.cloudflare.com/id-id/)

[API](https://blog.cloudflare.com/id-id/tag/api/)[Bots](https://blog.cloudflare.com/id-id/tag/bots/)[Keamanan](https://blog.cloudflare.com/id-id/tag/security/)+2Tampilkan 2 tag lainnya

5 TagTampilkan 5 tag

  * Tag Post
  * [Keamanan](https://blog.cloudflare.com/id-id/tag/security/)[Security Week](https://blog.cloudflare.com/id-id/tag/security-week/)
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



[Mobile](https://blog.cloudflare.com/id-id/tag/mobile/)[Security Week](https://blog.cloudflare.com/id-id/tag/security-week/)

[API](https://blog.cloudflare.com/id-id/tag/api/)[Bots](https://blog.cloudflare.com/id-id/tag/bots/)[Keamanan](https://blog.cloudflare.com/id-id/tag/security/)[Mobile](https://blog.cloudflare.com/id-id/tag/mobile/)[Security Week](https://blog.cloudflare.com/id-id/tag/security-week/)

26 Maret 2021

# Mengumumkan Deteksi Penyalahgunaan API

![Ben Solomon](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46SECATWZWE73T50K3E3EM.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Thomas Vissers](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48EQYHWTK57CBC6J7BZEHN.png&w=64&h=64&f=webp&fit=cover&position=center)

[Ben Solomon](https://blog.cloudflare.com/id-id/author/bensol/) dan [Thomas Vissers](https://blog.cloudflare.com/id-id/author/thomas-vissers/)

9 menit dibaca

SALIN URL

Artikel ini juga tersedia dalam [English](https://blog.cloudflare.com/api-abuse-detection/) dan [ภาษาไทย](https://blog.cloudflare.com/th-th/api-abuse-detection/).

![Announcing API Abuse Detection](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW492446S2QFTD6VYPMQW1MF.png&w=1999&h=903&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////+vv87uvn6OHc7Obj8u/v8PHy5+rr/////f7+8Ovl6d7V7ePd8+7u8vLz6uzt////////9Ozj693P7+LZ9u/t9vT27/Dx////////+e7l8N7P9OTa+/Px/Pn79fX2//////////Pr9uPW+unh//n4////+/v8//////////jz/Ong//Hs//////////////////////36/+/q//j1//////////////////////78//Hu//r4////////////)

API sangat penting. Sepanjang tahun 2000-an, mereka membentuk [backbone layanan web populer](https://blog.postman.com/intro-to-apis-history-of-apis/), membantu Internet menjadi lebih berguna dan dapat diakses. Di tahun 2010, API memainkan peran yang lebih besar dalam kehidupan kita, memungkinkan perangkat pribadi untuk berkomunikasi dengan dunia digital. Banyak aktivitas kita sehari-hari, seperti menggunakan layanan berbagi tumpangan dan membayar latte, bergantung pada bentuk komunikasi modern ini. Sekarang kita mendekati dunia pascapandemi di mana API akan menjadi lebih penting dari sebelumnya.

Sayangnya, seiring berkembangnya teknologi, begitu pula dengan luas permukaannya untuk disalahgunakan. API bukan pengecualian. Layanan berbagi kendara yang bersaing mungkin memantau harga satu sama lain melalui API, memicu perang harga, dan pemborosan sumber daya digital. Atau peminum kopi mungkin memanipulasi API untuk diskon latte. Beberapa perusahaan memiliki ribuan API — termasuk yang bahkan tidak mereka ketahui. Cloudflare dapat membantu menyelesaikan masalah ini.

Hari ini, kami mengumumkan akses awal ke Penemuan API dan Deteksi Penyalahgunaan API.

### **Latar belakang**

Sebelum melangkah lebih jauh, penting untuk menjelaskan _mengapa_ kami membutuhkan solusi untuk API. alat keamanan tradisional, termasuk [Pembatasan Tingkat](https://www.cloudflare.com/rate-limiting/) dan [Perlindungan DDoS](https://www.cloudflare.com/ddos/), dapat sangat berguna. Tetapi pendekatan ini tidak dibangun untuk bertindak sendiri. Kami mungkin menilai batas titik akhir API tertentu, tetapi bagaimana kami memilih ambang batas yang tepat? Akan sulit untuk melakukan ini dalam skala besar tanpa menimbulkan masalah. API mungkin akan terkena serangan terdistribusi (jatuh di bawah ambang batas), atau mungkin melihat peningkatan lalu lintas yang sah (melebihi ambang batas).

Yang lain menyarankan untuk memberlakukan [Manajemen Bot](https://www.cloudflare.com/products/bot-management) pada titik akhir API. Dalam banyak kasus, ini efektif dan menambahkan beberapa tingkat perlindungan, terutama jika API dimaksudkan untuk digunakan oleh browser (sebagai bagian dari aplikasi web). Tetapi Manajemen Bot dirancang untuk menemukan aktor jahat di antara _manusia_. Para aktor ini biasanya menggunakan otomatisasi, sedangkan manusia biasanya menggunakan browser, jadi perbedaannya agak jelas. Tetapi API menghadirkan masalah yang berbeda. API diotomatisasi, jadi solusi harus menemukan bot yang buruk di antara _bot lainnya_. Kita harus membedakan antara lalu lintas otomatis yang baik dan buruk.

Untuk memecahkan masalah API, kami harus mengembangkan tindakan _intent_ — hampir seperti mewawancarai setiap permintaan untuk menentukan tujuannya. Kita harus menjawab pertanyaan-pertanyaan berikut murni berdasarkan data tidak langsung:

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-454 Embedded Image - ylgm4e](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45CSADR131KP4B6WQ1Q56M.png&w=715&h=276&f=webp&fit=cover&position=center)

  * Apakah permintaan ini menggunakan API untuk tujuan penggunaan?
  * Apakah permintaan ini menunjukkan perilaku yang mencurigakan? Mengapa?



Sekali lagi, sementara alat seperti Pembatasan Tingkat dapat menangani masalah biner (misalnya, "apakah IP ini melebihi 200 permintaan?"), masalah API menuntut arbiter yang lebih subjektif. Ini mengharuskan kami untuk memeriksa _tujuan_ API dan menentukan batasan yang wajar berdasarkan apa yang kami temukan. Ini juga mengharuskan kami untuk menemukan sumber kebenaran dasar yang baru. Saat kami membangun Manajemen Bot, kami dapat mengonfirmasikan bahwa permintaan adalah manusia atau otomatis dengan [mengeluarkan tantangan](https://blog.cloudflare.com/stop-the-bots-practical-lessons-in-machine-learning/). API melibatkan layanan otomatis yang tidak dapat membuktikan legitimasinya dengan menyelesaikan tantangan.

Setelah berbulan-bulan memilah-milah masalah ini, kami bersemangat untuk memberikan pandangan pertama pada solusi kami. Hal ini akan dibahas dalam beberapa bagian…

### **Penemuan API**

Sebagian pengguna kami memberi tahu kami bahwa mereka tidak dapat melacak API mereka. Bahkan sebelum kami mencoba untuk melindungi titik akhir ini, kami perlu memetakannya dan memahami area permukaan serangan. Kami menyebutnya "Penemuan API."

Proses penemuan dimulai dengan penyederhanaan. Situs web besar mungkin memiliki ribuan API, tetapi banyak panggilan yang terlihat serupa. Perhatikan dua jalur berikut:

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-454 Embedded Image - 8j93Tn](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45H8JY6CT2GB6CCAH02SS2.png&w=715&h=369&f=webp&fit=cover&position=center)

  * api.example.com/**login/237**
  * api.example.com/**login/415**



Dalam contoh ini, "237" dan "415" adalah pengidentifikasi pelanggan. Kedua jalur memiliki tujuan yang sama — mengizinkan pengguna untuk masuk ke akun mereka — tetapi tidak identik. Jadi kami memetakan jalur dan segera _memperpendeknya_ menjadi yang berikut:

  * api.example.com/**login/***
  * api.example.com/**login/***



Perhatikan bagaimana kami menghapus pengidentifikasi pelanggan. Sistem kami dapat mendeteksi bagian API yang berubah, memungkinkan kami dalam mengenali kedua jalur sebagai jalur yang sama. Kami melakukan ini dengan merekam kardinalitas setiap titik akhir. Sebagai contoh, kami mungkin awalnya menemukan bahwa ada 700 string berbeda yang diamati sebagai pengganti tanda bintang. "237" dan "415" hanyalah dua dari kemungkinan tersebut. Kami kemudian menggunakan pembelajaran tanpa pengawasan untuk memilih ambang (dalam hal ini, katakanlah 30). Karena kami telah melihat lebih dari 30 varian jalur ini, kami mengenali pengidentifikasi pelanggan sebagai _variabel_ dan memperpendek jalur tersebut. Proses ini disebut "normalisasi jalur.”

Penemuan API adalah blok bangunan untuk berbagai produk keamanan yang akan datang. Tetapi pada intinya, teknologinya adalah tentang menghasilkan peta API yang sederhana dan dapat dipercaya. Berikut adalah contoh kecil dari apa yang mungkin Anda temukan:

Bayangkan daftar ini diskalakan ke ratusan, atau bahkan ribuan titik akhir. Beberapa akan terlihat jelas (semoga titik akhir login diperkirakan!), tetapi yang lain bisa menjadi kejutan. Peta terakhir akan membantu mengidentifikasi variabel atau token yang direferensikan oleh setiap titik akhir.
    
    
    login/<customer_identifier>
    auth
    account/<customer_identifier>
    password_reset
    logout

### **Mendeteksi Penyalahgunaan berdasarkan Volume**

Sekarang setelah kami menemukan API, kami dapat mulai mencari penyalahgunaan. Pendekatan pertama kami adalah menangani anomali volumetrik. Dengan kata lain, kami membuat tebakan yang cerdas tentang _seberapa sering_ setiap jalur dicapai dan menetapkan beberapa ambang batas untuk mengelola penyalahgunaan. Ini adalah bentuk pembatasan tingkat adaptif.

Pertimbangkan jalur API /**pembaruan skor** untuk situs web olahraga. Anda mungkin bisa menebak apa fungsinya — ini secara rutin mengambil skor terbaru untuk sebuah pertandingan, yang mungkin terjadi beberapa kali per detik. Kami mungkin memberlakukan pembelajaran tanpa pengawasan dan menetapkan ambang batas tinggi untuk penggunaan normal. Mungkin 150 permintaan per menit untuk IP tertentu, agen pengguna, atau pengidentifikasi sesi lainnya.

Tetapi situs web olahraga yang sama dapat mengharuskan penggunanya untuk memiliki akun. Dalam hal ini, API /**reset kata sandi** terpisah bisa ada di domain yang sama. Tidak ada penggemar olahraga yang akan mereset kata sandi mereka sebanyak mereka memeriksa skor, jadi jalur ini kemungkinan akan memiliki ambang batas yang lebih rendah. Keunggulan pembelajaran tanpa pengawasan (dan bentuk deteksi penyalahgunaan kami) adalah kami dapat memetakan situs Anda, mengembangkan garis dasar terpisah untuk setiap API, dan mencoba memprediksi intent permintaan saat dibuat. Jika kami melihat 150 upaya tiba-tiba untuk mereset kata sandi, sistem kami akan segera mencurigai pengambilalihan akun.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-454 Embedded Image - 94qcXC](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW490ZP2WNMBDZWBYJ300RJZ.png&w=715&h=316&f=webp&fit=cover&position=center)

Penting juga untuk memahami _mengapa_ mengapa lalu lintas berubah saat itu terjadi. Misalnya, kita tidak boleh memblokir lalu lintas olahraga saat melonjak karena Final NBA. Meskipun titik akhir /**pembaruan skor** mungkin untuk sementara lebih banyak digunakan, Cloudflare akan mengenali konteks yang lebih besar dan mengubah ambang batas yang relevan. Kami hanya ingin memitigasi ketika seseorang menyalahgunakan titik akhir.

### **Mendeteksi Penyalahgunaan berdasarkan Urutan**

Tim kami sering menerapkan [Model Keju Swiss](https://www.nytimes.com/2020/12/05/health/coronavirus-swiss-cheese-infection-mackay.html) untuk keamanan. Pendekatan ini telah digunakan dalam perawatan kesehatan, keamanan fisik, dan banyak industri lainnya, tetapi idenya sederhana. Setiap layer pertahanan akan memiliki beberapa lubang — tetapi menumpuk _pertahanan unik_ (atau irisan keju) di samping satu sama lain guna meningkatkan keamanan secara keseluruhan.

Dalam dunia keamanan Internet, kami menyebutnya "pertahanan mendalam". API pertama kali dilindungi oleh suite keamanan Cloudflare (DDoS, dll.). Layer kedua menggunakan deteksi volumetrik (dijelaskan di atas). Tetapi layer ketiga benar-benar berbeda dengan semua yang telah kami lakukan sebelumnya: ini adalah deteksi anomali _sekuensial_ . Kami berharap cara ini akan mengubah lanskap API secara dramatis..

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-454 Embedded Image - ktdjyC](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4584PXG865WKNF3D7SZD12.png&w=715&h=382&f=webp&fit=cover&position=center)

Begitulah cara kerjanya. Seperti biasa, kami mulai dengan menjalankan normalisasi jalur untuk menemukan himpunan status terhingga. Dalam satu pengujian, proses ini mengurangi sekitar 10.000 status menjadi hanya 60, menyederhanakan masalah API secara besar-besaran. Kemudian kami menggunakan [Rantai Markov](https://brilliant.org/wiki/markov-chains/) untuk membangun matriks transisi, yang merupakan peta dari semua negara dan ke mana mereka biasanya mengarah. Kami menyelesaikannya dengan menetapkan probabilitas untuk setiap transisi

Hasil akhirnya? Kami secara konseptual dapat menyatukan gerakan di sebuah situs, yang mungkin terdiri dari langkah-langkah berikut:

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-454 Embedded Image - xAe0wT](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49CQVZJXWFCK2Q8G3SFHC6.png&w=715&h=297&f=webp&fit=cover&position=center)

  1. Permintaan dikirim ke /**login/*/enter**
  2. Lalu diarahkan ke /**login/*/verify**
  3. Akhirnya dialihkan ke /**login-successful**



Ini terlihat seperti pengguna valid yang mencoba login. Sekali lagi, kami menggunakan pembelajaran tanpa pengawasan untuk mendeteksi aliran seperti ini, tetapi pendekatan kami juga mendeteksi outlier. Dalam hal ini, kami telah menemukan bahwa 1 → 2 → 3 adalah aliran logis, tetapi bagaimana jika seseorang tiba langsung di langkah 3? Kami mungkin menandai permintaan ini sebagai anomali.

Pendekatan ini, yang sangat bergantung pada Markov Chains, cukup efisien. Pertimbangkan untuk menambahkan satu node ke rantai: jelas, rantai tersebut sendiri berskala linear. Matriks transisi, yang memetakan semua kemungkinan hubungan node, ditingkatkan secara eksponensial. Tetapi kami telah menemukan bahwa sebagian besar dari hubungan ini tidak dilakukan. Dalam praktiknya, tidak ada yang mengupayakan jalur berbelit-belit seperti logout → upload → auth. Transisi yang lebih umum, yang mungkin terlihat seperti login → update-score → logout, hanya mencakup 2% dari semua transisi dalam pengujian kami. Kami dapat menyimpan matriks secara efisien dengan mengabaikan transisi yang tidak digunakan.

Itulah rangkuman ikhtisar kami tentang deteksi anomali sekuensial. Ini adalah layer terakhir dalam Model Keju Swiss kami, dan sama seperti pendekatan volumetrik, ini menggunakan garis dasar yang kami perbarui dari waktu ke waktu.

### **Penggunaan lainnya**

Deteksi Penyalahgunaan API sangat serbaguna. Meskipun kami menciptakan teknologi ini untuk penggunaan API umum, ada beberapa kasus penggunaan yang perlu disorot.

Yang pertama adalah Manajemen Bot untuk aplikasi seluler. Meski solusi Manajemen Bot kami telah bekerja dengan baik untuk banyak aplikasi, Deteksi Penyalahgunaan API jauh lebih efektif. Itu karena perangkat seluler sering mengandalkan API. Sementara permintaan mereka mengikuti langkah pengguna manusia yang lambat dan disengaja, aplikasi seluler menggunakan titik akhir API dan mungkin tampak otomatis. Aplikasi ini tidak menawarkan kebebasan navigasi yang sama seperti yang dilakukan situs web. Namun kami dapat menggunakan ini untuk keuntungan kami: pengguna yang sah mengikuti urutan yang dapat diprediksi berdasarkan status sebelumnya, yang sekarang dapat kami validasi dengan Deteksi Penyalahgunaan API.

Perusahaan lain telah mengembangkan SDK seluler untuk mendekati penyalahgunaan API. Namun SDK berukuran besar, sulit untuk diintegrasikan, dan terkadang tidak efektif. Pendekatan sisi klien ini juga rentan terhadap gangguan. SDK melakukan otentikasi perangkat lunak klien, tetapi tidak mampu mendeteksi setiap perilaku penyalahgunaan yang sebenarnya. Siapa pun yang dapat mengekstrak sertifikat sisi klien dapat segera melewati perlindungan bot. Kami yakin dapat mengamankan aplikasi seluler tanpa SDK apa pun — cukup dengan memberlakukan Deteksi Penyalahgunaan API di titik akhir seluler.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-454 Embedded Image - n0AvJM](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45AK9MV647A1KEK4R2GNA4.png&w=715&h=240&f=webp&fit=cover&position=center)

Selain itu, banyak titik akhir API yang penuh sesak. Tidak semua orang dapat mengidentifikasi lalu lintas API/bot "baik" mereka, yang berarti bahwa model keamanan positif mungkin tidak berfungsi. Hal ini terutama berlaku untuk perusahaan yang bekerja dengan mitra yang merotasi agen pengguna atau tidak dapat menyelaraskan sinyal mereka. Pendekatan kami benar-benar menghindari masalah ini. Kami secara otomatis membuat peta titik akhir API, mengembangkan garis dasar, dan mendeteksi penyalahgunaan.

### **Akses awal**

Apakah Anda memiliki situs yang membutuhkan Deteksi Penyalahgunaan API? Apakah Anda ingin mencoba Manajemen Bot generasi berikutnya untuk aplikasi seluler Anda? Harap beri tahu kami dengan menghubungi tim akun Anda. Kami dengan gembira akan menghadirkan model beberapa bulan mendatang.

Di halaman ini

Diskusikan Online

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fapi-abuse-detection%2F&t=Mengumumkan%20Deteksi%20Penyalahgunaan%20API)[](https://x.com/intent/post?text=Mengumumkan+Deteksi+Penyalahgunaan+API&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fapi-abuse-detection%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fapi-abuse-detection%2F)[](https://bsky.app/intent/compose?text=Mengumumkan+Deteksi+Penyalahgunaan+API+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fapi-abuse-detection%2F)[](https://mastodonshare.com/?text=Mengumumkan+Deteksi+Penyalahgunaan+API&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fapi-abuse-detection%2F)[](https://www.threads.net/intent/post?text=Mengumumkan+Deteksi+Penyalahgunaan+API+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fapi-abuse-detection%2F)

## Tag terkait

[API](https://blog.cloudflare.com/id-id/tag/api/)[Bots](https://blog.cloudflare.com/id-id/tag/bots/)[Keamanan](https://blog.cloudflare.com/id-id/tag/security/)[Mobile](https://blog.cloudflare.com/id-id/tag/mobile/)[Security Week](https://blog.cloudflare.com/id-id/tag/security-week/)

Ikuti di Media Sosial

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Berlangganan untuk menerima pemberitahuan postingan baru

Alamat email

Kami tidak akan pernah membagikan alamat email Anda.

Berlangganan

Terima kasih telah berlangganan! Periksa kotak masuk Anda untuk mengonfirmasi.
