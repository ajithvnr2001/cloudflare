---
url: https://blog.cloudflare.com/th-th/pii-and-selective-logging-controls-for-cloudflares-zero-trust-platform/
title: \u0e01\u0e32\u0e23\u0e04\u0e27\u0e1a\u0e04\u0e38\u0e21 PII \u0e41\u0e25\u0e30 Selective Logging \u0e2a\u0e33\u0e2b\u0e23\u0e31\u0e1a\u0e41\u0e1e\u0e25\u0e15\u0e1f\u0e2d\u0e23\u0e4c\u0e21 Zero Trust \u0e02\u0e2d\u0e07 Cloudflare | \u0e1a\u0e25\u0e47\u0e2d\u0e01 Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:46:18.479993+00:00
---

# การควบคุม PII และ Selective Logging สำหรับแพลตฟอร์ม Zero Trust ของ Cloudflare | บล็อก Cloudflare

> Source: https://blog.cloudflare.com/th-th/pii-and-selective-logging-controls-for-cloudflares-zero-trust-platform/

[บล็อก](https://blog.cloudflare.com/th-th/)

[CIO Week](https://blog.cloudflare.com/th-th/tag/cio-week/)[Cloudflare Gateway](https://blog.cloudflare.com/th-th/tag/gateway/)[Cloudflare One](https://blog.cloudflare.com/th-th/tag/cloudflare-one/)+3แสดงแท็กเพิ่มเติม 3 รายการ

6 แท็กแสดง 6 แท็ก

  * แท็กของโพสต์
  * [Cloudflare Gateway](https://blog.cloudflare.com/th-th/tag/gateway/)[ความปลอดภัย](https://blog.cloudflare.com/th-th/tag/security/)
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



[Firewall](https://blog.cloudflare.com/th-th/tag/firewall/)[Logs](https://blog.cloudflare.com/th-th/tag/logs/)[ความปลอดภัย](https://blog.cloudflare.com/th-th/tag/security/)

[CIO Week](https://blog.cloudflare.com/th-th/tag/cio-week/)[Cloudflare Gateway](https://blog.cloudflare.com/th-th/tag/gateway/)[Cloudflare One](https://blog.cloudflare.com/th-th/tag/cloudflare-one/)[Firewall](https://blog.cloudflare.com/th-th/tag/firewall/)[Logs](https://blog.cloudflare.com/th-th/tag/logs/)[ความปลอดภัย](https://blog.cloudflare.com/th-th/tag/security/)

6 ธันวาคม 2564

# การควบคุม PII และ Selective Logging สำหรับแพลตฟอร์ม Zero Trust ของ Cloudflare

![Ankur Aggarwal](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47NKH772PAS2QKG6BFKRHR.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Abe Carryl](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46JJ6YPQY3M4A69P72QXE8.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Ankur Aggarwal](https://blog.cloudflare.com/th-th/author/ankur/)และ[Abe Carryl](https://blog.cloudflare.com/th-th/author/abe/)

อ่าน 2 นาที

คัดลอก URL

โพสต์นี้มีให้อ่านใน [English](https://blog.cloudflare.com/pii-and-selective-logging-controls-for-cloudflares-zero-trust-platform/) [日本語](https://blog.cloudflare.com/ja-jp/pii-and-selective-logging-controls-for-cloudflares-zero-trust-platform/) [简体中文](https://blog.cloudflare.com/zh-cn/pii-and-selective-logging-controls-for-cloudflares-zero-trust-platform/) และ[Bahasa Indonesia](https://blog.cloudflare.com/id-id/pii-and-selective-logging-controls-for-cloudflares-zero-trust-platform/).

![PII and Selective Logging controls for Cloudflare’s Zero Trust platform](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW464M9Q06RY516BXK2535GP.png&w=964&h=537&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA//rq+/Lh8ePR69vK7uPU8+3e8ezc6eLP//7t/PXk7+PT59rN7OPZ8u7l8e7i6uTT///y/vnp7uXX5dvT6uTh8/Ht8/Lp7OjX///3//3u8One59/b7Ono9vb09/fv8O3d///7///z9vHm7ujj8/Hv/Pz4/Pzz9fLi///9///4/vnt9/Lr+/rz///6///0+vfl///////7///z//rx///2///6///0/vrn///////8///1//3z///3///6///0//vo)

ที่ Cloudflare เราเชื่อว่าคุณไม่ควรต้องผ่อนปรนเรื่องความเป็นส่วนตัวเพื่อแลกกับความปลอดภัย ปีที่แล้ว เราได้เปิดตัว Cloudflare Gateway ซึ่งเป็นเว็บเกตเวย์ที่ปลอดภัยและครอบคลุม ซึ่งมาพร้อมการควบคุมการเรียกดู Zero Trust ในตัวสำหรับองค์กรของคุณ และสำหรับวันนี้ เรารู้สึกตื่นเต้นที่จะได้แบ่งปันชุดคุณสมบัติความเป็นส่วนตัวล่าสุดที่มีให้สำหรับผู้ดูแลระบบเพื่อบันทึกและตรวจสอบกิจกรรมตามความต้องการของทีมของคุณ

### **การปกป้ององค์กรของคุณ**

Cloudflare Gateway ช่วยให้องค์กรสามารถแทนที่ไฟร์วอลล์แบบเดิม พร้อม ๆ กับที่ยังใช้การควบคุม Zero Trust สำหรับผู้ใช้ของตนได้ เกตเวย์พบคุณในทุกที่ที่ผู้ใช้ของคุณอยู่ และอนุญาตให้ผู้ใช้เชื่อมต่ออินเทอร์เน็ตหรือแม้แต่เครือข่ายส่วนตัวของคุณที่ทำงานบน Cloudflare ผลที่ได้คือการรักษาความปลอดภัยของคุณมีขอบเขตกว้างขวางขึ้นโดยไม่ต้องซื้อหรือบำรุงรักษาสิ่งใดๆ เพิ่มเติม

องค์กรยังได้รับประโยชน์จากการปรับปรุงประสิทธิภาพการทำงานของผู้ใช้นอกเหนือจากแค่ลบ backhaul ของการรับส่งข้อมูลไปยังสำนักงานหรือศูนย์ข้อมูลเพียงอย่างเดียว เครือข่ายของ Cloudflare นำเสนอตัวกรองความปลอดภัยที่ใกล้ชิดกับผู้ใช้ยิ่งกว่าเดิมในกว่า 250 เมืองทั่วโลก ลูกค้าเริ่มต้นการเชื่อมต่อโดยใช้[บริการแปลง DNS ที่เร็วที่สุดในโลก](https://blog.cloudflare.com/announcing-1111/) เมื่อเชื่อมต่อแล้ว Cloudflare จะกำหนดเส้นทางการรับส่งข้อมูลอย่างชาญฉลาดผ่านเครือข่ายของเราด้วยเครือข่ายเลเยอร์ 4 และตัวกรอง HTTP เลเยอร์ 7

ในการเริ่มต้น ผู้ดูแลระบบต้องปรับใช้ไคลเอนต์ของ Cloudflare (WARP) บนอุปกรณ์ของผู้ใช้ ไม่ว่าอุปกรณ์เหล่านั้นจะเป็น macOS, Windows, iOS, Android, ChromeOS หรือ Linux หลังจากนั้น ไคลเอนต์จะส่งการรับส่งข้อมูลเลเยอร์ 4 ขาออกทั้งหมดไปยัง Cloudflare พร้อมกับข้อมูลยืนยันตัวตนของผู้ใช้บนอุปกรณ์

เมื่อเปิดใช้พร็อกซีและการถอดรหัสลับ TLS แล้ว Cloudflare จะบันทึกการรับส่งข้อมูลทั้งหมดที่ส่งผ่านเกตเวย์และแสดงข้อมูลนี้ในแดชบอร์ดของ Cloudflare ในรูปแบบของไฟล์บันทึกดิบและการวิเคราะห์แบบสรุปรวม แต่ในบางกรณี ผู้ดูแลระบบอาจไม่ต้องการเก็บไฟล์บันทึกหรือให้สิทธิ์เข้าถึงกับสมาชิกทุกคนในทีมรักษาความปลอดภัย

เหตุผลอาจแตกต่างกันไป แต่ผลลัพธ์สุดท้ายล้วนเหมือนกัน นั่นคือ ผู้ดูแลระบบต้องการความสามารถในการควบคุมวิธีการรวบรวมข้อมูลของผู้ใช้และผู้ที่สามารถตรวจสอบบันทึกเหล่านั้นได้

โซลูชันรุ่นเก่ามักจะให้แค่ค้อนตุลาการทื่อๆ อันเดียวที่เลือกได้แค่เอาหรือไม่เอา แก่ผู้ดูแลระบบ องค์กรสามารถเปิดใช้งานการบันทึกทั้งหมด หรือไม่ก็ปิดใช้งานการบันทึกทั้งหมดเลย หากไม่มีการบันทึก บริการเหล่านั้นจะไม่บันทึกข้อมูลที่สามารถระบุถึงตัวบุคคลได้ (PII) เมื่อหลีกเลี่ยง PII แล้ว ผู้ดูแลระบบก็ไม่ต้องกังวลถึงเรื่องการควบคุมหรือสิทธิ์การเข้าถึง แต่เขาจะสูญเสียความสามารถในการมองภาพรวมทั้งหมดเพื่อตรวจสอบเหตุการณ์ด้านความปลอดภัย

การขาดความเข้าใจในภาพรวมทำให้เกิดความยุ่งยากมากขึ้นเมื่อทีมจำเป็นต้องแก้ไขปัญหาในตั๋วขอความช่วยเหลือจากลูกค้าเพื่อตอบคำถาม เช่น "ทำไมฉันจึงถูกบล็อก", "ทำไมคำขอนั้นจึงไม่ผ่าน" หรือ "ส่วนนี้ไม่ควรถูกบล็อกใช่ไหม" หากไม่มีไฟล์บันทึกที่เกี่ยวข้องกับเหตุการณ์เหล่านี้ ทีมของคุณก็จะไม่สามารถช่วยเหลือผู้ใช้ปลายทางวินิจฉัยปัญหาเหล่านี้ได้

### **การปกป้องข้อมูลของคุณ**

นับตั้งแต่นี้ ทีมของคุณจะมีตัวเลือกเพิ่มเติมเพื่อใช้ตัดสินใจประเภทของข้อมูลของไฟล์บันทึกของ Cloudflare Gateway และบุคคลในองค์กรของคุณที่สามารถตรวจสอบข้อมูลในประเภทนั้นได้ เรากำลังแนะนำการเข้าถึงแดชบอร์ดตามบทบาทสำหรับหน้าการบันทึกและการวิเคราะห์ รวมถึงการบันทึกเหตุการณ์ที่เลือก ซึ่งด้วยสิทธิ์เข้าถึงตามบทบาท ผู้ที่มีสิทธิ์เข้าถึงบัญชีของคุณจะมีข้อมูล PII ที่กันออกจากมุมมองแดชบอร์ดโดยค่าเริ่มต้น

เรารู้สึกตื่นเต้นที่ได้ช่วยองค์กรต่าง ๆ สร้างการควบคุมการจัดการการใช้งาน Cloudflare Gateway ที่มีสิทธิพิเศษน้อยที่สุด สมาชิกในทีมรักษาความปลอดภัยยังคงสามารถจัดการนโยบายหรือตรวจสอบการโจมตีโดยรวมได้ แต่บางเหตุการณ์กำหนดให้ต้องมีการสอบสวนเพิ่มเติม หลังการเปิดตัวในวันนี้ ทีมของคุณจะสามารถมอบหมายความสามารถในการตรวจสอบและค้นหาโดยใช้ PII ให้กับสมาชิกคนใดคนหนึ่งในทีม

เราทราบว่าลูกค้าบางรายต้องการลดไฟล์บันทึกที่จัดเก็บไว้ทั้งหมด เรารู้สึกตื่นเต้นที่จะได้ช่วยแก้ปัญหานั้นด้วย โดยตอนนี้ ผู้ดูแลระบบสามารถเลือกระดับของการบันทึกที่ต้องการให้ Cloudflare จัดเก็บในนามของตน ผู้ดูแลระบบยังสามารถควบคุมระดับการบันทึกนี้สำหรับแต่ละองค์ประกอบ, DNS, เครือข่าย หรือ HTTP และแม้แต่จะเลือกบันทึกแค่เหตุการณ์การบล็อกเท่านั้น

การตั้งค่านั้นไม่ได้หมายความว่าคุณสูญเสียบันทึกทั้งหมด เพียงแค่ Cloudflare จะไม่จัดเก็บบันทึกเหล่านั้น การบันทึกแบบเลือกที่รวมกับ[บริการ Logpush](https://blog.cloudflare.com/export-logs-from-cloudflare-gateway-with-logpush/) ที่เผยแพร่ก่อนหน้านี้ ทำให้ผู้ใช้สามารถหยุดจัดเก็บบันทึกบน Cloudflare และเปิดใช้งาน Logpush ไปยังปลายทางที่เลือกไว้ในตำแหน่งของตนได้อีกด้วย

### **วิธีเริ่มต้นใช้งาน**

ลูกค้า Cloudflare Gateway เริ่มต้นได้ด้วยการเยี่ยมชม[แดชบอร์ด Cloudflare for Teams](https://dash.teams.cloudflare.com/settings/network) และไปที่การตั้งค่า > เครือข่าย ตัวเลือกแรกในหน้านี้จะเป็นการระบุการตั้งค่าที่คุณจะใช้กับการบันทึกกิจกรรม ซึ่งตามค่าเริ่มต้นนั้น Gateway จะบันทึกเหตุการณ์ทั้งหมด รวมถึงการสืบค้น DNS, คำขอ HTTP และเซสชันเครือข่าย ส่วนในหน้าการตั้งค่าเครือข่าย คุณจะปรับเปลี่ยนประเภทเหตุการณ์ที่ต้องการบันทึกได้ และสำหรับแต่ละองค์ประกอบของ Gateway คุณจะพบสามตัวเลือก ได้แก่:

  1. บันทึกทั้งหมด
  2. บันทึกรายการที่ถูกปิดกั้นเท่านั้น
  3. ไม่ต้องบันทึก



นอกจากนี้ คุณจะพบตัวเลือกในการแก้ไข PII ทั้งหมดจากไฟล์บันทึกซึ่งเป็นค่าเริ่มต้น ซึ่งจะเป็นการแก้ไขข้อมูลใด ๆ ที่สามารถนำมาใช้เพื่อระบุผู้ใช้ที่อาจรวมถึงชื่อผู้ใช้ อีเมลผู้ใช้,ID ผู้ใช้, ID อุปกรณ์, IP ต้นทาง, URL, ผู้ส่งต่อ และเอเจนต์ผู้ใช้

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-840 Embedded Image - O7t3C0](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW475DN2QFSC1V9W4KPEDEJJ.png&w=715&h=278&f=webp&fit=cover&position=center)

เรายังรวมบทบาทใหม่ไว้ใน[แดชบอร์ด Cloudflare](https://dash.cloudflare.com/) ซึ่งให้รายละเอียดที่ดีขึ้นเมื่อแบ่งพาร์ติชันการเข้าถึงผู้ดูแลระบบไปยังส่วนประกอบของ Access หรือ Gateway บทบาทใหม่เหล่านี้จะมีผลใช้งานในเดือนมกราคม 2022 และสามารถแก้ไขได้จากบัญชีองค์กรโดยไปที่หน้าแรกของบัญชี → สมาชิก

หากคุณยังไม่พร้อมที่จะสร้างบัญชี แต่ต้องการสำรวจบริการ Zero Trust ของเรา [แนะนำให้ดูการสาธิตเชิงโต้ตอบ](https://www.cloudflare.com/teams/self-guided-tour-of-zero-trust-platform/) ที่คุณชมแพลตฟอร์มได้ด้วยตนเองพร้อมฟังคำแนะนำแบบบรรยายเกี่ยวกับกรณีการใช้งานที่สำคัญ ซึ่งรวมถึงการตั้งค่าการกรอง DNS และ HTTP ด้วย Cloudflare Gateway

### **แล้วยังไงต่อ**

จากที่เราดำเนินการมา เรารู้สึกตื่นเต้นที่ได้เพิ่มคุณสมบัติความเป็นส่วนตัวเข้ามามากขึ้นเรื่อยๆ ซึ่งจะช่วยให้คุณและทีมของคุณสามารถควบคุมสภาพแวดล้อมของคุณอย่างละเอียดยิ่งขึ้น คุณสมบัติที่ประกาศในวันนี้เหมาะสำหรับผู้ใช้ในทุกแผน ทีมของคุณสามารถติดตามลิงก์นี้เพื่อ[เริ่มต้นทันที](https://dash.cloudflare.com/sign-up/teams)

ในหน้านี้

สนทนาออนไลน์

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fpii-and-selective-logging-controls-for-cloudflares-zero-trust-platform%2F&t=%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%84%E0%B8%A7%E0%B8%9A%E0%B8%84%E0%B8%B8%E0%B8%A1%20PII%20%E0%B9%81%E0%B8%A5%E0%B8%B0%20Selective%20Logging%20%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B9%81%E0%B8%9E%E0%B8%A5%E0%B8%95%E0%B8%9F%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B8%A1%20Zero%20Trust%20%E0%B8%82%E0%B8%AD%E0%B8%87%20Cloudflare)[](https://x.com/intent/post?text=%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%84%E0%B8%A7%E0%B8%9A%E0%B8%84%E0%B8%B8%E0%B8%A1+PII+%E0%B9%81%E0%B8%A5%E0%B8%B0+Selective+Logging+%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B9%81%E0%B8%9E%E0%B8%A5%E0%B8%95%E0%B8%9F%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B8%A1+Zero+Trust+%E0%B8%82%E0%B8%AD%E0%B8%87+Cloudflare&url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fpii-and-selective-logging-controls-for-cloudflares-zero-trust-platform%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fpii-and-selective-logging-controls-for-cloudflares-zero-trust-platform%2F)[](https://bsky.app/intent/compose?text=%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%84%E0%B8%A7%E0%B8%9A%E0%B8%84%E0%B8%B8%E0%B8%A1+PII+%E0%B9%81%E0%B8%A5%E0%B8%B0+Selective+Logging+%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B9%81%E0%B8%9E%E0%B8%A5%E0%B8%95%E0%B8%9F%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B8%A1+Zero+Trust+%E0%B8%82%E0%B8%AD%E0%B8%87+Cloudflare+https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fpii-and-selective-logging-controls-for-cloudflares-zero-trust-platform%2F)[](https://mastodonshare.com/?text=%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%84%E0%B8%A7%E0%B8%9A%E0%B8%84%E0%B8%B8%E0%B8%A1+PII+%E0%B9%81%E0%B8%A5%E0%B8%B0+Selective+Logging+%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B9%81%E0%B8%9E%E0%B8%A5%E0%B8%95%E0%B8%9F%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B8%A1+Zero+Trust+%E0%B8%82%E0%B8%AD%E0%B8%87+Cloudflare&url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fpii-and-selective-logging-controls-for-cloudflares-zero-trust-platform%2F)[](https://www.threads.net/intent/post?text=%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%84%E0%B8%A7%E0%B8%9A%E0%B8%84%E0%B8%B8%E0%B8%A1+PII+%E0%B9%81%E0%B8%A5%E0%B8%B0+Selective+Logging+%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B9%81%E0%B8%9E%E0%B8%A5%E0%B8%95%E0%B8%9F%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B8%A1+Zero+Trust+%E0%B8%82%E0%B8%AD%E0%B8%87+Cloudflare+https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fpii-and-selective-logging-controls-for-cloudflares-zero-trust-platform%2F)

## แท็กที่เกี่ยวข้อง

[CIO Week](https://blog.cloudflare.com/th-th/tag/cio-week/)[Cloudflare Gateway](https://blog.cloudflare.com/th-th/tag/gateway/)[Cloudflare One](https://blog.cloudflare.com/th-th/tag/cloudflare-one/)[Firewall](https://blog.cloudflare.com/th-th/tag/firewall/)[Logs](https://blog.cloudflare.com/th-th/tag/logs/)[ความปลอดภัย](https://blog.cloudflare.com/th-th/tag/security/)

ติดตามบนโซเชียลมีเดีย

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## สมัครรับการแจ้งเตือนโพสต์ใหม่

อีเมล

เราจะไม่เปิดเผยอีเมลของคุณ

สมัคร

ขอบคุณที่สมัครรับข่าวสาร! โปรดตรวจสอบกล่องจดหมายเพื่อยืนยัน
