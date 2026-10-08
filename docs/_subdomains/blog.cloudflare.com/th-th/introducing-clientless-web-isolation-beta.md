---
url: https://blog.cloudflare.com/th-th/introducing-clientless-web-isolation-beta/
title: \u0e02\u0e2d\u0e41\u0e19\u0e30\u0e19\u0e33 Clientless Web Isolation | \u0e1a\u0e25\u0e47\u0e2d\u0e01 Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:46:12.333524+00:00
---

# ขอแนะนำ Clientless Web Isolation | บล็อก Cloudflare

> Source: https://blog.cloudflare.com/th-th/introducing-clientless-web-isolation-beta/

[บล็อก](https://blog.cloudflare.com/th-th/)

[CIO Week](https://blog.cloudflare.com/th-th/tag/cio-week/)[Clientless Web Isolation](https://blog.cloudflare.com/th-th/tag/clientless-web-isolation/)[Cloudflare Access](https://blog.cloudflare.com/th-th/tag/cloudflare-access/)+2แสดงแท็กเพิ่มเติม 2 รายการ

5 แท็กแสดง 5 แท็ก

  * แท็กของโพสต์
  * [Cloudflare Access](https://blog.cloudflare.com/th-th/tag/cloudflare-access/)
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



[Remote Browser Isolation](https://blog.cloudflare.com/th-th/tag/remote-browser-isolation/)[SASE](https://blog.cloudflare.com/th-th/tag/sase/)

[CIO Week](https://blog.cloudflare.com/th-th/tag/cio-week/)[Clientless Web Isolation](https://blog.cloudflare.com/th-th/tag/clientless-web-isolation/)[Cloudflare Access](https://blog.cloudflare.com/th-th/tag/cloudflare-access/)[Remote Browser Isolation](https://blog.cloudflare.com/th-th/tag/remote-browser-isolation/)[SASE](https://blog.cloudflare.com/th-th/tag/sase/)

8 ธันวาคม 2564

# ขอแนะนำ Clientless Web Isolation

![Tim Obezuk](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW493E1Z2ETFY5MBFNHC8RJD.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Tim Obezuk](https://blog.cloudflare.com/th-th/author/tim-obezuk/)

อ่าน 2 นาที

คัดลอก URL

โพสต์นี้มีให้อ่านใน [English](https://blog.cloudflare.com/introducing-clientless-web-isolation-beta/) [日本語](https://blog.cloudflare.com/ja-jp/introducing-clientless-web-isolation-beta/) [简体中文](https://blog.cloudflare.com/zh-cn/introducing-clientless-web-isolation-beta/) และ[Bahasa Indonesia](https://blog.cloudflare.com/id-id/introducing-clientless-web-isolation-beta/).

![Introducing Clientless Web Isolation](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44XQ0N47Y3DJ17M77142MA.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA+vnj9fPg6+jb5+Pa7Oje8u7g7+va5ePP/fvk+PTh7efa6ODY7eTc8+re8era6OPQ//3n/Pbj8Ofb697X8OHa9ene9Ora7OXS///s//rn9eve7+HZ9OTc+uzg+O7e8OnW///w///s+vHj9enf+ezj//Pn/fTj9e/b///1///x//rq+/Tn//jr//3u//zq+fXg///4///1///v//zu///y///1///v/Prl///5///2///x///w///1///3///x/fzm)

วันนี้ เรารู้สึกตื่นเต้นกับการประกาศเปิดตัว Clientless Web Isolation เวอร์ชันเบต้าของ Cloudflare การเชื่อมต่อแบบใหม่สำหรับ Browser Isolation ที่มาพร้อมกับ Zero Trust Network Access (ZTNA) ที่มีประโยชน์ในการป้องกันการโจมตีแบบ Zero-day ฟิชชิ่ง และการรั่วไหลของข้อมูลจากการเรียกดูระยะไกลสำหรับผู้ใช้ในทุกอุปกรณ์และการเรียกดูเว็บไซต์ทั้งหมด ไม่ว่าจะเป็นแอปภายในหรือแอปพลิเคชัน SaaS เข้าถึงประโยชน์ทั้งหมดโดยไม่ต้องติดตั้งซอฟต์แวร์หรือกำหนดค่าใบรับรองใดๆ บนอุปกรณ์ปลายทาง

### **การเข้าถึงที่ปลอดภัยสำหรับอุปกรณ์ที่ได้รับการจัดการและไม่ได้รับการจัดการ**

ในช่วงต้นปี 2021 Cloudflare ได้ประกาศการใช้งานทั่วไปของ Browser Isolation ซึ่งเป็นเบราว์เซอร์ระยะไกลที่รวดเร็วและปลอดภัยที่มาพร้อมกับแพลตฟอร์ม Zero Trust ของ Cloudflare แพลตฟอร์มนี้ — หรือที่เรียกว่า [Cloudflare for Teams](https://www.cloudflare.com/th-th/teams/) — เป็นแพลตฟอร์มที่รวมการเข้าถึงอินเทอร์เน็ตที่ปลอดภัยเข้ากับโซลูชันเว็บเกตเวย์ที่ปลอดภัยของเรา ([เกตเวย์](https://www.cloudflare.com/th-th/teams/gateway/)) และการเข้าถึงแอปพลิเคชันที่ปลอดภัยด้วยโซลูชัน ZTNA ([การเข้าถึง](https://www.cloudflare.com/th-th/teams/access/))

โดยทั่วไปแล้ว ผู้ดูแลระบบจะใช้งาน Browser Isolation ด้วยการเปิดใช้ไคลเอ็นต์อุปกรณ์ของ Cloudflare บนอุปกรณ์ปลายทาง เพื่อให้ Cloudflare สามารถให้บริการเป็น DNS ที่ปลอดภัยและพร็อกซีอินเทอร์เน็ต HTTPS ได้ โมเดลนี้ช่วยป้องกันผู้ใช้และแอปพลิเคชันที่ละเอียดอ่อนเมื่อผู้ดูแลระบบจัดการอุปกรณ์ต่างๆ ของทีม และผู้ใช้ปลายทางจะได้สัมผัสกับประสบการณ์ที่ลื่นไหลเหมือนกำลังใช้งานเบราว์เซอร์บนอุปกรณ์ ผู้ใช้แทบจะไม่รู้สึกเลยว่าจริงๆ แล้วกำลังท่องเว็บอยู่บนอุปกรณ์ที่ปลอดภัยซึ่งทำงานอยู่ในศูนย์ข้อมูล Cloudflare บริเวณใกล้เคียง

การผสานรวมแบบครบวงจรของ Browser Isolation เข้ากับการเข้าถึงอินเทอร์เน็ตที่ปลอดภัยทำให้เป็นเรื่องง่ายสำหรับผู้ดูแลระบบที่จะใช้งาน Browser Isolation ภายในทีม โดยที่ผู้ใช้ไม่รู้สึกเลยว่ากำลังจริงๆ แล้วกำลังท่องเว็บอยู่บนอุปกรณ์ที่ปลอดภัยซึ่งอยู่ในศูนย์ข้อมูล Cloudflare บริเวณใกล้เคียง อย่างไรก็ตาม การจัดการไคลเอนต์ปลายทางอาจเพิ่มค่าใช้จ่ายในการกำหนดค่าสำหรับผู้ใช้อุปกรณ์ที่ไม่ได้รับการจัดการ หรือผู้รับเหมาบนอุปกรณ์ที่ได้รับการจัดการโดยองค์กรบุคคลที่สามได้

Clientless Web Isolation ของ Cloudflare จะช่วยเพิ่มประสิทธิภาพการเชื่อมต่อกับเบราว์เซอร์ระยะไกลผ่านไฮเปอร์ลิงก์ (เช่น _https://.cloudflareaccess.com/browser_) เมื่อผู้ใช้ได้ยืนยันตัวตนผ่าน Cloudflare Access ที่รองรับ [ผู้ให้บริการพิสูจน์และยืนยันตัวตน](https://developers.cloudflare.com/cloudflare-one/identity)เบราว์เซอร์ของผู้ใช้จะใช้ HTML5 ในการสร้างการเชื่อมต่อที่มีเวลาแฝงต่ำกับเบราว์เซอร์ระยะไกลที่โฮสต์ในศูนย์ข้อมูล Cloudflare บริเวณใกล้เคียง โดยไม่ต้องติดตั้งซอฟแวร์ใดๆ ไม่มีเซิร์ฟเวอร์ที่ต้องจัดการหรือปรับขนาด หรือภูมิภาคที่ต้องกำหนดค่า

### **เรียกดูลิงก์ที่มีความเสี่ยงสูงได้อย่างปลอดภัย**

เพียงการคลิกลิงก์ในอีเมลหรือเว็บไซต์ก็ทำให้เบราว์เซอร์ของคุณดาวน์โหลดและเรียกใช้เพย์โหลดของเนื้อหาเว็บที่ใช้งานอยู่ได้ ซึ่งสามารถทำให้เกิดภัยคุกคามแบบ Zero-day ที่ไม่รู้จักและสร้างช่องโหว่ให้กับอุปกรณ์ปลายทางได้

สามารถเริ่มใช้งาน Clientless Web Isolation ของ Cloudflare ได้ผ่าน URL ที่มีคำนำหน้า (เช่น _https://.cloudflareaccess.com/browser/<https://www.example.com>_) เพียงแค่กำหนดค่าบล็อกเพจที่กำหนดเอง เกตเวย์อีเมล หรือเครื่องมือทิกเก็ตของคุณเพื่อใส่คํานําหน้าลิงก์ที่มีความเสี่ยงสูงด้วย Browser Isolation ก็จะเป็นการส่งการคลิกที่มีความเสี่ยงสูงไปยังเบราว์เซอร์ระยะไกลโดยอัตโนมัติ ซึ่งเป็นการป้องกันอุปกรณ์ปลายทางจากรหัสที่เป็นอันตรายที่อาจปรากฏในลิงก์เป้าหมาย

ที่ Cloudflare เราใช้ผลิตภัณฑ์ Cloudflare ในการปกป้อง Cloudflare และยังใช้วิธีการ Clientless Web Isolation นี้สำหรับกิจกรรมการตรวจสอบความปลอดภัยของเราเอง การใส่คำนำหน้าลิงก์ที่มีความเสี่ยงสูงด้วยโดเมนการตรวจสอบสิทธิ์ของเราจะทำให้ทีมความปลอดภัยของเราสามารถตรวจสอบเว็บไซต์ที่อาจเป็นอันตรายและและไซต์ฟิชชิ่งได้อย่างปลอดภัย

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Screenshot of clientless web isolation homepage](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW480JPESVVFSNMDRRGHARG2.png&w=715&h=492&f=webp&fit=cover&position=center)

ยังไม่เคยมีรหัสที่มีความเสี่ยงเข้าถึงอุปกรณ์ของพนักงานได้ และเมื่อสิ้นสุดการตรวจสอบ ระบบจะยุติการใช้งานเบราว์เซอร์ระยะไกลและรีเซ็ตเป็นสภาพที่รับรู้ว่าปลอดภัยสำหรับการตรวจสอบครั้งถัดไป

### **การเข้าถึงแบบ Zero Trust ที่เชื่อมโยงกันทั้งระบบและการเรียกดูระยะไกล**

ณ เวลาที่ข้อมูลของบริษัทมีการเข้าถึงจากเฉพาะอุปกรณ์ที่ได้รับการจัดการ ก็มีการผ่านเครื่องข่ายที่ควบคุมภายในไปเป็นเวลานานแล้ว องค์กรต่างๆ อาศัยการควบคุมสภาพของอุปกรณ์ที่เข้มงวดเพื่อตรวจสอบว่าการเข้าถึงแอปพลิเคชันที่เกิดจากเฉพาะอุปกรณ์ที่ได้รับการจัดการนั้นมีเครื่องมือบางอย่างในการสนับสนุนกลุ่มพนักงาน BYOD หรือผู้รับเหมา ก่อนหน้านี้ ผู้ดูแลระบบได้แก้ไขปัญหาด้วยการใช้งานสภาพแวดล้อมโครงสร้างพื้นฐานเดสก์ท็อปเสมือน (VDI) ที่ใช้ทรัพยากรและค่าใช้จ่ายสูงมาก

นอกจากนี้ เมื่อเป็นการรักษาความปลอดภัยการเข้าถึงแอปพลิเคชัน Cloudflare Access เป็นผู้เชี่ยวชาญในการใช้นโยบายการให้สิทธิ์ตามความจำเป็นที่กำหนดค่าเริ่มต้นเป็นปฏิเสธกับแอปพลิเคชันบนเว็บ โดยไม่ต้องติดตั้งซอฟต์แวร์ไคลเอ็นต์ใดๆ บนอุปกรณ์ผู้ใช้

Clientless Web Isolation ของ Cloudflare จะแบ่งกลุ่มกรณีการใช้งาน ZTNA เพื่อให้แอปพลิเคชันได้รับการป้องกันโดยใช้ [Access และ Gateway](https://developers.cloudflare.com/cloudflare-one/tutorials/require-swg#build-a-gateway-rule-in-access) เพื่อใช้ประโยชน์จาก[การควบคุมการคุ้มครองข้อมูล](https://docs.google.com/document/d/1YzcoC5WVxCYtVSriZW0ETeTzX9HEVxjKXdAEGeND3l8/edit)ของ Browser Isolation เช่น การควบคุมการพิมพ์บนอุปกรณ์ ข้อจำกัดการอัปโหลด / ดาวน์โหลดคลิปบอร์ดและไฟล์เพื่อป้องกันการถ่ายโอนข้อมูลที่ละเอียดอ่อนไปยังอุปกรณ์ที่ไม่ได้รับการจัดการ

สามารถเพิ่มลิงก์แบบแยกได้ที่[ตัวเปิดใช้แอป](https://developers.cloudflare.com/cloudflare-one/applications/app-launcher) Access ให้เป็น[บุ๊กมาร์ก](https://developers.cloudflare.com/cloudflare-one/applications/bookmarks)ได้อย่างง่ายดาย ทำให้ทีมของคุณและผู้รับเหมาเข้าถึงไซต์ต่างๆ ได้อย่างง่ายดายเพียงคลิกเดียว

และสุดท้าย เพียงเพราะเบราว์เซอร์ระยะไกลช่วยลดผลกระทบของช่องโหว่ ไม่ได้หมายความว่าควรมีการเข้าถึงอินเทอร์เน็ตที่ไม่ได้รับการจัดการ การรับส่งข้อมูลทั้งหมดจากเบราว์เซอร์ระยะไกลไปยังเว็บไซต์เป้าหมายนั้นปลอดภัย ได้รับการตรวจสอบ และได้รับการบันทึกโดยโซลูชัน SWG (Gateway) ของ Cloudflare เพื่อให้แน่ใจว่าภัยคุกคามที่ทราบได้รับการคัดกรองด้วยนโยบาย HTTP และ [การสแกนการป้องกันไวรัส](https://developers.cloudflare.com/cloudflare-one/policies/filtering/http-policies/antivirus-scanning)

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Screenshot of Access App Launcher bookmark linking to Browser Isolation](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45SJCQ79YVDD25DC0CZX00.png&w=715&h=482&f=webp&fit=cover&position=center)

### **ร่วมใช้งาน Clientless Web Isolation เวอร์ชันเบต้า**

Clientless Web Isolation จะพร้อมใช้งานสำหรับผู้สมัครใช้บริการ Cloudflare for Teams ที่ได้เพิ่ม Browser Isolation ไปยังแผน เราจะเปิดให้มีการเข้าถึง Clientless Web Isolation ของ Cloudflare เวอร์ชันเบต้าในเร็วๆ นี้ หากคุณสนใจเข้าร่วม [สมัครใช้งานที่นี่](https://www.cloudflare.com/zero-trust/lp/clientless-web-isolation-beta/) เพื่อรับข่าวสารจากเราเป็นคนแรก

เรารู้สึกตื่นเต้นเกี่ยวกับกรณีการใช้งานของการเรียดูที่ปลอดภัยและการเข้าถึงแอปพลิเคชันสำหรับโมเดล Clientless Web Isolation ของเรา ขณะนี้ ทีมทุกขนาดสามารถส่งการเชื่อมต่อ Zero Trust ที่ราบรื่นไปยังอุปกรณ์ที่ไม่ได้รับการจัดการได้ทุกที่บนโลก

ในหน้านี้

สนทนาออนไลน์

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fintroducing-clientless-web-isolation-beta%2F&t=%E0%B8%82%E0%B8%AD%E0%B9%81%E0%B8%99%E0%B8%B0%E0%B8%99%E0%B8%B3%20Clientless%20Web%20Isolation)[](https://x.com/intent/post?text=%E0%B8%82%E0%B8%AD%E0%B9%81%E0%B8%99%E0%B8%B0%E0%B8%99%E0%B8%B3+Clientless+Web+Isolation&url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fintroducing-clientless-web-isolation-beta%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fintroducing-clientless-web-isolation-beta%2F)[](https://bsky.app/intent/compose?text=%E0%B8%82%E0%B8%AD%E0%B9%81%E0%B8%99%E0%B8%B0%E0%B8%99%E0%B8%B3+Clientless+Web+Isolation+https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fintroducing-clientless-web-isolation-beta%2F)[](https://mastodonshare.com/?text=%E0%B8%82%E0%B8%AD%E0%B9%81%E0%B8%99%E0%B8%B0%E0%B8%99%E0%B8%B3+Clientless+Web+Isolation&url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fintroducing-clientless-web-isolation-beta%2F)[](https://www.threads.net/intent/post?text=%E0%B8%82%E0%B8%AD%E0%B9%81%E0%B8%99%E0%B8%B0%E0%B8%99%E0%B8%B3+Clientless+Web+Isolation+https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fintroducing-clientless-web-isolation-beta%2F)

## แท็กที่เกี่ยวข้อง

[CIO Week](https://blog.cloudflare.com/th-th/tag/cio-week/)[Clientless Web Isolation](https://blog.cloudflare.com/th-th/tag/clientless-web-isolation/)[Cloudflare Access](https://blog.cloudflare.com/th-th/tag/cloudflare-access/)[Remote Browser Isolation](https://blog.cloudflare.com/th-th/tag/remote-browser-isolation/)[SASE](https://blog.cloudflare.com/th-th/tag/sase/)

ติดตามบนโซเชียลมีเดีย

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## สมัครรับการแจ้งเตือนโพสต์ใหม่

อีเมล

เราจะไม่เปิดเผยอีเมลของคุณ

สมัคร

ขอบคุณที่สมัครรับข่าวสาร! โปรดตรวจสอบกล่องจดหมายเพื่อยืนยัน
