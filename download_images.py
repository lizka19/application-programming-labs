from icrawler.builtin import GoogleImageCrawler

def download_images(keyword: str, save_path: str, count: int=1000) -> None:
    """
    загружает изображения по ключевым словам
    :param keyword: ключевое слово для поиска
    :param save_path: путь к папке для сохранения
    """
    try:
        google_crawler = GoogleImageCrawler(storage={'root_dir': save_path})
        google_crawler.crawl(keyword=keyword, max_num=count)
    except Exception as e:
        raise Exception(f"Error loading images: {e}")