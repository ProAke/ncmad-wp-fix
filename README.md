# NCMAD WordPress — Local Staging

ชุดนี้ใช้สร้างเว็บ WordPress จำลองสำหรับทดสอบการกู้คืนและซ้อมอัปเกรด **โดยไม่เชื่อมต่อเว็บจริง** ใน repo นี้ยังไม่มีไฟล์เว็บหรือฐานข้อมูลของ `www.ncmad.com`

## เปิดเว็บ WordPress เปล่าบนเครื่องตัวเอง

ต้องมี Docker Engine/Desktop รุ่นปัจจุบัน (Engine 28 ขึ้นไป), Docker Compose v2 และ Python 3 รันคำสั่งจากโฟลเดอร์ที่มี `compose.yaml`:

```sh
python3 staging/init_env.py
docker compose config --quiet
docker compose up -d --wait gateway
```

บน Windows ใช้ `py -3 staging/init_env.py` ได้ หากไม่มีคำสั่ง `python3` เปิด **http://127.0.0.1:8088** จากเครื่องที่รัน Docker แล้วสร้างผู้ดูแลด้วยรหัสผ่านสำหรับเว็บจำลองเท่านั้น หากจะนำเข้าข้อมูลสำรอง ให้ใช้ขั้นตอนในคู่มือแทนการกดติดตั้ง WordPress เปล่าในฐานข้อมูลเดียวกัน

- มีเพียง gateway ที่เปิดพอร์ต และผูกกับ `127.0.0.1` เท่านั้น ไม่เปิดพอร์ตฐานข้อมูลหรือ Apache ออกมาที่ host อย่าใช้ tunnel หรือ port forwarding เผยแพร่ staging
- WordPress/DB/WP-CLI อยู่ในเครือข่าย Docker แบบ internal; WordPress ปิด WP-Cron และบล็อก HTTP requests ภายนอกผ่าน WordPress API ส่วนปลั๊กอินจำลองบล็อก `wp_mail()` และ gateway จำกัดการโหลดทรัพยากรภายนอกในเบราว์เซอร์ มาตรการเหล่านี้ไม่ใช่ sandbox สำหรับรันโค้ดที่ไม่น่าไว้ใจ เพราะบางปลั๊กอินอาจใช้ช่องทางอื่นหรือมีลิงก์/redirect ออกนอกเว็บ
- อิมเมจเริ่มต้นเป็นค่าเพื่อเปิดเว็บเปล่า ไม่ใช่ข้อสรุปว่าเข้ากับเว็บจริง ให้ระบุเวอร์ชันจาก inventory ก่อนทดสอบอัปเกรด
- ปิดด้วย `docker compose down` ข้อมูลใน volumes ยังอยู่ ไม่ต้องลบ `.env` ระหว่างใช้งาน เพราะรหัสผ่านฐานข้อมูลถูกตั้งครั้งแรกที่สร้าง volume

[คู่มือนำเข้าข้อมูล ซ้อมอัปเกรด ตรวจความเสี่ยง และวางแผน rollback](docs/staging-and-review.th.md)
