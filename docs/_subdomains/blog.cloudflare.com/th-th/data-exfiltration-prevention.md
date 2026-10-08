---
url: https://blog.cloudflare.com/th-th/data-exfiltration-prevention/
title: \u0e01\u0e32\u0e23\u0e43\u0e0a\u0e49 Cloudflare \u0e2a\u0e33\u0e2b\u0e23\u0e31\u0e1a\u0e01\u0e32\u0e23\u0e1b\u0e49\u0e2d\u0e07\u0e01\u0e31\u0e19\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e2a\u0e39\u0e0d\u0e2b\u0e32\u0e22 (Data Loss Prevention) | \u0e1a\u0e25\u0e47\u0e2d\u0e01 Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:46:28.484358+00:00
---

# การใช้ Cloudflare สำหรับการป้องกันข้อมูลสูญหาย (Data Loss Prevention) | บล็อก Cloudflare

> Source: https://blog.cloudflare.com/th-th/data-exfiltration-prevention/

[บล็อก](https://blog.cloudflare.com/th-th/)

[Cloudflare One](https://blog.cloudflare.com/th-th/tag/cloudflare-one/)[Data Loss Prevention](https://blog.cloudflare.com/th-th/tag/data-loss-prevention/)[Security Week](https://blog.cloudflare.com/th-th/tag/security-week/)

3 แท็กแสดง 3 แท็ก

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



[Cloudflare One](https://blog.cloudflare.com/th-th/tag/cloudflare-one/)[Data Loss Prevention](https://blog.cloudflare.com/th-th/tag/data-loss-prevention/)[Security Week](https://blog.cloudflare.com/th-th/tag/security-week/)

24 มีนาคม 2564

# การใช้ Cloudflare สำหรับการป้องกันข้อมูลสูญหาย (Data Loss Prevention)

![Misha Yalavarthy](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW492FTNDM76E8SFJW5K9591.png&w=64&h=64&f=webp&fit=cover&position=center)

[Misha Yalavarthy](https://blog.cloudflare.com/th-th/author/misha/)

อ่าน 2 นาที

คัดลอก URL

โพสต์นี้มีให้อ่านใน [English](https://blog.cloudflare.com/data-exfiltration-prevention/) [Español](https://blog.cloudflare.com/es-es/data-exfiltration-prevention/) [日本語](https://blog.cloudflare.com/ja-jp/data-exfiltration-prevention/) [한국어](https://blog.cloudflare.com/ko-kr/data-exfiltration-prevention/) [简体中文](https://blog.cloudflare.com/zh-cn/data-exfiltration-prevention/) และ[Bahasa Indonesia](https://blog.cloudflare.com/id-id/data-exfiltration-prevention/).

![Using Cloudflare for Data Loss Prevention](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44JTYQQVKKKYR0QCYWWTXT.png&w=1870&h=984&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////+/3/8vLy7uvo8u7o9vPv8/Px7O3t////+v3/7+3u6eLe7OTc8uvk8/Dr7e7t////+v7/7Orr5NrV6drQ8eTa8+7m8PHt/////P//7uzt5tvW69rP8+Xa9/Do9PXx////////9fP37+Xi8+be++/n/ffy+fn4/////////v3/+/X1//fz//76/////v7/////////////////////////////////////////////////////////////////)

การขโมยข้อมูลหรือการสูญหายของข้อมูลอาจเป็นการทดสอบที่ใช้เวลานานและมีราคาแพง ซึ่งทำให้เกิดการสูญเสียทางการเงิน การเชื่อมโยงแบรนด์เชิงลบ และบทลงโทษจากกฎหมายที่เน้นความเป็นส่วนตัว ยกตัวอย่าง เหตุการณ์ที่สมาร์ทกริดที่มีความละเอียดอ่อนและวัดข้อมูลความรู้ด้านการวิจัยและพัฒนาจาก[ระบบควบคุมอุตสาหกรรมของยูทิลิตี้ไฟฟ้าในอเมริกาเหนือ](https://www.power-grid.com/td/what-we-learned-from-a-data-exfiltration-incident-at-an-electric-utility/#gref)ถูกกรองผ่านการโจมตีที่สงสัยว่ามีต้นตอมาจากภายในเครือข่าย การเข้าถึงข้อมูลจากบริษัทสาธารณูปโภคโดยไม่ได้รับอนุญาตอาจส่งผลให้สมาร์ทกริดหรือไฟฟ้าดับได้

ในอีกตัวอย่างหนึ่ง นักวิจัยด้านความปลอดภัยพบ API endpoints ที่เปิดเผยและไม่รู้จัก (ไม่มีเอกสาร) สำหรับ[เกตเวย์สำรองของเทสลา](https://blog.rapid7.com/2020/11/17/dont-put-it-on-the-internet-tesla-backup-gateway-edition/)ที่สามารถใช้เพื่อส่งออกข้อมูลหรือทำการเปลี่ยนแปลงโดยไม่ได้รับอนุญาต สิ่งนี้จะมีผลกระทบทางกายภาพอย่างแท้จริงหากผู้โจมตีใช้ API endpoint ที่ไม่ผ่านการตรวจสอบสิทธิ์เพื่อสร้างความเสียหายให้กับแบตเตอรี่หรือกริดไฟฟ้าที่เชื่อมต่อ

ที่มา: รายงานการตรวจสอบการละเมิดข้อมูล Verizon 2020

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Source: Verizon 2020 Data Breach Investigations Report](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44JXVW3E4W8DAJXXQM4B61.png&w=715&h=161&f=webp&fit=cover&position=center)

ตัวอย่างทั้งสองนี้เน้นย้ำถึงความสำคัญของการพิจารณาภัยคุกคามภายในและภายนอกเมื่อคิดถึงวิธีป้องกันเครือข่ายจากการขโมยข้อมูล ภัยคุกคามจากข้อมูลภายในไม่จำเป็นว่าผู้ใช้จะจงใจสร้างความเสียหาย: ตามรายงานภัยคุกคามจากภายในปี 2019 ของ Fortinet จากองค์กรที่สำรวจ 71% มีความกังวลเกี่ยวกับผู้ใช้ที่ประมาททำให้เกิดการละเมิดโดยไม่ได้ตั้งใจ และ 65% กังวลเกี่ยวกับผู้ใช้ที่เพิกเฉยต่อนโยบายแต่ไม่มุ่งร้าย ผู้โจมตีที่ดำเนินการสำเร็จ[แฮ็ค Twitter ในปี 2020](https://www.dfs.ny.gov/Twitter_Report)เพื่อเข้าถึงบัญชีที่โดดเด่นที่เริ่มต้นด้วยการโจมตีทางวิศวกรรมสังคมต่อพนักงาน จากนั้นผู้โจมตีได้เปลี่ยนไปใช้เครื่องมือการดูแลระบบภายในเพื่อเปลี่ยนการตั้งค่าบัญชีลูกค้า รวมถึงการโพสต์ในนามของพวกเขาหรือแก้ไขอีเมลและ 2FA

บนพื้นผิวอาจดูเหมือนเป็นเพียงการหลอกลวง Bitcoin แต่ผู้โจมตีก็เช่นกัน[ดาวน์โหลดและดึงข้อมูลออกจากบัญชีเจ็ดบัญชี](https://blog.twitter.com/en_us/topics/company/2020/an-update-on-our-security-incident.html)หากบัญชีของผู้ใช้ภายในถูกบุกรุกได้สำเร็จผ่านการพยายาม vishing(วิชชิ่ง)(รูปแบบหนึ่งของการโจมตีทางวิศวกรรมสังคมที่ใช้ฟิชชิ่งด้วยเสียง) การเพิ่มฮาร์ดคีย์หรือการใช้สิทธิ์บัญชีแบบละเอียดกับเครื่องมือการดูแลระบบอาจขัดขวางการเข้าถึงของผู้โจมตี ต่อมาในสัปดาห์ความปลอดภัย เราจะอธิบายการแฮ็ก Twitter จากมุมของการโจมตีเพื่อเข้าครอบครองบัญชีและวิธีที่จะสามารถบรรเทาได้

การขโมยข้อมูลไม่จำเป็นต้องใช้เทคนิคที่ซับซ้อนหรือเครื่องมือที่คลุมเครือ ผู้ใช้ที่ถูกฟิชชิ่งร่วมกับนโยบายที่อนุญาตเกินบนปลายทาง แทนที่จะใช้บัญชี สามารถให้ผู้โจมตีเข้าถึงที่จำเป็นสำหรับการกรองข้อมูล การบล็อกโดเมนที่เป็นอันตรายในโซลูชันการป้องกันอีเมลของคุณเป็นขั้นตอนที่ทีมรักษาความปลอดภัยจำนวนมากพึ่งพาเพื่อตอบสนองต่อการโจมตีทางวิศวกรรมสังคม แต่จะเกิดอะไรขึ้นถ้าทรัพยากรที่เป็นอันตรายถูกแบ่งปันจากด้านข้างและไม่ใช่จากแหล่งภายนอกไปยังแหล่งภายใน โดเมนที่เป็นอันตรายสามารถแชร์ระหว่างพนักงานในการแชทหรือผ่านรูปแบบการสื่อสารอื่นที่ไม่ใช่อีเมล สิ่งนี้ทำให้เกิดช่องว่างที่ทำให้ทีมรักษาความปลอดภัยเสียเปรียบในการปกป้องผู้ใช้และข้อมูลภายใน

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-401 Embedded Image - hEAYC0](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44S40W838XYEXXDAJ2J1QA.png&w=715&h=248&f=webp&fit=cover&position=center)

เราให้ความสำคัญกับแนวทางการป้องกันและติดตามแบบหลายชั้นเสมอมา สำหรับเครื่องมือภายในของเรา เรามีการควบคุมการเข้าถึงตามบทบาทและตามความเสี่ยง เราวางแอปพลิเคชันของเราไว้ด้านหลัง Access เพื่อเพิ่มชั้นการอนุญาตที่ด้านบนของการรับรองความถูกต้อง การเพิ่มแอปพลิเคชัน SaaS เบื้องหลัง Access ช่วยให้เราเชื่อมต่อผู้ใช้กับสิ่งที่พวกเขาต้องการได้อย่างปลอดภัย ไม่ว่าจะเป็นในสถานที่หรือในระบบคลาวด์ ด้วยพนักงานจากระยะไกล Access ช่วยให้เรากำหนดค่านโยบายตามสถานที่ ประเภทอุปกรณ์ ตำแหน่งอุปกรณ์ และวิธีการ MFA เมื่อเราก้าวไปสู่สภาพแวดล้อมที่ไม่ใช้ VPN Access จะทำหน้าที่เป็นอุโมงค์ที่ปลอดภัย ทีมตรวจจับและตอบสนองของเราจะตรวจสอบทั้งบันทึกการเข้าถึงและบันทึกแอปพลิเคชัน SaaS เพื่อหาความผิดปกติ ในไม่ช้า เราจะเพิ่มการบันทึกการเข้าใช้ภายในแอปพลิเคชัน SaaS ซึ่งจะทำให้บันทึกสมบูรณ์ยิ่งขึ้นและปรับบริบทให้เหมาะสม

การปกป้องปลายทางโดยใช้ Cloudflare ยังรวมถึงไคลเอ็นต์ที่ใช้ในการบังคับใช้นโยบายด้วย กฎไฟร์วอลล์ของเกตเวย์สามารถใช้กับ Access เพื่อใช้แนวทางแบบองค์รวมมากขึ้นที่เลเยอร์ L4 (เครือข่าย) และ L7 (HTTP) เราใช้ตำแหน่งเกตเวย์เพื่อจำกัดการสืบค้น DNS ให้กับโดเมนที่เป็นอันตราย

เนื่องจากพนักงานทำงานจากระยะไกล บริษัทต่างๆ จะไม่สามารถบังคับใช้นโยบายเครือข่ายที่จุดออกของสำนักงานของบริษัทได้ ด้วยการใช้ไคลเอนต์เดสก์ท็อป WARP ของเราร่วมกับเกตเวย์บนจุดปลายผู้ใช้ของเรา ทีมรักษาความปลอดภัยสามารถมองเห็นบันทึก DNS พร้อมความสามารถในการบังคับใช้นโยบายที่ครั้งหนึ่งเคยสามารถใช้ได้ในสำนักงานของบริษัทในขณะที่รักษาความเป็นส่วนตัว เกตเวย์ทำหน้าที่เป็นตัวแก้ไข DNS บนอุปกรณ์ขององค์กร ซึ่งไม่เพียงแต่ช่วยให้ทีมตอบสนองต่อเหตุการณ์และระบุสาเหตุได้อย่างมีประสิทธิภาพมากขึ้น แต่ยังช่วยป้องกันด้วยการระบุเครื่องที่ถูกบุกรุกซึ่งเยี่ยมชมโดเมนที่เป็นอันตราย WARP ช่วยให้มั่นใจได้ว่าการรับส่งข้อมูล DNS ได้รับการเข้ารหัส ดังนั้นจึงเป็นการปกป้องความเป็นส่วนตัวของผู้ใช้

เครื่องมือแยกเบราว์เซอร์ของเราให้การป้องกันในชั้นที่ใกล้กับผู้ใช้มากที่สุดและเป็นที่ที่พวกเขาอาจใช้เวลาส่วนใหญ่ในการเข้าถึงแอปพลิเคชันบนคลาวด์ มันมีประโยชน์ทั้งการป้องกันและการตอบสนอง มันสามารถใช้เพื่อลบการเข้าถึงบางแอป SaaS ป้องกันไม่ให้ผู้ใช้คัดลอก/วาง จำกัดการพิมพ์ และบล็อกการดาวน์โหลดไฟล์ กล่าวอีกนัยหนึ่ง ข้อมูลที่โฮสต์ในบริการคลาวด์สามารถป้องกันได้ในหลายจุดที่สำคัญ ซึ่งจะทำให้ยากต่อการกรองข้อมูล ผ่านนโยบาย การแยกเบราว์เซอร์สามารถกำหนดค่าสำหรับแต่ละโดเมน ผู้ใช้ และหรือหมวดหมู่กว้างๆ ของเว็บไซต์ การแยกเบราว์เซอร์ยังช่วยให้ผู้ตอบสนองสามารถระบุจุดปลายที่อาจถูกบุกรุกโดยการจับโดเมนที่เป็นอันตรายที่รู้จักหรือดาวน์โหลดไฟล์บางไฟล์ผ่านเบราว์เซอร์ได้อย่างรวดเร็ว

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-401 Embedded Image - wW9Ppy](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW485X2T19A08SP41SVPG8WE.png&w=715&h=373&f=webp&fit=cover&position=center)

นี่คือจุดเริ่มต้นของโมเดล Zero Trust หากคุณไม่เคยได้ยินเรื่องนี้มาก่อน นี่เป็นการแนะนำข้อเสนอที่[ดี](https://www.cloudflare.com/learning/security/glossary/what-is-zero-trust/) Cloudflare Access เป็นส่วนสำคัญของชุดเครื่องมือของ Cloudflare One ที่ช่วยให้องค์กรต่างๆ ใช้โมเดล Zero Trust บนเครือข่ายของพวกเขา เราใช้ Cloudflare Access เพื่อจัดการแนวทางนโยบายที่เป็นหนึ่งเดียวกันสำหรับทรัพยากรภายใน ในฐานะวิศวกรความปลอดภัยในทีมตรวจจับและตอบสนองที่ตอบสนองต่อเหตุการณ์ที่เราต้องทำการเปลี่ยนแปลงการเข้าถึงทั่วทั้งบริษัท Cloudflare Access และ Cloudflare Access สำหรับแอปพลิเคชัน SaaS ทำให้เราอยู่ในฐานะที่จะผลักดันนโยบายอย่างมีประสิทธิภาพและมุ่งเน้นไปที่รายการที่มีลำดับความสำคัญสูงกว่า โดยไม่ต้องกังวลเกี่ยวกับการเปลี่ยนแปลงระดับแอปพลิเคชัน การจัดการการเข้าถึงที่จุดศูนย์กลางสำหรับแอปพลิเคชันที่มิฉะนั้นจะต้องได้รับการจัดการทีละรายการจะช่วยปรับปรุงเวลาในการตอบสนองของเราได้อย่างมาก

การย้ายไปยังเลเยอร์ API นั้น API Shield ของ Cloudflare ทำหน้าที่เป็นจุดหลักในการจัดการการควบคุมความปลอดภัยของ API ลองนึกถึงอุปกรณ์ IoT ที่เปิดเผยผ่าน API จำนวนมาก เช่น เกตเวย์ของเทสลา API Shield ให้แนวทางแบบหลายชั้นเพื่อจำกัดการเปิดเผยข้อมูลโดยไม่ได้ตั้งใจ ตัวอย่างเช่น สคีมาสามารถตรวจสอบได้เพื่อลดโอกาสที่ระบบดาวน์สตรีมจะถูกบุกรุกโดยอินพุตที่ไม่คาดคิด คำขอไปยังปลายทางสามารถจำกัดได้เฉพาะไคลเอ็นต์ที่มีใบรับรอง SSL/TLS ของไคลเอ็นต์ที่ถูกต้อง และสัญญาณรบกวนที่มาจากแหล่งที่มา เช่น พร็อกซี Open SOCKS สามารถกรองออกได้ พร้อมกับคำขอที่มาจากอุปกรณ์หรือภูมิภาคที่ API ไม่ควรสื่อสารด้วย การประกาศในวันนี้รวมถึงความสามารถในการสร้างความสับสนของข้อมูล และในปลายสัปดาห์นี้ เราจะประกาศวิธีการค้นพบ API "เงา" ที่ทีมรักษาความปลอดภัยของคุณอาจไม่ทราบ และตรวจพบกิจกรรมการโทรที่ผิดปกติ

ในฐานะวิศวกรการตรวจจับและการตอบสนอง มีหลายเหตุการณ์ที่ปัญหาด้านความปลอดภัยต้องการให้เราเข้าใจว่าการเข้าถึงระบบเหล่านี้ทำงานอย่างไรในทันที ระบบที่แตกต่างกันได้รับการจัดการที่แตกต่างกัน และบทบาทไม่ได้ถูกกำหนดอย่างเหมือนกันเสมอไป สิ่งนี้ทำให้การตอบกลับในขณะนั้นทำได้ยากมากและบ่อยครั้งกว่านั้น ทำให้เราต้องสนทนากับเจ้าของระบบเพื่อทำความเข้าใจการเข้าถึงให้ดียิ่งขึ้น การใช้การป้องกันแบบหลายชั้นที่ Cloudflare One, Browser Isolation และ API Shield มีให้ ทีมรักษาความปลอดภัยอยู่ในตำแหน่งที่พวกเขาสามารถมุ่งเน้นไปที่การป้องกันแทนที่จะตอบสนอง

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-401 Embedded Image - XmfgWu](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW490CNAXGQ5K7X0GMEVYM6P.png&w=715&h=298&f=webp&fit=cover&position=center)

ในหน้านี้

สนทนาออนไลน์

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fdata-exfiltration-prevention%2F&t=%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%83%E0%B8%8A%E0%B9%89%20Cloudflare%20%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9B%E0%B9%89%E0%B8%AD%E0%B8%87%E0%B8%81%E0%B8%B1%E0%B8%99%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%A1%E0%B8%B9%E0%B8%A5%E0%B8%AA%E0%B8%B9%E0%B8%8D%E0%B8%AB%E0%B8%B2%E0%B8%A2%20%28Data%20Loss%20Prevention%29)[](https://x.com/intent/post?text=%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%83%E0%B8%8A%E0%B9%89+Cloudflare+%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9B%E0%B9%89%E0%B8%AD%E0%B8%87%E0%B8%81%E0%B8%B1%E0%B8%99%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%A1%E0%B8%B9%E0%B8%A5%E0%B8%AA%E0%B8%B9%E0%B8%8D%E0%B8%AB%E0%B8%B2%E0%B8%A2+%28Data+Loss+Prevention%29&url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fdata-exfiltration-prevention%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fdata-exfiltration-prevention%2F)[](https://bsky.app/intent/compose?text=%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%83%E0%B8%8A%E0%B9%89+Cloudflare+%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9B%E0%B9%89%E0%B8%AD%E0%B8%87%E0%B8%81%E0%B8%B1%E0%B8%99%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%A1%E0%B8%B9%E0%B8%A5%E0%B8%AA%E0%B8%B9%E0%B8%8D%E0%B8%AB%E0%B8%B2%E0%B8%A2+%28Data+Loss+Prevention%29+https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fdata-exfiltration-prevention%2F)[](https://mastodonshare.com/?text=%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%83%E0%B8%8A%E0%B9%89+Cloudflare+%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9B%E0%B9%89%E0%B8%AD%E0%B8%87%E0%B8%81%E0%B8%B1%E0%B8%99%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%A1%E0%B8%B9%E0%B8%A5%E0%B8%AA%E0%B8%B9%E0%B8%8D%E0%B8%AB%E0%B8%B2%E0%B8%A2+%28Data+Loss+Prevention%29&url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fdata-exfiltration-prevention%2F)[](https://www.threads.net/intent/post?text=%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%83%E0%B8%8A%E0%B9%89+Cloudflare+%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9B%E0%B9%89%E0%B8%AD%E0%B8%87%E0%B8%81%E0%B8%B1%E0%B8%99%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%A1%E0%B8%B9%E0%B8%A5%E0%B8%AA%E0%B8%B9%E0%B8%8D%E0%B8%AB%E0%B8%B2%E0%B8%A2+%28Data+Loss+Prevention%29+https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fdata-exfiltration-prevention%2F)

## แท็กที่เกี่ยวข้อง

[Cloudflare One](https://blog.cloudflare.com/th-th/tag/cloudflare-one/)[Data Loss Prevention](https://blog.cloudflare.com/th-th/tag/data-loss-prevention/)[Security Week](https://blog.cloudflare.com/th-th/tag/security-week/)

ติดตามบนโซเชียลมีเดีย

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## สมัครรับการแจ้งเตือนโพสต์ใหม่

อีเมล

เราจะไม่เปิดเผยอีเมลของคุณ

สมัคร

ขอบคุณที่สมัครรับข่าวสาร! โปรดตรวจสอบกล่องจดหมายเพื่อยืนยัน
