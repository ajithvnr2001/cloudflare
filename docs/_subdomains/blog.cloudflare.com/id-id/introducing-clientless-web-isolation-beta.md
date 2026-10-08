---
url: https://blog.cloudflare.com/id-id/introducing-clientless-web-isolation-beta/
title: Memperkenalkan Isolasi Web Tanpa Klien | Blog Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:46:12.477937+00:00
---

# Memperkenalkan Isolasi Web Tanpa Klien | Blog Cloudflare

> Source: https://blog.cloudflare.com/id-id/introducing-clientless-web-isolation-beta/

[Blog](https://blog.cloudflare.com/id-id/)

[CIO Week](https://blog.cloudflare.com/id-id/tag/cio-week/)[Clientless Web Isolation](https://blog.cloudflare.com/id-id/tag/clientless-web-isolation/)[Cloudflare Access](https://blog.cloudflare.com/id-id/tag/cloudflare-access/)+2Tampilkan 2 tag lainnya

5 TagTampilkan 5 tag

  * Tag Post
  * [Cloudflare Access](https://blog.cloudflare.com/id-id/tag/cloudflare-access/)
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



[Remote Browser Isolation](https://blog.cloudflare.com/id-id/tag/remote-browser-isolation/)[SASE](https://blog.cloudflare.com/id-id/tag/sase/)

[CIO Week](https://blog.cloudflare.com/id-id/tag/cio-week/)[Clientless Web Isolation](https://blog.cloudflare.com/id-id/tag/clientless-web-isolation/)[Cloudflare Access](https://blog.cloudflare.com/id-id/tag/cloudflare-access/)[Remote Browser Isolation](https://blog.cloudflare.com/id-id/tag/remote-browser-isolation/)[SASE](https://blog.cloudflare.com/id-id/tag/sase/)

8 Desember 2021

# Memperkenalkan Isolasi Web Tanpa Klien

![Tim Obezuk](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW493E1Z2ETFY5MBFNHC8RJD.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Tim Obezuk](https://blog.cloudflare.com/id-id/author/tim-obezuk/)

5 menit dibaca

SALIN URL

Artikel ini juga tersedia dalam [English](https://blog.cloudflare.com/introducing-clientless-web-isolation-beta/), [日本語](https://blog.cloudflare.com/ja-jp/introducing-clientless-web-isolation-beta/), [简体中文](https://blog.cloudflare.com/zh-cn/introducing-clientless-web-isolation-beta/), dan [ภาษาไทย](https://blog.cloudflare.com/th-th/introducing-clientless-web-isolation-beta/).

![Introducing Clientless Web Isolation](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44XQ0N47Y3DJ17M77142MA.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA+vnj9fPg6+jb5+Pa7Oje8u7g7+va5ePP/fvk+PTh7efa6ODY7eTc8+re8era6OPQ//3n/Pbj8Ofb697X8OHa9ene9Ora7OXS///s//rn9eve7+HZ9OTc+uzg+O7e8OnW///w///s+vHj9enf+ezj//Pn/fTj9e/b///1///x//rq+/Tn//jr//3u//zq+fXg///4///1///v//zu///y///1///v/Prl///5///2///x///w///1///3///x/fzm)

Hari ini, kami dengan senang hati mengumumkan versi beta untuk isolasi web tanpa klien Cloudflare. Jalur baru untuk Isolasi Browser yang secara alami mengintegrasikan Zero Trust Network Access (ZTNA) dengan manfaat perlindungan zero-day, phishing, dan kehilangan data dari penelusuran jarak jauh untuk pengguna di perangkat apa pun yang menjelajahi situs web, aplikasi internal, atau aplikasi SaaS apa pun. Semua tanpa perlu menginstal perangkat lunak apa pun atau mengonfigurasi sertifikat apa pun di perangkat titik akhir.

### **Akses yang aman untuk perangkat yang dikelola dan tidak dikelola**

Pada awal tahun 2021, Cloudflare mengumumkan ketersediaan umum Isolasi Browser, browser jarak jauh yang cepat dan aman yang terintegrasi secara alami dengan platform Zero Trust Cloudflare. Platform ini — juga dikenal sebagai [Cloudflare for Teams](https://www.cloudflare.com/teams/) — menggabungkan akses Internet yang aman dengan solusi ([Gateway](https://www.cloudflare.com/teams/gateway/)) dan mengamankan akses aplikasi dengan solusi ZTNA ([Access](https://www.cloudflare.com/teams/access/)).

Biasanya, admin memberlakukan Isolasi Browser dengan meluncurkan klien perangkat Cloudflare di titik akhir, sehingga Cloudflare dapat berfungsi sebagai proxy Internet DNS dan HTTPS yang aman. Model ini melindungi pengguna dan aplikasi sensitif saat administrator mengelola perangkat tim mereka. Dan untuk pengguna akhir, pengalaman terasa tanpa gesekan seperti browser lokal: mereka hampir tidak menyadari bahwa sebenarnya mereka menjelajah di mesin aman yang berjalan pada pusat data Cloudflare di dekat mereka.

Integrasi Isolasi Browser dari ujung ke ujung dengan akses Internet yang aman memudahkan administrator untuk memberlakukan Isolasi Browser pada seluruh tim mereka tanpa pengguna menyadari bahwa mereka sebenarnya menjelajah di mesin yang aman pada pusat data Cloudflare terdekat. Namun, mengelola klien titik akhir dapat menambahkan biaya konfigurasi overhead untuk pengguna pada perangkat yang tidak dikelola, atau kontraktor pada perangkat yang dikelola oleh organisasi pihak ketiga.

Isolasi web tanpa klien Cloudflare menyederhanakan koneksi ke browser jarak jauh melalui hyperlink (misalnya: _https://.cloudflareaccess.com/browser_). Setelah pengguna diautentikasi melalui [penyedia identitas](https://developers.cloudflare.com/cloudflare-one/identity) yang didukung Cloudflare Access, browser pengguna akan menggunakan HTML5 untuk membuat koneksi latensi rendah ke browser jarak jauh yang dihosting di pusat data Cloudflare terdekat tanpa menginstal perangkat lunak apa pun. Tidak ada server untuk dikelola dan diskalakan, atau wilayah untuk dikonfigurasi.

### **Jelajahi tautan berisiko tinggi dengan aman**

Tindakan sederhana mengeklik tautan di email, atau situs web menyebabkan browser Anda mengunduh dan menjalankan muatan konten web aktif yang dapat mengeksploitasi ancaman zero-day yang tidak diketahui dan dapat membobol titik akhir.

Isolasi web tanpa klien Cloudflare dapat dimulai melalui URL awalan (misalnya, _https://.cloudflareaccess.com/browser/<https://www.example.com>_). Cukup dengan mengonfigurasi halaman pemblokiran khusus, gateway email, atau alat tiket Anda untuk mengawali tautan berisiko tinggi dengan Isolasi Browser akan secara otomatis mengirim klik berisiko tinggi ke browser jarak jauh, melindungi titik akhir dari setiap kode berbahaya yang mungkin ada pada tautan target.

Di sini, di Cloudflare, kami menggunakan produk Cloudflare untuk melindungi Cloudflare, dan pada kenyataannya, menggunakan pendekatan isolasi web tanpa klien ini untuk aktivitas investigasi keamanan kami sendiri. Dengan mengawali tautan berisiko tinggi menggunakan domain autentikasi kami, tim keamanan kami dapat menyelidiki situs web dan situs phishing yang berbahaya secara aman.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Screenshot of clientless web isolation homepage](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW480JPESVVFSNMDRRGHARG2.png&w=715&h=492&f=webp&fit=cover&position=center)

Tidak ada kode berisiko yang pernah mencapai perangkat karyawan, dan pada akhir penyelidikan mereka, browser jarak jauh dihentikan dan disetel ulang ke status bersih yang diketahui untuk penyelidikan berikutnya.

### **Akses Zero Trust terintegrasi dan penelusuran jarak jauh**

Saat data perusahaan hanya diakses dari perangkat yang dikelola, di dalam jaringan yang dikontrol dan telah lama berlalu. Perusahaan yang mengandalkan kontrol postur perangkat yang ketat untuk memverifikasi bahwa akses aplikasi hanya terjadi dari perangkat yang dikelola, hanya memiliki sedikit alat untuk mendapatkan dukungan tenaga kerja kontraktor atau BYOD. Secara historis, administrator telah mengatasi masalah ini dengan menerapkan lingkungan Virtual Desktop Infrastructure (VDI) yang mahal dan intensif sumber daya.

Selain itu, dalam hal mengamankan akses aplikasi, Cloudflare Access unggul dalam menerapkan kebijakan penolakan default yang paling rendah untuk aplikasi berbasis web, tanpa perlu menginstal perangkat lunak klien apa pun pada perangkat pengguna.

Isolasi web tanpa klien Cloudflare menambah kasus penggunaan ZTNA, memungkinkan aplikasi yang dilindungi oleh [Access dan Gateway](https://developers.cloudflare.com/cloudflare-one/tutorials/require-swg#build-a-gateway-rule-in-access) untuk memanfaatkan [kontrol perlindungan data](https://docs.google.com/document/d/1YzcoC5WVxCYtVSriZW0ETeTzX9HEVxjKXdAEGeND3l8/edit) Isolasi Browser seperti kontrol pencetakan lokal, clipboard, dan pembatasan unggah / unduh file untuk mencegah data sensitif ditransfer ke perangkat yang tidak dikelola.

Tautan terisolasi dapat dengan mudah ditambahkan ke [peluncur aplikasi](https://developers.cloudflare.com/cloudflare-one/applications/app-launcher) Access sebagai [bookmark](https://developers.cloudflare.com/cloudflare-one/applications/bookmarks) yang mengizinkan tim dan kontraktor Anda mengakses situs apa pun secara mudah dengan satu klik.

Terakhir, hanya karena browser jarak jauh mengurangi dampak pembobolan, tidak berarti browser tersebut harus memiliki akses tidak terkelola ke Internet. Semua traffic dari browser jarak jauh ke situs web target harus diamankan, diperiksa, dan dicatat oleh solusi SWG Cloudflare (Gateway) yang memastikan bahwa ancaman yang diketahui dapat difilter melalui kebijakan HTTP dan [pemindaian anti-virus](https://developers.cloudflare.com/cloudflare-one/policies/filtering/http-policies/antivirus-scanning).

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Screenshot of Access App Launcher bookmark linking to Browser Isolation](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45SJCQ79YVDD25DC0CZX00.png&w=715&h=482&f=webp&fit=cover&position=center)

### **Bergabunglah dengan isolasi web tanpa klien versi beta**

Isolasi web tanpa klien akan tersedia sebagai kemampuan bagi pelanggan Cloudflare for Teams yang telah menambahkan Isolasi Browser ke paket mereka. Kami akan segera membuka isolasi web tanpa klien Cloudflare untuk akses versi beta. Jika Anda tertarik untuk berpartisipasi, [daftar di sini](https://www.cloudflare.com/zero-trust/lp/clientless-web-isolation-beta/) untuk menjadi yang pertama mendengar kabar dari kami.

Kami senang dengan penelusuran aman dan aktivitas penggunaan akses aplikasi untuk model isolasi web tanpa klien kami. Sekarang, tim dari berbagai ukuran, dapat menghadirkan konektivitas Zero Trust tanpa batas ke perangkat yang tidak dikelola di mana pun di dunia.

Di halaman ini

Diskusikan Online

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fintroducing-clientless-web-isolation-beta%2F&t=Memperkenalkan%20Isolasi%20Web%20Tanpa%20Klien)[](https://x.com/intent/post?text=Memperkenalkan+Isolasi+Web+Tanpa+Klien&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fintroducing-clientless-web-isolation-beta%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fintroducing-clientless-web-isolation-beta%2F)[](https://bsky.app/intent/compose?text=Memperkenalkan+Isolasi+Web+Tanpa+Klien+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fintroducing-clientless-web-isolation-beta%2F)[](https://mastodonshare.com/?text=Memperkenalkan+Isolasi+Web+Tanpa+Klien&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fintroducing-clientless-web-isolation-beta%2F)[](https://www.threads.net/intent/post?text=Memperkenalkan+Isolasi+Web+Tanpa+Klien+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fintroducing-clientless-web-isolation-beta%2F)

## Tag terkait

[CIO Week](https://blog.cloudflare.com/id-id/tag/cio-week/)[Clientless Web Isolation](https://blog.cloudflare.com/id-id/tag/clientless-web-isolation/)[Cloudflare Access](https://blog.cloudflare.com/id-id/tag/cloudflare-access/)[Remote Browser Isolation](https://blog.cloudflare.com/id-id/tag/remote-browser-isolation/)[SASE](https://blog.cloudflare.com/id-id/tag/sase/)

Ikuti di Media Sosial

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Berlangganan untuk menerima pemberitahuan postingan baru

Alamat email

Kami tidak akan pernah membagikan alamat email Anda.

Berlangganan

Terima kasih telah berlangganan! Periksa kotak masuk Anda untuk mengonfirmasi.
