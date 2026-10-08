---
url: https://blog.cloudflare.com/th-th/magic-wan-firewall/
title: Magic WAN & Magic Firewall: \u0e01\u0e32\u0e23\u0e40\u0e0a\u0e37\u0e48\u0e2d\u0e21\u0e15\u0e48\u0e2d\u0e40\u0e04\u0e23\u0e37\u0e2d\u0e02\u0e48\u0e32\u0e22\u0e17\u0e35\u0e48\u0e1b\u0e25\u0e2d\u0e14\u0e20\u0e31\u0e22\u0e43\u0e19\u0e10\u0e32\u0e19\u0e30\u0e02\u0e2d\u0e07\u0e1a\u0e23\u0e34\u0e01\u0e32\u0e23 | \u0e1a\u0e25\u0e47\u0e2d\u0e01 Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:46:29.892338+00:00
---

# Magic WAN & Magic Firewall: การเชื่อมต่อเครือข่ายที่ปลอดภัยในฐานะของบริการ | บล็อก Cloudflare

> Source: https://blog.cloudflare.com/th-th/magic-wan-firewall/

[บล็อก](https://blog.cloudflare.com/th-th/)

[Cloudflare One](https://blog.cloudflare.com/th-th/tag/cloudflare-one/)[Firewall](https://blog.cloudflare.com/th-th/tag/firewall/)[Network](https://blog.cloudflare.com/th-th/tag/network/)+2แสดงแท็กเพิ่มเติม 2 รายการ

5 แท็กแสดง 5 แท็ก

  * แท็กของโพสต์
  * [Security Week](https://blog.cloudflare.com/th-th/tag/security-week/)[ข่าวผลิตภัณฑ์](https://blog.cloudflare.com/th-th/tag/product-news/)
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



[Security Week](https://blog.cloudflare.com/th-th/tag/security-week/)[ข่าวผลิตภัณฑ์](https://blog.cloudflare.com/th-th/tag/product-news/)

[Cloudflare One](https://blog.cloudflare.com/th-th/tag/cloudflare-one/)[Firewall](https://blog.cloudflare.com/th-th/tag/firewall/)[Network](https://blog.cloudflare.com/th-th/tag/network/)[Security Week](https://blog.cloudflare.com/th-th/tag/security-week/)[ข่าวผลิตภัณฑ์](https://blog.cloudflare.com/th-th/tag/product-news/)

22 มีนาคม 2564

# Magic WAN & Magic Firewall: การเชื่อมต่อเครือข่ายที่ปลอดภัยในฐานะของบริการ

![Achiel van der Mandele](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46PX2WV5KG8RYPQWH4Q50Q.png&w=64&h=64&f=webp&fit=cover&position=center)![Annika Garbers](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW485D91GWFS302KY7T9FVJF.png&w=64&h=64&f=webp&fit=cover&position=center)

[Achiel van der Mandele](https://blog.cloudflare.com/th-th/author/achiel/)และ[Annika Garbers](https://blog.cloudflare.com/th-th/author/annika/)

อ่าน 3 นาที

คัดลอก URL

โพสต์นี้มีให้อ่านใน [English](https://blog.cloudflare.com/magic-wan-firewall/) [Español](https://blog.cloudflare.com/es-es/magic-wan-firewall/) [日本語](https://blog.cloudflare.com/ja-jp/magic-wan-firewall/) [한국어](https://blog.cloudflare.com/ko-kr/magic-wan-firewall/) [繁體中文](https://blog.cloudflare.com/zh-tw/magic-wan-firewall/) [简体中文](https://blog.cloudflare.com/zh-cn/magic-wan-firewall/) และ[Bahasa Indonesia](https://blog.cloudflare.com/id-id/magic-wan-firewall/).

![Magic WAN & Magic Firewall: secure network connectivity as a service](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW480H37CXQZ2YVF4W0835D9.png&w=1200&h=628&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA+PD29fD27Ojt3tLT0LCsy56W0rWw3tfY/Pn9+ff67+/w49za2cW917ux3cnE5ODh////////9Pf16unj5dzS5tjO6uDb7Ort////////+v/88vXt8e/k9e/l9vLu9fT4////////////+f33+vvy//31//77/fz//////////////v/////7///+////////////////////////////////////////////////////////////////////////)

ย้อนกลับไปในเดือนตุลาคม 2020 เราได้เปิดตัว [Cloudflare One](https://blog.cloudflare.com/cloudflare-one/) ซึ่งก็คือวิสัยทัศน์ที่เรามีต่ออนาคตของเครือข่ายองค์กรและการรักษาความปลอดภัย และตั้งแต่นั้นเป็นต้นมา เราก็ได้มุ่งเน้นที่การนำเสนอส่วนต่าง ๆ ของแพลตฟอร์มนี้ และวันนี้เรารู้สึกตื่นเต้นที่จะประกาศองค์ประกอบที่เป็นพื้นฐานมากที่สุดสองประการ ได้แก่ [Magic WAN](https://www.cloudflare.com/th-th/magic-wan/) และ Magic Firewall ทั้งนี้ Magic WAN มาพร้อมกับการเชื่อมต่อและการกำหนดเส้นทางที่ปลอดภัยและมีประสิทธิภาพสำหรับเครือข่ายองค์กรทั้งหมดของคุณ ช่วยลดต้นทุนและความซับซ้อนในการปฏิบัติงาน ขณะที่ Magic Firewall ทำงานร่วมกับ Magic WAN ได้อย่างราบรื่น ทำให้คุณสามารถบังคับใช้นโยบายไฟร์วอลล์เครือข่าย หรือการรับส่งข้อมูลจากรายการใด ๆ ภายในเครือข่ายของคุณ

### สถาปัตยกรรมเครือข่ายแบบดั้งเดิมไม่ได้แก้ปัญหาในปัจจุบัน

เครือข่ายองค์กรได้นำรูปแบบใดรูปแบบหนึ่งมาใช้ ซึ่งได้รับการออกแบบมาเพื่อให้การเคลื่อนย้ายข้อมูลระหว่างสำนักงานและศูนย์ข้อมูลมีความปลอดภัย พร้อมการล็อคการเข้าถึงอินเทอร์เน็ต และจัดการภายในขอบเขตของสำนักงาน เมื่อแอปพลิเคชันย้ายไปยังระบบคลาวด์และพนักงานย้ายออกจากสำนักงาน การออกแบบเหล่านี้หยุดทำงาน และโซลูชันที่นำมาใช้ชั่วคราว เช่น กล่อง VPN ไม่ได้แก้ปัญหาหลักเกี่ยวกับสถาปัตยกรรมเครือข่ายขององค์กร

ในส่วนของการเชื่อมต่อนั้น เครือข่าย MPLS (multiprotocol label switching) แบบเต็มรูปแบบมีราคาแพงและต้องใช้เวลาในการปรับใช้ มีความท้าทายในการบำรุงรักษา ขยายแบบทวีคูณได้ยาก และมักมีช่องว่างในเรื่องการมองเห็นภาพรวมที่ไม่สามารถมองข้ามไปได้ สถาปัตยกรรมอื่น ๆ จำเป็นต้องมีการรับส่งข้อมูล backhauling ผ่านตำแหน่งศูนย์กลางก่อนที่จะส่งกลับไปยังต้นทาง ซึ่งทำให้เกิดผลเสียด้านเวลาหน่วงที่ยอมรับไม่ได้ และจำเป็นต้องซื้อฮาร์ดแวร์ฮับที่มีราคาแพงเพื่อให้ได้ความจุสูงสุดมากกว่าการใช้งานตามจริง และลูกค้าส่วนใหญ่ที่เราได้พูดคุยด้วยกำลังยุ่งอยู่กับปัญหาที่เลวร้ายที่สุดของทั้งสองโลก: การผสมผสานระหว่างสถาปัตยกรรมที่จัดการไม่ได้ซึ่งเชื่อมต่อเข้าด้วยกันมาตลอดเวลาหลายปีหรือหลายทศวรรษ สถาปนิกด้านความปลอดภัยยังต่อสู้กับโมเดลเหล่านี้ พวกเขาต้องเล่นกลกล่องฮาร์ดแวร์ความปลอดภัยจากผู้ขายหลายราย และพิจารณาสมดุลระหว่างต้นทุน ประสิทธิภาพ และความปลอดภัยเมื่อเครือข่ายเติบโตขึ้น

### ย้ายขอบเขตเครือข่ายของคุณไปยัง Edige และทำให้ปลอดภัยในฐานะบริการ

ด้วย Magic WAN คุณสามารถเชื่อมต่อแหล่งที่มาของการรับส่งข้อมูลได้อย่างปลอดภัย ไม่ว่าจะเป็นศูนย์ข้อมูล สำนักงาน อุปกรณ์ คุณสมบัติระบบคลาวด์ กับเครือข่ายของ Cloudflare และกำหนดค่านโยบายการกำหนดเส้นทางเพื่อรับบิตที่ต้องการ ทั้งหมดนี้รวมอยู่ในโซลูชัน SaaS เดียว Magic WAN รองรับ on-ramps ที่หลากหลาย รวมถึง [Anycast GRE tunnels](https://www.cloudflare.com/learning/network-layer/what-is-gre-tunneling/), [Cloudflare Network Interconnect](https://www.cloudflare.com/th-th/network-interconnect/), [Argo Tunnel](https://www.cloudflare.com/th-th/products/tunnel/), [WARP](https://blog.cloudflare.com/warp-for-desktop) และ [Network On-ramp Partners](https://blog.cloudflare.com/network-onramp-partnerships) แบบต่าง ๆ โดยไม่มีค่าใช้จ่ายสำหรับ MPLS หรือระยะเวลารอคอยอีกต่อไป ไม่มีผลเสียด้านประสิทธิภาพจากทรอมโบนการรับส่งข้อมูล และไม่ต้องเจอฝันร้ายในการจัดการโซลูชันรุ่นเก่าที่ยุ่งเหยิงอีกต่อไป: ใช้เครือข่าย Anycast ทั่วโลกของ Cloudflare เป็นส่วนขยายของคุณ และเปิดรับประสิทธิภาพและการมองเห็นภาพรวมที่ดีขึ้น

เมื่อการรับส่งข้อมูลของคุณเชื่อมต่อกับ Cloudflare แล้ว คุณจะควบคุมอย่างไร เพื่อจะกำหนดว่าจะให้เอนทิตีใดบ้างภายในเครือข่ายของคุณสามารถโต้ตอบระหว่างกัน หรือสามารถโต้ตอบกับอินเทอร์เน็ต? นี่คือที่มาของ Magic Firewall ทั้งนี้ Magic Firewall ช่วยให้คุณจัดการนโยบายทั่วทั้งเครือข่ายของคุณจาก Edge ในฐานะของบริการ Magic Firewall ช่วยให้คุณควบคุมได้อย่างละเอียดว่าจะอนุญาตให้ข้อมูลใดเข้าและออกจากเครือข่ายของคุณ หรือภายในเครือข่ายของคุณ ทั้งยังจะมองเห็นได้ดียิ่งขึ้นว่าการรับส่งข้อมูลผ่านเครือข่ายของคุณเป็นอย่างไรจากแดชบอร์ดเดียว

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Magic WAN & Magic Firewall: secure network connectivity as a service Embedded Image - kgBJAL](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45HDDRX2FXME3ANREM4FQ7.png&w=715&h=581&f=webp&fit=cover&position=center)

Magic WAN เป็นรากฐานของฟังก์ชันที่หลากหลายชุดหนึ่งที่รวมอยู่ใน Cloudflare One ซึ่งทั้งหมดนี้สร้างขึ้นในซอฟต์แวร์ตั้งแต่เริ่มต้น จนสามารถปรับขนาดและผสานรวมได้อย่างราบรื่น โดย Magic Firewall พร้อมนำมาใช้ประกอบกับ Magic WAN นอกกรอบ และลูกค้าสามารถเปิดใช้งานคุณสมบัติความปลอดภัยและประสิทธิภาพเพิ่มเติมของ Zero Trust ได้อย่างง่ายดาย เช่น [Secure Web Gateway](https://www.cloudflare.com/th-th/teams/) ของเราพร้อมการแยกเบราว์เซอร์ระยะไกล, [Intrusion Detection System](https://blog.cloudflare.com/one-more-zero-trust-thing-cloudflare-intrusion-detection/), Smart Routing และอีกมากมาย

>  _“ทีมเครือข่ายของเรารู้สึกตื่นเต้นกับ Magic WAN Cloudflare ได้สร้างแพลตฟอร์มเครือข่ายในฐานะบริการระดับโลกที่จะช่วยให้ทีมเครือข่ายจัดการสภาพแวดล้อม Edge และมัลติคลาวด์ที่ซับซ้อนได้อย่างมีประสิทธิภาพมากขึ้น การใช้งาน WAN เดียวทั่วโลกที่มีการรักษาความปลอดภัยในตัวและฟังก์ชันการกำหนดเส้นทางที่รวดเร็ว ไม่ว่าจะเป็นสำนักงานใหญ่ ศูนย์ข้อมูล สำนักงานสาขา หรือสถานที่ตั้งของผู้ใช้ปลายทาง ล้วนเป็นตัวเปลี่ยนเกมในเทคโนโลยี WAN”— Sander Petersson หัวหน้าฝ่ายโครงสร้างพื้นฐาน FlightRadar24_

หน้าตาเป็นอย่างไร มาสำรวจวิธีที่คุณสามารถใช้ Magic WAN และ Magic Firewall เพื่อแก้ปัญหาในระบบเครือข่ายและการรักษาความปลอดภัยภายในองค์กรผ่าน Acme Corp ซึ่งเป็นลูกค้าตัวอย่างกันเถอะ

### แทนที่ MPLS ระหว่างสำนักงานสาขาและศูนย์ข้อมูล

ปัจจุบัน Acme Corp มีสำนักงานทั่วโลกซึ่งแต่ละแห่งเชื่อมต่อกับศูนย์ข้อมูลระดับภูมิภาคและเชื่อมต่อกันผ่าน MPLS ศูนย์ข้อมูลแต่ละแห่งซึ่งโฮสต์แอปพลิเคชันขององค์กรและสแต็คกล่องฮาร์ดแวร์จำนวนมากเพื่อรักษาความปลอดภัย มีการเชื่อมต่อลีสไลน์กับศูนย์ข้อมูลอื่นอย่างน้อยหนึ่งแห่ง Acme กำลังโยกย้ายแอปพลิเคชันบางตัวไปยังระบบคลาวด์ และวางแผนสร้างการเชื่อมต่อโดยตรงจากศูนย์ข้อมูลของตนไปยังผู้ให้บริการระบบคลาวด์เพื่อเพิ่มความปลอดภัยและความน่าเชื่อถือ

เมื่อ Acme เติบโตขึ้น หนึ่งในจุดอ่อนที่เกิดขึ้นมาโดยตลอดของทีมเครือข่าย คือการจัดการและบำรุงรักษาการเชื่อมต่อ MPLS ของตนเอง มันมีราคาแพงและต้องใช้เวลานานในการปรับใช้ ซึ่งเป็นตัวจำกัดไม่ให้ Acme ขยายไปสู่สถานที่ใหม่ (โดยเฉพาะในต่างประเทศ) หรือไปยังสำนักงานสนับสนุนที่เพิ่มขึ้นจากการซื้อกิจการได้อย่างรวดเร็ว พนักงานในสำนักงานของ Acme ที่เชื่อมต่อกับผู้ให้บริการระบบคลาวด์และแอป SaaS ประสบกับเวลาหน่วงที่ชวนให้หงุดหงิด เนื่องจากการรับส่งข้อมูลเกิดติดขัดขณะผ่านศูนย์ข้อมูล Acme ที่บังคับใช้นโยบายความปลอดภัยผ่านสแต็คกล่องฮาร์ดแวร์ก่อนส่งไปยังปลายทาง การรับส่งข้อมูลระหว่างสำนักงาน เช่น ระบบโทรศัพท์ IP และการประชุมทางวิดีโอ ไม่มีนโยบายด้านความปลอดภัยใด ๆ ที่นำมาใช้ ทำให้รูปแบบความปลอดภัยของ Acme มีช่องโหว่

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Magic WAN & Magic Firewall: secure network connectivity as a service Embedded Image - QZOvId](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45CMSRQ82HD35J37SE39GP.png&w=715&h=590&f=webp&fit=cover&position=center)

Acme กำลังดำเนินการเปลี่ยนมาใช้ระบบคลาวด์สำหรับการประมวลผลและพื้นที่จัดเก็บ รวมถึงการย้ายออกจากลิงก์ส่วนตัวเหล่านี้และหันมาใช้ประโยชน์จากอินเทอร์เน็ตแทนเพื่อการเชื่อมต่ออย่างปลอดภัย พวกเขาพิจารณาที่จะสร้าง IPSec VPN tunnel แบบไซต์ต่อไซต์บนอินเทอร์เน็ต แต่ความซับซ้อนทำให้ทีมเครือข่ายของพวกเขาตึงเครียด รวมถึงการปรับใช้เราเตอร์ที่ต่างกัน Magic WAN พร้อมที่จะพบกับพวกเขาในที่ที่พวกเขาเป็นอยู่ในปัจจุบัน ทำให้การจัดการเครือข่ายง่ายขึ้น ให้ประโยชน์ด้านประสิทธิภาพในทันที และช่วยให้ Acme ค่อย ๆ ถอยออกมาจาก MPLS

ในตัวอย่างการปรับใช้ด้วย Magic WAN สิ่งที่เห็นคือ Acme เชื่อมต่อแต่ละสำนักงานและ VPC กับ Cloudflare ด้วย Anycast GRE tunnel ซึ่งเมื่อใช้สถาปัตยกรรมนี้ Acme จำเป็นต้องตั้งค่า tunnel เดี่ยว ๆ สำหรับแต่ละไซต์/การเชื่อมต่ออินเทอร์เน็ต เพื่อรับการเชื่อมต่อกับเครือข่ายทั่วโลกทั้งหมดของ Cloudflare โดยอัตโนมัติ (กว่า 200 เมืองในกว่า 100 ประเทศทั่วโลก) - เช่นเดียวกับสถาปัตยกรรม hub and spoke ยกเว้นฮับที่มีอยู่ทุกที่ Acme ยังเลือกสร้างการเชื่อมต่อส่วนตัวโดยเฉพาะจากศูนย์ข้อมูลของตนด้วย [Cloudflare Network Interconnect](https://www.cloudflare.com/th-th/network-interconnect/) ทำให้การรับส่งข้อมูลมีความปลอดภัยและเชื่อถือได้มากยิ่งขึ้นและการเชื่อมต่อที่ดีเยี่ยมกับเครือข่ายอื่นๆ / ผู้ให้บริการคลาวด์ผ่านเครือข่าย[ที่เชื่อมต่อถึงกันสูง](https://www.peeringdb.com/net/4224)ของ Cloudflare

เมื่อสร้าง tunnel เหล่านี้แล้ว Acme สามารถกำหนดค่าเส้นทางการรับส่งข้อมูลที่อนุญาตภายในเครือข่ายส่วนตัวของตน (พื้นที่ RFC 1918) และ Cloudflare รับการรับส่งข้อมูลในที่ที่ต้องไป โดยทำให้การรับส่งข้อมูลมีความยืดหยุ่นและมีประสิทธิภาพ เพราะขั้นตอนการตั้งค่าที่ง่ายดายซึ่งใช้เวลาเพียงไม่กี่ชั่วโมง ทำให้ Acme Corp สามารถเริ่มการย้ายข้อมูลออกจาก MPLS ได้ และประสิทธิภาพเครือข่ายและความน่าเชื่อถือของ Acme จะได้รับการปรับปรุงอย่างต่อเนื่องเมื่อมีการเปิดตัวความสามารถใหม่ ๆ ของ Cloudflare One เช่น QoS และ Argo for Networks

### รักษาความปลอดภัยให้พนักงานเข้าถึงเครือข่ายส่วนตัวจากระยะไกล

เมื่อพนักงานของ Acme Corp เปลี่ยนไปทำงานจากที่บ้านอย่างกะทันหันเมื่อปีที่แล้วเนื่องจากการแพร่ระบาดของ COVID-19 ฝ่ายไอทีของ Acme ต้องเร่งหาทางแก้ปัญหาในระยะสั้นเพื่อให้พนักงานสามารถเข้าถึงทรัพยากรภายในได้ VPN รุ่นเก่าไม่รองรับ พนักงานของ Acme ที่ทำงานจากที่บ้านประสบปัญหาด้านการเชื่อมต่อ ความน่าเชื่อถือ และประสิทธิภาพ เนื่องจากอุปกรณ์ถูกผลักดันให้ทำงานเกินขีดจำกัดที่ออกแบบมา

โชคดีที่ยังมีโซลูชันที่ดีกว่า! Acme Corp สามารถใช้ Cloudflare for Teams และ Magic WAN เพื่อให้พนักงานเข้าถึงทรัพยากรที่อยู่เบื้องหลังเครือข่ายส่วนตัวจากอุปกรณ์ของตนได้อย่างปลอดภัย ไม่ว่าพวกเขาจะทำงานจากที่ใด พนักงาน Acme ติดตั้งไคลเอนต์ WARP บนอุปกรณ์เพื่อส่งปริมาณข้อมูลไปยังเครือข่ายของ Cloudflare ซึ่งสามารถตรวจสอบและกำหนดเส้นทางไปยังทรัพยากรส่วนตัวภายในศูนย์ข้อมูลหรือ VPC ที่เชื่อมต่อกับ Cloudflare ผ่าน GRE tunnel (แสดงในตัวอย่างก่อนหน้านี้), Argo Tunnel Cloudflare Network Interconnect หรือ IPSec (เร็ว ๆ นี้) สถาปัตยกรรมนี้แก้ปัญหาด้านประสิทธิภาพและความจุที่ Acme ประสบกับ VPN รุ่นเก่า แทนที่จะส่งปริมาณข้อมูลทั้งหมดผ่านอุปกรณ์จุดควบคุมเดียว ระบบจะกำหนดเส้นทางไปยังตำแหน่ง Cloudflare ที่ใกล้ที่สุดซึ่งมีการนำนโยบายไปใช้ที่ Edge ก่อนส่งไปตามเส้นทางที่ปรับให้เหมาะสมไปยังปลายทาง

การรับส่งข้อมูลจากอุปกรณ์พนักงาน ศูนย์ข้อมูล และสำนักงานของ Acme Corp จะควบคุมด้วย Magic Firewall ได้เพื่อการควบคุมนโยบายที่ละเอียดและมีประสิทธิภาพ ซึ่งบังคับใช้กับ "เส้นทาง" ทั้งหมด ไม่ว่าพนักงานจะเชื่อมต่อจากโทรศัพท์และแล็ปท็อป หรือทำงานจากสำนักงานของ Acme นโยบายเดียวกันก็สามารถนำไปใช้ในที่เดียวกันได้ ลักษณะนี้ทำให้กำหนดค่าได้ง่ายขึ้นและปรับปรุงการมองเห็นภาพรวมของทีมไอทีและความปลอดภัยของ Acme ซึ่งจะสามารถล็อกเข้าสู่ระบบแดชบอร์ด Cloudflare เพื่อดูและควบคุมนโยบายได้ในที่เดียว ซึ่งเป็นตัวเปลี่ยนเกมเมื่อเทียบกับการจัดการการเข้าถึงของพนักงานผ่าน VPN, ไฟร์วอลล์ และบริการคลาวด์ต่าง ๆ

โซลูชันนี้ช่วยให้ Acme เปลี่ยนจาก VPN, ไฟร์วอลล์ และอุปกรณ์เกตเวย์เว็บที่ปลอดภัย ปรับปรุงประสิทธิภาพและเปิดใช้งานการจัดการนโยบายได้ง่าย ๆ เมื่อมีการรับส่งข้อมูลจากทุกที่ที่พนักงานทำงาน

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Magic WAN & Magic Firewall: secure network connectivity as a service Embedded Image - e4ROEK](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45DPZCT7WFGYNK68Z61WGD.png&w=715&h=284&f=webp&fit=cover&position=center)

### โอนย้ายฟังก์ชันเครือข่ายและความปลอดภัยไปที่ Edge

แต่เดิม Acme ใช้ชุดของอุปกรณ์ฮาร์ดแวร์ภายในสำนักงานและศูนย์ข้อมูลที่มีอยู่ ณ ขณะนั้นเพื่อบังคับใช้การรักษาความปลอดภัยเครือข่ายและเพิ่มการมองเห็นภาพรวมสิ่งที่เกิดขึ้นบนเครือข่าย: ไฟร์วอลล์เฉพาะเพื่อตรวจสอบการรับส่งข้อมูลขาเข้าหรือขาออก ระบบตรวจจับการบุกรุก และ SIEM ขณะที่บริษัทย้ายไปใช้ระบบคลาวด์และกลับมาทบทวนอนาคตของการทำงานระยะไกล ทีมรักษาความปลอดภัยของ Acme ก็มองหาโซลูชันที่ยั่งยืน ซึ่งปรับปรุงการรักษาความปลอดภัย แม้กระทั่งสิ่งที่เคยเป็นไปได้ในสถาปัตยกรรมแบบปราสาทและคูน้ำแบบเดิม

ก่อนหน้านี้ เราได้อธิบายวิธีที่ Acme สามารถกำหนดค่า Magic WAN เพื่อส่งปริมาณข้อมูลจากสำนักงาน ศูนย์ข้อมูล ทรัพย์สินบนระบบคลาวด์ และอุปกรณ์ไปยังเครือข่ายของ Cloudflare เมื่อปริมาณข้อมูลนี้ไหลผ่าน Cloudflare ทั้งการเพิ่มการควบคุมการเข้าถึงและฟังก์ชันการกรองเพื่อเพิ่มหรือเปลี่ยนฮาร์ดแวร์ความปลอดภัยภายในองค์กรจะทำได้ง่ายเมื่อส่งมอบและจัดการผ่านหน้าต่างกระจกบานเดียว

ลูกค้าสามารถใช้ Magic Firewall เพื่อรับบริการไฟร์วอลล์เดียวที่ทำงานที่ Edge แทนที่จะต้องใช้กล่องที่ยุ่งยากที่พวกเขาได้ติดตั้งไว้ที่สำนักงานสาขาหรือศูนย์ข้อมูล Magic Firewall ช่วยให้ลูกค้าจัดการการกำหนดค่าได้อย่างง่ายดาย และยังช่วยลดความยุ่งยากในการตรวจสอบการปฏิบัติตามข้อกำหนดอีกด้วย

หากต้องการควบคุมการเข้าถึง ลูกค้าสามารถกำหนดนโยบายที่ระบุอย่างชัดเจนว่าจะให้การรับส่งข้อมูลใดได้รับอนุญาตให้ไปที่ใด ตัวอย่างเช่น Acme ต้องการให้การรับส่งข้อมูลจากอินเทอร์เน็ตไปยังเว็บเซิร์ฟเวอร์ภายในศูนย์ข้อมูลบนพอร์ต 80 และ 443 แต่ต้องการจำกัดการเข้าถึง SSH ให้กับเครือข่ายส่วนตัวภายในสำนักงานสาขาเท่านั้น

หาก Acme ต้องการจำกัดการเข้าถึงเครือข่ายของตนต่อไป บริษัทสามารถใช้โมเดลการเข้าถึง Zero Trust ร่วมกับ [Access](https://www.cloudflare.com/th-th/teams/access/) และ [Gateway](https://www.cloudflare.com/th-th/teams/gateway/) เพื่อควบคุมบุคคลที่สามารถเข้าถึงสิ่งใดและวิธีการเข้าถึงสำหรับปริมาณข้อมูลทั้งหมดที่ไหลผ่านเครือข่าย Cloudflare เมื่อ Cloudflare เปิดตัวฟังก์ชันการกรองและการควบคุมใหม่ เช่น โซลูชัน IDS/IPS และ DLP ที่กำลังจะมีขึ้นของเรา Acme สามารถเปิดใช้งานโซลูชันเหล่านี้ด้วยการคลิกเพียงไม่กี่ครั้งเพื่อเพิ่มความปลอดภัย

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Magic WAN & Magic Firewall: secure network connectivity as a service Embedded Image - LJ3dM9](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46KME9H8MB480H1EWNHWHF.png&w=715&h=342&f=webp&fit=cover&position=center)

เป้าหมายระยะยาวของ Acme คือการถ่ายโอนฟังก์ชันการรักษาความปลอดภัยและการดำเนินงานทั้งหมดไปยังบริการระบบคลาวด์ และนำมาใช้ในฐานะของบริการ Magic WAN นำเสนอเส้นทางการโอนย้ายข้อมูลนี้ได้อย่างราบรื่น ทำให้ลูกค้าค่อย ๆ เพิ่มรูปแบบความปลอดภัยในขณะที่เลิกใช้ฮาร์ดแวร์รุ่นเก่า

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Magic WAN & Magic Firewall: secure network connectivity as a service Embedded Image - gUiM9w](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW464GY1KEAV29Z89W8FM1S6.png&w=715&h=422&f=webp&fit=cover&position=center)

>  _การปรับใช้คลาวด์ที่เพิ่มขึ้นพร้อมกับจุดหมุนล่าสุดสำหรับผู้ปฏิบัติงานระยะไกลได้เพิ่มปริมาณการรับส่งข้อมูลทางอินเทอร์เน็ต, SaaS และ IaaS ซึ่งทำให้สถาปัตยกรรมเครือข่ายแบบดั้งเดิม เช่น MPLS ต้องรับภาระหนัก สถาปัตยกรรม WAN ที่นำเสนอฟังก์ชันความปลอดภัยเครือข่ายระดับสากลแบบบูรณาการ และการเชื่อมต่อโดยตรงและปลอดภัยกับผู้ใช้ระยะไกลเป็นกุญแจสำคัญขององค์กรที่ต้องการเพิ่มความคล่องตัวในการดำเนินงานและลดต้นทุนโดยรวมในการเป็นเจ้าของ—Ghassan Abdo, รองประธานฝ่ายวิจัยของ IDC, WW Telecom, Virtualization & CDN_

### เครือข่าย Cloudflare คือส่วนขยายของเครือข่ายของคุณ

Cloudflare One เหมือนกับผลิตภัณฑ์มากมายของเราที่เริ่มต้นในฐานะของส่วนหนึ่งของชุดโซลูชันเพื่อแก้ไขปัญหาที่เราประสบขณะขยายกิจการและทำให้เครือข่ายของเราเองมีความปลอดภัย Magic WAN และ Magic Firewall ช่วยให้ลูกค้าของเราได้รับประโยชน์จากการตัดสินใจด้านสถาปัตยกรรมอย่างรอบคอบตลอดช่วงสิบปีที่ผ่านมา:

  * **ขนาดสากลและใกล้สายตา:** ไม่ว่าสำนักงาน ศูนย์ข้อมูล และผู้ใช้ของคุณจะอยู่ที่ใด เราก็อยู่ใกล้แค่เอื้อม เราทุ่มเทความพยายามเพื่อสร้างการเชื่อมต่อที่มีมาตรฐานเข้ากับเครือข่ายอายบอลเนื่องจากธุรกิจ CDN ของเรา ซึ่งจ่ายผลตอบแทนให้กับพนักงานที่อยู่ห่างไกลที่ต้องการการเชื่อมต่อที่มีประสิทธิภาพจากที่พักของตนกลับไปยังเครือข่ายของคุณ ประโยชน์ที่ได้ยังหมายความว่าเราสามารถหยุดยั้งการคุกคามที่ Edge, ใกล้ต้นทาง แทนที่จะต้องเผชิญกับความเสี่ยงของปริมาณข้อมูลที่มุ่งโจมตีระบบที่ทะลักเข้าสู่อุปกรณ์ที่มีความสามารถจำกัดภายในสถานที่
  * **ฮาร์ดแวร์และ carrier-agnostic:** ใช้ฮาร์ดแวร์ที่คุณมีในปัจจุบันเพื่อเชื่อมต่อกับเรา และรับประโยชน์จากความยืดหยุ่นจากการเชื่อมต่อของผู้ให้บริการที่หลากหลาย
  * **สร้างขึ้นจากศูนย์เพื่อการทำงานร่วมกัน:** เราได้พัฒนาผลิตภัณฑ์ของเราในซอฟต์แวร์ตั้งแต่ต้นจนจบเพื่อให้รวมเข้าด้วยกันได้อย่างง่ายดาย เราไม่เคยหยุดคิดค้นวิธีผสานรวมผลิตภัณฑ์ของเราเข้าด้วยกันเพื่อทำให้ผลิตภัณฑ์แต่ละอย่างดีขึ้นขณะที่สร้างและพัฒนาผลิตภัณฑ์เหล่านั้น



### เริ่มต้นวันนี้

Magic WAN พร้อมใช้งานในรุ่นเบต้าที่จำกัดฟังก์ชันการใช้งาน ขณะที่ Magic Firewall จะพร้อมใช้งานสำหรับลูกค้า [Magic Transit](https://www.cloudflare.com/th-th/magic-transit/) ทุกคนและรวมอยู่กับ Magic WAN หากคุณสนใจที่จะทดสอบ Magic WAN หรือต้องการเรียนรู้เพิ่มเติมเกี่ยวกับวิธีที่ Cloudflare สามารถช่วยองค์กรของคุณเปลี่ยนสถาปัตยกรรม MPLS แบบเดิม รักษาความปลอดภัยในการเข้าถึงสำหรับผู้ปฏิบัติงานจากระยะไกล และเพิ่มรูปแบบความปลอดภัยควบคู่กับการลดต้นทุนโดยรวมในการเป็นเจ้าของ โปรด[ติดต่อเรา](https://www.cloudflare.com/th-th/magic-wan/)

ในหน้านี้

สนทนาออนไลน์

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fmagic-wan-firewall%2F&t=Magic%20WAN%20%26%20Magic%20Firewall%3A%20%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%80%E0%B8%8A%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%A1%E0%B8%95%E0%B9%88%E0%B8%AD%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B8%82%E0%B9%88%E0%B8%B2%E0%B8%A2%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B8%9B%E0%B8%A5%E0%B8%AD%E0%B8%94%E0%B8%A0%E0%B8%B1%E0%B8%A2%E0%B9%83%E0%B8%99%E0%B8%90%E0%B8%B2%E0%B8%99%E0%B8%B0%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B8%9A%E0%B8%A3%E0%B8%B4%E0%B8%81%E0%B8%B2%E0%B8%A3)[](https://x.com/intent/post?text=Magic+WAN+%26+Magic+Firewall%3A+%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%80%E0%B8%8A%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%A1%E0%B8%95%E0%B9%88%E0%B8%AD%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B8%82%E0%B9%88%E0%B8%B2%E0%B8%A2%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B8%9B%E0%B8%A5%E0%B8%AD%E0%B8%94%E0%B8%A0%E0%B8%B1%E0%B8%A2%E0%B9%83%E0%B8%99%E0%B8%90%E0%B8%B2%E0%B8%99%E0%B8%B0%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B8%9A%E0%B8%A3%E0%B8%B4%E0%B8%81%E0%B8%B2%E0%B8%A3&url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fmagic-wan-firewall%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fmagic-wan-firewall%2F)[](https://bsky.app/intent/compose?text=Magic+WAN+%26+Magic+Firewall%3A+%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%80%E0%B8%8A%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%A1%E0%B8%95%E0%B9%88%E0%B8%AD%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B8%82%E0%B9%88%E0%B8%B2%E0%B8%A2%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B8%9B%E0%B8%A5%E0%B8%AD%E0%B8%94%E0%B8%A0%E0%B8%B1%E0%B8%A2%E0%B9%83%E0%B8%99%E0%B8%90%E0%B8%B2%E0%B8%99%E0%B8%B0%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B8%9A%E0%B8%A3%E0%B8%B4%E0%B8%81%E0%B8%B2%E0%B8%A3+https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fmagic-wan-firewall%2F)[](https://mastodonshare.com/?text=Magic+WAN+%26+Magic+Firewall%3A+%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%80%E0%B8%8A%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%A1%E0%B8%95%E0%B9%88%E0%B8%AD%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B8%82%E0%B9%88%E0%B8%B2%E0%B8%A2%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B8%9B%E0%B8%A5%E0%B8%AD%E0%B8%94%E0%B8%A0%E0%B8%B1%E0%B8%A2%E0%B9%83%E0%B8%99%E0%B8%90%E0%B8%B2%E0%B8%99%E0%B8%B0%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B8%9A%E0%B8%A3%E0%B8%B4%E0%B8%81%E0%B8%B2%E0%B8%A3&url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fmagic-wan-firewall%2F)[](https://www.threads.net/intent/post?text=Magic+WAN+%26+Magic+Firewall%3A+%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%80%E0%B8%8A%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%A1%E0%B8%95%E0%B9%88%E0%B8%AD%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B8%82%E0%B9%88%E0%B8%B2%E0%B8%A2%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B8%9B%E0%B8%A5%E0%B8%AD%E0%B8%94%E0%B8%A0%E0%B8%B1%E0%B8%A2%E0%B9%83%E0%B8%99%E0%B8%90%E0%B8%B2%E0%B8%99%E0%B8%B0%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B8%9A%E0%B8%A3%E0%B8%B4%E0%B8%81%E0%B8%B2%E0%B8%A3+https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fmagic-wan-firewall%2F)

## แท็กที่เกี่ยวข้อง

[Cloudflare One](https://blog.cloudflare.com/th-th/tag/cloudflare-one/)[Firewall](https://blog.cloudflare.com/th-th/tag/firewall/)[Network](https://blog.cloudflare.com/th-th/tag/network/)[Security Week](https://blog.cloudflare.com/th-th/tag/security-week/)[ข่าวผลิตภัณฑ์](https://blog.cloudflare.com/th-th/tag/product-news/)

ติดตามบนโซเชียลมีเดีย

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## สมัครรับการแจ้งเตือนโพสต์ใหม่

อีเมล

เราจะไม่เปิดเผยอีเมลของคุณ

สมัคร

ขอบคุณที่สมัครรับข่าวสาร! โปรดตรวจสอบกล่องจดหมายเพื่อยืนยัน
