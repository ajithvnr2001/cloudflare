---
url: https://blog.cloudflare.com/th-th/mitigating-bot-attacks-against-cloudflare/
title: \u0e01\u0e32\u0e23\u0e1a\u0e23\u0e23\u0e40\u0e17\u0e32\u0e1c\u0e25\u0e01\u0e23\u0e30\u0e17\u0e1a\u0e08\u0e32\u0e01\u0e01\u0e32\u0e23\u0e42\u0e08\u0e21\u0e15\u0e35 Cloudflare \u0e02\u0e2d\u0e07\u0e1a\u0e47\u0e2d\u0e15 | \u0e1a\u0e25\u0e47\u0e2d\u0e01 Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:51:04.049821+00:00
---

# การบรรเทาผลกระทบจากการโจมตี Cloudflare ของบ็อต | บล็อก Cloudflare

> Source: https://blog.cloudflare.com/th-th/mitigating-bot-attacks-against-cloudflare/

[บล็อก](https://blog.cloudflare.com/th-th/)

[Attacks](https://blog.cloudflare.com/th-th/tag/attacks/)[Bot Management](https://blog.cloudflare.com/th-th/tag/bot-management/)[Bots](https://blog.cloudflare.com/th-th/tag/bots/)+1แสดงแท็กเพิ่มเติม 1 รายการ

4 แท็กแสดง 4 แท็ก

  * แท็กของโพสต์
  * [Bot Management](https://blog.cloudflare.com/th-th/tag/bot-management/)[Security Week](https://blog.cloudflare.com/th-th/tag/security-week/)
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

[Attacks](https://blog.cloudflare.com/th-th/tag/attacks/)[Bot Management](https://blog.cloudflare.com/th-th/tag/bot-management/)[Bots](https://blog.cloudflare.com/th-th/tag/bots/)[Security Week](https://blog.cloudflare.com/th-th/tag/security-week/)

26 มีนาคม 2564

# การบรรเทาผลกระทบจากการโจมตี Cloudflare ของบ็อต

![Sergi Isasi](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44GA2M8TX4RHAHVAP55XN1.png&w=64&h=64&f=webp&fit=cover&position=center)

[Sergi Isasi](https://blog.cloudflare.com/th-th/author/sergi/)

อ่าน 2 นาที

คัดลอก URL

โพสต์นี้มีให้อ่านใน [English](https://blog.cloudflare.com/mitigating-bot-attacks-against-cloudflare/)และ[Bahasa Indonesia](https://blog.cloudflare.com/id-id/mitigating-bot-attacks-against-cloudflare/).

![Mitigating Bot Attacks against Cloudflare](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4895BES3KE5TVJ0RKV6CWB.png&w=1382&h=668&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/////fz+7+/w5ufo6ujq8e3w8O7x6Ont/////v3+7+/u5uXi6+bi8uzp8u7t6uvr////////8fDt6OXe7ebd9u3k9vDr7u7r////////9vXw7enh8+rf/PLn/PXu8/Pw/////////fz59fLr+/Pr//vy//34+fr4/////////////vz5///7////////////////////////////////////////////////////////////////////////////)

คำว่า “บ็อต” บนอินเทอร์เน็ตเป็นอะไรที่ค่อนข้างโหลดได้พอสมควร ประสบการณ์ 'บ็อต' แรกสุดของฉันคือ [บน IRC](https://en.wikipedia.org/wiki/IRC_bot) ที่บ็อตมีประโยชน์มาก โดยช่วยทำให้ช่องโปรดของคุณไม่ถูกผู้ใช้ที่ประสงค์ร้ายเข้าสวมรอยและเปิดให้ Game of Trivia ที่สนุกสนานเข้ามามีบทบาท ซึ่งเมื่อประมาณห้าปีที่แล้ว “บ็อต” มักจะนำมาอ้างถึงการแชทด้วยข้อความร่วมกับ AI และแพลตฟอร์ม/แอปการส่งข้อความว่าคือวิธีใหม่ในการโต้ตอบกับลูกค้า ทุกวันนี้ ความหมายแฝงส่วนใหญ่เกี่ยวกับบ็อตบนอินเทอร์เน็ต โดยเฉพาะอย่างยิ่งในพื้นที่ความปลอดภัยออกมาในทางลบ และเรามีผู้จำหน่ายหลายรายที่เสนอวิธีใหม่ในการตรวจจับและปิดกั้นบ็อต

บ็อตในรูปแบบที่ง่ายที่สุดคือซอฟต์แวร์อัตโนมัติที่นำมาใช้แทนการโต้ตอบของมนุษย์ ในตัวอย่างข้างต้น วิธีนี้ทำให้เราสามารถปรับขนาดกระบวนการให้เร็วขึ้นหรือครอบคลุมมากกว่าการดำเนินการโดยเจ้าหน้าที่เพียงครั้งเดียว [บ็อตของเครื่องมือค้นหา](https://help.duckduckgo.com/duckduckgo-help-pages/results/duckduckbot/) มีอยู่เพราะเป็นไปไม่ได้ (หรืออย่างน้อยที่สุดก็ทำไม่ได้) ที่จะรวบรวมข้อมูลอินเทอร์เน็ตทีละชุด ประโยชน์ของสเกลนำมาใช้ทั้งด้านดีและด้านไม่ดีด้วยการโจมตีทรัพย์สินทางอินเทอร์เน็ต มีการใช้บ็อตอย่างกว้างขวางเพื่อโจมตี API ที่กำหนดค่าไม่ถูกต้อง ลบไซต์ หรือดูรายการข้อมูลประจำตัวที่ถูกนำไปเร่ขาย และดูว่าข้อมูลใดใช้กับอุปกรณ์ปลายทางการเข้าสู่ระบบ ก่อนจะ[ขโมยข้อมูล](https://blog.cloudflare.com/protecting-apis-from-abuse-and-data-exfiltration/)

การแพร่ระบาดใหญ่ทั่วโลกทำให้เกิด[การขาดแคลนไมโครชิปทั่วโลก](https://hbr.org/2021/02/why-were-in-the-midst-of-a-global-semiconductor-shortage) โดยในปี 2020 ทั้ง Microsoft, Nvidia และ Sony ได้เปิดตัวอุปกรณ์เล่นเกมหรือการ์ดวิดีโอที่เป็นที่ต้องการมาก แต่มีสินค้าไม่เพียงพอ และสถานการณ์นี้คงอยู่ต่ออีกหลายเดือนหลังจากนั้น สภาพการณ์แบบนี้เกิดขึ้นกับกิจกรรมทุกแบบของบ็อต ตั้งแต่มือสมัครเล่นที่พยายามเข้าถึงหนึ่งในรายการเหล่านี้เพื่อใช้งานเอง ไปจนถึงนักสะสมที่พยายามกว้านซื้อในราคาขายปลีกเพื่อนำไปขายต่อในตลาดเปิดที่มีราคาสูงกว่ามาก บ็อตจะย้ายสินค้าคงคลัง แล้วจึงเขียนสคริปต์ผ่านกระบวนการเพิ่มในรถเข็น/ซื้อได้เร็วกว่าผู้ใช้ที่ถูกต้องตามกฎหมายซึ่งอยู่เบื้องหลังเบราว์เซอร์ ลักษณะนี้นำไปสู่ความคับข้องใจ นี่คือผลที่เกิดขึ้นน้อยที่สุด แต่ก็อาจทำให้เกิด Layer 7 DDoS บนแอปพลิเคชันที่รวมปัญหา สิ่งที่เกิดขึ้นคือ Nvidia ถูกบีบให้[ยกเลิกการขายด้วยตนเองและย้อนกลับไปให้กับบ็อต](https://www.theverge.com/2020/9/21/21449353/nvidia-apology-rtx-3080-gpu-preorder-shortage-issues)ในระหว่างการเปิดตัว แม้ว่าการเล่นเกมจะทำให้เสียสมาธิ แต่สถานการณ์แบบเดียวกันนี้ก็ส่งผลเสียต่อ[การกระจายวัคซีน](https://www.capitalgazette.com/coronavirus/ac-cn-maryland-vaccine-bots-20210324-ngcmoadnwne6peb3fv6iu2hbri-story.html)

### การใช้ Bot Management บน cloudflare.com

Cloudflare Bot Management รุ่นปัจจุบันเปิดตัวในปี 2019 ซึ่งก็คือรุ่นที่มีการทดสอบผลิตภัณฑ์เป็นการภายในเพื่อดูว่าเราจะสามารถใช้ข้อมูลเครือข่ายของเราและ[การเรียนรู้ของระบบ (ML)](https://blog.cloudflare.com/stop-the-bots-practical-lessons-in-machine-learning/) เพื่อคาดการณ์ถึงความเป็นไปได้หรือไม่ได้ที่คำขอที่ให้ไว้จะแก้ปัญหาความท้าทาย ซึ่งในท้ายที่สุดแล้ว การทดสอบได้นำไปสู่ Bot Score แรกของเราและผลิตภัณฑ์ Bot Management ที่สมบูรณ์ ซึ่งได้ผ่านการปรับปรุงและการทำซ้ำหลายครั้ง และเป็นผลิตภัณฑ์ที่ประสบความสำเร็จอย่างมากในชุดเครื่องมือความปลอดภัยของลูกค้า ปัจจุบันเราได้ปรับปรุงผลิตภัณฑ์ตัวนี้เพิ่มเติมด้วย [Super Bot Fight Mode](https://blog.cloudflare.com/super-bot-fight-mode) สำหรับแผน Pro และ Business ของเรา

ในระหว่างขั้นตอนการพัฒนาภายในเบื้องต้น เราพบปัญหาหนึ่งในไซต์ที่ติดต่อกับลูกค้าของเราเอง ด้วยเหตุผลที่ยังไม่ชัดเจนนัก (แต่มีแนวโน้มว่าจะเป็นอันตราย) ผู้โจมตีจะกรอกข้อมูลขยะลงในแบบฟอร์มบนหน้า Landing Page ต่าง ๆ ของ Cloudflare ที่ซึ่งผู้ใช้ที่ลงทะเบียนไว้อย่างถูกต้องจะป้อนข้อมูลของตนเพื่อลงทะเบียนเข้าร่วมกิจกรรมหรือโปรโมชัน หรือเพื่อให้ทีมขายของเราติดต่อกลับ ในเบื้องต้น คือสร้างความรำคาญใจเพราะทีมต้องเข้ามาไล่เรียงข้อมูลและลบข้อมูลที่ไม่เกี่ยวข้องออกไป เราต้องย้อนกลับไปและระบุว่าข้อมูลใดที่ส่งมาอย่างถูกต้อง เมื่อปัญหาเพิ่มขึ้น ปัญหาก็จะทวีความสำคัญ จนส่งผลกระทบต่อผู้ให้บริการงานสนับสนุนของเรา (ซึ่งแบบฟอร์มมีความสัมพันธ์กัน) และเข้าสู่ CRM ของเราในที่สุด ตอนนี้ความรู้สึกจะเปลี่ยนจากความรำคาญสู่รูปแบบของ DDoS แอปพลิเคชัน ซึ่งต้องพิจารณาอย่างละเอียดถี่ถ้วนเมื่อจะหยุดเพื่อหลีกเลี่ยงข้อผิดพลาด เช่น การปิดกั้นการส่งข้อมูลที่ถูกต้อง

ปัญหามาถึงทีมวิศวกรของเรา และเห็นได้ชัดว่านี่เป็นที่ที่ดีในการเปิดตัวลูกค้ารายแรกและลองใช้ผลิตภัณฑ์ของเรา ในตอนแรก ผู้โจมตีไม่ได้พยายามปกปิดมากนัก พวกเขาใช้สคริปต์ที่พร้อมใช้งานทันที และบ่อยครั้งก็ไม่สนใจที่จะเปลี่ยนสัญญาณที่ชัดเจน เช่น ส่วนหัวของ User Agent หรือกระจายการโจมตีไปยัง IP หรือ ASN จำนวนมาก ขณะที่เราเพิ่มการวิเคราะห์พฤติกรรมลงในระบบและปรับโมเดล ML ผู้โจมตีก็ปรับยุทธวิธีของตน เมื่อเวลาผ่านไป เราจำเป็นต้องใช้เครื่องมือเต็มรูปแบบเมื่อผู้โจมตียังคงปรับตัว ตัวอย่างของการโจมตีล่าสุดมีดังต่อไปนี้ โดยในระหว่างการโจมตี การรับส่งข้อมูลอัตโนมัติเพิ่มขึ้นเป็น 7 เท่าจากปกติเป็นเวลาประมาณ 30 นาที การปรับขนาดน่าจะเป็นปัญหาสำหรับผู้ให้บริการดาวน์สตรีมของเรา ซึ่งในที่สุดเราก็ส่งการเรียก API เมื่อส่งแบบฟอร์ม ซึ่งในระหว่างการโจมตีครั้งนี้ ผลิตภัณฑ์ใหม่ของเราในชื่อ Anomaly Detection (ซึ่งเป็นพื้นฐาน[การตรวจจับการละเมิด API](https://blog.cloudflare.com/th-th/api-abuse-detection-th-th/) ของเรา) ได้ดำเนินการส่วนใหญ่ในการยกของหนัก ซึ่งคิดเป็น 42% ของการตรวจจับ

เรายังต้องจัดการกับบ็อตบนแดชบอร์ดของเราใน API ที่ผู้ใช้เผชิญอยู่จำนวนมาก รูปแบบการละเมิดทั่วไปที่เราพบเห็นในช่วงหลายปีที่ผ่านมาคือผู้ใช้ที่ประสงค์ร้ายลงชื่อสมัครใช้โดเมนจำนวนมาก มักมาจาก TLD ฟรี และปรากฏให้เห็นในหลายบัญชี ผู้ใช้ใช้โดเมนเหล่านี้และมีส่วนร่วมในรูปแบบของสแปม Search Engine Optimization (SEO) เชื่อกันว่าวิธีหนึ่งที่คุณเพิ่มอันดับการค้นหาคือการมีไซต์จำนวนมากที่เชื่อมโยงไปยังโดเมนของคุณ นักส่งสแปม SEO ลงทะเบียนโดเมนจำนวนมาก และจัดทำบันทึกชื่อโฮสต์นับพันบันทึกไว้ภายใน จากนั้นจึงเรียกเก็บเงินจากเจ้าของเว็บไซต์ที่ไร้จรรยาบรรณเพื่อเชื่อมต่อข้ามจากแต่ละโดเมนเหล่านี้

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-458 Embedded Image - Syp88E](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46TAWZT307SNZGNFAG586A.png&w=715&h=240&f=webp&fit=cover&position=center)

นอกเหนือจากเรื่องหลอกลวงของ SEO แล้ว สิ่งนี้ยังนำแสดงให้เห็นว่าระบบของเรามีปัญหาทางเทคนิคสองประการ ประการแรก: หากสร้างโดเมนและระเบียนเหล่านี้พร้อม ๆ กันมากพอ สิ่งที่เกิดขึ้นคือ [DNS Pump](https://blog.cloudflare.com/how-we-made-our-dns-stack-3x-faster/) ระบบของเราออกแบบมาเพื่อผลักดันระเบียน DNS ของลูกค้าไปยังตำแหน่งที่ตั้งกว่า 200 ตำแหน่งในเวลาไม่กี่วินาทีเพื่อทำให้ช้าลง เราภาคภูมิใจที่ทำให้การเผยแพร่ DNS เป็นเรื่องราวมหัศจรรย์ และลูกค้าของเราก็เคยชินและต้องอาศัยความเร็วในระดับนี้ ประการที่สอง มีค่าใช้จ่ายในทางปฏิบัติเมื่อจัดเก็บบันทึกเหล่านี้ในเซิร์ฟเวอร์ Edge แต่ละเครื่องของเราโดยไม่มีจุดประสงค์อื่นใดนอกจากเพื่อหลอกให้เครื่องมือค้นหาคิดว่าเว็บไซต์เป็นที่นิยม

การละเมิดประเภทนี้ใช้ได้เฉพาะในระดับสเกลเท่านั้น นักส่งสแปม SEO จะต้องสามารถลงทะเบียนโดเมนจำนวนมากได้อย่างมีประสิทธิภาพและเป็นไปโดยอัตโนมัติเพื่อขายบริการของตน ดังนั้นเราจึงส่ง Bot Management ไปจัดการกับปัญหา เดิมทีเราทำให้ปัญหาช้าลงผ่านคุณสมบัติหนึ่งที่ชื่อ Rate Limiting หรือการจำกัดอัตราและป้องกัน IP ที่กำหนดไม่ให้ลงทะเบียนบัญชีจำนวนมากในช่วงเวลาสั้น ๆ แต่ผู้โจมตียังคงมีอยู่ เราท้าทายการสมัครบัญชีใหม่ที่ปรากฏขึ้นโดยอัตโนมัติผ่านผลิตภัณฑ์ Bot Management ของเรา และปัญหาก็หมดไปในทันที

อีกส่วนหนึ่งของแดชบอร์ดของ Cloudflare ที่เกี่ยวข้องกับบ็อต คือระบบการเรียกเก็บเงินของเรา ผู้โจมตีจะใช้ระบบประมวลผลบัตรชำระเงินของเราเพื่อทดสอบความถูกต้องของหมายเลขบัตรเครดิตที่ถูกขโมย ซึ่งช่วยให้พวกเขาใช้หรือขายบัตรเพื่อใช้ในการทำธุรกรรมอื่นที่มีราคาแพงกว่าในไซต์อื่นได้ ถือเป็นอีกครั้งที่ความเร็วและสเกลเป็นกุญแจสำคัญที่นี่ ผู้โจมตีไม่ต้องการทดสอบหมายเลขบัตรหนึ่งหรือสองหมายเลข แต่ต้องการทดสอบบัตรเครดิตหลายสิบหรือหลายร้อยใบและทำให้กระบวนการเป็นไปโดยอัตโนมัติ ทีมวิศวกรรมการเรียกเก็บเงินของเราใช้ Bot Management เพื่อกระตุ้นความท้าทายหรือปิดกั้นเมื่อผู้ใช้เพิ่มหรือเปลี่ยนวิธีการชำระเงินเพื่อหยุดการโจมตีนี้ ทีมเรียกเก็บเงินยังส่งคะแนนบ็อตไปยังระบบตรวจจับการฉ้อโกงของผู้ให้บริการชำระเงินบุคคลที่สามของเราด้วย (ผ่าน [Cloudflare Workers](https://developers.cloudflare.com/bots/bot-management-enterprise#bot-management-variables)) ซึ่งรวมคะแนนไว้ในการวิเคราะห์เพื่อการตรวจสอบธุรกรรมด้วยตนเอง

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-458 Embedded Image - 9QJk02](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48AAZ25NM38TA213DN0DA1.png&w=715&h=151&f=webp&fit=cover&position=center)

### การสร้างรากฐานของข้อมูลทั่วโลก

ผลิตภัณฑ์ Bot Management ของเราประสบความสำเร็จ ซึ่งดูได้จากจำนวนของลูกค้าและปริมาณการรับส่งข้อมูลบนเครือข่ายของเรา เราอยู่ในตำแหน่งที่ไม่ซ้ำใครด้วยทรัพย์สินอินเทอร์เน็ตประมาณ 25 ล้านรายการ ที่ได้รับการคุ้มครองโดย Cloudflare เพื่อทำหน้าที่รวบรวมสัญญาณเหล่านี้และตีความออกมาเป็นข่าวกรองที่นำไปดำเนินการได้ การเปิดตัว Super Bot Fight Mode ในวันนี้ได้ขยายความสามารถนี้สู่ลูกค้าระดับ Pro และ Business แต่จะเพิ่มประสิทธิภาพในหมู่ผู้ใช้ Bot Management ทุกคนอีกด้วย ในขณะที่โซน Pro และ Business เริ่มท้าทายและปิดกั้นบ็อตโดยอิงจากสัญญาณของบ็อตโดยตรง ข้อมูลนี้จะฝึกโมเดลของเราได้โดยตรงมากขึ้นเมื่อเทียบกับข้อมูลที่อนุมานขึ้นที่เรานำมาใช้ท้าทายและปิดกั้นในเรื่องที่ไม่เกี่ยวกับบ็อต ความหลากหลายของสัญญาณและสเกลของข้อมูลบนแพลตฟอร์มทั่วโลกทำให้เรามั่นใจในความสามารถของเรา ไม่ใช่แค่ปิดกั้นบ็อตในวันนี้ แต่ในอนาคตด้วย

เรารู้สึกตื่นเต้นที่จะได้รับข้อมูลการตอบรับการเข้าใช้ก่อนใครจากลูกค้า Enterprise เกี่ยวกับการตรวจจับ API และโมเดลการละเมิดของเรา ทั้งนี้ API นำเสนอความท้าทายที่แตกต่างจากความท้าทายที่ได้จากคุณสมบัติที่เผชิญหน้าเว็บไซต์ แต่ประสบการณ์ของเราในการสร้าง[แพลตฟอร์ม Anomaly Detection](https://blog.cloudflare.com/lessons-learned-from-scaling-up-cloudflare-anomaly-detection-platform/) สำหรับ Bot Management ทำให้เราสามารถใช้เทคนิคที่เกี่ยวข้องเพื่อระบุตำแหน่งข้อมูล API และตรวจจับความผิดปกติภายในการรับส่งข้อมูลอัตโนมัติ การรวมเทคนิคใหม่เหล่านี้เข้ากับพอร์ตโฟลิโอการรักษาความปลอดภัยที่มีอยู่ของเรานั้นแสดงให้เห็นว่าเรามีความมุ่งมั่นที่จะจัดหาเครื่องมือที่ดีที่สุดให้กับลูกค้าบนแพลตฟอร์มเดียว ไม่ว่าพวกเขาจะมีการรับส่งข้อมูลใดในโดเมนก็ตาม การผสมผสานเครื่องมือทั้งหมดของเราช่วยให้ตอบสนองได้อย่างยืดหยุ่นเช่นกัน ลูกค้าสามารถปิดกั้นการโจมตี DDoS และบ็อตบางตัว ท้าทายบ็อตที่มีแนวโน้ม และใช้การจำกัดอัตราเพื่อกำหนดเป้าหมายของการรับส่งข้อมูล API ที่น่าสงสัย

ในหน้านี้

สนทนาออนไลน์

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fmitigating-bot-attacks-against-cloudflare%2F&t=%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9A%E0%B8%A3%E0%B8%A3%E0%B9%80%E0%B8%97%E0%B8%B2%E0%B8%9C%E0%B8%A5%E0%B8%81%E0%B8%A3%E0%B8%B0%E0%B8%97%E0%B8%9A%E0%B8%88%E0%B8%B2%E0%B8%81%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%82%E0%B8%88%E0%B8%A1%E0%B8%95%E0%B8%B5%20Cloudflare%20%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B8%9A%E0%B9%87%E0%B8%AD%E0%B8%95)[](https://x.com/intent/post?text=%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9A%E0%B8%A3%E0%B8%A3%E0%B9%80%E0%B8%97%E0%B8%B2%E0%B8%9C%E0%B8%A5%E0%B8%81%E0%B8%A3%E0%B8%B0%E0%B8%97%E0%B8%9A%E0%B8%88%E0%B8%B2%E0%B8%81%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%82%E0%B8%88%E0%B8%A1%E0%B8%95%E0%B8%B5+Cloudflare+%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B8%9A%E0%B9%87%E0%B8%AD%E0%B8%95&url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fmitigating-bot-attacks-against-cloudflare%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fmitigating-bot-attacks-against-cloudflare%2F)[](https://bsky.app/intent/compose?text=%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9A%E0%B8%A3%E0%B8%A3%E0%B9%80%E0%B8%97%E0%B8%B2%E0%B8%9C%E0%B8%A5%E0%B8%81%E0%B8%A3%E0%B8%B0%E0%B8%97%E0%B8%9A%E0%B8%88%E0%B8%B2%E0%B8%81%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%82%E0%B8%88%E0%B8%A1%E0%B8%95%E0%B8%B5+Cloudflare+%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B8%9A%E0%B9%87%E0%B8%AD%E0%B8%95+https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fmitigating-bot-attacks-against-cloudflare%2F)[](https://mastodonshare.com/?text=%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9A%E0%B8%A3%E0%B8%A3%E0%B9%80%E0%B8%97%E0%B8%B2%E0%B8%9C%E0%B8%A5%E0%B8%81%E0%B8%A3%E0%B8%B0%E0%B8%97%E0%B8%9A%E0%B8%88%E0%B8%B2%E0%B8%81%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%82%E0%B8%88%E0%B8%A1%E0%B8%95%E0%B8%B5+Cloudflare+%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B8%9A%E0%B9%87%E0%B8%AD%E0%B8%95&url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fmitigating-bot-attacks-against-cloudflare%2F)[](https://www.threads.net/intent/post?text=%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9A%E0%B8%A3%E0%B8%A3%E0%B9%80%E0%B8%97%E0%B8%B2%E0%B8%9C%E0%B8%A5%E0%B8%81%E0%B8%A3%E0%B8%B0%E0%B8%97%E0%B8%9A%E0%B8%88%E0%B8%B2%E0%B8%81%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%82%E0%B8%88%E0%B8%A1%E0%B8%95%E0%B8%B5+Cloudflare+%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B8%9A%E0%B9%87%E0%B8%AD%E0%B8%95+https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fmitigating-bot-attacks-against-cloudflare%2F)

## แท็กที่เกี่ยวข้อง

[Attacks](https://blog.cloudflare.com/th-th/tag/attacks/)[Bot Management](https://blog.cloudflare.com/th-th/tag/bot-management/)[Bots](https://blog.cloudflare.com/th-th/tag/bots/)[Security Week](https://blog.cloudflare.com/th-th/tag/security-week/)

ติดตามบนโซเชียลมีเดีย

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## สมัครรับการแจ้งเตือนโพสต์ใหม่

อีเมล

เราจะไม่เปิดเผยอีเมลของคุณ

สมัคร

ขอบคุณที่สมัครรับข่าวสาร! โปรดตรวจสอบกล่องจดหมายเพื่อยืนยัน
