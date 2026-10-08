---
url: https://blog.cloudflare.com/th-th/extending-cloudflares-zero-trust-platform-to-support-udp-and-internal-dns/
title: \u0e02\u0e22\u0e32\u0e22\u0e41\u0e1e\u0e25\u0e15\u0e1f\u0e2d\u0e23\u0e4c\u0e21 Zero Trust \u0e02\u0e2d\u0e07 Cloudflare \u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e23\u0e2d\u0e07\u0e23\u0e31\u0e1a UDP \u0e41\u0e25\u0e30 DNS \u0e20\u0e32\u0e22\u0e43\u0e19 | \u0e1a\u0e25\u0e47\u0e2d\u0e01 Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:46:13.569465+00:00
---

# ขยายแพลตฟอร์ม Zero Trust ของ Cloudflare เพื่อรองรับ UDP และ DNS ภายใน | บล็อก Cloudflare

> Source: https://blog.cloudflare.com/th-th/extending-cloudflares-zero-trust-platform-to-support-udp-and-internal-dns/

[บล็อก](https://blog.cloudflare.com/th-th/)

[CIO Week](https://blog.cloudflare.com/th-th/tag/cio-week/)[Cloudflare One](https://blog.cloudflare.com/th-th/tag/cloudflare-one/)[Cloudflare Tunnel](https://blog.cloudflare.com/th-th/tag/cloudflare-tunnel/)+3แสดงแท็กเพิ่มเติม 3 รายการ

6 แท็กแสดง 6 แท็ก

  * แท็กของโพสต์
  * [Cloudflare Tunnel](https://blog.cloudflare.com/th-th/tag/cloudflare-tunnel/)[Zero Trust](https://blog.cloudflare.com/th-th/tag/zero-trust/)[ข่าวผลิตภัณฑ์](https://blog.cloudflare.com/th-th/tag/product-news/)
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



[UDP](https://blog.cloudflare.com/th-th/tag/udp/)[Zero Trust](https://blog.cloudflare.com/th-th/tag/zero-trust/)[ข่าวผลิตภัณฑ์](https://blog.cloudflare.com/th-th/tag/product-news/)

[CIO Week](https://blog.cloudflare.com/th-th/tag/cio-week/)[Cloudflare One](https://blog.cloudflare.com/th-th/tag/cloudflare-one/)[Cloudflare Tunnel](https://blog.cloudflare.com/th-th/tag/cloudflare-tunnel/)[UDP](https://blog.cloudflare.com/th-th/tag/udp/)[Zero Trust](https://blog.cloudflare.com/th-th/tag/zero-trust/)[ข่าวผลิตภัณฑ์](https://blog.cloudflare.com/th-th/tag/product-news/)

8 ธันวาคม 2564

# ขยายแพลตฟอร์ม Zero Trust ของ Cloudflare เพื่อรองรับ UDP และ DNS ภายใน

![Abe Carryl](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46JJ6YPQY3M4A69P72QXE8.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Abe Carryl](https://blog.cloudflare.com/th-th/author/abe/)

อ่าน 3 นาที

คัดลอก URL

โพสต์นี้มีให้อ่านใน [English](https://blog.cloudflare.com/extending-cloudflares-zero-trust-platform-to-support-udp-and-internal-dns/) [日本語](https://blog.cloudflare.com/ja-jp/extending-cloudflares-zero-trust-platform-to-support-udp-and-internal-dns/) [简体中文](https://blog.cloudflare.com/zh-cn/extending-cloudflares-zero-trust-platform-to-support-udp-and-internal-dns/) และ[Bahasa Indonesia](https://blog.cloudflare.com/id-id/extending-cloudflares-zero-trust-platform-to-support-udp-and-internal-dns/).

![Extending Cloudflare’s Zero Trust platform to support UDP and Internal DNS](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW458X27BH42R38GENAX3HNY.png&w=1801&h=1013&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////////9e3p693R7NvN8uTa9e3q8/Dz////////7+Xd4cq54MSu6dPC7+Xd8fDv///////+697S2Lee1qyL4MKp697R8fHs////////7ODS17WZ1KeC37+k7ODR8/bu////////9Ovg4Mey3r2j6NG89Ovf+f33/////////vv07+PX7t7P9+vf/vv0/////////////////Pny/Pjw///7///////////////////////8///8////////////)

ในช่วงสิ้นปี 2020 Cloudflare ช่วยให้องค์กรต่างๆ สามารถเริ่ม [สร้างเครือข่ายส่วนตัว](https://blog.cloudflare.com/build-your-own-private-network-on-cloudflare/) บนเครือข่ายของเรา โดยใช้ Cloudflare Tunnel ในฝั่งเซิร์ฟเวอร์ และ Cloudflare Warp ในฝั่งลูกค้า ทำให้ความต้องการใช้ VPN แบบดั้งเดิมถูกกำจัดไป ข้ามมาที่ปัจจุบัน องค์กรมากมายได้เดินตามเส้นทางนี้กับเรา — ถอนตัวรวมช่องสัญญาณ VPN ไฟร์วอลล์ภายใน และตัวบาลานซ์โหลดแบบดั้งเดิมออกไป พวกเขาได้กำจัดความจำเป็นในการดูแลรักษาฮาร์ดแวร์ดั้งเดิมนี้ไป พวกเขาพัฒนาความเร็วให้กับผู้ใช้ขึ้นอย่างมาก และยังรักษากฎ Zero Trust ในองค์กรได้อีกด้วย

เราเริ่มจาก TCP ที่ทรงพลังเนื่องจากการที่ช่วยทำให้สามารถทำกรณีการใช้งานที่สำคัญต่างๆ ได้มากมาย แต่การจะแทนที่ VPN ได้จริงนั้นคุณต้องสามารถครอบคลุม UDP ได้ด้วย เริ่มตั้งแต่วันนี้ เราตื่นเต้นที่จะให้สิทธิ์การเข้าถึงล่วงหน้าของ UDP บนแพลตฟอร์ม Zero Trust ของ Cloudflare และยิ่งดีขึ้นจากผลการสนับสนุนของ UDP ทำให้เราเสนอบริการ DNS ภายในได้ — ดังนั้นจึงไม่จำเป็นต้องย้ายชื่อโฮสต์ส่วนตัวกว่าพันรายการเองเพื่อแทนที่กฎ DNS คุณสามารถเริ่มต้นกับ Cloudflare for Teams ได้ฟรีวันนี้โดยลงชื่อ [ที่นี่](https://dash.cloudflare.com/sign-up/teams) และหากคุณสนใจเข้าชื่อรอเพื่อรับสิทธิ์การเข้าถึงล่วงหน้าของ UDP และ DNS ภายใน กรุณาไป[ที่นี่](https://cloudflare.com/zero-trust/lp/private-dns-waitlist)

## **โทโพโลยีของเครือข่ายส่วนตัวบน Cloudflare**

การสร้างเครือข่ายส่วนตัวต้องมีองค์ประกอบพื้นฐานสองอย่าง คือ ฝั่งโครงสร้างพื้นฐาน และฝั่งลูกค้าโครงสร้างพื้นฐาน

ฝั่งโครงสร้างพื้นฐานของความสมดุลดำเนินการโดย Cloudflare Tunnel ซึ่งจะเชื่อมต่อกับโครงสร้างพื้นฐานของคุณอย่างง่ายดาย (ไม่ว่าจะเป็นแอปพลิเคชันเดียว หลายแอปพลิเคชัน หรือกลุ่มเครือข่ายทั้งหมด) เข้ากับ Cloudflare ซึ่งจะเป็นไปได้ด้วยการใช้งานดีมอน command-line ทั่วไปในสภาพแวดล้อมของคุณเพื่อสร้างหลายความปลอดภัย การส่งออกเท่านั้น ลิงก์โหลดบาลานซ์ บน Cloudflare พูดง่ายๆ Tunnel จะเชื่อมเครือข่ายของคุณเข้ากับ Cloudflare

ในอีกฝั่งของสมการ เราต้องการให้ผู้ใช้ของคุณสามารถเชื่อมต่อได้อย่างง่ายดายกับ Cloudflare และสิ่งที่สำคัญกว่าคือ เครือข่ายของคุณ การเชื่อมต่อได้รับการจัดการโดยเครื่องมือที่แข็งแกร่งของลูกค้า [Cloudflare Warp](https://blog.cloudflare.com/warp-for-desktop/) ลูกค้ารายนี้สามารถใช้งานได้กับทั้งองค์กรของคุณในเวลาเพียงไม่กี่นาทีโดยใช้เครื่องมือ MDM ในองค์กรของคุณ และจะสร้างการเชื่อมต่อที่ปลอดภัยด้วย WireGuard จากอุปกรณ์ผู้ใช้ของคุณเข้ากับเครือข่าย Cloudflare

ตอนนี้เราก็เชื่อมต่อโครงสร้างพื้นฐานของคุณและผู้ใช้ของคุณเข้ากับ Cloudflare ได้แล้ว การแท็กแอปพลิเคชันและเลเยอร์บนการควบคุมความปลอดภัย Zero Trust จะเป็นเรื่องง่าย เพื่อยืนยันตัวตนและกฎ device-centric สำหรับการร้องขอแต่ละครั้งและทุกครั้งบนเครือข่ายของคุณ

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-860 Embedded Image - jQyQ7J](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45HM63YMWAAD3TWM6XH83F.png&w=715&h=340&f=webp&fit=cover&position=center)

แม้ว่าในตอนนี้ จะรองรับเพียง TCP เท่านั้น

## **การขยาย Zero Trust ของ Cloudflare เพื่อรองรับ UDP**

เมื่อปีที่ผ่านมาที่มีผู้ใช้งานแพลตฟอร์ม Zero Trust ของ Cloudflare มากขึ้นเรื่อยๆ เราได้รวบรวมข้อมูลเกี่ยวกับกรณีการใช้งานที่ยังใช้งาน VPN อยู่ จากข้อมูล ความจำเป็นที่พบมากที่สุดคือการรองรับที่ครอบคลุมสำหรับการรับส่งข้อมูลตาม UDP โปรโตคอลที่ทันสมัยอย่าง QUIC มีความได้เปรียบจากโครงสร้างขนาดเล็กของ UDP — และที่ Cloudflare เราเชื่อว่ามันเป็นส่วนหนึ่งในภารกิจของเราที่จะทำให้มาตรฐานนี้ก้าวหน้าขึ้นเพื่อช่วยสร้างอินเทอร์เน็ตที่ดีขึ้น

วันนี้ เราตื่นเต้นที่จะเปิดรายชื่อรออย่างเป็นทางการสำหรับคนที่ต้องการสิทธิ์การเข้าถึงล่วงหน้าของ Cloudflare for Teams กับการรองรับ UDP

### **UDP คืออะไร แล้วทำไมถึงมีความสำคัญ**

UDP เป็นองค์ประกอบสำคัญของอินเทอร์เน็ต หากไม่มี UDP แอปพลิเคชันหลายตัวอาจใช้งานได้ไม่เพียงพออย่างมากสำหรับการใช้งานที่ทันสมัย แอปพลิเคชันที่ขึ้นอยู่กับการติดต่อสื่อสารแบบเกือบจะเรียลไทม์ เช่น วิดีโอสตรีมมิ่ง หรือ การบริการ VoIP เป็นตัวอย่างที่ดีที่สุดว่าทำไมเราต้องการ UDP และบทบาทที่จะเข้ามาเติมเต็มการใช้งานอินเทอร์เน็ต แต่สิ่งสำคัญของ TCP และ UDP ให้ผลลัพธ์ที่เหมือนกัน — เพียงแค่ใช้วิธีการแตกต่างกัน แต่ละอย่างก็มีข้อดีและข้อเสียที่โดดเด่นแตกต่างกันไป ซึ่งมักจะรู้สึกว่าเป็นการส่งข้อมูลไปที่ผู้ใช้งานโดยแอปพลิเคชันที่ใช้งาน

นี่เป็นตัวอย่างว่าทั้งสองอย่างทำงานอย่างไร เปรียบเทียบว่า ถ้าคุณจะถามคำถามกับใครสักคน TCP น่าจะดูคุ้นเคยอยู่บ้าง คุณคงจะกล่าวสวัสดี รอให้เขาตอบสวัสดีกลับมา ถามว่าเป็นยังไงบ้าง รอให้เขาตอบ แล้วจึงถามสิ่งที่คุณอยากถาม

ในทางกลับกัน UDP เหมือนเป็นการเดินเข้าไปหาใครสักคนแล้วถามสิ่งที่คุณอยากถามโดยไม่ได้ตรวจสอบให้มั่นใจว่าเขากำลังฟังอยู่ไหม ด้วยวิธีการนี้ คำถามของคุณอาจตกหล่นไปบ้าง แต่ก็ไม่มีปัญหาอะไรถ้าคุณยังได้คำตอบอยู่

เหมือนการสนทนาด้านบน ด้วย UDP แอปพลิเคชันหลายตัวไม่สนใจว่าข้อมูลบางอย่างจะหายไป วิดีโอสตรีมมิ่งหรือเซิร์ฟเวอร์เกมเป็นตัวอย่างที่ดีในกรณีนี้ ถ้าคุณต้องสูญเสียแพ็กเก็ตไประหว่างการสตรีม คุณคงไม่อยากให้การสตรีมทั้งหมดถูกรบกวนจนกว่าจะได้รับแพ็กเก็ตนี้ — คุณคงจะทิ้งแพ็กเก็ตนั้นและดำเนินการต่อไป อีกหนึ่งเหตุผลที่ผู้พัฒนาแอปพลิเคชันอาจใช้ UDP ก็เพราะพวกเขาจะโอนย้ายไปเพื่อพัฒนาการควบคุมของตนเองในการเชื่อมต่อ การส่งข้อมูล และการควบคุมคุณภาพ มากกว่าที่จะใช้ตัวพื้นฐานของ TCP

สำหรับ Cloudflare การรองรับแบบครบวงจรสำหรับการรับส่งข้อมูลฝั่ง UDP จะปลดล็อกกรณีการใช้งานใหม่ๆ มากมาย นี่อาจจะเป็นสิ่งน่าตื่นเต้นที่เราคิดว่าคุณอาจจะเห็นด้วย

### **ตัวแก้ไข DNS ภายใน**

เครือข่ายองค์กรส่วนใหญ่ต้องใช้ตัวแก้ไข DNS ภายในเพื่อเผยแพร่การเข้าถึงแหล่งข้อมูลที่มีอยู่ในอินทราเน็ต อินทราเน็ตของคุณต้องการตัวแก้ไข DNS ภายในด้วยเหตุผลที่เหมือนกันหลายประการที่อินเทอร์เน็ตต้องการตัวแก้ไข DNS สาธารณะ พูดสั้นๆ ได้ว่า มนุษย์เก่งในหลายๆ ด้าน แต่การจดจำตัวเลขยาวๆ (ในกรณีคือ IP address) ไม่ใช่หนึ่งในนั้น ตัวแก้ไข DNS สาธารณะและภายในถูกออกแบบมาเพื่อแก้ปัญหานี้ (และ[มากกว่า](https://www.cloudflare.com/learning/dns/what-is-dns/)) สำหรับเรา

ในโลกขององค์กร การต้องบอกให้ผู้ใช้ภายในไปที่ 192.168.0.1 เพื่อเข้าถึง Sharepoint หรือ OneDrive ย่อมเป็นความยากลำบากโดยไม่จำเป็น แทนที่จะทำเช่นนั้น มันคงง่ายขึ้นถ้าสร้างการกรอกข้อมูล DNS สำหรับแต่ละแหล่งข้อมูลและให้ตัวแก้ไขภายในจัดการกับการส่งข้อมูลให้กับผู้ใช้ของคุณ เพราะมนุษย์เก่งในด้านนี้

เบื้องหลังการทำงาน โดยปกติแล้วการร้องขอ DNS จะประกอบด้วยการหนึ่งร้องขอ UDP จากลูกค้า แล้วเซิร์ฟเวอร์ก็จะตอบกลับลูกค้าเพียงครั้งเดียว เนื่องจากการรร้องขอ DNS มีขนาดไม่ใหญ่ จึงสามารถรับส่งได้ในแพ็กเก็ตเดียว จึงทำให้การรองรับ UDP ในแพลตฟอร์ม Zero Trust ของเราเป็นตัวเปิดใช้งานสำคัญที่จะทำให้ไม่ต้องใช้ VPN

### **แอปพลิเคชันของลูกค้ารายใหญ่**

กรณีการใช้งานที่พบบ่อยอีกอย่างหนึ่ง คือ แอปพลิเคชันของลูกค้ารายใหญ่ ข้อดีของ UDP ที่เราได้กล่าวไปแล้วคือโปรโตคอลแบบลีน เพราะมี [handshake แบบสามทิศทาง](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/)ของ TCP และมาตรการอื่นๆ เพราะความน่าเชื่อถือได้ถูกถอดออกไปจากการออกแบบ ในหลายๆ กรณี ผู้พัฒนาแอปพลิเคชันยังคงต้องการการควบคุมความน่าเชื่อถือนี้ แต่ก็มีความคุ้นเคยกับแอปพลิเคชันและรู้ว่าการควบคุมนี้จะามารถจัดการได้ดีขึ้นโดยการปรับให้เหมาะสมกับแอปพลิเคชันของพวกเขา แอปพลิเคชันของลูกค้ารายใหญ่นี้มักจะมีการทำงานฟังก์ชันธุรกิจที่สำคัญและต้องรองรับการโอนย้ายแบบครบวงจรอีกด้วย ตัวอย่างเช่น Outlook เวอร์ชันดั้งเดิมอาจมีการปรับใช้ผ่านลูกค้ารายใหญ่ที่การดำเนินการส่วนใหญ่ทำโดยเครื่องท้องถิ่นและมีเพียงการตอบโต้ที่เชื่อมต่อกับเซิร์ฟเวอร์ Exchange เท่านั้นที่ทำงานผ่าน UDP

ย้ำอีกครั้งว่าการรองรับ UDP บนแพลตฟอร์ม Zero Trust ของเราหมายความว่าแอปพลิเคชันประเภทนี้จะไม่ต้องใช้ VPN แบบดั้งเดิมอีกต่อไป

### **และยิ่งไปกว่านั้น...**

การรับส่งข้อมูลทางอินเทอร์เน็ตโลกเป็นการส่งผ่าน UDP ในสัดส่วนที่ใหญ่มาก บ่อยครั้งที่ผู้คนเปรียบเทียบแอปพลิเคชันที่ขึ้นอยู่กับเวลากับ UDP ที่บางครั้งการวางแพ็กเก็ตก็ดีกว่าการต้องรอเฉยๆ — แต่ก็ยังมีกรณีการใช้งานอื่นๆ และเราก็ตื่นเต้นที่จะให้การรองรับที่ครอบคลุม

## **ฉันจะเริ่มต้นใช้งานวันนี้เลยได้อย่างไร**

คุณสามารถเริ่มต้นสร้างเครือข่ายส่วนตัวบน Cloudflare ด้วยการสอนใช้งานและคำแนะนำของเราในเอกสารของผู้พัฒนา ด้านล่างนี้คือเส้นทางที่สำคัญ และหากคุณเป็นลูกค้าอยู่แล้ว และสนใจร่วมเข้าชื่อรอเพื่อการเข้าถึง UDP และ DNS ภายใน กรุณาข้ามไปที่ช่วงสุดท้ายของโพสต์นี้!

### **เชื่อมต่อเครือข่ายของคุณกับ Cloudflare**

อันดับแรก คุณต้อง [ติดตั้ง cloudflared](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation) บนเครือข่ายของคุณและยืนยันการติดตั้งด้วยคำสั่งด้านล่างนี้

ต่อไป คุณต้องสร้าง tunnel ด้วยชื่อผู้ใช้ที่เป็นมิตรเพื่อยืนยันเครือข่ายหรือสภาพแวดล้อมของคุณ
    
    
    cloudflared tunnel login

สุดท้าย คุณต้องกำหนดค่า tunnel ของคุณด้วย IP/CIDR ของเครือข่ายคุณ การดำเนินการนี้คุณได้ทำให้ agent ของ Cloudflare WARP รู้ว่าการร้องขอใดๆ จาก IP นี้จะต้องนำทางมาที่ tunnel ใหม่ของเรา
    
    
    cloudflared tunnel create acme-network

หลังจากนั้น สิ่งที่คุณต้องทำก็คือเปิดใช้งาน tunnel ของคุณ!
    
    
    cloudflared tunnel route ip add 192.168.0.1/32

### **เชื่อมต่อผู้ใช้กับเครือข่ายของคุณ**

การเชื่อมต่อผู้ใช้คนแรก เริ่มจากดาวน์โหลด agent Cloudflare WARP บนอุปกรณ์ที่ต้องการเชื่อมต่อ แล้วทำตามขั้นตอนการติดตั้ง

จากนั้น ไปที่ [แดชบอร์ด Teams](https://dash.teams.cloudflare.com/) และระบุคนที่จะอนุญาตให้เข้าถึงเครือข่าย โดยสร้างนโยบายการลงทะเบียน ซึ่งสามารถสร้างได้ที่ ตั้งค่า > อุปกรณ์ > การลงทะเบียนอุปกรณ์ จากตัวอย่างด้านล่างจะเห็นได้ว่าเรากำหนดว่าผู้ใช้ต้องอาศัยอยู่ในแคนาดาและมีที่อยู่อีเมลลงท้ายด้วย @cloudflare.com

เมื่อคุณสร้างนโยบายเรียบร้อยแล้ว คุณสามารถลงทะเบียนอุปกรณ์แรดได้โดยคลิกที่ไอคอน WARP ที่หน้า desktop บนเครื่องของคุณและไปที่ การตั้งค่า > บัญชี > ลงชื่อเข้าใช้ด้วย Teams

ท้ายที่สุด เราจะลบ IP ที่ได้เพิ่มเข้าไปใน Tunnel ของเราจากรายการที่ไม่ได้รวมอยู่ด้วยใน ตั้งค่า > เครือข่าย > Split Tunnels ซึ่งจะทำให้มั่นใจว่าการรับส่งข้อมูลจะนำทางมาที่ Cloudflare และส่งไปยังเครือข่าย Tunnel ส่วนตัวตามที่ต้องการ

นอกเหนือจากการสอนใช้งานข้างต้นแล้ว เรายังมีคำแนะนำในผลิตภัณฑ์ของแดชบอร์ด Teams ซึ่งจะกล่าวถึงรายละเอียดที่ลึกลงไปในแต่ละขั้นตอน และยังมีการตรวจสอบระหว่างการดำเนินการอีกด้วย

การสร้าง Tunnel แรกของคุณ ไปที่ [การเข้าถึง > Tunnels](https://dash.teams.cloudflare.com/access/tunnels)

การลงทะเบียนอุปกรณ์แรกใน WARP ไปที่ [Team ของฉัน > อุปกรณ์](https://dash.teams.cloudflare.com/team/devices)

## **แล้วยังไงต่อ**

เราตื่นเต้นที่จะเปิด [การเข้าชื่อรอ](https://cloudflare.com/zero-trust/lp/private-dns-waitlist) วันนี้ และตื่นเต้นยิ่งกว่าที่จะเปิดตัวคุณลักษณะนี้ในสัปดาห์ที่จะถึงนี้ เราเพิ่งเริ่มต้นกับเครือข่าย Tunnels ส่วนตัว และมีแผนที่เพิ่มการสนับสนุน Access Rules ของ Zero Trust สำหรับการร้องขอและชื่อโฮสต์ DNS ภายใน หลังจากการเปิดตัว นอกจากนี้เรายังพยายามที่จะวัดประสิทธิภาพการทำงานและทำให้มั่นใจว่าเรายังเป็นแพลตฟอร์ม Zero Trust ที่เร็วที่สุด — ทำให้การเลือกใช้งานกับเราเป็นเรื่องน่ายินดีสำหรับผู้ใช้ของคุณ เมื่อเปรียบเทียบกับความยากลำบากในการใช้งาน VPN แบบดั้งเดิม

ในหน้านี้

สนทนาออนไลน์

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fextending-cloudflares-zero-trust-platform-to-support-udp-and-internal-dns%2F&t=%E0%B8%82%E0%B8%A2%E0%B8%B2%E0%B8%A2%E0%B9%81%E0%B8%9E%E0%B8%A5%E0%B8%95%E0%B8%9F%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B8%A1%20Zero%20Trust%20%E0%B8%82%E0%B8%AD%E0%B8%87%20Cloudflare%20%E0%B9%80%E0%B8%9E%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%A3%E0%B8%AD%E0%B8%87%E0%B8%A3%E0%B8%B1%E0%B8%9A%20UDP%20%E0%B9%81%E0%B8%A5%E0%B8%B0%20DNS%20%E0%B8%A0%E0%B8%B2%E0%B8%A2%E0%B9%83%E0%B8%99)[](https://x.com/intent/post?text=%E0%B8%82%E0%B8%A2%E0%B8%B2%E0%B8%A2%E0%B9%81%E0%B8%9E%E0%B8%A5%E0%B8%95%E0%B8%9F%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B8%A1+Zero+Trust+%E0%B8%82%E0%B8%AD%E0%B8%87+Cloudflare+%E0%B9%80%E0%B8%9E%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%A3%E0%B8%AD%E0%B8%87%E0%B8%A3%E0%B8%B1%E0%B8%9A+UDP+%E0%B9%81%E0%B8%A5%E0%B8%B0+DNS+%E0%B8%A0%E0%B8%B2%E0%B8%A2%E0%B9%83%E0%B8%99&url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fextending-cloudflares-zero-trust-platform-to-support-udp-and-internal-dns%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fextending-cloudflares-zero-trust-platform-to-support-udp-and-internal-dns%2F)[](https://bsky.app/intent/compose?text=%E0%B8%82%E0%B8%A2%E0%B8%B2%E0%B8%A2%E0%B9%81%E0%B8%9E%E0%B8%A5%E0%B8%95%E0%B8%9F%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B8%A1+Zero+Trust+%E0%B8%82%E0%B8%AD%E0%B8%87+Cloudflare+%E0%B9%80%E0%B8%9E%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%A3%E0%B8%AD%E0%B8%87%E0%B8%A3%E0%B8%B1%E0%B8%9A+UDP+%E0%B9%81%E0%B8%A5%E0%B8%B0+DNS+%E0%B8%A0%E0%B8%B2%E0%B8%A2%E0%B9%83%E0%B8%99+https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fextending-cloudflares-zero-trust-platform-to-support-udp-and-internal-dns%2F)[](https://mastodonshare.com/?text=%E0%B8%82%E0%B8%A2%E0%B8%B2%E0%B8%A2%E0%B9%81%E0%B8%9E%E0%B8%A5%E0%B8%95%E0%B8%9F%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B8%A1+Zero+Trust+%E0%B8%82%E0%B8%AD%E0%B8%87+Cloudflare+%E0%B9%80%E0%B8%9E%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%A3%E0%B8%AD%E0%B8%87%E0%B8%A3%E0%B8%B1%E0%B8%9A+UDP+%E0%B9%81%E0%B8%A5%E0%B8%B0+DNS+%E0%B8%A0%E0%B8%B2%E0%B8%A2%E0%B9%83%E0%B8%99&url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fextending-cloudflares-zero-trust-platform-to-support-udp-and-internal-dns%2F)[](https://www.threads.net/intent/post?text=%E0%B8%82%E0%B8%A2%E0%B8%B2%E0%B8%A2%E0%B9%81%E0%B8%9E%E0%B8%A5%E0%B8%95%E0%B8%9F%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B8%A1+Zero+Trust+%E0%B8%82%E0%B8%AD%E0%B8%87+Cloudflare+%E0%B9%80%E0%B8%9E%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%A3%E0%B8%AD%E0%B8%87%E0%B8%A3%E0%B8%B1%E0%B8%9A+UDP+%E0%B9%81%E0%B8%A5%E0%B8%B0+DNS+%E0%B8%A0%E0%B8%B2%E0%B8%A2%E0%B9%83%E0%B8%99+https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fextending-cloudflares-zero-trust-platform-to-support-udp-and-internal-dns%2F)

## แท็กที่เกี่ยวข้อง

[CIO Week](https://blog.cloudflare.com/th-th/tag/cio-week/)[Cloudflare One](https://blog.cloudflare.com/th-th/tag/cloudflare-one/)[Cloudflare Tunnel](https://blog.cloudflare.com/th-th/tag/cloudflare-tunnel/)[UDP](https://blog.cloudflare.com/th-th/tag/udp/)[Zero Trust](https://blog.cloudflare.com/th-th/tag/zero-trust/)[ข่าวผลิตภัณฑ์](https://blog.cloudflare.com/th-th/tag/product-news/)

ติดตามบนโซเชียลมีเดีย

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## สมัครรับการแจ้งเตือนโพสต์ใหม่

อีเมล

เราจะไม่เปิดเผยอีเมลของคุณ

สมัคร

ขอบคุณที่สมัครรับข่าวสาร! โปรดตรวจสอบกล่องจดหมายเพื่อยืนยัน
