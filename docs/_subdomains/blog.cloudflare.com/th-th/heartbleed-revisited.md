---
url: https://blog.cloudflare.com/th-th/heartbleed-revisited/
title: \u0e22\u0e49\u0e2d\u0e19\u0e14\u0e39 Heartbleed | \u0e1a\u0e25\u0e47\u0e2d\u0e01 Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:51:03.520581+00:00
---

# ย้อนดู Heartbleed | บล็อก Cloudflare

> Source: https://blog.cloudflare.com/th-th/heartbleed-revisited/

[บล็อก](https://blog.cloudflare.com/th-th/)

[Security Week](https://blog.cloudflare.com/th-th/tag/security-week/)[TLS](https://blog.cloudflare.com/th-th/tag/tls/)

2 แท็กแสดง 2 แท็ก

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



[Security Week](https://blog.cloudflare.com/th-th/tag/security-week/)[TLS](https://blog.cloudflare.com/th-th/tag/tls/)

27 มีนาคม 2564

# ย้อนดู Heartbleed

![Nick Sullivan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44NXK9203HP874YB09STY7.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Nick Sullivan](https://blog.cloudflare.com/th-th/author/nick-sullivan/)

อ่าน 3 นาที

คัดลอก URL

โพสต์นี้มีให้อ่านใน [English](https://blog.cloudflare.com/heartbleed-revisited/)และ[Bahasa Indonesia](https://blog.cloudflare.com/id-id/heartbleed-revisited/).

![Heartbleed Revisited](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45RG1TJ1Y7WGGPC78AD8QV.png&w=1513&h=708&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////+/3/7u/w5uXl5+bn7e3u7vDx6+3u/////f//7evs4Nzc4Nvc6OTl7ezt7e7v////////7err3NTV2tHS5N3e7err8PHy////////8e7v3tbX3NHS597f8e3u9vb3////////+ff46OLj597g8enr+fb3/P39////////////9vP09vLz/vr8////////////////////////////////////////////////////////////////////////)

ในปี 2014 มีการพบจุดบกพร่องใน OpenSSL ซึ่งเป็นไลบรารีการเข้ารหัสยอดนิยมที่ทำให้เซิร์ฟเวอร์ส่วนมากบนอินเทอร์เน็ตปลอดภัย จุดบกพร่องนี้ทำให้ผู้โจมตีสามารถใช้คุณลักษณะที่ไม่สะดุดตาชื่อ TLS heartbeats ในการอ่านหน่วยความจำจากเซิร์ฟเวอร์ที่เกี่ยวข้องได้ การ Heartbleed นี้เป็นข่าวใหญ่จากการที่มันทำให้ผู้โจมตีสามารถดึงข้อมูลอันเป็นความลับที่สำคัญที่สุดบนเซิร์ฟเวอร์ไปได้: คีย์ส่วนตัวของ TLS/SSL certificate นั่นเอง หลังแน่ใจแล้วว่าข้อผิดพลาดนี้ [ถูกเอาไปใช้ผิดๆ ได้ง่าย](https://blog.cloudflare.com/the-results-of-the-cloudflare-challenge/) พวกเราจึงเพิกถอนและได้ออก Certificate ใหม่มากกว่า [100,000 certificates](https://blog.cloudflare.com/the-heartbleed-aftermath-all-cloudflare-certificates-revoked-and-reissued/) ซึ่งเป็นการทำให้ปัญหาใหญ่ในเรื่องการจัดการความปลอดภัยบนอินเทอร์เน็ตเป็นที่สนใจมากขึ้นได้

แม้ว่า Heartbleed และ[เหตุการณ์ที่เป็นช่องโหว่ครั้งสำคัญทั้งหลาย](https://www.bankinfosecurity.com/private-keys-for-23000-digital-certificates-leaked-a-10689)จะสร้างความลำบากให้กับทีมความปลอดภัยและปฏิบัติการทั่วโลก พวกมันก็ยังเป็นโอกาสในการเรียนรู้ครั้งสำคัญให้กับอุตสาหกรรมด้วย ตลอดเวลาเจ็ดปีที่ผ่านมา Cloudflare ได้นำสิ่งที่เรียนรู้จาก Heartbleed มาพัฒนาการออกแบบระบบของเรา รวมไปถึงความยืดหยุ่นของอินเทอร์เน็ตโดยรวมด้วย อ่านต่อไปว่าการใช้ Cloudflare ช่วยลดความเสี่ยงในการเกิดช่องโหว่สำคัญๆ และลดค่าใช้จ่ายในการกู้คืนความเสียหายหากเกิดช่องโหว่เหล่านั้นได้อย่างไร

## เก็บคีย์ให้ปลอดภัย

หลักที่สำคัญของการออกแบบระบบความปลอดภัย คือ การป้องกันเชิงลึก สิ่งที่สำคัญควรถูกป้องกันด้วยเลเยอร์หลายๆ ชั้น นั่นเป็นเหตุผลว่าทำไมผู้คนที่ตระหนักถึงความปลอดภัยจะเก็บกุญแจบ้านสำรองไว้ในกล่องติดกุญแจอันปลอดภัยแทนที่จะวางไว้ใต้พรม สำหรับระบบการเข้ารหัสลับที่ต้องเผชิญกับอินเทอร์เน็ต การป้องกันเชิงลึกหมายถึงการออกแบบระบบของคุณให้คีย์ไม่เสี่ยงถูกขโมยได้โดยง่าย ซึ่งไม่ใช่ในกรณีของ OpenSSl และ Heartbleed คีย์ส่วนตัวถูกเก็บไว้ในหน่วยความจำผ่านกระบวนการเผชิญกับอินเทอร์เน็ตที่ไม่ปลอดภัยต่อหน่วยความจำ ทำให้จุดบกพร่องในการเปิดเผยหน่วยความจำเพียงจุดเดียวก็สามารถขโมยคีย์นั้นได้

Keyless SSL: แยกเซิร์ฟเวอร์และคีย์

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Keyless SSL: keeping the server separate from the key](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW472YA43T5NRSR7C5HFMB0G.png&w=715&h=296&f=webp&fit=cover&position=center)

จากกันกลยุทธ์การป้องกันเชิงลึกที่ได้ผลในการป้องกันคีย์ส่วนตัวของ TLS/SSL คือการแบ่งกระบวนการออกเป็นสองส่วน: ส่วนของคีย์ส่วนตัว/การยืนยันตัวตนและส่วนของการเข้ารหัส/การถอดรหัส นี่จึงเป็นเหตุผลที่ทำให้เราพัฒนา Keyless SSL ขึ้น เพื่อให้ลูกค้ามีอำนาจในการควบคุมคีย์ส่วนตัวของพวกเขาอย่างเต็มที่ โดยที่ในขณะเดียวกันก็อนุญาตให้ Cloudflare จัดการรายละเอียดที่เหลือของการเชื่อมต่อ[Keyless SSL](https://blog.cloudflare.com/keyless-ssl-the-nitty-gritty-technical-details/)ช่วยให้เกิดการแยกกันอย่างเป็นรูปธรรมของที่ที่คีย์ถูกใช้กับที่ที่คีย์ถูกเก็บรักษา พวกเรารองรับ Keyless SSL ทั้งบนซอฟท์แวร์และอุปกรณ์จัดการความปลอดภัยฮาร์ดแวร์ (HSMs) และในวันนี้พวกเราขอประกาศว่าพวกเรารองรับ [HSMs บนคลาวด์หลายอุปกรณ์แล้ว](https://blog.cloudflare.com/keyless-ssl-supports-fips-140-2-l3-hsm)

Geo Key Manager: จัดการคีย์ที่กำหนดได้ตามภูมิศาสตร์

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Geo Key Manager: configurable key management by geography](https://blog.cloudflare.com/_emdash/api/media/file/01KW46J3EN9BBN0M4BRXK3Y7RN.gif)

Heartbleed แสดงให้เราเห็นว่ากลยุทธ์นี้ยังสามารถเป็นประโยชน์ในการเสริมเลเยอร์ของความปลอดภัยแก่คีย์ส่วนตัวที่เราจัดการให้กับลูกค้าของเราด้วย [Geo Key Manager](https://blog.cloudflare.com/geo-key-manager-how-it-works/) เป็นคุณลักษณะที่อนุญาตให้ลูกค้าสามารถเลือกสถานที่ใดก็ได้บนโลกเพื่อเป็นที่เก็บคีย์ของพวกเขา Geo Key Manager ป้องกันช่องโหว่ทางกายภาพของเซิร์ฟเวอร์บนภูมิภาคต่างๆ ในปี 2019 พวกเราพัฒนาไปอีกขั้นด้วยการปรับใช้กลยุทธ์ชื่อ [Keyless Everywhere](https://blog.cloudflare.com/going-keyless-everywhere/) โดยย้ายคีย์ที่ถูกจัดการทั้งหมดไปอยู่บนระบบซึ่งแยกอินเทอร์เน็ตและคีย์ออกจากกันอย่างสมเหตุสมผล

Delegated Credentials: แยกคีย์โดยปราศจากเวลาแฝง

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Delegated Credentials: key separation with no latency](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW490APX1HK0ET9YQWKKRS7V.jpg&w=512&h=292&f=webp&fit=cover&position=center)

Keyless SSL เป็นโซลูชันการรักษาความปลอดภัยที่ยอดเยี่ยม แต่อาจมีเวลาแฝงได้โดยขึ้นอยู่กับที่ที่เก็บคีย์ ดังนั้น พวกเราจึงพัฒนามาตรฐานใหม่ที่เรียกว่า [Delegated Credential](https://blog.cloudflare.com/keyless-delegation/) ร่วมกับ IETF ซึ่งจะอนุญาตให้การเชื่อมต่อสามารถใช้คีย์ที่มีอายุสั้นจาก Certificate แทนที่จะใช้ตัว Certificate เองใน TLS วิธีการนี้สามารถกำจัดเวลาแฝงที่เพิ่มจาก Keyless SSL ได้ พวกเรารองรับ Delegated Credential สำหรับลูกค้าที่ใช้ Keyless SSL และ Geo Key Manager ทุกรายและ Firefox 89 (พฤษภาคม 2021) จะทำให้สามารถรองรับ Delegated Credential เป็นค่าเริ่มต้นได้

### **ทำให้การเพิกถอนได้ผล**

เมื่อเกิด Heartbleed ขึ้นแล้วทำให้ Certificate กว่าหลายแสนใบมีความเสี่ยงที่จะเกิดช่องโหว่ขึ้นนั้น การเพิกถอนและออก Certificate เหล่านี้ใหม่จึงเป็นสิ่งที่สมเหตุสมผล แต่การทำเช่นนั้นก่อให้เกิดผลกระทบอันไม่คาดคิดตามมา

ผลกระทบแรกของการเพิกถอน คือ การเกิดปริมาณการรับส่งข้อมูลที่เกี่ยวข้องในเครือข่ายเพิ่มขึ้นอย่างมหาศาล ในปี 2014 มีกลไกการเพิกถอน Certificate สามกลไกหลักด้วยกัน คือ:

  * Certificate Revocation Lists (CRLs)
    * รายการหมายเลขซีเรียลที่ถูกเพิกถอนต่อ Certificate แต่ละรายการ
  * โปรโตคอลสถานะใบรับรองออนไลน์ (OCSP)
    * โปรโตคอลในการดูประวัติของ Certificate แต่ละรายการและสถานะการเพิกถอน
    * สามารถดูประวัติ OCSP ได้จากเบราว์เซอร์หรือสามารถรวมการตอบกลับจากเซิร์ฟเวอร์ ณ ขณะที่มีการเชื่อมต่อ “การเย็บเล่ม OCSP” ได้
  * ชุดของ CRL — ระบบเพิกถอนที่กำหนดได้ของ Chrome
    * รายการเกี่ยวกับการเปลี่ยนแปลงของหมายเลขประจำเครื่องที่ถูกเพิกถอนที่จำกัดแค่ Certificate ที่มีค่าสูง



Certificate หลายหมื่นใบถูกเพิกถอนพร้อมๆ กันจากความเสี่ยงในการเกิดช่องโหว่จาก Heartbleed จากนั้น CRL สำหรับ CA ที่โดดเด่น, GlobalSign เพิ่มจาก [22KB ขึ้นเป็น 4.7MB ในวันเดียว](https://blog.cloudflare.com/the-hard-costs-of-heartbleed/)นันทำให้เกิดการหยุดชะงักครั้งใหญ่ในโครงสร้างพื้นฐานการแคชภายในของ Cloudflare และการเพิ่มขึ้นอย่างฉับพลันของ Bandwidth ที่ส่งผลกระทบต่ออินเทอร์เน็ตโดยรวมเมื่อไคลเอ็นต์ทุกคนที่ใช้ CRL ตรวจสอบ Certificate (ส่วนใหญ่เป็น Microsoft Windows) ดาวน์โหลดไฟล์ดังกล่าวหลังเหตุการณ์การเพิกถอนในครั้งนี้ก็ชัดเจนว่ามีสาเหตุอื่นว่าทำไมการเพิกถอนไม่ใช่ระบบที่ใช้งานได้ หากมีผู้ใช้ใน Firefox สร้างการเชื่อมต่อกับเว็บไซต์และไม่มีการตอบสนองของ OCSP ที่เย็บเล่มแล้ว Firefox จะสืบค้นภายในเซิร์ฟเวอร์เพื่อหาการตอบสนองนั้น แต่ในขณะเดียวกัน Firefox ก็จะปรับใช้กลยุทธ์ใช้งานเมื่อเกิดความผิดพลาด นั่นคือ: หากการตอบสนองของ OCSP ใช้เวลานานเกินไป การตรวจสอบการเพิกถอนนั้นจะถูกลัดขั้นตอนและหน้านั้นจะแสดงผล ผู้โจมตีที่มีตำแหน่งในเครือข่ายที่ดีกว่าสามารถใช้ Certificate ที่มีช่องโหว่_และถูกเพิกถอน_ ในการโจมตีผู้ใช้งานได้โดยแค่บล็อกการร้องขอ OCSP และปล่อยให้เบราว์เซอร์ข้ามการตรวจสอบการเพิกถอนซะ การเย็บเล่มของ OCSP เป็นวิธีที่เชื่อถือได้ของเซิร์ฟเวอร์ในการได้การตอบสนองของ OCSP มายังเบราว์เซอร์ แต่เพราะการเย็บเล่มไม่ใช่ข้อบังคับสำหรับไคลเอ็นด์ ผู้โจมตีจึงสามารถแค่ตัดการเย็บเล่มออกไปได้และเบราว์เซอร์ก็จะไม่สามารถเปิดได้ ทำให้ผู้ใช้ถูกโจมตีได้ง่าย OCSP ยังไม่สามารถให้การป้องกันช่องโหว่ของคีย์ในโหมดเปิดใช้งานเมื่อล้มเหลวได้ดีนัก (แล้ว OCSP ยังถือเป็น [การรั่วไหลของความเป็นส่วนตัว](https://www.eff.org/deeplinks/2020/11/macos-leaks-application-usage-forces-apple-make-hard-decisions) ด้วย แต่นั่นเป็นอีกปัญหาหนึ่ง)

สถานการณ์ด้านความปลอดภัยใน Chrome น่าเป็นห่วงมากกว่านั้นอีก เนื่องจากทั้ง OCSP และ CRL ไม่ได้ถูกตรวจสอบ Certificate ส่วนใหญ่ (ชุดของ CRL มีแต่ Certificate ที่ "มีการตรวจสอบแบบขยาย") Certificate ส่วนใหญ่จึงได้รับความไว้ใจโดยไม่มีการตรวจสอบสถานะการเพิกถอนเลย โซลูชันสำหรับการเพิกถอนชุด Certificate ที่ Cloudflare จัดการบน Chrome ในกรณี Heartbleed นั้น แท้จริงแล้วเป็นเพียง Patch สั้นๆ ของฐานรหัส Chromium เท่านั้น ชัดเจนว่าไม่ได้เป็นโซลูชันที่ขยายผลได้แน่!

การเพิกถอน Certificate ปริมาณมากในปี 2014 ว่ากันอย่างตรงไปตรงมาได้เลยว่ามันไม่ได้ผล ในขณะนั้น Certificate บางส่วนยังมึอายุมากถึง 5 ปี ช่องโหว่ของคีย์จึงเป็นปัญหาที่ส่งผลระยะยาว

ในปี 2015 ได้เกิดมาตรฐานแบบใหม่ที่ดูเหมือนจะเป็นโซลูชันที่สมเหตุสมผลกับปัญหานี้ขึ้น: มีการออก Certificate [OCSP ที่ต้องเย็บเล่ม](https://scotthelme.co.uk/ocsp-must-staple/) ที่มีคุณลักษณะที่ต้องเย็บเล่ม ซึ่งจะได้รับความไว้วางใจก็ต่อเมื่อมีการเย็บเล่ม OCSP ที่ถูกต้อง หาก Certificate OCSP ที่ต้องเย็บเล่มนี้มีช่องโหว่และถูกเพิกถอน มันก็จะถูกใช้โจมตีผู้ใช้ได้ในอายุของ OCSP ที่ออกให้ล่าสุดเท่านั้น (โดยปกติคือ 10 วันหรือน้อยกว่า) นี่จึงเป็นการปรับปรุงครั้งใหญ่และช่วยลดความเสี่ยงโดยรวมของผู้ถือ Certificate ลงได้

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-405 Embedded Image - zbUHgD](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44MPE0YGV21V5F2ZNH0NX0.png&w=715&h=228&f=webp&fit=cover&position=center)

Cloudflare ได้รองรับการพยายามเย็บเล่ม OCSP ที่ดีที่สุด[มาตั้งแต่ปี 2012](https://blog.cloudflare.com/ocsp-stapling-how-cloudflare-just-made-ssl-30/) ในปี 2017 พวกเราได้เริ่มปรับปรุงความน่าเชื่อถือในการเย็บเล่ม OCSP ของพวกเราเพื่อให้เราสามารถรองรับ Certificate OCSP ที่ต้องเย็บเล่มได้ ผลลัพธ์ก็คือ [การเย็บเล่ม OCSP](https://blog.cloudflare.com/high-reliability-ocsp-stapling/) ที่น่าเชื่อถือสูงและงานวิจัยที่ได้รับการตีพิมพ์[ใน IMC](https://dl.acm.org/doi/10.1145/3278532.3278543)ซึ่งแสดงให้เห็นถึงความกว้างขวางที่มากขึ้นของ OCSP ที่ต้องเย็บเล่มบนอินเทอร์เน็ต ตอนนี้ Cloudflare รองรับ Certificate OCSP ที่ต้องเย็บเล่มแล้ว เป็นการเสริมความปลอดภัยหากเกิดกรณีช่องโหว่ของคีย์ในอนาคต

### **2014 เทียบกับ ปัจจุบัน**

พวกเรามากันได้ไกลในระยะเวลาเจ็ดปี Cloudflare ได้คิดค้นการป้องกันคีย์ของ TLS/SSL และพื้นที่เพื่อความปลอดภัยอย่างไม่หยุดยั้ง นี่เป็นสิ่งที่เปลี่ยนไปในหลายปีมานี้:

ปี 2014

  * Certificate อายุ 5 ปี
  * การเย็บเล่ม OCSP เมื่อมีโอกาส
  * ไม่มี OCSP ที่ต้องเย็บเล่ม
  * คีย์ในกระบวนการเผชิญกับอินเทอร์เน็ต
  * ไม่มี Keyless SSL
  * ไม่มี Delegated Credentials



ปี 2021

  * Certificate ตลอดชีพที่กำหนดได้ (จากหนึ่งปีลดลงมาเป็นสองสัปดาห์ด้วย [ACM](https://blog.cloudflare.com/advanced-certificate-manager))
  * รองรับการเย็บเล่ม OCSP ได้ 100%
  * รองรับ OCSP ที่ต้องเย็บเล่ม
  * Keyless Everywhere
  * Keyless SSL + รองรับ HSM คลาวด์! (ใหม่)
  * Geo Key Manager
  * รองรับ Delegated Credentialการปรับปรุงเหล่านี้และการปรับปรุงที่มากกว่านี้คือเหตุผลสำคัญว่าทำไม Cloudflare ถึงเป็นผู้นำในพื้นที่สำหรับความปลอดภัยและทำไม Heartbleed อันต่อไปจะไม่แย่เท่าที่อันก่อนหน้านี้



ในหน้านี้

สนทนาออนไลน์

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fheartbleed-revisited%2F&t=%E0%B8%A2%E0%B9%89%E0%B8%AD%E0%B8%99%E0%B8%94%E0%B8%B9%20Heartbleed)[](https://x.com/intent/post?text=%E0%B8%A2%E0%B9%89%E0%B8%AD%E0%B8%99%E0%B8%94%E0%B8%B9+Heartbleed&url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fheartbleed-revisited%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fheartbleed-revisited%2F)[](https://bsky.app/intent/compose?text=%E0%B8%A2%E0%B9%89%E0%B8%AD%E0%B8%99%E0%B8%94%E0%B8%B9+Heartbleed+https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fheartbleed-revisited%2F)[](https://mastodonshare.com/?text=%E0%B8%A2%E0%B9%89%E0%B8%AD%E0%B8%99%E0%B8%94%E0%B8%B9+Heartbleed&url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fheartbleed-revisited%2F)[](https://www.threads.net/intent/post?text=%E0%B8%A2%E0%B9%89%E0%B8%AD%E0%B8%99%E0%B8%94%E0%B8%B9+Heartbleed+https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fheartbleed-revisited%2F)

## แท็กที่เกี่ยวข้อง

[Security Week](https://blog.cloudflare.com/th-th/tag/security-week/)[TLS](https://blog.cloudflare.com/th-th/tag/tls/)

ติดตามบนโซเชียลมีเดีย

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)

  * ![Nick Sullivan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44NXK9203HP874YB09STY7.jpg&w=64&h=64&f=webp&fit=cover&position=center)[Nick Sullivan](https://blog.cloudflare.com/th-th/author/nick-sullivan/)

[](https://crypto.dance)




## สมัครรับการแจ้งเตือนโพสต์ใหม่

อีเมล

เราจะไม่เปิดเผยอีเมลของคุณ

สมัคร

ขอบคุณที่สมัครรับข่าวสาร! โปรดตรวจสอบกล่องจดหมายเพื่อยืนยัน
