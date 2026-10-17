from src.scraper import SimpleWebScraper

URL = "https://automatetheboringstuff.com/3e/"


def main():
    scraper = SimpleWebScraper(URL)

    if not scraper.fetch_content():
        return

    data = scraper.scrape_main_titles()
    if not data:
        print("ไม่พบข้อมูลที่ต้องการ")
        return

    print("\n--- ข้อมูลที่ Scrape ได้ ---")
    print(f"ชื่อหนังสือ: {data['book_title']}")

    print("\nชื่อบทต่างๆ:")
    for index, title in enumerate(data["chapter_titles"], start=1):
        print(f"{index}. {title}")
    print("--------------------")


if __name__ == "__main__":
    main()
