---
url: https://blog.cloudflare.com/th-th/guest-blog-zero-trust-access-kubernetes/
title: Guest Blog: k8s tunnels \u0e17\u0e35\u0e48\u0e21\u0e35 Kudelski Security | \u0e1a\u0e25\u0e47\u0e2d\u0e01 Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:46:11.464540+00:00
---

# Guest Blog: k8s tunnels ที่มี Kudelski Security | บล็อก Cloudflare

> Source: https://blog.cloudflare.com/th-th/guest-blog-zero-trust-access-kubernetes/

[บล็อก](https://blog.cloudflare.com/th-th/)

[CIO Week](https://blog.cloudflare.com/th-th/tag/cio-week/)[Cloudflare Access](https://blog.cloudflare.com/th-th/tag/cloudflare-access/)[Cloudflare Tunnel](https://blog.cloudflare.com/th-th/tag/cloudflare-tunnel/)+2แสดงแท็กเพิ่มเติม 2 รายการ

5 แท็กแสดง 5 แท็ก

  * แท็กของโพสต์
  * [Cloudflare Access](https://blog.cloudflare.com/th-th/tag/cloudflare-access/)[Cloudflare Tunnel](https://blog.cloudflare.com/th-th/tag/cloudflare-tunnel/)[Zero Trust](https://blog.cloudflare.com/th-th/tag/zero-trust/)
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



[Guest Post](https://blog.cloudflare.com/th-th/tag/guest-post/)[Zero Trust](https://blog.cloudflare.com/th-th/tag/zero-trust/)

[CIO Week](https://blog.cloudflare.com/th-th/tag/cio-week/)[Cloudflare Access](https://blog.cloudflare.com/th-th/tag/cloudflare-access/)[Cloudflare Tunnel](https://blog.cloudflare.com/th-th/tag/cloudflare-tunnel/)[Guest Post](https://blog.cloudflare.com/th-th/tag/guest-post/)[Zero Trust](https://blog.cloudflare.com/th-th/tag/zero-trust/)

8 ธันวาคม 2564

# Guest Blog: k8s tunnels ที่มี Kudelski Security

![Romain Aviolat](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46QR28J0P7014Z8BQ4JJKR.png&w=64&h=64&f=webp&fit=cover&position=center)

[Romain Aviolat](https://blog.cloudflare.com/th-th/author/romain-aviolat/)

อ่าน 3 นาที

คัดลอก URL

โพสต์นี้มีให้อ่านใน [English](https://blog.cloudflare.com/guest-blog-zero-trust-access-kubernetes/) [日本語](https://blog.cloudflare.com/ja-jp/guest-blog-zero-trust-access-kubernetes/) [简体中文](https://blog.cloudflare.com/zh-cn/guest-blog-zero-trust-access-kubernetes/) และ[Bahasa Indonesia](https://blog.cloudflare.com/id-id/guest-blog-zero-trust-access-kubernetes/).

![Guest Blog: k8s tunnels with Kudelski Security](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW471Y5SE2PHSG0TP2F83CTW.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/Pjk+PXg7+3a6+nZ7+vd8+3f7+ra5ePQ//vm+/fj8e/d7erc8ezg9e7i8evd6OXT//7q//rn9vLh8ezg9e3j+fDl9e7g7OjX///t//7q+vXl9u/j+fDn/fPo+vLk8ezb///x///u//nn+vPl/vTo//fr/vbn9fHe///0///w//zo/vbl//fp//vs//rp+fTg///2///x//7p//jl//rp//7t//zq/Pbh///2///y///p//nl//vp///t//3q/Pfi)

_วันนี้ เรารู้สึกตื่นเต้นที่จะได้เผยแพร่บล็อกโพสต์ที่เขียนโดยเพื่อนของเราที่ Kudelski Security ซึ่งเป็นผู้ให้บริการด้านความปลอดภัยที่มีการจัดการ เมื่อไม่กี่สัปดาห์ก่อนหน้านี้ Romain Aviolat หัวหน้าวิศวกรระบบคลาวด์และความปลอดภัยที่ Kudelski Security ได้ติดต่อทีม Zero Trust ของเราพร้อมเสนอโซลูชันเฉพาะสำหรับปัญหาที่ยากและขับเคลื่อนโดย Identity-aware Proxy ของ Cloudflare ซึ่งเราเรียกว่า Cloudflare Tunnel เพื่อให้แน่ใจว่ามีการเข้าถึงแอปพลิเคชันที่ปลอดภัยในสภาพแวดล้อมการทำงานจากระยะไกล_

 _เราสนุกกับการทำความรู้จักโซลูชันของพวกเขามากจนคิดจะเผยแพร่เรื่องราวเหล่านั้นต่อ สิ่งที่เราชื่นชอบเป็นพิเศษคือทีมวิศวกรของ Kudelski Security ที่ใช้ประโยชน์จากความยืดหยุ่นและความสามารถในการปรับขนาดของเทคโนโลยีของเราอย่างเต็มที่ เพื่อทำให้เวิร์กโฟลว์สำหรับผู้ใช้ปลายทางเกิดขึ้นโดยอัตโนมัติ หากคุณสนใจรายละเอียดเพิ่มเติมเกี่ยวกับ Kudelski Security โปรดดูผลงานด้านล่าง หรือ[บล็อกงานวิจัย](https://research.kudelskisecurity.com/)_ของทีมวิศวกร

### **การเข้าถึง Kubernetes แบบ Zero Trust**

ทีมวิศวกรของ Kudelski Security ได้หันมาให้ความสำคัญกับการย้ายโครงสร้างพื้นฐานของเราไปยังสภาพแวดล้อมแบบมัลติคลาวด์ในช่วงสองสามปีที่ผ่านมา การโยกย้ายระบบคลาวด์ภายในของเราสะท้อนถึงสิ่งที่ลูกค้าปลายทางของเราต้องการ และทำให้เรามีทั้งความเชี่ยวชาญและเครื่องมือเพื่อปรับปรุงการให้บริการลูกค้าเหล่านั้น นอกจากนั้น การเปลี่ยนแปลงลักษณะนี้ยังเปิดโอกาสให้เราได้ลองนึกภาพแนวทางการรักษาความปลอดภัยของตัวเองอีกครั้ง และใช้แนวปฏิบัติที่ดีที่สุดของ Zero Trust

จนถึงตอนนี้ หนึ่งในแง่มุมที่ท้าทายที่สุดของการนำ Zero Trust มาใช้คือการรักษาความปลอดภัยในการเข้าถึงระนาบการควบคุม (API) แบบต่าง ๆ ของ Kubernetes (K8) ในสภาพแวดล้อมคลาวด์ที่หลากหลาย ซึ่งในขั้นต้น ทีมโครงสร้างพื้นฐานของเราประสบปัญหาในการมองภาพรวม และใช้การควบคุมตามข้อมูลยืนยันตัวตนที่สอดคล้องกันกับ API ต่าง ๆ ที่เกี่ยวข้องกับคลัสเตอร์ K8 ที่แตกต่างกัน นอกจากนี้ เมื่อโต้ตอบกับ API เหล่านี้ นักพัฒนาของเรามักเจอทางตันเพราะไม่ทราบว่าจะต้องเข้าถึงคลัสเตอร์ใดและต้องทำอย่างไร

เราแก้ไขข้อขัดแย้งนี้ด้วยการออกแบบโซลูชันภายในองค์กรโดยใช้ประโยชน์จาก Cloudflare เพื่อให้นักพัฒนาสามารถใช้ระบบอัตโนมัติเพื่อตรวจสอบสิทธิ์คลัสเตอร์ K8 ได้อย่างปลอดภัยบนคลาวด์สาธารณะและสภาพแวดล้อมภายในองค์กร โดยเฉพาะอย่างยิ่งนักพัฒนารายใดๆ ตอนนี้เราสามารถแสดงบริการ K8 ทั้งหมดที่พวกเขาเข้าถึงได้ในสภาพแวดล้อมคลาวด์ที่กำหนด ตรวจสอบสิทธิ์คำขอเข้าถึงโดยใช้กฎ Zero Trust ของ Cloudflare และสร้างการเชื่อมต่อกับคลัสเตอร์นั้นผ่าน Cloudflare Tunnel ซึ่งเป็นพร็อกซี Identity-aware ของ Cloudflare

สิ่งสำคัญที่สุดคือ เครื่องมืออัตโนมัตินี้ทำให้ Kudelski Security เป็นองค์กรที่ดูแลการปรับปรุงรูปแบบความปลอดภัยของเราและยกระดับประสบการณ์ของนักพัฒนาไปพร้อม ๆ กัน เราคาดการณ์ว่า เครื่องมือนี้จะช่วยนักพัฒนาใหม่ประหยัดเวลาอย่างน้อยสองชั่วโมงที่จะต้องใช้เพื่ออ่านเอกสาร ส่งตั๋วบริการไอที และลงมือปรับใช้และกำหนดค่าเครื่องมือต่าง ๆ ที่จำเป็นสำหรับการเข้าถึงคลัสเตอร์ K8 ที่แตกต่างกัน

ในบล็อกนี้ เราจะให้รายละเอียดเกี่ยวกับกรณีปัญหาที่เราได้แก้ไข วิธีที่เราออกแบบเครื่องมืออัตโนมัติของเรา และวิธีที่ Cloudflare ช่วยให้เราเปลี่ยนแปลงในทางที่ดีขึ้นบนเส้นทาง Zero Trust ในแบบที่เป็นมิตรต่อการทำงานจากที่บ้าน

### **ความท้าทายในการรักษาความปลอดภัยของสภาพแวดล้อมมัลติคลาวด์**

เพราะ Kudelski Security ได้ขยายการให้บริการลูกค้าและทีมพัฒนาภายในของเรา เราจึงได้ขยายขอบเขตการใช้งานแอปพลิเคชันของเราภายในคลัสเตอร์ K8 หลายรายการและผู้ให้บริการระบบคลาวด์หลายราย K8s คลัสเตอร์ API สำหรับวิศวกรและนักพัฒนาโครงสร้างพื้นฐานของเรานั้นคือจุดเริ่มต้นที่สำคัญของการแก้ไขปัญหา เราทำงานใน GitOps และการปรับใช้แอปพลิเคชันทั้งหมดของเราเป็นแบบอัตโนมัติ แต่เรายังต้องเชื่อมต่อกับคลัสเตอร์อยู่บ่อยครั้งเพื่อดึงไฟล์บันทึกหรือดีบักปัญหา

แต่การรักษาความหลากหลายนี้สร้างความซับซ้อนและความกดดันให้กับผู้ดูแลระบบโครงสร้างพื้นฐาน สำหรับผู้ใช้ปลายทาง โครงสร้างพื้นฐานที่ขยายออกไปกว้างขวางอาจหมายถึงการต้องใช้ข้อมูลประจำตัวที่แตกต่างกัน เครื่องมือการเข้าถึงที่แตกต่างกันสำหรับแต่ละคลัสเตอร์ และไฟล์การกำหนดค่าต่าง ๆ เพื่อการติดตาม

ประสบการณ์การเข้าถึงที่ซับซ้อนเช่นนี้อาจทำให้การแก้ไขปัญหาแบบเรียลไทม์ประสบกับความยุ่งยาก ตัวอย่างเช่น วิศวกรที่รับช่วงงานพยายามทำความเข้าใจสภาพแวดล้อมของ K8 ที่ไม่คุ้นเคย เขาอาจค้นหาเอกสารกองโต หรือถูกบังคับให้ปลุกเพื่อนร่วมงานคนอื่น ๆ เพื่อถามคำถามง่าย ๆ ทั้งหมดนี้อาจเกิดข้อผิดพลาดได้และเสียเวลาอันมีค่า

วิธีการทั่วไปในการรักษาความปลอดภัยการเข้าถึง API ของ K8 คือความท้าทายที่เรารู้ว่าเราควรหลีกเลี่ยง ตัวอย่างเช่น เรารู้สึกว่าการเปิดเผย API สู่อินเทอร์เน็ตสาธารณะจะเพิ่มพื้นที่การโจมตีของเราอย่างหลีกเลี่ยงไม่ได้ ซึ่งเป็นความเสี่ยงที่เราไม่สามารถรับได้ เรายังไม่ต้องการให้มีการเข้าถึง API ของคลัสเตอร์ของเราในวงกว้างผ่านเครือข่ายภายใน และยอมรับความเสี่ยงของการเคลื่อนไหวดังกล่าว การที่ Kudelski เติบโตอย่างต่อเนื่อง ค่าใช้จ่ายในการดำเนินงานและความซับซ้อนของการปรับใช้ VPN ในกลุ่มพนักงานและภายใต้สภาพแวดล้อมระบบคลาวด์ที่แตกต่างกันจะนำไปสู่ความท้าทายในการปรับขนาดด้วย

แต่สิ่งที่เราต้องการกลับเป็นแนวทางที่จะช่วยให้เรารักษาสภาพแวดล้อมแบบไมโครเซ็กเมนต์ขนาดเล็ก โดเมนขนาดเล็กที่ทำงานผิดพลาด และการให้การเข้าถึงบริการได้ไม่เกินหนึ่งวิธี

### **การใช้ประโยชน์จากพร็อกซี Identity-aware ของ Cloudflare สำหรับการเข้าถึง Zero Trust**

ในการทำเช่นนี้ ทีมวิศวกรรมของ Kudelski Security ได้เลือกใช้แนวทางที่ทันสมัยกว่า นั่นคือ การสร้างการเชื่อมต่อระหว่างผู้ใช้และคลัสเตอร์ K8 ของเราแต่ละคลัสเตอร์ผ่านพร็อกซี Identity-aware (IAP) ทั้งนี้ IAP มีความยืดหยุ่นเมื่อนำมาใช้และเพิ่มเลเยอร์การรักษาความปลอดภัยด้านหน้าแอปพลิเคชันของเราโดยการตรวจสอบตัวตนของผู้ใช้เมื่อมีการร้องขอการเข้าถึง นอกจากนั้น พร็อกซีนี้ยังสนับสนุนแนวทาง Zero Trust ของเราด้วยการสร้างการเชื่อมต่อจากผู้ใช้ไปยังแอปพลิเคชันแต่ละรายการ ไม่ใช่เครือข่ายทั้งหมด

แต่ละคลัสเตอร์มี IAP ของตัวเองและชุดนโยบายของตัวเอง ซึ่งจะตรวจสอบข้อมูลระบุตัวตน (ผ่าน SSO ขององค์กรของเรา) และปัจจัยตามบริบทอื่น ๆ เช่น ตำแหน่งอุปกรณ์ของแล็ปท็อปของนักพัฒนาซอฟต์แวร์ IAP ไม่ได้แทนที่กลไกการพิสูจน์ตัวตนของคลัสเตอร์ K8 แต่เพิ่มกลไกใหม่เข้าไป และเพราะประโยชน์ของการเชื่อมโยงข้อมูลระบุตัวตนและ SSO กระบวนการนี้จึงโปร่งใสอย่างสมบูรณ์สำหรับผู้ใช้ปลายทางของเรา

ในการตั้งค่าของเรา Kudelski Security จะใช้ IAP ของ Cloudflare เป็นส่วนประกอบหนึ่งของ Cloudflare Access ซึ่งเป็นโซลูชัน ZTNA และหนึ่งในบริการด้านความปลอดภัยต่าง ๆ ที่รวมไว้เป็นหนึ่งเดียวโดยแพลตฟอร์ม Zero Trust ของ Cloudflare

สำหรับแอปบนเว็บจำนวนมาก IAP จะช่วยสร้างประสบการณ์ที่ราบรื่นสำหรับผู้ใช้ปลายทางที่ขอเข้าถึงผ่านเบราว์เซอร์ ผู้ใช้ตรวจสอบสิทธิ์ผ่าน SSO ขององค์กรหรือผู้ให้บริการข้อมูลระบุตัวตนก่อนเข้าถึงแอปที่ปลอดภัย ในขณะที่ IAP ทำงานในเบื้องหลัง

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-732 Embedded Image - P55jnN](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49K2VAFT4A519YQS24T537.png&w=715&h=445&f=webp&fit=cover&position=center)

โฟลว์ผู้ใช้นั้นดูแตกต่างไปสำหรับแอปพลิเคชันที่ใช้ CLI เนื่องจากเราไม่สามารถปรับเปลี่ยนเส้นทางโฟลว์เครือข่าย CLI เหมือนที่เราทำในเบราว์เซอร์ ในกรณีของเรา วิศวกรต้องการใช้ไคลเอนต์ K8 ที่พวกเขาชื่นชอบซึ่งอิงตาม CLI เช่น [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) หรือ [k9s](https://github.com/derailed/k9s) ซึ่งหมายความว่า Cloudflare IAP ของเราต้องทำหน้าที่เป็นพร็อกซี SOCKS5 ระหว่างไคลเอนต์ CLI และคลัสเตอร์ K8 แต่ละคลัสเตอร์

หากจะสร้างการเชื่อมต่อ IAP นี้ Cloudflare ต้องจัดเตรียม daemon ฝั่งเซิร์ฟเวอร์ที่มีน้ำหนักเบาซึ่งเรียกว่า_cloudflared_ ที่เชื่อมต่อโครงสร้างพื้นฐานกับแอปพลิเคชัน การเชื่อมต่อที่เข้ารหัสนี้ทำงานบนเครือข่ายทั่วโลกของ Cloudflare ซึ่งใช้นโยบาย Zero Trust กับการตรวจสอบครั้งเดียวผ่าน

อย่างไรก็ตาม หากไม่มีระบบอัตโนมัติ ทีมงานโครงสร้างพื้นฐานของ Kudelski Security จะต้องแจกจ่าย daemon บนอุปกรณ์ของผู้ใช้ปลายทาง ให้คำแนะนำเกี่ยวกับวิธีตั้งค่าการเชื่อมต่อที่เข้ารหัสเหล่านั้น และใช้ขั้นตอนการกำหนดค่าอื่น ๆ ที่ผู้ใช้ต้องทำเอง รวมถึงบำรุงรักษาตามช่วงเวลา นอกจากนี้ นักพัฒนายังคงขาดระนาบในการมองเห็นภายในคลัสเตอร์ K8 ต่าง ๆ ที่พวกเขาจะต้องเข้าถึงขณะทำงานประจำวัน

### **โซลูชันอัตโนมัติของเรา: k8s-tunnels!**

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-732 Embedded Image - cuETxG](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44DZ45FR0B1WE74BF3A9YQ.png&w=715&h=402&f=webp&fit=cover&position=center)

ทีมวิศวกรรมโครงสร้างพื้นฐานได้พัฒนาเครื่องมือภายในที่เรียกว่า "k8s-tunnels" เพื่อแก้ปัญหาเหล่านี้ เครื่องมือดังกล่าวจะฝังขั้นตอนการกำหนดค่าที่ซับซ้อนซึ่งทำให้นักพัฒนาซอฟต์แวร์ใช้ชีวิตได้ง่ายขึ้น นอกจากนี้ เครื่องมือนี้จะค้นหาคลัสเตอร์ K8 ทั้งหมดที่ผู้ใช้ที่ระบุเข้าถึงโดยอัตโนมัติตามนโยบาย Zero Trust ที่สร้างขึ้น หากต้องการเปิดใช้งานฟังก์ชันนี้ เราได้ฝัง SDK ของผู้ให้บริการคลาวด์สาธารณะรายใหญ่บางรายที่ Kudelski Security ใช้ เครื่องมือนี้ยังฝัง _cloudflared_ daemon ซึ่งหมายความว่าเราจำเป็นต้องแจกจ่ายเครื่องมือเพียงรายการเดียวให้กับผู้ใช้ของเรา

เมื่อรวบรวมรายละเอียดเข้าด้วยกัน พบว่า นักพัฒนาที่เปิดตัวเครื่องมือจะต้องผ่านเวิร์กโฟลว์ต่อไปนี้: (ภายใต้สมมุติฐานที่ว่าผู้ใช้มีข้อมูลประจำตัวที่ถูกต้องอยู่แล้ว ไม่เช่นนั้นเครื่องมือจะเปิดเบราว์เซอร์บน IDP ของเราเพื่อรับข้อมูลเหล่านี้)

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-732 Embedded Image - 1cW0Ni](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49D383W7PRHXJZ9GV5YH6T.png&w=715&h=402&f=webp&fit=cover&position=center)

1\. ผู้ใช้เลือกคลัสเตอร์หนึ่งรายการขึ้นไปเพื่อ

2\. k8s-tunnel จะเปิดการเชื่อมต่อกับ Cloudflare โดยอัตโนมัติและแสดงพร็อกซี SOCKS5 ในเครื่องบนเครื่องของนักพัฒนา

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-732 Embedded Image - e6BCTT](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48Q29GT1EXDBZ3768243HW.png&w=715&h=213&f=webp&fit=cover&position=center)

3.k8s-tunnel แก้ไขการกำหนดค่าไคลเอนต์ kubernetes ในเครื่องของผู้ใช้โดยผลักดันข้อมูลที่จำเป็นเพื่อให้ผ่านพร็อกซี SOCKS5 ในเครื่อง

4\. k8s-tunnel สลับบริบทจากไคลเอนต์ Kubernetes ไปเป็นการเชื่อมต่อปัจจุบัน

5\. ตอนนี้ ผู้ใช้สามารถใช้ไคลเอนต์ CLI ที่ตนเองชื่นชอบเพื่อเข้าถึงคลัสเตอร์ K8

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-732 Embedded Image - 33L8m2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47JP2K7630YC1MNQSH4H48.png&w=715&h=188&f=webp&fit=cover&position=center)

ทั้งกระบวนการทำได้ตรง ๆ ไม่สลับซับซ้อนและทีมวิศวกรของเราก็นำมาใช้เป็นประจำทุกวัน และแน่นอน ความมหัศจรรย์ทั้งหมดนี้เกิดขึ้นได้ผ่านกลไกการค้นหาอัตโนมัติที่เราได้สร้างไว้ใน k8s-tunnels เมื่อใดก็ตามที่มีวิศวกรใหม่เข้าร่วมทีม เราเพียงแค่ขอให้พวกเขาเริ่มกระบวนการค้นหาอัตโนมัติและเริ่มต้น

ดูตัวอย่างการทำงานของกระบวนการค้นหาอัตโนมัติได้จากด้านล่างนี้

  1. k8s-tunnels จะเชื่อมต่อกับ API ของผู้ให้บริการคลาวด์ที่แตกต่างกันของเรา และแสดงรายการคลัสเตอร์ K8 ที่ผู้ใช้สามารถเข้าถึงได้
  2. k8s-tunnels จะเก็บไฟล์กำหนดค่าในเครื่องบนเครื่องผู้ใช้ของคลัสเตอร์เหล่านั้น ดังนั้นกระบวนการนี้จะไม่ถูกเรียกใช้เกินหนึ่งครั้ง



### **การปรับปรุงระบบอัตโนมัติ**

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-732 Embedded Image - LLM3Dx](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45E9SX357T4GFFPEB0AD8X.png&w=715&h=265&f=webp&fit=cover&position=center)

สำหรับการปรับใช้ในสถานที่นั้นยากกว่าเล็กน้อย เนื่องจากเราไม่มีวิธีง่ายๆ ในการจัดเก็บเมตาดาต้าของคลัสเตอร์ K8 เช่นเดียวกับที่เราทำกับแท็กทรัพยากรกับผู้ให้บริการคลาวด์สาธารณะ เราตัดสินใจใช้ [Vault](https://www.vaultproject.io/) เป็นที่เก็บคีย์-ค่าเพื่อเลียนแบบแท็กทรัพยากรระบบคลาวด์สาธารณะสำหรับภายในองค์กร ซึ่งด้วยวิธีนี้ เราจะพบคลัสเตอร์ภายในองค์กรโดยอัตโนมัติโดยใช้กระบวนการเดียวกับผู้ให้บริการคลาวด์สาธารณะ

คุณอาจเห็นว่าในภาพบันทึกหน้าจอ CLI ก่อนหน้านี้ ผู้ใช้สามารถเลือกหลายคลัสเตอร์พร้อมกันได้! เรารับรู้อย่างรวดเร็วว่านักพัฒนาของเรามักต้องการเข้าถึงสภาพแวดล้อมที่หลากหลายพร้อมกันเพื่อเปรียบเทียบปริมาณงานที่กำลังทำในสายการผลิตและในขั้นตอนการจัดการ ดังนั้น แทนที่จะเปิดและปิดช่องสัญญาณทุกครั้งที่จำเป็นต้องสลับคลัสเตอร์ เราได้ออกแบบเครื่องมือเพื่อให้พวกเขาสามารถเปิดช่องสัญญาณหลายช่องพร้อมกันภายในอินสแตนซ์ k8s-tunnels เดียว และเพียงแค่สลับคลัสเตอร์ K8 ปลายทางบนแล็ปท็อปของตนเองเท่านั้น

สุดท้ายแต่ไม่ท้ายสุด เราเพิ่มการสนับสนุนรายการโปรดและการแจ้งเตือนเมื่อมีการเปิดตัวผลิตภัณฑ์รุ่นใหม่ โดยใช้ประโยชน์จาก Cloudflare Workers แต่ทั้งหมดนี้สำหรับโพสต์บล็อกอื่น

### **แล้วยังไงต่อ**

ในการออกแบบเครื่องมือนี้ เราได้ระบุปัญหาบางประการภายในไลบรารีของไคลเอนต์ Kubernetes เมื่อใช้ร่วมกับพร็อกซี SOCKS5 และเรากำลัง[ทำงานร่วมกับชุมชน Kubernetes](https://github.com/kubernetes/kubernetes/pull/105632) เพื่อแก้ไขปัญหาเหล่านั้น ทุกคนน่าจะได้รับประโยชน์จากโปรแกรมปะแก้หรือแพตช์เหล่านั้นในอนาคตอันใกล้

เราใช้บล็อกโพสต์นี้เพื่อเน้นถึงความเป็นไปได้ที่จะนำการรักษาความปลอดภัย Zero Trust ไปใช้กับปริมาณงานที่ซับซ้อนที่ทำงานบนสภาพแวดล้อมแบบมัลติคลาวด์ ควบคู่กับการปรับปรุงประสบการณ์ของผู้ใช้ปลายทาง

แม้ว่าวันนี้โค้ด "k8s-tunnels" ของเราจะเฉพาะเจาะจงกับ Kudelski Security มากเกินไป แต่เรามีเป้าหมายที่จะแชร์สิ่งที่เราสร้างขึ้นกลับคืนสู่ชุมชน Kubernetes เพื่อให้องค์กรอื่น ๆ และลูกค้า Cloudflare ได้รับประโยชน์

ในหน้านี้

สนทนาออนไลน์

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fguest-blog-zero-trust-access-kubernetes%2F&t=Guest%20Blog%3A%20k8s%20tunnels%20%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B8%A1%E0%B8%B5%20Kudelski%20Security)[](https://x.com/intent/post?text=Guest+Blog%3A+k8s+tunnels+%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B8%A1%E0%B8%B5+Kudelski+Security&url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fguest-blog-zero-trust-access-kubernetes%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fguest-blog-zero-trust-access-kubernetes%2F)[](https://bsky.app/intent/compose?text=Guest+Blog%3A+k8s+tunnels+%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B8%A1%E0%B8%B5+Kudelski+Security+https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fguest-blog-zero-trust-access-kubernetes%2F)[](https://mastodonshare.com/?text=Guest+Blog%3A+k8s+tunnels+%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B8%A1%E0%B8%B5+Kudelski+Security&url=https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fguest-blog-zero-trust-access-kubernetes%2F)[](https://www.threads.net/intent/post?text=Guest+Blog%3A+k8s+tunnels+%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B8%A1%E0%B8%B5+Kudelski+Security+https%3A%2F%2Fblog.cloudflare.com%2Fth-th%2Fguest-blog-zero-trust-access-kubernetes%2F)

## แท็กที่เกี่ยวข้อง

[CIO Week](https://blog.cloudflare.com/th-th/tag/cio-week/)[Cloudflare Access](https://blog.cloudflare.com/th-th/tag/cloudflare-access/)[Cloudflare Tunnel](https://blog.cloudflare.com/th-th/tag/cloudflare-tunnel/)[Guest Post](https://blog.cloudflare.com/th-th/tag/guest-post/)[Zero Trust](https://blog.cloudflare.com/th-th/tag/zero-trust/)

ติดตามบนโซเชียลมีเดีย

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)

  * ![Romain Aviolat](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46QR28J0P7014Z8BQ4JJKR.png&w=64&h=64&f=webp&fit=cover&position=center)[Romain Aviolat](https://blog.cloudflare.com/th-th/author/romain-aviolat/)

[](https://kudelskisecurity.com/)




## สมัครรับการแจ้งเตือนโพสต์ใหม่

อีเมล

เราจะไม่เปิดเผยอีเมลของคุณ

สมัคร

ขอบคุณที่สมัครรับข่าวสาร! โปรดตรวจสอบกล่องจดหมายเพื่อยืนยัน
