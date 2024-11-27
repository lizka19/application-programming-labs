import os

from icrawler.builtin import GoogleImageCrawler



def download_images(keyword: str, save_path: str) -> None:
    """
    загружает изображение по ключевым словам
    """
    try:
        google_crawler = GoogleImageCrawler(storage={'root_dir': save_path})
        google_crawler.crawl(keyword=keyword, max_num=1000)
    except Exception as e:
        raise Exception(f"Error loading images: {e}")