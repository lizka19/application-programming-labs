import csv
import os
from pathlib import Path

class SimpleIterator:
    def __init__(self, annotation_path: str) -> None:
        self.ap = annotation_path
        self.list = self.download_img()
        self.limit = len(self.list)
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self) -> str:
        if self.counter < self.limit:
            result = self.list[self.counter]
            self.counter += 1
            return result
        else:
            raise StopIteration

    def download_img(self) -> list:
        if os.path.isfile(self.ap):
            with open(self.ap, mode='r', encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader)
                image_paths = [row[0] for row in reader]
                return image_paths

        if os.path.isdir(self.ap):
            image_paths = [str(p) for p in Path(self.ap).glob('*.*') if p.is_file()]
            return image_paths
        raise FileNotFoundError(f"Path '{self.ap}' is not a file or directory.")


