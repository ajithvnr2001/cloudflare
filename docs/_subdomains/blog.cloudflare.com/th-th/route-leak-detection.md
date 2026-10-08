---
url: https://blog.cloudflare.com/th-th/route-leak-detection/
title: \u0e1b\u0e01\u0e1b\u0e49\u0e2d\u0e07\u0e25\u0e39\u0e01\u0e04\u0e49\u0e32 Cloudflare \u0e08\u0e32\u0e01\u0e04\u0e27\u0e32\u0e21\u0e44\u0e21\u0e48\u0e1b\u0e25\u0e2d\u0e14\u0e20\u0e31\u0e22\u0e02\u0e2d\u0e07 BGP \u0e14\u0e49\u0e27\u0e22\u0e01\u0e32\u0e23\u0e15\u0e23\u0e27\u0e08\u0e08\u0e31\u0e1a\u0e01\u0e32\u0e23\u0e23\u0e31\u0e48\u0e27\u0e44\u0e2b\u0e25\u0e02\u0e2d\u0e07\u0e40\u0e2a\u0e49\u0e19\u0e17\u0e32\u0e07 | \u0e1a\u0e25\u0e47\u0e2d\u0e01 Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:51:05.046957+00:00
---

# ปกป้องลูกค้า Cloudflare จากความไม่ปลอดภัยของ BGP ด้วยการตรวจจับการรั่วไหลของเส้นทาง | บล็อก Cloudflare

> Source: https://blog.cloudflare.com/th-th/route-leak-detection/

[บล็อก](https://blog.cloudflare.com/th-th/)

[BGP](https://blog.cloudflare.com/th-th/tag/bgp/)[RPKI](https://blog.cloudflare.com/th-th/tag/rpki/)[Security Week](https://blog.cloudflare.com/th-th/tag/security-week/)+1แสดงแท็กเพิ่มเติม 1 รายการ

4 แท็กแสดง 4 แท็ก

  * แท็กของโพสต์
  * [Security Week](https://blog.cloudflare.com/th-th/tag/security-week/)[ความปลอดภัย](https://blog.cloudflare.com/th-th/tag/security/)
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

[BGP](https://blog.cloudflare.com/th-th/tag/bgp/)[RPKI](https://blog.cloudflare.com/th-th/tag/rpki/)[Security Week](https://blog.cloudflare.com/th-th/tag/security-week/)[ความปลอดภัย](https://blog.cloudflare.com/th-th/tag/security/)

25 มีนาคม 2564

# ปกป้องลูกค้า Cloudflare จากความไม่ปลอดภัยของ BGP ด้วยการตรวจจับการรั่วไหลของเส้นทาง

![David Tuber](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47E8A7R1CB3C4YH862R2QY.png&w=64&h=64&f=webp&fit=cover&position=center)

[David Tuber](https://blog.cloudflare.com/th-th/author/tubes/)

อ่าน 2 นาที

คัดลอก URL

โพสต์นี้มีให้อ่านใน [English](https://blog.cloudflare.com/route-leak-detection/) [日本語](https://blog.cloudflare.com/ja-jp/route-leak-detection/) และ[Bahasa Indonesia](https://blog.cloudflare.com/id-id/route-leak-detection/).

![Protecting Cloudflare Customers from BGP Insecurity with Route Leak Detection](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45A6QSW66D06DRH2K9XW0W.png&w=1852&h=926&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////+vr87u7v5+bn6+nq8O/w7+/w6Ojq/////f3+8fDw6+jn7uvp8/Hv8vHx6+vt////////9vXz8Ozo8u7q9/Tx9vX08PDx/////////Pv59vLt+PPu/fn1/Pr59vb3/////////////fn2//v3///9////+/v9////////////////////////////////////////////////////////////////////////////////////////////////)

Border Gateway Protocol (BGP) การรั่วไหลของเส้นทางและการเข้ายึดเส้นทางสามารถทำลายการทำงานของคุณได้ ทั้งนี้ BGP [ไม่มีความปลอดภัย ซึ่งเป็นผลจากการออกแบบของมันเอง](https://blog.cloudflare.com/is-bgp-safe-yet-rpki-routing-security-initiative/) และข้อมูลการกำหนดเส้นทางที่ไม่ถูกต้องที่แพร่กระจายไปทั่วอินเทอร์เน็ตสามารถสร้างความชะงักงันและเป็นอันตรายต่อการทำงานปกติของเครือข่ายลูกค้าและอินเทอร์เน็ตโดยรวมได้อย่างเหลือเชื่อ วันนี้เรารู้สึกตื่นเต้นที่จะประกาศคุณสมับัติ Route Leak Detection ซึ่งเป็นคุณสมบัติการแจ้งเตือนเครือข่ายใหม่ที่จะแจ้งให้ลูกค้าทราบเมื่อ prefix ที่พวกเขาเป็นเจ้าของซึ่งอยู่บน Cloudflare นั้นมีการรั่วไหล เช่น มีการโฆษณาเส้นทางโดยบุคคลที่ไม่ได้รับอนุญาต ทั้งนี้ Route Leak Detection จะช่วยปกป้องเส้นทางของคุณบนอินเทอร์เน็ต โดยจะแจ้งให้คุณทราบเมื่อการรับส่งข้อมูลของคุณกำลังไปอยู่ในที่ที่ไม่ควรไป ซึ่งเป็นสัญญาณบ่งชี้การโจมตีที่อาจเกิดขึ้น และลดเวลาในการบรรเทาผลกระทบจากการรั่วไหลโดยให้ข้อมูลที่ทันท่วงทีแก่คุณ

ในบล็อกนี้ เราจะอธิบายว่าการรั่วไหลของเส้นทางคืออะไร, Cloudflare Route Leak Detection ทำงานอย่างไร และเราจะทำอะไรบ้างเพื่อช่วยปกป้องอินเทอร์เน็ตจากการรั่วไหลของเส้นทาง

## การรั่วไหลของเส้นทางคืออะไรและทำไมฉันจึงควรสนใจ

การรั่วไหลของเส้นทางเกิดขึ้นเมื่อเครือข่ายบนอินเทอร์เน็ตบอกให้โลกส่วนอื่นๆ กำหนดเส้นทางการรับส่งข้อมูลผ่านเครือข่ายของพวกเขาทั้ง ๆ ที่ไม่ควรผ่านไปในเส้นทางนั้น [ตัวอย่างที่สำคัญตัวอย่างหนึ่ง](https://blog.cloudflare.com/how-verizon-and-a-bgp-optimizer-knocked-large-parts-of-the-internet-offline-today/)ของกรณีนี้และผลกระทบที่เกิดขึ้น คือเหตุการณ์ในเดือนมิถุนายน 2019 ที่ ISP ขนาดเล็กในเพนซิลเวเนียเริ่มการโฆษณาเส้นทางสำหรับส่วนหนึ่งของอินเทอร์เน็ตที่รวมถึง Cloudflare, Amazon และ Linode การรับส่งข้อมูลที่กำหนดให้ส่งไปที่เครือข่ายเหล่านั้นจำนวนมากอย่างมีนัยสำคัญถูกเปลี่ยนเส้นทางไปยังเครือข่ายนั้นอย่างไม่ถูกต้อง ทำให้ prefix ของ Cloudflare, Amazon และ Linode รั่วไหล และทำให้เกิดความแออัดและผู้ใช้ปลายทางไม่สามารถเข้าถึงเครือข่ายได้ การรั่วไหลของเส้นทางมักจะเกิดขึ้นเนื่องจาก peering session หรือเราเตอร์ของลูกค้ามีการกำหนดค่าไม่ถูกต้อง บักของซอฟต์แวร์ในเราเตอร์ของลูกค้าหรือบุคคลที่สาม การโจมตีแบบ Man-in-the-Middle หรือลูกค้าหรือบุคคลที่สามที่เป็นอันตราย

การรั่วไหลของเส้นทางบางเส้นทางไม่เป็นอันตราย แต่การรั่วไหลของเส้นทางบางส่วนอาจเป็นอันตราย และส่งผลกระทบด้านความปลอดภัยอย่างแท้จริง ผู้โจมตีสามารถโฆษณาเส้นทางเฉพาะภายใต้จุดประสงค์เฉพาะ เพื่อนำผู้ใช้ไปยังเครือข่ายเพื่อทำสิ่งต่าง ๆ เช่น [ขโมยเงินคริปโต](https://blog.cloudflare.com/bgp-leaks-and-crypto-currencies/) และข้อมูลสำคัญอื่น ๆ หรือพยายามออกใบรับรอง SSL /TLS ที่สามารถใช้เพื่อปลอมโดเมน ซึ่งเมื่อมีการโฆษณาเส้นทางที่เฉพาะเจาะจงมากขึ้น ผู้โจมตีจะสามารถหลอกให้คุณเข้าถึงเว็บไซต์ที่คุณไม่ได้ตั้งใจจะเข้าได้ และถ้าเว็บไซต์ดังกล่าวมีหน้าตาเหมือนกับที่คุณคาดหวังไว้ คุณก็อาจป้อนข้อมูลส่วนบุคคลโดยไม่ตั้งใจและเสี่ยงต่อการถูกโจมตี นี่คือแผนภาพแสดงการรับส่งข้อมูลที่ตลอดเส้นทางไม่มีการรั่วไหล:

และนี่คือการรับส่งข้อมูลหลังจากเส้นทางรั่วไหล:

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Here’s a diagram representing traffic without a route leak](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46ZC0B3XDZ5D7FTXPB4NHQ.png&w=715&h=374&f=webp&fit=cover&position=center)

ดังนั้นนอกจากจะทำให้ผู้ใช้ไม่พอใจเนื่องจากมีปริมาณการใช้อินเทอร์เน็ตจำนวนมากกำลังผ่านเส้นทางที่ไม่สามารถจัดการได้ การรั่วไหลของเส้นทางอาจมีนัยยะถึงการรั่วไหลของข้อมูลที่แท้จริงอีกด้วย

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![And here’s traffic after a route leak](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44EW74YA2BQ6YG3RX68QGN.png&w=715&h=374&f=webp&fit=cover&position=center)

การตรวจจับการรั่วไหลของเส้นทางของ Cloudflare ช่วยให้คุณได้รับการแจ้งเตือนอย่างรวดเร็วเมื่อเส้นทางของคุณรั่ว คุณจะได้ทราบเมื่ออาจมีการโจมตีเกิดขึ้น

## Cloudflare Route Leak Detection ปกป้องเครือข่ายของฉันได้อย่างไร

### วิธีกำหนดค่า Route Leak Detection

หากต้องการกำหนดค่า Route Leak Detection คุณต้องเป็นลูกค้า Cloudflare ที่มีที่อยู่[“ IP ของคุณเอง” (BYOIP)](https://developers.cloudflare.com/byoip/) ซึ่งรวมถึงลูกค้า Magic Transit (L3), Spectrum (L4) และ WAF (L7) เฉพาะ prefix ที่โฆษณาโดย Cloudflare เท่านั้นที่เข้าเกณฑ์สำหรับคุณสมบัติ Route Leak Detection

การกำหนดค่า Route Leak Detection อาจทำได้ด้วยการตั้งค่าข้อความในแท็บการแจ้งเตือนในบัญชีของคุณ

Cloudflare จะเริ่มควบคุม prefix ออนบอร์ดทั้งหมดของคุณเพื่อตรวจสอบการรั่วไหลและการเข้ายึดเส้นทาง ก่อนส่งการแจ้งเตือนคุณทาง[อีเมลหรือเครื่องมือการโทร เช่น PagerDuty](https://support.cloudflare.com/hc/en-us/articles/360047358211-Connecting-PagerDuty-to-Cloudflare) เมื่อเกิดเหตุการณ์ดังกล่าวขึ้น

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Configuring Route Leak Detection can be done by setting up a message in the Notifications tab in your account.](https://blog.cloudflare.com/_emdash/api/media/file/01KW499YT8E6BES1Y1GT8MVJDM.gif)

ระบบประกาศการแจ้งเตือนของ Cloudflare รองรับเว็บฮุค อีเมล และ PagerDuty ดังนั้นทีมของคุณจะได้รับการอัปเดตผ่านทางสื่อที่ต้องการเมื่อมีการเปลี่ยนแปลงเส้นทางเครือข่าย และเพื่อให้มีการตอบกลับและดำเนินการแก้ไขเมื่อจำเป็น

### ตัวอย่างสถานการณ์การโจมตี

บุคคลที่เป็นอันตรายที่พยายามใช้เส้นทางเพื่อเข้าถึงข้อมูลลูกค้าเริ่มโฆษณาซับเน็ตของ prefix ที่ประกาศโฆษณาสำหรับลูกค้า Magic Transit รายหนึ่งของเรา หากไม่พบการโจมตีนี้และแก้ไขให้ได้โดยเร็ว ก็อาจส่งผลกระทบร้ายแรงต่อลูกค้าได้ เมื่อผู้โจมตีเริ่มประกาศโฆษณา prefix โดยที่ลูกค้าไม่ทราบ การอัปเดต BGP และการเปลี่ยนแปลงเส้นทางจะเริ่มขึ้นอย่างรวดเร็วในตารางเส้นทางทั่วโลก ซึ่งโดยปกติคือภายใน 60 วินาที

มาดูกันว่าลูกค้าจะปรับใช้ Route Leak Detection ได้อย่างไร ลูกค้า Acme Corp เป็นเจ้าของ prefix ของ IP 203.0.113.0/24 โดย Acme ได้ออนบอร์ด 203.0.113.0/24 ไปที่ Cloudflare และ Cloudflare จะบอกกับส่วนที่เหลือในโลกอินเทอร์เน็ตว่า prefix นี้สามารถเข้าถึงได้ผ่านเครือข่ายของ Cloudflare

เมื่อ Acme เปิดใช้งานคุณสมบัติ Route Leak Detection แล้ว Cloudflare จะตรวจสอบข้อมูลเส้นทางบนอินเทอร์เน็ตสำหรับ 203.0.113.0/24 อย่างต่อเนื่อง โดยมีเป้าหมายเพื่อตรวจจับการรั่วไหลภายในห้านาทีของข้อมูลการกำหนดเส้นทางที่ผิดพลาดที่เผยแพร่บนอินเทอร์เน็ต

กลับไปที่สถานการณ์การโจมตี บุคคลที่ประสงค์ร้ายที่พยายามโจมตีเครือข่ายของ Acme ปลอมแปลงประกาศโฆษณาสำหรับไอพี 203.0.113.0/24 พร้อมเปลี่ยนเส้นทางของผู้ใช้ที่ถูกต้องจากเส้นทางเครือข่ายที่ตั้งใจไว้ไปยัง Acme (ผ่านเครือข่ายของ Cloudflare) และไปยังเครื่องโทรสารของเครือข่ายของ Acme ที่ตั้งใจแทนเพื่อบันทึกข้อมูลจากผู้ใช้ที่ไม่ได้ตั้งใจ

เนื่องจาก Acme ได้เปิดใช้งาน Route Leak Detection การแจ้งเตือนจะถูกส่งไปยังผู้ดูแลระบบของ Acme

การแจ้งเตือนนี้รวม ASN ทั้งหมดที่เห็น prefix ที่กำลังโฆษณาโดยบุคคลที่มีแนวโน้มว่าจะเป็นอันตราย Acme สามารถเตือนผู้ใช้ว่าพวกเขาอาจเสี่ยงต่อการถูกโจมตีด้วยการขโมยข้อมูล และควรระมัดระวังพฤติกรรมที่น่าสงสัย

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Because Acme has enabled Route Leak Detection, an alert is sent to Acme’s administrators.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46P9FYXK95HSTCP2SZKRZG.png&w=715&h=798&f=webp&fit=cover&position=center)

Acme ยังสามารถติดต่อผู้ให้บริการที่ระบุไว้ในการแจ้งเตือนได้อย่างรวดเร็วเพื่อหยุดยั้งไม่ให้มีการใช้เส้นทางที่เล็กกว่า โดยปัจจุบัน กระบวนการบรรเทาผลกระทบจากการรั่วไหลของเส้นทางเป็นกระบวนการที่ต้องดำเนินการด้วยตนเองอย่างมาก โดยต้องติดต่อผู้ให้บริการโดยตรงผ่านทางข้อมูลติดต่อที่เผยแพร่ใน[ฐานข้อมูลสาธารณะ](https://www.peeringdb.com/) ส่วนในอนาคต เราวางแผนที่จะสร้างคุณสมบัติเพื่อทำให้กระบวนการขยายงานและบรรเทาผลกระทบนี้เป็นไปโดยอัตโนมัติ เพื่อลดเวลาการหยุดทำงานเพื่อบรรเทาเหตุการณ์การรั่วไหลของเส้นทางที่อาจส่งผลกระทบต่อลูกค้าของเรา

## Cloudflare ตรวจจับการรั่วไหลของเส้นทางได้อย่างไร

Cloudflare ใช้แหล่งข้อมูลการกำหนดเส้นทางหลายแห่งเพื่อสังเคราะห์วิธีที่อินเทอร์เน็ตเห็นเส้นทางไปยังลูกค้า BYOIP ของเรา Cloudflare เฝ้าดูมุมมองเหล่านี้เพื่อติดตามการเปลี่ยนแปลงที่เกิดขึ้นบนอินเทอร์เน็ตอย่างกะทันหัน หากเราสามารถเชื่อมโยงการเปลี่ยนแปลงเหล่านั้นกับสิ่งที่เราทำ แสดงว่าการเปลี่ยนแปลงนั้นไม่เป็นอันตรายและเป็นการดำเนินธุรกิจตามปกติ แต่ถ้าเราไม่ได้ทำการเปลี่ยนแปลงใด ๆ เราจะรีบดำเนินการเพื่อแจ้งให้คุณทราบว่าเส้นทางและผู้ใช้ของคุณอาจมีความเสี่ยง

### ไปป์ไลน์การบริโภคข้อมูลจากด้านนอกสู่ด้านในของ Cloudflare

แหล่งข้อมูลหลักของ Cloudflare มาจากที่เก็บที่ได้รับการดูแลจากภายนอก เช่น [ฟีด RIS ของ RIPE](https://ris-live.ripe.net/), [RouteViews](http://www.routeviews.org/), และ [ฟีด BMP สาธารณะของ Caida](https://bgpstream.caida.org/data#!caida-bmp) จึงต้องใช้มุมมองภายนอกหลายมุมมองของตารางเส้นทางอินเทอร์เน็ตเพื่อให้ถูกต้องที่สุดเมื่อทำการอนุมานเกี่ยวกับสถานะของอินเทอร์เน็ต Cloudflare เรียกใช้ API ไปยังแหล่งที่มาเหล่านั้นเพื่อบริโภคข้อมูลและวิเคราะห์การเปลี่ยนแปลงในเส้นทาง BGP ฟีดเหล่านี้ช่วยให้เราบริโภคข้อมูลการกำหนดเส้นทางสำหรับอินเทอร์เน็ตทั้งหมด Cloudflare จะกรองข้อมูลทั้งหมดลงไปตาม prefix ที่คุณเคยออนบอร์ดไปที่ Cloudflare

เมื่อข้อมูลนี้ถูกบริโภคและกรองแล้ว Cloudflare จะเริ่มอัปเดตการอ้างอิงไขว้ไปยังตารางการกำหนดเส้นทางทั่วโลกด้วยตัวชี้วัดที่ระบุว่าอาจมีการเข้ายึดเส้นทาง เช่น จำนวนของ ASN ที่เห็นเส้นทางของคุณโดยตรง จำนวนการอัปเดต BGP ที่เกิดขึ้นในช่วงเวลาสั้น ๆ และจำนวนซับเน็ตที่กำลังโฆษณา หากจำนวน ASN ที่เห็นเส้นทางของคุณโดยตรงหรือจำนวนการอัปเดตเปลี่ยนแปลงอย่างผิดสังเกต อาจหมายความว่า prefix ของคุณรั่วไหล หากพบเห็นการเปลี่ยนแปลงจำนวนมากในตารางการกำหนดเส้นทางทั่วโลก ในซับเน็ตของ prefix ที่คุณกำลังประกาศโฆษณา อาจเป็นไปได้ว่า prefix ของคุณรั่วไหลไปที่ใดที่หนึ่ง

Cloudflare ได้กำหนดค่านี้ใน prefix ของเราเองแล้ววันนี้ ต่อไปนี้คือตัวอย่างสิ่งที่เราเห็นเมื่อระบบตัดสินว่ามีบางอย่างผิดปกติ:

Cloudflare เป็นเจ้าของช่วง prefix 2606:4700:50::/44 เนื่องจากช่วงดังกล่าวเป็นซับเน็ตของช่วงใดช่วงหนึ่ง[ที่แสดงอยู่บนเว็บไซต์ของเราที่นี่](https://www.cloudflare.com/th-th/ips/) เราสังเกตตลอดหนึ่งชั่วโมงว่ามีคนพยายามโฆษณาเครือข่ายย่อยในช่วงนั้นไปยังเครือข่ายอื่นอีก 38 เครือข่าย แต่โชคดีเพราะเรา[นำ RPKI มาใช้](https://blog.cloudflare.com/rpki-details/) เรารู้ว่าเครือข่ายส่วนใหญ่จะปฏิเสธแทนที่จะยอมรับโฆษณาเส้นทางเหล่านี้จากผู้โจมตี

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare already has this configured on our own prefixes today. Here’s an example of what we see when our system determines that something is wrong:](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW462F218HHM4DVGF38GBY83.png&w=715&h=142&f=webp&fit=cover&position=center)

## ฉันจะทำอย่างไรเพื่อป้องกันการรั่วไหลของเส้นทางในอนาคต

วิธีที่ดีที่สุดในการป้องกันการรั่วไหลของเส้นทางคือการปรับใช้ [RPKI](https://blog.cloudflare.com/rpki-details/) ในเครือข่ายของคุณและกระตุ้นให้ผู้ให้บริการอินเทอร์เน็ตของคุณทำเช่นนั้นด้วย ทั้งนี้ RPKI จะช่วยให้คุณและผู้ให้บริการลงนามในเส้นทางที่คุณโฆษณาบนอินเทอร์เน็ต เพื่อไม่ให้ผู้อื่นขโมยเส้นทางได้ หากมีผู้โฆษณาเส้นทาง RPKI ของคุณ ผู้ให้บริการใด ๆ ที่สนับสนุน RPKI จะไม่ส่งต่อเส้นทางเหล่านั้นไปยังลูกค้ารายอื่น เพื่อจำกัดความพยายามที่จะทำให้เส้นทางรั่วไหลให้อยู่ใกล้กับผู้โจมตีให้มากที่สุด

การสนับสนุนอย่างต่อเนื่องของ Cloudflare [สำหรับ](https://isbgpsafeyet.com/) RPKI ส่งผลสัมฤทธิ์ตลอดช่วงสามเดือนที่ผ่านมา โดยผู้ให้บริการเช่น Amazon, Google, Telstra, Cogent และแม้แต่ Netflix ได้เริ่มสนับสนุน RPKI พร้อมกับกรองและลบ prefix ที่ไม่ถูกต้อง ซึ่งในความเป็นจริงแล้ว ผู้ให้บริการอินเทอร์เน็ตชั้นนำกว่า 50% ในตอนนี้ได้สนับสนุน RPKI ในรูปแบบใดรูปแบบหนึ่ง:

คุณสมบัติ Route Leak Detection ของ Cloudflare เมื่อนำมาใช้ร่วมกันในหมู่ผู้ให้บริการจำนวนมากที่ใช้ RPKI ช่วยให้แน่ใจว่าการสูญหายของข้อมูลและการหยุดทำงานที่มีสาเหตุจากการรั่วไหลของเส้นทางได้ยุติลงแล้ว หากคุณเป็นลูกค้า Cloudflare Magic Transit หรือ BYOIP ลองกำหนดค่าการแจ้งเตือนการรั่วไหลของเส้นทางใน dash วันนี้ หากคุณไม่ใช่ลูกค้า Magic Transit หรือ BYOIP โปรดติดต่อ[ทีมขาย](https://www.cloudflare.com/th-th/plans/enterprise/contact/)ของเราเพื่อเริ่มต้นกระบวนการเพื่อให้เครือข่าย หรือแม้กระทั่งเส้นทางต่าง ๆ ของคุณปลอดภัย

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![In fact, over 50% of the top Internet providers now support RPKI in some fashion:](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45RAWTD6NJGMZ17CKQJFQA.png&w=715&h=988&f=webp&fit=cover&position=center)

ในหน้านี้

สนทนาออนไลน์

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Froute-leak-detection%2F&t=%E0%B8%9B%E0%B8%81%E0%B8%9B%E0%B9%89%E0%B8%AD%E0%B8%87%E0%B8%A5%E0%B8%B9%E0%B8%81%E0%B8%84%E0%B9%89%E0%B8%B2%20Cloudflare%20%E0%B8%88%E0%B8%B2%E0%B8%81%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B9%84%E0%B8%A1%E0%B9%88%E0%B8%9B%E0%B8%A5%E0%B8%AD%E0%B8%94%E0%B8%A0%E0%B8%B1%E0%B8%A2%E0%B8%82%E0%B8%AD%E0%B8%87%20BGP%20%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%95%E0%B8%A3%E0%B8%A7%E0%B8%88%E0%B8%88%E0%B8%B1%E0%B8%9A%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%A3%E0%B8%B1%E0%B9%88%E0%B8%A7%E0%B9%84%E0%B8%AB%E0%B8%A5%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B9%80%E0%B8%AA%E0%B9%89%E0%B8%99%E0%B8%97%E0%B8%B2%E0%B8%87)[](https://x.com/intent/post?text=%E0%B8%9B%E0%B8%81%E0%B8%9B%E0%B9%89%E0%B8%AD%E0%B8%87%E0%B8%A5%E0%B8%B9%E0%B8%81%E0%B8%84%E0%B9%89%E0%B8%B2+Cloudflare+%E0%B8%88%E0%B8%B2%E0%B8%81%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B9%84%E0%B8%A1%E0%B9%88%E0%B8%9B%E0%B8%A5%E0%B8%AD%E0%B8%94%E0%B8%A0%E0%B8%B1%E0%B8%A2%E0%B8%82%E0%B8%AD%E0%B8%87+BGP+%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%95%E0%B8%A3%E0%B8%A7%E0%B8%88%E0%B8%88%E0%B8%B1%E0%B8%9A%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%A3%E0%B8%B1%E0%B9%88%E0%B8%A7%E0%B9%84%E0%B8%AB%E0%B8%A5%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B9%80%E0%B8%AA%E0%B9%89%E0%B8%99%E0%B8%97%E0%B8%B2%E0%B8%87&url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Froute-leak-detection%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Froute-leak-detection%2F)[](https://bsky.app/intent/compose?text=%E0%B8%9B%E0%B8%81%E0%B8%9B%E0%B9%89%E0%B8%AD%E0%B8%87%E0%B8%A5%E0%B8%B9%E0%B8%81%E0%B8%84%E0%B9%89%E0%B8%B2+Cloudflare+%E0%B8%88%E0%B8%B2%E0%B8%81%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B9%84%E0%B8%A1%E0%B9%88%E0%B8%9B%E0%B8%A5%E0%B8%AD%E0%B8%94%E0%B8%A0%E0%B8%B1%E0%B8%A2%E0%B8%82%E0%B8%AD%E0%B8%87+BGP+%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%95%E0%B8%A3%E0%B8%A7%E0%B8%88%E0%B8%88%E0%B8%B1%E0%B8%9A%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%A3%E0%B8%B1%E0%B9%88%E0%B8%A7%E0%B9%84%E0%B8%AB%E0%B8%A5%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B9%80%E0%B8%AA%E0%B9%89%E0%B8%99%E0%B8%97%E0%B8%B2%E0%B8%87+https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Froute-leak-detection%2F)[](https://mastodonshare.com/?text=%E0%B8%9B%E0%B8%81%E0%B8%9B%E0%B9%89%E0%B8%AD%E0%B8%87%E0%B8%A5%E0%B8%B9%E0%B8%81%E0%B8%84%E0%B9%89%E0%B8%B2+Cloudflare+%E0%B8%88%E0%B8%B2%E0%B8%81%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B9%84%E0%B8%A1%E0%B9%88%E0%B8%9B%E0%B8%A5%E0%B8%AD%E0%B8%94%E0%B8%A0%E0%B8%B1%E0%B8%A2%E0%B8%82%E0%B8%AD%E0%B8%87+BGP+%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%95%E0%B8%A3%E0%B8%A7%E0%B8%88%E0%B8%88%E0%B8%B1%E0%B8%9A%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%A3%E0%B8%B1%E0%B9%88%E0%B8%A7%E0%B9%84%E0%B8%AB%E0%B8%A5%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B9%80%E0%B8%AA%E0%B9%89%E0%B8%99%E0%B8%97%E0%B8%B2%E0%B8%87&url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Froute-leak-detection%2F)[](https://www.threads.net/intent/post?text=%E0%B8%9B%E0%B8%81%E0%B8%9B%E0%B9%89%E0%B8%AD%E0%B8%87%E0%B8%A5%E0%B8%B9%E0%B8%81%E0%B8%84%E0%B9%89%E0%B8%B2+Cloudflare+%E0%B8%88%E0%B8%B2%E0%B8%81%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B9%84%E0%B8%A1%E0%B9%88%E0%B8%9B%E0%B8%A5%E0%B8%AD%E0%B8%94%E0%B8%A0%E0%B8%B1%E0%B8%A2%E0%B8%82%E0%B8%AD%E0%B8%87+BGP+%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%95%E0%B8%A3%E0%B8%A7%E0%B8%88%E0%B8%88%E0%B8%B1%E0%B8%9A%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%A3%E0%B8%B1%E0%B9%88%E0%B8%A7%E0%B9%84%E0%B8%AB%E0%B8%A5%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B9%80%E0%B8%AA%E0%B9%89%E0%B8%99%E0%B8%97%E0%B8%B2%E0%B8%87+https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Froute-leak-detection%2F)

## แท็กที่เกี่ยวข้อง

[BGP](https://blog.cloudflare.com/th-th/tag/bgp/)[RPKI](https://blog.cloudflare.com/th-th/tag/rpki/)[Security Week](https://blog.cloudflare.com/th-th/tag/security-week/)[ความปลอดภัย](https://blog.cloudflare.com/th-th/tag/security/)

ติดตามบนโซเชียลมีเดีย

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## สมัครรับการแจ้งเตือนโพสต์ใหม่

อีเมล

เราจะไม่เปิดเผยอีเมลของคุณ

สมัคร

ขอบคุณที่สมัครรับข่าวสาร! โปรดตรวจสอบกล่องจดหมายเพื่อยืนยัน
