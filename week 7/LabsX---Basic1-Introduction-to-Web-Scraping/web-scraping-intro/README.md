# Web Scraping Intro

โปรเจกต์ตัวอย่างการทำ Web Scraping เบื้องต้นด้วย Python โดยใช้ `requests` และ `BeautifulSoup`
ดึงข้อมูลชื่อหนังสือและรายชื่อบทจากเว็บ <https://automatetheboringstuff.com/3e/>

## โครงสร้างโปรเจกต์

```
web-scraping-intro/
├── src/
│   ├── __init__.py
│   └── scraper.py      # คลาส SimpleWebScraper
├── main.py             # จุดเริ่มรันโปรแกรม
├── requirements.txt
├── .gitignore
└── README.md
```

## วิธีติดตั้ง

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## วิธีรัน

```powershell
python main.py
```

## ตัวอย่างผลลัพธ์

```
กำลังดาวน์โหลดเนื้อหาจาก: https://automatetheboringstuff.com/3e/
ดาวน์โหลดเนื้อหาสำเร็จ

--- ข้อมูลที่ Scrape ได้ ---
ชื่อหนังสือ: 3rd Edition

ชื่อบทต่างๆ:
1. Introduction
2. Chapter 1 - Python Basics
3. Chapter 2 - if-else and Flow Control
...
27. Appendix B - Answers to the Practice Questions
--------------------
```

## การทำงานของ `SimpleWebScraper`

- `fetch_content()` ดาวน์โหลดหน้าเว็บและแปลงเป็น BeautifulSoup
- `scrape_main_titles()` ดึงชื่อหนังสือจาก `article > header > h1` และรายชื่อบทจากลิงก์สารบัญ
