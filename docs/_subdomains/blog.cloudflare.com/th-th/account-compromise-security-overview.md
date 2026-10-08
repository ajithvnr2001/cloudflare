---
url: https://blog.cloudflare.com/th-th/account-compromise-security-overview/
title: \u0e20\u0e32\u0e22\u0e43\u0e19 Cloudflare: \u0e1b\u0e49\u0e2d\u0e07\u0e01\u0e31\u0e19\u0e01\u0e32\u0e23\u0e41\u0e2d\u0e1a\u0e2d\u0e49\u0e32\u0e07\u0e40\u0e1b\u0e47\u0e19\u0e40\u0e08\u0e49\u0e32\u0e02\u0e2d\u0e07\u0e1a\u0e31\u0e0d\u0e0a\u0e35 | \u0e1a\u0e25\u0e47\u0e2d\u0e01 Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:52:22.517501+00:00
---

# ภายใน Cloudflare: ป้องกันการแอบอ้างเป็นเจ้าของบัญชี | บล็อก Cloudflare

> Source: https://blog.cloudflare.com/th-th/account-compromise-security-overview/

[บล็อก](https://blog.cloudflare.com/th-th/)

[Cloudflare Access](https://blog.cloudflare.com/th-th/tag/cloudflare-access/)[Cloudflare Gateway](https://blog.cloudflare.com/th-th/tag/gateway/)[Security Week](https://blog.cloudflare.com/th-th/tag/security-week/)+1แสดงแท็กเพิ่มเติม 1 รายการ

4 แท็กแสดง 4 แท็ก

  * แท็กของโพสต์
  * [Cloudflare Access](https://blog.cloudflare.com/th-th/tag/cloudflare-access/)[Cloudflare Gateway](https://blog.cloudflare.com/th-th/tag/gateway/)[Security Week](https://blog.cloudflare.com/th-th/tag/security-week/)[ความปลอดภัย](https://blog.cloudflare.com/th-th/tag/security/)
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



[ความปลอดภัย](https://blog.cloudflare.com/th-th/tag/security/)

[Cloudflare Access](https://blog.cloudflare.com/th-th/tag/cloudflare-access/)[Cloudflare Gateway](https://blog.cloudflare.com/th-th/tag/gateway/)[Security Week](https://blog.cloudflare.com/th-th/tag/security-week/)[ความปลอดภัย](https://blog.cloudflare.com/th-th/tag/security/)

30 มีนาคม 2564

# ภายใน Cloudflare: ป้องกันการแอบอ้างเป็นเจ้าของบัญชี

![Julie A. Sparks](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44BAJVDRPB1FB1M1Z9V77K.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Julie A. Sparks](https://blog.cloudflare.com/th-th/author/julie/)

อ่าน 2 นาที

คัดลอก URL

โพสต์นี้มีให้อ่านใน [English](https://blog.cloudflare.com/account-compromise-security-overview/)และ[Bahasa Indonesia](https://blog.cloudflare.com/id-id/account-compromise-security-overview/).

![Inside Cloudflare: Preventing Account Takeovers](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW485JWNNH1XYV6F9WJBYZXW.png&w=1585&h=740&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA+ffe9PLb6+bU5t3O59zN6t/N6OHM4t/I/fvj+Pbg7+ra6uHV7OHU7+XU7ebS5uPN///p/fvn9O/h7+bd8ufd9uvd8+zZ6+jT///w///t+fPm9erj+ezj/fLk+vPh8e7a///2///x//bp+u3l/vDn//fp//jm9/Lf///6///0//jp/u7j//Ln//rs//zq/Pbi///8///1//no/+/h//Pm//zt//7s//jk///9///2//no/+/g//Pm//3t//7t//jk)

ตลอดสัปดาห์ที่ผ่านมา Cloudflare ได้เผยแพร่บล็อกโพสต์เกี่ยวกับผลิตภัณฑ์ที่สร้างขึ้นเพื่อรักษาความปลอดภัยลูกค้าของเราจาก[บ็อต credentials stuffing](https://blog.cloudflare.com/super-bot-fight-mode/) , [ตรวจจับผู้ใช้ที่มีข้อมูลประจำตัวที่ถูกบุกรุก](https://blog.cloudflare.com/account-takeover-protection) และ[ปิดกั้นผู้ใช้จากบริการพร็อกซี](https://blog.cloudflare.com/protecting-apis-from-abuse-and-data-exfiltration/) แต่เราจะทำอย่างไรภายใน Cloudflare เพื่อป้องกันการเข้าครอบครองบัญชีในแอปพลิเคชันของเราเอง ทีมรักษาความปลอดภัยใช้ผลิตภัณฑ์ Cloudflare เพื่อป้องกันการบุกรุกบัญชีในเชิงรุก เรายังมีระบบตรวจจับและการทำงานอัตโนมัติเป็นเลเยอร์ที่สองเพื่อแจ้งเตือนเราหากบัญชีพนักงานถูกบุกรุก เพื่อให้แน่ใจว่าเราสามารถตรวจจับพฤติกรรมที่น่าสงสัย ตรวจสอบ และแก้ไขได้อย่างรวดเร็ว

เป้าหมายของเราคือป้องกันผู้โจมตีแบบอัตโนมัติและแบบกำหนดเป้าหมาย โดยไม่คำนึงถึงเทคนิคการแอบอ้างเป็นเจ้าของบัญชี: การโจมตีด้วย brute force, credential stuffing, บ็อตเน็ต วิศวกรรมโซเชียล หรือฟิชชิ่ง

### วงจรการแอบอ้างเป็นเจ้าของบัญชีแบบคลาสสิก

อันดับแรก มาดูวงจรชีวิตทั่วไปสำหรับบัญชีที่ถูกบุกรุก

สถานการณ์ที่พบเห็นโดยทั่วไปคือการละเมิดรหัสผ่านและที่อยู่อีเมลหลายครั้ง ข้อมูลประจำตัวเหล่านี้ถูกนำมาใช้ซ้ำผ่าน credential stuffing เพื่อพยายามเข้าถึงบัญชีใด ๆ (บนแพลตฟอร์มใด ๆ ) ที่ผู้ใช้อาจใช้ข้อมูลข้างต้นซ้ำไปซ้ำมา เมื่อผู้โจมตีเข้าถึงครั้งแรกได้สำเร็จ ซึ่งหมายความว่ารหัสผ่านและที่อยู่อีเมลที่ใช้ร่วมกันได้ผล พวกเขาจะนำข้อมูลที่ได้จากระบบนั้นมาใช้กับระบบอื่น ๆ ผ่านวิธีการต่างๆ ลักษณะนี้จัดอยู่ในประเภทการเคลื่อนย้ายแบบด้านข้าง ด้วยรหัสผ่านเดียวที่รั่วไหล มีความเป็นไปได้ที่บริษัทที่ไม่เกี่ยวข้องจะเกิดการละเมิดโดยที่ผู้ใช้ที่ไม่ได้รับอนุญาตลงชื่อเข้าใช้และขโมยข้อมูล

การแอบอ้างเป็นเจ้าของบัญชีอีกรูปแบบหนึ่งคือ อีเมลฟิชชิ่งพร้อมลิงก์ที่ส่งถึงพนักงานโดยมีเป้าหมายเพื่อดึงข้อมูลประจำตัวของพนักงาน กลวิธีทั่วไปที่ผู้โจมตีใช้คือ Evilginx ซึ่งเป็นเฟรมเวิร์กการโจมตีแบบคนกลางที่ใช้เพื่อหลอกดึงข้อมูลประจำตัวและคุกกี้เซสชันของบริการเว็บใด ๆ ผู้โจมตีจะสร้างเพจที่คล้ายกับพอร์ทัลล็อกอินของบริษัท เพื่อดักจับการรับส่งข้อมูล และเก็บข้อมูลประจำตัวที่ป้อนลงในเพจไว้ เมื่อรวบรวมข้อมูลประจำตัวไว้ได้แล้ว ผู้โจมตีจะเข้าสู่ระบบในฐานะผู้ใช้ทันที ก่อนคัดกรองข้อมูล และพยายามลดทอนความแข็งแกร่งของระบบ/บัญชีที่เกี่ยวข้อง แต่เพราะมีการปรับปรุงระบบกรองอีเมลฟิชชิ่ง ผู้โจมตีจึงเลือกใช้วิธีการวิศวกรรมโซเชียลทางโทรศัพท์เพื่อให้พนักงานเข้าชมเว็บไซต์ที่เป็นอันตราย เช่น เว็บไซต์ที่กล่าวถึงข้างต้น

สองวิธีที่พบบ่อยที่สุดในการเพิ่มการตรวจสอบเพิ่มเติม คือการใช้รหัสผ่านครั้งเดียวแบบตามเวลา (TOTP) หรือรหัสยืนยันผ่านข้อความ (SMS) เป็นตัวเลือกการตรวจสอบสิทธิ์แบบหลายปัจจัย โดย TOTP จะสร้างรหัสผ่านแบบใช้ครั้งเดียวซึ่งใช้เวลาปัจจุบันเป็นต้นทางกำหนดลักษณะเฉพาะเจาะจง ซึ่งวิธีนี้มักได้มาจากแอปพลิเคชันมือถือ เช่น Google Authenticator แต่วิธีการตรวจสอบสิทธิ์แบบหลายปัจจัยทั้งสองวิธีเหล่านี้ไม่สามารถป้องกันการเข้าสวมบัญชีได้ เนื่องจากผู้โจมตีสามารถใช้กลวิธีทางวิศวกรรมโซเซียลเพื่อหลอกให้พนักงานบอกรหัส TOTP หรือ SMS นอกจากนี้ ผู้โจมตียังสามารถทำการสลับซิม ซึ่งเป็นกลวิธีที่ผู้ให้บริการโทรศัพท์ถูกหลอกให้กำหนดหมายเลขโทรศัพท์ของบุคคลอื่นให้กับอุปกรณ์เครื่องใหม่ เพื่อรับรหัสยืนยันที่ส่งไปยังอุปกรณ์ของผู้โจมตี

การแอบอ้างเป็นเจ้าของบัญชีเป็นภัยคุกคามต่อบริษัทและผู้ใช้อย่างแท้จริง มาดูตัวอย่างที่จับต้องได้ของการละเมิดความปลอดภัยลักษณะนี้ และวิธีป้องกันในหลายระดับโดยใช้ Cloudflare

## ตัวอย่างจริงของการแอบอ้างเป็นเจ้าของบัญชี

ในปี 2020 ตัวอย่างของผลกระทบของการแอบอ้างเป็ฯเจ้าของบัญชีถูกแสดงให้เห็นเมื่อผู้โจมตีสามารถ[ล้วงข้อมูลประจำตัวพนักงาน Twitter สำหรับใช้เข้าสู่ระบบ](https://www.wsj.com/articles/the-teenager-behind-the-twitter-hack-and-how-he-did-it-11596563449) แล้วเข้าถึงบัญชี Twitter ที่ยืนยันแล้วนับสิบบัญชี วัยรุ่นจากฟลอริดาปลอมหมายเลขโทรศัพท์ของพนักงานด้วยการแลกเปลี่ยนซิม ซึ่งเป็นกลวิธีที่นำมาใช้เพื่อให้ผู้ให้บริการโทรศัพท์กำหนดหมายเลขโทรศัพท์ของบุคคลอื่นให้กับอุปกรณ์เครื่องใหม่ จากนั้นผู้โจมตีก็ทำวิศวกรรมโซเชียลให้กับพนักงาน Twitter โดยแสร้งทำเป็นเป็นสมาชิกแผนกไอทีของพนักงาน เมื่อพนักงานเชื่อตามนั้น ผู้โจมตีจะแนะนำให้พนักงานไปยังหน้าฟิชชิ่งที่คล้ายกับพอร์ทัลเข้าสู่ระบบ Okta ของ Twitter เมื่อพนักงานป้อนข้อมูลประจำตัวลงในหน้าที่ดูเหมือนถูกต้องตามกฎหมาย ผู้โจมตีก็สามารถใช้ข้อมูลดังกล่าวเพื่อเข้าถึงระบบของ Twitter ได้ การโจมตีนี้เกิดขึ้นได้เนื่องจากการใช้ SMS และ/หรือ TOTP สำหรับการตรวจสอบสิทธิ์แบบหลายปัจจัย หากพนักงาน Twitter มีโทเค็นการรักษาความปลอดภัยฮาร์ดแวร์ U2F เช่น YubiKey ผู้โจมตีจะป้อนข้อมูลประจำตัวที่ขโมยมา จากนั้นจะได้รับแจ้งให้แตะคีย์จริงเพื่อขอสิทธิ์เข้าระบบ ซึ่งจะทำไม่ได้หากไม่มีคีย์ของพนักงาน

ในสถานการณ์จำลองนี้ บริษัทสามารถใช้ [Cloudflare Access](https://www.cloudflare.com/th-th/teams/access/) เพื่อล็อคการเข้าถึงระบบภายในของอุปกรณ์ของบริษัท และใช้นโยบายการเข้าถึงที่รัดกุมเพื่อจำกัดบัญชีที่ผู้ใช้แต่ละกลุ่มสามารถเข้าถึงได้ โดยสามารถนำนโยบายมาใช้เพื่อบังคับให้พนักงานตรวจสอบสิทธิ์ด้วยโทเค็นการรักษาความปลอดภัยของฮาร์ดแวร์ U2F และปิดกั้นเหตุการณ์ทั้งหมดที่ใช้ TOTP/SMS

ในปี 2018 การละเมิดข้อมูลได้ทำความเสียหายให้กับข้อมูลผู้ใช้ MyFitnessPal รวมถึงรหัสผ่าน อีกสองปีต่อมา มีการนำข้อมูลที่หลอกล่อมาได้นี้มาใช้ทำการโจมตีแบบ credential stuffing บริษัทประกันสองแห่ง ได้แก่ [Independence Blue Cross](https://www.prnewswire.com/news-releases/independence-blue-cross-provides-notice-of-a-privacy-incident-301087638.html) และ [AmeriHealth New Jersey](https://www.prnewswire.com/news-releases/amerihealth-hmo-inc-and-amerihealth-insurance-company-of-new-jersey-provides-notice-of-a-privacy-incident-301087643.html) การโจมตีแบบ credential stuffing ส่งผลให้มีการเข้าถึงข้อมูลการประกันของผู้ใช้โดยไม่ได้รับอนุญาต รวมถึงการเรียกร้องค่าสินไหมทดแทน ตัวอย่างนี้แสดงให้เห็นว่าบริษัทใดก็ตามสามารถตกเป็นเป้าหมายของกลยุทธ์การแอบอ้างเป็นเจ้าของบัญชีได้

โซลูชันบ็อตของ Cloudflare รวมถึง [Super Bot Fight Mode](https://blog.cloudflare.com/super-bot-fight-mode/) ซึ่งเปิดตัวในวันนี้อาจนำมาใช้ในหมู่บริษัทประกันภัยเพื่อปิดกั้น credential stuffing ในเชิงรุก สำหรับบริษัทประกันภัยที่กล่าวถึงอาจเปิดใช้งาน [Exposed Credential Checks in WAF](https://blog.cloudflare.com/account-takeover-protection/) เป็นการภายในเพื่อตรวจสอบรหัสผ่านของผู้ใช้ที่ถูกเจาะ ก่อนแจ้งให้ผู้ใช้รีบเปลี่ยนรหัสผ่าน

### การใช้ Cloudflare เพื่อรักษาความปลอดภัย Cloudflare

เวกเตอร์การแอบอ้างเป็นเจ้าของบัญชีทั่วไปจำนวนมากถูกปิดกั้นผ่านผลิตภัณฑ์ต่าง ๆ ของ Cloudflare ซึ่งช่วยให้ทีมรักษาความปลอดภัยมุ่งความสนใจไปที่การสร้างระบบป้องกันการโจมตีเฉพาะของ Cloudflare จากภายใน

ตัวอย่างเช่น [Cloudflare Gateway](https://www.cloudflare.com/th-th/teams/gateway/) ช่วยให้เราสามารถปิดกั้นโดเมนที่อาจเป็นอันตรายในเชิงรุกภายในตัวสร้างกฎ UI อย่างง่าย เมื่อปิดกั้นหมวดหมู่เหล่านี้บนปลายทางขององค์กร จะช่วยให้เราลดความเสี่ยงที่พนักงานจะพบกับภัยคุกคามที่รู้จัก

เมื่อมีโดเมนใหม่ที่ทีมรักษาความปลอดภัยสังเกตเห็นว่ากำลังพยายามโจมตีเพื่อรวบรวมข้อมูลประจำตัว เราสามารถปิดกั้นโดเมนในเชิงรุกได้โดยใช้รายการปิดกั้นใน Gateway ซึ่งจะป้องกันไม่ให้ปลายทางแก้ไขไซต์ได้แม้ว่าพนักงานจะนำทางไปยังไซต์นั้นโดยไม่ได้ตั้งใจ เครื่องมือรักษาความปลอดภัยมากมายสามารถใช้ที่อยู่ IP เพื่อปิดกั้น แต่นอกจากการปิดกั้น IP แล้ว เรายังสามารถปิดกั้นชื่อโดเมนเพื่อตอบสนองต่อการโจมตีให้ได้อย่างฉับไว เมื่อปิดกั้นโดเมนแล้ว หากผู้โจมตีใช้ไซต์เดียวกันบนที่อยู่ IP ใหม่ นั่นแสดงว่าเราได้บรรเทาความเสี่ยงที่อาจมีผู้เข้าไปซมไซต์ดังกล่าวแล้ว

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![img](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45MVRH4RPH04MXATTX5MHX.png&w=715&h=166&f=webp&fit=cover&position=center)

พนักงาน Cloudflare ทั้งหมดจะต้องใช้โทเค็นการรักษาความปลอดภัยของฮาร์ดแวร์ FIDO2 เป็นการภายในเพื่อตรวจสอบสิทธิ์กับทรัพยากรใด ๆ ของบริษัท ซึ่งจะช่วยปกป้องระบบภายในจากหลุมพรางต่าง ๆ ที่ทำให้การแอบอ้างเป็นเจ้าของบัญชีทำได้ง่ายขึ้น

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-403 Embedded Image - hXDAQM](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46BQE16882E9RXWBMQ97A9.png&w=715&h=104&f=webp&fit=cover&position=center)

นอกจากข้อกำหนดโทเค็นฮาร์ดแวร์แล้ว ทีมรักษาความปลอดภัยยังใช้ [Cloudflare Access](https://www.cloudflare.com/th-th/teams/access/) เพื่อกำหนดให้มีเพียง[อุปกรณ์ที่ได้รับการจัดการของบริษัท](https://blog.cloudflare.com/zero-trust-with-managed-devices/)เท่านั้นที่สามารถเชื่อมต่อกับระบบภายใน กฎที่มีการจัดการสามารถกำหนดค่าให้อนุญาตหรือปิดกั้นตามปัจจัยต่าง ๆ รวมกัน เช่น การใช้วิธีแบบหลายปัจจัยและภูมิศาสตร์ของที่อยู่ IP รวมกัน ทีมรักษาความปลอดภัยสามารถเปลี่ยนจากวิธีการเชิงรับเป็นเชิงรุกได้โดยการปิดกั้นเหตุการณ์การตรวจสอบสิทธิ์จากอุปกรณ์ที่ไม่ใช่ของบริษัท ประเทศที่เราไม่มีพนักงาน หรือกิจกรรมที่ใช้ SMS/TOTP แทนโทเค็นการรักษาความปลอดภัยฮาร์ดแวร์ U2F

### การเพิ่มเลเยอร์การป้องกันภายใน

นอกจากคุณสมบัติต่าง ๆ ของ Gateway แล้ว ทีมตรวจจับและตอบกลับยังส่งออกไฟล์บันทึก [Gateway](https://www.cloudflare.com/th-th/teams/gateway/) & [Access](https://www.cloudflare.com/th-th/teams/access/) เพื่อเพิ่มเติม เชื่อมโยง และพัฒนาการตรวจจับเหตุการณ์ดิบพร้อม ๆ กับไฟล์บันทึกระบบภายในอื่น ๆ ซึ่งเมื่อรวมไฟล์บันทึกทั้งหมดของเราไว้ในไปป์ไลน์ภายใน เราจะมีโอกาสสร้างการตรวจจับในแบบที่เรากำหนด และยกระดับให้การตอบสนองต่อเหตุการณ์เป็นระบบอัตโนมัติ

ในส่วนที่เกี่ยวข้องกับการแอบอ้างเป็นเจ้าของบัญชี ทีมงานของเรามุ่งเน้นไปที่การตรวจจับอาคารที่เน้นที่ [เทคนิคการเข้าถึงเบื้องต้น](https://attack.mitre.org/tactics/TA0001/)เป็นการป้องกันเลเยอร์ที่สองในบัญชีพนักงาน

ตัวอย่างบางส่วนของการตรวจจับที่เน้นการลดมาตรการความปลอดภัยของบัญชี ได้แก่

  * การเข้าสู่ระบบหรือเหตุการณ์การตรวจสอบสิทธิ์อื่น ๆ กับระบบภายในจาก VPN
  * การเปลี่ยนแปลงโทเค็นการตรวจสอบสิทธิ์แบบหลายปัจจัยของพนักงานและการใช้อุปกรณ์ใหม่
  * เหตุการณ์การเข้าสู่ระบบหรือการตรวจสอบสิทธิ์จากที่อยู่ IP ที่ไม่คุ้นเคย
  * เหตุการณ์การเข้าสู่ระบบหรือการตรวจสอบสิทธิ์จากที่อยู่ IP ในประเทศที่มีความเสี่ยงสูง
  * เหตุการณ์การตรวจสอบสิทธิ์ด้วยซอฟต์โทเค็นการตรวจสอบสิทธิ์แบบหลายปัจจัยกับระบบภายใน
  * เหตุการณ์ใด ๆ จากที่อยู่ IP ที่เกี่ยวข้องกับผู้คุกคามที่รู้จัก



อย่างไรก็ตาม ยังมีรูปแบบพฤติกรรมมากมายที่อาจบ่งบอกว่าบัญชีไม่ได้มาตรฐานความปลอดภัยเท่าที่ควร แทนการใช้กฎการตรวจจับแบบคงที่สำหรับกฎทั้งหมด ทีมตรวจจับและตอบกลับได้จัดลำดับความสำคัญของการสร้างโมเดลการเรียนรู้ของระบบที่ช่วยตรวจจับพฤติกรรมการตรวจสอบสิทธิ์ที่ผิดปกติภายในบัญชีของพนักงาน

สัญญาณความเสี่ยงคือรูปแบบที่_สามารถ_ระบุถึงพฤติกรรมที่เป็นอันตรายและนำมาใช้เพื่อกำหนดว่าพฤติกรรมนั้นน่าจะเป็นอันตรายอย่างแท้จริง ทุกบริษัทมีสัญญาณความเสี่ยงด้านความปลอดภัยบางสัญญาณที่เหมือนกันเพื่อตรวจจับบัญชีที่มีมาตรฐานความปลอดภัยลดลง อย่างไรก็ตาม สัญญาณดังกล่าวอาจแตกต่างกันมากขึ้นอยู่กับโครงสร้างพื้นฐาน การรวมผลิตภัณฑ์ความปลอดภัยของ Cloudflare เข้ากับงานวิศวกรรมของเราเองจะช่วยให้เรามีระบบป้องกันที่ราบรื่นสำหรับระบบเผชิญหน้าทั้งภายนอกและภายใน

### อิทธิพลต่อแผนกลยุทธ์สำหรับผลิตภัณฑ์

เมื่อ Cloudflare ขยายชุดผลิตภัณฑ์ด้านความปลอดภัย ทีมความปลอดภัยโดยรวมทำงานอย่างใกล้ชิดเพื่อการมีบทบาทที่สำคัญต่อแผนกลยุทธ์สำหรับผลิตภัณฑ์ เราสามารถให้ข้อมูลเชิงลึกที่นำไปใช้ได้จริงในการควบคุมและการตรวจจับทั้งหมดที่จำเป็นต่อการบรรเทาและตอบสนองต่อการโจมตีทางไซเบอร์ในปัจจุบันได้อย่างมีประสิทธิภาพ เราเปิดเผยกลยุทธ์ภายในร่วมกับทีมผลิตภัณฑ์โดยใช้ลูปการตอบรับที่ได้จากการสื่อสารและการทำงานร่วมกัน จากนั้นลองใช้ผลิตภัณฑ์ที่สร้างขึ้นที่ Cloudflare เพื่อให้แน่ใจว่าผลิตภัณฑ์ดังกล่าวปกป้องข้อมูลพนักงานและลูกค้าของเราได้จริง

Cloudflare เป็นสถานที่ที่ยินดีต้อนรับและอภิปรายแนวคิดใหม่ ๆ เพื่อให้แน่ใจว่าผลิตภัณฑ์ของเราเป็นทรัพย์สินสำหรับทีมความปลอดภัยและไอทีที่กำลังใช้งานผลิตภัณฑ์ดังกล่าว การได้เป็นส่วนหนึ่งของการเดินทางครั้งนั้นคือกำลังใจที่สำคัญ!

### ขั้นตอนถัดไป

การแอบอ้างเป็นเจ้าของบัญชีเป็นหนึ่งในการโจมตีการรักษาความปลอดภัยทางไซเบอร์ที่พบบ่อยที่สุด แต่คุณสามารถปรับปรุงความสมบูรณ์ของโปรแกรมความปลอดภัยของคุณได้อย่างรวดเร็วด้วยการวางมาตรการบรรเทาผลกระทบที่โฟกัสที่การเข้าถึงครั้งแรก การบรรเทาผลกระทบเหล่านี้จะหยุดผู้โจมตีที่ขั้นตอน "การลาดตระเวน" ของเชนการกำจัดทางไซเบอร์ ซึ่งเป็นรูปแบบขั้นตอนการโจมตีที่สร้างโดย Lockheed Martin และขยายผ่าน[โครงงาน MITRE ATT&CK](https://attack.mitre.org/tactics/enterprise/)

แล้วกลยุทธ์ใดดีที่สุดที่คุณสามารถนำมาใช้เพื่อปกป้องความปลอดภัยขององค์กรของคุณ

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-403 Embedded Image - AswhIQ](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45Q6Z6ACKAHV0QPTJCSMJG.png&w=715&h=1019&f=webp&fit=cover&position=center)

 _ทำให้การโจมตีด้วยการแอบอ้างเป็นเจ้าของบัญชีทำได้ยาก_

ที่ Cloudflare เราบังคับใช้นโยบายความปลอดภัยที่เน้นที่ความปลอดภัยของบัญชี ซึ่งรวมถึงการบังคับใช้โทเค็นความปลอดภัยของฮาร์ดแวร์สำหรับการตรวจสอบสิทธิ์แบบหลายปัจจัย ความซับซ้อนของรหัสผ่านที่รัดกุม การปิดกั้นเชิงรุกสำหรับโดเมนที่ไม่ดีที่รู้จัก และการป้องกันบ็อตบนไซต์ที่เชื่อมต่อภายนอก การบรรเทาผลกระทบเหล่านี้แต่ละอย่างมีจุดมุ่งหมายเพื่อขัดขวางช่วงเริ่มต้นของขั้นตอนการโจมตี (Kill Chain) ของผู้โจมตี

ในหน้านี้

สนทนาออนไลน์

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Faccount-compromise-security-overview%2F&t=%E0%B8%A0%E0%B8%B2%E0%B8%A2%E0%B9%83%E0%B8%99%20Cloudflare%3A%20%E0%B8%9B%E0%B9%89%E0%B8%AD%E0%B8%87%E0%B8%81%E0%B8%B1%E0%B8%99%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%81%E0%B8%AD%E0%B8%9A%E0%B8%AD%E0%B9%89%E0%B8%B2%E0%B8%87%E0%B9%80%E0%B8%9B%E0%B9%87%E0%B8%99%E0%B9%80%E0%B8%88%E0%B9%89%E0%B8%B2%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B8%9A%E0%B8%B1%E0%B8%8D%E0%B8%8A%E0%B8%B5)[](https://x.com/intent/post?text=%E0%B8%A0%E0%B8%B2%E0%B8%A2%E0%B9%83%E0%B8%99+Cloudflare%3A+%E0%B8%9B%E0%B9%89%E0%B8%AD%E0%B8%87%E0%B8%81%E0%B8%B1%E0%B8%99%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%81%E0%B8%AD%E0%B8%9A%E0%B8%AD%E0%B9%89%E0%B8%B2%E0%B8%87%E0%B9%80%E0%B8%9B%E0%B9%87%E0%B8%99%E0%B9%80%E0%B8%88%E0%B9%89%E0%B8%B2%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B8%9A%E0%B8%B1%E0%B8%8D%E0%B8%8A%E0%B8%B5&url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Faccount-compromise-security-overview%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Faccount-compromise-security-overview%2F)[](https://bsky.app/intent/compose?text=%E0%B8%A0%E0%B8%B2%E0%B8%A2%E0%B9%83%E0%B8%99+Cloudflare%3A+%E0%B8%9B%E0%B9%89%E0%B8%AD%E0%B8%87%E0%B8%81%E0%B8%B1%E0%B8%99%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%81%E0%B8%AD%E0%B8%9A%E0%B8%AD%E0%B9%89%E0%B8%B2%E0%B8%87%E0%B9%80%E0%B8%9B%E0%B9%87%E0%B8%99%E0%B9%80%E0%B8%88%E0%B9%89%E0%B8%B2%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B8%9A%E0%B8%B1%E0%B8%8D%E0%B8%8A%E0%B8%B5+https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Faccount-compromise-security-overview%2F)[](https://mastodonshare.com/?text=%E0%B8%A0%E0%B8%B2%E0%B8%A2%E0%B9%83%E0%B8%99+Cloudflare%3A+%E0%B8%9B%E0%B9%89%E0%B8%AD%E0%B8%87%E0%B8%81%E0%B8%B1%E0%B8%99%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%81%E0%B8%AD%E0%B8%9A%E0%B8%AD%E0%B9%89%E0%B8%B2%E0%B8%87%E0%B9%80%E0%B8%9B%E0%B9%87%E0%B8%99%E0%B9%80%E0%B8%88%E0%B9%89%E0%B8%B2%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B8%9A%E0%B8%B1%E0%B8%8D%E0%B8%8A%E0%B8%B5&url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Faccount-compromise-security-overview%2F)[](https://www.threads.net/intent/post?text=%E0%B8%A0%E0%B8%B2%E0%B8%A2%E0%B9%83%E0%B8%99+Cloudflare%3A+%E0%B8%9B%E0%B9%89%E0%B8%AD%E0%B8%87%E0%B8%81%E0%B8%B1%E0%B8%99%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%81%E0%B8%AD%E0%B8%9A%E0%B8%AD%E0%B9%89%E0%B8%B2%E0%B8%87%E0%B9%80%E0%B8%9B%E0%B9%87%E0%B8%99%E0%B9%80%E0%B8%88%E0%B9%89%E0%B8%B2%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B8%9A%E0%B8%B1%E0%B8%8D%E0%B8%8A%E0%B8%B5+https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Faccount-compromise-security-overview%2F)

## แท็กที่เกี่ยวข้อง

[Cloudflare Access](https://blog.cloudflare.com/th-th/tag/cloudflare-access/)[Cloudflare Gateway](https://blog.cloudflare.com/th-th/tag/gateway/)[Security Week](https://blog.cloudflare.com/th-th/tag/security-week/)[ความปลอดภัย](https://blog.cloudflare.com/th-th/tag/security/)

ติดตามบนโซเชียลมีเดีย

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## สมัครรับการแจ้งเตือนโพสต์ใหม่

อีเมล

เราจะไม่เปิดเผยอีเมลของคุณ

สมัคร

ขอบคุณที่สมัครรับข่าวสาร! โปรดตรวจสอบกล่องจดหมายเพื่อยืนยัน
