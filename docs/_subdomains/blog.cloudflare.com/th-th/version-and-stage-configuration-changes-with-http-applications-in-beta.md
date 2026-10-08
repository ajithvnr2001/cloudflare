---
url: https://blog.cloudflare.com/th-th/version-and-stage-configuration-changes-with-http-applications-in-beta/
title: \u0e40\u0e27\u0e2d\u0e23\u0e4c\u0e0a\u0e31\u0e19\u0e41\u0e25\u0e30\u0e01\u0e32\u0e23\u0e08\u0e31\u0e14\u0e01\u0e32\u0e23\u0e01\u0e32\u0e23\u0e01\u0e33\u0e2b\u0e19\u0e14\u0e04\u0e48\u0e32\u0e01\u0e32\u0e23\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19\u0e41\u0e1b\u0e25\u0e07\u0e14\u0e49\u0e27\u0e22\u0e41\u0e2d\u0e1b\u0e1e\u0e25\u0e34\u0e40\u0e04\u0e0a\u0e31\u0e19 HTTP \u0e40\u0e27\u0e2d\u0e23\u0e4c\u0e0a\u0e31\u0e19\u0e40\u0e1a\u0e15\u0e49\u0e32 | \u0e1a\u0e25\u0e47\u0e2d\u0e01 Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:47:20.106024+00:00
---

# เวอร์ชันและการจัดการการกำหนดค่าการเปลี่ยนแปลงด้วยแอปพลิเคชัน HTTP เวอร์ชันเบต้า | บล็อก Cloudflare

> Source: https://blog.cloudflare.com/th-th/version-and-stage-configuration-changes-with-http-applications-in-beta/

[บล็อก](https://blog.cloudflare.com/th-th/)

[CIO Week](https://blog.cloudflare.com/th-th/tag/cio-week/)

1 แท็กแสดง 1 แท็ก

  * แท็กของโพสต์
  *   * แท็กทั้งหมด
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



[CIO Week](https://blog.cloudflare.com/th-th/tag/cio-week/)

11 ธันวาคม 2564

# เวอร์ชันและการจัดการการกำหนดค่าการเปลี่ยนแปลงด้วยแอปพลิเคชัน HTTP เวอร์ชันเบต้า

![Garrett Galow](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48YN0EJVE0CEXVNHMJRJ6Q.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Garrett Galow](https://blog.cloudflare.com/th-th/author/garrett/)

อ่าน 2 นาที

คัดลอก URL

โพสต์นี้มีให้อ่านใน [English](https://blog.cloudflare.com/version-and-stage-configuration-changes-with-http-applications-in-beta/) [日本語](https://blog.cloudflare.com/ja-jp/version-and-stage-configuration-changes-with-http-applications-in-beta/) [简体中文](https://blog.cloudflare.com/zh-cn/version-and-stage-configuration-changes-with-http-applications-in-beta/) และ[Bahasa Indonesia](https://blog.cloudflare.com/id-id/version-and-stage-configuration-changes-with-http-applications-in-beta/).

![Version and Stage Configuration Changes with HTTP Applications in Beta](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46VR753WR50W3XEB355FSQ.png&w=1200&h=676&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/////f7/8vHz7evt8PDy9fb48vP16ens////////8/Dx7Ofo7+3t9fX28/T17Ovs////////9fHw7eXl8Ovq9vX19vb27+7u////////+fTz8Ojn8+3t+vj4+vr69PPy//////////v69+/v+fT0//7+////+fj4/////////////vn7//7//////////v3+////////////////////////////////////////////////////////////////)

วันนี้ เราประกาศแอปพลิเคชัน HTTP เวอร์ชันเบต้าแบบปิด ซึ่งเป็นวิธีในการทดสอบและใช้งานการเปลี่ยนแปลงได้อย่างปลอดภัยในการรับส่งข้อมูล HTTP ของคุณ แอปพลิเคชัน HTTP นำเสนอการเปลี่ยนแปลงการกำหนดค่าและความสามารถในการควบคุมว่าเมื่อใดจะเปิดใช้งานการเปลี่ยนแปลงนั้นกับการรับส่งข้อมูล HTTP บนเครือข่ายขอบนอกทั่วโลกของ Cloudflare ลูกค้าองค์กรที่กำลังมองหาการควบคุมที่ดีขึ้นควรติดต่อไปที่ผู้จัดการ Customer Success เพื่อรับการเข้าถึง

### **ปัญหาที่พบในการจัดการการกำหนดค่า**

ตั้งแต่ในช่วงแรกของ Cloudflare การจัดการเว็บไซต์และเว็บแอปพลิเคชันทำผ่านสิ่งที่เราเรียกว่า โซน ซึ่งมาจากแนวคิดของ [DNS Zone](https://www.cloudflare.com/learning/dns/glossary/dns-zone/) ในขณะที่โมเดลนี้ดูแลลูกค้ามาอย่างดีเป็นเวลาหลายปี แต่ก็สร้างความยากลำบากในการจัดการการกำหนดค่าขอบนอก กล่าวคือ

  1. ต้องใช้การดำเนินงานด้วยคนของลูกค้าในการติดตั้งสภาพแวดล้อมการเตรียมการ
  2. ความเสี่ยงที่การกำหนดค่าอาจเบี่ยงเบนระหว่างสภาพแวดล้อมการผลิตและสภาพแวดล้อมการเตรียมการ



ในการพัฒนาซอฟต์แวร์ คุณต้องทำการทดสอบความเปลี่ยนแปลงในสภาพแวดล้อมที่ปลอดภัยเพื่อตรวจสอบก่อนเข้าสู่ขั้นตอนการผลิตหรือส่งผลกระทบในการรับส่งข้อมูลในขณะนี้ ในวงจรการพัฒนาซอฟต์แวร์ทั่วไป หมายความว่าการนำการเปลี่ยนแปลงไปใช้งานในสภาพแวดล้อมการเตรียมการหรือสภาพแวดล้อมก่อนการผลิตสำหรับการทดสอบและการตรวจสอบ วิธีการส่วนใหญ่ที่ลูกค้าทำบน Cloudflare ทุกวันนี้ คือ การใช้สองโซน ที่แสดงโดยชื่อโฮสต์ของโซนนั้น ตัวอย่างเช่น อันแรกคือสภาพแวดล้อมการเตรียมการที่ชื่อว่า _staging.example.com_ และอีกอันคือสภาพแวดล้อมการผลิตที่ชื่อว่า _example.com_ วิธีนี้แก้ปัญหาหลักได้เพราะให้มีการป้องกันการเปลี่ยนแปลง ข้อผิดพลาดในโซนการเตรียมการจะไม่ส่งผลต่อการรับส่งข้อมูลการผลิต

อย่างไรก็ตาม เพื่อการนำไปใช้ในสภาพแวดล้อมการผลิต เมื่อการเปลี่ยนแปลงได้รับการตรวจสอบเรียบร้อยแล้วในสภาพแวดล้อมการเตรียมการ ลูกค้าต้องคัดลอกการเปลี่ยนแปลงนั้นด้วยตนเอง — หรือสร้างระบบอัตโนมัติฝ่านการใช้งาน [ผู้ให้บริการ Terraform](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs) ของ Cloudflare สำหรับหลายๆ คน นี่ยังรวมถึงขั้นตอน "การร้องขอการเปลี่ยนแปลง" ด้วยตนเองซึ่งมีตั๋วที่บันทึกข้อมูลที่ต้องทำการเปลี่ยนแปลงไว้ หลังจากนั้น อีกคนหนึ่ง (มักจะเป็นคนละคนกัน) ก็จะมาเอาตั๋วและต้องทำการเปลี่ยนแปลงซ้ำเดิมตามคำแนะนำที่ให้ไว้ ขั้นตอนนี้เป็นขั้นตอนที่อาจเกิดข้อผิดพลาดได้ และข้อผิดพลาดในขั้นตอนนี้อาจทำให้ไฟบริการหยุดชะงัก ทั้งนี้ขึ้นอยู่กับการเปลี่ยนแปลงที่เกี่ยวข้อง ยิ่งไปกว่านั้น ความเบี่ยงเบนระหว่างการกำหนดค่าสภาพแวดล้อมการเตรียมการและสภาพแวดล้อมการผลิตอาจสร้างความซับซ้อนมากยิ่งขึ้นได้

เราต้องการให้ความปลอดดภัยและความไว้วางใจแก่ลูกค้าในการจัดการบริการบน Cloudflare เพื่อเป็นการแก้ปัญหาที่กล่าวไปข้างต้น เราจึงประกาศแอปพลิเคชัน HTTP ควบคู่กับกฎการกำหนดเส้นทาง

### **แอปพลิเคชัน HTTP**

แอปพลิเคชัน HTTP เป็นวิธีการในการจัดการกับการกำหนดค่าบริเวณขอบนอกด้วยกรณีการใช้งาน แทนที่จะใช้ชื่อโฮสต์ แอปพลิเคชัน HTTP แต่ละตัวมีวัตถุประสงค์ของตัวเอง ไม่ว่าจะเป็นการจัดการกับการกำหนดค่าเว็บไซต์การตลาดของคุณหรือแอปพลิเคชันภายใน แอปพลิเคชัน HTTP แต่ละตัวประกอบด้วยเวอร์ชันการกำหนดค่าที่แสดงภาพการตั้งค่าสำหรับการจัดการการรับส่งข้อมูล — กฎของเพจ กฎไฟร์วอลล์ การตั้งค่าแคช และอื่นๆ เวอร์ชันการกำหนดค่าแต่ละเวอร์ชันภายในแอปพลิเคชัน HTTP ทำงานอย่างอิสระ แต่เมื่อมีการสร้างเวอร์ชันใหม่ขึ้นมา ก็จะตั้งค่าเริ่มต้นที่เป็นการคัดลอกแบบของเวอร์ชันก่อนหน้ามา

### **กฎการกำหนดเส้นทาง**

แอปพลิเคชัน HTTP แต่ละเวอร์ชันนั้นต่างกับโซน ตรงที่มันทำงานอย่างอิสระจากชื่อโฮสต์ที่เจาะจงใดๆ แล้วในเมื่อเวอร์ชันไม่ได้ผูกติดอยู่กับชื่อโฮสต์อย่างโซน แล้วคุณจะตัดสินใจอย่างไรว่าแอปพลิเคชัน HTTP เวอร์ชันใดจะส่งผลกับการรับส่งข้อมูลที่เฉพาะเจาะจง คำตอบก็คือ กฎการกำหนดเส้นทาง ด้วยการกำหนดเส้นทาง คุณจะสามารถตัดสินใจได้ว่าจะใช้แอปพลิเคชัน HTTP เวอร์ชันใดกับการรับส่งข้อมูลชนิดใด เช่น ชื่อโฮสต์ กฎการกำหนดเส้นทางทำงานโดย [Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/) ของ Cloudflare ซึ่งขึ้นอยู่กับเงื่อนไขการใช้งานของกฎ "ถ้า แล้ว" เพื่อจัดการชื่อโฮสต์ที่ควบคุมในบัญชี Cloudflare ของคุณเข้ากับเวอร์ชันของการกำหนดค่า ตัวอย่างเช่น ถ้าชื่อโฮสต์ของตรงกับ `[www.example.com`](http://www.example.com`) ดังนั้นให้ใช้เวอร์ชัน 2 ของแอปพลิเคชัน HTTP การตลาด เมื่อมีการใช้กฎนี้บริเวณขอบนอก แทนที่จะใช้การกำหนดค่าโซนปกติ [www.example.com](http://www.example.com/) ก็จะใช้การกำหนดค่าที่เฉพาะเจาะจงแทนในเวอร์ชัน 2 ของแอปพลิเคชัน HTTP

กฎการกำหนดเส้นทางนั้นรองรับกฎสองชนิด — กฎระยะเตรียมการ และกฎระยะการผลิต ทั้งสองจะใช้รายชื่อโฮสต์ ดังที่กล่าวไป แต่ในการสร้างกฎระยะเตรียมการ เราได้เพิ่มการคัดกรองว่ากฎนี้จะใช้ได้เฉพาะตอนที่การรับส่งข้อมูลถูกส่งไปที่ IP ที่เฉพาะเจาะจงบริเวณขอบนอกของเราเท่านั้น ซึ่งหมายความว่าคุณสามารถทดสอบการเปลี่ยนแปลงได้อย่างปลอดภัยโดยการรับส่งข้อมูลไปที่ [www.example.com](http://www.example.com/) ที่ IP ของสภาพแวดล้อมการเตรียมการโดยจะไม่ส่งผลกระทบต่อลูกค้า และที่ดียิ่งกว่านั้นก็คือ เมื่อคุณตรวจสอบการเปลี่ยนแปลงด้วยการสร้างกฎการกำหนดเส้นทางของสภาพแวดล้อมการผลิต การกำหนดค่าเดียวกันนั้นจะถูกนำไปใช้กับสภาพแวดล้อมการผลิตของลูกค้าทุกคน

เราพูดมามากแล้ว — มาดูการทำงานจริงเลยดีกว่า!

### **ใช้แอปพลิเคชัน HTTP เพื่อทดสอบและใช้งานการเปลี่ยนแปลงได้อย่างปลอดภัย**

สำหรับคำแนะนำครั้งนี้ ผมจะเล่นเป็นลูกค้าที่ใช้งานอยู่แล้ว ผมมีโซนไว้บริการลูกค้า และผมต้องการเปลี่ยนแปลงอะไรบางอย่าง เพื่อเปลี่ยนกฎให้ผมสามารถย้ายตำแหน่งข้อมูลของผมได้ แต่ผมไม่เก่งเรื่อง regex และถ้าเกิดข้อผิดพลาดอาจทำให้ไซต์ของลูกค้าผมพังหมดก็ได้! แทนที่จะทำการเปลี่ยนแปลงที่โซนโดยตรง เราจะใช้แอปพลเคชัน HTTP และกฎการกำหนดเส้นทางเพื่อสร้าง ทดสอบ และใช้งานการเปลี่ยนแปลง

อันดับแรก ผมเข้าสู่ระบบแดชบอร์ด Cloudflare หลังจากที่เลือกบัญชีของผมแล้ว ผมก็จะเห็นว่ามีแอปพลิเคชัน HTTP อยู่ที่แถบด้านข้าง การเลือกนี้เท่ากับว่าผมกำลังจะสร้างแอปพลิเคชัน HTTP ตัวแรกของผม

แดชบอร์ด Cloudflare แสดงหน้าสถานะว่างเปล่าสำหรับแอปพลิเคชัน HTTP

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![The Cloudflare Dashboard showing the empty state page for HTTP Applications](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW458EKZ2S3MRA5PVPCQ9GTS.png&w=715&h=508&f=webp&fit=cover&position=center)

เพื่อเป็นการสร้างแอปพลิเคชัน HTTP ตัวแรกของผม ผมต้องตั้งชื่อและเลือกโซนที่มีอยู่ก่อนแล้ว ในที่นี่คือ example.com Cloudflare จะใช้โซนนั้นในการกำหนดค่าเริ่มต้นของแอปพลิเคชัน HTTP เวอร์ชันแรก การคัดลอกการตั้งค่าเดิมมาจากโซนทำให้ผมมีสำเนาให้ทำงานได้อย่างปลอดภัย และผมไม่ต้องสร้างการกำหนดค่าใหม่ด้วยตัวเอง

หน้าจอ "สร้างแอปพลิเคชัน" แสดงให้เห็นว่าแอปพลิเคชัน HTTP จะสร้างขึ้นในชื่อ “แอปพลิเคชันตัวอย่าง” และกำหนดค่าเริ่มต้นจาก example.com

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![The “Create an Application” screen showing that an HTTP Application will be created named “Example Application” and initialized from example.com.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46SZ1YT1QX8DK9DE6SV6RM.png&w=715&h=597&f=webp&fit=cover&position=center)

หลังจากเลือกสร้าง ผมก็มีแอปพลิเคชัน HTTP ตัวแรกของผมแล้ว! ตอนนี้ เวอร์ชันแรกกำลังอยู่ในขั้นตอนการสร้าง ข้างหลังฉากนั้น Cloudflare จะนำการกำหนดค่าที่มีอยู่ของ example.com และคัดลอกมาไว้ที่เวอร์ชัน 1 ของแอปพลิเคชัน HTTP เมื่อคัดลอกสำเร็จ ผมก็สามารถแก้ไขการกำหนดค่าได้เลย

รายการเวอร์ชันของแอปพลิเคชันตัวอย่างแสดงให้เห็นว่าได้สร้างเวอร์ชัน 1 แล้ว

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![The Version list of the Example Application, showing Version 1 being created.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46S9XE345HJ7DW2D5D1SK9.png&w=715&h=509&f=webp&fit=cover&position=center)

ผมสามารถแก้ไขในเวอร์ชันนี้ได้เหมือนกับที่ผมทำในโซน แต่ก็ยังมีความแตกต่างกันสองประการ ประการแรกคือ การเปลี่ยนแปลงที่ผมทำในตอนนี้จะไม่ส่งผลต่อการรับส่งข้อมูลในขณะนี้ที่ขอบนอกของ Cloudflare เพราะเรายังไม่ได้สร้างกฎการกำหนดเส้นทางเพื่อที่จะส่งการรับส่งข้อมูลไปที่เวอร์ชันการกำหนดค่านี้ ประการที่สอง เราไม่อนุญาตให้ควบคุมสิ่งต่างๆ ที่เกี่ยวข้องกับโซนผ่านการใช้แอปพลิเคชัน HTTP กล่าวคือ บันทึก DNS ใบรับรอง SSL Spectrum หรือ Load Balancing

กฎการเปลี่ยนแปลงของเวอร์ชัน 1 แสดงให้เห็นว่ายังไม่มีการสร้างกฎ

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Transform rules of Version 1 showing a new rule named “Rewrite Assets” has been created.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4650766PWVQKE2S1CH0ZPT.png&w=715&h=508&f=webp&fit=cover&position=center)

ในส่วนของกฎด้านล่างภายใต้ [กฎการเปลี่ยนแปลง](https://blog.cloudflare.com/introducing-transform-rules-with-url-rewriting-at-the-edge/)ผมได้สร้างกฎใหม่เพื่อเขียนเส้นทางใหม่เพื่อให้ข้อมูลไปยังตำแหน่งที่ถูกต้อง การร้องขอใดๆ ที่ส่งไปที่ example.com/assets/* เราจะเขียนเส้นทางใหม่เพื่อให้ไปที่ example.com/internal/files/assets/*

การสร้างกฎการเปลี่ยนแปลงสำหรับเวอร์ชัน 1 ชื่อว่า "เขียนข้อมูลใหม่" ซึ่งกฎนี้จะไปแทนที่เส้นทางการร้องขอที่ขึ้นต้นด้วย “/assets/*” และ “internal/files/assets/*”

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Creating a transform rule for Version 1 named “Rewrite Assets”. This rule replaces the path for requests starting with “/assets/” with “internal/files/assets/”.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW456C7EFJVX26E4WG8HKEME.png&w=715&h=692&f=webp&fit=cover&position=center)

กฎการเปลี่ยนแปลงของเวอร์ชัน 1 แสดงให้เห็นว่ากฎใหม่ที่ชื่อ "เขียนข้อมูลใหม่" ได้ถูกสร้างขึ้นแล้ว

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Transform rules of Version 1 showing a new rule named “Rewrite Assets” has been created.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4650766PWVQKE2S1CH0ZPT.png&w=715&h=508&f=webp&fit=cover&position=center)

ณ จุดนี้ ผมได้ทำการเปลี่ยนแปลงแล้ว แต่ตอนนี้ผมต้องการทดสอบการเปลี่ยนแปลง เพื่อทำเช่นนั้น ผมสามารถทิ้งส่วนการแก้ไขเวอร์ชันและไปที่กฎการกำหนดเส้นทางสำหรับแอปพลิเคชัน HTTP ที่นี่ผมสามารถสร้างกฎที่จะอนุญาตให้การรับส่งข้อมูลที่มีอยู่ให้ใช้เส้นทางผ่านการกำหนดค่าของเวอร์ชันนี้

รายการว่างเปล่าของกฎการกำหนดเส้นทางสำหรับแอปพลิเคชันตัวอย่าง

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![An empty list of Routing Rules for the Example Application.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47YCJHBA4CE79D6EBGWXBB.png&w=715&h=509&f=webp&fit=cover&position=center)

ผมจะสร้างกฎระยะเตรียมการ เพราะผมต้องการเป็นคนเดียวที่จะทำการทดสอบการเปลี่ยนแปลงโดยไม่ให้ส่งผลกับลูกค้าคนใดๆ จำไว้ว่า เมื่อสร้างกฎระยะเตรียมการแล้ว IPs สำหรับใช้ในการทดสอบเวอร์ชันนี้จะปรากฏขึ้นในหน้าจอการสร้างกฎ

การสร้างกฎการกำหนดเส้นทางของสภาพแวดล้อมการเตรียมการที่จะตรงกับการร้องขอที่ตรงกับ example.com และ IP ขอบนอก คือ 192.168.1.1 หรือ 192.168.2.2 และใช้การกำหนดค่าของเวอร์ชัน 1

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Creating a staging Routing Rule that will match when requests match example.com and the edge IP is 192.168.1.1 or 192.168.2.2 and apply the configuration of Version 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48EYHVEC962GBGCXS4G320.png&w=715&h=555&f=webp&fit=cover&position=center)

หลังจากสร้างกฎแล้ว ผมสามารถกำหนดค่าคอมพิวเตอร์ของผมได้เพื่อส่งการร้องขอไปที่ IPs example.com Rackspace มี [คำแนะนำที่ครอบคลุม](https://docs.rackspace.com/support/how-to/modify-your-hosts-file/) สำหรับวิธีที่จะเปลี่ยนไฟล์โฮสต์ของเครื่องคุณ ตอนนี้ เมื่อผมไปที่ example.com กฎการเปลี่ยนแปลงใหม่จะถูกใช้งานอยู่ แต่สำหรับคนอื่นๆ ที่เข้าใช้ไซต์จะไม่มีอะไรเปลี่ยน

กฎการกำหนดเส้นทางสำหรับแอปพลิเคชันตัวอย่างแสดงให้เห็นว่าได้มีการสร้างกฎระยะเตรียมการขึ้น 1 กฎ

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Routing Rules for the Example Application showing one rule for staging has been created.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW483QYWQGJSYASW3SB1J6MZ.png&w=715&h=508&f=webp&fit=cover&position=center)

เมื่อผมมั่นใจแล้วว่าการเปลี่ยนแปลงทำงานได้ดี ผมสามารถสร้างการผลิตกฎการกำหนดเส้นทางที่จะนำการเปลี่ยนแปลงนี้ไปใช้กับการรับส่งข้อมูลทุกอย่างบน example.com — และผมก็ดำเนินการเสร็จแล้ว!

หน้าจอการสร้างกฎการกำหนดเส้นทางแสดงให้เห็นการสร้างกฎการผลิตที่จะใช้เวอร์ชัน 1 เมื่อมีการร้องขอตรงกับ example.com

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Routing Rule creation screen showing the creation of a production rule that will apply Version 1 when requests match example.com](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW483PNM5H34VA0H6R114BEG.png&w=715&h=555&f=webp&fit=cover&position=center)

เมื่ออัปเดตแล้ว เส้นทางข้อมูลสำหรับไซต์ของผมก็จะถูกเขียนใหม่สำหรับทุกการร้องขอให้ไปที่ _example.com_

กฎการกำหนดเส้นทางสำหรับแอปพลิเคชันตัวอย่างแสดงทั้งกฎระยะเตรียมการและกฎระยะการผลิตสำหรับเวอร์ชัน 1

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Routing Rules for the Example Application showing both a staging and production rule for Version 1.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4516H63F0TYZDA9GN20TKW.png&w=715&h=508&f=webp&fit=cover&position=center)

จะเกิดอะไรขึ้นหลังจากนั้น? เมื่อผมพร้อมที่จะสร้างการเปลี่ยนแปลงอีกครั้ง ผมสามารถไปที่แอปพลิเคชัน HTTP แล้วโคลนเวอร์ชัน 1 เพื่อสร้างเวอร์ชัน 2 ในช่วงแรกเวอร์ชัน 2 จะมีการกำหนดค่าเหมือนกับของเวอร์ชัน 1 ทุกประการ แต่เนื่องจากทั้งสองเวอร์ชันมีกฎการกำหนดเส้นทางต่างกัน จึงจะยังไม่มีการนำไปใช้กับการรับส่งข้อมูลใดๆ

รายการเวอร์ชันสำหรับแอปพลิเคชันตัวอย่างแสดงให้เห็นว่าเวอร์ชัน 1 ถูกใช้งานในการเตรียมการและการผลิต และเวอร์ชัน 2 พร้อมสำหรับการแก้ไข แต่ยังไม่มีการใช้ที่ใด

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![The list of versions for the Example Application showing Version 1 being applied to staging and production, and Version 2 ready to edit, but not being used anywhere.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44FBHN5DK9W8Q5HNG6A450.png&w=715&h=509&f=webp&fit=cover&position=center)

แล้วผมก็สามารถแก้ไขเวอร์ชัน 2 ได้อย่างปลอดภัย เหมือนกับที่ทำกับเวอร์ชัน 1 ไปก่อนหน้านี้ ครั้งนี้ผมต้องการเปลี่ยนแปลงกฎไฟร์วอลล์ เพื่อให้สามารถป้องกันการรับส่งข้อมูลอันตรายที่อาจเกิดขึ้นจากการเข้าถึงเว็บไซต์ของผมได้ การเปลี่ยนแปลงในเวอร์ชัน 2 จะไม่เปลี่ยนแปลงการรับส่งข้อมูลในบริเวณขอบนอกจนกว่าผมจะอัปเดตกฎการกำหนดเส้นทางของสภาพแวดล้อมการเตรียมการ เพื่อใช้กับเวอร์ชัน 2 ซึ่งทำให้ผมสามารถเปลี่ยนแปลงได้อย่างมั่นใจ และสามารถทดสอบได้อย่างปลอดภัยอีกด้วย

รายการกฎการกำหนดเส้นทางสำหรับแอปพลิเคชันตัวอย่างแสดงให้เห็นว่าเวอร์ชัน 2 ถูกใช้สำหรับการเตรียมการ ในขณะที่เวอร์ชัน 1 ยังคงใช้สำหรับการผลิต

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![The list of routing rules for the Example Application showing Version 2 being used for staging, while Version 1 is still used in production.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46KH032ZQ7EY8QQ0WJZR34.png&w=715&h=508&f=webp&fit=cover&position=center)

หลังจากตรวจสอบการเปลี่ยนแปลงครั้งใหม่นี้แล้ว ผมสามารถส่งเวอร์ชัน 2 ไปที่การรับส่งข้อมูลทั้งหมดได้โดยการอัปเดตการผลิตกฎการกำหนดเส้นทางเพื่อใช้เวอร์ชัน 2 ผมสามารถใช้กระบวนการเดียวกันได้กับการเปลี่ยนแปลงที่จะตามมา

### **แอปพลิเคชัน HTTP มีให้ใช้งานแล้วตอนนี้ในเวอร์ชันเบต้าแบบปิด**

ด้วยพลังแห่งแอปพลิเคชัน HTTP และกฎการกำหนดเส้นทาง ลูกค้าสามารถควบคุมได้ดีขึ้นว่าการเปลี่ยนแปลงการกำหนดค่าจะเกิดขึ้นอย่างไรและเมื่อไหร่ วิธีการนี้จะลดความกังวลในการเปลี่ยนแปลงที่ไม่ดีที่อาจเกิดกับไซต์ของคุณได้ ความสามารถนี้มีให้ใช้งานแล้วในเวอร์ชันเบต้าแบบปิดสำหรับผู้ใช้องค์กร แต่หากคุณสนใจ กรุณาติดต่อทีมบัญชี Cloudflare ของคุณเพื่อศึกษาข้อมูลเกี่ยวกับสิทธิ์การเข้าถึง

ในหน้านี้

สนทนาออนไลน์

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fversion-and-stage-configuration-changes-with-http-applications-in-beta%2F&t=%E0%B9%80%E0%B8%A7%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B8%8A%E0%B8%B1%E0%B8%99%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%88%E0%B8%B1%E0%B8%94%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%81%E0%B8%B3%E0%B8%AB%E0%B8%99%E0%B8%94%E0%B8%84%E0%B9%88%E0%B8%B2%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%80%E0%B8%9B%E0%B8%A5%E0%B8%B5%E0%B9%88%E0%B8%A2%E0%B8%99%E0%B9%81%E0%B8%9B%E0%B8%A5%E0%B8%87%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2%E0%B9%81%E0%B8%AD%E0%B8%9B%E0%B8%9E%E0%B8%A5%E0%B8%B4%E0%B9%80%E0%B8%84%E0%B8%8A%E0%B8%B1%E0%B8%99%20HTTP%20%E0%B9%80%E0%B8%A7%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B8%8A%E0%B8%B1%E0%B8%99%E0%B9%80%E0%B8%9A%E0%B8%95%E0%B9%89%E0%B8%B2)[](https://x.com/intent/post?text=%E0%B9%80%E0%B8%A7%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B8%8A%E0%B8%B1%E0%B8%99%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%88%E0%B8%B1%E0%B8%94%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%81%E0%B8%B3%E0%B8%AB%E0%B8%99%E0%B8%94%E0%B8%84%E0%B9%88%E0%B8%B2%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%80%E0%B8%9B%E0%B8%A5%E0%B8%B5%E0%B9%88%E0%B8%A2%E0%B8%99%E0%B9%81%E0%B8%9B%E0%B8%A5%E0%B8%87%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2%E0%B9%81%E0%B8%AD%E0%B8%9B%E0%B8%9E%E0%B8%A5%E0%B8%B4%E0%B9%80%E0%B8%84%E0%B8%8A%E0%B8%B1%E0%B8%99+HTTP+%E0%B9%80%E0%B8%A7%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B8%8A%E0%B8%B1%E0%B8%99%E0%B9%80%E0%B8%9A%E0%B8%95%E0%B9%89%E0%B8%B2&url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fversion-and-stage-configuration-changes-with-http-applications-in-beta%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fversion-and-stage-configuration-changes-with-http-applications-in-beta%2F)[](https://bsky.app/intent/compose?text=%E0%B9%80%E0%B8%A7%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B8%8A%E0%B8%B1%E0%B8%99%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%88%E0%B8%B1%E0%B8%94%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%81%E0%B8%B3%E0%B8%AB%E0%B8%99%E0%B8%94%E0%B8%84%E0%B9%88%E0%B8%B2%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%80%E0%B8%9B%E0%B8%A5%E0%B8%B5%E0%B9%88%E0%B8%A2%E0%B8%99%E0%B9%81%E0%B8%9B%E0%B8%A5%E0%B8%87%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2%E0%B9%81%E0%B8%AD%E0%B8%9B%E0%B8%9E%E0%B8%A5%E0%B8%B4%E0%B9%80%E0%B8%84%E0%B8%8A%E0%B8%B1%E0%B8%99+HTTP+%E0%B9%80%E0%B8%A7%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B8%8A%E0%B8%B1%E0%B8%99%E0%B9%80%E0%B8%9A%E0%B8%95%E0%B9%89%E0%B8%B2+https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fversion-and-stage-configuration-changes-with-http-applications-in-beta%2F)[](https://mastodonshare.com/?text=%E0%B9%80%E0%B8%A7%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B8%8A%E0%B8%B1%E0%B8%99%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%88%E0%B8%B1%E0%B8%94%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%81%E0%B8%B3%E0%B8%AB%E0%B8%99%E0%B8%94%E0%B8%84%E0%B9%88%E0%B8%B2%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%80%E0%B8%9B%E0%B8%A5%E0%B8%B5%E0%B9%88%E0%B8%A2%E0%B8%99%E0%B9%81%E0%B8%9B%E0%B8%A5%E0%B8%87%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2%E0%B9%81%E0%B8%AD%E0%B8%9B%E0%B8%9E%E0%B8%A5%E0%B8%B4%E0%B9%80%E0%B8%84%E0%B8%8A%E0%B8%B1%E0%B8%99+HTTP+%E0%B9%80%E0%B8%A7%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B8%8A%E0%B8%B1%E0%B8%99%E0%B9%80%E0%B8%9A%E0%B8%95%E0%B9%89%E0%B8%B2&url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fversion-and-stage-configuration-changes-with-http-applications-in-beta%2F)[](https://www.threads.net/intent/post?text=%E0%B9%80%E0%B8%A7%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B8%8A%E0%B8%B1%E0%B8%99%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%88%E0%B8%B1%E0%B8%94%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%81%E0%B8%B3%E0%B8%AB%E0%B8%99%E0%B8%94%E0%B8%84%E0%B9%88%E0%B8%B2%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%80%E0%B8%9B%E0%B8%A5%E0%B8%B5%E0%B9%88%E0%B8%A2%E0%B8%99%E0%B9%81%E0%B8%9B%E0%B8%A5%E0%B8%87%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2%E0%B9%81%E0%B8%AD%E0%B8%9B%E0%B8%9E%E0%B8%A5%E0%B8%B4%E0%B9%80%E0%B8%84%E0%B8%8A%E0%B8%B1%E0%B8%99+HTTP+%E0%B9%80%E0%B8%A7%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B8%8A%E0%B8%B1%E0%B8%99%E0%B9%80%E0%B8%9A%E0%B8%95%E0%B9%89%E0%B8%B2+https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fversion-and-stage-configuration-changes-with-http-applications-in-beta%2F)

## แท็กที่เกี่ยวข้อง

[CIO Week](https://blog.cloudflare.com/th-th/tag/cio-week/)

ติดตามบนโซเชียลมีเดีย

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## สมัครรับการแจ้งเตือนโพสต์ใหม่

อีเมล

เราจะไม่เปิดเผยอีเมลของคุณ

สมัคร

ขอบคุณที่สมัครรับข่าวสาร! โปรดตรวจสอบกล่องจดหมายเพื่อยืนยัน
