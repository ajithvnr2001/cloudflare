---
url: https://blog.cloudflare.com/th-th/programmable-packet-filtering-with-magic-firewall/
title: \u0e27\u0e34\u0e18\u0e35\u0e17\u0e35\u0e48\u0e40\u0e23\u0e32\u0e43\u0e0a\u0e49 eBPF \u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e2a\u0e23\u0e49\u0e32\u0e07\u0e01\u0e32\u0e23\u0e01\u0e23\u0e2d\u0e07\u0e41\u0e1e\u0e47\u0e01\u0e40\u0e01\u0e47\u0e15\u0e17\u0e35\u0e48\u0e15\u0e31\u0e49\u0e07\u0e42\u0e1b\u0e23\u0e41\u0e01\u0e23\u0e21\u0e44\u0e14\u0e49\u0e43\u0e19 Magic Firewall | \u0e1a\u0e25\u0e47\u0e2d\u0e01 Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:46:15.026181+00:00
---

# วิธีที่เราใช้ eBPF เพื่อสร้างการกรองแพ็กเก็ตที่ตั้งโปรแกรมได้ใน Magic Firewall | บล็อก Cloudflare

> Source: https://blog.cloudflare.com/th-th/programmable-packet-filtering-with-magic-firewall/

[บล็อก](https://blog.cloudflare.com/th-th/)

[CIO Week](https://blog.cloudflare.com/th-th/tag/cio-week/)[eBPF](https://blog.cloudflare.com/th-th/tag/ebpf/)[Magic Firewall](https://blog.cloudflare.com/th-th/tag/magic-firewall/)+3แสดงแท็กเพิ่มเติม 3 รายการ

6 แท็กแสดง 6 แท็ก

  * แท็กของโพสต์
  * [ความปลอดภัย](https://blog.cloudflare.com/th-th/tag/security/)
  * แท็กทั้งหมด
  * แท็กที่ตรงกัน
  * ไม่พบแท็ก
  * [AI](https://blog.cloudflare.com/th-th/tag/ai/)
  * [สัปดาห์เกิด](https://blog.cloudflare.com/th-th/tag/birthday-week/)
  * [Bot Management](https://blog.cloudflare.com/th-th/tag/bot-management/)
  * [ไม่ใช้ไคลเอ็นต์](https://blog.cloudflare.com/th-th/tag/clientless/)
  * [Cloudflare Access](https://blog.cloudflare.com/th-th/tag/cloudflare-access/)
  * [Cloudflare Gateway](https://blog.cloudflare.com/th-th/tag/gateway/)
  * [Cloudflare Tunnel](https://blog.cloudflare.com/th-th/tag/cloudflare-tunnel/)
  * [วิทยาการเข้ารหัสลับ](https://blog.cloudflare.com/th-th/tag/cryptography/)
  * [DDoS](https://blog.cloudflare.com/th-th/tag/ddos/)
  * [รายงาน DDoS](https://blog.cloudflare.com/th-th/tag/ddos-reports/)
  * [นักพัฒนา](https://blog.cloudflare.com/th-th/tag/developers/)
  * [DNS (TH)](https://blog.cloudflare.com/th-th/tag/dns/)
  * [dosd (TH)](https://blog.cloudflare.com/th-th/tag/dosd/)
  * [ผลกระทบ](https://blog.cloudflare.com/th-th/tag/impact/)
  * [ชีวิตที่ Cloudflare](https://blog.cloudflare.com/th-th/tag/life-at-cloudflare/)
  * [พันธมิตร](https://blog.cloudflare.com/th-th/tag/partners/)
  * [นโยบายและกฎหมาย](https://blog.cloudflare.com/th-th/tag/policy/)
  * [โพสต์ควอนตัม](https://blog.cloudflare.com/th-th/tag/post-quantum/)
  * [ข่าวผลิตภัณฑ์](https://blog.cloudflare.com/th-th/tag/product-news/)
  * [Project Galileo](https://blog.cloudflare.com/th-th/tag/project-galileo/)
  * [Radar](https://blog.cloudflare.com/th-th/tag/cloudflare-radar/)
  * [ความปลอดภัย](https://blog.cloudflare.com/th-th/tag/security/)
  * [Security Week](https://blog.cloudflare.com/th-th/tag/security-week/)
  * [ความเร็วและความน่าเชื่อถือ](https://blog.cloudflare.com/th-th/tag/speed-and-reliability/)
  * [Zero Trust](https://blog.cloudflare.com/th-th/tag/zero-trust/)



[Magic Transit](https://blog.cloudflare.com/th-th/tag/magic-transit/)[VoIP](https://blog.cloudflare.com/th-th/tag/voip/)[ความปลอดภัย](https://blog.cloudflare.com/th-th/tag/security/)

[CIO Week](https://blog.cloudflare.com/th-th/tag/cio-week/)[eBPF](https://blog.cloudflare.com/th-th/tag/ebpf/)[Magic Firewall](https://blog.cloudflare.com/th-th/tag/magic-firewall/)[Magic Transit](https://blog.cloudflare.com/th-th/tag/magic-transit/)[VoIP](https://blog.cloudflare.com/th-th/tag/voip/)[ความปลอดภัย](https://blog.cloudflare.com/th-th/tag/security/)

6 ธันวาคม 2564

# วิธีที่เราใช้ eBPF เพื่อสร้างการกรองแพ็กเก็ตที่ตั้งโปรแกรมได้ใน Magic Firewall

![Chris J Arges](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4865BZM73VVEYNTQ0VZBR4.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Chris J Arges](https://blog.cloudflare.com/th-th/author/arges/)

อ่าน 2 นาที

คัดลอก URL

โพสต์นี้มีให้อ่านใน [English](https://blog.cloudflare.com/programmable-packet-filtering-with-magic-firewall/) [日本語](https://blog.cloudflare.com/ja-jp/programmable-packet-filtering-with-magic-firewall/) [简体中文](https://blog.cloudflare.com/zh-cn/programmable-packet-filtering-with-magic-firewall/) และ[Bahasa Indonesia](https://blog.cloudflare.com/id-id/programmable-packet-filtering-with-magic-firewall/).

![How We Used eBPF to Build Programmable Packet Filtering in Magic Firewall](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44K5JZN9SGZA4NJKEMXA99.png&w=1801&h=1013&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/////v3/9PLz7+vp8u3p9vLu8/Dv6+rs////////9fPz7+zo8e3n9fHt8/Hv7Ovt////////+Pf18e/p8u/n9fPs9PPw7u7w////////+/z59PPt9fPr+Pfw9/f08vP1////////////+vr0+vrz/f34/P379/j6///////////////8///9////////+/7/////////////////////////////////////////////////////////////////)

Cloudflare ปกป้องบริการจากการโจมตีที่ซับซ้อนทุกวัน สำหรับผู้ใช้ Magic Transit นั้น การป้องกัน DDoS จะตรวจจับและลดการโจมตี ในขณะที่ [Magic Firewall](https://www.cloudflare.com/magic-firewall/) อนุญาตให้มีการตั้งกฎระดับแพ็กเก็ตในแบบที่ต้องการ ทำให้ลูกค้าสามารถเลิกใช้งานอุปกรณ์ฮาร์ดแวร์ไฟร์วอลล์และปิดกั้นการรับส่งข้อมูลที่เป็นอันตรายภายในเครือข่ายของ Cloudflare บริษัทยังคงพัฒนาประเภทของการโจมตีและความซับซ้อนของการโจมตีต่อไป เช่นที่แสดงให้เห็นจาก DDoS และ Reflection [การ](https://blog.cloudflare.com/th-th/attacks-on-voip-providers-th-th/) โจมตีผให้บริการ VoIP ที่เล็งเป้าไปที่โปรโตคอล เช่น [Session Initiation Protocol](https://en.wikipedia.org/wiki/Session_Initiation_Protocol) (SIP) การต่อสู้กับการโจมตีเหล่านี้จำเป็นต้องผลักดันขีดจำกัดของการกรองแพ็กเก็ตให้มากกว่าที่ไฟร์วอลล์แบบเดิมจะสามารถทำได้ โดยเราได้นำเทคโนโลยีที่ดีที่สุดมารวมเข้าด้วยกันในรูปแบบใหม่เพื่อเปลี่ยน Magic Firewall ให้กลายเป็นไฟร์วอลล์ที่ตั้งค่าโปรแกรมได้อย่างรวดเร็วและเต็มรูปแบบ ซึ่งสามารถต้านทานการโจมตีที่ซับซ้อนที่สุดได้

### **กำแพงเวทย์มนตร์แห่งไฟ**

[Magic Firewall](https://blog.cloudflare.com/introducing-magic-firewall/) เป็นไฟร์วอลล์แพ็กเก็ตไร้สัญชาติแบบกระจายที่สร้างขึ้นบน Linux nftables ไฟร์วอลล์นี้ทำงานบนทุกเซิร์ฟเวอร์ ในศูนย์ข้อมูล Cloudflare ทุกแห่งทั่วโลก หากจะให้การแยกตัวและความยืดหยุ่น กฎ nftables ของลูกค้าแต่ละรายจะได้รับการกำหนดค่าภายในเนมสเปซเครือข่าย Linux ของตนเอง

ไดอะแกรมนี้แสดงอายุของแพ็กเก็ตตัวอย่างเมื่อใช้ [Magic Transit](https://blog.cloudflare.com/magic-transit-network-functions/) ซึ่งมี Magic Firewall ในตัว อันดับแรก แพ็กเก็ตจะเข้าสู่เซิร์ฟเวอร์และการป้องกัน DDoS จะถูกนำมาใช้ ซึ่งจะลดการโจมตีให้เร็วที่สุด หลังจากนั้น แพ็กเก็ตจะถูกส่งไปยังเนมสเปซเครือข่ายเฉพาะลูกค้า ซึ่งใช้กฎ nftables กับแพ็กเก็ต แล้วแพ็กเก็ตก็จะถูกส่งกลับไปยังต้นทางผ่าน GRE tunnel โดยผู้ใช้ Magic Firewall สามารถสร้างคำสั่งไฟร์วอลล์จาก [API เดียว](https://developers.cloudflare.com/magic-firewall)ด้วย[ซินแท็กซ์ Wirefilter](https://github.com/cloudflare/wirefilter) ที่ยืดหยุ่น นอกจากนี้ กฎยังสามารถกำหนดค่าได้ผ่านแดชบอร์ด Cloudflare โดยใช้องค์ประกอบการลากและวาง UI ที่ใช้งานได้ง่าย

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![This diagram shows how packets are processed by Magic Firewall on a Cloudflare server.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48R9WMZ6CW711ZX84DH9QX.png&w=715&h=372&f=webp&fit=cover&position=center)

Magic Firewall ให้ซินแท็กซ์ที่ทรงพลังมากสำหรับการจับคู่กับพารามิเตอร์แพ็กเก็ตต่าง ๆ แต่ยังจำกัดเฉพาะการจับคู่ที่ให้โดย nftables แม้ว่าสิ่งนี้จะมากเกินพอสำหรับกรณีการใช้งานจำนวนมาก แต่ก็ไม่ได้ให้ความยืดหยุ่นเพียงพอเมื่อต้องแยกวิเคราะห์แพ็กเก็ตขั้นสูงและจับคู่เนื้อหาที่เราต้องการ เราต้องการพลังมากกว่าเดิม

### **สวัสดี eBPF ขอเชิญพบกับ Nftables!**

เมื่อต้องการเพิ่มพลังให้กับความต้องการเครือข่าย Linux ของคุณ Extended Berkeley Packet Filter ([eBPF](https://ebpf.io/)) เป็นตัวเลือกที่เป็นธรรมชาติ เพราะด้วย eBPF คุณสามารถแทรกโปรแกรมประมวลผลแพ็กเก็ตที่รัน_ในเคอร์เนล_ ให้ความยืดหยุ่นของกระบวนทัศน์การเขียนโปรแกรมที่คุ้นเคยด้วยความเร็วของการดำเนินการในเคอร์เนล ทั้งนี้ Cloudflare [ชื่นชอบ eBPF](https://blog.cloudflare.com/tag/ebpf/) และเทคโนโลยีนี้ได้รับการเปลี่ยนแปลงเมื่อเปิดใช้งานผลิตภัณฑ์มากมายของเรา เราต้องการหาวิธีใช้ eBPF ให้ได้อย่างเป็นธรรมชาติเพื่อขยายการใช้งาน nftables ใน Magic Firewall ซึ่งจะทำให้เราสามารถจับคู่ได้โดยใช้โปรแกรม eBPF ภายในตารางและโซ่เป็นกฎ การทำเช่นนี้เหมือนกับว่าเรามีเค้กเป็นของเราเอง และกินเองด้วยโดยการรักษาโครงสร้างพื้นฐานและโค้ดที่มีอยู่ของเราไว้ และขยายออกไปมากขึ้นอีก

หาก nftables สามารถใช้ประโยชน์จาก eBPF ได้จริง เรื่องนี้จะสั้นกว่านี้มาก เพราะงั้น เราต้องทำภารกิจกันต่อไป การที่เรารู้ว่า iptables ทำงานร่วมกับ eBPF คือจุดเริ่มต้นของภารกิจดังกล่าว ตัวอย่างเช่น เราสามารถใช้ iptables และโปรแกรม eBPF ที่ปักหมุดไว้เพื่อวางแพ็กเก็ตด้วยคำสั่งต่อไปนี้:

เงื่อนงำนี้ช่วยให้เราอยู่บนเส้นทางที่ถูกต้อง Iptables ใช้ส่วนขยาย [xt_bpf](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/net/netfilter/xt_bpf.c#n60) เพื่อจับคู่ในโปรแกรม eBPF ส่วนขยายนี้ใช้ประเภทโปรแกรม BPF_PROG_TYPE_SOCKET_FILTER eBPF ซึ่งช่วยให้เราโหลดข้อมูลแพ็กเก็ตจากซ็อกเก็ตบัฟเฟอร์และส่งคืนค่าตามรหัสของเรา
    
    
    iptables -A INPUT -m bpf --object-pinned /sys/fs/bpf/match -j DROP

เรารู้ว่า iptables สามารถใช้ eBPF ได้ แล้วทำไมไม่ลองใช้ดูล่ะ ปัจจุบัน Magic Firewall ใช้ประโยชน์จาก nftables ซึ่งเป็นตัวเลือกที่ยอดเยี่ยมกับเคสการใช้งานของเราเพราะซินแท็กซ์มีความยืดหยุ่นและอินเทอร์เฟซก็เป็นแบบตั้งโปรแกรมได้ ดังนั้น เราจำเป็นต้องหาวิธีใช้ส่วนขยาย xt_bpf กับ nftables

[แผนผัง](https://developers.redhat.com/blog/2020/08/18/iptables-the-two-variants-and-their-relationship-with-nftables#using_iptables_nft)นี้ช่วยอธิบายความสัมพันธ์ระหว่าง iptables, nftables และเคอร์เนล ทั้งนี้ nftables API สามารถใช้ได้กับทั้งโปรแกรม iptables และ nft userspace และสามารถกำหนดค่าการจับคู่ xtables ทั้งสอง (รวมถึง xt_bpf) และการจับคู่ nftables ปกติ

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-849 Embedded Image - BzET9q](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46K5HWGDGVFGANF0A6D7MF.png&w=715&h=536&f=webp&fit=cover&position=center)

ซึ่งหมายความว่าเมื่อมีการเรียก API ที่ถูกต้อง (ข้อความ netlink/netfilter) เราสามารถฝังการจับคู่ xt_bpf ภายในกฎ nftables หากจะดำเนินการนี้ เราต้องเข้าใจว่าข้อความ netfilter ใดที่เราต้องส่ง ซึ่งเมื่อใช้เครื่องมือต่าง ๆ เช่น strace, Wireshark และโดยเฉพาะอย่างยิ่งการใช้ [source](https://github.com/torvalds/linux/blob/master/net/netfilter/xt_bpf.c) เราจะสามารถสร้างข้อความที่สามารถผนวกกฎ eBPF ให้กับตารางและเชนได้

โครงสร้างของข้อความ netlink/netfilter เพื่อเพิ่มการจับคู่ eBPF ควรมีลักษณะเหมือนตัวอย่างด้านบน ซึ่งแน่นอนว่าข้อความนี้จำเป็นต้องฝังอย่างถูกต้องและรวมขั้นตอนที่มีเงื่อนไข เช่น verdict เมื่อมีคำที่ตรงกัน ขั้นตอนถัดไปคือการถอดรหัสรูปแบบของ "ebpf_bytes" ตามที่แสดงในตัวอย่างด้านล่าง
    
    
    NFTA_RULE_TABLE table
    NFTA_RULE_CHAIN chain
    NFTA_RULE_EXPRESSIONS | NFTA_MATCH_NAME
    	NFTA_LIST_ELEM | NLA_F_NESTED
    	NFTA_EXPR_NAME "match"
    		NLA_F_NESTED | NFTA_EXPR_DATA
    		NFTA_MATCH_NAME "bpf"
    		NFTA_MATCH_REV 1
    		NFTA_MATCH_INFO ebpf_bytes	

ดูรูปแบบไบต์ได้จากคำจำกัดความของส่วนหัวเคอร์เนลของ [struct xt_bpf_info_v1](https://git.netfilter.org/iptables/tree/include/linux/netfilter/xt_bpf.h#n27) ตัวอย่างโค้ดด้านบนแสดงส่วนที่เกี่ยวข้องของโครงสร้าง
    
    
     struct xt_bpf_info_v1 {
    	__u16 mode;
    	__u16 bpf_program_num_elem;
    	__s32 fd;
    	union {
    		struct sock_filter bpf_program[XT_BPF_MAX_NUM_INSTR];
    		char path[XT_BPF_PATH_MAX];
    	};
    };

โมดูล xt_bpf รองรับทั้ง bytecodes ดิบและเส้นทางไปยังโปรแกรม ebpf ที่ปักหมุดไว้ โหมดต่อมาคือเทคนิคที่เราใช้ในการรวมโปรแกรม ebpf กับ nftables

เราสามารถใช้ข้อมูลนี้เพื่อเขียนโค้ดที่สามารถสร้างข้อความ netlink และจัดลำดับช่องข้อมูลที่เกี่ยวข้องได้อย่างถูกต้อง แนวทางนี้เป็นเพียงขั้นตอนแรก เรากำลังพิจารณาที่จะรวมสิ่งนี้เข้ากับเครื่องมือที่เหมาะสม แทนที่จะส่งข้อความ netfilter ที่กำหนดเอง

### **แค่เพิ่ม eBPF**

ตอนนี้ เราต้องสร้างโปรแกรม eBPF และโหลดลงในตาราง nftables และเชนที่มีอยู่ การเริ่มใช้ eBPF อาจสร้างความกังวลเล็กน้อย เราต้องการใช้โปรแกรมประเภทใด เราจะคอมไพล์และโหลดโปรแกรม eBPF ได้อย่างไร เราเริ่มกระบวนการนี้โดยทำการสำรวจและวิจัย

ขั้นแรก เราสร้างโปรแกรมตัวอย่างเพื่อทดลองใช้เองก่อน

ข้อความที่ตัดตอนมาเป็นตัวอย่างของโปรแกรม eBPF ที่ยอมรับเฉพาะแพ็กเก็ตที่มีแมจิคสตริงต่อท้ายเพย์โหลด ซึ่งต้องตรวจสอบความยาวรวมของแพ็กเก็ตเพื่อค้นหาตำแหน่งที่จะเริ่มต้นการค้นหา กล่าวให้ชัดคือ ตัวอย่างนี้ละเว้นการตรวจสอบข้อผิดพลาดและส่วนหัว
    
    
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

เมื่อเรามีโปรแกรมแล้ว ขั้นตอนต่อไปคือการผสานโปรแกรมเข้ากับเครื่องมือของเรา เราลองใช้เทคโนโลยีสองสามอย่างเพื่อโหลดโปรแกรม เช่น BCC, libbpf และเรายังสร้างตัวโหลดแบบกำหนดเองอีกด้วย ท้ายที่สุด เราจะได้ใช้[ไลบรารี ebpf ของ cilium](https://github.com/cilium/ebpf/) เนื่องจากเราใช้ Golang สำหรับโปรแกรมควบคุมระนาบของเรา และไลบรารีทำให้ง่ายต่อการสร้าง ฝัง และโหลดโปรแกรม eBPF

เมื่อคอมไพล์และปักหมุดโปรแกรมแล้ว เราก็ใช้คำสั่ง netlink เพื่อเพิ่มรายการที่ตรงกันลงใน nftables การแสดงรายการชุดกฎแสดงว่ามีรายการที่ตรงกัน ซึ่งเหลือเชื่อมาก! ขณะนี้ เราสามารถปรับใช้โปรแกรม C แบบกำหนดเองเพื่อให้การจับคู่ขั้นสูงภายในชุดกฎของ Magic Firewall!
    
    
    # nft list ruleset
    table ip mfw {
    	chain input {
    		#match bpf pinned /sys/fs/bpf/mfw/match drop
    	}
    }

### **Magic เพิ่มเติม**

เมื่อเพิ่ม eBPF ในชุดเครื่องมือของเรา ทำให้ Magic Firewall เป็นวิธีที่ยืดหยุ่นและมีประสิทธิภาพยิ่งขึ้นไปอีก ในการปกป้องเครือข่ายของคุณจากผู้ไม่หวังดี ตอนนี้เราสามารถพิจารณารายละเอียดของแพ็กเก็ตและใช้ตรรกะการจับคู่ที่ซับซ้อนกว่าที่ nftables เท่านั้นที่ทำได้ และเนื่องจากไฟร์วอลล์ของเราทำงานเป็นซอฟต์แวร์บนเซิร์ฟเวอร์ Cloudflare ทั้งหมด เราจึงสามารถทำซ้ำและอัปเดตคุณสมบัติต่าง ๆ ได้อย่างรวดเร็ว

ผลลัพธ์หนึ่งของโครงการนี้คือการป้องกัน SIP ซึ่งขณะนี้อยู่ในรุ่นเบต้า นั่นเป็นเพียงจุดเริ่มต้นเท่านั้น เรากำลังสำรวจการใช้ eBPF เพื่อตรวจสอบความถูกต้องของโปรโตคอล การจับคู่ช่องข้อมูลขั้นสูง การดูเพย์โหลด และการสนับสนุนแม้แต่ชุดของรายการ IP ที่ใหญ่ขึ้น

เรายินดีรับความช่วยเหลือของคุณที่นี่เช่นกัน! หากคุณมีกรณีการใช้งานและแนวคิดอื่น ๆ โปรดพูดคุยกับทีมดูแลลูกค้าของเรา หากคุณพบว่าเทคโนโลยีนี้น่าสนใจ [มาร่วมทีมกับเรา](https://www.cloudflare.com/careers/)!

[**หารือกันบน Twitter**](https://twitter.com/intent/tweet?in_reply_to=1467870195343634433) [**หารือกันบน Hacker News**](https://news.ycombinator.com/item?id=29459826) [**หารือกันบน Reddit**](https://reddit.com/r/CloudFlare/comments/ra8cno/how_we_used_ebpf_to_build_programmable_packet/)

[CIO Week](https://blog.cloudflare.com/tag/cio-week/) [Magic Firewall](https://blog.cloudflare.com/tag/magic-firewall/) [Magic Transit](https://blog.cloudflare.com/tag/magic-transit/) [Security](https://blog.cloudflare.com/tag/security/) [VoIP](https://blog.cloudflare.com/tag/voip/)

ติดตามบน Twitter

Chris J Arges |[@ChrisArges](https://twitter.com/@ChrisArges)

Cloudflare |[Cloudflare](https://twitter.com/Cloudflare)

ในหน้านี้

สนทนาออนไลน์

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fprogrammable-packet-filtering-with-magic-firewall%2F&t=%E0%B8%A7%E0%B8%B4%E0%B8%98%E0%B8%B5%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B9%80%E0%B8%A3%E0%B8%B2%E0%B9%83%E0%B8%8A%E0%B9%89%20eBPF%20%E0%B9%80%E0%B8%9E%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%AA%E0%B8%A3%E0%B9%89%E0%B8%B2%E0%B8%87%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%81%E0%B8%A3%E0%B8%AD%E0%B8%87%E0%B9%81%E0%B8%9E%E0%B9%87%E0%B8%81%E0%B9%80%E0%B8%81%E0%B9%87%E0%B8%95%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B8%95%E0%B8%B1%E0%B9%89%E0%B8%87%E0%B9%82%E0%B8%9B%E0%B8%A3%E0%B9%81%E0%B8%81%E0%B8%A3%E0%B8%A1%E0%B9%84%E0%B8%94%E0%B9%89%E0%B9%83%E0%B8%99%20Magic%20Firewall)[](https://x.com/intent/post?text=%E0%B8%A7%E0%B8%B4%E0%B8%98%E0%B8%B5%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B9%80%E0%B8%A3%E0%B8%B2%E0%B9%83%E0%B8%8A%E0%B9%89+eBPF+%E0%B9%80%E0%B8%9E%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%AA%E0%B8%A3%E0%B9%89%E0%B8%B2%E0%B8%87%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%81%E0%B8%A3%E0%B8%AD%E0%B8%87%E0%B9%81%E0%B8%9E%E0%B9%87%E0%B8%81%E0%B9%80%E0%B8%81%E0%B9%87%E0%B8%95%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B8%95%E0%B8%B1%E0%B9%89%E0%B8%87%E0%B9%82%E0%B8%9B%E0%B8%A3%E0%B9%81%E0%B8%81%E0%B8%A3%E0%B8%A1%E0%B9%84%E0%B8%94%E0%B9%89%E0%B9%83%E0%B8%99+Magic+Firewall&url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fprogrammable-packet-filtering-with-magic-firewall%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fprogrammable-packet-filtering-with-magic-firewall%2F)[](https://bsky.app/intent/compose?text=%E0%B8%A7%E0%B8%B4%E0%B8%98%E0%B8%B5%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B9%80%E0%B8%A3%E0%B8%B2%E0%B9%83%E0%B8%8A%E0%B9%89+eBPF+%E0%B9%80%E0%B8%9E%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%AA%E0%B8%A3%E0%B9%89%E0%B8%B2%E0%B8%87%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%81%E0%B8%A3%E0%B8%AD%E0%B8%87%E0%B9%81%E0%B8%9E%E0%B9%87%E0%B8%81%E0%B9%80%E0%B8%81%E0%B9%87%E0%B8%95%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B8%95%E0%B8%B1%E0%B9%89%E0%B8%87%E0%B9%82%E0%B8%9B%E0%B8%A3%E0%B9%81%E0%B8%81%E0%B8%A3%E0%B8%A1%E0%B9%84%E0%B8%94%E0%B9%89%E0%B9%83%E0%B8%99+Magic+Firewall+https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fprogrammable-packet-filtering-with-magic-firewall%2F)[](https://mastodonshare.com/?text=%E0%B8%A7%E0%B8%B4%E0%B8%98%E0%B8%B5%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B9%80%E0%B8%A3%E0%B8%B2%E0%B9%83%E0%B8%8A%E0%B9%89+eBPF+%E0%B9%80%E0%B8%9E%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%AA%E0%B8%A3%E0%B9%89%E0%B8%B2%E0%B8%87%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%81%E0%B8%A3%E0%B8%AD%E0%B8%87%E0%B9%81%E0%B8%9E%E0%B9%87%E0%B8%81%E0%B9%80%E0%B8%81%E0%B9%87%E0%B8%95%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B8%95%E0%B8%B1%E0%B9%89%E0%B8%87%E0%B9%82%E0%B8%9B%E0%B8%A3%E0%B9%81%E0%B8%81%E0%B8%A3%E0%B8%A1%E0%B9%84%E0%B8%94%E0%B9%89%E0%B9%83%E0%B8%99+Magic+Firewall&url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fprogrammable-packet-filtering-with-magic-firewall%2F)[](https://www.threads.net/intent/post?text=%E0%B8%A7%E0%B8%B4%E0%B8%98%E0%B8%B5%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B9%80%E0%B8%A3%E0%B8%B2%E0%B9%83%E0%B8%8A%E0%B9%89+eBPF+%E0%B9%80%E0%B8%9E%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%AA%E0%B8%A3%E0%B9%89%E0%B8%B2%E0%B8%87%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%81%E0%B8%A3%E0%B8%AD%E0%B8%87%E0%B9%81%E0%B8%9E%E0%B9%87%E0%B8%81%E0%B9%80%E0%B8%81%E0%B9%87%E0%B8%95%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B8%95%E0%B8%B1%E0%B9%89%E0%B8%87%E0%B9%82%E0%B8%9B%E0%B8%A3%E0%B9%81%E0%B8%81%E0%B8%A3%E0%B8%A1%E0%B9%84%E0%B8%94%E0%B9%89%E0%B9%83%E0%B8%99+Magic+Firewall+https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fprogrammable-packet-filtering-with-magic-firewall%2F)

## แท็กที่เกี่ยวข้อง

[CIO Week](https://blog.cloudflare.com/th-th/tag/cio-week/)[eBPF](https://blog.cloudflare.com/th-th/tag/ebpf/)[Magic Firewall](https://blog.cloudflare.com/th-th/tag/magic-firewall/)[Magic Transit](https://blog.cloudflare.com/th-th/tag/magic-transit/)[VoIP](https://blog.cloudflare.com/th-th/tag/voip/)[ความปลอดภัย](https://blog.cloudflare.com/th-th/tag/security/)

ติดตามบนโซเชียลมีเดีย

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## สมัครรับการแจ้งเตือนโพสต์ใหม่

อีเมล

เราจะไม่เปิดเผยอีเมลของคุณ

สมัคร

ขอบคุณที่สมัครรับข่าวสาร! โปรดตรวจสอบกล่องจดหมายเพื่อยืนยัน
