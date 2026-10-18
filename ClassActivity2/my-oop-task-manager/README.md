
# 🏛️ Week 8: Object-Oriented Programming (OOP) Fundamentals & Refactoring the CLI Task Manager

[](https://github.com/sapphanyu/Class_activity_2_Object_Oriented_Programmin_OOP_Fundamentals_Refactoring_the_CLI_Task_Manager/tree/main/my-oop-task-manager#%EF%B8%8F-week-8-object-oriented-programming-oop-fundamentals--refactoring-the-cli-task-manager)

> **รายวิชา:** การเขียนโปรแกรมคอมพิวเตอร์ / วิศวกรรมซอฟต์แวร์ (ระดับปริญญาตรี ชั้นปีที่ 2)
> **หัวข้อประจำสัปดาห์:** สัปดาห์ที่ 8 — การเขียนโปรแกรมเชิงวัตถุพื้นฐานและการปรับปรุงโค้ดระบบจัดการงาน CLI
> **Repository:** `Week-8-Object-Oriented-Programming`

---

## 📌 1. ภาพรวมของคลังโค้ด (Repository Overview)

[](https://github.com/sapphanyu/Class_activity_2_Object_Oriented_Programmin_OOP_Fundamentals_Refactoring_the_CLI_Task_Manager/tree/main/my-oop-task-manager#-1-%E0%B8%A0%E0%B8%B2%E0%B8%9E%E0%B8%A3%E0%B8%A7%E0%B8%A1%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B8%84%E0%B8%A5%E0%B8%B1%E0%B8%87%E0%B9%82%E0%B8%84%E0%B9%89%E0%B8%94-repository-overview)

คลังโค้ดนี้รวบรวมสื่อการเรียนการสอน, ชุดแบบฝึกหัดปฏิบัติการ (Lab Package), โค้ดตั้งต้นสำหรับนักศึกษา (Starter Code), เฉลยฉบับสมบูรณ์ (Reference Solution), และสมุดงานสำหรับ Google Colab ในหัวข้อการเขียนโปรแกรมเชิงวัตถุ (Object-Oriented Programming: OOP)

ในสัปดาห์นี้ นักศึกษาจะได้เรียนรู้การเปลี่ยนผ่านจาก **Procedural Programming** (ในสัปดาห์ที่ 7 ที่ใช้ `dict` และฟังก์ชันแยกส่วน) สู่การสร้างระบบด้วย **Class และ Object** ตามหลักการ Software Engineering สากล

---

## 📂 2. โครงสร้างภายในคลังโค้ด (Repository Structure)

[](https://github.com/sapphanyu/Class_activity_2_Object_Oriented_Programmin_OOP_Fundamentals_Refactoring_the_CLI_Task_Manager/tree/main/my-oop-task-manager#-2-%E0%B9%82%E0%B8%84%E0%B8%A3%E0%B8%87%E0%B8%AA%E0%B8%A3%E0%B9%89%E0%B8%B2%E0%B8%87%E0%B8%A0%E0%B8%B2%E0%B8%A2%E0%B9%83%E0%B8%99%E0%B8%84%E0%B8%A5%E0%B8%B1%E0%B8%87%E0%B9%82%E0%B8%84%E0%B9%89%E0%B8%94-repository-structure)

```
Week-8-Object-Oriented-Programming/
├── starter_code/                     # 🧑‍💻 ชุดปฏิบัติการสำหรับแจกนักศึกษา (มี TODOs & Tests)
│   ├── src/
│   │   ├── __init__.py
│   │   ├── task.py                   # คลาส Task พร้อมคำอธิบายและจุด TODO
│   │   └── task_manager.py           # คลาส TaskManager พร้อมระบบจัดการข้อมูล
│   ├── tests/
│   │   ├── test_task.py              # Automated Unit Tests สำหรับคลาส Task
│   │   └── test_task_manager.py      # Automated Unit Tests สำหรับคลาส TaskManager
│   ├── data/
│   │   └── tasks.json                # ไฟล์ข้อมูลเริ่มต้น
│   ├── main.py                       # หน้าจอเมนู CLI โต้ตอบ
│   └── README.md                     # 📖 คู่มือแล็บฉบับละเอียดสำหรับนักศึกษา (ภาษาไทย)
│
├── solution/                         # 👨‍🏫 โค้ดเฉลยฉบับสมบูรณ์สำหรับอาจารย์/ผู้ช่วยสอน (TA)
│   ├── src/
│   ├── tests/
│   ├── data/
│   ├── main.py
│   └── README.md
│
├── colab/                            # ☁️ สมุดงาน Jupyter Notebook สำหรับ Google Colab
│   └── Week8_OOP_TaskManager_Lab.ipynb
│
├── Week 8_ ... .docx                 # เอกสารคำบรรยายต้นฉบับของผู้สอน
├── .gitignore                        # กฎการคัดกรองไฟล์สำหรับ Git
└── README.md                         # เอกสารหน้าแรกของคลังโค้ด (ไฟล์นี้)
```

---

## 🎯 3. สาระสำคัญและแนวคิดที่ได้เรียนรู้ (Key Learning Concepts)

[](https://github.com/sapphanyu/Class_activity_2_Object_Oriented_Programmin_OOP_Fundamentals_Refactoring_the_CLI_Task_Manager/tree/main/my-oop-task-manager#-3-%E0%B8%AA%E0%B8%B2%E0%B8%A3%E0%B8%B0%E0%B8%AA%E0%B8%B3%E0%B8%84%E0%B8%B1%E0%B8%8D%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B9%81%E0%B8%99%E0%B8%A7%E0%B8%84%E0%B8%B4%E0%B8%94%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B9%84%E0%B8%94%E0%B9%89%E0%B9%80%E0%B8%A3%E0%B8%B5%E0%B8%A2%E0%B8%99%E0%B8%A3%E0%B8%B9%E0%B9%89-key-learning-concepts)

1. **Classes & Objects (พิมพ์เขียวและอินสแตนซ์):**
   * การสร้างคลาส `Task` เป็นตัวแทนข้อมูลงานแต่ละรายการ
   * การสร้างคลาส `TaskManager` ทำหน้าที่จัดการคอลเลกชันของงาน
2. **Constructor (`__init__`) และพารามิเตอร์ `self`:**
   * การกำหนด State ให้กับแต่ละ Instance ผ่าน `self.id`, `self.description`, `self.completed`
   * การเข้าใจบทบาทของ `self` ในฐานะตัวแทนของ Object ปัจจุบัน
3. **การห่อหุ้มข้อมูลและพฤติกรรม (Encapsulation):**
   * รวมข้อมูล (Attributes) และฟังก์ชันการทำงาน (Methods เช่น `mark_complete()`) เข้าไว้ในคลาสเดียวกัน
4. **Dunder / Magic Methods:**
   * `__str__`: สำหรับการแสดงผลที่เข้าใจง่ายแก่ผู้ใช้ทั่วไป (`print(task)`)
   * `__repr__`: สำหรับการแสดงผลเชิงเทคนิคเพื่อการ Debugging
5. **Data Persistence & OOP (Serialization / Deserialization):**
   * แปลง Object เป็น Dictionary (`task.to_dict()`) เพื่อบันทึกลงไฟล์ JSON
   * โหลดข้อมูลจากไฟล์ JSON กลับมาสร้างเป็น `Task` Object ในหน่วยความจำ

---

## 🚀 4. คำแนะนำการใช้งาน (Quick Start Guide)

[](https://github.com/sapphanyu/Class_activity_2_Object_Oriented_Programmin_OOP_Fundamentals_Refactoring_the_CLI_Task_Manager/tree/main/my-oop-task-manager#-4-%E0%B8%84%E0%B8%B3%E0%B9%81%E0%B8%99%E0%B8%B0%E0%B8%99%E0%B8%B3%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%83%E0%B8%8A%E0%B9%89%E0%B8%87%E0%B8%B2%E0%B8%99-quick-start-guide)

### สำหรับนักศึกษา (Students):

[](https://github.com/sapphanyu/Class_activity_2_Object_Oriented_Programmin_OOP_Fundamentals_Refactoring_the_CLI_Task_Manager/tree/main/my-oop-task-manager#%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%99%E0%B8%B1%E0%B8%81%E0%B8%A8%E0%B8%B6%E0%B8%81%E0%B8%A9%E0%B8%B2-students)

1. เข้าไปที่โฟลเดอร์ [`starter_code/`](https://github.com/sapphanyu/Class_activity_2_Object_Oriented_Programmin_OOP_Fundamentals_Refactoring_the_CLI_Task_Manager/blob/main/my-oop-task-manager/starter_code)
2. อ่านคู่มือการปฏิบัติการฉบับเต็มได้ที่ [`starter_code/README.md`](https://github.com/sapphanyu/Class_activity_2_Object_Oriented_Programmin_OOP_Fundamentals_Refactoring_the_CLI_Task_Manager/blob/main/my-oop-task-manager/starter_code/README.md)
3. ลงมือเติมโค้ดในไฟล์ `src/task.py` และ `src/task_manager.py` ตามจุด `# TODO`
4. ทดสอบความถูกต้องด้วยตนเองผ่านคำสั่ง:
   ```shell
   cd starter_code
   python -m unittest discover tests
   ```
5. เมื่อเทสต์ผ่านครบทุกกรณี ให้รันโปรแกรมเพื่อทดสอบ CLI:
   ```shell
   python main.py
   ```

### สำหรับผู้สอนและผู้ช่วยสอน (Instructors / TAs):

[](https://github.com/sapphanyu/Class_activity_2_Object_Oriented_Programmin_OOP_Fundamentals_Refactoring_the_CLI_Task_Manager/tree/main/my-oop-task-manager#%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%9C%E0%B8%B9%E0%B9%89%E0%B8%AA%E0%B8%AD%E0%B8%99%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%9C%E0%B8%B9%E0%B9%89%E0%B8%8A%E0%B9%88%E0%B8%A7%E0%B8%A2%E0%B8%AA%E0%B8%AD%E0%B8%99-instructors--tas)

* สามารถดูโค้ดเฉลยฉบับสมบูรณ์และการตั้งค่าทั้งหมดได้ในโฟลเดอร์ [`solution/`](https://github.com/sapphanyu/Class_activity_2_Object_Oriented_Programmin_OOP_Fundamentals_Refactoring_the_CLI_Task_Manager/blob/main/my-oop-task-manager/solution)
* รันชุดทดสอบความถูกต้องของเฉลยทั้งหมด:
  ```shell
  cd solution
  python -m unittest discover tests
  ```

### สำหรับการรันบน Google Colab:

[](https://github.com/sapphanyu/Class_activity_2_Object_Oriented_Programmin_OOP_Fundamentals_Refactoring_the_CLI_Task_Manager/tree/main/my-oop-task-manager#%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%A3%E0%B8%B1%E0%B8%99%E0%B8%9A%E0%B8%99-google-colab)

* เปิดไฟล์ [`colab/Week8_OOP_TaskManager_Lab.ipynb`](https://github.com/sapphanyu/Class_activity_2_Object_Oriented_Programmin_OOP_Fundamentals_Refactoring_the_CLI_Task_Manager/blob/main/my-oop-task-manager/colab/Week8_OOP_TaskManager_Lab.ipynb) บน Google Colab เพื่อรันและทดลองสร้างไฟล์แบบออนไลน์ได้ทันที

---

## 📄 ลิขสิทธิ์และสัญญาอนุญาต (License)

[](https://github.com/sapphanyu/Class_activity_2_Object_Oriented_Programmin_OOP_Fundamentals_Refactoring_the_CLI_Task_Manager/tree/main/my-oop-task-manager#-%E0%B8%A5%E0%B8%B4%E0%B8%82%E0%B8%AA%E0%B8%B4%E0%B8%97%E0%B8%98%E0%B8%B4%E0%B9%8C%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%AA%E0%B8%B1%E0%B8%8D%E0%B8%8D%E0%B8%B2%E0%B8%AD%E0%B8%99%E0%B8%B8%E0%B8%8D%E0%B8%B2%E0%B8%95-license)

สื่อการเรียนการสอนนี้เผยแพร่เพื่อการศึกษาภายใต้ [MIT License](https://opensource.org/licenses/MIT)
