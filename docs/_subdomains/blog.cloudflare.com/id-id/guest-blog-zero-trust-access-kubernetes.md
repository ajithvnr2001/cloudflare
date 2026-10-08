---
url: https://blog.cloudflare.com/id-id/guest-blog-zero-trust-access-kubernetes/
title: Blog Tamu: k8s tunnels dengan Kudelski Security | Blog Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:46:11.767993+00:00
---

# Blog Tamu: k8s tunnels dengan Kudelski Security | Blog Cloudflare

> Source: https://blog.cloudflare.com/id-id/guest-blog-zero-trust-access-kubernetes/

[Blog](https://blog.cloudflare.com/id-id/)

[CIO Week](https://blog.cloudflare.com/id-id/tag/cio-week/)[Cloudflare Access](https://blog.cloudflare.com/id-id/tag/cloudflare-access/)[Cloudflare Tunnel](https://blog.cloudflare.com/id-id/tag/cloudflare-tunnel/)+2Tampilkan 2 tag lainnya

5 TagTampilkan 5 tag

  * Tag Post
  * [Cloudflare Access](https://blog.cloudflare.com/id-id/tag/cloudflare-access/)[Cloudflare Tunnel](https://blog.cloudflare.com/id-id/tag/cloudflare-tunnel/)[Zero Trust](https://blog.cloudflare.com/id-id/tag/zero-trust/)
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



[Guest Post](https://blog.cloudflare.com/id-id/tag/guest-post/)[Zero Trust](https://blog.cloudflare.com/id-id/tag/zero-trust/)

[CIO Week](https://blog.cloudflare.com/id-id/tag/cio-week/)[Cloudflare Access](https://blog.cloudflare.com/id-id/tag/cloudflare-access/)[Cloudflare Tunnel](https://blog.cloudflare.com/id-id/tag/cloudflare-tunnel/)[Guest Post](https://blog.cloudflare.com/id-id/tag/guest-post/)[Zero Trust](https://blog.cloudflare.com/id-id/tag/zero-trust/)

8 Desember 2021

# Blog Tamu: k8s tunnels dengan Kudelski Security

![Romain Aviolat](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46QR28J0P7014Z8BQ4JJKR.png&w=64&h=64&f=webp&fit=cover&position=center)

[Romain Aviolat](https://blog.cloudflare.com/id-id/author/romain-aviolat/)

9 menit dibaca

SALIN URL

Artikel ini juga tersedia dalam [English](https://blog.cloudflare.com/guest-blog-zero-trust-access-kubernetes/), [日本語](https://blog.cloudflare.com/ja-jp/guest-blog-zero-trust-access-kubernetes/), [简体中文](https://blog.cloudflare.com/zh-cn/guest-blog-zero-trust-access-kubernetes/), dan [ภาษาไทย](https://blog.cloudflare.com/th-th/guest-blog-zero-trust-access-kubernetes/).

![Guest Blog: k8s tunnels with Kudelski Security](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW471Y5SE2PHSG0TP2F83CTW.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/Pjk+PXg7+3a6+nZ7+vd8+3f7+ra5ePQ//vm+/fj8e/d7erc8ezg9e7i8evd6OXT//7q//rn9vLh8ezg9e3j+fDl9e7g7OjX///t//7q+vXl9u/j+fDn/fPo+vLk8ezb///x///u//nn+vPl/vTo//fr/vbn9fHe///0///w//zo/vbl//fp//vs//rp+fTg///2///x//7p//jl//rp//7t//zq/Pbh///2///y///p//nl//vp///t//3q/Pfi)

_Hari ini, kami dengan bangga memublikasikan entri blog yang ditulis oleh teman-teman kami di Kudelski Security, penyedia layanan keamanan terkelola. Beberapa minggu yang lalu, Romain Aviolat, Teknisi Cloud dan Keamanan Utama di Kudelski Security mendekati tim Zero Trust kami dengan solusi unik untuk masalah sulit yang didukung oleh Identity-aware Proxy Cloudflare, yang kami sebut Cloudflare Tunnel, untuk memastikan akses aplikasi yang aman di lingkungan kerja jarak jauh._

_Kami sangat menikmati belajar tentang solusi mereka sehingga kami ingin memperkuat cerita mereka. Secara khusus, kami menghargai bagaimana teknisi Kudelski Security memanfaatkan fleksibilitas dan skalabilitas teknologi kami sepenuhnya guna mengotomatisasi alur kerja bagi pengguna akhir mereka. Jika Anda tertarik untuk mempelajari lebih lanjut tentang Kudelski Security, lihat pekerjaan mereka di bawah ini atau_ _[blog penelitian mereka](https://research.kudelskisecurity.com/)._

### **Akses Zero Trust ke Kubernetes**

Selama beberapa tahun terakhir, tim teknisi Kudelski Security telah memprioritaskan migrasi infrastruktur kami ke lingkungan multi-cloud. Migrasi cloud internal kami mencerminkan apa yang dikejar klien akhir kami dan telah membekali kami dengan keahlian dan alat guna meningkatkan layanan kami bagi mereka. Selain itu, transisi ini telah memberi kami kesempatan untuk membayangkan kembali pendekatan keamanan kami sendiri dan menerapkan praktik terbaik Zero Trust.

Sejauh ini, salah satu aspek paling menantang dari adopsi Zero Trust kami adalah mengamankan akses ke berbagai bidang kontrol (API) Kubernetes (K8s) kami di berbagai lingkungan cloud. Awalnya, tim infrastruktur kami berusaha untuk mendapatkan visibilitas dan menerapkan kontrol berbasis identitas yang konsisten ke berbagai API yang terkait dengan klaster K8s yang berbeda. Selain itu, saat berinteraksi dengan API ini, pengembang kami sering tidak mengetahui klaster mana yang perlu mereka akses dan bagaimana melakukannya.

Untuk mengatasi pergesekan ini, kami merancang solusi internal yang memanfaatkan Cloudflare untuk mengotomatisasi bagaimana pengembang dapat dengan aman mengautentikasi ke klaster K8 yang berada di cloud publik dan lingkungan di lokasi. Secara khusus, untuk pengembang tertentu, kini kami dapat menampilkan semua layanan K8s yang mereka akses di lingkungan cloud tertentu, mengautentikasi permintaan akses menggunakan aturan Zero Trust Cloudflare, dan membuat koneksi ke klaster tersebut melalui Identity-aware proxy Cloudflare, Cloudflare Tunnel.

Yang terpenting, alat otomatisasi ini telah memungkinkan Kudelski Security sebagai organisasi untuk meningkatkan postur keamanan kami dan meningkatkan pengalaman pengembang kami pada saat yang bersamaan. Kami memperkirakan bahwa alat ini dapat memberi penghematan pada pengembang baru setidaknya dua jam dari waktu yang dihabiskan untuk membaca dokumentasi, mengirimkan tiket layanan TI, dan secara manual menerapkan dan mengonfigurasi berbagai alat yang diperlukan untuk mengakses klaster K8s yang berbeda.

Di blog ini, kami merinci beberapa poin masalah spesifik yang kami tangani, bagaimana kami merancang alat otomatisasi kami, dan bagaimana Cloudflare membantu kami berkembang dalam perjalanan Zero Trust kami dengan cara kerja dari rumah yang ramah.

### **Tantangan mengamankan lingkungan multi-cloud**

Karena Kudelski Security telah memperluas layanan klien dan tim pengembangan internal kami, kami secara inheren telah memperluas jejak aplikasi kami dalam beberapa klaster K8s dan beberapa penyedia cloud. Untuk teknisi dan pengembang infrastruktur kami, API klaster K8s adalah titik masuk penting untuk pemecahan masalah. Kami mengerjakan GitOps dan semua penerapan aplikasi secara otomatis, tetapi kami masih harus selalu terhubung ke klaster untuk menarik log atau men-debug masalah.

Namun, mempertahankan keragaman ini mengakibatkan kompleksitas dan tekanan bagi administrator infrastruktur. Untuk pengguna akhir, infrastruktur yang luas dapat diterjemahkan ke kredensial yang berbeda, alat akses yang berbeda untuk setiap klaster, dan file konfigurasi yang berbeda untuk dilacak.

Pengalaman akses yang kompleks seperti itu dapat membuat pemecahan masalah waktu riil menjadi sangat menyakitkan. Misalnya, teknisi panggilan yang mencoba memahami lingkungan K8s yang tidak dikenal mungkin akan menggali banyak dokumentasi atau dipaksa untuk membangunkan rekan kerja lain untuk mengajukan pertanyaan sederhana. Semua ini rawan kesalahan dan membuang waktu yang berharga.

Pendekatan umum dan tradisional untuk mengamankan akses ke K8s API menghadirkan tantangan yang kami tahu ingin kami hindari. Misalnya, kami merasa bahwa mengekspos API ke internet publik secara inheren akan meningkatkan permukaan serangan kami, itu adalah risiko yang tidak dapat kami tanggung. Selain itu, kami tidak ingin memberikan akses berbasis luas ke API klaster kami melalui jaringan internal dan mengabaikan risiko pergerakan lateral. Seiring pertumbuhan Kudelski, biaya operasional dan kerumitan penerapan VPN di seluruh tenaga kerja kami dan lingkungan cloud yang berbeda akan menimbulkan tantangan penskalaan juga.

Sebaliknya, kami menginginkan pendekatan yang memungkinkan kami mempertahankan lingkungan kecil dan mikro tersegmentasi, domain kegagalan kecil, dan tidak lebih dari satu cara untuk memberikan akses ke layanan.

### **Memanfaatkan Identity-aware Proxy Cloudflare untuk akses Zero Trust**

Untuk melakukan ini, tim teknik Kudelski Security memilih pendekatan yang lebih modern: membuat koneksi antara pengguna dan setiap klaster K8s kami melalui Identity-aware proxy (IAP). IAP fleksibel dalam memberlakukan dan menambahkan layer keamanan tambahan di depan aplikasi kami dengan memverifikasi identitas pengguna saat permintaan akses dibuat. Lebih lanjut, mereka mendukung pendekatan Zero Trust kami dengan membuat koneksi dari pengguna ke aplikasi individual — bukan seluruh jaringan.

Setiap klaster memiliki IAP dan kumpulan kebijakannya sendiri, yang memeriksa identitas (melalui SSO perusahaan kami) dan faktor kontekstual lainnya seperti postur perangkat laptop pengembang. IAP tidak menggantikan mekanisme autentikasi klaster K8s, ia menambahkan yang baru di atasnya, dan berkat federasi identitas dan SSO, proses ini sepenuhnya transparan bagi pengguna akhir kami.

Dalam setup kami, Kudelski Security menggunakan IAP Cloudflare sebagai komponen Cloudflare Access -- solusi ZTNA dan salah satu dari beberapa layanan keamanan yang disatukan oleh platform Zero Trust Cloudflare.

Untuk berbagai aplikasi berbasis web, IAP membantu menciptakan pengalaman tanpa hambatan bagi pengguna akhir yang meminta akses melalui browser. Pengguna mengautentikasi melalui SSO perusahaan atau penyedia identitas mereka sebelum mencapai aplikasi yang aman, sementara IAP bekerja di belakang layar.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-732 Embedded Image - P55jnN](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49K2VAFT4A519YQS24T537.png&w=715&h=445&f=webp&fit=cover&position=center)

Aliran pengguna itu terlihat berbeda untuk aplikasi berbasis CLI karena kami tidak dapat mengarahkan ulang aliran jaringan CLI seperti yang kami lakukan di browser. Dalam kasus kami, teknisi kami ingin menggunakan klien K8s favorit mereka yang berbasis CLI seperti [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) atau [k9s](https://github.com/derailed/k9s). Ini berarti Cloudflare IAP kami perlu bertindak sebagai proxy SOCKS5 antara klien CLI dan setiap klaster K8s.

Untuk membuat koneksi IAP ini, Cloudflare menyediakan daemon dari sisi server ringan yang disebut _cloudflared_ yang menghubungkan infrastruktur dengan aplikasi. Koneksi terenkripsi ini berjalan di jaringan global Cloudflare di mana kebijakan Zero Trust diterapkan dengan inspeksi sekali jalan.

Namun, tanpa otomatisasi apa pun, tim infrastruktur Kudelski Security perlu mendistribusikan daemon pada perangkat pengguna akhir, memberikan panduan tentang cara menyiapkan koneksi terenkripsi tersebut, dan mengambil langkah-langkah konfigurasi manual dan praktis lainnya serta memeliharanya dari waktu ke waktu. Selain itu, pengembang masih akan kekurangan satu panel visibilitas di berbagai klaster K8s yang perlu mereka akses dalam pekerjaan rutin mereka.

### **Solusi otomatis kami: k8s-tunnels!**

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-732 Embedded Image - cuETxG](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44DZ45FR0B1WE74BF3A9YQ.png&w=715&h=402&f=webp&fit=cover&position=center)

Untuk mengatasi tantangan ini, tim teknik infrastruktur kami mengembangkan alat internal — yang disebut 'k8s-tunnels' — yang menyematkan langkah-langkah konfigurasi kompleks guna mempermudah pengembang kami. Selain itu, alat ini secara otomatis menemukan semua klaster K8s yang dapat diakses oleh pengguna tertentu berdasarkan kebijakan Zero Trust yang dibuat. Untuk mengaktifkan fungsi ini, kami menyematkan SDK dari beberapa penyedia cloud publik utama yang digunakan oleh Kudelski Security. Alat ini juga menyematkan _cloudflared_ daemon_,_ artinya kami hanya perlu mendistribusikan satu alat kepada pengguna kami.

Secara keseluruhan, pengembang yang meluncurkan alat tersebut melalui alur kerja berikut: (kami berasumsi bahwa pengguna sudah memiliki kredensial yang valid jika tidak, alat akan membuka browser di IDP kami untuk mendapatkannya)

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-732 Embedded Image - 1cW0Ni](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49D383W7PRHXJZ9GV5YH6T.png&w=715&h=402&f=webp&fit=cover&position=center)

1\. Pengguna memilih satu atau lebih klaster untuk

2\. k8s-tunnel akan secara otomatis membuka koneksi dengan Cloudflare dan mengekspos proxy SOCKS5 lokal di mesin pengembang

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-732 Embedded Image - e6BCTT](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48Q29GT1EXDBZ3768243HW.png&w=715&h=213&f=webp&fit=cover&position=center)

3\. k8s-tunnel mengubah konfigurasi klien kubernetes lokal pengguna dengan mendorong informasi yang diperlukan untuk melalui proxy SOCKS5 lokal

4\. k8s-tunnel mengalihkan konteks klien Kubernetes ke koneksi saat ini

5\. Pengguna sekarang dapat menggunakan klien CLI favoritnya untuk mengakses klaster K8s

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-732 Embedded Image - 33L8m2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47JP2K7630YC1MNQSH4H48.png&w=715&h=188&f=webp&fit=cover&position=center)

Seluruh prosesnya sangat mudah dan digunakan setiap hari oleh tim teknik kami. Dan, tentu saja, semua keajaiban ini dimungkinkan melalui mekanisme penemuan otomatis yang kami buat di k8s-tunnels. Setiap kali teknisi baru bergabung dengan tim kami, kami hanya meminta mereka untuk meluncurkan proses penemuan otomatis dan memulainya.

Berikut adalah contoh proses penemuan otomatis yang sedang berjalan.

  1. k8s-tunnels akan terhubung ke berbagai API penyedia cloud kami dan mencantumkan klaster K8s yang dapat diakses pengguna
  2. k8s-tunnels akan mempertahankan file konfigurasi lokal pada mesin pengguna dari klaster tersebut sehingga proses ini tidak dijalankan lebih dari sekali



### **Peningkatan otomatisasi**

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-732 Embedded Image - LLM3Dx](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45E9SX357T4GFFPEB0AD8X.png&w=715&h=265&f=webp&fit=cover&position=center)

Untuk penerapan di lokasi, hal tersebut sedikit lebih rumit karena kami tidak memiliki cara sederhana untuk menyimpan metadata klaster K8 seperti yang kami lakukan dengan tag sumber daya dengan penyedia cloud publik. Kami memutuskan untuk menggunakan [Vault](https://www.vaultproject.io/) sebagai Penyimpanan Nilai Utama untuk meniru tag sumber daya cloud publik untuk lokal. Dengan cara ini kami dapat mencapai penemuan otomatis klaster lokal dengan mengikuti proses yang sama seperti dengan penyedia cloud publik.

Mungkin Anda melihat bahwa di tangkapan layar CLI sebelumnya, pengguna dapat memilih beberapa klaster secara bersamaan! Kami segera menyadari bahwa pengembang kami sering kali perlu mengakses beberapa lingkungan secara bersamaan untuk membandingkan beban kerja yang berjalan dalam produksi dan dalam staging. Jadi, alih-alih membuka dan menutup tunnel setiap kali mereka perlu berpindah klaster, kami merancang alat kami sedemikian rupa sehingga mereka dapat dengan mudah membuka beberapa tunnel secara paralel dalam satu instans k8s-tunnels dan cukup mengganti klaster K8s tujuan di laptop mereka.

Terakhir, tetapi tidak kalah penting, kami juga telah menambahkan dukungan untuk favorit dan notifikasi pada rilisan baru, memanfaatkan Cloudflare Worker, tapi hal tersebut untuk postingan blog lainnya.

### **Apa selanjutnya**

Dalam merancang alat ini, kami telah mengidentifikasi beberapa masalah di dalam pustaka klien Kubernetes saat digunakan bersama dengan beberapa proxy SOCKS5, dan kami [bekerja dengan komunitas Kubernetes](https://github.com/kubernetes/kubernetes/pull/105632) untuk memperbaiki masalah tersebut, jadi semua orang akan mendapatkan manfaat dari patch tersebut dalam waktu dekat.

Dengan postingan blog ini, kami ingin menyoroti bagaimana mungkin menerapkan keamanan Zero Trust untuk beban kerja kompleks yang berjalan di lingkungan multi-cloud, sekaligus meningkatkan pengalaman pengguna akhir.

Meskipun hari ini kode 'k8s-tunnels' kami terlalu spesifik untuk Kudelski Security, tujuan kami adalah untuk membagikan apa yang telah kami buat kembali ke komunitas Kubernetes, sehingga organisasi lain dan pelanggan Cloudflare dapat mengambil manfaat darinya.

Di halaman ini

Diskusikan Online

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fguest-blog-zero-trust-access-kubernetes%2F&t=Blog%20Tamu%3A%20k8s%20tunnels%20dengan%20Kudelski%20Security)[](https://x.com/intent/post?text=Blog+Tamu%3A+k8s+tunnels+dengan+Kudelski+Security&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fguest-blog-zero-trust-access-kubernetes%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fguest-blog-zero-trust-access-kubernetes%2F)[](https://bsky.app/intent/compose?text=Blog+Tamu%3A+k8s+tunnels+dengan+Kudelski+Security+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fguest-blog-zero-trust-access-kubernetes%2F)[](https://mastodonshare.com/?text=Blog+Tamu%3A+k8s+tunnels+dengan+Kudelski+Security&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fguest-blog-zero-trust-access-kubernetes%2F)[](https://www.threads.net/intent/post?text=Blog+Tamu%3A+k8s+tunnels+dengan+Kudelski+Security+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fguest-blog-zero-trust-access-kubernetes%2F)

## Tag terkait

[CIO Week](https://blog.cloudflare.com/id-id/tag/cio-week/)[Cloudflare Access](https://blog.cloudflare.com/id-id/tag/cloudflare-access/)[Cloudflare Tunnel](https://blog.cloudflare.com/id-id/tag/cloudflare-tunnel/)[Guest Post](https://blog.cloudflare.com/id-id/tag/guest-post/)[Zero Trust](https://blog.cloudflare.com/id-id/tag/zero-trust/)

Ikuti di Media Sosial

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)

  * ![Romain Aviolat](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46QR28J0P7014Z8BQ4JJKR.png&w=64&h=64&f=webp&fit=cover&position=center)[Romain Aviolat](https://blog.cloudflare.com/id-id/author/romain-aviolat/)

[](https://kudelskisecurity.com/)




## Berlangganan untuk menerima pemberitahuan postingan baru

Alamat email

Kami tidak akan pernah membagikan alamat email Anda.

Berlangganan

Terima kasih telah berlangganan! Periksa kotak masuk Anda untuk mengonfirmasi.
