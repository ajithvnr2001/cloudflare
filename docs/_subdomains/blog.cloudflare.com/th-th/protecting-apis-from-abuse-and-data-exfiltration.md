---
url: https://blog.cloudflare.com/th-th/protecting-apis-from-abuse-and-data-exfiltration/
title: \u0e1b\u0e01\u0e1b\u0e49\u0e2d\u0e07 API \u0e02\u0e2d\u0e07\u0e04\u0e38\u0e13\u0e08\u0e32\u0e01\u0e01\u0e32\u0e23\u0e25\u0e30\u0e40\u0e21\u0e34\u0e14\u0e41\u0e25\u0e30\u0e01\u0e32\u0e23\u0e02\u0e42\u0e21\u0e22\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25 | \u0e1a\u0e25\u0e47\u0e2d\u0e01 Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:47:36.969394+00:00
---

# ปกป้อง API ของคุณจากการละเมิดและการขโมยข้อมูล | บล็อก Cloudflare

> Source: https://blog.cloudflare.com/th-th/protecting-apis-from-abuse-and-data-exfiltration/

[บล็อก](https://blog.cloudflare.com/th-th/)

[API Shield](https://blog.cloudflare.com/th-th/tag/api-shield/)[DLP](https://blog.cloudflare.com/th-th/tag/dlp/)[Firewall](https://blog.cloudflare.com/th-th/tag/firewall/)+1แสดงแท็กเพิ่มเติม 1 รายการ

4 แท็กแสดง 4 แท็ก

  * แท็กของโพสต์
  * [Security Week](https://blog.cloudflare.com/th-th/tag/security-week/)
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



[Security Week](https://blog.cloudflare.com/th-th/tag/security-week/)

[API Shield](https://blog.cloudflare.com/th-th/tag/api-shield/)[DLP](https://blog.cloudflare.com/th-th/tag/dlp/)[Firewall](https://blog.cloudflare.com/th-th/tag/firewall/)[Security Week](https://blog.cloudflare.com/th-th/tag/security-week/)

24 มีนาคม 2564

# ปกป้อง API ของคุณจากการละเมิดและการขโมยข้อมูล

![Daniele Molteni](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW464793D50Z8QJQK451PK2A.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Daniele Molteni](https://blog.cloudflare.com/th-th/author/daniele/)

อ่าน 3 นาที

คัดลอก URL

โพสต์นี้มีให้อ่านใน [English](https://blog.cloudflare.com/protecting-apis-from-abuse-and-data-exfiltration/) [日本語](https://blog.cloudflare.com/ja-jp/protecting-apis-from-abuse-and-data-exfiltration/) [繁體中文](https://blog.cloudflare.com/zh-tw/protecting-apis-from-abuse-and-data-exfiltration/) [简体中文](https://blog.cloudflare.com/zh-cn/protecting-apis-from-abuse-and-data-exfiltration/) และ[Bahasa Indonesia](https://blog.cloudflare.com/id-id/protecting-apis-from-abuse-and-data-exfiltration/).

![Protecting your APIs from abuse and data exfiltration](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48AEAJPZKXEE30QZSDB5ZR.png&w=1513&h=757&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/////v/98PLw5+np6Ovr7vDx7/Dx6urt///////+8fHv5ubl5ubm7Ozt7u7w6+vt////////8/Lw5uTj5eLi6+nq7+3w7u7w////////+Pb06+fm6eXl7+vt8/Hz8/L0//////////378/Dv8e/v9/T2+vn7+fn7/////////////Pv7+/v7////////////////////////////////////////////////////////////////////////////)

การรับส่งข้อมูล API เติบโตอย่างรวดเร็ว ปีที่แล้วเพียงปีเดียว ขอบของเราเติบโตเร็วกว่าการเข้าชมเว็บถึง 300% เนื่องจาก API ขับเคลื่อนแอปพลิเคชันมือถือและเว็บ การส่งคำสั่งที่หลากหลายเช่น “สั่งพิซซ่าจากร้านอาหารโปรดของฉันโดยใช้บัตรเครดิตใบนี้” หรือ “ทำการซื้อขายสกุลเงินดิจิทัลและนี่คือรายละเอียดส่วนตัวของฉัน” สิ่งเหล่านี้จึงสุกงอมพอสำหรับการโจรกรรมข้อมูลและการละเมิด การเปิดเผยข้อมูลถูกระบุว่าเป็นหนึ่งในภัยคุกคามอันดับต้น ๆ สำหรับการรับส่งข้อมูล API โดย OWASP; ซึ่งรวมถึงการรั่วไหลของข้อมูลและการกรองข้อมูลจากการตอบกลับของข้อมูลต้นทาง ([ความปลอดภัยของ API - ภัยคุกคาม 10 อันดับสูงสุดของปี 2019](https://owasp.org/www-project-api-security/)) การเพิ่มขึ้นของการรับส่งข้อมูลของ API และการโจมตีข้อมูลบ่อยครั้งขึ้นเรียกร้องให้มีโซลูชันการรักษาความปลอดภัยใหม่

ชุดเครื่องมือความปลอดภัยของ Cloudflare ได้รับการออกแบบมาเพื่อปกป้องการรับส่งข้อมูลของเว็บและ API มาโดยตลอด อย่างไรก็ตาม หลังจากที่ได้พูดคุยกับลูกค้าหลายร้อยราย เราก็พบว่ามีความจำเป็นในการปรับใช้และกำหนดค่าเครื่องมือรักษาความปลอดภัยสำหรับการรับส่งข้อมูล API ในอินเทอร์เฟซเดียว เพื่อตอบสนองความต้องการนี้ ในเดือนตุลาคม 2020 เราได้เปิดตัว [API ShieldTM](https://blog.cloudflare.com/introducing-api-shield/) ซึ่งเป็นผลิตภัณฑ์ใหม่ที่มีจุดประสงค์เพื่อรวบรวมโซลูชันการรักษาความปลอดภัยทั้งหมดที่ออกแบบมาสำหรับการรับส่งข้อมูล API เราเริ่มต้นด้วยการให้การรับรองความถูกต้อง mTLS แก่ผู้ใช้ Cloudflare ทั้งหมดโดยไม่เสียค่าใช้จ่าย รองรับ gRPC และการตรวจสอบความถูกต้องของสคีมาในรุ่นเบต้า ระหว่างการเปิดตัว เราได้วางแผนสำหรับการเปิดตัวในอนาคตด้วยฟังก์ชันการรักษาความปลอดภัยขั้นสูงเพิ่มเติม ตอนนี้เรารู้สึกตื่นเต้นที่จะสามารถขยายข้อเสนอของเราด้วยคุณลักษณะใหม่ที่ออกแบบมาเพื่อคุ้มครอง API ของคุณจากการเปิดเผยข้อมูลที่ละเอียดอ่อน

วันนี้ เรากำลังเปิดตัวคุณลักษณะสี่ประการเพื่อช่วยลดผลกระทบของการโจมตีด้วยการกรองข้อมูล: การตรวจสอบความถูกต้องของสคีมาสำหรับลูกค้าองค์กรทั้งหมด รายการ IP ที่มีการจัดการซึ่งช่วยให้คุณสามารถบล็อกการรับส่งข้อมูลจากพร็อกซีเปิด Certificate ควบคุมวงจรชีวิตได้มากขึ้น และโซลูชันการป้องกันข้อมูลสูญหาย ปลายสัปดาห์นี้ เรายังจะประกาศความสามารถที่จะช่วยให้คุณค้นพบ API ที่ทำงานบนเครือข่ายของคุณที่คุณอาจไม่ทราบ และวิธีการระบุคำขอผิดปกติที่เบี่ยงเบนไปจากการใช้งานที่ตั้งใจไว้

### การตรวจสอบสคีมามีอยู่ทั่วไป

ระหว่างการเปิดตัว API Shield เราได้แนะนำการตรวจสอบสคีและเปิดตัวให้กับลูกค้าบางรายที่เลือกไว้ ในช่วงไม่กี่เดือนที่ผ่านมา เราได้ทำงานร่วมกับผู้ที่เริ่มใช้งานในช่วงแรกๆ เพื่อเพิ่มความสามารถและสร้างอินเทอร์เฟซที่ใช้งานง่ายลงในแดชบอร์ดของเราโดยตรง ตอนนี้คุณสามารถนำทางไปยังแท็บ 'API Shield' ซึ่งคุณสามารถปรับใช้งานผลิตภัณฑ์ความปลอดภัย API ได้โดยตรงจาก UI โฟลว์การปรับใช้งานจะขยายเร็วๆ นี้เพื่อรวมความสามารถเพิ่มเติมที่พบในแดชบอร์ด เช่น mTLS และการจำกัดอัตรา นอกจากนี้ เรายังจะผสานรวมคุณลักษณะใหม่ๆ เช่น การตรวจหาความผิดปกติของ API เพื่อการวนรอบความคิดเห็นที่ง่ายดาย

การตรวจสอบความถูกต้องของสคีมาทำงานโดยการสร้างโมเดลความปลอดภัยเชิงบวกโดยยึดตาม “สคีมา” ของ API ซึ่งเป็นสัญญาที่กำหนดการใช้ API และแนะนำนักพัฒนาให้รวมเข้ากับระบบของพวกเขา ตรงกันข้ามกับรูปแบบการรักษาความปลอดภัยเชิงลบ (โดยที่กฎกำหนดลักษณะที่คำขอต้องมีเพื่อทริกเกอร์การดำเนินการ เช่น การบล็อก) การตรวจสอบความถูกต้องของสคีมาออกแบบมาเพื่ออนุญาตคำขอที่ได้รับการยืนยันว่าเป็นไปตามข้อกำหนดในขณะที่ดำเนินการกับอย่างอื่น การตรวจสอบความถูกต้องของสคีมายอมรับสคีมาที่เป็นไปตามข้อกำหนด OpenAPI v3 (หรือที่รู้จักในชื่อ Swagger Specification) ซึ่งเป็นมาตรฐานสำหรับการกำหนดอินเทอร์เฟซ RESTful ([เรียนรู้เพิ่มเติมที่หน้านี้](https://swagger.io/solutions/getting-started-with-oas/))

การตรวจสอบความถูกต้องของสคีมาจะประเมินคำขอแต่ละรายการเทียบกับการบันทึกสคีมา API หรือการบล็อกคำขอที่ไม่ปฏิบัติตาม

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Schema Validation evaluates each request against an API Schema logging or blocking requests that do not comply with it.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4999JT849QWCP3JPY8VFSX.png&w=715&h=625&f=webp&fit=cover&position=center)

API Shield นำเสนอ UI ที่ใช้งานง่าย ซึ่งผู้ใช้สามารถอัปโหลดสคีมาของตนไปยังไฟร์วอลล์ และสร้างกฎที่ตรวจสอบคำขอแต่ละรายการตามคำจำกัดความของ API โดยอัตโนมัติ หากคำขอเป็นไปตามข้อกำหนดก็จะถูกส่งต่อไปยังต้นทาง ในทางกลับกัน หากรูปแบบหรือเนื้อหาข้อมูลของคำขอไม่ตรงกับที่ API Shield คาดหวัง การเรียกนั้นจะถูกบันทึกหรือหลุดเพื่อปกป้องต้นทางจากคำขอที่ไม่ถูกต้องหรือเพย์โหลดที่เป็นอันตราย คำขอที่มีการป้อนข้อมูลจากภายนอกอาจไม่ได้คาดการณ์ไว้โดยนักพัฒนา API และอาจกระตุ้นการทำงานของแอปพลิเคชันที่คาดไม่ถึง เช่น ข้อมูลรั่วไหล

API Shield พร้อมการตรวจสอบสคีมาถูกปรับใช้โดยใช้สคีมา Cloudflare Rulesets OpenAPI ‌‌

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![API Shield with Schema Validation being deployed using the Cloudflare Rulesets OpenAPI schema.](https://blog.cloudflare.com/_emdash/api/media/file/01KW47MPZN1X4W79VKPX4D3HFR.gif)

UI จะแนะนำผู้ใช้ผ่านขั้นตอนต่างๆ ซึ่งรวมถึงการกำหนดชื่อโฮสต์และเส้นทางพื้นฐานของ API ที่จะปรับใช้ API Shield และอัปโหลดไฟล์สคีมา เมื่อปรับใช้ API Shield พร้อมการตรวจสอบสคีมาแล้ว จะสามารถตรวจสอบปลายทางที่ไฟร์วอลล์แยกวิเคราะห์และระดับการป้องกันที่ได้รับ ในหน้าการตรวจสอบ มีปลายทางสองกลุ่ม: มีการป้องกันและไม่ได้รับการป้องกัน รายการแสดงปลายทางและเมธอดอันเดิมทั้งหมดที่สคีมาได้รับการสนับสนุน ส่วนหลังระบุตำแหน่งปลายทางใดๆ ที่คำจำกัดความไม่ได้รับการสนับสนุนหรือคลุมเครือ เพื่อหลีกเลี่ยงการทำลายการรับส่งข้อมูลที่ส่งไปยังปลายทางที่ไม่อยู่ในไฟล์สคีมา เราได้รวมกฎขั้นสุดท้ายที่ตรงกับการรับส่งข้อมูลที่ไม่ได้ส่งไปยังปลายทางที่มีการป้องกันใดๆ

ทุกครั้งที่มีการระบุคำขอที่ไม่เป็นไปตามข้อกำหนดโดยการตรวจสอบสคีมาและการดำเนินการ เช่น การบล็อกหรือบันทึก เหตุการณ์ใหม่ที่แท็กด้วย 'API Shield' ต้นทางจะถูกสร้างขึ้นและเพิ่มลงในบันทึกของไฟร์วอลล์ ผู้ใช้สามารถเข้าถึงการวิเคราะห์และบันทึกโดยไปที่หน้าภาพรวม ซึ่งพวกเขาสามารถเจาะลึกข้อมูลโดยใช้ความยืดหยุ่นของแดชบอร์ดที่ขับเคลื่อนด้วย GraphQL ของเรา

การตรวจสอบความถูกต้องของสคีมาดำเนินการตรวจสอบเส้นทาง ตัวแปรพาธ พารามิเตอร์การค้นหา ส่วนหัว และคุกกี้ และอนุญาตให้บันทึกการรับส่งข้อมูลที่ไม่เป็นไปตามข้อกำหนด การตรวจสอบสคีมารุ่นเบต้าพร้อมใช้งานสำหรับลูกค้าองค์กรแล้ว — [กรอกแบบฟอร์มนี้](https://www.cloudflare.com/th-th/waf/api-shield/)เพื่อเข้าถึง

### การป้องกันข้อมูลรั่วไหล

การสูญเสียข้อมูลเป็นหนึ่งในปัญหาด้านความปลอดภัยที่ใหญ่ที่สุดที่ส่งผลกระทบต่อองค์กรขนาดเล็กและขนาดใหญ่ แต่ก็มีผลกระทบต่อบุคคลและความเป็นส่วนตัวด้วย การสูญเสียข้อมูลที่ละเอียดอ่อนอาจมีผลกระทบอย่างใหญ่หลวงต่อบริษัทในแง่ของผลกระทบทางการเงิน การพังทลายของมูลค่าแบรนด์ และการปฏิบัติตามกฎหมายล่าสุดเกี่ยวกับการปกป้องข้อมูล สุดท้าย การสูญเสียข้อมูลที่ละเอียดอ่อนของบุคคลอาจส่งผลเสียในแง่ของการสูญเสียทางการเงินและความกังวลเรื่องความเป็นส่วนตัว

ก่อนหน้านี้ เราได้ประกาศชุดผลิตภัณฑ์ Data Loss Prevention (DLP) ของเรา ขณะนี้ เรากำลังขยายขอบเขตนี้เพื่อระบุข้อมูลที่ละเอียดอ่อนที่ปล่อยให้ต้นทางของคุณอยู่ในขั้นตอนการตอบสนองของคำขอ HTTP หรือ API โซลูชันจะประเมินการรับส่งข้อมูลขาออก โดยตรวจสอบน้ำหนักบรรทุกเทียบกับรูปแบบทั่วไปของข้อมูลที่ละเอียดอ่อน ซึ่งรวมถึงข้อมูลส่วนบุคคลที่สามารถระบุตัวตนได้ เช่น หมายเลขประกันสังคมและข้อมูลทางการเงิน รวมถึงหมายเลขบัตรเครดิต รายละเอียดธนาคาร ฯลฯ สำหรับรุ่นแรก ผู้ใช้จะสามารถบันทึกการจับคู่ที่เรียกโดย DLP ได้ เรากำลังวางแผนที่จะเพิ่มการดำเนินการอื่นๆ เช่น การทำให้งงงวยและปิดกั้นข้อมูลที่ละเอียดอ่อนโดยปล่อยให้ต้นทางอยู่เบื้องหลัง Cloudflare ต่อไป เราตั้งใจที่จะให้ลูกค้ากำหนดกฎเกณฑ์เพื่อระบุข้อมูลที่ละเอียดอ่อนซึ่งเจาะจงกับแอปพลิเคชันของตนโดยเฉพาะ

เราพัฒนา DLP โดยคำนึงถึงความเรียบง่าย เพื่อให้ลูกค้าทุกคนสามารถได้รับการปกป้องโดยไม่ต้องมีช่วงเวลาการตั้งค่าที่ซับซ้อนและใช้เวลานาน เรากำลังเผยแพร่ DLP เป็นชุดกฎที่มีการจัดการซึ่งสามารถเปิดได้ผ่านแท็บกฎที่มีการจัดการของไฟร์วอลล์ สามารถใช้ DLP เป็นส่วนหนึ่งของ WAF ของ reverse proxy ได้ แต่ยังสามารถใช้เป็นส่วนหนึ่งของ Cloudflare สำหรับ Teams ที่รวมการปกป้องข้อมูลในการกำหนดค่า Zero Trust การผสานรวมที่รัดกุมนี้ช่วยให้ควบคุมได้ดียิ่งขึ้นว่าใครบ้างที่สามารถเข้าถึงข้อมูลที่ละเอียดอ่อนภายในองค์กรของคุณ

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-424 Embedded Image - Ew1rId](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48KJTRYYMM8458BQDTRRN0.png&w=715&h=343&f=webp&fit=cover&position=center)

DLP อยู่ในรุ่นเบต้าและเรากำลังเปิดตัวให้กับลูกค้าที่นำร่องที่เลือก โปรด[กรอกแบบฟอร์มนี้](https://www.cloudflare.com/th-th/waf/api-shield/)เพื่อเข้าร่วมรายการรอ

สามารถเปิดการป้องกันข้อมูลรั่วไหลเป็นชุดกฎที่มีการจัดการ

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Data Loss Protection can be turned on as a Managed Ruleset.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46VMJ3Q4E38K8HACD27MZQ.png&w=715&h=403&f=webp&fit=cover&position=center)

### รายการ IP ที่มีการจัดการ: ข้อมูลภัยคุกคามโดย Cloudflare

เรากำลังเปิดตัวรายการ IP ที่มีการจัดการรายการแรกซึ่งจะพร้อมใช้งานภายในกฎไฟร์วอลล์ ในเดือนกรกฎาคม 2020 [เราปล่อย IP Lists](https://blog.cloudflare.com/introducing-ip-lists/) ซึ่งทำให้ลูกค้าสามารถอัปโหลดรายการ IP จำนวนมากที่สามารถใช้เมื่อเขียนกฎไฟร์วอลล์ วันนี้ เรากำลังเปิดตัวรายการที่รวบรวมโดย Cloudflare และลูกค้าสามารถใช้ในกฎของตนได้เหมือนกับที่พวกเขาใช้รายการที่อัปโหลดแบบกำหนดเอง

'Cloudflare Open Proxies' มี IP ของ Open SOCKS และ HTTP Proxies ที่กำหนดโดย Cloudflare โดยการวิเคราะห์การรับส่งข้อมูลที่ขอบ นี่ไม่ได้จำกัดแค่คำขอ API เท่านั้น กฎสามารถนำไปใช้กับการรับส่งข้อมูลทุกประเภทที่ได้รับการประเมินโดยไฟร์วอลล์

รายการนี้เป็นฟีดแรกที่เรากำลังเผยแพร่ต่อสาธารณะโดยอิงตามข้อมูลภัยคุกคาม Cloudflare ที่ใช้ประโยชน์จากขนาดและการเข้าถึงเครือข่ายของเรา เราจะเติมรายการนี้ได้อย่างไร? เราเห็นคำขอจากทุกที่อยู่ IP ที่เปิดเผยต่อสาธารณะบนอินเทอร์เน็ต Cloudflare รวมรายการโอเพ่นซอร์สเข้ากับเครือข่ายขนาดใหญ่เพื่อระบุพร็อกซีแบบเปิด หลังจากตรวจสอบพร็อกซีแล้ว Cloudflare จะกำหนด IP ออกและสร้างรายการ จากนั้น เราจะดึงข้อมูลชื่อเสียงนี้กลับเข้าไปในระบบรักษาความปลอดภัยของเรา และทำให้ลูกค้าสามารถเข้าถึงได้ในรูปแบบของรายการ IP ที่มีการจัดการ

รายการนี้มีให้สำหรับแผนองค์กรทั้งหมด และสามารถใช้ได้โดยการเลือก 'Cloudflare Open Proxies' ในเมนูแบบเลื่อนลงเพื่อรวบรวมรายการ IP ที่มีอยู่ทั้งหมด (ดูภาพด้านล่าง)

สามารถใช้รายการที่มีการจัดการ Cloudflare Open Proxies ได้โดยตรงในตัวสร้างกฎไฟร์วอลล์

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare Open Proxies managed list can be used directly in the Firewall rule builder.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45RXVK8Y3HNQY66EK6YQ2B.png&w=715&h=404&f=webp&fit=cover&position=center)

### การควบคุมเพิ่มเติมเกี่ยวกับใบรับรองไคลเอ็นต์ (client certificates)

เราเปิดตัว mTLS ด้วย API Shield รุ่นแรกที่คำนึงถึงแอปมือถือและอุปกรณ์ IoT การบังคับใช้การรับรองความถูกต้องที่เข้มงวดด้วยใบรับรองฝั่งไคลเอ็นต์ (client certificates) เป็นมาตรการที่มีประสิทธิภาพมากในการปกป้องการรับส่งข้อมูลจากการขโมยข้อมูลและการละเมิดโดยทั่วไป อย่างไรก็ตาม ในกรณีที่อุปกรณ์ IoT หรือโทรศัพท์มือถือถูกขโมย สูญหาย หรือถูกควบคุมโดยผู้ประสงค์ร้าย ผู้ใช้ Cloudflare ต้องการวิธีเพิกถอนใบรับรองที่ถือว่ามีความเสี่ยงด้านความปลอดภัย ความสามารถในการแยกการรับส่งข้อมูลจากอุปกรณ์ที่ถูกบุกรุกอย่างถาวรเป็นวิธีที่มีประสิทธิภาพในการป้องกันข้อมูลสูญหายและการโจมตีที่เป็นอันตราย

ลูกค้าจำนวนมากของเราที่เริ่มฝังใบรับรอง API Shield ในแอปของตนได้ใช้โซลูชันการเพิกถอนโดยใช้ Workers with Workers KV แม้ว่าโซลูชันนี้จะอนุญาตให้มีการควบคุมแบบละเอียดบนใบรับรองได้ แต่ก็ต้องการความพยายามในการพัฒนาอย่างมากจากลูกค้าของเราและไม่สามารถปรับขนาดได้อย่างง่ายดาย

สำหรับสัปดาห์ความปลอดภัย เรากำลังเปิดตัวโซลูชันที่มีการจัดการเต็มรูปแบบเพื่อเพิกถอน (และกู้คืน) ใบรับรองโดยไม่ต้องเขียนโค้ดแม้แต่บรรทัดเดียว เราสร้างอินเทอร์เฟซที่ตรงไปตรงมาเพื่อจัดการวงจรชีวิตทั้งหมดของใบรับรองของคุณที่ขอบของเรา ตั้งแต่การออกไปจนถึงการเพิกถอน เราดูแลเรื่องนี้ให้คุณ ดังนั้นคุณจึงสามารถมุ่งเน้นไปที่การสร้างแอปพลิเคชันของคุณโดยไม่ต้องกังวลกับการตั้งค่าโครงสร้างพื้นฐานกุญแจสาธารณะ (PKI) ที่ซับซ้อนและมีราคาแพง และการจัดการการเพิกถอนอุปกรณ์ที่อาจมีความเสี่ยง จุดสัมผัสของลูกค้าคือปุ่ม 'เพิกถอน' และ 'กู้คืน' ใหม่ในแท็บใบรับรองไคลเอ็นต์ การเรียก API ที่รองรับ และฟิลด์ใหม่สำหรับกฎไฟร์วอลล์

คำขอแต่ละรายการที่นำเสนอใบรับรองไปยังขอบของ Cloudflare จะมีการตั้งค่าฟิลด์ไฟร์วอลล์สองฟิลด์: cf.tls_client_auth.cert_verified และ cf.tls_client_auth.cert_revoked คำขอได้รับการประมวลผลโดยไฟร์วอลล์ ซึ่งผู้ใช้สามารถรวมฟิลด์เหล่านี้กับฟังก์ชันไฟร์วอลล์อื่นๆ ทั้งหมดได้ สิ่งนี้ช่วยให้ลูกค้าสามารถกำหนดพฤติกรรมที่แตกต่างกันโดยขึ้นอยู่กับว่าใบรับรองได้รับการตรวจสอบหรือตรวจสอบแล้ว แต่ถูกเพิกถอน นอกจากนี้ มันยังช่วยให้คุณสามารถใช้นโยบายความปลอดภัยที่จำเป็นในขณะที่ให้ประสบการณ์ที่ดีแก่ผู้ใช้ปลายทาง การกำหนดค่าแบบคลาสสิกจะอนุญาตเฉพาะคำขอที่มีใบรับรองที่ตรวจสอบแล้ว ในขณะที่ส่งต่อคำขอจากใบรับรองที่ถูกเพิกถอนไปยังหน้าอื่นหรือปลายทางเพื่อจัดการกับข้อยกเว้นตามเส้นทางของผู้ใช้ของคุณ

ผู้ใช้สามารถเพิกถอนใบรับรองได้โดยไปที่แท็บใบรับรองไคลเอ็นต์ (Client Certificates)

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Users can revoke certificates by visiting the Client Certificates tab.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45K8895H405YXRB4WDXEA5.png&w=715&h=638&f=webp&fit=cover&position=center)

### อะไรกำลังเกิดขึ้นอยู่?

ทีม Cloudflare กำลังทำงานเพื่อเปิดตัวคุณลักษณะเพิ่มเติมภายใต้ร่ม API Shield เรากำลังพูดคุยกับลูกค้าหลายร้อยรายที่ใช้ Cloudflare สำหรับการรับส่งข้อมูล API และคุณสมบัติสามอย่างที่มีความสำคัญสูง: การวิเคราะห์ API เชิงลึก เครื่องมือจำกัดอัตราที่ยืดหยุ่นมากขึ้น และการผสานรวมกับการตรวจจับความผิดปกติ API

การตรวจสอบความถูกต้องของสคีมาและการป้องกันข้อมูลสูญหายได้รับการเผยแพร่ในวันนี้โดยมีการผสานรวมอย่างเต็มรูปแบบในบันทึกและเครื่องมือวิเคราะห์ของเรา ในอนาคต เรากำลังวางแผนที่จะขยายความสามารถในการวิเคราะห์การรับส่งข้อมูลและจัดหาเครื่องมือให้กับลูกค้าเพื่อระบุและจัดการการโจมตีที่มุ่งเป้าไปที่ API endpoints โดยเฉพาะ

การจำกัดอัตราของ Cloudflare ได้รับการออกแบบมาให้ทำงานได้ดีที่สุดสำหรับการเข้าชมเว็บ ซึ่งคุณสามารถเขียนกฎตาม URL และวิธีการขอ ขณะนี้ เรากำลังดำเนินการผสานรวมพลังของกฎไฟร์วอลล์เข้ากับการควบคุมที่จำกัดอัตราไว้ ซึ่งจะทำให้ผู้ใช้สามารถแบ่งกลุ่มการรับส่งข้อมูลโดยใช้ตรรกะอันทรงพลังที่มีอยู่ในไฟร์วอลล์ เรายังขยายกลไกการนับเพื่อรวมความสามารถในการให้คะแนนขีดจำกัดตามคีย์ API และ ID ผู้ใช้

เมื่อกำหนดเป้าหมายการรับส่งข้อมูล API รูปแบบการโจมตีอาจแตกต่างกันอย่างมาก ทำให้โซลูชันการจัดการ Bot แบบเดิมไม่ใช่ตัวเลือกที่เหมาะสมที่สุดในการระบุพฤติกรรมที่น่าสงสัย ในวันศุกร์นี้ เราจะประกาศคุณสมบัติหลักสองประการที่มุ่งเน้นไปที่การปกป้องแอปพลิเคชันของคุณต่อไป: การค้นพบ API และการตรวจจับความผิดปกติ การค้นพบช่วยให้ลูกค้าสามารถจับคู่ปลายทางและมองเห็นพื้นที่ผิวของ API ได้ การตรวจจับการทำงานผิดปกติของเครื่อง (Anomaly Detection) เป็นโซลูชันของ Cloudflare ในการแยกทราฟฟิก API ที่ดีออกจากกิจกรรมที่เป็นอันตรายได้อย่างน่าเชื่อถือและหลากหลาย ลูกค้าจะสามารถตั้งค่านี้ร่วมกับ mTLS, การตรวจสอบความถูกต้องของสคีมาและการจํากัดอัตราเพื่อเพิ่มระดับการป้องกันสูงสุด ดูบล็อกของเราในวันศุกร์เพื่อเรียนรู้เพิ่มเติมเกี่ยวกับผลิตภัณฑ์ใหม่เหล่านี้

ในหน้านี้

สนทนาออนไลน์

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fprotecting-apis-from-abuse-and-data-exfiltration%2F&t=%E0%B8%9B%E0%B8%81%E0%B8%9B%E0%B9%89%E0%B8%AD%E0%B8%87%20API%20%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B8%84%E0%B8%B8%E0%B8%93%E0%B8%88%E0%B8%B2%E0%B8%81%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%A5%E0%B8%B0%E0%B9%80%E0%B8%A1%E0%B8%B4%E0%B8%94%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%82%E0%B9%82%E0%B8%A1%E0%B8%A2%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%A1%E0%B8%B9%E0%B8%A5)[](https://x.com/intent/post?text=%E0%B8%9B%E0%B8%81%E0%B8%9B%E0%B9%89%E0%B8%AD%E0%B8%87+API+%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B8%84%E0%B8%B8%E0%B8%93%E0%B8%88%E0%B8%B2%E0%B8%81%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%A5%E0%B8%B0%E0%B9%80%E0%B8%A1%E0%B8%B4%E0%B8%94%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%82%E0%B9%82%E0%B8%A1%E0%B8%A2%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%A1%E0%B8%B9%E0%B8%A5&url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fprotecting-apis-from-abuse-and-data-exfiltration%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fprotecting-apis-from-abuse-and-data-exfiltration%2F)[](https://bsky.app/intent/compose?text=%E0%B8%9B%E0%B8%81%E0%B8%9B%E0%B9%89%E0%B8%AD%E0%B8%87+API+%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B8%84%E0%B8%B8%E0%B8%93%E0%B8%88%E0%B8%B2%E0%B8%81%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%A5%E0%B8%B0%E0%B9%80%E0%B8%A1%E0%B8%B4%E0%B8%94%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%82%E0%B9%82%E0%B8%A1%E0%B8%A2%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%A1%E0%B8%B9%E0%B8%A5+https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fprotecting-apis-from-abuse-and-data-exfiltration%2F)[](https://mastodonshare.com/?text=%E0%B8%9B%E0%B8%81%E0%B8%9B%E0%B9%89%E0%B8%AD%E0%B8%87+API+%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B8%84%E0%B8%B8%E0%B8%93%E0%B8%88%E0%B8%B2%E0%B8%81%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%A5%E0%B8%B0%E0%B9%80%E0%B8%A1%E0%B8%B4%E0%B8%94%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%82%E0%B9%82%E0%B8%A1%E0%B8%A2%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%A1%E0%B8%B9%E0%B8%A5&url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fprotecting-apis-from-abuse-and-data-exfiltration%2F)[](https://www.threads.net/intent/post?text=%E0%B8%9B%E0%B8%81%E0%B8%9B%E0%B9%89%E0%B8%AD%E0%B8%87+API+%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B8%84%E0%B8%B8%E0%B8%93%E0%B8%88%E0%B8%B2%E0%B8%81%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%A5%E0%B8%B0%E0%B9%80%E0%B8%A1%E0%B8%B4%E0%B8%94%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%82%E0%B9%82%E0%B8%A1%E0%B8%A2%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%A1%E0%B8%B9%E0%B8%A5+https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fprotecting-apis-from-abuse-and-data-exfiltration%2F)

## แท็กที่เกี่ยวข้อง

[API Shield](https://blog.cloudflare.com/th-th/tag/api-shield/)[DLP](https://blog.cloudflare.com/th-th/tag/dlp/)[Firewall](https://blog.cloudflare.com/th-th/tag/firewall/)[Security Week](https://blog.cloudflare.com/th-th/tag/security-week/)

ติดตามบนโซเชียลมีเดีย

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## สมัครรับการแจ้งเตือนโพสต์ใหม่

อีเมล

เราจะไม่เปิดเผยอีเมลของคุณ

สมัคร

ขอบคุณที่สมัครรับข่าวสาร! โปรดตรวจสอบกล่องจดหมายเพื่อยืนยัน
