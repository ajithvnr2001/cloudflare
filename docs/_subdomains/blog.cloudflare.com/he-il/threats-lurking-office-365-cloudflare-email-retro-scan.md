---
url: https://blog.cloudflare.com/he-il/threats-lurking-office-365-cloudflare-email-retro-scan/
title: \u05d2\u05dc\u05d5 \u05d0\u05d9\u05dc\u05d5 \u05d0\u05d9\u05d5\u05de\u05d9\u05dd \u05d0\u05d5\u05e8\u05d1\u05d9\u05dd \u05d1-Office 365 \u05e9\u05dc\u05db\u05dd \u05e2\u05dd \u05db\u05dc\u05d9 \u05d4\u05e1\u05e8\u05d9\u05e7\u05d4 \u05dc\u05d0\u05d7\u05d5\u05e8 (Retro Scan) \u05e9\u05dc Cloudflare \u05e2\u05d1\u05d5\u05e8 \u05d4\u05d5\u05d3\u05e2\u05d5\u05ea \u05d3\u05d5\u05d0\"\u05dc | Cloudflare Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:37:01.423998+00:00
---

# גלו אילו איומים אורבים ב-Office 365 שלכם עם כלי הסריקה לאחור (Retro Scan) של Cloudflare עבור הודעות דוא"ל | Cloudflare Blog

> Source: https://blog.cloudflare.com/he-il/threats-lurking-office-365-cloudflare-email-retro-scan/

[בלוג](https://blog.cloudflare.com/he-il/)

[Birthday Week](https://blog.cloudflare.com/he-il/tag/birthday-week/)

1 תגיותהצג 1 תגיות

  * תגיות הפוסט
  *   * כל התגיות
  * תגיות תואמות
  * לא נמצאו תגיות
  * [בינה מלאכותית](https://blog.cloudflare.com/he-il/tag/ai/)
  * [מפתחים](https://blog.cloudflare.com/he-il/tag/developers/)
  * [Holocaust (HE)](https://blog.cloudflare.com/he-il/tag/holocaust/)
  * [החיים ב-Cloudflare](https://blog.cloudflare.com/he-il/tag/life-at-cloudflare/)
  * [שותפים](https://blog.cloudflare.com/he-il/tag/partners/)
  * [מדיניות ומשפטי](https://blog.cloudflare.com/he-il/tag/policy/)
  * [חדשות על מוצרים](https://blog.cloudflare.com/he-il/tag/product-news/)
  * [מכ"מ](https://blog.cloudflare.com/he-il/tag/cloudflare-radar/)
  * [אבטחה](https://blog.cloudflare.com/he-il/tag/security/)
  * [מהירות ומהימנות](https://blog.cloudflare.com/he-il/tag/speed-and-reliability/)
  * [Zero Trust](https://blog.cloudflare.com/he-il/tag/zero-trust/)



[Birthday Week](https://blog.cloudflare.com/he-il/tag/birthday-week/)

29 בספטמבר 2023

# גלו אילו איומים אורבים ב-Office 365 שלכם עם כלי הסריקה לאחור (Retro Scan) של Cloudflare עבור הודעות דוא"ל

![Ayush Kumar](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW449VZTK4C95VB94E47SS8C.png&w=64&h=64&f=webp&fit=cover&position=center)

[Ayush Kumar](https://blog.cloudflare.com/he-il/author/ayush/)

זמן קריאה של 3 דקות

העתקת כתובת URL

פוסט זה זמין גם ב [English](https://blog.cloudflare.com/threats-lurking-office-365-cloudflare-email-retro-scan/), [Deutsch](https://blog.cloudflare.com/de-de/threats-lurking-office-365-cloudflare-email-retro-scan/), [Español](https://blog.cloudflare.com/es-es/threats-lurking-office-365-cloudflare-email-retro-scan/), [Français](https://blog.cloudflare.com/fr-fr/threats-lurking-office-365-cloudflare-email-retro-scan/), [日本語](https://blog.cloudflare.com/ja-jp/threats-lurking-office-365-cloudflare-email-retro-scan/), [한국어](https://blog.cloudflare.com/ko-kr/threats-lurking-office-365-cloudflare-email-retro-scan/), [繁體中文](https://blog.cloudflare.com/zh-tw/threats-lurking-office-365-cloudflare-email-retro-scan/), [简体中文](https://blog.cloudflare.com/zh-cn/threats-lurking-office-365-cloudflare-email-retro-scan/), [Português](https://blog.cloudflare.com/pt-br/threats-lurking-office-365-cloudflare-email-retro-scan/), [Русский](https://blog.cloudflare.com/ru-ru/threats-lurking-office-365-cloudflare-email-retro-scan/) ו-[Polski](https://blog.cloudflare.com/pl-pl/threats-lurking-office-365-cloudflare-email-retro-scan/).

![See what threats are lurking in your Office 365 with Cloudflare Email Retro Scan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44HXTZY6W122ZVDFV058YX.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA//////387vDw4efr4env6e/07/Dy7+3p/////v7/7PH03Ofv2ebz4ev46e717u3s////////7PP62uj11OX42+n95u367e/x////////8Pf/3uz62Oj+3uz/6fD/8fL2////////+f3/6vP/5vH/6/T/8/f/+Pj7////////////+fz/+Pz//f////////3+////////////////////////////////////////////////////////////////)

אנחנו גאים להכריז שלקוחות Cloudflare יכולים כעת לסרוק הודעות ישנות בתיבות הדואר הנכנס שלהם ב-Office 365 כדי לאתר איומים. הסריקה לאחור תאפשר לכם לבחון את שבעת הימים האחרונים כדי לזהות את האיומים שכלי אבטחת הדוא"ל הנוכחי שלכם החמיץ.

## מדוע להפעיל סריקה לאחור

בשיחות שלנו עם לקוחות, אנו שומעים לעיתים קרובות שהם אינם יודעים מה מצבן של תיבות הדואר הארגוניות שלהם. לארגונים יש כלי לאבטחת מערכת הדוא"ל שלהם, או שהם משתמשים בהגנות המובנות של Microsoft, אבל הם לא מבינים את מידת האפקטיביות של הפתרון הנוכחי שלהם. בבדיקות שאנו עורכים, אנו מוצאים שהכלים האלו מאפשרים להודעות דוא"ל זדוניות לחדור דרך המסננים שלהם לעיתים קרובות, דבר שמגביר את הסיכון להפרת אבטחה בתוך החברה.

כחלק מהניסיון שלנו לשיפור האינטרנט, אנחנו מאפשרים ללקוחות Cloudflare להשתמש בכלי הסריקה לאחור כדי לסרוק הודעות בתוך תיבות הדואר הנכנס שלהם בחינם באמצעות המודלים המתקדמים שלנו של למידת מכונה. הסריקה לאחור שלנו תאתר ותסמן את כל האיומים שנמצא כדי שלקוחות יוכלו לנקות את תיבות הדואר הנכנס שלהם על ידי טיפול בהן במסגרת חשבונות הדוא"ל שלהם. בעזרת המידע הזה, לקוחות יוכלו גם להטמיע בקרות נוספות, כגון שימוש ב-Cloudflare או בפתרון המועדף עליהם כדי למנוע חדירה של איומים דומים לתיבת הדואר שלהם בעתיד.

## הפעלת סריקה לאחור

לקוחות יכולים לעבור אל לוח המחוונים של Cloudflare, שבו, תחת לשונית Area 1, הם יוכלו לראות את אפשרות הסריקה לאחור:

כדי שתוכל לגשת להודעות שיש לסרוק, Cloudflare זקוקה להרשאה לסריקת ההודעות. כדי להתחיל בתהליך, יש להעניק ל-Cloudflare את ההרשאות הדרושות לסריקת הודעות. ההרשאה השנייה תאפשר ליישום Cloudflare לגשת אל ה-Active Directory. גישה זו דרושה כדי להבין מיהם המשתמשים השייכים לארגון ולאילו קבוצות הם שייכים וזאת כדי לעזור לאלגוריתם שלנו להעריך בצורה טובה יותר אם הודעה כלשהי היא זדונית.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2087 Embedded Image - z1Mw1W](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45B0P1WD7XHRVCXSTT5YKK.png&w=715&h=402&f=webp&fit=cover&position=center)

לאחר שכל ההרשאות ניתנו, בשלב האחרון, תתבקשו לבחור את הדומיינים שברצונכם לכלול בסריקה ולספק לנו פרטים בנוגע לספקים האחרים של שירותי אבטחת דוא"ל שמגנים על תיבות הדואר הנכנס שלכם.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2087 Embedded Image - Ub1GiP](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47C2WNHKCCAWM6KSJ7117Y.png&w=715&h=501&f=webp&fit=cover&position=center)

לבסוף, לקוחות יוכלו ללחוץ על "הפעלת סריקה לאחור" (Generate Retro Scan) כדי להתחיל בסריקת הודעות ישנות על ידי Cloudflare Area 1 Email Security. מכיוון שתהליך זה אורך זמן מה, אנחנו שולחים ללקוחות התראה בדוא"ל בתום הסריקה.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2087 Embedded Image - wp2rvP](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46JFBDCB4HTZ5DK09EC6N7.png&w=715&h=585&f=webp&fit=cover&position=center)

ניתוח התוצאות

* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2087 Embedded Image - tuhT7z](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45DX4AHP4SCPW7VD0YT901.png&w=715&h=659&f=webp&fit=cover&position=center)

יוצג לכם פירוט קצר של האיומים שנמצאו בתיבות הדואר הנכנס של הארגון שלכם. החלק העליון מפרט את כל האיומים שאיתרנו לפי סוג. כאן תוכלו למצוא ספירה של הודעות זדוניות וחשודות, הודעות Spoof וזבל והודעות דוא"ל שנשלחו בצובר. אנחנו גם מדגישים את ההודעות החשובות ביותר שיש לבדוק תחת הקטגוריה של הודעות דיוג. תוכלו ללחוץ בכל שלב על הלחצן החיפוש (Search) כדי לקבל פרטים נוספים על הודעות הדוא"ל עם המקוטלגות כך.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2087 Embedded Image - 4CE93n](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45K7CD9047JJ6P0YCK7WRA.png&w=715&h=415&f=webp&fit=cover&position=center)

הדוח יציג גם את עשרת העובדים שנחשפו למספר האיומים הרב ביותר וכן את המקורות הנפוצים ביותר מהם הגיעו האיומים. כל הנתונים הללו נועדו לספק לכם הבנה טובה יותר של המתרחש בתוך תיבת הדואר הנכנס הארגונית שלכם.

## איך מצטרפים

הסריקה לאחור נמצאת כרגע בגרסת בתא סגורה. אם אתם מעוניינים בהפעלת סריקה לאחור בדומיינים של הדוא"ל שלכם ב-Office 365, צרו קשר עם איש הקשר שלכם ב-Cloudflare ואנחנו נוסיף את האפשרות לחשבונכם.

לאחר הפעלת סריקה לאחור וצפייה בתוצאות, תוכלו לבחור לרכוש את Cloudflare Area 1 כדי למנוע חדירה עתידית של איומים לתיבת הדואר הנכנס שלכם, או להגדיר הערכת סיכוני דיוג לקבלת גרסת ניסיון בחינם של מוצר Area 1 למשך 30 ימים. אף על פי שסריקה לאחור היא כלי מצוין כדי לראות את האיומים הרדומים הקיימים, הערכת סיכוני דיוג יכולה לעזור לכם להיחשף בצורה טובה יותר לכל הכלים שיש לנו כדי לשמור על תיבות דואר נקיות מאיומים.

כדי להתחיל, פשוט לחצו על לחצן "בקשת ניסיון" (“Request Trial”) שמופיע בתחתית דוח הסריקה לאחור, מלאו את הטופס המתאים ומישהו מ-Cloudflare ייצור איתכם קשר. לחלופין, תוכלו לפנות באופן ישיר לאיש הקשר שלכם ב-Cloudflare.

בעמוד זה

דיון מקוון

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fhe-il%2Fthreats-lurking-office-365-cloudflare-email-retro-scan%2F&t=%D7%92%D7%9C%D7%95%20%D7%90%D7%99%D7%9C%D7%95%20%D7%90%D7%99%D7%95%D7%9E%D7%99%D7%9D%20%D7%90%D7%95%D7%A8%D7%91%D7%99%D7%9D%20%D7%91-Office%20365%20%D7%A9%D7%9C%D7%9B%D7%9D%20%D7%A2%D7%9D%20%D7%9B%D7%9C%D7%99%20%D7%94%D7%A1%D7%A8%D7%99%D7%A7%D7%94%20%D7%9C%D7%90%D7%97%D7%95%D7%A8%20%28Retro%20Scan%29%20%D7%A9%D7%9C%20Cloudflare%20%D7%A2%D7%91%D7%95%D7%A8%20%D7%94%D7%95%D7%93%D7%A2%D7%95%D7%AA%20%D7%93%D7%95%D7%90%22%D7%9C)[](https://x.com/intent/post?text=%D7%92%D7%9C%D7%95+%D7%90%D7%99%D7%9C%D7%95+%D7%90%D7%99%D7%95%D7%9E%D7%99%D7%9D+%D7%90%D7%95%D7%A8%D7%91%D7%99%D7%9D+%D7%91-Office+365+%D7%A9%D7%9C%D7%9B%D7%9D+%D7%A2%D7%9D+%D7%9B%D7%9C%D7%99+%D7%94%D7%A1%D7%A8%D7%99%D7%A7%D7%94+%D7%9C%D7%90%D7%97%D7%95%D7%A8+%28Retro+Scan%29+%D7%A9%D7%9C+Cloudflare+%D7%A2%D7%91%D7%95%D7%A8+%D7%94%D7%95%D7%93%D7%A2%D7%95%D7%AA+%D7%93%D7%95%D7%90%22%D7%9C&url=https%3A%2F%2Fblog.cloudflare.com%2Fhe-il%2Fthreats-lurking-office-365-cloudflare-email-retro-scan%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fhe-il%2Fthreats-lurking-office-365-cloudflare-email-retro-scan%2F)[](https://bsky.app/intent/compose?text=%D7%92%D7%9C%D7%95+%D7%90%D7%99%D7%9C%D7%95+%D7%90%D7%99%D7%95%D7%9E%D7%99%D7%9D+%D7%90%D7%95%D7%A8%D7%91%D7%99%D7%9D+%D7%91-Office+365+%D7%A9%D7%9C%D7%9B%D7%9D+%D7%A2%D7%9D+%D7%9B%D7%9C%D7%99+%D7%94%D7%A1%D7%A8%D7%99%D7%A7%D7%94+%D7%9C%D7%90%D7%97%D7%95%D7%A8+%28Retro+Scan%29+%D7%A9%D7%9C+Cloudflare+%D7%A2%D7%91%D7%95%D7%A8+%D7%94%D7%95%D7%93%D7%A2%D7%95%D7%AA+%D7%93%D7%95%D7%90%22%D7%9C+https%3A%2F%2Fblog.cloudflare.com%2Fhe-il%2Fthreats-lurking-office-365-cloudflare-email-retro-scan%2F)[](https://mastodonshare.com/?text=%D7%92%D7%9C%D7%95+%D7%90%D7%99%D7%9C%D7%95+%D7%90%D7%99%D7%95%D7%9E%D7%99%D7%9D+%D7%90%D7%95%D7%A8%D7%91%D7%99%D7%9D+%D7%91-Office+365+%D7%A9%D7%9C%D7%9B%D7%9D+%D7%A2%D7%9D+%D7%9B%D7%9C%D7%99+%D7%94%D7%A1%D7%A8%D7%99%D7%A7%D7%94+%D7%9C%D7%90%D7%97%D7%95%D7%A8+%28Retro+Scan%29+%D7%A9%D7%9C+Cloudflare+%D7%A2%D7%91%D7%95%D7%A8+%D7%94%D7%95%D7%93%D7%A2%D7%95%D7%AA+%D7%93%D7%95%D7%90%22%D7%9C&url=https%3A%2F%2Fblog.cloudflare.com%2Fhe-il%2Fthreats-lurking-office-365-cloudflare-email-retro-scan%2F)[](https://www.threads.net/intent/post?text=%D7%92%D7%9C%D7%95+%D7%90%D7%99%D7%9C%D7%95+%D7%90%D7%99%D7%95%D7%9E%D7%99%D7%9D+%D7%90%D7%95%D7%A8%D7%91%D7%99%D7%9D+%D7%91-Office+365+%D7%A9%D7%9C%D7%9B%D7%9D+%D7%A2%D7%9D+%D7%9B%D7%9C%D7%99+%D7%94%D7%A1%D7%A8%D7%99%D7%A7%D7%94+%D7%9C%D7%90%D7%97%D7%95%D7%A8+%28Retro+Scan%29+%D7%A9%D7%9C+Cloudflare+%D7%A2%D7%91%D7%95%D7%A8+%D7%94%D7%95%D7%93%D7%A2%D7%95%D7%AA+%D7%93%D7%95%D7%90%22%D7%9C+https%3A%2F%2Fblog.cloudflare.com%2Fhe-il%2Fthreats-lurking-office-365-cloudflare-email-retro-scan%2F)

## תגיות קשורות

[Birthday Week](https://blog.cloudflare.com/he-il/tag/birthday-week/)

עקבו ברשתות החברתיות

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## הירשמו לקבלת הודעות על פוסטים חדשים

כתובת דוא״ל

לעולם לא נשתף את כתובת האימייל שלך.

הירשם

תודה על ההרשמה! יש לבדוק את תיבת הדואר הנכנס לאישור.
