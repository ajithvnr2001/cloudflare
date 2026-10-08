---
url: https://blog.cloudflare.com/th-th/defending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos/
title: \u0e01\u0e32\u0e23\u0e1b\u0e01\u0e1b\u0e49\u0e2d\u0e07\u0e2d\u0e34\u0e19\u0e40\u0e17\u0e2d\u0e23\u0e4c\u0e40\u0e19\u0e47\u0e15: Cloudflare \u0e1a\u0e25\u0e47\u0e2d\u0e01\u0e01\u0e32\u0e23\u0e42\u0e08\u0e21\u0e15\u0e35 DDoS \u0e04\u0e23\u0e31\u0e49\u0e07\u0e43\u0e2b\u0e0d\u0e48\u0e02\u0e19\u0e32\u0e14 7.3 Tbps \u0e44\u0e14\u0e49\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e44\u0e23 | \u0e1a\u0e25\u0e47\u0e2d\u0e01 Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:37:49.065994+00:00
---

# การปกป้องอินเทอร์เน็ต: Cloudflare บล็อกการโจมตี DDoS ครั้งใหญ่ขนาด 7.3 Tbps ได้อย่างไร | บล็อก Cloudflare

> Source: https://blog.cloudflare.com/th-th/defending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos/

[บล็อก](https://blog.cloudflare.com/th-th/)

[DDoS](https://blog.cloudflare.com/th-th/tag/ddos/)[รายงาน DDoS](https://blog.cloudflare.com/th-th/tag/ddos-reports/)

2 แท็กแสดง 2 แท็ก

  * แท็กของโพสต์
  * [DDoS](https://blog.cloudflare.com/th-th/tag/ddos/)[รายงาน DDoS](https://blog.cloudflare.com/th-th/tag/ddos-reports/)
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



[DDoS](https://blog.cloudflare.com/th-th/tag/ddos/)[รายงาน DDoS](https://blog.cloudflare.com/th-th/tag/ddos-reports/)

19 มิถุนายน 2568

# การปกป้องอินเทอร์เน็ต: Cloudflare บล็อกการโจมตี DDoS ครั้งใหญ่ขนาด 7.3 Tbps ได้อย่างไร

![Omer Yoachimik](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW485W0MZ0R9VGWD75RQN9ZH.png&w=64&h=64&f=webp&fit=cover&position=center)

[Omer Yoachimik](https://blog.cloudflare.com/th-th/author/omer/)

อ่าน 5 นาที

คัดลอก URL

โพสต์นี้มีให้อ่านใน [English](https://blog.cloudflare.com/defending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos/) [Deutsch](https://blog.cloudflare.com/de-de/defending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos/) [Español](https://blog.cloudflare.com/es-es/defending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos/) [Français](https://blog.cloudflare.com/fr-fr/defending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos/) [日本語](https://blog.cloudflare.com/ja-jp/defending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos/) [한국어](https://blog.cloudflare.com/ko-kr/defending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos/) [Português](https://blog.cloudflare.com/pt-br/defending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos/) [Bahasa Indonesia](https://blog.cloudflare.com/id-id/defending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos/) และ[Nederlands](https://blog.cloudflare.com/nl-nl/defending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos/).

![BLOG-2834 Hero Image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46Y2ZG1G9298P8YPT052PY.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///////88/Hx5+br5ujt7e7y8PHx7+/r///////+8O/z4OLs3eLu5Onz6+7z7u/t////////7u712d/u1d3w3eX16O317vDw////////8PH52uHy1d/03uf56vD58fP1////////9vf+4+n33+f56O/+8vf+9/n5////////////8fP87/T+9/v//f///f7+/////////////Pz//f7/////////////////////////////////////////////)

ในช่วงกลางเดือนพฤษภาคม 2025 ที่ผ่านมา Cloudflare ได้บล็อกการโจมตี DDoS ที่ใหญ่ที่สุดขนาด 7.3 เทราบิตต่อวินาที (Tbps) ที่เคยบันทึกไว้ เหตุการณ์นี้เกิดขึ้นในช่วงสั้น ๆ หลังจากการเผยแพร่ [_รายงานภัยคุกคาม DDoS ของเราในไตรมาสที่ 1 ปี 2025_](https://blog.cloudflare.com/ddos-threat-report-for-2025-q1/) เมื่อวันที่ 27 เมษายน 2025 ซึ่งเราได้เน้นย้ำถึงการโจมตีที่เข้าถึงระดับ 6.5 Tbps และ 4.8 พันล้านแพ็กเก็ตต่อวินาที (pps) การโจมตี 7.3 Tbps นั้นมีขนาดใหญ่กว่าสถิติก่อนหน้าของเราถึง 12% และมากกว่าการโจมตีล่าสุดถึง 1 Tbps จากที่รายงานโดย Brian Krebs ผู้สื่อข่าวด้านความปลอดภัยทางไซเบอร์จาก [_KrebsOnSecurity_](https://krebsonsecurity.com/2025/05/krebsonsecurity-hit-with-near-record-6-3-tbps-ddos/)

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2834 Image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW453A53NCMWX5CDMSCDQ6TM.png&w=715&h=322&f=webp&fit=cover&position=center)

 _สถิติโลกใหม่: การโจมตี DDoS 7.3 Tbps ถูก Cloudflare บล็อกได้โดยอัตโนมัติ_

การโจมตีครั้งนี้มุ่งเป้าไปที่ลูกค้าของ Cloudflare ซึ่งเป็นผู้ให้บริการโฮสติ้งที่ใช้ [_Magic Transit_](https://www.cloudflare.com/network-services/products/magic-transit/) เพื่อป้องกันเครือข่าย IP ของตน ผู้ให้บริการโฮสติ้งและโครงสร้างพื้นฐานอินเทอร์เน็ตที่สำคัญกลายเป็นเป้าหมายของการโจมตี DDoS มากขึ้นเรื่อย ๆ ตามที่เราได้รายงานไว้ใน [_รายงานภัยคุกคาม DDoS ล่าสุด_](https://blog.cloudflare.com/ddos-threat-report-for-2025-q1/#attacks-target-the-cloudflare-network-and-internet-infrastructure) ภาพด้านล่างแสดงแคมเปญการโจมตีตั้งแต่เดือนมกราคมและกุมภาพันธ์ 2025 ที่กล่าวอ้างถึงการโจมตีของ DDoS มากกว่า 13.5 ล้านครั้งที่มุ่งเป้าหมายไปที่โครงสร้างพื้นฐานของ Cloudflare และผู้ให้บริการโฮสติ้งที่ได้รับการปกป้องโดย Cloudflare

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2834 Image 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44QFH41JXA01MWKJA4WNCN.png&w=715&h=278&f=webp&fit=cover&position=center)

 _แคมเปญโจมตี DDoS มุ่งเป้าไปที่โครงสร้างพื้นฐานของ Cloudflare และผู้ให้บริการโฮสติ้งที่ได้รับการปกป้องโดย Cloudflare_

มาเริ่มด้วยสถิติกันก่อน จากนั้นเราจะมาดูกันว่าระบบของเราตรวจจับและลดการโจมตีลักษณะนี้ได้อย่างไร

## การโจมตี 7.3 Tbps ส่ง 37.4 เทราไบต์ใน 45 วินาที

37.4 เทราไบต์ไม่ใช่ตัวเลขที่น่าตกใจในปัจจุบัน แต่การจัดการขนาด 37.4 เทราไบต์ในเวลาเพียง 45 วินาทีนั้นต่างหากที่น่าตกใจ เทียบเท่ากับการส่งภาพยนตร์ความคมชัดระดับ HD ความยาวเต็มรูปแบบจำนวนกว่า 9,350 เรื่องอัดเข้าไปในเครือข่ายของคุณ หรือสตรีมวิดีโอความคมชัดสูง 7,480 ชั่วโมงแบบต่อเนื่อง (เท่ากับการดูรวดเดียวติดต่อกันเกือบปี) ในเวลาแค่ 45 วินาที หากเป็นเพลง คุณจะดาวน์โหลดเพลงราว 9.35 ล้านเพลงในเวลาไม่ถึงหนึ่งนาที เพื่อให้ผู้ฟังเพลิดเพลินได้นานถึง 57 ปีเลยทีเดียว ลองนึกภาพว่าคุณสามารถถ่ายภาพความละเอียดสูง 12.5 ล้านภาพบนสมาร์ทโฟนของคุณได้ และพื้นที่เก็บข้อมูลไม่มีวันหมด แม้ว่าคุณจะถ่ายภาพวันละภาพ คุณก็จะต้องใช้เวลาคลิกถ่ายภาพนานถึง 4,000 ปี แต่ทั้งหมดนี้ทำได้ในเวลาแค่ 45 วินาทีเท่านั้น 

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2834 Image 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW457QHPAPNF2MEMJSSTM5B1.png&w=715&h=495&f=webp&fit=cover&position=center)

 _การโจมตี DDoS ขนาด 7.3 Tbps เป็นการทำลายสถิติ ส่งผลให้มีข้อมูล 37.4 TB ในเวลา 45 วินาที_

## รายละเอียดการโจมตี

การโจมตีดังกล่าวโจมตีพอร์ตปลายทางโดยเฉลี่ย 21,925 พอร์ตจากที่อยู่ IP เดียวที่ลูกค้าของเราเป็นเจ้าของและใช้งาน และทำได้สูงสุดถึง 34,517 พอร์ตต่อวินาที การโจมตีดังกล่าวเกิดจากการกระจายพอร์ตต้นทางที่คล้ายคลึงกัน 

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2834 Image 4](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW496M1N59288D47J4QMFG9F.png&w=715&h=319&f=webp&fit=cover&position=center)

 _การกระจายของพอร์ตปลายทาง_

### เวกเตอร์การโจมตี

การโจมตีขนาด 7.3 Tbps เป็นการโจมตี DDoS แบบหลายเวกเตอร์ ประมาณ 99.996% ของปริมาณการโจมตีถูกจัดประเภทเป็น UDP Flood อย่างไรก็ตาม 0.004% ที่เหลือ ซึ่งคิดเป็น 1.3 GB ของปริมาณการโจมตีทั้งหมด ได้รับการระบุว่าเป็นการโจมตีแบบ QOTD reflection, การโจมตี Echo reflection, การโจมตี NTP reflection, การโจมตี Mirai UDP flood, การโจมตี Portmap flood และการโจมตี RIPv1 amplification

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2834 Image 5](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW447QBH13SB1BGGGNYCM2RJ.png&w=715&h=420&f=webp&fit=cover&position=center)

 _เวกเตอร์การโจมตีอื่น ๆ นอกเหนือจาก UDP floods_

### การแบ่งเวกเตอร์การโจมตี

ด้านล่างนี้คือรายละเอียดเกี่ยวกับเวกเตอร์การโจมตีต่าง ๆ ที่พบในการโจมตีนี้ วิธีที่องค์กรต่าง ๆ สามารถหลีกเลี่ยงการเป็นผู้มีส่วนร่วมใน ใน reflection และ amplification และคำแนะนำเกี่ยวกับวิธีป้องกันการโจมตีเหล่านี้ในขณะที่หลีกเลี่ยงผลกระทบต่อปริมาณการรับส่งข้อมูลที่ถูกต้อง ลูกค้าของ Cloudflare ได้รับการปกป้องจากการโจมตีเหล่านี้

#### การโจมตี UDP DDoS

  * **ประเภท** : Flood (อัดเข้าไป)
  * **วิธีการทำงาน:** แพ็กเก็ต UDP ปริมาณสูงจะถูกส่งไปยังพอร์ตแบบสุ่มหรือเฉพาะบนที่อยู่ IP เป้าหมาย เพื่อพยายามทำให้ลิงก์อินเทอร์เน็ตอิ่มตัวหรือทำให้อุปกรณ์อินไลน์รับข้แพ็กเก็ตมากเกินกว่าที่จะรับไหว
  * **วิธีป้องกันการโจมตี:** ใช้การป้องกัน DDoS เชิงปริมาณบนคลาวด์ ใช้การจำกัดอัตราอัจฉริยะกับการรับส่งข้อมูล UDP และลบการรับส่งข้อมูล UDP ที่ไม่ต้องการทั้งหมด
  * **วิธีหลีกเลี่ยงผลกระทบที่ไม่พึงประสงค์:** การกรองที่เข้มงวดอาจรบกวนบริการ UDP ที่ถูกต้องตามกฎหมาย เช่น VoIP, การประชุมทางวิดีโอ หรือเกมออนไลน์ ใช้เกณฑ์ต่าง ๆ อย่างระมัดระวัง



#### การโจมตี QOTD DDoS

  * **ประเภท :** Reflection + Amplification (การสะท้อน + การขยาย)
  * **วิธีการทำงาน:** ละเมิดโปรโตคอล Quote of the Day (QOTD) ซึ่งรับฟังบนพอร์ต UDP 17 และตอบกลับด้วยคำพูดหรือข้อความสั้น ๆ ผู้โจมตีจะส่งคำขอ QOTD ไปยังเซิร์ฟเวอร์ที่เปิดเผยจากที่อยู่ IP ปลอม ส่งผลให้มีการตอบรับที่ขยายจำนวนมากขึ้นเพื่ออัดการโจมตีเหยื่อ
  * **วิธีป้องกันไม่ให้กลายเป็นองค์ประกอบการสะท้อน/การขยาย:** ปิดใช้งานบริการ QOTD และบล็อก UDP/17 บนเซิร์ฟเวอร์และไฟร์วอลล์ทั้งหมด
  * **วิธีป้องกันการโจมตี:** บล็อก UDP/17 ขาเข้า ลดกลุ่มคำขอ UDP แพ็กเก็ตเล็กที่ผิดปกติ
  * **วิธีหลีกเลี่ยงผลกระทบที่ไม่ได้ตั้งใจ:** QOTD เป็นโปรโตคอลการวินิจฉัย/แก้ไขข้อบกพร่องที่ล้าสมัยและไม่ได้ใช้โดยแอปพลิเคชันสมัยใหม่ การปิดการใช้งานไม่ควรมีผลกระทบเชิงลบต่อบริการที่ถูกกฎหมาย



#### การโจมตี DDoS ของ Echo

  * **ประเภท :** Reflection + Amplification (การสะท้อน + การขยาย)
  * **วิธีการทำงาน:** ใช้ประโยชน์จากโปรโตคอล Echo (พอร์ต UDP/TCP 7) ซึ่งตอบกลับด้วยข้อมูลเดียวกับที่ได้รับ ผู้โจมตีจะปลอมแปลงที่อยู่ IP ของเหยื่อ ทำให้อุปกรณ์สะท้อนข้อมูลกลับมา ส่งผลให้การโจมตีรุนแรงขึ้น
  * **วิธีป้องกันไม่ให้กลายเป็นองค์ประกอบการสะท้อน/การขยาย:** ปิดใช้งานบริการ Echo บนอุปกรณ์ทั้งหมด บล็อค UDP/TCP พอร์ต 7 ที่ขอบ
  * **วิธีป้องกันการโจมตี:** ปิดใช้งานบริการ Echo และบล็อกพอร์ต TCP/UDP 7 ที่ขอบเขตเครือข่าย
  * **วิธีหลีกเลี่ยงผลกระทบที่ไม่พึงประสงค์:** Echo เป็นเครื่องมือวินิจฉัยที่ล้าสมัย การปิดใช้งานหรือการบล็อกไม่มีผลเสียต่อระบบสมัยใหม่



#### การโจมตี NTP DDoS

  * **ประเภท :** Reflection + Amplification (การสะท้อน + การขยาย)
  * **วิธีการทำงาน:** ใช้โปรโตคอล Network Time (NTP) ในทางที่ผิด คือนำมาใช้เพื่อซิงค์นาฬิกาผ่านทางอินเทอร์เน็ต ผู้โจมตีใช้ประโยชน์จากคำสั่ง monlist บนเซิร์ฟเวอร์ NTP เก่า (UDP/123) ซึ่งจะส่งคืนรายการการเชื่อมต่อล่าสุดจำนวนมาก คำขอปลอมจะทำให้เกิดการสะท้อนที่ขยายจำนวนมากขึ้น
  * **วิธีป้องกันไม่ให้กลายเป็นองค์ประกอบของการสะท้อน / การขยาย:** อัพเกรดหรือกำหนดค่าเซิร์ฟเวอร์ NTP เพื่อปิดการใช้งาน monlist จำกัดการสืบค้น NTP ให้แคบลงเหลือเฉพาะที่อยู่ IP ที่เชื่อถือได้เท่านั้น
  * **วิธีป้องกันการโจมตี:** ปิดใช้งานคำสั่ง monlist, อัปเดตซอฟต์แวร์ NTP และกรองหรือจำกัดอัตราทราฟฟิก UDP/123
  * **วิธีหลีกเลี่ยงผลกระทบที่ไม่พึงประสงค์:** การปิดใช้งาน monlist ไม่มีผลต่อการซิงโครไนซ์เวลา อย่างไรก็ตาม การกรองหรือการบล็อก UDP/123 อาจส่งผลต่อการซิงค์เวลาได้หากทำในขอบเขตกว้างเกินไป ให้แน่ใจว่าบล็อกเฉพาะแหล่งที่ไม่น่าเชื่อถือหรือแหล่งภายนอกเท่านั้น



#### การโจมตี Mirai UDP

  * **ประเภท :** Flood (อัดเข้าไป)
  * **วิธีการทำงาน:** [_บอทเน็ต Mirai_](https://www.cloudflare.com/learning/ddos/glossary/mirai-botnet/) ซึ่งประกอบด้วยอุปกรณ์ IoT ที่ถูกบุกรุก จะทุ่มลงมัลแวร์ไปให้กับเหยื่อโดยใช้แพ็กเก็ต UDP แบบสุ่มหรือเฉพาะบริการ (เช่น DNS, บริการเกม)
  * **วิธีป้องกันไม่ให้เป็นส่วนหนึ่งของบอทเน็ต:** รักษาความปลอดภัยอุปกรณ์ IoT ของคุณ เปลี่ยนรหัสผ่านเริ่มต้น อัปเกรดเป็นเฟิร์มแวร์เวอร์ชันล่าสุด และปฏิบัติตาม [_แนวทางปฏิบัติที่ดีที่สุดด้านความปลอดภัยของ IoT_](https://www.cloudflare.com/en-gb/learning/security/glossary/iot-security/) เพื่อหลีกเลี่ยงการเป็นส่วนหนึ่งของบอทเน็ต หากเป็นไปได้ ควรตรวจสอบการรับส่งข้อมูลขาออกเพื่อตรวจจับสิ่งผิดปกติ
  * **วิธีป้องกันการโจมตี:** ใช้การป้องกัน DDoS แบบปริมาณบนคลาวด์และการจำกัดอัตราสำหรับการรับส่งข้อมูล UDP
  * **วิธีหลีกเลี่ยงผลกระทบที่ไม่พึงประสงค์:** ขั้นแรก ให้ทำความเข้าใจเครือข่ายของคุณและประเภทของการรับส่งข้อมูลที่คุณได้รับ โดยเฉพาะอย่างยิ่งโปรโตคอล แหล่งที่มาและจุดหมายปลายทาง ระบุบริการที่ทำงานบน UDP ที่คุณต้องการหลีกเลี่ยงไม่ให้ส่งผลกระทบ เมื่อคุณระบุได้แล้ว คุณสามารถใช้การจำกัดอัตราโดยไม่รวมจุดสิ้นสุดเหล่านั้น หรือคำนึงถึงระดับปริมาณการรับส่งข้อมูลปกติของคุณ มิฉะนั้น การจำกัดอัตราการรับส่งข้อมูล UDP อย่างเข้มงวดอาจส่งผลกระทบต่อการรับส่งข้อมูลที่ถูกต้องของคุณ และส่งผลต่อบริการที่ทำงานบน UDP เช่น การโทร VoIP และการรับส่งข้อมูล VPN



#### การโจมตี Portmap DDoS

  * **ประเภท :** Reflection + Amplification (การสะท้อน + การขยาย)
  * **วิธีการทำงาน:** กำหนดเป้าหมายบริการ Portmapper (UDP/111) ที่ใช้โดยแอปพลิเคชันที่ใช้ Remote Procedure Call (RPC) เพื่อระบุว่ามีบริการใดบ้างที่พร้อมใช้งาน คำขอปลอมส่งผลให้มีการตอบสนองกลับ
  * **วิธีป้องกันไม่ให้กลายเป็นองค์ประกอบการสะท้อน / การขยาย:** ปิดใช้งานบริการ Portmapper หากไม่จำเป็น หากจำเป็นเป็นการภายใน ให้จำกัดเฉพาะที่อยู่ IP ที่เชื่อถือได้เท่านั้น
  * **วิธีป้องกันการโจมตี:** ปิดใช้งานบริการ Portmapper หากไม่จำเป็น และบล็อกการรับส่งข้อมูล UDP/111 ขาเข้า ใช้รายการควบคุมการเข้าถึง (ACL) หรือ Firewall เพื่อจำกัดการเข้าถึงบริการ RPC ที่รู้จัก
  * **วิธีหลีกเลี่ยงผลกระทบที่ไม่พึงประสงค์:** การปิดใช้งาน Portmapper อาจทำให้แอพพลิเคชันที่ต้องอาศัย RPC (เช่น โปรโตคอลระบบไฟล์เครือข่าย) หยุดชะงัก ตรวจสอบการอ้างอิงของบริการก่อนทำการลบ



#### การโจมตี RIPv1 DDoS

  * **ประเภท :** การสะท้อน + การขยาย (ต่ำ)
  * **วิธีการทำงาน:** ใช้ประโยชน์จากโปรโตคอล Routing Information เวอร์ชัน 1 (RIPv1) ซึ่งเป็นโปรโตคอลการกำหนดเส้นทางเวกเตอร์ระยะทางแบบเก่าที่ไม่ได้รับการตรวจรับรองซึ่งใช้ UDP/520 ผู้โจมตีจะส่งการอัพเดตเส้นทางปลอมเพื่อสร้างความสับสนหรือทำให้เครือข่ายเสียหาย
  * **วิธีป้องกันไม่ให้กลายเป็นองค์ประกอบการสะท้อน/การขยาย:** ปิดใช้งาน RIPv1 บนเราเตอร์ ใช้ RIPv2 พร้อมการยืนยันตัวตนในกรณีที่จำเป็นต้องมีการกำหนดเส้นทาง
  * **วิธีป้องกันการโจมตี:** บล็อก UDP/520 ขาเข้าจากเครือข่ายที่ไม่น่าเชื่อถือ ตรวจสอบการอัปเดตการกำหนดเส้นทางที่ไม่คาดคิด
  * **วิธีหลีกเลี่ยงผลกระทบที่ไม่พึงประสงค์:** RIPv1 แทบจะล้าสมัยแล้ว การปิดใช้งานถือเป็นเรื่องปกติ แต่ถ้าระบบเดิมยังต้องใช้อยู่ โปรดตรวจสอบพฤติกรรมการกำหนดเส้นทางก่อนการเปลี่ยนแปลง



คำแนะนำทั้งหมดที่นี่ควรนำมาพิจารณาร่วมกับบริบทและพฤติกรรมของเครือข่ายหรือแอปพลิเคชันเฉพาะแต่ละรายการ เพื่อหลีกเลี่ยงผลกระทบที่ไม่พึงประสงค์ที่อาจเกิดขึ้นกับปริมาณการรับส่งข้อมูลที่ถูกต้องตามกฎหมาย

### ต้นตอการโจมตี

การโจมตีมีต้นตอมาจากที่อยู่ IP ต้นทางกว่า 122,145 แห่งที่ครอบคลุม Autonomous System (AS) จำนวน 5,433 ระบบใน 161 ประเทศ 

เกือบครึ่งหนึ่งของการโจมตีมาจากบราซิลและเวียดนาม โดยอยู่ที่ประมาณหนึ่งในสี่ของแต่ละประเทศ อีกหนึ่งในสามโดยรวมมาจากไต้หวัน จีน อินโดนีเซีย ยูเครน เอกวาดอร์ ไทย สหรัฐอเมริกา และซาอุดิอาระเบีย

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2834 Image 6](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47990F484HK1HQJB53YVE6.png&w=715&h=407&f=webp&fit=cover&position=center)

 _10 อันดับประเทศต้นทางการโจมตี_

จำนวนเฉลี่ยของที่อยู่ IP ต้นทางที่ไม่ซ้ำกันต่อวินาทีอยู่ที่ 26,855 โดยสูงสุดอยู่ที่ 45,097 

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2834 Image 7](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47BMPT8HAWVMA1W1W6K9ZQ.png&w=715&h=304&f=webp&fit=cover&position=center)

 _การกระจายที่อยู่ IP ต้นทางที่ไม่ซ้ำกัน_

การโจมตีมีมาจากเครือข่ายที่แตกต่างกัน 5,433 เครือข่าย ([_ASes_](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/)) Telefonica Brazil ([_AS27699_](https://radar.cloudflare.com/as27699)) มีสัดส่วนปริมาณการโจมตี DDoS มากที่สุด โดยคิดเป็น 10.5% ของทั้งหมด Viettel Group ([_AS7552_](https://radar.cloudflare.com/as7552)) ตามมาติด ๆ ด้วยส่วนแบ่ง 9.8% ในขณะที่ China Unicom ([_AS4837_](https://radar.cloudflare.com/as4837)) และ Chunghwa Telecom ([_AS3462_](https://radar.cloudflare.com/as3462)) มีส่วนในสัดส่วน 3.9% และ 2.9% ตามลำดับ China Telecom ([_AS4134_](https://radar.cloudflare.com/as4134)) มีส่วนแบ่งการรับส่งข้อมูล 2.8% ASN ที่เหลือใน 10 อันดับแรก ได้แก่ Claro NXT ([_AS28573_](https://radar.cloudflare.com/as28573)), VNPT Corp ([_AS45899_](https://radar.cloudflare.com/as45899)), UFINET Panama ([_AS52468_](https://radar.cloudflare.com/as52468)), STC ([_AS25019_](https://radar.cloudflare.com/as25019)) และ FPT Telecom Company ([_AS18403_](https://radar.cloudflare.com/as18403)) แต่ละบริษัทมีครองสัดส่วนระหว่าง 1.3% ถึง 1.8% ของปริมาณการโจมตี DDoS ทั้งหมด  


![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2834 Image 8](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48CFW161VF8EB5SPKE4BDH.png&w=715&h=401&f=webp&fit=cover&position=center)

 _10 อันดับแหล่ง Autonomous System ชั้นนำ_

### ฟีดภัยคุกคามบอทเน็ตฟรี

เพื่อช่วยให้ผู้ให้บริการโฮสติ้ง ผู้ให้บริการการประมวลผลบนคลาวด์ และผู้ให้บริการอินเทอร์เน็ตใด ๆ ก็ตามสามารถระบุและลบบัญชีที่ละเมิดซึ่งเปิดใช้การโจมตีเหล่านี้ได้ เราจึงได้ใช้ประโยชน์จากมุมมองอันเป็นเอกลักษณ์เฉพาะของ Cloudflare เพื่อมอบ [_ฟีดภัยคุกคามบอทเน็ต DDoS ฟรีสำหรับผู้ให้บริการ_](https://developers.cloudflare.com/ddos-protection/botnet-threat-feed/) มีองค์กรทั่วโลกมากกว่า 600 แห่งลงทะเบียนรับฟีดนี้แล้ว ฟีดนี้จะแสดงรายชื่อที่อยู่ IP ที่มีปัญหาจากภายใน ASN ของผู้ให้บริการ ซึ่งเราพบว่ามีการเปิดตัวการโจมตี HTTP DDoS ฟีดนี้ฟรี คุณแค่ต้องเปิดบัญชี Cloudflare ฟรี ยืนยัน Autonomous System Number ผ่าน [_PeeringDB_](https://docs.peeringdb.com/howto/authenticate/) จากนั้น[ _ดึงฟีดผ่าน API_](https://developers.cloudflare.com/ddos-protection/botnet-threat-feed/#get-full-report)

## วิธีตรวจจับและบรรเทาการโจมตี

### การใช้ลักษณะการกระจายตัวของการโจมตี DDoS เพื่อจัดการ

ที่อยู่ IP ที่ถูกโจมตีได้รับการโฆษณาจากเครือข่ายของ Cloudflare โดยใช้ [_anycast_](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/) ทั่วโลก ซึ่งหมายความว่าแพ็กเก็ตโจมตีที่กำหนดเป้าหมายที่ IP นั้นถูกส่งไปยังศูนย์ข้อมูล Cloudflare ที่ใกล้ที่สุด การใช้ anycast ทั่วโลกช่วยให้เรากระจายปริมาณการโจมตีได้ และใช้ลักษณะการกระจายของปริมาณการโจมตีเป็นตัวจัดการ ทำให้เราสามารถลดความเสี่ยงของการโจมตีโหนดบอตเน็ตและให้บริการผู้ใช้จากศูนย์ข้อมูลที่อยู่ใกล้กับผู้ใช้ที่สุดได้ต่อไป ในกรณีของการโจมตีนี้ ได้มีการตรวจพบและบรรเทาผลกระทบในศูนย์ข้อมูล 477 แห่งใน 293 สถานที่ทั่วโลก ในสถานที่ที่มีปริมาณการเข้าใช้งานสูง เรามีสำนักงานอยู่ในศูนย์ข้อมูลหลายแห่ง 

### การตรวจจับและบรรเทา DDoS อัตโนมัติ

เครือข่ายทั่วโลกของ Cloudflare รันบริการทุกอย่างในทุกศูนย์ข้อมูล ซึ่งรวมถึงระบบตรวจจับและบรรเทา DDoS ของเรา ซึ่งหมายความว่าการโจมตีถูกตรวจจับและบรรเทาได้อย่างอัตโนมัติโดยสมบูรณ์โดยไม่คำนึงว่าการโจมตีนั้นมาจากที่ใด 

### การพิมพ์ลายนิ้วมือแบบเรียลไทม์

เมื่อแพ็กเก็ตเข้าสู่ศูนย์ข้อมูลของเรา แพ็กเก็ตจะ [_ถูกโหลดบาลานซ์อย่างชาญฉลาด_](https://blog.cloudflare.com/unimog-cloudflares-edge-load-balancer/)ไปยังเซิร์ฟเวอร์ที่พร้อมใช้งาน จากนั้นเราจะสุ่มตัวอย่างแพ็กเก็ตโดยตรงจากภายในส่วนลึกของเคอร์เนล Linux จาก [__eXpress Data Path_ (XDP)_](https://en.wikipedia.org/wiki/Express_Data_Path) โดยใช้โปรแกรม [_Berkley Packer Filter (eBPF) ที่ขยาย_](https://en.wikipedia.org/wiki/EBPF) เพื่อกำหนดเส้นทางแพ็กเก็ตตัวอย่างไปยังพื้นที่ผู้ใช้ที่เราจะเรียกใช้การวิเคราะห์

ระบบของเราวิเคราะห์ตัวอย่าง packet เพื่อระบุรูปแบบที่น่าสงสัยโดยอิงจากฮิวริสติกส์เอ็นจิ้นเฉพาะของเราที่มีชื่อว่า _dosd_ (denial of service daemon) Dosd มองหารูปแบบในตัวอย่างแพ็กเก็ต เช่น การค้นหาความเหมือนกันในฟิลด์ส่วนหัวแพ็กเก็ต และการค้นหาความผิดปกติของแพ็กเก็ต รวมถึงการใช้เทคนิคที่เป็นกรรมสิทธิ์อื่น ๆ

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2834 Image 9](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47KVQNE2FNZY927RQ17RBN.png&w=715&h=220&f=webp&fit=cover&position=center)

 _แผนผังขั้นตอนการสร้างลายนิ้วมือแบบเรียลไทม์_

สำหรับลูกค้าของเรา ระบบการพิมพ์ลายนิ้วมือที่ซับซ้อนนี้ถูกรวมไว้ในกลุ่ม _กฎที่ได้รับการจัดการ_ ที่เป็นมิตรกับผู้ใช้ที่เรียกว่า [_ชุดกฎการป้องกัน DDoS ที่ได้รับการจัดการ_](https://developers.cloudflare.com/ddos-protection/managed-rulesets/)

เมื่อ dosd ตรวจพบรูปแบบ ระบบจะสร้างการเรียงสับเปลี่ยนของลายนิ้วมือเหล่านั้นหลายชุดเพื่อค้นหาลายนิ้วมือที่แม่นยำที่สุดซึ่งจะมีประสิทธิภาพในการบรรเทาผลกระทบและความถูกต้องสูงสุด กล่าวคือ เพื่อพยายามจับคู่กับการรับส่งข้อมูลที่ถูกโจมตีโดยไม่ส่งผลกระทบต่อการรับส่งข้อมูลที่ถูกต้อง 

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2834 Image 10](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46TQCFDQQGJ1N78T9JE7FZ.png&w=715&h=532&f=webp&fit=cover&position=center)

 _แผนผังระบบการป้องกัน DDoS ของ Cloudflare_

## การบรรเทาผลกระทบ

เราจะนับตัวอย่างแพ็กเก็ตต่าง ๆ ที่ตรงกับการเรียงสับเปลี่ยนของลายนิ้วมือแต่ละครั้ง และใช้อัลกอริธึมการสตรีมข้อมูล เพื่อรวบรวมลายนิ้วมือที่มีการค้นหามากที่สุด เมื่อเกินเกณฑ์การเปิดใช้งาน เพื่อหลีกเลี่ยงผลลัพธ์บวกปลอม กฎการบรรเทาผลกระทบที่ใช้รูปแบบลายนิ้วมือจะถูกคอมไพล์เป็นโปรแกรม eBPF เพื่อลบแพ็กเก็ตที่ตรงกับรูปแบบการโจมตี เมื่อการโจมตีสิ้นสุดลง กฎจะหมดเวลาและจะถูกลบออกโดยอัตโนมัติ

## การรวบรวมข้อมูลการโจมตี

ดังที่เราได้กล่าวไปแล้ว เซิร์ฟเวอร์แต่ละตัวจะตรวจจับและบรรเทาการโจมตีโดยอัตโนมัติ ทำให้เครือข่ายของเรามีประสิทธิภาพสูง ยืดหยุ่น และบล็อกการโจมตีได้อย่างรวดเร็ว นอกจากนี้ เซิร์ฟเวอร์แต่ละตัว _จะรวบรวมข้อมูล_ ([__มัลติคาสต์__](https://www.cloudflare.com/en-gb/learning/network-layer/what-is-igmp/#:~:text=What%20is%20multicasting%3F)) ของการเรียงสับเปลี่ยนลายนิ้วมือชั้นนำภายในศูนย์ข้อมูลและทั่วโลก การแบ่งปันข้อมูลข่าวกรองเกี่ยวกับภัยคุกคามแบบเรียลไทม์นี้ช่วยปรับปรุงประสิทธิภาพในการบรรเทาผลกระทบภายในศูนย์ข้อมูลและทั่วโลก 

## การปกป้องอินเทอร์เน็ต

ระบบของเราประสบความสำเร็จในการบล็อกการโจมตี DDoS ที่ทำลายสถิติ 7.3 Tbps ได้อย่างอัตโนมัติโดยไม่ต้องมีการแทรกแซงจากมนุษย์ โดยไม่ทริกเกอร์สัญญาณเตือนใด ๆ และโดยไม่ก่อให้เกิดเหตุการณ์ใด ๆ ซึ่งแสดงให้เห็นถึงประสิทธิภาพของระบบการป้องกัน DDoS ชั้นนำของโลกของเรา เราสร้างระบบนี้ขึ้นเพื่อเป็นส่วนหนึ่งของภารกิจของเราในการช่วยสร้างอินเทอร์เน็ตที่ดีขึ้น พร้อมความมุ่งมั่นที่จะมอบการป้องกัน DDoS แบบไม่จำกัดโดยไม่มีค่าใช้จ่ายใด ๆ

ในหน้านี้

สนทนาออนไลน์

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fdefending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos%2F&t=%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9B%E0%B8%81%E0%B8%9B%E0%B9%89%E0%B8%AD%E0%B8%87%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%80%E0%B8%97%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B9%80%E0%B8%99%E0%B9%87%E0%B8%95%3A%20Cloudflare%20%E0%B8%9A%E0%B8%A5%E0%B9%87%E0%B8%AD%E0%B8%81%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%82%E0%B8%88%E0%B8%A1%E0%B8%95%E0%B8%B5%20DDoS%20%E0%B8%84%E0%B8%A3%E0%B8%B1%E0%B9%89%E0%B8%87%E0%B9%83%E0%B8%AB%E0%B8%8D%E0%B9%88%E0%B8%82%E0%B8%99%E0%B8%B2%E0%B8%94%207.3%20Tbps%20%E0%B9%84%E0%B8%94%E0%B9%89%E0%B8%AD%E0%B8%A2%E0%B9%88%E0%B8%B2%E0%B8%87%E0%B9%84%E0%B8%A3)[](https://x.com/intent/post?text=%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9B%E0%B8%81%E0%B8%9B%E0%B9%89%E0%B8%AD%E0%B8%87%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%80%E0%B8%97%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B9%80%E0%B8%99%E0%B9%87%E0%B8%95%3A+Cloudflare+%E0%B8%9A%E0%B8%A5%E0%B9%87%E0%B8%AD%E0%B8%81%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%82%E0%B8%88%E0%B8%A1%E0%B8%95%E0%B8%B5+DDoS+%E0%B8%84%E0%B8%A3%E0%B8%B1%E0%B9%89%E0%B8%87%E0%B9%83%E0%B8%AB%E0%B8%8D%E0%B9%88%E0%B8%82%E0%B8%99%E0%B8%B2%E0%B8%94+7.3+Tbps+%E0%B9%84%E0%B8%94%E0%B9%89%E0%B8%AD%E0%B8%A2%E0%B9%88%E0%B8%B2%E0%B8%87%E0%B9%84%E0%B8%A3&url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fdefending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fdefending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos%2F)[](https://bsky.app/intent/compose?text=%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9B%E0%B8%81%E0%B8%9B%E0%B9%89%E0%B8%AD%E0%B8%87%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%80%E0%B8%97%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B9%80%E0%B8%99%E0%B9%87%E0%B8%95%3A+Cloudflare+%E0%B8%9A%E0%B8%A5%E0%B9%87%E0%B8%AD%E0%B8%81%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%82%E0%B8%88%E0%B8%A1%E0%B8%95%E0%B8%B5+DDoS+%E0%B8%84%E0%B8%A3%E0%B8%B1%E0%B9%89%E0%B8%87%E0%B9%83%E0%B8%AB%E0%B8%8D%E0%B9%88%E0%B8%82%E0%B8%99%E0%B8%B2%E0%B8%94+7.3+Tbps+%E0%B9%84%E0%B8%94%E0%B9%89%E0%B8%AD%E0%B8%A2%E0%B9%88%E0%B8%B2%E0%B8%87%E0%B9%84%E0%B8%A3+https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fdefending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos%2F)[](https://mastodonshare.com/?text=%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9B%E0%B8%81%E0%B8%9B%E0%B9%89%E0%B8%AD%E0%B8%87%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%80%E0%B8%97%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B9%80%E0%B8%99%E0%B9%87%E0%B8%95%3A+Cloudflare+%E0%B8%9A%E0%B8%A5%E0%B9%87%E0%B8%AD%E0%B8%81%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%82%E0%B8%88%E0%B8%A1%E0%B8%95%E0%B8%B5+DDoS+%E0%B8%84%E0%B8%A3%E0%B8%B1%E0%B9%89%E0%B8%87%E0%B9%83%E0%B8%AB%E0%B8%8D%E0%B9%88%E0%B8%82%E0%B8%99%E0%B8%B2%E0%B8%94+7.3+Tbps+%E0%B9%84%E0%B8%94%E0%B9%89%E0%B8%AD%E0%B8%A2%E0%B9%88%E0%B8%B2%E0%B8%87%E0%B9%84%E0%B8%A3&url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fdefending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos%2F)[](https://www.threads.net/intent/post?text=%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9B%E0%B8%81%E0%B8%9B%E0%B9%89%E0%B8%AD%E0%B8%87%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%80%E0%B8%97%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B9%80%E0%B8%99%E0%B9%87%E0%B8%95%3A+Cloudflare+%E0%B8%9A%E0%B8%A5%E0%B9%87%E0%B8%AD%E0%B8%81%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%82%E0%B8%88%E0%B8%A1%E0%B8%95%E0%B8%B5+DDoS+%E0%B8%84%E0%B8%A3%E0%B8%B1%E0%B9%89%E0%B8%87%E0%B9%83%E0%B8%AB%E0%B8%8D%E0%B9%88%E0%B8%82%E0%B8%99%E0%B8%B2%E0%B8%94+7.3+Tbps+%E0%B9%84%E0%B8%94%E0%B9%89%E0%B8%AD%E0%B8%A2%E0%B9%88%E0%B8%B2%E0%B8%87%E0%B9%84%E0%B8%A3+https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fdefending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos%2F)

## แท็กที่เกี่ยวข้อง

[DDoS](https://blog.cloudflare.com/th-th/tag/ddos/)[รายงาน DDoS](https://blog.cloudflare.com/th-th/tag/ddos-reports/)

ติดตามบนโซเชียลมีเดีย

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## สมัครรับการแจ้งเตือนโพสต์ใหม่

อีเมล

เราจะไม่เปิดเผยอีเมลของคุณ

สมัคร

ขอบคุณที่สมัครรับข่าวสาร! โปรดตรวจสอบกล่องจดหมายเพื่อยืนยัน
