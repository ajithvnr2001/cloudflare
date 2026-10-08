---
url: https://blog.cloudflare.com/id-id/programmable-packet-filtering-with-magic-firewall/
title: Bagaimana Kami Menggunakan eBPF untuk Membangun Pemfilteran Paket yang Dapat Diprogram di Magic Firewall | Blog Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:46:15.631779+00:00
---

# Bagaimana Kami Menggunakan eBPF untuk Membangun Pemfilteran Paket yang Dapat Diprogram di Magic Firewall | Blog Cloudflare

> Source: https://blog.cloudflare.com/id-id/programmable-packet-filtering-with-magic-firewall/

[Blog](https://blog.cloudflare.com/id-id/)

[CIO Week](https://blog.cloudflare.com/id-id/tag/cio-week/)[eBPF](https://blog.cloudflare.com/id-id/tag/ebpf/)[Keamanan](https://blog.cloudflare.com/id-id/tag/security/)+3Tampilkan 3 tag lainnya

6 TagTampilkan 6 tag

  * Tag Post
  * [Keamanan](https://blog.cloudflare.com/id-id/tag/security/)
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



[Magic Firewall](https://blog.cloudflare.com/id-id/tag/magic-firewall/)[Magic Transit](https://blog.cloudflare.com/id-id/tag/magic-transit/)[VoIP](https://blog.cloudflare.com/id-id/tag/voip/)

[CIO Week](https://blog.cloudflare.com/id-id/tag/cio-week/)[eBPF](https://blog.cloudflare.com/id-id/tag/ebpf/)[Keamanan](https://blog.cloudflare.com/id-id/tag/security/)[Magic Firewall](https://blog.cloudflare.com/id-id/tag/magic-firewall/)[Magic Transit](https://blog.cloudflare.com/id-id/tag/magic-transit/)[VoIP](https://blog.cloudflare.com/id-id/tag/voip/)

6 Desember 2021

# Bagaimana Kami Menggunakan eBPF untuk Membangun Pemfilteran Paket yang Dapat Diprogram di Magic Firewall

![Chris J Arges](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4865BZM73VVEYNTQ0VZBR4.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Chris J Arges](https://blog.cloudflare.com/id-id/author/arges/)

6 menit dibaca

SALIN URL

Artikel ini juga tersedia dalam [English](https://blog.cloudflare.com/programmable-packet-filtering-with-magic-firewall/), [日本語](https://blog.cloudflare.com/ja-jp/programmable-packet-filtering-with-magic-firewall/), [简体中文](https://blog.cloudflare.com/zh-cn/programmable-packet-filtering-with-magic-firewall/), dan [ภาษาไทย](https://blog.cloudflare.com/th-th/programmable-packet-filtering-with-magic-firewall/).

![How We Used eBPF to Build Programmable Packet Filtering in Magic Firewall](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44K5JZN9SGZA4NJKEMXA99.png&w=1801&h=1013&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/////v3/9PLz7+vp8u3p9vLu8/Dv6+rs////////9fPz7+zo8e3n9fHt8/Hv7Ovt////////+Pf18e/p8u/n9fPs9PPw7u7w////////+/z59PPt9fPr+Pfw9/f08vP1////////////+vr0+vrz/f34/P379/j6///////////////8///9////////+/7/////////////////////////////////////////////////////////////////)

Cloudflare secara aktif melindungi layanan dari serangan canggih hari demi hari. Untuk pengguna Magic Transit, perlindungan DDoS mendeteksi dan menghentikan serangan, sementara [Magic Firewall](https://www.cloudflare.com/magic-firewall/) mengizinkan aturan tingkat paket khusus, memungkinkan pelanggan untuk tidak menggunakan perangkat firewall perangkat keras dan memblokir traffic berbahaya di jaringan Cloudflare. Jenis serangan dan kecanggihan serangan terus berkembang, seperti yang ditunjukkan oleh DDoS dan [serangan refleksi baru-baru ini](https://blog.cloudflare.com/id-id/attacks-on-voip-providers-id-id/) [terhadap](https://blog.cloudflare.com/update-on-voip-attacks/) layanan VoIP yang menargetkan protokol seperti [Session Initiation Protocol](https://en.wikipedia.org/wiki/Session_Initiation_Protocol) (SIP). Melawan serangan ini membutuhkan dorongan batas penyaringan paket di luar kemampuan firewall tradisional. Kami melakukan ini dengan mengambil teknologi kelas terbaik dan menggabungkannya dengan cara baru untuk mengubah Magic Firewall menjadi firewall yang sangat cepat dan dapat diprogram agar dapat bertahan bahkan dari serangan paling canggih sekalipun.

### **Magical Walls of Fire**

[Magic Firewall](https://blog.cloudflare.com/introducing-magic-firewall/) adalah firewall paket stateless terdistribusi yang dibangun di atas nftables Linux. Ini berjalan pada setiap server, di setiap pusat data Cloudflare di seluruh dunia. Untuk memberikan isolasi dan fleksibilitas, aturan nftables setiap pelanggan dikonfigurasi dalam namespace jaringan Linux mereka sendiri.

Diagram ini menunjukkan aktivitas contoh paket saat menggunakan [Magic Transit](https://blog.cloudflare.com/magic-transit-network-functions/), yang memiliki Magic Firewall bawaan. Pertama, paket masuk ke server dan perlindungan DDoS diterapkan, yang menghentikan serangan sedini mungkin. Selanjutnya, paket dirutekan ke namespace jaringan khusus pelanggan, yang menerapkan aturan nftables ke paket. Setelah ini, paket dirutekan kembali ke asal melalui terowongan GRE. Pengguna Magic Firewall dapat membuat pernyataan firewall dari [API tunggal](https://developers.cloudflare.com/magic-firewall), menggunakan [sintaks Wirefilter](https://github.com/cloudflare/wirefilter) yang fleksibel. Selain itu, aturan dapat dikonfigurasi melalui dasbor Cloudflare, menggunakan elemen seret dan lepas UI yang ramah.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![This diagram shows how packets are processed by Magic Firewall on a Cloudflare server.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48R9WMZ6CW711ZX84DH9QX.png&w=715&h=372&f=webp&fit=cover&position=center)

Magic Firewall menyediakan sintaks yang sangat kuat untuk pencocokan pada berbagai parameter paket, tetapi juga terbatas pada kecocokan yang disediakan oleh nftables. Meskipun hal tersebut lebih dari cukup untuk berbagai kasus penggunaan, Magic Firewall tidak memberikan fleksibilitas yang cukup untuk menerapkan penguraian paket lanjutan dan pencocokan konten yang kami inginkan. Kami membutuhkan lebih banyak kekuatan.

### **Halo eBPF, temui Nftables!**

Saat ingin menambahkan lebih banyak kekuatan untuk kebutuhan jaringan Linux Anda, Extended Berkeley Packet Filter ([eBPF](https://ebpf.io/)) adalah pilihan yang tepat. Dengan eBPF, Anda dapat menyisipkan program pemrosesan paket yang dijalankan _di kernel_ , memberi Anda fleksibilitas paradigma pemrograman yang sudah dikenal dengan kecepatan eksekusi di dalam kernel. Cloudflare [menyukai eBPF](https://blog.cloudflare.com/tag/ebpf/) dan teknologi ini telah mengubah banyak produk kami. Tentu saja, kami ingin menemukan cara untuk menggunakan eBPF guna memperluas penggunaan nftables di Magic Firewall. Ini berarti dapat mencocokkan dengan menggunakan program eBPF dalam tabel dan rantai sebagai aturan. Dengan melakukan ini, kita dapat memiliki kue dan memakannya juga, dengan menjaga infrastruktur dan kode yang ada, dan memperluasnya lebih jauh.

Jika nftables dapat memanfaatkan eBPF secara alami, cerita ini akan jauh lebih pendek; sayangnya, kami harus melanjutkan pencarian kami. Untuk memulai pencarian, kami tahu bahwa iptables terintegrasi dengan eBPF. Misalnya, seseorang dapat menggunakan iptables dan program eBPF yang disematkan untuk menjatuhkan paket dengan perintah berikut:

Petunjuk ini membantu menempatkan kami di jalan yang benar. Iptables menggunakan ekstensi [xt_bpf](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/net/netfilter/xt_bpf.c#n60) untuk dicocokkan dengan program eBPF. Ekstensi ini menggunakan jenis program eBPF BPF_PROG_TYPE_SOCKET_FILTER, yang memungkinkan kita memuat informasi paket dari buffer soket dan mengembalikan nilai berdasarkan kode kami.
    
    
    iptables -A INPUT -m bpf --object-pinned /sys/fs/bpf/match -j DROP

Karena kami tahu _iptables_ dapat menggunakan eBPF, mengapa tidak menggunakannya saja? Magic Firewall saat ini memanfaatkan nftables, yang merupakan pilihan tepat untuk kasus penggunaan kami karena fleksibilitasnya dalam sintaks dan antarmuka yang dapat diprogram. Jadi, kita perlu menemukan cara untuk menggunakan ekstensi xt_bpf dengan nftables.

Diagram [ini](https://developers.redhat.com/blog/2020/08/18/iptables-the-two-variants-and-their-relationship-with-nftables#using_iptables_nft) membantu menjelaskan hubungan antara iptables, nftables dan kernel. nftables API dapat digunakan oleh program iptables dan nft userspace, dan dapat mengonfigurasi kecocokan xtables (termasuk xt_bpf) dan kecocokan nftables normal.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-849 Embedded Image - BzET9q](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46K5HWGDGVFGANF0A6D7MF.png&w=715&h=536&f=webp&fit=cover&position=center)

Ini berarti bahwa dengan panggilan API yang tepat (pesan netlink/netfilter), kita dapat menyematkan kecocokan xt_bpf ke dalam aturan nftables. Untuk melakukan ini, kita perlu memahami pesan netfilter mana yang perlu kita kirim. Dengan menggunakan alat seperti strace, Wireshark, dan terutama menggunakan [sumber](https://github.com/torvalds/linux/blob/master/net/netfilter/xt_bpf.c) di mana kita dapat membuat pesan yang dapat menambahkan aturan eBPF dengan tabel dan rantai.

Struktur pesan netlink/netfilter untuk menambahkan kecocokan eBPF akan terlihat seperti contoh di atas. Tentu saja, pesan ini perlu disematkan dengan benar dan menyertakan langkah bersyarat, seperti putusan, ketika ada kecocokan. Langkah selanjutnya adalah penguraian kode format `ebpf_bytes` seperti yang ditunjukkan pada contoh di bawah ini.
    
    
    NFTA_RULE_TABLE table
    NFTA_RULE_CHAIN chain
    NFTA_RULE_EXPRESSIONS | NFTA_MATCH_NAME
    	NFTA_LIST_ELEM | NLA_F_NESTED
    	NFTA_EXPR_NAME "match"
    		NLA_F_NESTED | NFTA_EXPR_DATA
    		NFTA_MATCH_NAME "bpf"
    		NFTA_MATCH_REV 1
    		NFTA_MATCH_INFO ebpf_bytes	

Format byte dapat ditemukan dalam definisi header kernel dari [struct xt_bpf_info_v1](https://git.netfilter.org/iptables/tree/include/linux/netfilter/xt_bpf.h#n27). Contoh kode di atas menunjukkan bagian yang relevan dari struktur.
    
    
     struct xt_bpf_info_v1 {
    	__u16 mode;
    	__u16 bpf_program_num_elem;
    	__s32 fd;
    	union {
    		struct sock_filter bpf_program[XT_BPF_MAX_NUM_INSTR];
    		char path[XT_BPF_PATH_MAX];
    	};
    };

Modul xt_bpf mendukung bytecode mentah, serta jalur ke program ebpf yang disematkan. Modus selanjutnya adalah teknik yang kami gunakan untuk menggabungkan program ebpf dengan nftables.

Dengan informasi ini kami dapat menulis kode yang dapat membuat pesan netlink dan membuat serial dengan benar dari setiap bidang data yang relevan. Pendekatan ini hanyalah langkah pertama, kami juga sedang mempertimbangkan untuk memasukkan ini ke dalam alat yang tepat daripada mengirim pesan netfilter kustom.

### **Cukup tambahkan eBPF**

Sekarang kami perlu membuat program eBPF dan memuatnya ke dalam tabel dan rantai nftables yang ada. Mulai menggunakan eBPF bisa menjadi sedikit menakutkan. Jenis program mana yang ingin kami gunakan? Bagaimana kami mengkompilasi dan memuat program eBPF kami? Kami memulai proses ini dengan melakukan beberapa eksplorasi dan penelitian.

Pertama kami membuat program contoh untuk mencobanya.

Potongan skrip di atas adalah contoh program eBPF yang hanya menerima paket yang memiliki rangkaian ajaib di akhir payload. Ini memerlukan pemeriksaan total panjang paket untuk menemukan di mana memulai pencarian. Untuk kejelasan, contoh ini menghilangkan pemeriksaan kesalahan dan header.
    
    
    SEC("socket")
    int filter(struct __sk_buff *skb) {
      /* get header */
      struct iphdr iph;
      if (bpf_skb_load_bytes(skb, 0, &iph, sizeof(iph))) {
        return BPF_DROP;
      }
    
      /* read last 5 bytes in payload of udp */
      __u16 pkt_len = bswap_16(iph.tot_len);
      char data[5];
      if (bpf_skb_load_bytes(skb, pkt_len - sizeof(data), &data, sizeof(data))) {
        return BPF_DROP;
      }
    
      /* only packets with the magic word at the end of the payload are allowed */
      const char SECRET_TOKEN[5] = "xyzzy";
      for (int i = 0; i < sizeof(SECRET_TOKEN); i++) {
        if (SECRET_TOKEN[i] != data[i]) {
          return BPF_DROP;
        }
      }
    
      return BPF_OK;
    }

Setelah kami memiliki program, langkah selanjutnya adalah mengintegrasikannya ke dalam alat kami. Kami mencoba beberapa teknologi untuk memuat program, seperti BCC, libbpf, dan kami bahkan membuat pemuat khusus. Pada akhirnya, kami menggunakan [pustaka ebpf cilium](https://github.com/cilium/ebpf/), karena kami menggunakan Golang untuk program bidang kontrol dan pustaka memudahkan untuk menghasilkan, menyematkan, dan memuat program eBPF.

Setelah program dikompilasi dan disematkan, kami dapat menambahkan kecocokan ke dalam nftables menggunakan perintah netlink. Daftar aturan menunjukkan bahwa terdapat kecocokan. Ini luar biasa! Kami sekarang dapat memberlakukan program C khusus untuk menyediakan pencocokan tingkat lanjut di dalam kumpulan aturan Magic Firewall!
    
    
    # nft list ruleset
    table ip mfw {
    	chain input {
    		#match bpf pinned /sys/fs/bpf/mfw/match drop
    	}
    }

### **Lebih Banyak Keajaiban**

Dengan tambahan eBPF ke toolkit kami, Magic Firewall adalah cara yang lebih fleksibel dan kuat untuk melindungi jaringan Anda dari aktor jahat. Kami sekarang dapat melihat lebih dalam ke dalam paket dan menerapkan logika pencocokan yang lebih kompleks daripada yang dapat disediakan oleh nftables saja. Karena firewall kami berjalan sebagai perangkat lunak di semua server Cloudflare, kami dapat dengan cepat mengulangi dan memperbarui fitur.

Salah satu hasil dari proyek ini adalah perlindungan SIP, yang saat ini dalam versi beta. Itu hanya permulaan. Kami sedang menjajaki penggunaan eBPF untuk validasi protokol, pencocokan bidang lanjutan, melihat payload, dan mendukung kumpulan daftar IP yang lebih besar.

Kami juga menyambut bantuan Anda di sini! Jika Anda memiliki kasus penggunaan dan ide lain, harap diskusikan dengan tim akun Anda. Jika menurut Anda teknologi ini menarik, bergabunglah [dengan tim kami](https://www.cloudflare.com/careers/)!

Di halaman ini

Diskusikan Online

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fprogrammable-packet-filtering-with-magic-firewall%2F&t=Bagaimana%20Kami%20Menggunakan%20eBPF%20untuk%20Membangun%20Pemfilteran%20Paket%20yang%20Dapat%20Diprogram%20di%20Magic%20Firewall)[](https://x.com/intent/post?text=Bagaimana+Kami+Menggunakan+eBPF+untuk+Membangun+Pemfilteran+Paket+yang+Dapat+Diprogram+di+Magic+Firewall&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fprogrammable-packet-filtering-with-magic-firewall%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fprogrammable-packet-filtering-with-magic-firewall%2F)[](https://bsky.app/intent/compose?text=Bagaimana+Kami+Menggunakan+eBPF+untuk+Membangun+Pemfilteran+Paket+yang+Dapat+Diprogram+di+Magic+Firewall+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fprogrammable-packet-filtering-with-magic-firewall%2F)[](https://mastodonshare.com/?text=Bagaimana+Kami+Menggunakan+eBPF+untuk+Membangun+Pemfilteran+Paket+yang+Dapat+Diprogram+di+Magic+Firewall&url=https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fprogrammable-packet-filtering-with-magic-firewall%2F)[](https://www.threads.net/intent/post?text=Bagaimana+Kami+Menggunakan+eBPF+untuk+Membangun+Pemfilteran+Paket+yang+Dapat+Diprogram+di+Magic+Firewall+https%3A%2F%2Fblog.cloudflare.com%2Fid-id%2Fprogrammable-packet-filtering-with-magic-firewall%2F)

## Tag terkait

[CIO Week](https://blog.cloudflare.com/id-id/tag/cio-week/)[eBPF](https://blog.cloudflare.com/id-id/tag/ebpf/)[Keamanan](https://blog.cloudflare.com/id-id/tag/security/)[Magic Firewall](https://blog.cloudflare.com/id-id/tag/magic-firewall/)[Magic Transit](https://blog.cloudflare.com/id-id/tag/magic-transit/)[VoIP](https://blog.cloudflare.com/id-id/tag/voip/)

Ikuti di Media Sosial

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Berlangganan untuk menerima pemberitahuan postingan baru

Alamat email

Kami tidak akan pernah membagikan alamat email Anda.

Berlangganan

Terima kasih telah berlangganan! Periksa kotak masuk Anda untuk mengonfirmasi.
