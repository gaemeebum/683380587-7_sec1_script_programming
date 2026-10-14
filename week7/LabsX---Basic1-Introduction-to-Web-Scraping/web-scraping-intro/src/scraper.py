import re

import requests
from bs4 import BeautifulSoup


class SimpleWebScraper:
    """Scraper อย่างง่ายสำหรับดึงชื่อหนังสือและรายชื่อบทจากเว็บ"""

    CHAPTER_PATTERN = re.compile(r"^(Introduction|Chapter\s+\d+|Appendix\s+[A-Z])\b")

    def __init__(self, url):
        self.url = url
        self.soup = None

    def fetch_content(self):
        """ดาวน์โหลดเนื้อหา HTML จาก URL แล้วแปลงเป็น BeautifulSoup"""
        print(f"กำลังดาวน์โหลดเนื้อหาจาก: {self.url}")
        try:
            response = requests.get(
                self.url,
                headers={"User-Agent": "Mozilla/5.0 (web-scraping-intro lab)"},
                timeout=15,
            )
            response.raise_for_status()
        except requests.exceptions.RequestException as error:
            print(f"ดาวน์โหลดเนื้อหาไม่สำเร็จ: {error}")
            return False

        response.encoding = response.apparent_encoding
        self.soup = BeautifulSoup(response.text, "html.parser")
        print("ดาวน์โหลดเนื้อหาสำเร็จ")
        return True

    def scrape_main_titles(self):
        """ดึงชื่อหนังสือ (h1 ใน header ของ article) และรายชื่อบทต่างๆ"""
        if self.soup is None:
            return None

        # --- ชื่อหนังสือ ---
        book_title = None
        article_tag = self.soup.find("article")
        if article_tag:
            header_tag = article_tag.find("header")
            if header_tag:
                h1_tag = header_tag.find("h1")
                if h1_tag:
                    book_title = h1_tag.get_text(strip=True)

        # fallback: ถ้าไม่พบ article > header > h1 ให้ใช้ h1 ตัวแรกของหน้า
        if book_title is None:
            first_h1 = self.soup.find("h1")
            if first_h1:
                book_title = first_h1.get_text(strip=True)

        # --- ชื่อบทต่างๆ (จากลิงก์/รายการในสารบัญ) ---
        chapter_titles = []
        scope = article_tag if article_tag else self.soup
        for tag in scope.find_all(["a", "li"]):
            text = " ".join(tag.get_text(" ", strip=True).split())
            if self.CHAPTER_PATTERN.match(text) and text not in chapter_titles:
                chapter_titles.append(text)

        return {"book_title": book_title, "chapter_titles": chapter_titles}
